# ENTREGA | Marshall Beckett | Sea Moss Venda · pilha de notícia · seios

flow_seguro: v1

Produção `marshall_seamoss_seios_noticia` · Ângulo 1 Sea Moss (conta da Marshall) · VENDA · rodada de VALIDAÇÃO · formato mínimo de prompt do Flow

## 0. INSTRUÇÕES PARA A MEMÓRIA DO AGENTE · GOOGLE FLOW (colar inteiro antes do primeiro K)

```text
# Agente do Flow, produção atual: Sea Moss Venda · pilha de notícia · seios

Você é o executor do Google Flow. Você só gera imagens e vídeos a partir de prompts prontos. Você não cria, não edita e não melhora prompt.

## Produção atual
- Conta: Natural Rems Sea Moss (Marshall), vídeo de venda. Sea Moss Venda · pilha de notícia · seios.
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

**Vídeo: pilha de notícia, a pior comida para os seios (laticínio).**

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
Television news studio frame, vertical 9:16. A news anchor woman in her early fifties with shoulder-length dark brown hair, a navy-blue blazer over a white top, seated at a glossy news desk with her hands resting on a few papers, looking straight into the camera, caught mid-sentence with lips naturally parted. Behind her a large window wall shows a city skyline at blue hour, deep blue sky with lit towers. On the left, a large inset photo box beside her showing a close-up photo of two big round green coconuts hanging side by side from the top of a palm trunk, under the palm fronds, a funny suggestive shape, filling about a third of the frame. Across the bottom a red lower-third banner reads BREAKING NEWS in bold white letters with a white strip reading HEALTH ALERT. A small American flag stands on the desk at the right, in sharp focus. Broadcast camera at eye level, 35mm lens, front facing, medium shot from the chest up. Clean even studio light, true neutral colors, real skin texture with visible pores, everything in sharp focus, 9:16 vertical.
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

Cena: A âncora dá a notícia. Fala: "Últimas notícias. Uma mulher do Havaí está viralizando depois de revelar a comida mais venenosa para os seus seios, e ela está em quase toda geladeira. Assista."

```text
V01
The person in the image speaks in American English, looking at the camera: "Breaking news. A woman from Hawaii is going viral after she revealed the most poisonous food for your breasts, and it sits in nearly every fridge. Just watch."
Fixed camera. Natural lip sync, no music.
```

### V02 · T2, Eliminação tripla · anexar SÓ a imagem escolhida do K02

Cena: Ela fala para a câmera. Fala: "A comida mais venenosa para os seus seios não é fast food. Não é pizza. Nem é sorvete."

```text
V02
The person in the image speaks in American English, looking at the camera: "The most poisonous food for your breasts is not fast food. It is not pizza. It is not even ice cream."
Fixed camera. Natural lip sync, no music.
```

### V03 · T3, Proximidade · anexar SÓ a imagem escolhida do K02

Cena: Ela fala para a câmera. Fala: "É pior que todos eles, e está escondida na sua frente, na prateleira de cima da sua geladeira."

```text
V03
The person in the image speaks in American English, looking at the camera: "It is worse than all of them, and it is hiding in front of you, on the top shelf of your refrigerator."
Fixed camera. Natural lip sync, no music.
```

### V04 · T4, Absolvição · anexar SÓ a imagem escolhida do K02

Cena: Ela fala para a câmera. Fala: "Se ela está na sua casa, não se culpe. Por anos te disseram que fazia bem."

```text
V04
The person in the image speaks in American English, looking at the camera: "If it is in your house, do not blame yourself. For years you were told it was good for you."
Fixed camera. Natural lip sync, no music.
```

### V05 · T5, Ordem de assistir · anexar SÓ a imagem escolhida do K02

Cena: Ela fala para a câmera. Fala: "Então escute a próxima parte devagar. Depois de ouvir, você vai olhar a sua geladeira de outro jeito."

```text
V05
The person in the image speaks in American English, looking at the camera: "So listen to the next part slowly. Once you hear it, you will look at your fridge differently."
Fixed camera. Natural lip sync, no music.
```

### V06 · T6, Mecanismo · anexar SÓ a imagem escolhida do K02

Cena: Ela fala para a câmera. Fala: "Ela tem hormônios e fatores de crescimento. Quando eles entram no seu corpo, o corpo responde com inflamação, como se fosse uma toxina."

```text
V06
The person in the image speaks in American English, looking at the camera: "It holds hormones and growth factors. When they enter your body, the body answers with inflammation, as if it were a toxin."
Fixed camera. Natural lip sync, no music.
```

### V07 · T7, Mecanismo · anexar SÓ a imagem escolhida do K02

Cena: Ela fala para a câmera. Fala: "E essa inflamação desgasta o colágeno e o tecido que mantêm o seu peito firme e cheio."

```text
V07
The person in the image speaks in American English, looking at the camera: "And that inflammation wears down the collagen and the tissue that hold your chest firm and full."
Fixed camera. Natural lip sync, no music.
```

### V08 · T8, Mecanismo · anexar SÓ a imagem escolhida do K02

Cena: Ela fala para a câmera. Fala: "Ela também traz antibióticos e compostos que o corpo humano nunca foi feito para receber, e os seus hormônios perdem o equilíbrio. [fala real do take]"

```text
V08
The person in the image speaks in American English, looking at the camera: "It also carries antibiotics and compounds the human body was never made to receive."
Fixed camera. Natural lip sync, no music.
```

### V09 · T9, Mecanismo · anexar SÓ a imagem escolhida do K02

Cena: Ela fala para a câmera. Fala: "E o cálcio que prometeram? Mal é absorvido. Então você fica com os hormônios e perde o benefício."

```text
V09
The person in the image speaks in American English, looking at the camera: "And the calcium they promised? It barely absorbs. So you take in the hormones and miss the benefit."
Fixed camera. Natural lip sync, no music.
```

### V10 · T10, Revelação do vilão · anexar SÓ a imagem escolhida do K02

Cena: Ela fala para a câmera. Fala: "Se você ainda não adivinhou a comida, é o laticínio. Leite, queijo, creme, de todo tipo."

```text
V10
The person in the image speaks in American English, looking at the camera: "If you still have not guessed the food, it is dairy. Milk, cheese, cream, every kind of it."
Fixed camera. Natural lip sync, no music.
```

### V11 · T11, Sintoma visível · anexar SÓ a imagem escolhida do K02

Cena: Ela fala para a câmera. Fala: "Quando o corpo está inflamado por dentro, o colágeno se desfaz, o tecido do peito afina e cai, e a firmeza some."

```text
V11
The person in the image speaks in American English, looking at the camera: "When the body is inflamed inside, collagen breaks down, the tissue of the chest thins and sags, and the firmness fades."
Fixed camera. Natural lip sync, no music.
```

### V12 · T12, Sintoma visível · anexar SÓ a imagem escolhida do K02

Cena: Ela fala para a câmera. Fala: "Nenhum sutiã resolve, e perder peso não traz de volta. Você evita algumas blusas, e tirar a roupa vira algo que você teme."

```text
V12
The person in the image speaks in American English, looking at the camera: "No bra fixes it, and losing weight does not bring it back. You avoid some tops, and undressing becomes something you dread."
Fixed camera. Natural lip sync, no music.
```

### V13 · T13, Absolvição + causa · anexar SÓ a imagem escolhida do K02

Cena: Ela fala para a câmera. Fala: "Aí você se culpa, mas nunca foi você. Nem a gravidade, nem a idade. É inflamação, em silêncio, de dentro."

```text
V13
The person in the image speaks in American English, looking at the camera: "Then you blame yourself, but it was never you. Not gravity, not age. It is inflammation, quietly, from the inside."
Fixed camera. Natural lip sync, no music.
```

### V14 · T14, Virada · anexar SÓ a imagem escolhida do K02

Cena: Ela fala para a câmera. Fala: "Agora a parte boa. O seu corpo consegue se cuidar quando você dá o apoio de que ele precisa."

```text
V14
The person in the image speaks in American English, looking at the camera: "Here is the good part. Your body can take care of itself, when you give it the support it needs."
Fixed camera. Natural lip sync, no music.
```

### V15 · T15, Autoridade e exclusividade · anexar SÓ a imagem escolhida do K03

Cena: Ela segura o pote parado, rótulo legível. Fala: "Cinquenta anos neste oceano, colhendo alga com as minhas mãos. E tem uma coisa que eu tomo toda manhã."

```text
V15
The person in the image speaks in American English, looking at the camera: "Fifty years in this ocean, harvesting seaweed with my own hands. And there is one thing I take every morning."
Fixed camera. Natural lip sync, no music.
```

### V16 · T16, Ingrediente antes da marca · anexar SÓ a imagem escolhida do K03

Cena: Ela segura o pote parado, rótulo legível. Fala: "Sea moss irlandês selvagem, vitamina C para a formação normal de colágeno, cúrcuma e pimenta-do-reino, e gengibre. Dezesseis numa goma. Natural Rems Sea Moss."

```text
V16
The person in the image speaks in American English, looking at the camera: "Wild Irish sea moss, vitamin C for normal collagen formation, turmeric and black pepper, and ginger. Sixteen in one gummy. Natural Rems Sea Moss."
Fixed camera. Natural lip sync, no music.
```

### V17 · T17, Benefício do rótulo · anexar SÓ a imagem escolhida do K03

Cena: Ela segura o pote parado, rótulo legível. Fala: "Então você apoia a sua pele por dentro. E quando você se sente em casa no seu corpo, se vestir fica diferente."

```text
V17
The person in the image speaks in American English, looking at the camera: "So you support your skin from within. And when you feel at home in your body, getting dressed feels different."
Fixed camera. Natural lip sync, no music.
```

### V18 · T18, Fricção + custo · anexar SÓ a imagem escolhida do K03

Cena: Ela segura o pote parado, rótulo legível. Fala: "Uma goma de maçã verde no meu café da manhã. Umas mastigadas e acabou. Sem dezesseis frascos, sem alga para secar."

```text
V18
The person in the image speaks in American English, looking at the camera: "One green apple gummy with my breakfast. A few chews, and it is over. No sixteen bottles, no seaweed to dry."
Fixed camera. Natural lip sync, no music.
```

### V19 · T19, Comentário · anexar SÓ a imagem escolhida do K03

Cena: Ela segura o pote parado, rótulo legível. Fala: "Comenta yes se tem laticínio na sua geladeira hoje, e eu te mostro a minha rotina da manhã no próximo vídeo."

```text
V19
The person in the image speaks in American English, looking at the camera: "Comment yes if there is dairy in your refrigerator today, and I will show you my morning routine in the next video."
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
| T1 | Breaking news. A woman from Hawaii is going viral after she revealed the most poisonous food for your breasts, and it sits in nearly every fridge. Just watch. | Últimas notícias. Uma mulher do Havaí está viralizando depois de revelar a comida mais venenosa para os seus seios, e ela está em quase toda geladeira. Assista. |
| T2 | The most poisonous food for your breasts is not fast food. It is not pizza. It is not even ice cream. | A comida mais venenosa para os seus seios não é fast food. Não é pizza. Nem é sorvete. |
| T3 | It is worse than all of them, and it is hiding in front of you, on the top shelf of your refrigerator. | É pior que todos eles, e está escondida na sua frente, na prateleira de cima da sua geladeira. |
| T4 | If it is in your house, do not blame yourself. For years you were told it was good for you. | Se ela está na sua casa, não se culpe. Por anos te disseram que fazia bem. |
| T5 | So listen to the next part slowly. Once you hear it, you will look at your fridge differently. | Então escute a próxima parte devagar. Depois de ouvir, você vai olhar a sua geladeira de outro jeito. |
| T6 | It holds hormones and growth factors. When they enter your body, the body answers with inflammation, as if it were a toxin. | Ela tem hormônios e fatores de crescimento. Quando eles entram no seu corpo, o corpo responde com inflamação, como se fosse uma toxina. |
| T7 | And that inflammation wears down the collagen and the tissue that hold your chest firm and full. | E essa inflamação desgasta o colágeno e o tecido que mantêm o seu peito firme e cheio. |
| T8 | It also carries antibiotics and compounds the human body was never made to receive. | Ela também traz antibióticos e compostos que o corpo humano nunca foi feito para receber, e os seus hormônios perdem o equilíbrio. [fala real do take] |
| T9 | And the calcium they promised? It barely absorbs. So you take in the hormones and miss the benefit. | E o cálcio que prometeram? Mal é absorvido. Então você fica com os hormônios e perde o benefício. |
| T10 | If you still have not guessed the food, it is dairy. Milk, cheese, cream, every kind of it. | Se você ainda não adivinhou a comida, é o laticínio. Leite, queijo, creme, de todo tipo. |
| T11 | When the body is inflamed inside, collagen breaks down, the tissue of the chest thins and sags, and the firmness fades. | Quando o corpo está inflamado por dentro, o colágeno se desfaz, o tecido do peito afina e cai, e a firmeza some. |
| T12 | No bra fixes it, and losing weight does not bring it back. You avoid some tops, and undressing becomes something you dread. | Nenhum sutiã resolve, e perder peso não traz de volta. Você evita algumas blusas, e tirar a roupa vira algo que você teme. |
| T13 | Then you blame yourself, but it was never you. Not gravity, not age. It is inflammation, quietly, from the inside. | Aí você se culpa, mas nunca foi você. Nem a gravidade, nem a idade. É inflamação, em silêncio, de dentro. |
| T14 | Here is the good part. Your body can take care of itself, when you give it the support it needs. | Agora a parte boa. O seu corpo consegue se cuidar quando você dá o apoio de que ele precisa. |
| T15 | Fifty years in this ocean, harvesting seaweed with my own hands. And there is one thing I take every morning. | Cinquenta anos neste oceano, colhendo alga com as minhas mãos. E tem uma coisa que eu tomo toda manhã. |
| T16 | Wild Irish sea moss, vitamin C for normal collagen formation, turmeric and black pepper, and ginger. Sixteen in one gummy. Natural Rems Sea Moss. | Sea moss irlandês selvagem, vitamina C para a formação normal de colágeno, cúrcuma e pimenta-do-reino, e gengibre. Dezesseis numa goma. Natural Rems Sea Moss. |
| T17 | So you support your skin from within. And when you feel at home in your body, getting dressed feels different. | Então você apoia a sua pele por dentro. E quando você se sente em casa no seu corpo, se vestir fica diferente. |
| T18 | One green apple gummy with my breakfast. A few chews, and it is over. No sixteen bottles, no seaweed to dry. | Uma goma de maçã verde no meu café da manhã. Umas mastigadas e acabou. Sem dezesseis frascos, sem alga para secar. |
| T19 | Comment yes if there is dairy in your refrigerator today, and I will show you my morning routine in the next video. | Comenta yes se tem laticínio na sua geladeira hoje, e eu te mostro a minha rotina da manhã no próximo vídeo. |
| T20 | Search Natural Rems Sea Moss on Amazon. Or tap my profile picture, the link is waiting in my stories, or right there in my bio. | Procure Natural Rems Sea Moss na Amazon. Ou toque na minha foto de perfil, o link está te esperando nos meus stories, ou bem ali na minha bio. |
| T21 | And don't forget to hit that follow button. | E não esquece de apertar o botão de seguir. |

**EN corrido:** Breaking news. A woman from Hawaii is going viral after she revealed the most poisonous food for your breasts, and it sits in nearly every fridge. Just watch. The most poisonous food for your breasts is not fast food. It is not pizza. It is not even ice cream. It is worse than all of them, and it is hiding in front of you, on the top shelf of your refrigerator. If it is in your house, do not blame yourself. For years you were told it was good for you. So listen to the next part slowly. Once you hear it, you will look at your fridge differently. It holds hormones and growth factors. When they enter your body, the body answers with inflammation, as if it were a toxin. And that inflammation wears down the collagen and the tissue that hold your chest firm and full. It also carries antibiotics and compounds the human body was never made to receive. And the calcium they promised? It barely absorbs. So you take in the hormones and miss the benefit. If you still have not guessed the food, it is dairy. Milk, cheese, cream, every kind of it. When the body is inflamed inside, collagen breaks down, the tissue of the chest thins and sags, and the firmness fades. No bra fixes it, and losing weight does not bring it back. You avoid some tops, and undressing becomes something you dread. Then you blame yourself, but it was never you. Not gravity, not age. It is inflammation, quietly, from the inside. Here is the good part. Your body can take care of itself, when you give it the support it needs. Fifty years in this ocean, harvesting seaweed with my own hands. And there is one thing I take every morning. Wild Irish sea moss, vitamin C for normal collagen formation, turmeric and black pepper, and ginger. Sixteen in one gummy. Natural Rems Sea Moss. So you support your skin from within. And when you feel at home in your body, getting dressed feels different. One green apple gummy with my breakfast. A few chews, and it is over. No sixteen bottles, no seaweed to dry. Comment yes if there is dairy in your refrigerator today, and I will show you my morning routine in the next video. Search Natural Rems Sea Moss on Amazon. Or tap my profile picture, the link is waiting in my stories, or right there in my bio. And don't forget to hit that follow button.

**PT corrido:** Últimas notícias. Uma mulher do Havaí está viralizando depois de revelar a comida mais venenosa para os seus seios, e ela está em quase toda geladeira. Assista. A comida mais venenosa para os seus seios não é fast food. Não é pizza. Nem é sorvete. É pior que todos eles, e está escondida na sua frente, na prateleira de cima da sua geladeira. Se ela está na sua casa, não se culpe. Por anos te disseram que fazia bem. Então escute a próxima parte devagar. Depois de ouvir, você vai olhar a sua geladeira de outro jeito. Ela tem hormônios e fatores de crescimento. Quando eles entram no seu corpo, o corpo responde com inflamação, como se fosse uma toxina. E essa inflamação desgasta o colágeno e o tecido que mantêm o seu peito firme e cheio. Ela também traz antibióticos e compostos que o corpo humano nunca foi feito para receber, e os seus hormônios perdem o equilíbrio. [fala real do take] E o cálcio que prometeram? Mal é absorvido. Então você fica com os hormônios e perde o benefício. Se você ainda não adivinhou a comida, é o laticínio. Leite, queijo, creme, de todo tipo. Quando o corpo está inflamado por dentro, o colágeno se desfaz, o tecido do peito afina e cai, e a firmeza some. Nenhum sutiã resolve, e perder peso não traz de volta. Você evita algumas blusas, e tirar a roupa vira algo que você teme. Aí você se culpa, mas nunca foi você. Nem a gravidade, nem a idade. É inflamação, em silêncio, de dentro. Agora a parte boa. O seu corpo consegue se cuidar quando você dá o apoio de que ele precisa. Cinquenta anos neste oceano, colhendo alga com as minhas mãos. E tem uma coisa que eu tomo toda manhã. Sea moss irlandês selvagem, vitamina C para a formação normal de colágeno, cúrcuma e pimenta-do-reino, e gengibre. Dezesseis numa goma. Natural Rems Sea Moss. Então você apoia a sua pele por dentro. E quando você se sente em casa no seu corpo, se vestir fica diferente. Uma goma de maçã verde no meu café da manhã. Umas mastigadas e acabou. Sem dezesseis frascos, sem alga para secar. Comenta yes se tem laticínio na sua geladeira hoje, e eu te mostro a minha rotina da manhã no próximo vídeo. Procure Natural Rems Sea Moss na Amazon. Ou toque na minha foto de perfil, o link está te esperando nos meus stories, ou bem ali na minha bio. E não esquece de apertar o botão de seguir.
