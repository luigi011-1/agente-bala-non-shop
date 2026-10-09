// Vídeo de imóvel (temporada/locação): fotos e vídeos do proprietário + texto animado + ficha + CTA.
// node build.mjs   (lê imovel.json, escreve index.html)
import fs from "node:fs";

const W = 1080, H = 1920, XF = 0.5; // XF = duração do crossfade entre cenas
const cfg = JSON.parse(fs.readFileSync("imovel.json", "utf8"));
const SAND = cfg.cor ?? "#FFDDA6", WA = "#25D366";

const words = text => { const out = []; let key = false;
  for (let w of text.split(/\s+/)) { let k = key; if (w.startsWith("*")) { w = w.slice(1); k = key = true; }
    let close = false; if (w.endsWith("*")) { w = w.slice(0, -1); close = true; }
    out.push({ w, k }); if (close) key = false; } return out; };

let t = 0; const html = [], js = [];
cfg.cenas.forEach((c, i) => {
  const st = i === 0 ? 0 : t - XF, du = c.dur + (i === 0 ? 0 : XF), id = `c${i}`;
  c.t = t;
  const fadeIn = i === 0 ? "" : `tl.fromTo("#${id}-w", { opacity: 0 }, { opacity: 1, duration: ${XF}, ease: "sine.inOut" }, ${st.toFixed(3)});`;
  if (c.media?.endsWith(".mp4")) {
    html.push(`<div class="layer" id="${id}-w"><video class="clip full" id="${id}-v" src="assets/${c.media}" muted playsinline data-start="${st.toFixed(3)}" data-duration="${du.toFixed(3)}" data-media-start="${Math.max(0, (c.mediaStart ?? 0) - (i === 0 ? 0 : XF)).toFixed(3)}" data-track-index="${i % 2}"></video></div>`);
    js.push(fadeIn);
    js.push(`tl.fromTo("#${id}-w", { scale: 1.0 }, { scale: 1.06, duration: ${du.toFixed(3)}, ease: "none" }, ${st.toFixed(3)});`);
  } else if (c.media) {
    html.push(`<div class="clip layer" id="${id}-w" data-start="${st.toFixed(3)}" data-duration="${du.toFixed(3)}" data-track-index="${i % 2}"><img class="full" id="${id}-i" src="assets/${c.media}" alt=""></div>`);
    js.push(fadeIn);
    const kb = c.kb === "down" ? `{ scale: 1.18, yPercent: -4 }, { scale: 1.04, yPercent: 3` : `{ scale: 1.02 }, { scale: 1.14`;
    js.push(`tl.fromTo("#${id}-i", ${kb}, duration: ${du.toFixed(3)}, ease: "none" }, ${st.toFixed(3)});`);
  } else if (c.montagem) {
    const n = c.montagem.length, step = c.dur / n;
    html.push(`<div class="clip layer" id="${id}-w" data-start="${st.toFixed(3)}" data-duration="${du.toFixed(3)}" data-track-index="${i % 2}">${c.montagem.map(([f, lab], k) =>
      `<div class="mont" id="${id}-m${k}"><img class="full" id="${id}-mi${k}" src="assets/${f}" alt=""><div class="pill" id="${id}-p${k}">${lab}</div></div>`).join("")}</div>`);
    js.push(fadeIn);
    c.montagem.forEach((_, k) => {
      const a = t + k * step;
      if (k > 0) js.push(`tl.fromTo("#${id}-m${k}", { opacity: 0 }, { opacity: 1, duration: 0.18 }, ${(a - 0.09).toFixed(3)});`);
      js.push(`tl.fromTo("#${id}-mi${k}", { scale: 1.12 }, { scale: 1.0, duration: ${(step + 0.3).toFixed(3)}, ease: "power2.out" }, ${(a - 0.1).toFixed(3)});`);
      js.push(`tl.fromTo("#${id}-p${k}", { opacity: 0, y: 30, filter: "blur(10px)" }, { opacity: 1, y: 0, filter: "blur(0px)", duration: 0.4, ease: "power3.out" }, ${(a + 0.15).toFixed(3)});`);
    });
  } else if (c.final) {
    html.push(`<div class="clip layer" id="${id}-w" data-start="${st.toFixed(3)}" data-duration="${du.toFixed(3)}" data-track-index="${i % 2}"><img class="full" id="${id}-i" src="assets/${c.final}" alt=""><div class="shade"></div>
      <div class="card" id="${id}-card"><div class="ct">${cfg.titulo}</div><div class="cs">Temporada</div>
      ${cfg.ficha.map((f, k) => `<div class="fi" id="${id}-f${k}"><span class="ck"><svg viewBox="0 0 24 24" width="30" height="30" fill="none" stroke="#fff" stroke-width="3.2" stroke-linecap="round" stroke-linejoin="round"><path d="M20 6 9 17l-5-5"/></svg></span>${f}</div>`).join("")}
      <div class="wa" id="${id}-wa"><svg viewBox="0 0 24 24" width="46" height="46" fill="#fff"><path d="M12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2Zm5.3 14.2c-.2.6-1.3 1.2-1.8 1.2-.5.1-1 .2-3.3-.7-2.8-1.1-4.5-3.9-4.7-4.1-.1-.2-1.1-1.5-1.1-2.9s.7-2 1-2.3c.2-.3.5-.3.7-.3h.5c.2 0 .4 0 .6.5l.8 2c.1.2.1.4 0 .5l-.4.6-.4.4c-.1.1-.3.3-.1.6.2.3.8 1.3 1.6 2.1 1.1 1 2 1.3 2.3 1.4.3.1.5.1.6-.1l.9-1c.2-.3.4-.2.7-.1l1.9.9c.3.1.5.2.5.3.1.2.1.6-.1 1.2Z"/></svg>${cfg.cta}</div></div></div>`);
    js.push(fadeIn);
    js.push(`tl.fromTo("#${id}-i", { scale: 1.15, filter: "blur(0px)" }, { scale: 1.05, filter: "blur(6px)", duration: 1.2, ease: "power2.out" }, ${st.toFixed(3)});`);
    js.push(`tl.fromTo("#${id}-card", { opacity: 0, y: 80 }, { opacity: 1, y: 0, duration: 0.7, ease: "power3.out" }, ${(t + 0.2).toFixed(3)});`);
    cfg.ficha.forEach((_, k) => js.push(`tl.fromTo("#${id}-f${k}", { opacity: 0, x: -30 }, { opacity: 1, x: 0, duration: 0.35, ease: "power3.out" }, ${(t + 0.7 + k * 0.28).toFixed(3)});`));
    js.push(`tl.fromTo("#${id}-wa", { opacity: 0, scale: 0.85 }, { opacity: 1, scale: 1, duration: 0.45, ease: "back.out(1.8)" }, ${(t + 0.8 + cfg.ficha.length * 0.28).toFixed(3)});`);
    js.push(`tl.to("#${id}-wa", { scale: 1.05, duration: 0.4, yoyo: true, repeat: 3, ease: "sine.inOut" }, ${(t + 1.6 + cfg.ficha.length * 0.28).toFixed(3)});`);
  }
  // texto da cena
  if (c.text) {
    const ws = words(c.text), tt = t + (i === 0 ? 0.5 : 0.25), step = Math.min(0.32, (c.dur * 0.45) / ws.length);
    html.push(`<div class="clip txt" id="${id}-t" data-start="${tt.toFixed(3)}" data-duration="${(c.dur - (tt - t) - 0.05).toFixed(3)}" data-track-index="5"><div class="tin" id="${id}-tin">${ws.map((w, k) => `<span class="w ${w.k ? "k" : ""}" id="${id}-x${k}">${w.w}</span>`).join(" ")}</div></div>`);
    ws.forEach((w, k) => js.push(`tl.fromTo("#${id}-x${k}", { opacity: 0, y: 30, filter: "blur(14px)" }, { opacity: 1, y: 0, filter: "blur(0px)", duration: ${w.k ? 0.55 : 0.4}, ease: "power3.out" }, ${(tt + k * step).toFixed(3)});`));
    js.push(`tl.to("#${id}-tin", { opacity: 0, filter: "blur(12px)", duration: 0.3, ease: "power2.in" }, ${(t + c.dur - 0.38).toFixed(3)});`);
  }
  t += c.dur;
});
const TOTAL = +(t).toFixed(2);

const page = `<!doctype html>
<html lang="pt-BR" data-resolution="portrait">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=${W}, height=${H}" />
<script src="https://cdn.jsdelivr.net/npm/gsap@3.14.2/dist/gsap.min.js"></script>
<style>
@font-face { font-family: "Inter"; src: url("fonts/Inter.woff2") format("woff2"); font-weight: 100 900; }
@font-face { font-family: "Playfair Display"; src: url("fonts/PlayfairItalic.woff2") format("woff2"); font-style: italic; font-weight: 600; }
* { margin: 0; padding: 0; box-sizing: border-box; }
html, body { width: ${W}px; height: ${H}px; overflow: hidden; background: #000; }
#root { position: relative; width: 100%; height: 100%; overflow: hidden; font-family: "Inter", sans-serif; }
.layer, .mont { position: absolute; inset: 0; overflow: hidden; }
.full { position: absolute; inset: 0; width: 100%; height: 100%; object-fit: cover; display: block; }
.grad { position: absolute; inset: 0; z-index: 20; pointer-events: none; background: linear-gradient(180deg, rgba(0,0,0,0.35) 0%, rgba(0,0,0,0) 18%, rgba(0,0,0,0) 52%, rgba(0,0,0,0.62) 100%); }
.tag { position: absolute; top: 80px; left: 70px; z-index: 30; display: flex; gap: 14px; align-items: center; color: #fff; font-size: 30px; font-weight: 600; letter-spacing: 0.18em; text-transform: uppercase; text-shadow: 0 2px 12px rgba(0,0,0,0.4); }
.tag i { display: block; width: 56px; height: 3px; background: ${SAND}; }
.txt { position: absolute; left: 0; right: 0; bottom: 300px; z-index: 40; display: flex; justify-content: center; padding: 0 90px; }
.tin { text-align: center; line-height: 1.12; font-size: 66px; word-spacing: 0.04em; }
.w { display: inline-block; color: #fff; font-size: 66px; font-weight: 600; letter-spacing: -0.02em; text-shadow: 0 4px 24px rgba(0,0,0,0.45); }
.w.k { font-family: "Playfair Display", serif; font-style: italic; font-weight: 600; font-size: 104px; color: ${SAND}; letter-spacing: -0.01em; }
.pill { position: absolute; left: 70px; bottom: 330px; background: rgba(255,255,255,0.92); color: #1A2B3C; font-size: 46px; font-weight: 700; padding: 22px 38px; border-radius: 60px; box-shadow: 0 16px 40px rgba(0,0,0,0.3); }
.shade { position: absolute; inset: 0; background: linear-gradient(180deg, rgba(8,20,32,0.25), rgba(8,20,32,0.75)); }
.card { position: absolute; left: 80px; right: 80px; top: 520px; background: rgba(255,255,255,0.95); border-radius: 48px; padding: 64px 60px; box-shadow: 0 40px 90px rgba(0,0,0,0.4); }
.ct { font-family: "Playfair Display", serif; font-style: italic; font-size: 92px; color: #13314A; line-height: 1; }
.cs { font-size: 30px; letter-spacing: 0.2em; text-transform: uppercase; color: #C08A3E; font-weight: 700; margin: 18px 0 40px; }
.fi { display: flex; align-items: center; gap: 24px; font-size: 44px; font-weight: 600; color: #1A2B3C; padding: 14px 0; }
.ck { width: 58px; height: 58px; border-radius: 50%; background: #1F8A70; display: flex; align-items: center; justify-content: center; flex: none; }
.wa { margin-top: 44px; display: flex; align-items: center; justify-content: center; gap: 18px; background: ${WA}; color: #fff; font-size: 44px; font-weight: 700; padding: 34px; border-radius: 34px; box-shadow: 0 20px 44px rgba(37,211,102,0.45); }
</style>
</head>
<body>
<div id="root" data-composition-id="main" data-start="0" data-width="${W}" data-height="${H}" data-duration="${TOTAL}">
${html.join("\n")}
<div class="grad"></div>
<div class="clip tag" id="tag" data-start="0" data-duration="${(cfg.cenas.at(-1).t).toFixed(3)}" data-track-index="6"><i></i>Temporada · ${cfg.titulo}</div>
<audio id="mar" src="assets/mar.wav" data-start="0" data-duration="${TOTAL}" data-track-index="8" data-volume="${cfg.volumeMar ?? 0.9}"></audio>
${cfg.musica ? `<audio id="musica" src="assets/${cfg.musica}" data-start="0" data-duration="${TOTAL}" data-track-index="9" data-volume="${cfg.volumeMusica ?? 0.5}"></audio>` : ""}
</div>
<script>
document.fonts.ready.then(() => {
  const tl = gsap.timeline({ paused: true });
  tl.fromTo("#tag", { opacity: 0, x: -20 }, { opacity: 1, x: 0, duration: 0.6 }, 0.3);
  ${js.filter(Boolean).join("\n  ")}
  window.__timelines["main"] = tl;
});
</script>
</body>
</html>
`;
fs.writeFileSync("index.html", page);
console.log(`ok · ${cfg.cenas.length} cenas · ${TOTAL}s`);
