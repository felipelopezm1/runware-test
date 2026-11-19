# CHARACTER 6: SERA'KITH VEL
### "Captain Vel". Githyanki. Swashbuckler rogue with an alchemist's purse. Leader of the party. The lead of the film.
Storyboard id `ch-vel`. Props `pr-needle`, `pr-acid-pots`.
**Print:** `Creative Task Runware/Script/Characters/Character 6/IMG_8237.HEIC` (front), `IMG_8238` (right), `IMG_8239` (back, the cloak fills the view), `IMG_8240` (left). The print shows a long cloak with the hood pushed back, a fitted cuirass, a belt with pouches, thigh boots, shoulder-length hair and a thin sword held point down at rest: that is her silhouette and her resting pose in every shot where she is not fighting.

## Who she is
**Class and background:** Rogue (Swashbuckler), with alchemy picked up on the Astral raids. Background: Soldier, a former raid captain who left her people and took this odd company with her.
**Personality:** cold, controlled, dry, decisive. She counts supplies, counts enemies, counts her pots. She trusts no door. She does not raise her voice because she has never needed to. Her one indulgence is the running argument with Mordecai over who is the strongest; she keeps score by kills and she cheats by counting assists.
**Wants:** to get everyone out alive and to be right about the thing that is wrong. **Fears:** losing control of the room.
**Voice:** low female contralto, clipped, precise, almost no breath. Sarcasm flat. Commands are two or three words.
**Signature gesture:** two fingers tapping the pouches at her belt, counting the pots.

## LOCK BLOCK (paste unchanged into every prompt)
> VEL: a githyanki woman, 1.85 m, long-limbed and lean, pale sage-green skin with a faint grey undertone, long pointed ears swept back, sharp cheekbones, yellow-amber irises, straight black hair cut to the shoulders with a blunt fringe, a thin white scar under the right eye. She wears a long cloak of waxed black leather with the hood pushed back, a fitted cuirass of blackened steel scales over a dark oxblood quilted doublet with a high collar, a wide belt hung with six small clay pouches each holding an acid pot stoppered with yellow wax that seeps a faint acid-green glow, fingerless black gloves, thigh-high black boots. Her weapon is NEEDLE: a silvered rapier with a swept hilt of blackened steel, held point down in her right hand at rest and level when she fights. Posture upright, chin level, movements economical.

## Weapons, in detail
- **NEEDLE**, the rapier: 1.1 m blade of bright silvered steel, hexagonal section, needle point; swept hilt of blackened steel in three loops, wire-bound black grip, round pommel. At rest, point down to the floor at her right side (the print's pose). Never a sabre, never a longsword, never glowing.
- **The acid pots**: six fist-sized unglazed red-clay pots stoppered with yellow beeswax, each in its own leather pouch on the belt, three each side. The acid glows faint acid-green through the clay. She throws with the left hand, underhand, from the hip. A hit: a hissing acid-green splash, white smoke, stone pitted. Count down: 6, 5 (shot 1C), 4 (2B), 3 (3B), 2 (3D).

## Facts for `sheet_build`
```
heightHeads: 8, build: lean, long-limbed, age: appears 30
palette: skin sage-green #9DB58A, hair black #0B0B0D, eyes amber #D9A13B, cloak and boots waxed black #121212, cuirass blackened steel #2B2D30, doublet oxblood #5A1E22, acid glow #B6FF3B, wax yellow #E3C341
materials: waxed leather, blackened steel scales, quilted wool, red clay, beeswax, silvered steel
marks: thin white scar under the right eye; pointed ears swept back; six pouches on the belt
always: the cloak with the hood DOWN; the swept black rapier hilt; the six belt pouches; shoulder-length hair with a fringe
never: the hood up; round ears; grey or blue skin; two swords; a glowing blade; a bandolier; a smile with teeth
```

## Sheet panels (Nano Banana Pro on Runware, `google:4@2`; references: the four print photos above)
Each panel prompt = LOOK block + LOCK BLOCK + the panel line, "on a plain mid-grey studio ground, even soft light, full sharpness, no shadow on the ground". Turnaround front, left, back, right (3:4; the back view is the cloak). Face front, three-quarter, profile (1:1). Expressions: neutral, cold amusement (one corner of the mouth), anger (eyes only), alarm, contempt, exhaustion. Hands. Prop: Needle's hilt in the right hand, close. Outfit main. Outfit weathered (rain-soaked cloak, venom smear across the cuirass, three pouches empty). Fantasy counterpart: full body, rapier level, lantern light from the left, black ground. Realistic 3D counterpart: `cast_mesh` Pixal3D from the four turnaround views, saved to `Character 6/3D Model Assets (Images)/`.

## How she moves and fights
Economical. Fences with small movements: parries by angle, lunges in a straight line, retreats one step at a time. Never flails. Throws pots underhand without looking. The cloak swings behind her and never tangles. In the worm fight she commands from the edge of the mud and enters it once (3D) to pull Sylwen out of the loosening coil.

## Arc across the scenes
- Scene 1: stands apart by the crates, counting rations in a pouch; first on her feet when the frogs come; first order: "Lantern up. Line." Her print stands centre of the circle in `Scene 1/IMG_8086` to `8088`.
- Scene 2: at the front beside Borrin (`Scene 2/IMG_8123` to `8126`; her kills are the red arrows in `Scene 2 Actions/IMG_0339`); a pot thrown down the corridor lights it green; stops the party and reads the frogs. Her line closes the scene.
- Scene 3: calls the ground; runs the fight; pulls Sylwen out; takes Mordecai's kill with a flat "assist". Final shot: looks at the sky, says nothing, then one dry look at Borrin.
