# Dana Morrison | Ângulo 2 (FityWell) | Pacote de Prompts

Vídeo modelo: `AQO7QAQAw3TozLUxgBe_uOL5Cqa4HhdZTI7prrPVgDFUzWkQwh0CU1OnI7i4Qqz6jsYBcg6axG2pJLhDLtFswS7DPc8ZL0_zm0aPqPk.mp4` (46,7 s, avatar sozinho, receita de cheesecake de iogurte grego)

Referência de identidade: **fingerprint (character consistency sheet) anexado na mensagem original**, trava rosto/corpo/pele/barba. Cenário nasce do texto, usando o cenário canônico da garagem porque ele já cabe na demo sem adaptação (não precisa mostrar forno, o corte pro bolo já assado é off-screen igual ao vídeo original).

Funil: **nenhum, vídeo de crescimento.** CTA fecha em comment `cheesecake` + follow. Sem produto, sem app, sem quiz, sem keyword de conversão.

Avatar 1 de 3 da fila (`AVATAR_QUEUE.md`). Ganchos escolhidos pelo Luigi: 2 (ricota), 4 (tofu sedoso), 5 (mascarpone), 6 (scoop de whey), 1 (cottage cheese).

**Eficiência desta produção:** diferente da `fitywell_dentes`, aqui T2 a T8 não dependem visualmente
de qual base foi usada no hook (a massa já misturada fica parecida não importa a base), então K06,
K07 e K08 são **compartilhados pelos cinco vídeos finais**, sem duplicar.

---

## Índice de geração

| Take | Keyframe | Anexar | Ação de geração |
|---|---|---|---|
| T1 · gancho ricota | K01 | FINGERPRINT DANA MORRISON | GERAR DO ZERO. Ovo quebrado sobre ricota |
| T1 · gancho tofu sedoso | K02 | FINGERPRINT DANA MORRISON | GERAR DO ZERO. Ovo quebrado sobre tofu sedoso |
| T1 · gancho mascarpone | K03 | FINGERPRINT DANA MORRISON | GERAR DO ZERO. Ovo quebrado sobre mascarpone |
| T1 · gancho whey | K04 | FINGERPRINT DANA MORRISON | GERAR DO ZERO. Scoop de whey sobre iogurte grego |
| T1 · gancho cottage cheese | K05 | FINGERPRINT DANA MORRISON | GERAR DO ZERO. Ovo quebrado sobre cottage cheese |
| T2 (compartilhado) | K06 | FINGERPRINT DANA MORRISON | GERAR DO ZERO. Despeja a massa na forma untada |
| T3 a T7 (compartilhado) | K07 | FINGERPRINT DANA MORRISON | GERAR DO ZERO. Segura o cheesecake já assado |
| T8 (compartilhado) | K08 | FINGERPRINT DANA MORRISON | GERAR DO ZERO. Prato com a fatia, apontando pro CTA |

Regra de bolso: **GERAR DO ZERO anexa o fingerprint. EDITAR anexa uma imagem só, o keyframe de origem.**
🚫 Nunca anexar um keyframe editado como origem de outro. **K06, K07 e K08 não editam nenhum K01 a K05**, porque a massa já misturada não carrega mais a identidade visual da base usada no hook.

---

## Trava de identidade e continuidade

- Homem negro americano no início dos cinquenta, pele marrom escura.
- **Do-rag preto de cetim** amarrado na cabeça, com a aba caindo atrás do ombro esquerdo.
- **Barba do queixo comprida e branca**, cheia, bigode escuro salpicado de grisalho.
- Rosto magro e anguloso, maçãs altas, olhos castanhos escuros, olhar direto.
- **Corpo seco e treinado**, ombros largos, antebraços com veias marcadas, mãos grandes e calejadas.
- Pele com textura real, poros visíveis, linhas fundas na testa, pés de galinha, sem maquiagem.
- **Regata canelada PRETA** e **corrente fina de ouro** no pescoço, sem pingente, sem cruz. Calça escura.
- Cenário: bancada de madeira gasta e manchada da garagem, agora dobrando de bancada de receita, parede de pegboard marrom com ferramentas, armário de madeira à direita com potes de ervas rotulados (VALERIAN ROOT, ECHINACEA, MULLEIN), **bandeirinha dos EUA em pé na prateleira**, placa de papelão escrita à mão SLEEP WATER WALK GREENS SUN, porta de garagem branca de enrolar recolhida no alto do quadro.
- Luz **neutra de dia**, entrando pela porta aberta da garagem. Zero blur, tudo em foco nítido.

---

## Trava do prop herói

Cinco bases diferentes no hook (uma por gancho escolhido), descritas em cada K abaixo. De T2 a T8 o
prop é sempre a mesma forma/o mesmo cheesecake assado, sem estágios diferentes entre esses takes
além da evolução natural (massa crua → assado → fatiado).

```text
Sem marca em quadro: ricota, tofu, mascarpone, cottage cheese e whey ficam em potes/latas lisas sem
rótulo. Nunca negar marca no negative, resolver sempre no positivo com objeto liso.
```

## Trava da 2ª pessoa (REF-A)

Não se aplica. Não há segunda pessoa em nenhum take.

---

# Prompts de imagem

## K01 · T1 · GANCHO RICOTA · GERAR DO ZERO · FINGERPRINT DANA MORRISON

> ### 📎 ANEXAR: **1 IMAGEM**
> **1️⃣ FINGERPRINT DANA MORRISON** (character consistency sheet anexado na mensagem original)
>
> ### 🆕 GERAR DO ZERO

```json
{
  "shot_id": "K01_hook_ricotta",
  "reference_use": "Use the attached fingerprint reference ONLY for Dana Morrison's face, identity, body, beard and skin. Do NOT copy its pose, framing or background.",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "identity_main": "The EXACT man from the attached fingerprint reference (Dana Morrison): Black American man in his early fifties, deep dark brown skin, a black satin durag tied tightly over his head with the tail falling behind his left shoulder, dark brown eyes with a direct gaze, a lean angular face with high cheekbones, a wide nose and thick eyebrows, a long full white chin beard with a dark moustache flecked with grey, a lean powerfully trained build with broad shoulders, defined forearms with visible veins, large calloused hands, real skin texture with visible pores, deep forehead lines, crow's feet, no makeup.",
  "wardrobe": "A plain black ribbed tank top and a thin gold chain necklace with no pendant. Dark trousers. No cross, no other jewelry.",
  "prop": "A clear glass mixing bowl filled with thick smooth white ricotta cheese, resting on the workbench. In his raised hand, a whole egg is held directly above the bowl, cracked open at the moment the egg white and yolk begin spilling out onto the ricotta.",
  "scene": "SAME garage workshop as the reference: a scuffed, stained wooden workbench, a brown pegboard wall behind him hung with wrenches, a yellow handled hammer and colorful handled screwdrivers, an open wooden cabinet to the right with glass jars labelled VALERIAN ROOT, ECHINACEA and MULLEIN, a small American flag standing on that shelf, discreet but clearly visible and in sharp focus, a hand lettered cardboard sign taped to the cabinet reading SLEEP WATER WALK GREENS SUN, and the white roll up garage door raised at the top of the frame.",
  "posture": "Standing at the workbench, leaning forward slightly, one hand cracking the egg above the bowl.",
  "composition": "The bowl of ricotta fills the lower two thirds of the frame, closer to the lens than his face. His head and shoulders occupy the upper third. Nothing else competes.",
  "camera": "chest level, straight-on, camera pushed in close toward the bowl",
  "state": "Start frame: the eggshell is cracked open and the yolk is just beginning to drop onto the ricotta, the white already spilling. The ricotta is otherwise undisturbed.",
  "lighting": "Flat neutral daylight spilling in from the open garage door, evenly lighting his face, no warm orange cast and no yellow tint.",
  "realism": "UGC realism, real skin texture with visible pores, individual hair strands, subtle wrinkles, realistic shadows and reflections, iPhone-footage look, phone camera look not professional photography, no AI polish, no beauty smoothing, no blur anywhere, everything in sharp focus including the pegboard and the shelf.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no studio, no plastic skin, no extra fingers, no supernatural lighting, no blur, no artificial lighting, no warm orange color cast, no yellow tint, no jewelry besides the described gold chain, no cross, no second person, no brand label"
}
```

## K02 · T1 · GANCHO TOFU SEDOSO · GERAR DO ZERO · FINGERPRINT DANA MORRISON

> ### 📎 ANEXAR: **1 IMAGEM**
> **1️⃣ FINGERPRINT DANA MORRISON** (character consistency sheet anexado na mensagem original)
>
> ### 🆕 GERAR DO ZERO

```json
{
  "shot_id": "K02_hook_tofu",
  "reference_use": "Use the attached fingerprint reference ONLY for Dana Morrison's face, identity, body, beard and skin. Do NOT copy its pose, framing or background.",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "identity_main": "The EXACT man from the attached fingerprint reference (Dana Morrison): Black American man in his early fifties, deep dark brown skin, a black satin durag tied tightly over his head with the tail falling behind his left shoulder, dark brown eyes with a direct gaze, a lean angular face with high cheekbones, a wide nose and thick eyebrows, a long full white chin beard with a dark moustache flecked with grey, a lean powerfully trained build with broad shoulders, defined forearms with visible veins, large calloused hands, real skin texture with visible pores, deep forehead lines, crow's feet, no makeup.",
  "wardrobe": "A plain black ribbed tank top and a thin gold chain necklace with no pendant. Dark trousers. No cross, no other jewelry.",
  "prop": "A clear glass mixing bowl filled with pale, soft, jiggly silken tofu, resting on the workbench. In his raised hand, a whole egg is held directly above the bowl, cracked open at the moment the egg white and yolk begin spilling out onto the tofu.",
  "scene": "SAME garage workshop as the reference: a scuffed, stained wooden workbench, a brown pegboard wall behind him hung with wrenches, a yellow handled hammer and colorful handled screwdrivers, an open wooden cabinet to the right with glass jars labelled VALERIAN ROOT, ECHINACEA and MULLEIN, a small American flag standing on that shelf, discreet but clearly visible and in sharp focus, a hand lettered cardboard sign taped to the cabinet reading SLEEP WATER WALK GREENS SUN, and the white roll up garage door raised at the top of the frame.",
  "posture": "Standing at the workbench, leaning forward slightly, one hand cracking the egg above the bowl.",
  "composition": "The bowl of tofu fills the lower two thirds of the frame, closer to the lens than his face. His head and shoulders occupy the upper third. Nothing else competes.",
  "camera": "chest level, straight-on, camera pushed in close toward the bowl",
  "state": "Start frame: the eggshell is cracked open and the yolk is just beginning to drop onto the tofu, the white already spilling. The tofu is otherwise undisturbed, smooth and jiggly.",
  "lighting": "Flat neutral daylight spilling in from the open garage door, evenly lighting his face, no warm orange cast and no yellow tint.",
  "realism": "UGC realism, real skin texture with visible pores, individual hair strands, subtle wrinkles, realistic shadows and reflections, iPhone-footage look, phone camera look not professional photography, no AI polish, no beauty smoothing, no blur anywhere, everything in sharp focus including the pegboard and the shelf.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no studio, no plastic skin, no extra fingers, no supernatural lighting, no blur, no artificial lighting, no warm orange color cast, no yellow tint, no jewelry besides the described gold chain, no cross, no second person, no brand label"
}
```

## K03 · T1 · GANCHO MASCARPONE · GERAR DO ZERO · FINGERPRINT DANA MORRISON

> ### 📎 ANEXAR: **1 IMAGEM**
> **1️⃣ FINGERPRINT DANA MORRISON** (character consistency sheet anexado na mensagem original)
>
> ### 🆕 GERAR DO ZERO

```json
{
  "shot_id": "K03_hook_mascarpone",
  "reference_use": "Use the attached fingerprint reference ONLY for Dana Morrison's face, identity, body, beard and skin. Do NOT copy its pose, framing or background.",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "identity_main": "The EXACT man from the attached fingerprint reference (Dana Morrison): Black American man in his early fifties, deep dark brown skin, a black satin durag tied tightly over his head with the tail falling behind his left shoulder, dark brown eyes with a direct gaze, a lean angular face with high cheekbones, a wide nose and thick eyebrows, a long full white chin beard with a dark moustache flecked with grey, a lean powerfully trained build with broad shoulders, defined forearms with visible veins, large calloused hands, real skin texture with visible pores, deep forehead lines, crow's feet, no makeup.",
  "wardrobe": "A plain black ribbed tank top and a thin gold chain necklace with no pendant. Dark trousers. No cross, no other jewelry.",
  "prop": "A clear glass mixing bowl filled with thick pale yellow-white mascarpone, resting on the workbench. In his raised hand, a whole egg is held directly above the bowl, cracked open at the moment the egg white and yolk begin spilling out onto the mascarpone.",
  "scene": "SAME garage workshop as the reference: a scuffed, stained wooden workbench, a brown pegboard wall behind him hung with wrenches, a yellow handled hammer and colorful handled screwdrivers, an open wooden cabinet to the right with glass jars labelled VALERIAN ROOT, ECHINACEA and MULLEIN, a small American flag standing on that shelf, discreet but clearly visible and in sharp focus, a hand lettered cardboard sign taped to the cabinet reading SLEEP WATER WALK GREENS SUN, and the white roll up garage door raised at the top of the frame.",
  "posture": "Standing at the workbench, leaning forward slightly, one hand cracking the egg above the bowl.",
  "composition": "The bowl of mascarpone fills the lower two thirds of the frame, closer to the lens than his face. His head and shoulders occupy the upper third. Nothing else competes.",
  "camera": "chest level, straight-on, camera pushed in close toward the bowl",
  "state": "Start frame: the eggshell is cracked open and the yolk is just beginning to drop onto the mascarpone, the white already spilling. The mascarpone is otherwise undisturbed.",
  "lighting": "Flat neutral daylight spilling in from the open garage door, evenly lighting his face, no warm orange cast and no yellow tint.",
  "realism": "UGC realism, real skin texture with visible pores, individual hair strands, subtle wrinkles, realistic shadows and reflections, iPhone-footage look, phone camera look not professional photography, no AI polish, no beauty smoothing, no blur anywhere, everything in sharp focus including the pegboard and the shelf.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no studio, no plastic skin, no extra fingers, no supernatural lighting, no blur, no artificial lighting, no warm orange color cast, no yellow tint, no jewelry besides the described gold chain, no cross, no second person, no brand label"
}
```

## K04 · T1 · GANCHO WHEY · GERAR DO ZERO · FINGERPRINT DANA MORRISON

> ### 📎 ANEXAR: **1 IMAGEM**
> **1️⃣ FINGERPRINT DANA MORRISON** (character consistency sheet anexado na mensagem original)
>
> ### 🆕 GERAR DO ZERO

```json
{
  "shot_id": "K04_hook_whey",
  "reference_use": "Use the attached fingerprint reference ONLY for Dana Morrison's face, identity, body, beard and skin. Do NOT copy its pose, framing or background.",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "identity_main": "The EXACT man from the attached fingerprint reference (Dana Morrison): Black American man in his early fifties, deep dark brown skin, a black satin durag tied tightly over his head with the tail falling behind his left shoulder, dark brown eyes with a direct gaze, a lean angular face with high cheekbones, a wide nose and thick eyebrows, a long full white chin beard with a dark moustache flecked with grey, a lean powerfully trained build with broad shoulders, defined forearms with visible veins, large calloused hands, real skin texture with visible pores, deep forehead lines, crow's feet, no makeup.",
  "wardrobe": "A plain black ribbed tank top and a thin gold chain necklace with no pendant. Dark trousers. No cross, no other jewelry.",
  "prop": "A clear glass mixing bowl filled with thick white Greek yogurt, resting on the workbench. In his raised hand, a metal measuring scoop filled with pale off-white protein powder is tilted directly above the bowl, the first bit of powder just starting to fall onto the yogurt.",
  "scene": "SAME garage workshop as the reference: a scuffed, stained wooden workbench, a brown pegboard wall behind him hung with wrenches, a yellow handled hammer and colorful handled screwdrivers, an open wooden cabinet to the right with glass jars labelled VALERIAN ROOT, ECHINACEA and MULLEIN, a small American flag standing on that shelf, discreet but clearly visible and in sharp focus, a hand lettered cardboard sign taped to the cabinet reading SLEEP WATER WALK GREENS SUN, and the white roll up garage door raised at the top of the frame.",
  "posture": "Standing at the workbench, leaning forward slightly, one hand tilting the scoop above the bowl.",
  "composition": "The bowl of yogurt fills the lower two thirds of the frame, closer to the lens than his face. His head and shoulders occupy the upper third. Nothing else competes.",
  "camera": "chest level, straight-on, camera pushed in close toward the bowl",
  "state": "Start frame: the scoop is tilted and the first bit of protein powder is just leaving it, about to land on the yogurt. The yogurt is otherwise undisturbed.",
  "lighting": "Flat neutral daylight spilling in from the open garage door, evenly lighting his face, no warm orange cast and no yellow tint.",
  "realism": "UGC realism, real skin texture with visible pores, individual hair strands, subtle wrinkles, realistic shadows and reflections, iPhone-footage look, phone camera look not professional photography, no AI polish, no beauty smoothing, no blur anywhere, everything in sharp focus including the pegboard and the shelf.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no studio, no plastic skin, no extra fingers, no supernatural lighting, no blur, no artificial lighting, no warm orange color cast, no yellow tint, no jewelry besides the described gold chain, no cross, no second person, no brand label, no visible brand text on the scoop"
}
```

## K05 · T1 · GANCHO COTTAGE CHEESE · GERAR DO ZERO · FINGERPRINT DANA MORRISON

> ### 📎 ANEXAR: **1 IMAGEM**
> **1️⃣ FINGERPRINT DANA MORRISON** (character consistency sheet anexado na mensagem original)
>
> ### 🆕 GERAR DO ZERO

```json
{
  "shot_id": "K05_hook_cottage",
  "reference_use": "Use the attached fingerprint reference ONLY for Dana Morrison's face, identity, body, beard and skin. Do NOT copy its pose, framing or background.",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "identity_main": "The EXACT man from the attached fingerprint reference (Dana Morrison): Black American man in his early fifties, deep dark brown skin, a black satin durag tied tightly over his head with the tail falling behind his left shoulder, dark brown eyes with a direct gaze, a lean angular face with high cheekbones, a wide nose and thick eyebrows, a long full white chin beard with a dark moustache flecked with grey, a lean powerfully trained build with broad shoulders, defined forearms with visible veins, large calloused hands, real skin texture with visible pores, deep forehead lines, crow's feet, no makeup.",
  "wardrobe": "A plain black ribbed tank top and a thin gold chain necklace with no pendant. Dark trousers. No cross, no other jewelry.",
  "prop": "A clear glass mixing bowl filled with lumpy white cottage cheese, resting on the workbench. In his raised hand, a whole egg is held directly above the bowl, cracked open at the moment the egg white and yolk begin spilling out onto the cottage cheese.",
  "scene": "SAME garage workshop as the reference: a scuffed, stained wooden workbench, a brown pegboard wall behind him hung with wrenches, a yellow handled hammer and colorful handled screwdrivers, an open wooden cabinet to the right with glass jars labelled VALERIAN ROOT, ECHINACEA and MULLEIN, a small American flag standing on that shelf, discreet but clearly visible and in sharp focus, a hand lettered cardboard sign taped to the cabinet reading SLEEP WATER WALK GREENS SUN, and the white roll up garage door raised at the top of the frame.",
  "posture": "Standing at the workbench, leaning forward slightly, one hand cracking the egg above the bowl.",
  "composition": "The bowl of cottage cheese fills the lower two thirds of the frame, closer to the lens than his face. His head and shoulders occupy the upper third. Nothing else competes.",
  "camera": "chest level, straight-on, camera pushed in close toward the bowl",
  "state": "Start frame: the eggshell is cracked open and the yolk is just beginning to drop onto the cottage cheese, the white already spilling. The cottage cheese is otherwise undisturbed, its curds visible.",
  "lighting": "Flat neutral daylight spilling in from the open garage door, evenly lighting his face, no warm orange cast and no yellow tint.",
  "realism": "UGC realism, real skin texture with visible pores, individual hair strands, subtle wrinkles, realistic shadows and reflections, iPhone-footage look, phone camera look not professional photography, no AI polish, no beauty smoothing, no blur anywhere, everything in sharp focus including the pegboard and the shelf.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no studio, no plastic skin, no extra fingers, no supernatural lighting, no blur, no artificial lighting, no warm orange color cast, no yellow tint, no jewelry besides the described gold chain, no cross, no second person, no brand label"
}
```

## K06 · T2 (compartilhado) · RECEITA/PROTOCOLO · GERAR DO ZERO · FINGERPRINT DANA MORRISON

> ### 📎 ANEXAR: **1 IMAGEM**
> **1️⃣ FINGERPRINT DANA MORRISON** (character consistency sheet anexado na mensagem original)
>
> ### 🆕 GERAR DO ZERO

```json
{
  "shot_id": "K06_pour_pan",
  "reference_use": "Use the attached fingerprint reference ONLY for Dana Morrison's face, identity, body, beard and skin. Do NOT copy its pose, framing or background.",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "identity_main": "The EXACT man from the attached fingerprint reference (Dana Morrison): Black American man in his early fifties, deep dark brown skin, a black satin durag tied tightly over his head with the tail falling behind his left shoulder, dark brown eyes with a direct gaze, a lean angular face with high cheekbones, a wide nose and thick eyebrows, a long full white chin beard with a dark moustache flecked with grey, a lean powerfully trained build with broad shoulders, defined forearms with visible veins, large calloused hands, real skin texture with visible pores, deep forehead lines, crow's feet, no makeup.",
  "wardrobe": "A plain black ribbed tank top and a thin gold chain necklace with no pendant. Dark trousers. No cross, no other jewelry.",
  "prop": "He tilts a clear glass mixing bowl of smooth, pale cream batter, pouring it into a round metal springform pan with a lightly greased bottom, resting on the workbench.",
  "scene": "SAME garage workshop as the reference: a scuffed, stained wooden workbench, a brown pegboard wall behind him hung with wrenches, a yellow handled hammer and colorful handled screwdrivers, an open wooden cabinet to the right with glass jars labelled VALERIAN ROOT, ECHINACEA and MULLEIN, a small American flag standing on that shelf, discreet but clearly visible and in sharp focus, a hand lettered cardboard sign taped to the cabinet reading SLEEP WATER WALK GREENS SUN, and the white roll up garage door raised at the top of the frame.",
  "posture": "Standing at the workbench, leaning forward slightly, tilting the bowl over the pan with both hands.",
  "composition": "The pan and the pouring stream of batter fill the lower two thirds of the frame, closer to the lens than his face. His head and shoulders occupy the upper third.",
  "camera": "chest level, straight-on, camera pushed in close toward the pan",
  "state": "Start frame: the batter is mid-pour, a thick smooth stream falling from the bowl into the pan, which is already partly filled.",
  "lighting": "Flat neutral daylight spilling in from the open garage door, evenly lighting his face, no warm orange cast and no yellow tint.",
  "realism": "UGC realism, real skin texture with visible pores, individual hair strands, subtle wrinkles, realistic shadows and reflections, iPhone-footage look, phone camera look not professional photography, no AI polish, no beauty smoothing, no blur anywhere, everything in sharp focus including the pegboard and the shelf.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no studio, no plastic skin, no extra fingers, no supernatural lighting, no blur, no artificial lighting, no warm orange color cast, no yellow tint, no jewelry besides the described gold chain, no cross, no second person, no brand label"
}
```

## K07 · T3 a T7 (compartilhado) · RESULTADO/BENEFÍCIOS/MECANISMO/AUTORIDADE · GERAR DO ZERO · FINGERPRINT DANA MORRISON

> ### 📎 ANEXAR: **1 IMAGEM**
> **1️⃣ FINGERPRINT DANA MORRISON** (character consistency sheet anexado na mensagem original)
>
> ### 🆕 GERAR DO ZERO

```json
{
  "shot_id": "K07_baked_cheesecake",
  "reference_use": "Use the attached fingerprint reference ONLY for Dana Morrison's face, identity, body, beard and skin. Do NOT copy its pose, framing or background.",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "identity_main": "The EXACT man from the attached fingerprint reference (Dana Morrison): Black American man in his early fifties, deep dark brown skin, a black satin durag tied tightly over his head with the tail falling behind his left shoulder, dark brown eyes with a direct gaze, a lean angular face with high cheekbones, a wide nose and thick eyebrows, a long full white chin beard with a dark moustache flecked with grey, a lean powerfully trained build with broad shoulders, defined forearms with visible veins, large calloused hands, real skin texture with visible pores, deep forehead lines, crow's feet, no makeup.",
  "wardrobe": "A plain black ribbed tank top and a thin gold chain necklace with no pendant. Dark trousers. No cross, no other jewelry. His hands are covered by a pair of plain quilted oven mitts.",
  "prop": "He holds the same round metal springform pan close to the camera with both mitted hands, now containing a fully baked cheesecake with a golden brown top, its edges lightly caramelized.",
  "scene": "SAME garage workshop as the reference: a scuffed, stained wooden workbench, a brown pegboard wall behind him hung with wrenches, a yellow handled hammer and colorful handled screwdrivers, an open wooden cabinet to the right with glass jars labelled VALERIAN ROOT, ECHINACEA and MULLEIN, a small American flag standing on that shelf, discreet but clearly visible and in sharp focus, a hand lettered cardboard sign taped to the cabinet reading SLEEP WATER WALK GREENS SUN, and the white roll up garage door raised at the top of the frame.",
  "posture": "Standing at the workbench, holding the pan up toward the camera with both hands, confident and direct expression.",
  "composition": "The pan with the baked cheesecake fills the lower half of the frame, closer to the lens than his face. His head and shoulders occupy the upper half.",
  "camera": "chest level, straight-on, camera pushed in close toward the pan",
  "state": "Start frame: the baked cheesecake is held steady toward the camera. Nothing moves or changes.",
  "lighting": "Flat neutral daylight spilling in from the open garage door, evenly lighting his face, no warm orange cast and no yellow tint.",
  "realism": "UGC realism, real skin texture with visible pores, individual hair strands, subtle wrinkles, realistic shadows and reflections, iPhone-footage look, phone camera look not professional photography, no AI polish, no beauty smoothing, no blur anywhere, everything in sharp focus including the pegboard and the shelf.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no studio, no plastic skin, no extra fingers, no supernatural lighting, no blur, no artificial lighting, no warm orange color cast, no yellow tint, no jewelry besides the described gold chain, no cross, no second person, no brand label"
}
```

## K08 · T8 (compartilhado) · CTA + FOLLOW GATE · GERAR DO ZERO · FINGERPRINT DANA MORRISON

> ### 📎 ANEXAR: **1 IMAGEM**
> **1️⃣ FINGERPRINT DANA MORRISON** (character consistency sheet anexado na mensagem original)
>
> ### 🆕 GERAR DO ZERO

```json
{
  "shot_id": "K08_cta_slice",
  "reference_use": "Use the attached fingerprint reference ONLY for Dana Morrison's face, identity, body, beard and skin. Do NOT copy its pose, framing or background.",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "identity_main": "The EXACT man from the attached fingerprint reference (Dana Morrison): Black American man in his early fifties, deep dark brown skin, a black satin durag tied tightly over his head with the tail falling behind his left shoulder, dark brown eyes with a direct gaze, a lean angular face with high cheekbones, a wide nose and thick eyebrows, a long full white chin beard with a dark moustache flecked with grey, a lean powerfully trained build with broad shoulders, defined forearms with visible veins, large calloused hands, real skin texture with visible pores, deep forehead lines, crow's feet, no makeup.",
  "wardrobe": "A plain black ribbed tank top and a thin gold chain necklace with no pendant. Dark trousers. No cross, no other jewelry.",
  "prop": "He holds a plain white plate in one hand, with a single cut slice of the baked cheesecake on it, creamy pale interior visible from the cut edge. His other hand points directly toward the camera, index finger extended.",
  "scene": "SAME garage workshop as the reference: a scuffed, stained wooden workbench, a brown pegboard wall behind him hung with wrenches, a yellow handled hammer and colorful handled screwdrivers, an open wooden cabinet to the right with glass jars labelled VALERIAN ROOT, ECHINACEA and MULLEIN, a small American flag standing on that shelf, discreet but clearly visible and in sharp focus, a hand lettered cardboard sign taped to the cabinet reading SLEEP WATER WALK GREENS SUN, and the white roll up garage door raised at the top of the frame.",
  "posture": "Standing at the workbench, holding the plate toward the camera with one hand, the other hand raised in an urgent pointing gesture.",
  "composition": "The plate with the slice occupies the lower third of the frame, his pointing hand and upper body fill the rest, closer to the lens than a normal talking shot.",
  "camera": "chest level, straight-on, camera pushed in close",
  "state": "Start frame: the hand is mid gesture, finger extended toward the camera, the plate held steady.",
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

### V01 · T1 (gancho ricota) · usa K01

```text
o avatar (homem) fala em inglês com sotaque americano de Dana Morrison, voz direta, blue collar, um pouco urgente, como quem aprendeu isso do jeito difícil, a seguinte frase: "How old were you when you found out that if you crack an egg into ricotta cheese and whisk it until the batter is completely smooth,"

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ele quebra o ovo e a gema cai dentro da tigela de ricota, a clara já escorrendo por cima.

câmera: fixa

som ambiente: garagem silenciosa, com um leve eco metálico distante, sem música
```

### V02 · T1 (gancho tofu sedoso) · usa K02

```text
o avatar (homem) fala em inglês com sotaque americano de Dana Morrison, voz direta, blue collar, um pouco urgente, como quem aprendeu isso do jeito difícil, a seguinte frase: "How old were you when you found out that if you crack an egg into silken tofu and whisk it until the batter is completely smooth,"

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ele quebra o ovo e a gema cai dentro da tigela de tofu sedoso, a clara já escorrendo por cima.

câmera: fixa

som ambiente: garagem silenciosa, com um leve eco metálico distante, sem música
```

### V03 · T1 (gancho mascarpone) · usa K03

```text
o avatar (homem) fala em inglês com sotaque americano de Dana Morrison, voz direta, blue collar, um pouco urgente, como quem aprendeu isso do jeito difícil, a seguinte frase: "How old were you when you found out that if you crack an egg into mascarpone and whisk it until the batter is completely smooth,"

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ele quebra o ovo e a gema cai dentro da tigela de mascarpone, a clara já escorrendo por cima.

câmera: fixa

som ambiente: garagem silenciosa, com um leve eco metálico distante, sem música
```

### V04 · T1 (gancho whey) · usa K04

```text
o avatar (homem) fala em inglês com sotaque americano de Dana Morrison, voz direta, blue collar, um pouco urgente, como quem aprendeu isso do jeito difícil, a seguinte frase: "How old were you when you found out that if you stir a scoop of protein powder into Greek yogurt and whisk it until the batter is completely smooth,"

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ele inclina a colher medidora e o pó de proteína cai dentro da tigela de iogurte grego.

câmera: fixa

som ambiente: garagem silenciosa, com um leve eco metálico distante, sem música
```

### V05 · T1 (gancho cottage cheese) · usa K05

```text
o avatar (homem) fala em inglês com sotaque americano de Dana Morrison, voz direta, blue collar, um pouco urgente, como quem aprendeu isso do jeito difícil, a seguinte frase: "How old were you when you found out that if you crack an egg into cottage cheese and whisk it until the batter is completely smooth,"

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ele quebra o ovo e a gema cai dentro da tigela de cottage cheese, a clara já escorrendo por cima.

câmera: fixa

som ambiente: garagem silenciosa, com um leve eco metálico distante, sem música
```

### V06 · T2 · usa K06

```text
o avatar (homem) fala em inglês com sotaque americano de Dana Morrison, voz direta, blue collar, um pouco urgente, como quem aprendeu isso do jeito difícil, a seguinte frase: "stirring in a little raw honey and vanilla, pour it into a greased pan, bake it at 350 for 20 minutes and let it chill."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ele despeja a massa lisa da tigela dentro da forma untada, enchendo até a borda.

câmera: fixa

som ambiente: garagem silenciosa, com um leve eco metálico distante, sem música
```

### V07 · T3 · usa K07

```text
o avatar (homem) fala em inglês com sotaque americano de Dana Morrison, voz direta, blue collar, um pouco urgente, como quem aprendeu isso do jeito difícil, a seguinte frase: "You end up with a creamy cheesecake that not only tastes like the real deal, but is easy on the stomach,"

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ele mantém a forma com o cheesecake assado erguida perto da câmera, parado, olhando direto pro espectador.

câmera: fixa

som ambiente: garagem silenciosa, com um leve eco metálico distante, sem música
```

### V08 · T4 · usa K07

```text
o avatar (homem) fala em inglês com sotaque americano de Dana Morrison, voz direta, blue collar, um pouco urgente, como quem aprendeu isso do jeito difícil, a seguinte frase: "feeds the good bacteria in your gut and will not send your blood sugar through the roof."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ele continua segurando a forma erguida, aceno leve de cabeça confirmando o que fala.

câmera: fixa

som ambiente: garagem silenciosa, com um leve eco metálico distante, sem música
```

### V09 · T5 · usa K07

```text
o avatar (homem) fala em inglês com sotaque americano de Dana Morrison, voz direta, blue collar, um pouco urgente, como quem aprendeu isso do jeito difícil, a seguinte frase: "And the best part, the eggs in the yogurt carry tryptophan, the sleep amino acid."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ele continua segurando a forma erguida, expressão de quem revela um detalhe importante.

câmera: fixa

som ambiente: garagem silenciosa, com um leve eco metálico distante, sem música
```

### V10 · T6 · usa K07

```text
o avatar (homem) fala em inglês com sotaque americano de Dana Morrison, voz direta, blue collar, um pouco urgente, como quem aprendeu isso do jeito difícil, a seguinte frase: "Combined with raw honey, it winds your body down for deep sleep naturally, making it the perfect bedtime snack."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ele continua segurando a forma erguida, tom calmo e satisfeito.

câmera: fixa

som ambiente: garagem silenciosa, com um leve eco metálico distante, sem música
```

### V11 · T7 · usa K07

```text
o avatar (homem) fala em inglês com sotaque americano de Dana Morrison, voz direta, blue collar, um pouco urgente, como quem aprendeu isso do jeito difícil, a seguinte frase: "I have recipes like this for every sweet treat you can think of. No refined sugar, low carbs, high protein, and they taste amazing."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ele continua segurando a forma erguida, sorriso confiante enquanto lista os benefícios.

câmera: fixa

som ambiente: garagem silenciosa, com um leve eco metálico distante, sem música
```

### V12 · T8 · usa K08

```text
o avatar (homem) fala em inglês com sotaque americano de Dana Morrison, voz direta, blue collar, um pouco urgente, como quem aprendeu isso do jeito difícil, a seguinte frase: "Comment cheesecake if you want more like this and follow me so you do not miss a single one."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ele aponta o dedo direto pra câmera, segurando o prato com a fatia na outra mão.

câmera: fixa

som ambiente: garagem silenciosa, com um leve eco metálico distante, sem música
```

---

## Mapa de âncoras

| Keyframe | Referências a anexar | Modelo |
|---|---|---|
| K01 a K08 | FINGERPRINT DANA MORRISON | Nano Banana 2, 9:16 |

Vídeo: Veo 3.1 Lite, Lower Priority, 8 segundos, 1 variação por V, imagem sempre como INITIAL FRAME.

---

## Montagem no CapCut

1. **Escolher UM gancho por vídeo.** Cada vídeo finalizado é V01, V02, V03, V04 ou V05 na abertura,
   seguido sempre de V06 a V12.
2. Cortar cada clipe no fim da fala.
3. Legenda queimada em todos os takes, palavra destacada em amarelo na keyword de comentário
   `cheesecake`, dentro de T8.
4. Sem música. Só o som ambiente do clipe.
5. Exportar em 9:16, 1080 por 1920.

---

## Gates de qualidade

1. [ ] O prop herói está no lower foreground, mais perto da lente que o rosto, em todos os keyframes.
2. [ ] A base de cada hook (ricota, tofu, mascarpone, iogurte, cottage) sai com a textura certa.
3. [ ] Nenhum negative cita nome de órgão, gore ou marca.
4. [ ] Nenhum K mostra rótulo de marca na ricota, no tofu, no mascarpone, no whey ou no cottage cheese.
5. [ ] A bandeirinha dos EUA aparece e está em foco nos oito keyframes.
6. [ ] Zero joia além da corrente de ouro em todos os keyframes. Sem cruz.
7. [ ] O do-rag preto, a barba branca comprida e o bigode salpicado saem idênticos nos oito keyframes.
8. [ ] Zero blur em qualquer imagem, inclusive no pegboard e na prateleira.
9. [ ] Luz neutra de dia. Nenhuma imagem com cast quente.
10. [ ] A fala de cada V bate palavra por palavra com o take do `ROTEIRO.md` (ou com a variação de
    gancho aprovada, no caso dos T1).
11. [ ] Nenhum take promete além do que o vídeo original promete (sem claim de tratamento/cura).
12. [ ] `python checar_entrega.py producao/fitywell_cheesecake` fechou sem FALHA.
