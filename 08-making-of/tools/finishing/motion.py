"""One continuous handheld-camera signal for the whole film.

Units: translation in "ref px" = pixels at a 1080-line frame (multiply by H/1080 for the render
height), rotation in degrees, scale as a factor. The signal never resets at cuts; cuts only nudge
a smoothed per-shot intensity.

Layers
  drift    : layered smooth noise (periods ~9 s, ~3.5 s, ~1.3 s) on x, y, roll
  walk     : footstep bounce (vertical, ~1.6-2 Hz, slowly wandering cadence) with lateral sway and
             roll at the stride rate (half the step rate)
  breath   : ~0.25 Hz rise and fall, stronger (relatively) when dialogue calms the walk
  jolts    : damped kicks on impacts and flashes; a longer shaking kick on rumbles (the worm)
Envelopes  : speech calms walk and drift; near-black frames (title cards) calm everything; each shot
             gets its own smoothed intensity.
Coverage   : the frame is scaled by `scale` (>= base 1.06); rotation is soft-limited, then the
             translation is scaled down wherever the worst corner would leave the margin, with the
             limiter eroded and smoothed so it never kinks.
"""
import math

import numpy as np

from analyze import smooth

DEFAULTS = {
    "seed": 7,
    "scale": 1.06,          # base zoom (crop margin)
    "drift_x": 13.0,        # ref px std, slow layer (others are fractions of it)
    "drift_y": 7.5,
    "drift_rot": 0.32,      # degrees std, slow layer
    "step_hz": 1.8,         # footstep rate
    "bounce": 2.4,          # ref px, vertical footstep bounce
    "sway": 2.0,            # ref px, lateral sway at stride rate
    "sway_rot": 0.10,       # degrees, roll at stride rate
    "breath_hz": 0.25,
    "breath": 1.6,          # ref px
    "breath_rot": 0.05,
    "jolt": 11.0,           # ref px for a strength-1 impact
    "jolt_rot": 0.40,       # degrees for a strength-1 impact
    "jolt_tau": 0.15,       # s, decay time constant (gone after ~0.45 s)
    "jolt_hz": 4.2,         # oscillation of the kick
    "rumble": 4.0,          # ref px of sustained shake on rumbles
    "max_rot": 1.0,         # degrees, soft limit
    "speech_calm": 0.6,     # how much speech calms walk and drift (0..1)
    "dark_calm": 0.7,       # how much near-black frames calm everything (0..1)
    "safety": 2.0,          # ref px kept between the frame edge and the scaled picture edge
}


def _noise(rng, n, fps, period_s):
    """Unit-std smooth noise with a characteristic period (gaussian-filtered white noise)."""
    sigma = period_s * fps / (2 * math.pi)
    pad = int(6 * sigma) + 4
    x = smooth(rng.standard_normal(n + 2 * pad), sigma)[pad: pad + n]
    x = x - x.mean()
    return x / (x.std() + 1e-12)


def _layered(rng, n, fps, amp):
    return amp * (_noise(rng, n, fps, 9.0) + 0.45 * _noise(rng, n, fps, 3.5) + 0.16 * _noise(rng, n, fps, 1.3))


def _kick(n, fps, start, amp, tau, hz, phase, rise=0.03):
    t = (np.arange(n) - start) / fps
    out = np.zeros(n)
    m = t >= 0
    tt = t[m]
    out[m] = amp * np.exp(-tt / tau) * np.sin(2 * math.pi * hz * tt + phase) * (1 - np.exp(-tt / rise))
    return out


def corner_margin(dx, dy, rot_deg, scale, W, H):
    """Smallest distance (source px) from any output corner, mapped back into the source, to the
    source edge. Negative means a corner would show outside the picture. dx, dy in output px."""
    th = np.radians(rot_deg)
    c, s = np.cos(th), np.sin(th)
    m = np.full(np.shape(dx), np.inf)
    for px, py in ((W / 2, H / 2), (-W / 2, H / 2), (W / 2, -H / 2), (-W / 2, -H / 2)):
        ux, uy = px - dx, py - dy
        qx = (c * ux + s * uy) / scale       # R(-theta) (p - t) / s
        qy = (-s * ux + c * uy) / scale
        m = np.minimum(m, np.minimum(W / 2 - np.abs(qx), H / 2 - np.abs(qy)))
    return m


def build(info, events, curves, knobs=None, log=print):
    k = dict(DEFAULTS)
    k.update({kk: v for kk, v in (knobs or {}).items() if v is not None})
    n, fps = info["frames"], info["fps"]
    W = 1080.0 * info["width"] / info["height"]   # ref frame (1080 lines)
    H = 1080.0
    rng = np.random.default_rng(int(k["seed"]))
    t = np.arange(n) / fps

    # envelopes -------------------------------------------------------------
    speech = np.clip(np.asarray(curves.get("speech", np.zeros(n)))[:n], 0, 1)
    speech = smooth(speech, fps * 0.6)
    luma = np.asarray(curves["luma"])[:n]
    dark = np.clip((0.06 - luma) / 0.04, 0, 1)            # 1 on near-black frames
    dark = smooth(dark, fps * 0.5)
    cuts = [0] + [e["frame"] for e in events if e["kind"] == "cut"] + [n]
    shot = np.ones(n)
    for a, b in zip(cuts[:-1], cuts[1:]):
        shot[a:b] = rng.uniform(0.82, 1.15)
    shot = smooth(shot, fps * 0.5)
    calm_all = 1 - k["dark_calm"] * dark
    walk_env = np.clip(0.55 + 0.45 * _noise(rng, n, fps, 12.0) * 0.6, 0.3, 1.0)  # walking pace wanders
    walk_env = walk_env * (1 - k["speech_calm"] * speech) * shot * calm_all
    drift_env = (1 - 0.45 * k["speech_calm"] * speech) * shot * calm_all
    breath_env = (0.55 + 0.45 * speech) * (1 - 0.5 * dark)

    # drift -----------------------------------------------------------------
    dx = _layered(rng, n, fps, k["drift_x"]) * drift_env
    dy = _layered(rng, n, fps, k["drift_y"]) * drift_env
    rot = _layered(rng, n, fps, k["drift_rot"]) * drift_env

    # walk: cadence wanders +-6 %, phase integrates it --------------------------
    f_step = k["step_hz"] * (1 + 0.06 * _noise(rng, n, fps, 6.0))
    phase = 2 * math.pi * np.cumsum(f_step) / fps + rng.uniform(0, 2 * math.pi)
    # a footfall is a quick dip and a slower rise: fundamental plus a little second harmonic
    bounce = np.cos(phase) + 0.28 * np.cos(2 * phase + 0.6)
    dy += k["bounce"] * walk_env * bounce
    dx += k["sway"] * walk_env * np.sin(phase / 2)
    rot += k["sway_rot"] * walk_env * np.sin(phase / 2 + 0.5)

    # breath ----------------------------------------------------------------
    f_b = k["breath_hz"] * (1 + 0.12 * _noise(rng, n, fps, 15.0))
    bph = 2 * math.pi * np.cumsum(f_b) / fps + rng.uniform(0, 2 * math.pi)
    dy += k["breath"] * breath_env * np.sin(bph)
    rot += k["breath_rot"] * breath_env * np.sin(bph + 1.1)
    zoom = 0.0015 * breath_env * (0.5 + 0.5 * np.sin(bph - 0.4))   # tiny push, never below base

    # jolts -----------------------------------------------------------------
    jx, jy, jr = np.zeros(n), np.zeros(n), np.zeros(n)
    jolt_mask = np.zeros(n, bool)
    used = []
    for e in events:
        kind = e["kind"]
        if kind not in ("impact", "flash", "rumble"):
            continue
        f0 = e["frame"]
        if any(abs(f0 - u) < int(0.2 * fps) for u in used):   # merge near-coincident triggers
            continue
        used.append(f0)
        s = float(e["strength"]) * (1 - 0.6 * dark[min(f0, n - 1)])
        gain = {"impact": 1.0, "flash": 0.65, "rumble": 0.85}[kind]
        ang = rng.uniform(-0.6, 0.6) + (math.pi / 2)            # mostly vertical, some lateral
        a = k["jolt"] * s * gain
        tau = k["jolt_tau"] * (1.4 if kind == "rumble" else 1.0)
        jx += _kick(n, fps, f0, a * math.cos(ang), tau, k["jolt_hz"] * 1.13, rng.uniform(-0.3, 0.3))
        jy += _kick(n, fps, f0, a * math.sin(ang), tau, k["jolt_hz"], rng.uniform(-0.3, 0.3))
        jr += _kick(n, fps, f0, k["jolt_rot"] * s * gain * rng.choice([-1, 1]), tau * 1.2,
                    k["jolt_hz"] * 0.8, 0.0)
        end = f0 + int(fps * 4 * tau)
        if kind == "rumble" and e.get("end"):
            f1 = int(round(e["end"] * fps))
            env = np.zeros(n)
            env[f0:f1] = 1.0
            env = smooth(env, fps * 0.2) * s
            jx += k["rumble"] * env * _noise(rng, n, fps, 0.5)
            jy += k["rumble"] * 0.8 * env * _noise(rng, n, fps, 0.42)
            jr += 0.10 * env * _noise(rng, n, fps, 0.6)
            end = max(end, f1 + int(0.6 * fps))
        jolt_mask[max(0, f0 - 1): min(n, end)] = True
    # half-frame smoothing so a kick never steps from one frame to the next
    dx += smooth(jx, 0.5)
    dy += smooth(jy, 0.5)
    rot += smooth(jr, 0.5)

    # limits ----------------------------------------------------------------
    R = k["max_rot"]
    rot = R * np.tanh(rot / R)
    scale = k["scale"] * (1 + zoom)
    # soft-limit translation to the budget of the base scale, per axis
    mx = (k["scale"] - 1) * W / 2
    my = (k["scale"] - 1) * H / 2
    dx = 0.92 * mx * np.tanh(dx / (0.92 * mx))
    dy = 0.92 * my * np.tanh(dy / (0.92 * my))
    # exact coverage: scale translation by lam (bisection), then erode + smooth lam so it stays
    # below what each frame needs and never kinks
    safety = k["safety"]
    need = np.ones(n)
    bad = corner_margin(dx, dy, rot, scale, W, H) < safety
    for i in np.where(bad)[0]:
        lo, hi = 0.0, 1.0
        for _ in range(40):
            mid = 0.5 * (lo + hi)
            if corner_margin(dx[i] * mid, dy[i] * mid, rot[i], scale[i], W, H) >= safety:
                lo = mid
            else:
                hi = mid
        need[i] = lo
    limited = int(bad.sum())
    if limited:
        r = int(fps * 0.25)
        er = np.array([need[max(0, i - r): i + r + 1].min() for i in range(n)])
        lam = smooth(er, r / 3)
        lam = np.minimum(lam, need)     # guarantee (smoothing within the erosion window is already below)
        dx, dy = dx * lam, dy * lam
    margin = corner_margin(dx, dy, rot, scale, W, H)

    curve = {"dx": dx, "dy": dy, "rot": rot, "scale": scale, "margin": margin,
             "speech": speech, "walk_env": walk_env, "dark": dark, "jolt": jolt_mask.astype(float)}

    # stats -----------------------------------------------------------------
    def jerk(x):
        return np.abs(np.diff(x, 2)) if len(x) > 2 else np.zeros(1)
    calm = ~jolt_mask[1:-1]
    stats = {
        "frames": n,
        "max_abs_rot_deg": float(np.abs(rot).max()),
        "max_abs_dx_refpx": float(np.abs(dx).max()),
        "max_abs_dy_refpx": float(np.abs(dy).max()),
        "rms_dx_refpx": float(np.sqrt((dx ** 2).mean())),
        "rms_dy_refpx": float(np.sqrt((dy ** 2).mean())),
        "min_margin_refpx": float(margin.min()),
        "frames_limited": limited,
        "max_step_refpx": float(np.hypot(np.diff(dx), np.diff(dy)).max()),
        "jerk_calm_max_refpx": float(max(jerk(dx)[calm].max(), jerk(dy)[calm].max())),
        "jerk_jolt_max_refpx": float(max(jerk(dx)[~calm].max(initial=0), jerk(dy)[~calm].max(initial=0))),
        "jerk_calm_rot_deg": float(jerk(rot)[calm].max()),
        "jolts": len(used),
    }
    log("motion: " + ", ".join(f"{a}={b:.3f}" if isinstance(b, float) else f"{a}={b}" for a, b in stats.items()))
    return curve, stats, k
