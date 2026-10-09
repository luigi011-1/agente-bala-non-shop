// Edição v2 no estilo da referência (Holistic Brandon): sem silêncio, fala 1,3x, cortes secos,
// legenda serifada minúscula estática no meio da tela, light leak laranja em algumas trocas, música baixa.
// node edit2.mjs  → assets/base.mp4 (vídeo+voz cortados e acelerados), assets/mix2.wav, index.html
import fs from "node:fs";
import { execFileSync } from "node:child_process";

const SP = 1.12, GAP = 0.15, PAD_IN = 0.03, PAD_OUT = 0.07, W = 1080, H = 1920;
const LEAKS = [2, 4]; // light leak na entrada destes takes

const take = k => JSON.parse(fs.readFileSync(`../words/t${k}.json`, "utf8")).transcription
  .map(s => ({ w: s.text.trim(), a: s.offsets.from / 1000, b: s.offsets.to / 1000 })).filter(x => x.w);

// segmentos pelos silêncios reais do áudio (silencedetect); o whisper estica as palavras e esconde pausas
const DUR = { 1: 10.03, 2: 10.0, 3: 10.0, 4: 10.0, 5: 10.0 };
const segs = [];
for (let k = 1; k <= 5; k++) {
  const log = execFileSync("ffmpeg", ["-hide_banner", "-i", `assets/t0${k}.mp4`, "-af", `silencedetect=noise=-35dB:d=${GAP}`, "-f", "null", "-"], { stdio: ["ignore", "pipe", "pipe"] }).toString()
    + "";
  const err = execFileSync("sh", ["-c", `ffmpeg -hide_banner -i assets/t0${k}.mp4 -af silencedetect=noise=-35dB:d=${GAP} -f null - 2>&1`]).toString();
  const sil = []; let st = null;
  for (const m of err.matchAll(/silence_(start|end): ([\d.]+)/g)) { if (m[1] === "start") st = +m[2]; else { sil.push([st, +m[2]]); st = null; } }
  if (st !== null) sil.push([st, DUR[k]]);
  let pos = 0;
  for (const [a, b] of sil) { if (a - pos > 0.08) segs.push({ k, a: Math.max(0, pos - PAD_IN), b: Math.min(DUR[k], a + PAD_OUT) }); pos = b; }
  if (DUR[k] - pos > 0.08) segs.push({ k, a: Math.max(0, pos - PAD_IN), b: DUR[k] });
}
let o = 0; segs.forEach(s => { s.o = o; s.d = (s.b - s.a) / SP; o += s.d; });
const TOTAL = +o.toFixed(3);

// base.mp4: corta, acelera e concatena (vídeo + voz)
const args = ["-y", "-loglevel", "error"]; let f = "";
segs.forEach((s, i) => {
  args.push("-ss", s.a.toFixed(3), "-t", (s.b - s.a).toFixed(3), "-i", `assets/t0${s.k}.mp4`);
  f += `[${i}:v]setpts=(PTS-STARTPTS)/${SP},scale=${W}:${H}:flags=lanczos,fps=30,setsar=1[v${i}];[${i}:a]asetpts=PTS-STARTPTS,atempo=${SP},aformat=sample_rates=44100:channel_layouts=mono,afade=t=in:d=0.01,afade=t=out:st=${Math.max(0, s.d - 0.015).toFixed(3)}:d=0.015[a${i}];`;
});
f += segs.map((_, i) => `[v${i}][a${i}]`).join("") + `concat=n=${segs.length}:v=1:a=1[v][a]`;
execFileSync("ffmpeg", [...args, "-filter_complex", f, "-map", "[v]", "-map", "[a]", "-c:v", "libx264", "-crf", "16", "-preset", "medium", "-pix_fmt", "yuv420p", "-g", "15", "-c:a", "pcm_s16le", "assets/base.mov"]);

// mix: voz + lofi baixo com ducking
execFileSync("ffmpeg", ["-y", "-loglevel", "error", "-i", "assets/base.mov", "-ss", "15.93", "-i", "../sfx/lofi.mp3", "-filter_complex",
  `[0:a]loudnorm=I=-14:TP=-1.2,asplit=2[voz][key];[1:a]atrim=0:${TOTAL},aformat=sample_rates=44100:channel_layouts=mono,volume=0.22,afade=t=out:st=${(TOTAL - 0.8).toFixed(2)}:d=0.8[mus];[mus][key]sidechaincompress=threshold=0.04:ratio=4:attack=15:release=250[duck];[voz][duck]amix=inputs=2:normalize=0,atrim=0:${TOTAL},alimiter=limit=0.95[o]`,
  "-map", "[o]", "-ar", "44100", "-ac", "1", "assets/mix2.wav"]);
execFileSync("ffmpeg", ["-y", "-loglevel", "error", "-i", "assets/base.mov", "-an", "-c:v", "copy", "assets/base.mp4"]);

// legendas a partir da transcrição do próprio vídeo cortado (tempo exato da saída)
execFileSync("sh", ["-c", `ffmpeg -y -loglevel error -i assets/base.mov -ar 16000 -ac 1 /tmp/base16.wav && whisper-cli -m ~/.cache/agente-bala/models/ggml-small.en.bin -f /tmp/base16.wav -l en -ml 1 -sow -ojf -of /tmp/basew >/dev/null 2>&1`]);
const takeAt = t => (segs.find(s => t >= s.o && t < s.o + s.d) || segs.at(-1)).k;
const words = JSON.parse(fs.readFileSync("/tmp/basew.json", "utf8")).transcription.map(s => ({ w: s.text.trim(), t: s.offsets.from / 1000 })).filter(x => /[a-z0-9]/i.test(x.w)).map(x => ({ ...x, k: takeAt(x.t + 0.05) }));
// correções de escuta (o roteiro manda): "simmer for a cup" → "simmer, pour a cup"
const FIX = { "simmer|for": "pour" };
words.forEach((w, i) => { const prev = words[i - 1]; if (prev && FIX[prev.w.toLowerCase().replace(/[^a-z]/g, "") + "|" + w.w.toLowerCase()]) w.w = FIX[prev.w.toLowerCase().replace(/[^a-z]/g, "") + "|" + w.w.toLowerCase()]; });
// legendas: 2-3 palavras, minúsculas, estáticas, troca a cada página
const pages = []; let cur = [];
words.forEach((w, i) => { cur.push(w); const nx = words[i + 1];
  const cross = nx && segs.some((s, j) => j > 0 && segs[j - 1].k !== s.k && s.o > w.t && s.o <= nx.t + 0.02);
  if (!nx || cur.length >= 3 || /[.!?]$/.test(w.w) || (/,$/.test(w.w) && cur.length >= 2) || cross) { pages.push(cur); cur = []; } });
const html = [], js = [];
pages.forEach((p, n) => {
  const st = p[0].t, en = n < pages.length - 1 ? pages[n + 1][0].t : TOTAL;
  const txt = p.map(w => w.w.replace(/[.,!?]$/, "")).join(" ").toLowerCase();
  const up = p[0].k === 1 ? " up" : "";
  html.push(`<div class="clip cap${up}" id="cp${n}" data-start="${st.toFixed(3)}" data-duration="${(en - st).toFixed(3)}" data-track-index="${2 + (n % 2)}"><div class="capin">${txt}</div></div>`);
});
// light leak nas trocas escolhidas
segs.forEach((s, i) => { if (i > 0 && segs[i - 1].k !== s.k && LEAKS.includes(s.k)) {
  const t = s.o - 0.12;
  html.push(`<div class="clip leak" id="lk${i}" data-start="${t.toFixed(3)}" data-duration="0.5" data-track-index="5"></div>`);
  js.push(`tl.fromTo("#lk${i}", { opacity: 0 }, { opacity: 0.85, duration: 0.14, ease: "power2.out" }, ${t.toFixed(3)});`);
  js.push(`tl.to("#lk${i}", { opacity: 0, duration: 0.34, ease: "power2.in" }, ${(t + 0.16).toFixed(3)});`);
} });

const page = `<!doctype html>
<html lang="en" data-resolution="portrait">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=${W}, height=${H}" />
<script src="https://cdn.jsdelivr.net/npm/gsap@3.14.2/dist/gsap.min.js"></script>
<style>
@font-face { font-family: "Merriweather"; src: url("fonts/Merriweather900.woff2") format("woff2"); font-weight: 900; }
* { margin: 0; padding: 0; box-sizing: border-box; }
html, body { width: ${W}px; height: ${H}px; overflow: hidden; background: #000; }
#root { position: relative; width: 100%; height: 100%; overflow: hidden; }
.base { position: absolute; inset: 0; width: 100%; height: 100%; object-fit: cover; }
.cap { position: absolute; left: 0; right: 0; top: 880px; display: flex; justify-content: center; padding: 0 70px; z-index: 10; }
.cap.up { top: 760px; }
.capin { font-family: "Merriweather", serif; font-weight: 900; font-size: 64px; color: #fff; text-align: center; line-height: 1.15; letter-spacing: -0.01em;
  text-shadow: 0 3px 10px rgba(0,0,0,0.55), 0 0 2px rgba(0,0,0,0.6); }
.leak { position: absolute; inset: 0; z-index: 8; mix-blend-mode: screen; opacity: 0;
  background: radial-gradient(70% 55% at 20% 70%, rgba(255,110,40,0.95), rgba(255,60,20,0.5) 45%, rgba(255,40,0,0) 75%), linear-gradient(180deg, rgba(255,140,60,0.55), rgba(255,60,30,0.3)); }
</style>
</head>
<body>
<div id="root" data-composition-id="main" data-start="0" data-width="${W}" data-height="${H}" data-duration="${TOTAL}">
<video class="clip base" id="base" src="assets/base.mp4" muted playsinline data-start="0" data-duration="${TOTAL}" data-track-index="0"></video>
${html.join("\n")}
<audio id="mix" src="assets/mix2.wav" data-start="0" data-duration="${TOTAL}" data-track-index="9" data-volume="1"></audio>
</div>
<script>
const tl = gsap.timeline({ paused: true });
${js.join("\n")}
window.__timelines["main"] = tl;
</script>
</body>
</html>
`;
fs.writeFileSync("index.html", page);
const wps = (words.length / TOTAL).toFixed(2);
console.log(`ok · ${segs.length} cortes · ${pages.length} legendas · ${TOTAL}s · ${wps} palavras/s`);
