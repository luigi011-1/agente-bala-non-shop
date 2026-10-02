# AVATAR QUEUE

Production: `fitywell_growth_salmao_agua`
Angle: 2, FityWell
Objective: GROWTH
Round: VALIDATION
Reference video: `input/reference_video.mp4` (Jake Miller Health, 30,0s, três testes de comida na
água: salmão na água quente, peixe na água fria, brócolis no vinagre)

Ordem preservada dos 2 anexos recebidos em 2026-09-30. Identidade conferida abrindo uma âncora por
vez contra cada anexo: o anexo 1 é o Eva Dall (mesma imagem da âncora canônica, em resolução menor) e
o anexo 2 é idêntico, byte a byte, à âncora da holistic.brandon de 2026-09-29 (trazida do branch
`claude/ola-d85b5d` para `producao/_ancoras/`). Fila é estado em disco.

| Ordem | Estado | Avatar | Âncora | Cenário (texto dos K) |
|---:|---|---|---|---|
| 1 | DONE | Eva Dall | `producao/_ancoras/eva_dall_ancora.jpeg` | cozinha branca com parede e bancada de mármore verde-escuro, janelões, bandeirinha na prateleira |
| 2 | DONE | holistic.brandon | `producao/_ancoras/holistic_brandon_ancora.jpg` | box de treino: parede de bloco branco, neon TRAIN PRAY REPEAT, bandeira na parede, mesa preta |

## Travas da produção

- Os dois são COACH do FityWell para mulheres 40+. Eva Dall é homem (apesar do nome), ~49;
  holistic.brandon é mulher, ~30. A fala não tem primeira pessoa sobre corpo nem idade vivida, então
  vale igual para os dois.
- Growth: roteiro clonado palavra por palavra. Sem ponte, álibi, quiz, app, keyword ou preço.
- Rodada de validação: um gancho só, o do modelo, igual para a fila inteira. Sem as 10 variações.
- Produto fora de quadro. Garrafas de água e de vinagre lisas, sem rótulo.
- Brandon: os testes acontecem na mesa preta do box dela (cenário-base da conta). A mesa não é
  cozinha, então o aquário, a tigela e a tábua ficam sobre ela; registrar que pede mais regeneração.

## Estado atual

- 2026-09-30: roteiro com o gancho fiel aprovado pelo Luigi. Pacotes dos dois avatares entregues na
  mesma rodada (`ENTREGA_EVA_DALL.md`, `ENTREGA_HOLISTIC_BRANDON.md`), Flow v17, K em JSON, ficha 5/5.
  Linter: 0 falhas. Nenhum PENDING nem ACTIVE: PRODUCTION COMPLETE (entrega de prompts). Geração,
  montagem e publicação são marcos seguintes, do Luigi.
