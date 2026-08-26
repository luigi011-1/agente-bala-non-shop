# holistic.brandon | Ângulo 2 (FityWell) | Pacote de Prompts

Vídeo modelo: `f036698f-3446-482a-b9ac-cde212650d69.mp4`

Âncora de identidade: `C:\Users\luigi\Desktop\AVATARES NON-SHOP\holistic.brandon .png`

Funil: comment `yes` -> DM -> link do quiz FityWell

**Ângulo 2: o produto NÃO aparece em nenhum take.** Sem print de app, sem celular em quadro, sem mockup. O nome "FityWell" é dito em voz alta no V17.

---

## Índice de geração

| Take | Keyframe | Ação de geração |
|---|---|---|
| ref | REF-A | GERAR DO ZERO a 2ª pessoa (mulher ~50 anos). Aprovar rosto antes do K01. |
| T1 | K01 | GERAR DO ZERO (ref: âncora Brandon + REF-A aprovada). Frame herói, gerar no Pro com variações. |
| T2 | K02 | GERAR DO ZERO (ref: âncora Brandon) |
| T3 | K03 | GERAR DO ZERO (ref: âncora Brandon). Base da mesa. |
| T4 | K04 | EDITAR do K03 (abacates vão pra mesa e escurecem) |
| T5 | K05 | EDITAR do K03 (**nunca do K04**) (abacates saem, entra a tigela e a garrafa) |
| T6 | K06 | GERAR DO ZERO. Insert da tigela, sem rosto. |
| T7 a T12 | K07 | EDITAR do K05 (garrafa sai, mão na borda da tigela, postura de fala) |
| T13 a T20 | K08 | GERAR DO ZERO (ref: âncora Brandon). Corredor, cesta no braço. |

Total: 1 referência + 8 keyframes para 20 takes.

---

## Trava de identidade e continuidade

Aplicar em toda imagem e todo clipe. **Escrita aqui uma vez, não repetir inteira dentro de cada JSON.**

- Preservar exatamente o rosto da Brandon, mulher negra mestiça, pele clara-média, olhos castanhos, sem maquiagem.
- Cornrows trançadas pra trás com pontas trançadas soltas caindo na frente dos ombros, miçangas de madeira e âmbar nas pontas.
- Manga de tatuagem floral de linha fina cobrindo o braço do lado esquerdo do quadro. Pequena tatuagem de folha na clavícula.
- Regata branca canelada. **Corrente fina de OURO com pingente de cruz de OURO. Nunca prata.**
- Mesmo supermercado em todos os planos: seção de hortifruti, caixotes de madeira com tomate, pimentão e folhas, janelas altas e claras, luzes de teto. Mesa de madeira lisa nos setups A a G.
- Luz de dia difusa de loja, uniforme. Zero blur, tudo em foco nítido incluindo prateleira e fundo. Cara de vídeo de iPhone, nunca polimento de IA.
- **Nenhuma marca de supermercado em quadro.** Isso se resolve não descrevendo marca nenhuma, nunca negando marca no campo negative.

## Trava dos props herói (usar nos K01 e K02)

```text
Two orange bell peppers, each standing upright on its own small folded piece of plain brown kraft cardboard. The cardboard cards are completely BLANK with nothing written or printed on them. A brushed stainless steel electric kettle with a black handle. The peppers, the cards and the kettle keep the exact same shape, size and colour in every shot they appear in.
```

## Trava da 2ª pessoa (REF-A) — gerar e aprovar ANTES do K01

```text
IMPORTANT: THIS IS IPHONE FOOTAGE. Vertical 9:16 real smartphone photo. An ordinary American woman around fifty years old stands facing slightly to her left in the produce aisle of a supermarket. She has shoulder-length brown hair with some grey in it, warm medium skin, visible pores, fine lines around the eyes, natural facial asymmetry, no makeup and no retouching. She wears a dark quilted vest over a plain light top. Her arms hang relaxed at her sides and her expression is calm and mildly curious, a shopper watching something on a table. Soft daylight, sharp focus everywhere, no blur. She looks like a real ordinary woman, not a model. No captions, no subtitles, no words overlaid on the image, no studio lighting, no plastic skin, no beauty smoothing.
```

Gerar, aprovar o rosto, e usar essa imagem como referência da 2ª pessoa no K01.

---

# Prompts de imagem

## K01 · T1 · HOOK · GERAR DO ZERO (Nano Banana **Pro**, várias variações) · ÂNCORA BRANDON + REF-A

```json
{
  "shot_id": "K01_hook_pour",
  "context": "Fictional AI-generated characters. No real people are being filmed or depicted.",
  "reference_use": "Use the first attached image ONLY for Brandon's face, identity, hair, tattoos and clothing. Use the second attached image ONLY for the second woman's face so it is clearly the SAME woman. Do NOT copy the pose or framing of either reference. The scene is a supermarket, not a gym.",
  "identity_main": "The EXACT woman from the first reference image (Brandon): mixed-race Black woman, light-medium skin, brown eyes, cornrows braided back with loose braided ends falling in front of the shoulders and wooden and amber beads on the tips, fine-line floral tattoo sleeve on the arm on the left side of frame, small leaf tattoo on the collarbone, no makeup.",
  "wardrobe": "White ribbed tank top, thin GOLD chain with a GOLD cross pendant.",
  "second_person": "The EXACT woman from the second reference image: American woman around fifty, dark quilted vest over a light top, shoulder-length brown hair. She stands close beside Brandon on the right side of frame, watching the table with calm curiosity. Her arms hang relaxed. She touches nothing and does not speak.",
  "prop": "Two orange bell peppers, each standing upright on its own small folded piece of plain brown kraft cardboard, both cards completely BLANK with nothing written on them. Brandon holds a brushed stainless steel electric kettle with both hands, tilted forward over the pepper on the left.",
  "scene": "The produce section of a supermarket. A plain wooden display table in the foreground. Behind them, wooden crates of tomatoes, peppers and leafy greens, tall bright windows and ceiling lights.",
  "posture": "Brandon stands behind the table, leaning slightly forward, both arms working, focused on the pepper.",
  "composition": "Waist-up two-shot, tighter than a normal wide, the table filling the lower foreground. Brandon on the left of frame, the second woman on the right, cropped by the right edge from the shoulder down. The kettle and the pepper sit closest to the lens and are unmistakably the hero.",
  "camera": "chest level, angled slightly high toward the table, pushed in close to the kettle and the pepper",
  "state": "Start frame: the kettle is already tilted and the first thin stream of hot water is just touching the top of the left pepper. Only a small wisp of steam so far.",
  "lighting": "Bright even supermarket daylight from the tall windows plus ceiling lights.",
  "realism": "UGC realism, real skin texture with visible pores, individual hair strands, subtle wrinkles, realistic shadows and reflections, iPhone-footage look, phone camera look not professional photography, no AI polish, no beauty smoothing, no blur anywhere, everything in sharp focus including background shelves and produce.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no writing on the cards, no studio, no plastic skin, no extra fingers, no blur, no silver jewelry, no third person, no large steam cloud yet"
}
```

## K02 · T2 · DICA 1 · GERAR DO ZERO · ÂNCORA BRANDON

```json
{
  "shot_id": "K02_wax",
  "reference_use": "Use the attached image ONLY for Brandon's face, identity, hair, tattoos and clothing. Do NOT copy its pose or framing. The scene is a supermarket.",
  "identity_main": "The EXACT woman from the reference image (Brandon): mixed-race Black woman, light-medium skin, brown eyes, cornrows braided back with loose braided ends and wooden and amber beads on the tips, fine-line floral tattoo sleeve on the arm on the left side of frame, small leaf tattoo on the collarbone, no makeup.",
  "wardrobe": "White ribbed tank top, thin GOLD chain with a GOLD cross pendant.",
  "prop": "Two orange bell peppers on blank folded kraft cardboard cards. The pepper on the left is wet and dull from the water.",
  "scene": "SAME supermarket produce section and SAME wooden display table as K01.",
  "posture": "Standing alone behind the table, leaning in toward the camera, chin slightly down, focused on the pepper.",
  "composition": "TIGHT waist-up, much closer than K01. She is alone, the second woman is gone. The peppers sit in the lower foreground. Her right hand is on the wet pepper, thumb and fingertips pressed against the skin.",
  "camera": "chest level, close, angled slightly high toward her hand and the pepper",
  "state": "Start frame: her fingertips rest on the wet pepper skin, nothing on her fingers yet.",
  "lighting": "Bright even supermarket daylight plus ceiling lights.",
  "realism": "UGC realism, real skin texture with visible pores, individual hair strands, realistic shadows and reflections, iPhone-footage look, phone camera look not professional photography, no AI polish, no beauty smoothing, no blur anywhere, everything in sharp focus.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no writing on the cards, no studio, no plastic skin, no extra fingers, no blur, no silver jewelry, no second person"
}
```

## K03 · T3 · DICA 2 · GERAR DO ZERO · ÂNCORA BRANDON

```json
{
  "shot_id": "K03_avocado_raised",
  "reference_use": "Use the attached image ONLY for Brandon's face, identity, hair, tattoos and clothing. Do NOT copy its pose or framing. The scene is a supermarket.",
  "identity_main": "The EXACT woman from the reference image (Brandon): mixed-race Black woman, light-medium skin, brown eyes, cornrows braided back with loose braided ends and wooden and amber beads on the tips, fine-line floral tattoo sleeve on the arm on the left side of frame, small leaf tattoo on the collarbone, no makeup.",
  "wardrobe": "White ribbed tank top, thin GOLD chain with a GOLD cross pendant.",
  "scene": "SAME supermarket produce section and SAME wooden display table as K01.",
  "posture": "Standing behind the table, upright, chin up, both hands raised to chest height toward the lens.",
  "composition": "TIGHT waist-up, close. She holds ONE avocado half in each hand, raised to chest height and turned flat-face toward the camera, filling the lower half of the frame. The half in her right hand still holds the large round pit. The flesh of BOTH halves is completely clean, even, pale yellow-green, with no darkening anywhere. On the table below sit a second whole dark green avocado and a kitchen knife lying flat.",
  "camera": "chest level, close, straight-on toward the two halves",
  "state": "Start frame: she has just cut the avocado and is raising the two halves toward the lens. The flesh is entirely fresh and unmarked.",
  "lighting": "Bright even supermarket daylight plus ceiling lights.",
  "realism": "UGC realism, real skin texture with visible pores, individual hair strands, realistic shadows and reflections, iPhone-footage look, phone camera look not professional photography, no AI polish, no beauty smoothing, no blur anywhere, everything in sharp focus.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no studio, no plastic skin, no extra fingers, no blur, no silver jewelry, no browning on the flesh, no dark patches on the flesh"
}
```

## K04 · T4 · DICA 2 CONCLUSÃO · EDITAR do K03

```json
{
  "task": "edit the attached image, keep everything identical except the changes listed",
  "keep_identical": "Keep Brandon exactly the same: same face, same hair and beads, same tattoos, same white tank top, same gold cross. Keep the SAME background exactly: wooden table, produce crates, windows, same lighting, same camera angle and framing.",
  "change_1": "The two avocado halves are no longer in her hands. They now lie flat on the wooden table in the lower foreground, cut side up, side by side, with the knife beside them.",
  "change_2": "The flesh of both halves has gone deep muddy brown in a wide uneven ring around the pit, spreading outward into the remaining pale green.",
  "change_3": "Her right hand now points down toward the halves and her left hand rests on the edge of the table. She looks at the camera.",
  "realism": "UGC realism, real skin texture with visible pores, iPhone-footage look, no AI polish, no beauty smoothing, no blur anywhere. Do not make her skin darker, yellowish or orangish. Do not make the colors more saturated.",
  "negative": "do not change the face, do not change identity, do not change the background, do not change the camera angle, no captions, no subtitles, no words overlaid on the image, no plastic skin, no extra fingers, no silver jewelry"
}
```

## K05 · T5 · DICA 3 SETUP · EDITAR do K03 (nunca do K04)

```json
{
  "task": "edit the attached image, keep everything identical except the changes listed",
  "keep_identical": "Keep Brandon exactly the same: same face, same hair and beads, same tattoos, same white tank top, same gold cross. Keep the SAME background exactly: wooden table, produce crates, windows, same lighting, same camera angle and framing.",
  "change_1": "Remove the avocado halves, the whole avocado and the knife completely.",
  "change_2": "Place a wide clear glass mixing bowl on the table in the lower foreground, filled with fresh blueberries covered in clear water. The water surface is clean and clear with nothing floating on it.",
  "change_3": "Her right hand now holds a clear glass bottle of pale vinegar, tilted just above the bowl, about to pour. Her left hand rests on the table beside the bowl.",
  "realism": "UGC realism, real skin texture with visible pores, iPhone-footage look, no AI polish, no beauty smoothing, no blur anywhere. Do not make her skin darker, yellowish or orangish. Do not make the colors more saturated.",
  "negative": "do not change the face, do not change identity, do not change the background, do not change the camera angle, no captions, no subtitles, no words overlaid on the image, no labels on the bottle, no plastic skin, no extra fingers, no silver jewelry, nothing floating on the water"
}
```

## K06 · T6 · DICA 3 REVEAL · GERAR DO ZERO · INSERT SEM ROSTO

```json
{
  "shot_id": "K06_bowl_insert",
  "reference_use": "Close-up insert. No face. Use only the wooden table surface and the supermarket lighting of the other shots.",
  "identity_main": "No people in frame. Close-up of a wide clear glass mixing bowl on a plain wooden table.",
  "scene": "SAME wooden display table, the supermarket produce section softly visible far behind and above the bowl.",
  "composition": "Close-up on the bowl, filling most of the frame, shot slightly from above so the whole water surface is visible. The bowl is filled with fresh blueberries sitting under clear water. The water is perfectly clear and the surface is completely clean and undisturbed.",
  "camera": "slightly high angle, close to the bowl",
  "state": "Start frame: still clear water, clean surface, nothing on it.",
  "lighting": "Bright even supermarket daylight plus ceiling lights.",
  "realism": "UGC realism, real glass reflections, real water refraction, iPhone macro look, no AI polish, no blur anywhere, everything in sharp focus.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no face, no hands, no studio, no cartoon look, no blur"
}
```

## K07 · T7 a T12 · BLOCO DE ARGUMENTO · EDITAR do K05

```json
{
  "task": "edit the attached image, keep everything identical except the changes listed",
  "keep_identical": "Keep Brandon exactly the same: same face, same hair and beads, same tattoos, same white tank top, same gold cross. Keep the SAME background exactly: wooden table, produce crates, windows, same lighting, same camera angle and framing. Keep the SAME glass bowl of blueberries in water in the lower foreground.",
  "change_1": "The vinegar bottle is gone from her hand and from the table.",
  "change_2": "Her left hand now rests on the rim of the glass bowl and her right hand is open near her chest in a natural mid-gesture. She stands upright and speaks directly into the lens with a warm, direct expression.",
  "realism": "UGC realism, real skin texture with visible pores, iPhone-footage look, no AI polish, no beauty smoothing, no blur anywhere. Do not make her skin darker, yellowish or orangish. Do not make the colors more saturated.",
  "negative": "do not change the face, do not change identity, do not change the background, do not change the camera angle, no captions, no subtitles, no words overlaid on the image, no plastic skin, no extra fingers, no silver jewelry"
}
```

## K08 · T13 a T20 · FECHAMENTO E CTA · GERAR DO ZERO · ÂNCORA BRANDON

```json
{
  "shot_id": "K08_aisle_cta",
  "reference_use": "Use the attached image ONLY for Brandon's face, identity, hair, tattoos and clothing. Do NOT copy its pose or framing. This must be the CLOSEST framing of the entire video.",
  "identity_main": "The EXACT woman from the reference image (Brandon): mixed-race Black woman, light-medium skin, brown eyes, cornrows braided back with loose braided ends and wooden and amber beads on the tips, fine-line floral tattoo sleeve on the arm on the left side of frame, small leaf tattoo on the collarbone, no makeup.",
  "wardrobe": "White ribbed tank top, thin GOLD chain with a GOLD cross pendant.",
  "scene": "Standing in the produce aisle of the same supermarket. Behind her, bins of tomatoes, peppers, cucumbers and leafy greens running away down the aisle, bright windows and ceiling lights.",
  "posture": "Standing upright in the aisle, very close to the lens, chin up, shoulders squared, direct personal eye contact.",
  "composition": "TIGHT chest-up close-up, the tightest framing in the whole video, her head and shoulders fill the frame. A black plastic shopping basket hangs from the crook of her left arm, only its handle and top edge visible at the bottom corner of frame. Her right hand is up near her chest, open, mid-gesture. Nothing else in her hands.",
  "camera": "eye level, straight-on, very close",
  "state": "Start frame: speaking straight into the lens.",
  "lighting": "Bright even supermarket daylight plus ceiling lights.",
  "realism": "UGC realism, real skin texture with visible pores, individual hair strands, subtle wrinkles, realistic shadows and reflections, iPhone-footage look, phone camera look not professional photography, no AI polish, no beauty smoothing, no blur anywhere, everything in sharp focus.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no price tags, no studio, no plastic skin, no extra fingers, no blur, no silver jewelry, no phone in hand, no product, no bottle, no jar"
}
```

---

# Prompts de vídeo (Veo 3.1 via Flow)

## Bloco global

Colar em todo prompt:

```text
a avatar (mulher) fala em inglês com sotaque americano de mulher negra, voz autêntica, dinâmica, apaixonada e emocional, como se exigisse ser ouvida.

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

Estilo TikTok nativo, UGC. Preservar exatamente a identidade da Brandon, rosto, cornrows com miçangas, tatuagens, regata branca, cruz de OURO, o supermercado, a iluminação e o enquadramento do frame inicial. Sem legenda, sem texto gerado, sem música, sem pessoas extras.
```

**A câmera nunca é handheld de selfie neste vídeo.** As mãos dela estão nos props o tempo todo, então NÃO incluir a instrução de braço parado.

---

### V01 · T1 · usa K01

```text
a avatar (mulher) fala em inglês com sotaque americano de mulher negra, voz autêntica, dinâmica e emocional, como se exigisse ser ouvida, a seguinte frase: "Pour boiling water over your bell peppers, ma'am, and let them dry."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ela inclina a chaleira e a água quente cai sobre o pimentão; uma nuvem branca de vapor sobe e toma o quadro; ela levanta o olhar pra câmera. A mulher ao lado permanece parada, olhando a mesa, sem falar.

câmera: fixa, leve handheld natural

som ambiente: ambiente de supermercado, sem música, sem ruído de fundo
```

### V02 · T2 · usa K02

```text
a avatar (mulher) fala em inglês com sotaque americano de mulher negra, voz autêntica, dinâmica e emocional, a seguinte frase: "If a white waxy film shows up on the skin, that pepper was coated in wax just so it would shine under the store lights."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ela raspa os dedos na casca molhada do pimentão; uma película branca sai e se acumula nos dedos; ela levanta a mão pra câmera e esfrega o polegar no indicador.

câmera: fixa, leve handheld natural

som ambiente: ambiente de supermercado, sem música, sem ruído de fundo
```

### V03 · T3 · usa K03 · REVEAL CONTÍNUO, NÃO PODE CORTAR

```text
a avatar (mulher) fala em inglês com sotaque americano de mulher negra, voz autêntica, dinâmica e emocional, a seguinte frase: "Number two. Avocado. Cut one open and watch how fast the inside goes brown around the pit."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ela segura as duas metades de abacate erguidas na frente do corpo e a polpa escurece a partir do caroço, se espalhando pelas duas metades enquanto ela fala. Tudo acontece no mesmo take, sem nenhum corte, e as duas metades ficam em quadro o tempo inteiro.

câmera: fixa, leve handheld natural

som ambiente: ambiente de supermercado, sem música, sem ruído de fundo
```

### V04 · T4 · usa K04

```text
a avatar (mulher) fala em inglês com sotaque americano de mulher negra, voz autêntica, dinâmica e emocional, a seguinte frase: "If it darkens almost instantly, that avocado has been sitting a lot longer than the sticker says."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ela aponta pras metades escuras na mesa e volta o olhar pra câmera.

câmera: fixa, leve handheld natural

som ambiente: ambiente de supermercado, sem música, sem ruído de fundo
```

### V05 · T5 · usa K05

```text
a avatar (mulher) fala em inglês com sotaque americano de mulher negra, voz autêntica, dinâmica e emocional, a seguinte frase: "Number three. Blueberries. Drop them in a bowl of water with a splash of vinegar and wait five minutes."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ela inclina a garrafa e o vinagre cai na tigela; os mirtilos balançam na água; ela apoia a garrafa na mesa e olha pra câmera.

câmera: fixa, leve handheld natural

som ambiente: ambiente de supermercado, sem música, sem ruído de fundo
```

### V06 · T6 · usa K06 · B-ROLL · REVEAL CONTÍNUO, NÃO PODE CORTAR

```text
(sem fala no take: a fala 6 do roteiro entra como voz-over na edição)

o que acontece no vídeo: formas pálidas cor de creme, curvas, do tamanho de um grão de arroz cozido, sobem devagar de entre os mirtilos e se juntam na superfície da água, primeiro poucas e depois muitas, até haver dezenas delas paradas em cima. Tudo no mesmo take, sem corte.

câmera: leve push-in lento e contínuo em direção à superfície da água

som ambiente: ambiente de supermercado, sem música
```

**Se o V06 travar:** enxugar a ação primeiro (Passo 1 do protocolo). Tirar o push-in e deixar `câmera: fixa`, e reduzir a descrição a "formas pálidas cor de creme sobem devagar e se juntam na superfície da água". Não mexer em mais nada e não colocar palavra nenhuma no negative.

### V07 · T7 · usa K07

```text
a avatar (mulher) fala em inglês com sotaque americano de mulher negra, voz autêntica, dinâmica e emocional, a seguinte frase: "And it is the reason I stopped telling women over forty to just eat clean. And there is a fourth one."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ela mantém a mão esquerda na borda da tigela, levanta a mão direita e mostra quatro dedos pra câmera no fim da frase.

câmera: fixa, leve handheld natural

som ambiente: ambiente de supermercado, sem música, sem ruído de fundo
```

### V08 · T8 · usa K07

```text
a avatar (mulher) fala em inglês com sotaque americano de mulher negra, voz autêntica, dinâmica e emocional, a seguinte frase: "It is not on any label, you cannot wash it off, and it is the only one that decides whether your body lets go of anything."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ela balança a cabeça devagar de um lado pro outro e faz um gesto curto de negação com a mão direita, mantendo a esquerda na tigela.

câmera: fixa, leve handheld natural

som ambiente: ambiente de supermercado, sem música, sem ruído de fundo
```

### V09 · T9 · usa K07

```text
a avatar (mulher) fala em inglês com sotaque americano de mulher negra, voz autêntica, dinâmica e emocional, a seguinte frase: "Washing that fruit is worth doing. I do it. But it only fixes what goes in."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ela bate duas vezes com os dedos na borda da tigela e depois abre a mão direita na altura do peito.

câmera: fixa, leve handheld natural

som ambiente: ambiente de supermercado, sem música, sem ruído de fundo
```

### V10 · T10 · usa K07

```text
a avatar (mulher) fala em inglês com sotaque americano de mulher negra, voz autêntica, dinâmica e emocional, a seguinte frase: "And after forty, what goes in stopped being the problem."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ela tira a mão da tigela e abre as duas mãos na altura do peito, expressão mais séria.

câmera: fixa, leve handheld natural

som ambiente: ambiente de supermercado, sem música, sem ruído de fundo
```

### V11 · T11 · usa K07

```text
a avatar (mulher) fala em inglês com sotaque americano de mulher negra, voz autêntica, dinâmica e emocional, a seguinte frase: "Two women can eat the identical day of food and one of them stores every bite of it. Same food. Different instructions."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ela levanta as duas mãos separadas no ar como se pesasse duas coisas, e no fim baixa as mãos e para de gesticular nas duas últimas frases curtas.

câmera: fixa, leve handheld natural

som ambiente: ambiente de supermercado, sem música, sem ruído de fundo
```

### V12 · T12 · usa K07

```text
a avatar (mulher) fala em inglês com sotaque americano de mulher negra, voz autêntica, dinâmica e emocional, a seguinte frase: "So answer me one thing, and be honest. Does your bloat show up in the morning, or only at night?"

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ela se inclina pra mais perto da câmera, levanta um dedo, e no fim fica parada esperando, olhando fixo pra lente.

câmera: fixa, leve handheld natural

som ambiente: ambiente de supermercado, sem música, sem ruído de fundo
```

### V13 · T13 · usa K08

```text
a avatar (mulher) fala em inglês com sotaque americano de mulher negra, voz autêntica, dinâmica e emocional, a seguinte frase: "Those are two different problems and they need opposite plans."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: corte duro pro corredor. ela fala direto pra câmera e separa as duas mãos no ar indicando duas coisas distintas.

câmera: fixa, leve handheld natural

som ambiente: ambiente de supermercado, sem música, sem ruído de fundo
```

### V14 · T14 · usa K08

```text
a avatar (mulher) fala em inglês com sotaque americano de mulher negra, voz autêntica, dinâmica e emocional, a seguinte frase: "Most of the women I train had been treating the wrong one for years, and doing it perfectly."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: a expressão dela suaviza e fica protetora; ela balança a cabeça uma vez devagar na última frase.

câmera: fixa, leve handheld natural

som ambiente: ambiente de supermercado, sem música, sem ruído de fundo
```

### V15 · T15 · usa K08

```text
a avatar (mulher) fala em inglês com sotaque americano de mulher negra, voz autêntica, dinâmica e emocional, a seguinte frase: "And no app on your phone can answer that. It counts what you ate. It cannot tell you what your body did with it."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ela faz um gesto curto de descarte com a mão direita e depois aponta pra própria barriga na última frase.

câmera: fixa, leve handheld natural

som ambiente: ambiente de supermercado, sem música, sem ruído de fundo
```

### V16 · T16 · usa K08

```text
a avatar (mulher) fala em inglês com sotaque americano de mulher negra, voz autêntica, dinâmica e emocional, a seguinte frase: "That fourth thing is which one your body is actually running."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ela levanta quatro dedos de novo por um instante e depois fecha a mão, com uma expressão de quem entrega a resposta.

câmera: fixa, leve push-in

som ambiente: ambiente de supermercado, sem música, sem ruído de fundo
```

### V17 · T17 · usa K08

```text
a avatar (mulher) fala em inglês com sotaque americano de mulher negra, voz autêntica, dinâmica e emocional, a seguinte frase: "FityWell asks the questions that separate them, and it builds the whole plan around your answer."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ela mantém a mão aberta e firme na frente do peito enquanto fala, expressão aberta e confiante.

câmera: fixa, leve handheld natural

som ambiente: ambiente de supermercado, sem música, sem ruído de fundo
```

### V18 · T18 · usa K08

```text
a avatar (mulher) fala em inglês com sotaque americano de mulher negra, voz autêntica, dinâmica e emocional, a seguinte frase: "You have a grocery run coming up this week. You can walk it guessing again, or you can walk it knowing."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ela ergue de leve a cesta do braço esquerdo ao dizer a primeira frase e depois alterna as duas mãos ao dar as duas opções.

câmera: fixa, leve handheld natural

som ambiente: ambiente de supermercado, sem música, sem ruído de fundo
```

### V19 · T19 · usa K08

```text
a avatar (mulher) fala em inglês com sotaque americano de mulher negra, voz autêntica, dinâmica e emocional, a seguinte frase: "It is free, it takes two minutes, and if you comment yes I will send it straight to you."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ela se inclina pra mais perto da lente e aponta pra baixo, na direção dos comentários, ao dizer "comment yes".

câmera: fixa, leve push-in

som ambiente: ambiente de supermercado, sem música, sem ruído de fundo
```

### V20 · T20 · usa K08

```text
a avatar (mulher) fala em inglês com sotaque americano de mulher negra, voz autêntica, dinâmica e emocional, a seguinte frase: "Send this to whoever you shop with, and follow me first, or it will not let me reach you."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ela aponta uma vez pra câmera, direto, e termina com um aceno curto de cabeça.

câmera: fixa, leve push-in

som ambiente: ambiente de supermercado, sem música, sem ruído de fundo
```

---

## Mapa de âncoras

| Keyframe | Referências a anexar | Modelo |
|---|---|---|
| REF-A | nenhuma, gerar do zero | Nano Banana 2, regenerar até rosto crível |
| K01 | âncora Brandon + REF-A aprovada | Nano Banana **Pro**, várias variações |
| K02 | âncora Brandon | Nano Banana 2 |
| K03 | âncora Brandon | Nano Banana 2 |
| K04 | K03 aprovado | Nano Banana 2, comando de edição |
| K05 | K03 aprovado (**nunca a partir do K04**) | Nano Banana 2, comando de edição |
| K06 | nenhuma, insert sem rosto | Nano Banana 2 |
| K07 | K05 aprovado | Nano Banana 2, comando de edição |
| K08 | âncora Brandon | Nano Banana 2 |

---

## Montagem no CapCut

- Timeline 1080x1920, 30 fps.
- Cortes duros entre todos os takes. Os dois cortes que precisam de peso são V06 para V07, que volta do insert pra ela, e V12 para V13, que é a troca da mesa pro corredor.
- **Carimbar `FAKE` e `REAL`** nos dois cartões de papelão nos takes V01 e V02. Os cartões foram gerados em branco de propósito.
- **V06 leva a fala 6 como voz-over.** O take é b-roll sem rosto.
- Cortar o silêncio inicial de cada clipe para a fala começar imediatamente.
- **Segurar um beat extra de silêncio no fim do V12**, depois da pergunta do autodiagnóstico. A pausa é o que faz ela responder por dentro.
- Legendas grandes estilo Captions.ai Prism Pro, palavra destacada em vermelho, centralizadas na altura do peito. Nunca cobrir o pimentão no hook, as metades de abacate no V03 nem a superfície da tigela no V06.
- Manter `YES` isolado na tela no CTA.
- Color grading: temp -3, tint +2, saturação -6, exposição -3, contraste +12, highlight -35, shadow +18, fade +6.

## Gates de qualidade

1. Brandon é a mesma mulher em todos os clipes, com a cruz de OURO em todos.
2. As cornrows com miçangas estão iguais em todos os planos.
3. Os dois pimentões e os dois cartões de papelão têm a mesma forma e tamanho no K01 e no K02, e os cartões estão **em branco**.
4. A 2ª pessoa é a mesma mulher do REF-A, aparece só no V01, não fala e não toca em nada.
5. **O V03 não tem corte.** O escurecimento do abacate acontece dentro do take, com as duas metades em quadro o tempo inteiro.
6. **O V06 não tem corte.** As formas sobem progressivamente no mesmo take.
7. Nenhuma legenda ou texto foi gerado dentro da imagem, e nenhuma marca de supermercado aparece.
8. Mãos com cinco dedos, sem fusão com a chaleira, a tigela ou a cesta.
9. **Nenhum produto, celular ou tela em quadro em nenhum take.** O nome FityWell só existe em áudio, no V17.
10. `yes` e o follow gate estão os dois no CTA final.
