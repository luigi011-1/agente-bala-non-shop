# Karen Thompson (A3) | Ângulo 3 (Auraly) | Pacote de Prompts

Vídeo modelo: `DcjIIyWq3Bt_.mp4`

Âncora de identidade e cenário: `producao/_ancoras/karen_a3_ancora.jpeg`

Funil: vídeo -> comment `222` -> DM -> link do quiz Auraly

⚠️ **Existe outra Karen Thompson**, a sulista de ~60 anos da Jupi Hydration. Esta é a do Auraly, quarentona cacheada de traços latinos. Conferir o produto antes de usar o nome.

---

## Índice de geração

| Take | Keyframe | Ação de geração |
|---|---|---|
| ref | REF-CARTA | **Reaproveitar a REF-CARTA já aprovada** em `producao/trevor_a3_confissao`. Se ainda não existir, GERAR DO ZERO com o prompt abaixo. |
| T1 (A1) | K01 | GERAR DO ZERO · ÂNCORA KAREN A3 + REF-CARTA |
| T1 (A2) | K02 | EDITAR do K01 (muda só o prop e as mãos) |
| T1 (A3) | K03 | EDITAR do K01 (muda só o prop e as mãos) |
| T1 (A4) | K04 | EDITAR do K01 (muda só o prop e as mãos) |
| T1 (A5) | K05 | EDITAR do K01 (muda só o prop e as mãos) |
| T2, T3, T4 | K06 | GERAR DO ZERO · ÂNCORA KAREN A3 + REF-CARTA |
| T5, T6 | K07 | EDITAR do K06 (muda só a distância de câmera e a altura da carta) |

Total: 1 referência reaproveitada + 7 keyframes para 6 takes em 5 variações de vídeo.

**Os K02 a K05 saem todos do K01 original, nunca em cascata.**

---

## Trava de identidade e continuidade

Vale para toda imagem e todo clipe. Escrita aqui uma vez, não repetida dentro de cada JSON.

- Mulher americana de traços latinos, início dos quarenta, porte médio, rosto fino de maçãs altas.
- Pele oliva morena clara, lisa, com poros visíveis e brilho natural, poucas linhas. Sem maquiagem visível.
- Cabelo cacheado longo e bem definido até o meio do peito, castanho médio com mechas loiro claro e fios grisalhos prateados bem visíveis, volume grande, repicado enquadrando o rosto.
- Sobrancelhas escuras e cheias, olhos castanho escuros amendoados, lábios cheios, nariz reto. Olhar sereno e firme.
- Blusa boho creme de manga curta com gola em V, barra e faixas estampadas em laranja tijolo, azul marinho e vinho.
- **Duas alianças de prata e um anel de pedra clara. Sem colar em quadro.** A sobriedade de acessório é a marca dela e é o que a separa da Trevor A3.
- **Cenário: a mesma sala de leitura clara da imagem de referência, inalterada.** Não redescrever o cômodo item a item. As três âncoras que importam são a **tapeçaria de mandala clara, dourada sobre creme**, à esquerda, o **crucifixo de madeira** acima e à direita, e a **prateleira estreita de madeira escura com três velas brancas acesas e uma bandeira dos EUA pequena em suporte preto**, à direita, visível e em foco.
- Mesa de carvalho claro ocupando o terço inferior do quadro, com o **leque de cartas de tarô aberto sobre ela**.
- Parede creme, teto texturizado. Luz natural neutra e difusa de dia nublado. **As velas são pontos de luz e NÃO iluminam o ambiente**, senão entra cast quente e denuncia IA.
- **Zero blur, tudo em foco nítido**, incluindo a mandala, o crucifixo, as velas e a bandeira. Cara de vídeo de iPhone.

### A gramática dela é OUTRA, e isso é trava de produção
A Trevor A3 segura o **leque na mão**. A Karen mantém o **leque aberto na mesa** e ergue só a carta SOULMATE. As duas rodam o mesmo esqueleto em contas diferentes, e essa diferença mais a tabela de traços é tudo que impede as duas contas de parecerem a mesma. **Reforçar em todo keyframe.**

---

## Trava do prop herói: a carta SOULMATE (REF-CARTA)

**A mesma REF-CARTA do pacote da Trevor.** Reaproveitar a imagem já aprovada, nunca regerar, senão a arte diverge entre as duas contas e a congruência com o quiz se perde.

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
[x] 1. O heroi (a carta e as maos) esta no LOWER FOREGROUND, mais perto da lente que o rosto
[x] 2. Nada compete com ele. Fora as tres ancoras, o comodo nao e descrito
[x] 3. Volume explicitado onde importa (o leque aberto inteiro, a camada de sal cobrindo a arte)

DISTANCIA
[x] 4. "Da pra estar mais perto?" Setup B fecha em relacao ao A, Setup C fecha em relacao ao B
[x] 5. Pessoas: peito pra cima no A e no B, ombros pra cima no C
[x] 6. O take mais fechado do video inteiro e o do CTA (Setup C, T5 e T6)

FUNDO
[x] 7. Cenario RECONHECIVEL e nunca inventariado: mandala, crucifixo, prateleira com velas e bandeira
[x] 8. Fundo reduzido por ENQUADRAMENTO, nunca por blur
[x] 9. Menos elementos descritos = mais qualidade de geracao

2a PESSOA
[x] 10. Nao existe 2a pessoa neste video

REALISMO
[x] 1. Heroi isolado, tres ancoras de fundo
[x] 2. Camera puxada pra perto, o heroi enche o terco inferior
[x] 3. Luz NEUTRA de dia nublado. As velas sao pontos de luz e nao iluminam o ambiente
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


## K01 · T1 · GANCHO A1, A CARTA QUE SAI SOZINHA · GERAR DO ZERO · ÂNCORA KAREN A3 + REF-CARTA

Ela ajeita o leque aberto na mesa e a carta SOULMATE escorrega sozinha pra fora do leque e para virada pra cima.

```json
{
  "shot_id": "K01_hook_a1_carta_sai",
  "reference_use": "Use the first attached image ONLY for the woman's face, identity, hair, wardrobe, rings and the room. Use the second attached image ONLY for the artwork of the SOULMATE tarot card so it is exactly the same card. Do NOT copy the pose or framing of either reference.",
  "identity_main": "The EXACT woman from the first reference image, female, American woman with latin features in her early forties, medium build, narrow face with high cheekbones, olive skin with visible pores and natural sheen, long well defined curls falling to mid chest in medium brown with light blonde streaks and clearly visible silver grey strands, big volume, layers framing the face, full dark eyebrows, dark almond shaped brown eyes, full lips, straight nose, calm steady gaze.",
  "wardrobe": "Cream short-sleeved boho blouse with a V neck and printed border bands in brick orange, navy blue and wine. Two plain silver bands and one pale stone ring on her fingers. No necklace.",
  "prop": "A wide fan of face-up tarot cards from the same modern holographic deck, each with a wide mirror-metallic silver border that catches a rainbow sheen and saturated illustrated art, spread open on the tabletop in front of her, and the EXACT SOULMATE card from the second reference image, which has just slid out of the fan on its own and come to rest face up beside it.",
  "scene": "The same bright reading room as the reference image, unchanged. Three things read clearly behind her: a light mandala tapestry in gold on cream on the left, a small wooden crucifix high on the right, and a narrow dark wood shelf on the right holding three lit white pillar candles and a small United States flag on a black stand, the flag clearly visible and in sharp focus. Cream wall, textured ceiling. A light oak table runs across the lower third of the frame.",
  "posture": "She sits at the table facing the camera, chest up, both forearms resting on the tabletop, her hands low and close to the lens just behind the spread of cards.",
  "composition": "Chest-up framing from across the table. The tabletop crosses the lower third of the frame and the open fan of cards plus the fallen SOULMATE card sit in the lower foreground, clearly closer to the lens than her face, so the cards are unmistakably the hero. Her face occupies the upper portion of the frame. Only the tapestry, the crucifix and the candle shelf are readable behind her.",
  "camera": "chest level, straight-on, camera pushed in close from the other side of the table",
  "state": "Start frame: the SOULMATE card has just come to rest face up beside the fan and her fingertips are still near the spread. She is looking down at it, about to speak.",
  "lighting": "Soft neutral diffuse daylight of an overcast day coming from the side, evenly lighting her face, no warm cast. The three candles are small points of light and do not light the room.",
  "realism": "UGC realism, real skin texture with visible pores, individual hair strands, subtle wrinkles, realistic shadows and reflections, iPhone-footage look, phone camera look not professional photography, no AI polish, no beauty smoothing, no blur anywhere, everything in sharp focus including the mandala pattern, the crucifix, the candles, the flag and the cards.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no studio, no plastic skin, no extra fingers, no supernatural lighting, no blur, no artificial lighting, no warm orange color cast, no yellow tint, no golden glow, no beauty smoothing, no de-aging, no skin smoothing, no second person, no necklace, no gold jewelry"
}
```

## K02 · T1 · GANCHO A2, AS DUAS CARTAS GRUDADAS · EDITAR do K01

Ela levanta uma carta do leque da mesa e vêm duas grudadas costas com costas, e separa com o polegar.

```json
{
  "task": "edit the attached image, keep everything identical except the changes listed",
  "keep_identical": "Keep the woman exactly the same: same face, same olive skin, same long defined curls with blonde and silver strands, same cream boho blouse with orange navy and wine border print, same two silver bands and pale stone ring, no necklace, same seated position. Keep the SAME room exactly: light gold mandala tapestry, wooden crucifix, dark wood shelf with three lit white candles and the small United States flag on its black stand, light oak table, same lighting, same camera angle and framing.",
  "change_1": "She has now lifted TWO tarot cards off the spread, stuck together back to back, held just above the tabletop in the lower foreground. Her right thumb is peeling them apart at the corner and a thin gap is opening between them. The front card is the SOULMATE card and the back card shows only its plain patterned back.",
  "change_2": "The rest of the fan stays spread open on the table below her hands.",
  "realism": "UGC realism, real skin texture with visible pores, iPhone-footage look, no AI polish, no beauty smoothing, no blur anywhere. Do not make her skin darker, yellowish or orangish. Do not make the colors more saturated.",
  "negative": "do not change the face, do not change identity, do not change the room, do not change the camera angle, no captions, no subtitles, no words overlaid on the image, no plastic skin, no extra fingers, no blur, no warm orange color cast, no yellow tint, no golden glow, no de-aging, no skin smoothing, no second person, no necklace, no gold jewelry"
}
```

## K03 · T1 · GANCHO A3, A CORRENTE COM CADEADO · EDITAR do K01

A carta sob uma corrente com cadeado sobre a mesa, e ela corta o elo com um alicate pequeno.

```json
{
  "task": "edit the attached image, keep everything identical except the changes listed",
  "keep_identical": "Keep the woman exactly the same: same face, same olive skin, same long defined curls with blonde and silver strands, same cream boho blouse with orange navy and wine border print, same two silver bands and pale stone ring, no necklace, same seated position. Keep the SAME room exactly: light gold mandala tapestry, wooden crucifix, dark wood shelf with three lit white candles and the small United States flag on its black stand, light oak table, same lighting, same camera angle and framing.",
  "change_1": "The SOULMATE card now lies flat on the table in front of the fan with a thin steel chain looped across it and a small closed padlock resting on the chain, in the lower foreground closer to the lens than her face.",
  "change_2": "She holds a small pair of pliers in her right hand, closed around one link of the chain, in the moment just before the link gives. Her left hand rests flat on the table beside the spread.",
  "realism": "UGC realism, real metal texture, real skin texture with visible pores, iPhone-footage look, no AI polish, no beauty smoothing, no blur anywhere. Do not make her skin darker, yellowish or orangish. Do not make the colors more saturated.",
  "negative": "do not change the face, do not change identity, do not change the room, do not change the camera angle, no captions, no subtitles, no words overlaid on the image, no plastic skin, no extra fingers, no blur, no warm orange color cast, no yellow tint, no golden glow, no de-aging, no skin smoothing, no second person, no necklace, no gold jewelry"
}
```

## K04 · T1 · GANCHO A4, A PENEIRA DE SAL · EDITAR do K01

Ela peneira sal branco fino sobre a carta e a arte vai sumindo sob a camada.

```json
{
  "task": "edit the attached image, keep everything identical except the changes listed",
  "keep_identical": "Keep the woman exactly the same: same face, same olive skin, same long defined curls with blonde and silver strands, same cream boho blouse with orange navy and wine border print, same two silver bands and pale stone ring, no necklace, same seated position. Keep the SAME room exactly: light gold mandala tapestry, wooden crucifix, dark wood shelf with three lit white candles and the small United States flag on its black stand, light oak table, same lighting, same camera angle and framing.",
  "change_1": "The SOULMATE card lies flat on the table in front of the fan, in the lower foreground closer to the lens than her face. She holds a small round metal sieve in her right hand, raised just above the card, and a thin even fall of fine white salt is coming through it and settling on the card in a soft growing layer that already covers the lower part of the artwork.",
  "change_2": "Her left hand rests flat on the table beside the spread of cards.",
  "realism": "UGC realism, real salt grain texture, real skin texture with visible pores, iPhone-footage look, no AI polish, no beauty smoothing, no blur anywhere. Do not make her skin darker, yellowish or orangish. Do not make the colors more saturated.",
  "negative": "do not change the face, do not change identity, do not change the room, do not change the camera angle, no captions, no subtitles, no words overlaid on the image, no plastic skin, no extra fingers, no blur, no warm orange color cast, no yellow tint, no golden glow, no de-aging, no skin smoothing, no second person, no necklace, no gold jewelry"
}
```

## K05 · T1 · GANCHO A5, O LEQUE VARRIDO · EDITAR do K01

🎣 Clickbait puro. Ela recolhe a mão e o leque inteiro varre e se espalha pela mesa, com a carta SOULMATE parando virada pra cima.

```json
{
  "task": "edit the attached image, keep everything identical except the changes listed",
  "keep_identical": "Keep the woman exactly the same: same face, same olive skin, same long defined curls with blonde and silver strands, same cream boho blouse with orange navy and wine border print, same two silver bands and pale stone ring, no necklace, same seated position. Keep the SAME room exactly: light gold mandala tapestry, wooden crucifix, dark wood shelf with three lit white candles and the small United States flag on its black stand, light oak table, same lighting, same camera angle and framing.",
  "change_1": "The neat fan is gone. The whole spread has just swept and scattered loose across the tabletop in the lower foreground, a wide messy layer of face-up and face-down cards covering most of the table, much closer to the lens than her face. The SOULMATE card has come to rest face up on top of the scatter, fully readable.",
  "change_2": "Both of her hands are lifted just off the table, palms open and low, in the frozen instant right after the sweep. She is not touching the cards.",
  "realism": "UGC realism, real card and paper texture, real skin texture with visible pores, iPhone-footage look, no AI polish, no beauty smoothing, no blur anywhere. Do not make her skin darker, yellowish or orangish. Do not make the colors more saturated.",
  "negative": "do not change the face, do not change identity, do not change the room, do not change the camera angle, no captions, no subtitles, no words overlaid on the image, no plastic skin, no extra fingers, no blur, no warm orange color cast, no yellow tint, no golden glow, no de-aging, no skin smoothing, no second person, no necklace, no gold jewelry"
}
```

## K06 · T2, T3, T4 · A CARTA NA MÃO · GERAR DO ZERO · ÂNCORA KAREN A3 + REF-CARTA

Ela ergue a carta SOULMATE na altura do peito com o leque ainda aberto na mesa embaixo. Plano um pouco mais fechado que o do gancho.

```json
{
  "shot_id": "K06_corpo_carta_na_mao",
  "reference_use": "Use the first attached image ONLY for the woman's face, identity, hair, wardrobe, rings and the room. Use the second attached image ONLY for the artwork of the SOULMATE tarot card so it is exactly the same card. Do NOT copy the pose or framing of either reference.",
  "identity_main": "The EXACT woman from the first reference image, female, American woman with latin features in her early forties, medium build, narrow face with high cheekbones, olive skin with visible pores and natural sheen, long well defined curls falling to mid chest in medium brown with light blonde streaks and clearly visible silver grey strands, big volume, layers framing the face, full dark eyebrows, dark almond shaped brown eyes, full lips, straight nose, calm steady gaze.",
  "wardrobe": "Cream short-sleeved boho blouse with a V neck and printed border bands in brick orange, navy blue and wine. Two plain silver bands and one pale stone ring on her fingers. No necklace.",
  "prop": "The EXACT SOULMATE card from the second reference image, held upright in her right hand at chest height, facing the camera and fully readable. The wide fan of tarot cards stays spread open on the tabletop below her.",
  "scene": "The same bright reading room as the reference image, unchanged. Three things read clearly behind her: a light mandala tapestry in gold on cream on the left, a small wooden crucifix high on the right, and a narrow dark wood shelf on the right holding three lit white pillar candles and a small United States flag on a black stand, the flag clearly visible and in sharp focus. Cream wall, textured ceiling. The top edge of the light oak table with the spread of cards is visible across the very bottom of the frame.",
  "posture": "She sits at the table facing the camera, upright, right forearm raised so the card sits at chest height, left forearm resting on the table beside the spread.",
  "composition": "Chest-up framing, tighter than the previous setup. Her face fills a large part of the upper frame and the top of her head is cropped by the top edge. The SOULMATE card is held low and pushed forward toward the lens in the lower foreground, clearly closer to the camera than her face, without covering her mouth. Only the tapestry, the crucifix and the candle shelf are readable behind her.",
  "camera": "chest level, straight-on, close, from the other side of the table",
  "state": "Start frame: she has just raised the card and is looking directly into the lens, about to speak.",
  "lighting": "Soft neutral diffuse daylight of an overcast day coming from the side, evenly lighting her face, no warm cast. The three candles are small points of light and do not light the room.",
  "realism": "UGC realism, real skin texture with visible pores, individual hair strands, subtle wrinkles, realistic shadows and reflections, iPhone-footage look, phone camera look not professional photography, no AI polish, no beauty smoothing, no blur anywhere, everything in sharp focus including the mandala pattern, the crucifix, the candles, the flag and the card.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no studio, no plastic skin, no extra fingers, no supernatural lighting, no blur, no artificial lighting, no warm orange color cast, no yellow tint, no golden glow, no beauty smoothing, no de-aging, no skin smoothing, no second person, no necklace, no gold jewelry"
}
```

## K07 · T5, T6 · CTA · EDITAR do K06

O take mais fechado do vídeo. Ombros pra cima, a carta subindo perto da lente.

```json
{
  "task": "edit the attached image, keep everything identical except the changes listed",
  "keep_identical": "Keep the woman exactly the same: same face, same olive skin, same long defined curls with blonde and silver strands, same cream boho blouse with orange navy and wine border print, same two silver bands and pale stone ring, no necklace, same SOULMATE card with the same artwork. Keep the SAME room exactly: light gold mandala tapestry, wooden crucifix, dark wood shelf with three lit white candles and the small United States flag on its black stand, same lighting, same camera angle and height.",
  "change_1": "Push the framing in by about twenty percent so it becomes a shoulders-up shot and her face fills more of the frame. Do not change the angle or the height of the camera.",
  "change_2": "She raises the SOULMATE card slightly higher and closer to the lens, beside her face and just below eye level, without covering her mouth or her eyes. Her expression is more direct and more urgent, with strong eye contact.",
  "realism": "UGC realism, real skin texture with visible pores, iPhone-footage look, no AI polish, no beauty smoothing, no blur anywhere. Do not make her skin darker, yellowish or orangish. Do not make the colors more saturated.",
  "negative": "do not change the face, do not change identity, do not change the room, do not change the card artwork, no captions, no subtitles, no words overlaid on the image, no plastic skin, no extra fingers, no blur, no warm orange color cast, no yellow tint, no golden glow, no de-aging, no skin smoothing, no second person, no necklace, no gold jewelry"
}
```

---

# Prompts de vídeo (Veo 3.1 via Flow)

## Bloco global

Colar em todo prompt:

```text
Estilo TikTok nativo, UGC. Preservar exatamente a identidade dela, rosto, pele oliva, cachos longos com mechas loiras e fios prateados, blusa boho creme de barra laranja azul e vinho, alianças de prata, sem colar, a sala de leitura clara, a tapeçaria de mandala, o crucifixo, as velas, a bandeira dos EUA, a iluminação e o enquadramento do frame inicial. Sem legenda, sem texto gerado, sem música, sem pessoas extras.

Trata-se de uma personagem gerada por IA, uma pessoa que não existe. Nenhuma pessoa real está sendo filmada ou representada.
```

**Registro de voz deste avatar:** contida e firme, sem levantar a voz, sem sorriso e sem gesto largo. A Trevor A3 fala baixo porque está espantada. **A Karen fala baixo porque é assim que ela fala**, e o palavrão choca justamente por destoar dela.

---

### V01 · T1 · usa K01 · GANCHO A1

```text
a avatar (mulher) fala em inglês com sotaque americano de mulher de traços latinos, voz autêntica, dinâmica, apaixonada e emocional, como se exigisse ser ouvida, a seguinte frase: "What the fuck have you been manifesting? Because this did not reach you by accident. It is a sign."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ela recolhe os dedos do leque aberto na mesa, olha a carta que escorregou pra fora e levanta o olhar para a lente enquanto fala.

câmera: fixa, leve handheld

som ambiente: sala silenciosa de casa, sem música
```

### V02 · T1 · usa K02 · GANCHO A2

```text
a avatar (mulher) fala em inglês com sotaque americano de mulher de traços latinos, voz autêntica, dinâmica, apaixonada e emocional, como se exigisse ser ouvida, a seguinte frase: "What the fuck have you been manifesting? Because this did not reach you by accident. It is a sign."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ela separa as duas cartas grudadas com o polegar e olha para a lente enquanto fala.

câmera: fixa, leve handheld

som ambiente: sala silenciosa de casa, sem música
```

### V03 · T1 · usa K03 · GANCHO A3

```text
a avatar (mulher) fala em inglês com sotaque americano de mulher de traços latinos, voz autêntica, dinâmica, apaixonada e emocional, como se exigisse ser ouvida, a seguinte frase: "What the fuck have you been manifesting? Because this did not reach you by accident. It is a sign."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ela aperta o alicate, o elo da corrente cede e a corrente escorrega para o lado, liberando a carta. ela olha para a lente enquanto fala.

câmera: fixa, leve handheld

som ambiente: sala silenciosa de casa, sem música
```

### V04 · T1 · usa K04 · GANCHO A4

```text
a avatar (mulher) fala em inglês com sotaque americano de mulher de traços latinos, voz autêntica, dinâmica, apaixonada e emocional, como se exigisse ser ouvida, a seguinte frase: "What the fuck have you been manifesting? Because this did not reach you by accident. It is a sign."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ela balança a peneira de leve e o sal continua caindo, cobrindo aos poucos a arte da carta. ela olha para a lente enquanto fala.

câmera: fixa, leve handheld

som ambiente: sala silenciosa de casa, sem música
```

### V05 · T1 · usa K05 · GANCHO A5

```text
a avatar (mulher) fala em inglês com sotaque americano de mulher de traços latinos, voz autêntica, dinâmica, apaixonada e emocional, como se exigisse ser ouvida, a seguinte frase: "What the fuck have you been manifesting? Because this did not reach you by accident. It is a sign."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: as últimas cartas do leque varrido ainda escorregam e param na mesa. ela olha para a bagunça e levanta o olhar para a lente enquanto fala, sem recolher nada.

câmera: fixa, leve handheld

som ambiente: sala silenciosa de casa, sem música
```

### V06 · T2 · usa K06

```text
a avatar (mulher) fala em inglês com sotaque americano de mulher de traços latinos, voz autêntica, dinâmica, apaixonada e emocional, como se exigisse ser ouvida, a seguinte frase: "A confession is coming to you. The person you keep thinking about has been carrying the exact same thing for you."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ela mantém a carta erguida e parada na mão direita e olha direto para a lente enquanto fala, sem sorrir.

câmera: fixa, leve handheld

som ambiente: sala silenciosa de casa, sem música
```

### V07 · T3 · usa K06

```text
a avatar (mulher) fala em inglês com sotaque americano de mulher de traços latinos, voz autêntica, dinâmica, apaixonada e emocional, como se exigisse ser ouvida, a seguinte frase: "They are done hiding it. Inside the next twenty four hours, the thing between you two moves, and it does not move back."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ela inclina a carta de leve para a frente ao dizer as vinte e quatro horas e mantém o olhar na lente.

câmera: fixa, leve push-in

som ambiente: sala silenciosa de casa, sem música
```

### V08 · T4 · usa K06

```text
a avatar (mulher) fala em inglês com sotaque americano de mulher de traços latinos, voz autêntica, dinâmica, apaixonada e emocional, como se exigisse ser ouvida, a seguinte frase: "All you have to do is accept the energy I am sending. Comment two two two, and it is claimed."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ela mantém a carta na mão direita e faz um gesto pequeno e contido com a mão esquerda ao dizer o número.

câmera: fixa, leve handheld

som ambiente: sala silenciosa de casa, sem música
```

### V09 · T5 · usa K07

```text
a avatar (mulher) fala em inglês com sotaque americano de mulher de traços latinos, voz autêntica, dinâmica, apaixonada e emocional, como se exigisse ser ouvida, a seguinte frase: "Follow me first, or it will not let me reach you. Then I send their face straight to your messages."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ela aponta o indicador esquerdo para a lente ao dizer follow me first, mantendo a carta erguida na mão direita, e mantém contato visual forte.

câmera: fixa, leve push-in

som ambiente: sala silenciosa de casa, sem música
```

### V10 · T6 · usa K07

```text
a avatar (mulher) fala em inglês com sotaque americano de mulher de traços latinos, voz autêntica, dinâmica, apaixonada e emocional, como se exigisse ser ouvida, a seguinte frase: "Do it now. If you scroll past this, you cancel it, and somebody else discovers what was meant to be yours."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: ela aproxima um pouco a carta da lente ao dizer somebody else e segura o olhar até o fim, sem sorrir.

câmera: fixa, leve push-in

som ambiente: sala silenciosa de casa, sem música
```

---

## Mapa de âncoras

| Keyframe | Referências a anexar | Modelo |
|---|---|---|
| REF-CARTA | **reaproveitar a do pacote da Trevor A3**, nunca regerar | já aprovada |
| K01 | âncora Karen A3 + REF-CARTA aprovada | Nano Banana **Pro**, várias variações |
| K02 | K01 aprovado | Nano Banana 2, edição |
| K03 | K01 aprovado (**nunca do K02**) | Nano Banana 2, edição |
| K04 | K01 aprovado (**nunca do K02 ou K03**) | Nano Banana 2, edição |
| K05 | K01 aprovado (**nunca do K02, K03 ou K04**) | Nano Banana 2, edição |
| K06 | âncora Karen A3 + REF-CARTA aprovada | Nano Banana 2 |
| K07 | K06 aprovado | Nano Banana 2, edição |

---

## Montagem no CapCut

- Timeline 1080x1920, 30 fps.
- **Cinco vídeos, um por gancho.** Cada um monta V0X seguido de V06, V07, V08, V09 e V10, que são os mesmos arquivos nos cinco.
- Cortes duros entre todos os takes, com peso só no corte do gancho para o V06.
- Cortar o silêncio inicial de cada clipe para a fala começar imediatamente.
- Legenda karaokê palavra a palavra com destaque amarelo na altura do peito, no estilo do vídeo modelo. **Nunca cobrir a carta nem as mãos.**
- Caixa de gancho branca no topo, uma por variação: A1 `SCROLL PAST THIS` · A2 `MAN HIDING TWO` · A3 `ASKING WHY THEY` · A4 `TO SHARE THIS` · A5 `SKIP THIS Y'ALL`.
- Gráfico flutuante `222` fixo no canto superior o vídeo inteiro, e `222` isolado na tela no CTA.
- **Nunca publicar duas variações na mesma conta, e NUNCA publicar este pacote na conta que rodar o `trevor_a3_confissao`.** É o mesmo esqueleto.
- Color grading: temp -3, tint +2, saturação -6, exposição -3, contraste +12, highlight -35, shadow +18, fade +6.

## Gates de qualidade

1. Ela é a mesma mulher nos dez clipes, com a mesma pele oliva, os mesmos cachos longos e as mesmas mechas prateadas.
2. **Sem colar em nenhum plano.** Só as duas alianças de prata e o anel de pedra clara. É o diferenciador dela contra a Trevor A3.
3. **O leque de cartas fica aberto na MESA em todos os planos**, e ela ergue só a carta SOULMATE. Nunca o baralho inteiro na mão, que é a gramática da Trevor.
4. A carta SOULMATE tem arte, borda e palavra idênticas às do pacote da Trevor A3.
5. A palavra SOULMATE está legível e é o único texto gerado dentro de qualquer imagem.
6. A bandeira dos EUA aparece visível e em foco em todos os keyframes com cenário. A REF-CARTA é a única sem, de propósito.
7. As três velas aparecem acesas mas **não iluminam o ambiente**. A luz da cena é neutra de dia nublado, sem cast quente.
8. A mandala, o crucifixo e a prateleira estão nítidos. Nada foi borrado.
9. Nenhuma legenda ou palavra foi sobreposta na imagem pelo gerador.
10. Mãos com cinco dedos, sem fusão com as cartas, com a peneira nem com o alicate.
11. K02 a K05 saíram todos do K01 original, nunca em cascata.
12. O take do CTA (K07) é o mais fechado do vídeo inteiro.
13. `222` está dito na fala do T4 e isolado na tela no CTA.
14. **O rosto da alma gêmea nunca aparece no vídeo.**
15. Nenhuma leitura de pacto ou feitiço. A carta é clara e o crucifixo carrega o registro.
