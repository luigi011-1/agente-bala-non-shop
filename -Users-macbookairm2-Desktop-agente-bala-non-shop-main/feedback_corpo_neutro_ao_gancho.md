---
name: feedback-corpo-neutro-ao-gancho
description: "Quando N ganchos compartilham UM corpo, nenhum keyframe de corpo pode citar o prop que muda entre os ganchos. Se citar, o corpo só casa com um gancho e os outros viram entrega quebrada."
metadata:
  node_type: memory
  type: feedback
  originSessionId: current
  modified: 2026-09-22T15:51:10.751Z
---

# O corpo tem que ser NEUTRO ao gancho

Erro meu, pego pelo Luigi em 2026-09-22 na produção `fitywell_growth_cortisol_props`.
Palavras dele: *"nos prompts de imagem que você mandou do primeiro avatar foi feito só pra um gancho
e um corpo e no caso eu escolhi mais ganchos para o mesmo corpo e isso você simplesmente ignorou"*.

**O que eu fiz de errado:** ele escolheu quatro ganchos (H1, H2, H7, H10) para o mesmo corpo. Eu
gerei os quatro keyframes de gancho certinhos, mas escrevi nos keyframes de CORPO (K05 e K06) a
frase `The leg forms with red heels...`. O salto era exatamente o prop que mudava a cada gancho
(vermelho, fita, sapatilha nude, dourado). Resultado: o corpo só casava com o H1. Nos outros três, o
vídeo abriria com um calçado e continuaria com outro. Entreguei **um gancho utilizável, não quatro**,
e ainda declarei a entrega completa porque o linter passou (ele não checa continuidade entre takes).

## A regra

**Antes de escrever qualquer keyframe de corpo, listar o que muda entre os ganchos escolhidos. Nada
dessa lista pode aparecer no quadro do corpo.** O `CLAUDE.md` já dizia *"cada variação custa 1
keyframe + 1 clipe, porque só o T1 muda"*. Para isso ser verdade, o corpo precisa ser literalmente
reutilizável, e ele não é se carregar estado do gancho.

**Why:** o custo do método Puzzle depende de um corpo compartilhado. Corpo contaminado força uma de
duas saídas ruins: ou N corpos (o custo de imagem explode, 4 ganchos viram 12 keyframes por avatar
em vez de 6), ou vídeos com quebra visual no meio.

**How to apply:**
1. Listar o prop variável de cada gancho.
2. Enquadrar o corpo de forma que esse prop fique FORA de quadro (no caso das pernas: enquadrar a
   partir da altura do peito, prop abaixo da borda inferior). Reduzir por enquadramento, nunca por
   blur, que o negative proíbe.
3. Escrever no `negative` do corpo que o prop variável não entra em quadro.
4. Deixar em quadro só o que é idêntico nos N ganchos.
5. Registrar o desvio na análise quando o vídeo modelo mantinha o prop em quadro o tempo todo: lá
   existia um gancho só, aqui existem N.

**Gate mental antes de fechar:** *"se eu montar o gancho 3 com este corpo, alguma coisa muda de
aparência no meio do vídeo?"*. Se muda, o corpo está contaminado.

Relacionado: [[ganchos-variacao-puzzle]], [[feedback-prompt-imagem-compartilhado]],
[[checklist-composicao-visual]], [[workflow-entrega-gabarito]]
