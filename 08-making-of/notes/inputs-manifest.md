# Intake manifest

Working copies of `/home/felipe-lopez/Desktop/Runware Test/Creative Task Runware` (248 files). The originals are untouched; `manifest.json` beside this file has the same rows with the full paths, sha1 and notes. Made by `making-of/tools/intake/convert.py`.

- Photos (HEIC, JPG, PNG) are upright sRGB JPEGs, quality 88, long side 2048 (B-roll stills 640).
- Videos are not copied: each has a poster (middle frame, long side 1280, B-roll 640); six have a strip of 8 evenly spaced frames, first to last, 4 by 2.
- Working copies below are relative to `making-of/inputs/`.
- The owner's rule for the prints: they are the plan of each shot (silhouette, pose, costume pieces, weapon shape, blocking); their colour and layer lines are never carried into a prompt.
- Everything under B Roll has `model_input: false`: the owner forbids B-roll as a model input. Documents and stubs are false too (nothing to hand over); the markup animations, the Scene 3 clip and the frog clip are true, as pre-production the list names and not B-roll.
- `note` is the owner's words from `02-ASSET-PATHS.md`; anything after `[intake:` is what this intake measured or saw, not the owner's words.
- Fields beyond the asked ones: `over_doc` (the build photo the list names), `over_title` (the photo name kept inside the PNG), `over_pixels` (the build photo the pixels match), `duplicate_of`, `faces` (which way the figure faces in a turnaround photo, read by eye), `codec`, `rotation`.

## Counts by kind

| kind | files | with a working copy | with a poster | with a strip |
| --- | ---: | ---: | ---: | ---: |
| print | 29 | 29 | 0 | 0 |
| group | 6 | 6 | 0 | 0 |
| scale | 4 | 4 | 0 | 0 |
| mob-print | 17 | 17 | 0 | 0 |
| mob-video | 1 | 0 | 1 | 1 |
| build | 79 | 79 | 0 | 0 |
| build-video | 1 | 0 | 1 | 1 |
| action-map | 31 | 31 | 0 | 0 |
| action-animation | 4 | 0 | 4 | 4 |
| broll-still | 4 | 4 | 0 | 0 |
| broll-video | 23 | 0 | 23 | 0 |
| stub | 30 | 0 | 0 | 0 |
| doc | 19 | 0 | 0 | 0 |
| **all** | **248** | **170** | **29** | **6** |

## Action maps whose listed build photo is not the one under the drawing

`02-ASSET-PATHS.md` names a build photo for each action map. Each map was compared with every build photo (96 by 72 grey copies, mean absolute difference of 255): the right photo scores about 1, any other about 30 to 45. The photo's name kept inside each PNG (XMP `tiff:DocumentName`) agrees with the pixels in all cases. `over` holds the measured photo, `over_doc` the listed one.

| action map | listed over | really over | pixel difference (best, next) | title inside the PNG |
| --- | --- | --- | --- | --- |
| `Scene 1 Actions/IMG_0344.PNG` | IMG_8112 | **IMG_8113** | 0.2, 40.4 | IMG_8113 |
| `Scene 1 Actions/IMG_0345.PNG` | IMG_8111 | **IMG_8112** | 1.4, 41.2 | IMG_8112 |
| `Scene 1 Actions/IMG_0346.PNG` | IMG_8110 | **IMG_8109** | 1.0, 30.7 | IMG_8109 |
| `Scene 1 Actions/IMG_0347.PNG` | IMG_8109 | **IMG_8108** | 0.7, 32.8 | IMG_8108 |
| `Scene 1 Actions/IMG_0350.PNG` | IMG_8101 | **IMG_8098** | 0.9, 28.5 | IMG_8098 |
| `Scene 1 Actions/IMG_0351.PNG` | IMG_8099 | **IMG_8097** | 0.8, 32.4 | IMG_8097 |
| `Scene 2 Actions/IMG_0340.PNG` | IMG_8123 | **IMG_8124** | 0.9, 38.6 | IMG_8124 |
| `Scene 2 Actions/IMG_0341.PNG` | IMG_8124 | **IMG_8123** | 1.0, 38.8 | IMG_8123 |

## Turnaround labels against what the photos show

Read by eye off the working copies. Every character was turned the same way: in the second photo the figure faces image-left (the camera sees the figure's own left side), in the fourth it faces image-right (its own right side). `02-ASSET-PATHS.md` calls the second photo `right` and the fourth `left` for six characters, and the other way round for Character 3 (Dax). `view` keeps the list's word; `faces` says what the photo shows. Whoever hands these to a tool that wants left and right views should go by `faces`.

| photo | character | listed view | figure faces | the camera sees |
| --- | --- | --- | --- | --- |
| `IMG_8216.HEIC` | ch-vessa | front | camera | front |
| `IMG_8217.HEIC` | ch-vessa | right | image-left | its own left side |
| `IMG_8218.HEIC` | ch-vessa | back | away | back |
| `IMG_8219.HEIC` | ch-vessa | left | image-right | its own right side |
| `IMG_8220.HEIC` | ch-borrin | front | camera | front |
| `IMG_8221.HEIC` | ch-borrin | right | image-left | its own left side |
| `IMG_8222.HEIC` | ch-borrin | back | away | back |
| `IMG_8223.HEIC` | ch-borrin | left | image-right | its own right side |
| `IMG_8224.HEIC` | ch-dax | front | camera | front |
| `IMG_8225.HEIC` | ch-dax | left | image-left | its own left side |
| `IMG_8226.HEIC` | ch-dax | back | away | back |
| `IMG_8227.HEIC` | ch-dax | right | image-right | its own right side |
| `IMG_8228.HEIC` | ch-sylwen | front | camera | front |
| `IMG_8229.HEIC` | ch-sylwen | right | image-left | its own left side |
| `IMG_8230.HEIC` | ch-sylwen | back | away | back |
| `IMG_8231.HEIC` | ch-sylwen | left | image-right | its own right side |
| `IMG_8232.HEIC` | ch-sylwen | left | image-right | its own right side |
| `IMG_8233.HEIC` | ch-oswin | front | camera | front |
| `IMG_8234.HEIC` | ch-oswin | right | image-left | its own left side |
| `IMG_8235.HEIC` | ch-oswin | back | away | back |
| `IMG_8236.HEIC` | ch-oswin | left-three-quarter | image-right-three-quarter | its front and its own right side |
| `IMG_8237.HEIC` | ch-vel | front | camera | front |
| `IMG_8238.HEIC` | ch-vel | right | image-left | its own left side |
| `IMG_8239.HEIC` | ch-vel | back | away | back |
| `IMG_8240.HEIC` | ch-vel | left | image-right | its own right side |
| `IMG_8241.HEIC` | ch-mordecai | front | camera | front |
| `IMG_8242.HEIC` | ch-mordecai | right | image-left | its own left side |
| `IMG_8243.HEIC` | ch-mordecai | back | away | back |
| `IMG_8244.HEIC` | ch-mordecai | left | image-right | its own right side |

Hands, seen in the front photos: Borrin's axe is in his own left hand and his own right hand is on the hip (the list says left hand on the hip); Oswin's staff is in his own left hand and his own right hand is raised (the list says staff in the right hand, left hand raised). For Vessa (sword in her right hand, shield on her left arm) and Vel (sword in her right hand) the list matches the figure's own sides.

## Duplicates (same sha1)

- `Creative Task Runware/Pre Production Assets/B Roll/Scene 3 B Roll/IMG_8138.MOV` is byte for byte `Creative Task Runware/Pre Production Assets/Scenes/Scene 3/IMG_8138.MOV` (sha1 `8330698e2ca25f38b6c27a204db35317f571b56a`).
- `Creative Task Runware/Pre Production Assets/Scenes/Scene 1/Scene 1 Actions/IMG_0343.PNG` is byte for byte `Creative Task Runware/Pre Production Assets/Scenes/Scene 2/Scene 2 Actions/IMG_0343.PNG` (sha1 `f04d8caf1ee533c63ea4e2e07a61e3957c6b3966`).
- `Creative Task Runware/Pre Production Assets/Scenes/Scene 2/Scene 2 Actions/IMG_0332.PNG` is byte for byte `Creative Task Runware/Pre Production Assets/Scenes/Scene 3/Scene 3 Actions/IMG_0332.PNG` (sha1 `b9d537a8220cf28b2df78c24807c30438ee8e6c7`).

## Files by folder

### Pre Production Assets/B Roll (31)

Felipe's own footage of the build, to be listed in the log and cut into the making-of, never used as a model input. The thirty QuickTime movie files are 135-byte stubs.

| file | kind | subject | view or over | size | working copy |
| --- | --- | --- | --- | --- | --- |
| `QuickTime movie-4850-8024-91-15.mov` | stub |  |  | 135 B |  |
| `QuickTime movie-4850-8024-91-16.mov` | stub |  |  | 135 B |  |
| `QuickTime movie-4850-8024-91-17.mov` | stub |  |  | 135 B |  |
| `QuickTime movie-4850-8024-91-18.mov` | stub |  |  | 135 B |  |
| `QuickTime movie-4850-8024-91-19.mov` | stub |  |  | 135 B |  |
| `QuickTime movie-4850-8024-91-20.mov` | stub |  |  | 135 B |  |
| `QuickTime movie-4850-8024-91-21.mov` | stub |  |  | 135 B |  |
| `QuickTime movie-4850-8024-91-22.mov` | stub |  |  | 135 B |  |
| `QuickTime movie-4850-8024-91-23.mov` | stub |  |  | 135 B |  |
| `QuickTime movie-4850-8024-91-24.mov` | stub |  |  | 135 B |  |
| `QuickTime movie-4850-8024-91-25.mov` | stub |  |  | 135 B |  |
| `QuickTime movie-4850-8024-91-26.mov` | stub |  |  | 135 B |  |
| `QuickTime movie-4850-8024-91-27.mov` | stub |  |  | 135 B |  |
| `QuickTime movie-4850-8024-91-28.mov` | stub |  |  | 135 B |  |
| `QuickTime movie-4850-8024-91-29.mov` | stub |  |  | 135 B |  |
| `QuickTime movie-4850-8024-91-30.mov` | stub |  |  | 135 B |  |
| `QuickTime movie-4850-8024-91-31.mov` | stub |  |  | 135 B |  |
| `QuickTime movie-4850-8024-91-32.mov` | stub |  |  | 135 B |  |
| `QuickTime movie-4850-8024-91-33.mov` | stub |  |  | 135 B |  |
| `QuickTime movie-4850-8024-91-34.mov` | stub |  |  | 135 B |  |
| `QuickTime movie-4850-8024-91-35.mov` | stub |  |  | 135 B |  |
| `QuickTime movie-4850-8024-91-36.mov` | stub |  |  | 135 B |  |
| `QuickTime movie-4850-8024-91-37.mov` | stub |  |  | 135 B |  |
| `QuickTime movie-4850-8024-91-38.mov` | stub |  |  | 135 B |  |
| `QuickTime movie-4850-8024-91-39.mov` | stub |  |  | 135 B |  |
| `QuickTime movie-4850-8024-91-40.mov` | stub |  |  | 135 B |  |
| `QuickTime movie-4850-8024-91-41.mov` | stub |  |  | 135 B |  |
| `QuickTime movie-4850-8024-91-42.mov` | stub |  |  | 135 B |  |
| `QuickTime movie-4850-8024-91-43.mov` | stub |  |  | 135 B |  |
| `QuickTime movie-4850-8024-91-44.mov` | stub |  |  | 135 B |  |
| `Screen Recording 2026-11-19 at 07.45.22.mov` | broll-video |  |  | 2286x1370 · 63.47 s · 24.627 fps · h264 · 8.06 MB | `broll/Screen-Recording-2026-11-19-at-07.45.22.poster.jpg` |

### Pre Production Assets/B Roll/Scene 2 B Roll (4)

| file | kind | subject | view or over | size | working copy |
| --- | --- | --- | --- | --- | --- |
| `IMG_0108.MOV` | broll-video |  |  | 3840x2160 · 32.44 s · 29.965 fps · hevc · 92.89 MB | `broll/scene-2-b-roll/IMG_0108.poster.jpg` |
| `IMG_8115.MOV` | broll-video |  |  | 1080x1920 · 63.77 s · 29.997 fps · hevc · 70.16 MB | `broll/scene-2-b-roll/IMG_8115.poster.jpg` |
| `IMG_8116.MOV` | broll-video |  |  | 1920x1080 · 7.20 s · 30 fps · hevc · 7.97 MB | `broll/scene-2-b-roll/IMG_8116.poster.jpg` |
| `IMG_8118.MOV` | broll-video |  |  | 1920x1080 · 8.93 s · 29.994 fps · hevc · 9.65 MB | `broll/scene-2-b-roll/IMG_8118.poster.jpg` |

### Pre Production Assets/B Roll/Scene 3 B Roll (7)

| file | kind | subject | view or over | size | working copy |
| --- | --- | --- | --- | --- | --- |
| `IMG_0109.HEIC` | broll-still |  |  | 4032x3024 · 3.02 MB | `broll/scene-3-b-roll/IMG_0109.jpg` |
| `IMG_0110.MOV` | broll-video |  |  | 1920x1080 · 264.57 s · 29.965 fps · hevc · 260.30 MB | `broll/scene-3-b-roll/IMG_0110.poster.jpg` |
| `IMG_8134.HEIC` | broll-still |  |  | 4032x3024 · 1.14 MB | `broll/scene-3-b-roll/IMG_8134.jpg` |
| `IMG_8135.HEIC` | broll-still |  |  | 4032x3024 · 1.21 MB | `broll/scene-3-b-roll/IMG_8135.jpg` |
| `IMG_8136.MOV` | broll-video |  |  | 1920x1080 · 15.60 s · 29.997 fps · hevc · 16.99 MB | `broll/scene-3-b-roll/IMG_8136.poster.jpg` |
| `IMG_8137.MOV` | broll-video |  |  | 1920x1080 · 104.18 s · 29.997 fps · hevc · 112.17 MB | `broll/scene-3-b-roll/IMG_8137.poster.jpg` |
| `IMG_8138.MOV` | broll-video |  | duplicate of `sc3-8138-mov` | 1920x1080 · 20.80 s · 29.998 fps · hevc · 19.99 MB | `broll/scene-3-b-roll/IMG_8138.poster.jpg` |

### Pre Production Assets/B Roll/Starting (15)

| file | kind | subject | view or over | size | working copy |
| --- | --- | --- | --- | --- | --- |
| `IMG_0093.JPG` | broll-still |  |  | 4032x3024 · 2.31 MB | `broll/starting/IMG_0093.jpg` |
| `IMG_8052.MOV` | broll-video |  |  | 1920x1080 · 13.10 s · 29.996 fps · hevc · 9.61 MB | `broll/starting/IMG_8052.poster.jpg` |
| `IMG_8053.MOV` | broll-video |  |  | 1920x1080 · 20.68 s · 29.792 fps · hevc · 42.52 MB | `broll/starting/IMG_8053.poster.jpg` |
| `IMG_8054.MOV` | broll-video |  |  | 1920x1080 · 16.70 s · 29.997 fps · hevc · 29.61 MB | `broll/starting/IMG_8054.poster.jpg` |
| `IMG_8055.MOV` | broll-video |  |  | 1920x1080 · 16.34 s · 28.636 fps · hevc · 13.95 MB | `broll/starting/IMG_8055.poster.jpg` |
| `IMG_8056.MOV` | broll-video |  |  | 1920x1080 · 1.73 s · 30 fps · hevc · 1.50 MB | `broll/starting/IMG_8056.poster.jpg` |
| `IMG_8057.MOV` | broll-video |  |  | 1920x1080 · 5.77 s · 30 fps · hevc · 6.78 MB | `broll/starting/IMG_8057.poster.jpg` |
| `IMG_8058.MOV` | broll-video |  |  | 1920x1080 · 6.97 s · 28.852 fps · hevc · 8.17 MB | `broll/starting/IMG_8058.poster.jpg` |
| `IMG_8059.MOV` | broll-video |  |  | 1080x1920 · 1.20 s · 11.858 fps · hevc · 1.66 MB | `broll/starting/IMG_8059.poster.jpg` |
| `IMG_8060.MOV` | broll-video |  |  | 1080x1920 · 12.44 s · 29.996 fps · hevc · 13.57 MB | `broll/starting/IMG_8060.poster.jpg` |
| `IMG_8061.MOV` | broll-video |  |  | 1920x1080 · 1.04 s · 29.76 fps · hevc · 0.97 MB | `broll/starting/IMG_8061.poster.jpg` |
| `IMG_8062.MOV` | broll-video |  |  | 1920x1080 · 8.43 s · 29.08 fps · hevc · 13.61 MB | `broll/starting/IMG_8062.poster.jpg` |
| `IMG_8063.MOV` | broll-video |  |  | 1920x1080 · 84.72 s · 29.991 fps · hevc · 92.35 MB | `broll/starting/IMG_8063.poster.jpg` |
| `IMG_8064.MOV` | broll-video |  |  | 1920x1080 · 1.43 s · 30 fps · hevc · 1.60 MB | `broll/starting/IMG_8064.poster.jpg` |
| `IMG_8065.MOV` | broll-video |  |  | 1920x1080 · 62.74 s · 29.997 fps · hevc · 69.38 MB | `broll/starting/IMG_8065.poster.jpg` |

### Pre Production Assets/Scenes/Scene 1 (30)

Scene 1, the storeroom. Crates and a sack back left, barrels and a sack front left, a straight staircase from the floor at the front up to the back-right corner with crates at its top; the party in a loose circle.

| file | kind | subject | view or over | size | working copy |
| --- | --- | --- | --- | --- | --- |
| `IMG_8085.HEIC` | build | sc-1 | low-front | 4032x3024 · 1.33 MB | `scenes/scene-1/IMG_8085.jpg` |
| `IMG_8086.HEIC` | build | sc-1 | low-front | 4032x3024 · 1.49 MB | `scenes/scene-1/IMG_8086.jpg` |
| `IMG_8087.HEIC` | build | sc-1 | low-front | 4032x3024 · 1.52 MB | `scenes/scene-1/IMG_8087.jpg` |
| `IMG_8088.HEIC` | build | sc-1 | low-front | 4032x3024 · 1.28 MB | `scenes/scene-1/IMG_8088.jpg` |
| `IMG_8089.HEIC` | build | sc-1 | behind-party | 4032x3024 · 1.46 MB | `scenes/scene-1/IMG_8089.jpg` |
| `IMG_8090.HEIC` | build | sc-1 | behind-party | 4032x3024 · 1.46 MB | `scenes/scene-1/IMG_8090.jpg` |
| `IMG_8091.HEIC` | build | sc-1 | behind-party | 4032x3024 · 1.52 MB | `scenes/scene-1/IMG_8091.jpg` |
| `IMG_8092.HEIC` | build | sc-1 | behind-party | 4032x3024 · 1.45 MB | `scenes/scene-1/IMG_8092.jpg` |
| `IMG_8093.HEIC` | build | sc-1 | stairs-alone | 4032x3024 · 1.44 MB | `scenes/scene-1/IMG_8093.jpg` |
| `IMG_8094.HEIC` | build | sc-1 | over-barrels | 4032x3024 · 1.44 MB | `scenes/scene-1/IMG_8094.jpg` |
| `IMG_8095.HEIC` | build | sc-1 | over-barrels | 4032x3024 · 1.44 MB | `scenes/scene-1/IMG_8095.jpg` |
| `IMG_8096.HEIC` | build | sc-1 | stairs-alone | 4032x3024 · 1.40 MB | `scenes/scene-1/IMG_8096.jpg` |
| `IMG_8097.HEIC` | build | sc-1 | high-three-quarter | 4032x3024 · 1.57 MB | `scenes/scene-1/IMG_8097.jpg` |
| `IMG_8098.HEIC` | build | sc-1 | high-three-quarter | 4032x3024 · 1.65 MB | `scenes/scene-1/IMG_8098.jpg` |
| `IMG_8099.HEIC` | build | sc-1 | high-three-quarter | 4032x3024 · 1.65 MB | `scenes/scene-1/IMG_8099.jpg` |
| `IMG_8100.HEIC` | build | sc-1 | high-three-quarter | 4032x3024 · 1.68 MB | `scenes/scene-1/IMG_8100.jpg` |
| `IMG_8101.HEIC` | build | sc-1 | high-three-quarter | 4032x3024 · 1.60 MB | `scenes/scene-1/IMG_8101.jpg` |
| `IMG_8102.HEIC` | build | sc-1 | over-barrels | 4032x3024 · 1.08 MB | `scenes/scene-1/IMG_8102.jpg` |
| `IMG_8103.HEIC` | build | sc-1 | high-three-quarter | 4032x3024 · 1.11 MB | `scenes/scene-1/IMG_8103.jpg` |
| `IMG_8104.HEIC` | build | sc-1 | high-three-quarter | 4032x3024 · 1.11 MB | `scenes/scene-1/IMG_8104.jpg` |
| `IMG_8105.HEIC` | build | sc-1 | high-three-quarter | 4032x3024 · 1.10 MB | `scenes/scene-1/IMG_8105.jpg` |
| `IMG_8106.HEIC` | build | sc-1 | high-three-quarter | 4032x3024 · 1.12 MB | `scenes/scene-1/IMG_8106.jpg` |
| `IMG_8107.HEIC` | build | sc-1 | high-three-quarter | 4032x3024 · 1.09 MB | `scenes/scene-1/IMG_8107.jpg` |
| `IMG_8108.HEIC` | build | sc-1 | stairs-alone | 4032x3024 · 1.15 MB | `scenes/scene-1/IMG_8108.jpg` |
| `IMG_8109.HEIC` | build | sc-1 | high-three-quarter | 4032x3024 · 1.10 MB | `scenes/scene-1/IMG_8109.jpg` |
| `IMG_8110.HEIC` | build | sc-1 | high-three-quarter | 4032x3024 · 1.08 MB | `scenes/scene-1/IMG_8110.jpg` |
| `IMG_8111.HEIC` | build | sc-1 | behind-party | 4032x3024 · 1.09 MB | `scenes/scene-1/IMG_8111.jpg` |
| `IMG_8112.HEIC` | build | sc-1 | behind-party | 4032x3024 · 1.13 MB | `scenes/scene-1/IMG_8112.jpg` |
| `IMG_8113.HEIC` | build | sc-1 | behind-party | 4032x3024 · 1.28 MB | `scenes/scene-1/IMG_8113.jpg` |
| `IMG_8114.HEIC` | build | sc-1 | behind-party | 4032x3024 · 1.13 MB | `scenes/scene-1/IMG_8114.jpg` |

### Pre Production Assets/Scenes/Scene 1/Scene 1 Actions (18)

| file | kind | subject | view or over | size | working copy |
| --- | --- | --- | --- | --- | --- |
| `IMG_0343.PNG` | action-map | sc-2 | over IMG_8119 · duplicate of `sc2-act-0343` | 4032x3024 · 12.09 MB | `scenes/scene-1/actions/IMG_0343.jpg` |
| `IMG_0344.PNG` | action-map | sc-1 | over IMG_8113 (listed: IMG_8112) | 4032x3024 · 15.16 MB | `scenes/scene-1/actions/IMG_0344.jpg` |
| `IMG_0345.PNG` | action-map | sc-1 | over IMG_8112 (listed: IMG_8111) | 4032x3024 · 14.58 MB | `scenes/scene-1/actions/IMG_0345.jpg` |
| `IMG_0346.PNG` | action-map | sc-1 | over IMG_8109 (listed: IMG_8110) | 4032x3024 · 14.70 MB | `scenes/scene-1/actions/IMG_0346.jpg` |
| `IMG_0347.PNG` | action-map | sc-1 | over IMG_8108 (listed: IMG_8109) | 4032x3024 · 14.51 MB | `scenes/scene-1/actions/IMG_0347.jpg` |
| `IMG_0348.PNG` | action-map | sc-1 | over IMG_8103 | 4032x3024 · 14.79 MB | `scenes/scene-1/actions/IMG_0348.jpg` |
| `IMG_0349.PNG` | action-map | sc-1 | over IMG_8102 | 4032x3024 · 14.82 MB | `scenes/scene-1/actions/IMG_0349.jpg` |
| `IMG_0350.PNG` | action-map | sc-1 | over IMG_8098 (listed: IMG_8101) | 4032x3024 · 14.77 MB | `scenes/scene-1/actions/IMG_0350.jpg` |
| `IMG_0351.PNG` | action-map | sc-1 | over IMG_8097 (listed: IMG_8099) | 4032x3024 · 14.34 MB | `scenes/scene-1/actions/IMG_0351.jpg` |
| `IMG_0352.PNG` | action-map | sc-1 | over IMG_8096 | 4032x3024 · 14.41 MB | `scenes/scene-1/actions/IMG_0352.jpg` |
| `IMG_0357.PNG` | action-map | sc-1 | over IMG_8094 | 4032x3024 · 15.00 MB | `scenes/scene-1/actions/IMG_0357.jpg` |
| `IMG_0358.PNG` | action-map | sc-1 | over IMG_8093 | 4032x3024 · 14.24 MB | `scenes/scene-1/actions/IMG_0358.jpg` |
| `IMG_0359.PNG` | action-map | sc-1 | over IMG_8092 | 4032x3024 · 14.93 MB | `scenes/scene-1/actions/IMG_0359.jpg` |
| `IMG_0360.PNG` | action-map | sc-1 | over IMG_8087 | 4032x3024 · 15.09 MB | `scenes/scene-1/actions/IMG_0360.jpg` |
| `IMG_0361.PNG` | action-map | sc-1 | over IMG_8085 | 4032x3024 · 13.49 MB | `scenes/scene-1/actions/IMG_0361.jpg` |
| `IMG_8085.MP4` | action-animation | sc-1 | over IMG_8085 | 1440x1080 · 4.13 s · 27.692 fps · h264 · 2.15 MB | `scenes/scene-1/actions/IMG_8085.poster.jpg`<br>`scenes/scene-1/actions/IMG_8085.strip.jpg` |
| `IMG_8094.MP4` | action-animation | sc-1 | over IMG_8094 | 1440x1080 · 2.60 s · 27.439 fps · h264 · 1.10 MB | `scenes/scene-1/actions/IMG_8094.poster.jpg`<br>`scenes/scene-1/actions/IMG_8094.strip.jpg` |
| `IMG_8103.MP4` | action-animation | sc-1 | over IMG_8103 | 1440x1080 · 2.53 s · 27.75 fps · h264 · 0.91 MB | `scenes/scene-1/actions/IMG_8103.poster.jpg`<br>`scenes/scene-1/actions/IMG_8103.strip.jpg` |

### Pre Production Assets/Scenes/Scene 2 (15)

Scene 2, the corridor. A long corridor whose far end is the top of Scene 1's staircase; a long bench against the left wall, a barred window niche on the right wall, a fallen slab near the far wall, a crate and barrel at an opening near the far end; about twenty frogs on the floor, two on the bench.

| file | kind | subject | view or over | size | working copy |
| --- | --- | --- | --- | --- | --- |
| `IMG_8119.HEIC` | build | sc-2 |  | 4032x3024 · 1.16 MB | `scenes/scene-2/IMG_8119.jpg` |
| `IMG_8120.HEIC` | build | sc-2 |  | 4032x3024 · 1.21 MB | `scenes/scene-2/IMG_8120.jpg` |
| `IMG_8121.HEIC` | build | sc-2 |  | 4032x3024 · 1.19 MB | `scenes/scene-2/IMG_8121.jpg` |
| `IMG_8122.HEIC` | build | sc-2 |  | 4032x3024 · 1.12 MB | `scenes/scene-2/IMG_8122.jpg` |
| `IMG_8123.HEIC` | build | sc-2 |  | 4032x3024 · 1.08 MB | `scenes/scene-2/IMG_8123.jpg` |
| `IMG_8124.HEIC` | build | sc-2 |  | 4032x3024 · 1.02 MB | `scenes/scene-2/IMG_8124.jpg` |
| `IMG_8125.HEIC` | build | sc-2 |  | 4032x3024 · 1.03 MB | `scenes/scene-2/IMG_8125.jpg` |
| `IMG_8126.HEIC` | build | sc-2 |  | 4032x3024 · 1.03 MB | `scenes/scene-2/IMG_8126.jpg` |
| `IMG_8127.HEIC` | build | sc-2 |  | 4032x3024 · 1.07 MB | `scenes/scene-2/IMG_8127.jpg` |
| `IMG_8128.HEIC` | build | sc-2 |  | 4032x3024 · 1.18 MB | `scenes/scene-2/IMG_8128.jpg` |
| `IMG_8129.HEIC` | build | sc-2 |  | 4032x3024 · 1.14 MB | `scenes/scene-2/IMG_8129.jpg` |
| `IMG_8130.HEIC` | build | sc-2 |  | 4032x3024 · 1.06 MB | `scenes/scene-2/IMG_8130.jpg` |
| `IMG_8131.HEIC` | build | sc-2 |  | 4032x3024 · 1.02 MB | `scenes/scene-2/IMG_8131.jpg` |
| `IMG_8132.HEIC` | build | sc-2 |  | 4032x3024 · 1.09 MB | `scenes/scene-2/IMG_8132.jpg` |
| `IMG_8133.HEIC` | build | sc-2 |  | 4032x3024 · 1.11 MB | `scenes/scene-2/IMG_8133.jpg` |

### Pre Production Assets/Scenes/Scene 2/Scene 2 Actions (13)

| file | kind | subject | view or over | size | working copy |
| --- | --- | --- | --- | --- | --- |
| `IMG_0332.PNG` | action-map | sc-3 | over IMG_8139 · duplicate of `sc3-act-0332` | 4032x3024 · 14.87 MB | `scenes/scene-2/actions/IMG_0332.jpg` |
| `IMG_0333.PNG` | action-map | sc-2 | over IMG_8133 | 4032x3024 · 13.29 MB | `scenes/scene-2/actions/IMG_0333.jpg` |
| `IMG_0334.PNG` | action-map | sc-2 | over IMG_8132 | 4032x3024 · 13.50 MB | `scenes/scene-2/actions/IMG_0334.jpg` |
| `IMG_0335.PNG` | action-map | sc-2 | over IMG_8131 | 4032x3024 · 13.30 MB | `scenes/scene-2/actions/IMG_0335.jpg` |
| `IMG_0336.PNG` | action-map | sc-2 | over IMG_8130 | 4032x3024 · 13.66 MB | `scenes/scene-2/actions/IMG_0336.jpg` |
| `IMG_0337.PNG` | action-map | sc-2 | over IMG_8129 | 4032x3024 · 14.74 MB | `scenes/scene-2/actions/IMG_0337.jpg` |
| `IMG_0338.PNG` | action-map | sc-2 | over IMG_8128 | 4032x3024 · 14.72 MB | `scenes/scene-2/actions/IMG_0338.jpg` |
| `IMG_0339.PNG` | action-map | sc-2 | over IMG_8126 | 4032x3024 · 13.67 MB | `scenes/scene-2/actions/IMG_0339.jpg` |
| `IMG_0340.PNG` | action-map | sc-2 | over IMG_8124 (listed: IMG_8123) | 4032x3024 · 13.89 MB | `scenes/scene-2/actions/IMG_0340.jpg` |
| `IMG_0341.PNG` | action-map | sc-2 | over IMG_8123 (listed: IMG_8124) | 4032x3024 · 14.28 MB | `scenes/scene-2/actions/IMG_0341.jpg` |
| `IMG_0342.PNG` | action-map | sc-2 | over IMG_8122 | 4032x3024 · 12.16 MB | `scenes/scene-2/actions/IMG_0342.jpg` |
| `IMG_0343.PNG` | action-map | sc-2 | over IMG_8119 | 4032x3024 · 12.09 MB | `scenes/scene-2/actions/IMG_0343.jpg` |
| `IMG_8123.MP4` | action-animation | sc-2 | over IMG_8123 | 1440x1080 · 2.73 s · 28.256 fps · h264 · 1.13 MB | `scenes/scene-2/actions/IMG_8123.poster.jpg`<br>`scenes/scene-2/actions/IMG_8123.strip.jpg` |

### Pre Production Assets/Scenes/Scene 3 (35)

Scene 3, the roofless hall. Taller walls on three sides, a central mound of rubble with the worm coiled twice around it, its head raised; a figure lying inside the coil; barrels inside the coil and at the corners; a bench with frogs; the niche and slab pushed aside; shed crescent plates everywhere.

| file | kind | subject | view or over | size | working copy |
| --- | --- | --- | --- | --- | --- |
| `IMG_0111.HEIC` | build | sc-3 |  | 4032x3024 · 3.83 MB | `scenes/scene-3/IMG_0111.jpg` |
| `IMG_0112.HEIC` | build | sc-3 | master | 4032x3024 · 3.90 MB | `scenes/scene-3/IMG_0112.jpg` |
| `IMG_8138.MOV` | build-video | sc-3 |  | 1920x1080 · 20.80 s · 29.998 fps · hevc · 19.99 MB | `scenes/scene-3/IMG_8138.poster.jpg`<br>`scenes/scene-3/IMG_8138.strip.jpg` |
| `IMG_8139.HEIC` | build | sc-3 | behind-party | 4032x3024 · 1.58 MB | `scenes/scene-3/IMG_8139.jpg` |
| `IMG_8140.HEIC` | build | sc-3 | behind-party | 4032x3024 · 1.66 MB | `scenes/scene-3/IMG_8140.jpg` |
| `IMG_8141.HEIC` | build | sc-3 | coil-and-head-close | 4032x3024 · 1.51 MB | `scenes/scene-3/IMG_8141.jpg` |
| `IMG_8142.HEIC` | build | sc-3 | coil-and-head-close | 4032x3024 · 1.49 MB | `scenes/scene-3/IMG_8142.jpg` |
| `IMG_8143.HEIC` | build | sc-3 | coil-and-head-close | 4032x3024 · 1.65 MB | `scenes/scene-3/IMG_8143.jpg` |
| `IMG_8144.HEIC` | build | sc-3 |  | 4032x3024 · 1.61 MB | `scenes/scene-3/IMG_8144.jpg` |
| `IMG_8145.HEIC` | build | sc-3 |  | 4032x3024 · 1.67 MB | `scenes/scene-3/IMG_8145.jpg` |
| `IMG_8146.HEIC` | build | sc-3 | head-high-over-coil | 4032x3024 · 1.28 MB | `scenes/scene-3/IMG_8146.jpg` |
| `IMG_8147.HEIC` | build | sc-3 | head-high-over-coil | 4032x3024 · 1.13 MB | `scenes/scene-3/IMG_8147.jpg` |
| `IMG_8148.HEIC` | build | sc-3 | head-high-over-coil | 4032x3024 · 1.12 MB | `scenes/scene-3/IMG_8148.jpg` |
| `IMG_8149.HEIC` | build | sc-3 | head-high-over-coil | 4032x3024 · 1.07 MB | `scenes/scene-3/IMG_8149.jpg` |
| `IMG_8150.HEIC` | build | sc-3 | head-high-over-coil | 4032x3024 · 1.10 MB | `scenes/scene-3/IMG_8150.jpg` |
| `IMG_8151.HEIC` | build | sc-3 | head-high-over-coil | 4032x3024 · 1.25 MB | `scenes/scene-3/IMG_8151.jpg` |
| `IMG_8152.HEIC` | build | sc-3 | head-high-over-coil | 4032x3024 · 1.32 MB | `scenes/scene-3/IMG_8152.jpg` |
| `IMG_8153.HEIC` | build | sc-3 | head-high-over-coil | 4032x3024 · 1.21 MB | `scenes/scene-3/IMG_8153.jpg` |
| `IMG_8154.HEIC` | build | sc-3 | head-high-over-coil | 4032x3024 · 1.24 MB | `scenes/scene-3/IMG_8154.jpg` |
| `IMG_8155.HEIC` | build | sc-3 | head-high-over-coil | 4032x3024 · 1.32 MB | `scenes/scene-3/IMG_8155.jpg` |
| `IMG_8156.HEIC` | build | sc-3 | head-high-over-coil | 4032x3024 · 1.34 MB | `scenes/scene-3/IMG_8156.jpg` |
| `IMG_8157.HEIC` | build | sc-3 | head-high-over-coil | 4032x3024 · 1.28 MB | `scenes/scene-3/IMG_8157.jpg` |
| `IMG_8158.HEIC` | build | sc-3 | head-high-over-coil | 4032x3024 · 1.19 MB | `scenes/scene-3/IMG_8158.jpg` |
| `IMG_8159.HEIC` | build | sc-3 | head-high-over-coil | 4032x3024 · 1.13 MB | `scenes/scene-3/IMG_8159.jpg` |
| `IMG_8160.HEIC` | build | sc-3 | head-high-over-coil | 4032x3024 · 1.38 MB | `scenes/scene-3/IMG_8160.jpg` |
| `IMG_8161.HEIC` | build | sc-3 | head-high-over-coil | 4032x3024 · 1.57 MB | `scenes/scene-3/IMG_8161.jpg` |
| `IMG_8162.HEIC` | build | sc-3 | head-high-over-coil | 4032x3024 · 1.26 MB | `scenes/scene-3/IMG_8162.jpg` |
| `IMG_8163.HEIC` | build | sc-3 | head-high-over-coil | 4032x3024 · 1.36 MB | `scenes/scene-3/IMG_8163.jpg` |
| `IMG_8164.HEIC` | build | sc-3 | head-high-over-coil | 4032x3024 · 1.40 MB | `scenes/scene-3/IMG_8164.jpg` |
| `IMG_8165.HEIC` | build | sc-3 | head-high-over-coil | 4032x3024 · 1.50 MB | `scenes/scene-3/IMG_8165.jpg` |
| `IMG_8167.HEIC` | build | sc-3 |  | 4032x3024 · 1.41 MB | `scenes/scene-3/IMG_8167.jpg` |
| `IMG_8168.HEIC` | build | sc-3 |  | 4032x3024 · 1.28 MB | `scenes/scene-3/IMG_8168.jpg` |
| `IMG_8170.HEIC` | build | sc-3 |  | 4032x3024 · 1.00 MB | `scenes/scene-3/IMG_8170.jpg` |
| `IMG_8179.HEIC` | build | sc-3 |  | 4032x3024 · 1.02 MB | `scenes/scene-3/IMG_8179.jpg` |
| `IMG_8180.HEIC` | build | sc-3 |  | 4032x3024 · 0.96 MB | `scenes/scene-3/IMG_8180.jpg` |

### Pre Production Assets/Scenes/Scene 3/Scene 3 Actions (4)

| file | kind | subject | view or over | size | working copy |
| --- | --- | --- | --- | --- | --- |
| `IMG_0329.PNG` | action-map | sc-3 | over IMG_0112 | 4032x3024 · 19.31 MB | `scenes/scene-3/actions/IMG_0329.jpg` |
| `IMG_0330.PNG` | action-map | sc-3 | over IMG_8144 | 4032x3024 · 15.75 MB | `scenes/scene-3/actions/IMG_0330.jpg` |
| `IMG_0331.PNG` | action-map | sc-3 | over IMG_8141 | 4032x3024 · 14.45 MB | `scenes/scene-3/actions/IMG_0331.jpg` |
| `IMG_0332.PNG` | action-map | sc-3 | over IMG_8139 | 4032x3024 · 14.87 MB | `scenes/scene-3/actions/IMG_0332.jpg` |

### Script/Characters/All together (6)

the party in a row, for relative heights: left to right 4, 3, 5, 2, 7, 6, 1

| file | kind | subject | view or over | size | working copy |
| --- | --- | --- | --- | --- | --- |
| `IMG_8206.HEIC` | group |  |  | 4032x3024 · 1.40 MB | `characters/all-together/IMG_8206.jpg` |
| `IMG_8207.HEIC` | group |  |  | 4032x3024 · 1.41 MB | `characters/all-together/IMG_8207.jpg` |
| `IMG_8208.HEIC` | group |  |  | 4032x3024 · 1.49 MB | `characters/all-together/IMG_8208.jpg` |
| `IMG_8209.HEIC` | group |  |  | 4032x3024 · 1.39 MB | `characters/all-together/IMG_8209.jpg` |
| `IMG_8210.HEIC` | group |  |  | 4032x3024 · 1.37 MB | `characters/all-together/IMG_8210.jpg` |
| `IMG_8211.HEIC` | group |  |  | 4032x3024 · 1.36 MB | `characters/all-together/IMG_8211.jpg` |

### Script/Characters/Character 1 (4)

sword raised overhead in the right hand, blade broken at the top third; heater shield with a knot emblem on the left arm; scale cuirass, rounded pauldrons, tasset skirt, bracers, fur-topped boots, long hair

| file | kind | subject | view or over | size | working copy |
| --- | --- | --- | --- | --- | --- |
| `IMG_8216.HEIC` | print | ch-vessa | front | 4032x3024 · 0.75 MB | `characters/ch1-vessa/IMG_8216.jpg` |
| `IMG_8217.HEIC` | print | ch-vessa | right | 4032x3024 · 0.77 MB | `characters/ch1-vessa/IMG_8217.jpg` |
| `IMG_8218.HEIC` | print | ch-vessa | back | 4032x3024 · 0.78 MB | `characters/ch1-vessa/IMG_8218.jpg` |
| `IMG_8219.HEIC` | print | ch-vessa | left | 4032x3024 · 0.77 MB | `characters/ch1-vessa/IMG_8219.jpg` |

### Script/Characters/Character 1/Persona_Character Sheet (1)

| file | kind | subject | view or over | size | working copy |
| --- | --- | --- | --- | --- | --- |
| `Character 1 - Vessa Rowanblood (barbarian woman).md` | doc | ch-vessa |  | 5.5 kB |  |

### Script/Characters/Character 2 (4)

conical helmet with a nasal bar, two beard braids to the belt, pauldrons, scale tunic, long-hafted axe held upright, left hand on the hip

| file | kind | subject | view or over | size | working copy |
| --- | --- | --- | --- | --- | --- |
| `IMG_8220.HEIC` | print | ch-borrin | front | 4032x3024 · 0.77 MB | `characters/ch2-borrin/IMG_8220.jpg` |
| `IMG_8221.HEIC` | print | ch-borrin | right | 4032x3024 · 0.77 MB | `characters/ch2-borrin/IMG_8221.jpg` |
| `IMG_8222.HEIC` | print | ch-borrin | back | 4032x3024 · 0.77 MB | `characters/ch2-borrin/IMG_8222.jpg` |
| `IMG_8223.HEIC` | print | ch-borrin | left | 4032x3024 · 0.77 MB | `characters/ch2-borrin/IMG_8223.jpg` |

### Script/Characters/Character 2/Persona_Character Sheet (1)

| file | kind | subject | view or over | size | working copy |
| --- | --- | --- | --- | --- | --- |
| `Character 2 - Borrin Hollowcask (dwarf).md` | doc | ch-borrin |  | 5.4 kB |  |

### Script/Characters/Character 3 (4)

bare torso, fur loincloth with a round buckle, headband, shoulder-length hair, bracers, fur-topped boots; both hands on a sword hilt whose blade is broken off short

| file | kind | subject | view or over | size | working copy |
| --- | --- | --- | --- | --- | --- |
| `IMG_8224.HEIC` | print | ch-dax | front | 4032x3024 · 0.76 MB | `characters/ch3-dax/IMG_8224.jpg` |
| `IMG_8225.HEIC` | print | ch-dax | left | 4032x3024 · 0.77 MB | `characters/ch3-dax/IMG_8225.jpg` |
| `IMG_8226.HEIC` | print | ch-dax | back | 4032x3024 · 0.76 MB | `characters/ch3-dax/IMG_8226.jpg` |
| `IMG_8227.HEIC` | print | ch-dax | right | 4032x3024 · 0.76 MB | `characters/ch3-dax/IMG_8227.jpg` |

### Script/Characters/Character 3/Persona_Character Sheet (1)

| file | kind | subject | view or over | size | working copy |
| --- | --- | --- | --- | --- | --- |
| `Character 3 - Dax Vorrune (half-githyanki barbarian).md` | doc | ch-dax |  | 5.0 kB |  |

### Script/Characters/Character 4 (5)

long sleeveless belted gown with a front slit, bare feet, long straight hair, arms folded low, no weapon

| file | kind | subject | view or over | size | working copy |
| --- | --- | --- | --- | --- | --- |
| `IMG_8228.HEIC` | print | ch-sylwen | front | 4032x3024 · 0.77 MB | `characters/ch4-sylwen/IMG_8228.jpg` |
| `IMG_8229.HEIC` | print | ch-sylwen | right | 4032x3024 · 0.75 MB | `characters/ch4-sylwen/IMG_8229.jpg` |
| `IMG_8230.HEIC` | print | ch-sylwen | back | 4032x3024 · 0.74 MB | `characters/ch4-sylwen/IMG_8230.jpg` |
| `IMG_8231.HEIC` | print | ch-sylwen | left | 4032x3024 · 0.76 MB | `characters/ch4-sylwen/IMG_8231.jpg` |
| `IMG_8232.HEIC` | print | ch-sylwen | left | 4032x3024 · 0.76 MB | `characters/ch4-sylwen/IMG_8232.jpg` |

### Script/Characters/Character 4/Persona_Character Sheet (1)

| file | kind | subject | view or over | size | working copy |
| --- | --- | --- | --- | --- | --- |
| `Character 4 - Sylwen Aerindel (elf healer).md` | doc | ch-sylwen |  | 4.7 kB |  |

### Script/Characters/Character 5 (4)

elderly, long beard, flat round cap, belted robe with a round medallion, long cape, tall staff with a faceted crystal in the right hand, left hand raised

| file | kind | subject | view or over | size | working copy |
| --- | --- | --- | --- | --- | --- |
| `IMG_8233.HEIC` | print | ch-oswin | front | 4032x3024 · 0.79 MB | `characters/ch5-oswin/IMG_8233.jpg` |
| `IMG_8234.HEIC` | print | ch-oswin | right | 4032x3024 · 0.76 MB | `characters/ch5-oswin/IMG_8234.jpg` |
| `IMG_8235.HEIC` | print | ch-oswin | back | 4032x3024 · 0.80 MB | `characters/ch5-oswin/IMG_8235.jpg` |
| `IMG_8236.HEIC` | print | ch-oswin | left-three-quarter | 4032x3024 · 0.75 MB | `characters/ch5-oswin/IMG_8236.jpg` |

### Script/Characters/Character 5/Persona_Character Sheet (1)

| file | kind | subject | view or over | size | working copy |
| --- | --- | --- | --- | --- | --- |
| `Character 5 - Father Oswin Tallow (human priest).md` | doc | ch-oswin |  | 5.2 kB |  |

### Script/Characters/Character 6 (4)

long cloak with the hood pushed back, fitted cuirass, belt with pouches, thigh boots, a thin sword held point down in the right hand, shoulder-length hair

| file | kind | subject | view or over | size | working copy |
| --- | --- | --- | --- | --- | --- |
| `IMG_8237.HEIC` | print | ch-vel | front | 4032x3024 · 0.79 MB | `characters/ch6-vel/IMG_8237.jpg` |
| `IMG_8238.HEIC` | print | ch-vel | right | 4032x3024 · 0.77 MB | `characters/ch6-vel/IMG_8238.jpg` |
| `IMG_8239.HEIC` | print | ch-vel | back | 4032x3024 · 0.80 MB | `characters/ch6-vel/IMG_8239.jpg` |
| `IMG_8240.HEIC` | print | ch-vel | left | 4032x3024 · 0.76 MB | `characters/ch6-vel/IMG_8240.jpg` |

### Script/Characters/Character 6/Persona_Character Sheet (1)

| file | kind | subject | view or over | size | working copy |
| --- | --- | --- | --- | --- | --- |
| `Character 6 - Sera'kith Vel (githyanki leader).md` | doc | ch-vel |  | 5.7 kB |  |

### Script/Characters/Character 7 (4)

skull face, helmet with two curving horns meeting in a ring with a ball on top, layered armour with small skull ornaments, long tabard front and back, bracers, no weapon, both arms raised wide

| file | kind | subject | view or over | size | working copy |
| --- | --- | --- | --- | --- | --- |
| `IMG_8241.HEIC` | print | ch-mordecai | front | 4032x3024 · 0.79 MB | `characters/ch7-mordecai/IMG_8241.jpg` |
| `IMG_8242.HEIC` | print | ch-mordecai | right | 4032x3024 · 0.76 MB | `characters/ch7-mordecai/IMG_8242.jpg` |
| `IMG_8243.HEIC` | print | ch-mordecai | back | 4032x3024 · 0.79 MB | `characters/ch7-mordecai/IMG_8243.jpg` |
| `IMG_8244.HEIC` | print | ch-mordecai | left | 4032x3024 · 0.77 MB | `characters/ch7-mordecai/IMG_8244.jpg` |

### Script/Characters/Character 7/Persona_Character Sheet (1)

| file | kind | subject | view or over | size | working copy |
| --- | --- | --- | --- | --- | --- |
| `Character 7 - Mordecai Ashgrave (undead necromancer).md` | doc | ch-mordecai |  | 4.9 kB |  |

### Script/Characters/Mob 1 (8)

six small frogs, front legs together

| file | kind | subject | view or over | size | working copy |
| --- | --- | --- | --- | --- | --- |
| `IMG_8245.HEIC` | mob-print | ch-mob-frogs | cluster-front | 4032x3024 · 0.75 MB | `characters/mob1-frogs/IMG_8245.jpg` |
| `IMG_8246.HEIC` | mob-print | ch-mob-frogs | front | 4032x3024 · 0.73 MB | `characters/mob1-frogs/IMG_8246.jpg` |
| `IMG_8247.HEIC` | mob-print | ch-mob-frogs | right | 4032x3024 · 0.72 MB | `characters/mob1-frogs/IMG_8247.jpg` |
| `IMG_8248.HEIC` | mob-print | ch-mob-frogs | back | 4032x3024 · 0.73 MB | `characters/mob1-frogs/IMG_8248.jpg` |
| `IMG_8249.HEIC` | mob-print | ch-mob-frogs | three-quarter | 4032x3024 · 0.73 MB | `characters/mob1-frogs/IMG_8249.jpg` |
| `IMG_8250.HEIC` | mob-print | ch-mob-frogs | cluster-low | 4032x3024 · 0.75 MB | `characters/mob1-frogs/IMG_8250.jpg` |
| `IMG_8251.MOV` | mob-video | ch-mob-frogs |  | 1920x1440 · 0.50 s · 30 fps · hevc · 0.80 MB | `characters/mob1-frogs/IMG_8251.poster.jpg`<br>`characters/mob1-frogs/IMG_8251.strip.jpg` |
| `IMG_8252.HEIC` | mob-print | ch-mob-frogs | cluster-low | 4032x3024 · 0.75 MB | `characters/mob1-frogs/IMG_8252.jpg` |

### Script/Characters/Mob 2 (10)

an articulated segmented body about 40 rings long with a flared head; the print's big round "eye" marks the mouth end (the worm is blind), its cowl is the swollen collar, its shed crescent plates are the skin it sloughs

| file | kind | subject | view or over | size | working copy |
| --- | --- | --- | --- | --- | --- |
| `IMG_8253.HEIC` | mob-print | ch-mob-worm |  | 4032x3024 · 1.29 MB | `characters/mob2-worm/IMG_8253.jpg` |
| `IMG_8254.HEIC` | mob-print | ch-mob-worm |  | 4032x3024 · 1.24 MB | `characters/mob2-worm/IMG_8254.jpg` |
| `IMG_8255.HEIC` | mob-print | ch-mob-worm |  | 4032x3024 · 1.35 MB | `characters/mob2-worm/IMG_8255.jpg` |
| `IMG_8256.HEIC` | mob-print | ch-mob-worm |  | 4032x3024 · 1.31 MB | `characters/mob2-worm/IMG_8256.jpg` |
| `IMG_8257.HEIC` | mob-print | ch-mob-worm |  | 4032x3024 · 1.30 MB | `characters/mob2-worm/IMG_8257.jpg` |
| `IMG_8258.HEIC` | mob-print | ch-mob-worm |  | 4032x3024 · 1.30 MB | `characters/mob2-worm/IMG_8258.jpg` |
| `IMG_8259.HEIC` | mob-print | ch-mob-worm |  | 4032x3024 · 1.20 MB | `characters/mob2-worm/IMG_8259.jpg` |
| `IMG_8260.HEIC` | mob-print | ch-mob-worm |  | 4032x3024 · 1.34 MB | `characters/mob2-worm/IMG_8260.jpg` |
| `IMG_8261.HEIC` | mob-print | ch-mob-worm |  | 4032x3024 · 1.40 MB | `characters/mob2-worm/IMG_8261.jpg` |
| `IMG_8262.HEIC` | mob-print | ch-mob-worm |  | 4032x3024 · 1.27 MB | `characters/mob2-worm/IMG_8262.jpg` |

### Script/Characters/Size from afar (4)

Character 1 against the grid

| file | kind | subject | view or over | size | working copy |
| --- | --- | --- | --- | --- | --- |
| `IMG_8212.HEIC` | scale | ch-vessa |  | 4032x3024 · 1.32 MB | `characters/size-from-afar/IMG_8212.jpg` |
| `IMG_8213.HEIC` | scale | ch-vessa |  | 4032x3024 · 1.34 MB | `characters/size-from-afar/IMG_8213.jpg` |
| `IMG_8214.HEIC` | scale | ch-vessa |  | 4032x3024 · 1.36 MB | `characters/size-from-afar/IMG_8214.jpg` |
| `IMG_8215.HEIC` | scale | ch-vessa |  | 4032x3024 · 1.36 MB | `characters/size-from-afar/IMG_8215.jpg` |

### Script/Script (Scene 1 to 3)/Scene 1 (Direction & Description) (2)

| file | kind | subject | view or over | size | working copy |
| --- | --- | --- | --- | --- | --- |
| `Scene 1 - Environment.md` | doc | sc-1 |  | 4.0 kB |  |
| `Scene 1 - Shot list.md` | doc | sc-1 |  | 8.7 kB |  |

### Script/Script (Scene 1 to 3)/Scene 2 (Direction & Description) (2)

| file | kind | subject | view or over | size | working copy |
| --- | --- | --- | --- | --- | --- |
| `Scene 2 - Environment.md` | doc | sc-2 |  | 3.7 kB |  |
| `Scene 2 - Shot list.md` | doc | sc-2 |  | 7.7 kB |  |

### Script/Script (Scene 1 to 3)/Scene 3 (Direction & Description) (2)

| file | kind | subject | view or over | size | working copy |
| --- | --- | --- | --- | --- | --- |
| `Scene 3 - Environment.md` | doc | sc-3 |  | 4.1 kB |  |
| `Scene 3 - Shot list.md` | doc | sc-3 |  | 14.3 kB |  |

### Script/Script (Scene 1 to 3)/Script Final (1)

| file | kind | subject | view or over | size | working copy |
| --- | --- | --- | --- | --- | --- |
| `SCRIPT.md` | doc |  |  | 7.3 kB |  |

### Script/Setting & Look & Feel Descriptions/Environment/Castle at night (1)

| file | kind | subject | view or over | size | working copy |
| --- | --- | --- | --- | --- | --- |
| `00 - The three ambiances, one place.md` | doc |  |  | 7.5 kB |  |

### Script/Setting & Look & Feel Descriptions/Mobs & Enemies (2)

| file | kind | subject | view or over | size | working copy |
| --- | --- | --- | --- | --- | --- |
| `Mob 1 - Frogs and toads.md` | doc | ch-mob-frogs |  | 4.6 kB |  |
| `Mob 2 - The earthworm.md` | doc | ch-mob-worm |  | 5.0 kB |  |

### Task (2)

| file | kind | subject | view or over | size | working copy |
| --- | --- | --- | --- | --- | --- |
| `In Short.md` | doc |  |  | 312 B |  |
| `Runware_Creative Engineer Assessment (1).pdf` | doc |  |  | 80.8 kB |  |

## Contact sheets

- `contact/all-together.jpg`: 6 pictures, 2208x1250
- `contact/size-from-afar.jpg`: 4 pictures, 2940x654
- `contact/mob1-frogs.jpg`: 8 pictures, 2940x1250
- `contact/mob2-worm.jpg`: 10 pictures, 2940x1846
- `contact/broll.jpg`: 27 pictures, 3000x2158
- `contact/ch1-vessa.jpg`: 4 pictures, 2940x654
- `contact/ch2-borrin.jpg`: 4 pictures, 2940x654
- `contact/ch3-dax.jpg`: 4 pictures, 2940x654
- `contact/ch4-sylwen.jpg`: 5 pictures, 2997x553
- `contact/ch5-oswin.jpg`: 4 pictures, 2940x654
- `contact/ch6-vel.jpg`: 4 pictures, 2940x654
- `contact/ch7-mordecai.jpg`: 4 pictures, 2940x654
- `contact/scene-1.jpg`: 30 pictures, 2994x1888
- `contact/scene-1-actions.jpg`: 18 pictures, 2997x2038
- `contact/scene-2.jpg`: 15 pictures, 2997x1543
- `contact/scene-2-actions.jpg`: 13 pictures, 2997x1543
- `contact/scene-3.jpg`: 35 pictures, 2994x1888
- `contact/scene-3-actions.jpg`: 4 pictures, 2940x654
