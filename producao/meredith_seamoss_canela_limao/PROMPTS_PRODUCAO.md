# PROMPTS | Sea Moss Venda · Água de canela, limão e mel → Natural Rems Sea Moss

flow_seguro: v1

Vídeo modelo: `input/modelo.mp4`. Âncora: `producao/_ancoras/meredith_callahan_ancora.png` (no Flow: `meredith callahan .png`). Funil: venda.

Os blocos copiáveis (K em parágrafo, V só com a fala) estão em `ENTREGA_MEREDITH.md`. Este arquivo guarda o índice e as regras.

## Índice de geração

| Take | Keyframe | Ação de geração |
|---|---|---|
| T1 | K01 | gerar K + V01 |
| T2 | K02 | gerar K + V02 |
| T3 | K03 | gerar K + V03 |
| T4 | K04 | gerar K + V04 |
| T5 | K05 | gerar K + V05 |
| T6 | K06 | gerar K + V06 |
| T7 | K07 | gerar K + V07 |
| T8 | K07 | reaproveita a imagem do K + V08 |
| T9 | K08 | gerar K + V09 |
| T10 | K09 | gerar K + V10 |
| T11 | K09 | reaproveita a imagem do K + V11 |
| T12 | K09 | reaproveita a imagem do K + V12 |
| T13 | K09 | reaproveita a imagem do K + V13 |
| T14 | K09 | reaproveita a imagem do K + V14 |
| T15 | K09 | reaproveita a imagem do K + V15 |

## Trava de identidade e continuidade

Todo K abre com a mesma descrição da avatar e da cozinha do Brooklyn (avatar fixo da conta) e anexa só a imagem dela. Mesmo turbante verde e açafrão, mesmos óculos vermelhos, mesmas argolas e pulseiras de ouro, mesma blusa e avental, mesma mesa de fórmica e bandeira em todo K.

## Bloco global de vídeo

Todo V: `The person in the image speaks in American English, looking at the camera: "<fala literal>"` + `Fixed camera. Natural lip sync, no music.` Padrão único do Flow (AGENTS.md, 2026-10-09): sem cena, roupa, objeto nem tom de voz no V.

## Mapa de âncoras

| Keyframe | Referências a anexar | Modelo |
|---|---|---|
| K01 | `meredith callahan .png` | Nano Banana 2.1, 4 variações, 9:16 |
| K02 | nenhuma imagem (só o texto) | Nano Banana 2.1, 4 variações, 9:16 |
| K03 | `meredith callahan .png` | Nano Banana 2.1, 4 variações, 9:16 |
| K04 | `meredith callahan .png` | Nano Banana 2.1, 4 variações, 9:16 |
| K05 | `meredith callahan .png` | Nano Banana 2.1, 4 variações, 9:16 |
| K06 | `meredith callahan .png` | Nano Banana 2.1, 4 variações, 9:16 |
| K07 | `meredith callahan .png` | Nano Banana 2.1, 4 variações, 9:16 |
| K08 | `meredith callahan .png` | Nano Banana 2.1, 4 variações, 9:16 |
| K09 | `meredith callahan .png` + `natural_rems_seamoss_produto.jpg` | Nano Banana 2.1, 4 variações, 9:16 |

## Montagem no CapCut

Edição automática (`editar.py`, acabamento HyperFrames): legenda palavra por palavra, cortes de pausa, música a -18 dB da voz. Texto de tela no gancho (V01): "What cinnamon does to the SUGAR in your body". O V02 é mudo: entra logo depois da fala do V01, como no modelo. Nos takes de CENA CURTA, cortar no fim da fala (o resto do clipe de 8s é sobra). O pote fica parado e legível do take do produto até o fim, sem corte para outro plano. Legenda do post: `#ad #syntheticperformer #naturalrems` no topo, sem link; chave de conteúdo de IA ligada; Story no ar com o link da Amazon.

## Gates de qualidade

1. `python3 checar_entrega.py` e `python3 flow_seguro.py` sem falha.
2. Ficha dos frames escrita antes dos K (`FICHA_FRAMES.md`).
3. Checklist de envio rodado e informado fora dos blocos.
4. Na edição: fala de cada take conferida palavra por palavra com o roteiro.
