# Dana Morrison | Ângulo 2 (FityWell) | Pacote de Prompts

Vídeo modelo: `8bd57dab-62d3-452a-8809-4b5eb72834d5.mp4` (27,97 s, 6 takes)

Âncora de identidade: `producao/_ancoras/dana_morrison_ancora.jpeg`

Funil: comment `yes` -> DM -> link do quiz FityWell

Avatar 1 de 3 da fila. Ver `AVATAR_QUEUE.md`.

---

## Índice de geração

| Take | Keyframe | Anexar | Ação de geração |
|---|---|---|---|
| T1 | K01 | ÂNCORA DANA MORRISON | GERAR DO ZERO. Gancho vinte e cinco contra cinquenta e cinco |
| T9 | K02 | ÂNCORA DANA MORRISON | GERAR DO ZERO. Gancho da barriga |
| T10 | K03 | ÂNCORA DANA MORRISON | GERAR DO ZERO. Gancho do intestino |
| T11 | K04 | ÂNCORA DANA MORRISON | GERAR DO ZERO. Gancho do refrigerante |
| T12 | K05 | ÂNCORA DANA MORRISON | GERAR DO ZERO. Gancho do açúcar |
| T2 | K06 | ÂNCORA DANA MORRISON | GERAR DO ZERO. Copo de água limpa |
| T3 | K07 | o K06 aprovado | EDITAR do K06. Muda só o estado do copo e o limão |
| T4 | K08 | o K06 aprovado | EDITAR do K06. Muda só o líquido e as mãos |
| T5 | K09 | ÂNCORA DANA MORRISON | GERAR DO ZERO. Close de CTA, sem prop |
| T6 | K10 | o K09 aprovado | EDITAR do K09. Muda só o gesto de mão |
| T7 | K11 | o K09 aprovado | EDITAR do K09. Muda só o gesto de mão |
| T8 | K12 | o K09 aprovado | EDITAR do K09. Muda só o braço direito, apontando |

Regra de bolso: **GERAR DO ZERO anexa a âncora. EDITAR anexa uma imagem só, o keyframe de origem.**
🚫 Nunca anexar um keyframe editado como origem de outro. Estágios sempre a partir do original.

Total: 12 keyframes para 12 takes. Cada vídeo finalizado usa **um** dos cinco ganchos.

---

## Trava de identidade e continuidade

Aplicar em toda imagem e todo clipe:

- Homem negro americano de pouco mais de cinquenta anos, pele marrom escura, rosto magro e anguloso, maçãs altas, olhos castanhos escuros.
- **Do-rag preto de cetim** amarrado na cabeça, com a aba caindo atrás do ombro esquerdo.
- **Barba do queixo comprida e branca**, cheia, com bigode mais escuro salpicado de grisalho. Nunca encurtar a barba.
- Corpo seco e treinado, ombros largos, antebraços com veias marcadas, mãos grandes e calejadas.
- **Regata canelada preta e corrente fina de OURO sem pingente.** Sem cruz, sem prata, sem relógio.
- Mesma garagem em todos os planos: bancada de madeira gasta no primeiro plano, parede de pegboard marrom com chaves e chaves de fenda penduradas, armário de madeira com potes de vidro de ervas rotulados e **uma bandeirinha dos EUA em pé na prateleira**, discreta e em foco.
- Luz neutra de dia entrando pela porta aberta da garagem. Zero blur, tudo em foco nítido. Cara de vídeo de iPhone, nunca polimento de IA.

---

## Trava do prop herói

O herói é o **modelo anatômico coberto pela camada**, e o que vende é a **dissolução**. Regras que
valem nos cinco ganchos:

```text
Life-size anatomical teaching models molded in matte cream-toned silicone, the kind used in a health
classroom, lying flat on the workbench in the lower foreground, closer to the lens than the man's
face. Where the model is covered, the covering is a THICK, HEAPED, three-dimensional layer of pale
yellow waxy globules piled high with real volume, so dense that almost none of the cream silicone
underneath is visible. Never a thin scattered layer and never a flat sauce-like coating. The shape,
size and color of each model stay identical across every shot.
```

**Falha #6 vive aqui:** descrever sempre a FORMA do modelo, nunca só o nome, senão sai coração ou
crânio. O negative de todo keyframe de gancho carrega `no heart model, no skull model, no brain model`.

## Trava da 2ª pessoa (REF-A)

**Não se aplica nesta produção.** Não há segunda pessoa em nenhum take. O negative de todo keyframe
carrega `no second person`.

---

# Prompts de imagem

## K01 · T1 · HOOK A · GERAR DO ZERO · ÂNCORA DANA MORRISON

> ### 📎 ANEXAR: **1 IMAGEM**
> **1️⃣ ÂNCORA DANA MORRISON** `producao/_ancoras/dana_morrison_ancora.jpeg`
>
> ### 🆕 GERAR DO ZERO

```json
{
  "shot_id": "K01_hook_25_vs_55",
  "reference_use": "Use the attached image ONLY for Dana Morrison's face, identity, beard, do-rag, wardrobe and the garage scene. Do NOT copy its pose or framing.",
  "identity_main": "The EXACT man from the attached reference image (Dana Morrison): Black American man in his early fifties, deep brown skin, a black satin do-rag tied over his head with the tail falling behind his left shoulder, a long full white chin beard with a darker moustache flecked with grey, angular face with high cheekbones, dark brown eyes, lean powerfully trained build with broad shoulders and corded forearms with visible veins.",
  "wardrobe": "Plain black ribbed tank top and a thin gold chain with no pendant, dark trousers.",
  "prop": "Two life-size anatomical teaching models of a human leg from hip to ankle, molded in matte cream-toned silicone, lying flat side by side on the workbench. The model on the left carries only a thin sparse scatter of pale yellow waxy globules. The model on the right is buried under a THICK, HEAPED, three-dimensional layer of the same pale yellow globules, piled high with real volume so that almost none of the cream silicone is visible. In his right hand he holds a plain unlabeled clear glass jar of white powder, tilted just above the two models.",
  "scene": "SAME garage workshop as the reference image: brown pegboard wall hung with wrenches and screwdrivers, an open wooden shelf of labelled glass herb jars, and a small American flag standing upright on that shelf, discreet but clearly visible and in sharp focus.",
  "posture": "Seated at his own scuffed wooden workbench, leaning slightly forward toward the camera, both forearms low near the bench top.",
  "composition": "The two leg models fill the lower two thirds of the frame and sit much closer to the lens than his face, so they are unmistakably the hero. His head and shoulders occupy the upper third and the top of his head is cropped by the top edge. Nothing else competes. The garage behind is barely readable, just enough to recognize the place.",
  "camera": "chest level, straight-on, camera pushed in close and slightly high toward the two models",
  "state": "Start frame: the jar is tilted above the models and the first grains of white powder are about to fall. Nothing has reacted yet, no foam anywhere.",
  "lighting": "Flat neutral daylight spilling in from the open garage door, evenly lighting his face, no warm orange cast and no yellow tint.",
  "realism": "UGC realism, real skin texture with visible pores, individual hair strands, subtle wrinkles, realistic shadows and reflections, iPhone-footage look, phone camera look not professional photography, no AI polish, no beauty smoothing, no blur anywhere, everything in sharp focus including background wall shelf and tools.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no studio, no plastic skin, no extra fingers, no supernatural lighting, no blur, no artificial lighting, no warm orange color cast, no yellow tint, no heart model, no skull model, no brain model, no thin scattered layer, no flat sauce-like coating, no silver jewelry, no cross pendant, no second person, no foam"
}
```

## K02 · T9 · HOOK B · GERAR DO ZERO · ÂNCORA DANA MORRISON

> ### 📎 ANEXAR: **1 IMAGEM**
> **1️⃣ ÂNCORA DANA MORRISON** `producao/_ancoras/dana_morrison_ancora.jpeg`
>
> ### 🆕 GERAR DO ZERO

```json
{
  "shot_id": "K02_hook_belly",
  "reference_use": "Use the attached image ONLY for Dana Morrison's face, identity, beard, do-rag, wardrobe and the garage scene. Do NOT copy its pose or framing.",
  "identity_main": "The EXACT man from the attached reference image (Dana Morrison): Black American man in his early fifties, deep brown skin, a black satin do-rag tied over his head with the tail falling behind his left shoulder, a long full white chin beard with a darker moustache flecked with grey, angular face with high cheekbones, dark brown eyes, lean powerfully trained build with broad shoulders and corded forearms with visible veins.",
  "wardrobe": "Plain black ribbed tank top and a thin gold chain with no pendant, dark trousers.",
  "prop": "One life-size anatomical teaching model of a female midsection from the lower ribs down to the hips, molded in matte cream-toned silicone, lying flat on the workbench. The whole front of it is buried under a THICK, HEAPED, three-dimensional layer of pale yellow waxy globules piled high with real volume, so dense that almost none of the cream silicone is visible. In his right hand he holds a plain unlabeled clear glass jar of white powder, tilted just above it.",
  "scene": "SAME garage workshop as the reference image: brown pegboard wall hung with wrenches and screwdrivers, an open wooden shelf of labelled glass herb jars, and a small American flag standing upright on that shelf, discreet but clearly visible and in sharp focus.",
  "posture": "Seated at his own scuffed wooden workbench, leaning slightly forward toward the camera, both forearms low near the bench top.",
  "composition": "The midsection model fills the lower two thirds of the frame and sits much closer to the lens than his face, so it is unmistakably the hero. His head and shoulders occupy the upper third and the top of his head is cropped by the top edge. Nothing else competes. The garage behind is barely readable.",
  "camera": "chest level, straight-on, camera pushed in close and slightly high toward the model",
  "state": "Start frame: the jar is tilted above the model and the first grains of white powder are about to fall. Nothing has reacted yet, no foam anywhere.",
  "lighting": "Flat neutral daylight spilling in from the open garage door, evenly lighting his face, no warm orange cast and no yellow tint.",
  "realism": "UGC realism, real skin texture with visible pores, individual hair strands, subtle wrinkles, realistic shadows and reflections, iPhone-footage look, phone camera look not professional photography, no AI polish, no beauty smoothing, no blur anywhere, everything in sharp focus including background wall shelf and tools.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no studio, no plastic skin, no extra fingers, no supernatural lighting, no blur, no artificial lighting, no warm orange color cast, no yellow tint, no heart model, no skull model, no brain model, no thin scattered layer, no flat sauce-like coating, no silver jewelry, no cross pendant, no second person, no foam"
}
```

## K03 · T10 · HOOK C · GERAR DO ZERO · ÂNCORA DANA MORRISON

> ### 📎 ANEXAR: **1 IMAGEM**
> **1️⃣ ÂNCORA DANA MORRISON** `producao/_ancoras/dana_morrison_ancora.jpeg`
>
> ### 🆕 GERAR DO ZERO

```json
{
  "shot_id": "K03_hook_gut",
  "reference_use": "Use the attached image ONLY for Dana Morrison's face, identity, beard, do-rag, wardrobe and the garage scene. Do NOT copy its pose or framing.",
  "identity_main": "The EXACT man from the attached reference image (Dana Morrison): Black American man in his early fifties, deep brown skin, a black satin do-rag tied over his head with the tail falling behind his left shoulder, a long full white chin beard with a darker moustache flecked with grey, angular face with high cheekbones, dark brown eyes, lean powerfully trained build with broad shoulders and corded forearms with visible veins.",
  "wardrobe": "Plain black ribbed tank top and a thin gold chain with no pendant, dark trousers.",
  "prop": "One life-size anatomical teaching model of a long coiled digestive tube, a soft matte pale pink silicone tube folded back and forth on itself in wide loops on a flat white base, lying on the workbench. The whole surface of the coiled tube is caked under a THICK, HEAPED layer of dark brown crust with a dry cracked surface like dried mud, piled with real volume so that almost none of the pink silicone shows through. In his right hand he holds a plain unlabeled clear glass jar of white powder, tilted just above it.",
  "scene": "SAME garage workshop as the reference image: brown pegboard wall hung with wrenches and screwdrivers, an open wooden shelf of labelled glass herb jars, and a small American flag standing upright on that shelf, discreet but clearly visible and in sharp focus.",
  "posture": "Seated at his own scuffed wooden workbench, leaning slightly forward toward the camera, both forearms low near the bench top.",
  "composition": "The coiled model fills the lower two thirds of the frame and sits much closer to the lens than his face, so it is unmistakably the hero. His head and shoulders occupy the upper third and the top of his head is cropped by the top edge. Nothing else competes. The garage behind is barely readable.",
  "camera": "chest level, straight-on, camera pushed in close and slightly high toward the model",
  "state": "Start frame: the jar is tilted above the model and the first grains of white powder are about to fall. The crust is intact and dry, nothing has reacted yet, no foam anywhere.",
  "lighting": "Flat neutral daylight spilling in from the open garage door, evenly lighting his face, no warm orange cast and no yellow tint.",
  "realism": "UGC realism, real skin texture with visible pores, individual hair strands, subtle wrinkles, realistic shadows and reflections, iPhone-footage look, phone camera look not professional photography, no AI polish, no beauty smoothing, no blur anywhere, everything in sharp focus including background wall shelf and tools.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no studio, no plastic skin, no extra fingers, no supernatural lighting, no blur, no artificial lighting, no warm orange color cast, no yellow tint, no heart model, no skull model, no brain model, no thin scattered layer, no silver jewelry, no cross pendant, no second person, no foam"
}
```

## K04 · T11 · HOOK D · GERAR DO ZERO · ÂNCORA DANA MORRISON

> ### 📎 ANEXAR: **1 IMAGEM**
> **1️⃣ ÂNCORA DANA MORRISON** `producao/_ancoras/dana_morrison_ancora.jpeg`
>
> ### 🆕 GERAR DO ZERO

```json
{
  "shot_id": "K04_hook_soda_inverted",
  "reference_use": "Use the attached image ONLY for Dana Morrison's face, identity, beard, do-rag, wardrobe and the garage scene. Do NOT copy its pose or framing.",
  "identity_main": "The EXACT man from the attached reference image (Dana Morrison): Black American man in his early fifties, deep brown skin, a black satin do-rag tied over his head with the tail falling behind his left shoulder, a long full white chin beard with a darker moustache flecked with grey, angular face with high cheekbones, dark brown eyes, lean powerfully trained build with broad shoulders and corded forearms with visible veins.",
  "wardrobe": "Plain black ribbed tank top and a thin gold chain with no pendant, dark trousers.",
  "prop": "Two life-size anatomical teaching models of a human leg from hip to ankle, molded in matte cream-toned silicone, lying flat side by side on the workbench. Both models are completely clean, smooth and bare, with nothing on them at all. In his right hand he holds a plain unlabeled clear glass jug of dark caramel-colored fizzy drink, tilted just above the two models.",
  "scene": "SAME garage workshop as the reference image: brown pegboard wall hung with wrenches and screwdrivers, an open wooden shelf of labelled glass herb jars, and a small American flag standing upright on that shelf, discreet but clearly visible and in sharp focus.",
  "posture": "Seated at his own scuffed wooden workbench, leaning slightly forward toward the camera, both forearms low near the bench top.",
  "composition": "The two clean leg models fill the lower two thirds of the frame and sit much closer to the lens than his face, so they are unmistakably the hero. His head and shoulders occupy the upper third and the top of his head is cropped by the top edge. Nothing else competes. The garage behind is barely readable.",
  "camera": "chest level, straight-on, camera pushed in close and slightly high toward the two models",
  "state": "Start frame: the jug is tilted and the first drops of dark liquid are about to fall. The models are still perfectly clean, nothing has grown on them yet.",
  "lighting": "Flat neutral daylight spilling in from the open garage door, evenly lighting his face, no warm orange cast and no yellow tint.",
  "realism": "UGC realism, real skin texture with visible pores, individual hair strands, subtle wrinkles, realistic shadows and reflections, iPhone-footage look, phone camera look not professional photography, no AI polish, no beauty smoothing, no blur anywhere, everything in sharp focus including background wall shelf and tools.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no studio, no plastic skin, no extra fingers, no supernatural lighting, no blur, no artificial lighting, no warm orange color cast, no yellow tint, no heart model, no skull model, no brain model, no yellow globules in this frame, no label on the glass, no silver jewelry, no cross pendant, no second person"
}
```

## K05 · T12 · HOOK E · GERAR DO ZERO · ÂNCORA DANA MORRISON

> ### 📎 ANEXAR: **1 IMAGEM**
> **1️⃣ ÂNCORA DANA MORRISON** `producao/_ancoras/dana_morrison_ancora.jpeg`
>
> ### 🆕 GERAR DO ZERO

```json
{
  "shot_id": "K05_hook_sugar_inverted",
  "reference_use": "Use the attached image ONLY for Dana Morrison's face, identity, beard, do-rag, wardrobe and the garage scene. Do NOT copy its pose or framing.",
  "identity_main": "The EXACT man from the attached reference image (Dana Morrison): Black American man in his early fifties, deep brown skin, a black satin do-rag tied over his head with the tail falling behind his left shoulder, a long full white chin beard with a darker moustache flecked with grey, angular face with high cheekbones, dark brown eyes, lean powerfully trained build with broad shoulders and corded forearms with visible veins.",
  "wardrobe": "Plain black ribbed tank top and a thin gold chain with no pendant, dark trousers.",
  "prop": "Two life-size anatomical teaching models of a human leg from hip to ankle, molded in matte cream-toned silicone, lying flat side by side on the workbench. Both models are completely clean, smooth and bare, with nothing on them at all. In his right hand he holds a plain unlabeled clear glass jar of coarse white granulated sugar, raised high above the two models.",
  "scene": "SAME garage workshop as the reference image: brown pegboard wall hung with wrenches and screwdrivers, an open wooden shelf of labelled glass herb jars, and a small American flag standing upright on that shelf, discreet but clearly visible and in sharp focus.",
  "posture": "Seated at his own scuffed wooden workbench, leaning slightly forward toward the camera, the right arm raised so the jar is well above the bench.",
  "composition": "The two clean leg models fill the lower two thirds of the frame and sit much closer to the lens than his face, so they are unmistakably the hero. His head and shoulders occupy the upper third and the top of his head is cropped by the top edge. Nothing else competes. The garage behind is barely readable.",
  "camera": "chest level, straight-on, camera pushed in close and slightly high toward the two models",
  "state": "Start frame: the jar is tipped high and the first white grains are about to fall. The models are still perfectly clean, nothing has grown on them yet.",
  "lighting": "Flat neutral daylight spilling in from the open garage door, evenly lighting his face, no warm orange cast and no yellow tint.",
  "realism": "UGC realism, real skin texture with visible pores, individual hair strands, subtle wrinkles, realistic shadows and reflections, iPhone-footage look, phone camera look not professional photography, no AI polish, no beauty smoothing, no blur anywhere, everything in sharp focus including background wall shelf and tools.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no studio, no plastic skin, no extra fingers, no supernatural lighting, no blur, no artificial lighting, no warm orange color cast, no yellow tint, no heart model, no skull model, no brain model, no yellow globules in this frame, no label on the glass, no silver jewelry, no cross pendant, no second person"
}
```

## K06 · T2 · RECEITA A · GERAR DO ZERO · ÂNCORA DANA MORRISON

> ### 📎 ANEXAR: **1 IMAGEM**
> **1️⃣ ÂNCORA DANA MORRISON** `producao/_ancoras/dana_morrison_ancora.jpeg`
>
> ### 🆕 GERAR DO ZERO

```json
{
  "shot_id": "K06_recipe_clear_water",
  "reference_use": "Use the attached image ONLY for Dana Morrison's face, identity, beard, do-rag, wardrobe and the garage scene. Do NOT copy its pose or framing.",
  "identity_main": "The EXACT man from the attached reference image (Dana Morrison): Black American man in his early fifties, deep brown skin, a black satin do-rag tied over his head with the tail falling behind his left shoulder, a long full white chin beard with a darker moustache flecked with grey, angular face with high cheekbones, dark brown eyes, lean powerfully trained build with broad shoulders and corded forearms with visible veins.",
  "wardrobe": "Plain black ribbed tank top and a thin gold chain with no pendant, dark trousers.",
  "prop": "A tall straight plain drinking glass of completely clear water standing on the workbench, and a metal teaspoon heaped with white powder held in his right hand just above the rim of the glass.",
  "scene": "SAME garage workshop as the reference image: brown pegboard wall hung with wrenches and screwdrivers, an open wooden shelf of labelled glass herb jars, and a small American flag standing upright on that shelf, discreet but clearly visible and in sharp focus.",
  "posture": "Seated at his own scuffed wooden workbench, leaning slightly forward toward the camera, left forearm resting flat on the bench.",
  "composition": "The glass sits in the lower foreground, closer to the lens than his face, and the spoon hovers right above it. His head and shoulders occupy the upper part of the frame. Nothing else on the bench. The garage behind is barely readable.",
  "camera": "chest level, straight-on, camera close and slightly high toward the glass",
  "state": "Start frame: the water is perfectly clear and the powder is still on the spoon. Nothing has been added yet.",
  "lighting": "Flat neutral daylight spilling in from the open garage door, evenly lighting his face, no warm orange cast and no yellow tint.",
  "realism": "UGC realism, real skin texture with visible pores, individual hair strands, subtle wrinkles, realistic shadows and reflections, iPhone-footage look, phone camera look not professional photography, no AI polish, no beauty smoothing, no blur anywhere, everything in sharp focus including background wall shelf and tools.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no studio, no plastic skin, no extra fingers, no supernatural lighting, no blur, no artificial lighting, no warm orange color cast, no yellow tint, no cloudy water in this frame, no silver jewelry, no cross pendant, no second person"
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
  "keep_identical": "Keep the man exactly the same: same face, same long white chin beard, same black satin do-rag with the tail behind his left shoulder, same black ribbed tank top, same thin gold chain, same seated position and same distance from the camera. Keep the SAME garage background exactly: pegboard wall with wrenches and screwdrivers, wooden shelf of labelled herb jars, the small American flag on the shelf, same neutral daylight, same camera angle and framing.",
  "change_1": "The water inside the glass is now cloudy and pale gold instead of clear, as if powder had been stirred into it. The glass itself stays in exactly the same place.",
  "change_2": "The metal teaspoon is gone from his right hand. He now holds half a lemon, cut side down, squeezed between his fingers directly above the rim of the glass, with the first drop of juice about to fall.",
  "realism": "UGC realism, real skin texture with visible pores, iPhone-footage look, no AI polish, no beauty smoothing, no blur anywhere. Do not make his skin darker, yellowish or orangish. Do not make the colors more saturated.",
  "negative": "do not change the face, do not change the identity, do not change the background, do not change the camera angle, no captions, no subtitles, no words overlaid on the image, no plastic skin, no extra fingers, no warm orange color cast, no yellow tint, no silver jewelry, no second person"
}
```

## K08 · T4 · PROTOCOLO · EDITAR do K06

> ### 📎 ANEXAR: **1 IMAGEM**
> **1️⃣ O K06 já aprovado**
> 🚫 NUNCA anexar o K07 aqui. Os estágios saem sempre do K06 original, nunca em cascata.
>
> ### ✏️ EDITAR, muda só o líquido e as duas mãos

```json
{
  "task": "edit the attached image, keep everything identical except the changes listed",
  "keep_identical": "Keep the man exactly the same: same face, same long white chin beard, same black satin do-rag with the tail behind his left shoulder, same black ribbed tank top, same thin gold chain, same seated position and same distance from the camera. Keep the SAME garage background exactly: pegboard wall with wrenches and screwdrivers, wooden shelf of labelled herb jars, the small American flag on the shelf, same neutral daylight, same camera angle and framing.",
  "change_1": "The liquid inside the glass is now a settled warm amber, slightly translucent, filling the glass almost to the top. The glass stays in exactly the same place on the bench.",
  "change_2": "The teaspoon is gone. Both of his hands are now wrapped loosely around the glass on the bench, fingers relaxed, as if he had just set it down in front of the viewer.",
  "realism": "UGC realism, real skin texture with visible pores, iPhone-footage look, no AI polish, no beauty smoothing, no blur anywhere. Do not make his skin darker, yellowish or orangish. Do not make the colors more saturated.",
  "negative": "do not change the face, do not change the identity, do not change the background, do not change the camera angle, no captions, no subtitles, no words overlaid on the image, no plastic skin, no extra fingers, no warm orange color cast, no yellow tint, no silver jewelry, no second person"
}
```

## K09 · T5 · PONTE · GERAR DO ZERO · ÂNCORA DANA MORRISON

> ### 📎 ANEXAR: **1 IMAGEM**
> **1️⃣ ÂNCORA DANA MORRISON** `producao/_ancoras/dana_morrison_ancora.jpeg`
>
> ### 🆕 GERAR DO ZERO

```json
{
  "shot_id": "K09_bridge_close",
  "reference_use": "Use the attached image ONLY for Dana Morrison's face, identity, beard, do-rag, wardrobe and the garage scene. Do NOT copy its pose or framing.",
  "identity_main": "The EXACT man from the attached reference image (Dana Morrison): Black American man in his early fifties, deep brown skin, a black satin do-rag tied over his head with the tail falling behind his left shoulder, a long full white chin beard with a darker moustache flecked with grey, angular face with high cheekbones, dark brown eyes, broad shoulders.",
  "wardrobe": "Plain black ribbed tank top and a thin gold chain with no pendant.",
  "scene": "SAME garage workshop as the reference image, with the brown pegboard wall behind him and the edge of the wooden shelf with the small American flag visible over his shoulder, discreet but clearly visible and in sharp focus.",
  "posture": "Seated upright and leaning in close to the camera, chin level, direct and calm expression.",
  "composition": "TIGHT. Shoulders-up framing, closer than every other shot of the video. His face fills a large part of the frame and the top of his head is cropped by the top edge. The bench is out of frame and there is no prop anywhere. Very little of the garage is visible, just the pegboard and the edge of the shelf.",
  "camera": "eye level, straight-on, close talking distance",
  "state": "Start frame: speaking directly into the lens, both hands out of frame.",
  "lighting": "Flat neutral daylight spilling in from the open garage door, evenly lighting his face, no warm orange cast and no yellow tint.",
  "realism": "UGC realism, real skin texture with visible pores, individual hair strands, subtle wrinkles, realistic shadows and reflections, iPhone-footage look, phone camera look not professional photography, no AI polish, no beauty smoothing, no blur anywhere, everything in sharp focus including the background wall and shelf.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no studio, no plastic skin, no extra fingers, no supernatural lighting, no blur, no artificial lighting, no warm orange color cast, no yellow tint, no props, no silver jewelry, no cross pendant, no second person"
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
  "keep_identical": "Keep the man exactly the same: same face, same long white chin beard, same black satin do-rag with the tail behind his left shoulder, same black ribbed tank top, same thin gold chain, same head position, same expression, same distance from the camera. Keep the SAME garage background exactly: pegboard wall, the edge of the wooden shelf with the small American flag, same neutral daylight, same camera angle and framing.",
  "change_1": "His right hand now comes up into the bottom of the frame at chest height with two fingers extended in a small counting gesture. Nothing else moves.",
  "realism": "UGC realism, real skin texture with visible pores, iPhone-footage look, no AI polish, no beauty smoothing, no blur anywhere. Do not make his skin darker, yellowish or orangish. Do not make the colors more saturated.",
  "negative": "do not change the face, do not change the identity, do not change the background, do not change the camera angle, no captions, no subtitles, no words overlaid on the image, no plastic skin, no extra fingers, no warm orange color cast, no yellow tint, no props, no silver jewelry, no second person"
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
  "keep_identical": "Keep the man exactly the same: same face, same long white chin beard, same black satin do-rag with the tail behind his left shoulder, same black ribbed tank top, same thin gold chain, same expression. Keep the SAME garage background exactly: pegboard wall, the edge of the wooden shelf with the small American flag, same neutral daylight, same camera angle.",
  "change_1": "Push the camera about ten percent closer so the framing tightens slightly and his face becomes even more dominant. Do not change the angle or the height of the camera.",
  "change_2": "His right hand comes up into the bottom of the frame at chest height, palm open toward the lens in a natural offering gesture.",
  "realism": "UGC realism, real skin texture with visible pores, iPhone-footage look, no AI polish, no beauty smoothing, no blur anywhere. Do not make his skin darker, yellowish or orangish. Do not make the colors more saturated.",
  "negative": "do not change the face, do not change the identity, do not change the background, no captions, no subtitles, no words overlaid on the image, no plastic skin, no extra fingers, no warm orange color cast, no yellow tint, no props, no silver jewelry, no second person"
}
```

## K12 · T8 · FOLLOW GATE · EDITAR do K09

> ### 📎 ANEXAR: **1 IMAGEM**
> **1️⃣ O K09 já aprovado**
> 🚫 NUNCA anexar o K11 aqui. Estágios sempre a partir do K09 original.
>
> ### ✏️ EDITAR, muda só o braço direito, apontando

```json
{
  "task": "edit the attached image, keep everything identical except the change listed",
  "keep_identical": "Keep the man exactly the same: same face, same long white chin beard, same black satin do-rag with the tail behind his left shoulder, same black ribbed tank top, same thin gold chain, same head position, same distance from the camera. Keep the SAME garage background exactly: pegboard wall, the edge of the wooden shelf with the small American flag, same neutral daylight, same camera angle and framing.",
  "change_1": "His right arm comes up into the frame and he points his index finger straight at the lens, close to the camera, in a direct and friendly way. Nothing else moves.",
  "realism": "UGC realism, real skin texture with visible pores, iPhone-footage look, no AI polish, no beauty smoothing, no blur anywhere. Do not make his skin darker, yellowish or orangish. Do not make the colors more saturated.",
  "negative": "do not change the face, do not change the identity, do not change the background, do not change the camera angle, no captions, no subtitles, no words overlaid on the image, no plastic skin, no extra fingers, no warm orange color cast, no yellow tint, no props, no silver jewelry, no second person"
}
```

---

## Bloco global de vídeo

Colar em todo prompt de vídeo, com a fala do take no lugar da marcação:

```text
o avatar (homem) fala em inglês com sotaque americano de Dana Morrison, voz autêntica, dinâmica, apaixonada e emocional, como se exigisse ser ouvida, a seguinte frase: "[FALA EXATA DO ROTEIRO]"

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: [ação ENXUTA, só o que acontece]

câmera: [fixa / leve push-in]

som ambiente: garagem tranquila com um leve ruído de rua ao longe, sem música
```

---

# Prompts de vídeo

### V01 · T1 · usa K01

```text
o avatar (homem) fala em inglês com sotaque americano de Dana Morrison, voz autêntica, dinâmica, apaixonada e emocional, como se exigisse ser ouvida, a seguinte frase: "This is what baking soda does to the fat on a woman's legs at twenty five, and at fifty five."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ele inclina o pote e o pó branco cai sobre os dois modelos ao mesmo tempo. A espuma branca sobe nos dois. Na esquerda a camada amarela some quase toda, na direita quase nada se move.

câmera: fixa

som ambiente: garagem tranquila com um leve ruído de rua ao longe, sem música
```

### V02 · T9 · usa K02

```text
o avatar (homem) fala em inglês com sotaque americano de Dana Morrison, voz autêntica, dinâmica, apaixonada e emocional, como se exigisse ser ouvida, a seguinte frase: "This is what baking soda does to the fat on a woman's belly after forty. Watch."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ele inclina o pote e o pó branco cai sobre o modelo. A espuma branca sobe, ele passa a mão por cima e a camada amarela sai, deixando a superfície lisa.

câmera: fixa

som ambiente: garagem tranquila com um leve ruído de rua ao longe, sem música
```

### V03 · T10 · usa K03

```text
o avatar (homem) fala em inglês com sotaque americano de Dana Morrison, voz autêntica, dinâmica, apaixonada e emocional, como se exigisse ser ouvida, a seguinte frase: "This is what baking soda does to what is stuck in a woman's gut after forty. Watch."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ele inclina o pote e o pó branco cai sobre o modelo. A crosta escura borbulha alto e se solta em placas, que escorregam para a bancada.

câmera: fixa

som ambiente: garagem tranquila com um leve ruído de rua ao longe, sem música
```

### V04 · T11 · usa K04

```text
o avatar (homem) fala em inglês com sotaque americano de Dana Morrison, voz autêntica, dinâmica, apaixonada e emocional, como se exigisse ser ouvida, a seguinte frase: "This is what one soda a day does to the fat on a woman's legs after forty. Watch."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ele inclina a jarra e o líquido escuro escorre sobre os dois modelos. Onde o líquido encosta, glóbulos amarelos brotam e crescem depressa.

câmera: fixa

som ambiente: garagem tranquila com um leve ruído de rua ao longe, sem música
```

### V05 · T12 · usa K05

```text
o avatar (homem) fala em inglês com sotaque americano de Dana Morrison, voz autêntica, dinâmica, apaixonada e emocional, como se exigisse ser ouvida, a seguinte frase: "This is what sugar does to the fat on a woman's legs after forty. Watch."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ele vira o pote e o açúcar cai de cima em cascata. Onde os grãos encostam, a camada amarela infla e engrossa.

câmera: fixa

som ambiente: garagem tranquila com um leve ruído de rua ao longe, sem música
```

### V06 · T2 · usa K06

```text
o avatar (homem) fala em inglês com sotaque americano de Dana Morrison, voz autêntica, dinâmica, apaixonada e emocional, como se exigisse ser ouvida, a seguinte frase: "A teaspoon of baking soda and a pinch of cinnamon in a glass of warm water."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ele vira a colher e o pó branco cai dentro do copo. A água fica turva na hora.

câmera: fixa

som ambiente: garagem tranquila com um leve ruído de rua ao longe, sem música
```

### V07 · T3 · usa K07

```text
o avatar (homem) fala em inglês com sotaque americano de Dana Morrison, voz autêntica, dinâmica, apaixonada e emocional, como se exigisse ser ouvida, a seguinte frase: "Then the juice of half a lemon. Stir it until the water turns cloudy and gold."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ele aperta o meio limão e o suco escorre dentro do copo.

câmera: fixa

som ambiente: garagem tranquila com um leve ruído de rua ao longe, sem música
```

### V08 · T4 · usa K08

```text
o avatar (homem) fala em inglês com sotaque americano de Dana Morrison, voz autêntica, dinâmica, apaixonada e emocional, como se exigisse ser ouvida, a seguinte frase: "Drink it slow, on an empty stomach, every morning. The women who ask me about this always notice their legs first."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ele desliza o copo alguns centímetros na direção da câmera e solta as mãos.

câmera: fixa

som ambiente: garagem tranquila com um leve ruído de rua ao longe, sem música
```

### V09 · T5 · usa K09

```text
o avatar (homem) fala em inglês com sotaque americano de Dana Morrison, voz autêntica, dinâmica, apaixonada e emocional, como se exigisse ser ouvida, a seguinte frase: "That drink works. But after forty, three things hold that fat: your hormones, your metabolism, and your gut. It only touches the gut."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ele fala direto para a lente, sem se mexer do lugar.

câmera: fixa

som ambiente: garagem tranquila com um leve ruído de rua ao longe, sem música
```

### V10 · T6 · usa K10

```text
o avatar (homem) fala em inglês com sotaque americano de Dana Morrison, voz autêntica, dinâmica, apaixonada e emocional, como se exigisse ser ouvida, a seguinte frase: "If yours is the hormone one, or the metabolism one, you can drink this all month and your legs will not change."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ele mantém os dois dedos levantados e depois abaixa a mão devagar.

câmera: fixa

som ambiente: garagem tranquila com um leve ruído de rua ao longe, sem música
```

### V11 · T7 · usa K11

```text
o avatar (homem) fala em inglês com sotaque americano de Dana Morrison, voz autêntica, dinâmica, apaixonada e emocional, como se exigisse ser ouvida, a seguinte frase: "It was never what you drink. It is which of the three is yours. Comment yes and I will send you the FityWell quiz."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ele abre a mão na direção da lente enquanto fala.

câmera: leve push-in

som ambiente: garagem tranquila com um leve ruído de rua ao longe, sem música
```

### V12 · T8 · usa K12

```text
o avatar (homem) fala em inglês com sotaque americano de Dana Morrison, voz autêntica, dinâmica, apaixonada e emocional, como se exigisse ser ouvida, a seguinte frase: "But follow me first, or it will not let me reach you. Two minutes and you will know."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ele aponta o dedo para a lente e mantém o gesto até o fim da fala.

câmera: leve push-in

som ambiente: garagem tranquila com um leve ruído de rua ao longe, sem música
```

---

## Mapa de âncoras

| Keyframe | Referências a anexar | Modelo |
|---|---|---|
| K01 | ÂNCORA DANA MORRISON | Nano Banana 2, 9:16 |
| K02 | ÂNCORA DANA MORRISON | Nano Banana 2, 9:16 |
| K03 | ÂNCORA DANA MORRISON | Nano Banana 2, 9:16 |
| K04 | ÂNCORA DANA MORRISON | Nano Banana 2, 9:16 |
| K05 | ÂNCORA DANA MORRISON | Nano Banana 2, 9:16 |
| K06 | ÂNCORA DANA MORRISON | Nano Banana 2, 9:16 |
| K07 | o K06 aprovado | Nano Banana 2, 9:16 |
| K08 | o K06 aprovado | Nano Banana 2, 9:16 |
| K09 | ÂNCORA DANA MORRISON | Nano Banana 2, 9:16 |
| K10 | o K09 aprovado | Nano Banana 2, 9:16 |
| K11 | o K09 aprovado | Nano Banana 2, 9:16 |
| K12 | o K09 aprovado | Nano Banana 2, 9:16 |

Vídeo: Veo 3.1 Lite, Lower Priority, 8 segundos, 3 variações, imagem sempre como INITIAL FRAME.

---

## Montagem no CapCut

1. **Escolher UM gancho por vídeo.** Cada vídeo finalizado é V01, V02, V03, V04 ou V05 na abertura,
   seguido sempre da mesma sequência V06, V07, V08, V09, V10, V11 e V12.
2. Cortar cada clipe no fim da fala, sem sobra de silêncio. O corte do gancho entra no instante em
   que a reação está no auge, nunca depois dela terminar.
3. Legenda queimada em todos os takes, uma linha por vez, palavra destacada em amarelo na keyword.
4. No T7, quando ele disser `yes`, subir a palavra `YES` grande na tela por um segundo.
5. Sem música. Só o som ambiente que veio do clipe.
6. Exportar em 9:16, 1080 por 1920.

---

## Gates de qualidade

1. [ ] O herói está no lower foreground, mais perto da lente que o rosto dele, em K01 a K05.
2. [ ] A camada amarela saiu **volumosa**, não uma película fina. Se saiu fina, regerar.
3. [ ] O modelo anatômico saiu com a forma pedida e não virou coração, crânio ou cérebro.
4. [ ] A bandeirinha dos EUA aparece e está em foco em todos os doze keyframes.
5. [ ] Nenhum keyframe tem celular, tela, rótulo de marca ou qualquer coisa que leia como produto.
6. [ ] A barba branca comprida e o do-rag preto estão idênticos nos doze keyframes.
7. [ ] Zero blur em qualquer imagem, inclusive no fundo.
8. [ ] Luz neutra de dia. Nenhuma imagem saiu com cast quente ou amarelado.
9. [ ] A fala de cada V bate palavra por palavra com o take do `ROTEIRO.md`.
10. [ ] O take mais fechado do vídeo é o do CTA.
11. [ ] Nenhum take sugere que ela não se esforçou o bastante.
12. [ ] `python checar_entrega.py producao/fitywell_pernas` fechou sem FALHA.
