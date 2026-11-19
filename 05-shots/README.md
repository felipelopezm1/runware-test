# 05-shots: one folder per shot

Sixteen shots, named as the shot lists and the takes name them (`1C-1`, `2A-2`; the storyboard's own lettering, 1A to 3H, is in the second column). Two **bridges** were filmed to carry the cut from scene 1 into scene 2 and from scene 2 into scene 3. Every shot went the same way, and its folder holds one thing per link of the chain:

```
1C-2/
  README.md          the shot in one line, its size, angle, move, lens and length, and what was filmed
  clay/              the blocking clip from the Blender stage (the locked camera and motion guide), its first frame (the layout reference), cameras.json
  takes/             every clip take on Seedance 2.5: take-1, then v2, v3 where the shot was filmed again
  pick.mp4           the take that went into the cut
  compare/           the comparison strips: build photo, clay, take, side by side
  prompt.txt         the assembled clip prompt as sent (pending the copy)
```

All sixteen clay clips, first frames and camera files are here. The takes and picks are here too (every take is 2 to 5 MB, so plain Git holds them all); the compare strips for the shots that were filmed again. Frames drawn on Nano Banana Pro: see the note in each folder.

| folder | board | scene | title | size | angle | move | lens | length | takes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [`1A/`](1A/) | 1A | Scene 1 | The last of the bread | TABLEAU | low angle | delayed push | 35 mm | 5 s | take-1, v2 |
| [`1B/`](1B/) | 1B | Scene 1 | The dead pond | MCU | chest height | breath-drift hold | 50 mm | 4 s | take-1 |
| [`1C-1/`](1C-1/) | 1C | Scene 1 | Company: the stairs (from the doorway) | WS | high angle | handheld float | 28 mm | 2.5 s | take-1 |
| [`1C-2/`](1C-2/) | 1D | Scene 1 | Company: the room erupts (behind Mordecai and Oswin) | WS | low angle | handheld | 28 mm | 3.5 s | take-1, v2, v3 |
| [`2A-1/`](2A-1/) | 2A | Scene 2 | Eleven. Nine. (over Mordecai's shoulder) | MWS | rear three-quarter | over-shoulder follow | 35 mm | 2 s | take-1, v2 |
| [`2A-2/`](2A-2/) | 2B | Scene 2 | The follow, carried on | MWS | rear three-quarter | over-shoulder follow | 35 mm | 3 s | take-1, v2, v3 |
| [`2B/`](2B/) | 2C | Scene 2 | Oswin's water does nothing | MS | hip level | handheld float | 50 mm | 4 s | take-1, v2 |
| [`2C/`](2C/) | 2D | Scene 2 | They were running from something | WS | profile angle | parallel track | 40 mm | 6 s | take-1, v2, v3 |
| [`3A/`](3A/) | 3A | Scene 3 | Into the roofless hall | EWS | rear three-quarter | crane up | 24 mm | 5 s | take-1, v2 |
| [`3B/`](3B/) | 3B | Scene 3 | The worm rears | WS | low angle | tilt up | 28 mm | 5 s | take-1 |
| [`3C-1/`](3C-1/) | 3C | Scene 3 | Vessa hacks at the collar | MS | eye level | handheld | 50 mm | 2 s | take-1 |
| [`3C-2/`](3C-2/) | 3D | Scene 3 | Behind the shield; Sylwen in the coil | MS | eye level | breath-drift hold | 50 mm | 3 s | take-1 |
| [`3D-1/`](3D-1/) | 3E | Scene 3 | Up out of the mud | FS | hero low angle | arc follow | 35 mm | 3 s | take-1, v2 |
| [`3D-2/`](3D-2/) | 3F | Scene 3 | Forward through the rain | FS | hero low angle | handheld | 35 mm | 3 s | take-1 |
| [`3E/`](3E/) | 3G | Scene 3 | Dax's jump and Mordecai's blast | FS | low angle | snap-zoom-in punch | 85 mm | 5 s | take-1 |
| [`3F/`](3F/) | 3H | Scene 3 | Is this all on Runware? | TABLEAU | low angle | locked-off | 24 mm | 6 s | take-1 |
| [`bridges/`](bridges/) | | 1 to 2, 2 to 3 | the two bridge clips that carry the cut between scenes | | | | | | v1, final |

**Status, 19 November 2026 16:00 UTC:** every shot is filmed and has a pick; the clean cut and the 4K finish are being built in [`07-cut/`](../07-cut/).
