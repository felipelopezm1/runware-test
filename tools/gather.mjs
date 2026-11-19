#!/usr/bin/env node
/**
 * gather.mjs: copy the production's files into this repository along tools/paths.json.
 *
 * Runs on the production machine (the one with the hand-made pack and the storyboard folder), from the
 * repository's root. Node 18 or newer, standard library only. Nothing is deleted, and a file already here
 * with the same size is left alone.
 *
 *   node tools/gather.mjs                 dry run: says what would be copied, how big, and what is missing
 *   node tools/gather.mjs --copy          copies the small files (every entry without "large": true)
 *   node tools/gather.mjs --copy --large  copies the large ones too (they are gitignored or meant for LFS and Drive)
 *   node tools/gather.mjs --only 02-cast  limits to entries whose "to" starts with that prefix
 *
 * An entry's "from" is "<root>:<path>"; "files" is a space-separated list of glob-like names (* only) taken from
 * that folder; "{shot}" in "to", "from" or "files" expands to each of the sixteen shots.
 */
import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

const here = path.dirname(fileURLToPath(import.meta.url));
const repo = path.resolve(here, "..");
const spec = JSON.parse(fs.readFileSync(path.join(here, "paths.json"), "utf8"));
const args = process.argv.slice(2);
const copy = args.includes("--copy");
const large = args.includes("--large");
const only = args.includes("--only") ? args[args.indexOf("--only") + 1] : "";
const SHOTS = ["1A", "1B", "1C", "1D", "2A", "2B", "2C", "2D", "3A", "3B", "3C", "3D", "3E", "3F", "3G", "3H"];

const expand = (entry) =>
  JSON.stringify(entry).includes("{shot}")
    ? SHOTS.map((s) => JSON.parse(JSON.stringify(entry).replaceAll("{shot}", s)))
    : [entry];
const glob = (pattern) => new RegExp("^" + pattern.split("*").map((p) => p.replace(/[.+?^${}()|[\]\\]/g, "\\$&")).join(".*") + "$", "i");

let planned = 0, bytes = 0, copied = 0, missing = 0, skipped = 0;
const lines = [];
for (const raw of spec.map) {
  for (const entry of expand(raw)) {
    if (only && !entry.to.startsWith(only)) continue;
    if (entry.large && !large) { skipped++; continue; }
    const [root, rel] = entry.from.split(/:(.*)/s);
    const src = path.join(spec.roots[root], rel);
    const dst = path.join(repo, entry.to);
    if (!fs.existsSync(src)) {
      missing++;
      lines.push(`${entry.pending ? "pending" : "MISSING"}  ${entry.to}  <-  ${src}`);
      continue;
    }
    const stat = fs.statSync(src);
    const pairs = [];
    if (stat.isFile()) {
      pairs.push([src, dst]);
    } else {
      const names = fs.readdirSync(src).filter((n) => fs.statSync(path.join(src, n)).isFile());
      const wanted = entry.files ? entry.files.split(/\s+/).map(glob) : null;
      for (const n of names) {
        if (wanted && !wanted.some((re) => re.test(n))) continue;
        pairs.push([path.join(src, n), path.join(dst, n)]);
      }
    }
    for (const [s, d] of pairs) {
      const size = fs.statSync(s).size;
      if (fs.existsSync(d) && fs.statSync(d).size === size) continue;
      planned++; bytes += size;
      if (copy) {
        fs.mkdirSync(path.dirname(d), { recursive: true });
        fs.copyFileSync(s, d);
        copied++;
      }
    }
    lines.push(`${copy ? "copied " : "would  "} ${entry.to}  (${pairs.length} files)`);
  }
}
console.log(lines.join("\n"));
console.log(`\n${copy ? copied + " copied" : planned + " to copy"}, ${(bytes / 1e6).toFixed(1)} MB; ${missing} sources missing or pending; ${skipped} large entries ${large ? "" : "skipped (add --large)"}`);
