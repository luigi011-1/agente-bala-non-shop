"""Motor v4 da edição (Luigi, 2026-10-10: palavras comidas nos cortes, silêncio sobrando, final baixo cortado,
qualidade abaixo de 1080p e demora). Usado pelo editar.py.

1. Corte pelas bordas REAIS das palavras: alinhamento forçado do texto do roteiro no áudio (WhisperX, wav2vec2),
   bordas refinadas pelo volume em janelas de 10 ms (a cauda fraca da palavra fica, o silêncio sai).
2. Sem interpolação de quadros (deformava as mãos): fps simples + ampliação lanczos + nitidez leve.
3. Legenda desenhada como imagem (Pillow) e gravada pelo ffmpeg num passe só, sem render pelo navegador.
4. Saída em 1080x1920, CRF 17 (sem o teto de 25 MB, que era da cópia na nuvem).
"""
import os
import re
import subprocess

AQUI = os.path.dirname(os.path.abspath(__file__))
W, H, FPS = 1080, 1920, 30
FONTE = os.path.join(AQUI, "fonts", "Merriweather900.ttf")


def _sh(cmd):
    return subprocess.run(cmd, check=True, capture_output=True, text=True).stdout


def _dur(f):
    return float(_sh(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", f]))


# ---------- volume em janelas de 10 ms ----------
_rms10 = {}
def rms10(f):
    if f not in _rms10:
        e = subprocess.run(["ffmpeg", "-hide_banner", "-i", f, "-vn", "-af",
                            "aresample=16000,asetnsamples=160,astats=metadata=1:reset=1,"
                            "ametadata=print:key=lavfi.astats.Overall.RMS_level", "-f", "null", "-"],
                           capture_output=True, text=True).stderr
        _rms10[f] = [float(x) if x != "-inf" else -120.0 for x in re.findall(r"RMS_level=(-?[\d.]+|-inf)", e)]
    return _rms10[f]


# ---------- alinhamento forçado ----------
_al = None
def alinhar_forcado(f, fala, ws_asr):
    """Tempo de cada palavra do ROTEIRO no take, por alinhamento forçado. Devolve [[palavra, início, fim]] ou None.
    A janela é a da fala que o whisper ouviu (com folga), para o alinhador não espalhar palavra no silêncio."""
    global _al
    try:
        import whisperx
        if _al is None:
            _al = whisperx.load_align_model(language_code="en", device="cpu")
        modelo, meta = _al
        audio = whisperx.load_audio(f)
        d = len(audio) / 16000
        a0 = max(0.0, ws_asr[0][1] - 0.4) if ws_asr else 0.0
        b0 = min(d, ws_asr[-1][2] + 0.6) if ws_asr else d
        res = whisperx.align([{"start": a0, "end": b0, "text": fala}], modelo, meta, audio, "cpu",
                             return_char_alignments=False)
        out = [[w["word"], w.get("start"), w.get("end")] for s in res["segments"] for w in s.get("words", [])]
    except Exception:
        return None
    if not out or all(w[1] is None for w in out):
        return None
    for i, w in enumerate(out):  # palavra sem tempo (número, símbolo): entre as vizinhas
        if w[1] is None:
            ant = out[i - 1][2] if i else a0
            prox = next((x[1] for x in out[i + 1:] if x[1] is not None), b0)
            w[1], w[2] = ant, ant + max(0.08, (prox - ant) * 0.8)
    return out


def ilhas_v4(f, aw, gap=0.12, pre=0.03, pos=0.05, cauda=0.30, ataque=0.12):
    """Trechos a manter: cada palavra do alinhamento com a borda refinada pelo volume (estende o fim enquanto ainda
    há voz, até `cauda` s, sem invadir a próxima palavra; idem o início, até `ataque` s). Palavras com intervalo
    até `gap` s ficam juntas; o resto do intervalo sai. Folga final `pre`/`pos` s."""
    d = _dur(f)
    r = rms10(f)
    n = len(r)
    if not n:
        return [[0.0, d]]
    s = sorted(r)
    fundo, fala = s[n // 10], s[n * 7 // 10]
    limiar = min(fala - 10, max(fundo + 8, -55))  # acima do fundo do take, abaixo da fala
    nivel = lambda t: r[int(t / 0.01)] if 0 <= int(t / 0.01) < n else -120.0
    spans = []
    for i, (_, a, b) in enumerate(aw):
        ant = aw[i - 1][2] if i else 0.0
        prox = aw[i + 1][1] if i + 1 < len(aw) else d
        e = b
        while e < min(b + cauda, prox) and nivel(e) >= limiar:
            e += 0.01
        s0 = a
        while s0 > max(a - ataque, ant) and nivel(s0 - 0.01) >= limiar:
            s0 -= 0.01
        spans.append([s0, e])
    ilhas = []
    for a, b in spans:
        if ilhas and a - ilhas[-1][1] <= gap:
            ilhas[-1][1] = max(ilhas[-1][1], b)
        else:
            ilhas.append([a, b])
    out = []
    for a, b in ilhas:
        x = [max(0.0, a - pre), min(d, b + pos)]
        if out and x[0] <= out[-1][1]:
            out[-1][1] = x[1]
        else:
            out.append(x)
    return out


def filtro_trecho(a, b, sp, d_saida):
    """Vídeo do trecho: corte, velocidade, 30 fps sem interpolação, 1080x1920 com nitidez leve."""
    return (f"[0:v]trim=start={a:.3f}:end={b:.3f},setpts=(PTS-STARTPTS)/{sp},fps={FPS},"
            f"scale={W}:{H}:flags=lanczos,unsharp=5:5:0.55:5:5:0,setsar=1,"
            f"tpad=stop_mode=clone:stop_duration=0.2,trim=end_frame={max(1, round(d_saida * FPS))},"
            f"setpts=N/({FPS}*TB)[v]")


# ---------- legendas como imagem ----------
def _fonte(tam):
    from PIL import ImageFont
    return ImageFont.truetype(FONTE, tam)


def _desenhar(itens):
    """itens: [(texto, x, y, tamanho)] em coordenadas do quadro. Branco com sombra suave (igual o CSS v3)."""
    from PIL import Image, ImageDraw, ImageFilter
    img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    sombra = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    ds = ImageDraw.Draw(sombra)
    for t, x, y, tam in itens:
        ds.text((x, y + 3), t, font=_fonte(tam), fill=(0, 0, 0, 150))
    sombra = sombra.filter(ImageFilter.GaussianBlur(6))
    img.alpha_composite(sombra)
    dr = ImageDraw.Draw(img)
    for t, x, y, tam in itens:
        dr.text((x, y), t, font=_fonte(tam), fill=(255, 255, 255, 255), stroke_width=1, stroke_fill=(0, 0, 0, 130))
    return img


def png_fitwell(texto, topo, caminho, tam=64, largura=940):
    """Estilo FitWell v3: serifada branca, minúscula, centralizada, quebra em até 2 linhas."""
    f = _fonte(tam)
    palavras, linhas, cur = texto.split(), [], ""
    for p in palavras:
        teste = (cur + " " + p).strip()
        if f.getlength(teste) <= largura or not cur:
            cur = teste
        else:
            linhas.append(cur); cur = p
    if cur:
        linhas.append(cur)
    alt = int(tam * 1.15)
    itens = [(l, (W - f.getlength(l)) / 2, topo + i * alt, tam) for i, l in enumerate(linhas)]
    _desenhar(itens).save(caminho)


def layout_auraly(palavras, big, topo=960, larg=600, tam=66, tam_big=160, gap=20):
    """Posição de cada palavra da página (estilo da referência Auraly): linhas curtas centralizadas até `larg` px,
    a palavra-chave numa linha só dela e bem maior."""
    linhas, cur = [], []
    for j, w in enumerate(palavras):
        t = tam_big if j == big else tam
        if j == big:
            if cur: linhas.append(cur)
            linhas.append([(j, w, t)]); cur = []
            continue
        larg_cur = sum(_fonte(x[2]).getlength(x[1]) for x in cur) + gap * len(cur)
        if cur and larg_cur + _fonte(t).getlength(w) > larg:
            linhas.append(cur); cur = []
        cur.append((j, w, t))
    if cur:
        linhas.append(cur)
    pos, y = {}, topo
    for ln in linhas:
        alt = max(x[2] for x in ln)
        total = sum(_fonte(x[2]).getlength(x[1]) for x in ln) + gap * (len(ln) - 1)
        x0 = (W - total) / 2
        for j, w, t in ln:
            pos[j] = (w, x0, y + (alt - t) * 0.8, t)
            x0 += _fonte(t).getlength(w) + gap
        y += int(alt * 1.02)
    return pos


def png_auraly(pos, visiveis, caminho):
    _desenhar([pos[j] for j in sorted(pos) if j < visiveis]).save(caminho)


def png_selos(caminho):
    """Selos 777 (direita, altura do rosto) e 222 (esquerda, altura do peito) de todo vídeo Auraly."""
    from PIL import Image, ImageDraw, ImageFont
    img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    emoji = "/System/Library/Fonts/Apple Color Emoji.ttc"
    sans = next((p for p in ("/System/Library/Fonts/Supplemental/Arial Bold.ttf",
                             "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf") if os.path.exists(p)), None)
    def selo(e1, txt, e2):
        alto = 160
        fe = ImageFont.truetype(emoji, 160) if os.path.exists(emoji) else None
        ft = ImageFont.truetype(sans, 150) if sans else ImageFont.load_default()
        partes = [(e1, fe), (txt, ft), (e2, fe)]
        larg = int(sum((f.getlength(t) if f else 0) for t, f in partes)) + 40
        tela = Image.new("RGBA", (larg, alto + 40), (0, 0, 0, 0))
        d = ImageDraw.Draw(tela)
        x = 0
        for t, f in partes:
            if f is None:
                continue
            if f is ft:
                d.text((x, 10), t, font=f, fill=(255, 255, 255, 255), stroke_width=4, stroke_fill=(0, 0, 0, 120))
            else:
                d.text((x, 0), t, font=f, embedded_color=True)
            x += int(f.getlength(t)) + 10
        return tela.resize((int(tela.width * 48 / 160), int(tela.height * 48 / 160)))
    s1, s2 = selo("🇺🇸", "777", "🇺🇸"), selo("🔮", "222", "🔮")
    img.alpha_composite(s1, (W - s1.width - 56, 420))
    img.alpha_composite(s2, (56, 1310))
    img.save(caminho)


def faixa_legendas(eventos, total, tmp):
    """eventos: [(início, fim, png)] sem sobreposição. Escreve a lista do concat (com PNG vazio nos buracos)."""
    from PIL import Image
    vazio = os.path.join(tmp, "leg_vazio.png")
    Image.new("RGBA", (W, H), (0, 0, 0, 0)).save(vazio)
    linhas, t = ["ffconcat version 1.0"], 0.0
    for a, b, png in sorted(eventos):
        if a > t + 1e-3:
            linhas += [f"file '{vazio}'", f"duration {a - t:.4f}"]
        if b > a:
            linhas += [f"file '{png}'", f"duration {b - a:.4f}"]
        t = max(t, b)
    if total > t:
        linhas += [f"file '{vazio}'", f"duration {total - t:.4f}"]
    linhas += [f"file '{vazio}'"]
    lista = os.path.join(tmp, "legendas.txt")
    open(lista, "w").write("\n".join(linhas) + "\n")
    return lista


def _n_in(ins):
    return sum(1 for x in ins if x == "-i")


def render_final(base, lista_leg, mix, total, saida, flashes=(), selos=None, camadas=()):
    """Um passe: base 1080p + camadas transparentes da HyperFrames (webm, deslocamento vertical) + faixa de
    legendas + selos + flash + mix -> H.264 CRF 17, 30 fps. `lista_leg` None = sem legenda Pillow."""
    ins, fil, ult = ["-i", base, "-i", mix], [], "0:v"
    for i, (webm, dy) in enumerate(camadas):
        ins += ["-c:v", "libvpx-vp9", "-i", webm]
        fil.append(f"[{ult}][{2 + i}:v]overlay=0:{int(dy)}:format=auto:eof_action=pass[vc{i}]")
        ult = f"vc{i}"
    if lista_leg:
        ins += ["-f", "concat", "-safe", "0", "-i", lista_leg]
        fil += [f"[{2 + len(camadas)}:v]fps={FPS},format=rgba[lg]", f"[{ult}][lg]overlay=0:0:format=auto[v0]"]
        ult = "v0"
    if selos:
        ins += ["-loop", "1", "-i", selos]
        fil += [f"[{ult}][{_n_in(ins) - 1}:v]overlay=0:0:format=auto:shortest=1[vs]"]
        ult = "vs"
    for i, t in enumerate(flashes):
        fil += [f"color=c=0xFFF4CC:s={W}x{H}:d=0.5,format=rgba,colorchannelmixer=aa=0.85,"
                f"fade=t=in:st=0:d=0.14:alpha=1,fade=t=out:st=0.16:d=0.34:alpha=1,setpts=PTS+{t:.3f}/TB[fl{i}]",
                f"[{ult}][fl{i}]overlay=0:0:enable='between(t,{t:.3f},{t + 0.5:.3f})'[vf{i}]"]
        ult = f"vf{i}"
    if not fil:
        fil = ["[0:v]null[vn]"]; ult = "vn"
    _sh(["ffmpeg", "-y", "-loglevel", "error", *ins, "-filter_complex", ";".join(fil), "-map", f"[{ult}]", "-map", "1:a",
         "-t", f"{total:.3f}", "-c:v", "libx264", "-crf", "17", "-preset", "medium", "-profile:v", "high",
         "-pix_fmt", "yuv420p", "-r", str(FPS), "-c:a", "aac", "-b:a", "192k", "-movflags", "+faststart", saida])
