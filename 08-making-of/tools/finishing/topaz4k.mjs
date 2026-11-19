#!/usr/bin/env node
// topaz4k.mjs: upscale one finished film to 3840x2160 with Topaz Proteus 4 on Runware (topazlabs:proteus@4),
// download it, verify it, and put the source's own sound back on it untouched.
//
//   node topaz4k.mjs --in SRC.mp4 --out OUT.mp4 [--dry-run]
//
// Route: the private house-keyed Titanium app (the same one heph.mjs drives), never Runware directly, so no key
// is read, printed or sent by this script. The film goes to the owner's Blob store through the app's
// /api/blob/upload (Vercel Blob client upload: a one-file token from the app, the bytes straight to the store,
// no 4.2 MB limit; /api/runware/upload stops at 4.2 MB), then one raw `upscale` task goes to /api/runware/run
// (kind "raw", the shape the zombie test used on 2026-11-11) and is polled on /api/runware/status.
//
// Flags
//   --in SRC            the finished film (H.264 + AAC, 24 fps, 1920x1080 expected)
//   --out OUT           the 4K master to write; refused if it exists (never overwritten)
//   --dry-run           probe, estimate, build and print the payload(s), run the free checks, stop. Spends nothing,
//                       uploads nothing
//   --target vercel     vercel (default: https://titanium-hephaestus.vercel.app from ~/titanium-hephaestus-url.txt,
//                       bypass header from ~/titanium-hephaestus-bypass.txt) or local (http://localhost:3100)
//   --base URL          point the target elsewhere
//   --src-url URL       skip the upload: a public URL of the video already on the Blob store or Runware's storage
//                       (one segment only)
//   --split SECONDS     cut the film into segments of about this length at its own keyframes (stream copy, no
//                       re-encode), one task each, joined again by stream copy with the exact frame count checked.
//                       Off by default: Topaz's schema states no duration or size cap.
//   --resume ID[,ID]    do not launch: follow tasks already launched (their ids, in segment order) and finish
//   --max-usd N         refuse a real run whose high estimate is over N (default 3)
//   --quality N         outputQuality 20..99 (default 95, as the zombie test)
//   --work DIR          scratch folder (default making-of/finishing/work/<out-name>-<stamp>)
//   --timeout S         how long to follow the task(s) (default 3600)
//   --lane NAME --plan-step N --shot ID   for the log line (defaults: finishing, 11, null)
//   --no-log            do not append to making-of/log.jsonl
//   --allow-mismatch    mux even if the upscale's frame count differs from the source's (default: stop)

import fs from "node:fs";
import os from "node:os";
import path from "node:path";
import { spawnSync } from "node:child_process";
import { fileURLToPath, pathToFileURL } from "node:url";

const SELF = fileURLToPath(import.meta.url);
const MAKING_OF = path.resolve(path.dirname(SELF), "..", "..");
const LOG_TOOL = path.join(MAKING_OF, "tools", "log.mjs");
const AIR = "topazlabs:proteus@4";
const STORE_PROJECT = "is-this-all-on-runware";
const BLOB_CLIENT_CANDIDATES = [
  process.env.TOPAZ4K_BLOB_CLIENT,
  "/home/felipe-lopez/titanium/.hephaestus/irons/runware-hephaestus-control/node_modules/@vercel/blob/dist/client.js",
  path.join(os.homedir(), ".cache/rw-local/node_modules/@vercel/blob/dist/client.js"),
].filter(Boolean);

// What Runware charged and listed for Topaz Proteus 4 to 4K (notes/runware-facts.md, notes/cost-model.md):
// charged $0.0856 for 5.04 s and $0.1712 for 8.71 s at 24 fps 1080p -> 4K (zombie test, 2026-11-11);
// listed $0.15 for 4.8 s at 3840x2160 and 30 fps (the schema's measured price).
const RATE = {
  low: 0.0856 / 5.04,
  expected: (0.0856 + 0.1712) / (5.04 + 8.71),
  high: 0.15 / 4.8,
};

// ---------- arguments ----------

function parse(argv) {
  const f = {};
  for (let i = 0; i < argv.length; i++) {
    const a = argv[i];
    if (!a.startsWith("--")) throw new Error(`unexpected argument: ${a}`);
    const [k, v] = a.slice(2).split(/=(.*)/s, 2);
    if (v !== undefined) f[k] = v;
    else if (argv[i + 1] !== undefined && !argv[i + 1].startsWith("--")) f[k] = argv[++i];
    else f[k] = true;
  }
  return f;
}

const F = parse(process.argv.slice(2));
const DRY = !!F["dry-run"];
const say = (...a) => console.log(...a);
const fail = (msg) => {
  console.error(`topaz4k: ${msg}`);
  process.exit(1);
};
if (F.help || !F.in || !F.out) {
  say("usage: node topaz4k.mjs --in SRC.mp4 --out OUT.mp4 [--dry-run] [--target vercel|local] [--split S] [--src-url URL] [--resume ID] [--max-usd N] [--no-log]");
  process.exit(F.help ? 0 : 2);
}
const SRC = path.resolve(String(F.in));
const OUT = path.resolve(String(F.out));
const WIDTH = 3840;
const HEIGHT = 2160;
const QUALITY = Math.max(20, Math.min(99, Number(F.quality) || 95));
const MAX_USD = F["max-usd"] !== undefined ? Number(F["max-usd"]) : 3;
const TIMEOUT_S = Number(F.timeout) || 3600;

// ---------- small helpers ----------

function run(cmd, args, { allowFail = false } = {}) {
  const r = spawnSync(cmd, args, { encoding: "utf8", maxBuffer: 64 * 1024 * 1024 });
  if (r.error) fail(`${cmd} did not run (${r.error.code ?? r.error.message})`);
  if (r.status !== 0 && !allowFail) fail(`${cmd} ${args.slice(0, 6).join(" ")} ... failed:\n${(r.stderr || "").slice(-1500)}`);
  return r;
}

function probe(file) {
  const j = JSON.parse(run("ffprobe", ["-v", "error", "-count_packets", "-show_entries", "stream=index,codec_type,codec_name,width,height,r_frame_rate,nb_read_packets,sample_rate,channels,duration:format=duration,size", "-of", "json", file]).stdout);
  const v = j.streams.find((s) => s.codec_type === "video");
  const a = j.streams.filter((s) => s.codec_type === "audio");
  if (!v) fail(`${file} has no video stream`);
  const [n, d] = String(v.r_frame_rate).split("/").map(Number);
  return { file, width: v.width, height: v.height, fps: d ? n / d : n, fpsText: v.r_frame_rate, frames: Number(v.nb_read_packets), vcodec: v.codec_name, duration: Number(j.format.duration), size: Number(j.format.size), audio: a.map((s) => ({ codec: s.codec_name, rate: s.sample_rate, channels: s.channels, duration: Number(s.duration) })) };
}

function keyframes(file) {
  return run("ffprobe", ["-v", "error", "-select_streams", "v:0", "-skip_frame", "nokey", "-show_entries", "frame=pts_time", "-of", "csv=p=0", file])
    .stdout.split("\n").map((l) => parseFloat(l)).filter((t) => Number.isFinite(t));
}

const usd = (x) => `$${x.toFixed(4)}`;
const stamp = () => new Date().toISOString().replace(/[-:]/g, "").replace(/\..*/, "Z");
const sleep = (ms) => new Promise((r) => setTimeout(r, ms));

/** Copy without ever replacing an existing file. */
function placeNew(src, dest) {
  try {
    fs.copyFileSync(src, dest, fs.constants.COPYFILE_EXCL);
  } catch (e) {
    if (e.code === "EEXIST") fail(`${dest} exists; it is never overwritten`);
    throw e;
  }
}

// ---------- the target (the private app; the same rules as heph.mjs) ----------

const firstLine = (p) => (fs.existsSync(p) ? fs.readFileSync(p, "utf8").split("\n").map((l) => l.trim()).find(Boolean) ?? "" : "");

function target() {
  const name = String(F.target === true || F.target === undefined ? "vercel" : F.target);
  if (name !== "local" && name !== "vercel") fail(`--target is local or vercel, not ${name}`);
  let base = typeof F.base === "string" ? F.base : "";
  let bypass = "";
  const bypassFile = path.join(os.homedir(), "titanium-hephaestus-bypass.txt");
  if (name === "local") base ||= process.env.HEPH_LOCAL_URL || "http://localhost:3100";
  else {
    base ||= process.env.HEPH_VERCEL_URL || firstLine(path.join(os.homedir(), "titanium-hephaestus-url.txt"));
    bypass = process.env.HEPH_VERCEL_BYPASS || firstLine(bypassFile);
  }
  if (base && !/^https?:\/\//.test(base)) base = `https://${base}`;
  base = base.replace(/\/+$/, "");
  return { name, base, origin: base ? new URL(base).origin : "", bypass, bypassFile };
}
const T = target();

function headers(post) {
  const h = { accept: "application/json" };
  if (T.bypass) h["x-vercel-protection-bypass"] = T.bypass; // sent, never printed
  if (post) {
    h.origin = T.origin; // the routes refuse a POST from another site
    h["content-type"] = "application/json";
  }
  return h;
}

async function call(p, { method = "GET", body, tries = 4 } = {}) {
  for (let i = 0; ; i++) {
    let res;
    try {
      res = await fetch(T.base + p, { method, headers: headers(method !== "GET"), body: body === undefined ? undefined : JSON.stringify(body), redirect: "manual" });
    } catch (e) {
      return { status: 0, ok: false, json: { error: `${T.base} did not answer (${e.cause?.code ?? e.message})` } };
    }
    const text = await res.text();
    let json;
    try {
      json = text ? JSON.parse(text) : {};
    } catch {
      json = { error: `${method} ${p} answered ${res.status}, not JSON${res.status >= 300 && res.status < 400 ? " (Vercel's sign-in: the bypass secret is missing or not taken)" : ""}` };
    }
    if (res.status === 429 && i < tries - 1 && json?.type !== "spend_cap") {
      await sleep(Math.min(60, Number(res.headers.get("retry-after")) || 5) * 1000);
      continue;
    }
    return { status: res.status, ok: res.ok, json };
  }
}
const errOf = (r) => (typeof r.json?.error === "string" ? r.json.error : JSON.stringify(r.json?.error ?? r.json)).slice(0, 600);

// ---------- the store upload (Vercel Blob client upload through the app) ----------

async function blobClient() {
  for (const p of BLOB_CLIENT_CANDIDATES) if (fs.existsSync(p)) return { path: p, mod: await import(pathToFileURL(p).href) };
  return null;
}

async function uploadToStore(file, name) {
  const bc = await blobClient();
  if (!bc) fail(`no @vercel/blob client found (looked in ${BLOB_CLIENT_CANDIDATES.join(", ")}); set TOPAZ4K_BLOB_CLIENT`);
  const pathname = `titanium/${STORE_PROJECT}/clip/${name}`; // must pass the app's isOurPath
  const size = fs.statSync(file).size;
  const body = await fs.openAsBlob(file, { type: "video/mp4" });
  let last = -1;
  const out = await bc.mod.upload(pathname, body, {
    access: "public",
    handleUploadUrl: `${T.base}/api/blob/upload`,
    contentType: "video/mp4",
    multipart: size > 50 * 1024 * 1024,
    headers: headers(true), // origin + bypass for the token call to the app; the PUT to the store does not carry them
    onUploadProgress: (e) => {
      const p = Math.floor(e.percentage / 10) * 10;
      if (p !== last) {
        last = p;
        process.stdout.write(`  upload ${p}%\r`);
      }
    },
  });
  say(`  uploaded ${(size / 1e6).toFixed(1)} MB -> ${out.url}`);
  return out.url;
}

// ---------- the task ----------

function task(videoUrl) {
  // exactly the zombie test's Topaz task (2026-11-11, task 5cae9a93): width/height are an envelope (aspect kept),
  // fps left out so it stays the source's 24 (the schema rejects a lower one), no settings (the model's own weights)
  return { taskType: "upscale", model: AIR, inputs: { video: videoUrl }, width: WIDTH, height: HEIGHT, outputType: "URL", outputFormat: "MP4", outputQuality: QUALITY, includeCost: true };
}

async function follow(id, deadline) {
  const q = new URLSearchParams({ id, endpoint: AIR });
  let wait = 10_000;
  let lastLine = "";
  while (Date.now() < deadline) {
    const r = await call(`/api/runware/status?${q}`);
    const j = r.json ?? {};
    if (j.status === "done") {
      const row = (j.raw ?? []).find((x) => x.videoURL) ?? {};
      return { status: "done", url: j.output?.video?.url ?? row.videoURL, cost: typeof j.cost === "number" ? j.cost : row.cost, raw: j.raw };
    }
    if (j.status === "failed" || j.status === "unknown") return { status: "failed", error: j.error ?? errOf(r) };
    if (!r.ok && r.status !== 0) say(`  status answered ${r.status}: ${errOf(r)}`);
    const line = `  ${id.slice(0, 8)} ${j.status ?? "?"}${j.progress !== undefined ? ` ${j.progress}%` : ""}`;
    if (line !== lastLine) say(line);
    lastLine = line;
    await sleep(wait);
    wait = Math.min(20_000, wait + 2_000);
  }
  return { status: "timeout", error: `still running after ${TIMEOUT_S} s: rerun with --resume ${id}` };
}

async function download(url, dest) {
  const res = await fetch(url);
  if (!res.ok) fail(`download ${url} answered ${res.status}`);
  const fd = fs.openSync(dest, "wx"); // never overwrite
  try {
    for await (const chunk of res.body) fs.writeSync(fd, chunk);
  } finally {
    fs.closeSync(fd);
  }
  return fs.statSync(dest).size;
}

// ---------- the log line ----------

function logLine(entry) {
  if (F["no-log"]) return say("  log: skipped (--no-log)");
  const r = spawnSync(process.execPath, [LOG_TOOL, "add", "-"], { input: JSON.stringify(entry), encoding: "utf8" });
  if (r.status === 0) say(`  log: step ${r.stdout.trim()} in ${path.join(MAKING_OF, "log.jsonl")}`);
  else {
    const keep = path.join(WORK, "log-entry.json");
    fs.writeFileSync(keep, JSON.stringify(entry, null, 2));
    say(`  log: log.mjs failed (${(r.stderr || "").trim().slice(0, 300)}); the entry is kept at ${keep}: node ${LOG_TOOL} add ${keep}`);
  }
}

// ---------- 1. the source ----------

for (const tool of ["ffmpeg", "ffprobe"]) if (spawnSync(tool, ["-version"]).status !== 0) fail(`${tool} is missing`);
if (!fs.existsSync(SRC)) fail(`no such file: ${SRC}`);
if (fs.existsSync(OUT)) fail(`${OUT} exists; it is never overwritten`);
const src = probe(SRC);
say(`source  ${SRC}`);
say(`        ${src.width}x${src.height} ${src.vcodec} ${src.fpsText} fps, ${src.frames} frames, ${src.duration.toFixed(3)} s, ${(src.size / 1e6).toFixed(1)} MB; audio: ${src.audio.map((a) => `${a.codec} ${a.rate} Hz ${a.channels} ch`).join(", ") || "none"}`);
if (Math.abs(src.width / src.height - WIDTH / HEIGHT) > 0.01) say(`  warning: the source is not 16:9; Topaz keeps its aspect inside ${WIDTH}x${HEIGHT}, so the result will not be exactly ${WIDTH}x${HEIGHT} and the check will stop`);
if (src.audio.length > 1) say(`  note: ${src.audio.length} audio streams; all are copied back`);

// ---------- 2. segments ----------

const split = Number(F.split) || 0;
let cuts = []; // keyframe times where a new segment starts (besides 0)
if (split > 0) {
  const keys = keyframes(SRC);
  let last = 0;
  for (let t = split; t < src.duration - 1; t += split) {
    const k = keys.filter((x) => x > last + 1 && x < src.duration - 1).reduce((b, x) => (b === null || Math.abs(x - t) < Math.abs(b - t) ? x : b), null);
    if (k !== null && !cuts.includes(k)) {
      cuts.push(k);
      last = k;
    }
  }
  cuts.sort((a, b) => a - b);
}
const bounds = [0, ...cuts, src.duration];
const segs = bounds.slice(0, -1).map((s, i) => ({ i, start: s, end: bounds[i + 1], seconds: bounds[i + 1] - s, frames: Math.round((bounds[i + 1] - s) * src.fps) }));
if (segs.length > 1) {
  say(`segments (--split ${split}: cut at the source's own keyframes, stream copy, no re-encode):`);
  for (const s of segs) say(`  ${String(s.i).padStart(2, "0")}  ${s.start.toFixed(3)} -> ${s.end.toFixed(3)} s  (${s.seconds.toFixed(3)} s, ~${s.frames} frames)`);
} else say("segments: one (the whole film in one task; Topaz's schema states no duration or size cap)");

// ---------- 3. the estimate, first ----------

const est = { low: src.duration * RATE.low, expected: src.duration * RATE.expected, high: src.duration * RATE.high };
say(`estimate  ${src.duration.toFixed(2)} s at 24 fps to ${WIDTH}x${HEIGHT}: low ${usd(est.low)}, expected ${usd(est.expected)}, high ${usd(est.high)}`);
say(`          (charged $0.0170 to $0.0197 a second in the zombie test at 24 fps; listed $0.0313 a second at 30 fps)`);
say(`          ${segs.length} task(s); the app's daily ceiling is $25; this run refuses if high > --max-usd ${MAX_USD}`);

// ---------- 4. the payload(s) ----------

const slug = path.basename(OUT).replace(/\.[^.]+$/, "").toLowerCase().replace(/[^a-z0-9]+/g, "-").replace(/^-+|-+$/g, "").slice(0, 60) || "film";
const placeholder = (i) => (F["src-url"] && segs.length === 1 ? String(F["src-url"]) : `<the store URL of the upload: https://<store>.public.blob.vercel-storage.com/titanium/${STORE_PROJECT}/clip/topaz4k-${slug}${segs.length > 1 ? `-seg${String(i).padStart(2, "0")}` : ""}-<stamp>-<random>.mp4>`);
const bodies = segs.map((s) => ({ kind: "raw", task: task(placeholder(s.i)), cost: +(s.seconds * RATE.high).toFixed(4) }));
say(`route   ${T.name}: ${T.base || "(no URL)"}`);
say(`        1. upload: POST ${T.base}/api/blob/upload (Vercel Blob client token, Origin ${T.origin}${T.bypass ? ", x-vercel-protection-bypass from the bypass file" : ""}), bytes PUT straight to the store`);
say(`        2. run:    POST ${T.base}/api/runware/run with each body below`);
say(`        3. follow: GET  ${T.base}/api/runware/status?id=<task>&endpoint=${AIR}`);
say(`        4. download the videoURL (vm.runware.ai), verify, mux the source's sound back (-c:a copy)`);
for (const [i, b] of bodies.entries()) say(`payload${bodies.length > 1 ? ` ${i}` : ""} (POST /api/runware/run; the app adds taskUUID and holds the key):\n${JSON.stringify(b, null, 2)}`);

// ---------- 5. dry run: the free checks, then stop ----------

if (DRY) {
  say("checks (free):");
  const okMark = (b) => (b ? "ok     " : "MISSING");
  if (T.name === "vercel") say(`  ${okMark(!!T.base)} the app's URL (~/titanium-hephaestus-url.txt)`);
  if (T.name === "vercel") say(`  ${okMark(!!T.bypass)} the bypass secret (${T.bypassFile}; not printed)`);
  if (T.base) {
    const r = await call("/api/runware/ready?check=1");
    say(`  ${okMark(r.ok && r.json.ready && r.json.valid !== false)} the app's Runware key (ready ${r.json.ready}, source ${r.json.source}, valid ${r.json.valid}${r.ok ? "" : `, ${errOf(r)}`})`);
    const s = await call("/api/blob/ready?check=1");
    say(`  ${okMark(s.ok && s.json.ready && s.json.valid !== false)} the app's Blob store (ready ${s.json.ready}, source ${s.json.source}, valid ${s.json.valid}${s.ok ? "" : `, ${errOf(s)}`})`);
    const u = await call("/api/blob/upload");
    say(`  ${okMark(u.status === 405)} the upload route answers (GET -> ${u.status}; 405 means it is there and takes POST only)`);
    // the token handshake alone (what the Blob client does first): free, nothing is stored without the PUT
    const t = await call("/api/blob/upload", { method: "POST", body: { type: "blob.generate-client-token", payload: { pathname: `titanium/${STORE_PROJECT}/clip/topaz4k-dry-run-check.mp4`, clientPayload: null, multipart: true } } });
    const gotToken = t.ok && typeof t.json?.clientToken === "string" && t.json.clientToken.length > 20;
    say(`  ${okMark(gotToken)} the store hands this script an upload token through the app (POST -> ${t.status}${gotToken ? "; token not printed, unused, expires in an hour" : `, ${errOf(t)}`})`);
    const p = await call(`/api/runware/pricing?endpoint_id=${encodeURIComponent(AIR)}`);
    const pr = p.json?.prices?.[0] ?? p.json?.prices?.[AIR];
    say(`  ${okMark(p.ok)} the app knows ${AIR} (its own list price: ${pr ? `${pr.unit_price} USD / ${pr.unit}${pr.estimate ? ", an estimate (the 1080p rate)" : ""}` : errOf(p)})`);
  }
  const bc = await blobClient();
  say(`  ${okMark(!!bc)} the Blob client module (${bc ? bc.path : "set TOPAZ4K_BLOB_CLIENT"}; exports upload: ${!!bc?.mod?.upload})`);
  say(`  ${okMark(fs.existsSync(LOG_TOOL))} the log tool (${LOG_TOOL})`);
  say(`  ${okMark(!fs.existsSync(OUT))} the output does not exist yet (${OUT})`);
  say(`  ${okMark(est.high <= MAX_USD)} high estimate ${usd(est.high)} within --max-usd ${MAX_USD}`);
  say("dry run: nothing uploaded, nothing sent, nothing spent.");
  process.exit(0);
}

// ---------- 6. the real run ----------

if (!T.base) fail("no app URL: ~/titanium-hephaestus-url.txt is missing (or pass --base)");
if (T.name === "vercel" && !T.bypass) fail(`no bypass secret: ${T.bypassFile} is missing or empty`);
if (!F.resume && est.high > MAX_USD) fail(`the high estimate ${usd(est.high)} is over --max-usd ${MAX_USD}`);
const WORK = path.resolve(typeof F.work === "string" ? F.work : path.join(MAKING_OF, "finishing", "work", `${slug}-${stamp()}`));
fs.mkdirSync(WORK, { recursive: true });
const recordFile = path.join(WORK, "record.json");
const record = { at: new Date().toISOString(), src: SRC, out: OUT, target: T.name, base: T.base, air: AIR, estimate: est, segments: segs, tasks: [] };
const saveRecord = () => fs.writeFileSync(recordFile, JSON.stringify(record, null, 2));
saveRecord();
say(`work    ${WORK}`);

const r0 = await call("/api/runware/ready?check=1");
if (!r0.ok || !r0.json.ready || r0.json.valid === false) fail(`the app is not ready: ${errOf(r0)}`);

// the video stream alone (stream copy: the pixels Topaz gets are the source's own), one file per segment
const parts = [];
if (segs.length === 1) {
  const p = path.join(WORK, "video-only.mp4");
  run("ffmpeg", ["-hide_banner", "-v", "error", "-n", "-i", SRC, "-map", "0:v:0", "-c", "copy", "-an", "-movflags", "+faststart", p]);
  parts.push(p);
} else {
  run("ffmpeg", ["-hide_banner", "-v", "error", "-n", "-i", SRC, "-map", "0:v:0", "-c", "copy", "-an", "-f", "segment", "-segment_times", cuts.map((c) => c.toFixed(6)).join(","), "-reset_timestamps", "1", "-segment_format", "mp4", "-segment_format_options", "movflags=+faststart", path.join(WORK, "seg-%02d.mp4")]);
  for (const s of segs) parts.push(path.join(WORK, `seg-${String(s.i).padStart(2, "0")}.mp4`));
}
const partFrames = parts.map((p) => probe(p).frames);
const sumFrames = partFrames.reduce((a, b) => a + b, 0);
say(`  prepared ${parts.length} part(s), frames ${partFrames.join(" + ")} = ${sumFrames} (source ${src.frames})`);
if (sumFrames !== src.frames) fail(`the parts hold ${sumFrames} frames, the source ${src.frames}: not cutting`);

const resume = typeof F.resume === "string" ? F.resume.split(",").map((s) => s.trim()).filter(Boolean) : [];
if (resume.length && resume.length !== parts.length) fail(`--resume names ${resume.length} task(s), the plan has ${parts.length}`);

const deadline = Date.now() + TIMEOUT_S * 1000;
const results = [];
for (const [i, part] of parts.entries()) {
  let id = resume[i];
  let input = null;
  if (!id) {
    input = F["src-url"] && parts.length === 1 ? String(F["src-url"]) : await uploadToStore(part, `topaz4k-${slug}${parts.length > 1 ? `-seg${String(i).padStart(2, "0")}` : ""}-${stamp().toLowerCase()}.mp4`);
    const body = { kind: "raw", task: task(input), cost: +(segs[i].seconds * RATE.high).toFixed(4) };
    const r = await call("/api/runware/run", { method: "POST", body });
    if (!r.ok) fail(`run answered ${r.status}: ${errOf(r)}${r.json?.parameter ? ` (${r.json.parameter})` : ""}`);
    const job = r.json.jobs?.[0];
    if (!job?.requestId) fail(`run gave no task id: ${JSON.stringify(r.json).slice(0, 400)}`);
    id = job.requestId;
    say(`  launched part ${i}: task ${id} (if this stops, finish with --resume ${id})`);
  } else say(`  resuming part ${i}: task ${id}`);
  record.tasks[i] = { id, input };
  saveRecord();
  const f = await follow(id, deadline);
  record.tasks[i] = { ...record.tasks[i], ...f, raw: undefined };
  saveRecord();
  if (f.status !== "done") {
    const charged = record.tasks.reduce((a, t) => a + (typeof t?.cost === "number" ? t.cost : 0), 0);
    if (charged > 0) logLine(entryOf({ charged, outputs: [], ok: false, note: `stopped at part ${i}: ${f.error}` }));
    fail(`task ${id} ${f.status}: ${f.error}`);
  }
  const dest = path.join(WORK, `topaz-${String(i).padStart(2, "0")}.mp4`);
  const bytes = await download(f.url, dest);
  const u = probe(dest);
  say(`  part ${i} done: ${u.width}x${u.height} ${u.vcodec} ${u.fpsText} fps, ${u.frames} frames, ${(bytes / 1e6).toFixed(1)} MB, charged ${typeof f.cost === "number" ? usd(f.cost) : "(not reported)"}`);
  results.push({ file: dest, probe: u, cost: f.cost, url: f.url, id });
}

const charged = +results.reduce((a, r) => a + (typeof r.cost === "number" ? r.cost : 0), 0).toFixed(6);
const costReported = results.every((r) => typeof r.cost === "number");

// ---------- 7. verify, join, mux ----------

const problems = [];
for (const [i, r] of results.entries()) {
  if (r.probe.width !== WIDTH || r.probe.height !== HEIGHT) problems.push(`part ${i} is ${r.probe.width}x${r.probe.height}, not ${WIDTH}x${HEIGHT}`);
  if (r.probe.frames !== partFrames[i]) problems.push(`part ${i} has ${r.probe.frames} frames, its source ${partFrames[i]}`);
  if (Math.abs(r.probe.fps - src.fps) > 0.001) problems.push(`part ${i} runs at ${r.probe.fpsText} fps, the source ${src.fpsText}`);
}
if (problems.length && !F["allow-mismatch"]) {
  logLine(entryOf({ charged, outputs: results.map((r) => r.file), ok: false, note: `verification failed, not muxed: ${problems.join("; ")}` }));
  fail(`verification failed (the upscale is kept in ${WORK}; rerun the mux with --allow-mismatch --resume ${results.map((r) => r.id).join(",")} only if this is acceptable):\n  ${problems.join("\n  ")}`);
}

let video = results[0].file;
if (results.length > 1) {
  const list = path.join(WORK, "concat.txt");
  fs.writeFileSync(list, results.map((r) => `file '${r.file.replace(/'/g, "'\\''")}'`).join("\n") + "\n");
  video = path.join(WORK, "topaz-joined.mp4");
  run("ffmpeg", ["-hide_banner", "-v", "error", "-n", "-f", "concat", "-safe", "0", "-i", list, "-map", "0:v:0", "-c", "copy", "-movflags", "+faststart", video]);
}

const muxed = path.join(WORK, "final.mp4");
const audioMaps = src.audio.flatMap((_, k) => ["-map", `1:a:${k}`]);
// HEVC from Topaz gets the hvc1 tag so QuickTime and browsers play the MP4; the pixels are copied either way
const tag = results[0].probe.vcodec === "hevc" ? ["-tag:v", "hvc1"] : [];
run("ffmpeg", ["-hide_banner", "-v", "error", "-n", "-i", video, "-i", SRC, "-map", "0:v:0", ...audioMaps, "-c:v", "copy", ...tag, "-c:a", "copy", "-movflags", "+faststart", muxed]);
const fin = probe(muxed);
const finalProblems = [];
if (fin.width !== WIDTH || fin.height !== HEIGHT) finalProblems.push(`final is ${fin.width}x${fin.height}`);
if (fin.frames !== src.frames) finalProblems.push(`final has ${fin.frames} frames, the source ${src.frames}`);
if (fin.audio.length !== src.audio.length || fin.audio.some((a, k) => a.codec !== src.audio[k].codec || a.rate !== src.audio[k].rate)) finalProblems.push("the audio is not the source's");
if (Math.abs(fin.duration - src.duration) > 1 / src.fps + 0.05) finalProblems.push(`final lasts ${fin.duration.toFixed(3)} s, the source ${src.duration.toFixed(3)} s`);
if (finalProblems.length && !F["allow-mismatch"]) {
  logLine(entryOf({ charged, outputs: [muxed], ok: false, note: `final check failed, not placed: ${finalProblems.join("; ")}` }));
  fail(`final check failed (kept in ${muxed}):\n  ${finalProblems.join("\n  ")}`);
}
placeNew(muxed, OUT);
say(`done    ${OUT}`);
say(`        ${fin.width}x${fin.height} ${fin.vcodec} ${fin.fpsText} fps, ${fin.frames} frames (source ${src.frames}), ${fin.duration.toFixed(3)} s, ${(fs.statSync(OUT).size / 1e6).toFixed(1)} MB; audio copied: ${fin.audio.map((a) => `${a.codec} ${a.rate} Hz ${a.channels} ch`).join(", ") || "none"}`);
say(`        charged ${usd(charged)}${costReported ? "" : " (a part's cost was not reported: read the account)"}; estimate was ${usd(est.expected)}`);
record.final = { out: OUT, charged, costReported, probe: fin };
saveRecord();
logLine(entryOf({ charged, outputs: [OUT], ok: true, note: null }));

function entryOf({ charged, outputs, ok, note }) {
  return {
    plan_step: Number(F["plan-step"] ?? 11),
    plan_label: null,
    at: new Date().toISOString(),
    lane: typeof F.lane === "string" ? F.lane : "finishing",
    by: null,
    shot: typeof F.shot === "string" ? F.shot : null,
    arm: "runware",
    tool: `topaz4k.mjs --target ${T.name} (raw upscale through the private Titanium app; input via /api/blob/upload)`,
    model: "Topaz Proteus 4",
    air: AIR,
    inputs: [SRC],
    prompt: null,
    quote: +est.expected.toFixed(4),
    charged,
    outputs,
    decision: ok
      ? `the finished cut upscaled to ${WIDTH}x${HEIGHT} with Topaz Proteus 4 on Runware (${results.length} task${results.length > 1 ? "s, joined by stream copy" : ""}), outputQuality ${QUALITY}, fps left at the source's; the source's own audio muxed back with -c:a copy`
      : "Topaz Proteus 4 upscale of the finished cut did not finish cleanly",
    change: ok ? `new 4K master beside the 1080p cut (${path.basename(SRC)} kept unchanged)` : null,
    note: [note, `task ${(record.tasks ?? []).map((t) => t?.id).filter(Boolean).join(", ")}`, `inputs on the store: ${(record.tasks ?? []).map((t) => t?.input).filter(Boolean).join(", ") || "(resumed)"}`, ok ? `checked: ffprobe ${WIDTH}x${HEIGHT}, ${src.frames} frames as the source, ${src.fpsText} fps, audio ${src.audio.map((a) => a.codec).join("+") || "none"} copied` : null, `work ${WORK}`].filter(Boolean).join("; "),
    screens: [],
    clips: [],
  };
}
