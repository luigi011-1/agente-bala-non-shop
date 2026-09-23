---
name: pipeline-auraly-separacao
description: "Como o pipeline Auraly (ângulo 3) se separa do pipeline clássico — marcador, pastas, linter, arquivos"
metadata: 
  node_type: memory
  type: project
  originSessionId: e9b9af55-d673-475e-a98e-38d63c1361b0
  modified: 2026-09-07T03:58:59.987Z
---

Implementado em 2026-09-07. O pipeline Auraly é o novo fluxo para o ângulo 3 (app de manifestação de alma gêmea), separado do clássico que atende ângulos 1, 2 e 4.

**Marcador de pipeline:** Todo `ROTEIRO.md` de produção Auraly começa com `pipeline: auraly` (primeira linha, sem indentação). Sem ele o linter roda o ramo clássico e reprova por arquivos ausentes.

**Pasta:** `producao/<slug>/` sem prefixo de avatar. Clássico usa `producao/<avatar>_<slug>/`.

**Arquivos obrigatórios Auraly:** `ROTEIRO.md` + `GANCHOS_VISUAIS.md`. Sem `PROMPTS_PRODUCAO.md`, sem `DM.md`.

**Prompts de vídeo:** ficam em `<avatar>_<YYYY-MM-DD>/PROMPTS_VIDEO_FLOW.md`. Formato: `## V01A · T1 · K01 descricao`.

**Linter:** `checar_entrega.py` detecta o marcador e chama `checar_auraly()`. O ramo clássico `checar()` não foi alterado. `checar_auraly()` valida: travessão, keyword 222, contagem de palavras, seções do ROTEIRO híbrido, lei do selo, follow gate (sem motivo técnico revogado), funil invertido (Stories = destino), registro divino, 5 blocos nos prompts de vídeo, fala literal.

**Seções obrigatórias do ROTEIRO.md Auraly (híbrido):** marcador pipeline, tabela puzzle/esqueleto, `## Roteiro cena a cena` (com `### T1 · BEAT · TALKING · Setup A`), roteiro só-fala, notas de produção com compliance.

**AURALY_AGENT.md:** tem cabeçalho `ÂNGULO 3 SOMENTE` explícito. É o único dono do pipeline Auraly.

**CLAUDE.md /watch:** agora condicional — ângulo 3 vai para AURALY_AGENT.md, ângulos 1/2/4 seguem o fluxo clássico.

**Exemplos no disco:** `producao/barbie_the_aries/` é a referência de pipeline Auraly completo (pré-fronteira corrigida, zero falhas no linter). `producao/cody_1111/` é pré-fronteira, sem marcador, marcada como tal.

**Why:** separar os pipelines para que produzir vídeos dos ângulos 1/2/4 não conflite com o fluxo Auraly.

**How to apply:** ao receber `/watch` com ângulo 3, usar AURALY_AGENT.md. Ao receber qualquer outro ângulo, usar fluxo clássico. Antes de qualquer commit de produção Auraly, rodar `python checar_entrega.py producao/<slug>`.
