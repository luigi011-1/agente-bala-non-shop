# ENTREGA | Marshall Beckett | Sea Moss Venda · pilha de notícia · rins

flow_seguro: v1

Produção `marshall_seamoss_rins_noticia` · Ângulo 1 Sea Moss (conta da Marshall) · VENDA · rodada de VALIDAÇÃO · formato mínimo de prompt do Flow

## 0. INSTRUÇÕES PARA A MEMÓRIA DO AGENTE · GOOGLE FLOW (colar inteiro antes do primeiro K)

```text
# Agente do Flow, produção atual: Sea Moss Venda · pilha de notícia · rins

Você é o executor do Google Flow. Você só gera imagens e vídeos a partir de prompts prontos. Você não cria, não edita e não melhora prompt.

## Produção atual
- Conta: Natural Rems Sea Moss (Marshall), vídeo de venda. Sea Moss Venda · pilha de notícia · rins.
- Um avatar só: a senhora de roupa branca de mergulhadora com a máscara de latão na testa (arquivo `marshall beckett .jpg`). Imagens K01 a K03; vídeos V01 a V21.

## O que é anexado (só isto, nada mais)
- IMAGEM (K): anexe só a imagem da avatar e cole o prompt.
- EXCEÇÃO K01: NÃO anexe nenhuma imagem, só cole o prompt.
- EXCEÇÃO K03: anexe `marshall beckett .jpg` e `natural_rems_seamoss_produto.jpg` (nesta ordem).
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

**O que acontece:** abre num telejornal de emissora inventada (a âncora noticia que um vídeo viralizou). Corta para Marshall Beckett no cenário fixo da conta, que elimina três suspeitos, absolve, explica o mecanismo, revela o vilão, vira para a causa raiz e, com o pote na mão, apresenta o Natural Rems Sea Moss. Fecha com comment yes, Amazon, Stories e bio, e o lembrete do follow.

**Gancho:** a âncora do telejornal com a imagem de choque e a faixa BREAKING NEWS.

## 1. Anexos e mapa

- **Imagem (K):** anexar SÓ o que o título de cada K indica (padrão: a imagem da avatar, `marshall beckett .jpg`) e colar o prompt. 4 variações, 9:16. Nada de frame do modelo.
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
Television news studio frame, vertical 9:16. A news anchor woman in her early fifties with shoulder-length dark brown hair, a navy-blue blazer over a white top, seated at a glossy news desk with her hands resting on a few papers, looking straight into the camera, caught mid-sentence with lips naturally parted. Behind her a large window wall shows a city skyline at blue hour, deep blue sky with lit towers. On the left, a large inset photo box beside her showing a close-up photo of a kidney cut in half, pink-orange tissue with a big shiny black stone lodged in the middle, filling about a third of the frame. Across the bottom a red lower-third banner reads BREAKING NEWS in bold white letters with a white strip reading HEALTH ALERT. A small American flag stands on the desk at the right, in sharp focus. Broadcast camera at eye level, 35mm lens, front facing, medium shot from the chest up. Clean even studio light, true neutral colors, real skin texture with visible pores, everything in sharp focus, 9:16 vertical.
```

### K02 · anexar SÓ `marshall beckett .jpg`

Cena: Marshall Beckett no cenário fixo da conta falando, mão direita erguida com o indicador para cima perto da lente.

```text
K02
Match the attached image exactly for the woman's identity and outfit: a Japanese-American woman in her seventies with deeply sun-darkened skin, sun spots and dark freckles, deep wrinkles, calm narrow dark eyes, a lean strong build, a white cotton headscarf tied around her forehead with an antique round brass-rimmed diving mask pushed up on top of it, a white cotton wrap jacket tied at the waist with white cotton pants, and a small abalone shell pendant on a black cord. She stands behind a weathered gray wooden plank table under an open shed with a rusted corrugated tin roof on a black lava rock shore in Hawaii: bamboo mats of drying green and dark red seaweed on both sides, a wooden wash tub on the right, turquoise ocean with white surf behind her under an overcast blue-gray sky, and a small American flag tied to the right wooden post, in sharp focus. Hero: her right hand raised in the lower foreground, very close to the lens, large in frame and closer to the camera than her face, index finger pointing up as she makes a point. She looks straight at the camera, caught mid-sentence, lips naturally parted, serious and animated expression. Vertical smartphone shot, 26mm lens, camera at chest height about one meter from the table, level, front facing. Soft neutral even daylight, true neutral colors, real skin texture with visible pores, smartphone footage look, everything in sharp focus, 9:16 vertical.
```

### K03 · anexar SÓ `marshall beckett .jpg` + `natural_rems_seamoss_produto.jpg`

Cena: Marshall Beckett no mesmo plano segurando o frasco do Natural Rems Sea Moss colado na lente, rótulo legível.

```text
K03
Match the attached image exactly for the woman's identity and outfit: a Japanese-American woman in her seventies with deeply sun-darkened skin, sun spots and dark freckles, deep wrinkles, calm narrow dark eyes, a lean strong build, a white cotton headscarf tied around her forehead with an antique round brass-rimmed diving mask pushed up on top of it, a white cotton wrap jacket tied at the waist with white cotton pants, and a small abalone shell pendant on a black cord. She stands behind a weathered gray wooden plank table under an open shed with a rusted corrugated tin roof on a black lava rock shore in Hawaii: bamboo mats of drying green and dark red seaweed on both sides, a wooden wash tub on the right, turquoise ocean with white surf behind her under an overcast blue-gray sky, and a small American flag tied to the right wooden post, in sharp focus. Hero: she holds the Natural Rems Sea Moss Gummies jar exactly as in the second attached image: a short wide jar of dark amber plastic with a black screw cap, a pale sage-green label with dark green text, the Natural Rems logo with three leaves, the big title Sea Moss Gummies, a pill-shaped badge reading 6000 MG | 16-IN-1, and the line GREEN APPLE FLAVOR in her right hand out toward the camera, very close to the lens, large in frame and closer to the camera than her face, label fully readable, fingers on the sides. {MID} {REF_POTE} Vertical smartphone shot, 26mm lens, camera at chest height about one meter from the table, level, front facing. Soft neutral even daylight, true neutral colors, real skin texture with visible pores, smartphone footage look, everything in sharp focus, 9:16 vertical.
```

## 3. PROMPTS DE VÍDEO (um bloco por V)

### V01 · T1, Âncora de telejornal · anexar SÓ a imagem escolhida do K01

Cena: A âncora dá a notícia. Fala: "Últimas notícias do Havaí. Um vídeo está viralizando depois que ela expôs a bebida mais venenosa para os seus rins, que milhões de americanos bebem todo dia. Assista."

```text
V01
The person in the image speaks in American English, looking at the camera: "Breaking news out of Hawaii. A video is going viral after she exposed the most poisonous drink for your kidneys, one millions of Americans drink every day. Just watch."
Fixed camera. Natural lip sync, no music.
```

### V02 · T2, Eliminação tripla · anexar SÓ a imagem escolhida do K02

Cena: Ela fala para a câmera. Fala: "A bebida mais venenosa para os seus rins não é o álcool. Não é energético. Nem é suco de maçã."

```text
V02
The person in the image speaks in American English, looking at the camera: "The most poisonous drink for your kidneys is not alcohol. It is not energy drinks. It is not even apple juice."
Fixed camera. Natural lip sync, no music.
```

### V03 · T3, Proximidade · anexar SÓ a imagem escolhida do K02

Cena: Ela fala para a câmera. Fala: "É algo mais silencioso e mais perigoso. E muito provavelmente está na sua geladeira hoje à noite."

```text
V03
The person in the image speaks in American English, looking at the camera: "It is something quieter and more dangerous. And it is very likely sitting in your refrigerator tonight."
Fixed camera. Natural lip sync, no music.
```

### V04 · T4, Absolvição · anexar SÓ a imagem escolhida do K02

Cena: Ela fala para a câmera. Fala: "Se você bebe, a culpa não é sua. Te ensinaram a acreditar que era a escolha saudável."

```text
V04
The person in the image speaks in American English, looking at the camera: "If you drink it, the fault is not yours. You were taught to believe it was the healthy choice."
Fixed camera. Natural lip sync, no music.
```

### V05 · T5, Ordem de assistir · anexar SÓ a imagem escolhida do K02

Cena: Ela fala para a câmera. Fala: "Então assista com atenção, uma vez, e você nunca mais comete esse erro."

```text
V05
The person in the image speaks in American English, looking at the camera: "So watch this closely, one time, and you will never make this mistake again."
Fixed camera. Natural lip sync, no music.
```

### V06 · T6, Mecanismo · anexar SÓ a imagem escolhida do K02

Cena: Ela fala para a câmera. Fala: "Essa bebida é feita numa fábrica química. É cheia de adoçante artificial, e o seu corpo lê isso como toxina."

```text
V06
The person in the image speaks in American English, looking at the camera: "This drink is built in a chemical plant. It is full of artificial sweeteners, and your body reads them as a toxin."
Fixed camera. Natural lip sync, no music.
```

### V07 · T7, Mecanismo · anexar SÓ a imagem escolhida do K02

Cena: Ela fala para a câmera. Fala: "Então o corpo responde com inflamação, e os rins fazem hora extra só para lavar isso para fora."

```text
V07
The person in the image speaks in American English, looking at the camera: "So the body answers with inflammation, and the kidneys work overtime just to wash it back out."
Fixed camera. Natural lip sync, no music.
```

### V08 · T8, Mecanismo · anexar SÓ a imagem escolhida do K02

Cena: Ela fala para a câmera. Fala: "Pouca gente entende o tanto de esforço que essas bebidas põem nos rins, ou como o corpo se recupera devagar depois que começa."

```text
V08
The person in the image speaks in American English, looking at the camera: "Few people understand how much strain these drinks place on the kidneys, or how slowly the body recovers once it starts."
Fixed camera. Natural lip sync, no music.
```

### V09 · T9, Revelação do vilão · anexar SÓ a imagem escolhida do K02

Cena: Ela fala para a câmera. Fala: "E se você ainda está pensando em qual bebida eu falo, é o refrigerante diet. Zero açúcar, cola diet, todos."

```text
V09
The person in the image speaks in American English, looking at the camera: "And if you are still wondering which drink I mean, it is diet soda. Zero sugar, diet cola, all of them."
Fixed camera. Natural lip sync, no music.
```

### V10 · T10, Virar o benefício · anexar SÓ a imagem escolhida do K02

Cena: Ela fala para a câmera. Fala: "Ele não te dá energia limpa. Ele tira energia do seu futuro, calando o sinal que manda você descansar."

```text
V10
The person in the image speaks in American English, looking at the camera: "It does not give you clean energy. It takes energy from your future, by silencing the signal that tells you to rest."
Fixed camera. Natural lip sync, no music.
```

### V11 · T11, Virar o benefício · anexar SÓ a imagem escolhida do K02

Cena: Ela fala para a câmera. Fala: "O corpo fica em luta ou fuga. Devagar, isso te esvazia por dentro, e os rins nunca descansam."

```text
V11
The person in the image speaks in American English, looking at the camera: "The body stays in fight or flight. Slowly, it empties you from the inside, and the kidneys never rest."
Fixed camera. Natural lip sync, no music.
```

### V12 · T12, Causa raiz · anexar SÓ a imagem escolhida do K02

Cena: Ela fala para a câmera. Fala: "Então eu digo isso a todo mundo. Pare de depender da latinha e vá na raiz, o seu metabolismo."

```text
V12
The person in the image speaks in American English, looking at the camera: "So I say this to everyone. Stop depending on the can, and go to the root of it, your metabolism."
Fixed camera. Natural lip sync, no music.
```

### V13 · T13, Ponte pro sintoma · anexar SÓ a imagem escolhida do K02

Cena: Ela fala para a câmera. Fala: "Quando o metabolismo desacelera e a inflamação se espalha pelo corpo, ele luta para manter o equilíbrio de líquidos e para soltar o peso teimoso. [fala real do take]"

```text
V13
The person in the image speaks in American English, looking at the camera: "When metabolism slows and inflammation spreads through the body, it struggles to keep a healthy fluid balance and to release stubborn weight."
Fixed camera. Natural lip sync, no music.
```

### V14 · T14, Sintoma visível · anexar SÓ a imagem escolhida do K02

Cena: Ela fala para a câmera. Fala: "É por isso que a barriga continua crescendo e nada do que você tenta tira ela do lugar. Nunca foi culpa sua."

```text
V14
The person in the image speaks in American English, looking at the camera: "This is why the belly keeps growing, and nothing you try can move it. It was never your fault."
Fixed camera. Natural lip sync, no music.
```

### V15 · T15, Autoridade e exclusividade · anexar SÓ a imagem escolhida do K03

Cena: Ela segura o pote parado, rótulo legível. Fala: "Há cinquenta anos eu mergulho atrás de alga neste oceano. Em todo esse tempo, achei uma coisa em que confio acima de tudo. [fala real do take]"

```text
V15
The person in the image speaks in American English, looking at the camera: "For fifty years I have dived for seaweed in this ocean. In all that time, I have found one thing I trust above everything."
Fixed camera. Natural lip sync, no music.
```

### V16 · T16, Ingrediente antes da marca · anexar SÓ a imagem escolhida do K03

Cena: Ela segura o pote parado, rótulo legível. Fala: "Sea moss irlandês selvagem, vitamina D3, gengibre para o intestino, cúrcuma com pimenta-do-reino e óleo de semente preta. Dezesseis numa goma. Natural Rems Sea Moss. [fala real do take]"

```text
V16
The person in the image speaks in American English, looking at the camera: "Wild Irish sea moss, vitamin D3, ginger for the gut. Sixteen in one gummy. Natural Rems Sea Moss."
Fixed camera. Natural lip sync, no music.
```

### V17 · T17, Matar a fricção · anexar SÓ a imagem escolhida do K03

Cena: Ela segura o pote parado, rótulo legível. Fala: "É simples. Uma goma de maçã verde por dia, com comida. Você mastiga e pronto. É gostosa."

```text
V17
The person in the image speaks in American English, looking at the camera: "It is simple. One green apple gummy a day, with food. You chew it, and you are done. It tastes good."
Fixed camera. Natural lip sync, no music.
```

### V18 · T18, Reenquadrar o custo · anexar SÓ a imagem escolhida do K03

Cena: Ela segura o pote parado, rótulo legível. Fala: "Cuidar do corpo não devia ser comprar dezesseis frascos, tomar um por um, ou secar alga numa mesa como esta."

```text
V18
The person in the image speaks in American English, looking at the camera: "Caring for your body should not mean buying sixteen bottles, taking each one alone, or drying seaweed on a table like this one."
Fixed camera. Natural lip sync, no music.
```

### V19 · T19, Comentário · anexar SÓ a imagem escolhida do K03

Cena: Ela segura o pote parado, rótulo legível. Fala: "Comenta yes se essa latinha está na sua geladeira agora, e eu vou saber quem quer a minha rotina da manhã no próximo."

```text
V19
The person in the image speaks in American English, looking at the camera: "Comment yes if that can is in your fridge right now, and I will know who wants my morning routine next."
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
| T1 | Breaking news out of Hawaii. A video is going viral after she exposed the most poisonous drink for your kidneys, one millions of Americans drink every day. Just watch. | Últimas notícias do Havaí. Um vídeo está viralizando depois que ela expôs a bebida mais venenosa para os seus rins, que milhões de americanos bebem todo dia. Assista. |
| T2 | The most poisonous drink for your kidneys is not alcohol. It is not energy drinks. It is not even apple juice. | A bebida mais venenosa para os seus rins não é o álcool. Não é energético. Nem é suco de maçã. |
| T3 | It is something quieter and more dangerous. And it is very likely sitting in your refrigerator tonight. | É algo mais silencioso e mais perigoso. E muito provavelmente está na sua geladeira hoje à noite. |
| T4 | If you drink it, the fault is not yours. You were taught to believe it was the healthy choice. | Se você bebe, a culpa não é sua. Te ensinaram a acreditar que era a escolha saudável. |
| T5 | So watch this closely, one time, and you will never make this mistake again. | Então assista com atenção, uma vez, e você nunca mais comete esse erro. |
| T6 | This drink is built in a chemical plant. It is full of artificial sweeteners, and your body reads them as a toxin. | Essa bebida é feita numa fábrica química. É cheia de adoçante artificial, e o seu corpo lê isso como toxina. |
| T7 | So the body answers with inflammation, and the kidneys work overtime just to wash it back out. | Então o corpo responde com inflamação, e os rins fazem hora extra só para lavar isso para fora. |
| T8 | Few people understand how much strain these drinks place on the kidneys, or how slowly the body recovers once it starts. | Pouca gente entende o tanto de esforço que essas bebidas põem nos rins, ou como o corpo se recupera devagar depois que começa. |
| T9 | And if you are still wondering which drink I mean, it is diet soda. Zero sugar, diet cola, all of them. | E se você ainda está pensando em qual bebida eu falo, é o refrigerante diet. Zero açúcar, cola diet, todos. |
| T10 | It does not give you clean energy. It takes energy from your future, by silencing the signal that tells you to rest. | Ele não te dá energia limpa. Ele tira energia do seu futuro, calando o sinal que manda você descansar. |
| T11 | The body stays in fight or flight. Slowly, it empties you from the inside, and the kidneys never rest. | O corpo fica em luta ou fuga. Devagar, isso te esvazia por dentro, e os rins nunca descansam. |
| T12 | So I say this to everyone. Stop depending on the can, and go to the root of it, your metabolism. | Então eu digo isso a todo mundo. Pare de depender da latinha e vá na raiz, o seu metabolismo. |
| T13 | When metabolism slows and inflammation spreads through the body, it struggles to keep a healthy fluid balance and to release stubborn weight. | Quando o metabolismo desacelera e a inflamação se espalha pelo corpo, ele luta para manter o equilíbrio de líquidos e para soltar o peso teimoso. [fala real do take] |
| T14 | This is why the belly keeps growing, and nothing you try can move it. It was never your fault. | É por isso que a barriga continua crescendo e nada do que você tenta tira ela do lugar. Nunca foi culpa sua. |
| T15 | For fifty years I have dived for seaweed in this ocean. In all that time, I have found one thing I trust above everything. | Há cinquenta anos eu mergulho atrás de alga neste oceano. Em todo esse tempo, achei uma coisa em que confio acima de tudo. [fala real do take] |
| T16 | Wild Irish sea moss, vitamin D3, ginger for the gut. Sixteen in one gummy. Natural Rems Sea Moss. | Sea moss irlandês selvagem, vitamina D3, gengibre para o intestino, cúrcuma com pimenta-do-reino e óleo de semente preta. Dezesseis numa goma. Natural Rems Sea Moss. [fala real do take] |
| T17 | It is simple. One green apple gummy a day, with food. You chew it, and you are done. It tastes good. | É simples. Uma goma de maçã verde por dia, com comida. Você mastiga e pronto. É gostosa. |
| T18 | Caring for your body should not mean buying sixteen bottles, taking each one alone, or drying seaweed on a table like this one. | Cuidar do corpo não devia ser comprar dezesseis frascos, tomar um por um, ou secar alga numa mesa como esta. |
| T19 | Comment yes if that can is in your fridge right now, and I will know who wants my morning routine next. | Comenta yes se essa latinha está na sua geladeira agora, e eu vou saber quem quer a minha rotina da manhã no próximo. |
| T20 | Search Natural Rems Sea Moss on Amazon. Or tap my profile picture, the link is waiting in my stories, or right there in my bio. | Procure Natural Rems Sea Moss na Amazon. Ou toque na minha foto de perfil, o link está te esperando nos meus stories, ou bem ali na minha bio. |
| T21 | And don't forget to hit that follow button. | E não esquece de apertar o botão de seguir. |

**EN corrido:** Breaking news out of Hawaii. A video is going viral after she exposed the most poisonous drink for your kidneys, one millions of Americans drink every day. Just watch. The most poisonous drink for your kidneys is not alcohol. It is not energy drinks. It is not even apple juice. It is something quieter and more dangerous. And it is very likely sitting in your refrigerator tonight. If you drink it, the fault is not yours. You were taught to believe it was the healthy choice. So watch this closely, one time, and you will never make this mistake again. This drink is built in a chemical plant. It is full of artificial sweeteners, and your body reads them as a toxin. So the body answers with inflammation, and the kidneys work overtime just to wash it back out. Few people understand how much strain these drinks place on the kidneys, or how slowly the body recovers once it starts. And if you are still wondering which drink I mean, it is diet soda. Zero sugar, diet cola, all of them. It does not give you clean energy. It takes energy from your future, by silencing the signal that tells you to rest. The body stays in fight or flight. Slowly, it empties you from the inside, and the kidneys never rest. So I say this to everyone. Stop depending on the can, and go to the root of it, your metabolism. When metabolism slows and inflammation spreads through the body, it struggles to keep a healthy fluid balance and to release stubborn weight. This is why the belly keeps growing, and nothing you try can move it. It was never your fault. For fifty years I have dived for seaweed in this ocean. In all that time, I have found one thing I trust above everything. Wild Irish sea moss, vitamin D3, ginger for the gut. Sixteen in one gummy. Natural Rems Sea Moss. It is simple. One green apple gummy a day, with food. You chew it, and you are done. It tastes good. Caring for your body should not mean buying sixteen bottles, taking each one alone, or drying seaweed on a table like this one. Comment yes if that can is in your fridge right now, and I will know who wants my morning routine next. Search Natural Rems Sea Moss on Amazon. Or tap my profile picture, the link is waiting in my stories, or right there in my bio. And don't forget to hit that follow button.

**PT corrido:** Últimas notícias do Havaí. Um vídeo está viralizando depois que ela expôs a bebida mais venenosa para os seus rins, que milhões de americanos bebem todo dia. Assista. A bebida mais venenosa para os seus rins não é o álcool. Não é energético. Nem é suco de maçã. É algo mais silencioso e mais perigoso. E muito provavelmente está na sua geladeira hoje à noite. Se você bebe, a culpa não é sua. Te ensinaram a acreditar que era a escolha saudável. Então assista com atenção, uma vez, e você nunca mais comete esse erro. Essa bebida é feita numa fábrica química. É cheia de adoçante artificial, e o seu corpo lê isso como toxina. Então o corpo responde com inflamação, e os rins fazem hora extra só para lavar isso para fora. Pouca gente entende o tanto de esforço que essas bebidas põem nos rins, ou como o corpo se recupera devagar depois que começa. E se você ainda está pensando em qual bebida eu falo, é o refrigerante diet. Zero açúcar, cola diet, todos. Ele não te dá energia limpa. Ele tira energia do seu futuro, calando o sinal que manda você descansar. O corpo fica em luta ou fuga. Devagar, isso te esvazia por dentro, e os rins nunca descansam. Então eu digo isso a todo mundo. Pare de depender da latinha e vá na raiz, o seu metabolismo. Quando o metabolismo desacelera e a inflamação se espalha pelo corpo, ele luta para manter o equilíbrio de líquidos e para soltar o peso teimoso. [fala real do take] É por isso que a barriga continua crescendo e nada do que você tenta tira ela do lugar. Nunca foi culpa sua. Há cinquenta anos eu mergulho atrás de alga neste oceano. Em todo esse tempo, achei uma coisa em que confio acima de tudo. [fala real do take] Sea moss irlandês selvagem, vitamina D3, gengibre para o intestino, cúrcuma com pimenta-do-reino e óleo de semente preta. Dezesseis numa goma. Natural Rems Sea Moss. [fala real do take] É simples. Uma goma de maçã verde por dia, com comida. Você mastiga e pronto. É gostosa. Cuidar do corpo não devia ser comprar dezesseis frascos, tomar um por um, ou secar alga numa mesa como esta. Comenta yes se essa latinha está na sua geladeira agora, e eu vou saber quem quer a minha rotina da manhã no próximo. Procure Natural Rems Sea Moss na Amazon. Ou toque na minha foto de perfil, o link está te esperando nos meus stories, ou bem ali na minha bio. E não esquece de apertar o botão de seguir.
