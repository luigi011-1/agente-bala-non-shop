"""Gera o pacote da producao brandon_seamoss_joelho (Angulo 1, Natural Rems Sea Moss, venda, validacao).

Fonte unica da fala: ROTEIRO.md aprovado em 2026-10-02 (lido do disco, nunca redigitado). Identidade,
roupa e cenario: a ancora aprovada (avatar fixo por conta). Medidas de cada K: os frames do modelo em
input/frames_modelo/, registradas em FICHA_FRAMES.md, que este script tambem escreve, com a evidencia
de cada OK conferida contra o texto do K (assert). Gabarito: brandon_pes_peroxido/gerar_pacote.py.

Prompt de imagem entregue em JSON (contrato do Flow v17). Produto em quadro so do T12 ao T14, com a
foto oficial do pote como terceiro anexo.

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
assert TAKES == ["T%d" % i for i in range(1, 15)], TAKES
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
FALA_NO_COMECO = {"T2", "T3"}
# Takes com a mao da segunda pessoa em quadro (so antebraco e mao, cortados pela borda direita).
COM_AJUDANTE = {"T1", "T4", "T5"}
# Takes com o pote do Natural Rems Sea Moss em quadro.
COM_PRODUTO = {"T12", "T13", "T14"}

FICCAO = "This is a fictional AI-generated character, no real person is depicted."
PRODUTO_IMG = "producao/_ancoras/natural_rems_seamoss_produto.jpg"


def frame_modelo(cod):
    return f"input/frames_modelo/{cod}_modelo.png"


LUZ = ("Neutral overcast daylight from a large window out of frame, soft even light on her face, hands and knees "
       "with no harsh shadows. The red neon glows on the wall but does not tint her skin.")
REALISMO = ("Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural "
            "clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday "
            "reality, background fully in focus, everything in sharp focus, no AI polish, no beauty smoothing.")
NEG_BASE = ("no captions, no subtitles, no words overlaid on the image, no studio, no plastic-looking skin, "
            "no extra fingers, no third hand, no blur, no bokeh, no warm orange color cast, no yellow tint, "
            "no golden glow, no golden hour light, no sunset, no HDR, no cinematic lighting, no de-aging, "
            "no beauty smoothing, no visible phone, no glasses, no kitchen, no white marble "
            "counter, no silver cross, no white coat")
NEG_SOZINHA = ", no second person"
NEG_AJUDANTE = ", no second face in frame, no full second body"
NEG_SEM_FRASCO = ", no readable lettering on the bowl, mugs, glass dish or spoon"

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

FRASCO_PEROXIDO = ("a plain dark brown plastic bottle of hydrogen peroxide, the cap off, with a blank white label "
                   "and nothing written on it")
BANCO = "a black padded gym bench"
MESA = "the black table in front of her"
TIGELA = "a large plain white ceramic mixing bowl"
POTE = ("the Natural Rems Sea Moss Gummies jar exactly as in the attached product photo: a short wide jar of dark "
        "amber plastic with a black screw cap, a pale sage-green label with dark green text, the Natural Rems logo "
        "with three leaves at the top, the big title Sea Moss Gummies, a pill-shaped badge reading 6000 MG | 16-IN-1, "
        "the line GREEN APPLE FLAVOR, two columns of dark green ingredient pills, green seaweed illustrations on the "
        "sides and a small 30 Gummies badge")

EMOCAO = {
    "T1": "entonação intrigante e desafiadora, como quem avisa",
    "T2": "entonação calma e didática",
    "T3": "entonação calma e didática",
    "T4": "entonação calma e didática",
    "T5": "entonação séria e convicta, baixando a voz em rotting",
    "T6": "entonação séria e didática",
    "T7": "entonação compreensiva e próxima",
    "T8": "entonação indignada, como quem defende quem assiste",
    "T9": "entonação de quem conta um segredo, firme",
    "T10": "entonação didática e convicta",
    "T11": "entonação firme e segura",
    "T12": "entonação calorosa e confiante",
    "T13": "entonação animada e segura",
    "T14": "entonação clara e pausada, dizendo Natural Rems Sea Moss devagar e por inteiro",
}
ACOES = {
    "T1": ("Uma mão que entra pela borda direita derrama a água oxigenada do frasco marrom sobre o joelho dela; por "
           "volta de 2 segundos o líquido toca a pele, uma espuma branca nasce, cresce em bolhas grossas e depois "
           "escorre em gotas pela canela. {n} fala olhando para a câmera. A pessoa da mão fica em silêncio."),
    "T2": "{n}, inclinada sobre a mesa, derrama o frasco marrom dentro da tigela branca.",
    "T3": ("{n} despeja as duas canecas de água na tigela ao mesmo tempo, larga as canecas, pega a colher de "
           "bicarbonato e vira dentro da tigela."),
    "T4": ("{n} pega o pano branco da mão que entra pela direita, mergulha o pano na tigela e torce de leve. A pessoa "
           "da mão fica em silêncio."),
    "T5": ("As duas mãos que entram pela direita levantam o pano do joelho dela e revelam uma espuma branca de bolhas "
           "grossas sobre o joelho; {n} aponta para a espuma com o indicador. A pessoa das mãos fica em silêncio."),
    "T6": "{n} aponta para as manchas vermelhas do modelo de joelho da esquerda e depois toca o modelo liso da direita.",
    "T7": "{n}, com os antebraços apoiados na mesa, abre as mãos com as palmas para cima enquanto fala.",
    "T8": "{n} levanta um pouco as duas mãos abertas, palmas para cima, num gesto de pergunta.",
    "T9": "{n} junta as pontas dos dedos sobre a mesa e se inclina um pouco para a câmera.",
    "T10": "{n} fala para a câmera abrindo e fechando as mãos devagar sobre a mesa, com pequenos gestos naturais.",
    "T11": "{n} junta as mãos sobre a mesa e olha firme para a câmera.",
    "T12": ("{n} segura o pote de Natural Rems Sea Moss com as duas mãos na altura do peito, rótulo de frente para a "
            "câmera, e aproxima o pote um pouco da câmera quando diz o nome."),
    "T13": "{n} segura o pote parado na mão esquerda, rótulo de frente, e aponta para o rótulo com o indicador direito.",
    "T14": ("{n} segura o pote parado com as duas mãos, rótulo de frente e legível, sem nada cobrindo, do começo ao "
            "fim; só o rosto e a boca se mexem."),
}
CAMERA = {"T1": "leve handheld, bem perto do joelho", "T2": "leve handheld", "T3": "leve handheld",
          "T4": "leve handheld, bem perto do joelho", "T5": "leve handheld, bem perto do joelho",
          "T6": "fixa, bem perto dos modelos"}
SOM_EXTRA = {"T1": ", líquido caindo e espuma estalando", "T2": ", líquido caindo na tigela",
             "T3": ", água caindo na tigela e a colher batendo na cerâmica", "T4": ", pano pingando na tigela",
             "T5": ", espuma estalando baixinho"}
MOMENTO = {"T1": "0,0 a 7,6 s", "T2": "7,6 a 9,2 s", "T3": "9,2 a 13,2 s", "T4": "13,2 a 17,7 s",
           "T5": "17,7 a 23,4 s", "T6": "23,4 a 30,3 s", "T7": "30,3 a 35,7 s", "T8": "35,7 a 43,2 s",
           "T9": "43,2 a 50,4 s", "T10": "50,4 a 59,5 s", "T11": "59,5 a 64,8 s", "T12": "64,8 a ~70 s",
           "T13": "~70 a ~74,5 s", "T14": "o CTA inteiro, sem corte (~7 s)"}
TITULOS = {"T1": "gancho, água oxigenada no joelho colado na lente", "T2": "receita, frasco na tigela",
           "T3": "receita, duas canecas e bicarbonato", "T4": "protocolo, o pano entregue pela direita",
           "T5": "reveal, o pano saindo do joelho", "T6": "os dois modelos de joelho",
           "T7": "mesa, dor", "T8": "mesa, objeção", "T9": "mesa, virada", "T10": "mesa, mecanismo",
           "T11": "mesa, solução", "T12": "pote sobe no nome", "T13": "pote, ingredientes",
           "T14": "CTA, pote parado e legível"}


def keyframes(a):
    n = a["nome"]
    boca = "caught mid-sentence, lips naturally parted, animated expression, looking straight into the lens"
    ref_base = (f"Use the first attached image only for {n}'s exact identity, wardrobe and her own garage gym. Use the "
                "second attached image only as a composition reference for the camera position, framing and the "
                "action; do not copy its man, glasses, gray t-shirt, kitchen, marble counter, cartoon magnet or the "
                "caption text.")
    ref_prod = (ref_base + " Use the third attached image only for the exact look of the front jar and its label; "
                "ignore the MADE IN USA banner, the second jar with the Supplement Facts panel and the loose gummies.")
    joelho = ("Her bare right knee, bent and raised toward the camera, smooth skin, fills the lower 40 percent of the "
              "frame at the lower left, very close to the lens, larger than her head and closer to the camera than "
              "her face, nothing else competing with it.")
    post_banco = (f"{n} sits on {BANCO}, leaning slightly forward, her right foot up on the edge of the bench so her "
                  "right knee rises toward the lens, her left hand resting on her left thigh.")
    cam_joelho = "phone held at chest height about 30 centimeters in front of her knee, standard 1x lens tilted slightly down"
    comp_joelho = ("Close straight-on shot: the phone lens is about 30 centimeters from her knee; the knee fills the "
                   "lower 40 percent of the frame, her face and shoulders fill the upper part. The background is "
                   "reduced by framing, never by blur.")
    ajudante = ("a second person's slim bare forearm and hand in a plain navy t-shirt sleeve, cut off by the right edge of "
                "the frame")
    post_mesa = (f"{n} stands behind {MESA}, leaning forward over it, her forearms close to the table edge.")
    cam_mesa = "phone held just above the table edge at chest height, standard 1x lens tilted slightly down"
    receita_lista = (f"{TIGELA}, empty, in the center of {MESA}, very close to the lens; two plain white ceramic mugs "
                     "full of warm water at its left; a small clear glass dish of white baking soda with a metal "
                     "teaspoon at its right.")
    comp_receita = ("Close shot from just above the table: the phone lens is about 40 centimeters from the bowl, which "
                    "with the mugs and the glass dish fills the lower 40 percent of the frame, closer to the camera "
                    "than her face; her head and torso fill the upper part. Nothing else is on the table. The "
                    "background is reduced by framing, never by blur.")
    post_fala = (f"{n} stands behind {MESA}, leaning on her forearms on the table edge, seen from the waist up, her "
                 "bare hands resting on the table near the lens.")
    cam_fala = "phone propped at table height about 50 centimeters from her, standard 1x lens tilted slightly up"
    comp_fala = ("Straight-on medium shot from table height: the phone lens is about 50 centimeters from her; her "
                 "hands on the table fill about 30 percent of the frame at the bottom, closer to the camera than "
                 "her face, and her face and shoulders fill the upper half. The table is empty. The background is reduced by "
                 "framing, never by blur.")
    sem_prop = "No prop. The black table is empty; the bowl, the bottle and the jar are out of frame."
    cam_pote = "phone propped at table height about 40 centimeters from the jar, standard 1x lens, level"
    ks = {
        "T1": dict(ref=ref_base,
                   prop=(f"Above her knee, {ajudante}, tilts {FRASCO_PEROXIDO}. " + joelho),
                   posture=post_banco, composition=comp_joelho, camera=cam_joelho,
                   state=(f"Start frame: the first thin stream of clear liquid is just leaving the bottle toward the "
                          f"top of the knee; the skin is still clean and dry, no foam yet. {n} is {boca}."),
                   negative=NEG_BASE + NEG_AJUDANTE + ", no foam yet, no readable label on the bottle"),
        "T2": dict(ref=ref_base,
                   prop=(receita_lista[0].upper() + receita_lista[1:] + f" Her right hand tilts {FRASCO_PEROXIDO} "
                         "into the bowl from the right side."),
                   posture=post_mesa + " Her left hand rests on the table next to the mugs.",
                   composition=comp_receita, camera=cam_mesa,
                   state=f"Start frame: clear liquid is starting to pour from the bottle into the empty bowl. {n} is {boca}.",
                   negative=NEG_BASE + NEG_SOZINHA + NEG_SEM_FRASCO + ", no readable label on the bottle"),
        "T3": dict(ref=ref_base,
                   prop=(f"{TIGELA[0].upper()}{TIGELA[1:]} in the center of {MESA}, very close to the lens, with a little clear liquid in "
                         "it; a small clear glass dish of white baking soda with a metal teaspoon at its right. She "
                         "holds one plain white ceramic mug full of warm water in each hand, tilted above the bowl."),
                   posture=post_mesa, composition=comp_receita, camera=cam_mesa,
                   state=f"Start frame: the water is just starting to pour from both mugs into the bowl. {n} is {boca}.",
                   negative=NEG_BASE + NEG_SOZINHA + NEG_SEM_FRASCO + ", no bottle in frame"),
        "T4": dict(ref=ref_base,
                   prop=(f"{ajudante[0].upper()}{ajudante[1:]}, holds out a folded white cotton cloth toward her; at "
                         f"the lower right {TIGELA} full of clear liquid is held up by the second person's other hand. "
                         + joelho),
                   posture=post_banco.replace("her left hand resting on her left thigh",
                                              "her left hand reaching for the cloth"),
                   composition=comp_joelho, camera=cam_joelho,
                   state=f"Start frame: the cloth is dry and folded, just reaching her hand. {n} is {boca}.",
                   negative=NEG_BASE + NEG_AJUDANTE + ", no foam on the knee"),
        "T5": dict(ref=ref_base,
                   prop=("A wet white cotton cloth lies spread over her bare right knee, covering it completely; the "
                         "two hands of a second person, slim bare forearms in plain navy t-shirt sleeves cut off by the "
                         "right edge of the frame, hold its two upper corners, ready to lift it. Her bare right knee, "
                         "bent and raised toward the camera, under the cloth, fills the lower 40 percent of the frame "
                         "at the lower left, very close to the lens, larger than her head and closer to the camera than "
                         "her face, nothing else competing with it."),
                   posture=post_banco.replace("her left hand resting on her left thigh",
                                              "her right index finger raised, ready to point at the knee"),
                   composition=comp_joelho, camera=cam_joelho,
                   state=(f"Start frame: the cloth still covers the knee completely, nothing visible under it yet. "
                          f"{n} is {boca}."),
                   negative=NEG_BASE + NEG_AJUDANTE),
        "T6": dict(ref=ref_base,
                   prop=("Two life-size anatomical knee joint models stand upright side by side on two small white "
                         f"square bases on {MESA}, very close to the lens: each one a bone-colored femur on top and "
                         "tibia and fibula below, joined at the knee. The left model has the joint cartilage worn "
                         "rough and eroded, with red inflamed patches and frayed tissue across the joint surface; "
                         "the right model has smooth white cartilage, a clean joint and small pink ligaments. Her "
                         "right index finger points at the red patches of the left model."),
                   posture=f"{n} leans in behind the two models, her face just above and between them.",
                   composition=("Very close shot at table height: the phone lens is about 25 centimeters from the "
                                "models, which fill the lower 60 percent of the frame almost edge to edge, taller "
                                "than her head, closer to the camera than her face; her face is in the upper third "
                                "between their tops. Nothing else is on the table. The background is reduced by "
                                "framing, never by blur."),
                   camera="phone propped at table height, standard 1x lens, level",
                   state=f"Start frame: her finger touches the red patches of the left model. {n} is {boca}.",
                   negative=NEG_BASE + NEG_SOZINHA + ", no plastic skeleton, no extra bones"),
        "T7": dict(ref=ref_base, prop=sem_prop, posture=post_fala + " Both palms open upward, spread apart.",
                   composition=comp_fala, camera=cam_fala, state=f"Start frame: {n} is {boca}, understanding and warm.",
                   negative=NEG_BASE + NEG_SOZINHA),
        "T8": dict(ref=ref_base, prop=sem_prop, posture=post_fala + " Both palms open upward, lifted a little as in a question.",
                   composition=comp_fala, camera=cam_fala, state=f"Start frame: {n} is {boca}, eyebrows raised.",
                   negative=NEG_BASE + NEG_SOZINHA),
        "T9": dict(ref=ref_base, prop=sem_prop, posture=post_fala + " Her fingertips touch together above the table.",
                   composition=comp_fala, camera=cam_fala,
                   state=f"Start frame: {n} leans slightly toward the lens and is {boca}.",
                   negative=NEG_BASE + NEG_SOZINHA),
        "T10": dict(ref=ref_base, prop=sem_prop, posture=post_fala + " Both hands open, a little apart, mid-gesture.",
                    composition=comp_fala, camera=cam_fala, state=f"Start frame: {n} is {boca}, explaining.",
                    negative=NEG_BASE + NEG_SOZINHA),
        "T11": dict(ref=ref_base, prop=sem_prop, posture=post_fala + " Her hands are loosely clasped together on the table.",
                    composition=comp_fala, camera=cam_fala, state=f"Start frame: {n} is {boca}, firm and sure.",
                    negative=NEG_BASE + NEG_SOZINHA),
        "T12": dict(ref=ref_prod,
                    prop=(f"Raised with both hands in front of her chest, she holds {POTE}. The label is turned straight "
                          "to the lens and fully readable, her fingers only on the sides of the jar."),
                    posture=f"{n} stands behind {MESA}, seen from the waist up, holding the jar toward the camera.",
                    composition=("Straight-on medium shot from table height: the phone lens is about 40 centimeters "
                                 "from the jar, which fills about 25 percent of the frame in the lower center, closer "
                                 "to the camera than her face; her face and shoulders fill the upper half. The table "
                                 "is empty. The background is reduced by framing, never by blur."),
                    camera=cam_pote, state=f"Start frame: {n} is smiling and {boca}.",
                    negative=NEG_BASE + NEG_SOZINHA + ", no second jar, no loose gummies, no banner on the jar, no fingers over the label"),
        "T13": dict(ref=ref_prod,
                    prop=(f"In her left hand, in front of her chest, she holds {POTE}. The label is turned straight to the "
                          "lens and fully readable, her right index finger pointing at the ingredient pills on the label."),
                    posture=f"{n} stands behind {MESA}, seen from the waist up, holding the jar toward the camera.",
                    composition=("Straight-on medium shot from table height: the phone lens is about 40 centimeters "
                                 "from the jar, which fills about 25 percent of the frame in the lower center, closer "
                                 "to the camera than her face; her face and shoulders fill the upper half. The table "
                                 "is empty. The background is reduced by framing, never by blur."),
                    camera=cam_pote, state=f"Start frame: {n} is {boca}, upbeat.",
                    negative=NEG_BASE + NEG_SOZINHA + ", no second jar, no loose gummies, no banner on the jar, no fingers over the label"),
        "T14": dict(ref=ref_prod,
                    prop=(f"Perfectly still with both hands in front of her chest, centered, she holds {POTE}. The label is "
                          "turned straight to the lens, fully readable and with nothing covering it."),
                    posture=f"{n} stands behind {MESA}, seen from the chest up, holding the jar toward the camera.",
                    composition=("The tightest shot of the video, straight-on from chest height: the phone lens is "
                                 "about 35 centimeters from the jar, which fills about 30 percent of the frame in the "
                                 "lower center, closer to the camera than her face; her face fills the upper half. "
                                 "The background is reduced by framing, never by blur."),
                    camera="phone propped at chest height, standard 1x lens, level",
                    state=f"Start frame: {n} is {boca}, clear and calm.",
                    negative=NEG_BASE + NEG_SOZINHA + ", no second jar, no loose gummies, no banner on the jar, no fingers over the label"),
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
FICHA = {
    "K01": dict(heroi="o joelho dobrado e erguido para a lente, com o frasco marrom inclinado sobre ele pela mão da direita",
                termos=['"bare right knee"', '"plain dark brown plastic bottle of hydrogen peroxide"'],
                quadro="o joelho ocupa uns 40% de baixo do quadro, da esquerda ao centro; o frasco e o antebraço na direita, no terço do meio",
                dist="uns 30 cm do joelho; o joelho maior que a cabeça dele",
                camera="celular na altura do peito, lente 1x levemente para baixo, de frente",
                pose="sentado, inclinado para a frente, joelho erguido na frente da câmera, olhando para a lente",
                lista="joelho, frasco, antebraço e mão do ajudante, avatar, fundo (no K: parede com neon, quadro e bandeira)",
                frame0="o líquido começando a sair do frasco, pele ainda limpa, sem espuma",
                desvio="cozinha → box de treino; banco de cozinha → banco preto de academia; camiseta cinza → regata branca (avatar fixo); frasco sem marca legível",
                f2='"fills the lower 40 percent of the frame"', f3='"about 30 centimeters from her knee"',
                f4='"standard 1x lens tilted slightly down"', f5='"leaning slightly forward"',
                f6="N/A | não há frase de quadro fechado: o fundo vem da âncora e o quadro só tem joelho, frasco e mão"),
    "K02": dict(heroi="a tigela branca grande vazia no centro da mesa, o frasco marrom virando dentro dela",
                termos=['"large plain white ceramic mixing bowl"', '"two plain white ceramic mugs"'],
                quadro="tigela, canecas e potinho nos 40% de baixo; ele inclinado atrás, cabeça e tronco na metade de cima",
                dist="uns 40 cm da tigela",
                camera="celular logo acima da bancada, altura do peito, lente 1x levemente para baixo",
                pose="em pé atrás da bancada, inclinado, mão direita virando o frasco, esquerda perto das canecas",
                lista="tigela, duas canecas, potinho de vidro com bicarbonato, colher, frasco, avatar, fundo",
                frame0="o líquido começando a cair na tigela vazia",
                desvio="bancada de mármore → mesa preta da âncora (avatar fixo)",
                f2='"fills the lower 40 percent of the frame"', f3='"about 40 centimeters from the bowl"',
                f4='"standard 1x lens tilted slightly down"', f5='"leaning forward over it"',
                f6='"Nothing else is on the table"'),
    "K03": dict(heroi="as duas canecas viradas sobre a tigela branca",
                termos=['"large plain white ceramic mixing bowl"', '"plain white ceramic mug"'],
                quadro="tigela e canecas nos 40% de baixo",
                dist="uns 40 cm da tigela",
                camera="celular logo acima da bancada, altura do peito, lente 1x levemente para baixo",
                pose="em pé atrás da bancada, inclinado, uma caneca em cada mão sobre a tigela",
                lista="tigela, duas canecas, potinho de bicarbonato, colher, avatar, fundo (o frasco do modelo, cortado na borda, sai)",
                frame0="a água começando a cair das duas canecas",
                desvio="bancada → mesa preta (avatar fixo); o frasco cortado na borda direita do modelo sai do quadro",
                f2='"fills the lower 40 percent of the frame"', f3='"about 40 centimeters from the bowl"',
                f4='"standard 1x lens tilted slightly down"', f5='"leaning forward over it"',
                f6='"Nothing else is on the table"'),
    "K04": dict(heroi="o joelho erguido colado na lente e o pano branco dobrado entregue pela mão da direita",
                termos=['"bare right knee"', '"folded white cotton cloth"'],
                quadro="joelho nos 40% de baixo à esquerda; pano no centro; tigela na direita de baixo",
                dist="uns 30 cm do joelho",
                camera="celular na altura do peito, lente 1x levemente para baixo",
                pose="sentado, joelho erguido, mão esquerda indo pegar o pano",
                lista="joelho, pano, mão e antebraço do ajudante, tigela, avatar, fundo",
                frame0="o pano seco e dobrado chegando na mão dela",
                desvio="idem K01",
                f2='"fills the lower 40 percent of the frame"', f3='"about 30 centimeters from her knee"',
                f4='"standard 1x lens tilted slightly down"', f5='"her left hand reaching for the cloth"',
                f6="N/A | o quadro tem joelho, pano, mão e tigela; o fundo vem da âncora"),
    "K05": dict(heroi="o pano branco molhado cobrindo o joelho, seguro pelas duas mãos do ajudante prontas para levantar",
                termos=['"wet white cotton cloth"', '"bare right knee"'],
                quadro="pano e joelho nos 40% de baixo, do centro à esquerda; as mãos do ajudante na direita",
                dist="uns 30 cm do joelho",
                camera="celular na altura do peito, lente 1x levemente para baixo",
                pose="sentado, joelho erguido, indicador pronto para apontar",
                lista="joelho coberto, pano, duas mãos do ajudante, avatar, fundo",
                frame0="o pano ainda cobrindo o joelho inteiro; a espuma só aparece no vídeo",
                desvio="idem K01; a tigela do modelo, cortada na borda direita, sai do quadro",
                f2='"fills the lower 40 percent of the frame"', f3='"about 30 centimeters from her knee"',
                f4='"standard 1x lens tilted slightly down"', f5='"her right index finger raised, ready to point at the knee"',
                f6="N/A | o quadro tem joelho, pano e mãos; o fundo vem da âncora"),
    "K06": dict(heroi="os dois modelos de joelho em pé lado a lado, o da esquerda gasto e vermelho, o da direita liso e branco",
                termos=['"Two life-size anatomical knee joint models"', '"red inflamed patches"', '"smooth white cartilage"'],
                quadro="os modelos ocupam uns 60% de baixo, quase de borda a borda, mais altos que a cabeça dele",
                dist="uns 25 cm dos modelos",
                camera="celular na altura da bancada, lente 1x reta",
                pose="inclinado atrás dos modelos, rosto entre os topos, indicador nas manchas vermelhas do da esquerda",
                lista="dois modelos nas bases brancas, mão, avatar, fundo",
                frame0="o dedo tocando as manchas vermelhas do modelo da esquerda",
                desvio="bancada → mesa preta (avatar fixo)",
                f2='"fill the lower 60 percent of the frame"', f3='"about 25 centimeters from the models"',
                f4='"phone propped at table height, standard 1x lens"', f5='"leans in behind the two models"',
                f6='"Nothing else is on the table"'),
}
for _k, _gesto in (("K07", "palmas abertas para cima, afastadas"), ("K08", "palmas para cima, erguidas como pergunta"),
                   ("K09", "pontas dos dedos juntas"), ("K10", "mãos abertas no meio do gesto"),
                   ("K11", "mãos juntas sobre a mesa")):
    FICHA[_k] = dict(heroi="as mãos dela sobre a mesa, perto da lente, gesticulando enquanto fala para a câmera",
                     termos=['"hands on the table"'],
                     quadro="mãos nuns 30% de baixo, rosto e ombros na metade de cima",
                     dist="uns 50 cm dela; as mãos mais perto que o rosto",
                     camera="celular na altura da bancada, lente 1x levemente para cima (grande-angular no modelo)",
                     pose="apoiado nos antebraços na borda da bancada, " + _gesto,
                     lista="avatar, mesa vazia, fundo",
                     frame0="falando, " + _gesto,
                     desvio="bancada → mesa preta; a pose já é a da âncora",
                     f2='"fill about 30 percent of the frame at the bottom"', f3='"about 50 centimeters from her"',
                     f4='"phone propped at table height about 50 centimeters from her, standard 1x lens"',
                     f5='"leaning on her forearms on the table edge"', f6='"The table is empty"')
for _k, _quadro, _dist, _f2, _f3, _f4, _pose in (
        ("K12", "pote nuns 25% no centro de baixo (o tablet do modelo ocupava uns 30% à esquerda)", "uns 40 cm do pote",
         '"fills about 25 percent of the frame"', '"about 40 centimeters from the jar"',
         '"phone propped at table height about 40 centimeters from the jar, standard 1x lens"',
         '"Raised with both hands in front of her chest"'),
        ("K13", "pote nuns 25% no centro de baixo", "uns 40 cm do pote",
         '"fills about 25 percent of the frame"', '"about 40 centimeters from the jar"',
         '"phone propped at table height about 40 centimeters from the jar, standard 1x lens"',
         '"pointing at the ingredient pills on the label"'),
        ("K14", "pote nuns 30% no centro de baixo, o plano mais fechado do vídeo", "uns 35 cm do pote",
         '"fills about 30 percent of the frame"', '"about 35 centimeters from the jar"',
         '"phone propped at chest height, standard 1x lens"', '"Perfectly still with both hands"')):
    FICHA[_k] = dict(heroi="o pote de Natural Rems Sea Moss no lugar do tablet do ebook, rótulo de frente para a lente",
                     termos=['"short wide jar of dark amber plastic with a black screw cap"', '"Sea Moss Gummies"'],
                     quadro=_quadro, dist=_dist,
                     camera="celular na altura da bancada/peito, lente 1x reta",
                     pose="em pé atrás da mesa, segurando o pote na frente do peito",
                     lista="avatar, pote, fundo",
                     frame0="pote já na mão, rótulo legível, ela falando",
                     desvio="tablet com a capa do ebook → pote do Natural Rems Sea Moss (CTA da marca, aprovado no roteiro)",
                     f2=_f2, f3=_f3, f4=_f4, f5=_pose,
                     f6="N/A | o quadro tem só ela e o pote; o fundo vem da âncora")


def ficha(ks):
    L = ["# FICHA DO FRAME · brandon_seamoss_joelho", "",
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
        "1. Clipes numerados na ordem: V01 a V14.",
        "2. Cortar cada clipe no tempo da cena do modelo: " + "; ".join(f"V{t[1:].zfill(2)} {MOMENTO[t]}" for t in TAKES) + ".",
        "3. Zero tempo morto: todo clipe começa já falando. Isolate Voice / Keep Vocal no áudio.",
        "4. Nos V02 e V03 (cenas curtas) a fala vem no começo; cortar logo depois da última palavra. O V02 termina em vírgula e o V03 continua a lista: emendar sem pausa.",
        "5. V07 a V11 são o plano único de 34 s do modelo: emendar com corte seco, sem transição.",
        "6. V14 inteiro, sem corte e sem nada cobrindo o pote: é o CTA da marca (frasco parado e legível enquanto o nome é dito). O vídeo acaba nele.",
        "7. Legenda de tela como no modelo: serifada branca, palavra a palavra, no meio do quadro, com a palavra carregada maior (foaming, joints, bacteria, gut, Natural Rems Sea Moss).",
        "8. Sem Voice Changer: a voz vem do prompt de cada V.",
        "9. Música só depois do gancho (a partir do V02), nunca no pré-gancho, entre -19 e -20 dB, fora da biblioteca do TikTok.",
        "10. Rótulo pequeno `Synthetic performer` num canto do vídeo (a marca não exige mais, mas não custa).",
        "11. Legenda do post: `#ad #syntheticperformer #naturalrems` na primeira linha, e o link da Amazon logo abaixo; chave de conteúdo de IA ligada na plataforma.",
    ]


def transcricao():
    L = ["| Take | English | Português |", "|---|---|---|"]
    for t in TAKES:
        L.append(f"| {t} | {FALAS[t]} | {TRANSCRICAO_PT[t]} |")
    return L


def pacote(a):
    ks, vs = keyframes(a), videos(a)
    L = ["# holistic.brandon | Ângulo 1 Natural Rems Sea Moss | Joelho que espuma | Pacote de Prompts", "",
         "Vídeo modelo: `input/reference_video.mp4` (77,3 s, pessoa real)", "",
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
          "- 2ª pessoa: só antebraço e mão, cortados pela borda direita, nos K01, K04 e K05. Nunca rosto.", "",
          "## Trava do prop herói", "",
          f"- Gancho e receita: {FRASCO_PEROXIDO}; {TIGELA}; duas canecas brancas; potinho de vidro com bicarbonato e colher.",
          "- Protocolo: pano branco de algodão. Mecanismo: dois modelos anatômicos de joelho (um gasto e vermelho, um liso).",
          f"- Produto (T12 a T14): {POTE}. Referência: `{PRODUTO_IMG}`, só o pote da frente, sem a faixa MADE IN USA, sem o pote de trás e sem as gomas soltas.",
          "- O frasco de água oxigenada nunca tem marca legível.", "",
          "## Trava da 2ª pessoa (REF-A)", "",
          "- Não precisa de REF: a 2ª pessoa é só antebraço e mão (antebraço fino, manga de camiseta azul-marinho), "
          "descrita por escrito em cada K. Fica em silêncio em todos os V.", "",
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
          "2. Um take por cena do modelo; T2 e T3 marcados CENA CURTA; nenhum take acima de 29 palavras.",
          "3. Bandeira dos EUA no campo scene de todo K.",
          "4. Zero travessão.",
          "5. CTA da marca no T14: Search Natural Rems Sea Moss on Amazon, depois o link da legenda, e fim.",
          "6. Pote em quadro do T12 ao T14, rótulo legível; no T14 parado do começo ao fim.",
          "7. Nada médico em quadro nem na fala; sem antes e depois; sem cura nem tratamento.",
          "8. Negative sem termo sensível.",
          "9. GATE_VISUAL Partes 1 a 3 em todo K: herói colado na lente, luz neutra, sem tom quente, sem blur, trecho de realismo.",
          "10. Gancho fiel no conteúdo: água oxigenada derramada no joelho colado na lente e a espuma nascendo, falado desde o segundo 0.",
          "11. Um K = um V; a espuma do T1 e a do T5 nascem no vídeo, a imagem é o estado inicial.", ""]
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
    print("ok: pacote da Brandon; PROMPTS_PRODUCAO.md = holistic.brandon; FICHA_FRAMES.md com 14 K")


if __name__ == "__main__":
    main()
