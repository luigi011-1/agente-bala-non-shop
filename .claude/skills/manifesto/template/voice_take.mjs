// Locução em UMA tomada (entonação contínua), com pausa extra só nas trocas de fundo.
// node voice_take.mjs <voice_id> [speed]
import fs from "node:fs";
import { execFileSync } from "node:child_process";

const VOICE = process.argv[2], SPEED = process.argv[3] ?? "1.1";
if (!VOICE) { console.error("uso: node voice_take.mjs <voice_id> [speed]"); process.exit(1); }
const ROOT = process.env.HF_SKILLS ?? (process.env.HOME + "/.claude/plugins/cache/hyperframes/hyperframes/0.8.140/skills"); // ajuste a versão do plugin
const LAUNCH = ROOT + "/hyperframes/scripts/plugin-cli.mjs";
const TTS = ROOT + "/media-use/audio/scripts/heygen-tts.mjs";
const MIN_THEME_GAP = 0.85, LEAD = 0.5, TAIL = 2.4;

const { scenes } = JSON.parse(fs.readFileSync("script.json", "utf8"));
const says = scenes.map(s => (s.say ?? s.text).replaceAll("*", ""));
const dir = `assets/vo_take_${SPEED}`;
fs.mkdirSync(dir, { recursive: true });
const raw = `${dir}/take.wav`, wordsPath = `${dir}/take.words.json`;
if (!fs.existsSync(raw)) execFileSync("node", [LAUNCH, "--script", TTS, says.join(" "), "-o", raw, "--words", wordsPath, "--voice", VOICE, "--lang", "pt", "--speed", SPEED], { stdio: "inherit" });
const words = JSON.parse(fs.readFileSync(wordsPath, "utf8"));

// distribui as palavras faladas pelas cenas (pela contagem de palavras do texto falado)
const norm = w => w.toLowerCase().normalize("NFD").replace(/[^a-z0-9]/g, "");
let k = 0; const seg = [];
for (const [i, say] of says.entries()) {
  const n = say.split(/\s+/).length, ws = words.slice(k, k + n);
  const expect = norm(say.split(/\s+/)[0]);
  if (ws.length && norm(ws[0].text) !== expect) console.warn(`aviso ${scenes[i].id}: esperava "${expect}", veio "${ws[0].text}"`);
  seg.push({ s: scenes[i], ws, a: ws[0].start, b: ws.at(-1).end }); k += n;
}
if (k !== words.length) console.warn(`aviso: ${words.length} palavras na fala, ${k} no roteiro`);

// corta a tomada em blocos por tema e alonga a pausa entre blocos
const blocks = [];
for (const [i, g] of seg.entries()) {
  if (!blocks.length || seg[i - 1].s.theme !== g.s.theme) blocks.push({ items: [] });
  blocks.at(-1).items.push(g);
}
const out = { audio: `${dir}/locucao.wav`, scenes: {} };
let t = LEAD; const cuts = [];
for (const [bi, b] of blocks.entries()) {
  const first = b.items[0], last = b.items.at(-1);
  const nextA = blocks[bi + 1]?.items[0].a;
  const from = Math.max(0, first.a - 0.06), to = nextA ? (last.b + nextA) / 2 : last.b + 0.4;
  const offset = t - from;
  for (const g of b.items) out.scenes[g.s.id] = { start: +(g.a + offset).toFixed(3), duration: +(g.b - g.a).toFixed(3),
    words: g.s.text.split(/\s+/).length === g.ws.length ? g.ws.map(w => ({ start: +(w.start - g.a).toFixed(3) })) : null };
  cuts.push({ from, to, at: t });
  const natural = nextA ? nextA - last.b : 0;
  t += (to - from) + (nextA ? Math.max(0, MIN_THEME_GAP - natural) : 0);
}
const total = t + TAIL;
const filt = cuts.map((c, i) => `[0:a]atrim=${c.from.toFixed(3)}:${c.to.toFixed(3)},asetpts=PTS-STARTPTS,afade=t=out:st=${(c.to - c.from - 0.04).toFixed(3)}:d=0.04,adelay=${Math.round(c.at * 1000)}:all=1[a${i}]`).join(";")
  + ";" + cuts.map((_, i) => `[a${i}]`).join("") + `amix=inputs=${cuts.length}:normalize=0,apad=whole_dur=${total.toFixed(2)},loudnorm=I=-16:TP=-1.5[out]`;
execFileSync("ffmpeg", ["-y", "-loglevel", "error", "-i", raw, "-filter_complex", filt, "-map", "[out]", "-ar", "44100", "-ac", "1", out.audio]);
fs.writeFileSync("timing.json", JSON.stringify(out, null, 2));
console.log(`ok · uma tomada a ${SPEED}x · ${blocks.length} blocos · ${total.toFixed(1)}s → ${out.audio}`);
