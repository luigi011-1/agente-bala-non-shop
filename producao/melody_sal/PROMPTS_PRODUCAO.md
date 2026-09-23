# Melody Carter | Ângulo 1 (Korella Saffron) | Pacote de Prompts

Vídeo modelo: `9a493713-cebb-4181-bd39-22c89d7ac462.mp4`

Âncora de identidade: `C:\Users\luigi\Desktop\AVATARES NON-SHOP\melody carter .png`

Referência de produto: `C:\Users\luigi\Desktop\B-ROLL PRODUTOS\product.png`

Funil: comment `yes` -> DM -> deep link Amazon do Korella Saffron

> ⚠️ **ÂNGULO 1: o produto APARECE.** Frasco em quadro do T18 ao T22, e o nome "Korella Saffron" é dito em voz alta no V18, no mesmo take em que o frasco entra na mão.
>
> ⚠️ **CENÁRIO NOVO: box de chuveiro, não a oficina.** Decisão do Luigi em 2026-08-25. **A identidade fica intacta:** rosto, tranças, cavanhaque, tatuagens, **regata branca canelada e cruz de PRATA**. O original é sem camisa, nós não somos.
>
> ⚠️ **O K01 é o frame herói e é REVEAL CONTÍNUO.** Uma imagem só, com a montanha de sal ainda BAIXA. Ela cresce dentro do V01. Se sair já alta, o clipe não tem pra onde evoluir.

---

## Índice de geração

| Take | Keyframe | Ação de geração |
|---|---|---|
| T1 | K01 | GERAR DO ZERO (ref: âncora Melody). **Frame herói.** Pro, com variações. |
| T2 a T4, T6 a T17 | K02 | **EDITAR do K01** (pote sai de quadro, montanha cresce). **Atende 15 takes.** |
| T5 | K03 | GERAR DO ZERO. Insert nos pés, **sem rosto**. |
| T18 a T20 | K04 | GERAR DO ZERO (ref: **âncora Melody + product.png**). Em pé na pia. |
| T21, T22 | K05 | **EDITAR do K04** (fecha o plano, frasco sobe junto ao rosto) |

Total: **5 keyframes para 22 takes. Sem 2ª pessoa neste vídeo, então não há REF-A.**

---

## Trava de identidade e continuidade

**Escrita aqui uma vez, não repetir inteira dentro de cada JSON.**

- **MELODY É HOMEM.** Homem negro, musculoso, tranças box braids escuras compridas, cavanhaque e barba aparada.
- **Regata branca canelada e shorts pretos. Corrente fina de PRATA com pingente de cruz de PRATA. Nunca ouro.** Ele NÃO está sem camisa.
- Manga de tatuagem ornamental no braço direito, tatuagens no peito.
- **Cenário: box de chuveiro de pedra clara, com DUAS âncoras visuais apenas: o registro de metal escovado na parede e o ralo quadrado no chão.** Sem prateleira de frascos, sem chuveirinho duplo, sem porta de vidro em quadro. Nunca inventariar o banheiro.
- **Piso de pedra clara, seco.**
- **Luz neutra e difusa de dia nublado**, vinda de uma janela alta fora de quadro. **Nada de luz âmbar de teto**, que é o que mais entrega cara de IA. O original tem exatamente esse erro.
- Zero blur, tudo em foco nítido. Cara de vídeo de iPhone, nunca polimento de IA.
- **Corrigir a foto-âncora:** ela é sentada e relaxada. Nos prompts a postura é sempre declarada.

## Trava do prop herói (a montanha de sal)

O herói do vídeo é a **montanha de sal grosso**, e ela tem dois estados que nunca podem ser trocados:

```text
COARSE ROCK SALT: chunky, irregular, opaque white crystals roughly the size of small
pebbles, each grain clearly separate and visible. NOT fine powder and NOT snow.
```

- **K01, estado INICIAL:** monte ainda BAIXO e espalhado, uns 5 cm de altura, e o jato caindo em cima dele.
- **K02, estado MADURO:** **THICK, TALL, HEAPED MOUND**, uns 20 cm de altura, empilhada com volume 3D real, com os grãos rolando pra fora na base.

## Trava do pote de sal (usar no K01)

```text
A clear plastic canister with a black flip cap and NO label of any kind, about 20 cm tall,
held tilted in his right hand.
```

**Não há 2ª pessoa neste vídeo, então não há REF-A.**

---

## GATE DE COMPOSIÇÃO VISUAL (rodado ANTES dos prompts abaixo)

```
HEROI
[x] 1. Heroi no LOWER FOREGROUND mais perto que o rosto
       -> K01/K02: a montanha de sal. K03: macro puro. K04/K05: o frasco
[x] 2. Nada compete com ele
[x] 3. Volume e cobertura EXPLICITADOS
       -> K01 monte baixo de proposito. K02 THICK TALL HEAPED MOUND com volume 3D

DISTANCIA
[x] 4. "Da pra estar mais perto?"   -> todos fecham mais que o original
[x] 5. Enquadramento fechado        -> da cabeca ate a montanha, coxas cortadas pela borda
[x] 6. Take mais fechado e o do CTA -> K05

FUNDO
[x] 7. Cenario reconhecivel         -> 2 ancoras: o registro de metal e o ralo quadrado
[x] 8. Fundo por enquadramento, nunca blur
[x] 9. Menos elementos

2a PESSOA
[-] 10. Nao se aplica, video sem 2a pessoa
```

## GATE DE REALISMO (rodado junto)

```
[x] 1. Heroi isolado, 2 ancoras de fundo
[x] 2. Camera puxada perto, a montanha enche o terco inferior
[x] 3. Luz NEUTRA de dia nublado. O original usa ambar de teto e e justamente o erro
[x] 4. Negative carrega no warm orange color cast, no yellow tint, no golden glow
[x] 5. Fundo especifico e nunca borrado
[x] 6. Prop teimoso: o SAL GROSSO. Forma descrita em bloco proprio, nao so o nome
[x] 7. Bloco de realismo padrao colado por inteiro em todo prompt
```

**Três escolhas deliberadas.**

**A luz.** O original é banhado de âmbar quente de teto, que é exatamente o item 2 do gate de realismo e o que mais entrega cara de IA. Trocamos por luz neutra difusa de janela. Perde-se o clima de spa, ganha-se credibilidade de UGC.

**O sal.** É o prop mais provável de sair errado, porque a IA defaulta pra pó fino, açúcar ou neve quando você só diz "salt". Por isso ele tem **bloco de forma próprio**, com tamanho de grão e opacidade, exatamente como a falha #6 manda.

**O fundo.** Box de chuveiro é um cenário que convida inventário: prateleira, frascos, chuveirinho, porta de vidro, banco. Ficaram **duas âncoras**: o registro de metal e o ralo. Já lê como chuveiro e nada mais compete.

## ⚠️ NOTA DE RESTRIÇÃO

Risco **baixo**. Sem modelo anatômico, sem região sensível, sem 2ª pessoa, e ele está **de regata**, não sem camisa. Dois cuidados por precaução:

1. **O pote de sal vai SEM rótulo nenhum.** Não descrever marca no texto positivo, e **nunca negar marca no negative**: `no logos` já derrubou oito de oito prompts uma vez.
2. **Os pés vão descritos como normais e limpos.** Nenhum descritor de pele ou unha doente em lugar nenhum.

---

# Prompts de imagem

## K01 · T1 · HOOK · GERAR DO ZERO (Nano Banana **Pro**, várias variações) · ÂNCORA MELODY

```json
{
  "shot_id": "K01_hook_pour",
  "context": "Fictional AI-generated character. No real person is being filmed or depicted.",
  "reference_use": "Use the attached image ONLY for Melody's face, identity, hair, tattoos and clothing. IGNORE the garage background of the reference completely, this scene is a shower. Do NOT copy its pose or framing. Frame him much closer than the reference.",
  "identity_main": "The EXACT MAN from the attached reference image (Melody Carter), a muscular Black man with long dark box braids, a trimmed goatee and beard, an ornamental tattoo sleeve on his right arm and small chest tattoos.",
  "wardrobe": "White ribbed tank top and black shorts, thin SILVER chain with a SILVER cross pendant. He is NOT shirtless.",
  "prop": "A clear plastic canister with a black flip cap and NO label of any kind, about 20 cm tall, held tilted in his right hand, with a steady stream of coarse salt falling from it. COARSE ROCK SALT: chunky, irregular, opaque white crystals roughly the size of small pebbles, each grain clearly separate and visible. NOT fine powder and NOT snow.",
  "scene": "A walk-in shower with pale stone walls, with only two visible anchors: a brushed metal shower valve on the wall behind him and a square drain in the pale stone floor. Nothing else in frame.",
  "posture": "Crouched down on his heels on the shower floor, knees apart, leaning slightly forward, barefoot. NOT the seated slouch of the reference photo.",
  "composition": "TIGHT. Framed from the top of his head down to the salt on the floor, his thighs cropped by the left and right edges. The salt pile sits in the lower third, closer to the lens than his face, unmistakably the hero. The falling stream connects his hand to the pile.",
  "camera": "low, around knee height, angled slightly down toward the floor, close",
  "state": "Start frame: the salt pile is still LOW and spread out, only about 5 cm tall, and the stream is still falling onto it.",
  "lighting": "Flat neutral diffuse daylight from a high window out of frame, like an overcast day. No ceiling lights.",
  "realism": "UGC realism, real skin texture with visible pores, individual hair strands, subtle wrinkles, realistic shadows and reflections, iPhone-footage look, phone camera look not professional photography, no AI polish, no beauty smoothing, no blur anywhere, everything in sharp focus including background walls and details.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no studio, no plastic skin, no extra fingers, no blur, no gold jewelry, no shirtless torso, no seated slouch, no second person, no tall pile yet, no fine powder, no snow, no shelves, no bottles on the wall, no warm orange color cast, no yellow tint, no golden glow"
}
```

## K02 · T2 a T4, T6 a T17 · O BLOCO DE FALA · EDITAR do K01

```json
{
  "task": "edit the attached image, keep everything identical except the changes listed",
  "keep_identical": "Keep the man exactly the same: same face, same box braids, same goatee, same tattoos, same white tank top, same black shorts, same SILVER cross, same crouched posture, barefoot. Keep the SAME shower background exactly: pale stone walls, brushed metal valve, square drain, same neutral daylight, same camera angle and framing.",
  "change_1": "Remove the plastic canister and the falling stream of salt from his hand completely. His hands are now resting open on his knees.",
  "change_2": "The salt pile on the floor is now a THICK, TALL, HEAPED MOUND about 20 cm high, piled up with real 3D volume, with loose coarse crystals scattering out at its base. Same chunky irregular pebble-sized white crystals, not fine powder.",
  "change_3": "He now looks straight into the lens and speaks directly to camera.",
  "realism": "UGC realism, real skin texture with visible pores, iPhone-footage look, no AI polish, no beauty smoothing, no blur anywhere. Do not make his skin darker, yellowish or orangish. Do not make the colors more saturated.",
  "negative": "do not change the face, do not change identity, do not change the background, do not change the camera angle, no captions, no subtitles, no words overlaid on the image, no plastic skin, no extra fingers, no gold jewelry, no shirtless torso, no blur, no fine powder, no snow, no warm orange color cast, no yellow tint"
}
```

## K03 · T5 · AUTORIDADE · GERAR DO ZERO · INSERT SEM ROSTO

```json
{
  "shot_id": "K03_feet_macro",
  "reference_use": "Close-up insert. No face. Use only the pale stone shower floor and the neutral daylight of the other shots.",
  "identity_main": "No face and no head in frame. Close-up of two bare male feet standing flat on a spread layer of coarse salt on a pale stone shower floor, shins visible up to mid-calf.",
  "scene": "SAME pale stone shower floor, the square drain visible at the edge of the frame.",
  "composition": "Close-up straight down at the feet, filling most of the frame. The coarse salt is spread in a thick ring all around them and pressed down under the soles, with loose crystals scattered outward across the stone.",
  "camera": "top-down, close to the floor",
  "state": "Start frame: both feet standing still and flat on the salt.",
  "lighting": "Flat neutral diffuse daylight, like an overcast day.",
  "realism": "UGC realism, real skin texture, real salt crystal texture with real light refraction, iPhone macro look, no AI polish, no blur anywhere, everything in sharp focus.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no face, no head, no studio, no cartoon look, no blur, no fine powder, no snow, no warm orange color cast, no yellow tint"
}
```

## K04 · T18 a T20 · PRODUTO · GERAR DO ZERO · ÂNCORA MELODY + PRODUCT.PNG

```json
{
  "shot_id": "K04_product",
  "reference_use": "TWO references attached. Use the FIRST image ONLY for Melody's face, identity, hair, tattoos and clothing. IGNORE its garage background, this scene is a bathroom. Use the SECOND image for the EXACT supplement bottle he is holding, matching its shape, its white body, its purple and white label and its proportions exactly. Do NOT copy the framing of either reference.",
  "identity_main": "The EXACT MAN from the first reference image (Melody Carter), a muscular Black man with long dark box braids, a trimmed goatee and beard, an ornamental tattoo sleeve on his right arm and small chest tattoos.",
  "wardrobe": "White ribbed tank top, thin SILVER chain with a SILVER cross pendant. He is NOT shirtless.",
  "prop": "The EXACT supplement bottle from the second reference image, held upright in his right hand at chest height, label facing the camera and fully readable. The bottle is about 10 cm in height.",
  "scene": "Standing at a bathroom sink just outside the shower, pale stone wall behind him, with only one visible anchor: the edge of a plain rectangular mirror. Nothing else in frame.",
  "posture": "Standing upright at the sink, shoulders squared, chin up, NOT the seated slouch of the reference photo. No legs or lap in frame.",
  "composition": "TIGHT chest-up. The bottle sits in the lower foreground, closer to the lens than his face, held steady and turned toward the camera, unmistakably the hero of the shot. His left hand is open near his chest in a natural mid-gesture. He speaks straight into the lens.",
  "camera": "chest level, straight-on, close",
  "state": "Start frame: bottle raised and steady toward the lens, speaking directly to camera.",
  "lighting": "Flat neutral diffuse daylight, like an overcast day. No ceiling lights.",
  "realism": "UGC realism, real skin texture with visible pores, individual hair strands, subtle wrinkles, realistic shadows and reflections, iPhone-footage look, phone camera look not professional photography, no AI polish, no beauty smoothing, no blur anywhere, everything in sharp focus including background walls and details.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no studio, no plastic skin, no extra fingers, no blur, no gold jewelry, no shirtless torso, no seated slouch, no second person, no salt, no clutter on the sink, no warm orange color cast, no yellow tint, no golden glow"
}
```

## K05 · T21, T22 · CTA · EDITAR do K04

```json
{
  "task": "edit the attached image, keep everything identical except the changes listed",
  "keep_identical": "Keep the man exactly the same: same face, same box braids, same goatee, same tattoos, same white tank top, same SILVER cross, same standing posture. Keep the SAME background exactly: pale stone wall, edge of the mirror, same neutral daylight, same camera angle. Keep the supplement bottle EXACTLY the same shape and label.",
  "change_1": "Crop in much tighter. This must be the CLOSEST framing of the entire video: his head and shoulders now fill the frame.",
  "change_2": "The bottle is now raised higher, up beside his face at cheek height, label still facing the camera and fully readable.",
  "change_3": "His free hand is lowered out of frame and he looks straight into the lens with direct personal eye contact.",
  "realism": "UGC realism, real skin texture with visible pores, iPhone-footage look, no AI polish, no beauty smoothing, no blur anywhere. Do not make his skin darker, yellowish or orangish. Do not make the colors more saturated.",
  "negative": "do not change the face, do not change identity, do not change the background, do not change the bottle label, no captions, no subtitles, no words overlaid on the image, no plastic skin, no extra fingers, no gold jewelry, no blur, no warm orange color cast, no yellow tint"
}
```

---

# Prompts de vídeo (Veo 3.1 via Flow)

## Bloco global

Colar em todo prompt:

```text
o avatar (HOMEM) fala em inglês com sotaque americano de homem negro, voz autêntica, dinâmica, apaixonada e emocional, como se exigisse ser ouvido.

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

Estilo TikTok nativo, UGC. Preservar exatamente a identidade do Melody, rosto, tranças, cavanhaque, tatuagens, regata branca, cruz de PRATA, o box de chuveiro, a iluminação neutra e o enquadramento do frame inicial. Sem legenda, sem texto gerado, sem música, sem pessoas extras.
```

**A câmera do original é FIXA e não é handheld de selfie**, então NÃO incluir a instrução de braço parado em nenhum prompt.

---

### V01 · T1 · usa K01 · ⚠️ REVEAL CONTÍNUO, NÃO PODE CORTAR

```text
o avatar (HOMEM) fala em inglês com sotaque americano de homem negro, voz autêntica, dinâmica e emocional, como se exigisse ser ouvido, a seguinte frase: "Pour salt in your shower, spread a thick layer on the floor, and stand on it barefoot for ten minutes."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: o sal continua caindo do pote e a montanha vai crescendo no chão, de um monte baixo até um monte alto, com os grãos rolando pra fora na base. Tudo acontece no mesmo take, sem nenhum corte, e a montanha fica em quadro o tempo inteiro.

câmera: fixa

som ambiente: banheiro silencioso, grãos de sal caindo, sem música
```

### V02 · T2 · usa K02

```text
o avatar (HOMEM) fala em inglês com sotaque americano de homem negro, voz autêntica e convincente, a seguinte frase: "I know it sounds insane, brother, but you will thank me for the rest of your life."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: corte duro, o pote sumiu e a montanha já está alta. ele abre as duas mãos com as palmas pra cima e depois olha firme pra câmera.

câmera: fixa

som ambiente: banheiro silencioso, sem música, sem ruído de fundo
```

### V03 · T3 · usa K02

```text
o avatar (HOMEM) fala em inglês com sotaque americano de homem negro, voz direta e prática, a seguinte frase: "You already stand in that shower for ten minutes doing nothing."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ele dá de ombros uma vez enquanto fala, sem sair do lugar.

câmera: fixa

som ambiente: banheiro silencioso, sem música, sem ruído de fundo
```

### V04 · T4 · usa K02

```text
o avatar (HOMEM) fala em inglês com sotaque americano de homem negro, voz autêntica e direta, a seguinte frase: "You might as well drag out what forty years of stress packed into your body while you are at it."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ele puxa a mão pra baixo no ar, como quem arranca algo, ao dizer a primeira parte.

câmera: fixa, leve push-in

som ambiente: banheiro silencioso, sem música, sem ruído de fundo
```

### V05 · T5 · usa K03 · B-ROLL

```text
(sem fala no take: a fala 5 do roteiro entra como voz-over na edição)

o que acontece no vídeo: os dois pés se ajeitam devagar em cima do sal e os grãos afundam e se espalham um pouco embaixo das solas.

câmera: fixa, close de cima

som ambiente: banheiro silencioso, sal estalando baixinho, sem música
```

### V06 · T6 · usa K02

```text
o avatar (HOMEM) fala em inglês com sotaque americano de homem negro, voz autêntica e direta, a seguinte frase: "When hot water and salt hit them at the same time, it starts pulling fluid and inflammation out."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: corte duro, ele está de volta agachado. ele junta as duas mãos e depois abre puxando pra fora ao dizer a última parte.

câmera: fixa

som ambiente: banheiro silencioso, sem música, sem ruído de fundo
```

### V07 · T7 · usa K02

```text
o avatar (HOMEM) fala em inglês com sotaque americano de homem negro, voz autêntica, dinâmica e emocional, a seguinte frase: "And everything your body has been holding on to gets dragged out through the bottoms of your feet."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ele aponta pra baixo, na direção dos próprios pés, ao dizer a última parte.

câmera: fixa

som ambiente: banheiro silencioso, sem música, sem ruído de fundo
```

### V08 · T8 · usa K02

```text
o avatar (HOMEM) fala em inglês com sotaque americano de homem negro, voz mais calma e envolvente, a seguinte frase: "While you just stand there your cortisol drops, the inflammation melts away, and your muscles let go of tension you did not know was there."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ele baixa a mão devagar no ar a cada item que fala, três vezes, e relaxa os ombros no fim.

câmera: fixa, leve push-in

som ambiente: banheiro silencioso, sem música, sem ruído de fundo
```

### V09 · T9 · usa K02

```text
o avatar (HOMEM) fala em inglês com sotaque americano de homem negro, voz mais leve, a seguinte frase: "Your mood shifts, your mind clears, and by the time you step away your legs feel lighter."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ele passa a mão aberta na frente do rosto ao dizer "mind clears" e abre um sorriso curto.

câmera: fixa

som ambiente: banheiro silencioso, sem música, sem ruído de fundo
```

### V10 · T10 · usa K02

```text
o avatar (HOMEM) fala em inglês com sotaque americano de homem negro, voz quente e pessoal, a seguinte frase: "Your shoulders drop, and that night your sleep hits different than it has in years."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ele deixa os ombros caírem visivelmente ao dizer a primeira parte.

câmera: fixa

som ambiente: banheiro silencioso, sem música, sem ruído de fundo
```

### V11 · T11 · usa K02 · **O BEAT DE VIRADA**

```text
o avatar (HOMEM) fala em inglês com sotaque americano de homem negro, voz mais baixa e séria, a seguinte frase: "And while you are standing there for those ten minutes, something else is running the other twenty three, and that one actually costs you."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ele para de gesticular, se inclina um pouco pra frente e baixa o tom na segunda metade.

câmera: fixa, leve push-in

som ambiente: banheiro silencioso, sem música, sem ruído de fundo
```

### V12 · T12 · usa K02

```text
o avatar (HOMEM) fala em inglês com sotaque americano de homem negro, voz firme, a seguinte frase: "Your body did not stop handling stress. It changed what it takes to bring it back down, and nobody told you."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ele balança a cabeça na primeira frase e abre a mão com a palma pra cima na segunda.

câmera: fixa

som ambiente: banheiro silencioso, sem música, sem ruído de fundo
```

### V13 · T13 · usa K02

```text
o avatar (HOMEM) fala em inglês com sotaque americano de homem negro, voz honesta e equilibrada, a seguinte frase: "Ten minutes on salt buys you ten minutes. Cortisol goes right back up the second you towel off."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ele aponta pra montanha de sal na primeira frase e depois levanta a mão no ar na segunda.

câmera: fixa

som ambiente: banheiro silencioso, sem música, sem ruído de fundo
```

### V14 · T14 · usa K02

```text
o avatar (HOMEM) fala em inglês com sotaque americano de homem negro, voz compreensiva, quase de alívio, a seguinte frase: "So it is not that you stopped being able to shake it off. It is that it stopped going down on its own."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: a expressão dele suaviza e ele balança a cabeça uma vez, devagar, na primeira frase.

câmera: fixa

som ambiente: banheiro silencioso, sem música, sem ruído de fundo
```

### V15 · T15 · usa K02

```text
o avatar (HOMEM) fala em inglês com sotaque americano de homem negro, voz mais baixa e pessoal, a seguinte frase: "And every hour it stays up, it is quietly eating the one thing that made you feel like yourself at thirty."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ele para completamente de gesticular e olha direto pra lente enquanto fala.

câmera: fixa, leve push-in

som ambiente: banheiro silencioso, sem música, sem ruído de fundo
```

### V16 · T16 · usa K02

```text
o avatar (HOMEM) fala em inglês com sotaque americano de homem negro, voz direta, a seguinte frase: "Saffron brings it down. But real saffron runs about ten dollars a gram, and you would need it every morning."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ele assente na primeira frase e depois esfrega o polegar no indicador, o gesto de dinheiro, na segunda.

câmera: fixa

som ambiente: banheiro silencioso, sem música, sem ruído de fundo
```

### V17 · T17 · usa K02

```text
o avatar (HOMEM) fala em inglês com sotaque americano de homem negro, voz séria, quase de aviso, a seguinte frase: "And most of what lands on American shelves comes in with no testing at all. That is why yours did nothing."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ele levanta a palma da mão num gesto de pare na primeira frase e depois aponta pra câmera na última.

câmera: fixa, leve push-in

som ambiente: banheiro silencioso, sem música, sem ruído de fundo
```

### V18 · T18 · usa K04 · **O TAKE DO PRODUTO**

```text
o avatar (HOMEM) fala em inglês com sotaque americano de homem negro, voz confiante e de autoridade, a seguinte frase: "The only saffron I trust is Korella Saffron, and it is on Amazon. Independently tested, so you know what is actually in it."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: corte duro, ele está em pé na pia e o sal sumiu. ele ergue o frasco na direção da câmera ao dizer o nome e o mantém firme e parado, com o rótulo virado pra lente, até o fim da fala.

câmera: fixa

som ambiente: banheiro silencioso, sem música, sem ruído de fundo
```

### V19 · T19 · usa K04

```text
o avatar (HOMEM) fala em inglês com sotaque americano de homem negro, voz aberta e confiante, a seguinte frase: "One capsule a day costs less than what that gram would. And it works while you sleep, not for ten minutes."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ele continua segurando o frasco firme com uma mão e abre a outra num gesto natural enquanto fala.

câmera: fixa

som ambiente: banheiro silencioso, sem música, sem ruído de fundo
```

### V20 · T20 · usa K04

```text
o avatar (HOMEM) fala em inglês com sotaque americano de homem negro, voz mais quente e pessoal, a seguinte frase: "Give it three weeks. You will notice it first when somebody asks what you have been doing differently."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ele ergue três dedos da mão livre na primeira frase e abre um sorriso curto na última palavra.

câmera: fixa, leve push-in

som ambiente: banheiro silencioso, sem música, sem ruído de fundo
```

### V21 · T21 · usa K05

```text
o avatar (HOMEM) fala em inglês com sotaque americano de homem negro, voz direta e convidativa, a seguinte frase: "You are going to be in that shower tonight anyway. Comment yes and I will send you the protocol myself."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ele mantém o frasco erguido ao lado do rosto e aponta pra baixo com a outra mão, na direção dos comentários, ao dizer "comment yes".

câmera: fixa, leve push-in

som ambiente: banheiro silencioso, sem música, sem ruído de fundo
```

### V22 · T22 · usa K05

```text
o avatar (HOMEM) fala em inglês com sotaque americano de homem negro, voz direta, a seguinte frase: "Just make sure you are following me first, or it will not let me send it."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ele aponta uma vez pra câmera, direto, e termina com um aceno curto de cabeça, ainda segurando o frasco ao lado do rosto.

câmera: fixa, leve push-in

som ambiente: banheiro silencioso, sem música, sem ruído de fundo
```

---

## Mapa de âncoras

| Keyframe | Referências a anexar | Modelo |
|---|---|---|
| K01 | âncora Melody | Nano Banana **Pro**, várias variações. **Frame herói** |
| K02 | **K01 aprovado** | Nano Banana 2, comando de edição. **Atende 15 takes**, vale insistir |
| K03 | nenhuma, insert sem rosto | Nano Banana 2 |
| K04 | **âncora Melody + product.png** | Nano Banana 2 |
| K05 | **K04 aprovado** | Nano Banana 2, comando de edição |

---

## Montagem no CapCut

- Timeline 1080x1920, 30 fps. Cortes duros entre todos os takes.
- **Três cortes de peso:** V01 para V02 (some o pote, a montanha já está alta), V04 para V05 (entra o insert dos pés) e V17 para V18 (some o sal, entra o frasco).
- **V05 leva a fala 5 como voz-over.** É b-roll sem rosto.
- Cortar o silêncio inicial de cada clipe.
- **Segurar um beat extra de silêncio no fim do V15**, depois de "yourself at thirty". A pausa é o que faz a frase cair.
- Legendas grandes estilo Captions.ai Prism Pro, palavra destacada em vermelho, na altura do peito. **No V01 a legenda não pode cobrir a montanha de sal**, que é onde o crescimento acontece.
- Manter `YES` isolado na tela no CTA.
- Color grading: temp -5, tint +2, saturação -6, exposição -3, contraste +12, highlight -35, shadow +18, fade +6. **O temp vai mais frio que o padrão de propósito**, porque o modelo original é âmbar e a gente está fugindo disso.

## Gates de qualidade

1. Melody é **HOMEM**, é o mesmo em todos os clipes, com a cruz de **PRATA** sempre e **de regata**, nunca sem camisa.
2. Tranças e cavanhaque iguais em todos os planos.
3. **O V01 não tem corte.** A montanha cresce dentro do take, em quadro o tempo inteiro.
4. **O K01 sai com a montanha BAIXA**, uns 5 cm. Se já saiu alta, o V01 não tem pra onde evoluir.
5. **O K02 tem MONTANHA ALTA**, uns 20 cm com volume 3D e grãos rolando na base. Monte baixinho, regenerar.
6. **O sal é GROSSO**, grão de pedra irregular e opaco do tamanho de pedrisco. Se saiu pó fino, açúcar ou neve, regenerar.
7. **O pote de sal não tem rótulo nenhum**, nem inventado. Nenhuma marca legível em quadro.
8. **A cena NÃO está banhada de âmbar.** A luz é neutra difusa de dia nublado. Este é o erro do vídeo original e é o que mais entrega cara de IA.
9. Nenhuma legenda ou texto gerado dentro da imagem.
10. **O frasco do Korella aparece do K04 em diante**, rótulo legível e igual ao product.png, uns 10 cm.
11. **O nome "Korella Saffron" é dito no V18, no mesmo take em que o frasco entra em quadro.**
12. **O K05 é o plano mais fechado do vídeo inteiro.**
13. Fundo não inventariado: **duas âncoras no chuveiro** (registro e ralo), **uma na pia** (borda do espelho).
14. Nenhuma imagem com fundo desfocado.
15. Cinco dedos nas mãos e cinco nos pés, sem fusão com o pote nem com o frasco.
16. Ele **não larga o prop**: a montanha de sal fica em quadro do V02 ao V17.
17. `yes` e o follow gate os dois no CTA final.
18. **Nenhuma menção a preço do Korella, desconto, gratuidade ou dosagem em miligramas.**
