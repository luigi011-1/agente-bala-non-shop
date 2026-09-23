# PROMPTS DE PRODUÇÃO · Lynn Parker · CHURRASCO (Ângulo 4)

**Avatar ACTIVE: Lynn Parker.** O pacote do Dana está arquivado em `PROMPTS_DANA_MORRISON.md`.
**Só quatro keyframes e oito clipes são novos.** O resto se reaproveita, ver `AVATAR_QUEUE.md`.

| | |
|---|---|
| **Roteiro** | `producao/dana_churrasco/ROTEIRO.md`, aprovado pelo Luigi em 2026-09-12 |
| **Vídeo modelo** | `Diane Jackson_Obtenha Rhodiola Rosea A_1617284839873263`, 94,7s |
| **Âncora do Lynn** | `producao/_ancoras/lynn_parker_ancora.jpeg` |
| **Ângulo** | 4 · Body Hacks for Men · keyword `yes` |
| **Modelo** | Nano Banana 2 · 9:16 · uma imagem final por `K__` |
| **Reutilização** | **8 imagens para 13 clipes**, e no Lynn só 4 são novas |

---

## ÍNDICE DE GERAÇÃO

| Take | Keyframe | Ação | Anexos | Ciclo |
|---|---|---|---|---|
| REF | REF-NIA | GERAR DO ZERO | NADA | 0 |
| REF | REF-KEITH | GERAR DO ZERO | NADA | 0 |
| REF | REF-TERRELL | GERAR DO ZERO | NADA | 0 |
| REF | REF-LIVRO | GERAR DO ZERO | NADA | 0 |
| T1 | K01 | GERAR DO ZERO | ÂNCORA NIA | 1 |
| T2 | K02 | GERAR DO ZERO | ÂNCORA KEITH | 2 |
| T3 | K03 | GERAR DO ZERO | ÂNCORA TERRELL | 3 |
| T4 e T5 | K04 | GERAR DO ZERO | ÂNCORA TERRELL | 3 |
| T6 a T10 | K06 | GERAR DO ZERO | ÂNCORA DANA + REF-LIVRO | 4 |
| T11 | K11 | GERAR DO ZERO | ÂNCORA TERRELL | 3 |
| T12 | K12 | GERAR DO ZERO | ÂNCORA DANA + REF-LIVRO | 4 |
| T13 | K13 | GERAR DO ZERO | ÂNCORA DANA + REF-LIVRO | 4 |

**13 takes, 8 keyframes, 13 clipes.**

## 🔴 A REGRA DE REUTILIZAÇÃO

Cada `V__` parte do **maior `K__` menor ou igual ao número dele**. Na prática:

```
V01 -> K01   V02 -> K02   V03 -> K03   V04 V05 -> K04
V06 V07 V08 V09 V10 -> K06   V11 -> K11   V12 -> K12   V13 -> K13
```

Não existe nota dentro do bloco do Flow. A regra vive na **memória do agente**, versão 6 do
`producao/_flow/INSTRUCOES_AGENTE_FLOW.md`, e é determinística.

**O K06 sustenta cinco takes de propósito.** É talking head atrás da bancada, sem objeto na mão, e o
vídeo modelo faz o mesmo, sustentando uma posição só por oito takes. O K12 e o K13 têm o livro na
mão e enquadramento diferente, então ganham imagem própria.

## CICLOS DE ÂNCORA

| Ciclo | Âncora | Keyframes | Quem fala |
|---|---|---|---|
| 0 | **nada anexado** | as quatro REF | ninguém |
| 1 | REF-NIA | K01 | Nia |
| 2 | REF-KEITH | K02 | Keith |
| 3 | REF-TERRELL | K03, K04, K11 | Terrell |
| 4 | **âncora do Lynn + REF-LIVRO** | K06, K12, K13 | Lynn |

Em cada keyframe, **só a pessoa cuja âncora está ativa tem rosto em quadro.** Todos os outros entram
cortados pela borda, sem rosto. É o que permite os ciclos separados sem nenhuma geração dependendo de
duas identidades.

## TRAVAS GLOBAIS

## Trava de identidade e continuidade
Cada prompt repete por inteiro identidade, roupa, cenário e luz, porque o bloco do Flow é
autossuficiente. **As locs brancas prateadas e a barba branca do Lynn nunca encurtam**, e o `negative` dele carrega `no de-aging` e `no skin smoothing`, porque a idade é o ativo.

## Trava do prop herói, o livro
O livro entra **fechado no colo dele já no K06**, quarenta segundos antes de ele dizer o nome. Isso é
plantio, não antecipação: o espectador vê o objeto muito antes de ouvir o pitch. No K12 ele levanta
o livro, e é no mesmo take em que o nome é dito.

## Trava da bandeira
Bandeira dos EUA discreta, visível e em foco em **todos** os oito keyframes e nas três REF de pessoa.
Única exceção: a `REF-LIVRO`, prop isolado sem cenário.

## Trava do take mudo
O **K04 é o único B-ROLL do pacote.** A voz do médico entra na edição, e a câmera fica no rosto do
Terrell recebendo a frase. Sai mais forte que filmar o médico falando, e economiza uma âncora inteira.

---

## CICLO 0 · REFERÊNCIAS

## REF-NIA · GERAR DO ZERO · NADA

> ### 📎 ANEXAR: **NADA**
>
> ### 🆕 GERAR DO ZERO

Retrato de identidade, peito para cima, para servir de âncora do ciclo dessa pessoa.

```json
{
  "shot_id": "REF_nia_identity_anchor",
  "reference_use": "Generate one isolated identity reference portrait. No other person in frame and no attached reference.",
  "identity_main": "A Black American woman of forty four with warm brown skin, visible pores, minimal makeup, shoulder length pressed hair, natural eyebrows and an open friendly face.",
  "wardrobe": "A sleeveless olive summer dress and small gold hoop earrings, no other jewelry.",
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

## REF-KEITH · GERAR DO ZERO · NADA

> ### 📎 ANEXAR: **NADA**
>
> ### 🆕 GERAR DO ZERO

Retrato de identidade, peito para cima, para servir de âncora do ciclo dessa pessoa.

```json
{
  "shot_id": "REF_keith_identity_anchor",
  "reference_use": "Generate one isolated identity reference portrait. No other person in frame and no attached reference.",
  "identity_main": "A fit Black American man of about forty seven with medium brown skin, visible pores, a clean shaved head, a neat short beard, natural eyebrows and an easy confident face.",
  "wardrobe": "A fitted grey athletic t-shirt and dark shorts, no jewelry.",
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

## REF-TERRELL · GERAR DO ZERO · NADA

> ### 📎 ANEXAR: **NADA**
>
> ### 🆕 GERAR DO ZERO

Retrato de identidade, peito para cima, para servir de âncora do ciclo dessa pessoa.

```json
{
  "shot_id": "REF_terrell_identity_anchor",
  "reference_use": "Generate one isolated identity reference portrait. No other person in frame and no attached reference.",
  "identity_main": "A Black American man of forty seven with medium brown skin, visible pores, a close cropped fade going grey at the temples, a short trimmed beard, natural eyebrows and tired eyes, unretouched.",
  "wardrobe": "A charcoal short sleeve polo shirt, dark jeans and a plain steel watch, no other jewelry.",
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

## REF-LIVRO · GERAR DO ZERO · NADA

> ### 📎 ANEXAR: **NADA**
>
> ### 🆕 GERAR DO ZERO

O livro físico isolado, para ser anexado em todo keyframe do Dana.

```json
{
  "shot_id": "REF_LIVRO_body_hacks_for_men",
  "reference_use": "Generate one isolated physical book reference. No person, no hands and no avatar reference.",
  "identity_main": "No person. One physical paperback book only.",
  "prop": "A single thick matte paperback book about 23 cm tall lying flat, front cover facing up. The cover is a deep navy blue matte stock with a clean wide cream band across the upper third. Large bold condensed sans serif letters on the band read BODY HACKS FOR MEN, and a smaller line under it reads 42 HABIT HACKS FOR MEN OVER 40. A thin brushed steel rule sits under the subtitle. The spine shows real page thickness with visible page edges and a slightly used corner. The design is plain, masculine and practical, like a real trade paperback, never glossy and never a stack of books.",
  "scene": "Plain neutral matte wooden tabletop only, no room and no background objects.",
  "composition": "Extreme close-up of the single book lying flat, filling most of the vertical frame, with all four edges visible.",
  "camera": "macro close-up, slightly high toward the cover",
  "state": "Start frame: the book lies still and closed on the surface, ready to be reused as a fixed prop reference.",
  "lighting": "Soft neutral diffuse daylight of an overcast day, flat and even, no warm cast.",
  "realism": "UGC realism, real matte paper texture, visible page edges, tiny corner wear, realistic shadows, iPhone-footage look, phone camera look not professional photography, no AI polish, no blur anywhere, everything in sharp focus.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no person, no hands, no studio, no glossy finish, no stack of books, no plastic texture, no cartoon look, no blur, no artificial lighting, no warm orange color cast, no yellow tint, no golden glow"
}
```

---

## CICLO 1 · ÂNCORA REF-NIA

## K01 · T1 · A CHEGADA DO KEITH · GERAR DO ZERO · ÂNCORA NIA

> ### 📎 ANEXAR: **1 IMAGEM**
> **1️⃣ REF-NIA** já aprovada
>
> ### 🆕 GERAR DO ZERO

Nia iluminada em plano médio, o ombro do Keith enchendo o primeiro plano de costas, Terrell cortado na borda esquerda.

```json
{
  "shot_id": "K01_hook_arrival_initial",
  "reference_use": "Use the attached image ONLY for this woman's exact face, identity, skin texture, hair and wardrobe. Do NOT copy pose, action, framing or background from the reference.",
  "identity_main": "The EXACT woman from the attached reference image: a Black American woman of forty four with warm brown skin, visible pores, minimal makeup, shoulder length pressed hair and natural eyebrows. She is the main subject, chest-up, her face lit up in delighted surprise, looking past the lens.",
  "second_person": "A fit Black American man of about forty seven fills the lower foreground seen from BEHIND, only the back of his shoulder and the back of his head in frame, so his face is never visible. On the far left edge, cut by the frame, only the shoulder and forearm of a second man holding a pair of barbecue tongs.",
  "prop": "A pair of stainless barbecue tongs held in the cut man's hand at the lower left of the frame, closed and still, clearly readable.",
  "wardrobe": "The same sleeveless olive summer dress and small gold hoop earrings from the reference image.",
  "scene": "A real American backyard on an overcast afternoon. Only three visual anchors: a black kettle barbecue with thin smoke, a wooden picnic table with red plastic cups, and a small United States flag on the porch post, discreet but clearly visible and in sharp focus.",
  "posture": "Nia has just turned toward the arriving man, shoulders open, both hands coming up in greeting, mouth open in a wide delighted smile.",
  "composition": "The arriving man's back and shoulder fill the lower foreground and are much closer to the lens than Nia's face. Nia is chest-up in the upper portion of the frame. Nothing competes with the arrival.",
  "camera": "chest height, from behind the arriving man's shoulder, pushed in close",
  "state": "Start frame: the arriving man has just stopped walking and Nia has just turned to face him, before anyone speaks.",
  "lighting": "Soft neutral diffuse daylight of an overcast day, flat and even, no warm cast and no direct sun.",
  "realism": "UGC realism, real skin texture with visible pores, individual hair strands, subtle wrinkles, realistic shadows and reflections, iPhone-footage look, phone camera look not professional photography, no AI polish, no beauty smoothing, no blur anywhere, everything in sharp focus including background walls furniture and details.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no studio, no plastic skin, no extra fingers, no supernatural lighting, no blur, no artificial lighting, no warm orange color cast, no yellow tint, no golden glow, no change of identity, no change of wardrobe"
}
```

## CICLO 2 · ÂNCORA REF-KEITH

## K02 · T2 · A FARPA NEGAVEL · GERAR DO ZERO · ÂNCORA KEITH

> ### 📎 ANEXAR: **1 IMAGEM**
> **1️⃣ REF-KEITH** já aprovada
>
> ### 🆕 GERAR DO ZERO

Keith em plano médio batendo no ombro dele, a picape ao fundo, o ombro do Terrell cortado na borda direita.

```json
{
  "shot_id": "K02_jab_initial",
  "reference_use": "Use the attached image ONLY for this man's exact face, identity, skin texture, hair, beard and wardrobe. Do NOT copy pose, action, framing or background from the reference.",
  "identity_main": "The EXACT man from the attached reference image: a fit Black American man of about forty seven with medium brown skin, visible pores, a clean shaved head, a neat short beard and an easy confident face. He is the main subject, chest-up, half turned toward the lens.",
  "second_person": "On the right edge, cut by the frame, only the shoulder and upper arm of another man in a charcoal polo shirt. His face is not in frame.",
  "prop": "Keith's open right hand resting on the cut man's shoulder in the lower foreground, the hand anatomically clear and closer to the lens than Keith's face.",
  "wardrobe": "The same fitted grey athletic t-shirt and dark shorts from the reference image, no jewelry.",
  "scene": "A real American backyard on an overcast afternoon, the concrete driveway visible behind him with an older dark pickup truck parked on it. Only three visual anchors: the parked pickup truck, the wooden picnic table with red plastic cups, and a small United States flag on the porch post, discreet but clearly visible and in sharp focus.",
  "posture": "Keith stands relaxed with his weight on one hip, right hand on the other man's shoulder, head turned to glance toward the parked truck and then back toward the lens.",
  "composition": "Keith's hand on the shoulder fills the lower foreground and is closer to the lens than his face. Keith is chest-up in the upper portion of the frame. The parked truck stays small in the background.",
  "camera": "chest height, straight-on, close phone-camera distance",
  "state": "Start frame: his hand has just landed on the other man's shoulder, before he speaks.",
  "lighting": "Soft neutral diffuse daylight of an overcast day, flat and even, no warm cast and no direct sun.",
  "realism": "UGC realism, real skin texture with visible pores, individual hair strands, subtle wrinkles, realistic shadows and reflections, iPhone-footage look, phone camera look not professional photography, no AI polish, no beauty smoothing, no blur anywhere, everything in sharp focus including background walls furniture and details.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no studio, no plastic skin, no extra fingers, no supernatural lighting, no blur, no artificial lighting, no warm orange color cast, no yellow tint, no golden glow, no change of identity, no change of wardrobe"
}
```

## CICLO 3 · ÂNCORA REF-TERRELL

## K03 · T3 · O PEDIDO REAL · GERAR DO ZERO · ÂNCORA TERRELL

> ### 📎 ANEXAR: **1 IMAGEM**
> **1️⃣ REF-TERRELL** já aprovada
>
> ### 🆕 GERAR DO ZERO

Os dois punhos fechados dele no colo em primeiro plano, ele inclinado para frente na cadeira do consultório.

```json
{
  "shot_id": "K03_real_ask_initial",
  "reference_use": "Use the attached image ONLY for this man's exact face, identity, skin texture, hair, beard and wardrobe. Do NOT copy pose, action, framing or background from the reference.",
  "identity_main": "The EXACT man from the attached reference image: a Black American man of forty seven with medium brown skin, visible pores, a close cropped fade going grey at the temples, a short trimmed beard, natural eyebrows and tired eyes, unretouched. His jaw is set and he is holding eye contact with effort.",
  "second_person": "On the right edge, cut by the frame, only the white coated shoulder and forearm of a doctor seated behind a desk. No face and no head of the doctor is in frame.",
  "prop": "Both of his own hands closed into loose fists on his knees in the lower foreground, the knuckles and tendons anatomically clear and much closer to the lens than his face.",
  "wardrobe": "The same charcoal short sleeve polo shirt and dark jeans from the reference image, a plain steel watch and no other jewelry.",
  "scene": "A small real American doctor's consulting room during the day. Only three visual anchors: a laminate desk with a closed paper folder, a framed certificate on the wall, and a small United States flag on a short pole on the desk, discreet but clearly visible and in sharp focus.",
  "posture": "Terrell sits forward on the patient chair, elbows on his thighs, fists on his knees, looking straight at the doctor and then toward the lens.",
  "composition": "His two closed fists fill the lower foreground and are much closer to the lens than his face. Terrell is chest-up in the upper portion of the frame. The doctor stays cut by the right edge.",
  "camera": "chest height, straight-on toward Terrell, pushed in close",
  "state": "Start frame: he is already leaning forward with his fists on his knees, before he speaks.",
  "lighting": "Soft neutral diffuse daylight of an overcast day coming from a window outside the frame, no warm cast and no practical lamp lighting the room.",
  "realism": "UGC realism, real skin texture with visible pores, individual hair strands, subtle wrinkles, realistic shadows and reflections, iPhone-footage look, phone camera look not professional photography, no AI polish, no beauty smoothing, no blur anywhere, everything in sharp focus including background walls furniture and details.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no studio, no plastic skin, no extra fingers, no supernatural lighting, no blur, no artificial lighting, no warm orange color cast, no yellow tint, no golden glow, no change of identity, no change of wardrobe"
}
```

## K04 · T4 e T5 · O BLOCO DA PICAPE · GERAR DO ZERO · ÂNCORA TERRELL

> ### 📎 ANEXAR: **1 IMAGEM**
> **1️⃣ REF-TERRELL** já aprovada
>
> ### 🆕 GERAR DO ZERO

As duas maos dele no volante em primeiro plano, sozinho no banco do motorista. Este keyframe sustenta dois takes.

```json
{
  "shot_id": "K04_truck_block_initial",
  "reference_use": "Use the attached image ONLY for this man's exact face, identity, skin texture, hair, beard and wardrobe. Do NOT copy pose, action, framing or background from the reference.",
  "identity_main": "The EXACT man from the attached reference image: a Black American man of forty seven with medium brown skin, visible pores, a close cropped fade going grey at the temples, a short trimmed beard, natural eyebrows and tired eyes, unretouched. His eyes are fixed on nothing and his face is exhausted, with no tears.",
  "prop": "Both of his hands gripping the worn steering wheel in the lower foreground, the knuckles and the veins on the backs of the hands anatomically clear and much closer to the lens than his face.",
  "wardrobe": "The same charcoal short sleeve polo shirt and dark jeans from the reference image, a plain steel watch and no other jewelry.",
  "scene": "Inside a real older American pickup truck parked during the day. Only three visual anchors: the worn steering wheel, the cracked dashboard with a paper parking stub on it, and a small United States flag decal on the inside corner of the windshield, discreet but clearly visible and in sharp focus. The parking lot beyond the glass stays small in frame and in sharp focus.",
  "posture": "Terrell sits in the driver seat, both hands on the wheel, not moving, staring through the windshield and then toward the lens.",
  "composition": "His two hands on the wheel fill the lower foreground and are much closer to the lens than his face. Terrell is chest-up in the upper portion of the frame, alone. Nothing competes with the hands.",
  "camera": "chest height from the passenger side, angled toward Terrell, close",
  "state": "Start frame: the engine is off, his hands are already on the wheel and he is already still.",
  "lighting": "Soft neutral diffuse daylight of an overcast day, flat and even, no warm cast and no direct sun.",
  "realism": "UGC realism, real skin texture with visible pores, individual hair strands, subtle wrinkles, realistic shadows and reflections, iPhone-footage look, phone camera look not professional photography, no AI polish, no beauty smoothing, no blur anywhere, everything in sharp focus including background walls furniture and details.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no studio, no plastic skin, no extra fingers, no supernatural lighting, no blur, no artificial lighting, no warm orange color cast, no yellow tint, no golden glow, no change of identity, no change of wardrobe"
}
```

## K11 · T11 · O CONTRAPLANO DO TERRELL · GERAR DO ZERO · ÂNCORA TERRELL

> ### 📎 ANEXAR: **1 IMAGEM**
> **1️⃣ REF-TERRELL** já aprovada
>
> ### 🆕 GERAR DO ZERO

Terrell de pé na frente dele, o pilão de pedra e os potes da prateleira em primeiro plano.

```json
{
  "shot_id": "K11_reverse_terrell_apothecary_initial",
  "reference_use": "Use the attached image ONLY for this man's exact face, identity, skin texture, hair, beard and wardrobe. Do NOT copy pose, action, framing or background from the reference.",
  "identity_main": "The EXACT man from the attached reference image: a Black American man of forty seven with medium brown skin, visible pores, a close cropped fade going grey at the temples, a short trimmed beard, natural eyebrows and tired eyes, unretouched. His eyebrows are raised and his mouth is open in disbelief.",
  "second_person": "On the far right edge, cut by the frame, only the shoulder and a few long white locs of a seated older man in a white tunic. His face is not in frame.",
  "prop": "A grey stone mortar and pestle and two labelled glass herb jars on the shelf in the lower foreground, closer to the lens than Terrell's face. The labels read as printed labels and no specific wording is required.",
  "wardrobe": "The same charcoal short sleeve polo shirt and dark jeans from the reference image, a plain steel watch and no other jewelry.",
  "scene": "The same real home apothecary seen from the opposite side, facing Terrell. Only three visual anchors: the light wood shelving unit packed with labelled glass herb jars behind him, the grey stone mortar and pestle on the shelf in front of him, and a SMALL UNITED STATES FLAG on a desk stand on that shelf, discreet but clearly visible and in sharp focus.",
  "posture": "Terrell stands in front of the seated man, one hand resting on the shelf edge, leaning in, looking down at him and then toward the lens.",
  "composition": "The mortar and the herb jars fill the lower foreground and are closer to the lens than Terrell's face. Terrell is chest-up in the upper portion of the frame. The seated man stays cut by the right edge.",
  "camera": "chest height, straight-on toward Terrell, close",
  "state": "Start frame: he is already leaning on the shelf, before he speaks.",
  "lighting": "Soft neutral diffuse daylight of an overcast day coming from the blinded window on the right, flat and even, no warm cast and no practical lamp lighting the room.",
  "realism": "UGC realism, real skin texture with visible pores, individual hair strands, subtle wrinkles, realistic shadows and reflections, iPhone-footage look, phone camera look not professional photography, no AI polish, no beauty smoothing, no blur anywhere, everything in sharp focus including background walls furniture and details.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no studio, no plastic skin, no extra fingers, no supernatural lighting, no blur, no artificial lighting, no warm orange color cast, no yellow tint, no golden glow, no change of identity, no change of wardrobe, no de-aging, no skin smoothing"
}
```

## CICLO 4 · ÂNCORA LYNN PARKER + REF-LIVRO

## K06 · T6 a T10 · O BLOCO DE FALA DO LYNN · GERAR DO ZERO · ÂNCORA LYNN + REF-LIVRO

> ### 📎 ANEXAR: **2 IMAGENS**
> **1️⃣ ÂNCORA LYNN** `producao/_ancoras/lynn_parker_ancora.jpeg`
> **2️⃣ REF-LIVRO** já aprovada
>
> ### 🆕 GERAR DO ZERO

Talking head no banquinho, as duas mãos nos joelhos em primeiro plano e o livro fechado no colo. Este keyframe sustenta cinco takes.

```json
{
  "shot_id": "K06_lynn_stool_block_initial",
  "reference_use": "Use the first attached image ONLY for Lynn's exact face, identity, white locs, white beard, skin texture, wardrobe and the identity of his real home apothecary room. Preserve that same real environment and its established objects. Use the second attached image ONLY as the exact physical BODY HACKS FOR MEN book prop. Do NOT copy pose, action or framing from either reference.",
  "identity_main": "The EXACT man from the first attached reference image: a Black American man of about seventy with medium brown skin, LONG SILVER WHITE LOCS tied back behind the shoulders with two or three locs falling in front of the right shoulder, white hair on top with a high hairline, a FULL WHITE BEARD and white moustache neatly trimmed, a long dignified face with a high forehead, defined cheekbones, visible moles, grey eyebrows, dark brown eyes and a calm certain look. Upright firm posture, square shoulders. Real skin texture with deep lines, heavy crow's feet and loose skin at the neck. His age is the asset and must be fully preserved.",
  "second_person": "On the far left edge, cut by the frame, only the shoulder and forearm of another man standing in front of him. His face is not in frame.",
  "prop": "The exact physical BODY HACKS FOR MEN book from the second reference, a thick matte paperback, resting closed and flat on his lap under his hands, its front cover facing up and fully readable.",
  "wardrobe": "The same WHITE linen mandarin collar tunic with an asymmetric white button closure falling below the hip, and dark trousers, from the anchor image. No jewelry at all and no cross.",
  "scene": "The SAME real home apothecary identity as Lynn's anchor image. He sits on a round wooden stool. Shelf group behind him: a floor to ceiling light wood shelving unit packed with labelled glass jars of dried herbs and dark amber glass bottles with white labels. Left shelf group: a grey stone mortar and pestle, a row of green and brown spined books, and a SMALL UNITED STATES FLAG on a desk stand, discreet and in sharp focus. A printed anatomical meridian chart hangs on the left wall. A window with blinds on the right shows an ordinary American residential street with houses, lawn, a parked car and bare trees. Labels on the jars and the chart read as printed labels, and no specific wording is required on any of them. Preserve the established room and do not invent a different location.",
  "posture": "Lynn sits upright on the round wooden stool, both large hands resting flat on his knees over the closed book, shoulders square, looking straight into the lens, calm and quietly certain.",
  "composition": "Medium talking frame. His hands on his knees and the closed book on his lap fill the lower foreground and are closer to the lens than his face. Lynn is chest-up in the upper portion of the frame. The jar shelves stay recognizable without competing.",
  "camera": "chest height, straight-on, close phone-camera distance",
  "state": "Start frame: Lynn is already seated with his hands on his knees and looking into the lens, before speaking or gesturing.",
  "lighting": "Soft neutral diffuse daylight of an overcast day coming from the blinded window on the right, flat and even, no warm cast and no practical lamp lighting the room.",
  "realism": "UGC realism, real skin texture with visible pores, individual hair strands, subtle wrinkles, realistic shadows and reflections, iPhone-footage look, phone camera look not professional photography, no AI polish, no beauty smoothing, no blur anywhere, everything in sharp focus including background walls furniture and details.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no studio, no plastic skin, no extra fingers, no supernatural lighting, no blur, no artificial lighting, no warm orange color cast, no yellow tint, no golden glow, no change of identity, no change of wardrobe, no de-aging, no skin smoothing"
}
```

## K12 · T12 · O LIVRO ERGUIDO · GERAR DO ZERO · ÂNCORA LYNN + REF-LIVRO

> ### 📎 ANEXAR: **2 IMAGENS**
> **1️⃣ ÂNCORA LYNN** `producao/_ancoras/lynn_parker_ancora.jpeg`
> **2️⃣ REF-LIVRO** já aprovada
>
> ### 🆕 GERAR DO ZERO

O livro erguido na mão direita dele em primeiro plano, capa quadrada para a lente.

```json
{
  "shot_id": "K12_lynn_book_raised_initial",
  "reference_use": "Use the first attached image ONLY for Lynn's exact face, identity, white locs, white beard, skin texture, wardrobe and the identity of his real home apothecary room. Preserve that same real environment and its established objects. Use the second attached image ONLY as the exact physical BODY HACKS FOR MEN book prop. Do NOT copy pose, action or framing from either reference.",
  "identity_main": "The EXACT man from the first attached reference image: a Black American man of about seventy with medium brown skin, LONG SILVER WHITE LOCS tied back behind the shoulders with two or three locs falling in front of the right shoulder, white hair on top with a high hairline, a FULL WHITE BEARD and white moustache neatly trimmed, a long dignified face with a high forehead, defined cheekbones, visible moles, grey eyebrows, dark brown eyes and a calm certain look. Upright firm posture, square shoulders. Real skin texture with deep lines, heavy crow's feet and loose skin at the neck. His age is the asset and must be fully preserved.",
  "prop": "The exact physical BODY HACKS FOR MEN book from the second reference, a thick matte paperback, held up in his right hand in the lower foreground, closer to the lens than his face, the front cover square to the lens and fully readable.",
  "wardrobe": "The same WHITE linen mandarin collar tunic with an asymmetric white button closure falling below the hip, and dark trousers, from the anchor image. No jewelry at all and no cross.",
  "scene": "The SAME real home apothecary identity as Lynn's anchor image. He sits on a round wooden stool. Shelf group behind him: a floor to ceiling light wood shelving unit packed with labelled glass jars of dried herbs and dark amber glass bottles with white labels. Left shelf group: a grey stone mortar and pestle, a row of green and brown spined books, and a SMALL UNITED STATES FLAG on a desk stand, discreet and in sharp focus. A printed anatomical meridian chart hangs on the left wall. A window with blinds on the right shows an ordinary American residential street with houses, lawn, a parked car and bare trees. Labels on the jars and the chart read as printed labels, and no specific wording is required on any of them. Preserve the established room and do not invent a different location.",
  "posture": "Lynn sits upright on the stool and has just lifted the book off his lap with his right hand, holding it up steady, his left hand flat on his knee, looking straight into the lens.",
  "composition": "Tight chest-up talking frame. The raised book fills the lower foreground and is closer to the lens than his face. Lynn's face fills the upper third. Nothing else competes with the book.",
  "camera": "chest height, straight-on, close phone-camera distance",
  "state": "Start frame: the book is already raised and steady and he is looking into the lens, before speaking.",
  "lighting": "Soft neutral diffuse daylight of an overcast day coming from the blinded window on the right, flat and even, no warm cast and no practical lamp lighting the room.",
  "realism": "UGC realism, real skin texture with visible pores, individual hair strands, subtle wrinkles, realistic shadows and reflections, iPhone-footage look, phone camera look not professional photography, no AI polish, no beauty smoothing, no blur anywhere, everything in sharp focus including background walls furniture and details.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no studio, no plastic skin, no extra fingers, no supernatural lighting, no blur, no artificial lighting, no warm orange color cast, no yellow tint, no golden glow, no change of identity, no change of wardrobe, no de-aging, no skin smoothing"
}
```

## K13 · T13 · O CTA, O PLANO MAIS FECHADO · GERAR DO ZERO · ÂNCORA LYNN + REF-LIVRO

> ### 📎 ANEXAR: **2 IMAGENS**
> **1️⃣ ÂNCORA LYNN** `producao/_ancoras/lynn_parker_ancora.jpeg`
> **2️⃣ REF-LIVRO** já aprovada
>
> ### 🆕 GERAR DO ZERO

O plano mais fechado do vídeo. O livro na altura do peito e o indicador entrando pela borda de baixo.

```json
{
  "shot_id": "K13_lynn_cta_tightest_initial",
  "reference_use": "Use the first attached image ONLY for Lynn's exact face, identity, white locs, white beard, skin texture, wardrobe and the identity of his real home apothecary room. Preserve that same real environment and its established objects. Use the second attached image ONLY as the exact physical BODY HACKS FOR MEN book prop. Do NOT copy pose, action or framing from either reference.",
  "identity_main": "The EXACT man from the first attached reference image: a Black American man of about seventy with medium brown skin, LONG SILVER WHITE LOCS tied back behind the shoulders with two or three locs falling in front of the right shoulder, white hair on top with a high hairline, a FULL WHITE BEARD and white moustache neatly trimmed, a long dignified face with a high forehead, defined cheekbones, visible moles, grey eyebrows, dark brown eyes and a calm certain look. Upright firm posture, square shoulders. Real skin texture with deep lines, heavy crow's feet and loose skin at the neck. His age is the asset and must be fully preserved.",
  "prop": "The exact physical BODY HACKS FOR MEN book from the second reference held against his chest in his left hand, the front cover square to the lens and fully readable, at the very bottom of the frame. His free right index finger enters from the lower edge and points directly toward the lens.",
  "wardrobe": "The same WHITE linen mandarin collar tunic with an asymmetric white button closure falling below the hip, and dark trousers, from the anchor image. No jewelry at all and no cross.",
  "scene": "The SAME real home apothecary identity as Lynn's anchor image. He sits on a round wooden stool. Shelf group behind him: a floor to ceiling light wood shelving unit packed with labelled glass jars of dried herbs and dark amber glass bottles with white labels. Left shelf group: a grey stone mortar and pestle, a row of green and brown spined books, and a SMALL UNITED STATES FLAG on a desk stand, discreet and in sharp focus. A printed anatomical meridian chart hangs on the left wall. A window with blinds on the right shows an ordinary American residential street with houses, lawn, a parked car and bare trees. Labels on the jars and the chart read as printed labels, and no specific wording is required on any of them. Preserve the established room and do not invent a different location.",
  "posture": "Lynn leans in from the stool, holding the book at chest height in his left hand, his free right index finger pointing straight at the lens, expression urgent and certain.",
  "composition": "THE TIGHTEST FRAME OF THE WHOLE VIDEO. Only Lynn's face, the book and the pointing finger are dominant. The book is at the very bottom of the frame and closest to the lens. The room is barely in frame.",
  "camera": "chest height, straight-on, pushed in about twenty percent closer than the other apothecary setups",
  "state": "Start frame: the book is already at his chest and the finger is already pointing, before speaking.",
  "lighting": "Soft neutral diffuse daylight of an overcast day coming from the blinded window on the right, flat and even, no warm cast and no practical lamp lighting the room.",
  "realism": "UGC realism, real skin texture with visible pores, individual hair strands, subtle wrinkles, realistic shadows and reflections, iPhone-footage look, phone camera look not professional photography, no AI polish, no beauty smoothing, no blur anywhere, everything in sharp focus including background walls furniture and details.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no studio, no plastic skin, no extra fingers, no supernatural lighting, no blur, no artificial lighting, no warm orange color cast, no yellow tint, no golden glow, no change of identity, no change of wardrobe, no de-aging, no skin smoothing"
}
```

## BLOCO GLOBAL DE VÍDEO

Veo 3.1 Lite · Lower Priority · 8 segundos · 1 variação por `V__`. A imagem entra como **INITIAL FRAME**.
Cada `V__` parte do maior `K__` menor ou igual ao número dele.

| Clipe | Take | Keyframe | Tipo |
|---|---|---|---|
| V01 | T1 | K01 | TALKING |
| V02 | T2 | K02 | TALKING |
| V03 | T3 | K03 | TALKING |
| V04 | T4 | K04 | B-ROLL, voz-over de memória na edição |
| V05 | T5 | K04 | TALKING |
| V06 | T6 | K06 | TALKING |
| V07 | T7 | K06 | TALKING |
| V08 | T8 | K06 | TALKING |
| V09 | T9 | K06 | TALKING |
| V10 | T10 | K06 | TALKING |
| V11 | T11 | K11 | TALKING |
| V12 | T12 | K12 | TALKING |
| V13 | T13 | K13 | TALKING |

**Lotes fechados:** lote 1 de V01 a V07, lote 2 de V08 a V13.

### V01 · T1 · usa K01

```text
a pessoa em quadro (mulher negra americana de quarenta e quatro anos, cabelo liso na altura do ombro) fala em ingles com sotaque americano, voz autentica, dinamica, apaixonada e emocional, como se exigisse ser ouvida, a seguinte frase: "Keith? Oh my God, look at you. You have not aged a single day. Terrell, do not just stand there. Say something."

a pessoa diz todas as palavras corretamente, nao pula nenhuma palavra, e diz a ultima palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o video.

o que acontece no video: Keith entra em quadro de costas e para, e ela abre os dois bracos em direcao a ele no meio da frase, depois vira a cabeca para a esquerda na ultima frase. A pessoa age naturalmente, com movimentos rapidos e legiveis, mantendo o video engajante. Estilo TikTok nativo, UGC.

camera: fixa, leve push-in

som ambiente: quintal em tarde nublada, som leve de churrasqueira e conversa distante, sem musica, sem ruido de fundo
```

### V02 · T2 · usa K02

```text
a pessoa em quadro (homem negro americano de uns quarenta e sete anos, cabeca raspada e barba curta) fala em ingles com sotaque americano, voz autentica, dinamica, apaixonada e emocional, como se exigisse ser ouvida, a seguinte frase: "Terrell, my man. Still the same truck, same spot in the driveway. Some guys just never change a thing."

a pessoa diz todas as palavras corretamente, nao pula nenhuma palavra, e diz a ultima palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o video.

o que acontece no video: ele aperta o ombro do outro homem uma vez, olha para a picape na entrada e volta o olhar para a lente no fim da frase. A pessoa age naturalmente, com movimentos rapidos e legiveis, mantendo o video engajante. Estilo TikTok nativo, UGC.

camera: fixa

som ambiente: quintal em tarde nublada, som leve de conversa distante, sem musica, sem ruido de fundo
```

### V03 · T3 · usa K03

```text
a pessoa em quadro (homem negro americano de quarenta e sete anos, fade curto grisalho nas laterais e barba curta) fala em ingles com sotaque americano, voz autentica, dinamica, apaixonada e emocional, como se exigisse ser ouvida, a seguinte frase: "I lift four days a week. I cut the beer. And I am not here about my bloodwork, doc. I am here about me."

a pessoa diz todas as palavras corretamente, nao pula nenhuma palavra, e diz a ultima palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o video.

o que acontece no video: ele aperta mais os dois punhos no colo e levanta o olhar na segunda frase, sustentando ate o fim. A pessoa age naturalmente, com movimentos rapidos e legiveis, mantendo o video engajante. Estilo TikTok nativo, UGC.

camera: fixa, leve push-in

som ambiente: consultorio silencioso durante o dia, sem musica, sem ruido de fundo
```

### V04 · T4 · usa K04

```text
(sem fala no take: a fala T4 do roteiro entra como voz-over na edicao)

o que acontece no video: ele continua com as duas maos no volante, o maxilar solta um pouco, ele pisca uma vez devagar e baixa o olhar para o painel no fim. Ele nao fala em nenhum momento.

camera: fixa

som ambiente: dentro de uma picape parada, som abafado de estacionamento, sem musica
```

### V05 · T5 · usa K04

```text
a pessoa em quadro (homem negro americano de quarenta e sete anos, fade curto grisalho nas laterais e barba curta) fala em ingles com sotaque americano, voz autentica, dinamica, apaixonada e emocional, como se exigisse ser ouvida, a seguinte frase: "Forty seven years old, and a doctor just told me normal. My wife has not looked at me like that in two years."

a pessoa diz todas as palavras corretamente, nao pula nenhuma palavra, e diz a ultima palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o video.

o que acontece no video: ele aperta o volante uma vez com as duas maos, solta o ar pela boca e olha para a lente no fim da frase. A pessoa age naturalmente, com movimentos rapidos e legiveis, mantendo o video engajante. Estilo TikTok nativo, UGC.

camera: fixa, leve push-in

som ambiente: dentro de uma picape parada, som abafado de estacionamento, sem musica, sem ruido de fundo
```

### V06 · T6 · usa K06

```text
a pessoa em quadro (homem negro americano de uns setenta anos, locs brancas prateadas presas atras dos ombros e barba branca cheia) fala em ingles com sotaque americano, voz autentica, dinamica, apaixonada e emocional, como se exigisse ser ouvida, a seguinte frase: "You have been standing in my doorway for ten minutes, brother. Sit down, or go home."

a pessoa diz todas as palavras corretamente, nao pula nenhuma palavra, e diz a ultima palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o video.

o que acontece no video: ele levanta o olhar para a lente na primeira palavra e faz um gesto curto de cabeca apontando o banquinho no fim. A pessoa age naturalmente, com movimentos rapidos e legiveis, mantendo o video engajante. Estilo TikTok nativo, UGC.

camera: fixa

som ambiente: sala de apotecario durante o dia, som leve de rua distante, sem musica, sem ruido de fundo
```

### V07 · T7 · usa K06

```text
a pessoa em quadro (homem negro americano de uns setenta anos, locs brancas prateadas presas atras dos ombros e barba branca cheia) fala em ingles com sotaque americano, voz autentica, dinamica, apaixonada e emocional, como se exigisse ser ouvida, a seguinte frase: "Let me ask you one thing. When you wake up, is it already awake before you are? Or has that stopped?"

a pessoa diz todas as palavras corretamente, nao pula nenhuma palavra, e diz a ultima palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o video.

o que acontece no video: ele levanta um dedo uma vez e sustenta o olhar na lente ate o fim da frase, sem mexer mais as maos. A pessoa age naturalmente, com movimentos rapidos e legiveis, mantendo o video engajante. Estilo TikTok nativo, UGC.

camera: fixa, leve push-in

som ambiente: sala de apotecario durante o dia, som leve de rua distante, sem musica, sem ruido de fundo
```

### V08 · T8 · usa K06

```text
a pessoa em quadro (homem negro americano de uns setenta anos, locs brancas prateadas presas atras dos ombros e barba branca cheia) fala em ingles com sotaque americano, voz autentica, dinamica, apaixonada e emocional, como se exigisse ser ouvida, a seguinte frase: "Whatever you answered, that is a gauge, not the problem. The engine is sleep, load, and your waistline. In that order."

a pessoa diz todas as palavras corretamente, nao pula nenhuma palavra, e diz a ultima palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o video.

o que acontece no video: ele conta tres no ar com os dedos, um a cada palavra da lista, e bate a mao espalmada no joelho na ultima palavra. A pessoa age naturalmente, com movimentos rapidos e legiveis, mantendo o video engajante. Estilo TikTok nativo, UGC.

camera: fixa

som ambiente: sala de apotecario durante o dia, som seco da mao no joelho, sem musica, sem ruido de fundo
```

### V09 · T9 · usa K06

```text
a pessoa em quadro (homem negro americano de uns setenta anos, locs brancas prateadas presas atras dos ombros e barba branca cheia) fala em ingles com sotaque americano, voz autentica, dinamica, apaixonada e emocional, como se exigisse ser ouvida, a seguinte frase: "And it is not your age, brother. It is your playbook. At twenty five your body forgave everything. It stopped forgiving."

a pessoa diz todas as palavras corretamente, nao pula nenhuma palavra, e diz a ultima palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o video.

o que acontece no video: ele abre as duas maos sobre os joelhos, balanca a cabeca uma vez e sustenta o olhar na lente. A pessoa age naturalmente, com movimentos rapidos e legiveis, mantendo o video engajante. Estilo TikTok nativo, UGC.

camera: fixa

som ambiente: sala de apotecario durante o dia, som leve de rua distante, sem musica, sem ruido de fundo
```

### V10 · T10 · usa K06

```text
a pessoa em quadro (homem negro americano de uns setenta anos, locs brancas prateadas presas atras dos ombros e barba branca cheia) fala em ingles com sotaque americano, voz autentica, dinamica, apaixonada e emocional, como se exigisse ser ouvida, a seguinte frase: "Let me guess. Wired at eleven, dead by three. Your belt is one notch out from two years ago. And the mornings are empty."

a pessoa diz todas as palavras corretamente, nao pula nenhuma palavra, e diz a ultima palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o video.

o que acontece no video: ele levanta tres dedos, um a cada sintoma que diz, e para de mexer as maos por completo na ultima frase. A pessoa age naturalmente, com movimentos rapidos e legiveis, mantendo o video engajante. Estilo TikTok nativo, UGC.

camera: fixa, leve push-in

som ambiente: sala de apotecario durante o dia, som leve de rua distante, sem musica, sem ruido de fundo
```

### V11 · T11 · usa K11

```text
a pessoa em quadro (homem negro americano de quarenta e sete anos, fade curto grisalho nas laterais e barba curta) fala em ingles com sotaque americano, voz autentica, dinamica, apaixonada e emocional, como se exigisse ser ouvida, a seguinte frase: "How do you know that? You are seventy and you talk like it never left. So what changed it for you?"

a pessoa diz todas as palavras corretamente, nao pula nenhuma palavra, e diz a ultima palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o video.

o que acontece no video: ele apoia a mao na borda da prateleira e se inclina para frente, olha para baixo em direcao ao homem sentado e depois para a lente. A pessoa age naturalmente, com movimentos rapidos e legiveis, mantendo o video engajante. Estilo TikTok nativo, UGC.

camera: fixa

som ambiente: sala de apotecario durante o dia, som leve de rua distante, sem musica, sem ruido de fundo
```

### V12 · T12 · usa K12

```text
a pessoa em quadro (homem negro americano de uns setenta anos, locs brancas prateadas presas atras dos ombros e barba branca cheia) fala em ingles com sotaque americano, voz autentica, dinamica, apaixonada e emocional, como se exigisse ser ouvida, a seguinte frase: "This. Body Hacks for Men, forty two habit hacks. Six are only for fixing the drive and confidence part. Forty years, and nobody ever handed me that list."

a pessoa diz todas as palavras corretamente, nao pula nenhuma palavra, e diz a ultima palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o video.

o que acontece no video: ele levanta o livro do colo na primeira palavra, mantem a capa virada para a lente e nao abaixa o livro ate o fim do take. A pessoa age naturalmente, com movimentos rapidos e legiveis, mantendo o video engajante. Estilo TikTok nativo, UGC.

camera: fixa, leve push-in

som ambiente: sala de apotecario durante o dia, som leve do livro saindo do colo, sem musica, sem ruido de fundo
```

### V13 · T13 · usa K13

```text
a pessoa em quadro (homem negro americano de uns setenta anos, locs brancas prateadas presas atras dos ombros e barba branca cheia) fala em ingles com sotaque americano, voz autentica, dinamica, apaixonada e emocional, como se exigisse ser ouvida, a seguinte frase: "You can find pieces of this free online. You cannot find which one is yours. Nine ninety for all forty two. Comment yes and I send the link."

a pessoa diz todas as palavras corretamente, nao pula nenhuma palavra, e diz a ultima palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o video.

o que acontece no video: ele aponta o indicador para a lente na ultima frase e mantem o livro na altura do peito, terminando com o olhar fixo na camera. A pessoa age naturalmente, com movimentos rapidos e legiveis, mantendo o video engajante. Estilo TikTok nativo, UGC.

camera: fixa

som ambiente: sala de apotecario durante o dia, som leve de rua distante, sem musica, sem ruido de fundo
```

---

## MAPA DE ÂNCORAS

| Keyframe | Referências a anexar | Modelo |
|---|---|---|
| REF-NIA, REF-KEITH, REF-TERRELL, REF-LIVRO | nada | Nano Banana 2 |
| K01 | REF-NIA | Nano Banana 2 |
| K02 | REF-KEITH | Nano Banana 2 |
| K03, K04, K11 | REF-TERRELL | Nano Banana 2 |
| K06, K12, K13 | âncora do Lynn + REF-LIVRO | Nano Banana 2 |
| V01 a V13 | o `K__` correspondente como INITIAL FRAME | Veo 3.1 Lite |

## MONTAGEM NO CAPCUT

1. Ordem do roteiro, T1 a T13, sem reordenar.
2. O V04 é mudo. Entrar com a locução do médico como voz-over, gravada ou TTS, e legenda.
3. Legendas grandes estilo Prism Pro em todos os takes, incluindo o `yes` do V13.
4. Trilha entra só na edição. Nenhum clipe é gerado com música.
5. Export 9:16.

## GATES DE QUALIDADE

1. `python checar_entrega.py producao/dana_churrasco` com zero FALHAS.
2. `python checar_frases.py producao/dana_churrasco` sem frase queimada.
3. Os oito keyframes com bandeira dos EUA visível e em foco.
4. As locs brancas e a barba branca do Lynn intactas, e **zero rejuvenescimento**. A idade é o ativo dele.
5. O livro legível na capa no K12 e no K13.
6. O K13 visivelmente mais fechado que o K06 e o K12.
7. Nenhum rosto de segunda pessoa em quadro fora do ciclo da própria âncora.
8. O crivo do Ângulo 4 rodado: a copy não sugere que ele deixou isso acontecer.