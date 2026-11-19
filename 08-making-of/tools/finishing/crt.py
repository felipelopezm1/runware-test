"""The CRT finish: a warm film LUT (.cube, applied by ffmpeg's lut3d), then per frame in float32:
bloom (blurred highlights screen-blended), barrel distortion of the picture (one cubic remap),
and one precomputed multiplicative mask holding the rounded screen edge with soft falloff, the
vignette and the scanlines (computed through the distortion, so they curve with the tube and are
never resampled: no moire), then a light dither back to 8 bits.
"""
import math

import cv2
import numexpr as ne
import numpy as np

DEFAULTS = {
    # look (LUT)
    "lift": 0.022,          # black lift
    "white": 0.985,         # white point after the shoulder
    "contrast": 0.20,       # S-curve mix (toe and shoulder)
    "warm": 1.0,            # 0 = neutral, 1 = the chosen warmth
    "sat": 0.96,
    # geometry
    "k1": 0.012,            # barrel, r normalised to half the height
    "k2": 0.0020,
    "fit": 0.85,            # 1: side mid-points land exactly on the frame edge; <1: a sliver of curved edge shows
    "corner": 0.075,        # rounded-corner radius, fraction of height
    "edge_soft": 0.010,     # screen-edge falloff, fraction of height
    "inset": 0.004,         # screen edge inset, fraction of height
    # light
    "vignette": 0.30,       # darkening at the very corner of the frame
    "vig_power": 2.2,
    "bloom": 0.16,          # screen-blend opacity
    "bloom_thr": 0.62,
    "bloom_size": 0.018,    # blur sigma, fraction of height (a second, wider layer is 3x)
    "scan": 0.075,          # scanline depth (0 = none)
    "scan_period_1080": 3.0,  # px at 1080 lines (360 lines); scales with height
}


# --- LUT ---------------------------------------------------------------------------------------

def look(rgb, k):
    """rgb: (..., 3) display-referred in [0,1] -> graded."""
    x = np.clip(rgb, 0, 1).astype(np.float64)
    r, g, b = x[..., 0], x[..., 1], x[..., 2]
    luma = 0.2126 * r + 0.7152 * g + 0.0722 * b
    # protect saturated greens (the spell glow) from the warm push
    greenness = np.clip((g - np.maximum(r, b)) * 4.0, 0, 1)
    w = k["warm"] * (1 - 0.65 * greenness)
    # warmth: a white-balance shift, strongest in the mids, kept off pure black and pure white
    mids = 4 * luma * (1 - luma)
    wr = 1 + w * (0.030 + 0.020 * mids)
    wg = 1 + w * (0.004 * mids)
    wb = 1 - w * (0.045 + 0.030 * mids)
    x = np.stack([r * wr, g * wg, b * wb], -1)
    # mild desaturation around luma (film is a touch less saturated than video)
    l2 = (0.2126 * x[..., 0] + 0.7152 * x[..., 1] + 0.0722 * x[..., 2])[..., None]
    x = l2 + (x - l2) * k["sat"]
    x = np.clip(x, 0, 1)
    # filmic toe and shoulder: blend toward a smoothstep S
    s = x * x * (3 - 2 * x)
    x = x + k["contrast"] * (s - x)
    # extra highlight roll-off above 0.8
    hi = np.clip((x - 0.8) / 0.2, 0, 1)
    x = x - 0.04 * hi * hi
    # lifted, slightly warm blacks and a soft white
    lift = np.array([k["lift"] * 1.12, k["lift"], k["lift"] * 0.85])
    x = lift + (k["white"] - lift) * x
    return np.clip(x, 0, 1)


def write_cube(path, k, size=33):
    grid = np.linspace(0, 1, size)
    # .cube order: red changes fastest
    bb, gg, rr = np.meshgrid(grid, grid, grid, indexing="ij")
    rgb = np.stack([rr, gg, bb], -1).reshape(-1, 3)
    out = look(rgb, k)
    with open(path, "w") as f:
        f.write('TITLE "finishing warm film"\n')
        f.write(f"LUT_3D_SIZE {size}\nDOMAIN_MIN 0.0 0.0 0.0\nDOMAIN_MAX 1.0 1.0 1.0\n")
        for v in out:
            f.write(f"{v[0]:.6f} {v[1]:.6f} {v[2]:.6f}\n")
    return path


# --- geometry and mask ------------------------------------------------------------------------

def _smoothstep(e0, e1, x):
    t = np.clip((x - e0) / (e1 - e0), 0, 1)
    return t * t * (3 - 2 * t)


class CRT:
    def __init__(self, W, H, knobs=None):
        k = dict(DEFAULTS)
        k.update({kk: v for kk, v in (knobs or {}).items() if v is not None})
        self.k, self.W, self.H = k, W, H
        cx, cy = (W - 1) / 2, (H - 1) / 2
        hh = H / 2
        ys, xs = np.mgrid[0:H, 0:W].astype(np.float64)
        X, Y = (xs - cx) / hh, (ys - cy) / hh        # isotropic, half-height = 1
        a = W / H
        r2 = X * X + Y * Y
        mult = 1 + k["k1"] * r2 + k["k2"] * r2 * r2
        side = 1 + k["k1"] * a * a + k["k2"] * a ** 4
        top = 1 + k["k1"] + k["k2"]
        z = side ** k["fit"] * top ** (1 - k["fit"])
        sx = cx + X * mult / z * hh                   # source coordinates (px)
        sy = cy + Y * mult / z * hh
        self.mapx, self.mapy = cv2.convertMaps(sx.astype(np.float32), sy.astype(np.float32), cv2.CV_16SC2)

        # local output-px per source-px (to antialias the picture edge in output pixels)
        jac = mult / z
        # picture validity: inside the source rectangle, soft over ~1.2 output px
        dist_src = np.minimum(np.minimum(sx + 0.5, W - 0.5 - sx), np.minimum(sy + 0.5, H - 0.5 - sy))
        valid = _smoothstep(-0.6, 0.6, dist_src / jac)
        # rounded screen edge (straight bezel with round corners), soft falloff
        inset = k["inset"] * H
        rad = k["corner"] * H
        bx, by = W / 2 - inset - rad, H / 2 - inset - rad
        qx = np.maximum(np.abs(xs - cx) - bx, 0)
        qy = np.maximum(np.abs(ys - cy) - by, 0)
        outside = np.hypot(qx, qy) - rad                       # >0 outside the rounded rect
        sd = outside
        soft = max(1.0, k["edge_soft"] * H)
        screen = 1 - _smoothstep(-soft, 0.35 * soft, sd)
        # vignette (elliptical, frame-relative)
        u, v = (xs - cx) / (W / 2), (ys - cy) / (H / 2)
        rho = np.sqrt(u * u + v * v) / math.sqrt(2)
        vig = 1 - k["vignette"] * rho ** k["vig_power"]
        # scanlines through the distortion (they bow with the tube); brightness compensated
        period = k["scan_period_1080"] * H / 1080.0
        if k["scan"] > 0 and period >= 2.0:
            scan = 1 - k["scan"] * (0.5 - 0.5 * np.cos(2 * math.pi * (sy + 0.5) / period))
            scan /= (1 - k["scan"] / 2)
        else:
            scan = np.ones_like(sx)
        mask = valid * screen * vig * scan
        self.mask255 = (mask * 255.0).astype(np.float32)[..., None]
        # dither patterns (triangular, +-1 LSB), cycled
        rng = np.random.default_rng(3)
        self.dither = [(rng.random((H, W, 1)) - rng.random((H, W, 1))).astype(np.float32) for _ in range(4)]
        self.sig1 = k["bloom_size"] * H / 8.0
        self.n = 0

    def bloom(self, fu):
        """fu: the (already curved) uint8 frame -> float32 bloom layer in [0, 1] at full size."""
        k = self.k
        H, W = self.H, self.W
        sw, sh = max(8, W // 8), max(8, H // 8)
        small = cv2.resize(fu, (sw, sh), interpolation=cv2.INTER_AREA).astype(np.float32) * (1.0 / 255.0)
        hi = np.maximum(small - k["bloom_thr"], 0) * (1.0 / (1 - k["bloom_thr"]))
        b1 = cv2.GaussianBlur(hi, (0, 0), self.sig1)
        b2 = cv2.GaussianBlur(hi, (0, 0), self.sig1 * 3)
        b = cv2.addWeighted(b1, 0.6 * k["bloom"], b2, 0.4 * k["bloom"], 0)
        return cv2.resize(b, (W, H), interpolation=cv2.INTER_LINEAR)

    def __call__(self, frame_u8):
        fu = cv2.remap(frame_u8, self.mapx, self.mapy, cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)
        m, d = self.mask255, self.dither[self.n % 4]
        self.n += 1
        if self.k["bloom"] > 0:
            b = self.bloom(fu)
            # screen blend f + b - f*b, then the mask, then dither, in one threaded pass
            out = ne.evaluate("(fu * (1 - b) * (1.0 / 255.0) + b) * m + d")
        else:
            out = ne.evaluate("fu * (1.0 / 255.0) * m + d")
        return cv2.convertScaleAbs(out)
