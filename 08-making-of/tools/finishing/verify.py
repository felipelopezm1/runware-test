#!/usr/bin/env python3
"""verify.py: check a finishing run.

  verify.py --src SRC --prefix DIR/NAME [--height 1080] [--times 9.1,44.2 ...] [--start S]

  - the motion curve: min corner margin (numerical), max |rot|, |dx|, |dy|, jerk outside jolts
  - every frame of the handheld pass: its 3 px border strips against the source's (a black edge would
    show as a dark strip where the source is not dark)
  - ffprobe of every output: frames, duration, audio
  - stills at the given times (plus the frame after each cut and each impact, flash, rumble) and a 2x2
    corner sheet and a 1:1 centre crop of the CRT copy, under DIR/NAME-check/
"""
import argparse
import csv
import json
import os
import subprocess

import numpy as np


def probe(path):
    out = subprocess.run(["ffprobe", "-v", "error", "-count_packets", "-show_streams", "-show_format",
                          "-of", "json", path], capture_output=True, text=True, check=True).stdout
    j = json.loads(out)
    v = next(s for s in j["streams"] if s["codec_type"] == "video")
    a = [s for s in j["streams"] if s["codec_type"] == "audio"]
    return {"file": os.path.basename(path), "size": f"{v['width']}x{v['height']}",
            "frames": int(v.get("nb_read_packets") or v.get("nb_frames")), "fps": v["r_frame_rate"],
            "v_duration": float(v.get("duration", 0)), "format_duration": float(j["format"]["duration"]),
            "audio": [{"codec": s["codec_name"], "rate": s["sample_rate"], "ch": s["channels"],
                       "duration": float(s.get("duration", 0)), "bitrate": s.get("bit_rate")} for s in a],
            "MB": round(int(j["format"]["size"]) / 1e6, 1)}


def frames(path, W, H, start=None, dur=None):
    cmd = ["ffmpeg", "-v", "error"]
    if start:
        cmd += ["-ss", str(start)]
    cmd += ["-i", path]
    if dur:
        cmd += ["-t", str(dur)]
    cmd += ["-an", "-vf", f"scale={W}:{H}:in_color_matrix=bt709,format=rgb24", "-f", "rawvideo", "-"]
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, bufsize=W * H * 3 * 4)
    fsz = W * H * 3
    while True:
        b = p.stdout.read(fsz)
        if len(b) < fsz:
            break
        yield np.frombuffer(b, np.uint8).reshape(H, W, 3)
    p.wait()


def border_check(src, hh, W, H, start=None, dur=None, b=3):
    """Per frame: mean luma of each 3 px border strip in the handheld pass and the source."""
    def strips(f):
        y = f.astype(np.float32) @ np.array([0.2126, 0.7152, 0.0722], np.float32)
        return np.array([y[:b].mean(), y[-b:].mean(), y[:, :b].mean(), y[:, -b:].mean(),
                         y[:b, :b].mean(), y[:b, -b:].mean(), y[-b:, :b].mean(), y[-b:, -b:].mean()])
    s = np.array([strips(f) for f in frames(src, W, H, start, dur)])
    h = np.array([strips(f) for f in frames(hh, W, H)])
    n = min(len(s), len(h))
    s, h = s[:n], h[:n]
    # a black edge: the handheld strip is near black although the source frame there is not
    src_frame = np.array([v.mean() for v in s])
    bad = (h < 4) & (s.mean(axis=1, keepdims=True) > 12)
    return {"frames_checked": n, "frames_with_dark_edge": int(bad.any(axis=1).sum()),
            "min_edge_luma_where_source_lit": float(h[s.mean(axis=1) > 12].min()) if (s.mean(axis=1) > 12).any() else None,
            "worst_frames": [int(i) for i in np.argsort(h.min(axis=1))[:5]], "_src_mean": float(src_frame.mean())}


def still(path, t, out, vf=None):
    cmd = ["ffmpeg", "-v", "error", "-y", "-ss", f"{t:.3f}", "-i", path, "-frames:v", "1"]
    if vf:
        cmd += ["-vf", vf]
    subprocess.run(cmd + [out], check=True)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--src", required=True)
    ap.add_argument("--prefix", required=True)
    ap.add_argument("--height", type=int, default=1080)
    ap.add_argument("--start", type=float)
    ap.add_argument("--duration", type=float)
    ap.add_argument("--times", default="")
    ap.add_argument("--max-stills", type=int, default=14)
    a = ap.parse_args()
    H = a.height
    report = {}

    # curve --------------------------------------------------------------------------
    rows = list(csv.DictReader(open(a.prefix + "-curve.csv")))
    dx = np.array([float(r["dx_px"]) for r in rows])
    dy = np.array([float(r["dy_px"]) for r in rows])
    rot = np.array([float(r["rot_deg"]) for r in rows])
    mar = np.array([float(r["margin_px"]) for r in rows])
    jolt = np.array([int(r["jolt"]) for r in rows]).astype(bool)
    d2 = np.maximum(np.abs(np.diff(dx, 2)), np.abs(np.diff(dy, 2)))
    calm = ~jolt[1:-1]
    report["curve (px at the analysis height)"] = {
        "max_abs_rot_deg": round(float(np.abs(rot).max()), 3), "max_abs_dx": round(float(np.abs(dx).max()), 2),
        "max_abs_dy": round(float(np.abs(dy).max()), 2), "min_corner_margin": round(float(mar.min()), 2),
        "max_frame_step": round(float(np.hypot(np.diff(dx), np.diff(dy)).max()), 2),
        "max_accel_outside_jolts": round(float(d2[calm].max()), 3),
        "max_accel_in_jolts": round(float(d2[~calm].max(initial=0)), 3),
        "max_rot_accel_outside_jolts_deg": round(float(np.abs(np.diff(rot, 2))[calm].max()), 4)}

    # outputs ------------------------------------------------------------------------
    d = os.path.dirname(a.prefix)
    name = os.path.basename(a.prefix)
    outs = sorted(f for f in os.listdir(d) if f.startswith(name + "-") and f.endswith(".mp4"))
    report["source"] = probe(a.src)
    report["outputs"] = [probe(os.path.join(d, f)) for f in outs]

    hh = [f for f in outs if "-handheld-" in f]
    if hh:
        hp = os.path.join(d, hh[0])
        W = int(round(H * 16 / 9 / 2)) * 2
        report["border check (handheld vs source)"] = border_check(a.src, hp, W, H, a.start, a.duration)

    # stills -------------------------------------------------------------------------
    meta = json.load(open(a.prefix + "-motion.json"))
    times = [float(t) for t in a.times.split(",") if t]
    off = a.start or 0
    end = off + (a.duration or meta["source"]["duration"])
    for e in meta["events"]:
        if e["kind"] in ("cut", "impact", "flash", "rumble") and off <= e["t"] + 0.1 < end:
            times.append(e["t"] + (0.05 if e["kind"] == "cut" else 0.12))
    times = sorted(set(round(t, 2) for t in times))
    if len(times) > a.max_stills:
        times = [times[int(i)] for i in np.linspace(0, len(times) - 1, a.max_stills)]
    cdir = a.prefix + "-check"
    os.makedirs(cdir, exist_ok=True)
    crts = [os.path.join(d, f) for f in outs if "-crt-" in f]
    for c in crts:
        tag = os.path.basename(c)[len(name) + 1:-4]
        for t in times:
            still(c, t - off, os.path.join(cdir, f"{tag}-{t:06.2f}.jpg"), vf="scale=1280:-2")
        # 2x2 corner sheet at 1:1 pixels, and a 1:1 centre crop
        ch = int(probe(c)["size"].split("x")[1])
        cw = ch * 16 // 9
        s = ch // 4
        t = times[len(times) // 2] - off
        still(c, t, os.path.join(cdir, f"{tag}-corners.png"),
              vf=(f"split=4[a][b][c][d];[a]crop={s * 16 // 9}:{s}:0:0[A];[b]crop={s * 16 // 9}:{s}:{cw - s * 16 // 9}:0[B];"
                  f"[c]crop={s * 16 // 9}:{s}:0:{ch - s}[C];[d]crop={s * 16 // 9}:{s}:{cw - s * 16 // 9}:{ch - s}[D];"
                  f"[A][B]hstack[T];[C][D]hstack[U];[T][U]vstack"))
        still(c, t, os.path.join(cdir, f"{tag}-centre-1to1.png"), vf=f"crop=640:360:{cw // 2 - 320}:{ch // 2 - 180}")
    report["stills"] = {"dir": cdir, "times": times}
    print(json.dumps(report, indent=1, default=str))
    json.dump(report, open(a.prefix + "-verify.json", "w"), indent=1, default=str)


if __name__ == "__main__":
    main()
