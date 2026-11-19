"""Read one input film and derive the timeline the handheld motion follows.

Everything comes from the input itself (cut times will differ between edits):
  - shot cuts      : colour-histogram distance between frames on a 256x144 proxy
  - luma flashes   : sudden rises of mean luma that are not cuts (spells, glows)
  - audio onsets   : spectral-flux onset strength, peaks over an adaptive threshold
  - rumble         : sustained low-band (<180 Hz) energy bursts (the worm)
  - speech         : voice-band energy with syllabic (3-8 Hz) modulation, low flux
All per-frame curves are returned at the video frame rate.
"""
import json
import subprocess

import numpy as np

PW, PH = 256, 144          # analysis proxy size
SR = 24000                 # analysis sample rate


def probe(path):
    out = subprocess.run(
        ["ffprobe", "-v", "error", "-show_streams", "-show_format", "-of", "json", path],
        check=True, capture_output=True, text=True).stdout
    info = json.loads(out)
    v = next(s for s in info["streams"] if s["codec_type"] == "video")
    a = next((s for s in info["streams"] if s["codec_type"] == "audio"), None)
    num, den = (int(x) for x in v["r_frame_rate"].split("/"))
    fps = num / den
    nb = int(v.get("nb_frames") or 0)
    dur = float(v.get("duration") or info["format"]["duration"])
    if not nb:
        nb = int(round(dur * fps))
    return {"width": int(v["width"]), "height": int(v["height"]), "fps": fps,
            "fps_str": v["r_frame_rate"], "frames": nb, "duration": dur,
            "has_audio": a is not None,
            "color": {k: v.get(k) for k in ("color_space", "color_transfer", "color_primaries", "color_range")}}


def read_proxy(path, nframes):
    cmd = ["ffmpeg", "-v", "error", "-i", path, "-an",
           "-vf", f"scale={PW}:{PH}:flags=area:in_color_matrix=bt709,format=rgb24",
           "-f", "rawvideo", "-"]
    raw = subprocess.run(cmd, check=True, capture_output=True).stdout
    n = len(raw) // (PW * PH * 3)
    return np.frombuffer(raw[: n * PW * PH * 3], np.uint8).reshape(n, PH, PW, 3)


def read_audio(path):
    cmd = ["ffmpeg", "-v", "error", "-i", path, "-vn", "-ac", "1", "-ar", str(SR), "-f", "f32le", "-"]
    raw = subprocess.run(cmd, check=True, capture_output=True).stdout
    return np.frombuffer(raw, np.float32).copy()


def smooth(x, sigma):
    if sigma <= 0:
        return x
    r = int(np.ceil(3 * sigma))
    k = np.exp(-0.5 * (np.arange(-r, r + 1) / sigma) ** 2)
    k /= k.sum()
    xp = np.pad(x, r, mode="edge")
    return np.convolve(xp, k, mode="valid")


def peaks(x, thr, min_gap):
    """Local maxima of x above thr (array or scalar), at least min_gap samples apart (strongest wins)."""
    thr = np.broadcast_to(thr, x.shape)
    cand = np.where((x[1:-1] > x[:-2]) & (x[1:-1] >= x[2:]) & (x[1:-1] > thr[1:-1]))[0] + 1
    cand = cand[np.argsort(-x[cand])]
    keep = []
    for c in cand:
        if all(abs(c - k) >= min_gap for k in keep):
            keep.append(c)
    return sorted(keep)


def video_curves(frames):
    n = len(frames)
    f = frames.astype(np.float32) / 255.0
    luma = (0.2126 * f[..., 0] + 0.7152 * f[..., 1] + 0.0722 * f[..., 2])
    ymean = luma.mean(axis=(1, 2))
    # 4x4x4 colour histograms + 2x2 spatial luma grid, for cut detection
    q = (frames // 64).astype(np.int32)
    idx = q[..., 0] * 16 + q[..., 1] * 4 + q[..., 2]
    hist = np.stack([np.bincount(i.ravel(), minlength=64) for i in idx]).astype(np.float32)
    hist /= hist.sum(axis=1, keepdims=True)
    hd = np.zeros(n, np.float32)
    hd[1:] = 0.5 * np.abs(hist[1:] - hist[:-1]).sum(axis=1)
    grid = luma.reshape(n, 4, PH // 4, 4, PW // 4).mean(axis=(2, 4)).reshape(n, 16)
    gd = np.zeros(n, np.float32)
    gd[1:] = np.abs(grid[1:] - grid[:-1]).mean(axis=1)
    # green-glow measure: share of bright, green-dominant pixels (spell light)
    g = f[..., 1]
    green = ((g > 0.45) & (g > f[..., 0] * 1.25) & (g > f[..., 2] * 1.1)).mean(axis=(1, 2))
    return ymean, hd, gd, green


def detect_cuts(hd, gd, fps):
    score = hd + 2.0 * gd
    base = smooth(np.abs(score), fps * 0.5)
    # a cut is a one-frame spike well above its neighbourhood
    loc = np.maximum(np.r_[score[0], score[:-1]], np.r_[score[1:], score[-1]])
    cand = np.where((score > 0.22) & (score > 2.5 * base) & (score >= loc))[0]
    cuts = []
    for c in cand:
        if c < 2:
            continue
        if cuts and c - cuts[-1] < int(0.4 * fps):
            if score[c] > score[cuts[-1]]:
                cuts[-1] = int(c)
            continue
        cuts.append(int(c))
    return cuts, score


def audio_curves(a, fps, nframes):
    hop = int(round(SR / fps / 4))            # 4 analysis hops per video frame
    win = 1024
    nh = max(1, (len(a) - win) // hop + 1)
    idx = np.arange(win)[None, :] + hop * np.arange(nh)[:, None]
    seg = a[idx] * np.hanning(win)[None, :].astype(np.float32)
    mag = np.abs(np.fft.rfft(seg, axis=1)).astype(np.float32)
    freqs = np.fft.rfftfreq(win, 1 / SR)
    logm = np.log1p(100 * mag)
    flux = np.maximum(0, np.diff(logm, axis=0, prepend=logm[:1])).sum(axis=1)
    hf = freqs > 1500
    flux_hi = np.maximum(0, np.diff(logm[:, hf], axis=0, prepend=logm[:1, hf])).sum(axis=1)
    e_low = (mag[:, freqs < 180] ** 2).sum(axis=1)
    e_voice = (mag[:, (freqs > 250) & (freqs < 3500)] ** 2).sum(axis=1)
    e_all = (mag ** 2).sum(axis=1) + 1e-9

    def to_frames(x, how="mean"):
        m = nframes * 4
        x = np.pad(x, (0, max(0, m - len(x))), mode="edge")[:m].reshape(nframes, 4)
        return x.max(axis=1) if how == "max" else x.mean(axis=1)

    onset = to_frames(flux, "max")
    onset_hi = to_frames(flux_hi, "max")
    rms = np.sqrt(to_frames(e_all) / win)
    low = to_frames(e_low) / to_frames(e_all)
    voice = to_frames(e_voice) / to_frames(e_all)
    # syllabic modulation: voice-band envelope band-passed 3-8 Hz around each frame
    venv = np.sqrt(to_frames(e_voice))
    venv_db = 20 * np.log10(venv + 1e-6)
    bp = smooth(venv_db, fps / (2 * np.pi * 8)) - smooth(venv_db, fps / (2 * np.pi * 3))
    syll = np.sqrt(smooth(bp ** 2, fps * 0.25))
    return {"onset": onset, "onset_hi": onset_hi, "rms": rms, "low": low,
            "voice": voice, "syll": syll, "e_low": to_frames(e_low)}


def analyze(path, log=print):
    info = probe(path)
    fps, n = info["fps"], info["frames"]
    log(f"analyze: {info['width']}x{info['height']} {fps:g} fps, {n} frames, {info['duration']:.3f} s")
    frames = read_proxy(path, n)
    n = min(n, len(frames))
    frames = frames[:n]
    ymean, hd, gd, green = video_curves(frames)
    cuts, cut_score = detect_cuts(hd, gd, fps)
    near_cut = np.zeros(n, bool)
    for c in cuts:
        near_cut[max(0, c - 1): c + 3] = True

    events = [{"t": c / fps, "frame": c, "kind": "cut", "strength": float(min(1, cut_score[c]))} for c in cuts]

    # luma flashes and green glow rises (spells), not on cuts
    ys = smooth(ymean, 0.6)
    dy = np.r_[0, np.diff(ys)]
    rise = np.maximum(0, ys - smooth(ymean, fps * 0.6))
    gs = smooth(green, 0.6)
    grise = np.r_[0, np.diff(gs)]
    flash_score = np.maximum(dy / 0.03, rise / 0.06) + np.maximum(0, grise) / 0.01
    flash_score[near_cut] = 0
    for p in peaks(flash_score, 1.0, int(0.5 * fps)):
        events.append({"t": p / fps, "frame": int(p), "kind": "flash",
                       "strength": float(np.clip(flash_score[p] / 3.0, 0.3, 1.0))})

    curves = {"luma": ymean, "green": green, "cut_score": cut_score, "flash_score": flash_score}
    if info["has_audio"]:
        a = read_audio(path)
        ac = audio_curves(a, fps, n)
        on = ac["onset_hi"] * 0.5 + ac["onset"] * 0.5
        on_n = on / (np.median(on) + 1e-9)
        med = smooth(on_n, fps * 1.0)
        mad = smooth(np.abs(on_n - med), fps * 1.0)
        thr = np.maximum(med + 3.5 * mad, 2.3)
        # transients: sharp, loud, not part of syllabic speech
        loud = ac["rms"] / (np.percentile(ac["rms"], 90) + 1e-9)
        hits = peaks(on_n * np.clip(loud, 0.2, 2.0), thr * 0.9, int(0.30 * fps))
        for p in hits:
            s = float(np.clip((on_n[p] - thr[p]) / (2.5 * thr[p]) + 0.35, 0.25, 1.0))
            events.append({"t": p / fps, "frame": int(p), "kind": "impact", "strength": s})
        # rumble: low band holds a large share of a loud signal for > 0.5 s
        lowloud = smooth(ac["low"] * np.clip(loud, 0, 2), fps * 0.15)
        rum = lowloud > max(0.35, np.percentile(lowloud, 90))
        start = None
        for i in range(n + 1):
            on_ = i < n and rum[i]
            if on_ and start is None:
                start = i
            elif not on_ and start is not None:
                if i - start >= int(0.5 * fps):
                    events.append({"t": start / fps, "frame": int(start), "kind": "rumble",
                                   "strength": float(np.clip(lowloud[start:i].mean() / 0.6, 0.3, 1.0)),
                                   "end": i / fps})
                start = None
        # speech-like: voice band dominant, syllabic modulation, moderate level, not a hit
        vz = (ac["voice"] - 0.42) / 0.3
        sz = (ac["syll"] - 1.3) / 1.5
        speech_raw = np.clip(0.65 * vz + 0.35 * sz, 0, 1) * (loud > 0.12)
        speech = np.clip(smooth(speech_raw, fps * 0.35) * 1.6, 0, 1)
        curves.update({"onset": on_n, "onset_thr": thr, "rms": ac["rms"], "low": ac["low"],
                       "voice": ac["voice"], "syll": ac["syll"], "speech": speech})
        # speech stretches as events too (for the json)
        sp = speech > 0.5
        start = None
        for i in range(n + 1):
            on_ = i < n and sp[i]
            if on_ and start is None:
                start = i
            elif not on_ and start is not None:
                if i - start >= int(0.6 * fps):
                    events.append({"t": start / fps, "frame": int(start), "kind": "speech",
                                   "end": i / fps, "strength": float(speech[start:i].mean())})
                start = None
    else:
        curves["speech"] = np.zeros(n)

    events.sort(key=lambda e: e["t"])
    info["frames"] = n
    return info, events, curves
