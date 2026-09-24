# Lais Collins | FityWell Growth Água no modelo dental | Pacote de Prompts

Vídeo modelo: `input/reference_video.mp4` (37,7 s)

Âncora: `input/ancoras/06_lais_collins.jpg`

Funil: growth, comentário `yes` + follow. Rodada de validação, gancho fiel ao modelo. Sem produto em quadro.

## Índice de geração

| Take | Keyframe | Anexar | Ação |
|---|---|---|---|
| T1 | K01 | ÂNCORA LAIS COLLINS + FRAME DO MODELO | GERAR DO ZERO |
| T2 | K02 | ÂNCORA LAIS COLLINS | GERAR DO ZERO |
| T3 | K03 | ÂNCORA LAIS COLLINS | GERAR DO ZERO |
| T4 | K04 | ÂNCORA LAIS COLLINS | GERAR DO ZERO |
| T5 | K05 | ÂNCORA LAIS COLLINS | GERAR DO ZERO |
| T6 | K06 | ÂNCORA LAIS COLLINS | GERAR DO ZERO |
| T7 | K07 | ÂNCORA LAIS COLLINS | GERAR DO ZERO |

Todo K é GERAR DO ZERO: o bloco do Flow é autossuficiente e cada K descreve o cenário inteiro, então não existe `EDITAR do K__` aqui.

## Trava de identidade e continuidade

- Identidade: The exact fictional AI character Lais Collins, explicitly male: Black and mixed-race American man around thirty-two, light brown skin, highly athletic build, light grey-green eyes, short black locs, short beard and botanical line tattoos across chest, shoulders and arms.
- Roupa: Shirtless, black athletic shorts, a thin gold chain and small silver stud earrings.
- Cenário do corpo: His own bright contemporary apartment with a white kitchen island in front of him, floor-to-ceiling windows and a shelf of green plants with a small American flag.
- Cenário do gancho: His own bright contemporary apartment, at the white kitchen island: floor-to-ceiling windows and a shelf of green plants holding a small American flag behind him.
- Luz: Neutral overcast daylight from a window, the outside clearly visible through the window, soft even light on the face with no harsh shadows.
- Voz (igual em todos os V): voz média e energética de um homem de trinta e poucos anos, sotaque americano de um homem negro americano.
- Sem 2ª pessoa. O modelo dental só aparece no gancho.

## Trava do prop herói

- Gancho: An oversized plastic dental demonstration model, as big as a serving platter: the complete lower arch of teeth in a horseshoe shape, set in glossy pink plastic gums, lying flat on the white kitchen island. Every tooth is covered in a thick, crusty, uneven layer of brown and yellow stain deposits, with dark brown lines along the gumline and between the teeth, clearly a teaching model and not a real mouth. Garrafa plástica transparente de água, sem rótulo.
- Corpo: tigela de vidro transparente; na superfície, a plain clear glass jar of solid white coconut oil with no label, a small plain white cardboard carton of baking soda with no printing on it, and half a fresh yellow lemon. Nenhuma embalagem com texto ou marca.

## Trava da 2ª pessoa (REF-A)

- Não se aplica: não há 2ª pessoa.

## Prompts de imagem

## K01 · T1 · GERAR DO ZERO · ÂNCORA LAIS COLLINS + FRAME DO MODELO

> ### 📎 ANEXAR: **2 IMAGENS**
> **1️⃣ ÂNCORA LAIS COLLINS** `input/ancoras/06_lais_collins.jpg`
> **2️⃣ FRAME DO MODELO, só composição** `input/primeiro_frame_modelo.png`
>
> ### 🆕 GERAR DO ZERO

Cena: gancho, a água sobre o modelo dental manchado.

```json
{
  "shot_id": "K01_gancho_lais_collins",
  "reference_use": "Use the attached image only for Lais Collins's exact identity, wardrobe and own setting. Do not copy its pose or framing. Use the second attached image only as a composition reference for the low camera, the dental model filling the lower half and the water bottle tilted over it; do not copy its man, his clothes, glasses, room or colors.",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "identity_main": "The exact fictional AI character Lais Collins, explicitly male: Black and mixed-race American man around thirty-two, light brown skin, highly athletic build, light grey-green eyes, short black locs, short beard and botanical line tattoos across chest, shoulders and arms.",
  "wardrobe": "Shirtless, black athletic shorts, a thin gold chain and small silver stud earrings.",
  "scene": "His own bright contemporary apartment, at the white kitchen island: floor-to-ceiling windows and a shelf of green plants holding a small American flag behind him.",
  "prop": "An oversized plastic dental demonstration model, as big as a serving platter: the complete lower arch of teeth in a horseshoe shape, set in glossy pink plastic gums, lying flat on the white kitchen island. Every tooth is covered in a thick, crusty, uneven layer of brown and yellow stain deposits, with dark brown lines along the gumline and between the teeth, clearly a teaching model and not a real mouth. Lais Collins holds a clear plastic water bottle with no label in one hand, tilted over the front teeth, and a thin stream of water is just starting to fall onto them.",
  "posture": "Lais Collins leans in from behind the dental model, looking into the lens over it, the hand with the water bottle reaching over the teeth.",
  "composition": "The dental model fills the whole lower half of the frame, very close to the lens, large in frame, much closer to the camera than his face. He is clear in the upper half, head and upper chest. Nothing else competes with the dental model.",
  "camera": "phone camera low, just above the level of the teeth and very close to them, slight upward angle",
  "state": "Start frame: the first thin stream of water is just touching the fully stained front teeth; every tooth is still brown and yellow. Lais Collins is caught mid-sentence, lips naturally parted, animated expression.",
  "lighting": "Neutral overcast daylight from a window, the outside clearly visible through the window, soft even light on the face with no harsh shadows.",
  "realism": "Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday reality, background fully in focus, everything in sharp focus, no AI polish, no beauty smoothing.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no printed labels or lettering on any package, no studio, no plastic-looking human skin, no extra fingers, no supernatural lighting, no blur, no bokeh, no artificial lighting, no warm orange color cast, no yellow tint, no golden glow, no golden hour light, no sunset, no de-aging, no beauty smoothing, no visible phone, no HDR, no cinematic lighting, no real human mouth, no small dental model, no toy-sized teeth, no clean white teeth yet, no second person in frame"
}
```

## K02 · T2 · GERAR DO ZERO · ÂNCORA LAIS COLLINS

> ### 📎 ANEXAR: **1 IMAGEM**
> **1️⃣ ÂNCORA LAIS COLLINS** `input/ancoras/06_lais_collins.jpg`
>
> ### 🆕 GERAR DO ZERO

Cena: coco entrando na tigela, plano médio.

```json
{
  "shot_id": "K02_t2_lais_collins",
  "reference_use": "Use the attached image only for Lais Collins's exact identity, wardrobe and own setting. Do not copy its pose or framing.",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "identity_main": "The exact fictional AI character Lais Collins, explicitly male: Black and mixed-race American man around thirty-two, light brown skin, highly athletic build, light grey-green eyes, short black locs, short beard and botanical line tattoos across chest, shoulders and arms.",
  "wardrobe": "Shirtless, black athletic shorts, a thin gold chain and small silver stud earrings.",
  "scene": "His own bright contemporary apartment with a white kitchen island in front of him, floor-to-ceiling windows and a shelf of green plants with a small American flag.",
  "prop": "An empty clear glass mixing bowl stands on the white kitchen island in the lower foreground, very close to the lens, larger in frame than his hands. Beside it on the white kitchen island: a plain clear glass jar of solid white coconut oil with no label, a small plain white cardboard carton of baking soda with no printing on it, and half a fresh yellow lemon. Lais Collins holds a metal spoon with a heaped scoop of solid white coconut oil right above the bowl.",
  "posture": "Lais Collins is seated on a stool at the island, leaning slightly toward the camera.",
  "composition": "From the waist up, the bowl in the lower foreground closer to the camera than his face. The background is reduced by framing, never by blur.",
  "camera": "phone camera at chest height, straight on, fixed",
  "state": "Start frame: Lais Collins is about to drop the coconut oil into the bowl, caught mid-sentence, lips naturally parted, animated expression.",
  "lighting": "Neutral overcast daylight from a window, the outside clearly visible through the window, soft even light on the face with no harsh shadows.",
  "realism": "Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday reality, background fully in focus, everything in sharp focus, no AI polish, no beauty smoothing.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no printed labels or lettering on any package, no studio, no plastic-looking human skin, no extra fingers, no supernatural lighting, no blur, no bokeh, no artificial lighting, no warm orange color cast, no yellow tint, no golden glow, no golden hour light, no sunset, no de-aging, no beauty smoothing, no visible phone, no HDR, no cinematic lighting, no dental model in frame, no second person in frame"
}
```

## K03 · T3 · GERAR DO ZERO · ÂNCORA LAIS COLLINS

> ### 📎 ANEXAR: **1 IMAGEM**
> **1️⃣ ÂNCORA LAIS COLLINS** `input/ancoras/06_lais_collins.jpg`
>
> ### 🆕 GERAR DO ZERO

Cena: mãos misturando a pasta, close.

```json
{
  "shot_id": "K03_t3_lais_collins",
  "reference_use": "Use the attached image only for Lais Collins's exact identity, wardrobe and own setting. Do not copy its pose or framing.",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "identity_main": "The exact fictional AI character Lais Collins, explicitly male: Black and mixed-race American man around thirty-two, light brown skin, highly athletic build, light grey-green eyes, short black locs, short beard and botanical line tattoos across chest, shoulders and arms.",
  "wardrobe": "Shirtless, black athletic shorts, a thin gold chain and small silver stud earrings.",
  "scene": "His own bright contemporary apartment with a white kitchen island in front of him, floor-to-ceiling windows and a shelf of green plants with a small American flag.",
  "prop": "A clear glass mixing bowl with coconut oil, baking soda and a little lemon juice half-mixed into a thick white paste fills the lower half of the frame on the white kitchen island, very close to the lens. Lais Collins's hands hold the bowl rim and a metal spoon stirring inside it.",
  "posture": "Lais Collins is seated on a stool at the island, leaning slightly toward the camera.",
  "composition": "Close shot of the hands and the bowl, from the chest down, his face cut off by the top edge of the frame. The background is reduced by framing, never by blur.",
  "camera": "phone camera close to the bowl, slightly above it, fixed",
  "state": "Start frame: the spoon is mid-stir, the mixture streaky and almost a smooth paste.",
  "lighting": "Neutral overcast daylight from a window, the outside clearly visible through the window, soft even light on the face with no harsh shadows.",
  "realism": "Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday reality, background fully in focus, everything in sharp focus, no AI polish, no beauty smoothing.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no printed labels or lettering on any package, no studio, no plastic-looking human skin, no extra fingers, no supernatural lighting, no blur, no bokeh, no artificial lighting, no warm orange color cast, no yellow tint, no golden glow, no golden hour light, no sunset, no de-aging, no beauty smoothing, no visible phone, no HDR, no cinematic lighting, no dental model in frame, no second person in frame"
}
```

## K04 · T4 · GERAR DO ZERO · ÂNCORA LAIS COLLINS

> ### 📎 ANEXAR: **1 IMAGEM**
> **1️⃣ ÂNCORA LAIS COLLINS** `input/ancoras/06_lais_collins.jpg`
>
> ### 🆕 GERAR DO ZERO

Cena: tigela pronta perto da lente, inclinado.

```json
{
  "shot_id": "K04_t4_lais_collins",
  "reference_use": "Use the attached image only for Lais Collins's exact identity, wardrobe and own setting. Do not copy its pose or framing.",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "identity_main": "The exact fictional AI character Lais Collins, explicitly male: Black and mixed-race American man around thirty-two, light brown skin, highly athletic build, light grey-green eyes, short black locs, short beard and botanical line tattoos across chest, shoulders and arms.",
  "wardrobe": "Shirtless, black athletic shorts, a thin gold chain and small silver stud earrings.",
  "scene": "His own bright contemporary apartment with a white kitchen island in front of him, floor-to-ceiling windows and a shelf of green plants with a small American flag.",
  "prop": "Lais Collins holds a clear glass bowl full of smooth creamy white paste with both hands, pushed toward the lens, very close to the camera in the lower foreground. On the white kitchen island at the bottom edge: a plain clear glass jar of solid white coconut oil with no label, a small plain white cardboard carton of baking soda with no printing on it, and half a fresh yellow lemon.",
  "posture": "Lais Collins is seated on a stool at the island, leaning slightly toward the camera.",
  "composition": "From the chest up, leaning toward the lens, his face clear in the upper half, the bowl in the lower foreground closer to the camera than his face. The background is reduced by framing, never by blur.",
  "camera": "phone camera at chest height, straight on, fixed",
  "state": "Start frame: Lais Collins leans forward holding the bowl out, caught mid-sentence, lips naturally parted, animated expression.",
  "lighting": "Neutral overcast daylight from a window, the outside clearly visible through the window, soft even light on the face with no harsh shadows.",
  "realism": "Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday reality, background fully in focus, everything in sharp focus, no AI polish, no beauty smoothing.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no printed labels or lettering on any package, no studio, no plastic-looking human skin, no extra fingers, no supernatural lighting, no blur, no bokeh, no artificial lighting, no warm orange color cast, no yellow tint, no golden glow, no golden hour light, no sunset, no de-aging, no beauty smoothing, no visible phone, no HDR, no cinematic lighting, no dental model in frame, no second person in frame"
}
```

## K05 · T5 · GERAR DO ZERO · ÂNCORA LAIS COLLINS

> ### 📎 ANEXAR: **1 IMAGEM**
> **1️⃣ ÂNCORA LAIS COLLINS** `input/ancoras/06_lais_collins.jpg`
>
> ### 🆕 GERAR DO ZERO

Cena: tigela na altura do peito.

```json
{
  "shot_id": "K05_t5_lais_collins",
  "reference_use": "Use the attached image only for Lais Collins's exact identity, wardrobe and own setting. Do not copy its pose or framing.",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "identity_main": "The exact fictional AI character Lais Collins, explicitly male: Black and mixed-race American man around thirty-two, light brown skin, highly athletic build, light grey-green eyes, short black locs, short beard and botanical line tattoos across chest, shoulders and arms.",
  "wardrobe": "Shirtless, black athletic shorts, a thin gold chain and small silver stud earrings.",
  "scene": "His own bright contemporary apartment with a white kitchen island in front of him, floor-to-ceiling windows and a shelf of green plants with a small American flag.",
  "prop": "Lais Collins holds the clear glass bowl of smooth creamy white paste with both hands at chest height, very close to the lens in the lower foreground. On the white kitchen island at the bottom edge: a plain clear glass jar of solid white coconut oil with no label, a small plain white cardboard carton of baking soda with no printing on it, and half a fresh yellow lemon.",
  "posture": "Lais Collins is seated on a stool at the island, leaning slightly toward the camera.",
  "composition": "From the chest up, his face clear in the upper half, the bowl in the lower foreground closer to the camera than his face. The background is reduced by framing, never by blur.",
  "camera": "phone camera at chest height, straight on, fixed",
  "state": "Start frame: Lais Collins looks into the lens holding the bowl, caught mid-sentence, lips naturally parted, animated expression.",
  "lighting": "Neutral overcast daylight from a window, the outside clearly visible through the window, soft even light on the face with no harsh shadows.",
  "realism": "Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday reality, background fully in focus, everything in sharp focus, no AI polish, no beauty smoothing.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no printed labels or lettering on any package, no studio, no plastic-looking human skin, no extra fingers, no supernatural lighting, no blur, no bokeh, no artificial lighting, no warm orange color cast, no yellow tint, no golden glow, no golden hour light, no sunset, no de-aging, no beauty smoothing, no visible phone, no HDR, no cinematic lighting, no dental model in frame, no second person in frame"
}
```

## K06 · T6 · GERAR DO ZERO · ÂNCORA LAIS COLLINS

> ### 📎 ANEXAR: **1 IMAGEM**
> **1️⃣ ÂNCORA LAIS COLLINS** `input/ancoras/06_lais_collins.jpg`
>
> ### 🆕 GERAR DO ZERO

Cena: tigela na altura do peito, sorriso.

```json
{
  "shot_id": "K06_t6_lais_collins",
  "reference_use": "Use the attached image only for Lais Collins's exact identity, wardrobe and own setting. Do not copy its pose or framing.",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "identity_main": "The exact fictional AI character Lais Collins, explicitly male: Black and mixed-race American man around thirty-two, light brown skin, highly athletic build, light grey-green eyes, short black locs, short beard and botanical line tattoos across chest, shoulders and arms.",
  "wardrobe": "Shirtless, black athletic shorts, a thin gold chain and small silver stud earrings.",
  "scene": "His own bright contemporary apartment with a white kitchen island in front of him, floor-to-ceiling windows and a shelf of green plants with a small American flag.",
  "prop": "Lais Collins holds the clear glass bowl of smooth creamy white paste with both hands at chest height, very close to the lens in the lower foreground. On the white kitchen island at the bottom edge: a plain clear glass jar of solid white coconut oil with no label, a small plain white cardboard carton of baking soda with no printing on it, and half a fresh yellow lemon.",
  "posture": "Lais Collins is seated on a stool at the island, leaning slightly toward the camera.",
  "composition": "From the chest up, his face clear in the upper half, the bowl in the lower foreground closer to the camera than his face. The background is reduced by framing, never by blur.",
  "camera": "phone camera at chest height, straight on, fixed",
  "state": "Start frame: Lais Collins looks into the lens with a warm, confident half smile, caught mid-sentence, lips naturally parted, animated expression.",
  "lighting": "Neutral overcast daylight from a window, the outside clearly visible through the window, soft even light on the face with no harsh shadows.",
  "realism": "Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday reality, background fully in focus, everything in sharp focus, no AI polish, no beauty smoothing.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no printed labels or lettering on any package, no studio, no plastic-looking human skin, no extra fingers, no supernatural lighting, no blur, no bokeh, no artificial lighting, no warm orange color cast, no yellow tint, no golden glow, no golden hour light, no sunset, no de-aging, no beauty smoothing, no visible phone, no HDR, no cinematic lighting, no dental model in frame, no second person in frame"
}
```

## K07 · T7 · GERAR DO ZERO · ÂNCORA LAIS COLLINS

> ### 📎 ANEXAR: **1 IMAGEM**
> **1️⃣ ÂNCORA LAIS COLLINS** `input/ancoras/06_lais_collins.jpg`
>
> ### 🆕 GERAR DO ZERO

Cena: tigela, plano mais fechado do vídeo.

```json
{
  "shot_id": "K07_t7_lais_collins",
  "reference_use": "Use the attached image only for Lais Collins's exact identity, wardrobe and own setting. Do not copy its pose or framing.",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "identity_main": "The exact fictional AI character Lais Collins, explicitly male: Black and mixed-race American man around thirty-two, light brown skin, highly athletic build, light grey-green eyes, short black locs, short beard and botanical line tattoos across chest, shoulders and arms.",
  "wardrobe": "Shirtless, black athletic shorts, a thin gold chain and small silver stud earrings.",
  "scene": "His own bright contemporary apartment with a white kitchen island in front of him, floor-to-ceiling windows and a shelf of green plants with a small American flag.",
  "prop": "Lais Collins holds the clear glass bowl of smooth creamy white paste with both hands at chest height, very close to the lens in the lower foreground.",
  "posture": "Lais Collins is seated on a stool at the island, leaning slightly toward the camera.",
  "composition": "Tightest shot of the video: from the upper chest up, his face clear in the upper half, the bowl in the lower foreground closer to the camera than his face. The background is reduced by framing, never by blur.",
  "camera": "phone camera at chest height, straight on, fixed",
  "state": "Start frame: Lais Collins leans a little toward the lens, smiling, caught mid-sentence, lips naturally parted, animated expression.",
  "lighting": "Neutral overcast daylight from a window, the outside clearly visible through the window, soft even light on the face with no harsh shadows.",
  "realism": "Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday reality, background fully in focus, everything in sharp focus, no AI polish, no beauty smoothing.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no printed labels or lettering on any package, no studio, no plastic-looking human skin, no extra fingers, no supernatural lighting, no blur, no bokeh, no artificial lighting, no warm orange color cast, no yellow tint, no golden glow, no golden hour light, no sunset, no de-aging, no beauty smoothing, no visible phone, no HDR, no cinematic lighting, no dental model in frame, no second person in frame"
}
```

## Bloco global de vídeo

```text
o avatar Lais Collins, homem, fala em inglês com sotaque americano de um homem negro americano, voz média e energética de um homem de trinta e poucos anos, [emoção da fala], voz autêntica, como se exigisse ser ouvido, a seguinte frase: "[FALA EXATA DO ROTEIRO]"

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: [ação enxuta]

câmera: [fixa]

som ambiente: apartamento moderno tranquilo, sem música
```

# Prompts de vídeo

### V01 · T1 · usa K01

```text
o avatar Lais Collins, homem, fala em inglês com sotaque americano de um homem negro americano, voz média e energética de um homem de trinta e poucos anos, entonação confiante e cúmplice, como quem conta um segredo que ninguém mais conta, voz autêntica, como se exigisse ser ouvido, a seguinte frase: "Your dentist will never tell you this, because the day you learn it is the day you stop paying for whitening."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Lais Collins inclina a garrafa e a água cai em fio sobre os dentes manchados do modelo dental; a crosta marrom escorre com espuma e os dentes vão aparecendo brancos, da frente para os lados, até a arcada inteira ficar branca e limpa; ele fala olhando para a câmera o tempo todo.

câmera: fixa, baixa, leve handheld

som ambiente: apartamento moderno tranquilo, som da água caindo e borbulhando, sem música
```

### V02 · T2 · usa K02

```text
o avatar Lais Collins, homem, fala em inglês com sotaque americano de um homem negro americano, voz média e energética de um homem de trinta e poucos anos, entonação calma e didática, voz autêntica, como se exigisse ser ouvido, a seguinte frase: "Take one tablespoon of coconut oil, half a teaspoon of baking soda, and three drops of lemon juice,"

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Lais Collins põe uma colher de óleo de coco na tigela de vidro, depois uma colher de bicarbonato, e espreme três gotas do meio limão dentro dela, enquanto a câmera se aproxima devagar das mãos e da tigela.

câmera: push-in lento, do plano médio até as mãos e a tigela

som ambiente: apartamento moderno tranquilo, sem música
```

### V03 · T3 · usa K03

```text
o avatar Lais Collins, homem, fala em inglês com sotaque americano de um homem negro americano, voz média e energética de um homem de trinta e poucos anos, entonação calma e didática, voz autêntica, como se exigisse ser ouvido, a seguinte frase: "and mix it into a paste."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Lais Collins mexe a mistura com a colher e ela vira uma pasta branca e cremosa. Ele diz a frase em ritmo natural logo no começo e continua mexendo em silêncio até o fim.

câmera: fixa, fechada nas mãos

som ambiente: apartamento moderno tranquilo, som leve da colher na tigela, sem música
```

### V04 · T4 · usa K04

```text
o avatar Lais Collins, homem, fala em inglês com sotaque americano de um homem negro americano, voz média e energética de um homem de trinta e poucos anos, entonação calma e didática, sorrindo de leve, voz autêntica, como se exigisse ser ouvido, a seguinte frase: "Brush with it every morning for two minutes, then spit it out and rinse with warm water."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Lais Collins segura a tigela com a pasta branca perto da câmera com as duas mãos, inclinado para a frente, e fala direto para a lente.

câmera: fixa

som ambiente: apartamento moderno tranquilo, sem música
```

### V05 · T5 · usa K05

```text
o avatar Lais Collins, homem, fala em inglês com sotaque americano de um homem negro americano, voz média e energética de um homem de trinta e poucos anos, entonação confiante, explicando com clareza, voz autêntica, como se exigisse ser ouvido, a seguinte frase: "The coconut oil pulls the bacteria and build up off your enamel, and the baking soda lifts the surface stains, and the lemon brightens everything up."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Lais Collins segura a tigela com as duas mãos na altura do peito e fala para a câmera, com pequenos movimentos naturais.

câmera: fixa

som ambiente: apartamento moderno tranquilo, sem música
```

### V06 · T6 · usa K06

```text
o avatar Lais Collins, homem, fala em inglês com sotaque americano de um homem negro americano, voz média e energética de um homem de trinta e poucos anos, entonação calorosa e segura, com orgulho tranquilo no fim, voz autêntica, como se exigisse ser ouvido, a seguinte frase: "That yellow starts fading, and the stains disappear like they were never there. In all my years of working in wellness, this is something I always teach."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Lais Collins segura a tigela com as duas mãos na altura do peito e fala para a câmera, sorrindo no fim.

câmera: fixa

som ambiente: apartamento moderno tranquilo, sem música
```

### V07 · T7 · usa K07

```text
o avatar Lais Collins, homem, fala em inglês com sotaque americano de um homem negro americano, voz média e energética de um homem de trinta e poucos anos, entonação animada e convidativa, sorrindo, voz autêntica, como se exigisse ser ouvido, a seguinte frase: "Comment yes if you want more helpful videos like this, and make sure you follow me so you do not miss the next one."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Lais Collins segura a tigela com as duas mãos, se inclina um pouco para a câmera e fala direto com ela, sorrindo.

câmera: fixa

som ambiente: apartamento moderno tranquilo, sem música
```

## Mapa de âncoras

| Keyframe | Referências a anexar | Modelo |
|---|---|---|
| K01 | ÂNCORA LAIS COLLINS + FRAME DO MODELO (`input/primeiro_frame_modelo.png`, só composição) | Nano Banana 2, 9:16 |
| K02 a K07 | ÂNCORA LAIS COLLINS | Nano Banana 2, 9:16 |

## Montagem no CapCut

1. Clipes numerados na ordem: V01, V02, V03, V04, V05, V06, V07.
2. Cortar cada clipe no tempo da cena do modelo: T1 0,0 a 5,9 s; T2 5,9 a 11,4 s; T3 11,4 a 13,1 s; T4 13,1 a 17,5 s; T5 17,5 a 25,3 s; T6 25,3 a 32,4 s; T7 32,4 a 37,7 s.
3. Zero tempo morto: todo clipe começa já falando. Isolate Voice / Keep Vocal no áudio.
4. V03 é cena curta: a fala vem no começo; cortar logo depois de "paste", no tempo da cena.
5. Legenda palavra a palavra em serifa itálica branca no meio do quadro, igual ao modelo, do começo ao fim.
6. Sem Voice Changer: a voz vem do prompt de cada V.
7. Música só no corpo (V02 em diante), nunca no gancho, entre -19 e -20 dB, fora da biblioteca do TikTok.
8. Rótulo pequeno `AI-generated` num canto do vídeo.

## Gates de qualidade

1. Fala de cada V igual ao ROTEIRO, palavra por palavra (T6 na versão do avatar, tabela de congruência).
2. Um take por cena do modelo; T3 marcado CENA CURTA; nenhum take acima de 29 palavras.
3. Bandeira dos EUA no campo scene de todo K.
4. Zero travessão.
5. Keyword `yes` no T7.
6. Produto fora de quadro, nenhuma embalagem com marca ou texto.
7. Negative sem termo sensível.
8. GATE_VISUAL Partes 1 a 3 em todo K: herói colado na lente, luz neutra, sem tom quente, sem blur, trecho de realismo.
9. Gancho fiel no conteúdo: água de garrafa sobre o modelo dental gigante manchado, que fica branco sem corte.
10. Um K = um V, e o reveal do gancho é uma imagem só, do estado inicial (arcada inteira manchada).

