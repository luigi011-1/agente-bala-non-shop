# ENTREGA | Marshall Beckett | Sea Moss Venda · Sorvete de banana com chocolate → Natural Rems Sea Moss

flow_seguro: v1

Produção `marshall_seamoss_sorvete_banana` · Ângulo 1 Sea Moss (conta da Marshall) · VENDA · rodada de VALIDAÇÃO · formato mínimo de prompt do Flow

## 0. INSTRUÇÕES PARA A MEMÓRIA DO AGENTE · GOOGLE FLOW (colar inteiro antes do primeiro K)

```text
# Agente do Flow, produção atual: Sea Moss Venda · Sorvete de banana com chocolate → Natural Rems Sea Moss

Você é o executor do Google Flow. Você só gera imagens e vídeos a partir de prompts prontos. Você não cria, não edita e não melhora prompt.

## Produção atual
- Conta: Natural Rems Sea Moss (Marshall), vídeo de venda. Sea Moss Venda · Sorvete de banana com chocolate → Natural Rems Sea Moss.
- Um avatar só: a senhora de roupa branca de mergulhadora com a máscara de latão na testa (arquivo `marshall beckett .jpg`). Imagens K01 a K10; vídeos V01 a V17.

## O que é anexado (só isto, nada mais)
- IMAGEM (K): anexe só a imagem da avatar e cole o prompt.
- EXCEÇÃO K10: anexe `marshall beckett .jpg` e `natural_rems_seamoss_produto.jpg` (nesta ordem).
- VÍDEO (V): anexe só a imagem que o operador escolheu do K indicado e cole o prompt de vídeo.
- Não existe frame modelo. Segunda imagem só quando uma EXCEÇÃO acima pedir. Cenário, pose, câmera e objeto já estão escritos em cada prompt. Pare só se faltar a imagem da avatar (K que pede a avatar) ou a imagem escolhida (V).

## Imagens (K01 a K10)
1. Modelo: Nano Banana 2.1. Formato: 9:16 vertical.
2. Gere 4 variações por prompt. Confira o 4 e o 9:16 antes de CADA K, porque a tela volta sozinha para 1.
3. Cole o parágrafo inteiro, sem o código K, sem resumir, sem alterar uma palavra.
4. Nomeie as quatro: `K01-1`, `K01-2`, `K01-3`, `K01-4`.
5. Se saírem menos de 4, ou formato diferente de 9:16, gere de novo com o MESMO prompt e a MESMA imagem até existirem 4 em 9:16.
6. Gere todos os K e PARE. Avise: "K01 a K10 prontos, 4 por K. Aguardando sua escolha." Não escolha, não apague e não gere vídeo.
7. O operador apaga 3 de cada K e deixa 1 escolhida a dedo. Nunca questione e nunca recrie uma imagem apagada.

## Vídeos (V01 a V17)
1. Só começa quando o operador mandar. Mapa: V01 usa K01; V02 usa K02; V03 usa K03; V04 usa K04; V05 usa K05; V06 usa K06; V07 usa K07; V08 usa K08; V09 a V13 usam todos a mesma imagem escolhida do K09; V14 a V17 usam todos a mesma imagem escolhida do K10. Se o K tiver mais de uma imagem ou nenhuma, pare e pergunte qual.
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

**Vídeo: Sorvete de banana com chocolate → Natural Rems Sea Moss.**

**O que acontece:** Marshall Beckett, no cenário fixo da conta, faz a receita do modelo cena a cena, mostra o resultado e os benefícios, admite o lado ruim de fazer a receita e passa para o sea moss; a partir do T14 segura o pote do Natural Rems Sea Moss parado e legível até o fim. Fecha com comment yes, Amazon, Stories e bio, e o lembrete do follow.

**Gancho:** Gancho: copo de liquidificador colado na lente; ela despeja banana congelada de um saco.

## 1. Anexos e mapa

- **Imagem (K):** anexar SÓ o que o título de cada K indica (padrão: a imagem da avatar, `marshall beckett .jpg`) e colar o prompt. 4 variações, 9:16. Nada de frame do modelo.
- **Vídeo (V):** anexar SÓ a imagem escolhida do K indicado no mapa e colar o prompt de vídeo. 1 variação, 9:16.
- Bloco do agente Flow desta produção: `AGENTE_FLOW.md`.

V01 usa K01; V02 usa K02; V03 usa K03; V04 usa K04; V05 usa K05; V06 usa K06; V07 usa K07; V08 usa K08; V09 a V13 usam a mesma imagem escolhida do K09; V14 a V17 usam a mesma imagem escolhida do K10.

```text
MAPA K/V
V01: K01
V02: K02
V03: K03
V04: K04
V05: K05
V06: K06
V07: K07
V08: K08
V09: K09
V10: K09
V11: K09
V12: K09
V13: K09
V14: K10
V15: K10
V16: K10
V17: K10
```

## 2. PROMPTS DE IMAGEM (um bloco por K)

### K01 · anexar SÓ `marshall beckett .jpg`

Cena: Gancho: copo de liquidificador colado na lente; ela despeja banana congelada de um saco.

```text
K01
Match the attached image exactly for the woman's identity and outfit: a Japanese-American woman in her seventies with deeply sun-darkened skin, sun spots and dark freckles, deep wrinkles, calm narrow dark eyes, a lean strong build, a white cotton headscarf tied around her forehead with an antique round brass-rimmed diving mask pushed up on top of it, a white cotton wrap jacket tied at the waist with white cotton pants, and a small abalone shell pendant on a black cord. She stands behind a weathered gray wooden plank table under an open shed with a rusted corrugated tin roof on a black lava rock shore in Hawaii: bamboo mats of drying green and dark red seaweed on both sides, a wooden wash tub on the right, turquoise ocean with white surf behind her under an overcast blue-gray sky, and a small American flag tied to the right wooden post, in sharp focus. Hero: on the gray plank table in the lower foreground, very close to the lens, large in frame and closer to the camera than her face: a glass blender jar on its base. She leans toward the camera tipping a clear zip bag of frozen banana slices, the slices tumbling into the jar. She looks straight at the camera, caught mid-sentence, lips naturally parted, animated expression. Vertical smartphone shot, 26mm lens, camera at chest height about one meter from the table, level, front facing. Soft neutral even daylight, true neutral colors, real skin texture with visible pores, smartphone footage look, everything in sharp focus, 9:16 vertical.
```

### K02 · anexar SÓ `marshall beckett .jpg`

Cena: Ela põe uma colher de cacau em pó no liquidificador com banana, colado na lente.

```text
K02
Match the attached image exactly for the woman's identity and outfit: a Japanese-American woman in her seventies with deeply sun-darkened skin, sun spots and dark freckles, deep wrinkles, calm narrow dark eyes, a lean strong build, a white cotton headscarf tied around her forehead with an antique round brass-rimmed diving mask pushed up on top of it, a white cotton wrap jacket tied at the waist with white cotton pants, and a small abalone shell pendant on a black cord. She stands behind a weathered gray wooden plank table under an open shed with a rusted corrugated tin roof on a black lava rock shore in Hawaii: bamboo mats of drying green and dark red seaweed on both sides, a wooden wash tub on the right, turquoise ocean with white surf behind her under an overcast blue-gray sky, and a small American flag tied to the right wooden post, in sharp focus. Hero: on the gray plank table in the lower foreground, very close to the lens, large in frame and closer to the camera than her face: the glass blender jar filled with frozen banana slices. She holds a spoon heaped with dark cocoa powder over it. She looks straight at the camera, caught mid-sentence, lips naturally parted, animated expression. Vertical smartphone shot, 26mm lens, camera at chest height about one meter from the table, level, front facing. Soft neutral even daylight, true neutral colors, real skin texture with visible pores, smartphone footage look, everything in sharp focus, 9:16 vertical.
```

### K03 · anexar SÓ `marshall beckett .jpg`

Cena: Ela solta uma colherada de pasta de amendoim no liquidificador, colado na lente.

```text
K03
Match the attached image exactly for the woman's identity and outfit: a Japanese-American woman in her seventies with deeply sun-darkened skin, sun spots and dark freckles, deep wrinkles, calm narrow dark eyes, a lean strong build, a white cotton headscarf tied around her forehead with an antique round brass-rimmed diving mask pushed up on top of it, a white cotton wrap jacket tied at the waist with white cotton pants, and a small abalone shell pendant on a black cord. She stands behind a weathered gray wooden plank table under an open shed with a rusted corrugated tin roof on a black lava rock shore in Hawaii: bamboo mats of drying green and dark red seaweed on both sides, a wooden wash tub on the right, turquoise ocean with white surf behind her under an overcast blue-gray sky, and a small American flag tied to the right wooden post, in sharp focus. Hero: in the lower foreground, very close to the lens, large in frame and closer to the camera than her face: the glass blender jar of frozen banana slices dusted with cocoa. She drops a thick spoonful of creamy peanut butter from a metal spoon into the jar. She looks straight at the camera, caught mid-sentence, lips naturally parted, animated expression. Vertical smartphone shot, 26mm lens, camera at chest height about one meter from the table, level, front facing. Soft neutral even daylight, true neutral colors, real skin texture with visible pores, smartphone footage look, everything in sharp focus, 9:16 vertical.
```

### K04 · anexar SÓ `marshall beckett .jpg`

Cena: Vista de cima para dentro do liquidificador: creme grosso de chocolate girando, colado na lente.

```text
K04
Match the attached image exactly for the woman's identity and outfit: a Japanese-American woman in her seventies with deeply sun-darkened skin, sun spots and dark freckles, deep wrinkles, calm narrow dark eyes, a lean strong build, a white cotton headscarf tied around her forehead with an antique round brass-rimmed diving mask pushed up on top of it, a white cotton wrap jacket tied at the waist with white cotton pants, and a small abalone shell pendant on a black cord. She stands behind a weathered gray wooden plank table under an open shed with a rusted corrugated tin roof on a black lava rock shore in Hawaii: bamboo mats of drying green and dark red seaweed on both sides, a wooden wash tub on the right, turquoise ocean with white surf behind her under an overcast blue-gray sky, and a small American flag tied to the right wooden post, in sharp focus. Hero: top-down view into the open glass blender jar, very close to the lens, large in frame and closer to the camera than her face: a thick glossy chocolate banana cream swirling around the blade, cocoa specks on the side; she holds the jar with one hand. She looks straight at the camera, caught mid-sentence, lips naturally parted, animated expression. Vertical smartphone shot, 26mm lens, camera at chest height about one meter from the table, level, front facing. Soft neutral even daylight, true neutral colors, real skin texture with visible pores, smartphone footage look, everything in sharp focus, 9:16 vertical.
```

### K05 · anexar SÓ `marshall beckett .jpg`

Cena: Ela despeja um pouco de leite de uma garrafinha de vidro no liquidificador, colado na lente.

```text
K05
Match the attached image exactly for the woman's identity and outfit: a Japanese-American woman in her seventies with deeply sun-darkened skin, sun spots and dark freckles, deep wrinkles, calm narrow dark eyes, a lean strong build, a white cotton headscarf tied around her forehead with an antique round brass-rimmed diving mask pushed up on top of it, a white cotton wrap jacket tied at the waist with white cotton pants, and a small abalone shell pendant on a black cord. She stands behind a weathered gray wooden plank table under an open shed with a rusted corrugated tin roof on a black lava rock shore in Hawaii: bamboo mats of drying green and dark red seaweed on both sides, a wooden wash tub on the right, turquoise ocean with white surf behind her under an overcast blue-gray sky, and a small American flag tied to the right wooden post, in sharp focus. Hero: on the gray plank table in the lower foreground, very close to the lens, large in frame and closer to the camera than her face: the glass blender jar of thick chocolate cream. She pours a splash of milk from a small glass bottle into it. She looks straight at the camera, caught mid-sentence, lips naturally parted, animated expression. Vertical smartphone shot, 26mm lens, camera at chest height about one meter from the table, level, front facing. Soft neutral even daylight, true neutral colors, real skin texture with visible pores, smartphone footage look, everything in sharp focus, 9:16 vertical.
```

### K06 · anexar SÓ `marshall beckett .jpg`

Cena: O liquidificador cheio de sorvete de chocolate grosso na mesa, colado na lente; mão dela no copo.

```text
K06
Match the attached image exactly for the woman's identity and outfit: a Japanese-American woman in her seventies with deeply sun-darkened skin, sun spots and dark freckles, deep wrinkles, calm narrow dark eyes, a lean strong build, a white cotton headscarf tied around her forehead with an antique round brass-rimmed diving mask pushed up on top of it, a white cotton wrap jacket tied at the waist with white cotton pants, and a small abalone shell pendant on a black cord. She stands behind a weathered gray wooden plank table under an open shed with a rusted corrugated tin roof on a black lava rock shore in Hawaii: bamboo mats of drying green and dark red seaweed on both sides, a wooden wash tub on the right, turquoise ocean with white surf behind her under an overcast blue-gray sky, and a small American flag tied to the right wooden post, in sharp focus. Hero: on the gray plank table in the lower foreground, very close to the lens, large in frame and closer to the camera than her face: the glass blender jar full of thick soft chocolate ice cream; her hand rests on the jar. She looks straight at the camera, caught mid-sentence, lips naturally parted, animated expression. Vertical smartphone shot, 26mm lens, camera at chest height about one meter from the table, level, front facing. Soft neutral even daylight, true neutral colors, real skin texture with visible pores, smartphone footage look, everything in sharp focus, 9:16 vertical.
```

### K07 · anexar SÓ `marshall beckett .jpg`

Cena: Vista de cima: ela segura um pote branco com o creme de chocolate sobre o freezer aberto.

```text
K07
Match the attached image exactly for the woman's identity and outfit: a Japanese-American woman in her seventies with deeply sun-darkened skin, sun spots and dark freckles, deep wrinkles, calm narrow dark eyes, a lean strong build, a white cotton headscarf tied around her forehead with an antique round brass-rimmed diving mask pushed up on top of it, a white cotton wrap jacket tied at the waist with white cotton pants, and a small abalone shell pendant on a black cord. She stands behind a weathered gray wooden plank table under an open shed with a rusted corrugated tin roof on a black lava rock shore in Hawaii: bamboo mats of drying green and dark red seaweed on both sides, a wooden wash tub on the right, turquoise ocean with white surf behind her under an overcast blue-gray sky, and a small American flag tied to the right wooden post, in sharp focus. Hero: high top-down view, she holds a small white square container of smooth chocolate cream with both hands, very close to the lens, large in frame and closer to the camera than her face, right above a small open chest freezer beside the table, filled with frozen food bags and an ice tray; she looks up at the camera. She looks straight at the camera, caught mid-sentence, lips naturally parted, animated expression. Vertical smartphone shot, 26mm lens, camera at chest height about one meter from the table, level, front facing. Soft neutral even daylight, true neutral colors, real skin texture with visible pores, smartphone footage look, everything in sharp focus, 9:16 vertical.
```

### K08 · anexar SÓ `marshall beckett .jpg`

Cena: Ela segura uma tigela branca de sorvete de chocolate perto da lente.

```text
K08
Match the attached image exactly for the woman's identity and outfit: a Japanese-American woman in her seventies with deeply sun-darkened skin, sun spots and dark freckles, deep wrinkles, calm narrow dark eyes, a lean strong build, a white cotton headscarf tied around her forehead with an antique round brass-rimmed diving mask pushed up on top of it, a white cotton wrap jacket tied at the waist with white cotton pants, and a small abalone shell pendant on a black cord. She stands behind a weathered gray wooden plank table under an open shed with a rusted corrugated tin roof on a black lava rock shore in Hawaii: bamboo mats of drying green and dark red seaweed on both sides, a wooden wash tub on the right, turquoise ocean with white surf behind her under an overcast blue-gray sky, and a small American flag tied to the right wooden post, in sharp focus. Hero: she holds a round white bowl of creamy chocolate banana ice cream out toward the camera, very close to the lens, large in frame and closer to the camera than her face. She looks straight at the camera, caught mid-sentence, lips naturally parted, animated expression. Vertical smartphone shot, 26mm lens, camera at chest height about one meter from the table, level, front facing. Soft neutral even daylight, true neutral colors, real skin texture with visible pores, smartphone footage look, everything in sharp focus, 9:16 vertical.
```

### K09 · anexar SÓ `marshall beckett .jpg`

Cena: Tigela de sorvete na mesa colada na lente; ela tira uma bola com o boleador de metal.

```text
K09
Match the attached image exactly for the woman's identity and outfit: a Japanese-American woman in her seventies with deeply sun-darkened skin, sun spots and dark freckles, deep wrinkles, calm narrow dark eyes, a lean strong build, a white cotton headscarf tied around her forehead with an antique round brass-rimmed diving mask pushed up on top of it, a white cotton wrap jacket tied at the waist with white cotton pants, and a small abalone shell pendant on a black cord. She stands behind a weathered gray wooden plank table under an open shed with a rusted corrugated tin roof on a black lava rock shore in Hawaii: bamboo mats of drying green and dark red seaweed on both sides, a wooden wash tub on the right, turquoise ocean with white surf behind her under an overcast blue-gray sky, and a small American flag tied to the right wooden post, in sharp focus. Hero: on the gray plank table in the lower foreground, very close to the lens, large in frame and closer to the camera than her face: the round white bowl of creamy chocolate banana ice cream. She digs a metal ice cream scoop into it, lifting a round scoop. She looks straight at the camera, caught mid-sentence, lips naturally parted, animated expression. Vertical smartphone shot, 26mm lens, camera at chest height about one meter from the table, level, front facing. Soft neutral even daylight, true neutral colors, real skin texture with visible pores, smartphone footage look, everything in sharp focus, 9:16 vertical.
```

### K10 · anexar SÓ `marshall beckett .jpg` + `natural_rems_seamoss_produto.jpg`

Cena: Ela segura o pote do Natural Rems Sea Moss colado na lente, rótulo legível, parado.

```text
K10
Match the attached image exactly for the woman's identity and outfit: a Japanese-American woman in her seventies with deeply sun-darkened skin, sun spots and dark freckles, deep wrinkles, calm narrow dark eyes, a lean strong build, a white cotton headscarf tied around her forehead with an antique round brass-rimmed diving mask pushed up on top of it, a white cotton wrap jacket tied at the waist with white cotton pants, and a small abalone shell pendant on a black cord. She stands behind a weathered gray wooden plank table under an open shed with a rusted corrugated tin roof on a black lava rock shore in Hawaii: bamboo mats of drying green and dark red seaweed on both sides, a wooden wash tub on the right, turquoise ocean with white surf behind her under an overcast blue-gray sky, and a small American flag tied to the right wooden post, in sharp focus. Hero: she holds the Natural Rems Sea Moss Gummies jar exactly as in the second attached image: a short wide jar of dark amber plastic with a black screw cap, a pale sage-green label with dark green text, the Natural Rems logo with three leaves, the big title Sea Moss Gummies, a pill-shaped badge reading 6000 MG | 16-IN-1, and the line GREEN APPLE FLAVOR in her right hand out toward the camera, very close to the lens, large in frame and closer to the camera than her face, label fully readable, fingers on the sides, held still. She looks straight at the camera, caught mid-sentence, lips naturally parted, animated expression. Second image: front jar only. Vertical smartphone shot, 26mm lens, camera at chest height about one meter from the table, level, front facing. Soft neutral even daylight, true neutral colors, real skin texture with visible pores, smartphone footage look, everything in sharp focus, 9:16 vertical.
```

## 3. PROMPTS DE VÍDEO (um bloco por V)

### V01 · T1, GANCHO · anexar SÓ a imagem escolhida do K01

Cena: Gancho: copo de liquidificador colado na lente; ela despeja banana congelada de um saco. Fala: "Quantos anos você tinha quando descobriu que se você colocar banana congelada no liquidificador"

```text
V01
The person in the image speaks in American English, looking at the camera: "How old were you when you found out that if you put frozen bananas in a blender"
Fixed camera. Natural lip sync, no music.
```

### V02 · T2, RECEITA · anexar SÓ a imagem escolhida do K02

Cena: Ela põe uma colher de cacau em pó no liquidificador com banana, colado na lente. Fala: "com um pouquinho de cacau em pó"

```text
V02
The person in the image speaks in American English, looking at the camera: "with a little cocoa powder"
Fixed camera. Natural lip sync, no music.
```

### V03 · T3, RECEITA · anexar SÓ a imagem escolhida do K03

Cena: Ela solta uma colherada de pasta de amendoim no liquidificador, colado na lente. Fala: "e pasta de amendoim,"

```text
V03
The person in the image speaks in American English, looking at the camera: "and peanut butter,"
Fixed camera. Natural lip sync, no music.
```

### V04 · T4, RECEITA · anexar SÓ a imagem escolhida do K04

Cena: Vista de cima para dentro do liquidificador: creme grosso de chocolate girando, colado na lente. Fala: "e bater até ficar completamente liso, você consegue transformar isso num sorvete cremoso de chocolate?"

```text
V04
The person in the image speaks in American English, looking at the camera: "and blend it until it's completely smooth, you can turn it into creamy chocolate ice cream?"
Fixed camera. Natural lip sync, no music.
```

### V05 · T5, RECEITA · anexar SÓ a imagem escolhida do K05

Cena: Ela despeja um pouco de leite de uma garrafinha de vidro no liquidificador, colado na lente. Fala: "Coloque um pouquinho de leite"

```text
V05
The person in the image speaks in American English, looking at the camera: "Add a splash of milk"
Fixed camera. Natural lip sync, no music.
```

### V06 · T6, RECEITA · anexar SÓ a imagem escolhida do K06

Cena: O liquidificador cheio de sorvete de chocolate grosso na mesa, colado na lente; mão dela no copo. Fala: "e bata tudo junto até ficar como um sorvete de chocolate macio, bem grosso."

```text
V06
The person in the image speaks in American English, looking at the camera: "and blend it all together until it's like soft chocolate ice cream, really thick."
Fixed camera. Natural lip sync, no music.
```

### V07 · T7, RECEITA · anexar SÓ a imagem escolhida do K07

Cena: Vista de cima: ela segura um pote branco com o creme de chocolate sobre o freezer aberto. Fala: "Passe para um pote pequeno e coloque no freezer por uns trinta minutos."

```text
V07
The person in the image speaks in American English, looking at the camera: "Pour it into a small container and put it in the freezer for about thirty minutes."
Fixed camera. Natural lip sync, no music.
```

### V08 · T8, RECEITA · anexar SÓ a imagem escolhida do K08

Cena: Ela segura uma tigela branca de sorvete de chocolate perto da lente. Fala: "Depois sirva numa tigela."

```text
V08
The person in the image speaks in American English, looking at the camera: "Then serve it in a bowl."
Fixed camera. Natural lip sync, no music.
```

### V09 · T9, RESULTADO · anexar SÓ a imagem escolhida do K09

Cena: Tigela de sorvete na mesa colada na lente; ela tira uma bola com o boleador de metal. Fala: "Você ganha um sorvete cremoso de chocolate que não só tem gosto de sorveteria, ele é cheio de potássio"

```text
V09
The person in the image speaks in American English, looking at the camera: "You get a creamy chocolate ice cream that doesn't just taste like the one from the ice cream shop, it's packed with potassium"
Fixed camera. Natural lip sync, no music.
```

### V10 · T10, RESULTADO · anexar SÓ a imagem escolhida do K09

Cena: Tigela de sorvete na mesa colada na lente; ela tira uma bola com o boleador de metal. Fala: "e é feito sem todo o açúcar refinado que o sorvete costuma ter. Sem açúcar refinado, sem esforço, só banana."

```text
V10
The person in the image speaks in American English, looking at the camera: "and made without all the refined sugar ice cream usually has. No refined sugar, no effort, just bananas."
Fixed camera. Natural lip sync, no music.
```

### V11 · T11, VIRADA: O LADO RUIM DA RECEITA · anexar SÓ a imagem escolhida do K09

Cena: Tigela de sorvete na mesa colada na lente; ela tira uma bola com o boleador de metal. Fala: "Tá, um pouquinho de esforço. Você congela as bananas na noite anterior, briga com o liquidificador e espera trinta minutos quando a vontade é agora."

```text
V11
The person in the image speaks in American English, looking at the camera: "Okay, a little effort. You freeze the bananas the night before, fight the blender, and wait thirty minutes when the craving is right now."
Fixed camera. Natural lip sync, no music.
```

### V12 · T12, CATEGORIA + AUTORIDADE · anexar SÓ a imagem escolhida do K09

Cena: Tigela de sorvete na mesa colada na lente; ela tira uma bola com o boleador de metal. Fala: "Então nessas noites eu mastigo uma goma de maçã verde no lugar. É sea moss, a planta atrás da qual eu mergulho desde menina."

```text
V12
The person in the image speaks in American English, looking at the camera: "So on those nights I chew one green apple gummy instead. It is sea moss, the plant I have dived for since I was a girl."
Fixed camera. Natural lip sync, no music.
```

### V13 · T13, OBSTÁCULO · anexar SÓ a imagem escolhida do K09

Cena: Tigela de sorvete na mesa colada na lente; ela tira uma bola com o boleador de metal. Fala: "Mas cuidado, a maioria das gomas de sea moss é só bala, carregada do mesmo açúcar refinado que este sorvete foi feito para evitar."

```text
V13
The person in the image speaks in American English, looking at the camera: "But careful, most sea moss gummies are just candy, loaded with the same refined sugar this ice cream was made to avoid."
Fixed camera. Natural lip sync, no music.
```

### V14 · T14, PRODUTO NO GESTO · anexar SÓ a imagem escolhida do K10

Cena: Ela segura o pote do Natural Rems Sea Moss colado na lente, rótulo legível, parado. Fala: "A que eu confio é a Natural Rems Sea Moss. Sea moss irlandês selvagem e dezesseis ingredientes, com menos de um grama de açúcar e quatro calorias."

```text
V14
The person in the image speaks in American English, looking at the camera: "The one I trust is Natural Rems Sea Moss. Wild Irish sea moss and sixteen ingredients, with less than one gram of sugar and four calories."
Fixed camera. Natural lip sync, no music.
```

### V15 · T15, COMENTÁRIO · anexar SÓ a imagem escolhida do K10

Cena: Ela segura o pote do Natural Rems Sea Moss colado na lente, rótulo legível, parado. Fala: "Comenta yes se essa vontade de doce te pega toda noite, pra eu saber quem precisa da minha próxima receita."

```text
V15
The person in the image speaks in American English, looking at the camera: "Comment yes if that sweet tooth gets you every night, so I know who needs my next recipe."
Fixed camera. Natural lip sync, no music.
```

### V16 · T16, CTA AMAZON + DESTINO · anexar SÓ a imagem escolhida do K10

Cena: Ela segura o pote do Natural Rems Sea Moss colado na lente, rótulo legível, parado. Fala: "Procure Natural Rems Sea Moss na Amazon. Ou toque na minha foto de perfil, o link está te esperando nos meus stories, ou bem ali na minha bio."

```text
V16
The person in the image speaks in American English, looking at the camera: "Search Natural Rems Sea Moss on Amazon. Or tap my profile picture, the link is waiting in my stories, or right there in my bio."
Fixed camera. Natural lip sync, no music.
```

### V17 · T17, FOLLOW · anexar SÓ a imagem escolhida do K10

Cena: Ela segura o pote do Natural Rems Sea Moss colado na lente, rótulo legível, parado. Fala: "E não esquece de apertar o botão de seguir."

```text
V17
The person in the image speaks in American English, looking at the camera: "And don't forget to hit that follow button."
Fixed camera. Natural lip sync, no music.
```

## 4. Transcrição final

| Take | English | Português |
|---|---|---|
| T1 | How old were you when you found out that if you put frozen bananas in a blender | Quantos anos você tinha quando descobriu que se você colocar banana congelada no liquidificador |
| T2 | with a little cocoa powder | com um pouquinho de cacau em pó |
| T3 | and peanut butter, | e pasta de amendoim, |
| T4 | and blend it until it's completely smooth, you can turn it into creamy chocolate ice cream? | e bater até ficar completamente liso, você consegue transformar isso num sorvete cremoso de chocolate? |
| T5 | Add a splash of milk | Coloque um pouquinho de leite |
| T6 | and blend it all together until it's like soft chocolate ice cream, really thick. | e bata tudo junto até ficar como um sorvete de chocolate macio, bem grosso. |
| T7 | Pour it into a small container and put it in the freezer for about thirty minutes. | Passe para um pote pequeno e coloque no freezer por uns trinta minutos. |
| T8 | Then serve it in a bowl. | Depois sirva numa tigela. |
| T9 | You get a creamy chocolate ice cream that doesn't just taste like the one from the ice cream shop, it's packed with potassium | Você ganha um sorvete cremoso de chocolate que não só tem gosto de sorveteria, ele é cheio de potássio |
| T10 | and made without all the refined sugar ice cream usually has. No refined sugar, no effort, just bananas. | e é feito sem todo o açúcar refinado que o sorvete costuma ter. Sem açúcar refinado, sem esforço, só banana. |
| T11 | Okay, a little effort. You freeze the bananas the night before, fight the blender, and wait thirty minutes when the craving is right now. | Tá, um pouquinho de esforço. Você congela as bananas na noite anterior, briga com o liquidificador e espera trinta minutos quando a vontade é agora. |
| T12 | So on those nights I chew one green apple gummy instead. It is sea moss, the plant I have dived for since I was a girl. | Então nessas noites eu mastigo uma goma de maçã verde no lugar. É sea moss, a planta atrás da qual eu mergulho desde menina. |
| T13 | But careful, most sea moss gummies are just candy, loaded with the same refined sugar this ice cream was made to avoid. | Mas cuidado, a maioria das gomas de sea moss é só bala, carregada do mesmo açúcar refinado que este sorvete foi feito para evitar. |
| T14 | The one I trust is Natural Rems Sea Moss. Wild Irish sea moss and sixteen ingredients, with less than one gram of sugar and four calories. | A que eu confio é a Natural Rems Sea Moss. Sea moss irlandês selvagem e dezesseis ingredientes, com menos de um grama de açúcar e quatro calorias. |
| T15 | Comment yes if that sweet tooth gets you every night, so I know who needs my next recipe. | Comenta yes se essa vontade de doce te pega toda noite, pra eu saber quem precisa da minha próxima receita. |
| T16 | Search Natural Rems Sea Moss on Amazon. Or tap my profile picture, the link is waiting in my stories, or right there in my bio. | Procure Natural Rems Sea Moss na Amazon. Ou toque na minha foto de perfil, o link está te esperando nos meus stories, ou bem ali na minha bio. |
| T17 | And don't forget to hit that follow button. | E não esquece de apertar o botão de seguir. |

**EN corrido:** How old were you when you found out that if you put frozen bananas in a blender with a little cocoa powder and peanut butter, and blend it until it's completely smooth, you can turn it into creamy chocolate ice cream? Add a splash of milk and blend it all together until it's like soft chocolate ice cream, really thick. Pour it into a small container and put it in the freezer for about thirty minutes. Then serve it in a bowl. You get a creamy chocolate ice cream that doesn't just taste like the one from the ice cream shop, it's packed with potassium and made without all the refined sugar ice cream usually has. No refined sugar, no effort, just bananas. Okay, a little effort. You freeze the bananas the night before, fight the blender, and wait thirty minutes when the craving is right now. So on those nights I chew one green apple gummy instead. It is sea moss, the plant I have dived for since I was a girl. But careful, most sea moss gummies are just candy, loaded with the same refined sugar this ice cream was made to avoid. The one I trust is Natural Rems Sea Moss. Wild Irish sea moss and sixteen ingredients, with less than one gram of sugar and four calories. Comment yes if that sweet tooth gets you every night, so I know who needs my next recipe. Search Natural Rems Sea Moss on Amazon. Or tap my profile picture, the link is waiting in my stories, or right there in my bio. And don't forget to hit that follow button.

**PT corrido:** Quantos anos você tinha quando descobriu que se você colocar banana congelada no liquidificador com um pouquinho de cacau em pó e pasta de amendoim, e bater até ficar completamente liso, você consegue transformar isso num sorvete cremoso de chocolate? Coloque um pouquinho de leite e bata tudo junto até ficar como um sorvete de chocolate macio, bem grosso. Passe para um pote pequeno e coloque no freezer por uns trinta minutos. Depois sirva numa tigela. Você ganha um sorvete cremoso de chocolate que não só tem gosto de sorveteria, ele é cheio de potássio e é feito sem todo o açúcar refinado que o sorvete costuma ter. Sem açúcar refinado, sem esforço, só banana. Tá, um pouquinho de esforço. Você congela as bananas na noite anterior, briga com o liquidificador e espera trinta minutos quando a vontade é agora. Então nessas noites eu mastigo uma goma de maçã verde no lugar. É sea moss, a planta atrás da qual eu mergulho desde menina. Mas cuidado, a maioria das gomas de sea moss é só bala, carregada do mesmo açúcar refinado que este sorvete foi feito para evitar. A que eu confio é a Natural Rems Sea Moss. Sea moss irlandês selvagem e dezesseis ingredientes, com menos de um grama de açúcar e quatro calorias. Comenta yes se essa vontade de doce te pega toda noite, pra eu saber quem precisa da minha próxima receita. Procure Natural Rems Sea Moss na Amazon. Ou toque na minha foto de perfil, o link está te esperando nos meus stories, ou bem ali na minha bio. E não esquece de apertar o botão de seguir.
