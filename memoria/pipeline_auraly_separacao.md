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

**Arquivos obrigatórios Auraly:** `ROTEIRO.md` + `GANCHOS_VISUAIS.md`. Sem `PROMPTS_PRODUCAO.md`, sem `DM.md` (e sem automação de DM desde 2026-09-22).

**Prompts de vídeo:** ficam em `<avatar>_<YYYY-MM-DD>/`, no formato do OUTPUT CONTRACT de `WORKFLOW_AURALY.md` (`K__`/`V__` sozinhos na linha).

**Linter:** `checar_entrega.py` detecta o marcador e chama `checar_auraly()`. O ramo clássico `checar()` não foi alterado. `checar_auraly()` valida: travessão, keyword 222, contagem de palavras, seções do ROTEIRO híbrido, lei do selo, follow gate (sem motivo técnico revogado), funil invertido (Stories = destino), registro divino, 5 blocos nos prompts de vídeo, fala literal.

**Seções obrigatórias do ROTEIRO.md Auraly (híbrido):** marcador pipeline, tabela puzzle/esqueleto, `## Roteiro cena a cena` (com `### T1 · BEAT · TALKING · Setup A`), roteiro só-fala, notas de produção com compliance.

**Dono do processo (desde 2026-09-14):** `AGENTS.md` → `WORKFLOW_AURALY.md` → `CHECKPOINT.md` da produção. O `AURALY_AGENT.md` e o Auraly Studio foram arquivados em 2026-09-22 (`_arquivo/2026-09-22_limpeza_angulo3/ferramentas/`).

**Exemplos no disco:** nenhum pacote Auraly ativo depois da limpeza de 2026-09-22; os antigos estão em `_arquivo/2026-09-22_limpeza_angulo3/producao/` e não são gabarito.

**Why:** separar os pipelines para que produzir vídeos dos ângulos 1/2/4 não conflite com o fluxo Auraly.

**How to apply:** ao receber `/watch` com ângulo 3, seguir `WORKFLOW_AURALY.md`. Ao receber qualquer outro ângulo, usar fluxo clássico. Antes de qualquer commit de produção Auraly, rodar `python checar_entrega.py producao/<slug>`.

Relacionadas: [[feedback-entrega-avatar-completo-auraly]], [[feedback-entrega-multi-avatar-sob-demanda]], [[feedback-video-prompts-sem-esperar-imagem]].
