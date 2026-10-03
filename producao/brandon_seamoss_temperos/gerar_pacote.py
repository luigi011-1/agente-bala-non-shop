"""Gera o pacote da producao brandon_seamoss_temperos (Angulo 1, Natural Rems Sea Moss, venda, validacao).

Fonte unica da fala: ROTEIRO.md v2 aprovado em 2026-10-03 (lido do disco, nunca redigitado). Identidade,
roupa e cenario: a ancora aprovada (avatar fixo por conta). Medidas de cada K: os frames do modelo em
input/frames_modelo/, registradas em FICHA_FRAMES.md, que este script tambem escreve, com a evidencia
de cada OK conferida contra o texto do K (assert). Gabarito: brandon_seamoss_coxas/gerar_pacote.py.

Prompt de imagem entregue em JSON (contrato do Flow v17). Origem organica: copy literal do T1 ao T7.
Produto em quadro so no T9 e no T10, com a foto oficial do pote como terceiro anexo.

Saidas: PROMPTS_BRANDON.md, FLOW_BRANDON.md, PROMPTS_PRODUCAO.md (copia do avatar ACTIVE) e
FICHA_FRAMES.md. No chat, a entrega sai com um bloco de codigo por K e por V (workflow oficial,
memoria feedback-prompts-na-conversa).

Uso: python3 gerar_pacote.py
"""
import json
import re
from pathlib import Path

AQUI = Path(__file__).resolve().parent
ROTEIRO = (AQUI / "ROTEIRO.md").read_text(encoding="utf-8")

HEADS = dict(re.findall(r"^### (T\d+) · (.+)$", ROTEIRO, re.M))
TAKES = list(HEADS)
assert TAKES == ["T%d" % i for i in range(1, 11)], TAKES
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
COM_PRODUTO = {"T9", "T10"}

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
            "no beauty smoothing, no visible phone, no eyeglasses, no gray t-shirt, no kitchen cabinets, no white marble "
            "counter, no cartoon magnet, no silver cross, no white coat, no second person")
NEG_RECEITA = ", no readable lettering on the tank, glasses, spoons or jars"

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
AQUARIO = "a clear rectangular glass tank, like a small empty aquarium, filled with cold clear water"
COPOS = "two tall clear drinking glasses side by side"
POTE = ("the Natural Rems Sea Moss Gummies jar exactly as in the attached product photo: a short wide jar of dark "
        "amber plastic with a black screw cap, a pale sage-green label with dark green text, the Natural Rems logo "
        "with three leaves at the top, the big title Sea Moss Gummies, a pill-shaped badge reading 6000 MG | 16-IN-1, "
        "the line GREEN APPLE FLAVOR, two columns of dark green ingredient pills, green seaweed illustrations on the "
        "sides and a small 30 Gummies badge")
FILEIRA = ("lined up on the table: two small clear glasses of water, two cinnamon sticks, a small pile of black "
           "peppercorns and one potato")

EMOCAO = {
    "T1": "entonação intrigante, como quem vai provar algo agora",
    "T2": "entonação de denúncia, indignada na medida",
    "T3": "entonação didática e rápida",
    "T4": "entonação didática, marcando dyed",
    "T5": "entonação didática e segura",
    "T6": "entonação cúmplice, sorrindo em the cheap one",
    "T7": "entonação calma e confiante",
    "T8": "entonação próxima e sincera, como quem conta um hábito",
    "T9": "entonação calorosa e confiante",
    "T10": "entonação clara e pausada, dizendo Natural Rems Sea Moss devagar e por inteiro",
}
ACOES = {
    "T1": ("{n} vira as duas colheres de pimenta-do-reino dentro do aquário de água fria; os grãos caem e a maioria "
           "afunda devagar até o fundo."),
    "T2": "{n} aponta com o indicador para os grãos que ficaram boiando na superfície da água.",
    "T3": "{n} solta as duas batatas na água do aquário; uma afunda até o fundo e a outra fica boiando.",
    "T4": ("{n} mexe uma colher de cúrcuma em cada copo: no copo da esquerda o pó assenta devagar no fundo, no da "
           "direita a água fica amarela forte na hora."),
    "T5": ("{n} vira as colheres de café nos dois copos: no da esquerda o pó fica por cima da água, no da direita ele "
           "afunda soltando fios marrons."),
    "T6": "{n} mostra as duas canelas bem perto da câmera e depois aproxima a da direita.",
    "T7": "{n}, atrás da mesa com os ingredientes, abre as mãos com as palmas para cima enquanto fala.",
    "T8": "{n} passa a mão aberta por cima dos ingredientes enfileirados na mesa quando diz separate jars.",
    "T9": ("{n} segura o pote de Natural Rems Sea Moss com as duas mãos na altura do peito, rótulo de frente para a "
           "câmera, e aproxima o pote um pouco da câmera quando diz o nome."),
    "T10": ("{n} segura o pote parado com as duas mãos, rótulo de frente e legível, sem nada cobrindo, do começo ao "
            "fim; só o rosto e a boca se mexem."),
}
CAMERA = {t: "leve handheld" for t in ("T1", "T2", "T3", "T4", "T5", "T6")}
SOM_EXTRA = {"T1": ", grãos caindo na água", "T3": ", batatas caindo na água", "T4": ", colher batendo no vidro",
             "T5": ", colher batendo no vidro"}
MOMENTO = {"T1": "0,0 a 5,7 s", "T2": "5,7 a 9,6 s", "T3": "9,6 a 17,1 s", "T4": "17,1 a 25,0 s",
           "T5": "25,0 a 32,7 s", "T6": "32,7 a 40,2 s", "T7": "a fala inteira", "T8": "a fala inteira",
           "T9": "a fala inteira", "T10": "o CTA inteiro, sem corte"}
TITULOS = {"T1": "gancho, pimenta no aquário colado na lente", "T2": "pimenta no fundo, alguns grãos boiando",
           "T3": "batatas sobre o aquário", "T4": "cúrcuma nos dois copos", "T5": "café nos dois copos",
           "T6": "close das duas canelas", "T7": "plano aberto, autoridade", "T8": "plano aberto, transição",
           "T9": "pote sobe no nome", "T10": "CTA, pote parado e legível"}


def keyframes(a):
    n = a["nome"]
    boca = "caught mid-sentence, lips naturally parted, animated expression, looking straight into the lens"
    ref_base = (f"Use the first attached image only for {n}'s exact identity, wardrobe and her own garage gym. Use the "
                "second attached image only as a composition reference for the camera position, framing and the "
                "action; do not copy its man, his eyeglasses, his gray t-shirt, kitchen, marble counter, cartoon magnet or the "
                "caption text.")
    ref_prod = (ref_base + " Use the third attached image only for the exact look of the front jar and its label; "
                "ignore the MADE IN USA banner, the second jar with the Supplement Facts panel and the loose gummies.")
    post_mesa = f"{n} stands behind {MESA}, leaning forward over it, seen from the waist up."
    cam_mesa = "phone held at chest height about 35 centimeters from the tank, standard 1x lens tilted slightly down"
    comp_tanque = ("Close shot from chest height: the phone lens is about 35 centimeters from the tank, which fills the "
                   "lower 40 percent of the frame almost edge to edge, closer to the camera than her face; her face "
                   "and shoulders fill the upper part. Nothing else is on the table. The background is reduced by "
                   "framing, never by blur.")
    cam_copos = "phone held at chest height about 30 centimeters from the glasses, standard 1x lens tilted slightly down"
    comp_copos = ("Close shot from chest height: the phone lens is about 30 centimeters from the glasses, which fill the "
                  "lower 35 percent of the frame, closer to the camera than her face; her face fills the upper part. "
                  "Nothing else is on the table. The background is reduced by framing, never by blur.")
    post_aberto = (f"{n} stands upright behind {MESA}, seen from the thighs up, her hands open above the table.")
    cam_aberto = "phone propped at table height about 1 meter from her, standard 1x lens, level"
    comp_aberto = ("Straight-on wide shot from table height: the phone lens is about 60 centimeters from the ingredients and about 1 meter from her; the ingredients on "
                   "the table fill the lower 30 percent of the frame, closer to the camera than her face, and she "
                   "fills the upper two thirds from the thighs up. Nothing else is on the table. The background is "
                   "reduced by framing, never by blur.")
    cam_pote = "phone propped at table height about 40 centimeters from the jar, standard 1x lens, level"
    neg_pote = NEG_BASE + ", no second jar, no loose gummies, no banner on the jar, no fingers over the label"
    ks = {
        "T1": dict(ref=ref_base,
                   prop=(f"{AQUARIO[0].upper()}{AQUARIO[1:]}, standing on {MESA} very close to the lens, the water "
                         "clean and empty. In each hand she holds a metal spoon heaped with whole black peppercorns, "
                         "both spoons tilted right above the water."),
                   posture=post_mesa, composition=comp_tanque, camera=cam_mesa,
                   state=f"Start frame: the first peppercorns are just tipping off the spoons. {n} is {boca}.",
                   negative=NEG_BASE + NEG_RECEITA + ", no peppercorns in the water yet"),
        "T2": dict(ref=ref_base,
                   prop=(f"{AQUARIO[0].upper()}{AQUARIO[1:]}, standing on {MESA} very close to the lens: most of the "
                         "black peppercorns lie on the bottom of the tank, a few lighter brown wrinkled seeds float "
                         "on the surface, and some grains are still sinking through the water. Her right index finger "
                         "points at the floating seeds; the empty spoon rests in her left hand."),
                   posture=post_mesa, composition=comp_tanque, camera=cam_mesa,
                   state=f"Start frame: the floating seeds are clearly visible on the surface. {n} is {boca}.",
                   negative=NEG_BASE + NEG_RECEITA),
        "T3": dict(ref=ref_base,
                   prop=(f"{AQUARIO[0].upper()}{AQUARIO[1:]}, standing on {MESA} very close to the lens, the water "
                         "clean. She holds one brown russet potato in each hand right above the water."),
                   posture=post_mesa, composition=comp_tanque, camera=cam_mesa,
                   state=f"Start frame: both potatoes are still in her hands, about to drop. {n} is {boca}.",
                   negative=NEG_BASE + NEG_RECEITA + ", no potatoes in the water yet"),
        "T4": dict(ref=ref_base,
                   prop=(f"{COPOS[0].upper()}{COPOS[1:]}, full of warm clear water, standing on {MESA} very close to "
                         "the lens. In each hand she holds a metal spoon heaped with bright orange turmeric powder, "
                         "dipped just into the water of each glass."),
                   posture=post_mesa, composition=comp_copos, camera=cam_copos,
                   state=f"Start frame: the water in both glasses is still clear. {n} is {boca}.",
                   negative=NEG_BASE + NEG_RECEITA + ", no yellow water yet"),
        "T5": dict(ref=ref_base,
                   prop=(f"{COPOS[0].upper()}{COPOS[1:]}, full of cold clear water, standing on {MESA} very close to "
                         "the lens. In each hand she holds a metal spoon heaped with dark brown ground coffee, held "
                         "right above each glass."),
                   posture=post_mesa, composition=comp_copos, camera=cam_copos,
                   state=f"Start frame: the coffee is still on the spoons and the water is clear. {n} is {boca}.",
                   negative=NEG_BASE + NEG_RECEITA + ", no coffee in the water yet"),
        "T6": dict(ref=ref_base,
                   prop=("In front of her face she holds two cinnamon sticks toward the lens, one in each hand: the left "
                         "one thin and tightly rolled in many paper-thin brown layers like a cigar, the right one a "
                         "single thick, hard, dark brown curl of bark."),
                   posture=f"{n} leans in close to the lens, the sticks held at mouth height on either side of her chin.",
                   composition=("Extreme close shot: the phone lens is about 15 centimeters from the cinnamon sticks, "
                                "which fill the lower 40 percent of the frame, closer to the camera than her face; her "
                                "face fills the upper part. The background is reduced by framing, never by blur."),
                   camera="phone held just below eye height about 15 centimeters from the sticks, standard 1x lens, level",
                   state=f"Start frame: both sticks are side by side and their layers are clearly visible. {n} is {boca}.",
                   negative=NEG_BASE),
        "T7": dict(ref=ref_base, prop=f"No prop in her hands. The ingredients are {FILEIRA}.",
                   posture=post_aberto + " Both palms open upward.", composition=comp_aberto, camera=cam_aberto,
                   state=f"Start frame: {n} is {boca}, calm and confident.", negative=NEG_BASE),
        "T8": dict(ref=ref_base, prop=f"No prop in her hands. The ingredients are {FILEIRA}.",
                   posture=post_aberto + " Her right hand is held open just above the ingredients.",
                   composition=comp_aberto, camera=cam_aberto,
                   state=f"Start frame: {n} is {boca}, sincere and close.", negative=NEG_BASE),
        "T9": dict(ref=ref_prod,
                   prop=(f"Raised with both hands in front of her chest, she holds {POTE}. The label is turned "
                         "straight to the lens and fully readable, her fingers only on the sides of the jar."),
                   posture=f"{n} stands behind {MESA}, seen from the waist up, holding the jar toward the camera.",
                   composition=("Straight-on medium shot from table height: the phone lens is about 40 centimeters "
                                "from the jar, which fills about 25 percent of the frame in the lower center, closer "
                                "to the camera than her face; her face and shoulders fill the upper half. The table "
                                "is empty. The background is reduced by framing, never by blur."),
                   camera=cam_pote, state=f"Start frame: {n} is smiling and {boca}.", negative=neg_pote),
        "T10": dict(ref=ref_prod,
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
_TQ = dict(quadro="o aquário ocupa uns 40% de baixo, quase de borda a borda; ele inclinado atrás, rosto e ombros no alto",
           dist="uns 35 cm do aquário", camera="celular na altura do peito, lente 1x levemente para baixo",
           f2='"fills the lower 40 percent of the frame"', f3='"about 35 centimeters from the tank"',
           f4='"standard 1x lens tilted slightly down"', f5='"leaning forward over it"',
           f6='"Nothing else is on the table"')
_CP = dict(quadro="os dois copos ocupam uns 35% de baixo, mais perto que o rosto", dist="uns 30 cm dos copos",
           camera="celular na altura do peito, lente 1x levemente para baixo",
           f2='"fill the lower 35 percent of the frame"', f3='"about 30 centimeters from the glasses"',
           f4='"standard 1x lens tilted slightly down"', f5='"leaning forward over it"',
           f6='"Nothing else is on the table"')
_AB = dict(quadro="os ingredientes ocupam uns 30% de baixo; ele de pé da coxa pra cima nos dois terços de cima",
           dist="uns 60 cm dos ingredientes, 1 m dele", camera="celular apoiado na altura da bancada, lente 1x reta",
           f2='"fill the lower 30 percent of the frame"', f3='"about 60 centimeters from the ingredients"',
           f4='"phone propped at table height about 1 meter from her, standard 1x lens"',
           f5='"stands upright behind the black table"', f6='"Nothing else is on the table"',
           termos=['"two cinnamon sticks, a small pile of black peppercorns and one potato"'],
           lista="duas canelas, dois copinhos de água, montinho de pimenta, uma batata, apresentador, fundo")
FICHA = {
    "K01": dict(_TQ, heroi="o aquário de vidro com água limpa colado na lente e as duas colheres de pimenta inclinadas sobre a água",
                termos=['"clear rectangular glass tank"', '"heaped with whole black peppercorns"'],
                pose="inclinado sobre a bancada, uma colher em cada mão sobre a água",
                lista="aquário, duas colheres de pimenta, apresentador, fundo",
                frame0="os primeiros grãos saindo das colheres, água ainda limpa",
                desvio="cozinha e bancada de mármore → mesa preta do box (avatar fixo); camiseta cinza e óculos → regata branca"),
    "K02": dict(_TQ, heroi="os grãos no fundo do aquário e algumas sementes boiando na superfície",
                termos=['"clear rectangular glass tank"', '"a few lighter brown wrinkled seeds float"'],
                pose="inclinado, apontando os grãos que boiam",
                lista="aquário com grãos, colher vazia, apresentador, fundo",
                frame0="a maior parte no fundo, alguns grãos boiando e outros ainda descendo",
                desvio="idem K01"),
    "K03": dict(_TQ, heroi="as duas batatas seguras sobre a água do aquário",
                termos=['"clear rectangular glass tank"', '"brown russet potato"'],
                pose="inclinado, uma batata em cada mão sobre a água",
                lista="aquário, duas batatas, apresentador, fundo",
                frame0="as batatas ainda nas mãos, água limpa", desvio="idem K01"),
    "K04": dict(_CP, heroi="os dois copos altos de água morna e as duas colheres de cúrcuma mergulhadas",
                termos=['"tall clear drinking glasses"', '"bright orange turmeric powder"'],
                pose="inclinado, uma colher em cada copo", lista="dois copos, duas colheres, apresentador, fundo",
                frame0="a água dos dois copos ainda limpa", desvio="idem K01"),
    "K05": dict(_CP, heroi="os dois copos de água fria e as duas colheres cheias de café moído sobre eles",
                termos=['"tall clear drinking glasses"', '"heaped with dark brown ground coffee"'],
                pose="inclinado, uma colher sobre cada copo", lista="dois copos, duas colheres, apresentador, fundo",
                frame0="o café ainda nas colheres, água limpa", desvio="idem K01"),
    "K06": dict(heroi="as duas canelas em close, a fina em camadas e a cássia grossa, quase encostando na lente",
                termos=['"thin and tightly rolled in many paper-thin brown layers"', '"single thick, hard, dark brown curl of bark"'],
                quadro="as canelas ocupam uns 40% de baixo, uma de cada lado do queixo; o rosto enorme no resto",
                dist="uns 15 cm das canelas", camera="celular na altura da boca, lente 1x reta",
                pose="colado na lente, uma canela em cada mão na altura da boca",
                lista="duas canelas, mãos, rosto, fundo", frame0="as duas lado a lado, camadas visíveis",
                desvio="idem K01",
                f2='"fill the lower 40 percent of the frame"', f3='"about 15 centimeters from the cinnamon sticks"',
                f4='"phone held just below eye height about 15 centimeters from the sticks, standard 1x lens"',
                f5='"leans in close to the lens"',
                f6="N/A | o quadro tem só as canelas, as mãos e o rosto; o fundo vem da âncora"),
    "K07": dict(_AB, heroi="os ingredientes dos testes enfileirados na mesa e ela de mãos abertas",
                pose="de pé atrás da bancada, palmas para cima", frame0="falando, mãos abertas",
                desvio="bancada → mesa preta (avatar fixo)"),
    "K08": dict(_AB, heroi="os ingredientes enfileirados e a mão dela aberta sobre eles",
                pose="de pé atrás da bancada, mão aberta sobre os ingredientes", frame0="falando, a mão sobre a fileira",
                desvio="no modelo a fala é do CTA (mesmo plano); este take é a transição aprovada no roteiro v2"),
}
for _k, _quadro, _dist, _f2, _f3, _f4, _pose in (
        ("K09", "pote nuns 25% no centro de baixo (o modelo não tem produto; mesmo plano do fecho, mais perto)", "uns 40 cm do pote",
         '"fills about 25 percent of the frame"', '"about 40 centimeters from the jar"',
         '"phone propped at table height about 40 centimeters from the jar, standard 1x lens"',
         '"Raised with both hands in front of her chest"'),
        ("K10", "pote nuns 30% no centro de baixo, o plano mais fechado do vídeo", "uns 35 cm do pote",
         '"fills about 30 percent of the frame"', '"about 35 centimeters from the jar"',
         '"phone propped at chest height, standard 1x lens"', '"Perfectly still with both hands"')):
    FICHA[_k] = dict(heroi="o pote de Natural Rems Sea Moss no lugar da coleção de truques, rótulo de frente para a lente",
                     termos=['"short wide jar of dark amber plastic with a black screw cap"', '"Sea Moss Gummies"'],
                     quadro=_quadro, dist=_dist, camera="celular na altura da bancada/peito, lente 1x reta",
                     pose="em pé atrás da mesa, segurando o pote na frente do peito",
                     lista="apresentadora, pote, fundo", frame0="pote já na mão, rótulo legível, ela falando",
                     desvio="coleção de truques por DM → pote do Natural Rems Sea Moss (CTA da marca, aprovado no roteiro)",
                     f2=_f2, f3=_f3, f4=_f4, f5=_pose,
                     f6="N/A | o quadro tem só ela e o pote; o fundo vem da âncora")


def ficha(ks):
    L = ["# FICHA DO FRAME · brandon_seamoss_temperos", "",
         "Regra e método: `GATE_VISUAL.md` Parte 6. Cada K sai daqui, nunca da memória. O frame do modelo manda no",
         "CONTEÚDO (forma, quadro, distância, câmera, pose, o que está em quadro); o gate manda no ACABAMENTO e impõe o",
         "piso de proximidade do herói. A evidência de cada OK é um trecho que existe literalmente no K.",
         "Gerada por `gerar_pacote.py`, que confere cada evidência contra o texto do K antes de escrever.", ""]
    for k in ks:
        cod, txt = k["codigo"], json.dumps(k["j"], ensure_ascii=False)
        f = FICHA[cod]
        fala = k["take"] in FALAS
        itens = [("F1 forma do heroi", " · ".join(f["termos"])), ("F2 quanto do quadro", f["f2"]),
                 ("F3 distancia da lente", f["f3"]), ("F4 camera", f["f4"]), ("F5 pose do avatar", f["f5"]),
                 ("F6 lista fechada", f["f6"]), ("G1 luz neutra", EV_COMUM["G1"]), ("G2 ceu ou janela", EV_COMUM["G2"]),
                 ("G3 foco", EV_COMUM["G3"]), ("G4 realismo", EV_COMUM["G4"]), ("G5 sem tom quente", EV_COMUM["G5"]),
                 ("G6 sem texto", EV_COMUM["G6"]), ("G7 bandeira", EV_COMUM["G7"]),
                 ("G8 boca no K de fala", EV_COMUM["G8"] if fala else "N/A | take sem fala")]
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
        "1. Clipes numerados na ordem: V01 a V10.",
        "2. Cortar cada clipe no tempo da cena do modelo: " + "; ".join(f"V{t[1:].zfill(2)} {MOMENTO[t]}" for t in TAKES) + ".",
        "3. Zero tempo morto: todo clipe começa já falando. Isolate Voice / Keep Vocal no áudio.",
        "4. Dentro de cada teste (V01 a V06), jump cuts curtos de ritmo como no modelo, se quiser; o clipe é contínuo.",
        "5. V10 inteiro, sem corte e sem nada cobrindo o pote: é o CTA da marca (frasco parado e legível enquanto o nome é dito). O vídeo acaba nele.",
        "6. Legenda de tela como no modelo: serifada branca, palavra a palavra, no meio do quadro, com a palavra carregada maior; no começo do V01, \"Real peppercorns sink\".",
        "7. Sem Voice Changer: a voz vem do prompt de cada V.",
        "8. Música só depois do gancho (a partir do V03), nunca no pré-gancho, entre -19 e -20 dB, fora da biblioteca do TikTok.",
        "9. Rótulo pequeno `Synthetic performer` num canto do vídeo.",
        "10. Legenda do post: `#ad #syntheticperformer #naturalrems` na primeira linha e o link da Amazon logo abaixo; chave de conteúdo de IA ligada na plataforma.",
    ]


def transcricao():
    L = ["| Take | English | Português |", "|---|---|---|"]
    for t in TAKES:
        L.append(f"| {t} | {FALAS[t]} | {TRANSCRICAO_PT[t]} |")
    return L


def pacote(a):
    ks, vs = keyframes(a), videos(a)
    L = ["# holistic.brandon | Ângulo 1 Natural Rems Sea Moss | Cinco testes de comida falsificada | Pacote de Prompts", "",
         "Vídeo modelo: `input/reference_video.mp4` (57,8 s, pessoa real)", "",
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
          f"- Gancho: {AQUARIO}; colheres de metal com grãos inteiros de pimenta-do-reino; no K02 alguns grãos marrons enrugados boiando.",
          f"- Testes: duas batatas no mesmo aquário; {COPOS} com cúrcuma laranja e com café moído; duas canelas (a fina em camadas, a cássia grossa).",
          f"- Fecho: os ingredientes {FILEIRA}.",
          f"- Produto (T9 e T10): {POTE}. Referência: `{PRODUTO_IMG}`, só o pote da frente, sem a faixa MADE IN USA, sem o pote de trás e sem as gomas soltas.",
          "- Nada dos testes tem marca legível.", "",
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
          "5. CTA da marca no T10: Search Natural Rems Sea Moss on Amazon, depois o link da legenda, e fim.",
          "6. Pote em quadro no T9 e no T10, rótulo legível; no T10 parado do começo ao fim.",
          "7. Nada médico em quadro nem na fala; sem antes e depois; sem cura nem tratamento.",
          "8. Negative sem termo sensível.",
          "9. GATE_VISUAL Partes 1 a 3 em todo K: herói colado na lente, luz neutra, sem tom quente, sem blur, trecho de realismo.",
          "10. Gancho fiel no conteúdo: as colheres de pimenta virando no aquário colado na lente, falado desde o segundo 0.",
          "11. Um K = um V; a queda dos grãos, a batata que boia, a água amarela e o café que afunda nascem no vídeo.", ""]
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
