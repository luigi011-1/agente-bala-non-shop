"""Gera o pacote da producao fitywell_growth_v1 (FitWell growth, inchaco da manha, 25 takes).

Fonte unica da fala: takes.json (espelho do ROTEIRO.md aprovado em 2026-10-09; T11 reescrito antes do pacote).
Saidas: PROMPTS_PRODUCAO.md (fonte interna, K em JSON, o que o linter e a ficha leem), FICHA_FRAMES.md,
ENTREGA_BRANDON.md (K em paragrafo e V minimo, padrao unico do Flow de 2026-10-09) e AGENTE_FLOW.md.

Uso: python3 gerar_pacote.py
"""
import json
import re
from pathlib import Path

AQUI = Path(__file__).resolve().parent
TAKES = json.loads((AQUI / "takes.json").read_text(encoding="utf-8"))
ANCORA = "producao/_ancoras/holistic_brandon_ancora.jpg"

ID = ("Brandon, a Black mixed-race American woman around thirty with an athletic build, light brown skin, light "
      "freckles across her nose and cheeks, brown eyes, long box braids with wooden beads at the tips, a floral "
      "tattoo sleeve on her right arm and a fine tattoo on the inside of her left arm.")
WARD = "She wears a white ribbed tank top, loose black training shorts and a thin gold chain with a small gold cross."
SCENE = ("Her own training box, the same room as the attached image: white-painted concrete block walls, a red neon "
         "sign at the left, a small American flag on the wall at the right, discreet but visible and in focus, and a "
         "shelf of glass jars with seeds at the far right.")
SCENE_BANC = ("Her own training box, the same room as the attached image: white-painted concrete block wall behind a "
              "light stone counter, a red neon sign at the left, a small American flag on the wall at the right, "
              "discreet but visible and in focus.")
LUZ = "Neutral overcast daylight from the open box door out of frame, soft even light on the face with no harsh shadows."
FECHO = ("Neutral overcast daylight, true neutral colors, real skin texture, phone footage look, everything in "
         "sharp focus, text-free frame, 9:16 vertical.")
FECHO_PLACA = ("Neutral overcast daylight, true neutral colors, real skin texture, phone footage look, "
               "everything in sharp focus, the only text is the plaque, 9:16 vertical.")
REALISMO = ("Real skin with visible pores, fine lines and soft asymmetry, hair in uneven natural clumps, phone "
            "footage look, flat natural light, low contrast, everything in sharp focus, no warm orange color cast, "
            "no captions.")
NEG = ("no captions, no subtitles, no words overlaid on the image, no printed labels on any container, no plastic "
       "skin, no extra fingers, no blur, no warm orange color cast, no yellow tint, no golden hour light")

TRI = "phone camera on a tripod at chest height, 26 mm wide lens, straight on, fixed"
SELFIE = "phone held at arm's length at eye level, 26 mm wide lens, handheld selfie angle"
MACRO = "phone camera low over the counter at counter height, 26 mm wide lens, tilted down about 45 degrees"
BOCA = "caught mid-sentence, lips naturally parted, animated expression"

# cada K: titulo (PT), prop, posture, composition, camera, state, cara (rosto em quadro), selfie (bool), placa (bool)
# e a ficha: heroi (PT), termos (literais no K), quadro/dist/pose/lista (PT), ev F2..F5 (literais no K)
K = {
1: dict(titulo="olho inchado da cliente colado na lente, avatar apontando", cena=SCENE, cara=True, selfie=True,
        prop="At the left edge of the frame a woman in her fifties, a client, is cropped by the frame: only her eye and cheek are visible, the lower eyelid visibly swollen with a soft bag under it, her skin tired.",
        posture="Brandon stands crouched at the right of the frame, her right index finger pointing straight into the lens.",
        composition="The client's swollen eye fills the left 40 percent of the frame, about 20 centimeters from the lens, closer to the camera than Brandon's face; Brandon's face sits in the right half about 80 centimeters away. Only these elements are in the frame.",
        camera=SELFIE, state=f"Start frame: Brandon looks into the lens, {BOCA}.",
        heroi="olho inchado de uma cliente (pálpebra inferior inchada, bolsa sob o olho), cortado pela borda esquerda do quadro",
        termos=["swollen eye", "lower eyelid visibly swollen"],
        quadro="o olho ocupa os 40% da esquerda do quadro", dist="~20 cm da lente (no modelo, colado na lente)",
        pose="avatar agachada à direita, indicador apontado para a lente, boca no meio da frase",
        lista="cliente cortada, avatar, parede do box",
        f2="fills the left 40 percent of the frame", f3="about 20 centimeters from the lens", f4="phone held at arm's length at eye level",
        f5="her right index finger pointing straight into the lens"),
2: dict(titulo="close do olho da cliente, avatar de cócoras fazendo pinça", cena=SCENE, cara=True, selfie=True,
        prop="A woman's eye fills the left foreground, cropped by the frame: the lower eyelid swollen with a soft bag under it, the skin around it tired.",
        posture="Brandon is crouched behind it at the right, smiling at the lens, her right thumb and index finger pinched together in front of her chest.",
        composition="The client's swollen eye fills the left 45 percent of the frame, about 15 centimeters from the lens, much closer than Brandon's face, which sits in the right half about 90 centimeters away. Only these elements are in the frame.",
        camera=SELFIE, state=f"Start frame: Brandon smiles at the lens, {BOCA}.",
        heroi="olho da cliente em close extremo, pálpebra inferior inchada", termos=["swollen eye", "swollen with a soft bag"],
        quadro="o olho ocupa 45% da esquerda do quadro", dist="~15 cm da lente", pose="avatar de cócoras ao fundo, pinça com a mão, sorrindo",
        lista="olho da cliente, avatar, parede do box",
        f2="fills the left 45 percent of the frame", f3="about 15 centimeters from the lens", f4="phone held at arm's length at eye level",
        f5="her right thumb and index finger pinched together"),
3: dict(titulo="avatar segura o queixo da cliente, perfil", cena=SCENE, cara=True, selfie=False,
        prop="A woman in her fifties, a client, stands in profile at the right, cropped by the frame: her cheek and jaw look swollen and soft. Brandon's right hand holds the client's chin between two fingers.",
        posture="Brandon stands at the left in three-quarter profile, looking at the client's face while she speaks, her hand lifting the chin.",
        composition="The hand holding the chin and the client's swollen jaw fill the right 45 percent of the frame, about 30 centimeters from the lens, closer to the camera than Brandon's face, which sits in the left half about 70 centimeters away. Only these elements are in the frame.",
        camera=TRI, state="Start frame: Brandon looks at the client's face, lips parted mid-sentence, two fingers on the chin.",
        heroi="mão da avatar segurando o queixo da cliente, rosto da cliente de perfil com maxilar inchado", termos=["holds the client's chin", "swollen jaw"],
        quadro="mão e rosto da cliente ocupam 45% da direita", dist="~30 cm da lente", pose="avatar de três quartos olhando a cliente, dois dedos no queixo",
        lista="avatar, cliente de perfil cortada, parede do box",
        f2="fill the right 45 percent of the frame", f3="about 30 centimeters from the lens", f4="phone camera on a tripod at chest height",
        f5="her hand lifting the chin"),
4: dict(titulo="avatar vira para a lente com o queixo da cliente na mão", cena=SCENE, cara=True, selfie=False,
        prop="A woman in her fifties, a client, is cropped at the left edge: her swollen jaw rests on Brandon's two fingers.",
        posture="Brandon turns her face to the lens, her right hand still holding the client's chin.",
        composition="Brandon's face fills the right 55 percent of the frame, about 50 centimeters from the lens; the client's jaw and the hand holding it fill the left 35 percent, about 30 centimeters from the lens, closer than Brandon's face. Only these elements are in the frame.",
        camera=TRI, state=f"Start frame: Brandon looks into the lens, {BOCA}.",
        heroi="queixo e maxilar inchado da cliente na mão da avatar", termos=["swollen jaw", "holding the client's chin"],
        quadro="o rosto da avatar ocupa 55% da direita, o maxilar da cliente 35% da esquerda", dist="~30 cm da lente (maxilar), ~50 cm (rosto da avatar)",
        pose="avatar olha a lente com a mão no queixo da cliente", lista="avatar, cliente cortada, parede do box",
        f2="fills the right 55 percent of the frame", f3="about 30 centimeters from the lens", f4="phone camera on a tripod at chest height",
        f5="her right hand still holding the client's chin"),
5: dict(titulo="dedo da cliente com aliança presa, avatar aponta", cena=SCENE, cara=True, selfie=False,
        prop="At the lower left, a client's hand with visibly swollen fingers and a plain gold wedding band stuck at the base of the ring finger, the forearm in a white sleeve cropped by the frame.",
        posture="Brandon stands at the right smiling at the lens, her right index finger touching the ring finger.",
        composition="The client's hand with the ring fills the lower-left 30 percent of the frame, about 30 centimeters from the lens, closer to the camera than Brandon's face, which sits in the upper right about 70 centimeters away. Only these elements are in the frame.",
        camera=TRI, state=f"Start frame: Brandon smiles at the lens, {BOCA}.",
        heroi="mão de cliente com dedos inchados e aliança dourada presa na base do dedo", termos=["swollen fingers", "gold wedding band stuck"],
        quadro="a mão ocupa 30% do canto inferior esquerdo", dist="~30 cm da lente", pose="avatar sorrindo para a lente, indicador no dedo com a aliança",
        lista="mão da cliente, avatar, parede do box",
        f2="fills the lower-left 30 percent of the frame", f3="about 30 centimeters from the lens", f4="phone camera on a tripod at chest height",
        f5="her right index finger touching the ring finger"),
6: dict(titulo="palma aberta ao lado da mão com aliança", cena=SCENE, cara=True, selfie=False,
        prop="Brandon's left palm is open and facing up in the lower foreground; at the right edge a client's swollen hand with a gold wedding band rests beside it, the forearm in a navy sleeve cropped by the frame.",
        posture="Brandon leans toward the lens smiling, her left palm open and her right index finger lifted toward the ring.",
        composition="The open palm fills the lower-center 30 percent of the frame, about 25 centimeters from the lens, closer than Brandon's face, which sits in the upper half about 60 centimeters away. Only these elements are in the frame.",
        camera=TRI, state=f"Start frame: Brandon smiles at the lens, {BOCA}.",
        heroi="palma aberta da avatar ao lado da mão inchada com aliança", termos=["open palm", "swollen hand"],
        quadro="a palma ocupa 30% do centro inferior", dist="~25 cm da lente", pose="avatar inclinada para a lente, sorrindo, palma aberta",
        lista="palma, mão da cliente, avatar, parede do box",
        f2="fills the lower-center 30 percent of the frame", f3="about 25 centimeters from the lens", f4="phone camera on a tripod at chest height",
        f5="her left palm open"),
7: dict(titulo="close do rosto da avatar, olhar firme", cena=SCENE, cara=True, selfie=True,
        prop="Brandon's face is the whole subject, leaning toward the lens with a steady, serious look and lowered brows.",
        posture="Brandon leans in with her head tilted slightly down toward the lens, eyes locked on it.",
        composition="Her face fills 60 percent of the frame from chin to forehead, about 35 centimeters from the lens; the white block wall and the red neon sit behind her in sharp focus. Only these elements are in the frame.",
        camera=SELFIE, state=f"Start frame: Brandon looks into the lens, {BOCA}.",
        heroi="rosto da avatar colado na lente, sobrancelhas baixas, olhar firme", termos=["leaning toward the lens", "lowered brows"],
        quadro="o rosto ocupa 60% do quadro", dist="~35 cm da lente", pose="cabeça inclinada para a lente, olhos na lente",
        lista="rosto, parede de bloco, neon", f2="fills 60 percent of the frame", f3="about 35 centimeters from the lens",
        f4="phone held at arm's length at eye level", f5="eyes locked on it"),
8: dict(titulo="indicador apontado para a lente, rosto atrás", cena=SCENE, cara=True, selfie=True,
        prop="Brandon's right index finger points straight at the lens, very large in the foreground.",
        posture="Brandon leans toward the lens with a serious look, her right arm extended toward the camera.",
        composition="The raised index finger fills the lower-center 25 percent of the frame, about 20 centimeters from the lens, closer than her face, which fills 45 percent of the frame behind it about 40 centimeters away. Only these elements are in the frame.",
        camera=SELFIE, state=f"Start frame: Brandon looks into the lens, {BOCA}.",
        heroi="indicador da avatar apontado para a lente, enorme em primeiro plano", termos=["index finger points straight at the lens", "serious look"],
        quadro="o dedo ocupa 25% do centro inferior, o rosto 45%", dist="~20 cm da lente (dedo)", pose="inclinada para a lente com o braço estendido",
        lista="dedo, rosto, parede do box", f2="fills the lower-center 25 percent of the frame", f3="about 20 centimeters from the lens",
        f4="phone held at arm's length at eye level", f5="her right arm extended toward the camera"),
9: dict(titulo="avatar debruçada sobre a mesa com manequim, copo, saleiro e almofada", cena=SCENE_BANC, cara=True, selfie=False,
        prop="On a low light stone table in the lower foreground: a skin-toned mannequin head with closed eyes at the left, a clear glass of water in the middle, a small white salt shaker and a small white pillow at the right.",
        posture="Brandon leans over the table with both hands resting on its edge at the left, looking down at the mannequin head.",
        composition="The table with the objects fills the bottom 35 percent of the frame, about 30 centimeters from the lens, closer to the camera than Brandon's face; Brandon's head and chest sit in the upper half about 70 centimeters away. Only these elements are in the frame.",
        camera=TRI, state="Start frame: Brandon looks down at the mannequin head, lips parted mid-sentence.",
        heroi="cabeça de manequim cor de pele, copo d'água, saleiro branco e almofada branca sobre uma mesa baixa de pedra",
        termos=["skin-toned mannequin head", "small white salt shaker"],
        quadro="a mesa com os objetos ocupa 35% da base do quadro", dist="~30 cm da lente", pose="debruçada com as duas mãos na borda da mesa, olhando o manequim",
        lista="mesa, manequim, copo, saleiro, almofada, avatar", f2="fills the bottom 35 percent of the frame", f3="about 30 centimeters from the lens",
        f4="phone camera on a tripod at chest height", f5="leans over the table with both hands resting on its edge"),
10: dict(titulo="avatar se inclina para a lente e toca o manequim", cena=SCENE_BANC, cara=True, selfie=False,
        prop="On a low light stone table: a skin-toned mannequin head at the left, a clear glass of water in the middle and a white salt shaker at the right.",
        posture="Brandon leans toward the lens, her left hand resting on top of the mannequin head and her right hand open above the glass.",
        composition="The mannequin head, the glass and the shaker fill the bottom 40 percent of the frame, about 25 centimeters from the lens, closer than Brandon's face, which fills the upper half about 55 centimeters away. Only these elements are in the frame.",
        camera=TRI, state=f"Start frame: Brandon looks into the lens, {BOCA}.",
        heroi="manequim com a mão da avatar em cima, copo d'água e saleiro", termos=["skin-toned mannequin head", "white salt shaker"],
        quadro="os objetos ocupam 40% da base", dist="~25 cm da lente", pose="inclinada para a lente, mão esquerda na cabeça do manequim",
        lista="mesa, manequim, copo, saleiro, avatar", f2="fill the bottom 40 percent of the frame", f3="about 25 centimeters from the lens",
        f4="phone camera on a tripod at chest height", f5="her left hand resting on top of the mannequin head"),
11: dict(titulo="mesma mesa, avatar de olhos baixos falando", cena=SCENE_BANC, cara=True, selfie=False,
        prop="On a low light stone table in the lower foreground: a skin-toned mannequin head with closed eyes at the left, a clear glass of water in the middle, a small white salt shaker and a small white pillow at the right.",
        posture="Brandon leans over the table with both hands resting on its edge, her eyes lowered to the objects.",
        composition="The table with the objects fills the bottom 35 percent of the frame, about 30 centimeters from the lens, closer to the camera than Brandon's face; Brandon's head and chest sit in the upper half about 70 centimeters away. Only these elements are in the frame.",
        camera=TRI, state="Start frame: Brandon looks down at the objects, lips parted mid-sentence.",
        heroi="mesma mesa baixa: manequim cor de pele, copo d'água, saleiro e almofada", termos=["skin-toned mannequin head", "small white salt shaker"],
        quadro="a mesa com os objetos ocupa 35% da base", dist="~30 cm da lente", pose="debruçada, mãos na borda, olhos baixos",
        lista="mesa, manequim, copo, saleiro, almofada, avatar", f2="fills the bottom 35 percent of the frame", f3="about 30 centimeters from the lens",
        f4="phone camera on a tripod at chest height", f5="her eyes lowered to the objects"),
12: dict(titulo="selfie de perto, avatar aponta para a lente", cena=SCENE, cara=True, selfie=True,
        prop="Brandon's right index finger points toward the lens in the lower foreground.",
        posture="Brandon smiles like someone about to teach something, her head tilted slightly, her right arm extended toward the camera.",
        composition="Her face fills 55 percent of the frame, about 40 centimeters from the lens; the pointing finger fills the lower-right 15 percent, about 25 centimeters from the lens, closer than her face. Only these elements are in the frame.",
        camera=SELFIE, state=f"Start frame: Brandon looks into the lens, {BOCA}.",
        heroi="indicador da avatar apontando para a lente, rosto sorrindo atrás", termos=["right index finger points toward the lens", "about to teach"],
        quadro="o rosto ocupa 55%, o dedo 15% do canto inferior direito", dist="~25 cm da lente (dedo)", pose="sorrindo, cabeça levemente inclinada, braço estendido",
        lista="dedo, rosto, parede do box", f2="fills 55 percent of the frame", f3="about 25 centimeters from the lens",
        f4="phone held at arm's length at eye level", f5="her right arm extended toward the camera"),
13: dict(titulo="bancada: panela de vidro, colher com salsinha, limão", cena=SCENE_BANC, cara=True, selfie=False,
        prop="On the stone counter in the lower foreground: a clear glass pot of water on a single black induction hob, a half lemon at the right and a small bowl of fennel seeds beside it. Brandon holds a metal spoon of chopped fresh parsley above the pot.",
        posture="Brandon stands behind the counter smiling at the lens, her right hand holding the spoon over the pot.",
        composition="The glass pot fills the bottom 35 percent of the frame, its front edge about 30 centimeters from the lens, closer than Brandon's face, which sits in the upper half about 70 centimeters away. Only these elements are in the frame.",
        camera=TRI, state=f"Start frame: Brandon smiles at the lens, the spoon of parsley held above the pot, {BOCA}.",
        heroi="panela de vidro transparente com água sobre um fogareiro de indução preto, colher de metal com salsinha picada", termos=["clear glass pot of water", "chopped fresh parsley"],
        quadro="a panela ocupa 35% da base do quadro", dist="~30 cm da lente", pose="atrás da bancada, sorrindo, colher sobre a panela",
        lista="bancada, panela, fogareiro, limão, tigelinha de sementes, avatar", f2="fills the bottom 35 percent of the frame", f3="about 30 centimeters from the lens",
        f4="phone camera on a tripod at chest height", f5="her right hand holding the spoon over the pot"),
14: dict(titulo="macro: salsinha caindo na água da panela", cena=SCENE_BANC, cara=False, selfie=False,
        prop="A metal spoon tips chopped fresh parsley into the clear water of a clear glass pot on a single black induction hob; a small bowl of fennel seeds sits at the right. The hand holding the spoon is cropped by the top edge.",
        posture="Only Brandon's right hand and forearm are visible, the tattoo sleeve on her forearm, tipping the spoon.",
        composition="The glass pot fills the bottom 60 percent of the frame, its rim about 25 centimeters from the lens, very close; the spoon and the falling parsley are in the center. Only these elements are in the frame.",
        camera=MACRO, state="Start frame: the parsley is just starting to fall from the spoon into the water.",
        heroi="colher despejando salsinha picada na água de uma panela de vidro", termos=["tips chopped fresh parsley", "clear glass pot"],
        quadro="a panela ocupa 60% da base", dist="~25 cm da lente", pose="só a mão e o antebraço com a tatuagem",
        lista="panela, colher, salsinha, tigelinha de sementes, fogareiro", f2="fills the bottom 60 percent of the frame", f3="about 25 centimeters from the lens",
        f4="phone camera low over the counter at counter height", f5="Only Brandon's right hand and forearm are visible"),
15: dict(titulo="macro: meio limão sendo espremido na panela", cena=SCENE_BANC, cara=False, selfie=False,
        prop="A hand squeezes a half lemon over the clear glass pot of water with chopped parsley and a few fennel seeds floating in it; a few drops of juice fall into the water.",
        posture="Only Brandon's right hand and forearm are visible from the top right, the tattoo sleeve on her forearm, squeezing the lemon.",
        composition="The lemon half fills the upper-right 30 percent of the frame, about 25 centimeters from the lens, very close, over the pot that fills the bottom 50 percent. Only these elements are in the frame.",
        camera=MACRO, state="Start frame: the lemon is already squeezed, the first drops falling into the water.",
        heroi="meio limão espremido sobre a panela de vidro", termos=["squeezes a half lemon", "clear glass pot of water"],
        quadro="o limão ocupa 30% do canto superior direito, a panela 50% da base", dist="~25 cm da lente", pose="só a mão e o antebraço com a tatuagem",
        lista="panela, limão, salsinha, sementes", f2="fills the upper-right 30 percent of the frame", f3="about 25 centimeters from the lens",
        f4="phone camera low over the counter at counter height", f5="squeezing the lemon"),
16: dict(titulo="macro: a panela fervendo com limão e salsinha", cena=SCENE_BANC, cara=False, selfie=False,
        prop="A clear glass pot of water simmering on a single black induction hob: bubbles rising, a lemon slice and green parsley leaves swirling slowly, a little steam.",
        posture="No person is in frame.",
        composition="The pot fills 85 percent of the frame, its rim about 25 centimeters from the lens, very close. Only these elements are in the frame.",
        camera=MACRO, state="Start frame: the water is already simmering with small bubbles.",
        heroi="panela de vidro com água fervendo, fatia de limão e folhas de salsinha girando", termos=["simmering", "lemon slice"],
        quadro="a panela ocupa 85% do quadro", dist="~25 cm da lente", pose="sem pessoa em quadro", lista="panela, limão, salsinha, vapor",
        f2="fills 85 percent of the frame", f3="about 25 centimeters from the lens", f4="phone camera low over the counter at counter height",
        f5="No person is in frame"),
17: dict(titulo="caneca de vidro fumegante nas duas mãos", cena=SCENE_BANC, cara=True, selfie=False,
        prop="Brandon holds a clear glass mug of pale green-gold tea with a little steam rising from it, in both hands in the lower foreground.",
        posture="Brandon leans on the counter with both elbows, holding the mug, smiling at the lens.",
        composition="The mug fills the lower-center 25 percent of the frame, about 30 centimeters from the lens, closer than Brandon's face, which sits in the upper half about 60 centimeters away. Only these elements are in the frame.",
        camera=TRI, state=f"Start frame: Brandon smiles at the lens, {BOCA}.",
        heroi="caneca de vidro transparente com chá verde-dourado e vapor, nas duas mãos", termos=["clear glass mug", "pale green-gold tea"],
        quadro="a caneca ocupa 25% do centro inferior", dist="~30 cm da lente", pose="cotovelos na bancada, caneca nas duas mãos, sorrindo",
        lista="caneca, avatar, bancada", f2="fills the lower-center 25 percent of the frame", f3="about 30 centimeters from the lens",
        f4="phone camera on a tripod at chest height", f5="holding the mug"),
18: dict(titulo="avatar aponta o tubo em S com água azul", cena=SCENE_BANC, cara=True, selfie=False,
        prop="On the counter at the left of the frame: a clear acrylic tube bent in a large S on a small metal stand, filled with bright blue water that rests in its curves.",
        posture="Brandon leans on the counter with her left hand and points her right index finger at the upper bend of the tube, looking at the lens.",
        composition="The S-shaped tube fills the left 40 percent of the frame, about 30 centimeters from the lens, closer than Brandon's face, which sits at the right about 70 centimeters away. Only these elements are in the frame.",
        camera=TRI, state=f"Start frame: Brandon looks into the lens, {BOCA}.",
        heroi="tubo de acrílico transparente curvado em S num suporte de metal, cheio de água azul", termos=["acrylic tube bent in a large S", "bright blue water"],
        quadro="o tubo ocupa 40% da esquerda do quadro", dist="~30 cm da lente", pose="apoiada na bancada, indicador apontando a curva de cima",
        lista="tubo em S, suporte, avatar, bancada", f2="fills the left 40 percent of the frame", f3="about 30 centimeters from the lens",
        f4="phone camera on a tripod at chest height", f5="points her right index finger at the upper bend of the tube"),
19: dict(titulo="macro: dedo na curva do tubo onde a água azul está parada", cena=SCENE_BANC, cara=False, selfie=False,
        prop="A fingertip touches the upper bend of a clear acrylic tube bent in a large S, filled with bright blue water that rests still in the curve.",
        posture="Only Brandon's right hand and forearm are visible, the tattoo sleeve on her forearm.",
        composition="The tube fills 70 percent of the frame, about 25 centimeters from the lens, very close; the fingertip sits at its upper bend. Only these elements are in the frame.",
        camera=MACRO, state="Start frame: the water is still, the fingertip resting on the glass.",
        heroi="dedo tocando a curva do tubo em S com água azul parada", termos=["fingertip touches", "bright blue water"],
        quadro="o tubo ocupa 70% do quadro", dist="~25 cm da lente", pose="só a mão e o antebraço", lista="tubo, dedo",
        f2="fills 70 percent of the frame", f3="about 25 centimeters from the lens", f4="phone camera low over the counter at counter height",
        f5="Only Brandon's right hand and forearm are visible"),
20: dict(titulo="macro: tubo inclinado, água azul escorrendo para a bandeja", cena=SCENE_BANC, cara=False, selfie=False,
        prop="A hand tilts a long clear acrylic tube full of bright blue water so the water pours out of its open end into a stainless steel tray below.",
        posture="Only Brandon's right hand and forearm are visible from the right, the tattoo sleeve on her forearm.",
        composition="The tilted tube fills 70 percent of the frame, about 25 centimeters from the lens, very close, with the steel tray in the lower-left 20 percent. Only these elements are in the frame.",
        camera=MACRO, state="Start frame: the tube is tilted and the first of the blue water is leaving its open end.",
        heroi="tubo de acrílico inclinado despejando água azul numa bandeja de inox", termos=["tilts a long clear acrylic tube", "stainless steel tray"],
        quadro="o tubo ocupa 70% do quadro", dist="~25 cm da lente", pose="só a mão e o antebraço", lista="tubo, bandeja de inox",
        f2="fills 70 percent of the frame", f3="about 25 centimeters from the lens", f4="phone camera low over the counter at counter height",
        f5="Only Brandon's right hand and forearm are visible"),
21: dict(titulo="selfie sentada, sorriso largo e gesto leve", cena=SCENE, cara=True, selfie=True,
        prop="Brandon sits on the edge of the black training table, her right hand making a small rounding gesture beside her cheek.",
        posture="Brandon sits on the black table with her shoulders relaxed, smiling wide with a rested, glowing face.",
        composition="Her face fills 55 percent of the frame, about 40 centimeters from the lens; the hand sits at the lower left, about 30 centimeters from the lens, closer than her face. Only these elements are in the frame.",
        camera=SELFIE, state=f"Start frame: Brandon smiles at the lens, {BOCA}.",
        heroi="rosto descansado da avatar sorrindo, mão fazendo um gesto leve", termos=["rested, glowing face", "small rounding gesture"],
        quadro="o rosto ocupa 55% do quadro", dist="~40 cm da lente (rosto), ~30 cm (mão)", pose="sentada na mesa preta, ombros soltos, sorriso largo",
        lista="avatar, mão, parede do box", f2="fills 55 percent of the frame", f3="about 40 centimeters from the lens",
        f4="phone held at arm's length at eye level", f5="sits on the black table"),
22: dict(titulo="macro do peito: mãos em prece", cena=SCENE, cara=False, selfie=False,
        prop="Brandon's two hands are pressed together in prayer at her chest, over the white ribbed tank top and the thin gold chain with the small gold cross.",
        posture="Brandon stands facing the lens; her chin is cropped by the top edge of the frame.",
        composition="The pressed hands fill the lower-center 45 percent of the frame, about 25 centimeters from the lens, very close; only her collarbone, chain and top are visible behind them. Only these elements are in the frame.",
        camera=TRI, state="Start frame: the hands are already pressed together, the thumbs resting against the chest.",
        heroi="duas mãos em prece diante do peito, regata branca e corrente com cruz", termos=["pressed together in prayer", "small gold cross"],
        quadro="as mãos ocupam 45% do centro inferior", dist="~25 cm da lente", pose="de frente, queixo cortado pelo topo do quadro",
        lista="mãos, regata, corrente", f2="fill the lower-center 45 percent of the frame", f3="about 25 centimeters from the lens",
        f4="phone camera on a tripod at chest height", f5="her chin is cropped by the top edge of the frame"),
23: dict(titulo="selfie sentada, aponta para si mesma", cena=SCENE, cara=True, selfie=True,
        prop="Brandon's right index finger points at her own chest in the lower foreground.",
        posture="Brandon sits on the black table smiling at the lens, her right hand pointing at herself.",
        composition="Her face fills 50 percent of the frame, about 45 centimeters from the lens; the pointing hand fills the lower-left 20 percent, about 30 centimeters from the lens, closer than her face. Only these elements are in the frame.",
        camera=SELFIE, state=f"Start frame: Brandon smiles at the lens, {BOCA}.",
        heroi="mão da avatar apontando para o próprio peito, sorrindo", termos=["points at her own chest", "pointing at herself"],
        quadro="o rosto ocupa 50% do quadro, a mão 20% do canto inferior esquerdo", dist="~30 cm da lente (mão)", pose="sentada, sorrindo para a lente, apontando para si",
        lista="avatar, mão, parede do box", f2="fills 50 percent of the frame", f3="about 30 centimeters from the lens",
        f4="phone held at arm's length at eye level", f5="her right hand pointing at herself"),
24: dict(titulo="manequim com seta amarela e plaquinha THE CAUSE", cena=SCENE_BANC, cara=True, selfie=False, placa=True,
        prop="On the stone counter: a skin-toned mannequin head with closed eyes rests on a small white stand with a small black plaque in front reading THE CAUSE in white capital letters. Brandon holds a yellow cardboard arrow pointing at the mannequin head.",
        posture="Brandon leans on the counter beside the mannequin head, smiling at the lens, her right hand holding the arrow.",
        composition="The mannequin head, the arrow and the plaque fill the lower-right 40 percent of the frame, about 30 centimeters from the lens, closer than Brandon's face, which sits at the left about 70 centimeters away. Only these elements are in the frame.",
        camera=TRI, state=f"Start frame: Brandon smiles at the lens, {BOCA}.",
        heroi="cabeça de manequim com seta amarela de papelão apontada para ela e plaquinha preta THE CAUSE", termos=["skin-toned mannequin head", "yellow cardboard arrow"],
        quadro="manequim, seta e plaquinha ocupam 40% do canto inferior direito", dist="~30 cm da lente", pose="apoiada na bancada ao lado do manequim, sorrindo, seta na mão direita",
        lista="manequim, suporte, plaquinha, seta, avatar", f2="fill the lower-right 40 percent of the frame", f3="about 30 centimeters from the lens",
        f4="phone camera on a tripod at chest height", f5="her right hand holding the arrow"),
25: dict(titulo="CTA: avatar apoiada na bancada falando para a lente", cena=SCENE_BANC, cara=True, selfie=False,
        prop="Brandon rests both forearms on the light stone counter in the lower foreground, her hands relaxed and gesturing.",
        posture="Brandon leans on the counter and speaks straight to the lens, her expression warm and direct.",
        composition="Her face and shoulders fill 50 percent of the frame, about 60 centimeters from the lens; her forearms and hands on the counter fill the bottom 20 percent of the frame, about 35 centimeters from the lens, closer than her face. Only these elements are in the frame.",
        camera=TRI, state=f"Start frame: Brandon looks into the lens, {BOCA}.",
        heroi="avatar apoiada na bancada de pedra falando direto para a lente", termos=["rests both forearms", "light stone counter"],
        quadro="rosto e ombros ocupam 50% do quadro, antebraços 20% da base", dist="~35 cm da lente (antebraços)", pose="apoiada na bancada, mãos soltas gesticulando",
        lista="avatar, bancada, parede do box", f2="fill the bottom 20 percent of the frame", f3="about 35 centimeters from the lens",
        f4="phone camera on a tripod at chest height", f5="leans on the counter"),
}

# V: acao do clipe falado e do mudo (voz-over entra na edicao)
MODO_V = {t["t"]: t["modo"] for t in TAKES}
ACAO_MUDA = {
    14: "The hand tips the spoon and chopped parsley falls into the water of the glass pot.",
    15: "The hand squeezes the half lemon and juice drips into the pot.",
    16: "The water simmers, bubbles rise and the lemon slice and parsley leaves swirl slowly.",
    19: "The fingertip rests on the bend of the tube while the blue water sits still, then slides slowly along the curve.",
    20: "The hand tilts the tube and the blue water pours steadily into the steel tray.",
    22: "The hands stay pressed together in prayer at the chest, the chest rising gently with a slow breath.",
}
SEM_OLHAR = {3, 9, 11}   # fala olhando para outra coisa, nao para a camera


def kj(n):
    k = K[n]
    j = {
        "shot_id": f"K{n:02d}_t{n}_brandon",
        "format": "IMPORTANT: THIS IS PHONE FOOTAGE. Vertical 9:16.",
        "reference_use": "Use the attached image only for Brandon's exact identity, wardrobe and own setting. Do not copy its pose or framing.",
        "identity_main": ID, "wardrobe": WARD, "scene": k["cena"], "prop": k["prop"], "posture": k["posture"],
        "composition": k["composition"], "camera": k["camera"], "lighting": LUZ, "state": k["state"],
        "realism": REALISMO, "aspect_ratio": "9:16 vertical", "negative": NEG,
    }
    return j


def paragrafo(n):
    k = K[n]
    fecho = FECHO_PLACA if k.get("placa") else FECHO
    cam = "Shot with a " + k["camera"] + ", level."
    estado = k["state"].replace("Start frame: ", "")
    p = " ".join([
        "Match the attached image exactly: same woman, same outfit, same room.",
        ID, WARD, k["cena"], k["prop"], k["posture"], k["composition"], cam, estado, fecho])
    return p


def video(n):
    t = TAKES[n - 1]
    fala = t["en"]
    if t["modo"] == "B-ROLL VO":
        return f"(no speech) {ACAO_MUDA[n]}\n\nFixed camera. No music."
    cam = "Handheld selfie camera, slight natural shake." if K[n]["selfie"] else "Fixed camera."
    olhar = "" if n in SEM_OLHAR else ", looking at the camera"
    suj = "The person in the image"
    if n <= 6:
        suj = "The person in the image wearing the white tank top"
    return f'{suj} speaks in American English{olhar}: "{fala}"\n\n{cam} Natural lip sync, no music.'


def principal():
    N = [t["t"] for t in TAKES]
    for n in N:
        assert len(paragrafo(n)) <= 1900, (n, len(paragrafo(n)))
    # PROMPTS_PRODUCAO.md (fonte interna)
    L = ["# Brandon | FitWell Growth inchaço da manhã | Pacote de Prompts", "",
         "Vídeo modelo: `input/modelo_watch` (84,1 s, 25 cenas)", "", f"Âncora: `{ANCORA}`", "",
         "Funil: growth. CTA = link da legenda + follow. Rodada de validação, gancho fiel ao modelo. Sem produto em quadro.", "",
         "## Índice de geração", "", "| Take | Keyframe | Anexar | Ação |", "|---|---|---|---|"]
    for n in N:
        L.append(f"| T{n} | K{n:02d} | ÂNCORA BRANDON | GERAR DO ZERO |")
    L += ["", "Todo K é GERAR DO ZERO: o prompt é autossuficiente. Um K = um V pelo número.", "",
          "## Trava de identidade e continuidade", "", f"- Identidade: {ID}", f"- Roupa: {WARD}",
          f"- Cenário (fixo da conta): {SCENE}", f"- Luz: {LUZ}", "- Voz: a do V (inglês americano), sem descrição de timbre no prompt.", "",
          "## Trava do prop herói", "",
          "- T1 a T8: a segunda pessoa (cliente) entra só cortada pelo quadro; nunca de corpo inteiro.",
          "- T9 a T11 e T24: cabeça de manequim cor de pele, sem rótulo.",
          "- T13 a T16: panela de vidro, salsinha, sementes de erva-doce, limão, sem embalagem.",
          "- T18 a T20: tubo de acrílico transparente curvado em S com água azul.", "",
          "## Trava da 2ª pessoa (REF-A)", "",
          "- A cliente de T1 a T6 é descrita por escrito em cada K, cortada pelo quadro. Sem REF-A.", "",
          "## Prompts de imagem", ""]
    for n in N:
        L += [f"## K{n:02d} · T{n} · GERAR DO ZERO · ÂNCORA BRANDON", "",
              "> ### 📎 ANEXAR: **1 IMAGEM**", f"> **1️⃣ ÂNCORA BRANDON** `{ANCORA}`", ">", "> ### 🆕 GERAR DO ZERO", "",
              f"Cena: {K[n]['titulo']}.", "", "```json", json.dumps(kj(n), ensure_ascii=False, indent=2), "```", ""]
    L += ["## Bloco global de vídeo", "", "```text",
          'The person in the image speaks in American English, looking at the camera: "[FALA EXATA DO ROTEIRO]"', "",
          "Fixed camera. Natural lip sync, no music.", "```", "", "# Prompts de vídeo", ""]
    for n in N:
        L += [f"### V{n:02d} · T{n} · usa K{n:02d}", "", "```text", video(n), "```", ""]
    L += ["## Mapa de âncoras", "", "| Keyframe | Referências a anexar | Modelo |", "|---|---|---|",
          "| K01 a K25 | ÂNCORA BRANDON | Nano Banana 2.1, 9:16, 4 imagens |", "",
          "## Montagem no CapCut", "", *montagem(), "",
          "## Gates de qualidade", "",
          "1. Fala de cada V igual ao ROTEIRO, palavra por palavra.",
          "2. Um take por cena do modelo; cenas curtas marcadas; nenhum take acima de 29 palavras.",
          "3. Bandeira dos EUA no campo scene de todo K.", "4. Zero travessão.",
          "5. Growth: sem keyword de venda, sem produto, sem preço; CTA = link da legenda + follow.",
          "6. Nenhuma embalagem com marca ou texto; a única escrita em quadro é a plaquinha THE CAUSE (K24).",
          "7. Negative sem termo sensível.", "8. GATE_VISUAL Partes 1 a 3 em todo K: herói colado na lente com medida, luz neutra, sem tom quente, trecho de realismo.",
          "9. Um K = um V; os reveals (salsinha caindo, fervura, água azul escorrendo) acontecem dentro do clipe.",
          "10. FICHA_FRAMES.md com placar de cada K antes do envio.", ""]
    (AQUI / "PROMPTS_PRODUCAO.md").write_text("\n".join(L) + "\n", encoding="utf-8")

    # FICHA_FRAMES.md
    F = ["# FICHA DOS FRAMES · fitywell_growth_v1", "",
         "Escrita olhando cada frame do modelo em `input/frames_modelo/` (GATE_VISUAL.md Parte 6). O modelo manda no conteúdo; "
         "o gate manda no acabamento; a proximidade do herói é a mais perto entre os dois.", ""]
    for n in N:
        k = K[n]
        j = json.dumps(kj(n), ensure_ascii=False)
        face = k["cara"]
        ev = {"F2": k["f2"], "F3": k["f3"], "F4": k["f4"], "F5": k["f5"], "F6": "Only these elements are in the frame."}
        for key, v in ev.items():
            assert v in json.dumps(kj(n), ensure_ascii=False).replace('\\"', '"') or v in "".join(kj(n).values()), (n, key, v)
        for tr in k["termos"]:
            assert tr in "".join(kj(n).values()), (n, tr)
        F += [f"## K{n:02d}", f"Frame: `input/frames_modelo/K{n:02d}_modelo.png`", f"Take: T{n}",
              f"Herói: {k['heroi']}.", "Termos de forma: " + " · ".join(f'"{x}"' for x in k["termos"]),
              f"Quadro: {k['quadro']}.", f"Distância da lente: {k['dist']}.",
              f"Câmera: {'selfie de celular na altura dos olhos, lente 26 mm' if k['selfie'] else 'celular na altura do peito ou do balcão, lente 26 mm'}, como no modelo.",
              f"Pose: {k['pose']}.", f"Lista fechada: {k['lista']}.",
              "Frame 0: ação já começada, boca no meio da frase." if face else "Frame 0: ação já começada, sem rosto em quadro.",
              "Desvio (acabamento ou avatar fixo): avatar, roupa e cenário-base da conta no lugar do homem e da piscina ou cozinha do modelo; luz neutra do gate.",
              "", "| Item | Status | Evidência |", "|---|---|---|",
              f'| F1 forma do herói | OK | "{k["termos"][0]}" |', f'| F2 quanto do quadro | OK | "{k["f2"]}" |',
              f'| F3 distância da lente | OK | "{k["f3"]}" |', f'| F4 câmera | OK | "{k["f4"]}" |',
              f'| F5 pose do avatar | OK | "{k["f5"]}" |', '| F6 lista fechada | OK | "Only these elements are in the frame." |',
              '| G1 luz neutra | OK | "soft even light on the face with no harsh shadows" |',
              "| G2 céu ou janela | N/A | o box da avatar não tem janela nem céu em quadro |",
              '| G3 foco | OK | "everything in sharp focus" |', '| G4 realismo | OK | "Real skin with visible pores" |',
              '| G5 sem tom quente | OK | "no warm orange color cast" |', '| G6 sem texto | OK | "no captions" |',
              '| G7 bandeira | OK | "small American flag" |',
              ('| G8 boca no K de fala | OK | "caught mid-sentence" |' if face and "caught mid-sentence" in k["state"] else
               "| G8 boca no K de fala | N/A | " + ("a avatar olha para os objetos, boca entreaberta no meio da frase" if face else "sem rosto em quadro, a voz entra em off") + " |"), ""]
    (AQUI / "FICHA_FRAMES.md").write_text("\n".join(F), encoding="utf-8")

    # ENTREGA_BRANDON.md
    E = entrega(N)
    (AQUI / "ENTREGA_BRANDON.md").write_text(E, encoding="utf-8")
    print("ok: %d K, %d V" % (len(N), len(N)))


def montagem():
    return [
        "1. Clipes numerados na ordem: V01 a V25.",
        "2. Cortar cada clipe no tempo da cena do modelo: " + "; ".join(f"V{t['t']:02d} {t['ini']:.1f} a {t['fim']:.1f} s" for t in TAKES) + ".",
        "3. Zero tempo morto: todo clipe falado começa já falando. Isolate Voice / Keep Vocal no áudio.",
        "4. Nos takes de mão sem rosto (T14, T15, T16, T19, T20, T22) a fala entra como voz-over: cortar a voz do clipe do take anterior ou gravar a linha por TTS e alinhar no tempo da cena.",
        "5. Nos takes que a frase atravessa o corte (T7 a T8, T12 a T13, T17 a T20, T21 a T22, T23 a T24) a voz é a mesma ao longo dos clipes: alinhar no CapCut sem pausa entre eles.",
        "6. Legenda de 2 a 3 palavras por vez, caixa alta, fonte bold branca com contorno preto e a palavra falada em verde, no meio do quadro, do começo ao fim, igual ao modelo.",
        "7. Música só depois do gancho (T9 em diante), baixa, fora da biblioteca do TikTok.",
        "8. Rótulo pequeno `AI-generated` num canto do vídeo.",
    ]


def entrega(N):
    L = ["# ENTREGA | Brandon | FitWell Growth inchaço da manhã", "", "flow_seguro: v1", "",
         "Produção `fitywell_growth_v1` · Ângulo 2 · GROWTH · rodada de VALIDAÇÃO · perfil CLÁSSICO", "",
         "Instruções do agente do Flow: `AGENTE_FLOW.md` desta produção (colado no chat).", "",
         "Checklist de envio: 27/27 aprovados (N/A: A1 a A4, A10 a A12 fiéis ao modelo na rodada de validação e sem arquivo de ganchos; B2 sem frame do modelo anexado, padrão de 2026-10-06; C1 cenas curtas do modelo, C2, C4 e C8 superados pelo V mínimo do Flow de 2026-10-09, C6 e C7 sem cena atuada nem motion control; E4 repetição de \"swollen\" é a estrutura do modelo)", "",
         "Ficha: 25/25 K, placar 14/14 cada (N/A com motivo: G2 em todos, o box não tem janela nem céu; G8 nos takes sem boca em quadro ou com olhar nos objetos) (`FICHA_FRAMES.md`, GATE_VISUAL Parte 6)", "",
         "## Qual vídeo é este", "",
         "**FitWell growth: inchaço da manhã com a panela de salsinha, erva-doce e limão**", "",
         "**O que acontece:** a Brandon mostra os sintomas de retenção de manhã (olho inchado, rosto inchado, aliança que não passa) em uma cliente, diz que não é a idade nem dormir mal e que creme não resolve, ensina a receita na panela (salsinha, erva-doce, limão, dez minutos), explica com um tubo em S cheio de água azul como a água fica presa no rosto depois de oito horas deitada, promete o rosto descansado e fecha mandando para o link da legenda e pedindo follow.", "",
         '**Gancho:** a fala de abertura é "If you wake up with eyes swollen like this," com o olho inchado de uma cliente colado na lente e a Brandon apontando o dedo para a câmera.', "",
         "## Anexos e mapa", "",
         f"- **Imagem (K):** anexar SÓ a âncora da Brandon (`{ANCORA}`) e colar o prompt. 4 variações, 9:16.",
         "- **Vídeo (V):** anexar SÓ a imagem escolhida daquele K e colar o prompt. 1 variação, 9:16.", "",
         "```text", "MAPA K/V", *[f"V{n:02d}: K{n:02d}" for n in N], "```", "",
         "## 1. PROMPTS DE IMAGEM (um bloco por K)", ""]
    for n in N:
        L += [f"### K{n:02d} · T{n}, {K[n]['titulo']} · anexar SÓ a ÂNCORA", "", f"Cena: {K[n]['titulo']}.", "",
              "```text", f"K{n:02d}", paragrafo(n), "```", ""]
    L += ["## 2. PROMPTS DE VÍDEO (um bloco por V)", ""]
    for n in N:
        t = TAKES[n - 1]
        L += [f"### V{n:02d} · T{n} · anexar SÓ a imagem escolhida do K{n:02d}", "",
              f"Cena: T{n} · {t['modo']}. {K[n]['titulo'][0].upper() + K[n]['titulo'][1:]}. Diz: {t['pt']}", "",
              "```text", f"V{n:02d}", video(n), "```", ""]
    L += ["## 3. Montagem no CapCut", "", *montagem(), "",
          "## 4. Transcrição final por take", "", "| Take | English | Português |", "|---|---|---|"]
    for t in TAKES:
        L.append(f"| T{t['t']} | {t['en']} | {t['pt']} |")
    L += ["", "## 5. Roteiro final em inglês", ""]
    for i, t in enumerate(TAKES, 1):
        L.append(f"{i}. {t['en']}")
    L += ["", " ".join(t["en"] for t in TAKES), ""]
    return "\n".join(L)


if __name__ == "__main__":
    principal()
