# GATE VISUAL · realismo, composição e gancho (TODOS OS ÂNGULOS)

Criado em 2026-09-22 a pedido do Luigi. **Fonte única e transversal** das regras que fazem o vídeo de
IA não parecer IA e que fazem o herói do gancho parar o scroll. Vale para Korella, FitWell e Auraly.
**Sem exceção de ângulo:** Ângulo 1 (Korella), Ângulo 2 (FitWell) e Ângulo 3 (Auraly) rodam as quatro
partes. O que muda entre eles são só as travas de marca já escritas em cada seção.

**Por que existe:** as regras viviam só na memória (`realismo-anti-cara-de-ia` e
`checklist-composicao-visual`) e nenhum workflow vigente apontava para elas. Medido em 2026-09-22:
a maioria dos pacotes recentes ainda aplica, mas por hábito, e os furos já aparecem (6 K de um
pacote Auraly sem o negative de tom quente, 5 K de outro sem luz definida; ambos arquivados em 2026-09-22).
Regra que depende de lembrança se perde. Por isso ela agora é etapa do workflow e aviso do linter.

**Quando rodar:** as Partes 1 a 3, antes do primeiro `K__` de qualquer pacote. A Parte 4 é o método
de variação de gancho dos três ângulos, e **desde 2026-09-23 só roda na RODADA DE VARIAÇÃO**, depois
que o Luigi validar o vídeo no perfil dele (Parte 4, Passo 0). O gate não muda o formato do Flow:
ele define **o que vai dentro** de cada prompt.

Cada regra nova que mudar algo aqui se escreve **aqui**, e as memórias apontam para cá.

**Origem orgânica (2026-09-25):** quando o vídeo modelo é de pessoa real, as Partes 1 a 3 continuam
inteiras (fiel no conteúdo, nunca no acabamento), mas a bandeira dos EUA deixa de ser âncora
obrigatória e o "herói" é o objeto que o original segura no primeiro segundo, ou as mãos perto da
lente numa selfie sem objeto. Sinais de gente real em `PERFIL_ORGANICO.md` seção 6.

---

## PARTE 1 · REALISMO (anti cara de IA)

### 1.1 Cor e luz, o que mais denuncia
- **Nunca tom quente.** Amarelo, laranja e marrom são a assinatura de imagem de IA.
- **Interna:** `neutral overcast daylight from a window`, luz difusa de dia nublado.
- **Externa:** `overcast sky with visible cloud texture` ou `deep blue sky` (hora azul:
  `deep blue sky, soft cool ambient light, no orange sunset`).
- **Céu branco, claro ou estourado SEMPRE denuncia.** O céu tem cor e textura escritas no prompt.
- **Janela estourada também:** escrever `the outside is clearly visible through the window`.
- 🚫 **Golden hour BANIDA** (Luigi, 2026-09-22), em todos os ângulos. Revoga o "externa: golden
  hour" do gate antigo, que contradizia o item de tom quente. Pôr do sol, contraluz alaranjado e
  "fim de tarde" entram na mesma proibição. O linter reprova golden hour pedida no positivo.

### 1.2 Rosto e pele
- **Rosto sem sombra dura**, claro e nítido. Sombra no rosto é reprovação.
- Pele real: `visible pores, irregular skin texture, faint redness, fine lines, minor blemishes,
  soft facial asymmetry`. Cabelo em `uneven natural clumps`, nunca fio a fio perfeito.
- **No K de fala:** `caught mid-sentence, lips naturally parted, animated expression`. O frame
  inicial com a boca entreaberta ajuda o lip sync do Veo.

### 1.3 Foco e acabamento
- **Tudo em foco:** `background fully in focus, no bokeh, no blur anywhere`. Fundo borrado não se
  conserta depois.
- **Estética de celular comum:** `iPhone footage, flat natural light, low contrast, slight JPEG
  compression, boring everyday reality, not professional photography, no AI polish, no beauty
  smoothing, no HDR, no cinematic lighting`.

### 1.4 Partir sempre de algo real (regra-mãe)
> A IA copia bem o que você mostra e inventa mal o que você só descreve.
- **Print do primeiro frame do vídeo modelo** como referência de composição, junto com a âncora.
  Prompt sozinho não reproduz posição e enquadramento.
- Rosto de pessoa secundária: referência de rosto real. Prop que teima: gerar isolado primeiro.
- Âncora é o ativo que mais pesa. Nenhum prompt compensa âncora ruim.
- **Realismo é volume:** regenerar é o método, não sinal de prompt errado.
- Baixar a imagem aprovada em 4K e subir de novo antes de animar.

---

## PARTE 2 · COMPOSIÇÃO DO HERÓI

### 2.1 Herói
1. O herói do gancho fica no **lower foreground, mais perto da lente que o rosto**. Escrever:
   `the [hero] is very close to the lens in the lower foreground, large in frame, closer to the
   camera than her face`.
2. **"Dá pra estar mais perto?"** Se dá, está longe. Sempre mais perto do que parece certo.
3. **Nada compete com o herói.** Se um elemento não serve à fala do take, sai de quadro.
4. Volume do herói explícito: montanha, não camada fina; objeto inteiro, não detalhe.

### 2.2 Fundo
5. **Duas ou três âncoras de fundo descritas, no máximo.** O inimigo é o **inventário no prompt**,
   não a bagunça: cenário vivido que vem da âncora se preserva com `the same lived-in room as the
   reference, unchanged`, sem listar item a item.
6. **Reduzir fundo é com enquadramento, NUNCA com blur.**
7. Cenário **reconhecível** e, quando couber, **americano de bate-pronto** (bandeira discreta e
   visível, cozinha americana, fachada de Walmart ou Costco). Teste: em 2 segundos dá pra saber
   que é EUA?

### 2.3 Pessoas e distância
8. Pessoas do **peito pra cima**; o take mais fechado do vídeo é o do CTA.
9. **2ª pessoa entra cortada pelo quadro**, nunca de corpo inteiro.

### 2.4 Exceções que já existem (não mudam aqui)
- **Ângulo 3:** o kit de tarólogo é obrigatório e entra **agrupado em dois blocos** (prateleira +
  parede), que é como o teto de âncoras convive com ele. Âncora em cena real (Walt, Darlene,
  Lorraine), com a roupa e o cenário-base dela em todo vídeo e gancho (avatar fixo por conta,
  Luigi 2026-09-25; revoga o cenário próprio por gancho). ♻️ **Só no Auraly, desde 2026-10-04:** o anexo
  é o character sheet e **o cenário e o ângulo são os do vídeo modelo, quase 100% fiéis**; este gate
  manda só no acabamento (luz, céu, herói na lente, foco, realismo). Orgânico, nada sobrenatural
  (`WORKFLOW_AURALY.md`). FitWell e Sea Moss não mudam.
- **T1 do Ângulo 3:** cortes internos no `V__`, macro das mãos no payoff e split vertical liberado.
  Do T2 em diante, plano único.
- **Corpo neutro ao gancho:** o prop que muda entre os ganchos fica FORA de quadro no corpo.

---

## PARTE 3 · TRECHOS PRONTOS (para os campos do JSON de imagem do Flow)

Desde 2026-09-25 (contrato do Flow v17) o K entregue é JSON: cada trecho abaixo vai no campo
correspondente (`lighting`, `composition`, `realism`, `negative`), com o mesmo texto.

Colar **dentro** de cada prompt, adaptando só o que está entre colchetes. Os blocos do Flow são
autossuficientes, então isto se repete em todo `K__`, sem exceção.

**Luz interna**
`Neutral overcast daylight from a window, the outside clearly visible through the window, soft even light on the face with no harsh shadows.`

**Luz externa**
`Overcast sky with visible cloud texture, never white or blown out, neutral daylight, soft even light on the face.`

**Herói**
`The [hero] is very close to the lens in the lower foreground, large in frame, closer to the camera than [her/his] face, nothing else competing with it.`

**Realismo (fecha todo prompt)**
`Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday reality, background fully in focus, everything in sharp focus, no blur, no bokeh, no AI polish, no beauty smoothing, no warm orange color cast, no yellow tint, no golden glow, no golden hour light, no sunset, no captions, no subtitles, no words overlaid on the image.`

**Selfie (vale para o `V__`)**
`The hand holding the phone never moves; only the other hand gestures.`

---

## PARTE 4 · GANCHO VISUAL: PUZZLE COM DEGRAU (Luigi, 2026-09-22)

Funde os dois métodos e fica com o mais forte de cada um:

| Vem do **Puzzle** | Vem do **Step up** (curso Lib Korella) |
|---|---|
| a base é o hook do vídeo modelo, que já provou | nunca refazer o viral igual: quem se interessaria já viu |
| a ação estrutural não se toca | subir **um degrau** sobre o que já funcionou |
| **uma variável por variação**, então o resultado se lê | as camadas que mais pagaram: dificuldade diária, contradição, reação |
| 10 variações, 1 keyframe + 1 clipe cada | o vencedor vira a base da rodada seguinte |

**Por que os dois não brigam:** o degrau entra **uma vez, no esqueleto, antes das variações**. Ele
muda a base, não a variação. Cada uma das 10 continua trocando uma única variável, então a leitura
de qual gancho venceu continua limpa. Trocar duas variáveis numa mesma variação segue reprovado.

### Passo 0 · VALIDAR ANTES DE VARIAR (Luigi, 2026-09-23, vale nos três ângulos)

**Toda produção nova a partir de um vídeo modelo começa na RODADA DE VALIDAÇÃO.** As 10 variações
(Passos 1 a 5) só existem na **RODADA DE VARIAÇÃO**, que só abre quando o Luigi disser que um vídeo
já postado performou no perfil dele.

**Why:** o vídeo modelo provou que funciona no perfil de outra pessoa, não no nosso. Variar o gancho
de um vídeo que ainda não foi validado multiplica o custo e mata o teste: se a base não pega com o
nosso público, as cinco versões flopam juntas e não se sabe se o problema foi gancho, roteiro, avatar
ou assunto; se uma vai bem, não existe base validada para comparar. Otimização só faz sentido em cima
de algo que já funcionou aqui.

**Rodada de VALIDAÇÃO (o padrão):**
- **UM gancho por avatar, o do vídeo modelo, com o máximo de fidelidade possível:** mesma ação, mesmo
  herói, mesmo objeto e substância, mesmo tipo de local, mesma ordem de planos, mesmos cortes, mesmo
  timing e mesma abertura (falada ou muda). O texto de tela é o do modelo, traduzido e adaptado.
- 🔴 **Fidelidade é de CONTEÚDO, nunca de acabamento (Luigi, 2026-09-23).** As Partes 1 a 3 deste
  gate rodam INTEIRAS no gancho fiel, igual em qualquer outro `K__`: **herói colado na lente**, mais
  perto do que no modelo quando o modelo estiver aberto; **zero tom amarelado ou quente**, luz neutra
  de dia nublado ou céu com cor, mesmo que o modelo tenha golden hour; duas ou três âncoras de fundo;
  sem blur; trecho de realismo. Fidelidade ao modelo nunca justifica piorar o realismo ou afastar o
  herói (memória `feedback-enquadramento-mais-proximo`: fidelidade é de estrutura, não de câmera).
  Aplicar o gate não conta como desvio a declarar: é o padrão.
- **Só muda o obrigatório:** identidade do avatar, travas do ângulo (keyword, produto em quadro ou
  não, registro divino e rosto nunca revelado no Auraly, congruência na Korella e FitWell), moderação
  e compliance. **Cada desvio forçado é declarado com o motivo**, nunca feito em silêncio.
- **Sem 10 variações, sem degrau, sem controle e sem espera de seleção de gancho.** O gancho fiel vai
  descrito no T1 do roteiro e é aprovado **junto com o roteiro**. Depois da aprovação, direto para os
  prompts.
- ♻️ **Revoga, só nesta rodada, o princípio do step up** *"nunca refazer o viral igual"*: aqui o que
  se testa é se o conteúdo pega no nosso perfil, e para isso o clone tem que ser o mais fiel possível.
- **O resto do workflow não muda:** fila de avatares, aprovação única do roteiro, pacote por avatar,
  bloco do Flow, blocos K/V, transcrições, checklist de envio e linter.
- Arquivo de gancho da rodada: `GANCHOS_VISUAIS.md` com `Rodada: VALIDACAO` no topo e um único
  `HOOK 1 - FIEL` (formato no `OUTPUT CONTRACT` de `WORKFLOW_AURALY.md`, igual nos três ângulos).

**Rodada de VARIAÇÃO (só por ordem do Luigi):**
- Abre quando o Luigi disser que um vídeo postado performou. **Nunca por iniciativa minha**, nunca
  por analogia com outra produção, e o critério de "performou" é dele.
- **A base é o vídeo VALIDADO, como foi postado** (roteiro, gancho e corpo), não mais o vídeo modelo
  de fora. Registrar de onde veio: produção, avatar e o resultado que ele informou
  (`python3 gerenciar_operacao.py registrar`, PORTÃO P10).
- Aí sim roda o Puzzle com degrau dos Passos 1 a 5, com o gancho validado no lugar do hook do modelo.
  O roteiro já está aprovado e validado, então não se reescreve.
- `GANCHOS_VISUAIS.md` com `Rodada: VARIACAO`, `Base validada:` e as 10 de sempre.

### Passo 1 · Ação estrutural e peça viral
Escrever a **ação estrutural** do hook do modelo (Puzzle) e a **peça viral**: o que fez aquele vídeo
estourar (o primeiro clipe, o herói, o fundo, o layout ou o roteiro). **As duas são intocáveis.**

### Passo 2 · Um degrau no esqueleto
Acrescentar **UMA** camada que o modelo não tem, escolhida desta escada:

| Degrau | O que acrescenta | Caso medido no curso |
|---|---|---|
| `DIFICULDADE` | o problema num momento concreto do dia | "barriga" → "não consegue entrar no carro": 2k → 180k |
| `CONTRADICAO` | um estado impossível, visível no quadro | "78 anos" → "78 anos **andando** como 30": 6k → 150k |
| `REACAO` | segunda pessoa reagindo, validando ou chocada, cortada pelo quadro | mulheres atrás + homem reagindo à idade |
| `EUA` | cenário americano icônico carregando o take | fora do Costco ou do Walmart |
| `ESCALA` | exagero de volume, quantidade ou tamanho do herói | montanha no lugar de camada fina |

Travas do degrau:
- **Um só por produção.** É ele que a rodada está testando.
- **Não toca a peça viral** e **nunca obriga a reescrever a fala**.
- **Cabe em 1 keyframe + 1 clipe.** Se precisa de clipe extra, é degrau demais.
- **Korella e FitWell:** continua congruente com a fala do T1, e clickbait segue proibido. Na
  Korella o frasco nunca é a variável trocada nem o degrau: o produto fica fixo onde o roteiro pede.
- **Auraly:** o degrau aumenta o **constrangimento**, nunca a admiração, e o rosto da alma gêmea
  continua nunca revelado. `REACAO` aqui é alguém flagrando o ritual, não aplaudindo.

Declarar no topo: `Degrau: CATEGORIA - o que foi acrescentado`.

### Passo 3 · As 10 variações
- **HOOK 1 = CONTROLE:** o esqueleto **original, sem o degrau**, com uma variável trocada. É o que
  mostra se o degrau pagou. Recomendado escolher o controle em pelo menos um avatar.
- **HOOK 2 a 10:** o esqueleto **com o degrau**, uma variável trocada em cada um.
- No Auraly, clickbait puro continua liberado, no fim e marcado.
- **A camada verbal das 10** (fala do T1, texto de tela) segue a skill **`gancho-verbal`**, modo
  PRODUCAO (2026-09-22): no topo, tese, sintoma-alvo, direcao, padrao do modelo e banco verbal com 5
  frases literais do roteiro; em cada variacao, texto de tela de no maximo 9 palavras com uma frase
  do banco; no fim, `Recomendacao: HOOK X`. A frase muda so porque a variavel visual mudou: trocar a
  estrutura da frase junto seria segunda variavel.

### Passo 4 · Checklist de cada variação
1. **Coerência visual e verbal, sem redundância:** o que a fala ou o texto de tela diz aparece na
   imagem, mas o texto não narra o que a imagem já mostra. Mesmo assunto, informação diferente: se
   a imagem mostra o problema, o texto carrega o resultado, ou o contrário (skill `gancho-verbal`).
2. **Um único ponto focal, colado na lente** (Parte 2). Em 1 segundo o olho sabe onde olhar.
3. **Ação já começada** no primeiro frame. Mostrar, segurar ou apontar para o objeto reprova.
4. **Emoção crua** no rosto (raiva, espanto, vergonha), nunca a expressão neutra de banco de imagem.
5. **Sinal de EUA** no quadro quando couber (Parte 2, item 7).

### Passo 5 · Rotação
Quando uma variação vence, **ela vira a base** da próxima produção do mesmo esqueleto, que sobe
**mais um degrau, de outra categoria**, em cima dela. Nunca repetir o mesmo degrau sobre a mesma
base e nunca refazer o vencedor igual. Registrar em `biblioteca-videos`: esqueleto, degrau e
vencedor, para a próxima rodada saber de onde partir.

---

## PARTE 5 · CHECKLIST DE ENVIO (BLOQUEANTE, Luigi, 2026-09-22)

Depois das Partes 1 a 4 e **antes de enviar qualquer coisa** ao Luigi (lista de ganchos, `K__`,
`V__`, pacote ou prompt avulso), rodar o **checklist de envio** da memória `checklist-envio-prompt`:
os insights do curso Lib Korella em cinco blocos (A gancho, B imagem, C vídeo, D montagem, E marca),
válidos em todos os ângulos, presentes e futuros.

- **Item reprovado = o prompt não sai.** Corrige e roda o checklist de novo. Nunca enviar com ressalva.
- Item que não se aplica vira `N/A`, nunca aprovado por omissão.
- A entrega leva, **fora** dos blocos copiáveis: `Checklist de envio: X/X aprovados (N/A: ...)`.

---

## PARTE 6 · FICHA DO FRAME E PLACAR DE CADA K (BLOQUEANTE, Luigi, 2026-09-25)

**Por que existe:** em `fitywell_growth_modelo_intestino` o K01 passou no linter com 0 falha e gerou
outro gancho. O prompt tinha as palavras certas ("very close to the lens"), mas a forma do herói
estava genericizada por medo de censura, a câmera estava no peito e havia props inventados. As regras
das Partes 1 e 2 existiam; faltava obrigar a MEDIR o frame do modelo e provar, frase por frase, que o
K usa a medida. Vale nos três ângulos, em todo `K__` e `REF-P` de produção nova.

### 6.1 A ficha vem antes do K
Na pasta da produção, `FICHA_FRAMES.md`, uma seção `## Kxx` por keyframe, escrita **olhando o frame
do modelo daquele take** (`input/frames_modelo/Kxx_modelo.png`), nunca de memória:

```
## K01
Frame: `input/frames_modelo/K01_modelo.png`
Take: T1
Herói: o que é, como se vê
Termos de forma: "termo 1" · "termo 2"          (termos que o K TEM que usar, literais)
Quadro: quanto do quadro o herói ocupa e onde  (porcentagem, bordas)
Distância da lente: medida (centímetros, maior que a cabeça)
Câmera: altura, lente (0,5x / 1x), ângulo
Pose: onde o avatar está em relação ao herói, o que cada mão faz
Lista fechada: tudo o que está em quadro, e nada mais
Frame 0: o instante exato do primeiro frame
Desvio (acabamento ou avatar fixo): o que muda e por qual regra
Cenário do modelo: (SÓ AURALY, 2026-10-04) o ambiente atrás no frame, que o scene copia quase 100%
```

### 6.2 Desempate entre o modelo e o gate
- **O frame do modelo manda no CONTEÚDO:** forma, cor e textura do herói, quanto do quadro ele ocupa,
  distância, câmera, pose, o que está em quadro e o frame 0.
- **O gate manda no ACABAMENTO:** luz neutra, céu ou janela com cor, foco total, pele real, sem texto,
  negative, bandeira (formato IA), roupa e cenário da âncora (avatar fixo; no Auraly, desde 2026-10-04,
  roupa do character sheet e cenário e ângulo do vídeo modelo, que aí são CONTEÚDO e mandam).
- **Proximidade do herói tem piso:** a distância final é a MAIS PERTO entre o modelo e o gate. Nunca
  mais longe que no modelo, e sempre mais perto que o rosto (Parte 2).
- **Vocabulário seguro é só do negative.** No positivo a forma do herói vai descrita inteira, como se
  vê no frame (Falha #6 e #8 de `erros-recorrentes`). Genericizar o herói troca o gancho.
- **O texto nunca contradiz o frame anexado.** O anexo só ajuda; quando o texto diz outra coisa, o
  modelo de imagem segue o texto.

### 6.3 O placar de cada K, com evidência citada
Logo abaixo de cada seção, uma tabela `| Item | Status | Evidência |`. Status `OK` exige o trecho
**literal** do K entre aspas; `N/A` exige o motivo.

| Item | Critério | N/A permitido? |
|---|---|---|
| F1 forma do herói | os termos de forma da ficha no prop | não |
| F2 quanto do quadro | porcentagem, metade, dois terços, edge to edge | não |
| F3 distância da lente | inches, centimeters, touching the lens | não |
| F4 câmera | lente e altura | não |
| F5 pose do avatar | posição relativa ao herói | sim, com motivo (ex.: só mãos) |
| F6 lista fechada | frase que fecha o quadro ("the counter is empty", "no bottle in frame") | sim, com motivo |
| G1 luz neutra | trecho da luz do gate | não |
| G2 céu ou janela | "never white or blown out" ou equivalente | sim, com motivo |
| G3 foco | "everything in sharp focus" | não |
| G4 realismo | trecho de realismo | não |
| G5 sem tom quente | "no warm orange color cast" | não |
| G6 sem texto | "no captions" | não |
| G7 bandeira | trecho da bandeira (opcional na origem orgânica, com motivo) | sim, com motivo |
| G8 boca no K de fala | "caught mid-sentence" | sim, sem rosto ou sem fala |

A evidência é escrita sem nome de avatar, para valer em todos os pacotes da fila.

### 6.4 O que a máquina cobra e o que só o olho cobra
- **`checar_entrega.py` (via `ficha_frame.py`) reprova** quando: falta a ficha ou a seção de um K; o
  frame citado não existe; um termo de forma ou uma evidência não está literalmente no K de algum
  avatar; o placar tem item faltando, reprovado ou N/A proibido; a composição do K não tem medida de
  quadro; falta a distância até a lente; a câmera não diz lente e altura. Produções anteriores a esta
  regra ficam em `controle/ficha_legado.json` e nunca entram produções novas nessa lista.
- **Só o olho cobra:** se a ficha descreve o frame corretamente (por isso ela cita o arquivo do frame,
  para o Luigi abrir lado a lado) e se a imagem gerada saiu igual. **No K do gancho, quando o Luigi
  mandar o resultado, pontuar o resultado com o mesmo placar F1 a F6 contra o frame antes de seguir.**
- A entrega leva, fora dos blocos: `Ficha: N/N K, placar 14/14 cada` junto da linha do checklist.
