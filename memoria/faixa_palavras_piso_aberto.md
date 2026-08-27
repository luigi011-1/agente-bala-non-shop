---
name: faixa-palavras-piso-aberto
description: "Teto de palavras por take subiu de 25 para 29 em 2026-08-26 por decisao do Luigi. O PISO de 13 continua em aberto: 26 takes das producoes antigas ficam abaixo dele (de 4 a 12 palavras) e o linter reprova todos. Perguntar antes de assumir."
metadata:
  type: project
---

# Faixa de palavras por take: teto resolvido, piso em aberto

**2026-08-26, decisão do Luigi:** o teto subiu de **25 para 29** palavras. Motivo registrado em
[[regras-universais]] regra 6B: o gabarito `brandon_angle2` sempre teve takes de 26 a 29 e eles
funcionam, então quem estava errado era a faixa, não os roteiros. Já aplicado no `CLAUDE.md`,
na skill `/produzir`, no `checar_entrega.py` e nas memórias.

**O piso de 13 NÃO foi decidido.** Rodando o `checar_entrega.py --todos`, sobram **26 takes abaixo
de 13 palavras** nas produções antigas, distribuídos assim: 3 takes de 4, 3 de 7, 1 de 8, 2 de 9,
6 de 10, 4 de 11 e 6 de 12. Mais um único take de 30, acima do teto novo.

**How to apply:** o linter reprova todos esses hoje. Se o Luigi pedir pra "limpar as falhas de
palavras", **perguntar primeiro se o piso desce**, em vez de reescrever 26 takes de vídeos que já
foram ao ar. Takes curtos podem ser deliberados (fecho seco, "Two two two", ordem de uma linha).

**Why:** mexer em roteiro publicado pra satisfazer um linter é a inversão do que o linter serve.
A regra existe pro roteiro, não o contrário. Ver [[prompts-video-fase7]].
