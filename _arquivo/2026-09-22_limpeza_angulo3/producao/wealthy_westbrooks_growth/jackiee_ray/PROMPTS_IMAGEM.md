pipeline: auraly

# Jackiee Ray | wealthy_westbrooks_growth | Prompts de imagem (fonte interna, JSON)

**Anchor (fingerprint):** `/Users/macbookairm2/Desktop/AVATARES/avatares appyon/Jackiee Ray.jpeg`
**Ganchos travados para a fila inteira:** 1 (cofre estourado), 2 (jarro de moedas), 5 (mordida na moeda), 7 (pedra com ouro dentro), 8 (nota sob a cinza)
**Modelo:** Nano Banana 2, 9:16, uma imagem final por K, sem etapa de seleção.

## Índice de geração

| Keyframe | Setup | Ação de geração | Anexar |
|---|---|---|---|
| K01 | A · sala de estar, câmera de cima | 🆕 GERAR DO ZERO | 1 imagem: fingerprint Jackiee Ray |
| K02 | A · corpo (T2) | 🆕 GERAR DO ZERO | 1 imagem: fingerprint Jackiee Ray |
| K03 | A · CTA (T3) | ✏️ EDITAR do K02 (crop mais fechado, gesto de mão) | 1 imagem: K02 aprovado |
| K04 | B · varanda, câmera baixa | 🆕 GERAR DO ZERO | 1 imagem: fingerprint Jackiee Ray |
| K05 | B · corpo (T2) | 🆕 GERAR DO ZERO | 1 imagem: fingerprint Jackiee Ray |
| K06 | B · CTA (T3) | ✏️ EDITAR do K05 | 1 imagem: K05 aprovado |
| K07 | C · escritório, dutch tilt | 🆕 GERAR DO ZERO | 1 imagem: fingerprint Jackiee Ray |
| K08 | C · corpo (T2) | 🆕 GERAR DO ZERO | 1 imagem: fingerprint Jackiee Ray |
| K09 | C · CTA (T3) | ✏️ EDITAR do K08 | 1 imagem: K08 aprovado |
| K10 | D · quintal, câmera alta diagonal | 🆕 GERAR DO ZERO | 1 imagem: fingerprint Jackiee Ray |
| K11 | D · corpo (T2) | 🆕 GERAR DO ZERO | 1 imagem: fingerprint Jackiee Ray |
| K12 | D · CTA (T3) | ✏️ EDITAR do K11 | 1 imagem: K11 aprovado |
| K13 | E · sunroom, câmera deitada na mesa | 🆕 GERAR DO ZERO | 1 imagem: fingerprint Jackiee Ray |
| K14 | E · corpo (T2) | 🆕 GERAR DO ZERO | 1 imagem: fingerprint Jackiee Ray |
| K15 | E · CTA (T3) | ✏️ EDITAR do K14 | 1 imagem: K14 aprovado |

Regra de bolso: GERAR DO ZERO anexa a fingerprint; EDITAR anexa só o keyframe de origem (nunca a fingerprint junto).

## Trava de identidade (reaproveitada em todo K)

```
identity_main: "The EXACT man from the attached fingerprint reference (Jackiee Ray): a Black American in his mid-to-late 30s, dark-brown skin, shoulder-length black dreadlocks with bleached blonde tips worn loose, a full dark beard, and a lean athletic build."
reference_use: "Use the attached fingerprint ONLY for face, identity, body type and skin. Do NOT copy pose, wardrobe, background or lighting from it — those are defined per scenario below."
realism: "UGC realism, real skin texture with visible pores, individual hair strands, subtle wrinkles, realistic shadows and reflections, iPhone-footage look, phone camera look not professional photography, no AI polish, no beauty smoothing, no blur anywhere, everything in sharp focus including background walls furniture and details."
negative_base: "no captions, no subtitles, no words overlaid on the image, no studio, no plastic skin, no extra fingers, no supernatural lighting, no blur, no artificial lighting, no warm orange color cast, no yellow tint"
aspect_ratio: "9:16 vertical"
```

## SETUP A — HOOK 1, Cofre estourado (sala de estar, câmera de cima)

### K01 · HOOK (T1) · 🆕 GERAR DO ZERO · ÂNCORA: fingerprint Jackiee Ray
> 📎 ANEXAR: **1 IMAGEM** — fingerprint Jackiee Ray

```json
{
  "shot_id": "JR_A_K01_hook_piggybank",
  "wardrobe": "Unbuttoned olive-green linen shirt open over a plain white tank top, black pants, thin dark cord necklace with a small pendant.",
  "scene": "Small round wooden table in the corner of his real living room. Light wall behind him: small dark wooden cross, framed astrological wheel chart (no readable words). Low shelf beside table: tarot deck, cluster of clear quartz crystals, lit white pillar candle, thin lit incense stick with faint smoke, small American flag standing in a glass jar. All visible and sharp.",
  "composition": "Lower foreground, much closer to lens than his face: intact gold-painted ceramic piggy-bank money box, no cracks. Right hand grips small gold-toned toy hammer raised just above it, instant before striking. Left hand flat on table edge.",
  "posture": "Leans slightly toward lens, urgent focused eye contact, lips slightly parted as if speaking.",
  "camera": "Phone held directly overhead, pointed straight down at the table — top-down bird's-eye angle.",
  "lighting": "Soft neutral overcast daylight.",
  "state": "Start frame: hammer raised, piggy bank intact, before impact.",
  "negative": "no cracks yet, no glow visible yet, no second person"
}
```

### K02 · CORPO (T2) · 🆕 GERAR DO ZERO · ÂNCORA: fingerprint Jackiee Ray
> 📎 ANEXAR: **1 IMAGEM** — fingerprint Jackiee Ray

```json
{
  "shot_id": "JR_A_K02_body",
  "wardrobe": "Same as K01.",
  "scene": "Same living room table setup as K01, unchanged.",
  "composition": "Tight chest-up talking head. Both hands open, gesturing naturally at chest height as if counting off points.",
  "posture": "Shoulders relaxed, chin slightly lifted, looking directly into lens with calm certainty, lips slightly parted mid-word.",
  "camera": "Same top-down bird's-eye angle as K01.",
  "lighting": "Soft neutral overcast daylight.",
  "state": "Start frame: mid-sentence, speaking directly to camera.",
  "negative": "no second person"
}
```

### K03 · CTA (T3) · ✏️ EDITAR do K02 (crop mais fechado, gesto de mão levantada)
> 📎 ANEXAR: **1 IMAGEM** — K02 já aprovado
> 🚫 NUNCA anexar a fingerprint aqui, só o K02.

```json
{
  "task": "edit the attached K02 image, keep everything identical except the changes listed",
  "keep_identical": "Keep the man exactly the same: same face, same hair, same wardrobe, same background elements, same lighting, same camera angle family (top-down).",
  "change_1": "Push in tighter — the tightest shot of the whole video, shoulders-up and very close.",
  "change_2": "Right hand raised open beside his face at shoulder height, palm facing the lens. Left hand rests just out of frame at chest height. Expression: warm, direct sincerity, leaning slightly toward the lens.",
  "negative": "do not change the face, do not change identity, do not change wardrobe, no captions, no second person"
}
```

## SETUP B — HOOK 2, Jarro de moedas (varanda coberta, câmera baixa worm's-eye)

### K04 · HOOK (T1) · 🆕 GERAR DO ZERO · ÂNCORA: fingerprint Jackiee Ray
> 📎 ANEXAR: **1 IMAGEM** — fingerprint Jackiee Ray

```json
{
  "shot_id": "JR_B_K04_hook_coinjar",
  "wardrobe": "Unbuttoned rust-terracotta linen shirt open over a plain white tank top, black pants, thin dark cord necklace with a small pendant.",
  "scene": "Small wicker table on his real covered back porch. String lights along a wooden beam behind him. Wall-mounted dark wooden cross beside framed astrological wheel chart (no readable words). Side shelf: tarot deck, lit white pillar candle, small cluster of clear quartz crystals, thin lit incense stick with faint smoke, small American flag standing in a glass jar. All visible and sharp.",
  "composition": "Lower foreground, much closer to lens than his face: clear glass jar completely full of assorted gold and silver coins, held upside down at chest height, tilted just barely past vertical, instant before coins begin to fall. Other hand steadies the base.",
  "posture": "Leans slightly toward lens, urgent focused eye contact, lips slightly parted as if speaking.",
  "camera": "Phone propped low at the table's edge, tilted up at him — extreme low worm's-eye angle.",
  "lighting": "Soft neutral overcast daylight.",
  "state": "Start frame: jar tilted, coins still inside, before they fall.",
  "negative": "no coins falling yet, no second person"
}
```

### K05 · CORPO (T2) · 🆕 GERAR DO ZERO · ÂNCORA: fingerprint Jackiee Ray
> 📎 ANEXAR: **1 IMAGEM** — fingerprint Jackiee Ray

```json
{
  "shot_id": "JR_B_K05_body",
  "wardrobe": "Same as K04.",
  "scene": "Same porch table setup as K04, unchanged.",
  "composition": "Tight chest-up talking head. Both hands open, gesturing naturally at chest height.",
  "posture": "Shoulders relaxed, chin slightly lifted, looking directly into lens with calm certainty, lips slightly parted mid-word.",
  "camera": "Same low worm's-eye angle as K04.",
  "lighting": "Soft neutral overcast daylight.",
  "state": "Start frame: mid-sentence, speaking directly to camera.",
  "negative": "no second person"
}
```

### K06 · CTA (T3) · ✏️ EDITAR do K05
> 📎 ANEXAR: **1 IMAGEM** — K05 já aprovado
> 🚫 NUNCA anexar a fingerprint aqui, só o K05.

```json
{
  "task": "edit the attached K05 image, keep everything identical except the changes listed",
  "keep_identical": "Keep the man exactly the same: same face, same hair, same wardrobe, same background elements, same lighting, same camera angle family (low worm's-eye).",
  "change_1": "Push in tighter — the tightest shot of the whole video, shoulders-up and very close.",
  "change_2": "Right hand raised open beside his face at shoulder height, palm facing the lens. Left hand rests just out of frame. Expression: warm, direct sincerity.",
  "negative": "do not change the face, do not change identity, do not change wardrobe, no captions, no second person"
}
```

## SETUP C — HOOK 5, Mordida na moeda (escritório, dutch tilt três-quartos)

### K07 · HOOK (T1) · 🆕 GERAR DO ZERO · ÂNCORA: fingerprint Jackiee Ray
> 📎 ANEXAR: **1 IMAGEM** — fingerprint Jackiee Ray

```json
{
  "shot_id": "JR_C_K07_hook_bitecoin",
  "wardrobe": "Dark olive henley shirt, sleeves pushed up to the forearms, black pants, thin dark cord necklace with a small pendant.",
  "scene": "Wooden desk in the corner of his real home office. Low wooden bookshelf behind him with old books, small dark wooden cross mounted above it beside framed astrological wheel chart (no readable words). Desk: tarot deck, lit white pillar candle, small cluster of clear quartz crystals, thin lit incense stick with faint smoke, small American flag standing in a glass jar on the shelf. All visible and sharp.",
  "composition": "Lower foreground, much closer to lens than his face: one large antique gold coin engraved with a stylized sun symbol, raised sideways between his back teeth, biting down on its edge, lips parted around it. Other hand rests on the desk.",
  "posture": "Eyes locked on the lens the whole time.",
  "camera": "Three-quarter angle with a pronounced Dutch tilt, close to the desk.",
  "lighting": "Soft neutral overcast daylight.",
  "state": "Start frame: coin bitten, teeth pressing, before any bending or damage.",
  "negative": "no second person"
}
```

### K08 · CORPO (T2) · 🆕 GERAR DO ZERO · ÂNCORA: fingerprint Jackiee Ray
> 📎 ANEXAR: **1 IMAGEM** — fingerprint Jackiee Ray

```json
{
  "shot_id": "JR_C_K08_body",
  "wardrobe": "Same as K07.",
  "scene": "Same office desk setup as K07, unchanged.",
  "composition": "Tight chest-up talking head. Both hands open, gesturing naturally at chest height.",
  "posture": "Shoulders relaxed, chin slightly lifted, looking directly into lens with calm certainty, lips slightly parted mid-word.",
  "camera": "Same three-quarter Dutch tilt as K07.",
  "lighting": "Soft neutral overcast daylight.",
  "state": "Start frame: mid-sentence, speaking directly to camera.",
  "negative": "no second person"
}
```

### K09 · CTA (T3) · ✏️ EDITAR do K08
> 📎 ANEXAR: **1 IMAGEM** — K08 já aprovado
> 🚫 NUNCA anexar a fingerprint aqui, só o K08.

```json
{
  "task": "edit the attached K08 image, keep everything identical except the changes listed",
  "keep_identical": "Keep the man exactly the same: same face, same hair, same wardrobe, same background elements, same lighting, same camera angle family (Dutch tilt three-quarter).",
  "change_1": "Push in tighter — the tightest shot of the whole video, shoulders-up and very close.",
  "change_2": "Right hand raised open beside his face at shoulder height, palm facing the lens. Left hand rests just out of frame. Expression: warm, direct sincerity.",
  "negative": "do not change the face, do not change identity, do not change wardrobe, no captions, no second person"
}
```

## SETUP D — HOOK 7, Pedra com ouro dentro (quintal, câmera alta diagonal)

### K10 · HOOK (T1) · 🆕 GERAR DO ZERO · ÂNCORA: fingerprint Jackiee Ray
> 📎 ANEXAR: **1 IMAGEM** — fingerprint Jackiee Ray

```json
{
  "shot_id": "JR_D_K10_hook_stone",
  "wardrobe": "Unbuttoned sand-beige linen shirt open over a plain white tank top, black pants, thin dark cord necklace with a small pendant.",
  "scene": "Small metal patio table in the corner of his real backyard. Wooden fence and leafy plant behind him. Small dark wooden cross and framed astrological wheel chart (no readable words) propped on a nearby outdoor shelf. Table: tarot deck, lit white pillar candle, small cluster of clear quartz crystals, thin lit incense stick with faint smoke, small American flag standing in a glass jar. All visible and sharp.",
  "composition": "Lower foreground, much closer to lens than his face: smooth fist-sized grey stone held in both hands, intact with no cracks, positioned as if about to strike it against the metal table edge to split it open.",
  "posture": "Leans slightly toward lens, urgent focused eye contact, lips slightly parted as if speaking.",
  "camera": "Held high in the corner of the space, angled down diagonally at him.",
  "lighting": "Soft neutral overcast daylight.",
  "state": "Start frame: stone intact, positioned to strike, before any impact.",
  "negative": "no cracks yet, no gold visible yet, no second person"
}
```

### K11 · CORPO (T2) · 🆕 GERAR DO ZERO · ÂNCORA: fingerprint Jackiee Ray
> 📎 ANEXAR: **1 IMAGEM** — fingerprint Jackiee Ray

```json
{
  "shot_id": "JR_D_K11_body",
  "wardrobe": "Same as K10.",
  "scene": "Same backyard patio setup as K10, unchanged.",
  "composition": "Tight chest-up talking head. Both hands open, gesturing naturally at chest height.",
  "posture": "Shoulders relaxed, chin slightly lifted, looking directly into lens with calm certainty, lips slightly parted mid-word.",
  "camera": "Same high diagonal angle as K10.",
  "lighting": "Soft neutral overcast daylight.",
  "state": "Start frame: mid-sentence, speaking directly to camera.",
  "negative": "no second person"
}
```

### K12 · CTA (T3) · ✏️ EDITAR do K11
> 📎 ANEXAR: **1 IMAGEM** — K11 já aprovado
> 🚫 NUNCA anexar a fingerprint aqui, só o K11.

```json
{
  "task": "edit the attached K11 image, keep everything identical except the changes listed",
  "keep_identical": "Keep the man exactly the same: same face, same hair, same wardrobe, same background elements, same lighting, same camera angle family (high diagonal).",
  "change_1": "Push in tighter — the tightest shot of the whole video, shoulders-up and very close.",
  "change_2": "Right hand raised open beside his face at shoulder height, palm facing the lens. Left hand rests just out of frame. Expression: warm, direct sincerity.",
  "negative": "do not change the face, do not change identity, do not change wardrobe, no captions, no second person"
}
```

## SETUP E — HOOK 8, Nota sob a cinza (sunroom, câmera deitada na mesa)

### K13 · HOOK (T1) · 🆕 GERAR DO ZERO · ÂNCORA: fingerprint Jackiee Ray
> 📎 ANEXAR: **1 IMAGEM** — fingerprint Jackiee Ray

```json
{
  "shot_id": "JR_E_K13_hook_ash",
  "wardrobe": "Unbuttoned deep-green linen shirt open over a plain white tank top, black pants, thin dark cord necklace with a small pendant.",
  "scene": "Glass-topped table in his real sunroom. Tall windows behind him showing leafy plants and a pale cloudy sky. Small dark wooden cross mounted on the wall beside framed astrological wheel chart (no readable words). Table: tarot deck, lit white pillar candle, small cluster of clear quartz crystals, thin lit incense stick with faint smoke, small American flag standing in a glass jar. All visible and sharp.",
  "composition": "Lower foreground, much closer to lens than his face: small ceramic bowl holding a smooth, undisturbed mound of pale grey cold ash about three centimeters deep. Hands resting on the table edge on either side of the bowl.",
  "posture": "Leans in, lips pursed, a fraction of a second before blowing across the ash.",
  "camera": "Phone lying almost flat on the tabletop, tilted up at him — extreme low angle.",
  "lighting": "Soft neutral overcast daylight through the windows.",
  "state": "Start frame: ash undisturbed, before the blow.",
  "negative": "no ash disturbed yet, no bill visible yet, no second person"
}
```

### K14 · CORPO (T2) · 🆕 GERAR DO ZERO · ÂNCORA: fingerprint Jackiee Ray
> 📎 ANEXAR: **1 IMAGEM** — fingerprint Jackiee Ray

```json
{
  "shot_id": "JR_E_K14_body",
  "wardrobe": "Same as K13.",
  "scene": "Same sunroom table setup as K13, unchanged.",
  "composition": "Tight chest-up talking head. Both hands open, gesturing naturally at chest height.",
  "posture": "Shoulders relaxed, chin slightly lifted, looking directly into lens with calm certainty, lips slightly parted mid-word.",
  "camera": "Same low flat angle as K13.",
  "lighting": "Soft neutral overcast daylight through the windows.",
  "state": "Start frame: mid-sentence, speaking directly to camera.",
  "negative": "no second person"
}
```

### K15 · CTA (T3) · ✏️ EDITAR do K14
> 📎 ANEXAR: **1 IMAGEM** — K14 já aprovado
> 🚫 NUNCA anexar a fingerprint aqui, só o K14.

```json
{
  "task": "edit the attached K14 image, keep everything identical except the changes listed",
  "keep_identical": "Keep the man exactly the same: same face, same hair, same wardrobe, same background elements, same lighting, same camera angle family (low flat angle).",
  "change_1": "Push in tighter — the tightest shot of the whole video, shoulders-up and very close.",
  "change_2": "Right hand raised open beside his face at shoulder height, palm facing the lens. Left hand rests just out of frame. Expression: warm, direct sincerity.",
  "negative": "do not change the face, do not change identity, do not change wardrobe, no captions, no second person"
}
```
