# Is this all on Runware? The clean cut

**The film:** `07-cut/clean/is-this-all-on-runware-clean-1080p.mp4`
1920x1080, 24 fps, H.264 High (level 4.1) yuv420p, bt709 primaries, transfer and matrix, tv range; AAC-LC 48 kHz stereo 256 kb/s.
**Length:** 63.958 s (1535 frames). v3 ran 73.5 s.
**Loudness:** -14.0 LUFS integrated, true peak -1.2 dBTP, LRA 3.7 LU (ffmpeg ebur128 on the finished file).

Built on 2026-11-19 from v3 (`07-cut/1080p/is-this-all-on-runware-v3-bridges-1080p.mp4`, making-of log entry 782),
on Felipe's order of 15:34 UTC. No retake and no paid call: ffmpeg and Python on this machine only.
The earlier assemblies and every earlier file were left untouched.

## What changed from v3, and why

| # | Change | Why |
|---|--------|-----|
| 1 | The title card (2 s) moved from the end to the very start. | Felipe: title card first. |
| 2 | The end is now black only (1.5 s, silent). The title is no longer after it. | The title moved to the front; v3's black tail is kept. |
| 3 | 1A-v2 (5 s) dropped; the film opens on 1B-pick. | Wrong room. |
| 4 | bridge-1-2 (the remade one, 0-4 s) replaced by bridge-1-2-v1, used whole (5.042 s). | Felipe chose v1. Its last frame lands on 2A-1-v2's first frame. |
| 5 | 2A-1-v2 now runs 0.5-2.0 s (was 0-2). | The bridge already shows the arrival; trimming the first 0.5 s stops it being shown twice. |
| 6 | 3A-v2 now runs 0.5-5.0 s (was 0-5). | Same reason for bridge-2-3, whose tail lands on 3A's first frame. |
| 7 | 2C-v3 now runs 3-6 s, its last 3 s (was 0-6). | Felipe: trim 2C to its last 3 s. |
| 8 | 3E-pick now ends at 3.375 s (frame 81 excluded; was 0-5). | Frame 81 (3.375 s) is the first frame where the skull face shows; the cut lands just before it. |
| 9 | 2A-1 and 2A-2 colour-matched to 2B-v2; the last second of bridge-1-2-v1 graded into 2A-1's grade. | Kill the green tint. See "The grade". |
| 10 | Every piece with sound loudness-normalised to -14 LUFS on its own. | Felipe: loudness-match every segment to -14 LUFS. |

## The pieces, in order

All in `pieces/`, each rendered on its own with the parameters above (CRF 14, preset slow, GOP 48),
so the film is their concat (video stream-copied, audio joined sample-exact and encoded once).
Frames are at 24 fps; in and out are in the source's seconds (out is exclusive).

| Piece | Source | In | Out | Length | Grade | Loudness in -> out (LUFS) |
|-------|--------|----|-----|--------|-------|---------------------------|
| 00-title-card | titles/title-card-with-silence.mp4 | 0 | 2.0 | 2.000 s (48 f) | none | silent by design, not normalised |
| 01-1B-pick | takes/1B-pick.mp4 | 0 | 4.0 | 4.000 s (96 f) | none | -30.9 -> -14.1 |
| 02-1C-1-pick | takes/1C-1-pick.mp4 | 0 | 2.5 | 2.500 s (60 f) | none | -22.7 -> -14.0 |
| 03-1C-2-v3 | takes/1C-2-v3.mp4 | 0 | 3.5 | 3.500 s (84 f) | none | -25.0 -> -14.1 |
| 04-bridge-1-2-v1 | takes/bridge-1-2-v1.mp4 | 0 | 5.042 (whole) | 5.042 s (121 f) | last 1 s only: the 2A-1 grade ramped in (0 at 4.04 s, full on the last frame) | -23.7 -> -14.1 |
| 05-2A-1-v2-graded | takes/2A-1-v2.mp4 | 0.5 | 2.0 | 1.500 s (36 f) | graded to 2B | -20.2 -> -14.1 |
| 06-2A-2-v3-graded | takes/2A-2-v3.mp4 | 0 | 3.0 | 3.000 s (72 f) | graded to 2B, lifted | -27.2 -> -14.1 |
| 07-2B-v2 | takes/2B-v2.mp4 | 0 | 4.0 | 4.000 s (96 f) | none (the reference) | -24.7 -> -14.1 |
| 08-2C-v3 | takes/2C-v3.mp4 | 3.0 | 6.0 | 3.000 s (72 f) | none | -32.6 -> -14.0 |
| 09-bridge-2-3 | takes/bridge-2-3.mp4 | 0 | 4.042 (whole) | 4.042 s (97 f) | none | -32.0 -> -14.0 |
| 10-3A-v2 | takes/3A-v2.mp4 | 0.5 | 5.0 | 4.500 s (108 f) | none | -25.8 -> -14.1 |
| 11-3B-pick | takes/3B-pick.mp4 | 0 | 5.0 | 5.000 s (120 f) | none | -20.8 -> -14.1 |
| 12-3C-1-pick | takes/3C-1-pick.mp4 | 0 | 2.0 | 2.000 s (48 f) | none | -22.3 -> -14.0 |
| 13-3C-2-pick | takes/3C-2-pick.mp4 | 0 | 3.0 | 3.000 s (72 f) | none | -20.4 -> -14.2 |
| 14-3D-1-v2 | takes/3D-1-v2.mp4 | 0 | 3.0 | 3.000 s (72 f) | none | -25.3 -> -14.1 |
| 15-3D-2-pick | takes/3D-2-pick.mp4 | 0 | 3.0 | 3.000 s (72 f) | none | -24.7 -> -13.9 |
| 16-3E-pick | takes/3E-pick.mp4 | 0 | 3.375 | 3.375 s (81 f) | none | -22.2 -> -14.0 |
| 17-3F-pick | takes/3F-pick.mp4 | 0 | 6.0 | 6.000 s (144 f) | none | -29.0 -> -14.2 |
| 18-black-end | titles/black-1.5s.mp4 | 0 | 1.5 | 1.500 s (36 f) | none | silent by design, not normalised |

Sources: `takes/<shot>-<take>.mp4` is `05-shots/<shot>/takes/` in this repository (a `-pick` is that shot's `pick.mp4`; the bridges are in `05-shots/bridges/`), and `titles/` is `07-cut/title/`.
Total 1535 frames = 63.958 s.

## Loudness

- ffmpeg `loudnorm` two-pass (I=-14, TP=-1.5 dBTP, LRA=11), from the source audio (32 kHz in every take,
  resampled to 48 kHz stereo). Several pieces are only 1.5 to 3 s long, where loudnorm falls back to its dynamic
  mode and lands up to 2 LU off; those were then trimmed by a measured residual gain behind a -1.5 dB limiter,
  measured again, until within 0.2 LU (01, 02, 03, 05, 06, 08, 09, 10, 12, 13, 14; the dB of each trim is in
  `grade-scripts/pieces.jsonl`). Every piece reads -13.9 to -14.2 LUFS as written.
- The title and the black are digital silence (-91 dB in the sources) and stay silent: normalising silence would
  only raise noise, so they were not normalised.
- The whole film reads -14.0 LUFS, true peak -1.2 dBTP.
- Note: every shot is now at the same loudness, so quiet shots (2C, bridge-2-3, 1B were about -31 to -33 LUFS)
  were raised by 17 to 19 dB and loud ones lowered; that is what was asked, and the LRA of the film is 3.7 LU.

## The grade (2A-1, 2A-2, and the tail of bridge-1-2-v1)

Reference: 2B-v2 (its stone walls: mid-tone, low-chroma pixels). Measured in CIE Lab, mean of every pixel:

| | L | a | b |
|-|---|---|---|
| 2B-v2 (reference) | 29.1 | +2.4 | +0.9 |
| 2A-1-v2 0.5-2.0 before | 28.3 | -8.8 | +12.3 |
| 2A-1-v2 after | 28.3 | -0.7 | +3.5 (the green flame, kept, holds a and b of the mean) |
| 2A-2-v3 0-3 before | 16.9 | +0.7 | +2.8 |
| 2A-2-v3 after | 25.5 | +2.0 | +2.0 |

What it does, per frame (`grade-scripts/grade2.py`):
1. A mild white balance (30 % of the linear-light R and B gains that bring the stone walls to 2B's stone
   colour), smoothed over time (Gaussian, 4 frames), luminance kept.
2. The cast taken out in Lab: on every pixel with a green hue that is not the flame, 90 % of its green (a<0) and
   72 % of its yellow (b>0) removed, never pushed past neutral (the previous attempt matched means and turned the
   walls and the flame magenta; this one cannot). Because it scales the cast where it is, it follows the
   cast as it changes over time (strongest 0.5 to 1.5 s in 2A-1) without keyframes.
3. Protected: Mordecai's green flame and its glow (green, bright, saturated pixels) keep their colour.
   Lanterns, Vessa's hair and skin (warm hues) are untouched.
4. 2A-2 only: a soft lift (slope 2.2 at black, white stays white) from L 16.9 to 25.5, short of 2B's 29 so the
   shadows do not go grey and the flame is not clipped.
5. bridge-1-2-v1: its last half second turns green on its own (it was made to land on 2A-1's green first frame);
   the same grade fades in over its last 24 frames, so the cut into the graded 2A-1 does not flash green.
   The rest of the bridge, and bridge-2-3, are ungraded.

Check sheets (looked at): `checks/check-grade-2A-vs-2B.jpg` (2B beside 2A-1 and 2A-2 before and after, at the in,
middle and out of each) and `checks/check-grade-bridge-1-2-v1-tail.jpg`. The walls of 2A-1 read grey stone like 2B's,
the green flame stays green, Mordecai's helmet and plate in 2A-2 read dark iron instead of green, his hand's
flame stays green. 2A-1's out and 2A-2's in now match each other.

## Joins

`checks/check-joins.jpg` shows the last and first frame on both sides of all 18 joins in the finished film (looked at).

## Known flaws, kept

- **bridge-1-2-v1 after 1C-2-v3:** the bridge was made from the old 1C-2-v2's last frame, so at the join the
  staging jumps (the people stand differently than at 1C-2-v3's out). Felipe chose v1; kept.
- **bridge-1-2-v1 into 2A-1:** with 2A-1's first 0.5 s trimmed, the cut lands 12 frames on from the bridge's
  last picture (by design), and 2A-1 is brighter than the bridge's last frame (as in the sources).
- **2C:** the door the shot called for never appeared in 2C-v3; its last 3 s show the misty arch with no door.
- **3D-1:** 3D-1-v2's known axe flaw is still there (as in v3); no retakes, so not fixed.
- **3E:** cut at 3.375 s, before the skull face; the rest of the shot (the face) is gone.
- **Bridge-2-3 into 3A:** 3A's first 0.5 s trimmed, so the cut lands half a second on from the bridge's last frame.

## Files

- `is-this-all-on-runware-clean-1080p.mp4`: the film.
- `pieces/00-...mp4` to `pieces/18-...mp4`: the final version of each piece.
- `checks/`: the three check sheets.
- `grade-scripts/`: grade2.py, lab.py, piece.py, all.sh, and the measurements (2A-1.g3.json, 2A-2.g1.json,
  bridge.json, pieces.jsonl).


---

This page is the agents' own record of the cut, written on the production machine; its source paths were mapped onto this repository's folders. The scripts in `grade-scripts/` keep the production machine's paths as written, so they run as a record and not as a tool; `tools/paths.json` maps them.
