# ENTREGA | Cassidy Hargrove | Sea Moss Venda · pilha de notícia · rins

flow_seguro: v1

Produção `cassidy_seamoss_rins_noticia` · Ângulo 1 Sea Moss (conta da Cassidy) · VENDA · rodada de VALIDAÇÃO · formato mínimo de prompt do Flow

## 0. INSTRUÇÕES PARA A MEMÓRIA DO AGENTE · GOOGLE FLOW (colar inteiro antes do primeiro K)

```text
# Agente do Flow, produção atual: Sea Moss Venda · pilha de notícia · rins

Você é o executor do Google Flow. Você só gera imagens e vídeos a partir de prompts prontos. Você não cria, não edita e não melhora prompt.

## Produção atual
- Conta: Natural Rems Sea Moss (Cassidy), vídeo de venda. Sea Moss Venda · pilha de notícia · rins.
- Um avatar só: a mulher ruiva de trança, suéter creme e macacão amarelo (arquivo `cassidy hargrove .jpg`). Imagens K01 a K03; vídeos V01 a V21.

## O que é anexado (só isto, nada mais)
- IMAGEM (K): anexe só a imagem da avatar e cole o prompt.
- EXCEÇÃO K01: NÃO anexe nenhuma imagem, só cole o prompt.
- EXCEÇÃO K03: anexe `cassidy hargrove .jpg` e `natural_rems_seamoss_produto.jpg` (nesta ordem).
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

**Vídeo: pilha de notícia, a pior bebida para os rins (refrigerante diet).**

**O que acontece:** abre num telejornal de emissora inventada (a âncora noticia que um vídeo viralizou). Corta para Cassidy Hargrove no cenário fixo da conta, que elimina três suspeitos, absolve, explica o mecanismo, revela o vilão, vira para a causa raiz e, com o pote na mão, apresenta o Natural Rems Sea Moss. Fecha com comment yes, Amazon, Stories e bio, e o lembrete do follow.

**Gancho:** a âncora do telejornal com a imagem de choque e a faixa BREAKING NEWS.

## 1. Anexos e mapa

- **Imagem (K):** anexar SÓ o que o título de cada K indica (padrão: a imagem da avatar, `cassidy hargrove .jpg`) e colar o prompt. 4 variações, 9:16. Nada de frame do modelo.
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
Television news studio frame, vertical 9:16. A news anchor woman in her mid forties with deep brown skin and short natural curls, a deep red blazer over a black top, seated at a glossy news desk with her hands resting on a few papers, looking straight into the camera, caught mid-sentence with lips naturally parted. Behind her a large window wall shows a city skyline at blue hour, deep blue sky with lit towers. On the left, a large inset photo box beside her showing a close-up photo of a kidney cut in half, pink-orange tissue with a big shiny black stone lodged in the middle, filling about a third of the frame. Across the bottom a red lower-third banner reads BREAKING NEWS in bold white letters with a white strip reading HEALTH ALERT. A small American flag stands on the desk at the right, in sharp focus. Broadcast camera at eye level, 35mm lens, front facing, medium shot from the chest up. Clean even studio light, true neutral colors, real skin texture with visible pores, everything in sharp focus, 9:16 vertical.
```

### K02 · anexar SÓ `cassidy hargrove .jpg`

Cena: Cassidy Hargrove no cenário fixo da conta falando, mão direita erguida com o indicador para cima perto da lente.

```text
K02
Match the attached image exactly for the woman's identity and outfit: a woman in her early sixties with long wind-tossed copper-red hair worn in one thick loose braid over her left shoulder, dense freckles on her face and forearms, wind-weathered fair skin, light eyes, a small reddish mark on her chin, a thick cream cable-knit wool fisherman sweater with the sleeves pushed up, bright yellow oilskin bib overalls with black buckles, and a silver Claddagh ring on her left hand. She stands behind a weathered wooden plank workbench on a seaside dock in Maine: behind her a gray cedar-shingled harvest shed with an open door and wooden rakes inside, a wooden rack of drying dark purple-red seaweed on the left, gray-blue ocean and dark rocks on the right under an overcast blue-gray sky with visible clouds, and a small American flag mounted on the shed wall beside the door, in sharp focus. Hero: her right hand raised in the lower foreground, very close to the lens, large in frame and closer to the camera than her face, index finger pointing up as she makes a point. She looks straight at the camera, caught mid-sentence, lips naturally parted, serious and animated expression. Vertical smartphone shot, 26mm lens, camera at chest height about one meter from the table, level, front facing. Soft neutral even daylight, true neutral colors, real skin texture with visible pores, smartphone footage look, everything in sharp focus, 9:16 vertical.
```

### K03 · anexar SÓ `cassidy hargrove .jpg` + `natural_rems_seamoss_produto.jpg`

Cena: Cassidy Hargrove no mesmo plano segurando o frasco do Natural Rems Sea Moss colado na lente, rótulo legível.

```text
K03
Match the attached image exactly for the woman's identity and outfit: a woman in her early sixties with long wind-tossed copper-red hair worn in one thick loose braid over her left shoulder, dense freckles on her face and forearms, wind-weathered fair skin, light eyes, a small reddish mark on her chin, a thick cream cable-knit wool fisherman sweater with the sleeves pushed up, bright yellow oilskin bib overalls with black buckles, and a silver Claddagh ring on her left hand. She stands behind a weathered wooden plank workbench on a seaside dock in Maine: behind her a gray cedar-shingled harvest shed with an open door and wooden rakes inside, a wooden rack of drying dark purple-red seaweed on the left, gray-blue ocean and dark rocks on the right under an overcast blue-gray sky with visible clouds, and a small American flag mounted on the shed wall beside the door, in sharp focus. Hero: she holds the Natural Rems Sea Moss Gummies jar exactly as in the second attached image: a short wide jar of dark amber plastic with a black screw cap, a pale sage-green label with dark green text, the Natural Rems logo with three leaves, the big title Sea Moss Gummies, a pill-shaped badge reading 6000 MG | 16-IN-1, and the line GREEN APPLE FLAVOR in her right hand out toward the camera, very close to the lens, large in frame and closer to the camera than her face, label fully readable, fingers on the sides. {MID} {REF_POTE} Vertical smartphone shot, 26mm lens, camera at chest height about one meter from the table, level, front facing. Soft neutral even daylight, true neutral colors, real skin texture with visible pores, smartphone footage look, everything in sharp focus, 9:16 vertical.
```

## 3. PROMPTS DE VÍDEO (um bloco por V)

### V01 · T1, Âncora de telejornal · anexar SÓ a imagem escolhida do K01

Cena: A âncora dá a notícia. Fala: "Últimas notícias do Maine. Um vídeo está se espalhando rápido depois que ela expôs a bebida mais venenosa para os rins, e milhões de americanos bebem todo dia. Assista."

```text
V01
The person in the image speaks in American English, looking at the camera: "Breaking news from Maine. A video is spreading fast after she exposed the most poisonous drink for the kidneys, and millions of Americans drink it daily. Just watch."
Fixed camera. Natural lip sync, no music.
```

### V02 · T2, Eliminação tripla · anexar SÓ a imagem escolhida do K02

Cena: Ela fala para a câmera. Fala: "A pior coisa que você pode servir para os seus rins não é cerveja, não é energético, e nem é suco de fruta."

```text
V02
The person in the image speaks in American English, looking at the camera: "The worst thing you can pour for your kidneys is not beer, it is not an energy drink, and it is not even fruit juice."
Fixed camera. Natural lip sync, no music.
```

### V03 · T3, Proximidade · anexar SÓ a imagem escolhida do K02

Cena: Ela fala para a câmera. Fala: "É algo muito mais perigoso, e eu aposto que está na sua geladeira neste minuto."

```text
V03
The person in the image speaks in American English, looking at the camera: "It is something a lot more dangerous, and I would bet it is sitting in your fridge right this minute."
Fixed camera. Natural lip sync, no music.
```

### V04 · T4, Absolvição · anexar SÓ a imagem escolhida do K02

Cena: Ela fala para a câmera. Fala: "Se você bebe, isso não é culpa sua. Te enrolaram para acreditar que era a escolha esperta e saudável."

```text
V04
The person in the image speaks in American English, looking at the camera: "If you drink it, that is not on you. You got played into believing it was the smart, healthy choice."
Fixed camera. Natural lip sync, no music.
```

### V05 · T5, Ordem de assistir · anexar SÓ a imagem escolhida do K02

Cena: Ela fala para a câmera. Fala: "Então fica comigo no próximo minuto, e você nunca mais comete esse erro."

```text
V05
The person in the image speaks in American English, looking at the camera: "So stick with me for the next minute, and you will never make this mistake again."
Fixed camera. Natural lip sync, no music.
```

### V06 · T6, Mecanismo · anexar SÓ a imagem escolhida do K02

Cena: Ela fala para a câmera. Fala: "Isso é preparado numa fábrica química, e é carregado de adoçante artificial que o seu corpo trata como toxina."

```text
V06
The person in the image speaks in American English, looking at the camera: "This stuff is cooked up in a chemical factory, and it is loaded with artificial sweeteners your body handles like a toxin."
Fixed camera. Natural lip sync, no music.
```

### V07 · T7, Mecanismo · anexar SÓ a imagem escolhida do K02

Cena: Ela fala para a câmera. Fala: "Isso dispara inflamação, e os seus rins acabam fazendo turno dobrado só para jogar isso fora."

```text
V07
The person in the image speaks in American English, looking at the camera: "That sets off inflammation, and your kidneys end up pulling a double shift just to flush it out."
Fixed camera. Natural lip sync, no music.
```

### V08 · T8, Mecanismo · anexar SÓ a imagem escolhida do K02

Cena: Ela fala para a câmera. Fala: "A maioria não faz ideia do tanto de estresse que essas bebidas põem nos rins, ou de como é duro para o corpo se recuperar."

```text
V08
The person in the image speaks in American English, looking at the camera: "Most folks have no idea how much stress these drinks put on the kidneys, or how tough it is for the body to recover."
Fixed camera. Natural lip sync, no music.
```

### V09 · T9, Revelação do vilão · anexar SÓ a imagem escolhida do K02

Cena: Ela fala para a câmera. Fala: "Ainda não sabe de que bebida eu estou falando? Refrigerante diet. Zero açúcar, cola diet, todos eles, sem exceção."

```text
V09
The person in the image speaks in American English, looking at the camera: "Still not sure which drink I am talking about? Diet soda. Zero sugar soda, diet cola, every last one of them."
Fixed camera. Natural lip sync, no music.
```

### V10 · T10, Virar o benefício · anexar SÓ a imagem escolhida do K02

Cena: Ela fala para a câmera. Fala: "E não, não é energia limpa. É energia roubada do seu futuro, porque desliga a parte de você que sabe que está cansada."

```text
V10
The person in the image speaks in American English, looking at the camera: "And no, it is not clean energy. It is energy stolen from your future, because it shuts off the part of you that knows you are tired."
Fixed camera. Natural lip sync, no music.
```

### V11 · T11, Virar o benefício · anexar SÓ a imagem escolhida do K02

Cena: Ela fala para a câmera. Fala: "Você vive em luta ou fuga o dia todo, isso te desgasta por dentro, e os seus rins nunca têm folga."

```text
V11
The person in the image speaks in American English, looking at the camera: "You run on fight or flight all day, it wears you down from the inside, and your kidneys never catch a break."
Fixed camera. Natural lip sync, no music.
```

### V12 · T12, Causa raiz · anexar SÓ a imagem escolhida do K02

Cena: Ela fala para a câmera. Fala: "Então o meu conselho é simples. Para de se apoiar nessas bebidas e vai atrás da raiz de verdade, o seu metabolismo."

```text
V12
The person in the image speaks in American English, looking at the camera: "So my advice is simple. Quit leaning on these drinks and go after the real root of it, your metabolism."
Fixed camera. Natural lip sync, no music.
```

### V13 · T13, Ponte pro sintoma · anexar SÓ a imagem escolhida do K02

Cena: Ela fala para a câmera. Fala: "Quando o metabolismo desacelera e a inflamação se acumula, o corpo tem mais dificuldade de manter o equilíbrio de líquidos e de perder o peso teimoso."

```text
V13
The person in the image speaks in American English, looking at the camera: "Once your metabolism slows and inflammation builds up, your body has a harder time keeping its fluid balance and dropping stubborn weight."
Fixed camera. Natural lip sync, no music.
```

### V14 · T14, Sintoma visível · anexar SÓ a imagem escolhida do K02

Cena: Ela fala para a câmera. Fala: "E é por isso que a barriga continua aumentando, não importa o que você tente. Isso também nunca foi culpa sua."

```text
V14
The person in the image speaks in American English, looking at the camera: "And that is why the belly keeps getting bigger, no matter what you try. That was never your fault either."
Fixed camera. Natural lip sync, no music.
```

### V15 · T15, Autoridade e exclusividade · anexar SÓ a imagem escolhida do K03

Cena: Ela segura o pote parado, rótulo legível. Fala: "Trinta anos tirando Irish moss destas pedras, e em todo esse tempo eu achei uma coisa em que confio mais do que tudo."

```text
V15
The person in the image speaks in American English, looking at the camera: "Thirty years I have been pulling Irish moss off these rocks, and in all that time I found one thing I trust over everything."
Fixed camera. Natural lip sync, no music.
```

### V16 · T16, Ingrediente antes da marca · anexar SÓ a imagem escolhida do K03

Cena: Ela segura o pote parado, rótulo legível. Fala: "Sea moss irlandês selvagem, vitamina D3, gengibre para o intestino, cúrcuma, óleo de semente preta, dezesseis ingredientes numa goma só. Natural Rems Sea Moss."

```text
V16
The person in the image speaks in American English, looking at the camera: "Wild Irish sea moss, vitamin D3, ginger for your gut, turmeric, black seed oil, sixteen ingredients packed in one gummy. Natural Rems Sea Moss."
Fixed camera. Natural lip sync, no music.
```

### V17 · T17, Matar a fricção · anexar SÓ a imagem escolhida do K03

Cena: Ela segura o pote parado, rótulo legível. Fala: "E é fácil. Mastiga uma goma de maçã verde por dia com uma refeição, e é isso. E é muito gostosa."

```text
V17
The person in the image speaks in American English, looking at the camera: "And it is easy. Chew one green apple gummy a day with a meal, and that is it. Tastes great, too."
Fixed camera. Natural lip sync, no music.
```

### V18 · T18, Reenquadrar o custo · anexar SÓ a imagem escolhida do K03

Cena: Ela segura o pote parado, rótulo legível. Fala: "Se cuidar não devia ser um armário com dezesseis frascos, nem ferver alga no fogão como eu faço toda semana."

```text
V18
The person in the image speaks in American English, looking at the camera: "Looking after yourself should not mean a cupboard full of sixteen bottles, or boiling seaweed on the stove like I do every week."
Fixed camera. Natural lip sync, no music.
```

### V19 · T19, Comentário · anexar SÓ a imagem escolhida do K03

Cena: Ela segura o pote parado, rótulo legível. Fala: "Comenta yes se essa latinha está na sua geladeira agora, pra eu saber quem quer a minha rotina diária no próximo."

```text
V19
The person in the image speaks in American English, looking at the camera: "Comment yes if that can is in your fridge right now, so I know who wants my daily routine in the next one."
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
| T1 | Breaking news from Maine. A video is spreading fast after she exposed the most poisonous drink for the kidneys, and millions of Americans drink it daily. Just watch. | Últimas notícias do Maine. Um vídeo está se espalhando rápido depois que ela expôs a bebida mais venenosa para os rins, e milhões de americanos bebem todo dia. Assista. |
| T2 | The worst thing you can pour for your kidneys is not beer, it is not an energy drink, and it is not even fruit juice. | A pior coisa que você pode servir para os seus rins não é cerveja, não é energético, e nem é suco de fruta. |
| T3 | It is something a lot more dangerous, and I would bet it is sitting in your fridge right this minute. | É algo muito mais perigoso, e eu aposto que está na sua geladeira neste minuto. |
| T4 | If you drink it, that is not on you. You got played into believing it was the smart, healthy choice. | Se você bebe, isso não é culpa sua. Te enrolaram para acreditar que era a escolha esperta e saudável. |
| T5 | So stick with me for the next minute, and you will never make this mistake again. | Então fica comigo no próximo minuto, e você nunca mais comete esse erro. |
| T6 | This stuff is cooked up in a chemical factory, and it is loaded with artificial sweeteners your body handles like a toxin. | Isso é preparado numa fábrica química, e é carregado de adoçante artificial que o seu corpo trata como toxina. |
| T7 | That sets off inflammation, and your kidneys end up pulling a double shift just to flush it out. | Isso dispara inflamação, e os seus rins acabam fazendo turno dobrado só para jogar isso fora. |
| T8 | Most folks have no idea how much stress these drinks put on the kidneys, or how tough it is for the body to recover. | A maioria não faz ideia do tanto de estresse que essas bebidas põem nos rins, ou de como é duro para o corpo se recuperar. |
| T9 | Still not sure which drink I am talking about? Diet soda. Zero sugar soda, diet cola, every last one of them. | Ainda não sabe de que bebida eu estou falando? Refrigerante diet. Zero açúcar, cola diet, todos eles, sem exceção. |
| T10 | And no, it is not clean energy. It is energy stolen from your future, because it shuts off the part of you that knows you are tired. | E não, não é energia limpa. É energia roubada do seu futuro, porque desliga a parte de você que sabe que está cansada. |
| T11 | You run on fight or flight all day, it wears you down from the inside, and your kidneys never catch a break. | Você vive em luta ou fuga o dia todo, isso te desgasta por dentro, e os seus rins nunca têm folga. |
| T12 | So my advice is simple. Quit leaning on these drinks and go after the real root of it, your metabolism. | Então o meu conselho é simples. Para de se apoiar nessas bebidas e vai atrás da raiz de verdade, o seu metabolismo. |
| T13 | Once your metabolism slows and inflammation builds up, your body has a harder time keeping its fluid balance and dropping stubborn weight. | Quando o metabolismo desacelera e a inflamação se acumula, o corpo tem mais dificuldade de manter o equilíbrio de líquidos e de perder o peso teimoso. |
| T14 | And that is why the belly keeps getting bigger, no matter what you try. That was never your fault either. | E é por isso que a barriga continua aumentando, não importa o que você tente. Isso também nunca foi culpa sua. |
| T15 | Thirty years I have been pulling Irish moss off these rocks, and in all that time I found one thing I trust over everything. | Trinta anos tirando Irish moss destas pedras, e em todo esse tempo eu achei uma coisa em que confio mais do que tudo. |
| T16 | Wild Irish sea moss, vitamin D3, ginger for your gut, turmeric, black seed oil, sixteen ingredients packed in one gummy. Natural Rems Sea Moss. | Sea moss irlandês selvagem, vitamina D3, gengibre para o intestino, cúrcuma, óleo de semente preta, dezesseis ingredientes numa goma só. Natural Rems Sea Moss. |
| T17 | And it is easy. Chew one green apple gummy a day with a meal, and that is it. Tastes great, too. | E é fácil. Mastiga uma goma de maçã verde por dia com uma refeição, e é isso. E é muito gostosa. |
| T18 | Looking after yourself should not mean a cupboard full of sixteen bottles, or boiling seaweed on the stove like I do every week. | Se cuidar não devia ser um armário com dezesseis frascos, nem ferver alga no fogão como eu faço toda semana. |
| T19 | Comment yes if that can is in your fridge right now, so I know who wants my daily routine in the next one. | Comenta yes se essa latinha está na sua geladeira agora, pra eu saber quem quer a minha rotina diária no próximo. |
| T20 | Search Natural Rems Sea Moss on Amazon. Or tap my profile picture, the link is waiting in my stories, or right there in my bio. | Procure Natural Rems Sea Moss na Amazon. Ou toque na minha foto de perfil, o link está te esperando nos meus stories, ou bem ali na minha bio. |
| T21 | And don't forget to hit that follow button. | E não esquece de apertar o botão de seguir. |

**EN corrido:** Breaking news from Maine. A video is spreading fast after she exposed the most poisonous drink for the kidneys, and millions of Americans drink it daily. Just watch. The worst thing you can pour for your kidneys is not beer, it is not an energy drink, and it is not even fruit juice. It is something a lot more dangerous, and I would bet it is sitting in your fridge right this minute. If you drink it, that is not on you. You got played into believing it was the smart, healthy choice. So stick with me for the next minute, and you will never make this mistake again. This stuff is cooked up in a chemical factory, and it is loaded with artificial sweeteners your body handles like a toxin. That sets off inflammation, and your kidneys end up pulling a double shift just to flush it out. Most folks have no idea how much stress these drinks put on the kidneys, or how tough it is for the body to recover. Still not sure which drink I am talking about? Diet soda. Zero sugar soda, diet cola, every last one of them. And no, it is not clean energy. It is energy stolen from your future, because it shuts off the part of you that knows you are tired. You run on fight or flight all day, it wears you down from the inside, and your kidneys never catch a break. So my advice is simple. Quit leaning on these drinks and go after the real root of it, your metabolism. Once your metabolism slows and inflammation builds up, your body has a harder time keeping its fluid balance and dropping stubborn weight. And that is why the belly keeps getting bigger, no matter what you try. That was never your fault either. Thirty years I have been pulling Irish moss off these rocks, and in all that time I found one thing I trust over everything. Wild Irish sea moss, vitamin D3, ginger for your gut, turmeric, black seed oil, sixteen ingredients packed in one gummy. Natural Rems Sea Moss. And it is easy. Chew one green apple gummy a day with a meal, and that is it. Tastes great, too. Looking after yourself should not mean a cupboard full of sixteen bottles, or boiling seaweed on the stove like I do every week. Comment yes if that can is in your fridge right now, so I know who wants my daily routine in the next one. Search Natural Rems Sea Moss on Amazon. Or tap my profile picture, the link is waiting in my stories, or right there in my bio. And don't forget to hit that follow button.

**PT corrido:** Últimas notícias do Maine. Um vídeo está se espalhando rápido depois que ela expôs a bebida mais venenosa para os rins, e milhões de americanos bebem todo dia. Assista. A pior coisa que você pode servir para os seus rins não é cerveja, não é energético, e nem é suco de fruta. É algo muito mais perigoso, e eu aposto que está na sua geladeira neste minuto. Se você bebe, isso não é culpa sua. Te enrolaram para acreditar que era a escolha esperta e saudável. Então fica comigo no próximo minuto, e você nunca mais comete esse erro. Isso é preparado numa fábrica química, e é carregado de adoçante artificial que o seu corpo trata como toxina. Isso dispara inflamação, e os seus rins acabam fazendo turno dobrado só para jogar isso fora. A maioria não faz ideia do tanto de estresse que essas bebidas põem nos rins, ou de como é duro para o corpo se recuperar. Ainda não sabe de que bebida eu estou falando? Refrigerante diet. Zero açúcar, cola diet, todos eles, sem exceção. E não, não é energia limpa. É energia roubada do seu futuro, porque desliga a parte de você que sabe que está cansada. Você vive em luta ou fuga o dia todo, isso te desgasta por dentro, e os seus rins nunca têm folga. Então o meu conselho é simples. Para de se apoiar nessas bebidas e vai atrás da raiz de verdade, o seu metabolismo. Quando o metabolismo desacelera e a inflamação se acumula, o corpo tem mais dificuldade de manter o equilíbrio de líquidos e de perder o peso teimoso. E é por isso que a barriga continua aumentando, não importa o que você tente. Isso também nunca foi culpa sua. Trinta anos tirando Irish moss destas pedras, e em todo esse tempo eu achei uma coisa em que confio mais do que tudo. Sea moss irlandês selvagem, vitamina D3, gengibre para o intestino, cúrcuma, óleo de semente preta, dezesseis ingredientes numa goma só. Natural Rems Sea Moss. E é fácil. Mastiga uma goma de maçã verde por dia com uma refeição, e é isso. E é muito gostosa. Se cuidar não devia ser um armário com dezesseis frascos, nem ferver alga no fogão como eu faço toda semana. Comenta yes se essa latinha está na sua geladeira agora, pra eu saber quem quer a minha rotina diária no próximo. Procure Natural Rems Sea Moss na Amazon. Ou toque na minha foto de perfil, o link está te esperando nos meus stories, ou bem ali na minha bio. E não esquece de apertar o botão de seguir.
