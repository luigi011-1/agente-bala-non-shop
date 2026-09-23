# Shelby Turner | Ângulo 3 (Auraly) | Pacote de produção

Vídeo modelo: `C:/Users/luigi/Desktop/APPYON/Robin Matthews/ctv MARK COLLINS - 29.08-3.mp4`, 29,001 s.
Âncora: `C:/Users/luigi/Desktop/APPYON/ShelbyTurner.us .jpeg`.
Funil: vídeo → selo (`222`, like, save, follow) → Stories → link. DM de recuperação.
Status: roteiro e cinco ganchos aprovados. Este pacote contém instruções de geração; imagens e clipes ainda não foram gerados.

## Índice de geração

| Take | Keyframe | Ação de geração |
|---|---|---|
| Prop | REF-CARTA | Reutilizar a arte aprovada se disponível; caso contrário, gerar e fixar uma única referência |
| T1, louro | K01 | GERAR DO ZERO, ÂNCORA SHELBY + REF-CARTA |
| T1, cartas | K02 | EDITAR do K01 original |
| T1, acrílico | K03 | EDITAR do K01 original |
| T1, envelope | K04 | EDITAR do K01 original |
| T1, ampulheta | K05 | EDITAR do K01 original |
| T2, T3, T4 | K06 | GERAR DO ZERO, ÂNCORA SHELBY + REF-CARTA |
| T5, T6 | K07 | EDITAR do K06 original |

**7 keyframes de cena, 10 clipes e 5 montagens.** Há uma referência auxiliar de carta se a já aprovada não estiver disponível. K02–K05 derivam todos do K01, nunca uns dos outros. Cada novo hook custa somente seu K e seu V.

## Trava de identidade e continuidade

Shelby tem 26 anos, pele levemente bronzeada com poros, sardas discretas e pequenas imperfeições naturais, olhos verde-avelã, cabelo longo loiro-mel ondulado, risca central sem franja. Usa blusa canelada creme com mangas recolhidas, corrente fina com cruz pequena de prata e tatuagem de lua no pulso esquerdo. Preservar precisamente a imagem anexada. Mãos naturais, unhas curtas, sem inventar adornos.

Ela está sentada no chão diante da prateleira baixa de caixote. Baralho holográfico empilhado, nunca transformar seu arranjo canônico em fila ou leque. As três cartas comuns de K02 são apenas props temporários da ação. O pote de sal e louro da âncora permanece como detalhe do ambiente, sem ganhar função nova.

Luz neutra difusa de janela à esquerda, dia nublado. Kit em dois grupos: prateleira com cartas, cristais, incenso aceso, vela branca e bandeira dos EUA; parede com mapa astrológico e crucifixo. Mesmo arranjo em todas as imagens, em foco. Os JSON usam as referências para preservar esses detalhes sem reescrever a identidade a cada cena.

## Trava do prop herói

Uma única carta holográfica SOULMATE, aproximadamente 7 por 12 cm, com borda metálica de arco-íris e arte saturada de duas figuras simbólicas, coração, rosas e céu estrelado. As figuras são pequenas ilustrações sem retrato identificável. Não criar ou revelar um rosto de parceiro.

A carta está separada do baralho, mesmo quando pousada à sua frente. Em K04 começa dentro do envelope; a aparição ocorre no clipe. Em K03 começa atrás do acrílico. T2–T6 usam a mesma carta na mão direita. Não gerar o estado final do hook como uma segunda imagem.

Não foi localizado um arquivo de REF-CARTA no workspace pela busca de nomes. Se você já tem a arte aprovada na biblioteca do gerador, reutilize-a. Caso contrário, o prompt abaixo fornece a referência única para este pacote.

## Trava da 2ª pessoa (REF-A)

Não se aplica. Shelby é a única pessoa em cena.

## Gate de composição visual e de realismo

1. Herói e mãos no primeiro plano inferior, mais perto da lente que o rosto.
2. Um único prop ativo por hook. Os demais objetos ficam em posição secundária.
3. Carta inteira e ação legível; folhas com tamanho natural, painel e envelope com dimensões proporcionais. Não há material em montanha neste vídeo.
4. Câmera próxima e frontal na altura do peito.
5. T1 mostra peito para cima e prateleira; T2–T4 fecham mais.
6. T5–T6 são os planos mais fechados. Preservar uma estreita faixa inferior/lateral do kit: ajuste visual para conciliar o CTA próximo com as sete categorias obrigatórias.
7. Cenário reconhecível em dois grupos, preservado da âncora.
8. Recorte reduz o fundo; nenhum blur.
9. Props temporários aparecem somente no hook correspondente. O enquadramento B deixa suas áreas fora de campo.
10. Segunda pessoa ausente.
11. Luz neutra, textura natural e bloco completo de realismo em todos os JSON.
12. A imagem congela antes da ação, inclusive a aba fechada do envelope e a ampulheta deitada.

## REF-CARTA · GERAR DO ZERO SE NECESSÁRIO · SEM ANEXOS

Carta isolada; gerar apenas se a referência aprovada não estiver disponível.

```json
{
  "task": "Generate a single physical tarot card on a plain neutral gray surface.",
  "prop": "A portrait-orientation tarot card, 7 by 12 centimeters, all four corners visible. Reflective rainbow metallic foil border, rich saturated celestial blue and rose colors, two small symbolic illustrated figures facing each other beneath a heart, roses and stars. The small figures have no recognizable facial features. The physical printed title SOULMATE is crisp along the bottom edge. Photographic paper and foil texture, not a digital screen.",
  "lighting": "Neutral diffuse daylight with realistic metallic reflections.",
  "realism": "UGC realism, real skin texture with visible pores, individual hair strands, subtle wrinkles, realistic shadows and reflections, iPhone-footage look, phone camera look not professional photography, no AI polish, no beauty smoothing, no blur anywhere, everything in sharp focus including background walls furniture and details.",
  "aspect_ratio": "9:16",
  "negative": "no captions, no subtitles, no watermark, no extra cards, no hands, no people, no blur"
}
```

## K01 · T1 · FOLHAS DE LOURO · GERAR DO ZERO · ÂNCORA SHELBY + REF-CARTA

Anexar a âncora Shelby e REF-CARTA. Congelar o estado anterior à ação.

```json
{
  "task": "Generate the initial frame using the attached identity and card references.",
  "reference_use": "Use the Shelby anchor for exact identity, clothing, room and lighting. Use REF-CARTA for exact card artwork.",
  "scene": "The same lived-in room as the Shelby reference, with neutral overcast daylight from the left window. Two recognizable groups: the low wooden crate shelf with the stacked holographic tarot deck, clear and rose quartz, a burning incense stick with a fine smoke trail, a white pillar candle and a small United States flag on its stand; the wall with the navy zodiac wheel and the wooden crucifix. Preserve their relative positions. The flag and the two wall anchors remain visible and sharp.",
  "composition": "Single continuous vertical frame, Shelby seated on the floor, chest-up behind the low crate shelf spanning the lower third. Her face is large, her hands and the active prop are closer to the lens than her face. Keep the whole action area visible. No separate insert.",
  "state": "Three separate dry bay leaves sit beside the isolated face-up SOULMATE card on the lower foreground of the crate shelf. Her left fingertips touch the nearest leaf, ready to slide it. Her right hand rests beside the card. Leaves are separate, with no closed shape.",
  "camera": "Chest-height camera, close and straight-on.",
  "lighting": "Soft neutral overcast daylight from the window on the left.",
  "realism": "UGC realism, real skin texture with visible pores, individual hair strands, subtle wrinkles, realistic shadows and reflections, iPhone-footage look, phone camera look not professional photography, no AI polish, no beauty smoothing, no blur anywhere, everything in sharp focus including background walls furniture and details.",
  "aspect_ratio": "9:16",
  "negative": "no captions, no subtitles, no words overlaid on the image, no watermark, no plastic skin, no beauty smoothing, no extra fingers, no fused hands, no blur, no warm orange color cast, no yellow tint, no golden glow, no supernatural lighting, no second person, no phone, no studio lighting"
}
```

## K02 · T1 · CARTAS VARRIDAS · EDITAR do K01 · K01 ORIGINAL

Anexar somente K01 aprovado. Congelar o estado anterior à ação.

```json
{
  "task": "Edit the attached original K01 into this complete initial scene.",
  "reference_use": "Preserve the attached K01 woman's identity, clothing, room, lighting, lens position and hero card artwork. The active hook props are exactly those described in state; keep the canonical background kit.",
  "scene": "The same lived-in room as the Shelby reference, with neutral overcast daylight from the left window. Two recognizable groups: the low wooden crate shelf with the stacked holographic tarot deck, clear and rose quartz, a burning incense stick with a fine smoke trail, a white pillar candle and a small United States flag on its stand; the wall with the navy zodiac wheel and the wooden crucifix. Preserve their relative positions. The flag and the two wall anchors remain visible and sharp.",
  "composition": "Single continuous vertical frame, Shelby seated on the floor, chest-up behind the low crate shelf spanning the lower third. Her face is large, her hands and the active prop are closer to the lens than her face. Keep the whole action area visible. No separate insert.",
  "state": "Three ordinary white-bordered cards are loosely overlapped near the front left edge of the crate shelf, away from the separately placed face-up SOULMATE card at center right. Her left hand is touching the ordinary cards before a sweep. Her right hand rests beside the hero card. The canonical stacked holographic deck stays farther back. No loose bay leaves in the active foreground.",
  "camera": "Chest-height camera, close and straight-on.",
  "lighting": "Soft neutral overcast daylight from the window on the left.",
  "realism": "UGC realism, real skin texture with visible pores, individual hair strands, subtle wrinkles, realistic shadows and reflections, iPhone-footage look, phone camera look not professional photography, no AI polish, no beauty smoothing, no blur anywhere, everything in sharp focus including background walls furniture and details.",
  "aspect_ratio": "9:16",
  "negative": "no captions, no subtitles, no words overlaid on the image, no watermark, no plastic skin, no beauty smoothing, no extra fingers, no fused hands, no blur, no warm orange color cast, no yellow tint, no golden glow, no supernatural lighting, no second person, no phone, no studio lighting"
}
```

## K03 · T1 · ACRÍLICO LEITOSO · EDITAR do K01 · K01 ORIGINAL

Anexar somente K01 aprovado. Congelar o estado anterior à ação.

```json
{
  "task": "Edit the attached original K01 into this complete initial scene.",
  "reference_use": "Preserve the attached K01 woman's identity, clothing, room, lighting, lens position and hero card artwork. The active hook props are exactly those described in state; keep the canonical background kit.",
  "scene": "The same lived-in room as the Shelby reference, with neutral overcast daylight from the left window. Two recognizable groups: the low wooden crate shelf with the stacked holographic tarot deck, clear and rose quartz, a burning incense stick with a fine smoke trail, a white pillar candle and a small United States flag on its stand; the wall with the navy zodiac wheel and the wooden crucifix. Preserve their relative positions. The flag and the two wall anchors remain visible and sharp.",
  "composition": "Single continuous vertical frame, Shelby seated on the floor, chest-up behind the low crate shelf spanning the lower third. Her face is large, her hands and the active prop are closer to the lens than her face. Keep the whole action area visible. No separate insert.",
  "state": "A small upright milky acrylic panel, approximately 12 by 18 centimeters, stands at the front of the crate shelf on two discreet feet. The SOULMATE card is behind it, physically occluded except for its right edge. Her right fingers hold that exposed edge, ready to slide the card to the right. The panel stays below her neckline. No loose bay leaves in the active foreground.",
  "camera": "Chest-height camera, close and straight-on.",
  "lighting": "Soft neutral overcast daylight from the window on the left.",
  "realism": "UGC realism, real skin texture with visible pores, individual hair strands, subtle wrinkles, realistic shadows and reflections, iPhone-footage look, phone camera look not professional photography, no AI polish, no beauty smoothing, no blur anywhere, everything in sharp focus including background walls furniture and details.",
  "aspect_ratio": "9:16",
  "negative": "no captions, no subtitles, no words overlaid on the image, no watermark, no plastic skin, no beauty smoothing, no extra fingers, no fused hands, no blur, no warm orange color cast, no yellow tint, no golden glow, no supernatural lighting, no second person, no phone, no studio lighting"
}
```

## K04 · T1 · ENVELOPE · EDITAR do K01 · K01 ORIGINAL

Anexar somente K01 aprovado. Congelar o estado anterior à ação.

```json
{
  "task": "Edit the attached original K01 into this complete initial scene.",
  "reference_use": "Preserve the attached K01 woman's identity, clothing, room, lighting, lens position and hero card artwork. The active hook props are exactly those described in state; keep the canonical background kit.",
  "scene": "The same lived-in room as the Shelby reference, with neutral overcast daylight from the left window. Two recognizable groups: the low wooden crate shelf with the stacked holographic tarot deck, clear and rose quartz, a burning incense stick with a fine smoke trail, a white pillar candle and a small United States flag on its stand; the wall with the navy zodiac wheel and the wooden crucifix. Preserve their relative positions. The flag and the two wall anchors remain visible and sharp.",
  "composition": "Single continuous vertical frame, Shelby seated on the floor, chest-up behind the low crate shelf spanning the lower third. Her face is large, her hands and the active prop are closer to the lens than her face. Keep the whole action area visible. No separate insert.",
  "state": "A plain ivory envelope sized to fit the hero card lies low in the foreground. Its paper flap is still closed but unsealed, with her left thumb under its edge. The SOULMATE card is inside, wholly concealed. Her right hand supports the envelope at the opening. The canonical stacked deck sits farther back. No loose bay leaves in the active foreground.",
  "camera": "Chest-height camera, close and straight-on.",
  "lighting": "Soft neutral overcast daylight from the window on the left.",
  "realism": "UGC realism, real skin texture with visible pores, individual hair strands, subtle wrinkles, realistic shadows and reflections, iPhone-footage look, phone camera look not professional photography, no AI polish, no beauty smoothing, no blur anywhere, everything in sharp focus including background walls furniture and details.",
  "aspect_ratio": "9:16",
  "negative": "no captions, no subtitles, no words overlaid on the image, no watermark, no plastic skin, no beauty smoothing, no extra fingers, no fused hands, no blur, no warm orange color cast, no yellow tint, no golden glow, no supernatural lighting, no second person, no phone, no studio lighting"
}
```

## K05 · T1 · AMPULHETA · EDITAR do K01 · K01 ORIGINAL

Anexar somente K01 aprovado. Congelar o estado anterior à ação.

```json
{
  "task": "Edit the attached original K01 into this complete initial scene.",
  "reference_use": "Preserve the attached K01 woman's identity, clothing, room, lighting, lens position and hero card artwork. The active hook props are exactly those described in state; keep the canonical background kit.",
  "scene": "The same lived-in room as the Shelby reference, with neutral overcast daylight from the left window. Two recognizable groups: the low wooden crate shelf with the stacked holographic tarot deck, clear and rose quartz, a burning incense stick with a fine smoke trail, a white pillar candle and a small United States flag on its stand; the wall with the navy zodiac wheel and the wooden crucifix. Preserve their relative positions. The flag and the two wall anchors remain visible and sharp.",
  "composition": "Single continuous vertical frame, Shelby seated on the floor, chest-up behind the low crate shelf spanning the lower third. Her face is large, her hands and the active prop are closer to the lens than her face. Keep the whole action area visible. No separate insert.",
  "state": "A small wooden hourglass lies horizontally beside the isolated face-up SOULMATE card on the crate shelf. Her right hand loosely grips the hourglass before lifting it; her left index rests beside the card's lower edge without covering the title. Sand is inside the hourglass only. No loose bay leaves in the active foreground.",
  "camera": "Chest-height camera, close and straight-on.",
  "lighting": "Soft neutral overcast daylight from the window on the left.",
  "realism": "UGC realism, real skin texture with visible pores, individual hair strands, subtle wrinkles, realistic shadows and reflections, iPhone-footage look, phone camera look not professional photography, no AI polish, no beauty smoothing, no blur anywhere, everything in sharp focus including background walls furniture and details.",
  "aspect_ratio": "9:16",
  "negative": "no captions, no subtitles, no words overlaid on the image, no watermark, no plastic skin, no beauty smoothing, no extra fingers, no fused hands, no blur, no warm orange color cast, no yellow tint, no golden glow, no supernatural lighting, no second person, no phone, no studio lighting"
}
```

## K06 · T2, T3, T4 · GERAR DO ZERO · ÂNCORA SHELBY + REF-CARTA

Anexar a âncora Shelby e REF-CARTA. Carta já erguida na mão direita.

```json
{
  "task": "Generate the initial frame for the shared talking setup.",
  "reference_use": "Use the attached Shelby image for exact identity, clothes and room, and REF-CARTA for the exact hero card.",
  "scene": "The same lived-in room as the Shelby reference, with neutral overcast daylight from the left window. Two recognizable groups: the low wooden crate shelf with the stacked holographic tarot deck, clear and rose quartz, a burning incense stick with a fine smoke trail, a white pillar candle and a small United States flag on its stand; the wall with the navy zodiac wheel and the wooden crucifix. Preserve their relative positions. The flag and the two wall anchors remain visible and sharp.",
  "composition": "Closer chest-up view than the hook. Shelby's face fills the upper center. Her right hand holds the complete SOULMATE card in front of her upper chest, closer to the lens than her face, without covering her mouth or silver cross. A narrow edge of the low crate shelf and the two background groups remain visible. Hook prop areas are outside this framing.",
  "state": "Shelby looks directly at the lens, card already raised in her right hand. Her left hand rests low and relaxed before gesturing.",
  "camera": "Chest-height camera, straight-on, pushed closer than setup A.",
  "lighting": "Neutral diffuse overcast daylight from the left window.",
  "realism": "UGC realism, real skin texture with visible pores, individual hair strands, subtle wrinkles, realistic shadows and reflections, iPhone-footage look, phone camera look not professional photography, no AI polish, no beauty smoothing, no blur anywhere, everything in sharp focus including background walls furniture and details.",
  "aspect_ratio": "9:16",
  "negative": "no captions, no subtitles, no words overlaid on the image, no watermark, no plastic skin, no beauty smoothing, no extra fingers, no fused hands, no blur, no warm orange color cast, no yellow tint, no golden glow, no supernatural lighting, no second person, no phone, no studio lighting"
}
```

## K07 · T5, T6 · EDITAR do K06 · K06 ORIGINAL

Anexar somente K06 aprovado. CTA mais próximo, com carta abaixo do rosto e indicador livre.

```json
{
  "task": "Edit the attached K06 to the tightest CTA framing.",
  "reference_use": "Preserve the exact attached woman's identity, outfit, silver cross, left wrist marking, hero card artwork and room arrangement.",
  "scene": "The same lived-in room as the Shelby reference, with neutral overcast daylight from the left window. Two recognizable groups: the low wooden crate shelf with the stacked holographic tarot deck, clear and rose quartz, a burning incense stick with a fine smoke trail, a white pillar candle and a small United States flag on its stand; the wall with the navy zodiac wheel and the wooden crucifix. Preserve their relative positions. The flag and the two wall anchors remain visible and sharp.",
  "composition": "The tightest framing of the video, from upper chest to top of head, with her face large. A minimal lower and right-side margin preserves recognizable portions of the crate shelf kit, including crystals, smoking incense, white candle, tarot deck and United States flag. The navy zodiac wheel and wooden crucifix remain visible behind her. The complete SOULMATE card is in the lower foreground, closer than her face, without covering mouth or necklace.",
  "state": "Her right hand holds the card upright just below chin level. Her left index enters from the lower left, ready to point; shoulders and expression remain relaxed.",
  "camera": "Straight-on camera, closer than K06.",
  "lighting": "Unchanged neutral overcast window daylight.",
  "realism": "UGC realism, real skin texture with visible pores, individual hair strands, subtle wrinkles, realistic shadows and reflections, iPhone-footage look, phone camera look not professional photography, no AI polish, no beauty smoothing, no blur anywhere, everything in sharp focus including background walls furniture and details.",
  "aspect_ratio": "9:16",
  "negative": "no captions, no subtitles, no words overlaid on the image, no watermark, no plastic skin, no beauty smoothing, no extra fingers, no fused hands, no blur, no warm orange color cast, no yellow tint, no golden glow, no supernatural lighting, no second person, no phone, no studio lighting"
}
```

## Bloco global de vídeo

Modelo de produção previsto: Veo via Flow, imagem inicial aprovada. O texto global já está incorporado nos dez prompts abaixo, que podem ser copiados integralmente.

Preservar a identidade da Shelby e o cenário do frame inicial, com textura natural, cruz de prata, roupa creme, tatuagem no pulso esquerdo e carta idêntica. A bandeira, o mapa astrológico e o crucifixo permanecem estáveis. Estilo UGC, sem legendas geradas, sem música e sem pessoas extras.

Voz: mulher americana adulta, íntima, firme e dinâmica, com surpresa contida no hook. A fala começa imediatamente. Gerar o clipe completo, preservar a última palavra e ajustar apenas os silêncios na montagem. A duração final será medida após a geração; 29 s é alvo editorial, não resultado já obtido.

### V01 · T1 · usa K01 · Folhas de louro

Anexar K01 aprovado como frame inicial.

```text
a avatar (mulher) fala em inglês com sotaque americano de mulher de vinte e seis anos, voz autêntica, íntima, dinâmica e firme, a seguinte frase: "What the fuck have you been manifesting? You weren't meant to stop here today, but you did."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Ela desliza as três folhas de louro, uma após a outra, formando uma linha aberta que termina junto à carta. Olha para a lente enquanto fala. Preservar a identidade da Shelby e o cenário do frame inicial, com textura natural, cruz de prata, roupa creme, tatuagem no pulso esquerdo e carta idêntica. A bandeira, o mapa astrológico e o crucifixo permanecem estáveis. Estilo UGC, sem legendas geradas, sem música e sem pessoas extras.

câmera: fixa

som ambiente: quarto residencial silencioso durante o dia, ruídos discretos do movimento dos objetos, sem música
```

### V02 · T1 · usa K02 · Cartas varridas

Anexar K02 aprovado como frame inicial.

```text
a avatar (mulher) fala em inglês com sotaque americano de mulher de vinte e seis anos, voz autêntica, íntima, dinâmica e firme, a seguinte frase: "What the fuck have you been manifesting? You weren't meant to stop here today, but you did."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Ela varre as três cartas comuns pela borda inferior esquerda. A carta SOULMATE permanece parada e inteira; o baralho empilhado fica intacto. Preservar a identidade da Shelby e o cenário do frame inicial, com textura natural, cruz de prata, roupa creme, tatuagem no pulso esquerdo e carta idêntica. A bandeira, o mapa astrológico e o crucifixo permanecem estáveis. Estilo UGC, sem legendas geradas, sem música e sem pessoas extras.

câmera: fixa

som ambiente: quarto residencial silencioso durante o dia, ruídos discretos do movimento dos objetos, sem música
```

### V03 · T1 · usa K03 · Acrílico leitoso

Anexar K03 aprovado como frame inicial.

```text
a avatar (mulher) fala em inglês com sotaque americano de mulher de vinte e seis anos, voz autêntica, íntima, dinâmica e firme, a seguinte frase: "What the fuck have you been manifesting? You weren't meant to stop here today, but you did."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Ela puxa a carta para a direita, de trás do acrílico, até a arte aparecer inteira. A placa permanece parada enquanto ela fala. Preservar a identidade da Shelby e o cenário do frame inicial, com textura natural, cruz de prata, roupa creme, tatuagem no pulso esquerdo e carta idêntica. A bandeira, o mapa astrológico e o crucifixo permanecem estáveis. Estilo UGC, sem legendas geradas, sem música e sem pessoas extras.

câmera: fixa

som ambiente: quarto residencial silencioso durante o dia, ruídos discretos do movimento dos objetos, sem música
```

### V04 · T1 · usa K04 · Envelope

Anexar K04 aprovado como frame inicial.

```text
a avatar (mulher) fala em inglês com sotaque americano de mulher de vinte e seis anos, voz autêntica, íntima, dinâmica e firme, a seguinte frase: "What the fuck have you been manifesting? You weren't meant to stop here today, but you did."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Ela abre a aba do envelope com o polegar, inclina o envelope e retira a carta com a mão direita. No final, levanta a carta em direção à lente. Preservar a identidade da Shelby e o cenário do frame inicial, com textura natural, cruz de prata, roupa creme, tatuagem no pulso esquerdo e carta idêntica. A bandeira, o mapa astrológico e o crucifixo permanecem estáveis. Estilo UGC, sem legendas geradas, sem música e sem pessoas extras.

câmera: fixa

som ambiente: quarto residencial silencioso durante o dia, ruídos discretos do movimento dos objetos, sem música
```

### V05 · T1 · usa K05 · Ampulheta

Anexar K05 aprovado como frame inicial.

```text
a avatar (mulher) fala em inglês com sotaque americano de mulher de vinte e seis anos, voz autêntica, íntima, dinâmica e firme, a seguinte frase: "What the fuck have you been manifesting? You weren't meant to stop here today, but you did."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Ela levanta e vira a ampulheta, apoiando-a em pé. A areia começa a cair dentro do vidro; o indicador esquerdo toca de leve a borda inferior da carta. Preservar a identidade da Shelby e o cenário do frame inicial, com textura natural, cruz de prata, roupa creme, tatuagem no pulso esquerdo e carta idêntica. A bandeira, o mapa astrológico e o crucifixo permanecem estáveis. Estilo UGC, sem legendas geradas, sem música e sem pessoas extras.

câmera: fixa

som ambiente: quarto residencial silencioso durante o dia, ruídos discretos do movimento dos objetos, sem música
```

### V06 · T2 · usa K06

Anexar K06 aprovado como frame inicial.

```text
a avatar (mulher) fala em inglês com sotaque americano de mulher de vinte e seis anos, voz autêntica, íntima, dinâmica e firme, a seguinte frase: "Someone's about to confess something to you. It is the person who appeared in your mind just now."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Ela mantém a carta erguida e inclina a cabeça discretamente ao falar da pessoa que veio à mente. Sustenta o olhar na lente. Preservar a identidade da Shelby e o cenário do frame inicial, com textura natural, cruz de prata, roupa creme, tatuagem no pulso esquerdo e carta idêntica. A bandeira, o mapa astrológico e o crucifixo permanecem estáveis. Estilo UGC, sem legendas geradas, sem música e sem pessoas extras.

câmera: leve push-in

som ambiente: quarto residencial silencioso durante o dia, ruídos discretos do movimento dos objetos, sem música
```

### V07 · T3 · usa K06

Anexar K06 aprovado como frame inicial.

```text
a avatar (mulher) fala em inglês com sotaque americano de mulher de vinte e seis anos, voz autêntica, íntima, dinâmica e firme, a seguinte frase: "They have been holding it inside longer than you know. In the next twenty four hours, they stop holding it in."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Ela faz um gesto curto com a mão esquerda ao mencionar vinte e quatro horas. A carta permanece firme na mão direita. Preservar a identidade da Shelby e o cenário do frame inicial, com textura natural, cruz de prata, roupa creme, tatuagem no pulso esquerdo e carta idêntica. A bandeira, o mapa astrológico e o crucifixo permanecem estáveis. Estilo UGC, sem legendas geradas, sem música e sem pessoas extras.

câmera: leve push-in

som ambiente: quarto residencial silencioso durante o dia, ruídos discretos do movimento dos objetos, sem música
```

### V08 · T4 · usa K06

Anexar K06 aprovado como frame inicial.

```text
a avatar (mulher) fala em inglês com sotaque americano de mulher de vinte e seis anos, voz autêntica, íntima, dinâmica e firme, a seguinte frase: "Comment two two two. That is how this gets written next to your name. Like it and save it, so the blessing coming toward you stays strong."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Ela aponta para baixo ao dizer two two two e abre a mão esquerda ao pedir like e save. Mantém a carta erguida. Preservar a identidade da Shelby e o cenário do frame inicial, com textura natural, cruz de prata, roupa creme, tatuagem no pulso esquerdo e carta idêntica. A bandeira, o mapa astrológico e o crucifixo permanecem estáveis. Estilo UGC, sem legendas geradas, sem música e sem pessoas extras.

câmera: leve push-in

som ambiente: quarto residencial silencioso durante o dia, ruídos discretos do movimento dos objetos, sem música
```

### V09 · T5 · usa K07

Anexar K07 aprovado como frame inicial.

```text
a avatar (mulher) fala em inglês com sotaque americano de mulher de vinte e seis anos, voz autêntica, íntima, dinâmica e firme, a seguinte frase: "Follow me so this stays open, then tap my picture and watch my stories. Their face is waiting there, and it disappears tonight."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Ela faz um gesto breve em direção ao espectador e depois aponta para cima ao mencionar a foto de perfil. A carta continua inteira na mão direita. Preservar a identidade da Shelby e o cenário do frame inicial, com textura natural, cruz de prata, roupa creme, tatuagem no pulso esquerdo e carta idêntica. A bandeira, o mapa astrológico e o crucifixo permanecem estáveis. Estilo UGC, sem legendas geradas, sem música e sem pessoas extras.

câmera: leve push-in

som ambiente: quarto residencial silencioso durante o dia, ruídos discretos do movimento dos objetos, sem música
```

### V10 · T6 · usa K07

Anexar K07 aprovado como frame inicial.

```text
a avatar (mulher) fala em inglês com sotaque americano de mulher de vinte e seis anos, voz autêntica, íntima, dinâmica e firme, a seguinte frase: "Do it now. If you scroll past this, you close it, and somebody else finds out what was meant to be yours."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Ela aponta uma vez ao dizer Do it now. No final, aproxima a carta da lente sem cobrir a boca antes da última palavra. Preservar a identidade da Shelby e o cenário do frame inicial, com textura natural, cruz de prata, roupa creme, tatuagem no pulso esquerdo e carta idêntica. A bandeira, o mapa astrológico e o crucifixo permanecem estáveis. Estilo UGC, sem legendas geradas, sem música e sem pessoas extras.

câmera: leve push-in

som ambiente: quarto residencial silencioso durante o dia, ruídos discretos do movimento dos objetos, sem música
```

## Mapa de âncoras

| Keyframe | Referências a anexar | Modelo previsto |
|---|---|---|
| REF-CARTA | Sem anexos, se necessária | Nano Banana 2 |
| K01 | ÂNCORA SHELBY + REF-CARTA | Nano Banana Pro |
| K02, K03, K04, K05 | K01 original aprovado | Nano Banana 2, edição |
| K06 | ÂNCORA SHELBY + REF-CARTA | Nano Banana 2 |
| K07 | K06 original aprovado | Nano Banana 2, edição |

Aprovar visualmente K01 antes de suas quatro edições. Os modelos são os do workflow local; nenhuma geração remota foi enviada neste trabalho.

## Montagem no CapCut

Timeline vertical 1080 × 1920, 30 fps. Fazer cinco exportações:

| Exportação | Sequência de clipes | Texto do hook, somente na edição |
|---|---|---|
| shelby_confissao_louro.mp4 | V01 + V06 + V07 + V08 + V09 + V10 | IT'S LEADING TO ONE NAME |
| shelby_confissao_cartas.mp4 | V02 + V06 + V07 + V08 + V09 + V10 | DON'T SCROLL |
| shelby_confissao_acrilico.mp4 | V03 + V06 + V07 + V08 + V09 + V10 | THIS FOUND YOU |
| shelby_confissao_envelope.mp4 | V04 + V06 + V07 + V08 + V09 + V10 | WHAT THE FUCK HAVE YOU BEEN MANIFESTING? |
| shelby_confissao_ampulheta.mp4 | V05 + V06 + V07 + V08 + V09 + V10 | THE NEXT 24 HOURS |

Retirar silêncio no início e no fim dos clipes. A copy tem 128 palavras. Alvo de 29 s exige cerca de 4,41 palavras/s; conferir inteligibilidade antes de acelerar. Se a fala não couber com naturalidade, preservar as palavras aprovadas e registrar a duração real, sem cortar sílabas ou inventar filler.

K01, K02 e K05 terminam com carta pousada: corte editorial para a carta já erguida em V06. K03 e K04 podem encerrar com a carta subindo. Essa emenda é uma adaptação da geração por takes; o modelo original ergue a carta em movimento contínuo.

Legendas brancas grandes com destaque palavra a palavra, sem encobrir carta, mãos ou boca. Texto de hook apenas no T1. Gráfico `222` discreto no canto superior e `222` isolado no V08. V09 traz fala, legenda fixa `The reveal is in my stories` e seta vermelha para a posição real da foto de perfil na plataforma de publicação. Ajustar a seta à interface; não presumir que IG e FB usam a mesma posição. Sem celular como prop.

T5 e T6 recebem os punch-ins mais fortes, e a carta se aproxima no final. Preservar luz neutra; correção de cor deve depender do material gerado, sem aplicar receita fixa de temperatura ou exposição.

Stories e recuperação estão em `DM.md`. Preparar o destino antes de publicar. O cronograma precisa sustentar a expressão aprovada `tonight`; a mera duração de um Story não garante que ele expire à noite. O roteiro contém previsão de confissão e consequência espiritual: são elementos narrativos, não fatos verificados sobre quem assiste.

## Gates de qualidade

1. Conferir Shelby, roupa, cruz e tatuagem contra a âncora.
2. Kit A3 reconhecível em todos os keyframes; bandeira em foco.
3. A mesma carta em todos os clipes, título físico legível, nenhuma legenda gerada.
4. Mãos naturais, carta sem deformação, louro em caminho aberto e ampulheta contendo a areia.
5. Envelope e acrílico começam ocultando a carta; reveal acontece no vídeo.
6. Baralho canônico empilhado intacto. As cartas comuns do hook 2 saem sem arrastar a SOULMATE.
7. K02–K05 derivados diretamente de K01; K07 diretamente de K06.
8. Todas as falas idênticas ao roteiro e última palavra inteira.
9. V08 pede 222 antes de V09 mandar aos Stories.
10. CTA mais fechado, três camadas de orientação na edição.
11. Nenhum rosto de parceiro em vídeo ou Stories.
12. Duração, sincronismo e emendas só podem ser aprovados após os clipes existirem.
13. Publicação não executada. Registrar rota e biblioteca como pacote preparado, sem marcar como publicado.

## Tabela final bilíngue

Esta é a versão de referência que substitui as propostas anteriores. A fala aprovada foi preservada.

| # | Beat | K | English | Português |
|---|---|---|---|---|
| T1 | Hook | K01–K05 | What the fuck have you been manifesting? You weren't meant to stop here today, but you did. | Que porra você anda manifestando? Você não deveria ter parado aqui hoje, mas parou. |
| T2 | Promessa | K06 | Someone's about to confess something to you. It is the person who appeared in your mind just now. | Alguém está prestes a confessar algo para você. É a pessoa que apareceu na sua mente agora mesmo. |
| T3 | Prazo | K06 | They have been holding it inside longer than you know. In the next twenty four hours, they stop holding it in. | Essa pessoa vem guardando isso há mais tempo do que você imagina. Nas próximas vinte e quatro horas, vai parar de guardar. |
| T4 | Selo | K06 | Comment two two two. That is how this gets written next to your name. Like it and save it, so the blessing coming toward you stays strong. | Comente dois dois dois. É assim que isso fica escrito ao lado do seu nome. Curta e salve, para que a bênção que vem em sua direção continue forte. |
| T5 | Stories | K07 | Follow me so this stays open, then tap my picture and watch my stories. Their face is waiting there, and it disappears tonight. | Siga-me para manter isso aberto, depois toque na minha foto e veja meus Stories. O rosto dessa pessoa está esperando lá e desaparece esta noite. |
| T6 | Fecho | K07 | Do it now. If you scroll past this, you close it, and somebody else finds out what was meant to be yours. | Faça isso agora. Se passar por este vídeo, você fecha isso, e outra pessoa descobre o que era para ser seu. |

## Roteiro final em inglês, numerado por take

**T1**

What the fuck have you been manifesting? You weren't meant to stop here today, but you did.

**T2**

Someone's about to confess something to you. It is the person who appeared in your mind just now.

**T3**

They have been holding it inside longer than you know. In the next twenty four hours, they stop holding it in.

**T4**

Comment two two two. That is how this gets written next to your name. Like it and save it, so the blessing coming toward you stays strong.

**T5**

Follow me so this stays open, then tap my picture and watch my stories. Their face is waiting there, and it disappears tonight.

**T6**

Do it now. If you scroll past this, you close it, and somebody else finds out what was meant to be yours.

## Roteiro final em inglês, corrido só-fala

What the fuck have you been manifesting? You weren't meant to stop here today, but you did.

Someone's about to confess something to you. It is the person who appeared in your mind just now.

They have been holding it inside longer than you know. In the next twenty four hours, they stop holding it in.

Comment two two two. That is how this gets written next to your name. Like it and save it, so the blessing coming toward you stays strong.

Follow me so this stays open, then tap my picture and watch my stories. Their face is waiting there, and it disappears tonight.

Do it now. If you scroll past this, you close it, and somebody else finds out what was meant to be yours.

