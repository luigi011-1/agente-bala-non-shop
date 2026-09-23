# Jamie Anderson | Ângulo 2 (FityWell) | Pacote de Prompts

Vídeo modelo: `a8291dcf-3601-417b-8071-0d4076190f1c.mp4` (12,00 s, 1 take contínuo)

Âncora de identidade: `producao/_ancoras/jamie_anderson_ancora.jpeg`

Funil: vídeo de GROWTH. `comment yes` + follow, sem beat de venda.

Avatar 2 de 3 da fila (`AVATAR_QUEUE.md`). O pacote fechado do anterior está em `PROMPTS_DANA_MORRISON.md`.

---

## Índice de geração

| Take | Keyframe | Anexar | Ação de geração |
|---|---|---|---|
| T1 | K01 | ÂNCORA DANA MORRISON | GERAR DO ZERO. Gancho A, a mão que afunda |
| T1 | K02 | ÂNCORA DANA MORRISON | GERAR DO ZERO. Gancho B, o contorno riscado |
| T1 | K03 | ÂNCORA DANA MORRISON | GERAR DO ZERO. Gancho C, a camada amarela |
| T1 | K04 | ÂNCORA DANA MORRISON | GERAR DO ZERO. Gancho D, o vestido de verão |
| T2 | K05 | ÂNCORA DANA MORRISON | GERAR DO ZERO. CTA com os modelos nus, serve aos ganchos A, B e C |
| T2 | K06 | ÂNCORA DANA MORRISON | GERAR DO ZERO. CTA com os manequins vestidos, serve ao gancho D |

Regra de bolso: **GERAR DO ZERO anexa a âncora. EDITAR anexa uma imagem só, o keyframe de origem.**
Aqui não há EDITAR: os quatro ganchos têm props diferentes e os dois takes de CTA precisam bater com o gancho que veio antes.

**Cada vídeo finalizado usa UM gancho.** A montagem é sempre um par: K01 com K05, K02 com K05, K03 com K05, K04 com K06.

---

## Trava de identidade e continuidade

- Homem negro americano, meados dos cinquenta, pele marrom média, porte atlético e enxuto.
- **Cabelo curto, corte baixo, muito grisalho** nas têmporas e no topo, entradas naturais.
- **Barba curta cheia, quase toda branca**, com bigode grisalho. Pintas e sardas visíveis nas maçãs do rosto.
- **Camisa de linho BRANCA de botão**, colarinho aberto, mangas dobradas até o antebraço. Calça escura.
- **ZERO joia, sem corrente, sem relógio, sem cruz.** A ausência de joia é traço dele.
- Cenário adaptado: **porta-malas aberto do SUV**, no mesmo estacionamento da âncora, com fileira de lojas de tijolo ao fundo e o **adesivo da bandeira dos EUA no vidro lateral**. O piso do porta-malas é a superfície da demo.
- **Ele fica EM PÉ no porta-malas nos dois takes**, nunca sentado no banco do motorista. `no seated driver pose` obrigatório no negative.
- Luz neutra de dia nublado. Zero blur, tudo em foco nítido.
- **Teto de fundo descrito: dois blocos.** Lojas e carros atrás, adesivo da bandeira no vidro ao lado.

---

## Trava de locação (adaptação registrada)

O banco do motorista não comporta dois modelos apoiados, então a bancada dele vira o **porta-malas aberto**, no mesmo estacionamento, preservando carro, lojas ao fundo e o adesivo da bandeira. É a mesma solução da `fitywell_pernas`.

⚠️ **Desvio deliberado daquele precedente:** lá os takes de CTA voltavam para o banco do motorista. Aqui **os dois takes ficam no porta-malas**, porque o vídeo modelo é um take contínuo e trocar de locação no único corte denunciaria o corte.

## Trava do prop herói

```text
Soft matte silicone teaching models molded in muted cream, smooth shapes with no face and no fine
detail, resting flat on the tailgate floor in the lower foreground, closer to the lens than the man's face.
The heavy one is a large rounded dome that sags forward with soft folds. The lean one is a firm flat
panel with shallow grooves. Never anatomical precision, never a declared gender, never a named body
region.
```

**A forma vai descrita no positivo, nunca negada.** Nome de órgão ou de região do corpo no `negative` injeta o conceito e derruba a geração, que foi o que travou o K02 do Dana Morrison em 2026-09-10.

## Trava da 2ª pessoa (REF-A)

**Não se aplica.** Não há segunda pessoa em nenhum take.

---

# Prompts de imagem

## K01 · T1 · GANCHO A, a mão que afunda · GERAR DO ZERO · ÂNCORA JAMIE ANDERSON

> ### 📎 ANEXAR: **1 IMAGEM**
> **1️⃣ ÂNCORA JAMIE ANDERSON** `producao/_ancoras/jamie_anderson_ancora.jpeg`
>
> ### 🆕 GERAR DO ZERO

```json
{
  "shot_id": "K01_hook_hand_sinks",
  "reference_use": "Use the attached image ONLY for Jamie Anderson's face, identity, hair, wardrobe, his SUV and the parking lot. Do NOT copy its pose or framing.",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "identity_main": "The EXACT man from the attached reference image (Jamie Anderson): Black American man in his mid fifties, medium brown skin, short low-cut hair heavily greying at the temples and on top with a natural receding hairline, a short full beard almost entirely white with a grey moustache, a symmetrical face with a high forehead, visible moles and freckles across his cheeks, grey eyebrows and dark brown eyes, an athletic lean build with broad shoulders, real skin texture with visible pores, forehead lines and crow's feet, no makeup.",
  "wardrobe": "A white linen button shirt with the collar open and no tie, sleeves rolled up to the forearm, and dark trousers. No chain, no watch, no jewelry of any kind.",
  "prop": "Two soft matte silicone teaching models molded in muted cream, smooth shapes with no face and no fine detail, resting flat on the tailgate floor side by side. The one on the LEFT is a large heavy rounded dome about the size of a dinner tray that sags forward, with soft folds and a finely creased surface. The one on the RIGHT is a firm flat panel of the same cream material with shallow grooves molded into it. Both models are bare and clean. His right hand is open, palm down, held just above the left model.",
  "scene": "SAME ordinary American parking lot as the reference image, unchanged: he stands at the OPEN REAR TAILGATE of his parked SUV, with a row of brick storefronts with awnings and a few parked cars behind him, and the small American flag sticker on the SUV side window glass beside him, discreet but clearly visible and in sharp focus. The flat carpeted tailgate floor runs across the foreground and serves as the working surface.",
  "posture": "Standing at the open rear tailgate, leaning forward over the tailgate floor toward the camera, NOT the seated driver pose of the reference photo.",
  "composition": "The two models fill the lower two thirds of the frame and sit much closer to the lens than his face, so they are unmistakably the hero. His head and shoulders occupy the upper third and the top of his head is cropped by the top edge. Nothing else competes.",
  "camera": "chest level, straight-on, camera pushed in close and slightly high toward the models on the tailgate floor",
  "state": "Start frame: his open palm is a finger's width above the surface of the left model and has not touched it yet. Nothing has moved.",
  "lighting": "Flat neutral daylight under an overcast sky, evenly lighting his face, no warm orange cast and no yellow tint.",
  "realism": "UGC realism, real skin texture with visible pores, individual hair strands, subtle wrinkles, realistic shadows and reflections, iPhone-footage look, phone camera look not professional photography, no AI polish, no beauty smoothing, no blur anywhere, everything in sharp focus including the storefronts behind him.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no studio, no plastic skin, no extra fingers, no supernatural lighting, no blur, no artificial lighting, no warm orange color cast, no yellow tint, no beauty smoothing, no jewelry, no watch, no seated driver pose, no second person, no foam"
}
```

## K02 · T1 · GANCHO B, o contorno riscado · GERAR DO ZERO · ÂNCORA JAMIE ANDERSON

> ### 📎 ANEXAR: **1 IMAGEM**
> **1️⃣ ÂNCORA JAMIE ANDERSON** `producao/_ancoras/jamie_anderson_ancora.jpeg`
>
> ### 🆕 GERAR DO ZERO

```json
{
  "shot_id": "K02_hook_drawn_outline",
  "reference_use": "Use the attached image ONLY for Jamie Anderson's face, identity, hair, wardrobe, his SUV and the parking lot. Do NOT copy its pose or framing.",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "identity_main": "The EXACT man from the attached reference image (Jamie Anderson): Black American man in his mid fifties, medium brown skin, short low-cut hair heavily greying at the temples and on top with a natural receding hairline, a short full beard almost entirely white with a grey moustache, a symmetrical face with a high forehead, visible moles and freckles across his cheeks, grey eyebrows and dark brown eyes, an athletic lean build with broad shoulders, real skin texture with visible pores, forehead lines and crow's feet, no makeup.",
  "wardrobe": "A white linen button shirt with the collar open and no tie, sleeves rolled up to the forearm, and dark trousers. No chain, no watch, no jewelry of any kind.",
  "prop": "Two soft matte silicone teaching models molded in muted cream, smooth shapes with no face and no fine detail, resting flat on the tailgate floor side by side. The one on the LEFT is a large heavy rounded dome about the size of a dinner tray that sags forward, with soft folds and a finely creased surface. The one on the RIGHT is a firm flat panel of the same cream material with shallow grooves molded into it. In his right hand he holds a thick black marker pen, cap off, held against the left edge of the left model.",
  "scene": "SAME ordinary American parking lot as the reference image, unchanged: he stands at the OPEN REAR TAILGATE of his parked SUV, with a row of brick storefronts with awnings and a few parked cars behind him, and the small American flag sticker on the SUV side window glass beside him, discreet but clearly visible and in sharp focus. The flat carpeted tailgate floor runs across the foreground and serves as the working surface.",
  "posture": "Standing at the open rear tailgate, leaning forward over the tailgate floor toward the camera, NOT the seated driver pose of the reference photo.",
  "composition": "The two models fill the lower two thirds of the frame and sit much closer to the lens than his face, so they are unmistakably the hero. His head and shoulders occupy the upper third and the top of his head is cropped by the top edge. Nothing else competes.",
  "camera": "chest level, straight-on, camera pushed in close and slightly high toward the models on the tailgate floor",
  "state": "Start frame: the marker tip is touching the left edge of the left model and no line has been drawn yet.",
  "lighting": "Flat neutral daylight under an overcast sky, evenly lighting his face, no warm orange cast and no yellow tint.",
  "realism": "UGC realism, real skin texture with visible pores, individual hair strands, subtle wrinkles, realistic shadows and reflections, iPhone-footage look, phone camera look not professional photography, no AI polish, no beauty smoothing, no blur anywhere, everything in sharp focus including the storefronts behind him.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no studio, no plastic skin, no extra fingers, no supernatural lighting, no blur, no artificial lighting, no warm orange color cast, no yellow tint, no beauty smoothing, no jewelry, no watch, no seated driver pose, no second person, no foam"
}
```

## K03 · T1 · GANCHO C, a camada amarela · GERAR DO ZERO · ÂNCORA JAMIE ANDERSON

> ### 📎 ANEXAR: **1 IMAGEM**
> **1️⃣ ÂNCORA JAMIE ANDERSON** `producao/_ancoras/jamie_anderson_ancora.jpeg`
>
> ### 🆕 GERAR DO ZERO

```json
{
  "shot_id": "K03_hook_yellow_layer",
  "reference_use": "Use the attached image ONLY for Jamie Anderson's face, identity, hair, wardrobe, his SUV and the parking lot. Do NOT copy its pose or framing.",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "identity_main": "The EXACT man from the attached reference image (Jamie Anderson): Black American man in his mid fifties, medium brown skin, short low-cut hair heavily greying at the temples and on top with a natural receding hairline, a short full beard almost entirely white with a grey moustache, a symmetrical face with a high forehead, visible moles and freckles across his cheeks, grey eyebrows and dark brown eyes, an athletic lean build with broad shoulders, real skin texture with visible pores, forehead lines and crow's feet, no makeup.",
  "wardrobe": "A white linen button shirt with the collar open and no tie, sleeves rolled up to the forearm, and dark trousers. No chain, no watch, no jewelry of any kind.",
  "prop": "Two soft matte silicone teaching models molded in muted cream, smooth shapes with no face and no fine detail, resting flat on the tailgate floor side by side. The one on the LEFT is a large heavy rounded dome about the size of a dinner tray that sags forward, with soft folds and a finely creased surface. The one on the RIGHT is a firm flat panel of the same cream material with shallow grooves molded into it. The whole upper surface of the LEFT model is covered by a THICK, HEAPED, three-dimensional mound of small round pale yellow beads, piled high with real volume so that almost none of the cream surface shows. The RIGHT model is completely bare and clean. In his right hand he holds a thin pale wooden pointer stick, angled down just above the mound of beads.",
  "scene": "SAME ordinary American parking lot as the reference image, unchanged: he stands at the OPEN REAR TAILGATE of his parked SUV, with a row of brick storefronts with awnings and a few parked cars behind him, and the small American flag sticker on the SUV side window glass beside him, discreet but clearly visible and in sharp focus. The flat carpeted tailgate floor runs across the foreground and serves as the working surface.",
  "posture": "Standing at the open rear tailgate, leaning forward over the tailgate floor toward the camera, NOT the seated driver pose of the reference photo.",
  "composition": "The two models fill the lower two thirds of the frame and sit much closer to the lens than his face, so they are unmistakably the hero. His head and shoulders occupy the upper third and the top of his head is cropped by the top edge. Nothing else competes.",
  "camera": "chest level, straight-on, camera pushed in close and slightly high toward the models on the tailgate floor",
  "state": "Start frame: the tip of the pointer stick hovers just above the mound of beads and has not touched it yet.",
  "lighting": "Flat neutral daylight under an overcast sky, evenly lighting his face, no warm orange cast and no yellow tint.",
  "realism": "UGC realism, real skin texture with visible pores, individual hair strands, subtle wrinkles, realistic shadows and reflections, iPhone-footage look, phone camera look not professional photography, no AI polish, no beauty smoothing, no blur anywhere, everything in sharp focus including the storefronts behind him.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no studio, no plastic skin, no extra fingers, no supernatural lighting, no blur, no artificial lighting, no warm orange color cast, no yellow tint, no beauty smoothing, no jewelry, no watch, no seated driver pose, no second person, no foam, no thin scattered layer, no flat sauce-like coating"
}
```

## K04 · T1 · GANCHO D, o vestido de verão · GERAR DO ZERO · ÂNCORA JAMIE ANDERSON

> ### 📎 ANEXAR: **1 IMAGEM**
> **1️⃣ ÂNCORA JAMIE ANDERSON** `producao/_ancoras/jamie_anderson_ancora.jpeg`
>
> ### 🆕 GERAR DO ZERO

```json
{
  "shot_id": "K04_hook_summer_dress",
  "reference_use": "Use the attached image ONLY for Jamie Anderson's face, identity, hair, wardrobe, his SUV and the parking lot. Do NOT copy its pose or framing.",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "identity_main": "The EXACT man from the attached reference image (Jamie Anderson): Black American man in his mid fifties, medium brown skin, short low-cut hair heavily greying at the temples and on top with a natural receding hairline, a short full beard almost entirely white with a grey moustache, a symmetrical face with a high forehead, visible moles and freckles across his cheeks, grey eyebrows and dark brown eyes, an athletic lean build with broad shoulders, real skin texture with visible pores, forehead lines and crow's feet, no makeup.",
  "wardrobe": "A white linen button shirt with the collar open and no tie, sleeves rolled up to the forearm, and dark trousers. No chain, no watch, no jewelry of any kind.",
  "prop": "Two dressmaker mannequin torsos on short metal stands, resting on the tailgate floor side by side, both wearing the SAME light floral summer dress. On the LEFT the fabric is pulled taut and straining across the form, with visible drag lines. On the RIGHT the same dress hangs straight and loose. In his right hand he holds a thin pale wooden pointer stick, aimed at the left mannequin.",
  "scene": "SAME ordinary American parking lot as the reference image, unchanged: he stands at the OPEN REAR TAILGATE of his parked SUV, with a row of brick storefronts with awnings and a few parked cars behind him, and the small American flag sticker on the SUV side window glass beside him, discreet but clearly visible and in sharp focus. The flat carpeted tailgate floor runs across the foreground and serves as the working surface.",
  "posture": "Standing at the open rear tailgate, leaning forward over the tailgate floor toward the camera, NOT the seated driver pose of the reference photo.",
  "composition": "The two dressed mannequin torsos fill the lower two thirds of the frame and sit much closer to the lens than his face, so they are unmistakably the hero. His head and shoulders occupy the upper third and the top of his head is cropped by the top edge. Nothing else competes.",
  "camera": "chest level, straight-on, camera pushed in close and slightly high toward the models on the tailgate floor",
  "state": "Start frame: the tip of the pointer stick rests against the straining fabric of the left mannequin and has not moved yet.",
  "lighting": "Flat neutral daylight under an overcast sky, evenly lighting his face, no warm orange cast and no yellow tint.",
  "realism": "UGC realism, real skin texture with visible pores, individual hair strands, subtle wrinkles, realistic shadows and reflections, iPhone-footage look, phone camera look not professional photography, no AI polish, no beauty smoothing, no blur anywhere, everything in sharp focus including the storefronts behind him.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no studio, no plastic skin, no extra fingers, no supernatural lighting, no blur, no artificial lighting, no warm orange color cast, no yellow tint, no beauty smoothing, no jewelry, no watch, no seated driver pose, no second person, no foam"
}
```

## K05 · T2 · CTA, continuidade dos ganchos A, B e C · GERAR DO ZERO · ÂNCORA JAMIE ANDERSON

> ### 📎 ANEXAR: **1 IMAGEM**
> **1️⃣ ÂNCORA JAMIE ANDERSON** `producao/_ancoras/jamie_anderson_ancora.jpeg`
>
> ### 🆕 GERAR DO ZERO

```json
{
  "shot_id": "K05_cta_bare_models",
  "reference_use": "Use the attached image ONLY for Jamie Anderson's face, identity, hair, wardrobe, his SUV and the parking lot. Do NOT copy its pose or framing.",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "identity_main": "The EXACT man from the attached reference image (Jamie Anderson): Black American man in his mid fifties, medium brown skin, short low-cut hair heavily greying at the temples and on top with a natural receding hairline, a short full beard almost entirely white with a grey moustache, a symmetrical face with a high forehead, visible moles and freckles across his cheeks, grey eyebrows and dark brown eyes, an athletic lean build with broad shoulders, real skin texture with visible pores, forehead lines and crow's feet, no makeup.",
  "wardrobe": "A white linen button shirt with the collar open and no tie, sleeves rolled up to the forearm, and dark trousers. No chain, no watch, no jewelry of any kind.",
  "prop": "Two soft matte silicone teaching models molded in muted cream, smooth shapes with no face and no fine detail, resting flat on the tailgate floor side by side. The one on the LEFT is a large heavy rounded dome about the size of a dinner tray that sags forward, with soft folds and a finely creased surface. The one on the RIGHT is a firm flat panel of the same cream material with shallow grooves molded into it. Both models are bare and clean. The wooden pointer stick lies flat on the tailgate floor between them and both his hands are open and free.",
  "scene": "SAME ordinary American parking lot as the reference image, unchanged: he stands at the OPEN REAR TAILGATE of his parked SUV, with a row of brick storefronts with awnings and a few parked cars behind him, and the small American flag sticker on the SUV side window glass beside him, discreet but clearly visible and in sharp focus. The flat carpeted tailgate floor runs across the foreground and serves as the working surface.",
  "posture": "Standing at the open rear tailgate, leaning forward over the tailgate floor toward the camera, NOT the seated driver pose of the reference photo.",
  "composition": "Tighter than every other frame: his head and shoulders fill the upper half of the frame and he is close to the lens. The two models stay in the lower foreground, cut by the bottom edge. Nothing else competes.",
  "camera": "chest level, straight-on, camera pushed in close and slightly high toward the models on the tailgate floor",
  "state": "Start frame: he is looking straight into the camera and starting to speak, both hands open above the tailgate floor.",
  "lighting": "Flat neutral daylight under an overcast sky, evenly lighting his face, no warm orange cast and no yellow tint.",
  "realism": "UGC realism, real skin texture with visible pores, individual hair strands, subtle wrinkles, realistic shadows and reflections, iPhone-footage look, phone camera look not professional photography, no AI polish, no beauty smoothing, no blur anywhere, everything in sharp focus including the storefronts behind him.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no studio, no plastic skin, no extra fingers, no supernatural lighting, no blur, no artificial lighting, no warm orange color cast, no yellow tint, no beauty smoothing, no jewelry, no watch, no seated driver pose, no second person, no foam"
}
```

## K06 · T2 · CTA, continuidade do gancho D · GERAR DO ZERO · ÂNCORA JAMIE ANDERSON

> ### 📎 ANEXAR: **1 IMAGEM**
> **1️⃣ ÂNCORA JAMIE ANDERSON** `producao/_ancoras/jamie_anderson_ancora.jpeg`
>
> ### 🆕 GERAR DO ZERO

```json
{
  "shot_id": "K06_cta_dressed_mannequins",
  "reference_use": "Use the attached image ONLY for Jamie Anderson's face, identity, hair, wardrobe, his SUV and the parking lot. Do NOT copy its pose or framing.",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "identity_main": "The EXACT man from the attached reference image (Jamie Anderson): Black American man in his mid fifties, medium brown skin, short low-cut hair heavily greying at the temples and on top with a natural receding hairline, a short full beard almost entirely white with a grey moustache, a symmetrical face with a high forehead, visible moles and freckles across his cheeks, grey eyebrows and dark brown eyes, an athletic lean build with broad shoulders, real skin texture with visible pores, forehead lines and crow's feet, no makeup.",
  "wardrobe": "A white linen button shirt with the collar open and no tie, sleeves rolled up to the forearm, and dark trousers. No chain, no watch, no jewelry of any kind.",
  "prop": "Two dressmaker mannequin torsos on short metal stands, resting on the tailgate floor side by side, both wearing the SAME light floral summer dress. On the LEFT the fabric is pulled taut and straining across the form, with visible drag lines. On the RIGHT the same dress hangs straight and loose. The wooden pointer stick lies flat on the tailgate floor in front of them and both his hands are open and free.",
  "scene": "SAME ordinary American parking lot as the reference image, unchanged: he stands at the OPEN REAR TAILGATE of his parked SUV, with a row of brick storefronts with awnings and a few parked cars behind him, and the small American flag sticker on the SUV side window glass beside him, discreet but clearly visible and in sharp focus. The flat carpeted tailgate floor runs across the foreground and serves as the working surface.",
  "posture": "Standing at the open rear tailgate, leaning forward over the tailgate floor toward the camera, NOT the seated driver pose of the reference photo.",
  "composition": "Tighter than every other frame: his head and shoulders fill the upper half of the frame and he is close to the lens. The two models stay in the lower foreground, cut by the bottom edge. Nothing else competes.",
  "camera": "chest level, straight-on, camera pushed in close and slightly high toward the models on the tailgate floor",
  "state": "Start frame: he is looking straight into the camera and starting to speak, both hands open above the tailgate floor.",
  "lighting": "Flat neutral daylight under an overcast sky, evenly lighting his face, no warm orange cast and no yellow tint.",
  "realism": "UGC realism, real skin texture with visible pores, individual hair strands, subtle wrinkles, realistic shadows and reflections, iPhone-footage look, phone camera look not professional photography, no AI polish, no beauty smoothing, no blur anywhere, everything in sharp focus including the storefronts behind him.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no studio, no plastic skin, no extra fingers, no supernatural lighting, no blur, no artificial lighting, no warm orange color cast, no yellow tint, no beauty smoothing, no jewelry, no watch, no seated driver pose, no second person, no foam"
}
```

---

## Bloco global de vídeo

```text
o avatar (homem) fala em inglês com sotaque americano de Jamie Anderson, voz autêntica, dinâmica, apaixonada e emocional, como se exigisse ser ouvida, a seguinte frase: "[FALA EXATA DO ROTEIRO]"

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: [ação ENXUTA, só o que acontece]

câmera: [fixa / leve push-in]

som ambiente: estacionamento aberto, com carros passando ao longe, sem música
```

---

# Prompts de vídeo

### V01 · T1 · usa K01

```text
o avatar (homem) fala em inglês com sotaque americano de Jamie Anderson, voz autêntica, dinâmica, apaixonada e emocional, como se exigisse ser ouvida, a seguinte frase: "If your belly looks like this after forty, and you want it to look like this before summer,"

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ele pressiona a mão aberta no modelo da esquerda e a superfície afunda sob a palma. Ele tira a mão e bate duas vezes no modelo da direita, que não cede.

câmera: fixa

som ambiente: estacionamento aberto, com carros passando ao longe, sem música
```

### V02 · T1 · usa K02

```text
o avatar (homem) fala em inglês com sotaque americano de Jamie Anderson, voz autêntica, dinâmica, apaixonada e emocional, como se exigisse ser ouvida, a seguinte frase: "If your belly looks like this after forty, and you want it to look like this before summer,"

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ele risca com o marcador preto uma linha grossa acompanhando toda a curva do modelo da esquerda. Depois risca a mesma linha no modelo da direita, e ela sai bem menor.

câmera: fixa

som ambiente: estacionamento aberto, com carros passando ao longe, sem música
```

### V03 · T1 · usa K03

```text
o avatar (homem) fala em inglês com sotaque americano de Jamie Anderson, voz autêntica, dinâmica, apaixonada e emocional, como se exigisse ser ouvida, a seguinte frase: "If your belly looks like this after forty, and you want it to look like this before summer,"

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ele afunda a ponta do bastão na camada de esferas amarelas do modelo da esquerda, levanta o bastão e encosta a ponta no modelo da direita, que está limpo.

câmera: fixa

som ambiente: estacionamento aberto, com carros passando ao longe, sem música
```

### V04 · T1 · usa K04

```text
o avatar (homem) fala em inglês com sotaque americano de Jamie Anderson, voz autêntica, dinâmica, apaixonada e emocional, como se exigisse ser ouvida, a seguinte frase: "If your belly looks like this after forty, and you want it to look like this before summer,"

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ele encosta a ponta do bastão no tecido repuxado do manequim da esquerda e desliza a ponta até o vestido do manequim da direita, que cai reto.

câmera: fixa

som ambiente: estacionamento aberto, com carros passando ao longe, sem música
```

### V05 · T2 · usa K05

```text
o avatar (homem) fala em inglês com sotaque americano de Jamie Anderson, voz autêntica, dinâmica, apaixonada e emocional, como se exigisse ser ouvida, a seguinte frase: "it all starts with one simple ingredient, and most American women have never even heard of it. Comment yes, and don't forget to follow me."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ele fala olhando na câmera, com as duas mãos abertas acima do porta-malas, e no fim aponta o dedo para baixo, para o campo de comentário.

câmera: leve push-in

som ambiente: estacionamento aberto, com carros passando ao longe, sem música
```

### V06 · T2 · usa K06

```text
o avatar (homem) fala em inglês com sotaque americano de Jamie Anderson, voz autêntica, dinâmica, apaixonada e emocional, como se exigisse ser ouvida, a seguinte frase: "it all starts with one simple ingredient, and most American women have never even heard of it. Comment yes, and don't forget to follow me."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ele fala olhando na câmera, com as duas mãos abertas acima do porta-malas, e no fim aponta o dedo para baixo, para o campo de comentário.

câmera: leve push-in

som ambiente: estacionamento aberto, com carros passando ao longe, sem música
```

---

## Mapa de âncoras

| Keyframe | Referências a anexar | Modelo |
|---|---|---|
| K01 | `producao/_ancoras/jamie_anderson_ancora.jpeg` | Nano Banana 2, 9:16 |
| K02 | `producao/_ancoras/jamie_anderson_ancora.jpeg` | Nano Banana 2, 9:16 |
| K03 | `producao/_ancoras/jamie_anderson_ancora.jpeg` | Nano Banana 2, 9:16 |
| K04 | `producao/_ancoras/jamie_anderson_ancora.jpeg` | Nano Banana 2, 9:16 |
| K05 | `producao/_ancoras/jamie_anderson_ancora.jpeg` | Nano Banana 2, 9:16 |
| K06 | `producao/_ancoras/jamie_anderson_ancora.jpeg` | Nano Banana 2, 9:16 |
| V01 a V06 | o keyframe de mesmo número como INITIAL FRAME | Veo 3.1 Lite, Lower Priority, 8 s, 1 variação |

---

## Montagem no CapCut

1. **Quatro vídeos finalizados**, um por gancho. Cada um é o par do gancho com o take de CTA: V01 e V05, V02 e V05, V03 e V05, V04 e V06.
2. Cortar o clipe do gancho no fim da palavra `summer` e emendar direto no clipe de CTA. O modelo é take contínuo, então o corte tem que ser seco, sem transição e sem efeito.
3. Alvo de duração: **12 segundos**, cerca de 4 no gancho e 8 no CTA. Se o clipe de CTA vier mais longo, cortar no fim da palavra `me`.
4. **Legenda palavra por palavra**, branca, centralizada, na metade superior do quadro, exatamente como o modelo.
5. Sem música. O áudio do Veo já traz o ambiente do estacionamento.

---

## Gates de qualidade

1. A fala de cada prompt de vídeo bate **palavra por palavra** com o `ROTEIRO.md`.
2. T1 tem 18 palavras e T2 tem 25. Os dois dentro da faixa de 13 a 29.
3. Bandeirinha dos EUA presente e em foco no `scene` dos seis prompts de imagem.
4. `no captions, no subtitles, no words overlaid on the image` em todos os negatives, nunca `no text` seco.
5. Nenhum nome de órgão ou região do corpo no `negative` de nenhum prompt.
6. Herói no lower foreground, mais perto da lente que o rosto, nos seis keyframes.
7. O take de CTA é o mais fechado do vídeo.
8. Fundo descrito em dois blocos, não inventariado.
9. Luz neutra de dia, sem cast quente, em todos os prompts.
10. Zero travessão na copy e na entrega.
11. Keyword `yes`, nunca a palavra do vídeo original.
12. Avatar em PÉ no porta-malas nos dois takes, nunca sentado no banco do motorista.
13. Avatar como COACH. A copy não cobra esforço dela em nenhum ponto, e o crivo rodou duas vezes.
