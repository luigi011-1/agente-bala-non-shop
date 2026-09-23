---
name: feedback-entrega-multi-avatar-sob-demanda
description: "Produção multi-avatar grande (6+ avatares): gerar e validar TODOS os pacotes em disco de uma vez, mas colar cada pacote completo no chat só quando o Luigi disser qual avatar está trabalhando no Flow, não todos de uma vez."
metadata:
  node_type: memory
  type: feedback
  originSessionId: current
  modified: 2026-09-22T15:41:55.033Z
---

# Entrega multi-avatar: arquivos todos de uma vez, chat sob demanda

Confirmado pelo Luigi em 2026-09-22, na produção `fitywell_growth_cortisol_props` (9 avatares).
Perguntei se ele queria os 8 pacotes restantes colados em sequência numa resposta muito longa ou
um de cada vez sob demanda. Ele escolheu **um de cada vez, sob demanda**.

**Why:** cada pacote de avatar exige colar de novo o bloco `INSTRUÇÕES PARA A MEMÓRIA DO AGENTE`
mais o bloco de imagem e o bloco de vídeo inteiros (regra de [[feedback-flow-instrucoes-por-avatar]],
nunca pular). Em produções grandes isso gera paredes de texto enormes por avatar. Como o Luigi
trabalha o Flow um avatar por vez, colar os 8 de uma vez na conversa não ajuda, só torna a resposta
difícil de navegar.

## Como aplicar

1. **Gerar e validar TODOS os pacotes em disco na mesma rodada** (`PROMPTS_<AVATAR>.md` e
   `FLOW_<AVATAR>.md` para cada avatar da fila), rodando `checar_entrega.py` e `checar_frases.py`
   até zero falhas em todos. Isso não muda, é trabalho de produção normal.
2. **Colar no chat apenas o primeiro avatar (ACTIVE) completo**, exatamente como sempre.
3. **Para os avatares seguintes, NÃO colar automaticamente.** Avisar que estão prontos em disco,
   com os caminhos dos arquivos, e esperar o Luigi indicar qual avatar ele quer no chat agora.
4. **Quando ele pedir um avatar**, colar o pacote completo daquele avatar: bloco de instruções
   inteiro (nunca "igual ao anterior"), bloco de imagem, bloco de vídeo, mapa K/V, tabela bilíngue.
5. Isso não contradiz a regra de nunca pular o bloco de instruções. Muda só o RITMO de quando cada
   pacote entra na conversa, nunca o conteúdo de cada pacote quando ele entrar.

Relacionado: [[feedback-flow-instrucoes-por-avatar]], [[workflow-entrega-gabarito]]
