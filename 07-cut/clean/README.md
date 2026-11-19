# 07-cut/clean: the clean cut

[`is-this-all-on-runware-clean-1080p.mp4`](is-this-all-on-runware-clean-1080p.mp4) is the film as cut on 19 November 2026 at 16:15 UTC: 63.958 s, 1920x1080, 24 fps, -14 LUFS, title first and 1.5 s of black at the end. It is the base of the 4K handheld CRT finish, which is being made now.

| | |
| --- | --- |
| [`cuts.md`](cuts.md) | the cut's record: what changed from v3 and why, every piece with its in and out, the loudness work, the grade on 2A-1 and 2A-2, the joins, the known flaws kept |
| [`pieces/`](pieces/) | the 19 pieces in order, each rendered on its own (title, 17 shot and bridge pieces, black); the film is their concatenation |
| [`grade-scripts/`](grade-scripts/) | the Python and shell that graded 2A-1, 2A-2 and the tail of bridge-1-2-v1, cut and loudness-matched every piece, and the measurements they wrote |
| [`checks/`](checks/) | the three check sheets the agents looked at: the grade against 2B, the bridge tail, and both sides of all 18 joins |

No retake and no paid call went into this cut: ffmpeg and Python only, on the takes already in [`05-shots/`](../../05-shots/).

<p align="center"><img src="checks/check-joins.jpg" width="100%" alt="both sides of all 18 joins"></p>

**Where the files are:** everything in this folder is committed; the Drive folder mirrors it under `07-cut/clean/`.
