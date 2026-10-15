---
name: producao-licoes-lote-1014
description: "Lote Sea Moss VENDA a partir de receitas virais (2026-10-13/14, 4 modelos x Meredith/Marshall/Cassidy = 12 vídeos, do /watch ao editado): erros e acertos de roteiro, pacote, Flow e edição autônoma. Ler no começo de toda produção dos Ângulos 1, 2 e 4 e antes de toda edição em lote"
metadata:
  node_type: memory
  type: feedback
  originSessionId: 769237f4-1ad1-43d3-a650-d5a556746023
  modified: 2026-10-14T15:31:30.554Z
---

Lote `producao/seamoss_receitas_lote_2026_10_13/` (canela, bolinho de maçã, wrap de lentilha, sorvete de banana).
Formato novo pedido pelo Luigi: começo igual ao viral (gancho + receita) e ponte pelos pontos fracos de fazer a
receita (tempo, gosto, custo, ingrediente ruim, preparo de manhã) → sea moss faz o mesmo trabalho → gomas comuns
cheias de açúcar → Natural Rems → yes → Amazon → Stories/bio → follow. Lições da edição em
[[edicao-autonoma-sem-interferencia]]; lote anterior em [[producao-licoes-lote-1010]].

**Why:** pedido do Luigi em 2026-10-14: "liste os erros e acertos ... e grave ambos". Cada erro abaixo custou
retrabalho, take perdido ou reedição; cada acerto encurtou o lote.

**How to apply:**

ACERTOS (repetir)
- P1 de verdade: achei que 2 dos 4 modelos já tinham virado growth FityWell para as mesmas contas na véspera e
  que a fricção "16 frascos / panela toda manhã" já estava queimada nas três contas. Avisar antes de escrever.
- Vídeo em espanhol: retranscrever com `--language es --model small` (o `small.en` deu lixo) e traduzir fiel.
- Estrutura da ponte aprovada de primeira (só o CTA do roteiro 3 voltou): corpo idêntico entre avatares, só a
  linha de autoridade muda por conta; `checar_frases` OK nas 12. Ingredientes da ponte só do rótulo (canela não
  está nos 16: nunca dizer que a goma tem canela); limão → vitamina C, mel → manuka.
- Compliance na hora do roteiro: linha do tempo de resultado ("day three... day five") virou presente sem prazo;
  "burning belly fat" suavizado e só na receita; 180 °C → 350 °F; "brain fog" fora; brownie do modelo → sorvete.
- Infra reaproveitada: `textos.py` + `gerar_roteiros.py` + `gerar_pacotes.py` sobre `pacote_minimo.gerar` →
  12 pacotes de uma vez, 0 falhas no linter e no flow_seguro. Exceções por avatar/take em `OVR` no textos.py,
  aplicadas nos DOIS geradores (o editor lê fala de roteiro e de pacote).
- Cenário fixo da conta + aparelho de bancada quando a receita pede (forninho, fogareiro, freezer horizontal).
- Lote grande: todos os pacotes em disco, chat um por vez ([[feedback-entrega-multi-avatar-sob-demanda]]).
- Take que não gera: ignorar e registrar no roteiro/pacote/LOTE pelo gerador (a anotação à mão some no regen).
- Edição autônoma fechou 12/12 sem o Luigi: orquestrador nohup + repescagem, `auto.py` resolvendo sozinho
  escuta, invenção e corte de ponta, e `legendas.png` olhada em cada vídeo antes de dizer pronto.

ERROS (não repetir)
- CTA de venda escrito como growth (roteiro 3): "comment yes if you want more recipes" + follow com rabicho.
  Na venda o yes amarra à DOR do vídeo e o follow é só "And don't forget to hit that follow button."
- Gerador do lote anterior com `{MID} {REF_POTE}` literal no K (faltou f-string): conferir o texto final do K.
- Mapa K/V agrupava takes não contíguos como "V11 a V17 usam K11" (agente usaria imagem errada). Corrigido no
  `pacote_minimo`; conferir o mapa quando um K volta depois de outro.
- Take mudo de figura humana se desfazendo ("sugar figure crumbles") não gerou no Flow, nem com variação, para a
  Marshall: forma humana se desmanchando lê como corpo. Preferir objeto sem forma humana no V mudo.
- FALA LONGA DEMAIS PARA 8s com estas avatares 60+: cortaram no fim os takes de 22 a 27 palavras (T9 canela 26,
  T15/T16 bolinho, T13 wrap 27, T18 bolinho 24, CTA 25, T14 sorvete 26). Teto prático ~20 palavras nelas;
  quebrar produto e CTA em dois takes. O linter aceita 29, a avatar não.
- CENA CURTA (2 a 6 palavras) em clipe de 8s: o Flow inventa fala para encher ("An apple a day...", "Now we add
  cinnamon, sprinkle it all over...", "Thanks for watching!"). O editor apara, mas às vezes corta errado.
- Esqueci de renomear o take mudo da Meredith (`V02_...` → `t02_`); e take mudo com som ambiente faz o whisper
  "ouvir" fala: tirar o áudio (`-an`) dos mudos antes de editar.
- `auto.py` aceitava take com fala INVENTADA como exceção (a invenção ficaria no vídeo): só erro de escuta vira
  exceção; invenção se corta.
- Regra de encurtar fala gerou "But let's be real. Dicing." e "with less than one." antes de ser corrigida:
  auditar a lista de OVR no fim do lote e ler cada fala ajustada.
- Desktop no iCloud com disco cheio: takes `dataless` quebraram leitura no meio da edição; baixar antes.
  `/tmp/edicao` ~2 GB por vídeo: limpar o que já foi entregue antes de lote grande.
- Imagem escolhida do K do pote mostrou a tabela de trás (Meredith wrap): a foto do produto tem dois potes;
  reforçar "front label facing the camera" e conferir o rótulo da frente ao escolher a imagem.
- Pendências que ficaram sem resposta do Luigi: descartar as versões growth de 12/10 (v01/v02) e corrigir o
  gerador do lote rins/seios. Perguntar de novo no próximo contato.

Formato em [[formato-receita-ponte-venda]]; critério de take cortado em [[take-cortado-criterio-opcao1]].
