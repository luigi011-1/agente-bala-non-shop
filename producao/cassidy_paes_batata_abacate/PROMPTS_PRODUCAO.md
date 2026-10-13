# PROMPTS | Sea Moss Growth · pãezinhos de batata com abacate

flow_seguro: v1

Vídeo modelo: `input/modelo.mp4`. Âncora: `producao/_ancoras/cassidy_hargrove_ancora.jpg` (no Flow: `cassidy hargrove .jpg`). Funil: growth.

Os blocos copiáveis (K em parágrafo, V só com a fala) estão em `ENTREGA_CASSIDY.md`. Este arquivo guarda o índice e as regras.

## Índice de geração

| Take | Keyframe | Ação de geração |
|---|---|---|
| T1 | K01 | gerar K + V01 |
| T2 | K02 | gerar K + V02 |
| T3 | K03 | gerar K + V03 |
| T4 | K04 | gerar K + V04 |
| T5 | K04 | reaproveita a imagem do K + V05 |

## Trava de identidade e continuidade

Todo K abre com a mesma descrição da avatar e do cais na frente do galpão de cedro (avatar fixo da conta) e anexa só a imagem dela. Mesmo suéter creme, mesmo macacão amarelo, mesma trança ruiva, mesmo galpão, alga secando e bandeira em todo K.

## Bloco global de vídeo

Todo V: `The person in the image speaks in American English, looking at the camera: "<fala literal>"` + `Fixed camera. Natural lip sync, no music.` Padrão único do Flow (AGENTS.md, 2026-10-09): sem cena, roupa, objeto nem tom de voz no V.

## Mapa de âncoras

| Keyframe | Referências a anexar | Modelo |
|---|---|---|
| K01 | só `cassidy hargrove .jpg` | Nano Banana 2.1, 4 variações, 9:16 |
| K02 | só `cassidy hargrove .jpg` | Nano Banana 2.1, 4 variações, 9:16 |
| K03 | só `cassidy hargrove .jpg` | Nano Banana 2.1, 4 variações, 9:16 |
| K04 | só `cassidy hargrove .jpg` | Nano Banana 2.1, 4 variações, 9:16 |

## Montagem no CapCut

Edição automática (`editar.py`, acabamento HyperFrames): legenda palavra por palavra, cortes de pausa, música a -18 dB da voz. Salvar os vídeos como V01 a V05. Sem Voice Changer. Legenda do post: `#ad #syntheticperformer #naturalrems` no topo, sem link; chave de conteúdo de IA ligada.

## Gates de qualidade

1. `python3 checar_entrega.py` e `python3 flow_seguro.py` sem falha.
2. Ficha dos frames escrita antes dos K (`FICHA_FRAMES.md`).
3. Checklist de envio rodado e informado fora dos blocos.
4. Na edição: fala de cada take conferida palavra por palavra com o roteiro.
