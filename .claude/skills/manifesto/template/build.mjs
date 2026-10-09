// Gera index.html a partir de script.json (+ timing.json, quando a locução existe).
// node build.mjs
import fs from "node:fs";

const W = 1080, H = 1920;
const NAVY = "#1E3A5F", NAVY_D = "#0F1E33", ORANGE = "#F97316", LIGHT = "#F4F5F7", INK = "#14233A", GREEN = "#16A34A", RED = "#DC2626";

const script = JSON.parse(fs.readFileSync("script.json", "utf8"));
const timing = fs.existsSync("timing.json") ? JSON.parse(fs.readFileSync("timing.json", "utf8")) : null;

// ---------- tokens ----------
function tokenize(text) {
  const out = []; let key = false;
  for (const raw of text.split(/\s+/)) {
    let w = raw, k = key;
    if (w.startsWith("*")) { w = w.slice(1); k = true; key = true; }
    let closes = false;
    const m = w.match(/^(.*?)\*([^*]*)$/);
    if (m) { w = m[1] + m[2]; closes = true; }
    out.push({ text: w, key: k });
    if (closes) key = false;
  }
  return out;
}

// ---------- timing ----------
const GAP = 0.32, GAP_THEME = 0.8, LEAD = 0.6;
const gapAfter = i => (script.scenes[i + 1] && script.scenes[i + 1].theme !== script.scenes[i].theme) ? GAP_THEME : GAP;
let t = LEAD;
const scenes = script.scenes.map((s, i) => {
  const words = tokenize(s.text);
  const tm = timing?.scenes?.[s.id];
  let start, end, wt;
  if (tm) {
    start = tm.start; end = tm.start + tm.duration;
    wt = tm.words && tm.words.length === words.length
      ? tm.words.map(w => tm.start + w.start)
      : null;
    if (!wt) { // distribui pelo número de letras dentro da fala real
      const chars = words.map(w => w.text.length + 2), tot = chars.reduce((a, b) => a + b, 0);
      let acc = 0; wt = chars.map(c => { const v = start + (acc / tot) * tm.duration; acc += c; return v; });
    }
  } else {
    start = t; wt = []; let x = start;
    for (const w of words) { wt.push(x); x += 0.13 + 0.058 * w.text.length; }
    end = x; t = end + gapAfter(i);
  }
  if (tm) t = end + gapAfter(i);
  return { ...s, idx: i, words, start, end, wt };
});
// cada cena fica até a próxima começar
scenes.forEach((s, i) => { s.until = i < scenes.length - 1 ? scenes[i + 1].start : s.end + 3.2; });
const TOTAL = +(scenes.at(-1).until + 0.7).toFixed(2);

// corridas de tema (fundo + transição em círculo)
const runs = [];
for (const s of scenes) {
  if (!runs.length || runs.at(-1).theme !== s.theme) runs.push({ theme: s.theme, start: s.start, scenes: [] });
  runs.at(-1).scenes.push(s); runs.at(-1).end = s.until;
}

// ---------- ícones (traço 24x24, estilo lucide) ----------
const I = {
  sheet: '<rect x="3" y="3" width="18" height="18" rx="2"/><path d="M3 9h18M3 15h18M9 3v18M15 3v18"/>',
  note: '<path d="M15.5 3H5a2 2 0 0 0-2 2v14c0 1.1.9 2 2 2h14a2 2 0 0 0 2-2V8.5L15.5 3Z"/><path d="M15 3v6h6"/><path d="M7 13h6M7 17h9"/>',
  calendar: '<rect x="3" y="4" width="18" height="18" rx="2"/><path d="M16 2v4M8 2v4M3 10h18"/><path d="M7 14h4M13 18h4"/>',
  trend: '<path d="M22 7 13.5 15.5 8.5 10.5 2 17"/><path d="M16 7h6v6"/>',
  eye: '<path d="M2 12s3.5-7 10-7 10 7 10 7-3.5 7-10 7S2 12 2 12Z"/><circle cx="12" cy="12" r="3"/>',
  ruler: '<path d="M21.3 15.3a2.4 2.4 0 0 1 0 3.4l-2.6 2.6a2.4 2.4 0 0 1-3.4 0L2.7 8.7a2.4 2.4 0 0 1 0-3.4l2.6-2.6a2.4 2.4 0 0 1 3.4 0Z"/><path d="m14.5 12.5 2-2M11.5 9.5l2-2M8.5 6.5l2-2M17.5 15.5l2-2"/>',
  helmet: '<path d="M2 18a1 1 0 0 0 1 1h18a1 1 0 0 0 1-1v-2a1 1 0 0 0-1-1H3a1 1 0 0 0-1 1v2Z"/><path d="M10 10V5a1 1 0 0 1 1-1h2a1 1 0 0 1 1 1v5"/><path d="M4 15v-3a6 6 0 0 1 6-6"/><path d="M14 6a6 6 0 0 1 6 6v3"/>',
  building: '<path d="M6 22V4a2 2 0 0 1 2-2h8a2 2 0 0 1 2 2v18Z"/><path d="M6 12H4a2 2 0 0 0-2 2v6a2 2 0 0 0 2 2h2M18 9h2a2 2 0 0 1 2 2v9a2 2 0 0 1-2 2h-2"/><path d="M10 6h4M10 10h4M10 14h4M10 18h4"/>',
  chat: '<path d="M7.9 20A9 9 0 1 0 4 16.1L2 22Z"/>',
  receipt: '<path d="M4 2v20l2-1 2 1 2-1 2 1 2-1 2 1 2-1 2 1V2l-2 1-2-1-2 1-2-1-2 1-2-1-2 1Z"/><path d="M16 8h-6a2 2 0 1 0 0 4h4a2 2 0 1 1 0 4H8M12 17.5v-11"/>',
  calc: '<rect x="4" y="2" width="16" height="20" rx="2"/><path d="M8 6h8M16 14v4M16 10h.01M12 10h.01M8 10h.01M12 14h.01M8 14h.01M12 18h.01M8 18h.01"/>',
  bars: '<path d="M3 3v18h18"/><path d="M18 17V9M13 17V5M8 17v-3"/>',
  book: '<path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2Z"/><path d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7Z"/>',
  clipboard: '<rect x="8" y="2" width="8" height="4" rx="1"/><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"/><path d="M12 11h4M12 16h4M8 11h.01M8 16h.01"/>',
  box: '<path d="M21 8a2 2 0 0 0-1-1.7l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.7l7 4a2 2 0 0 0 2 0l7-4a2 2 0 0 0 1-1.7Z"/><path d="m3.3 7 8.7 5 8.7-5M12 22V12"/>',
  users: '<path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M22 21v-2a4 4 0 0 0-3-3.9M16 3.1a4 4 0 0 1 0 7.8"/>',
  dollar: '<path d="M12 2v20M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"/>',
  check: '<path d="M20 6 9 17l-5-5"/>',
  send: '<path d="m22 2-7 20-4-9-9-4Z"/><path d="M22 2 11 13"/>',
  spark: '<path d="M12 3l1.9 5.8L20 11l-6.1 2.2L12 19l-1.9-5.8L4 11l6.1-2.2Z"/>'
};
const svg = (name, size, color, sw = 1.8) =>
  `<svg viewBox="0 0 24 24" width="${size}" height="${size}" fill="none" stroke="${color}" stroke-width="${sw}" stroke-linecap="round" stroke-linejoin="round">${I[name]}</svg>`;
const LOGO_PATH = '<path class="lg-u" d="M 22,36 L 22,63 Q 22,84 47,84 Q 72,84 72,63 L 72,36" stroke="url(#lgO)" stroke-width="18" fill="none"/><polygon class="lg-a" points="72,9 58,38 86,38" fill="url(#lgO)"/>';
const logoSvg = (size, id) => `<svg viewBox="0 0 100 100" width="${size}" height="${size}"><defs><linearGradient id="lgO${id}" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#FFA040"/><stop offset="100%" stop-color="#E05E00"/></linearGradient></defs>${LOGO_PATH.replaceAll("url(#lgO)", `url(#lgO${id})`)}</svg>`;
const wordmark = (cls, dark) => `<div class="wordmark ${cls}"><span style="color:${dark ? "#fff" : NAVY}">obra</span><span style="color:${ORANGE}">UP</span></div>`;

// ---------- props: html + animação ----------
// cada prop devolve { html, anim(tl, s, sel) } ; sel(x) = seletor dentro da cena
const P = {};
const tile = (s, icon) => `<div class="tile ${s.theme}" id="${s.id}-tile">${svg(icon, 120, ORANGE, 1.7)}</div>`;
const tileIn = (tl, s, sel) => tl.fromTo(sel("-tile"), { opacity: 0, scale: 0.6, rotation: -14, y: 60, filter: "blur(10px)" },
  { opacity: 1, scale: 1, rotation: 0, y: 0, filter: "blur(0px)", duration: 0.75, ease: "back.out(1.6)" }, s.start - 0.15);

P.tile = s => ({ html: tile(s, s.icon), anim: (tl, s, sel) => {
  tileIn(tl, s, sel);
  tl.to(sel("-tile"), { y: -14, duration: Math.max(0.6, s.until - s.start - 0.4), ease: "sine.inOut" }, s.start + 0.6);
}});

P.chat = s => ({ html: `${tile(s, "chat")}${[0, 1, 2, 3].map(i => `<div class="bubble b${i}" id="${s.id}-b${i}">${["manda foto?", "quanto já gastou?", "o material chegou?", "99+"][i]}</div>`).join("")}`,
  anim: (tl, s, sel) => { tileIn(tl, s, sel);
    [0, 1, 2, 3].forEach(i => tl.fromTo(sel("-b" + i), { opacity: 0, scale: 0.4 }, { opacity: 1, scale: 1, duration: 0.35, ease: "back.out(2.2)" }, s.start + 0.15 + i * 0.22));
    tl.to(sel("-tile"), { rotation: 6, duration: 0.08, yoyo: true, repeat: 7, ease: "none" }, s.start + 0.65);
  }});

P.helmets = s => ({ html: `<div class="row" id="${s.id}-row">${[0, 1, 2, 3, 4].map(i => `<div class="mini dark" id="${s.id}-h${i}">${svg("helmet", 74, ORANGE, 1.7)}</div>`).join("")}</div>`,
  anim: (tl, s, sel) => [0, 1, 2, 3, 4].forEach(i => tl.fromTo(sel("-h" + i), { opacity: 0, y: 50, scale: 0.5 }, { opacity: 1, y: 0, scale: 1, duration: 0.45, ease: "back.out(1.8)" }, s.start - 0.1 + i * 0.16)) });

P.margin = s => ({ html: `<div class="panel dark" id="${s.id}-p"><div class="plabel">MARGEM DA OBRA</div><div class="pval" id="${s.id}-pv"><span id="${s.id}-v">18</span>%</div><div class="track"><div class="fill" id="${s.id}-f"></div></div><div class="pnote" id="${s.id}-n">−R$ 47.300 sem perceber</div></div>`,
  anim: (tl, s, sel) => {
    tl.fromTo(sel("-p"), { opacity: 0, y: 60, filter: "blur(10px)" }, { opacity: 1, y: 0, filter: "blur(0px)", duration: 0.6, ease: "power3.out" }, s.start - 0.15);
    tl.fromTo(sel("-v"), { innerText: 18 }, { innerText: -6, snap: { innerText: 1 }, duration: 1.6, ease: "power2.in" }, s.start + 0.5);
    tl.fromTo(sel("-f"), { scaleX: 0.72, backgroundColor: GREEN }, { scaleX: 0.08, backgroundColor: RED, duration: 1.6, ease: "power2.in" }, s.start + 0.5);
    tl.to(sel("-pv"), { color: RED, duration: 0.4 }, s.start + 1.4);
    tl.fromTo(sel("-n"), { opacity: 0, y: 16 }, { opacity: 1, y: 0, duration: 0.4 }, s.start + 1.7);
  }});

P.logo = s => ({ html: `<div class="logo-wrap" id="${s.id}-lw"><div class="glow" id="${s.id}-g"></div>${logoSvg(300, s.id)}</div>`,
  anim: (tl, s, sel) => {
    tl.fromTo(sel("-lw .lg-u"), { strokeDasharray: 220, strokeDashoffset: 220 }, { strokeDashoffset: 0, duration: 0.9, ease: "power2.inOut" }, s.start + 0.2);
    tl.fromTo(sel("-lw .lg-a"), { opacity: 0, y: 30 }, { opacity: 1, y: 0, duration: 0.45, ease: "back.out(2)" }, s.start + 0.9);
    tl.fromTo(sel("-g"), { opacity: 0, scale: 0.4 }, { opacity: 1, scale: 1, duration: 1.0, ease: "power2.out" }, s.start + 0.6);
  }});

P.receipt = s => ({ html: `<div class="receipt" id="${s.id}-r">${svg("receipt", 92, "#9AA8BC", 1.6)}<div class="rl"></div><div class="rl s"></div><div class="rl"></div><div class="rtot">−R$ 1.343,68</div></div><svg class="bigx" id="${s.id}-x" viewBox="0 0 100 100"><path d="M15 15 85 85M85 15 15 85" stroke="#fff" stroke-width="7" stroke-linecap="round" fill="none"/></svg>`,
  anim: (tl, s, sel) => {
    tl.fromTo(sel("-r"), { opacity: 0, rotation: -10, y: 70 }, { opacity: 1, rotation: -4, y: 0, duration: 0.6, ease: "back.out(1.5)" }, s.start - 0.15);
    const k = s.wt[s.words.findIndex(w => w.key)] ?? s.start + 0.5;
    tl.fromTo(sel("-x path"), { strokeDasharray: 100, strokeDashoffset: 100 }, { strokeDashoffset: 0, duration: 0.45, ease: "power2.out" }, k);
    tl.to(sel("-r"), { opacity: 0.35, filter: "grayscale(1)", duration: 0.4 }, k + 0.2);
  }});

P.bars = s => ({ html: `<div class="chart" id="${s.id}-c">${[["Obra A", 0.62], ["Obra B", 0.88], ["Obra C", 0.47]].map(([n, h], i) => `<div class="col"><div class="cval" id="${s.id}-cv${i}">+R$ ${[42, 76, 31][i]} mil</div><div class="cbar" id="${s.id}-cb${i}" style="height:${Math.round(h * 430)}px"></div><div class="cname">${n}</div></div>`).join("")}</div>`,
  anim: (tl, s, sel) => [0, 1, 2].forEach(i => {
    tl.fromTo(sel("-cb" + i), { scaleY: 0 }, { scaleY: 1, duration: 0.8, ease: "power3.out" }, s.start + 0.1 + i * 0.18);
    tl.fromTo(sel("-cv" + i), { opacity: 0, y: 20 }, { opacity: 1, y: 0, duration: 0.4 }, s.start + 0.6 + i * 0.18);
  })});

const MODS = [["calc", "Orçamento"], ["calendar", "Cronograma"], ["book", "Diário de obra"], ["clipboard", "Cotações"], ["box", "Estoque"], ["users", "Equipe"], ["dollar", "Financeiro"]];
P.modules = s => ({ html: `<div class="grid" id="${s.id}-g">${MODS.map(([ic, n], i) => `<div class="mod" id="${s.id}-m${i}"><div class="mini dark">${svg(ic, 62, ORANGE, 1.7)}</div><div class="mname">${n}</div></div>`).join("")}</div>`,
  anim: (tl, s, sel) => {
    // cada módulo entra quando seu nome é falado
    const starts = [0, 1, 2, 4, 5, 6, 8].map(wi => s.wt[wi] ?? s.start + wi * 0.3);
    MODS.forEach((_, i) => tl.fromTo(sel("-m" + i), { opacity: 0, scale: 0.5, y: 30 }, { opacity: 1, scale: 1, y: 0, duration: 0.4, ease: "back.out(2)" }, starts[i] - 0.05));
  }});

P.bridge = s => ({ html: `<div class="bridge" id="${s.id}-br"><div class="tile light sm" id="${s.id}-t1">${svg("helmet", 96, ORANGE, 1.7)}</div><svg class="dash" id="${s.id}-dash" viewBox="0 0 300 20"><path id="${s.id}-ln" d="M5 10 H295" stroke="${ORANGE}" stroke-width="5" stroke-dasharray="14 12" fill="none"/></svg><div class="tile light sm" id="${s.id}-t2">${svg("building", 96, ORANGE, 1.7)}</div></div>`,
  anim: (tl, s, sel) => {
    tl.fromTo(sel("-t1"), { opacity: 0, scale: 0.6, x: -40 }, { opacity: 1, scale: 1, x: 0, duration: 0.6, ease: "back.out(1.7)" }, s.wt[1] - 0.2);
    tl.fromTo(sel("-dash"), { scaleX: 0 }, { scaleX: 1, duration: 0.7, ease: "power2.inOut" }, s.wt[2] - 0.1);
    tl.fromTo(sel("-t2"), { opacity: 0, scale: 0.6, x: 40 }, { opacity: 1, scale: 1, x: 0, duration: 0.6, ease: "back.out(1.7)" }, s.wt[3] - 0.2);
  }});

P.upia = s => ({ html: `<div class="upia" id="${s.id}-u"><div class="uhead"><div class="ubot">${svg("spark", 40, "#fff", 1.8)}</div><div><div class="uname">UpIA</div><div class="usub">Sua inteligência operacional de obra</div></div></div><div class="umsg" id="${s.id}-msg"><span class="typed" id="${s.id}-typed">chegaram 40 sacos de cimento na Residencial Aurora</span></div><div class="ucard" id="${s.id}-card"><div class="uct">SOLICITAÇÃO DE MATERIAL</div><div class="ucr"><span>Obra</span><b>Residencial Aurora</b></div><div class="ucr"><span>Material</span><b>Cimento CP II · 40 sacos</b></div><div class="ucok" id="${s.id}-ok">${svg("check", 30, "#fff", 3)} Confirmar</div></div></div>`,
  anim: (tl, s, sel) => {
    tl.fromTo(sel("-u"), { opacity: 0, y: 60, filter: "blur(10px)" }, { opacity: 1, y: 0, filter: "blur(0px)", duration: 0.6, ease: "power3.out" }, s.start - 0.2);
    tl.fromTo(sel("-msg"), { opacity: 0 }, { opacity: 1, duration: 0.2 }, s.start + 0.2);
    tl.fromTo(sel("-typed"), { clipPath: "inset(0 100% 0 0)" }, { clipPath: "inset(0 0% 0 0)", duration: 1.2, ease: "steps(46)" }, s.start + 0.3);
    const k = s.wt[s.words.length - 1] ?? s.start + 1.6;
    tl.fromTo(sel("-card"), { opacity: 0, y: 40, scale: 0.92 }, { opacity: 1, y: 0, scale: 1, duration: 0.5, ease: "back.out(1.6)" }, k - 0.35);
    tl.fromTo(sel("-ok"), { scale: 1 }, { scale: 1.08, duration: 0.18, yoyo: true, repeat: 1 }, k + 0.4);
  }});

P.compare = s => ({ html: `<div class="cmp" id="${s.id}-cmp">${[["Fornecedor A", "R$ 33.640"], ["Fornecedor B", "R$ 31.300"], ["Fornecedor C", "R$ 28.900"]].map(([n, v], i) => `<div class="ccol ${i === 2 ? "best" : ""}" id="${s.id}-k${i}"><div class="cn">${n}</div><div class="cv">${v}</div>${i === 2 ? `<div class="ctag" id="${s.id}-tag">${svg("check", 24, "#fff", 3)} melhor preço</div>` : `<div class="ctag gray">30 dias</div>`}</div>`).join("")}</div>`,
  anim: (tl, s, sel) => {
    [0, 1, 2].forEach(i => tl.fromTo(sel("-k" + i), { opacity: 0, y: 60 }, { opacity: 1, y: 0, duration: 0.5, ease: "power3.out" }, s.start - 0.1 + i * 0.15));
    tl.fromTo(sel("-k2"), { boxShadow: "0 0 0 0 rgba(22,163,74,0)" }, { boxShadow: "0 0 0 6px rgba(22,163,74,0.9)", duration: 0.4 }, s.start + 0.9);
    tl.fromTo(sel("-tag"), { opacity: 0, scale: 0.6 }, { opacity: 1, scale: 1, duration: 0.4, ease: "back.out(2)" }, s.start + 1.0);
  }});

P.rdo = s => ({ html: `<div class="rdo" id="${s.id}-rd"><div class="rh"><span>RDO #28 · Residencial Aurora</span></div><div class="rgrid"><div><small>Clima</small><b>Claro · praticável</b></div><div><small>Equipe</small><b>8 pessoas</b></div></div><div class="ract"><span>Alvenaria</span><div class="rtrack"><div class="rfill" id="${s.id}-rf"></div></div><b>90%</b></div><div class="rphotos"><i></i><i></i><i></i><i></i></div><div class="stamp" id="${s.id}-st">${svg("check", 34, "#fff", 3)} Aprovado pelo cliente</div></div>`,
  anim: (tl, s, sel) => {
    tl.fromTo(sel("-rd"), { opacity: 0, y: 70, rotation: 3 }, { opacity: 1, y: 0, rotation: 0, duration: 0.6, ease: "power3.out" }, s.start - 0.15);
    tl.fromTo(sel("-rf"), { scaleX: 0 }, { scaleX: 0.9, duration: 0.9, ease: "power2.out" }, s.start + 0.4);
    const k = s.wt[s.words.length - 1] ?? s.start + 2;
    tl.fromTo(sel("-st"), { opacity: 0, scale: 1.8, rotation: -14 }, { opacity: 1, scale: 1, rotation: -6, duration: 0.35, ease: "power4.in" }, k);
  }});

P.nochaos = s => ({ html: `<div class="chaos" id="${s.id}-ch">${["cadê a nota?", "quem pagou?", "manda foto", "atrasou de novo", "?? ?"].map((m, i) => `<div class="bubble dk c${i}" id="${s.id}-c${i}">${m}</div>`).join("")}</div><svg class="bigx" id="${s.id}-x" viewBox="0 0 100 100"><path d="M15 15 85 85M85 15 15 85" stroke="${ORANGE}" stroke-width="7" stroke-linecap="round" fill="none"/></svg>`,
  anim: (tl, s, sel) => {
    [0, 1, 2, 3, 4].forEach(i => tl.fromTo(sel("-c" + i), { opacity: 0, scale: 0.4 }, { opacity: 1, scale: 1, duration: 0.3, ease: "back.out(2)" }, s.start - 0.15 + i * 0.12));
    const k = s.wt[s.words.findIndex(w => w.key)] ?? s.start + 0.6;
    tl.fromTo(sel("-x path"), { strokeDasharray: 100, strokeDashoffset: 100 }, { strokeDashoffset: 0, duration: 0.4, ease: "power2.out" }, k);
    tl.to(sel("-ch"), { opacity: 0.25, filter: "blur(4px)", duration: 0.4 }, k + 0.15);
  }});

P.checklist = s => ({ html: `<div class="clist" id="${s.id}-cl"><div class="clt">A gente acredita em</div>${["Dado", "Prazo", "Decisão na hora certa"].map((n, i) => `<div class="cli" id="${s.id}-i${i}"><span class="cbx" id="${s.id}-x${i}">${svg("check", 30, "#fff", 3.2)}</span>${n}</div>`).join("")}</div>`,
  anim: (tl, s, sel) => {
    tl.fromTo(sel("-cl"), { opacity: 0, y: 60, filter: "blur(10px)" }, { opacity: 1, y: 0, filter: "blur(0px)", duration: 0.6, ease: "power3.out" }, s.start - 0.15);
    const keyIdx = s.words.map((w, i) => w.key ? i : -1).filter(i => i >= 0);
    const at = [keyIdx[0], keyIdx[1], keyIdx[2]].map(i => s.wt[i] ?? s.start + 1);
    [0, 1, 2].forEach(i => {
      tl.fromTo(sel("-i" + i), { opacity: 0.25 }, { opacity: 1, duration: 0.3 }, at[i] - 0.05);
      tl.fromTo(sel("-x" + i), { scale: 0, backgroundColor: "#CBD5E1" }, { scale: 1, backgroundColor: ORANGE, duration: 0.35, ease: "back.out(2.5)" }, at[i]);
    });
  }});

P.final = s => ({ html: `<div class="final" id="${s.id}-fn"><div class="glow" id="${s.id}-g"></div>${logoSvg(230, s.id)}${wordmark("big", true)}</div>`,
  anim: (tl, s, sel) => {
    tl.fromTo(sel("-fn .lg-u"), { strokeDasharray: 220, strokeDashoffset: 220 }, { strokeDashoffset: 0, duration: 0.8, ease: "power2.inOut" }, s.start - 0.1);
    tl.fromTo(sel("-fn .lg-a"), { opacity: 0, y: 30 }, { opacity: 1, y: 0, duration: 0.4, ease: "back.out(2)" }, s.start + 0.5);
    tl.fromTo(sel("-fn .wordmark"), { opacity: 0, scale: 1.25, filter: "blur(12px)" }, { opacity: 1, scale: 1, filter: "blur(0px)", duration: 0.8, ease: "power3.out" }, s.start + 0.3);
    tl.fromTo(sel("-g"), { opacity: 0, scale: 0.4 }, { opacity: 1, scale: 1, duration: 1.2 }, s.start + 0.3);
  }});

P.cta = s => ({ html: `<div class="cta" id="${s.id}-cta">${logoSvg(150, s.id)}<div class="ctab" id="${s.id}-btn">${svg("send", 40, "#fff", 2.2)} Agendar demo no WhatsApp</div><div class="ctaurl">obraup.com.br</div></div>`,
  anim: (tl, s, sel) => {
    tl.fromTo(sel("-cta"), { opacity: 0, y: 50 }, { opacity: 1, y: 0, duration: 0.6, ease: "power3.out" }, s.start - 0.15);
    tl.fromTo(sel("-btn"), { scale: 1 }, { scale: 1.06, duration: 0.35, yoyo: true, repeat: 3, ease: "sine.inOut" }, s.end + 0.1);
  }});

// ---------- html ----------
const runHtml = runs.map((r, i) => {
  const st = i === 0 ? 0 : r.start - 0.5, du = Math.min(r.end + 0.6, TOTAL) - st;
  const deco = r.theme === "light"
    ? `<div class="gridbg"></div><svg class="arc" viewBox="0 0 400 400"><path d="M30 380 A350 350 0 0 1 380 30" stroke="#DADFE6" stroke-width="46" fill="none" stroke-linecap="round"/></svg><div class="hdr">${wordmark("sm", false)}<div class="ticks">${Array.from({ length: 14 }, (_, k) => `<i style="height:${k % 3 === 0 ? 30 : 18}px"></i>`).join("")}</div></div>`
    : `<div class="dots"></div><div class="vign"></div>`;
  return `<div class="clip run ${r.theme}" id="run${i}" data-start="${st.toFixed(3)}" data-duration="${du.toFixed(3)}" data-track-index="${i % 2}"><div class="runbg" id="run${i}-bg">${deco}</div></div>`;
}).join("\n");

const sceneHtml = scenes.map(s => {
  const prop = P[s.prop](s);
  s._prop = prop;
  const st = s.start - 0.35, du = Math.min(s.until + 0.35, TOTAL) - st;
  const words = s.words.map((w, i) => `<span class="w ${w.key ? "k" : ""}" id="${s.id}-w${i}">${w.text}</span>`).join(" ");
  return `<section class="clip scene ${s.theme}" id="${s.id}" data-start="${st.toFixed(3)}" data-duration="${du.toFixed(3)}" data-track-index="${2 + (s.idx % 2)}"><div class="inner" id="${s.id}-in"><div class="stage">${prop.html}</div><div class="txt">${words}</div></div></section>`;
}).join("\n");

const audioHtml = timing?.audio ? `<audio id="vo" src="${timing.audio}" data-start="0" data-duration="${TOTAL}" data-track-index="9"></audio>` : "";
const musicHtml = timing?.music ? `<audio id="bgm" src="${timing.music}" data-start="0" data-duration="${TOTAL}" data-track-index="10" data-volume="${timing.musicVolume ?? 0.16}"></audio>` : "";

const anims = [];
// transições de fundo: círculo que cresce
runs.forEach((r, i) => { if (i > 0) anims.push(`tl.fromTo("#run${i}-bg", { clipPath: "circle(0% at 50% 38%)" }, { clipPath: "circle(120% at 50% 38%)", duration: 0.65, ease: "power3.inOut" }, ${(r.start - 0.5).toFixed(3)});`); });

const html = `<!doctype html>
<html lang="pt-BR" data-resolution="portrait">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=${W}, height=${H}" />
<script src="https://cdn.jsdelivr.net/npm/gsap@3.14.2/dist/gsap.min.js"></script>
<style>
@font-face { font-family: "Space Grotesk"; src: url("fonts/SpaceGrotesk.woff2") format("woff2"); font-weight: 300 700; }
@font-face { font-family: "Inter"; src: url("fonts/Inter.woff2") format("woff2"); font-weight: 100 900; }
* { margin: 0; padding: 0; box-sizing: border-box; }
html, body { width: ${W}px; height: ${H}px; overflow: hidden; background: ${LIGHT}; }
#root { position: relative; width: 100%; height: 100%; overflow: hidden; font-family: "Inter", sans-serif; }
.run, .scene { position: absolute; inset: 0; }
.runbg { position: absolute; inset: 0; overflow: hidden; }
.run.light .runbg { background: ${LIGHT}; }
.run.dark .runbg { background: radial-gradient(120% 70% at 50% 36%, #1B3355 0%, ${NAVY_D} 55%, #0A1526 100%); }
.gridbg { position: absolute; inset: 0; background-image: linear-gradient(#E3E7EC 1.5px, transparent 1.5px), linear-gradient(90deg, #E3E7EC 1.5px, transparent 1.5px); background-size: 72px 72px; opacity: 0.55; }
.arc { position: absolute; width: 760px; height: 760px; left: -330px; bottom: 120px; opacity: 0.7; }
.dots { position: absolute; inset: 0; background-image: radial-gradient(rgba(249,115,22,0.16) 1.6px, transparent 1.6px); background-size: 36px 36px; opacity: 0.5; }
.vign { position: absolute; inset: 0; background: radial-gradient(60% 40% at 50% 38%, rgba(249,115,22,0.16), transparent 70%); }
.hdr { position: absolute; left: 70px; right: 70px; top: 70px; display: flex; justify-content: space-between; align-items: flex-end; }
.wordmark { font-family: "Space Grotesk", sans-serif; font-weight: 700; letter-spacing: -0.02em; }
.wordmark.sm { font-size: 40px; }
.wordmark.big { font-size: 150px; line-height: 1; margin-top: 30px; }
.ticks { display: flex; gap: 7px; align-items: flex-end; }
.ticks i { display: block; width: 4px; background: ${NAVY}; opacity: 0.75; }
.inner { position: absolute; inset: 0; display: flex; flex-direction: column; align-items: center; padding: 0 100px; }
.stage { position: relative; width: 100%; height: 1000px; margin-top: 260px; display: flex; align-items: center; justify-content: center; }
.txt { width: 100%; text-align: center; font-family: "Space Grotesk", sans-serif; line-height: 1.12; }
.w { display: inline-block; font-size: 58px; font-weight: 500; color: ${INK}; margin: 0 2px; }
.dark .w { color: #E8EEF6; }
.w.k { font-size: 116px; font-weight: 700; color: ${ORANGE}; letter-spacing: -0.03em; }
.dark .w.k { color: #FF8A2E; text-shadow: 0 0 40px rgba(249,115,22,0.45); }
.tile { width: 300px; height: 300px; border-radius: 76px; display: flex; align-items: center; justify-content: center; }
.tile.light { background: linear-gradient(160deg, #FFFFFF, #EEF1F5); box-shadow: 0 40px 70px rgba(30,58,95,0.18), 0 8px 18px rgba(30,58,95,0.08), inset 0 2px 0 #fff; }
.tile.dark { background: linear-gradient(160deg, #1F3A5E, #132640); border: 2px solid rgba(249,115,22,0.45); box-shadow: 0 0 60px rgba(249,115,22,0.22), inset 0 1px 0 rgba(255,255,255,0.08); }
.tile.sm { width: 220px; height: 220px; border-radius: 56px; }
.mini { width: 150px; height: 150px; border-radius: 40px; display: flex; align-items: center; justify-content: center; }
.mini.dark { background: linear-gradient(160deg, #1F3A5E, #132640); border: 2px solid rgba(249,115,22,0.4); box-shadow: 0 0 40px rgba(249,115,22,0.18); }
.row { display: flex; gap: 22px; }
.bubble { position: absolute; background: #fff; color: ${INK}; font-size: 36px; font-weight: 600; padding: 20px 30px; border-radius: 30px 30px 30px 8px; box-shadow: 0 18px 40px rgba(30,58,95,0.16); }
.bubble.b0 { left: 60px; top: 230px; } .bubble.b1 { right: 30px; top: 300px; } .bubble.b2 { left: 90px; bottom: 210px; }
.bubble.b3 { right: 250px; top: 300px; background: ${RED}; color: #fff; border-radius: 40px; padding: 14px 24px; font-size: 40px; }
.bubble.b1 { top: 190px; }
.bubble.dk { background: #20385A; color: #CFD9E6; }
.c0 { left: 40px; top: 300px; } .c1 { right: 40px; top: 260px; } .c2 { left: 180px; top: 520px; } .c3 { right: 80px; top: 600px; } .c4 { left: 100px; bottom: 140px; }
.chaos { position: absolute; inset: 0; }
.bigx { position: absolute; width: 520px; height: 520px; }
.panel { width: 820px; padding: 60px; border-radius: 48px; }
.panel.dark { background: rgba(20,38,64,0.9); border: 2px solid rgba(255,255,255,0.08); }
.plabel { font-size: 32px; letter-spacing: 0.12em; color: #8FA3BF; font-weight: 600; }
.pval { font-family: "Space Grotesk"; font-size: 190px; font-weight: 700; color: #34D27B; line-height: 1.1; }
.track { height: 34px; border-radius: 20px; background: rgba(255,255,255,0.08); overflow: hidden; margin-top: 20px; }
.fill { width: 100%; height: 100%; transform-origin: left center; border-radius: 20px; }
.pnote { margin-top: 30px; font-size: 42px; font-weight: 700; color: #FF6B6B; }
.logo-wrap, .final { position: relative; display: flex; flex-direction: column; align-items: center; }
.glow { position: absolute; width: 700px; height: 700px; border-radius: 50%; background: radial-gradient(circle, rgba(249,115,22,0.38), transparent 65%); top: 50%; left: 50%; margin: -350px 0 0 -350px; }
.final .glow { margin-top: -470px; }
.receipt { position: relative; width: 460px; padding: 50px; background: #E9EDF3; border-radius: 18px; display: flex; flex-direction: column; gap: 20px; }
.rl { height: 18px; background: #C6CFDB; border-radius: 9px; } .rl.s { width: 60%; }
.rtot { font-family: "Space Grotesk"; font-size: 54px; font-weight: 700; color: ${INK}; }
.chart { display: flex; gap: 60px; align-items: flex-end; height: 640px; }
.col { display: flex; flex-direction: column; align-items: center; gap: 18px; width: 200px; }
.cbar { width: 170px; border-radius: 26px 26px 10px 10px; background: linear-gradient(180deg, #34D27B, ${GREEN}); transform-origin: bottom center; box-shadow: 0 20px 40px rgba(22,163,74,0.25); }
.cval { font-family: "Space Grotesk"; font-size: 40px; font-weight: 700; color: ${GREEN}; white-space: nowrap; }
.cname { font-size: 36px; font-weight: 600; color: ${INK}; }
.grid { display: grid; grid-template-columns: repeat(3, 250px); gap: 34px 20px; justify-items: center; }
.mod { display: flex; flex-direction: column; align-items: center; gap: 16px; }
.mod:nth-child(7) { grid-column: 2; }
.mname { font-size: 31px; font-weight: 600; color: #DCE5F0; text-align: center; }
.bridge { display: flex; align-items: center; gap: 10px; }
.dash { display: block; width: 300px; height: 20px; transform-origin: left center; }
.upia { width: 880px; background: #F6F8FB; border-radius: 44px; overflow: hidden; box-shadow: 0 40px 90px rgba(0,0,0,0.45); }
.uhead { display: flex; gap: 26px; align-items: center; padding: 40px; background: linear-gradient(120deg, #1B355A, #33608F); }
.ubot { width: 90px; height: 90px; border-radius: 26px; background: rgba(255,255,255,0.12); display: flex; align-items: center; justify-content: center; }
.uname { font-family: "Space Grotesk"; font-size: 52px; font-weight: 700; color: #fff; }
.usub { font-size: 28px; color: #C9D6E6; }
.typed { display: inline-block; white-space: nowrap; }
.umsg { margin: 40px 40px 0 auto; width: fit-content; background: ${NAVY}; color: #fff; font-size: 33px; padding: 26px 32px; border-radius: 30px 30px 8px 30px; }
.ucard { margin: 30px 40px 40px; background: #fff; border-radius: 30px; padding: 34px; box-shadow: 0 12px 30px rgba(30,58,95,0.12); border: 2px solid #E5EAF0; }
.uct { font-size: 26px; letter-spacing: 0.12em; color: ${ORANGE}; font-weight: 700; margin-bottom: 18px; }
.ucr { display: flex; justify-content: space-between; font-size: 32px; padding: 10px 0; color: #5B6B80; } .ucr b { color: ${INK}; }
.ucok { margin-top: 22px; background: ${GREEN}; color: #fff; font-size: 34px; font-weight: 700; border-radius: 22px; padding: 20px; display: flex; align-items: center; justify-content: center; gap: 12px; }
.cmp { display: flex; gap: 24px; }
.ccol { width: 270px; background: #fff; border-radius: 34px; padding: 40px 26px; display: flex; flex-direction: column; align-items: center; gap: 22px; box-shadow: 0 24px 50px rgba(30,58,95,0.14); }
.ccol.best { background: #F0FDF4; }
.cn { font-size: 30px; color: #5B6B80; font-weight: 600; }
.cv { font-family: "Space Grotesk"; font-size: 50px; font-weight: 700; color: ${INK}; }
.best .cv { color: ${GREEN}; }
.ctag { display: flex; align-items: center; gap: 8px; background: ${GREEN}; color: #fff; font-size: 26px; font-weight: 700; padding: 12px 18px; border-radius: 18px; }
.ctag.gray { background: #EEF1F5; color: #8492A6; }
.rdo { position: relative; width: 840px; background: #fff; border-radius: 40px; padding: 46px; box-shadow: 0 40px 80px rgba(30,58,95,0.18); }
.rh { font-family: "Space Grotesk"; font-size: 38px; font-weight: 700; color: ${INK}; margin-bottom: 30px; }
.rgrid { display: flex; gap: 24px; margin-bottom: 30px; }
.rgrid div { flex: 1; background: #F4F6F9; border-radius: 22px; padding: 22px; display: flex; flex-direction: column; gap: 6px; }
.rgrid small { font-size: 24px; color: #8492A6; } .rgrid b { font-size: 32px; color: ${INK}; }
.ract { display: flex; align-items: center; gap: 20px; font-size: 32px; color: ${INK}; margin-bottom: 30px; }
.rtrack { flex: 1; height: 22px; background: #EEF1F5; border-radius: 12px; overflow: hidden; }
.rfill { width: 100%; height: 100%; background: ${ORANGE}; transform-origin: left center; border-radius: 12px; }
.rphotos { display: flex; gap: 16px; } .rphotos i { flex: 1; height: 150px; border-radius: 18px; background: linear-gradient(150deg, #C9D3DF, #9FB0C3); }
.stamp { position: absolute; right: -30px; bottom: -40px; background: ${GREEN}; color: #fff; font-size: 36px; font-weight: 700; padding: 22px 34px; border-radius: 26px; display: flex; gap: 12px; align-items: center; box-shadow: 0 20px 40px rgba(22,163,74,0.4); }
.clist { width: 800px; background: #fff; border-radius: 44px; padding: 56px; box-shadow: 0 40px 80px rgba(30,58,95,0.16); display: flex; flex-direction: column; gap: 34px; }
.clt { font-size: 34px; color: #8492A6; font-weight: 600; }
.cli { display: flex; align-items: center; gap: 28px; font-family: "Space Grotesk"; font-size: 54px; font-weight: 700; color: ${INK}; }
.cbx { width: 64px; height: 64px; border-radius: 20px; display: flex; align-items: center; justify-content: center; }
.cta { display: flex; flex-direction: column; align-items: center; gap: 50px; }
.ctab { display: flex; align-items: center; gap: 20px; background: ${ORANGE}; color: #fff; font-family: "Space Grotesk"; font-size: 48px; font-weight: 700; padding: 40px 56px; border-radius: 40px; box-shadow: 0 30px 60px rgba(249,115,22,0.4); }
.ctaurl { font-size: 38px; color: ${NAVY}; font-weight: 600; }
</style>
</head>
<body>
<div id="root" data-composition-id="main" data-start="0" data-width="${W}" data-height="${H}" data-duration="${TOTAL}">
${runHtml}
${sceneHtml}
${audioHtml}
${musicHtml}
</div>
<script>
document.fonts.ready.then(() => {
  const tl = gsap.timeline({ paused: true });
  const ORANGE = "${ORANGE}", GREEN = "${GREEN}", RED = "${RED}";
  ${anims.join("\n  ")}
  ${scenes.map(s => {
    const sel = x => `#${s.id}${x}`;
    const lines = [];
    const fake = { fromTo: (...a) => lines.push(["fromTo", a]), to: (...a) => lines.push(["to", a]) };
    s._prop.anim(fake, s, sel);
    const ser = v => JSON.stringify(v);
    const propJs = lines.map(([m, a]) => `tl.${m}(${a.map(ser).join(", ")});`).join("\n  ");
    const wordsJs = s.words.map((w, i) => `tl.fromTo("#${s.id}-w${i}", { opacity: 0, y: 34, filter: "blur(16px)" }, { opacity: 1, y: 0, filter: "blur(0px)", duration: ${w.key ? 0.42 : 0.3}, ease: "power3.out" }, ${(s.wt[i] - 0.06).toFixed(3)});`).join("\n  ");
    const nxt = scenes[s.idx + 1], themeChange = nxt && nxt.theme !== s.theme;
    const out = `tl.to("#${s.id}-in", { opacity: 0, y: -40, filter: "blur(14px)", duration: 0.3, ease: "power2.in" }, ${(themeChange ? s.end + 0.05 : s.until - 0.32).toFixed(3)});`;
    return `// ${s.id}\n  ${propJs}\n  ${wordsJs}\n  ${nxt ? out : ""}`;
  }).join("\n  ")}
  window.__timelines["main"] = tl;
});
</script>
</body>
</html>
`;
fs.writeFileSync("index.html", html);
console.log(`ok · ${scenes.length} cenas · ${TOTAL}s · voz: ${timing?.audio ? "sim" : "estimada"}`);
