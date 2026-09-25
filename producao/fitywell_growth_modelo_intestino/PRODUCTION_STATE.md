# PRODUCTION STATE
Production: `fitywell_growth_modelo_intestino`
Angle: 2, FityWell · Objective: GROWTH · Origin: IA · Round: VALIDATION
Reference video: `input/reference_video.mp4`
Current stage: WAITING_LUIGI_REQUEST
Next action: Luigi pede o pacote corrigido (ficha aplicada). Colar o avatar pedido; Eva Dall segue ACTIVE,
avançar o próximo PENDING e entregar o `ENTREGA_<AVATAR>.md` dele.

## Decisões do Luigi (2026-09-25)
- Ângulo 2, FityWell, objetivo GROWTH (declarados na mensagem de intake).
- Fila: os 5 avatares anexados, na ordem recebida.
- Roteiro v1 aprovado ("roteiro aprovado, prossiga"), com o corte do bloco do produto da Amazon.

## Log
- 2026-09-25: intake. 5 âncoras idênticas (md5) às já conferidas em `fitywell_growth_froyo_bites`.
- 2026-09-25: `/watch` rodado (53,7s, 22 cortes, 25 segmentos). Origem: avatar IA. Gancho: modelo
  transparente de intestino cheio de massa marrom; reveal da bebida limpando aos 9,6s.
- 2026-09-25: roteiro v1 com 13 takes, um por cena. Bloco do produto da Amazon (34,8 a 51,4s)
  cortado, `T` vira `yes`.
- 2026-09-25: roteiro aprovado. `gerar_pacote.py` (base froyo, K em JSON pelo Flow v17) gerou 5 pacotes,
  13 K + 13 V cada. Linter barrou `bottle` no K07 (frasco lê como produto): virou galheteiro de cozinha
  sem rótulo. Banco verbal ganhou a frase do texto de tela. Linter 0 FALHAS nos 5. Eva Dall ACTIVE.
- 2026-09-25: Luigi reprovou o K01 gerado (tubo em zigue-zague a meia distância, bancada com props). Causa: forma
  do herói genericizada, câmera no peito, props inventados. Corrigido: forma anatômica inteira, câmera rente à
  bancada 0,5x com lente a centímetros, bancada vazia, e reforço de proximidade do herói em todos os K. V01/V02
  ajustados. 5 pacotes regenerados, linter 0 FALHAS. Memória: Falha #8 em erros_recorrentes.
- 2026-09-25: processo novo da FICHA DO FRAME (GATE_VISUAL.md Parte 6). `FICHA_FRAMES.md` escrita olhando os 13
  frames do modelo; K das panelas com avatar agachado e câmera na altura da borda, copos com 1/3 do quadro,
  lista fechada em todo K. Linter com `ficha_frame.py`: 13 K, placar 14/14, evidência nos 6 arquivos, 0 FALHAS.
  Os pacotes corrigidos NÃO foram colados no chat (Luigi: só quando pedir).
