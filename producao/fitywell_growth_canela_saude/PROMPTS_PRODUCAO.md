# PROMPTS | FitWell Growth · canela e o aviso

flow_seguro: v1

Vídeo modelo: `input/modelo.mp4`. Âncora: `producao/_ancoras/holistic_brandon_ancora.jpg` (no Flow: `holistic brandon.jpg`). Funil: growth.

Os blocos copiáveis (K em parágrafo, V só com a fala) estão em `ENTREGA_AVATAR_FITWELL.md`. Este arquivo guarda o índice e as regras.

## Índice de geração

| Take | Keyframe | Ação de geração |
|---|---|---|
| T1 | K01 | gerar K + V01 |
| T2 | K02 | gerar K + V02 |
| T3 | K02 | reaproveita a imagem do K + V03 |
| T4 | K02 | reaproveita a imagem do K + V04 |
| T5 | K02 | reaproveita a imagem do K + V05 |
| T6 | K02 | reaproveita a imagem do K + V06 |
| T7 | K02 | reaproveita a imagem do K + V07 |
| T8 | K02 | reaproveita a imagem do K + V08 |
| T9 | K02 | reaproveita a imagem do K + V09 |
| T10 | K02 | reaproveita a imagem do K + V10 |
| T11 | K02 | reaproveita a imagem do K + V11 |
| T12 | K02 | reaproveita a imagem do K + V12 |
| T13 | K02 | reaproveita a imagem do K + V13 |
| T14 | K02 | reaproveita a imagem do K + V14 |

## Trava de identidade e continuidade

Todo K abre com a mesma descrição da avatar e do box de treino (avatar fixo da conta) e anexa só a imagem dela. Mesma roupa, mesma corrente com cruz de ouro, mesmo neon e bandeira em todo K.

## Bloco global de vídeo

Todo V: `The person in the image speaks in American English, looking at the camera: "<fala literal>"` + `Fixed camera. Natural lip sync, no music.` Padrão único do Flow (AGENTS.md, 2026-10-09): sem cena, roupa, objeto nem tom de voz no V.

## Mapa de âncoras

| Keyframe | Referências a anexar | Modelo |
|---|---|---|
| K01 | só `holistic brandon.jpg` | Nano Banana 2.1, 4 variações, 9:16 |
| K02 | só `holistic brandon.jpg` | Nano Banana 2.1, 4 variações, 9:16 |

## Montagem no CapCut

Edição automática (`editar.py`, estilo FitWell): ritmo ~3,8 palavras/s, sem silêncio, legenda serifada branca, sem light leak, música a -25 dB da voz. Salvar os vídeos como V01 a V14: a ordem dos takes de plano único vem da fala. Sem Voice Changer. Marcar o post como conteúdo gerado por IA.

## Gates de qualidade

1. `python3 checar_entrega.py` e `python3 flow_seguro.py` sem falha.
2. Ficha dos frames escrita antes dos K (`FICHA_FRAMES.md`).
3. Checklist de envio rodado e informado fora dos blocos.
4. Na edição: fala de cada take conferida palavra por palavra com o roteiro.
