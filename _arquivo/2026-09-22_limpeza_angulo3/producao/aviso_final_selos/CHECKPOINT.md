# PRODUCTION CHECKPOINT

Production: aviso_final_selos
Angle: 3 - Auraly
Objective: GROWTH
Reference video: producao/aviso_final_selos/VIDEO_MODELO.mp4 (101s, 720x1280)

Current stage: AVATAR_TRANSITION
Current avatar: 05_terno_creme_relogio_arco_iris
Next action: entregar os cinco cenarios do avatar 05.

## Avatar queue

Seis avatares enviados pelo Luigi em 2026-09-20, nesta ordem, na mesma mensagem do video modelo.
Os identificadores sao descritivos e provisorios: o Luigi nao enviou nomes. Nenhum nome do roster
historico foi atribuido, de proposito, para nao repetir o erro de 2026-09-14.

[DONE] 01_careca_barba_branca_polo
[DONE] 02_cabelo_prateado_camisa_azul
[DONE] 03_dreads_loiros_longos_jeans
[DONE] 04_dreads_loiros_medios_verde
[ACTIVE] 05_terno_creme_relogio_arco_iris
[PENDING] 06_terno_preto_barba_grisalha

| # | id provisorio | caminho da fingerprint | status |
|---|---|---|---|
| 1 | 01_careca_barba_branca_polo | producao/aviso_final_selos/fingerprints/01_careca_barba_branca_polo.jpg | DONE |
| 2 | 02_cabelo_prateado_camisa_azul | producao/aviso_final_selos/fingerprints/02_cabelo_prateado_camisa_azul.jpg | DONE |
| 3 | 03_dreads_loiros_longos_jeans | producao/aviso_final_selos/fingerprints/03_dreads_loiros_longos_jeans.jpg | DONE |
| 4 | 04_dreads_loiros_medios_verde | producao/aviso_final_selos/fingerprints/04_dreads_loiros_medios_verde.jpg | DONE |
| 5 | 05_terno_creme_relogio_arco_iris | producao/aviso_final_selos/fingerprints/05_terno_creme_relogio_arco_iris.jpg | ACTIVE |
| 6 | 06_terno_preto_barba_grisalha | producao/aviso_final_selos/fingerprints/06_terno_preto_barba_grisalha.jpg | PENDING |

## Approved script
status: APPROVED
growth-stories: aprovado
file: ROTEIRO.md

## Selected hooks
status: LOCKED
hooks: 1, 5, 6, 8, 2
formato: puzzle-10
acao estrutural: segura UM OBJETO, mergulha dentro de UM POTE DE SUBSTANCIA ESPESSA e levanta o
  objeto escorrendo por cima de UMA PANELA FERVENDO, e continua segurando ate o fim
eixos de troca: OBJETO, SUBSTANCIA, COR, LOCAL, RESULTADO, MARCADOR
cenarios: 1 carta/vaselina · 2 mel · 3 cera vermelha · 4 banheiro · 5 alianca

## Current avatar assets
cenario 1: 01_careca_barba_branca_polo/CENARIO_1_carta_vaselina.md (K01, K02, V01 a V14) ENTREGUE
cenarios 2 a 5: CENARIO_2_mel, CENARIO_3_cera_vermelha, CENARIO_4_banheiro, CENARIO_5_alianca ENTREGUES
avatar 01: DONE, 10 K e 70 V no total
avatar 02: DONE, 5 cenarios em 02_cabelo_prateado_camisa_azul/, 10 K e 70 V, gerado por gerar_avatar.py
avatar 03: DONE, 5 cenarios em 03_dreads_loiros_longos_jeans/, 10 K e 70 V
avatar 04: DONE, 5 cenarios em 04_dreads_loiros_medios_verde/, 10 K e 70 V

## Completed
- Video modelo analisado por medicao: cortes, volume por janela e leitura das legendas karaoke.
- Transcricao integral reconstruida a partir das legendas queimadas no video.
- Classificado como CRESCIMENTO, confirmado pelo Luigi no intake.
- Producao criada, fingerprints e video modelo copiados para dentro da pasta.
- Roteiro modelado escrito, entregue e APROVADO pelo Luigi.
- 10 ganchos por Puzzle entregues; Luigi escolheu 1, 5, 6, 8 e 2.
- Executor do Flow sincronizado para v11: o 4/3/3 saiu, entrou o Puzzle e a regra do T1 mudo.
- Avatar 01 completo: cinco cenarios, 10 K e 70 V, 0 falhas no checar_entrega.py.

## Pending
- Os cinco cenarios de cada um dos avatares 05 e 06.
- Nomes reais dos seis avatares, para substituir os identificadores provisorios.
- Confirmar se o numero do comentario no modelo e `222`, ver ANALISE_MODELO.md secao 5.

## User decisions
- Decision: produzir com os seis avatares anexados na mensagem, e somente eles.
  Reason: Luigi em 2026-09-20, "use somente os avatares que eu te enviar na respectiva producao".
  Operational consequence: nao puxar avatar do roster historico, nao sugerir troca.
- Decision: roteiro aprovado pelo Luigi em 2026-09-20, sem ajuste.
  Reason: "roteiro aprovado".
  Operational consequence: copy, takes e falas travados para a fila inteira de seis avatares.
- Decision: manter o CTA de Stories mesmo sendo GROWTH (growth-stories: aprovado).
  Reason: o CTA de Stories vem do PROPRIO video modelo, e video de crescimento clona o CTA do
  original. Nao e funil acrescentado. Aprovado junto com o roteiro.
  Operational consequence: o gate de objetivo do checar_entrega.py aceita o Stories nesta producao.
- Decision: objetivo GROWTH.
  Reason: declarado por escrito no intake.
  Operational consequence: roteiro clona o modelo quase palavra por palavra, sem bloco de venda,
  sem ponte, sem alibi e sem keyword de conversao. O CTA e o do proprio original.

## Next response format
- Pacote dos cinco cenarios do avatar 05, no formato de entrega completa.
