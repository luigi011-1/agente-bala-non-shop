# holistic.brandon | Ângulo 1 Natural Rems Sea Moss | Cinco testes de comida falsificada | Pacote de Prompts

Vídeo modelo: `input/reference_video.mp4` (57,8 s, pessoa real)

Âncora: `producao/_ancoras/holistic_brandon_ancora.jpg` · Foto do produto: `producao/_ancoras/natural_rems_seamoss_produto.jpg`

Funil: venda Amazon. Frasco em quadro, "Search Natural Rems Sea Moss on Amazon" primeiro, link da legenda do post depois, fim. Rodada de validação, gancho fiel ao modelo.

## Índice de geração

| Take | Keyframe | Anexar | Ação |
|---|---|---|---|
| T1 | K01 | ÂNCORA HOLISTIC BRANDON + FRAME DO MODELO (K01) | GERAR DO ZERO |
| T2 | K02 | ÂNCORA HOLISTIC BRANDON + FRAME DO MODELO (K02) | GERAR DO ZERO |
| T3 | K03 | ÂNCORA HOLISTIC BRANDON + FRAME DO MODELO (K03) | GERAR DO ZERO |
| T4 | K04 | ÂNCORA HOLISTIC BRANDON + FRAME DO MODELO (K04) | GERAR DO ZERO |
| T5 | K05 | ÂNCORA HOLISTIC BRANDON + FRAME DO MODELO (K05) | GERAR DO ZERO |
| T6 | K06 | ÂNCORA HOLISTIC BRANDON + FRAME DO MODELO (K06) | GERAR DO ZERO |
| T7 | K07 | ÂNCORA HOLISTIC BRANDON + FRAME DO MODELO (K07) | GERAR DO ZERO |
| T8 | K08 | ÂNCORA HOLISTIC BRANDON + FRAME DO MODELO (K08) | GERAR DO ZERO |
| T9 | K09 | ÂNCORA HOLISTIC BRANDON + FRAME DO MODELO + FOTO DO POTE (K09) | GERAR DO ZERO |
| T10 | K10 | ÂNCORA HOLISTIC BRANDON + FRAME DO MODELO + FOTO DO POTE (K10) | GERAR DO ZERO |

Todo K é GERAR DO ZERO: o bloco do Flow é autossuficiente e cada K descreve o cenário inteiro, então não existe `EDITAR do K__` aqui. O frame do modelo de cada K entra só como composição.

## Trava de identidade e continuidade

- Identidade: The exact fictional AI character holistic.brandon: Black mixed-race American woman around thirty, athletic and toned, medium light-brown skin with light freckles across the nose and cheeks, dark brown eyes, defined eyebrows, full lips, hair in tight cornrows that turn into long loose braids falling over both shoulders, finished with small wooden and gold beads, a black floral blackwork tattoo sleeve on her right arm, a small line tattoo on her left upper arm and small fine-line tattoos on her chest near the collarbones. She reads as an ordinary anonymous American fitness coach, not resembling anyone famous.
- Roupa (fixa da conta): Plain white ribbed tank top with nothing printed or written on it, loose black training shorts ending at mid-thigh, a thin gold chain with a small gold cross pendant and small stud earrings.
- Cenário-base (fixo da conta): Her own garage gym, the same room as the reference: a white-painted concrete block wall and a dark wooden slat ceiling, a red neon sign reading TRAIN PRAY REPEAT on the wall at the left, a whiteboard with handwritten black marker reading STAY READY. STAY DISCIPLINED. on the right, and a small American flag pinned above the whiteboard, discreet but clearly visible and in focus. The background is reduced by framing, never by blur.
- Luz: Neutral overcast daylight from a large window out of frame, soft even light on her face and hands with no harsh shadows. The red neon glows on the wall but does not tint her skin.
- Voz (mesmo timbre em todos os V): voz feminina clara e firme de uma mulher de uns trinta anos, sotaque americano de uma mulher negra americana.
- Sem 2ª pessoa.

## Trava do prop herói

- Gancho: a clear rectangular glass tank, like a small empty aquarium, filled with cold clear water; colheres de metal com grãos inteiros de pimenta-do-reino; no K02 alguns grãos marrons enrugados boiando.
- Testes: duas batatas no mesmo aquário; two tall clear drinking glasses side by side com cúrcuma laranja e com café moído; duas canelas (a fina em camadas, a cássia grossa).
- Fecho: os ingredientes lined up on the table: two small clear glasses of water, two cinnamon sticks, a small pile of black peppercorns and one potato.
- Produto (T9 e T10): the Natural Rems Sea Moss Gummies jar exactly as in the attached product photo: a short wide jar of dark amber plastic with a black screw cap, a pale sage-green label with dark green text, the Natural Rems logo with three leaves at the top, the big title Sea Moss Gummies, a pill-shaped badge reading 6000 MG | 16-IN-1, the line GREEN APPLE FLAVOR, two columns of dark green ingredient pills, green seaweed illustrations on the sides and a small 30 Gummies badge. Referência: `producao/_ancoras/natural_rems_seamoss_produto.jpg`, só o pote da frente, sem a faixa MADE IN USA, sem o pote de trás e sem as gomas soltas.
- Nada dos testes tem marca legível.

## Trava da 2ª pessoa (REF-A)

- Não se aplica: não há 2ª pessoa.

## Prompts de imagem

## K01 · T1 · GERAR DO ZERO · ÂNCORA HOLISTIC BRANDON + FRAME DO MODELO

> ### 📎 ANEXAR: **2 IMAGENS**
> **1️⃣ ÂNCORA HOLISTIC BRANDON** `producao/_ancoras/holistic_brandon_ancora.jpg`
> **2️⃣ FRAME DO MODELO, só composição** `input/frames_modelo/K01_modelo.png`
>
> ### 🆕 GERAR DO ZERO

Cena: gancho, pimenta no aquário colado na lente.

```json
{
  "shot_id": "K01_t1_brandon",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "reference_use": "Use the first attached image only for Brandon's exact identity, wardrobe and her own garage gym. Use the second attached image only as a composition reference for the camera position, framing and the action; do not copy its man, glasses, gray t-shirt, kitchen, marble counter, cartoon magnet or the caption text.",
  "identity_main": "The exact fictional AI character holistic.brandon: Black mixed-race American woman around thirty, athletic and toned, medium light-brown skin with light freckles across the nose and cheeks, dark brown eyes, defined eyebrows, full lips, hair in tight cornrows that turn into long loose braids falling over both shoulders, finished with small wooden and gold beads, a black floral blackwork tattoo sleeve on her right arm, a small line tattoo on her left upper arm and small fine-line tattoos on her chest near the collarbones. She reads as an ordinary anonymous American fitness coach, not resembling anyone famous.",
  "wardrobe": "Plain white ribbed tank top with nothing printed or written on it, loose black training shorts ending at mid-thigh, a thin gold chain with a small gold cross pendant and small stud earrings.",
  "scene": "Her own garage gym, the same room as the reference: a white-painted concrete block wall and a dark wooden slat ceiling, a red neon sign reading TRAIN PRAY REPEAT on the wall at the left, a whiteboard with handwritten black marker reading STAY READY. STAY DISCIPLINED. on the right, and a small American flag pinned above the whiteboard, discreet but clearly visible and in focus. The background is reduced by framing, never by blur.",
  "prop": "A clear rectangular glass tank, like a small empty aquarium, filled with cold clear water, standing on the black table in front of her very close to the lens, the water clean and empty. In each hand she holds a metal spoon heaped with whole black peppercorns, both spoons tilted right above the water.",
  "posture": "Brandon stands behind the black table in front of her, leaning forward over it, seen from the waist up.",
  "composition": "Close shot from chest height: the phone lens is about 35 centimeters from the tank, which fills the lower 40 percent of the frame almost edge to edge, closer to the camera than her face; her face and shoulders fill the upper part. Nothing else is on the table. The background is reduced by framing, never by blur.",
  "camera": "phone held at chest height about 35 centimeters from the tank, standard 1x lens tilted slightly down",
  "lighting": "Neutral overcast daylight from a large window out of frame, soft even light on her face and hands with no harsh shadows. The red neon glows on the wall but does not tint her skin.",
  "state": "Start frame: the first peppercorns are just tipping off the spoons. Brandon is caught mid-sentence, lips naturally parted, animated expression, looking straight into the lens.",
  "realism": "Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday reality, background fully in focus, everything in sharp focus, no AI polish, no beauty smoothing.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no studio, no plastic-looking skin, no extra fingers, no third hand, no blur, no bokeh, no warm orange color cast, no yellow tint, no golden glow, no golden hour light, no sunset, no HDR, no cinematic lighting, no de-aging, no beauty smoothing, no visible phone, no glasses, no gray t-shirt, no kitchen cabinets, no white marble counter, no cartoon magnet, no silver cross, no white coat, no second person, no readable lettering on the tank, glasses, spoons or jars, no peppercorns in the water yet"
}
```

## K02 · T2 · GERAR DO ZERO · ÂNCORA HOLISTIC BRANDON + FRAME DO MODELO

> ### 📎 ANEXAR: **2 IMAGENS**
> **1️⃣ ÂNCORA HOLISTIC BRANDON** `producao/_ancoras/holistic_brandon_ancora.jpg`
> **2️⃣ FRAME DO MODELO, só composição** `input/frames_modelo/K02_modelo.png`
>
> ### 🆕 GERAR DO ZERO

Cena: pimenta no fundo, alguns grãos boiando.

```json
{
  "shot_id": "K02_t2_brandon",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "reference_use": "Use the first attached image only for Brandon's exact identity, wardrobe and her own garage gym. Use the second attached image only as a composition reference for the camera position, framing and the action; do not copy its man, glasses, gray t-shirt, kitchen, marble counter, cartoon magnet or the caption text.",
  "identity_main": "The exact fictional AI character holistic.brandon: Black mixed-race American woman around thirty, athletic and toned, medium light-brown skin with light freckles across the nose and cheeks, dark brown eyes, defined eyebrows, full lips, hair in tight cornrows that turn into long loose braids falling over both shoulders, finished with small wooden and gold beads, a black floral blackwork tattoo sleeve on her right arm, a small line tattoo on her left upper arm and small fine-line tattoos on her chest near the collarbones. She reads as an ordinary anonymous American fitness coach, not resembling anyone famous.",
  "wardrobe": "Plain white ribbed tank top with nothing printed or written on it, loose black training shorts ending at mid-thigh, a thin gold chain with a small gold cross pendant and small stud earrings.",
  "scene": "Her own garage gym, the same room as the reference: a white-painted concrete block wall and a dark wooden slat ceiling, a red neon sign reading TRAIN PRAY REPEAT on the wall at the left, a whiteboard with handwritten black marker reading STAY READY. STAY DISCIPLINED. on the right, and a small American flag pinned above the whiteboard, discreet but clearly visible and in focus. The background is reduced by framing, never by blur.",
  "prop": "A clear rectangular glass tank, like a small empty aquarium, filled with cold clear water, standing on the black table in front of her very close to the lens: most of the black peppercorns lie on the bottom of the tank, a few lighter brown wrinkled seeds float on the surface, and some grains are still sinking through the water. Her right index finger points at the floating seeds; the empty spoon rests in her left hand.",
  "posture": "Brandon stands behind the black table in front of her, leaning forward over it, seen from the waist up.",
  "composition": "Close shot from chest height: the phone lens is about 35 centimeters from the tank, which fills the lower 40 percent of the frame almost edge to edge, closer to the camera than her face; her face and shoulders fill the upper part. Nothing else is on the table. The background is reduced by framing, never by blur.",
  "camera": "phone held at chest height about 35 centimeters from the tank, standard 1x lens tilted slightly down",
  "lighting": "Neutral overcast daylight from a large window out of frame, soft even light on her face and hands with no harsh shadows. The red neon glows on the wall but does not tint her skin.",
  "state": "Start frame: the floating seeds are clearly visible on the surface. Brandon is caught mid-sentence, lips naturally parted, animated expression, looking straight into the lens.",
  "realism": "Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday reality, background fully in focus, everything in sharp focus, no AI polish, no beauty smoothing.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no studio, no plastic-looking skin, no extra fingers, no third hand, no blur, no bokeh, no warm orange color cast, no yellow tint, no golden glow, no golden hour light, no sunset, no HDR, no cinematic lighting, no de-aging, no beauty smoothing, no visible phone, no glasses, no gray t-shirt, no kitchen cabinets, no white marble counter, no cartoon magnet, no silver cross, no white coat, no second person, no readable lettering on the tank, glasses, spoons or jars"
}
```

## K03 · T3 · GERAR DO ZERO · ÂNCORA HOLISTIC BRANDON + FRAME DO MODELO

> ### 📎 ANEXAR: **2 IMAGENS**
> **1️⃣ ÂNCORA HOLISTIC BRANDON** `producao/_ancoras/holistic_brandon_ancora.jpg`
> **2️⃣ FRAME DO MODELO, só composição** `input/frames_modelo/K03_modelo.png`
>
> ### 🆕 GERAR DO ZERO

Cena: batatas sobre o aquário.

```json
{
  "shot_id": "K03_t3_brandon",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "reference_use": "Use the first attached image only for Brandon's exact identity, wardrobe and her own garage gym. Use the second attached image only as a composition reference for the camera position, framing and the action; do not copy its man, glasses, gray t-shirt, kitchen, marble counter, cartoon magnet or the caption text.",
  "identity_main": "The exact fictional AI character holistic.brandon: Black mixed-race American woman around thirty, athletic and toned, medium light-brown skin with light freckles across the nose and cheeks, dark brown eyes, defined eyebrows, full lips, hair in tight cornrows that turn into long loose braids falling over both shoulders, finished with small wooden and gold beads, a black floral blackwork tattoo sleeve on her right arm, a small line tattoo on her left upper arm and small fine-line tattoos on her chest near the collarbones. She reads as an ordinary anonymous American fitness coach, not resembling anyone famous.",
  "wardrobe": "Plain white ribbed tank top with nothing printed or written on it, loose black training shorts ending at mid-thigh, a thin gold chain with a small gold cross pendant and small stud earrings.",
  "scene": "Her own garage gym, the same room as the reference: a white-painted concrete block wall and a dark wooden slat ceiling, a red neon sign reading TRAIN PRAY REPEAT on the wall at the left, a whiteboard with handwritten black marker reading STAY READY. STAY DISCIPLINED. on the right, and a small American flag pinned above the whiteboard, discreet but clearly visible and in focus. The background is reduced by framing, never by blur.",
  "prop": "A clear rectangular glass tank, like a small empty aquarium, filled with cold clear water, standing on the black table in front of her very close to the lens, the water clean. She holds one brown russet potato in each hand right above the water.",
  "posture": "Brandon stands behind the black table in front of her, leaning forward over it, seen from the waist up.",
  "composition": "Close shot from chest height: the phone lens is about 35 centimeters from the tank, which fills the lower 40 percent of the frame almost edge to edge, closer to the camera than her face; her face and shoulders fill the upper part. Nothing else is on the table. The background is reduced by framing, never by blur.",
  "camera": "phone held at chest height about 35 centimeters from the tank, standard 1x lens tilted slightly down",
  "lighting": "Neutral overcast daylight from a large window out of frame, soft even light on her face and hands with no harsh shadows. The red neon glows on the wall but does not tint her skin.",
  "state": "Start frame: both potatoes are still in her hands, about to drop. Brandon is caught mid-sentence, lips naturally parted, animated expression, looking straight into the lens.",
  "realism": "Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday reality, background fully in focus, everything in sharp focus, no AI polish, no beauty smoothing.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no studio, no plastic-looking skin, no extra fingers, no third hand, no blur, no bokeh, no warm orange color cast, no yellow tint, no golden glow, no golden hour light, no sunset, no HDR, no cinematic lighting, no de-aging, no beauty smoothing, no visible phone, no glasses, no gray t-shirt, no kitchen cabinets, no white marble counter, no cartoon magnet, no silver cross, no white coat, no second person, no readable lettering on the tank, glasses, spoons or jars, no potatoes in the water yet"
}
```

## K04 · T4 · GERAR DO ZERO · ÂNCORA HOLISTIC BRANDON + FRAME DO MODELO

> ### 📎 ANEXAR: **2 IMAGENS**
> **1️⃣ ÂNCORA HOLISTIC BRANDON** `producao/_ancoras/holistic_brandon_ancora.jpg`
> **2️⃣ FRAME DO MODELO, só composição** `input/frames_modelo/K04_modelo.png`
>
> ### 🆕 GERAR DO ZERO

Cena: cúrcuma nos dois copos.

```json
{
  "shot_id": "K04_t4_brandon",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "reference_use": "Use the first attached image only for Brandon's exact identity, wardrobe and her own garage gym. Use the second attached image only as a composition reference for the camera position, framing and the action; do not copy its man, glasses, gray t-shirt, kitchen, marble counter, cartoon magnet or the caption text.",
  "identity_main": "The exact fictional AI character holistic.brandon: Black mixed-race American woman around thirty, athletic and toned, medium light-brown skin with light freckles across the nose and cheeks, dark brown eyes, defined eyebrows, full lips, hair in tight cornrows that turn into long loose braids falling over both shoulders, finished with small wooden and gold beads, a black floral blackwork tattoo sleeve on her right arm, a small line tattoo on her left upper arm and small fine-line tattoos on her chest near the collarbones. She reads as an ordinary anonymous American fitness coach, not resembling anyone famous.",
  "wardrobe": "Plain white ribbed tank top with nothing printed or written on it, loose black training shorts ending at mid-thigh, a thin gold chain with a small gold cross pendant and small stud earrings.",
  "scene": "Her own garage gym, the same room as the reference: a white-painted concrete block wall and a dark wooden slat ceiling, a red neon sign reading TRAIN PRAY REPEAT on the wall at the left, a whiteboard with handwritten black marker reading STAY READY. STAY DISCIPLINED. on the right, and a small American flag pinned above the whiteboard, discreet but clearly visible and in focus. The background is reduced by framing, never by blur.",
  "prop": "Two tall clear drinking glasses side by side, full of warm clear water, standing on the black table in front of her very close to the lens. In each hand she holds a metal spoon heaped with bright orange turmeric powder, dipped just into the water of each glass.",
  "posture": "Brandon stands behind the black table in front of her, leaning forward over it, seen from the waist up.",
  "composition": "Close shot from chest height: the phone lens is about 30 centimeters from the glasses, which fill the lower 35 percent of the frame, closer to the camera than her face; her face fills the upper part. Nothing else is on the table. The background is reduced by framing, never by blur.",
  "camera": "phone held at chest height about 30 centimeters from the glasses, standard 1x lens tilted slightly down",
  "lighting": "Neutral overcast daylight from a large window out of frame, soft even light on her face and hands with no harsh shadows. The red neon glows on the wall but does not tint her skin.",
  "state": "Start frame: the water in both glasses is still clear. Brandon is caught mid-sentence, lips naturally parted, animated expression, looking straight into the lens.",
  "realism": "Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday reality, background fully in focus, everything in sharp focus, no AI polish, no beauty smoothing.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no studio, no plastic-looking skin, no extra fingers, no third hand, no blur, no bokeh, no warm orange color cast, no yellow tint, no golden glow, no golden hour light, no sunset, no HDR, no cinematic lighting, no de-aging, no beauty smoothing, no visible phone, no glasses, no gray t-shirt, no kitchen cabinets, no white marble counter, no cartoon magnet, no silver cross, no white coat, no second person, no readable lettering on the tank, glasses, spoons or jars, no yellow water yet"
}
```

## K05 · T5 · GERAR DO ZERO · ÂNCORA HOLISTIC BRANDON + FRAME DO MODELO

> ### 📎 ANEXAR: **2 IMAGENS**
> **1️⃣ ÂNCORA HOLISTIC BRANDON** `producao/_ancoras/holistic_brandon_ancora.jpg`
> **2️⃣ FRAME DO MODELO, só composição** `input/frames_modelo/K05_modelo.png`
>
> ### 🆕 GERAR DO ZERO

Cena: café nos dois copos.

```json
{
  "shot_id": "K05_t5_brandon",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "reference_use": "Use the first attached image only for Brandon's exact identity, wardrobe and her own garage gym. Use the second attached image only as a composition reference for the camera position, framing and the action; do not copy its man, glasses, gray t-shirt, kitchen, marble counter, cartoon magnet or the caption text.",
  "identity_main": "The exact fictional AI character holistic.brandon: Black mixed-race American woman around thirty, athletic and toned, medium light-brown skin with light freckles across the nose and cheeks, dark brown eyes, defined eyebrows, full lips, hair in tight cornrows that turn into long loose braids falling over both shoulders, finished with small wooden and gold beads, a black floral blackwork tattoo sleeve on her right arm, a small line tattoo on her left upper arm and small fine-line tattoos on her chest near the collarbones. She reads as an ordinary anonymous American fitness coach, not resembling anyone famous.",
  "wardrobe": "Plain white ribbed tank top with nothing printed or written on it, loose black training shorts ending at mid-thigh, a thin gold chain with a small gold cross pendant and small stud earrings.",
  "scene": "Her own garage gym, the same room as the reference: a white-painted concrete block wall and a dark wooden slat ceiling, a red neon sign reading TRAIN PRAY REPEAT on the wall at the left, a whiteboard with handwritten black marker reading STAY READY. STAY DISCIPLINED. on the right, and a small American flag pinned above the whiteboard, discreet but clearly visible and in focus. The background is reduced by framing, never by blur.",
  "prop": "Two tall clear drinking glasses side by side, full of cold clear water, standing on the black table in front of her very close to the lens. In each hand she holds a metal spoon heaped with dark brown ground coffee, held right above each glass.",
  "posture": "Brandon stands behind the black table in front of her, leaning forward over it, seen from the waist up.",
  "composition": "Close shot from chest height: the phone lens is about 30 centimeters from the glasses, which fill the lower 35 percent of the frame, closer to the camera than her face; her face fills the upper part. Nothing else is on the table. The background is reduced by framing, never by blur.",
  "camera": "phone held at chest height about 30 centimeters from the glasses, standard 1x lens tilted slightly down",
  "lighting": "Neutral overcast daylight from a large window out of frame, soft even light on her face and hands with no harsh shadows. The red neon glows on the wall but does not tint her skin.",
  "state": "Start frame: the coffee is still on the spoons and the water is clear. Brandon is caught mid-sentence, lips naturally parted, animated expression, looking straight into the lens.",
  "realism": "Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday reality, background fully in focus, everything in sharp focus, no AI polish, no beauty smoothing.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no studio, no plastic-looking skin, no extra fingers, no third hand, no blur, no bokeh, no warm orange color cast, no yellow tint, no golden glow, no golden hour light, no sunset, no HDR, no cinematic lighting, no de-aging, no beauty smoothing, no visible phone, no glasses, no gray t-shirt, no kitchen cabinets, no white marble counter, no cartoon magnet, no silver cross, no white coat, no second person, no readable lettering on the tank, glasses, spoons or jars, no coffee in the water yet"
}
```

## K06 · T6 · GERAR DO ZERO · ÂNCORA HOLISTIC BRANDON + FRAME DO MODELO

> ### 📎 ANEXAR: **2 IMAGENS**
> **1️⃣ ÂNCORA HOLISTIC BRANDON** `producao/_ancoras/holistic_brandon_ancora.jpg`
> **2️⃣ FRAME DO MODELO, só composição** `input/frames_modelo/K06_modelo.png`
>
> ### 🆕 GERAR DO ZERO

Cena: close das duas canelas.

```json
{
  "shot_id": "K06_t6_brandon",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "reference_use": "Use the first attached image only for Brandon's exact identity, wardrobe and her own garage gym. Use the second attached image only as a composition reference for the camera position, framing and the action; do not copy its man, glasses, gray t-shirt, kitchen, marble counter, cartoon magnet or the caption text.",
  "identity_main": "The exact fictional AI character holistic.brandon: Black mixed-race American woman around thirty, athletic and toned, medium light-brown skin with light freckles across the nose and cheeks, dark brown eyes, defined eyebrows, full lips, hair in tight cornrows that turn into long loose braids falling over both shoulders, finished with small wooden and gold beads, a black floral blackwork tattoo sleeve on her right arm, a small line tattoo on her left upper arm and small fine-line tattoos on her chest near the collarbones. She reads as an ordinary anonymous American fitness coach, not resembling anyone famous.",
  "wardrobe": "Plain white ribbed tank top with nothing printed or written on it, loose black training shorts ending at mid-thigh, a thin gold chain with a small gold cross pendant and small stud earrings.",
  "scene": "Her own garage gym, the same room as the reference: a white-painted concrete block wall and a dark wooden slat ceiling, a red neon sign reading TRAIN PRAY REPEAT on the wall at the left, a whiteboard with handwritten black marker reading STAY READY. STAY DISCIPLINED. on the right, and a small American flag pinned above the whiteboard, discreet but clearly visible and in focus. The background is reduced by framing, never by blur.",
  "prop": "In front of her face she holds two cinnamon sticks toward the lens, one in each hand: the left one thin and tightly rolled in many paper-thin brown layers like a cigar, the right one a single thick, hard, dark brown curl of bark.",
  "posture": "Brandon leans in close to the lens, the sticks held at mouth height on either side of her chin.",
  "composition": "Extreme close shot: the phone lens is about 15 centimeters from the cinnamon sticks, which fill the lower 40 percent of the frame, closer to the camera than her face; her face fills the upper part. The background is reduced by framing, never by blur.",
  "camera": "phone held just below eye height about 15 centimeters from the sticks, standard 1x lens, level",
  "lighting": "Neutral overcast daylight from a large window out of frame, soft even light on her face and hands with no harsh shadows. The red neon glows on the wall but does not tint her skin.",
  "state": "Start frame: both sticks are side by side and their layers are clearly visible. Brandon is caught mid-sentence, lips naturally parted, animated expression, looking straight into the lens.",
  "realism": "Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday reality, background fully in focus, everything in sharp focus, no AI polish, no beauty smoothing.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no studio, no plastic-looking skin, no extra fingers, no third hand, no blur, no bokeh, no warm orange color cast, no yellow tint, no golden glow, no golden hour light, no sunset, no HDR, no cinematic lighting, no de-aging, no beauty smoothing, no visible phone, no glasses, no gray t-shirt, no kitchen cabinets, no white marble counter, no cartoon magnet, no silver cross, no white coat, no second person"
}
```

## K07 · T7 · GERAR DO ZERO · ÂNCORA HOLISTIC BRANDON + FRAME DO MODELO

> ### 📎 ANEXAR: **2 IMAGENS**
> **1️⃣ ÂNCORA HOLISTIC BRANDON** `producao/_ancoras/holistic_brandon_ancora.jpg`
> **2️⃣ FRAME DO MODELO, só composição** `input/frames_modelo/K07_modelo.png`
>
> ### 🆕 GERAR DO ZERO

Cena: plano aberto, autoridade.

```json
{
  "shot_id": "K07_t7_brandon",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "reference_use": "Use the first attached image only for Brandon's exact identity, wardrobe and her own garage gym. Use the second attached image only as a composition reference for the camera position, framing and the action; do not copy its man, glasses, gray t-shirt, kitchen, marble counter, cartoon magnet or the caption text.",
  "identity_main": "The exact fictional AI character holistic.brandon: Black mixed-race American woman around thirty, athletic and toned, medium light-brown skin with light freckles across the nose and cheeks, dark brown eyes, defined eyebrows, full lips, hair in tight cornrows that turn into long loose braids falling over both shoulders, finished with small wooden and gold beads, a black floral blackwork tattoo sleeve on her right arm, a small line tattoo on her left upper arm and small fine-line tattoos on her chest near the collarbones. She reads as an ordinary anonymous American fitness coach, not resembling anyone famous.",
  "wardrobe": "Plain white ribbed tank top with nothing printed or written on it, loose black training shorts ending at mid-thigh, a thin gold chain with a small gold cross pendant and small stud earrings.",
  "scene": "Her own garage gym, the same room as the reference: a white-painted concrete block wall and a dark wooden slat ceiling, a red neon sign reading TRAIN PRAY REPEAT on the wall at the left, a whiteboard with handwritten black marker reading STAY READY. STAY DISCIPLINED. on the right, and a small American flag pinned above the whiteboard, discreet but clearly visible and in focus. The background is reduced by framing, never by blur.",
  "prop": "No prop in her hands. The ingredients are lined up on the table: two small clear glasses of water, two cinnamon sticks, a small pile of black peppercorns and one potato.",
  "posture": "Brandon stands upright behind the black table in front of her, seen from the thighs up, her hands open above the table. Both palms open upward.",
  "composition": "Straight-on wide shot from table height: the phone lens is about 60 centimeters from the ingredients and about 1 meter from her; the ingredients on the table fill the lower 30 percent of the frame, closer to the camera than her face, and she fills the upper two thirds from the thighs up. Nothing else is on the table. The background is reduced by framing, never by blur.",
  "camera": "phone propped at table height about 1 meter from her, standard 1x lens, level",
  "lighting": "Neutral overcast daylight from a large window out of frame, soft even light on her face and hands with no harsh shadows. The red neon glows on the wall but does not tint her skin.",
  "state": "Start frame: Brandon is caught mid-sentence, lips naturally parted, animated expression, looking straight into the lens, calm and confident.",
  "realism": "Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday reality, background fully in focus, everything in sharp focus, no AI polish, no beauty smoothing.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no studio, no plastic-looking skin, no extra fingers, no third hand, no blur, no bokeh, no warm orange color cast, no yellow tint, no golden glow, no golden hour light, no sunset, no HDR, no cinematic lighting, no de-aging, no beauty smoothing, no visible phone, no glasses, no gray t-shirt, no kitchen cabinets, no white marble counter, no cartoon magnet, no silver cross, no white coat, no second person"
}
```

## K08 · T8 · GERAR DO ZERO · ÂNCORA HOLISTIC BRANDON + FRAME DO MODELO

> ### 📎 ANEXAR: **2 IMAGENS**
> **1️⃣ ÂNCORA HOLISTIC BRANDON** `producao/_ancoras/holistic_brandon_ancora.jpg`
> **2️⃣ FRAME DO MODELO, só composição** `input/frames_modelo/K08_modelo.png`
>
> ### 🆕 GERAR DO ZERO

Cena: plano aberto, transição.

```json
{
  "shot_id": "K08_t8_brandon",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "reference_use": "Use the first attached image only for Brandon's exact identity, wardrobe and her own garage gym. Use the second attached image only as a composition reference for the camera position, framing and the action; do not copy its man, glasses, gray t-shirt, kitchen, marble counter, cartoon magnet or the caption text.",
  "identity_main": "The exact fictional AI character holistic.brandon: Black mixed-race American woman around thirty, athletic and toned, medium light-brown skin with light freckles across the nose and cheeks, dark brown eyes, defined eyebrows, full lips, hair in tight cornrows that turn into long loose braids falling over both shoulders, finished with small wooden and gold beads, a black floral blackwork tattoo sleeve on her right arm, a small line tattoo on her left upper arm and small fine-line tattoos on her chest near the collarbones. She reads as an ordinary anonymous American fitness coach, not resembling anyone famous.",
  "wardrobe": "Plain white ribbed tank top with nothing printed or written on it, loose black training shorts ending at mid-thigh, a thin gold chain with a small gold cross pendant and small stud earrings.",
  "scene": "Her own garage gym, the same room as the reference: a white-painted concrete block wall and a dark wooden slat ceiling, a red neon sign reading TRAIN PRAY REPEAT on the wall at the left, a whiteboard with handwritten black marker reading STAY READY. STAY DISCIPLINED. on the right, and a small American flag pinned above the whiteboard, discreet but clearly visible and in focus. The background is reduced by framing, never by blur.",
  "prop": "No prop in her hands. The ingredients are lined up on the table: two small clear glasses of water, two cinnamon sticks, a small pile of black peppercorns and one potato.",
  "posture": "Brandon stands upright behind the black table in front of her, seen from the thighs up, her hands open above the table. Her right hand is held open just above the ingredients.",
  "composition": "Straight-on wide shot from table height: the phone lens is about 60 centimeters from the ingredients and about 1 meter from her; the ingredients on the table fill the lower 30 percent of the frame, closer to the camera than her face, and she fills the upper two thirds from the thighs up. Nothing else is on the table. The background is reduced by framing, never by blur.",
  "camera": "phone propped at table height about 1 meter from her, standard 1x lens, level",
  "lighting": "Neutral overcast daylight from a large window out of frame, soft even light on her face and hands with no harsh shadows. The red neon glows on the wall but does not tint her skin.",
  "state": "Start frame: Brandon is caught mid-sentence, lips naturally parted, animated expression, looking straight into the lens, sincere and close.",
  "realism": "Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday reality, background fully in focus, everything in sharp focus, no AI polish, no beauty smoothing.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no studio, no plastic-looking skin, no extra fingers, no third hand, no blur, no bokeh, no warm orange color cast, no yellow tint, no golden glow, no golden hour light, no sunset, no HDR, no cinematic lighting, no de-aging, no beauty smoothing, no visible phone, no glasses, no gray t-shirt, no kitchen cabinets, no white marble counter, no cartoon magnet, no silver cross, no white coat, no second person"
}
```

## K09 · T9 · GERAR DO ZERO · ÂNCORA HOLISTIC BRANDON + FRAME DO MODELO + FOTO DO POTE

> ### 📎 ANEXAR: **3 IMAGENS**
> **1️⃣ ÂNCORA HOLISTIC BRANDON** `producao/_ancoras/holistic_brandon_ancora.jpg`
> **2️⃣ FRAME DO MODELO, só composição** `input/frames_modelo/K09_modelo.png`
> **3️⃣ FOTO DO POTE NATURAL REMS, só o pote da frente** `producao/_ancoras/natural_rems_seamoss_produto.jpg`
>
> ### 🆕 GERAR DO ZERO

Cena: pote sobe no nome.

```json
{
  "shot_id": "K09_t9_brandon",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "reference_use": "Use the first attached image only for Brandon's exact identity, wardrobe and her own garage gym. Use the second attached image only as a composition reference for the camera position, framing and the action; do not copy its man, glasses, gray t-shirt, kitchen, marble counter, cartoon magnet or the caption text. Use the third attached image only for the exact look of the front jar and its label; ignore the MADE IN USA banner, the second jar with the Supplement Facts panel and the loose gummies.",
  "identity_main": "The exact fictional AI character holistic.brandon: Black mixed-race American woman around thirty, athletic and toned, medium light-brown skin with light freckles across the nose and cheeks, dark brown eyes, defined eyebrows, full lips, hair in tight cornrows that turn into long loose braids falling over both shoulders, finished with small wooden and gold beads, a black floral blackwork tattoo sleeve on her right arm, a small line tattoo on her left upper arm and small fine-line tattoos on her chest near the collarbones. She reads as an ordinary anonymous American fitness coach, not resembling anyone famous.",
  "wardrobe": "Plain white ribbed tank top with nothing printed or written on it, loose black training shorts ending at mid-thigh, a thin gold chain with a small gold cross pendant and small stud earrings.",
  "scene": "Her own garage gym, the same room as the reference: a white-painted concrete block wall and a dark wooden slat ceiling, a red neon sign reading TRAIN PRAY REPEAT on the wall at the left, a whiteboard with handwritten black marker reading STAY READY. STAY DISCIPLINED. on the right, and a small American flag pinned above the whiteboard, discreet but clearly visible and in focus. The background is reduced by framing, never by blur.",
  "prop": "Raised with both hands in front of her chest, she holds the Natural Rems Sea Moss Gummies jar exactly as in the attached product photo: a short wide jar of dark amber plastic with a black screw cap, a pale sage-green label with dark green text, the Natural Rems logo with three leaves at the top, the big title Sea Moss Gummies, a pill-shaped badge reading 6000 MG | 16-IN-1, the line GREEN APPLE FLAVOR, two columns of dark green ingredient pills, green seaweed illustrations on the sides and a small 30 Gummies badge. The label is turned straight to the lens and fully readable, her fingers only on the sides of the jar.",
  "posture": "Brandon stands behind the black table in front of her, seen from the waist up, holding the jar toward the camera.",
  "composition": "Straight-on medium shot from table height: the phone lens is about 40 centimeters from the jar, which fills about 25 percent of the frame in the lower center, closer to the camera than her face; her face and shoulders fill the upper half. The table is empty. The background is reduced by framing, never by blur.",
  "camera": "phone propped at table height about 40 centimeters from the jar, standard 1x lens, level",
  "lighting": "Neutral overcast daylight from a large window out of frame, soft even light on her face and hands with no harsh shadows. The red neon glows on the wall but does not tint her skin.",
  "state": "Start frame: Brandon is smiling and caught mid-sentence, lips naturally parted, animated expression, looking straight into the lens.",
  "realism": "Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday reality, background fully in focus, everything in sharp focus, no AI polish, no beauty smoothing.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no studio, no plastic-looking skin, no extra fingers, no third hand, no blur, no bokeh, no warm orange color cast, no yellow tint, no golden glow, no golden hour light, no sunset, no HDR, no cinematic lighting, no de-aging, no beauty smoothing, no visible phone, no glasses, no gray t-shirt, no kitchen cabinets, no white marble counter, no cartoon magnet, no silver cross, no white coat, no second person, no second jar, no loose gummies, no banner on the jar, no fingers over the label"
}
```

## K10 · T10 · GERAR DO ZERO · ÂNCORA HOLISTIC BRANDON + FRAME DO MODELO + FOTO DO POTE

> ### 📎 ANEXAR: **3 IMAGENS**
> **1️⃣ ÂNCORA HOLISTIC BRANDON** `producao/_ancoras/holistic_brandon_ancora.jpg`
> **2️⃣ FRAME DO MODELO, só composição** `input/frames_modelo/K10_modelo.png`
> **3️⃣ FOTO DO POTE NATURAL REMS, só o pote da frente** `producao/_ancoras/natural_rems_seamoss_produto.jpg`
>
> ### 🆕 GERAR DO ZERO

Cena: CTA, pote parado e legível.

```json
{
  "shot_id": "K10_t10_brandon",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "reference_use": "Use the first attached image only for Brandon's exact identity, wardrobe and her own garage gym. Use the second attached image only as a composition reference for the camera position, framing and the action; do not copy its man, glasses, gray t-shirt, kitchen, marble counter, cartoon magnet or the caption text. Use the third attached image only for the exact look of the front jar and its label; ignore the MADE IN USA banner, the second jar with the Supplement Facts panel and the loose gummies.",
  "identity_main": "The exact fictional AI character holistic.brandon: Black mixed-race American woman around thirty, athletic and toned, medium light-brown skin with light freckles across the nose and cheeks, dark brown eyes, defined eyebrows, full lips, hair in tight cornrows that turn into long loose braids falling over both shoulders, finished with small wooden and gold beads, a black floral blackwork tattoo sleeve on her right arm, a small line tattoo on her left upper arm and small fine-line tattoos on her chest near the collarbones. She reads as an ordinary anonymous American fitness coach, not resembling anyone famous.",
  "wardrobe": "Plain white ribbed tank top with nothing printed or written on it, loose black training shorts ending at mid-thigh, a thin gold chain with a small gold cross pendant and small stud earrings.",
  "scene": "Her own garage gym, the same room as the reference: a white-painted concrete block wall and a dark wooden slat ceiling, a red neon sign reading TRAIN PRAY REPEAT on the wall at the left, a whiteboard with handwritten black marker reading STAY READY. STAY DISCIPLINED. on the right, and a small American flag pinned above the whiteboard, discreet but clearly visible and in focus. The background is reduced by framing, never by blur.",
  "prop": "Perfectly still with both hands in front of her chest, centered, she holds the Natural Rems Sea Moss Gummies jar exactly as in the attached product photo: a short wide jar of dark amber plastic with a black screw cap, a pale sage-green label with dark green text, the Natural Rems logo with three leaves at the top, the big title Sea Moss Gummies, a pill-shaped badge reading 6000 MG | 16-IN-1, the line GREEN APPLE FLAVOR, two columns of dark green ingredient pills, green seaweed illustrations on the sides and a small 30 Gummies badge. The label is turned straight to the lens, fully readable and with nothing covering it.",
  "posture": "Brandon stands behind the black table in front of her, seen from the chest up, holding the jar toward the camera.",
  "composition": "The tightest shot of the video, straight-on from chest height: the phone lens is about 35 centimeters from the jar, which fills about 30 percent of the frame in the lower center, closer to the camera than her face; her face fills the upper half. The background is reduced by framing, never by blur.",
  "camera": "phone propped at chest height, standard 1x lens, level",
  "lighting": "Neutral overcast daylight from a large window out of frame, soft even light on her face and hands with no harsh shadows. The red neon glows on the wall but does not tint her skin.",
  "state": "Start frame: Brandon is caught mid-sentence, lips naturally parted, animated expression, looking straight into the lens, clear and calm.",
  "realism": "Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday reality, background fully in focus, everything in sharp focus, no AI polish, no beauty smoothing.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no studio, no plastic-looking skin, no extra fingers, no third hand, no blur, no bokeh, no warm orange color cast, no yellow tint, no golden glow, no golden hour light, no sunset, no HDR, no cinematic lighting, no de-aging, no beauty smoothing, no visible phone, no glasses, no gray t-shirt, no kitchen cabinets, no white marble counter, no cartoon magnet, no silver cross, no white coat, no second person, no second jar, no loose gummies, no banner on the jar, no fingers over the label"
}
```

## Bloco global de vídeo

```text
a avatar Brandon, mulher, fala em inglês com sotaque americano de uma mulher negra americana, voz feminina clara e firme de uma mulher de uns trinta anos, [emoção da fala], voz autêntica, como se exigisse ser ouvida, a seguinte frase: "[FALA EXATA DO ROTEIRO]"

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: [ação enxuta]

câmera: [fixa / leve handheld]

som ambiente: box de treino em casa, tranquilo, sem música
```

# Prompts de vídeo

### V01 · T1 · usa K01

```text
a avatar Brandon, mulher, fala em inglês com sotaque americano de uma mulher negra americana, voz feminina clara e firme de uma mulher de uns trinta anos, entonação intrigante, como quem vai provar algo agora, voz autêntica, como se exigisse ser ouvida, a seguinte frase: "If you bought black pepper from the store, drop a spoonful into cold water. Real peppercorns sink."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Brandon vira as duas colheres de pimenta-do-reino dentro do aquário de água fria; os grãos caem e a maioria afunda devagar até o fundo.

câmera: leve handheld

som ambiente: box de treino em casa, tranquilo, grãos caindo na água, sem música
```

### V02 · T2 · usa K02

```text
a avatar Brandon, mulher, fala em inglês com sotaque americano de uma mulher negra americana, voz feminina clara e firme de uma mulher de uns trinta anos, entonação de denúncia, indignada na medida, voz autêntica, como se exigisse ser ouvida, a seguinte frase: "If some float, those are dried papaya seeds they mixed in to fill the jar."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Brandon aponta com o indicador para os grãos que ficaram boiando na superfície da água.

câmera: leve handheld

som ambiente: box de treino em casa, tranquilo, sem música
```

### V03 · T3 · usa K03

```text
a avatar Brandon, mulher, fala em inglês com sotaque americano de uma mulher negra americana, voz feminina clara e firme de uma mulher de uns trinta anos, entonação didática e rápida, voz autêntica, como se exigisse ser ouvida, a seguinte frase: "Potatoes, place them in a bowl of water. If they sink, they are good. If they float, they are hollow and already going bad."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Brandon solta as duas batatas na água do aquário; uma afunda até o fundo e a outra fica boiando.

câmera: leve handheld

som ambiente: box de treino em casa, tranquilo, batatas caindo na água, sem música
```

### V04 · T4 · usa K04

```text
a avatar Brandon, mulher, fala em inglês com sotaque americano de uma mulher negra americana, voz feminina clara e firme de uma mulher de uns trinta anos, entonação didática, marcando dyed, voz autêntica, como se exigisse ser ouvida, a seguinte frase: "Turmeric, stir a spoonful into warm water. Real turmeric slowly settles to the bottom. If the water turns bright yellow right away, it has been dyed."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Brandon mexe uma colher de cúrcuma em cada copo: no copo da esquerda o pó assenta devagar no fundo, no da direita a água fica amarela forte na hora.

câmera: leve handheld

som ambiente: box de treino em casa, tranquilo, colher batendo no vidro, sem música
```

### V05 · T5 · usa K05

```text
a avatar Brandon, mulher, fala em inglês com sotaque americano de uma mulher negra americana, voz feminina clara e firme de uma mulher de uns trinta anos, entonação didática e segura, voz autêntica, como se exigisse ser ouvida, a seguinte frase: "Coffee, sprinkle a little into a glass of cold water. If it floats on top, it is pure. If it sinks and releases color, it has been mixed."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Brandon vira as colheres de café nos dois copos: no da esquerda o pó fica por cima da água, no da direita ele afunda soltando fios marrons.

câmera: leve handheld

som ambiente: box de treino em casa, tranquilo, colher batendo no vidro, sem música
```

### V06 · T6 · usa K06

```text
a avatar Brandon, mulher, fala em inglês com sotaque americano de uma mulher negra americana, voz feminina clara e firme de uma mulher de uns trinta anos, entonação cúmplice, sorrindo em the cheap one, voz autêntica, como se exigisse ser ouvida, a seguinte frase: "Cinnamon sticks. A real cinnamon roll has thin paper layers like a cigar. If it is one thick hard curl, you bought cassia, the cheap one."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Brandon mostra as duas canelas bem perto da câmera e depois aproxima a da direita.

câmera: leve handheld

som ambiente: box de treino em casa, tranquilo, sem música
```

### V07 · T7 · usa K07

```text
a avatar Brandon, mulher, fala em inglês com sotaque americano de uma mulher negra americana, voz feminina clara e firme de uma mulher de uns trinta anos, entonação calma e confiante, voz autêntica, como se exigisse ser ouvida, a seguinte frase: "These are only some of the food secrets I have collected during years of my practice."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Brandon, atrás da mesa com os ingredientes, abre as mãos com as palmas para cima enquanto fala.

câmera: fixa

som ambiente: box de treino em casa, tranquilo, sem música
```

### V08 · T8 · usa K08

```text
a avatar Brandon, mulher, fala em inglês com sotaque americano de uma mulher negra americana, voz feminina clara e firme de uma mulher de uns trinta anos, entonação próxima e sincera, como quem conta um hábito, voz autêntica, como se exigisse ser ouvida, a seguinte frase: "My clients always ask how I test all of this. Honestly, I stopped buying turmeric, black pepper and sea moss in separate jars."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Brandon passa a mão aberta por cima dos ingredientes enfileirados na mesa no separate jars.

câmera: fixa

som ambiente: box de treino em casa, tranquilo, sem música
```

### V09 · T9 · usa K09

```text
a avatar Brandon, mulher, fala em inglês com sotaque americano de uma mulher negra americana, voz feminina clara e firme de uma mulher de uns trinta anos, entonação calorosa e confiante, voz autêntica, como se exigisse ser ouvida, a seguinte frase: "I get all of them, plus thirteen more, in Natural Rems Sea Moss. One green apple gummy each day, and sixteen fewer jars to test."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Brandon segura o pote de Natural Rems Sea Moss com as duas mãos na altura do peito, rótulo de frente para a câmera, e aproxima o pote um pouco da câmera quando diz o nome.

câmera: fixa

som ambiente: box de treino em casa, tranquilo, sem música
```

### V10 · T10 · usa K10

```text
a avatar Brandon, mulher, fala em inglês com sotaque americano de uma mulher negra americana, voz feminina clara e firme de uma mulher de uns trinta anos, entonação clara e pausada, dizendo Natural Rems Sea Moss devagar e por inteiro, voz autêntica, como se exigisse ser ouvida, a seguinte frase: "Search Natural Rems Sea Moss on Amazon. Or you can just tap the link I left right down below, in the caption of this video."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Brandon segura o pote parado com as duas mãos, rótulo de frente e legível, sem nada cobrindo, do começo ao fim; só o rosto e a boca se mexem.

câmera: fixa

som ambiente: box de treino em casa, tranquilo, sem música
```

## Mapa de âncoras

| Keyframe | Referências a anexar | Modelo |
|---|---|---|
| K01 | ÂNCORA HOLISTIC BRANDON + `input/frames_modelo/K01_modelo.png` (só composição) | Nano Banana 2, 9:16 |
| K02 | ÂNCORA HOLISTIC BRANDON + `input/frames_modelo/K02_modelo.png` (só composição) | Nano Banana 2, 9:16 |
| K03 | ÂNCORA HOLISTIC BRANDON + `input/frames_modelo/K03_modelo.png` (só composição) | Nano Banana 2, 9:16 |
| K04 | ÂNCORA HOLISTIC BRANDON + `input/frames_modelo/K04_modelo.png` (só composição) | Nano Banana 2, 9:16 |
| K05 | ÂNCORA HOLISTIC BRANDON + `input/frames_modelo/K05_modelo.png` (só composição) | Nano Banana 2, 9:16 |
| K06 | ÂNCORA HOLISTIC BRANDON + `input/frames_modelo/K06_modelo.png` (só composição) | Nano Banana 2, 9:16 |
| K07 | ÂNCORA HOLISTIC BRANDON + `input/frames_modelo/K07_modelo.png` (só composição) | Nano Banana 2, 9:16 |
| K08 | ÂNCORA HOLISTIC BRANDON + `input/frames_modelo/K08_modelo.png` (só composição) | Nano Banana 2, 9:16 |
| K09 | ÂNCORA HOLISTIC BRANDON + `input/frames_modelo/K09_modelo.png` (só composição) + `producao/_ancoras/natural_rems_seamoss_produto.jpg` (só o pote da frente) | Nano Banana 2, 9:16 |
| K10 | ÂNCORA HOLISTIC BRANDON + `input/frames_modelo/K10_modelo.png` (só composição) + `producao/_ancoras/natural_rems_seamoss_produto.jpg` (só o pote da frente) | Nano Banana 2, 9:16 |

## Montagem no CapCut

1. Clipes numerados na ordem: V01 a V10.
2. Cortar cada clipe no tempo da cena do modelo: V01 0,0 a 5,7 s; V02 5,7 a 9,6 s; V03 9,6 a 17,1 s; V04 17,1 a 25,0 s; V05 25,0 a 32,7 s; V06 32,7 a 40,2 s; V07 a fala inteira; V08 a fala inteira; V09 a fala inteira; V10 o CTA inteiro, sem corte.
3. Zero tempo morto: todo clipe começa já falando. Isolate Voice / Keep Vocal no áudio.
4. Dentro de cada teste (V01 a V06), jump cuts curtos de ritmo como no modelo, se quiser; o clipe é contínuo.
5. V10 inteiro, sem corte e sem nada cobrindo o pote: é o CTA da marca (frasco parado e legível enquanto o nome é dito). O vídeo acaba nele.
6. Legenda de tela como no modelo: serifada branca, palavra a palavra, no meio do quadro, com a palavra carregada maior; no começo do V01, "Real peppercorns sink".
7. Sem Voice Changer: a voz vem do prompt de cada V.
8. Música só depois do gancho (a partir do V03), nunca no pré-gancho, entre -19 e -20 dB, fora da biblioteca do TikTok.
9. Rótulo pequeno `Synthetic performer` num canto do vídeo.
10. Legenda do post: `#ad #syntheticperformer #naturalrems` na primeira linha e o link da Amazon logo abaixo; chave de conteúdo de IA ligada na plataforma.

## Gates de qualidade

1. Fala de cada V igual ao ROTEIRO, palavra por palavra.
2. Um take por cena do modelo; nenhum take acima de 29 palavras.
3. Bandeira dos EUA no campo scene de todo K.
4. Zero travessão.
5. CTA da marca no T10: Search Natural Rems Sea Moss on Amazon, depois o link da legenda, e fim.
6. Pote em quadro no T9 e no T10, rótulo legível; no T10 parado do começo ao fim.
7. Nada médico em quadro nem na fala; sem antes e depois; sem cura nem tratamento.
8. Negative sem termo sensível.
9. GATE_VISUAL Partes 1 a 3 em todo K: herói colado na lente, luz neutra, sem tom quente, sem blur, trecho de realismo.
10. Gancho fiel no conteúdo: as colheres de pimenta virando no aquário colado na lente, falado desde o segundo 0.
11. Um K = um V; a queda dos grãos, a batata que boia, a água amarela e o café que afunda nascem no vídeo.

