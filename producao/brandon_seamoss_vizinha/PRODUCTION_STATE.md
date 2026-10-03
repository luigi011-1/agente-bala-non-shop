# PRODUCTION STATE
Production: `brandon_seamoss_vizinha`
Angle: 1, Natural Rems Sea Moss · Objective: SALE · Round: VALIDATION
Reference video: `input/reference_video.mp4`
Current stage: WAITING_SCRIPT_APPROVAL
Next action: Luigi aprova ou ajusta o roteiro v1 (gancho fiel = a esquete). Depois da aprovação:
P5 (gabarito, GATE_VISUAL 1 a 3), `FICHA_FRAMES.md` com os 32 frames de `input/frames_modelo/`,
REF-P1 a REF-P3 da esquete, pacote (`PROMPTS_PRODUCAO.md` + entrega do Flow), checklist de envio,
linter com 0 FALHAS e as duas transcrições no fim.

## Decisões do Luigi (2026-10-03)
- Ângulo 1, Natural Rems Sea Moss Gummies, VENDA, avatar holistic.brandon (imagem da âncora na mensagem).
- Link do CTA **na legenda** do post ("mandando para o link da legenda"; reconfirmado: "seguindo o que
  eu disse na mensagem anterior"). Registrado na memória `angulo1-copy-seamoss` e aceito no linter.

## Log
- 2026-10-03: vídeo enviado por upload na sessão da nuvem; `/watch` rodado (small.en, 20 cenas no
  limiar padrão, cortes finos com limiar 0,06). Origem: avatar IA. Falantes da esquete conferidos por
  tom de voz (o "literally everything" é a vizinha em off sobre o close do marido).
- 2026-10-03: P1: esqueleto novo na biblioteca (movie style família B + listicle de 3 receitas + produto
  Amazon); nunca rodou na conta `brandon`.
- 2026-10-03: roteiro v1 (32 takes; esquete T1 a T15 no tempo do modelo, 10 CENA CURTA e 3 B-ROLL;
  Brandon T16 a T32). Trocas obrigatórias: indicação "holistic coach", credencial de coach no lugar de
  "91 years... without doctors", nº 3 vira sea moss pelo estresse, prova social sem prazo, CTA da marca
  com link na legenda, Facebook e follow gate cortados. `checar_frases.py`: nada repetido da conta.
  Linter: 0 falhas de copy (a única FALHA é o `PROMPTS_PRODUCAO.md`, que só nasce depois da aprovação).
