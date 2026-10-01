"""Gera os pacotes por avatar da producao auraly_growth_sal_tenis (Auraly, growth, validacao).

Fonte unica da fala: ROTEIRO.md aprovado (lido do disco, nunca redigitado). Nenhuma fala muda por
avatar. Identidade, roupa e cenario: fichas do ROSTER AURALY ATIVO (avatares-fichas) e as ancoras
em cena real de producao/_ancoras. Medidas de cada K: FICHA_FRAMES.md.

Prompt de imagem entregue em JSON (contrato do Flow v17). Mapa K/V explicito (WORKFLOW_AURALY.md):
K01 alimenta V01 (gancho), K02 alimenta V02 a V17 (corpo em plano unico, como no modelo).

Saidas por avatar: PROMPTS_<AVATAR>.md (fonte interna com JSON e titulos), FLOW_<AVATAR>.md (mapa +
dois blocos limpos) e ENTREGA_<AVATAR>.md (pacote inteiro, um bloco por K e por V).

Uso: python3 gerar_pacote.py
"""
import json
import re
from pathlib import Path

AQUI = Path(__file__).resolve().parent
ROTEIRO = (AQUI / "ROTEIRO.md").read_text(encoding="utf-8")
INSTR = (AQUI.parent / "_flow" / "INSTRUCOES_AGENTE_FLOW.md").read_text(encoding="utf-8")
VERSAO = re.search(r"^Versao (\d+)", INSTR, re.M).group(1)
BLOCO_FLOW = re.search(r"## Bloco para a memoria do executor\n\n(.*?)\n## Historico resumido", INSTR, re.S).group(1).rstrip()

HEADS = dict(re.findall(r"^### (T\d+) · (.+)$", ROTEIRO, re.M))
TAKES = list(HEADS)
assert TAKES == ["T%d" % i for i in range(1, 18)], TAKES
FALAS = {}
for bloco in re.split(r"^(?=### T\d+ · )", ROTEIRO, flags=re.M)[1:]:
    m = re.search(r'^> "(.+?)"\s*$', bloco.split("\n## ")[0], re.M)
    FALAS[re.match(r"### (T\d+)", bloco).group(1)] = m.group(1)
assert set(FALAS) == set(TAKES), FALAS
PT = dict(re.findall(r"^\| (T\d+) \| .+? \| (.+?) \|$", ROTEIRO.split("## Tradução completa (Português)")[1].split("\n## ")[0], re.M))
assert set(PT) == set(TAKES), PT

MAPA = {"V01": "K01", **{"V%02d" % i: "K02" for i in range(2, 18)}}

FICCAO = "This is a fictional AI-generated character, no real person is depicted."
LUZ_INTERNA = ("Neutral overcast daylight from a window, the outside clearly visible through the window, never white or "
               "blown out, soft even light on the face and hands with no harsh shadows.")
LUZ_EXTERNA = ("Overcast sky with visible cloud texture, never white or blown out, neutral daylight, soft even light on "
               "the face and hands with no harsh shadows.")
REALISMO = ("Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural "
            "clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday "
            "reality, background fully in focus, everything in sharp focus, no AI polish, no beauty smoothing.")
NEG_BASE = ("no captions, no subtitles, no words overlaid on the image, no printed labels or lettering on the shaker or "
            "the shoe, no studio, no plastic-looking human skin, no extra fingers, no third hand, no supernatural "
            "lighting, no blur, no bokeh, no artificial lighting, no warm orange color cast, no yellow tint on the skin, "
            "no golden glow, no golden hour light, no sunset, no de-aging, no beauty smoothing, no visible phone, no HDR, "
            "no cinematic lighting, no second person in frame")

TENIS = ("a red running sneaker made of red suede and red mesh, with a light grey heel counter, a white midsole with a "
         "thin tan stripe, pale pink-white laces and a dark navy insole, completely plain")
SALEIRO = ("a tall dark navy-blue cylindrical salt shaker with a round pour lid, completely plain, full of coarse white "
           "kosher salt crystals")

AVATARES = [
    dict(nome="Darlene Pruitt", arquivo="DARLENE_PRUITT", genero="mulher", pron="She", pos="her",
         ancora="producao/_ancoras/darlene_pruitt_ancora.jpg",
         identidade=("The exact fictional AI character Darlene Pruitt: white American woman around fifty-six from Texas, "
                     "voluminous shaggy layered platinum-blonde hair with visible dark roots, brown eyes, fair skin with "
                     "crow's feet and fine lines, everyday makeup with defined brows, mascara and pink lipstick."),
         roupa=("White long-sleeve button-up shirt with the cuffs loosely rolled, blue jeans, a large turquoise and silver "
                "squash-blossom necklace, several big turquoise rings on the fingers of both hands and a silver cuff "
                "bracelet set with turquoise."),
         maos="her fair hand with big turquoise rings and the silver and turquoise cuff at the wrist",
         chao="the grey-brown weathered wooden plank floor of her rustic kitchen",
         bandeira_hook=("At the top edge of the frame, a small American flag on a short wooden stick stands in a small "
                        "glass mason jar on the floor, discreet but visible and in focus."),
         cena=("Her own rustic American kitchen with knotty pine wood-paneled walls, the same lived-in kitchen as the "
               "reference, unchanged, seen from knee height: behind her the wooden wall with a framed astrological chart "
               "and a small wooden crucifix; at the right the open wooden shelves by the window with glass jars and a small "
               "American flag, discreet but visible and in focus; at the left the edge of the wooden island with a white "
               "candle, a lit incense stick with a thin line of smoke and clear quartz crystals. The grey-brown weathered "
               "wooden plank floor."),
         carta=("the holographic SOULMATE card from the reference: a tarot-sized card with a rainbow mirror-foil border and "
                "saturated art of a dark-haired woman and a man embracing forehead to forehead under a starry purple sky, a "
                "glowing red heart between them and red roses around, with the word SOULMATE on a cream banner at the bottom"),
         luz=LUZ_INTERNA, sotaque="texano carregado",
         voz="voz feminina média, levemente rouca e calorosa de uma texana de cinquenta e seis anos",
         som="cozinha residencial silenciosa"),
    dict(nome="Lorraine Vance", arquivo="LORRAINE_VANCE", genero="mulher", pron="She", pos="her",
         ancora="producao/_ancoras/lorraine_vance_ancora.jpg",
         identidade=("The exact fictional AI character Lorraine Vance: white American woman around fifty-two, closely "
                     "shaved head with grey stubble, freckles and sunspots on her face and scalp, light grey-green eyes, "
                     "defined jaw, fine lines and no makeup."),
         roupa=("Light-wash denim shirt worn open over a fitted black crew-neck T-shirt, dark jeans, large silver hoop "
                "earrings, a thin silver chain necklace and black-framed reading glasses hanging from the T-shirt collar."),
         maos="her freckled fair hand with bare fingers and the denim cuff at the wrist",
         chao="the light oak wooden floor of her bright white kitchen",
         bandeira_hook=("At the top edge of the frame, a small American flag on a short wooden stick stands in a small "
                        "glass jar on the floor, discreet but visible and in focus."),
         cena=("Her own bright white American kitchen, the same lived-in kitchen as the reference, unchanged, seen from "
               "knee height: white walls and white quartz counters; behind her the light wood floating shelves with clear "
               "quartz crystal points, a lit incense stick with a thin line of smoke, a white pillar candle and a small "
               "American flag, discreet but visible and in focus; on the wall a framed zodiac wheel chart and a small wooden "
               "crucifix; a window at the left with the street clearly visible. The light oak wooden floor."),
         carta=("the holographic SOULMATE card from the reference: a tarot-sized card with a rainbow mirror-foil border and "
                "saturated art of a brown-haired woman and a man embracing under a rainbow glow, a bright heart and red roses "
                "at the bottom, with the word SOULMATE on a pale banner at the bottom"),
         luz=LUZ_INTERNA, sotaque="de Chicago",
         voz="voz feminina grave, direta e de humor seco de uma mulher de cinquenta e dois anos de Chicago",
         som="cozinha residencial silenciosa"),
    dict(nome="Walt Hensley", arquivo="WALT_HENSLEY", genero="homem", pron="He", pos="his",
         ancora="producao/_ancoras/walt_hensley_ancora.jpg",
         identidade=("The exact fictional AI character Walt Hensley, explicitly male: white American man around fifty-eight, "
                     "long grey-white beard down to mid-chest, grey moustache, grey hair combed back short on the sides, "
                     "sun-weathered skin with freckles and deep crow's feet, light grey eyes, both forearms covered in faded "
                     "traditional American tattoos with no lettering, a swallow and a red rose on the left forearm."),
         roupa="Black leather vest over a heather grey crew-neck T-shirt and dark blue jeans.",
         maos="his weathered tattooed hand and forearm",
         chao="the grey weathered wooden deck boards of his front porch",
         bandeira_hook=("At the top edge of the frame, a small American flag on a short wooden stick stands in a small "
                        "glass jar on the deck, discreet but visible and in focus."),
         cena=("His own American front porch with grey weathered wooden siding, the same lived-in porch as the reference, "
               "unchanged, seen from knee height: behind him the old wooden rocking chair and, on the siding, the framed "
               "astrological chart with a small wooden crucifix; at the left a small wooden side table with a white candle "
               "in a jar, a lit incense stick with a thin line of smoke, crystals and a fanned tarot deck; at the right edge "
               "the chrome handlebar of a motorcycle and a small American flag on the porch post against the overcast sky, "
               "discreet but visible and in focus. The grey weathered wooden deck floor."),
         carta=("the holographic SOULMATE card from the reference: a tarot-sized card with a rainbow mirror-foil border and "
                "saturated art of a long-haired woman in red and a bearded tattooed man embracing, surrounded by red roses, "
                "with an iridescent heart at the bottom and the word SOULMATE on a white banner at the bottom"),
         luz=LUZ_EXTERNA, sotaque="do Tennessee",
         voz="voz masculina grave, devagar e gentil de um homem de cinquenta e oito anos do Tennessee",
         som="varanda tranquila, leve vento e passarinhos ao longe"),
]

EMOCAO = {
    "T1": "tom baixo e confidencial, como quem conta um segredo",
    "T2": "com um meio sorriso, convicta",
    "T3": "quase sussurrando, séria",
    "T4": "urgente, em tom de alerta",
    "T5": "animada e contida, confidencial",
    "T6": "aliviada e emocionada",
    "T7": "firme e solene",
    "T8": "urgente, depois intrigada",
    "T9": "intensa e emocionada",
    "T10": "calorosa e emocionada",
    "T11": "firme e intensa",
    "T12": "urgente e rápida",
    "T13": "firme, em ritmo de instrução",
    "T14": "rápida e firme",
    "T15": "animada, depois séria",
    "T16": "séria e baixa, em alerta",
    "T17": "firme e próxima, olhando direto na lente",
}
ACAO_CORPO = {
    "T2": "{n} continua ajoelhad{o} segurando o tênis vermelho e a carta, e fala para a câmera com um leve balançar da cabeça.",
    "T3": "{n} se inclina um pouco para a lente e fala baixo, com pequenos gestos da mão que segura a carta.",
    "T4": "{n} aponta para a lente com a mão que segura a carta enquanto fala.",
    "T8": "{n} franze a testa de leve e aponta para a lente com a mão da carta.",
    "T12": "{n} fala mais rápido, marcando o ritmo com a mão que segura a carta.",
    "T13": "{n} mostra a carta para a lente e fala com firmeza.",
    "T14": "{n} marca cada instrução com a mão da carta, falando rápido.",
    "T17": "{n} se inclina um pouco para a lente, séri{o}, segurando o tênis e a carta.",
}
ACAO_PADRAO = "{n} segura o tênis vermelho com uma mão e a carta com a outra, e fala para a câmera com pequenos gestos da mão da carta."
MOMENTO = {
    "T1": "0,0 a 4,1 s (três planos; flash branco de 0,1 s no corte para o V02)",
}
TITULOS = {"K01": "gancho, sal caindo dentro do tênis de trabalho", "K02": "corpo, ajoelhado com o tênis, o saleiro e a carta"}


def keyframes(a):
    n, P, p = a["nome"], a["pron"], a["pos"]
    ref = (f"Use the first attached image only for {n}'s exact identity, wardrobe, jewelry, SOULMATE card and own "
           f"setting. Use the second attached image only as a composition reference for the camera position, framing "
           f"and action; do not copy its person, clothes, room, rug, labels or on-screen text.")
    k01 = {
        "scene": (f"The floor of {n}'s own home: {a['chao']}, seen from above. {a['bandeira_hook']}"),
        "prop": (f"{TENIS[0].upper() + TENIS[1:]}, sits on the floor, seen from above straight into its heel opening; coarse "
                 f"white kosher salt crystals are falling into the heel opening and a small white pile is forming on the "
                 f"dark navy insole. The other red running sneaker of the pair lies on its side at the right edge, cut by "
                 f"the frame. A second identical {SALEIRO.replace('a tall', 'tall')}, stands upright at the upper left."),
        "posture": (f"No face in frame: only the hand and wrist enter from the upper right, {a['maos']}, tilting "
                    f"{SALEIRO}, so the salt pours into the shoe."),
        "composition": ("High-angle shot looking down into the heel opening: the red running sneaker is the hero and "
                        "fills about 55 percent of the frame, center and lower half, its heel touching the bottom edge, "
                        "about 10 inches from the lens, the largest thing in frame; the tilted shaker in the hand fills "
                        "the upper right third; the standing shaker sits at the upper left. Nothing else is on the floor. "
                        "The background is reduced by framing, never by blur."),
        "camera": "phone held about 16 inches above the floor, 1x lens, pointing down at about sixty degrees",
        "state": "Start frame: the coarse salt is already falling from the tilted shaker into the shoe, a small white pile on the insole.",
        "negative": NEG_BASE + ", no face in frame, no feet, no shoe being worn, no spilled salt around the shoe",
    }
    k02 = {
        "scene": a["cena"],
        "prop": (f"In the hand on the right side of the frame {n} holds {TENIS}, upright by the heel collar just above the "
                 f"floor, with a small white pile of coarse salt visible inside. {SALEIRO[0].upper() + SALEIRO[1:]}, stands "
                 f"upright on the floor in the lower left corner. In the other hand, at chest height and facing the lens, "
                 f"{P.lower()} holds {a['carta']}."),
        "posture": (f"{n} kneels on one knee on the floor, facing the lens, the other knee raised, the whole body visible "
                    f"from head to knee; the hand holding the card is the one that gestures."),
        "composition": (f"The tall dark navy-blue cylindrical salt shaker is very close to the lens in the lower left corner, "
                        f"about 10 inches from the lens, and takes up about 20 percent of the frame; the red running sneaker "
                        f"sits just behind it in the lower right and fills about 25 percent of the frame; both are closer to "
                        f"the camera than {p} face, nothing else competing with them. {n} kneels right behind them, face in "
                        f"the upper quarter of the frame. Nothing else is on the floor. The background is reduced by framing, "
                        f"never by blur."),
        "camera": "phone on a small tripod on the floor at knee height, 1x lens, about three feet from the face, pointing slightly upward, fixed",
        "state": f"Start frame: {n} looks into the lens, caught mid-sentence, lips naturally parted, animated expression.",
        "negative": NEG_BASE + ", no standing pose, no sitting on a chair, no salt spilled on the floor, no second card",
    }
    out = []
    for cod, d, take in (("K01", k01, "T1"), ("K02", k02, "T2 a T17")):
        j = {
            "shot_id": f"{cod}_{a['arquivo'].lower()}",
            "fiction_note": FICCAO,
            "reference_use": ref,
            "identity_main": a["identidade"],
            "wardrobe": a["roupa"],
            "scene": d["scene"],
            "prop": d["prop"],
            "posture": d["posture"],
            "composition": d["composition"],
            "camera": d["camera"],
            "lighting": a["luz"],
            "state": d["state"],
            "realism": REALISMO,
            "aspect_ratio": "9:16 vertical",
            "negative": d["negative"],
        }
        out.append(dict(codigo=cod, take=take, titulo=TITULOS[cod], j=j))
    return out


MASC = {"convicta": "convicto", "séria": "sério", "contida": "contido", "animada": "animado",
        "aliviada": "aliviado", "emocionada": "emocionado", "intrigada": "intrigado", "intensa": "intenso",
        "calorosa": "caloroso", "rápida": "rápido", "próxima": "próximo", "baixa": "baixo"}


def emocao(t, homem):
    e = EMOCAO[t]
    if homem:
        e = re.sub(r"\w+", lambda m: MASC.get(m.group(0), m.group(0)), e)
    return e


def videos(a):
    n = a["nome"]
    h = a["genero"] == "homem"
    art, Art = ("o avatar", "O avatar") if h else ("a avatar", "A avatar")
    ouvido = "ouvido" if h else "ouvida"
    abertura = (f"{art} {n}, {a['genero']}, fala em inglês com sotaque americano {a['sotaque']}, {a['voz']}, "
                "{emo}, voz autêntica, como se exigisse ser " + ouvido + ", a seguinte frase: \"{fala}\"")
    diz = (f"{art} diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro "
           "sem cortar no final.")
    vs = []
    for i, t in enumerate(TAKES, 1):
        cod = "V%02d" % i
        if t == "T1":
            txt = ("narração em off: " + abertura.format(emo=emocao(t, h), fala=FALAS[t]) + " Ninguém aparece falando em "
                   "quadro, só as mãos.\n\n"
                   f"{diz} Sem lip sync: a fala é narração em off e nenhum rosto aparece no quadro.\n\n"
                   f"o que acontece no vídeo: plano 1, já em andamento: a mão de {n} inclina o saleiro azul-escuro e o sal "
                   "grosso cai dentro do tênis vermelho no chão. Corte, perto de um segundo, para um macro da palma aberta "
                   "cheia de sal grosso logo acima da abertura do tênis: os dedos inclinam e o sal escorre em fio para "
                   "dentro, formando um montinho branco na palmilha escura. Corte, perto dos três segundos, para o tênis "
                   "inteiro visto de cima com o monte de sal dentro, parado até o fim.\n\n"
                   "câmera: cortes internos ao clipe: plano alto olhando para baixo, macro da mão e plano de cima do tênis, "
                   "cada plano com a câmera parada\n\n"
                   f"som ambiente: {a['som']}, som do sal grosso caindo no tênis, sem música")
        else:
            acao = ACAO_CORPO.get(t, ACAO_PADRAO).format(n=n, o="o" if h else "a", a2="" if h else "a")
            txt = (abertura.format(emo=emocao(t, h), fala=FALAS[t]) + "\n\n"
                   f"{diz} Lip sync perfeito durante todo o vídeo.\n\n"
                   f"o que acontece no vídeo: {acao}\n\n"
                   "câmera: fixa, no tripé baixo, sem movimento\n\n"
                   f"som ambiente: {a['som']}, sem música")
        vs.append((cod, t, MAPA[cod], txt))
    return vs


def texto_flow(j):
    """Prompt de imagem de EXECUCAO em JSON (Flow v17): sem shot_id, com o formato na frente."""
    ordem = ["fiction_note", "reference_use", "identity_main", "wardrobe", "scene", "prop", "posture",
             "composition", "camera", "lighting", "state", "realism", "aspect_ratio", "negative"]
    assert set(ordem) == set(j) - {"shot_id"}, set(j) ^ set(ordem)
    d = {"format": "IMPORTANT: THIS IS IPHONE FOOTAGE. Vertical 9:16."}
    d.update({k: j[k] for k in ordem})
    return json.dumps(d, ensure_ascii=False, indent=2)


def mapa_kv():
    return ["MAPA K/V"] + [f"{v}: {k}" for v, k in MAPA.items()]


def capcut():
    return [
        "1. Clipes numerados na ordem: V01 a V17.",
        "2. V01 (gancho): usar só os primeiros ~4,1 s, com os três planos e a narração inteira; deixar o fim da frase "
        "(\"the house\") vazar meio segundo sobre o começo do V02, como no modelo.",
        "3. Entre V01 e V02, flash branco de 0,1 s (transição de CapCut, igual ao modelo).",
        "4. V02 a V17: zero tempo morto, todo clipe começa já falando; cortar logo depois da última palavra. "
        "Isolate Voice / Keep Vocal no áudio. Como todos saem do mesmo frame, os cortes ficam quase invisíveis, igual ao plano único do modelo.",
        "5. Legenda karaokê em caixa alta, branca, palavra atual em amarelo, no meio do quadro, do V01 ao V17.",
        "6. Do V02 em diante: \"222\" fixo no canto superior esquerdo e \"444 💰\" pequeno perto do tênis.",
        "7. Sem Voice Changer: a voz vem do prompt de cada V.",
        "8. Música só depois do gancho (a partir do V02), nunca no pré-gancho, entre -19 e -20 dB, fora da biblioteca do TikTok.",
        "9. Rótulo pequeno `AI-generated` num canto do vídeo.",
    ]


def transcricao():
    L = ["| Take | English | Português |", "|---|---|---|"]
    for t in TAKES:
        L.append(f"| {t} | {FALAS[t]} | {PT[t]} |")
    return L


def anexo(a, k):
    return "\n".join([
        "> ### 📎 ANEXAR: **2 IMAGENS**",
        f"> **1️⃣ ÂNCORA {a['nome'].upper()}** `{a['ancora']}`",
        f"> **2️⃣ FRAME DO MODELO, só composição** `input/frames_modelo/{k['codigo']}_modelo.png`",
        ">", "> ### 🆕 GERAR DO ZERO"])


def pacote(a):
    ks, vs = keyframes(a), videos(a)
    L = [f"# {a['nome']} | Auraly Growth Sal no tênis | Pacote de Prompts", "",
         "pipeline: auraly", "",
         "Vídeo modelo: `/Users/macbookairm2/Downloads/snapinsta-1790613043359.mp4` (113,9 s, avatar IA)", "",
         f"Âncora: `{a['ancora']}`", "",
         "Funil: growth, save + double tap + `222` + follow. Rodada de validação, gancho fiel ao modelo. Sem produto.", "",
         "## Índice de geração", "",
         "| Take | Keyframe | Anexar | Ação |", "|---|---|---|---|",
         f"| T1 | K01 | ÂNCORA {a['nome'].upper()} + FRAME DO MODELO (K01) | GERAR DO ZERO |",
         f"| T2 a T17 | K02 | ÂNCORA {a['nome'].upper()} + FRAME DO MODELO (K02) | GERAR DO ZERO |", "",
         "Todo K é GERAR DO ZERO: o bloco do Flow é autossuficiente. O frame do modelo entra só como composição.", "",
         "## Trava de identidade e continuidade", "",
         f"- Identidade: {a['identidade']}",
         f"- Roupa (fixa da conta): {a['roupa']}",
         f"- Cenário-base (fixo da conta): {a['cena']}",
         f"- Luz: {a['luz']}",
         f"- Voz (mesmo timbre em todos os V): {a['voz']}, sotaque americano {a['sotaque']}.",
         "- Sem 2ª pessoa.", "",
         "## Trava do prop herói", "",
         f"- Tênis: {TENIS}.", f"- Saleiro: {SALEIRO}.", f"- Carta: {a['carta']}.", "",
         "## Trava da 2ª pessoa (REF-A)", "", "- Não se aplica: não há 2ª pessoa.", "",
         "## Prompts de imagem", ""]
    for k in ks:
        L += [f"## {k['codigo']} · {k['take']} · GERAR DO ZERO · ÂNCORA {a['nome'].upper()} + FRAME DO MODELO", "",
              anexo(a, k), "", f"Cena: {k['titulo']}.", "", "```json",
              json.dumps(k["j"], ensure_ascii=False, indent=2), "```", ""]
    L += ["# Prompts de vídeo", ""]
    for cod, take, kcod, txt in vs:
        L += [f"### {cod} · {take} · usa {kcod}", "", "```text", txt, "```", ""]
    L += ["## Montagem no CapCut", ""] + capcut() + [""]
    flow = [f"# Blocos limpos para o Google Flow | {a['nome']}", "", f"Fonte interna: `PROMPTS_{a['arquivo']}.md`", "",
            "```text"] + mapa_kv() + ["```", "", "## BLOCO DE IMAGEM", "", "```text"]
    for k in ks:
        flow += [k["codigo"], texto_flow(k["j"]), ""]
    flow += ["```", "", "## BLOCO DE VÍDEO", "", "```text"]
    for cod, _, _, txt in vs:
        flow += [cod, txt, ""]
    flow += ["```", "", "## Transcrição final por take", ""] + transcricao()
    return "\n".join(L) + "\n", "\n".join(flow) + "\n"


CHECKLIST = ("Checklist de envio: 32/32 aprovados (N/A: A1, A2, A7, A9 fiéis ao modelo, gancho sem rosto e com a fala "
             "do modelo; A10 growth sem produto; C3 a C7 sem segunda pessoa, selfie, frase curta repetida, cena atuada "
             "ou motion control)")
FICHA = "Ficha: 2/2 K conferidos contra o frame do modelo, placar 14/14 cada (`FICHA_FRAMES.md`, GATE_VISUAL Parte 6)"


def entrega(a):
    ks, vs = keyframes(a), videos(a)
    L = [f"# ENTREGA | {a['nome']} | Auraly Growth Sal no tênis", "",
         "Produção `auraly_growth_sal_tenis` · Ângulo 3 · GROWTH · vídeo modelo de avatar IA · rodada de VALIDAÇÃO · perfil AURALY", "",
         f"## 1. INSTRUÇÕES PARA A MEMÓRIA DO AGENTE · GOOGLE FLOW AI (v{VERSAO})", "",
         "Colar inteiro na memória do agente antes do primeiro K.", "", "```text", BLOCO_FLOW, "```", "",
         CHECKLIST, "", FICHA, "",
         "## Anexos e mapa", "",
         f"- **Âncora {a['nome']}:** `{a['ancora']}` em TODOS os K.",
         "- **Em cada K**, anexar também o frame do modelo daquele K (`input/frames_modelo/Kxx_modelo.png`), só como composição.",
         "", "```text"] + mapa_kv() + ["```", "",
         "## 2. PROMPTS DE IMAGEM (um bloco por K)", ""]
    for k in ks:
        L += [f"### {k['codigo']} · {k['take']}, {k['titulo']} · anexar ÂNCORA + FRAME DO MODELO", "",
              "```text", k["codigo"], texto_flow(k["j"]), "```", ""]
    L += ["## 3. PROMPTS DE VÍDEO (um bloco por V)", ""]
    for cod, take, kcod, txt in vs:
        L += [f"### {cod} · {take} · frame inicial = a imagem escolhida do {kcod}", "", "```text", cod, txt, "```", ""]
    L += ["## 4. Montagem no CapCut", ""] + capcut()
    L += ["", "## 5. Transcrição final por take", ""] + transcricao()
    L += ["", "## 6. Roteiro final em inglês", ""]
    for i, t in enumerate(TAKES, 1):
        L.append(f"{i}. {FALAS[t]}")
    L += ["", " ".join(FALAS[t] for t in TAKES), ""]
    return "\n".join(L)


def main():
    for a in AVATARES:
        p, f = pacote(a)
        (AQUI / f"PROMPTS_{a['arquivo']}.md").write_text(p, encoding="utf-8")
        (AQUI / f"FLOW_{a['arquivo']}.md").write_text(f, encoding="utf-8")
        (AQUI / f"ENTREGA_{a['arquivo']}.md").write_text(entrega(a), encoding="utf-8")
    print("ok: %d avatares, Flow v%s" % (len(AVATARES), VERSAO))


if __name__ == "__main__":
    main()
