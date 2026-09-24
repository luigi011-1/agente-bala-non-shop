"""Gera os pacotes por avatar da producao fitywell_growth_dentes_agua.

Fonte unica da fala: ROTEIRO.md aprovado (lido do disco, nunca redigitado). A unica fala que muda por
avatar e a frase de autoridade do T6 (tabela de congruencia do ROTEIRO), aplicada aqui por troca exata.
Identidade, roupa e cenario de cada avatar: as fichas aprovadas em fitywell_growth_canela_acucar
(2026-09-23), conferidas de novo contra as ancoras anexadas nesta producao.

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
assert len(FALAS) == 7, FALAS
TAKES = list(FALAS)

AUTORIDADE_50 = "In 30 years of working in wellness"
AUTORIDADE_JOVEM = "In all my years of working in wellness"
assert AUTORIDADE_50 in FALAS["T6"]
JOVENS = {"Ivy Carl", "Jamie Voss", "Lais Collins", "Robert Alves"}

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

NEG_BASE = ("no captions, no subtitles, no words overlaid on the image, no printed labels or lettering on any package, "
            "no studio, no plastic-looking human skin, no extra fingers, "
            "no supernatural lighting, no blur, no bokeh, no artificial lighting, no warm orange color cast, "
            "no yellow tint, no golden glow, no golden hour light, no sunset, no de-aging, no beauty smoothing, "
            "no visible phone, no HDR, no cinematic lighting")
NEG_HOOK = (", no real human mouth, no small dental model, no toy-sized teeth, no clean white teeth yet, "
            "no second person in frame")
NEG_CORPO = ", no dental model in frame, no second person in frame"

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

# O gancho: o mesmo lugar de cada avatar, visto de câmera baixa noutro ponto da superfície de trabalho.
HOOK_CENA = {
    "Dana Morrison": "The same lived-in garage as the reference image, seen from a low angle at the other end of his scuffed wooden workbench: the open garage door with the residential street behind him, the ceiling-mounted garage door opener above, and a wooden shelf holding a small American flag at the side.",
    "Eva Dall": "His own modern white kitchen, at the other end of the dark green veined marble counter: tall windows behind him and a small American flag beside a small potted plant on the shelf.",
    "Ivy Carl": "His own covered American backyard veranda, at the weathered wooden table: the beige veranda ceiling with a recessed light above him, and a black-framed glass door holding a small American flag with a glimpse of turquoise pool behind him.",
    "Jamie Anderson": "His own small family farm under an overcast sky with visible cloud texture, at the weathered grey wooden picnic table: white wooden beehive boxes on the grass and a weathered red barn with a small American flag on its wall behind him.",
    "Jamie Voss": "His own bright residential kitchen, at the white-veined stone counter: cream upper cabinets and a black-framed window with a small American flag behind him. The counter top is clear except for the dental model.",
    "Lais Collins": "His own bright contemporary apartment, at the white kitchen island: floor-to-ceiling windows and a shelf of green plants holding a small American flag behind him.",
    "Lynn Parker": "His own Japanese-style Zen tea garden in America under an overcast sky with visible cloud texture, at the light wooden table: two cherry trees in pink bloom and the small wooden tea house with a small American flag by its door behind him.",
    "Robert Alves": "His own American timber cabin kitchen, at the light butcher-block counter: pine walls, large windows showing pine forest and a small American flag on a shelf behind him.",
    "Roberta Carvalho": "Her own residential kitchen, at the light stone counter: dark wood cabinets, a broad window showing a green garden and a small American flag on the open shelf behind her. The counter top is clear except for the dental model.",
}
assert set(HOOK_CENA) == {a["nome"] for a in AVATARES}

DENTAL = ("An oversized plastic dental demonstration model, as big as a serving platter: the complete lower arch of teeth "
          "in a horseshoe shape, set in glossy pink plastic gums, lying flat on {sup}. Every tooth is covered in a thick, "
          "crusty, uneven layer of brown and yellow stain deposits, with dark brown lines along the gumline and between "
          "the teeth, clearly a teaching model and not a real mouth.")
INGREDIENTES = ("a plain clear glass jar of solid white coconut oil with no label, a small plain white cardboard carton of "
                "baking soda with no printing on it, and half a fresh yellow lemon")

EMOCAO = {
    "T1": "entonação confiante e cúmplice, como quem conta um segredo que ninguém mais conta",
    "T2": "entonação calma e didática",
    "T3": "entonação calma e didática",
    "T4": "entonação calma e didática, sorrindo de leve",
    "T5": "entonação confiante, explicando com clareza",
    "T6": "entonação calorosa e segura, com orgulho tranquilo no fim",
    "T7": "entonação animada e convidativa, sorrindo",
}
ACOES = {
    "T1": "{n} inclina a garrafa e a água cai em fio sobre os dentes manchados do modelo dental; a crosta marrom escorre com espuma e os dentes vão aparecendo brancos, da frente para os lados, até a arcada inteira ficar branca e limpa; {pr} fala olhando para a câmera o tempo todo.",
    "T2": "{n} põe uma colher de óleo de coco na tigela de vidro, depois uma colher de bicarbonato, e espreme três gotas do meio limão dentro dela, enquanto a câmera se aproxima devagar das mãos e da tigela.",
    "T3": "{n} mexe a mistura com a colher e ela vira uma pasta branca e cremosa. {Pr} diz a frase em ritmo natural logo no começo e continua mexendo em silêncio até o fim.",
    "T4": "{n} segura a tigela com a pasta branca perto da câmera com as duas mãos, inclinado para a frente, e fala direto para a lente.",
    "T5": "{n} segura a tigela com as duas mãos na altura do peito e fala para a câmera, com pequenos movimentos naturais.",
    "T6": "{n} segura a tigela com as duas mãos na altura do peito e fala para a câmera, sorrindo no fim.",
    "T7": "{n} segura a tigela com as duas mãos, se inclina um pouco para a câmera e fala direto com ela, sorrindo.",
}
CAMERA = {"T1": "fixa, baixa, leve handheld", "T2": "push-in lento, do plano médio até as mãos e a tigela",
          "T3": "fixa, fechada nas mãos", "T4": "fixa", "T5": "fixa", "T6": "fixa", "T7": "fixa"}
SOM_EXTRA = {"T1": ", som da água caindo e borbulhando", "T3": ", som leve da colher na tigela"}

TRANSCRICAO_PT = {
    "T1": "Seu dentista nunca vai te contar isso, porque no dia em que você aprender é o dia em que você para de pagar por clareamento.",
    "T2": "Pegue uma colher de sopa de óleo de coco, meia colher de chá de bicarbonato e três gotas de suco de limão,",
    "T3": "e misture até virar uma pasta.",
    "T4": "Escove com ela toda manhã por dois minutos, depois cuspa e enxágue com água morna.",
    "T5": "O óleo de coco puxa as bactérias e o acúmulo do seu esmalte, o bicarbonato levanta as manchas da superfície, e o limão clareia tudo.",
    "T6": "Aquele amarelo começa a sumir, e as manchas desaparecem como se nunca tivessem existido. Em 30 anos trabalhando com bem-estar, isso é algo que eu sempre ensino.",
    "T7": "Comente yes se você quer mais vídeos úteis como este, e não deixe de me seguir para não perder o próximo.",
}
CORTE = {"T1": "0,0 a 5,9 s", "T2": "5,9 a 11,4 s", "T3": "11,4 a 13,1 s", "T4": "13,1 a 17,5 s",
         "T5": "17,5 a 25,3 s", "T6": "25,3 a 32,4 s", "T7": "32,4 a 37,7 s"}


def falas(a):
    f = dict(FALAS)
    pt = dict(TRANSCRICAO_PT)
    if a["nome"] in JOVENS:
        f["T6"] = f["T6"].replace(AUTORIDADE_50, AUTORIDADE_JOVEM)
        pt["T6"] = pt["T6"].replace("Em 30 anos", "Em todos os meus anos")
    return f, pt


def keyframes(a):
    n, P, p = a["nome"], a["pron"], a["pos"]
    ref = f"Use the attached image only for {n}'s exact identity, wardrobe and own setting. Do not copy its pose or framing."
    boca = "caught mid-sentence, lips naturally parted, animated expression"
    ks = [dict(
        codigo="K01", take="T1", titulo="gancho, a água sobre o modelo dental manchado", anexos=2,
        j={
            "shot_id": f"K01_gancho_{a['arquivo'].lower()}",
            "reference_use": ref + " Use the second attached image only as a composition reference for the low camera, the dental model filling the lower half and the water bottle tilted over it; do not copy its man, his clothes, glasses, room or colors.",
            "fiction_note": FICCAO,
            "identity_main": a["identidade"],
            "wardrobe": a["roupa"],
            "scene": HOOK_CENA[n],
            "prop": DENTAL.format(sup=a["superficie"]) + f" {n} holds a clear plastic water bottle with no label in one hand, tilted over the front teeth, and a thin stream of water is just starting to fall onto them.",
            "posture": f"{n} leans in from behind the dental model, looking into the lens over it, the hand with the water bottle reaching over the teeth.",
            "composition": f"The dental model fills the whole lower half of the frame, very close to the lens, large in frame, much closer to the camera than {p} face. {P} is clear in the upper half, head and upper chest. Nothing else competes with the dental model.",
            "camera": "phone camera low, just above the level of the teeth and very close to them, slight upward angle",
            "state": f"Start frame: the first thin stream of water is just touching the fully stained front teeth; every tooth is still brown and yellow. {n} is {boca}.",
            "lighting": a["luz"],
            "realism": REALISMO,
            "aspect_ratio": "9:16 vertical",
            "negative": NEG_BASE + NEG_HOOK,
        })]
    corpo = [
        ("K02", "T2", "coco entrando na tigela, plano médio",
         f"An empty clear glass mixing bowl stands on {a['superficie']} in the lower foreground, very close to the lens, larger in frame than {p} hands. Beside it on {a['superficie']}: {INGREDIENTES}. {n} holds a metal spoon with a heaped scoop of solid white coconut oil right above the bowl.",
         "From the waist up, the bowl in the lower foreground closer to the camera than " + p + " face",
         f"Start frame: {n} is about to drop the coconut oil into the bowl, {boca}."),
        ("K03", "T3", "mãos misturando a pasta, close",
         f"A clear glass mixing bowl with coconut oil, baking soda and a little lemon juice half-mixed into a thick white paste fills the lower half of the frame on {a['superficie']}, very close to the lens. {n}'s hands hold the bowl rim and a metal spoon stirring inside it.",
         f"Close shot of the hands and the bowl, from the chest down, {p} face cut off by the top edge of the frame",
         "Start frame: the spoon is mid-stir, the mixture streaky and almost a smooth paste."),
        ("K04", "T4", "tigela pronta perto da lente, inclinado",
         f"{n} holds a clear glass bowl full of smooth creamy white paste with both hands, pushed toward the lens, very close to the camera in the lower foreground. On {a['superficie']} at the bottom edge: {INGREDIENTES}.",
         f"From the chest up, leaning toward the lens, {p} face clear in the upper half, the bowl in the lower foreground closer to the camera than {p} face",
         f"Start frame: {n} leans forward holding the bowl out, {boca}."),
        ("K05", "T5", "tigela na altura do peito",
         f"{n} holds the clear glass bowl of smooth creamy white paste with both hands at chest height, very close to the lens in the lower foreground. On {a['superficie']} at the bottom edge: {INGREDIENTES}.",
         f"From the chest up, {p} face clear in the upper half, the bowl in the lower foreground closer to the camera than {p} face",
         f"Start frame: {n} looks into the lens holding the bowl, {boca}."),
        ("K06", "T6", "tigela na altura do peito, sorriso",
         f"{n} holds the clear glass bowl of smooth creamy white paste with both hands at chest height, very close to the lens in the lower foreground. On {a['superficie']} at the bottom edge: {INGREDIENTES}.",
         f"From the chest up, {p} face clear in the upper half, the bowl in the lower foreground closer to the camera than {p} face",
         f"Start frame: {n} looks into the lens with a warm, confident half smile, {boca}."),
        ("K07", "T7", "tigela, plano mais fechado do vídeo",
         f"{n} holds the clear glass bowl of smooth creamy white paste with both hands at chest height, very close to the lens in the lower foreground.",
         f"Tightest shot of the video: from the upper chest up, {p} face clear in the upper half, the bowl in the lower foreground closer to the camera than {p} face",
         f"Start frame: {n} leans a little toward the lens, smiling, {boca}."),
    ]
    for cod, take, titulo, prop, comp, estado in corpo:
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
                "composition": comp + ". The background is reduced by framing, never by blur.",
                "camera": "phone camera at chest height, straight on, fixed" if cod != "K03" else "phone camera close to the bowl, slightly above it, fixed",
                "state": estado,
                "lighting": a["luz"],
                "realism": REALISMO,
                "aspect_ratio": "9:16 vertical",
                "negative": NEG_BASE + NEG_CORPO,
            }))
    return ks


def videos(a):
    n = a["nome"]
    f, _ = falas(a)
    art = "o avatar" if a["genero"] == "homem" else "a avatar"
    pr = "ele" if a["genero"] == "homem" else "ela"
    ouvido = "ouvido" if a["genero"] == "homem" else "ouvida"
    vs = []
    for i, take in enumerate(TAKES, 1):
        acao = ACOES[take].format(n=n, pr=pr, Pr=pr.capitalize())
        if a["genero"] == "mulher":
            acao = acao.replace("inclinado para a frente", "inclinada para a frente")
        txt = (f"{art} {n}, {a['genero']}, fala em inglês com sotaque americano {a['sotaque']}, {a['voz']}, "
               f"{EMOCAO[take]}, voz autêntica, como se exigisse ser {ouvido}, a seguinte frase: \"{f[take]}\"\n\n"
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


def pacote(a):
    ks, vs = keyframes(a), videos(a)
    f, pt = falas(a)
    L = [f"# {a['nome']} | FityWell Growth Água no modelo dental | Pacote de Prompts", "",
         "Vídeo modelo: `input/reference_video.mp4` (37,7 s)", "",
         f"Âncora: `{a['ancora']}`", "",
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
          f"- Cenário do gancho: {HOOK_CENA[a['nome']]}",
          f"- Luz: {a['luz']}",
          f"- Voz (igual em todos os V): {a['voz']}, sotaque americano {a['sotaque']}.",
          "- Sem 2ª pessoa. O modelo dental só aparece no gancho.", "",
          "## Trava do prop herói", "",
          "- Gancho: " + DENTAL.format(sup=a["superficie"]) + " Garrafa plástica transparente de água, sem rótulo.",
          f"- Corpo: tigela de vidro transparente; na superfície, {INGREDIENTES}. Nenhuma embalagem com texto ou marca.",
          "", "## Trava da 2ª pessoa (REF-A)", "", "- Não se aplica: não há 2ª pessoa.", "",
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
          f"| K02 a K07 | ÂNCORA {a['nome'].upper()} | Nano Banana 2, 9:16 |", "",
          "## Montagem no CapCut", "",
          "1. Clipes numerados na ordem: V01, V02, V03, V04, V05, V06, V07.",
          "2. Cortar cada clipe no tempo da cena do modelo: " + "; ".join(f"{t} {CORTE[t]}" for t in CORTE) + ".",
          "3. Zero tempo morto: todo clipe começa já falando. Isolate Voice / Keep Vocal no áudio.",
          "4. V03 é cena curta: a fala vem no começo; cortar logo depois de \"paste\", no tempo da cena.",
          "5. Legenda palavra a palavra em serifa itálica branca no meio do quadro, igual ao modelo, do começo ao fim.",
          "6. Sem Voice Changer: a voz vem do prompt de cada V.",
          "7. Música só no corpo (V02 em diante), nunca no gancho, entre -19 e -20 dB, fora da biblioteca do TikTok.",
          "8. Rótulo pequeno `AI-generated` num canto do vídeo.", "",
          "## Gates de qualidade", "",
          "1. Fala de cada V igual ao ROTEIRO, palavra por palavra (T6 na versão do avatar, tabela de congruência).",
          "2. Um take por cena do modelo; T3 marcado CENA CURTA; nenhum take acima de 29 palavras.",
          "3. Bandeira dos EUA no campo scene de todo K.",
          "4. Zero travessão.", "5. Keyword `yes` no T7.", "6. Produto fora de quadro, nenhuma embalagem com marca ou texto.",
          "7. Negative sem termo sensível.",
          "8. GATE_VISUAL Partes 1 a 3 em todo K: herói colado na lente, luz neutra, sem tom quente, sem blur, trecho de realismo.",
          "9. Gancho fiel no conteúdo: água de garrafa sobre o modelo dental gigante manchado, que fica branco sem corte.",
          "10. Um K = um V, e o reveal do gancho é uma imagem só, do estado inicial (arcada inteira manchada).", ""]
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
    for t in TAKES:
        flow.append(f"| {t} | {f[t]} | {pt[t]} |")
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
    print("ok: %d pacotes; PROMPTS_PRODUCAO.md = %s" % (len(AVATARES), ativo))


if __name__ == "__main__":
    main()
