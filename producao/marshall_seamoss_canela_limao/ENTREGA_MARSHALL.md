# ENTREGA | Marshall Beckett | Sea Moss Venda · Água de canela, limão e mel → Natural Rems Sea Moss

flow_seguro: v1

Produção `marshall_seamoss_canela_limao` · Ângulo 1 Sea Moss (conta da Marshall) · VENDA · rodada de VALIDAÇÃO · formato mínimo de prompt do Flow

## 0. INSTRUÇÕES PARA A MEMÓRIA DO AGENTE · GOOGLE FLOW (colar inteiro antes do primeiro K)

```text
# Agente do Flow, produção atual: Sea Moss Venda · Água de canela, limão e mel → Natural Rems Sea Moss

Você é o executor do Google Flow. Você só gera imagens e vídeos a partir de prompts prontos. Você não cria, não edita e não melhora prompt.

## Produção atual
- Conta: Natural Rems Sea Moss (Marshall), vídeo de venda. Sea Moss Venda · Água de canela, limão e mel → Natural Rems Sea Moss.
- Um avatar só: a senhora de roupa branca de mergulhadora com a máscara de latão na testa (arquivo `marshall beckett .jpg`). Imagens K01 a K09; vídeos V01 a V15.

## O que é anexado (só isto, nada mais)
- IMAGEM (K): anexe só a imagem da avatar e cole o prompt.
- EXCEÇÃO K02: NÃO anexe nenhuma imagem, só cole o prompt.
- EXCEÇÃO K09: anexe `marshall beckett .jpg` e `natural_rems_seamoss_produto.jpg` (nesta ordem).
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

## Vídeos (V01 a V15)
1. Só começa quando o operador mandar. Mapa: V01 usa K01; V02 usa K02; V03 usa K03; V04 usa K04; V05 usa K05; V06 usa K06; V07 a V08 usam todos a mesma imagem escolhida do K07; V09 usa K08; V10 a V15 usam todos a mesma imagem escolhida do K09. Se o K tiver mais de uma imagem ou nenhuma, pare e pergunte qual.
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

**Vídeo: Água de canela, limão e mel → Natural Rems Sea Moss.**

**O que acontece:** Marshall Beckett, no cenário fixo da conta, faz a receita do modelo cena a cena, mostra o resultado e os benefícios, admite o lado ruim de fazer a receita e passa para o sea moss; a partir do T10 segura o pote do Natural Rems Sea Moss parado e legível até o fim. Fecha com comment yes, Amazon, Stories e bio, e o lembrete do follow.

**Gancho:** Gancho: boneco humano de açúcar ao lado dela, colado na lente; ela despeja canela de um pote de vidro na cabeça dele.

## 1. Anexos e mapa

- **Imagem (K):** anexar SÓ o que o título de cada K indica (padrão: a imagem da avatar, `marshall beckett .jpg`) e colar o prompt. 4 variações, 9:16. Nada de frame do modelo.
- **Vídeo (V):** anexar SÓ a imagem escolhida do K indicado no mapa e colar o prompt de vídeo. 1 variação, 9:16.
- Bloco do agente Flow desta produção: `AGENTE_FLOW.md`.

V01 usa K01; V02 usa K02; V03 usa K03; V04 usa K04; V05 usa K05; V06 usa K06; V07 a V08 usam a mesma imagem escolhida do K07; V09 usa K08; V10 a V15 usam a mesma imagem escolhida do K09.

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
V10: K09
V11: K09
V12: K09
V13: K09
V14: K09
V15: K09
```

## 2. PROMPTS DE IMAGEM (um bloco por K)

### K01 · anexar SÓ `marshall beckett .jpg`

Cena: Gancho: boneco humano de açúcar ao lado dela, colado na lente; ela despeja canela de um pote de vidro na cabeça dele.

```text
K01
Match the attached image exactly for the woman's identity and outfit: a Japanese-American woman in her seventies with deeply sun-darkened skin, sun spots and dark freckles, deep wrinkles, calm narrow dark eyes, a lean strong build, a white cotton headscarf tied around her forehead with an antique round brass-rimmed diving mask pushed up on top of it, a white cotton wrap jacket tied at the waist with white cotton pants, and a small abalone shell pendant on a black cord. She stands behind a weathered gray wooden plank table under an open shed with a rusted corrugated tin roof on a black lava rock shore in Hawaii: bamboo mats of drying green and dark red seaweed on both sides, a wooden wash tub on the right, turquoise ocean with white surf behind her under an overcast blue-gray sky, and a small American flag tied to the right wooden post, in sharp focus. Hero: a life-size human figure sculpted entirely from coarse white sugar crystals stands right beside her, its head and shoulders very close to the lens, large in frame and closer to the camera than her face, a reddish-brown dusting of ground cinnamon already on its shoulders. She raises a small glass jar of ground cinnamon above its head and pours a stream of cinnamon onto the crown. She looks straight at the camera, caught mid-sentence, lips naturally parted, animated expression. Vertical smartphone shot, 26mm lens, camera at chest height about one meter from the table, level, front facing. Soft neutral even daylight, true neutral colors, real skin texture with visible pores, smartphone footage look, everything in sharp focus, 9:16 vertical.
```

### K02 · anexar SÓ nenhuma imagem (só o texto)

Cena: Take mudo: o boneco de açúcar sozinho no cenário da conta, inteiro, com canela nos ombros.

```text
K02
Vertical photo of an empty scene. Hero: a life-size human figure sculpted entirely from coarse white sugar crystals stands upright in the center of the frame, full body, arms at its sides, a reddish-brown dusting of ground cinnamon on its head and shoulders, a small pile of loose sugar crystals at its feet. The scene is set behind a weathered gray wooden plank table under an open shed with a rusted corrugated tin roof on a black lava rock shore in Hawaii: bamboo mats of drying green and dark red seaweed on both sides, a wooden wash tub on the right, turquoise ocean with white surf behind it under an overcast blue-gray sky, and a small American flag tied to the right wooden post, in sharp focus. Vertical smartphone shot, 26mm lens, camera at chest height about one meter from the table, level, front facing. Soft neutral even daylight, true neutral colors, crisp crystal texture, smartphone footage look, everything in sharp focus, 9:16 vertical.
```

### K03 · anexar SÓ `marshall beckett .jpg`

Cena: Copo de água colado na lente; ela põe uma colher de canela. Meio limão e pote de mel ao lado.

```text
K03
Match the attached image exactly for the woman's identity and outfit: a Japanese-American woman in her seventies with deeply sun-darkened skin, sun spots and dark freckles, deep wrinkles, calm narrow dark eyes, a lean strong build, a white cotton headscarf tied around her forehead with an antique round brass-rimmed diving mask pushed up on top of it, a white cotton wrap jacket tied at the waist with white cotton pants, and a small abalone shell pendant on a black cord. She stands behind a weathered gray wooden plank table under an open shed with a rusted corrugated tin roof on a black lava rock shore in Hawaii: bamboo mats of drying green and dark red seaweed on both sides, a wooden wash tub on the right, turquoise ocean with white surf behind her under an overcast blue-gray sky, and a small American flag tied to the right wooden post, in sharp focus. Hero: on the gray plank table in the lower foreground, very close to the lens, large in frame and closer to the camera than her face: a clear glass of warm water. She holds a teaspoon of ground cinnamon over the glass, tipping it in; half a lemon and a small glass jar of raw honey stand beside the glass. She looks straight at the camera, caught mid-sentence, lips naturally parted, animated expression. Vertical smartphone shot, 26mm lens, camera at chest height about one meter from the table, level, front facing. Soft neutral even daylight, true neutral colors, real skin texture with visible pores, smartphone footage look, everything in sharp focus, 9:16 vertical.
```

### K04 · anexar SÓ `marshall beckett .jpg`

Cena: Close: ela espreme meio limão em cima do copo, colado na lente.

```text
K04
Match the attached image exactly for the woman's identity and outfit: a Japanese-American woman in her seventies with deeply sun-darkened skin, sun spots and dark freckles, deep wrinkles, calm narrow dark eyes, a lean strong build, a white cotton headscarf tied around her forehead with an antique round brass-rimmed diving mask pushed up on top of it, a white cotton wrap jacket tied at the waist with white cotton pants, and a small abalone shell pendant on a black cord. She stands behind a weathered gray wooden plank table under an open shed with a rusted corrugated tin roof on a black lava rock shore in Hawaii: bamboo mats of drying green and dark red seaweed on both sides, a wooden wash tub on the right, turquoise ocean with white surf behind her under an overcast blue-gray sky, and a small American flag tied to the right wooden post, in sharp focus. Hero: in the lower foreground, very close to the lens, large in frame and closer to the camera than her face: the clear glass of water with cinnamon floating on top, and her hand squeezing half a fresh lemon over it, juice dripping in. She looks straight at the camera, caught mid-sentence, lips naturally parted, animated expression. Vertical smartphone shot, 26mm lens, camera at chest height about one meter from the table, level, front facing. Soft neutral even daylight, true neutral colors, real skin texture with visible pores, smartphone footage look, everything in sharp focus, 9:16 vertical.
```

### K05 · anexar SÓ `marshall beckett .jpg`

Cena: Ela segura uma colher de mel cru sobre o copo; potinhos de cúrcuma e sal rosa ao lado.

```text
K05
Match the attached image exactly for the woman's identity and outfit: a Japanese-American woman in her seventies with deeply sun-darkened skin, sun spots and dark freckles, deep wrinkles, calm narrow dark eyes, a lean strong build, a white cotton headscarf tied around her forehead with an antique round brass-rimmed diving mask pushed up on top of it, a white cotton wrap jacket tied at the waist with white cotton pants, and a small abalone shell pendant on a black cord. She stands behind a weathered gray wooden plank table under an open shed with a rusted corrugated tin roof on a black lava rock shore in Hawaii: bamboo mats of drying green and dark red seaweed on both sides, a wooden wash tub on the right, turquoise ocean with white surf behind her under an overcast blue-gray sky, and a small American flag tied to the right wooden post, in sharp focus. Hero: on the gray plank table in the lower foreground, very close to the lens, large in frame and closer to the camera than her face: the glass of cloudy cinnamon lemon water. She holds a tablespoon of thick raw honey over it; a small ceramic bowl of bright turmeric powder and a small bowl of pink salt stand beside it. She looks straight at the camera, caught mid-sentence, lips naturally parted, animated expression. Vertical smartphone shot, 26mm lens, camera at chest height about one meter from the table, level, front facing. Soft neutral even daylight, true neutral colors, real skin texture with visible pores, smartphone footage look, everything in sharp focus, 9:16 vertical.
```

### K06 · anexar SÓ `marshall beckett .jpg`

Cena: Close: ela solta uma fatia de gengibre fresco dentro do copo; potinhos de cúrcuma e sal rosa ao lado.

```text
K06
Match the attached image exactly for the woman's identity and outfit: a Japanese-American woman in her seventies with deeply sun-darkened skin, sun spots and dark freckles, deep wrinkles, calm narrow dark eyes, a lean strong build, a white cotton headscarf tied around her forehead with an antique round brass-rimmed diving mask pushed up on top of it, a white cotton wrap jacket tied at the waist with white cotton pants, and a small abalone shell pendant on a black cord. She stands behind a weathered gray wooden plank table under an open shed with a rusted corrugated tin roof on a black lava rock shore in Hawaii: bamboo mats of drying green and dark red seaweed on both sides, a wooden wash tub on the right, turquoise ocean with white surf behind her under an overcast blue-gray sky, and a small American flag tied to the right wooden post, in sharp focus. Hero: in the lower foreground, very close to the lens, large in frame and closer to the camera than her face: the glass of golden drink with a slice of lemon inside. Her fingers drop a thin round slice of fresh ginger into it; a small ceramic bowl of turmeric powder and a small bowl of pink salt stand beside the glass. She looks straight at the camera, caught mid-sentence, lips naturally parted, animated expression. Vertical smartphone shot, 26mm lens, camera at chest height about one meter from the table, level, front facing. Soft neutral even daylight, true neutral colors, real skin texture with visible pores, smartphone footage look, everything in sharp focus, 9:16 vertical.
```

### K07 · anexar SÓ `marshall beckett .jpg`

Cena: Ela segura o copo pronto, dourado e turvo com fatia de limão, perto da lente.

```text
K07
Match the attached image exactly for the woman's identity and outfit: a Japanese-American woman in her seventies with deeply sun-darkened skin, sun spots and dark freckles, deep wrinkles, calm narrow dark eyes, a lean strong build, a white cotton headscarf tied around her forehead with an antique round brass-rimmed diving mask pushed up on top of it, a white cotton wrap jacket tied at the waist with white cotton pants, and a small abalone shell pendant on a black cord. She stands behind a weathered gray wooden plank table under an open shed with a rusted corrugated tin roof on a black lava rock shore in Hawaii: bamboo mats of drying green and dark red seaweed on both sides, a wooden wash tub on the right, turquoise ocean with white surf behind her under an overcast blue-gray sky, and a small American flag tied to the right wooden post, in sharp focus. Hero: she holds the finished glass of cloudy golden drink with a slice of lemon and a slice of ginger inside out toward the camera in her right hand, very close to the lens, large in frame and closer to the camera than her face. She looks straight at the camera, caught mid-sentence, lips naturally parted, animated expression. Vertical smartphone shot, 26mm lens, camera at chest height about one meter from the table, level, front facing. Soft neutral even daylight, true neutral colors, real skin texture with visible pores, smartphone footage look, everything in sharp focus, 9:16 vertical.
```

### K08 · anexar SÓ `marshall beckett .jpg`

Cena: Ela segura uma tábua redonda com os seis ingredientes e o copo, perto da lente.

```text
K08
Match the attached image exactly for the woman's identity and outfit: a Japanese-American woman in her seventies with deeply sun-darkened skin, sun spots and dark freckles, deep wrinkles, calm narrow dark eyes, a lean strong build, a white cotton headscarf tied around her forehead with an antique round brass-rimmed diving mask pushed up on top of it, a white cotton wrap jacket tied at the waist with white cotton pants, and a small abalone shell pendant on a black cord. She stands behind a weathered gray wooden plank table under an open shed with a rusted corrugated tin roof on a black lava rock shore in Hawaii: bamboo mats of drying green and dark red seaweed on both sides, a wooden wash tub on the right, turquoise ocean with white surf behind her under an overcast blue-gray sky, and a small American flag tied to the right wooden post, in sharp focus. Hero: she holds a round wooden board out toward the camera with both hands, very close to the lens, large in frame and closer to the camera than her face: on it a glass mug of the golden drink, cinnamon sticks, a knob of fresh ginger, a small pile of grated ginger, a mound of turmeric powder, half a lemon and a small jar of honey. She looks straight at the camera, caught mid-sentence, lips naturally parted, animated expression. Vertical smartphone shot, 26mm lens, camera at chest height about one meter from the table, level, front facing. Soft neutral even daylight, true neutral colors, real skin texture with visible pores, smartphone footage look, everything in sharp focus, 9:16 vertical.
```

### K09 · anexar SÓ `marshall beckett .jpg` + `natural_rems_seamoss_produto.jpg`

Cena: Ela segura o pote do Natural Rems Sea Moss colado na lente, rótulo legível, parado.

```text
K09
Match the attached image exactly for the woman's identity and outfit: a Japanese-American woman in her seventies with deeply sun-darkened skin, sun spots and dark freckles, deep wrinkles, calm narrow dark eyes, a lean strong build, a white cotton headscarf tied around her forehead with an antique round brass-rimmed diving mask pushed up on top of it, a white cotton wrap jacket tied at the waist with white cotton pants, and a small abalone shell pendant on a black cord. She stands behind a weathered gray wooden plank table under an open shed with a rusted corrugated tin roof on a black lava rock shore in Hawaii: bamboo mats of drying green and dark red seaweed on both sides, a wooden wash tub on the right, turquoise ocean with white surf behind her under an overcast blue-gray sky, and a small American flag tied to the right wooden post, in sharp focus. Hero: she holds the Natural Rems Sea Moss Gummies jar exactly as in the second attached image: a short wide jar of dark amber plastic with a black screw cap, a pale sage-green label with dark green text, the Natural Rems logo with three leaves, the big title Sea Moss Gummies, a pill-shaped badge reading 6000 MG | 16-IN-1, and the line GREEN APPLE FLAVOR in her right hand out toward the camera, very close to the lens, large in frame and closer to the camera than her face, label fully readable, fingers on the sides, held still. She looks straight at the camera, caught mid-sentence, lips naturally parted, animated expression. Second image: front jar only. Vertical smartphone shot, 26mm lens, camera at chest height about one meter from the table, level, front facing. Soft neutral even daylight, true neutral colors, real skin texture with visible pores, smartphone footage look, everything in sharp focus, 9:16 vertical.
```

## 3. PROMPTS DE VÍDEO (um bloco por V)

### V01 · T1, GANCHO · anexar SÓ a imagem escolhida do K01

Cena: Gancho: boneco humano de açúcar ao lado dela, colado na lente; ela despeja canela de um pote de vidro na cabeça dele. Fala: "Isto é o que a canela faz com o açúcar no seu corpo."

```text
V01
The person in the image speaks in American English, looking at the camera: "This is what cinnamon does to the sugar in your body."
Fixed camera. Natural lip sync, no music.
```

### V02 · T2, GANCHO · anexar SÓ a imagem escolhida do K02

Cena: Take mudo: o boneco de açúcar sozinho no cenário da conta, inteiro, com canela nos ombros. Fala: "(sem fala)"

```text
V02
(no speech) The white sugar sculpture in the image slowly melts away grain by grain, the sugar crystals sliding down like fine sand into a soft heap on the ground, a light dust of cinnamon drifting down with them.
Fixed camera, no music.
```

### V03 · T3, RECEITA · anexar SÓ a imagem escolhida do K03

Cena: Copo de água colado na lente; ela põe uma colher de canela. Meio limão e pote de mel ao lado. Fala: "Num copo de água morna, misture uma colher de chá de canela,"

```text
V03
The person in the image speaks in American English, looking at the camera: "In a glass of warm water, mix one teaspoon of cinnamon,"
Fixed camera. Natural lip sync, no music.
```

### V04 · T4, RECEITA · anexar SÓ a imagem escolhida do K04

Cena: Close: ela espreme meio limão em cima do copo, colado na lente. Fala: "um pouco de suco de limão fresco,"

```text
V04
The person in the image speaks in American English, looking at the camera: "a squeeze of fresh lemon juice,"
Fixed camera. Natural lip sync, no music.
```

### V05 · T5, RECEITA · anexar SÓ a imagem escolhida do K05

Cena: Ela segura uma colher de mel cru sobre o copo; potinhos de cúrcuma e sal rosa ao lado. Fala: "e uma colher de sopa de mel cru. Agora, se você quer levar isso para o próximo nível,"

```text
V05
The person in the image speaks in American English, looking at the camera: "and one tablespoon of raw honey. Now, if you wanna take this to the next level,"
Fixed camera. Natural lip sync, no music.
```

### V06 · T6, RECEITA · anexar SÓ a imagem escolhida do K06

Cena: Close: ela solta uma fatia de gengibre fresco dentro do copo; potinhos de cúrcuma e sal rosa ao lado. Fala: "coloque uma fatia de gengibre fresco para fazer a digestão andar, uma pitada de cúrcuma para acalmar a inflamação, e uma pitadinha de sal rosa."

```text
V06
The person in the image speaks in American English, looking at the camera: "add a slice of fresh ginger to get your digestion moving, a pinch of turmeric to calm the inflammation, and a tiny pinch of pink salt."
Fixed camera. Natural lip sync, no music.
```

### V07 · T7, PROTOCOLO · anexar SÓ a imagem escolhida do K07

Cena: Ela segura o copo pronto, dourado e turvo com fatia de limão, perto da lente. Fala: "Misture bem e beba isso em jejum, toda santa manhã."

```text
V07
The person in the image speaks in American English, looking at the camera: "Mix it well, then drink this on an empty stomach every single morning."
Fixed camera. Natural lip sync, no music.
```

### V08 · T8, RESULTADO · anexar SÓ a imagem escolhida do K07

Cena: Ela segura o copo pronto, dourado e turvo com fatia de limão, perto da lente. Fala: "A sua energia começa a voltar, as roupas começam a servir melhor, e você finalmente começa a se sentir você de novo."

```text
V08
The person in the image speaks in American English, looking at the camera: "Your energy starts coming back, your clothes start fitting better, and you finally start feeling like yourself again."
Fixed camera. Natural lip sync, no music.
```

### V09 · T9, VIRADA: O LADO RUIM DA RECEITA · anexar SÓ a imagem escolhida do K08

Cena: Ela segura uma tábua redonda com os seis ingredientes e o copo, perto da lente. Fala: "Mas vamos ser sinceros, ralar gengibre e medir seis ingredientes em jejum, antes do seu dia nem começar, é chato."

```text
V09
The person in the image speaks in American English, looking at the camera: "But let's be honest, grating ginger and measuring six ingredients on an empty stomach, before your day even starts, is annoying."
Fixed camera. Natural lip sync, no music.
```

### V10 · T10, PONTE + PRODUTO NO GESTO · anexar SÓ a imagem escolhida do K09

Cena: Ela segura o pote do Natural Rems Sea Moss colado na lente, rótulo legível, parado. Fala: "É por isso que eu só mastigo uma goma de Natural Rems Sea Moss. Gengibre, cúrcuma, mel de manuka e vitamina C, tudo numa goma só."

```text
V10
The person in the image speaks in American English, looking at the camera: "That's why I just chew one Natural Rems Sea Moss gummy. Ginger, turmeric, manuka honey and vitamin C, all in one gummy."
Fixed camera. Natural lip sync, no music.
```

### V11 · T11, OBSTÁCULO + AUTORIDADE · anexar SÓ a imagem escolhida do K09

Cena: Ela segura o pote do Natural Rems Sea Moss colado na lente, rótulo legível, parado. Fala: "Eu colho alga deste oceano a vida inteira. A maioria das gomas da prateleira é cheia de açúcar, e isso desfaz essa bebida inteira."

```text
V11
The person in the image speaks in American English, looking at the camera: "I have gathered seaweed from this ocean my whole life. Most gummies on the shelf are packed with sugar, and that undoes this whole drink."
Fixed camera. Natural lip sync, no music.
```

### V12 · T12, DIFERENCIAL · anexar SÓ a imagem escolhida do K09

Cena: Ela segura o pote do Natural Rems Sea Moss colado na lente, rótulo legível, parado. Fala: "Esta é de sea moss irlandês selvagem, feita nos EUA, com menos de um grama de açúcar, e tem gosto de maçã verde."

```text
V12
The person in the image speaks in American English, looking at the camera: "This one is wild Irish sea moss, made in the USA, with less than one gram of sugar, and it tastes like green apple."
Fixed camera. Natural lip sync, no music.
```

### V13 · T13, COMENTÁRIO · anexar SÓ a imagem escolhida do K09

Cena: Ela segura o pote do Natural Rems Sea Moss colado na lente, rótulo legível, parado. Fala: "Se você convive com o inchaço todo dia, comenta yes, pra eu saber pra quem eu faço o próximo vídeo."

```text
V13
The person in the image speaks in American English, looking at the camera: "If you're dealing with bloating every day, comment yes, so I know who I'm making the next video for."
Fixed camera. Natural lip sync, no music.
```

### V14 · T14, CTA AMAZON + DESTINO · anexar SÓ a imagem escolhida do K09

Cena: Ela segura o pote do Natural Rems Sea Moss colado na lente, rótulo legível, parado. Fala: "Procure Natural Rems Sea Moss na Amazon. Ou toque na minha foto de perfil, o link está te esperando nos meus stories, ou bem ali na minha bio."

```text
V14
The person in the image speaks in American English, looking at the camera: "Search Natural Rems Sea Moss on Amazon. Or tap my profile picture, the link is waiting in my stories, or right there in my bio."
Fixed camera. Natural lip sync, no music.
```

### V15 · T15, FOLLOW · anexar SÓ a imagem escolhida do K09

Cena: Ela segura o pote do Natural Rems Sea Moss colado na lente, rótulo legível, parado. Fala: "E não esquece de apertar o botão de seguir."

```text
V15
The person in the image speaks in American English, looking at the camera: "And don't forget to hit that follow button."
Fixed camera. Natural lip sync, no music.
```

## 4. Transcrição final

| Take | English | Português |
|---|---|---|
| T1 | This is what cinnamon does to the sugar in your body. | Isto é o que a canela faz com o açúcar no seu corpo. |
| T2 | (no speech) | (sem fala) |
| T3 | In a glass of warm water, mix one teaspoon of cinnamon, | Num copo de água morna, misture uma colher de chá de canela, |
| T4 | a squeeze of fresh lemon juice, | um pouco de suco de limão fresco, |
| T5 | and one tablespoon of raw honey. Now, if you wanna take this to the next level, | e uma colher de sopa de mel cru. Agora, se você quer levar isso para o próximo nível, |
| T6 | add a slice of fresh ginger to get your digestion moving, a pinch of turmeric to calm the inflammation, and a tiny pinch of pink salt. | coloque uma fatia de gengibre fresco para fazer a digestão andar, uma pitada de cúrcuma para acalmar a inflamação, e uma pitadinha de sal rosa. |
| T7 | Mix it well, then drink this on an empty stomach every single morning. | Misture bem e beba isso em jejum, toda santa manhã. |
| T8 | Your energy starts coming back, your clothes start fitting better, and you finally start feeling like yourself again. | A sua energia começa a voltar, as roupas começam a servir melhor, e você finalmente começa a se sentir você de novo. |
| T9 | But let's be honest, grating ginger and measuring six ingredients on an empty stomach, before your day even starts, is annoying. | Mas vamos ser sinceros, ralar gengibre e medir seis ingredientes em jejum, antes do seu dia nem começar, é chato. |
| T10 | That's why I just chew one Natural Rems Sea Moss gummy. Ginger, turmeric, manuka honey and vitamin C, all in one gummy. | É por isso que eu só mastigo uma goma de Natural Rems Sea Moss. Gengibre, cúrcuma, mel de manuka e vitamina C, tudo numa goma só. |
| T11 | I have gathered seaweed from this ocean my whole life. Most gummies on the shelf are packed with sugar, and that undoes this whole drink. | Eu colho alga deste oceano a vida inteira. A maioria das gomas da prateleira é cheia de açúcar, e isso desfaz essa bebida inteira. |
| T12 | This one is wild Irish sea moss, made in the USA, with less than one gram of sugar, and it tastes like green apple. | Esta é de sea moss irlandês selvagem, feita nos EUA, com menos de um grama de açúcar, e tem gosto de maçã verde. |
| T13 | If you're dealing with bloating every day, comment yes, so I know who I'm making the next video for. | Se você convive com o inchaço todo dia, comenta yes, pra eu saber pra quem eu faço o próximo vídeo. |
| T14 | Search Natural Rems Sea Moss on Amazon. Or tap my profile picture, the link is waiting in my stories, or right there in my bio. | Procure Natural Rems Sea Moss na Amazon. Ou toque na minha foto de perfil, o link está te esperando nos meus stories, ou bem ali na minha bio. |
| T15 | And don't forget to hit that follow button. | E não esquece de apertar o botão de seguir. |

**EN corrido:** This is what cinnamon does to the sugar in your body. (no speech) In a glass of warm water, mix one teaspoon of cinnamon, a squeeze of fresh lemon juice, and one tablespoon of raw honey. Now, if you wanna take this to the next level, add a slice of fresh ginger to get your digestion moving, a pinch of turmeric to calm the inflammation, and a tiny pinch of pink salt. Mix it well, then drink this on an empty stomach every single morning. Your energy starts coming back, your clothes start fitting better, and you finally start feeling like yourself again. But let's be honest, grating ginger and measuring six ingredients on an empty stomach, before your day even starts, is annoying. That's why I just chew one Natural Rems Sea Moss gummy. Ginger, turmeric, manuka honey and vitamin C, all in one gummy. I have gathered seaweed from this ocean my whole life. Most gummies on the shelf are packed with sugar, and that undoes this whole drink. This one is wild Irish sea moss, made in the USA, with less than one gram of sugar, and it tastes like green apple. If you're dealing with bloating every day, comment yes, so I know who I'm making the next video for. Search Natural Rems Sea Moss on Amazon. Or tap my profile picture, the link is waiting in my stories, or right there in my bio. And don't forget to hit that follow button.

**PT corrido:** Isto é o que a canela faz com o açúcar no seu corpo. (sem fala) Num copo de água morna, misture uma colher de chá de canela, um pouco de suco de limão fresco, e uma colher de sopa de mel cru. Agora, se você quer levar isso para o próximo nível, coloque uma fatia de gengibre fresco para fazer a digestão andar, uma pitada de cúrcuma para acalmar a inflamação, e uma pitadinha de sal rosa. Misture bem e beba isso em jejum, toda santa manhã. A sua energia começa a voltar, as roupas começam a servir melhor, e você finalmente começa a se sentir você de novo. Mas vamos ser sinceros, ralar gengibre e medir seis ingredientes em jejum, antes do seu dia nem começar, é chato. É por isso que eu só mastigo uma goma de Natural Rems Sea Moss. Gengibre, cúrcuma, mel de manuka e vitamina C, tudo numa goma só. Eu colho alga deste oceano a vida inteira. A maioria das gomas da prateleira é cheia de açúcar, e isso desfaz essa bebida inteira. Esta é de sea moss irlandês selvagem, feita nos EUA, com menos de um grama de açúcar, e tem gosto de maçã verde. Se você convive com o inchaço todo dia, comenta yes, pra eu saber pra quem eu faço o próximo vídeo. Procure Natural Rems Sea Moss na Amazon. Ou toque na minha foto de perfil, o link está te esperando nos meus stories, ou bem ali na minha bio. E não esquece de apertar o botão de seguir.
