# 07-cut: the film

The film, in the order it was made: the title, the 1080p assemblies, the clean cut, the finish. **Watch the final film:** [`clean/is-this-all-on-runware-crt-1080p-github.mp4`](clean/is-this-all-on-runware-crt-1080p-github.mp4) (the 4K master is on [release v1.0](https://github.com/felipelopezm1/runware-test/releases/tag/v1.0) and on Drive).

| folder | what it holds | where |
| --- | --- | --- |
| `title/` | the title card ("Is this all on Runware?", white serif on black, 2 s), the same with silence, the 1.5 s black, and the sheet it was drawn from | here |
| `1080p/` | the four 1080p assemblies: `is-this-all-on-runware-v1-1080p.mp4`, `-v2-1080p.mp4`, `-1080p.mp4` (the final of the first day) and `-v3-bridges-1080p.mp4` (with the two bridge clips), about 60 MB each | `is-this-all-on-runware-v3-bridges-1080p.mp4`, the assembly the clean cut was built from, is committed here; the earlier three are on Drive only |
| [`clean/`](clean/) | the clean cut, `is-this-all-on-runware-clean-1080p.mp4` (64 s, 82 MB; 4K on Drive), its 19 pieces, the grade and loudness scripts, the check sheets and [`cuts.md`](clean/cuts.md), the record of every change from v3 | here |
| [`clean/`](clean/) (the finish) | **the final film**, `is-this-all-on-runware-crt-4k.mp4`: the clean cut with a mild handheld shake and the CRT look (360 MB), its 1080p render (114 MB) and a 1080p copy that fits in Git | the 4K and the 114 MB render on [release v1.0](https://github.com/felipelopezm1/runware-test/releases/tag/v1.0) and on Drive under `07-cut/clean/`; the Git copy here |
| `picks/` | the picked take of every shot in order (copies of `05-shots/*/pick.mp4`) | in `05-shots/` here |
| `reels/` | the time-lapse of every take and the comparison reel per shot | pending |

**Where the files are:** what is committed is in this folder; everything else is in the [Drive folder](https://drive.google.com/drive/folders/1juyE0-suxmhWmGCIBmtff-UqxkQxNRRH) under `07-cut/`, which mirrors these folders. Nothing here points at a private machine.

The 4K path held: every clip was made natively on Seedance 2.5, so Topaz was not needed for the clips; the finishing tools in [`08-making-of/tools/finishing/`](../08-making-of/tools/finishing/) carry a Topaz 4K pass for the finish if it is wanted.
