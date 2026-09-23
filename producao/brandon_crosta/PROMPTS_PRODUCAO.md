# holistic.brandon | Ângulo 4 (Body Hacks for Men 40+) | Pacote de Prompts

Vídeo modelo: `holistic.brandon.mp4` (51,7s)

Âncora de identidade: `C:\Users\luigi\Desktop\AVATARES NON-SHOP\holistic.brandon .png`
(atenção ao espaço antes da extensão, o nome do arquivo é esse mesmo)

Funil: comment `yes` -> DM -> landing `bodyhacksformen.netlify.app` -> checkout Hotmart embutido

> **Não existe 2ª pessoa neste vídeo.** O modelo é solo do começo ao fim, então não se inventa uma
> (`erros-recorrentes` falha #2). Por isso não há `REF-A` aqui, e sim três REF de prop.

---

## Índice de geração

| Take | Keyframe | Ação de geração |
|---|---|---|
| ref | REF-PROP | GERAR DO ZERO. O modelo encrustado, isolado, sem cenário. **Aprovar ANTES de tudo.** |
| ref | REF-VASO | GERAR DO ZERO. O mesmo modelo já limpo, isolado. Contingência do reveal. |
| ref | REF-LIVRO | GERAR DO ZERO. O livro físico, isolado, sem cenário. |
| T1 | K01 | GERAR DO ZERO (ÂNCORA BRANDON + REF-PROP). Frame herói, gerar no Pro com variações. |
| T2 | K02 | EDITAR do K01 (muda só: o modelo passa a estar submerso) |
| T3, T4 | K03 | GERAR DO ZERO (ÂNCORA BRANDON + REF-PROP). Câmera na linha d'água. |
| T5 | K04 | GERAR DO ZERO (ÂNCORA BRANDON) |
| T6 | K05 | GERAR DO ZERO (ÂNCORA BRANDON) |
| T7 | K06 | EDITAR do K05 (muda só: colher de sal rosa no lugar da colher de mel) |
| T8 | K07 | EDITAR do K05 (muda só: pote tampado, as duas mãos livres) |
| T9, T10, T11 | K08 | GERAR DO ZERO (ÂNCORA BRANDON) |
| T12, T13, T14 | K09 | EDITAR do K08 (muda só: pote pousado, câmera um passo mais perto) |
| T15, T16 | K10 | EDITAR do K08 (muda só o gesto de mão) |
| T17 | K11 | GERAR DO ZERO (ÂNCORA BRANDON + REF-LIVRO) |
| T18 | K12 | EDITAR do K11 (o take mais fechado do vídeo inteiro) |

Total: 3 referências + 12 keyframes para 18 takes.

**Estágios sempre a partir do original.** O K06 e o K07 saem do K05, nunca um do outro. O K09 e o K10 saem do K08, nunca um do outro.

---

## Trava de identidade e continuidade

Aplicar em toda imagem e todo clipe. Escrita aqui uma vez, não repetida dentro de cada JSON.

- Preservar exatamente o rosto da Brandon: mulher negra mestiça americana, atlética, pele média clara com sardas suaves, olhos castanhos.
- **Cornrows trançadas para trás com pontas trançadas soltas caindo na frente dos ombros e miçangas de madeira e âmbar nas pontas.**
- Manga de tatuagem floral de linha fina cobrindo o braço do lado esquerdo do quadro. Pequena tatuagem de folha na clavícula e pequena tatuagem escrita no antebraço do lado direito do quadro.
- Regata branca canelada e shorts de treino pretos. **Corrente fina de OURO com pingente de cruz de OURO. Nunca prata.**
- Mesma box de treino em todos os planos, e **no máximo três âncoras de fundo por quadro**: parede de bloco de concreto cinza claro, neon vermelho `TRAIN PRAY REPEAT`, **bandeira vintage dos EUA**. O quadro branco e a estante de potes entram só quando a bandeira não couber, nunca os três juntos.
- **A sinalização da parede é canônica e continua existindo.** O que não pode aparecer é legenda ou palavra sobreposta na imagem.
- Luz natural difusa de dia nublado entrando pelo portão do galpão. O vermelho do neon fica **confinado à parede**, nunca banha a pele.
- Zero blur, tudo em foco nítido incluindo parede e prateleira. Cara de vídeo de iPhone, nunca polimento de IA.

---

## Trava do prop herói (usar em REF-PROP, K01, K02 e K03)

O herói do vídeo inteiro. **Descrito por FORMA, COR e MATERIAL, nunca pelo nome do que ele representa.**
O trabalho anatômico é feito pela fala e pela legenda, não pelo objeto, que é o padrão registrado do nicho.

```text
A classroom-style anatomical teaching model of a vascular bundle, molded in soft matte silicone. Its body is one elongated pale tuber form, about thirty centimeters long, thicker at the top and tapering slightly, with two rounded bulbs joined at the base. Branching cords in deep red and muted blue run along the length of the pale form, and there is a soft rounded dusty-rose cap at the top end. The entire object is buried under a thick dried crust in dusty beige and pale grey, cracked on the surface like dried clay, so the red and blue cords underneath are almost completely hidden. It looks like a calm educational teaching aid from a health classroom. The shape, size, colors and crust must stay identical in every shot.
```

**REF-VASO é o mesmo objeto sem a crosta**, para o caso do reveal do V04 não sair no primeiro corte.
Se ele não sair, o protocolo é o passo 3 de `restricoes-protocolo`: gerar dois clipes limpos e juntar
no corte, nunca insistir no mesmo prompt.

## Trava do prop de produto (usar em REF-LIVRO, K11 e K12)

```text
A physical hardcover book, about twenty centimeters tall, matte dark navy cover with a plain cream-colored spine and clean cream lettering on the front reading BODY HACKS FOR MEN. The cover has no illustration and no photograph, only the lettering. The edges of the pages are visible and slightly worn, like a book that has been opened many times. It is an ordinary printed book, not a device and not a screen.
```

> ⚠️ **O livro é PROP, a fala nunca promete objeto físico.** O produto é digital com entrega
> instantânea. Nenhum take diz que ela envia um livro impresso.

## Trava da 2ª pessoa

**Não se aplica.** O vídeo modelo é solo do começo ao fim e não se inventa figurante que o original
não tem. Todos os prompts levam `no second person` no negative.

---

# Prompts de imagem

## REF-PROP · GERAR DO ZERO · SEM REFERÊNCIA

o modelo encrustado sozinho sobre fundo neutro
> *Gerar e aprovar ANTES de qualquer keyframe. É o prop de maior risco do pacote.*

```json
{
  "shot_id": "REF_PROP_crusted",
  "reference_use": "No reference image. Generate the object alone.",
  "identity_main": "No people in frame. Product-style reference photo of a single object on a plain light grey seamless surface.",
  "prop": "A classroom-style anatomical teaching model of a vascular bundle, molded in soft matte silicone. Its body is one elongated pale tuber form, about thirty centimeters long, thicker at the top and tapering slightly, with two rounded bulbs joined at the base. Branching cords in deep red and muted blue run along the length of the pale form, and there is a soft rounded dusty-rose cap at the top end. The entire object is buried under a thick dried crust in dusty beige and pale grey, cracked on the surface like dried clay, so the red and blue cords underneath are almost completely hidden.",
  "scene": "Plain light grey seamless studio-less surface, nothing else in frame.",
  "composition": "The object lies at a slight diagonal and fills almost the whole frame. Nothing else is visible.",
  "camera": "straight-on, close, object centered",
  "state": "Start frame: the object at rest, fully crusted, dry.",
  "lighting": "Flat neutral daylight, soft even shadows.",
  "realism": "UGC realism, real matte silicone texture, visible crust granularity and hairline cracks, realistic shadows and reflections, iPhone-footage look, phone camera look not professional photography, no AI polish, no blur anywhere, everything in sharp focus.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no people, no hands, no studio, no plastic look, no supernatural lighting, no blur, no artificial lighting, no warm orange color cast, no yellow tint, no golden glow"
}
```

## REF-VASO · GERAR DO ZERO · SEM REFERÊNCIA

o mesmo modelo já limpo, contingência do reveal
> *Só é usado se o V04 não entregar o reveal dentro do clipe.*

```json
{
  "shot_id": "REF_VASO_clean",
  "reference_use": "No reference image. Generate the object alone.",
  "identity_main": "No people in frame. Product-style reference photo of a single object on a plain light grey seamless surface.",
  "prop": "A classroom-style anatomical teaching model of a vascular bundle, molded in soft matte silicone. Its body is one elongated pale tuber form, about thirty centimeters long, thicker at the top and tapering slightly, with two rounded bulbs joined at the base. Branching cords in deep red and muted blue run clearly along the length of the pale form, fully visible and clean, and there is a soft rounded dusty-rose cap at the top end. The surface is clean matte silicone with no crust on it at all.",
  "scene": "Plain light grey seamless surface, nothing else in frame.",
  "composition": "The object lies at a slight diagonal and fills almost the whole frame, in the same position and angle as the crusted reference.",
  "camera": "straight-on, close, object centered",
  "state": "Start frame: the object at rest, clean, dry.",
  "lighting": "Flat neutral daylight, soft even shadows.",
  "realism": "UGC realism, real matte silicone texture, realistic shadows and reflections, iPhone-footage look, phone camera look not professional photography, no AI polish, no blur anywhere, everything in sharp focus.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no people, no hands, no studio, no plastic look, no supernatural lighting, no blur, no artificial lighting, no warm orange color cast, no yellow tint, no golden glow"
}
```

## REF-LIVRO · GERAR DO ZERO · SEM REFERÊNCIA

o livro físico sozinho sobre fundo neutro

```json
{
  "shot_id": "REF_LIVRO",
  "reference_use": "No reference image. Generate the object alone.",
  "identity_main": "No people in frame. Product-style reference photo of a single book on a plain light grey seamless surface.",
  "prop": "A physical hardcover book, about twenty centimeters tall, matte dark navy cover with a plain cream-colored spine and clean cream lettering on the front reading BODY HACKS FOR MEN. The cover has no illustration and no photograph, only the lettering. The edges of the pages are visible and slightly worn, like a book that has been opened many times. It is an ordinary printed book, not a device and not a screen.",
  "scene": "Plain light grey seamless surface, nothing else in frame.",
  "composition": "The book stands upright, front cover facing the camera, filling most of the frame.",
  "camera": "straight-on, close, book centered",
  "state": "Start frame: the book standing still, closed.",
  "lighting": "Flat neutral daylight, soft even shadows.",
  "realism": "UGC realism, real paper and cloth texture, slightly worn page edges, realistic shadows, iPhone-footage look, phone camera look not professional photography, no AI polish, no blur anywhere, everything in sharp focus.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image beyond the printed cover title, no people, no hands, no studio, no screen, no tablet, no phone, no blur, no artificial lighting, no warm orange color cast, no yellow tint, no golden glow"
}
```

## K01 · T1 · HOOK · GERAR DO ZERO · ÂNCORA BRANDON + REF-PROP

Brandon ergue o modelo encrustado na vertical com as duas mãos, a bandeja de vinagre colada na lente embaixo
> *Gerar no Nano Banana Pro, com várias variações. É o frame que para o scroll.*

```json
{
  "shot_id": "K01_hook_crusted_up",
  "reference_use": "Use the first attached image ONLY for Brandon's face, identity, hair, tattoos, wardrobe and the gym scene. Use the second attached image ONLY for the exact shape, colors and crust of the object she is holding. Do NOT copy the pose or framing of either reference.",
  "identity_main": "The EXACT woman from the first reference image (Brandon): mixed-race Black American woman, light-medium skin with soft freckles, brown eyes, cornrows braided back with loose braided ends falling in front of the shoulders and wooden and amber beads on the tips, fine-line floral tattoo sleeve on the arm on the left side of frame, small leaf tattoo on the collarbone.",
  "wardrobe": "White ribbed tank top, black training shorts, thin GOLD chain with a GOLD cross pendant.",
  "prop": "The EXACT object from the second reference image: a classroom-style anatomical teaching model of a vascular bundle in soft matte silicone, one elongated pale tuber form about thirty centimeters long with two rounded bulbs joined at the base, deep red and muted blue branching cords running along it, a soft rounded dusty-rose cap at the top end, the whole object buried under a thick dried crust in dusty beige and pale grey, cracked on the surface like dried clay.",
  "prop_secondary": "A wide clear rectangular glass tray sits on the wooden counter in the lower foreground, filled with amber apple cider vinegar to about two thirds. The liquid is still.",
  "scene": "SAME concrete-block gym as the reference image: light gray cinderblock wall, red neon sign reading TRAIN PRAY REPEAT on the wall, and a small vintage American flag pinned flat on the wall, discreet but clearly visible and in sharp focus. Nothing else on the wall.",
  "posture": "Brandon stands upright behind the counter facing the camera, holding the crusted object vertically with both hands in front of her chest, the base of it just above the surface of the liquid.",
  "composition": "VERY CLOSE, almost close-up. The glass tray of amber liquid sits in the lower foreground closer to the lens than anything else, and the crusted object stands vertically above it filling the central third of the frame from bottom to top. The object is unmistakably the hero. Brandon's face is visible in the upper third, cropped at the top of her head. Nothing else competes.",
  "camera": "chest level, straight-on, camera pushed in close to the object",
  "state": "Start frame: Brandon holds the crusted object steady above the tray and looks directly into the lens, about to speak.",
  "lighting": "Soft neutral overcast daylight coming through the open gym door. The red neon glow stays confined to the wall behind her and does not fall on her skin.",
  "realism": "UGC realism, real skin texture with visible pores, individual hair strands, subtle wrinkles, realistic shadows and reflections, iPhone-footage look, phone camera look not professional photography, no AI polish, no beauty smoothing, no blur anywhere, everything in sharp focus including background wall and signage.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no studio, no plastic skin, no extra fingers, no supernatural lighting, no blur, no artificial lighting, no warm orange color cast, no yellow tint, no golden glow, no silver jewelry, no second person"
}
```

## K02 · T2 · HOOK · EDITAR do K01

o mesmo quadro, mas o modelo agora está deitado dentro do vinagre e as mãos dela seguram ele embaixo
> *Anexar: K01 aprovado.*

```json
{
  "task": "edit the attached image, keep everything identical except the changes listed",
  "keep_identical": "Keep Brandon exactly the same: same face, same hair and beads, same tattoos, same white tank top, same gold cross. Keep the SAME crusted object with the same shape, size, crust and colors. Keep the SAME background exactly: cinderblock wall, red neon sign, American flag on the wall, same lighting, same camera height and angle.",
  "change_1": "The crusted object is now lying horizontally fully submerged inside the glass tray, under the amber liquid, instead of being held upright above it.",
  "change_2": "Both of Brandon's hands are now down inside the tray, holding the object under the surface, her forearms wet to the wrist. She is looking down at the tray and then up toward the lens.",
  "realism": "UGC realism, real skin texture with visible pores, iPhone-footage look, no AI polish, no beauty smoothing, no blur anywhere. Do not make her skin darker, yellowish or orangish. Do not make the colors more saturated.",
  "negative": "do not change the face, do not change identity, do not change the background, do not change the object, do not change the camera angle, no captions, no subtitles, no words overlaid on the image, no plastic skin, no extra fingers, no silver jewelry, no second person, no blur"
}
```

## K03 · T3 e T4 · HOOK e REVEAL · GERAR DO ZERO · ÂNCORA BRANDON + REF-PROP

câmera baixa na linha d'água, o modelo em pé saindo do vinagre, crosta ainda cobrindo tudo
> *Uma imagem só para os dois takes: o T3 fala e o T4 é a quebra, que é reveal contínuo e acontece no vídeo.*

```json
{
  "shot_id": "K03_hook_waterline",
  "reference_use": "Use the first attached image ONLY for Brandon's face, identity, hair, tattoos, wardrobe and the gym scene. Use the second attached image ONLY for the exact shape, colors and crust of the object. Do NOT copy the pose or framing of either reference.",
  "identity_main": "The EXACT woman from the first reference image (Brandon): mixed-race Black American woman, light-medium skin with soft freckles, brown eyes, cornrows braided back with loose braided ends falling in front of the shoulders and wooden and amber beads on the tips, fine-line floral tattoo sleeve on the arm on the left side of frame.",
  "wardrobe": "White ribbed tank top, black training shorts, thin GOLD chain with a GOLD cross pendant.",
  "prop": "The EXACT object from the second reference image, still fully covered by the thick dried crust cracked like dried clay, standing upright with its two rounded bulbs resting at the waterline.",
  "prop_secondary": "The wide clear rectangular glass tray of amber apple cider vinegar, seen almost edge-on from very close, filling the bottom of the frame. A few small pale flakes float on the surface.",
  "scene": "SAME concrete-block gym as the reference image: light gray cinderblock wall and a small vintage American flag pinned flat on the wall behind her, discreet but clearly visible and in sharp focus. Only a corner of the red neon is in frame.",
  "posture": "Brandon stands behind the counter, both hands loosely around the lower part of the object, holding it upright with its base in the liquid.",
  "composition": "The camera is very low, almost level with the surface of the liquid. The object stands vertically and fills the lower two thirds of the frame, closer to the lens than anything else. Brandon's face is small in the upper third, cropped at the top of her head. Tighter than the previous shot.",
  "camera": "very low, almost at the waterline, looking slightly up along the object",
  "state": "Start frame: the object standing upright and still fully crusted, Brandon's hands around its lower half, looking into the lens.",
  "lighting": "Soft neutral overcast daylight coming through the open gym door. The red neon glow stays confined to the wall and does not fall on her skin.",
  "realism": "UGC realism, real skin texture with visible pores, individual hair strands, realistic shadows and reflections on the liquid surface, iPhone-footage look, phone camera look not professional photography, no AI polish, no beauty smoothing, no blur anywhere, everything in sharp focus including the background wall.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no studio, no plastic skin, no extra fingers, no supernatural lighting, no blur, no artificial lighting, no warm orange color cast, no yellow tint, no golden glow, no silver jewelry, no second person"
}
```

## K04 · T5 · ACESSO · GERAR DO ZERO · ÂNCORA BRANDON

os quatro itens enfileirados na bancada, sacola de compra atrás, ela apontando para eles

```json
{
  "shot_id": "K04_tableau",
  "reference_use": "Use the attached image ONLY for Brandon's face, identity, hair, tattoos, wardrobe and the gym scene. Do NOT copy its pose or framing.",
  "identity_main": "The EXACT woman from the reference image (Brandon): mixed-race Black American woman, light-medium skin with soft freckles, brown eyes, cornrows braided back with loose braided ends falling in front of the shoulders and wooden and amber beads on the tips, fine-line floral tattoo sleeve on the arm on the left side of frame.",
  "wardrobe": "White ribbed tank top, black training shorts, thin GOLD chain with a GOLD cross pendant.",
  "prop": "Four items stand in a row across the wooden counter in the lower foreground, close to the lens: a tall amber glass bottle of apple cider vinegar, a net bag of yellow lemons, a single head of white garlic, a squat glass jar of honey, and a small glass grinder of pink salt. A plain black canvas shopping bag sits behind them.",
  "scene": "SAME concrete-block gym as the reference image: light gray cinderblock wall and a small vintage American flag pinned flat on the wall behind her, discreet but clearly visible and in sharp focus. A corner of the red neon is in frame.",
  "posture": "Brandon stands upright behind the counter, her right hand lowered toward the row of items with the palm open, presenting them.",
  "composition": "Close. The row of items sits in the lower foreground closer to the lens than her face and runs across the bottom third of the frame. Brandon is visible from the chest up above them, her head cropped at the top edge. Nothing else in the room competes.",
  "camera": "chest level, straight-on, slightly high toward the row of items",
  "state": "Start frame: her hand just settling open above the items, looking into the lens.",
  "lighting": "Soft neutral overcast daylight coming through the open gym door. The red neon glow stays confined to the wall.",
  "realism": "UGC realism, real skin texture with visible pores, individual hair strands, real glass and paper textures, realistic shadows and reflections, iPhone-footage look, phone camera look not professional photography, no AI polish, no beauty smoothing, no blur anywhere, everything in sharp focus including background wall.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no studio, no plastic skin, no extra fingers, no supernatural lighting, no blur, no artificial lighting, no warm orange color cast, no yellow tint, no golden glow, no silver jewelry, no second person"
}
```

## K05 · T6 · RECEITA · GERAR DO ZERO · ÂNCORA BRANDON

mel escorrendo da colher para dentro do pote que já tem alho amassado

```json
{
  "shot_id": "K05_recipe_honey",
  "reference_use": "Use the attached image ONLY for Brandon's face, identity, hair, tattoos, wardrobe and the gym scene. Do NOT copy its pose or framing.",
  "identity_main": "The EXACT woman from the reference image (Brandon): mixed-race Black American woman, light-medium skin with soft freckles, brown eyes, cornrows braided back with loose braided ends falling in front of the shoulders and wooden and amber beads on the tips, fine-line floral tattoo sleeve on the arm on the left side of frame.",
  "wardrobe": "White ribbed tank top, black training shorts, thin GOLD chain with a GOLD cross pendant.",
  "prop": "A wide-mouth glass mason jar sits open on the wooden counter in the lower foreground, already about half full with pale amber liquid and coarsely crushed garlic. Brandon holds a metal spoon above it with her right hand, tilted, and a thick unbroken thread of honey runs from the spoon down into the jar. A small wooden board with more crushed garlic and one cut lemon half sit beside the jar.",
  "scene": "SAME concrete-block gym as the reference image: light gray cinderblock wall and a small vintage American flag pinned flat on the wall behind her, discreet but clearly visible and in sharp focus.",
  "posture": "Brandon stands behind the counter looking down at the jar, right arm raised holding the tilted spoon.",
  "composition": "Close. The open jar sits in the lower foreground closer to the lens than her face, and the falling thread of honey runs down the center of the frame. Brandon is visible from the chest up, head cropped at the top edge.",
  "camera": "chest level, straight-on, slightly high toward the jar",
  "state": "Start frame: the honey has just begun to fall from the spoon and the thread has not yet reached the surface.",
  "lighting": "Soft neutral overcast daylight coming through the open gym door. The red neon glow stays confined to the wall.",
  "realism": "UGC realism, real skin texture with visible pores, individual hair strands, real glass and honey textures, realistic shadows and reflections, iPhone-footage look, phone camera look not professional photography, no AI polish, no beauty smoothing, no blur anywhere, everything in sharp focus including background wall.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no studio, no plastic skin, no extra fingers, no supernatural lighting, no blur, no artificial lighting, no warm orange color cast, no yellow tint, no golden glow, no silver jewelry, no second person"
}
```

## K06 · T7 · RECEITA · EDITAR do K05

a colher agora está cheia de sal rosa em cristais, parada acima do pote
> *Anexar: K05 aprovado. Nunca partir do K06 ou do K07 um do outro.*

```json
{
  "task": "edit the attached image, keep everything identical except the changes listed",
  "keep_identical": "Keep Brandon exactly the same: same face, same hair and beads, same tattoos, same white tank top, same gold cross, same body position. Keep the SAME jar in the same place with the same contents, the same wooden board, the same lemon half. Keep the SAME background exactly: cinderblock wall, red neon, American flag, same lighting, same camera height and angle.",
  "change_1": "The spoon in her right hand is now level instead of tilted, and it is heaped with coarse pink salt crystals. There is no honey falling anywhere in the frame.",
  "change_2": "A small open glass grinder of pink salt now sits on the counter beside the jar.",
  "realism": "UGC realism, real skin texture with visible pores, real crystal texture on the salt, iPhone-footage look, no AI polish, no beauty smoothing, no blur anywhere. Do not make her skin darker, yellowish or orangish. Do not make the colors more saturated.",
  "negative": "do not change the face, do not change identity, do not change the background, do not change the jar, do not change the camera angle, no captions, no subtitles, no words overlaid on the image, no plastic skin, no extra fingers, no silver jewelry, no second person, no blur"
}
```

## K07 · T8 · PROTOCOLO · EDITAR do K05

o pote agora está tampado na bancada e as duas mãos dela estão livres
> *Anexar: K05 aprovado.*

```json
{
  "task": "edit the attached image, keep everything identical except the changes listed",
  "keep_identical": "Keep Brandon exactly the same: same face, same hair and beads, same tattoos, same white tank top, same gold cross. Keep the SAME jar in the same place with the same contents, the same wooden board, the same lemon half. Keep the SAME background exactly: cinderblock wall, red neon, American flag, same lighting, same camera height and angle.",
  "change_1": "The jar is now closed with a flat metal screw lid, and there is no spoon and no honey anywhere in the frame.",
  "change_2": "Both of Brandon's hands now rest flat on the counter on either side of the closed jar, and she is looking straight into the lens instead of down.",
  "realism": "UGC realism, real skin texture with visible pores, real metal and glass textures, iPhone-footage look, no AI polish, no beauty smoothing, no blur anywhere. Do not make her skin darker, yellowish or orangish. Do not make the colors more saturated.",
  "negative": "do not change the face, do not change identity, do not change the background, do not change the jar contents, do not change the camera angle, no captions, no subtitles, no words overlaid on the image, no plastic skin, no extra fingers, no silver jewelry, no second person, no blur"
}
```

## K08 · T9, T10 e T11 · MECANISMO e VIRADA · GERAR DO ZERO · ÂNCORA BRANDON

o pote fechado na mão dela, e uma árvore vascular vermelha e azul em pé na bancada colada na lente

```json
{
  "shot_id": "K08_mechanism",
  "reference_use": "Use the attached image ONLY for Brandon's face, identity, hair, tattoos, wardrobe and the gym scene. Do NOT copy its pose or framing.",
  "identity_main": "The EXACT woman from the reference image (Brandon): mixed-race Black American woman, light-medium skin with soft freckles, brown eyes, cornrows braided back with loose braided ends falling in front of the shoulders and wooden and amber beads on the tips, fine-line floral tattoo sleeve on the arm on the left side of frame.",
  "wardrobe": "White ribbed tank top, black training shorts, thin GOLD chain with a GOLD cross pendant.",
  "prop": "A classroom-style anatomical teaching model of a branching vessel tree stands upright on a round black base on the wooden counter, molded in matte silicone, with deep red branches on one side and muted blue branches on the other, splitting into finer and finer cords toward the top. Brandon holds the closed glass mason jar with the pale amber liquid and garlic in her right hand, raised beside her chest.",
  "scene": "SAME concrete-block gym as the reference image: light gray cinderblock wall, red neon sign reading TRAIN PRAY REPEAT, and a small vintage American flag pinned flat on the wall, discreet but clearly visible and in sharp focus.",
  "posture": "Brandon stands upright behind the counter, chin level, holding the jar up beside her chest, speaking directly into the lens.",
  "composition": "Close. The vessel tree stands in the lower foreground closer to the lens than her face, rising into the lower third of the frame on the left. Brandon is visible from the chest up on the right with the jar in hand, head cropped at the top edge. Nothing else competes.",
  "camera": "chest level, straight-on, slightly high toward the counter",
  "state": "Start frame: speaking directly into the lens with the jar raised.",
  "lighting": "Soft neutral overcast daylight coming through the open gym door. The red neon glow stays confined to the wall and does not fall on her skin.",
  "realism": "UGC realism, real skin texture with visible pores, individual hair strands, subtle wrinkles, real matte silicone texture on the model, realistic shadows and reflections, iPhone-footage look, phone camera look not professional photography, no AI polish, no beauty smoothing, no blur anywhere, everything in sharp focus including background wall and signage.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no studio, no plastic skin, no extra fingers, no supernatural lighting, no blur, no artificial lighting, no warm orange color cast, no yellow tint, no golden glow, no silver jewelry, no second person"
}
```

## K09 · T12, T13 e T14 · INCIDENTE, TESTEMUNHA e PONTE · EDITAR do K08

o pote pousado, as mãos livres, câmera um passo mais perto para o bloco mais pessoal do vídeo
> *Anexar: K08 aprovado.*

```json
{
  "task": "edit the attached image, keep everything identical except the changes listed",
  "keep_identical": "Keep Brandon exactly the same: same face, same hair and beads, same tattoos, same white tank top, same gold cross. Keep the SAME vessel tree model in the same place on the counter. Keep the SAME background exactly: cinderblock wall, red neon sign, American flag, same lighting, same camera height and angle.",
  "change_1": "The glass jar is now standing on the counter instead of being held, and both of Brandon's hands are free. Her right hand is open at chest height in a calm, low gesture.",
  "change_2": "Push the camera closer so the framing tightens by about fifteen percent and her face becomes larger in the frame. Her expression is quieter and more direct than before, less instructional and more personal.",
  "realism": "UGC realism, real skin texture with visible pores, iPhone-footage look, no AI polish, no beauty smoothing, no blur anywhere. Do not make her skin darker, yellowish or orangish. Do not make the colors more saturated.",
  "negative": "do not change the face, do not change identity, do not change the background, do not change the vessel tree, no captions, no subtitles, no words overlaid on the image, no plastic skin, no extra fingers, no silver jewelry, no second person, no blur"
}
```

## K10 · T15 e T16 · MECANISMO e ÁLIBI · EDITAR do K08

mesma cena, mão contando no ar
> *Anexar: K08 aprovado. Nunca partir do K09.*

```json
{
  "task": "edit the attached image, keep everything identical except the changes listed",
  "keep_identical": "Keep Brandon exactly the same: same face, same hair and beads, same tattoos, same white tank top, same gold cross. Keep the SAME vessel tree model in the same place on the counter. Keep the SAME background exactly: cinderblock wall, red neon sign, American flag, same lighting, same camera height and angle.",
  "change_1": "The glass jar is now standing on the counter instead of being held, and both of Brandon's hands are free. Her right hand is raised at chest height with three fingers extended in a clear counting gesture.",
  "change_2": "Her eyebrows are slightly raised and her expression is emphatic, like she is laying out something in order.",
  "realism": "UGC realism, real skin texture with visible pores, iPhone-footage look, no AI polish, no beauty smoothing, no blur anywhere. Do not make her skin darker, yellowish or orangish. Do not make the colors more saturated.",
  "negative": "do not change the face, do not change identity, do not change the background, do not change the vessel tree, no captions, no subtitles, no words overlaid on the image, no plastic skin, no extra fingers, no silver jewelry, no second person, no blur"
}
```

## K11 · T17 · PRODUTO · GERAR DO ZERO · ÂNCORA BRANDON + REF-LIVRO

o livro físico erguido na mão dela, a árvore vascular ainda na bancada

```json
{
  "shot_id": "K11_product",
  "reference_use": "Use the first attached image ONLY for Brandon's face, identity, hair, tattoos, wardrobe and the gym scene. Use the second attached image ONLY for the exact look of the book she is holding. Do NOT copy the pose or framing of either reference.",
  "identity_main": "The EXACT woman from the first reference image (Brandon): mixed-race Black American woman, light-medium skin with soft freckles, brown eyes, cornrows braided back with loose braided ends falling in front of the shoulders and wooden and amber beads on the tips, fine-line floral tattoo sleeve on the arm on the left side of frame.",
  "wardrobe": "White ribbed tank top, black training shorts, thin GOLD chain with a GOLD cross pendant.",
  "prop": "The EXACT book from the second reference image: a physical hardcover book about twenty centimeters tall, matte dark navy cover with a cream spine and clean cream lettering reading BODY HACKS FOR MEN, page edges slightly worn. Brandon holds it up in her right hand at chest height, front cover turned toward the lens. The branching vessel tree model on its round black base still stands on the counter in the lower foreground.",
  "scene": "SAME concrete-block gym as the reference image: light gray cinderblock wall, red neon sign reading TRAIN PRAY REPEAT, and a small vintage American flag pinned flat on the wall, discreet but clearly visible and in sharp focus.",
  "posture": "Brandon stands upright behind the counter, chin level, holding the book up beside her chest with the cover facing the camera, speaking directly into the lens.",
  "composition": "Close. The book is held forward, closer to the lens than her face, and its cover is fully readable. The vessel tree stays in the lower foreground on the left. Brandon is visible from the chest up, head cropped at the top edge.",
  "camera": "chest level, straight-on",
  "state": "Start frame: the book just raised into position, her eyes on the lens.",
  "lighting": "Soft neutral overcast daylight coming through the open gym door. The red neon glow stays confined to the wall and does not fall on her skin.",
  "realism": "UGC realism, real skin texture with visible pores, individual hair strands, real paper and cloth texture on the book, realistic shadows and reflections, iPhone-footage look, phone camera look not professional photography, no AI polish, no beauty smoothing, no blur anywhere, everything in sharp focus including background wall and signage.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image beyond the printed book cover, no studio, no plastic skin, no extra fingers, no supernatural lighting, no blur, no artificial lighting, no warm orange color cast, no yellow tint, no golden glow, no silver jewelry, no second person, no screen, no tablet, no phone"
}
```

## K12 · T18 · CTA · EDITAR do K11

o take mais fechado do vídeo inteiro, livro ainda na mão, mão livre apontando para a lente
> *Anexar: K11 aprovado.*

```json
{
  "task": "edit the attached image, keep everything identical except the changes listed",
  "keep_identical": "Keep Brandon exactly the same: same face, same hair and beads, same tattoos, same white tank top, same gold cross. Keep the SAME book with the same cover in her right hand. Keep the SAME background exactly: cinderblock wall, red neon sign, American flag, same lighting, same camera angle.",
  "change_1": "Push the camera in closer than any other shot in the video, so the framing is shoulders-up and her face fills a large part of the frame. The top of her head is cropped by the top edge. The book stays visible in the lower part of the frame.",
  "change_2": "Her left hand comes up into the bottom of the frame with the index finger pointing toward the lens, and her expression is direct and warm.",
  "realism": "UGC realism, real skin texture with visible pores, iPhone-footage look, no AI polish, no beauty smoothing, no blur anywhere. Do not make her skin darker, yellowish or orangish. Do not make the colors more saturated.",
  "negative": "do not change the face, do not change identity, do not change the background, do not change the book cover, no captions, no subtitles, no words overlaid on the image, no plastic skin, no extra fingers, no silver jewelry, no second person, no blur"
}
```

---

# Bloco global de vídeo

Colar em todo prompt de vídeo, já embutido em cada um abaixo.

```text
o avatar (mulher) fala em inglês com sotaque americano de mulher negra americana, voz autêntica, dinâmica, apaixonada e emocional, como se exigisse ser ouvida, a seguinte frase: "[FALA]"

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: [AÇÃO ENXUTA]

câmera: [MOVIMENTO]

som ambiente: ambiente de box de treino, sem música
```

---

# Prompts de vídeo

### V01 · T1 · usa K01

```text
o avatar (mulher) fala em inglês com sotaque americano de mulher negra americana, voz autêntica, dinâmica, apaixonada e emocional, como se exigisse ser ouvida, a seguinte frase: "Brother, this is what twenty years of sugar buildup looks like inside your champion. And nobody has ever shown you one."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ela segura o objeto encrustado em pé com as duas mãos e o gira devagar meia volta enquanto olha para a câmera.

câmera: fixa, leve handheld natural

som ambiente: ambiente de box de treino, sem música
```

### V02 · T2 · usa K02

```text
o avatar (mulher) fala em inglês com sotaque americano de mulher negra americana, voz autêntica, dinâmica, apaixonada e emocional, como se exigisse ser ouvida, a seguinte frase: "Every man past forty who walks into my gym gets the same three words from his doctor. Nothing is wrong."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: as mãos dela seguram o objeto embaixo do líquido âmbar e nuvens brancas soltam da crosta e se espalham na bandeja.

câmera: fixa

som ambiente: ambiente de box de treino, sem música
```

### V03 · T3 · usa K03

```text
o avatar (mulher) fala em inglês com sotaque americano de mulher negra americana, voz autêntica, dinâmica, apaixonada e emocional, como se exigisse ser ouvida, a seguinte frase: "Because nobody is looking at this. They read your blood work, they call it age, and they send you home."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ela mantém o objeto em pé na linha do líquido e pequenos flocos pálidos continuam se soltando dele.

câmera: fixa, leve push-in

som ambiente: ambiente de box de treino, sem música
```

### V04 · T4 · usa K03

```text
(sem fala no take: a fala 4 não existe, este take é mudo e entra sem voz-over na edição)

o que acontece no vídeo: ela fecha as duas mãos sobre o objeto e a crosta seca racha e se abre em pedaços, que caem na bandeja. Embaixo aparece a superfície lisa com os cordões vermelhos e azuis.

câmera: fixa, leve push-in

som ambiente: ambiente de box de treino, sem música
```

### V05 · T5 · usa K04

```text
o avatar (mulher) fala em inglês com sotaque americano de mulher negra americana, voz autêntica, dinâmica, apaixonada e emocional, como se exigisse ser ouvida, a seguinte frase: "Everything that strips it costs thirteen dollars, and it is sitting in the store you already shop at every week."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ela passa a mão aberta sobre a fileira de itens na bancada e olha para a câmera.

câmera: fixa

som ambiente: ambiente de box de treino, sem música
```

### V06 · T6 · usa K05

```text
o avatar (mulher) fala em inglês com sotaque americano de mulher negra americana, voz autêntica, dinâmica, apaixonada e emocional, como se exigisse ser ouvida, a seguinte frase: "Raw apple cider vinegar in a jar. One tablespoon of honey, and three or four cloves of garlic, crushed."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: o mel escorre da colher e cai dentro do pote, e ela olha do pote para a câmera.

câmera: fixa

som ambiente: ambiente de box de treino, sem música
```

### V07 · T7 · usa K06

```text
o avatar (mulher) fala em inglês com sotaque americano de mulher negra americana, voz autêntica, dinâmica, apaixonada e emocional, como se exigisse ser ouvida, a seguinte frase: "Finally, one teaspoon of pink Himalayan salt. Four things, and you probably have three of them already."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ela vira a colher e os cristais de sal rosa caem dentro do pote.

câmera: fixa

som ambiente: ambiente de box de treino, sem música
```

### V08 · T8 · usa K07

```text
o avatar (mulher) fala em inglês com sotaque americano de mulher negra americana, voz autêntica, dinâmica, apaixonada e emocional, como se exigisse ser ouvida, a seguinte frase: "Seal it and let it sit overnight. One to two spoons every morning, before anything else hits your stomach."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ela apoia a mão em cima da tampa do pote e olha para a câmera enquanto fala.

câmera: fixa

som ambiente: ambiente de box de treino, sem música
```

### V09 · T9 · usa K08

```text
o avatar (mulher) fala em inglês com sotaque americano de mulher negra americana, voz autêntica, dinâmica, apaixonada e emocional, como se exigisse ser ouvida, a seguinte frase: "The vinegar strips the sugar off your vessel walls. The garlic pushes the vessel open. Two different jobs."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ela levanta um pouco o pote ao falar do vinagre e depois aponta com a mão livre para o modelo na bancada.

câmera: fixa

som ambiente: ambiente de box de treino, sem música
```

### V10 · T10 · usa K08

```text
o avatar (mulher) fala em inglês com sotaque americano de mulher negra americana, voz autêntica, dinâmica, apaixonada e emocional, como se exigisse ser ouvida, a seguinte frase: "The salt keeps the water in the blood, and it starts arriving where it stopped arriving."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ela desce a mão livre acompanhando os ramos do modelo de cima para baixo enquanto fala.

câmera: fixa, leve push-in

som ambiente: ambiente de box de treino, sem música
```

### V11 · T11 · usa K08

```text
o avatar (mulher) fala em inglês com sotaque americano de mulher negra americana, voz autêntica, dinâmica, apaixonada e emocional, como se exigisse ser ouvida, a seguinte frase: "But here is the part that costs men years. You could strip every pipe in your body and still lie there with nothing happening."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ela para o gesto, abaixa o pote e encara a câmera de frente.

câmera: fixa, leve push-in

som ambiente: ambiente de box de treino, sem música
```

### V12 · T12 · usa K09

```text
o avatar (mulher) fala em inglês com sotaque americano de mulher negra americana, voz autêntica, dinâmica, apaixonada e emocional, como se exigisse ser ouvida, a seguinte frase: "You know the night I mean. She was ready. You were ready in your head. And nothing else showed up."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ela fala mais baixo e mais devagar, quase parada, com a mão aberta na altura do peito.

câmera: fixa

som ambiente: ambiente de box de treino, sem música
```

### V13 · T13 · usa K09

```text
o avatar (mulher) fala em inglês com sotaque americano de mulher negra americana, voz autêntica, dinâmica, apaixonada e emocional, como se exigisse ser ouvida, a seguinte frase: "And you said you were tired. Here is what no woman says to your face. She knew, and she let that excuse stand."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ela inclina levemente a cabeça e sustenta o olhar na câmera até o fim da frase.

câmera: fixa

som ambiente: ambiente de box de treino, sem música
```

### V14 · T14 · usa K09

```text
o avatar (mulher) fala em inglês com sotaque americano de mulher negra americana, voz autêntica, dinâmica, apaixonada e emocional, como se exigisse ser ouvida, a seguinte frase: "That was not a pipe problem. The pipe was clean that night. The order to open it never came, and no pill writes that order."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ela aponta rapidamente para o modelo na bancada e volta a mão para a altura do peito.

câmera: fixa

som ambiente: ambiente de box de treino, sem música
```

### V15 · T15 · usa K10

```text
o avatar (mulher) fala em inglês com sotaque americano de mulher negra americana, voz autêntica, dinâmica, apaixonada e emocional, como se exigisse ser ouvida, a seguinte frase: "Your body writes that order while you sleep, ships it when you lift heavy, and what sits at your waist eats it first."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ela conta três dedos no ar, um a cada parte da frase.

câmera: fixa

som ambiente: ambiente de box de treino, sem música
```

### V16 · T16 · usa K10

```text
o avatar (mulher) fala em inglês com sotaque americano de mulher negra americana, voz autêntica, dinâmica, apaixonada e emocional, como se exigisse ser ouvida, a seguinte frase: "Nothing about you quit. Those three stopped talking to each other, and nobody ever sent you the update."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ela abre a mão devagar e balança a cabeça de leve negando na primeira frase.

câmera: fixa

som ambiente: ambiente de box de treino, sem música
```

### V17 · T17 · usa K11

```text
o avatar (mulher) fala em inglês com sotaque americano de mulher negra americana, voz autêntica, dinâmica, apaixonada e emocional, como se exigisse ser ouvida, a seguinte frase: "So this is what I hand them now. Body Hacks for Men 40+, with the order already done, so you stop guessing."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ela levanta o livro na altura do peito com a capa virada para a câmera no exato momento em que diz o nome.

câmera: fixa

som ambiente: ambiente de box de treino, sem música
```

### V18 · T18 · usa K12

```text
o avatar (mulher) fala em inglês com sotaque americano de mulher negra americana, voz autêntica, dinâmica, apaixonada e emocional, como se exigisse ser ouvida, a seguinte frase: "If you want your drive back, comment yes and I send it to you myself. Follow me first, or it will not let me reach you."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ela aponta para a câmera ao dizer a palavra yes, inclina o corpo levemente para frente e fecha com expressão direta.

câmera: fixa, leve push-in

som ambiente: ambiente de box de treino, sem música
```

---

## Mapa de âncoras

| Keyframe | Referências a anexar | Modelo |
|---|---|---|
| REF-PROP | nenhuma, gerar do zero | Nano Banana 2, regenerar até a crosta ficar crível |
| REF-VASO | nenhuma, gerar do zero | Nano Banana 2 |
| REF-LIVRO | nenhuma, gerar do zero | Nano Banana 2, regenerar até a capa sair legível |
| K01 | âncora Brandon + REF-PROP aprovado | Nano Banana **Pro**, várias variações |
| K02 | K01 aprovado | Nano Banana 2, comando de edição |
| K03 | âncora Brandon + REF-PROP aprovado | Nano Banana **Pro**, várias variações |
| K04 | âncora Brandon | Nano Banana 2 |
| K05 | âncora Brandon | Nano Banana 2 |
| K06 | K05 aprovado | Nano Banana 2, comando de edição |
| K07 | K05 aprovado (**nunca a partir do K06**) | Nano Banana 2, comando de edição |
| K08 | âncora Brandon | Nano Banana 2 |
| K09 | K08 aprovado | Nano Banana 2, comando de edição |
| K10 | K08 aprovado (**nunca a partir do K09**) | Nano Banana 2, comando de edição |
| K11 | âncora Brandon + REF-LIVRO aprovado | Nano Banana 2 |
| K12 | K11 aprovado | Nano Banana 2, comando de edição |

---

## Montagem no CapCut

- Timeline 1080x1920, 30 fps.
- Cortes duros entre todos os takes. Os dois cortes que pedem peso são **V04 para V05** (a quebra do prop para a bancada de ingredientes) e **V11 para V12** (a virada para o bloco pessoal).
- **O V04 é mudo e entra cortado em cerca de 2 segundos**, só a quebra e o reveal. No original esse momento dura 1,4s e é o que segura o vídeo.
- Cortar o silêncio inicial de cada clipe para a fala começar imediatamente.
- Legendas grandes estilo Captions.ai Prism Pro, palavra destacada em vermelho, centralizadas na altura do peito. **Nunca cobrir o prop no hook nem a capa do livro no V17.**
- **A legenda é quem carrega a leitura anatômica.** No V01 e no V04 a legenda tem que estar grande e legível, porque o prop é deliberadamente ambíguo em quadro.
- Manter `YES` isolado na tela no V18.
- Color grading: temp -3, tint +2, saturação -6, exposição -3, contraste +12, highlight -35, shadow +18, fade +6.

## Gates de qualidade

1. Brandon é a mesma mulher em todos os clipes, com a **cruz de OURO** em todos, nunca prata.
2. As cornrows com miçangas de madeira e âmbar estão iguais em todos os planos.
3. O prop herói tem forma, tamanho, cordões vermelhos e azuis e crosta **idênticos** em K01, K02 e K03.
4. A crosta do K03 ainda está inteira. **O reveal acontece no vídeo, nunca na imagem.**
5. O livro tem a mesma capa em K11 e K12, e a capa está legível no V17.
6. Nenhuma legenda ou texto foi gerado dentro da imagem, e a sinalização canônica da parede continua existindo.
7. **Bandeira dos EUA discreta, visível e em foco em todos os keyframes com cenário.**
8. Nunca mais de três âncoras de fundo por quadro.
9. Mãos com cinco dedos, sem fusão com o prop, com o pote nem com o livro.
10. Luz neutra de dia nublado em todos os planos. O vermelho do neon fica na parede e nunca na pele.
11. Zero blur em qualquer plano, inclusive parede e prateleira.
12. `yes` e o follow gate estão os dois no V18, e o V18 é o plano mais fechado do vídeo inteiro.
13. Nenhum take diz que ela envia um livro impresso. O produto é digital.
14. Nenhum take usa `treat`, `cure`, nome clínico de órgão ou `johnson`.
