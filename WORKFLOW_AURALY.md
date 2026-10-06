# WORKFLOW AURALY

Fonte canonica unica para a operacao do Angle 3 / Auraly. Consolida somente processo, estado e
formato de saida. A inteligencia criativa permanece nas fontes especializadas.

## Bootstrap

```text
AGENTS.md
-> WORKFLOW_AURALY.md
-> producao/<producao_ativa>/CHECKPOINT.md
-> Current stage
-> Next action
```

Durante uma producao ativa, usar o checkpoint mais o artefato necessario para a etapa atual. Nao
refazer etapa concluida e nao reabrir decisao aprovada.

## Fluxo oficial

```text
INPUT
-> registrar video + AVATAR QUEUE
-> confirmar Angle 3 / Auraly
-> ANALYSIS
-> METHOD_PUZZLE
-> SCRIPT_MODELLING, com o HOOK FIEL do modelo descrito junto
-> WAITING_SCRIPT_APPROVAL (aprova roteiro + hook fiel de uma vez)
-> [so na RODADA DE VARIACAO] HOOK_IDEATION, exatamente 10 hooks
-> [so na RODADA DE VARIACAO] WAITING_HOOK_SELECTION
-> bloquear hooks para toda a fila
-> IMAGE_PROMPTS + VIDEO_PROMPTS do avatar ativo, na mesma resposta em blocos separados
-> avatar DONE
-> proximo avatar ACTIVE
-> repetir pacote K + V adaptando apenas identidade visual
-> todos os avatares DONE
-> PRODUCTION_COMPLETE
-> quando o Luigi confirmar a postagem: `python3 gerenciar_operacao.py registrar` (controle/README.md)
```

### Validar antes de variar (Luigi, 2026-09-23)

Toda producao nova a partir de video modelo e `Round: VALIDATION`: **um gancho so, o do video
modelo, clonado com o maximo de fidelidade**, igual para toda a fila. Sem 10 hooks, sem degrau, sem
`HOOK_IDEATION` e sem `WAITING_HOOK_SELECTION`: depois de `WAITING_SCRIPT_APPROVAL` o proximo estado
e `IMAGE_PROMPTS`. So muda o obrigatorio (identidade, travas do angulo, moderacao), e cada
desvio forcado vai declarado no hook fiel. **Fiel no conteudo, nunca no acabamento:** o
`GATE_VISUAL.md` Partes 1 a 3 roda inteiro no gancho fiel (heroi colado na lente, zero tom quente,
luz neutra ou ceu nublado, 2 a 3 ancoras, sem blur), mesmo que o modelo seja aberto ou amarelado.

`Round: VARIATION` so existe quando o Luigi disser que um video postado performou. E uma producao
nova, com `Validated from:` apontando producao, avatar e resultado informado; a base e o video
validado como foi postado, o roteiro nao se reescreve, e ai roda `HOOK_IDEATION` com as 10 do Puzzle
com degrau. Metodo completo em `GATE_VISUAL.md` Parte 4, Passo 0. Nunca abrir rodada de variacao
por iniciativa propria.

Nesta rodada o T1 segue a gramatica do **modelo**: se o modelo abre mudo com cortes, clonar mudo com
os cortes dentro do `V__` (secao abaixo, item 7); se o modelo abre falando, o T1 fala.

## Regra de estado

Toda pasta de producao Auraly deve conter `CHECKPOINT.md`. Atualizar imediatamente depois de cada
aprovacao, selecao, entrega de pacote ou mudanca de avatar. Registrar somente fatos, decisoes e uma
unica proxima acao concreta.

Estados canonicos: `INTAKE`, `WAITING_ANGLE`, `ANALYSIS`, `METHOD_PUZZLE`, `SCRIPT_MODELLING`,
`WAITING_SCRIPT_APPROVAL`, `HOOK_IDEATION`, `WAITING_HOOK_SELECTION`, `IMAGE_PROMPTS`,
`WAITING_IMAGE_SELECTION`, `VIDEO_PROMPTS`, `AVATAR_TRANSITION` e `PRODUCTION_COMPLETE`.

Estados `WAITING_*` sempre significam parar e aguardar o usuario.

⚠️ **Regra declarada por Luigi em 2026-09-17:** no caminho padrão novo, `WAITING_IMAGE_SELECTION`
não interrompe a autoria. Os prompts de vídeo (`V__`) saem na MESMA mensagem que os prompts de
imagem (`K__`) do avatar ativo, sem esperar seleção ou aprovação de imagem. Depois de entregar os
dois blocos, marcar o pacote do avatar como DONE e avançar para `AVATAR_TRANSITION` ou
`PRODUCTION_COMPLETE`. As demais esperas (`WAITING_SCRIPT_APPROVAL`, `WAITING_HOOK_SELECTION`)
continuam pausando normalmente. `WAITING_IMAGE_SELECTION` permanece apenas para retomadas
históricas ou quando o usuário pedir explicitamente revisão de imagem antes de receber V.

Isto antecipa somente a **entrega textual** dos `V__`. A execução continua sequencial: o executor
gera quatro candidatas por `K__`, aguarda a seleção manual de uma imagem por código e somente então
executa o `V__` correspondente usando a escolhida como INITIAL FRAME. Entregar K e V juntos nunca
autoriza o executor a pular a seleção de imagem.

### Objetivo, identidade e fonte de estado

Registrar `Objective: SALE` ou `Objective: GROWTH` no checkpoint. A oferta permanece Auraly nos
dois casos. SALE usa o destino Stories; GROWTH, quando explicitamente aprovado para a producao,
usa save, 222 e follow, sem exigir Stories ou DM. Nao inferir GROWTH porque o video modelo era
de crescimento. Uma decisao de GROWTH vale so para a producao cujo checkpoint a registra.

Registrar tambem `Source: ORGANIC` quando o video modelo for de **pessoa real** (Luigi, 2026-09-25).
Nesse caso `PERFIL_ORGANICO.md` governa a copy e o visual: copia literal do gancho visual, da copy e
da estrutura, **so o CTA muda** (SALE: engajamento do original com `222` e a consequencia, depois
`tap my profile picture`, a resposta esta no Stories). Kit de tarologo, carta SOULMATE, T1 mudo com
cortes internos, plano unico com mesa e bandeira em todo K **nao se aplicam**; `spell` e afins viram
`prayer`, `ritual` ou `blessing`. O `ROTEIRO.md` leva `origem: organico` e `CTA original:` no topo.
Sem `Source:`, vale o formato de avatar IA.

O CHECKPOINT e a fonte autoritativa de estado. `AVATAR_QUEUE.md`, quando existir, e uma vista
derivada: preservar nomes e caminhos das anchors e atualizar os estados pelo checkpoint. Nao
inferir aprovacao, geracao de midia ou publicacao pela existencia de um arquivo. Pastas historicas
sem checkpoint continuam historicas; nao fabricar aprovacoes para migra-las.

Cada avatar deve ter um identificador estavel e o caminho exato da anchor. Nunca casar nomes e
imagens apenas pela ordem dos anexos. Conferir a identidade antes de aprovar o roteiro para a fila.

`PRODUCTION_COMPLETE` significa pacote de prompts entregue para toda a fila. Midia gerada,
montagem, publicacao e resultados sao marcos separados, registrados em `controle/` quando houver
evidencia. Eles nao reabrem o roteiro nem alteram o significado deste estado.

O contrato do executor e subordinado a este arquivo. O perfil Auraly em
`producao/_flow/INSTRUCOES_AGENTE_FLOW.md` deve reproduzir as travas permanentes abaixo. Perfis
classicos e pacotes historicos nao alteram o contrato Auraly. Entregar instrucoes do executor
separadamente quando necessario; nunca anexar texto auxiliar aos blocos K/V nem eliminar as
esperas de aprovacao deste workflow.

### Verificacao da entrega

Executar `python3 checar_entrega.py producao/<slug> --estrito` nas novas producoes. O modo
estrito exige checkpoint. Sem essa opcao, pastas historicas sem checkpoint recebem aviso de
cobertura, sem serem migradas automaticamente. Falta de arquivo esperado, codigos duplicados e
fala divergente devem aparecer como problemas, nunca como verificacao bem-sucedida.

O validador aceita blocos limpos K/V em arquivos de avatar na raiz ou em subpastas. Informacoes
de revisao ficam fora dos blocos. Validacao mecanica nao comprova realismo, qualidade criativa,
renderizacao, publicacao nem resultado comercial.

## Consulta minima por etapa

### ANALYSIS e METHOD_PUZZLE

Abrir somente o video, a transcricao, `02_metodo_puzzle.md`, `memoria/metodo_puzzle.md`,
`memoria/feedback_copy_lapida_estrutura.md`, `memoria/referencia_frameworks_copy.md` e
`memoria/congruencia_matriz.md`.

Preservar micro-beats, ordem, transicoes, progressao psicologica, intensidade, open loops, timing da
promessa, mecanismo, prova, urgencia, CTA, duracao e ritmo. Nunca condensar sem pedido explicito.

### SCRIPT_MODELLING

Abrir a analise/transcricao e somente `PLAYBOOK_MESTRE_AURALY.md` nas secoes criativas vigentes,
`memoria/angulo3_copy_auraly.md`, `memoria/angulo3_swipe_padroes.md` e
`memoria/feedback_copy_lapida_estrutura.md`. Regra: `COPY THE ENGINEERING, NOT THE WORDS`.

### HOOK FIEL (rodada de validacao, dentro de SCRIPT_MODELLING)

Abrir o hook do video modelo, `GATE_VISUAL.md` Parte 4 Passo 0, a skill **`gancho-verbal`** (so o
topo e os testes, sobre o unico hook) e o banco `producao/_swipe_auraly/BANCO_GANCHOS_VISUAIS.md`
apenas para saber se aquele hook ja foi publicado por nos. Escrever `GANCHOS_VISUAIS.md` no formato
`HOOK FIEL` do OUTPUT CONTRACT e entregar junto com o roteiro.

### HOOK_IDEATION (so na rodada de variacao)

Abrir o **hook do VIDEO VALIDADO** (na rodada de variacao ele ocupa o lugar do hook do video
modelo em tudo o que segue), o roteiro aprovado, `producao/_swipe_auraly/BANCO_GANCHOS_VISUAIS.md`,
as secoes de hook de `memoria/angulo3_swipe_padroes.md` e a **Parte 4 de `GATE_VISUAL.md`**
(**Puzzle com degrau**, o metodo de variacao desde 2026-09-22, com o checklist de gancho visual)
e a skill **`gancho-verbal`** no modo PRODUCAO (2026-09-22), que cuida do texto de tela: aqui o T1
e mudo, entao o gancho verbal vive so na tela e tem que repetir uma frase que a voz diz no T2 em diante.

♻️ **REESCRITO EM 2026-09-20 (Luigi): aqui e METODO PUZZLE, igual ao Angulo 2.** Revoga o portfolio
`4 + 3 + 3` em tres familias. **O esqueleto sai do hook do video modelo, fica intacto, e cada uma
das 10 sugestoes troca UMA variavel.** O banco NAO e a fonte da ideia: serve para controle de
repeticao (nao repetir literalmente objeto, texto de tela ou execucao ja publicados), padrao de
qualidade e universo visual. Gabarito de formato: `producao/fitywell_pernas/GANCHOS_VISUAIS.md`.

♻️ **2026-09-22 (Luigi): PUZZLE COM DEGRAU.** Antes das 10, declarar a **peca viral** (intocavel) e
subir **UM degrau** no esqueleto (`DIFICULDADE`, `CONTRADICAO`, `REACAO`, `EUA` ou `ESCALA`). No
Auraly o degrau aumenta o constrangimento, nunca a admiracao. **HOOK 1 = CONTROLE** sem o degrau;
HOOK 2 a 10 com o degrau, uma variavel cada. Metodo completo em `GATE_VISUAL.md` Parte 4.

#### Protocolo de decisao antes de escrever os hooks (Auraly somente)

Registrar no artefato de hooks, de forma objetiva e auditavel:

1. qual e a promessa central e a primeira linha do roteiro aprovado;
2. qual e a **ACAO ESTRUTURAL do hook do video modelo**, escrita com os substantivos
   genericos que marcam onde entram as variaveis;
   - qual e a **PECA VIRAL** (o que fez o modelo estourar, intocavel) e qual **DEGRAU** sobe o
     esqueleto (`GATE_VISUAL.md` Parte 4), com o HOOK 1 reservado ao controle sem degrau;
3. quais sao os **eixos de troca** disponiveis neste esqueleto, entre `OBJETO`, `SUBSTANCIA`,
   `LOCAL`, `COR`, `RESULTADO`, `MARCADOR` e `ALVO`;
4. qual unica variavel muda em cada uma das 10 sugestoes;
5. qual variacao e clickbait puro, que aqui e liberado, vai no fim e vai marcada;
6. qual anomalia domina o primeiro segundo: fisica, contextual, transformacional ou semantica;
7. como os cortes internos do clipe servem a acao estrutural preservada;
8. qual texto de tela cria desejo/perigo e qual marcador cria selecao pessoal;
9. como o significado fica adiado sem quebrar a congruencia com Auraly/alma gemea;
10. quais conceitos passam pelos criterios de impacto, leitura imediata, densidade semantica,
    selecao pessoal, significado adiado, repetibilidade, congruencia e viabilidade.

Esse protocolo registra decisoes operacionais, nao raciocinio livre. Rejeitar qualquer conceito que
mude duas ou mais variaveis centrais de uma vez, que abandone a acao estrutural do modelo, que
revele a explicacao inteira no primeiro segundo ou que dependa de texto generico sem uma anomalia
visual legivel.

Regra consolidada: `ANOMALIA IMEDIATA + DESEJO/PERIGO ESCRITO + SELECAO PESSOAL + SIGNIFICADO
ADIADO + REPETICAO MODULAR`. `IMPACT FIRST / CURIOSITY SECOND / CONGRUENCE ALWAYS` continua valido.

O texto de tela pertence ao plano de edicao. Ele deve ser especificado no hook, mas nao deve ser
impresso dentro do `K__` nem solicitado como legenda no `V__`.

### IMAGE_PROMPTS

Abrir somente checkpoint, hooks selecionados, roteiro aprovado, o **character sheet** do avatar ativo,
os frames do vídeo modelo (cenário e ângulo fiéis, 2026-10-04) e **`GATE_VISUAL.md`**
(Partes 1 a 3: realismo, composicao do heroi e trechos prontos), que sao as regras vigentes de
prompt de imagem. Rodar o gate antes do primeiro `K__`: todo `K__` carrega luz neutra ou ceu com
cor, heroi colado na lente e o trecho de realismo, porque o bloco do Flow e autossuficiente.
Manter hooks e copy bloqueados. Entregar somente `K__`.

**Bloqueante (2026-09-22):** antes de enviar K e V, rodar o **checklist de envio** (`GATE_VISUAL.md`
Parte 5, memoria `checklist-envio-prompt`). Item reprovado impede o envio. A resposta leva
`Checklist de envio: X/X aprovados` fora dos blocos copiaveis.

### VIDEO_PROMPTS

Abrir somente checkpoint, pacote textual `K__` do avatar e roteiro/takes aprovados. Escrever os
`V__` na mesma resposta do pacote K, antes da geracao das imagens. Cada `V__` usa exatamente o
`K__` declarado no `MAPA K/V`; varios V podem reutilizar o mesmo frame de body, mas nenhum
mapeamento pode ser inferido silenciosamente. A execucao do V continua bloqueada ate a candidata K
correspondente ser aprovada no Flow.

### Proximo avatar

Abrir somente checkpoint, nova anchor e pacote aprovado anterior. Adaptar apenas identidade, anchor,
roupa, ambiente e caracteristicas visuais. Manter copy, hooks, falas, ordem, takes e funcao visual.

## OUTPUT CONTRACT

### Roteiro

```text
01 - ORIGINAL STRUCTURE
[estrutura objetiva]

02 - MODELLED SCRIPT - ENGLISH
[roteiro em ingles]

03 - PORTUGUES
[traducao integral]

04 - HOOK FIEL DO MODELO
[o bloco HOOK FIEL abaixo; so na rodada de validacao]

05 - WAITING FOR APPROVAL
```

Definir `Current stage: WAITING_SCRIPT_APPROVAL` e parar. Aprovado o roteiro na rodada de
validacao, o hook fiel esta aprovado junto e o proximo estado e `IMAGE_PROMPTS`.

### Hook fiel (rodada de validacao)

```text
HOOK FIEL - RODADA DE VALIDACAO

Rodada: VALIDACAO

Tese:
[primeira frase do roteiro aprovado lida como tese]

Sintoma-alvo:
[a situacao concreta que o roteiro resolve]

Direcao:
[quem vence / quem fica para tras]

Padrao do modelo:
[A · PROVA | B · DOR DIRETA]

Banco verbal:
- "[frase literal do roteiro 1]"
- "[... ate no minimo 5]"

Acao estrutural:
[a acao do hook do video modelo, como ele e]

Peca viral:
[o que fez o modelo viralizar]

HOOK 1 - FIEL - nome
Cena:
[o hook do modelo, plano a plano: acao, heroi, objeto, local, ordem de planos, cortes, timing,
 abertura muda ou falada. O acabamento segue GATE_VISUAL.md Partes 1 a 3: heroi colado na
 lente, luz neutra sem tom quente, 2 a 3 ancoras de fundo, sem blur]
Screen text:
[o texto de tela do modelo, traduzido e adaptado]
Desvios obrigatorios:
[cada mudanca em relacao ao modelo + o motivo (identidade, trava do angulo, moderacao,
 realismo). "nenhum" quando nao houver]
Delayed meaning:
[o que fica em aberto, como no modelo]
```

### Hooks (rodada de variacao)

```text
PUZZLE AURALY - 10 VARIACOES DO HOOK VALIDADO

Rodada: VARIACAO

Base validada:
[producao, avatar e resultado informado pelo Luigi]

Tese:
[a primeira frase do roteiro aprovado lida como tese, em uma linha]

Sintoma-alvo:
[a situacao concreta e contavel que o roteiro resolve, nunca emocional]

Direcao:
[ela faz o gesto e o universo responde / a perda e da inacao, nunca do valor dela]

Padrao do modelo:
[A · PROVA | B · DOR DIRETA, preservado nas dez]

Banco verbal:
- "[frase literal do roteiro aprovado 1]"
- "[... ate no minimo 5]"

Acao estrutural:
[a acao do hook do video modelo, preservada nas dez, com substantivos genericos
 marcando onde entram as variaveis]

Peca viral:
[o que fez o modelo viralizar: primeiro clipe, heroi, fundo, layout ou roteiro. Intocavel]

Degrau:
[DIFICULDADE | CONTRADICAO | REACAO | EUA | ESCALA] - [a unica camada acrescentada ao
 esqueleto, que vale do HOOK 2 ao HOOK 10]

Eixos de troca:
[quais dos eixos OBJETO / SUBSTANCIA / LOCAL / COR / RESULTADO / MARCADOR / ALVO
 este esqueleto aceita]

Shot sequence (vai DENTRO do V do gancho, mesmo clipe, e e a MESMA nas dez,
porque pertence a acao estrutural preservada):
[acao ja comecada > corte para MACRO das maos no payoff > corte de volta ao
 plano de corpo. O take e MUDO]

Custo:
1 keyframe + 1 clipe por variacao. Os takes do corpo sao os mesmos em todas.

HOOK 1 - CONTROLE - nome
[esqueleto original SEM o degrau, uma variavel trocada]
Changed variable:
[OBJECT | MATERIAL | COLOR | LOCATION | ANGLE | RESULT | MARKER] - [uma unica mudanca]
Dominant anomaly:
[fisica, contextual, transformacional ou semantica]
Cena:
[descricao]
Screen text:
[linha de desejo concreto no padrao "When you need [desejo urgente]:" + linha de prazo/segredo.
 Cada linha com no maximo 9 palavras, e pelo menos uma frase do banco verbal]
Delayed meaning:
[o que fica em aberto]
Por que para o scroll:
[motivo]

HOOK 2 ... HOOK 10
[mesma estrutura, sempre a MESMA acao estrutural COM o degrau, uma unica variavel
 trocada em cada um. Clickbait puro, se houver, vai no fim e vai marcado]

Recomendacao: HOOK X
[1 ou 2 frases: por que este, e qual frase do banco verbal ele puxa. A escolha e do Luigi]

WAITING FOR HOOK SELECTION
```

Definir `Current stage: WAITING_HOOK_SELECTION` e parar.

### Prompts de imagem

Entregar um bloco copiavel de imagem e, imediatamente depois dele, um bloco copiavel separado de
video para o mesmo avatar. Antes dos dois blocos, entregar um mapa tecnico separado que declare o
INITIAL FRAME de cada V. Um mesmo K pode alimentar varios V do mesmo setup:

```text
MAPA K/V
V01: K01
V02: K02
V03: K02
V04: K03
```

O mapa nao entra no campo de prompt do Flow. Dentro do bloco de imagem, somente `K__`:

```text
K01
{ ...objeto JSON completo e autossuficiente... }

K02
{ ...objeto JSON completo e autossuficiente... }
```

Desde 2026-09-25 (Luigi, contrato do Flow v17) cada K do bloco e UM objeto JSON em ingles, de `{` a
`}`, com os mesmos campos do JSON interno menos `shot_id`. As regras de conteudo nao mudam.

**Antes do primeiro K (Luigi, 2026-09-25): `FICHA_FRAMES.md` com a ficha do frame e o placar de cada K**
(`GATE_VISUAL.md` Parte 6). O K se escreve a partir da ficha, e o `checar_entrega.py` reprova o pacote
sem ela, com evidencia que nao esta no K, heroi sem medida ou camera sem lente e altura.

Sem descricao, titulo, `T__`, metadata ou `Prompt:` dentro do bloco. Depois do bloco K, entregar o
bloco V previsto abaixo na mesma resposta. A seleção manual continua sendo gate do executor Flow,
mas não deixa o checkpoint do Codex parado: após os dois blocos, atualizar para `AVATAR_TRANSITION`
ou `PRODUCTION_COMPLETE`, conforme a fila.

### Prompts de video

Na mesma resposta do pacote de imagem, entregar um segundo bloco copiavel contendo somente `V__`:

```text
V01
[prompt completo e autossuficiente]

V02
[prompt completo e autossuficiente]
```

Sem descricao, titulo, `T__`, `usa K__`, metadata ou configuracao do Flow dentro do bloco. Nao
reabrir roteiro ou hooks. O executor armazena o bloco V, mas so o executa depois de uma candidata
K aprovada para cada codigo indicado no mapa.

## Comandos textuais

### STATUS

Responder somente:

```yaml
Production:
Stage:
Active avatar:
Queue:
Last completed:
Next action:
```

### CONTINUE

Ler o checkpoint e executar somente `Next action`. Nao fazer nova auditoria.

### CHECKPOINT

Atualizar `CHECKPOINT.md` com o estado factual e mostrar somente um resumo curto.

### RESUME PRODUCTION

Ler `AGENTS.md`, este arquivo e o checkpoint da producao ativa; mostrar status em poucas linhas e
executar exatamente `Next action`. Nao refazer decisoes.

## Contrato do CHECKPOINT.md

```yaml
# PRODUCTION CHECKPOINT

Production:
Angle:
Objective: SALE ou GROWTH
Source: ORGANIC (so quando o video modelo e de pessoa real; PERFIL_ORGANICO.md)
Round: VALIDATION ou VARIATION
Validated from: (so em VARIATION: producao, avatar, resultado)
Reference video:

Current stage:
Current avatar:
Next action:

## Avatar queue
[DONE] ...
[ACTIVE] ...
[PENDING] ...

## Approved script
status:
file:

## Selected hooks
status:
hooks:
formato: fiel-validacao | puzzle-10
acao estrutural:
eixos de troca:

## Current avatar assets
image prompts:
video prompts:

## Completed
- ...

## Pending
- ...

## User decisions
- Decision:
  Reason:
  Operational consequence:

## Next response format
- ...
```

O arquivo termina com uma unica `Next action` concreta. Nao registrar raciocinio, transcricoes ou
analises longas.

## Âncora e cenário por gancho (Luigi, 2026-09-14; âncora revista em 2026-09-22)

> 🔴🔴 **2026-10-04 (Luigi): CENÁRIO E ÂNGULO DO VÍDEO MODELO, QUASE 100% FIÉIS; ANEXO = CHARACTER
> SHEET; TUDO ORGÂNICO, NADA SOBRENATURAL. VALE SÓ PARA O AURALY APP.** Palavras dele: *"quero que os
> prompts sejam detalhando bem o ambiente [...] porque eu quero diversificar o cenário e não me prender
> a somente um que não está validado"* e, na mesma data, *"quero que seja o mais orgânico possível, não
> quero nada sobrenatural; puxe bastante do cenário do vídeo que está sendo modelado, não inventa muita
> moda em questão de cenário; só coloca as regras padrões de realismo [...] mas o ângulo e o cenário
> têm que ser quase 100% fiéis ao vídeo que a gente está modelando"*. **Revoga, só no Auraly, a parte
> de CENÁRIO do avatar fixo por conta (2026-09-25, logo abaixo).** FitWell (Ângulos 2 e 4) e Sea Moss
> (Ângulo 1) continuam com avatar fixo por conta, roupa e cenário da âncora, sem mudança nenhuma.
>
> 1. **O CENÁRIO É O DO VÍDEO MODELO.** O `scene` reproduz o ambiente do modelo quase 100%: o mesmo tipo
>    de lugar, a mesma disposição, os mesmos móveis e superfícies, as mesmas cores, a mesma janela ou
>    parede atrás, os mesmos objetos de fundo. **Não inventar cenário.** É assim que o cenário varia
>    entre produções: cada vídeo modelo traz o seu. Se o modelo está num sofá de couro com parede creme,
>    o nosso está num sofá de couro com parede creme.
> 2. **O ÂNGULO DE CÂMERA É O DO VÍDEO MODELO**, quase 100%: altura, distância, lente, inclinação,
>    selfie na mão ou celular apoiado, enquadramento e quanto do corpo aparece. Medido no frame do modelo
>    e escrito na `FICHA_FRAMES.md` (F4) e no campo `camera`. Não adaptar a câmera ao cenário da âncora.
> 3. **Muda só o que a lei e o acabamento obrigam**, as regras de sempre do `GATE_VISUAL.md` Partes 1 a
>    3: luz neutra de dia nublado no lugar de abajur ou luz quente; céu ou janela com cor e textura,
>    nunca branco ou estourado; herói do gancho colado na lente (nunca mais longe que no modelo); tudo
>    em foco, sem blur; trecho de realismo; 2 a 3 âncoras de fundo (as do próprio modelo); bandeira dos
>    EUA como detalhe discreto (obrigatória no formato IA, opcional no orgânico); sem texto na imagem.
>    Cada mudança dessas vai declarada como desvio na ficha, nunca como cenário novo.
> 4. **ORGÂNICO, NADA SOBRENATURAL.** Nos K e nos V do Auraly: nada de brilho mágico, aura, luz que sai
>    de objeto, partícula, objeto flutuando, fumaça mística, portal ou efeito visual. Cartas, cristal e
>    vela entram só como objetos comuns de casa. O único caso de efeito é quando o PRÓPRIO vídeo modelo
>    tem, e aí ele é copiado como no modelo (fidelidade), nunca acrescentado.
> 5. **Anexo de identidade em todo `K__` = o CHARACTER SHEET do avatar**, em
>    `producao/_ancoras/character_sheets/<avatar>_character_sheet.jpg` (gerado com
>    `producao/_ancoras/PROMPT_CHARACTER_SHEET_AURALY_2026-10-04.md`). Trava rosto, pele, cabelo, corpo e
>    roupa. **É o ÚNICO anexo (Luigi, 2026-10-06): o frame do modelo NÃO é mais anexado** (nem no K nem no V; no V
>    o único anexo é a imagem escolhida do K). Cenário, ângulo e enquadramento do modelo vão por extenso no
>    texto. A foto em cena real deixa de ser anexo dos K. Roster com sheet: Avery Knox, Devon Price, Jordan Vale e Morgan
>    Vance (nomes = arquivos do Luigi).
> 6. **`reference_use` padrão:** `Use the first attached image (character sheet) only for [Name]'s exact
>    identity (face, skin, hair, body) and wardrobe; ignore its grey studio background. The setting, camera
>    angle and framing are described in full in the scene, camera and composition fields; no other image is
>    attached.` (v20, 2026-10-06: sem segunda imagem.) Proibido no K do Auraly: `the same
>    lived-in room as the reference`, `as the reference, unchanged`, `own setting` (o linter reprova).
> 7. **O `scene` descreve por escrito o cenário do modelo**, porque o K é autossuficiente: o lugar (e a
>    região dos EUA quando dá para ler), parede, piso e móveis com cor, a janela ou o céu com cor e de
>    onde vem a luz, as 2 a 3 âncoras de fundo do modelo com a posição no quadro, e a bandeira. Na
>    `FICHA_FRAMES.md` cada `## Kxx` ganha a linha `Cenário do modelo:` com o que se vê atrás no frame,
>    e o `scene` sai dela (o linter reprova a ficha sem essa linha).
> 8. **Registro:** `Scenario: <cenário do modelo em poucas palavras>` no `CHECKPOINT.md` (o linter
>    reprova sem) e a linha em `producao/_ancoras/CENARIOS_AURALY.md`, que é histórico por conta e
>    nunca vence a fidelidade ao modelo: se dois modelos têm o mesmo tipo de cômodo, copia-se o modelo.
> 9. **Roupa:** a do character sheet, igual em todo K e todo vídeo da conta, até o Luigi decidir outra
>    coisa.
> 10. **Pacotes entregues antes de 2026-10-04 não se reescrevem** (`controle/cenario_auraly_legado.json`).

> ♻️ **2026-09-25: AVATAR FIXO POR CONTA (Luigi).** ⚠️ *No Auraly a parte de CENÁRIO foi revogada em
> 2026-10-04 (bloco acima); a roupa continua fixa, agora pelo character sheet.* *"sim, vale para o Auraly também"*. Cada conta
> usa **o mesmo avatar com a roupa e o cenário-base da âncora em todo vídeo e em todo gancho**; o que
> varia entre vídeos é o conteúdo. **Revoga os itens 2 e 3 abaixo** (cenário próprio e roupa livre
> por gancho). O ângulo de câmera continua podendo variar para servir à ação estrutural (item 4).
> Se o vídeo modelo tem uma cena em outro lugar, ela acompanha o modelo com a mesma pessoa e a mesma
> roupa. O único formato sem avatar fixo é o movie style / short form. Mesma regra da FitWell
> (`PERFIL_ORGANICO.md` seção 4.1 e checklist B8).

> ♻️ **2026-09-22: a FINGERPRINT caiu.** O Luigi reprovou o resultado e decidiu produzir com as
> imagens de teste em cena real. **Roster único do Ângulo 3: Walt Hensley, Darlene Pruitt e Lorraine
> Vance**, âncoras em `producao/_ancoras/walt_hensley_ancora.jpg`, `darlene_pruitt_ancora.jpg` e
> `lorraine_vance_ancora.jpg`. A âncora vai anexada em todo `K__`. Quando o cenário do gancho é o da
> âncora, o `K__` descreve esse cenário por escrito; quando o gancho pede cenário ou roupa novos, o
> `K__` diz `use the attached image only for his/her identity (face, eyes, hair, skin, body,
> signature); ignore its clothing, background and props` e descreve o cenário novo inteiro. Os itens
> abaixo que falam de fingerprint ficam valendo só como lógica de "identidade separada do cenário".

Testado em 2026-09-14 com um avatar hoje descartado e aprovado. Revoga o modelo de âncora
única + corpo compartilhado como padrão de todo Ângulo 3 daqui pra frente.

**O que muda:**

1. **A referência de identidade deixa de ser uma foto de ambiente real e vira uma FINGERPRINT**:
   grade de estúdio, fundo neutro, rosto em vários ângulos, corpo de frente/lado/costas, macro de
   pele. Ela trava **somente rosto, textura de pele, tipo físico e cabelo**. Nunca trava roupa,
   cenário, pose ou luz.
2. ~~**Cada gancho escolhido vira um vídeo com CENÁRIO PRÓPRIO, do T1 ao CTA**~~ (revogado em
   2026-09-25: o cenário é o da âncora em todos os ganchos). Texto histórico: não mais "5 hooks
   compartilhando um corpo comum". Isso significa um `K` de hook + um `K` de corpo (serve T2 a T5)
   + um `K` de CTA (edição textual do corpo, mais fechado) **por cenário**, não um só conjunto
   compartilhado pela fila de ganchos.
3. ~~**Liberdade total de roupa por cenário.**~~ (revogado em 2026-09-25: a roupa é a da âncora). A roupa da fingerprint não é obrigatória em nenhum
   `K`; cada cenário ganha a roupa que fizer sentido com o ambiente e o físico.
4. **O angulo de camera serve a acao estrutural.** Pode ser exótico quando aumenta a anomalia, mas
   nao e obrigatorio mudar o angulo em toda variacao. Preservar a acao estrutural e o timing pode
   exigir repetir o enquadramento; mudar o angulo conta como a unica variavel da variacao.
5. **Excecao de T1/hook aprovada em 2026-09-20:** o kit completo de tarologo nao e obrigatorio no
   primeiro segundo. Usar de zero a dois marcadores discretos somente se nao competirem com a
   anomalia principal. Do T2 ao CTA, permanecem as regras de credencial visual e carta previstas em
   `memoria/angulo3_copy_auraly.md`, salvo excecao de producao registrada no checkpoint.
6. **Copy, roteiro e ganchos continuam aprovados uma única vez pra fila inteira.** Isso não muda:
   só a pele visual varia por cenário, nunca a fala.
7. **Os CORTES do T1 vao DENTRO do prompt de video (Luigi, 2026-09-20).** Medido em 54 virais do
   nicho: 5 a 7 mudancas de plano nos primeiros 6 segundos e **zero cortes** nos 70 a 130 segundos
   seguintes, e os 3 primeiros segundos 14 a 17 dB abaixo do corpo, o que e room tone e nao fala
   baixa. ⚠️ **Nao sao varios clipes: e UM clipe so**, com as mudancas de plano escritas no `V__` e
   geradas pelo Veo no mesmo take. Consequencias, **validas so no T1**:
   - **continua `1 K + 1 V`**, sem excecao ao `UMA IMAGEM = UM VIDEO`. O `K__` do gancho e o
     **primeiro plano** da sequencia; o resto nasce dentro do `V__`;
   - o bloco `o que acontece no video` carrega a sequencia: **acao ja comecada > corte para MACRO
     das maos no instante do payoff > corte de volta ao plano de corpo**. Excecao consciente ao
     "menos e mais na descricao da acao", valida so aqui;
   - o bloco `camera` declara **cortes internos ao clipe**, em vez de `fixa / push-in`;
   - **o T1 nasce MUDO:** marcar `T1 · B-ROLL · MUDO` no `ROTEIRO.md` e abrir o `V__` com
     `(sem fala no take: ...)`. O `checar_entrega.py` ja aceita (`:78`, `:138`, `:254`);
   - **split vertical liberado** (rosto em cima, ritual embaixo), descrito dentro do `V__`, so aqui.
   **Do T2 em diante o plano unico volta a ser obrigatorio** e o contrato de take de 8s e integral.
   **Custo do gancho nao muda: 1 keyframe + 1 clipe por variacao.**
   Detalhe e medicoes em `producao/analise_ganchos_maya_claude_2026_09_20/ANALISE_MEDIDA_GANCHOS.md`
   e nas memorias `gancho-sequencia-montada-auraly` e `constrangimento-produtivo-auraly`.

**Custo sobe de propósito.** O modelo antigo gastava ~7 `K` e 10 `V` por avatar (5 hooks + 1 corpo
comum + 1 CTA). O novo modelo gasta ~15 `K` e o mesmo tanto de `V` que a fila de ganchos escolhida
exigir (6 `V` por cenário: 1 mudo + 4 falados + 1 CTA). Luigi confirmou que vale o custo.

**Exemplo dos 5 cenários aprovados em 2026-09-14** (cozinha câmera de cima, varanda câmera deitada,
escritório três-quartos holandês, ateliê baixo lateral, sala de meditação alto diagonal): pacote
arquivado em `_arquivo/2026-09-22_limpeza_angulo3/producao/oliviamadison671/`, só como referência de
variedade de cenário, nunca de avatar.

**Entrada do `/watch` desde 2026-09-22:** as imagens que vêm junto do `.mp4` são as âncoras em cena
real do roster (Walt, Darlene, Lorraine e, desde 2026-09-30, Morgan Vance em
`producao/_ancoras/morgan_vance_ancora.jpg`, conta orgânica nova). Se chegar imagem de um avatar fora do roster, perguntar antes
de produzir (`avatar-so-o-que-o-luigi-mandar`).

**Instruções do agente Flow correspondentes: v10**, em `producao/_flow/INSTRUCOES_AGENTE_FLOW.md`.
A ETAPA 0 muda de "âncora trava identidade + roupa + cenário" para "fingerprint trava só
identidade/corpo/pele, roupa e cenário vêm do texto de cada `K`".

---

## Travas permanentes

- Roteiro aprovado uma vez para toda a fila.
- **Cenário e ângulo de câmera do VÍDEO MODELO, quase 100% fiéis, orgânico e sem nada
  sobrenatural; anexo = character sheet (Luigi, 2026-10-04, só Auraly).** Só o acabamento do
  `GATE_VISUAL.md` muda. `Scenario:` no checkpoint e `Cenário do modelo:` em cada K da ficha.
- Hooks selecionados uma vez para toda a fila.
- **Validar antes de variar (2026-09-23):** producao nova e `Round: VALIDATION`, com UM hook fiel ao
  modelo e sem selecao de hook. As 10 so existem em `Round: VARIATION`, aberta pelo Luigi depois de
  um video postado performar.
- Na rodada de variacao, gerar exatamente 10 hooks antes da selecao, **todos do mesmo esqueleto**,
  que e o hook do video validado. ♻️ Revoga o portfolio `4 + 3 + 3` em tres familias, de 2026-09-20.
- **Nenhum hook, K ou V e enviado sem o checklist de envio 100% aprovado** (`GATE_VISUAL.md` Parte 5).
- Preservar a acao estrutural do modelo e mudar **uma unica variavel central** por hook.
- **Puzzle com degrau (2026-09-22):** peca viral intocavel, UM degrau no esqueleto, HOOK 1 como
  controle sem degrau. `GATE_VISUAL.md` Parte 4.
- Declarar a acao estrutural uma vez no topo e a variavel trocada em cada hook.
- O metodo e o mesmo da FitWell; o que muda e que aqui clickbait puro e liberado e a congruencia
  trava na fala, nunca no objeto do gancho.
- ♻️ **2026-10-04 (Luigi): orgânico, nada sobrenatural.** Efeito visual só quando o PRÓPRIO vídeo modelo
  tem, copiado como no modelo. (Histórico:) Efeito visual simples e legivel e permitido no T1 (uma rachadura, brilho, cor ou revelacao). Nao
  combinar varios efeitos nem transformar o hook em cena cinematografica desconectada do roteiro.
- Formatos limpos `K__` e `V__`; a relacao de INITIAL FRAME vem do `MAPA K/V` explicito.
- Um K pode alimentar varios V do mesmo setup; nenhum V pode existir sem K mapeado e aprovado.
- Entrega textual K+V na mesma resposta; execucao em duas fases, com selecao manual do K antes do V.
- O Codex nao gera imagens nem executa navegador ou Google Flow.
- Instrucoes canonicas do executor: `producao/_flow/INSTRUCOES_AGENTE_FLOW.md`.
- Preservar Nano Banana 2, 9:16, anchor, 4 imagens por prompt e selecao manual.
- Preservar Veo 3.1 Lite, Lower Priority, 8 segundos e UM unico resultado por V (Luigi, 2026-10-05: sempre 4 imagens por K e 1 video por V, em todos os perfis; revoga as 3 variacoes).
- Video usa o `K__` correspondente exclusivamente como INITIAL FRAME, nunca como Element.
- Flow executa `V__` em CLOSED BATCHES de no maximo 7 codigos, sem preencher vaga liberada.
- Esperar todos do lote; se houver pendentes, parar e aguardar `prossiga`.
- Nunca reiniciar `V__` concluido sem pedido explicito.
- `AVATAR DONE != PRODUCTION DONE`.
