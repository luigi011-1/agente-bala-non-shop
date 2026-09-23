---
name: feedback-prompt-completo-sempre
description: "Luigi (2026-08-26): NUNCA entregar instrucao de patch tipo 'adicione X em todos os prompts'. Toda regra nova tem que ja vir aplicada dentro de cada prompt, completo, pronto pra copiar e colar. Vale pra prompt de imagem, de video e pra qualquer bloco reaproveitado."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 35741d33-8b83-4947-a661-f71261849cf0
  modified: 2026-08-26T22:58:24.476Z
---

# Prompt entregue é prompt COMPLETO. Nunca instrução de patch.

**Regra do Luigi, 2026-08-26.** Palavras dele: *"sempre manda os prompts completo, não quero que
você me mande algo do tipo 'adicione a seguinte coisa em todos os prompts', não, quero que você
mesmo já adicione nos prompts pra mim."*

**O que está proibido:**
- "adicione `X` no campo `scene` de todos os prompts"
- "troque o `prop` por..." como forma de entregar uma variação
- colar só a linha que mudou e mandar ele aplicar nos outros
- resumir prompts do corpo com `...a seguinte frase:` em vez de colar os cinco blocos inteiros

**O que é obrigatório:** quando uma regra nova aparece no meio da produção, eu **reescrevo todos os
prompts afetados por inteiro**, no arquivo E na conversa, com a regra já dentro. Ele copia e cola,
nunca edita.

**Why:** o trabalho dele é copiar prompt e gerar imagem. Instrução de patch transfere pra ele um
trabalho de edição manual que é meu, e é onde entra erro humano: um prompt esquecido no meio de
oito, e a continuidade do vídeo quebra num take só, que é o tipo de defeito que só aparece depois
de tudo gerado.

**How to apply:** antes de fechar qualquer entrega de prompts, conferir se existe alguma frase minha
pedindo que ELE altere alguma coisa. Se existir, aplicar eu mesmo e reescrever o bloco inteiro.
Uma nota explicando *por que* mudou pode ficar, desde que o prompt ao lado dela já esteja corrigido.

Vale junto com [[feedback-prompts-na-conversa]] (arquivo E chat, nunca só um) e
[[workflow-entrega-gabarito]].

**Exceção única:** quando eu ofereço uma ALTERNATIVA que ele pode ou não querer (dois caminhos
possíveis), aí sim entrego os dois prompts completos, lado a lado, e ele escolhe. Nunca um prompt
mais a instrução de como virar o outro.
