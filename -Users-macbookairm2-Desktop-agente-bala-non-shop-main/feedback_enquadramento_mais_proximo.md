---
name: feedback-enquadramento-mais-proximo
description: "Fidelidade ao original é de ESTRUTURA (elementos, ação, reveal), NUNCA de enquadramento. Sempre puxar a câmera pra mais perto que o vídeo original: quase close-up em props E pessoas, mesmo quando o original usa plano médio ou aberto."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: f522ec05-bf5e-47fd-b93c-3480612112e4
  modified: 2026-08-19T01:13:26.970Z
---

Ao clonar um vídeo, manter fiel o **elemento, a ação e o reveal**, mas **NÃO copiar o enquadramento do original**. Sempre puxar a câmera pra mais perto do que o original estava: padrão quase close-up, bem próximo da câmera, tanto para props/heróis quanto para pessoas.

**Why:** o enquadramento não faz parte do esqueleto. Copiar a distância de câmera do original é jogar fora a maior alavanca gratuita que existe de atenção e de qualidade de geração. Mantendo os mesmos elementos e a mesma ação, um enquadramento mais fechado faz o clone **chamar mais atenção que o próprio original**, e ainda melhora o realismo, porque menos informação de fundo faz o gerador segurar a qualidade. O Luigi corrigiu isso em 2026-08-18 depois que entreguei prompts reproduzindo o plano médio do vídeo modelo.

**How to apply:**
- Perguntar em todo prompt de imagem: "dá pra estar mais perto?" Se der, está longe demais.
- Props/herói: encher o quadro, muito à frente do rosto, câmera puxada em cima dele.
- Pessoas: preferir peito pra cima ou ombros pra cima. Rosto ocupando boa parte do quadro.
- 2ª pessoa: pode entrar **cortada** pelo quadro em vez de aparecer de corpo inteiro. Presença parcial basta pra dar o contexto e ainda deixa o herói dominar.
- Fundo: quanto menos informação, melhor. O cenário canônico do avatar só precisa ser reconhecível, não inventariado.
- Vale para TODOS os takes, não só o hook.

O que continua intocável: quais elementos aparecem, o que acontece com eles, a ordem dos beats e o reveal. Ver [[metodo-puzzle]] (composição do hook), [[stack-ferramentas]] (close-up + poucos elementos = mais qualidade e realismo), [[erros-recorrentes]].
