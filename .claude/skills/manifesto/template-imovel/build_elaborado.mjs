// v2 elaborada: história em horários, cartões que expandem, álbum, pino, calendário, cortes no compasso.
// node build2.mjs  → index.html + audio_mix.wav (música lofi + mar + whoosh)
import fs from "node:fs";
import { execFileSync } from "node:child_process";

const W = 1080, H = 1920;
const BAR = 2.86, T0 = 3.0, DOWNBEAT_SRC = 15.93, M = DOWNBEAT_SRC - T0; // música começa em M
const SAND = "#F3ECE1", INK = "#14304A", GOLD = "#C08A3E", ACC = "#FFDDA6", WA = "#25D366", TEAL = "#1F8A70";
const b = n => +(T0 + n * BAR).toFixed(3); // tempo da barra n
const BEAT = BAR / 4;

const S = [
  { type: "full", t0: 0, t1: b(0), media: "g_v1.mp4", ms: 0.0, title: "Seu próximo *fim de semana.*" },
  { type: "card", t0: b(0), t1: b(1), media: "g_f01.jpg", stamp: "Sexta · 18h", text: "Você *chega.*" },
  { type: "full", t0: b(1), t1: b(2), media: "g_v2.mp4", ms: 0.1, stamp: "Sábado · 7h", text: "Café *olhando o mar.*" },
  { type: "full", t0: b(2), t1: b(3), media: "g_v3.mp4", ms: 0.6, stamp: "10h", text: "Piscina com *vista pro mar.*" },
  { type: "pin", t0: b(3), t1: b(4), media: "g_f10.jpg", text: "*100% pé na areia.*" },
  { type: "album", t0: b(4), t1: b(6), cards: [["g_f02.jpg", "Sala integrada"], ["g_f06.jpg", "Cozinha completa"], ["g_f05.jpg", "2 quartos"], ["g_f17.jpg", "Conforto pra família"]], title: "Tudo *pronto pra você.*" },
  { type: "card", t0: b(6), t1: b(7), media: "g_f16.jpg", stamp: "13h", text: "Churrasco na *sua área privativa.*" },
  { type: "duo", t0: b(7), t1: b(8), media: ["g_f15.jpg", "g_f12.jpg"], text: "Área de lazer *completa.*" },
  { type: "duo", t0: b(8), t1: b(10), media: ["g_f13.jpg", "g_f18.jpg"], stamp: "17h40", text: "*Esse pôr do sol.*" },
  { type: "full", t0: b(10), t1: b(11), media: "g_f14.jpg", stamp: "Domingo", text: "Você *já quer voltar.*" },
  { type: "final", t0: b(11), t1: b(13) + 1.6 }
];
const TOTAL = +S.at(-1).t1.toFixed(2);

const IC = {
  wave: '<path d="M2 12c2 0 2-2 4-2s2 2 4 2 2-2 4-2 2 2 4 2 2-2 4-2"/><path d="M2 18c2 0 2-2 4-2s2 2 4 2 2-2 4-2 2 2 4 2 2-2 4-2"/><path d="M12 3v4"/>',
  bed: '<path d="M2 20v-8a2 2 0 0 1 2-2h16a2 2 0 0 1 2 2v8"/><path d="M4 10V6a2 2 0 0 1 2-2h12a2 2 0 0 1 2 2v4"/><path d="M12 4v6M2 18h20"/>',
  shield: '<path d="M20 13c0 5-3.5 7.5-7.7 9a1 1 0 0 1-.6 0C7.5 20.5 4 18 4 13V6a1 1 0 0 1 1-1c2 0 4.5-1.2 6.2-2.7a1.2 1.2 0 0 1 1.6 0C14.5 3.8 17 5 19 5a1 1 0 0 1 1 1z"/><path d="m9 12 2 2 4-4"/>',
  flame: '<path d="M8.5 14.5A2.5 2.5 0 0 0 11 12c0-1.4-.5-2-1-3-1.1-2.1-.2-4 2-6 .5 2.5 2 4.9 4 6.5 2 1.6 3 3.5 3 5.5a7 7 0 1 1-14 0c0-1.2.4-2.3 1-3.4.2 1.5 1.3 2.9 2.5 2.9Z"/>',
  palm: '<path d="M13 8c0-2.8-2.2-5-5-5-1.8 0-3.4 1-4.2 2.5"/><path d="M13 7.9C15 5 18.5 4.5 21 6"/><path d="M13 8.1c3 .1 5.6 2 6.3 5"/><path d="M13 8c-2.9.4-5 3-4.7 6"/><path d="M13 8c.6 4.5-.4 9.5-3 13"/><path d="M5 21h12"/>',
  check: '<path d="M20 6 9 17l-5-5"/>'
};
const ic = (n, s, c, w = 1.9) => `<svg viewBox="0 0 24 24" width="${s}" height="${s}" fill="none" stroke="${c}" stroke-width="${w}" stroke-linecap="round" stroke-linejoin="round">${IC[n]}</svg>`;
const FICHA = [["wave", "100% pé na areia"], ["bed", "2 quartos"], ["shield", "Condomínio fechado"], ["flame", "Churrasqueira privativa"], ["palm", "Área de lazer completa"]];

const words = text => { const out = []; let key = false;
  for (let w of text.split(/\s+/)) { let k = key; if (w.startsWith("*")) { w = w.slice(1); k = key = true; }
    let close = false; if (w.endsWith("*")) { w = w.slice(0, -1); close = true; } out.push({ w, k }); if (close) key = false; } return out; };

const html = [], js = [], whoosh = [];
const media = (src, id, cls = "full") => src.endsWith(".mp4") ? null : `<img class="${cls}" id="${id}" src="assets/${src}" alt="">`;
const textBlock = (id, text, at, until, cls = "txt") => {
  const ws = words(text), step = Math.min(0.24, (until - at) * 0.35 / ws.length);
  html.push(`<div class="clip ${cls}" id="${id}" data-start="${at.toFixed(3)}" data-duration="${(until - at).toFixed(3)}" data-track-index="6"><div class="tin" id="${id}-in">${ws.map((w, k) => `<span class="w ${w.k ? "k" : ""}" id="${id}-${k}">${w.w}</span>`).join(" ")}</div></div>`);
  ws.forEach((w, k) => js.push(`tl.fromTo("#${id}-${k}", { opacity: 0, y: 30, filter: "blur(14px)" }, { opacity: 1, y: 0, filter: "blur(0px)", duration: ${w.k ? 0.5 : 0.36}, ease: "power3.out" }, ${(at + k * step).toFixed(3)});`));
  js.push(`tl.to("#${id}-in", { opacity: 0, filter: "blur(10px)", duration: 0.22, ease: "power2.in" }, ${(until - 0.24).toFixed(3)});`);
};
const stampBlock = (id, txt, at, until) => {
  html.push(`<div class="clip stamp" id="${id}" data-start="${at.toFixed(3)}" data-duration="${(until - at).toFixed(3)}" data-track-index="7"><div class="sin" id="${id}-in"><svg viewBox="0 0 24 24" width="34" height="34" fill="none" stroke="${INK}" stroke-width="2.2" stroke-linecap="round"><circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/></svg>${txt}</div></div>`);
  js.push(`tl.fromTo("#${id}-in", { opacity: 0, y: -24, scale: 0.9 }, { opacity: 1, y: 0, scale: 1, duration: 0.4, ease: "back.out(2)" }, ${(at + 0.05).toFixed(3)});`);
  js.push(`tl.to("#${id}-in", { opacity: 0, duration: 0.2 }, ${(until - 0.22).toFixed(3)});`);
};

S.forEach((s, i) => {
  const id = `s${i}`, du = s.t1 - s.t0;
  if (s.type === "full") {
    if (s.media.endsWith(".mp4")) {
      html.push(`<div class="layer" id="${id}-w"><video class="clip full" id="${id}-v" src="assets/${s.media}" muted playsinline data-start="${s.t0}" data-duration="${du.toFixed(3)}" data-media-start="${s.ms}" data-track-index="${i % 2}"></video></div>`);
      js.push(`tl.fromTo("#${id}-w", { scale: 1.1 }, { scale: 1.0, duration: 0.55, ease: "power3.out" }, ${s.t0});`);
    } else {
      html.push(`<div class="clip layer" id="${id}-w" data-start="${s.t0}" data-duration="${du.toFixed(3)}" data-track-index="${i % 2}">${media(s.media, id + "-i")}</div>`);
      js.push(`tl.fromTo("#${id}-i", { scale: 1.12 }, { scale: 1.02, duration: ${du.toFixed(3)}, ease: "power2.out" }, ${s.t0});`);
    }
  }
  if (s.type === "card") { // fundo areia, foto entra como cartão e expande até tela cheia no meio do compasso
    html.push(`<div class="clip layer sand" id="${id}-w" data-start="${s.t0}" data-duration="${du.toFixed(3)}" data-track-index="${i % 2}"><div class="cardm" id="${id}-c">${media(s.media, id + "-i")}</div></div>`);
    js.push(`tl.fromTo("#${id}-c", { clipPath: "inset(560px 150px 560px 150px round 48px)", rotation: -4, y: 120 }, { clipPath: "inset(380px 90px 520px 90px round 48px)", rotation: 0, y: 0, duration: 0.6, ease: "power3.out" }, ${s.t0});`);
    js.push(`tl.to("#${id}-c", { clipPath: "inset(0px 0px 0px 0px round 0px)", duration: 0.7, ease: "power3.inOut" }, ${(s.t0 + BEAT * 2).toFixed(3)});`);
    js.push(`tl.fromTo("#${id}-i", { scale: 1.15 }, { scale: 1.02, duration: ${du.toFixed(3)}, ease: "power2.out" }, ${s.t0});`);
    whoosh.push(s.t0 - 0.12, s.t0 + BEAT * 2 - 0.1);
  }
  if (s.type === "duo") { // duas fotos, corte na metade (no tempo)
    const mid = +(s.t0 + du / 2).toFixed(3);
    html.push(`<div class="clip layer" id="${id}-a" data-start="${s.t0}" data-duration="${(mid - s.t0).toFixed(3)}" data-track-index="${i % 2}">${media(s.media[0], id + "-ia")}</div>`);
    html.push(`<div class="clip layer" id="${id}-b" data-start="${mid}" data-duration="${(s.t1 - mid).toFixed(3)}" data-track-index="${(i + 1) % 2}">${media(s.media[1], id + "-ib")}</div>`);
    js.push(`tl.fromTo("#${id}-ia", { scale: 1.12 }, { scale: 1.02, duration: ${(mid - s.t0).toFixed(3)}, ease: "power2.out" }, ${s.t0});`);
    js.push(`tl.fromTo("#${id}-ib", { scale: 1.12 }, { scale: 1.02, duration: ${(s.t1 - mid).toFixed(3)}, ease: "power2.out" }, ${mid});`);
  }
  if (s.type === "pin") {
    html.push(`<div class="clip layer" id="${id}-w" data-start="${s.t0}" data-duration="${du.toFixed(3)}" data-track-index="${i % 2}">${media(s.media, id + "-i")}
      <div class="pin" id="${id}-p"><div class="pulse" id="${id}-pu"></div><svg viewBox="0 0 24 24" width="120" height="120"><path d="M12 2a7 7 0 0 0-7 7c0 5.2 7 13 7 13s7-7.8 7-13a7 7 0 0 0-7-7Z" fill="#E4572E" stroke="#fff" stroke-width="1.4"/><circle cx="12" cy="9" r="2.6" fill="#fff"/></svg><div class="plabel" id="${id}-pl">Praia das Fontes · CE</div></div></div>`);
    js.push(`tl.fromTo("#${id}-i", { scale: 1.25 }, { scale: 1.05, duration: ${du.toFixed(3)}, ease: "power2.out" }, ${s.t0});`);
    js.push(`tl.fromTo("#${id}-p", { y: -500, opacity: 0 }, { y: 0, opacity: 1, duration: 0.5, ease: "bounce.out" }, ${(s.t0 + BEAT).toFixed(3)});`);
    js.push(`tl.fromTo("#${id}-pu", { scale: 0.2, opacity: 0.9 }, { scale: 2.4, opacity: 0, duration: 0.9, ease: "power2.out" }, ${(s.t0 + BEAT + 0.45).toFixed(3)});`);
    js.push(`tl.fromTo("#${id}-pl", { opacity: 0, x: -20 }, { opacity: 1, x: 0, duration: 0.4 }, ${(s.t0 + BEAT + 0.55).toFixed(3)});`);
  }
  if (s.type === "album") {
    const rot = [-6, 5, -3, 4], dx = [-30, 40, -20, 25];
    html.push(`<div class="clip layer sand" id="${id}-w" data-start="${s.t0}" data-duration="${du.toFixed(3)}" data-track-index="${i % 2}">${s.cards.map(([f, lab], k) =>
      `<div class="acard" id="${id}-c${k}"><img class="full" src="assets/${f}" alt=""><div class="alab">${lab}</div></div>`).join("")}</div>`);
    s.cards.forEach((_, k) => {
      const at = s.t0 + 0.2 + k * BEAT * 2;
      js.push(`tl.fromTo("#${id}-c${k}", { opacity: 0, y: 900, rotation: ${rot[k] * 3}, x: ${dx[k] * 3} }, { opacity: 1, y: 0, rotation: ${rot[k]}, x: ${dx[k]}, duration: 0.6, ease: "power3.out" }, ${at.toFixed(3)});`);
      if (k > 0) js.push(`tl.to("#${id}-c${k - 1}", { scale: 0.93, opacity: 0.55, duration: 0.5 }, ${at.toFixed(3)});`);
      whoosh.push(at - 0.08);
    });
    textBlock(id + "-t", s.title, s.t0 + 0.3, s.t1, "txt top");
  }
  if (s.type === "final") {
    const days = Array.from({ length: 35 }, (_, k) => k - 2); // grade de 5 semanas, sem mês nem datas reais
    const sel = [17, 18, 19]; // sex, sáb, dom (dia 1 cai na quarta)
    html.push(`<div class="clip layer sand" id="${id}-w" data-start="${s.t0}" data-duration="${du.toFixed(3)}" data-track-index="${i % 2}">
      <div class="fin">
        <div class="ftitle" id="${id}-ti">Praia das Fontes</div>
        <div class="fsub" id="${id}-su">Temporada · apartamento pé na areia</div>
        <div class="ficons">${FICHA.map(([n, l], k) => `<div class="fic" id="${id}-f${k}"><div class="fbub">${ic(n, 52, TEAL)}</div><span>${l}</span></div>`).join("")}</div>
        <div class="cal" id="${id}-cal"><div class="calh"><span>D</span><span>S</span><span>T</span><span>Q</span><span>Q</span><span>S</span><span>S</span></div><div class="calg">${days.map((d, k) => `<div class="cd ${d < 1 || d > 30 ? "off" : ""}" id="${id}-d${k}">${d >= 1 && d <= 30 ? d : ""}</div>`).join("")}</div></div>
        <div class="fwa" id="${id}-wa"><svg viewBox="0 0 24 24" width="48" height="48" fill="#fff"><path d="M12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2Zm5.3 14.2c-.2.6-1.3 1.2-1.8 1.2-.5.1-1 .2-3.3-.7-2.8-1.1-4.5-3.9-4.7-4.1-.1-.2-1.1-1.5-1.1-2.9s.7-2 1-2.3c.2-.3.5-.3.7-.3h.5c.2 0 .4 0 .6.5l.8 2c.1.2.1.4 0 .5l-.4.6-.4.4c-.1.1-.3.3-.1.6.2.3.8 1.3 1.6 2.1 1.1 1 2 1.3 2.3 1.4.3.1.5.1.6-.1l.9-1c.2-.3.4-.2.7-.1l1.9.9c.3.1.5.2.5.3.1.2.1.6-.1 1.2Z"/></svg>Reserve sua data no WhatsApp</div>
      </div></div>`);
    js.push(`tl.fromTo("#${id}-ti", { opacity: 0, y: 40, filter: "blur(12px)" }, { opacity: 1, y: 0, filter: "blur(0px)", duration: 0.6, ease: "power3.out" }, ${s.t0});`);
    js.push(`tl.fromTo("#${id}-su", { opacity: 0 }, { opacity: 1, duration: 0.4 }, ${(s.t0 + 0.35).toFixed(3)});`);
    FICHA.forEach((_, k) => js.push(`tl.fromTo("#${id}-f${k}", { opacity: 0, y: 40, scale: 0.8 }, { opacity: 1, y: 0, scale: 1, duration: 0.4, ease: "back.out(2)" }, ${(s.t0 + BEAT + k * BEAT / 2).toFixed(3)});`));
    const ct = s.t0 + BAR;
    js.push(`tl.fromTo("#${id}-cal", { opacity: 0, y: 60 }, { opacity: 1, y: 0, duration: 0.5, ease: "power3.out" }, ${(ct - 0.3).toFixed(3)});`);
    sel.forEach((d, k) => js.push(`tl.fromTo("#${id}-d${d + 2}", { backgroundColor: "rgba(31,138,112,0)", color: "${INK}", scale: 1 }, { backgroundColor: "${TEAL}", color: "#ffffff", scale: 1.12, duration: 0.25, ease: "back.out(3)" }, ${(ct + 0.3 + k * BEAT).toFixed(3)});`));
    js.push(`tl.fromTo("#${id}-wa", { opacity: 0, y: 40, scale: 0.9 }, { opacity: 1, y: 0, scale: 1, duration: 0.45, ease: "back.out(1.8)" }, ${(ct + 0.3 + 3 * BEAT).toFixed(3)});`);
    js.push(`tl.to("#${id}-wa", { scale: 1.05, duration: ${BEAT / 2}, yoyo: true, repeat: 5, ease: "sine.inOut" }, ${(ct + 0.3 + 4 * BEAT).toFixed(3)});`);
    whoosh.push(s.t0 - 0.1);
  }
  if (["full", "duo", "pin", "card"].includes(s.type)) { const gs = s.type === "card" ? s.t0 + BEAT * 2 + 0.3 : s.t0;
    html.push(`<div class="clip grad" id="${id}-g" data-start="${gs.toFixed(3)}" data-duration="${(s.t1 - gs).toFixed(3)}" data-track-index="5"></div>`);
    if (s.type === "card") js.push(`tl.fromTo("#${id}-g", { opacity: 0 }, { opacity: 1, duration: 0.4 }, ${gs.toFixed(3)});`); }
  if (s.stamp) stampBlock(id + "-st", s.stamp, s.t0, s.t1);
  if (s.text) textBlock(id + "-t", s.text, s.t0 + (s.type === "card" ? BEAT * 2 + 0.2 : 0.25), s.t1);
  if (s.title && s.type === "full") textBlock(id + "-t", s.title, 0.35, s.t1, "txt hook");
});

// áudio: lofi a partir de M + mar baixinho + whoosh
const wsrc = "assets/whoosh.wav"; // copie de .claude/skills/manifesto/template/whoosh.wav
const args = ["-y", "-loglevel", "error", "-ss", M.toFixed(3), "-t", TOTAL.toFixed(2), "-i", "assets/lofi.mp3", "-i", "assets/mar.wav"];
whoosh.forEach(() => args.push("-i", wsrc));
let f = `[0:a]aformat=channel_layouts=mono,afade=t=in:d=0.6,afade=t=out:st=${(TOTAL - 2.2).toFixed(2)}:d=2.2,volume=0.85[m];[1:a]atrim=0:${TOTAL},volume=0.32[s];`;
whoosh.forEach((w, k) => { f += `[${k + 2}:a]volume=0.5,adelay=${Math.max(0, Math.round(w * 1000))}:all=1[w${k}];`; });
f += `[m][s]${whoosh.map((_, k) => `[w${k}]`).join("")}amix=inputs=${2 + whoosh.length}:normalize=0,loudnorm=I=-14:TP=-1.2[o]`;
execFileSync("ffmpeg", [...args, "-filter_complex", f, "-map", "[o]", "-ar", "44100", "-ac", "2", "assets/audio_mix.wav"]);

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
html, body { width: ${W}px; height: ${H}px; overflow: hidden; background: ${SAND}; }
#root { position: relative; width: 100%; height: 100%; overflow: hidden; font-family: "Inter", sans-serif; }
.layer { position: absolute; inset: 0; overflow: hidden; }
.sand { background: radial-gradient(120% 80% at 50% 30%, #FBF6EE 0%, ${SAND} 60%, #E9DFCF 100%); }
.full { position: absolute; inset: 0; width: 100%; height: 100%; object-fit: cover; display: block; }
.cardm { position: absolute; inset: 0; overflow: hidden; box-shadow: 0 40px 80px rgba(60,40,10,0.25); }
.grad { position: absolute; inset: 0; z-index: 4; pointer-events: none; background: linear-gradient(180deg, rgba(0,0,0,0.3) 0%, rgba(0,0,0,0) 20%, rgba(0,0,0,0) 50%, rgba(0,0,0,0.6) 100%); }
.txt { position: absolute; left: 0; right: 0; bottom: 290px; z-index: 10; display: flex; justify-content: center; padding: 0 80px; }
.txt.top { top: 210px; bottom: auto; }
.txt.top .w { color: ${INK}; text-shadow: none; }
.txt.top .w.k { color: ${GOLD}; }
.txt.hook { top: 0; bottom: 0; align-items: center; }
.txt.hook .w { font-size: 74px; } .txt.hook .w.k { font-size: 128px; }
.tin { text-align: center; line-height: 1.1; font-size: 66px; word-spacing: 0.04em; }
.w { display: inline-block; color: #fff; font-size: 66px; font-weight: 600; letter-spacing: -0.02em; text-shadow: 0 4px 24px rgba(0,0,0,0.45); }
.w.k { font-family: "Playfair Display", serif; font-style: italic; font-size: 108px; color: ${ACC}; letter-spacing: -0.01em; }
.stamp { position: absolute; left: 0; right: 0; top: 150px; z-index: 11; display: flex; justify-content: center; }
.sin { display: flex; align-items: center; gap: 14px; background: rgba(255,255,255,0.94); color: ${INK}; font-size: 38px; font-weight: 700; letter-spacing: 0.08em; text-transform: uppercase; padding: 18px 34px; border-radius: 60px; box-shadow: 0 14px 34px rgba(0,0,0,0.22); }
.acard { position: absolute; left: 150px; top: 520px; width: 780px; height: 1000px; border-radius: 40px; overflow: hidden; border: 14px solid #fff; box-shadow: 0 40px 80px rgba(60,40,10,0.28); }
.alab { position: absolute; left: 30px; bottom: 30px; background: rgba(255,255,255,0.95); color: ${INK}; font-size: 42px; font-weight: 700; padding: 18px 32px; border-radius: 50px; }
.pin { position: absolute; left: 470px; top: 760px; display: flex; flex-direction: column; align-items: center; z-index: 5; }
.pulse { position: absolute; top: 96px; width: 80px; height: 30px; border-radius: 50%; border: 5px solid #fff; }
.plabel { margin-top: 10px; background: #fff; color: ${INK}; font-size: 38px; font-weight: 700; padding: 14px 28px; border-radius: 40px; box-shadow: 0 12px 30px rgba(0,0,0,0.3); white-space: nowrap; }
.fin { position: absolute; inset: 0; display: flex; flex-direction: column; align-items: center; justify-content: center; padding: 0 70px; }
.ftitle { white-space: nowrap; text-align: center; font-family: "Playfair Display", serif; font-style: italic; font-size: 118px; color: ${INK}; line-height: 1; }
.fsub { margin-top: 20px; font-size: 32px; font-weight: 700; letter-spacing: 0.16em; text-transform: uppercase; color: ${GOLD}; }
.ficons { margin-top: 80px; display: flex; flex-wrap: wrap; justify-content: center; gap: 30px 26px; width: 940px; }
.fic { width: 280px; display: flex; flex-direction: column; align-items: center; gap: 16px; text-align: center; font-size: 34px; font-weight: 600; color: ${INK}; line-height: 1.2; }
.fbub { width: 110px; height: 110px; border-radius: 34px; background: #fff; display: flex; align-items: center; justify-content: center; box-shadow: 0 16px 34px rgba(60,40,10,0.14); }
.cal { margin-top: 80px; width: 860px; background: #fff; border-radius: 40px; padding: 34px 40px; box-shadow: 0 30px 60px rgba(60,40,10,0.16); }
.calh, .calg { display: grid; grid-template-columns: repeat(7, 1fr); gap: 10px; text-align: center; }
.calh span { font-size: 26px; font-weight: 700; color: #9AA5B1; padding-bottom: 12px; }
.cd { height: 74px; border-radius: 18px; display: flex; align-items: center; justify-content: center; font-size: 30px; font-weight: 600; color: ${INK}; }
.cd.off { opacity: 0; }
.fwa { margin-top: 70px; display: flex; align-items: center; gap: 18px; background: ${WA}; color: #fff; font-size: 44px; font-weight: 700; padding: 34px 50px; border-radius: 40px; box-shadow: 0 22px 48px rgba(37,211,102,0.45); }
</style>
</head>
<body>
<div id="root" data-composition-id="main" data-start="0" data-width="${W}" data-height="${H}" data-duration="${TOTAL}">
${html.join("\n")}
<audio id="mix" src="assets/audio_mix.wav" data-start="0" data-duration="${TOTAL}" data-track-index="9" data-volume="1"></audio>
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
console.log(`ok · ${S.length} cenas · ${TOTAL}s · música a partir de ${M.toFixed(2)}s · ${whoosh.length} whoosh`);
