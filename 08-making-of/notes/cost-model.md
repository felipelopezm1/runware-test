# Cost model for "Is this all on Runware?"

Quartermaster, 2026-11-19. A sum, not a quote from Runware: nothing was sent and nothing was spent. The account holds **215.7715 USD** (`rw_account`, tool answer, 10:11 UTC). The facts behind every rate are in `runware-facts.md` beside this file.

Every price is marked `listed` (Runware's schema or page, or our catalogue) or `charged` (a real bill in our records: the `rw_*` ledger at `/home/felipe-lopez/titanium/.hephaestus/arm-spend.jsonl`, or the zombie test's session reports of 2026-11-11).

## The answer in one table

| path | low | expected | high |
| --- | --- | --- | --- |
| **A. Native 4K** on Seedance 2.5 (if the first 4K take proves the schema right) | $73 | **$152** | $263 |
| **B. 1080p** on Seedance 2.5, then one Topaz pass to 4K | $56 | **$111** | $192 |

- Low is one take of everything, at list price, with no clay clip sent.
- Expected is the brief's own assumption: a first take and one retake of every clip, on average.
- High is three takes of every clip, each with the clay clip as a video reference, and frames and plates drawn at 4K.
- **Path A's high case is $47 more than the account holds.** Its expected case leaves about $64; path B's expected case leaves about $105.

The three biggest lines of path A's expected $152: the clips ($110.55, 73%), the character and mob sheets ($20.41, 13%), and sending the clay clip as a video reference on half the takes ($12.94, 9%). Everything else together is $8.

## The rates used

| what | rate | mark | from |
| --- | --- | --- | --- |
| Seedance 2.5 at 4K, from a frame or reference pictures | $0.92129 a second: 4 s $3.69, 5 s $4.61, 6 s $5.52 | `listed` | the model's schema, `info.x-pricing.rates`; never charged to us |
| Seedance 2.5 at 4K with a clip as input | $1.13692 a second when the clip is as long as the shot: 4 s $4.56, 5 s $5.68, 6 s $6.81 | `listed` | the same |
| Seedance 2.5 at 1080p, from a frame or reference pictures | $0.61354 a second: 4 s $2.46, 5 s $3.07, 6 s $3.68 | `charged` | $3.06771 for 5 s and $6.110073 for 10 s on 2026-11-11; equal to the list |
| Seedance 2.5 at 1080p with a clip as input | $0.73415 a second: 4 s $2.94, 5 s $3.67, 6 s $4.40 | `charged` once | $6.45 for an edit of a 9 s clip that came back 8.71 s; the list rate fits it |
| Seedance 2.5 sound | $0 | `charged` | all three charged clips had sound on and paid the plain rate |
| Nano Banana Pro, 1K or 2K | $0.138 an image | `listed` | its schema |
| Nano Banana Pro, 2K with references | $0.1427 an image (seven calls, $0.1413 to $0.1435) | `charged` | ledger, 2026-11-11 |
| Nano Banana Pro, 4K | $0.244 an image | `listed` | its schema |
| caption, Qwen2.5-VL 7B | $0.0013 a picture | `listed` | our catalogue |
| caption, the same | $0.00265 a picture (four calls, $0.0019 to $0.0037) | `charged` | ledger, 2026-11-09 |
| MiniMax Speech 2.8, HD | $0.0001 a character | `listed` | its schema; never used here |
| Fish S2.1 Pro | $0.000015 a byte of text | `listed` | its schema; never used here |
| Mirelo SFX 1.5 | $0.01 a second | `listed` | its schema's overview (its rate line and our catalogue say $0.00025) |
| Mirelo SFX 1.5 | **$0.02 a second** (seven effects, 2 to 10 s) | `charged` | ledger, 2026-11-11 |
| ACE-Step music | $0.0009 to $0.00225 for 60 s | `listed` | our catalogue; its schema |
| ACE-Step music | $0.0018 for 30 s | `charged` | ledger, 2026-11-11 |
| Topaz Proteus, a clip to 4K | $0.0856 for 5.04 s, $0.17 for 8.71 s (about $0.017 to $0.020 a second at 24 fps) | `charged` | zombie test, 2026-11-11 |
| Topaz Proteus, a clip to 4K | $0.15 for 4.8 s at 30 fps ($0.031 a second) | `listed` | its schema, measured |

## What was counted

1. **Captions.** 170 pictures, one caption each. Expected adds 10% asked again and uses the charged mean; high adds 50% (a second question on the action maps) at the dearest charge seen.
2. **Sheet panels.** 110 panels at 2K: seven characters with 4 turnaround views and 3 faces (49); five of them with 6 expressions, hands and a prop (40); one fantasy counterpart each (7); two mobs with about 7 panels each (14). Low is one take a panel at list; expected 1.3 takes at the charged mean; high 2 takes.
3. **Location plates.** Low 3 plates, one take, 2K. Expected 6 plates, 1.5 takes, 2K. High 6 plates, 3 takes, at 4K.
4. **Shot frames.** Low 12 frames, one take, 2K. Expected 12 frames, 2.5 takes, 2K. High 16 frames (12 first frames and 4 last frames), 4 takes, at 4K.
5. **Clips.** The twelve shots as the shot lists time them: three of 4 s, six of 5 s, three of 6 s, 60 s in all. Low one take each; expected two; high three. Counted in frame mode (or from reference pictures, which costs the same).
6. **The clay clip as a video reference.** A separate line, because Runware bills a clip that goes in by its own length on top of the output. Low: never sent. Expected: sent on half the takes. High: sent on every take. The clay clip is taken to be as long as its shot; a longer one costs more.
7. **Spoken lines.** 47 lines, 213 words, taken as 1,150 characters (the script's own text holds 40 lines and 933 characters; the difference is cents). Low: once, on Fish. Expected: twice on MiniMax HD, and ten cue lines twice on Fish. High: five times on MiniMax HD and $0.05 of voice-cloning tries.
8. **Sound effects.** 8 effects on Mirelo. Low 5 s each, once, at the listed $0.01 a second. Expected 8 s each, 1.5 takes, at the charged $0.02. High 10 s each, three takes.
9. **Music.** One 60 s bed on ACE-Step: one, three and six takes. Under two cents in every case.
10. **Topaz**, path B only: the finished 60 s cut, once. Low and expected on the charged rates, high on the listed one.

Not counted, because they are free here: `prompt_check`, the scraper, the storyboard, the Blender stage on this computer, the cut, the title, the screenshots and recordings. Not counted, because the plan forbids it: `rw_enhance`. A request Runware rejects is not billed.

## Path A: native 4K

| line | low | expected | high | price basis |
| --- | --- | --- | --- | --- |
| captions (170 pictures) | 0.22 | 0.50 | 0.94 | `listed` / `charged` / `charged` |
| sheet panels (110) | 15.18 | 20.41 | 31.57 | `listed` / `charged` / `charged` |
| location plates | 0.41 | 1.28 | 4.39 | `listed` / `charged` / `listed` |
| shot frames | 1.66 | 4.28 | 15.62 | `listed` / `charged` / `listed` |
| **clips at 4K** (60 s, 120 s, 180 s billed) | 55.28 | **110.55** | 165.83 | `listed` |
| clay clip as a video reference | 0.00 | 12.94 | 38.81 | `listed` |
| spoken lines | 0.02 | 0.24 | 0.63 | `listed` |
| sound effects | 0.40 | 1.92 | 4.80 | `listed` / `charged` / `charged` |
| music bed | 0.00 | 0.01 | 0.02 | `listed` |
| **total** | **73.17** | **152.13** | **262.61** | |
| left of 215.77 | 142.60 | 63.64 | **short by 46.84** | |

## Path B: 1080p, then Topaz to 4K

| line | low | expected | high | price basis |
| --- | --- | --- | --- | --- |
| captions, sheets, plates, frames | 17.47 | 26.47 | 52.52 | as in path A |
| **clips at 1080p** | 36.81 | **73.63** | 110.44 | `charged` |
| clay clip as a video reference | 0.00 | 7.23 | 21.70 | `charged` once |
| spoken lines, effects, music | 0.42 | 2.17 | 5.45 | as in path A |
| Topaz Proteus, the 60 s cut to 4K | 1.03 | 1.18 | 1.88 | `charged` / `charged` / `listed` |
| **total** | **55.73** | **110.67** | **191.98** | |
| left of 215.77 | 160.04 | 105.10 | 23.79 | |

## What moves the total

- **Takes of clips are the whole story.** One more take of all twelve shots is $55.28 at 4K and $36.81 at 1080p. One more take of a single 5 s shot is $4.61 at 4K.
- **Frame mode or reference mode.** A start frame and references cannot share a call. Reference pictures cost nothing; a clay clip sent as a video reference adds about a fifth to a take ($1.08 on a 5 s take at 4K).
- **Draft first** (`listed`, never tried by us): Seedance 2.5 can make a 480p preview and then render the approved preview at 4K from its draft id. Three previews of every shot at the 480p rate come to $18.66, and one 4K final each to $55.28: $73.94 against $110.55 for two blind 4K takes. Our `rw_video` tool cannot do it (it drops the draft id and has no field to send one), so it needs the raw route. Whether the final is billed at the plain 4K rate is not in our records.
- **4K pictures.** A 4K frame or plate is $0.244 against $0.138 to $0.143.
- **Fewer sheet panels.** The mandatory core (turnaround and three faces for nine sheets, with the mobs at 7 panels) is 63 panels, $8.69 at list; the other 47 are $6.49.

## Money outside this table

- **The GPU pod is RunPod's bill, not Runware's**: about $0.89 an hour while awake (`listed`, the tool's card). The ten meshes and any GPU pass would be one to five hours, $0.89 to $4.45. Its state could not be read this morning and it was not started. On Runware the same meshes are about $0.02 to $0.05 each on TRELLIS.2 (`charged` $0.018 to $0.021 a figure in the zombie test), through the Titanium app's route only.
- **The fal fall-back for a shot** that master prompt step 8 names: Seedance 2.5 on fal is $1.164 a second at 1080p (`listed`, our fal catalogue), $5.82 for a 5 s take, and all twelve shots once would be $69.84. It has no 4K, its arm cuts the prompt at 2,450 characters, and fal refused the zombie test's character twice.

## How the quotes will fall

- The owner's rule is a new yes before any step over $5. At 4K that means every 6 s take ($5.52: shots 1C, 2C, 3D) and every take of 5 s or more that carries a clay clip ($5.68 and up). At 1080p no single take passes $5.
- `rw_video` cannot quote Seedance 2.5 (the model is not in the arm's catalogue; it answers "price known after the call"), and the Titanium app prices it at its 480p from-price, $0.102 a second. Until one of them is corrected, quote from the per-take figures above.
- The Titanium app's own ceiling is $25 a day. Scene 3's first takes at 4K are $27.64.
- Running total to report after each scene, at one take of each shot: scene 1 $13.82, scene 2 $13.82, scene 3 $27.64 at 4K; $9.20, $9.20 and $18.41 at 1080p.
