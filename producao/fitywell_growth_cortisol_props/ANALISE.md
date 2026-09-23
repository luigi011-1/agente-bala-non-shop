# Análise do vídeo modelo

Produção: `fitywell_growth_cortisol_props`
Ângulo: 2, FityWell
Objetivo: GROWTH (classificado pelo usuário, 2026-09-22, ver nota de classificação abaixo)
Duração do modelo: 28,327 s
Formato: vertical 720 x 1280, 30 fps
Cortes detectados: praticamente nenhum. É um plano único contínuo, câmera estática, do início ao fim.

## Nota de classificação (growth x venda)

O modelo fecha com keyword `yes`, follow gate com motivo de entrega ("must be following or I can't
reach you") e oferta de um protocolo ("I'll send you the complete cortisol protocol I give all my
clients"), que é o padrão técnico de VENDA, não de crescimento puro. Perguntei e o usuário confirmou
classificação GROWTH mesmo assim: clonar o roteiro quase palavra por palavra, sem ponte de causas
extra, sem álibi, sem crivo pesado de copy, sem enxertar app/quiz/preço. O CTA final é o mesmo do
original (protocolo + `yes` + follow gate), só com o registro de voz ajustado por avatar (todos são
COACH, então "I give all my clients" já encaixa sem mudança).

## Diagnóstico central

A retenção nasce de comparação física direta usando três props de referência sempre visíveis no
quadro: um par de formas de perna com salto vermelho, dois bustos de manequim de alfaiataria
pendurados com vestido branco, e um antebraço de prop. O coach aponta, em sequência, para um ponto
mais alto e depois mais baixo em cada prop, sugerindo que uma marca do corpo "desceu" com o tempo.
Não há transformação em vídeo (é tudo still + fala), a comparação é sugerida pela fala e pelo gesto
de apontar dois pontos.

## Beat map do modelo

| Tempo | Função | Fala | Ação visual |
|---|---|---|---|
| 0,00 a 5,34 | HOOK, salto + pernas | "You put on high heels. Your legs used to be here. Now they're closer to here." | Plano fechado nas pernas-prop com salto vermelho, dedo enluvado azul aponta um ponto alto e depois um ponto mais baixo na coxa |
| 5,34 a 13,22 | Vestido + braço | "Your favorite dress used to sit here... And your arm used to be here..." | Câmera sobe para os bustos pendurados (vestido) e depois para o antebraço-prop erguido, mesmo gesto de apontar dois pontos |
| 13,22 a 17,06 | Vilão institucional | "They told you it was age and genetics. But honey, that's only a small part of the story." | Direto pra câmera, sem prop, meio-corpo |
| 17,06 a 21,50 | Reveal + qualificação | "This isn't fat. This is cortisol. If you can relate to two or more of these," | Direto pra câmera, mesmo plano |
| 21,50 a 28,18 | CTA + follow gate | "comment yes below and I'll send you the complete cortisol protocol I give all my clients. Must be following or I can't reach you." | Direto pra câmera, mesmo plano, sorri no final |

## Herói do hook

Os props (pernas com salto, bustos com vestido, antebraço) são o herói visual do vídeo inteiro, não
só do hook. Não há 2ª pessoa em cena: é o coach sozinho com os três props de comparação. Cenário do
modelo: oficina/estúdio rústico com vigas de madeira, macramê, vasos de planta e luz neutra de dia.

## Engenharia que será preservada

- Coach sozinho, sem 2ª pessoa, com os props de comparação em quadro.
- ⚠️ Desvio consciente do modelo: no original as pernas-prop ficam em quadro o vídeo inteiro, porque
  lá existe UM gancho só. Aqui são quatro ganchos compartilhando um corpo, e as pernas são justamente
  o prop que muda entre eles, então elas saem de quadro do T2 em diante. Sem isso, o corpo só serviria
  ao H1 e os outros três ganchos abririam com um calçado e continuariam com outro.
- Mesmo gesto em todos os três props: apontar um ponto alto, depois um ponto mais baixo.
- Plano único, câmera estática, do início ao fim (sem corte de cena).
- Progressão `heels/pernas -> vestido/braço -> vilão institucional -> reveal cortisol -> CTA + follow`.
- CTA de protocolo, keyword `yes` e follow gate idênticos ao original (regra de growth: clonar o
  fechamento, não regravar).
- Produto, app e quiz fora de quadro e fora da fala (nem o original menciona).

## Adaptação por avatar

Cenário do modelo (oficina rústica) não é obrigatório: cada avatar preserva o próprio cenário
canônico (regra fixada em `PLAYBOOK_FITYWELL.md` seção 5, já usada em `fitywell_growth_wentao_healer`
para este mesmo roster). Os três props (pernas com salto, bustos com vestido, antebraço) entram como
adição pontual dentro do cenário de cada um, mesma lógica da tábua de corte que entrou nas cozinhas
do pacote de gengibre.

## Risco e mitigação

Claim central ("this is cortisol") é linguagem comum no nicho de wellness (cortisol belly/cortisol
face), não uma alegação médica exclusiva. O ponto de maior risco de compliance é o CTA de protocolo:
mantido porque o usuário confirmou classificação growth e pediu clonagem do fechamento original tal
como está. Nenhuma alegação nova foi adicionada além do que já existe no vídeo modelo.
