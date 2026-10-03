"""Gera o pacote da producao brandon_seamoss_vizinha (Angulo 1, Natural Rems Sea Moss, VENDA, validacao).

Formato: movie style familia B. A esquete (T1 a T15) tem elenco proprio com character sheets REF-P1 a
REF-P3; da indicacao em diante (T16 a T35) e a holistic.brandon, avatar fixo da conta, no box de treino.

Fonte unica da fala: ROTEIRO.md aprovado (lido do disco, nunca redigitado). Medidas de cada K: a ficha
abaixo, escrita olhando input/frames_modelo/Kxx_modelo.png e gravada em FICHA_FRAMES.md com o placar
cuja evidencia e conferida aqui mesmo contra o texto do K (assert). Prompt de imagem em JSON (Flow v17).
Gabarito de formato: brandon_maca_alho/gerar_pacote.py e sf_madrasta_frango (REF-P e V de dialogo).

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
assert TAKES == ["T%d" % i for i in range(1, 36)], TAKES
FALAS = {}
for bloco in re.split(r"^(?=### T\d+ · )", ROTEIRO, flags=re.M)[1:]:
    m = re.search(r'^> "(.+?)"\s*$', bloco.split("\n## ")[0], re.M)
    if m:
        FALAS[re.match(r"### (T\d+)", bloco).group(1)] = m.group(1)
MUDOS = {"T1", "T2", "T15"}
assert set(FALAS) == set(TAKES) - MUDOS, sorted(set(TAKES) - set(FALAS))
TRANSCRICAO_PT = dict(re.findall(r"^\| (T\d+) \| [^|]+ \| .+? \| (.+?) \|$",
                                 ROTEIRO.split("## Tabela bilíngue")[1].split("\n## ")[0], re.M))
assert set(TRANSCRICAO_PT) == set(TAKES), set(TAKES) - set(TRANSCRICAO_PT)

ESQUETE = ["T%d" % i for i in range(1, 16)]
BRANDON_T = ["T%d" % i for i in range(16, 36)]
PRODUTO_T = {"T31", "T32", "T33", "T34", "T35"}

FICCAO = "This is a fictional AI-generated scene with fictional characters, no real person is depicted."
FICCAO_B = "This is a fictional AI-generated character, no real person is depicted."
ANCORA = "producao/_ancoras/holistic_brandon_ancora.jpg"
FOTO_PRODUTO = "producao/_ancoras/natural_rems_seamoss_produto.jpg"


def frame_modelo(cod):
    return f"input/frames_modelo/{cod}_modelo.png"


REALISMO = ("Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural "
            "clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday "
            "reality, background fully in focus, everything in sharp focus, no AI polish, no beauty smoothing.")
NEG_COMUM = ("no captions, no subtitles, no words overlaid on the image, no plastic-looking skin, no extra fingers, "
             "no third hand, no blur, no bokeh, no warm orange color cast, no yellow tint, no golden glow, no golden "
             "hour light, no sunset, no HDR, no cinematic lighting, no beauty smoothing, no visible phone")

# ------------------------------------------------------------------ esquete: elenco e cenario
P = {
    "P1": dict(nome="VIZINHA", rotulo="the neighbor",
               ident=("The neighbor: a fictional white American woman who looks about thirty, slim and athletic with a "
                      "toned flat stomach, long straight light blonde hair past her shoulders, fair skin, light blue "
                      "eyes, thin clear round eyeglasses with a pale gold frame"),
               roupa=("the neighbor wears a plain black sports bra top with nothing printed on it, high-waisted navy "
                      "blue bike shorts and black gardening gloves"),
               curto="mulher loira de óculos redondos, top preto e luvas pretas",
               voz="voz feminina de uma mulher de uns trinta anos, média, clara e segura, sotaque americano do sul, leve"),
    "P2": dict(nome="MARIDO", rotulo="the husband",
               ident=("The husband: a fictional white American man around thirty-two, very muscular and lean, "
                      "shirtless, broad defined chest and visible abs, lightly tanned skin, short dark brown hair swept "
                      "up, light stubble, grey-blue eyes"),
               roupa=("the husband wears only loose grey athletic shorts with a black drawstring, a black smartwatch "
                      "on his left wrist and a thin gold wedding ring, no shirt"),
               curto="homem sarado sem camisa, de short cinza",
               voz="voz masculina de barítono de um homem de uns trinta anos, confiante e galanteadora, sotaque americano padrão"),
    "P3": dict(nome="ESPOSA", rotulo="the wife",
               ident=("The wife: a fictional white American woman around thirty-five, plus-size with a full round "
                      "body, brown hair pulled back in a messy ponytail, fair skin flushed pink from running, blue-grey "
                      "eyes"),
               roupa=("the wife wears a heather grey sports bra, grey leggings, light grey running shoes and a black "
                      "smartwatch"),
               curto="mulher acima do peso de top e legging cinza",
               voz=""),
}
RUA = ("A quiet suburban Texas street right after rain: a wet light grey concrete sidewalk with small puddles, a neat "
       "green lawn and a dense trimmed green hedge, two-story houses of pale cream stone with dark grey roofs, big "
       "leafy oak trees, and on the porch of one house a small American flag hanging from a short pole, discreet but "
       "clearly visible and in focus. The sky above the houses is overcast pale grey with visible soft cloud texture, "
       "never blown white.")
LUZ_RUA = ("Neutral overcast daylight, soft even light on every face and body with no harsh shadows, the cloudy sky "
           "clearly visible with soft grey texture, no warm orange cast and no yellow tint.")
NEG_RUA = NEG_COMUM + ", no blown white sky, no sunshine, no harsh shadows, no studio, no fourth person, no dog"
CAM_RUA = "phone held at adult chest height by someone standing with them on the sidewalk, standard 1x lens, light handheld"
BOCA = "caught mid-sentence, lips naturally parted, animated expression"


def ref_esquete(ps):
    ordem = ["first", "second", "third"]
    partes = [f"{P[p]['rotulo']} is the person in the {ordem[i]} character sheet" for i, p in enumerate(ps)]
    return ("Use the attached character sheets ONLY for faces, hair, bodies and clothes: " + "; ".join(partes) +
            ". The last attached image is a composition reference only: copy its camera position, framing and where "
            "each person stands, never its faces, bodies, clothes, houses or caption text.")


# Cada K da esquete: elenco em quadro (ordem dos anexos), prop, pose, composicao, camera, estado.
# A FICHA sai das mesmas strings (F2 quadro, F3 distancia, F5 pose, F6 lista), por isso a evidencia bate.
ESQ = {
    "T1": dict(ps=["P1", "P2", "P3"], titulo="plano aberto mudo, vizinha podando e o casal correndo",
               prop="Long-handled wooden hedge shears in the neighbor's gloved hands, the blades open against the hedge.",
               pose=("the neighbor stands in profile in the left foreground, bent forward at the hips, trimming the "
                     "hedge; far behind her on the wet sidewalk, the husband and the wife jog side by side toward the "
                     "camera"),
               quadro=("the neighbor is about 100 centimeters from the lens and fills the left 40 percent of the frame from "
                       "head to knees; the husband and the wife are about six meters away in the center and right, "
                       "each about 25 percent of the frame tall"),
               cam=CAM_RUA, estado="Start frame: mid-stride jogging, the shears half closed, nobody has spoken yet.",
               lista="vizinha com a tesoura, cerca viva, marido e esposa correndo, calçada, casas, árvores, bandeira",
               heroi="o contraste: a vizinha sarada podando no primeiro plano e o casal correndo ao fundo",
               termos=["bent forward at the hips, trimming the hedge", "jog side by side toward the camera"]),
    "T2": dict(ps=["P3"], titulo="close da esposa em choque",
               prop="No object in her hands; both palms pressed flat against the sides of her head.",
               pose=("the wife stares past the camera in shock, both palms pressed flat against the sides of her head, "
                     "eyes wide open, mouth stretched wide open in a silent gasp"),
               quadro=("the wife's face is about 25 centimeters from the lens and fills the upper 70 percent of the "
                       "frame, her shoulders and grey sports bra at the bottom edge"),
               cam="phone held at her eye level, wide 0.5x lens, light handheld",
               estado="Start frame: frozen mid-gasp, mouth wide open, eyebrows high.",
               lista="esposa, mãos na cabeça, árvores e céu atrás",
               heroi="o rosto da esposa em choque, mãos coladas na cabeça, boca escancarada",
               termos=["both palms pressed flat against the sides of her head", "mouth stretched wide open"]),
    "T3": dict(ps=["P1", "P2", "P3"], titulo="o marido chega na vizinha",
               prop="The hedge shears hang from the neighbor's gloved hand.",
               pose=("seen over the neighbor's shoulder, the husband walks up toward her smiling, one hand raised in a "
                     "small wave; the wife is still jogging, small, on the sidewalk behind him"),
               quadro=("the neighbor's bare shoulder and blonde hair are about 20 centimeters from the lens, cut by the "
                       "left edge and filling the left 25 percent of the frame; the husband is about two meters away in "
                       "the center, from the thighs up, filling 50 percent of the frame height"),
               cam=CAM_RUA, estado=f"Start frame: the husband mid-step, {BOCA}.",
               lista="ombro e cabelo da vizinha, marido, esposa ao fundo, calçada, casas, bandeira",
               heroi="o marido chegando sorridente, visto por cima do ombro da vizinha",
               termos=["seen over the neighbor's shoulder", "one hand raised in a small wave"]),
    "T4": dict(ps=["P1", "P2"], titulo="a vizinha se vira",
               prop="The neighbor holds the wooden hedge shears closed in front of her waist.",
               pose="the neighbor has just turned toward the husband, polite and cool, holding the shears",
               quadro=("the neighbor is about 70 centimeters from the lens, from the waist up, filling 60 percent of "
                       "the frame; the husband's bare shoulder is about 20 centimeters from the lens, cut by the right "
                       "edge"),
               cam=CAM_RUA, estado=f"Start frame: the neighbor is {BOCA}.",
               lista="vizinha com a tesoura, ombro do marido, casa de pedra, árvore, bandeira",
               heroi="a vizinha virando, tesoura na mão, casa de pedra atrás",
               termos=["holding the shears", "the husband's bare shoulder"]),
    "T5": dict(ps=["P2", "P3", "P1"], titulo="o marido se apresenta, a esposa ofegante atrás",
               prop="No props in the husband's hands.",
               pose=("the husband stands facing the neighbor, gesturing with an open hand toward the house next door; "
                     "behind him on the sidewalk the wife is bent over with her hands on her knees, catching her "
                     "breath"),
               quadro=("the husband is about 120 centimeters from the lens, from the hips up, filling 55 percent of the frame "
                       "at the right of center; the wife is about four meters behind him, small, about 20 percent of "
                       "the frame tall; the neighbor's bare shoulder and blonde hair are about 20 centimeters from the "
                       "lens, cut by the left edge"),
               cam=CAM_RUA, estado=f"Start frame: the husband is {BOCA}.",
               lista="marido, esposa curvada ao fundo, ombro da vizinha, calçada, casas, bandeira",
               heroi="o marido se apresentando enquanto a esposa, ao fundo, está curvada com as mãos nos joelhos",
               termos=["gesturing with an open hand toward the house next door", "bent over with her hands on her knees"]),
    "T6": dict(ps=["P2"], titulo="close do marido, you look so fine",
               prop="A leafy green hedge branch pokes into the lower left corner of the frame.",
               pose="the husband looks just past the lens at the neighbor with a flirty half smile",
               quadro=("the husband's face and chest are about 40 centimeters from the lens and fill 70 percent of the "
                       "frame; the hedge branch is about 10 centimeters from the lens in the lower left corner"),
               cam=CAM_RUA, estado=f"Start frame: the husband is {BOCA}, flirty.",
               lista="marido, galho da cerca, casa e árvore atrás, bandeira",
               heroi="o rosto e o peito do marido, sorriso galanteador",
               termos=["flirty half smile", "leafy green hedge branch"]),
    "T7": dict(ps=["P1", "P3", "P2"], titulo="a vizinha aponta a esposa correndo",
               prop="The hedge shears hang from the neighbor's gloved hand.",
               pose=("the neighbor, in three-quarter view, glances past the husband toward the wife, who is jogging "
                     "away down the sidewalk with her back to the camera"),
               quadro=("the neighbor is about 80 centimeters from the lens, from the waist up, filling the left 55 "
                       "percent of the frame; the husband's bare arm is about 20 centimeters from the lens, cut by the "
                       "right edge; the wife is about eight meters away in the center, small, about 15 percent of the "
                       "frame tall"),
               cam=CAM_RUA, estado=f"Start frame: the neighbor is {BOCA}, eyebrows slightly raised.",
               lista="vizinha, braço do marido, esposa de costas correndo, calçada, casas, bandeira",
               heroi="a vizinha olhando a esposa que se afasta correndo",
               termos=["jogging away down the sidewalk with her back to the camera"]),
    "T8": dict(ps=["P2", "P1", "P3"], titulo="o marido de perfil, if my wife looked like you",
               prop="A hedge branch crosses the lower foreground.",
               pose=("the husband stands in profile looking at the neighbor, one hand open toward her; far behind, the "
                     "wife keeps jogging away"),
               quadro=("the husband is about 100 centimeters from the lens, from the hips up, filling the right 50 percent of "
                       "the frame; the neighbor is cut by the left edge; the wife is about fifteen meters away, tiny, "
                       "about 8 percent of the frame tall; the hedge branch is about 15 centimeters from the lens"),
               cam=CAM_RUA, estado=f"Start frame: the husband is {BOCA}.",
               lista="marido de perfil, borda da vizinha, esposa ao longe, galho, calçada, casas, bandeira",
               heroi="o marido de perfil falando com a vizinha, a esposa pequena ao fundo",
               termos=["stands in profile looking at the neighbor"]),
    "T9": dict(ps=["P1", "P2"], titulo="close da vizinha, start doing what I do",
               prop="The wooden handle of the hedge shears in her gloved hand at the bottom of the frame.",
               pose="the neighbor looks at the husband, dry and unimpressed",
               quadro=("the neighbor is about 45 centimeters from the lens, from the chest up, filling 65 percent of "
                       "the frame; the husband's shoulder is about 20 centimeters from the lens, cut by the right edge"),
               cam=CAM_RUA, estado=f"Start frame: the neighbor is {BOCA}, no smile.",
               lista="vizinha, cabo da tesoura, ombro do marido, casa de pedra com janela, bandeira",
               heroi="o rosto da vizinha, seca, sem sorrir",
               termos=["dry and unimpressed"]),
    "T10": dict(ps=["P2"], titulo="close do marido, hitting the gym",
                prop="Hedge leaves in the lower left corner of the frame.",
                pose="the husband tilts his head, curious and still flirting",
                quadro=("the husband's face and chest are about 40 centimeters from the lens and fill 70 percent of the "
                        "frame; the hedge leaves are about 10 centimeters from the lens in the lower left corner"),
                cam="phone held just below his chin height, tilted slightly up, standard 1x lens, light handheld",
                estado=f"Start frame: the husband is {BOCA}.",
                lista="marido, folhas da cerca, casas e árvores atrás, bandeira",
                heroi="o rosto do marido, curioso",
                termos=["tilts his head, curious"]),
    "T11": dict(ps=["P1", "P2"], titulo="a vizinha volta a podar, I am fifty-seven",
                prop="The wooden hedge shears open in both gloved hands, against the hedge.",
                pose="the neighbor is back at the hedge, shears open in both hands, glancing back over her shoulder",
                quadro=("the neighbor is about 90 centimeters from the lens, from the knees up, filling 55 percent of "
                        "the frame; the husband's bare arm is about 20 centimeters from the lens, cut by the right edge"),
                cam=CAM_RUA, estado=f"Start frame: the neighbor is {BOCA}, matter-of-fact.",
                lista="vizinha com a tesoura aberta, cerca viva, braço do marido, casa de pedra, bandeira",
                heroi="a vizinha podando e respondendo por cima do ombro",
                termos=["shears open in both hands, glancing back over her shoulder"]),
    "T12": dict(ps=["P2"], titulo="close do marido em choque, what",
                prop="No props.",
                pose="the husband stares straight ahead in total shock, eyebrows raised high, mouth open",
                quadro="the husband's face is about 35 centimeters from the lens and fills 60 percent of the frame",
                cam="phone held at his eye level, standard 1x lens, straight-on, light handheld",
                estado=f"Start frame: the husband is {BOCA}, frozen in shock.",
                lista="marido, casas e árvores atrás, bandeira",
                heroi="o rosto do marido em choque",
                termos=["eyebrows raised high, mouth open"]),
    "T13": dict(ps=["P2", "P1"], titulo="o marido, what's your secret",
                prop="Hedge branches in the lower foreground.",
                pose="the husband faces the neighbor, hands open in disbelief",
                quadro=("the husband is about 100 centimeters from the lens, from the hips up, filling 60 percent of the "
                        "frame; the neighbor's shoulder is cut by the left edge; the hedge branches are about 15 "
                        "centimeters from the lens at the bottom"),
                cam=CAM_RUA, estado=f"Start frame: the husband is {BOCA}, amazed.",
                lista="marido, borda da vizinha, galhos da cerca, calçada, casas, bandeira",
                heroi="o marido incrédulo, mãos abertas",
                termos=["hands open in disbelief"]),
    "T14": dict(ps=["P1", "P2"], titulo="a indicação, this holistic coach",
                prop=("A bunch of freshly cut hedge branches in the neighbor's right gloved hand and an open black "
                      "garbage bag held in her left gloved hand."),
                pose="the neighbor faces the husband, holding up the cut branches and the garbage bag",
                quadro=("the neighbor is about 80 centimeters from the lens, from the waist up, filling 60 percent of "
                        "the frame; the husband's hand is about 20 centimeters from the lens at the lower right edge"),
                cam=CAM_RUA, estado=f"Start frame: the neighbor is {BOCA}, casual.",
                lista="vizinha com galhos e saco preto, mão do marido, casas, árvore, bandeira",
                heroi="a vizinha com os galhos podados e o saco de lixo, contando o segredo",
                termos=["freshly cut hedge branches", "open black garbage bag"]),
    "T15": dict(ps=["P2"], titulo="close do marido ouvindo, mudo",
                prop="No props.",
                pose="the husband listens in silence, mouth closed, slowly taking it in",
                quadro="the husband's face and chest are about 35 centimeters from the lens and fill 65 percent of the frame",
                cam="phone held at his eye level, standard 1x lens, straight-on, light handheld",
                estado="Start frame: mouth closed, a slow blink.",
                lista="marido, casas e árvores atrás, bandeira",
                heroi="o marido ouvindo calado",
                termos=["listens in silence, mouth closed"]),
}

# ------------------------------------------------------------------ Brandon (avatar fixo da conta)
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
          "visible and in focus. In front of her stands a plain matte black table."),
    voz="voz feminina clara e firme de uma mulher de uns trinta anos",
    sotaque="de uma mulher negra americana",
    som="box de treino em casa, tranquilo",
)
LUZ_BOX = ("Neutral overcast daylight from a large window out of frame, soft even light on her face, hands and the "
           "table with no harsh shadows. The red neon glows on the wall but does not tint her skin.")
NEG_BOX = (NEG_COMUM + ", no studio, no second person, no eyeglasses, no grey curly hair, no wooden bench, no street, "
           "no houses, no silver cross")
NEG_SEM_ROTULO = ", no printed labels or lettering on the glass, bowls or jar"
NEG_PRODUTO = (", no second jar, no other bottles, no loose gummies, no banner above the jar, no hand covering "
               "the label")
REF_B = ("Use the first attached image only for Brandon's exact identity, wardrobe and own garage gym with the black "
         "table. Use the second attached image only as a composition reference for the camera position, framing and "
         "how the object is held; do not copy its person, grey curly hair, eyeglasses, wooden bench, street, houses or "
         "the caption text.")
REF_B_PROD = (REF_B + " Use the third attached image only for the Natural Rems Sea Moss jar: copy ONLY the front jar, "
              "without the MADE IN USA banner at the top, without the second jar behind it and without the loose "
              "gummies.")
FRASCO = ("the Natural Rems Sea Moss jar: a short wide jar of dark amber plastic with a black screw cap, a pale "
          "cream-green label with dark green text, the Natural Rems logo with three leaves, the big title Sea Moss "
          "Gummies, a 6000 MG | 16-IN-1 badge, the words GREEN APPLE FLAVOR, a list of ingredients in dark green pill "
          "shapes and green seaweed illustrations on both sides, label facing the camera, fully readable")
COPO = "a clear drinking glass of warm water"
LIMAO = "half a lemon with its cut side facing the lens"
TIGELA = ("a small clear glass bowl with a pale creamy yellow mixture of apple cider vinegar and coconut oil, "
          "smooth and slightly glossy")
POTE = ("a wide clear glass jar filled with dried raw Irish sea moss: tangled pale golden and beige seaweed strands "
        "with a light frosty sea-salt coating")
GEL = "a small clear glass bowl holding a spoonful of smooth pale beige sea moss gel, glossy and jelly-like"
ACUCAR = "a small clear glass bowl heaped with white granulated sugar"
PO = "a small clear glass bowl heaped with a fine white powder"
CAM_B = "phone at her chest height, straight-on, standard 1x lens, light handheld"


def comp_b(objeto, cm, pct, extra=""):
    return (f"Straight-on medium shot{extra}: the phone lens is about {cm} centimeters from {objeto}, which fills "
            f"the lower {pct} percent of the frame, closer to the camera than her face; her face and shoulders fill "
            "the upper half of the frame. The black table edge is at the bottom. The background is reduced by "
            "framing, never by blur.")


BR = {
    "T16": dict(titulo="credencial de coach, mãos na mesa", prop="Nothing in her hands; the black table is empty.", f6="the black table is empty",
                pose="Brandon stands behind the black table, both hands resting flat on it, shoulders square to the lens",
                comp=("Straight-on medium shot from the waist up: the phone lens is about 60 centimeters from her, she "
                      "fills 60 percent of the frame, her hands resting flat on the black table at the bottom edge. The "
                      "background is reduced by framing, never by blur."),
                obj="her", cm=60, pct=60, est="calm and sure",
                lista="avatar, mesa preta vazia, neon, quadro branco, bandeira",
                heroi="a própria Brandon, mãos espalmadas na mesa preta (pose da âncora)",
                termos=["both hands resting flat on it"],
                desvio="apresentadora sentada num banco na rua → Brandon em pé atrás da mesa preta no box (avatar fixo da conta)"),
    "T17": dict(titulo="receita 1, copo e meio limão", obj="the glass and the lemon", cm=25, pct=30,
                prop=f"{COPO[0].upper()}{COPO[1:]} in her left hand and {LIMAO} in her right hand, both held at chest height.",
                pose="Brandon holds the glass and the lemon half out toward the lens, the lemon tilted above the glass",
                est="about to squeeze the lemon into the glass",
                lista="copo de água, meio limão, avatar, mesa vazia",
                heroi="copo de água morna e meio limão erguidos na altura do peito",
                termos=["clear drinking glass of warm water", "half a lemon with its cut side facing the lens"]),
    "T18": dict(titulo="receita 1, benefício", obj="the glass and the lemon", cm=25, pct=30,
                prop=f"{COPO[0].upper()}{COPO[1:]} in her left hand and {LIMAO} in her right hand, both held at chest height.",
                pose="Brandon holds the glass and the lemon half side by side at chest height",
                est="lively and certain", lista="copo de água, meio limão, avatar, mesa vazia",
                heroi="copo e meio limão lado a lado na altura do peito",
                termos=["clear drinking glass of warm water", "half a lemon with its cut side facing the lens"]),
    "T19": dict(titulo="ponte para a pele", obj="the glass and the lemon", cm=30, pct=25, extra=" from slightly above",
                prop=f"{COPO[0].upper()}{COPO[1:]} in her left hand and {LIMAO} in her right hand, lowered a little.",
                pose="Brandon holds the glass and the lemon half a little lower, about to put them down",
                est="raising one eyebrow, turning a point", lista="copo de água, meio limão, avatar, mesa vazia",
                heroi="copo e meio limão um pouco mais baixos, antes da troca de prop",
                termos=["clear drinking glass of warm water", "half a lemon with its cut side facing the lens"]),
    "T20": dict(titulo="receita 2, a máscara na tigelinha", obj="the bowl", cm=25, pct=25,
                prop=f"{TIGELA[0].upper()}{TIGELA[1:]}, held in her left hand at chest height; two fingers of her right hand touch the mixture.",
                pose="Brandon holds the bowl toward the lens and dips two fingers into the mixture",
                est="explaining, focused", lista="tigelinha com a mistura, mãos, avatar, mesa vazia",
                heroi="a tigelinha de vidro com a mistura cremosa amarelo-clara, dois dedos tocando a mistura",
                termos=["pale creamy yellow mixture of apple cider vinegar and coconut oil"]),
    "T21": dict(titulo="receita 2, benefício e virada", obj="the bowl", cm=25, pct=25,
                prop=f"{TIGELA[0].upper()}{TIGELA[1:]}, held in both hands at chest height.",
                pose="Brandon holds the bowl in both hands toward the lens",
                est="confident, a little conspiratorial at the end",
                lista="tigelinha com a mistura, avatar, mesa vazia",
                heroi="a tigelinha da máscara nas duas mãos",
                termos=["pale creamy yellow mixture of apple cider vinegar and coconut oil"]),
    "T22": dict(titulo="o álibi do estresse", obj="the bowl", cm=30, pct=22, extra=", a little tighter",
                prop=f"{TIGELA[0].upper()}{TIGELA[1:]}, held in both hands at chest height.",
                pose="Brandon holds the bowl in both hands, leaning slightly toward the lens",
                est="serious and reassuring", lista="tigelinha com a mistura, avatar, mesa vazia",
                heroi="a tigelinha nas duas mãos, ela inclinada para a lente",
                termos=["pale creamy yellow mixture of apple cider vinegar and coconut oil"]),
    "T23": dict(titulo="receita 3, o pote de sea moss", obj="the jar", cm=25, pct=35,
                prop=f"{POTE[0].upper()}{POTE[1:]}, held in both hands at chest height.",
                pose="Brandon holds the jar of dried sea moss in both hands, pushed toward the lens",
                est="emphatic, this is the important one",
                lista="pote de sea moss seco, avatar, mesa vazia",
                heroi="o pote de vidro largo cheio de sea moss seco, fios dourados e bege embaraçados",
                termos=["dried raw Irish sea moss", "tangled pale golden and beige seaweed strands"],
                desvio="pote de fibra em pó branca do modelo → pote de sea moss seco (troca obrigatória do nº 3)"),
    "T24": dict(titulo="receita 3, autoridade de coach", obj="the jar", cm=25, pct=35,
                prop=f"{POTE[0].upper()}{POTE[1:]}, held in both hands at chest height.",
                pose="Brandon holds the jar of dried sea moss in both hands at chest height",
                est="warm and proud", lista="pote de sea moss seco, avatar, mesa vazia",
                heroi="o pote de sea moss seco nas duas mãos",
                termos=["dried raw Irish sea moss"]),
    "T25": dict(titulo="mecanismo, o estresse queima os minerais", obj="the jar", cm=30, pct=30, extra=" from slightly above",
                prop=f"{POTE[0].upper()}{POTE[1:]}, held in her left hand at chest height; her right hand open beside it.",
                pose="Brandon holds the jar in her left hand and explains with her right hand open",
                est="serious, explaining", lista="pote de sea moss seco, avatar, mesa vazia",
                heroi="o pote de sea moss seco numa mão, a outra explicando",
                termos=["dried raw Irish sea moss"]),
    "T26": dict(titulo="mecanismo, o gel devolve os minerais", obj="the bowl", cm=25, pct=25,
                prop=f"{GEL[0].upper()}{GEL[1:]}, held in her left hand at chest height; her right index finger points at the gel.",
                pose="Brandon holds the small bowl toward the lens and points at the gel with her right index finger",
                est="calm and reassuring", lista="tigelinha com gel de sea moss, avatar, mesa vazia",
                heroi="a tigelinha com a colherada de gel de sea moss bege-claro, o indicador apontando",
                termos=["smooth pale beige sea moss gel, glossy and jelly-like"],
                desvio="tigelinha de fibra do modelo → gel de sea moss"),
    "T27": dict(titulo="prova social das clientes", obj="the bowl", cm=25, pct=25,
                prop=f"{GEL[0].upper()}{GEL[1:]}, held in both hands at chest height.",
                pose="Brandon holds the small bowl of gel in both hands",
                est="warm, telling a story", lista="tigelinha com gel de sea moss, avatar, mesa vazia",
                heroi="a tigelinha com o gel nas duas mãos",
                termos=["smooth pale beige sea moss gel, glossy and jelly-like"]),
    "T28": dict(titulo="a conspiração da prateleira", prop="Nothing in her hands; the black table is empty.", f6="the black table is empty",
                pose="Brandon leans on the black table with both hands, closer to the lens",
                comp=("Straight-on close medium shot: the phone lens is about 45 centimeters from her face, her head and "
                      "shoulders fill the upper 60 percent of the frame, her hands on the black table edge at the "
                      "bottom. The background is reduced by framing, never by blur."),
                obj="her face", cm=45, pct=60, est="indignant, lowering her voice",
                lista="avatar, mesa vazia, neon, quadro branco, bandeira",
                heroi="a Brandon mais perto, apoiada na mesa, sem prop",
                termos=["leans on the black table with both hands"]),
    "T29": dict(titulo="ninguém vai fazer por você", prop="Nothing in her hands; the black table is empty.", f6="the black table is empty",
                pose="Brandon leans on the black table with both hands, closer to the lens, one hand lifting slightly",
                comp=("Straight-on close medium shot: the phone lens is about 45 centimeters from her face, her head and "
                      "shoulders fill the upper 60 percent of the frame, her hands on the black table edge at the "
                      "bottom. The background is reduced by framing, never by blur."),
                obj="her face", cm=45, pct=60, est="firm", lista="avatar, mesa vazia, neon, quadro branco, bandeira",
                heroi="a Brandon apoiada na mesa, firme",
                termos=["leans on the black table with both hands"]),
    "T30": dict(titulo="o obstáculo, açúcar e enchimento", obj="the two bowls", cm=25, pct=35,
                prop=f"{ACUCAR[0].upper()}{ACUCAR[1:]} in her left hand and {PO} in her right hand, both held out at chest height.",
                pose="Brandon holds one small bowl in each hand, out toward the lens",
                est="warning, a little disgusted", lista="tigelinha de açúcar, tigelinha de pó branco, avatar, mesa vazia",
                heroi="uma tigelinha em cada mão: açúcar cristal e pó branco de enchimento",
                termos=["heaped with white granulated sugar", "heaped with a fine white powder"]),
    "T31": dict(titulo="o produto, o frasco sobe no nome", obj="the jar", cm=35, pct=20,
                comp=("Straight-on medium shot: the phone lens is about 35 centimeters from the jar, which she holds low "
                      "in her right hand just above the black table and fills the lower right 20 percent of the frame, "
                      "closer to the camera than her face; her face and shoulders fill the upper half of the frame. "
                      "The background is reduced by framing, never by blur."),
                prop=f"In her right hand, held low just above the black table, {FRASCO}. Nothing else on the table.",
                pose="Brandon holds the jar low in her right hand, about to raise it beside her face",
                est="proud, about to show it", lista="frasco Natural Rems Sea Moss, avatar, mesa vazia",
                heroi="o frasco Natural Rems Sea Moss baixo na mão direita, rótulo de frente",
                termos=["short wide jar of dark amber plastic with a black screw cap", "Sea Moss Gummies"],
                f6="Nothing else on the table",
                desvio="o produto do modelo (pote de fibra) → frasco Natural Rems Sea Moss, já na mão para nascer da foto real"),
}
FRASCO_ALTO = dict(
    obj="the jar", cm=30, pct=20,
    comp=("Straight-on medium shot: the jar is held up beside her right cheek and pushed slightly toward the camera, "
          "the phone lens is about 30 centimeters from the jar, which fills 20 percent of the frame at the right of "
          "her face, closer to the camera than her face, label facing the camera and fully readable. The background "
          "is reduced by framing, never by blur."),
    prop=f"In her right hand, held still beside her right cheek, {FRASCO}. Her left hand rests on the black table.",
    pose="Brandon holds the jar still beside her right cheek, label toward the lens",
    lista="frasco Natural Rems Sea Moss, avatar, mesa vazia",
    heroi="o frasco Natural Rems Sea Moss parado ao lado do rosto, rótulo de frente e legível",
    termos=["short wide jar of dark amber plastic with a black screw cap", "Sea Moss Gummies"],
    f6="Her left hand rests on the black table",
    desvio="frasco do modelo ao lado do ombro → Natural Rems um pouco mais perto da lente, rótulo legível (passo 1 da marca)")
for t, (tit, est) in {"T32": ("diferencial 16 em 1", "lively, listing"),
                      "T33": ("prova social da coach", "warm and certain"),
                      "T34": ("comment yes + follow", "inviting, smiling on yes"),
                      "T35": ("CTA da marca, Amazon e legenda", "clear and slow on the brand name")}.items():
    BR[t] = dict(FRASCO_ALTO, titulo=tit, est=est)

EMOCAO = {
    "T16": "entonação calma e segura de quem tem autoridade",
    "T17": "entonação animada e didática",
    "T18": "entonação animada e convicta",
    "T19": "entonação intrigante, virando o assunto",
    "T20": "entonação didática e prática",
    "T21": "entonação confiante, baixando a voz no fim como quem conta um segredo",
    "T22": "entonação séria e acolhedora",
    "T23": "entonação enfática, como quem chega na parte mais importante",
    "T24": "entonação calorosa e orgulhosa",
    "T25": "entonação séria e explicativa",
    "T26": "entonação calma e tranquilizadora",
    "T27": "entonação calorosa, contando uma história",
    "T28": "entonação indignada, baixando a voz",
    "T29": "entonação firme e direta",
    "T30": "entonação de alerta, com um leve desgosto",
    "T31": "entonação orgulhosa, dizendo Natural Rems Sea Moss devagar e por inteiro",
    "T32": "entonação animada, listando",
    "T33": "entonação calorosa e segura",
    "T34": "entonação convidativa, sorrindo no yes",
    "T35": "entonação clara, dizendo Natural Rems Sea Moss devagar e por inteiro",
}
ACOES_B = {
    "T16": "{n} fala para a câmera com as duas mãos apoiadas na mesa preta.",
    "T17": "{n} ergue o copo e o meio limão e, no squeeze, espreme o limão dentro do copo.",
    "T18": "{n} fala para a câmera segurando o copo e o meio limão.",
    "T19": "{n} fala para a câmera e baixa um pouco o copo e o limão.",
    "T20": "{n} mexe a mistura com dois dedos e, no face, toca a bochecha com os dedos.",
    "T21": "{n} fala para a câmera segurando a tigelinha com as duas mãos.",
    "T22": "{n} se inclina um pouco para a câmera segurando a tigelinha.",
    "T23": "{n} empurra o pote de sea moss seco na direção da câmera e fala.",
    "T24": "{n} fala para a câmera segurando o pote com as duas mãos.",
    "T25": "{n} fala segurando o pote numa mão e explicando com a outra mão aberta.",
    "T26": "{n} aponta o gel com o indicador e fala para a câmera.",
    "T27": "{n} fala para a câmera segurando a tigelinha com as duas mãos.",
    "T28": "{n} se apoia na mesa e fala para a câmera, mais perto.",
    "T29": "{n} fala para a câmera apoiada na mesa, levantando um pouco uma das mãos.",
    "T30": "{n} mostra uma tigelinha em cada mão e fala para a câmera.",
    "T31": "{n} ergue o frasco devagar da altura da cintura até o lado do rosto no nome do produto e o deixa parado, rótulo de frente.",
    "T32": "{n} fala para a câmera com o frasco parado ao lado do rosto, rótulo de frente.",
    "T33": "{n} fala para a câmera com o frasco parado ao lado do rosto, rótulo de frente.",
    "T34": "{n} fala para a câmera com o frasco parado ao lado do rosto, sorrindo no yes.",
    "T35": "{n} fala para a câmera com o frasco parado ao lado do rosto, rótulo de frente, do começo ao fim, sem baixar o frasco.",
}

# Falas da esquete: quem fala, voz, emocao e quem cala.
DIALOGO = {
    "T3": ("P2", "fala animado, alto, chegando", ["P1", "P3"]),
    "T4": ("P1", "fala educada e seca", ["P2"]),
    "T5": ("P2", "fala galanteador e simpático", ["P1", "P3"]),
    "T6": ("P2", "fala galanteador, voz baixa", []),
    "T7": ("P1", "fala irônica, sobrancelha erguida", ["P2", "P3"]),
    "T8": ("P2", "fala galanteador, sem vergonha nenhuma", ["P1", "P3"]),
    "T9": ("P1", "fala seca e cortante", ["P2"]),
    "T10": ("P2", "fala curioso, ainda flertando", []),
    "T11": ("P1", "fala tranquila e direta, sem parar de podar", ["P2"]),
    "T12": ("P2", "fala em choque, alto", []),
    "T13": ("P2", "fala incrédulo e espantado", ["P1"]),
    "T14": ("P1", "fala casual e confiante, como quem conta um segredo simples", ["P2"]),
}
ACOES_E = {
    "T1": "A vizinha poda a cerca viva no primeiro plano; o marido e a esposa vêm correndo pela calçada molhada na direção da câmera.",
    "T2": "A esposa fica paralisada de choque, com as mãos coladas na cabeça e a boca escancarada, olhando para frente.",
    "T3": "O marido chega trotando até a vizinha, sorrindo, com a mão erguida num aceno.",
    "T4": "A vizinha se vira para o marido segurando a tesoura e responde.",
    "T5": "O marido aponta a casa ao lado com a mão aberta enquanto fala; ao fundo a esposa continua curvada, recuperando o fôlego.",
    "T6": "O marido sorri de canto e fala olhando a vizinha.",
    "T7": "A vizinha olha para a esposa que se afasta correndo e fala com o marido.",
    "T8": "O marido abre a mão na direção da vizinha enquanto fala; a esposa segue correndo ao longe.",
    "T9": "A vizinha olha para o marido e fala, sem sorrir.",
    "T10": "O marido inclina a cabeça e pergunta.",
    "T11": "A vizinha volta a podar e responde olhando por cima do ombro.",
    "T12": "O marido arregala os olhos e fala.",
    "T13": "O marido abre as mãos, incrédulo, e fala.",
    "T14": "A vizinha ergue os galhos podados e o saco de lixo e fala com naturalidade.",
    "T15": "O marido escuta em silêncio, pisca devagar e fica pensativo.",
}
SOM_E = {"T1": ", tesoura de poda cortando galhos e passos na calçada molhada",
         "T2": ", respiração ofegante de corrida",
         "T11": ", tesoura de poda cortando galhos",
         "T14": ", farfalhar do saco de lixo"}
MOMENTO = {"T1": "0,00 a 0,97 s", "T2": "0,97 a 2,97 s", "T3": "2,97 a 3,50 s", "T4": "3,50 a 4,50 s",
           "T5": "4,50 a 7,87 s", "T6": "7,87 a 9,47 s", "T7": "9,47 a 11,80 s", "T8": "11,80 a 16,83 s",
           "T9": "16,83 a 18,70 s", "T10": "18,70 a 21,07 s", "T11": "21,07 a 23,87 s", "T12": "23,87 a 24,57 s",
           "T13": "24,57 a 27,43 s", "T14": "27,43 a 29,80 s", "T15": "29,80 a 30,90 s"}


# ------------------------------------------------------------------ montagem dos K
def k_esquete(t):
    d = ESQ[t]
    ps = d["ps"]
    return dict(
        fiction_note=FICCAO,
        reference_use=ref_esquete(ps),
        identity_main=". ".join(P[p]["ident"] for p in ps) + ".",
        wardrobe="; ".join(P[p]["roupa"] for p in ps) + ".",
        scene=RUA,
        prop=d["prop"],
        posture=d["pose"][0].upper() + d["pose"][1:] + ".",
        composition=(d["quadro"][0].upper() + d["quadro"][1:] + ". Every face in sharp focus. The background is "
                     "reduced by framing, never by blur."),
        camera=d["cam"],
        lighting=LUZ_RUA,
        state=d["estado"],
        realism=REALISMO,
        aspect_ratio="9:16 vertical",
        negative=NEG_RUA,
    )


def k_brandon(t):
    d = BR[t]
    comp = d.get("comp") or comp_b(d["obj"], d["cm"], d["pct"], d.get("extra", ""))
    neg = NEG_BOX + (NEG_PRODUTO if t in PRODUTO_T else NEG_SEM_ROTULO)
    return dict(
        fiction_note=FICCAO_B,
        reference_use=REF_B_PROD if t in PRODUTO_T else REF_B,
        identity_main=B["identidade"],
        wardrobe=B["roupa"],
        scene=B["cena"],
        prop=d["prop"],
        posture=d["pose"] + ".",
        composition=comp,
        camera=d.get("cam", CAM_B),
        lighting=LUZ_BOX,
        state=f"Start frame: Brandon is {BOCA}, looking straight into the lens, {d['est']}.",
        realism=REALISMO,
        aspect_ratio="9:16 vertical",
        negative=neg,
    )


def keyframes():
    out = []
    for i, t in enumerate(TAKES, 1):
        cod = f"K{i:02d}"
        j = k_esquete(t) if t in ESQ else k_brandon(t)
        j = dict(shot_id=f"{cod}_{t.lower()}", **j)
        titulo = (ESQ.get(t) or BR[t])["titulo"]
        out.append(dict(codigo=cod, take=t, titulo=titulo, j=j))
    return out


def anexos(k):
    t = k["take"]
    if t in ESQ:
        return [f"REF-P{p[1]} ({P[p]['nome']})" for p in ESQ[t]["ps"]] + [f"FRAME DO MODELO `{frame_modelo(k['codigo'])}` (por último, só composição)"]
    lst = [f"ÂNCORA HOLISTIC BRANDON `{ANCORA}`", f"FRAME DO MODELO `{frame_modelo(k['codigo'])}` (só composição)"]
    if t in PRODUTO_T:
        lst.append(f"FOTO DO PRODUTO `{FOTO_PRODUTO}` (só o pote da frente)")
    return lst


# ------------------------------------------------------------------ REF-P (character sheets)
def refs_p():
    out = []
    for p, d in P.items():
        j = {
            "shot_id": f"REF-{p}_character_sheet_{d['nome'].lower()}",
            "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
            "sheet_layout": ("CHARACTER SHEET of ONE person on a plain light grey wall background: three full-body "
                             "views side by side (front, three-quarter and profile) in the lower two thirds, and a large "
                             "front close-up of the face across the top third. The same person, the same clothes and the "
                             "same hair in every view."),
            "identity_main": d["ident"] + ", " + d["roupa"].split(" wears ", 1)[1] + ".",
            "expression": "Neutral relaxed expression, mouth closed, looking straight ahead.",
            "lighting": ("Flat neutral daylight, soft and even on the face and body, no harsh shadows, no warm orange "
                         "cast and no yellow tint."),
            "realism": REALISMO + " No blur, no bokeh.",
            "aspect_ratio": "9:16 vertical",
            "negative": ("no captions, no subtitles, no words overlaid on the image, no plastic skin, no extra fingers, "
                         "no blur, no bokeh, no warm orange color cast, no yellow tint, no golden hour light, no AI "
                         "polish, no beauty smoothing, no cinematic lighting, no labels, no numbers, no arrows, no "
                         "second person"),
        }
        out.append(dict(codigo=f"REF-{p}", nome=d["nome"], j=j))
    return out


# ------------------------------------------------------------------ ficha do frame
def ficha(ks):
    L = ["# FICHA DO FRAME · brandon_seamoss_vizinha", "",
         "Regra e método: `GATE_VISUAL.md` Parte 6. Cada K sai daqui, nunca da memória. O frame do modelo manda no",
         "CONTEÚDO (forma, quadro, distância, câmera, pose, o que está em quadro); o gate manda no ACABAMENTO e impõe o",
         "piso de proximidade do herói. A evidência de cada OK é um trecho que existe literalmente no K",
         "(conferido por `gerar_pacote.py` com assert antes de gravar).", ""]
    for k in ks:
        t, cod, j = k["take"], k["codigo"], k["j"]
        texto = json.dumps(j, ensure_ascii=False)
        if t in ESQ:
            d = ESQ[t]
            quadro_txt = d["quadro"]
            m_pct = re.search(r"(?:fills?|filling)[^,;]*?\d+ percent of the frame(?: height)?", quadro_txt)
            m_cm = re.search(r"about [^,;]*? (?:meters?|centimeters) from the lens", quadro_txt)
            assert m_pct and m_cm, (cod, quadro_txt)
            ev = dict(F2=m_pct.group(0), F3=m_cm.group(0), F4=d["cam"].split(", ")[1] if "lens" in d["cam"] else d["cam"],
                      F5=d["pose"][:60].rsplit(" ", 1)[0], F6=d["prop"].rstrip("."))
            camera_pt = d["cam"]
            pose = d["pose"]
            dist = re.sub(r"^.*?(about [^,;]*? (?:meters?|centimeters) from the lens).*$", r"\1", quadro_txt)
            heroi, termos, lista = d["heroi"], d["termos"], d["lista"]
            quadro = f"no K: {m_pct.group(0)} (medido no frame do modelo, mesmo enquadramento)"
            f0 = d["estado"]
            desvio = ("rostos novos de elenco próprio (REF-P), nunca os do modelo; céu branco estourado → nublado com "
                      "textura (gate); bandeira na varanda (gate)")
            g2 = '"overcast pale grey with visible soft cloud texture"'
            g8 = None if t in MUDOS else '"caught mid-sentence, lips naturally parted"'
            if t == "T2":
                g8 = None
        else:
            d = BR[t]
            comp = j["composition"]
            m_pct = re.search(r"fills? (?:the (?:lower |upper )?(?:right )?)?\d+ percent of the frame", comp)
            m_cm = re.search(r"about \d+ centimeters from [a-z ]+?(?=[,.])", comp)
            assert m_pct and m_cm, (cod, comp)
            ev = dict(F2=m_pct.group(0), F3=m_cm.group(0), F4="standard 1x lens", F5=d["pose"][:55].rsplit(" ", 1)[0],
                      F6=d.get("f6") or d["prop"].split(";")[0].split(",")[0].rstrip("."))
            camera_pt = j["camera"]
            pose = d["pose"]
            dist = m_cm.group(0)
            heroi, termos, lista = d["heroi"], d["termos"], d["lista"]
            quadro = (f"no modelo o prop ocupa uns 12 a 15% do quadro, na altura do peito da apresentadora sentada; "
                      f"no K: {m_pct.group(0)} (piso de proximidade do gate)")
            f0 = j["state"]
            desvio = d.get("desvio", "apresentadora sentada num banco na rua → Brandon em pé atrás da mesa preta no box "
                                     "(avatar fixo da conta); prop mais perto da lente que no modelo (piso do gate)")
            g2 = None
            g8 = '"caught mid-sentence, lips naturally parted"'
        ev = dict(ev, G1='"Neutral overcast daylight"', G3='"everything in sharp focus"', G4='"Real skin with visible pores"',
                  G5='"no warm orange color cast"', G6='"no captions"', G7='"small American flag"')
        for it in ("F2", "F3", "F4", "F5", "F6"):
            ev[it] = f'"{ev[it]}"'
        ev["F1"] = " · ".join(f'"{x}"' for x in termos)
        if g2:
            ev["G2"] = g2
        if g8:
            ev["G8"] = g8
        for item, e in ev.items():
            for trecho in re.findall(r'"([^"]+)"', e):
                assert trecho.lower() in texto.lower(), (cod, item, trecho)
        L += [f"## {cod}", f"Frame: `{frame_modelo(cod)}`", f"Take: {t}", f"Herói: {heroi}",
              "Termos de forma: " + ev["F1"], f"Quadro: {quadro}", f"Distância da lente: {dist}",
              f"Câmera: {camera_pt}", f"Pose: {pose}", f"Lista fechada: {lista}", f"Frame 0: {f0}",
              f"Desvio (acabamento ou avatar fixo): {desvio}", "",
              "| Item | Status | Evidência (trecho literal do K) |", "|---|---|---|"]
        nomes = ["F1 forma do heroi", "F2 quanto do quadro", "F3 distancia da lente", "F4 camera",
                 "F5 pose do avatar", "F6 lista fechada", "G1 luz neutra", "G2 ceu ou janela", "G3 foco",
                 "G4 realismo", "G5 sem tom quente", "G6 sem texto", "G7 bandeira", "G8 boca no K de fala"]
        for nome in nomes:
            it = nome[:2]
            if it == "G2" and it not in ev:
                L.append(f"| {nome} | N/A | sem janela nem céu em quadro: a janela fica fora do quadro, só a luz entra |")
            elif it == "G8" and it not in ev:
                L.append(f"| {nome} | N/A | take sem fala (B-ROLL mudo ou reação de choque sem palavra) |")
            else:
                L.append(f"| {nome} | OK | {ev[it]} |")
        L.append("")
    return "\n".join(L)


# ------------------------------------------------------------------ videos
def videos():
    vs = []
    for i, t in enumerate(TAKES, 1):
        if t in ESQ:
            som = "rua de bairro residencial depois da chuva, pássaros ao longe" + SOM_E.get(t, "")
            cam = "leve handheld, como alguém na calçada filmando com o celular, sem trocar de plano"
            if t in MUDOS:
                abre = {"T1": "(sem fala no take: abertura muda, a primeira fala entra no V03)",
                        "T2": "(sem fala no take: reação muda da esposa, ninguém fala)",
                        "T15": ("(sem fala no take: o \"literally everything\" da vizinha no V14 entra como voz-over "
                                "na edição; o marido fica calado)")}[t]
                txt = (f"{abre}\n\no que acontece no vídeo: {ACOES_E[t]}\n\ncâmera: {cam}\n\n"
                       f"som ambiente: {som}, sem música")
            else:
                quem, emo, calados = DIALOGO[t]
                pq = P[quem]
                linha = (f"1. {'o' if quem == 'P2' else 'a'} {pq['nome']} ({pq['curto']}), {pq['voz']}, {emo}: "
                         f"\"{FALAS[t]}\"")
                cala = " e ".join(f"{'o' if c == 'P2' else 'a'} {P[c]['nome']}" for c in calados)
                cala = (cala[0].upper() + cala[1:] + (" não diz" if len(calados) == 1 else " não dizem") +
                        " nenhuma palavra.") if calados else "Ninguém mais fala."
                txt = ("falas no take, em inglês, na ordem:\n" + linha + "\n" + cala + "\n\n"
                       "cada personagem diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última "
                       "palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo, só na boca de "
                       "quem está falando.\n\n"
                       f"o que acontece no vídeo: {ACOES_E[t]}" +
                       ((" Ela" if quem != "P2" else " Ele") + " diz a frase em ritmo natural logo no começo e a ação "
                        "continua até o fim." if "CENA CURTA" in HEADS[t] else "") +
                       f"\n\ncâmera: {cam}\n\nsom ambiente: {som}, sem música")
        else:
            n = B["nome"]
            txt = (f"a avatar {n}, mulher, fala em inglês com sotaque americano {B['sotaque']}, {B['voz']}, "
                   f"{EMOCAO[t]}, voz autêntica, como se exigisse ser ouvida, a seguinte frase: \"{FALAS[t]}\"\n\n"
                   "a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por "
                   "inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.\n\n"
                   f"o que acontece no vídeo: {ACOES_B[t].format(n=n)}\n\n"
                   f"câmera: {'fixa' if t in PRODUTO_T else 'fixa, leve handheld natural'}\n\n"
                   f"som ambiente: {B['som']}, sem música")
        vs.append((f"V{i:02d}", t, f"K{i:02d}", txt))
    return vs


ORDEM_K = ["fiction_note", "reference_use", "identity_main", "wardrobe", "scene", "prop", "posture",
           "composition", "camera", "lighting", "state", "realism", "aspect_ratio", "negative"]


def texto_flow(j):
    """Prompt de imagem de EXECUCAO, em JSON (contrato do Flow v17): sem shot_id, com o formato na frente."""
    assert set(ORDEM_K) == set(j) - {"shot_id"}, set(j) ^ set(ORDEM_K)
    d = {"format": "IMPORTANT: THIS IS IPHONE FOOTAGE. Vertical 9:16."}
    d.update({k: j[k] for k in ORDEM_K})
    return json.dumps(d, ensure_ascii=False, indent=2)


def texto_flow_ref(j):
    d = {k: v for k, v in j.items() if k != "shot_id"}
    return json.dumps(d, ensure_ascii=False, indent=2)


def bloco_anexo(k):
    lst = anexos(k)
    nums = ["1️⃣", "2️⃣", "3️⃣", "4️⃣"]
    L = [f"> ### 📎 ANEXAR: **{len(lst)} IMAGENS**"]
    L += [f"> **{nums[i]} {a}**" for i, a in enumerate(lst)]
    L += [">", "> ### 🆕 GERAR DO ZERO"]
    return "\n".join(L)


def capcut():
    return [
        "1. Clipes numerados na ordem: V01 a V35.",
        "2. Esquete no tempo exato do modelo: " + "; ".join(f"V{t[1:].zfill(2)} {MOMENTO[t]}" for t in ESQUETE) + ".",
        "3. **V14 → V15:** cortar para o V15 em \"She taught me\" e deixar o áudio do V14 continuar por baixo com "
        "\"literally everything\" sobre o close do marido calado.",
        "4. Corte seco do V15 para o V16 (a Brandon entra já falando). Do V16 ao V35, cortar logo depois da última palavra de cada clipe.",
        "5. Zero tempo morto: todo clipe falado começa já falando. Isolate Voice / Keep Vocal no áudio.",
        "6. Legenda de tela branca sem serifa, duas a três palavras por vez, no meio do quadro, igual ao modelo. "
        "No V34, `yes` grande e isolado na tela. No V35, duas setas vermelhas apontando para baixo (para a legenda do post), como no modelo.",
        "7. Sem Voice Changer: a voz de cada personagem e da Brandon vem do prompt de cada V.",
        "8. Música opcional só a partir do V16, nunca na esquete, entre -19 e -20 dB, fora da biblioteca do TikTok.",
        "9. Rótulo pequeno `AI-generated` num canto do vídeo.",
        "10. No V31 a V35 o frasco não pode ser cortado nem coberto: nenhum B-roll por cima (regra da marca).",
    ]


LEGENDA = [
    "Primeira linha, sempre: `#ad #syntheticperformer #naturalrems`",
    "Logo abaixo: o link da Amazon do Natural Rems Sea Moss (o V35 manda tocar no link da legenda).",
    "Chave de conteúdo de IA da plataforma LIGADA.",
]


def transcricao():
    L = ["| Take | English | Português |", "|---|---|---|"]
    for t in TAKES:
        en = FALAS.get(t, "(sem fala)" if t != "T15" else "(voz-over do T14: literally everything)")
        L.append(f"| {t} | {en} | {TRANSCRICAO_PT[t]} |")
    return L


def pacote():
    ks, vs, rs = keyframes(), videos(), refs_p()
    L = ["# holistic.brandon | Natural Rems Sea Moss Venda, a vizinha de 57 | Pacote de Prompts", "",
         "Vídeo modelo: `input/reference_video.mp4` (160,2 s, avatar IA, movie style família B)", "",
         f"Âncora: `{ANCORA}` (T16 a T35) · Foto do produto: `{FOTO_PRODUTO}` (T31 a T35)", "",
         "Funil: VENDA. Esquete com elenco próprio (REF-P1 a REF-P3) → indicação → a Brandon ensina três receitas → "
         "Natural Rems Sea Moss com comment `yes` + follow, busca na Amazon e link na legenda. Rodada de validação, "
         "gancho fiel ao modelo. Perfil CLÁSSICO.", "",
         "## Índice de geração", "",
         "| Take | Keyframe | Anexar | Ação |", "|---|---|---|---|"]
    for r in rs:
        L.append(f"| (elenco) | {r['codigo']} | nenhuma | GERAR DO ZERO, aprovar antes de qualquer K |")
    for k in ks:
        L.append(f"| {k['take']} | {k['codigo']} | " + " + ".join(a.split(" `")[0] for a in anexos(k)) + " | GERAR DO ZERO |")
    L += ["", "Todo K é GERAR DO ZERO: o bloco do Flow é autossuficiente e cada K descreve o cenário inteiro, "
          "então não existe `EDITAR do K__` aqui. O frame do modelo de cada K entra só como composição.", "",
          "## Fichas do elenco e de voz", "",
          "| Código | Personagem | Aparência | Voz |", "|---|---|---|---|"]
    for p, d in P.items():
        L.append(f"| REF-{p} | {d['nome']} | {d['ident']} | {d['voz'] or 'não fala'} |")
    L.append(f"| âncora | BRANDON | holistic.brandon (âncora) | {B['voz']}, sotaque americano {B['sotaque']} |")
    L += ["", "## Trava de identidade e continuidade", "",
          f"- Brandon, identidade: {B['identidade']}",
          f"- Brandon, roupa (fixa da conta): {B['roupa']}",
          f"- Brandon, cenário-base (fixo da conta): {B['cena']}",
          f"- Luz do box: {LUZ_BOX}",
          f"- Esquete, cenário: {RUA}",
          f"- Luz da rua: {LUZ_RUA}",
          "- Cada personagem da esquete tem o mesmo rosto, cabelo e roupa do REF-P dele em todos os K; nenhum rosto parecido com o do vídeo modelo.",
          "- Voz: o mesmo timbre de cada personagem em todos os V em que ele fala (a emoção muda por fala, o timbre não).", "",
          "## Trava do prop herói", "",
          f"- Receita 1: {COPO}; {LIMAO}.",
          f"- Receita 2: {TIGELA}.",
          f"- Receita 3: {POTE}; depois {GEL}.",
          f"- Obstáculo: {ACUCAR}; {PO}.",
          f"- Produto: {FRASCO}. Só o pote da frente da foto oficial; sem a faixa MADE IN USA, sem o segundo pote, sem gomas soltas.",
          "- Nenhum outro prop com texto ou marca.", "",
          "## Trava da 2ª pessoa (REF-A)", "",
          "- Não há REF-A: a esquete usa os character sheets REF-P1 (vizinha), REF-P2 (marido) e REF-P3 (esposa), "
          "gerados e aprovados antes de qualquer K. A Brandon nunca divide quadro com eles.", "",
          "# Prompts de imagem", ""]
    for r in rs:
        L += [f"## {r['codigo']} · {r['nome']} · CHARACTER SHEET · GERAR DO ZERO", "",
              "> ### 📎 ANEXAR: **NENHUMA IMAGEM**", ">", "> ### 🆕 GERAR DO ZERO, aprovar antes de qualquer K", "",
              "```json", json.dumps(r["j"], ensure_ascii=False, indent=2), "```", ""]
    for k in ks:
        refs = " + ".join(a.split(" `")[0].split(" (")[0] for a in anexos(k))
        L += [f"## {k['codigo']} · {k['take']} · GERAR DO ZERO · {refs.upper()}", "",
              bloco_anexo(k), "", f"Cena: {k['titulo']}.", "", "```json",
              json.dumps(k["j"], ensure_ascii=False, indent=2), "```", ""]
    L += ["## Bloco global de vídeo", "", "```text",
          f"a avatar {B['nome']}, mulher, fala em inglês com sotaque americano {B['sotaque']}, {B['voz']}, "
          "[emoção da fala], voz autêntica, como se exigisse ser ouvida, a seguinte frase: \"[FALA EXATA DO ROTEIRO]\"", "",
          "a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.", "",
          "o que acontece no vídeo: [ação enxuta]", "", "câmera: [fixa]", "", f"som ambiente: {B['som']}, sem música",
          "```", "", "Na esquete, a abertura vira o bloco `falas no take, em inglês, na ordem:` com quem fala, a voz "
          "e a emoção, e quem fica calado escrito (Flow v13).", "", "# Prompts de vídeo", ""]
    for cod, take, kcod, txt in vs:
        L += [f"### {cod} · {take} · usa {kcod}", "", "```text", txt, "```", ""]
    L += ["## Mapa de âncoras", "", "| Código | Anexar, nesta ordem | Modelo |", "|---|---|---|"]
    for r in rs:
        L.append(f"| {r['codigo']} | nenhuma | Nano Banana 2, 9:16, aprovar antes dos K |")
    for k in ks:
        L.append(f"| {k['codigo']} | " + " + ".join(anexos(k)) + " | Nano Banana 2, 9:16 |")
    L += ["", "Vídeo: Omni Flash, 8 segundos, um resultado por V, a imagem escolhida do K de mesmo número como INITIAL FRAME.",
          "", "## Montagem no CapCut", ""] + capcut() + ["", "Legenda do post:", ""] + [f"- {x}" for x in LEGENDA] + [
          "", "## Gates de qualidade", "",
          "1. Os três REF-P aprovados antes do primeiro K; o mesmo rosto, cabelo e roupa de cada personagem em todos os K.",
          "2. Fala de cada V igual ao ROTEIRO, palavra por palavra; em cada V de diálogo a fala sai na boca certa.",
          "3. Um take por cena do modelo na esquete; cenas curtas marcadas; nenhum take acima de 29 palavras.",
          "4. Bandeira dos EUA no campo scene de todo K (varanda na rua, quadro branco no box).",
          "5. Zero travessão.",
          "6. Natural Rems: frasco parado e legível do V31 ao V35; \"Search Natural Rems Sea Moss on Amazon\" antes do link; nada depois do link; comment `yes` + follow no V34, antes da Amazon.",
          "7. Compliance da marca: nada médico em fala ou quadro, sem antes/depois, sem cura ou resultado garantido, sem concorrente; legenda com `#ad #syntheticperformer #naturalrems` no topo.",
          "8. GATE_VISUAL Partes 1 a 3 em todo K: herói colado na lente, luz neutra, céu com textura na rua, sem tom quente, sem blur, trecho de realismo.",
          "9. Gancho fiel no conteúdo: plano aberto mudo da vizinha podando com o casal correndo, e o close de choque da esposa.",
          "10. Um K = um V; a Brandon nunca aparece na esquete e ninguém da esquete aparece no box.",
          "11. `python3 checar_entrega.py producao/brandon_seamoss_vizinha` sem FALHA.", ""]
    flow = ["# Blocos limpos para o Google Flow | holistic.brandon", "", "Fonte interna: `PROMPTS_BRANDON.md`", "",
            "## BLOCO DE IMAGEM", "", "```text"]
    for r in rs:
        flow += [r["codigo"], texto_flow_ref(r["j"]), ""]
    for k in ks:
        flow += [k["codigo"], texto_flow(k["j"]), ""]
    flow += ["```", "", "## BLOCO DE VÍDEO", "", "```text"]
    for cod, _, _, txt in vs:
        flow += [cod, txt, ""]
    flow += ["```", "", "## Tabela de leitura humana", "", "| Código | Take | Anexar |", "|---|---|---|"]
    for k in ks:
        flow.append(f"| {k['codigo']} / V{k['codigo'][1:]} | {k['take']}, {k['titulo']} | " + " + ".join(anexos(k)) + " |")
    flow += ["", "## Transcrição final por take", ""] + transcricao()
    return "\n".join(L) + "\n", "\n".join(flow) + "\n", ficha(ks) + "\n"


def main():
    p, f, fi = pacote()
    (AQUI / "FICHA_FRAMES.md").write_text(fi, encoding="utf-8")
    (AQUI / "PROMPTS_BRANDON.md").write_text(p, encoding="utf-8")
    (AQUI / "FLOW_BRANDON.md").write_text(f, encoding="utf-8")
    (AQUI / "PROMPTS_PRODUCAO.md").write_text(p, encoding="utf-8")
    print("ok: ficha + pacote; %d REF-P, %d K, %d V" % (len(refs_p()), len(keyframes()), len(videos())))


if __name__ == "__main__":
    main()
