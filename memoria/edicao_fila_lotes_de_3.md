---
name: edicao-fila-lotes-de-3
description: "Edição automática da fila: 3 vídeos em paralelo na ordem aprovada na conversa, próximo lote de 3 só quando os 3 terminam, até zerar a fila (Luigi, 2026-10-15); papéis de orquestrador, executor e agentes"
metadata:
  type: feedback
---

Luigi, 2026-10-15: *"quando a fila já estiver definida na conversa após eu aprovar os roteiros e produzir os takes, pra
edição automática vamos seguir a ordem que definimos na fila daquela conversa e serão editados automaticamente 3
vídeos em paralelo, acabou a edição dos 3 vídeos em paralelo? partimos para os próximos 3 da fila... até concluirmos a fila."*

**Why:** teste no MacBook Air M2 em 2026-10-15: 3 acabamentos juntos ~4 min; 5 juntos 13 min, cada render 3-7x mais lento
e sem ganho sobre a fila (load médio 43 em 8 núcleos). 3 é o ponto em que o paralelo ainda rende sem travar o Mac.

**How to apply:**
- Skill `edicao-lote` (repo `.claude/skills/edicao-lote/`): `FILA_EDICAO.json` na ordem aprovada, executor
  `fila_edicao.py` em `nohup` (lotes de 3, barreira entre lotes, `EDICAO_WORKERS=3`, entrega na pasta dos takes,
  `STATUS_EDICAO.md`), Monitor só no `tail -f` do log.
- A cada lote: `revisor-visual` por vídeo EDITED e `resolvedor-fala` por vídeo BLOCKED_FALA, em paralelo com o próximo
  lote (são leves). Render nunca passa de 3 ao mesmo tempo, contando `editor-video` avulso e `variador-hooks`.
- Agentes em `~/.claude/agents/`: editor-video (haiku, só avulso), revisor-visual (sonnet), resolvedor-fala (sonnet),
  variador-hooks (sonnet). Compliance de copy fica no pacote (`checar_entrega.py`), não na edição.
- Achados do teste CORRIGIDOS no motor em 2026-10-15 (erros 30-32 das regras): legenda desce para 1300 px nos takes
  com produto (lido do pacote), Auraly com topo 1300, `acabamento.py` sozinho põe os selos. Ainda sem teste com takes
  reais: conferir no 1º lote.
- O executor marca RECEIVED sozinho, segura o Mac acordado (`caffeinate`) e a `/produzir` cria a fila (`--adicionar`).

Relacionado: [[edicao-autonoma-sem-interferencia]], [[ambiente-mac-luigi]], [[edicao-licoes-teste]].
