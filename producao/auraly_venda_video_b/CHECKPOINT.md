# PRODUCTION CHECKPOINT

Production: auraly_venda_video_b
Angle: 3 (Auraly)
Objective: SALE
Round: VALIDATION
Reference video: input/modelo.mp4 (videoB_snapinsta-1791508253073.mp4, 119,8s, espanhol)
Scenario: sala aconchegante com teto claro de vigas, guirlanda de estrelas douradas e fitas, trepadeira artificial à esquerda, persiana branca com luz de dia à direita; câmera fixa na altura da mesa; tábua de madeira com sal grosso, louro e canela na base do quadro. Jordan: sala de jantar de mansão com mesa de mármore.

Current stage: PRODUCTION_COMPLETE
Current avatar: NONE
Next action: aguardar a geração no Flow pelo Luigi (4 imagens por K, escolher 1, depois 1 vídeo por V)

## Avatar queue
[DONE] Avery Knox (inglês): producao/_ancoras/character_sheets/avery_knox_character_sheet.jpg
[DONE] Devon Price (inglês): producao/_ancoras/character_sheets/devon_price_character_sheet.jpg
[DONE] Jordan Vale (ESPANHOL): producao/_ancoras/character_sheets/jordan_vale_character_sheet.jpg

## Approved script
status: APPROVED (Luigi, 2026-10-09: "manda o pack de todos os avatares")
file: ROTEIRO.md

## Selected hooks
status: APPROVED (hook fiel aprovado junto com o roteiro, 2026-10-09)
hooks: HOOK 1 - FIEL - O fogo entre as mãos
formato: fiel-validacao
acao estrutural: derramar uísque sobre sal, louro e canela numa tábua, acender, chama entre as mãos em oração, T1 mudo com cortes internos
eixos de troca: n/a (validacao)

## Current avatar assets
image prompts: ENTREGA_<AVATAR>.md (K01, K02)
video prompts: ENTREGA_<AVATAR>.md (V01 a V14)

## Completed
- Intake: video + 3 character sheets (Avery, Devon, Jordan)
- ANALYSIS: /watch (transcrição em espanhol refeita com Whisper small, língua es)
- SCRIPT_MODELLING: ROTEIRO.md (checklist de copy de venda, checar_frases OK) + GANCHOS_VISUAIS.md
- Rota alinhada com o coordenador (Zadkiel, Lid Seal, Wanda, panela sem tampa)
- FICHA_FRAMES.md (K01 e K02, placar 14/14), gerar_pacote.py, AGENTE_FLOW.md
- Pacotes dos três avatares (MAPA K/V, K01, K02, V01 a V14), checar_entrega --estrito 0 falhas; T14 ajustado só no CTA do Stories para passar o linter e o checar_frases

## Pending
- Geração no Flow, montagem e postagem (marcos do Luigi)

## User decisions
- Decision: Jordan Vale em espanhol latino neutro; Avery e Devon em inglês
  Reason: Luigi, 2026-10-09 (teste de idioma na conta do Jordan)
  Operational consequence: todo V do Jordan declara que ele fala espanhol e leva a fala em espanhol; tabela de aprovação do Jordan em Español | Português

## Next response format
- Aguardar o Luigi
