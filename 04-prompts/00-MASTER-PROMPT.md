# MASTER PROMPT: "Is this all on Runware?"
### A one-minute hyper-realistic fantasy short, made on Runware through Hephaestus

Paste everything below the line into Hephaestus as one quest. The files it refers to sit in `/home/felipe-lopez/Desktop/Runware Test/`.

---

Hephaestus, this is a production quest on Runware. Make a 60-second hyper-realistic fantasy short called **"Is this all on Runware?"** from the pre-production I built by hand in `/home/felipe-lopez/Desktop/Runware Test/`: seven 3D-printed character minis and two mob prints photographed in turnaround, three scene builds with clay walls, and the "Scene N Actions" maps drawn over the build photos, where **blue arrows are movement and sound, red arrows are attacks, green arrows are a character's reaction or emotion**. Every shot comes from Seedance 2.5 on Runware at 4K, through the Runware arm and the Titanium studio's account, the way the zombie test was made. Record every step as you go: the record is a deliverable. Nothing paid is sent before you quote it and I say yes.

The pack beside this prompt is yours to work from, and yours to change. Where a shot, a prompt, a tool or a step works better another way, or fails, change it: reshape a shot, split or merge takes, pick another move, reorder steps, swap a model for one that holds the look better. Keep three things fixed: the story and its ending, each character's identity (the LOCK BLOCKS), and the honesty of the log. Write every change you make and why in the log.

## 1. The files
- `Original Prompt/00-MASTER-PROMPT.md` is this prompt. `Original Prompt/01-CONTINUITY-BIBLE.md` is the law for appearance: every LOCK BLOCK, the reference order, the voice table, the state ladder, the location blocks. `Original Prompt/02-ASSET-PATHS.md` lists every input file by path and what it shows, and the folders you write into. Read all three first, then the brief in `Creative Task Runware/Task/In Short.md` and `Creative Task Runware/Task/Runware_Creative Engineer Assessment (1).pdf`.
- The cast: `Creative Task Runware/Script/Characters/Character 1/` to `Character 7/` (four turnaround photos each), `Mob 1/`, `Mob 2/`, `All together/`, `Size from afar/`. The character sheets I wrote go in each character's `Persona_Character Sheet/` folder; the mob sheets in `Creative Task Runware/Script/Setting & Look & Feel Descriptions/Mobs & Enemies/`.
- The scenes: `Creative Task Runware/Pre Production Assets/Scenes/Scene 1/`, `Scene 2/`, `Scene 3/`, each with its build photos and its `Scene N Actions/` maps. The direction for each scene (environment and shot list) is in `Creative Task Runware/Script/Script (Scene 1 to 3)/Scene N (Direction & Description)/`; the script in `Script Final/SCRIPT.md`; the three ambiances as one place in `Setting & Look & Feel Descriptions/Environment/Castle at night/`.
- My own footage of the build is under `Pre Production Assets/B Roll/`: list it in the log for the making-of, never use it as a model input.

## 2. What we are making

A party of seven is deep in an abandoned dungeon under a fallen castle, low on supplies, on a quest they do not understand. Three scenes, one film, 16:9, Seedance 2.5 at 4K (fall-back: 1080p and a Topaz upscale to 4K):

| scene | length | where | what happens |
| --- | --- | --- | --- |
| 1 | 15 s | the storeroom under the stairs | the party rests and argues over the last of the food; the dwarf's lantern is the only light; poisonous frogs and toads pour down the staircase and burst out of the barrels; the party fights its way up the stairs |
| 2 | 15 s | the corridor | the party advances down a long flooded corridor finishing the frogs and toads; the priest's water magic does nothing to amphibians; the leader notices the frogs were running *from* something |
| 3 | 30 s | the roofless hall of the fallen castle, open to a cold starry night | a gigantic earthworm coiled round a mound of rubble in reeking mud rears up screaming; the elf is caught in its coil and heals from inside it; rain begins mid-fight; the barbarian man's jump and the undead necromancer's final blast kill it; smash cut to all seven looking up at the stars, and the dwarf asks: "...is this all on Runware?" |

The cast: **Sera'kith Vel** (Character 6, githyanki leader, rapier and acid pots, the lead), **Mordecai Ashgrave** (Character 7, undead necromancer with a horned helmet who casts from his hands, her rival for "strongest"), **Vessa Rowanblood** (Character 1, barbarian woman, red hair, shield, greatsword broken at the tip), **Dax Vorrune** (Character 3, half-githyanki barbarian, sword broken through the middle, jumps and slips), **Borrin Hollowcask** (Character 2, dwarf, the lantern hangs from his axe, half drunk), **Sylwen Aerindel** (Character 4, elf healer, no weapon), **Father Oswin Tallow** (Character 5, old human priest, crystal staff, water magic). **Mob 1** is the swarm of poisonous frogs and toads. **Mob 2** is the earthworm (the pink articulated print is its stand-in: its big round "eye" marks the mouth end, its cowl is the swollen collar, its shed crescent plates are the skin it sloughs).

## 3. The look

Hyper-realistic live-action fantasy: real skin, real cloth, wet stone, lantern light that falls off into black. Modern photoreal cinema, anamorphic character inside a 16:9 frame, 35 mm and 50 mm lenses for groups, 85 mm for faces, shallow depth of field on faces and deep focus on the wide shots. Palette: lantern amber, cold slate blue, moss green, bone white, acid yellow-green only on Vel's pots and Mordecai's flame. No cartoon, no game-engine sheen, no text on screen, no watermark. Nothing in frame reads as a toy, a print or a miniature: the prints and the clay walls are the *plan* of each shot (silhouette, pose, costume pieces, weapon shapes, blocking, camera); the output is flesh and stone.

## 4. How to build it, in order

Work through the plays `storyboard-a-film`, `runware-first`, `image-to-3d` and `reshoot-a-shot`. Use these arms, by these names. The zombie test is only the idea of what to produce: the same kind of asset set (sheets, realistic and fantasy counterparts, rigged 3D stand-ins, clay passes, takes, a making-of), made fresh from these files.

1. **Read the folder first.** Open every file `02-ASSET-PATHS.md` lists: the brief, each character's four photos, each scene's build photos, each action map. Use `rw_caption` (Runware) on each print photo, each build photo you will match and each action map, and write what you see into the log beside my notes. Match the shot lists to what the maps show; where my map and the shot list disagree, the map wins and you note the change.
2. **Gather references with the scraper.** `find_references` (openly licensed, Openverse and Wikimedia Commons) and `grab_media` for: wet medieval cellar masonry, stone staircases in crypts, torch-lit vaulted corridors, roofless castle halls at night under stars, the Milky Way over ruins, poison dart frogs and cane toads up close, earthworm skin macro, a bubbling mud flat, a swept-hilt rapier, a bearded long-hafted axe, a heater shield, woad tattoos, a conical nasal helmet, githyanki concept descriptions. Keep author and licence on each. Use `rw_caption` to turn the best references into precise material and light descriptions and feed those words into the style bible. Where a reference has no commercial licence, use it for description only, never as an image input.
3. **Storyboard on paper.** Load `director:storyboard-director`. `film_grammar` for the style, moves and engines. `board_save` the design draft: logline, destination, concept, the seven characters, the two mobs, the three locations and the props declared once with the ids in the bible. Then the production draft: the Fountain script from `SCRIPT.md` and every shot from the three shot lists, with `duration`, `size`, `angle`, `move`, `lens`, `cast`, `dialogue`, `sound`, `beats` and `continuity`. Show me the storyboard and wait for my yes before anything is generated.
4. **Character sheets (the character design maker).** For each of the seven characters and both mobs: `sheet_build` with the facts from its sheet file (height in heads, build, age, palette swatches, materials, marks, always and never). Draw the panels with `rw_image` on **Nano Banana Pro (`google:4@2`)** with that character's four print photos as `references` so the silhouette, pose and costume pieces are mine, and the LOCK BLOCK as the prompt. Run `prompt_check` before each draw. File the panels back with `sheet_build panels`, then `sheet_render`. The turnaround and the three faces are mandatory for every character; expressions, hands and prop for the five who speak most (Vel, Mordecai, Vessa, Dax, Borrin). Each character also gets one **fantasy counterpart** panel (full body in costume, their real look, in the storeroom's light) and one **realistic 3D counterpart** render from step 5. Save each sheet and its panels into that character's `Persona_Character Sheet/` folder.
5. **3D counterparts and the stage.** `cast_mesh` (Pixal3D from the four rendered turnaround views) for each character, for one frog, one toad and the worm's head; on the Blender stage, `scene_build` each location from its environment file, `scene_place` the meshes where the build photos and action maps put them, and render a turntable of each character with `scene_render`. Give each humanoid mesh a skeleton (an armature through `scene_python`, asking me first) so the blocking can pose it: Dax's jump, Vessa flat behind her shield, Mordecai's arms wide, Sylwen inside the coil. If the GPU pod is asleep, stop and ask me before waking it. Save the turntables and stage renders into each character's `3D Model Assets (Images)/` folder (make that folder and `Persona_Character Sheet/` for Characters 2 to 7 and the mobs, as Character 1 has them).
6. **Block every shot.** `scene_block` each shot of the shot lists on its location's stage scene, with the cast meshes at the positions and facings the build photos and action maps give, and `scene_pass` the clay clip, depth, normals, lines and `cameras.json`. The clay clip is the locked camera and motion guide of that shot. Save the clay clip's first frame as the shot's layout reference. Copies go to `Creative Task Runware/Assets/Scene N/`.
7. **Frames.** For each shot, `rw_image` on Nano Banana Pro: the shot's video prompt as the image prompt (minus the timeline and the dialogue), with references in this order: the clay first frame (layout), each present character's face-front and front-turnaround panels (identity), the location plate (place), then any scraped material reference. `prompt_check` before. Lock the frame when I approve it on the board; within a scene, the next shot's first frame is the last frame of the previous clip wherever the shot list says `continuous`.
8. **Clips on Seedance 2.5 at 4K.** `rw_models` to confirm the AIR id `bytedance:seedance@2.5` and read its schema (resolutions, `frameImages`, `referenceImages`, video references, audio, seed). **Check 4K first**: if the schema lists a 4K (2160p) resolution, every clip is made at 4K; if it lists 1080p at most, make every clip at 1080p and upscale the finished cut with Topaz Proteus to 4K (step 11), and write which path you took in the log. Then `rw_video` per shot with: the approved frame as the first frame, the next shot's frame as the last frame where the shot list gives one, every present character's face panel as a reference (named `[Image1]`, `[Image2]`... in the prompt exactly as the bible binds them), the clay clip as a reference where the schema takes a video reference, `resolution` 4K (or 1080p on the fall-back), 16:9, the shot's exact duration (4 to 30 s), audio on, and the shot's assembled prompt (step 9) verbatim. If Runware's Seedance 2.5 schema does not take the clay clip, fall back for that shot to `fal_video` `seedance-25` with `guide: true` and `video` set to the clay clip, and say so in the log. Never let the Model Router pick: every shot is pinned to the same AIR id. Keep every take, rate each, pick one per shot with me; copies of the picks go to `Creative Task Runware/Final Shot/`.
9. **How every clip prompt is assembled**, in this order: the LOOK block; the WORLD block; that scene's SCENE block (ambiance, tone, how people speak, sound); the location lock block; the lock block of every character and mob in the shot, each with its state line and its reference tags; the shot body from the shot list verbatim, with its dialogue in quotes, speaker named, delivery in parentheses, so Seedance performs the lines, the tone and the sound itself; then the hold line. The prompts in the shot lists are written to this shape; when you change a shot, keep the shape.
10. **Voices and sound.** Every line in the script in that character's voice with `rw_audio` (MiniMax Speech 2.8 by default; Fish S2.1 Pro where a line needs a cue such as a hiccup or a scream), the voice notes in the bible's table. The frogs' chorus, the worm's scream, rain, the lantern and steel with `rw_audio` Mirelo SFX. A quiet low-string bed with ACE-Step, 60 s, no lyrics. Where Seedance's own sound on a clip is better, keep it and skip the foley for that shot.
11. **The cut.** `board_attach` every take, then `board_cut`: shots in order, lines under their shots, cues, the rain building through scene 3, a hard smash cut into the final shot and a 1.5 s hold on black after the last line. 16:9, 24 fps, 60 s plus or minus 2. On the 1080p fall-back only: `rw_upscale` the finished cut with **Topaz Proteus to 4K** (quote first), and keep both. On native 4K, keep the 4K master and render a 1080p copy with `cut_edit`. Both go to `Creative Task Runware/Final Video/`.
12. **Title.** `title_render` one title card, "Is this all on Runware?", white serif on black, 2 s, laid over the final black by `cut_edit`. Nothing else written on screen.
13. **Masks and passes where needed.** `mask_video` for the final smash cut if the sky needs replacing, and `depth_video` on the worm shots if a shot needs a relight. Optional.
14. **The showcase around the film.** The brief in `Task/` asks for a social post and a draft piece for the Runware website beside the showcase. From the log, draft both as pots: a builder's post (X or LinkedIn) with the frames it would carry, and an outline for a Runware website piece ("seven minis and a worm: a 60 s film on Seedance 2.5 through one API") with the key points, the pipeline and the costs. Drafts for me to rewrite, not to publish.

## 5. Continuity: the rule above all rules

- A character's **LOCK BLOCK** from the bible is pasted unchanged into every image and video prompt that shows them. Never paraphrase it, never shorten it, never let `rw_enhance` touch it.
- Their **face-front panel and front turnaround** ride as references on every frame and every clip they appear in; their print photos are references too until the sheet exists, and then the sheet replaces them.
- Weapons never change hands, length or colour: Vessa's greatsword is broken at the top third and her shield is on her left arm, Dax's sword is broken through the middle and held in both hands, Vel's rapier is silvered with a swept black hilt, Borrin's lantern hangs under his axe head, Mordecai has no weapon and casts green flame from his hands, Oswin's staff carries a clear faceted crystal, Sylwen carries nothing.
- Wounds, mud and rain accumulate and never reset: the bible's **state ladder** says what each character looks like at each shot.
- Costumes, skin tones, hair and ears are described with the same words every time. Where a model drifts, reshoot with the `reshoot-a-shot` play from the same block; never fix a face by changing the words.
- One pinned model per job: Nano Banana Pro for every frame and panel, Seedance 2.5 for every clip, the same `seed` on a shot's retakes where the schema allows one.
- `prompt_check` before every paid call, and after each render with `seen` set to what the take shows; a failed rule means a reshoot, not a new prompt.

## 6. Record everything: the making-of log

We will cut a making-of from this, so the record is a deliverable, not a by-product. Keep it in one folder, `.hephaestus/storyboards/<storyboard id>/making-of/`, with this shape:

```
making-of/
  log.md            the human log, one entry per step (below)
  log.jsonl         the same entries as one JSON line each (step, at, arm, tool, model, air, inputs[], prompt, quote, charged, outputs[], decision, change, note)
  screens/          screenshots, named NNN-<step>-<what>.png, numbered in the order they were taken
  clips/            screen recordings and process clips, named NNN-<step>-<what>.mp4 or .webm
  takes/            every generated frame and clip, kept, named <shot>-take-<n>-<model>.<ext>, plus the picked one as <shot>-pick.<ext>
  clay/             every blocking clip, its first frame and its passes from scene_pass, per shot
  sheets/           a copy of every rendered character and mob sheet and each panel
  plates/           the location plates
  references/       every scraped reference with its licence and author in references.md
  audio/            every recorded line and sound, named <line id>-<character>.mp3 and <cue>.mp3
```

**A log entry** (every step, including the free ones) says: the step number and the plan step it belongs to; the time; the arm and tool; the model and AIR id; every input by its full path (my asset files included, exactly as they are under `Runware Test/`); the prompt in full; the cost quoted and the cost Runware charged; every output by path; what I approved or rejected and why; any change you made to the pack and why; any fall-back or failure in plain words; and the screenshot and clip numbers that show it.

**Screenshots (`screens/`), through the browser arm (`browse` with a screenshot, or `check_page`), at least these:**
- the folder listing and each of my print, build and action-map photos as you first open them (one per file, so the making-of can show the mini next to the result)
- `rw_caption`'s description beside each print, build photo and action map
- the scraper's reference grid after step 2
- the storyboard editor after the design draft, after my approval, and after every scene is filmed
- each character sheet page as rendered, and the Titanium studio or Loom view of each panel being drawn
- the Blender stage for each location and each blocked shot (the camera view, and a top view with the action-map arrows beside it)
- each frame as approved, each take as it lands, the chosen take
- the quote dialogue before every paid step and the charge after
- the cut's timeline before the render, the final frame of the 4K master, the usage meter at the end

**Video recordings (`clips/`), at least these:**
- `record_motion` of the Loom while each scene's clips are generating (the spiders, the silk, the arms lighting up), 30 fps, one clip per scene
- `record_motion` of the storyboard editor's board wall as the takes land, one clip per scene
- a `scene_render` turntable of every character mesh and of the worm head (10 s each) and of each location
- the clay blocking clip of every shot (already in `clay/`, listed in the log)
- a 60 s time-lapse of every frame and take in order, built with `cut_edit` at the end, 2 frames a second
- the comparison reel: for every shot, my build photo, the clay clip, the frame and the picked take side by side, built with `cut_edit`

Also keep the live view: a pot, **"Runware dungeon: production log"**, that mirrors `log.md` with the thumbnails inline, updated after each step, and a **shot sheet pot** (one row per shot: status, picked take, cost, screenshot numbers). At the end write the **how-we-made-it pot**: the whole process scene by scene with the pictures from `screens/` (mini, build photo, action map, blocking clip, frame, clip, final), and file the log and the write-up in the wiki with `wiki_add`. Say in the log, honestly, what the model could not hold and what we worked around, and give me the total paid.

## 7. Money and permissions

Runware for every paid step; nothing on fal unless step 8's fall-back applies, and then say so. Quote the whole plan with `board_plan` (budget `best`) and wait for my yes before the first paid call; after that, quote and wait again before any step over $5, before waking the GPU pod, and before the 4K upscale. Tell me the running total after each scene. Keys stay in the vault; never print one.

## 8. Done means

In the Files tab and in `Creative Task Runware/`: the 4K cut and a 1080p copy (`Final Video/`), the picked take of every shot (`Final Shot/`), the how-we-made-it pot, and the `making-of/` folder complete with its log, screenshots, recordings, takes and comparison reel. Seven character sheets and two mob sheets in their folders, three location plates, every clay blocking clip, every take, the storyboard, the log, and the two content drafts. All of it under one storyboard folder so I can open it in the storyboard editor.
