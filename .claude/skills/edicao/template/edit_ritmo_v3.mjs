// Edição v3 (sobre a v2 aprovada): sem silêncio, fala 1,12x, legenda serifada estática no centro,
// light leak em 2 trocas. Corrige as travadas da v2: trim no filtro (sem -ss antes do -i), padding
// 0,05/0,11, ilha de fala < 0,4s junta com a vizinha, ruído sem palavra fora, 30fps por minterpolate
// POR SEGMENTO (no vídeo inteiro ele interpola através do corte e cria um quadro fantasma)
// e, no take-herói, a pausa é ACELERADA (rampa) em vez de cortada, para o reveal não pular.
// Entrada: assets/tNN.mp4, roteiro.json (lista com a fala literal de cada take) e fonts/Merriweather900.woff2.
// Antes: python3 palavras.py words_takes.json assets/t01.mp4 ... (tempo por palavra de cada take).
// Ajuste TAKES, RAMP (take-herói), LEAKS e UP para o vídeo. Leva ~7 min (minterpolate) para 50s de takes.
import fs from "node:fs";
import { execFileSync } from "node:child_process";

const SP = 1.12, GAP = 0.15, PAD_IN = 0.05, PAD_OUT = 0.11, MIN_ISLAND = 0.4, W = 1080, H = 1920;
const TAKES = fs.readdirSync("assets").map(f => f.match(/^t(\d+)\.mp4$/)).filter(Boolean).map(m => +m[1]).sort((a, b) => a - b);
const RAMP = { 1: 5 };      // take-herói: pausas aceleradas Nx em vez de cortadas
const LEAKS = [2, 4];       // light leak na entrada destes takes
const UP = [1];             // legenda mais alta nestes takes (herói visual embaixo)
const sh = c => execFileSync("sh", ["-c", c], { maxBuffer: 1 << 26 }).toString();
const words = JSON.parse(fs.readFileSync("words_takes.json", "utf8"));
const roteiro = JSON.parse(fs.readFileSync("roteiro.json", "utf8"));

const segs = [];
for (const k of TAKES) {
  const f = `assets/t${String(k).padStart(2, "0")}.mp4`;
  const dur = +sh(`ffprobe -v error -show_entries format=duration -of csv=p=0 ${f}`);
  const log = sh(`ffmpeg -hide_banner -i ${f} -af silencedetect=noise=-35dB:d=${GAP} -f null - 2>&1`);
  const sil = []; let st = null;
  for (const m of log.matchAll(/silence_(start|end): ([\d.]+)/g)) { if (m[1] === "start") st = +m[2]; else { sil.push([st, +m[2]]); st = null; } }
  if (st !== null) sil.push([st, dur]);
  // ilhas de som entre silêncios
  let isl = [], pos = 0;
  for (const [a, b] of sil) { if (a - pos > 0.02) isl.push([pos, a]); pos = b; }
  if (dur - pos > 0.02) isl.push([pos, dur]);
  // ruído: ilha sem nenhuma palavra do whisper fora
  const ws = words[k];
  isl = isl.filter(([a, b]) => ws.some(([, wa, wb]) => wb > a + 0.03 && wa < b - 0.03));
  // ilha curta junta com a vizinha (a pausa entre elas fica)
  const merged = [];
  for (const i of isl) {
    const last = merged.at(-1);
    if (last && (i[1] - i[0] < MIN_ISLAND || last[1] - last[0] < MIN_ISLAND)) last[1] = i[1]; else merged.push([...i]);
  }
  const sp = merged.map(([a, b]) => [Math.max(0, a - PAD_IN), Math.min(dur, b + PAD_OUT)]);
  sp.forEach(([a, b], j) => {
    segs.push({ k, a, b, sp: SP });
    const nx = sp[j + 1];
    if (RAMP[k] && nx && nx[0] > b) segs.push({ k, a: b, b: nx[0], sp: RAMP[k], mute: true });
  });
}
let o = 0; segs.forEach(s => { s.o = o; s.d = (s.b - s.a) / s.sp; o += s.d; });
const TOTAL = +o.toFixed(3);

const ins = TAKES.flatMap(k => ["-i", `assets/t${String(k).padStart(2, "0")}.mp4`]);
let f = "";
segs.forEach((s, i) => {
  const n = TAKES.indexOf(s.k);
  f += `[${n}:v]trim=start=${s.a.toFixed(3)}:end=${s.b.toFixed(3)},setpts=(PTS-STARTPTS)/${s.sp},minterpolate=fps=30:mi_mode=mci:mc_mode=aobmc:me_mode=bidir:vsbmc=1:scd=none,scale=${W}:${H}:flags=lanczos,setsar=1[v${i}];`;
  f += s.mute
    ? `aevalsrc=0:d=${s.d.toFixed(4)}:s=44100,aformat=sample_rates=44100:channel_layouts=mono[a${i}];`
    : `[${n}:a]atrim=start=${s.a.toFixed(3)}:end=${s.b.toFixed(3)},asetpts=PTS-STARTPTS,atempo=${s.sp},aformat=sample_rates=44100:channel_layouts=mono,afade=t=in:d=0.012,afade=t=out:st=${Math.max(0, s.d - 0.02).toFixed(3)}:d=0.02[a${i}];`;
});
f += segs.map((_, i) => `[v${i}][a${i}]`).join("") + `concat=n=${segs.length}:v=1:a=1[vc][ac];`;
f += `[vc]null[v];[ac]loudnorm=I=-14:TP=-1.2,aresample=44100[a]`;
execFileSync("ffmpeg", ["-y", "-loglevel", "error", ...ins, "-filter_complex", f, "-map", "[v]", "-map", "[a]",
  "-c:v", "libx264", "-crf", "16", "-preset", "medium", "-pix_fmt", "yuv420p", "-g", "15", "-r", "30", "-c:a", "pcm_s16le", "assets/base.mov"]);
execFileSync("ffmpeg", ["-y", "-loglevel", "error", "-i", "assets/base.mov", "-an", "-c:v", "copy", "assets/base.mp4"]);
execFileSync("ffmpeg", ["-y", "-loglevel", "error", "-i", "assets/base.mov", "-vn", "-ar", "44100", "-ac", "1", "assets/mix.wav"]);

// legenda: tempo do whisper no vídeo JÁ cortado, texto do roteiro (o roteiro manda na escuta)
sh(`ffmpeg -y -loglevel error -i assets/base.mov -ar 16000 -ac 1 base16.wav && python3 palavras.py basew.json base16.wav --flat`);
const heard = JSON.parse(fs.readFileSync("basew.json", "utf8"));
const script = roteiro.join(" ").split(/\s+/);
if (heard.length !== script.length) console.warn(`AVISO: ouvi ${heard.length} palavras, roteiro tem ${script.length}; legenda usa o que ouvi`);
const segAt = t => segs.find(s => t >= s.o && t < s.o + s.d) || segs.at(-1);
const ws = heard.map(([w, a], i) => ({ w: heard.length === script.length ? script[i] : w, t: a, k: segAt(a + 0.05).k }));
const pages = []; let cur = [];
ws.forEach((w, i) => { cur.push(w); const nx = ws[i + 1];
  if (!nx || cur.length >= 3 || /[.!?]$/.test(w.w) || (/,$/.test(w.w) && cur.length >= 2) || nx.k !== w.k) { pages.push(cur); cur = []; } });
const html = [], js = [];
pages.forEach((p, n) => {
  const st = n === 0 ? 0 : p[0].t, en = n < pages.length - 1 ? pages[n + 1][0].t : TOTAL;
  const txt = p.map(w => w.w.replace(/[.,!?]$/, "")).join(" ").toLowerCase();
  html.push(`<div class="clip cap${UP.includes(p[0].k) ? " up" : ""}" id="cp${n}" data-start="${st.toFixed(3)}" data-duration="${(en - st).toFixed(3)}" data-track-index="${2 + (n % 2)}"><div class="capin">${txt}</div></div>`);
});
segs.forEach((s, i) => { if (i > 0 && segs[i - 1].k !== s.k && LEAKS.includes(s.k)) {
  const t = Math.max(0, s.o - 0.12);
  html.push(`<div class="clip leak" id="lk${i}" data-start="${t.toFixed(3)}" data-duration="0.5" data-track-index="5"></div>`);
  js.push(`tl.fromTo("#lk${i}", { opacity: 0 }, { opacity: 0.85, duration: 0.14, ease: "power2.out" }, ${t.toFixed(3)});`);
  js.push(`tl.to("#lk${i}", { opacity: 0, duration: 0.34, ease: "power2.in" }, ${(t + 0.16).toFixed(3)});`);
} });

fs.writeFileSync("index.html", `<!doctype html>
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
<audio id="mix" src="assets/mix.wav" data-start="0" data-duration="${TOTAL}" data-track-index="9" data-volume="1"></audio>
</div>
<script>
const tl = gsap.timeline({ paused: true });
${js.join("\n")}
window.__timelines["main"] = tl;
</script>
</body>
</html>
`);
fs.writeFileSync("segs.json", JSON.stringify(segs, null, 1));
console.log(`ok · ${segs.length} segmentos (${segs.filter(s => s.mute).length} rampas) · menor ${Math.min(...segs.filter(s=>!s.mute).map(s => s.d)).toFixed(2)}s · ${pages.length} legendas · ${TOTAL}s · ${(ws.length / TOTAL).toFixed(2)} palavras/s`);
