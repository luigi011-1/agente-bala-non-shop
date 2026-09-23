# Dana Morrison | FityWell Growth | Pacote de Prompts

Vídeo modelo: `input/reference_video.mp4`, 29,304 s

Âncora de identidade: `input/anchors/dana_morrison_sheet.png`

Referência da cliente: `REF-A`, gerada com `REF_CLIENTE_40PLUS.md`

Objetivo: crescimento orgânico. Sem produto, aplicativo, quiz, DM ou keyword.

Avatar 1 de 10 da fila. Hooks escolhidos: H1, H4, H10, H9 e H6.

## Índice de geração

| Take | Hook | Keyframe | Anexar | Ação de geração |
|---|---|---|---|---|
| T1 | H1 | K01 | ÂNCORA DANA + REF-A | GERAR DO ZERO. Moeda fina no centro da língua |
| T6 | H4 | K02 | ÂNCORA DANA + REF-A | GERAR DO ZERO. Gengibre ralado na colher |
| T7 | H10 | K03 | ÂNCORA DANA + REF-A | GERAR DO ZERO. Fatia antes do contato |
| T8 | H9 | K04 | ÂNCORA DANA + REF-A | GERAR DO ZERO. Fatia entre os dentes |
| T9 | H6 | K05 | ÂNCORA DANA + REF-A | GERAR DO ZERO. Borda tocando a ponta da língua |
| T2 | corpo | K06 | ÂNCORA DANA + REF-A | GERAR DO ZERO. Pausa física, mesmo setup do hook |
| T3 | corpo | K07 | ÂNCORA DANA + REF-A | GERAR DO ZERO. Coach cortando gengibre |
| T4 e T5 | corpo | K08 | ÂNCORA DANA + REF-A | GERAR DO ZERO. Coach mostra três fatias à lente |

Todos os keyframes são gerados do zero com as duas referências. A REF-A trava a mesma cliente nos oito keyframes. K08 sustenta dois clipes porque T4 e T5 mantêm setup, prop e enquadramento idênticos.

## Trava de identidade e continuidade

- Dana Morrison é um homem negro americano no início dos cinquenta, pele marrom escura, rosto magro e anguloso, olhos castanho-escuros e expressão direta.
- Do-rag preto de cetim, com a aba caindo atrás do ombro esquerdo.
- Barba do queixo comprida e branca, cheia, com bigode escuro salpicado de grisalho. Nunca encurtar.
- Corpo seco e treinado, antebraços com veias marcadas, mãos grandes e calejadas.
- Regata canelada preta e corrente fina de ouro sem pingente. Sem cruz.
- Cenário próprio: garagem com bancada de madeira gasta, pegboard marrom, ferramentas e prateleira de ervas com pequena bandeira dos EUA.
- Luz neutra de dia entrando pela garagem aberta. Zero cast quente e zero blur.
- A cliente é sempre a mulher fictícia da REF-A, cerca de cinquenta anos, cabelo loiro preso e regata azul-marinho.

## Trava do prop herói

```text
Fresh raw ginger with pale golden-yellow flesh, fibrous natural texture and a thin light-brown skin edge.
Every slice is visibly food, moist but not glossy, very thin and small enough to rest safely on the tongue.
The ginger and the exact point of contact with the mouth are always the largest and closest elements
to the lens in the hook. No other food or object competes with them.
```

## Trava da segunda pessoa, REF-A

Gerar e aprovar `REF-A` uma vez com `REF_CLIENTE_40PLUS.md`. Anexar a REF-A junto com a âncora Dana em K01 a K08. Usar a REF-A apenas para identidade, idade, cabelo, roupa e proporções da cliente. O cenário vem da âncora do coach.

# Prompts de imagem

## K01 · T1 · H1 · GERAR DO ZERO · ÂNCORA DANA MORRISON + REF-A

> ### 📎 ANEXAR: **2 IMAGENS**
> **1️⃣ ÂNCORA DANA MORRISON** `input/anchors/dana_morrison_sheet.png`
> **2️⃣ REF-A** cliente FitWell 40+ já aprovada
>
> ### 🆕 GERAR DO ZERO

```json
{
  "shot_id": "K01_H1_ginger_coin_on_tongue",
  "reference_use": "Use the first attached image only for Dana Morrison's exact face, black satin do-rag, long white chin beard, black ribbed tank top, gold chain and garage identity. Use the second attached image only for the exact female client's face, blonde ponytail, age and navy sleeveless top. Do not copy either reference pose or framing.",
  "fiction_note": "These are fictional AI-generated characters, no real person is depicted.",
  "identity_main": "The exact man from the first reference, Dana Morrison: Black American man in his early fifties, deep brown skin, lean angular face, dark brown eyes, black satin do-rag tied with its tail behind his left shoulder, long full white chin beard and darker moustache flecked with grey, real pores and deep forehead lines.",
  "second_person": "The exact woman from REF-A, around fifty, fair neutral skin with natural fine lines, blonde hair in a loose low ponytail, navy sleeveless cotton top. She is in the near foreground with her mouth open and tongue naturally extended. One single paper-thin coin of fresh raw ginger rests flat in the center of her tongue.",
  "wardrobe": "Dana wears a plain black ribbed tank top and a thin gold chain with no pendant. The client wears her plain navy sleeveless top and no jewelry.",
  "scene": "Dana's same garage workshop: a scuffed wooden workbench edge below, a brown pegboard with a few hand tools and one wooden herb shelf with a small American flag behind them.",
  "posture": "The client is closest to the phone, cropped at the shoulders. Dana stands immediately behind and to her right, leaning close enough for his face and lips to remain clear, pointing one large index finger at the ginger without touching her.",
  "composition": "Extreme intimate two-person close-up. The client's open mouth, tongue, ginger coin and Dana's pointing fingertip fill the lower and central foreground, much closer to the lens than either full face. Dana's head and shoulders remain visible in the upper right for lip sync. The client is partially cut by the left edge. Nothing else competes.",
  "camera": "phone camera at mouth level, straight-on, pushed extremely close to the ginger and tongue",
  "state": "Start frame: the ginger coin is already resting motionless on the center of her tongue. Dana's fingertip is two centimeters away and he is beginning to speak. The client does not speak.",
  "lighting": "Flat neutral daylight from the open garage door, even skin tones, no warm orange cast and no yellow tint.",
  "realism": "UGC realism, real skin texture with visible pores, individual hair strands and beard hairs, natural mouth texture, realistic shadows and reflections, iPhone-footage look, phone camera not professional photography, no AI polish, no beauty smoothing, no blur anywhere, everything in sharp focus.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no studio, no plastic skin, no extra fingers, no supernatural lighting, no blur, no artificial lighting, no warm color cast, no food other than ginger, no spoon, no knife, no plate, no second ginger slice, no cross"
}
```

## K02 · T6 · H4 · GERAR DO ZERO · ÂNCORA DANA MORRISON + REF-A

> ### 📎 ANEXAR: **2 IMAGENS**
> **1️⃣ ÂNCORA DANA MORRISON** `input/anchors/dana_morrison_sheet.png`
> **2️⃣ REF-A** cliente FitWell 40+ já aprovada
>
> ### 🆕 GERAR DO ZERO

```json
{
  "shot_id": "K02_H4_grated_ginger_on_spoon",
  "reference_use": "Use the first attached image only for Dana Morrison's exact identity, wardrobe and garage. Use the second attached image only for the exact female client's identity and wardrobe. Do not copy either pose or framing.",
  "fiction_note": "These are fictional AI-generated characters, no real person is depicted.",
  "identity_main": "The exact man from the first reference, Dana Morrison: Black American man in his early fifties with deep brown skin, black satin do-rag, long full white chin beard, darker grey-flecked moustache, angular face and dark brown eyes.",
  "second_person": "The exact woman from REF-A, around fifty, blonde low ponytail, navy sleeveless top. She is in the near foreground with her mouth open and tongue slightly extended. A small plain metal teaspoon holds one tiny loose pinch of freshly grated raw ginger, and the ginger just touches the tip of her tongue.",
  "wardrobe": "Dana wears his black ribbed tank top and thin gold chain without a pendant. The client wears her navy sleeveless top and no jewelry.",
  "scene": "Dana's same garage workshop, with only a narrow edge of the scuffed workbench, the brown pegboard and the herb shelf with a small American flag readable behind them.",
  "posture": "The client holds the teaspoon steadily near her own mouth. Dana leans immediately behind and to her right, pointing directly at the grated ginger without touching the spoon.",
  "composition": "Extreme two-person close-up. The teaspoon bowl, grated ginger, tongue and Dana's fingertip dominate the center foreground. Dana's face remains visible in the upper right for lip sync. The client's face is partially cropped by the left and top edges. Nothing else competes.",
  "camera": "phone camera at mouth level, straight-on, extremely close to the spoon and point of contact",
  "state": "Start frame: the grated ginger is still on the teaspoon and only its outer strands touch the tongue. Dana is beginning to speak. The client remains silent.",
  "lighting": "Flat neutral daylight from the open garage door, no warm orange cast and no yellow tint.",
  "realism": "UGC realism, real pores, individual hair and beard strands, fibrous ginger texture, natural mouth detail, realistic shadows, iPhone-footage look, no AI polish, no beauty smoothing, no blur anywhere.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no studio, no plastic skin, no extra fingers, no supernatural lighting, no blur, no artificial lighting, no warm color cast, no plate, no knife, no whole ginger root, no cross"
}
```

## K03 · T7 · H10 · GERAR DO ZERO · ÂNCORA DANA MORRISON + REF-A

> ### 📎 ANEXAR: **2 IMAGENS**
> **1️⃣ ÂNCORA DANA MORRISON** `input/anchors/dana_morrison_sheet.png`
> **2️⃣ REF-A** cliente FitWell 40+ já aprovada
>
> ### 🆕 GERAR DO ZERO

```json
{
  "shot_id": "K03_H10_ginger_before_contact",
  "reference_use": "Use the first attached image only for Dana Morrison's exact identity, wardrobe and garage. Use the second attached image only for the exact female client's identity and wardrobe. Do not copy either pose or framing.",
  "fiction_note": "These are fictional AI-generated characters, no real person is depicted.",
  "identity_main": "The exact man from the first reference, Dana Morrison: Black American man in his early fifties, deep brown skin, black satin do-rag, long full white chin beard, grey-flecked moustache, angular face and dark brown eyes.",
  "second_person": "The exact woman from REF-A, around fifty, blonde low ponytail and navy sleeveless top. She is closest to camera with her mouth open and tongue naturally extended. She pinches one paper-thin ginger coin between thumb and index finger exactly one centimeter in front of the tip of her tongue.",
  "wardrobe": "Dana wears a black ribbed tank top and thin gold chain with no pendant. The client wears her navy sleeveless top and no jewelry.",
  "scene": "Dana's same garage workshop, with a small readable section of brown pegboard and the herb shelf with a small American flag behind them.",
  "posture": "The client's hand is steady at mouth height. Dana leans behind and to her right and points his index finger at the tiny visible gap between ginger and tongue.",
  "composition": "Extreme close-up. The ginger coin, the one-centimeter air gap, the tongue and the pointing fingertip dominate the frame. Dana's speaking face remains visible in the upper right. The client is cropped at the shoulders and along the left edge. Nothing else competes.",
  "camera": "phone camera at mouth level, straight-on, pushed extremely close to the gap before contact",
  "state": "Start frame: the ginger has not touched the tongue yet. The gap is clear and creates anticipation. Dana is starting the line; the client does not speak.",
  "lighting": "Flat neutral daylight from the garage opening, even and cool-neutral, no warm cast.",
  "realism": "UGC realism, visible skin pores, individual hair and beard strands, accurate fingers, fibrous ginger texture, iPhone-footage look, no AI polish, no beauty smoothing, no blur anywhere.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no studio, no plastic skin, no extra fingers, no supernatural lighting, no blur, no artificial lighting, no warm color cast, no contact between ginger and tongue in the start frame, no spoon, no knife, no plate, no cross"
}
```

## K04 · T8 · H9 · GERAR DO ZERO · ÂNCORA DANA MORRISON + REF-A

> ### 📎 ANEXAR: **2 IMAGENS**
> **1️⃣ ÂNCORA DANA MORRISON** `input/anchors/dana_morrison_sheet.png`
> **2️⃣ REF-A** cliente FitWell 40+ já aprovada
>
> ### 🆕 GERAR DO ZERO

```json
{
  "shot_id": "K04_H9_ginger_between_teeth",
  "reference_use": "Use the first attached image only for Dana Morrison's exact identity, wardrobe and garage. Use the second attached image only for the exact female client's identity and wardrobe. Do not copy either pose or framing.",
  "fiction_note": "These are fictional AI-generated characters, no real person is depicted.",
  "identity_main": "The exact man from the first reference, Dana Morrison: Black American man in his early fifties, deep brown skin, black satin do-rag, long full white chin beard, darker moustache flecked with grey, lean angular face and dark brown eyes.",
  "second_person": "The exact woman from REF-A, around fifty, blonde hair in a low ponytail and navy sleeveless top. Her lips are parted and one paper-thin ginger slice is held gently between her front teeth, with half of the slice clearly visible outside. She is not biting or chewing.",
  "wardrobe": "Dana wears his black ribbed tank top and thin gold chain without a pendant. The client wears her plain navy sleeveless top and no jewelry.",
  "scene": "Dana's same garage workshop, only the pegboard and the herb shelf with the small American flag readable behind them.",
  "posture": "The client is closest to camera, cropped at the shoulders. Dana leans immediately behind and to her right, pointing at the exposed half of the ginger slice without touching her.",
  "composition": "Extreme intimate close-up. The ginger between the front teeth and Dana's fingertip dominate the center foreground. Dana's face and moving lips remain clear in the upper right. The client's face is partially cut by the left edge. Nothing else competes.",
  "camera": "phone camera at mouth level, straight-on, extremely close",
  "state": "Start frame: the slice is held motionless between the front teeth, no bite. Dana begins speaking while the client remains silent.",
  "lighting": "Flat neutral daylight from the open garage door, even and natural, no warm cast.",
  "realism": "UGC realism, natural teeth and lips, real pores, individual hair and beard strands, fibrous ginger texture, iPhone-footage look, no AI polish, no beauty smoothing, no blur anywhere.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no studio, no plastic skin, no extra fingers, no supernatural lighting, no blur, no artificial lighting, no warm color cast, no chewing, no broken ginger, no spoon, no knife, no plate, no cross"
}
```

## K05 · T9 · H6 · GERAR DO ZERO · ÂNCORA DANA MORRISON + REF-A

> ### 📎 ANEXAR: **2 IMAGENS**
> **1️⃣ ÂNCORA DANA MORRISON** `input/anchors/dana_morrison_sheet.png`
> **2️⃣ REF-A** cliente FitWell 40+ já aprovada
>
> ### 🆕 GERAR DO ZERO

```json
{
  "shot_id": "K05_H6_ginger_tip_of_tongue",
  "reference_use": "Use the first attached image only for Dana Morrison's exact identity, wardrobe and garage. Use the second attached image only for the exact female client's identity and wardrobe. Do not copy either pose or framing.",
  "fiction_note": "These are fictional AI-generated characters, no real person is depicted.",
  "identity_main": "The exact man from the first reference, Dana Morrison: Black American man in his early fifties, deep brown skin, black satin do-rag, long full white chin beard, grey-flecked moustache, lean angular face and dark brown eyes.",
  "second_person": "The exact woman from REF-A, around fifty, blonde low ponytail and navy sleeveless top. Her mouth is open and tongue slightly extended. She pinches one paper-thin ginger coin between thumb and index finger, touching only one edge of it to the very tip of her tongue.",
  "wardrobe": "Dana wears his black ribbed tank top and thin gold chain without a pendant. The client wears her navy sleeveless top and no jewelry.",
  "scene": "Dana's same garage workshop with a narrow readable area of brown pegboard and the herb shelf with a small American flag behind them.",
  "posture": "The client's hand stays steady at mouth height. Dana leans behind and to her right and points at the exact point where ginger meets the tip of the tongue.",
  "composition": "Extreme close-up. The point of contact, ginger edge, tongue tip and pointing fingertip fill the central foreground. Dana's speaking face remains visible in the upper right. The client is cropped at shoulders and left edge. Nothing else competes.",
  "camera": "phone camera at mouth level, straight-on, pushed extremely close to the point of contact",
  "state": "Start frame: only the edge of the slice touches the tongue. Dana is beginning to speak. The client remains silent and still.",
  "lighting": "Flat neutral daylight from the open garage door, no warm orange cast or yellow tint.",
  "realism": "UGC realism, real pores, individual hair and beard strands, accurate hand anatomy, natural mouth texture, fibrous ginger, iPhone-footage look, no AI polish, no beauty smoothing, no blur anywhere.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no studio, no plastic skin, no extra fingers, no supernatural lighting, no blur, no artificial lighting, no warm color cast, no full slice lying on the tongue, no spoon, no knife, no plate, no cross"
}
```

## K06 · T2 · MECANISMO · GERAR DO ZERO · ÂNCORA DANA MORRISON + REF-A

> ### 📎 ANEXAR: **2 IMAGENS**
> **1️⃣ ÂNCORA DANA MORRISON** `input/anchors/dana_morrison_sheet.png`
> **2️⃣ REF-A** cliente FitWell 40+ já aprovada
>
> ### 🆕 GERAR DO ZERO

```json
{
  "shot_id": "K06_body_physical_pause",
  "reference_use": "Use the first attached image only for Dana Morrison's exact identity, wardrobe and garage. Use the second attached image only for the exact female client's identity and wardrobe. Do not copy either pose or framing.",
  "fiction_note": "These are fictional AI-generated characters, no real person is depicted.",
  "identity_main": "The exact man from the first reference, Dana Morrison: Black American man in his early fifties, deep brown skin, black satin do-rag, long full white chin beard, grey-flecked moustache, lean angular face and dark brown eyes.",
  "second_person": "The exact woman from REF-A, around fifty, blonde low ponytail and navy sleeveless top. She is closest to camera with her mouth open, one paper-thin ginger coin resting flat in the center of her tongue.",
  "wardrobe": "Dana wears a black ribbed tank top and a thin gold chain with no pendant. The client wears her navy sleeveless top and no jewelry.",
  "scene": "Dana's same garage workshop: scuffed workbench edge, brown pegboard and herb shelf with a small American flag behind them.",
  "posture": "Dana stands close behind and to the client's right. His pointing hand has lowered slightly, and he looks from the ginger back to the phone lens while speaking. The client remains silent.",
  "composition": "Very tight two-person close-up, only slightly wider than the hook. Mouth, ginger and Dana's lowered pointing hand remain in the foreground. Dana's full speaking face is clearer in the upper right. The client stays cropped by the left edge.",
  "camera": "phone camera at mouth level, straight-on, close and intimate",
  "state": "Start frame: the ginger remains still on the center of the tongue. Dana is looking into the lens at the start of his explanation.",
  "lighting": "Flat neutral garage daylight, no warm color cast.",
  "realism": "UGC realism, real pores, individual hair and beard strands, natural mouth detail, iPhone-footage look, no AI polish, no beauty smoothing, no blur anywhere.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no studio, no plastic skin, no extra fingers, no supernatural lighting, no blur, no artificial lighting, no warm color cast, no spoon, no knife, no plate, no second ginger slice, no cross"
}
```

## K07 · T3 · AUTODIAGNÓSTICO · GERAR DO ZERO · ÂNCORA DANA MORRISON + REF-A

> ### 📎 ANEXAR: **2 IMAGENS**
> **1️⃣ ÂNCORA DANA MORRISON** `input/anchors/dana_morrison_sheet.png`
> **2️⃣ REF-A** cliente FitWell 40+ já aprovada
>
> ### 🆕 GERAR DO ZERO

```json
{
  "shot_id": "K07_cutting_raw_ginger",
  "reference_use": "Use the first attached image only for Dana Morrison's exact identity, wardrobe and garage. Use the second attached image only for the exact female client's identity and wardrobe. Do not copy either pose or framing.",
  "fiction_note": "These are fictional AI-generated characters, no real person is depicted.",
  "identity_main": "The exact man from the first reference, Dana Morrison: Black American man in his early fifties, deep brown skin, black satin do-rag, long full white chin beard, grey-flecked moustache, lean trained build, veined forearms and large calloused hands.",
  "second_person": "The exact woman from REF-A, around fifty, blonde low ponytail, navy sleeveless top, standing immediately beside him and watching the preparation with a thoughtful expression.",
  "wardrobe": "Dana wears his black ribbed tank top and thin gold chain without a pendant. The client wears her navy sleeveless top and no jewelry.",
  "scene": "Dana's same garage workshop. A clean rectangular wooden cutting board sits on the scuffed workbench. Only the brown pegboard, one herb shelf and the small American flag remain readable behind them.",
  "prop": "A fresh raw ginger root and six very thin ginger coins lie on the cutting board. Dana holds a plain chef's knife with its blade resting safely against the ginger root, ready for the next thin slice.",
  "posture": "Dana leans toward the board while keeping his face turned enough toward the phone to speak. The client stands close at his right shoulder, partially cut by the frame.",
  "composition": "Tight chest-up two-shot. The cutting board, ginger root, thin slices and Dana's hands fill the lower foreground closer to the lens than either face. Dana dominates center-left; the client is cropped at the right edge. Nothing else on the bench.",
  "camera": "phone camera at upper-chest level, slightly high toward the cutting board, pushed close",
  "state": "Start frame: the knife rests against the ginger before the cutting motion. The six finished slices are arranged loosely in front.",
  "lighting": "Flat neutral daylight from the open garage door, no warm cast.",
  "realism": "UGC realism, real skin and hand texture, individual beard hairs, natural ginger fibers and knife reflections, iPhone-footage look, no AI polish, no beauty smoothing, no blur anywhere, background still sharp.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no studio, no plastic skin, no extra fingers, no supernatural lighting, no blur, no artificial lighting, no warm color cast, no food other than ginger, no plate, no cross"
}
```

## K08 · T4 E T5 · CONTRASTE, SHARE E FOLLOW · GERAR DO ZERO · ÂNCORA DANA MORRISON + REF-A

> ### 📎 ANEXAR: **2 IMAGENS**
> **1️⃣ ÂNCORA DANA MORRISON** `input/anchors/dana_morrison_sheet.png`
> **2️⃣ REF-A** cliente FitWell 40+ já aprovada
>
> ### 🆕 GERAR DO ZERO

```json
{
  "shot_id": "K08_three_ginger_slices_to_lens",
  "reference_use": "Use the first attached image only for Dana Morrison's exact identity, wardrobe and garage. Use the second attached image only for the exact female client's identity and wardrobe. Do not copy either pose or framing.",
  "fiction_note": "These are fictional AI-generated characters, no real person is depicted.",
  "identity_main": "The exact man from the first reference, Dana Morrison: Black American man in his early fifties, deep brown skin, black satin do-rag, long full white chin beard, grey-flecked moustache, lean angular face and direct dark brown eyes.",
  "second_person": "The exact woman from REF-A, around fifty, blonde low ponytail and navy sleeveless top, standing beside and slightly behind him with a calm attentive expression, partially cropped by the right edge.",
  "wardrobe": "Dana wears his black ribbed tank top and thin gold chain without a pendant. The client wears her navy sleeveless top and no jewelry.",
  "scene": "Dana's same garage workshop, with a small portion of the brown pegboard and the herb shelf with the small American flag readable behind them. The workbench is mostly below frame.",
  "prop": "Dana pinches three very thin fresh ginger coins in a small fan between thumb and index finger, holding them extremely close to the phone lens. The pale yellow cut surfaces and fibrous texture are clearly visible.",
  "posture": "Dana leans close behind the ginger fan and looks directly into the lens while speaking. The client stands close to his right shoulder and remains silent.",
  "composition": "Tight shoulders-up framing. The three ginger coins fill the lower central foreground and are closer than Dana's face. Dana's face dominates the upper half for lip sync. The client is partially cut by the right edge. Nothing else competes.",
  "camera": "eye level, straight-on, very close phone-camera distance",
  "state": "Start frame: the three slices are held steady near the lens. Dana is beginning to speak directly to the viewer.",
  "lighting": "Flat neutral daylight from the garage opening, no warm orange cast or yellow tint.",
  "realism": "UGC realism, real pores, individual beard hairs, accurate fingers, fibrous ginger texture, realistic shadows, iPhone-footage look, no AI polish, no beauty smoothing, no blur anywhere.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no studio, no plastic skin, no extra fingers, no supernatural lighting, no blur, no artificial lighting, no warm color cast, no product, no phone visible, no knife, no plate, no cross"
}
```

## Bloco global de vídeo

```text
o avatar Dana Morrison, homem, fala em inglês com sotaque americano de um homem negro, voz autêntica, direta, dinâmica e urgente, como se exigisse ser ouvido, a seguinte frase: "[FALA EXATA DO ROTEIRO]"

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: [ação enxuta e fiel ao frame]. A cliente permanece silenciosa e nunca move os lábios como se estivesse falando.

câmera: [fixa ou leve push-in]

som ambiente: garagem tranquila com um leve ruído de rua ao longe, sem música
```

# Prompts de vídeo

### V01 · T1 · usa K01

```text
o avatar Dana Morrison, homem, fala em inglês com sotaque americano de um homem negro, voz autêntica, direta, dinâmica e urgente, como se exigisse ser ouvido, a seguinte frase: "Put a thin slice of raw ginger on your tongue for ten seconds when an afternoon craving hits. Watch what happens before you reach for food."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Dana aponta para a fatia sobre a língua e fala para a câmera. A cliente mantém a boca aberta, fica imóvel e silenciosa.

câmera: fixa

som ambiente: garagem tranquila com um leve ruído de rua ao longe, sem música
```

### V02 · T6 · usa K02

```text
o avatar Dana Morrison, homem, fala em inglês com sotaque americano de um homem negro, voz autêntica, direta, dinâmica e urgente, como se exigisse ser ouvido, a seguinte frase: "Touch a tiny pinch of fresh grated ginger to your tongue for ten seconds when an afternoon craving hits. Notice what happens before the snack."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Dana aponta para o gengibre ralado enquanto a cliente encosta a colher na ponta da língua. Ela permanece imóvel e silenciosa.

câmera: fixa

som ambiente: garagem tranquila com um leve ruído de rua ao longe, sem música
```

### V03 · T7 · usa K03

```text
o avatar Dana Morrison, homem, fala em inglês com sotaque americano de um homem negro, voz autêntica, direta, dinâmica e urgente, como se exigisse ser ouvido, a seguinte frase: "Before your next afternoon snack, hold one thin slice of raw ginger right at your tongue for ten seconds. Then watch what your hand does."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Dana aponta para o pequeno espaço. A cliente aproxima a fatia até tocar a ponta da língua e então mantém a mão parada. Ela não fala.

câmera: fixa, leve push-in no instante do contato

som ambiente: garagem tranquila com um leve ruído de rua ao longe, sem música
```

### V04 · T8 · usa K04

```text
o avatar Dana Morrison, homem, fala em inglês com sotaque americano de um homem negro, voz autêntica, direta, dinâmica e urgente, como se exigisse ser ouvido, a seguinte frase: "Hold one thin slice of raw ginger between your front teeth for ten seconds when an afternoon craving hits. Notice what happens before you snack."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Dana aponta para a parte visível da fatia enquanto fala. A cliente segura o gengibre entre os dentes sem morder, mastigar ou falar.

câmera: fixa

som ambiente: garagem tranquila com um leve ruído de rua ao longe, sem música
```

### V05 · T9 · usa K05

```text
o avatar Dana Morrison, homem, fala em inglês com sotaque americano de um homem negro, voz autêntica, direta, dinâmica e urgente, como se exigisse ser ouvido, a seguinte frase: "Touch one thin slice of raw ginger to the tip of your tongue for ten seconds when an afternoon craving hits. Watch what happens next."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Dana aponta para o ponto de contato enquanto a cliente mantém a borda da fatia encostada na ponta da língua. Ela fica silenciosa.

câmera: fixa

som ambiente: garagem tranquila com um leve ruído de rua ao longe, sem música
```

### V06 · T2 · usa K06

```text
o avatar Dana Morrison, homem, fala em inglês com sotaque americano de um homem negro, voz autêntica, direta, dinâmica e urgente, como se exigisse ser ouvido, a seguinte frase: "The ginger does not melt fat. Its sharp taste creates a physical pause between the craving and your next automatic bite."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Dana baixa levemente a mão, olha da fatia para a lente e explica. A cliente mantém a fatia sobre a língua e permanece silenciosa.

câmera: fixa

som ambiente: garagem tranquila com um leve ruído de rua ao longe, sem música
```

### V07 · T3 · usa K07

```text
o avatar Dana Morrison, homem, fala em inglês com sotaque americano de um homem negro, voz autêntica, direta, dinâmica e urgente, como se exigisse ser ouvido, a seguinte frase: "Use those ten seconds to ask: am I hungry, or am I tired, stressed, thirsty, or simply repeating my usual afternoon pattern?"

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Dana corta duas fatias finas de gengibre com movimentos controlados, alternando o olhar entre a tábua e a câmera. A cliente observa e não fala.

câmera: fixa

som ambiente: corte suave sobre a tábua e garagem tranquila, sem música
```

### V08 · T4 · usa K08

```text
o avatar Dana Morrison, homem, fala em inglês com sotaque americano de um homem negro, voz autêntica, direta, dinâmica e urgente, como se exigisse ser ouvido, a seguinte frase: "Most diets tell women over forty to fight cravings harder. I teach them to interrupt the loop first. Share this with a woman who blames her willpower."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Dana mantém as três fatias perto da lente, baixa a mão alguns centímetros e a levanta novamente ao pedir o compartilhamento. A cliente observa e faz um leve aceno afirmativo.

câmera: fixa, leve push-in

som ambiente: garagem tranquila com um leve ruído de rua ao longe, sem música
```

### V09 · T5 · usa K08

```text
o avatar Dana Morrison, homem, fala em inglês com sotaque americano de um homem negro, voz autêntica, direta, dinâmica e urgente, como se exigisse ser ouvido, a seguinte frase: "Follow me for more simple weight-loss habits made for women over forty, so you do not miss the next one."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Dana mantém as três fatias visíveis perto da lente e aponta brevemente para a câmera com a mão livre no pedido de follow. A cliente permanece silenciosa.

câmera: leve push-in

som ambiente: garagem tranquila com um leve ruído de rua ao longe, sem música
```

## Mapa de âncoras

| Keyframe | Referências a anexar | Modelo |
|---|---|---|
| K01 a K08 | ÂNCORA DANA MORRISON + REF-A | Nano Banana 2, 9:16 |

Vídeo: Veo 3.1 Lite, Lower Priority, 8 segundos, uma variação por V, imagem indicada como frame inicial.

## Montagem no CapCut

1. Cada vídeo usa uma abertura: V01, V02, V03, V04 ou V05.
2. Depois da abertura, usar sempre V06, V07, V08 e V09.
3. Cortar cada clipe imediatamente depois da última palavra completa.
4. Legenda queimada em todos os takes, com uma palavra importante destacada em amarelo.
5. Sem música. Preservar somente som ambiente e adicionar trilha depois apenas se necessário.
6. Exportar 9:16 em 1080 por 1920.

## Gates de qualidade

1. [ ] Dana mantém do-rag preto, barba branca longa, regata preta e corrente de ouro sem pingente em K01 a K08.
2. [ ] A mesma cliente REF-A aparece em todos os oito keyframes.
3. [ ] O gengibre e o ponto de contato dominam K01 a K06.
4. [ ] Dana permanece visível o suficiente para lip sync nos seis closes de boca.
5. [ ] A cliente nunca move os lábios como se estivesse falando.
6. [ ] K03 começa antes do contato e o contato acontece dentro de V03.
7. [ ] K04 mostra gengibre entre os dentes sem mordida.
8. [ ] K07 preserva a ação de cortar gengibre do modelo.
9. [ ] K08 mantém três fatias próximas da lente em T4 e T5.
10. [ ] A pequena bandeira dos EUA está presente e em foco sem competir.
11. [ ] Zero blur e luz neutra em todos os keyframes.
12. [ ] Nenhum produto, celular, quiz ou tela aparece.
13. [ ] Nenhum campo `negative` cita marca, gore ou órgão.
14. [ ] Cada fala dos V01 a V09 bate literalmente com `ROTEIRO.md`.
15. [ ] `python3 checar_entrega.py producao/fitywell_growth_wentao_healer` fecha sem falha.
