---
name: take-segue-cena-do-modelo
description: "Cada cena do vídeo modelo vira o próprio take. Nunca juntar duas cenas num take nem cortar frase no meio para caber em 13 a 29 palavras. Cena curta = take curto marcado CENA CURTA (Luigi, 2026-09-23)"
metadata:
  type: feedback
---

Em 2026-09-23 o Luigi reprovou o roteiro de `fitywell_growth_canela_acucar`: eu tinha juntado o
gancho (cena de 4s, 10 palavras) com o começo da receita e cortado a frase da receita no meio para
cada take cair dentro de 13 a 29 palavras. Palavras dele: *"você está misturando cenas e cortando
frases ao meio pra que caibam no limite que você propôs pra cada take, não quero que faça isso mais"*.

**Why:** a faixa de palavras existe para o take de 8s não sair acelerado nem arrastado. Ela nunca
foi motivo para desmontar a estrutura do modelo. Juntar cena e cortar frase quebra a fidelidade de
ritmo e de corte, que é o que a rodada de validação testa ([[validar-antes-de-variar]]).

**How to apply:**
- Mapear as cenas do modelo pelos cortes do `/watch`. Cada cena = um take (um `K__` + um `V__`).
- Cena curta: take curto, cabeçalho `### Tn · BEAT · TALKING · Setup X · CENA CURTA`. O piso de 13
  não vale para ele. No `V__`, a fala sai em ritmo natural no começo e o resto do clipe é a ação sem
  fala; na edição corta no tempo da cena do modelo.
- Plano do modelo com mais de 8s: dividir só em fim de frase, nunca no meio.
- A frase só atravessa dois takes quando o próprio modelo corta a cena no meio dela.
- Teto de 29 palavras vale sempre. Nunca filler. Ver [[faixa-palavras-take]].
- O `checar_entrega.py` só aceita take abaixo de 13 com a marca `CENA CURTA`.
- Linha com fala por cima de uma ação nunca vira take mudo com voz-over: ver [[take-mudo-so-sem-voz]].
