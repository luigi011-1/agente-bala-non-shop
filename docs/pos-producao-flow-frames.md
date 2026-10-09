# Frames to Video, geografia e tela de celular

Aprendido em 2026-10-05 a 10-08 (casos 27 e 28 da biblioteca). Vale para qualquer produção
que gere do zero no Flow (Nano Banana → Veo) com mais de um plano no mesmo espaço.

## 1. Geografia: uma âncora, o resto por edição

**Sintoma:** V1 com quadro inicial K01 (POV na remada) e final K02 (Leslie no banco). O Veo
inventou 1,8s de giro pela academia vazia e a câmera "teletransportou" para trás de uma
coluna. O produtor: "ficou sem sentido de espaço".

**Causa:** K01 e K02 foram gerados separados, cada um com sua academia, luz e posição de
câmera. Não existe movimento físico que ligue os dois, então o Veo inventa um.

**Regra:**
- Gere e aprove **uma imagem-âncora** (o herói). Todas as outras imagens do mesmo espaço
  saem **por edição dela** ("o momento um segundo antes, do mesmo lugar, celular virado 45°
  para a direita" / "zoom 3x do mesmo lugar e ângulo").
- Defina o **mapa** antes de escrever: quem filma, onde, virado para onde. Escreva na
  primeira linha do plano.
- **A câmera não anda.** Gira no lugar (≤ 45°) e dá zoom. É o que alguém filmando
  escondido faz, e o Veo reproduz sem inventar espaço.
- A âncora decide a direção do giro. Se ela mudar, reescreva o giro (caso 27: esquerda →
  direita depois da nova âncora).

**Conserto sem gerar de novo:** corte no meio do giro (o borrão do movimento esconde o corte,
efeito whip) e pule o trecho inventado. Caso 27: 0-2,2s + 4,0-8s.

## 2. Tela de celular

| Quero | Faça | Não faça |
|---|---|---|
| Tela real de um app | Edite o keyframe anexando o print: "replace only the content of the phone screen with the attached app screen, same angle and perspective" | Pedir a tela ao Veo ou ao Omni por referência: ele inventa a interface (caso 28) |
| Texto da tela estável no vídeo | **Mesma imagem como início e fim** no Frames to Video; a mão mexe pouco e a tela não troca | Pedir que o polegar role a página: as letras deformam |
| Tela genérica | "generic dark-mode workout app, white card, flat illustration, gray placeholder lines, no readable text" | Deixar o gerador escrever: sai alfabeto inventado |

- Prints das gravações de tela do produtor servem de tela real: extraia o quadro com
  `ffmpeg -ss <t> -i gravacao.mov -frames:v 1 tela.png`.
- **Orgânico de curiosidade** ("que app é esse?"): esconda o logo ("the top header with the
  logo is scrolled out of view"). **Anúncio pago:** mostre a marca.

## 3. Texto dentro da imagem (motion de app, anúncio)

Exceção à regra "zero texto": em anúncio de app o título vai **dentro do keyframe**, porque
o Nano Banana Pro escreve certo e o Veo não.
- O quadro final que tem texto novo sai **por edição** do inicial, então o título igual não muda.
- Texto que só existe no meio do vídeo (sem estar num quadro) sai errado: "Toncud Meah",
  etiquetas duplicadas quando voam. Prenda o texto num quadro ou esconda o trecho com
  aceleração (2x) na montagem.

## 4. Movimento: descreva o passo, não o nome

"Faz três pontes de glúteo" → a figura ficou parada 4s. Descreva a mecânica: "sobe o quadril
até formar uma linha reta dos ombros aos joelhos, segura um instante, desce até encostar o
quadril no chão, e repete mais duas vezes, ritmo constante".

## 5. Ferramentas

- **Omni (plano único de 10s):** ótimo para movimento contínuo (scan + etiquetas + celular
  levantando saíram lindos), mas **só respeita a imagem inicial**. Telas e referências do
  meio viram inspiração. Use só quando nada depois do primeiro segundo precisar ser fiel.
- **Flow vídeo-para-vídeo** com referência > 8s, câmera em movimento e duas pessoas: falhou
  4x com "Falha ao gerar áudio", mesmo mudo, mínimo e cortado em 8s. Não insista: FORMA 1.
- O Flow entrega 720p por padrão. Baixe em 1080p.
- Quando o Veo deixa a tela do celular branca por ~1s numa transição, corte o trecho.

## 6. Elemento que entra em cena (caso 29, 2026-10-08)

"Mesma imagem no início e no fim" serve para **segurar** texto parado. Se o prompt pede que
algo **entre** (mão subindo com o celular), o Veo mantém o elemento parado e inventa um
**segundo** subindo. Faça o quadro inicial **sem** o elemento (edição: "remove the hand and
the phone completely") e o final com ele, e escreva "existe só uma mão em todo o vídeo".

## 7. Uma pergunta, uma resposta por cena

Cena com scan + 5 etiquetas + cartão de total em 4s ficou "confusa" para o produtor. Cada
cena responde a pergunta do texto com **um** elemento grande ("✓ Fits your day · 383 of
2719 kcal"). Detalhe extra fica fora.
