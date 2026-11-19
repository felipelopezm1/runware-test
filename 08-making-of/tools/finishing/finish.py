#!/usr/bin/env python3
"""finish.py: the finishing pass. One input film in; a handheld-camera pass, then a CRT finish on top.

  finish.py --in SRC --name NAME --out-dir DIR [--height 2160 --height 1080]
            [--handheld-only | --crt-only] [--start S --duration D] [--seed N] [knobs ...]

Stages (each writes into --out-dir):
  1 analyze   NAME-motion.json      cuts, flashes, impacts, rumbles, speech stretches, knobs, stats
              NAME-curve.csv        per frame: t, dx, dy (output px at the source height), rot, scale, margin, envelopes
              NAME-curve.png        the curve plotted, events marked
  2 handheld  NAME-handheld-<H>p.mp4  x264 CRF 14 (an intermediate), audio copied
  3 crt       NAME-crt-<H>p.mp4       x264 CRF 16 for every --height, audio copied
              NAME-look.cube          the warm film LUT the CRT stage applies

The handheld pass is rendered once, at the largest requested height; every CRT copy is made from it
(scaled with lanczos first when smaller), so the 1080p copy gets its own scanlines, never downscaled ones.
Audio is copied untouched. Run with the venv next to this file: tools/.venv/bin/python tools/finish.py ...
"""
import argparse
import csv
import json
import os
import queue
import subprocess
import sys
import threading
import time

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import analyze  # noqa: E402
import motion  # noqa: E402

COLOR_TAGS = ["-colorspace", "bt709", "-color_primaries", "bt709", "-color_trc", "bt709", "-color_range", "tv"]
SWS = "flags=lanczos+accurate_rnd+full_chroma_int"


def log(*a):
    print(time.strftime("%H:%M:%S"), *a, flush=True)


def even(x):
    return int(round(x / 2)) * 2


# --- pipes ------------------------------------------------------------------------------------

def decoder(src, W, H, start, dur, pre_vf=None, sws=SWS):
    vf = f"scale={W}:{H}:{sws}:in_color_matrix=bt709:in_range=tv:out_range=full,format=rgb24"
    if pre_vf:
        vf += "," + pre_vf
    cmd = ["ffmpeg", "-v", "error", "-nostdin"]
    if start:
        cmd += ["-ss", f"{start:.6f}"]
    cmd += ["-i", src]
    if dur:
        cmd += ["-t", f"{dur:.6f}"]
    cmd += ["-an", "-vf", vf, "-f", "rawvideo", "-pix_fmt", "rgb24", "-"]
    return subprocess.Popen(cmd, stdout=subprocess.PIPE, bufsize=0)


def encoder(out, W, H, fps_str, audio_src, start, dur, crf, preset):
    cmd = ["ffmpeg", "-v", "error", "-nostdin", "-y",
           "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r", fps_str, "-i", "-"]
    if audio_src:
        if start:
            cmd += ["-ss", f"{start:.6f}"]
        cmd += ["-i", audio_src]
        if dur:
            cmd += ["-t", f"{dur:.6f}"]
    cmd += ["-map", "0:v:0"]
    if audio_src:
        cmd += ["-map", "1:a:0?", "-c:a", "copy"]
    cmd += ["-vf", f"scale={W}:{H}:{SWS}:in_range=full:out_color_matrix=bt709:out_range=tv,format=yuv420p",
            "-c:v", "libx264", "-preset", preset, "-crf", str(crf), "-tune", "film",
            "-x264-params", "aq-mode=3", *COLOR_TAGS, "-movflags", "+faststart", "-shortest", out]
    return subprocess.Popen(cmd, stdin=subprocess.PIPE, bufsize=0)


def run_pipe(dec, enc, W, H, n_expected, fn, label):
    """reader thread -> fn (cv2 releases the GIL) -> writer thread."""
    fsz = W * H * 3
    qin, qout = queue.Queue(8), queue.Queue(8)
    t_fn = [0.0]

    def reader():
        while True:
            buf = bytearray(fsz)
            mv = memoryview(buf)
            got = 0
            while got < fsz:
                r = dec.stdout.readinto(mv[got:])
                if not r:
                    break
                got += r
            if got < fsz:
                qin.put(None)
                return
            qin.put(np.frombuffer(buf, np.uint8).reshape(H, W, 3))

    def writer():
        while True:
            fr = qout.get()
            if fr is None:
                break
            enc.stdin.write(memoryview(np.ascontiguousarray(fr)).cast("B"))
        enc.stdin.close()

    tr, tw = threading.Thread(target=reader, daemon=True), threading.Thread(target=writer, daemon=True)
    tr.start(), tw.start()
    i, t0 = 0, time.time()
    while True:
        fr = qin.get()
        if fr is None:
            break
        a = time.time()
        qout.put(fn(i, fr))
        t_fn[0] += time.time() - a
        i += 1
        if i % 120 == 0:
            el = time.time() - t0
            log(f"  {label}: {i}/{n_expected} frames, {i / el:.1f} fps")
    qout.put(None)
    tw.join()
    dec.wait()
    rc = enc.wait()
    if rc != 0:
        raise SystemExit(f"{label}: encoder failed ({rc})")
    return i, time.time() - t0, t_fn[0]


# --- stages -----------------------------------------------------------------------------------

def stage_analyze(args, info, prefix):
    t0 = time.time()
    info_a, events, curves = analyze.analyze(args.src, log=log)
    knobs = {k: getattr(args, k) for k in motion.DEFAULTS if hasattr(args, k)}
    curve, stats, used = motion.build(info_a, events, curves, knobs, log=log)
    H = info["height"]
    f = H / 1080.0
    n = info_a["frames"]
    fps = info_a["fps"]
    with open(prefix + "-curve.csv", "w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["frame", "t", "dx_px", "dy_px", "rot_deg", "scale", "margin_px", "speech", "walk", "dark", "jolt"])
        for i in range(n):
            w.writerow([i, f"{i / fps:.4f}", f"{curve['dx'][i] * f:.3f}", f"{curve['dy'][i] * f:.3f}",
                        f"{curve['rot'][i]:.4f}", f"{curve['scale'][i]:.5f}", f"{curve['margin'][i] * f:.2f}",
                        f"{curve['speech'][i]:.3f}", f"{curve['walk_env'][i]:.3f}", f"{curve['dark'][i]:.3f}",
                        int(curve["jolt"][i])])
    doc = {"input": args.src, "source": info, "px_unit": f"output px at {H} lines (ref px x {f:g})",
           "events": events, "knobs": used, "stats": stats}
    with open(prefix + "-motion.json", "w") as fh:
        json.dump(doc, fh, indent=1, default=float)
    plot_curve(prefix + "-curve.png", curve, events, fps)
    log(f"analyze + motion: {time.time() - t0:.1f} s -> {prefix}-motion.json")
    return curve, time.time() - t0


def load_curve(prefix, info):
    f = info["height"] / 1080.0
    rows = list(csv.DictReader(open(prefix + "-curve.csv")))
    return {"dx": np.array([float(r["dx_px"]) for r in rows]) / f,
            "dy": np.array([float(r["dy_px"]) for r in rows]) / f,
            "rot": np.array([float(r["rot_deg"]) for r in rows]),
            "scale": np.array([float(r["scale"]) for r in rows])}


def stage_handheld(args, info, curve, H, out):
    import cv2
    W = even(H * info["width"] / info["height"])
    f = H / 1080.0
    start_f = int(round((args.start or 0) * info["fps"]))
    n = info["frames"] - start_f if not args.duration else int(round(args.duration * info["fps"]))
    cx, cy = (W - 1) / 2, (H - 1) / 2
    interp = cv2.INTER_LANCZOS4 if args.interp == "lanczos" else cv2.INTER_CUBIC

    def fn(i, fr):
        j = min(start_f + i, len(curve["dx"]) - 1)
        M = cv2.getRotationMatrix2D((cx, cy), float(curve["rot"][j]), float(curve["scale"][j]))
        M[0, 2] += curve["dx"][j] * f
        M[1, 2] += curve["dy"][j] * f
        return cv2.warpAffine(fr, M, (W, H), flags=interp, borderMode=cv2.BORDER_REFLECT_101)

    dec = decoder(args.src, W, H, args.start, args.duration)
    enc = encoder(out, W, H, info["fps_str"], args.src if info["has_audio"] else None,
                  args.start, args.duration, args.crf_handheld, args.preset)
    log(f"handheld: {W}x{H}, {n} frames -> {out}")
    done, el, tfn = run_pipe(dec, enc, W, H, n, fn, "handheld")
    log(f"handheld: {done} frames in {el:.1f} s ({done / el:.2f} fps; warp {tfn:.1f} s)")
    return el


def stage_crt(args, info, src, H, out, cube):
    import crt
    W = even(H * info["width"] / info["height"])
    knobs = {k: getattr(args, "crt_" + k) for k in crt.DEFAULTS if getattr(args, "crt_" + k, None) is not None}
    t0 = time.time()
    c = crt.CRT(W, H, knobs)
    log(f"crt: mask built in {time.time() - t0:.1f} s ({W}x{H})")
    n = int(round((args.duration or info["duration"]) * info["fps"]))
    cube_esc = cube.replace("\\", "\\\\").replace(":", "\\:").replace("'", "\\'")
    dec = decoder(src, W, H, args.start if args.crt_only else None, args.duration if args.crt_only else None,
                  pre_vf=f"lut3d=file='{cube_esc}':interp=tetrahedral")
    enc = encoder(out, W, H, info["fps_str"], src if info["has_audio"] else None,
                  args.start if args.crt_only else None, args.duration if args.crt_only else None,
                  args.crf, args.preset)
    log(f"crt: {W}x{H} -> {out}")
    done, el, tfn = run_pipe(dec, enc, W, H, n, lambda i, fr: c(fr), f"crt {H}p")
    log(f"crt {H}p: {done} frames in {el:.1f} s ({done / el:.2f} fps; finish {tfn:.1f} s)")
    return el + (time.time() - t0 - el)


# --- plot ---------------------------------------------------------------------------------------

def plot_curve(path, curve, events, fps):
    """A plain numpy plot: dx, dy (ref px), rot (deg x20), margin; events as ticks. Written via ffmpeg."""
    n = len(curve["dx"])
    Wp, Hp = 1800, 720
    img = np.full((Hp, Wp, 3), 250, np.uint8)
    rows = [("dx", curve["dx"], (40, 90, 200), 30), ("dy", curve["dy"], (200, 80, 40), 20),
            ("rot x20", curve["rot"] * 20, (40, 150, 60), 20), ("margin", curve["margin"], (120, 60, 160), 60)]
    band = Hp // len(rows)
    for r, (name, y, col, lim) in enumerate(rows):
        y0 = r * band + band // 2
        img[y0, :] = 200
        img[r * band, :] = 120
        xs = (np.arange(n) * (Wp - 1) / max(1, n - 1)).astype(int)
        ys = np.clip(y0 - y / lim * (band / 2 - 6), r * band + 1, (r + 1) * band - 2).astype(int)
        for a in range(n - 1):
            y_a, y_b = sorted((ys[a], ys[a + 1]))
            img[y_a: y_b + 1, xs[a]: xs[a + 1] + 1] = col
    colors = {"cut": (0, 0, 0), "impact": (220, 30, 30), "flash": (40, 200, 40), "rumble": (150, 90, 20), "speech": (60, 60, 230)}
    for e in events:
        x = int(e["t"] * fps * (Wp - 1) / max(1, n - 1))
        c = colors.get(e["kind"], (0, 0, 0))
        if e["kind"] == "speech":
            x2 = int(e["end"] * fps * (Wp - 1) / max(1, n - 1))
            img[Hp - 8: Hp - 2, x: x2 + 1] = c
        else:
            img[:14, max(0, x - 1): x + 2] = c
    for s in range(0, int(n / fps) + 1, 5):
        x = int(s * fps * (Wp - 1) / max(1, n - 1))
        img[Hp - 20: Hp - 10, x] = 0
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{Wp}x{Hp}",
                    "-i", "-", "-frames:v", "1", path], input=img.tobytes(), check=True)


# --- main ---------------------------------------------------------------------------------------

def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--in", dest="src", required=True)
    ap.add_argument("--name", required=True)
    ap.add_argument("--out-dir", required=True)
    ap.add_argument("--height", type=int, action="append", help="output height(s); default the input's")
    ap.add_argument("--handheld-only", action="store_true")
    ap.add_argument("--crt-only", action="store_true", help="the input is already handheld: CRT only")
    ap.add_argument("--start", type=float, help="render an excerpt from here (s); the motion is the full film's")
    ap.add_argument("--duration", type=float)
    ap.add_argument("--reuse-curve", action="store_true", help="reuse NAME-curve.csv instead of re-analysing")
    ap.add_argument("--drop-handheld", action="store_true", help="delete the handheld intermediate after the CRT copies")
    ap.add_argument("--crf", type=int, default=16)
    ap.add_argument("--crf-handheld", type=int, default=14)
    ap.add_argument("--preset", default="medium")
    ap.add_argument("--interp", choices=["lanczos", "cubic"], default="lanczos")
    for k, v in motion.DEFAULTS.items():
        ap.add_argument("--" + k.replace("_", "-"), dest=k, type=type(v), default=None, help=f"motion (default {v})")
    import crt as _crt
    for k, v in _crt.DEFAULTS.items():
        ap.add_argument("--crt-" + k.replace("_", "-"), dest="crt_" + k, type=type(v), default=None, help=f"crt (default {v})")
    args = ap.parse_args()

    os.makedirs(args.out_dir, exist_ok=True)
    prefix = os.path.join(args.out_dir, args.name)
    info = analyze.probe(args.src)
    heights = sorted(set(args.height or [info["height"]]), reverse=True)
    timings = {}
    T0 = time.time()

    hh_path = None
    if not args.crt_only:
        if args.reuse_curve and os.path.exists(prefix + "-curve.csv"):
            curve = load_curve(prefix, info)
            log("motion: reused " + prefix + "-curve.csv")
        else:
            curve, timings["analyze"] = stage_analyze(args, info, prefix)
        hh_path = f"{prefix}-handheld-{heights[0]}p.mp4"
        timings[f"handheld_{heights[0]}p"] = stage_handheld(args, info, curve, heights[0], hh_path)
    if not args.handheld_only:
        import crt
        cube = crt.write_cube(prefix + "-look.cube",
                              {**crt.DEFAULTS, **{k: getattr(args, "crt_" + k) for k in crt.DEFAULTS
                                                  if getattr(args, "crt_" + k) is not None}})
        src = args.src if args.crt_only else hh_path
        sinfo = analyze.probe(src)
        for H in heights:
            out = f"{prefix}-crt-{H}p.mp4"
            timings[f"crt_{H}p"] = stage_crt(args, sinfo, src, H, out, cube)
        if args.drop_handheld and hh_path:
            os.remove(hh_path)
    timings["total"] = time.time() - T0
    log("timings (s): " + ", ".join(f"{k}={v:.1f}" for k, v in timings.items()))
    with open(prefix + "-timings.json", "w") as fh:
        json.dump(timings, fh, indent=1)


if __name__ == "__main__":
    main()
