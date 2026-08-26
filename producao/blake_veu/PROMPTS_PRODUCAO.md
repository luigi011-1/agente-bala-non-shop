# Blake Epeterson | Ângulo 3 (Auraly) | Pacote de Prompts

Vídeo modelo: `AQNw72u-N08pJ7ZDe6hq...mp4` (FB01 do swipe)
Âncora do avatar: `producao/_ancoras/Man_sitting_at_table_4K_202608241610.jpeg`
Roteiro: `ROTEIRO.md` · Ganchos: `GANCHOS.md` · DM: `DM.md`

Funil: comentar `222` → DM → mensagem com o rosto → link
**Sem take de produto.** O prop herói é a carta SOULMATE.

## FORMATO: PLANO ÚNICO, nunca split screen

Câmera na **altura do peito, do outro lado da mesa**. O Blake aparece do peito pra cima na parte de cima do quadro e **a mesa ocupa o terço inferior do MESMO quadro**. **Ele executa a ação do gancho com as próprias mãos enquanto fala**, olhando pra lente.
Sem close isolado na mesa, sem B-roll separado, sem composição de duas metades.

## As 5 variações aprovadas

| Var | Gancho | Keyframe do T1 | Clipe do T1 |
|---|---|---|---|
| **A** | véu puxado do retrato | K01A | V01A |
| **B** | polaroid revelando | K01B | V01B |
| **C** | fio vermelho do destino | K01C | V01C |
| **D** | círculo de sal com vela | K01D | V01D |
| **E** | envelope com lacre de cera | K01E | V01E |

**O gancho vive só no T1.** Do T2 em diante o enquadramento fecha, a mesa sai de quadro e ele segura a carta. Por isso **K02, K03 e os clipes V02 a V07 são gerados uma vez só e servem para as cinco variações**. Cada gancho novo custa **1 keyframe + 1 clipe**.

---

## Índice de geração

| Take | Keyframe | Ação de geração |
|---|---|---|
| REF-CARTA | REF | **GERAR e APROVAR ANTES DE TUDO** |
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
- **Todo o resto da sala fica FORA DE QUADRO por enquadramento**, nunca por blur. Sem janela, sem bandeira, sem potes, sem sofá, sem carpete. Inventário de fundo é o erro que mais estraga a geração.
- **Luz neutra de dia nublado**, difusa e levemente fria. **Nunca luz quente**, que é o que mais denuncia IA.
- **Zero blur, tudo nítido.** Cara de vídeo de iPhone.

---

## Trava do prop herói · a CARTA SOULMATE (REF-CARTA)

**Gerar e aprovar ANTES de qualquer keyframe.** É o objeto recorrente do ângulo inteiro.

```json
{
  "shot_id": "REF_CARTA_soulmate",
  "subject": "A single tarot-style card lying flat on a plain light wooden table, photographed straight from above.",
  "card_art": "The card shows a warm illustration of a couple embracing, seen from the chest up, drawn in a soft storybook style with clean lines. The palette is light and inviting: cream, warm gold, soft pink and pale blue. A thin gold border frames the art. The word SOULMATE is printed in clean capital letters along the bottom of the card.",
  "card_object": "Standard tarot card size with slightly rounded corners, matte paper with a faint texture, resting flat and fully visible, no hand touching it.",
  "lighting": "Soft neutral daylight of an overcast day from the side, even and slightly cool, gentle shadow under the card edge. No warm orange cast.",
  "realism": "Real photograph of a real printed card, iPhone-footage look, visible paper grain and fibre, realistic shadow, no AI polish, sharp focus across the whole card, no blur.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no dark or gothic art, no black card, no deep purple card, no skulls, no hands, no plastic sheen, no blur, no warm orange color cast, no yellow tint, no golden glow, no cluttered background"
}
```

---

## Trava da 2ª pessoa (REF-A)

**Não se aplica.** Vídeo solo. Negative de todos os prompts carrega `no second person`.

---

## Gate de composição visual (rodado ANTES dos prompts)

```
HERÓI
[x] 1. No T1 o herói é a AÇÃO na mesa, no lower foreground, mais perto da lente que o rosto
[x] 2. Do T2 em diante o herói é a CARTA na mão, também mais perto que o rosto
[x] 3. Volume e forma da carta travados no REF-CARTA

DISTÂNCIA
[x] 4. Âncora é plano médio relaxado. Override de postura e composição em todo prompt
[x] 5. Peito pra cima em todos os takes
[x] 6. Take mais fechado do vídeo é o CTA (K03)

FUNDO
[x] 7. Só DUAS âncoras de fundo: cruz na parede e borda da estante com uma ametista
[x] 8. Fundo reduzido por ENQUADRAMENTO, nunca por blur
[x] 9. Mesa limpa, só o objeto do gancho

2ª PESSOA
[x] 10. Não se aplica
```

## Gate de realismo (memória `realismo-anti-cara-de-ia`)

```
[x] 1. Herói ISOLADO. Duas âncoras de fundo, não seis
[x] 2. Câmera puxada pra perto. No T1 o herói enche os dois terços de baixo
[x] 3. Luz NEUTRA de dia nublado. Nenhum "warm and even"
[x] 4. Negative carrega: no warm orange color cast, no yellow tint, no golden glow
[x] 5. Fundo específico e nunca borrado
[x] 6. REF-CARTA gerado isolado e aprovado antes de tudo
[x] 7. Bloco de realismo padrão colado por inteiro em todo prompt
```

> **Regra-mãe:** a IA copia bem o que você mostra e inventa mal o que você só descreve.
> **Realismo é volume de regeneração, não prompt mágico.** Nano Banana 2 supera o ChatGPT em avatar.

---

# Prompts de imagem · T1, um por variação

Todos partem do mesmo bloco de cena e postura. **Muda só o que está na mesa e o que as mãos fazem.**

## K01D · VARIAÇÃO D · CÍRCULO DE SAL · GERAR DO ZERO · ÂNCORA BLAKE + REF-CARTA

A variação de referência, igual ao print. Ele derrama sal de um potinho fechando o anel ao redor da carta.

```json
{
  "shot_id": "K01D_hook_circulo_sal",
  "reference_use": "Use the FIRST attached image ONLY for Blake's face, identity, hair, beard, wardrobe, silver cross and the room. Reproduce him as the SAME person. Do NOT copy the pose of the reference, he must be leaning forward and working with his hands on the table. Use the SECOND attached image ONLY to reproduce the tarot card art exactly.",
  "identity_main": "The EXACT man from the first reference image (Blake): Black American man, medium brown skin with real visible pores and natural asymmetry, dark brown eyes, short sparse beard with a fuller mustache and chin beard, long platinum-cream bleached dreadlocks to shoulder length with dark roots, strands falling in front of both shoulders.",
  "wardrobe": "Gray crew-neck cotton t-shirt, relaxed fit, small embroidered American flag patch on the chest on the right side of frame. Thin SILVER chain with an ornate SILVER cross pendant.",
  "scene": "SAME living room as the reference but with almost NOTHING else in frame: the light oak wooden table with its worn scratched top filling the lower part of the shot, and behind him only TWO readable anchors, the plain wooden cross on the beige wall and the edge of the wooden shelf with a single purple amethyst cluster on it. Every other object in the room is out of frame.",
  "action": "Blake is pouring coarse white salt from a small clear glass jar held in his right hand, tilting it over the table. The salt has already formed a thick ring on the wood and only a small gap is still open on one side. The tarot card from the second reference lies flat at the centre of the ring, facing up and fully readable. His left hand is raised beside the jar in a small gesture.",
  "posture": "He sits at the table leaning slightly forward toward the camera, shoulders squared, head up and eyes looking straight into the lens while his hands work on the table below. He is speaking. NOT the relaxed seated slouch of the reference.",
  "composition": "Vertical shot from across the table, camera at chest height and PUSHED IN CLOSE. The action on the tabletop fills the lower two thirds of the frame and is clearly closer to the lens than his face. His face and shoulders sit in the upper third, cropped just above the hairline. Only the wall cross and a sliver of the shelf are visible behind him, small and secondary. ONE continuous shot, no split screen and no inset.",
  "camera": "chest level, straight-on, phone propped on the far edge of the table",
  "state": "Start frame: the ring still has a visible gap, the jar is tilted and salt is falling.",
  "lighting": "Soft neutral daylight of an overcast day coming from a window out of frame. Even and slightly cool. No warm orange cast, no golden glow.",
  "realism": "UGC realism, real skin texture with visible pores, individual hair strands, subtle wrinkles, realistic shadows and reflections, iPhone-footage look, phone camera look not professional photography, no AI polish, no beauty smoothing, no blur anywhere, everything in sharp focus including background walls furniture and details.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no split screen, no inset frame, no studio lighting, no plastic skin, no extra fingers, no supernatural lighting, no glow effects, no blur, no gold jewelry, no second person, no dark or gothic styling, no seated slouch, no warm orange color cast, no yellow tint, no golden glow, no cluttered background"
}
```

## K01A · VARIAÇÃO A · VÉU PUXADO DO RETRATO · GERAR DO ZERO · ÂNCORA BLAKE

Mesmo enquadramento. Muda o que está na mesa e o que as mãos fazem.

```json
{
  "shot_id": "K01A_hook_veu_retrato",
  "reference_use": "Use the attached image ONLY for Blake's face, identity, hair, beard, wardrobe, silver cross and the room. Reproduce him as the SAME person. Do NOT copy the pose, he must be leaning forward and working with his hands on the table.",
  "identity_main": "The EXACT man from the reference image (Blake): Black American man, medium brown skin with real visible pores, dark brown eyes, short sparse beard with a fuller mustache and chin beard, long platinum-cream bleached dreadlocks to shoulder length with dark roots.",
  "wardrobe": "Gray crew-neck cotton t-shirt with a small embroidered American flag patch on the chest. Thin SILVER chain with an ornate SILVER cross pendant.",
  "scene": "SAME living room as the reference but with almost NOTHING else in frame: the light oak wooden table with its worn scratched top filling the lower part of the shot, and behind him only TWO readable anchors, the plain wooden cross on the beige wall and the edge of the wooden shelf with a single purple amethyst cluster on it. Every other object in the room is out of frame.",
  "action": "A small dark wooden picture frame lies flat on the table in front of him, still mostly covered by a loose piece of pale natural linen cloth. His right hand has taken hold of one corner of the cloth and has begun to lift it, so a sliver of the frame is uncovered. Under the cloth is a printed photograph of a man from the chest up, and THE PRINTED PHOTOGRAPH ITSELF IS OUT OF FOCUS, so the face is a soft unreadable smudge on the paper. The frame, the glass and the cloth are perfectly sharp.",
  "posture": "He sits leaning slightly forward toward the camera, shoulders squared, head up and eyes looking straight into the lens while his hands work on the table below. He is speaking.",
  "composition": "Vertical shot from across the table, camera at chest height and PUSHED IN CLOSE. The action on the tabletop fills the lower two thirds of the frame and is clearly closer to the lens than his face. His face and shoulders sit in the upper third, cropped just above the hairline. Only the wall cross and a sliver of the shelf are visible behind him, small and secondary. ONE continuous shot, no split screen and no inset.",
  "camera": "chest level, straight-on, phone propped on the far edge of the table",
  "state": "Start frame: the cloth still covers most of the frame, his hand is gripping the corner.",
  "lighting": "Soft neutral daylight of an overcast day coming from a window out of frame. Even and slightly cool. No warm orange cast, no golden glow.",
  "realism": "UGC realism, real skin texture with visible pores, individual hair strands, subtle wrinkles, realistic shadows and reflections, iPhone-footage look, phone camera look not professional photography, no AI polish, no beauty smoothing, no blur anywhere, everything in sharp focus including background walls furniture and details.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no readable face, no sharp portrait, no split screen, no inset frame, no studio lighting, no plastic skin, no extra fingers, no glow effects, no camera blur, no gold jewelry, no second person, no dark or gothic styling, no seated slouch, no warm orange color cast, no yellow tint, no golden glow, no cluttered background"
}
```

## K01B · VARIAÇÃO B · POLAROID REVELANDO · GERAR DO ZERO · ÂNCORA BLAKE

```json
{
  "shot_id": "K01B_hook_polaroid",
  "reference_use": "Use the attached image ONLY for Blake's face, identity, hair, beard, wardrobe, silver cross and the room. Reproduce him as the SAME person. Do NOT copy the pose, he must be leaning forward with his hands on the table.",
  "identity_main": "The EXACT man from the reference image (Blake): Black American man, medium brown skin with real visible pores, dark brown eyes, short sparse beard with a fuller mustache and chin beard, long platinum-cream bleached dreadlocks to shoulder length with dark roots.",
  "wardrobe": "Gray crew-neck cotton t-shirt with a small embroidered American flag patch on the chest. Thin SILVER chain with an ornate SILVER cross pendant.",
  "scene": "SAME living room as the reference but with almost NOTHING else in frame: the light oak wooden table with its worn scratched top filling the lower part of the shot, and behind him only TWO readable anchors, the plain wooden cross on the beige wall and the edge of the wooden shelf with a single purple amethyst cluster on it. Every other object in the room is out of frame.",
  "action": "A single instant photo with the classic white border lies on the table in front of him, held flat under his fingertips. The image inside is only HALF DEVELOPED: the background and the outline of a man's head and shoulders have come through in pale grey, but the face area is still an unresolved flat grey patch with no features at all. The white border and the table are perfectly sharp.",
  "posture": "He sits leaning slightly forward toward the camera, shoulders squared, head up and eyes looking straight into the lens while his fingers rest on the photo below. He is speaking.",
  "composition": "Vertical shot from across the table, camera at chest height and PUSHED IN CLOSE. The action on the tabletop fills the lower two thirds of the frame and is clearly closer to the lens than his face. His face and shoulders sit in the upper third, cropped just above the hairline. Only the wall cross and a sliver of the shelf are visible behind him, small and secondary. ONE continuous shot, no split screen and no inset.",
  "camera": "chest level, straight-on, phone propped on the far edge of the table",
  "state": "Start frame: the photo is mid development, the face still blank grey.",
  "lighting": "Soft neutral daylight of an overcast day coming from a window out of frame. Even and slightly cool. No warm orange cast, no golden glow.",
  "realism": "UGC realism, real skin texture with visible pores, individual hair strands, subtle wrinkles, realistic shadows and reflections, iPhone-footage look, phone camera look not professional photography, no AI polish, no beauty smoothing, no blur anywhere, everything in sharp focus including background walls furniture and details.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no readable face, no facial features, no finished photograph, no split screen, no inset frame, no studio lighting, no plastic skin, no extra fingers, no camera blur, no gold jewelry, no second person, no dark or gothic styling, no seated slouch, no warm orange color cast, no yellow tint, no golden glow, no cluttered background"
}
```

## K01C · VARIAÇÃO C · FIO VERMELHO DO DESTINO · GERAR DO ZERO · ÂNCORA BLAKE + REF-CARTA

```json
{
  "shot_id": "K01C_hook_fio_vermelho",
  "reference_use": "Use the FIRST attached image ONLY for Blake's face, identity, hair, beard, wardrobe, silver cross and the room. Do NOT copy the pose, he must be leaning forward with his hands on the table. Use the SECOND attached image ONLY to reproduce the tarot card art exactly.",
  "identity_main": "The EXACT man from the first reference image (Blake): Black American man, medium brown skin with real visible pores, dark brown eyes, short sparse beard with a fuller mustache and chin beard, long platinum-cream bleached dreadlocks to shoulder length with dark roots.",
  "wardrobe": "Gray crew-neck cotton t-shirt with a small embroidered American flag patch on the chest. Thin SILVER chain with an ornate SILVER cross pendant.",
  "scene": "SAME living room as the reference but with almost NOTHING else in frame: the light oak wooden table with its worn scratched top filling the lower part of the shot, and behind him only TWO readable anchors, the plain wooden cross on the beige wall and the edge of the wooden shelf with a single purple amethyst cluster on it. Every other object in the room is out of frame.",
  "action": "Two plain gold wedding bands sit apart on the table, one to his left and one to his right. A single red cotton thread is tied to each ring and lies loose and wavy across the wood with plenty of slack. Each of his hands holds one end of the thread just behind the rings, and he has started to draw them apart. The tarot card from the second reference lies flat between the two rings, facing up and fully readable.",
  "posture": "He sits leaning slightly forward toward the camera, shoulders squared, head up and eyes looking straight into the lens while his hands work the thread below. He is speaking.",
  "composition": "Vertical shot from across the table, camera at chest height and PUSHED IN CLOSE. The action on the tabletop fills the lower two thirds of the frame and is clearly closer to the lens than his face. His face and shoulders sit in the upper third, cropped just above the hairline. Only the wall cross and a sliver of the shelf are visible behind him, small and secondary. ONE continuous shot, no split screen and no inset.",
  "camera": "chest level, straight-on, phone propped on the far edge of the table",
  "state": "Start frame: the thread is still slack and wavy.",
  "lighting": "Soft neutral daylight of an overcast day coming from a window out of frame. Even and slightly cool. No warm orange cast, no golden glow.",
  "realism": "UGC realism, real skin texture with visible pores, individual hair strands, subtle wrinkles, realistic shadows and reflections, iPhone-footage look, phone camera look not professional photography, no AI polish, no beauty smoothing, no blur anywhere, everything in sharp focus including background walls furniture and details.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no split screen, no inset frame, no studio lighting, no plastic skin, no extra fingers, no glow effects, no camera blur, no gold jewelry on his body, no second person, no dark or gothic styling, no seated slouch, no warm orange color cast, no yellow tint, no golden glow, no cluttered background"
}
```

## K01E · VARIAÇÃO E · ENVELOPE COM LACRE DE CERA · GERAR DO ZERO · ÂNCORA BLAKE

```json
{
  "shot_id": "K01E_hook_envelope_lacre",
  "reference_use": "Use the attached image ONLY for Blake's face, identity, hair, beard, wardrobe, silver cross and the room. Reproduce him as the SAME person. Do NOT copy the pose, he must be leaning forward with the envelope in his hands over the table.",
  "identity_main": "The EXACT man from the reference image (Blake): Black American man, medium brown skin with real visible pores, dark brown eyes, short sparse beard with a fuller mustache and chin beard, long platinum-cream bleached dreadlocks to shoulder length with dark roots.",
  "wardrobe": "Gray crew-neck cotton t-shirt with a small embroidered American flag patch on the chest. Thin SILVER chain with an ornate SILVER cross pendant.",
  "scene": "SAME living room as the reference but with almost NOTHING else in frame: the light oak wooden table with its worn scratched top filling the lower part of the shot, and behind him only TWO readable anchors, the plain wooden cross on the beige wall and the edge of the wooden shelf with a single purple amethyst cluster on it. Every other object in the room is out of frame.",
  "action": "He holds a cream coloured paper envelope flat with both hands just above the tabletop, tilted toward the camera so the sealed flap is visible. The flap is closed with a round blob of deep red wax, smooth, glossy and unbroken. Both thumbs are pressed at the edges of the seal, about to break it. The envelope looks slightly thick, as if something firm is inside.",
  "posture": "He sits leaning slightly forward toward the camera, shoulders squared, head up and eyes looking straight into the lens while his hands hold the envelope below. He is speaking.",
  "composition": "Vertical shot from across the table, camera at chest height and PUSHED IN CLOSE. The action on the tabletop fills the lower two thirds of the frame and is clearly closer to the lens than his face. His face and shoulders sit in the upper third, cropped just above the hairline. Only the wall cross and a sliver of the shelf are visible behind him, small and secondary. ONE continuous shot, no split screen and no inset.",
  "camera": "chest level, straight-on, phone propped on the far edge of the table",
  "state": "Start frame: the wax seal is still whole, thumbs in position.",
  "lighting": "Soft neutral daylight of an overcast day coming from a window out of frame. Even and slightly cool. No warm orange cast, no golden glow.",
  "realism": "UGC realism, real skin texture with visible pores, individual hair strands, subtle wrinkles, realistic shadows and reflections, iPhone-footage look, phone camera look not professional photography, no AI polish, no beauty smoothing, no blur anywhere, everything in sharp focus including background walls furniture and details.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no writing on the envelope, no split screen, no inset frame, no studio lighting, no plastic skin, no extra fingers, no camera blur, no gold jewelry, no second person, no dark or gothic styling, no seated slouch, no warm orange color cast, no yellow tint, no golden glow, no cluttered background"
}
```

---

# Prompts de imagem · T2 em diante (compartilhados pelas 5 variações)

## K02 · T2 A T5 · BLAKE COM A CARTA · GERAR DO ZERO · ÂNCORA BLAKE + REF-CARTA

Setup novo: o enquadramento **fecha**, a mesa sai quase toda de quadro e ele ergue a carta. É isso que mantém este keyframe reaproveitável entre as cinco variações.

```json
{
  "shot_id": "K02_carta_na_mao",
  "reference_use": "Use the FIRST attached image ONLY for Blake's face, identity, hair, beard, wardrobe, silver cross and the room. Do NOT copy the pose or the camera distance, this shot is much closer. Use the SECOND attached image ONLY to reproduce the tarot card art exactly.",
  "identity_main": "The EXACT man from the first reference image (Blake): Black American man, medium brown skin with real visible pores and natural asymmetry, dark brown eyes, short sparse beard with a fuller mustache and chin beard, long platinum-cream bleached dreadlocks to shoulder length with dark roots, strands falling in front of both shoulders.",
  "wardrobe": "Gray crew-neck cotton t-shirt with a small embroidered American flag patch on the chest on the right side of frame. Thin SILVER chain with an ornate SILVER cross pendant.",
  "scene": "SAME living room as the reference, but tighter: the shelf with glass jars, amethyst clusters and spirituality books on the right, the small American flag, the plain wooden cross on the beige wall, and daylight from the window on the left. Only a thin sliver of the tabletop shows at the very bottom edge.",
  "action": "His right hand holds the tarot card from the second reference raised in front of his chest, pushed slightly toward the lens so the card is closer to the camera than his face. The card faces the camera and is fully readable. Reproduce the card art EXACTLY: the embracing couple illustration, the light cream and gold palette, the thin gold border and the word on the bottom edge. His left hand is out of frame or resting low.",
  "posture": "He sits upright facing the camera, mouth slightly open as if speaking, eyes on the lens. NOT the relaxed seated slouch of the reference.",
  "composition": "Vertical, CLOSE, chest up. Much tighter than the reference. His face fills the upper middle of the frame, cropped just above the hairline. The card sits in the lower foreground, nearer the lens than his face. The table is essentially out of frame.",
  "camera": "chest level, straight-on, phone propped across from him",
  "state": "Neutral speaking frame with the card raised.",
  "lighting": "Soft neutral daylight of an overcast day coming from a window out of frame. Even and slightly cool. No warm orange cast, no golden glow.",
  "realism": "UGC realism, real skin texture with visible pores, individual hair strands, subtle wrinkles, realistic shadows and reflections, iPhone-footage look, phone camera look not professional photography, no AI polish, no beauty smoothing, no blur anywhere, everything in sharp focus including background walls furniture and details.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no split screen, no studio lighting, no plastic skin, no extra fingers, no supernatural lighting, no glow effects, no blur, no gold jewelry, no second person, no dark or gothic card, no seated slouch, no salt, no envelope, no picture frame, no thread, no warm orange color cast, no yellow tint, no golden glow, no cluttered background"
}
```

## K03 · T6 E T7 · CTA, MAIS FECHADO · EDITAR do K02

```json
{
  "task": "edit the attached image, keep everything identical except the changes listed",
  "keep_identical": "Keep Blake exactly the same: same face, same beard, same platinum dreadlocks, same gray t-shirt with the flag patch, same SILVER cross. Keep the SAME tarot card with the same art. Keep the SAME room, shelf, flag, wall cross and lighting.",
  "change_1": "Push the camera closer so the framing tightens by about twenty five percent. His face fills more of the frame, cropped at the top of his head and at the shoulders. Do not change the angle or the height of the camera.",
  "change_2": "The card is now held higher, right beside his face, still facing the camera and fully readable. Less of the room is visible because the framing is tighter.",
  "realism": "UGC realism, real skin texture with visible pores, individual hair strands, subtle wrinkles, realistic shadows and reflections, iPhone-footage look, phone camera look not professional photography, no AI polish, no beauty smoothing, no blur anywhere, everything in sharp focus including background walls furniture and details.",
  "negative": "do not change the face, do not change the identity, do not redraw the card art, do not add background objects, no captions, no subtitles, no words overlaid on the image, no plastic skin, no extra fingers, no gold jewelry, no second person, no blur, no warm orange color cast, no yellow tint, no golden glow, no cluttered background"
}
```

---

# Prompts de vídeo (Veo 3.1 via Flow)

## Bloco global

Colar em todo prompt:

```text
o avatar (homem) fala em inglês com sotaque americano de homem negro, voz autêntica, calma e convicta, como se estivesse contando algo que acabou de ver.

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

Estilo TikTok nativo, UGC. Preservar exatamente a identidade do Blake, rosto, dreadlocks loiro-platinados, barba, camiseta cinza, cruz de PRATA, a sala com a estante, a bandeira e a cruz na parede, a iluminação e o enquadramento do frame inicial. Plano único, sem split screen. Sem legenda, sem texto gerado, sem música, sem pessoas extras.
```

---

### V01D · T1 · VARIAÇÃO D · usa K01D

```text
o avatar (homem) fala em inglês com sotaque americano de homem negro, voz autêntica, calma e convicta, a seguinte frase: "Before you scroll. Almost everyone scrolls past this. The ones who stay always come back saying the same thing."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: enquanto fala olhando na lente, ele inclina o potinho de vidro e derrama o sal que falta, fechando o círculo por inteiro ao redor da carta. Depois apoia o potinho na mesa.

câmera: fixa, leve handheld natural

som ambiente: ambiente de sala de casa, som seco de grãos caindo na madeira, sem música
```

### V01A · T1 · VARIAÇÃO A · usa K01A

```text
o avatar (homem) fala em inglês com sotaque americano de homem negro, voz autêntica, calma e convicta, a seguinte frase: "Before you scroll. Almost everyone scrolls past this. The ones who stay always come back saying the same thing."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: enquanto fala olhando na lente, ele puxa o pano de linho devagar para o lado, descobrindo o retrato por completo. O rosto impresso na foto continua sendo uma mancha suave e ilegível. Ele solta o pano fora de quadro.

câmera: fixa, leve handheld natural

som ambiente: ambiente de sala de casa, som suave de tecido deslizando, sem música
```

### V01B · T1 · VARIAÇÃO B · usa K01B

```text
o avatar (homem) fala em inglês com sotaque americano de homem negro, voz autêntica, calma e convicta, a seguinte frase: "Before you scroll. Almost everyone scrolls past this. The ones who stay always come back saying the same thing."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: enquanto fala olhando na lente, ele desliza a foto instantânea um pouco para a frente na mesa com os dedos. Na foto o fundo e o contorno dos ombros vão aparecendo devagar, e a área do rosto continua uma mancha cinza lisa que não se resolve.

câmera: fixa, leve handheld natural

som ambiente: ambiente de sala de casa, sem música
```

### V01C · T1 · VARIAÇÃO C · usa K01C

```text
o avatar (homem) fala em inglês com sotaque americano de homem negro, voz autêntica, calma e convicta, a seguinte frase: "Before you scroll. Almost everyone scrolls past this. The ones who stay always come back saying the same thing."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: enquanto fala olhando na lente, ele afasta as duas mãos e o fio vermelho vai perdendo a folga até esticar reto entre as alianças. Com o fio tenso, as duas alianças deslizam uma na direção da outra sobre a madeira até encostarem.

câmera: fixa, leve handheld natural

som ambiente: ambiente de sala de casa, tilintar curto de metal no fim, sem música
```

### V01E · T1 · VARIAÇÃO E · usa K01E

```text
o avatar (homem) fala em inglês com sotaque americano de homem negro, voz autêntica, calma e convicta, a seguinte frase: "Before you scroll. Almost everyone scrolls past this. The ones who stay always come back saying the same thing."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: enquanto fala olhando na lente, ele pressiona os polegares e o lacre de cera vermelha racha ao meio. A aba do envelope abre para trás e ele inclina o envelope, deixando uma carta de tarô deslizar para fora até a metade.

câmera: fixa, leve handheld natural

som ambiente: ambiente de sala de casa, estalo seco da cera e papel deslizando, sem música
```

---

### V02 · T2 · usa K02

```text
o avatar (homem) fala em inglês com sotaque americano de homem negro, voz autêntica, calma e convicta, a seguinte frase: "Something was covering this, and it just lifted. There is a face the universe has been holding for you."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ele ergue a carta alguns centímetros ao dizer que algo se levantou, e volta a baixar. Mantém o olhar na lente.

câmera: fixa, leve handheld natural

som ambiente: ambiente de sala de casa, sem música
```

### V03 · T3 · usa K02

```text
o avatar (homem) fala em inglês com sotaque americano de homem negro, voz autêntica, calma e convicta, a seguinte frase: "Not hidden from you. Held for you, until you were ready. And today you were the one who stopped."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ele balança a cabeça devagar em negativa ao dizer "not hidden", e depois assente uma vez. A carta continua firme na mão.

câmera: fixa, leve handheld natural

som ambiente: ambiente de sala de casa, sem música
```

### V04 · T4 · usa K02

```text
o avatar (homem) fala em inglês com sotaque americano de homem negro, voz autêntica, calma e convicta, a seguinte frase: "It is open right now, and it stays open one day. After that it closes and goes quiet again."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ele levanta o dedo indicador da mão livre ao dizer "one day", e depois recolhe a mão. A carta não se move.

câmera: fixa, leve handheld natural

som ambiente: ambiente de sala de casa, sem música
```

### V05 · T5 · usa K02

```text
o avatar (homem) fala em inglês com sotaque americano de homem negro, voz autêntica, calma e convicta, a seguinte frase: "Comment 222 below so the universe knows you are claiming it. Then send this video to yourself and save it."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ele aponta para baixo com a mão livre ao dizer "below" e depois abre a palma na direção da lente. A carta continua erguida na outra mão.

câmera: fixa, leve handheld natural

som ambiente: ambiente de sala de casa, sem música
```

### V06 · T6 · usa K03

```text
o avatar (homem) fala em inglês com sotaque americano de homem negro, voz autêntica, calma e convicta, a seguinte frase: "The second you comment 222, I send their face straight to your messages. That is where the reveal happens."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ele se inclina levemente para a lente ao dizer "I send their face", e mantém o olhar fixo até o fim da frase. A carta fica parada ao lado do rosto.

câmera: fixa, leve push-in muito sutil

som ambiente: ambiente de sala de casa, sem música
```

### V07 · T7 · usa K03

```text
o avatar (homem) fala em inglês com sotaque americano de homem negro, voz autêntica, calma e convicta, a seguinte frase: "But follow me first, or it will not let me reach you. And I only have three readings left today."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ele aponta para cima com o indicador da mão livre ao dizer "follow me first", e depois baixa a mão. Termina olhando parado na lente, com a carta ainda erguida.

câmera: fixa, leve push-in muito sutil

som ambiente: ambiente de sala de casa, sem música
```

---

## Mapa de âncoras

| Keyframe | Referências a anexar | Modelo |
|---|---|---|
| REF-CARTA | nenhuma, gerar do zero | Nano Banana **Pro** |
| K01A, K01B, K01E | **ÂNCORA BLAKE** | Nano Banana **Pro**, várias variações |
| K01C, K01D | **ÂNCORA BLAKE + REF-CARTA** | Nano Banana **Pro**, várias variações |
| K02 | **ÂNCORA BLAKE + REF-CARTA** | Nano Banana **Pro** |
| K03 | K02 aprovado | Nano Banana 2, edição |

---

## Montagem no CapCut

- Timeline 1080x1920, 30 fps. **Plano único o vídeo inteiro, nunca split screen.**
- Cortes duros entre todos os takes. O único que pede peso é T1 para T2, que é a troca de setup.
- Cortar o silêncio inicial de cada clipe.
- **Gráfico fixo o vídeo inteiro:** `222` no topo à esquerda, do frame 0 ao fim.
- **Legendas karaokê**, uma linha por vez, palavra destacada em **amarelo**, centralizadas na altura do peito. **Nunca cobrir a mesa no T1 nem a carta nos demais takes.**
- **Texto de gancho** em caixa branca no topo, só nos primeiros segundos: A e B usam `MAN HIDING TWO`, C usa `SITTING EXACTLY WHERE`, D e E usam `SKIP THIS Y'ALL`.
- Manter `222` isolado e grande na tela durante o V05 e o V06.
- **Cartela final** depois do V07: foto de perfil em círculo com seta apontando pra ela.
- Color grading: temp -3, tint +2, saturação -6, exposição -3, contraste +12, highlight -35, shadow +18, fade +6.

---

## Gates de qualidade

1. **Plano único em todos os keyframes.** Nenhuma imagem saiu com split screen, moldura interna ou inset.
2. **No T1 o Blake está em quadro executando a ação com as próprias mãos**, e não há close isolado na mesa.
3. Blake é o mesmo homem em todos os clipes, com a **cruz de PRATA**.
4. Dreadlocks com mesmo comprimento e mesma raiz escura em todos os planos.
5. **A carta tem arte idêntica ao REF-CARTA** em K01C, K01D, K02 e K03.
6. **A carta está na mão dele do T2 ao T7**, sem sumir em nenhum take.
7. 🚫 **Nenhum rosto de alma gêmea legível em nenhum frame.**
8. O velamento é **propriedade do objeto**, não blur de câmera. Moldura, vidro, papel e mesa nítidos.
9. Estante, bandeira, cruz e janela iguais em todos os keyframes.
10. Mesa limpa no T1, só o objeto do gancho. **No K02 e no K03 nenhum prop de gancho aparece.**
11. Mãos com cinco dedos, sem fusão com a carta nem com o prop.
12. Zero blur de câmera em qualquer keyframe.
13. Nenhuma leitura de pacto. Carta em tons claros.
14. `222` na fala do T5 e do T6, e isolado na tela no CTA.
15. CTA promete o **rosto na DM**, sem citar quiz, teste, app, plano nem preço.
16. Follow gate do T7 presente **com o motivo**.
