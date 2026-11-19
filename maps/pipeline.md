# The pipeline, in Mermaid

GitHub renders these. The drawn versions are [`pipeline.svg`](pipeline.svg) and [`studio.svg`](studio.svg).

## From clay to cut

```mermaid
flowchart LR
  classDef hand fill:#1a0605,stroke:#d8261c,color:#e8e8e8
  classDef rw fill:#0b0b0b,stroke:#d8ff3d,color:#e8e8e8
  classDef free fill:#0b0b0b,stroke:#8a8a8a,color:#e8e8e8
  classDef rec fill:#0b0b0b,stroke:#9ec9ff,color:#e8e8e8

  subgraph hand[made by hand]
    minis[7 minis + 2 mobs<br/>photographed in turnaround]:::hand
    sets[3 clay sets<br/>photographed around]:::hand
    maps[action maps<br/>blue move, red attack, green react]:::hand
    script[script, shot lists,<br/>lock blocks, ambiances]:::hand
  end

  read[1 read + caption<br/>rw_caption, Qwen2.5-VL]:::rw
  refs[2 references<br/>scraper, open licences]:::free
  board[3 storyboard<br/>director, 16 takes]:::free
  sheets[4 character sheets<br/>rw_image, Nano Banana Pro]:::rw
  stage[5 meshes + Blender stages<br/>cast_mesh, scene_build, plates]:::free
  block[6 blocking<br/>scene_block, scene_pass: clay clip per shot]:::free
  frames[7 frames<br/>rw_image, Nano Banana Pro]:::rw
  clips[8 clips<br/>rw_video, Seedance 2.5 at 4K]:::rw
  sound[10 voices + sound<br/>rw_audio: MiniMax, Fish, Mirelo, ACE-Step]:::rw
  cut[11 cut + 12 title<br/>board_cut, cut_edit, title_render]:::free
  show[14 showcase<br/>post, website piece]:::free
  record[(the record<br/>log, screens, clips, recordings)]:::rec

  minis --> read
  sets --> read
  maps --> read
  script --> read
  read --> refs --> board --> sheets --> stage --> block --> frames --> clips --> cut --> show
  sheets -. face panels as references .-> frames
  sheets -. face panels as references .-> clips
  stage -. plates .-> frames
  block -. clay first frame = layout .-> frames
  frames -. approved frame = first frame .-> clips
  script -. assembled prompt, lock blocks verbatim .-> clips
  sound --> cut
  read & refs & board & sheets & stage & block & frames & clips & sound & cut -.-> record
```

## One shot, from the build photo to the pick

```mermaid
flowchart TB
  classDef hand fill:#1a0605,stroke:#d8261c,color:#e8e8e8
  classDef rw fill:#0b0b0b,stroke:#d8ff3d,color:#e8e8e8
  classDef free fill:#0b0b0b,stroke:#8a8a8a,color:#e8e8e8

  photo[build photo + action map]:::hand
  body[shot body from the shot list<br/>dialogue in quotes, delivery in parentheses]:::hand
  clay[clay blocking clip on the Blender stage<br/>locked camera and motion; first frame = layout]:::free
  panels[face-front + front-turnaround panels<br/>of every character in the shot]:::rw
  plate[location plate]:::rw
  prompt[assembled prompt<br/>LOOK · WORLD · SCENE · location · lock blocks with state lines and tags · body · hold line]:::free
  check[prompt_check]:::free
  frame[frame on Nano Banana Pro<br/>references: clay first frame, panels, plate]:::rw
  ok{approved on the board?}
  clip[clip on Seedance 2.5 at 4K<br/>first frame + panels as Image1..n + prompt verbatim<br/>the shot's exact length, 16:9, audio on]:::rw
  rate{rated: keep?}
  pick[pick.mp4 → 07-cut/picks]:::free

  photo --> clay
  body --> prompt
  clay --> frame
  panels --> frame
  plate --> frame
  prompt --> check --> frame
  frame --> ok
  ok -- no: reshoot from the same block --> frame
  ok -- yes --> clip
  panels --> clip
  prompt --> clip
  clip --> rate
  rate -- retake, same seed --> clip
  rate -- yes --> pick
```

## The agents

```mermaid
flowchart LR
  classDef lead fill:#1a0605,stroke:#ff3b2f,color:#e8e8e8
  classDef lane fill:#0b0b0b,stroke:#e8e8e8,color:#e8e8e8
  owner[the owner<br/>approves the board, every quote, every pick]:::lead
  lead[lead agent<br/>reads the pack, plans, quotes, keeps the log honest]:::lead
  clerk[clerk<br/>intake: converts every input, screenshots, the log tool]:::lane
  scout[scout<br/>references with their licences]:::lane
  qm[quartermaster<br/>Runware facts, the cost model, the quote]:::lane
  director[director<br/>the storyboard, the prompts, the reshaped shots]:::lane
  stagelane[stage<br/>the Blender stages, turntables, blocking]:::lane
  sheetlane[sheets<br/>the character and mob panels]:::lane
  owner <--> lead
  lead --> clerk & scout & qm & director & stagelane & sheetlane
```

## The folders

```mermaid
flowchart LR
  classDef f fill:#0b0b0b,stroke:#8a8a8a,color:#e8e8e8
  root[runware-test]:::f
  root --> b[00-brief]:::f
  root --> s[01-story: script, shot list, storyboard]:::f
  root --> c[02-cast: prints, sheet, mesh per character]:::f
  root --> l[03-locations: build, maps, stage, plates per scene]:::f
  root --> p[04-prompts: master prompt, bible, every prompt sent]:::f
  root --> sh[05-shots: clay, frame, takes, pick per shot]:::f
  root --> so[06-sound]:::f
  root --> cu[07-cut: 4K master, 1080p, title, picks, reels]:::f
  root --> m[08-making-of: log, screens, clips, recordings, notes]:::f
  root --> w[09-showcase]:::f
  root --> br[10-b-roll]:::f
  root --> mp[maps]:::f
  root --> t[tools: paths.json, gather.mjs]:::f
```
