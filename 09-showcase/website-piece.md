# Is this all on Runware? A 64-second film from seven printed minis and one API

*I built a tabletop dungeon by hand and photographed it with a phone, then agents turned it into a 64-second film with one pinned model per job on the Runware API. This is the chain each shot went through, and what the API taught us on the way.*

*A guest piece by Felipe López Mantilla*

## What was built

I was asked to pick one idea and build it on Runware. Mine was to start from the least digital inputs I could make, and see whether a short film could come out of one API with the characters staying themselves from the first shot to the last.

I made the inputs by hand: seven 3D-printed character minis, two mob prints (the frogs and toads, and the worm), three sets walled with air-dry clay bricks, action maps drawn over the build photos, hand-written shot lists and a phone. Everything after that was made by agents working in Hephaestus, and everything generated came through the Runware API.

The result is "Is this all on Runware?", a 64-second film at 24 fps, counting a 2-second title and 1.5 seconds of black. A party of seven, deep in a dungeon under a fallen castle and low on food, finds that the frogs flooding their storeroom were running from something. The last line is the title. Watch [the film](https://github.com/felipelopezm1/runware-test/releases/download/v1.0/is-this-all-on-runware-crt-4k.mp4) and [the 15-minute making-of](https://drive.google.com/file/d/1kgRFjdAkuBUdGYxVxfez5BUM2wCBTxc7/view); the takes, the continuity rules and the production notes are in [the repo](https://github.com/felipelopezm1/runware-test).

## What the minis are for

The minis are the plan of each shot, never the picture. Their silhouettes, poses, costume pieces and weapon shapes went into character sheets, and their photographs rode as references on every sheet panel. The clay sets became Blender stages, where every shot was blocked with a camera before anything was paid for. The action maps (blue arrows for movement and sound, red for attacks, green for a character's reaction) settled the shots where the shot lists and the maps disagreed.

> The minis are the plan of each shot, never the picture.

Each job had one pinned model, and the Model Router was never used:

| Job | Model on Runware | AIR id |
| --- | --- | --- |
| Sheet panels, location plates, first frames | Nano Banana Pro | `google:4@2` |
| Every clip | Seedance 2.5 | `bytedance:seedance@2.5` |
| Captions | Qwen2.5-VL | `runware:152@2` |
| Meshes for the Blender stages | TRELLIS.2 | `microsoft:trellis-2@4b` |
| 4K fall-back, held and not needed for the clips | Topaz Proteus | `topazlabs:proteus@4` |

I also pinned MiniMax Speech 2.8 and Fish S2.1 Pro for voices, and Mirelo SFX 1.5 and ACE-Step for sound, but no separate recordings were made. The cut uses the takes' own audio, which Seedance 2.5 returns with the clip at no separate price.

## The chain per shot

Sixteen takes were on the storyboard, and each went the same way:

1. **Blocking.** The clay blocking clip from the Blender stage, which is the locked camera and motion guide.
2. **First frame.** Drawn on Nano Banana Pro from the blocking clip's first frame, the face panels, the location plate and the assembled prompt, then locked on approval.
3. **Clip.** Filmed on Seedance 2.5 with the assembled prompt, in one of the two modes described below.
4. **Pick.** The take that goes into the cut, with a comparison strip kept where a shot was filmed again.

Eight shots were filmed again, and two bridges carry the cut between scenes. Shot 1A was dropped in the clean cut, so the finished film holds 15 shots and the 2 bridges.

Continuity sits above everything else. Each character's lock block from the bible is pasted unchanged into every image and video prompt that shows them, a shot's retakes keep the same seed where the schema allows one, and the model under a job never changes.

## What a developer should know before trying this

These cost us time, and all are written up in `08-making-of/notes/runware-facts.md`.

- **A start frame and references cannot go in the same Seedance 2.5 call.** `frameImages` cannot be used with `referenceImages`, `referenceVideos` or `video`, so each shot picks a mode. In frame mode the approved frame is the start frame and no references ride along, so identity rests on the frame and the words. In reference mode the approved frame is the first reference picture, beside the identity strips, the plate and the clay clip as a guide video, with no locked first frame.
- **Reference videos are a real feature.** Seedance 2.5 takes up to ten, 2 to 30 seconds each and 30 seconds in all. A video reference appears to be billed by its own length too; that rests on one charged edit, so test it first.
- **Prompts can be long.** Our 16-take set measured 5,725 to 12,039 characters for clips and 5,203 to 11,640 for frames. Seedance 2.5 allows 50,000 characters and Nano Banana Pro 45,000. Our first tool capped prompts at 3,000.
- **Billing is by token count, so you can quote a call before you send it.** Tokens are width x height x (24 x seconds + 1) / 1024. The listed rate at 1080p is $12.52 per million tokens from words, a frame or pictures, and $7.49 per million tokens with a clip as input. That formula reproduced three 1080p test charges from 11 November to the cent.
- **4K is in Seedance 2.5's schema**, at a listed $0.921 per second.
- **Reference pictures cost nothing extra**, and a rejected request is not billed.

> If your wrapper caps prompts at a few thousand characters, you lose the continuity block that does the work.

## The numbers

- 64 seconds: 63.958 s, 1535 frames at 24 fps
- 16 takes on the storyboard; 15 shots and 2 bridges in the film; retakes on eight shots
- An approved ceiling of $177.91 on Runware: the expected $142.32 plus 25%, split per part
- $31.63 recorded in the committed log over 727 entries, all before the first clip
- One production day, 19 November 2026
- A 4K master on [release v1.0](https://github.com/felipelopezm1/runware-test/releases/tag/v1.0)

## What I would ship

The model is the easy part. What is worth building for product teams is the structure around it: a sheet per character, a stage per location, a blocking pass that fixes the camera before the first paid call, a continuity bible whose lock blocks every prompt carries unchanged, and a prompt check and a price quote before every paid call.

> The model is the easy part. The structure around it is the thing worth building.

That structure kept seven printed minis a cast for a minute of screen time. I would expect it to do the same for a product's characters or a brand's world.

Everything is open in [the repo](https://github.com/felipelopezm1/runware-test). If you try this, read the facts file first.

---

## Suggested images

1. **The cast as printed.** Six phone photos of the party's yellow 3D-printed minis standing together on a grey cutting mat. https://raw.githubusercontent.com/felipelopezm1/runware-test/claude/project-thread-xs5t14/02-cast/all-together/contact-sheet.jpg
2. **One mini from four sides.** Front, right, back and left photos of the Vel print, a caped figure with a rapier on a round base, against a ruled mat. https://raw.githubusercontent.com/felipelopezm1/runware-test/claude/project-thread-xs5t14/02-cast/ch6-vel/prints/contact-sheet.jpg
3. **The same character as a sheet panel.** The face-front panel for Sera'kith Vel: pale green skin, amber eyes and a black fringe, scale armour over a dark red quilted coat, one gloved hand on a swept-hilt rapier. https://raw.githubusercontent.com/felipelopezm1/runware-test/claude/project-thread-xs5t14/02-cast/ch6-vel/sheet/preview-face-front.jpg
4. **An action map.** A build photo of clay-brick walls, yellow printed barrels and crates and a floor of pink frogs, with blue marks drawn over the frogs and green exclamation marks over the party at the far end. https://raw.githubusercontent.com/felipelopezm1/runware-test/claude/project-thread-xs5t14/03-locations/scene-1-storeroom/action-maps/preview-IMG_0343.jpg
5. **Blocking in Blender.** The first frame of shot 2B's blocking clip: an untextured 3D render with a robed figure holding a staff in the foreground and an armed figure standing under a lit arch. https://raw.githubusercontent.com/felipelopezm1/runware-test/claude/project-thread-xs5t14/05-shots/2B/clay/first-frame.png
6. **Shot 2B, two versions.** The comparison strip for shot 2B: a white-bearded priest in a cream cloak raises his hand over a flooded corridor in both frames, with a beam of light crossing the second. https://raw.githubusercontent.com/felipelopezm1/runware-test/claude/project-thread-xs5t14/05-shots/2B/compare/2B.jpg
7. **Shot 1C-2, the room erupts.** Four frames from the comparison strip for the storeroom shot, seen from behind a horned-helmed figure with glowing green hands while frogs sit on the barrels, crates and floor. https://raw.githubusercontent.com/felipelopezm1/runware-test/claude/project-thread-xs5t14/05-shots/1C-2/compare/1C-2-v3.jpg
8. **Mordecai's face-front panel.** A skull with pale blue eyes under a horned iron helm topped by a ring, in dark armour with brass trim over purple velvet. https://raw.githubusercontent.com/felipelopezm1/runware-test/claude/project-thread-xs5t14/02-cast/ch7-mordecai/sheet/preview-face-front.jpg

## Meta description

How seven 3D-printed minis, three clay-walled sets and a phone became a 64-second film on Runware, one pinned model per job, and what the API taught us.

## Could not verify in the repo

The total spend (my brief says about 127 USD; the committed log stops at $31.63 over 727 entries, before the first clip); that every clip was generated at 4K (the five committed takes that were probed are 1920x1080); and which mode each clip call used.
