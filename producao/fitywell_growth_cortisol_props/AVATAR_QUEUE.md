# AVATAR QUEUE

Production: `fitywell_growth_cortisol_props`
Angle: 2, FityWell
Objective: GROWTH
Reference video: `input/reference_video.mp4`

Ordem preservada dos anexos recebidos em 2026-09-22. Fila é estado em disco, nunca conversa.

| Ordem | Estado | Avatar | Âncora exata | Adaptação de cenário registrada |
|---:|---|---|---|---|
| 1 | DONE | Dana Morrison | `/Users/macbookairm2/Desktop/AVATARES/avatares fitywell/dana morrison .png` | props (pernas com salto, bustos com vestido, antebraço) na bancada de madeira e no chão de concreto da garagem |
| 2 | DONE | Eva Dall | `/Users/macbookairm2/Desktop/AVATARES/avatares fitywell/Eva Dall .jpeg` | props na bancada de mármore verde da cozinha |
| 3 | DONE | Ivy Carl | `/Users/macbookairm2/Desktop/AVATARES/avatares fitywell/Ivy Carl .jpeg` | props na mesa de madeira da varanda coberta |
| 4 | DONE | Jamie Anderson | `/Users/macbookairm2/Desktop/AVATARES/avatares fitywell/jamie anderson .png` | props no porta-malas aberto do SUV, mesmo estacionamento (mesma adaptação já usada em `fitywell_growth_wentao_healer`) |
| 5 | DONE | Jamie Voss | `/Users/macbookairm2/Desktop/AVATARES/avatares fitywell/Jamie Voss .jpeg` | props na bancada de pedra da cozinha clara |
| 6 | DONE | Lais Collins | `/Users/macbookairm2/Desktop/AVATARES/avatares fitywell/Lais Collins .jpeg` | props na ilha branca do apartamento moderno |
| 7 | DONE | Lynn Parker | `/Users/macbookairm2/Desktop/AVATARES/avatares fitywell/lynn_parker_.jpeg_20260919203702.jpeg` | props na mesa de madeira escura já adicionada ao apotecário (mesma adaptação já usada em `fitywell_growth_wentao_healer`) |
| 8 | DONE | Robert Alves | `/Users/macbookairm2/Desktop/AVATARES/avatares fitywell/Robert Alves .jpeg` | props na bancada clara da cozinha de cabana |
| 9 | DONE | Roberta Carvalho | `/Users/macbookairm2/Desktop/AVATARES/avatares fitywell/Roberta Carvalho.jpeg` | props na bancada de pedra da cozinha residencial |

## Travas da produção

- Todos são COACH do FityWell para mulheres 40+.
- Objetivo é crescimento: clonar o esqueleto e o fechamento do modelo quase palavra por palavra, sem
  enxertar venda, quiz, app ou preço além do que já está no original.
- Produto fora de quadro.
- Roteiro, takes e fechamento serão aprovados uma vez e bloqueados para toda a fila. O hook (T1) é a
  única variável por avatar, escolhido entre as dez opções de `HOOKS.md`.
- Cada avatar preserva a própria identidade e o próprio cenário canônico (`avatares-fichas`, roster
  FityWell). Os três props (pernas com salto, bustos com vestido, antebraço) entram como adição
  pontual dentro de cada cenário, nunca substituindo o cenário do modelo.
- Seis dos nove avatares são homens apesar do nome (Eva Dall, Ivy Carl, Jamie Voss, Lais Collins,
  Robert Alves e o já conhecido Jamie Anderson); Roberta Carvalho é mulher. Nenhum fala em primeira
  pessoa sobre corpo feminino. Ver `producao/_ancoras/AVATARES_FITYWELL_2026-09-19.md`.

## Estado atual

- Roteiro aprovado em 2026-09-22. Hooks escolhidos: H1, H2, H7, H10.
- Nove pacotes internos concluídos (`PROMPTS_<AVATAR>.md`) e nove blocos limpos do Flow
  (`FLOW_<AVATAR>.md`).
- Cada avatar gera quatro vídeos finais (um por hook), totalizando trinta e seis combinações.
- Todos os nove passaram `checar_entrega.py` com zero falhas e `checar_frases.py` sem repetição.
- Não há avatar `PENDING` nem `ACTIVE`. `PRODUCTION COMPLETE`.
