# 04-prompts: the logic

Everything the agents were told, and everything they then said to the models. This is the part of the repo to read if you want to know *how* the film was made rather than *what* it shows.

| file or folder | what it is |
| --- | --- |
| [`00-MASTER-PROMPT.md`](00-MASTER-PROMPT.md) | the one prompt pasted into Hephaestus as a quest: the story, the look, the fourteen build steps by arm and tool, the continuity rules, the making-of spec, money and permissions |
| `01-CONTINUITY-BIBLE.md` | the law for appearance: the LOOK block, every character's and mob's LOCK BLOCK, the reference tag order, the voice table, the state ladder (wounds, mud and rain accumulate), the location blocks, the camera rules |
| `02-ASSET-PATHS.md` | every input file by path and what the print or build shows; the folders the agents write into |
| `where-each-file-goes.md` | the index of the 21-file pack and where each file was placed |
| [`shots/`](shots/) | per shot, the prompts as assembled and sent: `<shot>.frame.txt` (the frame on Nano Banana Pro), `<shot>.clip.txt` (the clip on Seedance 2.5; `.frame-mode` and `.reference` variants for the two ways the model takes its inputs), and the `faithful/` set that keeps the hand-written body verbatim beside the `shooting-bodies/` set with the director's changes and a `.diff.md` for each |
| [`plates/`](plates/) | the prompt that drew each location plate, with its takes |
| [`sheet-facts/`](sheet-facts/) | the facts fed to `sheet_build` for every character and mob (height in heads, build, age, palette, materials, marks, always and never), one JSON each, and the checker that verifies the drawn panels against them |

The prompts name their input files by the path they had on the production machine, as written; that is the record and it is left as it is. Every such file is in this repository or in the [Drive folder](https://drive.google.com/drive/folders/1FWxTWA6g5YAU0IvnW3phteEQP4Db5o-Y) at the place [`tools/paths.json`](../tools/paths.json) gives for it.

## How a clip prompt is assembled

In this order, every time, so that Seedance performs the lines, the tone and the sound itself:

1. the LOOK block
2. the WORLD block
3. that scene's SCENE block (ambiance, tone, how people speak, sound)
4. the location lock block
5. the lock block of every character and mob in the shot, each with its state line and its reference tags (`[Image1]`, `[Image2]`, bound in the bible's order)
6. the shot body from the shot list, with its dialogue in quotes, the speaker named and the delivery in parentheses
7. the hold line

A LOCK BLOCK is never paraphrased, shortened or passed through a prompt enhancer. A model that drifts gets a reshoot from the same block, never a reworded one.

## Pinned models

One model per job, never the Model Router: Nano Banana Pro (`google:4@2`) for every panel, plate and frame; Seedance 2.5 (`bytedance:seedance@2.5`) for every clip; the same seed on a shot's retakes where the schema allows one.
