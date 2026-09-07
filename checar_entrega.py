# -*- coding: utf-8 -*-
"""
checar_entrega.py - Gate mecanico da entrega de producao.

Le os arquivos de producao/<avatar>_<slug>/ DO DISCO e checa as regras do CLAUDE.md
que podem ser verificadas por maquina. Nao depende de nada estar carregado em contexto.

Uso:
    python checar_entrega.py producao/kendra_selos
    python checar_entrega.py --todos

Existe porque regra lembrada e regra esquecida. Criado em 2026-08-26.
"""
from __future__ import annotations
import sys, os, re, json, io, glob

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

FALHAS, AVISOS, OKS = [], [], []


def falha(check, msg, loc=""):
    FALHAS.append((check, msg, loc))


def aviso(check, msg, loc=""):
    AVISOS.append((check, msg, loc))


def ok(check, msg=""):
    OKS.append((check, msg))


def ler(path):
    if not os.path.exists(path):
        return None
    return io.open(path, encoding="utf-8").read()


def linha_de(texto, idx):
    return texto.count("\n", 0, idx) + 1


# ---------------------------------------------------------------- normalizacao
ASPAS = dict.fromkeys(map(ord, "“”„″"), '"')
APOST = dict.fromkeys(map(ord, "‘’ʼ"), "'")


def norm_fala(s):
    s = s.translate(ASPAS).translate(APOST)
    s = re.sub(r"\s+", " ", s).strip().strip('"').strip()
    return s


def palavras(s):
    return [w for w in re.split(r"\s+", norm_fala(s)) if re.search(r"[A-Za-z0-9]", w)]


# ---------------------------------------------------------------- parsers
RE_TAKE = re.compile(r"^###\s+(T\d+)\s*[·|]\s*(.*)$", re.M)
# Aceita rotulo de locutor nos videos de dialogo: > MULHER: "..." / > HOMEM IDOSO: "..."
RE_FALA_ROT = re.compile(r'^>\s*(?:[A-ZÀ-Ú][A-ZÀ-Ú0-9 ª\.]{1,24}:\s*)?"(.+?)"\s*$', re.M | re.S)


def parse_takes(roteiro):
    """Retorna a lista de takes na ordem do arquivo."""
    out = []
    ms = list(RE_TAKE.finditer(roteiro))
    for i, m in enumerate(ms):
        fim = ms[i + 1].start() if i + 1 < len(ms) else len(roteiro)
        corpo = roteiro[m.start():fim]
        head = m.group(2)
        mudo = bool(re.search(r"B-ROLL|MUDO|SEM FALA", head, re.I))
        fm = RE_FALA_ROT.search(corpo)
        out.append({
            "id": m.group(1),
            "head": head.strip(),
            "fala": norm_fala(fm.group(1)) if fm else None,
            "mudo": mudo,
            "linha": linha_de(roteiro, m.start()),
        })
    return out


RE_BLOCO_JSON = re.compile(r"```json\s*\n(.*?)\n```", re.S)
RE_BLOCO_TXT = re.compile(r"```(?:text)?\s*\n(.*?)\n```", re.S)
RE_H_KEY = re.compile(r"^##\s+(REF-[A-Z0-9\-]+|K\d+[A-Z]?)\s*(?:[·|].*)?$", re.M)
RE_H_VID = re.compile(
    r"^###\s+(V\d+[A-Z]?)\s*[·|]\s*(T\d+)\s*[·|]\s*usa\s+(K\d+[A-Z]?)", re.M | re.I)

# Nome do arquivo de prompts de imagem, para os locs das falhas.
# Classico: PROMPTS_PRODUCAO.md. Auraly: PROMPTS_IMAGEM.md. checar_auraly() troca.
PROMPTS_FILE = "PROMPTS_PRODUCAO.md"


def parse_keyframes(prompts):
    """Casa cada heading K__/REF-__ com o proximo bloco json."""
    out = []
    hs = list(RE_H_KEY.finditer(prompts))
    for i, m in enumerate(hs):
        fim = hs[i + 1].start() if i + 1 < len(hs) else len(prompts)
        corpo = prompts[m.start():fim]
        jm = RE_BLOCO_JSON.search(corpo)
        quebra = prompts.find("\n", m.start())
        out.append({
            "id": m.group(1),
            "head": prompts[m.start():quebra if quebra > 0 else len(prompts)].strip(),
            "json_raw": jm.group(1) if jm else None,
            "linha": linha_de(prompts, m.start()),
        })
    return out


def parse_videos(prompts):
    out = []
    hs = list(RE_H_VID.finditer(prompts))
    for i, m in enumerate(hs):
        fim = hs[i + 1].start() if i + 1 < len(hs) else len(prompts)
        corpo = prompts[m.start():fim]
        bm = RE_BLOCO_TXT.search(corpo)
        out.append({
            "id": m.group(1), "take": m.group(2), "usa": m.group(3),
            "bloco": bm.group(1) if bm else None,
            "linha": linha_de(prompts, m.start()),
        })
    return out


def fala_do_bloco(bloco):
    """Extrai a fala entre aspas do prompt de video. Segundo retorno diz se e take mudo."""
    if bloco is None:
        return None, False
    if re.search(r"sem fala no take|voz-?over|voz off", bloco, re.I):
        return None, True
    m = re.search(r'a seguinte frase:\s*"(.+?)"', bloco, re.S)
    if not m:
        m = re.search(r'"(.{15,})"', bloco, re.S)
    return (norm_fala(m.group(1)) if m else None), False


# 2026-09-05: entrou "zero X", que e como as notas de compliance dos pacotes de
# Angulo 3 escrevem a proibicao ("Registro conferido: zero spell, witch, shield").
# Sem ele o linter acusava de registro OCULTO justamente a linha que prova que a
# lei foi obedecida, que e o falso positivo que este helper existe pra evitar.
NEGADORES = (r"nunca|nenhum\w*|jamais|sem\s|n[aã]o\s|nada de|proibid\w+|evitar|"
             r"zero\s|\bno\b|do not|don't|avoid|never")


def em_negacao(texto, idx, janela=110):
    """True se o trecho em torno de idx estiver numa frase de PROIBICAO.

    As notas de compliance listam os termos proibidos de proposito
    ('Nunca dizer one-time', 'Nenhum prompt diz feitico, bruxa'). Sem isto
    o linter acusa justamente quem esta obedecendo a regra.
    """
    ini = texto.rfind("\n", 0, idx) + 1
    ini_frase = max(ini, idx - janela)
    for sep in (". ", "! ", "? ", "**", ": "):
        pos = texto.rfind(sep, ini_frase, idx)
        if pos > ini_frase:
            ini_frase = max(ini_frase, pos + len(sep))
    return bool(re.search(NEGADORES, texto[ini_frase:idx], re.I))


# ---------------------------------------------------------------- deteccao de pipeline
def detectar_pipeline(roteiro):
    """Retorna 'auraly', 'classico', ou None se nao declarado."""
    if roteiro is None:
        return None
    m = re.search(r"^pipeline:\s*(auraly|classico)\s*$", roteiro[:600], re.M | re.I)
    return m.group(1).lower() if m else None


# ---------------------------------------------------------------- checagens
def detectar_angulo(roteiro, prompts):
    txt = (roteiro or "") + (prompts or "")
    m = re.search(r"[ÂA]ngulo\s*([1234])", txt)
    return int(m.group(1)) if m else None


def c_travessao(arquivos, takes):
    """Em dash na COPY e falha. Em titulo ou nota de producao e so aviso.

    A copy vai pro ar, o titulo nao. O proprio gabarito (brandon_angle2) tem
    em dash num heading, entao tratar heading como falha reprovaria a referencia.
    """
    falas = {t["fala"] for t in takes if t["fala"]}
    achou = False
    for nome, txt in arquivos.items():
        linhas = txt.split("\n")
        for m in re.finditer("—", txt):
            achou = True
            ln = linha_de(txt, m.start())
            linha = linhas[ln - 1]
            trecho = linha.strip()[:90]
            copy = (linha.lstrip().startswith(">")
                    or any(f[:40] in linha for f in falas if len(f) > 40)
                    or nome == "DM.md" and not linha.lstrip().startswith("#"))
            (falha if copy else aviso)(
                "travessao", "travessao (em dash) %s: %s"
                % ("na COPY" if copy else "em titulo/nota", trecho), "%s:%d" % (nome, ln))
    if not achou:
        ok("travessao", "nenhum em dash nos arquivos")


# Keyword por angulo. O Luigi decidiu manter 'yes' no Angulo 4 em 2026-08-27,
# recusando a sugestao de keyword tematica.
KEYWORD_POR_ANGULO = {1: "yes", 2: "yes", 3: "222", 4: "yes"}


def c_keyword(angulo, arquivos, takes):
    """A keyword errada so conta se estiver na FALA de um take.

    As notas de producao citam o modelo dos outros angulos de proposito
    ('Modelo do Angulo 2: Comment yes and I will send you the quiz'), e isso
    e referencia, nao CTA.
    """
    if angulo is None:
        aviso("keyword", "angulo nao detectado, checagem pulada")
        return
    esperada = KEYWORD_POR_ANGULO.get(angulo, "yes")
    proibida = "yes" if esperada != "yes" else "222"
    txt = "\n".join(arquivos.values())
    if re.search(r'["\'`]%s["\'`]|\b%s\b' % (esperada, esperada), txt, re.I):
        ok("keyword", "keyword '%s' presente (angulo %d)" % (esperada, angulo))
    else:
        falha("keyword", "keyword '%s' do angulo %d nao aparece em lugar nenhum" % (esperada, angulo))
    for t in takes:
        if not t["fala"]:
            continue
        if re.search(r'(?:comment|type|write)\s+["\'`]?%s\b' % proibida, t["fala"], re.I):
            falha("keyword", "%s usa a keyword ERRADA '%s' (angulo %d exige '%s')"
                  % (t["id"], proibida, angulo, esperada), "ROTEIRO.md:%d" % t["linha"])


def c_palavras_por_take(takes):
    ruim = False
    for t in takes:
        if t["fala"] is None:
            if not t["mudo"]:
                falha("palavras", "%s nao tem fala e nao esta marcado como B-ROLL/MUDO" % t["id"],
                      "ROTEIRO.md:%d" % t["linha"])
                ruim = True
            continue
        n = len(palavras(t["fala"]))
        if n < 13 or n > 29:
            falha("palavras",
                  "%s tem %d palavras (faixa 13 a 29). Quebrar em fim de frase, nunca inventar filler."
                  % (t["id"], n), "ROTEIRO.md:%d" % t["linha"])
            ruim = True
    if not ruim and takes:
        ok("palavras", "%d takes falados, todos dentro de 13 a 29 palavras"
           % len([t for t in takes if t["fala"]]))


def c_fala_literal(takes, videos):
    mapa = {t["id"]: t for t in takes}
    ruim = False
    for v in videos:
        t = mapa.get(v["take"])
        if t is None:
            falha("fala-literal", "%s aponta pro take %s, que nao existe no ROTEIRO.md"
                  % (v["id"], v["take"]), (PROMPTS_FILE + ":%d") % v["linha"])
            ruim = True
            continue
        fala_v, mudo_v = fala_do_bloco(v["bloco"])
        if mudo_v or t["mudo"]:
            continue
        if fala_v is None:
            falha("fala-literal", "%s nao tem fala entre aspas no bloco" % v["id"],
                  (PROMPTS_FILE + ":%d") % v["linha"])
            ruim = True
            continue
        if fala_v != t["fala"]:
            falha("fala-literal",
                  "%s NAO e copia literal de %s.\n           roteiro: %s\n           prompt : %s"
                  % (v["id"], t["id"], t["fala"], fala_v), (PROMPTS_FILE + ":%d") % v["linha"])
            ruim = True
    if not ruim and videos:
        ok("fala-literal", "%d prompts de video batem palavra por palavra com o roteiro" % len(videos))


def c_json_valido(kfs):
    ruim = False
    for k in kfs:
        if k["json_raw"] is None:
            falha("json", "%s nao tem bloco json" % k["id"], (PROMPTS_FILE + ":%d") % k["linha"])
            ruim = True
            continue
        try:
            json.loads(k["json_raw"])
        except Exception as e:
            falha("json", "%s tem JSON invalido: %s" % (k["id"], e),
                  (PROMPTS_FILE + ":%d") % k["linha"])
            ruim = True
    if not ruim and kfs:
        ok("json", "%d prompts de imagem com JSON valido" % len(kfs))


def c_bandeira(kfs):
    ruim = False
    for k in kfs:
        if k["id"].startswith("REF-"):
            continue  # excecao: prop isolado nao tem cenario
        if not k["json_raw"]:
            continue
        try:
            d = json.loads(k["json_raw"])
        except Exception:
            continue
        blob = " ".join(str(v) for v in d.values())
        if not re.search(r"\bflag\b|american flag|stars and stripes", blob, re.I):
            falha("bandeira",
                  "%s nao tem bandeira dos EUA no cenario (obrigatoria, discreta porem visivel, no campo scene)"
                  % k["id"], (PROMPTS_FILE + ":%d") % k["linha"])
            ruim = True
        elif not re.search(r"\bflag\b|american flag", str(d.get("scene", "")), re.I):
            # em prompt EDITAR a bandeira vive em keep_identical, e isso e o correto
            if not re.search(r"EDITAR do", k["head"], re.I):
                aviso("bandeira", "%s cita bandeira fora do campo 'scene'" % k["id"],
                      (PROMPTS_FILE + ":%d") % k["linha"])
    if not ruim and kfs:
        ok("bandeira", "bandeira dos EUA presente em todos os keyframes com cenario")


TERMOS_SENSIVEIS = [
    "penis", "erectile", "erection", "genital", "breast", "nipple", "gore",
    "wound", "naked", "nude", "sexual", "witch", "spell", "occult", "demon", "satan",
]


def c_negative(kfs):
    ruim = False
    for k in kfs:
        if not k["json_raw"]:
            continue
        try:
            d = json.loads(k["json_raw"])
        except Exception:
            continue
        neg = str(d.get("negative", ""))
        loc = (PROMPTS_FILE + ":%d") % k["linha"]
        if not neg:
            falha("negative", "%s nao tem campo 'negative'" % k["id"], loc)
            ruim = True
            continue
        if re.search(r"\bno text\b", neg, re.I):
            falha("negative",
                  "%s usa 'no text' seco. Correto: 'no captions, no subtitles, no words overlaid on the image'"
                  % k["id"], loc)
            ruim = True
        if "no captions" not in neg.lower():
            falha("negative", "%s nao tem 'no captions' no negative" % k["id"], loc)
            ruim = True
        for termo in TERMOS_SENSIVEIS:
            if re.search(r"\b%s\b" % termo, neg, re.I):
                falha("negative",
                      "%s lista termo sensivel '%s' no negative. O classificador le o token, nao a negacao."
                      % (k["id"], termo), loc)
                ruim = True
    if not ruim and kfs:
        ok("negative", "negatives corretos, sem 'no text' seco e sem termo sensivel")


def c_nomenclatura(prompts, roteiro):
    ruim = False
    for nome, txt in (("PROMPTS_PRODUCAO.md", prompts), ("ROTEIRO.md", roteiro)):
        if not txt:
            continue
        for m in re.finditer(r"^#{2,4}\s+([A-Z]{1,4})(\d+)", txt, re.M):
            if m.group(1) not in ("T", "K", "V", "REF"):
                falha("nomenclatura", "prefixo '%s%s' fora do padrao T/K/V/REF"
                      % (m.group(1), m.group(2)), "%s:%d" % (nome, linha_de(txt, m.start())))
                ruim = True
    if not ruim:
        ok("nomenclatura", "prefixos T/K/V/REF consistentes")


SECOES_ROTEIRO = [
    (r"Esqueleto preservado", "tabela de esqueleto preservado"),
    (r"Setups? de cena", "setups de cena"),
    (r"Roteiro cena a cena", "roteiro cena a cena"),
    (r"s[oó]-fala", "roteiro so-fala"),
    (r"Notas de produ", "notas de producao"),
]
SECOES_PROMPTS = [
    (r"[ÍI]ndice de gera", "indice de geracao"),
    (r"Trava de identidade", "trava de identidade e continuidade"),
    (r"Bloco global", "bloco global de video"),
    (r"Mapa de [âa]ncoras", "mapa de ancoras"),
    (r"CapCut", "montagem no CapCut"),
    (r"Gates? de qualidade", "gates de qualidade"),
]


def c_secoes(roteiro, prompts):
    for txt, specs, nome in ((roteiro, SECOES_ROTEIRO, "ROTEIRO.md"),
                             (prompts, SECOES_PROMPTS, "PROMPTS_PRODUCAO.md")):
        if txt is None:
            continue
        faltando, pos = [], []
        for pat, label in specs:
            m = re.search(r"^#{1,4}.*%s" % pat, txt, re.M | re.I)
            if m:
                pos.append((m.start(), label))
            else:
                faltando.append(label)
        if faltando:
            falha("secoes", "%s sem as secoes: %s" % (nome, ", ".join(faltando)))
        elif [l for _, l in sorted(pos)] != [l for _, l in pos]:
            falha("secoes", "%s tem as secoes fora da ordem do CLAUDE.md" % nome)
        else:
            ok("secoes", "%s com todas as secoes, na ordem" % nome)


def c_gerar_do_zero(kfs):
    zeros = [k["id"] for k in kfs if re.search(r"GERAR DO ZERO", k["head"], re.I)]
    edits = [k["id"] for k in kfs if re.search(r"EDITAR do", k["head"], re.I)]
    sem = [k["id"] for k in kfs
           if k["id"] not in zeros and k["id"] not in edits and not k["id"].startswith("REF-")]
    if sem:
        falha("gerar-do-zero",
              "keyframes sem acao declarada no titulo (GERAR DO ZERO ou EDITAR do K__): %s"
              % ", ".join(sem))
    if kfs:
        aviso("gerar-do-zero",
              "GERAR DO ZERO: %s  |  EDITAR: %s  (conferir a olho: um zero por SETUP, nunca por take)"
              % (", ".join(zeros) or "-", ", ".join(edits) or "-"))


def c_ref_maiuscula(prompts):
    ruim = False
    for m in re.finditer(r"^##+\s+(K\d+[A-Z]?|REF-[A-Z0-9\-]+)\s*[·|](.*)$", prompts, re.M):
        titulo = m.group(2)
        for ref in re.finditer(r"[âa]ncora\s+(\w+)|ref-(\w+)", titulo, re.I):
            achado = (ref.group(1) or ref.group(2))
            if achado and achado != achado.upper():
                falha("ref-caixa-alta", "referencia '%s' no titulo de %s nao esta em CAIXA ALTA"
                      % (achado, m.group(1)), (PROMPTS_FILE + ":%d") % linha_de(prompts, m.start()))
                ruim = True
    if not ruim:
        ok("ref-caixa-alta", "referencias nos titulos em caixa alta")


PRODUTO_PAT = (r"\bapp\b|\bquiz\b|smartphone|phone screen|app screenshot|mockup"
               r"|\bbottle\b|supplement|frasco")


def c_sem_produto(angulo, kfs):
    if angulo not in (2, 3):
        return
    ruim = False
    for k in kfs:
        if not k["json_raw"]:
            continue
        try:
            d = json.loads(k["json_raw"])
        except Exception:
            continue
        # o negative e onde o produto DEVE ser proibido, entao nao conta
        corpo = " ".join(str(v) for campo, v in d.items()
                         if campo not in ("negative", "reference_use"))
        for m in re.finditer(PRODUTO_PAT, corpo, re.I):
            ctx = corpo[max(0, m.start() - 45):m.start() + 45]
            if em_negacao(corpo, m.start(), janela=60):
                continue
            falha("sem-produto", "angulo %d nao mostra produto, mas %s cita '%s': ...%s..."
                  % (angulo, k["id"], m.group(0), ctx), (PROMPTS_FILE + ":%d") % k["linha"])
            ruim = True
    if not ruim and kfs:
        ok("sem-produto", "angulo %d sem produto em quadro" % angulo)


def c_blocos_video(videos):
    ruim = False
    for v in videos:
        if v["bloco"] is None:
            falha("blocos-video", "%s nao tem bloco de prompt" % v["id"],
                  (PROMPTS_FILE + ":%d") % v["linha"])
            ruim = True
            continue
        b = v["bloco"]
        loc = (PROMPTS_FILE + ":%d") % v["linha"]
        if not re.search(r"^c[âa]mera:", b, re.M | re.I):
            falha("blocos-video", "%s sem o bloco 'camera:'" % v["id"], loc)
            ruim = True
        if not re.search(r"^som ambiente:", b, re.M | re.I):
            falha("blocos-video", "%s sem o bloco 'som ambiente:'" % v["id"], loc)
            ruim = True
        elif not re.search(r"sem m[uú]sica", b, re.I):
            falha("blocos-video", "%s: som ambiente sem 'sem musica'" % v["id"], loc)
            ruim = True
        if not re.search(r"o que acontece no v[ií]deo:", b, re.I):
            falha("blocos-video", "%s sem o bloco 'o que acontece no video:'" % v["id"], loc)
            ruim = True
        _, mudo = fala_do_bloco(b)
        if not mudo and not re.search(r"lip sync", b, re.I):
            falha("blocos-video", "%s sem a trava de lip sync" % v["id"], loc)
            ruim = True
        # so vale dentro de "o que acontece no video". Na linha "camera:" falar de
        # enquadramento e legitimo ("fixa no enquadramento" = camera estavel), e o
        # proprio gabarito faz isso.
        acao = re.search(r"o que acontece no v[ií]deo:(.*?)(?=^c[âa]mera:|\Z)", b, re.S | re.M | re.I)
        if acao and re.search(r"composi[cç][aã]o|aspect ratio|9:16|plano m[eé]dio|close-?up", acao.group(1), re.I):
            falha("blocos-video",
                  "%s descreve enquadramento/composicao na acao. Isso e da IMAGEM, nunca do video." % v["id"], loc)
            ruim = True
    if not ruim and videos:
        ok("blocos-video", "%d prompts de video com os 5 blocos corretos" % len(videos))


def c_patch(arquivos):
    ruim = False
    pats = [r"adicione .{0,40}em todos os prompts", r"acrescente .{0,40}em (todos|cada)",
            r"troque .{0,30}em todos", r"basta (adicionar|trocar|colar)"]
    for nome, txt in arquivos.items():
        for pat in pats:
            for m in re.finditer(pat, txt, re.I):
                falha("prompt-completo",
                      "instrucao de patch: '%s'. Prompt entregue e prompt COMPLETO."
                      % txt[m.start():m.end()][:70], "%s:%d" % (nome, linha_de(txt, m.start())))
                ruim = True
    if not ruim:
        ok("prompt-completo", "nenhuma instrucao de patch, prompts entregues inteiros")


def c_angulo3(angulo, arquivos, kfs, takes):
    if angulo != 3:
        return
    antes = len([f for f in FALHAS if f[0] == "angulo3"])
    if "DM.md" not in arquivos:
        falha("angulo3", "angulo 3 exige TRES arquivos: falta o DM.md")
    else:
        dm = arquivos["DM.md"]
        for pat, msg in ((r"one[- ]time", "'one-time' e trava de copy proibida"),
                         (r"pagamento [uú]nico", "'pagamento unico' e trava de copy proibida")):
            for m in re.finditer(pat, dm, re.I):
                if em_negacao(dm, m.start()):
                    continue  # e a propria nota de proibicao
                falha("angulo3", msg + " (o checkout renova a $29/mes)",
                      "DM.md:%d" % linha_de(dm, m.start()))
    for nome, txt in arquivos.items():
        for m in re.finditer(r"\bwitch\w*|\bspell\b|circle of protection|feiti[cç]o|bruxa", txt, re.I):
            if em_negacao(txt, m.start()):
                continue  # nota de compliance listando o que NAO se diz
            falha("angulo3", "registro OCULTO detectado ('%s'). A lei e: divino, nunca oculto."
                  % m.group(0), "%s:%d" % (nome, linha_de(txt, m.start())))
    for k in kfs:
        if not k["json_raw"]:
            continue
        j = k["json_raw"]
        # "portrait orientation" e formato de carta, nao retrato de rosto
        # "his/her face" e o rosto da PROPRIA avatar, e "face turned toward the camera"
        # e a face da CARTA. Nenhum dos dois e o rosto da alma gemea.
        if re.search(r"\bportrait of\b|\bpolaroid\b|photograph of a (man|person|face)"
                     r"|drawing of a face|soulmate'?s face|face of (the|her) (soulmate|man)", j, re.I):
            if not re.search(r"obscur|out of focus|frosted|silhouett|fog|mist|ice|partial"
                             r"|unreadable|not visible|hidden", j, re.I):
                falha("angulo3",
                      "%s mostra retrato/rosto sem obscurecimento. O rosto NUNCA e revelado no video."
                      % k["id"], (PROMPTS_FILE + ":%d") % k["linha"])
    c_angulo3_stories(takes)
    c_angulo3_selo(takes)
    if len([f for f in FALHAS if f[0] == "angulo3"]) == antes:
        ok("angulo3", "travas do angulo 3 respeitadas")


# CTA de Stories, segundo canal aberto pelo Luigi em 2026-09-01.
# A PRESENCA e aviso e nao falha, de proposito: os 10 pacotes de Angulo 3 ja
# produzidos nasceram sob a regra antiga (traduzir story para DM) e roteiro
# publicado nao se reescreve. Mesma logica dos 26 takes abaixo do piso de palavras.
# O que e FALHA e usar o canal ERRADO, porque ai a escada de reveal quebra.
#
# So olha a FALA dos takes, nunca a prosa dos arquivos. A primeira versao lia o
# texto cru e reprovou os 6 pacotes existentes lendo notas de producao que
# descreviam o comportamento CERTO ("no lugar de 'Check out the surprise in my
# Stories': THE FACE IS IN YOUR MESSAGES"). Nota que explica a regra nao e copy.
STORY_PAT = r"my stories|my profile picture|check my stor|watch my stor|access(ing)? my stor"
# O CTA nomeia o objeto: "his face is in there", "find out who it is".
DECLARADO_PAT = r"\bface\b|who (it|he|she) is|(his|her|their) name|the initial"
# A copy entregou um pedaco da identidade antes do CTA, o que autoriza declarar.
# Inclui o truque do WhatsApp, que e como IG02 e IG14 ganham o direito de declarar.
#
# 2026-09-04: entrou a familia "PROVA POR PARTICIPACAO SEM LISTA", que estava
# faltando. O truque do WhatsApp e so UMA das formas de fazer a espectadora
# fornecer a identificacao; a outra, igualmente validada no swipe, e mandar ela
# pensar numa pessoa ("think of one person", IG07 e IG15) ou nomear o instante do
# pensamento ("the person who came into your head the second I said that"). Nos
# dois casos quem identifica e ELA, que e o que caracteriza prova parcial de
# identidade e autoriza o modo DECLARADO. Sem isto o gate reprovava copy correta.
IDENTIDADE_PAT = (r"\bface\b|who (it|he|she) is|(his|her|their) name|the initial"
                  r"|first letter|goes by|contact|whatsapp|\binitials?\b"
                  r"|dark features|tall\b|he is coming|his eyes"
                  r"|in(to)? your head|came to mind|appeared in your mind|think of (one|a|that) person"
                  r"|already know who")


def c_angulo3_stories(takes):
    falas = [t for t in takes if t["fala"]]
    if not falas:
        return
    i_story = next((i for i, t in enumerate(falas)
                    if re.search(STORY_PAT, t["fala"], re.I)), None)
    if i_story is None:
        aviso("angulo3", "sem CTA de Stories na fala. Desde 2026-09-01 o Angulo 3 roda DOIS canais "
                         "(comentar 222 E mandar pro Stories). Ver _stories_auraly/STORIES_PADRAO.md")
        return
    t_story = falas[i_story]
    # 1. o comentario vem primeiro. A razao mudou em 2026-09-04, o gate nao:
    #    antes o 222 vinha antes porque o Stories era ADITIVO e a DM era a promessa.
    #    Agora o Stories e o DESTINO, e o 222 vem antes porque e o SELO, e porque
    #    quem sai pro perfil pode nunca voltar pra comentar. Nos dois regimes a
    #    ordem e a mesma, e inverter ela custa o comentario e a DM de recuperacao.
    i_kw = next((i for i, t in enumerate(falas) if "222" in t["fala"]), None)
    if i_kw is not None and i_story < i_kw:
        falha("angulo3", "%s manda pro Stories ANTES de pedir o 222. O selo vem primeiro: "
                         "quem sai pro perfil pode nunca voltar pra comentar" % t_story["id"],
              "ROTEIRO.md:%d" % t_story["linha"])
    # 2. congruencia de MODO (Luigi, 2026-09-01). O CTA de Stories tem dois modos:
    #    DECLARADO (diz o que tem la dentro) e CURIOSIDADE (diz que tem algo).
    #    Declarar so funciona se a copy ja entregou um pedaco da identidade dele,
    #    porque ai nomear FECHA um loop aberto. Sem isso, nomear no ultimo segundo
    #    introduz um objeto que o video nunca apresentou, e le como isca trocada.
    #    No swipe a correlacao e limpa: os 3 que declaram (IG02, IG14, IG11) tinham
    #    entregue identidade antes; nenhum dos que prometeu bencao vaga declarou.
    #
    #    ATENCAO: a versao anterior deste gate reprovava QUALQUER mencao a rosto no
    #    take de Stories. Estava errado e apertado demais: confundia NOMEAR o rosto,
    #    que e o objeto de desejo do angulo inteiro, com ENTREGAR a imagem dele.
    #    A imagem e que nunca entra no Stories, e imagem nao se checa em roteiro.
    if re.search(DECLARADO_PAT, t_story["fala"], re.I):
        antes_do_story = " ".join(t["fala"] for t in falas[:i_story])
        if not re.search(IDENTIDADE_PAT, antes_do_story, re.I):
            falha("angulo3",
                  "%s usa o CTA de Stories em modo DECLARADO (nomeia o rosto ou quem e), mas a copy "
                  "nunca entregou identidade antes. Ou a copy ganha a prova parcial (inicial, traco, "
                  "timing), ou o CTA cai pro modo CURIOSIDADE" % t_story["id"],
                  "ROTEIRO.md:%d" % t_story["linha"])


# LEI DO SELO (Luigi, 2026-09-04). O pedido de engajamento do Angulo 3 nunca e
# um pedido seco: cada acao carrega a CONSEQUENCIA dela sobre o que ja esta vindo
# pra prospect. E a consequencia tem que bater com o GESTO REAL.
#
# O erro que gerou este gate: eu escrevi "comment 222, that's you claiming it OUT
# LOUD" e comentar e ESCREVER, nao falar. Verbo espiritual que contradiz o gesto
# fisico quebra a suspensao de descrenca na frase mais cara do roteiro.
#
# So checa o que da pra checar por maquina: a incongruencia de gesto, que e
# literal. Se ha consequencia ou so rotulo e leitura, e fica com o humano.
GESTO_FALADO_PAT = (r"out loud|say (it|this|that) (out loud|to the universe)|speak (it|this|that)"
                    r"|with your voice|said out loud|saying it out loud")


def c_angulo3_selo(takes):
    """O take que pede o 222 nao pode descrever o comentario como fala."""
    for t in takes:
        if not t["fala"] or "222" not in t["fala"]:
            continue
        m = re.search(GESTO_FALADO_PAT, t["fala"], re.I)
        if m:
            falha("angulo3",
                  "%s pede o 222 e descreve a acao como FALA ('%s'). Comentar e ESCREVER: a "
                  "consequencia tem que ser de quem digita (amarra ao nome, deixa registrado, "
                  "assina), nunca de quem fala. LEI DO SELO, angulo3-swipe-padroes"
                  % (t["id"], m.group(0)),
                  "ROTEIRO.md:%d" % t["linha"])


# Frases que fazem o produto parecer insuficiente sozinho. Banidas no Angulo 4:
# la a dor prometida (desempenho) e o mecanismo (testosterona) sao a mesma linha,
# entao toda ressalva encosta na promessa. Ver feedback-cta-produto, 2026-08-27.
LIMITE_HONESTO_PAT = (r"nothing does\b|do(es)? the rest\b|by itself\b|on (its|their) own\b"
                      r"|does not (give|fix|cure|solve|bring|repair)"
                      r"|will not (give|fix|cure|solve|bring|repair)"
                      r"|it is (just|only) a tool|is not a magic")
# Culpar a virilidade dele e a regra inviolavel do angulo (espelho da do Angulo 2).
CULPA_PAT = (r"you let (this|it|yourself)|you stopped (taking care|trying|caring)"
             r"|your own fault|you did this to yourself|you gave up on")
# O produto e um LIVRO FISICO. Mockup de ebook e tela de celular estao proibidos.
EBOOK_DIGITAL_PAT = r"mockup|phone screen|app screenshot|tablet|kindle|e-?reader|screen of a phone"
ORGAO_PAT = r"\bpenis\b|\berection\b|\bgenital"
# Promessas que a landing NAO cumpre. Conferido em https://bodyhacksformen.netlify.app
# em 2026-08-27: e um playbook de 42 hacks de HABITO, sem uma unica receita.
INCONGRUENTE_PAT = r"ancestral"
# 'recipe'/'ingredient' sao legitimos: o conteudo GRATIS do video costuma ser uma
# receita. O que nao pode e o LIVRO ser descrito assim. Por isso e aviso, e so
# quando cai perto do nome do produto.
RECEITA_PERTO_DO_PRODUTO_PAT = (r"(body hacks|the (book|playbook))[^.]{0,60}"
                                r"(recipes?|ingredients?)"
                                r"|(recipes?|ingredients?)[^.]{0,60}(body hacks|the (book|playbook))")
# Claim hormonal: a pagina rejeita o frame do frasco por escrito (hack 39), mas o
# Luigi manteve ED como eixo principal em 2026-08-27, entao isto e AVISO e nao falha.
HORMONIO_PAT = r"testosterone|\bhormones?\b"
# So pega ENTREGA FISICA. "I send you the book" e o CTA aprovado pelo Luigi e a DM
# de fato entrega o livro, entao nao entra aqui. O que quebra e objeto impresso chegando.
ENTREGA_FISICA_PAT = r"\b(mail|ship)\b[^.]{0,20}\b(book|copy|it)\b|in the mail|to your door|printed copy"


def c_angulo4(angulo, arquivos, takes, kfs):
    if angulo != 4:
        return
    antes = len([f for f in FALHAS if f[0] == "angulo4"])
    falas = [t for t in takes if t["fala"]]

    for t in falas:
        for pat, msg in (
                (LIMITE_HONESTO_PAT, "LIMITE HONESTO e PROIBIDO no angulo 4"),
                (CULPA_PAT, "culpa a masculinidade dele, regra inviolavel do angulo"),
                (r"\bjohnson\b", "'johnson' NUNCA sai da boca dela, so em legenda"),
                (ORGAO_PAT, "nome clinico de orgao nao entra em fala"),
                (INCONGRUENTE_PAT,
                 "a landing NAO vende isso. O produto e um playbook de 42 hacks de "
                 "HABITO, sem uma unica receita. Promessa assim quebra no clique"),
                (ENTREGA_FISICA_PAT,
                 "o produto e DIGITAL com entrega instantanea. O livro e prop, "
                 "a fala nunca promete objeto fisico")):
            m = re.search(pat, t["fala"], re.I)
            if m:
                falha("angulo4", "%s usa '%s': %s" % (t["id"], m.group(0), msg),
                      "ROTEIRO.md:%d" % t["linha"])

    for t in falas:
        m = re.search(RECEITA_PERTO_DO_PRODUTO_PAT, t["fala"], re.I)
        if m:
            aviso("angulo4", "%s descreve o LIVRO como receita ou ingrediente. O video pode "
                             "entregar uma receita de graca, mas o produto e um playbook de "
                             "hacks de habito." % t["id"], "ROTEIRO.md:%d" % t["linha"])
        m = re.search(HORMONIO_PAT, t["fala"], re.I)
        if m:
            aviso("angulo4", "%s usa '%s'. A landing rejeita o frame hormonal por escrito "
                             "(hack 39: 'more reliably than anything sold in a bottle'). "
                             "O mecanismo sao os hacks, nao o hormonio."
                  % (t["id"], m.group(0)), "ROTEIRO.md:%d" % t["linha"])
        m = re.search(r"\b(treats?|treating|cures?|curing)\b", t["fala"], re.I)
        if m:
            aviso("angulo4", "%s usa '%s'. O rodape da landing diz que o produto NAO trata nem "
                             "cura. 'Fix' e 'the hacks for this' carregam a mesma forca sem o "
                             "claim medico." % (t["id"], m.group(0)), "ROTEIRO.md:%d" % t["linha"])

    # A landing so fala 'drive and confidence'. O CTA tem que aterrissar nela,
    # senao ele chega numa pagina que nao parece falar do que ele ouviu.
    if falas and not re.search(r"drive and confidence|your drive\b|\bconfidence\b",
                               " ".join(t["fala"] for t in falas), re.I):
        aviso("angulo4", "nenhuma fala aterrissa em 'drive and confidence', "
                         "que e a ponte verbal com a landing")

    # O nome do produto tem que ser DITO em voz alta, e nunca sozinho.
    if falas and not any(re.search(r"body hacks for men", t["fala"], re.I) for t in falas):
        falha("angulo4", "o nome 'Body Hacks For Men' nao e dito em nenhuma fala. "
                         "O produto tem que ser visto E ouvido.")

    for k in kfs:
        if not k["json_raw"]:
            continue
        try:
            d = json.loads(k["json_raw"])
        except Exception:
            continue
        corpo = " ".join(str(v) for campo, v in d.items()
                         if campo not in ("negative", "reference_use"))
        m = re.search(EBOOK_DIGITAL_PAT, corpo, re.I)
        if m and not em_negacao(corpo, m.start(), janela=60):
            falha("angulo4", "%s cita '%s'. O produto em quadro e um LIVRO FISICO, "
                             "nunca mockup de ebook nem tela." % (k["id"], m.group(0)),
                  (PROMPTS_FILE + ":%d") % k["linha"])

    if len([f for f in FALHAS if f[0] == "angulo4"]) == antes:
        ok("angulo4", "travas do angulo 4 respeitadas")


# ---------------------------------------------------------------- pipeline Auraly (angulo 3)

# Secoes obrigatorias do ROTEIRO.md hibrido do pipeline Auraly.
# Ordem nao e checada aqui: a estrutura e mais flexivel que o classico.
SECOES_ROTEIRO_AURALY = [
    (r"pipeline:\s*auraly", "marcador pipeline: auraly"),
    (r"puzzle|Esqueleto preservado", "tabela puzzle / esqueleto preservado"),
    (r"Roteiro cena a cena", "roteiro cena a cena (com ### T1)"),
    (r"s[oó]-?fala", "roteiro so-fala"),
    (r"Notas de produ|compliance", "notas de producao com compliance"),
]

# Motivo tecnico do follow gate, revogado em 2026-09-04.
# O motivo correto e de CAMINHO: "so this stays open", nao condicao de entrega da DM.
FOLLOW_GATE_REVOGADO_PAT = (
    r"(it may|may not)\s+(let me|be able to)\s+reach you"
    r"|not let me reach you after"
    r"|can.?t reach you after you comment"
)

# Linguagem do funil pre-inversao: DM como destino principal.
# Desde 2026-09-04 o destino e o Stories, DM e recuperacao.
FUNIL_PRE_INVERSAO_PAT = (
    r"send (it|the face|their face) (to your|in a) (DM|message|inbox)"
    r"|face (will|is going to) (arrive|come|land) in your (DM|messages)"
    r"|I (will|am going to) send (you|it) (to )?your (DM|messages)"
    r"|straight into your (DM|messages)"
)

# Parser de PROMPTS_VIDEO_FLOW.md — formato ## V01A · T1 · K01 descricao
RE_H_VID_FLOW = re.compile(
    r"^##\s+(V\d+[A-E]?)\s*[·|]\s*(T\d+)", re.M | re.I)


def parse_videos_flow(flow_txt):
    """Parse PROMPTS_VIDEO_FLOW.md do pipeline Auraly."""
    out = []
    hs = list(RE_H_VID_FLOW.finditer(flow_txt))
    for i, m in enumerate(hs):
        fim = hs[i + 1].start() if i + 1 < len(hs) else len(flow_txt)
        corpo = flow_txt[m.start():fim]
        bm = RE_BLOCO_TXT.search(corpo)
        out.append({
            "id": m.group(1), "take": m.group(2),
            "bloco": bm.group(1) if bm else None,
            "linha": linha_de(flow_txt, m.start()),
        })
    return out


def c_secoes_auraly(roteiro):
    if roteiro is None:
        return
    faltando = []
    for pat, label in SECOES_ROTEIRO_AURALY:
        if not re.search(r"^#{0,4}.*%s" % pat, roteiro, re.M | re.I):
            faltando.append(label)
    if faltando:
        falha("secoes", "ROTEIRO.md (auraly) sem as secoes: %s" % ", ".join(faltando))
    else:
        ok("secoes", "ROTEIRO.md (auraly) com todas as secoes obrigatorias")


def c_follow_gate_auraly(takes):
    """O motivo tecnico do follow gate foi revogado em 2026-09-04."""
    for t in takes:
        if not t["fala"]:
            continue
        m = re.search(FOLLOW_GATE_REVOGADO_PAT, t["fala"], re.I)
        if m:
            falha("angulo3",
                  "%s usa o motivo TECNICO do follow gate ('%s'), revogado em 2026-09-04. "
                  "O motivo agora e o CAMINHO: 'so this stays open', nunca a condicao de entrega da DM."
                  % (t["id"], m.group(0)),
                  "ROTEIRO.md:%d" % t["linha"])


def c_funil_invertido_auraly(roteiro):
    """Detecta linguagem do funil pre-inversao (DM como destino principal)."""
    for m in re.finditer(FUNIL_PRE_INVERSAO_PAT, roteiro, re.I):
        if em_negacao(roteiro, m.start()):
            continue
        falha("angulo3",
              "funil pre-inversao: '%s'. Desde 2026-09-04 o destino e o Stories, DM e recuperacao."
              % m.group(0),
              "ROTEIRO.md:%d" % linha_de(roteiro, m.start()))


def c_blocos_video_flow(videos, sub_nome):
    """Verifica os 5 blocos do PROMPTS_VIDEO_FLOW.md (pipeline Auraly)."""
    ruim = False
    for v in videos:
        if v["bloco"] is None:
            falha("blocos-video", "%s/%s nao tem bloco de prompt" % (sub_nome, v["id"]))
            ruim = True
            continue
        b = v["bloco"]
        loc = "%s/PROMPTS_VIDEO_FLOW.md:%d" % (sub_nome, v["linha"])
        if not re.search(r"^c[âa]mera:", b, re.M | re.I):
            falha("blocos-video", "%s/%s sem o bloco 'camera:'" % (sub_nome, v["id"]), loc)
            ruim = True
        if not re.search(r"^som ambiente:", b, re.M | re.I):
            falha("blocos-video", "%s/%s sem o bloco 'som ambiente:'" % (sub_nome, v["id"]), loc)
            ruim = True
        elif not re.search(r"sem m[uú]sica", b, re.I):
            falha("blocos-video", "%s/%s: som ambiente sem 'sem musica'" % (sub_nome, v["id"]), loc)
            ruim = True
        if not re.search(r"o que acontece no v[ií]deo:", b, re.I):
            falha("blocos-video", "%s/%s sem 'o que acontece no video:'" % (sub_nome, v["id"]), loc)
            ruim = True
        _, mudo = fala_do_bloco(b)
        if not mudo and not re.search(r"lip sync", b, re.I):
            falha("blocos-video", "%s/%s sem a trava de lip sync" % (sub_nome, v["id"]), loc)
            ruim = True
    if not ruim and videos:
        ok("blocos-video", "%s: %d prompts de video com os 5 blocos corretos"
           % (sub_nome, len(videos)))


def c_fala_literal_flow(takes, videos, sub_nome):
    """Verifica fala literal nos prompts de video do pipeline Auraly."""
    mapa = {t["id"]: t for t in takes}
    ruim = False
    for v in videos:
        t = mapa.get(v["take"])
        if t is None:
            aviso("fala-literal", "%s/%s aponta pro take %s, nao encontrado no ROTEIRO.md"
                  % (sub_nome, v["id"], v["take"]))
            continue
        fala_v, mudo_v = fala_do_bloco(v["bloco"])
        if mudo_v or t["mudo"]:
            continue
        if fala_v is None:
            falha("fala-literal", "%s/%s nao tem fala entre aspas no bloco" % (sub_nome, v["id"]),
                  "%s/PROMPTS_VIDEO_FLOW.md:%d" % (sub_nome, v["linha"]))
            ruim = True
            continue
        if fala_v != t["fala"]:
            falha("fala-literal",
                  "%s/%s NAO e copia literal de %s.\n           roteiro: %s\n           prompt : %s"
                  % (sub_nome, v["id"], t["id"], t["fala"], fala_v),
                  "%s/PROMPTS_VIDEO_FLOW.md:%d" % (sub_nome, v["linha"]))
            ruim = True
    if not ruim and videos:
        ok("fala-literal", "%s: %d prompts batem com o roteiro" % (sub_nome, len(videos)))


def c_preco_auraly(arquivos):
    """Auraly nunca fala de preco (Luigi, 2026-09-07), nem 'one-time' nem valor."""
    pats = (r"\bone[- ]time\b", r"pagamento [uú]nico", r"\$\s?\d", r"\bUSD\b",
            r"\b\d+\s?dollars?\b", r"per month", r"por m[eê]s")
    ruim = False
    for nome, txt in arquivos.items():
        if nome not in ("ROTEIRO.md",):
            continue
        for t in parse_takes(txt):
            if not t["fala"]:
                continue
            for pat in pats:
                m = re.search(pat, t["fala"], re.I)
                if m:
                    falha("preco", "%s cita preco/pagamento na fala ('%s'). Auraly nunca fala de preco."
                          % (t["id"], m.group(0)), "ROTEIRO.md:%d" % t["linha"])
                    ruim = True
    if not ruim:
        ok("preco", "nenhuma fala cita preco")


def checar_auraly(pasta, roteiro):
    """Valida o pipeline Auraly (marcador pipeline: auraly, angulo 3).

    Nao exige PROMPTS_PRODUCAO.md nem DM.md.
    Aceita nomes descritivos de imagem e video.
    Prompts de video ficam em subpastas de avatar/data.
    Se houver PROMPTS_IMAGEM.md, valida os JSON de imagem.
    """
    global PROMPTS_FILE
    ganchos = ler(os.path.join(pasta, "GANCHOS_VISUAIS.md"))
    prompts_img = ler(os.path.join(pasta, "PROMPTS_IMAGEM.md"))
    if roteiro is None:
        falha("arquivos", "ROTEIRO.md nao existe")
    if ganchos is None:
        aviso("arquivos", "GANCHOS_VISUAIS.md nao encontrado (esperado no pipeline Auraly)")
    if prompts_img is None:
        aviso("arquivos", "PROMPTS_IMAGEM.md nao encontrado (esperado antes da geracao de imagem)")

    arquivos = {}
    for nome in ("ROTEIRO.md", "GANCHOS_VISUAIS.md", "PROMPTS_IMAGEM.md"):
        t = ler(os.path.join(pasta, nome))
        if t is not None:
            arquivos[nome] = t

    takes = parse_takes(roteiro) if roteiro else []

    c_travessao(arquivos, takes)
    c_keyword(3, arquivos, takes)
    c_palavras_por_take(takes)
    c_secoes_auraly(roteiro)
    c_angulo3_stories(takes)
    c_angulo3_selo(takes)
    c_follow_gate_auraly(takes)
    c_preco_auraly(arquivos)
    c_patch(arquivos)
    if roteiro:
        c_funil_invertido_auraly(roteiro)

    # PROMPTS_IMAGEM.md: valida os JSON de imagem com os mesmos checks do classico
    if prompts_img:
        PROMPTS_FILE = "PROMPTS_IMAGEM.md"
        kfs = parse_keyframes(prompts_img)
        if kfs:
            c_json_valido(kfs)
            c_bandeira(kfs)
            c_negative(kfs)
            c_sem_produto(3, kfs)
            c_gerar_do_zero(kfs)
            c_ref_maiuscula(prompts_img)
        else:
            aviso("arquivos", "PROMPTS_IMAGEM.md sem headings K__/REF-__ reconheciveis")
        PROMPTS_FILE = "PROMPTS_PRODUCAO.md"

    # Registro divino (mesmo check do classico)
    antes = len([f for f in FALHAS if f[0] == "angulo3"])
    for nome, txt in arquivos.items():
        for m in re.finditer(r"\bwitch\w*|\bspell\b|circle of protection|feiti[cç]o|bruxa", txt, re.I):
            if em_negacao(txt, m.start()):
                continue
            falha("angulo3", "registro OCULTO detectado ('%s'). A lei e: divino, nunca oculto."
                  % m.group(0), "%s:%d" % (nome, linha_de(txt, m.start())))
    if len([f for f in FALHAS if f[0] == "angulo3"]) == antes and takes:
        ok("angulo3", "travas do angulo 3 (auraly) respeitadas")

    # Varrer subpastas de avatar para PROMPTS_VIDEO_FLOW.md
    for sub in sorted(glob.glob(os.path.join(pasta, "*"))):
        if not os.path.isdir(sub):
            continue
        flow = ler(os.path.join(sub, "PROMPTS_VIDEO_FLOW.md"))
        if flow is None:
            continue
        sub_nome = os.path.basename(sub)
        videos_flow = parse_videos_flow(flow)
        if videos_flow:
            c_blocos_video_flow(videos_flow, sub_nome)
            if takes:
                c_fala_literal_flow(takes, videos_flow, sub_nome)

    return takes


# ---------------------------------------------------------------- runner
def checar(pasta):
    global FALHAS, AVISOS, OKS
    FALHAS, AVISOS, OKS = [], [], []
    roteiro = ler(os.path.join(pasta, "ROTEIRO.md"))

    # Roteamento por marcador de pipeline
    if detectar_pipeline(roteiro) == "auraly":
        takes = checar_auraly(pasta, roteiro)
        print("=" * 82)
        print("  %s   (pipeline: auraly | angulo 3 | %d takes)" % (pasta, len(takes)))
        print("=" * 82)
        for c, m in OKS:
            print("  [OK]     %-16s %s" % (c, m))
        for c, m, loc in AVISOS:
            print("  [AVISO]  %-16s %s%s" % (c, m, ("  (%s)" % loc) if loc else ""))
        for c, m, loc in FALHAS:
            print("  [FALHA]  %-16s %s%s" % (c, m, ("\n           -> %s" % loc) if loc else ""))
        print("-" * 82)
        print("  %d ok, %d avisos, %d FALHAS" % (len(OKS), len(AVISOS), len(FALHAS)))
        print()
        return len(FALHAS)

    # Pipeline classico (angulos 1, 2, 4 — e angulo 3 sem marcador, que reprova por arquivos)
    prompts = ler(os.path.join(pasta, "PROMPTS_PRODUCAO.md"))
    if roteiro is None:
        falha("arquivos", "ROTEIRO.md nao existe")
    if prompts is None:
        falha("arquivos", "PROMPTS_PRODUCAO.md nao existe")

    arquivos = {}
    for nome in ("ROTEIRO.md", "PROMPTS_PRODUCAO.md", "DM.md", "GANCHOS.md"):
        t = ler(os.path.join(pasta, nome))
        if t is not None:
            arquivos[nome] = t

    angulo = detectar_angulo(roteiro or "", prompts or "")
    takes = parse_takes(roteiro) if roteiro else []
    kfs = parse_keyframes(prompts) if prompts else []
    videos = parse_videos(prompts) if prompts else []

    c_travessao(arquivos, takes)
    c_keyword(angulo, arquivos, takes)
    c_palavras_por_take(takes)
    c_fala_literal(takes, videos)
    c_json_valido(kfs)
    c_bandeira(kfs)
    c_negative(kfs)
    c_nomenclatura(prompts or "", roteiro or "")
    c_secoes(roteiro, prompts)
    c_gerar_do_zero(kfs)
    c_ref_maiuscula(prompts or "")
    c_sem_produto(angulo, kfs)
    c_blocos_video(videos)
    c_patch(arquivos)
    c_angulo3(angulo, arquivos, kfs, takes)
    c_angulo4(angulo, arquivos, takes, kfs)

    print("=" * 82)
    print("  %s   (angulo %s | %d takes | %d keyframes | %d clipes)"
          % (pasta, angulo if angulo else "?", len(takes), len(kfs), len(videos)))
    print("=" * 82)
    for c, m in OKS:
        print("  [OK]     %-16s %s" % (c, m))
    for c, m, loc in AVISOS:
        print("  [AVISO]  %-16s %s%s" % (c, m, ("  (%s)" % loc) if loc else ""))
    for c, m, loc in FALHAS:
        print("  [FALHA]  %-16s %s%s" % (c, m, ("\n           -> %s" % loc) if loc else ""))
    print("-" * 82)
    print("  %d ok, %d avisos, %d FALHAS" % (len(OKS), len(AVISOS), len(FALHAS)))
    print()
    return len(FALHAS)


def main():
    args = sys.argv[1:]
    if not args:
        print(__doc__)
        return 2
    if args[0] == "--todos":
        alvos = sorted(d for d in glob.glob("producao/*")
                       if os.path.isdir(d) and os.path.exists(os.path.join(d, "ROTEIRO.md")))
    else:
        alvos = args
    total = sum(checar(a.rstrip("/\\")) for a in alvos)
    print("TOTAL: %d falhas em %d pasta(s)" % (total, len(alvos)))
    return 1 if total else 0


if __name__ == "__main__":
    sys.exit(main())
