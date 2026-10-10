"""Acabamento HyperFrames da edição (Luigi, 2026-10-10: "o nosso era pra ter um resultado bem melhor").
O motor v4 corta e monta a base; este módulo põe por cima, sem tocar no corte nem no ritmo aprovados:

1. Palavra de pico ATRÁS do avatar: o avatar é recortado (hyperframes remove-background, u2net_human_seg, CPU)
   só nas janelas dos picos, a palavra é animada letra por letra num render transparente da HyperFrames e o
   recorte decide onde ela aparece (atrás do corpo, nunca sobre o rosto). Altura escolhida pelo próprio recorte:
   ~35% da palavra escondida pelo corpo, acima da legenda.
2. Zoom de pico: punch-in leve (8%) no tempo da palavra, centrado na cabeça, volta antes da próxima frase.
3. Efeitos do catálogo HyperFrames: grão de filme (grain-overlay, opcional) e, no Auraly, o flash
   de câmera (editorial-flash-overlay) no lugar do flash chapado do ffmpeg.
4. SFX da biblioteca HyperFrames (media-use, ../sfx_hf): pacotes em PACOTES_SFX (troca de take + pico). A música
   fica a -18 dB da voz (a edição não tem silêncio, então ducking não muda nada).
Regras da HyperFrames têm prioridade (Luigi, 2026-10-10): grão desligado por padrão (embedded-captions: a filmagem
não se gradua; grão só como reação), zoom só no pico (reação "punch"), palavra embutida escassa.

Uso dentro do editar.py (--acabamento) ou sozinho, numa pasta de trabalho já editada:
    python3 acabamento.py /tmp/edicao/<nome>-<tag> [--legenda caption-highlight] [--sfx cinema] [--picos fake,cloudy]
                           [--sem-zoom] [--grao]
"""
import json
import os
import re
import shutil
import subprocess
import sys

import numpy as np

AQUI = os.path.dirname(os.path.abspath(__file__))
W, H, FPS = 1080, 1920, 30
HF = ["npx", "-y", "hyperframes@0.8.144"]
# fonte da palavra de pico: a do DNA "loud" do embedded-captions (Anton, caixa-alta condensada); serifada = a nossa
FONTES_PICO = {"anton": ("Anton400.woff2", "Anton", 400), "serifada": ("Merriweather900.woff2", "Merri", 900),
               "montserrat": ("Montserrat900.woff2", "Montserrat", 900)}
ZOOM = 0.08            # punch-in do pico
OCUPA = 0.20           # fração da palavra escondida pelo corpo: 35% comia as letras do meio (V02, 2026-10-10)
GRAO = 0.06            # opacidade do grão
LEG_TOPO = 880         # topo da legenda FitWell: a palavra de pico fica acima
VAZIAS = {"the", "a", "an", "and", "or", "but", "of", "to", "in", "on", "at", "for", "with", "that", "this", "it",
          "is", "was", "be", "are", "your", "my", "i", "me", "so", "if", "just", "what", "when", "they", "she", "he",
          "we", "you", "it's", "its", "down", "some", "like", "more", "one", "want", "never", "miss", "made", "way",
          "there", "their", "these", "those", "about", "which", "would", "could", "should", "every", "right", "here"}
CTA = {"comment", "follow", "yes", "link", "caption", "below", "save", "share", "subscribe", "222", "stories", "profile"}


def _sh(cmd, **kw):
    return subprocess.run(cmd, check=True, capture_output=True, text=True, **kw).stdout


def _limpa(w):
    return re.sub(r"[^a-z0-9']", "", w.lower())


# ---------- 1. picos ----------
def escolher_picos(ws, total, mudos=(), forcados=None, espaco=5.0):
    """ws: [{w, t, k}] no tempo do vídeo editado. Regras do embedded-captions: no máximo um pico por bloco,
    espaçados (aqui 5s), nunca dois iguais. Pico = palavra que fecha a frase (o payoff: candle, cloudy,
    imitation); vírgula vale menos; o CTA não leva pico. `forcados` (lista de palavras) manda."""
    cand = []
    for i, w in enumerate(ws):
        if w["k"] in mudos or w["t"] < 0.3 or w["t"] > total - 1.2:
            continue
        lw = _limpa(w["w"])
        if forcados is not None:
            if lw in forcados:
                cand.append((9, i))
            continue
        if lw in VAZIAS or lw in CTA or len(lw) < 4 and not re.search(r"\d", lw):
            continue
        if any(_limpa(x["w"]) in CTA for x in ws[max(0, i - 6):i + 6]):  # dentro do CTA
            continue
        nota = 3 if re.search(r"[.!?]$", w["w"]) else 2 if re.search(r"[,;:]$", w["w"]) else 0
        if not nota:
            continue
        cand.append((nota + min(len(lw), 9) / 10, i))
    escolhidos, usados = [], set()
    for nota, i in sorted(cand, key=lambda x: (-x[0], ws[x[1]]["t"])):
        t, lw = ws[i]["t"], _limpa(ws[i]["w"])
        if lw not in usados and all(abs(t - ws[j]["t"]) >= espaco for j in escolhidos):
            escolhidos.append(i); usados.add(lw)
    escolhidos.sort()
    picos = []
    for i in escolhidos:
        t = ws[i]["t"]
        # janela: da palavra até o começo da frase seguinte (mínimo 1,2s, máximo 1,8s)
        prox = next((ws[j]["t"] for j in range(i + 1, len(ws)) if re.search(r"[.!?]$", ws[j - 1]["w"])), total)
        fim = min(total - 0.05, t + 1.8, max(t + 1.2, prox - 0.05))
        picos.append(dict(w=re.sub(r"[.,!?;:]$", "", ws[i]["w"]), t=t, a=max(0.0, t - 0.08), b=fim))
    return picos


# ---------- 2. recorte do avatar nas janelas ----------
def recortar(base, picos, tmp, log=print):
    os.makedirs(f"{tmp}/hf_recorte", exist_ok=True)
    for n, p in enumerate(picos):
        f0, f1 = round(p["a"] * FPS), round(p["b"] * FPS)
        p["f0"], p["f1"] = f0, f1
        chave = f"{base}|{f0}|{f1}"
        fg = f"{tmp}/hf_recorte/fg{n:02d}.webm"
        if os.path.exists(fg) and open(f"{fg}.key").read() == chave:
            p["fg"] = fg
            continue
        corte = f"{tmp}/hf_recorte/corte{n:02d}.mp4"
        _sh(["ffmpeg", "-y", "-loglevel", "error", "-i", base, "-vf",
             f"trim=start_frame={f0}:end_frame={f1},setpts=PTS-STARTPTS", "-an", "-c:v", "libx264", "-crf", "12",
             "-preset", "veryfast", corte])
        log(f"   recorte do avatar {n + 1}/{len(picos)} ({(f1 - f0) / FPS:.1f}s)")
        # CPU: o CoreML corrompe o alfa do rosto (embedded-captions, anti-patterns)
        _sh(HF + ["remove-background", corte, "-o", fg, "--device", "cpu", "--quality", "best"], cwd=tmp)
        open(f"{fg}.key", "w").write(chave)
        p["fg"] = fg


def _alfas(webm):
    """Todos os quadros de alfa (uint8, H x W) de um webm transparente."""
    raw = subprocess.run(["ffmpeg", "-loglevel", "error", "-c:v", "libvpx-vp9", "-i", webm, "-vf", "alphaextract",
                          "-pix_fmt", "gray", "-f", "rawvideo", "-"], capture_output=True, check=True).stdout
    return np.frombuffer(raw, np.uint8).reshape(-1, H, W)


def medir(picos, base, fonte="anton"):
    """Tamanho, altura e cor da palavra de cada pico a partir do recorte; centro do zoom na cabeça."""
    from PIL import ImageFont
    arq = os.path.join(AQUI, "fonts", FONTES_PICO[fonte][0])
    for p in picos:
        al = _alfas(p["fg"])
        corpo = (al > 128)
        uniao = corpo.any(axis=0)
        meio = corpo[min(len(corpo) - 1, round((p["t"] - p["a"]) * FPS))]
        linhas = np.where(meio.sum(axis=1) > 12)[0]
        topo = int(linhas[0]) if len(linhas) else 300
        cab = meio[topo:topo + 260]
        xs = np.where(cab.any(axis=0))[0]
        p["cx"] = float(xs.mean()) if len(xs) else W / 2
        p["cy"] = float(min(H * 0.45, topo + 300))
        txt = p["w"].upper()
        tam = 340
        while tam > 120 and ImageFont.truetype(arq, tam).getlength(txt) > 940:
            tam -= 8
        f = ImageFont.truetype(arq, tam)
        larg = f.getlength(txt)
        x0, x1 = int((W - larg) / 2), int((W + larg) / 2)
        bb = f.getbbox("H")
        alt = int(bb[3] - bb[1])  # altura da caixa-alta
        melhor = None
        for cy in range(max(alt // 2 + 60, topo + 40), LEG_TOPO - alt // 2 - 30, 10):
            caixa = uniao[cy - alt // 2:cy + alt // 2, x0:x1]
            occ = float(caixa.mean()) if caixa.size else 1.0
            if occ > 0.55:
                continue
            nota = abs(occ - OCUPA)
            if melhor is None or nota < melhor[0]:
                melhor = (nota, cy, occ)
        if melhor is None:  # corpo largo demais: a palavra vai para cima da cabeça
            melhor = (0, max(alt // 2 + 120, topo - alt // 2 - 40), 0.0)
        _, cy, occ = melhor
        p.update(tam=tam, cy=int(cy), occ=round(occ, 2), fonte=fonte)
        # cor: fundo claro atrás da palavra pede texto escuro (screen em fundo claro some)
        raw = subprocess.run(["ffmpeg", "-loglevel", "error", "-ss", f"{p['t']:.3f}", "-i", base, "-frames:v", "1",
                              "-pix_fmt", "gray", "-f", "rawvideo", "-"], capture_output=True, check=True).stdout
        cinza = np.frombuffer(raw, np.uint8).reshape(H, W)[cy - alt // 2:cy + alt // 2, x0:x1]
        fora = ~uniao[cy - alt // 2:cy + alt // 2, x0:x1]
        lum = float(cinza[fora].mean()) if fora.any() else 100.0
        p["escuro"] = lum > 170
    return picos


# ---------- 3. camadas HyperFrames ----------
PAGINA = """<!doctype html>
<html lang="en"><head><meta charset="UTF-8" />
<script src="https://cdn.jsdelivr.net/npm/gsap@3.14.2/dist/gsap.min.js"></script>
<style>
{fontes}
* {{ margin: 0; padding: 0; box-sizing: border-box; }}
html, body {{ width: {W}px; height: {H}px; overflow: hidden; background: transparent; }}
#root {{ position: relative; width: 100%; height: 100%; background: transparent; }}
.pico {{ position: absolute; left: 0; right: 0; display: flex; align-items: center; justify-content: center;
  color: #fff; line-height: 1; white-space: nowrap; text-shadow: 0 8px 34px rgba(0,0,0,0.38); }}
.pico.escuro {{ color: #161616; text-shadow: 0 6px 26px rgba(255,255,255,0.45); }}
.pico span {{ display: inline-block; }}
{css}
</style></head>
<body>
<div id="root" data-composition-id="main" data-start="0" data-duration="{total:.3f}" data-width="{W}" data-height="{H}">
{html}
</div>
<script>
const tl = gsap.timeline({{ paused: true }});
{js}
window.__timelines["main"] = tl;
</script></body></html>
"""

# grain-overlay do catálogo (hyperframes add grain-overlay), com opacidade de acabamento
GRAO_CSS = """#grain-overlay { position: absolute; inset: 0; pointer-events: none; overflow: hidden; }
@keyframes hf-grain-noise { 0%, 100% { transform: translate(0, 0); } 10% { transform: translate(-5%, -5%); }
  20% { transform: translate(-10%, 5%); } 30% { transform: translate(5%, -10%); } 40% { transform: translate(-5%, 15%); }
  50% { transform: translate(-10%, 5%); } 60% { transform: translate(15%, 0); } 70% { transform: translate(0, 10%); }
  80% { transform: translate(-15%, 0); } 90% { transform: translate(10%, 5%); } }
#grain-overlay .grain-texture { position: absolute; top: -50%; left: -50%; width: 200%; height: 200%;
  background: url("data:image/svg+xml,%3Csvg viewBox='0 0 256 256' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='noise'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.65' numOctaves='3' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23noise)'/%3E%3C/svg%3E");
  opacity: OPAC; animation: hf-grain-noise 0.5s steps(1) infinite; }"""

# editorial-flash-overlay do catálogo, em camadas por flash
FLASH_CSS = """.ef { position: absolute; inset: -12%; overflow: hidden; pointer-events: none; }
.ef .l { position: absolute; inset: 0; opacity: 0; }
.ef .wash { background: rgb(255 253 250); }
.ef .core { inset: -18%; background: radial-gradient(ellipse 68% 92% at 37% 47%, rgb(255 255 255) 0%,
  rgb(255 255 255 / 98%) 20%, rgb(255 253 250 / 86%) 45%, rgb(255 174 105 / 32%) 67%, transparent 86%);
  transform-origin: 38% 48%; }"""


def _fontes_css():
    return "\n".join(f'@font-face {{ font-family: "{fam}"; src: url("fonts/{arq}") format("woff2"); font-weight: {peso}; }}'
                     for arq, fam, peso in FONTES_PICO.values())


def _render(pasta, html, saida, log):
    os.makedirs(f"{pasta}/fonts", exist_ok=True)
    for arq, _, _ in FONTES_PICO.values():
        shutil.copy(os.path.join(AQUI, "fonts", arq), f"{pasta}/fonts/")
    open(f"{pasta}/index.html", "w", encoding="utf8").write(html)
    out = subprocess.run(HF + ["lint", "."], cwd=pasta, capture_output=True, text=True)
    erros = re.search(r"(\d+) error\(s\)", out.stdout + out.stderr)
    if erros and int(erros.group(1)):
        raise RuntimeError(f"lint HyperFrames com erro em {pasta}:\n{out.stdout[-2000:]}")
    _sh(HF + ["render", ".", "--format", "webm", "-o", saida], cwd=pasta)
    log(f"   render HyperFrames: {os.path.basename(saida)}")


def camada_picos(picos, total, tmp, log=print):
    html, js = [], []
    for n, p in enumerate(picos):
        letras = "".join(f"<span>{c}</span>" if c != " " else "<span>&nbsp;</span>" for c in p["w"].upper())
        html.append(f'<div class="clip pico{" escuro" if p["escuro"] else ""}" id="p{n}" data-start="{p["a"]:.3f}" '
                    f'data-duration="{p["b"] - p["a"]:.3f}" data-track-index="{1 + n % 2}" '
                    f'style="top: {p["cy"] - p["tam"] // 2}px; height: {p["tam"]}px; font-size: {p["tam"]}px; font-family: {FONTES_PICO[p["fonte"]][1]}; '
                    f'font-weight: {FONTES_PICO[p["fonte"]][2]};"><div id="p{n}in">{letras}</div></div>')
        js.append(f'tl.fromTo("#p{n}in span", {{ opacity: 0, y: 110, scale: 0.6 }}, {{ opacity: 1, y: 0, scale: 1, '
                  f'duration: 0.3, ease: "back.out(1.8)", stagger: 0.03 }}, {p["a"]:.3f});')
        js.append(f'tl.to("#p{n}in", {{ opacity: 0, y: -24, duration: 0.22, ease: "power2.in" }}, {p["b"] - 0.24:.3f});')
    saida = f"{tmp}/hf_picos.webm"
    _render(f"{tmp}/hf_picos", PAGINA.format(W=W, H=H, total=total, fontes=_fontes_css(), css="", html="\n".join(html), js="\n".join(js)),
            saida, log)
    return saida


def camada_frente(total, flashes, tmp, grao=True, log=print):
    """Grão (tela inteira, o vídeo todo) e flashes de câmera. None se não houver nada."""
    if not grao and not flashes:
        return None
    css, html, js = [], [], []
    if grao:
        css.append(GRAO_CSS.replace("OPAC", str(GRAO)))
        html.append(f'<div class="clip" id="grain-overlay" data-start="0" data-duration="{total:.3f}" '
                    f'data-track-index="1"><div class="grain-texture"></div></div>')
    if flashes:
        css.append(FLASH_CSS)
    for n, t in enumerate(flashes):
        html.append(f'<div class="clip ef" id="ef{n}" data-start="{t:.3f}" data-duration="0.6" data-track-index="2">'
                    f'<div class="l wash" id="ef{n}w"></div><div class="l core" id="ef{n}c"></div></div>')
        h = t + 0.06
        js += [f'tl.to("#ef{n}w", {{ opacity: 0.85, duration: 0.04, ease: "power4.in" }}, {h:.3f});',
               f'tl.fromTo("#ef{n}c", {{ opacity: 0, scale: 0.86 }}, {{ opacity: 1, scale: 1, duration: 0.05, ease: "power4.in" }}, {h - 0.01:.3f});',
               f'tl.to("#ef{n}w", {{ opacity: 0, duration: 0.2, ease: "power3.out" }}, {h + 0.04:.3f});',
               f'tl.to("#ef{n}c", {{ opacity: 0, scale: 1.18, duration: 0.36, ease: "power2.out" }}, {h + 0.04:.3f});']
    saida = f"{tmp}/hf_frente.webm"
    _render(f"{tmp}/hf_frente", PAGINA.format(W=W, H=H, total=total, fontes=_fontes_css(), css="\n".join(css), html="\n".join(html),
                                              js="\n".join(js)), saida, log)
    return saida


# ---------- 4. composição: base + palavra atrás do corpo + zoom ----------
def _z(t, picos):
    z, cx, cy = 1.0, W / 2, H * 0.4
    for p in picos:
        a, b = p["t"] - 0.05, p["b"]
        if not a - 0.01 <= t <= b:
            continue
        sobe = min(1.0, (t - a) / 0.2)
        sobe = 1 - (1 - max(0.0, sobe)) ** 3          # ease-out
        desce = min(1.0, max(0.0, (b - t) / 0.35))
        desce = desce * desce * (3 - 2 * desce)       # smoothstep
        z, cx, cy = 1 + ZOOM * min(sobe, desce), p["cx"], p["cy"]
    return z, cx, cy


def compor(base, picos_webm, picos, total, saida, zoom=True, log=print):
    import cv2
    n = round(total * FPS)
    lb = subprocess.Popen(["ffmpeg", "-loglevel", "error", "-i", base, "-f", "rawvideo", "-pix_fmt", "rgb24", "-"],
                          stdout=subprocess.PIPE)
    lp = subprocess.Popen(["ffmpeg", "-loglevel", "error", "-c:v", "libvpx-vp9", "-i", picos_webm, "-f", "rawvideo",
                           "-pix_fmt", "rgba", "-"], stdout=subprocess.PIPE) if picos_webm else None
    enc = subprocess.Popen(["ffmpeg", "-y", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}",
                            "-r", str(FPS), "-i", "-", "-c:v", "libx264", "-crf", "12", "-preset", "veryfast",
                            "-pix_fmt", "yuv420p", "-g", "15", saida], stdin=subprocess.PIPE)
    alfas = {}
    tam = W * H * 3
    for i in range(n):
        buf = lb.stdout.read(tam)
        if len(buf) < tam:
            break
        txt = lp.stdout.read(W * H * 4) if lp else b""
        t = i / FPS
        ativo = [p for p in picos if p["f0"] <= i < p["f1"]]
        z, cx, cy = _z(t, picos) if zoom else (1.0, 0, 0)
        if not ativo and z == 1.0:
            enc.stdin.write(buf)
            continue
        q = np.frombuffer(buf, np.uint8).reshape(H, W, 3).astype(np.float32)
        if ativo and len(txt) == W * H * 4:
            p = ativo[0]
            if id(p) not in alfas:
                alfas.clear(); alfas[id(p)] = _alfas(p["fg"])
            al = alfas[id(p)]
            corpo = al[min(len(al) - 1, i - p["f0"])].astype(np.float32) / 255
            tx = np.frombuffer(txt, np.uint8).reshape(H, W, 4).astype(np.float32)
            a = (tx[..., 3] / 255) * (1 - corpo)       # a palavra só aparece fora do corpo
            q = q * (1 - a[..., None]) + tx[..., :3] * a[..., None]
        if z != 1.0:
            m = np.float32([[z, 0, cx - cx * z], [0, z, cy - cy * z]])
            q = cv2.warpAffine(q, m, (W, H), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REFLECT)
        enc.stdin.write(np.clip(q, 0, 255).astype(np.uint8).tobytes())
    enc.stdin.close(); enc.wait(); lb.wait()
    if lp:
        lp.stdout.close(); lp.wait()
    if enc.returncode:
        raise RuntimeError("falha ao gravar a base com acabamento")


# ---------- 5. SFX ----------
SFX_HF = os.path.normpath(os.path.join(AQUI, "..", "sfx_hf"))  # biblioteca do media-use (Pixabay, uso comercial)
# pacote: (som da troca de take, dB), (som do pico, dB); níveis medidos contra a voz em -15 dB de média
PACOTES_SFX = {
    "sutil": (("whoosh-short.mp3", -9.0), ("impact-bass-1.mp3", -21.0)),
    "cinema": (("whoosh-cinematic.mp3", -8.0), ("impact-bass-2.mp3", -20.0)),
    "pop": (("whoosh-short.mp3", -10.0), ("pop.mp3", -2.0)),
    "brilho": (("whoosh.mp3", -10.0), ("sparkle.mp3", -12.0)),
    "glitch": (("glitch-3.mp3", -14.0), ("glitch-1.mp3", -18.0)),
    "nenhum": (None, None),
}


def sfx(mix, total, trocas, picos, saida, pacote="sutil"):
    """Som na troca de take e em cada pico, por cima do mix (voz + música). Pacotes em PACOTES_SFX."""
    troca, pico = PACOTES_SFX[pacote]
    ev = ([(max(0, t - 0.2), troca) for t in trocas] if troca else []) + \
         ([(max(0, p["t"] - 0.03), pico) for p in picos] if pico else [])
    if not ev:
        shutil.copy(mix, saida); return
    ins, fil = ["-i", mix], []
    for j, (t, (f, db)) in enumerate(ev, 1):
        ins += ["-i", os.path.join(SFX_HF, f)]
        ms = int(t * 1000)
        fil.append(f"[{j}:a]aformat=sample_rates=44100:channel_layouts=mono,volume={db}dB,adelay={ms}|{ms}[s{j}]")
    fil.append("[0:a]" + "".join(f"[s{j}]" for j in range(1, len(ev) + 1)) +
               f"amix=inputs={len(ev) + 1}:normalize=0:duration=first,atrim=0:{total:.3f},alimiter=limit=0.95[o]")
    _sh(["ffmpeg", "-y", "-loglevel", "error", *ins, "-filter_complex", ";".join(fil), "-map", "[o]",
         "-ar", "44100", "-ac", "1", saida])


# ---------- rodízio entre vídeos ----------
# Luigi, 2026-10-10: variações existem para os vídeos não ficarem iguais entre si, não para testar todas em cada
# vídeo. Cardápio curto e testado; cada vídeo NOVO pega a próxima combinação, o mesmo vídeo reeditado mantém a sua.
CARDAPIO = {
    "legenda": ["padrao", "caption-highlight", "caption-pill-karaoke"],
    "sfx": ["sutil", "cinema", "pop", "brilho"],
    "fonte_pico": ["anton", "montserrat"],
}
ROTACAO = os.path.normpath(os.path.join(AQUI, "..", "rotacao.json"))


def variacao(nome):
    """{legenda, sfx, fonte_pico} do vídeo `nome`, girando o cardápio a cada vídeo novo (registro em rotacao.json)."""
    try:
        reg = json.load(open(ROTACAO))
    except (OSError, ValueError):
        reg = {"videos": {}}
    if nome not in reg["videos"]:
        n = len(reg["videos"])
        reg["videos"][nome] = {k: v[n % len(v)] for k, v in CARDAPIO.items()}
        json.dump(reg, open(ROTACAO, "w"), indent=1, ensure_ascii=False)
    return reg["videos"][nome]


# ---------- tudo junto ----------
def aplicar(tmp, ws, segs, total, estilo, flashes=(), forcados=None, zoom=True, grao=False, pacote="sutil",
            fonte="anton", log=print):
    """Devolve (base_nova, frente_webm ou None, mix_novo, linhas do relatório). `ws` = [{w, t, k}] no tempo do
    vídeo editado; `segs` = trechos do editar.py (para trocas de take e inserts)."""
    base = f"{tmp}/assets/base.mp4"
    mudos = {s["k"] for s in segs} - {s["k"] for s in segs if not s.get("mute")} if segs else set()
    trocas = [s["o"] for i, s in enumerate(segs) if i and segs[i - 1]["k"] != s["k"]] if segs else []
    picos = escolher_picos(ws, total, mudos, forcados)
    rel = []
    pw = None
    if picos:
        log(f"   {len(picos)} picos: " + ", ".join(f"{p['w']} ({p['t']:.1f}s)" for p in picos))
        recortar(base, picos, tmp, log)
        medir(picos, base, fonte)
        pw = camada_picos(picos, total, tmp, log)
    frente = camada_frente(total, list(flashes) if estilo == "auraly" else [], tmp, grao, log)
    nova = f"{tmp}/assets/base_hf.mp4"
    log("   compondo palavra atrás do avatar e zoom")
    compor(base, pw, picos, total, nova, zoom, log)
    mix = f"{tmp}/assets/mix_sfx.wav"
    sfx(f"{tmp}/assets/mix.wav", total, trocas, picos, mix, pacote)
    json.dump([{k: v for k, v in p.items() if k != "fg"} for p in picos], open(f"{tmp}/picos.json", "w"), indent=1)
    rel.append("- Acabamento HyperFrames: " + (", ".join(
        f"{p['w']} {p['t']:.1f}s ({int(p['occ'] * 100)}% atrás do corpo{', texto escuro' if p['escuro'] else ''})"
        for p in picos) or "nenhum pico") +
        f" · zoom {'sim' if zoom else 'não'} · grão {'sim' if grao else 'não'} · "
        f"SFX {pacote}")
    return nova, frente, mix, rel


def main():
    import argparse
    import legendas_hf
    ap = argparse.ArgumentParser()
    ap.add_argument("trabalho"); ap.add_argument("--picos", default=None, help="palavras de pico (padrão: automático)")
    ap.add_argument("--sem-zoom", action="store_true"); ap.add_argument("--grao", action="store_true")
    ap.add_argument("--sfx", default="sutil", choices=list(PACOTES_SFX))
    ap.add_argument("--legenda", default="padrao", help="padrao (serifada aprovada) ou um estilo do catálogo: "
                    + ", ".join(legendas_hf.estilos()))
    ap.add_argument("--fonte-pico", default="anton", choices=list(FONTES_PICO))
    ap.add_argument("--estilo", default="fitwell"); ap.add_argument("--saida", default=None)
    a = ap.parse_args()
    tmp = os.path.abspath(a.trabalho)
    sys.path.insert(0, AQUI)
    import motor
    total = float(_sh(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0",
                       f"{tmp}/assets/base.mp4"]))
    segs = json.load(open(f"{tmp}/segs.json")) if os.path.exists(f"{tmp}/segs.json") else []
    if os.path.exists(f"{tmp}/palavras_saida.json"):
        ws = json.load(open(f"{tmp}/palavras_saida.json"))
    else:  # pasta antiga: palavras ouvidas na voz editada, sem número de take
        ws = [dict(w=w, t=t, k=0) for w, t, _ in json.load(open(f"{tmp}/palavras_ouvidas.json"))]
    forcados = [_limpa(x) for x in a.picos.split(",")] if a.picos else None
    nova, frente, mix, rel = aplicar(tmp, ws, segs, total, a.estilo, (), forcados, not a.sem_zoom, a.grao, a.sfx, a.fonte_pico)
    camadas = [(frente, 0)] if frente else []
    lista = None
    if a.legenda != "padrao":
        picos = json.load(open(f"{tmp}/picos.json"))
        idx = [i for i, w in enumerate(ws) for p in picos if abs(w["t"] - p["t"]) < 0.01]
        camadas.append(legendas_hf.camada(a.legenda, ws, total, tmp, idx))
    elif os.path.exists(f"{tmp}/legendas.txt"):
        lista = f"{tmp}/legendas.txt"
    else:  # pasta antiga: legenda aprovada refeita a partir das palavras
        ev, pag = [], []
        for i, w in enumerate(ws):
            pag.append(w)
            if len(pag) >= 3 or re.search(r"[.!?,]$", w["w"]) or i + 1 == len(ws):
                ev.append(pag); pag = []
        eventos = []
        for n, p in enumerate(ev):
            png = f"{tmp}/legacab_{n:03d}.png"
            motor.png_fitwell(" ".join(re.sub(r"[.,!?]$", "", x["w"]) for x in p).lower(), 880, png)
            eventos.append((0 if n == 0 else p[0]["t"], ev[n + 1][0]["t"] if n + 1 < len(ev) else total, png))
        lista = motor.faixa_legendas(eventos, total, tmp)
    nome = os.path.basename(tmp).split("-")[0]
    saida = a.saida or f"{tmp}/{nome}_acabamento_{a.legenda}_{a.sfx}.mp4"
    motor.render_final(nova, lista, mix, total, saida, (), None, camadas)
    print("\n".join(rel + [f"- Legenda: {a.legenda}"])); print(saida)


if __name__ == "__main__":
    main()
