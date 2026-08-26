# Kendra Collins | Ângulo 3 (Auraly) | Pacote de Prompts

Vídeo modelo: `snapinsta-1787622485916.mp4` (biblioteca #18)
Âncora do avatar: `producao/_ancoras/KENDRA COLLINS .jpeg`
Roteiro: `ROTEIRO.md` · DM: `DM.md`

Funil: comentar `222` → DM → mensagem com o rosto → link
**Sem take de produto.** O prop herói é a **carta**, presente nos cinco ganchos.

## FORMATO: PLANO ÚNICO
Câmera na altura do peito, do outro lado da mesa. Kendra do peito pra cima em cima, **mesa no terço inferior do MESMO quadro**, e **ela executa a ação com as próprias mãos enquanto fala**. Sem split screen, sem close isolado na mesa, sem B-roll separado.

## As 5 variações (as mesmas do `blake_inicial`)

| Var | Gancho | Keyframe do T1 | Clipe do T1 |
|---|---|---|---|
| **A** | três cartas viradas e uma revelada | K01A | V01A |
| **B** | envelope com lacre de cera | K01B | V01B |
| **C** | o ímã e a carta ⭐ | K01C | V01C |
| **D** | as letrinhas ao redor da carta | K01D | V01D |
| **E** | a borra de café ao lado da carta | K01E | V01E |

**K02, K03 e os clipes V02 a V07 são gerados uma vez só e servem às cinco.** Cada gancho custa **1 keyframe + 1 clipe**.

> ⚠️ **O envelope (B) já roda em outros três pacotes.** Substituto pronto no `ROTEIRO.md`: o pêndulo sobre a carta.

---

## Índice de geração

| Take | Keyframe | Ação de geração |
|---|---|---|
| REF-CARTA | REF | **reaproveitar a aprovada**, é do ângulo e não do avatar |
| T1 | K01A a K01E | **GERAR DO ZERO**, um por variação · ÂNCORA KENDRA + REF-CARTA |
| T2 a T5 | K02 | **GERAR DO ZERO** (setup novo, enquadramento fechado) · ÂNCORA KENDRA + REF-CARTA |
| T6, T7 | K03 | **EDITAR do K02** |

> Se o `kendra_veu` já foi gerado, **K02 e K03 são os mesmos** e podem ser reaproveitados inteiros. Só os cinco K01 mudam.

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

**Reaproveitar a arte já aprovada.** A carta é do ângulo, não do avatar. Se precisar gerar, o prompt está em `producao/kendra_veu/PROMPTS_PRODUCAO.md`.

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

## K01C · VARIAÇÃO C · O ÍMÃ E A CARTA · GERAR DO ZERO · ÂNCORA KENDRA + REF-CARTA

```json
{
  "shot_id": "K01C_kendra_inicial_ima_carta",
  "reference_use": "Use the FIRST attached image ONLY for Kendra's face, identity, hair, glasses, wardrobe, silver cross and the room. Reproduce her as the SAME person. Do NOT copy the pose of the reference, she must be leaning slightly forward and working with her hands on the table. Use the SECOND attached image ONLY to reproduce the tarot card art exactly.",
  "identity_main": "The EXACT woman from the first reference image (Kendra): white American woman in her late twenties, fair skin with real visible pores, freckles across the nose and cheeks and small natural blemishes, pale blonde eyebrows, full lips, light eyes, a tiny hoop stud in one nostril. Very short platinum bleached buzzcut, closely cropped at the sides. Thick black rectangular glasses with slightly rounded corners.",
  "wardrobe": "White ribbed cotton tank top with an oatmeal linen shirt worn open over it, sleeves rolled to the elbow. Thin SILVER chain with a small ornate SILVER cross pendant. Thin silver rings.",
  "scene": "SAME room as the reference but with almost NOTHING else in frame: the light oak wooden table with its worn scratched top filling the lower part of the shot, and behind her only THREE readable anchors, one framed zodiac wheel print on the white wall, the plain wooden cross on the wall, and the edge of the wooden shelf with a single purple amethyst geode. Every other object in the room is out of frame.",
  "action": "The tarot card from the second reference lies flat on the table facing up, fully readable. A small plain steel ring rests on the wood a short distance from the card, with a clear gap of bare table between them. Her right hand is flat on the tabletop just beside the ring, holding a small black magnet against the wood. Her left hand rests on the table.",
  "posture": "She sits at the table leaning slightly forward toward the camera, shoulders squared, head up and eyes looking straight into the lens while her hands work on the table below. She is speaking.",
  "composition": "Vertical shot from across the table, camera at chest height and PUSHED IN CLOSE. The card and the steel ring fill the lower two thirds of the frame and are clearly closer to the lens than her face. Her face and shoulders sit in the upper third, cropped just above the top of her head. Only the framed print, the wall cross and a sliver of the shelf are visible behind her, small and secondary. ONE continuous shot, no split screen and no inset.",
  "camera": "chest level, straight-on, phone propped on the far edge of the table",
  "state": "Start frame: the ring is still apart from the card, nothing is moving yet.",
  "lighting": "Soft neutral daylight of an overcast day coming from a window out of frame. Even and slightly cool. No warm orange cast, no golden glow.",
  "realism": "UGC realism, real skin texture with visible pores, individual short hairs on the scalp, subtle wrinkles, realistic shadows and honest reflections on the glasses lenses, iPhone-footage look, phone camera look not professional photography, no AI polish, no beauty smoothing, no blur anywhere, everything in sharp focus including background walls furniture and details.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no split screen, no inset frame, no studio lighting, no plastic skin, no beauty filter, no extra fingers, no supernatural lighting, no glow effects, no blur, no gold jewelry, no second person, no dark or gothic styling, no warm orange color cast, no yellow tint, no golden glow, no cluttered background"
}
```

## K01A · VARIAÇÃO A · TRÊS CARTAS VIRADAS · GERAR DO ZERO · ÂNCORA KENDRA + REF-CARTA

```json
{
  "shot_id": "K01A_kendra_inicial_tres_cartas",
  "reference_use": "Use the FIRST attached image ONLY for Kendra's face, identity, hair, glasses, wardrobe, silver cross and the room. Do NOT copy the pose, she must be leaning slightly forward with her hands on the table. Use the SECOND attached image ONLY to reproduce the tarot card art exactly.",
  "identity_main": "The EXACT woman from the first reference image (Kendra): white American woman in her late twenties, fair skin with real visible pores, freckles across the nose and cheeks, pale blonde eyebrows, full lips, light eyes, a tiny hoop stud in one nostril. Very short platinum bleached buzzcut. Thick black rectangular glasses.",
  "wardrobe": "White ribbed cotton tank top with an oatmeal linen shirt worn open over it, sleeves rolled to the elbow. Thin SILVER chain with a small ornate SILVER cross pendant. Thin silver rings.",
  "scene": "SAME room as the reference but with almost NOTHING else in frame: the light oak wooden table filling the lower part of the shot, and behind her only THREE readable anchors, one framed zodiac wheel print on the white wall, the plain wooden cross on the wall, and the edge of the wooden shelf with a single purple amethyst geode. Every other object is out of frame.",
  "action": "Three tarot cards lie in a neat row on the table, all three face down, showing a plain cream card back with a thin gold border and no illustration. Her right hand rests on the middle card with two fingertips, having just started to lift its near edge a few millimetres off the wood.",
  "posture": "She sits at the table leaning slightly forward toward the camera, shoulders squared, head up and eyes looking straight into the lens while her hand rests on the card below. She is speaking.",
  "composition": "Vertical shot from across the table, camera at chest height and PUSHED IN CLOSE. The three cards fill the lower two thirds of the frame and are clearly closer to the lens than her face. Her face and shoulders sit in the upper third. Only the framed print, the wall cross and a sliver of the shelf are visible behind her. ONE continuous shot, no split screen and no inset.",
  "camera": "chest level, straight-on, phone propped on the far edge of the table",
  "state": "Start frame: all three cards are still face down, the middle one barely lifted at one edge.",
  "lighting": "Soft neutral daylight of an overcast day coming from a window out of frame. Even and slightly cool. No warm orange cast, no golden glow.",
  "realism": "UGC realism, real skin texture with visible pores, individual short hairs on the scalp, subtle wrinkles, realistic shadows and honest reflections on the glasses lenses, iPhone-footage look, phone camera look not professional photography, no AI polish, no beauty smoothing, no blur anywhere, everything in sharp focus including background walls furniture and details.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no visible card faces, no illustration on the card backs, no split screen, no inset frame, no studio lighting, no plastic skin, no beauty filter, no extra fingers, no blur, no gold jewelry, no second person, no dark or gothic styling, no warm orange color cast, no yellow tint, no golden glow, no cluttered background"
}
```

## K01B · VARIAÇÃO B · ENVELOPE COM LACRE · GERAR DO ZERO · ÂNCORA KENDRA

```json
{
  "shot_id": "K01B_kendra_inicial_envelope",
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

## K01D · VARIAÇÃO D · LETRINHAS AO REDOR DA CARTA · GERAR DO ZERO · ÂNCORA KENDRA + REF-CARTA

```json
{
  "shot_id": "K01D_kendra_inicial_letrinhas",
  "reference_use": "Use the FIRST attached image ONLY for Kendra's face, identity, hair, glasses, wardrobe, silver cross and the room. Do NOT copy the pose, she must be leaning slightly forward with her hands on the table. Use the SECOND attached image ONLY to reproduce the tarot card art exactly.",
  "identity_main": "The EXACT woman from the first reference image (Kendra): white American woman in her late twenties, fair skin with real visible pores, freckles across the nose and cheeks, pale blonde eyebrows, full lips, light eyes, a tiny hoop stud in one nostril. Very short platinum bleached buzzcut. Thick black rectangular glasses.",
  "wardrobe": "White ribbed cotton tank top with an oatmeal linen shirt worn open over it, sleeves rolled to the elbow. Thin SILVER chain with a small ornate SILVER cross pendant. Thin silver rings.",
  "scene": "SAME room as the reference but with almost NOTHING else in frame: the light oak wooden table filling the lower part of the shot, and behind her only THREE readable anchors, one framed zodiac wheel print on the white wall, the plain wooden cross on the wall, and the edge of the wooden shelf with a single purple amethyst geode. Every other object is out of frame.",
  "action": "The tarot card from the second reference lies flat at the centre of the table, facing up and fully readable. Around it, about ten small square wooden game tiles are scattered, ALL of them lying blank side up so no letter is visible anywhere. Her right index finger has slid one tile forward toward the camera and is tipping it up onto its edge, so the tile stands leaning with its face turned away from the lens and still unreadable.",
  "posture": "She sits at the table leaning slightly forward toward the camera, shoulders squared, head up and eyes looking straight into the lens while her finger works the tile below. She is speaking.",
  "composition": "Vertical shot from across the table, camera at chest height and PUSHED IN CLOSE. The card and the scattered tiles fill the lower two thirds of the frame and are clearly closer to the lens than her face. Her face and shoulders sit in the upper third. Only the framed print, the wall cross and a sliver of the shelf are visible behind her. ONE continuous shot, no split screen and no inset.",
  "camera": "chest level, straight-on, phone propped on the far edge of the table",
  "state": "Start frame: every tile blank side up, one tile tipped onto its edge with the face hidden.",
  "lighting": "Soft neutral daylight of an overcast day coming from a window out of frame. Even and slightly cool. No warm orange cast, no golden glow.",
  "realism": "UGC realism, real skin texture with visible pores, individual short hairs on the scalp, subtle wrinkles, realistic shadows and honest reflections on the glasses lenses, iPhone-footage look, phone camera look not professional photography, no AI polish, no beauty smoothing, no blur anywhere, everything in sharp focus including background walls furniture and details.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no visible letters, no readable tile faces, no alphabet, no split screen, no inset frame, no studio lighting, no plastic skin, no beauty filter, no extra fingers, no blur, no gold jewelry, no second person, no dark or gothic styling, no warm orange color cast, no yellow tint, no golden glow, no cluttered background"
}
```

## K01E · VARIAÇÃO E · BORRA DE CAFÉ AO LADO DA CARTA · GERAR DO ZERO · ÂNCORA KENDRA + REF-CARTA

```json
{
  "shot_id": "K01E_kendra_inicial_borra_cafe",
  "reference_use": "Use the FIRST attached image ONLY for Kendra's face, identity, hair, glasses, wardrobe, silver cross and the room. Do NOT copy the pose, she must be leaning slightly forward with her hands on the table. Use the SECOND attached image ONLY to reproduce the tarot card art exactly.",
  "identity_main": "The EXACT woman from the first reference image (Kendra): white American woman in her late twenties, fair skin with real visible pores, freckles across the nose and cheeks, pale blonde eyebrows, full lips, light eyes, a tiny hoop stud in one nostril. Very short platinum bleached buzzcut. Thick black rectangular glasses.",
  "wardrobe": "White ribbed cotton tank top with an oatmeal linen shirt worn open over it, sleeves rolled to the elbow. Thin SILVER chain with a small ornate SILVER cross pendant. Thin silver rings.",
  "scene": "SAME room as the reference but with almost NOTHING else in frame: the light oak wooden table filling the lower part of the shot, and behind her only THREE readable anchors, one framed zodiac wheel print on the white wall, the plain wooden cross on the wall, and the edge of the wooden shelf with a single purple amethyst geode. Every other object is out of frame.",
  "action": "A plain white ceramic cup with dark wet coffee grounds pooled in the bottom sits on a matching white saucer. Her right hand holds the cup by the rim, tilted and mid swirl, so the grounds are sliding around the inside wall. The tarot card from the second reference lies flat on the table right beside the saucer, facing up and fully readable.",
  "posture": "She sits at the table leaning slightly forward toward the camera, shoulders squared, head up and eyes looking straight into the lens while her hand swirls the cup below. She is speaking.",
  "composition": "Vertical shot from across the table, camera at chest height and PUSHED IN CLOSE. The cup, the saucer and the card fill the lower two thirds of the frame and are clearly closer to the lens than her face. Her face and shoulders sit in the upper third. Only the framed print, the wall cross and a sliver of the shelf are visible behind her. ONE continuous shot, no split screen and no inset.",
  "camera": "chest level, straight-on, phone propped on the far edge of the table",
  "state": "Start frame: the cup is tilted mid swirl, the grounds still inside.",
  "lighting": "Soft neutral daylight of an overcast day coming from a window out of frame. Even and slightly cool. No warm orange cast, no golden glow.",
  "realism": "UGC realism, real skin texture with visible pores, individual short hairs on the scalp, subtle wrinkles, realistic shadows and honest reflections on the glasses lenses, iPhone-footage look, phone camera look not professional photography, no AI polish, no beauty smoothing, no blur anywhere, everything in sharp focus including background walls furniture and details.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no letters in the grounds, no split screen, no inset frame, no studio lighting, no plastic skin, no beauty filter, no extra fingers, no blur, no gold jewelry, no second person, no dark or gothic styling, no warm orange color cast, no yellow tint, no golden glow, no cluttered background"
}
```

---

# Prompts de imagem · T2 em diante (compartilhados)

> Se o `kendra_veu` já foi gerado, **reaproveitar o K02 e o K03 aprovados de lá**. São exatamente o mesmo setup.

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
  "negative": "no captions, no subtitles, no words overlaid on the image, no split screen, no studio lighting, no plastic skin, no beauty filter, no extra fingers, no supernatural lighting, no glow effects, no blur, no gold jewelry, no second person, no dark or gothic card, no salt, no envelope, no coffee cup, no game tiles, no magnet, no warm orange color cast, no yellow tint, no golden glow, no cluttered background"
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
a avatar (mulher) fala em inglês com sotaque americano de mulher branca, voz autêntica, calma e direta, como se estivesse lendo algo que só ela está vendo.

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

Estilo TikTok nativo, UGC. Preservar exatamente a identidade da Kendra, rosto, sardas, buzzcut platinado, óculos pretos, regata branca com camisa de linho aveia, cruz de PRATA, o quarto com o quadro de astrologia e a cruz na parede, a iluminação e o enquadramento do frame inicial. Plano único, sem split screen. Sem legenda, sem texto gerado, sem música, sem pessoas extras.
```

---

### V01C · T1 · VARIAÇÃO C · usa K01C

```text
a avatar (mulher) fala em inglês com sotaque americano de mulher branca, voz autêntica, calma e direta, a seguinte frase: "There is someone who thinks you gave up on them. The cards just told me everything, including their initial."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ela desliza a mão sob a borda da mesa e o anel de metal corre sobre a madeira em direção à carta, para a dois dedos dela e volta atrás. Ela repete o movimento uma vez.

câmera: fixa, leve handheld natural

som ambiente: ambiente de quarto de casa, som seco do metal deslizando na madeira, sem música
```

### V01A · T1 · VARIAÇÃO A · usa K01A

```text
a avatar (mulher) fala em inglês com sotaque americano de mulher branca, voz autêntica, calma e direta, a seguinte frase: "There is someone who thinks you gave up on them. The cards just told me everything, including their initial."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ela vira a carta do meio sobre a mesa, e ela para deitada com a ilustração para cima. As outras duas continuam viradas para baixo.

câmera: fixa, leve handheld natural

som ambiente: ambiente de quarto de casa, som seco de papel na madeira, sem música
```

### V01B · T1 · VARIAÇÃO B · usa K01B

```text
a avatar (mulher) fala em inglês com sotaque americano de mulher branca, voz autêntica, calma e direta, a seguinte frase: "There is someone who thinks you gave up on them. The cards just told me everything, including their initial."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ela pressiona os polegares e o lacre de cera racha ao meio. A aba abre para trás e ela inclina o envelope, deixando a carta deslizar para fora até a metade.

câmera: fixa, leve handheld natural

som ambiente: ambiente de quarto de casa, estalo seco da cera e papel deslizando, sem música
```

### V01D · T1 · VARIAÇÃO D · usa K01D

```text
a avatar (mulher) fala em inglês com sotaque americano de mulher branca, voz autêntica, calma e direta, a seguinte frase: "There is someone who thinks you gave up on them. The cards just told me everything, including their initial."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ela empurra a peça de madeira mais para a frente com o indicador e a levanta até ficar em pé sobre a borda, com a face virada para longe da lente. A peça fica parada em pé.

câmera: fixa, leve handheld natural

som ambiente: ambiente de quarto de casa, som seco de madeira na madeira, sem música
```

### V01E · T1 · VARIAÇÃO E · usa K01E

```text
a avatar (mulher) fala em inglês com sotaque americano de mulher branca, voz autêntica, calma e direta, a seguinte frase: "There is someone who thinks you gave up on them. The cards just told me everything, including their initial."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ela gira a xícara em círculo e a vira de boca para baixo sobre o pires. Depois levanta a xícara devagar, deixando uma mancha escura irregular no branco do pires.

câmera: fixa, leve handheld natural

som ambiente: ambiente de quarto de casa, som de louça, sem música
```

---

### V02 · T2 · usa K02

```text
a avatar (mulher) fala em inglês com sotaque americano de mulher branca, voz autêntica, calma e direta, a seguinte frase: "This video did not find you by accident. I ask the universe to carry it to the right person."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ela mantém a carta erguida ao lado do rosto e olha direto na lente enquanto fala.

câmera: fixa, leve handheld natural

som ambiente: ambiente de quarto de casa, sem música
```

### V03 · T3 · usa K02

```text
a avatar (mulher) fala em inglês com sotaque americano de mulher branca, voz autêntica, calma e direta, a seguinte frase: "So comment 222 right now. That is you telling the universe you are ready to receive this."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ela aponta o indicador da mão livre para a lente ao dizer "comment 222" e depois recolhe a mão. A carta não se move.

câmera: fixa, leve handheld natural

som ambiente: ambiente de quarto de casa, sem música
```

### V04 · T4 · usa K02

```text
a avatar (mulher) fala em inglês com sotaque americano de mulher branca, voz autêntica, calma e direta, a seguinte frase: "This person watches you. They get close, then pull away. They have feelings they will not say out loud."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ela inclina a cabeça de leve ao dizer "pull away" e volta a olhar direto na lente. A carta continua parada ao lado do rosto.

câmera: fixa, leve handheld natural

som ambiente: ambiente de quarto de casa, sem música
```

### V05 · T5 · usa K02

```text
a avatar (mulher) fala em inglês com sotaque americano de mulher branca, voz autêntica, calma e direta, a seguinte frase: "They are not playing games. They are scared. And the cards say they are closer than you think."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ela balança a cabeça devagar em negativa ao dizer "not playing games" e depois assente uma vez.

câmera: fixa, leve handheld natural

som ambiente: ambiente de quarto de casa, sem música
```

### V06 · T6 · usa K03

```text
a avatar (mulher) fala em inglês com sotaque americano de mulher branca, voz autêntica, calma e direta, a seguinte frase: "Their initial is the same as your tenth contact on WhatsApp. Go look. I will wait."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ela para de falar depois de "I will wait" e continua olhando para a lente em silêncio por um instante, com a carta erguida ao lado do rosto.

câmera: fixa, leve push-in muito sutil

som ambiente: ambiente de quarto de casa, sem música
```

### V07 · T7 · usa K03

```text
a avatar (mulher) fala em inglês com sotaque americano de mulher branca, voz autêntica, calma e direta, a seguinte frase: "Now comment 222 and I send their face straight to your messages. Follow me first, or it will not reach you."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ela aponta para baixo ao dizer "comment 222" e depois para cima ao dizer "follow me first". Termina olhando parada na lente com a carta erguida.

câmera: fixa, leve push-in muito sutil

som ambiente: ambiente de quarto de casa, sem música
```

---

## Mapa de âncoras

| Keyframe | Referências a anexar | Modelo |
|---|---|---|
| REF-CARTA | reaproveitar a aprovada | Nano Banana **Pro** |
| K01B | **ÂNCORA KENDRA** | Nano Banana **Pro**, várias variações |
| K01A, K01C, K01D, K01E | **ÂNCORA KENDRA + REF-CARTA** | Nano Banana **Pro**, várias variações |
| K02 | **ÂNCORA KENDRA + REF-CARTA** (ou reaproveitar do `kendra_veu`) | Nano Banana **Pro** |
| K03 | K02 aprovado | Nano Banana 2, edição |

---

## Montagem no CapCut

- Timeline 1080x1920, 30 fps. **Plano único o vídeo inteiro.**
- Cortes duros entre todos os takes. O único que pede peso é T1 para T2.
- Cortar o silêncio inicial de cada clipe, **menos no V06**, onde a pausa depois de "I will wait" é intencional e é o que faz ela ir conferir o WhatsApp.
- **Gráfico fixo o vídeo inteiro:** `222` no topo à esquerda, do frame 0 ao fim.
- **Legendas karaokê**, uma linha por vez, palavra destacada em **amarelo**. **Nunca cobrir a mesa no T1 nem a carta nos demais takes.**
- **Caixa de gancho** no topo, vermelha com texto branco: `You Need To Know This!` nas variações A e C, `FOUND YOU ON` na D, `SITTING EXACTLY WHERE` na E, `SKIP THIS Y'ALL` na B.
- Manter `222` isolado e grande na tela durante o V03 e o V07.
- **Cartela final** depois do V07: foto de perfil em círculo com seta apontando pra ela.
- Color grading: temp -3, tint +2, saturação -6, exposição -3, contraste +12, highlight -35, shadow +18, fade +6.

---

## Gates de qualidade

1. **Plano único em todos os keyframes**, sem split screen, moldura ou inset.
2. **No T1 a Kendra está em quadro executando a ação com as próprias mãos.**
3. Mesma mulher em todos os clipes, com **óculos pretos, buzzcut platinado e cruz de PRATA**.
4. **Sardas no nariz e nas bochechas presentes em todos os planos.** É o traço que mais some em regeneração.
5. **Reflexo honesto nas lentes dos óculos**, sem lente apagada nem vidro invisível.
6. **A carta tem arte idêntica ao REF-CARTA** em K01A, K01C, K01D, K01E, K02 e K03.
7. **A carta está na mão dela do T2 ao T7**, sem sumir.
8. 🚫 **Nenhum rosto de alma gêmea em nenhum frame.**
9. 🚫 **Nenhuma letra visível no K01D.**
10. 🚫 **Nenhuma face de carta visível no K01A** antes da virada.
11. Só **três âncoras de fundo** em todos os keyframes.
12. **Nenhum tom quente alaranjado ou amarelado.**
13. Mesa limpa no T1. **No K02 e K03 nenhum prop de gancho aparece.**
14. Mãos com cinco dedos, sem fusão com a carta nem com o prop.
15. Zero blur de câmera.
16. Nenhuma leitura de pacto. Carta em tons claros.
17. `222` na fala do T3 e do T7, e isolado na tela no CTA.
18. CTA promete o **rosto na DM**, sem citar quiz, teste, app, plano nem preço.
19. Follow gate do T7 presente **com o motivo**.

---

## ⚠️ Nota do PORTÃO P6 · o modelo é FILMAGEM REAL

O insight 3.1 do playbook diz que *"a fala já passou uma vez, não é o gatilho"* **só vale quando o vídeo modelo foi gerado por IA**. Este modelo é **filmagem real** de uma leitora de tarô, então a fala nunca passou por um gerador e pode travar.

**Se algum take travar:** o substituto vem **de dentro do próprio roteiro original**, nunca inventado, e aplicar `restricoes-protocolo` na ordem: enxugar a ação, neutralizar o alvo, separar em takes diferentes.

**O mais provável de travar aqui é o `K01D`**, pela combinação de letras e adivinhação, que pode ser lida como jogo de azar. Se travar, gerar as peças isoladas como REF-PROP.
