# THE THREE AMBIANCES, ONE PLACE
### How the storeroom, the corridor and the roofless hall are one dungeon, and what Seedance is told about each scene as a whole

This file gives Seedance 2.5 (and the frame model before it) the world in three sizes: the whole place in one paragraph, each scene as a whole with its ambiance, tone and dialogue manner, and the seams between them. The master prompt tells Hephaestus to put the **WORLD block** and the **SCENE block** at the head of every clip prompt for that scene, before the shot's own action, so the model carries the mood, the sound and the way people speak even on a four-second shot.

---

## WORLD block (paste at the head of every clip prompt, after LOOK)
> WORLD: one abandoned dungeon under a fallen castle, cold and wet, climbing from a deep storeroom up a staircase, along a corridor and out into the castle's roofless hall under the sky. The same dark grey ashlar runs through every wall; the same water runs down it and gathers on every floor; the same smell of a dead pond grows stronger the further the party goes, until in the courtyard it has a shape. The light goes from one amber lantern in black, to lantern and green flame in a long wet corridor with grey light at its end, to starlight, green flame and rain in the open. The frogs, the rising water and the smell all run from the same thing: the worm under the courtyard mud. The tone is grounded fantasy adventure with dry humour: seven tired professionals bickering while doing something very dangerous very well. Dialogue is natural, overlapping, half-heard under the action, never shouted at the camera. Sound is wet: drips, splashes, slaps, rain.

---

## SCENE 1 block: the storeroom (15 s)
> SCENE 1, THE STOREROOM: deep underground, a vaulted cellar of crates, barrels and sacks lit only by the amber lantern hanging from the dwarf's axe and one torch beside a wet stone staircase that climbs along the right wall into a dark doorway. The air is still and cold; water drips with a long echo. The party has stopped to rest and divide the last of the food, tired, low on supplies, talking in low voices with the ease of people who have fought together for a long time. The mood is weary and dry-humoured until the sound of wet chirping grows in the dark doorway above the stairs, dozens of gold eyes open there, and the barrels at the other side of the room begin to rock; then it snaps to alert in one breath. Everyone speaks quietly here except the dwarf; the leader's commands are two words.
**Dialogue manner:** low, tired, teasing; Borrin half-singing; the first alarm is Mordecai's quiet "Company." and Vel's "Lantern up. Line." Every line is heard under the echo of the room.
**Sound:** drips, torch hiss, breathing, cloth; a wet chirping chorus rising above; then slaps of frogs on stone and the first steel.
**Seam into scene 2:** caught between the stairs and the barrels, the party fights its way UP the staircase through the frogs and into the corridor; the lantern goes with them, so the storeroom goes dark behind them as the frogs fill it. The last frame of 1C (the party climbing the stairs, frogs around their boots) is the first frame of 2A.

## SCENE 2 block: the corridor (15 s)
> SCENE 2, THE CORRIDOR: a long barrel-vaulted passage ankle-deep in water that begins at the top of the storeroom's stairs, the dwarf's lantern bobbing at the front and the necromancer's green fire at the back throwing two colours of light on weeping walls, an open archway at the far end with cold grey light beyond it. The party advances toward that archway in a loose line, killing frogs and toads that fill the floor and the walls and hang from the chains; the fight is loud, quick and almost cheerful, with the barbarians counting kills and jumps, the priest's water doing nothing, and the two rivals keeping score. Toward the end the frogs thin and run past the party rather than at them, and the leader stops, reads it, and the mood turns cold and quiet.
**Dialogue manner:** fast, overlapping, competitive and funny while fighting: counts shouted ("Eleven." "Nine."), Dax's "Seven!", Oswin's "They're AMPHIBIANS"; then in 2C quiet and clipped: Vel's "They're not attacking. They're running." and Borrin's "Told you. Pond."
**Sound:** the frog chorus very close and echoing, splashing feet, steel, the acid hiss and a green-white flash, water running; at the end the chorus fading down the passage and a cold wind from the far doorway.
**Seam into scene 3:** Vel walks to the archway and steps through it into grey light; the lantern follows; the camera does not cut inside the move. The last frame of 2C (Vel's silhouette in the archway against stars) is the first frame of 3A.

## SCENE 3 block: the roofless hall (30 s)
> SCENE 3, THE ROOFLESS HALL: the party steps out of the corridor into the great hall of the fallen castle, its roof long gone, under a cold, moonless, star-thick sky, high broken limestone walls on three sides, a stone bench with the last frogs on it, fallen blocks, and in the centre a mound of rubble sunk in black bubbling mud that reeks of death. The air is freezing and the sky is huge after the dungeon. The mud bulges; a gigantic earthworm coiled round the mound rears up screaming and the fight is the biggest of the film: mud, the barbarian woman flattened behind her shield, the elf caught inside the coil and healing from inside it without raising her voice, the leader's acid, the priest's wave, and halfway through the sky opens and cold rain falls in sheets, backlit green by the necromancer's flame. The half-githyanki jumps from the rubble onto the worm's head, drives his half sword in and slips; the coil loosens and the elf is pulled free; the worm screams with its mouth wide and the necromancer, arms raised wide, puts a beam of green fire down its throat. Then a smash cut: the seven of them, soaked and filthy, standing and sitting in the mud, looking up at the stars in silence, and the dwarf asks the question.
**Dialogue manner:** shouted over the scream and the rain, short and physical ("Collar!", "Dax, DOWN", "Now, bone-man!"); Mordecai alone speaks in full sentences and enjoys it; the final shot is silence, then one quiet, slightly drunk, utterly sincere question: "...is this all on Runware?"
**Sound:** wind, grass, bubbling mud, the lantern; the scream (wet, piercing, bubbling, with a sub-bass body); rain from a patter to a roar; one thunderclap on the kill; then only rain and breathing; then nothing under the last line.
**Seam out:** smash cut to black, the title.

---

## The seams in one line each (for `continuity` on the storyboard)
- 1C → 2A: `continuous`, carry the lantern, the frogs and the party's order up the stairs; the storeroom darkens behind.
- 2C → 3A: `continuous`, carry Vel's silhouette in the archway; the grey light becomes starlight.
- 3E → 3F: `smash-cut`, carry the rain and the mud; everything else stops.
- 3F → title: `fade-black` 1.5 s.

## Dialogue in the clip prompts
Seedance 2.5 makes sound and speech on the clip. Every shot prompt therefore carries its lines in quotes with the speaker's name and a delivery note (for example `BORRIN (slurred, cheerful): "I had the smaller half, lads."`), the way the shot lists write them. Hephaestus still records every line separately with `rw_audio` in the voice table's voices, so the cut can replace Seedance's speech on any shot where it drifts, and the same voice holds across all takes.
