# Eva Dall | FityWell Growth Canela sobre o açúcar | Pacote de Prompts

Vídeo modelo: `input/reference_video.mp4` (James Smith, 26,2 s)

Âncora: `input/ancoras/02_eva_dall.jpg`

Funil: growth, comentário `yes` + follow. Rodada de validação, gancho fiel ao modelo. Sem produto em quadro.

## Índice de geração

| Take | Keyframe | Anexar | Ação |
|---|---|---|---|
| T1 | K01 | ÂNCORA EVA DALL + FRAME DO MODELO | GERAR DO ZERO |
| T2 | K02 | ÂNCORA EVA DALL | GERAR DO ZERO |
| T3 | K03 | ÂNCORA EVA DALL | GERAR DO ZERO |
| T4 | K04 | ÂNCORA EVA DALL | GERAR DO ZERO |
| T5 | K05 | ÂNCORA EVA DALL | GERAR DO ZERO |
| T6 | K06 | ÂNCORA EVA DALL | GERAR DO ZERO |

Todo K é GERAR DO ZERO: o bloco do Flow é autossuficiente e cada K descreve o cenário inteiro, então não existe `EDITAR do K__` aqui.

## Trava de identidade e continuidade

- Identidade: The exact fictional AI character Eva Dall, explicitly male: Black American man around forty-nine, medium brown skin, lean athletic build, long oval face, dark brown eyes, subtle freckles and moles, very long locs mixing black, grey and silver, grey goatee and moustache, brown leather cap worn backward.
- Roupa: White ribbed tank top and a thin silver chain.
- Cenário do corpo: His own modern white kitchen with a strongly veined dark green marble counter in front of him, tall windows to the right and a small American flag on the shelf beside a small plant.
- Luz: Neutral overcast daylight from a window, the outside clearly visible through the window, soft even light on the face with no harsh shadows.
- Voz (igual em todos os V): voz média e amigável de um homem de quase cinquenta anos, sotaque americano de um homem negro americano.
- Sem 2ª pessoa. O manequim do gancho é prop e não aparece do T2 em diante.

## Trava do prop herói

- Gancho: manequim feminino de plástico fosco sentado numa cadeira de escritório preta, camiseta cinza puxada até abaixo do peito, calça bege, barriga coberta por uma montanha alta de cubos de açúcar mascavo. Pote de canela transparente com tampa laranja, sem rótulo.
- Corpo: um copo reto de vidro transparente. Água limpa (T2), água turva de canela (T3), bebida âmbar (T4 a T6).

## Trava da 2ª pessoa (REF-A)

- Não se aplica: não há 2ª pessoa. O manequim é prop.

## Prompts de imagem

## K01 · T1 · GERAR DO ZERO · ÂNCORA EVA DALL + FRAME DO MODELO

> ### 📎 ANEXAR: **2 IMAGENS**
> **1️⃣ ÂNCORA EVA DALL** `input/ancoras/02_eva_dall.jpg`
> **2️⃣ FRAME DO MODELO, só composição** `input/primeiro_frame_modelo.png`
>
> ### 🆕 GERAR DO ZERO

Cena: gancho, a montanha de açúcar.

```json
{
  "shot_id": "K01_gancho_eva_dall",
  "reference_use": "Use the attached image only for Eva Dall's exact identity, wardrobe and own setting. Do not copy its pose or framing. Use the second attached image only as a composition reference for where the seated mannequin, the sugar mound and the spice jar sit in the frame; do not copy its man, his clothes, cap, room or colors.",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "identity_main": "The exact fictional AI character Eva Dall, explicitly male: Black American man around forty-nine, medium brown skin, lean athletic build, long oval face, dark brown eyes, subtle freckles and moles, very long locs mixing black, grey and silver, grey goatee and moustache, brown leather cap worn backward.",
  "wardrobe": "White ribbed tank top and a thin silver chain.",
  "scene": "His own modern white kitchen: the black office chair with the mannequin stands beside his dark green veined marble counter, with tall windows and a small plant beside a small American flag behind them.",
  "prop": "A featureless female store mannequin of smooth matte plastic sits reclined in a black office chair, wearing a grey heather T-shirt pulled up to just under the chest and beige chinos. Covering its entire bare plastic belly is a THICK, TALL, HEAPED DOME of light brown raw cane sugar cubes, hundreds of small square lumps piled high with real 3D volume, so much that almost no plastic is visible under it. Eva Dall holds a clear spice jar of ground cinnamon with a bright orange flip-top lid and no label, tilted over the top of the sugar dome, and a thin stream of cinnamon is starting to fall onto it.",
  "posture": "Eva Dall stands just behind and to the right of the mannequin, leaning in over the sugar dome with the jar.",
  "composition": "The heaped sugar dome fills the lower third of the frame, very close to the lens, much closer to the camera than Eva Dall's face. He is clear in the upper half. The mannequin's head and shoulders are cut off by the left edge of the frame. Nothing else competes with the sugar dome.",
  "camera": "phone camera at the height of the mannequin's belly, very close to the sugar dome, slight upward angle",
  "state": "Start frame: the first thin stream of cinnamon is just falling on top of the full, intact sugar dome. Eva Dall is caught mid-sentence, lips naturally parted, animated expression.",
  "lighting": "Neutral overcast daylight from a window, the outside clearly visible through the window, soft even light on the face with no harsh shadows.",
  "realism": "Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday reality, background fully in focus, everything in sharp focus, no AI polish, no beauty smoothing.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no studio, no plastic-looking human skin, no extra fingers, no supernatural lighting, no blur, no bokeh, no artificial lighting, no warm orange color cast, no yellow tint, no golden glow, no golden hour light, no sunset, no de-aging, no beauty smoothing, no visible phone, no HDR, no cinematic lighting, no real human body, no thin scattered sugar layer, no flat sauce-like coating, no loose white granulated sugar"
}
```

## K02 · T2 · GERAR DO ZERO · ÂNCORA EVA DALL

> ### 📎 ANEXAR: **1 IMAGEM**
> **1️⃣ ÂNCORA EVA DALL** `input/ancoras/02_eva_dall.jpg`
>
> ### 🆕 GERAR DO ZERO

Cena: colher de canela sobre o copo d'água.

```json
{
  "shot_id": "K02_t2_eva_dall",
  "reference_use": "Use the attached image only for Eva Dall's exact identity, wardrobe and own setting. Do not copy its pose or framing.",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "identity_main": "The exact fictional AI character Eva Dall, explicitly male: Black American man around forty-nine, medium brown skin, lean athletic build, long oval face, dark brown eyes, subtle freckles and moles, very long locs mixing black, grey and silver, grey goatee and moustache, brown leather cap worn backward.",
  "wardrobe": "White ribbed tank top and a thin silver chain.",
  "scene": "His own modern white kitchen with a strongly veined dark green marble counter in front of him, tall windows to the right and a small American flag on the shelf beside a small plant.",
  "prop": "A clear straight drinking glass of plain water stands on the dark green veined marble counter in the lower foreground, very close to the lens, larger in frame than his hands. Eva Dall holds a metal teaspoon heaped with ground cinnamon toward the camera, just above the glass.",
  "posture": "Eva Dall is standing behind his counter, both forearms near the counter, leaning slightly toward the camera.",
  "composition": "From the chest up, Eva Dall's face clear in the upper half, the glass in the lower foreground closer to the camera than his face. The background is reduced by framing, never by blur.",
  "camera": "phone camera at chest height, straight on, fixed",
  "state": "Start frame: Eva Dall shows the heaped spoon of cinnamon to the camera, caught mid-sentence, lips naturally parted, animated expression.",
  "lighting": "Neutral overcast daylight from a window, the outside clearly visible through the window, soft even light on the face with no harsh shadows.",
  "realism": "Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday reality, background fully in focus, everything in sharp focus, no AI polish, no beauty smoothing.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no studio, no plastic-looking human skin, no extra fingers, no supernatural lighting, no blur, no bokeh, no artificial lighting, no warm orange color cast, no yellow tint, no golden glow, no golden hour light, no sunset, no de-aging, no beauty smoothing, no visible phone, no HDR, no cinematic lighting, no mannequin in frame, no second person in frame"
}
```

## K03 · T3 · GERAR DO ZERO · ÂNCORA EVA DALL

> ### 📎 ANEXAR: **1 IMAGEM**
> **1️⃣ ÂNCORA EVA DALL** `input/ancoras/02_eva_dall.jpg`
>
> ### 🆕 GERAR DO ZERO

Cena: limão espremido no copo.

```json
{
  "shot_id": "K03_t3_eva_dall",
  "reference_use": "Use the attached image only for Eva Dall's exact identity, wardrobe and own setting. Do not copy its pose or framing.",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "identity_main": "The exact fictional AI character Eva Dall, explicitly male: Black American man around forty-nine, medium brown skin, lean athletic build, long oval face, dark brown eyes, subtle freckles and moles, very long locs mixing black, grey and silver, grey goatee and moustache, brown leather cap worn backward.",
  "wardrobe": "White ribbed tank top and a thin silver chain.",
  "scene": "His own modern white kitchen with a strongly veined dark green marble counter in front of him, tall windows to the right and a small American flag on the shelf beside a small plant.",
  "prop": "A clear straight drinking glass of cloudy light brown cinnamon water stands on the dark green veined marble counter in the lower foreground, very close to the lens. Eva Dall holds half a fresh yellow lemon in one hand right above the glass, squeezing it.",
  "posture": "Eva Dall is standing behind his counter, both forearms near the counter, leaning slightly toward the camera.",
  "composition": "From the chest up, Eva Dall's face clear in the upper half, the glass in the lower foreground closer to the camera than his face. The background is reduced by framing, never by blur.",
  "camera": "phone camera at chest height, straight on, fixed",
  "state": "Start frame: the first drops of lemon juice are falling into the glass, Eva Dall is caught mid-sentence, lips naturally parted, animated expression.",
  "lighting": "Neutral overcast daylight from a window, the outside clearly visible through the window, soft even light on the face with no harsh shadows.",
  "realism": "Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday reality, background fully in focus, everything in sharp focus, no AI polish, no beauty smoothing.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no studio, no plastic-looking human skin, no extra fingers, no supernatural lighting, no blur, no bokeh, no artificial lighting, no warm orange color cast, no yellow tint, no golden glow, no golden hour light, no sunset, no de-aging, no beauty smoothing, no visible phone, no HDR, no cinematic lighting, no mannequin in frame, no second person in frame"
}
```

## K04 · T4 · GERAR DO ZERO · ÂNCORA EVA DALL

> ### 📎 ANEXAR: **1 IMAGEM**
> **1️⃣ ÂNCORA EVA DALL** `input/ancoras/02_eva_dall.jpg`
>
> ### 🆕 GERAR DO ZERO

Cena: fio de mel no copo.

```json
{
  "shot_id": "K04_t4_eva_dall",
  "reference_use": "Use the attached image only for Eva Dall's exact identity, wardrobe and own setting. Do not copy its pose or framing.",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "identity_main": "The exact fictional AI character Eva Dall, explicitly male: Black American man around forty-nine, medium brown skin, lean athletic build, long oval face, dark brown eyes, subtle freckles and moles, very long locs mixing black, grey and silver, grey goatee and moustache, brown leather cap worn backward.",
  "wardrobe": "White ribbed tank top and a thin silver chain.",
  "scene": "His own modern white kitchen with a strongly veined dark green marble counter in front of him, tall windows to the right and a small American flag on the shelf beside a small plant.",
  "prop": "A clear straight drinking glass of cloudy amber drink stands on the dark green veined marble counter in the lower foreground, very close to the lens. Eva Dall holds a metal tablespoon of thick amber raw honey right above the glass.",
  "posture": "Eva Dall is standing behind his counter, both forearms near the counter, leaning slightly toward the camera.",
  "composition": "From the chest up, Eva Dall's face clear in the upper half, the glass in the lower foreground closer to the camera than his face. The background is reduced by framing, never by blur.",
  "camera": "phone camera at chest height, straight on, fixed",
  "state": "Start frame: a thick thread of honey is starting to fall from the spoon into the glass, Eva Dall is caught mid-sentence, lips naturally parted, animated expression.",
  "lighting": "Neutral overcast daylight from a window, the outside clearly visible through the window, soft even light on the face with no harsh shadows.",
  "realism": "Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday reality, background fully in focus, everything in sharp focus, no AI polish, no beauty smoothing.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no studio, no plastic-looking human skin, no extra fingers, no supernatural lighting, no blur, no bokeh, no artificial lighting, no warm orange color cast, no yellow tint, no golden glow, no golden hour light, no sunset, no de-aging, no beauty smoothing, no visible phone, no HDR, no cinematic lighting, no mannequin in frame, no second person in frame"
}
```

## K05 · T5 · GERAR DO ZERO · ÂNCORA EVA DALL

> ### 📎 ANEXAR: **1 IMAGEM**
> **1️⃣ ÂNCORA EVA DALL** `input/ancoras/02_eva_dall.jpg`
>
> ### 🆕 GERAR DO ZERO

Cena: segurando o copo pronto.

```json
{
  "shot_id": "K05_t5_eva_dall",
  "reference_use": "Use the attached image only for Eva Dall's exact identity, wardrobe and own setting. Do not copy its pose or framing.",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "identity_main": "The exact fictional AI character Eva Dall, explicitly male: Black American man around forty-nine, medium brown skin, lean athletic build, long oval face, dark brown eyes, subtle freckles and moles, very long locs mixing black, grey and silver, grey goatee and moustache, brown leather cap worn backward.",
  "wardrobe": "White ribbed tank top and a thin silver chain.",
  "scene": "His own modern white kitchen with a strongly veined dark green marble counter in front of him, tall windows to the right and a small American flag on the shelf beside a small plant.",
  "prop": "Eva Dall holds the clear straight drinking glass of cloudy amber-brown drink with both hands at chest height, very close to the lens, the glass in the lower foreground.",
  "posture": "Eva Dall is standing behind his counter, both forearms near the counter, leaning slightly toward the camera.",
  "composition": "From the chest up, Eva Dall's face clear in the upper half, the glass in the lower foreground closer to the camera than his face. The background is reduced by framing, never by blur.",
  "camera": "phone camera at chest height, straight on, fixed",
  "state": "Start frame: Eva Dall looks into the lens holding the glass, caught mid-sentence, lips naturally parted, animated expression.",
  "lighting": "Neutral overcast daylight from a window, the outside clearly visible through the window, soft even light on the face with no harsh shadows.",
  "realism": "Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday reality, background fully in focus, everything in sharp focus, no AI polish, no beauty smoothing.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no studio, no plastic-looking human skin, no extra fingers, no supernatural lighting, no blur, no bokeh, no artificial lighting, no warm orange color cast, no yellow tint, no golden glow, no golden hour light, no sunset, no de-aging, no beauty smoothing, no visible phone, no HDR, no cinematic lighting, no mannequin in frame, no second person in frame"
}
```

## K06 · T6 · GERAR DO ZERO · ÂNCORA EVA DALL

> ### 📎 ANEXAR: **1 IMAGEM**
> **1️⃣ ÂNCORA EVA DALL** `input/ancoras/02_eva_dall.jpg`
>
> ### 🆕 GERAR DO ZERO

Cena: segurando o copo, plano mais fechado.

```json
{
  "shot_id": "K06_t6_eva_dall",
  "reference_use": "Use the attached image only for Eva Dall's exact identity, wardrobe and own setting. Do not copy its pose or framing.",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "identity_main": "The exact fictional AI character Eva Dall, explicitly male: Black American man around forty-nine, medium brown skin, lean athletic build, long oval face, dark brown eyes, subtle freckles and moles, very long locs mixing black, grey and silver, grey goatee and moustache, brown leather cap worn backward.",
  "wardrobe": "White ribbed tank top and a thin silver chain.",
  "scene": "His own modern white kitchen with a strongly veined dark green marble counter in front of him, tall windows to the right and a small American flag on the shelf beside a small plant.",
  "prop": "Eva Dall holds the clear straight drinking glass of cloudy amber-brown drink with both hands at chest height, very close to the lens, the glass in the lower foreground.",
  "posture": "Eva Dall is standing behind his counter, both forearms near the counter, leaning slightly toward the camera.",
  "composition": "Tightest shot of the video: from the upper chest up, Eva Dall's face clear in the upper half, the glass in the lower foreground closer to the camera than his face. The background is reduced by framing, never by blur.",
  "camera": "phone camera at chest height, straight on, fixed",
  "state": "Start frame: Eva Dall leans a little toward the lens holding the glass, caught mid-sentence, lips naturally parted, animated expression.",
  "lighting": "Neutral overcast daylight from a window, the outside clearly visible through the window, soft even light on the face with no harsh shadows.",
  "realism": "Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday reality, background fully in focus, everything in sharp focus, no AI polish, no beauty smoothing.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no studio, no plastic-looking human skin, no extra fingers, no supernatural lighting, no blur, no bokeh, no artificial lighting, no warm orange color cast, no yellow tint, no golden glow, no golden hour light, no sunset, no de-aging, no beauty smoothing, no visible phone, no HDR, no cinematic lighting, no mannequin in frame, no second person in frame"
}
```

## Bloco global de vídeo

```text
o avatar Eva Dall, homem, fala em inglês com sotaque americano de um homem negro americano, voz média e amigável de um homem de quase cinquenta anos, [emoção da fala], voz autêntica, como se exigisse ser ouvido, a seguinte frase: "[FALA EXATA DO ROTEIRO]"

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: [ação enxuta]

câmera: [fixa]

som ambiente: cozinha residencial tranquila, sem música
```

# Prompts de vídeo

### V01 · T1 · usa K01

```text
o avatar Eva Dall, homem, fala em inglês com sotaque americano de um homem negro americano, voz média e amigável de um homem de quase cinquenta anos, entonação animada e intrigada, sorrindo, como quem mostra algo surpreendente, voz autêntica, como se exigisse ser ouvido, a seguinte frase: "This is what cinnamon does to the sugar in your body."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Eva Dall inclina o pote e a canela cai em fio sobre a montanha de cubos de açúcar; perto do fim da frase a montanha inteira desaba para os lados e os cubos rolam para fora da barriga do manequim, revelando a barriga lisa de plástico polvilhada de canela; ele olha o resultado e sorri.

câmera: fixa, leve handheld

som ambiente: cozinha residencial tranquila, som dos cubos de açúcar caindo, sem música
```

### V02 · T2 · usa K02

```text
o avatar Eva Dall, homem, fala em inglês com sotaque americano de um homem negro americano, voz média e amigável de um homem de quase cinquenta anos, entonação animada e didática, sorrindo, voz autêntica, como se exigisse ser ouvido, a seguinte frase: "In a glass, mix one teaspoon of cinnamon,"

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Eva Dall mostra a colher cheia de canela para a câmera e depois mexe a canela dentro do copo d'água. Ele diz a frase em ritmo natural logo no começo e continua mexendo em silêncio até o fim.

câmera: fixa

som ambiente: cozinha residencial tranquila, sem música
```

### V03 · T3 · usa K03

```text
o avatar Eva Dall, homem, fala em inglês com sotaque americano de um homem negro americano, voz média e amigável de um homem de quase cinquenta anos, entonação animada e didática, voz autêntica, como se exigisse ser ouvido, a seguinte frase: "a squeeze of fresh lemon juice,"

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Eva Dall espreme o meio limão e o suco cai dentro do copo. Ele diz a frase em ritmo natural logo no começo e continua espremendo em silêncio até o fim.

câmera: fixa

som ambiente: cozinha residencial tranquila, sem música
```

### V04 · T4 · usa K04

```text
o avatar Eva Dall, homem, fala em inglês com sotaque americano de um homem negro americano, voz média e amigável de um homem de quase cinquenta anos, entonação animada e didática, sorrindo, voz autêntica, como se exigisse ser ouvido, a seguinte frase: "and one tablespoon of raw honey."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: o fio grosso de mel escorre da colher para dentro do copo. Eva Dall diz a frase em ritmo natural logo no começo e continua despejando o mel em silêncio até o fim.

câmera: fixa

som ambiente: cozinha residencial tranquila, sem música
```

### V05 · T5 · usa K05

```text
o avatar Eva Dall, homem, fala em inglês com sotaque americano de um homem negro americano, voz média e amigável de um homem de quase cinquenta anos, entonação confiante e calorosa, voz autêntica, como se exigisse ser ouvido, a seguinte frase: "Drink this every morning on an empty stomach and your energy starts coming back and your clothes start fitting better."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Eva Dall segura o copo com as duas mãos na altura do peito e fala para a câmera, com pequenos movimentos naturais.

câmera: fixa

som ambiente: cozinha residencial tranquila, sem música
```

### V06 · T6 · usa K06

```text
o avatar Eva Dall, homem, fala em inglês com sotaque americano de um homem negro americano, voz média e amigável de um homem de quase cinquenta anos, entonação animada e convidativa, voz autêntica, como se exigisse ser ouvido, a seguinte frase: "And comment yes, and I will send you one more ingredient that makes this ten times more powerful. And follow me so that I can reach you."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Eva Dall segura o copo com as duas mãos, se inclina um pouco para a câmera e fala direto com ela, sorrindo no fim.

câmera: fixa

som ambiente: cozinha residencial tranquila, sem música
```

## Mapa de âncoras

| Keyframe | Referências a anexar | Modelo |
|---|---|---|
| K01 | ÂNCORA EVA DALL + FRAME DO MODELO (`input/primeiro_frame_modelo.png`, só composição) | Nano Banana 2, 9:16 |
| K02 a K06 | ÂNCORA EVA DALL | Nano Banana 2, 9:16 |

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

