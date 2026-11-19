"""Grade toward 2B-v2: per-frame white balance from the stone walls (ratio of linear-RGB medians of
mid-tone, non-flame pixels matched to 2B's stone pixels), temporally smoothed; green flame protected;
green spill on armour and skin desaturated in Lab outside the flame core; optional soft-shoulder lift;
optional per-frame strength ramp. Writes lossless ffv1 (yuv420p bt709 tv)."""
import sys, json, subprocess, numpy as np
sys.path.insert(0, '/tmp/cleancut/scripts')
from lab import rgb2lab, lab2rgb, s2l, l2s
YW = np.array([0.2126729, 0.7151522, 0.0721750])
def ss(x, e0, e1):
    t = np.clip((x - e0) / (e1 - e0), 0, 1); return t * t * (3 - 2 * t)
def frames(path, a, b, W, H, fmt='rgb24'):
    vf = f'trim=start_frame={a}:end_frame={b},setpts=PTS-STARTPTS,scale={W}:{H}:flags=area:in_color_matrix=bt709:in_range=tv,format={fmt}'
    raw = subprocess.run(['ffmpeg','-v','error','-i',path,'-vf',vf,'-f','rawvideo','-pix_fmt',fmt,'-'],capture_output=True,check=True).stdout
    return np.frombuffer(raw, np.uint8).reshape(-1, H, W, 3) / 255.0
def flame(lab):  # bright green light: the flame and its glow core
    return ss(-lab[..., 1], 8, 20) * ss(lab[..., 0], 45, 65) * ss(np.hypot(lab[..., 1], lab[..., 2]), 18, 35)
def stone_mask(lab, ref=False):
    m = (lab[..., 0] > 10) & (lab[..., 0] < 60) & (flame(lab) < 0.2) & ~((lab[..., 2] > 25) & (lab[..., 0] > 40))
    if ref: m &= np.hypot(lab[..., 1], lab[..., 2]) < 25
    return m
def ratios(srgb, ref=False):
    lab = rgb2lab(srgb); m = stone_mask(lab, ref); lin = s2l(srgb)[m]
    med = np.median(lin, 0); return np.array([med[0] / med[1], med[2] / med[1]])
def lift(x, k):  # slope k at black, 1 -> 1
    return x * k / (1 + (k - 1) * x) if k != 1 else x
def grade_frame(srgb, g, k, desat, s, wb=1.0, chroma=0.0):
    g = np.asarray(g) ** wb
    lin = s2l(srgb); lab0 = rgb2lab(srgb); fl = flame(lab0)
    gains = np.array([g[0], 1.0, g[1]]); n = (lin.reshape(-1, 3).mean(0) @ YW) / ((lin.reshape(-1, 3).mean(0) * gains) @ YW)
    w = (1 - fl)[..., None] * s
    lin2 = lin + (lin * gains * n - lin) * w
    lin2 = lift(np.clip(lin2, 0, 1), 1 + (k - 1) * s)
    out = l2s(lin2)
    if chroma > 0:  # take the green-yellow cast out of non-flame pixels in Lab, never pushing past neutral
        lab = rgb2lab(out); gr = ss(-lab[..., 1], 0, 6) * (1 - fl) * s
        lab[..., 1] = lab[..., 1] * (1 - chroma * gr)
        lab[..., 2] = np.where(lab[..., 2] > 0, lab[..., 2] * (1 - 0.8 * chroma * gr), lab[..., 2])
        out = np.clip(lab2rgb(lab), 0, 1)
    if desat > 0:
        lab = rgb2lab(out); green = ss(-lab[..., 1], 4, 14) * (1 - fl)
        f = 1 - desat * s * green
        lab[..., 1] *= f; lab[..., 2] = lab[..., 2] * (1 - 0.5 * (1 - f))
        out = lab2rgb(lab)
    return np.clip(out, 0, 1)
def main():
    c = json.loads(sys.argv[1]); src, a, b = c['src'], c['a'], c['b']
    ref = frames(c['ref'], 0, 96, 240, 135); R = np.median([ratios(f, True) for f in ref[::4]], 0)
    ca, cb = max(0, a - 12), b + 12  # context for smoothing
    sm = frames(src, ca, cb, 240, 135); P = np.log(np.array([R / ratios(f) for f in sm]))
    sig = c.get('sigma', 4.0); r = int(3 * sig); kx = np.arange(-r, r + 1); kern = np.exp(-kx**2 / (2 * sig * sig)); kern /= kern.sum()
    Pp = np.pad(P, ((r, r), (0, 0)), mode='edge'); G = np.exp(np.stack([np.convolve(Pp[:, j], kern, 'valid') for j in range(2)], 1))
    G = G[a - ca: a - ca + (b - a)]; sm = sm[a - ca: a - ca + (b - a)]
    N = b - a; ramp = c.get('ramp')  # [first_full_frame_index_from_end] -> strength 0..1 ramp over last N frames
    S = np.ones(N)
    if ramp: S = ss(np.arange(N), N - ramp, N - 1)
    k, desat = c.get('k', 1.0), c.get('desat', 0.0); wb, chroma = c.get('wb', 1.0), c.get('chroma', 0.0)
    st = lambda L: [round(float(v), 2) for v in (L[..., 0].mean(), L[..., 1].mean(), L[..., 2].mean())]
    refL = rgb2lab(ref); before = rgb2lab(sm)
    after = np.stack([rgb2lab(grade_frame(sm[i], G[i], k, desat, S[i], wb, chroma)) for i in range(N)])
    rep = {'ref_Lab': st(refL), 'before_Lab': st(before), 'after_Lab': st(after), 'ref_ratios': R.round(3).tolist(),
           'gainR': G[[0, N // 2, -1], 0].round(3).tolist(), 'gainB': G[[0, N // 2, -1], 1].round(3).tolist(), 'k': k, 'desat': desat,
           'per_frame_ab_before': [[round(float(before[i][..., 1].mean()), 1), round(float(before[i][..., 2].mean()), 1)] for i in range(0, N, 6)],
           'per_frame_ab_after': [[round(float(after[i][..., 1].mean()), 1), round(float(after[i][..., 2].mean()), 1)] for i in range(0, N, 6)]}
    print(json.dumps(rep))
    if c.get('dry'): return
    W, H = 1920, 1080
    vf = f'trim=start_frame={a}:end_frame={b},setpts=PTS-STARTPTS,format=rgb48le'
    vf = f'trim=start_frame={a}:end_frame={b},setpts=PTS-STARTPTS,scale=in_color_matrix=bt709:in_range=tv,format=rgb48le'
    dec = subprocess.Popen(['ffmpeg','-v','error','-i',src,'-vf',vf,'-f','rawvideo','-pix_fmt','rgb48le','-'], stdout=subprocess.PIPE)
    enc = subprocess.Popen(['ffmpeg','-v','error','-y','-f','rawvideo','-pix_fmt','rgb48le','-s',f'{W}x{H}','-r','24','-i','-',
        '-vf','scale=out_color_matrix=bt709:out_range=tv,format=yuv420p','-c:v','ffv1','-color_primaries','bt709','-color_trc','bt709',
        '-colorspace','bt709','-color_range','tv', c['out']], stdin=subprocess.PIPE)
    n = 0; fb = W * H * 6
    while True:
        buf = dec.stdout.read(fb)
        if len(buf) < fb: break
        x = (np.frombuffer(buf, np.uint16).reshape(H, W, 3) / 65535.0).astype(np.float32)
        o = grade_frame(x, G[n], k, desat, S[n], wb, chroma) if S[n] > 1e-3 else x
        enc.stdin.write((o * 65535 + 0.5).astype(np.uint16).tobytes()); n += 1
    enc.stdin.close(); enc.wait(); dec.wait(); assert n == N, (n, N)
main()
