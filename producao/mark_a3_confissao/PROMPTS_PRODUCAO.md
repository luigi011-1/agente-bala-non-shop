# Mark Collins (A3) | Ângulo 3 (Auraly) | Pacote de Prompts

Vídeo modelo: `DcjIIyWq3Bt_.mp4`

Âncora de identidade e cenário: `producao/_ancoras/MARK COLLINS .jpeg` (atenção ao espaço antes da extensão)

Funil: vídeo -> comment `222` -> DM -> link do quiz Auraly

⚠️ **MARK COLLINS É MULHER.** O nome soa masculino, igual ao caso inverso da Melody Carter. Todo prompt marca `female` explicitamente, e o roteiro só-fala vai marcado como VOZ FEMININA.

---

## Índice de geração

| Take | Keyframe | Ação de geração |
|---|---|---|
| ref | REF-CARTA | **Reaproveitar a REF-CARTA já aprovada** em `producao/trevor_a3_confissao`. Se ainda não existir, GERAR DO ZERO com o prompt abaixo. |
| T1 (A1) | K01 | GERAR DO ZERO · ÂNCORA MARK COLLINS + REF-CARTA |
| T1 (A2) | K02 | EDITAR do K01 (muda só o prop e as mãos) |
| T1 (A3) | K03 | EDITAR do K01 (muda só o prop e as mãos) |
| T1 (A4) | K04 | EDITAR do K01 (muda só o prop e as mãos) |
| T1 (A5) | K05 | EDITAR do K01 (muda só o prop e as mãos) |
| T2, T3, T4 | K06 | GERAR DO ZERO · ÂNCORA MARK COLLINS + REF-CARTA |
| T5, T6 | K07 | EDITAR do K06 (muda só a distância de câmera e a altura da carta) |

Total: 1 referência reaproveitada + 7 keyframes para 6 takes em 5 variações de vídeo.

**Os K02 a K05 saem todos do K01 original, nunca em cascata.**

---

## Trava de identidade e continuidade

Vale para toda imagem e todo clipe. Escrita aqui uma vez, não repetida dentro de cada JSON.

- **Mulher** branca americana, fim dos trinta, magra, ombros estreitos.
- Cabelo ondulado loiro escuro com mechas mais claras queimadas de sol e raiz escura visível, **franja cortina** aberta no meio, comprimento passando dos ombros até o meio do peito, textura natural de praia, sem escova.
- Pele clara **castigada de sol**, com sardas no nariz e nas maçãs, poros visíveis, linhas embaixo dos olhos, e um **sinal escuro pequeno na bochecha esquerda**, perto da linha da mandíbula. Zero maquiagem.
- Olhos castanho-esverdeados, sobrancelhas naturais mais escuras que o cabelo, olhar direto e sereno.
- **A pele castigada é ativo.** Nunca rejuvenescer, nunca alisar.
- Regata canelada creme por baixo, **camisa de linho azul-poeira aberta** por cima, mangas dobradas até o cotovelo, bolso no peito, amarrotado natural do linho.
- **Corrente fina de PRATA com pingente de cruz de prata trabalhada**, de braços ornamentados, bem visível no centro do peito. **Ela é a única das três avatares do ângulo que usa a cruz no pescoço.**
- **Vários anéis de prata chunky nas duas mãos**, incluindo **dois anéis de pedra da lua oval, um em cada mão**, e bandas texturizadas nos outros dedos. Os anéis são parte da identidade dela.
- **Cenário: o mesmo cômodo claro da imagem de referência, inalterado.** Não redescrever o cômodo item a item. As três âncoras que importam são o **quadro emoldurado das fases da lua** atrás do ombro direito dela, o **crucifixo de madeira** acima e à direita, e o **aparador baixo de madeira à direita com uma vela branca acesa em copo de vidro, uma bandeira dos EUA pequena em suporte preto e um aglomerado de quartzo bruto**, com a bandeira visível e em foco.
- Mesa de madeira clara tom mel, tampo gasto e arranhado, ocupando o terço inferior do quadro, com o **leque de cartas de tarô aberto sobre ela** e uma **pedra de quartzo transparente bruta** no canto direito da frente.
- Parede off-white, teto inclinado, janela na borda esquerda. Luz natural neutra e difusa de dia nublado. **A vela é ponto de luz e NÃO ilumina o ambiente.**
- **Zero blur, tudo em foco nítido**, incluindo o quadro da lua, o crucifixo, a bandeira e as cartas. Cara de vídeo de iPhone.

### A gramática dela é a TERCEIRA, e isso é trava de produção
A Trevor A3 segura o **leque na mão**. A Karen A3 mantém as **mãos entrelaçadas** acima do leque na mesa. A Mark apoia as **mãos SOBRE o leque, palma para baixo**. As três rodam o mesmo esqueleto em contas diferentes, e essa diferença mais a joia (cruz de prata e anéis chunky só nela) é o que impede as três contas de parecerem a mesma. **Reforçar em todo keyframe.**

---

## Trava do prop herói: a carta SOULMATE (REF-CARTA)

**A mesma REF-CARTA dos pacotes da Trevor e da Karen.** Reaproveitar a imagem já aprovada, nunca regerar, senão a arte diverge entre as três contas e a congruência com o quiz se perde.

Prompt, caso ainda precise ser gerada:

```text
Uma carta de tarô retangular de cantos arredondados, papel marfim envelhecido com fibra visível e cantos levemente gastos. Borda ornamentada em dourado fosco com arabesco gravado e um floreio em cada canto. Numeral romano em capitulares serifadas no topo. Faixa de título na base com a palavra SOULMATE em capitulares serifadas espaçadas. No centro, duas figuras humanas de túnicas atemporais lado a lado, em estilo simbólico chapado com hachura fina de nanquim. Atrás delas um motivo celeste com um sol estilizado, uma lua crescente e estrelas de cinco pontas. Paleta limitada e fosca: dourado antigo, marfim, rosa empoeirado e azul pálido.
```

⚠️ **A carta é o alvo da ação nos cinco ganchos**, e é ela que fica na mão dela do T2 até o fim.

⚠️ **REF-CARTA é a única exceção da regra da bandeira dos EUA.** Objeto isolado sem cenário, e pôr bandeira ali contaminaria todo keyframe que anexasse a referência.

⚠️ **O negative da REF-CARTA não pode carregar `no words overlaid on the image`**, senão mata a palavra SOULMATE. Usar `no captions, no subtitles, no watermark`.

---

## Trava da 2ª pessoa (REF-A)

**Não se aplica neste vídeo.** O modelo é uma pessoa só do primeiro ao último frame, e o clone também. `no second person` entra no negative de todos.

---

## Gate de composição visual e gate de realismo, rodados antes do primeiro JSON

```
HEROI
[x] 1. O heroi (as maos com os aneis sobre o leque) esta no LOWER FOREGROUND, mais perto da lente que o rosto
[x] 2. Nada compete com ele. Fora as tres ancoras, o comodo nao e descrito
[x] 3. Volume explicitado onde importa (o leque aberto inteiro, a camada de sal cobrindo a arte)

DISTANCIA
[x] 4. "Da pra estar mais perto?" Setup B fecha em relacao ao A, Setup C fecha em relacao ao B
[x] 5. Pessoas: peito pra cima no A e no B, ombros pra cima no C
[x] 6. O take mais fechado do video inteiro e o do CTA (Setup C, T5 e T6)

FUNDO
[x] 7. Cenario RECONHECIVEL e nunca inventariado: quadro da lua, crucifixo, aparador com vela e bandeira
[x] 8. Fundo reduzido por ENQUADRAMENTO, nunca por blur
[x] 9. Menos elementos descritos = mais qualidade de geracao

2a PESSOA
[x] 10. Nao existe 2a pessoa neste video

REALISMO
[x] 1. Heroi isolado, tres ancoras de fundo
[x] 2. Camera puxada pra perto, o heroi enche o terco inferior
[x] 3. Luz NEUTRA de dia nublado. A vela e ponto de luz e nao ilumina o ambiente
[x] 4. Negative carrega no warm orange color cast, no yellow tint, no golden glow
[x] 5. Fundo descrito com especificidade e nunca borrado
[x] 6. O prop que teima (a carta) tem REF-CARTA aprovada e reaproveitada
[x] 7. Bloco de realismo padrao colado por inteiro em todo prompt
```

---

# Prompts de imagem

## REF-CARTA · A CARTA SOULMATE · REAPROVEITAR DO PACOTE DA TREVOR · GERAR DO ZERO SÓ SE NÃO EXISTIR

A carta sozinha sobre fundo neutro, nada mais em quadro.

```json
{
  "shot_id": "REF_CARTA_soulmate_holo",
  "reference_use": "No reference image. Generate the object alone. No person, no hands, no room.",
  "identity_main": "No person. A single modern printed tarot card lying flat and straight, filling most of the frame, photographed from directly above on a plain neutral light gray surface.",
  "prop": "A rectangular tarot card with rounded corners, printed on smooth clean cardstock. A wide mirror-metallic border frames the whole card, silver with a rainbow holographic sheen that shifts across it the way foil stamping catches the light, with fine engraved scrollwork and a flourish in each corner. At the top centre, inside a small tablet set into the border, the roman numeral VI in spaced serif capitals. Across the bottom, a cream title band carries the word SOULMATE in spaced serif capitals with a small red heart at the right end of the band.",
  "card_art": "Inside the border, a man and a woman stand facing each other in profile, hands joined, seen from the knees up, painted in a rich saturated illustrative style with fine detail and clean line work. He wears a dark timeless coat, she wears a long deep rose dress. Between and above their heads a single luminous white heart shines, with light rays spreading behind it into a lavender and pink sky. An arch of climbing roses in crimson and blush frames them on both sides, with large open roses along the base. Timeless clothing only, never modern clothing, never cartoon faces.",
  "palette": "Saturated and vivid: crimson and blush rose, deep pink, lavender, warm gold and clean white light, over the silver rainbow sheen of the metallic border.",
  "scene": "Plain neutral light gray surface, nothing else in frame.",
  "composition": "Straight top-down, the card fills most of the frame, all four edges and all four corners fully visible, the whole card readable.",
  "camera": "top-down, straight on, flat, close",
  "state": "Start frame: the card lying still and flat, fully readable.",
  "lighting": "Soft neutral diffuse daylight, even across the card, no glare, so the metallic border reads as a printed foil finish and not as a light source.",
  "realism": "Real printed cardstock with a smooth foil-stamped surface, visible ink detail in the illustration, realistic soft shadow under the card, iPhone-footage look, phone camera look not professional photography, no AI polish, no blur anywhere, everything in sharp focus.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no cartoon style, no children's book illustration, no cute rounded faces, no modern clothing, no plain white border, no comic art, no 3d render, no gothic art, no skulls, no ravens, no snakes, no swords, no inverted symbols, no sigils, no captions, no subtitles, no watermark, no hands, no people, no blur. The ONLY text on the card is the roman numeral VI at the top and the word SOULMATE in the bottom title band."
}
```

> ⚠️ **ESTILO NOVO, decidido pelo Luigi em 2026-08-29.** A carta passou a ser **holográfica / foil e saturada**, e este prompt já está reescrito por inteiro nesse estilo. A paleta pálida antiga (marfim, dourado fosco, rosa empoeirado, azul pálido) está **revogada**. A trava do ângulo continua sendo a **leitura** e não a cor: casal, coração luminoso, rosas, luz. Sem caveira, corvo, serpente, espada ou símbolo invertido.
>
> ⚠️ **DUAS armadilhas técnicas já resolvidas dentro do prompt.** 1) O negative padrão do projeto carrega `no words overlaid on the image`, que mataria a palavra da carta, e aqui foi trocado por `no captions, no subtitles, no watermark`. 2) O bloco de realismo padrão carrega `no golden glow`, `no warm orange color cast`, `no sparkles` e `no glowing edges`, que matariam o foil e o coração luminoso, e por isso **ficam de fora só aqui**. Nos keyframes da avatar segurando a carta o negative segue completo e normal, porque lá a arte já vem travada pela REF anexada.


## K01 · T1 · GANCHO A1, A CARTA QUE APARECE SOZINHA · GERAR DO ZERO · ÂNCORA MARK COLLINS + REF-CARTA

Ela desliza a palma pelo leque e uma carta se solta e vira sozinha, virada pra cima sob os dedos dela.

```json
{
  "shot_id": "K01_hook_a1_carta_aparece",
  "reference_use": "Use the first attached image ONLY for the woman's face, identity, hair, wardrobe, jewelry and the room. Use the second attached image ONLY for the artwork of the SOULMATE tarot card so it is exactly the same card. Do NOT copy the pose or framing of either reference.",
  "identity_main": "The EXACT woman from the first reference image, female, white American woman in her late thirties, slim with narrow shoulders, long wavy dark blonde hair with sun bleached lighter streaks and visible dark roots, soft curtain bangs parted in the middle, length past her shoulders to mid chest, natural undone beach texture, fair sun-worn skin with freckles across her nose and cheeks, visible pores, fine lines under the eyes, a small dark mole on her left cheek near the jawline, hazel green brown eyes, natural eyebrows darker than her hair, direct calm gaze.",
  "wardrobe": "Cream ribbed tank top under an open dusty blue linen shirt with the sleeves rolled to the elbow and a chest pocket, natural linen creasing. A thin SILVER chain with an ornate silver cross pendant clearly visible at the center of her chest. Several chunky silver rings across both hands, including one wide oval moonstone ring on each hand, and textured bands on the other fingers.",
  "prop": "A wide fan of face-up tarot cards from the same modern holographic deck, each with a wide mirror-metallic silver border that catches a rainbow sheen and saturated illustrated art, spread open on the tabletop under her hands, and the EXACT SOULMATE card from the second reference image, which has just come loose and turned face up under her fingers.",
  "scene": "The same bright room as the reference image, unchanged. Three things read clearly behind her: a framed moon phase print in a thin wooden frame behind her right shoulder, a small wooden crucifix high on the right, and a low wooden console on the right holding a lit white candle in a glass cup, a small United States flag on a black stand and a raw quartz cluster, the flag clearly visible and in sharp focus. Off-white wall, sloped ceiling, a window at the left edge. A honey toned light wood table with a worn scratched top runs across the lower third of the frame, with a raw clear quartz stone at the front right corner.",
  "posture": "She sits at the table facing the camera, chest up, both forearms resting on the tabletop and both hands laid flat over the spread of cards, palms down, fingers slightly apart, low and close to the lens.",
  "composition": "Chest-up framing from across the table. The tabletop crosses the lower third of the frame and her ringed hands over the open fan sit in the lower foreground, clearly closer to the lens than her face, so the hands and cards are unmistakably the hero. The SOULMATE card lies face up under her fingers. Her face occupies the upper portion of the frame. Only the moon print, the crucifix and the console are readable behind her.",
  "camera": "chest level, straight-on, camera pushed in close from the other side of the table",
  "state": "Start frame: the SOULMATE card has just turned face up under her fingers and her palm is still sliding back from the spread. She is looking down at it, about to speak.",
  "lighting": "Soft neutral diffuse daylight of an overcast day coming from the window on the left, evenly lighting her face, no warm cast. The candle is a small point of light and does not light the room.",
  "realism": "UGC realism, real skin texture with visible pores, individual hair strands, subtle wrinkles, realistic shadows and reflections, iPhone-footage look, phone camera look not professional photography, no AI polish, no beauty smoothing, no blur anywhere, everything in sharp focus including the moon print, the crucifix, the flag, the rings and the cards.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no studio, no plastic skin, no extra fingers, no supernatural lighting, no blur, no artificial lighting, no warm orange color cast, no yellow tint, no golden glow, no beauty smoothing, no de-aging, no skin smoothing, no second person, no gold jewelry"
}
```

## K02 · T1 · GANCHO A2, AS DUAS CARTAS GRUDADAS · EDITAR do K01

Ela levanta uma carta de baixo da palma e vêm duas grudadas costas com costas, e separa com o polegar.

```json
{
  "task": "edit the attached image, keep everything identical except the changes listed",
  "keep_identical": "Keep the woman exactly the same: same face, same freckles and the small mole on her left cheek, same long wavy dark blonde hair with curtain bangs, same cream tank under the open dusty blue linen shirt, same silver chain with the ornate silver cross pendant, same chunky silver rings and moonstone rings on both hands, same seated position. Keep the SAME room exactly: framed moon phase print, wooden crucifix, wooden console with the lit candle, the small United States flag on its black stand and the quartz cluster, honey toned wood table, the raw quartz at the front right corner, same lighting, same camera angle and framing.",
  "change_1": "She has now lifted TWO tarot cards off the spread, stuck together back to back, held just above the tabletop in the lower foreground. Her right thumb is peeling them apart at the corner and a thin gap is opening between them. The front card is the SOULMATE card and the back card shows only its plain patterned back.",
  "change_2": "Her left hand stays laid flat over the rest of the fan, palm down, on the table.",
  "realism": "UGC realism, real skin texture with visible pores, iPhone-footage look, no AI polish, no beauty smoothing, no blur anywhere. Do not make her skin darker, yellowish or orangish. Do not make the colors more saturated.",
  "negative": "do not change the face, do not change identity, do not change the room, do not change the camera angle, no captions, no subtitles, no words overlaid on the image, no plastic skin, no extra fingers, no blur, no warm orange color cast, no yellow tint, no golden glow, no de-aging, no skin smoothing, no second person, no gold jewelry"
}
```

## K03 · T1 · GANCHO A3, A CORRENTE COM CADEADO · EDITAR do K01

A carta sob uma corrente com cadeado sobre a mesa, e ela corta o elo com um alicate pequeno.

```json
{
  "task": "edit the attached image, keep everything identical except the changes listed",
  "keep_identical": "Keep the woman exactly the same: same face, same freckles and the small mole on her left cheek, same long wavy dark blonde hair with curtain bangs, same cream tank under the open dusty blue linen shirt, same silver chain with the ornate silver cross pendant, same chunky silver rings and moonstone rings on both hands, same seated position. Keep the SAME room exactly: framed moon phase print, wooden crucifix, wooden console with the lit candle, the small United States flag on its black stand and the quartz cluster, honey toned wood table, the raw quartz at the front right corner, same lighting, same camera angle and framing.",
  "change_1": "The SOULMATE card now lies flat on the table in front of the fan with a thin steel chain looped across it and a small closed padlock resting on the chain, in the lower foreground closer to the lens than her face.",
  "change_2": "She holds a small pair of pliers in her right hand, closed around one link of the chain, in the moment just before the link gives. Her left hand stays laid flat on the table beside the spread, palm down.",
  "realism": "UGC realism, real metal texture, real skin texture with visible pores, iPhone-footage look, no AI polish, no beauty smoothing, no blur anywhere. Do not make her skin darker, yellowish or orangish. Do not make the colors more saturated.",
  "negative": "do not change the face, do not change identity, do not change the room, do not change the camera angle, no captions, no subtitles, no words overlaid on the image, no plastic skin, no extra fingers, no blur, no warm orange color cast, no yellow tint, no golden glow, no de-aging, no skin smoothing, no second person, no gold jewelry"
}
```

## K04 · T1 · GANCHO A4, A PENEIRA DE SAL · EDITAR do K01

Ela peneira sal branco fino sobre a carta e a arte vai sumindo sob a camada.

```json
{
  "task": "edit the attached image, keep everything identical except the changes listed",
  "keep_identical": "Keep the woman exactly the same: same face, same freckles and the small mole on her left cheek, same long wavy dark blonde hair with curtain bangs, same cream tank under the open dusty blue linen shirt, same silver chain with the ornate silver cross pendant, same chunky silver rings and moonstone rings on both hands, same seated position. Keep the SAME room exactly: framed moon phase print, wooden crucifix, wooden console with the lit candle, the small United States flag on its black stand and the quartz cluster, honey toned wood table, the raw quartz at the front right corner, same lighting, same camera angle and framing.",
  "change_1": "The SOULMATE card lies flat on the table in front of the fan, in the lower foreground closer to the lens than her face. She holds a small round metal sieve in her right hand, raised just above the card, and a thin even fall of fine white salt is coming through it and settling on the card in a soft growing layer that already covers the lower part of the artwork.",
  "change_2": "Her left hand stays laid flat on the table beside the spread, palm down.",
  "realism": "UGC realism, real salt grain texture, real skin texture with visible pores, iPhone-footage look, no AI polish, no beauty smoothing, no blur anywhere. Do not make her skin darker, yellowish or orangish. Do not make the colors more saturated.",
  "negative": "do not change the face, do not change identity, do not change the room, do not change the camera angle, no captions, no subtitles, no words overlaid on the image, no plastic skin, no extra fingers, no blur, no warm orange color cast, no yellow tint, no golden glow, no de-aging, no skin smoothing, no second person, no gold jewelry"
}
```

## K05 · T1 · GANCHO A5, O LEQUE EMPURRADO · EDITAR do K01

🎣 Clickbait puro. Ela empurra as duas palmas pra frente e o leque inteiro se espalha pela mesa, com a carta SOULMATE parando virada pra cima.

```json
{
  "task": "edit the attached image, keep everything identical except the changes listed",
  "keep_identical": "Keep the woman exactly the same: same face, same freckles and the small mole on her left cheek, same long wavy dark blonde hair with curtain bangs, same cream tank under the open dusty blue linen shirt, same silver chain with the ornate silver cross pendant, same chunky silver rings and moonstone rings on both hands, same seated position. Keep the SAME room exactly: framed moon phase print, wooden crucifix, wooden console with the lit candle, the small United States flag on its black stand and the quartz cluster, honey toned wood table, the raw quartz at the front right corner, same lighting, same camera angle and framing.",
  "change_1": "The neat fan is gone. The whole spread has just been pushed forward and scattered loose across the tabletop in the lower foreground, a wide messy layer of face-up and face-down cards covering most of the table, much closer to the lens than her face. The SOULMATE card has come to rest face up on top of the scatter, fully readable.",
  "change_2": "Both of her hands are still extended forward over the table, palms down and open, just past the scattered cards, in the frozen instant right after the push. She is not gripping anything.",
  "realism": "UGC realism, real card and paper texture, real skin texture with visible pores, iPhone-footage look, no AI polish, no beauty smoothing, no blur anywhere. Do not make her skin darker, yellowish or orangish. Do not make the colors more saturated.",
  "negative": "do not change the face, do not change identity, do not change the room, do not change the camera angle, no captions, no subtitles, no words overlaid on the image, no plastic skin, no extra fingers, no blur, no warm orange color cast, no yellow tint, no golden glow, no de-aging, no skin smoothing, no second person, no gold jewelry"
}
```

## K06 · T2, T3, T4 · A CARTA NA MÃO · GERAR DO ZERO · ÂNCORA MARK COLLINS + REF-CARTA

Ela ergue a carta SOULMATE na altura do peito com o leque ainda aberto na mesa embaixo. Plano um pouco mais fechado que o do gancho.

```json
{
  "shot_id": "K06_corpo_carta_na_mao",
  "reference_use": "Use the first attached image ONLY for the woman's face, identity, hair, wardrobe, jewelry and the room. Use the second attached image ONLY for the artwork of the SOULMATE tarot card so it is exactly the same card. Do NOT copy the pose or framing of either reference.",
  "identity_main": "The EXACT woman from the first reference image, female, white American woman in her late thirties, slim with narrow shoulders, long wavy dark blonde hair with sun bleached lighter streaks and visible dark roots, soft curtain bangs parted in the middle, length past her shoulders to mid chest, natural undone beach texture, fair sun-worn skin with freckles across her nose and cheeks, visible pores, fine lines under the eyes, a small dark mole on her left cheek near the jawline, hazel green brown eyes, natural eyebrows darker than her hair, direct calm gaze.",
  "wardrobe": "Cream ribbed tank top under an open dusty blue linen shirt with the sleeves rolled to the elbow and a chest pocket, natural linen creasing. A thin SILVER chain with an ornate silver cross pendant clearly visible at the center of her chest. Several chunky silver rings across both hands, including one wide oval moonstone ring on each hand, and textured bands on the other fingers.",
  "prop": "The EXACT SOULMATE card from the second reference image, held upright in her right hand at chest height, facing the camera and fully readable. The wide fan of tarot cards stays spread open on the tabletop below her.",
  "scene": "The same bright room as the reference image, unchanged. Three things read clearly behind her: a framed moon phase print in a thin wooden frame behind her right shoulder, a small wooden crucifix high on the right, and a low wooden console on the right holding a lit white candle in a glass cup, a small United States flag on a black stand and a raw quartz cluster, the flag clearly visible and in sharp focus. Off-white wall, sloped ceiling, a window at the left edge. The top edge of the honey toned wood table with the spread of cards is visible across the very bottom of the frame.",
  "posture": "She sits at the table facing the camera, upright, right forearm raised so the card sits at chest height, left hand laid flat on the table over the spread, palm down.",
  "composition": "Chest-up framing, tighter than the previous setup. Her face fills a large part of the upper frame and the top of her head is cropped by the top edge. The SOULMATE card is held low and pushed forward toward the lens in the lower foreground, clearly closer to the camera than her face, without covering her mouth. Only the moon print, the crucifix and the console are readable behind her.",
  "camera": "chest level, straight-on, close, from the other side of the table",
  "state": "Start frame: she has just raised the card and is looking directly into the lens, about to speak.",
  "lighting": "Soft neutral diffuse daylight of an overcast day coming from the window on the left, evenly lighting her face, no warm cast. The candle is a small point of light and does not light the room.",
  "realism": "UGC realism, real skin texture with visible pores, individual hair strands, subtle wrinkles, realistic shadows and reflections, iPhone-footage look, phone camera look not professional photography, no AI polish, no beauty smoothing, no blur anywhere, everything in sharp focus including the moon print, the crucifix, the flag, the rings and the card.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no studio, no plastic skin, no extra fingers, no supernatural lighting, no blur, no artificial lighting, no warm orange color cast, no yellow tint, no golden glow, no beauty smoothing, no de-aging, no skin smoothing, no second person, no gold jewelry"
}
```

## K07 · T5, T6 · CTA · EDITAR do K06

O take mais fechado do vídeo. Ombros pra cima, a carta subindo perto da lente.

```json
{
  "task": "edit the attached image, keep everything identical except the changes listed",
  "keep_identical": "Keep the woman exactly the same: same face, same freckles and the small mole on her left cheek, same long wavy dark blonde hair with curtain bangs, same cream tank under the open dusty blue linen shirt, same silver chain with the ornate silver cross pendant, same chunky silver rings and moonstone rings, same SOULMATE card with the same artwork. Keep the SAME room exactly: framed moon phase print, wooden crucifix, wooden console with the lit candle, the small United States flag on its black stand and the quartz cluster, same lighting, same camera angle and height.",
  "change_1": "Push the framing in by about twenty percent so it becomes a shoulders-up shot and her face fills more of the frame. Do not change the angle or the height of the camera.",
  "change_2": "She raises the SOULMATE card slightly higher and closer to the lens, beside her face and just below eye level, without covering her mouth or her eyes. Her expression is more direct and more urgent, with strong eye contact.",
  "realism": "UGC realism, real skin texture with visible pores, iPhone-footage look, no AI polish, no beauty smoothing, no blur anywhere. Do not make her skin darker, yellowish or orangish. Do not make the colors more saturated.",
  "negative": "do not change the face, do not change identity, do not change the room, do not change the card artwork, no captions, no subtitles, no words overlaid on the image, no plastic skin, no extra fingers, no blur, no warm orange color cast, no yellow tint, no golden glow, no de-aging, no skin smoothing, no second person, no gold jewelry"
}
```

---

# Prompts de vídeo (Veo 3.1 via Flow)

## Bloco global

Colar em todo prompt:

```text
Estilo TikTok nativo, UGC. Preservar exatamente a identidade dela, rosto, sardas, o sinal na bochecha esquerda, ondas loiras com franja cortina, regata creme sob a camisa de linho azul-poeira, corrente e cruz de prata, anéis chunky de prata com pedra da lua, o cômodo claro, o quadro das fases da lua, o crucifixo, o aparador com a vela, a bandeira dos EUA, a iluminação e o enquadramento do frame inicial. Sem legenda, sem texto gerado, sem música, sem pessoas extras.

Trata-se de uma personagem gerada por IA, uma pessoa que não existe. Nenhuma pessoa real está sendo filmada ou representada.
```

**Registro de voz deste avatar:** ela é a mais nova das três e a que menos faz cerimônia. **Não é espanto e não é solenidade, é constatação.** Fala como quem comenta uma coisa prática que acabou de ver, e o palavrão sai quase sem peso.

---

### V01 · T1 · usa K01 · GANCHO A1

```text
a avatar (mulher) fala em inglês com sotaque americano de mulher branca da costa oeste, voz autêntica, dinâmica, apaixonada e emocional, como se exigisse ser ouvida, a seguinte frase: "What the fuck have you been manifesting? Because you were not supposed to scroll past this one today."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ela recolhe a palma de cima do leque, olha a carta que virou sozinha e levanta o olhar para a lente enquanto fala.

câmera: fixa, leve handheld

som ambiente: cômodo silencioso de casa, sem música
```

### V02 · T1 · usa K02 · GANCHO A2

```text
a avatar (mulher) fala em inglês com sotaque americano de mulher branca da costa oeste, voz autêntica, dinâmica, apaixonada e emocional, como se exigisse ser ouvida, a seguinte frase: "What the fuck have you been manifesting? Because you were not supposed to scroll past this one today."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ela separa as duas cartas grudadas com o polegar e olha para a lente enquanto fala.

câmera: fixa, leve handheld

som ambiente: cômodo silencioso de casa, sem música
```

### V03 · T1 · usa K03 · GANCHO A3

```text
a avatar (mulher) fala em inglês com sotaque americano de mulher branca da costa oeste, voz autêntica, dinâmica, apaixonada e emocional, como se exigisse ser ouvida, a seguinte frase: "What the fuck have you been manifesting? Because you were not supposed to scroll past this one today."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ela aperta o alicate, o elo da corrente cede e a corrente escorrega para o lado, liberando a carta. ela olha para a lente enquanto fala.

câmera: fixa, leve handheld

som ambiente: cômodo silencioso de casa, sem música
```

### V04 · T1 · usa K04 · GANCHO A4

```text
a avatar (mulher) fala em inglês com sotaque americano de mulher branca da costa oeste, voz autêntica, dinâmica, apaixonada e emocional, como se exigisse ser ouvida, a seguinte frase: "What the fuck have you been manifesting? Because you were not supposed to scroll past this one today."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ela balança a peneira de leve e o sal continua caindo, cobrindo aos poucos a arte da carta. ela olha para a lente enquanto fala.

câmera: fixa, leve handheld

som ambiente: cômodo silencioso de casa, sem música
```

### V05 · T1 · usa K05 · GANCHO A5

```text
a avatar (mulher) fala em inglês com sotaque americano de mulher branca da costa oeste, voz autêntica, dinâmica, apaixonada e emocional, como se exigisse ser ouvida, a seguinte frase: "What the fuck have you been manifesting? Because you were not supposed to scroll past this one today."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: as últimas cartas do leque empurrado ainda escorregam e param na mesa. ela olha para a bagunça e levanta o olhar para a lente enquanto fala, sem recolher nada.

câmera: fixa, leve handheld

som ambiente: cômodo silencioso de casa, sem música
```

### V06 · T2 · usa K06

```text
a avatar (mulher) fala em inglês com sotaque americano de mulher branca da costa oeste, voz autêntica, dinâmica, apaixonada e emocional, como se exigisse ser ouvida, a seguinte frase: "Somebody is about to confess something to you. And it is the person you already have in your head right now."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ela mantém a carta erguida e parada na mão direita e olha direto para a lente enquanto fala.

câmera: fixa, leve handheld

som ambiente: cômodo silencioso de casa, sem música
```

### V07 · T3 · usa K06

```text
a avatar (mulher) fala em inglês com sotaque americano de mulher branca da costa oeste, voz autêntica, dinâmica, apaixonada e emocional, como se exigisse ser ouvida, a seguinte frase: "They have been sitting on it for a while. And in the next twenty four hours, they stop sitting on it."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ela inclina a carta de leve para a frente ao dizer as vinte e quatro horas e mantém o olhar na lente.

câmera: fixa, leve push-in

som ambiente: cômodo silencioso de casa, sem música
```

### V08 · T4 · usa K06

```text
a avatar (mulher) fala em inglês com sotaque americano de mulher branca da costa oeste, voz autêntica, dinâmica, apaixonada e emocional, como se exigisse ser ouvida, a seguinte frase: "Your part is easy. Take the good energy I am putting on this. Comment two two two, and it is claimed."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ela mantém a carta na mão direita e faz um gesto pequeno e contido com a mão esquerda ao dizer o número.

câmera: fixa, leve handheld

som ambiente: cômodo silencioso de casa, sem música
```

### V09 · T5 · usa K07

```text
a avatar (mulher) fala em inglês com sotaque americano de mulher branca da costa oeste, voz autêntica, dinâmica, apaixonada e emocional, como se exigisse ser ouvida, a seguinte frase: "Follow me first, or it will not let me reach you. Then I send their face straight to your messages."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ela aponta o indicador esquerdo para a lente ao dizer follow me first, mantendo a carta erguida na mão direita, e mantém contato visual forte.

câmera: fixa, leve push-in

som ambiente: cômodo silencioso de casa, sem música
```

### V10 · T6 · usa K07

```text
a avatar (mulher) fala em inglês com sotaque americano de mulher branca da costa oeste, voz autêntica, dinâmica, apaixonada e emocional, como se exigisse ser ouvida, a seguinte frase: "Do it now. If you scroll past this, you cancel it, and somebody else discovers what was meant to be yours."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ela aproxima um pouco a carta da lente ao dizer somebody else e segura o olhar até o fim, sem sorrir.

câmera: fixa, leve push-in

som ambiente: cômodo silencioso de casa, sem música
```

---

## Mapa de âncoras

| Keyframe | Referências a anexar | Modelo |
|---|---|---|
| REF-CARTA | **reaproveitar a do pacote da Trevor A3**, nunca regerar | já aprovada |
| K01 | âncora Mark Collins + REF-CARTA | Nano Banana **Pro**, várias variações |
| K02 | K01 aprovado | Nano Banana 2, edição |
| K03 | K01 aprovado (**nunca do K02**) | Nano Banana 2, edição |
| K04 | K01 aprovado (**nunca do K02 ou K03**) | Nano Banana 2, edição |
| K05 | K01 aprovado (**nunca do K02, K03 ou K04**) | Nano Banana 2, edição |
| K06 | âncora Mark Collins + REF-CARTA | Nano Banana 2 |
| K07 | K06 aprovado | Nano Banana 2, edição |

---

## Montagem no CapCut

- Timeline 1080x1920, 30 fps.
- **Cinco vídeos, um por gancho.** Cada um monta V0X seguido de V06, V07, V08, V09 e V10, que são os mesmos arquivos nos cinco.
- Cortes duros entre todos os takes, com peso só no corte do gancho para o V06.
- Cortar o silêncio inicial de cada clipe para a fala começar imediatamente.
- Legenda karaokê palavra a palavra com destaque amarelo na altura do peito, no estilo do vídeo modelo. **Nunca cobrir a carta nem as mãos**, que é onde estão os anéis.
- Caixa de gancho branca no topo, uma por variação: A1 `SCROLL PAST THIS` · A2 `MAN HIDING TWO` · A3 `ASKING WHY THEY` · A4 `TO SHARE THIS` · A5 `SKIP THIS Y'ALL`.
- Gráfico flutuante `222` fixo no canto superior o vídeo inteiro, e `222` isolado na tela no CTA.
- **Nunca publicar duas variações na mesma conta, e NUNCA publicar este pacote nas contas que rodarem o `trevor_a3_confissao` ou o `karen_a3_confissao`.** É o mesmo esqueleto.
- Color grading: temp -3, tint +2, saturação -6, exposição -3, contraste +12, highlight -35, shadow +18, fade +6.

## Gates de qualidade

1. Ela é a mesma mulher nos dez clipes, com as mesmas sardas, o mesmo sinal na bochecha esquerda e a mesma franja cortina.
2. **A CRUZ DE PRATA está no pescoço em todos os planos.** Ela é a única das três avatares do ângulo que a usa, e é um dos diferenciadores.
3. **Os anéis chunky de prata estão nas duas mãos**, com um anel de pedra da lua em cada, em todos os planos.
4. **O leque fica aberto na MESA e as mãos apoiadas SOBRE ele, palma para baixo.** Nunca o leque na mão (gramática da Trevor) nem mãos entrelaçadas (gramática da Karen).
5. A carta SOULMATE tem arte idêntica à dos pacotes da Trevor A3 e da Karen A3.
6. A palavra SOULMATE está legível e é o único texto gerado dentro de qualquer imagem.
7. A bandeira dos EUA aparece visível e em foco em todos os keyframes com cenário. A REF-CARTA é a única sem, de propósito.
8. A vela aparece acesa mas **não ilumina o ambiente**. A luz da cena é neutra de dia nublado, sem cast quente.
9. O quadro das fases da lua, o crucifixo e o aparador estão nítidos. Nada foi borrado.
10. Nenhuma legenda ou palavra foi sobreposta na imagem pelo gerador.
11. Mãos com cinco dedos, sem fusão com as cartas, com a peneira nem com o alicate.
12. K02 a K05 saíram todos do K01 original, nunca em cascata.
13. O take do CTA (K07) é o mais fechado do vídeo inteiro.
14. `222` está dito na fala do T4 e isolado na tela no CTA.
15. **O rosto da alma gêmea nunca aparece no vídeo.**
16. Nenhuma leitura de pacto ou feitiço. A carta é clara, e aqui o registro é carregado pelo crucifixo na parede E pela cruz no pescoço.
