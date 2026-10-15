---
name: take-cortado-criterio-opcao1
description: "Take gerado que cortou a ponta da frase (Luigi, 2026-10-14, 'opção 1'): a fala termina na última frase completa do take, sem refazer no Flow; vale em todos os ângulos. Inclui o que nunca pode cair (marca, Amazon, yes, follow, Stories) e o que pode (bio)"
metadata:
  node_type: memory
  type: feedback
  originSessionId: 769237f4-1ad1-43d3-a650-d5a556746023
  modified: 2026-10-14T15:38:43.168Z
---

Em 2026-10-14 o V09 da Marshall (canela) cortou em "...is annoying, and no" porque 26 palavras não couberam em
8s. Ofereci: (1) terminar a fala em "is annoying." ou (2) refazer o take. **Luigi escolheu a opção 1**, e depois
mandou resolver tudo sozinho sem pedir auxílio ("resolva tudo isso e não me peça mais auxílio").

**Why:** refazer no Flow quase sempre corta de novo (a frase não cabe), custa tempo dele e a frase anterior já
fecha o sentido.

**How to apply:**
- Take que cortou a ponta: a fala termina na vírgula ou ponto anterior ao que faltou; se essa vírgula jogar fora
  mais de 3 palavras ouvidas, termina na última palavra ouvida, nunca numa palavra solta ("one", "than", "of",
  "with", "and"); se não houver jeito limpo, volta para a vírgula. Ex.: "...takes an hour.", "...and sixteen
  ingredients." (nunca "Dicing." nem "with less than one.").
- Palavra inicial faltando (1 ou 2): a fala começa onde o take começou ("They honestly taste like...").
- Grava como exceção por avatar/take (`OVR` no `textos.py` do lote), regenera roteiro e pacote e reedita; o
  editor apara o pedaço que sobrou no take.
- **Nunca pode cair:** Natural Rems / nome da marca, Amazon, `yes`, follow, Stories. **Pode cair:** a bio
  (aceito no CTA da Cassidy · bolinho, 2026-10-14). Se o corte levaria algo da lista, o take volta para o Flow.
- Não perguntar de novo ao Luigi em lote autônomo: aplicar, registrar no STATUS e listar no relatório final.
- Prevenção vale mais que o critério: teto ~20 palavras por take nas avatares 60+ ([[producao-licoes-lote-1014]]).
Relacionado: [[edicao-autonoma-sem-interferencia]].
