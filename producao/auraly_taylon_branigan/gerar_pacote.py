"""Gera os pacotes por avatar da producao auraly_taylon_branigan (Auraly, growth, dinheiro, avatar IA, validacao).

Fonte unica da fala: ROTEIRO.md aprovado (lido do disco, nunca redigitado). Identidade e roupa: os CHARACTER
SHEETS (producao/_ancoras/character_sheets/, regra so Auraly de 2026-10-04). Cenario e angulo de camera: os do
VIDEO MODELO, quase 100% fieis (varanda e soleira da porta). Medidas: FICHA_FRAMES.md.
Mapa K/V: K01 -> V01 (gancho, voz-over, plano unico), K02 -> V02 a V18 (corpo, plano unico).

Saidas por avatar: PROMPTS_<AVATAR>.md, FLOW_<AVATAR>.md e ENTREGA_<AVATAR>.md.
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
assert TAKES == ["T%d" % i for i in range(1, 19)], TAKES
FALAS = {}
for bloco in re.split(r"^(?=### T\d+ · )", ROTEIRO, flags=re.M)[1:]:
    m = re.search(r'^> "(.+?)"\s*$', bloco.split("\n## ")[0], re.M)
    FALAS[re.match(r"### (T\d+)", bloco).group(1)] = m.group(1)
assert set(FALAS) == set(TAKES), FALAS.keys()
PT = dict(re.findall(r"^\| (T\d+) \| .+? \| (.+?) \|$", ROTEIRO.split("## Tabela bilíngue completa")[1], re.M))
assert set(PT) == set(TAKES), PT

MAPA = {"V01": "K01", **{"V%02d" % i: "K02" for i in range(2, 19)}}

FICCAO = "This is a fictional AI-generated character, no real person is depicted."
CENA_K01 = ("The front porch of an ordinary American suburban house seen from just above a sturdy wooden bench with visible "
            "grain that fills the bottom of the frame: a white painted porch column in the middle behind the hands, a dark "
            "wood door frame and a stained wooden front door with a glass pane at the right edge, a woven doormat on the "
            "porch floor, a white flowering shrub in a dark pot at the left, and green garden shrubs and flagstone paving "
            "behind. A small American flag is tucked into the shrubs at the left, discreet but visible and in focus.")
CENA_K02 = ("The open front doorway of an ordinary American house seen from the porch: the avatar sits on the wooden "
            "threshold of the open front door, the dark wood door jamb at the left with green ivy climbing the white porch "
            "column at the far left, the open stained-wood front door at the right edge with a black iron lever handle, and "
            "behind the avatar through the doorway a living room with a window showing green trees outside and a table lamp "
            "switched off beside it, a framed map of the United States on the cream wall at the upper right above a wooden "
            "bookshelf full of books, and below the threshold a gray stone step and a woven doormat. A small American flag is "
            "tucked into the ivy on the column at the left, discreet but visible and in focus.")
LUZ_K01 = ("Neutral overcast daylight outdoors, cool and even, soft light on the hands and the wallet, no harsh shadows and "
           "no dappled sun patches on the bench.")
LUZ_K02 = ("Neutral overcast daylight from a window, the outside clearly visible through the window, soft even light on "
           "the face with no harsh shadows.")
REALISMO = ("Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural "
            "clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday "
            "reality, background fully in focus, everything in sharp focus, no AI polish, no beauty smoothing.")
NEG = ("no captions, no subtitles, no words overlaid on the image, no brand name or logo on the shaker or the wallet, no "
       "studio, no grey studio background, no plastic-looking human skin, no extra fingers, no third hand, no supernatural "
       "lighting, no blur, no bokeh, no artificial lighting, no warm orange color cast, no yellow tint on the skin, no "
       "golden glow, no golden hour light, no sunset, no sun flares, no de-aging, no beauty smoothing, no visible phone, no "
       "HDR, no cinematic lighting, no second person in frame, no tarot cards, no candles, no magic effects")
SALEIRO = ("a navy blue cylindrical salt shaker with a plain white perforated lid and no label")
CARTEIRA = ("a brown leather bifold wallet, plain, no logo, open with its card slots and inner pocket visible")

AVATARES = [
    dict(nome="Avery Knox", arquivo="AVERY_KNOX", genero="mulher", pos="her",
         sheet="producao/_ancoras/character_sheets/avery_knox_character_sheet.jpg",
         identidade=("The exact fictional AI character Avery Knox: white American woman around fifty-six, voluminous shaggy "
                     "layered platinum-blonde hair with visible darker roots, brown eyes, fair skin with crow's feet and "
                     "fine lines, everyday makeup with defined brows, mascara and pink lipstick."),
         roupa=("White long-sleeve button-up shirt with a chest pocket and the cuffs rolled, medium-blue bootcut jeans, "
                "a large turquoise and silver squash-blossom necklace, several big turquoise rings and silver "
                "cuff bracelets set with turquoise on both wrists."),
         maos="her fair hands with big turquoise rings and silver cuff bracelets, the cuffs of a white shirt rolled to the forearms",
         sotaque="texano carregado",
         voz="voz feminina média, levemente rouca e calorosa de uma texana de cinquenta e seis anos"),
    dict(nome="Devon Price", arquivo="DEVON_PRICE", genero="mulher", pos="her",
         sheet="producao/_ancoras/character_sheets/devon_price_character_sheet.jpg",
         identidade=("The exact fictional AI character Devon Price: white American woman around fifty-two, closely shaved "
                     "head with grey stubble, freckles and sunspots on her face and scalp, light grey-green eyes, defined "
                     "jaw, fine lines and no makeup."),
         roupa=("Light-wash denim shirt worn open with the cuffs rolled over a fitted black crew-neck T-shirt, dark blue "
                "jeans, large silver hoop earrings, a thin silver chain necklace and black-framed reading "
                "glasses hanging from the T-shirt collar."),
         maos="her freckled fair hands with bare fingers, the cuffs of a light-wash denim shirt rolled on the forearms",
         sotaque="de Chicago",
         voz="voz feminina grave, direta e de humor seco de uma mulher de cinquenta e dois anos de Chicago"),
    dict(nome="Jordan Vale", arquivo="JORDAN_VALE", genero="homem", pos="his",
         sheet="producao/_ancoras/character_sheets/jordan_vale_character_sheet.jpg",
         identidade=("The exact fictional AI character Jordan Vale, explicitly male: white American man around fifty-eight, "
                     "long grey-white beard down to mid-chest, grey moustache, grey hair combed back short on the sides, "
                     "sun-weathered skin with freckles and deep crow's feet, light grey eyes, both forearms covered in faded "
                     "traditional American tattoos with no lettering, a swallow and a red rose on the left forearm."),
         roupa="Black leather vest over a heather grey crew-neck T-shirt, dark blue straight jeans.",
         maos="his weathered hands with the faded traditional tattoos on both bare forearms, a swallow and a red rose on the left forearm",
         sotaque="do Tennessee",
         voz="voz masculina grave, devagar e gentil de um homem de cinquenta e oito anos do Tennessee"),
]

EMOCAO = {
    "T2": "séria e intrigante", "T3": "convicta e intensa", "T4": "urgente e direta", "T5": "solene e firme",
    "T6": "aliviada e firme", "T7": "direta e urgente", "T8": "intensa e solene", "T9": "séria, em tom de aviso",
    "T10": "intensa e baixa", "T11": "calorosa e firme", "T12": "séria e urgente", "T13": "rápida e prática",
    "T14": "firme e confiante", "T15": "rápida e prática", "T16": "calorosa e animada", "T17": "séria e baixa",
    "T18": "próxima e urgente",
}
MASC = {"séria": "sério", "convicta": "convicto", "intensa": "intenso", "direta": "direto", "aliviada": "aliviado",
        "rápida": "rápido", "prática": "prático", "baixa": "baixo", "próxima": "próximo", "calorosa": "caloroso",
        "animada": "animado", "solene": "solene"}
ACAO = {
    "T4": "{n} aponta para a lente com a mão livre.",
    "T6": "{n} abre a mão livre com a palma para cima, aliviado(a).",
    "T7": "{n} aponta para baixo, para os comentários, e depois para a lente.",
    "T8": "{n} fecha a mão livre devagar em punho, mantém e solta.",
    "T9": "{n} balança a mão livre de um lado para o outro, como quem manda parar.",
    "T14": "{n} abre a mão livre para a lente, com a palma aberta.",
    "T15": "{n} toca o ar duas vezes com o dedo indicador, como quem toca a tela, e aponta para baixo, para os comentários.",
    "T17": "{n} fala mais baixo, com o dedo indicador erguido.",
    "T18": "{n} aponta para a lente com a mão livre.",
}
ACAO_PADRAO = "{n} gesticula com a mão livre, pequenos gestos naturais, olhando direto para a lente."
TITULOS = {"K01": "gancho, saleiro despejando sal na carteira aberta, macro das mãos na varanda",
           "K02": "corpo, sentado na soleira da porta aberta com a carteira nas mãos"}

CAMERA_K01 = ("handheld phone at upper-chest height about 14 inches from the hands, 1x lens, tilted downward about 35 "
              "degrees, steady")
CAMERA_K02 = ("phone resting at chest height about 3.5 feet off the porch floor and about four feet from the doorway, 1x "
              "lens, level, fixed")


def keyframes(a):
    n, p = a["nome"], a["pos"]
    ref = (f"Use the first attached image (character sheet) only for {n}'s exact identity (face, skin, hair, body) and "
           f"wardrobe; ignore its grey studio background. Use the second attached image (frame of the model video) as the "
           f"reference for the setting, camera angle and framing; do not copy its person, clothes or on-screen text.")
    k01 = {
        "scene": CENA_K01, "lighting": LUZ_K01, "camera": CAMERA_K01,
        "prop": (f"In one of {a['maos']}, {SALEIRO} is tipped, a thin stream of coarse white salt "
                 f"pouring from its lid into {CARTEIRA}, which the other hand holds open from the right edge of the frame, "
                 f"thumb on the wallet's edge, a small pile of salt already at the bottom of the wallet."),
        "posture": (f"Only {n}'s hands and forearms are in the frame, entering from the right edge: one hand tips the shaker "
                    f"from the upper left, the other holds the wallet open in the lower middle. No face is visible."),
        "composition": (f"Macro of the hands. The wallet is in the lower middle of the frame, very close to the lens, about "
                        f"12 inches from the lens, taking up about 10 percent of the frame; the navy shaker is in the upper left, "
                        f"about 10 inches from the lens, about 8 percent of the frame, the salt stream falling between them; "
                        f"both are the hero, large in frame, nothing else competing with them. The bench fills the bottom of "
                        f"the frame. Nothing else is in the foreground. The background is reduced by framing, never by blur."),
        "state": "Start frame: the salt is already pouring in a thin stream from the shaker into the open wallet.",
        "negative": NEG + ", no face, no second person, no salt spilled on the bench",
        "identity": a["identidade"] + " Only the hands and forearms appear in this shot.",
    }
    k02 = {
        "scene": CENA_K02, "lighting": LUZ_K02, "camera": CAMERA_K02,
        "prop": (f"{n} holds {CARTEIRA}, empty, open in both hands at belly height, held forward toward the lens. "
                 f"{SALEIRO[0].upper() + SALEIRO[1:]} stands upright on the wooden threshold at the lower left."),
        "posture": (f"{n} sits on the wooden threshold of the open front door, leaning slightly forward with the elbows "
                    f"near the knees, holding the open wallet in both hands, looking straight into the lens."),
        "composition": (f"The open wallet is in the lower middle of the frame, about 30 inches from the lens, taking up about "
                        f"4 percent of the frame, closer to the camera than {p} face, nothing else competing with it; the "
                        f"navy salt shaker stands at the lower left. {n} is framed from the top of the head to mid-thigh, "
                        f"{p} face in the upper third. Nothing else is in the foreground. The background is reduced by "
                        f"framing, never by blur."),
        "state": f"Start frame: {n} caught mid-sentence, lips naturally parted, serious intrigued expression, wallet held open.",
        "negative": NEG + ", no salt on the wallet yet, no salt on the floor",
        "identity": a["identidade"],
    }
    out = []
    for cod, d, take in (("K01", k01, "T1"), ("K02", k02, "T2 a T18")):
        j = {"shot_id": f"{cod}_{a['arquivo'].lower()}", "fiction_note": FICCAO, "reference_use": ref,
             "identity_main": d["identity"], "wardrobe": a["roupa"], "scene": d["scene"], "prop": d["prop"],
             "posture": d["posture"], "composition": d["composition"], "camera": d["camera"], "lighting": d["lighting"],
             "state": d["state"], "realism": REALISMO, "aspect_ratio": "9:16 vertical", "negative": d["negative"]}
        out.append(dict(codigo=cod, take=take, titulo=TITULOS[cod], j=j))
    return out


def emocao(t, homem):
    e = EMOCAO[t]
    return re.sub(r"\w+", lambda m: MASC.get(m.group(0), m.group(0)), e) if homem else e


def videos(a):
    n = a["nome"]
    h = a["genero"] == "homem"
    art = "o avatar" if h else "a avatar"
    ouvido = "ouvido" if h else "ouvida"
    vs = []
    for i, t in enumerate(TAKES, 1):
        cod = "V%02d" % i
        if t == "T1":
            txt = (f"narração em off: {art} {n}, {a['genero']}, fala em inglês com sotaque americano {a['sotaque']}, "
                   f"{a['voz']}, tom baixo e confidencial, como quem conta um segredo, voz autêntica, como se exigisse ser "
                   f"{ouvido}, a seguinte frase: \"{FALAS[t]}\" Ninguém aparece falando em quadro, só as mãos.\n\n"
                   f"{art} diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro "
                   f"sem cortar no final. Sem lip sync: a fala é narração em off e nenhum rosto aparece no quadro.\n\n"
                   f"o que acontece no vídeo: plano único contínuo, já em andamento: a mão de {n} inclina o saleiro azul-escuro "
                   f"e o sal grosso cai em fio dentro da carteira marrom aberta, segurada pela outra mão; o fio de sal "
                   f"diminui e para perto do fim, deixando um montinho de sal no fundo da carteira, e as duas mãos ficam "
                   f"paradas até o fim.\n\n"
                   "câmera: plano único, sem cortes, câmera parada na altura do peito olhando para baixo\n\n"
                   "som ambiente: varanda residencial silenciosa, som do sal grosso caindo na carteira, sem música")
        else:
            txt = (f"{art} {n}, {a['genero']}, fala em inglês com sotaque americano {a['sotaque']}, {a['voz']}, "
                   f"{emocao(t, h)}, voz autêntica, como se exigisse ser {ouvido}, a seguinte frase: \"{FALAS[t]}\"\n\n"
                   f"{art} diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro "
                   f"sem cortar no final. Lip sync perfeito durante todo o vídeo.\n\n"
                   f"o que acontece no vídeo: {n} segura a carteira aberta com uma mão na altura da barriga, sentado na "
                   f"soleira da porta aberta. " .replace("sentado", "sentado" if h else "sentada")
                   + ACAO.get(t, ACAO_PADRAO).format(n=n).replace("aliviado(a)", "aliviado" if h else "aliviada")
                   + " O saleiro azul-escuro continua parado na soleira, no canto inferior esquerdo.\n\n"
                   "câmera: fixa na altura do peito, sem movimento\n\n"
                   "som ambiente: varanda residencial silenciosa, sem música")
        vs.append((cod, t, MAPA[cod], txt))
    return vs


def texto_flow(j):
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
        "1. Clipes numerados na ordem: V01 a V18.",
        "2. V01 (gancho, voz-over): usar só os primeiros ~3,1 s, com a narração inteira; deixar o fim da frase (\"the house\") "
        "vazar meio segundo sobre o começo do V02.",
        "3. Entre V01 e V02, corte seco, sem flash (o modelo corta seco aos 3,12 s).",
        "4. V02 a V18: zero tempo morto, todo clipe começa já falando; cortar logo depois da última palavra. Isolate Voice / "
        "Keep Vocal. Todos saem do mesmo frame (K02), então a troca de clipe fica no mesmo enquadramento, como no plano único do modelo.",
        "5. Legenda karaokê em caixa alta, palavra atual em amarelo ou vermelho, no meio-baixo do quadro, do V01 ao V18.",
        "6. O pedido de 222 está no V07 (antes da metade); o lembrete no V15. Sem seta para a foto de perfil: o CTA do fim é follow.",
        "7. Sem Voice Changer: a voz vem do prompt de cada V.",
        "8. Música só depois do gancho (a partir do V02), nunca no pré-gancho, entre -19 e -20 dB, fora da biblioteca do TikTok.",
        "9. Rótulo pequeno `AI-generated` num canto do vídeo.",
    ]


def transcricao():
    L = ["| Take | English | Português |", "|---|---|---|"]
    for t in TAKES:
        L.append(f"| {t} | {FALAS[t]} | {PT[t]} |")
    return L


INDICE = [("T1", "K01"), ("T2 a T18", "K02")]


def pacote(a):
    ks, vs = keyframes(a), videos(a)
    up = a["nome"].upper()
    L = [f"# {a['nome']} | Auraly Taylon Branigan (sal na carteira) | Pacote de Prompts", "", "pipeline: auraly", "",
         "Vídeo modelo: `producao/auraly_taylon_branigan/input/taylon_branigan.mp4` (87 s, avatar IA)", "",
         f"Character sheet: `{a['sheet']}`", "",
         "Funil: growth, 222 antes da metade + save + double tap + follow. Rodada de validação, cenário e ângulo do modelo.", "",
         "## Índice de geração", "", "| Take | Keyframe | Anexar | Ação |", "|---|---|---|---|"]
    L += [f"| {t} | {k} | CHARACTER SHEET {up} + FRAME DO MODELO ({k}) | GERAR DO ZERO |" for t, k in INDICE]
    L += ["", "## Trava de identidade e continuidade", "",
          f"- Identidade (character sheet): {a['identidade']}", f"- Roupa (character sheet): {a['roupa']}",
          f"- Cenário do gancho (do vídeo modelo): {CENA_K01}", f"- Cenário do corpo (do vídeo modelo): {CENA_K02}",
          f"- Luz: {LUZ_K01} / {LUZ_K02}",
          f"- Voz (mesmo timbre em todos os V): {a['voz']}, sotaque americano {a['sotaque']}.", "- Sem 2ª pessoa.", "",
          "## Trava do prop herói", "", f"- O saleiro: {SALEIRO}.", f"- A carteira: {CARTEIRA}.", "",
          "## Trava da 2ª pessoa (REF-A)", "", "- Não se aplica: não há 2ª pessoa.", "", "## Prompts de imagem", ""]
    for k in ks:
        L += [f"## {k['codigo']} · {k['take']} · GERAR DO ZERO · CHARACTER SHEET {up} + FRAME DO MODELO", "",
              "> ### 📎 ANEXAR: **2 IMAGENS**", f"> **1️⃣ CHARACTER SHEET {up}** `{a['sheet']}`",
              f"> **2️⃣ FRAME DO MODELO, cenário e ângulo** `input/frames_modelo/{k['codigo']}_modelo.png`", ">",
              "> ### 🆕 GERAR DO ZERO", "", f"Cena: {k['titulo']}.", "", "```json",
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


CHECKLIST = ("Checklist de envio: 32/32 aprovados (N/A: A1, A2, A7, A9 fiéis ao modelo; A10 growth sem produto; C3 a C7 sem "
             "segunda pessoa, selfie, frase curta repetida, cena atuada ou motion control)")
FICHA = "Ficha: 2/2 K conferidos contra o frame do modelo, placar 14/14 cada (`FICHA_FRAMES.md`, GATE_VISUAL Parte 6)"


def entrega(a):
    ks, vs = keyframes(a), videos(a)
    L = [f"# ENTREGA | {a['nome']} | Auraly Taylon Branigan (sal na carteira)", "",
         "Produção `auraly_taylon_branigan` · Ângulo 3 · GROWTH · vídeo modelo de avatar IA · rodada de VALIDAÇÃO · perfil AURALY", "",
         f"## 1. INSTRUÇÕES PARA A MEMÓRIA DO AGENTE · GOOGLE FLOW AI (v{VERSAO})", "",
         "Colar inteiro na memória do agente antes do primeiro K.", "", "```text", BLOCO_FLOW, "```", "",
         CHECKLIST, "", FICHA, "", "## Anexos e mapa", "",
         f"- **Character sheet {a['nome']}:** `{a['sheet']}` no K01 e no K02 (identidade e roupa).",
         "- **Frame do modelo** do mesmo código: `input/frames_modelo/K01_modelo.png` no K01 e `K02_modelo.png` no K02 "
         "(cenário, ângulo e enquadramento).",
         "", "```text"] + mapa_kv() + ["```", "", "## 2. PROMPTS DE IMAGEM", ""]
    for k in ks:
        L += [f"### {k['codigo']} · {k['take']}, {k['titulo']} · anexar CHARACTER SHEET + FRAME DO MODELO", "",
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
