# Jamie Voss | FityWell Growth Canela sobre o açúcar | Pacote de Prompts

Vídeo modelo: `input/reference_video.mp4` (James Smith, 26,2 s)

Âncora: `input/ancoras/05_jamie_voss.jpg`

Funil: growth, comentário `yes` + follow. Rodada de validação, gancho fiel ao modelo. Sem produto em quadro.

## Índice de geração

| Take | Keyframe | Anexar | Ação |
|---|---|---|---|
| T1 | K01 | ÂNCORA JAMIE VOSS + FRAME DO MODELO | GERAR DO ZERO |
| T2 | K02 | ÂNCORA JAMIE VOSS | GERAR DO ZERO |
| T3 | K03 | ÂNCORA JAMIE VOSS | GERAR DO ZERO |
| T4 | K04 | ÂNCORA JAMIE VOSS | GERAR DO ZERO |
| T5 | K05 | ÂNCORA JAMIE VOSS | GERAR DO ZERO |
| T6 | K06 | ÂNCORA JAMIE VOSS | GERAR DO ZERO |

Todo K é GERAR DO ZERO: o bloco do Flow é autossuficiente e cada K descreve o cenário inteiro, então não existe `EDITAR do K__` aqui.

## Trava de identidade e continuidade

- Identidade: The exact fictional AI character Jamie Voss, explicitly male: white American man around forty-six, fair skin, solid athletic build, blue-grey eyes, short brown hair under a beige cap worn backward, full brown beard with substantial grey and real forehead lines.
- Roupa: Beige cap backward, navy long-sleeve henley and jeans.
- Cenário do corpo: His own bright residential kitchen with a white-veined stone counter in front of him, cream upper cabinets and a black-framed window with a small American flag. The counter top is clear, with nothing on it except what he is using.
- Luz: Neutral overcast daylight from a window, the outside clearly visible through the window, soft even light on the face with no harsh shadows.
- Voz (igual em todos os V): voz grave e firme de um homem de quarenta e poucos anos, sotaque americano de um homem branco americano.
- Sem 2ª pessoa. O manequim do gancho é prop e não aparece do T2 em diante.

## Trava do prop herói

- Gancho: manequim feminino de plástico fosco sentado numa cadeira de escritório preta, camiseta cinza puxada até abaixo do peito, calça bege, barriga coberta por uma montanha alta de cubos de açúcar mascavo. Pote de canela transparente com tampa laranja, sem rótulo.
- Corpo: um copo reto de vidro transparente. Água limpa (T2), água turva de canela (T3), bebida âmbar (T4 a T6).

## Trava da 2ª pessoa (REF-A)

- Não se aplica: não há 2ª pessoa. O manequim é prop.

## Prompts de imagem

## K01 · T1 · GERAR DO ZERO · ÂNCORA JAMIE VOSS + FRAME DO MODELO

> ### 📎 ANEXAR: **2 IMAGENS**
> **1️⃣ ÂNCORA JAMIE VOSS** `input/ancoras/05_jamie_voss.jpg`
> **2️⃣ FRAME DO MODELO, só composição** `input/primeiro_frame_modelo.png`
>
> ### 🆕 GERAR DO ZERO

Cena: gancho, a montanha de açúcar.

```json
{
  "shot_id": "K01_gancho_jamie_voss",
  "reference_use": "Use the attached image only for Jamie Voss's exact identity, wardrobe and own setting. Do not copy its pose or framing. Use the second attached image only as a composition reference for where the seated mannequin, the sugar mound and the spice jar sit in the frame; do not copy its man, his clothes, cap, room or colors.",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "identity_main": "The exact fictional AI character Jamie Voss, explicitly male: white American man around forty-six, fair skin, solid athletic build, blue-grey eyes, short brown hair under a beige cap worn backward, full brown beard with substantial grey and real forehead lines.",
  "wardrobe": "Beige cap backward, navy long-sleeve henley and jeans.",
  "scene": "His own bright residential kitchen: the black office chair with the mannequin stands beside his white-veined stone counter, with cream upper cabinets and a black-framed window holding a small American flag behind them. The counter top is clear, with nothing else on it.",
  "prop": "A featureless female store mannequin of smooth matte plastic sits reclined in a black office chair, wearing a grey heather T-shirt pulled up to just under the chest and beige chinos. Covering its entire bare plastic belly is a THICK, TALL, HEAPED DOME of light brown raw cane sugar cubes, hundreds of small square lumps piled high with real 3D volume, so much that almost no plastic is visible under it. Jamie Voss holds a clear spice jar of ground cinnamon with a bright orange flip-top lid and no label, tilted over the top of the sugar dome, and a thin stream of cinnamon is starting to fall onto it.",
  "posture": "Jamie Voss stands just behind and to the right of the mannequin, leaning in over the sugar dome with the jar.",
  "composition": "The heaped sugar dome fills the lower third of the frame, very close to the lens, much closer to the camera than Jamie Voss's face. He is clear in the upper half. The mannequin's head and shoulders are cut off by the left edge of the frame. Nothing else competes with the sugar dome.",
  "camera": "phone camera at the height of the mannequin's belly, very close to the sugar dome, slight upward angle",
  "state": "Start frame: the first thin stream of cinnamon is just falling on top of the full, intact sugar dome. Jamie Voss is caught mid-sentence, lips naturally parted, animated expression.",
  "lighting": "Neutral overcast daylight from a window, the outside clearly visible through the window, soft even light on the face with no harsh shadows.",
  "realism": "Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday reality, background fully in focus, everything in sharp focus, no AI polish, no beauty smoothing.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no studio, no plastic-looking human skin, no extra fingers, no supernatural lighting, no blur, no bokeh, no artificial lighting, no warm orange color cast, no yellow tint, no golden glow, no golden hour light, no sunset, no de-aging, no beauty smoothing, no visible phone, no HDR, no cinematic lighting, no real human body, no thin scattered sugar layer, no flat sauce-like coating, no loose white granulated sugar"
}
```

## K02 · T2 · GERAR DO ZERO · ÂNCORA JAMIE VOSS

> ### 📎 ANEXAR: **1 IMAGEM**
> **1️⃣ ÂNCORA JAMIE VOSS** `input/ancoras/05_jamie_voss.jpg`
>
> ### 🆕 GERAR DO ZERO

Cena: colher de canela sobre o copo d'água.

```json
{
  "shot_id": "K02_t2_jamie_voss",
  "reference_use": "Use the attached image only for Jamie Voss's exact identity, wardrobe and own setting. Do not copy its pose or framing.",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "identity_main": "The exact fictional AI character Jamie Voss, explicitly male: white American man around forty-six, fair skin, solid athletic build, blue-grey eyes, short brown hair under a beige cap worn backward, full brown beard with substantial grey and real forehead lines.",
  "wardrobe": "Beige cap backward, navy long-sleeve henley and jeans.",
  "scene": "His own bright residential kitchen with a white-veined stone counter in front of him, cream upper cabinets and a black-framed window with a small American flag. The counter top is clear, with nothing on it except what he is using.",
  "prop": "A clear straight drinking glass of plain water stands on the white-veined stone counter in the lower foreground, very close to the lens, larger in frame than his hands. Jamie Voss holds a metal teaspoon heaped with ground cinnamon toward the camera, just above the glass.",
  "posture": "Jamie Voss is leaning on the counter with his forearms, toward the camera.",
  "composition": "From the chest up, Jamie Voss's face clear in the upper half, the glass in the lower foreground closer to the camera than his face. The background is reduced by framing, never by blur.",
  "camera": "phone camera at chest height, straight on, fixed",
  "state": "Start frame: Jamie Voss shows the heaped spoon of cinnamon to the camera, caught mid-sentence, lips naturally parted, animated expression.",
  "lighting": "Neutral overcast daylight from a window, the outside clearly visible through the window, soft even light on the face with no harsh shadows.",
  "realism": "Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday reality, background fully in focus, everything in sharp focus, no AI polish, no beauty smoothing.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no studio, no plastic-looking human skin, no extra fingers, no supernatural lighting, no blur, no bokeh, no artificial lighting, no warm orange color cast, no yellow tint, no golden glow, no golden hour light, no sunset, no de-aging, no beauty smoothing, no visible phone, no HDR, no cinematic lighting, no mannequin in frame, no second person in frame"
}
```

## K03 · T3 · GERAR DO ZERO · ÂNCORA JAMIE VOSS

> ### 📎 ANEXAR: **1 IMAGEM**
> **1️⃣ ÂNCORA JAMIE VOSS** `input/ancoras/05_jamie_voss.jpg`
>
> ### 🆕 GERAR DO ZERO

Cena: limão espremido no copo.

```json
{
  "shot_id": "K03_t3_jamie_voss",
  "reference_use": "Use the attached image only for Jamie Voss's exact identity, wardrobe and own setting. Do not copy its pose or framing.",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "identity_main": "The exact fictional AI character Jamie Voss, explicitly male: white American man around forty-six, fair skin, solid athletic build, blue-grey eyes, short brown hair under a beige cap worn backward, full brown beard with substantial grey and real forehead lines.",
  "wardrobe": "Beige cap backward, navy long-sleeve henley and jeans.",
  "scene": "His own bright residential kitchen with a white-veined stone counter in front of him, cream upper cabinets and a black-framed window with a small American flag. The counter top is clear, with nothing on it except what he is using.",
  "prop": "A clear straight drinking glass of cloudy light brown cinnamon water stands on the white-veined stone counter in the lower foreground, very close to the lens. Jamie Voss holds half a fresh yellow lemon in one hand right above the glass, squeezing it.",
  "posture": "Jamie Voss is leaning on the counter with his forearms, toward the camera.",
  "composition": "From the chest up, Jamie Voss's face clear in the upper half, the glass in the lower foreground closer to the camera than his face. The background is reduced by framing, never by blur.",
  "camera": "phone camera at chest height, straight on, fixed",
  "state": "Start frame: the first drops of lemon juice are falling into the glass, Jamie Voss is caught mid-sentence, lips naturally parted, animated expression.",
  "lighting": "Neutral overcast daylight from a window, the outside clearly visible through the window, soft even light on the face with no harsh shadows.",
  "realism": "Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday reality, background fully in focus, everything in sharp focus, no AI polish, no beauty smoothing.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no studio, no plastic-looking human skin, no extra fingers, no supernatural lighting, no blur, no bokeh, no artificial lighting, no warm orange color cast, no yellow tint, no golden glow, no golden hour light, no sunset, no de-aging, no beauty smoothing, no visible phone, no HDR, no cinematic lighting, no mannequin in frame, no second person in frame"
}
```

## K04 · T4 · GERAR DO ZERO · ÂNCORA JAMIE VOSS

> ### 📎 ANEXAR: **1 IMAGEM**
> **1️⃣ ÂNCORA JAMIE VOSS** `input/ancoras/05_jamie_voss.jpg`
>
> ### 🆕 GERAR DO ZERO

Cena: fio de mel no copo.

```json
{
  "shot_id": "K04_t4_jamie_voss",
  "reference_use": "Use the attached image only for Jamie Voss's exact identity, wardrobe and own setting. Do not copy its pose or framing.",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "identity_main": "The exact fictional AI character Jamie Voss, explicitly male: white American man around forty-six, fair skin, solid athletic build, blue-grey eyes, short brown hair under a beige cap worn backward, full brown beard with substantial grey and real forehead lines.",
  "wardrobe": "Beige cap backward, navy long-sleeve henley and jeans.",
  "scene": "His own bright residential kitchen with a white-veined stone counter in front of him, cream upper cabinets and a black-framed window with a small American flag. The counter top is clear, with nothing on it except what he is using.",
  "prop": "A clear straight drinking glass of cloudy amber drink stands on the white-veined stone counter in the lower foreground, very close to the lens. Jamie Voss holds a metal tablespoon of thick amber raw honey right above the glass.",
  "posture": "Jamie Voss is leaning on the counter with his forearms, toward the camera.",
  "composition": "From the chest up, Jamie Voss's face clear in the upper half, the glass in the lower foreground closer to the camera than his face. The background is reduced by framing, never by blur.",
  "camera": "phone camera at chest height, straight on, fixed",
  "state": "Start frame: a thick thread of honey is starting to fall from the spoon into the glass, Jamie Voss is caught mid-sentence, lips naturally parted, animated expression.",
  "lighting": "Neutral overcast daylight from a window, the outside clearly visible through the window, soft even light on the face with no harsh shadows.",
  "realism": "Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday reality, background fully in focus, everything in sharp focus, no AI polish, no beauty smoothing.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no studio, no plastic-looking human skin, no extra fingers, no supernatural lighting, no blur, no bokeh, no artificial lighting, no warm orange color cast, no yellow tint, no golden glow, no golden hour light, no sunset, no de-aging, no beauty smoothing, no visible phone, no HDR, no cinematic lighting, no mannequin in frame, no second person in frame"
}
```

## K05 · T5 · GERAR DO ZERO · ÂNCORA JAMIE VOSS

> ### 📎 ANEXAR: **1 IMAGEM**
> **1️⃣ ÂNCORA JAMIE VOSS** `input/ancoras/05_jamie_voss.jpg`
>
> ### 🆕 GERAR DO ZERO

Cena: segurando o copo pronto.

```json
{
  "shot_id": "K05_t5_jamie_voss",
  "reference_use": "Use the attached image only for Jamie Voss's exact identity, wardrobe and own setting. Do not copy its pose or framing.",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "identity_main": "The exact fictional AI character Jamie Voss, explicitly male: white American man around forty-six, fair skin, solid athletic build, blue-grey eyes, short brown hair under a beige cap worn backward, full brown beard with substantial grey and real forehead lines.",
  "wardrobe": "Beige cap backward, navy long-sleeve henley and jeans.",
  "scene": "His own bright residential kitchen with a white-veined stone counter in front of him, cream upper cabinets and a black-framed window with a small American flag. The counter top is clear, with nothing on it except what he is using.",
  "prop": "Jamie Voss holds the clear straight drinking glass of cloudy amber-brown drink with both hands at chest height, very close to the lens, the glass in the lower foreground.",
  "posture": "Jamie Voss is leaning on the counter with his forearms, toward the camera.",
  "composition": "From the chest up, Jamie Voss's face clear in the upper half, the glass in the lower foreground closer to the camera than his face. The background is reduced by framing, never by blur.",
  "camera": "phone camera at chest height, straight on, fixed",
  "state": "Start frame: Jamie Voss looks into the lens holding the glass, caught mid-sentence, lips naturally parted, animated expression.",
  "lighting": "Neutral overcast daylight from a window, the outside clearly visible through the window, soft even light on the face with no harsh shadows.",
  "realism": "Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday reality, background fully in focus, everything in sharp focus, no AI polish, no beauty smoothing.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no studio, no plastic-looking human skin, no extra fingers, no supernatural lighting, no blur, no bokeh, no artificial lighting, no warm orange color cast, no yellow tint, no golden glow, no golden hour light, no sunset, no de-aging, no beauty smoothing, no visible phone, no HDR, no cinematic lighting, no mannequin in frame, no second person in frame"
}
```

## K06 · T6 · GERAR DO ZERO · ÂNCORA JAMIE VOSS

> ### 📎 ANEXAR: **1 IMAGEM**
> **1️⃣ ÂNCORA JAMIE VOSS** `input/ancoras/05_jamie_voss.jpg`
>
> ### 🆕 GERAR DO ZERO

Cena: segurando o copo, plano mais fechado.

```json
{
  "shot_id": "K06_t6_jamie_voss",
  "reference_use": "Use the attached image only for Jamie Voss's exact identity, wardrobe and own setting. Do not copy its pose or framing.",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "identity_main": "The exact fictional AI character Jamie Voss, explicitly male: white American man around forty-six, fair skin, solid athletic build, blue-grey eyes, short brown hair under a beige cap worn backward, full brown beard with substantial grey and real forehead lines.",
  "wardrobe": "Beige cap backward, navy long-sleeve henley and jeans.",
  "scene": "His own bright residential kitchen with a white-veined stone counter in front of him, cream upper cabinets and a black-framed window with a small American flag. The counter top is clear, with nothing on it except what he is using.",
  "prop": "Jamie Voss holds the clear straight drinking glass of cloudy amber-brown drink with both hands at chest height, very close to the lens, the glass in the lower foreground.",
  "posture": "Jamie Voss is leaning on the counter with his forearms, toward the camera.",
  "composition": "Tightest shot of the video: from the upper chest up, Jamie Voss's face clear in the upper half, the glass in the lower foreground closer to the camera than his face. The background is reduced by framing, never by blur.",
  "camera": "phone camera at chest height, straight on, fixed",
  "state": "Start frame: Jamie Voss leans a little toward the lens holding the glass, caught mid-sentence, lips naturally parted, animated expression.",
  "lighting": "Neutral overcast daylight from a window, the outside clearly visible through the window, soft even light on the face with no harsh shadows.",
  "realism": "Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday reality, background fully in focus, everything in sharp focus, no AI polish, no beauty smoothing.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no studio, no plastic-looking human skin, no extra fingers, no supernatural lighting, no blur, no bokeh, no artificial lighting, no warm orange color cast, no yellow tint, no golden glow, no golden hour light, no sunset, no de-aging, no beauty smoothing, no visible phone, no HDR, no cinematic lighting, no mannequin in frame, no second person in frame"
}
```

## Bloco global de vídeo

```text
o avatar Jamie Voss, homem, fala em inglês com sotaque americano de um homem branco americano, voz grave e firme de um homem de quarenta e poucos anos, [emoção da fala], voz autêntica, como se exigisse ser ouvido, a seguinte frase: "[FALA EXATA DO ROTEIRO]"

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: [ação enxuta]

câmera: [fixa]

som ambiente: cozinha residencial tranquila, sem música
```

# Prompts de vídeo

### V01 · T1 · usa K01

```text
o avatar Jamie Voss, homem, fala em inglês com sotaque americano de um homem branco americano, voz grave e firme de um homem de quarenta e poucos anos, entonação animada e intrigada, sorrindo, como quem mostra algo surpreendente, voz autêntica, como se exigisse ser ouvido, a seguinte frase: "This is what cinnamon does to the sugar in your body."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Jamie Voss inclina o pote e a canela cai em fio sobre a montanha de cubos de açúcar; perto do fim da frase a montanha inteira desaba para os lados e os cubos rolam para fora da barriga do manequim, revelando a barriga lisa de plástico polvilhada de canela; ele olha o resultado e sorri.

câmera: fixa, leve handheld

som ambiente: cozinha residencial tranquila, som dos cubos de açúcar caindo, sem música
```

### V02 · T2 · usa K02

```text
o avatar Jamie Voss, homem, fala em inglês com sotaque americano de um homem branco americano, voz grave e firme de um homem de quarenta e poucos anos, entonação animada e didática, sorrindo, voz autêntica, como se exigisse ser ouvido, a seguinte frase: "In a glass, mix one teaspoon of cinnamon,"

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Jamie Voss mostra a colher cheia de canela para a câmera e depois mexe a canela dentro do copo d'água. Ele diz a frase em ritmo natural logo no começo e continua mexendo em silêncio até o fim.

câmera: fixa

som ambiente: cozinha residencial tranquila, sem música
```

### V03 · T3 · usa K03

```text
o avatar Jamie Voss, homem, fala em inglês com sotaque americano de um homem branco americano, voz grave e firme de um homem de quarenta e poucos anos, entonação animada e didática, voz autêntica, como se exigisse ser ouvido, a seguinte frase: "a squeeze of fresh lemon juice,"

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Jamie Voss espreme o meio limão e o suco cai dentro do copo. Ele diz a frase em ritmo natural logo no começo e continua espremendo em silêncio até o fim.

câmera: fixa

som ambiente: cozinha residencial tranquila, sem música
```

### V04 · T4 · usa K04

```text
o avatar Jamie Voss, homem, fala em inglês com sotaque americano de um homem branco americano, voz grave e firme de um homem de quarenta e poucos anos, entonação animada e didática, sorrindo, voz autêntica, como se exigisse ser ouvido, a seguinte frase: "and one tablespoon of raw honey."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: o fio grosso de mel escorre da colher para dentro do copo. Jamie Voss diz a frase em ritmo natural logo no começo e continua despejando o mel em silêncio até o fim.

câmera: fixa

som ambiente: cozinha residencial tranquila, sem música
```

### V05 · T5 · usa K05

```text
o avatar Jamie Voss, homem, fala em inglês com sotaque americano de um homem branco americano, voz grave e firme de um homem de quarenta e poucos anos, entonação confiante e calorosa, voz autêntica, como se exigisse ser ouvido, a seguinte frase: "Drink this every morning on an empty stomach and your energy starts coming back and your clothes start fitting better."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Jamie Voss segura o copo com as duas mãos na altura do peito e fala para a câmera, com pequenos movimentos naturais.

câmera: fixa

som ambiente: cozinha residencial tranquila, sem música
```

### V06 · T6 · usa K06

```text
o avatar Jamie Voss, homem, fala em inglês com sotaque americano de um homem branco americano, voz grave e firme de um homem de quarenta e poucos anos, entonação animada e convidativa, voz autêntica, como se exigisse ser ouvido, a seguinte frase: "And comment yes, and I will send you one more ingredient that makes this ten times more powerful. And follow me so that I can reach you."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Jamie Voss segura o copo com as duas mãos, se inclina um pouco para a câmera e fala direto com ela, sorrindo no fim.

câmera: fixa

som ambiente: cozinha residencial tranquila, sem música
```

## Mapa de âncoras

| Keyframe | Referências a anexar | Modelo |
|---|---|---|
| K01 | ÂNCORA JAMIE VOSS + FRAME DO MODELO (`input/primeiro_frame_modelo.png`, só composição) | Nano Banana 2, 9:16 |
| K02 a K06 | ÂNCORA JAMIE VOSS | Nano Banana 2, 9:16 |

## Montagem no CapCut

1. Clipes numerados na ordem: V01, V02, V03, V04, V05, V06.
2. Cortar cada clipe no tempo da cena do modelo: T1 0,0 a 4,0 s; T2 4,0 a 7,8 s; T3 7,8 a 10,1 s; T4 10,1 a 12,6 s; T5 12,6 a 18,6 s; T6 18,6 a 26,2 s.
3. Zero tempo morto: todo clipe começa já falando. Isolate Voice / Keep Vocal no áudio.
4. Nos clipes de cena curta (V01 a V04) a fala vem no começo; cortar logo depois da última palavra, no tempo da cena.
5. Legenda palavra a palavra com destaque amarelo, igual ao modelo. `yes` isolado na tela no T6.
6. Sem Voice Changer: a voz vem do prompt de cada V.
7. Música só no corpo (V02 em diante), nunca no gancho, entre -19 e -20 dB, fora da biblioteca do TikTok.
8. Rótulo pequeno `AI-generated` num canto do vídeo.

## Gates de qualidade

1. Fala de cada V igual ao ROTEIRO, palavra por palavra.
2. Um take por cena do modelo; T1 a T4 marcados CENA CURTA; nenhum take acima de 29 palavras.
3. Bandeira dos EUA no campo scene de todo K.
4. Zero travessão.
5. Keyword `yes` no T6.
6. Produto fora de quadro.
7. Negative sem termo sensível.
8. GATE_VISUAL Partes 1 a 3 em todo K: herói colado na lente, luz neutra, sem tom quente, sem blur, trecho de realismo.
9. Gancho fiel no conteúdo: canela sobre a montanha de cubos de açúcar que desaba e revela a barriga lisa.
10. Um K = um V, e o reveal do gancho é uma imagem só, do estado inicial.

