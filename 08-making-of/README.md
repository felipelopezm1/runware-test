# 08-making-of: the record

The record is a deliverable, not a by-product. Every step of the production, including the free ones, was written to one log through one tool, with its screenshots and clips numbered in the order they reached it. This folder is the whole of that record, in the shape it had on the production machine.

| folder or file | what it holds | status |
| --- | --- | --- |
| `log/log.md` | the human log, one entry per step, generated from `log.jsonl` | being written (about 1.6 MB so far) |
| `log/log.jsonl` | the same entries as JSON lines: step, plan step, time, lane, who, shot, arm, tool, model, AIR id, inputs, the prompt in full, the cost quoted and the cost charged, outputs, decision, change, note, screenshots, clips | being written |
| `log/log-parts/`, `log/log.d/` | the interim lines each lane wrote before import (lead, scout, quartermaster, director, quote, intake, prompts, references) | written |
| [`screens/`](screens/) | the numbered screenshots, `NNN-<plan step>-<what>.png`: the folder listing and every print, build photo and action map as first opened; each caption beside its picture; the storyboard editor; each sheet as rendered; the Blender stage and each blocked shot; each frame and take; the quote before every paid step and the charge after | 250 so far (about 290 MB) |
| [`clips/`](clips/) | the numbered process clips, `NNN-<plan step>-<what>.mp4`: the stage turntables (rejected ones kept), the Loom while clips generate, the board wall as takes land | 8 so far |
| [`recordings/`](recordings/) | the outside screen recording of the whole desktop while the quest ran: 10-minute segments (`loom-YYYYmmdd-HHMM.mp4`, about 85 MB each) and one full-screen shot a minute (`shots/`); the two scripts that made them | running since 13:34 UTC; Drive only |
| [`notes/`](notes/) | the lanes' working notes: the cast reading of the build photos, the map-against-shot-list comparisons, the director's proposals and review, the cost model and the quote, the stage axes, the intake manifest | written |
| [`references/`](references/) | every scraped reference with its author and licence (wet cellar masonry, crypt stairs, roofless halls under stars, dart frogs and cane toads, earthworm skin, a swept-hilt rapier, a bearded axe, a heater shield, a nasal helmet), and the thumbnails | 46 kept |
| [`tools/`](tools/) | the tools the agents wrote for this production: the log tool, the intake converter and viewer, the director's prompt assembler, the recording scripts, and `finishing/` (the handheld motion and CRT finish, the Topaz 4K pass) | the finishing tools are here; the rest at the end |
| `inputs/` | the intake: every hand-made input converted to 2048 px JPEG with a 320 px thumb, poster frames of the clips, contact sheets, and the manifest of all 252 files | made (not copied here: the originals are in `02-cast/` and `03-locations/`, the manifest is in `notes/`) |

The log names every input and output by the path it had on the production machine, as written; that is the record. The sheets, plates, meshes and takes it points at are in `02-cast/`, `03-locations/` and `05-shots/` here, or in the [Drive folder](https://drive.google.com/drive/folders/1FWxTWA6g5YAU0IvnW3phteEQP4Db5o-Y) at the place [`tools/paths.json`](../tools/paths.json) gives, which mirrors these folders.

## The plan steps

The log files every entry under one of fifteen plan steps:

| step | what | status at 16:00 UTC, 19 November 2026 |
| --- | --- | --- |
| 0 | setup and coordination | done |
| 1 | read the folder (every file opened, captioned with Qwen2.5-VL on Runware, compared with the notes) | done |
| 2 | references (openly licensed, Openverse and Wikimedia Commons) | done |
| 3 | storyboard (16 takes, 62 s) | done, approved |
| 4 | character sheets (116 panels on Nano Banana Pro) | done; small redraws |
| 5 | 3D counterparts and the stage (meshes, the three Blender stages, turntables, plates) | done |
| 6 | blocking (a clay clip per shot) | done: 16 clay clips |
| 7 | frames | done |
| 8 | clips on Seedance 2.5 (16 takes, then v2 and v3 retakes on eight shots, and two bridges) | done |
| 9 | prompt assembly | written, applied at 7 and 8 |
| 10 | voices and sound | no separate recordings yet (the audio folder is empty) |
| 11 | the cut | done: four 1080p assemblies (v1, v2, final, v3 with bridges), then the clean cut at 16:15 UTC (`07-cut/clean/`, record in `cuts.md`); the 4K handheld CRT finish is being made from it |
| 12 | title | done: the title card and the 1.5 s black are in `07-cut/title/` |
| 13 | masks and passes (optional) | pending |
| 14 | the showcase (social post, website piece) | pending |
