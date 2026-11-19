# CHARACTER 2: BORRIN HOLLOWCASK
### Dwarf. Small, brown-bearded, half drunk, always in front with the light. The party's lantern and the party's mouth.
Storyboard id `ch-borrin`. Props `pr-axe`, `pr-lantern`, `pr-flask`.
**Print:** `Creative Task Runware/Script/Characters/Character 2/IMG_8220.HEIC` (front), `IMG_8221` (right, axe head to camera), `IMG_8222` (back), `IMG_8223` (left). The print: the shortest figure, a conical helmet with a nasal bar, a beard in two braids to the belt, heavy pauldrons, a scale tunic with a scalloped skirt, a long-hafted axe held upright in the right hand with its butt on the ground, the left hand on the hip.

## Who he is
**Class and background:** Fighter (Battle Master), who insists he is "the scout". Background: Guild Artisan, a brewer whose brewery burned. He carries the light because he is the only one who never worries about what it shows.
**Personality:** cheerful, fearless because mildly pickled, loud, generous with his flask, calls everyone "lads" regardless, sings half of songs, and is sharper than he lets on: he smells the dead pond before anyone and says so in a joke nobody takes seriously. He gets the last line of the film.
**Wants:** a drink, a fire, a story worth telling. **Fears:** the dark when the lantern goes out.
**Voice:** thick gravelly tenor, slightly slurred, hiccups, trails off, sings half a line.
**Signature gesture:** raises the axe (and its lantern) and the flask together as a toast.

## LOCK BLOCK (paste unchanged into every prompt)
> BORRIN: a dwarf man, 1.30 m, barrel-chested and broad, ruddy weathered skin, a red bulbous nose, hazel eyes, a thick chestnut-brown beard in two long braids reaching his belt, each ending in a copper ring, chestnut hair showing under a conical steel helmet with a nasal bar. He wears heavy rounded steel pauldrons, a tunic of riveted steel scales with a scalloped skirt over a stained olive gambeson, a wide belt with a dented pewter flask on the right hip, heavy boots. In his right hand, butt on the ground, he holds a long-hafted bearded axe taller than himself with a knotwork relief on the blade, and from an iron hook just under the axe head hangs the LANTERN: an iron hooded lantern with a warm amber flame behind soot-smoked glass, the brightest light in the frame. His left hand rests on his hip or holds the flask. He walks in front, swaying slightly, cheerful.

## Weapons and props, in detail
- **The axe**: 1.5 m ash haft, a steel head with a long "beard" and a knotwork relief; held upright at rest (the print's pose), swung low and hooking in a fight. RIGHT hand.
- **The LANTERN**: a black iron hooded lantern, 30 cm, hung by a short chain from an iron hook under the axe head, so wherever the axe goes the light goes. Key light of scenes 1 and 2, a fill in scene 3 until the rain guts it (3D onward: a small struggling flame; 3F: an ember).
- **The flask**: dented pewter, right hip, in the LEFT hand when raised (1A, 2B, 3F).
- **The helmet**: conical steel with a nasal bar; never off.

## Facts for `sheet_build`
```
heightHeads: 5, build: barrel-chested, short-legged, age: about 140 (looks a weathered 50)
palette: skin ruddy #C98B6B, nose red #B9503F, beard and hair chestnut #6B3E1E, eyes hazel #8A7A3A, helmet and scales steel #7A7D82, gambeson olive #5B5A36, copper rings #B87333, lantern iron #1F1F1F, flame amber #FFB347, pewter #9A9A96
materials: riveted steel scales, steel plate, stained quilted linen, leather, pewter, soot-smoked glass, ash wood
marks: two beard braids to the belt with copper rings; bulbous red nose; the nasal-bar helmet
always: the lantern hanging under the axe head, lit; axe in the RIGHT hand; the helmet on; the flask on the right hip
never: a hood; a short beard; a hand-held lantern on a pole; a torch; a two-handed hammer; sober posture
```

## Sheet panels
Turnaround, faces (the helmet on, the nasal bar), expressions: cheer, hiccup (eyes shut), alarm (axe and lantern raised), sniffing the air, the toast, deadpan (the last line). Hands. Prop: the axe head with the lantern hanging, close, lit. Outfit main. Outfit weathered (beard wet, scales muddy, flame guttering). Fantasy counterpart: the lantern on the axe lighting the stairs as the frogs come. Realistic 3D: `cast_mesh`; axe with lantern as one separate mesh, the flame as an emissive sphere on the stage; saved to `Character 2/3D Model Assets (Images)/`.

## How he moves and fights
Front of the line, a rolling sway, axe and lantern up. Chops low and fast; in `Scene 2 Actions/IMG_0334`, `0336` and `0339` the red crosses around his feet are his kills, a dozen of them; he wades through the frogs (`Scene 2/IMG_8126`). Head-butts a toad once with the helmet (2B). In scene 3 he stays at the mud's edge keeping the light on the worm, which is the bravest thing in the film and he does it swaying.

## Arc across the scenes
- Scene 1: by the foot of the stairs (`Scene 1/IMG_8086`), arguing with Vessa over the bread, flask in hand: "I had the smaller half, lads. I measured." Sniffs the air at the barrels: "Smells like a pond. A dead pond." Nobody listens; the green strokes at his head in `Scene 1 Actions/IMG_0348` and `0358` are him hearing it first.
- Scene 2: leads down the corridor (`Scene 2 Actions/IMG_0333`); the toast to a dead toad; "Told you. Pond."
- Scene 3: holds the light. In the smash cut, flask raised to the stars: "...is this all on Runware?"
