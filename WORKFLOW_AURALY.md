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
-> SCRIPT_MODELLING
-> WAITING_SCRIPT_APPROVAL
-> HOOK_IDEATION, exatamente 10 hooks
-> WAITING_HOOK_SELECTION
-> bloquear hooks para toda a fila
-> IMAGE_PROMPTS do avatar ativo
-> WAITING_IMAGE_SELECTION
-> VIDEO_PROMPTS do avatar ativo
-> avatar DONE
-> proximo avatar ACTIVE
-> repetir IMAGE_PROMPTS + VIDEO_PROMPTS adaptando apenas identidade visual
-> todos os avatares DONE
-> PRODUCTION_COMPLETE
```

## Regra de estado

Toda pasta de producao Auraly deve conter `CHECKPOINT.md`. Atualizar imediatamente depois de cada
aprovacao, selecao, entrega de pacote ou mudanca de avatar. Registrar somente fatos, decisoes e uma
unica proxima acao concreta.

Estados canonicos: `INTAKE`, `WAITING_ANGLE`, `ANALYSIS`, `METHOD_PUZZLE`, `SCRIPT_MODELLING`,
`WAITING_SCRIPT_APPROVAL`, `HOOK_IDEATION`, `WAITING_HOOK_SELECTION`, `IMAGE_PROMPTS`,
`WAITING_IMAGE_SELECTION`, `VIDEO_PROMPTS`, `AVATAR_TRANSITION` e `PRODUCTION_COMPLETE`.

Estados `WAITING_*` sempre significam parar e aguardar o usuario.

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

### HOOK_IDEATION

Abrir somente o roteiro aprovado, `producao/_swipe_auraly/BANCO_GANCHOS_VISUAIS.md` e as secoes de
hook de `memoria/angulo3_swipe_padroes.md`. Gerar exatamente 10 conceitos. O banco historico serve
principalmente para evitar repeticao. Regra: `IMPACT FIRST / CURIOSITY SECOND / CONGRUENCE ALWAYS`.

### IMAGE_PROMPTS

Abrir somente checkpoint, hooks selecionados, roteiro aprovado, anchor ativa e regras vigentes de
prompt de imagem. Manter hooks e copy bloqueados. Entregar somente `K__`.

### VIDEO_PROMPTS

Abrir somente checkpoint, imagens `K__` aprovadas e roteiro/takes aprovados. Entregar somente `V__`.
Cada `V__` corresponde ao `K__` de mesmo numero.

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

04 - WAITING FOR APPROVAL
```

Definir `Current stage: WAITING_SCRIPT_APPROVAL` e parar.

### Hooks

```text
HOOK 1 - nome
Cena:
[descricao]
Por que para o scroll:
[motivo]

...

HOOK 10 - nome
Cena:
[descricao]
Por que para o scroll:
[motivo]

WAITING FOR HOOK SELECTION
```

Definir `Current stage: WAITING_HOOK_SELECTION` e parar.

### Prompts de imagem

Entregar somente um bloco copiavel:

```text
K01
[prompt completo e autossuficiente]

K02
[prompt completo e autossuficiente]
```

Sem descricao, titulo, `T__`, metadata ou `Prompt:`. Nao incluir `V__` na mesma resposta. Definir
`Current stage: WAITING_IMAGE_SELECTION` e parar.

### Prompts de video

Entregar somente um bloco copiavel:

```text
V01
[prompt completo e autossuficiente]

V02
[prompt completo e autossuficiente]
```

Sem descricao, titulo, `T__`, `usa K__`, metadata ou configuracao do Flow. Nao reabrir roteiro,
hooks ou prompts de imagem.

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

## Travas permanentes

- Roteiro aprovado uma vez para toda a fila.
- Hooks selecionados uma vez para toda a fila.
- Gerar exatamente 10 hooks antes da selecao.
- Formatos limpos `K__` e `V__`; `K01` corresponde a `V01` pelo numero.
- O Codex nao gera imagens nem executa navegador ou Google Flow.
- Instrucoes canonicas do executor: `producao/_flow/INSTRUCOES_AGENTE_FLOW.md`.
- Preservar Nano Banana 2, 9:16, anchor, 4 imagens por prompt e selecao manual.
- Preservar Veo 3.1 Lite, Lower Priority, 8 segundos e 3 variacoes.
- Video usa o `K__` correspondente exclusivamente como INITIAL FRAME, nunca como Element.
- Flow executa `V__` em CLOSED BATCHES de no maximo 7 codigos, sem preencher vaga liberada.
- Esperar todos do lote; se houver pendentes, parar e aguardar `prossiga`.
- Nunca reiniciar `V__` concluido sem pedido explicito.
- `AVATAR DONE != PRODUCTION DONE`.
