// Edição dopaminérgica: jump cuts, zoom alternado, legenda palavra por palavra, pop-ups, SFX, música com ducking.
// node edit.mjs  (lê edit.json + ../words/t*.json, escreve index.html e assets/mix.wav)
import fs from "node:fs";
import { execFileSync } from "node:child_process";

const W = 1080, H = 1920, Y = "#FFE14D", G = "#3CFF8F";
const cfg = JSON.parse(fs.readFileSync("edit.json", "utf8"));
const norm = w => w.toLowerCase().replace(/[^a-z0-9']/g, "");
const isKey = w => cfg.destaques.includes(norm(w));

const takeWords = {};
for (let k = 1; k <= 5; k++) takeWords[k] = JSON.parse(fs.readFileSync(`../words/t${k}.json`, "utf8")).transcription
  .map(s => ({ w: s.text.trim(), a: s.offsets.from / 1000, b: s.offsets.to / 1000 })).filter(x => x.w);

// linha do tempo de saída
let o = 0; const segs = cfg.segmentos.map(([k, a, b], i) => { const s = { i, k, a, b, o, d: b - a }; o += s.d; return s; });
const TOTAL = +o.toFixed(3);
const words = [];
for (const s of segs) for (const w of takeWords[s.k]) if (w.a >= s.a - 0.02 && w.a < s.b - 0.05)
  words.push({ ...w, t: s.o + Math.max(0, w.a - s.a), te: s.o + Math.min(w.b, s.b) - s.a, seg: s.i });

// páginas de legenda: até 3 palavras, quebra em pontuação, pausa ou troca de segmento
const pages = []; let cur = [];
words.forEach((w, i) => { cur.push(w); const nx = words[i + 1];
  if (!nx || cur.length >= 3 || /[.,]$/.test(w.w) || nx.seg !== w.seg || nx.t - w.te > 0.3) { pages.push(cur); cur = []; } });

const html = [], js = [], sfx = [];
// vídeos
segs.forEach(s => {
  const z = s.i % 2 ? 1.17 : 1.0;
  html.push(`<div class="vw" id="vw${s.i}"><video class="clip vid" id="v${s.i}" src="assets/t0${s.k}.mp4" muted playsinline data-start="${s.o.toFixed(3)}" data-duration="${s.d.toFixed(3)}" data-media-start="${s.a.toFixed(3)}" data-track-index="${s.i % 2}"></video></div>`);
  const from = s.i === 0 ? 1.35 : z + 0.09;
  js.push(`tl.fromTo("#vw${s.i}", { scale: ${from} }, { scale: ${z}, duration: ${s.i === 0 ? 0.7 : 0.22}, ease: "power3.out" }, ${s.o.toFixed(3)});`);
  const takeChange = s.i > 0 && segs[s.i - 1].k !== s.k;
  if (takeChange) {
    html.push(`<div class="clip flash" id="fl${s.i}" data-start="${s.o.toFixed(3)}" data-duration="0.16" data-track-index="8"></div>`);
    js.push(`tl.fromTo("#fl${s.i}", { opacity: 0.9 }, { opacity: 0, duration: 0.16, ease: "power2.out" }, ${s.o.toFixed(3)});`);
    sfx.push(["whoosh", s.o - 0.12, 0.7]);
  } else if (s.i > 0) sfx.push(["pop", s.o, 0.22]);
});

// legenda
pages.forEach((p, n) => {
  const st = p[0].t - 0.04, en = n < pages.length - 1 ? pages[n + 1][0].t - 0.04 : TOTAL;
  const up = segs[p[0].seg].k === 1 ? " up" : "";
  html.push(`<div class="clip cap${up}" id="cp${n}" data-start="${st.toFixed(3)}" data-duration="${(en - st).toFixed(3)}" data-track-index="5"><div class="capin">${p.map((w, j) =>
    `<span class="cw ${isKey(w.w) ? "k" : ""}" id="cw${n}_${j}">${w.w.replace(/[.,]$/, "").toUpperCase()}</span>`).join(" ")}</div></div>`);
  p.forEach((w, j) => js.push(`tl.fromTo("#cw${n}_${j}", { opacity: 0, scale: 0.55, y: 24 }, { opacity: 1, scale: ${isKey(w.w) ? 1.12 : 1}, y: 0, duration: 0.18, ease: "back.out(3)" }, ${(w.t - 0.03).toFixed(3)});`));
});

// gancho
html.push(`<div class="clip hook" id="hook" data-start="0.05" data-duration="2.85" data-track-index="6"><div class="hookin" id="hookin">${cfg.hook}</div></div>`);
js.push(`tl.fromTo("#hookin", { opacity: 0, scale: 1.6, rotation: -6 }, { opacity: 1, scale: 1, rotation: -3, duration: 0.35, ease: "back.out(2.4)" }, 0.08);`);
js.push(`tl.to("#hookin", { scale: 1.06, duration: 0.3, yoyo: true, repeat: 3, ease: "sine.inOut" }, 0.6);`);
js.push(`tl.to("#hookin", { opacity: 0, y: -40, duration: 0.2 }, 2.65);`);
sfx.push(["impact", 0.05, 0.6]);

// pop-ups de lista (ingredientes / benefícios), acumulando no canto
const findWord = (key, after = 0) => words.find(w => norm(w.w) === key && w.t >= after);
const stack = (list, color, num, id) => {
  const ts = []; let after = 0;
  list.forEach(([key]) => { const w = findWord(key, after); ts.push(w ? w.t : after + 1); after = (w ? w.t : after) + 0.01; });
  const seg = segs.find(s => s.o <= ts[0] && ts[0] < s.o + s.d), takeEnd = segs.filter(s => s.k === seg.k).at(-1);
  const end = takeEnd.o + takeEnd.d;
  html.push(`<div class="clip stack" id="${id}" data-start="${(ts[0] - 0.1).toFixed(3)}" data-duration="${(end - ts[0] + 0.1).toFixed(3)}" data-track-index="7">${list.map(([, lab], j) =>
    `<div class="chip" id="${id}${j}"><span class="badge" style="background:${color}">${num ? j + 1 : "✓"}</span>${lab}</div>`).join("")}</div>`);
  ts.forEach((t, j) => { js.push(`tl.fromTo("#${id}${j}", { opacity: 0, x: -260, scale: 0.8 }, { opacity: 1, x: 0, scale: 1, duration: 0.28, ease: "back.out(2)" }, ${(t - 0.05).toFixed(3)});`); sfx.push(["ding", t - 0.02, 0.45]); });
  return end;
};
stack(cfg.ingredientes, "#FF7A1A", true, "ing");
const benEnd = stack(cfg.beneficios, "#18B26B", false, "ben");
const benStart = findWord(cfg.beneficios[0][0]).t;
sfx.push(["riser", benStart - 1.25, 0.5]);

// impacto + tremor de câmera
const imp = findWord(cfg.impacto);
if (imp) {
  sfx.push(["impact", imp.t, 0.9]);
  const sh = [[-14, 8], [12, -10], [-9, 6], [7, -5], [-4, 3], [0, 0]];
  sh.forEach(([x, y], j) => js.push(`tl.to("#cam", { x: ${x}, y: ${y}, duration: 0.035, ease: "none" }, ${(imp.t + j * 0.035).toFixed(3)});`));
}

// CTA
const lk = findWord("link"), fw = findWord("follow");
if (lk) {
  html.push(`<div class="clip ctachip" id="lk" data-start="${(lk.t - 0.05).toFixed(3)}" data-duration="${(fw.t - lk.t).toFixed(3)}" data-track-index="7"><div class="lkin" id="lkin">LINK IN CAPTION <svg viewBox="0 0 24 24" width="54" height="54" fill="none" stroke="#111" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><path d="M12 5v14M5 12l7 7 7-7"/></svg></div></div>`);
  js.push(`tl.fromTo("#lkin", { opacity: 0, y: -60 }, { opacity: 1, y: 0, duration: 0.3, ease: "back.out(2)" }, ${lk.t.toFixed(3)});`);
  js.push(`tl.to("#lkin svg", { y: 14, duration: 0.25, yoyo: true, repeat: 7, ease: "sine.inOut" }, ${(lk.t + 0.3).toFixed(3)});`);
  sfx.push(["pop", lk.t, 0.5]);
}
if (fw) {
  html.push(`<div class="clip follow" id="fwb" data-start="${(fw.t - 0.05).toFixed(3)}" data-duration="${(TOTAL - fw.t + 0.05).toFixed(3)}" data-track-index="7"><div class="fwin" id="fwin"><span class="plus">+</span>${cfg.cta}</div></div>`);
  js.push(`tl.fromTo("#fwin", { opacity: 0, scale: 0.4 }, { opacity: 1, scale: 1, duration: 0.3, ease: "back.out(2.6)" }, ${fw.t.toFixed(3)});`);
  js.push(`tl.to("#fwin", { scale: 1.08, duration: 0.22, yoyo: true, repeat: 5, ease: "sine.inOut" }, ${(fw.t + 0.35).toFixed(3)});`);
  sfx.push(["pop", fw.t, 0.6], ["ding", fw.t + 0.05, 0.4]);
}

// progresso
js.push(`tl.fromTo("#prog", { scaleX: 0 }, { scaleX: 1, duration: ${TOTAL}, ease: "none" }, 0);`);

// ---------- áudio ----------
const S = "../sfx/";
const args = ["-y", "-loglevel", "error"];
segs.forEach(s => args.push("-i", `assets/t0${s.k}.mp4`));
const nV = segs.length;
args.push("-ss", "15.93", "-i", S + "lofi.mp3");
sfx.forEach(([n]) => args.push("-i", S + n + ".wav"));
let f = segs.map((s, i) => `[${i}:a]atrim=${s.a}:${s.b},asetpts=PTS-STARTPTS,afade=t=in:d=0.012,afade=t=out:st=${(s.d - 0.02).toFixed(3)}:d=0.02,aformat=sample_rates=44100:channel_layouts=mono[a${i}]`).join(";");
f += ";" + segs.map((_, i) => `[a${i}]`).join("") + `concat=n=${nV}:v=0:a=1,loudnorm=I=-15:TP=-1.5,asplit=2[voz][key];`;
f += `[${nV}:a]atrim=0:${TOTAL},aformat=sample_rates=44100:channel_layouts=mono,volume=0.32,afade=t=out:st=${(TOTAL - 1).toFixed(2)}:d=1[mus];[mus][key]sidechaincompress=threshold=0.03:ratio=6:attack=20:release=300[duck];`;
sfx.forEach(([n, t, v], j) => { f += `[${nV + 1 + j}:a]aformat=sample_rates=44100:channel_layouts=mono,volume=${v},adelay=${Math.max(0, Math.round(t * 1000))}:all=1[x${j}];`; });
f += `[voz][duck]${sfx.map((_, j) => `[x${j}]`).join("")}amix=inputs=${2 + sfx.length}:normalize=0,atrim=0:${TOTAL},alimiter=limit=0.95[o]`;
execFileSync("ffmpeg", [...args, "-filter_complex", f, "-map", "[o]", "-ar", "44100", "-ac", "1", "assets/mix.wav"]);

const page = `<!doctype html>
<html lang="en" data-resolution="portrait">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=${W}, height=${H}" />
<script src="https://cdn.jsdelivr.net/npm/gsap@3.14.2/dist/gsap.min.js"></script>
<style>
@font-face { font-family: "Inter"; src: url("fonts/Inter.woff2") format("woff2"); font-weight: 100 900; }
* { margin: 0; padding: 0; box-sizing: border-box; }
html, body { width: ${W}px; height: ${H}px; overflow: hidden; background: #000; }
#root { position: relative; width: 100%; height: 100%; overflow: hidden; font-family: "Inter", sans-serif; }
#cam { position: absolute; inset: -20px; }
.vw { position: absolute; inset: 0; transform-origin: 50% 30%; overflow: hidden; }
.vid { position: absolute; inset: 0; width: 100%; height: 100%; object-fit: cover; }
.flash { position: absolute; inset: 0; background: #fff; z-index: 30; }
.cap { position: absolute; left: 0; right: 0; bottom: 330px; z-index: 20; display: flex; justify-content: center; padding: 0 50px; }
.capin { text-align: center; line-height: 1.05; font-size: 92px; }
.cw { display: inline-block; font-weight: 900; font-size: 92px; color: #fff; letter-spacing: -0.01em; -webkit-text-stroke: 14px #000; paint-order: stroke fill; text-shadow: 0 8px 0 rgba(0,0,0,0.35); }
.cw.k { color: ${Y}; margin: 0 14px; }
.cap.up { bottom: 960px; }
.cw { margin: 0 4px; }
.hook { position: absolute; left: 0; right: 0; top: 600px; z-index: 22; display: flex; justify-content: center; }
.hookin { background: #FF2D55; color: #fff; font-weight: 900; font-size: 86px; padding: 18px 40px; border-radius: 22px; box-shadow: 0 16px 0 #B5002A; letter-spacing: -0.02em; }
.stack { position: absolute; left: 40px; top: 230px; z-index: 21; display: flex; flex-direction: column; gap: 18px; }
.chip { display: flex; align-items: center; gap: 18px; background: #fff; color: #111; font-weight: 900; font-size: 46px; padding: 16px 30px 16px 16px; border-radius: 26px; box-shadow: 0 10px 0 rgba(0,0,0,0.25); width: fit-content; }
.badge { width: 62px; height: 62px; border-radius: 18px; color: #fff; display: flex; align-items: center; justify-content: center; font-size: 40px; }
.ctachip { position: absolute; left: 0; right: 0; top: 1060px; z-index: 22; display: flex; justify-content: center; }
.lkin { display: flex; align-items: center; gap: 12px; background: ${Y}; color: #111; font-weight: 900; font-size: 66px; padding: 20px 40px; border-radius: 26px; box-shadow: 0 12px 0 #B39A00; }
.follow { position: absolute; left: 0; right: 0; top: 1060px; z-index: 22; display: flex; justify-content: center; }
.fwin { display: flex; align-items: center; gap: 18px; background: #FF2D55; color: #fff; font-weight: 900; font-size: 84px; padding: 22px 56px; border-radius: 80px; box-shadow: 0 14px 0 #B5002A; }
.plus { font-size: 96px; line-height: 1; }
.bar { position: absolute; left: 0; right: 0; top: 0; height: 12px; background: rgba(255,255,255,0.25); z-index: 40; }
#prog { width: 100%; height: 100%; background: ${Y}; transform-origin: left center; }
</style>
</head>
<body>
<div id="root" data-composition-id="main" data-start="0" data-width="${W}" data-height="${H}" data-duration="${TOTAL}">
<div id="cam">
${html.filter(h => h.startsWith('<div class="vw"')).join("\n")}
</div>
${html.filter(h => !h.startsWith('<div class="vw"')).join("\n")}
<div class="bar"><div id="prog"></div></div>
<audio id="mix" src="assets/mix.wav" data-start="0" data-duration="${TOTAL}" data-track-index="9" data-volume="1"></audio>
</div>
<script>
document.fonts.ready.then(() => {
  const tl = gsap.timeline({ paused: true });
  ${js.join("\n  ")}
  window.__timelines["main"] = tl;
});
</script>
</body>
</html>
`;
fs.writeFileSync("index.html", page);
console.log(`ok · ${segs.length} cortes · ${pages.length} legendas · ${sfx.length} sfx · ${TOTAL}s`);
