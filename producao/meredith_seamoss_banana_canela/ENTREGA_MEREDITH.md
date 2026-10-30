# ENTREGA | Meredith Callahan | Sea Moss Venda · Banana com canela e vitamina → Natural Rems Sea Moss

flow_seguro: v1

Produção `meredith_seamoss_banana_canela` · Ângulo 1 Sea Moss (conta da Meredith) · VENDA · rodada de VALIDAÇÃO · formato mínimo de prompt do Flow

## 0. INSTRUÇÕES PARA A MEMÓRIA DO AGENTE · GOOGLE FLOW (colar inteiro antes do primeiro K)

```text
# Agente do Flow, produção atual: Sea Moss Venda · Banana com canela e vitamina → Natural Rems Sea Moss

Você é o executor do Google Flow. Você só gera imagens e vídeos a partir de prompts prontos. Você não cria, não edita e não melhora prompt.

## Produção atual
- Conta: Natural Rems Sea Moss (Meredith), vídeo de venda. Sea Moss Venda · Banana com canela e vitamina → Natural Rems Sea Moss.
- Um avatar só: a senhora de turbante verde e amarelo, blusa creme e avental laranja (arquivo `meredith callahan .png`). Imagens K01 a K09; vídeos V01 a V16.

## O que é anexado (só isto, nada mais)
- IMAGEM (K): anexe só a imagem da avatar e cole o prompt.
- EXCEÇÃO K09: anexe `meredith callahan .png` e `natural_rems_seamoss_produto.jpg` (nesta ordem).
- VÍDEO (V): anexe só a imagem que o operador escolheu do K indicado e cole o prompt de vídeo.
- Não existe frame modelo. Segunda imagem só quando uma EXCEÇÃO acima pedir. Cenário, pose, câmera e objeto já estão escritos em cada prompt. Pare só se faltar a imagem da avatar (K que pede a avatar) ou a imagem escolhida (V).

## Imagens (K01 a K09)
1. Modelo: Nano Banana 2.1. Formato: 9:16 vertical.
2. Gere 4 variações por prompt. Confira o 4 e o 9:16 antes de CADA K, porque a tela volta sozinha para 1.
3. Cole o parágrafo inteiro, sem o código K, sem resumir, sem alterar uma palavra.
4. Nomeie as quatro: `K01-1`, `K01-2`, `K01-3`, `K01-4`.
5. Se saírem menos de 4, ou formato diferente de 9:16, gere de novo com o MESMO prompt e a MESMA imagem até existirem 4 em 9:16.
6. Gere todos os K e PARE. Avise: "K01 a K09 prontos, 4 por K. Aguardando sua escolha." Não escolha, não apague e não gere vídeo.
7. O operador apaga 3 de cada K e deixa 1 escolhida a dedo. Nunca questione e nunca recrie uma imagem apagada.

## Vídeos (V01 a V16)
1. Só começa quando o operador mandar. Mapa: V01 usa K01; V02 usa K02; V03 usa K03; V04 usa K04; V05 usa K05; V06 usa K06; V07 a V08 usam todos a mesma imagem escolhida do K07; V09 a V11 usam todos a mesma imagem escolhida do K08; V12 a V16 usam todos a mesma imagem escolhida do K09. Se o K tiver mais de uma imagem ou nenhuma, pare e pergunte qual.
2. Modelo: Omni 1.1 Flash (use só esse). Duração: 8 segundos. Formato: 9:16. A imagem entra como imagem inicial.
3. Gere 1 variação por V. Confira o 1 antes de cada V.
4. O campo de texto recebe só o prompt V, inteiro, sem alterar uma palavra. O prompt V é curto e começa com `The person in the image`. Se começar com `Match the attached image`, é prompt de imagem: pare e avise.
5. Nomeie cada vídeo com o código do V (`V01`, `V02`...), que é a ordem da montagem.
6. No máximo 7 V por vez. Terminou o lote, relate e espere o operador dizer `prossiga`.

## Falhou, censura ou bloqueio
- Se a geração falhar, cair na censura, der erro ou o prompt for bloqueado: refaça com o MESMO prompt, sem trocar, cortar ou suavizar uma palavra, e tente de novo até aquele item sair.
- Não passe para o próximo item sem avisar qual está pendente: "K03 ainda pendente, tentativas: N."
- Você nunca reescreve prompt. Só o operador altera.
- Se o mesmo item falhar 3 vezes seguidas com "might violate our policies" (ou parecida), continue tentando com o MESMO prompt, mas avise na hora: código, quantas tentativas e a mensagem exata. O operador decide se reescreve.
- Se a interface não permitir 9:16, 4 variações (imagem) ou 1 variação (vídeo), avise antes de mudar qualquer configuração.

## Relatório de status
Depois de cada K ou V, diga: código, resultado (pronto, tentando de novo, pendente) e quantas tentativas. No fim do lote, liste concluídos e pendentes.

## Regras gerais
- Não adicione música, legenda, texto ou tradução.
- A fala do prompt é literal. Não corrija nem complete.
- Em caso de dúvida real (pacote incompleto, código duplicado, anexo faltando), pare e pergunte em uma linha.
```

## Qual vídeo é este

**Vídeo: Banana com canela e vitamina → Natural Rems Sea Moss.**

**O que acontece:** Meredith Callahan, no cenário fixo da conta, faz a receita do modelo cena a cena, mostra o resultado e os benefícios, admite o lado ruim de fazer a receita e passa para o sea moss; a partir do T12 segura o pote do Natural Rems Sea Moss parado e legível até o fim. Fecha com comment yes, Amazon, link na bio, e o lembrete do follow.

**Gancho:** Gancho: ela segura três bananas descascadas colada na lente e despeja canela de um potinho por cima.

## 1. Anexos e mapa

- **Imagem (K):** anexar SÓ o que o título de cada K indica (padrão: a imagem da avatar, `meredith callahan .png`) e colar o prompt. 4 variações, 9:16. Nada de frame do modelo.
- **Vídeo (V):** anexar SÓ a imagem escolhida do K indicado no mapa e colar o prompt de vídeo. 1 variação, 9:16.
- Bloco do agente Flow desta produção: `AGENTE_FLOW.md`.

V01 usa K01; V02 usa K02; V03 usa K03; V04 usa K04; V05 usa K05; V06 usa K06; V07 a V08 usam a mesma imagem escolhida do K07; V09 a V11 usam a mesma imagem escolhida do K08; V12 a V16 usam a mesma imagem escolhida do K09.

```text
MAPA K/V
V01: K01
V02: K02
V03: K03
V04: K04
V05: K05
V06: K06
V07: K07
V08: K07
V09: K08
V10: K08
V11: K08
V12: K09
V13: K09
V14: K09
V15: K09
V16: K09
```

## 2. PROMPTS DE IMAGEM (um bloco por K)

### K01 · anexar SÓ `meredith callahan .png`

Cena: Gancho: ela segura três bananas descascadas colada na lente e despeja canela de um potinho por cima.

```text
K01
Match the attached image exactly for the woman's identity and outfit: a woman around seventy with deep brown skin, dark freckles on her cheekbones, deep laugh lines, gold-capped front teeth, silver-gray locs piled high inside a tall emerald-green and saffron-yellow patterned head wrap, red reading glasses resting on the front of the wrap, large gold bamboo hoop earrings, a stack of thin gold bangles on her left wrist, a loose cream cotton short-sleeve blouse with green leaf embroidery at the neckline, and a rust-orange apron tied at the waist. She stands behind a mint-green speckled Formica kitchen table in her small Brooklyn apartment kitchen: wooden cabinets, a row of large glass jars of pale golden sea moss and a glass blender on the counter at the left, a window at the right showing a red brick building with black iron balconies under an overcast blue-gray sky, and a small American flag in a potted plant on the windowsill, in sharp focus. Hero: she holds three peeled bananas side by side, peels folded down around the base, up toward the camera in her left hand, very close to the lens, large in frame and closer to the camera than her face, their tops already dusted with ground cinnamon. With her right hand she tips a small unlabeled glass spice jar, a stream of reddish-brown cinnamon falling onto the bananas. She looks straight at the camera, caught mid-sentence, lips naturally parted, animated expression. Vertical smartphone shot, 26mm lens, camera at chest height about one meter from the table, level, front facing. Soft neutral even daylight, true neutral colors, real skin texture with visible pores, smartphone footage look, everything in sharp focus, 9:16 vertical.
```

### K02 · anexar SÓ `meredith callahan .png`

Cena: Macro: as três bananas cobertas de canela empurradas quase encostando na lente, rosto dela atrás.

```text
K02
Match the attached image exactly for the woman's identity and outfit: a woman around seventy with deep brown skin, dark freckles on her cheekbones, deep laugh lines, gold-capped front teeth, silver-gray locs piled high inside a tall emerald-green and saffron-yellow patterned head wrap, red reading glasses resting on the front of the wrap, large gold bamboo hoop earrings, a stack of thin gold bangles on her left wrist, a loose cream cotton short-sleeve blouse with green leaf embroidery at the neckline, and a rust-orange apron tied at the waist. She stands behind a mint-green speckled Formica kitchen table in her small Brooklyn apartment kitchen: wooden cabinets, a row of large glass jars of pale golden sea moss and a glass blender on the counter at the left, a window at the right showing a red brick building with black iron balconies under an overcast blue-gray sky, and a small American flag in a potted plant on the windowsill, in sharp focus. Hero: three peeled bananas thickly coated in ground cinnamon pushed right up to the lens, filling the lower two thirds of the frame in extreme close-up, the cinnamon texture crisp; her face is partly visible just behind the banana tips. She looks straight at the camera, caught mid-sentence, lips naturally parted, animated expression. Vertical smartphone shot, 26mm lens, camera at chest height about one meter from the table, level, front facing. Soft neutral even daylight, true neutral colors, real skin texture with visible pores, smartphone footage look, everything in sharp focus, 9:16 vertical.
```

### K03 · anexar SÓ `meredith callahan .png`

Cena: Ela segura uma colher de canela e uma banana sobre o copo vazio do liquidificador; meio limão e copo de água na mesa.

```text
K03
Match the attached image exactly for the woman's identity and outfit: a woman around seventy with deep brown skin, dark freckles on her cheekbones, deep laugh lines, gold-capped front teeth, silver-gray locs piled high inside a tall emerald-green and saffron-yellow patterned head wrap, red reading glasses resting on the front of the wrap, large gold bamboo hoop earrings, a stack of thin gold bangles on her left wrist, a loose cream cotton short-sleeve blouse with green leaf embroidery at the neckline, and a rust-orange apron tied at the waist. She stands behind a mint-green speckled Formica kitchen table in her small Brooklyn apartment kitchen: wooden cabinets, a row of large glass jars of pale golden sea moss and a glass blender on the counter at the left, a window at the right showing a red brick building with black iron balconies under an overcast blue-gray sky, and a small American flag in a potted plant on the windowsill, in sharp focus. Hero: on the mint-green Formica table in the lower foreground, very close to the lens, large in frame and closer to the camera than her face: an empty glass blender jar on its black base, half a lemon and a glass of water beside it. She holds a peeled banana in one hand and a teaspoon of ground cinnamon in the other above the jar. She looks straight at the camera, caught mid-sentence, lips naturally parted, animated expression. Vertical smartphone shot, 26mm lens, camera at chest height about one meter from the table, level, front facing. Soft neutral even daylight, true neutral colors, real skin texture with visible pores, smartphone footage look, everything in sharp focus, 9:16 vertical.
```

### K04 · anexar SÓ `meredith callahan .png`

Cena: Close: banana dentro do copo do liquidificador; ela segura meio limão espremendo por cima.

```text
K04
Match the attached image exactly for the woman's identity and outfit: a woman around seventy with deep brown skin, dark freckles on her cheekbones, deep laugh lines, gold-capped front teeth, silver-gray locs piled high inside a tall emerald-green and saffron-yellow patterned head wrap, red reading glasses resting on the front of the wrap, large gold bamboo hoop earrings, a stack of thin gold bangles on her left wrist, a loose cream cotton short-sleeve blouse with green leaf embroidery at the neckline, and a rust-orange apron tied at the waist. She stands behind a mint-green speckled Formica kitchen table in her small Brooklyn apartment kitchen: wooden cabinets, a row of large glass jars of pale golden sea moss and a glass blender on the counter at the left, a window at the right showing a red brick building with black iron balconies under an overcast blue-gray sky, and a small American flag in a potted plant on the windowsill, in sharp focus. Hero: in the lower foreground, very close to the lens, large in frame and closer to the camera than her face: the glass blender jar with a peeled banana and a dusting of cinnamon inside. She squeezes half a lemon over the jar with her right hand. She looks straight at the camera, caught mid-sentence, lips naturally parted, animated expression. Vertical smartphone shot, 26mm lens, camera at chest height about one meter from the table, level, front facing. Soft neutral even daylight, true neutral colors, real skin texture with visible pores, smartphone footage look, everything in sharp focus, 9:16 vertical.
```

### K05 · anexar SÓ `meredith callahan .png`

Cena: Ela despeja um copo de água no liquidificador com a banana.

```text
K05
Match the attached image exactly for the woman's identity and outfit: a woman around seventy with deep brown skin, dark freckles on her cheekbones, deep laugh lines, gold-capped front teeth, silver-gray locs piled high inside a tall emerald-green and saffron-yellow patterned head wrap, red reading glasses resting on the front of the wrap, large gold bamboo hoop earrings, a stack of thin gold bangles on her left wrist, a loose cream cotton short-sleeve blouse with green leaf embroidery at the neckline, and a rust-orange apron tied at the waist. She stands behind a mint-green speckled Formica kitchen table in her small Brooklyn apartment kitchen: wooden cabinets, a row of large glass jars of pale golden sea moss and a glass blender on the counter at the left, a window at the right showing a red brick building with black iron balconies under an overcast blue-gray sky, and a small American flag in a potted plant on the windowsill, in sharp focus. Hero: in the lower foreground, very close to the lens, large in frame and closer to the camera than her face: the glass blender jar with the banana and cinnamon inside. She pours a glass of water into it. She looks straight at the camera, caught mid-sentence, lips naturally parted, animated expression. Vertical smartphone shot, 26mm lens, camera at chest height about one meter from the table, level, front facing. Soft neutral even daylight, true neutral colors, real skin texture with visible pores, smartphone footage look, everything in sharp focus, 9:16 vertical.
```

### K06 · anexar SÓ `meredith callahan .png`

Cena: Mão dela na tampa do liquidificador batendo, a vitamina bege girando, colado na lente.

```text
K06
Match the attached image exactly for the woman's identity and outfit: a woman around seventy with deep brown skin, dark freckles on her cheekbones, deep laugh lines, gold-capped front teeth, silver-gray locs piled high inside a tall emerald-green and saffron-yellow patterned head wrap, red reading glasses resting on the front of the wrap, large gold bamboo hoop earrings, a stack of thin gold bangles on her left wrist, a loose cream cotton short-sleeve blouse with green leaf embroidery at the neckline, and a rust-orange apron tied at the waist. She stands behind a mint-green speckled Formica kitchen table in her small Brooklyn apartment kitchen: wooden cabinets, a row of large glass jars of pale golden sea moss and a glass blender on the counter at the left, a window at the right showing a red brick building with black iron balconies under an overcast blue-gray sky, and a small American flag in a potted plant on the windowsill, in sharp focus. Hero: in the lower foreground, very close to the lens, large in frame and closer to the camera than her face: the glass blender with its lid on, a creamy beige banana smoothie swirling inside. She presses the lid down with one hand. She looks straight at the camera, caught mid-sentence, lips naturally parted, animated expression. Vertical smartphone shot, 26mm lens, camera at chest height about one meter from the table, level, front facing. Soft neutral even daylight, true neutral colors, real skin texture with visible pores, smartphone footage look, everything in sharp focus, 9:16 vertical.
```

### K07 · anexar SÓ `meredith callahan .png`

Cena: Ela segura o copo alto de vitamina de banana perto da lente; liquidificador atrás.

```text
K07
Match the attached image exactly for the woman's identity and outfit: a woman around seventy with deep brown skin, dark freckles on her cheekbones, deep laugh lines, gold-capped front teeth, silver-gray locs piled high inside a tall emerald-green and saffron-yellow patterned head wrap, red reading glasses resting on the front of the wrap, large gold bamboo hoop earrings, a stack of thin gold bangles on her left wrist, a loose cream cotton short-sleeve blouse with green leaf embroidery at the neckline, and a rust-orange apron tied at the waist. She stands behind a mint-green speckled Formica kitchen table in her small Brooklyn apartment kitchen: wooden cabinets, a row of large glass jars of pale golden sea moss and a glass blender on the counter at the left, a window at the right showing a red brick building with black iron balconies under an overcast blue-gray sky, and a small American flag in a potted plant on the windowsill, in sharp focus. Hero: she holds a tall clear glass of thick beige banana cinnamon smoothie out toward the camera in her right hand, very close to the lens, large in frame and closer to the camera than her face; the half-empty blender stands on the mint-green Formica table behind it. She looks straight at the camera, caught mid-sentence, lips naturally parted, animated expression. Vertical smartphone shot, 26mm lens, camera at chest height about one meter from the table, level, front facing. Soft neutral even daylight, true neutral colors, real skin texture with visible pores, smartphone footage look, everything in sharp focus, 9:16 vertical.
```

### K08 · anexar SÓ `meredith callahan .png`

Cena: Ela sentada num banco junto à mesa, segurando o copo de vitamina perto da lente.

```text
K08
Match the attached image exactly for the woman's identity and outfit: a woman around seventy with deep brown skin, dark freckles on her cheekbones, deep laugh lines, gold-capped front teeth, silver-gray locs piled high inside a tall emerald-green and saffron-yellow patterned head wrap, red reading glasses resting on the front of the wrap, large gold bamboo hoop earrings, a stack of thin gold bangles on her left wrist, a loose cream cotton short-sleeve blouse with green leaf embroidery at the neckline, and a rust-orange apron tied at the waist. She stands behind a mint-green speckled Formica kitchen table in her small Brooklyn apartment kitchen: wooden cabinets, a row of large glass jars of pale golden sea moss and a glass blender on the counter at the left, a window at the right showing a red brick building with black iron balconies under an overcast blue-gray sky, and a small American flag in a potted plant on the windowsill, in sharp focus. Hero: she sits on a wooden stool beside the mint-green Formica table, relaxed, holding the tall glass of beige banana smoothie out toward the camera, very close to the lens, large in frame and closer to the camera than her face. She looks straight at the camera, caught mid-sentence, lips naturally parted, animated expression. Vertical smartphone shot, 26mm lens, camera at chest height about one meter from the table, level, front facing. Soft neutral even daylight, true neutral colors, real skin texture with visible pores, smartphone footage look, everything in sharp focus, 9:16 vertical.
```

### K09 · anexar SÓ `meredith callahan .png` + `natural_rems_seamoss_produto.jpg`

Cena: Ela segura o pote do Natural Rems Sea Moss colado na lente, rótulo legível, parado.

```text
K09
Match the attached image exactly for the woman's identity and outfit: a woman around seventy with deep brown skin, dark freckles on her cheekbones, deep laugh lines, gold-capped front teeth, silver-gray locs piled high inside a tall emerald-green and saffron-yellow patterned head wrap, red reading glasses resting on the front of the wrap, large gold bamboo hoop earrings, a stack of thin gold bangles on her left wrist, a loose cream cotton short-sleeve blouse with green leaf embroidery at the neckline, and a rust-orange apron tied at the waist. She stands behind a mint-green speckled Formica kitchen table in her small Brooklyn apartment kitchen: wooden cabinets, a row of large glass jars of pale golden sea moss and a glass blender on the counter at the left, a window at the right showing a red brick building with black iron balconies under an overcast blue-gray sky, and a small American flag in a potted plant on the windowsill, in sharp focus. Hero: she holds the Natural Rems Sea Moss Gummies jar exactly as in the second attached image: a short wide jar of dark amber plastic with a black screw cap, a pale sage-green label with dark green text, the Natural Rems logo with three leaves, the big title Sea Moss Gummies, a pill-shaped badge reading 6000 MG | 16-IN-1, and the line GREEN APPLE FLAVOR in her right hand out toward the camera, very close to the lens, large in frame and closer to the camera than her face, label fully readable, fingers on the sides, held still. She looks straight at the camera, caught mid-sentence, lips naturally parted, animated expression. Second image: front jar only. Vertical smartphone shot, 26mm lens, camera at chest height about one meter from the table, level, front facing. Soft neutral even daylight, true neutral colors, real skin texture with visible pores, smartphone footage look, everything in sharp focus, 9:16 vertical.
```

## 3. PROMPTS DE VÍDEO (um bloco por V)

### V01 · T1, GANCHO · anexar SÓ a imagem escolhida do K01

Cena: Gancho: ela segura três bananas descascadas colada na lente e despeja canela de um potinho por cima. Fala: "Coloque canela numa banana e só observe o que acontece."

```text
V01
The person in the image speaks in American English, looking at the camera: "Put cinnamon on a banana and just watch what happens."
Fixed camera. Natural lip sync, no music.
```

### V02 · T2, GANCHO · anexar SÓ a imagem escolhida do K02

Cena: Macro: as três bananas cobertas de canela empurradas quase encostando na lente, rosto dela atrás. Fala: "A grande indústria farmacêutica não quer que você saiba disso, porque perderia bilhões de dólares da noite pro dia."

```text
V02
The person in the image speaks in American English, looking at the camera: "Big Pharma does not want you to know this, because they would lose billions of dollars overnight."
Fixed camera. Natural lip sync, no music.
```

### V03 · T3, RECEITA · anexar SÓ a imagem escolhida do K03

Cena: Ela segura uma colher de canela e uma banana sobre o copo vazio do liquidificador; meio limão e copo de água na mesa. Fala: "Coloque uma banana fresca no liquidificador,"

```text
V03
The person in the image speaks in American English, looking at the camera: "Add one fresh banana to a blender,"
Fixed camera. Natural lip sync, no music.
```

### V04 · T4, RECEITA · anexar SÓ a imagem escolhida do K04

Cena: Close: banana dentro do copo do liquidificador; ela segura meio limão espremendo por cima. Fala: "uma colher de chá de canela, esprema meio limão,"

```text
V04
The person in the image speaks in American English, looking at the camera: "a teaspoon of cinnamon, squeeze in half a lemon,"
Fixed camera. Natural lip sync, no music.
```

### V05 · T5, RECEITA · anexar SÓ a imagem escolhida do K05

Cena: Ela despeja um copo de água no liquidificador com a banana. Fala: "coloque um copo de água,"

```text
V05
The person in the image speaks in American English, looking at the camera: "add a glass of water,"
Fixed camera. Natural lip sync, no music.
```

### V06 · T6, RECEITA · anexar SÓ a imagem escolhida do K06

Cena: Mão dela na tampa do liquidificador batendo, a vitamina bege girando, colado na lente. Fala: "e bata tudo isso até ficar liso."

```text
V06
The person in the image speaks in American English, looking at the camera: "and blend this whole thing until it is smooth."
Fixed camera. Natural lip sync, no music.
```

### V07 · T7, RESULTADO · anexar SÓ a imagem escolhida do K07

Cena: Ela segura o copo alto de vitamina de banana perto da lente; liquidificador atrás. Fala: "Essa vitamina bate no seu organismo como um botão de reiniciar que você nem sabia que existia."

```text
V07
The person in the image speaks in American English, looking at the camera: "This smoothie hits your insides like a reset button you never knew existed."
Fixed camera. Natural lip sync, no music.
```

### V08 · T8, RESULTADO · anexar SÓ a imagem escolhida do K07

Cena: Ela segura o copo alto de vitamina de banana perto da lente; liquidificador atrás. Fala: "Ela acalma o inchaço, te deixa saciada por horas, e segura a sua vontade de doce."

```text
V08
The person in the image speaks in American English, looking at the camera: "It calms the bloating, keeps you full for hours, and keeps your sugar cravings in check."
Fixed camera. Natural lip sync, no music.
```

### V09 · T9, VIRADA: O LADO RUIM DA RECEITA · anexar SÓ a imagem escolhida do K08

Cena: Ela sentada num banco junto à mesa, segurando o copo de vitamina perto da lente. Fala: "Mas vamos falar a verdade, banana escurece em dois dias, e lavar liquidificador toda santa manhã é um saco."

```text
V09
The person in the image speaks in American English, looking at the camera: "But let's be real, bananas go brown in two days, and scrubbing a blender every single morning is a chore."
Fixed camera. Natural lip sync, no music.
```

### V10 · T10, CATEGORIA + AUTORIDADE · anexar SÓ a imagem escolhida do K08

Cena: Ela sentada num banco junto à mesa, segurando o copo de vitamina perto da lente. Fala: "Então nas manhãs corridas, meu bem, eu confio no que os jamaicanos mexem nas bebidas há gerações, sea moss. Sem liquidificador."

```text
V10
The person in the image speaks in American English, looking at the camera: "So on busy mornings, baby, I trust what Jamaicans have stirred into drinks for generations, sea moss. No blender."
Fixed camera. Natural lip sync, no music.
```

### V11 · T11, OBSTÁCULO · anexar SÓ a imagem escolhida do K08

Cena: Ela sentada num banco junto à mesa, segurando o copo de vitamina perto da lente. Fala: "Mas a maioria das gomas de sea moss é carregada de açúcar, e açúcar é exatamente o que alimenta essa vontade."

```text
V11
The person in the image speaks in American English, looking at the camera: "But most sea moss gummies are loaded with sugar, and sugar is exactly what feeds those cravings."
Fixed camera. Natural lip sync, no music.
```

### V12 · T12, PRODUTO NO GESTO · anexar SÓ a imagem escolhida do K09

Cena: Ela segura o pote do Natural Rems Sea Moss colado na lente, rótulo legível, parado. Fala: "Eu mastigo Natural Rems Sea Moss. Ashwagandha, vinagre de maçã e vitamina C, dezesseis ingredientes numa goma."

```text
V12
The person in the image speaks in American English, looking at the camera: "I chew Natural Rems Sea Moss. Ashwagandha, apple cider vinegar and vitamin C, sixteen ingredients in one gummy."
Fixed camera. Natural lip sync, no music.
```

### V13 · T13, DIFERENCIAL · anexar SÓ a imagem escolhida do K09

Cena: Ela segura o pote do Natural Rems Sea Moss colado na lente, rótulo legível, parado. Fala: "Menos de um grama de açúcar, quatro calorias, e tem gosto de maçã verde, não de alga."

```text
V13
The person in the image speaks in American English, looking at the camera: "Under one gram of sugar, four calories, and it tastes like green apple, not seaweed."
Fixed camera. Natural lip sync, no music.
```

### V14 · T14, COMENTÁRIO · anexar SÓ a imagem escolhida do K09

Cena: Ela segura o pote do Natural Rems Sea Moss colado na lente, rótulo legível, parado. Fala: "Comenta yes se a vontade de doce ganha toda noite na sua casa, pra eu saber pra quem é isso."

```text
V14
The person in the image speaks in American English, looking at the camera: "Comment yes if sugar cravings win every night in your house, so I know who this is for."
Fixed camera. Natural lip sync, no music.
```

### V15 · T15, CTA AMAZON + BIO · anexar SÓ a imagem escolhida do K09

Cena: Ela segura o pote do Natural Rems Sea Moss colado na lente, rótulo legível, parado. Fala: "Procure Natural Rems Sea Moss na Amazon. Ou você também encontra o link na minha bio."

```text
V15
The person in the image speaks in American English, looking at the camera: "Search Natural Rems Sea Moss on Amazon. Or you can also find the link in my bio."
Fixed camera. Natural lip sync, no music.
```

### V16 · T16, FOLLOW · anexar SÓ a imagem escolhida do K09

Cena: Ela segura o pote do Natural Rems Sea Moss colado na lente, rótulo legível, parado. Fala: "E não esquece de apertar o botão de seguir."

```text
V16
The person in the image speaks in American English, looking at the camera: "And don't forget to hit that follow button."
Fixed camera. Natural lip sync, no music.
```

## 4. Transcrição final

| Take | English | Português |
|---|---|---|
| T1 | Put cinnamon on a banana and just watch what happens. | Coloque canela numa banana e só observe o que acontece. |
| T2 | Big Pharma does not want you to know this, because they would lose billions of dollars overnight. | A grande indústria farmacêutica não quer que você saiba disso, porque perderia bilhões de dólares da noite pro dia. |
| T3 | Add one fresh banana to a blender, | Coloque uma banana fresca no liquidificador, |
| T4 | a teaspoon of cinnamon, squeeze in half a lemon, | uma colher de chá de canela, esprema meio limão, |
| T5 | add a glass of water, | coloque um copo de água, |
| T6 | and blend this whole thing until it is smooth. | e bata tudo isso até ficar liso. |
| T7 | This smoothie hits your insides like a reset button you never knew existed. | Essa vitamina bate no seu organismo como um botão de reiniciar que você nem sabia que existia. |
| T8 | It calms the bloating, keeps you full for hours, and keeps your sugar cravings in check. | Ela acalma o inchaço, te deixa saciada por horas, e segura a sua vontade de doce. |
| T9 | But let's be real, bananas go brown in two days, and scrubbing a blender every single morning is a chore. | Mas vamos falar a verdade, banana escurece em dois dias, e lavar liquidificador toda santa manhã é um saco. |
| T10 | So on busy mornings, baby, I trust what Jamaicans have stirred into drinks for generations, sea moss. No blender. | Então nas manhãs corridas, meu bem, eu confio no que os jamaicanos mexem nas bebidas há gerações, sea moss. Sem liquidificador. |
| T11 | But most sea moss gummies are loaded with sugar, and sugar is exactly what feeds those cravings. | Mas a maioria das gomas de sea moss é carregada de açúcar, e açúcar é exatamente o que alimenta essa vontade. |
| T12 | I chew Natural Rems Sea Moss. Ashwagandha, apple cider vinegar and vitamin C, sixteen ingredients in one gummy. | Eu mastigo Natural Rems Sea Moss. Ashwagandha, vinagre de maçã e vitamina C, dezesseis ingredientes numa goma. |
| T13 | Under one gram of sugar, four calories, and it tastes like green apple, not seaweed. | Menos de um grama de açúcar, quatro calorias, e tem gosto de maçã verde, não de alga. |
| T14 | Comment yes if sugar cravings win every night in your house, so I know who this is for. | Comenta yes se a vontade de doce ganha toda noite na sua casa, pra eu saber pra quem é isso. |
| T15 | Search Natural Rems Sea Moss on Amazon. Or you can also find the link in my bio. | Procure Natural Rems Sea Moss na Amazon. Ou você também encontra o link na minha bio. |
| T16 | And don't forget to hit that follow button. | E não esquece de apertar o botão de seguir. |

**EN corrido:** Put cinnamon on a banana and just watch what happens. Big Pharma does not want you to know this, because they would lose billions of dollars overnight. Add one fresh banana to a blender, a teaspoon of cinnamon, squeeze in half a lemon, add a glass of water, and blend this whole thing until it is smooth. This smoothie hits your insides like a reset button you never knew existed. It calms the bloating, keeps you full for hours, and keeps your sugar cravings in check. But let's be real, bananas go brown in two days, and scrubbing a blender every single morning is a chore. So on busy mornings, baby, I trust what Jamaicans have stirred into drinks for generations, sea moss. No blender. But most sea moss gummies are loaded with sugar, and sugar is exactly what feeds those cravings. I chew Natural Rems Sea Moss. Ashwagandha, apple cider vinegar and vitamin C, sixteen ingredients in one gummy. Under one gram of sugar, four calories, and it tastes like green apple, not seaweed. Comment yes if sugar cravings win every night in your house, so I know who this is for. Search Natural Rems Sea Moss on Amazon. Or you can also find the link in my bio. And don't forget to hit that follow button.

**PT corrido:** Coloque canela numa banana e só observe o que acontece. A grande indústria farmacêutica não quer que você saiba disso, porque perderia bilhões de dólares da noite pro dia. Coloque uma banana fresca no liquidificador, uma colher de chá de canela, esprema meio limão, coloque um copo de água, e bata tudo isso até ficar liso. Essa vitamina bate no seu organismo como um botão de reiniciar que você nem sabia que existia. Ela acalma o inchaço, te deixa saciada por horas, e segura a sua vontade de doce. Mas vamos falar a verdade, banana escurece em dois dias, e lavar liquidificador toda santa manhã é um saco. Então nas manhãs corridas, meu bem, eu confio no que os jamaicanos mexem nas bebidas há gerações, sea moss. Sem liquidificador. Mas a maioria das gomas de sea moss é carregada de açúcar, e açúcar é exatamente o que alimenta essa vontade. Eu mastigo Natural Rems Sea Moss. Ashwagandha, vinagre de maçã e vitamina C, dezesseis ingredientes numa goma. Menos de um grama de açúcar, quatro calorias, e tem gosto de maçã verde, não de alga. Comenta yes se a vontade de doce ganha toda noite na sua casa, pra eu saber pra quem é isso. Procure Natural Rems Sea Moss na Amazon. Ou você também encontra o link na minha bio. E não esquece de apertar o botão de seguir.
