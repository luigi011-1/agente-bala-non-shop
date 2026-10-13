"""Estilos de legenda do catálogo HyperFrames (Luigi, 2026-10-10: priorizar o que o repositório HyperFrames
oferece, em tudo). Os componentes `caption-*` ficam como vieram do `hyperframes add` em `../legendas_hf/`; este
módulo só troca a fala de exemplo pela nossa, vira o quadro para 9:16 e renderiza uma camada transparente.

    estilos()                          -> nomes disponíveis
    camada(estilo, ws, total, tmp)     -> (webm transparente, deslocamento vertical em px)

`ws` = [{w, t, k}] no tempo do vídeo editado. A posição vertical é medida no render e a camada é deslocada até
a altura do peito (LEG_CENTRO), porque cada componente posiciona a legenda de um jeito.
"""
import json
import os
import re
import shutil
import subprocess

AQUI = os.path.dirname(os.path.abspath(__file__))
PASTA = os.path.normpath(os.path.join(AQUI, "..", "legendas_hf"))
HF = ["npx", "-y", "hyperframes@0.8.144"]
W, H, FPS = 1080, 1920, 30
LEG_CENTRO = 960  # centro da legenda: peito, abaixo do rosto e acima do herói da mesa
# os que leem a fala de WORDS/TRANSCRIPT com grupos; editorial-emphasis e parallax-layers montam BLOCKS à mão e
# blend-difference é texto fixo: ficam de fora até ganharem adaptador próprio
SUPORTADOS = ["caption-highlight", "caption-pill-karaoke", "caption-emoji-pop", "caption-kinetic-slam",
              "caption-clip-wipe", "caption-gradient-fill", "caption-neon-glow", "caption-neon-accent",
              "caption-glitch-rgb", "caption-matrix-decode", "caption-particle-burst", "caption-weight-shift",
              "caption-texture", "caption-camera-follow"]


def estilos():
    return [s for s in SUPORTADOS if os.path.exists(f"{PASTA}/{s}.html")]


def _array(src, nome):
    """(início, fim) do literal `var NOME = [ ... ];` com colchetes casados."""
    m = re.search(rf"var {nome} = \[", src)
    if not m:
        return None
    i, nivel = m.end() - 1, 0
    for j in range(i, len(src)):
        c = src[j]
        if c == "[":
            nivel += 1
        elif c == "]":
            nivel -= 1
            if nivel == 0:
                return i, j + 1
    return None


def _troca(src, nome, valor):
    r = _array(src, nome)
    return src if not r else src[:r[0]] + json.dumps(valor) + src[r[1]:]


def grupos(ws, maximo=3):
    """Páginas de até `maximo` palavras, quebrando no ponto, na vírgula e na troca de take (como o editar.py)."""
    out, cur = [], []
    for i, w in enumerate(ws):
        cur.append(i)
        nx = ws[i + 1] if i + 1 < len(ws) else None
        if (not nx or len(cur) >= maximo or re.search(r"[.!?]$", w["w"]) or (re.search(r",$", w["w"]) and len(cur) >= 2)
                or nx["k"] != w["k"]):
            out.append([cur[0], cur[-1]]); cur = []
    # cada legenda >= 0,5s na tela (embedded-captions): grupo curto junta com o seguinte do mesmo take
    junto = []
    for g in out:
        if junto and ws[g[0]]["t"] - ws[junto[-1][0]]["t"] < 0.5 and ws[g[0]]["k"] == ws[junto[-1][0]]["k"]:
            junto[-1][1] = g[1]
        else:
            junto.append(list(g))
    return junto


def adaptar(src, ws, total, picos=()):
    palavras = []
    for i, w in enumerate(ws):
        fim = ws[i + 1]["t"] - 0.02 if i + 1 < len(ws) else min(total, w["t"] + 0.6)
        palavras.append({"text": w["w"], "start": round(w["t"], 3), "end": round(max(w["t"] + 0.08, fim), 3)})
    gr = grupos(ws)
    obj = []
    for n, (a, b) in enumerate(gr):
        fim = palavras[gr[n + 1][0]]["start"] - 0.03 if n + 1 < len(gr) else total
        obj.append({"wordStart": a, "wordEnd": b, "start": palavras[a]["start"], "end": round(fim, 3)})
    for nome in ("WORDS", "TRANSCRIPT"):
        src = _troca(src, nome, palavras)
    if _array(src, "RAW_GROUPS"):
        src = _troca(src, "RAW_GROUPS", gr)
    r = _array(src, "GROUPS")
    if r and src[r[0]:r[1]].lstrip("[ \n").startswith("{"):
        src = _troca(src, "GROUPS", obj)
    # palavra-chave dos componentes que destacam (kinetic-slam): os picos do acabamento
    src = re.sub(r"var KEYWORDS = new Set\(\[[^\]]*\]\)", f"var KEYWORDS = new Set({json.dumps(list(picos))})", src)
    src = re.sub(r"var DURATION = [\d.]+;", f"var DURATION = {total:.3f};", src)
    src = re.sub(r"(\?\s*[A-Z_]+\[[^\]]+\]\[0\]\]\.start\s*:\s*)8\.0", rf"\g<1>{total:.3f}", src)
    src = re.sub(r'(data-composition-id="[^"]+"[^>]*?data-duration=")[\d.]+(")', rf"\g<1>{total:.3f}\g<2>", src, flags=re.S)
    src = re.sub(r'(data-duration=")[\d.]+("[^>]*?data-composition-id=)', rf"\g<1>{total:.3f}\g<2>", src, flags=re.S)
    # 16:9 -> 9:16: troca largura e altura do quadro; a largura útil dos textos encolhe na mesma proporção
    src = src.replace("1920px", "@@W").replace("1080px", "@@H").replace("@@W", f"{W}px").replace("@@H", f"{H}px")
    src = src.replace('data-width="1920"', f'data-width="{W}"').replace('data-height="1080"', f'data-height="{H}"')
    src = src.replace('content="width=1920, height=1080"', f'content="width={W}, height={H}"')
    # caixas de texto feitas para 16:9 (1400 a 1600px) saíam do quadro de 1080px: a pill-karaoke cortava a frase
    # nas bordas ("hen whisk completely smoot", Marshall, 2026-10-10). Toda largura fixa > 940px vira 940px.
    src = re.sub(r"((?:max-)?width:\s*)(1[1-9]\d\d)px", lambda m: f"{m.group(1)}940px", src)
    src = re.sub(r"(var [A-Z_]*MAX_WIDTH\s*=\s*)(\d{4})", lambda m: f"{m.group(1)}{min(int(m.group(2)), 900)}", src)
    src = re.sub(r"(fitFontSize\([^;]*?,\s*)(\d{3,4})(\s*\))",
                 lambda m: f"{m.group(1)}{int(int(m.group(2)) * 940 / 1920)}{m.group(3)}", src)
    return src


def _faixa_texto(webm, total):
    """Centro vertical médio do texto renderizado (amostras a cada ~1s), em px."""
    import numpy as np
    centros = []
    for t in [x + 0.5 for x in range(int(total))]:
        raw = subprocess.run(["ffmpeg", "-loglevel", "error", "-c:v", "libvpx-vp9", "-ss", f"{t:.2f}", "-i", webm,
                              "-frames:v", "1", "-vf", "alphaextract", "-pix_fmt", "gray", "-f", "rawvideo", "-"],
                             capture_output=True).stdout
        if len(raw) != W * H:
            continue
        a = np.frombuffer(raw, np.uint8).reshape(H, W)
        ys = np.where((a > 60).sum(axis=1) > 4)[0]
        if len(ys):
            centros.append((ys[0] + ys[-1]) / 2)
    return float(np.median(centros)) if centros else LEG_CENTRO


def camada(estilo, ws, total, tmp, picos=(), log=print, centro=LEG_CENTRO):
    if estilo not in estilos():
        raise SystemExit(f"Estilo de legenda '{estilo}' não existe. Disponíveis: {', '.join(estilos())}")
    pasta = f"{tmp}/hf_legenda_{estilo}"
    shutil.rmtree(pasta, ignore_errors=True)
    os.makedirs(pasta)
    for f in os.listdir(PASTA):  # texturas do caption-texture
        if f.endswith(".png"):
            shutil.copy(f"{PASTA}/{f}", pasta)
    src = adaptar(open(f"{PASTA}/{estilo}.html", encoding="utf8").read(), ws, total, picos)
    open(f"{pasta}/index.html", "w", encoding="utf8").write(src)
    saida = f"{tmp}/hf_legenda_{estilo}.webm"
    r = subprocess.run(HF + ["render", ".", "--format", "webm", "--workers", "1", "--low-memory-mode", "-o", saida], cwd=pasta, capture_output=True, text=True)
    if r.returncode or not os.path.exists(saida):
        raise RuntimeError(f"render da legenda {estilo} falhou:\n{(r.stdout + r.stderr)[-2000:]}")
    dy = int(round(centro - _faixa_texto(saida, total)))
    log(f"   legenda {estilo}: render ok, deslocada {dy:+d}px até o peito")
    return saida, dy
