# Casey Harrisson | Ângulo 3 (Auraly) | Pacote de Prompts

Vídeo modelo: `scarlletmorgantarot.mp4` · 87,352s · zero cortes de cena

Âncora de identidade: `producao/_ancoras/casey.harrisson_us .jpeg`
**Atenção ao espaço antes da extensão.** Copiar o caminho, nunca digitar de memória.

Funil: vídeo → comentário `222` → DM com o rosto → link · mais o **Stories como degrau 2**

> ⚠️ **`Casey` é nome ambíguo de gênero em inglês.** Todo `identity_main` começa com
> **`The EXACT woman / female`**, sem exceção. Ver a trava do roster em `avatares_fichas.md`.

---

## Índice de geração

**A coluna que mais importa é a do meio. Ela responde sozinha "o que eu anexo agora".**

| Keyframe | 📎 O QUE ANEXAR | Ação | Take |
|---|---|---|---|
| **REF-CARTA** | **nada** | 🆕 GERAR DO ZERO | ref |
| **K01** | **âncora Casey + REF-CARTA** | 🆕 GERAR DO ZERO | T1, gancho 1 |
| **K02** | **K01** | ✏️ EDITAR | T1, gancho 2 |
| **K03** | **K01** | ✏️ EDITAR | T1, gancho 5 |
| **K04** | **K01** | ✏️ EDITAR | T1, gancho 7 |
| **K05** | **K01** | ✏️ EDITAR | T1, gancho 3 |
| **K06** | **âncora Casey + REF-CARTA** | 🆕 GERAR DO ZERO | T2 a T7 |
| **K07** | **K06** | ✏️ EDITAR | T8 a T11 |
| **K08** | **K06**, nunca o K07 | ✏️ EDITAR | T12 |

**Ordem de geração, de cima pra baixo:** REF-CARTA primeiro e aprovada, depois K01, depois K02 a K05
saindo do K01, depois K06, depois K07 e K08 saindo do K06.

**Regra de bolso:** se o keyframe está marcado como 🆕 **GERAR DO ZERO**, você anexa **a âncora da Casey
mais a REF-CARTA**. Se está marcado como ✏️ **EDITAR**, você anexa **uma imagem só, o keyframe de origem**,
e não anexa mais nada.

Total: **1 referência + 8 keyframes para 12 takes em 5 variações de gancho.**

**Os K02 a K05 saem todos do K01 original, nunca em cascata.** O K08 sai do K06, nunca do K07.

---

## Trava de identidade e continuidade

Vale para toda imagem e todo clipe. Escrita aqui uma vez, não repetida dentro de cada JSON.

- **MULHER** americana de traços latinos, **21 anos**, magra. É a mais nova do roster.
- Pele **oliva clara** com **acne ativa nas bochechas e no queixo mais marcas reais de acne**, poros
  visíveis. **ZERO maquiagem.** A pele com acne é **ativo, não defeito**: é o que faz ela ler como
  garota de verdade e não como criadora de conteúdo. Nunca rejuvenescer, nunca alisar, nunca limpar.
- **Cabelo liso castanho escuro, longo, risca ao meio, com DUAS MECHAS LOIRAS DESCOLORIDAS enquadrando
  o rosto.** É o marcador dela, e entra escrito em todo keyframe.
- Rosto de coração, queixo estreito, lábios cheios, sobrancelhas grossas escuras, olhos castanho escuros.
- **Moletom CROPPED cinza mescla** de gola careca, calça preta.
- **Argolas pequenas de PRATA** e **corrente fina de PRATA com pingente pequeno de cruz de prata.**
  Nunca ouro.
- **Cenário: o mesmo quarto da imagem de referência, inalterado.** Não redescrever o quarto item a item.
  **As duas âncoras que importam** são: **a parede atrás dela** com a bandeira dos EUA esticada à
  esquerda, o mapa de constelação emoldurado (disco de estrelas branco sobre preto) ao centro, o
  crucifixo de madeira à direita e o pisca-pisca branco frio em festão; e **o baú de madeira escura**
  no terço inferior com o leque de cartas holográficas, o quartzo rosa bruto, a geoda de celestita azul,
  o prato de terracota com a vareta de incenso acesa e a vela branca acesa em pote de vidro.
- Ela está **sentada no chão aos pés da cama desarrumada**, e a cama fica em quadro. **A bagunça é ativo**,
  lê como "abriu a câmera e gravou". **Nunca listar a bagunça item a item.**
- **A bandeira dos EUA é visível e em foco em todo keyframe.**
- **Luz neutra e difusa, o rosto lavado por luz branca**, sem cast quente. **O pisca-pisca é branco frio
  e ilumina só a parede.** A vela é ponto de luz e **não** ilumina o ambiente. Cast quente na pele dela
  denuncia IA no primeiro segundo.
- **Zero blur, tudo em foco nítido**, incluindo a bandeira, o mapa, o crucifixo e as cartas.
  Cara de vídeo de iPhone, nunca fotografia profissional.

### A gramática dela, e por que é trava de produção
Ela é a **única do roster que senta no chão com um BAÚ**, a única com **pisca-pisca**, e a única
**abaixo dos vinte e quatro**. A Shelby também senta no chão, mas com **caixote ripado**, cabelo loiro
e tatuagem no pulso. **Reforçar mechas loiras, acne e baú em todo keyframe** é o que impede as duas
contas de parecerem a mesma.

---

## Trava do prop herói: a carta SOULMATE (REF-CARTA)

> ### 📎 ANEXAR: **NADA**
> Esta é a única geração do pacote que roda **sem nenhuma imagem anexada**.
>
> ### 🆕 GERAR DO ZERO, e aprovar ANTES do K01

**⚠️ A Casey tem REF-CARTA PRÓPRIA, holográfica. Não reaproveitar a dos pacotes antigos.**
A REF-CARTA que existe em `trevor_a3_confissao`, `karen_a3_confissao` e `mark_a3_confissao` é a arte
**fosca de dourado e marfim**, anterior à espec de 2026-08-29. **O baralho da mesa da Casey é
holográfico** (traço canônico dela, confirmado na âncora), então a carta herói dela tem que ser
holográfica também, senão a arte da mão não bate com a arte da mesa **no mesmo quadro**.

Prompt da REF-CARTA:

```text
Uma carta de tarô retangular de cantos arredondados, cartão liso de baralho moderno com acabamento foil, superfície impressa limpa. Borda metálica larga em prata espelhada com reflexo de arco-íris, arabesco gravado e um floreio em cada canto. Numeral romano em capitulares serifadas no topo. Faixa de título na base com a palavra SOULMATE em capitulares serifadas espaçadas. No centro, duas figuras humanas de túnicas atemporais lado a lado, em estilo simbólico chapado com hachura fina de nanquim, com um coração luminoso branco entre as cabeças dos dois e raios de luz atrás. Um arco de rosas enquadra o casal. Atrás deles um motivo celeste com sol estilizado, lua crescente e estrelas de cinco pontas. Paleta saturada: carmim e rosa das rosas, lavanda, dourado quente e luz branca, sobre a borda metálica com reflexo de arco-íris. O brilho metálico é propriedade impressa do objeto, tinta foil que reflete a luz, nunca luz própria.

negative: no cartoon style, no children's book illustration, no cute rounded faces, no modern clothing, no plain white border, no comic art, no 3d render, no gothic art, no skulls, no ravens, no snakes, no swords, no inverted symbols, no sigils, no captions, no subtitles, no watermark
```

⚠️ **Três travas que já custaram carta reprovada:**
1. **O negative da REF-CARTA NÃO pode carregar `no words overlaid on the image`**, senão mata a palavra
   `SOULMATE` da faixa da base. Usar `no captions, no subtitles, no watermark`.
2. **Não entram aqui `no golden glow`, `no warm orange color cast`, `no sparkles` nem `no glowing edges`.**
   As quatro matam o foil e o coração luminoso. O brilho está descrito como **tinta impressa que reflete
   a luz**, que é o que evita a colisão com o gate de realismo. **Nos keyframes da Casey o negative volta
   completo**, porque lá a arte já vem travada pela REF anexada.
3. **REF-CARTA é a única exceção da regra da bandeira dos EUA.** Objeto isolado sem cenário, e pôr
   bandeira ali contaminaria todo keyframe que anexasse a referência.

⚠️ **A carta é o alvo da ação em três dos cinco ganchos, e fica na mão dela do T2 até o fim.**

---

## Trava da 2ª pessoa (REF-A)

**Não se aplica neste vídeo.** O modelo é uma pessoa só do primeiro ao último frame, e o clone também.
`no second person` entra no negative de todos os keyframes.

---

# Prompts de imagem

## K01 · T1 · GANCHO 1, A FUMAÇA QUE ENTREGA A CARTA · GERAR DO ZERO · ÂNCORA CASEY + REF-CARTA

> ### 📎 ANEXAR: **2 IMAGENS**
> **1️⃣ ÂNCORA CASEY** `producao/_ancoras/casey.harrisson_us .jpeg`
> **2️⃣ REF-CARTA** já aprovada
>
> ### 🆕 GERAR DO ZERO

```json
{
  "shot_id": "K01_hook_smoke_delivers_card",
  "reference_use": "Use the first attached image ONLY for Casey's face, identity, hair, wardrobe and the bedroom scene. Use the second attached image ONLY for the exact art of the tarot card. Do NOT copy the pose or framing of either reference.",
  "identity_main": "The EXACT woman from the first reference image (Casey): female, 21-year-old Latina American woman, slim, light olive skin with active acne on the cheeks and chin and real acne marks, visible pores, absolutely no makeup, long straight dark brown hair parted in the centre with TWO bleached blonde strands framing her face, heart-shaped face, narrow chin, full lips, thick dark eyebrows, dark brown eyes.",
  "wardrobe": "Plain heather-grey cropped crew-neck sweatshirt, black trousers, small silver hoop earrings, thin silver chain with a small silver cross pendant. No gold.",
  "prop": "The EXACT tarot card from the second reference image, lying face up on the trunk in the lower foreground, the word SOULMATE readable on the base band, its mirrored rainbow foil border catching the light as printed ink. A shallow terracotta dish holding a lit incense stick with a glowing ember and a thin thread of smoke rising, held in both of her hands and raised toward the lens.",
  "scene": "SAME lived-in bedroom as the reference image, unchanged. On the cream wall behind her: a United States flag pinned flat on the left, clearly visible and in sharp focus, a framed constellation map with a white star disc on black in the centre, a wooden crucifix on the right, and a string of cool white fairy lights swagged along the top of the wall. Her unmade bed is behind her. On the dark wooden trunk in front of her: an open fan of holographic tarot cards, a rough chunk of rose quartz, a blue celestite geode and a white candle burning in a glass jar.",
  "posture": "She is sitting on the floor at the foot of her bed, upright, leaning slightly toward the lens, both hands lifting the terracotta dish.",
  "composition": "Chest up. The SOULMATE card lies in the lower foreground on the trunk, closer to the lens than her face, and it is unmistakably the hero. The terracotta dish is raised between the card and her mouth. Nothing else competes. The bedroom behind is readable but not inventoried.",
  "camera": "chest level, straight-on from the other side of the trunk, pushed in close to the trunk",
  "state": "Start frame: she has just raised the dish toward the lens, lips parting, about to blow across the ember. The card is still lying on the trunk and the smoke is still a thin thread.",
  "lighting": "Flat neutral daylight, her face washed by soft neutral white light. The fairy lights are cool white and fall on the wall only. The candle is a point of light and does not light the room.",
  "realism": "UGC realism, real skin texture with visible pores and real acne, individual hair strands, realistic shadows and reflections, iPhone-footage look, phone camera look not professional photography, no AI polish, no beauty smoothing, no blur anywhere, everything in sharp focus including the wall, the flag, the framed map and the cards.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no studio, no plastic skin, no extra fingers, no supernatural lighting, no blur, no artificial lighting, no warm orange color cast, no yellow tint, no de-aging, no skin smoothing, no makeup, no beauty smoothing, no gold jewelry, no second person, no phone, no screens"
}
```

## K02 · T1 · GANCHO 2, O SOPRO NA BRASA · EDITAR do K01

> ### 📎 ANEXAR: **1 IMAGEM**
> **1️⃣ O K01 já aprovado**
>
> ### ✏️ EDITAR, muda só a altura do prato e a posição da carta

```json
{
  "task": "edit the attached image, keep everything identical except the changes listed",
  "keep_identical": "Keep the woman exactly the same: same face, same acne, same hair with the two blonde front strands, same cropped grey sweatshirt, same silver cross, same seated position on the floor. Keep the SAME bedroom exactly: flag, framed constellation map, crucifix, fairy lights, unmade bed, dark wooden trunk, fan of cards, rose quartz, celestite, candle, same lighting, same camera height.",
  "change_1": "Raise the terracotta incense dish higher and closer to the lens, so the dish and her hands now fill the lower foreground and are the closest thing to the camera. Her face stays visible above it.",
  "change_2": "The SOULMATE card is no longer separate on the trunk. It is back inside the fan of tarot cards on the trunk, so no single card stands out.",
  "realism": "UGC realism, real skin texture with visible pores and real acne, iPhone-footage look, no AI polish, no beauty smoothing, no blur anywhere. Do not make her skin darker, yellowish or orangish. Do not make the colors more saturated.",
  "negative": "do not change the face, do not change the identity, do not change the background, do not change the camera angle, no captions, no subtitles, no words overlaid on the image, no plastic skin, no extra fingers, no gold jewelry, no makeup, no second person, no phone"
}
```

## K03 · T1 · GANCHO 5, A CARTA COLADA NA LENTE · EDITAR do K01

> ### 📎 ANEXAR: **1 IMAGEM**
> **1️⃣ O K01 já aprovado**
>
> ### ✏️ EDITAR, muda só a carta, que sobe até quase encostar na lente

```json
{
  "task": "edit the attached image, keep everything identical except the changes listed",
  "keep_identical": "Keep the woman exactly the same: same face, same acne, same hair with the two blonde front strands, same cropped grey sweatshirt, same silver cross, same seated position. Keep the SAME bedroom, the SAME lighting and the SAME camera height. The United States flag pinned flat on the wall must stay fully visible and in sharp focus in the upper left corner of the frame, never cropped by the edge.",
  "change_1": "She now holds the SOULMATE tarot card up toward the lens with her right hand, so the card fills the large majority of the frame and is unmistakably the hero. The word SOULMATE and the couple illustration are fully readable and the mirrored rainbow foil border catches the light as printed ink. The card is in sharp focus.",
  "change_2": "The card is positioned slightly low and to the right, so the upper left corner of the frame still shows the United States flag whole on the wall behind her. A sliver of her shoulder and hair stays visible on one side. The terracotta incense dish stays on the trunk with its thin thread of smoke rising at the bottom edge of frame.",
  "realism": "UGC realism, real printed card surface, iPhone-footage look, no AI polish, no blur anywhere, the flag in sharp focus. Do not make the colors more saturated. The foil shine is printed ink reflecting light, never light of its own.",
  "negative": "do not change the face, do not change the identity, do not change the card art, do not change the background, do not crop the flag, no captions, no subtitles, no words overlaid on the image, no plastic skin, no extra fingers, no gold jewelry, no second person, no phone, no glowing edges"
}
```

> ⚠️ **Este é o único keyframe em que a regra da bandeira brigou com o gancho.** O gancho pede a carta
> ocupando o quadro inteiro, e a regra pede a bandeira inteira, visível e nunca cortada pela borda.
> **Resolvi pela regra:** a carta desce um pouco e vai para a direita, fica com a maioria larga do quadro
> e continua sendo o herói, e o canto superior esquerdo segura a bandeira inteira. Se você preferir a
> carta ocupando tudo mesmo, é decisão sua e eu reescrevo, mas aí o keyframe passa a violar uma regra
> que o linter reprova de propósito.

## K04 · T1 · GANCHO 7, O MAÇO EMBARALHADO NA LENTE · EDITAR do K01

> ### 📎 ANEXAR: **1 IMAGEM**
> **1️⃣ O K01 já aprovado**
>
> ### ✏️ EDITAR, muda só as mãos, que passam a segurar o maço

```json
{
  "task": "edit the attached image, keep everything identical except the changes listed",
  "keep_identical": "Keep the woman exactly the same: same face, same acne, same hair with the two blonde front strands, same cropped grey sweatshirt, same silver cross, same seated position. Keep the SAME bedroom exactly: flag, framed constellation map, crucifix, fairy lights, unmade bed, trunk, rose quartz, celestite, candle, same lighting, same camera height.",
  "change_1": "Both of her hands are now holding the closed deck of holographic tarot cards close to the lens, in the lower foreground, fingers bent in the position of a riffle shuffle about to start. The deck is the closest object to the camera.",
  "change_2": "The open fan of cards is gone from the trunk, because the whole deck is now in her hands. The terracotta incense dish stays on the trunk with its thin thread of smoke rising.",
  "realism": "UGC realism, real skin texture with visible pores and real acne, real printed card edges, iPhone-footage look, no AI polish, no beauty smoothing, no blur anywhere. Do not make her skin darker, yellowish or orangish.",
  "negative": "do not change the face, do not change the identity, do not change the background, do not change the camera angle, no captions, no subtitles, no words overlaid on the image, no plastic skin, no extra fingers, no fused fingers, no gold jewelry, no makeup, no second person, no phone"
}
```

## K05 · T1 · GANCHO 3, AS MÃOS EM CONCHA COM A FUMAÇA PRESA · EDITAR do K01

> ### 📎 ANEXAR: **1 IMAGEM**
> **1️⃣ O K01 já aprovado**
>
> ### ✏️ EDITAR, muda só as mãos, em concha sobre a vareta

```json
{
  "task": "edit the attached image, keep everything identical except the changes listed",
  "keep_identical": "Keep the woman exactly the same: same face, same acne, same hair with the two blonde front strands, same cropped grey sweatshirt, same silver cross, same seated position. Keep the SAME bedroom exactly: the United States flag pinned flat on the wall clearly visible and in sharp focus, the framed constellation map, the wooden crucifix, the cool white fairy lights, the unmade bed, the trunk, the fan of cards, the rose quartz, the celestite and the candle. Keep the SAME lighting and the SAME camera height.",
  "change_1": "The terracotta dish with the lit incense stick is back down on the trunk. Both of her hands are now cupped together directly above the incense stick, palms curved and fingers loosely closed, trapping the smoke inside. Thin threads of smoke escape between her fingers and rise in front of her chest.",
  "change_2": "The SOULMATE card lies face up on the trunk directly below her cupped hands, in the lower foreground, closer to the lens than her face, with the word SOULMATE readable.",
  "realism": "UGC realism, real skin texture with visible pores and real acne, real smoke with soft edges, iPhone-footage look, no AI polish, no beauty smoothing, no blur anywhere. Do not make her skin darker, yellowish or orangish.",
  "negative": "do not change the face, do not change the identity, do not change the background, do not change the camera angle, no captions, no subtitles, no words overlaid on the image, no plastic skin, no extra fingers, no fused fingers, no gold jewelry, no makeup, no second person, no phone"
}
```

## K06 · T2 a T7 · SETUP B, A CARTA NA COLUNA DE FUMAÇA · GERAR DO ZERO · ÂNCORA CASEY + REF-CARTA

> ### 📎 ANEXAR: **2 IMAGENS**
> **1️⃣ ÂNCORA CASEY** `producao/_ancoras/casey.harrisson_us .jpeg`
> **2️⃣ REF-CARTA** já aprovada
>
> ### 🆕 GERAR DO ZERO
>
> ⚠️ **NÃO anexar o K01 aqui.** Este é o segundo SETUP, e sai do zero com a âncora.

```json
{
  "shot_id": "K06_setupB_card_in_smoke",
  "reference_use": "Use the first attached image ONLY for Casey's face, identity, hair, wardrobe and the bedroom scene. Use the second attached image ONLY for the exact art of the tarot card. Do NOT copy the pose or framing of either reference.",
  "identity_main": "The EXACT woman from the first reference image (Casey): female, 21-year-old Latina American woman, slim, light olive skin with active acne on the cheeks and chin and real acne marks, visible pores, absolutely no makeup, long straight dark brown hair parted in the centre with TWO bleached blonde strands framing her face, heart-shaped face, narrow chin, full lips, thick dark eyebrows, dark brown eyes.",
  "wardrobe": "Plain heather-grey cropped crew-neck sweatshirt, black trousers, small silver hoop earrings, thin silver chain with a small silver cross pendant. No gold.",
  "prop": "The EXACT tarot card from the second reference image, held upright in her left hand at chest height, facing the lens, the word SOULMATE readable on the base band and the mirrored rainbow foil border catching the light as printed ink. The terracotta dish with the lit incense stick sits on the trunk directly below the card, and a continuous column of thin smoke rises from the stick and curls around the card.",
  "scene": "SAME lived-in bedroom as the reference image, unchanged. On the cream wall behind her: a United States flag pinned flat on the left, clearly visible and in sharp focus, a framed constellation map with a white star disc on black in the centre, a wooden crucifix on the right, and a string of cool white fairy lights swagged along the top of the wall. Her unmade bed is behind her. On the dark wooden trunk in front of her: an open fan of holographic tarot cards, a rough chunk of rose quartz, a blue celestite geode and a white candle burning in a glass jar.",
  "posture": "She is sitting on the floor at the foot of her bed, upright, shoulders square to the camera, left hand holding the card up in the smoke, right hand resting open on the trunk.",
  "composition": "Chest up. The SOULMATE card and the rising smoke sit in the lower foreground, closer to the lens than her face, and the card is the hero. Her face is fully visible above it. Nothing else competes.",
  "camera": "chest level, straight-on from the other side of the trunk",
  "state": "Start frame: the card is steady in the smoke and she is looking directly into the lens, about to speak.",
  "lighting": "Flat neutral daylight, her face washed by soft neutral white light. The fairy lights are cool white and fall on the wall only. The candle is a point of light and does not light the room.",
  "realism": "UGC realism, real skin texture with visible pores and real acne, individual hair strands, real smoke with soft edges, realistic shadows and reflections, iPhone-footage look, phone camera look not professional photography, no AI polish, no beauty smoothing, no blur anywhere, everything in sharp focus including the wall, the flag, the framed map and the cards.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no studio, no plastic skin, no extra fingers, no supernatural lighting, no blur, no artificial lighting, no warm orange color cast, no yellow tint, no de-aging, no skin smoothing, no makeup, no beauty smoothing, no gold jewelry, no second person, no phone, no screens"
}
```

## K07 · T8 a T11 · EDITAR do K06

> ### 📎 ANEXAR: **1 IMAGEM**
> **1️⃣ O K06 já aprovado**
>
> ### ✏️ EDITAR, muda só a mão direita e aproxima a câmera

```json
{
  "task": "edit the attached image, keep everything identical except the changes listed",
  "keep_identical": "Keep the woman exactly the same: same face, same acne, same hair with the two blonde front strands, same cropped grey sweatshirt, same silver cross, same seated position. Keep the SAME tarot card with the same art and the same word SOULMATE. Keep the SAME bedroom exactly: flag, framed constellation map, crucifix, fairy lights, unmade bed, trunk, fan of cards, rose quartz, celestite, candle, same lighting.",
  "change_1": "Push the camera in by about fifteen percent so the framing tightens on her face and the card, and the bedroom behind reads with fewer details. Do not change the camera height or the angle.",
  "change_2": "Her right hand is no longer resting on the trunk. It is now raised open beside the card, palm turned slightly toward the lens in a small explaining gesture.",
  "realism": "UGC realism, real skin texture with visible pores and real acne, iPhone-footage look, no AI polish, no beauty smoothing, no blur anywhere. Do not make her skin darker, yellowish or orangish. Do not make the colors more saturated.",
  "negative": "do not change the face, do not change the identity, do not change the card art, do not change the background, no captions, no subtitles, no words overlaid on the image, no plastic skin, no extra fingers, no gold jewelry, no makeup, no second person, no phone"
}
```

## K08 · T12 · CTA, O TAKE MAIS FECHADO · EDITAR do K06 (nunca do K07)

> ### 📎 ANEXAR: **1 IMAGEM**
> **1️⃣ O K06 já aprovado**
>
> ### ✏️ EDITAR, fecha o plano e muda a expressão
>
> 🚫 **NUNCA anexar o K07 aqui.** Estágio sempre a partir do original, nunca em cascata.

```json
{
  "task": "edit the attached image, keep everything identical except the changes listed",
  "keep_identical": "Keep the woman exactly the same: same face, same acne, same hair with the two blonde front strands, same cropped grey sweatshirt, same silver cross, same seated position. Keep the SAME tarot card with the same art and the same word SOULMATE. Keep the SAME bedroom: flag, framed constellation map, crucifix, fairy lights, unmade bed, trunk, same lighting.",
  "change_1": "Push the camera in by about thirty percent, the tightest framing of the whole video. Her face fills a large part of the frame, shoulders up, and the card is held higher so it stays in the lower foreground beside her chin. Do not change the camera height or the angle.",
  "change_2": "Her expression shifts to direct and urgent, chin slightly lifted, eyes locked on the lens. Her right hand is lowered out of frame.",
  "realism": "UGC realism, real skin texture with visible pores and real acne, iPhone-footage look, no AI polish, no beauty smoothing, no blur anywhere. Do not make her skin darker, yellowish or orangish. Do not make the colors more saturated.",
  "negative": "do not change the face, do not change the identity, do not change the card art, do not change the background, no captions, no subtitles, no words overlaid on the image, no plastic skin, no extra fingers, no gold jewelry, no makeup, no second person, no phone"
}
```

---

# Bloco global de vídeo

**Colar em todo prompt de vídeo falado.** A voz e o registro não mudam de take para take.

```text
a avatar (mulher) fala em inglês com sotaque americano de mulher jovem latina, voz autêntica, rápida, urgente e emocional, como se exigisse ser ouvida, a seguinte frase: "[FALA EXATA DO ROTEIRO]"

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: [ação enxuta]

câmera: fixa

som ambiente: quarto silencioso, sem música, sem ruído de fundo
```

⚠️ **A câmera NÃO é selfie handheld.** O celular está apoiado do outro lado do baú, então **não entra**
a instrução de braço parado. As duas mãos dela estão livres em quadro.

⚠️ **A fala de cada prompt é cópia literal do `ROTEIRO.md`**, palavra por palavra. Nada de filler,
nada de paráfrase.

---

# Prompts de vídeo

## Os cinco ganchos (T1, mudo)

### V01 · T1 · usa K01 · GANCHO 1, A FUMAÇA QUE ENTREGA A CARTA · B-ROLL

> ### 🖼️ IMAGEM INICIAL NO FLOW: **K01**

```text
(sem fala no take: o take é mudo como no modelo, nenhuma fala entra como voz-over)

o que acontece no vídeo: ela sopra na brasa do incenso e a fumaça se abre na direção da lente até cobrir o quadro. Quando a fumaça afina, ela já está com a carta erguida na mão esquerda, dentro da coluna de fumaça, virada para a lente.

câmera: fixa

som ambiente: quarto silencioso, o sopro dela, sem música
```

### V02 · T1 · usa K02 · GANCHO 2, O SOPRO NA BRASA · B-ROLL

> ### 🖼️ IMAGEM INICIAL NO FLOW: **K02**

```text
(sem fala no take: o take é mudo como no modelo, nenhuma fala entra como voz-over)

o que acontece no vídeo: ela levanta o prato de terracota até perto da boca e sopra na brasa na direção da lente. A fumaça branca se abre e cobre o quadro inteiro.

câmera: fixa

som ambiente: quarto silencioso, o sopro dela, sem música
```

### V03 · T1 · usa K03 · GANCHO 5, A CARTA COLADA NA LENTE · B-ROLL

> ### 🖼️ IMAGEM INICIAL NO FLOW: **K03**

```text
(sem fala no take: o take é mudo como no modelo, nenhuma fala entra como voz-over)

o que acontece no vídeo: a carta está encostada na lente ocupando o quadro inteiro. Ela puxa a carta para trás devagar e o rosto dela aparece atrás, olhando na lente, com a carta parada na altura do peito.

câmera: fixa

som ambiente: quarto silencioso, sem música
```

### V04 · T1 · usa K04 · GANCHO 7, O MAÇO EMBARALHADO NA LENTE · B-ROLL

> ### 🖼️ IMAGEM INICIAL NO FLOW: **K04**

```text
(sem fala no take: o take é mudo como no modelo, nenhuma fala entra como voz-over)

o que acontece no vídeo: ela embaralha o maço bem perto da lente, as cartas passam rápido entre as mãos e atravessam o quadro. Ela para de repente com a carta SOULMATE por cima do maço, virada para a lente.

câmera: fixa

som ambiente: quarto silencioso, o som das cartas, sem música
```

### V05 · T1 · usa K05 · GANCHO 3, AS MÃOS EM CONCHA · B-ROLL

> ### 🖼️ IMAGEM INICIAL NO FLOW: **K05**

```text
(sem fala no take: o take é mudo como no modelo, nenhuma fala entra como voz-over)

o que acontece no vídeo: ela mantém as mãos em concha fechadas sobre a vareta por um instante e depois abre as duas mãos na direção da lente. A fumaça presa escapa de uma vez e sobe cobrindo o quadro.

câmera: fixa

som ambiente: quarto silencioso, sem música
```

## Os takes falados

### V06 · T2 · usa K06

> ### 🖼️ IMAGEM INICIAL NO FLOW: **K06**

```text
a avatar (mulher) fala em inglês com sotaque americano de mulher jovem latina, voz autêntica, rápida, urgente e emocional, como se exigisse ser ouvida, a seguinte frase: "I don't know your name, and I don't need it. This video landed on you today, and it wasn't random."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ela olha fixo na lente e mantém a carta parada na fumaça, dando um pequeno balanço de cabeça na negativa ao falar do nome.

câmera: fixa

som ambiente: quarto silencioso, sem música, sem ruído de fundo
```

### V07 · T3 · usa K06

> ### 🖼️ IMAGEM INICIAL NO FLOW: **K06**

```text
a avatar (mulher) fala em inglês com sotaque americano de mulher jovem latina, voz autêntica, rápida, urgente e emocional, como se exigisse ser ouvida, a seguinte frase: "The eleven eleven portal opened this morning. Before you scroll past me, you need to know what that means for you."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ela levanta um pouco a carta ao falar do portal e depois abre a mão direita na frente do peito ao pedir que ela não role a tela.

câmera: fixa

som ambiente: quarto silencioso, sem música, sem ruído de fundo
```

### V08 · T4 · usa K06

> ### 🖼️ IMAGEM INICIAL NO FLOW: **K06**

```text
a avatar (mulher) fala em inglês com sotaque americano de mulher jovem latina, voz autêntica, rápida, urgente e emocional, como se exigisse ser ouvida, a seguinte frase: "Something is moving toward you right now that hasn't moved in years. Don't you dare skip this video."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ela aproxima o corpo da lente e endurece o olhar na última frase, mantendo a carta parada na fumaça.

câmera: fixa

som ambiente: quarto silencioso, sem música, sem ruído de fundo
```

### V09 · T5 · usa K06

> ### 🖼️ IMAGEM INICIAL NO FLOW: **K06**

```text
a avatar (mulher) fala em inglês com sotaque americano de mulher jovem latina, voz autêntica, rápida, urgente e emocional, como se exigisse ser ouvida, a seguinte frase: "Not everybody gets this video. And what's coming for you isn't money. It's a person."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ela faz um gesto curto de descarte com a mão direita ao dizer que não é dinheiro, e depois aponta a carta um pouco mais para a lente ao dizer que é uma pessoa.

câmera: fixa

som ambiente: quarto silencioso, sem música, sem ruído de fundo
```

### V10 · T6 · usa K06

> ### 🖼️ IMAGEM INICIAL NO FLOW: **K06**

```text
a avatar (mulher) fala em inglês com sotaque americano de mulher jovem latina, voz autêntica, rápida, urgente e emocional, como se exigisse ser ouvida, a seguinte frase: "How do I know? Because you're still here. Out of everyone scrolling tonight, it stopped on you, and I felt it."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ela faz uma pausa curta depois da pergunta, e encosta a mão direita no próprio peito ao dizer que sentiu.

câmera: fixa

som ambiente: quarto silencioso, sem música, sem ruído de fundo
```

### V11 · T7 · usa K06

> ### 🖼️ IMAGEM INICIAL NO FLOW: **K06**

```text
a avatar (mulher) fala em inglês com sotaque americano de mulher jovem latina, voz autêntica, rápida, urgente e emocional, como se exigisse ser ouvida, a seguinte frase: "Tomorrow at eleven eleven in the morning, something reaches you that's big enough to split your life in two."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ela marca a hora com dois toques curtos do dedo indicador direito no ar e volta a mão para o baú.

câmera: fixa

som ambiente: quarto silencioso, sem música, sem ruído de fundo
```

### V12 · T8 · usa K07

> ### 🖼️ IMAGEM INICIAL NO FLOW: **K07**

```text
a avatar (mulher) fala em inglês com sotaque americano de mulher jovem latina, voz autêntica, rápida, urgente e emocional, como se exigisse ser ouvida, a seguinte frase: "So tomorrow when you wake up, check your phone. What's waiting there is their face, and it's going to stop you cold."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ela abre a mão direita para a lente ao falar do rosto e para o gesto de uma vez na última palavra, com o olhar fixo.

câmera: fixa

som ambiente: quarto silencioso, sem música, sem ruído de fundo
```

### V13 · T9 · usa K07

> ### 🖼️ IMAGEM INICIAL NO FLOW: **K07**

```text
a avatar (mulher) fala em inglês com sotaque americano de mulher jovem latina, voz autêntica, rápida, urgente e emocional, como se exigisse ser ouvida, a seguinte frase: "Two two two. Type it now, that's you answering out loud. Then send this to yourself and save it."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ela aponta o dedo indicador direito para baixo, na direção de onde fica o comentário, e depois conta as duas outras ações com pequenos movimentos da mesma mão.

câmera: fixa

som ambiente: quarto silencioso, sem música, sem ruído de fundo
```

### V14 · T10 · usa K07

> ### 🖼️ IMAGEM INICIAL NO FLOW: **K07**

```text
a avatar (mulher) fala em inglês com sotaque americano de mulher jovem latina, voz autêntica, rápida, urgente e emocional, como se exigisse ser ouvida, a seguinte frase: "The second you comment, I put their face straight into your messages. That's where the reveal happens, not here."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ela leva a mão direita da lente para o lado ao falar das mensagens, e balança a cabeça de leve na negativa na última palavra.

câmera: fixa

som ambiente: quarto silencioso, sem música, sem ruído de fundo
```

### V15 · T11 · usa K07

> ### 🖼️ IMAGEM INICIAL NO FLOW: **K07**

```text
a avatar (mulher) fala em inglês com sotaque americano de mulher jovem latina, voz autêntica, rápida, urgente e emocional, como se exigisse ser ouvida, a seguinte frase: "But follow me first, or it won't let me reach you. Tomorrow at eleven eleven, open your messages."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ela ergue o dedo indicador direito ao dizer para seguir primeiro, e volta a mão para o baú na segunda frase, mantendo o olhar na lente.

câmera: fixa

som ambiente: quarto silencioso, sem música, sem ruído de fundo
```

### V16 · T12 · usa K08

> ### 🖼️ IMAGEM INICIAL NO FLOW: **K08**

```text
a avatar (mulher) fala em inglês com sotaque americano de mulher jovem latina, voz autêntica, rápida, urgente e emocional, como se exigisse ser ouvida, a seguinte frase: "One last thing. Tap my profile picture and check my stories before they disappear, because the proof they exist is sitting in there."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ela aponta o dedo indicador direito para cima, na direção do canto onde fica a foto de perfil, e mantém contato visual forte até o fim.

câmera: fixa, leve push-in

som ambiente: quarto silencioso, sem música, sem ruído de fundo
```

---

## Mapa de âncoras

| Keyframe | Referências a anexar | Modelo |
|---|---|---|
| REF-CARTA | nenhuma, gerar do zero | Nano Banana **Pro**, regenerar até o foil sair como tinta impressa |
| K01 | âncora Casey + REF-CARTA aprovada | Nano Banana **Pro**, várias variações |
| K02 | K01 aprovado | Nano Banana 2, comando de edição |
| K03 | K01 aprovado | Nano Banana 2, comando de edição |
| K04 | K01 aprovado | Nano Banana 2, comando de edição |
| K05 | K01 aprovado | Nano Banana 2, comando de edição |
| K06 | âncora Casey + REF-CARTA aprovada | Nano Banana **Pro** |
| K07 | K06 aprovado | Nano Banana 2, comando de edição |
| K08 | K06 aprovado (**nunca a partir do K07**) | Nano Banana 2, comando de edição |

---

## Montagem no CapCut

- Timeline 1080x1920, 30 fps.
- **Cortes duros entre todos os takes.** O único que precisa de peso é V01 a V05 para V06, que é a troca
  do Setup A para o Setup B. Nos ganchos 1, 2, 3, 5 e 7 a emenda cai dentro da fumaça, da carta ou das
  cartas passando, então ela some sozinha. **Cortar exatamente no frame em que o quadro está mais coberto.**
- Cortar o silêncio inicial de cada clipe para a fala começar imediatamente.
- **Adesivo de topo, primeiros 55s:** `⚠️ ATTENTION: THURSDAY, SEPTEMBER 3RD`, **com a data trocada a
  cada nova postagem**. É assim que a especificidade do modelo sobrevive sem queimar o clipe.
- **Adesivo de topo, do 55s ao fim:** troca para `Your reading is waiting in your messages ⭐`.
- **Últimos 8s, junto do V16:** legenda fixa `Check out the surprise in my Stories` mais **seta vermelha
  apontando para o canto da foto de perfil**. É a gramática de três camadas do IG19.
- **Canto inferior esquerdo, quase o vídeo todo:** dois comentários falsos fixos, `222` e `Amen`, que
  somem nos últimos segundos.
- Legenda karaokê palavra a palavra, padrão do nicho. **Nunca cobrir a carta.**
- Manter `222` isolado na tela no V13.
- Color grading: temp -3, tint +2, saturação -6, exposição -3, contraste +12, highlight -35, shadow +18, fade +6.

---

## Gates de qualidade

1. Casey é a mesma mulher em todos os clipes, com **as duas mechas loiras da frente** em todos.
2. **A acne está preservada em todos os keyframes.** Nenhum frame com pele lisa, alisada ou maquiada.
3. A cruz é de **PRATA** em todos, e não aparece ouro em lugar nenhum.
4. **A bandeira dos EUA está visível e em foco** em todos os keyframes com cenário.
5. O crucifixo, o mapa de constelação e o pisca-pisca continuam iguais e no mesmo lugar.
6. A carta SOULMATE tem **a mesma arte holográfica** em todos os takes, e a palavra está legível.
7. **O baralho da mesa é holográfico e bate com a carta da mão.** Se um sair fosco, regerar.
8. Nenhuma legenda ou texto foi gerado dentro da imagem.
9. Mãos com cinco dedos, sem fusão com a carta nem com o maço. **O K04 e o K05 são os de maior risco.**
10. **Nenhum celular em quadro em nenhum take**, inclusive no V12 que fala de telefone.
11. A luz do rosto é branca e neutra em todos. **Nenhum cast quente e nenhum roxo ou rosa na pele.**
12. `222` e o follow gate estão os dois presentes, e **o CTA de Stories vem DEPOIS dos dois**.
