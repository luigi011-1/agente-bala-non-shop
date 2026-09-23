---
name: faixa-palavras-take
description: "Faixa fechada: 13 a 29 palavras por take, exatamente o que checar_entrega.py:230 exige. Teto subiu de 25 para 29 em 2026-08-26; piso de 13 confirmado em 2026-08-29. Os 26 takes antigos abaixo de 13 continuam reprovando de proposito, e nao se reescreve roteiro publicado."
metadata: 
  node_type: memory
  type: project
  originSessionId: 743d3401-da9c-4753-ba54-509bfe4c9d13
  modified: 2026-08-29T03:02:33.743Z
---

# Faixa de palavras por take: 13 a 29, fechada

**A fonte de verdade é o `checar_entrega.py`**, linha 230: `if n < 13 or n > 29`. Qualquer dúvida
sobre a faixa se resolve lendo o linter, não a lembrança.

**2026-08-26, decisão do Luigi:** o teto subiu de **25 para 29** palavras. Motivo em
[[regras-universais]] regra 6B: o gabarito `brandon_angle2` sempre teve takes de 26 a 29 e eles
funcionam, então quem estava errado era a faixa, não os roteiros.

**2026-08-29, decisão do Luigi:** o **piso de 13 fica**, alinhado ao linter. A pergunta que estava
em aberto desde 2026-08-26 está respondida: não desce.

**Consequência aceita, não é bug.** Rodando `checar_entrega.py --todos`, **26 takes de produções
antigas** continuam abaixo de 13 (3 de 4 palavras, 3 de 7, 1 de 8, 2 de 9, 6 de 10, 4 de 11 e 6 de
12), mais um único take de 30 acima do teto. Eles **permanecem reprovados de propósito**.

**How to apply:** produção NOVA nasce dentro de 13 a 29, contado antes de escrever os prompts.
Quando o linter acusar essas falhas num pacote antigo, é histórico conhecido e não regressão:
**não reescrever roteiro que já foi ao ar para satisfazer linter**. Take curto pode ser deliberado
(fecho seco, "Two two two", ordem de uma linha).

**Why:** mexer em roteiro publicado pra agradar o linter é a inversão do que o linter serve. A
regra existe pro roteiro, não o contrário. Ver [[prompts-video-fase7]].

Aplicado em: `CLAUDE.md`, skill `/produzir`, `checar_entrega.py`, `.claude/hooks/gabarito_hook.py`
(este último estava travado em 25 até 2026-08-29) e [[erros-recorrentes]].
