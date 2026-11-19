# tools: this repository's own tools

| file | what it does |
| --- | --- |
| [`paths.json`](paths.json) | the map from the production machine's two folders (the hand-made pack and the agents' storyboard folder) to the folders here and to the Drive mirror: one entry per destination, with the files it takes, where it belongs (`git`, `drive` or both) and whether its source exists yet |
| [`gather.mjs`](gather.mjs) | walks that map and copies the files in; a dry run by default, `--copy` to copy, `--link` to hard-link instead of copying (no extra disk on the production machine, which is tight), `--large` to include the Drive-only entries, `--only <prefix>` to limit it |

The agents' own production tools (the log tool, the intake converter, the director's prompt assembler, the finishing scripts, the recording scripts) are not here: they belong to the record and live in [`08-making-of/tools/`](../08-making-of/tools/).

The paths in `paths.json` are the only place in this repository that names the production machine's folders; every other page points at the file here or at its place in the Drive folder.

```
node tools/gather.mjs                     # what would be copied, and what is still pending
node tools/gather.mjs --link              # the Git-sized files, as hard links (same filesystem, no disk used)
node tools/gather.mjs --link --large      # the Drive-only files too, into the same layout, ready to drag to Drive
```
