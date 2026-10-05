"""Gera os pacotes por avatar da producao auraly_growth_manifestar_dinheiro (Auraly, growth, dinheiro, avatar IA, validacao).

Fonte unica da fala: ROTEIRO.md aprovado (lido do disco, nunca redigitado). Identidade e roupa: os CHARACTER
SHEETS (producao/_ancoras/character_sheets/, regra so Auraly de 2026-10-04). Cenario e angulo de camera: os do
VIDEO MODELO, quase 100% fieis (banheiro, camera no chao). Medidas: FICHA_FRAMES.md. Prompt de imagem em JSON.
Mapa K/V: K01 -> V01 (gancho mudo com cortes internos), K02 -> V02 a V11 (corpo, plano unico).

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
assert TAKES == ["T%d" % i for i in range(1, 12)], TAKES
FALAS = {}
for bloco in re.split(r"^(?=### T\d+ · )", ROTEIRO, flags=re.M)[1:]:
    m = re.search(r'^> "(.+?)"\s*$', bloco.split("\n## ")[0], re.M)
    if m:
        FALAS[re.match(r"### (T\d+)", bloco).group(1)] = m.group(1)
assert set(FALAS) == set(TAKES) - {"T1"}, FALAS.keys()
PT = dict(re.findall(r"^\| (T\d+) \| .+? \| (.+?) \|$", ROTEIRO.split("## Tradução completa (Português)")[1].split("\n## ")[0], re.M))
assert set(PT) == set(TAKES), PT

MAPA = {"V01": "K01", **{"V%02d" % i: "K02" for i in range(2, 12)}}

FICCAO = "This is a fictional AI-generated character, no real person is depicted."
CENA = ("The ordinary American bathroom of the reference video: white shaker-style vanity cabinets with drawers and a light "
        "speckled countertop on the right side, a stack of folded grey towels on the countertop, a framed botanical print "
        "of a green plant in a thin wooden frame on the cream wall at the left, the vanity mirror with a three-bulb light "
        "fixture above it, and large light grey porcelain floor tiles. On the vanity countertop a small American flag "
        "stands in a drinking glass, discreet but visible and in focus.")
LUZ = ("Neutral overcast daylight coming in from a window just out of frame on the left, cool and even, the vanity lights "
       "switched off, soft even light on the face, hands and feet with no harsh shadows.")
REALISMO = ("Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural "
            "clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday "
            "reality, background fully in focus, everything in sharp focus, no AI polish, no beauty smoothing.")
NEG = ("no captions, no subtitles, no words overlaid on the image, no label on the jar, no studio, no grey studio "
       "background, no plastic-looking human skin, no extra fingers, no extra toes, no third hand, no supernatural "
       "lighting, no blur, no bokeh, no artificial lighting, no warm orange color cast, no yellow tint on the skin, no "
       "golden glow, no golden hour light, no sunset, no de-aging, no beauty smoothing, no visible phone, no HDR, no "
       "cinematic lighting, no second person in frame, no shoes, no socks, no tarot cards, no candles")
POTE = ("a clear glass mason jar filled with coarse white salt, with a handful of dried green bay leaves on top of the "
        "salt, no lid")
CIRCULO = ("a wide ring of coarse white salt poured on the porcelain floor, about two feet across, with a crown of dried "
           "bay leaves laid along it, the bay leaves burning with small low flames all around the ring and the empty "
           "grey tile showing in the middle")

AVATARES = [
    dict(nome="Avery Knox", arquivo="AVERY_KNOX", genero="mulher", pos="her",
         sheet="producao/_ancoras/character_sheets/avery_knox_character_sheet.jpg",
         identidade=("The exact fictional AI character Avery Knox: white American woman around fifty-six, voluminous shaggy "
                     "layered platinum-blonde hair with visible darker roots, brown eyes, fair skin with crow's feet and "
                     "fine lines, everyday makeup with defined brows, mascara and pink lipstick."),
         roupa=("White long-sleeve button-up shirt with a chest pocket and the cuffs rolled, medium-blue bootcut jeans, "
                "barefoot, a large turquoise and silver squash-blossom necklace, several big turquoise rings and silver "
                "cuff bracelets set with turquoise on both wrists."),
         maos="her fair hands with big turquoise rings",
         sotaque="texano carregado",
         voz="voz feminina média, levemente rouca e calorosa de uma texana de cinquenta e seis anos"),
    dict(nome="Devon Price", arquivo="DEVON_PRICE", genero="mulher", pos="her",
         sheet="producao/_ancoras/character_sheets/devon_price_character_sheet.jpg",
         identidade=("The exact fictional AI character Devon Price: white American woman around fifty-two, closely shaved "
                     "head with grey stubble, freckles and sunspots on her face and scalp, light grey-green eyes, defined "
                     "jaw, fine lines and no makeup."),
         roupa=("Light-wash denim shirt worn open with the cuffs rolled over a fitted black crew-neck T-shirt, dark blue "
                "jeans, barefoot, large silver hoop earrings, a thin silver chain necklace and black-framed reading "
                "glasses hanging from the T-shirt collar."),
         maos="her freckled fair hands with bare fingers",
         sotaque="de Chicago",
         voz="voz feminina grave, direta e de humor seco de uma mulher de cinquenta e dois anos de Chicago"),
    dict(nome="Jordan Vale", arquivo="JORDAN_VALE", genero="homem", pos="his",
         sheet="producao/_ancoras/character_sheets/jordan_vale_character_sheet.jpg",
         identidade=("The exact fictional AI character Jordan Vale, explicitly male: white American man around fifty-eight, "
                     "long grey-white beard down to mid-chest, grey moustache, grey hair combed back short on the sides, "
                     "sun-weathered skin with freckles and deep crow's feet, light grey eyes, both forearms covered in faded "
                     "traditional American tattoos with no lettering, a swallow and a red rose on the left forearm."),
         roupa="Black leather vest over a heather grey crew-neck T-shirt, dark blue straight jeans, barefoot.",
         maos="his weathered hands with faded tattoos on the forearms",
         sotaque="do Tennessee",
         voz="voz masculina grave, devagar e gentil de um homem de cinquenta e oito anos do Tennessee"),
    dict(nome="Morgan Vance", arquivo="MORGAN_VANCE", genero="mulher", pos="her",
         sheet="producao/_ancoras/character_sheets/morgan_vance_character_sheet.jpg",
         identidade=("The exact fictional AI character Morgan Vance: Black American woman around twenty-five, long knotless "
                     "box braids down to the waist with a middle part and a few small gold cuffs in the braids, neat baby "
                     "hairs, dark brown skin with real texture, visible pores and acne marks on the forehead and cheeks, "
                     "dark brown eyes, long lashes, defined brows, glossy lips, a small gold hoop in her nostril and small "
                     "gold earrings."),
         roupa=("Cobalt blue ribbed long-sleeve top with a scoop neckline, a thin gold chain necklace with a small gold "
                "heart pendant, medium-blue bootcut jeans, barefoot."),
         maos="her dark brown hands with short natural nails",
         sotaque="leve de Atlanta",
         voz="voz feminina média e jovem, confiante e direta, de uma mulher de vinte e cinco anos de Atlanta"),
]

EMOCAO = {
    "T2": "séria e intrigante", "T3": "convicta e intensa", "T4": "urgente e direta", "T5": "aliviada e firme",
    "T6": "séria, em tom de aviso", "T7": "intensa e solene", "T8": "rápida e prática", "T9": "firme e confiante",
    "T10": "séria e baixa", "T11": "próxima e urgente",
}
MASC = {"séria": "sério", "convicta": "convicto", "intensa": "intenso", "direta": "direto", "aliviada": "aliviado",
        "rápida": "rápido", "prática": "prático", "baixa": "baixo", "próxima": "próximo"}
ACAO = {
    "T5": "{n} abre a mão livre para a lente, aliviada, com a outra mão apoiada no chão.",
    "T8": "{n} toca o ar duas vezes com o dedo indicador, como quem toca a tela, com a outra mão apoiada no chão.",
    "T9": "{n} aponta para baixo, para os comentários, e depois para a lente.",
    "T10": "{n} fala devagar, com o dedo indicador erguido, a outra mão apoiada no chão.",
    "T11": "{n} se inclina um pouco para a lente e aponta para ela.",
}
ACAO_PADRAO = "{n} aponta para a lente com uma mão, com a outra apoiada no chão, e fala com pequenos gestos naturais."
TITULOS = {"K01": "gancho mudo, pote de sal e louro colado na lente, câmera no chão do banheiro",
           "K02": "corpo, ajoelhada atrás do círculo de sal e louro em chamas, câmera no chão"}

CAMERA = "phone resting on the bathroom floor, lens at floor level about three feet away, 1x lens, pointing slightly upward, fixed"


def keyframes(a):
    n, p = a["nome"], a["pos"]
    ref = (f"Use the first attached image (character sheet) only for {n}'s exact identity (face, skin, hair, body) and "
           f"wardrobe; ignore its grey studio background. Use the second attached image (frame of the model video) as the "
           f"reference for the setting, camera angle and framing; do not copy its person, clothes or on-screen text.")
    quadro = (f"{n} is framed from the top of the head down to the knees, {p} face in the upper third. Nothing else is in "
              f"the foreground. The background is reduced by framing, never by blur.")
    k01 = {
        "prop": (f"The only object is {POTE}, held out in one of {a['maos']} toward the lens; the other hand rests on "
                 f"{p} thigh. The floor in front of {n} is still empty and clean."),
        "posture": (f"{n} kneels on the bathroom floor sitting back on {p} heels, facing the lens, holding the jar out "
                    f"toward the phone, smiling softly and looking down at the lens, mouth closed."),
        "composition": (f"The glass jar of salt and bay leaves is in the lower right of the frame, very close to the lens, "
                        f"about 14 inches from the lens, taking up about 20 percent of the frame, closer to the camera than "
                        f"{p} face, nothing else competing with it. " + quadro),
        "state": f"Start frame: {n} holds the full jar still, about to tip it toward the floor, mouth closed.",
        "negative": NEG + ", no fire, no flames, no smoke, no salt on the floor yet",
    }
    k02 = {
        "prop": (f"In the lower part of the frame, right in front of the lens, lies {CIRCULO}. One of {a['maos']} rests "
                 f"flat on the floor beside the ring; the other hand points at the lens."),
        "posture": (f"{n} kneels on the bathroom floor right behind the burning ring, leaning slightly toward the lens, "
                    f"one hand flat on the tiles, the other hand pointing at the lens, looking straight into the lens."),
        "composition": (f"The burning ring of salt and bay leaves fills the bottom quarter of the frame, about 25 percent "
                        f"of the frame, touching the bottom edge, its near edge about 10 inches from the lens, closer to the "
                        f"camera than {p} face, nothing else competing with it. " + quadro),
        "state": f"Start frame: {n} points at the lens, caught mid-sentence, lips naturally parted, serious expression.",
        "negative": NEG + ", no smoke cloud, no tall flames, no fire on the person",
    }
    out = []
    for cod, d, take in (("K01", k01, "T1"), ("K02", k02, "T2 a T11")):
        j = {"shot_id": f"{cod}_{a['arquivo'].lower()}", "fiction_note": FICCAO, "reference_use": ref,
             "identity_main": a["identidade"], "wardrobe": a["roupa"], "scene": CENA, "prop": d["prop"],
             "posture": d["posture"], "composition": d["composition"], "camera": CAMERA, "lighting": LUZ,
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
            txt = (f"(sem fala no take: gancho mudo, {art} fica em silêncio o clipe inteiro, boca fechada)\n\n"
                   f"o que acontece no vídeo: plano 1, {n} ajoelhada no chão do banheiro inclina o pote de vidro e despeja "
                   f"o sal grosso com as folhas de louro em um círculo no chão, bem na frente da lente; corte seco para o "
                   f"plano 2, {n} agachada atrás do círculo pronto acende um isqueiro na borda e o círculo inteiro pega fogo; "
                   f"corte seco para o plano 3, {n} de pé pisa descalça dentro do círculo em chamas, sobe uma nuvem de "
                   f"fumaça branca, {n} se ajoelha dentro da fumaça com as duas mãos abertas para a lente e a fumaça cobre "
                   f"a câmera.\n\n"
                   "câmera: fixa no chão, olhando levemente para cima, com dois cortes secos internos ao clipe, sem movimento\n\n"
                   "som ambiente: banheiro silencioso, o sal caindo no piso, o clique do isqueiro e o fogo estalando, sem música")
            if h:
                txt = txt.replace("ajoelhada", "ajoelhado").replace("agachada", "agachado")
        else:
            txt = (f"{art} {n}, {a['genero']}, fala em inglês com sotaque americano {a['sotaque']}, {a['voz']}, "
                   f"{emocao(t, h)}, voz autêntica, como se exigisse ser {ouvido}, a seguinte frase: \"{FALAS[t]}\"\n\n"
                   f"{art} diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro "
                   f"sem cortar no final. Lip sync perfeito durante todo o vídeo.\n\n"
                   f"o que acontece no vídeo: {ACAO.get(t, ACAO_PADRAO).format(n=n)} As chamas baixas do círculo de sal à "
                   f"frente continuam queimando.\n\n"
                   "câmera: fixa no chão, olhando levemente para cima, sem movimento\n\n"
                   "som ambiente: banheiro silencioso, o fogo estalando baixinho, sem música")
            if h:
                txt = txt.replace("aliviada", "aliviado")
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
        "1. Clipes numerados na ordem: V01 a V11.",
        "2. V01 (gancho mudo): usar ~6 s, até a fumaça cobrir a lente, que é a transição para o V02. Texto branco no topo: "
        "\"When you urgently need unexpected money!\".",
        "3. V02 a V11: zero tempo morto, todo clipe começa já falando; cortar logo depois da última palavra. Isolate Voice / "
        "Keep Vocal. Todos saem do mesmo frame (K02), então a troca de clipe fica no mesmo enquadramento, como no modelo. "
        "V04 termina na vírgula e o V05 continua a frase: juntar sem pausa.",
        "4. Do V02 ao V11, \"11:11 ✨\" no canto superior esquerdo e legenda branca da fala no meio do quadro.",
        "5. Sem seta para a foto de perfil: o CTA é follow.",
        "6. Sem Voice Changer: a voz vem do prompt de cada V.",
        "7. Música no V01 (o modelo abre com música) e baixa por baixo da fala a partir do V02, entre -19 e -20 dB, fora "
        "da biblioteca do TikTok.",
        "8. Rótulo pequeno `AI-generated` num canto do vídeo.",
    ]


def transcricao():
    L = ["| Take | English | Português |", "|---|---|---|"]
    for t in TAKES:
        L.append(f"| {t} | {FALAS.get(t, '(sem fala)')} | {PT[t]} |")
    return L


INDICE = [("T1", "K01"), ("T2 a T11", "K02")]


def pacote(a):
    ks, vs = keyframes(a), videos(a)
    up = a["nome"].upper()
    L = [f"# {a['nome']} | Auraly Growth Manifestar Dinheiro | Pacote de Prompts", "", "pipeline: auraly", "",
         "Vídeo modelo: `producao/auraly_growth_manifestar_dinheiro/input/modelo.mp4` (69,8 s, avatar IA)", "",
         f"Character sheet: `{a['sheet']}`", "",
         "Funil: growth, save + double tap + `222` + follow. Rodada de validação, cenário e ângulo do modelo.", "",
         "## Índice de geração", "", "| Take | Keyframe | Anexar | Ação |", "|---|---|---|---|"]
    L += [f"| {t} | {k} | CHARACTER SHEET {up} + FRAME DO MODELO ({k}) | GERAR DO ZERO |" for t, k in INDICE]
    L += ["", "## Trava de identidade e continuidade", "",
          f"- Identidade (character sheet): {a['identidade']}", f"- Roupa (character sheet, descalço pela ação do modelo): {a['roupa']}",
          f"- Cenário (do vídeo modelo): {CENA}", f"- Luz: {LUZ}",
          f"- Voz (mesmo timbre em todos os V): {a['voz']}, sotaque americano {a['sotaque']}.", "- Sem 2ª pessoa.", "",
          "## Trava do prop herói", "", f"- O pote: {POTE}.", f"- O círculo: {CIRCULO}.", "",
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


CHECKLIST = ("Checklist de envio: 32/32 aprovados (N/A: A1, A2, A7, A9 fiéis ao modelo, gancho mudo; A10 growth sem "
             "produto; C3 a C7 sem segunda pessoa, selfie, frase curta repetida, cena atuada ou motion control)")
FICHA = "Ficha: 2/2 K conferidos contra o frame do modelo, placar 14/14 cada (`FICHA_FRAMES.md`, GATE_VISUAL Parte 6)"


def entrega(a):
    ks, vs = keyframes(a), videos(a)
    L = [f"# ENTREGA | {a['nome']} | Auraly Growth Manifestar Dinheiro", "",
         "Produção `auraly_growth_manifestar_dinheiro` · Ângulo 3 · GROWTH · vídeo modelo de avatar IA · rodada de VALIDAÇÃO · perfil AURALY", "",
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
        L.append(f"{i}. {FALAS.get(t, '(sem fala: gancho mudo)')}")
    L += ["", " ".join(FALAS[t] for t in TAKES if t in FALAS), ""]
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
