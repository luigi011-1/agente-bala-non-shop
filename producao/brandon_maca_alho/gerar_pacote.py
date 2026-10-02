"""Gera o pacote da producao brandon_maca_alho (avatar IA, VENDA, validacao, holistic.brandon).

Fonte unica da fala: ROTEIRO.md aprovado (lido do disco, nunca redigitado). Identidade, roupa e
cenario: a ancora aprovada em 2026-09-29 (avatar fixo por conta). Medidas de cada K: a ficha abaixo,
escrita olhando input/frames_modelo/Kxx_modelo.png, e gravada em FICHA_FRAMES.md com o placar cuja
evidencia e conferida aqui mesmo contra o texto do K (assert). Prompt de imagem em JSON (Flow v17).
Gabarito de formato: brandon_pes_peroxido/gerar_pacote.py.

Saidas: FICHA_FRAMES.md, PROMPTS_BRANDON.md, FLOW_BRANDON.md e PROMPTS_PRODUCAO.md (avatar ACTIVE).

Uso: python3 gerar_pacote.py
"""
import json
import re
from pathlib import Path

AQUI = Path(__file__).resolve().parent
ROTEIRO = (AQUI / "ROTEIRO.md").read_text(encoding="utf-8")

HEADS = dict(re.findall(r"^### (T\d+) · (.+)$", ROTEIRO, re.M))
TAKES = list(HEADS)
assert TAKES == ["T%d" % i for i in range(1, 14)], TAKES
FALAS = {}
for bloco in re.split(r"^(?=### T\d+ · )", ROTEIRO, flags=re.M)[1:]:
    m = re.search(r'^> "(.+?)"\s*$', bloco.split("\n## ")[0], re.M)
    if m:
        FALAS[re.match(r"### (T\d+)", bloco).group(1)] = m.group(1)
assert set(FALAS) == set(TAKES), FALAS
TRANSCRICAO_PT = dict(re.findall(r"^\| (T\d+) \| [^|]+ \| .+? \| (.+?) \|$",
                                 ROTEIRO.split("## Tabela bilíngue")[1].split("\n## ")[0], re.M))
assert set(TRANSCRICAO_PT) == set(TAKES), TRANSCRICAO_PT
# Cenas curtas do modelo: a fala entra no comeco do clipe e o resto e acao em silencio.
FALA_NO_COMECO = {"T2", "T3", "T4"}

FICCAO = "This is a fictional AI-generated character, no real person is depicted."


def frame_modelo(cod):
    return f"input/frames_modelo/{cod}_modelo.png"


LUZ = ("Neutral overcast daylight from a large window out of frame, soft even light on her face, hands and the "
       "table with no harsh shadows. The red neon glows on the wall but does not tint her skin.")
REALISMO = ("Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural "
            "clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday "
            "reality, background fully in focus, everything in sharp focus, no AI polish, no beauty smoothing.")
NEG_BASE = ("no captions, no subtitles, no words overlaid on the image, no printed labels or lettering on the "
            "blender, bowl, glass or apple, no studio, no plastic-looking skin, no extra fingers, no third hand, "
            "no blur, no bokeh, no warm orange color cast, no yellow tint, no golden glow, no golden hour light, "
            "no sunset, no HDR, no cinematic lighting, no beauty smoothing, no visible phone, no second person, "
            "no eyeglasses, no gray t-shirt, no white kitchen cabinets, no marble countertop, no silver cross")

A = dict(
    nome="Brandon", arquivo="BRANDON", ancora="producao/_ancoras/holistic_brandon_ancora.jpg",
    identidade=("The exact fictional AI character holistic.brandon: Black mixed-race American woman around thirty, "
                "athletic and toned, medium light-brown skin with light freckles across the nose and cheeks, dark brown "
                "eyes, defined eyebrows, full lips, hair in tight cornrows that turn into long loose braids falling "
                "over both shoulders, finished with small wooden and gold beads, a black floral blackwork tattoo "
                "sleeve on her right arm, a fine line tattoo on her left inner arm and a small fine-line floral "
                "tattoo below her left collarbone."),
    roupa=("Plain white ribbed tank top with nothing printed on it, loose black training shorts, a thin gold chain "
           "with a small gold cross pendant and small stud earrings."),
    cena=("Her own garage gym: a white-painted concrete block wall behind her, a red neon sign reading TRAIN PRAY "
          "REPEAT on the wall at the left, a whiteboard with handwritten black marker reading STAY READY. STAY "
          "DISCIPLINED. on the right, and a small American flag pinned above the whiteboard, discreet but clearly "
          "visible and in focus. In front of her stands a plain matte black table she uses as a counter."),
    voz="voz feminina clara e firme de uma mulher de uns trinta anos",
    sotaque="de uma mulher negra americana",
    som="box de treino em casa, tranquilo",
)

MACA = ("A whole shiny red apple with its core scooped out from the top, leaving a round hole about 3 centimeters "
        "wide that shows clean pale cream flesh inside")
ALHO = "a single peeled garlic clove"
LIQ = "a glass blender jar on a stainless steel base"
COPO_SUCO = "a clear drinking glass full of a pale creamy yellow apple drink"
BOCA = "caught mid-sentence, lips naturally parted, animated expression, looking straight into the lens"
REF = ("Use the first attached image only for {n}'s exact identity, wardrobe and own garage gym with the black "
       "table. Use the second attached image only as a composition reference for the camera position, framing and "
       "the action; do not copy its person, eyeglasses, gray t-shirt, white kitchen, marble countertop, wall "
       "decorations or the caption text.")
CAM_PEITO = "phone held at her chest height, tilted slightly down toward the table, standard 1x lens, light handheld"
FALA_POST = ("{n} stands behind the black table, leaning on its edge with both forearms, holding the glass up in her "
             "right hand, her left hand {mao}.")
FALA_PROP = (f"{COPO_SUCO[0].upper()}{COPO_SUCO[1:]}, held up in her right hand at chest height, close to the lens "
             "in the lower foreground. The apple, the blender and the bowl are out of frame.")


def fala_comp(cm, pct, extra=""):
    return (f"Straight-on medium shot{extra}: the phone lens is about {cm} centimeters from the glass, which fills "
            f"the lower left {pct} percent of the frame, closer to the camera than her face; her face and shoulders "
            "fill the upper half of the frame and her forearms rest on the edge of the black table at the bottom. "
            "Nothing else is on the table. The background is reduced by framing, never by blur.")


# Corpo falado T6 a T13: mesmo setup (Setup F), variacao leve de camera e gesto; T13 e o mais fechado (CTA).
FALA_VAR = {
    "T6": dict(cm=40, pct=20, extra="", cam="phone at her eye level, standard 1x lens, straight-on, fixed",
               mao="open in a small gesture", est="calm and sure"),
    "T7": dict(cm=40, pct=20, extra=" from slightly above", cam="phone just above her eye level, tilted slightly down, standard 1x lens, fixed",
               mao="raised with the index finger up", est="intrigued, as if about to tell a secret"),
    "T8": dict(cm=35, pct=22, extra="", cam="phone at her eye level, standard 1x lens, straight-on, fixed",
               mao="resting flat on the table", est="warm and knowing"),
    "T9": dict(cm=35, pct=22, extra=" from a slight angle at her left", cam="phone at her eye level, slightly to her left, standard 1x lens, fixed",
               mao="counting on her fingers", est="serious and focused"),
    "T10": dict(cm=35, pct=22, extra="", cam="phone at her eye level, standard 1x lens, straight-on, fixed",
                mao="open with the palm up", est="firm and reassuring"),
    "T11": dict(cm=35, pct=22, extra=" from slightly above", cam="phone just above her eye level, tilted slightly down, standard 1x lens, fixed",
                mao="pointing loosely toward the lens", est="direct and slightly indignant"),
    "T12": dict(cm=30, pct=25, extra=", tighter", cam="phone at her eye level, standard 1x lens, straight-on, fixed",
                mao="resting on the table", est="warm and inviting"),
    "T13": dict(cm=25, pct=28, extra=", the tightest of the video", cam="phone at her eye level, standard 1x lens, straight-on, fixed",
                mao="resting on the table", est="intense and certain"),
}

EMOCAO = {
    "T1": "entonação animada e intrigante, com espanto no fim, como quem revela um segredo",
    "T2": "entonação animada e didática, rápida",
    "T3": "entonação animada e didática, rápida",
    "T4": "entonação animada e didática, rápida",
    "T5": "entonação convicta e entusiasmada",
    "T6": "entonação convicta e animada",
    "T7": "entonação intrigante, baixando um pouco a voz no fim",
    "T8": "entonação calorosa, imitando a cliente na frase citada",
    "T9": "entonação séria e firme",
    "T10": "entonação firme e acolhedora, com ênfase em You didn't",
    "T11": "entonação direta, levemente indignada",
    "T12": "entonação calorosa e convidativa, com ênfase no yes",
    "T13": "entonação intensa e segura, com urgência no fim",
}
ACOES = {
    "T1": ("{n} empurra o dente de alho para dentro do buraco da maçã; por volta de 2 segundos uma espuma branca "
           "começa a subir do buraco e cresce em bolhas grandes, cobrindo o topo da maçã e escorrendo pelos lados "
           "até o fim do clipe; ela olha da maçã para a câmera, espantada."),
    "T2": "{n} vira a tigela e os pedaços de maçã caem dentro da jarra do liquidificador.",
    "T3": "{n} solta o dente de alho dentro da jarra e espreme o meio limão por cima.",
    "T4": "{n} despeja o copo de água dentro da jarra.",
    "T5": "{n} despeja o suco batido, grosso e amarelo-claro, da jarra dentro do copo, olhando para a câmera.",
    "T6": "{n} fala para a câmera segurando o copo do suco, com pequenos gestos da outra mão.",
    "T7": "{n} levanta o dedo indicador da mão livre e fala para a câmera, segurando o copo.",
    "T8": "{n} fala para a câmera segurando o copo, com a mão livre apoiada na mesa.",
    "T9": "{n} conta nos dedos da mão livre enquanto fala, segurando o copo.",
    "T10": "{n} abre a mão livre com a palma para cima e fala para a câmera, segurando o copo.",
    "T11": "{n} aponta de leve para a câmera com a mão livre e fala, segurando o copo.",
    "T12": "{n} fala direto com quem assiste, sorrindo no yes, segurando o copo.",
    "T13": "{n} se inclina um pouco para a câmera e fala, séria e segura, segurando o copo.",
}
CAMERA = {"T1": "fixa, levemente de cima, colada na maçã, leve handheld natural",
          "T2": "leve handheld natural", "T3": "leve handheld natural", "T4": "leve handheld natural",
          "T5": "leve handheld natural", "T13": "fixa, leve push-in"}
SOM_EXTRA = {"T1": ", espuma chiando baixinho", "T2": ", pedaços de maçã batendo no vidro",
             "T3": ", limão sendo espremido", "T4": ", água caindo na jarra", "T5": ", suco grosso caindo no copo"}
MOMENTO = {"T1": "0,0 a 7,5 s", "T2": "7,5 a 9,5 s", "T3": "9,5 a 12,7 s", "T4": "12,7 a 14,1 s",
           "T5": "14,1 a 21,0 s", "T6": "21,0 a 27,8 s"}
TITULOS = {"T1": "gancho, alho na maçã colada na lente", "T2": "receita, maçã picada na jarra",
           "T3": "receita, alho e limão", "T4": "receita, copo de água", "T5": "despeja o suco no copo",
           "T6": "copo na mão, resultado", "T7": "copo na mão, quinto ingrediente", "T8": "copo na mão, a frase das clientes",
           "T9": "copo na mão, as três causas", "T10": "copo na mão, álibi", "T11": "copo na mão, o app",
           "T12": "copo na mão, comment yes + follow", "T13": "CTA, plano mais fechado"}

# FICHA DO FRAME (GATE_VISUAL Parte 6), escrita olhando cada frame do modelo. Evidencias = trechos literais do K.
FICHA = {
    "T1": dict(heroi="maçã vermelha inteira com o miolo escavado (buraco redondo no topo) na palma da mão, e o dente de alho descascado na outra mão logo acima do buraco",
               termos=["red apple with its core scooped out", "single peeled garlic clove"],
               quadro="no modelo a maçã ocupa uns 30% de baixo, à esquerda do centro, maior que a cabeça; no K 35%",
               dist="uns 20 cm no modelo (grande-angular); no K, 15 cm",
               camera="celular na altura do peito, inclinado para baixo, grande-angular 0,5x",
               pose="debruçado sobre a bancada na direção da lente, uma mão com a maçã, a outra com o alho",
               lista="maçã, alho, mãos, avatar, cenário de fundo; bancada vazia",
               f0="alho logo acima do buraco, ainda fora; buraco limpo, sem espuma",
               desvio="cozinha branca e bancada de mármore → box de treino e mesa preta (avatar fixo); óculos e camiseta cinza → regata branca e cruz de ouro; luz neutra (gate)",
               ev=dict(F2="fills the lower 35 percent of the frame", F3="about 15 centimeters from the apple",
                       F4="wide 0.5x lens", F5="leans over the black table toward the lens", F6="nothing else in her hands")),
    "T2": dict(heroi="jarra de vidro do liquidificador vazia no primeiro plano e a tigela branca de maçã picada com casca inclinada sobre ela",
               termos=["glass blender jar", "white ceramic bowl full of apple chunks with red skin"],
               quadro="a jarra ocupa uns 35% de baixo à esquerda e a tigela o canto de cima à direita; no K igual",
               dist="uns 45 cm no modelo; no K, 40 cm",
               camera="celular na altura do peito, levemente de cima, lente 1x",
               pose="em pé atrás da bancada, as duas mãos segurando a tigela inclinada sobre a jarra",
               lista="jarra, tigela, meio limão, dente de alho, copo de água na bancada, avatar",
               f0="primeiros pedaços escorregando da tigela para a jarra vazia",
               desvio="copo medidor do modelo → copo de vidro liso; bancada de mármore → mesa preta",
               ev=dict(F2="fills the lower 35 percent of the frame", F3="about 40 centimeters from the blender jar",
                       F4="standard 1x lens", F5="both hands holding the bowl tilted over the jar", F6="Nothing else is on the table")),
    "T3": dict(heroi="jarra com a maçã picada no primeiro plano e o dente de alho na mão logo acima da boca da jarra",
               termos=["glass blender jar", "single peeled garlic clove"],
               quadro="a jarra ocupa uns 35% de baixo no centro-esquerda; no K 40%",
               dist="uns 50 cm no modelo; no K, 45 cm",
               camera="celular na altura do peito, levemente de cima, lente 1x",
               pose="em pé atrás da bancada, mão direita com o alho sobre a jarra, mão esquerda na borda da mesa",
               lista="jarra com maçã, alho, meio limão inteiro, copo de água, avatar",
               f0="alho prestes a cair; limão ainda não espremido",
               desvio="bancada de mármore → mesa preta (avatar fixo)",
               ev=dict(F2="fills the lower 40 percent of the frame", F3="about 45 centimeters from the blender jar",
                       F4="standard 1x lens", F5="her right hand holds the garlic clove right above the open jar", F6="Nothing else is on the table")),
    "T4": dict(heroi="jarra cheia de maçã e o copo de água sendo erguido ao lado da boca da jarra; o meio limão espremido colado na lente no canto de baixo",
               termos=["glass blender jar", "clear drinking glass full of water", "squeezed lemon half"],
               quadro="a jarra ocupa uns 35% de baixo no centro e o limão o canto de baixo à esquerda; no K 40%",
               dist="o limão a uns 20 cm e a jarra a uns 45 cm no modelo; no K, 15 cm e 40 cm",
               camera="celular na altura do peito, levemente de cima, lente 1x",
               pose="em pé atrás da bancada, mão direita erguendo o copo de água sobre a jarra",
               lista="jarra, copo de água, limão espremido, avatar",
               f0="copo inclinado logo acima da boca da jarra, a água ainda não caiu",
               desvio="bancada de mármore → mesa preta (avatar fixo)",
               ev=dict(F2="fills the lower 40 percent of the frame", F3="about 15 centimeters from the lens",
                       F4="standard 1x lens", F5="her right hand lifts the clear drinking glass", F6="Nothing else is on the table")),
    "T5": dict(heroi="a jarra solta da base, cheia de suco grosso amarelo-esverdeado claro, inclinada sobre um copo vazio na outra mão",
               termos=["thick pale creamy yellow-green apple drink", "empty clear drinking glass"],
               quadro="jarra e copo ocupam uns 40% do quadro no centro-direita, maiores que a cabeça; no K 45%",
               dist="uns 35 cm no modelo; no K, 30 cm",
               camera="celular na altura do peito, levemente de cima, lente 1x",
               pose="debruçado sobre a bancada, a jarra numa mão e o copo na outra",
               lista="jarra, copo, avatar, bancada vazia",
               f0="o primeiro fio de suco começando a cair no copo vazio",
               desvio="bancada de mármore → mesa preta (avatar fixo)",
               ev=dict(F2="fill the lower 45 percent of the frame", F3="about 30 centimeters from the jar",
                       F4="standard 1x lens", F5="leaning over the black table", F6="Nothing else is on the table")),
}
FALA_FICHA = dict(
    heroi="o copo de vidro cheio do suco amarelo-claro, erguido na mão direita na altura do peito, à frente do corpo",
    termos=["clear drinking glass full of a pale creamy yellow apple drink"],
    camera="celular na altura dos olhos, de frente, lente 1x",
    pose="em pé atrás da bancada, antebraços apoiados, copo na mão direita, a outra mão gesticula",
    lista="copo, avatar, bancada vazia, cenário de fundo",
    desvio="bancada de mármore e cozinha → mesa preta e box de treino (avatar fixo); o copo mais perto da lente que no modelo (piso de proximidade do gate)",
)


def keyframes(a):
    n = a["nome"]
    ref = REF.format(n=n)
    ks = {
        "T1": dict(prop=(f"{MACA}, resting in her right palm on the left side of the frame; in her left hand, between "
                         f"thumb and index finger, {ALHO}, held just above the hole. There is nothing else in her hands "
                         "and the black table below is empty."),
                   posture=f"{n} leans over the black table toward the lens, holding the apple out toward the camera.",
                   composition=("Close-up from chest height: the phone lens is about 15 centimeters from the apple, which "
                                "fills the lower 35 percent of the frame at the left of center, far closer to the camera "
                                "than her face and larger than her head, nothing else competing with it; the garlic clove "
                                "is just above it and her face is in the upper third. The background is reduced by "
                                "framing, never by blur."),
                   camera="phone held at her chest height, tilted down toward the apple, wide 0.5x lens, light handheld",
                   state=(f"Start frame: the garlic clove is held just above the hole, not yet inside; the hole shows only "
                          f"clean pale flesh, no foam yet. {n} is {BOCA}."),
                   negative=NEG_BASE + ", no foam yet, no bubbles yet"),
        "T2": dict(prop=(f"On the black table in the lower foreground, {LIQ}, empty. In her hands, a white ceramic bowl "
                         "full of apple chunks with red skin, tilted over the open jar so the first chunks slide toward "
                         "it. On the table beside the blender: half a lemon cut side up, one peeled garlic clove and a "
                         "clear drinking glass full of water."),
                   posture=f"{n} stands behind the black table, both hands holding the bowl tilted over the jar.",
                   composition=("Standing medium shot from chest height: the phone lens is about 40 centimeters from the "
                                "blender jar, which fills the lower 35 percent of the frame at the left, closer to the "
                                "camera than her face; the tilted bowl is at the upper right, close to the lens; her face "
                                "and shoulders are in the upper part of the frame. Nothing else is on the table. The "
                                "background is reduced by framing, never by blur."),
                   camera=CAM_PEITO,
                   state=f"Start frame: the first apple chunks are sliding from the bowl into the empty jar. {n} is {BOCA}."),
        "T3": dict(prop=(f"On the black table in the lower foreground, {LIQ}, half full of apple chunks with red skin. "
                         f"Her right hand holds {ALHO} right above the open jar. Half a lemon, still whole and unsqueezed, "
                         "lies cut side up on the table next to the jar, and a clear drinking glass full of water stands "
                         "behind it."),
                   posture=(f"{n} stands behind the black table; her right hand holds the garlic clove right above the "
                            "open jar and her left hand rests on the table edge."),
                   composition=("Standing medium shot from chest height: the phone lens is about 45 centimeters from the "
                                "blender jar, which fills the lower 40 percent of the frame at the left of center, closer "
                                "to the camera than her face; her face and torso fill the upper part of the frame. Nothing "
                                "else is on the table. The background is reduced by framing, never by blur."),
                   camera=CAM_PEITO,
                   state=f"Start frame: the garlic clove is about to drop into the jar. {n} is {BOCA}."),
        "T4": dict(prop=(f"On the black table, {LIQ}, half full of apple chunks with a garlic clove and lemon juice. Her "
                         "right hand lifts the clear drinking glass full of water above the open top of the jar. The "
                         "squeezed lemon half lies cut side up at the lower left corner of the table."),
                   posture=f"{n} stands behind the black table; her right hand lifts the clear drinking glass over the jar.",
                   composition=("Standing medium shot from chest height: the squeezed lemon half is about 15 centimeters "
                                "from the lens at the lower left corner and the blender jar, about 40 centimeters away, "
                                "fills the lower 40 percent of the frame at the center, both closer to the camera than her "
                                "face; her face and torso fill the upper part of the frame. Nothing else is on the table. "
                                "The background is reduced by framing, never by blur."),
                   camera=CAM_PEITO,
                   state=f"Start frame: the glass of water is tilted just above the jar, the water not poured yet. {n} is {BOCA}."),
        "T5": dict(prop=("The glass blender jar, lifted off its base and full of a thick pale creamy yellow-green apple "
                         "drink, tilted in her right hand over an empty clear drinking glass that she holds in her left "
                         "hand just above the black table."),
                   posture=f"{n} is leaning over the black table toward the lens, jar in one hand and glass in the other.",
                   composition=("Close shot from chest height: the phone lens is about 30 centimeters from the jar and "
                                "the glass, which together fill the lower 45 percent of the frame at the center right, "
                                "larger than her head and closer to the camera than her face; her face and shoulders are "
                                "in the upper third. Nothing else is on the table. The background is reduced by framing, "
                                "never by blur."),
                   camera=CAM_PEITO,
                   state=f"Start frame: the first stream of the thick drink is starting to fall into the empty glass. {n} is {BOCA}."),
    }
    for t, v in FALA_VAR.items():
        ks[t] = dict(prop=FALA_PROP, posture=FALA_POST.format(n=n, mao=v["mao"]),
                     composition=fala_comp(v["cm"], v["pct"], v["extra"]), camera=v["cam"],
                     state=f"Start frame: {n} is {BOCA}, {v['est']}.")
    out = []
    for i, t in enumerate(TAKES, 1):
        d = ks[t]
        cod = f"K{i:02d}"
        j = {
            "shot_id": f"{cod}_{t.lower()}_{a['arquivo'].lower()}",
            "fiction_note": FICCAO,
            "reference_use": ref,
            "identity_main": a["identidade"],
            "wardrobe": a["roupa"],
            "scene": a["cena"],
            "prop": d["prop"],
            "posture": d["posture"],
            "composition": d["composition"],
            "camera": d["camera"],
            "lighting": LUZ,
            "state": d["state"],
            "realism": REALISMO,
            "aspect_ratio": "9:16 vertical",
            "negative": d.get("negative", NEG_BASE),
        }
        out.append(dict(codigo=cod, take=t, titulo=TITULOS[t], j=j))
    return out


def ficha(ks):
    L = ["# FICHA DO FRAME · brandon_maca_alho", "",
         "Regra e método: `GATE_VISUAL.md` Parte 6. Cada K sai daqui, nunca da memória. O frame do modelo manda no",
         "CONTEÚDO (forma, quadro, distância, câmera, pose, o que está em quadro); o gate manda no ACABAMENTO e impõe o",
         "piso de proximidade do herói. A evidência de cada OK é um trecho que existe literalmente no K",
         "(conferido por `gerar_pacote.py` com assert antes de gravar).", ""]
    for k in ks:
        t, cod, j = k["take"], k["codigo"], k["j"]
        texto = json.dumps(j, ensure_ascii=False)
        if t in FICHA:
            f = FICHA[t]
            ev = f["ev"]
            quadro, dist, f0, termos = f["quadro"], f["dist"], f["f0"], f["termos"]
            heroi, camera, pose, lista, desvio = f["heroi"], f["camera"], f["pose"], f["lista"], f["desvio"]
        else:
            v = FALA_VAR[t]
            f = FALA_FICHA
            heroi, termos, camera, pose, lista, desvio = (f["heroi"], f["termos"], f["camera"], f["pose"],
                                                          f["lista"], f["desvio"])
            quadro = f"no modelo o copo ocupa uns 12% de baixo à esquerda; no K {v['pct']}% (piso de proximidade)"
            dist = f"uns 55 cm no modelo; no K, {v['cm']} cm"
            f0 = f"falando para a câmera com o copo erguido; mão livre {v['mao']}"
            ev = dict(F2=f"fills the lower left {v['pct']} percent of the frame",
                      F3=f"about {v['cm']} centimeters from the glass", F4="standard 1x lens",
                      F5="leaning on its edge with both forearms", F6="Nothing else is on the table")
        ev = dict(ev, G1="Neutral overcast daylight", G3="everything in sharp focus", G4="Real skin with visible pores",
                  G5="no warm orange color cast", G6="no captions", G7="small American flag", G8="caught mid-sentence")
        ev["F1"] = " · ".join(f'"{x}"' for x in termos)
        for item, e in ev.items():
            for trecho in re.findall(r'"([^"]+)"', e) if item == "F1" else [e]:
                assert trecho.lower() in texto.lower(), (cod, item, trecho)
        L += [f"## {cod}", f"Frame: `{frame_modelo(cod)}`", f"Take: {t}", f"Herói: {heroi}",
              "Termos de forma: " + ev["F1"], f"Quadro: {quadro}", f"Distância da lente: {dist}",
              f"Câmera: {camera}", f"Pose: {pose}", f"Lista fechada: {lista}", f"Frame 0: {f0}",
              f"Desvio (acabamento ou avatar fixo): {desvio}", "",
              "| Item | Status | Evidência (trecho literal do K) |", "|---|---|---|"]
        nomes = ["F1 forma do heroi", "F2 quanto do quadro", "F3 distancia da lente", "F4 camera",
                 "F5 pose do avatar", "F6 lista fechada", "G1 luz neutra", "G2 ceu ou janela", "G3 foco",
                 "G4 realismo", "G5 sem tom quente", "G6 sem texto", "G7 bandeira", "G8 boca no K de fala"]
        for nome in nomes:
            it = nome[:2]
            if it == "G2":
                L.append(f"| {nome} | N/A | sem janela nem céu em quadro: a janela fica fora do quadro, só a luz entra |")
            elif it == "F1":
                L.append(f"| {nome} | OK | {ev['F1']} |")
            else:
                L.append(f'| {nome} | OK | "{ev[it]}" |')
        L.append("")
    return "\n".join(L)


def videos(a):
    n = a["nome"]
    vs = []
    for i, t in enumerate(TAKES, 1):
        acao = ACOES[t].format(n=n)
        if t in FALA_NO_COMECO:
            acao += " Ela diz a frase em ritmo natural logo no começo e a ação continua em silêncio até o fim."
        txt = (f"a avatar {n}, mulher, fala em inglês com sotaque americano {a['sotaque']}, {a['voz']}, "
               f"{EMOCAO[t]}, voz autêntica, como se exigisse ser ouvida, a seguinte frase: \"{FALAS[t]}\"\n\n"
               "a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por "
               "inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.\n\n"
               f"o que acontece no vídeo: {acao}\n\n"
               f"câmera: {CAMERA.get(t, 'fixa')}\n\n"
               f"som ambiente: {a['som']}{SOM_EXTRA.get(t, '')}, sem música")
        vs.append((f"V{i:02d}", t, f"K{i:02d}", txt))
    return vs


def texto_flow(j):
    """Prompt de imagem de EXECUCAO, em JSON (contrato do Flow v17): sem shot_id, com o formato na frente."""
    ordem = ["fiction_note", "reference_use", "identity_main", "wardrobe", "scene", "prop", "posture",
             "composition", "camera", "lighting", "state", "realism", "aspect_ratio", "negative"]
    assert set(ordem) == set(j) - {"shot_id"}, set(j) ^ set(ordem)
    d = {"format": "IMPORTANT: THIS IS IPHONE FOOTAGE. Vertical 9:16."}
    d.update({k: j[k] for k in ordem})
    return json.dumps(d, ensure_ascii=False, indent=2)


def anexo(a, k):
    return "\n".join([
        "> ### 📎 ANEXAR: **2 IMAGENS**",
        f"> **1️⃣ ÂNCORA HOLISTIC BRANDON** `{a['ancora']}`",
        f"> **2️⃣ FRAME DO MODELO, só composição** `{frame_modelo(k['codigo'])}`",
        ">", "> ### 🆕 GERAR DO ZERO"])


def capcut():
    return [
        "1. Clipes numerados na ordem: V01 a V13.",
        "2. Cortar os seis primeiros no tempo da cena do modelo: " + "; ".join(
            f"V{t[1:].zfill(2)} {MOMENTO[t]}" for t in MOMENTO) + ". Do V07 ao V13, cortar logo depois da última palavra de cada um.",
        "3. Zero tempo morto: todo clipe começa já falando. Isolate Voice / Keep Vocal no áudio.",
        "4. Nos V02, V03 e V04 (cenas curtas) a fala vem no começo; cortar logo depois da última palavra, mantendo a ação até o tempo da cena do modelo.",
        "5. Legenda branca serifada, duas a três palavras por vez, com a palavra-chave maior, no meio-baixo do quadro, igual ao modelo. No V12, `yes` grande e isolado na tela.",
        "6. Sem Voice Changer: a voz vem do prompt de cada V.",
        "7. Música só depois do gancho (a partir do V02), nunca no pré-gancho, entre -19 e -20 dB, fora da biblioteca do TikTok.",
        "8. Rótulo pequeno `AI-generated` num canto do vídeo.",
        "9. Ao publicar, fixar o comentário com o link do plano personalizado FityWell Metabolic Reset (o V13 manda tocar nele).",
    ]


def transcricao():
    L = ["| Take | English | Português |", "|---|---|---|"]
    for t in TAKES:
        L.append(f"| {t} | {FALAS[t]} | {TRANSCRICAO_PT[t]} |")
    return L


def pacote(a):
    ks, vs = keyframes(a), videos(a)
    L = ["# holistic.brandon | FityWell Venda Alho na maçã | Pacote de Prompts", "",
         "Vídeo modelo: `input/reference_video.mp4` (38,7 s, avatar IA)", "",
         f"Âncora: `{a['ancora']}`", "",
         "Funil: VENDA. Comment `yes` + follow (engajamento) e o plano personalizado FityWell Metabolic Reset no "
         "comentário fixado. Rodada de validação, gancho fiel ao modelo. Sem produto em quadro.", "",
         "## Índice de geração", "",
         "| Take | Keyframe | Anexar | Ação |", "|---|---|---|---|"]
    for k in ks:
        L.append(f"| {k['take']} | {k['codigo']} | ÂNCORA HOLISTIC BRANDON + FRAME DO MODELO ({k['codigo']}) | GERAR DO ZERO |")
    L += ["", "Todo K é GERAR DO ZERO: o bloco do Flow é autossuficiente e cada K descreve o cenário inteiro, "
          "então não existe `EDITAR do K__` aqui. O frame do modelo de cada K entra só como composição.", "",
          "## Trava de identidade e continuidade", "",
          f"- Identidade: {a['identidade']}",
          f"- Roupa (fixa da conta): {a['roupa']}",
          f"- Cenário-base (fixo da conta): {a['cena']}",
          f"- Luz: {LUZ}",
          f"- Voz (mesmo timbre em todos os V): {a['voz']}, sotaque americano {a['sotaque']}.",
          "- Sem 2ª pessoa.", "",
          "## Trava do prop herói", "",
          f"- Gancho: {MACA}; {ALHO}. A espuma branca nasce no vídeo, nunca na imagem.",
          f"- Receita: {LIQ}, tigela branca de cerâmica com maçã picada com casca, meio limão, dente de alho, copo de água.",
          f"- Corpo: {COPO_SUCO}, sempre na mão direita dela; maçã, liquidificador e tigela fora de quadro.",
          "- Nenhuma embalagem com texto ou marca.", "",
          "## Trava da 2ª pessoa (REF-A)", "", "- Não se aplica: não há 2ª pessoa.", "",
          "## Prompts de imagem", ""]
    for k in ks:
        L += [f"## {k['codigo']} · {k['take']} · GERAR DO ZERO · ÂNCORA HOLISTIC BRANDON + FRAME DO MODELO", "",
              anexo(a, k), "", f"Cena: {k['titulo']}.", "", "```json",
              json.dumps(k["j"], ensure_ascii=False, indent=2), "```", ""]
    L += ["## Bloco global de vídeo", "", "```text",
          f"a avatar {a['nome']}, mulher, fala em inglês com sotaque americano {a['sotaque']}, {a['voz']}, "
          "[emoção da fala], voz autêntica, como se exigisse ser ouvida, a seguinte frase: \"[FALA EXATA DO ROTEIRO]\"", "",
          "a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.", "",
          "o que acontece no vídeo: [ação enxuta]", "", "câmera: [fixa]", "", f"som ambiente: {a['som']}, sem música",
          "```", "", "# Prompts de vídeo", ""]
    for cod, take, kcod, txt in vs:
        L += [f"### {cod} · {take} · usa {kcod}", "", "```text", txt, "```", ""]
    L += ["## Mapa de âncoras", "", "| Keyframe | Referências a anexar | Modelo |", "|---|---|---|"]
    for k in ks:
        L.append(f"| {k['codigo']} | ÂNCORA HOLISTIC BRANDON + `{frame_modelo(k['codigo'])}` (só composição) | Nano Banana 2, 9:16 |")
    L += ["", "## Montagem no CapCut", ""] + capcut() + [
          "", "## Gates de qualidade", "",
          "1. Fala de cada V igual ao ROTEIRO, palavra por palavra.",
          "2. Um take por cena do modelo; cenas curtas marcadas; nenhum take acima de 29 palavras.",
          "3. Bandeira dos EUA no campo scene de todo K.",
          "4. Zero travessão.", "5. Keyword `yes` no T12; FityWell e o comentário fixado ditos no T13.",
          "6. Nenhuma marca nem produto em quadro: liquidificador, tigela, jarra e copo lisos, sem app nem celular.",
          "7. Negative sem termo sensível.",
          "8. GATE_VISUAL Partes 1 a 3 em todo K: herói colado na lente, luz neutra, sem tom quente, sem blur, trecho de realismo.",
          "9. Gancho fiel no conteúdo: alho entrando na maçã escavada colada na lente e a espuma branca subindo, falado desde o segundo 0.",
          "10. Um K = um V; a espuma do T1 é uma imagem só, do estado inicial (buraco limpo).", ""]
    flow = ["# Blocos limpos para o Google Flow | holistic.brandon", "", "Fonte interna: `PROMPTS_BRANDON.md`", "",
            "## BLOCO DE IMAGEM", "", "```text"]
    for k in ks:
        flow += [k["codigo"], texto_flow(k["j"]), ""]
    flow += ["```", "", "## BLOCO DE VÍDEO", "", "```text"]
    for cod, _, _, txt in vs:
        flow += [cod, txt, ""]
    flow += ["```", "", "## Tabela de leitura humana", "", "| Código | Take | Anexar |", "|---|---|---|"]
    for k in ks:
        flow.append(f"| {k['codigo']} / V{k['codigo'][1:]} | {k['take']}, {k['titulo']} | ÂNCORA + `{frame_modelo(k['codigo'])}` |")
    flow += ["", "## Transcrição final por take", ""] + transcricao()
    return "\n".join(L) + "\n", "\n".join(flow) + "\n", ficha(ks) + "\n"


AVATARES = [A]


def main():
    p, f, fi = pacote(A)
    (AQUI / "FICHA_FRAMES.md").write_text(fi, encoding="utf-8")
    (AQUI / "PROMPTS_BRANDON.md").write_text(p, encoding="utf-8")
    (AQUI / "FLOW_BRANDON.md").write_text(f, encoding="utf-8")
    (AQUI / "PROMPTS_PRODUCAO.md").write_text(p, encoding="utf-8")
    print("ok: ficha + pacote da Brandon; PROMPTS_PRODUCAO.md = holistic.brandon")


if __name__ == "__main__":
    main()
