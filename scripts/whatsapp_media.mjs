#!/usr/bin/env node
// Make WhatsApp copies of a formula-sheet SVG: a full-size JPG still, a looping
// MP4 (1080 px wide, at least 10 s) and a short GIF (720 px wide).
//
//   node scripts/whatsapp_media.mjs s2/science-formula-sheets/svg/science-diagram-xx-xy.svg:6
//   node scripts/whatsapp_media.mjs path/to/static.svg            # no :seconds = JPG only
//
// The number after the colon is the length of one animation loop in seconds
// (every animation in the SVG must repeat evenly inside it, so the GIF loops
// without a jump). Output goes to s2/science-formula-sheets/whatsapp/ unless
// --out DIR is given. Those files are git-ignored: they are local copies.
//
// No npm packages: Node 22 (built-in WebSocket and fetch), Google Chrome,
// ffmpeg and gifski (brew install ffmpeg gifski).
import { spawn, execFileSync } from "node:child_process";
import { mkdtempSync, readFileSync, writeFileSync, rmSync, mkdirSync } from "node:fs";
import { tmpdir } from "node:os";
import path from "node:path";
import { pathToFileURL, fileURLToPath } from "node:url";

const ROOT = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");
const CHROME = process.env.CHROME || "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome";
const MP4_FPS = 30, GIF_FPS = 15, GIF_WIDTH = 720, MIN_MP4_SECONDS = 10;

const args = process.argv.slice(2);
let outDir = path.join(ROOT, "s2/science-formula-sheets/whatsapp");
const jobs = [];
for (let i = 0; i < args.length; i++) {
  if (args[i] === "--out") { outDir = path.resolve(args[++i]); continue; }
  const m = args[i].match(/^(.*\.svg)(?::([\d.]+))?$/);
  if (!m) { console.error(`not an .svg[:seconds] argument: ${args[i]}`); process.exit(2); }
  jobs.push({ svg: path.resolve(m[1]), loop: m[2] ? Number(m[2]) : 0 });
}
if (!jobs.length) { console.error("usage: whatsapp_media.mjs file.svg[:loopSeconds] ... [--out DIR]"); process.exit(2); }
mkdirSync(outDir, { recursive: true });

const port = 9300 + Math.floor(Math.random() * 500);
const profile = mkdtempSync(path.join(tmpdir(), "wa-chrome-"));
const chrome = spawn(CHROME, ["--headless=new", "--disable-gpu", "--hide-scrollbars", `--remote-debugging-port=${port}`,
  `--user-data-dir=${profile}`, "about:blank"], { stdio: "ignore" });

async function waitForChrome() {
  for (let i = 0; i < 100; i++) {
    try { return await (await fetch(`http://127.0.0.1:${port}/json/version`)).json(); }
    catch { await new Promise(r => setTimeout(r, 100)); }
  }
  throw new Error("Chrome did not start");
}

function cdp(wsUrl) {
  const ws = new WebSocket(wsUrl); let id = 0; const pending = new Map(); const waiters = [];
  ws.onmessage = ev => {
    const msg = JSON.parse(ev.data);
    if (msg.id && pending.has(msg.id)) {
      const { res, rej } = pending.get(msg.id); pending.delete(msg.id);
      msg.error ? rej(new Error(msg.error.message)) : res(msg.result);
    } else if (msg.method) {
      for (const w of waiters.splice(0)) if (w.method === msg.method) w.res(msg.params); else waiters.push(w);
    }
  };
  const ready = new Promise(r => (ws.onopen = r));
  return {
    ready,
    send: (method, params = {}) => new Promise((res, rej) => { const i = ++id; pending.set(i, { res, rej }); ws.send(JSON.stringify({ id: i, method, params })); }),
    once: method => new Promise(res => waiters.push({ method, res })),
    close: () => ws.close(),
  };
}

const run = (cmd, a) => execFileSync(cmd, a, { stdio: ["ignore", "ignore", "inherit"] });

try {
  await waitForChrome();
  const target = await (await fetch(`http://127.0.0.1:${port}/json/new?about:blank`, { method: "PUT" })).json();
  const page = cdp(target.webSocketDebuggerUrl); await page.ready;
  await page.send("Page.enable");

  for (const { svg, loop } of jobs) {
    const src = readFileSync(svg, "utf8");
    const w = Number(src.match(/<svg[^>]*\swidth="(\d+)"/)[1]), h = Number(src.match(/<svg[^>]*\sheight="(\d+)"/)[1]);
    const base = path.basename(svg, ".svg");
    await page.send("Emulation.setDeviceMetricsOverride", { width: w, height: h, deviceScaleFactor: 1, mobile: false });
    const loaded = page.once("Page.loadEventFired");
    await page.send("Page.navigate", { url: pathToFileURL(svg).href });
    await loaded;
    await page.send("Runtime.evaluate", { expression: "document.fonts ? document.fonts.ready.then(() => true) : true", awaitPromise: true });

    const frames = mkdtempSync(path.join(tmpdir(), `wa-${base}-`));
    const n = loop ? Math.round(loop * MP4_FPS) : 1;
    for (let f = 0; f < n; f++) {
      const t = f / MP4_FPS;
      await page.send("Runtime.evaluate", { expression: `(() => { const s = document.documentElement; s.pauseAnimations(); s.setCurrentTime(${t}); return new Promise(r => requestAnimationFrame(() => requestAnimationFrame(r))); })()`, awaitPromise: true });
      const { data } = await page.send("Page.captureScreenshot", { format: "png" });
      writeFileSync(path.join(frames, `f${String(f).padStart(4, "0")}.png`), Buffer.from(data, "base64"));
    }

    const jpg = path.join(outDir, `${base}.jpg`);
    run("ffmpeg", ["-y", "-loglevel", "error", "-i", path.join(frames, "f0000.png"), "-q:v", "2", jpg]);
    const made = [path.relative(ROOT, jpg)];
    if (loop) {
      const reps = Math.max(1, Math.ceil(MIN_MP4_SECONDS / loop));
      const mp4 = path.join(outDir, `${base}.mp4`);
      run("ffmpeg", ["-y", "-loglevel", "error", "-stream_loop", String(reps - 1), "-framerate", String(MP4_FPS),
        "-i", path.join(frames, "f%04d.png"), "-c:v", "libx264", "-pix_fmt", "yuv420p", "-crf", "20",
        "-movflags", "+faststart", mp4]);
      const step = MP4_FPS / GIF_FPS;
      const gifFrames = Array.from({ length: Math.floor(n / step) }, (_, i) => path.join(frames, `f${String(i * step).padStart(4, "0")}.png`));
      const gif = path.join(outDir, `${base}.gif`);
      run("gifski", ["--quiet", "--fps", String(GIF_FPS), "--width", String(GIF_WIDTH), "--quality", "80", "-o", gif, ...gifFrames]);
      made.push(path.relative(ROOT, mp4), path.relative(ROOT, gif));
    }
    rmSync(frames, { recursive: true, force: true });
    console.log(`${base}: ${made.join(", ")}`);
  }
  page.close();
} finally {
  chrome.kill();
  setTimeout(() => rmSync(profile, { recursive: true, force: true }), 500);
}
