# `sexta_pessoa` · Ângulo 3 (Auraly) · Prompts de imagem

- **Vídeo modelo:** `C:\Users\luigi\Downloads\snapinsta-1788806271562.mp4`
- **Funil:** vídeo → selo (`222` + like + save + follow) → STORIES (revelação do rosto) → link. DM = recuperação pela plataforma.
- **5 ganchos escolhidos (só o T1 / Setup A muda entre eles):** a letra na areia · o selo de cera com a inicial · o louro com a letra de madeira · a segunda mão · o mel sobre a carta.
- **Estrutura por avatar:** REF-CARTA e REF-A são de PRODUÇÃO, geradas uma vez e reaproveitadas nos 5 avatares. Por avatar: 5 keyframes de gancho (Setup A) + 1 body (Setup B) + 1 CTA (Setup B) = 7 keyframes.
- **Ordem de geração:** REF-CARTA → REF-A → K01 a K05 (cada um GERAR DO ZERO da âncora, são setups diferentes) → K06 (GERAR DO ZERO) → K07 (EDITAR do K06).

## Roster desta produção (resolvido, Luigi 2026-09-07)

**A identidade de cada avatar sai da IMAGEM da âncora enviada. O nome da pasta é o rótulo do arquivo, não o roster canônico de `avatares-fichas`.** Regra do `PLAYBOOK_MESTRE_AURALY.md` §8.

| Slug / rótulo | Âncora | A imagem mostra |
|---|---|---|
| `casey_harrisson` | `casey.harrisson_us .jpeg` | latina, 21, acne, money piece loiro, senta no chão, baú, pisca-pisca branco frio |
| `kris_walker` | `Kris.Walker_us .jpeg` | negra, 24, box braids com mel, mesa de quarto de dia, três cartas em fila |
| `shelby_turner` | `ShelbyTurner.us .jpeg` | branca, meados dos 20, sardas e acne, tatuagem de lua no pulso esquerdo, senta no chão, caixote |
| `kelly_bennett` | `Kelly Bennett.jpeg` | senhora ~72, bob prateado, óculos de aro dourado, cozinha de carvalho, aliança de ouro |
| `robin_matthews` | `Robin Matthews .jpeg` | mulher fim dos 30, ondas loiras de sol, franja cortina, anéis de pedra da lua, cartas sob as mãos |

Os JSON de imagem de **todos os 5** estão em `producao/sexta_pessoa/pacote_browser/<slug>/` no formato Modo B
(um `.md` por asset com anexo, ação, cena, JSON, nome do download, checklist e recuperação, mais
`MAPA_ABAS.md` e `CHECKLIST_REVISAO.md`). Este arquivo carrega o lote da Casey inteiro como referência do formato;
os outros 4 seguem a mesma estrutura, mudando só identidade, cenário e caminho da âncora.

---

## Índice de geração (lote Casey Harrisson)

| Take | Keyframe | Ação de geração | Anexar |
|---|---|---|---|
| ref | REF-CARTA | GERAR DO ZERO, prop isolado. Aprovar antes de tudo | NADA |
| ref | REF-A | GERAR DO ZERO, mão da 2ª pessoa cortada pelo quadro. Aprovar antes do K04 | NADA |
| T1 (gancho 1) | K01 · a letra na areia | GERAR DO ZERO | âncora Casey + REF-CARTA |
| T1 (gancho 2) | K02 · o selo de cera | GERAR DO ZERO | âncora Casey + REF-CARTA |
| T1 (gancho 3) | K03 · o louro com a letra | GERAR DO ZERO | âncora Casey + REF-CARTA |
| T1 (gancho 4) | K04 · a segunda mão | GERAR DO ZERO | âncora Casey + REF-CARTA + REF-A |
| T1 (gancho 5) | K05 · o mel sobre a carta | GERAR DO ZERO | âncora Casey + REF-CARTA |
| T2, T3 | K06 · body / leitura | GERAR DO ZERO | âncora Casey + REF-CARTA |
| T4 | K07 · share + prova | EDITAR do K06 | K06 aprovado |
| T5 | K08 · CTA Stories | EDITAR do K06 | K06 aprovado |

Regra de bolso do anexo: GERAR DO ZERO anexa âncora mais REF, EDITAR anexa só o keyframe de origem.
**🚫 Nunca anexar o K07 no prompt do K07. Nunca gerar K02 a K05 a partir do K01.**

---

## Trava de identidade e continuidade (Casey Harrisson)

Aplicar em toda imagem:

- **A EXATA mulher da âncora anexada.** Mulher americana de traços latinos, **21 anos**, magra, a mais nova do roster. Pele oliva clara com **acne ativa nas bochechas e no queixo mais marcas reais de acne**, poros visíveis, **zero maquiagem**. A pele com acne é traço, não defeito: `no de-aging`, `no skin smoothing`, `no makeup` obrigatórios no negative.
- **Cabelo liso castanho escuro, longo, risca ao meio, com DUAS MECHAS LOIRAS DESCOLORIDAS enquadrando o rosto** (money piece). Rosto de coração, queixo estreito, lábios cheios, sobrancelhas grossas escuras, olhos castanho escuros.
- **Moletom CROPPED cinza mescla de gola careca**, calça preta. **Argolas pequenas de prata** e **corrente fina de PRATA com pingente pequeno de cruz de prata.** Nunca ouro.
- **Cenário, o mesmo quarto vivido da âncora, sem mudar nada.** Ela senta no chão aos pés da cama, com um **baú de madeira escura** na frente fazendo as vezes de mesa, no terço inferior do quadro. Não listar a bagunça item a item: escrever `the same lived-in bedroom as the reference image, unchanged` mais as âncoras que importam.
- **Kit de tarólogo, agrupado em dois blocos** (conta como duas âncoras de fundo, não como oito objetos):
  - no baú à frente dela: leque de cartas HOLOGRÁFICAS com THE LOVERS virada para cima, quartzo rosa bruto, geodo de celestita azul, prato de terracota com vareta de incenso e fumaça fina visível, vela branca acesa em pote de vidro
  - na parede atrás dela: bandeira dos EUA esticada, mapa de constelação emoldurado (disco de estrelas branco sobre preto), crucifixo de madeira
- **Pisca-pisca de luz BRANCA FRIA em festão** acompanhando o topo da parede, e **cama desarrumada atrás**. É dela sozinha, fica. O pisca-pisca ilumina só a parede, o rosto é lavado por luz branca neutra. Nunca pisca-pisca quente.
- **Luz diurna neutra e difusa de dia nublado**, sem cast quente. Zero blur, tudo em foco nítido incluindo parede e prateleira. Cara de filmagem de iPhone, nunca polimento de IA.
- A bandeira dos EUA da parede conta como uma das âncoras de fundo e tem que aparecer visível e em foco.

**Bloco de realismo padrão (colar em todo prompt):**
`UGC realism, real skin texture with visible pores, individual hair strands, subtle wrinkles, active acne and acne scars kept exactly as in the reference, realistic shadows and reflections, iPhone-footage look, phone camera look not professional photography, no AI polish, no beauty smoothing, no blur anywhere, everything in sharp focus including background wall furniture and details.`

**Negative base do avatar (colar em todo prompt de geração):**
`no captions, no subtitles, no words overlaid on the image, no studio, no plastic skin, no extra fingers, no supernatural lighting, no blur, no artificial lighting, no warm orange color cast, no yellow tint, no golden glow, no de-aging, no skin smoothing, no makeup, no second person`

Nos prompts de EDIÇÃO acrescentar: `Do not make her skin darker, yellowish or orangish. Do not make the colors more saturated.`

---

## Trava do prop herói · REF-CARTA (a carta SOULMATE holográfica)

Gerar **uma vez** para a produção inteira, aprovar, e anexar como referência de objeto em todo keyframe que a mostre. Sem isso a arte muda de take pra take.

> ### 📎 ANEXAR: **NADA**
>
> ### 🆕 GERAR DO ZERO

```json
{
  "shot_id": "REF_CARTA_soulmate_holographic",
  "reference_use": "Generate an isolated prop reference. No person, no avatar identity.",
  "identity_main": "No face. One single physical tarot card lying flat on a plain neutral gray surface, all four corners visible.",
  "prop": "A portrait-orientation modern foil tarot card about 7 by 12 centimeters with rounded corners and a clean printed surface. WIDE mirror-silver metallic border with a rainbow holographic sheen and an engraved arabesque flourish in each corner. A serifed Roman numeral at the top. A base title band with the single word SOULMATE in spaced serif capitals. Inside: two timeless robed symbolic figures facing each other in flat symbolic ink-hatched style, a glowing white heart between their heads, rays of light behind them, an arch of roses framing the pair, a stylized sun, crescent moon and five-point stars in the celestial background. The two figures have NO recognizable facial features. Saturated palette: crimson and pink roses, lavender, warm gold and white light over the mirrored rainbow border.",
  "scene": "Plain neutral matte gray tabletop only, no room, no background objects.",
  "composition": "The single card fills most of the vertical frame, flat and centered. Nothing else competes.",
  "camera": "top-down, slightly angled, close to the card",
  "state": "Start frame: the card lies still, ready to be used as a fixed reference prop.",
  "lighting": "Soft neutral daylight of an overcast day.",
  "realism": "UGC realism, real printed foil texture that reflects light as a physical property of the paper, tiny edge wear, realistic reflections, iPhone-footage look, phone camera look not professional photography, no AI polish, everything in sharp focus.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no cartoon style, no children's book illustration, no cute rounded faces, no modern clothing, no plain white border, no comic art, no 3d render, no gothic art, no skulls, no ravens, no snakes, no swords, no inverted symbols, no sigils, no captions, no subtitles, no watermark, no extra text anywhere except the SOULMATE title band"
}
```

Nota técnica: neste prompt as linhas `no golden glow`, `no warm orange color cast`, `no yellow tint` e `no sparkles` ficam FORA de propósito, senão matam o foil e o coração luminoso. O brilho é propriedade impressa do objeto, não luz de cena.

---

## Trava da 2ª pessoa · REF-A (a segunda mão, gancho 4)

Gerar **uma vez** para a produção, aprovar, anexar no K04 de cada avatar. É uma mão de outra pessoa, cortada pelo quadro.

> ### 📎 ANEXAR: **NADA**
>
> ### 🆕 GERAR DO ZERO

```json
{
  "shot_id": "REF_A_second_hand",
  "reference_use": "Generate an isolated reference of one hand only. No face, no full body.",
  "identity_main": "No face. One ordinary adult right hand and part of the forearm, plain skin, short natural nails, no rings, no nail polish, neutral relaxed fingers.",
  "scene": "Plain neutral gray background, nothing else.",
  "composition": "The hand and forearm enter from the right edge of the frame and are CROPPED by that edge, so only the hand and a short length of forearm are visible. The hand is in a gentle pushing gesture, palm angled forward, fingers slightly spread.",
  "camera": "eye level, straight-on, close",
  "state": "Start frame: the hand is mid-push, steady.",
  "lighting": "Soft neutral daylight of an overcast day.",
  "realism": "UGC realism, real skin texture with visible pores, fine hairs and knuckle creases, realistic shadows, iPhone-footage look, no AI polish, no blur anywhere, sharp focus.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no face, no second hand, no rings, no nail polish, no captions, no subtitles, no words overlaid on the image, no studio, no plastic skin, no extra fingers, no supernatural lighting, no blur, no artificial lighting, no warm orange color cast, no yellow tint"
}
```

---

# Prompts de imagem · lote Casey Harrisson

## K01 · T1 · GANCHO A LETRA NA AREIA · GERAR DO ZERO · ÂNCORA CASEY + REF-CARTA

> ### 📎 ANEXAR: **2 IMAGENS**
> **1️⃣ ÂNCORA CASEY** `producao/_ancoras/casey.harrisson_us .jpeg`
> **2️⃣ REF-CARTA** já aprovada
>
> ### 🆕 GERAR DO ZERO

```json
{
  "shot_id": "K01_hook_sand_letter",
  "reference_use": "Use the first attached image ONLY for Casey's face, identity, hair, skin with acne, wardrobe and the exact bedroom scene. Use the second attached image ONLY for the exact art of the SOULMATE tarot card. Keep the attached bedroom scene exactly identical: same wall, bed, string lights, flag, framed star map, crucifix, chest, objects, positions, framing and lighting. Do NOT copy the pose of either reference.",
  "identity_main": "The EXACT woman from the first reference image (Casey Harrisson): American woman of Latina features, 21 years old, slim, olive skin with active acne and acne scars on the cheeks and chin kept exactly as in the reference, visible pores, no makeup. Long straight dark brown hair parted in the middle with two bleached blonde money-piece strands framing the face. Heart-shaped face, narrow chin, full lips, thick dark brows, dark brown eyes.",
  "wardrobe": "Cropped heather-gray crew-neck sweatshirt, black pants, small silver hoop earrings, thin silver chain with a small silver cross pendant.",
  "prop": "A SHALLOW rectangular tray of fine black sand resting on the wooden chest. A single capital letter is drawn into the sand with a fingertip. The holographic SOULMATE tarot card from the second reference lies flat on the chest just beyond the tray, its art fully readable.",
  "scene": "SAME lived-in bedroom as the reference image, unchanged. She sits on the floor at the foot of the bed with the dark wood chest in front of her filling the lower third of the frame. On the chest: holographic tarot fan with THE LOVERS face up, raw rose quartz, blue celestite geode, terracotta dish with a lit incense stick and thin visible smoke, white candle lit in a glass jar. On the wall behind her: the stretched US flag visible and in focus, the framed constellation star-map, the wooden crucifix. Cool white string lights along the top of the wall, unmade bed behind.",
  "posture": "She sits upright facing the camera, chest-up in the upper half of the frame, both hands over the sand tray in the lower foreground, one fingertip still resting where the letter was drawn.",
  "composition": "Plano unico. Chest-up of Casey in the top half, the wooden chest and the black sand tray in the lower third, CLOSER to the lens than her face so the tray and the drawn letter are the hero. The camera is chest level, angled slightly down toward the tray. Nothing competes with the tray and the card. The bedroom reads clearly but sits behind.",
  "camera": "chest level, slightly high toward the sand tray, plano unico from across the chest",
  "state": "Start frame: the capital letter sits complete and crisp in the black sand, she has just finished drawing it and looks straight into the lens, about to speak. She has not blown yet.",
  "lighting": "Soft neutral daylight of an overcast day from the window, cool white glow from the string lights on the wall only. No warm cast on her skin.",
  "realism": "UGC realism, real skin texture with visible pores, individual hair strands, subtle wrinkles, active acne and acne scars kept exactly as in the reference, realistic shadows and reflections, iPhone-footage look, phone camera look not professional photography, no AI polish, no beauty smoothing, no blur anywhere, everything in sharp focus including background wall furniture and details.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no studio, no plastic skin, no extra fingers, no supernatural lighting, no blur, no artificial lighting, no warm orange color cast, no yellow tint, no golden glow, no de-aging, no skin smoothing, no makeup, no second person, no sand already blown away"
}
```

## K02 · T1 · GANCHO O SELO DE CERA COM A INICIAL · GERAR DO ZERO · ÂNCORA CASEY + REF-CARTA

> ### 📎 ANEXAR: **2 IMAGENS**
> **1️⃣ ÂNCORA CASEY** `producao/_ancoras/casey.harrisson_us .jpeg`
> **2️⃣ REF-CARTA** já aprovada
>
> ### 🆕 GERAR DO ZERO

```json
{
  "shot_id": "K02_hook_wax_seal",
  "reference_use": "Use the first attached image ONLY for Casey's face, identity, hair, skin with acne, wardrobe and the exact bedroom scene. Use the second attached image ONLY for the exact art of the SOULMATE tarot card. Keep the attached bedroom scene exactly identical: same wall, bed, string lights, flag, framed star map, crucifix, chest, objects, positions, framing and lighting. Do NOT copy the pose of either reference.",
  "identity_main": "The EXACT woman from the first reference image (Casey Harrisson): American woman of Latina features, 21 years old, slim, olive skin with active acne and acne scars on the cheeks and chin kept exactly as in the reference, visible pores, no makeup. Long straight dark brown hair parted in the middle with two bleached blonde money-piece strands framing the face. Heart-shaped face, narrow chin, full lips, thick dark brows, dark brown eyes.",
  "wardrobe": "Cropped heather-gray crew-neck sweatshirt, black pants, small silver hoop earrings, thin silver chain with a small silver cross pendant.",
  "prop": "The holographic SOULMATE tarot card from the second reference lies flat on the wooden chest. On the lower corner of the card sits a fresh blob of deep red sealing wax with a small brass stamp handle standing upright in it, and a lit white pillar candle beside it with a short stick of red sealing wax next to the candle. The wax blob shows a faint pressed initial starting to take shape, still slightly shapeless.",
  "scene": "SAME lived-in bedroom as the reference image, unchanged. She sits on the floor at the foot of the bed with the dark wood chest in front of her filling the lower third of the frame. On the chest: holographic tarot fan with THE LOVERS face up, raw rose quartz, blue celestite geode, terracotta dish with a lit incense stick and thin visible smoke. On the wall behind her: the stretched US flag visible and in focus, the framed constellation star-map, the wooden crucifix. Cool white string lights along the top of the wall, unmade bed behind.",
  "posture": "She sits upright facing the camera, chest-up in the upper half of the frame, one hand pressing the brass stamp into the wax on the card in the lower foreground, the other flat on the chest.",
  "composition": "Plano unico. Chest-up of Casey in the top half, the chest and the card with the wax seal in the lower third, CLOSER to the lens than her face so the card and the forming seal are the hero. Camera chest level, angled slightly down toward the card. The single small candle flame is isolated in the lower foreground and her face is out of its glow. Nothing else competes.",
  "camera": "chest level, slightly high toward the card and the wax seal, plano unico from across the chest",
  "state": "Start frame: the stamp is pressed down into the red wax, a rough initial just forming, she looks straight into the lens about to speak. The stamp has not been lifted yet.",
  "lighting": "Soft neutral daylight of an overcast day from the window, cool white glow from the string lights on the wall only. The candle flame is a small point of light and does not light the room. No warm cast on her skin.",
  "realism": "UGC realism, real skin texture with visible pores, individual hair strands, subtle wrinkles, active acne and acne scars kept exactly as in the reference, realistic shadows and reflections, iPhone-footage look, phone camera look not professional photography, no AI polish, no beauty smoothing, no blur anywhere, everything in sharp focus including background wall furniture and details.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no studio, no plastic skin, no extra fingers, no supernatural lighting, no blur, no artificial lighting, no warm orange color cast, no yellow tint, no golden glow, no de-aging, no skin smoothing, no makeup, no second person, no room lit by candlelight, no finished clean seal"
}
```

## K03 · T1 · GANCHO O LOURO COM A LETRA DE MADEIRA · GERAR DO ZERO · ÂNCORA CASEY + REF-CARTA

> ### 📎 ANEXAR: **2 IMAGENS**
> **1️⃣ ÂNCORA CASEY** `producao/_ancoras/casey.harrisson_us .jpeg`
> **2️⃣ REF-CARTA** já aprovada
>
> ### 🆕 GERAR DO ZERO

```json
{
  "shot_id": "K03_hook_bay_leaf_letter",
  "reference_use": "Use the first attached image ONLY for Casey's face, identity, hair, skin with acne, wardrobe and the exact bedroom scene. Use the second attached image ONLY for the exact art of the SOULMATE tarot card. Keep the attached bedroom scene exactly identical: same wall, bed, string lights, flag, framed star map, crucifix, chest, objects, positions, framing and lighting. Do NOT copy the pose of either reference.",
  "identity_main": "The EXACT woman from the first reference image (Casey Harrisson): American woman of Latina features, 21 years old, slim, olive skin with active acne and acne scars on the cheeks and chin kept exactly as in the reference, visible pores, no makeup. Long straight dark brown hair parted in the middle with two bleached blonde money-piece strands framing the face. Heart-shaped face, narrow chin, full lips, thick dark brows, dark brown eyes.",
  "wardrobe": "Cropped heather-gray crew-neck sweatshirt, black pants, small silver hoop earrings, thin silver chain with a small silver cross pendant.",
  "prop": "The holographic SOULMATE tarot card from the second reference lies flat and centered on the wooden chest. A ring of dried bay leaves is arranged all the way around the card. Resting at the top of the ring is one small wooden letter tile, a single carved capital letter.",
  "scene": "SAME lived-in bedroom as the reference image, unchanged. She sits on the floor at the foot of the bed with the dark wood chest in front of her filling the lower third of the frame. On the chest: holographic tarot fan with THE LOVERS face up, raw rose quartz, blue celestite geode, terracotta dish with a lit incense stick and thin visible smoke, white candle lit in a glass jar. On the wall behind her: the stretched US flag visible and in focus, the framed constellation star-map, the wooden crucifix. Cool white string lights along the top of the wall, unmade bed behind.",
  "posture": "She sits upright facing the camera, chest-up in the upper half of the frame, both hands just finishing placing the wooden letter tile at the top of the bay-leaf ring in the lower foreground.",
  "composition": "Plano unico. Chest-up of Casey in the top half, the chest with the ringed card and the wooden letter in the lower third, CLOSER to the lens than her face so the ring and the letter are the hero. Camera chest level, angled slightly down toward the card. Nothing competes with the card, the ring and the letter.",
  "camera": "chest level, slightly high toward the ringed card, plano unico from across the chest",
  "state": "Start frame: the bay-leaf ring is complete around the card and the wooden letter is set at the top, her fingertips still on the tile, she looks straight into the lens about to speak.",
  "lighting": "Soft neutral daylight of an overcast day from the window, cool white glow from the string lights on the wall only. No warm cast on her skin.",
  "realism": "UGC realism, real skin texture with visible pores, individual hair strands, subtle wrinkles, active acne and acne scars kept exactly as in the reference, realistic shadows and reflections, iPhone-footage look, phone camera look not professional photography, no AI polish, no beauty smoothing, no blur anywhere, everything in sharp focus including background wall furniture and details.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no studio, no plastic skin, no extra fingers, no supernatural lighting, no blur, no artificial lighting, no warm orange color cast, no yellow tint, no golden glow, no de-aging, no skin smoothing, no makeup, no second person, no burning leaves, no smoke from the leaves"
}
```

## K04 · T1 · GANCHO A SEGUNDA MÃO · GERAR DO ZERO · ÂNCORA CASEY + REF-CARTA + REF-A

> ### 📎 ANEXAR: **3 IMAGENS**
> **1️⃣ ÂNCORA CASEY** `producao/_ancoras/casey.harrisson_us .jpeg`
> **2️⃣ REF-CARTA** já aprovada
> **3️⃣ REF-A** já aprovada (a segunda mão)
>
> ### 🆕 GERAR DO ZERO

```json
{
  "shot_id": "K04_hook_second_hand",
  "reference_use": "Use the first attached image ONLY for Casey's face, identity, hair, skin with acne, wardrobe and the exact bedroom scene. Use the second attached image ONLY for the exact art of the SOULMATE tarot card. Use the third attached image ONLY for the second person's hand so it is clearly that same hand. Keep the attached bedroom scene exactly identical. Do NOT copy the pose of any reference.",
  "identity_main": "The EXACT woman from the first reference image (Casey Harrisson): American woman of Latina features, 21 years old, slim, olive skin with active acne and acne scars on the cheeks and chin kept exactly as in the reference, visible pores, no makeup. Long straight dark brown hair parted in the middle with two bleached blonde money-piece strands framing the face. Heart-shaped face, narrow chin, full lips, thick dark brows, dark brown eyes.",
  "wardrobe": "Cropped heather-gray crew-neck sweatshirt, black pants, small silver hoop earrings, thin silver chain with a small silver cross pendant.",
  "second_person": "The EXACT hand from the third reference image: one ordinary adult hand and part of a forearm, no rings, entering from the RIGHT edge of the frame and CROPPED by that edge so only the hand and a short length of forearm are visible. No face, no body, no shoulder. The hand is pushing the SOULMATE tarot card across the chest toward Casey.",
  "prop": "The holographic SOULMATE tarot card from the second reference lies flat on the wooden chest, being pushed toward Casey by the second hand.",
  "scene": "SAME lived-in bedroom as the reference image, unchanged. She sits on the floor at the foot of the bed with the dark wood chest in front of her filling the lower third of the frame. On the chest: holographic tarot fan with THE LOVERS face up, raw rose quartz, blue celestite geode, terracotta dish with a lit incense stick and thin visible smoke, white candle lit in a glass jar. On the wall behind her: the stretched US flag visible and in focus, the framed constellation star-map, the wooden crucifix. Cool white string lights along the top of the wall, unmade bed behind.",
  "posture": "Casey sits upright facing the camera, chest-up in the upper half of the frame, both her hands open on the chest about to receive the card. The second hand enters from the right, cropped by the frame, mid-push.",
  "composition": "Plano unico. Chest-up of Casey in the top half, the chest and the card in the lower third, CLOSER to the lens than her face so the card and the two hands meeting over it are the hero. The second hand is only partially in frame on the right, cut by the edge. Camera chest level, angled slightly down toward the card. Nothing else competes.",
  "camera": "chest level, slightly high toward the card, plano unico from across the chest",
  "state": "Start frame: the second hand is mid-push, the card sliding toward Casey, her hands open to receive it, she glances at the card then up to the lens.",
  "lighting": "Soft neutral daylight of an overcast day from the window, cool white glow from the string lights on the wall only. No warm cast on her skin.",
  "realism": "UGC realism, real skin texture with visible pores, individual hair strands, subtle wrinkles, active acne and acne scars kept exactly as in the reference, realistic shadows and reflections, iPhone-footage look, phone camera look not professional photography, no AI polish, no beauty smoothing, no blur anywhere, everything in sharp focus including background wall furniture and details.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no studio, no plastic skin, no extra fingers, no supernatural lighting, no blur, no artificial lighting, no warm orange color cast, no yellow tint, no golden glow, no de-aging, no skin smoothing, no makeup, no second face, no second body, no full arm, no visible shoulder of the second person"
}
```

## K05 · T1 · GANCHO O MEL SOBRE A CARTA · GERAR DO ZERO · ÂNCORA CASEY + REF-CARTA

> ### 📎 ANEXAR: **2 IMAGENS**
> **1️⃣ ÂNCORA CASEY** `producao/_ancoras/casey.harrisson_us .jpeg`
> **2️⃣ REF-CARTA** já aprovada
>
> ### 🆕 GERAR DO ZERO

```json
{
  "shot_id": "K05_hook_honey",
  "reference_use": "Use the first attached image ONLY for Casey's face, identity, hair, skin with acne, wardrobe and the exact bedroom scene. Use the second attached image ONLY for the exact art of the SOULMATE tarot card. Keep the attached bedroom scene exactly identical. Do NOT copy the pose of either reference.",
  "identity_main": "The EXACT woman from the first reference image (Casey Harrisson): American woman of Latina features, 21 years old, slim, olive skin with active acne and acne scars on the cheeks and chin kept exactly as in the reference, visible pores, no makeup. Long straight dark brown hair parted in the middle with two bleached blonde money-piece strands framing the face. Heart-shaped face, narrow chin, full lips, thick dark brows, dark brown eyes.",
  "wardrobe": "Cropped heather-gray crew-neck sweatshirt, black pants, small silver hoop earrings, thin silver chain with a small silver cross pendant.",
  "prop": "A SHALLOW plain light ceramic bowl on the wooden chest with the holographic SOULMATE tarot card from the second reference lying flat inside it. She pours amber honey from a spoon over the card and the card is slowly disappearing under the amber. The honey is a thick amber liquid, an object, not a light source. NOT a glass bowl.",
  "scene": "SAME lived-in bedroom as the reference image, unchanged. She sits on the floor at the foot of the bed with the dark wood chest in front of her filling the lower third of the frame. On the chest: holographic tarot fan with THE LOVERS face up, raw rose quartz, blue celestite geode, terracotta dish with a lit incense stick and thin visible smoke, white candle lit in a glass jar. On the wall behind her: the stretched US flag visible and in focus, the framed constellation star-map, the wooden crucifix. Cool white string lights along the top of the wall, unmade bed behind.",
  "posture": "She sits upright facing the camera, chest-up in the upper half of the frame, one hand tilting a spoon of amber honey over the ceramic bowl in the lower foreground, the other steadying the bowl.",
  "composition": "Plano unico. Chest-up of Casey in the top half, the ceramic bowl with the card and the pouring honey in the lower third, CLOSER to the lens than her face so the bowl and the card half-covered in amber are the hero. Camera chest level, angled slightly down toward the bowl. Nothing else competes.",
  "camera": "chest level, slightly high toward the ceramic bowl, plano unico from across the chest",
  "state": "Start frame: the first ribbon of amber honey is falling from the spoon onto the card, the card still mostly visible, she looks from the bowl up to the lens about to speak.",
  "lighting": "Soft neutral daylight of an overcast day from the window, cool white glow from the string lights on the wall only. No warm cast on her skin. The amber color belongs to the honey only, not to the light.",
  "realism": "UGC realism, real skin texture with visible pores, individual hair strands, subtle wrinkles, active acne and acne scars kept exactly as in the reference, realistic shadows and reflections, real honey viscosity and surface reflection, iPhone-footage look, phone camera look not professional photography, no AI polish, no beauty smoothing, no blur anywhere, everything in sharp focus including background wall furniture and details.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no studio, no plastic skin, no extra fingers, no supernatural lighting, no blur, no artificial lighting, no warm orange color cast on skin or walls, no yellow tint on skin, no golden glow lighting, no de-aging, no skin smoothing, no makeup, no second person, no glass bowl, no card fully submerged"
}
```

## K06 · T2, T3 · BODY / LEITURA · GERAR DO ZERO · ÂNCORA CASEY + REF-CARTA

> ### 📎 ANEXAR: **2 IMAGENS**
> **1️⃣ ÂNCORA CASEY** `producao/_ancoras/casey.harrisson_us .jpeg`
> **2️⃣ REF-CARTA** já aprovada
>
> ### 🆕 GERAR DO ZERO

```json
{
  "shot_id": "K06_body_reading",
  "reference_use": "Use the first attached image ONLY for Casey's face, identity, hair, skin with acne, wardrobe and the exact bedroom scene. Use the second attached image ONLY for the exact art of the SOULMATE tarot card she holds. Keep the attached bedroom scene exactly identical. Do NOT copy its pose or framing.",
  "identity_main": "The EXACT woman from the first reference image (Casey Harrisson): American woman of Latina features, 21 years old, slim, olive skin with active acne and acne scars on the cheeks and chin kept exactly as in the reference, visible pores, no makeup. Long straight dark brown hair parted in the middle with two bleached blonde money-piece strands framing the face. Heart-shaped face, narrow chin, full lips, thick dark brows, dark brown eyes.",
  "wardrobe": "Cropped heather-gray crew-neck sweatshirt, black pants, small silver hoop earrings, thin silver chain with a small silver cross pendant.",
  "prop": "The holographic SOULMATE tarot card from the second reference held in her right hand, raised to chest height and angled toward the lens, art readable. Her left hand rests on the chest.",
  "scene": "SAME lived-in bedroom as the reference image, unchanged. She sits on the floor at the foot of the bed with the dark wood chest in front of her filling the lower third of the frame, the tarot fan, rose quartz, celestite geode, incense dish with thin smoke and lit candle on it. On the wall behind her: the stretched US flag visible and in focus, the framed constellation star-map, the wooden crucifix. Cool white string lights along the top of the wall, unmade bed behind.",
  "posture": "She sits upright, close to the camera, chest-up, direct and urgent expression, holding the card up in her right hand.",
  "composition": "Plano unico, tighter than the hooks. Chest-up, her face fills a large part of the frame with the top of her head near the top edge. The SOULMATE card in her raised right hand sits in the lower foreground, closer to the lens than her face, clearly the held object. Little of the room shows, just the wall anchors behind her.",
  "camera": "chest level, straight-on, close",
  "state": "Start frame: she has just raised the card and is speaking directly into the lens.",
  "lighting": "Soft neutral daylight of an overcast day from the window, cool white glow from the string lights on the wall only. No warm cast on her skin.",
  "realism": "UGC realism, real skin texture with visible pores, individual hair strands, subtle wrinkles, active acne and acne scars kept exactly as in the reference, realistic shadows and reflections, iPhone-footage look, phone camera look not professional photography, no AI polish, no beauty smoothing, no blur anywhere, everything in sharp focus including background wall furniture and details.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no studio, no plastic skin, no extra fingers, no supernatural lighting, no blur, no artificial lighting, no warm orange color cast, no yellow tint, no golden glow, no de-aging, no skin smoothing, no makeup, no second person, no phone in frame"
}
```

## K07 · T4 · SHARE + PROVA POR PARTICIPAÇÃO · EDITAR do K06

> ### 📎 ANEXAR: **1 IMAGEM**
> **1️⃣ O K06 já aprovado**
>
> ### ✏️ EDITAR, muda só o enquadramento, o espaço no canto e a expressão
> 🚫 NUNCA anexar o K07 aqui

```json
{
  "task": "edit the attached image, keep everything identical except the changes listed",
  "keep_identical": "Keep Casey exactly the same: same face, same acne and scars, same hair with the two blonde money-piece strands, same silver hoops and silver cross, same cropped gray sweatshirt, same body position, same SOULMATE card in her right hand with the same art. Keep the SAME background exactly: wall, US flag, framed star map, crucifix, string lights, chest with the tarot fan, crystals, incense dish and candle, same lighting, same camera angle.",
  "change_1": "Push the framing in by about fifteen percent so it is the tightest shot of the whole video, chest-up going to shoulders-up, her face dominant. Do not change the camera height or angle.",
  "change_2": "Lower the SOULMATE card slightly and move it a little to her side so the lower-left corner of the frame is clear and open, leaving room for an edit arrow to be added later. Do not cover her face with the card.",
  "change_3": "Her expression is more urgent and direct with strong eye contact straight into the lens.",
  "realism": "UGC realism, real skin texture with visible pores, active acne and acne scars kept exactly as in the reference, iPhone-footage look, no AI polish, no beauty smoothing, no blur anywhere. Do not make her skin darker, yellowish or orangish. Do not make the colors more saturated.",
  "negative": "do not change the face, do not change identity, do not change the acne, do not change the background, do not change the card art, do not change the camera angle, no captions, no subtitles, no words overlaid on the image, no plastic skin, no extra fingers, no warm orange color cast, no yellow tint, no golden glow, no second person, no phone in frame, no arrow drawn in the image"
}
```


## K08 · T5 · CTA STORIES DECLARADO · EDITAR do K06

> ### 📎 ANEXAR: **1 IMAGEM**
> **1️⃣ O K06 já aprovado**
>
> ### ✏️ EDITAR, muda o enquadramento, a mão esquerda, a posição da carta e a expressão
> 🚫 NUNCA anexar o K07 nem o K08 aqui. Este keyframe sai do K06, igual o K07, e nunca de outro estágio.

```json
{
  "task": "edit the attached image, keep everything identical except the changes listed",
  "keep_identical": "Keep Casey exactly the same: same face, same active acne and acne scars, same long dark brown hair with the two bleached blonde money-piece strands, same small silver hoops and thin silver chain with the small silver cross, same cropped heather-gray crew-neck sweatshirt, same seated body position, same holographic SOULMATE card in her right hand with the same art. Keep the SAME background exactly: the wall with the stretched US flag visible and in focus, the framed constellation star-map, the wooden crucifix, the cool white string lights, the unmade bed, the wooden chest with the holographic tarot fan, rose quartz, celestite geode, incense dish with thin smoke and the lit candle. Same neutral overcast daylight, same camera height and angle.",
  "change_1": "Push the framing in by about eight percent, chest-up and slightly tighter than the attached image, but still a little wider than the tightest shot of the video. Do not change the camera height or angle.",
  "change_2": "Raise her LEFT hand and point the index finger straight up past the top edge of the frame, forearm vertical, the gesture clearly aimed above the frame. The hand must not cover her face.",
  "change_3": "Lower the SOULMATE card in her right hand and move it toward the lower right of the frame, still in the lower foreground and closer to the lens than her face, art still readable, so the UPPER LEFT area of the frame is clear and open for an edit arrow to be added later.",
  "change_4": "Her expression is the most urgent of the whole video, direct strong eye contact into the lens, mouth open mid-speech.",
  "realism": "UGC realism, real skin texture with visible pores, individual hair strands, active acne and acne scars kept exactly as in the reference, realistic shadows and reflections, iPhone-footage look, phone camera look not professional photography, no AI polish, no beauty smoothing, no blur anywhere, everything in sharp focus including the background wall and details. Do not make her skin darker, yellowish or orangish. Do not make the colors more saturated.",
  "negative": "do not change the face, do not change identity, do not change the acne, do not change the background, do not change the US flag, do not change the card art, do not change the camera angle, no captions, no subtitles, no words overlaid on the image, no studio, no plastic skin, no extra fingers, no supernatural lighting, no blur, no artificial lighting, no warm orange color cast, no yellow tint, no golden glow, no de-aging, no skin smoothing, no makeup, no second person, no phone in frame, no arrow drawn in the image, no hand covering her face"
}
```

---

## Mapa de âncoras (lote Casey)

| Keyframe | Referências a anexar | Ação |
|---|---|---|
| REF-CARTA | nenhuma | GERAR DO ZERO, prop isolado |
| REF-A | nenhuma | GERAR DO ZERO, mão isolada |
| K01 | âncora Casey + REF-CARTA | GERAR DO ZERO |
| K02 | âncora Casey + REF-CARTA | GERAR DO ZERO |
| K03 | âncora Casey + REF-CARTA | GERAR DO ZERO |
| K04 | âncora Casey + REF-CARTA + REF-A | GERAR DO ZERO |
| K05 | âncora Casey + REF-CARTA | GERAR DO ZERO |
| K06 | âncora Casey + REF-CARTA | GERAR DO ZERO |
| K07 | K06 aprovado | EDITAR |
| K08 | K06 aprovado | EDITAR |

Ordem de geração: REF-CARTA e REF-A primeiro, aprovar. Depois K01 a K06. K07 e K08 só depois do
K06 aprovado, e **os dois saem do K06**, nunca um do outro. Estágio em cascata faz a identidade derivar.

## Gates de qualidade (rodar antes de aprovar cada imagem)

1. É a mesma Casey em todos: acne e cicatrizes preservadas, money piece loiro, cruz de PRATA, argolas de prata.
2. O cenário é o mesmo da âncora, sem objeto novo inventado, sem item removido. Bandeira dos EUA visível e em foco.
3. O herói do gancho está no lower foreground, mais perto da lente que o rosto, e nada compete com ele.
4. Luz neutra de dia nublado. Zero cast quente na pele ou na parede. O pisca-pisca é branco frio e ilumina só a parede.
5. Nenhuma legenda ou texto dentro da imagem. A carta SOULMATE é o único texto permitido, e só quando aparece.
6. K02: a chama da vela é ponto de luz isolado no primeiro plano, o rosto está fora do brilho, o ambiente não está iluminado por vela.
7. K03: as folhas de louro estão arrumadas, nunca queimando, sem fumaça saindo delas.
8. K04: a segunda mão entra só parcialmente, cortada pelo quadro à direita. Zero rosto, zero ombro, zero braço inteiro da 2ª pessoa.
9. K05: tigela de CERÂMICA, nunca vidro. A cor âmbar é do mel, não da luz.
10. K06, K07 e K08: a carta na mão está no lower foreground, sem cobrir o rosto. K07 é o take mais
    fechado do vídeo e tem o canto inferior esquerdo livre pra seta de compartilhar. K08 tem o dedo
    apontando pra cima e o canto superior esquerdo livre pra seta que aponta pra foto de perfil.
13. K08 saiu do K06, nunca do K07. Conferir que a acne, o money piece e a cruz de prata seguem iguais.
11. Mãos com cinco dedos, sem fusão com a carta nem com os props.
12. `no blur` respeitado, fundo em foco nítido.
