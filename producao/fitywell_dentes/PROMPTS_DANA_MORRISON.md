# Dana Morrison | Ângulo 2 (FityWell) | Pacote de Prompts

Vídeo modelo: `AQNOzaiELL1KUf6UdTBVtG4QDvs3fuADfwu921kuiKd22EV28JMbptZOsqzF0de8_ikAESRjZM62j6piUfrFgmsVOXZMwl7HG0h_4LM.mp4` (34,9 s, avatar sozinho, clareador dental caseiro)

Referência de identidade: **fingerprint (character consistency sheet) anexado na mensagem original**, trava rosto/corpo/pele/barba. Cenário nasce do texto, usando o cenário canônico da garagem porque ele já cabe na demo sem adaptação.

Funil: **nenhum, vídeo de crescimento.** CTA fecha em comment `teeth` + follow, receber a rotina completa por DM. Sem produto, sem app, sem quiz, sem keyword de conversão.

Avatar 1 de 3 da fila (`AVATAR_QUEUE.md`). Ganchos escolhidos pelo Luigi: 6 (café), 7 (vinho tinto), 8 (refrigerante de cola), 1 (dentadura no suporte), 3 (protetor bucal esportivo).

---

## Índice de geração

| Take | Keyframe | Anexar | Ação de geração |
|---|---|---|---|
| T1 · gancho café | K01 | FINGERPRINT DANA MORRISON | GERAR DO ZERO. Café sobre o modelo dental manchado |
| T1 · gancho vinho | K02 | FINGERPRINT DANA MORRISON | GERAR DO ZERO. Vinho tinto sobre o modelo dental manchado |
| T1 · gancho refrigerante | K03 | FINGERPRINT DANA MORRISON | GERAR DO ZERO. Refrigerante de cola sobre o modelo dental manchado |
| T1 · gancho dentadura | K04 | FINGERPRINT DANA MORRISON | GERAR DO ZERO. Água sobre a dentadura manchada no suporte |
| T1 · gancho protetor | K05 | FINGERPRINT DANA MORRISON | GERAR DO ZERO. Água sobre o protetor bucal amarelado no suporte |
| T2 | K06 | FINGERPRINT DANA MORRISON | GERAR DO ZERO. Receita, ingredientes indo pra tigela |
| T3, T4 | K07 | o K06 aprovado | EDITAR do K06. Muda só o estado da tigela e a distância da câmera |
| T5, T6 | K08 | FINGERPRINT DANA MORRISON | GERAR DO ZERO. Tigela na bancada, mão apontando pro CTA |

Regra de bolso: **GERAR DO ZERO anexa o fingerprint. EDITAR anexa uma imagem só, o keyframe de origem.**
🚫 Nunca anexar um keyframe editado como origem de outro.

---

## Trava de identidade e continuidade

- Homem negro americano no início dos cinquenta, pele marrom escura.
- **Do-rag preto de cetim** amarrado na cabeça, com a aba caindo atrás do ombro esquerdo.
- **Barba do queixo comprida e branca**, cheia, bigode escuro salpicado de grisalho. É a marca do rosto dele, nunca encurtar.
- Rosto magro e anguloso, maçãs altas, olhos castanhos escuros, olhar direto e levemente urgente.
- **Corpo seco e treinado**, ombros largos, antebraços com veias marcadas, mãos grandes e calejadas.
- Pele com textura real, poros visíveis, linhas fundas na testa, pés de galinha, sem maquiagem.
- **Regata canelada PRETA** e **corrente fina de ouro** no pescoço, sem pingente, sem cruz. Calça escura.
- Cenário: bancada de madeira gasta e manchada da garagem, parede de pegboard marrom com ferramentas, armário de madeira à direita com potes de ervas rotulados (VALERIAN ROOT, ECHINACEA, MULLEIN), **bandeirinha dos EUA em pé na prateleira**, placa de papelão escrita à mão SLEEP WATER WALK GREENS SUN, porta de garagem branca de enrolar recolhida no alto do quadro.
- Luz **neutra de dia**, entrando pela porta aberta da garagem. Zero blur, tudo em foco nítido.

---

## Trava do prop herói

Cinco props diferentes no hook (um por gancho escolhido), descritos em cada K abaixo. De T2 a T6 o
prop é sempre a mesma tigela de vidro com a pasta branca, sem estágios de mistura diferentes entre
esses takes, é o mesmo objeto sendo montado e depois segurado.

```text
Sem marca em quadro: o óleo de coco fica num pote de vidro liso sem rótulo, o bicarbonato numa lata
sem rótulo. Nunca negar marca no negative, resolver sempre no positivo com objeto liso.
```

## Trava da 2ª pessoa (REF-A)

Não se aplica. Não há segunda pessoa em nenhum take.

---

# Prompts de imagem

## K01 · T1 · GANCHO CAFÉ · GERAR DO ZERO · FINGERPRINT DANA MORRISON

> ### 📎 ANEXAR: **1 IMAGEM**
> **1️⃣ FINGERPRINT DANA MORRISON** (character consistency sheet anexado na mensagem original)
>
> ### 🆕 GERAR DO ZERO

```json
{
  "shot_id": "K01_hook_coffee",
  "reference_use": "Use the attached fingerprint reference ONLY for Dana Morrison's face, identity, body, beard and skin. Do NOT copy its pose, framing or background.",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "identity_main": "The EXACT man from the attached fingerprint reference (Dana Morrison): Black American man in his early fifties, deep dark brown skin, a black satin durag tied tightly over his head with the tail falling behind his left shoulder, dark brown eyes with a direct and slightly urgent gaze, a lean angular face with high cheekbones, a wide nose and thick eyebrows, a long full white chin beard with a dark moustache flecked with grey, a lean powerfully trained build with broad shoulders, defined forearms with visible veins, large calloused hands, real skin texture with visible pores, deep forehead lines, crow's feet, no makeup.",
  "wardrobe": "A plain black ribbed tank top and a thin gold chain necklace with no pendant. Dark trousers. No cross, no other jewelry.",
  "prop": "A dental teaching model of a full set of upper teeth and gums, heavily stained yellow brown with visible dark tartar buildup along the gumline, held low and very close to the lens from underneath so it fills the frame like a mouth seen from below. In his other hand, held higher, a plain dark ceramic mug is tilted, pouring a thin stream of dark coffee down onto the stained teeth.",
  "scene": "SAME garage workshop as the reference: a scuffed, stained wooden workbench, a brown pegboard wall behind him hung with wrenches, a yellow handled hammer and colorful handled screwdrivers, an open wooden cabinet to the right with glass jars labelled VALERIAN ROOT, ECHINACEA and MULLEIN, a small American flag standing on that shelf, discreet but clearly visible and in sharp focus, a hand lettered cardboard sign taped to the cabinet reading SLEEP WATER WALK GREENS SUN, and the white roll up garage door raised at the top of the frame.",
  "posture": "Seated at the workbench, leaning forward and down slightly toward the model, both hands raised toward the camera.",
  "composition": "The stained teeth model fills the lower two thirds of the frame and sits much closer to the lens than his face, so it is unmistakably the hero. His head and shoulders occupy the upper third, tilted slightly down toward it. Nothing else competes.",
  "camera": "chest level, straight-on, camera pushed in close and slightly low toward the model, looking faintly upward",
  "state": "Start frame: the mug is tilted and the first thin stream of dark coffee is just leaving its rim, about to land on the stained teeth. The model is fully dry and stained, nothing has been touched yet.",
  "lighting": "Flat neutral daylight spilling in from the open garage door, evenly lighting his face, no warm orange cast and no yellow tint.",
  "realism": "UGC realism, real skin texture with visible pores, individual hair strands, subtle wrinkles, realistic shadows and reflections, iPhone-footage look, phone camera look not professional photography, no AI polish, no beauty smoothing, no blur anywhere, everything in sharp focus including the pegboard and the shelf.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no studio, no plastic skin, no extra fingers, no supernatural lighting, no blur, no artificial lighting, no warm orange color cast, no yellow tint, no jewelry besides the described gold chain, no cross, no second person, no brand label"
}
```

## K02 · T1 · GANCHO VINHO TINTO · GERAR DO ZERO · FINGERPRINT DANA MORRISON

> ### 📎 ANEXAR: **1 IMAGEM**
> **1️⃣ FINGERPRINT DANA MORRISON** (character consistency sheet anexado na mensagem original)
>
> ### 🆕 GERAR DO ZERO

```json
{
  "shot_id": "K02_hook_wine",
  "reference_use": "Use the attached fingerprint reference ONLY for Dana Morrison's face, identity, body, beard and skin. Do NOT copy its pose, framing or background.",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "identity_main": "The EXACT man from the attached fingerprint reference (Dana Morrison): Black American man in his early fifties, deep dark brown skin, a black satin durag tied tightly over his head with the tail falling behind his left shoulder, dark brown eyes with a direct and slightly urgent gaze, a lean angular face with high cheekbones, a wide nose and thick eyebrows, a long full white chin beard with a dark moustache flecked with grey, a lean powerfully trained build with broad shoulders, defined forearms with visible veins, large calloused hands, real skin texture with visible pores, deep forehead lines, crow's feet, no makeup.",
  "wardrobe": "A plain black ribbed tank top and a thin gold chain necklace with no pendant. Dark trousers. No cross, no other jewelry.",
  "prop": "A dental teaching model of a full set of upper teeth and gums, heavily stained yellow brown with visible dark tartar buildup along the gumline, held low and very close to the lens from underneath so it fills the frame like a mouth seen from below. In his other hand, held higher, a plain dark glass carafe is tilted, pouring a thin stream of deep red wine down onto the stained teeth.",
  "scene": "SAME garage workshop as the reference: a scuffed, stained wooden workbench, a brown pegboard wall behind him hung with wrenches, a yellow handled hammer and colorful handled screwdrivers, an open wooden cabinet to the right with glass jars labelled VALERIAN ROOT, ECHINACEA and MULLEIN, a small American flag standing on that shelf, discreet but clearly visible and in sharp focus, a hand lettered cardboard sign taped to the cabinet reading SLEEP WATER WALK GREENS SUN, and the white roll up garage door raised at the top of the frame.",
  "posture": "Seated at the workbench, leaning forward and down slightly toward the model, both hands raised toward the camera.",
  "composition": "The stained teeth model fills the lower two thirds of the frame and sits much closer to the lens than his face, so it is unmistakably the hero. His head and shoulders occupy the upper third, tilted slightly down toward it. Nothing else competes.",
  "camera": "chest level, straight-on, camera pushed in close and slightly low toward the model, looking faintly upward",
  "state": "Start frame: the carafe is tilted and the first thin stream of red wine is just leaving its rim, about to land on the stained teeth. The model is fully dry and stained, nothing has been touched yet.",
  "lighting": "Flat neutral daylight spilling in from the open garage door, evenly lighting his face, no warm orange cast and no yellow tint.",
  "realism": "UGC realism, real skin texture with visible pores, individual hair strands, subtle wrinkles, realistic shadows and reflections, iPhone-footage look, phone camera look not professional photography, no AI polish, no beauty smoothing, no blur anywhere, everything in sharp focus including the pegboard and the shelf.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no studio, no plastic skin, no extra fingers, no supernatural lighting, no blur, no artificial lighting, no warm orange color cast, no yellow tint, no jewelry besides the described gold chain, no cross, no second person, no brand label"
}
```

## K03 · T1 · GANCHO REFRIGERANTE DE COLA · GERAR DO ZERO · FINGERPRINT DANA MORRISON

> ### 📎 ANEXAR: **1 IMAGEM**
> **1️⃣ FINGERPRINT DANA MORRISON** (character consistency sheet anexado na mensagem original)
>
> ### 🆕 GERAR DO ZERO

```json
{
  "shot_id": "K03_hook_cola",
  "reference_use": "Use the attached fingerprint reference ONLY for Dana Morrison's face, identity, body, beard and skin. Do NOT copy its pose, framing or background.",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "identity_main": "The EXACT man from the attached fingerprint reference (Dana Morrison): Black American man in his early fifties, deep dark brown skin, a black satin durag tied tightly over his head with the tail falling behind his left shoulder, dark brown eyes with a direct and slightly urgent gaze, a lean angular face with high cheekbones, a wide nose and thick eyebrows, a long full white chin beard with a dark moustache flecked with grey, a lean powerfully trained build with broad shoulders, defined forearms with visible veins, large calloused hands, real skin texture with visible pores, deep forehead lines, crow's feet, no makeup.",
  "wardrobe": "A plain black ribbed tank top and a thin gold chain necklace with no pendant. Dark trousers. No cross, no other jewelry.",
  "prop": "A dental teaching model of a full set of upper teeth and gums, heavily stained yellow brown with visible dark tartar buildup along the gumline, held low and very close to the lens from underneath so it fills the frame like a mouth seen from below. In his other hand, held higher, a plain dark glass jug is tilted, pouring a thin, faintly foaming stream of dark cola down onto the stained teeth.",
  "scene": "SAME garage workshop as the reference: a scuffed, stained wooden workbench, a brown pegboard wall behind him hung with wrenches, a yellow handled hammer and colorful handled screwdrivers, an open wooden cabinet to the right with glass jars labelled VALERIAN ROOT, ECHINACEA and MULLEIN, a small American flag standing on that shelf, discreet but clearly visible and in sharp focus, a hand lettered cardboard sign taped to the cabinet reading SLEEP WATER WALK GREENS SUN, and the white roll up garage door raised at the top of the frame.",
  "posture": "Seated at the workbench, leaning forward and down slightly toward the model, both hands raised toward the camera.",
  "composition": "The stained teeth model fills the lower two thirds of the frame and sits much closer to the lens than his face, so it is unmistakably the hero. His head and shoulders occupy the upper third, tilted slightly down toward it. Nothing else competes.",
  "camera": "chest level, straight-on, camera pushed in close and slightly low toward the model, looking faintly upward",
  "state": "Start frame: the jug is tilted and the first thin, faintly foaming stream of cola is just leaving its rim, about to land on the stained teeth. The model is fully dry and stained, nothing has been touched yet.",
  "lighting": "Flat neutral daylight spilling in from the open garage door, evenly lighting his face, no warm orange cast and no yellow tint.",
  "realism": "UGC realism, real skin texture with visible pores, individual hair strands, subtle wrinkles, realistic shadows and reflections, iPhone-footage look, phone camera look not professional photography, no AI polish, no beauty smoothing, no blur anywhere, everything in sharp focus including the pegboard and the shelf.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no studio, no plastic skin, no extra fingers, no supernatural lighting, no blur, no artificial lighting, no warm orange color cast, no yellow tint, no jewelry besides the described gold chain, no cross, no second person, no brand label"
}
```

## K04 · T1 · GANCHO DENTADURA NO SUPORTE · GERAR DO ZERO · FINGERPRINT DANA MORRISON

> ### 📎 ANEXAR: **1 IMAGEM**
> **1️⃣ FINGERPRINT DANA MORRISON** (character consistency sheet anexado na mensagem original)
>
> ### 🆕 GERAR DO ZERO

```json
{
  "shot_id": "K04_hook_denture",
  "reference_use": "Use the attached fingerprint reference ONLY for Dana Morrison's face, identity, body, beard and skin. Do NOT copy its pose, framing or background.",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "identity_main": "The EXACT man from the attached fingerprint reference (Dana Morrison): Black American man in his early fifties, deep dark brown skin, a black satin durag tied tightly over his head with the tail falling behind his left shoulder, dark brown eyes with a direct and slightly urgent gaze, a lean angular face with high cheekbones, a wide nose and thick eyebrows, a long full white chin beard with a dark moustache flecked with grey, a lean powerfully trained build with broad shoulders, defined forearms with visible veins, large calloused hands, real skin texture with visible pores, deep forehead lines, crow's feet, no makeup.",
  "wardrobe": "A plain black ribbed tank top and a thin gold chain necklace with no pendant. Dark trousers. No cross, no other jewelry.",
  "prop": "A complete removable denture, heavily stained yellow brown with visible dark tartar buildup along the gumline, standing upright in a small clear plastic stand at the edge of the workbench, closest to the lens and lower than his face. In his hand, held higher, a small metal kettle is tilted, pouring a thin stream of clean water down onto the stained denture.",
  "scene": "SAME garage workshop as the reference: a scuffed, stained wooden workbench, a brown pegboard wall behind him hung with wrenches, a yellow handled hammer and colorful handled screwdrivers, an open wooden cabinet to the right with glass jars labelled VALERIAN ROOT, ECHINACEA and MULLEIN, a small American flag standing on that shelf, discreet but clearly visible and in sharp focus, a hand lettered cardboard sign taped to the cabinet reading SLEEP WATER WALK GREENS SUN, and the white roll up garage door raised at the top of the frame.",
  "posture": "Seated at the workbench, leaning forward slightly toward the stand, one hand pouring from above.",
  "composition": "The stained denture on its stand fills the lower two thirds of the frame and sits much closer to the lens than his face, so it is unmistakably the hero. His head and shoulders occupy the upper third. Nothing else competes.",
  "camera": "chest level, straight-on, camera pushed in close toward the stand",
  "state": "Start frame: the kettle is tilted and the first thin stream of clean water is just leaving its spout, about to land on the stained denture. The denture is fully dry and stained, nothing has been touched yet.",
  "lighting": "Flat neutral daylight spilling in from the open garage door, evenly lighting his face, no warm orange cast and no yellow tint.",
  "realism": "UGC realism, real skin texture with visible pores, individual hair strands, subtle wrinkles, realistic shadows and reflections, iPhone-footage look, phone camera look not professional photography, no AI polish, no beauty smoothing, no blur anywhere, everything in sharp focus including the pegboard and the shelf.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no studio, no plastic skin, no extra fingers, no supernatural lighting, no blur, no artificial lighting, no warm orange color cast, no yellow tint, no jewelry besides the described gold chain, no cross, no second person, no brand label"
}
```

## K05 · T1 · GANCHO PROTETOR BUCAL · GERAR DO ZERO · FINGERPRINT DANA MORRISON

> ### 📎 ANEXAR: **1 IMAGEM**
> **1️⃣ FINGERPRINT DANA MORRISON** (character consistency sheet anexado na mensagem original)
>
> ### 🆕 GERAR DO ZERO

```json
{
  "shot_id": "K05_hook_mouthguard",
  "reference_use": "Use the attached fingerprint reference ONLY for Dana Morrison's face, identity, body, beard and skin. Do NOT copy its pose, framing or background.",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "identity_main": "The EXACT man from the attached fingerprint reference (Dana Morrison): Black American man in his early fifties, deep dark brown skin, a black satin durag tied tightly over his head with the tail falling behind his left shoulder, dark brown eyes with a direct and slightly urgent gaze, a lean angular face with high cheekbones, a wide nose and thick eyebrows, a long full white chin beard with a dark moustache flecked with grey, a lean powerfully trained build with broad shoulders, defined forearms with visible veins, large calloused hands, real skin texture with visible pores, deep forehead lines, crow's feet, no makeup.",
  "wardrobe": "A plain black ribbed tank top and a thin gold chain necklace with no pendant. Dark trousers. No cross, no other jewelry.",
  "prop": "A thick silicone sports mouthguard, yellowed with visibly darkened edges from wear, resting in a small clear plastic stand at the edge of the workbench, closest to the lens and lower than his face. In his hand, held higher, a small metal kettle is tilted, pouring a thin stream of clean water down onto the yellowed mouthguard.",
  "scene": "SAME garage workshop as the reference: a scuffed, stained wooden workbench, a brown pegboard wall behind him hung with wrenches, a yellow handled hammer and colorful handled screwdrivers, an open wooden cabinet to the right with glass jars labelled VALERIAN ROOT, ECHINACEA and MULLEIN, a small American flag standing on that shelf, discreet but clearly visible and in sharp focus, a hand lettered cardboard sign taped to the cabinet reading SLEEP WATER WALK GREENS SUN, and the white roll up garage door raised at the top of the frame.",
  "posture": "Seated at the workbench, leaning forward slightly toward the stand, one hand pouring from above.",
  "composition": "The yellowed mouthguard on its stand fills the lower two thirds of the frame and sits much closer to the lens than his face, so it is unmistakably the hero. His head and shoulders occupy the upper third. Nothing else competes.",
  "camera": "chest level, straight-on, camera pushed in close toward the stand",
  "state": "Start frame: the kettle is tilted and the first thin stream of clean water is just leaving its spout, about to land on the yellowed mouthguard. Nothing has been touched yet.",
  "lighting": "Flat neutral daylight spilling in from the open garage door, evenly lighting his face, no warm orange cast and no yellow tint.",
  "realism": "UGC realism, real skin texture with visible pores, individual hair strands, subtle wrinkles, realistic shadows and reflections, iPhone-footage look, phone camera look not professional photography, no AI polish, no beauty smoothing, no blur anywhere, everything in sharp focus including the pegboard and the shelf.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no studio, no plastic skin, no extra fingers, no supernatural lighting, no blur, no artificial lighting, no warm orange color cast, no yellow tint, no jewelry besides the described gold chain, no cross, no second person, no brand label"
}
```

## K06 · T2 · RECEITA · GERAR DO ZERO · FINGERPRINT DANA MORRISON

> ### 📎 ANEXAR: **1 IMAGEM**
> **1️⃣ FINGERPRINT DANA MORRISON** (character consistency sheet anexado na mensagem original)
>
> ### 🆕 GERAR DO ZERO

```json
{
  "shot_id": "K06_recipe",
  "reference_use": "Use the attached fingerprint reference ONLY for Dana Morrison's face, identity, body, beard and skin. Do NOT copy its pose, framing or background.",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "identity_main": "The EXACT man from the attached fingerprint reference (Dana Morrison): Black American man in his early fifties, deep dark brown skin, a black satin durag tied tightly over his head with the tail falling behind his left shoulder, dark brown eyes with a direct and slightly urgent gaze, a lean angular face with high cheekbones, a wide nose and thick eyebrows, a long full white chin beard with a dark moustache flecked with grey, a lean powerfully trained build with broad shoulders, defined forearms with visible veins, large calloused hands, real skin texture with visible pores, deep forehead lines, crow's feet, no makeup.",
  "wardrobe": "A plain black ribbed tank top and a thin gold chain necklace with no pendant. Dark trousers. No cross, no other jewelry.",
  "prop": "On the workbench in front of him: an unlabeled plain glass jar of coconut oil with the lid off, a plain unlabeled tin of baking soda, a halved lemon, a plain metal spoon and a clear glass mixing bowl with a small amount of white coconut oil already resting in the bottom. His right hand holds the spoon, mid scoop over the open tin of baking soda, about to add it to the bowl.",
  "scene": "SAME garage workshop as the reference: the scuffed wooden workbench now doubling as a prep surface, a brown pegboard wall behind him hung with wrenches, a yellow handled hammer and colorful handled screwdrivers, an open wooden cabinet to the right with glass jars labelled VALERIAN ROOT, ECHINACEA and MULLEIN, a small American flag standing on that shelf, discreet but clearly visible and in sharp focus, a hand lettered cardboard sign taped to the cabinet reading SLEEP WATER WALK GREENS SUN, and the white roll up garage door raised at the top of the frame.",
  "posture": "Seated at the workbench, leaning forward over the ingredients.",
  "composition": "The bowl, jar, tin and lemon fill the lower two thirds of the frame, closer to the lens than his face. His head and shoulders occupy the upper third. Nothing else competes.",
  "camera": "chest level, straight-on, camera pushed in close toward the ingredients",
  "state": "Start frame: the spoon holds a scoop of white baking soda just above the bowl, about to be added to the coconut oil already inside. Nothing has been mixed yet, no paste texture is visible, only the plain coconut oil in the bowl.",
  "lighting": "Flat neutral daylight spilling in from the open garage door, evenly lighting his face, no warm orange cast and no yellow tint.",
  "realism": "UGC realism, real skin texture with visible pores, individual hair strands, subtle wrinkles, realistic shadows and reflections, iPhone-footage look, phone camera look not professional photography, no AI polish, no beauty smoothing, no blur anywhere, everything in sharp focus including the pegboard and the shelf.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no studio, no plastic skin, no extra fingers, no supernatural lighting, no blur, no artificial lighting, no warm orange color cast, no yellow tint, no jewelry besides the described gold chain, no cross, no second person, no brand label, no visible brand text on the tin or the jar"
}
```

## K07 · T3 e T4 · PROTOCOLO/RESULTADO · EDITAR do K06

> ### 📎 ANEXAR: **1 IMAGEM**
> **1️⃣ O K06 APROVADO**
>
> ### ✏️ EDITAR

```json
{
  "shot_id": "K07_holding_bowl",
  "reference_use": "Edit the attached image (K06, already approved). Keep Dana Morrison's face, identity, wardrobe, the garage background and the lighting IDENTICAL. Change only what is described below.",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "identity_main": "The EXACT same man as the attached image (Dana Morrison): Black American man in his early fifties, deep dark brown skin, black satin durag with the tail falling behind his left shoulder, long full white chin beard with a dark moustache flecked with grey, lean angular face, direct and slightly urgent gaze, lean powerfully trained build, defined forearms with visible veins, large calloused hands, real skin texture, no makeup.",
  "wardrobe": "SAME plain black ribbed tank top and thin gold chain necklace. Dark trousers. No cross, no other jewelry.",
  "prop": "He now holds the clear glass mixing bowl close to the camera with both hands, filled with a smooth, finished white paste. The spoon, the tin and the jar are no longer in his hands.",
  "scene": "SAME garage workshop, unchanged: the workbench, the pegboard wall, the wooden cabinet with the labelled herb jars, the small American flag on the shelf, the hand lettered cardboard sign, the white roll up garage door.",
  "posture": "Leaning forward at the workbench, holding the bowl up toward the camera with both hands, calm and direct expression.",
  "composition": "The bowl of white paste fills the lower half of the frame, closer to the lens than his face. His head and shoulders occupy the upper half.",
  "camera": "chest level, straight-on, camera pushed in close toward the bowl",
  "state": "Start frame: the bowl of finished white paste is held steady toward the camera. Nothing pours or changes, the paste is smooth and unmoving.",
  "lighting": "SAME flat neutral daylight from the open garage door, no warm orange cast and no yellow tint.",
  "realism": "UGC realism, real skin texture with visible pores, individual hair strands, subtle wrinkles, realistic shadows and reflections, iPhone-footage look, phone camera look not professional photography, no AI polish, no beauty smoothing, no blur anywhere, everything in sharp focus.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no studio, no plastic skin, no extra fingers, no supernatural lighting, no blur, no artificial lighting, no warm orange color cast, no yellow tint, no jewelry besides the described gold chain, no cross, no second person, no brand label"
}
```

## K08 · T5 e T6 · ESCALADA/CTA · GERAR DO ZERO · FINGERPRINT DANA MORRISON

> ### 📎 ANEXAR: **1 IMAGEM**
> **1️⃣ FINGERPRINT DANA MORRISON** (character consistency sheet anexado na mensagem original)
>
> ### 🆕 GERAR DO ZERO

```json
{
  "shot_id": "K08_cta_point",
  "reference_use": "Use the attached fingerprint reference ONLY for Dana Morrison's face, identity, body, beard and skin. Do NOT copy its pose, framing or background.",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "identity_main": "The EXACT man from the attached fingerprint reference (Dana Morrison): Black American man in his early fifties, deep dark brown skin, a black satin durag tied tightly over his head with the tail falling behind his left shoulder, dark brown eyes with a direct and slightly urgent gaze, a lean angular face with high cheekbones, a wide nose and thick eyebrows, a long full white chin beard with a dark moustache flecked with grey, a lean powerfully trained build with broad shoulders, defined forearms with visible veins, large calloused hands, real skin texture with visible pores, deep forehead lines, crow's feet, no makeup.",
  "wardrobe": "A plain black ribbed tank top and a thin gold chain necklace with no pendant. Dark trousers. No cross, no other jewelry.",
  "prop": "The clear glass mixing bowl with the finished white paste rests on the workbench between his forearms. His right hand is raised toward the camera in an urgent pointing gesture, index finger extended.",
  "scene": "SAME garage workshop as the reference: the scuffed wooden workbench, a brown pegboard wall behind him hung with wrenches, a yellow handled hammer and colorful handled screwdrivers, an open wooden cabinet to the right with glass jars labelled VALERIAN ROOT, ECHINACEA and MULLEIN, a small American flag standing on that shelf, discreet but clearly visible and in sharp focus, a hand lettered cardboard sign taped to the cabinet reading SLEEP WATER WALK GREENS SUN, and the white roll up garage door raised at the top of the frame.",
  "posture": "Leaning forward at the workbench, the bowl resting between his forearms, right hand raised and pointing directly at the camera, urgent and direct expression.",
  "composition": "The bowl and his forearms occupy the lower third of the frame, his raised pointing hand and upper body fill the rest, closer to the lens than a normal talking shot.",
  "camera": "chest level, straight-on, camera pushed in close",
  "state": "Start frame: the hand is mid gesture, finger extended toward the camera, the bowl sits still on the bench.",
  "lighting": "Flat neutral daylight spilling in from the open garage door, evenly lighting his face, no warm orange cast and no yellow tint.",
  "realism": "UGC realism, real skin texture with visible pores, individual hair strands, subtle wrinkles, realistic shadows and reflections, iPhone-footage look, phone camera look not professional photography, no AI polish, no beauty smoothing, no blur anywhere, everything in sharp focus including the pegboard and the shelf.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no studio, no plastic skin, no extra fingers, no supernatural lighting, no blur, no artificial lighting, no warm orange color cast, no yellow tint, no jewelry besides the described gold chain, no cross, no second person, no brand label"
}
```

---

## Bloco global de vídeo

```text
o avatar (homem) fala em inglês com sotaque americano de Dana Morrison, voz direta, blue collar, um pouco urgente, como quem aprendeu isso do jeito difícil, a seguinte frase: "[FALA EXATA DO ROTEIRO]"

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: [ação ENXUTA, só o que acontece]

câmera: [fixa / leve push-in]

som ambiente: garagem silenciosa, com um leve eco metálico distante, sem música
```

---

# Prompts de vídeo

### V01 · T1 (gancho café) · usa K01

```text
o avatar (homem) fala em inglês com sotaque americano de Dana Morrison, voz direta, blue collar, um pouco urgente, como quem aprendeu isso do jeito difícil, a seguinte frase: "Nobody's gonna tell you this because your dentist never wants you to find out."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ele inclina a caneca e o café escuro escorre em fio sobre o modelo de dentes manchado, escurecendo ainda mais a superfície já amarelada.

câmera: fixa

som ambiente: garagem silenciosa, com um leve eco metálico distante, sem música
```

### V02 · T1 (gancho vinho) · usa K02

```text
o avatar (homem) fala em inglês com sotaque americano de Dana Morrison, voz direta, blue collar, um pouco urgente, como quem aprendeu isso do jeito difícil, a seguinte frase: "Nobody's gonna tell you this because your dentist never wants you to find out."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ele inclina a garrafa e o vinho tinto escorre em fio sobre o modelo de dentes manchado, contraste forte de cor sobre o amarelo.

câmera: fixa

som ambiente: garagem silenciosa, com um leve eco metálico distante, sem música
```

### V03 · T1 (gancho refrigerante) · usa K03

```text
o avatar (homem) fala em inglês com sotaque americano de Dana Morrison, voz direta, blue collar, um pouco urgente, como quem aprendeu isso do jeito difícil, a seguinte frase: "Nobody's gonna tell you this because your dentist never wants you to find out."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ele inclina a garrafa e o refrigerante escuro escorre com uma leve espuma sobre o modelo de dentes manchado.

câmera: fixa

som ambiente: garagem silenciosa, com um leve eco metálico distante, sem música
```

### V04 · T1 (gancho dentadura) · usa K04

```text
o avatar (homem) fala em inglês com sotaque americano de Dana Morrison, voz direta, blue collar, um pouco urgente, como quem aprendeu isso do jeito difícil, a seguinte frase: "Nobody's gonna tell you this because your dentist never wants you to find out."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ele inclina a chaleira e a água escorre sobre a dentadura manchada em pé no suporte, sem tirar a mancha.

câmera: fixa

som ambiente: garagem silenciosa, com um leve eco metálico distante, sem música
```

### V05 · T1 (gancho protetor bucal) · usa K05

```text
o avatar (homem) fala em inglês com sotaque americano de Dana Morrison, voz direta, blue collar, um pouco urgente, como quem aprendeu isso do jeito difícil, a seguinte frase: "Nobody's gonna tell you this because your dentist never wants you to find out."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ele inclina a chaleira e a água escorre sobre o protetor bucal amarelado apoiado no suporte, sem tirar a mancha.

câmera: fixa

som ambiente: garagem silenciosa, com um leve eco metálico distante, sem música
```

### V06 · T2 · usa K06

```text
o avatar (homem) fala em inglês com sotaque americano de Dana Morrison, voz direta, blue collar, um pouco urgente, como quem aprendeu isso do jeito difícil, a seguinte frase: "Take one tablespoon of coconut oil, half a teaspoon of baking soda, three drops of lemon juice, and mix it into a paste."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ele despeja a colherada de bicarbonato na tigela com o óleo de coco, espreme uma gota de limão e mistura com a colher até formar uma pasta branca lisa.

câmera: fixa

som ambiente: garagem silenciosa, com um leve eco metálico distante, sem música
```

### V07 · T3 · usa K07

```text
o avatar (homem) fala em inglês com sotaque americano de Dana Morrison, voz direta, blue collar, um pouco urgente, como quem aprendeu isso do jeito difícil, a seguinte frase: "Brush with it every morning for two minutes, spit it out, rinse with warm water, and your teeth will look brand new in no time."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ele mantém a tigela erguida perto da câmera, parado, olhando direto pro espectador enquanto fala.

câmera: fixa

som ambiente: garagem silenciosa, com um leve eco metálico distante, sem música
```

### V08 · T4 · usa K07

```text
o avatar (homem) fala em inglês com sotaque americano de Dana Morrison, voz direta, blue collar, um pouco urgente, como quem aprendeu isso do jeito difícil, a seguinte frase: "That funky yellow will disappear, stains will be a thing of the past."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ele continua segurando a tigela erguida perto da câmera, sorriso leve e confiante, sem mexer na pasta.

câmera: fixa

som ambiente: garagem silenciosa, com um leve eco metálico distante, sem música
```

### V09 · T5 · usa K08

```text
o avatar (homem) fala em inglês com sotaque americano de Dana Morrison, voz direta, blue collar, um pouco urgente, como quem aprendeu isso do jeito difícil, a seguinte frase: "But if this issue keeps coming back, you need an anti-detox. Follow and comment teeth,"

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ele aponta o dedo direto pra câmera, tom mais urgente, a tigela parada na bancada entre os antebraços.

câmera: fixa

som ambiente: garagem silenciosa, com um leve eco metálico distante, sem música
```

### V10 · T6 · usa K08

```text
o avatar (homem) fala em inglês com sotaque americano de Dana Morrison, voz direta, blue collar, um pouco urgente, como quem aprendeu isso do jeito difícil, a seguinte frase: "and I'll send you my complete anti-aging routine with the secret for the best results. But make sure you are following first, or I can't reach you."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ele mantém o dedo apontado pra câmera, dá um leve aceno de cabeça confirmando, tom direto até o final.

câmera: fixa

som ambiente: garagem silenciosa, com um leve eco metálico distante, sem música
```

---

## Mapa de âncoras

| Keyframe | Referências a anexar | Modelo |
|---|---|---|
| K01 a K06 | FINGERPRINT DANA MORRISON | Nano Banana 2, 9:16 |
| K07 | o K06 aprovado | Nano Banana 2, 9:16 |
| K08 | FINGERPRINT DANA MORRISON | Nano Banana 2, 9:16 |

Vídeo: Veo 3.1 Lite, Lower Priority, 8 segundos, 1 variação por V, imagem sempre como INITIAL FRAME.

---

## Montagem no CapCut

1. **Escolher UM gancho por vídeo.** Cada vídeo finalizado é V01, V02, V03, V04 ou V05 na abertura,
   seguido sempre de V06, V07, V08, V09 e V10.
2. Cortar cada clipe no fim da fala. O corte do gancho entra no auge do despejo do líquido.
3. Legenda queimada em todos os takes, palavra destacada em amarelo na keyword de comentário
   `teeth`, dentro de T5.
4. Sem música. Só o som ambiente do clipe.
5. Exportar em 9:16, 1080 por 1920.

---

## Gates de qualidade

1. [ ] O prop herói está no lower foreground, mais perto da lente que o rosto, em K01 a K05.
2. [ ] Cada um dos cinco props do hook saiu manchado/amarelado como descrito, nunca já limpo.
3. [ ] Nenhum negative cita nome de órgão, gore ou marca.
4. [ ] Nenhum K mostra rótulo de marca no óleo de coco, no bicarbonato, no café, no vinho ou no
   refrigerante.
5. [ ] A bandeirinha dos EUA aparece e está em foco nos oito keyframes.
6. [ ] Zero joia além da corrente de ouro em todos os keyframes. Sem cruz.
7. [ ] O do-rag preto, a barba branca comprida e o bigode salpicado saem idênticos nos oito
   keyframes.
8. [ ] Zero blur em qualquer imagem, inclusive no pegboard e na prateleira.
9. [ ] Luz neutra de dia. Nenhuma imagem com cast quente.
10. [ ] A fala de cada V bate palavra por palavra com o take do `ROTEIRO.md`.
11. [ ] Nenhum take promete além do que o vídeo original promete (sem claim de saúde/tratamento).
12. [ ] `python checar_entrega.py producao/fitywell_dentes` fechou sem FALHA.
