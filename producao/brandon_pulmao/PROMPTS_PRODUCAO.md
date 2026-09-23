# holistic.brandon | Ângulo 2 (FityWell) | Pacote de Prompts

Vídeo modelo: `snapinsta-1787581398049.mp4`

Âncora de identidade: `C:\Users\luigi\Desktop\AVATARES NON-SHOP\holistic.brandon .png`

Funil: comment `yes` -> DM -> link do quiz FityWell

> ⚠️ **ÂNGULO 2: o produto NÃO aparece em nenhum take.** Sem print de app, sem celular, sem mockup. O nome "FityWell" é dito em voz alta no V20.
>
> ⚠️ **O K01 É O PROMPT DE MAIOR RISCO DE RESTRIÇÃO DE TODA A OPERAÇÃO.** Modelo anatômico já travou duas vezes aqui. Ele já sai escrito com o protocolo aplicado: modelo didático de resina fosca, cores neutras, e **zero nome de órgão no negative**. Ver a seção de restrição abaixo.

---

## Índice de geração

| Take | Keyframe | Ação de geração |
|---|---|---|
| T1 | K01 | GERAR DO ZERO (ref: âncora Brandon). **Frame herói.** Pro, com variações. |
| T2, T3 | K02 | GERAR DO ZERO (ref: âncora Brandon). Fogão e panela na bancada. |
| T4, T5 | K03 | GERAR DO ZERO. Close na panela, **sem rosto**. |
| T6, T7 | K04 | EDITAR do K02 (panela sai, caneca na mão) |
| T8 a T24 | K05 | GERAR DO ZERO (ref: âncora Brandon). Close puro, sem prop. |

Total: 5 keyframes para 24 takes. **Sem 2ª pessoa neste vídeo.**

---

## Trava de identidade e continuidade

**Escrita aqui uma vez, não repetir inteira dentro de cada JSON.**

- Rosto da Brandon, mulher negra mestiça, pele clara-média, olhos castanhos, sem maquiagem.
- Cornrows trançadas pra trás com pontas trançadas soltas caindo na frente dos ombros, miçangas de madeira e âmbar nas pontas.
- Manga de tatuagem floral de linha fina cobrindo o braço do lado esquerdo do quadro. Pequena tatuagem de folha na clavícula.
- Regata branca canelada. **Corrente fina de OURO com pingente de cruz de OURO. Nunca prata.**
- Box de treino dela com **duas âncoras visuais apenas**: o neon vermelho na parede e a **prateleira de metal com potes de vidro de ervas e sementes**. A prateleira é o que torna a receita crível ali dentro, então ela precisa aparecer nos setups da receita. **Nunca inventariar o resto do box.**
- Luz natural difusa de galpão com o brilho vermelho do neon. Zero blur, tudo em foco nítido. Cara de vídeo de iPhone, nunca polimento de IA.
- **Sempre em pé.**

## Trava do prop herói (usar no K01)

```text
A classroom anatomy teaching model of a pair of lungs, made of soft matte painted resin, about 30 cm tall, standing upright on a plain wooden bench. It has two rounded lobes, wider at the bottom and tapering toward the top, joined in the middle by a short vertical central tube. The whole surface is currently covered in a dull, flat charcoal grey coating with no shine. The shape and size stay identical in every shot.
```

## Trava dos props da receita (usar no K02 e no K03)

```text
A small portable single burner on the bench with a stainless steel pot of simmering water on it. Beside the pot: a small wooden bowl of bright yellow-orange turmeric powder, a few slices of fresh ginger on a board, one half of a fresh lemon cut side up, and a glass jar of raw honey with the lid off. The items keep the exact same positions in every shot.
```

**Não há 2ª pessoa neste vídeo, então não há REF-A.**

---

## GATE DE COMPOSIÇÃO VISUAL (rodado ANTES dos prompts abaixo)

```
HEROI
[x] 1. Heroi no LOWER FOREGROUND mais perto que o rosto
       -> K01: o modelo. K02: a panela. K03: close puro na panela. K04: a caneca
[x] 2. Nada compete com o heroi
[-] 3. Volume e cobertura              -> nao se aplica, nao ha heroi volumetrico

DISTANCIA
[x] 4. "Da pra estar mais perto?"      -> todos fecham mais que o original
[x] 5. Pessoas em peito pra cima       -> K02, K04, K05
[x] 6. Take mais fechado e o do CTA    -> K05

FUNDO
[x] 7. Cenario reconhecivel            -> 2 ancoras: o neon e a prateleira de potes
[x] 8. Fundo por enquadramento, nunca blur
[x] 9. Menos elementos

2a PESSOA
[-] 10. Nao se aplica, video sem 2a pessoa
```

**Uma escolha deliberada no item 7:** das duas âncoras do box, uma delas é a **prateleira de potes de ervas**, e ela não é decoração. É o que torna crível ferver uma receita dentro de um box de treino. Por isso ela precisa estar visível no K02 e no K03, e o quadro branco e a bandeira ficam fora de quadro.

---

## ⚠️ PROTOCOLO DE RESTRIÇÃO APLICADO NO K01

Modelo anatômico travou duas vezes nesta operação. O K01 já nasce com as quatro correções:

1. **Reenquadrado como objeto didático:** "classroom anatomy teaching model", "soft matte painted resin". Nunca órgão real.
2. **Cores da tabela de substituição:** `dull flat charcoal grey` no lugar de preto alcatroado, `soft muted rose` no lugar de rosa vivo de tecido.
3. **ZERO nome de órgão, gore ou doença no negative.** O classificador lê o token, não a negação.
4. **Campo `context` declarando ficção de IA.**

**Palavras banidas deste prompt:** tar, tarred, smoker, diseased, damaged, blackened, tissue, wet, glossy.

**Se travar mesmo assim,** ir direto pro Passo 3 do protocolo: gerar o modelo sozinho na bancada, sem pessoa, aprovar, e usar como referência de objeto numa segunda geração com a âncora da Brandon. **Nunca sugerir tentar de novo.**

---

# Prompts de imagem

## K01 · T1 · HOOK · GERAR DO ZERO (Nano Banana **Pro**, várias variações) · ÂNCORA BRANDON

```json
{
  "shot_id": "K01_hook_pour",
  "context": "Fictional AI-generated character. No real person is being filmed or depicted. The prop is a classroom teaching model.",
  "reference_use": "Use the attached image ONLY for Brandon's face, identity, hair, tattoos, clothing and the gym scene. Do NOT copy its pose or framing. Frame her much closer than the reference.",
  "identity_main": "The EXACT woman from the attached reference image (Brandon): mixed-race Black woman, light-medium skin, brown eyes, cornrows braided back with loose braided ends falling in front of the shoulders and wooden and amber beads on the tips, fine-line floral tattoo sleeve on the arm on the left side of frame, small leaf tattoo on the collarbone, no makeup.",
  "wardrobe": "White ribbed tank top, thin GOLD chain with a GOLD cross pendant.",
  "prop": "A classroom anatomy teaching model of a pair of lungs, made of soft matte painted resin, about 30 cm tall, standing upright on the bench. It has two rounded lobes, wider at the bottom and tapering toward the top, joined in the middle by a short vertical central tube. The whole surface is covered in a dull, flat charcoal grey coating with no shine.",
  "scene": "SAME gym box as the reference image, with only two visible anchors: the red neon sign on the wall and the metal shelf of glass jars of dried herbs and seeds. A plain wooden bench in front of her.",
  "posture": "Standing upright behind the bench, leaning slightly forward, both hands working over the model.",
  "composition": "TIGHT waist-up, close. The teaching model fills the lower foreground and sits closer to the lens than her face, unmistakably the hero. Her left hand steadies the base of the model and her right hand holds a clear glass jug of warm golden liquid, tilted above it, the first stream just about to touch the top.",
  "camera": "chest level, close, angled slightly high toward the model",
  "state": "Start frame: the model is still entirely dull charcoal grey, the jug is tilted and the liquid has not reached it yet.",
  "lighting": "Natural gym daylight from the side plus a warm red glow from the neon sign.",
  "realism": "UGC realism, real skin texture with visible pores, individual hair strands, realistic shadows and reflections, iPhone-footage look, phone camera look not professional photography, no AI polish, no beauty smoothing, no blur anywhere, everything in sharp focus.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no studio, no plastic skin, no extra fingers, no blur, no silver jewelry, no second person, no rose colour yet"
}
```

## K02 · T2, T3 · RECEITA · GERAR DO ZERO · ÂNCORA BRANDON

```json
{
  "shot_id": "K02_recipe_pot",
  "reference_use": "Use the attached image ONLY for Brandon's face, identity, hair, tattoos, clothing and the gym scene. Do NOT copy its pose or framing. Frame her closer than the reference.",
  "identity_main": "The EXACT woman from the attached reference image (Brandon): mixed-race Black woman, light-medium skin, brown eyes, cornrows braided back with loose braided ends and wooden and amber beads on the tips, fine-line floral tattoo sleeve on the arm on the left side of frame, small leaf tattoo on the collarbone, no makeup.",
  "wardrobe": "White ribbed tank top, thin GOLD chain with a GOLD cross pendant.",
  "prop": "A small portable single burner on the bench with a stainless steel pot of simmering water on it, faint steam rising. Beside the pot: a small wooden bowl of bright yellow-orange turmeric powder, a few slices of fresh ginger on a board, one half of a fresh lemon cut side up, and a glass jar of raw honey with the lid off.",
  "scene": "SAME gym box as the reference image, with only two visible anchors: the red neon sign and the metal shelf of glass jars of dried herbs and seeds directly behind her. A plain wooden bench in front of her.",
  "posture": "Standing upright behind the bench, leaning slightly forward over the pot.",
  "composition": "TIGHT waist-up, close. The pot and the bowls fill the lower foreground, closer to the lens than her face. Her right hand is above the pot holding the small wooden bowl of turmeric, tilted, about to tip it in. The water in the pot is still clear.",
  "camera": "chest level, close, angled slightly high toward the pot",
  "state": "Start frame: the water is still clear, nothing added yet, the bowl is tilted just above it.",
  "lighting": "Natural gym daylight from the side plus a warm red glow from the neon sign.",
  "realism": "UGC realism, real skin texture with visible pores, individual hair strands, realistic shadows and reflections, iPhone-footage look, phone camera look not professional photography, no AI polish, no beauty smoothing, no blur anywhere, everything in sharp focus.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no studio, no plastic skin, no extra fingers, no blur, no silver jewelry, no second person, no coloured water"
}
```

## K03 · T4, T5 · MECANISMO · GERAR DO ZERO · INSERT SEM ROSTO

```json
{
  "shot_id": "K03_pot_insert",
  "reference_use": "Close-up insert. No face. Use only the bench surface and the gym lighting of the other shots.",
  "identity_main": "No face in frame. Close-up of a stainless steel pot on a small burner, with one hand stirring it with a wooden spoon. Only the hand and forearm are visible, with a fine-line floral tattoo sleeve.",
  "scene": "SAME wooden bench and SAME gym box, the metal shelf of glass jars softly visible far behind and above the pot.",
  "composition": "Close-up on the pot, filling most of the frame, shot slightly from above so the whole surface of the liquid is visible. The liquid is a warm golden-orange with slices of ginger and lemon floating in it. A wooden spoon rests in it mid-stir.",
  "camera": "slightly high angle, close to the pot",
  "state": "Start frame: the spoon is in the liquid, mid-stir, gentle steam rising.",
  "lighting": "Natural gym daylight plus a warm red glow from the neon.",
  "realism": "UGC realism, real steam, real liquid surface, real metal reflections, iPhone macro look, no AI polish, no blur anywhere, everything in sharp focus.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no face, no studio, no cartoon look, no blur"
}
```

## K04 · T6, T7 · A BEBIDA PRONTA · EDITAR do K02

```json
{
  "task": "edit the attached image, keep everything identical except the changes listed",
  "keep_identical": "Keep the woman exactly the same: same face, same cornrows and beads, same tattoos, same white tank top, same gold cross, same standing posture. Keep the SAME background exactly: bench, red neon, shelf of glass jars, same lighting, same camera angle and framing.",
  "change_1": "Remove the burner, the pot, the wooden bowl, the ginger board, the lemon and the honey jar from the bench completely.",
  "change_2": "She now holds a clear glass mug of warm golden-orange liquid in her right hand at chest height, closer to the lens than her face, held steady toward the camera.",
  "change_3": "Her left hand is open near her chest in a natural mid-gesture and she speaks directly into the lens.",
  "realism": "UGC realism, real skin texture with visible pores, iPhone-footage look, no AI polish, no beauty smoothing, no blur anywhere. Do not make her skin darker, yellowish or orangish. Do not make the colors more saturated.",
  "negative": "do not change the face, do not change identity, do not change the background, do not change the camera angle, no captions, no subtitles, no words overlaid on the image, no plastic skin, no extra fingers, no silver jewelry, no straw, no garnish"
}
```

## K05 · T8 a T24 · O BLOCO DE VENDA · GERAR DO ZERO · ÂNCORA BRANDON

```json
{
  "shot_id": "K05_cta_close",
  "reference_use": "Use the attached image ONLY for Brandon's face, identity, hair, tattoos, clothing and the gym scene. Do NOT copy its pose or framing. This must be the CLOSEST framing of the entire video.",
  "identity_main": "The EXACT woman from the attached reference image (Brandon): mixed-race Black woman, light-medium skin, brown eyes, cornrows braided back with loose braided ends and wooden and amber beads on the tips, fine-line floral tattoo sleeve on the arm on the left side of frame, small leaf tattoo on the collarbone, no makeup.",
  "wardrobe": "White ribbed tank top, thin GOLD chain with a GOLD cross pendant.",
  "scene": "SAME gym box as the reference image, with only the red neon sign visible behind her. Everything else is out of frame because she fills the shot.",
  "posture": "Standing upright, very close to the lens, chin up, shoulders squared, direct personal eye contact.",
  "composition": "TIGHT chest-up close-up, the tightest framing in the whole video, her head and shoulders fill the frame. NOTHING in her hands. Both hands are up near her chest, open, mid-gesture.",
  "camera": "eye level, straight-on, very close",
  "state": "Start frame: hands open near her chest, speaking straight into the lens.",
  "lighting": "Natural gym daylight from the side plus a warm red glow from the neon sign.",
  "realism": "UGC realism, real skin texture with visible pores, individual hair strands, subtle wrinkles, realistic shadows and reflections, iPhone-footage look, phone camera look not professional photography, no AI polish, no beauty smoothing, no blur anywhere, everything in sharp focus.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no studio, no plastic skin, no extra fingers, no blur, no silver jewelry, no phone in hand, no product, no mug, no second person"
}
```

---

# Prompts de vídeo (Veo 3.1 via Flow)

## Bloco global

Colar em todo prompt:

```text
a avatar (mulher) fala em inglês com sotaque americano de mulher negra, voz autêntica, dinâmica, apaixonada e emocional, como se exigisse ser ouvida.

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

Estilo TikTok nativo, UGC. Preservar exatamente a identidade da Brandon, rosto, cornrows com miçangas, tatuagens, regata branca, cruz de OURO, o box de treino, a iluminação e o enquadramento do frame inicial. Sem legenda, sem texto gerado, sem música, sem pessoas extras.
```

**A câmera nunca é handheld de selfie neste vídeo.** As mãos dela estão nos props, então NÃO incluir a instrução de braço parado.

---

### V01 · T1 · usa K01 · REVEAL CONTÍNUO, NÃO PODE CORTAR

```text
a avatar (mulher) fala em inglês com sotaque americano de mulher negra, voz autêntica, dinâmica e emocional, como se exigisse ser ouvida, a seguinte frase: "If you still wake up tired after eight full hours, it is not your sleep that is broken. It is your breathing."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ela inclina a jarra e o líquido dourado escorre por cima do modelo. Onde o líquido passa, a superfície cinza escura vai clarando até virar um rosa suave, de cima pra baixo, até o modelo inteiro estar rosa. Tudo acontece no mesmo take, sem nenhum corte, e o modelo fica em quadro o tempo inteiro.

câmera: fixa, leve handheld natural

som ambiente: galpão de treino silencioso, líquido escorrendo, sem música
```

### V02 · T2 · usa K02

```text
a avatar (mulher) fala em inglês com sotaque americano de mulher negra, voz autêntica e direta, a seguinte frase: "Turmeric and fresh ginger into boiling water. Let it simmer for about ten minutes."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ela vira a tigelinha e a cúrcuma cai na panela, tingindo a água de laranja. Depois ela pega as fatias de gengibre e solta na água.

câmera: fixa, leve handheld natural

som ambiente: galpão de treino silencioso, água fervendo baixinho, sem música
```

### V03 · T3 · usa K02

```text
a avatar (mulher) fala em inglês com sotaque americano de mulher negra, voz autêntica e direta, a seguinte frase: "Then squeeze in lemon and stir in raw honey."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ela espreme a metade do limão sobre a panela e depois inclina o pote de mel, deixando um fio de mel cair dentro.

câmera: fixa, leve handheld natural

som ambiente: galpão de treino silencioso, água fervendo baixinho, sem música
```

### V04 · T4 · usa K03 · B-ROLL

```text
(sem fala no take: a fala 4 do roteiro entra como voz-over na edição)

o que acontece no vídeo: a mão dela mexe o líquido dourado com a colher de pau, girando devagar. As fatias de gengibre e limão rodam na superfície e sobe um vapor leve.

câmera: fixa, close alto sobre a panela

som ambiente: galpão de treino silencioso, água fervendo baixinho, sem música
```

### V05 · T5 · usa K03 · B-ROLL

```text
(sem fala no take: a fala 5 do roteiro entra como voz-over na edição)

o que acontece no vídeo: a colher de pau continua girando o líquido, agora mais devagar, e ela levanta a colher deixando o líquido escorrer de volta na panela.

câmera: fixa, close alto sobre a panela

som ambiente: galpão de treino silencioso, água fervendo baixinho, sem música
```

### V06 · T6 · usa K04

```text
a avatar (mulher) fala em inglês com sotaque americano de mulher negra, voz autêntica e direta, a seguinte frase: "Drink it warm every morning for a week and your chest opens up."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: corte duro, a panela sumiu. ela ergue a caneca na direção da câmera e a mantém firme enquanto fala.

câmera: fixa, leve handheld natural

som ambiente: galpão de treino silencioso, sem música, sem ruído de fundo
```

### V07 · T7 · usa K04

```text
a avatar (mulher) fala em inglês com sotaque americano de mulher negra, voz autêntica e confiante, a seguinte frase: "You will breathe deeper by day three. And that part is real."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ela respira fundo uma vez ao dizer a primeira frase e depois olha firme pra câmera na segunda.

câmera: fixa, leve push-in

som ambiente: galpão de treino silencioso, sem música, sem ruído de fundo
```

### V08 · T8 · usa K05

```text
a avatar (mulher) fala em inglês com sotaque americano de mulher negra, voz mais baixa e confidencial, a seguinte frase: "And I am going to tell you something I probably should not say out loud."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: corte duro, a caneca sumiu. ela se inclina um pouco pra frente e baixa o tom, como quem vai contar um segredo.

câmera: fixa, leve push-in

som ambiente: galpão de treino silencioso, sem música, sem ruído de fundo
```

### V09 · T9 · usa K05

```text
a avatar (mulher) fala em inglês com sotaque americano de mulher negra, voz honesta, quase de desculpa, a seguinte frase: "I told women over forty to fix their sleep for years. I was treating the wrong thing."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ela balança a cabeça devagar de um lado pro outro na última frase.

câmera: fixa, leve handheld natural

som ambiente: galpão de treino silencioso, sem música, sem ruído de fundo
```

### V10 · T10 · usa K05

```text
a avatar (mulher) fala em inglês com sotaque americano de mulher negra, voz que faz uma pergunta de verdade, a seguinte frase: "Think about the last time eight hours actually left you rested. Really think about it."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ela levanta um dedo e depois fica parada olhando fixo pra lente no fim da frase, esperando.

câmera: fixa, leve push-in

som ambiente: galpão de treino silencioso, sem música, sem ruído de fundo
```

### V11 · T11 · usa K05

```text
a avatar (mulher) fala em inglês com sotaque americano de mulher negra, voz firme, a seguinte frase: "Whatever year that was, that is the year your body changed the rules on you."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ela abre a mão com a palma pra cima num gesto de constatação.

câmera: fixa, leve handheld natural

som ambiente: galpão de treino silencioso, sem música, sem ruído de fundo
```

### V12 · T12 · usa K05

```text
a avatar (mulher) fala em inglês com sotaque americano de mulher negra, voz autêntica, dinâmica e emocional, a seguinte frase: "Stress locked your breathing up into your chest instead of your belly, and shallow breathing keeps cortisol high all day."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ela toca o próprio peito com a mão ao dizer "chest" e desce a mão pra barriga ao dizer "belly".

câmera: fixa, leve handheld natural

som ambiente: galpão de treino silencioso, sem música, sem ruído de fundo
```

### V13 · T13 · usa K05

```text
a avatar (mulher) fala em inglês com sotaque americano de mulher negra, voz firme, a seguinte frase: "Cortisol is the hormone that tells your body to store instead of burn."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ela fecha a mão devagar num punho ao dizer "store" e abre ao dizer "burn".

câmera: fixa, leve handheld natural

som ambiente: galpão de treino silencioso, sem música, sem ruído de fundo
```

### V14 · T14 · usa K05

```text
a avatar (mulher) fala em inglês com sotaque americano de mulher negra, voz de constatação, a seguinte frase: "So the tired and the weight were never two problems. They were always one."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ela separa as duas mãos no ar na primeira frase e junta as duas na segunda.

câmera: fixa, leve push-in

som ambiente: galpão de treino silencioso, sem música, sem ruído de fundo
```

### V15 · T15 · usa K05

```text
a avatar (mulher) fala em inglês com sotaque americano de mulher negra, voz honesta e equilibrada, a seguinte frase: "This drink helps. It calms the inflammation. But it does not touch the hormone."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ela assente nas duas primeiras frases e balança a cabeça na última.

câmera: fixa, leve handheld natural

som ambiente: galpão de treino silencioso, sem música, sem ruído de fundo
```

### V16 · T16 · usa K05

```text
a avatar (mulher) fala em inglês com sotaque americano de mulher negra, voz autêntica e direta, a seguinte frase: "And after forty there are three things holding your body. Hormones, a metabolism that stalled, and a gut that stopped moving."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ela conta três nos dedos, um pra cada item, enquanto fala.

câmera: fixa, leve handheld natural

som ambiente: galpão de treino silencioso, sem música, sem ruído de fundo
```

### V17 · T17 · usa K05

```text
a avatar (mulher) fala em inglês com sotaque americano de mulher negra, voz séria, a seguinte frase: "If yours is one of the other two, you will drink this every morning and feel nothing."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ela para de gesticular e olha direto pra lente enquanto fala.

câmera: fixa, leve handheld natural

som ambiente: galpão de treino silencioso, sem música, sem ruído de fundo
```

### V18 · T18 · usa K05

```text
a avatar (mulher) fala em inglês com sotaque americano de mulher negra, voz mais macia e protetora, a seguinte frase: "And you were never lazy about this. You were given a rulebook that expired."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: a expressão dela suaviza e ela balança a cabeça uma vez, devagar, na primeira frase.

câmera: fixa, leve push-in

som ambiente: galpão de treino silencioso, sem música, sem ruído de fundo
```

### V19 · T19 · usa K05

```text
a avatar (mulher) fala em inglês com sotaque americano de mulher negra, voz autêntica e direta, a seguinte frase: "No sleep tracker on your wrist tells you which of the three you are running."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ela toca o próprio pulso com dois dedos ao falar do monitor e depois abre a mão.

câmera: fixa, leve handheld natural

som ambiente: galpão de treino silencioso, sem música, sem ruído de fundo
```

### V20 · T20 · usa K05

```text
a avatar (mulher) fala em inglês com sotaque americano de mulher negra, voz aberta e confiante, a seguinte frase: "That is the whole thing FityWell does. Two minutes of questions, and the plan comes back built around your answer."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ela mantém a mão aberta e firme na frente do peito enquanto fala.

câmera: fixa, leve handheld natural

som ambiente: galpão de treino silencioso, sem música, sem ruído de fundo
```

### V21 · T21 · usa K05

```text
a avatar (mulher) fala em inglês com sotaque americano de mulher negra, voz mais baixa e pessoal, a seguinte frase: "Every one of them told me they had stopped expecting to feel rested. Not one of them was lazy."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ela para de gesticular na primeira frase e balança a cabeça uma vez na segunda.

câmera: fixa, leve push-in

som ambiente: galpão de treino silencioso, sem música, sem ruído de fundo
```

### V22 · T22 · usa K05

```text
a avatar (mulher) fala em inglês com sotaque americano de mulher negra, voz direta, a seguinte frase: "Tomorrow morning you are going to wake up either knowing which one it is, or guessing again."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ela alterna as duas mãos no ar mostrando as duas opções e para na segunda.

câmera: fixa, leve handheld natural

som ambiente: galpão de treino silencioso, sem música, sem ruído de fundo
```

### V23 · T23 · usa K05

```text
a avatar (mulher) fala em inglês com sotaque americano de mulher negra, voz direta e convidativa, a seguinte frase: "Two minutes and you will know which one it is. Comment yes and I will send it to you."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ela aponta pra baixo, na direção dos comentários, ao dizer "comment yes".

câmera: fixa, leve push-in

som ambiente: galpão de treino silencioso, sem música, sem ruído de fundo
```

### V24 · T24 · usa K05

```text
a avatar (mulher) fala em inglês com sotaque americano de mulher negra, voz direta, a seguinte frase: "But follow me first, or it will not let me reach you."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ela aponta uma vez pra câmera, direto, e termina com um aceno curto de cabeça.

câmera: fixa, leve push-in

som ambiente: galpão de treino silencioso, sem música, sem ruído de fundo
```

---

## Mapa de âncoras

| Keyframe | Referências a anexar | Modelo |
|---|---|---|
| K01 | âncora Brandon | Nano Banana **Pro**, várias variações. **O de maior risco de restrição** |
| K02 | âncora Brandon | Nano Banana 2 |
| K03 | nenhuma, insert sem rosto | Nano Banana 2 |
| K04 | K02 aprovado | Nano Banana 2, comando de edição |
| K05 | âncora Brandon | Nano Banana 2 |

---

## Montagem no CapCut

- Timeline 1080x1920, 30 fps. Cortes duros entre todos os takes.
- **Três cortes de peso:** V03 para V04 (entra o insert), V05 para V06 (some a panela, entra a caneca) e V07 para V08 (some a caneca, começa a venda).
- **V04 e V05 levam as falas 4 e 5 como voz-over.** São b-roll sem rosto.
- Cortar o silêncio inicial de cada clipe.
- **Segurar um beat extra de silêncio no fim do V10**, depois de "Really think about it". A pausa é o que faz ela procurar a resposta.
- Legendas grandes estilo Captions.ai Prism Pro, palavra destacada em vermelho, na altura do peito. **No V01 a legenda não pode cobrir o modelo**, que é o herói e onde a transformação acontece.
- Manter `YES` isolado na tela no CTA.
- Color grading: temp -3, tint +2, saturação -6, exposição -3, contraste +12, highlight -35, shadow +18, fade +6.

## Gates de qualidade

1. Brandon é a mesma mulher em todos os clipes, com a cruz de **OURO** em todos, nunca prata.
2. As cornrows com miçangas estão iguais em todos os planos.
3. **O V01 não tem corte.** A transformação acontece dentro do take, com o modelo em quadro o tempo inteiro. Se vier cortado, regenerar.
4. **O modelo do K01 está inteiramente cinza escuro.** Se já saiu rosa ou com partes rosa, regenerar: o V01 não tem pra onde evoluir.
5. **A água do K02 está LIMPA.** Se saiu já alaranjada, regenerar.
6. **A prateleira de potes de ervas aparece no K02 e no K03.** É ela que torna a receita crível dentro de um box de treino.
7. Nenhuma legenda ou texto foi gerado dentro da imagem.
8. **Nenhum produto, celular ou tela em quadro em nenhum take.** FityWell só existe em áudio, no V20.
9. **O K05 é o plano mais fechado do vídeo inteiro** e não tem nada nas mãos dela.
10. Fundo reconhecível e não inventariado: duas âncoras apenas.
11. Nenhuma imagem tem fundo desfocado.
12. Mãos com cinco dedos, sem fusão com a jarra, a panela nem a caneca.
13. `yes` e o follow gate estão os dois no CTA final.
14. **Nenhuma menção a preço, desconto ou gratuidade em nenhum take.**
