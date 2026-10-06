# PRODUCTION CHECKPOINT

Production: auraly_venda_dinheiro_v1
Angle: 3 (Auraly)
Objective: SALE
Source: ORGANIC
Round: VALIDATION
Reference video: producao/auraly_venda_dinheiro_v1/input/modelo.mp4 (snapinsta-1791302581803.mp4)
Scenario: cozinha do modelo, azulejo branco tipo metrô, prateleiras de madeira com plantas e livros, janela grande com cerca e jardim, bancada cinza clara, recipiente de vidro retangular no primeiro plano

Current stage: WAITING_SCRIPT_APPROVAL
Current avatar: Avery Knox
Next action: esperar o Luigi aprovar ou ajustar o roteiro e o hook fiel (ROTEIRO.md); depois colar INSTRUCOES_AGENTE_FLOW.md (versão com a regra nova: K só com character sheet, V só com a imagem escolhida) e entregar K+V do avatar ativo

## Avatar queue
[ACTIVE] Avery Knox (producao/_ancoras/character_sheets/avery_knox_character_sheet.jpg)
[PENDING] Devon Price (producao/_ancoras/character_sheets/devon_price_character_sheet.jpg)
[PENDING] Jordan Vale (producao/_ancoras/character_sheets/jordan_vale_character_sheet.jpg)

## Approved script
status: PENDING_APPROVAL
file: ROTEIRO.md

## Selected hooks
status: PENDING_APPROVAL (hook fiel junto com o roteiro)
hooks: HOOK 1 - FIEL - Álcool e canela no pote de vidro
formato: fiel-validacao
acao estrutural: avatar despeja um líquido e um pó num recipiente de vidro e mexe com o dedo, falando
eixos de troca: n/a (validacao)

## Current avatar assets
image prompts: pendente
video prompts: pendente

## Completed
- Intake: 2 vídeos modelo + 3 character sheets; este chat fica com o vídeo 1
- ANALYSIS: /watch em input/modelo_watch/; plano único de 110,8s, gancho falado desde 0s
- SCRIPT_MODELLING: ROTEIRO.md + GANCHOS_VISUAIS.md

## Pending
- Aprovação do roteiro; pacote K+V dos 3 avatares

## User decisions
- Decision: venda Auraly com oferta de dinheiro, prosperidade e fortuna, promessas e consequências agressivas se pular os selos
  Reason: Luigi, 2026-10-06
  Operational consequence: T10 e T14 novos no roteiro; tom agressivo sem mal real e sem valor em dólar garantido
- Decision: K só com character sheet + prompt (sem frame modelo); V só com a imagem escolhida + prompt; 4 variações por K, 1 por V, 9:16
  Reason: Luigi, 2026-10-06
  Operational consequence: cenário, pose e ação do modelo vão por escrito em cada K

## Next response format
- Roteiro bilíngue completo e parar em WAITING_SCRIPT_APPROVAL
