# Blake Epeterson | Ângulo 3 (Auraly) | Pacote de Prompts

Vídeo modelo: `snapinsta-1787622485916.mp4` (leitora de tarô, 47,5s, uma cena contínua)
Âncora do avatar: `producao/_ancoras/Man_sitting_at_table_4K_202608241610.jpeg`
Roteiro: `ROTEIRO.md` · Ganchos: `GANCHOS.md` · DM: `DM.md`

Funil: comentar `222` → DM → mensagem com o rosto → link
**Sem take de produto.** O prop herói é a **carta**, presente em todos os cinco ganchos.

## FORMATO: PLANO ÚNICO
Câmera na altura do peito, do outro lado da mesa. Blake do peito pra cima em cima, **mesa no terço inferior do MESMO quadro**, e **ele executa a ação com as próprias mãos enquanto fala**. Sem split screen, sem close isolado na mesa, sem B-roll separado.

## As 5 variações aprovadas

| Var | Gancho | Keyframe do T1 | Clipe do T1 |
|---|---|---|---|
| **A** | G-CARTAS · três viradas e uma revelada | K01A | V01A |
| **B** | N5 · envelope com lacre de cera | K01B | V01B |
| **C** | N11 · o ímã e a carta ⭐ | K01C | V01C |
| **D** | N14 · as letrinhas ao redor da carta | K01D | V01D |
| **E** | N15 · a borra de café ao lado da carta | K01E | V01E |

**O gancho vive só no T1.** Do T2 em diante o enquadramento fecha, a mesa sai de quadro e ele segura a carta. Por isso **K02, K03 e os clipes V02 a V07 são gerados uma vez só e servem às cinco**. Cada gancho custa **1 keyframe + 1 clipe**.

---

## Índice de geração

| Take | Keyframe | Ação de geração |
|---|---|---|
| REF-CARTA | REF | **GERAR e APROVAR ANTES DE TUDO** |
| REF-CARTA-2 (opcional) | REF | idem, arte `TWINFLAME`, para alternar entre variações |
| T1 | K01A a K01E | **GERAR DO ZERO**, um por variação · ÂNCORA BLAKE + REF-CARTA |
| T2 a T5 | K02 | **GERAR DO ZERO** (setup novo, enquadramento fechado) · ÂNCORA BLAKE + REF-CARTA |
| T6, T7 | K03 | **EDITAR do K02** |

---

## Trava de identidade e continuidade

Aplicar em toda imagem e todo clipe:

- Rosto do Blake da âncora: homem negro americano, pele marrom média com poros visíveis, olhos castanhos escuros, **barba curta e rala** com bigode mais cheio, **dreadlocks loiro-creme na altura dos ombros com raiz escura visível**, mechas na frente dos dois ombros.
- **Camiseta cinza** de gola careca com **patch pequeno da bandeira dos EUA no peito**, lado direito do quadro.
- **Corrente fina de PRATA com pingente de cruz de PRATA trabalhada.** Nunca ouro.
- Mesma sala, mas **em quadro só DUAS âncoras de fundo**: a **cruz de madeira na parede bege** e a **borda da estante com uma drusa de ametista roxa**. A **mesa de madeira clara** de tampo gasto ocupa o primeiro plano.
- **Todo o resto da sala fica FORA DE QUADRO por enquadramento**, nunca por blur. Sem janela, sem bandeira, sem potes, sem sofá.
- **Luz neutra de dia nublado**, difusa e levemente fria. **Nunca luz quente.**
- **Zero blur, tudo nítido.** Cara de vídeo de iPhone.

---

## Trava do prop herói · a CARTA (REF-CARTA)

**Gerar e aprovar ANTES de qualquer keyframe.** Aparece nos cinco ganchos e do T2 ao T7.

```json
{
  "shot_id": "REF_CARTA_soulmate",
  "subject": "A single tarot-style card lying flat on a plain light wooden table, photographed straight from above.",
  "card_art": "The card shows a warm illustration of a couple embracing, seen from the chest up, drawn in a soft storybook style with clean lines. The palette is light and inviting: cream, warm gold, soft pink and pale blue. A thin gold border frames the art. The word SOULMATE is printed in clean capital letters along the bottom of the card.",
  "card_object": "Standard tarot card size with slightly rounded corners, matte paper with a faint texture, resting flat and fully visible, no hand touching it.",
  "lighting": "Soft neutral daylight of an overcast day from the side, even and slightly cool, gentle shadow under the card edge. No warm orange cast.",
  "realism": "Real photograph of a real printed card, iPhone-footage look, visible paper grain and fibre, realistic shadow, no AI polish, sharp focus across the whole card, no blur.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no dark or gothic art, no black card, no deep purple card, no skulls, no hands, no plastic sheen, no blur, no warm orange color cast, no yellow tint, no golden glow"
}
```

### REF-CARTA-2 (opcional, arte `TWINFLAME`)
Mesmo prompt, trocando a palavra da base para `TWINFLAME` e a ilustração para **duas figuras espelhadas de perfil, quase se tocando**, na mesma paleta clara. Serve para alternar entre variações sem quebrar continuidade.

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
[x] 4. Âncora é plano médio relaxado. Override de postura e composição em todo prompt
[x] 5. Peito pra cima em todos os takes
[x] 6. Take mais fechado do vídeo é o CTA (K03)

FUNDO
[x] 7. Só DUAS âncoras de fundo: cruz na parede e borda da estante com uma ametista
[x] 8. Fundo reduzido por ENQUADRAMENTO, nunca por blur
[x] 9. Mesa limpa, só o objeto do gancho e a carta

2ª PESSOA
[x] 10. Não se aplica
```

## Gate de realismo

```
[x] 1. Herói ISOLADO. Duas âncoras de fundo, não seis
[x] 2. Câmera puxada pra perto. No T1 o herói enche os dois terços de baixo
[x] 3. Luz NEUTRA de dia nublado. Nenhum "warm and even"
[x] 4. Negative carrega: no warm orange color cast, no yellow tint, no golden glow
[x] 5. Fundo específico e nunca borrado
[x] 6. REF-CARTA gerado isolado e aprovado antes de tudo
[x] 7. Bloco de realismo padrão colado por inteiro em todo prompt
```

---

# Prompts de imagem · T1, um por variação

## K01C · VARIAÇÃO C · O ÍMÃ E A CARTA · GERAR DO ZERO · ÂNCORA BLAKE + REF-CARTA

O melhor gancho do lote. O anel de metal corre até quase encostar na carta e recua.

```json
{
  "shot_id": "K01C_hook_ima_carta",
  "reference_use": "Use the FIRST attached image ONLY for Blake's face, identity, hair, beard, wardrobe, silver cross and the room. Reproduce him as the SAME person. Do NOT copy the pose of the reference, he must be leaning forward and working with his hands on the table. Use the SECOND attached image ONLY to reproduce the tarot card art exactly.",
  "identity_main": "The EXACT man from the first reference image (Blake): Black American man, medium brown skin with real visible pores and natural asymmetry, dark brown eyes, short sparse beard with a fuller mustache and chin beard, long platinum-cream bleached dreadlocks to shoulder length with dark roots, strands falling in front of both shoulders.",
  "wardrobe": "Gray crew-neck cotton t-shirt, relaxed fit, small embroidered American flag patch on the chest on the right side of frame. Thin SILVER chain with an ornate SILVER cross pendant.",
  "scene": "SAME living room as the reference but with almost NOTHING else in frame: the light oak wooden table with its worn scratched top filling the lower part of the shot, and behind him only TWO readable anchors, the plain wooden cross on the beige wall and the edge of the wooden shelf with a single purple amethyst cluster on it. Every other object in the room is out of frame.",
  "action": "The tarot card from the second reference lies flat on the table facing up, fully readable. A small plain steel ring rests on the wood a short distance from the card, with a clear gap of bare table between them. His right hand is flat on the tabletop just beside the ring, holding a small black magnet against the wood. His left hand rests on the table.",
  "posture": "He sits at the table leaning slightly forward toward the camera, shoulders squared, head up and eyes looking straight into the lens while his hands work on the table below. He is speaking. NOT the relaxed seated slouch of the reference.",
  "composition": "Vertical shot from across the table, camera at chest height and PUSHED IN CLOSE. The card and the steel ring fill the lower two thirds of the frame and are clearly closer to the lens than his face. His face and shoulders sit in the upper third, cropped just above the hairline. Only the wall cross and a sliver of the shelf are visible behind him, small and secondary. ONE continuous shot, no split screen and no inset.",
  "camera": "chest level, straight-on, phone propped on the far edge of the table",
  "state": "Start frame: the ring is still apart from the card, nothing is moving yet.",
  "lighting": "Soft neutral daylight of an overcast day coming from a window out of frame. Even and slightly cool. No warm orange cast, no golden glow.",
  "realism": "UGC realism, real skin texture with visible pores, individual hair strands, subtle wrinkles, realistic shadows and reflections, iPhone-footage look, phone camera look not professional photography, no AI polish, no beauty smoothing, no blur anywhere, everything in sharp focus including background walls furniture and details.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no split screen, no inset frame, no studio lighting, no plastic skin, no extra fingers, no supernatural lighting, no glow effects, no blur, no gold jewelry, no second person, no dark or gothic styling, no seated slouch, no warm orange color cast, no yellow tint, no golden glow, no cluttered background"
}
```

## K01A · VARIAÇÃO A · TRÊS CARTAS VIRADAS · GERAR DO ZERO · ÂNCORA BLAKE + REF-CARTA

O mais fiel ao vídeo modelo, que tem cartas viradas na mesa o tempo inteiro.

```json
{
  "shot_id": "K01A_hook_tres_cartas",
  "reference_use": "Use the FIRST attached image ONLY for Blake's face, identity, hair, beard, wardrobe, silver cross and the room. Do NOT copy the pose, he must be leaning forward with his hands on the table. Use the SECOND attached image ONLY to reproduce the tarot card art exactly.",
  "identity_main": "The EXACT man from the first reference image (Blake): Black American man, medium brown skin with real visible pores, dark brown eyes, short sparse beard with a fuller mustache and chin beard, long platinum-cream bleached dreadlocks to shoulder length with dark roots.",
  "wardrobe": "Gray crew-neck cotton t-shirt with a small embroidered American flag patch on the chest. Thin SILVER chain with an ornate SILVER cross pendant.",
  "scene": "SAME living room as the reference but with almost NOTHING else in frame: the light oak wooden table with its worn scratched top filling the lower part of the shot, and behind him only TWO readable anchors, the plain wooden cross on the beige wall and the edge of the wooden shelf with a single purple amethyst cluster on it. Every other object in the room is out of frame.",
  "action": "Three tarot cards lie in a neat row on the table, all three face down, showing a plain cream card back with a thin gold border and no illustration. His right hand rests on the middle card with two fingertips, having just started to lift its near edge a few millimetres off the wood.",
  "posture": "He sits at the table leaning slightly forward toward the camera, shoulders squared, head up and eyes looking straight into the lens while his hand rests on the card below. He is speaking. NOT the relaxed seated slouch of the reference.",
  "composition": "Vertical shot from across the table, camera at chest height and PUSHED IN CLOSE. The three cards fill the lower two thirds of the frame and are clearly closer to the lens than his face. His face and shoulders sit in the upper third, cropped just above the hairline. Only the wall cross and a sliver of the shelf are visible behind him. ONE continuous shot, no split screen and no inset.",
  "camera": "chest level, straight-on, phone propped on the far edge of the table",
  "state": "Start frame: all three cards are still face down, the middle one barely lifted at one edge.",
  "lighting": "Soft neutral daylight of an overcast day coming from a window out of frame. Even and slightly cool. No warm orange cast, no golden glow.",
  "realism": "UGC realism, real skin texture with visible pores, individual hair strands, subtle wrinkles, realistic shadows and reflections, iPhone-footage look, phone camera look not professional photography, no AI polish, no beauty smoothing, no blur anywhere, everything in sharp focus including background walls furniture and details.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no visible card faces, no illustration on the card backs, no split screen, no inset frame, no studio lighting, no plastic skin, no extra fingers, no blur, no gold jewelry, no second person, no dark or gothic styling, no seated slouch, no warm orange color cast, no yellow tint, no golden glow, no cluttered background"
}
```

## K01B · VARIAÇÃO B · ENVELOPE COM LACRE · GERAR DO ZERO · ÂNCORA BLAKE

```json
{
  "shot_id": "K01B_hook_envelope_lacre",
  "reference_use": "Use the attached image ONLY for Blake's face, identity, hair, beard, wardrobe, silver cross and the room. Do NOT copy the pose, he must be leaning forward with the envelope in his hands over the table.",
  "identity_main": "The EXACT man from the reference image (Blake): Black American man, medium brown skin with real visible pores, dark brown eyes, short sparse beard with a fuller mustache and chin beard, long platinum-cream bleached dreadlocks to shoulder length with dark roots.",
  "wardrobe": "Gray crew-neck cotton t-shirt with a small embroidered American flag patch on the chest. Thin SILVER chain with an ornate SILVER cross pendant.",
  "scene": "SAME living room as the reference but with almost NOTHING else in frame: the light oak wooden table with its worn scratched top filling the lower part of the shot, and behind him only TWO readable anchors, the plain wooden cross on the beige wall and the edge of the wooden shelf with a single purple amethyst cluster on it. Every other object in the room is out of frame.",
  "action": "He holds a cream coloured paper envelope flat with both hands just above the tabletop, tilted toward the camera so the sealed flap is visible. The flap is closed with a round blob of deep red wax, smooth, glossy and unbroken. Both thumbs are pressed at the edges of the seal. The envelope looks slightly thick, as if a card is inside.",
  "posture": "He sits at the table leaning slightly forward toward the camera, shoulders squared, head up and eyes looking straight into the lens while his hands hold the envelope below. He is speaking. NOT the relaxed seated slouch of the reference.",
  "composition": "Vertical shot from across the table, camera at chest height and PUSHED IN CLOSE. The envelope and the wax seal fill the lower two thirds of the frame and are clearly closer to the lens than his face. His face and shoulders sit in the upper third, cropped just above the hairline. Only the wall cross and a sliver of the shelf are visible behind him. ONE continuous shot, no split screen and no inset.",
  "camera": "chest level, straight-on, phone propped on the far edge of the table",
  "state": "Start frame: the wax seal is still whole, thumbs in position.",
  "lighting": "Soft neutral daylight of an overcast day coming from a window out of frame. Even and slightly cool. No warm orange cast, no golden glow.",
  "realism": "UGC realism, real skin texture with visible pores, individual hair strands, subtle wrinkles, realistic shadows and reflections, iPhone-footage look, phone camera look not professional photography, no AI polish, no beauty smoothing, no blur anywhere, everything in sharp focus including background walls furniture and details.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no writing on the envelope, no split screen, no inset frame, no studio lighting, no plastic skin, no extra fingers, no blur, no gold jewelry, no second person, no dark or gothic styling, no seated slouch, no warm orange color cast, no yellow tint, no golden glow, no cluttered background"
}
```

## K01D · VARIAÇÃO D · LETRINHAS AO REDOR DA CARTA · GERAR DO ZERO · ÂNCORA BLAKE + REF-CARTA

```json
{
  "shot_id": "K01D_hook_letrinhas",
  "reference_use": "Use the FIRST attached image ONLY for Blake's face, identity, hair, beard, wardrobe, silver cross and the room. Do NOT copy the pose, he must be leaning forward with his hands on the table. Use the SECOND attached image ONLY to reproduce the tarot card art exactly.",
  "identity_main": "The EXACT man from the first reference image (Blake): Black American man, medium brown skin with real visible pores, dark brown eyes, short sparse beard with a fuller mustache and chin beard, long platinum-cream bleached dreadlocks to shoulder length with dark roots.",
  "wardrobe": "Gray crew-neck cotton t-shirt with a small embroidered American flag patch on the chest. Thin SILVER chain with an ornate SILVER cross pendant.",
  "scene": "SAME living room as the reference but with almost NOTHING else in frame: the light oak wooden table with its worn scratched top filling the lower part of the shot, and behind him only TWO readable anchors, the plain wooden cross on the beige wall and the edge of the wooden shelf with a single purple amethyst cluster on it. Every other object in the room is out of frame.",
  "action": "The tarot card from the second reference lies flat at the centre of the table, facing up and fully readable. Around it, about ten small square wooden game tiles are scattered, ALL of them lying blank side up so no letter is visible anywhere. His right index finger has slid one tile forward toward the camera and is tipping it up onto its edge, so the tile stands leaning with its face turned away from the lens and still unreadable.",
  "posture": "He sits at the table leaning slightly forward toward the camera, shoulders squared, head up and eyes looking straight into the lens while his finger works the tile below. He is speaking. NOT the relaxed seated slouch of the reference.",
  "composition": "Vertical shot from across the table, camera at chest height and PUSHED IN CLOSE. The card and the scattered tiles fill the lower two thirds of the frame and are clearly closer to the lens than his face. His face and shoulders sit in the upper third, cropped just above the hairline. Only the wall cross and a sliver of the shelf are visible behind him. ONE continuous shot, no split screen and no inset.",
  "camera": "chest level, straight-on, phone propped on the far edge of the table",
  "state": "Start frame: every tile blank side up, one tile tipped onto its edge with the face hidden.",
  "lighting": "Soft neutral daylight of an overcast day coming from a window out of frame. Even and slightly cool. No warm orange cast, no golden glow.",
  "realism": "UGC realism, real skin texture with visible pores, individual hair strands, subtle wrinkles, realistic shadows and reflections, iPhone-footage look, phone camera look not professional photography, no AI polish, no beauty smoothing, no blur anywhere, everything in sharp focus including background walls furniture and details.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no visible letters, no readable tile faces, no alphabet, no split screen, no inset frame, no studio lighting, no plastic skin, no extra fingers, no blur, no gold jewelry, no second person, no dark or gothic styling, no seated slouch, no warm orange color cast, no yellow tint, no golden glow, no cluttered background"
}
```

## K01E · VARIAÇÃO E · BORRA DE CAFÉ AO LADO DA CARTA · GERAR DO ZERO · ÂNCORA BLAKE + REF-CARTA

```json
{
  "shot_id": "K01E_hook_borra_cafe",
  "reference_use": "Use the FIRST attached image ONLY for Blake's face, identity, hair, beard, wardrobe, silver cross and the room. Do NOT copy the pose, he must be leaning forward with his hands on the table. Use the SECOND attached image ONLY to reproduce the tarot card art exactly.",
  "identity_main": "The EXACT man from the first reference image (Blake): Black American man, medium brown skin with real visible pores, dark brown eyes, short sparse beard with a fuller mustache and chin beard, long platinum-cream bleached dreadlocks to shoulder length with dark roots.",
  "wardrobe": "Gray crew-neck cotton t-shirt with a small embroidered American flag patch on the chest. Thin SILVER chain with an ornate SILVER cross pendant.",
  "scene": "SAME living room as the reference but with almost NOTHING else in frame: the light oak wooden table with its worn scratched top filling the lower part of the shot, and behind him only TWO readable anchors, the plain wooden cross on the beige wall and the edge of the wooden shelf with a single purple amethyst cluster on it. Every other object in the room is out of frame.",
  "action": "A plain white ceramic cup with dark wet coffee grounds pooled in the bottom sits on a matching white saucer. His right hand holds the cup by the rim, tilted and mid swirl, so the grounds are sliding around the inside wall. The tarot card from the second reference lies flat on the table right beside the saucer, facing up and fully readable.",
  "posture": "He sits at the table leaning slightly forward toward the camera, shoulders squared, head up and eyes looking straight into the lens while his hand swirls the cup below. He is speaking. NOT the relaxed seated slouch of the reference.",
  "composition": "Vertical shot from across the table, camera at chest height and PUSHED IN CLOSE. The cup, the saucer and the card fill the lower two thirds of the frame and are clearly closer to the lens than his face. His face and shoulders sit in the upper third, cropped just above the hairline. Only the wall cross and a sliver of the shelf are visible behind him. ONE continuous shot, no split screen and no inset.",
  "camera": "chest level, straight-on, phone propped on the far edge of the table",
  "state": "Start frame: the cup is tilted mid swirl, the grounds still inside.",
  "lighting": "Soft neutral daylight of an overcast day coming from a window out of frame. Even and slightly cool. No warm orange cast, no golden glow.",
  "realism": "UGC realism, real skin texture with visible pores, individual hair strands, subtle wrinkles, realistic shadows and reflections, iPhone-footage look, phone camera look not professional photography, no AI polish, no beauty smoothing, no blur anywhere, everything in sharp focus including background walls furniture and details.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no letters in the grounds, no split screen, no inset frame, no studio lighting, no plastic skin, no extra fingers, no blur, no gold jewelry, no second person, no dark or gothic styling, no seated slouch, no warm orange color cast, no yellow tint, no golden glow, no cluttered background"
}
```

---

# Prompts de imagem · T2 em diante (compartilhados)

## K02 · T2 A T5 · CARTA NA MÃO · GERAR DO ZERO · ÂNCORA BLAKE + REF-CARTA

O enquadramento fecha e a mesa sai de quadro. É isso que mantém o keyframe servindo às cinco variações.

```json
{
  "shot_id": "K02_carta_na_mao",
  "reference_use": "Use the FIRST attached image ONLY for Blake's face, identity, hair, beard, wardrobe, silver cross and the room. Do NOT copy the pose or the camera distance, this shot is much closer. Use the SECOND attached image ONLY to reproduce the tarot card art exactly.",
  "identity_main": "The EXACT man from the first reference image (Blake): Black American man, medium brown skin with real visible pores and natural asymmetry, dark brown eyes, short sparse beard with a fuller mustache and chin beard, long platinum-cream bleached dreadlocks to shoulder length with dark roots, strands falling in front of both shoulders.",
  "wardrobe": "Gray crew-neck cotton t-shirt with a small embroidered American flag patch on the chest on the right side of frame. Thin SILVER chain with an ornate SILVER cross pendant.",
  "scene": "SAME living room as the reference, tighter: only TWO anchors visible behind him, the plain wooden cross on the beige wall and the edge of the wooden shelf with a single purple amethyst cluster. Only a thin sliver of the tabletop shows at the very bottom edge. Everything else is out of frame.",
  "action": "His right hand holds the tarot card from the second reference raised beside his face at cheek height, pushed slightly toward the lens so the card is closer to the camera than his face. The card faces the camera and is fully readable. Reproduce the card art EXACTLY: the embracing couple illustration, the light cream and gold palette, the thin gold border and the word on the bottom edge. His left hand is out of frame.",
  "posture": "He sits upright facing the camera, mouth slightly open as if speaking, eyes on the lens. NOT the relaxed seated slouch of the reference.",
  "composition": "Vertical, CLOSE, chest up. Much tighter than the reference. His face fills the upper middle of the frame, cropped just above the hairline. The card sits beside his cheek, nearer the lens than his face. The table is essentially out of frame.",
  "camera": "chest level, straight-on, phone propped across from him",
  "state": "Neutral speaking frame with the card raised beside the face.",
  "lighting": "Soft neutral daylight of an overcast day coming from a window out of frame. Even and slightly cool. No warm orange cast, no golden glow.",
  "realism": "UGC realism, real skin texture with visible pores, individual hair strands, subtle wrinkles, realistic shadows and reflections, iPhone-footage look, phone camera look not professional photography, no AI polish, no beauty smoothing, no blur anywhere, everything in sharp focus including background walls furniture and details.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no split screen, no studio lighting, no plastic skin, no extra fingers, no supernatural lighting, no glow effects, no blur, no gold jewelry, no second person, no dark or gothic card, no seated slouch, no salt, no envelope, no coffee cup, no game tiles, no magnet, no warm orange color cast, no yellow tint, no golden glow, no cluttered background"
}
```

## K03 · T6 E T7 · CTA, MAIS FECHADO · EDITAR do K02

```json
{
  "task": "edit the attached image, keep everything identical except the changes listed",
  "keep_identical": "Keep Blake exactly the same: same face, same beard, same platinum dreadlocks, same gray t-shirt with the flag patch, same SILVER cross. Keep the SAME tarot card with the same art. Keep the SAME room, wall cross, shelf edge with the amethyst, and the same neutral overcast lighting.",
  "change_1": "Push the camera closer so the framing tightens by about twenty five percent. His face fills more of the frame, cropped at the top of his head and at the shoulders. Do not change the angle or the height of the camera.",
  "change_2": "The card is held a little higher, right beside his temple, still facing the camera and fully readable. Less of the room is visible because the framing is tighter.",
  "realism": "UGC realism, real skin texture with visible pores, iPhone-footage look, no AI polish, no beauty smoothing, no blur anywhere. Do not make his skin darker, yellowish or orangish. Do not make the colors more saturated.",
  "negative": "do not change the face, do not change the identity, do not redraw the card art, do not add background objects, no captions, no subtitles, no words overlaid on the image, no plastic skin, no extra fingers, no gold jewelry, no second person, no blur, no warm orange color cast, no yellow tint"
}
```

---

# Prompts de vídeo (Veo 3.1 via Flow)

## Bloco global

Colar em todo prompt:

```text
o avatar (homem) fala em inglês com sotaque americano de homem negro, voz autêntica, calma e convicta, como se estivesse lendo algo que só ele está vendo.

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

Estilo TikTok nativo, UGC. Preservar exatamente a identidade do Blake, rosto, dreadlocks loiro-platinados, barba, camiseta cinza, cruz de PRATA, a sala, a cruz na parede, a iluminação e o enquadramento do frame inicial. Plano único, sem split screen. Sem legenda, sem texto gerado, sem música, sem pessoas extras.
```

---

### V01C · T1 · VARIAÇÃO C · usa K01C

```text
o avatar (homem) fala em inglês com sotaque americano de homem negro, voz autêntica, calma e convicta, a seguinte frase: "There is someone who thinks you gave up on them. The cards just told me everything, including their initial."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ele desliza a mão sob a borda da mesa e o anel de metal corre sobre a madeira em direção à carta, para a dois dedos dela e volta atrás. Ele repete o movimento uma vez.

câmera: fixa, leve handheld natural

som ambiente: ambiente de sala de casa, som seco do metal deslizando na madeira, sem música
```

### V01A · T1 · VARIAÇÃO A · usa K01A

```text
o avatar (homem) fala em inglês com sotaque americano de homem negro, voz autêntica, calma e convicta, a seguinte frase: "There is someone who thinks you gave up on them. The cards just told me everything, including their initial."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ele vira a carta do meio sobre a mesa, e ela para deitada com a ilustração para cima. As outras duas continuam viradas para baixo.

câmera: fixa, leve handheld natural

som ambiente: ambiente de sala de casa, som seco de papel na madeira, sem música
```

### V01B · T1 · VARIAÇÃO B · usa K01B

```text
o avatar (homem) fala em inglês com sotaque americano de homem negro, voz autêntica, calma e convicta, a seguinte frase: "There is someone who thinks you gave up on them. The cards just told me everything, including their initial."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ele pressiona os polegares e o lacre de cera racha ao meio. A aba abre para trás e ele inclina o envelope, deixando a carta deslizar para fora até a metade.

câmera: fixa, leve handheld natural

som ambiente: ambiente de sala de casa, estalo seco da cera e papel deslizando, sem música
```

### V01D · T1 · VARIAÇÃO D · usa K01D

```text
o avatar (homem) fala em inglês com sotaque americano de homem negro, voz autêntica, calma e convicta, a seguinte frase: "There is someone who thinks you gave up on them. The cards just told me everything, including their initial."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ele empurra a peça de madeira mais para a frente com o indicador e a levanta até ficar em pé sobre a borda, com a face virada para longe da lente. A peça fica parada em pé.

câmera: fixa, leve handheld natural

som ambiente: ambiente de sala de casa, som seco de madeira na madeira, sem música
```

### V01E · T1 · VARIAÇÃO E · usa K01E

```text
o avatar (homem) fala em inglês com sotaque americano de homem negro, voz autêntica, calma e convicta, a seguinte frase: "There is someone who thinks you gave up on them. The cards just told me everything, including their initial."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ele gira a xícara em círculo e a vira de boca para baixo sobre o pires. Depois levanta a xícara devagar, deixando uma mancha escura irregular no branco do pires.

câmera: fixa, leve handheld natural

som ambiente: ambiente de sala de casa, som de louça, sem música
```

---

### V02 · T2 · usa K02

```text
o avatar (homem) fala em inglês com sotaque americano de homem negro, voz autêntica, calma e convicta, a seguinte frase: "This video did not find you by accident. I ask the universe to carry it to the right person."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ele mantém a carta erguida ao lado do rosto e olha direto na lente enquanto fala.

câmera: fixa, leve handheld natural

som ambiente: ambiente de sala de casa, sem música
```

### V03 · T3 · usa K02

```text
o avatar (homem) fala em inglês com sotaque americano de homem negro, voz autêntica, calma e convicta, a seguinte frase: "So comment 222 right now. That is you telling the universe you are ready to receive this."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ele aponta o indicador da mão livre para a lente ao dizer "comment 222" e depois recolhe a mão. A carta não se move.

câmera: fixa, leve handheld natural

som ambiente: ambiente de sala de casa, sem música
```

### V04 · T4 · usa K02

```text
o avatar (homem) fala em inglês com sotaque americano de homem negro, voz autêntica, calma e convicta, a seguinte frase: "This person watches you. They get close, then pull away. They have feelings they will not say out loud."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ele inclina a cabeça de leve ao dizer "pull away" e volta a olhar direto na lente. A carta continua parada ao lado do rosto.

câmera: fixa, leve handheld natural

som ambiente: ambiente de sala de casa, sem música
```

### V05 · T5 · usa K02

```text
o avatar (homem) fala em inglês com sotaque americano de homem negro, voz autêntica, calma e convicta, a seguinte frase: "They are not playing games. They are scared. And the cards say they are closer than you think."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ele balança a cabeça devagar em negativa ao dizer "not playing games" e depois assente uma vez.

câmera: fixa, leve handheld natural

som ambiente: ambiente de sala de casa, sem música
```

### V06 · T6 · usa K03

```text
o avatar (homem) fala em inglês com sotaque americano de homem negro, voz autêntica, calma e convicta, a seguinte frase: "Their initial is the same as your tenth contact on WhatsApp. Go look. I will wait."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ele para de falar depois de "I will wait" e continua olhando para a lente em silêncio por um instante, com a carta erguida ao lado do rosto.

câmera: fixa, leve push-in muito sutil

som ambiente: ambiente de sala de casa, sem música
```

### V07 · T7 · usa K03

```text
o avatar (homem) fala em inglês com sotaque americano de homem negro, voz autêntica, calma e convicta, a seguinte frase: "Now comment 222 and I send their face straight to your messages. Follow me first, or it will not reach you."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ele aponta para baixo ao dizer "comment 222" e depois para cima ao dizer "follow me first". Termina olhando parado na lente com a carta erguida.

câmera: fixa, leve push-in muito sutil

som ambiente: ambiente de sala de casa, sem música
```

---

## Mapa de âncoras

| Keyframe | Referências a anexar | Modelo |
|---|---|---|
| REF-CARTA | nenhuma, gerar do zero | Nano Banana **Pro**, regenerar até a arte ficar limpa |
| REF-CARTA-2 (opcional) | nenhuma, gerar do zero | Nano Banana **Pro** |
| K01B | **ÂNCORA BLAKE** | Nano Banana **Pro**, várias variações |
| K01A, K01C, K01D, K01E | **ÂNCORA BLAKE + REF-CARTA** | Nano Banana **Pro**, várias variações |
| K02 | **ÂNCORA BLAKE + REF-CARTA** | Nano Banana **Pro** |
| K03 | K02 aprovado | Nano Banana 2, edição |

---

## Montagem no CapCut

- Timeline 1080x1920, 30 fps. **Plano único o vídeo inteiro.**
- Cortes duros entre todos os takes. O único que pede peso é T1 para T2, que é a troca de setup.
- Cortar o silêncio inicial de cada clipe, **menos no V06**, onde a pausa depois de "I will wait" é intencional e é o que faz ela ir conferir o WhatsApp.
- **Gráfico fixo o vídeo inteiro:** `222` no topo à esquerda, do frame 0 ao fim.
- **Legendas karaokê**, uma linha por vez, palavra destacada em **amarelo**. **Nunca cobrir a mesa no T1 nem a carta nos demais takes.**
- **Caixa de gancho** no topo, vermelha com texto branco, igual ao modelo: `You Need To Know This!` nas variações A e C, `FOUND YOU ON` na D, `SITTING EXACTLY WHERE` na E, `SKIP THIS Y'ALL` na B.
- Manter `222` isolado e grande na tela durante o V03 e o V07.
- **Cartela final** depois do V07: foto de perfil em círculo com seta apontando pra ela.
- Color grading: temp -3, tint +2, saturação -6, exposição -3, contraste +12, highlight -35, shadow +18, fade +6.

---

## Gates de qualidade

1. **Plano único em todos os keyframes.** Nenhuma imagem com split screen, moldura interna ou inset.
2. **No T1 o Blake está em quadro executando a ação com as próprias mãos**, sem close isolado na mesa.
3. Blake é o mesmo homem em todos os clipes, com a **cruz de PRATA**.
4. Dreadlocks com mesmo comprimento e mesma raiz escura em todos os planos.
5. **A carta tem arte idêntica ao REF-CARTA** em K01A, K01C, K01D, K01E, K02 e K03.
6. **A carta está na mão dele do T2 ao T7**, sem sumir em nenhum take.
7. 🚫 **Nenhum rosto de alma gêmea em nenhum frame.**
8. 🚫 **Nenhuma letra visível no K01D.** As peças estão todas de face pra baixo e a que sobe fica virada pra longe da lente.
9. 🚫 **Nenhuma face de carta visível no K01A** antes da virada. Os versos são lisos, creme, sem ilustração.
10. Só **duas âncoras de fundo** em todos os keyframes: cruz na parede e borda da estante com a ametista.
11. **Nenhum tom quente alaranjado ou amarelado** em nenhum keyframe.
12. Mesa limpa no T1, só o objeto do gancho e a carta. **No K02 e no K03 nenhum prop de gancho aparece.**
13. Mãos com cinco dedos, sem fusão com a carta nem com o prop.
14. Zero blur de câmera.
15. Nenhuma leitura de pacto. Carta em tons claros.
16. `222` na fala do T3 e do T7, e isolado na tela no CTA.
17. O CTA promete o **rosto na DM** e não cita quiz, teste, app, plano nem preço.
18. Follow gate do T7 presente **com o motivo**.

---

## ⚠️ Nota do PORTÃO P6 · o modelo é FILMAGEM REAL

O insight 3.1 do playbook diz que *"a fala já passou uma vez, não é o gatilho"* **só vale quando o vídeo modelo foi gerado por IA**. Este modelo é **filmagem real** de uma leitora de tarô, então **a fala nunca passou por um gerador e pode travar**.

**Se algum take travar:** o substituto vem **de dentro do próprio roteiro original**, nunca inventado. E aplicar o protocolo de `restricoes-protocolo` na ordem: enxugar a ação, neutralizar o alvo, separar em takes diferentes.

**O que mais pode travar aqui, por ordem:**
1. Nada de anatômico ou gore neste roteiro, então o risco base é baixo.
2. `K01D` pela combinação de letras e adivinhação, que pode ser lida como jogo de azar. Se travar, gerar as peças isoladas como REF-PROP.
3. Nenhuma combinação de elementos sensíveis foi criada em nenhum prompt (insight 3.3).
