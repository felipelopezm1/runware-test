# tools: this repository's own tools

| file | what it does |
| --- | --- |
| [`paths.json`](paths.json) | the map from the production machine's two folders (the hand-made pack and the agents' storyboard folder) to the folders here: one entry per destination, with the files it takes, whether it is large (Drive first) and whether its source exists yet |
| [`gather.mjs`](gather.mjs) | walks that map and copies the files in; a dry run by default, `--copy` to copy, `--large` to include the large entries, `--only <prefix>` to limit it |

The agents' own production tools (the log tool, the intake converter, the director's prompt assembler, the recording scripts) are not here: they belong to the record and live in [`08-making-of/tools/`](../08-making-of/tools/).

```
node tools/gather.mjs              # what would be copied, and what is still pending
node tools/gather.mjs --copy       # the small files
node tools/gather.mjs --copy --large
```
