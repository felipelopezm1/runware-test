# Website piece: a draft for the Runware website

A draft by the agents from the log, 20 November 2026, for Felipe to rewrite by hand. Written for developers and product builders. Nothing here has been published. Every number comes from `08-making-of/` and `04-prompts/`; the prices marked "listed" come from Runware's model pages on 19 November 2026.

---

## Seven minis and a worm: a 60-second film on Seedance 2.5, through one API

*A guest piece by Felipe López Mantilla*

I was asked to pick one idea, build it on Runware and show how developers and product builders would notice it. The idea: take the least digital inputs I could make, seven air-dry clay miniatures, three cardboard sets and a phone, and see whether a whole short film could come out of one API with the characters staying themselves from the first shot to the last. The last line of the film is the question in its title, "Is this all on Runware?", and the answer is yes.

The film is 64 seconds, sixteen shots, a party of seven deep in a dungeon under a fallen castle, low on food, who find that the frogs flooding their storeroom were running from something. The film, the 15-minute making-of, every prompt, every take and the full log are public at github.com/felipelopezm1/runware-test.

### What the minis are for

The minis are the plan of each shot, never the picture. Their silhouettes, poses, costume pieces and weapon shapes went into character sheets. Their photographs rode as references on every panel. The clay sets became Blender stages where every shot was blocked with a camera before anything was paid for. "Action maps" drawn over the build photos (blue arrows for movement, red for attacks, green for a character's reaction) settled the shots where the hand-written shot lists and the maps disagreed.

Everything after that is generated, and everything generated came through Runware with one pinned model per job:

| job | model on Runware |
| --- | --- |
| reading the folder: every print, build photo and action map captioned | Qwen2.5-VL |
| character sheet panels, location plates, the first frame of every shot | Nano Banana Pro |
| every clip | Seedance 2.5 at 4K |
| the voices | MiniMax Speech 2.8, Fish S2.1 Pro |
| foley and the music bed | Mirelo SFX 1.5, ACE-Step |
| 4K fall-back, held and not needed | Topaz Proteus |

### The chain per shot

Each of the sixteen shots went the same way, and the repository holds one thing per link of the chain:

1. the clay blocking clip from the Blender stage, which is the locked camera and motion guide;
2. the first frame, drawn on Nano Banana Pro from the clay first frame, the face panels, the location plate and the assembled prompt, locked on approval;
3. the clip on Seedance 2.5, filmed from the approved frame with the face panels as references and the prompt sent verbatim; retakes (v2, v3) on eight shots, two bridges filmed to carry the cut between scenes;
4. the pick, and a comparison strip of clay beside take beside finish.

The continuity rules sit above everything else: a bible the prompts obey, the same seed on a shot's retakes where the schema allows one, and the Model Router never used, because a pinned model is the only way to make take three look like take one.

### What a developer should know before trying this

These are the things that cost us time, all recorded in the log:

- **A start frame and reference images cannot go in the same Seedance 2.5 call.** The plan wanted the approved frame as first frame, the face panels as references and the clay clip as a video reference together. The API refuses the combination, so each shot picks a mode. We filmed from the frame with references and kept the clay clip as the camera guide upstream.
- **Reference videos are a real feature.** Seedance 2.5 takes up to ten, 2 to 30 seconds each, and a clay blocking clip rides as one in reference mode. A video reference is billed by its own length too, so a long guide clip on a short shot costs more than the shot.
- **Prompts are long and the model allows it.** The assembled prompts ran from 6,900 to 12,800 characters; Seedance 2.5 takes up to 50,000 and Nano Banana Pro 45,000. If your own wrapper caps prompts at a few thousand characters, as our first tool did, you lose the continuity block that does the work.
- **Billing is by token count, and you can predict it.** At 1080p the listed rate is 12.52 USD a million tokens from words, a frame or pictures, and 7.49 USD a million with a clip as input, where tokens are width x height x (24 x seconds + 1) / 1024 over every frame in and out. That formula reproduced our real charges to the cent, which is what let the agents quote every call before sending it.
- **4K is listed on Seedance 2.5 at 0.921 USD a second** and it worked; the first paid 4K take was the proof the plan waited for. A request the API rejects is not billed.
- **Reference pictures cost nothing extra**, so there is no reason to send a shot without its face panels.

### The numbers

- 16 shots, 2 bridges, retakes on 8 shots; 62 seconds on screen
- 7 characters, 2 mobs, 3 sets
- an approved ceiling of 177.91 USD on Runware, split per scene; about 127 USD spent
- one day of production, 19 November 2026, after four days of hand-made inputs

### What I would ship

The model is the easy part. The thing worth building for product teams is the structure around it: a sheet per character, a stage per location, a blocking pass that fixes the camera before the first paid call, a continuity bible that every prompt carries verbatim, and a quartermaster that quotes each call and refuses the ones that break a rule. That is what turned seven lumps of clay into a cast that holds together for a minute of screen time, and it would do the same for a product's characters, a brand's world or an explainer series.

Everything is open: github.com/felipelopezm1/runware-test.
