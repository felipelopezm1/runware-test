# Quote: the shooting board (16 takes)

Quartermaster, second pass, 2026-11-19, 11:24 UTC. A sum from rates already found, not a bill: no paid tool was called and nothing was generated. Balance **215.7715 USD** (`rw_account`, 2026-11-19, unchanged). Every rate comes from `cost-model.md` or `runware-facts.md` beside this file (step 10's from `voice-casting.md`) and is marked `charged` (a real bill to us) or `listed` (a schema, page or catalogue); the charged rate is used wherever one exists. The board is rev 15: 16 takes, 62 s on screen, 72 s generated.

## The answer

| path | low | expected | high | left at expected | left at high |
| --- | --- | --- | --- | --- | --- |
| **A. Draft at 480p, final at 4K** | $103.31 | **$142.32** | $231.61 | $73.45 | **short by $15.84** |
| **B. Draft at 480p, final at 1080p, one Topaz pass to 4K** | $79.55 | **$112.58** | $183.19 | $103.19 | $32.58 |

**Recommendation: path A, gated by 1A's 4K proof. Approve $177.91**: the expected $142.32 plus 25%, laid out as the five ceilings below, with $37.86 of the balance left untouched. If the proof fails or Runware refuses 4K, path B runs inside the same approval (its ceilings come to $140.73).

- **The first paid clip** is 1A's final at 4K: 5 s in frame mode, **$4.61** (`listed`, never charged to us). Its 480p draft comes first, so the take costs $5.12.
- **Takes over $5 at 4K**, counting the final alone: **2C $6.82, 3A $5.68, 3B $5.68, 3F $5.53**.
- **Days** under the app's ceiling, counting money alone: path A expected needs **6 days at $25, 2 at $100**; path B needs 5 and 2.
- **Path A's high case is $15.84 over the balance.** Cut first: the 4K retakes beyond the four hardest takes ($55.04 in all).

What each case assumes. **Low**: one draft and one final of every take, every picture drawn once, step 10 once. **Expected**: two drafts of every take, one final, and a retake of the final on the four hardest takes (1C-2, 2A-1, 3C-1, 3D-1); 1.3 takes a panel, 2.5 a frame, step 10 twice. **High**: three drafts, one final and a retake of the final on all sixteen; two takes a panel, four a frame at 4K, step 10 twice.

## The rates

Where we have more than one charge, low takes the cheapest seen, expected the mean, high the dearest. Elsewhere one rate serves all three cases.

| what | rate | mark | from |
| --- | --- | --- | --- |
| caption, Qwen2.5-VL 7B | $0.0019 / $0.00265 / $0.0037 a picture (cheapest, mean, dearest of four) | `charged` | ledger 2026-11-09 (`cost-model.md`; `runware-facts.md` 5) |
| Nano Banana Pro, 2K with references | $0.1413 / $0.1427 / $0.1435 an image (cheapest, mean, dearest of seven) | `charged` | ledger 2026-11-11 (`runware-facts.md` 2) |
| Nano Banana Pro, 4K | $0.244 an image | `listed` | its schema (`runware-facts.md` 2) |
| TRELLIS.2, image to mesh | $0.02 a mesh (the zombie test's $0.018 to $0.021 a figure, rounded up); $0.05 in high (the schema's $0.019 to $0.052, top rounded) | `charged` / `listed` | `runware-facts.md` 5 |
| Seedance 2.5 at 480p | $0.1025 a second; $0.1313 with a clip as input | `listed` | S25 `x-pricing` (`runware-facts.md` 1) |
| Seedance 2.5 at 1080p | $0.61354 a second; $0.73415 with a clip as input | `charged` (twice); `charged` once | zombie test (`runware-facts.md` 1) |
| Seedance 2.5 at 4K | $0.92129 a second; $1.13692 with a clip as input | `listed`, never charged | S25 (`runware-facts.md` 1) |
| Seedance 2.5 sound | $0 | `charged` | three clips with sound on paid the plain rate |
| Topaz Proteus, a 24 fps clip to 4K | $0.016984 / $0.018589 / $0.019518 a second ($0.0856 for 5.04 s; both charges pooled, $0.2556 for 13.75 s; $0.17 for 8.71 s) | `charged` | zombie test (`cost-model.md`) |
| the 40 lines (13 MiniMax HD, 27 Fish) and five anchors | $0.132005 a round | `listed` | `voice-casting.md` 5 |
| Mirelo SFX 1.5: 36 cues, 157 s | $0.02 a second, $3.14 a round | `charged` | ledger 2026-11-11 (`voice-casting.md` 3, 5) |
| ACE-Step: the 60 s bed | $0.002 a round | `charged` basis ($0.0018 for 30 s) | `voice-casting.md` 4 |
| the audition: 38 calls | $0.17598 | `listed` | `voice-casting.md` 6 |
| Qwen3-TTS VoiceDesign, Vessa (decision 14) | $0.000015 a character; her 186-character anchor is $0.00279 a try | `listed` | `voice-casting.md` 7, question 1 |

## The lines

### 1. Captions

166 pictures, once each. These are the still model inputs in `inputs/manifest.json`: 29 prints, 79 build photos, 31 action maps, 17 mob prints, 6 group photos and 4 scale photos. The six clips and animations are not captioned.

| | low | expected | high |
| --- | --- | --- | --- |
| pictures | 166 | 166 | 166 |
| rate | $0.0019 `charged` | $0.00265 `charged` | $0.0037 `charged` |
| **cost** | **$0.32** | **$0.44** | **$0.61** |

### 2. Sheet panels

**116 panels, not 112.** The sheet-facts README says "Panels to draw in all: 116 ... it was 112 before the toad's four views", and a count of the nine sheet files agrees: five characters at 16, Sylwen and Oswin at 8, the two mobs at 8, and the toad's 4. All are at 2K with references.

| | low | expected | high |
| --- | --- | --- | --- |
| panels x takes | 116 x 1.0 | 116 x 1.3 = 150.8 | 116 x 2.0 = 232 |
| rate | $0.1413 `charged` | $0.1427 `charged` | $0.1435 `charged` |
| **cost** | **$16.39** | **$21.52** | **$33.29** |

At 112 panels it would be $15.83, $20.78 and $32.14.

### 3. Location plates

As in the cost model: low is 3 plates once at 2K; expected is 6 plates at 1.5 takes, 2K; high is 6 plates at 3 takes, 4K.

| | low | expected | high |
| --- | --- | --- | --- |
| plates x takes | 3 x 1 | 6 x 1.5 = 9 | 6 x 3 = 18 |
| rate | $0.1413 `charged` | $0.1427 `charged` | $0.244 `listed` (4K) |
| **cost** | **$0.42** | **$1.28** | **$4.39** |

### 4. Shot frames

**4a. First frames.** 14 are drawn: the 16 takes less 2A-2 and 3C-2, which start on `cut_frame` at 2.0 s of the take before (free). Board rev 15 has both as `continuous`. A reference-mode take still gets its frame, because the frame rides as its first picture.

| | low | expected | high |
| --- | --- | --- | --- |
| frames x takes | 14 x 1 | 14 x 2.5 = 35 | 14 x 4 = 56 |
| rate | $0.1413 `charged` | $0.1427 `charged` | $0.244 `listed` (4K) |
| **cost** | **$1.98** | **$4.99** | **$13.66** |

**4b. Last frames for 1C-1 and 3D-2.** These are the two frame-mode takes whose mode line in `shot-table.md` says "a last frame ... is worth giving". They are not in the brief; I added them so the quote covers what the table asks for.

| | low | expected | high |
| --- | --- | --- | --- |
| frames x takes | 0 | 2 x 2.5 = 5 | 2 x 4 = 8 |
| rate | | $0.1427 `charged` | $0.244 `listed` (4K) |
| **cost** | **$0.00** | **$0.71** | **$1.95** |

High draws frames and plates at 4K, as the first cost model did. Path B would not need 4K pictures; at 2K its high case would be $8.24 lower.

### 5. Meshes

Ten meshes: the seven characters, one frog, one toad and the worm's head. They are made on Runware's TRELLIS.2 through the app's raw route (decision 12) instead of on the GPU pod.

| | low | expected | high |
| --- | --- | --- | --- |
| meshes x tries | 10 x 1 | 10 x 2 | 10 x 3 |
| rate | $0.02 `charged` | $0.02 `charged` | $0.05 `listed` |
| **cost** | **$0.20** | **$0.40** | **$1.50** |

### 6. Clips, path A: draft at 480p, final at 4K

- **Seconds generated, not seconds on screen: 72 s.** Ten frame-mode takes come to 44 s. Six reference-mode takes come to 28 s: 1C-2 4, 2A-1 4, 2C 6, 3A 5, 3B 5 and 3D-1 4. Both counts come from `shot-table.md`'s rows.
- **A reference-mode take carries the clay clip as a reference video on its drafts and its final**, billed at the "with a clip as input" rate. The clay clip is taken to be as long as the generated take; a longer one costs more (inferred from one charged edit).
- **Draft then final is listed in Seedance 2.5's schema but has never been tried by us.** The final is a second call with `inputs.draftId` alone, which goes through the app's raw route because `rw_video` has no field for it. **Whether a final is billed at the plain 4K rate is unknown.** Here a final is priced as a fresh 4K take of its mode.
- A retake of a final renders another of that take's drafts already made, so it adds no draft. Low has no retakes.
- Sound is on and costs nothing (`charged`). `numberResults` is 1.

**One take at each resolution** (the 480p draft and the 4K final are `listed`; the 1080p final is `charged`):

| take | scene | mode | s generated | 480p draft | 1080p final | 4K final |
| --- | --- | --- | --- | --- | --- | --- |
| 1A | 1 | frame | 5 | $0.51 | $3.07 | $4.61 |
| 1B | 1 | frame | 4 | $0.41 | $2.45 | $3.69 |
| 1C-1 | 1 | frame | 4 | $0.41 | $2.45 | $3.69 |
| 1C-2 | 1 | reference | 4 | $0.53 | $2.94 | $4.55 |
| 2A-1 | 2 | reference | 4 | $0.53 | $2.94 | $4.55 |
| 2A-2 | 2 | frame | 4 | $0.41 | $2.45 | $3.69 |
| 2B | 2 | frame | 4 | $0.41 | $2.45 | $3.69 |
| 2C | 2 | reference | 6 | $0.79 | $4.40 | $6.82 |
| 3A | 3 | reference | 5 | $0.66 | $3.67 | $5.68 |
| 3B | 3 | reference | 5 | $0.66 | $3.67 | $5.68 |
| 3C-1 | 3 | frame | 4 | $0.41 | $2.45 | $3.69 |
| 3C-2 | 3 | frame | 4 | $0.41 | $2.45 | $3.69 |
| 3D-1 | 3 | reference | 4 | $0.53 | $2.94 | $4.55 |
| 3D-2 | 3 | frame | 4 | $0.41 | $2.45 | $3.69 |
| 3E | 3 | frame | 5 | $0.51 | $3.07 | $4.61 |
| 3F | 3 | frame | 6 | $0.62 | $3.68 | $5.53 |
| **one round of all 16** | | | **72** | **$8.19** | **$47.55** | **$72.37** |

**Path A by scene.** Totals are the exact sums rounded to the cent; a component rounded on its own can be a cent off.

| scene | takes | case | drafts | 4K finals | 4K retakes | total |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 1A, 1B, 1C-1, 1C-2 (13 s frame, 4 s reference) | low | 1 x $1.86 | $16.52 | none | **$18.38** |
| | | expected | 2 x $1.86 = $3.72 | $16.52 | 1C-2 $4.55 | **$24.79** |
| | | high | 3 x $1.86 = $5.57 | $16.52 | all four $16.52 | **$38.62** |
| 2 | 2A-1, 2A-2, 2B, 2C (8 s frame, 10 s reference) | low | 1 x $2.13 | $18.74 | none | **$20.87** |
| | | expected | 2 x $2.13 = $4.27 | $18.74 | 2A-1 $4.55 | **$27.55** |
| | | high | 3 x $2.13 = $6.40 | $18.74 | all four $18.74 | **$43.88** |
| 3 | 3A, 3B, 3C-1, 3C-2, 3D-1, 3D-2, 3E, 3F (23 s frame, 14 s reference) | low | 1 x $4.20 | $37.11 | none | **$41.30** |
| | | expected | 2 x $4.20 = $8.39 | $37.11 | 3C-1 $3.69, 3D-1 $4.55 = $8.23 | **$53.73** |
| | | high | 3 x $4.20 = $12.59 | $37.11 | all eight $37.11 | **$86.80** |
| **all** | 16 | low / expected / high | | | | **$80.55 / $106.07 / $169.30** |

### 7. Clips, path B: draft at 480p, final at 1080p, then Topaz

This path uses the same drafts and the same retakes, with finals at 1080p (`charged`). A 1080p final from a draft id is just as untried as a 4K one; 1080p without a draft is the way we have been charged.

| scene | case | drafts | 1080p finals | 1080p retakes | total |
| --- | --- | --- | --- | --- | --- |
| 1 | low | $1.86 | $10.91 | none | **$12.77** |
| | expected | $3.72 | $10.91 | 1C-2 $2.94 | **$17.56** |
| | high | $5.57 | $10.91 | $10.91 | **$27.40** |
| 2 | low | $2.13 | $12.25 | none | **$14.38** |
| | expected | $4.27 | $12.25 | 2A-1 $2.94 | **$19.45** |
| | high | $6.40 | $12.25 | $12.25 | **$30.90** |
| 3 | low | $4.20 | $24.39 | none | **$28.59** |
| | expected | $8.39 | $24.39 | 3C-1 $2.45, 3D-1 $2.94 = $5.39 | **$38.17** |
| | high | $12.59 | $24.39 | $24.39 | **$61.37** |
| **all** | low / expected / high | | | | **$55.74 / $75.18 / $119.67** |

**Topaz Proteus on the cut.** The 62 s of takes at 24 fps (the board's frame rate and the charged runs' rate) cost 62 x $0.016984 / $0.018589 / $0.019518 = **$1.05 / $1.15 / $1.21** (`charged`). If the 1.5 s fade and the 2 s title go through it too (65.5 s), add at most $0.07. The title is better made at 4K by `title_render`, which is free.

### 8. Voices, cues, music

These figures are from `voice-casting.md` part 5, recomputed from `voice-casting.json`. They are made once in low and twice in expected and high, so expected and high are the same.

| item | a round | mark | low (x1) | expected (x2) | high (x2) |
| --- | --- | --- | --- | --- | --- |
| the 40 lines and the five anchors | $0.1320 | `listed` | $0.1320 | $0.2640 | $0.2640 |
| 36 Mirelo cues, 157 s at $0.02 | $3.1400 | `charged` | $3.1400 | $6.2800 | $6.2800 |
| the ACE-Step bed, 60 s | $0.0020 | `charged` basis | $0.0020 | $0.0040 | $0.0040 |
| the audition, 38 calls | $0.1760 | `listed` | $0.1760 | $0.3520 | $0.3520 |
| Vessa's voice designed in words, her 186-character anchor | $0.0028 | `listed` | $0.0028 | $0.0056 | $0.0056 |
| **line 8** | | | **$3.45** | **$6.91** | **$6.91** |

The cues are 91% of this line, and only because Runware charges Mirelo $0.02 a second against the $0.00025 it lists. `rw_audio` will quote cues at the listed rate, so quote them from here.

### 9. The first 4K proof

1A's final, alone, at 4K: frame mode, 5 s x $0.92129 = **$4.61** (`listed`). This would be the first 4K Seedance charge on our account. It sits inside scene 1 of line 6. Its 480p draft comes first (5 s x $0.1025 = $0.51), so the take costs $5.12.

How to read the result:

- If Runware charges anything other than $4.61, every 4K figure here moves by the same ratio. Stop and quote again before 1B.
- If 4K is refused (a refusal is not billed) or the clip comes back short of 3840x2160, switch to path B before any other final. At that point at most $5.12 has been spent.

## Totals by path

The pre-clip lines are the same in both paths. Every total is the sum of the rounded lines above it.

| line | A low | A expected | A high | B low | B expected | B high |
| --- | --- | --- | --- | --- | --- | --- |
| 1 captions | 0.32 | 0.44 | 0.61 | 0.32 | 0.44 | 0.61 |
| 2 sheet panels | 16.39 | 21.52 | 33.29 | 16.39 | 21.52 | 33.29 |
| 3 plates | 0.42 | 1.28 | 4.39 | 0.42 | 1.28 | 4.39 |
| 4a first frames | 1.98 | 4.99 | 13.66 | 1.98 | 4.99 | 13.66 |
| 4b last frames | 0.00 | 0.71 | 1.95 | 0.00 | 0.71 | 1.95 |
| 5 meshes | 0.20 | 0.40 | 1.50 | 0.20 | 0.40 | 1.50 |
| **pre-clip** | **19.31** | **29.34** | **55.40** | **19.31** | **29.34** | **55.40** |
| clips, scene 1 | 18.38 | 24.79 | 38.62 | 12.77 | 17.56 | 27.40 |
| clips, scene 2 | 20.87 | 27.55 | 43.88 | 14.38 | 19.45 | 30.90 |
| clips, scene 3 | 41.30 | 53.73 | 86.80 | 28.59 | 38.17 | 61.37 |
| Topaz on the cut | 0.00 | 0.00 | 0.00 | 1.05 | 1.15 | 1.21 |
| 8 voices, cues, music | 3.45 | 6.91 | 6.91 | 3.45 | 6.91 | 6.91 |
| **total** | **103.31** | **142.32** | **231.61** | **79.55** | **112.58** | **183.19** |
| left of 215.7715 | 112.46 | 73.45 | **-15.84** | 136.22 | 103.19 | 32.58 |

**Path A's high case is $15.84 more than the account holds.** Retakes go first, before anything else. The 4K retakes of the twelve takes outside the hardest four come to $55.04 (72.37 for all sixteen less 17.33 for the four). Cut them by the shot table's risk, lowest first: 3A (LOW, $5.68), then the MEDIUM takes in story order, 1B ($3.69), 1C-1 ($3.69) and 2C ($6.82). That is $19.88, which closes the gap with $4.04 to spare. With all twelve cut, the high case is $176.57 and leaves $39.20. Path B's high case fits, with $32.58 left.

## Ceilings: expected plus 25%

These are the stops for HANDOFF decision 10. Report the running total after each part; a part that would pass its ceiling stops for a new quote.

**Path A (recommended).**

| part | what is in it | expected | ceiling | running total, expected |
| --- | --- | --- | --- | --- |
| pre-clip | captions, 116 panels, plates, 14 first frames, 2 last frames, 10 meshes | 29.34 | **36.68** | 29.34 |
| scene 1 clips | 1A (the proof), 1B, 1C-1, 1C-2 | 24.79 | **30.99** | 54.13 |
| scene 2 clips | 2A-1, 2A-2, 2B, 2C | 27.55 | **34.44** | 81.68 |
| scene 3 clips | 3A, 3B, 3C-1, 3C-2, 3D-1, 3D-2, 3E, 3F | 53.73 | **67.16** | 135.41 |
| sound | lines, anchors, cues, bed, audition, Vessa's design | 6.91 | **8.64** | 142.32 |
| **all** | | **142.32** | **177.91** | |

**Path B (the fall-back, by the same rule).**

| part | expected | ceiling | running total, expected |
| --- | --- | --- | --- |
| pre-clip | 29.34 | **36.68** | 29.34 |
| scene 1 clips | 17.56 | **21.95** | 46.90 |
| scene 2 clips | 19.45 | **24.31** | 66.35 |
| scene 3 clips | 38.17 | **47.71** | 104.52 |
| Topaz on the cut | 1.15 | **1.44** | 105.67 |
| sound | 6.91 | **8.64** | 112.58 |
| **all** | **112.58** | **140.73** | |

If the shoot switches from A to B partway, the parts not yet started take B's ceilings and the part in progress keeps its A ceiling.

## Takes over $5 at 4K

| take | mode, s | 4K final alone | with its two expected 480p drafts | with a 4K retake as well |
| --- | --- | --- | --- | --- |
| **2C** | reference, 6 | **$6.82** | $8.40 | |
| **3A** | reference, 5 | **$5.68** | $7.00 | |
| **3B** | reference, 5 | **$5.68** | $7.00 | |
| **3F** | frame, 6 | **$5.53** | $6.76 | |
| 1A | frame, 5 | $4.61 | $5.63 | |
| 3E | frame, 5 | $4.61 | $5.63 | |
| 1C-2 | reference, 4 | $4.55 | $5.60 | $10.15 |
| 2A-1 | reference, 4 | $4.55 | $5.60 | $10.15 |
| 3D-1 | reference, 4 | $4.55 | $5.60 | $10.15 |
| 3C-1 | frame, 4 | $3.69 | $4.51 | $8.19 |

The other six takes stay under $5 even with two drafts ($4.51 each). At 1080p no final passes $5 (the dearest, 2C, is $4.40); with its two drafts 2C is $5.98. This is why decision 10 trades the "new yes over $5" rule for the ceilings above.

## Days under the app's ceiling

The app's ceiling (`TITANIUM_DAILY_CAP_USD`) counts only the calls that go through the app: every raw task, which means panels, plates, frames, meshes, clips, Topaz and Vessa's design. The captions (`rw_caption`) and the voices, cues, bed and audition (`rw_audio`) go through the arm and the app does not count them: $7.34 at expected.

| path, case | spend through the app | days at $25 | days at $100 |
| --- | --- | --- | --- |
| A low | 99.54 | 4 | 1 |
| **A expected** | **134.98** | **6** | **2** |
| A high | 224.10 | 9 | 3 |
| B low | 75.78 | 4 | 1 |
| B expected | 105.24 | 5 | 2 |
| B high | 175.68 | 8 | 2 |

Days are the spend divided by the ceiling, rounded up: the fewest the money allows. If each part above starts on a fresh day instead, path A expected takes 8 days at $25 (2 + 1 + 2 + 3; scene 3 alone is $53.73) and 4 at $100. Path B takes 6 at $25 (2 + 1 + 1 + 2) and 4 at $100. Raising the ceiling to $100 (decision 11) lets each scene finish in one day.

Two facts about the ceiling decide whether these days mean anything. Both are from the app's code (`src/lib/guard/spend.ts`, `src/lib/guard/index.ts`, `src/app/api/runware/run/route.ts` in the `runware-hephaestus-control` iron):

- **It counts the `cost` the caller sends with a raw task.** Without one, it counts the app's own unit price for the model: $0.102 for Seedance 2.5, whatever the take's length and resolution. It never reads what Runware charges later, because every task starts async and is charged at the status poll. **So each raw call must send its figure from this quote as `cost`.** Otherwise a day of 4K takes counts as cents and the ceiling never brakes.
- **It is checked before a call starts** (`spent < cap`), so the last call of a day can take the day over by up to one call ($6.82 at most). The count is also held in memory per server instance, and it resets at midnight UTC and on a cold start. As its own comment says, it is a brake, not accounting.

## What moves the total

- **Retakes of finals move the total most.** One more 4K final of every take is $72.37 ($47.55 at 1080p); a 4K retake of a single take is $3.69 to $6.82. Drafts are cheap: a round of all 16 at 480p is $8.19.
- **What the final bills is unknown.** Every final here is priced at the plain 4K rate (or the clip-as-input rate). If a draft-id final bills more, path A moves with it; the 1A proof shows it first.
- **The two carries, 2A-2 and 3C-2, depend on their parent take.** Each carry's start frame is cut from the parent's picked clip. Draft a carry only after 2A-1 or 3C-1 is settled, retake and all. Otherwise a picked retake throws the carry away: $4.51 at 4K with two drafts, $3.27 at 1080p.
- **Billing by frame shifts each take by a fraction of a percent.** The per-second rates are exact for a 5 s take: billing by 24 x s + 1 frames fits every Seedance charge to the cent. A 4 s take bills about 0.2% more and a 6 s take about 0.1% less. That is under $0.15 over all of path A, and it is not added.
- **Sheets at 116 rather than 112** add $0.57, $0.74 and $1.15 in the three cases.

## Not counted

- **Free here:** `prompt_check`, `cut_frame`, `sheet_build` and `sheet_render`, the Blender stage (stages, blocking, passes, armatures), `board_cut`, `title_render`, `cut_edit`, uploads, screenshots and recordings.
- **Not used:** `rw_enhance` (forbidden), the GPU pod (decision 12 moves the meshes to Runware) and fal.
- **Not billed:** a task Runware refuses.
- **Optional extras left out:** Vel's and Sylwen's anchors ($0.0336 a round) and Mirelo foley made from a finished clip.

## Against the first cost model

The first pass (`cost-model.md`) priced 12 shots and 60 s on two blind takes: $152.13 for path A and $110.67 for path B, expected. This quote prices the shooting board instead:

- 16 takes and 72 s generated (four splits, each generated at Seedance's 4 s minimum).
- 480p drafts in place of a second blind final.
- The clay clip on the six reference-mode takes (28 s), not on half of every take.
- 116 panels instead of 110.
- Step 10 from `voice-casting.md` at $6.91 instead of $2.17.
- Captions once.
- 14 first frames and 2 last frames instead of 12.
- Meshes on Runware.

The net effect is that path A falls by $9.81 and path B rises by $1.91.

## How this was checked

- **Every line recomputed.** A script recomputed every line from the rates above; nothing from it was saved in the project.
- **Every total re-added.** A second script read this file's tables back and re-added every total, ceiling, running total and balance.
- **The seconds counted.** The 72 generated seconds and the 28 reference-mode seconds were counted from `shot-table.md`'s rows: 10 frame-mode takes at 44 s, 6 reference-mode takes at 28 s.
- **The panels counted.** The 116 panels were counted from the nine sheet files.
- **Step 10 recomputed.** Step 10's figures were recomputed from `voice-casting.json`: 40 lines, 36 cues, 157 s, $3.274005 a round before the audition.
