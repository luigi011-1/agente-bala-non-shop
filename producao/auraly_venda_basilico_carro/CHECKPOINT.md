# PRODUCTION CHECKPOINT

Production: auraly_venda_basilico_carro
Angle: 3 (Auraly)
Objective: SALE
Source: ORGANIC
Round: VALIDATION
Reference video: video1_modelo.mp4 (86,6s, homem agachado ao lado da porta traseira aberta de um SUV, pote de vidro nas mãos, folhas secas sob o tapete do carro)
Scenario: entrada de garagem de bairro residencial americano em dia de sol, SUV escuro com a porta traseira aberta (bancos de couro preto, tapete de borracha), chão de concreto claro, casas e árvores ao fundo, céu azul

Scenario (Jordan, regra de luxo de Luigi 2026-10-07): mesma ação do modelo, porta traseira aberta de um Bentley Bentayga preto (carro de luxo) em frente ao portão de uma mansão, piso de pedra clara, jardim aparado e fachada de pedra ao fundo, céu azul

Current stage: PRODUCTION_COMPLETE
Current avatar: NONE
Next action: aguardar o Luigi gerar as imagens (4 por K, 1 escolhida) e os vídeos no Flow; quando ele disser que o vídeo performou, abrir a rodada de variação

## Avatar queue
[DONE] Jordan Vale
[DONE] Avery Knox
[DONE] Devon Price (producao/auraly_avatares_rico_careca/AVATARES_RICO_CARECA.md; cenário do modelo como a Avery)

## Approved script
status: APPROVED (Luigi, 2026-10-07)
file: ROTEIRO.md

## Selected hooks
status: APPROVED (hook fiel aprovado junto com o roteiro, 2026-10-07)
hooks: HOOK 1 - FIEL - Manjericão seco sob o tapete do carro
formato: fiel-validacao
acao estrutural: avatar despeja ervas secas de um pote de vidro sob um tapete de carro, depois fala agachado para a lente
eixos de troca: n/a (validacao)

## Completed
- Intake: 1 vídeo modelo + 3 avatares
- ANALYSIS: transcrição (Whisper) e frames; plano único com inserto de abertura
- SCRIPT_MODELLING: ROTEIRO.md + GANCHOS_VISUAIS.md, aprovados 2026-10-07
- IMAGE_PROMPTS + VIDEO_PROMPTS: Jordan e Avery (gerar_pacote.py)

## Current avatar assets
image prompts: FLOW_<AVATAR>.md dos 3 avatares (K01, K02)
video prompts: FLOW_<AVATAR>.md dos 3 avatares (V01 a V10)

## Pending
- Luigi gerar K e V no Flow com AGENTE_FLOW.md

## User decisions
- Decision: Avery Knox fica exatamente como está; ricaço = Jordan Vale
  Reason: Luigi, 2026-10-07
  Operational consequence: mesma copy para os dois, só identidade muda
- Decision: cenário do Jordan sempre de luxo máximo (dentro de casa = mansão; carro = carro de luxo ou esportivo; ar livre = viagem em lugar famoso: Torre Eiffel, Burj Khalifa, Marrocos etc.)
  Reason: Luigi, 2026-10-07 (regra permanente para o Jordan)
  Operational consequence: o scene dos K do Jordan troca o cenário do modelo pelo equivalente de luxo, mesma ação e câmera; Avery fica com o cenário do modelo
