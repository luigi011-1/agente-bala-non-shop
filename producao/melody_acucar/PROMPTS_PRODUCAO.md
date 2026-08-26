# Melody Carter | Ângulo 1 (Korella Saffron) | Pacote de Prompts

Vídeo modelo: `e47258d0-5ab6-4c69-a982-5e4557a26cd5.mp4`

Âncora de identidade: `C:\Users\luigi\Desktop\AVATARES NON-SHOP\melody_carter_.png`

Referência de produto: `C:\Users\luigi\Desktop\B-ROLL PRODUTOS\product.png`

Funil: comment `yes` -> DM -> deep link Amazon

> ⚠️ **MELODY É HOMEM.** Escrever `The EXACT man / male adult` em todo `identity_main`. Há 2ª pessoa em cena nos três primeiros keyframes.
>
> ⚠️ **O CLIENTE DO HOOK É HOMEM**, uns cinquenta anos. No original é mulher. Ângulo 1 é público masculino e o espectador precisa se reconhecer no corpo apontado.
>
> ⚠️ **A foto-âncora do Melody é sentada.** Aqui ele fica **EM PÉ** nos setups A a D e G. Corrigir a postura em todo prompt.

---

## Índice de geração

| Take | Keyframe | Ação de geração |
|---|---|---|
| ref | REF-A | GERAR DO ZERO o cliente (homem ~50, corpo). Aprovar antes do K01. |
| T1 | K01 | GERAR DO ZERO (ref: âncora Melody + REF-A). **Frame herói.** Pro, com variações. |
| T2 | K02 | GERAR DO ZERO (ref: âncora Melody + REF-A) |
| T3 | K03 | GERAR DO ZERO (ref: âncora Melody + REF-A) |
| T4, T5, T18 a T21 | K04 | GERAR DO ZERO (ref: âncora Melody). Sozinho, sem prop. **Serve os dois blocos.** |
| T6, T7 | K05 | GERAR DO ZERO (ref: âncora Melody). Bancada com os ingredientes. |
| T8 a T17 | K06 | EDITAR do K05 (ingredientes saem, copo pronto na mão) |
| T22 a T29 | K07 | GERAR DO ZERO (ref: âncora Melody + product.png). Frasco na mão. Pro. |

Total: 1 referência + 7 keyframes para 29 takes.

---

## Trava de identidade e continuidade

**Escrita aqui uma vez, não repetir inteira dentro de cada JSON.**

- Rosto do Melody, **homem** negro, cavanhaque e barba aparada, musculoso.
- Longas tranças box braids escuras caindo na frente dos ombros.
- Tatuagem ornamental de manga no braço direito, pequenas tatuagens no peito.
- Regata branca canelada. **Corrente fina de PRATA com cruz de PRATA. Nunca ouro.**
- **EM PÉ** nos setups A a D e G, nunca a pose sentada e relaxada da foto-âncora.
- Garagem dele com **duas âncoras visuais apenas**: o neon vermelho e a bandeira vintage dos EUA. **Nunca inventariar o fundo.**
- Luz quente e baixa de garagem. Zero blur, tudo nítido. Cara de iPhone, nunca polimento de IA.

## Trava dos props da receita (usar no K05 e no K06)

```text
A dark slate board on a plain wooden bench holding four small separate piles: bright yellow-orange turmeric powder, chopped fresh ginger, red cayenne powder, and coarse pink Himalayan salt. Beside the board, a tall clear glass of warm water and one half of a fresh lemon, cut side up. The piles keep the exact same colours and positions in every shot.
```

## Trava do produto (usar no K07)

```text
A white supplement bottle with a purple and white label, about 10 cm tall, held upright in his hand with the label facing the camera. The bottle keeps the exact same size, proportions and label layout as the attached product reference image.
```

## Trava da 2ª pessoa · REF-A · o cliente · gerar e aprovar ANTES do K01

```text
IMPORTANT: THIS IS IPHONE FOOTAGE. Vertical 9:16 real smartphone photo. An ordinary American man around fifty years old stands in a plain garage, facing away from the camera. He is heavier around the middle, with a soft roll of fat at the side of his lower back above the waistband. He wears a plain grey athletic tank top and dark shorts. Real skin with visible pores, body hair, moles and no retouching. His arms hang relaxed at his sides. Warm low indoor light, sharp focus everywhere, no blur. He looks like a real ordinary middle aged man, not a model or an athlete. No captions, no subtitles, no words overlaid on the image, no studio lighting, no plastic skin, no beauty smoothing.
```

Gerar, aprovar o corpo, e usar como referência nos K01, K02 e K03.

---

## GATE DE COMPOSIÇÃO VISUAL (rodado ANTES dos prompts abaixo)

```
HEROI
[x] 1. Heroi no LOWER FOREGROUND mais perto que o rosto
       -> K01/K02/K03: a MAO DELE na area do corpo. K05: os ingredientes. K06: o copo. K07: o frasco
[x] 2. Nada compete com o heroi
[-] 3. Volume e cobertura                 -> nao se aplica, nao ha heroi volumetrico

DISTANCIA
[x] 4. "Da pra estar mais perto?"         -> os tres hooks fecham AINDA MAIS que o original
[x] 5. Pessoas em peito pra cima          -> K04, K06, K07
[x] 6. Take mais fechado e o do CTA       -> K07

FUNDO
[x] 7. Cenario reconhecivel               -> 2 ancoras na garagem
[x] 8. Fundo por enquadramento, nunca blur
[x] 9. Menos elementos

2a PESSOA
[x] 10. 2a pessoa CORTADA pelo quadro     -> ver a decisao abaixo
```

### Uma decisão de composição que MELHORA o original

**O cliente aparece sem rosto identificável nos três hooks.**

No original a cliente aparece de rosto inteiro no take do queixo. Aqui o quadro corta acima da boca nos três keyframes: nas costas ele está de costas, no queixo o corte é logo abaixo do nariz, na barriga só o tronco.

Três motivos:
1. **Identificação.** Corpo anônimo é "qualquer homem de cinquenta", e o espectador se coloca ali. Rosto identificável é "aquele cara", e ele assiste de fora.
2. **O herói ganha o quadro inteiro.** Sem rosto competindo, a mão do Melody na área é a única coisa em cena.
3. **Risco.** Some o rosto de uma pessoa sendo apontada como tendo dano corporal.

É a aplicação do item 10 do gate levada até o fim, e neste vídeo ela é vantagem, não concessão.

---

# Prompts de imagem

## K01 · T1 · HOOK 1 · GERAR DO ZERO (Nano Banana **Pro**, várias variações) · ÂNCORA MELODY + REF-A

```json
{
  "shot_id": "K01_back_roll",
  "context": "Fictional AI-generated characters. No real people are being filmed or depicted.",
  "reference_use": "Use the first attached image ONLY for Melody's face, identity, hair, tattoos and clothing. Use the second attached image ONLY for the client's body and skin so it is clearly the SAME man. Do NOT copy the pose or framing of either reference.",
  "identity_main": "The EXACT MAN from the first reference image (Melody Carter), a male adult: Black man, muscular build, long dark box braids falling in front of the shoulders, trimmed goatee and beard, ornamental tattoo sleeve on his right arm. Only his face, shoulders and hands are in frame, in the upper left of the shot, looking down at the client's back.",
  "wardrobe": "White ribbed tank top, thin SILVER chain with a SILVER cross pendant.",
  "second_person": "The EXACT client from the second reference image: American man around fifty, grey athletic tank top, heavier around the middle. He stands with his back to the camera and is CROPPED by the frame: only his lower back and waist are in shot, from the shoulder blades down to the top of his shorts. His head is above the top edge and is not visible.",
  "scene": "SAME garage as the reference image, with only two visible anchors far behind them: the red neon sign and the vintage American flag. Nothing else competes for attention.",
  "posture": "Melody stands upright behind and slightly to the side of the client, NOT the seated slouch of the reference photo.",
  "composition": "TIGHT close-up on the client's lower back, filling the lower two thirds of the frame. BOTH of Melody's hands are on the soft roll of fat at the side of the client's waist, holding it, and his hands are the closest thing to the lens. Melody's face is small in the upper left corner, looking down at his own hands. The garage behind is barely readable.",
  "camera": "waist level, very close, angled slightly down toward his hands",
  "state": "Start frame: his hands are already holding the roll, he is beginning to speak.",
  "lighting": "Warm low garage light with the red glow of the neon behind them.",
  "realism": "UGC realism, real skin texture with visible pores, body hair, moles, natural imperfection, iPhone-footage look, phone camera look not professional photography, no AI polish, no beauty smoothing, no blur anywhere, everything in sharp focus.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no studio, no plastic skin, no extra fingers, no blur, no gold jewelry, no seated slouch, no woman in frame, no visible face on the client, no third person"
}
```

## K02 · T2 · HOOK 2 · GERAR DO ZERO · ÂNCORA MELODY + REF-A

```json
{
  "shot_id": "K02_chin",
  "reference_use": "Use the first attached image ONLY for Melody's face, identity, hair, tattoos and clothing. Use the second attached image ONLY for the client's skin and build so it is clearly the SAME man. Do NOT copy the pose or framing of either reference.",
  "identity_main": "The EXACT MAN from the first reference image (Melody Carter), a male adult: Black man, long dark box braids falling in front of the shoulders, trimmed goatee and beard, ornamental tattoo sleeve on his right arm. He is beside the client, his face in the left of frame, looking at the client's jaw.",
  "wardrobe": "White ribbed tank top, thin SILVER chain with a SILVER cross pendant.",
  "second_person": "The EXACT client from the second reference image: American man around fifty, grey athletic tank top. He faces the camera but the frame CROPS HIM just below the nose, so only his jaw, chin, soft under-chin and neck are visible. His eyes are above the top edge and are never seen.",
  "scene": "SAME garage as K01, same red neon and vintage flag far behind. Nothing else competes for attention.",
  "posture": "Melody stands upright beside the client, NOT the seated slouch of the reference photo.",
  "composition": "TIGHT close-up on the client's jaw and neck, filling the right two thirds of the frame. Melody's right hand is under the client's chin, thumb and fingers lightly holding the soft area beneath the jaw, and his hand is the closest thing to the lens. Melody's own face is partly visible on the left, looking at his hand.",
  "camera": "chin level, very close, straight-on",
  "state": "Start frame: his hand is already under the client's chin, he is beginning to speak.",
  "lighting": "SAME warm low garage light and red neon glow as K01.",
  "realism": "UGC realism, real skin texture with visible pores, stubble, natural imperfection, iPhone-footage look, phone camera look not professional photography, no AI polish, no beauty smoothing, no blur anywhere, everything in sharp focus.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no studio, no plastic skin, no extra fingers, no blur, no gold jewelry, no seated slouch, no woman in frame, no eyes visible on the client, no third person"
}
```

## K03 · T3 · HOOK 3 · GERAR DO ZERO · ÂNCORA MELODY + REF-A

```json
{
  "shot_id": "K03_belly",
  "reference_use": "Use the first attached image ONLY for Melody's face, identity, hair, tattoos and clothing. Use the second attached image ONLY for the client's body and skin so it is clearly the SAME man. Do NOT copy the pose or framing of either reference.",
  "identity_main": "The EXACT MAN from the first reference image (Melody Carter), a male adult: Black man, long dark box braids falling in front of the shoulders, trimmed goatee and beard, ornamental tattoo sleeve on his right arm. He stands beside the client, his face in the left of frame, looking down at the client's midsection.",
  "wardrobe": "White ribbed tank top, thin SILVER chain with a SILVER cross pendant.",
  "second_person": "The EXACT client from the second reference image: American man around fifty, grey athletic tank top riding slightly up, dark shorts. He faces the camera and is CROPPED by the frame at the chest and at the thighs, so only his belly and waist are in shot. His head is above the top edge and is not visible.",
  "scene": "SAME garage as K01, same red neon and vintage flag far behind. Nothing else competes for attention.",
  "posture": "Melody stands upright beside the client, NOT the seated slouch of the reference photo.",
  "composition": "TIGHT close-up on the client's belly, filling the lower two thirds of the frame. Melody's right index finger is extended and pointing at the client's belly, almost touching it, and his hand is the closest thing to the lens. Melody's face is partly visible on the left, looking at where he points.",
  "camera": "waist level, very close, angled slightly down toward the belly",
  "state": "Start frame: his finger is already pointing, he is beginning to speak.",
  "lighting": "SAME warm low garage light and red neon glow as K01.",
  "realism": "UGC realism, real skin texture with visible pores, body hair, natural imperfection, iPhone-footage look, phone camera look not professional photography, no AI polish, no beauty smoothing, no blur anywhere, everything in sharp focus.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no studio, no plastic skin, no extra fingers, no blur, no gold jewelry, no seated slouch, no woman in frame, no visible face on the client, no third person"
}
```

## K04 · T4, T5, T18 a T21 · GERAR DO ZERO · ÂNCORA MELODY

```json
{
  "shot_id": "K04_melody_alone",
  "reference_use": "Use the attached image ONLY for Melody's face, identity, hair, tattoos and clothing. Do NOT copy its pose or framing.",
  "identity_main": "The EXACT MAN from the reference image (Melody Carter), a male adult: Black man, muscular build, long dark box braids falling in front of the shoulders, trimmed goatee and beard, ornamental tattoo sleeve on his right arm, small chest tattoos.",
  "wardrobe": "White ribbed tank top, thin SILVER chain with a SILVER cross pendant.",
  "scene": "SAME garage as the reference image, with only two visible anchors: the red neon sign and the vintage American flag. Nothing else competes for attention.",
  "posture": "Standing upright, close to the lens, chin level, NOT the seated slouch of the reference photo, no legs or lap in frame.",
  "composition": "TIGHT chest-up framing, close to the lens, his head and shoulders filling most of the frame, cropped at the top of his head. NOTHING in his hands. His right hand comes up into the bottom of frame in a natural open gesture.",
  "camera": "chest level, straight-on, close",
  "state": "Start frame: speaking directly into the lens, calm and direct.",
  "lighting": "Warm low garage light with the red glow of the neon behind him.",
  "realism": "UGC realism, real skin texture with visible pores, individual hair strands, subtle wrinkles, realistic shadows and reflections, iPhone-footage look, phone camera look not professional photography, no AI polish, no beauty smoothing, no blur anywhere, everything in sharp focus.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no studio, no plastic skin, no extra fingers, no blur, no gold jewelry, no seated slouch, no second person, no props"
}
```

## K05 · T6, T7 · RECEITA · GERAR DO ZERO · ÂNCORA MELODY

```json
{
  "shot_id": "K05_recipe_bench",
  "reference_use": "Use the attached image ONLY for Melody's face, identity, hair, tattoos and clothing. Do NOT copy its pose or framing.",
  "identity_main": "The EXACT MAN from the reference image (Melody Carter), a male adult: Black man, muscular build, long dark box braids falling in front of the shoulders, trimmed goatee and beard, ornamental tattoo sleeve on his right arm.",
  "wardrobe": "White ribbed tank top, thin SILVER chain with a SILVER cross pendant.",
  "prop": "A dark slate board on the bench holding four small separate piles: bright yellow-orange turmeric powder, chopped fresh ginger, red cayenne powder, and coarse pink Himalayan salt. Beside the board, a tall clear glass of warm water and one half of a fresh lemon, cut side up.",
  "scene": "SAME garage as the reference image, with only two visible anchors far behind: the red neon sign and the vintage American flag. A plain wooden bench in front of him.",
  "posture": "Standing upright behind the bench, leaning slightly forward, NOT the seated slouch of the reference photo.",
  "composition": "TIGHT waist-up, close. The slate board and the glass fill the lower foreground, closer to the lens than his face, and are unmistakably the hero. His right hand is above the board, fingers pinching a little turmeric, about to drop it into the glass. Nothing has been added to the water yet.",
  "camera": "chest level, close, angled slightly high toward the board and the glass",
  "state": "Start frame: the water in the glass is still completely clear, nothing added yet, his fingers are just above it.",
  "lighting": "Warm low garage light with the red glow of the neon behind him.",
  "realism": "UGC realism, real skin texture with visible pores, individual hair strands, realistic shadows and reflections, iPhone-footage look, phone camera look not professional photography, no AI polish, no beauty smoothing, no blur anywhere, everything in sharp focus.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no studio, no plastic skin, no extra fingers, no blur, no gold jewelry, no seated slouch, no second person, no coloured water"
}
```

## K06 · T8 a T17 · A BEBIDA PRONTA · EDITAR do K05

```json
{
  "task": "edit the attached image, keep everything identical except the changes listed",
  "keep_identical": "Keep the man exactly the same: same face, same box braids, same tattoos, same white tank top, same silver cross, same standing posture. Keep the SAME background exactly: bench, red neon, flag, same lighting, same camera angle and framing.",
  "change_1": "Remove the slate board, the four piles and the lemon half from the bench completely.",
  "change_2": "The glass is no longer on the bench. He now holds it up in his right hand at chest height, closer to the lens than his face. The water inside is now a cloudy warm golden-orange, with fine darker specks of spice suspended in it.",
  "change_3": "His left hand is open near his chest in a natural mid-gesture and he speaks directly into the lens.",
  "realism": "UGC realism, real skin texture with visible pores, iPhone-footage look, no AI polish, no beauty smoothing, no blur anywhere. Do not make his skin darker, yellowish or orangish. Do not make the colors more saturated.",
  "negative": "do not change the face, do not change identity, do not change the background, do not change the camera angle, no captions, no subtitles, no words overlaid on the image, no plastic skin, no extra fingers, no gold jewelry, no straw, no garnish"
}
```

## K07 · T22 a T29 · PRODUTO E CTA · GERAR DO ZERO (Nano Banana **Pro**) · ÂNCORA MELODY + PRODUCT.PNG

```json
{
  "shot_id": "K07_melody_product",
  "reference_use": "Use the first attached image ONLY for Melody's face, identity, hair, tattoos and clothing. Use the second attached image ONLY for the exact shape, size, proportions and label layout of the bottle. Do NOT copy the pose or framing of either reference. This must be the CLOSEST framing of the entire video.",
  "identity_main": "The EXACT MAN from the first reference image (Melody Carter), a male adult: Black man, muscular build, long dark box braids falling in front of the shoulders, trimmed goatee and beard, ornamental tattoo sleeve on his right arm, small chest tattoos.",
  "wardrobe": "White ribbed tank top, thin SILVER chain with a SILVER cross pendant.",
  "product": "The EXACT white supplement bottle from the second reference image, with its purple and white label, about 10 cm tall. He holds it upright in his right hand at chest height, label turned squarely toward the lens, closer to the camera than his own face and clearly the hero of the frame.",
  "scene": "SAME garage as K04, same red neon and vintage flag behind him.",
  "posture": "Standing upright, very close to the lens, chin up, shoulders squared, NOT the seated slouch of the reference photo.",
  "composition": "TIGHT chest-up close-up, the tightest framing in the whole video. His head and shoulders fill the upper frame and the bottle sits in the lower foreground, closer to the lens than his face.",
  "camera": "chest level, straight-on, very close, angled slightly toward the bottle",
  "state": "Start frame: bottle already raised and steady, speaking straight into the lens.",
  "lighting": "SAME warm low garage light and red neon glow as K04.",
  "realism": "UGC realism, real skin texture with visible pores, individual hair strands, subtle wrinkles, realistic shadows and reflections, iPhone-footage look, phone camera look not professional photography, no AI polish, no beauty smoothing, no blur anywhere, everything in sharp focus.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no studio, no plastic skin, no extra fingers, no blur, no gold jewelry, no seated slouch, no second bottle, no second person"
}
```

---

# Prompts de vídeo (Veo 3.1 via Flow)

## Bloco global

Colar em todo prompt:

```text
o avatar (homem) fala em inglês com sotaque americano de homem negro, voz autêntica, dinâmica, apaixonada e emocional, como se exigisse ser ouvido.

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

Estilo TikTok nativo, UGC. Preservar exatamente a identidade do Melody, HOMEM, rosto, box braids, cavanhaque, tatuagens, regata branca, cruz de PRATA, a garagem, a iluminação e o enquadramento do frame inicial. Sem legenda, sem texto gerado, sem música, sem pessoas extras.
```

**Nos V01, V02 e V03 o cliente não fala e não se mexe.** Ele é objeto da demonstração, nunca participante.

---

### V01 · T1 · usa K01
```text
o avatar (homem) fala em inglês com sotaque americano de homem negro, voz firme e direta, a seguinte frase: "This is sugar damage."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ele aperta de leve o rolinho na lateral da cintura do cliente duas vezes enquanto fala. O cliente permanece parado de costas, sem se mexer e sem falar.

câmera: fixa, leve handheld natural

som ambiente: garagem silenciosa, sem música, sem ruído de fundo
```

### V02 · T2 · usa K02
```text
o avatar (homem) fala em inglês com sotaque americano de homem negro, voz firme e direta, a seguinte frase: "This is sugar damage."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ele move de leve a mão sob o queixo do cliente enquanto fala. O cliente permanece parado, sem falar.

câmera: fixa, leve handheld natural

som ambiente: garagem silenciosa, sem música, sem ruído de fundo
```

### V03 · T3 · usa K03
```text
o avatar (homem) fala em inglês com sotaque americano de homem negro, voz firme e direta, a seguinte frase: "This is sugar damage."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ele bate o dedo indicador duas vezes na barriga do cliente enquanto fala. O cliente permanece parado, sem falar.

câmera: fixa, leve handheld natural

som ambiente: garagem silenciosa, sem música, sem ruído de fundo
```

### V04 · T4 · usa K04
```text
o avatar (homem) fala em inglês com sotaque americano de homem negro, voz autêntica, dinâmica e emocional, a seguinte frase: "And the best thing to fix sugar damage is not cutting carbs, not drinking more water, and it is definitely not willpower."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: corte duro. ele conta três itens nos dedos da mão direita enquanto fala e descarta cada um com um gesto curto.

câmera: fixa, leve handheld natural

som ambiente: garagem silenciosa, sem música, sem ruído de fundo
```

### V05 · T5 · usa K04
```text
o avatar (homem) fala em inglês com sotaque americano de homem negro, voz autêntica e confiante, a seguinte frase: "Let me show you what actually works."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ele abre a mão na direção da câmera num gesto de convite e se inclina um pouco pra frente.

câmera: fixa, leve push-in

som ambiente: garagem silenciosa, sem música, sem ruído de fundo
```

### V06 · T6 · usa K05
```text
o avatar (homem) fala em inglês com sotaque americano de homem negro, voz autêntica e direta, a seguinte frase: "In a glass of warm water, add turmeric, chopped ginger, and a pinch of cayenne."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ele solta a cúrcuma no copo, depois pega o gengibre picado e solta, depois pega a cayenne e solta. A água fica alaranjada e turva conforme cada item cai.

câmera: fixa, leve handheld natural

som ambiente: garagem silenciosa, sem música, sem ruído de fundo
```

### V07 · T7 · usa K05
```text
o avatar (homem) fala em inglês com sotaque americano de homem negro, voz autêntica e direta, a seguinte frase: "Then a pinch of Himalayan salt, and squeeze in half a lemon."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ele solta o sal no copo e depois espreme a metade do limão sobre a bebida, com o suco caindo dentro.

câmera: fixa, leve handheld natural

som ambiente: garagem silenciosa, sem música, sem ruído de fundo
```

### V08 · T8 · usa K06
```text
o avatar (homem) fala em inglês com sotaque americano de homem negro, voz autêntica e direta, a seguinte frase: "Drink it on an empty stomach every single morning."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ele ergue o copo pronto na direção da câmera e o mantém firme enquanto fala.

câmera: fixa, leve handheld natural

som ambiente: garagem silenciosa, sem música, sem ruído de fundo
```

### V09 · T9 · usa K06
```text
o avatar (homem) fala em inglês com sotaque americano de homem negro, voz autêntica, dinâmica e emocional, a seguinte frase: "The turmeric kills the inflammation that sugar has been building in your gut for years."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ele aponta pro copo com a mão livre ao dizer o nome do ingrediente e depois fecha a mão.

câmera: fixa, leve handheld natural

som ambiente: garagem silenciosa, sem música, sem ruído de fundo
```

### V10 · T10 · usa K06
```text
o avatar (homem) fala em inglês com sotaque americano de homem negro, voz autêntica, dinâmica e emocional, a seguinte frase: "The ginger breaks down what has been sitting in there. The cayenne fires through whatever is left."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ele faz um gesto de quebrar com a mão livre na primeira frase e um gesto rápido pra frente na segunda.

câmera: fixa, leve handheld natural

som ambiente: garagem silenciosa, sem música, sem ruído de fundo
```

### V11 · T11 · usa K06
```text
o avatar (homem) fala em inglês com sotaque americano de homem negro, voz autêntica, dinâmica e emocional, a seguinte frase: "And the salt rehydrates your gut lining so your body can absorb real nutrients again."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ele abre a mão livre com a palma pra cima num gesto de explicação enquanto fala.

câmera: fixa, leve handheld natural

som ambiente: garagem silenciosa, sem música, sem ruído de fundo
```

### V12 · T12 · usa K06
```text
o avatar (homem) fala em inglês com sotaque americano de homem negro, voz que abre e fica mais leve, a seguinte frase: "The cravings quiet down. The brain fog clears. The belly that has been stuck for years finally starts to move."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ele conta três coisas no ar com a mão livre, uma pra cada frase, e a expressão dele vai abrindo.

câmera: fixa, leve handheld natural

som ambiente: garagem silenciosa, sem música, sem ruído de fundo
```

### V13 · T13 · usa K06
```text
o avatar (homem) fala em inglês com sotaque americano de homem negro, voz mais baixa e confidencial, a seguinte frase: "But here is what nobody tells you about the craving itself. Your body is not weak for wanting it."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ele baixa um pouco o copo e balança a cabeça devagar na última frase.

câmera: fixa, leve push-in

som ambiente: garagem silenciosa, sem música, sem ruído de fundo
```

### V14 · T14 · usa K06
```text
o avatar (homem) fala em inglês com sotaque americano de homem negro, voz autêntica, dinâmica e emocional, a seguinte frase: "It is asking for fast fuel because it thinks you are in danger. That is cortisol talking."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ele aponta pro próprio peito ao dizer que o corpo acha que está em perigo e depois levanta um dedo na última frase.

câmera: fixa, leve handheld natural

som ambiente: garagem silenciosa, sem música, sem ruído de fundo
```

### V15 · T15 · usa K06
```text
o avatar (homem) fala em inglês com sotaque americano de homem negro, voz autêntica, dinâmica e emocional, a seguinte frase: "Cortisol locks you in survival mode, and survival mode wants sugar right now, not in an hour."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ele faz um gesto de trancar com a mão livre e depois bate o dedo na palma ao dizer "right now".

câmera: fixa, leve handheld natural

som ambiente: garagem silenciosa, sem música, sem ruído de fundo
```

### V16 · T16 · usa K06
```text
o avatar (homem) fala em inglês com sotaque americano de homem negro, voz firme, quase de alívio, a seguinte frase: "That is why willpower never worked. You were not fighting a habit. You were fighting a hormone."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ele para de gesticular nas duas frases curtas e olha fixo pra câmera.

câmera: fixa, leve push-in

som ambiente: garagem silenciosa, sem música, sem ruído de fundo
```

### V17 · T17 · usa K06
```text
o avatar (homem) fala em inglês com sotaque americano de homem negro, voz autêntica e direta, a seguinte frase: "The drink calms the gut. It does not touch the hormone that keeps ordering the sugar."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ele ergue o copo na primeira frase e depois o baixa devagar na segunda.

câmera: fixa, leve handheld natural

som ambiente: garagem silenciosa, sem música, sem ruído de fundo
```

### V18 · T18 · usa K04
```text
o avatar (homem) fala em inglês com sotaque americano de homem negro, voz autêntica e direta, a seguinte frase: "And buying all of this separately every week is expensive."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: corte duro, o copo sumiu. ele esfrega o polegar no indicador num gesto de dinheiro enquanto fala.

câmera: fixa, leve handheld natural

som ambiente: garagem silenciosa, sem música, sem ruído de fundo
```

### V19 · T19 · usa K04
```text
o avatar (homem) fala em inglês com sotaque americano de homem negro, voz autêntica e direta, a seguinte frase: "Nobody actually sticks with it. You and I both know that."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ele levanta as sobrancelhas na última frase e dá um meio sorriso de cumplicidade.

câmera: fixa, leve handheld natural

som ambiente: garagem silenciosa, sem música, sem ruído de fundo
```

### V20 · T20 · usa K04
```text
o avatar (homem) fala em inglês com sotaque americano de homem negro, voz de alerta, a seguinte frase: "And the saffron on most shelves sat under warehouse lights for a year. The actives die in light and heat."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ele aponta pra cima como quem indica uma luz de teto na primeira frase e depois abre a mão na segunda.

câmera: fixa, leve handheld natural

som ambiente: garagem silenciosa, sem música, sem ruído de fundo
```

### V21 · T21 · usa K04
```text
o avatar (homem) fala em inglês com sotaque americano de homem negro, voz firme e curta, a seguinte frase: "You are buying a ghost of it."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ele abre as duas mãos vazias na frente do corpo e para o gesto no fim da frase.

câmera: fixa, leve push-in

som ambiente: garagem silenciosa, sem música, sem ruído de fundo
```

### V22 · T22 · usa K07
```text
o avatar (homem) fala em inglês com sotaque americano de homem negro, voz autêntica e confiante, a seguinte frase: "That is why I put my clients on Korella Saffron."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: corte duro. ele ergue o frasco na direção da câmera ao dizer o nome do produto e o mantém firme.

câmera: fixa, leve push-in

som ambiente: garagem silenciosa, sem música, sem ruído de fundo
```

### V23 · T23 · usa K07
```text
o avatar (homem) fala em inglês com sotaque americano de homem negro, voz autêntica e direta, a seguinte frase: "Pure extract, eighty eight point five milligrams, sealed dark so the actives are still alive when it reaches you."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ele gira o frasco de leve mostrando o rótulo e aponta pra ele com o dedo enquanto fala.

câmera: fixa, leve handheld natural

som ambiente: garagem silenciosa, sem música, sem ruído de fundo
```

### V24 · T24 · usa K07
```text
o avatar (homem) fala em inglês com sotaque americano de homem negro, voz leve e prática, a seguinte frase: "One capsule in the morning. Thirty seconds and you are done."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ele encolhe os ombros de leve na última frase, mantendo o frasco erguido.

câmera: fixa, leve handheld natural

som ambiente: garagem silenciosa, sem música, sem ruído de fundo
```

### V25 · T25 · usa K07
```text
o avatar (homem) fala em inglês com sotaque americano de homem negro, voz mais leve e satisfeita, a seguinte frase: "Within a few weeks the same two things come back. The cravings stop, and the energy shows up again."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ele conta duas coisas no ar com a mão livre enquanto fala.

câmera: fixa, leve handheld natural

som ambiente: garagem silenciosa, sem música, sem ruído de fundo
```

### V26 · T26 · usa K07
```text
o avatar (homem) fala em inglês com sotaque americano de homem negro, voz firme, com uma pausa entre as duas frases, a seguinte frase: "They did not quit sugar. Sugar quit them."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ele para completamente entre as duas frases e depois abre um meio sorriso na segunda.

câmera: fixa, leve push-in

som ambiente: garagem silenciosa, sem música, sem ruído de fundo
```

### V27 · T27 · usa K07
```text
o avatar (homem) fala em inglês com sotaque americano de homem negro, voz firme e conclusiva, a seguinte frase: "It is on Amazon, and it is what finally gets your body out of survival mode."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ele ergue o frasco um pouco mais alto e o mantém parado até o fim da frase.

câmera: fixa, leve push-in

som ambiente: garagem silenciosa, sem música, sem ruído de fundo
```

### V28 · T28 · usa K07
```text
o avatar (homem) fala em inglês com sotaque americano de homem negro, voz direta, a seguinte frase: "Comment yes below and I will send you the link."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ele aponta pra baixo, na direção dos comentários, mantendo o frasco na outra mão.

câmera: fixa, leve push-in

som ambiente: garagem silenciosa, sem música, sem ruído de fundo
```

### V29 · T29 · usa K07
```text
o avatar (homem) fala em inglês com sotaque americano de homem negro, voz direta, a seguinte frase: "Just make sure you are following me, otherwise it will not let the message through."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ele aponta uma vez pra câmera, direto, e termina com um aceno curto de cabeça.

câmera: fixa, leve push-in

som ambiente: garagem silenciosa, sem música, sem ruído de fundo
```

---

## Mapa de âncoras

| Keyframe | Referências a anexar | Modelo |
|---|---|---|
| REF-A | nenhuma, gerar do zero | Nano Banana 2, regenerar até corpo crível de homem 50 |
| K01 | âncora Melody + REF-A aprovada | Nano Banana **Pro**, várias variações |
| K02 | âncora Melody + REF-A aprovada | Nano Banana 2 |
| K03 | âncora Melody + REF-A aprovada | Nano Banana 2 |
| K04 | âncora Melody | Nano Banana 2 |
| K05 | âncora Melody | Nano Banana 2 |
| K06 | K05 aprovado | Nano Banana 2, comando de edição |
| K07 | **âncora Melody + product.png** | Nano Banana **Pro** (o rótulo precisa sair legível) |

---

## Montagem no CapCut

- Timeline 1080x1920, 30 fps. Cortes duros entre todos os takes.
- **Os três primeiros cortes são o ritmo do hook.** V01, V02 e V03 têm uns 2 segundos cada. Cortar rente à fala, sem respiro entre eles. O staccato é o que segura o scroll.
- **Três cortes de peso:** V03 para V04 (sai o cliente, entra ele sozinho), V17 para V18 (some o copo) e V21 para V22 (entra o produto).
- **Ícones riscados em PiP no V04**, um pra cada negação: carboidrato, copo de água, e um terceiro pra força de vontade. Entram na EDIÇÃO, nunca na geração.
- Cortar o silêncio inicial de cada clipe.
- **Segurar um beat de silêncio entre as duas frases do V26.** "They did not quit sugar" e depois a virada.
- Legendas grandes estilo Captions.ai Prism Pro, palavra destacada em vermelho, na altura do peito. **Nos V01 a V03 a legenda não pode cobrir a mão dele na área do corpo**, que é o herói. E nunca cobrir o rótulo do frasco de V22 em diante.
- Manter `YES` isolado na tela no CTA.
- Color grading: temp +4, tint 0, saturação -4, exposição -3, contraste +14, highlight -30, shadow +20, fade +4.

## Gates de qualidade

1. **Melody é HOMEM em todos os clipes.**
2. Mesmo homem em todos, cruz de **PRATA** sempre, nunca ouro.
3. Box braids iguais em todos os planos e ele **em pé** em todos.
4. **O cliente é HOMEM** e é o mesmo do REF-A nos três hooks.
5. **O cliente não tem rosto identificável em nenhum dos três hooks.** Se apareceram os olhos, regenerar.
6. **A mão do Melody é a coisa mais perto da lente nos K01, K02 e K03.**
7. Os quatro montinhos da tábua têm as mesmas cores e posições no K05.
8. **A água está limpa no K05 e alaranjada no K06.** Se o K05 saiu com água colorida, regenerar.
9. Nenhuma legenda, ícone ou texto foi gerado dentro da imagem. Tudo entra na edição.
10. **O frasco do K07 bate com o product.png** e aparece de T22 a T29.
11. **O K07 é o plano mais fechado do vídeo inteiro.**
12. Fundo reconhecível e não inventariado: duas âncoras na garagem.
13. Nenhuma imagem com fundo desfocado.
14. Mãos com cinco dedos, sem fusão com o corpo do cliente, com o copo nem com o frasco.
15. `yes` e o follow gate estão os dois no CTA final. **O original não tem follow gate, o nosso tem.**
