# Eva Dall | FityWell Growth Salmão na água | Pacote de Prompts

Vídeo modelo: `input/reference_video.mp4` (30,0 s, Jake Miller Health)

Âncora: `producao/_ancoras/eva_dall_ancora.jpeg`

Funil: growth, save + comment + follow. Rodada de validação, gancho fiel ao modelo. Sem produto em quadro.

## Índice de geração

| Take | Keyframe | Anexar | Ação |
|---|---|---|---|
| T1 | K01 | ÂNCORA EVA DALL + FRAME DO MODELO | GERAR DO ZERO |
| T2 | K02 | ÂNCORA EVA DALL | GERAR DO ZERO |
| T3 | K03 | ÂNCORA EVA DALL | GERAR DO ZERO |
| T4 | K04 | ÂNCORA EVA DALL | GERAR DO ZERO |
| T5 | K05 | ÂNCORA EVA DALL | GERAR DO ZERO |

Todo K é GERAR DO ZERO: o bloco do Flow é autossuficiente e cada K descreve o cenário inteiro, então não existe `EDITAR do K__` aqui. Um K = um V pelo número.

## Trava de identidade e continuidade

- Identidade: The exact fictional AI character Eva Dall, explicitly male: Black American man around forty-nine, medium brown skin, lean athletic build, long oval face, dark brown eyes, subtle freckles and moles, very long locs mixing black, grey and silver, grey goatee and moustache, brown leather cap worn backward.
- Roupa: White ribbed tank top and a thin silver chain.
- Cenário (fixo da conta, em todos os K): His own modern white kitchen, the same room as the reference image, unchanged: a strongly veined dark green marble counter in front of him, a matching dark green marble wall behind the stove at the left, tall windows to the right and a small American flag on the shelf beside a small potted plant.
- Luz: Neutral overcast daylight from a window, the outside clearly visible through the window, soft even light on the face with no harsh shadows.
- Voz (igual em todos os V): voz média e amigável de um homem de quase cinquenta anos, sotaque americano de um homem negro americano.
- Sem 2ª pessoa.

## Trava do prop herói

- Gancho e T2: A rectangular clear glass tank with no lid, shaped like a small aquarium about as wide as his shoulders and one hand deep, stands on the dark green veined marble counter, cheio de água quente, com um filé grosso de salmão cru, laranja com linhas brancas de gordura.
- T3: o mesmo aquário, água fria, salmão inteiro cru prateado com pintinhas pretas.
- T4: tigela redonda de vidro com floretes de brócolis na água, garrafa plástica de água e garrafinha de vidro de vinagre, as duas sem rótulo.
- T5: tábua de madeira grossa com frango inteiro cru, três postas de salmão e uma truta inteira crua.
- Nenhuma embalagem com texto ou marca.

## Trava da 2ª pessoa (REF-A)

- Não se aplica: não há 2ª pessoa.

## Prompts de imagem

## K01 · T1 · GERAR DO ZERO · ÂNCORA EVA DALL + FRAME DO MODELO

> ### 📎 ANEXAR: **2 IMAGENS**
> **1️⃣ ÂNCORA EVA DALL** `producao/_ancoras/eva_dall_ancora.jpeg`
> **2️⃣ FRAME DO MODELO, só composição** `input/frames_modelo/K01_modelo.png`
>
> ### 🆕 GERAR DO ZERO

Cena: gancho, o filé de salmão entrando no aquário de água quente.

```json
{
  "shot_id": "K01_t1_eva_dall",
  "format": "IMPORTANT: THIS IS IPHONE FOOTAGE. Vertical 9:16.",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "reference_use": "Use the attached image only for Eva Dall's exact identity, wardrobe and own setting. Do not copy its pose or framing. Use the second attached image only as a composition reference for the glass tank filling the lower third, the hand lowering the salmon fillet into it and the person centered behind it; do not copy its man, his T-shirt, his room or its colors.",
  "identity_main": "The exact fictional AI character Eva Dall, explicitly male: Black American man around forty-nine, medium brown skin, lean athletic build, long oval face, dark brown eyes, subtle freckles and moles, very long locs mixing black, grey and silver, grey goatee and moustache, brown leather cap worn backward.",
  "wardrobe": "White ribbed tank top and a thin silver chain.",
  "scene": "His own modern white kitchen, the same room as the reference image, unchanged: a strongly veined dark green marble counter in front of him, a matching dark green marble wall behind the stove at the left, tall windows to the right and a small American flag on the shelf beside a small potted plant.",
  "prop": "A rectangular clear glass tank with no lid, shaped like a small aquarium about as wide as his shoulders and one hand deep, stands on the dark green veined marble counter, filled almost to the top with clear hot water. Eva Dall's right hand is lowering a thick raw salmon fillet, bright orange with thin white fat lines, held by one corner between the fingertips: the lower half of the fillet is already under the water, the upper half still above the surface, with small ripples spreading around it. The work surface is otherwise empty.",
  "posture": "Eva Dall is standing behind his dark green marble counter, leaning slightly toward the camera, the right hand reaching down into the tank, the left forearm resting on the work surface beside it.",
  "composition": "The glass tank fills the bottom 35 percent of the frame, very close to the lens, its front glass wall about 30 centimeters from the camera, large in frame and closer to the camera than his face; the salmon fillet sits in the center of that lower third and is the brightest thing in the frame. From the chest up, his head and upper chest clear and centered in the upper half of the frame, his face about 70 centimeters from the lens. Nothing else competes with the salmon fillet. The background is reduced by framing, never by blur.",
  "camera": "phone camera on a small tripod at chest height, 26 mm wide lens, straight on, slight downward angle toward the work surface, fixed",
  "lighting": "Neutral overcast daylight from a window, the outside clearly visible through the window, soft even light on the face with no harsh shadows.",
  "state": "Start frame: the salmon fillet is half submerged and still perfectly whole, ripples on the water. Eva Dall looks into the lens, caught mid-sentence, lips naturally parted, animated expression.",
  "realism": "Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday reality, background fully in focus, everything in sharp focus, no blur, no bokeh, no AI polish, no beauty smoothing, no warm orange color cast, no yellow tint, no golden glow, no golden hour light, no sunset, no captions, no subtitles, no words overlaid on the image.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no printed labels or lettering on any container or package, no studio, no plastic-looking human skin, no extra fingers, no supernatural lighting, no blur, no bokeh, no artificial lighting, no warm orange color cast, no yellow tint, no golden glow, no golden hour light, no sunset, no de-aging, no beauty smoothing, no visible phone, no HDR, no cinematic lighting, no second person in frame, no aquarium gravel, no aquarium plants or decorations, no live fish swimming, no lid on the tank, no cooked fish, no broken or flaking fillet yet"
}
```

## K02 · T2 · GERAR DO ZERO · ÂNCORA EVA DALL

> ### 📎 ANEXAR: **1 IMAGEM**
> **1️⃣ ÂNCORA EVA DALL** `producao/_ancoras/eva_dall_ancora.jpeg`
>
> ### 🆕 GERAR DO ZERO

Cena: close do aquário, o filé inteiro no fundo antes de se desmanchar.

```json
{
  "shot_id": "K02_t2_eva_dall",
  "format": "IMPORTANT: THIS IS IPHONE FOOTAGE. Vertical 9:16.",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "reference_use": "Use the attached image only for Eva Dall's exact identity, wardrobe and own setting. Do not copy its pose or framing.",
  "identity_main": "The exact fictional AI character Eva Dall, explicitly male: Black American man around forty-nine, medium brown skin, lean athletic build, long oval face, dark brown eyes, subtle freckles and moles, very long locs mixing black, grey and silver, grey goatee and moustache, brown leather cap worn backward.",
  "wardrobe": "White ribbed tank top and a thin silver chain.",
  "scene": "His own modern white kitchen, the same room as the reference image, unchanged: a strongly veined dark green marble counter in front of him, a matching dark green marble wall behind the stove at the left, tall windows to the right and a small American flag on the shelf beside a small potted plant.",
  "prop": "A rectangular clear glass tank with no lid, shaped like a small aquarium about as wide as his shoulders and one hand deep, stands on the dark green veined marble counter, filled with clear hot water, seen at water level through its front glass wall. One whole thick raw salmon fillet, bright orange with thin white fat lines, rests flat on the glass bottom in the center of the tank, intact. Nothing else is inside the tank.",
  "posture": "Behind the tank only Eva Dall's torso is visible, his white ribbed tank top and thin silver chain, with the fingertips of one hand resting on the top edge of the tank. His face is above the top edge of the frame.",
  "composition": "Close shot at tank height: the tank fills the frame from the bottom edge up to about 75 percent of its height, its front glass wall about 20 centimeters from the lens, very close to the lens, large in frame; the salmon fillet sits in the center of the frame, larger than his hand. Above the waterline only his torso. No face in frame. The background is reduced by framing, never by blur.",
  "camera": "phone camera low, at counter level, at the height of the water, about 20 centimeters from the front glass, 26 mm wide lens, straight on, fixed",
  "lighting": "Neutral overcast daylight from a window, the outside clearly visible through the window, soft even light on the face with no harsh shadows.",
  "state": "Start frame: the water is calm and clear, the fillet lies whole and still on the bottom, not a single flake floating yet.",
  "realism": "Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday reality, background fully in focus, everything in sharp focus, no blur, no bokeh, no AI polish, no beauty smoothing, no warm orange color cast, no yellow tint, no golden glow, no golden hour light, no sunset, no captions, no subtitles, no words overlaid on the image.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no printed labels or lettering on any container or package, no studio, no plastic-looking human skin, no extra fingers, no supernatural lighting, no blur, no bokeh, no artificial lighting, no warm orange color cast, no yellow tint, no golden glow, no golden hour light, no sunset, no de-aging, no beauty smoothing, no visible phone, no HDR, no cinematic lighting, no second person in frame, no aquarium gravel, no aquarium plants or decorations, no live fish swimming, no lid on the tank, no cooked fish, no face in frame, no broken or flaking fillet yet"
}
```

## K03 · T3 · GERAR DO ZERO · ÂNCORA EVA DALL

> ### 📎 ANEXAR: **1 IMAGEM**
> **1️⃣ ÂNCORA EVA DALL** `producao/_ancoras/eva_dall_ancora.jpeg`
>
> ### 🆕 GERAR DO ZERO

Cena: salmão inteiro entrando na água fria.

```json
{
  "shot_id": "K03_t3_eva_dall",
  "format": "IMPORTANT: THIS IS IPHONE FOOTAGE. Vertical 9:16.",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "reference_use": "Use the attached image only for Eva Dall's exact identity, wardrobe and own setting. Do not copy its pose or framing.",
  "identity_main": "The exact fictional AI character Eva Dall, explicitly male: Black American man around forty-nine, medium brown skin, lean athletic build, long oval face, dark brown eyes, subtle freckles and moles, very long locs mixing black, grey and silver, grey goatee and moustache, brown leather cap worn backward.",
  "wardrobe": "White ribbed tank top and a thin silver chain.",
  "scene": "His own modern white kitchen, the same room as the reference image, unchanged: a strongly veined dark green marble counter in front of him, a matching dark green marble wall behind the stove at the left, tall windows to the right and a small American flag on the shelf beside a small potted plant.",
  "prop": "A rectangular clear glass tank with no lid, shaped like a small aquarium about as wide as his shoulders and one hand deep, stands on the dark green veined marble counter, filled with clear cold water. Eva Dall's right hand holds a whole raw salmon by the back, silver skin with small black spots, head and tail intact, lying on its side and longer than the tank is deep, and lowers it into the water: the belly is just under the surface and the tail hangs over the front edge, with ripples around it. The work surface is otherwise empty.",
  "posture": "Eva Dall is standing behind his dark green marble counter, leaning slightly toward the camera, the right hand holding the fish over the tank, the left forearm resting on the work surface.",
  "composition": "The glass tank with the whole salmon fills the bottom 35 percent of the frame, very close to the lens, its front glass wall about 30 centimeters from the camera, large in frame and closer to the camera than his face; the salmon runs almost the full width of the frame. From the chest up, his head and upper chest clear and centered in the upper half of the frame, his face about 70 centimeters from the lens. Nothing else competes with the salmon. The background is reduced by framing, never by blur.",
  "camera": "phone camera on a small tripod at chest height, 26 mm wide lens, straight on, slight downward angle toward the work surface, fixed",
  "lighting": "Neutral overcast daylight from a window, the outside clearly visible through the window, soft even light on the face with no harsh shadows.",
  "state": "Start frame: the whole salmon is half in the water, not yet released. Eva Dall looks into the lens, caught mid-sentence, lips naturally parted, animated expression.",
  "realism": "Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday reality, background fully in focus, everything in sharp focus, no blur, no bokeh, no AI polish, no beauty smoothing, no warm orange color cast, no yellow tint, no golden glow, no golden hour light, no sunset, no captions, no subtitles, no words overlaid on the image.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no printed labels or lettering on any container or package, no studio, no plastic-looking human skin, no extra fingers, no supernatural lighting, no blur, no bokeh, no artificial lighting, no warm orange color cast, no yellow tint, no golden glow, no golden hour light, no sunset, no de-aging, no beauty smoothing, no visible phone, no HDR, no cinematic lighting, no second person in frame, no aquarium gravel, no aquarium plants or decorations, no live fish swimming, no lid on the tank, no cooked fish"
}
```

## K04 · T4 · GERAR DO ZERO · ÂNCORA EVA DALL

> ### 📎 ANEXAR: **1 IMAGEM**
> **1️⃣ ÂNCORA EVA DALL** `producao/_ancoras/eva_dall_ancora.jpeg`
>
> ### 🆕 GERAR DO ZERO

Cena: brócolis na tigela de vidro, água despejada.

```json
{
  "shot_id": "K04_t4_eva_dall",
  "format": "IMPORTANT: THIS IS IPHONE FOOTAGE. Vertical 9:16.",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "reference_use": "Use the attached image only for Eva Dall's exact identity, wardrobe and own setting. Do not copy its pose or framing.",
  "identity_main": "The exact fictional AI character Eva Dall, explicitly male: Black American man around forty-nine, medium brown skin, lean athletic build, long oval face, dark brown eyes, subtle freckles and moles, very long locs mixing black, grey and silver, grey goatee and moustache, brown leather cap worn backward.",
  "wardrobe": "White ribbed tank top and a thin silver chain.",
  "scene": "His own modern white kitchen, the same room as the reference image, unchanged: a strongly veined dark green marble counter in front of him, a matching dark green marble wall behind the stove at the left, tall windows to the right and a small American flag on the shelf beside a small potted plant.",
  "prop": "A round clear glass mixing bowl full of fresh, clean-looking bright green broccoli florets half covered in water stands on the dark green veined marble counter in the lower foreground. Eva Dall's right hand holds a clear plastic water bottle with no label, tilted over the bowl, pouring a steady stream of water onto the florets. A small plain clear glass vinegar cruet with no label stands on the work surface beside the bowl. Nothing else is on the work surface.",
  "posture": "Eva Dall is standing behind his dark green marble counter, leaning slightly toward the camera, the left hand resting flat on the work surface beside the bowl.",
  "composition": "The glass bowl of broccoli fills the bottom 30 percent of the frame, very close to the lens, about 30 centimeters from the camera, large in frame and closer to the camera than his face. From the chest up, his head and upper chest clear and centered in the upper half of the frame, his face about 70 centimeters from the lens. Nothing else competes with the broccoli bowl. The background is reduced by framing, never by blur.",
  "camera": "phone camera on a small tripod at chest height, 26 mm wide lens, straight on, slight downward angle toward the work surface, fixed",
  "lighting": "Neutral overcast daylight from a window, the outside clearly visible through the window, soft even light on the face with no harsh shadows.",
  "state": "Start frame: water is streaming from the water bottle onto the broccoli, small splashes on the surface. Eva Dall looks into the lens, caught mid-sentence, lips naturally parted, animated expression.",
  "realism": "Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday reality, background fully in focus, everything in sharp focus, no blur, no bokeh, no AI polish, no beauty smoothing, no warm orange color cast, no yellow tint, no golden glow, no golden hour light, no sunset, no captions, no subtitles, no words overlaid on the image.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no printed labels or lettering on any container or package, no studio, no plastic-looking human skin, no extra fingers, no supernatural lighting, no blur, no bokeh, no artificial lighting, no warm orange color cast, no yellow tint, no golden glow, no golden hour light, no sunset, no de-aging, no beauty smoothing, no visible phone, no HDR, no cinematic lighting, no second person in frame, no cooked broccoli, no sauce, no plate"
}
```

## K05 · T5 · GERAR DO ZERO · ÂNCORA EVA DALL

> ### 📎 ANEXAR: **1 IMAGEM**
> **1️⃣ ÂNCORA EVA DALL** `producao/_ancoras/eva_dall_ancora.jpeg`
>
> ### 🆕 GERAR DO ZERO

Cena: tábua com frango, salmão e truta, CTA.

```json
{
  "shot_id": "K05_t5_eva_dall",
  "format": "IMPORTANT: THIS IS IPHONE FOOTAGE. Vertical 9:16.",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "reference_use": "Use the attached image only for Eva Dall's exact identity, wardrobe and own setting. Do not copy its pose or framing.",
  "identity_main": "The exact fictional AI character Eva Dall, explicitly male: Black American man around forty-nine, medium brown skin, lean athletic build, long oval face, dark brown eyes, subtle freckles and moles, very long locs mixing black, grey and silver, grey goatee and moustache, brown leather cap worn backward.",
  "wardrobe": "White ribbed tank top and a thin silver chain.",
  "scene": "His own modern white kitchen, the same room as the reference image, unchanged: a strongly veined dark green marble counter in front of him, a matching dark green marble wall behind the stove at the left, tall windows to the right and a small American flag on the shelf beside a small potted plant.",
  "prop": "Eva Dall holds a thick rectangular wooden cutting board horizontally with both hands, pushed toward the lens, very close to the camera in the lower foreground, large in frame: on the board a whole raw chicken on the left, three thick raw salmon fillet portions standing side by side in the middle, bright orange with white fat lines, and a whole raw trout with silver and pink skin on the right. Nothing else is on the board.",
  "posture": "Eva Dall is standing behind his dark green marble counter, leaning slightly toward the camera, holding the board by its two short ends.",
  "composition": "The cutting board fills the bottom 35 percent of the frame, its front edge about 30 centimeters from the lens, closer to the camera than his face, the salmon portions in the center. From the chest up, his head and upper chest clear and centered in the upper half of the frame, his face about 70 centimeters from the lens. This is the tightest talking shot of the video. The background is reduced by framing, never by blur.",
  "camera": "phone camera on a small tripod at chest height, 26 mm wide lens, straight on, slight downward angle toward the work surface, fixed",
  "lighting": "Neutral overcast daylight from a window, the outside clearly visible through the window, soft even light on the face with no harsh shadows.",
  "state": "Start frame: Eva Dall smiles wide with excitement, eyes on the lens, caught mid-sentence, lips naturally parted, animated expression.",
  "realism": "Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday reality, background fully in focus, everything in sharp focus, no blur, no bokeh, no AI polish, no beauty smoothing, no warm orange color cast, no yellow tint, no golden glow, no golden hour light, no sunset, no captions, no subtitles, no words overlaid on the image.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no printed labels or lettering on any container or package, no studio, no plastic-looking human skin, no extra fingers, no supernatural lighting, no blur, no bokeh, no artificial lighting, no warm orange color cast, no yellow tint, no golden glow, no golden hour light, no sunset, no de-aging, no beauty smoothing, no visible phone, no HDR, no cinematic lighting, no second person in frame, no cooked food, no packaging, no price tags"
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
o avatar Eva Dall, homem, fala em inglês com sotaque americano de um homem negro americano, voz média e amigável de um homem de quase cinquenta anos, entonação direta e curiosa, de quem vai mostrar um teste que pouca gente conhece, voz autêntica, como se exigisse ser ouvido, a seguinte frase: "If you bought salmon at the market, put it in hot water."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Eva Dall termina de baixar o filé de salmão na água do aquário, solta o filé e ele desce devagar até o fundo; ele fala olhando para a câmera. Ele diz a frase em ritmo natural logo no começo e depois fica olhando para o aquário em silêncio.

câmera: fixa, no tripé, na altura do peito

som ambiente: cozinha residencial tranquila, som leve de água mexendo, sem música
```

### V02 · T2 · usa K02

```text
o avatar Eva Dall, homem, fora de quadro (só o torso aparece, o rosto fica acima do quadro), fala em inglês com sotaque americano de um homem negro americano, voz média e amigável de um homem de quase cinquenta anos, entonação séria e firme, com um toque de alerta, voz autêntica, como se exigisse ser ouvido, a seguinte frase: "If it falls apart easily, the meat isn't real."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: o filé de salmão parado no fundo do aquário começa a rachar pelas linhas brancas de gordura e se desfaz em dezenas de lascas laranja que se soltam e flutuam pela água; atrás do vidro só aparece o torso, parado, com a mão apoiada na borda do aquário. A voz diz a frase em ritmo natural logo no começo e o resto do clipe é o filé se desmanchando.

câmera: fixa, na altura da água, colada no vidro do aquário

som ambiente: cozinha residencial tranquila, som leve e abafado de água, sem música
```

### V03 · T3 · usa K03

```text
o avatar Eva Dall, homem, fala em inglês com sotaque americano de um homem negro americano, voz média e amigável de um homem de quase cinquenta anos, entonação didática e confiante, explicando com clareza, voz autêntica, como se exigisse ser ouvido, a seguinte frase: "Number two, put your fish in cold water. If it sinks, it's fresh. If it floats, it's been sitting on the shelf too long."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Eva Dall solta o salmão inteiro dentro da água; o peixe afunda devagar e fica deitado no fundo do aquário; ele apoia os braços dos dois lados do aquário e fala para a câmera.

câmera: fixa, no tripé, com uma leve descida e aproximação contínua, sem corte

som ambiente: cozinha residencial tranquila, som de água mexendo quando o peixe entra, sem música
```

### V04 · T4 · usa K04

```text
o avatar Eva Dall, homem, fala em inglês com sotaque americano de um homem negro americano, voz média e amigável de um homem de quase cinquenta anos, entonação didática, com um leve tom de nojo no fim da frase, voz autêntica, como se exigisse ser ouvido, a seguinte frase: "Number three, put broccoli in water with a splash of vinegar. Any hidden insects and their eggs will come loose and end up in the water."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Eva Dall despeja a água da garrafa sobre os brócolis, larga a garrafa, pega a garrafinha de vinagre e despeja um fio dentro da tigela; na metade do clipe a câmera avança devagar até a tigela encher o quadro e o rosto sair por cima; no close, pequenas larvinhas finas e bege se soltam dos floretes e ficam boiando na água.

câmera: fixa no começo, depois push-in lento e contínuo até a tigela, sem corte

som ambiente: cozinha residencial tranquila, som da água caindo na tigela, sem música
```

### V05 · T5 · usa K05

```text
o avatar Eva Dall, homem, fala em inglês com sotaque americano de um homem negro americano, voz média e amigável de um homem de quase cinquenta anos, entonação animada e convidativa, sorrindo, voz autêntica, como se exigisse ser ouvido, a seguinte frase: "I have tips like this for almost every food you buy. Save this and comment with other foods for more. Follow me so you don't miss out."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Eva Dall segura a tábua com as duas mãos e fala para a câmera, sorrindo animado; nos últimos segundos a câmera avança devagar até a tábua, o rosto sai por cima e o quadro fecha nas postas de salmão.

câmera: fixa, depois push-in lento e contínuo até a tábua nos últimos segundos, sem corte

som ambiente: cozinha residencial tranquila, sem música
```

## Mapa de âncoras

| Keyframe | Referências a anexar | Modelo |
|---|---|---|
| K01 | ÂNCORA EVA DALL + FRAME DO MODELO (`input/frames_modelo/K01_modelo.png`, só composição) | Nano Banana 2, 9:16, 4 imagens |
| K02 a K05 | ÂNCORA EVA DALL | Nano Banana 2, 9:16, 4 imagens |

## Montagem no CapCut

1. Clipes numerados na ordem: V01, V02, V03, V04, V05.
2. Cortar cada clipe no tempo da cena do modelo: V01 0,0 a 3,0 s; V02 3,0 a 7,5 s; V03 7,5 a 15,1 s; V04 15,1 a 22,8 s; V05 22,8 a 30,0 s.
3. Zero tempo morto: todo clipe começa já falando. Isolate Voice / Keep Vocal no áudio.
4. V01 e V02 são cenas curtas: a fala vem no começo; cortar V01 logo depois de "hot water" e V02 quando o filé estiver todo em lascas, no tempo da cena.
5. Legenda de 2 a 3 palavras por vez, caixa alta, fonte bold branca com contorno preto e a palavra falada em amarelo, no meio do quadro, do começo ao fim, igual ao modelo.
6. Sem Voice Changer: a voz vem do prompt de cada V.
7. Música só do V03 em diante, nunca no gancho (V01 e V02), entre -19 e -20 dB, fora da biblioteca do TikTok.
8. Rótulo pequeno `AI-generated` num canto do vídeo.

## Gates de qualidade

1. Fala de cada V igual ao ROTEIRO, palavra por palavra.
2. Um take por cena do modelo; T1 e T2 marcados CENA CURTA; nenhum take acima de 29 palavras.
3. Bandeira dos EUA no campo scene de todo K.
4. Zero travessão.
5. Growth: sem keyword, sem produto, sem link; CTA save + comment + follow do próprio modelo.
6. Produto fora de quadro, nenhuma garrafa ou embalagem com marca ou texto.
7. Negative sem termo sensível.
8. GATE_VISUAL Partes 1 a 3 em todo K: herói colado na lente com medida, luz neutra, sem tom quente, sem blur, trecho de realismo.
9. Gancho fiel no conteúdo: filé de salmão cru entrando no aquário de água, falado desde o segundo 0; payoff do filé se desmanchando no close do T2.
10. Um K = um V; os reveals (filé desmanchando, peixe afundando, larvinhas, push-in) acontecem dentro do clipe, a imagem é o estado inicial.
11. FICHA_FRAMES.md com placar de cada K antes do envio.

