# Operação Vídeos Avatares IA — regras de trabalho

Este arquivo é carregado automaticamente em toda sessão. É a fonte de verdade do PROCESSO.
Copy, ângulos, obstáculos e rotas argumentativas ficam na memória. Aqui fica **como entregar**.

---

## Antes de começar QUALQUER produção

1. Rodar `/watch` no `.mp4`.
2. **Ler `producao/brandon_angle2/ROTEIRO.md` e `PROMPTS_PRODUCAO.md`.** São o gabarito vivo. Nunca reinventar o formato de memória.
3. Perguntar o ângulo (1 Korella / 2 FityWell / 3 Auraly / 4 Body Hacks For Men) e confirmar o avatar.
   **Exceção do avatar:** `.mp4` + imagem de avatar na mesma mensagem já decide para quem é,
   ver a seção do Ângulo 3. Nesse caso só resta perguntar o ângulo.
   **Ângulo 3 tem fluxo próprio**, ver a seção no fim deste arquivo. O passo 1 vira opcional lá.
4. Criar a pasta `producao/<avatar>_<slug>/` e escrever os DOIS arquivos.

## A entrega tem SEMPRE dois arquivos + tudo colado na conversa
(**três no Ângulo 3**, com o `DM.md`)

Arquivo não substitui o chat, e chat não substitui o arquivo. **Os dois, sempre.**

### `producao/<avatar>_<slug>/ROTEIRO.md`
Nesta ordem, sem pular seção:
1. Cabeçalho: vídeo modelo, avatar, variável trocada, funil, enquadramento do avatar
2. **Tabela de esqueleto preservado** (`# | Beat | Original | Adaptado`)
3. **Setups de cena** (Setup A, B, C... = os blocos de imagem)
4. Roteiro cena a cena: `### T1 · BEAT · TALKING|B-ROLL · Setup A`
5. Roteiro só-fala (inglês, pra TTS)
6. Notas de produção (duração, herói do hook, compliance, o que cortar se ficar longo)

### `producao/<avatar>_<slug>/PROMPTS_PRODUCAO.md`
Nesta ordem, sem pular seção:
1. Cabeçalho: vídeo modelo, caminho da âncora, funil
2. **Índice de geração** (`Take | Keyframe | Ação de geração`)
3. **Trava de identidade e continuidade** (bloco único, reaproveitado, não repetir em cada JSON)
4. **Trava do prop herói** (se houver)
5. **Trava da 2ª pessoa (REF-A)**, gerar e aprovar ANTES de tudo
6. Prompts de imagem: `K01`, `K02`... JSON
7. **Bloco global de vídeo** (colar em todo prompt)
8. Prompts de vídeo: `V01 · T1 · usa K01`, texto simples
9. **Mapa de âncoras** (`Keyframe | Referências a anexar | Modelo`)
10. **Montagem no CapCut**
11. **Gates de qualidade** (checklist numerado)

## Nomenclatura, nunca misturar

| Prefixo | O que é |
|---|---|
| `T__` | Take do roteiro (a fala) |
| `K__` | Keyframe, a imagem |
| `V__` | Clipe de vídeo |
| `REF-__` | Referência auxiliar (2ª pessoa, prop) |

Vários `T` podem usar o mesmo `K`. Cada `T` tem seu `V`.

## Imagem: gerar do zero é exceção

`GERAR DO ZERO` só no primeiro keyframe de cada setup. Todo o resto é **`EDITAR do K__`**, que trava rosto, fundo e luz.
Gerar tudo do zero faz a identidade derivar entre blocos.
Estágios sempre a partir do original, **nunca em cascata**.

## Prompt de imagem = JSON. Prompt de vídeo = texto simples.

**Nunca misturar.** O prompt de vídeo não descreve enquadramento, cor nem composição, isso já está na imagem. Ele só carrega fala, ação, câmera e som.

Formato de vídeo (Fase 7), os cinco blocos:
```
o avatar (mulher) fala em inglês com sotaque americano de [avatar], voz autêntica, dinâmica, apaixonada e emocional, como se exigisse ser ouvida, a seguinte frase: "[FALA EXATA DO ROTEIRO]"

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: [ação ENXUTA, só o que acontece]

câmera: [fixa / leve push-in / leve handheld]

som ambiente: [ambiente], sem música
```
B-ROLL: trocar a primeira linha por `(sem fala no take: a fala N entra como voz-over na edição)`.

## Regras que quebram a entrega se forem ignoradas

- **8 segundos por take = 13 a 29 palavras.** Contar ANTES de escrever os prompts. Take longo se quebra em fim de frase. **Nunca inventar filler, nunca parafrasear.**
- **A fala no prompt é cópia literal do roteiro final.**
- **Keyword por ângulo: `yes` nos Ângulos 1, 2 e 4, `222` no Ângulo 3 (Auraly).** Nunca a palavra do vídeo original. No Ângulo 4 a keyword é provisória, ver a seção dele.
- **Zero travessão (`—`)** em copy, roteiro e resposta.
- **Reveal contínuo dentro de um take = UMA imagem** do estado inicial. Se o original corta, aí sim são imagens separadas.
- **Um prompt de imagem por SETUP**, não por take.
- **Rodar o GATE DE REALISMO junto com o de composição** (memória `realismo-anti-cara-de-ia`): herói isolado com
  duas ou três âncoras de fundo no máximo, luz **neutra de dia nublado** e nunca quente, negative carregando
  `no warm orange color cast, no yellow tint`, e partir sempre de algo real. Realismo é volume de regeneração.
- **Rodar o gate de composição visual ANTES de escrever os prompts** (memória `checklist-composicao-visual`): herói no lower foreground mais perto que o rosto, sempre mais perto do que parece certo, 2ª pessoa cortada pelo quadro, cenário reconhecível e nunca inventariado. Reduzir fundo é com enquadramento, nunca com blur.
- **Bandeira dos EUA em TODO prompt de imagem, discreta porém VISÍVEL e em foco.** Escrever no campo
  `scene`, contando como uma das três âncoras de fundo. Única exceção: prompt de REF de prop isolado
  (REF-CARTA, `product.png`), que não tem cenário e contaminaria todo keyframe que anexasse a REF.
- **Prompt entregue é prompt COMPLETO.** Nunca "adicione X em todos os prompts", nunca colar só a linha
  que mudou. Regra nova no meio da produção obriga **reescrever por inteiro todos os prompts afetados**,
  no arquivo e no chat. Alternativa se entrega como dois prompts completos lado a lado, nunca como
  um prompt mais a instrução de como virar o outro.
- **Referências no título do prompt, em CAIXA ALTA.**
- **Ângulo 3, lei do registro: divino, nunca oculto.** O teste é a LEITURA, não o objeto: prop que lê como
  manifestação entra (cartas, cristais, vela, defumador, tigela com pétalas), prop ou fala que lê como pacto não.
  Sem bruxa, feitiço, spell, shield, círculo de proteção. **Cartas sempre em dourado, branco, rosa claro ou azul claro.**
- **Ângulos 2 e 3 não mostram produto.** Ângulos 1 e 4 mostram sempre (no 4 é um **livro FÍSICO**, nunca mockup de ebook nem tela de celular).
- **[ÂNGULO 4] LIMITE HONESTO É PROIBIDO.** Nenhuma ressalva, nenhum "isso não faz X". A dor prometida
  e o mecanismo do produto são a mesma linha, então toda ressalva encosta na promessa. O take vai pra
  autoridade, prova social, urgência ou escassez. No Ângulo 3 o objeto de desejo do CTA é
  **o rosto da alma gêmea**, nunca o app: ela mandou uma mensagem ao universo, o universo respondeu, e o
  rosto só é revelado se ela clicar no link. Ângulo de entrada é livre, a **ponte pro rosto é obrigatória**.
- **Roteiro final completo é a ÚLTIMA coisa da entrega**, depois de todos os prompts. E o último bloco de todos é sempre o **roteiro final em INGLÊS**, numerado por take mais a versão corrida só-fala. A tabela bilíngue vem antes dele, não no lugar dele.
- **Os gates de maquina rodam sozinhos no `pre-commit`** (`git config core.hooksPath .githooks`,
uma vez por clone). Ele bloqueia commit com drift de memoria ou FALHA de entrega.
- **Entrega não fecha com FALHA no `checar_entrega.py`.** O linter lê do disco e sobrevive ao resumo
  de contexto de sessão longa, que é exatamente quando eu esqueço regra.
- **Nunca sugerir "tenta de novo"** quando o Luigi reporta bloqueio. Ele já tentou várias vezes.
- **Nunca listar termo sensível no `negative`** (nome de órgão, gore, logo/marca). O classificador lê o token, não a negação.

## PORTÕES DE CONSULTA (ler ANTES de agir, nunca depois)

Regra que gera tudo isto: **eu não abro documento sozinho.** Se a leitura não estiver amarrada a um
momento do fluxo, ela não acontece e eu erro. Cada portão abaixo é obrigatório no seu momento.

### P1 · Ao receber o `.mp4`, ANTES de rodar `/watch`
- `biblioteca-videos` → **este esqueleto já foi produzido?** Se já, qual variável usamos e o que não repetir
- `skill-watch` → como rodar o pipeline
- `erros-recorrentes` → os 3 erros históricos de leitura de hook, pra não repetir o quarto

### P2 · Depois da transcrição, ANTES de tocar em uma vírgula da copy
**Este é o portão que mais paga.** Nada de método puzzle antes de reler estes:
- `metodo-puzzle` → esqueleto, variável, herói, teste do estranho
- `feedback-copy-lapida-estrutura` → **rodar o CRIVO DE COPY**
- `referencia-frameworks-copy` → régua germânica, 3 relevâncias, loop aberto, os 4 vazamentos de venda
- `congruencia-matriz` → usuário x coach, e se o claim exige idade vivida
- `estilo-copy-sem-travessao`
- **Do ângulo:** 1 → `produtos-angulos` · 2 → `angulo2-copy-fitywell` · 3 → `angulo3-copy-auraly` + `angulo3-swipe-padroes` · 4 → `angulo4-copy-bodyhacks`
- **Rodar `python checar_frases.py producao/<pacote>`**: compara o roteiro com os anteriores da
  MESMA conta e aponta frase ja queimada. Ignora clone entre avatares e o beat de CTA
- **Se o roteiro tiver fechamento:** `banco-rotas-argumentativas` (**conferir o LOG de rotação**) + `banco-obstaculos` + `feedback-ponte-argumentada`
- **No beat de CTA:** `feedback-cta-produto`

Só depois disso a copy pode ser modificada e mandada pro Luigi aprovar ou ajustar.

### P3 · ANTES de entregar o roteiro pra aprovação
- `ordem-entrega-padrao` → transcrição, cena a cena, só-fala, tabela bilíngue única
- Contagem de palavras take a take, feita **agora** e não depois
- `compliance-riscos` → qual é o claim mais arriscado deste roteiro

### P4 · [ÂNGULO 3] ANTES de sugerir os ganchos visuais
- `producao/_swipe_auraly/BANCO_GANCHOS_VISUAIS.md` → os mecanismos e o formato de plano único
- As três travas do ângulo: **rosto nunca revelado**, **carta na mão depois do gancho**, **registro divino**

### P5 · Ao receber "roteiro aprovado" e `/produzir`, ANTES do primeiro JSON
**Executar a skill não substitui ler.** A skill é a ordem, isto aqui é o conteúdo:
- **O gabarito vivo:** `producao/brandon_angle2/ROTEIRO.md` e `PROMPTS_PRODUCAO.md`
- `workflow-entrega-gabarito` → as 8 coisas que eu perdi ao parar de conferir
- `checklist-composicao-visual` → os 10 itens
- `realismo-anti-cara-de-ia` → os 7 itens do gate de realismo
- `prompts-imagem-json` → campos e blocos padrão
- `erros-recorrentes` → falhas 1 a 7 de geração de imagem
- `avatares-fichas` → traços canônicos e **caminho da âncora**
- `feedback-prompt-imagem-compartilhado` → um keyframe por SETUP, nunca por take
- `feedback-enquadramento-mais-proximo`

### P6 · ANTES de escrever os prompts de VÍDEO (portão que não existia)
- `prompts-video-fase7` → os 5 blocos, e a exceção da regra da fala
- `PLAYBOOK_COMPLETO/11_insights_otimizacao.md` seção 3 → **menos é mais na descrição da ação**, combinação de elementos é o gatilho invisível de moderação, o prop fiel é o ambíguo
- `restricoes-protocolo` → escrever já evitando o que costuma travar

### P7 · [ÂNGULO 3] ANTES de escrever o `DM.md`
- `producao/_dm_auraly/DM_PADRAO.md` → estrutura de 4 beats e rotação
- `banco-obstaculos` → objeções antecipadas
- Travas de preço: nunca "one-time", nunca "pagamento único"

### P8 · Se travar restrição de geração
- `restricoes-protocolo` → **Regra #0: o Luigi já tentou, nunca sugerir retry**
- `PLAYBOOK_COMPLETO/09_troubleshooting_restricoes.md`

### P9 · Fechando a entrega
- **RODAR O LINTER, e só fechar com zero FALHAS:** `python checar_entrega.py producao/<avatar>_<slug>`
  Ele checa do DISCO o que dá pra checar por máquina, então **não depende de eu lembrar de nada**:
  travessão na copy, keyword do ângulo, 13 a 29 palavras por take, fala do prompt igual palavra por
  palavra ao roteiro, JSON válido, bandeira dos EUA, `no captions`, termo sensível no negative,
  seções na ordem, nomenclatura T/K/V/REF, os 5 blocos do prompt de vídeo, instrução de patch,
  produto em quadro nos ângulos 2 e 3, e as travas do ângulo 3. Falso positivo se conserta no linter,
  nunca se ignora.
- **Se a entrega mexeu em memoria, rodar `python checar_memoria.py`**: wikilink quebrado,
  memoria fora do indice, drift do espelho. O `pre-commit` bloqueia, mas rodar antes evita surpresa
- `feedback-prompts-na-conversa` → arquivo E chat, linha curta antes de cada prompt
- `feedback-roteiro-final` → roteiro final em inglês por último
- Gate final da skill `/produzir`, colado preenchido

### P10 · DEPOIS que o vídeo for ao ar (o furo mais caro)
**Ninguém escreve nesses arquivos hoje, então eles envelhecem e eu repito rota sem saber.**
- Escrever no **LOG de rotação** de `banco-rotas-argumentativas`: data, vídeo, ângulo, rota, obstáculo
- Adicionar o vídeo em `biblioteca-videos` com o esqueleto usado
- **Rodar `python checar_rotacao.py`**: lista o que esta em `producao/` e nao foi registrado no log
  nem na biblioteca. Avisa, nunca reprova, porque o casamento e por heuristica
- **Rodar `python grafo_memoria.py` e `python grafo_producao.py`** para o grafo entrar fresco
- Se alguma prática foi revogada no caminho, **editar a memória velha**, nunca só adicionar

## Onde está o resto

Copy e estratégia estão na memória em `~/.claude/projects/.../memory/`:
`banco-rotas-argumentativas` (fechamento) · `banco-obstaculos` · `angulo2-copy-fitywell` · `feedback-ponte-argumentada` · `metodo-puzzle` · `restricoes-protocolo` · `erros-recorrentes` · `avatares-fichas`

### Espelho da memória no repo, e a regra que vem junto

A pasta `memoria/` deste repositório é um **espelho versionado** da memória viva, para backup e
histórico. **A fonte de verdade continua sendo `~/.claude/projects/.../memory/`.** Nunca editar
`memoria/` na mão, nunca ler dela para decidir nada.

**Antes de todo commit que envolva memória, rodar:**
```
powershell -ExecutionPolicy Bypass -File sync_memoria.ps1
```

Existe pelo mesmo motivo do PORTÃO P10: documento que ninguém atualiza envelhece em silêncio, e
espelho desatualizado é pior que espelho nenhum, porque parece confiável.

---

## ÂNGULO 3 (Auraly), o que muda em relação aos Ângulos 1 e 2

**O PROCESSO É O MESMO. Nada aqui substitui o fluxo validado.** `/watch` no modelo, método puzzle,
mesma cabeça de copy, mesma ordem de entrega, mesma estrutura de prompts, mesmas travas de realismo,
mesmos 5 blocos no prompt de vídeo. Só troca o que é **do produto**. Doutrina em `angulo3-copy-auraly`,
banco de copy do nicho em `angulo3-swipe-padroes` (o equivalente ao `angulo2-copy-fitywell`).

**Duração, número de takes e gramática visual saem do VÍDEO MODELO**, como sempre. Não existe formato
fixo do ângulo. Se o modelo tem 66s e um reveal mudo de 8s, o clone tem 66s e o reveal mudo. Se o
modelo tem split screen, o clone tem. Fidelidade de estrutura é a regra de sempre.

**Keyword `222`** no lugar de `yes`.

**Não mostra produto.** O objeto de desejo do CTA é **o rosto da alma gêmea**, nunca o app: ela mandou
uma mensagem ao universo, o universo respondeu, e o rosto chega **na mensagem que o Luigi manda na DM**.
O vídeo nunca diz quiz, teste, app, plano nem preço.

**Ângulo de entrada é livre, a ponte pro rosto é obrigatória.** Com **dois avatares** (Kendra Collins
e Cody Miller), o eixo de variação é **1 esqueleto × N ângulos de entrada × 2 avatares**.
O **Blake Epeterson foi aposentado em 2026-08-25** e substituído pela Cody.

**Registro: divino, nunca oculto.** Ver a lei em `angulo3-copy-auraly`.

**🃏 Depois do take do gancho, a avatar segura a CARTA SOULMATE** (casal ilustrado, palavra SOULMATE na
base, tons claros) e a mantém na mão até o fim. Gerar uma vez como `REF-CARTA` e anexar sempre, igual
o Ângulo 1 faz com o `product.png`.

**🚫 O ROSTO NUNCA É REVELADO NO VÍDEO.** Só na DM, e só depois do `222`. Qualquer gancho que envolva
retrato, foto, polaroid ou desenho tem o rosto **obscurecido**: impressão fora de foco, vidro fosco,
revelação parcial, silhueta, gelo ou névoa. **Descrever sempre como propriedade física do objeto**,
nunca como blur de câmera, senão colide com o `no blur` do negative.

**Âncoras:** Kendra em `producao/_ancoras/KENDRA COLLINS .jpeg`, Cody em
`producao/_ancoras/cody_ancora.jpeg`. Anexar a da avatar escolhida como
referência de identidade e cenário, exatamente como o Ângulo 1 anexa o `product.png`. A regra normal
continua valendo: **`GERAR DO ZERO` no primeiro keyframe de cada setup** (com a âncora anexada),
`EDITAR do K__` em todo o resto.

**📎 SINAL DE ENTRADA: `.mp4` + IMAGEM DE AVATAR na mesma mensagem = produzir PARA AQUELE AVATAR primeiro.**
Quando o Luigi manda o vídeo modelo junto de uma âncora, a âncora **diz para quem é**. Não perguntar,
produzir para ela. O ciclo completo (roteiro, ganchos, prompts, DM) sai para esse avatar antes de qualquer outro.

**Depois de fechar o primeiro, o MESMO vídeo modelo pode rodar no próximo avatar**, com:
- **Ajustes de COPY para congruência com o novo avatar.** ⚠️ **Não é copiar palavra por palavra.**
  Idade, gênero e registro mudam o que soa crível na boca de cada uma. Ver `congruencia-matriz`.
- **Ajustes nos prompts de imagem e de vídeo** (identidade, cenário, registro de voz, rastreio).

**PASSO EXTRA, SÓ NO ÂNGULO 3: sugestões de GANCHO VISUAL antes dos prompts.**
Depois do roteiro aprovado e **antes de entregar qualquer prompt**, mandar sugestões de variações de
gancho visual derivadas do mesmo vídeo modelo. **A copy fica idêntica, só os primeiros segundos mudam.**

*Por que:* neste ângulo a copy é o ativo e o gancho visual é descartável. Ele existe só pra parar o
scroll e fazer ela ouvir. Um roteiro validado vira N vídeos trocando só o hook. E como o Ângulo 3
não precisa segmentar público, gancho de clickbait puro converte, então isso é vantagem e não risco.

Não vale nos Ângulos 1 e 2, onde o herói do hook carrega argumento e não pode ser trocado à toa.

**Entregar de 8 a 10 variações**, ordenadas por congruência, clickbait puro no fim e marcado como tal.
Banco dos 13 mecanismos em `producao/_swipe_auraly/BANCO_GANCHOS_VISUAIS.md`.

**O formato das contas do Ângulo 3 é PLANO ÚNICO, nunca split screen.** Câmera na altura do peito do outro
lado da mesa: a avatar do peito pra cima em cima, a mesa no terço inferior do MESMO quadro, e **ela executa
a ação do gancho com as próprias mãos enquanto fala**. Sem close isolado na mesa, sem B-roll separado.
É a regra 1 do `checklist-composicao-visual`: herói no lower foreground, mais perto que o rosto.
O gancho vive no **T1**. Do T2 em diante ela segura a carta e os takes **se reaproveitam** entre
variações, então cada gancho novo custa **só 1 keyframe + 1 clipe**.

**Terceiro arquivo, `DM.md`:** a mensagem que promete o rosto, a ponte pro link sem citar quiz/app,
os obstáculos antecipados e o follow-up. Mestre em `producao/_dm_auraly/DM_PADRAO.md`.
O `banco-rotas-argumentativas` e o `banco-obstaculos` continuam sendo consultados normalmente, e
atendem o beat de fechamento onde ele existir, no vídeo ou no `DM.md`.

---

## ÂNGULO 4 (Body Hacks For Men), o que muda em relação aos outros

**O PROCESSO É O MESMO.** `/watch` no modelo, método puzzle, mesma ordem de entrega, mesma estrutura
de prompts, mesmas travas de realismo, mesmos 5 blocos no prompt de vídeo, **DOIS arquivos** (não tem
`DM.md` obrigatório como o Ângulo 3). Duração, número de takes e gramática visual saem do vídeo modelo.
Só troca o que é **do produto**. Doutrina completa em `angulo4-copy-bodyhacks`.

**Produto:** `Body Hacks for Men 40+`, marca **FITYWELL** (mesma casa do Ângulo 2), um **PLAYBOOK
DIGITAL** de **42 hacks de HÁBITO** em 7 áreas, 4 linhas e 2 minutos cada. Homens 40+ dos EUA.
Landing: `https://bodyhacksformen.netlify.app/` · checkout **Hotmart embutido na própria página** ·
**$9.90 uma vez**, ancorado em $47 launch price, sem renovação, garantia de 30 dias.

**⚠️ NÃO são receitas ancestrais e NÃO é testosterona.** Foi a descrição inicial, e a landing
desmentiu no mesmo dia. Os hacks são hábito e estratégia. Ler a seção 0 da doutrina antes de escrever
qualquer copy, porque prometer receita e entregar hábito **quebra no clique**, que é o pior lugar.

**Avatar: holistic.brandon, sempre COACH.** Ela **migrou de vez do Ângulo 2 em 2026-08-27**, porque a
audiência da página dela é **97% homens dos EUA**. Nunca usuária, nunca "at our age". A autoridade dela
é **volume observado**: "every man past forty who walks into my gym".

**Keyword `yes`**, decidida pelo Luigi em 2026-08-27.

**MOSTRA produto: livro FÍSICO como prop**, nunca print de tela nem mockup. Gerar uma vez como
**`REF-LIVRO`** e anexar sempre, igual o Ângulo 1 faz com o `product.png`. **O nome nunca vem
sozinho**, sempre colado ao descritor, no mesmo take e no mesmo gesto de levantar o livro.
**Mas a FALA nunca promete objeto físico**, porque o produto é digital com entrega instantânea. De
preferência o CTA diz que ele lê hoje à noite, no celular.

**🚫 LIMITE HONESTO É BANIDO.** Ver a regra na lista acima.

**🚫 NUNCA CULPAR A MASCULINIDADE DELE.** Espelho da regra do Ângulo 2 (lá era o esforço dela).
Zero "você se deixou levar", zero "você parou de se cuidar", zero cobrança pelo que ele era aos 25.
Vergonha é o que trava esse cara. O álibi é **o cano e a mesa, nunca o homem**.
**Crivo antes de entregar:** *"essa copy sugere, em algum ponto, que ele deixou isso acontecer?"*

**🔑 ED É O EIXO PRINCIPAL DE TODO VÍDEO DO ÂNGULO 4** (decisão do Luigi, 2026-08-27, reafirmada
depois da análise da landing). A página sustenta: Men's Vitality é uma das 7 áreas e tem 6 hacks só
dela, então "vários body hacks que resolvem isso" é verdade. **A promessa é ED, o mecanismo é o
mostrador, e o produto é "vários hacks só pra isso mais 40 pro resto".** O mecanismo não esvazia a
promessa, ele explica por que tudo que ele tentou falhou. Base fixa, variando a cada roteiro:
promessa de ED → o mostrador → vários hacks pra isso no livro → comenta `yes` → eu mesmo mando na DM.

**No CTA: `fix`, nunca `treat` nem `cure`** (o rodapé da landing diz que o produto não trata nem cura,
e "the hacks for this" tem a mesma força sem o claim médico). E **cuidado com "eu te mando o livro"**:
a DM entrega link de uma página de $9.90, não o livro de graça, e é o mesmo erro do "it is free" do
Ângulo 2. **Dizer o preço joga a favor**, porque $9.90 com garantia de 30 dias mata a suspeita de
upsell antes dela nascer.

**A PONTE já está escrita dentro do produto, usar ela:** *"drive is a readout, not the problem"*
(hack 39). Ele vinha tentando consertar o mostrador, e é por isso que nada pegou, inclusive o que vem
em frasco. O motor é **sono, carga e cintura**, e são as três que ele controla sem receita.
**Nunca usar a estrutura das 3 causas do Ângulo 2 aqui**, e nunca a ponte de testosterona: a própria
página rejeita o frame hormonal por escrito.

**O ÁLIBI também já está na página:** *"It's not your age. It's your playbook."* Mais a tabela
25 playbook contra 40+ playbook, que é device de copy pronto.

**O vazamento do ângulo, e o que o fecha:** o vídeo entrega um hack de graça e o produto tem 42.
O que fecha é que **um hack conserta uma área e ele não sabe qual é a dele**, e que fazer mais coisa
certa isolada **é o playbook dos 25**, que é justamente o erro que o produto nomeia.

**A PONTE VERBAL com a página é obrigatória.** A landing é contida, nunca diz ED, o termo dela é
**`drive and confidence`**. O vídeo pode ser mais quente, mas **o CTA tem que aterrissar nessa frase**,
senão ele cai numa página que não parece falar do que ele acabou de ouvir.

**Vocabulário, quem pode dizer o quê:** `champion`, `your soldier` e "the part of you that stopped
answering" são liberados na boca dela. **`johnson` NUNCA sai da boca dela**, só em legenda. Nome
clínico de órgão nunca, em lugar nenhum. Um beat de testemunha feminina por roteiro, **na escalada,
nunca no hook**, e ela relata o que as esposas dos clientes dizem, nunca julga o espectador.

**2ª pessoa em cena é homem 45+.** Tratamento no hook: `brother`, `man`, `my guy`.
Nunca `ma'am`, `girl`, `honey`.

## graphify, o grafo de conhecimento da operacao

Existe um grafo em `graphify-out/` cobrindo `memoria/`, `PLAYBOOK_COMPLETO/` e `producao/`:
**1110 nos, 2239 arestas, 96 comunidades**, um unico componente conexo. Ele liga doutrina a
execucao, entao responde coisas que nenhum arquivo sozinho responde: qual rota ja foi usada em
qual video, onde uma regra foi aplicada, se um esqueleto ja rodou.

**Consultar o grafo ANTES de responder qualquer pergunta sobre a operacao.**

- `graphify query "<pergunta>"` devolve o subgrafo relevante, mais barato que abrir os arquivos.
  Se o resultado vier truncado, subir com `--budget 1500`.
- `graphify path "<A>" "<B>" --undirected` mostra como duas coisas se ligam.
  **O `--undirected` e obrigatorio**: sem ele a busca e direcionada e responde "no path"
  mesmo existindo caminho.
- `graphify explain "<conceito>"` abre um no e a vizinhanca dele.
- `graphify-out/GRAPH_REPORT.md` so para visao geral, nunca como primeira parada.

**O grafo NAO substitui os PORTOES DE CONSULTA.** Ele orienta e cruza; os portoes mandam ler o
arquivo inteiro. Quando o portao diz "ler `producao/brandon_angle2/ROTEIRO.md`", e ler o arquivo,
nao perguntar ao grafo sobre ele. Precedencia: **PORTAO > grafo > lembranca**.

**Nos com nome de caminho** (`memoria/banco_obstaculos.md`, `memoria/`) sao o esqueleto documental,
nao conceitos. Servem de indice e garantem que nenhum no fique orfao. Ignorar na leitura de conteudo.

**O grafo envelhece igual a memoria, e pelo mesmo motivo do PORTAO P10.** `graphify update` aqui e
AST-only e ignora markdown, entao **nao adianta** neste projeto. Depois de mexer em `memoria/` ou
fechar uma producao, o grafo fica defasado ate uma reconstrucao semantica, que custa subagentes.
Enquanto isso, tratar resposta do grafo como **datada**, e conferir no arquivo o que for decisivo.
