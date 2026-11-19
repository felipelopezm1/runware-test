# MOB 1: THE POISONOUS FROGS AND TOADS
### A swarm. Different colours, all poisonous, all dangerous, none of them clever.
Storyboard id `ch-mob-frogs`. Scenes 1 and 2, and a few on the bench at the start of scene 3.
**Print:** `Creative Task Runware/Script/Characters/Mob 1/IMG_8245.HEIC` (a cluster of six, front), `IMG_8246` to `IMG_8249` (one frog front, right, back, three-quarter), `IMG_8250` and `IMG_8252` (the cluster, low), `IMG_8251.MOV` (0.5 s). In the builds: one on the stairs in `Scenes/Scene 1/IMG_8096`, on the barrels and stairs from `IMG_8097`, twenty on the corridor floor in `Scenes/Scene 2/IMG_8126`, a few on the bench in `Scenes/Scene 3/IMG_0112`.

## What they are
Dungeon amphibians grown fat and bright on something in the water below. They come in a swarm of forty to sixty, from fist-sized frogs to toads the size of a small dog. They are not clever: they go for the light and the movement, climb over each other, and leap at anything that swings. They are running from the worm, which the party does not understand until Vel does at the end of scene 2.

## LOCK BLOCK (paste unchanged into every prompt where they appear)
> FROGS AND TOADS: a swarm of poisonous frogs and toads from fist-sized to the size of a small dog, glistening with mucus. The frogs are poison-dart coloured: electric blue with black spots, acid yellow with black bands, blood orange, violet with black legs, lime green with black eyes. The toads are warty olive-brown with blood-red eyes and swollen poison glands behind the head that weep milky venom. Wide mouths, long pink tongues, gold eyes with horizontal pupils. They move as a swarm: leaping, climbing over one another, clinging to walls and stairs, lashing with tongues and spitting venom. Dozens at once, never one alone, never cute, every one wet.

## The six kinds (so a shot can name one)
| kind | size | colour | attack |
| --- | --- | --- | --- |
| blue dart | fist | electric blue, black spots | 2 m leap, bite |
| yellow band | fist | acid yellow, black bands | spits a venom gob that smokes on stone |
| orange | two fists | blood orange, black feet | tongue lash, 1.5 m |
| violet | two fists | violet body, black legs, white throat | clings to walls and drops from above |
| lime | fist | lime green, huge black eyes | the fastest; swarms legs |
| the toads | small dog | warty olive-brown, blood-red eyes, swollen glands | heavy slam, milky venom spray from the glands when struck |

## Behaviour per shot
- **1C**: they come down the stairs from the dark doorway as a single pouring mass, eyes first (dozens of gold points in the dark above), then the front rank leaps the last three steps into the lantern light, and at the same moment more burst out of the barrels (the blue flame shapes in `Scene 1 Actions/IMG_0349` to `0352`).
- **2A to 2B**: the corridor is a channel; they fill the floor, climb the walls, sit on the bench and hang from the chains; toads come behind the frogs like shields; one toad knocks Vessa flat.
- **2C**: the last of them run PAST the party back toward the stairs; one orange frog sits in Oswin's puddle and croaks at him.
- **3A**: a few on the stone bench leap off and scatter toward the mound when the coil moves (`Scene 3 Actions/IMG_0329`).

## Sound
Wet slaps, chirps and croaks rising to a chorus like a marsh at night; a toad's bass croak; a venom gob hissing on stone; a tongue snap like a wet whip. (`rw_audio` Mirelo SFX.)

## Facts for `sheet_build` (one sheet for the mob)
```
build: a swarm, six kinds, fist to small dog
palette: electric blue #1E6BFF, acid yellow #E3FF2B, blood orange #FF5A1F, violet #7A2BD6, lime #8CFF3D, toad olive-brown #5E5A2E, toad eye red #C8102E, venom milk #EDE8D0, black #0A0A0A
materials: wet glistening skin, mucus, warts, pink tongue
always: wet; several in frame; gold eyes with horizontal pupils; the toads bigger than the frogs
never: one frog alone as a hero; cartoon eyes; smiling mouths; dry skin; wings; teeth
```
Panels: one "swarm on the stairs" plate (the main reference), one row of the six kinds at scale beside a hand, one toad face front, one frog mid-leap, one tongue-lash. References: Felipe's clay and 3D frogs; scraped poison-dart frog and cane toad photos for skin.

## Realistic 3D counterparts
`cast_mesh` one frog (blue dart) and one toad from the print photos (`IMG_8246` to `8249`); on the stage, instance them with `scene_place` along the stairs, on the barrels and over the corridor floor as the build photos show and the action maps move them (blue arrows = their movement), so the clay blocking clips carry the swarm's flow and the real clips follow it.
