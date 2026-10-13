# ENTREGA | Meredith Callahan | Sea Moss Venda · pilha de notícia · seios

flow_seguro: v1

Produção `meredith_seamoss_seios_noticia` · Ângulo 1 Sea Moss (conta da Meredith) · VENDA · rodada de VALIDAÇÃO · formato mínimo de prompt do Flow

## 0. INSTRUÇÕES PARA A MEMÓRIA DO AGENTE · GOOGLE FLOW (colar inteiro antes do primeiro K)

```text
# Agente do Flow, produção atual: Sea Moss Venda · pilha de notícia · seios

Você é o executor do Google Flow. Você só gera imagens e vídeos a partir de prompts prontos. Você não cria, não edita e não melhora prompt.

## Produção atual
- Conta: Natural Rems Sea Moss (Meredith), vídeo de venda. Sea Moss Venda · pilha de notícia · seios.
- Um avatar só: a senhora de turbante verde e amarelo, blusa creme e avental laranja (arquivo `meredith callahan .png`). Imagens K01 a K03; vídeos V01 a V21.

## O que é anexado (só isto, nada mais)
- IMAGEM (K): anexe só a imagem da avatar e cole o prompt.
- EXCEÇÃO K01: NÃO anexe nenhuma imagem, só cole o prompt.
- EXCEÇÃO K03: anexe `meredith callahan .png` e `natural_rems_seamoss_produto.jpg` (nesta ordem).
- VÍDEO (V): anexe só a imagem que o operador escolheu do K indicado e cole o prompt de vídeo.
- Não existe frame modelo. Segunda imagem só quando uma EXCEÇÃO acima pedir. Cenário, pose, câmera e objeto já estão escritos em cada prompt. Pare só se faltar a imagem da avatar (K que pede a avatar) ou a imagem escolhida (V).

## Imagens (K01 a K03)
1. Modelo: Nano Banana 2.1. Formato: 9:16 vertical.
2. Gere 4 variações por prompt. Confira o 4 e o 9:16 antes de CADA K, porque a tela volta sozinha para 1.
3. Cole o parágrafo inteiro, sem o código K, sem resumir, sem alterar uma palavra.
4. Nomeie as quatro: `K01-1`, `K01-2`, `K01-3`, `K01-4`.
5. Se saírem menos de 4, ou formato diferente de 9:16, gere de novo com o MESMO prompt e a MESMA imagem até existirem 4 em 9:16.
6. Gere todos os K e PARE. Avise: "K01 a K03 prontos, 4 por K. Aguardando sua escolha." Não escolha, não apague e não gere vídeo.
7. O operador apaga 3 de cada K e deixa 1 escolhida a dedo. Nunca questione e nunca recrie uma imagem apagada.

## Vídeos (V01 a V21)
1. Só começa quando o operador mandar. Mapa: V01 usa K01; V02 a V14 usam todos a mesma imagem escolhida do K02; V15 a V21 usam todos a mesma imagem escolhida do K03. Se o K tiver mais de uma imagem ou nenhuma, pare e pergunte qual.
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

**Vídeo: pilha de notícia, a pior comida para os seios (laticínio).**

**O que acontece:** abre num telejornal de emissora inventada (a âncora noticia que um vídeo viralizou). Corta para Meredith Callahan no cenário fixo da conta, que elimina três suspeitos, absolve, explica o mecanismo, revela o vilão, vira para a causa raiz e, com o pote na mão, apresenta o Natural Rems Sea Moss. Fecha com comment yes, Amazon, Stories e bio, e o lembrete do follow.

**Gancho:** a âncora do telejornal com a imagem de choque e a faixa BREAKING NEWS.

## 1. Anexos e mapa

- **Imagem (K):** anexar SÓ o que o título de cada K indica (padrão: a imagem da avatar, `meredith callahan .png`) e colar o prompt. 4 variações, 9:16. Nada de frame do modelo.
- **Vídeo (V):** anexar SÓ a imagem escolhida do K indicado no mapa e colar o prompt de vídeo. 1 variação, 9:16.
- Bloco do agente Flow desta produção: `AGENTE_FLOW.md`.

V01 usa K01; V02 a V14 usam a mesma imagem escolhida do K02; V15 a V21 usam a mesma imagem escolhida do K03.

```text
MAPA K/V
V01: K01
V02: K02
V03: K02
V04: K02
V05: K02
V06: K02
V07: K02
V08: K02
V09: K02
V10: K02
V11: K02
V12: K02
V13: K02
V14: K02
V15: K03
V16: K03
V17: K03
V18: K03
V19: K03
V20: K03
V21: K03
```

## 2. PROMPTS DE IMAGEM (um bloco por K)

### K01 · anexar SÓ nenhuma imagem (só o texto)

Cena: Telejornal de emissora inventada: âncora na bancada, skyline noturno, caixa de imagem de choque, faixa BREAKING NEWS.

```text
K01
Television news studio frame, vertical 9:16. A news anchor woman in her late forties with a sleek blonde bob, a sage-green blazer over a black top, seated at a glossy news desk with her hands resting on a few papers, looking straight into the camera, caught mid-sentence with lips naturally parted. Behind her a large window wall shows a city skyline at blue hour, deep blue sky with lit towers. On the left, a large inset photo box beside her showing a close-up photo of two big round green coconuts hanging side by side from the top of a palm trunk, under the palm fronds, a funny suggestive shape, filling about a third of the frame. Across the bottom a red lower-third banner reads BREAKING NEWS in bold white letters with a white strip reading HEALTH ALERT. A small American flag stands on the desk at the right, in sharp focus. Broadcast camera at eye level, 35mm lens, front facing, medium shot from the chest up. Clean even studio light, true neutral colors, real skin texture with visible pores, everything in sharp focus, 9:16 vertical.
```

### K02 · anexar SÓ `meredith callahan .png`

Cena: Meredith Callahan no cenário fixo da conta falando, mão direita erguida com o indicador para cima perto da lente.

```text
K02
Match the attached image exactly for the woman's identity and outfit: a woman around seventy with deep brown skin, dark freckles on her cheekbones, deep laugh lines, gold-capped front teeth, silver-gray locs piled high inside a tall emerald-green and saffron-yellow patterned head wrap, red reading glasses resting on the front of the wrap, large gold bamboo hoop earrings, a stack of thin gold bangles on her left wrist, a loose cream cotton short-sleeve blouse with green leaf embroidery at the neckline, and a rust-orange apron tied at the waist. She stands behind a mint-green speckled Formica kitchen table in her small Brooklyn apartment kitchen: wooden cabinets, a row of large glass jars of pale golden sea moss and a glass blender on the counter at the left, a window at the right showing a red brick building with black iron balconies under an overcast blue-gray sky, and a small American flag in a potted plant on the windowsill, in sharp focus. Hero: her right hand raised in the lower foreground, very close to the lens, large in frame and closer to the camera than her face, index finger pointing up as she makes a point. She looks straight at the camera, caught mid-sentence, lips naturally parted, serious and animated expression. Vertical smartphone shot, 26mm lens, camera at chest height about one meter from the table, level, front facing. Soft neutral even daylight, true neutral colors, real skin texture with visible pores, smartphone footage look, everything in sharp focus, 9:16 vertical.
```

### K03 · anexar SÓ `meredith callahan .png` + `natural_rems_seamoss_produto.jpg`

Cena: Meredith Callahan no mesmo plano segurando o frasco do Natural Rems Sea Moss colado na lente, rótulo legível.

```text
K03
Match the attached image exactly for the woman's identity and outfit: a woman around seventy with deep brown skin, dark freckles on her cheekbones, deep laugh lines, gold-capped front teeth, silver-gray locs piled high inside a tall emerald-green and saffron-yellow patterned head wrap, red reading glasses resting on the front of the wrap, large gold bamboo hoop earrings, a stack of thin gold bangles on her left wrist, a loose cream cotton short-sleeve blouse with green leaf embroidery at the neckline, and a rust-orange apron tied at the waist. She stands behind a mint-green speckled Formica kitchen table in her small Brooklyn apartment kitchen: wooden cabinets, a row of large glass jars of pale golden sea moss and a glass blender on the counter at the left, a window at the right showing a red brick building with black iron balconies under an overcast blue-gray sky, and a small American flag in a potted plant on the windowsill, in sharp focus. Hero: she holds the Natural Rems Sea Moss Gummies jar exactly as in the second attached image: a short wide jar of dark amber plastic with a black screw cap, a pale sage-green label with dark green text, the Natural Rems logo with three leaves, the big title Sea Moss Gummies, a pill-shaped badge reading 6000 MG | 16-IN-1, and the line GREEN APPLE FLAVOR in her right hand out toward the camera, very close to the lens, large in frame and closer to the camera than her face, label fully readable, fingers on the sides. {MID} {REF_POTE} Vertical smartphone shot, 26mm lens, camera at chest height about one meter from the table, level, front facing. Soft neutral even daylight, true neutral colors, real skin texture with visible pores, smartphone footage look, everything in sharp focus, 9:16 vertical.
```

## 3. PROMPTS DE VÍDEO (um bloco por V)

### V01 · T1, Âncora de telejornal · anexar SÓ a imagem escolhida do K01

Cena: A âncora dá a notícia. Fala: "Últimas notícias desta noite. Um vídeo do Brooklyn está explodindo depois que ela revelou a comida mais venenosa para os seios de uma mulher, e ela está em toda cozinha. Assista."

```text
V01
The person in the image speaks in American English, looking at the camera: "Breaking news tonight. A clip from Brooklyn is blowing up after she named the most poisonous food for a woman's breasts, and it is in every kitchen. Just watch."
Fixed camera. Natural lip sync, no music.
```

### V02 · T2, Eliminação tripla · anexar SÓ a imagem escolhida do K02

Cena: Ela fala para a câmera. Fala: "Não é o hambúrguer, meu bem. Não é a pizza. E não, nem é o sorvete do seu freezer."

```text
V02
The person in the image speaks in American English, looking at the camera: "It is not the burgers, baby. It is not the pizza. And no, it is not even the ice cream in your freezer."
Fixed camera. Natural lip sync, no music.
```

### V03 · T3, Proximidade · anexar SÓ a imagem escolhida do K02

Cena: Ela fala para a câmera. Fala: "É algo pior, escondido à vista de todos na prateleira da sua geladeira, e você pega isso todo santo dia."

```text
V03
The person in the image speaks in American English, looking at the camera: "It is something worse, hiding in plain sight on the shelf of your fridge, and you reach for it every single day."
Fixed camera. Natural lip sync, no music.
```

### V04 · T4, Absolvição · anexar SÓ a imagem escolhida do K02

Cena: Ela fala para a câmera. Fala: "E se você come, a culpa não é sua, filha. Os comerciais te disseram a vida inteira que fazia bem."

```text
V04
The person in the image speaks in American English, looking at the camera: "And if you eat it, that is not your fault, child. The commercials told you your whole life it was good for you."
Fixed camera. Natural lip sync, no music.
```

### V05 · T5, Ordem de assistir · anexar SÓ a imagem escolhida do K02

Cena: Ela fala para a câmera. Fala: "Então senta comigo um minuto, porque o que eu vou te contar ninguém me contou."

```text
V05
The person in the image speaks in American English, looking at the camera: "So you sit with me for one minute, because what I am about to tell you nobody told me."
Fixed camera. Natural lip sync, no music.
```

### V06 · T6, Mecanismo · anexar SÓ a imagem escolhida do K02

Cena: Ela fala para a câmera. Fala: "Ela carrega hormônios e fatores de crescimento, e no momento em que eles entram no seu corpo, o corpo responde com inflamação."

```text
V06
The person in the image speaks in American English, looking at the camera: "It carries hormones and growth factors, and the moment they get into your body, your body answers with inflammation."
Fixed camera. Natural lip sync, no music.
```

### V07 · T7, Mecanismo · anexar SÓ a imagem escolhida do K02

Cena: Ela fala para a câmera. Fala: "Essa inflamação ataca o colágeno e o tecido conjuntivo, justamente o que mantém o seu peito firme e cheio."

```text
V07
The person in the image speaks in American English, looking at the camera: "That inflammation goes after the collagen and the connective tissue, the very things that keep your chest firm and full."
Fixed camera. Natural lip sync, no music.
```

### V08 · T8, Mecanismo · anexar SÓ a imagem escolhida do K02

Cena: Ela fala para a câmera. Fala: "Além disso, ela é cheia de antibiótico e de coisa para a qual o seu corpo nunca foi feito, e os seus hormônios saem do equilíbrio."

```text
V08
The person in the image speaks in American English, looking at the camera: "On top of that, it is full of antibiotics and things your body was never built for, and your hormones get thrown off balance."
Fixed camera. Natural lip sync, no music.
```

### V09 · T9, Mecanismo · anexar SÓ a imagem escolhida do K02

Cena: Ela fala para a câmera. Fala: "E aquele cálcio que te prometeram? O seu corpo mal segura ele. Você fica com todos os hormônios e nada do lado bom."

```text
V09
The person in the image speaks in American English, looking at the camera: "And that calcium they promised you? Your body barely holds on to it. You get all the hormones and none of the good."
Fixed camera. Natural lip sync, no music.
```

### V10 · T10, Revelação do vilão · anexar SÓ a imagem escolhida do K02

Cena: Ela fala para a câmera. Fala: "Ainda não sabe de que comida eu falo? É o laticínio, meu bem. O leite, o queijo, o creme, tudo."

```text
V10
The person in the image speaks in American English, looking at the camera: "Still do not know what food I mean? It is dairy, baby. The milk, the cheese, the cream, all of it."
Fixed camera. Natural lip sync, no music.
```

### V11 · T11, Sintoma visível · anexar SÓ a imagem escolhida do K02

Cena: Ela fala para a câmera. Fala: "Quando você está inflamada por dentro, o colágeno se desfaz, a pele do peito fica fina, e a firmeza vai embora."

```text
V11
The person in the image speaks in American English, looking at the camera: "When you are inflamed on the inside, the collagen breaks down, the skin on your chest gets thin, and the firmness goes."
Fixed camera. Natural lip sync, no music.
```

### V12 · T12, Sintoma visível · anexar SÓ a imagem escolhida do K02

Cena: Ela fala para a câmera. Fala: "E não importa o sutiã que você compra ou quanto peso você perde. Você evita certas blusas, e tem pavor do espelho."

```text
V12
The person in the image speaks in American English, looking at the camera: "And it does not matter what bra you buy or how much weight you lose. You skip certain tops, and you dread the mirror."
Fixed camera. Natural lip sync, no music.
```

### V13 · T13, Absolvição + causa · anexar SÓ a imagem escolhida do K02

Cena: Ela fala para a câmera. Fala: "E aí você se culpa, quando nunca foi você. Não é a gravidade e não é a idade. É inflamação, de dentro para fora. [fala real do take]"

```text
V13
The person in the image speaks in American English, looking at the camera: "And then you blame yourself, when it was never you. It is not gravity and it is not age. It is inflammation, from the inside."
Fixed camera. Natural lip sync, no music.
```

### V14 · T14, Virada · anexar SÓ a imagem escolhida do K02

Cena: Ela fala para a câmera. Fala: "Mas a boa notícia, meu bem. O seu corpo sabe se cuidar quando você dá a ele o apoio certo."

```text
V14
The person in the image speaks in American English, looking at the camera: "But here is the good news, baby. Your body knows how to take care of itself when you give it the right support."
Fixed camera. Natural lip sync, no music.
```

### V15 · T15, Autoridade e exclusividade · anexar SÓ a imagem escolhida do K03

Cena: Ela segura o pote parado, rótulo legível. Fala: "Quarenta anos fazendo sea moss para toda mulher deste quarteirão, e tem uma coisa que eu deixo na minha própria bancada. [fala real do take]"

```text
V15
The person in the image speaks in American English, looking at the camera: "Forty years making sea moss for every woman on this block, and there is one thing I keep on my own counter."
Fixed camera. Natural lip sync, no music.
```

### V16 · T16, Ingrediente antes da marca · anexar SÓ a imagem escolhida do K03

Cena: Ela segura o pote parado, rótulo legível. Fala: "Vitamina C, que apoia a formação normal de colágeno, cúrcuma com pimenta-do-reino, gengibre e sea moss irlandês selvagem. Dezesseis numa goma. Natural Rems Sea Moss."

```text
V16
The person in the image speaks in American English, looking at the camera: "Vitamin C, which supports normal collagen formation, turmeric with black pepper, ginger, and wild Irish sea moss. Sixteen in one gummy. Natural Rems Sea Moss."
Fixed camera. Natural lip sync, no music.
```

### V17 · T17, Benefício do rótulo · anexar SÓ a imagem escolhida do K03

Cena: Ela segura o pote parado, rótulo legível. Fala: "Então você está cuidando da sua pele de dentro para fora, e quando você se sente bem no seu corpo, até se vestir fica diferente."

```text
V17
The person in the image speaks in American English, looking at the camera: "So you are supporting your skin from the inside out, and when you feel good in your body, even getting dressed feels different."
Fixed camera. Natural lip sync, no music.
```

### V18 · T18, Fricção + custo · anexar SÓ a imagem escolhida do K03

Cena: Ela segura o pote parado, rótulo legível. Fala: "Uma goma de maçã verde toda manhã no café, você mastiga e é só isso. Sem panela no fogão, sem dezesseis frascos."

```text
V18
The person in the image speaks in American English, looking at the camera: "One green apple gummy every morning at breakfast, you chew it, and that is all. No pot on the stove, no sixteen bottles."
Fixed camera. Natural lip sync, no music.
```

### V19 · T19, Comentário · anexar SÓ a imagem escolhida do K03

Cena: Ela segura o pote parado, rótulo legível. Fala: "Comenta yes se tem leite ou queijo na sua geladeira hoje, e eu faço um vídeo de como eu começo as minhas manhãs."

```text
V19
The person in the image speaks in American English, looking at the camera: "Comment yes if there is milk or cheese in your fridge tonight, and I will make you a video on how I start my mornings."
Fixed camera. Natural lip sync, no music.
```

### V20 · T20, Cta amazon + destino · anexar SÓ a imagem escolhida do K03

Cena: Ela segura o pote parado, rótulo legível. Fala: "Procure Natural Rems Sea Moss na Amazon. Ou toque na minha foto de perfil, o link está te esperando nos meus stories, ou bem ali na minha bio."

```text
V20
The person in the image speaks in American English, looking at the camera: "Search Natural Rems Sea Moss on Amazon. Or tap my profile picture, the link is waiting in my stories, or right there in my bio."
Fixed camera. Natural lip sync, no music.
```

### V21 · T21, Follow · anexar SÓ a imagem escolhida do K03

Cena: Ela segura o pote parado, rótulo legível. Fala: "E não esquece de apertar o botão de seguir."

```text
V21
The person in the image speaks in American English, looking at the camera: "And don't forget to hit that follow button."
Fixed camera. Natural lip sync, no music.
```

## 4. Transcrição final

| Take | English | Português |
|---|---|---|
| T1 | Breaking news tonight. A clip from Brooklyn is blowing up after she named the most poisonous food for a woman's breasts, and it is in every kitchen. Just watch. | Últimas notícias desta noite. Um vídeo do Brooklyn está explodindo depois que ela revelou a comida mais venenosa para os seios de uma mulher, e ela está em toda cozinha. Assista. |
| T2 | It is not the burgers, baby. It is not the pizza. And no, it is not even the ice cream in your freezer. | Não é o hambúrguer, meu bem. Não é a pizza. E não, nem é o sorvete do seu freezer. |
| T3 | It is something worse, hiding in plain sight on the shelf of your fridge, and you reach for it every single day. | É algo pior, escondido à vista de todos na prateleira da sua geladeira, e você pega isso todo santo dia. |
| T4 | And if you eat it, that is not your fault, child. The commercials told you your whole life it was good for you. | E se você come, a culpa não é sua, filha. Os comerciais te disseram a vida inteira que fazia bem. |
| T5 | So you sit with me for one minute, because what I am about to tell you nobody told me. | Então senta comigo um minuto, porque o que eu vou te contar ninguém me contou. |
| T6 | It carries hormones and growth factors, and the moment they get into your body, your body answers with inflammation. | Ela carrega hormônios e fatores de crescimento, e no momento em que eles entram no seu corpo, o corpo responde com inflamação. |
| T7 | That inflammation goes after the collagen and the connective tissue, the very things that keep your chest firm and full. | Essa inflamação ataca o colágeno e o tecido conjuntivo, justamente o que mantém o seu peito firme e cheio. |
| T8 | On top of that, it is full of antibiotics and things your body was never built for, and your hormones get thrown off balance. | Além disso, ela é cheia de antibiótico e de coisa para a qual o seu corpo nunca foi feito, e os seus hormônios saem do equilíbrio. |
| T9 | And that calcium they promised you? Your body barely holds on to it. You get all the hormones and none of the good. | E aquele cálcio que te prometeram? O seu corpo mal segura ele. Você fica com todos os hormônios e nada do lado bom. |
| T10 | Still do not know what food I mean? It is dairy, baby. The milk, the cheese, the cream, all of it. | Ainda não sabe de que comida eu falo? É o laticínio, meu bem. O leite, o queijo, o creme, tudo. |
| T11 | When you are inflamed on the inside, the collagen breaks down, the skin on your chest gets thin, and the firmness goes. | Quando você está inflamada por dentro, o colágeno se desfaz, a pele do peito fica fina, e a firmeza vai embora. |
| T12 | And it does not matter what bra you buy or how much weight you lose. You skip certain tops, and you dread the mirror. | E não importa o sutiã que você compra ou quanto peso você perde. Você evita certas blusas, e tem pavor do espelho. |
| T13 | And then you blame yourself, when it was never you. It is not gravity and it is not age. It is inflammation, from the inside. | E aí você se culpa, quando nunca foi você. Não é a gravidade e não é a idade. É inflamação, de dentro para fora. [fala real do take] |
| T14 | But here is the good news, baby. Your body knows how to take care of itself when you give it the right support. | Mas a boa notícia, meu bem. O seu corpo sabe se cuidar quando você dá a ele o apoio certo. |
| T15 | Forty years making sea moss for every woman on this block, and there is one thing I keep on my own counter. | Quarenta anos fazendo sea moss para toda mulher deste quarteirão, e tem uma coisa que eu deixo na minha própria bancada. [fala real do take] |
| T16 | Vitamin C, which supports normal collagen formation, turmeric with black pepper, ginger, and wild Irish sea moss. Sixteen in one gummy. Natural Rems Sea Moss. | Vitamina C, que apoia a formação normal de colágeno, cúrcuma com pimenta-do-reino, gengibre e sea moss irlandês selvagem. Dezesseis numa goma. Natural Rems Sea Moss. |
| T17 | So you are supporting your skin from the inside out, and when you feel good in your body, even getting dressed feels different. | Então você está cuidando da sua pele de dentro para fora, e quando você se sente bem no seu corpo, até se vestir fica diferente. |
| T18 | One green apple gummy every morning at breakfast, you chew it, and that is all. No pot on the stove, no sixteen bottles. | Uma goma de maçã verde toda manhã no café, você mastiga e é só isso. Sem panela no fogão, sem dezesseis frascos. |
| T19 | Comment yes if there is milk or cheese in your fridge tonight, and I will make you a video on how I start my mornings. | Comenta yes se tem leite ou queijo na sua geladeira hoje, e eu faço um vídeo de como eu começo as minhas manhãs. |
| T20 | Search Natural Rems Sea Moss on Amazon. Or tap my profile picture, the link is waiting in my stories, or right there in my bio. | Procure Natural Rems Sea Moss na Amazon. Ou toque na minha foto de perfil, o link está te esperando nos meus stories, ou bem ali na minha bio. |
| T21 | And don't forget to hit that follow button. | E não esquece de apertar o botão de seguir. |

**EN corrido:** Breaking news tonight. A clip from Brooklyn is blowing up after she named the most poisonous food for a woman's breasts, and it is in every kitchen. Just watch. It is not the burgers, baby. It is not the pizza. And no, it is not even the ice cream in your freezer. It is something worse, hiding in plain sight on the shelf of your fridge, and you reach for it every single day. And if you eat it, that is not your fault, child. The commercials told you your whole life it was good for you. So you sit with me for one minute, because what I am about to tell you nobody told me. It carries hormones and growth factors, and the moment they get into your body, your body answers with inflammation. That inflammation goes after the collagen and the connective tissue, the very things that keep your chest firm and full. On top of that, it is full of antibiotics and things your body was never built for, and your hormones get thrown off balance. And that calcium they promised you? Your body barely holds on to it. You get all the hormones and none of the good. Still do not know what food I mean? It is dairy, baby. The milk, the cheese, the cream, all of it. When you are inflamed on the inside, the collagen breaks down, the skin on your chest gets thin, and the firmness goes. And it does not matter what bra you buy or how much weight you lose. You skip certain tops, and you dread the mirror. And then you blame yourself, when it was never you. It is not gravity and it is not age. It is inflammation, from the inside. But here is the good news, baby. Your body knows how to take care of itself when you give it the right support. Forty years making sea moss for every woman on this block, and there is one thing I keep on my own counter. Vitamin C, which supports normal collagen formation, turmeric with black pepper, ginger, and wild Irish sea moss. Sixteen in one gummy. Natural Rems Sea Moss. So you are supporting your skin from the inside out, and when you feel good in your body, even getting dressed feels different. One green apple gummy every morning at breakfast, you chew it, and that is all. No pot on the stove, no sixteen bottles. Comment yes if there is milk or cheese in your fridge tonight, and I will make you a video on how I start my mornings. Search Natural Rems Sea Moss on Amazon. Or tap my profile picture, the link is waiting in my stories, or right there in my bio. And don't forget to hit that follow button.

**PT corrido:** Últimas notícias desta noite. Um vídeo do Brooklyn está explodindo depois que ela revelou a comida mais venenosa para os seios de uma mulher, e ela está em toda cozinha. Assista. Não é o hambúrguer, meu bem. Não é a pizza. E não, nem é o sorvete do seu freezer. É algo pior, escondido à vista de todos na prateleira da sua geladeira, e você pega isso todo santo dia. E se você come, a culpa não é sua, filha. Os comerciais te disseram a vida inteira que fazia bem. Então senta comigo um minuto, porque o que eu vou te contar ninguém me contou. Ela carrega hormônios e fatores de crescimento, e no momento em que eles entram no seu corpo, o corpo responde com inflamação. Essa inflamação ataca o colágeno e o tecido conjuntivo, justamente o que mantém o seu peito firme e cheio. Além disso, ela é cheia de antibiótico e de coisa para a qual o seu corpo nunca foi feito, e os seus hormônios saem do equilíbrio. E aquele cálcio que te prometeram? O seu corpo mal segura ele. Você fica com todos os hormônios e nada do lado bom. Ainda não sabe de que comida eu falo? É o laticínio, meu bem. O leite, o queijo, o creme, tudo. Quando você está inflamada por dentro, o colágeno se desfaz, a pele do peito fica fina, e a firmeza vai embora. E não importa o sutiã que você compra ou quanto peso você perde. Você evita certas blusas, e tem pavor do espelho. E aí você se culpa, quando nunca foi você. Não é a gravidade e não é a idade. É inflamação, de dentro para fora. [fala real do take] Mas a boa notícia, meu bem. O seu corpo sabe se cuidar quando você dá a ele o apoio certo. Quarenta anos fazendo sea moss para toda mulher deste quarteirão, e tem uma coisa que eu deixo na minha própria bancada. [fala real do take] Vitamina C, que apoia a formação normal de colágeno, cúrcuma com pimenta-do-reino, gengibre e sea moss irlandês selvagem. Dezesseis numa goma. Natural Rems Sea Moss. Então você está cuidando da sua pele de dentro para fora, e quando você se sente bem no seu corpo, até se vestir fica diferente. Uma goma de maçã verde toda manhã no café, você mastiga e é só isso. Sem panela no fogão, sem dezesseis frascos. Comenta yes se tem leite ou queijo na sua geladeira hoje, e eu faço um vídeo de como eu começo as minhas manhãs. Procure Natural Rems Sea Moss na Amazon. Ou toque na minha foto de perfil, o link está te esperando nos meus stories, ou bem ali na minha bio. E não esquece de apertar o botão de seguir.
