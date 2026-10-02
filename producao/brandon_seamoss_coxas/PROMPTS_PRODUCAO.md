# holistic.brandon | Ângulo 1 Natural Rems Sea Moss | Coxa escura | Pacote de Prompts

Vídeo modelo: `input/reference_video.mp4` (36,7 s, avatar IA, original em espanhol)

Âncora: `producao/_ancoras/holistic_brandon_ancora.jpg` · Foto do produto: `producao/_ancoras/natural_rems_seamoss_produto.jpg`

Funil: venda Amazon. Frasco em quadro, "Search Natural Rems Sea Moss on Amazon" primeiro, link da legenda do post depois, fim. Rodada de validação, gancho fiel ao modelo sem o antes e depois.

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
| T9 | K09 | ÂNCORA HOLISTIC BRANDON + FRAME DO MODELO (K09) | GERAR DO ZERO |
| T10 | K10 | ÂNCORA HOLISTIC BRANDON + FRAME DO MODELO + FOTO DO POTE (K10) | GERAR DO ZERO |
| T11 | K11 | ÂNCORA HOLISTIC BRANDON + FRAME DO MODELO + FOTO DO POTE (K11) | GERAR DO ZERO |

Todo K é GERAR DO ZERO: o bloco do Flow é autossuficiente e cada K descreve o cenário inteiro, então não existe `EDITAR do K__` aqui. O frame do modelo de cada K entra só como composição.

## Trava de identidade e continuidade

- Identidade: The exact fictional AI character holistic.brandon: Black mixed-race American woman around thirty, athletic and toned, medium light-brown skin with light freckles across the nose and cheeks, dark brown eyes, defined eyebrows, full lips, hair in tight cornrows that turn into long loose braids falling over both shoulders, finished with small wooden and gold beads, a black floral blackwork tattoo sleeve on her right arm, a small line tattoo on her left upper arm and small fine-line tattoos on her chest near the collarbones. She reads as an ordinary anonymous American fitness coach, not resembling anyone famous.
- Roupa (fixa da conta): Plain white ribbed tank top with nothing printed or written on it, loose black training shorts ending at mid-thigh, a thin gold chain with a small gold cross pendant and small stud earrings.
- Cenário-base (fixo da conta): Her own garage gym, the same room as the reference: a white-painted concrete block wall and a dark wooden slat ceiling, a red neon sign reading TRAIN PRAY REPEAT on the wall at the left, a whiteboard with handwritten black marker reading STAY READY. STAY DISCIPLINED. on the right, and a small American flag pinned above the whiteboard, discreet but clearly visible and in focus. The background is reduced by framing, never by blur.
- Luz: Neutral overcast daylight from a large window out of frame, soft even light on her face, hands and skin with no harsh shadows. The red neon glows on the wall but does not tint anyone's skin.
- Voz (mesmo timbre em todos os V): voz feminina clara e firme de uma mulher de uns trinta anos, sotaque americano de uma mulher negra americana.
- A cliente só aparece nos K01 e K02, deitada, cortada pela borda direita. Nunca fala.

## Trava do prop herói

- Gancho: a mancha escura, áspera e aveludada na parte interna da coxa da cliente, do tamanho de uma mão aberta, logo abaixo da barra do short. **Igual no K01 e no K02**: a coxa nunca clareia em quadro.
- Receita: a clear glass mixing bowl, bicarbonato, meio limão, conta-gotas âmbar de óleo de coco, colher de medida, colher.
- Produto (T10 e T11): the Natural Rems Sea Moss Gummies jar exactly as in the attached product photo: a short wide jar of dark amber plastic with a black screw cap, a pale sage-green label with dark green text, the Natural Rems logo with three leaves at the top, the big title Sea Moss Gummies, a pill-shaped badge reading 6000 MG | 16-IN-1, the line GREEN APPLE FLAVOR, two columns of dark green ingredient pills, green seaweed illustrations on the sides and a small 30 Gummies badge. Referência: `producao/_ancoras/natural_rems_seamoss_produto.jpg`, só o pote da frente, sem a faixa MADE IN USA, sem o pote de trás e sem as gomas soltas.
- Nada da receita tem marca legível.

## Trava da 2ª pessoa (REF-A)

- Não precisa de REF: a cliente é descrita por escrito nos K01 e K02 (The client, a fictional American woman around fifty with shoulder-length gray-brown hair, wearing a plain light gray crew-neck t-shirt and loose black athletic shorts that fully cover her hips, lies on her back on a black padded flat gym bench, her head and shoulders at the right edge of the frame, partly cut off by it.) Fica em silêncio.

## Prompts de imagem

## K01 · T1 · GERAR DO ZERO · ÂNCORA HOLISTIC BRANDON + FRAME DO MODELO

> ### 📎 ANEXAR: **2 IMAGENS**
> **1️⃣ ÂNCORA HOLISTIC BRANDON** `producao/_ancoras/holistic_brandon_ancora.jpg`
> **2️⃣ FRAME DO MODELO, só composição** `input/frames_modelo/K01_modelo.png`
>
> ### 🆕 GERAR DO ZERO

Cena: gancho, a coxa escura da cliente colada na lente.

```json
{
  "shot_id": "K01_t1_brandon",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "reference_use": "Use the first attached image only for Brandon's exact identity, wardrobe and her own garage gym. Use the second attached image only as a composition reference for the camera position, framing and the action; do not copy its older man and woman, aprons, kitchen, marble counter, exam room, framed certificates or the caption text.",
  "identity_main": "The exact fictional AI character holistic.brandon: Black mixed-race American woman around thirty, athletic and toned, medium light-brown skin with light freckles across the nose and cheeks, dark brown eyes, defined eyebrows, full lips, hair in tight cornrows that turn into long loose braids falling over both shoulders, finished with small wooden and gold beads, a black floral blackwork tattoo sleeve on her right arm, a small line tattoo on her left upper arm and small fine-line tattoos on her chest near the collarbones. She reads as an ordinary anonymous American fitness coach, not resembling anyone famous.",
  "wardrobe": "Plain white ribbed tank top with nothing printed or written on it, loose black training shorts ending at mid-thigh, a thin gold chain with a small gold cross pendant and small stud earrings.",
  "scene": "Her own garage gym, the same room as the reference: a white-painted concrete block wall and a dark wooden slat ceiling, a red neon sign reading TRAIN PRAY REPEAT on the wall at the left, a whiteboard with handwritten black marker reading STAY READY. STAY DISCIPLINED. on the right, and a small American flag pinned above the whiteboard, discreet but clearly visible and in focus. The background is reduced by framing, never by blur.",
  "prop": "The client, a fictional American woman around fifty with shoulder-length gray-brown hair, wearing a plain light gray crew-neck t-shirt and loose black athletic shorts that fully cover her hips, lies on her back on a black padded flat gym bench, her head and shoulders at the right edge of the frame, partly cut off by it. Her left leg is bent at the knee with the inner side of the thigh turned toward the camera: the bare inner thigh fills the lower 45 percent of the frame from the lower left to the center, very close to the lens, larger than both faces and closer to the camera than them, nothing else competing with it. On the upper inner thigh, just below the hem of her shorts, a large patch of dark brown, rough, velvety skin about the size of an open hand, clearly darker than the rest of her leg, with a few darker spots around its edge. Brandon's right hand rests flat on the thigh just above the dark patch, her index finger pointing at it.",
  "posture": "Brandon kneels on the black rubber floor at the left side of the bench, leaning in over the thigh, her face in the upper left of the frame.",
  "composition": "Low close shot at bench height: the phone lens is about 25 centimeters from the inner thigh, which fills the lower 45 percent of the frame; Brandon's face is in the upper left and the client's head at the right edge. The background is reduced by framing, never by blur.",
  "camera": "phone held low at bench height about 25 centimeters from the thigh, wide 0.5x lens, level",
  "lighting": "Neutral overcast daylight from a large window out of frame, soft even light on her face, hands and skin with no harsh shadows. The red neon glows on the wall but does not tint anyone's skin.",
  "state": "Start frame: the client lies calm with her eyes half closed. Brandon is caught mid-sentence, lips naturally parted, animated expression, looking straight into the lens.",
  "realism": "Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday reality, background fully in focus, everything in sharp focus, no AI polish, no beauty smoothing.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no studio, no plastic-looking skin, no extra fingers, no third hand, no blur, no bokeh, no warm orange color cast, no yellow tint, no golden glow, no golden hour light, no sunset, no HDR, no cinematic lighting, no de-aging, no beauty smoothing, no visible phone, no apron, no older man, no kitchen cabinets, no white marble counter, no framed certificates, no silver cross, no white coat, no gown, no paper sheet on the bench, no underwear showing, no lightened patch, no even skin on the inner thigh"
}
```

## K02 · T2 · GERAR DO ZERO · ÂNCORA HOLISTIC BRANDON + FRAME DO MODELO

> ### 📎 ANEXAR: **2 IMAGENS**
> **1️⃣ ÂNCORA HOLISTIC BRANDON** `producao/_ancoras/holistic_brandon_ancora.jpg`
> **2️⃣ FRAME DO MODELO, só composição** `input/frames_modelo/K02_modelo.png`
>
> ### 🆕 GERAR DO ZERO

Cena: virada, mão aberta, a coxa igual.

```json
{
  "shot_id": "K02_t2_brandon",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "reference_use": "Use the first attached image only for Brandon's exact identity, wardrobe and her own garage gym. Use the second attached image only as a composition reference for the camera position, framing and the action; do not copy its older man and woman, aprons, kitchen, marble counter, exam room, framed certificates or the caption text.",
  "identity_main": "The exact fictional AI character holistic.brandon: Black mixed-race American woman around thirty, athletic and toned, medium light-brown skin with light freckles across the nose and cheeks, dark brown eyes, defined eyebrows, full lips, hair in tight cornrows that turn into long loose braids falling over both shoulders, finished with small wooden and gold beads, a black floral blackwork tattoo sleeve on her right arm, a small line tattoo on her left upper arm and small fine-line tattoos on her chest near the collarbones. She reads as an ordinary anonymous American fitness coach, not resembling anyone famous.",
  "wardrobe": "Plain white ribbed tank top with nothing printed or written on it, loose black training shorts ending at mid-thigh, a thin gold chain with a small gold cross pendant and small stud earrings.",
  "scene": "Her own garage gym, the same room as the reference: a white-painted concrete block wall and a dark wooden slat ceiling, a red neon sign reading TRAIN PRAY REPEAT on the wall at the left, a whiteboard with handwritten black marker reading STAY READY. STAY DISCIPLINED. on the right, and a small American flag pinned above the whiteboard, discreet but clearly visible and in focus. The background is reduced by framing, never by blur.",
  "prop": "The client, a fictional American woman around fifty with shoulder-length gray-brown hair, wearing a plain light gray crew-neck t-shirt and loose black athletic shorts that fully cover her hips, lies on her back on a black padded flat gym bench, her head and shoulders at the right edge of the frame, partly cut off by it. Her left leg is bent at the knee with the inner side of the thigh turned toward the camera: the bare inner thigh fills the lower 45 percent of the frame from the lower left to the center, very close to the lens, larger than both faces and closer to the camera than them, nothing else competing with it. On the upper inner thigh, just below the hem of her shorts, a large patch of dark brown, rough, velvety skin about the size of an open hand, clearly darker than the rest of her leg, with a few darker spots around its edge. Brandon's left hand is held open, palm up, toward the lens just above the thigh.",
  "posture": "Brandon kneels on the black rubber floor at the left side of the bench, leaning in over the thigh, her face in the upper left of the frame.",
  "composition": "Low close shot at bench height: the phone lens is about 25 centimeters from the inner thigh, which fills the lower 45 percent of the frame; Brandon's face is in the upper left and the client's head at the right edge. The background is reduced by framing, never by blur.",
  "camera": "phone held low at bench height about 25 centimeters from the thigh, wide 0.5x lens, level",
  "lighting": "Neutral overcast daylight from a large window out of frame, soft even light on her face, hands and skin with no harsh shadows. The red neon glows on the wall but does not tint anyone's skin.",
  "state": "Start frame: the dark patch is exactly as before; the client looks at the lens with a faint smile. Brandon is caught mid-sentence, lips naturally parted, animated expression, looking straight into the lens.",
  "realism": "Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday reality, background fully in focus, everything in sharp focus, no AI polish, no beauty smoothing.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no studio, no plastic-looking skin, no extra fingers, no third hand, no blur, no bokeh, no warm orange color cast, no yellow tint, no golden glow, no golden hour light, no sunset, no HDR, no cinematic lighting, no de-aging, no beauty smoothing, no visible phone, no apron, no older man, no kitchen cabinets, no white marble counter, no framed certificates, no silver cross, no white coat, no gown, no paper sheet on the bench, no underwear showing, no lightened patch, no even skin on the inner thigh"
}
```

## K03 · T3 · GERAR DO ZERO · ÂNCORA HOLISTIC BRANDON + FRAME DO MODELO

> ### 📎 ANEXAR: **2 IMAGENS**
> **1️⃣ ÂNCORA HOLISTIC BRANDON** `producao/_ancoras/holistic_brandon_ancora.jpg`
> **2️⃣ FRAME DO MODELO, só composição** `input/frames_modelo/K03_modelo.png`
>
> ### 🆕 GERAR DO ZERO

Cena: receita, limão na tigela.

```json
{
  "shot_id": "K03_t3_brandon",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "reference_use": "Use the first attached image only for Brandon's exact identity, wardrobe and her own garage gym. Use the second attached image only as a composition reference for the camera position, framing and the action; do not copy its older man and woman, aprons, kitchen, marble counter, exam room, framed certificates or the caption text.",
  "identity_main": "The exact fictional AI character holistic.brandon: Black mixed-race American woman around thirty, athletic and toned, medium light-brown skin with light freckles across the nose and cheeks, dark brown eyes, defined eyebrows, full lips, hair in tight cornrows that turn into long loose braids falling over both shoulders, finished with small wooden and gold beads, a black floral blackwork tattoo sleeve on her right arm, a small line tattoo on her left upper arm and small fine-line tattoos on her chest near the collarbones. She reads as an ordinary anonymous American fitness coach, not resembling anyone famous.",
  "wardrobe": "Plain white ribbed tank top with nothing printed or written on it, loose black training shorts ending at mid-thigh, a thin gold chain with a small gold cross pendant and small stud earrings.",
  "scene": "Her own garage gym, the same room as the reference: a white-painted concrete block wall and a dark wooden slat ceiling, a red neon sign reading TRAIN PRAY REPEAT on the wall at the left, a whiteboard with handwritten black marker reading STAY READY. STAY DISCIPLINED. on the right, and a small American flag pinned above the whiteboard, discreet but clearly visible and in focus. The background is reduced by framing, never by blur.",
  "prop": "A clear glass mixing bowl with a heap of white baking soda powder in the center of the black table in front of her, very close to the lens, a metal measuring spoon lying at its left. Her right hand squeezes half a fresh lemon above the bowl; her left hand holds the rim of the bowl.",
  "posture": "Brandon stands behind the black table in front of her, leaning forward over it, seen from the waist up.",
  "composition": "Close shot from just above the table: the phone lens is about 40 centimeters from the bowl, which fills about 25 percent of the frame in the lower center, closer to the camera than her face; her head and torso fill the upper part. Nothing else is on the table. The background is reduced by framing, never by blur.",
  "camera": "phone held just above the table edge at chest height about 40 centimeters from the bowl, standard 1x lens tilted slightly down",
  "lighting": "Neutral overcast daylight from a large window out of frame, soft even light on her face, hands and skin with no harsh shadows. The red neon glows on the wall but does not tint anyone's skin.",
  "state": "Start frame: the first drops of lemon juice are falling into the powder. Brandon is caught mid-sentence, lips naturally parted, animated expression, looking straight into the lens.",
  "realism": "Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday reality, background fully in focus, everything in sharp focus, no AI polish, no beauty smoothing.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no studio, no plastic-looking skin, no extra fingers, no third hand, no blur, no bokeh, no warm orange color cast, no yellow tint, no golden glow, no golden hour light, no sunset, no HDR, no cinematic lighting, no de-aging, no beauty smoothing, no visible phone, no apron, no older man, no kitchen cabinets, no white marble counter, no framed certificates, no silver cross, no white coat, no second person, no readable lettering on the bowl, spoon or dropper bottle"
}
```

## K04 · T4 · GERAR DO ZERO · ÂNCORA HOLISTIC BRANDON + FRAME DO MODELO

> ### 📎 ANEXAR: **2 IMAGENS**
> **1️⃣ ÂNCORA HOLISTIC BRANDON** `producao/_ancoras/holistic_brandon_ancora.jpg`
> **2️⃣ FRAME DO MODELO, só composição** `input/frames_modelo/K04_modelo.png`
>
> ### 🆕 GERAR DO ZERO

Cena: receita, óleo de coco no conta-gotas.

```json
{
  "shot_id": "K04_t4_brandon",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "reference_use": "Use the first attached image only for Brandon's exact identity, wardrobe and her own garage gym. Use the second attached image only as a composition reference for the camera position, framing and the action; do not copy its older man and woman, aprons, kitchen, marble counter, exam room, framed certificates or the caption text.",
  "identity_main": "The exact fictional AI character holistic.brandon: Black mixed-race American woman around thirty, athletic and toned, medium light-brown skin with light freckles across the nose and cheeks, dark brown eyes, defined eyebrows, full lips, hair in tight cornrows that turn into long loose braids falling over both shoulders, finished with small wooden and gold beads, a black floral blackwork tattoo sleeve on her right arm, a small line tattoo on her left upper arm and small fine-line tattoos on her chest near the collarbones. She reads as an ordinary anonymous American fitness coach, not resembling anyone famous.",
  "wardrobe": "Plain white ribbed tank top with nothing printed or written on it, loose black training shorts ending at mid-thigh, a thin gold chain with a small gold cross pendant and small stud earrings.",
  "scene": "Her own garage gym, the same room as the reference: a white-painted concrete block wall and a dark wooden slat ceiling, a red neon sign reading TRAIN PRAY REPEAT on the wall at the left, a whiteboard with handwritten black marker reading STAY READY. STAY DISCIPLINED. on the right, and a small American flag pinned above the whiteboard, discreet but clearly visible and in focus. The background is reduced by framing, never by blur.",
  "prop": "A clear glass mixing bowl with milky white liquid in the center of the black table in front of her, very close to the lens, a squeezed lemon half and a metal measuring spoon beside it. Her right hand holds the glass dropper of a small amber dropper bottle of coconut oil above the bowl.",
  "posture": "Brandon stands behind the black table in front of her, leaning forward over it, seen from the waist up.",
  "composition": "Close shot from just above the table: the phone lens is about 40 centimeters from the bowl, which fills about 25 percent of the frame in the lower center, closer to the camera than her face; her head and torso fill the upper part. Nothing else is on the table. The background is reduced by framing, never by blur.",
  "camera": "phone held just above the table edge at chest height about 40 centimeters from the bowl, standard 1x lens tilted slightly down",
  "lighting": "Neutral overcast daylight from a large window out of frame, soft even light on her face, hands and skin with no harsh shadows. The red neon glows on the wall but does not tint anyone's skin.",
  "state": "Start frame: a drop of oil hangs from the tip of the dropper. Brandon is caught mid-sentence, lips naturally parted, animated expression, looking straight into the lens.",
  "realism": "Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday reality, background fully in focus, everything in sharp focus, no AI polish, no beauty smoothing.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no studio, no plastic-looking skin, no extra fingers, no third hand, no blur, no bokeh, no warm orange color cast, no yellow tint, no golden glow, no golden hour light, no sunset, no HDR, no cinematic lighting, no de-aging, no beauty smoothing, no visible phone, no apron, no older man, no kitchen cabinets, no white marble counter, no framed certificates, no silver cross, no white coat, no second person, no readable lettering on the bowl, spoon or dropper bottle"
}
```

## K05 · T5 · GERAR DO ZERO · ÂNCORA HOLISTIC BRANDON + FRAME DO MODELO

> ### 📎 ANEXAR: **2 IMAGENS**
> **1️⃣ ÂNCORA HOLISTIC BRANDON** `producao/_ancoras/holistic_brandon_ancora.jpg`
> **2️⃣ FRAME DO MODELO, só composição** `input/frames_modelo/K05_modelo.png`
>
> ### 🆕 GERAR DO ZERO

Cena: protocolo, mexendo a pasta.

```json
{
  "shot_id": "K05_t5_brandon",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "reference_use": "Use the first attached image only for Brandon's exact identity, wardrobe and her own garage gym. Use the second attached image only as a composition reference for the camera position, framing and the action; do not copy its older man and woman, aprons, kitchen, marble counter, exam room, framed certificates or the caption text.",
  "identity_main": "The exact fictional AI character holistic.brandon: Black mixed-race American woman around thirty, athletic and toned, medium light-brown skin with light freckles across the nose and cheeks, dark brown eyes, defined eyebrows, full lips, hair in tight cornrows that turn into long loose braids falling over both shoulders, finished with small wooden and gold beads, a black floral blackwork tattoo sleeve on her right arm, a small line tattoo on her left upper arm and small fine-line tattoos on her chest near the collarbones. She reads as an ordinary anonymous American fitness coach, not resembling anyone famous.",
  "wardrobe": "Plain white ribbed tank top with nothing printed or written on it, loose black training shorts ending at mid-thigh, a thin gold chain with a small gold cross pendant and small stud earrings.",
  "scene": "Her own garage gym, the same room as the reference: a white-painted concrete block wall and a dark wooden slat ceiling, a red neon sign reading TRAIN PRAY REPEAT on the wall at the left, a whiteboard with handwritten black marker reading STAY READY. STAY DISCIPLINED. on the right, and a small American flag pinned above the whiteboard, discreet but clearly visible and in focus. The background is reduced by framing, never by blur.",
  "prop": "A clear glass mixing bowl full of thick white paste in the center of the black table in front of her, very close to the lens, two squeezed lemon halves at its left. Her right hand stirs the paste with a metal spoon; her left hand holds the rim of the bowl.",
  "posture": "Brandon stands behind the black table in front of her, leaning forward over it, seen from the waist up.",
  "composition": "Close shot from just above the table: the phone lens is about 40 centimeters from the bowl, which fills about 25 percent of the frame in the lower center, closer to the camera than her face; her head and torso fill the upper part. Nothing else is on the table. The background is reduced by framing, never by blur.",
  "camera": "phone held just above the table edge at chest height about 40 centimeters from the bowl, standard 1x lens tilted slightly down",
  "lighting": "Neutral overcast daylight from a large window out of frame, soft even light on her face, hands and skin with no harsh shadows. The red neon glows on the wall but does not tint anyone's skin.",
  "state": "Start frame: the spoon is mid-stir in the paste. Brandon is caught mid-sentence, lips naturally parted, animated expression, looking straight into the lens.",
  "realism": "Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday reality, background fully in focus, everything in sharp focus, no AI polish, no beauty smoothing.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no studio, no plastic-looking skin, no extra fingers, no third hand, no blur, no bokeh, no warm orange color cast, no yellow tint, no golden glow, no golden hour light, no sunset, no HDR, no cinematic lighting, no de-aging, no beauty smoothing, no visible phone, no apron, no older man, no kitchen cabinets, no white marble counter, no framed certificates, no silver cross, no white coat, no second person, no readable lettering on the bowl, spoon or dropper bottle"
}
```

## K06 · T6 · GERAR DO ZERO · ÂNCORA HOLISTIC BRANDON + FRAME DO MODELO

> ### 📎 ANEXAR: **2 IMAGENS**
> **1️⃣ ÂNCORA HOLISTIC BRANDON** `producao/_ancoras/holistic_brandon_ancora.jpg`
> **2️⃣ FRAME DO MODELO, só composição** `input/frames_modelo/K06_modelo.png`
>
> ### 🆕 GERAR DO ZERO

Cena: resultado, a tigela erguida.

```json
{
  "shot_id": "K06_t6_brandon",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "reference_use": "Use the first attached image only for Brandon's exact identity, wardrobe and her own garage gym. Use the second attached image only as a composition reference for the camera position, framing and the action; do not copy its older man and woman, aprons, kitchen, marble counter, exam room, framed certificates or the caption text.",
  "identity_main": "The exact fictional AI character holistic.brandon: Black mixed-race American woman around thirty, athletic and toned, medium light-brown skin with light freckles across the nose and cheeks, dark brown eyes, defined eyebrows, full lips, hair in tight cornrows that turn into long loose braids falling over both shoulders, finished with small wooden and gold beads, a black floral blackwork tattoo sleeve on her right arm, a small line tattoo on her left upper arm and small fine-line tattoos on her chest near the collarbones. She reads as an ordinary anonymous American fitness coach, not resembling anyone famous.",
  "wardrobe": "Plain white ribbed tank top with nothing printed or written on it, loose black training shorts ending at mid-thigh, a thin gold chain with a small gold cross pendant and small stud earrings.",
  "scene": "Her own garage gym, the same room as the reference: a white-painted concrete block wall and a dark wooden slat ceiling, a red neon sign reading TRAIN PRAY REPEAT on the wall at the left, a whiteboard with handwritten black marker reading STAY READY. STAY DISCIPLINED. on the right, and a small American flag pinned above the whiteboard, discreet but clearly visible and in focus. The background is reduced by framing, never by blur.",
  "prop": "With both hands she holds a clear glass mixing bowl full of thick white paste with a metal spoon in it, raised and tilted toward the lens; on the table below, a lemon half, a metal measuring spoon and a small amber dropper bottle.",
  "posture": "Brandon stands behind the black table in front of her, seen from the waist up, holding the bowl toward the camera.",
  "composition": "Close shot from chest height: the phone lens is about 30 centimeters from the bowl, which fills about 30 percent of the frame in the lower center, closer to the camera than her face; her face fills the upper part. The background is reduced by framing, never by blur.",
  "camera": "phone held at chest height about 30 centimeters from the bowl, standard 1x lens, level",
  "lighting": "Neutral overcast daylight from a large window out of frame, soft even light on her face, hands and skin with no harsh shadows. The red neon glows on the wall but does not tint anyone's skin.",
  "state": "Start frame: the paste is clearly visible inside the tilted bowl. Brandon is caught mid-sentence, lips naturally parted, animated expression, looking straight into the lens, relieved.",
  "realism": "Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday reality, background fully in focus, everything in sharp focus, no AI polish, no beauty smoothing.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no studio, no plastic-looking skin, no extra fingers, no third hand, no blur, no bokeh, no warm orange color cast, no yellow tint, no golden glow, no golden hour light, no sunset, no HDR, no cinematic lighting, no de-aging, no beauty smoothing, no visible phone, no apron, no older man, no kitchen cabinets, no white marble counter, no framed certificates, no silver cross, no white coat, no second person, no readable lettering on the bowl, spoon or dropper bottle"
}
```

## K07 · T7 · GERAR DO ZERO · ÂNCORA HOLISTIC BRANDON + FRAME DO MODELO

> ### 📎 ANEXAR: **2 IMAGENS**
> **1️⃣ ÂNCORA HOLISTIC BRANDON** `producao/_ancoras/holistic_brandon_ancora.jpg`
> **2️⃣ FRAME DO MODELO, só composição** `input/frames_modelo/K07_modelo.png`
>
> ### 🆕 GERAR DO ZERO

Cena: ponte, a superfície.

```json
{
  "shot_id": "K07_t7_brandon",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "reference_use": "Use the first attached image only for Brandon's exact identity, wardrobe and her own garage gym. Use the second attached image only as a composition reference for the camera position, framing and the action; do not copy its older man and woman, aprons, kitchen, marble counter, exam room, framed certificates or the caption text.",
  "identity_main": "The exact fictional AI character holistic.brandon: Black mixed-race American woman around thirty, athletic and toned, medium light-brown skin with light freckles across the nose and cheeks, dark brown eyes, defined eyebrows, full lips, hair in tight cornrows that turn into long loose braids falling over both shoulders, finished with small wooden and gold beads, a black floral blackwork tattoo sleeve on her right arm, a small line tattoo on her left upper arm and small fine-line tattoos on her chest near the collarbones. She reads as an ordinary anonymous American fitness coach, not resembling anyone famous.",
  "wardrobe": "Plain white ribbed tank top with nothing printed or written on it, loose black training shorts ending at mid-thigh, a thin gold chain with a small gold cross pendant and small stud earrings.",
  "scene": "Her own garage gym, the same room as the reference: a white-painted concrete block wall and a dark wooden slat ceiling, a red neon sign reading TRAIN PRAY REPEAT on the wall at the left, a whiteboard with handwritten black marker reading STAY READY. STAY DISCIPLINED. on the right, and a small American flag pinned above the whiteboard, discreet but clearly visible and in focus. The background is reduced by framing, never by blur.",
  "prop": "A clear glass mixing bowl full of thick white paste with a metal spoon resting in it, standing still on the black table in front of her; her right index finger points at the paste.",
  "posture": "Brandon stands behind the black table in front of her, seen from the waist up, both forearms near the table edge.",
  "composition": "Straight-on medium shot from table height: the phone lens is about 45 centimeters from the bowl, which sits in the lower left and fills about 20 percent of the frame, closer to the camera than her face; her face and shoulders fill the upper half. Nothing else is on the table. The background is reduced by framing, never by blur.",
  "camera": "phone propped at table height about 45 centimeters from the bowl, standard 1x lens tilted slightly up",
  "lighting": "Neutral overcast daylight from a large window out of frame, soft even light on her face, hands and skin with no harsh shadows. The red neon glows on the wall but does not tint anyone's skin.",
  "state": "Start frame: Brandon is caught mid-sentence, lips naturally parted, animated expression, looking straight into the lens, serious.",
  "realism": "Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday reality, background fully in focus, everything in sharp focus, no AI polish, no beauty smoothing.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no studio, no plastic-looking skin, no extra fingers, no third hand, no blur, no bokeh, no warm orange color cast, no yellow tint, no golden glow, no golden hour light, no sunset, no HDR, no cinematic lighting, no de-aging, no beauty smoothing, no visible phone, no apron, no older man, no kitchen cabinets, no white marble counter, no framed certificates, no silver cross, no white coat, no second person, no readable lettering on the bowl, spoon or dropper bottle"
}
```

## K08 · T8 · GERAR DO ZERO · ÂNCORA HOLISTIC BRANDON + FRAME DO MODELO

> ### 📎 ANEXAR: **2 IMAGENS**
> **1️⃣ ÂNCORA HOLISTIC BRANDON** `producao/_ancoras/holistic_brandon_ancora.jpg`
> **2️⃣ FRAME DO MODELO, só composição** `input/frames_modelo/K08_modelo.png`
>
> ### 🆕 GERAR DO ZERO

Cena: mecanismo, causa e consequência.

```json
{
  "shot_id": "K08_t8_brandon",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "reference_use": "Use the first attached image only for Brandon's exact identity, wardrobe and her own garage gym. Use the second attached image only as a composition reference for the camera position, framing and the action; do not copy its older man and woman, aprons, kitchen, marble counter, exam room, framed certificates or the caption text.",
  "identity_main": "The exact fictional AI character holistic.brandon: Black mixed-race American woman around thirty, athletic and toned, medium light-brown skin with light freckles across the nose and cheeks, dark brown eyes, defined eyebrows, full lips, hair in tight cornrows that turn into long loose braids falling over both shoulders, finished with small wooden and gold beads, a black floral blackwork tattoo sleeve on her right arm, a small line tattoo on her left upper arm and small fine-line tattoos on her chest near the collarbones. She reads as an ordinary anonymous American fitness coach, not resembling anyone famous.",
  "wardrobe": "Plain white ribbed tank top with nothing printed or written on it, loose black training shorts ending at mid-thigh, a thin gold chain with a small gold cross pendant and small stud earrings.",
  "scene": "Her own garage gym, the same room as the reference: a white-painted concrete block wall and a dark wooden slat ceiling, a red neon sign reading TRAIN PRAY REPEAT on the wall at the left, a whiteboard with handwritten black marker reading STAY READY. STAY DISCIPLINED. on the right, and a small American flag pinned above the whiteboard, discreet but clearly visible and in focus. The background is reduced by framing, never by blur.",
  "prop": "A clear glass mixing bowl full of thick white paste with a metal spoon resting in it, standing still on the black table in front of her; her left hand is open in a small explaining gesture.",
  "posture": "Brandon stands behind the black table in front of her, seen from the waist up, her right hand open on her own chest.",
  "composition": "Straight-on medium shot from table height: the phone lens is about 45 centimeters from the bowl, which sits in the lower left and fills about 20 percent of the frame, closer to the camera than her face; her face and shoulders fill the upper half. Nothing else is on the table. The background is reduced by framing, never by blur.",
  "camera": "phone propped at table height about 45 centimeters from the bowl, standard 1x lens tilted slightly up",
  "lighting": "Neutral overcast daylight from a large window out of frame, soft even light on her face, hands and skin with no harsh shadows. The red neon glows on the wall but does not tint anyone's skin.",
  "state": "Start frame: Brandon is caught mid-sentence, lips naturally parted, animated expression, looking straight into the lens, convinced.",
  "realism": "Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday reality, background fully in focus, everything in sharp focus, no AI polish, no beauty smoothing.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no studio, no plastic-looking skin, no extra fingers, no third hand, no blur, no bokeh, no warm orange color cast, no yellow tint, no golden glow, no golden hour light, no sunset, no HDR, no cinematic lighting, no de-aging, no beauty smoothing, no visible phone, no apron, no older man, no kitchen cabinets, no white marble counter, no framed certificates, no silver cross, no white coat, no second person, no readable lettering on the bowl, spoon or dropper bottle"
}
```

## K09 · T9 · GERAR DO ZERO · ÂNCORA HOLISTIC BRANDON + FRAME DO MODELO

> ### 📎 ANEXAR: **2 IMAGENS**
> **1️⃣ ÂNCORA HOLISTIC BRANDON** `producao/_ancoras/holistic_brandon_ancora.jpg`
> **2️⃣ FRAME DO MODELO, só composição** `input/frames_modelo/K09_modelo.png`
>
> ### 🆕 GERAR DO ZERO

Cena: a saída, tigela de lado.

```json
{
  "shot_id": "K09_t9_brandon",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "reference_use": "Use the first attached image only for Brandon's exact identity, wardrobe and her own garage gym. Use the second attached image only as a composition reference for the camera position, framing and the action; do not copy its older man and woman, aprons, kitchen, marble counter, exam room, framed certificates or the caption text.",
  "identity_main": "The exact fictional AI character holistic.brandon: Black mixed-race American woman around thirty, athletic and toned, medium light-brown skin with light freckles across the nose and cheeks, dark brown eyes, defined eyebrows, full lips, hair in tight cornrows that turn into long loose braids falling over both shoulders, finished with small wooden and gold beads, a black floral blackwork tattoo sleeve on her right arm, a small line tattoo on her left upper arm and small fine-line tattoos on her chest near the collarbones. She reads as an ordinary anonymous American fitness coach, not resembling anyone famous.",
  "wardrobe": "Plain white ribbed tank top with nothing printed or written on it, loose black training shorts ending at mid-thigh, a thin gold chain with a small gold cross pendant and small stud earrings.",
  "scene": "Her own garage gym, the same room as the reference: a white-painted concrete block wall and a dark wooden slat ceiling, a red neon sign reading TRAIN PRAY REPEAT on the wall at the left, a whiteboard with handwritten black marker reading STAY READY. STAY DISCIPLINED. on the right, and a small American flag pinned above the whiteboard, discreet but clearly visible and in focus. The background is reduced by framing, never by blur.",
  "prop": "A clear glass mixing bowl full of thick white paste with a metal spoon resting in it, on the black table in front of her; her right hand rests on the rim of the bowl, about to slide it aside.",
  "posture": "Brandon stands behind the black table in front of her, seen from the waist up, leaning slightly toward the lens.",
  "composition": "Straight-on medium shot from table height: the phone lens is about 45 centimeters from the bowl, which sits in the lower left and fills about 20 percent of the frame, closer to the camera than her face; her face and shoulders fill the upper half. Nothing else is on the table. The background is reduced by framing, never by blur.",
  "camera": "phone propped at table height about 45 centimeters from the bowl, standard 1x lens tilted slightly up",
  "lighting": "Neutral overcast daylight from a large window out of frame, soft even light on her face, hands and skin with no harsh shadows. The red neon glows on the wall but does not tint anyone's skin.",
  "state": "Start frame: Brandon is caught mid-sentence, lips naturally parted, animated expression, looking straight into the lens, firm.",
  "realism": "Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday reality, background fully in focus, everything in sharp focus, no AI polish, no beauty smoothing.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no studio, no plastic-looking skin, no extra fingers, no third hand, no blur, no bokeh, no warm orange color cast, no yellow tint, no golden glow, no golden hour light, no sunset, no HDR, no cinematic lighting, no de-aging, no beauty smoothing, no visible phone, no apron, no older man, no kitchen cabinets, no white marble counter, no framed certificates, no silver cross, no white coat, no second person, no readable lettering on the bowl, spoon or dropper bottle"
}
```

## K10 · T10 · GERAR DO ZERO · ÂNCORA HOLISTIC BRANDON + FRAME DO MODELO + FOTO DO POTE

> ### 📎 ANEXAR: **3 IMAGENS**
> **1️⃣ ÂNCORA HOLISTIC BRANDON** `producao/_ancoras/holistic_brandon_ancora.jpg`
> **2️⃣ FRAME DO MODELO, só composição** `input/frames_modelo/K10_modelo.png`
> **3️⃣ FOTO DO POTE NATURAL REMS, só o pote da frente** `producao/_ancoras/natural_rems_seamoss_produto.jpg`
>
> ### 🆕 GERAR DO ZERO

Cena: pote sobe no nome.

```json
{
  "shot_id": "K10_t10_brandon",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "reference_use": "Use the first attached image only for Brandon's exact identity, wardrobe and her own garage gym. Use the second attached image only as a composition reference for the camera position, framing and the action; do not copy its older man and woman, aprons, kitchen, marble counter, exam room, framed certificates or the caption text. Use the third attached image only for the exact look of the front jar and its label; ignore the MADE IN USA banner, the second jar with the Supplement Facts panel and the loose gummies.",
  "identity_main": "The exact fictional AI character holistic.brandon: Black mixed-race American woman around thirty, athletic and toned, medium light-brown skin with light freckles across the nose and cheeks, dark brown eyes, defined eyebrows, full lips, hair in tight cornrows that turn into long loose braids falling over both shoulders, finished with small wooden and gold beads, a black floral blackwork tattoo sleeve on her right arm, a small line tattoo on her left upper arm and small fine-line tattoos on her chest near the collarbones. She reads as an ordinary anonymous American fitness coach, not resembling anyone famous.",
  "wardrobe": "Plain white ribbed tank top with nothing printed or written on it, loose black training shorts ending at mid-thigh, a thin gold chain with a small gold cross pendant and small stud earrings.",
  "scene": "Her own garage gym, the same room as the reference: a white-painted concrete block wall and a dark wooden slat ceiling, a red neon sign reading TRAIN PRAY REPEAT on the wall at the left, a whiteboard with handwritten black marker reading STAY READY. STAY DISCIPLINED. on the right, and a small American flag pinned above the whiteboard, discreet but clearly visible and in focus. The background is reduced by framing, never by blur.",
  "prop": "Raised with both hands in front of her chest, she holds the Natural Rems Sea Moss Gummies jar exactly as in the attached product photo: a short wide jar of dark amber plastic with a black screw cap, a pale sage-green label with dark green text, the Natural Rems logo with three leaves at the top, the big title Sea Moss Gummies, a pill-shaped badge reading 6000 MG | 16-IN-1, the line GREEN APPLE FLAVOR, two columns of dark green ingredient pills, green seaweed illustrations on the sides and a small 30 Gummies badge. The label is turned straight to the lens and fully readable, her fingers only on the sides of the jar.",
  "posture": "Brandon stands behind the black table in front of her, seen from the waist up, holding the jar toward the camera.",
  "composition": "Straight-on medium shot from table height: the phone lens is about 40 centimeters from the jar, which fills about 25 percent of the frame in the lower center, closer to the camera than her face; her face and shoulders fill the upper half. The table is empty. The background is reduced by framing, never by blur.",
  "camera": "phone propped at table height about 40 centimeters from the jar, standard 1x lens, level",
  "lighting": "Neutral overcast daylight from a large window out of frame, soft even light on her face, hands and skin with no harsh shadows. The red neon glows on the wall but does not tint anyone's skin.",
  "state": "Start frame: Brandon is smiling and caught mid-sentence, lips naturally parted, animated expression, looking straight into the lens.",
  "realism": "Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday reality, background fully in focus, everything in sharp focus, no AI polish, no beauty smoothing.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no studio, no plastic-looking skin, no extra fingers, no third hand, no blur, no bokeh, no warm orange color cast, no yellow tint, no golden glow, no golden hour light, no sunset, no HDR, no cinematic lighting, no de-aging, no beauty smoothing, no visible phone, no apron, no older man, no kitchen cabinets, no white marble counter, no framed certificates, no silver cross, no white coat, no second person, no second jar, no loose gummies, no banner on the jar, no fingers over the label"
}
```

## K11 · T11 · GERAR DO ZERO · ÂNCORA HOLISTIC BRANDON + FRAME DO MODELO + FOTO DO POTE

> ### 📎 ANEXAR: **3 IMAGENS**
> **1️⃣ ÂNCORA HOLISTIC BRANDON** `producao/_ancoras/holistic_brandon_ancora.jpg`
> **2️⃣ FRAME DO MODELO, só composição** `input/frames_modelo/K11_modelo.png`
> **3️⃣ FOTO DO POTE NATURAL REMS, só o pote da frente** `producao/_ancoras/natural_rems_seamoss_produto.jpg`
>
> ### 🆕 GERAR DO ZERO

Cena: CTA, pote parado e legível.

```json
{
  "shot_id": "K11_t11_brandon",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "reference_use": "Use the first attached image only for Brandon's exact identity, wardrobe and her own garage gym. Use the second attached image only as a composition reference for the camera position, framing and the action; do not copy its older man and woman, aprons, kitchen, marble counter, exam room, framed certificates or the caption text. Use the third attached image only for the exact look of the front jar and its label; ignore the MADE IN USA banner, the second jar with the Supplement Facts panel and the loose gummies.",
  "identity_main": "The exact fictional AI character holistic.brandon: Black mixed-race American woman around thirty, athletic and toned, medium light-brown skin with light freckles across the nose and cheeks, dark brown eyes, defined eyebrows, full lips, hair in tight cornrows that turn into long loose braids falling over both shoulders, finished with small wooden and gold beads, a black floral blackwork tattoo sleeve on her right arm, a small line tattoo on her left upper arm and small fine-line tattoos on her chest near the collarbones. She reads as an ordinary anonymous American fitness coach, not resembling anyone famous.",
  "wardrobe": "Plain white ribbed tank top with nothing printed or written on it, loose black training shorts ending at mid-thigh, a thin gold chain with a small gold cross pendant and small stud earrings.",
  "scene": "Her own garage gym, the same room as the reference: a white-painted concrete block wall and a dark wooden slat ceiling, a red neon sign reading TRAIN PRAY REPEAT on the wall at the left, a whiteboard with handwritten black marker reading STAY READY. STAY DISCIPLINED. on the right, and a small American flag pinned above the whiteboard, discreet but clearly visible and in focus. The background is reduced by framing, never by blur.",
  "prop": "Perfectly still with both hands in front of her chest, centered, she holds the Natural Rems Sea Moss Gummies jar exactly as in the attached product photo: a short wide jar of dark amber plastic with a black screw cap, a pale sage-green label with dark green text, the Natural Rems logo with three leaves at the top, the big title Sea Moss Gummies, a pill-shaped badge reading 6000 MG | 16-IN-1, the line GREEN APPLE FLAVOR, two columns of dark green ingredient pills, green seaweed illustrations on the sides and a small 30 Gummies badge. The label is turned straight to the lens, fully readable and with nothing covering it.",
  "posture": "Brandon stands behind the black table in front of her, seen from the chest up, holding the jar toward the camera.",
  "composition": "The tightest shot of the video, straight-on from chest height: the phone lens is about 35 centimeters from the jar, which fills about 30 percent of the frame in the lower center, closer to the camera than her face; her face fills the upper half. The background is reduced by framing, never by blur.",
  "camera": "phone propped at chest height, standard 1x lens, level",
  "lighting": "Neutral overcast daylight from a large window out of frame, soft even light on her face, hands and skin with no harsh shadows. The red neon glows on the wall but does not tint anyone's skin.",
  "state": "Start frame: Brandon is caught mid-sentence, lips naturally parted, animated expression, looking straight into the lens, clear and calm.",
  "realism": "Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday reality, background fully in focus, everything in sharp focus, no AI polish, no beauty smoothing.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no studio, no plastic-looking skin, no extra fingers, no third hand, no blur, no bokeh, no warm orange color cast, no yellow tint, no golden glow, no golden hour light, no sunset, no HDR, no cinematic lighting, no de-aging, no beauty smoothing, no visible phone, no apron, no older man, no kitchen cabinets, no white marble counter, no framed certificates, no silver cross, no white coat, no second person, no second jar, no loose gummies, no banner on the jar, no fingers over the label"
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
a avatar Brandon, mulher, fala em inglês com sotaque americano de uma mulher negra americana, voz feminina clara e firme de uma mulher de uns trinta anos, entonação baixa e séria, como quem conta um segredo de uma cliente, voz autêntica, como se exigisse ser ouvida, a seguinte frase: "She started hiding her legs because of her dark inner thighs."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Brandon, ajoelhada ao lado do banco, passa a mão pela coxa da cliente e aponta a mancha escura com o indicador, olhando para a câmera. A cliente fica deitada e em silêncio. Ela diz a frase em ritmo natural logo no começo e a ação continua em silêncio até o fim.

câmera: leve handheld, baixa, bem perto da coxa

som ambiente: box de treino em casa, tranquilo, sem música
```

### V02 · T2 · usa K02

```text
a avatar Brandon, mulher, fala em inglês com sotaque americano de uma mulher negra americana, voz feminina clara e firme de uma mulher de uns trinta anos, entonação de virada, curiosa, com um meio sorriso, voz autêntica, como se exigisse ser ouvida, a seguinte frase: "Then she found this."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Brandon vira a mão aberta, palma para cima, na direção da câmera; a cliente olha para a câmera com um meio sorriso e fica em silêncio. A coxa não muda. Ela diz a frase em ritmo natural logo no começo e a ação continua em silêncio até o fim.

câmera: leve handheld, baixa, bem perto da coxa

som ambiente: box de treino em casa, tranquilo, sem música
```

### V03 · T3 · usa K03

```text
a avatar Brandon, mulher, fala em inglês com sotaque americano de uma mulher negra americana, voz feminina clara e firme de uma mulher de uns trinta anos, entonação calma e didática, voz autêntica, como se exigisse ser ouvida, a seguinte frase: "Mix a spoonful of baking soda with the juice of half a lemon"

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Brandon, inclinada sobre a mesa, espreme o meio limão dentro da tigela de bicarbonato.

câmera: leve handheld

som ambiente: box de treino em casa, tranquilo, limão pingando na tigela, sem música
```

### V04 · T4 · usa K04

```text
a avatar Brandon, mulher, fala em inglês com sotaque americano de uma mulher negra americana, voz feminina clara e firme de uma mulher de uns trinta anos, entonação calma e didática, voz autêntica, como se exigisse ser ouvida, a seguinte frase: "and two drops of coconut oil until it forms a paste."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Brandon pinga duas gotas de óleo de coco com o conta-gotas dentro da tigela. Ela diz a frase em ritmo natural logo no começo e a ação continua em silêncio até o fim.

câmera: leve handheld

som ambiente: box de treino em casa, tranquilo, gotas caindo na tigela, sem música
```

### V05 · T5 · usa K05

```text
a avatar Brandon, mulher, fala em inglês com sotaque americano de uma mulher negra americana, voz feminina clara e firme de uma mulher de uns trinta anos, entonação calma e didática, firme nos números, voz autêntica, como se exigisse ser ouvida, a seguinte frase: "Rub it in gentle circles on your inner thighs for thirty seconds. Let it sit five minutes, then rinse with cold water."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Brandon mexe a pasta com a colher, mostra o movimento em círculos com a ponta dos dedos e abre cinco dedos no five.

câmera: leve handheld, com leve push-in no meio e volta ao plano

som ambiente: box de treino em casa, tranquilo, colher raspando o vidro, sem música
```

### V06 · T6 · usa K06

```text
a avatar Brandon, mulher, fala em inglês com sotaque americano de uma mulher negra americana, voz feminina clara e firme de uma mulher de uns trinta anos, entonação aliviada e calorosa, voz autêntica, como se exigisse ser ouvida, a seguinte frase: "The skin breathes again. What took years to darken can start to look lighter in days."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Brandon ergue a tigela de pasta na direção da câmera, depois abaixa e gesticula com a mão livre.

câmera: fixa

som ambiente: box de treino em casa, tranquilo, sem música
```

### V07 · T7 · usa K07

```text
a avatar Brandon, mulher, fala em inglês com sotaque americano de uma mulher negra americana, voz feminina clara e firme de uma mulher de uns trinta anos, entonação séria, como quem avisa, voz autêntica, como se exigisse ser ouvida, a seguinte frase: "But the paste only works on the surface, and that darkening keeps coming back when your skin is inflamed underneath."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Brandon, com a tigela parada na mesa, aponta para a pasta e depois abre as mãos.

câmera: fixa

som ambiente: box de treino em casa, tranquilo, sem música
```

### V08 · T8 · usa K08

```text
a avatar Brandon, mulher, fala em inglês com sotaque americano de uma mulher negra americana, voz feminina clara e firme de uma mulher de uns trinta anos, entonação didática e convicta, marcando consequence, voz autêntica, como se exigisse ser ouvida, a seguinte frase: "The darkening was never the problem, it's the consequence. Skin under constant inflammation makes extra pigment to protect itself, and it keeps going darker until that stops."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Brandon aponta a tigela no problem e encosta a mão aberta no próprio peito no protect itself.

câmera: fixa

som ambiente: box de treino em casa, tranquilo, sem música
```

### V09 · T9 · usa K09

```text
a avatar Brandon, mulher, fala em inglês com sotaque americano de uma mulher negra americana, voz feminina clara e firme de uma mulher de uns trinta anos, entonação firme e segura, voz autêntica, como se exigisse ser ouvida, a seguinte frase: "Calm what's happening underneath, and the skin has no reason to keep making that pigment. That's the part no paste can reach."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Brandon empurra a tigela de pasta devagar para o lado, abrindo espaço na mesa.

câmera: fixa

som ambiente: box de treino em casa, tranquilo, sem música
```

### V10 · T10 · usa K10

```text
a avatar Brandon, mulher, fala em inglês com sotaque americano de uma mulher negra americana, voz feminina clara e firme de uma mulher de uns trinta anos, entonação calorosa e confiante, voz autêntica, como se exigisse ser ouvida, a seguinte frase: "That's why I have my clients add Natural Rems Sea Moss. Turmeric, ginger and vitamin C to support your skin from the inside, in one green apple gummy."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Brandon segura o pote de Natural Rems Sea Moss com as duas mãos na altura do peito, rótulo de frente para a câmera, e aproxima o pote um pouco da câmera quando diz o nome.

câmera: fixa

som ambiente: box de treino em casa, tranquilo, sem música
```

### V11 · T11 · usa K11

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
| K09 | ÂNCORA HOLISTIC BRANDON + `input/frames_modelo/K09_modelo.png` (só composição) | Nano Banana 2, 9:16 |
| K10 | ÂNCORA HOLISTIC BRANDON + `input/frames_modelo/K10_modelo.png` (só composição) + `producao/_ancoras/natural_rems_seamoss_produto.jpg` (só o pote da frente) | Nano Banana 2, 9:16 |
| K11 | ÂNCORA HOLISTIC BRANDON + `input/frames_modelo/K11_modelo.png` (só composição) + `producao/_ancoras/natural_rems_seamoss_produto.jpg` (só o pote da frente) | Nano Banana 2, 9:16 |

## Montagem no CapCut

1. Clipes numerados na ordem: V01 a V11.
2. Cortar cada clipe no tempo da cena do modelo: V01 0,0 a 4,7 s; V02 4,7 a 6,2 s; V03 6,2 a 10,2 s; V04 10,2 a 14,0 s; V05 14,0 a 21,8 s; V06 21,8 a 28,8 s; V07 a fala inteira; V08 a fala inteira; V09 a fala inteira; V10 a fala inteira; V11 o CTA inteiro, sem corte.
3. Zero tempo morto: todo clipe começa já falando. Isolate Voice / Keep Vocal no áudio.
4. Nos V01, V02 e V04 (cenas curtas) a fala vem no começo; cortar logo depois da última palavra. O V03 termina sem ponto e o V04 continua a frase: emendar sem pausa.
5. V01 e V02 são o mesmo plano com corte seco entre eles, como no modelo; a coxa não muda de um para o outro.
6. V11 inteiro, sem corte e sem nada cobrindo o pote: é o CTA da marca (frasco parado e legível enquanto o nome é dito). O vídeo acaba nele.
7. Legenda de tela em inglês como no modelo: branca, grossa, palavra a palavra, no meio do quadro.
8. Sem Voice Changer: a voz vem do prompt de cada V.
9. Música só depois do gancho (a partir do V03), nunca no pré-gancho, entre -19 e -20 dB, fora da biblioteca do TikTok.
10. Rótulo pequeno `Synthetic performer` no canto de cima à esquerda, como no modelo.
11. Legenda do post: `#ad #syntheticperformer #naturalrems` na primeira linha e o link da Amazon logo abaixo; chave de conteúdo de IA ligada na plataforma.

## Gates de qualidade

1. Fala de cada V igual ao ROTEIRO, palavra por palavra.
2. Um take por cena do modelo; T1, T2 e T4 marcados CENA CURTA; nenhum take acima de 29 palavras.
3. Bandeira dos EUA no campo scene de todo K.
4. Zero travessão.
5. CTA da marca no T11: Search Natural Rems Sea Moss on Amazon, depois o link da legenda, e fim.
6. Pote em quadro no T10 e no T11, rótulo legível; no T11 parado do começo ao fim.
7. Nada médico em quadro nem na fala (sem maca, papel de maca, camisola, diploma); sem antes e depois; sem cura nem tratamento.
8. Negative sem termo sensível.
9. GATE_VISUAL Partes 1 a 3 em todo K: herói colado na lente, luz neutra, sem tom quente, sem blur, trecho de realismo.
10. Gancho fiel no conteúdo: a mancha escura na coxa da cliente colada na lente, falado desde o segundo 0, e o corte para a mão aberta com a coxa igual.
11. Um K = um V; nenhum K mostra a coxa clara.

