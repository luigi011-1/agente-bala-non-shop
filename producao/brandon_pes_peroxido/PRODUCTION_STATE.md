# PRODUCTION STATE
Production: `brandon_pes_peroxido`
Angle: 2, FityWell · Objective: GROWTH · Round: VALIDATION
Reference video: `input/reference_video.mp4`
Current stage: PRODUCTION_COMPLETE
Next action: Luigi gera a mídia no Flow com `ENTREGA_BRANDON.md`; quando mandar o K01 gerado, pontuar
F1 a F6 contra o frame do modelo; depois da postagem, rodar o P10.

## Decisões do Luigi (2026-09-29)
- Ângulo 2, FityWell, GROWTH, avatar holistic.brandon ("vamos modelar esse video pra growth para a holistic brandon").
- Roteiro v1 aprovado com o gancho fiel e a troca WD-40 → água oxigenada ("roteiro aprovado, prossiga").

## Log
- 2026-09-29: `/watch` rodado; cortes medidos com limiar mais baixo: 5,80 · flash 9,63 a 9,83 ·
  17,73 · dissolve ~20,4 · 25,57 · 38,17 · 41,27s. Origem: avatar IA.
- 2026-09-29: P1: o esqueleto é o do caso 15 da biblioteca (escalda-pés com peróxido, `melody_pes`,
  Ângulo 1, outra conta). Nesta versão o modelo trocou o peróxido por WD-40. Nunca rodou na conta
  `brandon`.
- 2026-09-29: roteiro v1 (9 takes; T1, T4 e T8 CENA CURTA) com a troca obrigatória WD-40 → água
  oxigenada, por segurança e marca.
- 2026-09-29: checar_frases.py: nada repetido dos 5 roteiros da conta brandon. Checklist de envio, bloco A (gancho fiel): 11/11 aprovados (N/A: A1, A2, A7, fiel ao modelo). Linter: só a FALHA esperada de PROMPTS_PRODUCAO.md.
- 2026-09-29: roteiro aprovado. 9 frames do modelo, FICHA_FRAMES.md (9 K, placar 14/14), gerar_pacote.py e
  montar_entrega.py (Flow v17 do branch claude/ola-d0d6f0) geraram o pacote e ENTREGA_BRANDON.md.
- 2026-09-29: linter do claude/ola-d0d6f0: 7 FALHAS de "bottle" lido como produto; o borrifador virou
  "trigger sprayer" no texto (mesmo objeto) e o linter fechou com 0 FALHAS. Linter local: 0 FALHAS.
- 2026-09-29: checklist de envio 34/34 (N/A: A1, A2, A7, C3 a C7). Fila: holistic.brandon DONE.
  PRODUCTION COMPLETE (entrega de prompts).
