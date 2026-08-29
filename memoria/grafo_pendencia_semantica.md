---
name: grafo-pendencia-semantica
description: "PENDENTE, o Luigi pediu para ser lembrado ANTES da proxima producao: falta a passada semantica que cria arestas conceito-a-conceito entre memoria/ e producao/ no grafo do graphify. Custo estimado ~1M tokens so nos docs, ~100 subagentes a mais se incluir as imagens. Adiado em 2026-08-29 por custo."
metadata: 
  node_type: memory
  type: project
  originSessionId: 743d3401-da9c-4753-ba54-509bfe4c9d13
  modified: 2026-08-29T03:04:30.102Z
---

# Grafo do graphify: a passada semantica que ficou pendente

**Lembrar disto ANTES de comecar a proxima producao.** Foi pedido explicitamente pelo Luigi em
2026-08-29: adiar por custo, mas nao deixar cair no esquecimento.

## O que ja esta pronto (nao refazer)

`graphify-out/graph.json`: **1110 nos, 2239 arestas, 96 comunidades, 1 componente conexo, 0
isolados**. Cobre `memoria/`, `PLAYBOOK_COMPLETO/` e `producao/`. Consulta via
`graphify query`, `graphify explain` e `graphify path --undirected`. O `--undirected` e
obrigatorio no `path`, senao responde "no path" com caminho existindo.

As duas metades foram unidas com `graphify merge-graphs`, mais **19 pontes de evidencia textual**
(o rotulo do no de doutrina cita o slug da pasta, ou o arquivo de doutrina cita a pasta pelo nome)
e um **esqueleto documental** (conceito, arquivo, pasta, projeto) que zerou os nos orfaos.

## O que falta

**Arestas conceito-a-conceito atravessando os dois corpora.** Hoje da para ir de um video ate a
doutrina, mas nao existe aresta ligando *cada* regra ao *cada* take que a aplicou. As duas metades
foram extraidas em passadas separadas, entao nenhum subagente viu doutrina e producao juntas.

## Por que foi adiado: o custo, medido

A passada sobre os **52 arquivos** de `memoria/` + `PLAYBOOK_COMPLETO/` custou **689.783 tokens**
em 3 subagentes, e ainda assim **estourou o limite de sessao** no meio (um chunk teve de ser
retomado). `producao/` tem ~85 documentos e ~100 imagens:

- so os documentos: ~4 subagentes, da ordem de **1M tokens**
- com as imagens: **~100 subagentes a mais** (visao exige um chunk por imagem)

## How to apply

Nao rodar isso no meio de uma producao, porque o limite de sessao e compartilhado e derruba os dois.
Se for rodar, rodar sozinho e com a sessao fresca. Se o Luigi so quiser o ganho barato, os
documentos de `producao/` sem as imagens ja entregam quase toda a ligacao semantica, porque a copy
mora no `ROTEIRO.md`, no `PROMPTS_PRODUCAO.md` e no `DM.md`, nao nas ancoras.

**Enquanto isso o grafo e um retrato de 2026-08-28:** producao nova nao entra sozinha. Tratar
resposta do grafo como datada e conferir no arquivo o que for decisivo. Ver [[workflow-entrega-gabarito]].
