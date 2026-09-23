# Dana Morrison | Ângulo 2 (FityWell) | Pacote de Prompts

Vídeo modelo: `de823669-024c-4538-a012-8553ea7f146f.mp4` (22,15 s, 5 cenas)

Referência de identidade: **fingerprint** (grade de estúdio, vários ângulos de rosto/corpo/pele),
anexada pelo Luigi junto com o `.mp4`. Trava só **identidade, corpo, pele e cabelo**. Cenário, roupa
e ângulo de câmera nascem do texto de cada `K`, não da imagem. Ver `AVATAR_QUEUE.md` e
`GANCHOS_VISUAIS.md` seção "Cenário e câmera agora nascem por gancho".

Ganchos escolhidos pelo Luigi: **1 (pia da cozinha), 2 (ralo em macro extremo), 5 (água da aveia de
molho), 7 (bueiro da rua, de cima) e 9 (direto na lata de lixo)**.

Funil: comment `yes` → DM → link do quiz FityWell

Avatar 1 de 3 da fila (`AVATAR_QUEUE.md`).

---

## Índice de geração

| Take | Keyframe | Anexar | Ação de geração |
|---|---|---|---|
| T1 (gancho 1) | K01 | FINGERPRINT DANA MORRISON | GERAR DO ZERO. A pia da cozinha |
| T1 (gancho 2) | K02 | FINGERPRINT DANA MORRISON | GERAR DO ZERO. O ralo, em macro extremo |
| T1 (gancho 5) | K03 | FINGERPRINT DANA MORRISON | GERAR DO ZERO. Água da aveia de molho |
| T1 (gancho 7) | K04 | FINGERPRINT DANA MORRISON | GERAR DO ZERO. O bueiro da rua, visto de cima |
| T1 (gancho 9) | K05 | FINGERPRINT DANA MORRISON | GERAR DO ZERO. Direto na lata de lixo |
| T2 | K06 | FINGERPRINT DANA MORRISON | GERAR DO ZERO. Pote de vidro na bancada da cozinha |
| T3 | K07 | FINGERPRINT DANA MORRISON | GERAR DO ZERO. Modelo anatômico de intestino com crosta |
| T4 | K08 | o K07 aprovado | EDITAR do K07. Crosta já parcialmente solta, pote vazio na mão |
| T5 | K09 | FINGERPRINT DANA MORRISON | GERAR DO ZERO. Close de CTA, sem prop |
| T6 | K10 | o K09 aprovado | EDITAR do K09. Muda só o gesto de mão |
| T7 | K11 | o K09 aprovado | EDITAR do K09. Muda só o gesto de mão e a distância |
| T8 | K12 | o K09 aprovado | EDITAR do K09. Muda só o braço direito, apontando |

Regra de bolso: **GERAR DO ZERO anexa a fingerprint. EDITAR anexa uma imagem só, o keyframe de
origem.** 🚫 Nunca anexar um keyframe editado como origem de outro.

Cada vídeo finalizado usa **um** dos cinco K de hook (K01 a K05) seguido sempre de K06 a K12. Cinco
vídeos, 10 clipes compartilhados entre eles.

---

## Trava de identidade e continuidade

- Homem negro americano no início dos cinquenta, pele marrom escura.
- **Do-rag preto de cetim** amarrado na cabeça, aba caindo atrás do ombro esquerdo.
- **Barba do queixo comprida e branca**, cheia, bigode escuro salpicado de grisalho. Nunca encurtar.
- Rosto magro e anguloso, maçãs altas, olhos castanhos escuros, olhar direto e levemente urgente.
- Corpo seco e treinado, ombros largos, antebraços com veias marcadas, mãos grandes e calejadas.
- Pele com textura real, poros visíveis, linhas na testa, pés de galinha, sem maquiagem.
- **Regata canelada PRETA**, corrente fina de OURO sem pingente, calça escura. **Sem cruz.**
- Luz **neutra de dia nublado, nunca quente**. Zero blur, tudo em foco nítido.

---

## Trava do prop herói (T1, líquido amiláceo)

```text
A pale cloudy starchy liquid, opaque and milky, poured or streaming from a container. Where it
lands, it forms visible foam and carries along small solid pieces from the ingredient (rice grains,
oat flakes) that stick briefly to whatever it hits before being carried away.
```

## Trava do prop herói (T3/T4, modelo anatômico)

```text
One soft matte silicone teaching model of a digestive tube, a pale dusty rose tube folded back and
forth on itself in wide loops on a flat white base, resting on the kitchen counter. The whole
surface of the coiled tube is caked under a THICK, HEAPED layer of dried crust, cracked like dried
clay in a warm brown tone, piled with real volume so that almost none of the tube shows through.
```

**A forma vai descrita no positivo, nunca negada.** Nome de órgão no `negative` injeta o conceito
(trava do `PLAYBOOK_FITYWELL.md` §7).

## Trava da 2ª pessoa (REF-A)

**Não se aplica.** Sem 2ª pessoa viva em nenhum take. Ver `AVATAR_QUEUE.md`.

---

# Prompts de imagem

## K01 · T1 · HOOK, gancho 1 (a pia da cozinha) · GERAR DO ZERO · FINGERPRINT DANA MORRISON

> ### 📎 ANEXAR: **1 IMAGEM**
> **1️⃣ FINGERPRINT DANA MORRISON** (grade de estúdio, vários ângulos)
>
> ### 🆕 GERAR DO ZERO

```json
{
  "shot_id": "K01_hook_kitchen_sink",
  "reference_use": "Use the attached fingerprint sheet ONLY for Dana Morrison's face, identity, hair, skin texture and body build, seen from multiple angles. Do NOT copy any wardrobe, background, pose or lighting from it.",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "identity_main": "The EXACT man from the attached fingerprint reference (Dana Morrison): Black American man in his early fifties, dark brown skin, a black satin do-rag tied on his head with the tail falling behind his left shoulder, a long full white chin beard with a dark moustache flecked with grey, a lean angular face with high cheekbones, direct and slightly urgent dark brown eyes, a lean trained build with wide shoulders and defined forearms with visible veins, large calloused hands, real skin texture with visible pores, deep forehead lines and crow's feet, no makeup.",
  "wardrobe": "A black ribbed tank top, a thin gold chain necklace with no pendant, dark trousers. No cross.",
  "prop": "A dark metal pot held in both hands, tilted over the sink, pouring a pale cloudy starchy water in a thick continuous stream into the metal sink basin. Where the stream hits the sink, white foam is building up around the drain and a few stray grains of cooked rice are caught against the drain grate.",
  "scene": "A modest, lived-in American kitchen: a metal sink built into a pale granite countertop, a window above the sink with a potted herb on the sill, a stack of folded dish towels to one side, a small American flag pin stuck into a cork board on the wall, discreet but clearly visible and in sharp focus.",
  "posture": "Standing at the sink, upper body leaning slightly forward and down toward the drain.",
  "composition": "The sink, the pouring stream and the foaming drain fill the lower two thirds of the frame, closer to the lens than his face. His head and shoulders occupy the upper third, top of the do-rag cropped by the top edge. Nothing else competes.",
  "camera": "slightly below counter height, angled a little upward, soft backlight from the window behind the stream",
  "state": "Start frame: the pot is tilted and the stream is already flowing, foam just starting to form around the drain, steam faintly visible.",
  "lighting": "Flat neutral daylight from the window under an overcast sky, soft backlight outlining the steam, no warm orange cast and no yellow tint.",
  "realism": "UGC realism, real skin texture with visible pores, individual hair strands, subtle wrinkles, realistic shadows and reflections, iPhone-footage look, phone camera look not professional photography, no AI polish, no beauty smoothing, no blur anywhere, everything in sharp focus including the window and the sink.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no studio, no plastic skin, no extra fingers, no supernatural lighting, no blur, no artificial lighting, no warm orange color cast, no yellow tint, no jewelry besides the thin gold chain, no cross, no second person, no brand label"
}
```

## K02 · T1 · HOOK, gancho 2 (ralo em macro extremo) · GERAR DO ZERO · FINGERPRINT DANA MORRISON

> ### 📎 ANEXAR: **1 IMAGEM**
> **1️⃣ FINGERPRINT DANA MORRISON**
>
> ### 🆕 GERAR DO ZERO

```json
{
  "shot_id": "K02_hook_drain_macro",
  "reference_use": "Use the attached fingerprint sheet ONLY for Dana Morrison's face, identity, hair, skin texture and body build. Do NOT copy any wardrobe, background, pose or lighting from it.",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "identity_main": "The EXACT man from the attached fingerprint reference (Dana Morrison): Black American man in his early fifties, dark brown skin, a black satin do-rag tied on his head with the tail falling behind his left shoulder, a long full white chin beard with a dark moustache flecked with grey, a lean angular face with high cheekbones, direct and slightly urgent dark brown eyes, a lean trained build with wide shoulders and defined forearms with visible veins, large calloused hands, real skin texture with visible pores, deep forehead lines and crow's feet, no makeup.",
  "wardrobe": "A black ribbed tank top, a thin gold chain necklace with no pendant, dark trousers. No cross.",
  "prop": "A round metal floor drain set into the concrete, its grates filling almost the entire lower frame. A pale cloudy starchy stream pours in from above, out of focus at the very top edge where it enters frame, gaining sharp focus only where it hits the grate: white foam blooms at the point of impact and spreads in concentric ripples, draining through the slots and carrying a few grains of rice that catch briefly on the metal bars.",
  "scene": "Smooth concrete floor of a covered outdoor utility area. A small American flag sticker is fixed to the edge of a metal support post just visible at the top corner of the frame, discreet but clearly visible and in sharp focus. No landscaping competing in frame otherwise.",
  "posture": "The man is barely in frame, only the lower edge of his tank top and one calloused hand holding the pot visible at the very top corner.",
  "composition": "Worm's-eye macro, the drain grate and the foaming impact point dominate almost the entire frame. His face is mostly out of frame.",
  "camera": "worm's-eye, nearly at floor level, extreme macro on the drain",
  "state": "Start frame: the stream is mid-fall, about to hit the grate, first foam just beginning to form at the point of impact.",
  "lighting": "Flat neutral daylight under an overcast sky, no warm orange cast and no yellow tint.",
  "realism": "UGC realism, real texture on the wet concrete and metal grate, iPhone-footage look, phone camera look not professional photography, no AI polish, no blur anywhere, everything in sharp focus at the point of impact.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no studio, no plastic skin, no extra fingers, no supernatural lighting, no blur, no artificial lighting, no warm orange color cast, no yellow tint, no jewelry besides the thin gold chain, no cross, no second person, no brand label"
}
```

## K03 · T1 · HOOK, gancho 5 (água da aveia de molho) · GERAR DO ZERO · FINGERPRINT DANA MORRISON

> ### 📎 ANEXAR: **1 IMAGEM**
> **1️⃣ FINGERPRINT DANA MORRISON**
>
> ### 🆕 GERAR DO ZERO

```json
{
  "shot_id": "K03_hook_oat_water",
  "reference_use": "Use the attached fingerprint sheet ONLY for Dana Morrison's face, identity, hair, skin texture and body build. Do NOT copy any wardrobe, background, pose or lighting from it.",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "identity_main": "The EXACT man from the attached fingerprint reference (Dana Morrison): Black American man in his early fifties, dark brown skin, a black satin do-rag tied on his head with the tail falling behind his left shoulder, a long full white chin beard with a dark moustache flecked with grey, a lean angular face with high cheekbones, direct and slightly urgent dark brown eyes, a lean trained build with wide shoulders and defined forearms with visible veins, large calloused hands, real skin texture with visible pores, deep forehead lines and crow's feet, no makeup.",
  "wardrobe": "A black ribbed tank top, a thin gold chain necklace with no pendant, dark trousers. No cross.",
  "prop": "A deep ceramic bowl of soaking oats held tilted in both hands, pouring a thick, milky, slow-moving liquid in a continuous viscous stream over a floor drain below. Whole oat flakes slide along the rim of the bowl and drop with the liquid, some catching on the drain grate.",
  "scene": "A kitchen counter near a large window in the morning, rows of glass jars filled with grains lined up along the counter, a small American flag in a little table stand on the windowsill, discreet but clearly visible and in sharp focus, soft morning light through the glass.",
  "posture": "Standing at the counter, upper body angled down and forward over the drain, one arm extended holding the bowl.",
  "composition": "The bowl, the thick stream and the drain fill the lower two thirds of the frame, closer to the lens than his face. His head and shoulders occupy the upper third.",
  "camera": "high angle, diagonal over-the-shoulder, looking down at the liquid",
  "state": "Start frame: the bowl is tilted and the thick stream is already flowing, oat flakes visible sliding along its edge, nothing has fully drained yet.",
  "lighting": "Flat neutral daylight from the large window, no warm orange cast and no yellow tint.",
  "realism": "UGC realism, real skin texture with visible pores, individual hair strands, subtle wrinkles, iPhone-footage look, phone camera look not professional photography, no AI polish, no blur anywhere, everything in sharp focus including the jars on the counter.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no studio, no plastic skin, no extra fingers, no supernatural lighting, no blur, no artificial lighting, no warm orange color cast, no yellow tint, no jewelry besides the thin gold chain, no cross, no second person, no brand label"
}
```

## K04 · T1 · HOOK, gancho 7 (bueiro da rua, de cima) · GERAR DO ZERO · FINGERPRINT DANA MORRISON

> ### 📎 ANEXAR: **1 IMAGEM**
> **1️⃣ FINGERPRINT DANA MORRISON**
>
> ### 🆕 GERAR DO ZERO

```json
{
  "shot_id": "K04_hook_storm_drain_top",
  "reference_use": "Use the attached fingerprint sheet ONLY for Dana Morrison's face, identity, hair, skin texture and body build. Do NOT copy any wardrobe, background, pose or lighting from it.",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "identity_main": "The EXACT man from the attached fingerprint reference (Dana Morrison): Black American man in his early fifties, dark brown skin, a black satin do-rag tied on his head with the tail falling behind his left shoulder, a long full white chin beard with a dark moustache flecked with grey, a lean angular face with high cheekbones, direct and slightly urgent dark brown eyes, a lean trained build with wide shoulders and defined forearms with visible veins, large calloused hands, real skin texture with visible pores, deep forehead lines and crow's feet, no makeup.",
  "wardrobe": "A black ribbed tank top, a thin gold chain necklace with no pendant, dark trousers. No cross.",
  "prop": "A dark metal pot held high above a street storm drain, pouring a pale cloudy starchy stream from a greater height than usual so it visibly widens and breaks apart in the air before hitting the grate, splashing outward and wetting the surrounding concrete in several directions.",
  "scene": "A residential sidewalk in front of a house, trimmed green lawn and a section of white picket fence in the background, a small American flag stuck upright in the lawn near the sidewalk edge, discreet but clearly visible and in sharp focus, ordinary American suburban street.",
  "posture": "Standing over the drain, arm raised high, pot tilted well above the grate.",
  "composition": "Bird's-eye, top-down. The drain sits centered in frame like a clock, the spreading splash pattern visible around it. His hand and forearm enter frame from one side, the rest of him out of frame.",
  "camera": "directly overhead, zenithal, top-down",
  "state": "Start frame: the stream is mid-air, already breaking apart into droplets, about to hit the grate.",
  "lighting": "Flat neutral daylight under an overcast sky, no warm orange cast and no yellow tint.",
  "realism": "UGC realism, real texture on the wet concrete, lawn and fence, iPhone-footage look, phone camera look not professional photography, no AI polish, no blur anywhere, everything in sharp focus.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no studio, no plastic skin, no extra fingers, no supernatural lighting, no blur, no artificial lighting, no warm orange color cast, no yellow tint, no jewelry besides the thin gold chain, no cross, no second person, no brand label, no people in background, no cars"
}
```

## K05 · T1 · HOOK, gancho 9 (direto na lata de lixo) · GERAR DO ZERO · FINGERPRINT DANA MORRISON

> ### 📎 ANEXAR: **1 IMAGEM**
> **1️⃣ FINGERPRINT DANA MORRISON**
>
> ### 🆕 GERAR DO ZERO
>
> ⚠️ Demo invertida, marcada em `GANCHOS_VISUAIS.md`. Escolha do Luigi, produzir normalmente.

```json
{
  "shot_id": "K05_hook_trash_can",
  "reference_use": "Use the attached fingerprint sheet ONLY for Dana Morrison's face, identity, hair, skin texture and body build. Do NOT copy any wardrobe, background, pose or lighting from it.",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "identity_main": "The EXACT man from the attached fingerprint reference (Dana Morrison): Black American man in his early fifties, dark brown skin, a black satin do-rag tied on his head with the tail falling behind his left shoulder, a long full white chin beard with a dark moustache flecked with grey, a lean angular face with high cheekbones, direct and slightly urgent dark brown eyes, a lean trained build with wide shoulders and defined forearms with visible veins, large calloused hands, real skin texture with visible pores, deep forehead lines and crow's feet, no makeup.",
  "wardrobe": "A black ribbed tank top, a thin gold chain necklace with no pendant, dark trousers. No cross.",
  "prop": "A dark metal pot tilted over an open household trash can, pouring a pale cloudy starchy stream down onto ordinary household waste already inside the can (food scraps and paper, described only in general terms, nothing graphic). Where the liquid lands, it darkens quickly as it mixes with what is already there, forming a shallow murky pool with no drainage and no reaction.",
  "scene": "The side exterior wall of a plain house, smooth light-colored siding, an ordinary household trash can standing on the concrete, a small American flag decal fixed to the siding just above the can, discreet but clearly visible and in sharp focus.",
  "posture": "Standing beside the trash can, upper body leaning over it, pot tilted downward.",
  "composition": "Looking down into the can, the pouring stream and the darkening pool fill most of the frame. His hand and forearm are visible at the top edge, face mostly out of frame.",
  "camera": "high angle, looking down into the can, harder and colder framing than the rest of the set",
  "state": "Start frame: the stream is mid-pour, just starting to darken where it meets the waste inside.",
  "lighting": "Flat neutral daylight under an overcast sky, no warm orange cast and no yellow tint.",
  "realism": "UGC realism, real texture on the siding and the trash can, iPhone-footage look, phone camera look not professional photography, no AI polish, no blur anywhere, everything in sharp focus.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no studio, no plastic skin, no extra fingers, no supernatural lighting, no blur, no artificial lighting, no warm orange color cast, no yellow tint, no jewelry besides the thin gold chain, no cross, no second person, no brand label, no graphic or rotting waste detail"
}
```

## K06 · T2 · CORREÇÃO · GERAR DO ZERO · FINGERPRINT DANA MORRISON

> ### 📎 ANEXAR: **1 IMAGEM**
> **1️⃣ FINGERPRINT DANA MORRISON**
>
> ### 🆕 GERAR DO ZERO

```json
{
  "shot_id": "K06_correction_jar",
  "reference_use": "Use the attached fingerprint sheet ONLY for Dana Morrison's face, identity, hair, skin texture and body build. Do NOT copy any wardrobe, background, pose or lighting from it.",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "identity_main": "The EXACT man from the attached fingerprint reference (Dana Morrison): Black American man in his early fifties, dark brown skin, a black satin do-rag tied on his head with the tail falling behind his left shoulder, a long full white chin beard with a dark moustache flecked with grey, a lean angular face with high cheekbones, direct and slightly urgent dark brown eyes, a lean trained build with wide shoulders and defined forearms with visible veins, large calloused hands, real skin texture with visible pores, deep forehead lines and crow's feet, no makeup.",
  "wardrobe": "A black ribbed tank top, a thin gold chain necklace with no pendant, dark trousers. No cross.",
  "prop": "A dark metal pot tilted in his hands, pouring the same pale cloudy starchy liquid in a controlled stream into a plain unlabeled clear glass jar standing on the counter, already a third full.",
  "scene": "The same modest lived-in American kitchen: pale granite countertop, a window with a potted herb on the sill, a stack of folded dish towels, a small American flag pin on the cork board behind him, discreet but clearly visible and in sharp focus.",
  "posture": "Standing at the counter, leaning slightly forward, pot tilted over the jar.",
  "composition": "The jar and the pouring stream sit in the lower foreground, closer to the lens than his face. His head and shoulders occupy the upper part of the frame.",
  "camera": "chest level, straight-on, camera close to the jar",
  "state": "Start frame: the jar is a third full, the stream still flowing steadily into it.",
  "lighting": "Flat neutral daylight from the window under an overcast sky, no warm orange cast and no yellow tint.",
  "realism": "UGC realism, real skin texture with visible pores, individual hair strands, subtle wrinkles, iPhone-footage look, phone camera look not professional photography, no AI polish, no blur anywhere, everything in sharp focus including the window.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no studio, no plastic skin, no extra fingers, no supernatural lighting, no blur, no artificial lighting, no warm orange color cast, no yellow tint, no jewelry besides the thin gold chain, no cross, no second person, no brand label"
}
```

## K07 · T3 · MECANISMO / DEMO · GERAR DO ZERO · FINGERPRINT DANA MORRISON

> ### 📎 ANEXAR: **1 IMAGEM**
> **1️⃣ FINGERPRINT DANA MORRISON**
>
> ### 🆕 GERAR DO ZERO

```json
{
  "shot_id": "K07_mechanism_gut_model",
  "reference_use": "Use the attached fingerprint sheet ONLY for Dana Morrison's face, identity, hair, skin texture and body build. Do NOT copy any wardrobe, background, pose or lighting from it.",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "identity_main": "The EXACT man from the attached fingerprint reference (Dana Morrison): Black American man in his early fifties, dark brown skin, a black satin do-rag tied on his head with the tail falling behind his left shoulder, a long full white chin beard with a dark moustache flecked with grey, a lean angular face with high cheekbones, direct and slightly urgent dark brown eyes, a lean trained build with wide shoulders and defined forearms with visible veins, large calloused hands, real skin texture with visible pores, deep forehead lines and crow's feet, no makeup.",
  "wardrobe": "A black ribbed tank top, a thin gold chain necklace with no pendant, dark trousers. No cross.",
  "prop": "One soft matte silicone teaching model of a digestive tube, a pale dusty rose tube folded back and forth on itself in wide loops on a flat white base, resting on the kitchen counter. The whole surface of the coiled tube is caked under a THICK, HEAPED layer of dried crust, cracked like dried clay in a warm brown tone, piled with real volume so that almost none of the tube shows through. In his right hand he holds the glass jar from K06, tilted just above it, pouring the starchy liquid onto the crust.",
  "scene": "The same modest lived-in American kitchen: pale granite countertop, a window with a potted herb on the sill, a small American flag pin on the cork board behind him, discreet but clearly visible and in sharp focus.",
  "posture": "Standing at the counter, leaning forward toward the model, jar tilted above it.",
  "composition": "The coiled model fills the lower two thirds of the frame, closer to the lens than his face, unmistakably the hero. His head and shoulders occupy the upper third.",
  "camera": "chest level, straight-on, camera pushed in close and slightly high toward the model",
  "state": "Start frame: the jar is tilted and the first liquid is about to touch the crust. The crust is intact and dry, nothing has reacted yet.",
  "lighting": "Flat neutral daylight from the window under an overcast sky, no warm orange cast and no yellow tint.",
  "realism": "UGC realism, real skin texture with visible pores, individual hair strands, subtle wrinkles, iPhone-footage look, phone camera look not professional photography, no AI polish, no blur anywhere, everything in sharp focus.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no studio, no plastic skin, no extra fingers, no supernatural lighting, no blur, no artificial lighting, no warm orange color cast, no yellow tint, no de-aging, no skin smoothing, no jewelry besides the thin gold chain, no cross, no second person"
}
```

## K08 · T4 · VALIDAÇÃO · EDITAR do K07

> ### 📎 ANEXAR: **1 IMAGEM**
> **1️⃣ O K07 já aprovado**
> 🚫 NUNCA anexar a fingerprint aqui.
>
> ### ✏️ EDITAR, muda só o estado do modelo e as mãos

```json
{
  "task": "edit the attached image, keep everything identical except the changes listed",
  "keep_identical": "Keep the man exactly the same: same face, same do-rag, same long white chin beard, same black tank top, same thin gold chain, same standing position and same distance from the camera. Keep the SAME kitchen background exactly: the countertop, the window, the cork board with the flag pin, same neutral daylight, same camera angle and framing.",
  "change_1": "The crust on the coiled model is now partly broken apart, large cracked pieces lifted and peeling away in several places, revealing smooth pink tissue underneath where the crust has come off. Some loose crust pieces sit on the counter beside the model.",
  "change_2": "The glass jar is gone from his hand. He now holds it empty, lowered at his side, mostly out of frame, and looks up toward the camera.",
  "realism": "UGC realism, real skin texture with visible pores, iPhone-footage look, no AI polish, no beauty smoothing, no blur anywhere. Do not make his skin darker or change his skin tone. Do not make the colors more saturated.",
  "negative": "do not change the face, do not change the identity, do not change the background, do not change the camera angle, no captions, no subtitles, no words overlaid on the image, no plastic skin, no extra fingers, no warm orange color cast, no yellow tint, no organ name, no jewelry besides the thin gold chain, no cross, no second person"
}
```

## K09 · T5 · PONTE · GERAR DO ZERO · FINGERPRINT DANA MORRISON

> ### 📎 ANEXAR: **1 IMAGEM**
> **1️⃣ FINGERPRINT DANA MORRISON**
>
> ### 🆕 GERAR DO ZERO

```json
{
  "shot_id": "K09_bridge_close",
  "reference_use": "Use the attached fingerprint sheet ONLY for Dana Morrison's face, identity, hair, skin texture and body build. Do NOT copy any wardrobe, background, pose or lighting from it.",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "identity_main": "The EXACT man from the attached fingerprint reference (Dana Morrison): Black American man in his early fifties, dark brown skin, a black satin do-rag tied on his head with the tail falling behind his left shoulder, a long full white chin beard with a dark moustache flecked with grey, a lean angular face with high cheekbones, direct and slightly urgent dark brown eyes, real skin texture with visible pores, deep forehead lines and crow's feet, no makeup.",
  "wardrobe": "A black ribbed tank top, a thin gold chain necklace with no pendant. No cross.",
  "scene": "The same modest lived-in American kitchen, the cork board with the small American flag pin visible over his shoulder, discreet but clearly visible and in sharp focus.",
  "posture": "Standing close to the camera, chin level, direct and slightly urgent expression.",
  "composition": "TIGHT. Shoulders-up framing, closer than every other shot. His face fills a large part of the frame, top of the do-rag cropped by the top edge. The counter is out of frame, no prop anywhere.",
  "camera": "eye level, straight-on, close talking distance",
  "state": "Start frame: speaking directly into the lens, both hands out of frame.",
  "lighting": "Flat neutral daylight under an overcast sky, no warm orange cast and no yellow tint.",
  "realism": "UGC realism, real skin texture with visible pores, individual hair strands, subtle wrinkles, iPhone-footage look, phone camera look not professional photography, no AI polish, no beauty smoothing, no blur anywhere.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no studio, no plastic skin, no extra fingers, no supernatural lighting, no blur, no artificial lighting, no warm orange color cast, no yellow tint, no props, no jewelry besides the thin gold chain, no cross, no second person"
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
  "keep_identical": "Keep the man exactly the same: same face, same do-rag, same beard, same tank top, same thin gold chain, same head position, same expression, same distance from the camera. Keep the SAME kitchen background exactly, including the small American flag pin on the cork board behind him, discreet but clearly visible and in sharp focus. Same neutral daylight, same camera angle and framing.",
  "change_1": "His right hand now comes up into the bottom of the frame at chest height with two fingers extended in a small counting gesture. Nothing else moves.",
  "realism": "UGC realism, real skin texture with visible pores, iPhone-footage look, no AI polish, no beauty smoothing, no blur anywhere. Do not change his skin tone. Do not make the colors more saturated.",
  "negative": "do not change the face, do not change the identity, do not change the background, do not change the camera angle, no captions, no subtitles, no words overlaid on the image, no plastic skin, no extra fingers, no warm orange color cast, no yellow tint, no props, no cross, no second person"
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
  "keep_identical": "Keep the man exactly the same: same face, same do-rag, same beard, same tank top, same thin gold chain, same expression. Keep the SAME kitchen background exactly, including the small American flag pin on the cork board behind him, discreet but clearly visible and in sharp focus. Same neutral daylight, same camera angle.",
  "change_1": "Push the camera about ten percent closer so the framing tightens slightly and his face becomes even more dominant. Do not change the angle or the height of the camera.",
  "change_2": "His right hand comes up into the bottom of the frame at chest height, palm open toward the lens in a natural offering gesture.",
  "realism": "UGC realism, real skin texture with visible pores, iPhone-footage look, no AI polish, no beauty smoothing, no blur anywhere. Do not change his skin tone. Do not make the colors more saturated.",
  "negative": "do not change the face, do not change the identity, do not change the background, no captions, no subtitles, no words overlaid on the image, no plastic skin, no extra fingers, no warm orange color cast, no yellow tint, no props, no cross, no second person"
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
  "keep_identical": "Keep the man exactly the same: same face, same do-rag, same beard, same tank top, same thin gold chain, same head position, same distance from the camera. Keep the SAME kitchen background exactly, including the small American flag pin on the cork board behind him, discreet but clearly visible and in sharp focus. Same neutral daylight, same camera angle and framing.",
  "change_1": "His right arm comes up into the frame and he points his index finger straight at the lens, close to the camera, in a direct way. Nothing else moves.",
  "realism": "UGC realism, real skin texture with visible pores, iPhone-footage look, no AI polish, no beauty smoothing, no blur anywhere. Do not change his skin tone. Do not make the colors more saturated.",
  "negative": "do not change the face, do not change the identity, do not change the background, do not change the camera angle, no captions, no subtitles, no words overlaid on the image, no plastic skin, no extra fingers, no warm orange color cast, no yellow tint, no props, no cross, no second person"
}
```

---

## Bloco global de vídeo

```text
o avatar (homem) fala em inglês com sotaque americano de Dana Morrison, voz autêntica, direta e um pouco urgente, como quem aprendeu do jeito difícil, a seguinte frase: "[FALA EXATA DO ROTEIRO]"

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: [ação ENXUTA, só o que acontece]

câmera: [fixa / leve push-in]

som ambiente: cozinha silenciosa de casa, com um leve ruído do lado de fora, sem música
```

---

# Prompts de vídeo

### V01 · T1 (gancho 1) · usa K01

```text
o avatar (homem) fala em inglês com sotaque americano de Dana Morrison, voz autêntica, direta e um pouco urgente, como quem aprendeu do jeito difícil, a seguinte frase: "Next time you cook rice, don't pour that starchy water down the kitchen sink. Most of my clients throw it away without knowing what it does."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ele inclina a panela sobre a pia, a água turva escorre em jato grosso, forma espuma branca ao redor do ralo e alguns grãos de arroz ficam presos nas grades.

câmera: fixa

som ambiente: cozinha silenciosa de casa, com um leve ruído do lado de fora, sem música
```

### V02 · T1 (gancho 2) · usa K02

```text
o avatar (homem) fala em inglês com sotaque americano de Dana Morrison, voz autêntica, direta e um pouco urgente, como quem aprendeu do jeito difícil, a seguinte frase: "Next time you cook rice, don't pour that starchy water down the drain. Watch how much of it disappears without you even noticing."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: o jato cai de cima e ganha nitidez ao bater nas grades, a espuma nasce no impacto e escorre pelas ranhuras arrastando grãos de arroz.

câmera: fixa

som ambiente: cozinha silenciosa de casa, com um leve ruído do lado de fora, sem música
```

### V03 · T1 (gancho 5) · usa K03

```text
o avatar (homem) fala em inglês com sotaque americano de Dana Morrison, voz autêntica, direta e um pouco urgente, como quem aprendeu do jeito difícil, a seguinte frase: "Next time you soak your oats, don't pour that starchy water down the drain. It's exactly what most of the women I coach throw away."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ele inclina a tigela e o líquido leitoso escorre devagar num fio contínuo, flocos de aveia deslizam pela borda e ficam presos no ralo.

câmera: fixa

som ambiente: cozinha silenciosa de casa, com um leve ruído do lado de fora, sem música
```

### V04 · T1 (gancho 7) · usa K04

```text
o avatar (homem) fala em inglês com sotaque americano de Dana Morrison, voz autêntica, direta e um pouco urgente, como quem aprendeu do jeito difícil, a seguinte frase: "Next time you cook rice, don't pour that starchy water down the storm drain outside. It's exactly what most of the women I coach throw away."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: de uma altura maior, o jato se abre no ar antes de bater no bueiro, salpicando água para os lados sobre o concreto.

câmera: fixa

som ambiente: rua residencial tranquila, pássaros ao longe, sem música
```

### V05 · T1 (gancho 9) · usa K05

```text
o avatar (homem) fala em inglês com sotaque americano de Dana Morrison, voz autêntica, direta e um pouco urgente, como quem aprendeu do jeito difícil, a seguinte frase: "Next time you cook rice, don't dump that starchy water straight into the trash. It's exactly what most of the women I coach throw away."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ele inclina a panela sobre a lata de lixo aberta, a água cai sobre o lixo dentro dela e escurece na hora ao se misturar.

câmera: fixa

som ambiente: área externa silenciosa, sem música
```

### V06 · T2 · usa K06

```text
o avatar (homem) fala em inglês com sotaque americano de Dana Morrison, voz autêntica, direta e um pouco urgente, como quem aprendeu do jeito difícil, a seguinte frase: "Let it cool, and pour it into a jar instead of the sink. It costs you one extra minute."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ele deixa o líquido esfriar e o despeja dentro do pote de vidro na bancada, o pote vai enchendo aos poucos.

câmera: fixa

som ambiente: cozinha silenciosa de casa, com um leve ruído do lado de fora, sem música
```

### V07 · T3 · usa K07

```text
o avatar (homem) fala em inglês com sotaque americano de Dana Morrison, voz autêntica, direta e um pouco urgente, como quem aprendeu do jeito difícil, a seguinte frase: "That starchy water is loaded with resistant starch, the exact fuel a woman's gut bacteria start starving for after forty."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ele despeja o líquido guardado sobre o modelo, a crosta escura amolece e começa a se soltar em placas, revelando o tecido rosado por baixo.

câmera: fixa

som ambiente: cozinha silenciosa de casa, com um leve ruído do lado de fora, sem música
```

### V08 · T4 · usa K08

```text
o avatar (homem) fala em inglês com sotaque americano de Dana Morrison, voz autêntica, direta e um pouco urgente, como quem aprendeu do jeito difícil, a seguinte frase: "A simple, no waste habit worth trying tonight. But it only reaches one piece of what's actually holding her back."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ele afasta o pote vazio e olha pra câmera, o modelo atrás dele já com boa parte da crosta solta.

câmera: fixa

som ambiente: cozinha silenciosa de casa, com um leve ruído do lado de fora, sem música
```

### V09 · T5 · usa K09

```text
o avatar (homem) fala em inglês com sotaque americano de Dana Morrison, voz autêntica, direta e um pouco urgente, como quem aprendeu do jeito difícil, a seguinte frase: "After forty, three things hold your body: your hormones, your metabolism, and your gut. That water only touches the gut."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ele fala direto para a lente, sem se mexer do lugar.

câmera: fixa

som ambiente: cozinha silenciosa de casa, com um leve ruído do lado de fora, sem música
```

### V10 · T6 · usa K10

```text
o avatar (homem) fala em inglês com sotaque americano de Dana Morrison, voz autêntica, direta e um pouco urgente, como quem aprendeu do jeito difícil, a seguinte frase: "If yours is the hormone one, or the metabolism one, you can drink this every night and nothing will change."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ele levanta dois dedos e depois abaixa a mão devagar.

câmera: fixa

som ambiente: cozinha silenciosa de casa, com um leve ruído do lado de fora, sem música
```

### V11 · T7 · usa K11

```text
o avatar (homem) fala em inglês com sotaque americano de Dana Morrison, voz autêntica, direta e um pouco urgente, como quem aprendeu do jeito difícil, a seguinte frase: "It was never about the water. It's which of the three is yours. Comment yes and I will send you the FityWell quiz."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ele abre a mão na direção da lente enquanto fala.

câmera: leve push-in

som ambiente: cozinha silenciosa de casa, com um leve ruído do lado de fora, sem música
```

### V12 · T8 · usa K12

```text
o avatar (homem) fala em inglês com sotaque americano de Dana Morrison, voz autêntica, direta e um pouco urgente, como quem aprendeu do jeito difícil, a seguinte frase: "But follow me first, or it will not let me reach you. Two minutes, and you will finally know which one."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ele aponta o dedo para a lente e mantém o gesto até o fim da fala.

câmera: leve push-in

som ambiente: cozinha silenciosa de casa, com um leve ruído do lado de fora, sem música
```

---

## Mapa de âncoras

| Keyframe | Referências a anexar | Modelo |
|---|---|---|
| K01 a K07 | FINGERPRINT DANA MORRISON | Nano Banana 2, 9:16 |
| K08 | o K07 aprovado | Nano Banana 2, 9:16 |
| K09 | FINGERPRINT DANA MORRISON | Nano Banana 2, 9:16 |
| K10 | o K09 aprovado | Nano Banana 2, 9:16 |
| K11 | o K09 aprovado | Nano Banana 2, 9:16 |
| K12 | o K09 aprovado | Nano Banana 2, 9:16 |

Vídeo: Veo 3.1 Lite, Lower Priority, 8 segundos, 1 variação, imagem sempre como INITIAL FRAME.

---

## Montagem no CapCut

1. **Escolher UM gancho por vídeo.** Cada vídeo finalizado é V01, V02, V03, V04 ou V05 na abertura,
   seguido sempre de V06 a V12.
2. Cortar cada clipe no fim da fala.
3. Legenda queimada em todos os takes, palavra destacada em amarelo na keyword.
4. No T7, quando ele disser `yes`, subir a palavra `YES` grande na tela por um segundo.
5. Sem música. Só o som ambiente do clipe.
6. Exportar em 9:16, 1080 por 1920.

---

## Gates de qualidade

1. [ ] O herói (jato/impacto) está no lower foreground, mais perto da lente que o rosto, em K01 a K05.
2. [ ] A crosta do modelo anatômico saiu volumosa em K07, não uma película fina.
3. [ ] O modelo didático saiu com a forma pedida e sem detalhe anatômico fino, sem nome de órgão no negative.
4. [ ] A bandeirinha dos EUA aparece e está em foco em todo keyframe que tenha cenário fixo (K01, K06 a K12).
5. [ ] Nenhum keyframe tem celular, tela, rótulo de marca ou qualquer coisa que leia como produto.
6. [ ] Identidade batendo com a fingerprint em todos os 12 keyframes (rosto, do-rag, barba, corrente).
7. [ ] Zero blur em qualquer imagem.
8. [ ] Luz neutra de dia nublado em todas. Nenhuma imagem com cast quente.
9. [ ] K05 (lata de lixo) sem detalhe gráfico de lixo, sem inseto.
10. [ ] A fala de cada V bate palavra por palavra com o take do `ROTEIRO.md`.
11. [ ] Nenhum take sugere que ela não se esforçou o bastante.
12. [ ] Sem 2ª pessoa viva em nenhum keyframe.
13. [ ] `python checar_entrega.py producao/fitywell_arroz` fechou sem FALHA.
