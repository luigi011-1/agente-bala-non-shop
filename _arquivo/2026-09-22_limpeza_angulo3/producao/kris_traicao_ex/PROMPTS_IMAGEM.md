# PROMPTS DE IMAGEM · Kris Walker · TRAIÇÃO + VIZINHO

♻️ **VERSÃO 2, 2026-09-12.** Refeito sobre o roteiro v2, em que a personagem nomeia a oferta em cena.

| | |
|---|---|
| **Roteiro** | `producao/kris_traicao_ex/ROTEIRO.md` v2, aprovado em 2026-09-12 |
| **Pipeline** | `auraly` · Ângulo 3 · keyword `222` |
| **Ganchos visuais** | **um só**, por decisão do Luigi |
| **Âncora da Kris** | `producao/_ancoras/Kris.Walker_us .jpeg` |
| **Modelo** | Nano Banana 2 · 9:16 · uma imagem final por `K__` |

---

## 🔴 TRÊS CICLOS DE ÂNCORA

O agente do Flow anexa **uma** âncora em todas as gerações do ciclo. Este roteiro tem três pessoas com
rosto, então ele roda em três ciclos, separados pela frase `finalizamos, vamos para o próximo avatar`.

| Ciclo | Âncora | Keyframes | Quem fala |
|---|---|---|---|
| 0 | **nada anexado** | REF-MAYA, REF-DEREK, REF-CARTA | ninguém, são referências |
| 1 | REF-MAYA | K01, K03, K04, K05, K06, K07, K08, K09 | Maya |
| 2 | REF-DEREK | K02 | Derek |
| 3 | `Kris.Walker_us .jpeg` + REF-CARTA | K10, K11, K12, K13 | Kris |

**Por que funciona:** no K02 a Maya entra cortada pelo quadro **com o rosto fora de cena**, então a
âncora ativa é sempre a da pessoa cujo rosto aparece. Nenhuma geração depende de duas identidades.

♻️ **A REF-TASHA saiu do pacote** junto com a amiga, na v2. São três ciclos, não quatro.

## ÍNDICE DE GERAÇÃO

| Take | Keyframe | Ação | Anexos | Ciclo |
|---|---|---|---|---|
| T1 | K01 | GERAR DO ZERO | ÂNCORA MAYA | 1 |
| T2 | K02 | GERAR DO ZERO | ÂNCORA DEREK | 2 |
| T3 | K03 | GERAR DO ZERO | ÂNCORA MAYA | 1 |
| T4 | K04 | GERAR DO ZERO | ÂNCORA MAYA | 1 |
| T5 | K05 | GERAR DO ZERO | ÂNCORA MAYA | 1 |
| T6 | K06 | GERAR DO ZERO | ÂNCORA MAYA | 1 |
| T7 | K07 | GERAR DO ZERO | ÂNCORA MAYA | 1 |
| T8 | K08 | GERAR DO ZERO | ÂNCORA MAYA | 1 |
| T9 | K09 | GERAR DO ZERO | ÂNCORA MAYA | 1 |
| T10 | K10 | GERAR DO ZERO | ÂNCORA KRIS + REF-CARTA | 3 |
| T11 | K11 | GERAR DO ZERO | ÂNCORA KRIS + REF-CARTA | 3 |
| T12 | K12 | GERAR DO ZERO | ÂNCORA KRIS + REF-CARTA | 3 |
| T13 | K13 | GERAR DO ZERO | ÂNCORA KRIS + REF-CARTA | 3 |

**13 takes, 13 keyframes, 13 clipes.** Um keyframe nunca serve dois takes.

---

## TRAVAS GLOBAIS

### Identidade e continuidade
Cada prompt repete por inteiro identidade, roupa, cenário e luz, porque o bloco do Flow é
autossuficiente e o agente recebe só a âncora mais aquele prompt.

### Trava do rosto e do visor
🔴 **O rosto da alma gêmea nunca é revelado.** Nos K04, K05 e K06 o telefone fica **de costas para a**
**lente** e o visor nunca aparece. Quem esconde é o próprio aparelho. Nunca descrever como blur de
câmera, porque o `negative` carrega `no blur` para a cena inteira.

🔴 **Andre nunca tem rosto em quadro.** Só antebraço e mão, entrando pela borda direita.

### Trava da bandeira
Bandeira dos EUA discreta, visível e em foco em **todos** os treze keyframes e nas duas REF de pessoa.
Única exceção: a `REF-CARTA`, prop isolado sem cenário.

### Trava da carta
A `REF-CARTA` entra só a partir do K10 e fica na mão da Kris até o fim. O baralho **da mesa** dela é
clássico de borda branca, e a carta **na mão** é holográfica.

---

## CICLO 0 · REFERÊNCIAS

## REF-MAYA · GERAR DO ZERO · NADA

> ### 📎 ANEXAR: **NADA**
>
> ### 🆕 GERAR DO ZERO

Retrato de identidade, peito para cima, para servir de âncora do ciclo dessa pessoa.

```json
{
  "shot_id": "REF_maya_identity_anchor",
  "reference_use": "Generate one isolated identity reference portrait. No other person in frame and no attached reference.",
  "identity_main": "A Black American woman of thirty one with deep brown skin, visible pores, a natural shine on the forehead, zero makeup, natural tightly coiled hair pulled into a low bun with loose coils at the hairline, full lips, natural eyebrows, tired but composed eyes and short natural nails with no polish.",
  "wardrobe": "A heather grey ribbed tank top, dark straight jeans and thin gold stud earrings, no other jewelry.",
  "scene": "A plain real American room during the day with a neutral off white wall and a small framed United States flag print on the wall behind the shoulder, discreet but clearly visible and in sharp focus. No other objects.",
  "posture": "Standing relaxed, square to the lens, arms down and out of frame, neutral calm expression, eyes on the lens.",
  "composition": "Chest-up identity portrait, the face filling the upper half of the frame, nothing competing.",
  "camera": "eye level, straight-on, close phone-camera distance",
  "state": "Start frame: standing still, before any movement.",
  "lighting": "Soft neutral diffuse daylight of an overcast day from the side, flat and even, no warm cast.",
  "realism": "UGC realism, real skin texture with visible pores, individual hair strands, subtle wrinkles, realistic shadows and reflections, iPhone-footage look, phone camera look not professional photography, no AI polish, no beauty smoothing, no blur anywhere, everything in sharp focus including background walls furniture and details.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no studio, no plastic skin, no extra fingers, no blur, no artificial lighting, no warm orange color cast, no yellow tint, no golden glow, no second person, no beauty retouching"
}
```

## REF-DEREK · GERAR DO ZERO · NADA

> ### 📎 ANEXAR: **NADA**
>
> ### 🆕 GERAR DO ZERO

Retrato de identidade, peito para cima, para servir de âncora do ciclo dessa pessoa.

```json
{
  "shot_id": "REF_derek_identity_anchor",
  "reference_use": "Generate one isolated identity reference portrait. No other person in frame and no attached reference.",
  "identity_main": "A Black American man in his mid thirties with deep brown skin, visible pores, a short fade, a trimmed beard with a few grey hairs, natural eyebrows and an unretouched face.",
  "wardrobe": "A plain black crewneck sweatshirt and dark jeans, no jewelry.",
  "scene": "A plain real American room during the day with a neutral off white wall and a small framed United States flag print on the wall behind the shoulder, discreet but clearly visible and in sharp focus. No other objects.",
  "posture": "Standing relaxed, square to the lens, arms down and out of frame, neutral calm expression, eyes on the lens.",
  "composition": "Chest-up identity portrait, the face filling the upper half of the frame, nothing competing.",
  "camera": "eye level, straight-on, close phone-camera distance",
  "state": "Start frame: standing still, before any movement.",
  "lighting": "Soft neutral diffuse daylight of an overcast day from the side, flat and even, no warm cast.",
  "realism": "UGC realism, real skin texture with visible pores, individual hair strands, subtle wrinkles, realistic shadows and reflections, iPhone-footage look, phone camera look not professional photography, no AI polish, no beauty smoothing, no blur anywhere, everything in sharp focus including background walls furniture and details.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no studio, no plastic skin, no extra fingers, no blur, no artificial lighting, no warm orange color cast, no yellow tint, no golden glow, no second person, no beauty retouching"
}
```

## REF-CARTA · ÂNGULO 3 · GERAR DO ZERO · NADA

> ### 📎 ANEXAR: **NADA**
>
> ### 🆕 GERAR DO ZERO

Se a `REF-CARTA` canônica já estiver aprovada em disco, **reusar e não regenerar**. O JSON abaixo é o
canônico do §10 do `PLAYBOOK_MESTRE_AURALY.md`, colado para o pacote ficar autossuficiente.

⚠️ **O `negative` desta REF é diferente de todos os outros do pacote.** Ele não carrega
`no warm orange color cast`, `no yellow tint` nem `no golden glow`, porque essas linhas matam o foil.

```json
{
  "shot_id": "REF_CARTA_soulmate_holographic",
  "reference_use": "Generate one isolated physical tarot card reference. No person, no hands and no avatar reference.",
  "identity_main": "No person. One premium physical soulmate tarot card only.",
  "prop": "A single vertical tarot card about 10 cm tall, printed on real thick card stock. The illustration shows an elegant adult couple connected by a soft celestial ribbon of light, surrounded by roses, tiny stars and a crescent moon. The artwork is saturated in deep sapphire, magenta, ruby and luminous teal. A wide mirrored silver metallic border produces subtle holographic rainbow reflections, with engraved arabesque flourishes in all four corners. A clean metallic title band at the bottom reads SOULMATE in large legible serif letters. The visual language is sophisticated spiritual tarot art for adults, never childish and never gothic.",
  "scene": "Plain neutral matte tabletop only, no room and no background objects.",
  "composition": "Extreme close-up of the single card lying flat, filling most of the vertical frame, with all four edges visible.",
  "camera": "macro close-up, slightly high toward the card",
  "state": "Start frame: the card lies still on the surface, ready to be reused as a fixed prop reference.",
  "lighting": "Soft neutral diffuse daylight of an overcast day, with realistic reflections on the metallic border.",
  "realism": "UGC realism, real paper texture, tiny edge wear, realistic shadows and reflections, iPhone-footage look, phone camera look not professional photography, no AI polish, no blur anywhere, everything in sharp focus.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no person, no hands, no studio, no plastic texture, no childish illustration, no cartoon look, no blur, no artificial lighting, no gothic art, no skulls, no ravens, no snakes, no swords, no inverted symbols, no sigils"
}
```

---

## CICLO 1 · ÂNCORA REF-MAYA

## K01 · T1 · CAMISA ARREMESSADA · GERAR DO ZERO · ÂNCORA MAYA

> ### 📎 ANEXAR: **1 IMAGEM**
> **1️⃣ REF-MAYA** já aprovada
>
> ### 🆕 GERAR DO ZERO

A camisa com a marca de batom no ar, muito perto da lente, ainda sem encostar nele.

```json
{
  "shot_id": "K01_hook_shirt_thrown_initial",
  "reference_use": "Use the attached image ONLY for Maya's exact face, identity, skin texture, hair and wardrobe. Do NOT copy pose, action, framing or background from the reference.",
  "identity_main": "The EXACT woman from the attached reference image: a Black American woman of thirty one with deep brown skin, visible pores, a natural shine on the forehead, zero makeup, natural tightly coiled hair pulled into a low bun with loose coils at the hairline, full lips, natural eyebrows and short natural nails with no polish.",
  "second_person": "A Black American man in his mid thirties with a short fade and a trimmed beard, in a black crewneck and dark jeans. He stands on the right, cut by the right edge of the frame, only his chest and arm inside the frame.",
  "prop": "A crumpled white cotton men's dress shirt with a smear of dark red lipstick on the inside of the collar. The shirt is bunched in flight, the lipstick mark turned toward the lens and clearly readable.",
  "wardrobe": "The same heather grey ribbed tank top and dark straight jeans from the reference image, thin gold stud earrings and no other jewelry.",
  "scene": "A small real American apartment living room during the day. Only three visual anchors: a beige couch with a woven throw on the left, a white plastic laundry basket on the floor, and a small framed United States flag print on the wall, discreet but clearly visible and in sharp focus.",
  "posture": "Maya stands facing him, weight on the front foot, right arm fully extended forward having just released the shirt, jaw tight and eyes locked on him. Both hands anatomically clear.",
  "composition": "EXTREME CLOSE foreground emphasis. The thrown shirt fills the lower foreground and is much closer to the lens than Maya's face. Maya is chest-up in the upper portion of the frame. Nothing competes with the shirt.",
  "camera": "chest height, straight-on, pushed in very close",
  "state": "Start frame: the shirt has just left her hand and is in the air between them, not yet touching him.",
  "lighting": "Soft neutral diffuse daylight of an overcast day coming from a window outside the frame, no warm cast and no practical lamp lighting the room.",
  "realism": "UGC realism, real skin texture with visible pores, individual hair strands, subtle wrinkles, realistic shadows and reflections, iPhone-footage look, phone camera look not professional photography, no AI polish, no beauty smoothing, no blur anywhere, everything in sharp focus including background walls furniture and details.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no studio, no plastic skin, no extra fingers, no supernatural lighting, no blur, no artificial lighting, no warm orange color cast, no yellow tint, no golden glow, no change of identity, no change of wardrobe"
}
```

## K03 · T3 · FUNDO DO POCO NO SOFA · GERAR DO ZERO · ÂNCORA MAYA

> ### 📎 ANEXAR: **1 IMAGEM**
> **1️⃣ REF-MAYA** já aprovada
>
> ### 🆕 GERAR DO ZERO

As duas bolsas fechadas em primeiro plano junto da porta, ela afundada no sofá atrás.

```json
{
  "shot_id": "K03_rock_bottom_couch_initial",
  "reference_use": "Use the attached image ONLY for Maya's exact face, identity, skin texture, hair and wardrobe. Do NOT copy pose, action, framing or background from the reference.",
  "identity_main": "The EXACT woman from the attached reference image: a Black American woman of thirty one with deep brown skin, visible pores, a natural shine on the forehead, zero makeup, natural tightly coiled hair pulled into a low bun with loose coils at the hairline, full lips, natural eyebrows and short natural nails with no polish. Her eyes are glassy and her face is exhausted, with no tears running.",
  "prop": "Two zipped and overfilled soft dark duffel bags standing on the floor in the lower foreground, the worn handles and a loose strap clearly visible, much closer to the lens than her face.",
  "wardrobe": "The same heather grey ribbed tank top and dark straight jeans from the reference image, thin gold stud earrings and no other jewelry.",
  "scene": "The same real apartment living room during the day, seen from in front of the couch. Only three visual anchors: the beige couch with the woven throw, two zipped duffel bags on the floor by the front door behind her, and the small framed United States flag print on the wall behind her, clearly visible and in sharp focus.",
  "posture": "Maya sits sunk back into the couch behind the bags, arms slack at her sides, head tipped back, looking off lens and then down at the bags.",
  "composition": "The two duffel bags fill the lower foreground and are much closer to the lens than her face. Maya is chest-up behind them, alone. Nothing competes with the bags.",
  "camera": "floor height, slightly low toward the bags, pushed in close",
  "state": "Start frame: Maya is already sunk into the couch and still, before she speaks.",
  "lighting": "Soft neutral diffuse daylight of an overcast day coming from a window outside the frame, no warm cast and no practical lamp lighting the room.",
  "realism": "UGC realism, real skin texture with visible pores, individual hair strands, subtle wrinkles, realistic shadows and reflections, iPhone-footage look, phone camera look not professional photography, no AI polish, no beauty smoothing, no blur anywhere, everything in sharp focus including background walls furniture and details.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no studio, no plastic skin, no extra fingers, no supernatural lighting, no blur, no artificial lighting, no warm orange color cast, no yellow tint, no golden glow, no change of identity, no change of wardrobe"
}
```

## K04 · T4 · O DEBOCHE, ELA LE EM VOZ ALTA · GERAR DO ZERO · ÂNCORA MAYA

> ### 📎 ANEXAR: **1 IMAGEM**
> **1️⃣ REF-MAYA** já aprovada
>
> ### 🆕 GERAR DO ZERO

O telefone de costas para a lente em primeiro plano, ela lendo em voz alta com deboche.

```json
{
  "shot_id": "K04_skeptic_reads_aloud_initial",
  "reference_use": "Use the attached image ONLY for Maya's exact face, identity, skin texture, hair and wardrobe. Do NOT copy pose, action, framing or background from the reference.",
  "identity_main": "The EXACT woman from the attached reference image: a Black American woman of thirty one with deep brown skin, visible pores, a natural shine on the forehead, zero makeup, natural tightly coiled hair pulled into a low bun with loose coils at the hairline, full lips, natural eyebrows and short natural nails with no polish. One eyebrow is raised and the corner of her mouth is pulled into a tired sarcastic smile.",
  "prop": "Her own plain dark phone held upright in both hands, its back turned fully to the lens so the camera never sees what she is looking at. The display faces only her. The phone body itself is what hides it.",
  "wardrobe": "The same heather grey ribbed tank top and dark straight jeans from the reference image, thin gold stud earrings and no other jewelry.",
  "scene": "The same real apartment living room during the day, seen from in front of the couch. Only three visual anchors: the beige couch with the woven throw, two zipped duffel bags on the floor by the front door behind her, and the small framed United States flag print on the wall behind her, clearly visible and in sharp focus.",
  "posture": "Maya sits forward on the couch with her elbows on her knees, both hands holding the phone low in front of her, reading off it with a scornful half smile. Both hands anatomically clear.",
  "composition": "EXTREME CLOSE foreground emphasis. The back of the phone fills the lower foreground and is much closer to the lens than her face. Maya's face fills the upper third. Nothing competes with the phone.",
  "camera": "chest height, straight-on, pushed in very close",
  "state": "Start frame: she is already holding the phone low and reading, before she speaks or taps.",
  "lighting": "Soft neutral diffuse daylight of an overcast day coming from a window outside the frame, no warm cast and no practical lamp lighting the room.",
  "realism": "UGC realism, real skin texture with visible pores, individual hair strands, subtle wrinkles, realistic shadows and reflections, iPhone-footage look, phone camera look not professional photography, no AI polish, no beauty smoothing, no blur anywhere, everything in sharp focus including background walls furniture and details.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no studio, no plastic skin, no extra fingers, no supernatural lighting, no blur, no artificial lighting, no warm orange color cast, no yellow tint, no golden glow, no change of identity, no change of wardrobe"
}
```

## K05 · T5 · A REVELACAO, ELA SE SENTA RETA · GERAR DO ZERO · ÂNCORA MAYA

> ### 📎 ANEXAR: **1 IMAGEM**
> **1️⃣ REF-MAYA** já aprovada
>
> ### 🆕 GERAR DO ZERO

A mão dela subindo aberta em primeiro plano até a boca, o telefone ainda virado para longe da lente.

```json
{
  "shot_id": "K05_reveal_recognition_initial",
  "reference_use": "Use the attached image ONLY for Maya's exact face, identity, skin texture, hair and wardrobe. Do NOT copy pose, action, framing or background from the reference.",
  "identity_main": "The EXACT woman from the attached reference image: a Black American woman of thirty one with deep brown skin, visible pores, a natural shine on the forehead, zero makeup, natural tightly coiled hair pulled into a low bun with loose coils at the hairline, full lips, natural eyebrows and short natural nails with no polish. Her eyes are wide and fixed, her eyebrows high, her mouth beginning to open.",
  "prop": "Her own plain dark phone held upright in her right hand, its back turned fully to the lens so the camera never sees what she is looking at, the display facing only her. Her free left hand rises open into the lower foreground toward her mouth, palm and every finger anatomically clear and much closer to the lens than her face.",
  "wardrobe": "The same heather grey ribbed tank top and dark straight jeans from the reference image, thin gold stud earrings and no other jewelry.",
  "scene": "The same real apartment living room during the day, seen from in front of the couch. Only three visual anchors: the beige couch with the woven throw, two zipped duffel bags on the floor by the front door behind her, and the small framed United States flag print on the wall behind her, clearly visible and in sharp focus.",
  "posture": "Maya has just snapped upright on the couch, spine straight, right hand holding the phone, left hand rising toward her open mouth, shoulders locked.",
  "composition": "EXTREME CLOSE foreground emphasis. Her rising open left hand fills the lower foreground and is much closer to the lens than her face. Maya's face fills the upper third. Nothing competes with the hand.",
  "camera": "chest height, straight-on, pushed in very close",
  "state": "Start frame: she has just seen it and her hand has only begun to rise.",
  "lighting": "Soft neutral diffuse daylight of an overcast day coming from a window outside the frame, no warm cast and no practical lamp lighting the room.",
  "realism": "UGC realism, real skin texture with visible pores, individual hair strands, subtle wrinkles, realistic shadows and reflections, iPhone-footage look, phone camera look not professional photography, no AI polish, no beauty smoothing, no blur anywhere, everything in sharp focus including background walls furniture and details.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no studio, no plastic skin, no extra fingers, no supernatural lighting, no blur, no artificial lighting, no warm orange color cast, no yellow tint, no golden glow, no change of identity, no change of wardrobe"
}
```

## K06 · T6 · A FICHA CAINDO · GERAR DO ZERO · ÂNCORA MAYA

> ### 📎 ANEXAR: **1 IMAGEM**
> **1️⃣ REF-MAYA** já aprovada
>
> ### 🆕 GERAR DO ZERO

O telefone abandonado no colo em primeiro plano, ela olhando a parede do corredor.

```json
{
  "shot_id": "K06_realisation_initial",
  "reference_use": "Use the attached image ONLY for Maya's exact face, identity, skin texture, hair and wardrobe. Do NOT copy pose, action, framing or background from the reference.",
  "identity_main": "The EXACT woman from the attached reference image: a Black American woman of thirty one with deep brown skin, visible pores, a natural shine on the forehead, zero makeup, natural tightly coiled hair pulled into a low bun with loose coils at the hairline, full lips, natural eyebrows and short natural nails with no polish. Her face is slack and thoughtful, eyes unfocused, lips slightly parted.",
  "prop": "Her plain dark phone lying abandoned face down on her lap in the lower foreground, the blank back of it turned to the lens, closer to the lens than her face.",
  "wardrobe": "The same heather grey ribbed tank top and dark straight jeans from the reference image, thin gold stud earrings and no other jewelry.",
  "scene": "The same real apartment living room during the day, seen from in front of the couch. Only three visual anchors: the beige couch with the woven throw, two zipped duffel bags on the floor by the front door behind her, and the small framed United States flag print on the wall behind her, clearly visible and in sharp focus.",
  "posture": "Maya sits back on the couch with both hands loose on either side of the phone in her lap, head turned slowly toward the wall on her right, then back toward the lens.",
  "composition": "The phone lying on her lap occupies the lower foreground, closer to the lens than her face. Maya is chest-up and her face fills the upper third. The room stays recognizable without competing.",
  "camera": "chest height, straight-on, close phone-camera distance",
  "state": "Start frame: the phone is already face down on her lap and she is already still, before she speaks.",
  "lighting": "Soft neutral diffuse daylight of an overcast day coming from a window outside the frame, no warm cast and no practical lamp lighting the room.",
  "realism": "UGC realism, real skin texture with visible pores, individual hair strands, subtle wrinkles, realistic shadows and reflections, iPhone-footage look, phone camera look not professional photography, no AI polish, no beauty smoothing, no blur anywhere, everything in sharp focus including background walls furniture and details.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no studio, no plastic skin, no extra fingers, no supernatural lighting, no blur, no artificial lighting, no warm orange color cast, no yellow tint, no golden glow, no change of identity, no change of wardrobe"
}
```

## K07 · T7 · A MESA DO CAFE · GERAR DO ZERO · ÂNCORA MAYA

> ### 📎 ANEXAR: **1 IMAGEM**
> **1️⃣ REF-MAYA** já aprovada
>
> ### 🆕 GERAR DO ZERO

As duas canecas e o antebraço dele em primeiro plano, ela do outro lado da mesa.

```json
{
  "shot_id": "K07_cafe_table_initial",
  "reference_use": "Use the attached image ONLY for Maya's exact face, identity, skin texture, hair and wardrobe. Do NOT copy pose, action, framing or background from the reference. The man's arm is NOT from the attached reference.",
  "identity_main": "The EXACT woman from the attached reference image: a Black American woman of thirty one with deep brown skin, visible pores, a natural shine on the forehead, zero makeup, natural tightly coiled hair pulled into a low bun with loose coils at the hairline, full lips, natural eyebrows and short natural nails with no polish. Her face is relaxed and lit up, a real unforced smile with the eyes involved.",
  "second_person": "Only a man's right forearm and hand enter from the right edge of the frame, medium brown skin, a plain steel watch on the wrist. No face, no head and no shoulders of this man are in frame.",
  "prop": "Two white ceramic coffee cups on the round metal table in the lower foreground, one close to the man's hand, steam visible from the nearer cup.",
  "wardrobe": "The same heather grey ribbed tank top and dark straight jeans from the reference image, thin gold stud earrings and no other jewelry.",
  "scene": "The sidewalk terrace of a small American coffee shop on an overcast day. Only three visual anchors: a round metal table with two white ceramic cups, a green awning post with a small United States flag clipped to it, clearly visible and in sharp focus, and the quiet street kept small in frame by real distance. Everything in frame stays in sharp focus.",
  "posture": "Maya sits at the table leaning slightly forward toward the man, both hands around her cup, talking and smiling.",
  "composition": "The two cups and the man's forearm fill the lower foreground and are closer to the lens than Maya's face. Maya is chest-up in the upper portion of the frame. The man stays cut by the right edge.",
  "camera": "table height, straight-on toward Maya, close",
  "state": "Start frame: both are already seated and still, cups on the table, before she speaks.",
  "lighting": "Soft neutral diffuse daylight of an overcast day, flat and even, no warm cast and no direct sun.",
  "realism": "UGC realism, real skin texture with visible pores, individual hair strands, subtle wrinkles, realistic shadows and reflections, iPhone-footage look, phone camera look not professional photography, no AI polish, no beauty smoothing, no blur anywhere, everything in sharp focus including background walls furniture and details.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no studio, no plastic skin, no extra fingers, no supernatural lighting, no blur, no artificial lighting, no warm orange color cast, no yellow tint, no golden glow, no change of identity, no change of wardrobe"
}
```

## K08 · T8 · A PROVA, A MAO DELE · GERAR DO ZERO · ÂNCORA MAYA

> ### 📎 ANEXAR: **1 IMAGEM**
> **1️⃣ REF-MAYA** já aprovada
>
> ### 🆕 GERAR DO ZERO

A mão dela fechada sobre a mão dele em primeiro plano.

```json
{
  "shot_id": "K08_proof_hand_initial",
  "reference_use": "Use the attached image ONLY for Maya's exact face, identity, skin texture, hair and wardrobe. Do NOT copy pose, action, framing or background from the reference. The man's hand is NOT from the attached reference.",
  "identity_main": "The EXACT woman from the attached reference image: a Black American woman of thirty one with deep brown skin, visible pores, a natural shine on the forehead, zero makeup, natural tightly coiled hair pulled into a low bun with loose coils at the hairline, full lips, natural eyebrows and short natural nails with no polish. Her expression is warm and steady, a small closed smile.",
  "second_person": "Only a man's right forearm and hand enter from the right edge of the frame, medium brown skin, a plain steel watch on the wrist. No face, no head and no shoulders of this man are in frame.",
  "prop": "Maya's right hand closed gently over the man's hand on the metal table in the lower foreground, both hands anatomically clear and much closer to the lens than her face.",
  "wardrobe": "The same heather grey ribbed tank top and dark straight jeans from the reference image, thin gold stud earrings and no other jewelry.",
  "scene": "The sidewalk terrace of a small American coffee shop on an overcast day. Only three visual anchors: a round metal table with two white ceramic cups, a green awning post with a small United States flag clipped to it, clearly visible and in sharp focus, and the quiet street kept small in frame by real distance. Everything in frame stays in sharp focus.",
  "posture": "Maya leans in over the table, her right hand on his, looking at him and then toward the lens as she speaks.",
  "composition": "The two joined hands fill the lower foreground and are much closer to the lens than her face. Maya is chest-up. Nothing competes with the hands.",
  "camera": "table height, straight-on toward Maya, pushed in close",
  "state": "Start frame: her hand is already resting on his and both are still, before she speaks.",
  "lighting": "Soft neutral diffuse daylight of an overcast day, flat and even, no warm cast and no direct sun.",
  "realism": "UGC realism, real skin texture with visible pores, individual hair strands, subtle wrinkles, realistic shadows and reflections, iPhone-footage look, phone camera look not professional photography, no AI polish, no beauty smoothing, no blur anywhere, everything in sharp focus including background walls furniture and details.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no studio, no plastic skin, no extra fingers, no supernatural lighting, no blur, no artificial lighting, no warm orange color cast, no yellow tint, no golden glow, no change of identity, no change of wardrobe"
}
```

## K09 · T9 · A DEVOLUCAO, DEREK AO FUNDO · GERAR DO ZERO · ÂNCORA MAYA

> ### 📎 ANEXAR: **1 IMAGEM**
> **1️⃣ REF-MAYA** já aprovada
>
> ### 🆕 GERAR DO ZERO

A caneca e a mão dela em primeiro plano, ele pequeno ao fundo virando a cabeça.

```json
{
  "shot_id": "K09_handover_initial",
  "reference_use": "Use the attached image ONLY for Maya's exact face, identity, skin texture, hair and wardrobe. Do NOT copy pose, action, framing or background from the reference. The man in the far background is NOT from the attached reference.",
  "identity_main": "The EXACT woman from the attached reference image: a Black American woman of thirty one with deep brown skin, visible pores, a natural shine on the forehead, zero makeup, natural tightly coiled hair pulled into a low bun with loose coils at the hairline, full lips, natural eyebrows and short natural nails with no polish. Her expression is calm and certain, no longer smiling wide.",
  "second_person": "Far behind her on the sidewalk, small in frame because of real distance and still in sharp focus, a Black American man in his mid thirties in a black crewneck walks past and turns his head to look toward the table. He is small, clearly identifiable and does not speak.",
  "prop": "A single white ceramic coffee cup on the metal table in the lower foreground with her own hand resting flat beside it, the hand and the cup closer to the lens than her face.",
  "wardrobe": "The same heather grey ribbed tank top and dark straight jeans from the reference image, thin gold stud earrings and no other jewelry.",
  "scene": "The sidewalk terrace of a small American coffee shop on an overcast day. Only three visual anchors: a round metal table with two white ceramic cups, a green awning post with a small United States flag clipped to it, clearly visible and in sharp focus, and the quiet street kept small in frame by real distance. Everything in frame stays in sharp focus.",
  "posture": "Maya sits upright at the table, one hand resting flat beside the cup, looking just off lens and then into the lens as she speaks.",
  "composition": "The cup and her resting hand fill the lower foreground and are closer to the lens than her face. Maya is chest-up. The passing man is small in the far background and never competes.",
  "camera": "table height, straight-on toward Maya, close",
  "state": "Start frame: Maya is already seated and still, the man already mid stride behind her.",
  "lighting": "Soft neutral diffuse daylight of an overcast day, flat and even, no warm cast and no direct sun.",
  "realism": "UGC realism, real skin texture with visible pores, individual hair strands, subtle wrinkles, realistic shadows and reflections, iPhone-footage look, phone camera look not professional photography, no AI polish, no beauty smoothing, no blur anywhere, everything in sharp focus including background walls furniture and details.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no studio, no plastic skin, no extra fingers, no supernatural lighting, no blur, no artificial lighting, no warm orange color cast, no yellow tint, no golden glow, no change of identity, no change of wardrobe"
}
```

## CICLO 2 · ÂNCORA REF-DEREK

## K02 · T2 · AS CHAVES NA PORTA · GERAR DO ZERO · ÂNCORA DEREK

> ### 📎 ANEXAR: **1 IMAGEM**
> **1️⃣ REF-DEREK** já aprovada
>
> ### 🆕 GERAR DO ZERO

As chaves do carro na mão dele em primeiro plano, ele parado no vão da porta.

```json
{
  "shot_id": "K02_derek_keys_initial",
  "reference_use": "Use the attached image ONLY for this man's exact face, identity, skin texture, hair, beard and wardrobe. Do NOT copy pose, action, framing or background from the reference.",
  "identity_main": "The EXACT man from the attached reference image, a Black American man in his mid thirties with deep brown skin, visible pores, a short fade and a trimmed beard. He is the main subject of this frame, chest-up, facing the lens.",
  "second_person": "A Black American woman stands on the left, cut by the left edge of the frame, only her shoulder and upper arm inside the frame. Her face is not in frame.",
  "prop": "A small ring of car keys held loosely in his right hand in the lower foreground, the metal catching the flat daylight.",
  "wardrobe": "The same plain black crewneck and dark jeans from the reference image, no jewelry.",
  "scene": "A small real American apartment living room during the day. Only three visual anchors: a beige couch with a woven throw on the left, a white plastic laundry basket on the floor, and a small framed United States flag print on the wall, discreet but clearly visible and in sharp focus. He stands in the open doorway of the room.",
  "posture": "He stands in the doorway, shoulders squared, one hand on the doorframe, looking at her and then toward the lens, calm and unapologetic.",
  "composition": "The car keys fill the lower foreground and are closer to the lens than his face. He is chest-up in the upper portion of the frame. The woman's cut shoulder frames the left edge.",
  "camera": "chest height, straight-on, close phone-camera distance",
  "state": "Start frame: he is already holding the keys and looking at her, before he speaks or turns to leave.",
  "lighting": "Soft neutral diffuse daylight of an overcast day coming from a window outside the frame, no warm cast and no practical lamp lighting the room.",
  "realism": "UGC realism, real skin texture with visible pores, individual hair strands, subtle wrinkles, realistic shadows and reflections, iPhone-footage look, phone camera look not professional photography, no AI polish, no beauty smoothing, no blur anywhere, everything in sharp focus including background walls furniture and details.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no studio, no plastic skin, no extra fingers, no supernatural lighting, no blur, no artificial lighting, no warm orange color cast, no yellow tint, no golden glow, no change of identity, no change of wardrobe"
}
```

## CICLO 3 · ÂNCORA KRIS WALKER

## K10 · T10 · CORTE SECO, A CARTA ENTRA · GERAR DO ZERO · ÂNCORA KRIS + REF-CARTA

> ### 📎 ANEXAR: **2 IMAGENS**
> **1️⃣ ÂNCORA KRIS** `producao/_ancoras/Kris.Walker_us .jpeg`
> **2️⃣ REF-CARTA** já aprovada
>
> ### 🆕 GERAR DO ZERO

A carta SOULMATE erguida em primeiro plano, ela olhando direto para a lente.

```json
{
  "shot_id": "K10_T10_kris_initial",
  "reference_use": "Use the first attached image ONLY for Kris's exact face, identity, hair, skin texture, wardrobe and the identity of her real room. Preserve that same real environment and its established objects. Use the second attached image ONLY as the exact physical SOULMATE tarot card prop. Do NOT copy pose, action or framing from either reference.",
  "identity_main": "The EXACT woman from the first attached reference image: a Black American woman of twenty four with deep brown skin, visible pores, natural shine on the forehead and cheeks, small dark marks on the forehead, the cheek and above the lip, zero makeup, chest length box braids in dark brown with honey highlights parted in the middle and pulled back, dark brown eyes, full lips, natural eyebrows and short natural nails with no polish.",
  "prop": "The exact physical SOULMATE tarot card from the second reference, held upright in one hand in the lower foreground, closer to the lens than her face, fully visible. Its wide mirrored metallic holographic border and the printed SOULMATE title band stay identical to the reference.",
  "wardrobe": "The same brown ribbed short sleeve t-shirt and black trousers from the anchor image, small silver hoop earrings and a thin silver chain with a small silver cross pendant.",
  "scene": "The SAME real daylight bedroom identity as Kris's anchor image. Table group on the light wooden table in the lower third: three classic white bordered tarot cards face up in a row, a green fluorite chunk, a white selenite tower, a ceramic dish with a tall incense stick and visible smoke, and three tealight candles on the right. Wall group: a LARGE United States flag pinned flat on the left, clearly visible and in sharp focus, a wooden crucifix at the centre, and the sun and moon print and the natal chart wheel print on the right. Window on the left, floral bedspread bed behind her and a wooden dresser with a pothos in a terracotta pot on the right. Preserve the established room and do not invent a different location.",
  "posture": "Kris sits upright behind the table, shoulders relaxed, holding the SOULMATE card upright in her right hand in the lower foreground, looking straight into the lens, calm and direct.",
  "composition": "Tight chest-up talking frame. The SOULMATE card occupies the lower foreground and is closer to the lens than her face. Kris's face fills the upper third. The room stays recognizable without competing with the card.",
  "camera": "eye level, straight-on, close phone-camera distance",
  "state": "Start frame: Kris already holds the card in position and looks into the lens, before speaking or gesturing.",
  "lighting": "Soft neutral diffuse daylight from the window on the left, matching Kris's real room, no warm cast. The tealight candles and the incense do not light the room.",
  "realism": "UGC realism, real skin texture with visible pores, individual hair strands, subtle wrinkles, realistic shadows and reflections, iPhone-footage look, phone camera look not professional photography, no AI polish, no beauty smoothing, no blur anywhere, everything in sharp focus including background walls furniture and details.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no studio, no plastic skin, no extra fingers, no supernatural lighting, no blur, no artificial lighting, no warm orange color cast, no yellow tint, no golden glow, no change of identity, no change of wardrobe"
}
```

## K11 · T11 · A DECLARACAO, CARTA ERGUIDA · GERAR DO ZERO · ÂNCORA KRIS + REF-CARTA

> ### 📎 ANEXAR: **2 IMAGENS**
> **1️⃣ ÂNCORA KRIS** `producao/_ancoras/Kris.Walker_us .jpeg`
> **2️⃣ REF-CARTA** já aprovada
>
> ### 🆕 GERAR DO ZERO

A carta na altura do maxilar, sem cobrir o rosto, a mão livre aberta sobre a mesa.

```json
{
  "shot_id": "K11_T11_kris_initial",
  "reference_use": "Use the first attached image ONLY for Kris's exact face, identity, hair, skin texture, wardrobe and the identity of her real room. Preserve that same real environment and its established objects. Use the second attached image ONLY as the exact physical SOULMATE tarot card prop. Do NOT copy pose, action or framing from either reference.",
  "identity_main": "The EXACT woman from the first attached reference image: a Black American woman of twenty four with deep brown skin, visible pores, natural shine on the forehead and cheeks, small dark marks on the forehead, the cheek and above the lip, zero makeup, chest length box braids in dark brown with honey highlights parted in the middle and pulled back, dark brown eyes, full lips, natural eyebrows and short natural nails with no polish.",
  "prop": "The exact physical SOULMATE tarot card from the second reference, held upright in one hand in the lower foreground, closer to the lens than her face, fully visible. Its wide mirrored metallic holographic border and the printed SOULMATE title band stay identical to the reference.",
  "wardrobe": "The same brown ribbed short sleeve t-shirt and black trousers from the anchor image, small silver hoop earrings and a thin silver chain with a small silver cross pendant.",
  "scene": "The SAME real daylight bedroom identity as Kris's anchor image. Table group on the light wooden table in the lower third: three classic white bordered tarot cards face up in a row, a green fluorite chunk, a white selenite tower, a ceramic dish with a tall incense stick and visible smoke, and three tealight candles on the right. Wall group: a LARGE United States flag pinned flat on the left, clearly visible and in sharp focus, a wooden crucifix at the centre, and the sun and moon print and the natal chart wheel print on the right. Window on the left, floral bedspread bed behind her and a wooden dresser with a pothos in a terracotta pot on the right. Preserve the established room and do not invent a different location.",
  "posture": "Kris sits upright and raises the SOULMATE card to chest height beside her jaw, never covering her face, her free hand open on the table, looking straight into the lens.",
  "composition": "Chest-up talking frame, slightly closer than the previous setup. The raised SOULMATE card is in the lower foreground beside her jaw and stays closer to the lens than her face. Nothing else competes.",
  "camera": "eye level, straight-on, close phone-camera distance",
  "state": "Start frame: Kris already holds the card in position and looks into the lens, before speaking or gesturing.",
  "lighting": "Soft neutral diffuse daylight from the window on the left, matching Kris's real room, no warm cast. The tealight candles and the incense do not light the room.",
  "realism": "UGC realism, real skin texture with visible pores, individual hair strands, subtle wrinkles, realistic shadows and reflections, iPhone-footage look, phone camera look not professional photography, no AI polish, no beauty smoothing, no blur anywhere, everything in sharp focus including background walls furniture and details.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no studio, no plastic skin, no extra fingers, no supernatural lighting, no blur, no artificial lighting, no warm orange color cast, no yellow tint, no golden glow, no change of identity, no change of wardrobe"
}
```

## K12 · T12 · O SELO, DUAS MAOS NA CARTA · GERAR DO ZERO · ÂNCORA KRIS + REF-CARTA

> ### 📎 ANEXAR: **2 IMAGENS**
> **1️⃣ ÂNCORA KRIS** `producao/_ancoras/Kris.Walker_us .jpeg`
> **2️⃣ REF-CARTA** já aprovada
>
> ### 🆕 GERAR DO ZERO

A carta segura com as duas mãos abaixo da clavícula, plano mais fechado.

```json
{
  "shot_id": "K12_T12_kris_initial",
  "reference_use": "Use the first attached image ONLY for Kris's exact face, identity, hair, skin texture, wardrobe and the identity of her real room. Preserve that same real environment and its established objects. Use the second attached image ONLY as the exact physical SOULMATE tarot card prop. Do NOT copy pose, action or framing from either reference.",
  "identity_main": "The EXACT woman from the first attached reference image: a Black American woman of twenty four with deep brown skin, visible pores, natural shine on the forehead and cheeks, small dark marks on the forehead, the cheek and above the lip, zero makeup, chest length box braids in dark brown with honey highlights parted in the middle and pulled back, dark brown eyes, full lips, natural eyebrows and short natural nails with no polish.",
  "prop": "The exact physical SOULMATE tarot card from the second reference, held upright in one hand in the lower foreground, closer to the lens than her face, fully visible. Its wide mirrored metallic holographic border and the printed SOULMATE title band stay identical to the reference.",
  "wardrobe": "The same brown ribbed short sleeve t-shirt and black trousers from the anchor image, small silver hoop earrings and a thin silver chain with a small silver cross pendant.",
  "scene": "The SAME real daylight bedroom identity as Kris's anchor image. Table group on the light wooden table in the lower third: three classic white bordered tarot cards face up in a row, a green fluorite chunk, a white selenite tower, a ceramic dish with a tall incense stick and visible smoke, and three tealight candles on the right. Wall group: a LARGE United States flag pinned flat on the left, clearly visible and in sharp focus, a wooden crucifix at the centre, and the sun and moon print and the natal chart wheel print on the right. Window on the left, floral bedspread bed behind her and a wooden dresser with a pothos in a terracotta pot on the right. Preserve the established room and do not invent a different location.",
  "posture": "Kris holds the SOULMATE card upright with both hands just below her collarbone, elbows resting on the table, leaning slightly toward the lens, looking straight into it.",
  "composition": "Tighter chest-up frame. The SOULMATE card held in both hands fills the lower foreground, closer to the lens than her face. The table group is only partly in frame because the shot is closer.",
  "camera": "eye level, straight-on, close phone-camera distance",
  "state": "Start frame: Kris already holds the card in position and looks into the lens, before speaking or gesturing.",
  "lighting": "Soft neutral diffuse daylight from the window on the left, matching Kris's real room, no warm cast. The tealight candles and the incense do not light the room.",
  "realism": "UGC realism, real skin texture with visible pores, individual hair strands, subtle wrinkles, realistic shadows and reflections, iPhone-footage look, phone camera look not professional photography, no AI polish, no beauty smoothing, no blur anywhere, everything in sharp focus including background walls furniture and details.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no studio, no plastic skin, no extra fingers, no supernatural lighting, no blur, no artificial lighting, no warm orange color cast, no yellow tint, no golden glow, no change of identity, no change of wardrobe"
}
```

## K13 · T13 · O DESTINO, O PLANO MAIS FECHADO · GERAR DO ZERO · ÂNCORA KRIS + REF-CARTA

> ### 📎 ANEXAR: **2 IMAGENS**
> **1️⃣ ÂNCORA KRIS** `producao/_ancoras/Kris.Walker_us .jpeg`
> **2️⃣ REF-CARTA** já aprovada
>
> ### 🆕 GERAR DO ZERO

O plano mais fechado do vídeo, a carta no rodapé e o indicador apontando para a lente.

```json
{
  "shot_id": "K13_T13_kris_initial",
  "reference_use": "Use the first attached image ONLY for Kris's exact face, identity, hair, skin texture, wardrobe and the identity of her real room. Preserve that same real environment and its established objects. Use the second attached image ONLY as the exact physical SOULMATE tarot card prop. Do NOT copy pose, action or framing from either reference.",
  "identity_main": "The EXACT woman from the first attached reference image: a Black American woman of twenty four with deep brown skin, visible pores, natural shine on the forehead and cheeks, small dark marks on the forehead, the cheek and above the lip, zero makeup, chest length box braids in dark brown with honey highlights parted in the middle and pulled back, dark brown eyes, full lips, natural eyebrows and short natural nails with no polish.",
  "prop": "The exact physical SOULMATE tarot card from the second reference, held upright in one hand in the lower foreground, closer to the lens than her face, fully visible. Its wide mirrored metallic holographic border and the printed SOULMATE title band stay identical to the reference.",
  "wardrobe": "The same brown ribbed short sleeve t-shirt and black trousers from the anchor image, small silver hoop earrings and a thin silver chain with a small silver cross pendant.",
  "scene": "The SAME real daylight bedroom identity as Kris's anchor image. Table group on the light wooden table in the lower third: three classic white bordered tarot cards face up in a row, a green fluorite chunk, a white selenite tower, a ceramic dish with a tall incense stick and visible smoke, and three tealight candles on the right. Wall group: a LARGE United States flag pinned flat on the left, clearly visible and in sharp focus, a wooden crucifix at the centre, and the sun and moon print and the natal chart wheel print on the right. Window on the left, floral bedspread bed behind her and a wooden dresser with a pothos in a terracotta pot on the right. Preserve the established room and do not invent a different location.",
  "posture": "Kris leans in, holding the SOULMATE card upright in one hand at the very bottom of the frame, her free index finger entering from the lower edge and pointing toward the lens, expression urgent and certain.",
  "composition": "THE TIGHTEST FRAME OF THE WHOLE VIDEO. Only Kris's face and the SOULMATE card are dominant. The card is at the very bottom of the frame and closest to the lens. The room is barely in frame.",
  "camera": "eye level, straight-on, pushed in about twenty percent closer than the other Kris setups",
  "state": "Start frame: Kris already holds the card in position and looks into the lens, before speaking or gesturing.",
  "lighting": "Soft neutral diffuse daylight from the window on the left, matching Kris's real room, no warm cast. The tealight candles and the incense do not light the room.",
  "realism": "UGC realism, real skin texture with visible pores, individual hair strands, subtle wrinkles, realistic shadows and reflections, iPhone-footage look, phone camera look not professional photography, no AI polish, no beauty smoothing, no blur anywhere, everything in sharp focus including background walls furniture and details.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no studio, no plastic skin, no extra fingers, no supernatural lighting, no blur, no artificial lighting, no warm orange color cast, no yellow tint, no golden glow, no change of identity, no change of wardrobe"
}
```
