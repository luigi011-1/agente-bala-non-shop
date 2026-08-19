# holistic.brandon | Ângulo 2 (FityWell) | Pacote de Prompts

Vídeo modelo: `531403f2-4826-4586-8ba1-02906c2a73d0.mp4`

Âncora de identidade: `C:\Users\luigi\Desktop\AVATARES NON-SHOP\holistic.brandon .png`

Funil: comment `yes` -> DM -> link do quiz FityWell

---

## Índice de geração

| Take | Keyframe | Ação de geração |
|---|---|---|
| ref | REF-A | GERAR DO ZERO a 2ª pessoa (mulher 40+). Aprovar rosto antes de tudo. |
| T1 | K01 | GERAR DO ZERO (ref: âncora Brandon + REF-A aprovada). Frame herói, gerar no Pro com variações. |
| T2 | K02 | EDITAR do K01 (muda só a distância de câmera e a mão livre) |
| T3, T6, T9 | K03 | GERAR DO ZERO (ref: âncora Brandon) |
| T4, T7, T11 | K04 | EDITAR do K03 (muda só o gesto de mão) |
| T5, T8, T10, T12 | K05 | EDITAR do K03 (muda só o gesto de mão) |
| T13, T14 | K06 | GERAR DO ZERO (ref: âncora Brandon). Celular com tela apagada. |
| T15 | K07 | EDITAR do K06 (muda só o braço direito, apontando) |

Total: 1 referência + 7 keyframes para 15 takes.

---

## Trava de identidade e continuidade

Aplicar em toda imagem e todo clipe:

- Preservar exatamente o rosto da Brandon, pele mestiça clara com sardas suaves, olhos castanhos, cornrows para trás com pontas trançadas soltas caindo na frente dos ombros e miçangas de madeira e âmbar nas pontas.
- Manga de tatuagem floral blackwork de linha fina cobrindo o braço do lado esquerdo do quadro. Pequena tatuagem de folha na clavícula e pequena tatuagem escrita no antebraço do lado direito do quadro.
- Regata branca canelada e shorts de treino cinza escuro. **Corrente fina de OURO com pingente de cruz de OURO.** Nunca prata.
- Mesma box de treino em todos os planos: parede de bloco de concreto cinza claro, neon vermelho `TRAIN PRAY REPEAT`, bandeira vintage dos EUA, quadro branco `STAY READY. STAY DISCIPLINED.` com as três linhas, estante preta de metal com potes de vidro de ervas e sementes, teto de ripas de madeira avermelhada.
- A sinalização da parede é canônica e deve continuar existindo. O que não pode aparecer é legenda ou palavra sobreposta na imagem.
- Luz natural difusa de galpão. Zero blur, tudo em foco nítido incluindo parede e prateleira. Cara de vídeo de iPhone, nunca polimento de IA.

---

## Trava do prop herói (usar em K01 e K02)

```text
A clean classroom-style anatomical teaching plaque of a female midsection from the ribs down to the hips, molded in soft matte cream-toned silicone, mounted upright on a white rectangular base with two thin metal posts. The belly of the plaque is clearly swollen and rounded outward. An oval cutaway window in the center of the abdomen exposes a pale matte silicone digestive tube that is packed tight and completely blocked with compacted dried material in dusty beige and muted dusty rose, cracked on the surface like dried clay. The whole object looks like a calm educational teaching aid from a health classroom. The shape, size, colors and internal detail must stay identical in every shot.
```

## Trava da 2ª pessoa (REF-A) — gerar e aprovar ANTES do K01

```text
IMPORTANT: THIS IS IPHONE FOOTAGE. Vertical 9:16 real smartphone photo. An ordinary American woman in her mid forties stands facing the camera in a plain concrete-block gym. She has shoulder-length dark brown hair tied back, warm medium skin, visible pores, fine lines around the eyes, natural facial asymmetry, no makeup and no retouching. She wears a simple black sports bra and dark gray leggings. Her lower belly is visibly swollen and distended, which is the honest reason she is in the shot. Her arms hang relaxed at her sides and her expression is neutral and slightly self-conscious, looking slightly down and away from the lens. Soft neutral daylight, sharp focus everywhere, no blur. She looks like a real ordinary woman, not a model and not a celebrity. No captions, no subtitles, no words overlaid on the image, no studio lighting, no plastic skin, no beauty smoothing.
```

Gerar, aprovar o rosto, e usar essa imagem como referência da 2ª pessoa no K01.

---

# Prompts de imagem

## K01 · T1 · HOOK · GERAR DO ZERO (Nano Banana **Pro**, várias variações)

Anexar: âncora da Brandon + REF-A aprovada + a trava do prop herói.

```json
{
  "shot_id": "K01_hook_initial",
  "reference_use": "Use the first attached image ONLY for Brandon's face, identity, hair, tattoos, wardrobe and the gym scene. Use the second attached image ONLY for the second woman's face so it is clearly the SAME woman. Do NOT copy the pose or framing of either reference.",
  "identity_main": "The EXACT woman from the first reference image (Brandon): mixed-race Black American woman, athletic build, light-medium skin with soft freckles, brown eyes, cornrows braided back with loose braided ends falling in front of the shoulders and wooden and amber beads on the tips, fine-line floral blackwork sleeve on the arm on the left side of frame, small leaf tattoo on the collarbone.",
  "wardrobe": "White ribbed tank top, dark gray training shorts, thin GOLD chain with a GOLD cross pendant.",
  "second_person": "The EXACT woman from the second reference image: American woman in her mid forties, black sports bra and dark gray leggings, visibly swollen lower belly. She stands close beside Brandon on the right, and the frame CROPS her: only her torso from collarbone to upper thigh is in shot, her head is above the top edge and part of her body is cut by the right edge. Her swollen belly is what is visible and it sits right next to the plaque. Her arms hang relaxed. She does not touch the plaque.",
  "prop": "A clean classroom-style anatomical teaching plaque of a female midsection from the ribs down to the hips, molded in soft matte cream-toned silicone, mounted upright on a white rectangular base with two thin metal posts. The belly of the plaque is clearly swollen and rounded outward. An oval cutaway window in the center of the abdomen exposes a pale matte silicone digestive tube packed tight and completely blocked with compacted dried material in dusty beige and muted dusty rose, cracked on the surface like dried clay. It looks like a calm educational teaching aid.",
  "scene": "SAME concrete-block gym as the reference image: light gray cinderblock wall, red neon sign reading TRAIN PRAY REPEAT, vintage American flag, white board reading STAY READY. STAY DISCIPLINED., black metal shelf with glass jars of herbs and seeds, reddish wooden slat ceiling.",
  "posture": "Brandon stands upright facing the camera, holding the plaque vertically with both hands in front of her own midsection, at the height of her own waist and hips.",
  "composition": "VERY CLOSE, almost close-up. The camera is right on top of the plaque. The plaque fills most of the frame and is much closer to the lens than everything else, so it is unmistakably the hero. Brandon's face is visible in the upper third of the frame, cropped at the top of her head. Nothing else competes for attention. The gym behind is barely readable, just enough to recognize the place.",
  "camera": "chest level, straight-on, camera pushed in very close to the plaque, tight framing",
  "state": "Start frame: Brandon holds the plaque steady and looks directly into the lens, about to speak.",
  "lighting": "Soft neutral daylight of an open gym, warm red glow from the neon on the wall.",
  "realism": "UGC realism, real skin texture with visible pores, individual hair strands, subtle wrinkles, realistic shadows and reflections, iPhone-footage look, phone camera look not professional photography, no AI polish, no beauty smoothing, no blur anywhere, everything in sharp focus including background wall shelf and signage.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no studio, no plastic skin, no extra fingers, no supernatural lighting, no blur, no artificial lighting, no silver jewelry, no third person"
}
```

## K02 · T2 · HOOK · EDITAR do K01

```json
{
  "task": "edit the attached image, keep everything identical except the changes listed",
  "keep_identical": "Keep both women exactly the same: same faces, same hair, same tattoos, same wardrobe, same gold cross, same body positions. Keep the SAME anatomical plaque with the same shape, swelling and internal detail. Keep the SAME background exactly: cinderblock wall, neon sign, flag, white board, shelf, same lighting.",
  "change_1": "Push the camera even closer to the plaque so the framing tightens by about twenty percent and the cutaway window of the plaque becomes the dominant element of the frame. Do not change the angle or the height of the camera.",
  "change_2": "Brandon now holds the plaque with her left hand only, and her right hand is raised beside the plaque with the index finger extended in a small counting gesture.",
  "realism": "UGC realism, real skin texture with visible pores, iPhone-footage look, no AI polish, no beauty smoothing, no blur anywhere. Do not make their skin darker, yellowish or orangish. Do not make the colors more saturated.",
  "negative": "do not change the faces, do not change identities, do not change the background, do not change the plaque, no captions, no subtitles, no words overlaid on the image, no plastic skin, no extra fingers, no silver jewelry"
}
```

## K03 · T3, T6, T9 · TALKING HEAD · GERAR DO ZERO

```json
{
  "shot_id": "K03_talking_a",
  "reference_use": "Use the attached image ONLY for Brandon's face, identity, hair, tattoos, wardrobe and the gym scene. Do NOT copy its pose or framing.",
  "identity_main": "The EXACT woman from the reference image (Brandon): mixed-race Black American woman, athletic build, light-medium skin with soft freckles, brown eyes, cornrows braided back with loose braided ends falling in front of the shoulders and wooden and amber beads on the tips, fine-line floral blackwork sleeve on the arm on the left side of frame, small leaf tattoo on the collarbone.",
  "wardrobe": "White ribbed tank top, dark gray training shorts, thin GOLD chain with a GOLD cross pendant.",
  "scene": "SAME concrete-block gym as the reference image, standing against the light gray cinderblock wall with the red TRAIN PRAY REPEAT neon and the vintage American flag visible behind her.",
  "posture": "Standing upright, close to the camera, chin level, direct and warm expression.",
  "composition": "VERY CLOSE, almost close-up. Shoulders-up framing, her face fills a large part of the frame and the top of her head is cropped by the top edge. Her left arm is extended toward the bottom left corner of the frame because that hand is holding the phone that is filming. Her right hand comes up into the bottom of the frame at chest height in a natural open gesture. Very little of the gym is visible, just the wall and a hint of the neon behind her.",
  "camera": "eye level, straight-on, close selfie distance with the phone held near the face",
  "state": "Start frame: speaking directly into the lens.",
  "lighting": "Soft neutral daylight of an open gym, warm red glow from the neon behind her.",
  "realism": "UGC realism, real skin texture with visible pores, individual hair strands, subtle wrinkles, realistic shadows and reflections, iPhone-footage look, phone camera look not professional photography, no AI polish, no beauty smoothing, no blur anywhere, everything in sharp focus including the background wall and signage.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no studio, no plastic skin, no extra fingers, no supernatural lighting, no blur, no artificial lighting, no silver jewelry, no second person, no props"
}
```

## K04 · T4, T7, T11 · EDITAR do K03

```json
{
  "task": "edit the attached image, keep everything identical except the change listed",
  "keep_identical": "Keep Brandon exactly the same: same face, same hair and beads, same tattoos, same white tank top, same gold cross, same body position, same extended left arm holding the phone. Keep the SAME background exactly: cinderblock wall, neon sign, flag, same lighting, same camera angle and framing.",
  "change_1": "Her right hand is now open with the palm turned upward at chest height, in a calm explaining gesture. Her eyebrows are slightly raised and her expression is more emphatic.",
  "realism": "UGC realism, real skin texture with visible pores, iPhone-footage look, no AI polish, no beauty smoothing, no blur anywhere. Do not make her skin darker, yellowish or orangish. Do not make the colors more saturated.",
  "negative": "do not change the face, do not change identity, do not change the background, do not change the extended left arm, do not change the camera angle, no captions, no subtitles, no words overlaid on the image, no plastic skin, no extra fingers, no silver jewelry"
}
```

## K05 · T5, T8, T10, T12 · EDITAR do K03

```json
{
  "task": "edit the attached image, keep everything identical except the change listed",
  "keep_identical": "Keep Brandon exactly the same: same face, same hair and beads, same tattoos, same white tank top, same gold cross, same body position, same extended left arm holding the phone. Keep the SAME background exactly: cinderblock wall, neon sign, flag, same lighting, same camera angle and framing.",
  "change_1": "Her right hand is now closed in a light loose fist at chest height, held in a firm and serious gesture. Her expression is direct and a little harder, like she is stating a fact she is tired of repeating.",
  "realism": "UGC realism, real skin texture with visible pores, iPhone-footage look, no AI polish, no beauty smoothing, no blur anywhere. Do not make her skin darker, yellowish or orangish. Do not make the colors more saturated.",
  "negative": "do not change the face, do not change identity, do not change the background, do not change the extended left arm, do not change the camera angle, no captions, no subtitles, no words overlaid on the image, no plastic skin, no extra fingers, no silver jewelry"
}
```

## K06 · T13, T14 · PRODUTO · GERAR DO ZERO

Tela do celular fica **apagada**. O print do quiz entra no CapCut.

```json
{
  "shot_id": "K06_product",
  "reference_use": "Use the attached image ONLY for Brandon's face, identity, hair, tattoos, wardrobe and the gym scene. Do NOT copy its pose or framing.",
  "identity_main": "The EXACT woman from the reference image (Brandon): mixed-race Black American woman, athletic build, light-medium skin with soft freckles, brown eyes, cornrows braided back with loose braided ends falling in front of the shoulders and wooden and amber beads on the tips, fine-line floral blackwork sleeve on the arm on the left side of frame, small leaf tattoo on the collarbone.",
  "wardrobe": "White ribbed tank top, dark gray training shorts, thin GOLD chain with a GOLD cross pendant.",
  "scene": "SAME concrete-block gym as the reference image, standing against the light gray cinderblock wall with the red TRAIN PRAY REPEAT neon and the vintage American flag visible behind her.",
  "posture": "Standing upright, close to the camera, direct and confident expression.",
  "composition": "VERY CLOSE, almost close-up. Shoulders-up framing, the top of her head cropped by the top edge. Her left arm is extended toward the bottom left corner of the frame because that hand is holding the phone that is filming. In her right hand she holds up a second ordinary black smartphone right beside her face, pushed well forward toward the lens so it is clearly closer to the camera than her face and reads as the hero object, without covering her eyes or mouth. Very little of the gym is visible.",
  "camera": "eye level, straight-on, close selfie distance",
  "state": "Start frame: she has just raised the phone and is speaking directly into the lens. The screen of the held phone is completely off, plain matte black, showing nothing at all.",
  "lighting": "Soft neutral daylight of an open gym, warm red glow from the neon behind her.",
  "realism": "UGC realism, real skin texture with visible pores, individual hair strands, subtle wrinkles, realistic shadows and reflections, iPhone-footage look, no AI polish, no beauty smoothing, no blur anywhere, everything in sharp focus including the background wall and signage.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no interface on the phone screen, no icons, no app screenshot, no logo, no studio, no plastic skin, no extra fingers, no supernatural lighting, no blur, no silver jewelry, no second person"
}
```

## K07 · T15 · CTA · EDITAR do K06

```json
{
  "task": "edit the attached image, keep everything identical except the change listed",
  "keep_identical": "Keep Brandon exactly the same: same face, same hair and beads, same tattoos, same white tank top, same gold cross, same extended left arm holding the filming phone. Keep the held phone in her right hand with the same completely black empty screen. Keep the SAME background exactly: cinderblock wall, neon sign, flag, same lighting, same camera angle and framing.",
  "change_1": "She now holds the second phone slightly lower and further to the side, so the center of the frame is clear, and her expression is more urgent and direct with strong eye contact.",
  "realism": "UGC realism, real skin texture with visible pores, iPhone-footage look, no AI polish, no beauty smoothing, no blur anywhere. Do not make her skin darker, yellowish or orangish. Do not make the colors more saturated.",
  "negative": "do not change the face, do not change identity, do not change the background, do not change the camera angle, no interface on the phone screen, no icons, no captions, no subtitles, no words overlaid on the image, no plastic skin, no extra fingers, no silver jewelry"
}
```

---

# Prompts de vídeo (Veo 3.1 via Flow)

## Bloco global

Colar em todo prompt:

```text
a avatar (mulher) fala em inglês com sotaque americano de mulher negra, voz autêntica, dinâmica, apaixonada e emocional, como se exigisse ser ouvida.

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

Estilo TikTok nativo, UGC. Preservar exatamente a identidade da Brandon, rosto, cornrows com miçangas, tatuagens, regata branca, cruz de OURO, a box de treino, a iluminação e o enquadramento do frame inicial. Sem legenda, sem texto gerado, sem música, sem pessoas extras.
```

Nos takes de selfie (T3 a T15), acrescentar:

```text
a avatar não move o braço esquerdo que está estendido para a esquerda do quadro porque a mão está segurando o celular que captura o vídeo.
```

---

### V01 · T1 · usa K01

```text
a avatar (mulher) fala em inglês com sotaque americano de mulher negra, voz autêntica, dinâmica e emocional, como se exigisse ser ouvida, a seguinte frase: "If your belly is flat in the morning and swollen by night, if your jeans only button on good days,"

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: a avatar segura a placa anatômica firme na frente do corpo e olha direto para a câmera enquanto fala. A placa fica parada e centralizada. A mulher ao lado permanece parada, olhando para baixo, sem falar.

câmera: fixa, leve handheld natural

som ambiente: ambiente de galpão de treino, sem música, sem ruído de fundo
```

### V02 · T2 · usa K02

Fala curta. A frase filler no fim é para o take não sair arrastado e **deve ser cortada no CapCut**.

```text
a avatar (mulher) fala em inglês com sotaque americano de mulher negra, voz autêntica, dinâmica e emocional, a seguinte frase: "if you feel puffy no matter what you eat, you need to hear this right now. Because nobody ever explained this to you properly."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: a avatar levanta o dedo indicador da mão direita ao lado da placa e depois volta a apoiar a placa com as duas mãos, mantendo o olhar na câmera. A mulher ao lado permanece parada.

câmera: fixa, leve handheld natural

som ambiente: ambiente de galpão de treino, sem música, sem ruído de fundo
```

### V03 · T3 · usa K03

```text
a avatar (mulher) fala em inglês com sotaque americano de mulher negra, voz autêntica, dinâmica e emocional, como se exigisse ser ouvida, a seguinte frase: "Most women spend years blaming themselves for a problem that was never about willpower in the first place. And the longer you ignore it, the worse it gets."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: corte duro para a selfie. a avatar fala direto para a câmera e faz um gesto aberto com a mão direita. a avatar não move o braço esquerdo que está estendido para a esquerda do quadro porque a mão está segurando o celular que captura o vídeo.

câmera: leve handheld de selfie, fixa no enquadramento

som ambiente: ambiente de galpão de treino, sem música, sem ruído de fundo
```

### V04 · T4 · usa K04

```text
a avatar (mulher) fala em inglês com sotaque americano de mulher negra, voz autêntica, dinâmica e emocional, a seguinte frase: "Eight out of ten women over 40 deal with this exact imbalance and have no idea it is even happening. They just think it is aging. It is not aging."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: a avatar fala direto para a câmera, abre a mão direita para o lado e depois nega com um pequeno movimento firme da cabeça na última frase. a avatar não move o braço esquerdo que está estendido para a esquerda do quadro porque a mão está segurando o celular que captura o vídeo.

câmera: leve handheld de selfie, fixa no enquadramento

som ambiente: ambiente de galpão de treino, sem música, sem ruído de fundo
```

### V05 · T5 · usa K05

```text
a avatar (mulher) fala em inglês com sotaque americano de mulher negra, voz autêntica, dinâmica e emocional, a seguinte frase: "Another salad will not fix this. Cutting calories will not fix this. Your hormones are telling your body to store fat."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: a avatar marca as duas primeiras frases com dois pequenos gestos secos da mão direita e depois aponta o dedo para a própria barriga na última frase. a avatar não move o braço esquerdo que está estendido para a esquerda do quadro porque a mão está segurando o celular que captura o vídeo.

câmera: leve handheld de selfie, fixa no enquadramento

som ambiente: ambiente de galpão de treino, sem música, sem ruído de fundo
```

### V06 · T6 · usa K03

```text
a avatar (mulher) fala em inglês com sotaque americano de mulher negra, voz autêntica, dinâmica e emocional, a seguinte frase: "Your metabolism is stalled and your gut is backed up, and no diet is reaching what is actually stuck inside you. You have to fix it from the inside."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: a avatar fala direto para a câmera e leva a mão direita à altura do abdômen na expressão "stuck inside you", depois volta a mão para a altura do peito. a avatar não move o braço esquerdo que está estendido para a esquerda do quadro porque a mão está segurando o celular que captura o vídeo.

câmera: leve handheld de selfie, fixa no enquadramento

som ambiente: ambiente de galpão de treino, sem música, sem ruído de fundo
```

### V07 · T7 · usa K04

```text
a avatar (mulher) fala em inglês com sotaque americano de mulher negra, voz autêntica, dinâmica e emocional, a seguinte frase: "Here's what happens when women ignore this. First comes the bloating every single night. You tell yourself it is nothing."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: a avatar levanta um dedo ao dizer "first" e depois dá de ombros levemente na última frase, com expressão de quem já ouviu essa desculpa muitas vezes. a avatar não move o braço esquerdo que está estendido para a esquerda do quadro porque a mão está segurando o celular que captura o vídeo.

câmera: leve handheld de selfie, fixa no enquadramento

som ambiente: ambiente de galpão de treino, sem música, sem ruído de fundo
```

### V08 · T8 · usa K05

```text
a avatar (mulher) fala em inglês com sotaque americano de mulher negra, voz autêntica, dinâmica e emocional, a seguinte frase: "Then the tired mornings, the clothes that stop fitting, the photos you skip. One day you feel fine, the next you cannot look in the mirror."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: a avatar conta os itens com pequenos movimentos da mão direita, acelerando o ritmo, e termina com a expressão mais dura e o olhar fixo na câmera. a avatar não move o braço esquerdo que está estendido para a esquerda do quadro porque a mão está segurando o celular que captura o vídeo.

câmera: leve handheld de selfie, fixa no enquadramento

som ambiente: ambiente de galpão de treino, sem música, sem ruído de fundo
```

### V09 · T9 · usa K03

```text
a avatar (mulher) fala em inglês com sotaque americano de mulher negra, voz autêntica, dinâmica e emocional, a seguinte frase: "It is exhausting, and it kills your confidence. Here's what actually works. Eating and moving on the schedule your hormones actually run on."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: a avatar faz uma pausa curta depois de "confidence", muda a expressão de cansada para resolvida, e abre a mão direita para frente ao começar a explicar. a avatar não move o braço esquerdo que está estendido para a esquerda do quadro porque a mão está segurando o celular que captura o vídeo.

câmera: leve handheld de selfie, fixa no enquadramento

som ambiente: ambiente de galpão de treino, sem música, sem ruído de fundo
```

### V10 · T10 · usa K05

```text
a avatar (mulher) fala em inglês com sotaque americano de mulher negra, voz autêntica, dinâmica e emocional, a seguinte frase: "Not some starvation plan, and not a gym membership you will quit in three weeks. That wakes your metabolism back up, clears the bloat and calms the cravings."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: a avatar faz um gesto curto de descarte com a mão direita nas duas negativas, depois vira a palma para cima e conta três benefícios com pequenos movimentos. a avatar não move o braço esquerdo que está estendido para a esquerda do quadro porque a mão está segurando o celular que captura o vídeo.

câmera: leve handheld de selfie, fixa no enquadramento

som ambiente: ambiente de galpão de treino, sem música, sem ruído de fundo
```

### V11 · T11 · usa K04

```text
a avatar (mulher) fala em inglês com sotaque americano de mulher negra, voz autêntica, dinâmica e emocional, a seguinte frase: "And this is not theory. It is what every woman I train does. But there is a catch."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: a avatar aponta o polegar por cima do ombro na direção da academia ao dizer "every woman I train", depois para o gesto e ergue a sobrancelha na última frase. a avatar não move o braço esquerdo que está estendido para a esquerda do quadro porque a mão está segurando o celular que captura o vídeo.

câmera: leve handheld de selfie, fixa no enquadramento

som ambiente: ambiente de galpão de treino, sem música, sem ruído de fundo
```

### V12 · T12 · usa K05

```text
a avatar (mulher) fala em inglês com sotaque americano de mulher negra, voz autêntica, dinâmica e emocional, a seguinte frase: "Every woman's hormones run on a different clock, and guessing yours is exactly why every plan you tried before failed you."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: a avatar desenha um pequeno círculo no ar com o dedo ao falar de relógio, depois abre a mão e mantém o olhar firme na câmera até o fim da frase. a avatar não move o braço esquerdo que está estendido para a esquerda do quadro porque a mão está segurando o celular que captura o vídeo.

câmera: leve handheld de selfie, fixa no enquadramento

som ambiente: ambiente de galpão de treino, sem música, sem ruído de fundo
```

### V13 · T13 · usa K06

Take da ponte. O nome do produto cai no mesmo instante em que o celular sobe.

```text
a avatar (mulher) fala em inglês com sotaque americano de mulher negra, voz autêntica, dinâmica e emocional, a seguinte frase: "That is why I send them all to FityWell. It builds the whole plan around your body from a two minute quiz. No extreme dieting, no gym required."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: a avatar já está com o celular erguido na mão direita ao lado do rosto e dá um pequeno impulso com ele exatamente ao dizer "FityWell", mantendo a tela virada para a câmera e parada o resto do take. a avatar não move o braço esquerdo que está estendido para a esquerda do quadro porque a mão está segurando o celular que captura o vídeo.

câmera: leve handheld de selfie, fixa no enquadramento

som ambiente: ambiente de galpão de treino, sem música, sem ruído de fundo
```

### V14 · T14 · usa K06

```text
a avatar (mulher) fala em inglês com sotaque americano de mulher negra, voz autêntica, dinâmica e emocional, a seguinte frase: "Women tell me that within three weeks they feel lighter, their face looks thinner, and their jeans button without a fight."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: a avatar mantém o celular erguido e parado na mão direita e sorri de leve ao falar dos resultados, com o olhar na câmera. a avatar não move o braço esquerdo que está estendido para a esquerda do quadro porque a mão está segurando o celular que captura o vídeo.

câmera: leve handheld de selfie, fixa no enquadramento

som ambiente: ambiente de galpão de treino, sem música, sem ruído de fundo
```

### V15 · T15 · usa K07

```text
a avatar (mulher) fala em inglês com sotaque americano de mulher negra, voz autêntica, dinâmica e emocional, a seguinte frase: "Comment yes and I will send you the quiz directly. But make sure you are following me first, or it will not let me reach you."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: a avatar aponta o dedo indicador direito para a câmera ao dizer "comment yes", mantendo o celular na mesma mão, e mantém contato visual forte até o fim. O dedo se aproxima da câmera sem cobrir o rosto. a avatar não move o braço esquerdo que está estendido para a esquerda do quadro porque a mão está segurando o celular que captura o vídeo.

câmera: leve handheld de selfie, leve push-in

som ambiente: ambiente de galpão de treino, sem música, sem ruído de fundo
```

---

## Mapa de âncoras

| Keyframe | Referências a anexar | Modelo |
|---|---|---|
| REF-A | nenhuma, gerar do zero | Nano Banana 2, regenerar até rosto crível |
| K01 | âncora Brandon + REF-A aprovada | Nano Banana **Pro**, várias variações |
| K02 | K01 aprovado | Nano Banana 2, comando de edição |
| K03 | âncora Brandon | Nano Banana 2 |
| K04 | K03 aprovado | Nano Banana 2, comando de edição |
| K05 | K03 aprovado (**nunca a partir do K04**) | Nano Banana 2, comando de edição |
| K06 | âncora Brandon | Nano Banana 2 |
| K07 | K06 aprovado | Nano Banana 2, comando de edição |

---

## Montagem no CapCut

- Timeline 1080x1920, 30 fps.
- Cortes duros entre todos os takes. O único corte que precisa de peso é V02 para V03, que é a troca de setup do hook para a selfie.
- Cortar a frase filler do fim do V02 ("Because nobody ever explained this to you properly").
- Cortar o silêncio inicial de cada clipe para a fala começar imediatamente.
- Compor o print do quiz FityWell na tela do celular em V13, V14 e V15. A tela foi gerada apagada de propósito.
- Legendas grandes estilo Captions.ai Prism Pro, palavra destacada em vermelho, centralizadas na altura do peito. Nunca cobrir a placa anatômica no hook nem o celular nos takes finais.
- Manter `YES` isolado na tela no CTA.
- Color grading: temp -3, tint +2, saturação -6, exposição -3, contraste +12, highlight -35, shadow +18, fade +6.

## Gates de qualidade

1. Brandon é a mesma mulher em todos os clipes, com a cruz de OURO em todos.
2. As cornrows com miçangas estão iguais em todos os planos.
3. A placa anatômica tem forma, inchaço e interior idênticos em K01 e K02.
4. A 2ª pessoa é a mesma mulher em K01 e K02, e nunca toca a placa.
5. A sinalização da parede continua igual e legível, sem palavras inventadas novas.
6. Nenhuma legenda ou texto foi gerado dentro da imagem.
7. A tela do celular está apagada em K06 e K07, sem interface gerada.
8. Mãos com cinco dedos, sem fusão com a placa nem com o celular.
9. O braço esquerdo estendido não se mexe em nenhum take de selfie.
10. `yes` e o follow gate estão os dois no CTA final.
