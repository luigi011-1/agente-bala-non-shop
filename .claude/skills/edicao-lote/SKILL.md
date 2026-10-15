---
name: edicao-lote
description: Edição automática de uma FILA inteira de vídeos (lote), 3 em paralelo na ordem da fila aprovada na conversa, até zerar a fila. Use quando os roteiros do lote já foram aprovados, os takes do Flow chegaram e o Luigi manda editar ("edita o lote", "pode editar", "takes prontos", pastas de takes de vários vídeos). Para UM vídeo avulso use o agente editor-video; para o estilo da edição em si, a skill edicao.
---

# Edição em lote: 3 por vez, na ordem da fila (Luigi, 2026-10-15)

> *"quando a fila já estiver definida na conversa após eu aprovar os roteiros e produzir os takes, pra edição
> automática vamos seguir a ordem que definimos na fila daquela conversa e serão editados automaticamente 3
> vídeos em paralelo; acabou a edição dos 3? partimos para os próximos 3 da fila, até concluirmos a fila."*

Por que 3: teste de 2026-10-15 no MacBook Air M2 (8 núcleos, 16 GB). 3 juntos ≈ 4 min para os 3; 5 juntos levaram
13 min e cada render ficou 3-7x mais lento (sem ganho sobre a fila). Revisão e resolução de fala são leves e
podem rodar enquanto o próximo lote renderiza; **render nunca passa de 3 ao mesmo tempo** (inclusive variador-hooks
e editor-video avulso contam como render).

Edição continua sem pausa e sem perguntar (memória `edicao-autonoma-sem-interferencia`): decidir, registrar, seguir.

## Papéis

| Quem | O que faz | Onde roda | Modelo |
|---|---|---|---|
| **Orquestrador** (a sessão principal, esta skill) | monta a fila, liga o executor, despacha revisores e resolvedores, atualiza a fila, avisa o Luigi | conversa | o da sessão |
| **Executor** `fila_edicao.py` | roda o `editar.py` em lotes de 3, entrega na pasta dos takes, grava estado e `STATUS_EDICAO.md` | `nohup`, sem IA | — |
| **revisor-visual** (agente) | conferência 19 de UM vídeo: legenda sobre rosto/produto/bordas, selos Auraly | em paralelo, 1 por vídeo `EDITED` | sonnet |
| **resolvedor-fala** (agente) | UM vídeo `BLOCKED_FALA`: exceção de escuta, corte do take, ou take de volta pro Flow | em paralelo, 1 por vídeo travado | sonnet |
| **editor-video** (agente) | só vídeo avulso / reedição fora da fila | sob demanda | haiku |
| **variador-hooks** (agente) | variações de abertura de vídeo aprovado | fora da fila, conta como render | sonnet |

Estilo e regras de corte, legenda, música: skill `edicao` + `docs/pos-producao-edicao-regras.md` (o executor já cumpre).
Compliance de copy não entra aqui: é do pacote (`checar_entrega.py`), antes do Flow.

## Passo a passo do orquestrador

1. **Fila.** Já nasce na produção: a `/produzir` (e o workflow Auraly) roda `fila_edicao.py --adicionar` a cada pacote
   de avatar entregue, na ordem aprovada, e cria `~/Desktop/<lote>/<NN>_<modelo>_<avatar>/` para os takes. Se o lote é
   antigo e não tem `FILA_EDICAO.json`, crie com o mesmo comando, item por item, na ORDEM aprovada na conversa
   (modelos x avatares do `AGENTS.md`, salvo ordem diferente dita pelo Luigi). Se o Luigi soltou os takes em outra
   pasta, corrija `takes_folder` do item.
2. **Antes de ligar.** `df -h /tmp` (≥ 3 × 2,5 GB + 3 GB). Take mudo renomeado `tNN_` e sem áudio (`-an`), como manda
   `producao_licoes_lote_1014`. Não precisa marcar `RECEIVED`: o executor marca sozinho quando a pasta tem
   `take_count` .mp4 e nada mudou há 2 min.
3. **Ligar o executor** (uma vez, em segundo plano, nunca como comando do Monitor):
   `nohup .venv-operacao/bin/python .claude/skills/edicao-lote/fila_edicao.py producao/<lote>/FILA_EDICAO.json --esperar-takes 60 > producao/<lote>/edicao_fila.log 2>&1 &`
   Ele segura o Mac acordado (`caffeinate`) enquanto roda; com a tampa fechada, só na tomada. `--esperar-takes 60`
   deixa ele esperando até 1 h por takes que ainda não chegaram antes de encerrar.
   Acompanhar com Monitor só fazendo `tail -f` do log, esperando `TAKES_RECEBIDOS`, `VIDEO_FIM`, `LOTE_FIM`,
   `FILA_FIM`, `DISCO_CHEIO`.
4. **A cada `LOTE_FIM`** (enquanto o próximo lote já renderiza):
   - cada vídeo `EDITED` → um `revisor-visual` (todos em paralelo, background) com o MP4 e o `report_folder`;
   - cada `BLOCKED_FALA` → um `resolvedor-fala` (paralelo). Ele devolve o item para `PENDING` (a fila reedita) ou
     `BLOCKED_TAKE` (take volta pro Flow, em `TAKES_PARA_CORRIGIR.md`);
   - `FAILED` → ler o log do item; erro de ambiente (disco, iCloud, python) se corrige e volta para `PENDING`.
5. **Resultado da revisão.** APROVADO → `APPROVED`. REPROVADO → `REVIEW_FAIL` com o motivo no `note`; se a correção
   cabe em argumento do editor (ex.: `--legenda-topo`, `--up`), grave em `extra_args` e volte para `PENDING`.
6. **Fila zerou com itens que voltaram para `PENDING`** → ligar o executor de novo (passo 3). Ele pega só o que falta.
7. **Avisar o Luigi** a cada lote: uma linha por vídeo (estado, arquivo). No fim, tabela do `STATUS_EDICAO.md`.

## Estados (`editing_status`)
`PENDING` → `EDITING` → `EDITED` → `APPROVED` | `REVIEW_FAIL`
`EDITING` → `BLOCKED_FALA` → (`PENDING` | `BLOCKED_TAKE`) · `EDITING` → `FAILED`
Item com takes ainda não recebidos fica `PENDING` com `takes_status: NOT_RECEIVED` e não trava ninguém.

## NÃO FAZER (tão obrigatório quanto o passo a passo)
- Não passar de 3 renders ao mesmo tempo (contando `editor-video` avulso e `variador-hooks`).
- Não ligar um segundo executor na mesma fila nem rodar o `editar.py` à mão em vídeo que está na fila.
- Não mudar a ordem da fila aprovada na conversa nem pular vídeo com takes recebidos.
- Não começar o próximo lote antes de os 3 do lote atual terminarem (o executor já espera; não force).
- Não editar, revisar ou resolver fala com as próprias mãos na conversa: despache o agente certo.
- Não parar para perguntar ao Luigi no meio da fila; só a decisão que é dele (take sem autorização para ir assim).
- Não marcar `APPROVED` sem o veredito do `revisor-visual`.
- Não recomprimir abaixo de 100 MB (regra 21).
- Não reescrever roteiro pela transcrição; não criar exceção para repetição (ver resolvedor-fala).
- Não apagar takes originais; a pasta de trabalho em `/tmp/edicao` o executor apaga sozinho depois de copiar.
- Não usar o Monitor para rodar o executor (ele mata o comando ao expirar): só para `tail -f` do log.
- Não alterar motor, regras ou skills durante a fila; achado vira nota no `STATUS_EDICAO.md` e se corrige depois.
