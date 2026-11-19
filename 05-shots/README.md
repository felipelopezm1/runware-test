# 05-shots: one folder per shot

The storyboard (rev 15) has 16 takes across the three scenes, 62 s on screen. Every shot goes through the same chain, and its folder holds one thing per link of that chain:

```
1A/
  README.md      the shot in one line, its size, angle, move, lens and length, and where it stands
  clay/          the blocking clip from the Blender stage (the locked camera and motion guide), its first frame (the layout reference), and the passes (depth, normals, lines, cameras.json)
  frame/         every frame take drawn on Nano Banana Pro, and the one approved (frame-pick.png)
  takes/         every clip take on Seedance 2.5 (<shot>-take-<n>-seedance-2.5.mp4), each rated
  pick.mp4       the take chosen for the cut (a copy also goes to 07-cut/)
  prompt.txt     the assembled clip prompt exactly as sent (a copy of 04-prompts/shots/<shot>.clip.txt)
```

The titles below are the storyboard's. The shot lists in `01-story/` name them 1A, 1B, 1C-1, 1C-2, 2A-1 and so on; the storyboard letters them straight through.

| shot | scene | title | size | angle | move | lens | length | status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [`1A/`](1A/) | Scene 1 | The last of the bread | TABLEAU | low angle | delayed push | 35 mm | 5 s | planned |
| [`1B/`](1B/) | Scene 1 | The dead pond | MCU | chest height | breath-drift hold | 50 mm | 4 s | planned |
| [`1C/`](1C/) | Scene 1 | Company: the stairs (from the doorway) | WS | high angle | handheld float | 28 mm | 2.5 s | planned |
| [`1D/`](1D/) | Scene 1 | Company: the room erupts (behind Mordecai and Oswin) | WS | low angle | handheld | 28 mm | 3.5 s | planned |
| [`2A/`](2A/) | Scene 2 | Eleven. Nine. (over Mordecai's shoulder) | MWS | rear three-quarter | over-shoulder follow | 35 mm | 2 s | planned |
| [`2B/`](2B/) | Scene 2 | The follow, carried on | MWS | rear three-quarter | over-shoulder follow | 35 mm | 3 s | planned |
| [`2C/`](2C/) | Scene 2 | Oswin's water does nothing | MS | hip level | handheld float | 50 mm | 4 s | planned |
| [`2D/`](2D/) | Scene 2 | They were running from something | WS | profile angle | parallel track | 40 mm | 6 s | planned |
| [`3A/`](3A/) | Scene 3 | Into the roofless hall | EWS | rear three-quarter | crane up | 24 mm | 5 s | planned |
| [`3B/`](3B/) | Scene 3 | The worm rears | WS | low angle | tilt up | 28 mm | 5 s | planned |
| [`3C/`](3C/) | Scene 3 | Vessa hacks at the collar | MS | eye level | handheld | 50 mm | 2 s | planned |
| [`3D/`](3D/) | Scene 3 | Behind the shield; Sylwen in the coil | MS | eye level | breath-drift hold | 50 mm | 3 s | planned |
| [`3E/`](3E/) | Scene 3 | Up out of the mud | FS | hero low angle | arc follow | 35 mm | 3 s | planned |
| [`3F/`](3F/) | Scene 3 | Forward through the rain | FS | hero low angle | handheld | 35 mm | 3 s | planned |
| [`3G/`](3G/) | Scene 3 | Dax's jump and Mordecai's blast | FS | low angle | snap-zoom-in punch | 85 mm | 5 s | planned |
| [`3H/`](3H/) | Scene 3 | Is this all on Runware? | TABLEAU | low angle | locked-off | 24 mm | 6 s | planned |

**Status words:** planned (on the storyboard), blocked (clay clip made), framed (frame approved), filmed (a take picked), cut (in the film). All sixteen are *planned* as of 19 November 2026 14:00 UTC; blocking is next. The first paid clip will be 1A at 4K, the proof that the 4K path holds before any other clip is made.

Takes are 4K MP4s and will be large (tens of MB each). See the README's note on large files.
