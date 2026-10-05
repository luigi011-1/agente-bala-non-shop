"""Gera o pacote da producao brandon_seamoss_gengibre_limao (Angulo 1, Natural Rems Sea Moss, VENDA, validacao).

Avatar unico: holistic.brandon, avatar fixo da conta, no box de treino com a mesa preta como bancada.
Fonte unica da fala: ROTEIRO.md aprovado em 2026-10-05 (lido do disco, nunca redigitado). Medidas de cada K: a
ficha abaixo, escrita olhando input/frames_modelo/Kxx_modelo.png e gravada em FICHA_FRAMES.md com o placar cuja
evidencia e conferida aqui mesmo contra o texto do K (assert). Prompt de imagem em JSON (Flow v17).
Gabarito de formato: brandon_seamoss_muffin/gerar_pacote.py e brandon_seamoss_vizinha (takes mudos).

Saidas: FICHA_FRAMES.md, PROMPTS_BRANDON.md, FLOW_BRANDON.md e PROMPTS_PRODUCAO.md.

Uso: python3 gerar_pacote.py
"""
import json
import re
from pathlib import Path

AQUI = Path(__file__).resolve().parent
ROTEIRO = (AQUI / "ROTEIRO.md").read_text(encoding="utf-8")

HEADS = dict(re.findall(r"^### (T\d+) · (.+)$", ROTEIRO, re.M))
TAKES = list(HEADS)
assert TAKES == ["T%d" % i for i in range(1, 17)], TAKES
FALAS = {}
for bloco in re.split(r"^(?=### T\d+ · )", ROTEIRO, flags=re.M)[1:]:
    m = re.search(r'^> "(.+?)"\s*$', bloco.split("\n## ")[0], re.M)
    if m:
        FALAS[re.match(r"### (T\d+)", bloco).group(1)] = m.group(1)
MUDOS = {"T3", "T5", "T6", "T9"}
VOZ_OVER = {"T2", "T4", "T7", "T11"}
assert set(FALAS) == set(TAKES) - MUDOS, sorted(set(TAKES) - MUDOS - set(FALAS))
for t in VOZ_OVER:
    assert "B-ROLL" in HEADS[t], t
TRANSCRICAO_PT = dict(re.findall(r"^\| (T\d+) \| .+? \| (.+?) \|$",
                                 ROTEIRO.split("## Tabela bilíngue")[1].split("\n## ")[0], re.M))
assert set(TRANSCRICAO_PT) == set(TAKES), set(TAKES) - set(TRANSCRICAO_PT)
TRANSCRICAO_EN = dict(re.findall(r"^\| (T\d+) \| (.+?) \| .+? \|$",
                                 ROTEIRO.split("## Tabela bilíngue")[1].split("\n## ")[0], re.M))

PRODUTO_T = {"T13", "T14", "T15", "T16"}
FICCAO = "This is a fictional AI-generated character, no real person is depicted."
ANCORA = "producao/_ancoras/holistic_brandon_ancora.jpg"
FOTO_PRODUTO = "producao/_ancoras/natural_rems_seamoss_produto.jpg"


def frame_modelo(cod):
    return f"input/frames_modelo/{cod}_modelo.png"


REALISMO = ("Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural "
            "clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday "
            "reality, background fully in focus, everything in sharp focus, no AI polish, no beauty smoothing.")
NEG = ("no captions, no subtitles, no words overlaid on the image, no plastic-looking skin, no extra fingers, "
       "no third hand, no blur, no bokeh, no warm orange color cast, no yellow tint, no golden glow, no golden "
       "hour light, no sunset, no HDR, no cinematic lighting, no beauty smoothing, no visible phone, no studio, "
       "no second person, no eyeglasses, no grey t-shirt, no white kitchen cabinets, no marble countertop, "
       "no silver cross, no log cabin, no suspenders, no shirtless man")
NEG_SEM_ROTULO = ", no printed labels or lettering on the cups, trays, board, knife or measuring cup"
NEG_PRODUTO = (", no second jar, no other bottles, no loose gummies, no banner above the jar, no hand covering "
               "the label, no lemons or ginger on the table")

B = dict(
    nome="Brandon", arquivo="BRANDON",
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
          "visible and in focus. In front of her stands a plain matte black table she uses as a kitchen counter."),
    voz="voz feminina clara e firme de uma mulher de uns trinta anos",
    sotaque="de uma mulher negra americana",
    som="box de treino em casa, tranquilo",
)
LUZ = ("Neutral overcast daylight from a large window out of frame, soft even light on her face, hands and the "
       "table with no harsh shadows. The red neon glows on the wall but does not tint her skin.")
REF = ("Use the first attached image only for Brandon's exact identity, wardrobe and own garage gym with the black "
       "table. Use the second attached image only as a composition reference for the camera position, framing and "
       "the action; do not copy its man, his suspenders, bare chest, log cabin, wooden counter or the "
       "caption text.")
REF_PROD = (REF + " Use the third attached image only for the Natural Rems Sea Moss jar: copy ONLY the front jar, "
            "without the MADE IN USA banner at the top, without the second jar behind it and without the loose "
            "gummies.")
FRASCO = ("the Natural Rems Sea Moss jar: a short wide jar of dark amber plastic with a black screw cap, a pale "
          "cream-green label with dark green text, the Natural Rems logo with three leaves, the big title Sea Moss "
          "Gummies, a 6000 MG | 16-IN-1 badge, the words GREEN APPLE FLAVOR, a list of ingredients in dark green pill "
          "shapes and green seaweed illustrations on both sides, label facing the camera, fully readable")
LIMAO = "a bright yellow lemon"
TABUA = "a rustic wooden cutting board with a natural wavy edge"
GENGIBRE = "a knobby tan ginger root"
COPO = "a tall clear plastic blender cup with a ridged wall"
FORMINHAS = "two white plastic ice cube trays side by side"
CANECA = "a clear thick glass mug with a handle"
BOCA = "caught mid-sentence, lips naturally parted, animated expression, looking straight into the lens"
CAM_PEITO = "phone at her chest height, tilted slightly down toward the table, standard 1x lens, light handheld"
NADA = "Nothing else is on the table."

K = {
    "T1": dict(titulo="gancho, limão e zester colados na lente",
               prop=(f"In her hands in front of her chest, {LIMAO} and a small metal zester that she drags down the lemon "
                     f"skin, one thin curl of yellow peel already hanging off it. On the black table below, {TABUA} "
                     f"with a chef's knife on it, two {GENGIBRE.split(' ', 2)[2]}s, a tall empty clear blender cup and "
                     f"a small wicker basket of lemons. {NADA}"),
               pose="Brandon stands upright behind the black table, zesting the lemon at chest height",
               comp=("Medium shot from chest height: the phone lens is about 45 centimeters from the lemon and zester, "
                     "which fill the lower 35 percent of the frame at the center, closer to the camera than her face; "
                     "her face, shoulders and torso fill the upper part and the table items sit along the bottom edge. "
                     "The background is reduced by framing, never by blur."),
               cam="phone at her chest height, straight-on, standard 1x lens, light handheld",
               est="eyebrows raised, as if sharing a trick",
               heroi="o limão e o zester nas mãos na frente do peito, a tira de casca já saindo, tábua, gengibre, copo e cesta na mesa",
               termos=["small metal zester", "one thin curl of yellow peel"],
               f6="Nothing else is on the table.",
               lista="limão e zester, tábua com faca, duas raízes de gengibre, copo vazio, cesta de limões, avatar",
               f0="a primeira tira de casca saindo do zester, faca e gengibre na tábua",
               desvio="cabana de toras, suspensório e homem sem camisa → box de treino e regata branca (avatar fixo); limão e zester um pouco mais perto da lente que no modelo (piso do gate)"),
    "T2": dict(titulo="receita, faca cortando o limão",
               prop=(f"On {TABUA} in the lower foreground, {LIMAO} halfway through being cut in half by a chef's knife "
                     f"held in her right hand while her left hand holds the lemon steady, a curl of peel beside it. "
                     f"{NADA}"),
               pose="Brandon leans over the black table, only her hands, forearms and white tank top visible, cutting the lemon",
               comp=("Close shot from chest height: the phone lens is about 30 centimeters from the board, which with the "
                     "lemon and knife fills the lower 55 percent of the frame, closer to the camera than her torso; her "
                     "torso and the tattoo sleeve on her right forearm fill the upper part and her face is out of "
                     "frame. The background is reduced by framing, never by blur."),
               cam="phone at her chest height, tilted down toward the board, standard 1x lens, light handheld",
               est="hands only, no face in frame",
               heroi="a faca de chef cortando o limão ao meio na tábua, mãos e antebraço com a tatuagem",
               termos=["halfway through being cut in half by a chef's knife"],
               f6="Nothing else is on the table.", lista="tábua, limão, faca, casca, mãos, torso",
               f0="a faca já na metade do limão", sem_rosto=True),
    "T3": dict(titulo="insert, gomos de limão em macro",
               prop=(f"On {TABUA}, a heap of freshly cut lemon wedges with glistening juicy flesh and thin white pith, "
                     "one half lemon with its cut face turned to the lens. Her fingertips rest at the edge of the pile. "
                     f"{NADA}"),
               pose="Brandon leans over the black table, only her fingertips visible beside the wedges",
               comp=("Extreme close shot: the phone lens is about 20 centimeters from the wedges, which fill about 85 "
                     "percent of the frame, closer to the camera than anything else; only a strip of her white tank "
                     "top shows at the top edge and her face is out of frame. The background is reduced by framing, "
                     "never by blur."),
               cam="phone at table height, tilted down toward the wedges, standard 1x lens, light handheld",
               est="hands only, no face in frame",
               heroi="os gomos de limão cortados em macro, ocupando quase o quadro todo",
               termos=["freshly cut lemon wedges with glistening juicy flesh"],
               f6="Nothing else is on the table.", lista="gomos de limão, meio limão, pontas dos dedos, tábua",
               f0="a pilha de gomos de limão preenchendo o quadro", sem_rosto=True),
    "T4": dict(titulo="receita, descascando o gengibre",
               prop=(f"In her hands, {GENGIBRE} that she peels with a small paring knife held in her right hand, thin "
                     "tan shavings falling onto the cutting board in the lower foreground. "
                     f"{NADA}"),
               pose="Brandon leans over the black table, only her hands, forearms and white tank top visible, peeling the ginger",
               comp=("Close shot from chest height: the phone lens is about 25 centimeters from her hands and the ginger "
                     "root, which fill the lower 60 percent of the frame, closer to the camera than her torso; her torso "
                     "fills the upper part and her face is out of frame. The background is reduced by framing, never by "
                     "blur."),
               cam="phone at her chest height, tilted down toward her hands, standard 1x lens, light handheld",
               est="hands only, no face in frame",
               heroi="a raiz de gengibre sendo descascada com a faquinha, casquinhas caindo na tábua",
               termos=["small paring knife held in her right hand"],
               f6="Nothing else is on the table.", lista="gengibre, faquinha, casquinhas, tábua, mãos, torso",
               f0="a faquinha no meio da casca, primeiras casquinhas na tábua", sem_rosto=True),
    "T5": dict(titulo="insert, limão e gengibre no copo",
               prop=(f"On the black table in the lower center, {COPO} filled to the top with chopped lemon wedges and "
                     "small pieces of ginger, clear plastic walls and a wide open mouth, her hand just lifting away "
                     f"from the rim. {NADA}"),
               pose="Brandon stands behind the black table, torso visible, one hand just lifting away from the blender cup",
               comp=("Straight-on close shot from table height: the phone lens is about 40 centimeters from the cup, "
                     "which fills the lower 65 percent of the frame, closer to the camera than her torso; her torso "
                     "fills the upper part and her face is out of frame. The background is reduced by framing, never "
                     "by blur."),
               cam="phone propped at table height, straight-on, standard 1x lens, light handheld",
               est="torso only, no face in frame",
               heroi="o copo transparente do liquidificador cheio de limão picado e gengibre",
               termos=["filled to the top with chopped lemon wedges and small pieces of ginger"],
               f6="Nothing else is on the table.", lista="copo do liquidificador com limão e gengibre, mão, torso",
               f0="o copo cheio, a mão se afastando da borda", sem_rosto=True),
    "T6": dict(titulo="insert, a água medida entrando",
               prop=(f"On the black table in the lower center, {COPO} full of lemon wedges and ginger. From above, her "
                     "right hand tilts a small metal measuring cup with a handle and a thin stream of clear water "
                     f"starts pouring into the blender cup. {NADA}"),
               pose="Brandon stands behind the black table, torso visible, pouring water from the measuring cup",
               comp=("Straight-on close shot from table height: the phone lens is about 40 centimeters from the cup, "
                     "which fills the lower 60 percent of the frame, closer to the camera than her torso; the measuring "
                     "cup enters from the top; her face is out of frame. The background is reduced by framing, never by "
                     "blur."),
               cam="phone propped at table height, straight-on, standard 1x lens, light handheld",
               est="torso only, no face in frame",
               heroi="o copo do liquidificador cheio e a medida de metal despejando o fio de água",
               termos=["small metal measuring cup with a handle", "a thin stream of clear water"],
               f6="Nothing else is on the table.", lista="copo com limão e gengibre, medida de metal, fio de água, mão, torso",
               f0="o primeiro fio de água saindo da medida", sem_rosto=True),
    "T7": dict(titulo="bate, copo no liquidificador",
               prop=(f"On the black table, the blender cup turned upside down and locked on a black blender base, the "
                     "chopped lemon and ginger inside swirling, her right palm pressed flat on top of the cup. "
                     f"{NADA}"),
               pose="Brandon stands behind the black table, torso visible, her right palm pressed flat on top of the blender",
               comp=("Straight-on close shot from table height: the phone lens is about 35 centimeters from the blender, "
                     "which fills the lower 70 percent of the frame, closer to the camera than her torso; her torso "
                     "fills the top strip and her face is out of frame. The background is reduced by framing, never by "
                     "blur."),
               cam="phone propped at table height, straight-on, standard 1x lens, light handheld",
               est="torso only, no face in frame",
               heroi="o copo no liquidificador batendo com a palma dela por cima",
               termos=["locked on a black blender base", "her right palm pressed flat on top of the cup"],
               f6="Nothing else is on the table.", lista="liquidificador com copo, mão, torso",
               f0="o limão e o gengibre já girando dentro do copo", sem_rosto=True),
    "T8": dict(titulo="resultado, copinho liso colado na lente",
               prop=("In her hands, held toward the lens, a small clear plastic blender cup with a lid ring, about a third "
                     "full of a smooth pale cream-yellow mixture with tiny flecks of fiber. Her other hand gestures "
                     f"open. {NADA}"),
               pose="Brandon leans forward over the black table toward the lens, holding the small cup of mixture",
               comp=("Close shot from chest height: the phone lens is about 30 centimeters from the cup, which fills the "
                     "lower 35 percent of the frame in the lower right, closer to the camera than her face; her face "
                     "fills the upper half. The background is reduced by framing, never by blur."),
               cam="phone at her chest height, straight-on, standard 1x lens, light handheld",
               est="lively, relaxed, a little proud",
               heroi="o copinho transparente com a mistura lisa, creme claro, colado na lente",
               termos=["small clear plastic blender cup with a lid ring", "smooth pale cream-yellow mixture"],
               f6="Nothing else is on the table.", lista="copinho com a mistura, mão aberta, avatar",
               f0="falando com o copinho já na frente da lente",
               desvio="cabana e homem de suspensório → box de treino (avatar fixo); copinho um pouco mais perto da lente que no modelo (piso do gate)"),
    "T9": dict(titulo="insert, despejando nas forminhas",
               prop=(f"On the black table in the lower foreground, {FORMINHAS}, each cavity partly filled with smooth pale "
                     "cream-yellow mixture. From the upper right, her hand tilts a small clear plastic blender cup and "
                     f"the last of the mixture runs into the trays. {NADA}"),
               pose="Brandon stands behind the black table, torso visible, pouring the mixture into the ice trays",
               comp=("Straight-on close shot from table height: the phone lens is about 35 centimeters from the trays, "
                     "which fill the lower 55 percent of the frame, closer to the camera than her torso; the cup enters "
                     "from the upper right and her face is out of frame. The background is reduced by framing, never "
                     "by blur."),
               cam="phone propped at table height, straight-on, standard 1x lens, light handheld",
               est="torso only, no face in frame",
               heroi="as duas forminhas de gelo brancas recebendo a mistura do copinho inclinado",
               termos=["two white plastic ice cube trays side by side", "the last of the mixture runs into the trays"],
               f6="Nothing else is on the table.", lista="duas forminhas, copinho inclinado, mão, torso",
               f0="a mistura caindo na última cavidade", sem_rosto=True),
    "T10": dict(titulo="fecha, plano aberto das forminhas cheias",
                prop=(f"On the black table in the lower foreground, {FORMINHAS} full of pale cream-yellow cubes, and a "
                      f"tall empty clear blender cup on the left. Her hands rest on the table edge. {NADA}"),
                pose="Brandon stands behind the black table leaning slightly forward with both hands on the table edge",
                comp=("Straight-on wide shot from table height: the phone lens is about 60 centimeters from the trays, "
                      "which fill the lower 30 percent of the frame, closer to the camera than her face, and she fills "
                      "the upper two thirds from the thighs up. The background is reduced by framing, never by blur."),
                cam="phone propped at table height about 1 meter from her, standard 1x lens, level",
                est="smiling, satisfied",
                heroi="as duas forminhas de gelo cheias de cubos creme e o copo vazio ao lado, ela sorrindo atrás",
                termos=["full of pale cream-yellow cubes", "tall empty clear blender cup"],
                f6="Nothing else is on the table.", lista="duas forminhas cheias, copo vazio, avatar",
                f0="sorrindo para a lente, mãos na borda da mesa",
                desvio="cabana e homem de suspensório → box de treino (avatar fixo); forminhas na borda da mesa, mais perto da lente que no modelo"),
    "T11": dict(titulo="uso, cubo caindo na caneca",
                prop=(f"On the black table in the lower center, {CANECA}, empty, with {LIMAO} beside it. One pale cream-"
                      "yellow ice cube dropped from her fingers is falling into the mug from above. "
                      f"{NADA}"),
                pose="Brandon stands behind the black table, torso visible, her fingers just letting go of the cube above the mug",
                comp=("Straight-on close shot from table height: the phone lens is about 30 centimeters from the mug, "
                      "which fills the lower 60 percent of the frame, closer to the camera than her torso; her torso "
                      "fills the upper part and her face is out of frame. The background is reduced by framing, never "
                      "by blur."),
                cam="phone propped at table height, straight-on, standard 1x lens, light handheld",
                est="torso only, no face in frame",
                heroi="o cubo creme caindo numa caneca de vidro vazia, limão ao lado",
                termos=["one pale cream-yellow ice cube", "clear thick glass mug with a handle"],
                f6="Nothing else is on the table.", lista="caneca vazia, cubo caindo, limão, dedos, torso",
                f0="o cubo no ar, logo acima da caneca", sem_rosto=True),
    "T12": dict(titulo="autodiagnóstico, caneca na mão",
                prop=(f"In her right hand, held at chest height, {CANECA} about half full of a pale cream-yellow drink. On "
                      f"the black table in the lower foreground, {FORMINHAS} full of cubes and a tall empty clear "
                      f"blender cup. {NADA}"),
                pose="Brandon stands behind the black table with the mug in her right hand, her left hand open",
                comp=("Straight-on medium shot: the phone lens is about 55 centimeters from the mug, which she holds at "
                      "chest height and which fills about 20 percent of the frame at the lower right, closer to the "
                      "camera than her face; the trays fill the lower 25 percent of the frame; her face and shoulders "
                      "fill the upper half. The background is reduced by framing, never by blur."),
                cam="phone propped at chest height, straight-on, standard 1x lens, light handheld",
                est="honest, a little challenging, eyebrows raised",
                heroi="a caneca de vidro com a bebida clara na mão e as forminhas cheias na mesa",
                termos=["about half full of a pale cream-yellow drink"],
                f6="Nothing else is on the table.", lista="caneca na mão, duas forminhas, copo vazio, avatar",
                f0="falando com a caneca na mão",
                desvio="cabana e homem de suspensório → box de treino (avatar fixo); caneca um pouco mais perto da lente que no modelo"),
}
for t, (tit, est) in {"T13": ("oferta, o frasco sobe no nome", "proud, about to show it"),
                      "T14": ("prova social da coach", "warm and certain"),
                      "T15": ("comment yes + follow", "inviting, smiling on yes"),
                      "T16": ("CTA da marca", "clear and slow on the brand name")}.items():
    low = t == "T13"
    K[t] = dict(titulo=tit,
                prop=(f"In her right hand, held low just above the black table, {FRASCO}. Nothing else is on the table."
                      if low else
                      f"In her right hand, held still beside her right cheek, {FRASCO}. Her left hand rests on the black table."),
                pose=("Brandon holds the jar low in her right hand, about to raise it beside her face" if low else
                      "Brandon holds the jar still beside her right cheek, label toward the lens"),
                comp=(("Straight-on medium shot: the phone lens is about 35 centimeters from the jar, which she holds low in "
                       "her right hand just above the black table and fills the lower right 20 percent of the frame, "
                       "closer to the camera than her face; her face and shoulders fill the upper half of the frame. The "
                       "background is reduced by framing, never by blur.") if low else
                      ("Straight-on medium shot: the jar is held up beside her right cheek and pushed slightly toward the "
                       "camera, the phone lens is about 30 centimeters from the jar, which fills 20 percent of the frame "
                       "at the right of her face, closer to the camera than her face, label facing the camera and fully "
                       "readable. The background is reduced by framing, never by blur.")),
                cam="phone at her chest height, straight-on, standard 1x lens, light handheld",
                est=est,
                heroi=("o frasco Natural Rems Sea Moss baixo na mão direita, rótulo de frente" if low else
                       "o frasco parado ao lado do rosto, rótulo de frente e legível"),
                termos=["short wide jar of dark amber plastic with a black screw cap", "Sea Moss Gummies"],
                lista="frasco, avatar, mesa vazia", f0=("frasco baixo, prestes a subir" if low else "falando com o frasco parado"),
                f6=("Nothing else is on the table" if low else "Her left hand rests on the black table"),
                desvio=("o modelo segura a caneca aqui; no bloco de venda o frasco entra no lugar, já na mão para nascer da foto real" if low else
                        "o modelo abre as mãos no CTA; aqui o frasco fica parado e legível (passo 1 da marca)"))

EMOCAO = {
    "T1": "entonação animada e intrigante, como quem conta um truque de cozinha", "T8": "entonação relaxada e satisfeita",
    "T10": "entonação curta e sorridente", "T12": "entonação sincera e desafiadora, com as sobrancelhas levantadas",
    "T13": "entonação orgulhosa, dizendo Natural Rems Sea Moss devagar e por inteiro",
    "T14": "entonação calorosa e segura", "T15": "entonação convidativa, sorrindo no yes",
    "T16": "entonação clara, dizendo Natural Rems Sea Moss devagar e por inteiro",
}
ACOES = {
    "T1": "{n} rala a casca do limão com o zester, uma tira fina de casca amarela pendurada, e olha para a câmera enquanto fala.",
    "T2": "A faca corta o limão ao meio na tábua; só as mãos e o antebraço com a tatuagem aparecem.",
    "T3": "Os gomos de limão cortados brilham em macro; uma ponta de dedo ajeita um gomo na pilha.",
    "T4": "As mãos descascam a raiz de gengibre com a faquinha, casquinhas finas caindo na tábua.",
    "T5": "O copo do liquidificador cheio de limão picado e gengibre; a mão se afasta da borda.",
    "T6": "A medida de metal despeja um fio de água dentro do copo cheio de limão e gengibre.",
    "T7": "A palma da mão por cima do copo travado na base; o limão e o gengibre giram e batem dentro do copo.",
    "T8": "{n} inclina o copinho com a mistura lisa na direção da câmera e abre a outra mão enquanto fala.",
    "T9": "A mão inclina o copinho e a última mistura escorre para dentro das duas forminhas de gelo.",
    "T10": "{n} sorri para a câmera atrás das forminhas cheias, com as mãos na borda da mesa.",
    "T11": "Os dedos soltam um cubo de gelo creme que cai dentro da caneca de vidro vazia, o limão ao lado.",
    "T12": "{n} fala para a câmera segurando a caneca com a mão direita, a mão esquerda aberta, as forminhas cheias na mesa.",
    "T13": "{n} ergue o frasco devagar da altura da cintura até o lado do rosto no nome do produto e o deixa parado, rótulo de frente.",
    "T14": "{n} fala para a câmera com o frasco parado ao lado do rosto, rótulo de frente.",
    "T15": "{n} fala para a câmera com o frasco parado ao lado do rosto, sorrindo no yes.",
    "T16": "{n} fala para a câmera com o frasco parado ao lado do rosto, rótulo de frente, do começo ao fim, sem baixar o frasco.",
}
SOM = {"T1": ", zester raspando a casca", "T2": ", faca cortando o limão na tábua", "T3": ", gomos de limão suculentos",
       "T4": ", faquinha descascando o gengibre", "T5": ", pedaços caindo no copo", "T6": ", água entrando no copo",
       "T7": ", liquidificador batendo", "T9": ", mistura escorrendo nas forminhas", "T11": ", cubo batendo no vidro"}
ABRE_MUDO = {
    "T2": "(sem fala no take: a fala 2 entra como voz-over na edição)",
    "T3": "(sem fala no take: insert mudo, a voz da fala 2 e da fala 4 segue por cima na edição)",
    "T4": "(sem fala no take: a fala 4 entra como voz-over na edição)",
    "T5": "(sem fala no take: insert mudo, a voz da fala 4 segue por cima na edição)",
    "T6": "(sem fala no take: insert mudo, a voz da fala 4 segue por cima na edição)",
    "T7": "(sem fala no take: a fala 7 entra como voz-over na edição)",
    "T9": "(sem fala no take: insert mudo, a voz da fala 8 termina por cima na edição)",
    "T11": "(sem fala no take: a fala 11 entra como voz-over na edição)",
}
MOMENTO = {"T1": "0,0 a 3,8 s", "T2": "3,8 a 5,6 s", "T3": "5,6 a 6,7 s", "T4": "6,7 a 7,8 s", "T5": "7,8 a 8,7 s",
           "T6": "8,7 a 9,9 s", "T7": "9,9 a 14,0 s", "T8": "14,0 a 16,5 s", "T9": "16,5 a 18,0 s",
           "T10": "18,0 a 19,4 s", "T11": "19,4 a 22,9 s"}


def keyframes():
    out = []
    for i, t in enumerate(TAKES, 1):
        d = K[t]
        cod = f"K{i:02d}"
        boca = (f"Start frame: Brandon is {BOCA}, {d['est']}." if t in FALAS and not d.get("sem_rosto") and t not in VOZ_OVER
                else f"Start frame: {d['f0']}.")
        j = {
            "shot_id": f"{cod}_{t.lower()}",
            "fiction_note": FICCAO,
            "reference_use": REF_PROD if t in PRODUTO_T else REF,
            "identity_main": B["identidade"],
            "wardrobe": B["roupa"],
            "scene": B["cena"],
            "prop": d["prop"],
            "posture": d["pose"] + ".",
            "composition": d["comp"],
            "camera": d["cam"],
            "lighting": LUZ,
            "state": boca,
            "realism": REALISMO,
            "aspect_ratio": "9:16 vertical",
            "negative": NEG + (NEG_PRODUTO if t in PRODUTO_T else NEG_SEM_ROTULO),
        }
        out.append(dict(codigo=cod, take=t, titulo=d["titulo"], j=j))
    return out


def anexos(k):
    lst = [f"ÂNCORA HOLISTIC BRANDON `{ANCORA}`", f"FRAME DO MODELO `{frame_modelo(k['codigo'])}` (só composição)"]
    if k["take"] in PRODUTO_T:
        lst.append(f"FOTO DO PRODUTO `{FOTO_PRODUTO}` (só o pote da frente)")
    return lst


def com_boca(t):
    return t in FALAS and t not in VOZ_OVER


def ficha(ks):
    L = ["# FICHA DO FRAME · brandon_seamoss_gengibre_limao", "",
         "Regra e método: `GATE_VISUAL.md` Parte 6. Cada K sai daqui, nunca da memória. O frame do modelo manda no",
         "CONTEÚDO (forma, quadro, distância, câmera, pose, o que está em quadro); o gate manda no ACABAMENTO e impõe o",
         "piso de proximidade do herói. A evidência de cada OK é um trecho que existe literalmente no K",
         "(conferido por `gerar_pacote.py` com assert antes de gravar).", ""]
    for k in ks:
        t, cod, j = k["take"], k["codigo"], k["j"]
        d = K[t]
        texto = json.dumps(j, ensure_ascii=False)
        comp = j["composition"]
        m_pct = re.search(r"fills? (?:about |the (?:lower |upper )?(?:right )?)?\d+ percent of the frame", comp)
        m_cm = re.search(r"about \d+ centimeters from [a-z ]+?(?=[,.])", comp)
        assert m_pct and m_cm, (cod, comp)
        ev = dict(F2=m_pct.group(0), F3=m_cm.group(0), F4="standard 1x lens", F5=d["pose"][:55].rsplit(" ", 1)[0],
                  F6=d["f6"])
        ev = {it: f'"{v}"' for it, v in ev.items()}
        ev.update(G1='"Neutral overcast daylight"', G3='"everything in sharp focus"', G4='"Real skin with visible pores"',
                  G5='"no warm orange color cast"', G6='"no captions"', G7='"small American flag"',
                  G8='"caught mid-sentence, lips naturally parted"')
        ev["F1"] = " · ".join(f'"{x}"' for x in d["termos"])
        for item, e in ev.items():
            if item == "G8" and not com_boca(t):
                continue
            for trecho in re.findall(r'"([^"]+)"', e):
                assert trecho.lower() in texto.lower(), (cod, item, trecho)
        desvio = d.get("desvio", "cabana de toras e bancada de madeira → box de treino e mesa preta (avatar fixo); "
                                 "homem de suspensório → mãos e antebraço dela com a tatuagem da âncora; luz neutra (gate)")
        L += [f"## {cod}", f"Frame: `{frame_modelo(cod)}`", f"Take: {t}", f"Herói: {d['heroi']}",
              "Termos de forma: " + ev["F1"], f"Quadro: no K: {m_pct.group(0)} (medido contra o frame do modelo)",
              f"Distância da lente: {m_cm.group(0)}", f"Câmera: {j['camera']}", f"Pose: {d['pose']}",
              f"Lista fechada: {d['lista']}", f"Frame 0: {d['f0']}", f"Desvio (acabamento ou avatar fixo): {desvio}", "",
              "| Item | Status | Evidência (trecho literal do K) |", "|---|---|---|"]
        nomes = ["F1 forma do heroi", "F2 quanto do quadro", "F3 distancia da lente", "F4 camera",
                 "F5 pose do avatar", "F6 lista fechada", "G1 luz neutra", "G2 ceu ou janela", "G3 foco",
                 "G4 realismo", "G5 sem tom quente", "G6 sem texto", "G7 bandeira", "G8 boca no K de fala"]
        for nome in nomes:
            it = nome[:2]
            if it == "G2":
                L.append(f"| {nome} | N/A | sem janela nem céu em quadro: a janela fica fora do quadro, só a luz entra |")
            elif it == "G8" and not com_boca(t):
                L.append(f"| {nome} | N/A | take sem a boca dela em quadro: B-roll de mãos e utensílios, voz-over ou mudo |")
            else:
                L.append(f"| {nome} | OK | {ev[it]} |")
        L.append("")
    return "\n".join(L)


def videos():
    vs = []
    n = B["nome"]
    for i, t in enumerate(TAKES, 1):
        som = f"{B['som']}{SOM.get(t, '')}"
        cam = "fixa" if t in PRODUTO_T else "leve handheld natural"
        acao = ACOES[t].format(n=n)
        if t in ABRE_MUDO:
            txt = (f"{ABRE_MUDO[t]}\n\no que acontece no vídeo: {acao}\n\ncâmera: {cam}\n\n"
                   f"som ambiente: {som}, sem música")
        else:
            if "CENA CURTA" in HEADS[t]:
                acao += " Ela diz a frase em ritmo natural logo no começo e a ação continua até o fim."
            txt = (f"a avatar {n}, mulher, fala em inglês com sotaque americano {B['sotaque']}, {B['voz']}, "
                   f"{EMOCAO[t]}, voz autêntica, como se exigisse ser ouvida, a seguinte frase: \"{FALAS[t]}\"\n\n"
                   "a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por "
                   "inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.\n\n"
                   f"o que acontece no vídeo: {acao}\n\n"
                   f"câmera: {cam}\n\n"
                   f"som ambiente: {som}, sem música")
        vs.append((f"V{i:02d}", t, f"K{i:02d}", txt))
    return vs


ORDEM_K = ["fiction_note", "reference_use", "identity_main", "wardrobe", "scene", "prop", "posture",
           "composition", "camera", "lighting", "state", "realism", "aspect_ratio", "negative"]


def texto_flow(j):
    assert set(ORDEM_K) == set(j) - {"shot_id"}, set(j) ^ set(ORDEM_K)
    d = {"format": "IMPORTANT: THIS IS IPHONE FOOTAGE. Vertical 9:16."}
    d.update({k: j[k] for k in ORDEM_K})
    return json.dumps(d, ensure_ascii=False, indent=2)


def bloco_anexo(k):
    lst = anexos(k)
    nums = ["1️⃣", "2️⃣", "3️⃣"]
    L = [f"> ### 📎 ANEXAR: **{len(lst)} IMAGENS**"] + [f"> **{nums[i]} {a}**" for i, a in enumerate(lst)]
    return "\n".join(L + [">", "> ### 🆕 GERAR DO ZERO"])


def capcut():
    return [
        "1. Clipes numerados na ordem: V01 a V16.",
        "2. Do V01 ao V11, cortar no tempo da cena do modelo: " + "; ".join(
            f"V{t[1:].zfill(2)} {MOMENTO[t]}" for t in MOMENTO) + ". Do V12 ao V16, cortar logo depois da última palavra.",
        "3. Voz: V01, V08, V10 e V12 a V16 têm fala e lip sync. V02, V04, V07 e V11 são B-roll com a fala de mesmo número "
        "como voz-over (usar o áudio do V que tem a fala escrita no roteiro, ou gravar a voz na edição). V03, V05, V06 e "
        "V09 são inserts mudos. Isolate Voice / Keep Vocal no áudio.",
        "4. A voz dos takes B-roll segue a fala do roteiro, na ordem: 1, 2, 4, 7, 8, 10, 11, sobre as imagens do modelo.",
        "5. Legenda branca serifada, duas a três palavras por vez, com a palavra de peso maior, no meio do quadro, igual "
        "ao modelo. Texto fixo no topo do V01: \"My trick for feeling my best\". No V15, `yes` grande e isolado na tela. "
        "No V16, setas apontando para a legenda do post.",
        "6. Sem Voice Changer: a voz vem do prompt de cada V.",
        "7. Música só depois do gancho (a partir do V02), entre -19 e -20 dB, fora da biblioteca do TikTok.",
        "8. Rótulo pequeno `Synthetic performer` num canto do vídeo.",
        "9. Do V13 ao V16 o frasco não pode ser cortado nem coberto: nenhum B-roll por cima (regra da marca).",
    ]


LEGENDA = [
    "Primeira linha, sempre: `#ad #syntheticperformer #naturalrems`",
    "Logo abaixo: o link da Amazon do Natural Rems Sea Moss (o V16 manda tocar no link da legenda).",
    "Chave de conteúdo de IA da plataforma LIGADA.",
]


def transcricao():
    L = ["| Take | English | Português |", "|---|---|---|"]
    for t in TAKES:
        L.append(f"| {t} | {TRANSCRICAO_EN[t]} | {TRANSCRICAO_PT[t]} |")
    return L


def pacote():
    ks, vs = keyframes(), videos()
    L = ["# holistic.brandon | Ângulo 1 Natural Rems Sea Moss | Gengibre e limão em cubos de freezer | Pacote de Prompts", "",
         "Vídeo modelo: `input/reference_video.mp4` (25,2 s, avatar IA)", "",
         f"Âncora: `{ANCORA}` · Foto do produto: `{FOTO_PRODUTO}`", "",
         "Funil: venda Amazon. Frasco em quadro, comment `yes` + follow antes, \"Search Natural Rems Sea Moss on "
         "Amazon\" depois, link da legenda do post e fim. Rodada de validação, gancho fiel ao modelo.", "",
         "## Índice de geração", "", "| Take | Keyframe | Anexar | Ação |", "|---|---|---|---|"]
    for k in ks:
        L.append(f"| {k['take']} | {k['codigo']} | {' + '.join(a.split(' `')[0] for a in anexos(k))} | GERAR DO ZERO |")
    L += ["", "Todo K é GERAR DO ZERO: o bloco do Flow é autossuficiente e cada K descreve o cenário inteiro, "
          "então não existe `EDITAR do K__` aqui. O frame do modelo de cada K entra só como composição.", "",
          "## Trava de identidade e continuidade", "",
          f"- Identidade: {B['identidade']}", f"- Roupa (fixa da conta): {B['roupa']}",
          f"- Cenário-base (fixo da conta): {B['cena']}", f"- Luz: {LUZ}",
          f"- Voz (mesmo timbre em todos os V): {B['voz']}, sotaque americano {B['sotaque']}.",
          "- Sem 2ª pessoa. Nos B-roll de mãos aparecem só as mãos e o antebraço direito com a tatuagem da âncora.", "",
          "## Trava do prop herói", "",
          f"- Receita: {LIMAO}, {GENGIBRE}, {TABUA}, {COPO} (base de liquidificador preta), {FORMINHAS} e {CANECA}; "
          "a mistura é lisa, creme claro, com fibras mínimas. Nada tem marca legível.",
          f"- Produto (T13 a T16): {FRASCO}. Referência: `{FOTO_PRODUTO}`, só o pote da frente, sem a faixa MADE IN USA, "
          "sem o pote de trás e sem as gomas soltas.", "",
          "## Trava da 2ª pessoa (REF-A)", "", "- Não se aplica: não há 2ª pessoa.", "", "## Prompts de imagem", ""]
    for k in ks:
        L += [f"## {k['codigo']} · {k['take']} · GERAR DO ZERO · " + " + ".join(a.split(" `")[0] for a in anexos(k)), "",
              bloco_anexo(k), "", f"Cena: {k['titulo']}.", "", "```json",
              json.dumps(k["j"], ensure_ascii=False, indent=2), "```", ""]
    L += ["## Bloco global de vídeo", "", "```text",
          f"a avatar {B['nome']}, mulher, fala em inglês com sotaque americano {B['sotaque']}, {B['voz']}, "
          "[emoção da fala], voz autêntica, como se exigisse ser ouvida, a seguinte frase: \"[FALA EXATA DO ROTEIRO]\"", "",
          "a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.", "",
          "o que acontece no vídeo: [ação enxuta]", "", "câmera: [fixa / leve handheld]", "", f"som ambiente: {B['som']}, sem música",
          "```", "", "# Prompts de vídeo", ""]
    for cod, take, kcod, txt in vs:
        L += [f"### {cod} · {take} · usa {kcod}", "", "```text", txt, "```", ""]
    L += ["## Mapa de âncoras", "", "| Keyframe | Referências a anexar | Modelo |", "|---|---|---|"]
    for k in ks:
        L.append(f"| {k['codigo']} | " + " + ".join(anexos(k)) + " | Nano Banana 2, 9:16 |")
    L += ["", "## Montagem no CapCut", ""] + capcut() + ["", "Legenda do post:", ""] + [f"- {x}" for x in LEGENDA] + [
          "", "## Gates de qualidade", "",
          "1. Fala de cada V igual ao ROTEIRO, palavra por palavra.",
          "2. Um take por cena do modelo; cenas curtas marcadas; nenhum take acima de 29 palavras.",
          "3. Bandeira dos EUA no campo scene de todo K.", "4. Zero travessão.",
          "5. Natural Rems: frasco parado e legível do V13 ao V16; comment `yes` + follow no V15, antes da Amazon; nada depois do link.",
          "6. Compliance da marca: nada médico, sem antes/depois, sem cura ou resultado garantido, sem concorrente; legenda com `#ad #syntheticperformer #naturalrems` no topo.",
          "7. GATE_VISUAL Partes 1 a 3 em todo K: herói colado na lente, luz neutra, sem tom quente, sem blur, trecho de realismo.",
          "8. Gancho fiel no conteúdo: o limão sendo ralado com o zester colado na lente, falado desde o segundo 0.",
          "9. Um K = um V; a queda do cubo, a água entrando e o liquidificador batendo nascem no vídeo.", ""]
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
        flow.append(f"| {k['codigo']} / V{k['codigo'][1:]} | {k['take']}, {k['titulo']} | " + " + ".join(anexos(k)) + " |")
    flow += ["", "## Transcrição final por take", ""] + transcricao()
    return "\n".join(L) + "\n", "\n".join(flow) + "\n"


def main():
    p, f = pacote()
    (AQUI / "PROMPTS_BRANDON.md").write_text(p, encoding="utf-8")
    (AQUI / "FLOW_BRANDON.md").write_text(f, encoding="utf-8")
    (AQUI / "PROMPTS_PRODUCAO.md").write_text(p, encoding="utf-8")
    (AQUI / "FICHA_FRAMES.md").write_text(ficha(keyframes()), encoding="utf-8")
    print("ok: pacote da Brandon; PROMPTS_PRODUCAO.md = holistic.brandon; FICHA_FRAMES.md com %d K" % len(TAKES))


if __name__ == "__main__":
    main()
