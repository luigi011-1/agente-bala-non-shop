# Jamie Anderson | Ângulo 2 (FityWell) | Pacote de Prompts

Vídeo modelo: `AQO7QAQAw3TozLUxgBe_uOL5Cqa4HhdZTI7prrPVgDFUzWkQwh0CU1OnI7i4Qqz6jsYBcg6axG2pJLhDLtFswS7DPc8ZL0_zm0aPqPk.mp4` (46,7 s, avatar sozinho, receita de cheesecake de iogurte grego)

Referência de identidade: **fingerprint (character consistency sheet) anexado na mensagem original**, trava rosto/corpo/pele/barba. Cenário nasce do texto.

**Adaptação de cenário:** o banco do motorista não comporta a receita. Ele passa o vídeo inteiro no
**porta-malas aberto do SUV, no mesmo estacionamento**, mesma adaptação já validada em
`fitywell_dentes`. O forno nunca aparece em quadro, a forma sai já assada por um corte, igual ao
vídeo original.

Funil: **nenhum, vídeo de crescimento.** CTA fecha em comment `cheesecake` + follow. Sem produto,
sem app, sem quiz, sem keyword de conversão.

Avatar 2 de 3 da fila (`AVATAR_QUEUE.md`). Ganchos escolhidos pelo Luigi: 2 (ricota), 4 (tofu
sedoso), 5 (mascarpone), 6 (scoop de whey), 1 (cottage cheese). Pacote anterior (Dana Morrison)
arquivado em `PROMPTS_DANA_MORRISON.md`/`FLOW_DANA_MORRISON.md`.

**Eficiência desta produção:** K06, K07 e K08 (massa na forma, cheesecake assado, CTA) são
**compartilhados pelos cinco vídeos finais**, porque a massa já misturada fica igual não importa a
base usada no hook.

---

## Índice de geração

| Take | Keyframe | Anexar | Ação de geração |
|---|---|---|---|
| T1 · gancho ricota | K01 | FINGERPRINT JAMIE ANDERSON | GERAR DO ZERO. Ovo quebrado sobre ricota |
| T1 · gancho tofu sedoso | K02 | FINGERPRINT JAMIE ANDERSON | GERAR DO ZERO. Ovo quebrado sobre tofu sedoso |
| T1 · gancho mascarpone | K03 | FINGERPRINT JAMIE ANDERSON | GERAR DO ZERO. Ovo quebrado sobre mascarpone |
| T1 · gancho whey | K04 | FINGERPRINT JAMIE ANDERSON | GERAR DO ZERO. Scoop de whey sobre iogurte grego |
| T1 · gancho cottage cheese | K05 | FINGERPRINT JAMIE ANDERSON | GERAR DO ZERO. Ovo quebrado sobre cottage cheese |
| T2 (compartilhado) | K06 | FINGERPRINT JAMIE ANDERSON | GERAR DO ZERO. Despeja a massa na forma untada |
| T3 a T7 (compartilhado) | K07 | FINGERPRINT JAMIE ANDERSON | GERAR DO ZERO. Segura o cheesecake já assado |
| T8 (compartilhado) | K08 | FINGERPRINT JAMIE ANDERSON | GERAR DO ZERO. Prato com a fatia, apontando pro CTA |

Regra de bolso: **GERAR DO ZERO anexa o fingerprint. EDITAR anexa uma imagem só, o keyframe de origem.**
🚫 Nunca anexar um keyframe editado como origem de outro. K06, K07 e K08 não editam nenhum K01 a K05.

---

## Trava de identidade e continuidade

- Homem negro americano em meados dos cinquenta, pele marrom média.
- **Cabelo curto, corte baixo, muito grisalho** nas têmporas e no topo, entradas naturais.
- **Barba curta cheia, quase toda branca**, com bigode grisalho.
- Rosto simétrico, testa alta, **pintas e sardas visíveis nas maçãs do rosto**, olhos castanhos escuros, sobrancelhas grisalhas.
- Porte atlético e enxuto, ombros largos, sem volume de academia. Pele com textura real, linhas na testa, pés de galinha, sem maquiagem.
- **Camisa de linho BRANCA de botão**, colarinho aberto sem gravata, **mangas dobradas até o antebraço**, calça escura. **Sem joia nenhuma, sem relógio, sem cruz.**
- Cenário: em pé atrás do porta-malas aberto do próprio SUV, num estacionamento americano comum, usando o piso do porta-malas como bancada. Pela janela traseira e ao redor: um sedan azul e um SUV cinza estacionados, uma fileira de lojas de tijolo com toldos ao fundo, **adesivo da bandeira dos EUA no canto do vidro traseiro**, discreto e em foco.
- Luz **neutra de dia nublado**. Zero blur, tudo em foco nítido.

---

## Trava do prop herói

Cinco bases diferentes no hook (uma por gancho escolhido), descritas em cada K abaixo. De T2 a T8 o
prop é sempre a mesma forma/o mesmo cheesecake assado.

```text
Sem marca em quadro: ricota, tofu, mascarpone, cottage cheese e whey ficam em potes/latas lisas sem
rótulo. Nunca negar marca no negative, resolver sempre no positivo com objeto liso.
```

## Trava da 2ª pessoa (REF-A)

Não se aplica. Não há segunda pessoa em nenhum take.

---

# Prompts de imagem

## K01 · T1 · GANCHO RICOTA · GERAR DO ZERO · FINGERPRINT JAMIE ANDERSON

> ### 📎 ANEXAR: **1 IMAGEM**
> **1️⃣ FINGERPRINT JAMIE ANDERSON** (character consistency sheet anexado na mensagem original)
>
> ### 🆕 GERAR DO ZERO

```json
{
  "shot_id": "K01_hook_ricotta",
  "reference_use": "Use the attached fingerprint reference ONLY for Jamie Anderson's face, identity, body and skin. Do NOT copy its pose, framing or background.",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "identity_main": "The EXACT man from the attached fingerprint reference (Jamie Anderson): Black American man in his mid fifties, medium brown skin, short low-cut hair heavily greyed at the temples and crown with a natural hairline, a short full beard almost entirely white with a greying moustache, a symmetric face with a high forehead, visible moles and freckles on his cheekbones, dark brown eyes, grey eyebrows, lean athletic build with wide shoulders, real skin texture with visible pores, forehead lines and crow's feet, no makeup.",
  "wardrobe": "A white linen button-up shirt, collar open, no tie, sleeves rolled to the forearm, dark trousers. No jewelry of any kind, no watch.",
  "prop": "A clear glass mixing bowl filled with thick smooth white ricotta cheese, resting on the tailgate's cargo floor. In his raised hand, a whole egg is held directly above the bowl, cracked open at the moment the egg white and yolk begin spilling out onto the ricotta.",
  "scene": "Standing behind the raised tailgate of his own parked SUV in an ordinary American parking lot, the flat cargo floor of the open trunk serving as a makeshift workbench in front of him. Through the open tailgate and rear window, an ordinary American parking lot is visible with a blue sedan and a grey SUV parked nearby and a row of brick storefronts with awnings in the distance. A small American flag decal sits on the corner of the rear window glass, discreet but clearly visible and in sharp focus.",
  "posture": "Leaning forward slightly over the open tailgate, one hand cracking the egg above the bowl.",
  "composition": "The bowl of ricotta fills the lower two thirds of the frame, closer to the lens than his face. His head and shoulders occupy the upper third.",
  "camera": "chest level, straight-on, camera pushed in close toward the bowl",
  "state": "Start frame: the eggshell is cracked open and the yolk is just beginning to drop onto the ricotta, the white already spilling. The ricotta is otherwise undisturbed.",
  "lighting": "Flat neutral daylight under an overcast sky, evenly lighting his face, no warm orange cast and no yellow tint.",
  "realism": "UGC realism, real skin texture with visible pores, individual hair strands, subtle wrinkles, realistic shadows and reflections, iPhone-footage look, phone camera look not professional photography, no AI polish, no beauty smoothing, no blur anywhere, everything in sharp focus including the parking lot and the storefronts.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no studio, no plastic skin, no extra fingers, no supernatural lighting, no blur, no artificial lighting, no warm orange color cast, no yellow tint, no jewelry, no watch, no cross, no second person, no brand label"
}
```

## K02 · T1 · GANCHO TOFU SEDOSO · GERAR DO ZERO · FINGERPRINT JAMIE ANDERSON

> ### 📎 ANEXAR: **1 IMAGEM**
> **1️⃣ FINGERPRINT JAMIE ANDERSON** (character consistency sheet anexado na mensagem original)
>
> ### 🆕 GERAR DO ZERO

```json
{
  "shot_id": "K02_hook_tofu",
  "reference_use": "Use the attached fingerprint reference ONLY for Jamie Anderson's face, identity, body and skin. Do NOT copy its pose, framing or background.",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "identity_main": "The EXACT man from the attached fingerprint reference (Jamie Anderson): Black American man in his mid fifties, medium brown skin, short low-cut hair heavily greyed at the temples and crown with a natural hairline, a short full beard almost entirely white with a greying moustache, a symmetric face with a high forehead, visible moles and freckles on his cheekbones, dark brown eyes, grey eyebrows, lean athletic build with wide shoulders, real skin texture with visible pores, forehead lines and crow's feet, no makeup.",
  "wardrobe": "A white linen button-up shirt, collar open, no tie, sleeves rolled to the forearm, dark trousers. No jewelry of any kind, no watch.",
  "prop": "A clear glass mixing bowl filled with pale, soft, jiggly silken tofu, resting on the tailgate's cargo floor. In his raised hand, a whole egg is held directly above the bowl, cracked open at the moment the egg white and yolk begin spilling out onto the tofu.",
  "scene": "Standing behind the raised tailgate of his own parked SUV in an ordinary American parking lot, the flat cargo floor of the open trunk serving as a makeshift workbench in front of him. Through the open tailgate and rear window, an ordinary American parking lot is visible with a blue sedan and a grey SUV parked nearby and a row of brick storefronts with awnings in the distance. A small American flag decal sits on the corner of the rear window glass, discreet but clearly visible and in sharp focus.",
  "posture": "Leaning forward slightly over the open tailgate, one hand cracking the egg above the bowl.",
  "composition": "The bowl of tofu fills the lower two thirds of the frame, closer to the lens than his face. His head and shoulders occupy the upper third.",
  "camera": "chest level, straight-on, camera pushed in close toward the bowl",
  "state": "Start frame: the eggshell is cracked open and the yolk is just beginning to drop onto the tofu, the white already spilling. The tofu is otherwise undisturbed, smooth and jiggly.",
  "lighting": "Flat neutral daylight under an overcast sky, evenly lighting his face, no warm orange cast and no yellow tint.",
  "realism": "UGC realism, real skin texture with visible pores, individual hair strands, subtle wrinkles, realistic shadows and reflections, iPhone-footage look, phone camera look not professional photography, no AI polish, no beauty smoothing, no blur anywhere, everything in sharp focus including the parking lot and the storefronts.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no studio, no plastic skin, no extra fingers, no supernatural lighting, no blur, no artificial lighting, no warm orange color cast, no yellow tint, no jewelry, no watch, no cross, no second person, no brand label"
}
```

## K03 · T1 · GANCHO MASCARPONE · GERAR DO ZERO · FINGERPRINT JAMIE ANDERSON

> ### 📎 ANEXAR: **1 IMAGEM**
> **1️⃣ FINGERPRINT JAMIE ANDERSON** (character consistency sheet anexado na mensagem original)
>
> ### 🆕 GERAR DO ZERO

```json
{
  "shot_id": "K03_hook_mascarpone",
  "reference_use": "Use the attached fingerprint reference ONLY for Jamie Anderson's face, identity, body and skin. Do NOT copy its pose, framing or background.",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "identity_main": "The EXACT man from the attached fingerprint reference (Jamie Anderson): Black American man in his mid fifties, medium brown skin, short low-cut hair heavily greyed at the temples and crown with a natural hairline, a short full beard almost entirely white with a greying moustache, a symmetric face with a high forehead, visible moles and freckles on his cheekbones, dark brown eyes, grey eyebrows, lean athletic build with wide shoulders, real skin texture with visible pores, forehead lines and crow's feet, no makeup.",
  "wardrobe": "A white linen button-up shirt, collar open, no tie, sleeves rolled to the forearm, dark trousers. No jewelry of any kind, no watch.",
  "prop": "A clear glass mixing bowl filled with thick pale yellow-white mascarpone, resting on the tailgate's cargo floor. In his raised hand, a whole egg is held directly above the bowl, cracked open at the moment the egg white and yolk begin spilling out onto the mascarpone.",
  "scene": "Standing behind the raised tailgate of his own parked SUV in an ordinary American parking lot, the flat cargo floor of the open trunk serving as a makeshift workbench in front of him. Through the open tailgate and rear window, an ordinary American parking lot is visible with a blue sedan and a grey SUV parked nearby and a row of brick storefronts with awnings in the distance. A small American flag decal sits on the corner of the rear window glass, discreet but clearly visible and in sharp focus.",
  "posture": "Leaning forward slightly over the open tailgate, one hand cracking the egg above the bowl.",
  "composition": "The bowl of mascarpone fills the lower two thirds of the frame, closer to the lens than his face. His head and shoulders occupy the upper third.",
  "camera": "chest level, straight-on, camera pushed in close toward the bowl",
  "state": "Start frame: the eggshell is cracked open and the yolk is just beginning to drop onto the mascarpone, the white already spilling. The mascarpone is otherwise undisturbed.",
  "lighting": "Flat neutral daylight under an overcast sky, evenly lighting his face, no warm orange cast and no yellow tint.",
  "realism": "UGC realism, real skin texture with visible pores, individual hair strands, subtle wrinkles, realistic shadows and reflections, iPhone-footage look, phone camera look not professional photography, no AI polish, no beauty smoothing, no blur anywhere, everything in sharp focus including the parking lot and the storefronts.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no studio, no plastic skin, no extra fingers, no supernatural lighting, no blur, no artificial lighting, no warm orange color cast, no yellow tint, no jewelry, no watch, no cross, no second person, no brand label"
}
```

## K04 · T1 · GANCHO WHEY · GERAR DO ZERO · FINGERPRINT JAMIE ANDERSON

> ### 📎 ANEXAR: **1 IMAGEM**
> **1️⃣ FINGERPRINT JAMIE ANDERSON** (character consistency sheet anexado na mensagem original)
>
> ### 🆕 GERAR DO ZERO

```json
{
  "shot_id": "K04_hook_whey",
  "reference_use": "Use the attached fingerprint reference ONLY for Jamie Anderson's face, identity, body and skin. Do NOT copy its pose, framing or background.",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "identity_main": "The EXACT man from the attached fingerprint reference (Jamie Anderson): Black American man in his mid fifties, medium brown skin, short low-cut hair heavily greyed at the temples and crown with a natural hairline, a short full beard almost entirely white with a greying moustache, a symmetric face with a high forehead, visible moles and freckles on his cheekbones, dark brown eyes, grey eyebrows, lean athletic build with wide shoulders, real skin texture with visible pores, forehead lines and crow's feet, no makeup.",
  "wardrobe": "A white linen button-up shirt, collar open, no tie, sleeves rolled to the forearm, dark trousers. No jewelry of any kind, no watch.",
  "prop": "A clear glass mixing bowl filled with thick white Greek yogurt, resting on the tailgate's cargo floor. In his raised hand, a metal measuring scoop filled with pale off-white protein powder is tilted directly above the bowl, the first bit of powder just starting to fall onto the yogurt.",
  "scene": "Standing behind the raised tailgate of his own parked SUV in an ordinary American parking lot, the flat cargo floor of the open trunk serving as a makeshift workbench in front of him. Through the open tailgate and rear window, an ordinary American parking lot is visible with a blue sedan and a grey SUV parked nearby and a row of brick storefronts with awnings in the distance. A small American flag decal sits on the corner of the rear window glass, discreet but clearly visible and in sharp focus.",
  "posture": "Leaning forward slightly over the open tailgate, one hand tilting the scoop above the bowl.",
  "composition": "The bowl of yogurt fills the lower two thirds of the frame, closer to the lens than his face. His head and shoulders occupy the upper third.",
  "camera": "chest level, straight-on, camera pushed in close toward the bowl",
  "state": "Start frame: the scoop is tilted and the first bit of protein powder is just leaving it, about to land on the yogurt. The yogurt is otherwise undisturbed.",
  "lighting": "Flat neutral daylight under an overcast sky, evenly lighting his face, no warm orange cast and no yellow tint.",
  "realism": "UGC realism, real skin texture with visible pores, individual hair strands, subtle wrinkles, realistic shadows and reflections, iPhone-footage look, phone camera look not professional photography, no AI polish, no beauty smoothing, no blur anywhere, everything in sharp focus including the parking lot and the storefronts.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no studio, no plastic skin, no extra fingers, no supernatural lighting, no blur, no artificial lighting, no warm orange color cast, no yellow tint, no jewelry, no watch, no cross, no second person, no brand label, no visible brand text on the scoop"
}
```

## K05 · T1 · GANCHO COTTAGE CHEESE · GERAR DO ZERO · FINGERPRINT JAMIE ANDERSON

> ### 📎 ANEXAR: **1 IMAGEM**
> **1️⃣ FINGERPRINT JAMIE ANDERSON** (character consistency sheet anexado na mensagem original)
>
> ### 🆕 GERAR DO ZERO

```json
{
  "shot_id": "K05_hook_cottage",
  "reference_use": "Use the attached fingerprint reference ONLY for Jamie Anderson's face, identity, body and skin. Do NOT copy its pose, framing or background.",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "identity_main": "The EXACT man from the attached fingerprint reference (Jamie Anderson): Black American man in his mid fifties, medium brown skin, short low-cut hair heavily greyed at the temples and crown with a natural hairline, a short full beard almost entirely white with a greying moustache, a symmetric face with a high forehead, visible moles and freckles on his cheekbones, dark brown eyes, grey eyebrows, lean athletic build with wide shoulders, real skin texture with visible pores, forehead lines and crow's feet, no makeup.",
  "wardrobe": "A white linen button-up shirt, collar open, no tie, sleeves rolled to the forearm, dark trousers. No jewelry of any kind, no watch.",
  "prop": "A clear glass mixing bowl filled with lumpy white cottage cheese, resting on the tailgate's cargo floor. In his raised hand, a whole egg is held directly above the bowl, cracked open at the moment the egg white and yolk begin spilling out onto the cottage cheese.",
  "scene": "Standing behind the raised tailgate of his own parked SUV in an ordinary American parking lot, the flat cargo floor of the open trunk serving as a makeshift workbench in front of him. Through the open tailgate and rear window, an ordinary American parking lot is visible with a blue sedan and a grey SUV parked nearby and a row of brick storefronts with awnings in the distance. A small American flag decal sits on the corner of the rear window glass, discreet but clearly visible and in sharp focus.",
  "posture": "Leaning forward slightly over the open tailgate, one hand cracking the egg above the bowl.",
  "composition": "The bowl of cottage cheese fills the lower two thirds of the frame, closer to the lens than his face. His head and shoulders occupy the upper third.",
  "camera": "chest level, straight-on, camera pushed in close toward the bowl",
  "state": "Start frame: the eggshell is cracked open and the yolk is just beginning to drop onto the cottage cheese, the white already spilling. The cottage cheese is otherwise undisturbed, its curds visible.",
  "lighting": "Flat neutral daylight under an overcast sky, evenly lighting his face, no warm orange cast and no yellow tint.",
  "realism": "UGC realism, real skin texture with visible pores, individual hair strands, subtle wrinkles, realistic shadows and reflections, iPhone-footage look, phone camera look not professional photography, no AI polish, no beauty smoothing, no blur anywhere, everything in sharp focus including the parking lot and the storefronts.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no studio, no plastic skin, no extra fingers, no supernatural lighting, no blur, no artificial lighting, no warm orange color cast, no yellow tint, no jewelry, no watch, no cross, no second person, no brand label"
}
```

## K06 · T2 (compartilhado) · RECEITA/PROTOCOLO · GERAR DO ZERO · FINGERPRINT JAMIE ANDERSON

> ### 📎 ANEXAR: **1 IMAGEM**
> **1️⃣ FINGERPRINT JAMIE ANDERSON** (character consistency sheet anexado na mensagem original)
>
> ### 🆕 GERAR DO ZERO

```json
{
  "shot_id": "K06_pour_pan",
  "reference_use": "Use the attached fingerprint reference ONLY for Jamie Anderson's face, identity, body and skin. Do NOT copy its pose, framing or background.",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "identity_main": "The EXACT man from the attached fingerprint reference (Jamie Anderson): Black American man in his mid fifties, medium brown skin, short low-cut hair heavily greyed at the temples and crown with a natural hairline, a short full beard almost entirely white with a greying moustache, a symmetric face with a high forehead, visible moles and freckles on his cheekbones, dark brown eyes, grey eyebrows, lean athletic build with wide shoulders, real skin texture with visible pores, forehead lines and crow's feet, no makeup.",
  "wardrobe": "A white linen button-up shirt, collar open, no tie, sleeves rolled to the forearm, dark trousers. No jewelry of any kind, no watch.",
  "prop": "He tilts a clear glass mixing bowl of smooth, pale cream batter, pouring it into a round metal springform pan with a lightly greased bottom, resting on the tailgate's cargo floor.",
  "scene": "Standing behind the raised tailgate of his own parked SUV in an ordinary American parking lot. Through the open tailgate and rear window, an ordinary American parking lot is visible with a blue sedan and a grey SUV parked nearby and a row of brick storefronts with awnings in the distance. A small American flag decal sits on the corner of the rear window glass, discreet but clearly visible and in sharp focus.",
  "posture": "Leaning forward slightly over the tailgate, tilting the bowl over the pan with both hands.",
  "composition": "The pan and the pouring stream of batter fill the lower two thirds of the frame, closer to the lens than his face. His head and shoulders occupy the upper third.",
  "camera": "chest level, straight-on, camera pushed in close toward the pan",
  "state": "Start frame: the batter is mid-pour, a thick smooth stream falling from the bowl into the pan, which is already partly filled.",
  "lighting": "Flat neutral daylight under an overcast sky, evenly lighting his face, no warm orange cast and no yellow tint.",
  "realism": "UGC realism, real skin texture with visible pores, individual hair strands, subtle wrinkles, realistic shadows and reflections, iPhone-footage look, phone camera look not professional photography, no AI polish, no beauty smoothing, no blur anywhere, everything in sharp focus including the parking lot and the storefronts.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no studio, no plastic skin, no extra fingers, no supernatural lighting, no blur, no artificial lighting, no warm orange color cast, no yellow tint, no jewelry, no watch, no cross, no second person, no brand label"
}
```

## K07 · T3 a T7 (compartilhado) · RESULTADO/BENEFÍCIOS/MECANISMO/AUTORIDADE · GERAR DO ZERO · FINGERPRINT JAMIE ANDERSON

> ### 📎 ANEXAR: **1 IMAGEM**
> **1️⃣ FINGERPRINT JAMIE ANDERSON** (character consistency sheet anexado na mensagem original)
>
> ### 🆕 GERAR DO ZERO

```json
{
  "shot_id": "K07_baked_cheesecake",
  "reference_use": "Use the attached fingerprint reference ONLY for Jamie Anderson's face, identity, body and skin. Do NOT copy its pose, framing or background.",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "identity_main": "The EXACT man from the attached fingerprint reference (Jamie Anderson): Black American man in his mid fifties, medium brown skin, short low-cut hair heavily greyed at the temples and crown with a natural hairline, a short full beard almost entirely white with a greying moustache, a symmetric face with a high forehead, visible moles and freckles on his cheekbones, dark brown eyes, grey eyebrows, lean athletic build with wide shoulders, real skin texture with visible pores, forehead lines and crow's feet, no makeup.",
  "wardrobe": "A white linen button-up shirt, collar open, no tie, sleeves rolled to the forearm, dark trousers. No jewelry of any kind, no watch. His hands are covered by a pair of plain quilted oven mitts.",
  "prop": "He holds the same round metal springform pan close to the camera with both mitted hands, now containing a fully baked cheesecake with a golden brown top, its edges lightly caramelized.",
  "scene": "Standing behind the raised tailgate of his own parked SUV in an ordinary American parking lot. Through the open tailgate and rear window, an ordinary American parking lot is visible with a blue sedan and a grey SUV parked nearby and a row of brick storefronts with awnings in the distance. A small American flag decal sits on the corner of the rear window glass, discreet but clearly visible and in sharp focus.",
  "posture": "Leaning forward over the tailgate, holding the pan up toward the camera with both hands, confident and direct expression.",
  "composition": "The pan with the baked cheesecake fills the lower half of the frame, closer to the lens than his face. His head and shoulders occupy the upper half.",
  "camera": "chest level, straight-on, camera pushed in close toward the pan",
  "state": "Start frame: the baked cheesecake is held steady toward the camera. Nothing moves or changes.",
  "lighting": "Flat neutral daylight under an overcast sky, evenly lighting his face, no warm orange cast and no yellow tint.",
  "realism": "UGC realism, real skin texture with visible pores, individual hair strands, subtle wrinkles, realistic shadows and reflections, iPhone-footage look, phone camera look not professional photography, no AI polish, no beauty smoothing, no blur anywhere, everything in sharp focus including the parking lot and the storefronts.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no studio, no plastic skin, no extra fingers, no supernatural lighting, no blur, no artificial lighting, no warm orange color cast, no yellow tint, no jewelry, no watch, no cross, no second person, no brand label"
}
```

## K08 · T8 (compartilhado) · CTA + FOLLOW GATE · GERAR DO ZERO · FINGERPRINT JAMIE ANDERSON

> ### 📎 ANEXAR: **1 IMAGEM**
> **1️⃣ FINGERPRINT JAMIE ANDERSON** (character consistency sheet anexado na mensagem original)
>
> ### 🆕 GERAR DO ZERO

```json
{
  "shot_id": "K08_cta_slice",
  "reference_use": "Use the attached fingerprint reference ONLY for Jamie Anderson's face, identity, body and skin. Do NOT copy its pose, framing or background.",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "identity_main": "The EXACT man from the attached fingerprint reference (Jamie Anderson): Black American man in his mid fifties, medium brown skin, short low-cut hair heavily greyed at the temples and crown with a natural hairline, a short full beard almost entirely white with a greying moustache, a symmetric face with a high forehead, visible moles and freckles on his cheekbones, dark brown eyes, grey eyebrows, lean athletic build with wide shoulders, real skin texture with visible pores, forehead lines and crow's feet, no makeup.",
  "wardrobe": "A white linen button-up shirt, collar open, no tie, sleeves rolled to the forearm, dark trousers. No jewelry of any kind, no watch.",
  "prop": "He holds a plain white plate in one hand, with a single cut slice of the baked cheesecake on it, creamy pale interior visible from the cut edge. His other hand points directly toward the camera, index finger extended.",
  "scene": "Standing behind the raised tailgate of his own parked SUV in an ordinary American parking lot. Through the open tailgate and rear window, an ordinary American parking lot is visible with a blue sedan and a grey SUV parked nearby and a row of brick storefronts with awnings in the distance. A small American flag decal sits on the corner of the rear window glass, discreet but clearly visible and in sharp focus.",
  "posture": "Leaning forward over the tailgate, holding the plate toward the camera with one hand, the other hand raised in an urgent pointing gesture.",
  "composition": "The plate with the slice occupies the lower third of the frame, his pointing hand and upper body fill the rest, closer to the lens than a normal talking shot.",
  "camera": "chest level, straight-on, camera pushed in close",
  "state": "Start frame: the hand is mid gesture, finger extended toward the camera, the plate held steady.",
  "lighting": "Flat neutral daylight under an overcast sky, evenly lighting his face, no warm orange cast and no yellow tint.",
  "realism": "UGC realism, real skin texture with visible pores, individual hair strands, subtle wrinkles, realistic shadows and reflections, iPhone-footage look, phone camera look not professional photography, no AI polish, no beauty smoothing, no blur anywhere, everything in sharp focus including the parking lot and the storefronts.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no studio, no plastic skin, no extra fingers, no supernatural lighting, no blur, no artificial lighting, no warm orange color cast, no yellow tint, no jewelry, no watch, no cross, no second person, no brand label"
}
```

---

## Bloco global de vídeo

```text
o avatar (homem) fala em inglês com sotaque americano de Jamie Anderson, voz confiante, de alto padrão porém acessível, direta e animada, como quem parou o carro no estacionamento porque precisava falar aquilo agora, a seguinte frase: "[FALA EXATA DO ROTEIRO]"

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: [ação ENXUTA, só o que acontece]

câmera: [fixa / leve push-in]

som ambiente: estacionamento americano comum, tráfego distante abafado, sem música
```

---

# Prompts de vídeo

### V01 · T1 (gancho ricota) · usa K01

```text
o avatar (homem) fala em inglês com sotaque americano de Jamie Anderson, voz confiante, de alto padrão porém acessível, direta e animada, como quem parou o carro no estacionamento porque precisava falar aquilo agora, a seguinte frase: "How old were you when you found out that if you crack an egg into ricotta cheese and whisk it until the batter is completely smooth,"

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ele quebra o ovo e a gema cai dentro da tigela de ricota, a clara já escorrendo por cima.

câmera: fixa

som ambiente: estacionamento americano comum, tráfego distante abafado, sem música
```

### V02 · T1 (gancho tofu sedoso) · usa K02

```text
o avatar (homem) fala em inglês com sotaque americano de Jamie Anderson, voz confiante, de alto padrão porém acessível, direta e animada, como quem parou o carro no estacionamento porque precisava falar aquilo agora, a seguinte frase: "How old were you when you found out that if you crack an egg into silken tofu and whisk it until the batter is completely smooth,"

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ele quebra o ovo e a gema cai dentro da tigela de tofu sedoso, a clara já escorrendo por cima.

câmera: fixa

som ambiente: estacionamento americano comum, tráfego distante abafado, sem música
```

### V03 · T1 (gancho mascarpone) · usa K03

```text
o avatar (homem) fala em inglês com sotaque americano de Jamie Anderson, voz confiante, de alto padrão porém acessível, direta e animada, como quem parou o carro no estacionamento porque precisava falar aquilo agora, a seguinte frase: "How old were you when you found out that if you crack an egg into mascarpone and whisk it until the batter is completely smooth,"

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ele quebra o ovo e a gema cai dentro da tigela de mascarpone, a clara já escorrendo por cima.

câmera: fixa

som ambiente: estacionamento americano comum, tráfego distante abafado, sem música
```

### V04 · T1 (gancho whey) · usa K04

```text
o avatar (homem) fala em inglês com sotaque americano de Jamie Anderson, voz confiante, de alto padrão porém acessível, direta e animada, como quem parou o carro no estacionamento porque precisava falar aquilo agora, a seguinte frase: "How old were you when you found out that if you stir a scoop of protein powder into Greek yogurt and whisk it until the batter is completely smooth,"

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ele inclina a colher medidora e o pó de proteína cai dentro da tigela de iogurte grego.

câmera: fixa

som ambiente: estacionamento americano comum, tráfego distante abafado, sem música
```

### V05 · T1 (gancho cottage cheese) · usa K05

```text
o avatar (homem) fala em inglês com sotaque americano de Jamie Anderson, voz confiante, de alto padrão porém acessível, direta e animada, como quem parou o carro no estacionamento porque precisava falar aquilo agora, a seguinte frase: "How old were you when you found out that if you crack an egg into cottage cheese and whisk it until the batter is completely smooth,"

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ele quebra o ovo e a gema cai dentro da tigela de cottage cheese, a clara já escorrendo por cima.

câmera: fixa

som ambiente: estacionamento americano comum, tráfego distante abafado, sem música
```

### V06 · T2 · usa K06

```text
o avatar (homem) fala em inglês com sotaque americano de Jamie Anderson, voz confiante, de alto padrão porém acessível, direta e animada, como quem parou o carro no estacionamento porque precisava falar aquilo agora, a seguinte frase: "stirring in a little raw honey and vanilla, pour it into a greased pan, bake it at 350 for 20 minutes and let it chill."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ele despeja a massa lisa da tigela dentro da forma untada, enchendo até a borda.

câmera: fixa

som ambiente: estacionamento americano comum, tráfego distante abafado, sem música
```

### V07 · T3 · usa K07

```text
o avatar (homem) fala em inglês com sotaque americano de Jamie Anderson, voz confiante, de alto padrão porém acessível, direta e animada, como quem parou o carro no estacionamento porque precisava falar aquilo agora, a seguinte frase: "You end up with a creamy cheesecake that not only tastes like the real deal, but is easy on the stomach,"

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ele mantém a forma com o cheesecake assado erguida perto da câmera, parado, olhando direto pro espectador.

câmera: fixa

som ambiente: estacionamento americano comum, tráfego distante abafado, sem música
```

### V08 · T4 · usa K07

```text
o avatar (homem) fala em inglês com sotaque americano de Jamie Anderson, voz confiante, de alto padrão porém acessível, direta e animada, como quem parou o carro no estacionamento porque precisava falar aquilo agora, a seguinte frase: "feeds the good bacteria in your gut and will not send your blood sugar through the roof."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ele continua segurando a forma erguida, aceno leve de cabeça confirmando o que fala.

câmera: fixa

som ambiente: estacionamento americano comum, tráfego distante abafado, sem música
```

### V09 · T5 · usa K07

```text
o avatar (homem) fala em inglês com sotaque americano de Jamie Anderson, voz confiante, de alto padrão porém acessível, direta e animada, como quem parou o carro no estacionamento porque precisava falar aquilo agora, a seguinte frase: "And the best part, the eggs in the yogurt carry tryptophan, the sleep amino acid."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ele continua segurando a forma erguida, expressão de quem revela um detalhe importante.

câmera: fixa

som ambiente: estacionamento americano comum, tráfego distante abafado, sem música
```

### V10 · T6 · usa K07

```text
o avatar (homem) fala em inglês com sotaque americano de Jamie Anderson, voz confiante, de alto padrão porém acessível, direta e animada, como quem parou o carro no estacionamento porque precisava falar aquilo agora, a seguinte frase: "Combined with raw honey, it winds your body down for deep sleep naturally, making it the perfect bedtime snack."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ele continua segurando a forma erguida, tom calmo e satisfeito.

câmera: fixa

som ambiente: estacionamento americano comum, tráfego distante abafado, sem música
```

### V11 · T7 · usa K07

```text
o avatar (homem) fala em inglês com sotaque americano de Jamie Anderson, voz confiante, de alto padrão porém acessível, direta e animada, como quem parou o carro no estacionamento porque precisava falar aquilo agora, a seguinte frase: "I have recipes like this for every sweet treat you can think of. No refined sugar, low carbs, high protein, and they taste amazing."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ele continua segurando a forma erguida, sorriso confiante enquanto lista os benefícios.

câmera: fixa

som ambiente: estacionamento americano comum, tráfego distante abafado, sem música
```

### V12 · T8 · usa K08

```text
o avatar (homem) fala em inglês com sotaque americano de Jamie Anderson, voz confiante, de alto padrão porém acessível, direta e animada, como quem parou o carro no estacionamento porque precisava falar aquilo agora, a seguinte frase: "Comment cheesecake if you want more like this and follow me so you do not miss a single one."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ele aponta o dedo direto pra câmera, segurando o prato com a fatia na outra mão.

câmera: fixa

som ambiente: estacionamento americano comum, tráfego distante abafado, sem música
```

---

## Mapa de âncoras

| Keyframe | Referências a anexar | Modelo |
|---|---|---|
| K01 a K08 | FINGERPRINT JAMIE ANDERSON | Nano Banana 2, 9:16 |

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
5. [ ] O adesivo da bandeira dos EUA aparece e está em foco nos oito keyframes.
6. [ ] Zero joia, zero relógio, zero cruz em todos os keyframes.
7. [ ] O cabelo grisalho curto, a barba quase toda branca e as pintas/sardas saem idênticos nos
   oito keyframes.
8. [ ] Zero blur em qualquer imagem, inclusive no estacionamento e nas lojas ao fundo.
9. [ ] Luz neutra de dia nublado. Nenhuma imagem com cast quente.
10. [ ] A fala de cada V bate palavra por palavra com o take do `ROTEIRO.md` (ou com a variação de
    gancho aprovada, no caso dos T1).
11. [ ] Nenhum take promete além do que o vídeo original promete (sem claim de tratamento/cura).
12. [ ] `python checar_entrega.py producao/fitywell_cheesecake` fechou sem FALHA.
