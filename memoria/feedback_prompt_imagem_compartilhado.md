---
name: feedback-prompt-imagem-compartilhado
description: "Regra de entrega dos prompts: quando takes consecutivos são o mesmo talking head (mesma posição, mesmo enquadramento, mesmo ângulo de câmera) e só mudam gesto/expressão, entregar UM ÚNICO prompt de imagem para o bloco inteiro e só variar os prompts de vídeo. Exceção: se muda o ESTADO de um prop/herói, o take ganha imagem própria."
metadata: 
  node_type: memory
  type: feedback
  modified: 2026-08-21T14:57:39.052Z
  originSessionId: 32e5549f-536c-4d15-8e9c-ed26d399e783
---

# Um prompt de imagem por BLOCO, não por take

Pedido do Luigi em 2026-08-20.

**A regra:** se uma sequência de takes é basicamente o avatar falando com a câmera na mesma posição e ângulo, e a única coisa que muda entre eles é gesto de mão e expressão, então **entregar UM prompt de imagem que serve o bloco inteiro** e entregar os prompts de vídeo separados, um por take, descrevendo a movimentação, a fala e o que muda de uma cena pra outra.

Ex.: se as cenas 4 a 10 são só ele conversando e gesticulando, é 1 imagem + 7 prompts de vídeo, não 7 imagens.

**Why:** cada geração de imagem custa tempo e crédito, e gerar 7 variações que diferem só no gesto é desperdício puro. O Veo já produz o gesto a partir de um único frame inicial. Antes eu estava entregando um "EDITAR do T_" por take, o que multiplicava geração sem ganho nenhum.

**How to apply:**
- Ao montar o índice de geração, agrupar takes contíguos que compartilham cenário, enquadramento, ângulo e props.
- Entregar 1 prompt de imagem por bloco, nomeando quais takes ele atende (ex.: "IMAGEM A · atende T8 a T13").
- Entregar os prompts de vídeo normalmente, um por take, cada um descrevendo o gesto e a fala daquele take.
- No índice, deixar explícito qual imagem alimenta qual take.

**Exceção (take ganha imagem própria):**
Quando muda o **estado** de alguma coisa em cena, não só o corpo do avatar:
- prop diferente na mão (frasco entra, caneca entra)
- cenário ou enquadramento muda
Aí é imagem nova, porque o frame inicial é de fato outro.

**Regra de bolso:** se dá pra chegar no frame do take seguinte só movendo o corpo a partir do frame anterior, é o mesmo bloco. Se precisa aparecer ou sumir alguma coisa, é bloco novo.

## NUNCA dividir um reveal contínuo em dois takes (erro cometido em 2026-08-20)

Se a transformação acontece **dentro de um único take do original, sem corte**, ela NUNCA pode virar dois takes nossos com duas imagens. Gera-se **uma imagem só, do estado inicial** (a pessoa prestes a despejar o líquido no pulmão sujo), e o **prompt de vídeo carrega a fala inteira do hook mais o reveal acontecendo**.

**Why:** o reveal É o herói do hook. Se a gente corta no meio dele, o espectador lê "ele pausou o vídeo e trocou o pulmão", não "o líquido limpou o pulmão". O corte destrói a prova e mata a credibilidade justamente no beat que segura o scroll. Correção dada pelo Luigi depois que eu dividi o hook do vídeo do pulmão em T1 preto e T2 rosa.

**O teste, uma pergunta só: o ORIGINAL corta entre os dois estados?**
- **Não corta** (líquido lavando o pulmão, cristais derretendo, água revelando dente branco) → **1 imagem do estado inicial**, o Veo faz a transformação. Ver [[regras-universais]] #9.
- **Corta** (antes/depois disfarçado, braço encolhendo take a take, roupa mudando de cor pra fingir dias) → imagens separadas, uma por estágio. Essa é a única exceção real.

**No ÂNGULO 2 a resposta desse teste inverte com frequência.** O herói lá costuma ser **corpo antes/depois**, que é o caso legítimo de imagens separadas. O teste continua exatamente o mesmo, só não estranhar quando a resposta for "corta". Take único vale quando o herói for físico e contínuo (algo despejado em algo, que é o que mais roda hoje). Ver [[angulo2-copy-fitywell]].

Ver [[erros-recorrentes]] falha #1 e #5.

Relacionado: [[prompts-imagem-json]], [[prompts-video-fase7]], [[feedback-prompts-na-conversa]], [[ordem-entrega-padrao]], [[regras-universais]]
