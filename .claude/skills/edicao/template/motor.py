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
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
W, H, FPS = 1080, 1920, 30
IDIOMA = "en"
FONTE = os.path.join(AQUI, "fonts", "Merriweather900.ttf")


def _sh(cmd):
    return subprocess.run(cmd, check=True, capture_output=True, text=True).stdout


def _dur(f):
    return float(_sh(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", f]))


# ---------- volume em janelas de 10 ms ----------
_rms10 = {}
def rms10(f):
    if f not in _rms10:
        e = subprocess.run(["ffmpeg", "-hide_banner", "-threads", "2", "-i", f, "-vn", "-af",
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
    import json
    cache_p = f"{f}.alinhado.json"
    try:
        st = os.stat(f)
        chave = f"{int(st.st_mtime)}:{st.st_size}:{fala}"
        if os.path.exists(cache_p):
            dc = json.load(open(cache_p))
            if dc.get("k") == chave and dc.get("out"):
                return dc["out"]
    except Exception:
        chave = None
    if ws_asr and any(x[1] is not None for x in ws_asr):
        import difflib
        def _lim(s):
            return re.sub(r"[^a-z0-9']", "", s.lower())
        rot = fala.split()
        if rot:
            h_norm = [_lim(x[0]) for x in ws_asr]
            r_norm = [_lim(w) for w in rot]
            ops = difflib.SequenceMatcher(None, h_norm, r_norm, autojunk=False).get_opcodes()
            out = [[w, None, None] for w in rot]
            for op, i1, i2, j1, j2 in ops:
                if op == "equal":
                    for d_i in range(j2 - j1):
                        out[j1 + d_i][1] = round(float(ws_asr[i1 + d_i][1]), 3)
                        out[j1 + d_i][2] = round(float(ws_asr[i1 + d_i][2]), 3)
                elif op in ("replace", "insert") and (j2 > j1):
                    a_span = float(ws_asr[i1][1]) if i1 < len(ws_asr) else (float(ws_asr[-1][2]) if ws_asr else 0.0)
                    b_span = (float(ws_asr[i2 - 1][2])
                              if (op == "replace" and i2 > i1 and i2 - 1 < len(ws_asr))
                              else min(a_span + 0.18 * (j2 - j1), float(ws_asr[i1][2]) if i1 < len(ws_asr) else a_span + 0.25))
                    if b_span <= a_span:
                        b_span = a_span + 0.12 * (j2 - j1)
                    passo = (b_span - a_span) / max(1, j2 - j1)
                    for d_i in range(j2 - j1):
                        out[j1 + d_i][1] = round(a_span + d_i * passo, 3)
                        out[j1 + d_i][2] = round(a_span + (d_i + 1) * passo, 3)
            if any(w[1] is not None for w in out):
                a0 = max(0.0, float(ws_asr[0][1]))
                b0 = float(ws_asr[-1][2])
                for i, w in enumerate(out):
                    if w[1] is None:
                        ant = out[i - 1][2] if i and out[i - 1][2] is not None else a0
                        prox = next((x[1] for x in out[i + 1:] if x[1] is not None), b0)
                        w[1], w[2] = round(ant, 3), round(ant + max(0.08, (prox - ant) * 0.8), 3)
                # Refina início/fim de cada palavra pelo volume real (rms10), removendo silêncio ou respiro isolado que o Whisper cola no span
                r10 = rms10(f)
                if len(r10) >= 20:
                    sr = sorted(r10)
                    lim_w = max(-38.0, min(sr[len(sr) * 7 // 10] - 12, sr[len(sr) // 10] + 8))
                    niv_w = lambda t: r10[int(t / 0.01)] if 0 <= int(t / 0.01) < len(r10) else -120.0
                    for w in out:
                        wa, wb = float(w[1]), float(w[2])
                        if wb - wa > 0.35:
                            # Se houver silêncio >= 0.18s dentro de uma única palavra (ex.: respiro + pausa + palavra), fica com a ilha de voz principal
                            i0, i1 = max(0, int(wa / 0.01)), min(len(r10), int(wb / 0.01))
                            sub, st_i, sil_cnt = [], None, 0
                            for idx_r in range(i0, i1):
                                if r10[idx_r] >= lim_w:
                                    if st_i is None:
                                        st_i = idx_r
                                    sil_cnt = 0
                                elif st_i is not None:
                                    sil_cnt += 1
                                    if sil_cnt >= 18:
                                        sub.append((st_i, idx_r - sil_cnt + 1))
                                        st_i, sil_cnt = None, 0
                            if st_i is not None:
                                sub.append((st_i, i1 - sil_cnt))
                            if sub:
                                melhor = max(sub, key=lambda ab: sum(max(0.0, r10[k] - lim_w) for k in range(ab[0], max(ab[0] + 1, ab[1]))))
                                wa, wb = max(wa, melhor[0] * 0.01), min(wb, melhor[1] * 0.01)
                        while wa < wb - 0.12 and niv_w(wa) < lim_w:
                            wa += 0.01
                        while wb > wa + 0.12 and niv_w(wb - 0.01) < lim_w:
                            wb -= 0.01
                        w[1], w[2] = round(wa, 3), round(wb, 3)
                if chave:
                    try:
                        json.dump({"k": chave, "out": out}, open(cache_p, "w"))
                    except Exception:
                        pass
                return out
    try:
        import torch, whisperx
        torch.set_num_threads(2)
        if _al is None:
            _al = whisperx.load_align_model(language_code=IDIOMA, device="cpu")
        modelo, meta = _al
        audio = whisperx.load_audio(f)
        d = len(audio) / 16000
        a0 = max(0.0, ws_asr[0][1] - 0.4) if ws_asr else 0.0
        b0 = min(d, ws_asr[-1][2] + 0.6) if ws_asr else d
        with torch.inference_mode():
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
    if chave:
        try:
            json.dump({"k": chave, "out": out}, open(cache_p, "w"))
        except Exception:
            pass
    return out


def ilhas_v4(f, aw, gap=0.50, pre=0.10, pos=0.15, cauda=0.35, ataque=0.20):
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
    lim_voz = max(-38.0, limiar)
    nivel = lambda t: r[int(t / 0.01)] if 0 <= int(t / 0.01) < n else -120.0
    spans = []
    for i, (_, a, b) in enumerate(aw):
        ant = aw[i - 1][2] if i else 0.0
        prox = aw[i + 1][1] if i + 1 < len(aw) else d
        s0, e = a, b
        if e - s0 > 0.35:
            i0, i1 = max(0, int(s0 / 0.01)), min(n, int(e / 0.01))
            sub, st_i, sil_cnt = [], None, 0
            for idx_r in range(i0, i1):
                if r[idx_r] >= lim_voz:
                    if st_i is None:
                        st_i = idx_r
                    sil_cnt = 0
                elif st_i is not None:
                    sil_cnt += 1
                    if sil_cnt >= 18:
                        sub.append((st_i, idx_r - sil_cnt + 1))
                        st_i, sil_cnt = None, 0
            if st_i is not None:
                sub.append((st_i, i1 - sil_cnt))
            if sub:
                melhor = max(sub, key=lambda ab: sum(max(0.0, r[k] - lim_voz) for k in range(ab[0], max(ab[0] + 1, ab[1]))))
                s0, e = max(s0, melhor[0] * 0.01), min(e, melhor[1] * 0.01)
        while s0 < e - 0.12 and nivel(s0) < lim_voz:
            s0 += 0.01
        while e > s0 + 0.12 and nivel(e - 0.01) < lim_voz:
            e -= 0.01
        while e < min(b + cauda, prox) and nivel(e) >= limiar:
            e += 0.01
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
    """Vídeo do trecho: corte, velocidade, 30 fps sem interpolação, 1080x1920 rápido."""
    return (f"[0:v]trim=start={a:.3f}:end={b:.3f},setpts=(PTS-STARTPTS)/{sp},fps={FPS},"
            f"scale={W}:{H}:flags=bicubic,setsar=1,"
            f"tpad=stop_mode=clone:stop_duration=0.2,trim=end_frame={max(1, round(d_saida * FPS))},"
            f"setpts=N/({FPS}*TB)[v]")


# ---------- legendas como imagem ----------
def _fonte(tam):
    from PIL import ImageFont
    return ImageFont.truetype(FONTE, tam)


def _desenhar(itens, banda=None):
    """itens: [(texto, x, y, tamanho)] em coordenadas do quadro. Branco com sombra suave (igual o CSS v3)."""
    from PIL import Image, ImageDraw, ImageFilter
    y0, h_img = banda if banda else (0, H)
    img = Image.new("RGBA", (W, h_img), (0, 0, 0, 0))
    sombra = Image.new("RGBA", (W, h_img), (0, 0, 0, 0))
    ds = ImageDraw.Draw(sombra)
    for t, x, y, tam in itens:
        ds.text((x, y + 3 - y0), t, font=_fonte(tam), fill=(0, 0, 0, 150))
    sombra = sombra.filter(ImageFilter.GaussianBlur(6))
    img.alpha_composite(sombra)
    dr = ImageDraw.Draw(img)
    for t, x, y, tam in itens:
        dr.text((x, y - y0), t, font=_fonte(tam), fill=(255, 255, 255, 255), stroke_width=1, stroke_fill=(0, 0, 0, 130))
    return img


def png_fitwell(texto, topo, caminho, tam=64, largura=940, banda=None):
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
    _desenhar(itens, banda=banda).save(caminho)


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
            elif t == "🇺🇸":
                # Pillow/Apple Color Emoji pode medir a bandeira e não desenhá-la.
                # Desenho raster do mesmo símbolo, na mesma caixa, mantém posição e tamanho do selo.
                fw = max(1, int(f.getlength(t)))
                fh = max(13, round(fw / 1.9))
                flag = Image.new("RGBA", (fw, fh), "white")
                fd = ImageDraw.Draw(flag)
                for row in range(13):
                    if row % 2 == 0:
                        fd.rectangle((0, round(row * fh / 13), fw, round((row + 1) * fh / 13) - 1), fill="#b22234")
                cw, ch = round(fw * .4), round(fh * 7 / 13)
                fd.rectangle((0, 0, cw, ch), fill="#3c3b6e")
                for row in range(9):
                    cols = 6 if row % 2 == 0 else 5
                    for col in range(cols):
                        sx = (col + (.5 if cols == 6 else 1)) * cw / 6
                        sy = (row + .5) * ch / 9
                        rr = max(1, fh / 50)
                        fd.ellipse((sx-rr, sy-rr, sx+rr, sy+rr), fill="white")
                tela.alpha_composite(flag, (x, 20))
            else:
                d.text((x, 0), t, font=f, embedded_color=True)
            x += int(f.getlength(t)) + 10
        return tela.resize((int(tela.width * 48 / 160), int(tela.height * 48 / 160)))
    s1, s2 = selo("🇺🇸", "777", "🇺🇸"), selo("🔮", "222", "🔮")
    img.alpha_composite(s1, (W - s1.width - 56, 420))
    img.alpha_composite(s2, (56, 1310))
    img.save(caminho)


def faixa_legendas(eventos, total, tmp, banda=None):
    """eventos: [(início, fim, png)] sem sobreposição. Escreve a lista do concat (com PNG vazio nos buracos)."""
    from PIL import Image
    vazio = os.path.join(tmp, "leg_vazio.png")
    h_img = banda[1] if banda else H
    Image.new("RGBA", (W, h_img), (0, 0, 0, 0)).save(vazio, compress_level=1)
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


def render_final(base, lista_leg, mix, total, saida, flashes=(), selos=None, camadas=(), leg_y=0):
    """Um passe: base 1080p + clipes curtos de zoom de pico + camadas transparentes da HyperFrames + faixa de
    legendas + selos + flash + mix -> H.264, 30 fps. `lista_leg` None = sem legenda Pillow."""
    import json
    usa_vt = sys.platform == "darwin"
    hw_in = ["-hwaccel", "videotoolbox"] if usa_vt else []
    ins, fil, ult = [*hw_in, "-threads", "2", "-i", base, "-threads", "1", "-i", mix], [], "0:v"
    if os.path.basename(base) == "base.mp4":
        zc_file = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(base))), "zoom_clips.json")
        if os.path.exists(zc_file):
            try:
                for idx_z, (zmp4, a0, b0) in enumerate(json.load(open(zc_file))):
                    if os.path.exists(zmp4):
                        ins += ["-threads", "1", "-i", zmp4]
                        in_k = _n_in(ins) - 1
                        fil.append(f"[{in_k}:v]setpts=PTS+{float(a0):.4f}/TB[zv{idx_z}];"
                                   f"[{ult}][zv{idx_z}]overlay=0:0:enable='between(t,{float(a0):.4f},{float(b0):.4f})':eof_action=pass[vz{idx_z}]")
                        ult = f"vz{idx_z}"
            except Exception:
                pass
    for i, (webm, dy) in enumerate(camadas):
        ins += ["-threads", "2", "-c:v", "libvpx-vp9", "-i", webm]
        in_k = _n_in(ins) - 1
        fil.append(f"[{ult}][{in_k}:v]overlay=0:{int(dy)}:format=auto:eof_action=pass[vc{i}]")
        ult = f"vc{i}"
    if lista_leg:
        ins += ["-threads", "2", "-f", "concat", "-safe", "0", "-i", lista_leg]
        in_k = _n_in(ins) - 1
        fil += [f"[{in_k}:v]fps={FPS},format=rgba[lg]", f"[{ult}][lg]overlay=0:{int(leg_y)}:format=auto[v0]"]
        ult = "v0"
    if selos:
        ins += ["-threads", "1", "-loop", "1", "-i", selos]
        fil += [f"[{ult}][{_n_in(ins) - 1}:v]overlay=0:0:format=auto:shortest=1[vs]"]
        ult = "vs"
    for i, t in enumerate(flashes):
        fil += [f"color=c=0xFFF4CC:s={W}x{H}:d=0.5,format=rgba,colorchannelmixer=aa=0.85,"
                f"fade=t=in:st=0:d=0.14:alpha=1,fade=t=out:st=0.16:d=0.34:alpha=1,setpts=PTS+{t:.3f}/TB[fl{i}]",
                f"[{ult}][fl{i}]overlay=0:0:enable='between(t,{t:.3f},{t + 0.5:.3f})'[vf{i}]"]
        ult = f"vf{i}"
    if not fil:
        fil = ["[0:v]null[vn]"]; ult = "vn"
    v_enc = (["-c:v", "h264_videotoolbox", "-q:v", "68", "-profile:v", "high"]
             if usa_vt else ["-c:v", "libx264", "-crf", "17", "-preset", "veryfast", "-threads", "2", "-profile:v", "high"])
    _sh(["ffmpeg", "-y", "-loglevel", "error", "-filter_threads", "4", "-filter_complex_threads", "4", *ins,
         "-filter_complex", ";".join(fil), "-map", f"[{ult}]", "-map", "1:a",
         "-t", f"{total:.3f}", *v_enc,
         "-pix_fmt", "yuv420p", "-r", str(FPS), "-c:a", "aac", "-b:a", "192k", "-movflags", "+faststart", saida])


# ---------- legenda dinâmica (Luigi, 2026-10-13: "mais dinâmica, que chame atenção", sem render HyperFrames) ----------
FONTE_DIN = os.path.join(os.path.dirname(os.path.abspath(__file__)), "fonts", "Montserrat900.woff2")
AMARELO = (255, 214, 10, 255)
_cache_fontes_din = {}


def png_dinamica(palavras, ativa, topo, caminho, tam=86, largura=960, banda=None):
    """Caixa alta Montserrat 900, branca com contorno preto grosso; a palavra falada agora fica amarela e 15% maior.
    Uma imagem por palavra da página: troca no tempo da fala (efeito karaokê)."""
    from PIL import Image, ImageDraw, ImageFilter, ImageFont
    def fn(t):
        if t not in _cache_fontes_din:
            _cache_fontes_din[t] = ImageFont.truetype(FONTE_DIN, t)
        return _cache_fontes_din[t]
    ws = [p.upper() for p in palavras]
    tams = [int(tam * 1.15) if i == ativa else tam for i in range(len(ws))]
    esp = int(tam * 0.28)
    linhas, cur, larg = [], [], 0
    for i, w in enumerate(ws):
        lw = fn(tams[i]).getlength(w)
        if cur and larg + esp + lw > largura:
            linhas.append(cur); cur, larg = [], 0
        cur.append((i, w, lw)); larg += (esp if len(cur) > 1 else 0) + lw
    if cur:
        linhas.append(cur)
    y_base, h_img = banda if banda else (0, H)
    img = Image.new("RGBA", (W, h_img), (0, 0, 0, 0))
    y_min = max(y_base, topo - 40)
    alt_estimada = len(linhas) * int(max(tams or [tam]) * 1.3) + 100
    y_max = min(y_base + h_img, topo + alt_estimada)
    faixa_h = max(1, y_max - y_min)
    sombra = Image.new("RGBA", (W, faixa_h), (0, 0, 0, 0))
    ds, y = ImageDraw.Draw(sombra), topo
    pos = []
    for ln in linhas:
        tot = sum(x[2] for x in ln) + esp * (len(ln) - 1)
        x = (W - tot) / 2
        alt = max(tams[i] for i, _, _ in ln)
        for i, w, lw in ln:
            yy = y + (alt - tams[i]) * 0.75
            pos.append((i, w, x, yy))
            ds.text((x, yy + 6 - y_min), w, font=fn(tams[i]), fill=(0, 0, 0, 170))
            x += lw + esp
        y += int(alt * 1.12)
    img.alpha_composite(sombra.filter(ImageFilter.GaussianBlur(8)), (0, y_min - y_base))
    dr = ImageDraw.Draw(img)
    for i, w, x, yy in pos:
        dr.text((x, yy - y_base), w, font=fn(tams[i]), fill=AMARELO if i == ativa else (255, 255, 255, 255),
                stroke_width=9, stroke_fill=(0, 0, 0, 255))
    img.save(caminho, compress_level=1)
