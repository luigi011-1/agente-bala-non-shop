---
name: p1-checar-branches-nao-mesclados
description: "No P1 (este esqueleto ja foi produzido?), procurar tambem nos branches claude/* nao mesclados: em 2026-09-30 a producao auraly_growth_sal_tenis (mesma copy, mesmos 3 avatares) so existia no branch claude/ola-d0d6f0 e a main nao mostrava nada"
metadata:
  node_type: memory
  type: project
  originSessionId: 2442f658-602c-4e33-8b76-d0032c7ebcd6
  modified: 2026-09-30T03:23:05.220Z
---

Em 2026-09-30 o Luigi mandou um modelo de sal no sapato para Darlene, Lorraine e Walt. A `main` e a
[[biblioteca-videos]] nao tinham nada parecido, mas a mesma copy ja tinha sido produzida para os mesmos
avatares em 2026-09-28 (`producao/auraly_growth_sal_tenis`), que vive so no branch `claude/ola-d0d6f0`,
nunca mesclado. So descobri na etapa de prompts. O Luigi decidiu seguir como teste A/B (orgânico x IA)
e gerar no contrato da main (Flow v16), sem mesclar.

**Why:** cada sessao roda num worktree novo a partir da `main`; o que outra sessao entregou e nao foi
mesclado fica invisivel para o P1 e para o `checar_frases.py`. O mesmo branch tem o Flow v17 (K em
JSON), o `ficha_frame.py` e as producoes Auraly de 28 e 29/09 (`auraly_growth_dinheiro`, `_prece`,
`_sal_tenis`, `auraly_venda_fortuna`).

**How to apply:** no P1, antes de declarar esqueleto novo, rodar
`git ls-tree -r --name-only <branch> producao | grep -i <termo>` nos branches `claude/*` (ou
`git log --all --oneline -- 'producao/*<termo>*'`). Achou, avisar o Luigi ANTES do roteiro. Enquanto o
branch nao for mesclado, lembrar que a `main` esta atras em contrato do Flow e ficha. Ver
[[feedback-prompt-imagem-json-no-flow]] e [[ficha-do-frame-placar]].
