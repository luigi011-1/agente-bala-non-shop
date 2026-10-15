---
name: instrucao-agente-com-nao-fazer
description: Toda instrução para agente, subagente ou skill leva uma seção NÃO FAZER tão explícita quanto o que fazer (Luigi, 2026-10-15)
metadata:
  type: feedback
---

Luigi, 2026-10-15: *"quando for falar para os agentes, subagentes e skills suas respectivas tarefas, falar o que eles
NÃO devem fazer é tão importante quanto falar o que eles DEVEM fazer"*.

**Why:** agente sem limite escrito invade a tarefa do vizinho (revisor que reedita, editor que conserta fala, reviewer
que reprova copy fora do escopo) e o lote perde velocidade e previsibilidade. No teste de 5 vídeos, revisores
reprovaram por coisas fora do escopo pedido.

**How to apply:** ao criar ou editar definição de agente (`~/.claude/agents/*.md`), SKILL.md ou prompt de subagente,
incluir sempre uma seção `## NÃO FAZER` com: o que é tarefa de outro agente, o que não pode alterar (motor, regras,
roteiro, originais), limites de recurso (máx. 3 renders no Mac), e quando não deve perguntar ou decidir no lugar do
Luigi. Vale também para o prompt de cada despacho avulso de subagente. Ver [[edicao-fila-lotes-de-3]].
