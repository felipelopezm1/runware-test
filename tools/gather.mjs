#!/usr/bin/env node
/**
 * gather.mjs: copy the production's files into this repository along tools/paths.json.
 *
 * Entries with "where": "drive" are skipped unless --large is given (they are not for Git).
 * Runs on the production machine (the one with the hand-made pack and the storyboard folder), from the
 * repository's root. Node 18 or newer, standard library only. Nothing is deleted, and a file already here
 * with the same size is left alone.
 *
 *   node tools/gather.mjs                 dry run: says what would be copied, how big, and what is missing
 *   node tools/gather.mjs --copy          copies the Git-sized files (every entry without "large": true)
 *   node tools/gather.mjs --link          the same as hard links (same filesystem): no disk is used; a file that cannot
 *                                         be linked is named and left out, never copied
 *   node tools/gather.mjs --copy --large  the Drive-only files too, into the same layout, ready to upload to Drive
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
// GATHER_LAPTOP and GATHER_STORYBOARD override the two roots (for a test on another machine).
if (process.env.GATHER_LAPTOP) spec.roots.laptop = process.env.GATHER_LAPTOP;
if (process.env.GATHER_STORYBOARD) spec.roots.storyboard = process.env.GATHER_STORYBOARD;
const args = process.argv.slice(2);
const link = args.includes("--link");
const copy = args.includes("--copy") || link;
const large = args.includes("--large");
const only = args.includes("--only") ? args[args.indexOf("--only") + 1] : "";
const SHOTS = ["1A", "1B", "1C-1", "1C-2", "2A-1", "2A-2", "2B", "2C", "3A", "3B", "3C-1", "3C-2", "3D-1", "3D-2", "3E", "3F"];

const expand = (entry) =>
  JSON.stringify(entry).includes("{shot}")
    ? SHOTS.map((s) => JSON.parse(JSON.stringify(entry).replaceAll("{shot}", s)))
    : [entry];
const glob = (pattern) => new RegExp("^" + pattern.split("*").map((p) => p.replace(/[.+?^${}()|[\]\\]/g, "\\$&")).join(".*") + "$", "i");

let planned = 0, bytes = 0, copied = 0, missing = 0, skipped = 0;
const unlinked = [];
const lines = [];
for (const raw of spec.map) {
  for (const entry of expand(raw)) {
    if (only && !entry.to.startsWith(only)) continue;
    if (entry.where === "drive" && !large) { skipped++; continue; }
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
        if (link) {
          // a hard link uses no disk; across filesystems it fails, and then the file is skipped and named, never copied
          try { fs.linkSync(s, d); } catch { unlinked.push(d); continue; }
        } else fs.copyFileSync(s, d);
        copied++;
      }
    }
    lines.push(`${copy ? "copied " : "would  "} ${entry.to}  (${pairs.length} files)`);
  }
}
console.log(lines.join("\n"));
if (unlinked.length) console.log(`\ncould not hard-link (another filesystem), left out:\n  ${unlinked.join("\n  ")}`);
console.log(`\n${copy ? copied + " copied" : planned + " to copy"}, ${(bytes / 1e6).toFixed(1)} MB; ${missing} sources missing or pending; ${skipped} large entries ${large ? "" : "skipped (add --large)"}`);
