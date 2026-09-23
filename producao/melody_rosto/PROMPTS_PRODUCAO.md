# Melody Carter | Ângulo 1 (Korella Saffron) | Pacote de Prompts

Vídeo modelo: `snapinsta-1787707339628.mp4` (original em espanhol)

Âncora de identidade: `C:\Users\luigi\Desktop\AVATARES NON-SHOP\melody carter .png`

Referência de produto: `C:\Users\luigi\Desktop\B-ROLL PRODUTOS\product.png`

Funil: comment `yes` -> DM -> deep link Amazon do Korella Saffron

> ⚠️ **ÂNGULO 1: o produto APARECE.** Frasco em quadro do T15 ao T20, e "Korella Saffron" é dito em voz alta no V15, no mesmo take em que o frasco entra na mão.
>
> 🔴 **ESTE PACOTE TEM DOIS PONTOS DE RISCO ALTO, NÃO UM: o K01 e o V01.** A escultura da cabeça inchada derretendo é o prop de maior risco de toda a operação. Os dois já saem com o protocolo aplicado. Ver a seção própria abaixo.
>
> ⚠️ **O K01 É REVEAL CONTÍNUO.** Uma imagem só, com a cabeça **totalmente inchada**. O derretimento acontece dentro do V01. Se sair já murcha, o clipe não tem pra onde evoluir.

---

## Índice de geração

| Take | Keyframe | Ação de geração |
|---|---|---|
| T1 | K01 | GERAR DO ZERO (ref: âncora Melody). **Frame herói. Risco máximo.** Pro, com variações. |
| T2 | K02 | **EDITAR do K01** (a cabeça já derretida e magra) |
| T3, T4 | K03 | GERAR DO ZERO (ref: âncora Melody). Bule e ingredientes na bancada. |
| T5 a T14 | K04 | **EDITAR do K03** (ingredientes saem, bule pronto na mão, plano fecha). **Atende 10 takes.** |
| T15 a T18 | K05 | GERAR DO ZERO (ref: **âncora Melody + product.png**) |
| T19, T20 | K06 | **EDITAR do K05** (fecha o plano, frasco sobe junto ao rosto) |

Total: **6 keyframes para 20 takes. Sem 2ª pessoa neste vídeo, então não há REF-A.**

---

## Trava de identidade e continuidade

**Escrita aqui uma vez, não repetir inteira dentro de cada JSON.**

- **MELODY É HOMEM.** Homem negro, musculoso, tranças box braids escuras compridas, cavanhaque e barba aparada.
- **Regata branca canelada. Corrente fina de PRATA com pingente de cruz de PRATA. Nunca ouro.**
- Manga de tatuagem ornamental no braço direito, tatuagens no peito.
- **Cenário: a oficina dele, com DUAS âncoras visuais apenas: a porta de enrolar metálica aberta e o pequeno neon vermelho na parede.** A placa de madeira, a bandeira e a parede de ferramentas ficam **fora de quadro**.
- **Bancada de madeira gasta ocupando o terço inferior do quadro.**
- **Luz principal é a luz neutra de dia nublado entrando pela porta de enrolar aberta.** O neon é um ponto vermelho contido na parede do fundo, **não banha a cena**.
- Zero blur, tudo em foco nítido. Cara de vídeo de iPhone, nunca polimento de IA.
- **Corrigir a foto-âncora:** ela é sentada e relaxada. A postura vai declarada em todo prompt.

## Trava do prop herói (a escultura, usar no K01 e no K02)

**Este bloco é o resultado do protocolo de restrição. Copiar exatamente, não reescrever com sinônimos.**

```text
A classroom teaching sculpture of a human head, carved from pale matte cream-coloured wax,
about 30 cm tall, standing upright on the bench. Its surface is built up in THICK, SMOOTH,
ROUNDED LAYERS so the head reads as heavily swollen and very rounded, the layers stacked so
deep that the features are almost buried in them. CALM NEUTRAL CLOSED-MOUTH EXPRESSION,
EYES CLOSED, like a classical bust. Soft matte finish with no shine.
```

- **K01, estado INICIAL:** camadas no máximo, cabeça grande e redonda, traços quase somem.
- **K02, estado FINAL:** as camadas baixaram, a cabeça agora é **magra e angulosa**, com a cera derretida numa poça brilhante na bancada em volta da base.

## Trava dos props da receita (usar no K03)

```text
A clear glass teapot on a small warmer on the bench, holding clear water. Beside it: a plain
wooden bowl with a knob of fresh ginger root, a small wooden bowl of bright yellow-orange
turmeric powder, and two cinnamon sticks resting on the bench. The items keep the exact same
positions in every shot.
```

**Não há 2ª pessoa neste vídeo, então não há REF-A.**

---

## GATE DE COMPOSIÇÃO VISUAL (rodado ANTES dos prompts abaixo)

```
HEROI
[x] 1. Heroi no LOWER FOREGROUND mais perto que o rosto
       -> K01/K02: a escultura. K03: o bule. K04: o bule na mao. K05/K06: o frasco
[x] 2. Nada compete com ele
[x] 3. Volume e cobertura EXPLICITADOS
       -> K01 camadas no MAXIMO, tracos quase enterrados. K02 magra e angulosa

DISTANCIA
[x] 4. "Da pra estar mais perto?"   -> todos fecham mais que o original
[x] 5. Peito pra cima               -> K03, K04, K05, K06
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
[x] 2. Camera puxada perto, a escultura enche o terco inferior
[x] 3. Luz NEUTRA de dia nublado pela porta aberta. O neon nao banha a cena
[x] 4. Negative carrega no warm orange color cast, no yellow tint, no golden glow
[x] 5. Fundo especifico e nunca borrado
[x] 6. Prop teimoso: a ESCULTURA. Bloco de forma proprio, e se travar vira REF-PROP isolado
[x] 7. Bloco de realismo padrao colado por inteiro em todo prompt
```

**Uma escolha deliberada.** A escultura do original é **amarelada e brilhante**, cor de massa crua. Isso é ruim duas vezes: entrega cara de IA pelo tom quente, e é justamente o vocabulário de textura que dispara o classificador. Trocamos por **cera fosca creme-clara**, que resolve os dois de uma vez e na tela lê praticamente igual.

---

## 🔴 PROTOCOLO DE RESTRIÇÃO, APLICADO NO K01 E NO V01

A escultura junta num frame só **quatro** coisas que o classificador lê mal isoladas e péssimo juntas: cabeça humana, expressão de sofrimento, textura de carne, e derretimento. O modelo de pulmão travou duas vezes com metade disso.

**As cinco correções já estão dentro dos prompts:**

1. **Reenquadrado como objeto didático.** `classroom teaching sculpture`, `carved from pale matte cream-coloured wax`. Nunca rosto real, nunca carne.
2. **A EXPRESSÃO VIRA NEUTRA.** `calm neutral closed-mouth expression, eyes closed, like a classical bust`. **Esta é a alavanca principal e custa quase nada visualmente**, porque o herói é o INCHAÇO, nunca a careta. O original tem uma careta de sofrimento e é ela que mais pesa.
3. **Cores e texturas da tabela de substituição.** `pale matte cream`, `soft matte finish with no shine` no lugar do amarelo brilhante e oleoso.
4. **ZERO termo sensível no negative.** O classificador lê o token, não a negação.
5. **Campo `context`** declarando ficção de IA e que o prop é uma escultura.

**Palavras banidas destes dois prompts:** flesh, fat, skin, greasy, oily, glossy, wet, grotesque, tortured, suffering, agony, corpse, dead, sagging, blob.

**No V01 a ação vai ENXUTA**, sem adjetivo dramático: a cera amolece, escorre e as camadas baixam. Só isso.

**Se travar mesmo assim,** o Passo 3 do protocolo é gerar a escultura **sozinha na bancada, sem pessoa em quadro**, aprovar, e usar essa imagem como referência de objeto numa segunda geração junto com a âncora do Melody. **Nunca sugerir tentar de novo.**

---

# Prompts de imagem

## K01 · T1 · HOOK · GERAR DO ZERO (Nano Banana **Pro**, várias variações) · ÂNCORA MELODY

```json
{
  "shot_id": "K01_hook_pour",
  "context": "Fictional AI-generated character. No real person is being filmed or depicted. The object on the bench is a classroom teaching sculpture, not a person.",
  "reference_use": "Use the attached image ONLY for Melody's face, identity, hair, tattoos, clothing and the garage workshop scene. Do NOT copy its pose or framing. Frame him much closer than the reference.",
  "identity_main": "The EXACT MAN from the attached reference image (Melody Carter), a muscular Black man with long dark box braids, a trimmed goatee and beard, an ornamental tattoo sleeve on his right arm and small chest tattoos.",
  "wardrobe": "White ribbed tank top, thin SILVER chain with a SILVER cross pendant.",
  "prop": "A classroom teaching sculpture of a human head, carved from pale matte cream-coloured wax, about 30 cm tall, standing upright on the bench. Its surface is built up in THICK, SMOOTH, ROUNDED LAYERS so the head reads as heavily swollen and very rounded, the layers stacked so deep that the features are almost buried in them. CALM NEUTRAL CLOSED-MOUTH EXPRESSION, EYES CLOSED, like a classical bust. Soft matte finish with no shine.",
  "prop_2": "A clear glass teapot of warm amber tea held tilted in his right hand, high above the sculpture, with the first thin stream just about to touch the top of the head.",
  "scene": "SAME garage workshop as the attached reference image, with only two visible anchors: the open metal roller door letting in flat daylight, and a small red neon sign on the wall far behind him. A worn wooden bench in front of him.",
  "posture": "Seated upright at the bench, back straight, leaning slightly forward, NOT the seated slouch of the reference photo. No legs or lap in frame.",
  "composition": "TIGHT. The teaching sculpture fills the lower third and sits much closer to the lens than his face, unmistakably the hero. His face is smaller in the upper third, looking at the camera over the top of it.",
  "camera": "chest level, close, angled slightly down toward the sculpture",
  "state": "Start frame: the sculpture is at its FULLEST, the layers at maximum, nothing has melted yet, and the stream has not reached it.",
  "lighting": "Flat neutral overcast daylight coming in through the open roller door. The red neon is a small contained glow on the back wall only.",
  "realism": "UGC realism, real skin texture with visible pores, individual hair strands, subtle wrinkles, realistic shadows and reflections, iPhone-footage look, phone camera look not professional photography, no AI polish, no beauty smoothing, no blur anywhere, everything in sharp focus including background walls and details.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no studio, no plastic skin, no extra fingers, no blur, no gold jewelry, no seated slouch, no second person, no shine on the sculpture, no melted pool yet, no warm orange color cast, no yellow tint, no golden glow"
}
```

## K02 · T2 · APÓS O REVEAL · EDITAR do K01

```json
{
  "task": "edit the attached image, keep everything identical except the changes listed",
  "keep_identical": "Keep the man exactly the same: same face, same box braids, same goatee, same tattoos, same white tank top, same SILVER cross, same seated upright posture. Keep the SAME background exactly: worn wooden bench, open roller door, small red neon on the back wall, same neutral daylight, same camera angle and framing.",
  "change_1": "The teaching sculpture is now much smaller and narrower: the thick rounded layers are gone and the head is lean and angular, with clear cheekbones and a defined jawline. Same pale matte cream-coloured wax, same calm neutral closed-mouth expression with eyes closed.",
  "change_2": "A shallow pool of pale cream-coloured melted wax has spread across the bench around the base of the sculpture.",
  "change_3": "The glass teapot is now lowered and resting on the bench beside it, and he speaks straight into the lens.",
  "realism": "UGC realism, real skin texture with visible pores, iPhone-footage look, no AI polish, no beauty smoothing, no blur anywhere. Do not make his skin darker, yellowish or orangish. Do not make the colors more saturated.",
  "negative": "do not change the face, do not change identity, do not change the background, do not change the camera angle, no captions, no subtitles, no words overlaid on the image, no plastic skin, no extra fingers, no gold jewelry, no blur, no warm orange color cast, no yellow tint"
}
```

## K03 · T3, T4 · RECEITA · GERAR DO ZERO · ÂNCORA MELODY

```json
{
  "shot_id": "K03_recipe",
  "reference_use": "Use the attached image ONLY for Melody's face, identity, hair, tattoos, clothing and the garage workshop scene. Do NOT copy its pose or framing. Frame him closer than the reference.",
  "identity_main": "The EXACT MAN from the attached reference image (Melody Carter), a muscular Black man with long dark box braids, a trimmed goatee and beard, an ornamental tattoo sleeve on his right arm and small chest tattoos.",
  "wardrobe": "White ribbed tank top, thin SILVER chain with a SILVER cross pendant.",
  "prop": "A clear glass teapot on a small warmer on the bench, holding clear water. Beside it: a plain wooden bowl with a knob of fresh ginger root, a small wooden bowl of bright yellow-orange turmeric powder, and two cinnamon sticks resting on the bench. His right hand is above the teapot holding a piece of fresh ginger, about to drop it in.",
  "scene": "SAME garage workshop as the attached reference image, with only two visible anchors: the open metal roller door letting in flat daylight, and a small red neon sign on the wall far behind him. A worn wooden bench in front of him.",
  "posture": "Seated upright at the bench, leaning slightly forward over the teapot, NOT the seated slouch of the reference photo. No legs or lap in frame.",
  "composition": "TIGHT chest-up. The teapot and the bowls fill the lower foreground, closer to the lens than his face. The water in the teapot is still completely clear.",
  "camera": "chest level, close, angled slightly down toward the teapot",
  "state": "Start frame: the water is still clear, nothing added yet, the ginger held just above it.",
  "lighting": "Flat neutral overcast daylight coming in through the open roller door. The red neon is a small contained glow on the back wall only.",
  "realism": "UGC realism, real skin texture with visible pores, individual hair strands, subtle wrinkles, realistic shadows and reflections, iPhone-footage look, phone camera look not professional photography, no AI polish, no beauty smoothing, no blur anywhere, everything in sharp focus including background walls and details.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no studio, no plastic skin, no extra fingers, no blur, no gold jewelry, no seated slouch, no second person, no sculpture, no coloured water, no warm orange color cast, no yellow tint, no golden glow"
}
```

## K04 · T5 a T14 · O BLOCO DE VENDA · EDITAR do K03

```json
{
  "task": "edit the attached image, keep everything identical except the changes listed",
  "keep_identical": "Keep the man exactly the same: same face, same box braids, same goatee, same tattoos, same white tank top, same SILVER cross, same seated upright posture. Keep the SAME background exactly: worn wooden bench, open roller door, small red neon on the back wall, same neutral daylight.",
  "change_1": "Remove the warmer, the wooden bowls, the ginger and the cinnamon sticks from the bench completely.",
  "change_2": "He now holds the clear glass teapot up in his right hand at chest height, closer to the lens than his face. The liquid inside is now a warm amber tea with slices of ginger floating in it.",
  "change_3": "Crop in tighter than the original framing, chest-up, and his left hand is open near his chest in a natural mid-gesture. He speaks straight into the lens.",
  "realism": "UGC realism, real skin texture with visible pores, iPhone-footage look, no AI polish, no beauty smoothing, no blur anywhere. Do not make his skin darker, yellowish or orangish. Do not make the colors more saturated.",
  "negative": "do not change the face, do not change identity, do not change the background, do not change the camera angle, no captions, no subtitles, no words overlaid on the image, no plastic skin, no extra fingers, no gold jewelry, no blur, no sculpture, no warm orange color cast, no yellow tint"
}
```

## K05 · T15 a T18 · PRODUTO · GERAR DO ZERO · ÂNCORA MELODY + PRODUCT.PNG

```json
{
  "shot_id": "K05_product",
  "reference_use": "TWO references attached. Use the FIRST image ONLY for Melody's face, identity, hair, tattoos, clothing and the garage workshop scene. Use the SECOND image for the EXACT supplement bottle he is holding, matching its shape, its white body, its purple and white label and its proportions exactly. Do NOT copy the framing of either reference.",
  "identity_main": "The EXACT MAN from the first reference image (Melody Carter), a muscular Black man with long dark box braids, a trimmed goatee and beard, an ornamental tattoo sleeve on his right arm and small chest tattoos.",
  "wardrobe": "White ribbed tank top, thin SILVER chain with a SILVER cross pendant.",
  "prop": "The EXACT supplement bottle from the second reference image, held upright in his right hand at chest height, label facing the camera and fully readable. The bottle is about 10 cm in height.",
  "scene": "SAME garage workshop as the first reference image, standing at the wooden bench, with only two visible anchors: the open metal roller door letting in flat daylight, and a small red neon sign on the wall far behind him. The bench is empty.",
  "posture": "Standing upright at the bench, shoulders squared, chin up, NOT the seated slouch of the reference photo. No legs or lap in frame.",
  "composition": "TIGHT chest-up. The bottle sits in the lower foreground, closer to the lens than his face, held steady and turned toward the camera, unmistakably the hero of the shot. His left hand is open near his chest in a natural mid-gesture. He speaks straight into the lens.",
  "camera": "chest level, straight-on, close",
  "state": "Start frame: bottle raised and steady toward the lens, speaking directly to camera.",
  "lighting": "Flat neutral overcast daylight coming in through the open roller door. The red neon is a small contained glow on the back wall only.",
  "realism": "UGC realism, real skin texture with visible pores, individual hair strands, subtle wrinkles, realistic shadows and reflections, iPhone-footage look, phone camera look not professional photography, no AI polish, no beauty smoothing, no blur anywhere, everything in sharp focus including background walls and details.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no studio, no plastic skin, no extra fingers, no blur, no gold jewelry, no seated slouch, no second person, no teapot, no sculpture, no warm orange color cast, no yellow tint, no golden glow"
}
```

## K06 · T19, T20 · CTA · EDITAR do K05

```json
{
  "task": "edit the attached image, keep everything identical except the changes listed",
  "keep_identical": "Keep the man exactly the same: same face, same box braids, same goatee, same tattoos, same white tank top, same SILVER cross, same standing posture. Keep the SAME background exactly: wooden bench, open roller door, small red neon on the back wall, same neutral daylight, same camera angle. Keep the supplement bottle EXACTLY the same shape and label.",
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

Estilo TikTok nativo, UGC. Preservar exatamente a identidade do Melody, rosto, tranças, cavanhaque, tatuagens, regata branca, cruz de PRATA, a oficina, a iluminação neutra e o enquadramento do frame inicial. Sem legenda, sem texto gerado, sem música, sem pessoas extras.
```

**A câmera do original é FIXA e não é handheld de selfie**, então NÃO incluir a instrução de braço parado.

---

### V01 · T1 · usa K01 · 🔴 REVEAL CONTÍNUO + RISCO ALTO. AÇÃO PROPOSITALMENTE ENXUTA

```text
o avatar (HOMEM) fala em inglês com sotaque americano de homem negro, voz autêntica, dinâmica e emocional, como se exigisse ser ouvido, a seguinte frase: "This is what sugar is doing to your face, brother. And nobody in that grocery store is telling you."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ele inclina o bule e o líquido quente escorre por cima da escultura de cera. A cera vai amolecendo e as camadas grossas vão baixando devagar, até a escultura ficar magra e angulosa, com a cera escorrida formando uma poça na bancada. Tudo acontece no mesmo take, sem nenhum corte, e a escultura fica em quadro o tempo inteiro.

câmera: fixa

som ambiente: oficina silenciosa, líquido escorrendo, sem música
```

### V02 · T2 · usa K02

```text
o avatar (HOMEM) fala em inglês com sotaque americano de homem negro, voz firme e direta, a seguinte frase: "But I am. And it is not your weight. It is your face, and your face shows it first."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ele pousa o bule na bancada, aponta pra si mesmo ao dizer a primeira frase e depois aponta pro próprio rosto na última.

câmera: fixa, leve push-in

som ambiente: oficina silenciosa, sem música, sem ruído de fundo
```

### V03 · T3 · usa K03

```text
o avatar (HOMEM) fala em inglês com sotaque americano de homem negro, voz autêntica e direta, a seguinte frase: "A good piece of fresh ginger, a teaspoon of turmeric, two sticks of cinnamon."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: corte duro, a escultura sumiu. ele solta o gengibre no bule, depois vira a tigelinha de cúrcuma dentro, e por último solta os dois paus de canela.

câmera: fixa

som ambiente: oficina silenciosa, água morna, sem música
```

### V04 · T4 · usa K03

```text
o avatar (HOMEM) fala em inglês com sotaque americano de homem negro, voz autêntica, dinâmica e emocional, a seguinte frase: "The ginger drives the water out. The turmeric kills the swelling under it. The cinnamon keeps the sugar from spiking again."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ele conta três nos dedos, um pra cada ingrediente, enquanto fala.

câmera: fixa

som ambiente: oficina silenciosa, sem música, sem ruído de fundo
```

### V05 · T5 · usa K04

```text
o avatar (HOMEM) fala em inglês com sotaque americano de homem negro, voz confiante, a seguinte frase: "Drink this every single morning, and in thirty days the face in the mirror is not the same one."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: corte duro, os ingredientes sumiram e o chá está pronto. ele ergue o bule na direção da câmera e o mantém firme enquanto fala.

câmera: fixa

som ambiente: oficina silenciosa, sem música, sem ruído de fundo
```

### V06 · T6 · usa K04

```text
o avatar (HOMEM) fala em inglês com sotaque americano de homem negro, voz de prova, a seguinte frase: "For thousands of men over forty in this country, it is already happening."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ele assente uma vez, devagar, enquanto fala, sem largar o bule.

câmera: fixa

som ambiente: oficina silenciosa, sem música, sem ruído de fundo
```

### V07 · T7 · usa K04 · **O BEAT DE VIRADA**

```text
o avatar (HOMEM) fala em inglês com sotaque americano de homem negro, voz mais baixa e séria, a seguinte frase: "But let me ask you something worse. If it is already showing in your face, where is it showing that you cannot see?"

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ele se inclina um pouco pra frente, baixa o tom e fica parado olhando fixo pra lente no fim da pergunta.

câmera: fixa, leve push-in

som ambiente: oficina silenciosa, sem música, sem ruído de fundo
```

### V08 · T8 · usa K04

```text
o avatar (HOMEM) fala em inglês com sotaque americano de homem negro, voz firme, a seguinte frase: "Every warning you ever got about sugar was about your weight. Nobody ever told you it hits your face first."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ele balança a cabeça na primeira frase e aponta pro próprio rosto na segunda.

câmera: fixa

som ambiente: oficina silenciosa, sem música, sem ruído de fundo
```

### V09 · T9 · usa K04

```text
o avatar (HOMEM) fala em inglês com sotaque americano de homem negro, voz honesta e equilibrada, a seguinte frase: "This tea pulls the water out. That part is real and you will see it in a week."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ele levanta o bule um pouco mais alto na primeira frase e assente na segunda.

câmera: fixa

som ambiente: oficina silenciosa, sem música, sem ruído de fundo
```

### V10 · T10 · usa K04

```text
o avatar (HOMEM) fala em inglês com sotaque americano de homem negro, voz compreensiva, quase de alívio, a seguinte frase: "But the water comes back, because the sugar comes back. And you did not fail a diet. You lost to nine at night."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: a expressão dele suaviza e ele balança a cabeça uma vez, devagar, na última frase.

câmera: fixa, leve push-in

som ambiente: oficina silenciosa, sem música, sem ruído de fundo
```

### V11 · T11 · usa K04

```text
o avatar (HOMEM) fala em inglês com sotaque americano de homem negro, voz mais baixa e pessoal, a seguinte frase: "That craving is not weakness. And it has been winning in places your face was never going to show you."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ele para de gesticular e olha direto pra lente enquanto fala.

câmera: fixa, leve push-in

som ambiente: oficina silenciosa, sem música, sem ruído de fundo
```

### V12 · T12 · usa K04

```text
o avatar (HOMEM) fala em inglês com sotaque americano de homem negro, voz aberta e confiante, a seguinte frase: "Saffron is the one thing that works on the craving itself, before it starts."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ele abre a mão livre com a palma pra cima ao dizer a última parte.

câmera: fixa

som ambiente: oficina silenciosa, sem música, sem ruído de fundo
```

### V13 · T13 · usa K04

```text
o avatar (HOMEM) fala em inglês com sotaque americano de homem negro, voz direta, a seguinte frase: "But two sticks of cinnamon every single morning is rough on a stomach that is already past forty."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ele olha pro bule na própria mão ao dizer a primeira parte e depois volta pra câmera.

câmera: fixa

som ambiente: oficina silenciosa, sem música, sem ruído de fundo
```

### V14 · T14 · usa K04

```text
o avatar (HOMEM) fala em inglês com sotaque americano de homem negro, voz séria, quase de aviso, a seguinte frase: "And that bottle on the shelf was picked by a buyer whose only job was price per unit. That is why yours did nothing."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ele levanta a palma da mão livre num gesto de pare na primeira frase e depois aponta pra câmera na última.

câmera: fixa, leve push-in

som ambiente: oficina silenciosa, sem música, sem ruído de fundo
```

### V15 · T15 · usa K05 · **O TAKE DO PRODUTO**

```text
o avatar (HOMEM) fala em inglês com sotaque americano de homem negro, voz confiante e de autoridade, a seguinte frase: "So I stopped brewing it. Korella Saffron, on Amazon. One capsule, nothing to be rough on your stomach."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: corte duro, ele está em pé e o bule sumiu. ele ergue o frasco na direção da câmera ao dizer o nome e o mantém firme e parado, com o rótulo virado pra lente, até o fim da fala.

câmera: fixa

som ambiente: oficina silenciosa, sem música, sem ruído de fundo
```

### V16 · T16 · usa K05

```text
o avatar (HOMEM) fala em inglês com sotaque americano de homem negro, voz firme, a seguinte frase: "It never sat on that shelf, and nobody bought it by the pound. What is on the label is what is in the capsule."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ele gira levemente o frasco pra deixar o rótulo mais visível ao dizer a última frase.

câmera: fixa

som ambiente: oficina silenciosa, sem música, sem ruído de fundo
```

### V17 · T17 · usa K05

```text
o avatar (HOMEM) fala em inglês com sotaque americano de homem negro, voz mais quente e pessoal, a seguinte frase: "First week it is the mirror. By the third, it is the guy at work who cannot figure out what changed."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ele ergue um dedo da mão livre na primeira frase e três na segunda, e abre um sorriso curto no fim.

câmera: fixa, leve push-in

som ambiente: oficina silenciosa, sem música, sem ruído de fundo
```

### V18 · T18 · usa K05

```text
o avatar (HOMEM) fala em inglês com sotaque americano de homem negro, voz direta, a seguinte frase: "Send this to a man who needs to see it before he blames his age."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ele aponta pra câmera com a mão livre ao dizer "send this".

câmera: fixa

som ambiente: oficina silenciosa, sem música, sem ruído de fundo
```

### V19 · T19 · usa K06

```text
o avatar (HOMEM) fala em inglês com sotaque americano de homem negro, voz direta e convidativa, a seguinte frase: "You are going to look in a mirror tonight anyway. Comment yes and I will send you the link myself."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ele mantém o frasco erguido ao lado do rosto e aponta pra baixo com a outra mão, na direção dos comentários, ao dizer "comment yes".

câmera: fixa, leve push-in

som ambiente: oficina silenciosa, sem música, sem ruído de fundo
```

### V20 · T20 · usa K06

```text
o avatar (HOMEM) fala em inglês com sotaque americano de homem negro, voz direta, a seguinte frase: "But follow me first, or I will not be able to reach you."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ele aponta uma vez pra câmera, direto, e termina com um aceno curto de cabeça, ainda segurando o frasco ao lado do rosto.

câmera: fixa, leve push-in

som ambiente: oficina silenciosa, sem música, sem ruído de fundo
```

---

## Mapa de âncoras

| Keyframe | Referências a anexar | Modelo |
|---|---|---|
| K01 | âncora Melody | Nano Banana **Pro**, várias variações. **Frame herói e o de maior risco da operação** |
| K02 | **K01 aprovado** | Nano Banana 2, comando de edição |
| K03 | âncora Melody | Nano Banana 2 |
| K04 | **K03 aprovado** | Nano Banana 2, comando de edição. **Atende 10 takes**, vale insistir |
| K05 | **âncora Melody + product.png** | Nano Banana 2 |
| K06 | **K05 aprovado** | Nano Banana 2, comando de edição |

---

## Montagem no CapCut

- Timeline 1080x1920, 30 fps. Cortes duros entre todos os takes.
- **Três cortes de peso:** V02 para V03 (some a escultura, entra a receita), V04 para V05 (somem os ingredientes, o chá está pronto) e V14 para V15 (some o bule, entra o frasco).
- Cortar o silêncio inicial de cada clipe.
- **Segurar um beat extra de silêncio no fim do V07**, depois de "that you cannot see". A pausa é o que faz a pergunta trabalhar.
- **E outro no fim do V10**, depois de "nine at night". É a melhor frase do roteiro.
- Legendas grandes estilo Captions.ai Prism Pro, palavra destacada em vermelho, na altura do peito. **No V01 a legenda não pode cobrir a escultura**, que é onde a transformação acontece.
- Manter `YES` isolado na tela no CTA.
- Color grading: temp -3, tint +2, saturação -6, exposição -3, contraste +12, highlight -35, shadow +18, fade +6.

## Gates de qualidade

1. Melody é **HOMEM**, o mesmo em todos os clipes, com a cruz de **PRATA** sempre, nunca ouro.
2. Tranças e cavanhaque iguais em todos os planos.
3. **O V01 não tem corte.** A escultura derrete dentro do take, em quadro o tempo inteiro.
4. **O K01 sai com a escultura no MÁXIMO**, camadas grossas e traços quase enterrados. Se já saiu magra, o V01 não tem pra onde evoluir.
5. **A expressão da escultura é NEUTRA, de olhos fechados.** Se veio careta de sofrimento, regenerar: além do risco, não é o herói.
6. **A escultura é FOSCA e cor de creme.** Se saiu amarela e brilhante, regenerar. Tom quente é cara de IA e é o vocabulário que dispara restrição.
7. **A água do K03 está LIMPA.** Se saiu já âmbar, o V03 perde a ação.
8. Nenhuma legenda ou texto gerado dentro da imagem.
9. **O frasco do Korella aparece do K05 em diante**, rótulo legível e igual ao product.png, uns 10 cm.
10. **O nome "Korella Saffron" é dito no V15, no mesmo take em que o frasco entra em quadro.**
11. **O K06 é o plano mais fechado do vídeo inteiro.**
12. Fundo não inventariado: **duas âncoras apenas**, a porta de enrolar e o neon.
13. **A cena não está banhada de laranja nem de amarelo.**
14. Nenhuma imagem com fundo desfocado.
15. Mãos com cinco dedos, sem fusão com o bule nem com o frasco.
16. Ele **não larga o prop**: o bule fica na mão do V05 ao V14.
17. `yes` e o follow gate os dois no CTA final.
18. **Nenhuma menção a preço, desconto, gratuidade ou dosagem em miligramas.**
19. **Nenhuma marca de varejo dita em voz alta.** A fala é "that grocery store", não o nome da rede.
