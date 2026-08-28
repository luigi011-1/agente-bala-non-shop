# Melody Carter | Ângulo 1 (Korella Saffron) | Pacote de Prompts

Vídeo modelo: `f036698f-3446-482a-b9ac-cde212650d69.mp4`

Âncora de identidade: `C:\Users\luigi\Desktop\AVATARES NON-SHOP\melody carter .png`

Referência de produto: `C:\Users\luigi\Desktop\B-ROLL PRODUTOS\product.png`

Funil: comment `yes` -> DM -> deep link Amazon

> ⚠️ **MELODY É HOMEM.** Escrever `The EXACT man / male` em todo `identity_main`. Este vídeo tem uma 2ª pessoa em cena no K01, que é o caso exato em que a IA troca os gêneros por causa do nome "Melody" soar feminino.
>
> ⚠️ **A foto-âncora dele é SENTADO na bancada.** Corrigir a postura em todo prompt: `standing upright, NOT the seated slouch of the reference photo, no legs or lap in frame` + negative `no seated slouch`.

---

## Índice de geração

| Take | Keyframe | Ação de geração |
|---|---|---|
| ref | REF-A | GERAR DO ZERO a 2ª pessoa (homem ~50 anos). Aprovar rosto antes do K01. |
| T1 | K01 | GERAR DO ZERO (ref: âncora Melody + REF-A aprovada). Frame herói, gerar no Pro com variações. |
| T2 | K02 | GERAR DO ZERO (ref: âncora Melody) |
| T3 | K03 | GERAR DO ZERO (ref: âncora Melody). Base da mesa. |
| T4 | K04 | EDITAR do K03 (abacates vão pra mesa e escurecem) |
| T5 | K05 | EDITAR do K03 (**nunca do K04**) (abacates saem, entra a tigela e a garrafa) |
| T6 | K06 | GERAR DO ZERO. Insert da tigela, sem rosto. |
| T7 a T17 | K07 | EDITAR do K05 (garrafa sai, mão na borda da tigela, postura de fala) |
| T18 a T23 | K08 | GERAR DO ZERO (ref: âncora Melody + product.png). Frasco na mão. |

Total: 1 referência + 8 keyframes para 23 takes.

---

## Trava de identidade e continuidade

Aplicar em toda imagem e todo clipe. **Escrita aqui uma vez, não repetir inteira dentro de cada JSON.**

- Preservar exatamente o rosto do Melody, **homem** negro, cavanhaque e barba aparada, musculoso.
- Longas tranças box braids escuras caindo na frente dos ombros.
- Tatuagem ornamental de manga no braço direito, pequenas tatuagens no peito.
- Regata branca canelada. **Corrente fina de PRATA com pingente de cruz de PRATA. Nunca ouro.**
- Mesmo supermercado em todos os planos, com **duas âncoras visuais apenas**: caixotes de produtos frescos e janelas claras. Mesa de madeira lisa nos setups A a G. **Nunca inventariar o fundo**, o cenário só precisa ser reconhecível.
- **Sempre em pé**, nunca a pose sentada e relaxada da foto-âncora.
- Luz de dia difusa de loja, uniforme. Zero blur, tudo em foco nítido incluindo prateleira e fundo. Cara de vídeo de iPhone, nunca polimento de IA.
- **Nenhuma marca de supermercado em quadro.** Resolve-se não descrevendo marca nenhuma, nunca negando marca no negative.

## Trava dos props herói (usar nos K01 e K02)

```text
Two orange bell peppers, each standing upright on its own small folded piece of plain brown kraft cardboard. The cardboard cards are completely BLANK with nothing written or printed on them. A brushed stainless steel electric kettle with a black handle. The peppers, the cards and the kettle keep the exact same shape, size and colour in every shot they appear in.
```

## Trava do produto (usar no K08)

```text
A white supplement bottle with a purple and white label, about 10 cm tall, held upright in his hand with the label facing the camera and fully readable in shape. The bottle keeps the exact same size, proportions and label layout as the attached product reference image.
```

## Trava da 2ª pessoa (REF-A) — gerar e aprovar ANTES do K01

```text
IMPORTANT: THIS IS IPHONE FOOTAGE. Vertical 9:16 real smartphone photo. An ordinary American man around fifty years old stands facing slightly to his left in the produce aisle of a supermarket. He has short greying hair, a trimmed grey beard, warm medium skin, visible pores, fine lines around the eyes, natural facial asymmetry and no retouching. He wears a plain dark zip jacket over a light t-shirt. His arms hang relaxed at his sides and his expression is calm and mildly curious, a shopper watching something on a table. Soft daylight, sharp focus everywhere, no blur. He looks like a real ordinary man, not a model. No captions, no subtitles, no words overlaid on the image, no studio lighting, no plastic skin, no beauty smoothing.
```

Gerar, aprovar o rosto, e usar essa imagem como referência da 2ª pessoa no K01.

---

## GATE DE COMPOSIÇÃO VISUAL (rodado ANTES de escrever os prompts abaixo)

Composição não se conserta depois da geração, se conserta no prompt. Os 10 itens de `checklist-composicao-visual`:

```
HEROI
[x] 1. O heroi esta no LOWER FOREGROUND, mais perto da lente que o rosto
[x] 2. Nada compete com ele: elemento que nao serve a fala do take sai de quadro
[x] 3. Volume e cobertura do heroi explicitados

DISTANCIA
[x] 4. "Da pra estar mais perto?" aplicado em TODO take, nao so no hook
[x] 5. Pessoas em peito pra cima ou ombros pra cima
[x] 6. O take mais fechado do video inteiro e o do CTA (K08)

FUNDO
[x] 7. Cenario RECONHECIVEL, nunca inventariado: 2 ancoras visuais, nao 6
[x] 8. Fundo reduzido por ENQUADRAMENTO, nunca por blur
[x] 9. Menos elementos = mais qualidade de geracao

2a PESSOA
[x] 10. Entra CORTADA pelo quadro, nunca de corpo inteiro
```

**Duas correções que este gate pegou nos prompts deste vídeo:**

1. **Inventário de fundo.** Todos os prompts listavam "caixotes de tomate, pimentão e folhas, janelas altas e claras, luzes de teto". Seis substantivos onde bastavam dois. Cada um a mais é atenção dispersada e um detalhe a mais pro gerador errar. Reduzido para **"caixotes de produtos frescos e janelas claras"**.
2. **Two-shot largo demais no K01.** Estava "waist-up two-shot" pra caber as duas pessoas. Fechado para o herói colado na lente, com a 2ª pessoa **cortada da cintura pra cima e pela borda direita**.

**Nota sobre o item 8:** o negative da operação proíbe blur em tudo, então tirar informação de fundo **nunca** é desfocar. É fechar o plano e escrever menos.

---

# Prompts de imagem

## K01 · T1 · HOOK · GERAR DO ZERO (Nano Banana **Pro**, várias variações) · ÂNCORA MELODY + REF-A

```json
{
  "shot_id": "K01_hook_pour",
  "context": "Fictional AI-generated characters. No real people are being filmed or depicted.",
  "reference_use": "Use the first attached image ONLY for Melody's face, identity, hair, tattoos and clothing. Use the second attached image ONLY for the second man's face so it is clearly the SAME man. Do NOT copy the pose or framing of either reference. The scene is a supermarket, not a garage.",
  "identity_main": "The EXACT MAN from the first reference image (Melody Carter), a male adult: Black man, muscular build, long dark box braids falling in front of the shoulders, trimmed goatee and beard, ornamental tattoo sleeve on his right arm, small chest tattoos.",
  "wardrobe": "White ribbed tank top, thin SILVER chain with a SILVER cross pendant.",
  "second_person": "The EXACT man from the second reference image: American man around fifty, short greying hair, trimmed grey beard, plain dark zip jacket over a light t-shirt. He stands close beside Melody on the right side of frame, watching the table with calm curiosity. His arms hang relaxed. He touches nothing and does not speak.",
  "prop": "Two orange bell peppers, each standing upright on its own small folded piece of plain brown kraft cardboard, both cards completely BLANK with nothing written on them. Melody holds a brushed stainless steel electric kettle with both hands, tilted forward over the pepper on the left.",
  "scene": "The produce section of a supermarket. A plain wooden display table in the foreground. Behind them, crates of fresh produce and bright windows. Nothing else competes for attention.",
  "posture": "Melody stands upright behind the table, NOT the seated slouch of the reference photo, no legs or lap in frame, leaning slightly forward with both arms working, focused on the pepper.",
  "composition": "TIGHT chest-up framing, much closer than a normal two-shot. The kettle and the pepper fill the lower foreground and sit closer to the lens than anything else, unmistakably the hero. Melody occupies the left of frame from the chest up, cropped at the top of his head. The second man is CROPPED HARD by the right edge: only his shoulder, chest and part of his face are in shot, never his full body. The store behind is barely readable, just enough to recognise the place.",
  "camera": "chest level, angled slightly high toward the table, pushed in close to the kettle and the pepper",
  "state": "Start frame: the kettle is already tilted and the first thin stream of hot water is just touching the top of the left pepper. Only a small wisp of steam so far.",
  "lighting": "Bright even supermarket daylight from the tall windows plus ceiling lights.",
  "realism": "UGC realism, real skin texture with visible pores, individual hair strands, subtle wrinkles, realistic shadows and reflections, iPhone-footage look, phone camera look not professional photography, no AI polish, no beauty smoothing, no blur anywhere, everything in sharp focus including background shelves and produce.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no writing on the cards, no studio, no plastic skin, no extra fingers, no blur, no gold jewelry, no seated slouch, no third person, no large steam cloud yet, no woman in frame"
}
```

## K02 · T2 · DICA 1 · GERAR DO ZERO · ÂNCORA MELODY

```json
{
  "shot_id": "K02_wax",
  "reference_use": "Use the attached image ONLY for Melody's face, identity, hair, tattoos and clothing. Do NOT copy its pose or framing. The scene is a supermarket.",
  "identity_main": "The EXACT MAN from the reference image (Melody Carter), a male adult: Black man, muscular build, long dark box braids falling in front of the shoulders, trimmed goatee and beard, ornamental tattoo sleeve on his right arm, small chest tattoos.",
  "wardrobe": "White ribbed tank top, thin SILVER chain with a SILVER cross pendant.",
  "prop": "Two orange bell peppers on blank folded kraft cardboard cards. The pepper on the left is wet and dull from the water.",
  "scene": "SAME supermarket produce section and SAME wooden display table as K01.",
  "posture": "Standing upright alone behind the table, NOT the seated slouch of the reference photo, leaning in toward the camera, chin slightly down, focused on the pepper.",
  "composition": "TIGHT waist-up, much closer than K01. He is alone, the second man is gone. The peppers sit in the lower foreground. His right hand is on the wet pepper, thumb and fingertips pressed against the skin.",
  "camera": "chest level, close, angled slightly high toward his hand and the pepper",
  "state": "Start frame: his fingertips rest on the wet pepper skin, nothing on his fingers yet.",
  "lighting": "Bright even supermarket daylight plus ceiling lights.",
  "realism": "UGC realism, real skin texture with visible pores, individual hair strands, realistic shadows and reflections, iPhone-footage look, phone camera look not professional photography, no AI polish, no beauty smoothing, no blur anywhere, everything in sharp focus.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no writing on the cards, no studio, no plastic skin, no extra fingers, no blur, no gold jewelry, no seated slouch, no second person"
}
```

## K03 · T3 · DICA 2 · GERAR DO ZERO · ÂNCORA MELODY

```json
{
  "shot_id": "K03_avocado_raised",
  "reference_use": "Use the attached image ONLY for Melody's face, identity, hair, tattoos and clothing. Do NOT copy its pose or framing. The scene is a supermarket.",
  "identity_main": "The EXACT MAN from the reference image (Melody Carter), a male adult: Black man, muscular build, long dark box braids falling in front of the shoulders, trimmed goatee and beard, ornamental tattoo sleeve on his right arm, small chest tattoos.",
  "wardrobe": "White ribbed tank top, thin SILVER chain with a SILVER cross pendant.",
  "scene": "SAME supermarket produce section and SAME wooden display table as K01.",
  "posture": "Standing upright behind the table, NOT the seated slouch of the reference photo, chin up, both hands raised to chest height toward the lens.",
  "composition": "TIGHT waist-up, close. He holds ONE avocado half in each hand, raised to chest height and turned flat-face toward the camera, filling the lower half of the frame. The half in his right hand still holds the large round pit. The flesh of BOTH halves is completely clean, even, pale yellow-green, with no darkening anywhere. On the table below sit a second whole dark green avocado and a kitchen knife lying flat.",
  "camera": "chest level, close, straight-on toward the two halves",
  "state": "Start frame: he has just cut the avocado and is raising the two halves toward the lens. The flesh is entirely fresh and unmarked.",
  "lighting": "Bright even supermarket daylight plus ceiling lights.",
  "realism": "UGC realism, real skin texture with visible pores, individual hair strands, realistic shadows and reflections, iPhone-footage look, phone camera look not professional photography, no AI polish, no beauty smoothing, no blur anywhere, everything in sharp focus.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no studio, no plastic skin, no extra fingers, no blur, no gold jewelry, no seated slouch, no browning on the flesh, no dark patches on the flesh"
}
```

## K04 · T4 · DICA 2 CONCLUSÃO · EDITAR do K03

```json
{
  "task": "edit the attached image, keep everything identical except the changes listed",
  "keep_identical": "Keep the man exactly the same: same face, same box braids, same tattoos, same white tank top, same silver cross, same standing posture. Keep the SAME background exactly: wooden table, produce crates, same lighting, same camera angle and framing.",
  "change_1": "The two avocado halves are no longer in his hands. They now lie flat on the wooden table in the lower foreground, cut side up, side by side, with the knife beside them.",
  "change_2": "The flesh of both halves has gone deep muddy brown in a wide uneven ring around the pit, spreading outward into the remaining pale green.",
  "change_3": "His right hand now points down toward the halves and his left hand rests on the edge of the table. He looks at the camera.",
  "realism": "UGC realism, real skin texture with visible pores, iPhone-footage look, no AI polish, no beauty smoothing, no blur anywhere. Do not make his skin darker, yellowish or orangish. Do not make the colors more saturated.",
  "negative": "do not change the face, do not change identity, do not change the background, do not change the camera angle, no captions, no subtitles, no words overlaid on the image, no plastic skin, no extra fingers, no gold jewelry"
}
```

## K05 · T5 · DICA 3 SETUP · EDITAR do K03 (nunca do K04)

```json
{
  "task": "edit the attached image, keep everything identical except the changes listed",
  "keep_identical": "Keep the man exactly the same: same face, same box braids, same tattoos, same white tank top, same silver cross, same standing posture. Keep the SAME background exactly: wooden table, produce crates, same lighting, same camera angle and framing.",
  "change_1": "Remove the avocado halves, the whole avocado and the knife completely.",
  "change_2": "Place a wide clear glass mixing bowl on the table in the lower foreground, filled with fresh blueberries covered in clear water. The water surface is clean and clear with nothing floating on it.",
  "change_3": "His right hand now holds a clear glass bottle of pale vinegar, tilted just above the bowl, about to pour. His left hand rests on the table beside the bowl.",
  "realism": "UGC realism, real skin texture with visible pores, iPhone-footage look, no AI polish, no beauty smoothing, no blur anywhere. Do not make his skin darker, yellowish or orangish. Do not make the colors more saturated.",
  "negative": "do not change the face, do not change identity, do not change the background, do not change the camera angle, no captions, no subtitles, no words overlaid on the image, no labels on the bottle, no plastic skin, no extra fingers, no gold jewelry, nothing floating on the water"
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

## K07 · T7 a T17 · BLOCO DE ARGUMENTO · EDITAR do K05

```json
{
  "task": "edit the attached image, keep everything identical except the changes listed",
  "keep_identical": "Keep the man exactly the same: same face, same box braids, same tattoos, same white tank top, same silver cross, same standing posture. Keep the SAME background exactly: wooden table, produce crates, same lighting, same camera angle and framing. Keep the SAME glass bowl of blueberries in water in the lower foreground.",
  "change_1": "The vinegar bottle is gone from his hand and from the table.",
  "change_2": "His left hand now rests on the rim of the glass bowl and his right hand is open near his chest in a natural mid-gesture. He stands upright and speaks directly into the lens with a calm, direct expression.",
  "realism": "UGC realism, real skin texture with visible pores, iPhone-footage look, no AI polish, no beauty smoothing, no blur anywhere. Do not make his skin darker, yellowish or orangish. Do not make the colors more saturated.",
  "negative": "do not change the face, do not change identity, do not change the background, do not change the camera angle, no captions, no subtitles, no words overlaid on the image, no plastic skin, no extra fingers, no gold jewelry"
}
```

## K08 · T18 a T23 · PRODUTO E CTA · GERAR DO ZERO · ÂNCORA MELODY + PRODUCT.PNG

```json
{
  "shot_id": "K08_aisle_product",
  "reference_use": "Use the first attached image ONLY for Melody's face, identity, hair, tattoos and clothing. Use the second attached image ONLY for the exact shape, size, proportions and label layout of the bottle. Do NOT copy the pose or framing of either reference. This must be the CLOSEST framing of the entire video.",
  "identity_main": "The EXACT MAN from the first reference image (Melody Carter), a male adult: Black man, muscular build, long dark box braids falling in front of the shoulders, trimmed goatee and beard, ornamental tattoo sleeve on his right arm, small chest tattoos.",
  "wardrobe": "White ribbed tank top, thin SILVER chain with a SILVER cross pendant.",
  "product": "The EXACT white supplement bottle from the second reference image, with its purple and white label, about 10 cm tall. He holds it upright in his right hand at chest height, label turned squarely toward the lens, close to the camera and clearly the hero of the frame.",
  "scene": "Standing in the produce aisle of the same supermarket. Behind him, bins of fresh produce running away down the aisle. Nothing else competes for attention.",
  "posture": "Standing upright in the aisle, NOT the seated slouch of the reference photo, very close to the lens, chin up, shoulders squared, direct eye contact.",
  "composition": "TIGHT chest-up close-up, the tightest framing in the whole video. His head and shoulders fill the upper frame and the bottle sits in the lower foreground, closer to the lens than his face.",
  "camera": "chest level, straight-on, very close, angled slightly toward the bottle",
  "state": "Start frame: bottle already raised and steady, speaking straight into the lens.",
  "lighting": "Bright even supermarket daylight plus ceiling lights.",
  "realism": "UGC realism, real skin texture with visible pores, individual hair strands, subtle wrinkles, realistic shadows and reflections, iPhone-footage look, phone camera look not professional photography, no AI polish, no beauty smoothing, no blur anywhere, everything in sharp focus.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no price tags, no studio, no plastic skin, no extra fingers, no blur, no gold jewelry, no seated slouch, no second bottle, no shopping basket"
}
```

---

# Prompts de vídeo (Veo 3.1 via Flow)

## Bloco global

Colar em todo prompt:

```text
o avatar (homem) fala em inglês com sotaque americano de homem negro, voz autêntica, dinâmica, apaixonada e emocional, como se exigisse ser ouvido.

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

Estilo TikTok nativo, UGC. Preservar exatamente a identidade do Melody, HOMEM, rosto, box braids, cavanhaque, tatuagens, regata branca, cruz de PRATA, o supermercado, a iluminação e o enquadramento do frame inicial. Sem legenda, sem texto gerado, sem música, sem pessoas extras.
```

**A câmera nunca é handheld de selfie neste vídeo.** As mãos dele estão nos props, então NÃO incluir a instrução de braço parado.

---

### V01 · T1 · usa K01
```text
o avatar (homem) fala em inglês com sotaque americano de homem negro, voz autêntica, dinâmica e emocional, como se exigisse ser ouvido, a seguinte frase: "Pour boiling water over your bell peppers, brother, and let them dry."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ele inclina a chaleira e a água quente cai sobre o pimentão; uma nuvem branca de vapor sobe e toma o quadro; ele levanta o olhar pra câmera. O homem ao lado permanece parado, olhando a mesa, sem falar.

câmera: fixa, leve handheld natural

som ambiente: ambiente de supermercado, sem música, sem ruído de fundo
```

### V02 · T2 · usa K02
```text
o avatar (homem) fala em inglês com sotaque americano de homem negro, voz autêntica, dinâmica e emocional, a seguinte frase: "If a white waxy film shows up on the skin, that pepper was coated in wax just so it would shine under the store lights."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ele raspa os dedos na casca molhada do pimentão; uma película branca sai e se acumula nos dedos; ele levanta a mão pra câmera e esfrega o polegar no indicador.

câmera: fixa, leve handheld natural

som ambiente: ambiente de supermercado, sem música, sem ruído de fundo
```

### V03 · T3 · usa K03 · REVEAL CONTÍNUO, NÃO PODE CORTAR
```text
o avatar (homem) fala em inglês com sotaque americano de homem negro, voz autêntica, dinâmica e emocional, a seguinte frase: "Number two. Avocado. Cut one open and watch how fast the inside goes brown around the pit."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ele segura as duas metades de abacate erguidas na frente do corpo e a polpa escurece a partir do caroço, se espalhando pelas duas metades enquanto ele fala. Tudo acontece no mesmo take, sem nenhum corte, e as duas metades ficam em quadro o tempo inteiro.

câmera: fixa, leve handheld natural

som ambiente: ambiente de supermercado, sem música, sem ruído de fundo
```

### V04 · T4 · usa K04
```text
o avatar (homem) fala em inglês com sotaque americano de homem negro, voz autêntica, dinâmica e emocional, a seguinte frase: "If it darkens almost instantly, that avocado has been sitting a lot longer than the sticker says."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ele aponta pras metades escuras na mesa e volta o olhar pra câmera.

câmera: fixa, leve handheld natural

som ambiente: ambiente de supermercado, sem música, sem ruído de fundo
```

### V05 · T5 · usa K05
```text
o avatar (homem) fala em inglês com sotaque americano de homem negro, voz autêntica, dinâmica e emocional, a seguinte frase: "Number three. Blueberries. Drop them in a bowl of water with a splash of vinegar and wait five minutes."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ele inclina a garrafa e o vinagre cai na tigela; os mirtilos balançam na água; ele apoia a garrafa na mesa e olha pra câmera.

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

**Se travar:** enxugar a ação, Passo 1 do protocolo. Trocar pra `câmera: fixa` e reduzir a descrição a "formas pálidas cor de creme sobem devagar e se juntam na superfície da água". Não mexer em mais nada e não colocar palavra nenhuma no negative.

### V07 · T7 · usa K07
```text
o avatar (homem) fala em inglês com sotaque americano de homem negro, voz autêntica, dinâmica e emocional, a seguinte frase: "And it is the reason I stopped telling my clients over forty to just eat better."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ele mantém a mão esquerda na borda da tigela e abre a mão direita na altura do peito enquanto fala.

câmera: fixa, leve handheld natural

som ambiente: ambiente de supermercado, sem música, sem ruído de fundo
```

### V08 · T8 · usa K07
```text
o avatar (homem) fala em inglês com sotaque americano de homem negro, voz autêntica, dinâmica e emocional, a seguinte frase: "Because you could buy the cleanest food in this store and still be dragging by four in the afternoon."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ele faz um gesto amplo com a mão direita indicando a loja ao redor e depois deixa o braço cair.

câmera: fixa, leve handheld natural

som ambiente: ambiente de supermercado, sem música, sem ruído de fundo
```

### V09 · T9 · usa K07
```text
o avatar (homem) fala em inglês com sotaque americano de homem negro, voz autêntica, dinâmica e emocional, a seguinte frase: "After forty the problem stopped being what you put in. It is what actually reaches you."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ele tira a mão da tigela e aponta pro próprio peito na segunda frase.

câmera: fixa, leve handheld natural

som ambiente: ambiente de supermercado, sem música, sem ruído de fundo
```

### V10 · T10 · usa K07
```text
o avatar (homem) fala em inglês com sotaque americano de homem negro, voz autêntica, dinâmica e emocional, a seguinte frase: "Everything you eat has to be carried. Blood carries it. And the pipes doing the carrying have been narrowing for twenty years."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ele junta o polegar e o indicador aos poucos, fechando o espaço entre eles, enquanto diz a última frase.

câmera: fixa, leve handheld natural

som ambiente: ambiente de supermercado, sem música, sem ruído de fundo
```

### V11 · T11 · usa K07
```text
o avatar (homem) fala em inglês com sotaque americano de homem negro, voz autêntica, dinâmica e emocional, a seguinte frase: "So you eat clean and most of it never arrives. You are buying groceries your body never gets to use."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ele dá um tapinha leve na borda da tigela e balança a cabeça devagar.

câmera: fixa, leve handheld natural

som ambiente: ambiente de supermercado, sem música, sem ruído de fundo
```

### V12 · T12 · usa K07
```text
o avatar (homem) fala em inglês com sotaque americano de homem negro, voz autêntica, dinâmica e emocional, a seguinte frase: "You feel it in the afternoon crash, in the workouts that stopped paying off, and in the parts that used to answer on their own."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ele conta três itens nos dedos da mão direita enquanto fala, e na última parte baixa a mão e olha fixo pra câmera.

câmera: fixa, leve handheld natural

som ambiente: ambiente de supermercado, sem música, sem ruído de fundo
```

### V13 · T13 · usa K07
```text
o avatar (homem) fala em inglês com sotaque americano de homem negro, voz autêntica, dinâmica e emocional, a seguinte frase: "That is why none of it ever paid you back. It was not your discipline. It was the delivery."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ele levanta a mão aberta num gesto de pausa e a expressão fica mais firme nas duas frases curtas.

câmera: fixa, leve handheld natural

som ambiente: ambiente de supermercado, sem música, sem ruído de fundo
```

### V14 · T14 · usa K07
```text
o avatar (homem) fala em inglês com sotaque americano de homem negro, voz autêntica, dinâmica e emocional, a seguinte frase: "And you are not going to eat your way out of it. What those vessels need does not exist in a grocery cart."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ele faz um gesto curto de negação com a mão e depois aponta pro lado, na direção do corredor.

câmera: fixa, leve handheld natural

som ambiente: ambiente de supermercado, sem música, sem ruído de fundo
```

### V15 · T15 · usa K07
```text
o avatar (homem) fala em inglês com sotaque americano de homem negro, voz autêntica, dinâmica e emocional, a seguinte frase: "One thing opens them back up, and men have been using it for centuries. Saffron."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ele levanta um dedo e para o gesto no ar ao dizer a última palavra.

câmera: fixa, leve push-in

som ambiente: ambiente de supermercado, sem música, sem ruído de fundo
```

### V16 · T16 · usa K07
```text
o avatar (homem) fala em inglês com sotaque americano de homem negro, voz autêntica, dinâmica e emocional, a seguinte frase: "But here is the fourth label that lies to you. Flip a saffron bottle over and look for the words proprietary blend."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ele faz um gesto de virar um pote de cabeça pra baixo com a mão direita, como se lesse o verso de um rótulo.

câmera: fixa, leve handheld natural

som ambiente: ambiente de supermercado, sem música, sem ruído de fundo
```

### V17 · T17 · usa K07
```text
o avatar (homem) fala em inglês com sotaque americano de homem negro, voz autêntica, dinâmica e emocional, a seguinte frase: "That phrase exists so they never have to tell you how little is actually in there."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ele junta o polegar e o indicador mostrando uma quantidade minúscula e levanta as sobrancelhas.

câmera: fixa, leve handheld natural

som ambiente: ambiente de supermercado, sem música, sem ruído de fundo
```

### V18 · T18 · usa K08
```text
o avatar (homem) fala em inglês com sotaque americano de homem negro, voz autêntica, dinâmica e emocional, a seguinte frase: "This is the one I take. Korella Saffron. Eighty eight point five milligrams, printed on the front, no blend, nothing hidden."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: corte duro pro corredor. ele ergue o frasco na direção da câmera ao dizer o nome do produto e depois aponta pro rótulo com o dedo.

câmera: fixa, leve push-in

som ambiente: ambiente de supermercado, sem música, sem ruído de fundo
```

### V19 · T19 · usa K08
```text
o avatar (homem) fala em inglês com sotaque americano de homem negro, voz autêntica, dinâmica e emocional, a seguinte frase: "It is on Amazon, and it is the only one I put my clients on."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ele mantém o frasco erguido e firme, e a expressão fica mais confiante.

câmera: fixa, leve handheld natural

som ambiente: ambiente de supermercado, sem música, sem ruído de fundo
```

### V20 · T20 · usa K08
```text
o avatar (homem) fala em inglês com sotaque americano de homem negro, voz autêntica, dinâmica e emocional, a seguinte frase: "It will not fix a bad diet. Nothing does. What it does is make what you already eat actually land."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ele baixa um pouco o frasco e balança a cabeça na primeira frase, depois volta a erguer na última.

câmera: fixa, leve handheld natural

som ambiente: ambiente de supermercado, sem música, sem ruído de fundo
```

### V21 · T21 · usa K08
```text
o avatar (homem) fala em inglês com sotaque americano de homem negro, voz autêntica, dinâmica e emocional, a seguinte frase: "You have a grocery run coming up this week. You can walk it feeding a body that cannot deliver, or fix the delivery first."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ele aponta pro corredor atrás dele na primeira frase e depois traz o frasco de volta pra frente do peito.

câmera: fixa, leve handheld natural

som ambiente: ambiente de supermercado, sem música, sem ruído de fundo
```

### V22 · T22 · usa K08
```text
o avatar (homem) fala em inglês com sotaque americano de homem negro, voz autêntica, dinâmica e emocional, a seguinte frase: "Comment yes and I will send you the link straight to your messages."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ele aponta pra baixo, na direção dos comentários, mantendo o frasco na outra mão.

câmera: fixa, leve push-in

som ambiente: ambiente de supermercado, sem música, sem ruído de fundo
```

### V23 · T23 · usa K08
```text
o avatar (homem) fala em inglês com sotaque americano de homem negro, voz autêntica, dinâmica e emocional, a seguinte frase: "Send this to whoever you shop with, and follow me first, or it will not let me reach you."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ele aponta uma vez pra câmera, direto, e termina com um aceno curto de cabeça.

câmera: fixa, leve push-in

som ambiente: ambiente de supermercado, sem música, sem ruído de fundo
```

---

## Mapa de âncoras

| Keyframe | Referências a anexar | Modelo |
|---|---|---|
| REF-A | nenhuma, gerar do zero | Nano Banana 2, regenerar até rosto crível |
| K01 | âncora Melody + REF-A aprovada | Nano Banana **Pro**, várias variações |
| K02 | âncora Melody | Nano Banana 2 |
| K03 | âncora Melody | Nano Banana 2 |
| K04 | K03 aprovado | Nano Banana 2, comando de edição |
| K05 | K03 aprovado (**nunca a partir do K04**) | Nano Banana 2, comando de edição |
| K06 | nenhuma, insert sem rosto | Nano Banana 2 |
| K07 | K05 aprovado | Nano Banana 2, comando de edição |
| K08 | **âncora Melody + product.png** | Nano Banana **Pro** (o rótulo precisa sair legível) |

---

## Montagem no CapCut

- Timeline 1080x1920, 30 fps. Cortes duros entre todos os takes.
- Os dois cortes que pedem peso: **V06 para V07**, que volta do insert pra ele, e **V17 para V18**, que é a troca da mesa pro corredor e a entrada do produto.
- **Carimbar `FAKE` e `REAL`** nos dois cartões de papelão em V01 e V02. Foram gerados em branco de propósito.
- **V06 leva a fala 6 como voz-over.** O take é b-roll sem rosto.
- Cortar o silêncio inicial de cada clipe para a fala começar imediatamente.
- **Segurar um beat de silêncio depois de "Saffron" no fim do V15.** É o pagamento do loop aberto lá no V08 e precisa respirar.
- Legendas grandes estilo Captions.ai Prism Pro, palavra destacada em vermelho, centralizadas na altura do peito. Nunca cobrir o pimentão no V01, as metades no V03, a superfície da tigela no V06 nem o rótulo do frasco de V18 em diante.
- Manter `YES` isolado na tela no CTA.
- Color grading: temp -3, tint +2, saturação -6, exposição -3, contraste +12, highlight -35, shadow +18, fade +6.

## Gates de qualidade

1. **Melody é HOMEM em todos os clipes.** Conferir especialmente o V01, onde há uma segunda pessoa em cena.
2. Melody é o mesmo homem em todos os clipes, com a cruz de PRATA em todos, nunca ouro.
3. As box braids estão iguais em todos os planos e ele está **em pé** em todos, nunca sentado.
4. Os dois pimentões e os dois cartões têm a mesma forma e tamanho no K01 e no K02, e os cartões estão **em branco**.
5. A 2ª pessoa é o mesmo homem do REF-A, aparece só no V01, não fala e não toca em nada.
6. **O V03 não tem corte.** O escurecimento do abacate acontece dentro do take, com as duas metades em quadro o tempo inteiro.
7. **O V06 não tem corte.** As formas sobem progressivamente no mesmo take.
8. Nenhuma legenda ou texto foi gerado dentro da imagem, e nenhuma marca de supermercado aparece.
9. **O frasco do K08 tem o mesmo tamanho, proporção e layout de rótulo do product.png**, e aparece em todos os takes de T18 a T23.
10. Mãos com cinco dedos, sem fusão com a chaleira, a tigela ou o frasco.
11. `yes` e o follow gate estão os dois no CTA final.

### Composição (conferir em cada imagem gerada, antes de mandar pro Veo)
12. **O herói está mais perto da lente que o rosto** em todo take que tem herói: a chaleira e o pimentão no K01, os dedos com a cera no K02, as metades no K03, a tigela no K06, o frasco no K08.
13. **Nada compete com o herói.** Se sobrou algum objeto em cena que não serve à fala daquele take, regenerar.
14. **O fundo está reconhecível, não inventariado.** Se dá pra contar mais de três coisas distintas atrás dele, está poluído.
15. **O K08 é o plano mais fechado do vídeo inteiro.** Se algum outro estiver mais fechado que ele, está errado.
16. **A 2ª pessoa no K01 está cortada pelo quadro**, nunca de corpo inteiro.
17. **Nenhuma imagem tem fundo desfocado.** Fundo limpo se resolve com enquadramento, e blur é proibido em todas.
