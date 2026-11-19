# Runware facts for "Is this all on Runware?"

Quartermaster, 2026-11-19, 10:04 to 10:22 UTC. Nothing was generated and nothing was spent: the account's balance is 215.7715 USD before and after (`rw_account`, tool answer, about 10:11 UTC; requests today 0).

Every price is marked `listed` (a Runware page, a model's schema or our own catalogue) or `charged` (a real bill in our records). Where two sources disagree, both are shown.

## Sources

| short name | what it is |
| --- | --- |
| S25 | `https://runware.ai/docs/models/bytedance-seedance-2-5/schema.json`, fetched 10:04 UTC (the same file the arm reads and caches for a week) |
| S25-page | `https://runware.ai/docs/models/bytedance-seedance-2-5.md` |
| NBP | `https://runware.ai/docs/models/google-nano-banana-pro/schema.json` |
| ARM | `/home/felipe-lopez/.config/Hephaestus/runtime-overlay/80a85aade4ab/runtime/runware.mjs` |
| CAT | `/home/felipe-lopez/.config/Hephaestus/runtime-overlay/80a85aade4ab/runtime/runware-catalog.mjs` |
| FAL | `/home/felipe-lopez/.config/Hephaestus/runtime-overlay/80a85aade4ab/runtime/fal-catalog.mjs` |
| APP | the private app's code, `/home/felipe-lopez/titanium/.hephaestus/irons/runware-hephaestus-control` (`src/lib/runware/catalog.mjs`, `src/app/api/runware/run/route.ts`, `scripts/heph.mjs`); `origin/runware` is at the same commit, 8cba21d |
| LEDGER | `/home/felipe-lopez/titanium/.hephaestus/arm-spend.jsonl`: every charge Runware reported to the `rw_*` tools, 23 lines, 2026-11-09 to 2026-11-11 |
| ZT | the zombie test's records: `/home/felipe-lopez/Desktop/test 2/making-of-parts/index.html` (its Costs table) and the session reports in `/home/felipe-lopez/titanium/.hephaestus/chats/general.jsonl`, 2026-11-11 18:17 to 18:51 UTC |
| offline run | the arm's own request builders (CAT is pure: no network, no key) run against S25 and NBP in a scratch folder, to see exactly what `rw_video` and `rw_image` would send |

## The answers that decide the route

1. **4K is in Seedance 2.5's schema today, at $0.921 a second, but we have never been charged for one.** The zombie test was made at 1080p and upscaled.
2. **A start frame and references cannot go in the same Seedance 2.5 call.** The plan (master prompt step 8, bible section 3) asks for the approved frame as first frame, the face panels as references and the clay clip as a video reference together. Runware refuses that combination. Each shot must be one or the other: frame mode (frame, optional last frame, nothing else but audio references) or reference mode (up to 30 pictures and up to 10 clips, no locked first frame).
3. **No assembled prompt fits our `rw_video` or `rw_image` tools.** The twelve prompts measure 6,875 to 12,812 characters; the tools stop at 3,000. The models themselves take 50,000 (Seedance 2.5) and 45,000 (Nano Banana Pro).
4. **The clay clip can ride as a video reference on Runware, but not through `rw_video`,** which has no field for it. The zombie test went round the tool with a raw task through the Titanium app's run route.
5. **The fall-back to fal that step 8 names is a poor one**: fal's arm cuts the prompt at 2,450 characters, fal has no 4K for this model, it costs about 1.9 times more, and fal's Seedance refused the zombie test's character twice for likeness.

---

## 1. Seedance 2.5 on Runware (`bytedance:seedance@2.5`)

Status live, released 2026-08-07 (S25 `info`).

| what | answer | source |
| --- | --- | --- |
| resolutions | `480p`, `720p`, `1080p`, `4k` (lower-case k), default `720p`; as width and height the 16:9 pairs are 854x480, 1280x720, 1920x1080 and **3840x2160** | S25 `properties.resolution.enum` and the last rule of `allOf` |
| durations | any whole number of seconds from 4 to 30, or `"auto"`; default 5. An edit of a clip takes only `"auto"` | S25 `properties.duration` |
| frame rate | no parameter. Measured on our own outputs: 24 fps, H.264 with AAC stereo at 32 kHz. A 10 s ask came back 10.08 s, a 5 s ask 5.04 s (a frame or two more than asked) | ZT (ffprobe of task e4f1df3a), `charged` clips |
| aspect ratios | 16:9, 4:3, 1:1, 3:4, 9:16 and 21:9 at every tier, as fixed width and height pairs. With a start frame or a source clip, width and height are refused: only `resolution` goes, and the shape follows the frame | S25 `allOf`; S25-page "Compatibility & Validation" |
| `frameImages` | at most 2: first, or first and last (a last frame alone is refused). **Not with `referenceImages`, `referenceVideos` or `video`.** With `referenceAudios` it is allowed | S25 `inputs.frameImages` (maxItems 2, `contains`), `allOf[1]`, `info.x-modes`; S25-page: "Inside `inputs`, `frameImages` cannot be used with `referenceImages`, `referenceVideos`, or `video`" |
| `referenceImages` | at most **30**; each up to 30 MB, 300 to 6000 px a side, ratio 0.4 to 2.5 | S25 `inputs.referenceImages.maxItems`, `x-constraints` |
| `referenceVideos` | at most **10**, "used as visual guidance for a new video"; each 2 to 30 s, 30 s in all, up to 200 MB, 300 to 6000 px a side. **Yes: a clay blocking clip can ride as a video reference**, in reference mode only | S25 `inputs.referenceVideos`, `x-constraints` |
| `referenceAudios` | at most 10; each 2 to 30 s, 30 s in all, up to 15 MB | S25 `inputs.referenceAudios`, `x-constraints` |
| source clip | `inputs.video` edits or extends a clip (`settings.operation` `edit` or `extend`) | S25 |
| native sound | `settings.audio`, on by default; no separate price | S25 `properties.settings`; see prices below |
| `seed` | yes, 0 to 2147483647; the answer says the seed used | S25 `properties.seed`; ZT (seed 2113674798 came back) |
| longest prompt | **50,000 characters** (at least 2) | S25 `properties.positivePrompt.maxLength` |
| negative prompt | none: the schema has no `negativePrompt` | S25 (the bible already says so, section 1) |
| how references are named in the prompt | "Reference assets in array order as `@Image1`, `@Video1`, and `@Audio1`, numbered from one" | S25 `properties.positivePrompt.description` |
| takes per call | `numberResults` 1 to 4 | S25 |
| draft mode | `settings.draft: true` makes a quick 480p preview and answers `outputs.draftId`; a second call with `inputs.draftId` alone renders that same preview at `1080p` or `4k` | S25 `settings.draft`, `inputs.draftId`, `ResponseBody` |

### Is 4K really there? Two sources against one

- For: the schema's `resolution` list has `4k`, its size table has "4K (16:9) 3840x2160", and its price list has 4K rates (S25; the page shows the same).
- Against, on the same page: the Notes prose still says "`resolution` (`480p`, `720p`)" and "at either resolution" (S25-page, "Notes"), and the schema's price overview prices only 480p, 720p and 1080p tokens. Both read like text written before 4K was added.
- Against, in our own records: on 2026-11-11 the session that made the zombie test wrote "Seedance 2.5 goes no higher than 1080p on either Runware or fal" and upscaled with Topaz (ZT). The Titanium app's catalogue lists 480p to 1080p only (APP `catalog.mjs` lines 1092 to 1096).
- Verdict: `listed`, not `charged`. Nothing on our account proves a 4K Seedance clip. The first paid 4K take is the proof. A request Runware rejects is not billed (ZT: the rejected Kling call "fails without a charge").

### Prices (per second of output, `listed`, S25 `info.x-pricing.rates`)

| | 480p | 720p | 1080p | 4K |
| --- | --- | --- | --- | --- |
| from words, a frame or reference pictures | $0.1025 | $0.2304 | $0.61354 | $0.92129 |
| with a clip as input ("video-to-video") | $0.1313 | $0.2953 | $0.73415 | $1.13692 |

**With and without sound the price is the same.** There is no audio rate in the schema, and our three charged clips, all with sound on, paid exactly the plain rate.

`charged`, all three at 1080p with sound on (ZT):

| clip | request | charged | per second |
| --- | --- | --- | --- |
| eye opener, task 7a75d470 | reference mode, 3 pictures, 1920x1080, 5 s | $3.06771 | $0.6135 |
| one-take, task e4f1df3a | reference mode, 5 pictures, 1920x1080, 10 s | $6.110073 | $0.6110 |
| edit of the 9 s first cut, task d798cd8a | `inputs.video` (9 s) with 2 pictures, `1080p`, duration auto, 8.71 s back | $6.45 as the session reported it (the whole pass was $6.77728 with Topaz $0.17 and Mirelo $0.16) | $0.74 of output |

How the bill is worked out (inferred from those three charges, which it reproduces to the cent, and from the schema's overview line "$12.52/M Token ... at 1080p; $7.49/M Token for Video-to-Video at 1080p"):

- without a clip as input: width x height x (24 x seconds + 1) / 1024 tokens, at $12.52 a million at 1080p. Reference pictures cost nothing extra.
- with a clip as input: the same count over the input clip's frames plus the output's frames, at $7.49 a million. So **a video reference is billed by its own length too**: a 5 s clay clip on a 5 s shot is where the listed $0.734 a second comes from; a longer clay clip costs more. This rests on one charged edit, not on a `referenceVideos` call, so treat it as inferred.
- at 4K the listed rates work out to $4.70 and $2.90 a million tokens. A take costs: 4 s $3.69, 5 s $4.61, 6 s $5.52; with a clay clip of the same length $4.56, $5.68, $6.81.

### Through our own tools

`bytedance:seedance@2.5` is **not in the arm's catalogue** (CAT lines 58 to 67 list eight video models; the only Seedance is 2.0 Fast). It passes as a bare AIR, and the arm then reads S25 from Runware's docs (ARM lines 241 to 283). What `rw_video` does with it, from the source and the offline run:

| ask of `rw_video` | what is sent | result |
| --- | --- | --- |
| a prompt over 3,000 characters | nothing: the tool's own check refuses it (ARM line 677) | refused before sending |
| start frame, `size: "4k"`, no `aspectRatio` | `frameImages` and `resolution: "4k"` | valid |
| start frame, `size: "4K"` with `aspectRatio: "16:9"` | `frameImages` with `width` 3840 and `height` 2160 | Runware refuses (width and height with a frame); the arm does not catch it |
| `size: "4K"` (capital K), no aspect | `width` 2880, `height` 2880: a **square** 4K clip | valid and wrong; the preset match is case-sensitive (CAT line 193) |
| references only, `aspectRatio: "16:9"`, `size: "4K"` | `referenceImages` with 3840x2160 | valid |
| start frame and references together | both lists | Runware refuses; the arm does not catch it |
| more than 10 references | the tool refuses 11 or more (ARM line 681); the builder would cut to 10 anyway (CAT line 292) | 10 at most |
| a clay clip, a reference recording, a draft id | no such fields exist on `rw_video` | cannot be sent |
| `negative` | `negativePrompt` | the arm refuses it: the schema lists no such parameter |
| the quote | "price known after the call" with the schema's token line: the arm has no rate for this model (CAT line 418) | the quote must come from this memo |

The arm's rule "a parameter the model's schema does not list is refused before anything is sent" checks parameter names only (CAT lines 572 to 579). It does not read the schema's rules about which inputs go together.

## 2. Nano Banana Pro on Runware (`google:4@2`)

| what | answer | source |
| --- | --- | --- |
| reference pictures | at most **14** | NBP `inputs.referenceImages.maxItems`; CAT line 51 says the same |
| sizes | `1K`, `2K`, `4K`. At 16:9: 1376x768, 2752x1536, 5504x3072. `resolution` goes only with references and takes its shape from them; width and height go either way | NBP `properties.resolution`, `allOf` |
| longest prompt | **45,000 characters** (at least 3) | NBP `properties.positivePrompt.maxLength` |
| a second text channel | `settings.systemPrompt`, up to 50,000 characters | NBP `properties.settings` |
| seed | yes | NBP |
| price by size, `listed` | 1K $0.138, 2K $0.138, 4K $0.244 an image | NBP `info.x-pricing.rates` |
| price, `charged` | $0.1413 to $0.1435 an image, seven images at 2752x1536 with references on 2026-11-11 (mean $0.1427); $0.277 for two on 2026-11-10 | LEDGER; ZT Costs table |

Through `rw_image`: the prompt stops at 3,000 characters (ARM line 611). The tool lets 16 references in (ARM line 625) but the builder silently keeps the first 14 (CAT line 240). `aspectRatio: "16:9"` with `size: "2K"` sends 2752x1536, with `"4K"` 5504x3072; the estimate says $0.138 whatever the size, so a 4K picture is under-quoted (offline run). `settings` passes through as given, so `settings.systemPrompt` can be sent today (offline run: accepted, 11,000 characters).

Note: 2752x1536 is 1.792 to 1, not exactly 16:9 (1.778). A Seedance clip started from such a frame takes its shape from the frame, and we have no record of what size comes back. Check the first clip with `cut_probe`.

## 3. The prompt-length problem, measured

Method: each prompt assembled exactly as "How a clip prompt is assembled" says (Scene 1 shot list, lines 5 to 11): LOOK, WORLD, the SCENE block, the location block, the LOCK BLOCK of every character in the shot's cast column followed by its state line and its tags (`VEL ([Image4], [Image11])`), the mob blocks, the rain line from 3D on, the SHOT body verbatim, the hold line; blocks joined by a blank line. Texts read from the bible, the three shot lists and `00 - The three ambiances, one place.md`. All of it is plain ASCII, so characters and bytes are equal.

The pieces: LOOK 486, WORLD 958, SCENE blocks 801 / 760 / 1,234, location blocks 788 / 625 / 965, hold line 214. LOCK BLOCKS: Vel 824, Mordecai 842, Vessa 842, Dax 771, Borrin 871, Sylwen 702, Oswin 829 (5,681 for the seven); frogs 665, worm 739. SHOT bodies run 997 to 1,772.

| shot | cast (people + mobs) | characters | times the tools' 3,000 |
| --- | --- | --- | --- |
| 1A | 7 + 0 | 10,899 | 3.6 |
| 1B | 3 + 0 | 6,875 | 2.3 |
| 1C | 4 + 1 | 9,378 (11,125 with Dax and Oswin, whom the body also names) | 3.1 |
| 2A | 7 + 1 | 11,437 | 3.8 |
| 2B | 4 + 1 | 8,627 | 2.9 |
| 2C | 7 + 1 | 11,203 | 3.7 |
| **3A** | 7 + 2 | **12,812** (the heaviest: all seven, the frogs and the worm) | 4.3 |
| 3B | 3 + 1 | 8,851 | 3.0 |
| 3C | 3 + 1 | 8,605 | 2.9 |
| 3D | 4 + 1 | 9,616 | 3.2 |
| 3E | 4 + 1 | 9,690 | 3.2 |
| 3F | 7 + 1 | 12,065 | 4.0 |

In scene 3 the head alone (LOOK, WORLD, SCENE 3 and the location block, before any character) is 3,649 characters: over the tools' limit with no LOCK BLOCK and no shot in it.

**Does it fit?**

- (a) The model's own limit on Runware: **yes.** 12,812 is a quarter of Seedance 2.5's 50,000 and under a third of Nano Banana Pro's 45,000. For scale: Runware's own six published examples for this model use prompts of 1,105 to 1,886 characters, and the zombie test's two were 1,604 and 1,818. Nothing in our records shows how Seedance holds a 12,000-character prompt.
- (b) Our `rw_video` and `rw_image` tools: **no, not one of the twelve.** Both stop at 3,000 characters (ARM lines 677 and 611). The limit is the tools' own, not Runware's.
- (c) The private app (`heph.mjs`, `/api/runware/run`):
  - `kind: "video"`: **no.** The route builds its own prompt and cuts it at 2,450 characters without saying so (APP `catalog.mjs` lines 1646 and 1742). It also has no 4K tier for this model and sends a clip only as an edit, never as a reference.
  - `kind: "image"`: the prompt is cut at 8,000 characters without saying so (APP `catalog.mjs` line 860; `brief.ts` line 194); a system text up to 20,000 rides beside it (line 877). The whole prompt as one text does not fit.
  - `kind: "raw"`: **yes.** The task goes as the caller built it (APP `route.ts` lines 45 to 61): the whole prompt, `resolution: "4k"`, 30 reference pictures, `referenceVideos`, `referenceAudios`, a draft id. This is the route the zombie test used for Seedance and for Topaz.

**The routes that carry the prompt whole, and what each costs.** None of them shortens a LOCK BLOCK.

| route | carries | what it costs |
| --- | --- | --- |
| A. A raw task through the private app (`heph.mjs run` with `kind: "raw"`) | everything, today, with no code change | Every input must first be a file Runware can fetch: uploaded through the app (4.2 MB a file on Vercel) or in the Blob store. The app's setup notes give it a ceiling of $25 a day (`TITANIUM_DAILY_CAP_USD=25`, APP `docs/runware/hephaestus.md`), which the 4K takes of scene 3 alone can pass. Its own price for this model is the 480p from-price ($0.102 a second, `heph price`, tool answer), so the quote has to be ours. The arm's quote, hold and spend ledger do not see the call: the log must record the charge itself. The local copy on port 3100 is down now; the Vercel copy answers ready |
| B. Change the arm | everything, with the arm's own quote, hold and ledger | A change to the forge's runtime by its owner, tested before the film: raise `ask` to the schema's `maxLength` in `rw_video` and `rw_image` (ARM lines 611, 677); give Seedance 2.5 a catalogue entry with its rates and 30 references (ARM line 681, CAT line 292); add `referenceVideos`, `referenceAudios`, `video`, `draftId` to `rw_video`; match the preset without case and send `resolution` when a frame is given (CAT line 193); refuse a frame with references before sending; give `rw_upscale` a width and height for Topaz (CAT line 301) |
| C. Runware's own CLI or MCP `run` | everything | Both are held from every quest by design (arm README): only the owner can run them, by hand, one call at a time |
| D. For pictures only: the fixed blocks in `settings.systemPrompt`, the shot in `ask` | LOOK, WORLD, SCENE, location and every LOCK BLOCK unchanged, up to 50,000 characters, through `rw_image` as it is today | The blocks are then in the system text and not in the prompt field. Whether that meets "pasted unchanged into every prompt" is the owner's call, and whether Nano Banana Pro weighs the system text like the prompt is untested. Seedance has no such field, so this does nothing for clips |
| E. fal (`fal_video`, `seedance-25`) | no | fal's arm cuts the built prompt at 2,450 characters (FAL line 1698); 1080p at most; $1.164 a second there (FAL line 840) against $0.614 here; refused the zombie test's character twice for likeness (ZT) |

## 4. The reference-count problem

The bible's binding for a seven-character shot with both mobs and the five props: the frame, the clay frame, the plate, 7 face panels, 7 turnarounds, 2 mob sheets, 5 props: **24 pictures**, `[Image1]` to `[Image24]`, plus the clay clip.

| where | limit | what fits for seven characters |
| --- | --- | --- |
| Seedance 2.5 on Runware, reference mode | 30 pictures, 10 clips, 10 recordings (S25) | **All 24 and the clay clip fit.** But then there is no locked first frame: the approved frame is `@Image1`, a reference |
| Seedance 2.5 on Runware, frame mode | the frame, a last frame, recordings (S25) | **No reference pictures and no clay clip at all.** Identity rests on the frame and the words |
| `rw_video` as built | 10 pictures, no clip (ARM line 681) | for example the frame, the clay frame, the plate and the 7 faces: exactly 10. No turnarounds, mobs or props |
| the private app, raw task | the model's own limits | all 24 and the clip |
| Nano Banana Pro on Runware | 14 pictures (NBP) | **The bible's order does not fit**: without `[Image1]` it is 23, before the print photos it adds at the end. In 14: the clay frame, the plate, the 7 faces and 5 of the 7 turnarounds; or the clay frame, the plate, 7 faces, 2 mob sheets and 3 props; or, if each character's rendered sheet page goes as one picture, the clay frame, the plate, 7 sheet pages, 2 mob sheets and 3 props |
| `rw_image` as built | lets 16 in, sends the first 14 | the same 14, and the last two vanish without a word |

Two things follow from how Runware binds references:

- Tags follow the array's order, numbered from one. "Omit absent characters but keep the order of the rest" therefore moves the numbers from shot to shot, unless every call carries the full fixed set (24 fits Seedance's 30; it cannot fit Nano Banana Pro's 14).
- The schema writes the tag `@Image1`. The bible writes `[Image1]`. The zombie test's calls that held the character used `@Image1` (ZT). The app's catalogue writes `[Image1]` for Seedance (APP `catalog.mjs` line 1608). Which forms the model reads is not something our records settle; `@Image1` is the documented one.

## 5. The other paid tools

| tool, model | `listed` | `charged` | for this film |
| --- | --- | --- | --- |
| `rw_caption`, Qwen2.5-VL 7B (`runware:152@2`) | about $0.0013 a picture (CAT line 97); the schema measures $0.003 at 1024x1024 and shows $0.0013 to $0.0032 | $0.0019, $0.0025, $0.0025, $0.0037 on 2026-11-09 (LEDGER), mean $0.0027 | 170 pictures: $0.22 to $0.63 |
| `rw_audio`, MiniMax Speech 2.8 (`minimax:speech@2.8`) | $0.0001 a character HD, $0.00006 turbo; up to 50,000 characters; voices are a fixed list of names | never used here | all the lines once: about $0.12 |
| `rw_audio`, Fish S2.1 Pro (`fishaudio:s2.1@pro`) | $0.000015 a byte of text; up to 3,000 characters; clones one voice from a 1 to 90 s sample with its transcript | never used here | all the lines once: about $0.02 |
| `rw_audio`, Mirelo SFX 1.5 (`mirelo:1@1`) | **three prices**: $0.00025 a second (the schema's rate and CAT line 118); "$0.01/s" (the schema's overview, and `heph price`) | **$0.02 a second**: seven effects of 2 to 10 s at $0.04 to $0.20 (LEDGER; lengths by ffprobe) | 1 to 10 s an effect, so at most $0.20 each: 8 effects about $1.30 |
| `rw_audio`, ACE-Step v1.5 XL Turbo | $0.0009 for 60 s (CAT line 117); the schema measures $0.00225 | $0.0018 for 30 s (LEDGER) | 60 s: under a cent |
| Topaz Proteus video upscale (`topazlabs:proteus@4`) to 4K | measured $0.15 for a 4.8 s clip at 3840x2160 and 30 fps, $0.05 at 1080p (schema); the arm's rate, $0.0104 a second, is the 1080p one (CAT line 91) | $0.0856 for 5.04 s and $0.17 for 8.71 s, both 1080p to 4K at 24 fps (ZT) | a 60 s cut: $1.03 to $1.88, expected $1.18 |
| the same through `rw_upscale` | **cannot run**: Topaz's schema requires `width` and `height`, and the arm's clip upscale sends neither (CAT line 301; offline run). The zombie test sent it as a raw task | | use the app's route |
| ByteDance Video Upscaler through `rw_upscale` (the arm's default for a clip) | from $0.00265 a second at 720p | $0.3204 for 15.1 s, 3840x2160 out (LEDGER): $0.021 a second | works through the arm today; 60 s about $1.27 |
| `rw_upscale` pictures | Real-ESRGAN $0.0006 at 2x and $0.0013 at 4x from a 1 MP picture; SwinIR $0.0032; Clarity $0.005 to $0.007; Bria $0.018; Topaz Wonder 4 $0.0428 up to 8 MP of output, $0.0856 to 16 MP, $0.128 to 24 MP (schemas). The arm says Wonder 4 is $0.0428 "up to 4 MP" (CAT line 76): the schema says 8 | never used here | not in the plan |
| image to 3D, TRELLIS.2 (`microsoft:trellis-2@4b`), not in the `rw_*` tools | $0.019 to $0.052 a mesh (schema) | $0.018 to $0.021 a figure (ZT) | a Runware way to make the ten meshes without the GPU pod, through the app's `threed` route only |

## 6. How the zombie test was really made

Made 2026-11-11: "Not Hikers", 13.1 s, the final all on Seedance 2.5. Source: ZT throughout.

- **Model and route.** `bytedance:seedance@2.5` on Runware. Not through `rw_video` ("has no field for a clip") but as **raw tasks through the Titanium app's run route** (`https://titanium-runware.vercel.app/api/runware/run`), inputs uploaded through `/api/runware/upload` to Runware's storage, polled on `/api/runware/status`.
- **Resolution.** 1920x1080 from Seedance, 24 fps. The 4K masters are Topaz Proteus upscales, not native.
- **The three Seedance clips that were kept or used:**

| clip | inputs | prompt | charged |
| --- | --- | --- | --- |
| the edit (task d798cd8a) | the 9 s first cut as `inputs.video` (re-encoded to fit the 4.2 MB upload), 2 reference pictures (front and face sheets), `operation: edit`, `duration: auto`, `1080p`, sound on | 1,604 characters, with `@Video1`, `@Image1`, `@Image2` | $6.45, then Topaz $0.17 and Mirelo foley $0.16: $6.77728 in all |
| the eye opener (task 7a75d470) | 3 reference pictures, 1920x1080, 5 s, sound on | about the same shape | $3.06771, then Topaz $0.0856: $3.15331 |
| the one-take, the final (task e4f1df3a) | 5 reference pictures (face, sheet, three frames of the earlier pass), `width` 1920, `height` 1080, `duration` 10, sound on, seed 2113674798 | 1,818 characters, a timeline in seconds, `@Image1` to `@Image5` | $6.110073; $6.44 with foley and the 4K upscale |

- **Per clip, plainly:** $0.61 a second at 1080p from references, $0.74 a second of output when a clip went in. About $3.07 for 5 s and $6.11 for 10 s.
- **The Seedance work in all:** $16.37. The whole film about $18.75, an estimate that includes the Kling first cut and seven Nano Banana Pro frames.
- **What failed, and the way round:**
  - A frame with references was refused by the schema ("the fallback in the brief, first frame plus references, wasn't possible either"). Way round: references only, with the opening and ending frames sent as references and described in words.
  - Seedance slipped hard cuts into its takes: one at 5.75 s in the edit, one at 8.5 s in the 10 s take. Way round: the take was trimmed to 8.5 s.
  - fal's Seedance refused the character twice "for likeness of real people", once even from a back view, at no charge. Runware raised no such refusal on three calls.
  - `rw_upscale` could not send Topaz its width and height. Way round: a raw task.
  - `rw_video` with an aspect ratio sent Kling 3 a `width` it rejects; the call failed without a charge. Way round: leave the aspect out.
  - `rw_audio` foley on a clip failed once with `invalidEnum ... 'outputFormat' ... 'mp4', 'mov', 'webm'` (recipe R-504): a clip's foley comes back as a clip.
  - The upload route takes 4.2 MB a file, so the source clip was re-encoded at 3.3 Mb/s.
  - The browser project with the Stage's own depth, normal and guide clips was lost; the passes were made again from the clay frames with Runware's preprocessors ($0.0192 for 18).
- **What it did not test:** a start frame on Seedance (every Seedance call was reference mode or an edit), a clay clip as `referenceVideos`, 4K, more than 5 reference pictures, a prompt over 1,818 characters, spoken lines, more than one character's face.

## 7. The GPU pod

- `cloud_host` with action `status`, tried once more at 10:11 UTC: **"fetch failed"**, the same answer Hephaestus got earlier this morning (the day's web log, `brain/webs/2026-11-19.md`, shows "fetch failed" at 09:59, 10:00 and 10:02).
- `access_status`: the permission is held ("Cloud host: ready, through the cloud key and the hosted app"; the cloud token and the RunPod key are sealed). So the keys are there and the status read itself does not get through.
- `comfy_studio` with action `status`: "this computer: not running; GPU pod: not paired".
- So the pod's state could not be read; nothing here is paired with it, and it should be taken as asleep. It was not started, and `gpu_host` was not called. `cast_mesh` and the other GPU steps wait on it (about $0.89 an hour while awake, `listed` on the tool's card); the Blender stage's own tools (`scene_build`, `scene_block`, `scene_pass`, `scene_render`) run on this computer and do not.

## 8. The cost model

In `cost-model.md` beside this file.

## Caught on the way

- The pack's photos are HEIC and sit outside the project folder. The arm reads only PNG, JPEG, WebP and GIF, and only inside the project (ARM line 200; `imageType` in `fal.mjs`). The clerk's previews in `making-of/previews` (JPEG, 2048 px) are the files to send.
- The arm sends a local picture inline as base64. A 2K PNG from Nano Banana Pro weighs about 7.7 MB (our seven from 2026-11-11), so ten of them in one call is a body of about 100 MB. JPEG copies, or public addresses from `media_publish`, avoid that. Untested at that size.
- The master prompt's rule "quote and wait before any step over $5" bites on single takes at 4K: every 6 s take ($5.52) and every take of 5 s or more with a clay clip ($5.68 and up).
- `SCRIPT.md` holds 40 spoken lines (176 words, 933 characters) but its own table says 47 lines and 213 words.
- The Hindsight arm did not answer (port 7484); the zombie test's facts here come from the chat log, the ledger and the making-of page instead.
