# PRODUCTION STATE
Production: `brandon_seamoss_joelho`
Angle: 1, Natural Rems Sea Moss · Objective: SALE · Round: VALIDATION
Reference video: `input/reference_video.mp4`
Current stage: PRODUCTION_COMPLETE
Next action: Luigi gera a mídia no Flow com `ENTREGA_BRANDON.md`; quando mandar o K01 gerado, pontuar
F1 a F6 contra o frame do modelo; depois da postagem, rodar o P10.

## Decisões do Luigi (2026-10-02)
- Ângulo 1, Sea Moss, VENDA, avatar holistic.brandon ("vamos modelar esse video para venda de seamoss
  gummies para a holistic.brandon").
- Roteiro v1 aprovado com o gancho fiel ("roteiro aprovado, prossiga").

## Log
- 2026-10-02: `/watch` rodado: 77,3s, 8 cenas, cortes em 7,63 · 9,20 · 13,20 · 17,73 · 23,37 · 30,33 ·
  64,80 · 74,47s. Origem: pessoa real (orgânico). Frames por cena em `input/frames_modelo/`.
- 2026-10-02: P1: mesma moldura de gancho da `brandon_pes_peroxido` (Ângulo 2, growth, mesma conta),
  agora no joelho e em venda. Esqueleto do corpo (joelho, intestino, ebook) nunca rodou.
- 2026-10-02: roteiro v1 (14 takes; T2 e T3 CENA CURTA). Desvios: CTA da marca no lugar do ebook e do
  follow gate; T6 sem claim de tratamento.
- 2026-10-02: checar_frases.py: 1 trecho igual à `brandon_pes_peroxido` no T3 ("two cups of warm water
  and"), que é medida da receita copiada literal do modelo, não argumento; fica. Checklist de envio,
  bloco A (gancho fiel): 11/11 aprovados (N/A: A1, A2, A7, fiel ao modelo). Linter: só a FALHA
  esperada de PROMPTS_PRODUCAO.md (pacote ainda não escrito).
- 2026-10-02: roteiro aprovado. 14 frames do modelo (`input/frames_modelo/K01..K14_modelo.png`),
  FICHA_FRAMES.md (14 K, placar 14/14), gerar_pacote.py e montar_entrega.py (Flow v17) geraram
  PROMPTS_BRANDON.md, FLOW_BRANDON.md, PROMPTS_PRODUCAO.md e ENTREGA_BRANDON.md.
- 2026-10-02: linter 0 FALHAS (aviso esperado: todos os K GERAR DO ZERO, bloco do Flow autossuficiente).
  Checklist de envio 34/34 (N/A: A1, A2, A7, C4 a C7, E4). Fila: holistic.brandon DONE.
  PRODUCTION COMPLETE (entrega de prompts).
