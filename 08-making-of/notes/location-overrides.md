# Location overrides: the layout phrases of the three location LOCK BLOCKS

By the director spider, 2026-11-19, on Felipe's yes of 12:04 UTC ("yes to all, apply the layout pass ..."), which
approves decision 17 (`notes/HANDOFF.md`): the location layout phrases follow the build. This file is the director's;
the prompt assembler reads it (contract: `notes/prompt-lengths.md`, section (f), "Location overrides") and applies each
row to the prompt copy of its LOCK BLOCK when `locationOverrides` is "on" in `prompts/shots.json`. The bible, the
board's location descriptions and Felipe's pack are never edited: every LOCK BLOCK stays character for character on
the board (`tools/director/verify_shooting.py` checks), and only the copy sent in a prompt takes these phrases.

What a row may change: which side, which end, how many steps, where the slab, the bench, the stairs, the barrels and
the crates stand. Never a material, light or mood word: the self-test fails a row that drops or adds one of the
protected words. Every position comes from the readers' layout (`notes/scene-1.md`, `notes/scene-2.md`,
`notes/scene-3.md` and their `notes/_parts/map-vs-shotlist-s1.md`, `-s2.md`, `-s3.md`), read by eye from the build
photos; none from `clay/_stage/axes.md`, whose storeroom lines are mirrored against the build. Left and right are
each location's master view: the storeroom from its open front (8087, the 1A camera), the corridor from the archway
end looking toward the stairs (8119), the hall from behind the party looking toward the worm (0112, 0111 as the plan).

| id | location | the owner's words | the build's words | why |
| --- | --- | --- | --- | --- |
| storeroom-crates | lo-storeroom | `Along the back-left corner three stacked wooden crates and a slumped sack` | `Along the front-right corner three stacked wooden crates and a slumped sack` | the big crate pile and its sack stand in the front-right corner, two more crates along the front wall beside them (scene-1.md (a), crates and sack; 8086, 8087, 8091, 8094, 8097, 8104) |
| storeroom-barrels | lo-storeroom | `at the front left a cluster of three iron-banded barrels and a sack` | `at the back right, against the right wall beside the upper stairs, a cluster of three iron-banded barrels and a sack` | the three barrels and the sack stand against the right wall's back end, less than a barrel from the upper half of the stairs (scene-1.md (a), barrels and sack; 8086, 8087, 8093, 8094) |
| storeroom-stairs | lo-storeroom | `From the floor at the front a straight stone staircase 1.5 m wide climbs along the right wall to a dark doorway in the back-right corner` | `From the floor at the left, about mid-depth, a straight stone staircase 1.5 m wide climbs about twelve steps along the slanting left wall to a dark doorway at the back, just left of centre` | the stairs' foot is inside the room at the left about mid-depth; they climb about twelve treads along the slanted stair wall to the back edge just left of centre, where the doorway goes (scene-1.md (a), staircase and steps; map-vs-shotlist-s1.md rows 1 and 5; 8087, 8088, 8093, 8100) |
| storeroom-stair-top | lo-storeroom | `two more crates and a fallen block at its top` | `two more crates and a fallen block beside its top on the stair-wall side` | the top crates and the grey block sit on the stair-wall side of the top step (scene-1.md (a), crates at the top; 8087, 8093, 8096, 8097) |
| corridor-steps | lo-corridor | `its far end the top of the storeroom's staircase` | `its far end a flight of about ten steps rising inside it to the top of the storeroom's staircase` | a flight of about ten treads stands inside the far end; the party comes down it into the corridor (scene-2.md (a), flight of steps; map-vs-shotlist-s2.md row 1; 8119 to 8122, 8127 to 8129) |
| corridor-archway | lo-corridor | `its near end an open archway` | `its near end an open archway set left of centre, where the left wall stops short` | the gateway is left of centre; the left wall stops short of it and the way out bends past its free end (scene-2.md (a), archway and left wall; map-vs-shotlist-s2.md rows 7 and 19; 8119, 8130, 0333, 0334) |
| corridor-bench | lo-corridor | `Along the left wall a long low stone bench` | `Along the left wall, from the foot of those steps toward the middle, a long low stone bench` | the bench runs along the left wall from the stair foot, about 15 to 21 m from the archway (scene-2.md (a), bench; map-vs-shotlist-s2.md, the bench row; 8119, 8121 to 8127) |
| corridor-niche | lo-corridor | `on the right wall a barred window niche` | `on the right wall, raised on its low section about 11 m from the archway, a barred window niche` | the niche sits on top of the right wall's low section, just past the bench's near end toward the archway (scene-2.md (a), barred window niche; map-vs-shotlist-s2.md row 4; 8122 to 8124, 8131 to 8133) |
| corridor-slab | lo-corridor | `a fallen stone slab near the far end` | `a fallen stone slab against the right wall near the archway` | the slab leans on the right wall's rubble at the near end, 2 to 5 m from the archway (scene-2.md (a), slab; map-vs-shotlist-s2.md row 5; 8119, 8130 to 8133) |
| corridor-side-opening | lo-corridor | `a crate and a barrel in a side opening near the stairs` | `a crate and a barrel in a side opening in the right wall about 17 m from the archway` | the side opening is a gap in the right wall a few metres short of the stair foot, the crate and barrel just outside it (scene-2.md (a), side opening; map-vs-shotlist-s2.md row 6 (a); 8119, 8123, 8124, 8127) |
| hall-walls | lo-roofless-hall | `high broken walls of pale weathered limestone on three sides, taller at the back` | `broken walls of pale weathered limestone on three sides, high only where they curve round the far end behind the mound, low broken stubs along the two long sides` | the only tall wall is the curved apse round the far end; the long sides are low stubs near it and open toward the party (scene-3.md (a), walls; map-vs-shotlist-s3.md row 2; 0111, 0112, 8141, 8144) |
| hall-bench | lo-roofless-hall | `A long stone bench to one side with frogs on it` | `A long stone bench between the archway and the mound with frogs on it` | the frog bench stands just ahead of the party, between it and the mound (scene-3.md (a), bench with frogs; 0111, 0112, 8138, 8144) |
| hall-niche-slab | lo-roofless-hall | `a barred window niche and a fallen slab pushed against the walls` | `a barred window niche standing free on the floor beside the mound and a fallen slab along one long side` | the niche is a free-standing grid box on the floor outside the coil, in no wall; the slab lies along the far long side as a low stub (scene-3.md (a), niche and low slab; map-vs-shotlist-s3.md row 23; 0111, 8146, 8168) |
| hall-barrels-crates | lo-roofless-hall | `more barrels and crates in the corners` | `more barrels round the mound and crates stacked either side of the archway` | two crate stacks flank the party where it enters (the archway's gateposts); the barrels stand in two groups at the coil's edge (scene-3.md (a), crates and barrels; map-vs-shotlist-s3.md row 3; 0111, 8138, 8146, 8168) |

Not changed here, and why:

- **The storeroom's doorway, torch, vault, water and loose blocks**, and **the corridor's vault, sconces and chains**:
  the build shows none of them, but they are not layout; the words stand.
- **The corridor's crate stack with three barrels in the far-left corner by the stair foot** (map-vs-shotlist-s2.md
  row 6 (b)) is an object the block does not name: adding it is more than a layout phrase. The re-staged bodies of
  2A-1 and 2A-2 carry it.
- **The hall's mound "in the centre"**: the build's is a little right of centre; the readers judge the block's 20 m
  "centre right" to hold, so the words stand. The worm's size, the mound's size and the head hidden until 3B are
  separate proposals on the board's notes, not layout phrases.
