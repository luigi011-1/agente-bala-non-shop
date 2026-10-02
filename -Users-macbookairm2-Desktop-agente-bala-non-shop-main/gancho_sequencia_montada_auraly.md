---
name: gancho-sequencia-montada-auraly
description: "[ANGULO 3 AURALY SOMENTE] Os cortes do gancho vao DENTRO do prompt de video, no mesmo clipe, gerados pelo Veo. Nao sao varios clipes: continua 1 K + 1 V. O bloco 'o que acontece no video' carrega acao ja comecada > corte para macro das maos no payoff > corte de volta, e o T1 nasce MUDO. Medido em 54 virais em 2026-09-20 e corrigido pelo Luigi na mesma data."
metadata: 
  node_type: memory
  type: feedback
  created: 2026-09-20T00:00:00.000Z
  modified: 2026-09-21T01:47:03.185Z
  originSessionId: ec5689bb-000a-402a-9a9d-15c449b3993c
---

**Vale so no Angulo 3 (Auraly).** FityWell (2 e 4) e Korella (1) nao mudam.

Analise medida de 54 virais do nicho (`maya.astor` e afins) em 2026-09-20, com `ffmpeg`.
Relatorio: `producao/analise_ganchos_maya_claude_2026_09_20/ANALISE_MEDIDA_GANCHOS.md`.

## A correcao que define a regra

♻️ **A primeira versao desta memoria estava errada** e mandava fatiar o T1 em 4 a 6 `K__`/`V__`
curtos. O Luigi corrigiu no mesmo dia: **nao sao varios clipes.** E **UM clipe so**, com as mudancas
de plano **escritas dentro do prompt de video** e geradas pelo Veo no mesmo take.

**Continua `1 K + 1 V`. Nao existe excecao ao `UMA IMAGEM = UM VIDEO`.**
O `K__` do gancho e o **primeiro plano** da sequencia; o resto nasce dentro do `V__`.
**Custo do gancho nao muda: 1 keyframe + 1 clipe por variacao.**

## As tres medicoes que sustentam a regra

**1. O gancho concentra as mudancas de plano.** Num viral de 110s, os cortes caem em
`0.93 · 1.57 · 2.13 · 4.13 · 6.00 · 6.07`, e ha **zero cortes nos 104 segundos seguintes**. Outro,
de 81s: sete mudancas em cinco segundos e zero nos 76 seguintes. Cerca de **1 corte por segundo**
dentro do clipe do gancho.

**2. Os tres primeiros segundos sao MUDOS.** Volume medio de -31 a -34 dB nos primeiros 3s contra
-17 dB no corpo, diferenca de 14 a 17 dB. Isso e room tone, nao fala baixa. A voz entra por volta de
3-4s. O scroll-stop e carregado 100% por imagem mais texto de tela.

**3. Os videos sao longos:** 57s a 135s, a maioria entre 80 e 110.

## Como escrever o `V__` do gancho

- O bloco **`o que acontece no video`** carrega a sequencia, nesta ordem fixa:
  **acao ja comecada** → **corte para MACRO das maos exatamente no instante do payoff** →
  **corte de volta para o plano de corpo**.
  O macro nunca e decorativo: entrega recompensa tatil sem entregar explicacao.
  ⚠️ Excecao consciente ao *"menos e mais na descricao da acao"* de [[restricoes-protocolo]] e do
  P6. Vale **so no take do gancho**; do T2 em diante a acao volta a ser enxuta.
- O bloco **`camera`** declara **cortes internos ao clipe**, em vez de `fixa / push-in`.
- **T1 mudo:** marcar `T1 · B-ROLL · MUDO` no `ROTEIRO.md` e abrir o `V__` com
  `(sem fala no take: ...)`. A fala vira voz-over no T2 ou e cortada. O `checar_entrega.py` ja
  aceita (`:78`, `:138`, `:254`), entao nao ha conflito tecnico.
- **Split vertical liberado so no T1** (rosto em cima, ritual embaixo), descrito dentro do `V__`.
  Do T2 em diante o plano unico de [[checklist-composicao-visual]] volta a ser obrigatorio.

**Por que:** repetir familia de gancho com um plano fixo de 8 segundos produz dez variacoes que
flopam juntas, so que organizadas. A gramatica de montagem dentro do clipe e o que separa o formato
deles do nosso, e ela custa zero keyframe a mais.

**Como aplicar:** ao montar as 10 variacoes por Puzzle de [[ganchos-variacao-puzzle]], cada hook ja
nasce com a sequencia de planos declarada, para entrar direto no `V__`. A sequencia de cortes
pertence a ACAO ESTRUTURAL preservada, entao ela e a mesma nas dez: o que muda e a variavel. Ver tambem
[[constrangimento-produtivo-auraly]] para o criterio de qual acao merece o gancho.
