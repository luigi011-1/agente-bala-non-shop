"""Gera os pacotes por avatar da producao fitywell_growth_canela_acucar.

Fonte unica da fala: ROTEIRO.md aprovado (lido do disco, nunca redigitado).
Saidas: PROMPTS_<AVATAR>.md (fonte interna com JSON), FLOW_<AVATAR>.md (blocos limpos do Flow)
e PROMPTS_PRODUCAO.md (copia do avatar ACTIVE, que e o que o checar_entrega.py le).

Uso: python3 gerar_pacote.py [NOME_DO_ATIVO]   (padrao: o ACTIVE do AVATAR_QUEUE.md)
"""
import json
import re
import sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
ROTEIRO = (AQUI / "ROTEIRO.md").read_text(encoding="utf-8")

FALAS = {}
for m in re.finditer(r'^### (T\d+) · .*?\n\n> "(.+?)"\s*$', ROTEIRO, re.M | re.S):
    FALAS[m.group(1)] = m.group(2)
assert len(FALAS) == 6, FALAS

FICCAO = "This is a fictional AI-generated character, no real person is depicted."
FRAME_MODELO = "input/primeiro_frame_modelo.png"

LUZ_INTERNA = ("Neutral overcast daylight from a window, the outside clearly visible through the window, "
               "soft even light on the face with no harsh shadows.")
LUZ_EXTERNA = ("Overcast sky with visible cloud texture, never white or blown out, neutral daylight, "
               "soft even light on the face with no harsh shadows.")
LUZ_GARAGEM = ("Neutral overcast daylight coming in through the open garage door, the outside clearly visible, "
               "soft even light on the face with no harsh shadows.")

REALISMO = ("Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural "
            "clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday "
            "reality, background fully in focus, everything in sharp focus, no AI polish, no beauty smoothing.")

NEG_BASE = ("no captions, no subtitles, no words overlaid on the image, no studio, no plastic-looking human skin, no extra fingers, "
            "no supernatural lighting, no blur, no bokeh, no artificial lighting, no warm orange color cast, "
            "no yellow tint, no golden glow, no golden hour light, no sunset, no de-aging, no beauty smoothing, "
            "no visible phone, no HDR, no cinematic lighting")
NEG_SHEET = ", no character sheet layout, no grid, no multiple panels, no grey studio backdrop"
NEG_HOOK = (", no real human body, no thin scattered sugar layer, no flat sauce-like coating, "
            "no loose white granulated sugar")

# Traços aprovados (fitywell_growth_cortisol_cintura e fichas), sem as luvas daquele video.
AVATARES = [
    dict(nome="Dana Morrison", arquivo="DANA_MORRISON", genero="homem", pron="He", pos="his",
         ancora="input/ancoras/01_dana_morrison.jpg", sheet=False,
         identidade="The exact fictional AI character Dana Morrison: Black American man in his early fifties, deep brown skin, lean angular face, high cheekbones, dark brown eyes, black satin do-rag tied tight with its tail behind his left shoulder, full salt-and-pepper beard that turns grey-white at the chin, darker grey-flecked moustache, real pores and deep forehead lines, broad trained shoulders and veined forearms with faded grey-ink tattoos of a rose and praying hands.",
         roupa="Open short-sleeve charcoal work shirt over a black ribbed tank top, a gold rope chain layered with a thin gold chain, dark old-school sunglasses hanging from the tank neckline, a gold watch on his left wrist and a gold pinky ring.",
         cena_hook="The same lived-in garage as the reference image: the black office chair with the mannequin stands beside his scuffed wooden workbench, with the black 1960s lowrider sedan with chrome wire wheels, the worn red boxing gloves hanging under a wooden shelf that holds a small American flag, and the open garage door behind them.",
         cena_corpo="The same lived-in garage as the reference image: a scuffed wooden workbench in front of him; behind him the black 1960s lowrider sedan with chrome wire wheels, the worn red boxing gloves hanging under a wooden shelf with a row of glass jars and a small American flag, and the open garage door showing the driveway and a residential street.",
         superficie="the scuffed wooden workbench", postura="standing behind the scuffed wooden workbench, leaning in with his forearms resting on its edge",
         luz=LUZ_GARAGEM, sotaque="de um homem negro americano",
         voz="voz grave e levemente rouca de um homem de cinquenta e poucos anos", som="garagem tranquila"),
    dict(nome="Eva Dall", arquivo="EVA_DALL", genero="homem", pron="He", pos="his",
         ancora="input/ancoras/02_eva_dall.jpg", sheet=False,
         identidade="The exact fictional AI character Eva Dall, explicitly male: Black American man around forty-nine, medium brown skin, lean athletic build, long oval face, dark brown eyes, subtle freckles and moles, very long locs mixing black, grey and silver, grey goatee and moustache, brown leather cap worn backward.",
         roupa="White ribbed tank top and a thin silver chain.",
         cena_hook="His own modern white kitchen: the black office chair with the mannequin stands beside his dark green veined marble counter, with tall windows and a small plant beside a small American flag behind them.",
         cena_corpo="His own modern white kitchen with a strongly veined dark green marble counter in front of him, tall windows to the right and a small American flag on the shelf beside a small plant.",
         superficie="the dark green veined marble counter", postura="standing behind his counter, both forearms near the counter, leaning slightly toward the camera",
         luz=LUZ_INTERNA, sotaque="de um homem negro americano",
         voz="voz média e amigável de um homem de quase cinquenta anos", som="cozinha residencial tranquila"),
    dict(nome="Ivy Carl", arquivo="IVY_CARL", genero="homem", pron="He", pos="his",
         ancora="input/ancoras/03_ivy_carl.jpg", sheet=False,
         identidade="The exact fictional AI character Ivy Carl, explicitly male: Black American man around twenty-eight, dark brown skin, lean athletic build, long oval face, very light grey-hazel eyes, fine black braids beneath a plain black cap and a short goatee.",
         roupa="Plain black cap, fitted black long-sleeve athletic shirt, black trousers and small silver stud earrings.",
         cena_hook="His own covered American backyard veranda: the black office chair with the mannequin stands beside his weathered wooden table, with beige walls, a black-framed glass door holding a small American flag and a glimpse of turquoise pool behind them.",
         cena_corpo="His own covered American backyard veranda with a weathered wooden table in front of him, beige walls, a black-framed glass door with a small American flag and a glimpse of turquoise pool at the right.",
         superficie="the weathered wooden table", postura="leaning on the wooden table toward the camera",
         luz=LUZ_EXTERNA, sotaque="de um homem negro americano",
         voz="voz clara e jovem de um homem no fim dos vinte anos", som="varanda tranquila ao ar livre"),
    dict(nome="Jamie Anderson", arquivo="JAMIE_ANDERSON", genero="homem", pron="He", pos="his",
         ancora="input/ancoras/04_jamie_anderson.jpg", sheet=False,
         identidade="The exact fictional AI character Jamie Anderson, a beekeeper who grows his own food on his small family farm: Black American man in his mid-fifties, medium brown skin, short low-cut hair heavily grey at the temples and top, short full grey-white beard and grey moustache, high forehead, visible freckles and moles on his cheeks, dark brown eyes, lean athletic build, veined forearms and natural age lines.",
         roupa="A worn white zip-front beekeeping jacket with faint work stains, the mesh veil hood lowered behind his head and shoulders, the sleeves pushed up to the forearms, and a pair of reading glasses hooked in the chest pocket.",
         cena_hook="His own small family farm under an overcast sky: the black office chair with the mannequin stands on the grass beside his weathered grey wooden picnic table, with white wooden beehive boxes on the grass, a weathered red barn with a small American flag on its wall, and a small roadside stand with shelves of glass jars of honey behind them.",
         cena_corpo="His own small family farm under an overcast sky: a weathered grey wooden picnic table in front of him; behind him white wooden beehive boxes on the grass, a weathered red barn with a small American flag on its wall at the left, and a small roadside stand with shelves of glass jars of honey at the right, green fields beyond.",
         superficie="the weathered grey wooden picnic table", postura="standing behind the weathered wooden picnic table, leaning in with his forearms resting on its edge",
         luz=LUZ_EXTERNA, sotaque="de um homem negro americano",
         voz="voz média, calma e calorosa de um homem de cinquenta e cinco anos que fala com certeza", som="fazenda tranquila ao ar livre, pássaros ao longe"),
    dict(nome="Jamie Voss", arquivo="JAMIE_VOSS", genero="homem", pron="He", pos="his",
         ancora="input/ancoras/05_jamie_voss.jpg", sheet=False,
         identidade="The exact fictional AI character Jamie Voss, explicitly male: white American man around forty-six, fair skin, solid athletic build, blue-grey eyes, short brown hair under a beige cap worn backward, full brown beard with substantial grey and real forehead lines.",
         roupa="Beige cap backward, navy long-sleeve henley and jeans.",
         cena_hook="His own bright residential kitchen: the black office chair with the mannequin stands beside his white-veined stone counter, with cream upper cabinets and a black-framed window holding a small American flag behind them. The counter top is clear, with nothing else on it.",
         cena_corpo="His own bright residential kitchen with a white-veined stone counter in front of him, cream upper cabinets and a black-framed window with a small American flag. The counter top is clear, with nothing on it except what he is using.",
         superficie="the white-veined stone counter", postura="leaning on the counter with his forearms, toward the camera",
         luz=LUZ_INTERNA, sotaque="de um homem branco americano",
         voz="voz grave e firme de um homem de quarenta e poucos anos", som="cozinha residencial tranquila"),
    dict(nome="Lais Collins", arquivo="LAIS_COLLINS", genero="homem", pron="He", pos="his",
         ancora="input/ancoras/06_lais_collins.jpg", sheet=False,
         identidade="The exact fictional AI character Lais Collins, explicitly male: Black and mixed-race American man around thirty-two, light brown skin, highly athletic build, light grey-green eyes, short black locs, short beard and botanical line tattoos across chest, shoulders and arms.",
         roupa="Shirtless, black athletic shorts, a thin gold chain and small silver stud earrings.",
         cena_hook="His own bright contemporary apartment: the black office chair with the mannequin stands beside his white kitchen island, with floor-to-ceiling windows and a shelf of green plants holding a small American flag behind them.",
         cena_corpo="His own bright contemporary apartment with a white kitchen island in front of him, floor-to-ceiling windows and a shelf of green plants with a small American flag.",
         superficie="the white kitchen island", postura="seated on a stool at the island, leaning slightly toward the camera",
         luz=LUZ_INTERNA, sotaque="de um homem negro americano",
         voz="voz média e energética de um homem de trinta e poucos anos", som="apartamento moderno tranquilo"),
    dict(nome="Lynn Parker", arquivo="LYNN_PARKER", genero="homem", pron="He", pos="his",
         ancora="input/ancoras/07_lynn_parker.jpg", sheet=False,
         identidade="The exact fictional AI character Lynn Parker, a Black American Zen monk who lived for decades in a Japanese mountain temple: Black American man around seventy, medium brown skin, long dignified face, white hair on top with a high hairline, long silver-white locs falling loose over his chest, full neat white beard and moustache, grey brows, visible moles on his cheeks, calm dark brown eyes, deep natural age lines and a lean upright build.",
         roupa="A charcoal-grey samue, the plain cotton work clothes of a Zen monk, with a wrap-front top tied at the side and the sleeves pushed up to the forearms, a dark brown rakusu, the small square cloth panel of an ordained Zen monk, hung on a thin cord at the center of his chest, and a dark wooden bead bracelet on his left wrist.",
         cena_hook="His own Japanese-style Zen tea garden in America under an overcast sky: the black office chair with the mannequin stands on the mossy stone path beside his light wooden table, with the small wooden tea house with a dark tiled roof, a small American flag by its door and strings of dried persimmons hanging from its eave, two cherry trees in pink bloom, and a row of large brown glazed fermentation crocks with wooden lids and stones on top behind them.",
         cena_corpo="His own Japanese-style Zen tea garden in America under an overcast sky: a light wooden table in front of him; behind him the small wooden tea house with a dark tiled roof, a small American flag by its door and strings of dried persimmons hanging from its eave, two cherry trees in pink bloom arching over the scene, and a row of large brown glazed fermentation crocks with wooden lids and stones on top at the left, on a mossy stone path.",
         superficie="the light wooden table", postura="standing behind the light wooden table, leaning slightly toward the camera with his hands resting on its edge",
         luz=LUZ_EXTERNA, sotaque="de um homem negro americano idoso",
         voz="voz grave, pausada, serena e um pouco envelhecida de um homem de setenta anos", som="jardim zen tranquilo ao ar livre, pássaros ao longe"),
    dict(nome="Robert Alves", arquivo="ROBERT_ALVES", genero="homem", pron="He", pos="his",
         ancora="input/ancoras/08_robert_alves.jpg", sheet=False,
         identidade="The exact fictional AI character Robert Alves: Black American man around forty-three, medium brown skin, lean healthy build, oval face, green-hazel eyes, black jaw-length locs, short full black beard and thin round tortoiseshell glasses.",
         roupa="Plain black polo shirt and black trousers.",
         cena_hook="His own American timber cabin kitchen: the black office chair with the mannequin stands beside his light butcher-block counter, with pine walls, large windows showing pine forest and a small American flag on a shelf behind them.",
         cena_corpo="His own American timber cabin kitchen with a light butcher-block counter in front of him, pine walls, large windows showing pine forest and a small American flag on a shelf.",
         superficie="the light butcher-block counter", postura="standing behind the counter, leaning slightly toward the camera",
         luz=LUZ_INTERNA, sotaque="de um homem negro americano",
         voz="voz média e calma de um homem de quarenta e poucos anos", som="cozinha de cabana tranquila"),
    dict(nome="Roberta Carvalho", arquivo="ROBERTA_CARVALHO", genero="mulher", pron="She", pos="her",
         ancora="input/ancoras/09_roberta_carvalho.jpg", sheet=False,
         identidade="The exact fictional AI character Roberta Carvalho: white American woman around forty-nine, lightly tanned fair skin, lean healthy build, oval face, blue-grey eyes, long medium-brown layered hair with soft waves, natural fine lines and discreet makeup.",
         roupa="Fitted navy T-shirt, two thin gold chains with a small circular pendant and small gold hoop earrings.",
         cena_hook="Her own residential kitchen: the black office chair with the mannequin stands beside her light stone counter, with dark wood cabinets and a broad window to a green garden, and a small American flag on the open shelf behind them. The counter top is clear, with nothing else on it.",
         cena_corpo="Her own residential kitchen with a light stone counter in front of her, dark wood cabinets, a broad window showing a green garden and a small American flag on the open shelf. The counter top is clear, with nothing on it except what she is using.",
         superficie="the light stone counter", postura="standing behind the counter, both hands near the counter, leaning slightly toward the camera",
         luz=LUZ_INTERNA, sotaque="de uma mulher branca americana",
         voz="voz feminina média e calorosa de uma mulher de quase cinquenta anos", som="cozinha residencial tranquila"),
]

EMOCAO = {
    "T1": "entonação animada e intrigada, sorrindo, como quem mostra algo surpreendente",
    "T2": "entonação animada e didática, sorrindo",
    "T3": "entonação animada e didática",
    "T4": "entonação animada e didática, sorrindo",
    "T5": "entonação confiante e calorosa",
    "T6": "entonação animada e convidativa",
}


def keyframes(a):
    n, P, p = a["nome"], a["pron"], a["pos"]
    if a["sheet"]:
        ref = (f"Use the attached character sheet only for {n}'s exact face, hair, beard, skin and body. "
               "Ignore its grey studio background, its panel layout and its labels. Do not copy any pose.")
    else:
        ref = f"Use the attached image only for {n}'s exact identity, wardrobe and own setting. Do not copy its pose or framing."
    neg = NEG_BASE + (NEG_SHEET if a["sheet"] else "")
    boca = "caught mid-sentence, lips naturally parted, animated expression"
    ks = []
    ks.append(dict(
        codigo="K01", take="T1", titulo="gancho, a montanha de açúcar", anexos=2,
        j={
            "shot_id": f"K01_gancho_{a['arquivo'].lower()}",
            "reference_use": ref + " Use the second attached image only as a composition reference for where the seated mannequin, the sugar mound and the spice jar sit in the frame; do not copy its man, his clothes, cap, room or colors.",
            "fiction_note": FICCAO,
            "identity_main": a["identidade"],
            "wardrobe": a["roupa"],
            "scene": a["cena_hook"],
            "prop": ("A featureless female store mannequin of smooth matte plastic sits reclined in a black office chair, wearing a grey heather T-shirt pulled up to just under the chest and beige chinos. "
                     "Covering its entire bare plastic belly is a THICK, TALL, HEAPED DOME of light brown raw cane sugar cubes, hundreds of small square lumps piled high with real 3D volume, so much that almost no plastic is visible under it. "
                     f"{n} holds a clear spice jar of ground cinnamon with a bright orange flip-top lid and no label, tilted over the top of the sugar dome, and a thin stream of cinnamon is starting to fall onto it."),
            "posture": f"{n} stands just behind and to the right of the mannequin, leaning in over the sugar dome with the jar.",
            "composition": f"The heaped sugar dome fills the lower third of the frame, very close to the lens, much closer to the camera than {n}'s face. {P} is clear in the upper half. The mannequin's head and shoulders are cut off by the left edge of the frame. Nothing else competes with the sugar dome.",
            "camera": "phone camera at the height of the mannequin's belly, very close to the sugar dome, slight upward angle",
            "state": f"Start frame: the first thin stream of cinnamon is just falling on top of the full, intact sugar dome. {n} is {boca}.",
            "lighting": a["luz"],
            "realism": REALISMO,
            "aspect_ratio": "9:16 vertical",
            "negative": neg + NEG_HOOK,
        }))
    corpo = [
        ("K02", "T2", "colher de canela sobre o copo d'água",
         f"A clear straight drinking glass of plain water stands on {a['superficie']} in the lower foreground, very close to the lens, larger in frame than {p} hands. {n} holds a metal teaspoon heaped with ground cinnamon toward the camera, just above the glass.",
         f"Start frame: {n} shows the heaped spoon of cinnamon to the camera, {boca}."),
        ("K03", "T3", "limão espremido no copo",
         f"A clear straight drinking glass of cloudy light brown cinnamon water stands on {a['superficie']} in the lower foreground, very close to the lens. {n} holds half a fresh yellow lemon in one hand right above the glass, squeezing it.",
         f"Start frame: the first drops of lemon juice are falling into the glass, {n} is {boca}."),
        ("K04", "T4", "fio de mel no copo",
         f"A clear straight drinking glass of cloudy amber drink stands on {a['superficie']} in the lower foreground, very close to the lens. {n} holds a metal tablespoon of thick amber raw honey right above the glass.",
         f"Start frame: a thick thread of honey is starting to fall from the spoon into the glass, {n} is {boca}."),
        ("K05", "T5", "segurando o copo pronto",
         f"{n} holds the clear straight drinking glass of cloudy amber-brown drink with both hands at chest height, very close to the lens, the glass in the lower foreground.",
         f"Start frame: {n} looks into the lens holding the glass, {boca}."),
        ("K06", "T6", "segurando o copo, plano mais fechado",
         f"{n} holds the clear straight drinking glass of cloudy amber-brown drink with both hands at chest height, very close to the lens, the glass in the lower foreground.",
         f"Start frame: {n} leans a little toward the lens holding the glass, {boca}."),
    ]
    for cod, take, titulo, prop, estado in corpo:
        mais_perto = cod == "K06"
        ks.append(dict(
            codigo=cod, take=take, titulo=titulo, anexos=1,
            j={
                "shot_id": f"{cod}_{take.lower()}_{a['arquivo'].lower()}",
                "reference_use": ref,
                "fiction_note": FICCAO,
                "identity_main": a["identidade"],
                "wardrobe": a["roupa"],
                "scene": a["cena_corpo"],
                "prop": prop,
                "posture": f"{n} is {a['postura']}.",
                "composition": (f"{'Tightest shot of the video: from the upper chest up' if mais_perto else 'From the chest up'}, "
                                f"{n}'s face clear in the upper half, the glass in the lower foreground closer to the camera than {p} face. "
                                "The background is reduced by framing, never by blur."),
                "camera": "phone camera at chest height, straight on, fixed",
                "state": estado,
                "lighting": a["luz"],
                "realism": REALISMO,
                "aspect_ratio": "9:16 vertical",
                "negative": neg + ", no mannequin in frame, no second person in frame",
            }))
    return ks


ACOES = {
    "T1": "{n} inclina o pote e a canela cai em fio sobre a montanha de cubos de açúcar; perto do fim da frase a montanha inteira desaba para os lados e os cubos rolam para fora da barriga do manequim, revelando a barriga lisa de plástico polvilhada de canela; {pr} olha o resultado e sorri.",
    "T2": "{n} mostra a colher cheia de canela para a câmera e depois mexe a canela dentro do copo d'água. {Pr} diz a frase em ritmo natural logo no começo e continua mexendo em silêncio até o fim.",
    "T3": "{n} espreme o meio limão e o suco cai dentro do copo. {Pr} diz a frase em ritmo natural logo no começo e continua espremendo em silêncio até o fim.",
    "T4": "o fio grosso de mel escorre da colher para dentro do copo. {n} diz a frase em ritmo natural logo no começo e continua despejando o mel em silêncio até o fim.",
    "T5": "{n} segura o copo com as duas mãos na altura do peito e fala para a câmera, com pequenos movimentos naturais.",
    "T6": "{n} segura o copo com as duas mãos, se inclina um pouco para a câmera e fala direto com ela, sorrindo no fim.",
}
CAMERA = {"T1": "fixa, leve handheld", "T2": "fixa", "T3": "fixa", "T4": "fixa", "T5": "fixa", "T6": "fixa"}
SOM_EXTRA = {"T1": ", som dos cubos de açúcar caindo"}


def videos(a):
    n = a["nome"]
    art = "o avatar" if a["genero"] == "homem" else "a avatar"
    vs = []
    for i, take in enumerate(["T1", "T2", "T3", "T4", "T5", "T6"], 1):
        pr = "ele" if a["genero"] == "homem" else "ela"
        acao = ACOES[take].format(n=n, pr=pr, Pr=pr.capitalize())
        ouvido = "ouvido" if a["genero"] == "homem" else "ouvida"
        txt = (f"{art} {n}, {a['genero']}, fala em inglês com sotaque americano {a['sotaque']}, {a['voz']}, "
               f"{EMOCAO[take]}, voz autêntica, como se exigisse ser {ouvido}, a seguinte frase: \"{FALAS[take]}\"\n\n"
               f"{art} diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.\n\n"
               f"o que acontece no vídeo: {acao}\n\n"
               f"câmera: {CAMERA[take]}\n\n"
               f"som ambiente: {a['som']}{SOM_EXTRA.get(take, '')}, sem música")
        vs.append((f"V{i:02d}", take, f"K{i:02d}", txt))
    return vs


def texto_flow(j):
    partes = ["IMPORTANT: THIS IS IPHONE FOOTAGE. Vertical 9:16.", j["fiction_note"], j["reference_use"],
              j["identity_main"], j["wardrobe"], j["scene"], j["prop"], j["posture"], j["composition"],
              j["camera"][0].upper() + j["camera"][1:] + ".", j["lighting"], j["state"], j["realism"],
              j["negative"] + "."]
    return " ".join(partes)


def anexo(a, k):
    linhas = [f"> ### 📎 ANEXAR: **{k['anexos']} {'IMAGENS' if k['anexos'] > 1 else 'IMAGEM'}**",
              f"> **1️⃣ ÂNCORA {a['nome'].upper()}** `{a['ancora']}`"]
    if k["anexos"] > 1:
        linhas.append(f"> **2️⃣ FRAME DO MODELO, só composição** `{FRAME_MODELO}`")
    linhas += [">", "> ### 🆕 GERAR DO ZERO"]
    return "\n".join(linhas)


TRANSCRICAO_PT = {
    "T1": "Isso é o que a canela faz com o açúcar no seu corpo.",
    "T2": "Num copo, misture uma colher de chá de canela,",
    "T3": "um pouco de suco de limão fresco,",
    "T4": "e uma colher de sopa de mel cru.",
    "T5": "Beba isso toda manhã em jejum e a sua energia começa a voltar e as suas roupas começam a servir melhor.",
    "T6": "E comente yes, que eu te mando mais um ingrediente que deixa isso dez vezes mais poderoso. E me siga para eu conseguir te alcançar.",
}
CORTE = {"T1": "0,0 a 4,0 s", "T2": "4,0 a 7,8 s", "T3": "7,8 a 10,1 s", "T4": "10,1 a 12,6 s",
         "T5": "12,6 a 18,6 s", "T6": "18,6 a 26,2 s"}


def pacote(a):
    ks, vs = keyframes(a), videos(a)
    L = [f"# {a['nome']} | FityWell Growth Canela sobre o açúcar | Pacote de Prompts", "",
         "Vídeo modelo: `input/reference_video.mp4` (James Smith, 26,2 s)", "",
         f"Âncora: `{a['ancora']}`" + (" (character sheet: só identidade, o cenário vem do texto)" if a["sheet"] else ""), "",
         "Funil: growth, comentário `yes` + follow. Rodada de validação, gancho fiel ao modelo. Sem produto em quadro.", "",
         "## Índice de geração", "",
         "| Take | Keyframe | Anexar | Ação |", "|---|---|---|---|"]
    for k in ks:
        anex = f"ÂNCORA {a['nome'].upper()}" + (" + FRAME DO MODELO" if k["anexos"] > 1 else "")
        L.append(f"| {k['take']} | {k['codigo']} | {anex} | GERAR DO ZERO |")
    L += ["", "Todo K é GERAR DO ZERO: o bloco do Flow é autossuficiente e cada K descreve o cenário inteiro, "
          "então não existe `EDITAR do K__` aqui.", "",
          "## Trava de identidade e continuidade", "",
          f"- Identidade: {a['identidade']}",
          f"- Roupa: {a['roupa']}",
          f"- Cenário do corpo: {a['cena_corpo']}",
          f"- Luz: {a['luz']}",
          f"- Voz (igual em todos os V): {a['voz']}, sotaque americano {a['sotaque']}.",
          "- Sem 2ª pessoa. O manequim do gancho é prop e não aparece do T2 em diante.", "",
          "## Trava do prop herói", "",
          "- Gancho: manequim feminino de plástico fosco sentado numa cadeira de escritório preta, camiseta cinza puxada "
          "até abaixo do peito, calça bege, barriga coberta por uma montanha alta de cubos de açúcar mascavo. Pote de canela "
          "transparente com tampa laranja, sem rótulo.",
          "- Corpo: um copo reto de vidro transparente. Água limpa (T2), água turva de canela (T3), bebida âmbar (T4 a T6).",
          "", "## Trava da 2ª pessoa (REF-A)", "", "- Não se aplica: não há 2ª pessoa. O manequim é prop.", "",
          "## Prompts de imagem", ""]
    for k in ks:
        anex = f"ÂNCORA {a['nome'].upper()}" + (" + FRAME DO MODELO" if k["anexos"] > 1 else "")
        L += [f"## {k['codigo']} · {k['take']} · GERAR DO ZERO · {anex}", "", anexo(a, k), "",
              f"Cena: {k['titulo']}.", "", "```json", json.dumps(k["j"], ensure_ascii=False, indent=2), "```", ""]
    art = "o avatar" if a["genero"] == "homem" else "a avatar"
    ouvido = "ouvido" if a["genero"] == "homem" else "ouvida"
    L += ["## Bloco global de vídeo", "", "```text",
          f"{art} {a['nome']}, {a['genero']}, fala em inglês com sotaque americano {a['sotaque']}, {a['voz']}, "
          f"[emoção da fala], voz autêntica, como se exigisse ser {ouvido}, a seguinte frase: \"[FALA EXATA DO ROTEIRO]\"", "",
          f"{art} diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.", "",
          "o que acontece no vídeo: [ação enxuta]", "", "câmera: [fixa]", "", f"som ambiente: {a['som']}, sem música",
          "```", "", "# Prompts de vídeo", ""]
    for cod, take, kcod, txt in vs:
        L += [f"### {cod} · {take} · usa {kcod}", "", "```text", txt, "```", ""]
    L += ["## Mapa de âncoras", "", "| Keyframe | Referências a anexar | Modelo |", "|---|---|---|",
          f"| K01 | ÂNCORA {a['nome'].upper()} + FRAME DO MODELO (`{FRAME_MODELO}`, só composição) | Nano Banana 2, 9:16 |",
          f"| K02 a K06 | ÂNCORA {a['nome'].upper()} | Nano Banana 2, 9:16 |", "",
          "## Montagem no CapCut", "",
          "1. Clipes numerados na ordem: V01, V02, V03, V04, V05, V06.",
          "2. Cortar cada clipe no tempo da cena do modelo: " + "; ".join(f"{t} {CORTE[t]}" for t in CORTE) + ".",
          "3. Zero tempo morto: todo clipe começa já falando. Isolate Voice / Keep Vocal no áudio.",
          "4. Nos clipes de cena curta (V01 a V04) a fala vem no começo; cortar logo depois da última palavra, no tempo da cena.",
          "5. Legenda palavra a palavra com destaque amarelo, igual ao modelo. `yes` isolado na tela no T6.",
          "6. Sem Voice Changer: a voz vem do prompt de cada V.",
          "7. Música só no corpo (V02 em diante), nunca no gancho, entre -19 e -20 dB, fora da biblioteca do TikTok.",
          "8. Rótulo pequeno `AI-generated` num canto do vídeo.", "",
          "## Gates de qualidade", "",
          "1. Fala de cada V igual ao ROTEIRO, palavra por palavra.",
          "2. Um take por cena do modelo; T1 a T4 marcados CENA CURTA; nenhum take acima de 29 palavras.",
          "3. Bandeira dos EUA no campo scene de todo K.",
          "4. Zero travessão.", "5. Keyword `yes` no T6.", "6. Produto fora de quadro.",
          "7. Negative sem termo sensível.",
          "8. GATE_VISUAL Partes 1 a 3 em todo K: herói colado na lente, luz neutra, sem tom quente, sem blur, trecho de realismo.",
          "9. Gancho fiel no conteúdo: canela sobre a montanha de cubos de açúcar que desaba e revela a barriga lisa.",
          "10. Um K = um V, e o reveal do gancho é uma imagem só, do estado inicial.", ""]
    flow = [f"# Blocos limpos para o Google Flow | {a['nome']}", "", f"Fonte interna: `PROMPTS_{a['arquivo']}.md`", "",
            "## BLOCO DE IMAGEM", "", "```text"]
    for k in ks:
        flow += [k["codigo"], texto_flow(k["j"]), ""]
    flow += ["```", "", "## BLOCO DE VÍDEO", "", "```text"]
    for cod, _, _, txt in vs:
        flow += [cod, txt, ""]
    flow += ["```", "", "## Tabela de leitura humana", "", "| Código | Take | Anexar |", "|---|---|---|"]
    for k in ks:
        flow.append(f"| {k['codigo']} / V{k['codigo'][1:]} | {k['take']}, {k['titulo']} | ÂNCORA"
                    + (" + FRAME DO MODELO" if k["anexos"] > 1 else "") + " |")
    flow += ["", "## Transcrição final por take", "", "| Take | English | Português |", "|---|---|---|"]
    for t in FALAS:
        flow.append(f"| {t} | {FALAS[t]} | {TRANSCRICAO_PT[t]} |")
    return "\n".join(L) + "\n", "\n".join(flow) + "\n"


def main():
    fila = (AQUI / "AVATAR_QUEUE.md").read_text(encoding="utf-8")
    ativo = sys.argv[1] if len(sys.argv) > 1 else re.search(r"\| ACTIVE \| ([^|]+?) \|", fila).group(1)
    for a in AVATARES:
        p, f = pacote(a)
        (AQUI / f"PROMPTS_{a['arquivo']}.md").write_text(p, encoding="utf-8")
        (AQUI / f"FLOW_{a['arquivo']}.md").write_text(f, encoding="utf-8")
        if a["nome"] == ativo:
            (AQUI / "PROMPTS_PRODUCAO.md").write_text(p, encoding="utf-8")
    print("ok: 9 pacotes; PROMPTS_PRODUCAO.md =", ativo)


if __name__ == "__main__":
    main()
