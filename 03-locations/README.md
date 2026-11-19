# 03-locations: the three sets

One folder per scene. Each set was built by hand with clay walls and photographed from the master view and around it; the **action maps** were drawn over those photos (blue arrows are movement and sound, red arrows are attacks, green arrows are a character's reaction or emotion). The agents rebuilt each set as a Blender **stage** (the clay stand-in with one cylinder per character, in the frame written down in `axes.md`), rendered its turntable, and drew two **plates** of each location on Nano Banana Pro from the build photos and the environment lock block.

| folder | scene | stage id | length in the film |
| --- | --- | --- | --- |
| [`scene-1-storeroom/`](scene-1-storeroom/) | Scene 1 | `lo-storeroom` (and `lo-storeroom-open`, the twin without the wall nearest the camera) | 15 s |
| [`scene-2-corridor/`](scene-2-corridor/) | Scene 2 | `lo-corridor` (and `lo-corridor-open`, the twin without the wall nearest the camera) | 15 s |
| [`scene-3-roofless-hall/`](scene-3-roofless-hall/) | Scene 3 | `lo-roofless-hall` (and `lo-roofless-hall-open`, the twin without the wall nearest the camera) | 30 s |

Each location folder:

```
scene-N-name/
  README.md          the place, the build, the status of its plates
  environment.md     the location lock block, layout from the build, materials and light words (from the prompt pack)
  build-photos/      the clay build photographed from the master view and around it
  action-maps/       the build photos with the arrows drawn over them (the shot plan)
  stage/             the Blender stage: window captures, top view against the build photo, master-view render, turntable clip, the generator scripts
  plates/            the two location plates and their layout overlays and prompts
```

`axes.md` in this folder is the frame every position in the film is written in (origin, axes, facing, the proportion rule that maps the clay build to the lock block's metres).

**Where the files are:** what is committed is in this folder; everything else is in the [Drive folder](https://drive.google.com/drive/folders/19oNrUVefdrb2mwJs_GR5v11iavYkja07) under `03-locations/`, which mirrors these folders. Nothing here points at a private machine.
