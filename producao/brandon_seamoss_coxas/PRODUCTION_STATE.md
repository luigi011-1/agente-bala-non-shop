# PRODUCTION STATE
Production: `brandon_seamoss_coxas`
Angle: 1, Natural Rems Sea Moss · Objective: SALE · Round: VALIDATION
Reference video: `input/reference_video.mp4`
Current stage: WAITING_SCRIPT_APPROVAL
Next action: Luigi aprova ou ajusta o roteiro v1 com o gancho fiel. Aprovado, extrair um frame do
modelo por take, escrever FICHA_FRAMES.md e o pacote (gerador no molde de `brandon_seamoss_joelho`).

## Decisões do Luigi (2026-10-02)
- Ângulo 1, Sea Moss, VENDA, holistic.brandon.
- CTA novo do Sea Moss: link na LEGENDA do post (o do comentário fixado não fica clicável).

## Log
- 2026-10-02: `/watch` rodado: 36,7s, cortes em 4,67 · 6,21 · 10,21 · 14,00 · 21,79 · 28,75s (limiar
  0,03), push-in dentro do plano entre ~15,6 e ~17,6s. Origem: avatar IA ("Synthetic performer"),
  fala em espanhol, retranscrita com o modelo multilíngue (`watch/audio/transcript_es.txt`).
- 2026-10-02: P1: esqueleto novo na biblioteca (coxa escura + pasta de bicarbonato, limão e óleo de coco).
- 2026-10-02: roteiro v1 (9 takes; T1, T2 e T4 CENA CURTA). Desvios: T2 sem antes e depois, T6 sem
  resultado garantido, cenário sem clínica, elenco solo, CTA da marca com link da legenda.
- 2026-10-02: checar_frases.py: 1 trecho igual à `brandon_maca_alho` no T3 ("the juice of half a
  lemon"), medida da receita, não argumento; fica. Checklist de envio, bloco A (gancho fiel): 11/11
  aprovados (N/A: A1, A2, A7, fiel ao modelo). Linter: só a FALHA esperada de PROMPTS_PRODUCAO.md.
- 2026-10-02: roteiro v2 (pedido do Luigi: explicar depois do T7 o mecanismo, a inflamação como causa
  real e o escurecimento como consequência). Entram T8 (causa e consequência) e T9 (a saída); o produto
  vira T10 e o CTA vira T11. 11 takes, ~68s.
