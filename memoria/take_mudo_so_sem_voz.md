---
name: take-mudo-so-sem-voz
description: "Take mudo (insert) só quando NÃO há fala por cima dele. Fala de roteiro em cima de uma ação vira take FALADO com a ação acontecendo enquanto o avatar diz a frase. Vale em todos os ângulos (Luigi, 2026-10-09)"
metadata:
  type: feedback
---

Em 2026-10-09, no teste do editor automático com o v04 (FitWell growth, gengibre e limão), os inserts
da pimenta (T7) e do limão (T8) estavam no pacote como mudos com "voz-over", mas nenhum take gravava as
falas "and a pinch of black pepper," e "then squeeze in the juice of half a lemon.". Resultado: essas
falas não existem no vídeo, nem na versão aprovada. Decisão do Luigi: *"vamos priorizar não fazer takes
mudos pra maior segurança, os takes mudos serão permitidos apenas se não tiver nenhuma fala por cima do
take"*.

**Why:** voz-over em cima de take mudo depende de uma fala gravada em outro lugar, que no Flow não
existe, e o editor automático não tem de onde tirar essa voz. Take falado com a ação junto é seguro:
a fala sai na mesma geração.

**How to apply:**
- Toda linha do roteiro com fala é um take FALADO: o avatar diz a frase enquanto a ação acontece
  (ex.: ela fala "and a pinch of black pepper" jogando a pimenta na panela).
- Take mudo (`(no speech) ...` no V) só quando nada é dito em cima dele. Vale para os ganchos mudos do
  Auraly (T1 sem voz-over, com os cortes internos ao V) e para qualquer take realmente mudo, em todo ângulo.
- Nunca marcar "voz-over" num take mudo. Se o modelo usa narração por cima de B-roll, o clone vira
  take falado com a ação, ou a fala vai para o take falado vizinho.
- Take mudo no pacote já leva o nome de arquivo com o número do take (`t07_pimenta.mp4`) para a edição.
- O editor avisa no relatório quando um take mudo tem fala no roteiro. Ver [[take-segue-cena-do-modelo]]
  e [[prompts-video-fase7]].
