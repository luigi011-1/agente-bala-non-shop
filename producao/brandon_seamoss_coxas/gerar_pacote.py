"""Gera o pacote da producao brandon_seamoss_coxas (Angulo 1, Natural Rems Sea Moss, venda, validacao).

Fonte unica da fala: ROTEIRO.md v2 aprovado em 2026-10-02 (lido do disco, nunca redigitado). Identidade,
roupa e cenario: a ancora aprovada (avatar fixo por conta). Medidas de cada K: os frames do modelo em
input/frames_modelo/, registradas em FICHA_FRAMES.md, que este script tambem escreve, com a evidencia
de cada OK conferida contra o texto do K (assert). Gabarito: brandon_seamoss_joelho/gerar_pacote.py.

Prompt de imagem entregue em JSON (contrato do Flow v17). A cliente (2a pessoa) aparece so no T1 e no
T2, cortada pela borda direita. Produto em quadro so no T10 e no T11, com a foto oficial do pote como
terceiro anexo. A coxa nunca clareia em quadro (antes e depois proibido pela marca).

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
assert TAKES == ["T%d" % i for i in range(1, 12)], TAKES
FALAS = {}
for bloco in re.split(r"^(?=### T\d+ · )", ROTEIRO, flags=re.M)[1:]:
    m = re.search(r'^> "(.+?)"\s*$', bloco.split("\n## ")[0], re.M)
    if m:
        FALAS[re.match(r"### (T\d+)", bloco).group(1)] = m.group(1)
assert set(FALAS) == set(TAKES), FALAS
TRANSCRICAO_PT = dict(re.findall(r"^\| (T\d+) \| .+? \| (.+?) \|$",
                                 ROTEIRO.split("## Tabela bilíngue")[1].split("## ")[0], re.M))
assert set(TRANSCRICAO_PT) == set(TAKES), TRANSCRICAO_PT
# Cenas curtas do modelo: a fala sai no comeco do clipe e a acao segue em silencio.
FALA_NO_COMECO = {"T1", "T2", "T4"}
# Takes com a cliente em quadro.
COM_CLIENTE = {"T1", "T2"}
# Takes com o pote do Natural Rems Sea Moss em quadro.
COM_PRODUTO = {"T10", "T11"}

FICCAO = "This is a fictional AI-generated character, no real person is depicted."
PRODUTO_IMG = "producao/_ancoras/natural_rems_seamoss_produto.jpg"


def frame_modelo(cod):
    return f"input/frames_modelo/{cod}_modelo.png"


LUZ = ("Neutral overcast daylight from a large window out of frame, soft even light on her face, hands and skin "
       "with no harsh shadows. The red neon glows on the wall but does not tint anyone's skin.")
REALISMO = ("Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural "
            "clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday "
            "reality, background fully in focus, everything in sharp focus, no AI polish, no beauty smoothing.")
NEG_BASE = ("no captions, no subtitles, no words overlaid on the image, no studio, no plastic-looking skin, "
            "no extra fingers, no third hand, no blur, no bokeh, no warm orange color cast, no yellow tint, "
            "no golden glow, no golden hour light, no sunset, no HDR, no cinematic lighting, no de-aging, "
            "no beauty smoothing, no visible phone, no apron, no older man, no kitchen cabinets, no white marble "
            "counter, no framed certificates, no silver cross, no white coat")
NEG_SOZINHA = ", no second person"
NEG_CLIENTE = (", no gown, no paper sheet on the bench, no underwear showing, no lightened patch, "
               "no even skin on the inner thigh")
NEG_RECEITA = ", no readable lettering on the bowl, spoon or dropper bottle"

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

BANCO = "a black padded flat gym bench"
MESA = "the black table in front of her"
TIGELA = "a clear glass mixing bowl"
CLIENTE = ("The client, a fictional American woman around fifty with shoulder-length gray-brown hair, wearing a plain "
           "light gray crew-neck t-shirt and loose black athletic shorts that fully cover her hips, lies on her back "
           f"on {BANCO}, her head and shoulders at the right edge of the frame, partly cut off by it.")
COXA = ("Her left leg is bent at the knee with the inner side of the thigh turned toward the camera: the bare inner "
        "thigh fills the lower 45 percent of the frame from the lower left to the center, very close to the lens, "
        "larger than both faces and closer to the camera than them, nothing else competing with it. On the upper "
        "inner thigh, just below the hem of her shorts, a large patch of dark brown, rough, velvety skin about the "
        "size of an open hand, clearly darker than the rest of her leg, with a few darker spots around its edge.")
POTE = ("the Natural Rems Sea Moss Gummies jar exactly as in the attached product photo: a short wide jar of dark "
        "amber plastic with a black screw cap, a pale sage-green label with dark green text, the Natural Rems logo "
        "with three leaves at the top, the big title Sea Moss Gummies, a pill-shaped badge reading 6000 MG | 16-IN-1, "
        "the line GREEN APPLE FLAVOR, two columns of dark green ingredient pills, green seaweed illustrations on the "
        "sides and a small 30 Gummies badge")

EMOCAO = {
    "T1": "entonação baixa e séria, como quem conta um segredo de uma cliente",
    "T2": "entonação de virada, curiosa, com um meio sorriso",
    "T3": "entonação calma e didática",
    "T4": "entonação calma e didática",
    "T5": "entonação calma e didática, firme nos números",
    "T6": "entonação aliviada e calorosa",
    "T7": "entonação séria, como quem avisa",
    "T8": "entonação didática e convicta, marcando consequence",
    "T9": "entonação firme e segura",
    "T10": "entonação calorosa e confiante",
    "T11": "entonação clara e pausada, dizendo Natural Rems Sea Moss devagar e por inteiro",
}
ACOES = {
    "T1": ("{n}, ajoelhada ao lado do banco, passa a mão pela coxa da cliente e aponta a mancha escura com o "
           "indicador, olhando para a câmera. A cliente fica deitada e em silêncio."),
    "T2": ("{n} vira a mão aberta, palma para cima, na direção da câmera; a cliente olha para a câmera com um meio "
           "sorriso e fica em silêncio. A coxa não muda."),
    "T3": "{n}, inclinada sobre a mesa, espreme o meio limão dentro da tigela de bicarbonato.",
    "T4": "{n} pinga duas gotas de óleo de coco com o conta-gotas dentro da tigela.",
    "T5": ("{n} mexe a pasta com a colher, mostra o movimento em círculos com a ponta dos dedos e abre cinco dedos "
           "no five."),
    "T6": "{n} ergue a tigela de pasta na direção da câmera, depois abaixa e gesticula com a mão livre.",
    "T7": "{n}, com a tigela parada na mesa, aponta para a pasta e depois abre as mãos.",
    "T8": "{n} aponta a tigela no problem e encosta a mão aberta no próprio peito no protect itself.",
    "T9": "{n} empurra a tigela de pasta devagar para o lado, abrindo espaço na mesa.",
    "T10": ("{n} segura o pote de Natural Rems Sea Moss com as duas mãos na altura do peito, rótulo de frente para a "
            "câmera, e aproxima o pote um pouco da câmera quando diz o nome."),
    "T11": ("{n} segura o pote parado com as duas mãos, rótulo de frente e legível, sem nada cobrindo, do começo ao "
            "fim; só o rosto e a boca se mexem."),
}
CAMERA = {"T1": "leve handheld, baixa, bem perto da coxa", "T2": "leve handheld, baixa, bem perto da coxa",
          "T3": "leve handheld", "T4": "leve handheld",
          "T5": "leve handheld, com leve push-in no meio e volta ao plano"}
SOM_EXTRA = {"T3": ", limão pingando na tigela", "T4": ", gotas caindo na tigela", "T5": ", colher raspando o vidro"}
MOMENTO = {"T1": "0,0 a 4,7 s", "T2": "4,7 a 6,2 s", "T3": "6,2 a 10,2 s", "T4": "10,2 a 14,0 s",
           "T5": "14,0 a 21,8 s", "T6": "21,8 a 28,8 s", "T7": "a fala inteira", "T8": "a fala inteira",
           "T9": "a fala inteira", "T10": "a fala inteira", "T11": "o CTA inteiro, sem corte"}
TITULOS = {"T1": "gancho, a coxa escura da cliente colada na lente", "T2": "virada, mão aberta, a coxa igual",
           "T3": "receita, limão na tigela", "T4": "receita, óleo de coco no conta-gotas",
           "T5": "protocolo, mexendo a pasta", "T6": "resultado, a tigela erguida", "T7": "ponte, a superfície",
           "T8": "mecanismo, causa e consequência", "T9": "a saída, tigela de lado", "T10": "pote sobe no nome",
           "T11": "CTA, pote parado e legível"}


def keyframes(a):
    n = a["nome"]
    boca = "caught mid-sentence, lips naturally parted, animated expression, looking straight into the lens"
    ref_base = (f"Use the first attached image only for {n}'s exact identity, wardrobe and her own garage gym. Use the "
                "second attached image only as a composition reference for the camera position, framing and the "
                "action; do not copy its older man and woman, aprons, kitchen, marble counter, exam room, framed "
                "certificates or the caption text.")
    ref_prod = (ref_base + " Use the third attached image only for the exact look of the front jar and its label; "
                "ignore the MADE IN USA banner, the second jar with the Supplement Facts panel and the loose gummies.")
    post_cliente = (f"{n} kneels on the black rubber floor at the left side of the bench, leaning in over the thigh, "
                    "her face in the upper left of the frame.")
    cam_cliente = "phone held low at bench height about 25 centimeters from the thigh, wide 0.5x lens, level"
    comp_cliente = ("Low close shot at bench height: the phone lens is about 25 centimeters from the inner thigh, which "
                    "fills the lower 45 percent of the frame; Brandon's face is in the upper left and the client's "
                    "head at the right edge. The background is reduced by framing, never by blur.")
    post_mesa = f"{n} stands behind {MESA}, leaning forward over it, seen from the waist up."
    cam_mesa = "phone held just above the table edge at chest height about 40 centimeters from the bowl, standard 1x lens tilted slightly down"
    comp_mesa = ("Close shot from just above the table: the phone lens is about 40 centimeters from the bowl, which "
                 "fills about 25 percent of the frame in the lower center, closer to the camera than her face; her "
                 "head and torso fill the upper part. Nothing else is on the table. The background is reduced by "
                 "framing, never by blur.")
    cam_fala = "phone propped at table height about 45 centimeters from the bowl, standard 1x lens tilted slightly up"
    comp_fala = ("Straight-on medium shot from table height: the phone lens is about 45 centimeters from the bowl, "
                 "which sits in the lower left and fills about 20 percent of the frame, closer to the camera than her "
                 "face; her face and shoulders fill the upper half. Nothing else is on the table. The background is "
                 "reduced by framing, never by blur.")
    pasta = f"{TIGELA[0].upper()}{TIGELA[1:]} full of thick white paste with a metal spoon resting in it"
    cam_pote = "phone propped at table height about 40 centimeters from the jar, standard 1x lens, level"
    neg_pote = NEG_BASE + NEG_SOZINHA + ", no second jar, no loose gummies, no banner on the jar, no fingers over the label"
    ks = {
        "T1": dict(ref=ref_base,
                   prop=(f"{CLIENTE} {COXA} {n}'s right hand rests flat on the thigh just above the dark patch, her "
                         "index finger pointing at it."),
                   posture=post_cliente, composition=comp_cliente, camera=cam_cliente,
                   state=(f"Start frame: the client lies calm with her eyes half closed. {n} is {boca}."),
                   negative=NEG_BASE + NEG_CLIENTE),
        "T2": dict(ref=ref_base,
                   prop=(f"{CLIENTE} {COXA} {n}'s left hand is held open, palm up, toward the lens just above the "
                         "thigh."),
                   posture=post_cliente, composition=comp_cliente, camera=cam_cliente,
                   state=(f"Start frame: the dark patch is exactly as before; the client looks at the lens with a "
                          f"faint smile. {n} is {boca}."),
                   negative=NEG_BASE + NEG_CLIENTE),
        "T3": dict(ref=ref_base,
                   prop=(f"{TIGELA[0].upper()}{TIGELA[1:]} with a heap of white baking soda powder in the center of "
                         f"{MESA}, very close to the lens, a metal measuring spoon lying at its left. Her right hand "
                         "squeezes half a fresh lemon above the bowl; her left hand holds the rim of the bowl."),
                   posture=post_mesa, composition=comp_mesa, camera=cam_mesa,
                   state=f"Start frame: the first drops of lemon juice are falling into the powder. {n} is {boca}.",
                   negative=NEG_BASE + NEG_SOZINHA + NEG_RECEITA),
        "T4": dict(ref=ref_base,
                   prop=(f"{TIGELA[0].upper()}{TIGELA[1:]} with milky white liquid in the center of {MESA}, very "
                         "close to the lens, a squeezed lemon half and a metal measuring spoon beside it. Her right hand "
                         "holds the glass dropper of a small amber dropper bottle of coconut oil above the bowl."),
                   posture=post_mesa, composition=comp_mesa, camera=cam_mesa,
                   state=f"Start frame: a drop of oil hangs from the tip of the dropper. {n} is {boca}.",
                   negative=NEG_BASE + NEG_SOZINHA + NEG_RECEITA),
        "T5": dict(ref=ref_base,
                   prop=(f"{TIGELA[0].upper()}{TIGELA[1:]} full of thick white paste in the center of {MESA}, very "
                         "close to the lens, two squeezed lemon halves at its left. Her right hand stirs the paste with a "
                         "metal spoon; her left hand holds the rim of the bowl."),
                   posture=post_mesa, composition=comp_mesa, camera=cam_mesa,
                   state=f"Start frame: the spoon is mid-stir in the paste. {n} is {boca}.",
                   negative=NEG_BASE + NEG_SOZINHA + NEG_RECEITA),
        "T6": dict(ref=ref_base,
                   prop=(f"With both hands she holds {TIGELA} full of thick white paste with a metal spoon in it, "
                         "raised and tilted toward the lens; on the table below, a lemon half, a metal measuring spoon "
                         "and a small amber dropper bottle."),
                   posture=f"{n} stands behind {MESA}, seen from the waist up, holding the bowl toward the camera.",
                   composition=("Close shot from chest height: the phone lens is about 30 centimeters from the bowl, "
                                "which fills about 30 percent of the frame in the lower center, closer to the camera "
                                "than her face; her face fills the upper part. The background is reduced by framing, "
                                "never by blur."),
                   camera="phone held at chest height about 30 centimeters from the bowl, standard 1x lens, level",
                   state=f"Start frame: the paste is clearly visible inside the tilted bowl. {n} is {boca}, relieved.",
                   negative=NEG_BASE + NEG_SOZINHA + NEG_RECEITA),
        "T7": dict(ref=ref_base,
                   prop=f"{pasta}, standing still on {MESA}; her right index finger points at the paste.",
                   posture=f"{n} stands behind {MESA}, seen from the waist up, both forearms near the table edge.",
                   composition=comp_fala, camera=cam_fala, state=f"Start frame: {n} is {boca}, serious.",
                   negative=NEG_BASE + NEG_SOZINHA + NEG_RECEITA),
        "T8": dict(ref=ref_base,
                   prop=f"{pasta}, standing still on {MESA}; her left hand is open in a small explaining gesture.",
                   posture=f"{n} stands behind {MESA}, seen from the waist up, her right hand open on her own chest.",
                   composition=comp_fala, camera=cam_fala, state=f"Start frame: {n} is {boca}, convinced.",
                   negative=NEG_BASE + NEG_SOZINHA + NEG_RECEITA),
        "T9": dict(ref=ref_base,
                   prop=f"{pasta}, on {MESA}; her right hand rests on the rim of the bowl, about to slide it aside.",
                   posture=f"{n} stands behind {MESA}, seen from the waist up, leaning slightly toward the lens.",
                   composition=comp_fala, camera=cam_fala, state=f"Start frame: {n} is {boca}, firm.",
                   negative=NEG_BASE + NEG_SOZINHA + NEG_RECEITA),
        "T10": dict(ref=ref_prod,
                    prop=(f"Raised with both hands in front of her chest, she holds {POTE}. The label is turned "
                          "straight to the lens and fully readable, her fingers only on the sides of the jar."),
                    posture=f"{n} stands behind {MESA}, seen from the waist up, holding the jar toward the camera.",
                    composition=("Straight-on medium shot from table height: the phone lens is about 40 centimeters "
                                 "from the jar, which fills about 25 percent of the frame in the lower center, closer "
                                 "to the camera than her face; her face and shoulders fill the upper half. The table "
                                 "is empty. The background is reduced by framing, never by blur."),
                    camera=cam_pote, state=f"Start frame: {n} is smiling and {boca}.",
                    negative=neg_pote),
        "T11": dict(ref=ref_prod,
                    prop=(f"Perfectly still with both hands in front of her chest, centered, she holds {POTE}. The "
                          "label is turned straight to the lens, fully readable and with nothing covering it."),
                    posture=f"{n} stands behind {MESA}, seen from the chest up, holding the jar toward the camera.",
                    composition=("The tightest shot of the video, straight-on from chest height: the phone lens is "
                                 "about 35 centimeters from the jar, which fills about 30 percent of the frame in the "
                                 "lower center, closer to the camera than her face; her face fills the upper half. "
                                 "The background is reduced by framing, never by blur."),
                    camera="phone propped at chest height, standard 1x lens, level",
                    state=f"Start frame: {n} is {boca}, clear and calm.",
                    negative=neg_pote),
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
# Lida olhando cada frame do modelo (input/frames_modelo/Kxx_modelo.png). As evidencias sao trechos
# literais dos K acima; o assert em ficha() garante que existem.
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
_CLI = dict(termos=['"large patch of dark brown, rough, velvety skin"', '"inner thigh fills the lower 45 percent of the frame"'],
            quadro="a coxa ocupa uns 45% de baixo, da esquerda ao centro; o rosto dele no alto à esquerda, a cliente deitada à direita",
            dist="uns 25 cm da coxa; a coxa maior que os dois rostos",
            camera="celular baixo, na altura da maca, grande-angular, reto",
            f2='"fills the lower 45 percent of the frame"', f3='"about 25 centimeters from the inner thigh"',
            f4='"wide 0.5x lens"', f5='"kneels on the black rubber floor at the left side of the bench"',
            f6="N/A | o quadro tem coxa, mão, cliente e Brandon; o fundo vem da âncora")
FICHA = {
    "K01": dict(_CLI, heroi="a mancha escura, áspera e aveludada na parte interna da coxa da cliente, colada na lente, com a mão do apresentador em cima",
                pose="inclinado sobre a coxa, a mão espalmada acima da mancha, o indicador apontando",
                lista="coxa com a mancha, mão, apresentador, cliente deitada, a mulher de avental atrás (sai), fundo",
                frame0="mão sobre a coxa apontando a mancha, cliente de olhos meio fechados",
                desvio="maca, papel de maca, diplomas e camisola → banco preto do box, camiseta e short (sem clínica, regra da marca); casal → só a Brandon (avatar fixo)"),
    "K02": dict(_CLI, heroi="a mesma coxa com a mancha, e a mão aberta virada para a lente",
                pose="mão aberta, palma para cima, na direção da lente",
                lista="coxa, mão aberta, apresentador, cliente sorrindo, fundo",
                frame0="a mão aberta para a lente; no modelo a coxa já aparece clara",
                desvio="a coxa clara do modelo vira a MESMA mancha (antes e depois proibido pela marca); idem K01"),
    "K03": dict(heroi="a tigela de vidro com bicarbonato e o meio limão espremido sobre ela",
                termos=['"clear glass mixing bowl"', '"squeezes half a fresh lemon"'],
                quadro="tigela nuns 25% no centro de baixo; ela inclinada atrás, cabeça e tronco no alto",
                dist="uns 40 cm da tigela", camera="celular acima da bancada, altura do peito, lente 1x levemente para baixo",
                pose="inclinada sobre a bancada, mão direita espremendo o limão, esquerda na borda da tigela",
                lista="tigela com bicarbonato, limão, colher de medida, apresentadora, fundo (o homem atrás sai)",
                frame0="as primeiras gotas de limão caindo no pó", desvio="cozinha → mesa preta do box (avatar fixo); o homem atrás sai",
                f2='"fills about 25 percent of the frame"', f3='"about 40 centimeters from the bowl"',
                f4='"standard 1x lens tilted slightly down"', f5='"leaning forward over it"',
                f6='"Nothing else is on the table"'),
    "K04": dict(heroi="o conta-gotas de óleo de coco sobre a tigela de líquido branco",
                termos=['"clear glass mixing bowl"', '"small amber dropper bottle of coconut oil"'],
                quadro="tigela nuns 25% no centro de baixo", dist="uns 40 cm da tigela",
                camera="celular acima da bancada, altura do peito, lente 1x levemente para baixo",
                pose="inclinada, conta-gotas na mão direita sobre a tigela",
                lista="tigela, limão espremido, colher, conta-gotas, apresentadora, fundo",
                frame0="uma gota pendurada na ponta do conta-gotas", desvio="idem K03",
                f2='"fills about 25 percent of the frame"', f3='"about 40 centimeters from the bowl"',
                f4='"standard 1x lens tilted slightly down"', f5='"leaning forward over it"',
                f6='"Nothing else is on the table"'),
    "K05": dict(heroi="a pasta branca grossa sendo mexida na tigela de vidro",
                termos=['"clear glass mixing bowl"', '"thick white paste"'],
                quadro="tigela nuns 25% no centro de baixo", dist="uns 40 cm da tigela",
                camera="celular acima da bancada, altura do peito, lente 1x levemente para baixo",
                pose="inclinada, mexendo com a colher, a outra mão na borda",
                lista="tigela de pasta, colher, metades de limão, apresentadora, fundo",
                frame0="a colher no meio da mexida", desvio="idem K03",
                f2='"fills about 25 percent of the frame"', f3='"about 40 centimeters from the bowl"',
                f4='"standard 1x lens tilted slightly down"', f5='"leaning forward over it"',
                f6='"Nothing else is on the table"'),
    "K06": dict(heroi="a tigela de pasta erguida e inclinada para a lente",
                termos=['"clear glass mixing bowl"', '"thick white paste with a metal spoon in it"'],
                quadro="tigela nuns 30% no centro e à direita de baixo, mais perto que o rosto",
                dist="uns 30 cm da tigela", camera="celular na altura do peito, lente 1x reta",
                pose="em pé, segurando a tigela com as duas mãos na direção da lente",
                lista="tigela erguida, limão, colher de medida, conta-gotas, apresentadora, fundo",
                frame0="a pasta bem visível na tigela inclinada", desvio="idem K03",
                f2='"fills about 30 percent of the frame"', f3='"about 30 centimeters from the bowl"',
                f4='"phone held at chest height about 30 centimeters from the bowl, standard 1x lens"',
                f5='"holding the bowl toward the camera"',
                f6="N/A | o quadro tem a tigela, os três itens da receita na mesa e ela; o fundo vem da âncora"),
}
for _k, _pose, _f5 in (("K07", "aponta a pasta com o indicador", '"her right index finger points at the paste"'),
                       ("K08", "mão aberta no próprio peito, a outra explicando", '"her right hand open on her own chest"'),
                       ("K09", "mão na borda da tigela, prestes a afastá-la", '"about to slide it aside"')):
    FICHA[_k] = dict(heroi="a tigela de pasta parada no primeiro plano, à esquerda, e as mãos dela gesticulando",
                     termos=['"full of thick white paste with a metal spoon resting in it"'],
                     quadro="tigela nuns 20% embaixo à esquerda; rosto e ombros na metade de cima",
                     dist="uns 45 cm da tigela", camera="celular na altura da bancada, lente 1x levemente para cima",
                     pose=_pose, lista="tigela, mãos, apresentadora, fundo (o homem atrás sai)",
                     frame0="falando, " + _pose,
                     desvio="no modelo a fala é do T6 (mesmo plano); estes takes são o bloco de venda novo, aprovado no roteiro v2",
                     f2='"fills about 20 percent of the frame"', f3='"about 45 centimeters from the bowl"',
                     f4='"phone propped at table height about 45 centimeters from the bowl, standard 1x lens"',
                     f5=_f5, f6='"Nothing else is on the table"')
for _k, _quadro, _dist, _f2, _f3, _f4, _pose in (
        ("K10", "pote nuns 25% no centro de baixo (o livro do modelo ocupava uns 25% à direita)", "uns 40 cm do pote",
         '"fills about 25 percent of the frame"', '"about 40 centimeters from the jar"',
         '"phone propped at table height about 40 centimeters from the jar, standard 1x lens"',
         '"Raised with both hands in front of her chest"'),
        ("K11", "pote nuns 30% no centro de baixo, o plano mais fechado do vídeo", "uns 35 cm do pote",
         '"fills about 30 percent of the frame"', '"about 35 centimeters from the jar"',
         '"phone propped at chest height, standard 1x lens"', '"Perfectly still with both hands"')):
    FICHA[_k] = dict(heroi="o pote de Natural Rems Sea Moss no lugar do livro de remédios, rótulo de frente para a lente",
                     termos=['"short wide jar of dark amber plastic with a black screw cap"', '"Sea Moss Gummies"'],
                     quadro=_quadro, dist=_dist, camera="celular na altura da bancada/peito, lente 1x reta",
                     pose="em pé atrás da mesa, segurando o pote na frente do peito",
                     lista="apresentadora, pote, fundo (a mulher ao lado do modelo sai)",
                     frame0="pote já na mão, rótulo legível, ela falando",
                     desvio="livro de remédios → pote do Natural Rems Sea Moss (CTA da marca, aprovado no roteiro); casal → só a Brandon",
                     f2=_f2, f3=_f3, f4=_f4, f5=_pose,
                     f6="N/A | o quadro tem só ela e o pote; o fundo vem da âncora")


def ficha(ks):
    L = ["# FICHA DO FRAME · brandon_seamoss_coxas", "",
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
        "1. Clipes numerados na ordem: V01 a V11.",
        "2. Cortar cada clipe no tempo da cena do modelo: " + "; ".join(f"V{t[1:].zfill(2)} {MOMENTO[t]}" for t in TAKES) + ".",
        "3. Zero tempo morto: todo clipe começa já falando. Isolate Voice / Keep Vocal no áudio.",
        "4. Nos V01, V02 e V04 (cenas curtas) a fala vem no começo; cortar logo depois da última palavra. O V03 termina sem ponto e o V04 continua a frase: emendar sem pausa.",
        "5. V01 e V02 são o mesmo plano com corte seco entre eles, como no modelo; a coxa não muda de um para o outro.",
        "6. V11 inteiro, sem corte e sem nada cobrindo o pote: é o CTA da marca (frasco parado e legível enquanto o nome é dito). O vídeo acaba nele.",
        "7. Legenda de tela em inglês como no modelo: branca, grossa, palavra a palavra, no meio do quadro.",
        "8. Sem Voice Changer: a voz vem do prompt de cada V.",
        "9. Música só depois do gancho (a partir do V03), nunca no pré-gancho, entre -19 e -20 dB, fora da biblioteca do TikTok.",
        "10. Rótulo pequeno `Synthetic performer` no canto de cima à esquerda, como no modelo.",
        "11. Legenda do post: `#ad #syntheticperformer #naturalrems` na primeira linha e o link da Amazon logo abaixo; chave de conteúdo de IA ligada na plataforma.",
    ]


def transcricao():
    L = ["| Take | English | Português |", "|---|---|---|"]
    for t in TAKES:
        L.append(f"| {t} | {FALAS[t]} | {TRANSCRICAO_PT[t]} |")
    return L


def pacote(a):
    ks, vs = keyframes(a), videos(a)
    L = ["# holistic.brandon | Ângulo 1 Natural Rems Sea Moss | Coxa escura | Pacote de Prompts", "",
         "Vídeo modelo: `input/reference_video.mp4` (36,7 s, avatar IA, original em espanhol)", "",
         f"Âncora: `{a['ancora']}` · Foto do produto: `{PRODUTO_IMG}`", "",
         "Funil: venda Amazon. Frasco em quadro, \"Search Natural Rems Sea Moss on Amazon\" primeiro, link da "
         "legenda do post depois, fim. Rodada de validação, gancho fiel ao modelo sem o antes e depois.", "",
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
          "- A cliente só aparece nos K01 e K02, deitada, cortada pela borda direita. Nunca fala.", "",
          "## Trava do prop herói", "",
          "- Gancho: a mancha escura, áspera e aveludada na parte interna da coxa da cliente, do tamanho de uma mão "
          "aberta, logo abaixo da barra do short. **Igual no K01 e no K02**: a coxa nunca clareia em quadro.",
          f"- Receita: {TIGELA}, bicarbonato, meio limão, conta-gotas âmbar de óleo de coco, colher de medida, colher.",
          f"- Produto (T10 e T11): {POTE}. Referência: `{PRODUTO_IMG}`, só o pote da frente, sem a faixa MADE IN USA, sem o pote de trás e sem as gomas soltas.",
          "- Nada da receita tem marca legível.", "",
          "## Trava da 2ª pessoa (REF-A)", "",
          f"- Não precisa de REF: a cliente é descrita por escrito nos K01 e K02 ({CLIENTE}) Fica em silêncio.", "",
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
          "2. Um take por cena do modelo; T1, T2 e T4 marcados CENA CURTA; nenhum take acima de 29 palavras.",
          "3. Bandeira dos EUA no campo scene de todo K.",
          "4. Zero travessão.",
          "5. CTA da marca no T11: Search Natural Rems Sea Moss on Amazon, depois o link da legenda, e fim.",
          "6. Pote em quadro no T10 e no T11, rótulo legível; no T11 parado do começo ao fim.",
          "7. Nada médico em quadro nem na fala (sem maca, papel de maca, camisola, diploma); sem antes e depois; sem cura nem tratamento.",
          "8. Negative sem termo sensível.",
          "9. GATE_VISUAL Partes 1 a 3 em todo K: herói colado na lente, luz neutra, sem tom quente, sem blur, trecho de realismo.",
          "10. Gancho fiel no conteúdo: a mancha escura na coxa da cliente colada na lente, falado desde o segundo 0, e o corte para a mão aberta com a coxa igual.",
          "11. Um K = um V; nenhum K mostra a coxa clara.", ""]
    flow = ["# Blocos limpos para o Google Flow | holistic.brandon", "", "Fonte interna: `PROMPTS_BRANDON.md`", "",
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
