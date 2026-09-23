---
name: ordem-entrega-padrao
description: "Ordem obrigatória de entrega ao decompor um vídeo — SEMPRE mandar (1) transcrição completa do vídeo modelo, (2) roteiro final separado cena a cena, e (2b) uma versão só-fala do roteiro (sem rótulos/descrições, pronta pra gerar a voz), ANTES de qualquer prompt de imagem ou vídeo."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 20a5bfba-89c2-4020-a895-ec8b0f5fa495
  modified: 2026-08-21T03:34:23.059Z
---

# Ordem de entrega padrão (obrigatória)

Ao decompor um vídeo de referência, **antes de enviar QUALQUER prompt de imagem ou de vídeo**, entregar nesta ordem:

## 1. Transcrição completa do vídeo modelo
A transcrição integral do vídeo que vamos modelar, com timestamps (sai do `/watch` em `audio/transcript.txt`). Completa, não resumida.

## 2. Roteiro final separado cena a cena
O roteiro adaptado que vai virar os takes do vídeo final, **já quebrado por cena/take**, com:
- Número do take
- Função do beat (HOOK / MECANISMO / RECEITA / PROTOCOLO / RESULTADO / PROVA / UPSELL / CTA)
- A fala exata em inglês daquele take
- Marcação TALKING ou B-ROLL

## 2b. Roteiro só-fala (versão para gerar a voz)
Junto do roteiro cena a cena, entregar TAMBÉM uma versão **só com as falas** — sem rótulos de take, sem descrição de cena, sem função do beat. Só o texto que o avatar diz, pronto pra colar no gerador de voz (TTS). Juntar as falas que ficam partidas entre dois takes numa frase contínua (fica mais natural na voz; ele corta nos pontos se gerar por take). Pedido do usuário em 2026-08-14.

## 2c. Roteiro traduzido para PORTUGUÊS (obrigatório)
**SEMPRE** entregar também o roteiro completo em português, logo depois da versão em inglês, nessa mesma etapa. Pedido do Luigi em 2026-08-21.

**Why:** ele revisa e ajusta a copy em português. Ler só em inglês dificulta enxergar o que está fraco e decidir o que mudar, e é justamente nessa etapa que ele quer intervir antes de gastar geração.

**How to apply:**
- **FORMATO OBRIGATÓRIO: uma tabela só, com as duas línguas na MESMA LINHA.** Colunas: `# | Beat | English | Português`. Nunca duas tabelas separadas.
- Tradução fiel, não recriação: o objetivo é ele enxergar a copy, então traduzir o sentido e o tom sem "melhorar" nada por conta própria.
- O inglês continua sendo a fonte de verdade que vai pros prompts.
- A versão só-fala pode ficar só em inglês (é pro TTS).
- Aplicar a regra do [[estilo-copy-sem-travessao]] também na tradução.

**Por que tabela única (corrigido em 2026-08-21):** eu entregava duas tabelas separadas e o roteiro mudou de 19 pra 22 takes durante os ajustes. Sobrou versão antiga em inglês no histórico e o Luigi ficou sem saber qual valia. Com as duas línguas na mesma linha é impossível uma ficar desatualizada em relação à outra.

**Ao reentregar depois de um ajuste:** marcar a versão nova como a que vale e dizer explicitamente que ela substitui tudo que veio antes na conversa.

## 3. Só então os prompts
Prompts de imagem (frame inicial) e prompts de vídeo (Fase 7).

**Why:** o usuário precisa validar a fala e a estrutura do roteiro ANTES de gastar geração em imagem/vídeo. Prompt gerado em cima de roteiro não aprovado é retrabalho garantido.

**How to apply:** vale para todo vídeo novo, todo avatar, todo nicho. Sem exceção. Faz parte do fluxo de [[processo-7-fases]] entre a Fase 4 (Roteiro) e a Fase 5 (Prompts de imagem) — é o ponto de checagem com o usuário.

Ver também: [[skill-watch]] (de onde sai a transcrição), [[regras-universais]].
