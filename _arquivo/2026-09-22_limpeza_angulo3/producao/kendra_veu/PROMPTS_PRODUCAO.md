# Kendra Collins | Ângulo 3 (Auraly) | Pacote de Prompts

Vídeo modelo: `AQNw72u-N08pJ7ZDe6hq...mp4` (biblioteca #17)
Âncora do avatar: `producao/_ancoras/KENDRA COLLINS .jpeg`
Roteiro: `ROTEIRO.md` · DM: `DM.md`

Funil: comentar `222` → DM → mensagem com o rosto → link
**Sem take de produto.** O prop herói é a **carta**.

## FORMATO: PLANO ÚNICO
Câmera na altura do peito, do outro lado da mesa. Kendra do peito pra cima em cima, **mesa no terço inferior do MESMO quadro**, e **ela executa a ação com as próprias mãos enquanto fala**. Sem split screen, sem close isolado na mesa, sem B-roll separado.

## As 5 variações (as mesmas do `blake_veu`)

| Var | Gancho | Keyframe do T1 | Clipe do T1 |
|---|---|---|---|
| **A** | véu puxado do retrato | K01A | V01A |
| **B** | polaroid revelando | K01B | V01B |
| **C** | fio vermelho do destino | K01C | V01C |
| **D** | círculo de sal com vela | K01D | V01D |
| **E** | envelope com lacre de cera | K01E | V01E |

**K02, K03 e os clipes V02 a V07 são gerados uma vez só e servem às cinco.** Cada gancho custa **1 keyframe + 1 clipe**.

---

## Índice de geração

| Take | Keyframe | Ação de geração |
|---|---|---|
| REF-CARTA | REF | reaproveitar a do `blake_inicial` se já aprovada, senão gerar |
| T1 | K01A a K01E | **GERAR DO ZERO**, um por variação · ÂNCORA KENDRA + REF-CARTA |
| T2 a T5 | K02 | **GERAR DO ZERO** (setup novo, enquadramento fechado) · ÂNCORA KENDRA + REF-CARTA |
| T6, T7 | K03 | **EDITAR do K02** |

> A **REF-CARTA é do ângulo, não do avatar.** Se a arte já foi aprovada para o Blake, usar a mesma. Duas contas com a mesma carta é coerência do produto, não repetição.

---

## Trava de identidade e continuidade

Aplicar em toda imagem e todo clipe:

- Rosto da Kendra da âncora: mulher branca americana, **fim dos vinte**, pele clara com **poros visíveis, sardas no nariz e nas bochechas** e pequenas imperfeições reais, sobrancelhas claras, lábios cheios, olhos claros, **piercing pequeno de argola numa narina**.
- **Cabelo raspado platinado**, buzzcut bem curto, mais curto nas laterais.
- **Óculos pretos grossos**, armação retangular de cantos levemente arredondados.
- **Regata branca canelada** com **camisa de linho cor aveia aberta por cima**, mangas dobradas até o cotovelo.
- **Corrente fina de PRATA com pingente de cruz de PRATA trabalhada.** Nunca ouro. **Anéis finos de prata** nas mãos.
- Mesmo quarto, mas **em quadro só TRÊS âncoras de fundo**: **um quadro emoldurado da roda zodiacal** na parede branca, a **cruz de madeira na parede** e a **borda da estante com uma drusa de ametista roxa**. A **mesa de madeira clara** de tampo gasto ocupa o primeiro plano.
- **Todo o resto do quarto fica FORA DE QUADRO por enquadramento**, nunca por blur. Sem janela, sem os outros dois quadros, sem bandeira, sem livros, sem incenso.
- **Luz neutra de dia nublado**, difusa e levemente fria. **Nunca luz quente.**
- **Zero blur, tudo nítido.** Cara de vídeo de iPhone.

---

## Trava do prop herói · a CARTA (REF-CARTA)

Se já aprovada no `blake_inicial`, **reaproveitar**. Se precisar gerar:

```json
{
  "shot_id": "REF_CARTA_soulmate",
  "subject": "A single traditional divination tarot card lying flat on a plain light wooden table, photographed straight from above. It is a real printed tarot card in the Rider-Waite lineage, not a modern illustration and not a children's book drawing.",
  "card_stock": "Aged ivory cardstock with visible paper fibre and a matte uncoated surface. The corners are slightly worn and softly rounded from handling. The card is NOT bright white.",
  "card_border": "A thick ornate border printed in matte antique gold, with fine engraved scrollwork running along all four sides and a small symmetrical flourish in each corner, framing the artwork in a clean inner rectangle. At the top centre, inside the border, the roman numeral VI in letter-spaced serif capitals.",
  "card_art": "Inside the frame, two robed figures stand close, one behind the other, the front figure's head tilted back to rest against the other's shoulder, both seen in profile. They are drawn in a flat symbolic style with fine ink hatching and limited flat colour, the way classic tarot figures are drawn: stylised and serene, never cartoonish, never with big rounded cute faces. They wear simple timeless robes, never modern clothing. Behind them a stylised sun and a crescent moon overlap, with a scatter of small five pointed stars.",
  "palette": "Limited and muted: antique gold, ivory, dusty rose and pale blue, with black ink line work. Matte and slightly faded, never bright pastel and never glossy.",
  "card_title": "At the bottom of the card, inside a narrow banner set into the gold border, the single word SOULMATE in letter-spaced serif capitals. This word is the ONLY text on the card besides the roman numeral.",
  "composition": "Straight down from above, close. The card fills most of the frame, resting flat and fully visible, no hand touching it. The table is bare around it.",
  "lighting": "Soft neutral daylight of an overcast day from the side, even and slightly cool, gentle shadow under the card edge. No warm orange cast.",
  "realism": "Real photograph of a real printed tarot card, iPhone-footage look, visible paper grain and fibre, tiny surface imperfections, realistic shadow, no AI polish, sharp focus across the whole card, no blur.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no watermark, no cartoon style, no children's book illustration, no cute rounded faces, no modern clothing, no white border, no bright pastel colors, no comic art, no 3d render, no glossy plastic sheen, no dark or gothic art, no black card, no skulls, no hands, no blur, no warm orange color cast"
}
```

---

## Trava da 2ª pessoa (REF-A)

**Não se aplica.** Vídeo solo. Negative de todos os prompts carrega `no second person`.

---

## Gate de composição visual

```
HERÓI
[x] 1. No T1 o herói é a AÇÃO na mesa, no lower foreground, mais perto da lente que o rosto
[x] 2. Do T2 em diante o herói é a CARTA na mão, também mais perto que o rosto
[x] 3. Forma e cor da carta travadas no REF-CARTA

DISTÂNCIA
[x] 4. Âncora é plano médio sentado. Override de postura e composição em todo prompt
[x] 5. Peito pra cima em todos os takes
[x] 6. Take mais fechado do vídeo é o CTA (K03)

FUNDO
[x] 7. Três âncoras: quadro da roda zodiacal, cruz na parede, borda da estante com ametista
[x] 8. Fundo reduzido por ENQUADRAMENTO, nunca por blur
[x] 9. Mesa limpa, só o objeto do gancho e a carta

2ª PESSOA
[x] 10. Não se aplica
```

## Gate de realismo

```
[x] 1. Herói ISOLADO. Três âncoras de fundo, não o quarto inteiro
[x] 2. Câmera puxada pra perto. No T1 o herói enche os dois terços de baixo
[x] 3. Luz NEUTRA de dia nublado. Nenhum "warm and even"
[x] 4. Negative carrega: no warm orange color cast, no yellow tint, no golden glow
[x] 5. Fundo específico e nunca borrado
[x] 6. REF-CARTA aprovado antes de tudo
[x] 7. Bloco de realismo padrão colado por inteiro em todo prompt
```

---

# Prompts de imagem · T1, um por variação

## K01A · VARIAÇÃO A · VÉU PUXADO DO RETRATO · GERAR DO ZERO · ÂNCORA KENDRA

```json
{
  "shot_id": "K01A_kendra_hook_veu_retrato",
  "reference_use": "Use the attached image ONLY for Kendra's face, identity, hair, glasses, wardrobe, silver cross and the room. Reproduce her as the SAME person. Do NOT copy the pose of the reference, she must be leaning slightly forward and working with her hands on the table.",
  "identity_main": "The EXACT woman from the reference image (Kendra): white American woman in her late twenties, athletic build, fair skin with real visible pores, freckles across the nose and cheeks and small natural blemishes, pale blonde eyebrows, full lips, light eyes, a tiny hoop stud in one nostril. Very short platinum bleached buzzcut, closely cropped at the sides. Thick black rectangular glasses with slightly rounded corners.",
  "wardrobe": "White ribbed cotton tank top with an oatmeal linen shirt worn open over it, sleeves rolled to the elbow. Thin SILVER chain with a small ornate SILVER cross pendant. Thin silver rings on her fingers.",
  "scene": "SAME room as the reference but with almost NOTHING else in frame: the light oak wooden table with its worn scratched top filling the lower part of the shot, and behind her only THREE readable anchors, one framed zodiac wheel print on the white wall, the plain wooden cross on the wall, and the edge of the wooden shelf with a single purple amethyst geode on it. Every other object in the room is out of frame.",
  "action": "A small dark wooden picture frame lies flat on the table in front of her, still mostly covered by a loose piece of pale natural linen cloth. Her right hand has taken hold of one corner of the cloth and has begun to lift it, so a sliver of the frame is uncovered. Under the cloth is a printed photograph of a man from the chest up, and THE PRINTED PHOTOGRAPH ITSELF IS OUT OF FOCUS, so the face is a soft unreadable smudge on the paper. The frame, the glass and the cloth are perfectly sharp.",
  "posture": "She sits at the table leaning slightly forward toward the camera, shoulders squared, head up and eyes looking straight into the lens while her hands work on the table below. She is speaking.",
  "composition": "Vertical shot from across the table, camera at chest height and PUSHED IN CLOSE. The frame and the cloth fill the lower two thirds of the frame and are clearly closer to the lens than her face. Her face and shoulders sit in the upper third, cropped just above the top of her head. Only the framed print, the wall cross and a sliver of the shelf are visible behind her, small and secondary. ONE continuous shot, no split screen and no inset.",
  "camera": "chest level, straight-on, phone propped on the far edge of the table",
  "state": "Start frame: the cloth still covers most of the frame, her hand is gripping the corner.",
  "lighting": "Soft neutral daylight of an overcast day coming from a window out of frame. Even and slightly cool. No warm orange cast, no golden glow.",
  "realism": "UGC realism, real skin texture with visible pores, individual short hairs on the scalp, subtle wrinkles, realistic shadows and honest reflections on the glasses lenses, iPhone-footage look, phone camera look not professional photography, no AI polish, no beauty smoothing, no blur anywhere, everything in sharp focus including background walls furniture and details.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no readable face, no sharp portrait, no split screen, no inset frame, no studio lighting, no plastic skin, no beauty filter, no extra fingers, no blur, no gold jewelry, no second person, no dark or gothic styling, no warm orange color cast, no yellow tint, no golden glow, no cluttered background"
}
```

## K01B · VARIAÇÃO B · POLAROID REVELANDO · GERAR DO ZERO · ÂNCORA KENDRA

```json
{
  "shot_id": "K01B_kendra_hook_polaroid",
  "reference_use": "Use the attached image ONLY for Kendra's face, identity, hair, glasses, wardrobe, silver cross and the room. Do NOT copy the pose, she must be leaning slightly forward with her hands on the table.",
  "identity_main": "The EXACT woman from the reference image (Kendra): white American woman in her late twenties, fair skin with real visible pores, freckles across the nose and cheeks, pale blonde eyebrows, full lips, light eyes, a tiny hoop stud in one nostril. Very short platinum bleached buzzcut. Thick black rectangular glasses.",
  "wardrobe": "White ribbed cotton tank top with an oatmeal linen shirt worn open over it, sleeves rolled to the elbow. Thin SILVER chain with a small ornate SILVER cross pendant. Thin silver rings.",
  "scene": "SAME room as the reference but with almost NOTHING else in frame: the light oak wooden table filling the lower part of the shot, and behind her only THREE readable anchors, one framed zodiac wheel print on the white wall, the plain wooden cross on the wall, and the edge of the wooden shelf with a single purple amethyst geode. Every other object is out of frame.",
  "action": "A single instant photo with the classic white border lies on the table in front of her, held flat under her fingertips. The image inside is only HALF DEVELOPED: the background and the outline of a man's head and shoulders have come through in pale grey, but the face area is still an unresolved flat grey patch with no features at all. The white border and the table are perfectly sharp.",
  "posture": "She sits at the table leaning slightly forward toward the camera, shoulders squared, head up and eyes looking straight into the lens while her fingers rest on the photo below. She is speaking.",
  "composition": "Vertical shot from across the table, camera at chest height and PUSHED IN CLOSE. The instant photo fills the lower two thirds of the frame and is clearly closer to the lens than her face. Her face and shoulders sit in the upper third. Only the framed print, the wall cross and a sliver of the shelf are visible behind her. ONE continuous shot, no split screen and no inset.",
  "camera": "chest level, straight-on, phone propped on the far edge of the table",
  "state": "Start frame: the photo is mid development, the face still blank grey.",
  "lighting": "Soft neutral daylight of an overcast day coming from a window out of frame. Even and slightly cool. No warm orange cast, no golden glow.",
  "realism": "UGC realism, real skin texture with visible pores, individual short hairs on the scalp, subtle wrinkles, realistic shadows and honest reflections on the glasses lenses, iPhone-footage look, phone camera look not professional photography, no AI polish, no beauty smoothing, no blur anywhere, everything in sharp focus including background walls furniture and details.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no readable face, no facial features, no finished photograph, no split screen, no inset frame, no studio lighting, no plastic skin, no beauty filter, no extra fingers, no blur, no gold jewelry, no second person, no dark or gothic styling, no warm orange color cast, no yellow tint, no golden glow, no cluttered background"
}
```

## K01C · VARIAÇÃO C · FIO VERMELHO DO DESTINO · GERAR DO ZERO · ÂNCORA KENDRA + REF-CARTA

```json
{
  "shot_id": "K01C_kendra_hook_fio_vermelho",
  "reference_use": "Use the FIRST attached image ONLY for Kendra's face, identity, hair, glasses, wardrobe, silver cross and the room. Do NOT copy the pose, she must be leaning slightly forward with her hands on the table. Use the SECOND attached image ONLY to reproduce the tarot card art exactly.",
  "identity_main": "The EXACT woman from the first reference image (Kendra): white American woman in her late twenties, fair skin with real visible pores, freckles across the nose and cheeks, pale blonde eyebrows, full lips, light eyes, a tiny hoop stud in one nostril. Very short platinum bleached buzzcut. Thick black rectangular glasses.",
  "wardrobe": "White ribbed cotton tank top with an oatmeal linen shirt worn open over it, sleeves rolled to the elbow. Thin SILVER chain with a small ornate SILVER cross pendant. Thin silver rings.",
  "scene": "SAME room as the reference but with almost NOTHING else in frame: the light oak wooden table filling the lower part of the shot, and behind her only THREE readable anchors, one framed zodiac wheel print on the white wall, the plain wooden cross on the wall, and the edge of the wooden shelf with a single purple amethyst geode. Every other object is out of frame.",
  "action": "Two plain gold wedding bands sit apart on the table, one to her left and one to her right. A single red cotton thread is tied to each ring and lies loose and wavy across the wood with plenty of slack. Each of her hands holds one end of the thread just behind the rings, and she has started to draw them apart. The tarot card from the second reference lies flat between the two rings, facing up and fully readable.",
  "posture": "She sits at the table leaning slightly forward toward the camera, shoulders squared, head up and eyes looking straight into the lens while her hands work the thread below. She is speaking.",
  "composition": "Vertical shot from across the table, camera at chest height and PUSHED IN CLOSE. The rings, the thread and the card fill the lower two thirds of the frame and are clearly closer to the lens than her face. Her face and shoulders sit in the upper third. Only the framed print, the wall cross and a sliver of the shelf are visible behind her. ONE continuous shot, no split screen and no inset.",
  "camera": "chest level, straight-on, phone propped on the far edge of the table",
  "state": "Start frame: the thread is still slack and wavy.",
  "lighting": "Soft neutral daylight of an overcast day coming from a window out of frame. Even and slightly cool. No warm orange cast, no golden glow.",
  "realism": "UGC realism, real skin texture with visible pores, individual short hairs on the scalp, subtle wrinkles, realistic shadows and honest reflections on the glasses lenses, iPhone-footage look, phone camera look not professional photography, no AI polish, no beauty smoothing, no blur anywhere, everything in sharp focus including background walls furniture and details.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no split screen, no inset frame, no studio lighting, no plastic skin, no beauty filter, no extra fingers, no glow effects, no blur, no gold necklace, no second person, no dark or gothic styling, no warm orange color cast, no yellow tint, no golden glow, no cluttered background"
}
```

## K01D · VARIAÇÃO D · CÍRCULO DE SAL COM VELA · GERAR DO ZERO · ÂNCORA KENDRA + REF-CARTA

```json
{
  "shot_id": "K01D_kendra_hook_circulo_sal",
  "reference_use": "Use the FIRST attached image ONLY for Kendra's face, identity, hair, glasses, wardrobe, silver cross and the room. Do NOT copy the pose, she must be leaning slightly forward and working with her hands on the table. Use the SECOND attached image ONLY to reproduce the tarot card art exactly.",
  "identity_main": "The EXACT woman from the first reference image (Kendra): white American woman in her late twenties, fair skin with real visible pores, freckles across the nose and cheeks, pale blonde eyebrows, full lips, light eyes, a tiny hoop stud in one nostril. Very short platinum bleached buzzcut. Thick black rectangular glasses.",
  "wardrobe": "White ribbed cotton tank top with an oatmeal linen shirt worn open over it, sleeves rolled to the elbow. Thin SILVER chain with a small ornate SILVER cross pendant. Thin silver rings.",
  "scene": "SAME room as the reference but with almost NOTHING else in frame: the light oak wooden table filling the lower part of the shot, and behind her only THREE readable anchors, one framed zodiac wheel print on the white wall, the plain wooden cross on the wall, and the edge of the wooden shelf with a single purple amethyst geode. Every other object is out of frame.",
  "action": "She is pouring coarse white salt from a small clear glass jar held in her right hand, tilting it over the table. The salt has already formed a thick ring on the wood and only a small gap is still open on one side. In the middle of the ring stands a short white pillar candle, lit, with a small steady flame. The tarot card from the second reference lies flat inside the ring beside the candle, facing up and fully readable.",
  "posture": "She sits at the table leaning slightly forward toward the camera, shoulders squared, head up and eyes looking straight into the lens while her hands work on the table below. She is speaking.",
  "composition": "Vertical shot from across the table, camera at chest height and PUSHED IN CLOSE. The salt ring, the candle and the card fill the lower two thirds of the frame and are clearly closer to the lens than her face. Her face and shoulders sit in the upper third. Only the framed print, the wall cross and a sliver of the shelf are visible behind her. ONE continuous shot, no split screen and no inset.",
  "camera": "chest level, straight-on, phone propped on the far edge of the table",
  "state": "Start frame: the ring still has a visible gap, the jar is tilted and salt is falling.",
  "lighting": "Soft neutral daylight of an overcast day coming from a window out of frame. Even and slightly cool. No warm orange cast, no golden glow.",
  "realism": "UGC realism, real skin texture with visible pores, individual short hairs on the scalp, individual salt grains, subtle wrinkles, realistic shadows and honest reflections on the glasses lenses, iPhone-footage look, phone camera look not professional photography, no AI polish, no beauty smoothing, no blur anywhere, everything in sharp focus including background walls furniture and details.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no split screen, no inset frame, no studio lighting, no plastic skin, no beauty filter, no extra fingers, no supernatural lighting, no glow effects, no blur, no gold jewelry, no second person, no dark or gothic styling, no warm orange color cast, no yellow tint, no golden glow, no cluttered background"
}
```

## K01E · VARIAÇÃO E · ENVELOPE COM LACRE DE CERA · GERAR DO ZERO · ÂNCORA KENDRA

```json
{
  "shot_id": "K01E_kendra_hook_envelope_lacre",
  "reference_use": "Use the attached image ONLY for Kendra's face, identity, hair, glasses, wardrobe, silver cross and the room. Do NOT copy the pose, she must be leaning slightly forward with the envelope in her hands over the table.",
  "identity_main": "The EXACT woman from the reference image (Kendra): white American woman in her late twenties, fair skin with real visible pores, freckles across the nose and cheeks, pale blonde eyebrows, full lips, light eyes, a tiny hoop stud in one nostril. Very short platinum bleached buzzcut. Thick black rectangular glasses.",
  "wardrobe": "White ribbed cotton tank top with an oatmeal linen shirt worn open over it, sleeves rolled to the elbow. Thin SILVER chain with a small ornate SILVER cross pendant. Thin silver rings.",
  "scene": "SAME room as the reference but with almost NOTHING else in frame: the light oak wooden table filling the lower part of the shot, and behind her only THREE readable anchors, one framed zodiac wheel print on the white wall, the plain wooden cross on the wall, and the edge of the wooden shelf with a single purple amethyst geode. Every other object is out of frame.",
  "action": "She holds a cream coloured paper envelope flat with both hands just above the tabletop, tilted toward the camera so the sealed flap is visible. The flap is closed with a round blob of deep red wax, smooth, glossy and unbroken. Both thumbs are pressed at the edges of the seal. The envelope looks slightly thick, as if a card is inside.",
  "posture": "She sits at the table leaning slightly forward toward the camera, shoulders squared, head up and eyes looking straight into the lens while her hands hold the envelope below. She is speaking.",
  "composition": "Vertical shot from across the table, camera at chest height and PUSHED IN CLOSE. The envelope and the wax seal fill the lower two thirds of the frame and are clearly closer to the lens than her face. Her face and shoulders sit in the upper third. Only the framed print, the wall cross and a sliver of the shelf are visible behind her. ONE continuous shot, no split screen and no inset.",
  "camera": "chest level, straight-on, phone propped on the far edge of the table",
  "state": "Start frame: the wax seal is still whole, thumbs in position.",
  "lighting": "Soft neutral daylight of an overcast day coming from a window out of frame. Even and slightly cool. No warm orange cast, no golden glow.",
  "realism": "UGC realism, real skin texture with visible pores, individual short hairs on the scalp, subtle wrinkles, realistic shadows and honest reflections on the glasses lenses, iPhone-footage look, phone camera look not professional photography, no AI polish, no beauty smoothing, no blur anywhere, everything in sharp focus including background walls furniture and details.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no writing on the envelope, no split screen, no inset frame, no studio lighting, no plastic skin, no beauty filter, no extra fingers, no blur, no gold jewelry, no second person, no dark or gothic styling, no warm orange color cast, no yellow tint, no golden glow, no cluttered background"
}
```

---

# Prompts de imagem · T2 em diante (compartilhados)

## K02 · T2 A T5 · CARTA NA MÃO · GERAR DO ZERO · ÂNCORA KENDRA + REF-CARTA

```json
{
  "shot_id": "K02_kendra_carta_na_mao",
  "reference_use": "Use the FIRST attached image ONLY for Kendra's face, identity, hair, glasses, wardrobe, silver cross and the room. Do NOT copy the pose or the camera distance, this shot is much closer. Use the SECOND attached image ONLY to reproduce the tarot card art exactly.",
  "identity_main": "The EXACT woman from the first reference image (Kendra): white American woman in her late twenties, fair skin with real visible pores, freckles across the nose and cheeks and small natural blemishes, pale blonde eyebrows, full lips, light eyes, a tiny hoop stud in one nostril. Very short platinum bleached buzzcut, closely cropped at the sides. Thick black rectangular glasses with slightly rounded corners.",
  "wardrobe": "White ribbed cotton tank top with an oatmeal linen shirt worn open over it, sleeves rolled to the elbow. Thin SILVER chain with a small ornate SILVER cross pendant. Thin silver rings.",
  "scene": "SAME room as the reference, tighter: only THREE anchors visible behind her, one framed zodiac wheel print on the white wall, the plain wooden cross on the wall, and the edge of the wooden shelf with a single purple amethyst geode. Only a thin sliver of the tabletop shows at the very bottom edge. Everything else is out of frame.",
  "action": "Her right hand holds the tarot card from the second reference raised beside her face at cheek height, pushed slightly toward the lens so the card is closer to the camera than her face. The card faces the camera and is fully readable. Reproduce the card art EXACTLY: the ornate antique gold border, the roman numeral at the top, the two robed figures, the muted ivory and gold palette and the word in the bottom banner. Her left hand is out of frame.",
  "posture": "She sits upright facing the camera, mouth slightly open as if speaking, eyes on the lens.",
  "composition": "Vertical, CLOSE, chest up. Much tighter than the reference. Her face fills the upper middle of the frame, cropped just above the top of her head. The card sits beside her cheek, nearer the lens than her face. The table is essentially out of frame.",
  "camera": "chest level, straight-on, phone propped across from her",
  "state": "Neutral speaking frame with the card raised beside the face.",
  "lighting": "Soft neutral daylight of an overcast day coming from a window out of frame. Even and slightly cool. No warm orange cast, no golden glow.",
  "realism": "UGC realism, real skin texture with visible pores, individual short hairs on the scalp, subtle wrinkles, realistic shadows and honest reflections on the glasses lenses, visible card paper grain, iPhone-footage look, phone camera look not professional photography, no AI polish, no beauty smoothing, no blur anywhere, everything in sharp focus including background walls furniture and details.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no split screen, no studio lighting, no plastic skin, no beauty filter, no extra fingers, no supernatural lighting, no glow effects, no blur, no gold jewelry, no second person, no dark or gothic card, no salt, no envelope, no picture frame, no thread, no instant photo, no warm orange color cast, no yellow tint, no golden glow, no cluttered background"
}
```

## K03 · T6 E T7 · CTA, MAIS FECHADO · EDITAR do K02

```json
{
  "task": "edit the attached image, keep everything identical except the changes listed",
  "keep_identical": "Keep Kendra exactly the same: same face, same freckles, same platinum buzzcut, same black glasses, same white tank with the oatmeal linen shirt, same SILVER cross and silver rings. Keep the SAME tarot card with the same art. Keep the SAME room, framed zodiac print, wall cross, shelf edge with the amethyst, and the same neutral overcast lighting.",
  "change_1": "Push the camera closer so the framing tightens by about twenty five percent. Her face fills more of the frame, cropped at the top of her head and at the shoulders. Do not change the angle or the height of the camera.",
  "change_2": "The card is held a little higher, right beside her temple, still facing the camera and fully readable. Less of the room is visible because the framing is tighter.",
  "realism": "UGC realism, real skin texture with visible pores, iPhone-footage look, no AI polish, no beauty smoothing, no blur anywhere. Do not make her skin more orange or yellow. Do not make the colors more saturated.",
  "negative": "do not change the face, do not change the identity, do not redraw the card art, do not add background objects, no captions, no subtitles, no words overlaid on the image, no plastic skin, no beauty filter, no extra fingers, no gold jewelry, no second person, no blur, no warm orange color cast, no yellow tint"
}
```

---

# Prompts de vídeo (Veo 3.1 via Flow)

## Bloco global

Colar em todo prompt:

```text
a avatar (mulher) fala em inglês com sotaque americano de mulher branca, voz autêntica, calma e direta, como se estivesse contando algo que só ela está vendo.

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

Estilo TikTok nativo, UGC. Preservar exatamente a identidade da Kendra, rosto, sardas, buzzcut platinado, óculos pretos, regata branca com camisa de linho aveia, cruz de PRATA, o quarto com o quadro de astrologia e a cruz na parede, a iluminação e o enquadramento do frame inicial. Plano único, sem split screen. Sem legenda, sem texto gerado, sem música, sem pessoas extras.
```

---

### V01A · T1 · VARIAÇÃO A · usa K01A

```text
a avatar (mulher) fala em inglês com sotaque americano de mulher branca, voz autêntica, calma e direta, a seguinte frase: "Before you scroll. Almost everyone scrolls past this. The ones who stay always come back saying the same thing."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: enquanto fala olhando na lente, ela puxa o pano de linho devagar para o lado, descobrindo o retrato por completo. O rosto impresso na foto continua sendo uma mancha suave e ilegível. Ela solta o pano fora de quadro.

câmera: fixa, leve handheld natural

som ambiente: ambiente de quarto de casa, som suave de tecido deslizando, sem música
```

### V01B · T1 · VARIAÇÃO B · usa K01B

```text
a avatar (mulher) fala em inglês com sotaque americano de mulher branca, voz autêntica, calma e direta, a seguinte frase: "Before you scroll. Almost everyone scrolls past this. The ones who stay always come back saying the same thing."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: enquanto fala olhando na lente, ela desliza a foto instantânea um pouco para a frente na mesa com os dedos. Na foto o fundo e o contorno dos ombros vão aparecendo devagar, e a área do rosto continua uma mancha cinza lisa que não se resolve.

câmera: fixa, leve handheld natural

som ambiente: ambiente de quarto de casa, sem música
```

### V01C · T1 · VARIAÇÃO C · usa K01C

```text
a avatar (mulher) fala em inglês com sotaque americano de mulher branca, voz autêntica, calma e direta, a seguinte frase: "Before you scroll. Almost everyone scrolls past this. The ones who stay always come back saying the same thing."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: enquanto fala olhando na lente, ela afasta as duas mãos e o fio vermelho vai perdendo a folga até esticar reto entre as alianças. Com o fio tenso, as duas alianças deslizam uma na direção da outra sobre a madeira até encostarem.

câmera: fixa, leve handheld natural

som ambiente: ambiente de quarto de casa, tilintar curto de metal no fim, sem música
```

### V01D · T1 · VARIAÇÃO D · usa K01D

```text
a avatar (mulher) fala em inglês com sotaque americano de mulher branca, voz autêntica, calma e direta, a seguinte frase: "Before you scroll. Almost everyone scrolls past this. The ones who stay always come back saying the same thing."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: enquanto fala olhando na lente, ela inclina o potinho de vidro e derrama o sal que falta, fechando o círculo por inteiro ao redor da carta. Depois apoia o potinho na mesa.

câmera: fixa, leve handheld natural

som ambiente: ambiente de quarto de casa, som seco de grãos caindo na madeira, sem música
```

### V01E · T1 · VARIAÇÃO E · usa K01E

```text
a avatar (mulher) fala em inglês com sotaque americano de mulher branca, voz autêntica, calma e direta, a seguinte frase: "Before you scroll. Almost everyone scrolls past this. The ones who stay always come back saying the same thing."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: enquanto fala olhando na lente, ela pressiona os polegares e o lacre de cera vermelha racha ao meio. A aba do envelope abre para trás e ela inclina o envelope, deixando uma carta de tarô deslizar para fora até a metade.

câmera: fixa, leve handheld natural

som ambiente: ambiente de quarto de casa, estalo seco da cera e papel deslizando, sem música
```

---

### V02 · T2 · usa K02

```text
a avatar (mulher) fala em inglês com sotaque americano de mulher branca, voz autêntica, calma e direta, a seguinte frase: "Something was covering this, and it just lifted. There is a face the universe has been holding for you."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ela ergue a carta alguns centímetros ao dizer que algo se levantou, e volta a baixar. Mantém o olhar na lente.

câmera: fixa, leve handheld natural

som ambiente: ambiente de quarto de casa, sem música
```

### V03 · T3 · usa K02

```text
a avatar (mulher) fala em inglês com sotaque americano de mulher branca, voz autêntica, calma e direta, a seguinte frase: "Not hidden from you. Held for you, until you were ready. And today you were the one who stopped."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ela balança a cabeça devagar em negativa ao dizer "not hidden", e depois assente uma vez. A carta continua firme na mão.

câmera: fixa, leve handheld natural

som ambiente: ambiente de quarto de casa, sem música
```

### V04 · T4 · usa K02

```text
a avatar (mulher) fala em inglês com sotaque americano de mulher branca, voz autêntica, calma e direta, a seguinte frase: "It is open right now, and it stays open one day. After that it closes and goes quiet again."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ela levanta o dedo indicador da mão livre ao dizer "one day", e depois recolhe a mão. A carta não se move.

câmera: fixa, leve handheld natural

som ambiente: ambiente de quarto de casa, sem música
```

### V05 · T5 · usa K02

```text
a avatar (mulher) fala em inglês com sotaque americano de mulher branca, voz autêntica, calma e direta, a seguinte frase: "Comment 222 below so the universe knows you are claiming it. Then send this video to yourself and save it."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ela aponta para baixo com a mão livre ao dizer "below" e depois abre a palma na direção da lente. A carta continua erguida na outra mão.

câmera: fixa, leve handheld natural

som ambiente: ambiente de quarto de casa, sem música
```

### V06 · T6 · usa K03

```text
a avatar (mulher) fala em inglês com sotaque americano de mulher branca, voz autêntica, calma e direta, a seguinte frase: "The second you comment 222, I send their face straight to your messages. That is where the reveal happens."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ela se inclina levemente para a lente ao dizer "I send their face", e mantém o olhar fixo até o fim da frase. A carta fica parada ao lado do rosto.

câmera: fixa, leve push-in muito sutil

som ambiente: ambiente de quarto de casa, sem música
```

### V07 · T7 · usa K03

```text
a avatar (mulher) fala em inglês com sotaque americano de mulher branca, voz autêntica, calma e direta, a seguinte frase: "But follow me first, or it will not let me reach you. And I only have three readings left today."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ela aponta para cima com o indicador da mão livre ao dizer "follow me first", e depois baixa a mão. Termina olhando parada na lente, com a carta ainda erguida.

câmera: fixa, leve push-in muito sutil

som ambiente: ambiente de quarto de casa, sem música
```

---

## Mapa de âncoras

| Keyframe | Referências a anexar | Modelo |
|---|---|---|
| REF-CARTA | reaproveitar a aprovada, senão gerar do zero | Nano Banana **Pro** |
| K01A, K01B, K01E | **ÂNCORA KENDRA** | Nano Banana **Pro**, várias variações |
| K01C, K01D | **ÂNCORA KENDRA + REF-CARTA** | Nano Banana **Pro**, várias variações |
| K02 | **ÂNCORA KENDRA + REF-CARTA** | Nano Banana **Pro** |
| K03 | K02 aprovado | Nano Banana 2, edição |

---

## Montagem no CapCut

- Timeline 1080x1920, 30 fps. **Plano único o vídeo inteiro.**
- Cortes duros entre todos os takes. O único que pede peso é T1 para T2, que é a troca de setup.
- Cortar o silêncio inicial de cada clipe.
- **Gráfico fixo o vídeo inteiro:** `222` no topo à esquerda, do frame 0 ao fim.
- **Legendas karaokê**, uma linha por vez, palavra destacada em **amarelo**. **Nunca cobrir a mesa no T1 nem a carta nos demais takes.**
- **Texto de gancho** em caixa branca no topo, só nos primeiros segundos: A e B usam `MAN HIDING TWO`, C usa `SITTING EXACTLY WHERE`, D e E usam `SKIP THIS Y'ALL`.
- Manter `222` isolado e grande na tela durante o V05 e o V06.
- **Cartela final** depois do V07: foto de perfil em círculo com seta apontando pra ela.
- Color grading: temp -3, tint +2, saturação -6, exposição -3, contraste +12, highlight -35, shadow +18, fade +6.

---

## Gates de qualidade

1. **Plano único em todos os keyframes**, sem split screen, moldura ou inset.
2. **No T1 a Kendra está em quadro executando a ação com as próprias mãos.**
3. Mesma mulher em todos os clipes, com **óculos pretos, buzzcut platinado e cruz de PRATA**.
4. **Sardas no nariz e nas bochechas presentes em todos os planos.** É o traço que mais some em regeneração.
5. **Reflexo honesto nas lentes dos óculos**, sem lente apagada nem vidro invisível.
6. **A carta tem arte idêntica ao REF-CARTA** em K01C, K01D, K02 e K03.
7. **A carta está na mão dela do T2 ao T7**, sem sumir.
8. 🚫 **Nenhum rosto de alma gêmea legível em nenhum frame.**
9. O velamento é **propriedade do objeto**, não blur de câmera.
10. Só **três âncoras de fundo** em todos os keyframes: quadro da roda zodiacal, cruz na parede, borda da estante com ametista.
11. **Nenhum tom quente alaranjado ou amarelado.**
12. Mesa limpa no T1. **No K02 e K03 nenhum prop de gancho aparece.**
13. Mãos com cinco dedos, sem fusão com a carta nem com o prop.
14. Zero blur de câmera.
15. Nenhuma leitura de pacto. Carta em tons claros.
16. `222` na fala do T5 e do T6, e isolado na tela no CTA.
17. CTA promete o **rosto na DM**, sem citar quiz, teste, app, plano nem preço.
18. Follow gate do T7 presente **com o motivo**.

---

## ⚠️ Nota do PORTÃO P6 · o modelo é FILMAGEM REAL

O insight 3.1 do playbook diz que *"a fala já passou uma vez, não é o gatilho"* **só vale quando o vídeo modelo foi gerado por IA**. Este modelo é **filmagem real**, então a fala nunca passou por um gerador e pode travar.

**Se algum take travar:** o substituto vem **de dentro do próprio roteiro original**, nunca inventado, e aplicar `restricoes-protocolo` na ordem: enxugar a ação, neutralizar o alvo, separar em takes diferentes. O risco base aqui é baixo, não há nada anatômico.
