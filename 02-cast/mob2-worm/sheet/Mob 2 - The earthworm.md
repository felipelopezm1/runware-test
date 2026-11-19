# MOB 2: THE EARTHWORM
### Gigantic. Screams. Soggy, slick, caked in mud, risen from a patch that reeks of death.
Storyboard id `ch-mob-worm`. Scene 3 only.
**Print:** `Creative Task Runware/Script/Characters/Mob 2/IMG_8253.HEIC` to `IMG_8262.HEIC`: a long articulated segmented body of about forty rings with a flared head, photographed coiled, arched and in an S. The print is the worm's stand-in: its big round "eye" marks the mouth end (the worm is blind), its flared cowl is the swollen collar, and the loose crescent plates it sheds are the skin the worm sloughs. In the Scene 3 build it is coiled twice around the rubble mound with its head raised (`Scenes/Scene 3/IMG_8141` to `8143`, `8146` to `8165`).

## What it is
A worm the size of a siege engine that has lived under the fallen castle for longer than the castle stood, feeding on what falls into the mud. It is blind, it hunts by vibration and by the lantern's warmth, and it screams: a wet, piercing, bubbling shriek that is the loudest sound in the film. Every frog in the dungeon was running from it.

## LOCK BLOCK (paste unchanged into every prompt where it appears)
> THE WORM: a gigantic earthworm, 15 m long and 2 m thick, coiled around and rising from a mound of rubble sunk in black mud. Its skin is translucent pink-grey-brown with pale segment rings every half metre, slick with mucus, caked with black mud and clotted dirt, with pale pulsing veins visible under the skin, a thick swollen collar one third along the body, and loose pale crescent plates of sloughed skin shedding off it onto the ground. Its head end is a blind rounded tip that peels open into a round mouth of ringed inner lips. It screams: a wet, piercing, bubbling shriek. The mud around it is black, wet, bubbling, strewn with old bones, broken barrels and rotten cloth, steaming in the cold. It rears, slams, coils and sprays mud.

## Anatomy for the shots
- **The head**: blind, rounded, the skin thinnest and most translucent here; it peels open in four lips into a round mouth 1.5 m across lined with rings of pale ridges going inward into black. It opens fully only when it screams (3B, 3E), which is Mordecai's window.
- **The collar** (clitellum): a swollen pale band 2 m wide one third of the way along, thicker skin, where Vessa grapples (3C).
- **The body**: segments every half metre, each ring a shallow groove; mud and mucus slide off in sheets when it moves; the rain (3D on) makes it shine and steam.
- **The mud patch**: 20 m across, black, bubbling where the body moves under it, bones and rotten cloth turning over, a haze of stink in the cold air. The worm never fully leaves it: 6 to 8 m of body rears up, the rest stays under.

## Behaviour per shot
- **3A**: the coil round the mound heaves under the mud; a ripple crosses the patch toward the lantern; the frogs scatter toward it.
- **3B**: it rears straight up out of the coil, a column of mud, the first scream, the mouth opening at the top of the rise.
- **3C**: the coil sweeps the ground: Vessa goes flat behind her shield, Sylwen is caught in the loop to the waist; Oswin's wave hits the flank.
- **3D**: it sees Dax; he jumps onto its head and drives the half blade in; the rain begins; it writhes and the coil loosens; Vel pulls Sylwen out.
- **3E**: the second scream, the mouth wide, Mordecai's green beam from both hands into the mouth, the body spasms and falls across the mound.
- **3F**: dead, slumped over the rubble; the mud still, steaming, the party looking up.

## Sound
A wet bubbling shriek with a sub-bass body under it; mud sucking and slapping; the hiss of rain on hot skin. (`rw_audio` Mirelo SFX for the scream; Seedance's own audio for the rest where good.)

## Facts for `sheet_build`
```
build: 15 m long, 2 m thick, a third above ground at most
palette: skin pink-grey-brown #A88A7C, translucent pink #D9A9A0, veins #B8707A, collar pale #D8C9B8, mud black #141210, bones #E6DCC3, mouth interior #2A1518, mucus sheen #F2EFEA
materials: translucent slick skin, mucus, wet black mud, old bone, rotten cloth
always: segmented rings; the swollen collar; mud and mucus running off it; part of the body still under the mud
never: teeth; eyes; a face; tentacles; a dry worm; a sandworm's beak; it fully out of the ground
```
Panels: a head plate with the mouth closed, the mouth open and screaming, the collar close with Vessa for scale, a full-body side view with a 1.8 m figure beside it, the mud patch alone. References: Felipe's clay and 3D worm; scraped earthworm macro photos for skin and mucus, a fresh mud bank for the patch.

## Realistic 3D counterpart
`cast_mesh` the head and the first 5 m from the print photos (`IMG_8253`, `8256`); on the stage, `scene_place` it in the roofless hall as a spline coiled twice round the rubble mound with the head on top (match `Scene 3/IMG_8141`), so `scene_block` can rear it along the arrows of `Scene 3 Actions/IMG_0331` and `IMG_0332`. Model the open mouth as a second head mesh and swap it in for 3B and 3E.
