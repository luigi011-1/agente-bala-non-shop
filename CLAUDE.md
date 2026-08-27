# Operação Vídeos Avatares IA — regras de trabalho

Este arquivo é carregado automaticamente em toda sessão. É a fonte de verdade do PROCESSO.
Copy, ângulos, obstáculos e rotas argumentativas ficam na memória. Aqui fica **como entregar**.

---

## Antes de começar QUALQUER produção

1. Rodar `/watch` no `.mp4`.
2. **Ler `producao/brandon_angle2/ROTEIRO.md` e `PROMPTS_PRODUCAO.md`.** São o gabarito vivo. Nunca reinventar o formato de memória.
3. Perguntar o ângulo (1 Korella / 2 FityWell / 3 Auraly) e confirmar o avatar.
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
- **Keyword por ângulo: `yes` nos Ângulos 1 e 2, `222` no Ângulo 3 (Auraly).** Nunca a palavra do vídeo original.
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
- **Ângulos 2 e 3 não mostram produto.** Ângulo 1 mostra sempre. No Ângulo 3 o objeto de desejo do CTA é
  **o rosto da alma gêmea**, nunca o app: ela mandou uma mensagem ao universo, o universo respondeu, e o
  rosto só é revelado se ela clicar no link. Ângulo de entrada é livre, a **ponte pro rosto é obrigatória**.
- **Roteiro final completo é a ÚLTIMA coisa da entrega**, depois de todos os prompts. E o último bloco de todos é sempre o **roteiro final em INGLÊS**, numerado por take mais a versão corrida só-fala. A tabela bilíngue vem antes dele, não no lugar dele.
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
- **Do ângulo:** 1 → `produtos-angulos` · 2 → `angulo2-copy-fitywell` · 3 → `angulo3-copy-auraly` + `angulo3-swipe-padroes`
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
- `feedback-prompts-na-conversa` → arquivo E chat, linha curta antes de cada prompt
- `feedback-roteiro-final` → roteiro final em inglês por último
- Gate final da skill `/produzir`, colado preenchido

### P10 · DEPOIS que o vídeo for ao ar (o furo mais caro)
**Ninguém escreve nesses arquivos hoje, então eles envelhecem e eu repito rota sem saber.**
- Escrever no **LOG de rotação** de `banco-rotas-argumentativas`: data, vídeo, ângulo, rota, obstáculo
- Adicionar o vídeo em `biblioteca-videos` com o esqueleto usado
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
