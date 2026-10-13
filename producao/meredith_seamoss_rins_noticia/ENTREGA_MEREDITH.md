# ENTREGA | Meredith Callahan | Sea Moss Venda · pilha de notícia · rins

flow_seguro: v1

Produção `meredith_seamoss_rins_noticia` · Ângulo 1 Sea Moss (conta da Meredith) · VENDA · rodada de VALIDAÇÃO · formato mínimo de prompt do Flow

## 0. INSTRUÇÕES PARA A MEMÓRIA DO AGENTE · GOOGLE FLOW (colar inteiro antes do primeiro K)

```text
# Agente do Flow, produção atual: Sea Moss Venda · pilha de notícia · rins

Você é o executor do Google Flow. Você só gera imagens e vídeos a partir de prompts prontos. Você não cria, não edita e não melhora prompt.

## Produção atual
- Conta: Natural Rems Sea Moss (Meredith), vídeo de venda. Sea Moss Venda · pilha de notícia · rins.
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

**Vídeo: pilha de notícia, a pior bebida para os rins (refrigerante diet).**

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
Television news studio frame, vertical 9:16. A news anchor woman in her late forties with a sleek blonde bob, a sage-green blazer over a black top, seated at a glossy news desk with her hands resting on a few papers, looking straight into the camera, caught mid-sentence with lips naturally parted. Behind her a large window wall shows a city skyline at blue hour, deep blue sky with lit towers. On the left, a large inset photo box beside her showing a close-up photo of a kidney cut in half, pink-orange tissue with a big shiny black stone lodged in the middle, filling about a third of the frame. Across the bottom a red lower-third banner reads BREAKING NEWS in bold white letters with a white strip reading HEALTH ALERT. A small American flag stands on the desk at the right, in sharp focus. Broadcast camera at eye level, 35mm lens, front facing, medium shot from the chest up. Clean even studio light, true neutral colors, real skin texture with visible pores, everything in sharp focus, 9:16 vertical.
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

Cena: A âncora dá a notícia. Fala: "Últimas notícias no Brooklyn. Um vídeo está viralizando depois que ela expôs a bebida mais venenosa para os rins, que milhões de americanos bebem todo dia. Assista."

```text
V01
The person in the image speaks in American English, looking at the camera: "Breaking news in Brooklyn. A video is going viral after she exposed the most poisonous drink for the kidneys that millions of Americans drink every day. Just watch."
Fixed camera. Natural lip sync, no music.
```

### V02 · T2, Eliminação tripla · anexar SÓ a imagem escolhida do K02

Cena: Ela fala para a câmera. Fala: "A pior bebida para os seus rins não é a bebida alcoólica, meu bem, não são aqueles energéticos, e nem é o suco de laranja."

```text
V02
The person in the image speaks in American English, looking at the camera: "The worst drink for your kidneys is not liquor, baby, it is not those energy drinks, and it is not even the orange juice."
Fixed camera. Natural lip sync, no music.
```

### V03 · T3, Proximidade · anexar SÓ a imagem escolhida do K02

Cena: Ela fala para a câmera. Fala: "É algo muito mais perigoso que os três, e agora mesmo deve estar gelado na sua geladeira."

```text
V03
The person in the image speaks in American English, looking at the camera: "It is something much more dangerous than all three, and right now it is probably sitting cold in your fridge."
Fixed camera. Natural lip sync, no music.
```

### V04 · T4, Absolvição · anexar SÓ a imagem escolhida do K02

Cena: Ela fala para a câmera. Fala: "Se você bebe, a culpa não é sua, filha. Venderam isso como a escolha saudável, e você acreditou."

```text
V04
The person in the image speaks in American English, looking at the camera: "If you drink it, this is not your fault, child. They sold it to you as the healthy choice, and you believe them."
Fixed camera. Natural lip sync, no music.
```

### V05 · T5, Ordem de assistir · anexar SÓ a imagem escolhida do K02

Cena: Ela fala para a câmera. Fala: "Então me escuta com atenção, porque depois deste vídeo você nunca mais comete esse erro."

```text
V05
The person in the image speaks in American English, looking at the camera: "So listen to me carefully, because after this video you will never make that mistake again."
Fixed camera. Natural lip sync, no music.
```

### V06 · T6, Mecanismo · anexar SÓ a imagem escolhida do K02

Cena: Ela fala para a câmera. Fala: "Essa bebida sai de uma fábrica química, e é cheia de adoçante artificial que o seu corpo encara como veneno."

```text
V06
The person in the image speaks in American English, looking at the camera: "This drink comes out of a chemical factory, and it is full of artificial sweeteners that your body handles like a poison."
Fixed camera. Natural lip sync, no music.
```

### V07 · T7, Mecanismo · anexar SÓ a imagem escolhida do K02

Cena: Ela fala para a câmera. Fala: "O seu corpo reage com inflamação, e os seus rins têm que fazer hora extra só para jogar tudo isso para fora."

```text
V07
The person in the image speaks in American English, looking at the camera: "Your body fights it with inflammation, and your kidneys have to work overtime just to flush all of it back out."
Fixed camera. Natural lip sync, no music.
```

### V08 · T8, Mecanismo · anexar SÓ a imagem escolhida do K02

Cena: Ela fala para a câmera. Fala: "Quase ninguém pensa no tanto de estresse que isso põe nos rins, ou no tanto que o corpo trabalha para se recuperar."

```text
V08
The person in the image speaks in American English, looking at the camera: "Most folks never think about how much stress this puts on the kidneys, or how hard the body works to bounce back from it."
Fixed camera. Natural lip sync, no music.
```

### V09 · T9, Revelação do vilão · anexar SÓ a imagem escolhida do K02

Cena: Ela fala para a câmera. Fala: "E se você ainda não sabe de que bebida eu estou falando, é o refrigerante diet. Zero açúcar, cola diet, todos eles."

```text
V09
The person in the image speaks in American English, looking at the camera: "And if you still do not know which drink I mean, it is diet soda. Zero sugar soda, diet cola, every single one of them."
Fixed camera. Natural lip sync, no music.
```

### V10 · T10, Virar o benefício · anexar SÓ a imagem escolhida do K02

Cena: Ela fala para a câmera. Fala: "E não, meu bem, ele não te dá energia de verdade. Ele pega emprestada a energia do seu amanhã desligando o sinal que avisa que você está cansada."

```text
V10
The person in the image speaks in American English, looking at the camera: "And no, baby, it does not give you real energy. It borrows energy from your tomorrow by switching off the signal that tells you that you are tired."
Fixed camera. Natural lip sync, no music.
```

### V11 · T11, Virar o benefício · anexar SÓ a imagem escolhida do K02

Cena: Ela fala para a câmera. Fala: "O seu corpo vive em modo luta ou fuga o dia inteiro, isso te esgota por dentro, e os seus rins nunca descansam."

```text
V11
The person in the image speaks in American English, looking at the camera: "Your body lives in fight or flight all day long, it drains you from the inside, and your kidneys never get a break."
Fixed camera. Natural lip sync, no music.
```

### V12 · T12, Causa raiz · anexar SÓ a imagem escolhida do K02

Cena: Ela fala para a câmera. Fala: "Então para de se apoiar nessa latinha e começa a arrumar o que está de verdade por trás disso tudo, o seu metabolismo."

```text
V12
The person in the image speaks in American English, looking at the camera: "So stop leaning on that can, and start fixing what is really behind all of this, your metabolism."
Fixed camera. Natural lip sync, no music.
```

### V13 · T13, Ponte pro sintoma · anexar SÓ a imagem escolhida do K02

Cena: Ela fala para a câmera. Fala: "Quando o metabolismo desacelera e a inflamação se acumula, o corpo tem dificuldade de manter o equilíbrio de líquidos e de soltar aquele peso teimoso."

```text
V13
The person in the image speaks in American English, looking at the camera: "When your metabolism slows down and inflammation builds up, your body has a hard time holding a healthy fluid balance and letting go of stubborn weight."
Fixed camera. Natural lip sync, no music.
```

### V14 · T14, Sintoma visível · anexar SÓ a imagem escolhida do K02

Cena: Ela fala para a câmera. Fala: "É por isso que a barriga continua crescendo e nada do que você tenta faz ela sair. E nada disso foi culpa sua."

```text
V14
The person in the image speaks in American English, looking at the camera: "That is why the belly keeps growing, and nothing you try will move it. And none of that was ever your fault."
Fixed camera. Natural lip sync, no music.
```

### V15 · T15, Autoridade e exclusividade · anexar SÓ a imagem escolhida do K03

Cena: Ela segura o pote parado, rótulo legível. Fala: "Quarenta anos fazendo sea moss para o bairro inteiro, filha, e eu achei uma coisa."

```text
V15
The person in the image speaks in American English, looking at the camera: "Forty years I have been making sea moss for this whole neighborhood, child, and I have found one thing I trust above everything else."
Fixed camera. Natural lip sync, no music.
```

### V16 · T16, Ingrediente antes da marca · anexar SÓ a imagem escolhida do K03

Cena: Ela segura o pote parado, rótulo legível. Fala: "Sea moss irlandês selvagem, vitamina D3, gengibre para o intestino. Chama Natural Rems Sea Moss."

```text
V16
The person in the image speaks in American English, looking at the camera: "Wild Irish sea moss, vitamin D3, ginger for your gut. It is called Natural Rems Sea Moss."
Fixed camera. Natural lip sync, no music.
```

### V17 · T17, Matar a fricção · anexar SÓ a imagem escolhida do K03

Cena: Ela segura o pote parado, rótulo legível. Fala: "E é fácil, meu bem. Você só mastiga uma goma de maçã verde por dia com a comida, e pronto. E é gostosa."

```text
V17
The person in the image speaks in American English, looking at the camera: "And it is easy, baby. You just chew one green apple gummy a day with your food, and you are done. It tastes good, too."
Fixed camera. Natural lip sync, no music.
```

### V18 · T18, Reenquadrar o custo · anexar SÓ a imagem escolhida do K03

Cena: Ela segura o pote parado, rótulo legível. Fala: "Se cuidar não devia ser pagar dezesseis frascos e engolir um por um, nem cozinhar uma panela como a minha toda manhã."

```text
V18
The person in the image speaks in American English, looking at the camera: "Taking care of yourself should not mean paying for sixteen bottles and swallowing them one by one, or cooking a pot like mine every morning."
Fixed camera. Natural lip sync, no music.
```

### V19 · T19, Comentário · anexar SÓ a imagem escolhida do K03

Cena: Ela segura o pote parado, rótulo legível. Fala: "Comenta yes se essa latinha mora na sua geladeira, pra eu saber quem precisa da minha rotina da manhã no próximo vídeo."

```text
V19
The person in the image speaks in American English, looking at the camera: "Comment yes if that can has been living in your fridge, so I know who needs my morning routine in the next video."
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
| T1 | Breaking news in Brooklyn. A video is going viral after she exposed the most poisonous drink for the kidneys that millions of Americans drink every day. Just watch. | Últimas notícias no Brooklyn. Um vídeo está viralizando depois que ela expôs a bebida mais venenosa para os rins, que milhões de americanos bebem todo dia. Assista. |
| T2 | The worst drink for your kidneys is not liquor, baby, it is not those energy drinks, and it is not even the orange juice. | A pior bebida para os seus rins não é a bebida alcoólica, meu bem, não são aqueles energéticos, e nem é o suco de laranja. |
| T3 | It is something much more dangerous than all three, and right now it is probably sitting cold in your fridge. | É algo muito mais perigoso que os três, e agora mesmo deve estar gelado na sua geladeira. |
| T4 | If you drink it, this is not your fault, child. They sold it to you as the healthy choice, and you believe them. | Se você bebe, a culpa não é sua, filha. Venderam isso como a escolha saudável, e você acreditou. |
| T5 | So listen to me carefully, because after this video you will never make that mistake again. | Então me escuta com atenção, porque depois deste vídeo você nunca mais comete esse erro. |
| T6 | This drink comes out of a chemical factory, and it is full of artificial sweeteners that your body handles like a poison. | Essa bebida sai de uma fábrica química, e é cheia de adoçante artificial que o seu corpo encara como veneno. |
| T7 | Your body fights it with inflammation, and your kidneys have to work overtime just to flush all of it back out. | O seu corpo reage com inflamação, e os seus rins têm que fazer hora extra só para jogar tudo isso para fora. |
| T8 | Most folks never think about how much stress this puts on the kidneys, or how hard the body works to bounce back from it. | Quase ninguém pensa no tanto de estresse que isso põe nos rins, ou no tanto que o corpo trabalha para se recuperar. |
| T9 | And if you still do not know which drink I mean, it is diet soda. Zero sugar soda, diet cola, every single one of them. | E se você ainda não sabe de que bebida eu estou falando, é o refrigerante diet. Zero açúcar, cola diet, todos eles. |
| T10 | And no, baby, it does not give you real energy. It borrows energy from your tomorrow by switching off the signal that tells you that you are tired. | E não, meu bem, ele não te dá energia de verdade. Ele pega emprestada a energia do seu amanhã desligando o sinal que avisa que você está cansada. |
| T11 | Your body lives in fight or flight all day long, it drains you from the inside, and your kidneys never get a break. | O seu corpo vive em modo luta ou fuga o dia inteiro, isso te esgota por dentro, e os seus rins nunca descansam. |
| T12 | So stop leaning on that can, and start fixing what is really behind all of this, your metabolism. | Então para de se apoiar nessa latinha e começa a arrumar o que está de verdade por trás disso tudo, o seu metabolismo. |
| T13 | When your metabolism slows down and inflammation builds up, your body has a hard time holding a healthy fluid balance and letting go of stubborn weight. | Quando o metabolismo desacelera e a inflamação se acumula, o corpo tem dificuldade de manter o equilíbrio de líquidos e de soltar aquele peso teimoso. |
| T14 | That is why the belly keeps growing, and nothing you try will move it. And none of that was ever your fault. | É por isso que a barriga continua crescendo e nada do que você tenta faz ela sair. E nada disso foi culpa sua. |
| T15 | Forty years I have been making sea moss for this whole neighborhood, child, and I have found one thing I trust above everything else. | Quarenta anos fazendo sea moss para o bairro inteiro, filha, e eu achei uma coisa. |
| T16 | Wild Irish sea moss, vitamin D3, ginger for your gut. It is called Natural Rems Sea Moss. | Sea moss irlandês selvagem, vitamina D3, gengibre para o intestino. Chama Natural Rems Sea Moss. |
| T17 | And it is easy, baby. You just chew one green apple gummy a day with your food, and you are done. It tastes good, too. | E é fácil, meu bem. Você só mastiga uma goma de maçã verde por dia com a comida, e pronto. E é gostosa. |
| T18 | Taking care of yourself should not mean paying for sixteen bottles and swallowing them one by one, or cooking a pot like mine every morning. | Se cuidar não devia ser pagar dezesseis frascos e engolir um por um, nem cozinhar uma panela como a minha toda manhã. |
| T19 | Comment yes if that can has been living in your fridge, so I know who needs my morning routine in the next video. | Comenta yes se essa latinha mora na sua geladeira, pra eu saber quem precisa da minha rotina da manhã no próximo vídeo. |
| T20 | Search Natural Rems Sea Moss on Amazon. Or tap my profile picture, the link is waiting in my stories, or right there in my bio. | Procure Natural Rems Sea Moss na Amazon. Ou toque na minha foto de perfil, o link está te esperando nos meus stories, ou bem ali na minha bio. |
| T21 | And don't forget to hit that follow button. | E não esquece de apertar o botão de seguir. |

**EN corrido:** Breaking news in Brooklyn. A video is going viral after she exposed the most poisonous drink for the kidneys that millions of Americans drink every day. Just watch. The worst drink for your kidneys is not liquor, baby, it is not those energy drinks, and it is not even the orange juice. It is something much more dangerous than all three, and right now it is probably sitting cold in your fridge. If you drink it, this is not your fault, child. They sold it to you as the healthy choice, and you believe them. So listen to me carefully, because after this video you will never make that mistake again. This drink comes out of a chemical factory, and it is full of artificial sweeteners that your body handles like a poison. Your body fights it with inflammation, and your kidneys have to work overtime just to flush all of it back out. Most folks never think about how much stress this puts on the kidneys, or how hard the body works to bounce back from it. And if you still do not know which drink I mean, it is diet soda. Zero sugar soda, diet cola, every single one of them. And no, baby, it does not give you real energy. It borrows energy from your tomorrow by switching off the signal that tells you that you are tired. Your body lives in fight or flight all day long, it drains you from the inside, and your kidneys never get a break. So stop leaning on that can, and start fixing what is really behind all of this, your metabolism. When your metabolism slows down and inflammation builds up, your body has a hard time holding a healthy fluid balance and letting go of stubborn weight. That is why the belly keeps growing, and nothing you try will move it. And none of that was ever your fault. Forty years I have been making sea moss for this whole neighborhood, child, and I have found one thing I trust above everything else. Wild Irish sea moss, vitamin D3, ginger for your gut. It is called Natural Rems Sea Moss. And it is easy, baby. You just chew one green apple gummy a day with your food, and you are done. It tastes good, too. Taking care of yourself should not mean paying for sixteen bottles and swallowing them one by one, or cooking a pot like mine every morning. Comment yes if that can has been living in your fridge, so I know who needs my morning routine in the next video. Search Natural Rems Sea Moss on Amazon. Or tap my profile picture, the link is waiting in my stories, or right there in my bio. And don't forget to hit that follow button.

**PT corrido:** Últimas notícias no Brooklyn. Um vídeo está viralizando depois que ela expôs a bebida mais venenosa para os rins, que milhões de americanos bebem todo dia. Assista. A pior bebida para os seus rins não é a bebida alcoólica, meu bem, não são aqueles energéticos, e nem é o suco de laranja. É algo muito mais perigoso que os três, e agora mesmo deve estar gelado na sua geladeira. Se você bebe, a culpa não é sua, filha. Venderam isso como a escolha saudável, e você acreditou. Então me escuta com atenção, porque depois deste vídeo você nunca mais comete esse erro. Essa bebida sai de uma fábrica química, e é cheia de adoçante artificial que o seu corpo encara como veneno. O seu corpo reage com inflamação, e os seus rins têm que fazer hora extra só para jogar tudo isso para fora. Quase ninguém pensa no tanto de estresse que isso põe nos rins, ou no tanto que o corpo trabalha para se recuperar. E se você ainda não sabe de que bebida eu estou falando, é o refrigerante diet. Zero açúcar, cola diet, todos eles. E não, meu bem, ele não te dá energia de verdade. Ele pega emprestada a energia do seu amanhã desligando o sinal que avisa que você está cansada. O seu corpo vive em modo luta ou fuga o dia inteiro, isso te esgota por dentro, e os seus rins nunca descansam. Então para de se apoiar nessa latinha e começa a arrumar o que está de verdade por trás disso tudo, o seu metabolismo. Quando o metabolismo desacelera e a inflamação se acumula, o corpo tem dificuldade de manter o equilíbrio de líquidos e de soltar aquele peso teimoso. É por isso que a barriga continua crescendo e nada do que você tenta faz ela sair. E nada disso foi culpa sua. Quarenta anos fazendo sea moss para o bairro inteiro, filha, e eu achei uma coisa. Sea moss irlandês selvagem, vitamina D3, gengibre para o intestino. Chama Natural Rems Sea Moss. E é fácil, meu bem. Você só mastiga uma goma de maçã verde por dia com a comida, e pronto. E é gostosa. Se cuidar não devia ser pagar dezesseis frascos e engolir um por um, nem cozinhar uma panela como a minha toda manhã. Comenta yes se essa latinha mora na sua geladeira, pra eu saber quem precisa da minha rotina da manhã no próximo vídeo. Procure Natural Rems Sea Moss na Amazon. Ou toque na minha foto de perfil, o link está te esperando nos meus stories, ou bem ali na minha bio. E não esquece de apertar o botão de seguir.
