# Stage axes: the frame every position in this film is written in

Written 2026-11-19 by the stage lane (session you-can-deploy-implement-9xo-ac) before the three location stages were built.
The stages are free prep made ahead of the storyboard's approval: clay primitives and one cylinder per character, throwaway if a location changes.
Where a stage and the intake notes' reading of the build photos disagree, the intake notes win and the stage is rebuilt.

## Common to all three stages

- Blender stage scenes, glTF convention: **Y is up**, metres, right-handed.
- **Origin** = the middle of the room's floor. A position on the floor is `(x, z)`; `y` is height above the floor.
- **+X** = the right-hand side of the location's *master view* (named per location below). **+Z** = toward that master camera. So "back" is -Z, "front" is +Z, "left" is -X, "right" is +X.
- **Facing** is a yaw in degrees about +Y: `0` faces +Z (toward the master camera), `+90` faces +X (right), `180` faces -Z (the back), `-90` faces -X (left).
- The room sizes are the lock blocks' (bible section 6), not the miniature's. The clay builds are smaller in proportion, so a thing is placed **by proportion**: read its place in the build as fractions `u` (0 at the left wall, 1 at the right wall) and `v` (0 at the back, 1 at the front, both as the master view sees them), then `x = (u - 0.5) * W` and `z = (v - 0.5) * D`. Intake notes may give either `(u, v)` or metres; say which.
- Heights of the cast stand-ins: Vel 1.85 m, Mordecai 1.90, Vessa 1.80, Dax 1.95, Borrin 1.30, Sylwen 1.75, Oswin 1.70. Their scene ids are the bible's: `ch-vel`, `ch-mordecai`, `ch-vessa`, `ch-dax`, `ch-borrin`, `ch-sylwen`, `ch-oswin`; the worm's parts are `ch-mob-worm-*`.

## lo-storeroom (scene 1) — twin without the vault: lo-storeroom-open

- Master view: `Scenes/Scene 1/IMG_8087.HEIC` (low three-quarter from the open front, the whole circle).
- Size: W = 8 m along X, D = 6 m along Z, 5 m to the vault's apex. `x` runs -4 to +4, `z` runs -3 to +3.
- Back wall at `z = -3`, left wall at `x = -4`, right wall at `x = +4`, **no front wall** (`z = +3` is open: the camera's side).
- The staircase, 1.5 m wide, runs along the right wall (`x` from +2.5 to +4). Which end is its foot is read from the photos; the prose says it climbs from the floor at the front to a doorway in the back-right corner.
- Crates and a sack: back left (-X, -Z). Barrels and a sack: front left (-X, +Z).

## lo-corridor (scene 2) — twin without the vault: lo-corridor-open

- Master view: `Scenes/Scene 2/IMG_8119.HEIC` (wide from the open near end, looking toward the stairs).
- Size: W = 3 m along X, D = 30 m along Z, 4 m high. `x` runs -1.5 to +1.5, `z` runs -15 to +15.
- The **near archway** (cold grey light, where Vel stops in 2C) is at `z = +15`. The **stair doorway** (the top of the storeroom's stairs, where the party comes in) is at `z = -15`. The party advances toward +Z.
- A distance "d metres along" in the lock block is measured from the near archway: `z = 15 - d` (the niche near d = 20, the slab near d = 25, the crate and barrel near d = 27).
- Left wall at `x = -1.5`, right wall at `x = +1.5`, as the master view sees them. Which wall carries the bench and which the niche is read from the photos (the prose calls the bench wall "left" from both ends).

## lo-roofless-hall (scene 3) — twin without the wall nearest the master camera: lo-roofless-hall-open

- Master view: `Scenes/Scene 3/IMG_0112.HEIC` (party at the left, the bench with frogs in the centre, the worm's head at the right).
- Size: W = 40 m along X, D = 25 m along Z, no roof. `x` runs -20 to +20, `z` runs -12.5 to +12.5.
- The party's archway is on the **-X** side. The tall back wall (15 m) is at `z = -12.5`. The worm's head is toward +X.
- The mud patch is a disc 20 m across, centre right; the rubble mound stands in it; the stepped platform of fallen blocks is at the back right (+X, -Z).
- The top-down photo `Scenes/Scene 3/IMG_0111.HEIC` is the plan view; which of its edges is the master camera's side is stated in `roofless-hall.md` once the stage stands.

## Where the built values are

Each stage's own note in this folder (`storeroom.md`, `corridor.md`, `roofless-hall.md`) lists every object with its id, position and size, the cast table, the camera views, the scene's rev, and every place where the prose and the build disagreed.
