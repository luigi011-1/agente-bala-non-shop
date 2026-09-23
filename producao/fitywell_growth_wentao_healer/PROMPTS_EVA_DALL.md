# Eva Dall | FityWell Growth | Pacote de Prompts

Vídeo modelo: `input/reference_video.mp4`, 29,304 s

Âncora: `input/anchors/eva_dall.jpeg`

Referência da cliente: `REF-A`, gerada com `REF_CLIENTE_40PLUS.md`

Objetivo: crescimento orgânico. Hooks: H1, H4, H10, H9 e H6.

## Índice de geração

| Take | Hook | Keyframe | Anexar | Ação |
|---|---|---|---|---|
| T1 | H1 | K01 | ÂNCORA EVA DALL + REF-A | GERAR DO ZERO |
| T6 | H4 | K02 | ÂNCORA EVA DALL + REF-A | GERAR DO ZERO |
| T7 | H10 | K03 | ÂNCORA EVA DALL + REF-A | GERAR DO ZERO |
| T8 | H9 | K04 | ÂNCORA EVA DALL + REF-A | GERAR DO ZERO |
| T9 | H6 | K05 | ÂNCORA EVA DALL + REF-A | GERAR DO ZERO |
| T2 | corpo | K06 | ÂNCORA EVA DALL + REF-A | GERAR DO ZERO |
| T3 | corpo | K07 | ÂNCORA EVA DALL + REF-A | GERAR DO ZERO |
| T4 e T5 | corpo | K08 | ÂNCORA EVA DALL + REF-A | GERAR DO ZERO |

K08 sustenta V08 e V09 porque setup, prop e enquadramento permanecem idênticos.

## Trava de identidade e continuidade

- The exact fictional AI character Eva Dall, explicitly male: Black American man around forty-nine, medium brown skin, lean athletic build, long oval face, dark brown eyes, subtle freckles and moles, very long locs mixing black, grey and silver, grey goatee and moustache, brown leather cap worn backward.
- Roupa: White ribbed tank top and a thin silver chain.
- Cenário: His own modern white kitchen with strongly veined dark green marble counter and backsplash, tall windows to the right, one small plant and a small American flag.
- Superfície: the dark green marble counter.
- Luz: Neutral daylight from the tall windows, no warm cast.
- A cliente é sempre a mulher fictícia da REF-A.

## Trava do prop herói

```text
Fresh raw ginger with pale golden-yellow flesh, fibrous texture and a thin light-brown skin edge.
Every slice is visibly food, moist but not glossy, paper-thin and small. Ginger and exact mouth contact
are always the closest elements to the lens in the hook. Nothing competes.
```

## Trava da 2ª pessoa, REF-A

Gerar e aprovar `REF-A` uma vez. Anexar com a âncora do coach em K01 a K08. A REF-A trava identidade, idade, cabelo e roupa. O cenário vem da âncora do coach.

# Prompts de imagem

## K01 · T1 · H1 · GERAR DO ZERO · ÂNCORA EVA DALL + REF-A

> ### 📎 ANEXAR: **2 IMAGENS**
> **1️⃣ ÂNCORA EVA DALL** `input/anchors/eva_dall.jpeg`
> **2️⃣ REF-A** cliente FitWell 40+ já aprovada
>
> ### 🆕 GERAR DO ZERO

```json
{
  "shot_id": "K01_H1_eva_dall",
  "reference_use": "Use the first attached image only for Eva Dall's exact identity, wardrobe and own setting. Use the second attached image only for the exact female client's identity and wardrobe. Do not copy either pose or framing.",
  "fiction_note": "These are fictional AI-generated characters, no real person is depicted.",
  "identity_main": "The exact fictional AI character Eva Dall, explicitly male: Black American man around forty-nine, medium brown skin, lean athletic build, long oval face, dark brown eyes, subtle freckles and moles, very long locs mixing black, grey and silver, grey goatee and moustache, brown leather cap worn backward.",
  "second_person": "The same fictional American female client around fifty: fair neutral skin with natural fine lines, oval face, blue-grey eyes, blonde hair in a loose low ponytail, plain navy sleeveless cotton top, no jewelry. One paper-thin coin of fresh raw ginger rests flat in the center of her extended tongue.",
  "wardrobe": "White ribbed tank top and a thin silver chain.",
  "scene": "His own modern white kitchen with strongly veined dark green marble counter and backsplash, tall windows to the right, one small plant and a small American flag.",
  "posture": "The client is closest to camera with mouth open. The coach stands immediately behind and to her right and points at the ginger without touching her.",
  "composition": "Extreme close-up. Open mouth, tongue, ginger coin and pointing fingertip dominate the foreground; the coach's speaking face remains clear in the upper right. The client is partially cropped by the frame and nothing else competes.",
  "camera": "phone camera at mouth level, straight-on, pushed extremely close to the ginger and point of contact",
  "state": "Start frame: One paper-thin coin of fresh raw ginger rests flat in the center of her extended tongue. The coach is beginning to speak and the client remains silent.",
  "lighting": "Neutral daylight from the tall windows, no warm cast.",
  "realism": "UGC realism, real skin texture with visible pores, individual hair strands, realistic shadows and reflections, iPhone-footage look, no AI polish, no beauty smoothing, no blur anywhere, everything in sharp focus.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no studio, no plastic skin, no extra fingers, no supernatural lighting, no blur, no artificial lighting, no warm color cast, no visible phone, no spoon, no knife, no plate, no second ginger slice"
}
```

## K02 · T6 · H4 · GERAR DO ZERO · ÂNCORA EVA DALL + REF-A

> ### 📎 ANEXAR: **2 IMAGENS**
> **1️⃣ ÂNCORA EVA DALL** `input/anchors/eva_dall.jpeg`
> **2️⃣ REF-A** cliente FitWell 40+ já aprovada
>
> ### 🆕 GERAR DO ZERO

```json
{
  "shot_id": "K02_H4_eva_dall",
  "reference_use": "Use the first attached image only for Eva Dall's exact identity, wardrobe and own setting. Use the second attached image only for the exact female client's identity and wardrobe. Do not copy either pose or framing.",
  "fiction_note": "These are fictional AI-generated characters, no real person is depicted.",
  "identity_main": "The exact fictional AI character Eva Dall, explicitly male: Black American man around forty-nine, medium brown skin, lean athletic build, long oval face, dark brown eyes, subtle freckles and moles, very long locs mixing black, grey and silver, grey goatee and moustache, brown leather cap worn backward.",
  "second_person": "The same fictional American female client around fifty: fair neutral skin with natural fine lines, oval face, blue-grey eyes, blonde hair in a loose low ponytail, plain navy sleeveless cotton top, no jewelry. A small plain metal teaspoon holds one tiny loose pinch of freshly grated raw ginger, and only the outer ginger strands touch the tip of her extended tongue.",
  "wardrobe": "White ribbed tank top and a thin silver chain.",
  "scene": "His own modern white kitchen with strongly veined dark green marble counter and backsplash, tall windows to the right, one small plant and a small American flag.",
  "posture": "The client holds the spoon steadily. The coach stands immediately behind and points at the grated ginger.",
  "composition": "Extreme close-up. Spoon bowl, grated ginger, tongue and pointing fingertip dominate; the coach's speaking face stays clear. The client is partially cropped by the frame and nothing else competes.",
  "camera": "phone camera at mouth level, straight-on, pushed extremely close to the ginger and point of contact",
  "state": "Start frame: A small plain metal teaspoon holds one tiny loose pinch of freshly grated raw ginger, and only the outer ginger strands touch the tip of her extended tongue. The coach is beginning to speak and the client remains silent.",
  "lighting": "Neutral daylight from the tall windows, no warm cast.",
  "realism": "UGC realism, real skin texture with visible pores, individual hair strands, realistic shadows and reflections, iPhone-footage look, no AI polish, no beauty smoothing, no blur anywhere, everything in sharp focus.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no studio, no plastic skin, no extra fingers, no supernatural lighting, no blur, no artificial lighting, no warm color cast, no visible phone, no knife, no plate, no whole ginger root"
}
```

## K03 · T7 · H10 · GERAR DO ZERO · ÂNCORA EVA DALL + REF-A

> ### 📎 ANEXAR: **2 IMAGENS**
> **1️⃣ ÂNCORA EVA DALL** `input/anchors/eva_dall.jpeg`
> **2️⃣ REF-A** cliente FitWell 40+ já aprovada
>
> ### 🆕 GERAR DO ZERO

```json
{
  "shot_id": "K03_H10_eva_dall",
  "reference_use": "Use the first attached image only for Eva Dall's exact identity, wardrobe and own setting. Use the second attached image only for the exact female client's identity and wardrobe. Do not copy either pose or framing.",
  "fiction_note": "These are fictional AI-generated characters, no real person is depicted.",
  "identity_main": "The exact fictional AI character Eva Dall, explicitly male: Black American man around forty-nine, medium brown skin, lean athletic build, long oval face, dark brown eyes, subtle freckles and moles, very long locs mixing black, grey and silver, grey goatee and moustache, brown leather cap worn backward.",
  "second_person": "The same fictional American female client around fifty: fair neutral skin with natural fine lines, oval face, blue-grey eyes, blonde hair in a loose low ponytail, plain navy sleeveless cotton top, no jewelry. She pinches one paper-thin raw ginger coin exactly one centimeter in front of the tip of her extended tongue. The ginger has not touched yet.",
  "wardrobe": "White ribbed tank top and a thin silver chain.",
  "scene": "His own modern white kitchen with strongly veined dark green marble counter and backsplash, tall windows to the right, one small plant and a small American flag.",
  "posture": "The coach stands immediately behind and points at the visible air gap.",
  "composition": "Extreme close-up. Ginger coin, one-centimeter gap, tongue and fingertip dominate; the coach's speaking face stays clear. The client is partially cropped by the frame and nothing else competes.",
  "camera": "phone camera at mouth level, straight-on, pushed extremely close to the ginger and point of contact",
  "state": "Start frame: She pinches one paper-thin raw ginger coin exactly one centimeter in front of the tip of her extended tongue. The ginger has not touched yet. The coach is beginning to speak and the client remains silent.",
  "lighting": "Neutral daylight from the tall windows, no warm cast.",
  "realism": "UGC realism, real skin texture with visible pores, individual hair strands, realistic shadows and reflections, iPhone-footage look, no AI polish, no beauty smoothing, no blur anywhere, everything in sharp focus.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no studio, no plastic skin, no extra fingers, no supernatural lighting, no blur, no artificial lighting, no warm color cast, no visible phone, no contact between ginger and tongue, no spoon, no knife, no plate"
}
```

## K04 · T8 · H9 · GERAR DO ZERO · ÂNCORA EVA DALL + REF-A

> ### 📎 ANEXAR: **2 IMAGENS**
> **1️⃣ ÂNCORA EVA DALL** `input/anchors/eva_dall.jpeg`
> **2️⃣ REF-A** cliente FitWell 40+ já aprovada
>
> ### 🆕 GERAR DO ZERO

```json
{
  "shot_id": "K04_H9_eva_dall",
  "reference_use": "Use the first attached image only for Eva Dall's exact identity, wardrobe and own setting. Use the second attached image only for the exact female client's identity and wardrobe. Do not copy either pose or framing.",
  "fiction_note": "These are fictional AI-generated characters, no real person is depicted.",
  "identity_main": "The exact fictional AI character Eva Dall, explicitly male: Black American man around forty-nine, medium brown skin, lean athletic build, long oval face, dark brown eyes, subtle freckles and moles, very long locs mixing black, grey and silver, grey goatee and moustache, brown leather cap worn backward.",
  "second_person": "The same fictional American female client around fifty: fair neutral skin with natural fine lines, oval face, blue-grey eyes, blonde hair in a loose low ponytail, plain navy sleeveless cotton top, no jewelry. One paper-thin raw ginger slice is held gently between her front teeth with half clearly visible outside. She is not biting or chewing.",
  "wardrobe": "White ribbed tank top and a thin silver chain.",
  "scene": "His own modern white kitchen with strongly veined dark green marble counter and backsplash, tall windows to the right, one small plant and a small American flag.",
  "posture": "The coach stands immediately behind and points at the exposed ginger.",
  "composition": "Extreme close-up. Ginger between the front teeth and pointing fingertip dominate; the coach's speaking face stays clear. The client is partially cropped by the frame and nothing else competes.",
  "camera": "phone camera at mouth level, straight-on, pushed extremely close to the ginger and point of contact",
  "state": "Start frame: One paper-thin raw ginger slice is held gently between her front teeth with half clearly visible outside. She is not biting or chewing. The coach is beginning to speak and the client remains silent.",
  "lighting": "Neutral daylight from the tall windows, no warm cast.",
  "realism": "UGC realism, real skin texture with visible pores, individual hair strands, realistic shadows and reflections, iPhone-footage look, no AI polish, no beauty smoothing, no blur anywhere, everything in sharp focus.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no studio, no plastic skin, no extra fingers, no supernatural lighting, no blur, no artificial lighting, no warm color cast, no visible phone, no chewing, no broken ginger, no spoon, no knife, no plate"
}
```

## K05 · T9 · H6 · GERAR DO ZERO · ÂNCORA EVA DALL + REF-A

> ### 📎 ANEXAR: **2 IMAGENS**
> **1️⃣ ÂNCORA EVA DALL** `input/anchors/eva_dall.jpeg`
> **2️⃣ REF-A** cliente FitWell 40+ já aprovada
>
> ### 🆕 GERAR DO ZERO

```json
{
  "shot_id": "K05_H6_eva_dall",
  "reference_use": "Use the first attached image only for Eva Dall's exact identity, wardrobe and own setting. Use the second attached image only for the exact female client's identity and wardrobe. Do not copy either pose or framing.",
  "fiction_note": "These are fictional AI-generated characters, no real person is depicted.",
  "identity_main": "The exact fictional AI character Eva Dall, explicitly male: Black American man around forty-nine, medium brown skin, lean athletic build, long oval face, dark brown eyes, subtle freckles and moles, very long locs mixing black, grey and silver, grey goatee and moustache, brown leather cap worn backward.",
  "second_person": "The same fictional American female client around fifty: fair neutral skin with natural fine lines, oval face, blue-grey eyes, blonde hair in a loose low ponytail, plain navy sleeveless cotton top, no jewelry. She pinches one paper-thin ginger coin and touches only one edge to the very tip of her extended tongue.",
  "wardrobe": "White ribbed tank top and a thin silver chain.",
  "scene": "His own modern white kitchen with strongly veined dark green marble counter and backsplash, tall windows to the right, one small plant and a small American flag.",
  "posture": "The coach stands immediately behind and points at the exact contact point.",
  "composition": "Extreme close-up. Ginger edge, tongue tip and fingertip dominate; the coach's speaking face stays clear. The client is partially cropped by the frame and nothing else competes.",
  "camera": "phone camera at mouth level, straight-on, pushed extremely close to the ginger and point of contact",
  "state": "Start frame: She pinches one paper-thin ginger coin and touches only one edge to the very tip of her extended tongue. The coach is beginning to speak and the client remains silent.",
  "lighting": "Neutral daylight from the tall windows, no warm cast.",
  "realism": "UGC realism, real skin texture with visible pores, individual hair strands, realistic shadows and reflections, iPhone-footage look, no AI polish, no beauty smoothing, no blur anywhere, everything in sharp focus.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no studio, no plastic skin, no extra fingers, no supernatural lighting, no blur, no artificial lighting, no warm color cast, no visible phone, no full slice lying on tongue, no spoon, no knife, no plate"
}
```

## K06 · T2 · MECANISMO · GERAR DO ZERO · ÂNCORA EVA DALL + REF-A

> ### 📎 ANEXAR: **2 IMAGENS**
> **1️⃣ ÂNCORA EVA DALL** `input/anchors/eva_dall.jpeg`
> **2️⃣ REF-A** cliente FitWell 40+ já aprovada
>
> ### 🆕 GERAR DO ZERO

```json
{
  "shot_id": "K06_body_pause",
  "reference_use": "Use the first attached image only for Eva Dall's exact identity, wardrobe and setting. Use the second only for the exact female client. Do not copy poses.",
  "fiction_note": "These are fictional AI-generated characters, no real person is depicted.",
  "identity_main": "The exact fictional AI character Eva Dall, explicitly male: Black American man around forty-nine, medium brown skin, lean athletic build, long oval face, dark brown eyes, subtle freckles and moles, very long locs mixing black, grey and silver, grey goatee and moustache, brown leather cap worn backward.",
  "second_person": "The same fictional American female client around fifty: fair neutral skin with natural fine lines, oval face, blue-grey eyes, blonde hair in a loose low ponytail, plain navy sleeveless cotton top, no jewelry. Her mouth is open with one paper-thin ginger coin flat in the center of her tongue.",
  "wardrobe": "White ribbed tank top and a thin silver chain.",
  "scene": "His own modern white kitchen with strongly veined dark green marble counter and backsplash, tall windows to the right, one small plant and a small American flag.",
  "posture": "The coach stands close behind and to her right, pointing hand lowered slightly, looking from ginger to phone lens while speaking.",
  "composition": "Very tight two-person close-up, slightly wider than the hook. Mouth and ginger remain foreground, coach's full speaking face clear, client cropped by the edge.",
  "camera": "phone camera at mouth level, straight-on, close and intimate",
  "state": "Start frame: ginger still on the center of her tongue, coach looking into lens, client silent.",
  "lighting": "Neutral daylight from the tall windows, no warm cast.",
  "realism": "UGC realism, real skin texture with visible pores, individual hair strands, realistic shadows and reflections, iPhone-footage look, no AI polish, no beauty smoothing, no blur anywhere, everything in sharp focus.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no studio, no plastic skin, no extra fingers, no supernatural lighting, no blur, no artificial lighting, no warm color cast, no visible phone, no spoon, no knife, no plate, no second ginger slice"
}
```

## K07 · T3 · AUTODIAGNÓSTICO · GERAR DO ZERO · ÂNCORA EVA DALL + REF-A

> ### 📎 ANEXAR: **2 IMAGENS**
> **1️⃣ ÂNCORA EVA DALL** `input/anchors/eva_dall.jpeg`
> **2️⃣ REF-A** cliente FitWell 40+ já aprovada
>
> ### 🆕 GERAR DO ZERO

```json
{
  "shot_id": "K07_cutting_ginger",
  "reference_use": "Use the first attached image only for Eva Dall's exact identity, wardrobe and setting. Use the second only for the exact female client. Do not copy poses.",
  "fiction_note": "These are fictional AI-generated characters, no real person is depicted.",
  "identity_main": "The exact fictional AI character Eva Dall, explicitly male: Black American man around forty-nine, medium brown skin, lean athletic build, long oval face, dark brown eyes, subtle freckles and moles, very long locs mixing black, grey and silver, grey goatee and moustache, brown leather cap worn backward.",
  "second_person": "The same fictional American female client around fifty: fair neutral skin with natural fine lines, oval face, blue-grey eyes, blonde hair in a loose low ponytail, plain navy sleeveless cotton top, no jewelry. She stands immediately beside the coach and watches thoughtfully.",
  "wardrobe": "White ribbed tank top and a thin silver chain.",
  "scene": "His own modern white kitchen with strongly veined dark green marble counter and backsplash, tall windows to the right, one small plant and a small American flag. A clean rectangular wooden cutting board sits on the dark green marble counter.",
  "prop": "A fresh raw ginger root and six paper-thin ginger coins lie on the board. The coach holds a plain chef's knife with its blade resting safely against the root.",
  "posture": "The coach leans toward the board while keeping the face turned enough toward the phone to speak. The client is cropped by the side edge.",
  "composition": "Tight chest-up two-shot. Board, ginger, slices and hands fill the lower foreground closer than faces. Nothing else sits on the work surface.",
  "camera": "phone camera at upper-chest level, slightly high toward the cutting board, pushed close",
  "state": "Start frame: knife rests against ginger before cutting motion.",
  "lighting": "Neutral daylight from the tall windows, no warm cast.",
  "realism": "UGC realism, real skin texture with visible pores, individual hair strands, realistic shadows and reflections, iPhone-footage look, no AI polish, no beauty smoothing, no blur anywhere, everything in sharp focus.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no studio, no plastic skin, no extra fingers, no supernatural lighting, no blur, no artificial lighting, no warm color cast, no visible phone, no food other than ginger, no plate"
}
```

## K08 · T4 E T5 · CONTRASTE, SHARE E FOLLOW · GERAR DO ZERO · ÂNCORA EVA DALL + REF-A

> ### 📎 ANEXAR: **2 IMAGENS**
> **1️⃣ ÂNCORA EVA DALL** `input/anchors/eva_dall.jpeg`
> **2️⃣ REF-A** cliente FitWell 40+ já aprovada
>
> ### 🆕 GERAR DO ZERO

```json
{
  "shot_id": "K08_slices_to_lens",
  "reference_use": "Use the first attached image only for Eva Dall's exact identity, wardrobe and setting. Use the second only for the exact female client. Do not copy poses.",
  "fiction_note": "These are fictional AI-generated characters, no real person is depicted.",
  "identity_main": "The exact fictional AI character Eva Dall, explicitly male: Black American man around forty-nine, medium brown skin, lean athletic build, long oval face, dark brown eyes, subtle freckles and moles, very long locs mixing black, grey and silver, grey goatee and moustache, brown leather cap worn backward.",
  "second_person": "The same fictional American female client around fifty: fair neutral skin with natural fine lines, oval face, blue-grey eyes, blonde hair in a loose low ponytail, plain navy sleeveless cotton top, no jewelry. She stands beside and slightly behind the coach, calm, attentive and partially cropped.",
  "wardrobe": "White ribbed tank top and a thin silver chain.",
  "scene": "His own modern white kitchen with strongly veined dark green marble counter and backsplash, tall windows to the right, one small plant and a small American flag.",
  "prop": "The coach pinches three paper-thin fresh ginger coins in a small fan between thumb and index finger, holding them extremely close to the phone lens.",
  "posture": "The coach leans close behind the ginger fan and looks directly into the lens while speaking.",
  "composition": "Tight shoulders-up frame. Three ginger coins fill the lower center foreground closer than the coach's face. The coach's speaking face dominates the upper half; client cropped by edge.",
  "camera": "eye level, straight-on, very close phone-camera distance",
  "state": "Start frame: three slices held steady near lens, coach beginning to speak.",
  "lighting": "Neutral daylight from the tall windows, no warm cast.",
  "realism": "UGC realism, real skin texture with visible pores, individual hair strands, realistic shadows and reflections, iPhone-footage look, no AI polish, no beauty smoothing, no blur anywhere, everything in sharp focus.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no studio, no plastic skin, no extra fingers, no supernatural lighting, no blur, no artificial lighting, no warm color cast, no visible phone, no product, no knife, no plate"
}
```

## Bloco global de vídeo

```text
o avatar Eva Dall, homem, fala em inglês com sotaque americano de um homem negro americano, voz autêntica, energética, amigável, experiente e prática, como se exigisse ser ouvido, a seguinte frase: "[FALA EXATA DO ROTEIRO]"

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: [ação enxuta]. A cliente permanece silenciosa.

câmera: [fixa ou leve push-in]

som ambiente: cozinha residencial tranquila, sem música
```

# Prompts de vídeo

### V01 · T1 · usa K01

```text
o avatar Eva Dall, homem, fala em inglês com sotaque americano de um homem negro americano, voz autêntica, energética, amigável, experiente e prática, como se exigisse ser ouvido, a seguinte frase: "Put a thin slice of raw ginger on your tongue for ten seconds when an afternoon craving hits. Watch what happens before you reach for food."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: o coach aponta para a fatia sobre a língua e fala para a câmera. A cliente fica imóvel e silenciosa.

câmera: fixa

som ambiente: cozinha residencial tranquila, sem música
```

### V02 · T6 · usa K02

```text
o avatar Eva Dall, homem, fala em inglês com sotaque americano de um homem negro americano, voz autêntica, energética, amigável, experiente e prática, como se exigisse ser ouvido, a seguinte frase: "Touch a tiny pinch of fresh grated ginger to your tongue for ten seconds when an afternoon craving hits. Notice what happens before the snack."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: o coach aponta para o gengibre ralado enquanto a cliente encosta a colher na ponta da língua. Ela permanece silenciosa.

câmera: fixa

som ambiente: cozinha residencial tranquila, sem música
```

### V03 · T7 · usa K03

```text
o avatar Eva Dall, homem, fala em inglês com sotaque americano de um homem negro americano, voz autêntica, energética, amigável, experiente e prática, como se exigisse ser ouvido, a seguinte frase: "Before your next afternoon snack, hold one thin slice of raw ginger right at your tongue for ten seconds. Then watch what your hand does."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: o coach aponta para o espaço. A cliente aproxima a fatia até tocar a ponta da língua e mantém a mão parada. Ela não fala.

câmera: fixa, leve push-in no contato

som ambiente: cozinha residencial tranquila, sem música
```

### V04 · T8 · usa K04

```text
o avatar Eva Dall, homem, fala em inglês com sotaque americano de um homem negro americano, voz autêntica, energética, amigável, experiente e prática, como se exigisse ser ouvido, a seguinte frase: "Hold one thin slice of raw ginger between your front teeth for ten seconds when an afternoon craving hits. Notice what happens before you snack."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: o coach aponta para a parte visível da fatia. A cliente segura o gengibre sem morder, mastigar ou falar.

câmera: fixa

som ambiente: cozinha residencial tranquila, sem música
```

### V05 · T9 · usa K05

```text
o avatar Eva Dall, homem, fala em inglês com sotaque americano de um homem negro americano, voz autêntica, energética, amigável, experiente e prática, como se exigisse ser ouvido, a seguinte frase: "Touch one thin slice of raw ginger to the tip of your tongue for ten seconds when an afternoon craving hits. Watch what happens next."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: o coach aponta para o ponto de contato enquanto a cliente mantém a borda encostada na ponta da língua. Ela fica silenciosa.

câmera: fixa

som ambiente: cozinha residencial tranquila, sem música
```

### V06 · T2 · usa K06

```text
o avatar Eva Dall, homem, fala em inglês com sotaque americano de um homem negro americano, voz autêntica, energética, amigável, experiente e prática, como se exigisse ser ouvido, a seguinte frase: "The ginger does not melt fat. Its sharp taste creates a physical pause between the craving and your next automatic bite."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: o coach baixa a mão, olha da fatia para a lente e explica. A cliente mantém a fatia sobre a língua e permanece silenciosa.

câmera: fixa

som ambiente: cozinha residencial tranquila, sem música
```

### V07 · T3 · usa K07

```text
o avatar Eva Dall, homem, fala em inglês com sotaque americano de um homem negro americano, voz autêntica, energética, amigável, experiente e prática, como se exigisse ser ouvido, a seguinte frase: "Use those ten seconds to ask: am I hungry, or am I tired, stressed, thirsty, or simply repeating my usual afternoon pattern?"

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: o coach corta duas fatias finas de gengibre com movimentos controlados, alternando o olhar entre a tábua e a câmera. A cliente observa e não fala.

câmera: fixa

som ambiente: cozinha residencial tranquila, sem música
```

### V08 · T4 · usa K08

```text
o avatar Eva Dall, homem, fala em inglês com sotaque americano de um homem negro americano, voz autêntica, energética, amigável, experiente e prática, como se exigisse ser ouvido, a seguinte frase: "Most diets tell women over forty to fight cravings harder. I teach them to interrupt the loop first. Share this with a woman who blames her willpower."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: o coach mantém três fatias perto da lente, baixa a mão e a levanta novamente ao pedir o compartilhamento. A cliente faz um leve aceno.

câmera: fixa, leve push-in

som ambiente: cozinha residencial tranquila, sem música
```

### V09 · T5 · usa K08

```text
o avatar Eva Dall, homem, fala em inglês com sotaque americano de um homem negro americano, voz autêntica, energética, amigável, experiente e prática, como se exigisse ser ouvido, a seguinte frase: "Follow me for more simple weight-loss habits made for women over forty, so you do not miss the next one."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: o coach mantém as três fatias visíveis e aponta brevemente para a câmera com a mão livre. A cliente permanece silenciosa.

câmera: leve push-in

som ambiente: cozinha residencial tranquila, sem música
```

## Mapa de âncoras

| Keyframe | Referências | Modelo |
|---|---|---|
| K01 a K08 | ÂNCORA EVA DALL + REF-A | Nano Banana 2, 9:16 |

Vídeo: Veo 3.1 Lite, Lower Priority, 8 segundos, uma variação por V.

## Montagem no CapCut

1. Usar uma abertura entre V01 e V05.
2. Depois usar sempre V06, V07, V08 e V09.
3. Cortar no fim da última palavra completa.
4. Legenda queimada, uma palavra-chave destacada em amarelo.
5. Sem música na geração.
6. Exportar 9:16, 1080 por 1920.

## Gates de qualidade

1. [ ] Identidade, roupa e cenário de Eva Dall iguais à âncora.
2. [ ] Mesma cliente REF-A nos oito keyframes.
3. [ ] Gengibre e ponto de contato dominam K01 a K06.
4. [ ] Coach visível para lip sync nos closes.
5. [ ] Cliente nunca fala.
6. [ ] K03 começa antes do contato.
7. [ ] K04 não mostra mordida.
8. [ ] K07 preserva o corte do gengibre.
9. [ ] K08 mantém três fatias perto da lente.
10. [ ] Bandeira dos EUA presente e em foco.
11. [ ] Zero blur e luz neutra.
12. [ ] Sem produto, celular, quiz ou tela.
13. [ ] Negative sem marca, gore ou órgão.
14. [ ] Falas literais do roteiro.
15. [ ] Validação sem falha.

