# Lynn Parker | Ângulo 2 (FityWell) | Pacote de Prompts

Vídeo modelo: `8bd57dab-62d3-452a-8809-4b5eb72834d5.mp4` (27,97 s, 6 takes)

Âncora de identidade: `producao/_ancoras/lynn_parker_ancora.jpeg`

Funil: comment `yes` -> DM -> link do quiz FityWell

Avatar 3 de 3 da fila. Os pacotes fechados estão em `PROMPTS_DANA_MORRISON.md` e `PROMPTS_JAMIE_ANDERSON.md`.

---

## Índice de geração

| Take | Keyframe | Anexar | Ação de geração |
|---|---|---|---|
| T1 | K01 | ÂNCORA LYNN PARKER | GERAR DO ZERO. Gancho vinte e cinco contra cinquenta e cinco |
| T9 | K02 | ÂNCORA LYNN PARKER | GERAR DO ZERO. Gancho da barriga |
| T10 | K03 | ÂNCORA LYNN PARKER | GERAR DO ZERO. Gancho do intestino |
| T11 | K04 | ÂNCORA LYNN PARKER | GERAR DO ZERO. Gancho do refrigerante |
| T12 | K05 | ÂNCORA LYNN PARKER | GERAR DO ZERO. Gancho do açúcar |
| T2 | K06 | ÂNCORA LYNN PARKER | GERAR DO ZERO. Copo de água limpa |
| T3 | K07 | o K06 aprovado | EDITAR do K06. Muda só o estado do copo e o limão |
| T4 | K08 | o K06 aprovado | EDITAR do K06. Muda só o líquido e as mãos |
| T5 | K09 | ÂNCORA LYNN PARKER | GERAR DO ZERO. Close de CTA, sem prop |
| T6 | K10 | o K09 aprovado | EDITAR do K09. Muda só o gesto de mão |
| T7 | K11 | o K09 aprovado | EDITAR do K09. Muda só o gesto de mão |
| T8 | K12 | o K09 aprovado | EDITAR do K09. Muda só o braço direito, apontando |

Regra de bolso: **GERAR DO ZERO anexa a âncora. EDITAR anexa uma imagem só, o keyframe de origem.**
🚫 Nunca anexar um keyframe editado como origem de outro.

---

## Trava de identidade e continuidade

- Homem negro americano por volta dos setenta, pele marrom média, porte ereto e firme.
- **Locs brancas prateadas compridas**, presas atrás dos ombros, com duas ou três mechas caindo na frente do ombro direito. Cabelo branco no topo, entradas altas.
- **Barba branca cheia e bigode branco**, aparados com capricho. Rosto longo e digno, testa alta, pintas visíveis, sobrancelhas grisalhas.
- **Túnica de linho BRANCA de gola mandarim**, fechamento assimétrico com botões brancos, comprida até abaixo do quadril. Calça escura.
- **ZERO joia, sem cruz.**
- **A idade é o ativo dele.** `no de-aging` e `no skin smoothing` obrigatórios em todo negative.
- Cenário: apotecário dentro de casa, estante de madeira clara com potes de vidro rotulados e frascos âmbar, pilão de pedra, **bandeirinha dos EUA em suporte de mesa**, gráfico impresso na parede, janela à direita com persiana mostrando uma rua residencial americana.
- **Mesa de madeira escura no primeiro plano**, que é a única coisa fora da âncora e é a gramática do próprio vídeo modelo.
- Luz neutra de dia nublado vindo da janela. Zero blur, tudo em foco nítido.

---

## Trava do prop herói

```text
Soft matte silicone teaching models molded in muted cream, smooth shapes with no face and no fine
detail, resting flat on the dark wooden table in the lower foreground, closer to the lens than the
man's face. Where a model is covered, the covering is a THICK, HEAPED, three-dimensional mound of
small round pale yellow beads, piled high with real volume so that almost none of the cream surface
shows. Never a thin scattered layer and never a flat sauce-like coating.
```

**A forma vai descrita no positivo, nunca negada.** Nome de órgão no `negative` injeta o conceito.

## Trava da 2ª pessoa (REF-A)

**Não se aplica.** Não há segunda pessoa em nenhum take.

---

# Prompts de imagem

## K01 · T1 · HOOK A · GERAR DO ZERO · ÂNCORA LYNN PARKER

> ### 📎 ANEXAR: **1 IMAGEM**
> **1️⃣ ÂNCORA LYNN PARKER** `producao/_ancoras/lynn_parker_ancora.jpeg`
>
> ### 🆕 GERAR DO ZERO

```json
{
  "shot_id": "K01_hook_25_vs_55",
  "reference_use": "Use the attached image ONLY for Lynn Parker's face, identity, hair, wardrobe and his home apothecary room. Do NOT copy its pose or framing.",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "identity_main": "The EXACT man from the attached reference image (Lynn Parker): Black American man around seventy, medium brown skin, long silver white locs tied back behind his shoulders with two or three strands falling in front of his right shoulder, white hair on top with a high hairline, a full white beard and white moustache neatly trimmed, a long dignified face with a high forehead, visible moles, grey eyebrows and calm dark brown eyes, upright and steady posture, deep lines and heavy crow's feet.",
  "wardrobe": "A white linen mandarin collar tunic with an asymmetric front closure and white buttons, falling below the hip, and dark trousers. No jewelry of any kind.",
  "prop": "Two soft matte silicone teaching models shaped like human legs, smooth tapered forms in muted cream with no face and no fine detail, lying flat side by side on the dark wooden table. The one on the left carries only a thin sparse scatter of small round pale yellow beads. The one on the right is covered by a THICK, HEAPED, three-dimensional mound of the same small round pale yellow beads, piled high with real volume so that almost none of the cream surface shows. In his right hand he holds a plain unlabeled clear glass jar of white powder, tilted just above the two models.",
  "scene": "SAME home apothecary room as the reference image: a light wood shelf of labelled glass jars and dark amber bottles behind him, a small American flag on a table stand on that shelf, discreet but clearly visible and in sharp focus, and a window with blinds to the right showing an ordinary American residential street. A dark wooden table sits in front of him.",
  "posture": "Seated on his round wooden stool at the dark wooden table, leaning slightly forward toward the camera.",
  "composition": "The two models fill the lower two thirds of the frame and sit much closer to the lens than his face, so they are unmistakably the hero. His head and shoulders occupy the upper third and the top of his head is cropped by the top edge. Nothing else competes.",
  "camera": "chest level, straight-on, camera pushed in close and slightly high toward the two models",
  "state": "Start frame: the jar is tilted above the models and the first grains of white powder are about to fall. Nothing has reacted yet.",
  "lighting": "Flat neutral daylight from the window under an overcast sky, evenly lighting his face, no warm orange cast and no yellow tint.",
  "realism": "UGC realism, real skin texture with visible pores, individual hair strands, subtle wrinkles, realistic shadows and reflections, iPhone-footage look, phone camera look not professional photography, no AI polish, no beauty smoothing, no blur anywhere, everything in sharp focus including the shelf and the window.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no studio, no plastic skin, no extra fingers, no supernatural lighting, no blur, no artificial lighting, no warm orange color cast, no yellow tint, no de-aging, no skin smoothing, no thin scattered layer, no flat sauce-like coating, no jewelry, no second person, no foam"
}
```

## K02 · T9 · HOOK B · GERAR DO ZERO · ÂNCORA LYNN PARKER

> ### 📎 ANEXAR: **1 IMAGEM**
> **1️⃣ ÂNCORA LYNN PARKER** `producao/_ancoras/lynn_parker_ancora.jpeg`
>
> ### 🆕 GERAR DO ZERO

```json
{
  "shot_id": "K02_hook_belly",
  "reference_use": "Use the attached image ONLY for Lynn Parker's face, identity, hair, wardrobe and his home apothecary room. Do NOT copy its pose or framing.",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "identity_main": "The EXACT man from the attached reference image (Lynn Parker): Black American man around seventy, medium brown skin, long silver white locs tied back behind his shoulders with two or three strands falling in front of his right shoulder, white hair on top with a high hairline, a full white beard and white moustache neatly trimmed, a long dignified face with a high forehead, visible moles, grey eyebrows and calm dark brown eyes, upright and steady posture, deep lines and heavy crow's feet.",
  "wardrobe": "A white linen mandarin collar tunic with an asymmetric front closure and white buttons, falling below the hip, and dark trousers. No jewelry of any kind.",
  "prop": "One soft matte silicone teaching model of a torso panel, a smooth oval dome about the size of a dinner tray, molded in muted cream with no face and no fine detail, resting flat on the dark wooden table. Its whole upper surface is covered by a THICK, HEAPED, three-dimensional mound of small round pale yellow beads, piled high with real volume so that almost none of the cream surface shows. In his right hand he holds a plain unlabeled clear glass jar of white powder, tilted just above it.",
  "scene": "SAME home apothecary room as the reference image: a light wood shelf of labelled glass jars and dark amber bottles behind him, a small American flag on a table stand on that shelf, discreet but clearly visible and in sharp focus, and a window with blinds to the right showing an ordinary American residential street. A dark wooden table sits in front of him.",
  "posture": "Seated on his round wooden stool at the dark wooden table, leaning slightly forward toward the camera.",
  "composition": "The model fills the lower two thirds of the frame and sits much closer to the lens than his face, so it is unmistakably the hero. His head and shoulders occupy the upper third and the top of his head is cropped by the top edge. Nothing else competes.",
  "camera": "chest level, straight-on, camera pushed in close and slightly high toward the model",
  "state": "Start frame: the jar is tilted above the model and the first grains of white powder are about to fall. Nothing has reacted yet.",
  "lighting": "Flat neutral daylight from the window under an overcast sky, evenly lighting his face, no warm orange cast and no yellow tint.",
  "realism": "UGC realism, real skin texture with visible pores, individual hair strands, subtle wrinkles, realistic shadows and reflections, iPhone-footage look, phone camera look not professional photography, no AI polish, no beauty smoothing, no blur anywhere, everything in sharp focus including the shelf and the window.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no studio, no plastic skin, no extra fingers, no supernatural lighting, no blur, no artificial lighting, no warm orange color cast, no yellow tint, no de-aging, no skin smoothing, no thin scattered layer, no flat sauce-like coating, no jewelry, no second person, no foam"
}
```

## K03 · T10 · HOOK C · GERAR DO ZERO · ÂNCORA LYNN PARKER

> ### 📎 ANEXAR: **1 IMAGEM**
> **1️⃣ ÂNCORA LYNN PARKER** `producao/_ancoras/lynn_parker_ancora.jpeg`
>
> ### 🆕 GERAR DO ZERO

```json
{
  "shot_id": "K03_hook_gut",
  "reference_use": "Use the attached image ONLY for Lynn Parker's face, identity, hair, wardrobe and his home apothecary room. Do NOT copy its pose or framing.",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "identity_main": "The EXACT man from the attached reference image (Lynn Parker): Black American man around seventy, medium brown skin, long silver white locs tied back behind his shoulders with two or three strands falling in front of his right shoulder, white hair on top with a high hairline, a full white beard and white moustache neatly trimmed, a long dignified face with a high forehead, visible moles, grey eyebrows and calm dark brown eyes, upright and steady posture, deep lines and heavy crow's feet.",
  "wardrobe": "A white linen mandarin collar tunic with an asymmetric front closure and white buttons, falling below the hip, and dark trousers. No jewelry of any kind.",
  "prop": "One soft matte silicone teaching model of a digestive tube, a pale dusty rose tube folded back and forth on itself in wide loops on a flat white base, resting on the dark wooden table. The whole surface of the coiled tube is caked under a THICK, HEAPED layer of dried crust, cracked like dried clay in a warm brown tone, piled with real volume so that almost none of the tube shows through. In his right hand he holds a plain unlabeled clear glass jar of white powder, tilted just above it.",
  "scene": "SAME home apothecary room as the reference image: a light wood shelf of labelled glass jars and dark amber bottles behind him, a small American flag on a table stand on that shelf, discreet but clearly visible and in sharp focus, and a window with blinds to the right showing an ordinary American residential street. A dark wooden table sits in front of him.",
  "posture": "Seated on his round wooden stool at the dark wooden table, leaning slightly forward toward the camera.",
  "composition": "The coiled model fills the lower two thirds of the frame and sits much closer to the lens than his face, so it is unmistakably the hero. His head and shoulders occupy the upper third and the top of his head is cropped by the top edge. Nothing else competes.",
  "camera": "chest level, straight-on, camera pushed in close and slightly high toward the model",
  "state": "Start frame: the jar is tilted above the model and the first grains of white powder are about to fall. The crust is intact and dry, nothing has reacted yet.",
  "lighting": "Flat neutral daylight from the window under an overcast sky, evenly lighting his face, no warm orange cast and no yellow tint.",
  "realism": "UGC realism, real skin texture with visible pores, individual hair strands, subtle wrinkles, realistic shadows and reflections, iPhone-footage look, phone camera look not professional photography, no AI polish, no beauty smoothing, no blur anywhere, everything in sharp focus including the shelf and the window.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no studio, no plastic skin, no extra fingers, no supernatural lighting, no blur, no artificial lighting, no warm orange color cast, no yellow tint, no de-aging, no skin smoothing, no thin scattered layer, no jewelry, no second person, no foam"
}
```

## K04 · T11 · HOOK D · GERAR DO ZERO · ÂNCORA LYNN PARKER

> ### 📎 ANEXAR: **1 IMAGEM**
> **1️⃣ ÂNCORA LYNN PARKER** `producao/_ancoras/lynn_parker_ancora.jpeg`
>
> ### 🆕 GERAR DO ZERO

```json
{
  "shot_id": "K04_hook_soda_inverted",
  "reference_use": "Use the attached image ONLY for Lynn Parker's face, identity, hair, wardrobe and his home apothecary room. Do NOT copy its pose or framing.",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "identity_main": "The EXACT man from the attached reference image (Lynn Parker): Black American man around seventy, medium brown skin, long silver white locs tied back behind his shoulders with two or three strands falling in front of his right shoulder, white hair on top with a high hairline, a full white beard and white moustache neatly trimmed, a long dignified face with a high forehead, visible moles, grey eyebrows and calm dark brown eyes, upright and steady posture, deep lines and heavy crow's feet.",
  "wardrobe": "A white linen mandarin collar tunic with an asymmetric front closure and white buttons, falling below the hip, and dark trousers. No jewelry of any kind.",
  "prop": "Two soft matte silicone teaching models shaped like human legs, smooth tapered forms in muted cream with no face and no fine detail, lying flat side by side on the dark wooden table. Both are completely clean, smooth and bare, with nothing on them at all. In his right hand he holds a plain unlabeled clear glass jug of dark caramel-colored fizzy drink, tilted just above the two models.",
  "scene": "SAME home apothecary room as the reference image: a light wood shelf of labelled glass jars and dark amber bottles behind him, a small American flag on a table stand on that shelf, discreet but clearly visible and in sharp focus, and a window with blinds to the right showing an ordinary American residential street. A dark wooden table sits in front of him.",
  "posture": "Seated on his round wooden stool at the dark wooden table, leaning slightly forward toward the camera.",
  "composition": "The two clean models fill the lower two thirds of the frame and sit much closer to the lens than his face, so they are unmistakably the hero. His head and shoulders occupy the upper third and the top of his head is cropped by the top edge. Nothing else competes.",
  "camera": "chest level, straight-on, camera pushed in close and slightly high toward the two models",
  "state": "Start frame: the jug is tilted and the first drops of dark liquid are about to fall. The models are still perfectly clean.",
  "lighting": "Flat neutral daylight from the window under an overcast sky, evenly lighting his face, no warm orange cast and no yellow tint.",
  "realism": "UGC realism, real skin texture with visible pores, individual hair strands, subtle wrinkles, realistic shadows and reflections, iPhone-footage look, phone camera look not professional photography, no AI polish, no beauty smoothing, no blur anywhere, everything in sharp focus including the shelf and the window.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no studio, no plastic skin, no extra fingers, no supernatural lighting, no blur, no artificial lighting, no warm orange color cast, no yellow tint, no de-aging, no skin smoothing, no yellow beads in this frame, no label on the glass, no jewelry, no second person"
}
```

## K05 · T12 · HOOK E · GERAR DO ZERO · ÂNCORA LYNN PARKER

> ### 📎 ANEXAR: **1 IMAGEM**
> **1️⃣ ÂNCORA LYNN PARKER** `producao/_ancoras/lynn_parker_ancora.jpeg`
>
> ### 🆕 GERAR DO ZERO

```json
{
  "shot_id": "K05_hook_sugar_inverted",
  "reference_use": "Use the attached image ONLY for Lynn Parker's face, identity, hair, wardrobe and his home apothecary room. Do NOT copy its pose or framing.",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "identity_main": "The EXACT man from the attached reference image (Lynn Parker): Black American man around seventy, medium brown skin, long silver white locs tied back behind his shoulders with two or three strands falling in front of his right shoulder, white hair on top with a high hairline, a full white beard and white moustache neatly trimmed, a long dignified face with a high forehead, visible moles, grey eyebrows and calm dark brown eyes, upright and steady posture, deep lines and heavy crow's feet.",
  "wardrobe": "A white linen mandarin collar tunic with an asymmetric front closure and white buttons, falling below the hip, and dark trousers. No jewelry of any kind.",
  "prop": "Two soft matte silicone teaching models shaped like human legs, smooth tapered forms in muted cream with no face and no fine detail, lying flat side by side on the dark wooden table. Both are completely clean, smooth and bare, with nothing on them at all. In his raised right hand he holds a plain unlabeled clear glass jar of coarse white granulated sugar, tipped high above the two models.",
  "scene": "SAME home apothecary room as the reference image: a light wood shelf of labelled glass jars and dark amber bottles behind him, a small American flag on a table stand on that shelf, discreet but clearly visible and in sharp focus, and a window with blinds to the right showing an ordinary American residential street. A dark wooden table sits in front of him.",
  "posture": "Seated on his round wooden stool at the dark wooden table, right arm raised so the jar is well above the table.",
  "composition": "The two clean models fill the lower two thirds of the frame and sit much closer to the lens than his face, so they are unmistakably the hero. His head and shoulders occupy the upper third and the top of his head is cropped by the top edge. Nothing else competes.",
  "camera": "chest level, straight-on, camera pushed in close and slightly high toward the two models",
  "state": "Start frame: the jar is tipped high and the first white grains are about to fall. The models are still perfectly clean.",
  "lighting": "Flat neutral daylight from the window under an overcast sky, evenly lighting his face, no warm orange cast and no yellow tint.",
  "realism": "UGC realism, real skin texture with visible pores, individual hair strands, subtle wrinkles, realistic shadows and reflections, iPhone-footage look, phone camera look not professional photography, no AI polish, no beauty smoothing, no blur anywhere, everything in sharp focus including the shelf and the window.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no studio, no plastic skin, no extra fingers, no supernatural lighting, no blur, no artificial lighting, no warm orange color cast, no yellow tint, no de-aging, no skin smoothing, no yellow beads in this frame, no label on the glass, no jewelry, no second person"
}
```

## K06 · T2 · RECEITA A · GERAR DO ZERO · ÂNCORA LYNN PARKER

> ### 📎 ANEXAR: **1 IMAGEM**
> **1️⃣ ÂNCORA LYNN PARKER** `producao/_ancoras/lynn_parker_ancora.jpeg`
>
> ### 🆕 GERAR DO ZERO

```json
{
  "shot_id": "K06_recipe_clear_water",
  "reference_use": "Use the attached image ONLY for Lynn Parker's face, identity, hair, wardrobe and his home apothecary room. Do NOT copy its pose or framing.",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "identity_main": "The EXACT man from the attached reference image (Lynn Parker): Black American man around seventy, medium brown skin, long silver white locs tied back behind his shoulders with two or three strands falling in front of his right shoulder, white hair on top with a high hairline, a full white beard and white moustache neatly trimmed, a long dignified face with a high forehead, visible moles, grey eyebrows and calm dark brown eyes, upright and steady posture, deep lines and heavy crow's feet.",
  "wardrobe": "A white linen mandarin collar tunic with an asymmetric front closure and white buttons, falling below the hip, and dark trousers. No jewelry of any kind.",
  "prop": "A tall straight plain drinking glass of completely clear water standing on the dark wooden table, and a metal teaspoon heaped with white powder held in his right hand just above the rim of the glass.",
  "scene": "SAME home apothecary room as the reference image: a light wood shelf of labelled glass jars and dark amber bottles behind him, a small American flag on a table stand on that shelf, discreet but clearly visible and in sharp focus, and a window with blinds to the right showing an ordinary American residential street. A dark wooden table sits in front of him.",
  "posture": "Seated on his round wooden stool at the dark wooden table, leaning slightly forward toward the camera, left forearm resting on the table.",
  "composition": "The glass sits in the lower foreground, closer to the lens than his face, and the spoon hovers right above it. His head and shoulders occupy the upper part of the frame. Nothing else on the table.",
  "camera": "chest level, straight-on, camera close and slightly high toward the glass",
  "state": "Start frame: the water is perfectly clear and the powder is still on the spoon.",
  "lighting": "Flat neutral daylight from the window under an overcast sky, evenly lighting his face, no warm orange cast and no yellow tint.",
  "realism": "UGC realism, real skin texture with visible pores, individual hair strands, subtle wrinkles, realistic shadows and reflections, iPhone-footage look, phone camera look not professional photography, no AI polish, no beauty smoothing, no blur anywhere, everything in sharp focus including the shelf and the window.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no studio, no plastic skin, no extra fingers, no supernatural lighting, no blur, no artificial lighting, no warm orange color cast, no yellow tint, no de-aging, no skin smoothing, no cloudy water in this frame, no jewelry, no second person"
}
```

## K07 · T3 · RECEITA B · EDITAR do K06

> ### 📎 ANEXAR: **1 IMAGEM**
> **1️⃣ O K06 já aprovado**
> 🚫 NUNCA anexar a âncora aqui, e nunca anexar o K08.
>
> ### ✏️ EDITAR, muda só o estado do copo e o limão na mão

```json
{
  "task": "edit the attached image, keep everything identical except the changes listed",
  "keep_identical": "Keep the man exactly the same: same face, same long white locs, same full white beard, same white linen mandarin collar tunic, no jewelry, same seated position on the stool and same distance from the camera. Keep the SAME apothecary background exactly: the shelf of labelled jars and amber bottles, the small American flag on its stand, the window with blinds and the street beyond, same neutral daylight, same camera angle and framing.",
  "change_1": "The water inside the glass is now cloudy and pale gold instead of clear, as if powder had been stirred into it. The glass stays in exactly the same place.",
  "change_2": "The metal teaspoon is gone from his right hand. He now holds half a lemon, cut side down, squeezed between his fingers directly above the rim of the glass, with the first drop of juice about to fall.",
  "realism": "UGC realism, real skin texture with visible pores, iPhone-footage look, no AI polish, no beauty smoothing, no blur anywhere. Do not make his skin darker, yellowish or orangish. Do not make the colors more saturated.",
  "negative": "do not change the face, do not change the identity, do not change the background, do not change the camera angle, no captions, no subtitles, no words overlaid on the image, no plastic skin, no extra fingers, no warm orange color cast, no yellow tint, no de-aging, no skin smoothing, no jewelry, no second person"
}
```

## K08 · T4 · PROTOCOLO · EDITAR do K06

> ### 📎 ANEXAR: **1 IMAGEM**
> **1️⃣ O K06 já aprovado**
> 🚫 NUNCA anexar o K07 aqui. Os estágios saem sempre do K06 original.
>
> ### ✏️ EDITAR, muda só o líquido e as duas mãos

```json
{
  "task": "edit the attached image, keep everything identical except the changes listed",
  "keep_identical": "Keep the man exactly the same: same face, same long white locs, same full white beard, same white linen mandarin collar tunic, no jewelry, same seated position on the stool and same distance from the camera. Keep the SAME apothecary background exactly: the shelf of labelled jars and amber bottles, the small American flag on its stand, the window with blinds and the street beyond, same neutral daylight, same camera angle and framing.",
  "change_1": "The liquid inside the glass is now a settled warm amber, slightly translucent, filling the glass almost to the top. The glass stays in exactly the same place.",
  "change_2": "The teaspoon is gone. Both of his hands are now wrapped loosely around the glass on the table, fingers relaxed, as if he had just set it down in front of the viewer.",
  "realism": "UGC realism, real skin texture with visible pores, iPhone-footage look, no AI polish, no beauty smoothing, no blur anywhere. Do not make his skin darker, yellowish or orangish. Do not make the colors more saturated.",
  "negative": "do not change the face, do not change the identity, do not change the background, do not change the camera angle, no captions, no subtitles, no words overlaid on the image, no plastic skin, no extra fingers, no warm orange color cast, no yellow tint, no de-aging, no skin smoothing, no jewelry, no second person"
}
```

## K09 · T5 · PONTE · GERAR DO ZERO · ÂNCORA LYNN PARKER

> ### 📎 ANEXAR: **1 IMAGEM**
> **1️⃣ ÂNCORA LYNN PARKER** `producao/_ancoras/lynn_parker_ancora.jpeg`
>
> ### 🆕 GERAR DO ZERO

```json
{
  "shot_id": "K09_bridge_close",
  "reference_use": "Use the attached image ONLY for Lynn Parker's face, identity, hair, wardrobe and his home apothecary room. Do NOT copy its pose or framing.",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "identity_main": "The EXACT man from the attached reference image (Lynn Parker): Black American man around seventy, medium brown skin, long silver white locs tied back behind his shoulders with two or three strands falling in front of his right shoulder, a full white beard and white moustache, a long dignified face with a high forehead, visible moles, grey eyebrows and calm dark brown eyes, deep lines and heavy crow's feet.",
  "wardrobe": "A white linen mandarin collar tunic with an asymmetric front closure and white buttons. No jewelry of any kind.",
  "scene": "SAME home apothecary room as the reference image, with the light wood shelf of labelled glass jars behind him and the small American flag on its stand visible over his shoulder, discreet but clearly visible and in sharp focus.",
  "posture": "Seated upright on his stool, leaning in close to the camera, chin level, calm and certain expression.",
  "composition": "TIGHT. Shoulders-up framing, closer than every other shot of the video. His face fills a large part of the frame and the top of his head is cropped by the top edge. The table is out of frame and there is no prop anywhere.",
  "camera": "eye level, straight-on, close talking distance",
  "state": "Start frame: speaking directly into the lens, both hands out of frame.",
  "lighting": "Flat neutral daylight from the window under an overcast sky, evenly lighting his face, no warm orange cast and no yellow tint.",
  "realism": "UGC realism, real skin texture with visible pores, individual hair strands, subtle wrinkles, realistic shadows and reflections, iPhone-footage look, phone camera look not professional photography, no AI polish, no beauty smoothing, no blur anywhere, everything in sharp focus including the shelf behind him.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no studio, no plastic skin, no extra fingers, no supernatural lighting, no blur, no artificial lighting, no warm orange color cast, no yellow tint, no de-aging, no skin smoothing, no props, no jewelry, no second person"
}
```

## K10 · T6 · ÁLIBI · EDITAR do K09

> ### 📎 ANEXAR: **1 IMAGEM**
> **1️⃣ O K09 já aprovado**
>
> ### ✏️ EDITAR, muda só o gesto de mão

```json
{
  "task": "edit the attached image, keep everything identical except the change listed",
  "keep_identical": "Keep the man exactly the same: same face, same long white locs, same full white beard, same white linen mandarin collar tunic, no jewelry, same head position, same expression, same distance from the camera. Keep the SAME apothecary background exactly: the shelf of labelled jars, the small American flag on its stand, same neutral daylight, same camera angle and framing.",
  "change_1": "His right hand now comes up into the bottom of the frame at chest height with two fingers extended in a small counting gesture. Nothing else moves.",
  "realism": "UGC realism, real skin texture with visible pores, iPhone-footage look, no AI polish, no beauty smoothing, no blur anywhere. Do not make his skin darker, yellowish or orangish. Do not make the colors more saturated.",
  "negative": "do not change the face, do not change the identity, do not change the background, do not change the camera angle, no captions, no subtitles, no words overlaid on the image, no plastic skin, no extra fingers, no warm orange color cast, no yellow tint, no de-aging, no skin smoothing, no props, no jewelry, no second person"
}
```

## K11 · T7 · CTA · EDITAR do K09

> ### 📎 ANEXAR: **1 IMAGEM**
> **1️⃣ O K09 já aprovado**
> 🚫 NUNCA anexar o K10 aqui.
>
> ### ✏️ EDITAR, muda só o gesto de mão e a distância

```json
{
  "task": "edit the attached image, keep everything identical except the changes listed",
  "keep_identical": "Keep the man exactly the same: same face, same long white locs, same full white beard, same white linen mandarin collar tunic, no jewelry, same expression. Keep the SAME apothecary background exactly: the shelf of labelled jars, the small American flag on its stand, same neutral daylight, same camera angle.",
  "change_1": "Push the camera about ten percent closer so the framing tightens slightly and his face becomes even more dominant. Do not change the angle or the height of the camera.",
  "change_2": "His right hand comes up into the bottom of the frame at chest height, palm open toward the lens in a natural offering gesture.",
  "realism": "UGC realism, real skin texture with visible pores, iPhone-footage look, no AI polish, no beauty smoothing, no blur anywhere. Do not make his skin darker, yellowish or orangish. Do not make the colors more saturated.",
  "negative": "do not change the face, do not change the identity, do not change the background, no captions, no subtitles, no words overlaid on the image, no plastic skin, no extra fingers, no warm orange color cast, no yellow tint, no de-aging, no skin smoothing, no props, no jewelry, no second person"
}
```

## K12 · T8 · FOLLOW GATE · EDITAR do K09

> ### 📎 ANEXAR: **1 IMAGEM**
> **1️⃣ O K09 já aprovado**
> 🚫 NUNCA anexar o K11 aqui.
>
> ### ✏️ EDITAR, muda só o braço direito, apontando

```json
{
  "task": "edit the attached image, keep everything identical except the change listed",
  "keep_identical": "Keep the man exactly the same: same face, same long white locs, same full white beard, same white linen mandarin collar tunic, no jewelry, same head position, same distance from the camera. Keep the SAME apothecary background exactly: the shelf of labelled jars, the small American flag on its stand, same neutral daylight, same camera angle and framing.",
  "change_1": "His right arm comes up into the frame and he points his index finger straight at the lens, close to the camera, in a direct and warm way. Nothing else moves.",
  "realism": "UGC realism, real skin texture with visible pores, iPhone-footage look, no AI polish, no beauty smoothing, no blur anywhere. Do not make his skin darker, yellowish or orangish. Do not make the colors more saturated.",
  "negative": "do not change the face, do not change the identity, do not change the background, do not change the camera angle, no captions, no subtitles, no words overlaid on the image, no plastic skin, no extra fingers, no warm orange color cast, no yellow tint, no de-aging, no skin smoothing, no props, no jewelry, no second person"
}
```

---

## Bloco global de vídeo

```text
o avatar (homem) fala em inglês com sotaque americano de Lynn Parker, voz autêntica, dinâmica, apaixonada e emocional, como se exigisse ser ouvida, a seguinte frase: "[FALA EXATA DO ROTEIRO]"

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: [ação ENXUTA, só o que acontece]

câmera: [fixa / leve push-in]

som ambiente: sala silenciosa de casa, com um leve ruído de rua ao longe, sem música
```

---

# Prompts de vídeo

### V01 · T1 · usa K01

```text
o avatar (homem) fala em inglês com sotaque americano de Lynn Parker, voz autêntica, dinâmica, apaixonada e emocional, como se exigisse ser ouvida, a seguinte frase: "This is what baking soda does to the fat on a woman's legs at twenty five, and at fifty five."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ele inclina o pote e o pó branco cai sobre os dois modelos ao mesmo tempo. A espuma branca sobe nos dois. Na esquerda a camada amarela some quase toda, na direita quase nada se move.

câmera: fixa

som ambiente: sala silenciosa de casa, com um leve ruído de rua ao longe, sem música
```

### V02 · T9 · usa K02

```text
o avatar (homem) fala em inglês com sotaque americano de Lynn Parker, voz autêntica, dinâmica, apaixonada e emocional, como se exigisse ser ouvida, a seguinte frase: "This is what baking soda does to the fat on a woman's belly after forty. Watch."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ele inclina o pote e o pó branco cai sobre o modelo. A espuma branca sobe, ele passa a mão por cima e a camada amarela sai, deixando a superfície lisa.

câmera: fixa

som ambiente: sala silenciosa de casa, com um leve ruído de rua ao longe, sem música
```

### V03 · T10 · usa K03

```text
o avatar (homem) fala em inglês com sotaque americano de Lynn Parker, voz autêntica, dinâmica, apaixonada e emocional, como se exigisse ser ouvida, a seguinte frase: "This is what baking soda does to what is stuck in a woman's gut after forty. Watch."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ele inclina o pote e o pó branco cai sobre o modelo. A crosta seca borbulha alto e se solta em placas, que escorregam para a mesa.

câmera: fixa

som ambiente: sala silenciosa de casa, com um leve ruído de rua ao longe, sem música
```

### V04 · T11 · usa K04

```text
o avatar (homem) fala em inglês com sotaque americano de Lynn Parker, voz autêntica, dinâmica, apaixonada e emocional, como se exigisse ser ouvida, a seguinte frase: "This is what one soda a day does to the fat on a woman's legs after forty. Watch."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ele inclina a jarra e o líquido escuro escorre sobre os dois modelos. Onde o líquido encosta, contas amarelas brotam e crescem depressa.

câmera: fixa

som ambiente: sala silenciosa de casa, com um leve ruído de rua ao longe, sem música
```

### V05 · T12 · usa K05

```text
o avatar (homem) fala em inglês com sotaque americano de Lynn Parker, voz autêntica, dinâmica, apaixonada e emocional, como se exigisse ser ouvida, a seguinte frase: "This is what sugar does to the fat on a woman's legs after forty. Watch."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ele vira o pote e o açúcar cai de cima em cascata. Onde os grãos encostam, a camada amarela infla e engrossa.

câmera: fixa

som ambiente: sala silenciosa de casa, com um leve ruído de rua ao longe, sem música
```

### V06 · T2 · usa K06

```text
o avatar (homem) fala em inglês com sotaque americano de Lynn Parker, voz autêntica, dinâmica, apaixonada e emocional, como se exigisse ser ouvida, a seguinte frase: "A teaspoon of baking soda and a pinch of cinnamon in a glass of warm water."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ele vira a colher e o pó branco cai dentro do copo. A água fica turva na hora.

câmera: fixa

som ambiente: sala silenciosa de casa, com um leve ruído de rua ao longe, sem música
```

### V07 · T3 · usa K07

```text
o avatar (homem) fala em inglês com sotaque americano de Lynn Parker, voz autêntica, dinâmica, apaixonada e emocional, como se exigisse ser ouvida, a seguinte frase: "Then the juice of half a lemon. Stir it until the water turns cloudy and gold."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ele aperta o meio limão e o suco escorre dentro do copo.

câmera: fixa

som ambiente: sala silenciosa de casa, com um leve ruído de rua ao longe, sem música
```

### V08 · T4 · usa K08

```text
o avatar (homem) fala em inglês com sotaque americano de Lynn Parker, voz autêntica, dinâmica, apaixonada e emocional, como se exigisse ser ouvida, a seguinte frase: "Drink it slow, on an empty stomach, every morning. In forty years, the women who come to me notice their legs first."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ele desliza o copo alguns centímetros na direção da câmera e solta as mãos.

câmera: fixa

som ambiente: sala silenciosa de casa, com um leve ruído de rua ao longe, sem música
```

### V09 · T5 · usa K09

```text
o avatar (homem) fala em inglês com sotaque americano de Lynn Parker, voz autêntica, dinâmica, apaixonada e emocional, como se exigisse ser ouvida, a seguinte frase: "That drink works. But after forty, three things hold that fat: your hormones, your metabolism, and your gut. It only touches the gut."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ele fala direto para a lente, sem se mexer do lugar.

câmera: fixa

som ambiente: sala silenciosa de casa, com um leve ruído de rua ao longe, sem música
```

### V10 · T6 · usa K10

```text
o avatar (homem) fala em inglês com sotaque americano de Lynn Parker, voz autêntica, dinâmica, apaixonada e emocional, como se exigisse ser ouvida, a seguinte frase: "If yours is the hormone one, or the metabolism one, you can drink this all month and your legs will not change."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ele mantém os dois dedos levantados e depois abaixa a mão devagar.

câmera: fixa

som ambiente: sala silenciosa de casa, com um leve ruído de rua ao longe, sem música
```

### V11 · T7 · usa K11

```text
o avatar (homem) fala em inglês com sotaque americano de Lynn Parker, voz autêntica, dinâmica, apaixonada e emocional, como se exigisse ser ouvida, a seguinte frase: "It was never what you drink. It is which of the three is yours. Comment yes and I will send you the FityWell quiz."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ele abre a mão na direção da lente enquanto fala.

câmera: leve push-in

som ambiente: sala silenciosa de casa, com um leve ruído de rua ao longe, sem música
```

### V12 · T8 · usa K12

```text
o avatar (homem) fala em inglês com sotaque americano de Lynn Parker, voz autêntica, dinâmica, apaixonada e emocional, como se exigisse ser ouvida, a seguinte frase: "But follow me first, or it will not let me reach you. Two minutes and you will know."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ele aponta o dedo para a lente e mantém o gesto até o fim da fala.

câmera: leve push-in

som ambiente: sala silenciosa de casa, com um leve ruído de rua ao longe, sem música
```

---

## Mapa de âncoras

| Keyframe | Referências a anexar | Modelo |
|---|---|---|
| K01 a K06 | ÂNCORA LYNN PARKER | Nano Banana 2, 9:16 |
| K07 | o K06 aprovado | Nano Banana 2, 9:16 |
| K08 | o K06 aprovado | Nano Banana 2, 9:16 |
| K09 | ÂNCORA LYNN PARKER | Nano Banana 2, 9:16 |
| K10 | o K09 aprovado | Nano Banana 2, 9:16 |
| K11 | o K09 aprovado | Nano Banana 2, 9:16 |
| K12 | o K09 aprovado | Nano Banana 2, 9:16 |

Vídeo: Veo 3.1 Lite, Lower Priority, 8 segundos, 3 variações, imagem sempre como INITIAL FRAME.

---

## Montagem no CapCut

1. **Escolher UM gancho por vídeo.** Cada vídeo finalizado é V01, V02, V03, V04 ou V05 na abertura,
   seguido sempre de V06, V07, V08, V09, V10, V11 e V12.
2. Cortar cada clipe no fim da fala. O corte do gancho entra no auge da reação.
3. Legenda queimada em todos os takes, palavra destacada em amarelo na keyword.
4. No T7, quando ele disser `yes`, subir a palavra `YES` grande na tela por um segundo.
5. Sem música. Só o som ambiente do clipe.
6. Exportar em 9:16, 1080 por 1920.

---

## Gates de qualidade

1. [ ] O herói está no lower foreground, mais perto da lente que o rosto, em K01 a K05.
2. [ ] A camada de contas saiu **volumosa**, não uma película fina.
3. [ ] O modelo didático saiu com a forma pedida e sem detalhe anatômico fino.
4. [ ] A bandeirinha dos EUA aparece e está em foco nos doze keyframes.
5. [ ] Nenhum keyframe tem celular, tela, rótulo de marca ou qualquer coisa que leia como produto.
6. [ ] Zero joia em todos os keyframes.
7. [ ] **A idade dele não foi suavizada em nenhum keyframe.** Linhas, rugas e pele solta intactas.
8. [ ] As locs brancas e a barba branca estão idênticas nos doze keyframes.
9. [ ] Zero blur em qualquer imagem, inclusive na estante e na janela.
10. [ ] Luz neutra de dia nublado. Nenhuma imagem com cast quente.
11. [ ] Nenhum `negative` cita nome de órgão, gore ou marca.
12. [ ] A fala de cada V bate palavra por palavra com o take do `ROTEIRO.md`.
13. [ ] Nenhum take sugere que ela não se esforçou o bastante.
14. [ ] `python checar_entrega.py producao/fitywell_pernas` fechou sem FALHA.
