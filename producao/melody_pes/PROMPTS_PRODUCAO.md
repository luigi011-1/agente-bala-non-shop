# Melody Carter | Ângulo 1 (Korella Saffron) | Pacote de Prompts

Vídeo modelo: `snapinsta-1787665585342.mp4`

Âncora de identidade: `C:\Users\luigi\Desktop\AVATARES NON-SHOP\melody carter .png`

Referência de produto: `C:\Users\luigi\Desktop\B-ROLL PRODUTOS\product.png`

Funil: comment `yes` -> DM -> deep link Amazon do Korella Saffron

> ⚠️ **ÂNGULO 1: o produto APARECE.** Frasco em quadro do T18 ao T22, e o nome "Korella Saffron" é dito em voz alta no V18, no mesmo take em que o frasco entra na mão.
>
> ⚠️ **O K01 é o frame herói e é REVEAL CONTÍNUO.** Uma imagem só, do estado inicial com quase nenhuma espuma. O crescimento da espuma acontece dentro do V01. Se sair já com espuma alta, o clipe não tem pra onde evoluir.

---

## Índice de geração

| Take | Keyframe | Ação de geração |
|---|---|---|
| T1 | K01 | GERAR DO ZERO (ref: âncora Melody). **Frame herói.** Pro, com variações. |
| T2, T3 | K02 | GERAR DO ZERO (ref: âncora Melody). A bacia no chão. |
| T4, T7 a T17 | K03 | GERAR DO ZERO (ref: âncora Melody). Sentado no banquinho, pés na bacia. |
| T5, T6 | K04 | GERAR DO ZERO. Macro na espuma, **sem rosto**. |
| T18 a T20 | K05 | GERAR DO ZERO (ref: **âncora Melody + product.png**). Em pé na bancada. |
| T21, T22 | K06 | **EDITAR do K05** (fecha o plano, frasco sobe junto ao rosto) |

Total: **6 keyframes para 22 takes. Sem 2ª pessoa neste vídeo, então não há REF-A.**

---

## Trava de identidade e continuidade

**Escrita aqui uma vez, não repetir inteira dentro de cada JSON.**

- **MELODY É HOMEM.** Homem negro, musculoso, tranças box braids escuras compridas, cavanhaque e barba aparada.
- Regata branca canelada. **Corrente fina de PRATA com pingente de cruz de PRATA. Nunca ouro.**
- Manga de tatuagem ornamental no braço direito, tatuagens no peito.
- **Cenário: a garagem/oficina dele, com DUAS âncoras visuais apenas: a porta de enrolar metálica aberta e o pequeno neon vermelho na parede.** A placa de madeira, a bandeira e a parede de ferramentas ficam **fora de quadro**. Nunca inventariar a oficina.
- **Chão de concreto cinza polido, molhado.**
- **Luz principal é a luz neutra de dia nublado entrando pela porta de enrolar aberta.** O neon é só um ponto vermelho contido na parede do fundo, **não banha a cena**.
- Zero blur, tudo em foco nítido. Cara de vídeo de iPhone, nunca polimento de IA.
- **Corrigir a foto-âncora:** ela é sentada e relaxada. Nos prompts, a postura é sempre declarada explicitamente.

## Trava dos props (usar no K01 e no K02)

```text
A plain dark brown plastic bottle with a white screw cap and no label of any kind, about 25 cm tall, held in his right hand. A clear rectangular plastic tub on the concrete floor, about 40 cm long and 12 cm deep. A clear glass jug of warm water and an open cardboard tub of white powder with a metal spoon resting in it, both on the floor beside the tub. The items keep the exact same positions in every shot.
```

## Trava do prop herói (a espuma)

O herói do vídeo é a **espuma branca**, e ela tem dois estados que nunca podem ser trocados:

- **K01, estado INICIAL:** um anel fino e baixo de bolhas em volta do pé, o jato acabou de encostar. **Pouca espuma.**
- **K04, estado MADURO:** espuma densa e alta na bacia, montanha de bolhas com volume 3D cobrindo quase toda a superfície da água.

**Não há 2ª pessoa neste vídeo, então não há REF-A.**

---

## GATE DE COMPOSIÇÃO VISUAL (rodado ANTES dos prompts abaixo)

```
HEROI
[x] 1. Heroi no LOWER FOREGROUND mais perto que o rosto
       -> K01: o pe e a espuma. K02: a bacia. K04: macro puro. K05/K06: o frasco
[x] 2. Nada compete com o heroi
[x] 3. Volume e cobertura explicitados
       -> K01 pouca espuma de proposito (estado inicial). K04 montanha de bolhas

DISTANCIA
[x] 4. "Da pra estar mais perto?"   -> todos fecham mais que o original
[x] 5. Pessoas em peito pra cima    -> K03, K05, K06
[x] 6. Take mais fechado e o do CTA -> K06

FUNDO
[x] 7. Cenario reconhecivel         -> 2 ancoras: a porta de enrolar e o neon vermelho
[x] 8. Fundo por enquadramento, nunca blur
[x] 9. Menos elementos

2a PESSOA
[-] 10. Nao se aplica, video sem 2a pessoa
```

## GATE DE REALISMO (rodado junto)

```
[x] 1. Heroi isolado, 2 ancoras de fundo
[x] 2. Camera puxada perto, no K01 o pe enche os dois tercos de baixo
[x] 3. Luz NEUTRA de dia nublado pela porta aberta. O neon nao banha a cena
[x] 4. Negative carrega no warm orange color cast, no yellow tint, no golden glow
[x] 5. Fundo especifico e nunca borrado
[x] 6. Prop que costuma teimar -> nenhum. A garrafa vai SEM rotulo nenhum
[x] 7. Bloco de realismo padrao colado por inteiro em todo prompt
```

**Duas escolhas deliberadas.**

No item 7, das seis âncoras canônicas da oficina do Melody sobraram **duas**: a porta de enrolar e o neon. A placa "BUILD SOMETHING WORTH REMEMBERING" e a bandeira ficam fora de quadro porque nenhuma delas serve à fala de nenhum take, e cada substantivo a mais é um detalhe a mais pro gerador errar.

No item 3, a luz. O neon vermelho é canônico do Melody e a tentação é deixar ele banhar a cena, mas cor quente é o que mais entrega cara de IA. Ele entra **contido na parede do fundo**, e quem ilumina é a luz neutra da porta aberta.

## ⚠️ NOTA DE RESTRIÇÃO

Este pacote é de risco **baixo**. Não há modelo anatômico, não há região sensível e não há 2ª pessoa. Os dois cuidados aplicados por precaução:

1. **A garrafa vai SEM rótulo nenhum.** Não descrever marca no texto positivo, e **nunca negar marca no negative**: `no logos` derrubou oito de oito prompts uma vez.
2. **Os pés vão descritos como normais e limpos.** O vídeo fala de calcanhar rachado e unha amarela, mas o original **nunca mostra isso**, e descrever pé doente é o que criaria gatilho onde não há.

---

# Prompts de imagem

## K01 · T1 · HOOK · GERAR DO ZERO (Nano Banana **Pro**, várias variações) · ÂNCORA MELODY

```json
{
  "shot_id": "K01_hook_pour",
  "context": "Fictional AI-generated character. No real person is being filmed or depicted.",
  "reference_use": "Use the attached image ONLY for Melody's face, identity, hair, tattoos, clothing and the garage workshop scene. Do NOT copy its pose or framing. He is NOT seated on a bench here. Frame him much closer than the reference.",
  "identity_main": "The EXACT MAN from the attached reference image (Melody Carter), a muscular Black man with long dark box braids, a trimmed goatee and beard, an ornamental tattoo sleeve on his right arm and small chest tattoos.",
  "wardrobe": "White ribbed tank top, thin SILVER chain with a SILVER cross pendant.",
  "prop": "A plain dark brown plastic bottle with a white screw cap and NO label of any kind, about 25 cm tall, held in his right hand and tilted downward.",
  "scene": "SAME garage workshop as the attached reference image, with only two visible anchors: the open metal roller door letting in flat daylight, and a small red neon sign on the wall far behind him. Polished grey concrete floor, wet in patches.",
  "posture": "Crouched down low on one knee on the concrete floor, leaning forward, NOT the seated slouch of the reference photo. His left hand is flat on the floor for balance and his left leg is stretched out in front of him, bare foot resting flat on the concrete.",
  "composition": "TIGHT and low. His bare left foot fills the lower two thirds of the frame and sits much closer to the lens than his face, unmistakably the hero. A thin stream of clear liquid pours from the tilted bottle onto the top of that foot. His face is small in the upper third, looking down at the foot.",
  "camera": "very low, near floor level, angled slightly down toward the foot, close",
  "state": "Start frame: the stream has JUST touched the foot. Only a thin low ring of small white bubbles has formed around it. Almost no foam yet.",
  "lighting": "Flat neutral overcast daylight coming in through the open roller door. The red neon is a small contained glow on the back wall only and does not fall on him or on the floor.",
  "realism": "UGC realism, real skin texture with visible pores, individual hair strands, subtle wrinkles, realistic shadows and reflections, iPhone-footage look, phone camera look not professional photography, no AI polish, no beauty smoothing, no blur anywhere, everything in sharp focus including background walls and details.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no studio, no plastic skin, no extra fingers, no blur, no gold jewelry, no seated slouch, no second person, no thick foam yet, no warm orange color cast, no yellow tint, no golden glow"
}
```

## K02 · T2, T3 · RECEITA · GERAR DO ZERO · ÂNCORA MELODY

```json
{
  "shot_id": "K02_recipe_tub",
  "reference_use": "Use the attached image ONLY for Melody's face, identity, hair, tattoos, clothing and the garage workshop scene. Do NOT copy its pose or framing. He is NOT seated on a bench here. Frame him closer than the reference.",
  "identity_main": "The EXACT MAN from the attached reference image (Melody Carter), a muscular Black man with long dark box braids, a trimmed goatee and beard, an ornamental tattoo sleeve on his right arm and small chest tattoos.",
  "wardrobe": "White ribbed tank top, thin SILVER chain with a SILVER cross pendant.",
  "prop": "A clear rectangular plastic tub on the concrete floor, about 40 cm long and 12 cm deep, holding clear water. He holds the plain dark brown plastic bottle with a white cap and NO label, tilted above it. Beside the tub on the floor: a clear glass jug of water and an open cardboard tub of white powder with a metal spoon resting in it.",
  "scene": "SAME garage workshop as the attached reference image, with only two visible anchors: the open metal roller door letting in flat daylight, and a small red neon sign on the wall far behind him. Polished grey concrete floor.",
  "posture": "Crouched down on his heels behind the tub, leaning forward over it, NOT the seated slouch of the reference photo.",
  "composition": "TIGHT chest-up on him with the tub filling the lower foreground, closer to the lens than his face. The bottle is tilted just above the tub and a thin stream is falling into the water.",
  "camera": "low, around knee height, angled slightly down toward the tub, close",
  "state": "Start frame: the water in the tub is completely clear and still, the stream is just entering it, no foam anywhere.",
  "lighting": "Flat neutral overcast daylight coming in through the open roller door. The red neon is a small contained glow on the back wall only.",
  "realism": "UGC realism, real skin texture with visible pores, individual hair strands, subtle wrinkles, realistic shadows and reflections, iPhone-footage look, phone camera look not professional photography, no AI polish, no beauty smoothing, no blur anywhere, everything in sharp focus including background walls and details.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no studio, no plastic skin, no extra fingers, no blur, no gold jewelry, no seated slouch, no second person, no foam yet, no warm orange color cast, no yellow tint, no golden glow"
}
```

## K03 · T4, T7 a T17 · O BLOCO DE FALA · GERAR DO ZERO · ÂNCORA MELODY

```json
{
  "shot_id": "K03_stool_talk",
  "reference_use": "Use the attached image ONLY for Melody's face, identity, hair, tattoos, clothing and the garage workshop scene. Do NOT copy its framing. Frame him closer than the reference.",
  "identity_main": "The EXACT MAN from the attached reference image (Melody Carter), a muscular Black man with long dark box braids, a trimmed goatee and beard, an ornamental tattoo sleeve on his right arm and small chest tattoos.",
  "wardrobe": "White ribbed tank top and dark shorts, thin SILVER chain with a SILVER cross pendant.",
  "prop": "The same clear rectangular plastic tub on the concrete floor in front of him, now holding cloudy water with a layer of white bubbles on the surface. Both of his bare feet are in it.",
  "scene": "SAME garage workshop as the attached reference image, with only two visible anchors: the open metal roller door letting in flat daylight, and a small red neon sign on the wall far behind him. Polished grey concrete floor.",
  "posture": "Sitting upright on a low wooden workshop stool, back straight, shoulders squared, leaning slightly forward with his forearms resting on his knees. NOT the seated slouch of the reference photo.",
  "composition": "TIGHT chest-up on him, his head and shoulders filling the upper two thirds. The tub with his feet in it sits in the lower third of the SAME frame, closer to the lens than his face. His hands are open in a natural mid-gesture between his knees. He speaks straight into the lens.",
  "camera": "chest level, straight-on, close, angled very slightly down",
  "state": "Start frame: feet in the water, hands open mid-gesture, speaking directly to camera.",
  "lighting": "Flat neutral overcast daylight coming in through the open roller door. The red neon is a small contained glow on the back wall only.",
  "realism": "UGC realism, real skin texture with visible pores, individual hair strands, subtle wrinkles, realistic shadows and reflections, iPhone-footage look, phone camera look not professional photography, no AI polish, no beauty smoothing, no blur anywhere, everything in sharp focus including background walls and details.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no studio, no plastic skin, no extra fingers, no blur, no gold jewelry, no seated slouch, no second person, no bottle in hand, no warm orange color cast, no yellow tint, no golden glow"
}
```

## K04 · T5, T6 · MECANISMO · GERAR DO ZERO · INSERT SEM ROSTO

```json
{
  "shot_id": "K04_foam_macro",
  "reference_use": "Close-up insert. No face. Use only the concrete floor surface and the flat daylight of the other shots.",
  "identity_main": "No face and no head in frame. Extreme close-up of two bare male feet resting inside a clear rectangular plastic tub of water.",
  "scene": "SAME polished grey concrete floor of the garage workshop, visible only as a narrow strip at the very top of the frame.",
  "composition": "Extreme macro close-up straight down into the tub, the water surface filling almost the entire frame. A THICK, DENSE, RAISED layer of white foam covers most of the surface, piled up in a mound of bubbles with real 3D volume, so much that only parts of the feet show through. Bubbles of many different sizes.",
  "camera": "macro, top-down, very close to the water surface",
  "state": "Start frame: the foam is thick and settled, with small bubbles rising and popping across the surface.",
  "lighting": "Flat neutral overcast daylight from above.",
  "realism": "UGC realism, real bubble texture with real light refraction, real wet skin, iPhone macro look, no AI polish, no blur anywhere, everything in sharp focus.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no face, no head, no studio, no cartoon look, no blur, no thin scattered foam, no flat sauce-like coating, no warm orange color cast, no yellow tint"
}
```

## K05 · T18 a T20 · PRODUTO · GERAR DO ZERO · ÂNCORA MELODY + PRODUCT.PNG

```json
{
  "shot_id": "K05_product",
  "reference_use": "TWO references attached. Use the FIRST image ONLY for Melody's face, identity, hair, tattoos, clothing and the garage workshop scene. Use the SECOND image for the EXACT supplement bottle he is holding, matching its shape, its white body, its purple and white label and its proportions exactly. Do NOT copy the framing of either reference.",
  "identity_main": "The EXACT MAN from the first reference image (Melody Carter), a muscular Black man with long dark box braids, a trimmed goatee and beard, an ornamental tattoo sleeve on his right arm and small chest tattoos.",
  "wardrobe": "White ribbed tank top, thin SILVER chain with a SILVER cross pendant.",
  "prop": "The EXACT supplement bottle from the second reference image, held upright in his right hand at chest height, label facing the camera and fully readable. The bottle is about 10 cm in height.",
  "scene": "SAME garage workshop as the first reference image, standing at the wooden workbench, with only two visible anchors: the open metal roller door letting in flat daylight, and a small red neon sign on the wall far behind him. The tub is gone.",
  "posture": "Standing upright at the workbench, shoulders squared, chin up, NOT the seated slouch of the reference photo. No legs or lap in frame.",
  "composition": "TIGHT chest-up. The bottle sits in the lower foreground, closer to the lens than his face, held steady and turned toward the camera, unmistakably the hero of the shot. His left hand is open near his chest in a natural mid-gesture. He speaks straight into the lens.",
  "camera": "chest level, straight-on, close",
  "state": "Start frame: bottle raised and steady toward the lens, speaking directly to camera.",
  "lighting": "Flat neutral overcast daylight coming in through the open roller door. The red neon is a small contained glow on the back wall only.",
  "realism": "UGC realism, real skin texture with visible pores, individual hair strands, subtle wrinkles, realistic shadows and reflections, iPhone-footage look, phone camera look not professional photography, no AI polish, no beauty smoothing, no blur anywhere, everything in sharp focus including background walls and details.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no studio, no plastic skin, no extra fingers, no blur, no gold jewelry, no seated slouch, no second person, no tub, no warm orange color cast, no yellow tint, no golden glow"
}
```

## K06 · T21, T22 · CTA · EDITAR do K05

```json
{
  "task": "edit the attached image, keep everything identical except the changes listed",
  "keep_identical": "Keep the man exactly the same: same face, same box braids, same goatee, same tattoos, same white tank top, same SILVER cross, same standing posture. Keep the SAME background exactly: workbench, open roller door, small red neon on the back wall, same lighting, same camera angle. Keep the supplement bottle EXACTLY the same shape and label.",
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

Estilo TikTok nativo, UGC. Preservar exatamente a identidade do Melody, rosto, tranças, cavanhaque, tatuagens, regata branca, cruz de PRATA, a oficina, a iluminação e o enquadramento do frame inicial. Sem legenda, sem texto gerado, sem música, sem pessoas extras.
```

**A câmera nunca é handheld de selfie neste vídeo.** As mãos dele estão nos props e a câmera do original é fixa, então NÃO incluir a instrução de braço parado.

---

### V01 · T1 · usa K01 · ⚠️ REVEAL CONTÍNUO, NÃO PODE CORTAR

```text
o avatar (HOMEM) fala em inglês com sotaque americano de homem negro, voz autêntica, dinâmica e emocional, como se exigisse ser ouvido, a seguinte frase: "Pour hydrogen peroxide on your feet, brother, and watch what happens. Because if it starts foaming, it just found what has been living on them."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: o líquido continua caindo no pé dele e a espuma branca vai crescendo em volta, de um anel fino até virar uma camada grossa e alta de bolhas que cobre os dedos e se espalha pelo concreto. Tudo acontece no mesmo take, sem nenhum corte, e o pé fica em quadro o tempo inteiro.

câmera: fixa, leve handheld natural

som ambiente: oficina silenciosa, líquido escorrendo e bolhas estourando, sem música
```

### V02 · T2 · usa K02

```text
o avatar (HOMEM) fala em inglês com sotaque americano de homem negro, voz autêntica e direta, a seguinte frase: "Half a cup of hydrogen peroxide into a foot bath. Two cups of warm water."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ele termina de despejar a garrafa na bacia, pousa ela no chão, pega a jarra de vidro e despeja a água dentro.

câmera: fixa, leve handheld natural

som ambiente: oficina silenciosa, água caindo, sem música
```

### V03 · T3 · usa K02

```text
o avatar (HOMEM) fala em inglês com sotaque americano de homem negro, voz autêntica e direta, a seguinte frase: "And one heaping spoonful of baking soda."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ele pega a colher de metal cheia do pó branco, ergue ela sobre a bacia e vira, deixando o pó cair na água.

câmera: fixa, leve handheld natural

som ambiente: oficina silenciosa, sem música
```

### V04 · T4 · usa K03

```text
o avatar (HOMEM) fala em inglês com sotaque americano de homem negro, voz autêntica e direta, a seguinte frase: "Soak for fifteen minutes and watch the foam. Especially if you are past forty and your feet go cold at night."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: corte duro, ele já está sentado no banquinho com os dois pés dentro da bacia. ele aponta pra baixo, pra bacia, ao dizer a primeira frase e depois olha firme pra câmera.

câmera: fixa, leve handheld natural

som ambiente: oficina silenciosa, sem música, sem ruído de fundo
```

### V05 · T5 · usa K04 · B-ROLL

```text
(sem fala no take: a fala 5 do roteiro entra como voz-over na edição)

o que acontece no vídeo: a espuma branca continua borbulhando na superfície da água. bolhas pequenas sobem e estouram sem parar, e a camada de espuma se move devagar.

câmera: fixa, macro de cima

som ambiente: oficina silenciosa, bolhas estourando, sem música
```

### V06 · T6 · usa K04 · B-ROLL

```text
(sem fala no take: a fala 6 do roteiro entra como voz-over na edição)

o que acontece no vídeo: um dos pés se mexe devagar dentro da água e abre um rasgo na camada de espuma, que volta a fechar em seguida.

câmera: fixa, macro de cima

som ambiente: oficina silenciosa, água mexendo, sem música
```

### V07 · T7 · usa K03

```text
o avatar (HOMEM) fala em inglês com sotaque americano de homem negro, voz autêntica e confiante, a seguinte frase: "Fifteen minutes in that tub does what a whole year of showers never got close to."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: corte duro, ele está de volta no banquinho. ele abre as duas mãos com as palmas pra cima num gesto de constatação.

câmera: fixa, leve push-in

som ambiente: oficina silenciosa, sem música, sem ruído de fundo
```

### V08 · T8 · usa K03

```text
o avatar (HOMEM) fala em inglês com sotaque americano de homem negro, voz autêntica e direta, a seguinte frase: "It clears the odor, it softens cracked heels, and it peels the dead skin right off."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ele conta três nos dedos, um pra cada item, enquanto fala.

câmera: fixa, leve handheld natural

som ambiente: oficina silenciosa, sem música, sem ruído de fundo
```

### V09 · T9 · usa K03

```text
o avatar (HOMEM) fala em inglês com sotaque americano de homem negro, voz autêntica e animada, a seguinte frase: "And even thick yellow nails start growing out clear again. You will be shocked."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ele levanta as sobrancelhas e balança a cabeça uma vez na última frase.

câmera: fixa, leve handheld natural

som ambiente: oficina silenciosa, sem música, sem ruído de fundo
```

### V10 · T10 · usa K03

```text
o avatar (HOMEM) fala em inglês com sotaque americano de homem negro, voz mais baixa e séria, a seguinte frase: "Those four you can see. The one you cannot see is why they keep coming back every year."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ele para de gesticular na primeira frase, se inclina um pouco pra frente e baixa o tom na segunda.

câmera: fixa, leve push-in

som ambiente: oficina silenciosa, sem música, sem ruído de fundo
```

### V11 · T11 · usa K03

```text
o avatar (HOMEM) fala em inglês com sotaque americano de homem negro, voz calma e generosa, a seguinte frase: "You did the right thing tonight. You just did it from the outside in."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ele assente uma vez na primeira frase e depois move a mão de fora pra dentro no ar na segunda.

câmera: fixa, leve handheld natural

som ambiente: oficina silenciosa, sem música, sem ruído de fundo
```

### V12 · T12 · usa K03

```text
o avatar (HOMEM) fala em inglês com sotaque americano de homem negro, voz firme, a seguinte frase: "Cracked heels and thick yellow nails are not a hygiene problem. Skin and nail are the last two things your blood feeds."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ele balança a cabeça na primeira frase e ergue dois dedos na segunda.

câmera: fixa, leve handheld natural

som ambiente: oficina silenciosa, sem música, sem ruído de fundo
```

### V13 · T13 · usa K03

```text
o avatar (HOMEM) fala em inglês com sotaque americano de homem negro, voz autêntica, dinâmica e emocional, a seguinte frase: "Your feet are the end of the pipe. When the pressure drops, the end of the pipe goes first."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ele estende o braço e aponta pra ponta dos próprios dedos ao falar da ponta do cano.

câmera: fixa, leve handheld natural

som ambiente: oficina silenciosa, sem música, sem ruído de fundo
```

### V14 · T14 · usa K03

```text
o avatar (HOMEM) fala em inglês com sotaque americano de homem negro, voz mais baixa e pessoal, a seguinte frase: "And the same flow that stopped reaching your feet stopped reaching the part that used to answer on its own."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ele para completamente de gesticular e olha direto pra lente enquanto fala.

câmera: fixa, leve push-in

som ambiente: oficina silenciosa, sem música, sem ruído de fundo
```

### V15 · T15 · usa K03

```text
o avatar (HOMEM) fala em inglês com sotaque americano de homem negro, voz honesta e equilibrada, a seguinte frase: "So keep soaking. It cleans what is on you. What puts pressure back in that line is saffron."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ele aponta pra bacia nas duas primeiras frases e depois abre a mão pra cima na terceira.

câmera: fixa, leve handheld natural

som ambiente: oficina silenciosa, sem música, sem ruído de fundo
```

### V16 · T16 · usa K03

```text
o avatar (HOMEM) fala em inglês com sotaque americano de homem negro, voz compreensiva, a seguinte frase: "But it takes six weeks straight, and most men quit a daily ritual by day nine. That is not weakness."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: a expressão dele suaviza e ele balança a cabeça uma vez, devagar, na última frase.

câmera: fixa, leve handheld natural

som ambiente: oficina silenciosa, sem música, sem ruído de fundo
```

### V17 · T17 · usa K03

```text
o avatar (HOMEM) fala em inglês com sotaque americano de homem negro, voz séria, quase de aviso, a seguinte frase: "And do not grab any bottle either. No two harvests carry the same strength, and that is why yours did nothing."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ele levanta a palma da mão num gesto de pare na primeira frase e depois aponta pra câmera na última.

câmera: fixa, leve push-in

som ambiente: oficina silenciosa, sem música, sem ruído de fundo
```

### V18 · T18 · usa K05 · **O TAKE DO PRODUTO**

```text
o avatar (HOMEM) fala em inglês com sotaque americano de homem negro, voz confiante e de autoridade, a seguinte frase: "This is the only one I put my clients on. Korella Saffron from Amazon. Every batch tested, so your bottle is the one I opened."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: corte duro, ele está em pé na bancada e a bacia sumiu. ele ergue o frasco na direção da câmera ao dizer o nome e o mantém firme e parado, com o rótulo virado pra lente, até o fim da fala.

câmera: fixa, leve handheld natural

som ambiente: oficina silenciosa, sem música, sem ruído de fundo
```

### V19 · T19 · usa K05

```text
o avatar (HOMEM) fala em inglês com sotaque americano de homem negro, voz aberta e confiante, a seguinte frase: "One capsule with your coffee, nothing to quit. And every man I have put on it comes back asking why nobody told him sooner."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ele continua segurando o frasco firme com uma mão e abre a outra num gesto natural enquanto fala.

câmera: fixa, leve handheld natural

som ambiente: oficina silenciosa, sem música, sem ruído de fundo
```

### V20 · T20 · usa K05

```text
o avatar (HOMEM) fala em inglês com sotaque americano de homem negro, voz mais quente e pessoal, a seguinte frase: "Week two your feet stop going cold at night. Week four your wife is the one who brings it up first."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ele conta dois nos dedos da mão livre, um pra cada semana, e abre um sorriso curto na última palavra.

câmera: fixa, leve push-in

som ambiente: oficina silenciosa, sem música, sem ruído de fundo
```

### V21 · T21 · usa K06

```text
o avatar (HOMEM) fala em inglês com sotaque americano de homem negro, voz direta e convidativa, a seguinte frase: "You have got a shower coming tonight. Comment yes and I will send you the link myself."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ele mantém o frasco erguido ao lado do rosto e aponta pra baixo com a outra mão, na direção dos comentários, ao dizer "comment yes".

câmera: fixa, leve push-in

som ambiente: oficina silenciosa, sem música, sem ruído de fundo
```

### V22 · T22 · usa K06

```text
o avatar (HOMEM) fala em inglês com sotaque americano de homem negro, voz direta, a seguinte frase: "But make sure you follow me first, or it will not let me reach you."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ele aponta uma vez pra câmera, direto, e termina com um aceno curto de cabeça, ainda segurando o frasco ao lado do rosto.

câmera: fixa, leve push-in

som ambiente: oficina silenciosa, sem música, sem ruído de fundo
```

---

## Mapa de âncoras

| Keyframe | Referências a anexar | Modelo |
|---|---|---|
| K01 | âncora Melody | Nano Banana **Pro**, várias variações. **Frame herói** |
| K02 | âncora Melody | Nano Banana 2 |
| K03 | âncora Melody | Nano Banana 2. É o keyframe que atende **12 takes**, vale regenerar até sair perfeito |
| K04 | nenhuma, insert sem rosto | Nano Banana 2 |
| K05 | **âncora Melody + product.png** | Nano Banana 2 |
| K06 | **K05 aprovado** | Nano Banana 2, comando de edição |

---

## Montagem no CapCut

- Timeline 1080x1920, 30 fps. Cortes duros entre todos os takes.
- **Quatro cortes de peso:** V03 para V04 (ele senta, a bacia enche), V04 para V05 (entra o macro), V06 para V07 (volta o rosto) e V17 para V18 (some a bacia, entra o frasco).
- **V05 e V06 levam as falas 5 e 6 como voz-over.** São b-roll sem rosto.
- Cortar o silêncio inicial de cada clipe.
- **Segurar um beat extra de silêncio no fim do V14**, depois de "used to answer on its own". A pausa é o que faz a frase cair.
- Legendas grandes estilo Captions.ai Prism Pro, palavra destacada em vermelho, na altura do peito. **No V01 a legenda não pode cobrir o pé nem a espuma**, que é onde a transformação acontece.
- Manter `YES` isolado na tela no CTA.
- Color grading: temp -3, tint +2, saturação -6, exposição -3, contraste +12, highlight -35, shadow +18, fade +6.

## Gates de qualidade

1. Melody é **HOMEM** e é o mesmo em todos os clipes, com a cruz de **PRATA** em todos, nunca ouro.
2. As tranças e o cavanhaque estão iguais em todos os planos.
3. **O V01 não tem corte.** A espuma cresce dentro do take, com o pé em quadro o tempo inteiro. Se vier cortado, o hook morreu.
4. **O K01 sai com POUCA espuma**, só um anel fino. Se já saiu com espuma alta, o V01 não tem pra onde evoluir.
5. **A água do K02 está LIMPA e sem espuma.** Se saiu turva, o V02 perde a ação.
6. **O K04 tem MONTANHA de espuma**, camada grossa e alta com volume 3D. Camada fininha tipo molho, regenerar.
7. **A garrafa não tem rótulo nenhum**, nem inventado. Nenhuma marca legível em quadro em nenhum take.
8. Nenhuma legenda ou texto foi gerado dentro da imagem.
9. **O frasco do Korella aparece do K05 em diante e o rótulo está legível e igual ao product.png.** Tamanho de uns 10 cm, nunca gigante.
10. **O nome "Korella Saffron" é dito no V18, no mesmo take em que o frasco entra em quadro.**
11. **O K06 é o plano mais fechado do vídeo inteiro.**
12. Fundo reconhecível e não inventariado: **duas âncoras apenas**, a porta de enrolar e o neon.
13. **A cena não está banhada de laranja nem de amarelo.** A luz é neutra de dia nublado e o neon fica contido na parede.
14. Nenhuma imagem tem fundo desfocado.
15. Mãos com cinco dedos e pés com cinco dedos, sem fusão com a garrafa, a bacia nem o frasco.
16. Ele **não larga o prop** enquanto argumenta: os pés ficam na bacia do V04 ao V17.
17. `yes` e o follow gate estão os dois no CTA final.
18. **Nenhuma menção a preço, desconto, gratuidade ou dosagem em miligramas em nenhum take.**
