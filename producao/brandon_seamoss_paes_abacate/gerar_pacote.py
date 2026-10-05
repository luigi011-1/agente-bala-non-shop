"""Gera o pacote da producao brandon_seamoss_paes_abacate (Angulo 1, Natural Rems Sea Moss, venda, validacao).

Fonte unica da fala: ROTEIRO.md v1 aprovado em 2026-10-05 (lido do disco, nunca redigitado). Identidade,
roupa e cenario: a ancora aprovada (avatar fixo por conta). Medidas de cada K: os frames do modelo em
input/frames_modelo/, registradas em FICHA_FRAMES.md, que este script tambem escreve, com a evidencia
de cada OK conferida contra o texto do K (assert). Gabarito: brandon_seamoss_temperos/gerar_pacote.py.

Prompt de imagem entregue em JSON (contrato do Flow v17). Origem organica: copy literal do T1 ao T8.
Produto em quadro so de T11 a T13, com a foto oficial do pote como terceiro anexo.

Saidas: PROMPTS_BRANDON.md, FLOW_BRANDON.md, PROMPTS_PRODUCAO.md (copia do avatar ACTIVE) e
FICHA_FRAMES.md.

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
TRANSCRICAO_PT = dict(re.findall(r"^\| (T\d+) \| .+? \| (.+?) \|$",
                                 ROTEIRO.split("## Tabela bilíngue")[1].split("## ")[0], re.M))
assert set(TRANSCRICAO_PT) == set(TAKES), TRANSCRICAO_PT
FALA_NO_COMECO = set()
VOZ_OVER = {"T2", "T4"}
COM_PRODUTO = {"T11", "T12", "T13"}

FICCAO = "This is a fictional AI-generated character, no real person is depicted."
PRODUTO_IMG = "producao/_ancoras/natural_rems_seamoss_produto.jpg"


def frame_modelo(cod):
    return f"input/frames_modelo/{cod}_modelo.png"


LUZ = ("Neutral overcast daylight from a large window out of frame, soft even light on her face and hands with no "
       "harsh shadows. The red neon glows on the wall but does not tint her skin.")
REALISMO = ("Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural "
            "clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday "
            "reality, background fully in focus, everything in sharp focus, no AI polish, no beauty smoothing.")
NEG_BASE = ("no captions, no subtitles, no words overlaid on the image, no studio, no plastic-looking skin, "
            "no extra fingers, no third hand, no blur, no bokeh, no warm orange color cast, no yellow tint, "
            "no golden glow, no golden hour light, no sunset, no HDR, no cinematic lighting, no de-aging, "
            "no beauty smoothing, no visible phone, no baseball cap, no kitchen cabinets, no man, "
            "no white marble counter, no second person")
NEG_RECEITA = ", no readable lettering on the bowl, tray, oven or jars"

A = dict(
    nome="Brandon", arquivo="BRANDON", ancora="producao/_ancoras/holistic_brandon_ancora.jpg",
    identidade=("The exact fictional AI character holistic.brandon: Black mixed-race American woman around thirty, "
                "athletic and toned, medium light-brown skin with light freckles across the nose and cheeks, dark brown "
                "eyes, defined eyebrows, full lips, hair in tight cornrows that turn into long loose braids falling "
                "over both shoulders, finished with small wooden and gold beads, a black floral blackwork tattoo "
                "sleeve on her right arm, a small line tattoo on her left upper arm and small fine-line tattoos on "
                "her chest near the collarbones. She reads as an ordinary anonymous American fitness coach, not "
                "resembling anyone famous."),
    roupa=("Plain white ribbed tank top with nothing printed or written on it, loose black training shorts ending "
           "at mid-thigh, a thin gold chain with a small gold cross pendant and small stud earrings."),
    cena=("Her own garage gym, the same room as the reference: a white-painted concrete block wall and a dark wooden "
          "slat ceiling, a red neon sign reading TRAIN PRAY REPEAT on the wall at the left, a whiteboard with "
          "handwritten black marker reading STAY READY. STAY DISCIPLINED. on the right, and a small American flag "
          "pinned above the whiteboard, discreet but clearly visible and in focus. The background is reduced by "
          "framing, never by blur."),
    voz="voz feminina clara e firme de uma mulher de uns trinta anos",
    sotaque="de uma mulher negra americana",
    som="box de treino em casa, tranquilo",
)

MESA = "the black table in front of her"
TIGELA = "a large clear glass mixing bowl"
ASSADEIRA = "a rectangular silver metal baking tray"
POTE = ("the Natural Rems Sea Moss Gummies jar exactly as in the attached product photo: a short wide jar of dark "
        "amber plastic with a black screw cap, a pale sage-green label with dark green text, the Natural Rems logo "
        "with three leaves at the top, the big title Sea Moss Gummies, a pill-shaped badge reading 6000 MG | 16-IN-1, "
        "the line GREEN APPLE FLAVOR, two columns of dark green ingredient pills, green seaweed illustrations on the "
        "sides and a small 30 Gummies badge")
PAO = "one round golden-brown bun with a shiny crust and a few sesame seeds"

EMOCAO = {
    "T1": "entonação intrigante, como quem vai mostrar um truque de cozinha",
    "T2": "entonação didática e rápida, voz-over calma",
    "T3": "entonação alegre, sorrindo enquanto polvilha",
    "T4": "entonação didática, voz-over curta",
    "T5": "entonação orgulhosa e animada, marcando softest e fluffiest",
    "T6": "entonação animada, mostrando o pãozinho",
    "T7": "entonação calma e confiante",
    "T8": "entonação próxima e sincera, como quem divide o que faz todo dia",
    "T9": "entonação calorosa e firme, como quem revela algo que ninguém conta",
    "T10": "entonação pausada e curiosa, deixando a pergunta no ar",
    "T11": "entonação clara e sincera, dizendo Natural Rems Sea Moss devagar e por inteiro",
    "T12": "entonação calorosa e convidativa",
    "T13": "entonação clara e pausada, dizendo Natural Rems Sea Moss devagar e por inteiro",
}
ACOES = {
    "T1": ("{n} amassa uma batata cozida com o espremedor e a câmera acompanha a tigela: entram metades de abacate, "
           "ovos, uma colherada de iogurte grego, uma pitada de fermento e de sal, e ela mistura tudo com uma colher "
           "de madeira até virar uma massa verde-clara."),
    "T2": "As mãos de {n} sovam a massa lisa numa bolinha clara e a pousam na assadeira ao lado de outras bolinhas.",
    "T3": "{n} polvilha sementes de gergelim com as pontas dos dedos sobre as bolinhas da assadeira, sorrindo para a câmera.",
    "T4": "{n}, de perfil, enfia a assadeira com as bolinhas no forno elétrico de bancada e para com a mão na porta.",
    "T5": "{n} inclina a assadeira dos pãezinhos dourados em direção à câmera e volta a olhar a lente.",
    "T6": "{n} ergue o pãozinho dourado com as duas mãos, quase na câmera, e o vira de leve para mostrar a crosta.",
    "T7": "{n} abre o pão ao meio e aproxima as duas metades da câmera, mostrando o miolo macio e aerado.",
    "T8": "{n} fala para a câmera de selfie, segurando o pãozinho na mão direita baixa; a mão que segura o celular nunca se mexe, só a outra gesticula.",
    "T9": "{n} fala para a câmera de selfie, o pãozinho na mão baixa; só o rosto e os ombros se mexem, com um aceno de cabeça no it is protecting you; a mão que segura o celular nunca se mexe.",
    "T10": "{n} fala para a câmera de selfie, sem nada nas mãos, e inclina a cabeça de leve no final da pergunta; a mão que segura o celular nunca se mexe.",
    "T11": ("{n} segura o pote de Natural Rems Sea Moss com as duas mãos na altura do peito, rótulo de frente para a "
            "câmera, e aproxima o pote um pouco da câmera quando diz o nome."),
    "T12": ("{n} segura o pote parado com as duas mãos, rótulo de frente e legível; só o rosto e a boca se mexem."),
    "T13": ("{n} segura o pote parado com as duas mãos, rótulo de frente e legível, sem nada cobrindo, do começo ao "
            "fim; só o rosto e a boca se mexem."),
}
CAMERA = {t: "leve handheld" for t in ("T1", "T2", "T3", "T4", "T5", "T6", "T7", "T8", "T9", "T10")}
SOM_EXTRA = {"T1": ", colher batendo no vidro", "T2": ", massa sendo sovada", "T3": ", sementes caindo na bandeja",
             "T4": ", bandeja deslizando no forno"}
MOMENTO = {"T1": "0,0 a 7,4 s", "T2": "7,4 a 9,9 s", "T3": "9,9 a 12,5 s", "T4": "12,5 a 13,8 s",
           "T5": "13,8 a 19,6 s", "T6": "19,6 a 24,0 s", "T7": "24,0 a 27,4 s", "T8": "a fala inteira",
           "T9": "a fala inteira", "T10": "a fala inteira", "T11": "a fala inteira", "T12": "a fala inteira",
           "T13": "o CTA inteiro, sem corte"}
TITULOS = {"T1": "gancho, tigela de vidro colada na lente com a batata sendo amassada", "T2": "mãos moldando a bolinha de massa",
           "T3": "gergelim sobre as bolinhas", "T4": "assadeira entrando no forno de bancada",
           "T5": "assadeira dourada no colo", "T6": "pãozinho erguido na lente", "T7": "pão aberto ao meio na lente",
           "T8": "selfie, autoridade", "T9": "selfie, o corpo em guarda", "T10": "selfie, pergunta sem saída",
           "T11": "pote sobe no nome", "T12": "comentário e follow, pote parado", "T13": "CTA, pote parado e legível"}


def keyframes(a):
    n = a["nome"]
    boca = "caught mid-sentence, lips naturally parted, animated expression, looking straight into the lens"
    ref_base = (f"Use the first attached image only for {n}'s exact identity, wardrobe and her own garage gym. Use the "
                "second attached image only as a composition reference for the camera position, framing and the "
                "action; do not copy its man, his dreadlocks, his navy baseball cap, his white tank top, his kitchen "
                "or the caption text.")
    ref_prod = (ref_base + " Use the third attached image only for the exact look of the front jar and its label; "
                "ignore the MADE IN USA banner, the second jar with the Supplement Facts panel and the loose gummies.")
    post_mesa = f"{n} stands behind {MESA}, leaning forward over it, seen from the waist up."
    neg_pote = NEG_BASE + ", no second jar, no loose gummies, no banner on the jar, no fingers over the label"
    cam_selfie = "phone held at arm's length at eye height about 50 centimeters from her face, standard 1x lens, level, slightly handheld"
    comp_selfie = ("Selfie shot: the phone lens is about 50 centimeters from her face; her face and shoulders fill the "
                   "frame down to the chest and the bun in her low hand sits in the lower-left corner, closer to the "
                   "camera than her face. The background is reduced by framing, never by blur.")
    ks = {
        "T1": dict(ref=ref_base,
                   prop=(f"{TIGELA[0].upper()}{TIGELA[1:]} stands on {MESA} very close to the lens, holding three whole "
                         "boiled yellow potatoes, one of them already half mashed. She grips a stainless steel potato "
                         "masher in her right fist and presses it into the half mashed potato."),
                   posture=post_mesa,
                   composition=("Close shot from chest height: the phone lens is about 30 centimeters from the bowl, "
                                "which fills the lower 50 percent of the frame almost edge to edge, closer to the camera "
                                "than her face; her face and shoulders fill the upper part. Nothing else is on the table. "
                                "The background is reduced by framing, never by blur."),
                   camera="phone held at chest height about 30 centimeters from the bowl, standard 1x lens tilted slightly down",
                   state=f"Start frame: the masher is pressed into the potato and the bowl has no avocado, eggs or yogurt yet. {n} is {boca}.",
                   negative=NEG_BASE + NEG_RECEITA + ", no avocado in the bowl yet"),
        "T2": dict(ref=ref_base,
                   prop=(f"Her two hands shape one smooth pale dough ball over {MESA}; beside it lies {ASSADEIRA} with "
                         "five more pale round dough balls lined up on it."),
                   posture=f"{n} stands behind {MESA}, bent slightly forward, only her neck, chest and arms in frame, her chin just out of frame.",
                   composition=("Close shot from chest height: the phone lens is about 30 centimeters from her hands, "
                                "which fill the lower 50 percent of the frame, closer to the camera than her chest; the "
                                "upper part shows her tank top and chest. Nothing else is on the table. The background "
                                "is reduced by framing, never by blur."),
                   camera="phone held at chest height about 30 centimeters from her hands, standard 1x lens tilted slightly down",
                   state="Start frame: the dough ball sits in her cupped hands, smooth and round. No speech in this take.",
                   negative=NEG_BASE + NEG_RECEITA),
        "T3": dict(ref=ref_base,
                   prop=(f"{ASSADEIRA[0].upper()}{ASSADEIRA[1:]} stands on {MESA} very close to the lens with six round "
                         "pale dough buns in two rows. Her right hand, raised above the tray, pinches white sesame seeds "
                         "that are just starting to fall."),
                   posture=post_mesa,
                   composition=("Close shot from chest height: the phone lens is about 35 centimeters from the tray, which "
                                "fills the lower 45 percent of the frame almost edge to edge, closer to the camera than "
                                "her face; her face and shoulders fill the upper part. Nothing else is on the table. The "
                                "background is reduced by framing, never by blur."),
                   camera="phone held at chest height about 35 centimeters from the tray, standard 1x lens tilted slightly down",
                   state=f"Start frame: only a few sesame seeds are on the buns. {n} is {boca}, smiling.",
                   negative=NEG_BASE + NEG_RECEITA + ", no oven in the frame"),
        "T4": dict(ref=ref_base,
                   prop=(f"A small silver countertop electric oven stands at the left end of {MESA}, closer to the camera "
                         f"than she is, its glass door open. In profile, she slides {ASSADEIRA} holding six pale sesame "
                         "buns into it with both hands."),
                   posture=f"{n} stands in profile at the left end of the table, bent slightly forward, seen from the thighs up, not looking at the lens.",
                   composition=("Wide side shot from table height: the phone lens is about 1.2 meters from her and the oven is "
                                "about 70 centimeters from the lens; the oven and the tray fill the lower 40 percent of "
                                "the frame on the left, closer to the camera than her face; she fills the middle of the "
                                "frame. The background is reduced by framing, never by blur."),
                   camera="phone propped at table height about 1.2 meters from her, standard 1x lens, level",
                   state="Start frame: the tray is half inside the oven. No speech in this take.",
                   negative=NEG_BASE + NEG_RECEITA + ", no smoke, no flames"),
        "T5": dict(ref=ref_base,
                   prop=(f"On her lap she holds {ASSADEIRA} with both hands, with six golden-brown buns topped with "
                         "sesame seeds, the tray tilted slightly toward the lens."),
                   posture=f"{n} sits on the edge of {MESA}, seen from the thighs up, the tray resting on her lap, her elbows out.",
                   composition=("Straight-on medium shot from table height: the phone lens is about 80 centimeters from "
                                "her and the tray fills the lower 35 percent of the frame, closer to the camera than her "
                                "face; her face and shoulders fill the upper two thirds. The background is reduced by "
                                "framing, never by blur."),
                   camera="phone propped at table height about 80 centimeters from her, standard 1x lens, level",
                   state=f"Start frame: the golden buns are clearly visible on the tray. {n} is {boca}.",
                   negative=NEG_BASE + NEG_RECEITA),
        "T6": dict(ref=ref_base,
                   prop=f"Raised with both hands in front of her chest she holds {PAO}, close to the lens.",
                   posture=f"{n} stands behind {MESA}, seen from the chest up, the bun held toward the camera.",
                   composition=("Close shot from chest height: the phone lens is about 25 centimeters from the bun, which "
                                "fills about 35 percent of the frame in the lower center, closer to the camera than her "
                                "face; her face fills the upper half. The table is empty. The background is reduced by "
                                "framing, never by blur."),
                   camera="phone held at chest height about 25 centimeters from the bun, standard 1x lens, level",
                   state=f"Start frame: the bun is raised and its crust is clearly visible. {n} is {boca}.",
                   negative=NEG_BASE + NEG_RECEITA),
        "T7": dict(ref=ref_base,
                   prop=("She holds a golden-brown bun torn open in two halves, one half in each hand, side by side in "
                         "front of her chest, showing a soft airy fluffy crumb with small holes."),
                   posture=f"{n} stands behind {MESA}, seen from the chest up, the two halves held toward the camera.",
                   composition=("Close shot from chest height: the phone lens is about 20 centimeters from the two halves, "
                                "which fill about 40 percent of the frame in the lower center, closer to the camera than her "
                                "face; her face fills the upper half. The table is empty. The background is reduced by "
                                "framing, never by blur."),
                   camera="phone held at chest height about 20 centimeters from the buns, standard 1x lens, level",
                   state=f"Start frame: the two torn halves are side by side and the crumb is clearly visible. {n} is {boca}.",
                   negative=NEG_BASE + NEG_RECEITA),
        "T8": dict(ref=ref_base, prop=f"In her low right hand she holds {PAO}, held low at the bottom of the frame.",
                   posture=f"{n} stands in her garage gym in front of the whiteboard, seen from the chest up, one arm extended holding the phone.",
                   composition=comp_selfie, camera=cam_selfie,
                   state=f"Start frame: {n} is {boca}, sincere and close.", negative=NEG_BASE),
        "T9": dict(ref=ref_base, prop=f"In her low right hand she holds {PAO}, lowered and relaxed at the bottom of the frame.",
                   posture=f"{n} stands in her garage gym in front of the whiteboard, seen from the chest up, one arm extended holding the phone.",
                   composition=comp_selfie, camera=cam_selfie,
                   state=f"Start frame: {n} is {boca}, warm and sure of herself.", negative=NEG_BASE),
        "T10": dict(ref=ref_base, prop="Her hands are empty and out of frame.",
                    posture=f"{n} stands in her garage gym in front of the whiteboard, seen from the chest up, one arm extended holding the phone, her head tilted slightly.",
                    composition=("Selfie shot: the phone lens is about 45 centimeters from her face; her face and shoulders "
                                 "fill the frame down to the chest and her extended forearm crosses the lower-left corner, "
                                 "closer to the camera than her face. The background is reduced by framing, never by blur."),
                    camera="phone held at arm's length at eye height about 45 centimeters from her face, standard 1x lens, level, slightly handheld",
                    state=f"Start frame: {n} is {boca}, curious, with a hint of a question in her eyes.", negative=NEG_BASE),
        "T11": dict(ref=ref_prod,
                    prop=(f"Raised with both hands in front of her chest, she holds {POTE}. The label is turned "
                          "straight to the lens and fully readable, her fingers only on the sides of the jar."),
                    posture=f"{n} stands behind {MESA}, seen from the waist up, holding the jar toward the camera.",
                    composition=("Straight-on medium shot from table height: the phone lens is about 40 centimeters "
                                 "from the jar, which fills about 25 percent of the frame in the lower center, closer "
                                 "to the camera than her face; her face and shoulders fill the upper half. The table "
                                 "is empty. The background is reduced by framing, never by blur."),
                    camera="phone propped at table height about 40 centimeters from the jar, standard 1x lens, level",
                    state=f"Start frame: {n} is smiling and {boca}.", negative=neg_pote),
        "T12": dict(ref=ref_prod,
                    prop=(f"Perfectly still with both hands in front of her chest, centered, she holds {POTE}. The "
                          "label is turned straight to the lens, fully readable and with nothing covering it."),
                    posture=f"{n} stands behind {MESA}, seen from the waist up, holding the jar toward the camera.",
                    composition=("Straight-on medium shot from table height: the phone lens is about 40 centimeters "
                                 "from the jar, which fills about 25 percent of the frame in the lower center, closer "
                                 "to the camera than her face; her face and shoulders fill the upper half. The table "
                                 "is empty. The background is reduced by framing, never by blur."),
                    camera="phone propped at table height about 40 centimeters from the jar, standard 1x lens, level",
                    state=f"Start frame: {n} is {boca}, warm and inviting.", negative=neg_pote),
        "T13": dict(ref=ref_prod,
                    prop=(f"Perfectly still with both hands in front of her chest, centered, she holds {POTE}. The "
                          "label is turned straight to the lens, fully readable and with nothing covering it."),
                    posture=f"{n} stands behind {MESA}, seen from the chest up, holding the jar toward the camera.",
                    composition=("The tightest shot of the video, straight-on from chest height: the phone lens is "
                                 "about 35 centimeters from the jar, which fills about 30 percent of the frame in the "
                                 "lower center, closer to the camera than her face; her face fills the upper half. "
                                 "The background is reduced by framing, never by blur."),
                    camera="phone propped at chest height, standard 1x lens, level",
                    state=f"Start frame: {n} is {boca}, clear and calm.", negative=neg_pote),
    }
    out = []
    for i, t in enumerate(TAKES, 1):
        d = ks[t]
        cod = f"K{i:02d}"
        j = {
            "shot_id": f"{cod}_{t.lower()}_{a['arquivo'].lower()}",
            "fiction_note": FICCAO,
            "reference_use": d["ref"],
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
            "negative": d["negative"],
        }
        out.append(dict(codigo=cod, take=t, titulo=TITULOS[t], j=j))
    return out


def videos(a):
    n = a["nome"]
    vs = []
    for i, t in enumerate(TAKES, 1):
        acao = ACOES[t].format(n=n)
        if t in VOZ_OVER:
            linha1 = (f"a voz da avatar {n}, fora de quadro (voz-over, ela não aparece falando), em inglês com sotaque "
                      f"americano {a['sotaque']}, {a['voz']}, {EMOCAO[t]}, diz a seguinte frase: \"{FALAS[t]}\"")
            linha2 = ("a voz diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por "
                      "inteiro sem cortar no final. Nenhuma boca visível no quadro.")
        else:
            linha1 = (f"a avatar {n}, mulher, fala em inglês com sotaque americano {a['sotaque']}, {a['voz']}, "
                      f"{EMOCAO[t]}, voz autêntica, como se exigisse ser ouvida, a seguinte frase: \"{FALAS[t]}\"")
            linha2 = ("a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por "
                      "inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.")
        txt = (f"{linha1}\n\n{linha2}\n\n"
               f"o que acontece no vídeo: {acao}\n\n"
               f"câmera: {CAMERA.get(t, 'fixa')}\n\n"
               f"som ambiente: {a['som']}{SOM_EXTRA.get(t, '')}, sem música")
        vs.append((f"V{i:02d}", t, f"K{i:02d}", txt))
    return vs


# ---------------------------------------------------------------- ficha do frame
EV_COMUM = {
    "G1": '"Neutral overcast daylight"',
    "G2": "N/A | janela fora do quadro, só a luz entra; nenhum céu em quadro",
    "G3": '"everything in sharp focus"',
    "G4": '"Real skin with visible pores"',
    "G5": '"no warm orange color cast"',
    "G6": '"no captions"',
    "G7": '"small American flag"',
    "G8": '"caught mid-sentence"',
}
_SELFIE = dict(quadro="rosto e ombros enchem o quadro; o pãozinho na mão baixa no canto de baixo à esquerda",
               dist="uns 50 cm do rosto", camera="selfie de braço estendido, lente 1x reta",
               f2='"the bun in her low hand sits in the lower-left corner"', f3='"about 50 centimeters from her face"',
               f4='"phone held at arm\'s length at eye height about 50 centimeters from her face, standard 1x lens"',
               f5='"one arm extended holding the phone"', f6="N/A | o quadro tem só ela e o pãozinho; o fundo vem da âncora")
FICHA = {
    "K01": dict(heroi="a tigela de vidro colada na lente com as batatas cozidas e o espremedor de aço, ele amassando",
                termos=['"large clear glass mixing bowl"', '"stainless steel potato masher"'],
                quadro="a tigela ocupa uns 50% de baixo, quase de borda a borda; ele inclinado atrás, rosto e ombros no alto",
                dist="uns 30 cm da tigela", camera="celular na altura do peito, lente 1x levemente para baixo",
                pose="inclinado sobre a bancada, punho no espremedor",
                lista="tigela com batatas, espremedor, apresentador, fundo",
                frame0="o espremedor pressionado na batata, tigela ainda sem abacate, ovo ou iogurte",
                desvio="cozinha de madeira e boné → mesa preta do box (avatar fixo); regata branca igual",
                f2='"fills the lower 50 percent of the frame"', f3='"about 30 centimeters from the bowl"',
                f4='"standard 1x lens tilted slightly down"', f5='"leaning forward over it"',
                f6='"Nothing else is on the table"'),
    "K02": dict(heroi="as mãos moldando a bolinha de massa clara, com a assadeira de bolinhas ao lado",
                termos=['"one smooth pale dough ball"', '"rectangular silver metal baking tray"'],
                quadro="as mãos ocupam uns 50% de baixo; só pescoço, peito e braços no quadro, sem rosto",
                dist="uns 30 cm das mãos", camera="celular na altura do peito, lente 1x levemente para baixo",
                pose="inclinada, mãos moldando a bolinha", lista="mãos, bolinha de massa, assadeira, tronco, fundo",
                frame0="a bolinha lisa nas mãos em concha",
                desvio="tábua de cortar e camiseta branca → mesa preta do box; sem rosto, como no modelo",
                f2='"fill the lower 50 percent of the frame"', f3='"about 30 centimeters from her hands"',
                f4='"standard 1x lens tilted slightly down"', f5='"bent slightly forward"',
                f6='"Nothing else is on the table"'),
    "K03": dict(heroi="a assadeira com seis bolinhas colada na lente e a mão dela polvilhando gergelim",
                termos=['"rectangular silver metal baking tray"', '"white sesame seeds"'],
                quadro="a assadeira ocupa uns 45% de baixo, quase de borda a borda; ela atrás, rosto e ombros no alto",
                dist="uns 35 cm da assadeira", camera="celular na altura do peito, lente 1x levemente para baixo",
                pose="inclinada sobre a bancada, mão direita pinçando gergelim",
                lista="assadeira com bolinhas, mão com gergelim, apresentadora, fundo",
                frame0="poucos grãos de gergelim já sobre as bolinhas, ela sorrindo",
                desvio="cozinha branca e boné → mesa preta do box (avatar fixo)",
                f2='"fills the lower 45 percent of the frame"', f3='"about 35 centimeters from the tray"',
                f4='"standard 1x lens tilted slightly down"', f5='"leaning forward over it"',
                f6='"Nothing else is on the table"'),
    "K04": dict(heroi="o forno elétrico de bancada de porta aberta e a assadeira entrando, ela de perfil",
                termos=['"silver countertop electric oven"', '"rectangular silver metal baking tray"'],
                quadro="forno e assadeira ocupam uns 40% de baixo à esquerda; ela no meio do quadro, coxa pra cima",
                dist="uns 70 cm do forno, 1,2 m dela", camera="celular apoiado na altura da bancada, lente 1x reta",
                pose="de pé, de perfil, inclinada, deslizando a assadeira", lista="forno, assadeira, apresentadora, fundo",
                frame0="a assadeira meio dentro do forno",
                desvio="forno embutido da cozinha → forno elétrico de bancada sobre a mesa preta (declarado no roteiro)",
                f2='"fill the lower 40 percent of the frame"', f3='"about 70 centimeters from the lens"',
                f4='"phone propped at table height about 1.2 meters from her, standard 1x lens"',
                f5='"stands in profile at the left end of the table"', f6="N/A | o quadro tem ela, o forno e a assadeira; o fundo vem da âncora"),
    "K05": dict(heroi="a assadeira de pãezinhos dourados no colo, inclinada para a lente",
                termos=['"rectangular silver metal baking tray"', '"six golden-brown buns"'],
                quadro="a assadeira ocupa uns 35% de baixo; rosto e ombros nos dois terços de cima",
                dist="uns 80 cm dela", camera="celular apoiado na altura da bancada, lente 1x reta",
                pose="sentada na beira da mesa, assadeira no colo", lista="assadeira com pães, apresentadora, fundo",
                frame0="os pães dourados bem visíveis", desvio="bancada de cozinha → mesa preta do box (avatar fixo)",
                f2='"fills the lower 35 percent of the frame"', f3='"about 80 centimeters from her"',
                f4='"phone propped at table height about 80 centimeters from her, standard 1x lens"',
                f5='"sits on the edge of the black table in front of her"', f6="N/A | o quadro tem ela e a assadeira; o fundo vem da âncora"),
    "K06": dict(heroi="um pãozinho dourado erguido com as duas mãos quase na lente",
                termos=['"one round golden-brown bun with a shiny crust"'],
                quadro="o pão ocupa uns 35% de baixo no centro; rosto na metade de cima",
                dist="uns 25 cm do pão", camera="celular na altura do peito, lente 1x reta",
                pose="de pé atrás da mesa, pão erguido com as duas mãos", lista="pãozinho, mãos, apresentadora, fundo",
                frame0="pão erguido, crosta visível", desvio="sala de estar e boné → box (avatar fixo)",
                f2='"fills about 35 percent of the frame"', f3='"about 25 centimeters from the bun"',
                f4='"phone held at chest height about 25 centimeters from the bun, standard 1x lens"',
                f5='"Raised with both hands in front of her chest"', f6='"The table is empty"'),
    "K07": dict(heroi="o pão aberto ao meio, as duas metades coladas na lente, miolo aerado",
                termos=['"torn open in two halves"', '"soft airy fluffy crumb"'],
                quadro="as metades ocupam uns 40% de baixo no centro; rosto na metade de cima",
                dist="uns 20 cm das metades", camera="celular na altura do peito, lente 1x reta",
                pose="de pé atrás da mesa, uma metade em cada mão", lista="duas metades de pão, mãos, apresentadora, fundo",
                frame0="as duas metades lado a lado, miolo visível", desvio="sala de estar e boné → box (avatar fixo)",
                f2='"fill about 40 percent of the frame"', f3='"about 20 centimeters from the two halves"',
                f4='"phone held at chest height about 20 centimeters from the buns, standard 1x lens"',
                f5='"one half in each hand"', f6='"The table is empty"'),
    "K08": dict(_SELFIE, heroi="selfie dela com o pãozinho dourado na mão baixa",
                termos=['"one round golden-brown bun with a shiny crust"'], pose="selfie de braço estendido",
                lista="apresentadora, pãozinho, fundo", frame0="falando, o pão na mão baixa",
                desvio="sala e boné → garagem-box (avatar fixo)"),
    "K09": dict(_SELFIE, heroi="selfie dela, pãozinho baixo na mão, aceno de cabeça no fim",
                termos=['"one round golden-brown bun with a shiny crust"'], pose="selfie de braço estendido",
                lista="apresentadora, pãozinho, fundo", frame0="falando, o pão relaxado na mão baixa",
                desvio="no modelo a fala é do CTA (mesmo plano); este take é a rota 6 aprovada no roteiro"),
    "K10": dict(heroi="selfie dela de mãos vazias, cabeça inclinada, a pergunta no ar",
                termos=['"Her hands are empty and out of frame"'],
                quadro="rosto e ombros enchem o quadro; o antebraço estendido cruza o canto de baixo à esquerda",
                dist="uns 45 cm do rosto", camera="selfie de braço estendido, lente 1x reta",
                pose="selfie de braço estendido, cabeça inclinada", lista="apresentadora, fundo",
                frame0="falando, cabeça levemente inclinada",
                desvio="no modelo a fala é do CTA (mesmo plano); este take é a virada aprovada no roteiro",
                f2='"her extended forearm crosses the lower-left corner"', f3='"about 45 centimeters from her face"',
                f4='"phone held at arm\'s length at eye height about 45 centimeters from her face, standard 1x lens"',
                f5='"one arm extended holding the phone"', f6="N/A | o quadro tem só ela; o fundo vem da âncora"),
}
for _k, _quadro, _dist, _f2, _f3, _f4, _pose in (
        ("K11", "pote nuns 25% no centro de baixo (o modelo não tem produto; mesmo plano de selfie, mais perto)", "uns 40 cm do pote",
         '"fills about 25 percent of the frame"', '"about 40 centimeters from the jar"',
         '"phone propped at table height about 40 centimeters from the jar, standard 1x lens"',
         '"Raised with both hands in front of her chest"'),
        ("K12", "pote nuns 25% no centro de baixo, parado", "uns 40 cm do pote",
         '"fills about 25 percent of the frame"', '"about 40 centimeters from the jar"',
         '"phone propped at table height about 40 centimeters from the jar, standard 1x lens"',
         '"Perfectly still with both hands"'),
        ("K13", "pote nuns 30% no centro de baixo, o plano mais fechado do vídeo", "uns 35 cm do pote",
         '"fills about 30 percent of the frame"', '"about 35 centimeters from the jar"',
         '"phone propped at chest height, standard 1x lens"', '"Perfectly still with both hands"')):
    FICHA[_k] = dict(heroi="o pote de Natural Rems Sea Moss no lugar do pãozinho, rótulo de frente para a lente",
                     termos=['"short wide jar of dark amber plastic with a black screw cap"', '"Sea Moss Gummies"'],
                     quadro=_quadro, dist=_dist, camera="celular na altura da bancada/peito, lente 1x reta",
                     pose="em pé atrás da mesa, segurando o pote na frente do peito",
                     lista="apresentadora, pote, fundo", frame0="pote já na mão, rótulo legível, ela falando",
                     desvio="sem produto no modelo → pote do Natural Rems Sea Moss (oferta e CTA da marca, aprovados no roteiro)",
                     f2=_f2, f3=_f3, f4=_f4, f5=_pose,
                     f6="N/A | o quadro tem só ela e o pote; o fundo vem da âncora")


def ficha(ks):
    L = ["# FICHA DO FRAME · brandon_seamoss_paes_abacate", "",
         "Regra e método: `GATE_VISUAL.md` Parte 6. Cada K sai daqui, nunca da memória. O frame do modelo manda no",
         "CONTEÚDO (forma, quadro, distância, câmera, pose, o que está em quadro); o gate manda no ACABAMENTO e impõe o",
         "piso de proximidade do herói. A evidência de cada OK é um trecho que existe literalmente no K.",
         "Gerada por `gerar_pacote.py`, que confere cada evidência contra o texto do K antes de escrever.", ""]
    for k in ks:
        cod, txt = k["codigo"], json.dumps(k["j"], ensure_ascii=False)
        f = FICHA[cod]
        fala = k["take"] in FALAS and k["take"] not in VOZ_OVER
        itens = [("F1 forma do heroi", " · ".join(f["termos"])), ("F2 quanto do quadro", f["f2"]),
                 ("F3 distancia da lente", f["f3"]), ("F4 camera", f["f4"]), ("F5 pose do avatar", f["f5"]),
                 ("F6 lista fechada", f["f6"]), ("G1 luz neutra", EV_COMUM["G1"]), ("G2 ceu ou janela", EV_COMUM["G2"]),
                 ("G3 foco", EV_COMUM["G3"]), ("G4 realismo", EV_COMUM["G4"]), ("G5 sem tom quente", EV_COMUM["G5"]),
                 ("G6 sem texto", EV_COMUM["G6"]), ("G7 bandeira", EV_COMUM["G7"]),
                 ("G8 boca no K de fala", EV_COMUM["G8"] if fala else "N/A | take sem fala em quadro (voz-over ou sem rosto)")]
        L += [f"## {cod}", f"Frame: `{frame_modelo(cod)}`", f"Take: {k['take']}", f"Herói: {f['heroi']}",
              "Termos de forma: " + " · ".join(f["termos"]), f"Quadro: {f['quadro']}",
              f"Distância da lente: {f['dist']}", f"Câmera: {f['camera']}", f"Pose: {f['pose']}",
              f"Lista fechada: {f['lista']}", f"Frame 0: {f['frame0']}",
              f"Desvio (acabamento ou avatar fixo): {f['desvio']}", "",
              "| Item | Status | Evidência (trecho literal do K) |", "|---|---|---|"]
        for q in re.findall(r'"([^"]+)"', " ".join(f["termos"])):
            assert q in txt, (cod, "termo", q)
        for nome, ev in itens:
            if ev.startswith("N/A |"):
                L.append(f"| {nome} | N/A | {ev[5:].strip()} |")
            else:
                for q in re.findall(r'"([^"]+)"', ev):
                    assert q in txt, (cod, nome, q)
                L.append(f"| {nome} | OK | {ev} |")
        L.append("")
    return "\n".join(L)


def texto_flow(j):
    """Prompt de imagem de EXECUCAO, em JSON (contrato do Flow v17): sem shot_id, com o formato na frente."""
    ordem = ["fiction_note", "reference_use", "identity_main", "wardrobe", "scene", "prop", "posture",
             "composition", "camera", "lighting", "state", "realism", "aspect_ratio", "negative"]
    assert set(ordem) == set(j) - {"shot_id"}, set(j) ^ set(ordem)
    d = {"format": "IMPORTANT: THIS IS IPHONE FOOTAGE. Vertical 9:16."}
    d.update({k: j[k] for k in ordem})
    return json.dumps(d, ensure_ascii=False, indent=2)


def anexos(a, k):
    n = 3 if k["take"] in COM_PRODUTO else 2
    L = [f"> ### 📎 ANEXAR: **{n} IMAGENS**",
         f"> **1️⃣ ÂNCORA HOLISTIC BRANDON** `{a['ancora']}`",
         f"> **2️⃣ FRAME DO MODELO, só composição** `{frame_modelo(k['codigo'])}`"]
    if n == 3:
        L.append(f"> **3️⃣ FOTO DO POTE NATURAL REMS, só o pote da frente** `{PRODUTO_IMG}`")
    return "\n".join(L + [">", "> ### 🆕 GERAR DO ZERO"])


def titulo_anexo(k):
    base = "ÂNCORA HOLISTIC BRANDON + FRAME DO MODELO"
    return base + (" + FOTO DO POTE" if k["take"] in COM_PRODUTO else "")


def capcut():
    return [
        "1. Clipes numerados na ordem: V01 a V13.",
        "2. Cortar cada clipe no tempo da cena do modelo: " + "; ".join(f"V{t[1:].zfill(2)} {MOMENTO[t]}" for t in TAKES) + ".",
        "3. Zero tempo morto: todo clipe começa já falando. Isolate Voice / Keep Vocal no áudio.",
        "4. V02 e V04 são B-roll com voz-over da avatar fora de quadro: a voz já vem gerada no próprio clipe. Se alguma ficar fraca, cortar o áudio dela do clipe vizinho do mesmo tom.",
        "5. Dentro do V01 (a receita inteira em um clipe), jump cuts curtos de ritmo como no modelo, se quiser; o clipe é contínuo.",
        "6. V13 inteiro, sem corte e sem nada cobrindo o pote: é o CTA da marca (frasco parado e legível enquanto o nome é dito). O vídeo acaba nele.",
        "7. Legenda de tela como no modelo: serifada branca, palavra a palavra, no meio do quadro, com a palavra carregada maior; no começo do V01, \"mash one boiled potato\".",
        "8. Sem Voice Changer: a voz vem do prompt de cada V.",
        "9. Música só depois do gancho (a partir do V02), nunca no pré-gancho, entre -19 e -20 dB, fora da biblioteca do TikTok.",
        "10. Rótulo pequeno `Synthetic performer` num canto do vídeo.",
        "11. Legenda do post: `#ad #syntheticperformer #naturalrems` na primeira linha e o link da Amazon logo abaixo; chave de conteúdo de IA ligada na plataforma.",
    ]


def transcricao():
    L = ["| Take | English | Português |", "|---|---|---|"]
    for t in TAKES:
        L.append(f"| {t} | {FALAS[t]} | {TRANSCRICAO_PT[t]} |")
    return L


def pacote(a):
    ks, vs = keyframes(a), videos(a)
    L = ["# holistic.brandon | Ângulo 1 Natural Rems Sea Moss | Pãezinhos de batata com abacate | Pacote de Prompts", "",
         "Vídeo modelo: `input/reference_video.mp4` (36,9 s, pessoa real)", "",
         f"Âncora: `{a['ancora']}` · Foto do produto: `{PRODUTO_IMG}`", "",
         "Funil: venda Amazon. Frasco em quadro, \"Search Natural Rems Sea Moss on Amazon\" primeiro, link da "
         "legenda do post depois, fim. Rodada de validação, gancho fiel ao modelo.", "",
         "## Índice de geração", "",
         "| Take | Keyframe | Anexar | Ação |", "|---|---|---|---|"]
    for k in ks:
        L.append(f"| {k['take']} | {k['codigo']} | {titulo_anexo(k)} ({k['codigo']}) | GERAR DO ZERO |")
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
          f"- Gancho: {TIGELA} com três batatas cozidas e um espremedor de aço; a receita entra dentro do V01 (abacate, ovos, iogurte, fermento, sal, colher de madeira).",
          f"- Receita: {ASSADEIRA} com bolinhas de massa e depois pãezinhos dourados com gergelim; um forno elétrico de bancada pequeno sobre a mesa preta (T4); {PAO}.",
          f"- Produto (T11 a T13): {POTE}. Referência: `{PRODUTO_IMG}`, só o pote da frente, sem a faixa MADE IN USA, sem o pote de trás e sem as gomas soltas.",
          "- Nada da receita tem marca legível.", "",
          "## Trava da 2ª pessoa (REF-A)", "", "- Não se aplica: não há 2ª pessoa.", "",
          "## Prompts de imagem", ""]
    for k in ks:
        L += [f"## {k['codigo']} · {k['take']} · GERAR DO ZERO · {titulo_anexo(k)}", "",
              anexos(a, k), "", f"Cena: {k['titulo']}.", "", "```json",
              json.dumps(k["j"], ensure_ascii=False, indent=2), "```", ""]
    L += ["## Bloco global de vídeo", "", "```text",
          f"a avatar {a['nome']}, mulher, fala em inglês com sotaque americano {a['sotaque']}, {a['voz']}, "
          "[emoção da fala], voz autêntica, como se exigisse ser ouvida, a seguinte frase: \"[FALA EXATA DO ROTEIRO]\"", "",
          "a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.", "",
          "o que acontece no vídeo: [ação enxuta]", "", "câmera: [fixa / leve handheld]", "", f"som ambiente: {a['som']}, sem música",
          "```", "", "# Prompts de vídeo", ""]
    for cod, take, kcod, txt in vs:
        L += [f"### {cod} · {take} · usa {kcod}", "", "```text", txt, "```", ""]
    L += ["## Mapa de âncoras", "", "| Keyframe | Referências a anexar | Modelo |", "|---|---|---|"]
    for k in ks:
        extra = f" + `{PRODUTO_IMG}` (só o pote da frente)" if k["take"] in COM_PRODUTO else ""
        L.append(f"| {k['codigo']} | ÂNCORA HOLISTIC BRANDON + `{frame_modelo(k['codigo'])}` (só composição){extra} | Nano Banana 2, 9:16 |")
    L += ["", "## Montagem no CapCut", ""] + capcut() + [
          "", "## Gates de qualidade", "",
          "1. Fala de cada V igual ao ROTEIRO, palavra por palavra.",
          "2. Um take por cena do modelo; nenhum take acima de 29 palavras.",
          "3. Bandeira dos EUA no campo scene de todo K.",
          "4. Zero travessão.",
          "5. CTA da marca no T13: Search Natural Rems Sea Moss on Amazon, depois o link da legenda, e fim.",
          "6. Pote em quadro de T11 a T13, rótulo legível; no T13 parado do começo ao fim.",
          "7. Nada médico em quadro nem na fala; sem antes e depois; sem cura nem tratamento.",
          "8. Negative sem termo sensível.",
          "9. GATE_VISUAL Partes 1 a 3 em todo K: herói colado na lente, luz neutra, sem tom quente, sem blur, trecho de realismo.",
          "10. Gancho fiel no conteúdo: a tigela de vidro colada na lente com a batata sendo amassada, falado desde o segundo 0.",
          "11. Um K = um V; o abacate, os ovos, o iogurte e a mistura nascem dentro do V01.", ""]
    flow = ["# Blocos limpos para o Google Flow | holistic.brandon", "", "Fonte interna: `PROMPTS_BRANDON.md`",
            "No chat, cada K e cada V sai no seu próprio bloco (workflow oficial). Este arquivo é só apoio.", "",
            "## BLOCO DE IMAGEM", "", "```text"]
    for k in ks:
        flow += [k["codigo"], texto_flow(k["j"]), ""]
    flow += ["```", "", "## BLOCO DE VÍDEO", "", "```text"]
    for cod, _, _, txt in vs:
        flow += [cod, txt, ""]
    flow += ["```", "", "## Tabela de leitura humana", "", "| Código | Take | Anexar |", "|---|---|---|"]
    for k in ks:
        extra = f" + `{PRODUTO_IMG}`" if k["take"] in COM_PRODUTO else ""
        flow.append(f"| {k['codigo']} / V{k['codigo'][1:]} | {k['take']}, {k['titulo']} | ÂNCORA + `{frame_modelo(k['codigo'])}`{extra} |")
    flow += ["", "## Transcrição final por take", ""] + transcricao()
    return "\n".join(L) + "\n", "\n".join(flow) + "\n"


AVATARES = [A]


def main():
    p, f = pacote(A)
    (AQUI / "PROMPTS_BRANDON.md").write_text(p, encoding="utf-8")
    (AQUI / "FLOW_BRANDON.md").write_text(f, encoding="utf-8")
    (AQUI / "PROMPTS_PRODUCAO.md").write_text(p, encoding="utf-8")
    (AQUI / "FICHA_FRAMES.md").write_text(ficha(keyframes(A)), encoding="utf-8")
    print("ok: pacote da Brandon; PROMPTS_PRODUCAO.md = holistic.brandon; FICHA_FRAMES.md com %d K" % len(TAKES))


if __name__ == "__main__":
    main()
