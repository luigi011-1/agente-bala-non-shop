"""Gera o pacote da producao fitywell_brownie_feijao (FityWell, VENDA, holistic.brandon).

Fonte unica da fala: ROTEIRO.md aprovado em 2026-09-30 (lido do disco, nunca redigitado).
Identidade, roupa e cenario: ficha de 2026-09-29 em avatares-fichas, conferida contra a ancora anexada
(identica byte a byte a producao/_ancoras/holistic_brandon_ancora.jpg).

K em JSON tambem no bloco do Flow (format na frente, sem shot_id). Perfil CLASSICO: cada V usa o maior
K menor ou igual ao seu numero (V10 -> K09; V11 a V16 -> K11, a mesma selfie).

Saidas: PROMPTS_HOLISTIC_BRANDON.md e PROMPTS_PRODUCAO.md (fonte interna com JSON), FLOW_HOLISTIC_BRANDON.md
(blocos limpos) e FICHA_FRAMES.md (ficha medida no frame do modelo + placar com evidencia literal do K).
"""
import json
import re
from pathlib import Path

AQUI = Path(__file__).resolve().parent
ROTEIRO = (AQUI / "ROTEIRO.md").read_text(encoding="utf-8")

TAKES, FALAS, MUDOS = [], {}, set()
for m in re.finditer(r"^### (T\d+) · (.*)$", ROTEIRO, re.M):
    t = m.group(1)
    TAKES.append(t)
    fim = ROTEIRO.find("\n### ", m.end())
    corpo = ROTEIRO[m.end(): fim if fim > 0 else len(ROTEIRO)]
    f = re.search(r'^> "(.+?)"\s*$', corpo, re.M)
    if f:
        FALAS[t] = f.group(1)
    else:
        MUDOS.add(t)
assert len(TAKES) == 16 and MUDOS == {"T3", "T4", "T5", "T7", "T8"}, (TAKES, MUDOS)
VOZ_OVER = {"T2", "T6"}
SELFIE = {"T11", "T12", "T13", "T14", "T15", "T16"}

FORMATO = "IMPORTANT: THIS IS IPHONE FOOTAGE. Vertical 9:16."
FICCAO = "This is a fictional AI-generated character, no real person is depicted."
NOME = "Brandon"
ANCORA = "producao/_ancoras/holistic_brandon_ancora.jpg"
ARQ = "HOLISTIC_BRANDON"

IDENTIDADE = ("The exact fictional AI character Brandon, explicitly female: Black mixed-race American woman around "
              "thirty, athletic build, light brown skin with light freckles across her nose and cheeks, brown eyes, "
              "cornrow braids that turn into long loose braids down to her waist with wooden and gold beads at the "
              "tips, small stud earrings, a floral blackwork tattoo sleeve on her right arm, a fine tattoo on the "
              "inside of her left arm and a fine floral tattoo on her chest below the left collarbone.")
ROUPA = ("White ribbed tank top, loose black lightweight training shorts, and a thin gold chain with a small gold "
         "cross pendant.")
CENA = ("Her own garage training box, the same room as the reference image, unchanged: white-painted concrete "
        "block walls under a dark wood slat ceiling, a red neon sign on the left wall, a small American flag high on "
        "the wall at the right, and a metal-and-wood shelf with glass jars of seeds at the far right. A black table "
        "stands in front of her.")
LUZ = ("Neutral overcast daylight coming in from a wide open garage door out of frame, soft even light on the face "
       "with no harsh shadows, the red neon adding only a faint glow on the wall behind her.")
REALISMO = ("Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural "
            "clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday "
            "reality, background fully in focus, everything in sharp focus, no blur, no bokeh, no AI polish, "
            "no beauty smoothing, no warm orange color cast, no yellow tint, no golden glow, no golden hour light, "
            "no sunset, no captions, no subtitles, no words overlaid on the image.")
NEG = ("no captions, no subtitles, no words overlaid on the image, no printed labels or lettering on any container "
       "or package, no studio, no plastic-looking human skin, no extra fingers, no supernatural lighting, no blur, "
       "no bokeh, no artificial lighting, no warm orange color cast, no yellow tint, no golden glow, no golden hour "
       "light, no sunset, no de-aging, no beauty smoothing, no HDR, no cinematic lighting, no second person in frame")
NEG_PHONE = ", no visible phone"
REF = f"Use the attached image only for {NOME}'s exact identity, wardrobe and own setting. Do not copy its pose or framing."
BOCA = "caught mid-sentence, lips naturally parted, animated expression"
CAM_PEITO = "phone camera on a small tripod at chest height, 26 mm wide lens, straight on, slight downward angle toward the table, fixed"
MAOS = "only her hands and the white ribbed tank top of her torso behind them are in frame, her face above the top edge of the frame"

# Cada K: prop, posture, composition, camera, state, negative extra, e a ficha medida no frame do modelo.
KS = [
    dict(codigo="K01", take="T1", titulo="gancho, a tigela de feijão preto perto da lente com o amassador", anexos=2,
         reference_use=REF + " Use the second attached image only as a composition reference for the glass bowl of black beans held close to the lens at the lower center, the masher raised over it and the person centered behind it; do not copy its man, his chef jacket, glasses, kitchen or colors.",
         prop="Brandon holds a round clear glass mixing bowl full of cooked black beans with her left hand, pushed toward the lens, and her right hand raises a stainless steel potato masher with a flat perforated plate just above the beans, about to press down. On the black table in front of her lie only a wooden spoon and a wire whisk.",
         posture="Brandon is standing behind her black table, leaning slightly toward the camera, the left hand under the bowl, the right hand gripping the masher.",
         composition="The glass bowl of black beans fills about 25 percent of the frame at the lower center, held about 35 centimeters from the lens, large in frame and closer to the camera than her face; the masher rises beside it. From the chest up, her head and upper chest clear and centered in the upper half of the frame, her face about 70 centimeters from the lens. Nothing else competes with the bowl of black beans. The background is reduced by framing, never by blur.",
         camera=CAM_PEITO,
         state=f"Start frame: the masher is just above the whole shiny black beans, not a single bean mashed yet. Brandon looks into the lens, {BOCA}.",
         neg=NEG_PHONE + ", no mashed beans yet, no chef jacket",
         ficha=dict(heroi="tigela de vidro redonda cheia de feijão preto cozido, segurada na altura do peito e empurrada para a lente, com o amassador de inox de placa furada erguido logo acima.",
                    termos=["round clear glass mixing bowl", "cooked black beans", "stainless steel potato masher"],
                    quadro="a tigela ocupa ~25% do quadro no centro-baixo (de ~48% a ~75% da altura), o amassador sobe pela esquerda.",
                    dist="no modelo a tigela está a ~45 cm; no K, 35 cm (mais perto, piso do gate).",
                    cam="celular fixo na altura do peito, lente 1x (~26 mm), frontal, leve inclinação para baixo.",
                    pose="pessoa centrada atrás da bancada, mão esquerda por baixo da tigela, mão direita com o amassador.",
                    lista="pessoa, tigela de feijão, amassador; na bancada só colher de pau e batedor. Nada mais.",
                    frame0="amassador logo acima do feijão inteiro, boca aberta no começo da frase.",
                    desvio="Brandon, regata e box da âncora no lugar do chef de dólmã na cozinha de mármore (avatar fixo); luz neutra do gate.",
                    ev=dict(F1="round clear glass mixing bowl full of cooked black beans", F2="fills about 25 percent of the frame at the lower center",
                            F3="held about 35 centimeters from the lens", F4="at chest height, 26 mm wide lens, straight on",
                            F5="the left hand under the bowl, the right hand gripping the masher", F6="On the black table in front of her lie only a wooden spoon and a wire whisk."),
                    g8=True)),
    dict(codigo="K02", take="T2", titulo="close da tigela, dois ovos entrando no feijão (voz fora de quadro)", anexos=1,
         reference_use=REF,
         prop="A round clear glass mixing bowl of roughly mashed black beans stands on the black table in the lower foreground. Her right hand tips a small clear glass cup, and two whole raw eggs with bright orange yolks slide out of it into the beans. Beside the bowl on the black table stand three small clear glass bowls: one of cocoa powder, one of golden raw honey and one of ground cinnamon. Nothing else is on the table.",
         posture=f"Close shot: {MAOS}; only the tip of her chin shows at the very top edge.",
         composition="The bowl of black beans fills the bottom 40 percent of the frame, about 40 centimeters from the lens, very close to the lens and large in frame, the eggs sliding in at its center; the three small bowls sit beside it. No face in frame. The background is reduced by framing, never by blur.",
         camera="phone camera on a small tripod at chest height, tilted down about 30 degrees toward the table, 26 mm wide lens, fixed",
         state="Start frame: the first egg yolk is just touching the black beans, the second still sliding out of the cup.",
         neg=NEG_PHONE + ", no face in frame, no cracked eggshell pieces in the bowl",
         ficha=dict(heroi="tigela de vidro com feijão preto amassado na bancada; a mão vira um potinho de vidro e dois ovos crus inteiros, gema laranja, escorregam para dentro.",
                    termos=["round clear glass mixing bowl", "two whole raw eggs", "three small clear glass bowls"],
                    quadro="a tigela ocupa o terço de baixo (~40%), os potinhos de cacau, mel e canela ao lado; do torso só a dólmã e a ponta do queixo no topo.",
                    dist="no modelo ~45 cm; no K, 40 cm.",
                    cam="celular na altura do peito inclinado ~30° para a bancada, lente 1x (~26 mm), fixo.",
                    pose="só mão e torso: mão direita virando o potinho sobre a tigela; rosto fora de quadro, só o queixo.",
                    lista="tigela, potinho com ovos, três potinhos (cacau, mel, canela); nada mais na bancada.",
                    frame0="a primeira gema tocando o feijão, a segunda ainda escorrendo.",
                    desvio="mesa preta e regata branca da âncora no lugar do mármore e da dólmã; luz neutra.",
                    ev=dict(F1="two whole raw eggs with bright orange yolks slide out of it into the beans", F2="The bowl of black beans fills the bottom 40 percent of the frame",
                            F3="about 40 centimeters from the lens", F4="at chest height, tilted down about 30 degrees toward the table, 26 mm wide lens",
                            F5="only the tip of her chin shows at the very top edge", F6="Nothing else is on the table."),
                    g8=False)),
    dict(codigo="K03", take="T3", titulo="close, colher de cacau em pó sobre a tigela", anexos=1,
         reference_use=REF,
         prop="Inside a round clear glass mixing bowl on the black table: roughly mashed black beans with two raw egg yolks on top. Her right hand holds a metal spoon heaped with dark cocoa powder right above the yolks, and her left hand holds a small clear glass bowl of cocoa powder just behind it. Nothing else is in frame.",
         posture=f"Close shot: {MAOS}.",
         composition="The bowl fills the bottom 60 percent of the frame, about 30 centimeters from the lens, very close to the lens and large in frame, the heaped spoon of cocoa at the center. No face in frame. The background is reduced by framing, never by blur.",
         camera="phone camera held above the table at chest height, looking down at about 45 degrees into the bowl, 26 mm wide lens, fixed",
         state="Start frame: the spoon is full and level, the first grains of cocoa starting to fall onto the yolks.",
         neg=NEG_PHONE + ", no face in frame",
         ficha=dict(heroi="colher de metal cheia de cacau em pó escuro sobre a tigela de feijão com duas gemas; a outra mão segura o potinho de cacau.",
                    termos=["metal spoon heaped with dark cocoa powder", "two raw egg yolks"],
                    quadro="a tigela ocupa ~60% de baixo, a colher no centro; torso branco ao fundo sem rosto.",
                    dist="no modelo ~30 cm; no K, 30 cm.",
                    cam="celular acima da bancada na altura do peito, ~45° para dentro da tigela, lente 1x (~26 mm).",
                    pose="só as duas mãos: direita com a colher, esquerda com o potinho.",
                    lista="tigela, colher, potinho de cacau, torso; nada mais em quadro.",
                    frame0="colher cheia, os primeiros grãos caindo.",
                    desvio="regata branca da âncora no torso; mesa preta; luz neutra.",
                    ev=dict(F1="a metal spoon heaped with dark cocoa powder right above the yolks", F2="The bowl fills the bottom 60 percent of the frame",
                            F3="about 30 centimeters from the lens", F4="at chest height, looking down at about 45 degrees into the bowl, 26 mm wide lens",
                            F5="her left hand holds a small clear glass bowl of cocoa powder just behind it", F6="Nothing else is in frame."),
                    g8=False)),
    dict(codigo="K04", take="T4", titulo="close, mel cru escorrendo da colher", anexos=1,
         reference_use=REF,
         prop="Inside a round clear glass mixing bowl on the black table: roughly mashed black beans with raw egg and cocoa powder on top. Her right hand holds a metal spoon above the bowl, and a thick glossy stream of golden raw honey pours from it onto the beans. Nothing else is in frame.",
         posture=f"Close shot: {MAOS}.",
         composition="The bowl fills the bottom 55 percent of the frame, about 30 centimeters from the lens, very close to the lens and large in frame, the honey stream in the center of the frame. No face in frame. The background is reduced by framing, never by blur.",
         camera="phone camera at chest height just above the bowl rim, slight downward angle, 26 mm wide lens, fixed",
         state="Start frame: the honey stream is already falling in one unbroken golden ribbon.",
         neg=NEG_PHONE + ", no face in frame",
         ficha=dict(heroi="fio grosso e brilhante de mel cru dourado caindo da colher de metal sobre o feijão preto na tigela de vidro.",
                    termos=["thick glossy stream of golden raw honey", "round clear glass mixing bowl"],
                    quadro="a tigela ocupa ~55% de baixo, o fio de mel no centro.",
                    dist="no modelo ~30 cm; no K, 30 cm.",
                    cam="celular na altura do peito logo acima da borda da tigela, leve inclinação para baixo, lente 1x.",
                    pose="só a mão direita com a colher; a esquerda apoiada na borda.",
                    lista="tigela, colher, fio de mel, torso; nada mais.",
                    frame0="o fio de mel já caindo inteiro.",
                    desvio="regata branca da âncora; luz neutra.",
                    ev=dict(F1="a thick glossy stream of golden raw honey pours from it onto the beans", F2="The bowl fills the bottom 55 percent of the frame",
                            F3="about 30 centimeters from the lens", F4="at chest height just above the bowl rim, slight downward angle, 26 mm wide lens",
                            F5="Her right hand holds a metal spoon above the bowl", F6="Nothing else is in frame."),
                    g8=False)),
    dict(codigo="K05", take="T5", titulo="close, canela em pó caindo no centro da tigela", anexos=1,
         reference_use=REF,
         prop="Inside a round clear glass mixing bowl on the black table: roughly mashed black beans glossy with honey, egg and cocoa. Her right hand tips a metal spoon of reddish-brown ground cinnamon over the center of the bowl, the powder just starting to fall. Nothing else is in frame.",
         posture=f"Close shot: {MAOS}.",
         composition="The bowl fills the bottom 60 percent of the frame, about 30 centimeters from the lens, very close to the lens and large in frame, the spoon of cinnamon at the center. No face in frame. The background is reduced by framing, never by blur.",
         camera="phone camera at chest height above the bowl, looking down at about 45 degrees, 26 mm wide lens, fixed",
         state="Start frame: the spoon is tipping and the first cinnamon falls onto the glossy beans.",
         neg=NEG_PHONE + ", no face in frame",
         ficha=dict(heroi="colher de metal com canela em pó marrom-avermelhada virando sobre o centro da tigela de feijão brilhante de mel.",
                    termos=["reddish-brown ground cinnamon", "round clear glass mixing bowl"],
                    quadro="a tigela ocupa ~60% de baixo, a colher no centro.",
                    dist="no modelo ~30 cm; no K, 30 cm.",
                    cam="celular na altura do peito acima da tigela, ~45° para baixo, lente 1x.",
                    pose="só a mão direita virando a colher.",
                    lista="tigela, colher, canela, torso; nada mais.",
                    frame0="a colher virando, a primeira canela caindo.",
                    desvio="regata branca da âncora; luz neutra.",
                    ev=dict(F1="a metal spoon of reddish-brown ground cinnamon over the center of the bowl", F2="The bowl fills the bottom 60 percent of the frame",
                            F3="about 30 centimeters from the lens", F4="at chest height above the bowl, looking down at about 45 degrees, 26 mm wide lens",
                            F5="Her right hand tips a metal spoon", F6="Nothing else is in frame."),
                    g8=False)),
    dict(codigo="K06", take="T6", titulo="close, batedor na massa de chocolate (voz fora de quadro)", anexos=1,
         reference_use=REF,
         prop="A round clear glass mixing bowl on the black table is full of smooth, glossy, thick chocolate-brown batter. Her right hand works a stainless steel wire whisk through it, leaving swirls, and her left hand steadies the bowl rim. Nothing else is in frame.",
         posture=f"Close shot: {MAOS}.",
         composition="The bowl of batter fills the bottom 60 percent of the frame, about 30 centimeters from the lens, very close to the lens and large in frame, the whisk swirls at the center. No face in frame. The background is reduced by framing, never by blur.",
         camera="phone camera at chest height just above the bowl, slight downward angle, 26 mm wide lens, fixed",
         state="Start frame: the whisk is mid-stroke in the smooth glossy batter.",
         neg=NEG_PHONE + ", no face in frame, no whole beans visible in the batter",
         ficha=dict(heroi="massa de chocolate lisa, grossa e brilhante na tigela de vidro, com o batedor de arame fazendo espirais.",
                    termos=["smooth, glossy, thick chocolate-brown batter", "stainless steel wire whisk"],
                    quadro="a tigela ocupa ~60% de baixo, o batedor no centro.",
                    dist="no modelo ~30 cm; no K, 30 cm.",
                    cam="celular na altura do peito logo acima da tigela, leve inclinação, lente 1x.",
                    pose="mão direita com o batedor, esquerda segurando a borda.",
                    lista="tigela, massa, batedor, mãos, torso; nada mais.",
                    frame0="batedor no meio do movimento.",
                    desvio="regata branca da âncora; luz neutra.",
                    ev=dict(F1="full of smooth, glossy, thick chocolate-brown batter", F2="The bowl of batter fills the bottom 60 percent of the frame",
                            F3="about 30 centimeters from the lens", F4="at chest height just above the bowl, slight downward angle, 26 mm wide lens",
                            F5="her left hand steadies the bowl rim", F6="Nothing else is in frame."),
                    g8=False)),
    dict(codigo="K07", take="T7", titulo="close, massa escorrendo para a forma forrada", anexos=1,
         reference_use=REF,
         prop="Her left hand tilts the round clear glass mixing bowl over a square dark metal baking tin lined with parchment paper on the black table, and a thick ribbon of glossy chocolate batter pours out and folds into a mound in the center of the tin. Her right hand holds the wire whisk against the bowl. Nothing else is in frame.",
         posture=f"Close shot: {MAOS}.",
         composition="The square baking tin fills the bottom 45 percent of the frame, about 35 centimeters from the lens, very close to the lens and large in frame; the ribbon of batter runs down the center of the frame from the tilted bowl. No face in frame. The background is reduced by framing, never by blur.",
         camera="phone camera at chest height, looking down at about 40 degrees at the tin on the table, 26 mm wide lens, fixed",
         state="Start frame: the ribbon of batter is already falling and has started a small mound in the tin.",
         neg=NEG_PHONE + ", no face in frame",
         ficha=dict(heroi="fita grossa de massa de chocolate brilhante escorrendo da tigela inclinada e dobrando num montinho no centro da forma quadrada forrada com papel manteiga.",
                    termos=["square dark metal baking tin lined with parchment paper", "thick ribbon of glossy chocolate batter"],
                    quadro="a forma ocupa ~45% de baixo, a fita de massa no centro, a tigela inclinada no alto.",
                    dist="no modelo ~35 cm; no K, 35 cm.",
                    cam="celular na altura do peito, ~40° para baixo na forma, lente 1x.",
                    pose="mão esquerda inclinando a tigela, direita com o batedor encostado.",
                    lista="tigela, batedor, forma forrada, massa; nada mais.",
                    frame0="a fita já caindo, montinho começando.",
                    desvio="mesa preta no lugar do mármore; luz neutra.",
                    ev=dict(F1="a thick ribbon of glossy chocolate batter pours out and folds into a mound in the center of the tin", F2="The square baking tin fills the bottom 45 percent of the frame",
                            F3="about 35 centimeters from the lens", F4="at chest height, looking down at about 40 degrees at the tin on the table, 26 mm wide lens",
                            F5="Her left hand tilts the round clear glass mixing bowl", F6="Nothing else is in frame."),
                    g8=False)),
    dict(codigo="K08", take="T8", titulo="a forma entrando no forno de bancada do box", anexos=1,
         reference_use=REF + " The countertop oven is new: it stands on the same metal-and-wood shelf of her garage box.",
         prop="A stainless steel countertop convection oven with a black glass door, a plain smooth front and two simple round black knobs, stands on the metal-and-wood shelf of her garage box, the door wide open and the wire rack visible inside. Her two hands slide the square metal baking tin of raw chocolate batter, lined with parchment paper, onto the rack. Nothing else is in frame.",
         posture="Only her forearms and hands enter the frame from the left, sliding the tin in; no face in frame.",
         composition="The open countertop oven fills about 70 percent of the frame, its open door about 50 centimeters from the lens, large in frame and centered, the tin halfway onto the rack. No face in frame. The background is reduced by framing, never by blur.",
         camera="phone camera at counter level on the shelf, level with the oven rack, 26 mm wide lens, straight on, fixed",
         state="Start frame: the tin is halfway onto the rack, the oven light on inside.",
         neg=NEG_PHONE + ", no face in frame",
         ficha=dict(heroi="forno aberto com a forma de massa crua entrando na grade; só antebraços e mãos entram pela esquerda.",
                    termos=["stainless steel countertop convection oven", "square metal baking tin of raw chocolate batter"],
                    quadro="o forno aberto ocupa ~70% do quadro, centralizado; as mãos entram pela esquerda.",
                    dist="no modelo ~50 cm; no K, 50 cm.",
                    cam="celular na altura da prateleira, nivelado com a grade, lente 1x, frontal.",
                    pose="só antebraços e mãos empurrando a forma.",
                    lista="forno, grade, forma, mãos; nada mais.",
                    frame0="forma no meio do caminho para dentro da grade.",
                    desvio="a âncora não tem forno: forno de bancada na prateleira de metal e madeira do mesmo box (PERFIL_ORGANICO 4.1); luz neutra.",
                    ev=dict(F1="stainless steel countertop convection oven with a black glass door", F2="The open countertop oven fills about 70 percent of the frame",
                            F3="its open door about 50 centimeters from the lens", F4="at counter level on the shelf, level with the oven rack, 26 mm wide lens, straight on",
                            F5="Only her forearms and hands enter the frame from the left", F6="Nothing else is in frame."),
                    g8=False)),
    dict(codigo="K09", take="T9", titulo="reveal, brownie pronto na mesa e os potinhos na frente", anexos=1,
         reference_use=REF,
         prop="On the black table in front of her: a square dark metal baking tin of freshly baked fudgy brownies with a crackly shiny top, still in its parchment paper, and in front of it a row of five small bowls holding black beans, cocoa powder, one raw egg yolk, ground cinnamon and golden raw honey, with a pair of grey oven mitts at the left. Nothing else is on the table.",
         posture="Brandon is standing behind her black table, both hands raised in front of her chest mid-gesture, open palms, talking.",
         composition="The tin of brownies and the row of small bowls fill the bottom 30 percent of the frame, the front bowls about 40 centimeters from the lens, closer to the camera than her face. From the waist up, her head and upper chest clear and centered in the upper half of the frame, her face about 80 centimeters from the lens. The background is reduced by framing, never by blur.",
         camera=CAM_PEITO,
         state=f"Start frame: Brandon gestures with both open hands over the brownies, eyes on the lens, {BOCA}.",
         neg=NEG_PHONE + ", no chef jacket",
         ficha=dict(heroi="forma com o brownie assado de casquinha craquelada e brilhante, com a fila de potinhos (feijão, cacau, gema, canela, mel) na frente e as luvas de forno à esquerda.",
                    termos=["freshly baked fudgy brownies with a crackly shiny top", "row of five small bowls"],
                    quadro="forma e potinhos ocupam ~30% de baixo; pessoa da cintura para cima no centro.",
                    dist="no modelo os potinhos estão a ~45 cm; no K, 40 cm.",
                    cam="celular fixo na altura do peito, lente 1x, frontal.",
                    pose="atrás da bancada, as duas mãos abertas gesticulando na frente do peito.",
                    lista="forma de brownie, cinco potinhos, luvas; nada mais na bancada.",
                    frame0="mãos abertas no meio do gesto, boca aberta.",
                    desvio="Brandon e box da âncora; luz neutra (o modelo tem janela ao fundo).",
                    ev=dict(F1="square dark metal baking tin of freshly baked fudgy brownies with a crackly shiny top", F2="fill the bottom 30 percent of the frame",
                            F3="the front bowls about 40 centimeters from the lens", F4="at chest height, 26 mm wide lens, straight on",
                            F5="both hands raised in front of her chest mid-gesture", F6="Nothing else is on the table."),
                    g8=True)),
    dict(codigo="K11", take="T11", titulo="selfie com o pedaço de brownie perto da lente (fechamento e CTA)", anexos=1,
         reference_use=REF,
         prop="Brandon holds a thick square piece of fudgy chocolate brownie with a crackly shiny top in her right hand, close to the lens at the lower left of the frame. The piece is whole, not bitten.",
         posture="Selfie: her left arm is stretched out toward the camera holding the phone out of frame at the right edge; her right hand holds the brownie piece up near the lens.",
         composition="Tightest shot of the video. The brownie piece fills about 15 percent of the frame at the lower left, about 25 centimeters from the lens, closer to the camera than her face; her face is clear in the upper center, about 50 centimeters from the lens, head and shoulders in frame, the extended left arm entering from the right edge. The background is reduced by framing, never by blur.",
         camera="front phone camera held at arm's length at eye level, ultra-wide 0.5x selfie lens, slight high angle, handheld",
         state=f"Start frame: Brandon looks straight into the lens with a serious, certain expression, {BOCA}.",
         neg=", no bitten brownie",
         ficha=dict(heroi="pedaço quadrado e grosso de brownie de casquinha craquelada na mão, perto da lente no canto inferior esquerdo, em selfie de braço esticado.",
                    termos=["thick square piece of fudgy chocolate brownie", "Selfie"],
                    quadro="o pedaço ocupa ~15% no canto inferior esquerdo; rosto no centro-alto; braço esticado entrando pela direita.",
                    dist="no modelo ~30 cm; no K, 25 cm.",
                    cam="câmera frontal do celular no braço esticado, na altura dos olhos, ultra-wide 0,5x, leve ângulo de cima.",
                    pose="braço esquerdo esticado segurando o celular fora de quadro, mão direita com o brownie perto da lente.",
                    lista="pessoa, pedaço de brownie, box ao fundo; nada mais.",
                    frame0="olhando na lente, expressão séria e certa, boca aberta.",
                    desvio="box da âncora no lugar da janela com árvores; expressão séria no lugar do sorriso (o fechamento é de venda); luz neutra.",
                    ev=dict(F1="a thick square piece of fudgy chocolate brownie with a crackly shiny top", F2="The brownie piece fills about 15 percent of the frame at the lower left",
                            F3="about 25 centimeters from the lens", F4="held at arm's length at eye level, ultra-wide 0.5x selfie lens",
                            F5="her left arm is stretched out toward the camera holding the phone out of frame", F6="The piece is whole, not bitten."),
                    g8=True)),
]


def k_json(k):
    return {
        "shot_id": f"{k['codigo']}_{k['take'].lower()}_{ARQ.lower()}",
        "format": FORMATO,
        "fiction_note": FICCAO,
        "reference_use": k["reference_use"],
        "identity_main": IDENTIDADE,
        "wardrobe": ROUPA,
        "scene": CENA,
        "prop": k["prop"],
        "posture": k["posture"],
        "composition": k["composition"],
        "camera": k["camera"],
        "lighting": LUZ,
        "state": k["state"],
        "realism": REALISMO,
        "aspect_ratio": "9:16 vertical",
        "negative": NEG + k["neg"],
    }


def json_flow(j):
    return json.dumps({c: v for c, v in j.items() if c != "shot_id"}, ensure_ascii=False, indent=2)


def k_de(num):
    """Perfil classico: o maior K <= numero do V."""
    cod = [int(k["codigo"][1:]) for k in KS]
    return "K%02d" % max(c for c in cod if c <= num)


VOZ = "voz feminina média, firme e calorosa de uma mulher atlética de uns trinta anos"
SOTAQUE = "de uma mulher negra americana"
SOM = "box de treino tranquilo"
EMOCAO = {
    "T1": "entonação direta e curiosa, de quem vai contar uma receita que parece impossível",
    "T2": "no ritmo de quem dita uma receita, clara e segura",
    "T6": "no ritmo de quem dita uma receita, clara e segura",
    "T9": "entonação animada e apetitosa, com um sorriso na voz",
    "T10": "entonação confiante e calorosa",
    "T11": "a voz muda de animada para séria, firme, como quem vai contar o que ninguém conta",
    "T12": "entonação firme e acolhedora, com convicção total no 'It's not'",
    "T13": "entonação didática e firme, sem pressa",
    "T14": "entonação firme, com um leve tom de indignação com o app",
    "T15": "entonação direta e segura, sem sorrir, olhando fundo na lente",
    "T16": "entonação firme, urgente e convicta, sem tom de oferta, como quem aponta a única saída",
}
ACOES = {
    "T1": "Brandon amassa o feijão preto na tigela com o amassador, duas ou três vezes, segurando a tigela perto da câmera; ela diz a frase em ritmo natural logo no começo e continua amassando olhando para a lente.",
    "T2": "a mão vira o potinho e os dois ovos caem inteiros dentro da tigela de feijão; só a regata e a ponta do queixo aparecem, o rosto fica fora de quadro. A voz diz a frase inteira em ritmo natural logo no começo e o resto do clipe é a tigela.",
    "T3": "a colher vira o cacau em pó dentro da tigela, em cima dos ovos e do feijão.",
    "T4": "o mel cru cai da colher em fio grosso e dourado sobre o feijão.",
    "T5": "a colher vira a canela em pó no centro da tigela.",
    "T6": "o batedor de arame gira na massa de chocolate lisa e brilhante, fazendo espirais; só as mãos e a regata aparecem. A voz diz a frase inteira em ritmo natural logo no começo e o resto do clipe é a massa sendo batida.",
    "T7": "a tigela inclina e a massa grossa de chocolate escorre em fita para dentro da forma forrada, empilhando em dobras.",
    "T8": "as mãos empurram a forma até o fundo do forno de bancada e a porta começa a fechar.",
    "T9": "Brandon gesticula com as duas mãos abertas por cima do brownie e fala para a câmera, animada.",
    "T10": "Brandon continua falando para a câmera com gestos pequenos por cima do brownie, confiante.",
    "T11": "Brandon, em selfie, segura o pedaço de brownie perto da lente e fala direto com a câmera; a expressão muda de animada para séria.",
    "T12": "Brandon, em selfie, segura o pedaço de brownie perto da lente e fala direto com a câmera, firme, balançando a cabeça de leve no 'It's not'.",
    "T13": "Brandon, em selfie, levanta um pouco o pedaço de brownie no 'This brownie calms one' e fala direto com a câmera.",
    "T14": "Brandon, em selfie, segura o pedaço de brownie perto da lente e fala direto com a câmera, firme.",
    "T15": "Brandon, em selfie, segura o pedaço de brownie perto da lente e fala direto com a câmera, séria e segura.",
    "T16": "Brandon, em selfie, se aproxima um pouco da lente e fala direto com a câmera, firme e urgente, segurando o pedaço de brownie.",
}
CAMERA = {
    "T1": "fixa, no tripé, na altura do peito", "T2": "fixa, levemente de cima para a tigela",
    "T3": "fixa, de cima para dentro da tigela", "T4": "fixa, logo acima da borda da tigela",
    "T5": "fixa, de cima para dentro da tigela", "T6": "fixa, logo acima da tigela",
    "T7": "fixa, de cima para a forma", "T8": "fixa, na altura da prateleira do forno",
    "T9": "fixa, no tripé, na altura do peito", "T10": "fixa, no tripé, na altura do peito",
}
SELFIE_CAM = "selfie na mão com leve tremor natural; a mão que segura o celular nunca se mexe, só a outra mão se move com o brownie"
SOM_EXTRA = {"T1": ", som do amassador no feijão", "T2": ", som leve dos ovos caindo", "T3": ", som leve da colher",
             "T4": "", "T5": ", som leve da colher", "T6": ", som do batedor na tigela de vidro",
             "T7": ", som leve da massa caindo", "T8": ", som do forno e da grade de metal"}
B_ROLL_VO = {"T3": "T2", "T4": "T2", "T5": "T2", "T7": "T6", "T8": "T6"}

TRANSCRICAO_PT = {}
for m in re.finditer(r"^\| (T\d+) \| (.+?) \| (.+?) \|$", ROTEIRO.split("## Tabela bilíngue", 1)[1].split("##", 1)[0], re.M):
    TRANSCRICAO_PT[m.group(1)] = m.group(3)
CORTE = {"T1": "0,0 a 2,4 s", "T2": "2,4 a 3,5 s (o áudio corre até 8,2 s)", "T3": "3,5 a 5,2 s", "T4": "5,2 a 6,8 s",
         "T5": "6,8 a 8,2 s", "T6": "8,2 a 9,1 s (o áudio corre até 10,9 s)", "T7": "9,1 a 10,5 s", "T8": "10,5 a 10,9 s",
         "T9": "10,9 a 19,2 s", "T10": "19,2 a 24,7 s", "T11": "clipe inteiro, corte no fim da frase",
         "T12": "clipe inteiro, corte no fim da frase", "T13": "clipe inteiro, corte no fim da frase",
         "T14": "clipe inteiro, corte no fim da frase", "T15": "clipe inteiro, corte no fim da frase",
         "T16": "clipe inteiro, corte no fim da frase"}


def videos():
    vs = []
    for i, t in enumerate(TAKES, 1):
        som = f"som ambiente: {SOM}{SOM_EXTRA.get(t, '')}, sem música"
        cam = SELFIE_CAM if t in SELFIE else CAMERA[t]
        acao = ACOES[t]
        if t in MUDOS:
            txt = (f"(sem fala no take: a fala do {B_ROLL_VO[t]} continua como voz-over na edição)\n\n"
                   f"o que acontece no vídeo: {acao}\n\ncâmera: {cam}\n\n{som}")
        else:
            fora = ", fora de quadro (só as mãos e a regata aparecem, o rosto fica acima do quadro)," if t in VOZ_OVER else ","
            txt = (f"a avatar {NOME}, mulher{fora} fala em inglês com sotaque americano {SOTAQUE}, {VOZ}, "
                   f"{EMOCAO[t]}, voz autêntica, como se exigisse ser ouvida, a seguinte frase: \"{FALAS[t]}\"\n\n"
                   "a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.\n\n"
                   f"o que acontece no vídeo: {acao}\n\ncâmera: {cam}\n\n{som}")
        vs.append((f"V{i:02d}", t, k_de(i), txt))
    return vs


def rotulo(k):
    return "ÂNCORA HOLISTIC BRANDON" + (" + FRAME DO MODELO" if k["anexos"] > 1 else "")


def anexo(k):
    L = [f"> ### 📎 ANEXAR: **{k['anexos']} {'IMAGENS' if k['anexos'] > 1 else 'IMAGEM'}**",
         f"> **1️⃣ ÂNCORA HOLISTIC BRANDON** `{ANCORA}`"]
    if k["anexos"] > 1:
        L.append("> **2️⃣ FRAME DO MODELO, só composição** `input/frames_modelo/K01_modelo.png`")
    return "\n".join(L + [">", "> ### 🆕 GERAR DO ZERO"])


def montagem():
    return [
        "1. Clipes numerados na ordem: " + ", ".join(v[0] for v in videos()) + ".",
        "2. Cortes no tempo das cenas do modelo: " + "; ".join(f"V{t[1:].zfill(2)} {CORTE[t]}" for t in TAKES) + ".",
        "3. Voz-over: o áudio do V02 corre por baixo de V02, V03, V04 e V05; o do V06 corre por baixo de V06, V07 e V08. Os B-rolls entram sem áudio próprio.",
        "4. Zero tempo morto: todo clipe falado começa já falando. Isolate Voice / Keep Vocal no áudio.",
        "5. Legenda de uma palavra por vez, caixa alta, fonte bold branca com contorno, no meio do quadro, do começo ao fim, igual ao modelo.",
        "6. Sem Voice Changer: a voz vem do prompt de cada V.",
        "7. Música só do V09 em diante, nunca no gancho nem na receita, entre -19 e -20 dB, fora da biblioteca do TikTok.",
        "8. Rótulo pequeno `AI-generated` num canto do vídeo.",
        "9. No V16, uma seta de edição apontando para baixo (comentário fixado) na frase \"Tap the link in the pinned comment\". Fixar o comentário com o link no vídeo publicado.",
    ]


def ficha_md():
    L = ["# FICHA DOS FRAMES · fitywell_brownie_feijao", "",
         "Escrita olhando cada frame do modelo em `input/frames_modelo/` (GATE_VISUAL.md Parte 6). O modelo manda no",
         "conteúdo; o gate manda no acabamento; a proximidade do herói é a mais perto entre os dois. O K10 não existe:",
         "o V10 usa o K09 (mesmo quadro), e o V11 a V16 usam o K11 (a mesma selfie).", ""]
    for k in KS:
        f, j = k["ficha"], json.dumps(k_json(k), ensure_ascii=False)
        L += [f"## {k['codigo']}", f"Frame: `input/frames_modelo/{k['codigo']}_modelo.png`", f"Take: {k['take']}",
              f"Herói: {f['heroi']}", "Termos de forma: " + " · ".join(f'"{x}"' for x in f["termos"]),
              f"Quadro: {f['quadro']}", f"Distância da lente: {f['dist']}", f"Câmera: {f['cam']}", f"Pose: {f['pose']}",
              f"Lista fechada: {f['lista']}", f"Frame 0: {f['frame0']}", f"Desvio (acabamento ou avatar fixo): {f['desvio']}", "",
              "| Item | Status | Evidência |", "|---|---|---|"]
        ev = dict(f["ev"], G1="soft even light on the face with no harsh shadows", G3="everything in sharp focus",
                  G4="Real skin with visible pores", G5="no warm orange color cast", G6="no captions", G7="small American flag")
        for item, rot in [("F1", "forma do herói"), ("F2", "quanto do quadro"), ("F3", "distância da lente"), ("F4", "câmera"),
                          ("F5", "pose do avatar"), ("F6", "lista fechada"), ("G1", "luz neutra")]:
            assert ev[item] in j, (k["codigo"], item, ev[item])
            L.append(f'| {item} {rot} | OK | "{ev[item]}" |')
        L.append("| G2 céu ou janela | N/A | o box da âncora não tem janela em quadro; a luz vem da porta da garagem fora de quadro |")
        for item, rot in [("G3", "foco"), ("G4", "realismo"), ("G5", "sem tom quente"), ("G6", "sem texto"), ("G7", "bandeira")]:
            assert ev[item] in j, (k["codigo"], item)
            L.append(f'| {item} {rot} | OK | "{ev[item]}" |')
        if f["g8"]:
            assert "caught mid-sentence" in j
            L.append('| G8 boca no K de fala | OK | "caught mid-sentence" |')
        else:
            L.append("| G8 boca no K de fala | N/A | sem rosto em quadro (close de mãos ou voz fora de quadro, como no modelo) |")
        for termo in f["termos"]:
            assert termo in j, (k["codigo"], termo)
        L.append("")
    return "\n".join(L)


def pacote():
    vs = videos()
    L = ["# holistic.brandon | FityWell Venda Brownie de feijão preto | Pacote de Prompts", "",
         "Vídeo modelo: `input/reference_video.mp4` (32,5 s, Chef Joey, avatar IA)", "",
         f"Âncora: `{ANCORA}`", "",
         "Funil: VENDA. comment yes + follow (engajamento) e o link do plano personalizado Metabolic Reset da FityWell no comentário fixado. Rodada de validação, gancho fiel ao modelo. Sem produto em quadro.", "",
         "## Índice de geração", "", "| Take | Keyframe | Anexar | Ação |", "|---|---|---|---|"]
    for cod, t, kc, _ in vs:
        k = next(x for x in KS if x["codigo"] == kc)
        acao = "GERAR DO ZERO" if k["take"] == t else f"REUSA a imagem aprovada do {kc} (mesmo quadro)"
        L.append(f"| {t} | {kc} | {rotulo(k)} | {acao} |")
    L += ["", "Todo K é GERAR DO ZERO e autossuficiente. Perfil clássico: V10 usa o K09 e V11 a V16 usam o K11, sem imagem nova.", "",
          "## Trava de identidade e continuidade", "",
          f"- Identidade: {IDENTIDADE}", f"- Roupa: {ROUPA}", f"- Cenário (fixo da conta, em todos os K): {CENA}",
          f"- Luz: {LUZ}", f"- Voz (igual em todos os V): {VOZ}, sotaque americano {SOTAQUE}.",
          "- Sem 2ª pessoa. Nos closes de receita (K02 a K08) o rosto fica fora de quadro, como no modelo.", "",
          "## Trava do prop herói", "",
          "- T1: tigela de vidro redonda cheia de feijão preto cozido + amassador de inox de placa furada.",
          "- Receita: dois ovos crus inteiros, cacau em pó escuro, mel cru dourado, canela em pó, batedor de arame, forma quadrada escura forrada com papel manteiga, forno de bancada de inox na prateleira do box.",
          "- T9: forma com o brownie assado de casquinha craquelada + fila de cinco potinhos + luvas de forno cinza.",
          "- T11 a T16: pedaço quadrado e grosso de brownie na mão, inteiro, perto da lente.",
          "- Nenhuma embalagem, garrafa ou forno com marca ou texto.", "",
          "## Trava da 2ª pessoa (REF-A)", "", "- Não se aplica: não há 2ª pessoa.", "",
          "## Prompts de imagem", ""]
    for k in KS:
        L += [f"## {k['codigo']} · {k['take']} · GERAR DO ZERO · {rotulo(k)}", "", anexo(k), "",
              f"Cena: {k['titulo']}.", "", "```json", json.dumps(k_json(k), ensure_ascii=False, indent=2), "```", ""]
    L += ["## Bloco global de vídeo", "", "```text",
          f"a avatar {NOME}, mulher, fala em inglês com sotaque americano {SOTAQUE}, {VOZ}, [emoção da fala], voz autêntica, como se exigisse ser ouvida, a seguinte frase: \"[FALA EXATA DO ROTEIRO]\"", "",
          "a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.", "",
          "o que acontece no vídeo: [ação enxuta]", "", "câmera: [fixa]", "", f"som ambiente: {SOM}, sem música", "```", "",
          "# Prompts de vídeo", ""]
    for cod, t, kc, txt in vs:
        L += [f"### {cod} · {t} · usa {kc}", "", "```text", txt, "```", ""]
    L += ["## Mapa de âncoras", "", "| Keyframe | Referências a anexar | Modelo |", "|---|---|---|",
          "| K01 | ÂNCORA HOLISTIC BRANDON + FRAME DO MODELO (`input/frames_modelo/K01_modelo.png`, só composição) | Nano Banana 2, 9:16, 4 imagens |",
          "| K02 a K09, K11 | ÂNCORA HOLISTIC BRANDON | Nano Banana 2, 9:16, 4 imagens |", "",
          "| V | Frame inicial |", "|---|---|"]
    L += [f"| {cod} | a imagem que sobrou no {kc} |" for cod, _, kc, _ in vs]
    L += ["", "## Montagem no CapCut", "", *montagem(), "", "## Gates de qualidade", "",
          "1. Fala de cada V igual ao ROTEIRO, palavra por palavra.",
          "2. Um take por cena do modelo; T1, T6 e os B-rolls marcados; nenhum take acima de 29 palavras.",
          "3. Bandeira dos EUA no campo scene de todo K.", "4. Zero travessão.",
          "5. Keyword `yes` no T15; destino no comentário fixado no T16; nunca DM, \"I'll send you\" nem \"free\".",
          "6. Produto fora de quadro, nenhuma embalagem ou forno com marca.", "7. Negative sem termo sensível.",
          "8. GATE_VISUAL Partes 1 a 3 em todo K: herói colado na lente com medida, luz neutra, sem tom quente, sem blur, trecho de realismo.",
          "9. Gancho fiel no conteúdo: tigela de feijão preto colada na lente com o amassador, falado desde o segundo 0.",
          "10. FICHA_FRAMES.md com placar 14/14 de cada K antes do envio.", ""]
    flow = ["# Blocos limpos para o Google Flow | Brandon", "", f"Fonte interna: `PROMPTS_{ARQ}.md`", "",
            "## BLOCO DE IMAGEM", "", "```text"]
    for k in KS:
        flow += [k["codigo"], json_flow(k_json(k)), ""]
    flow += ["```", "", "## BLOCO DE VÍDEO", "", "```text"]
    for cod, _, _, txt in vs:
        flow += [cod, txt, ""]
    flow += ["```", ""]
    return "\n".join(L) + "\n", "\n".join(flow) + "\n"


def main():
    p, f = pacote()
    (AQUI / f"PROMPTS_{ARQ}.md").write_text(p, encoding="utf-8")
    (AQUI / "PROMPTS_PRODUCAO.md").write_text(p, encoding="utf-8")
    (AQUI / f"FLOW_{ARQ}.md").write_text(f, encoding="utf-8")
    (AQUI / "FICHA_FRAMES.md").write_text(ficha_md(), encoding="utf-8")
    print("ok: %d K, %d V, ficha escrita" % (len(KS), len(videos())))


if __name__ == "__main__":
    main()
