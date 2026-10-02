---
name: grafo-pendencia-semantica
description: "Custos MEDIDOS da passada semantica do grafo e o que sobrou. A parte cara foi substituida por casamento determinista em 2026-08-29 (grafo_rotas.py). O que resta e opcional: ~401k tokens so nos ROTEIRO.md. NUNCA rodar a passada de imagens, ~3M de tokens pelo pior retorno do projeto."
metadata:
  type: project
---

# Grafo: o que a passada semantica ainda renderia, e a que custo

**Lembrar antes da proxima producao.** O Luigi estava com 88% do limite semanal em
2026-08-29, entao o custo aqui e decisao, nao detalhe.

## A taxa medida, que serve para qualquer estimativa futura

A passada nos 54 arquivos de doutrina custou **689.783 tokens** para 68.324 palavras de
corpus, ou seja **10,1 tokens por palavra**. Use essa taxa antes de despachar subagente.

| Alvo em `producao/` | Arquivos | Palavras | Tokens estimados |
|---|---|---|---|
| `PROMPTS_PRODUCAO.md` | 19 | 123.709 | **~1.249.000** |
| `ROTEIRO.md` | 17 | 39.764 | ~401.000 |
| outros `.md` | 8 | 11.228 | ~113.000 |
| `DM.md` | 8 | 7.936 | ~80.000 |
| imagens | 99 | | **~3.000.000** (menos confiavel) |

## O que JA foi resolvido de graca (nao refazer)

`grafo_rotas.py`, 2026-08-29. Rota, gatilho de obstaculo e gatilho de virada sao
**vocabulario fechado e numerado**, entao os dois lados do grafo casam por nome sem
LLM nenhum. Rendeu 36 arestas: 7 por numero, 3 por texto descritivo e 34 mencoes
literais nos `ROTEIRO.md`. Hoje `brandon_pulmao/ROTEIRO.md` alcanca
`Rota 5: a data em que parou de funcionar` em **1 hop**.

Antes disso, `grafo_memoria.py` (204 arestas de wikilink) e `grafo_producao.py`
(287 takes). As duas metades do grafo sao reconstruiveis sem LLM.

## O que sobrou, e a recomendacao

**Opcional, ~401.000 tokens:** passada semantica so nos `ROTEIRO.md`. Renderia relacao
de texto corrido que o vocabulario controlado nao pega (argumento, obstaculo descrito
sem numero, device de copy).

**NUNCA rodar a passada de imagens.** ~3M de tokens pelo pior retorno do projeto: as
imagens sao ancoras e keyframes, e a copy mora nos `.md`.

**Pular `PROMPTS_PRODUCAO.md`.** Sozinhos sao 1,25M dos 1,84M e sao encanamento ja
coberto por [[workflow-entrega-gabarito]], pelo `checar_entrega.py` e pelo
`grafo_producao.py`.

## How to apply

Nao despachar subagente com o limite semanal apertado. Em 2026-08-28 a passada
**estourou o limite no meio** e um chunk queimou 156.374 tokens sem produzir arquivo:
pagar e nao levar e o pior desfecho. Rodar sozinho, com sessao fresca, depois do reset.

Antes de considerar qualquer passada por LLM, perguntar: **isso e vocabulario controlado?**
Se for lista fechada, numerada ou nomeada, casa por string e custa zero. Ver
[[autocobranca-no-canal-repetido]] para o principio irmao.
