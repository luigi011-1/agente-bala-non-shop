# Swipe orgânico · rodada 2026-09-25 · análise do lote de calibração

Lote enviado pelo Luigi em 2026-09-25: três vídeos de pessoa real no estilo que ele quer modelar e
dois vídeos de avatar IA que já fazem essa adaptação. Pipeline `/watch` rodado nos cinco
(`vN_watch/`), grades compactas em `grids/`, mapa dos arquivos em `input/MAPA.txt`.

**Nenhum vídeo do lote é do nicho Auraly.** Tudo aqui calibra FitWell (receita, saúde, hábito).
A Auraly precisa do próprio lote antes de qualquer regra.

---

## 1. Ficha de cada vídeo

| | v1 | v2 | v3 | v4 | v5 |
|---|---|---|---|---|---|
| Arquivo | `4M views.mp4` | `snapinsta-...5784701` | `snapinsta-...8095494` | `snapinsta-...8868128` | `snapinsta-...7668260` |
| Origem | **real** | **real** | **IA** | **real** | **IA** |
| Quem | homem ~35, casa suburbana | mulher ~35, cozinha | homem grisalho ~55, jaleco de chef | homem ~35, cozinha | homem grisalho ~55, cozinha de luxo |
| Duração | 20,8 s | 50,8 s | 37,4 s | 80,4 s | 34,4 s |
| Cortes | 3 | **0** (plano único) | 7 | 26 | 10 |
| Maior plano | ~6 s | 50,8 s | **7,9 s** | ~5 s | **6,9 s** |
| Palavras / ritmo | 73 · 3,6 p/s | 160 · 3,2 p/s | 110 · 2,9 p/s | 214 · 2,7 p/s | 96 · 2,9 p/s |
| Objetivo | **GROWTH** (sem CTA nenhum) | **VENDA** (isca: livro grátis) | GROWTH | **VENDA** (isca: replay de masterclass) | GROWTH |
| CTA | nenhum, o vídeo acaba no 4º hack | `comment fun` + livro de receitas grátis | `comment yes` + follow | `comment REPLAY` + replay grátis por tempo limitado | `comment yes` + save + follow + "take care of yourself" |
| Views conhecidas | 4M (nome do arquivo) | ? | ? | ? | ? |

### v1 · 4 hacks de casa contra praga (real, 4M)
Quatro itens `If you [põe X em Y], you can repel [praga]`, **um cenário por item**: lixeira no quintal
(canela e pimenta caiena, um pote em cada mão, derramando ao mesmo tempo), peitoril da janela
(algodão com óleo de hortelã, câmera na mão), porta da despensa (folha de louro), bancada (tigela de
vinagre de maçã com detergente). O primeiro frame já tem o pó caindo e a lixeira colada na lente.
Acaba seco no 4º item, sem CTA, o que favorece o loop.

### v2 · leite dourado (real, venda)
Plano único de tripé, meio corpo, bancada. Copo de leite no centro e **três colheres já carregadas
enfileiradas na frente** (cúrcuma, pimenta, mel). Cada ingrediente cai no copo quando é nomeado, e o
leite muda de cor ao vivo. Recapitula os quatro ingredientes com o benefício de cada um, fecha com
"thank me later" e oferece **mais do mesmo**: *"if you want more recipes... comment FUN and I'll send
you my free recipe book"*. Legenda em caixa alta condensada, uma ou duas palavras por vez.

### v3 · cookie de grão de bico (IA)
Tigela gigante de grão de bico colada na lente, o chef atrás debruçado. **Um corte por passo da
receita** (manteiga de amendoim, mel e baunilha, mixer, gotas de chocolate, boleador), depois a
bandeja pronta empurrada para a lente enquanto ele lista três benefícios leves, a linha de identidade
*"I make recipes that help you fight inflammation from the inside out"* e `comment yes` + follow.
Denuncia IA: luz dourada quente de fim de tarde, jaleco de chef de banco de imagem, cookies perfeitos.

### v4 · macarrão de alho e frango (real, venda)
26 cortes, estética ASMR de cozinha: câmera baixa na altura da bancada, ele **debruçado nos
cotovelos com o rosto perto da comida**, planos de cima (POV) no macarrão, mãos fazendo tudo. Fecha
com macros (500 kcal, 40 g de proteína, 7 g de fibra), **prova comendo** ("like this is so good") e
pivota seco para a oferta: masterclass gravada, *"comment the word REPLAY and I'll send it over to
you for free"*, disponível por tempo limitado.

### v5 · cheesecake de abóbora (IA)
Abre segurando o refratário com abóbora e cream cheese **estendido para a lente**. Um corte por
ingrediente (ovo, mel, baunilha, especiaria), batedor em close na hora do "silky smooth", forno,
chantilly em close, travessa pronta de volta à lente durante os benefícios, **comendo uma garfada
no CTA**. Denuncia IA: cozinha de revista ensolarada, rosto e cabelo de modelo.

---

## 2. O que os cinco têm em comum (5/5 salvo indicação)

1. **A primeira palavra é a instrução, e a frase é condicional.** `If you...` (3/5) ou
   `Did you know that if you...` (2/5). O benefício fecha a primeira frase, dentro de 4 s.
   Nenhum abre com dor, vilão, medo ou choque.
2. **A curiosidade vem da combinação inesperada**, não do bizarro: canela na lixeira, manteiga de
   amendoim no grão de bico, cream cheese na abóbora, cúrcuma no leite.
3. **Ação já começada no frame 0** (4/5): o ingrediente já está caindo. A exceção (v2) compensa com
   as colheres enfileiradas, que prometem a sequência antes de ela acontecer.
4. **O herói é o recipiente colado na lente** (lixeira, tigela, refratário, panela) com o rosto
   atrás. É exatamente a regra 1 do nosso `GATE_VISUAL.md`, que continua valendo aqui.
5. **Cada ingrediente é mostrado no momento em que é dito.** Fala e ação sincronizadas palavra a
   palavra; a legenda queimada acompanha.
6. **Benefício leve e de estrutura/função:** "supports your body's inflammatory response", "helps
   digestion", "steady your blood sugar", "keep you full for hours". Nada de curar, derreter, destruir.
   A única promessa forte do lote (v4, "15 to 25 pounds in 90 days") é da oferta, não da receita.
7. **Posição de quem ensina, nunca de depoimento.** Ninguém diz "eu perdi X kg". Isso encaixa direto
   no COACH da FitWell, sem precisar liberar primeira pessoa de resultado.
8. **Prova de sabor no fim** (v4 e v5 comem na câmera; v2 "thank me later"; v3 empurra a bandeja).
9. **Legenda queimada palavra a palavra** em todos, cada conta com a sua fonte.
10. **Áudio sem silêncio.** No vão de 2 s sem fala do v4 o nível fica em -17 dB, igual ao da fala:
    tem trilha ou som de cozinha por baixo. Não consegui separar qual dos dois; conferir de ouvido.

## 3. Os dois formatos de venda (v2 e v4)

- **O corpo é igual ao de growth.** A receita é entregue inteira, sem esconder passo.
- **A oferta é MAIS DO MESMO e é grátis:** livro de receitas (v2), replay da aula (v4). Não é
  pivô para dor. Quem gostou da receita pede mais receita.
- **Keyword própria em caixa alta** (`FUN`, `REPLAY`) + "I'll send you". É o nosso `yes` + DM.
- **v4 tem escassez** ("available for a limited time this month") e pivota sem ponte depois da
  garfada. **v2 faz ponte de continuidade** ("more recipes on how you can use functional foods").

## 4. Como a IA fez a adaptação (v3 e v5), e onde errou

**O truque central:** o formato real de plano longo (v2 tem 50 s sem corte) virou **um clipe por
passo da receita, todos com 8 s ou menos**. O corte no ingrediente esconde o limite do Veo e
qualquer deriva de identidade, e parece edição de criador, não costura de IA.

Esqueleto dos dois, que é o gabarito direto para nós:

```
T1  recipiente colado na lente + ingrediente já caindo + "Did you know that if you [X] to [Y]"
T2..Tn  um clipe por ingrediente ou passo, fala = o passo, mão fazendo; inserts macro no payoff
Tn+1  o prato pronto empurrado para a lente + 2 ou 3 benefícios leves com "which helps"
Tn+2  linha de identidade ("I make recipes that...") ou garfada na câmera
Tn+3  comment yes + save + follow (+ sign-off pessoal)
```

- Inserts de 0,7 a 2 s sem fala própria (v5: ovo, batedor, chantilly) = nosso `B-ROLL` com a fala
  do take vizinho por cima.
- Os dois avatares são **homens grisalhos de 50 e poucos**, congruentes com público 40+.
- **Os dois erram onde o nosso gate já acerta:** luz quente e dourada (v3), cozinha de revista
  ensolarada (v5), pessoa bonita demais. Os reais têm luz de dia nublado, casa comum e bagunça.

## 5. Sinais de "pessoa real" que os reais têm e os IA não (para os prompts)

- **Microfone de lapela preto preso na gola** (v1 e v4). Detalhe barato que grita criador real.
- Casa comum com ruído: ímãs e fotos na geladeira (v2), caixa de correio e rua pela janela (v1),
  cafeteira e tábua de corte gasta (v4). Nada de cozinha de catálogo.
- Camiseta lisa, sem figurino.
- Câmera: tripé na altura da bancada (v2, v4), selfie na mão (v1 janela), POV de cima (v4).
- Postura: **debruçado nos cotovelos com o rosto perto da comida** (v4), gesto de mão grande (v1).
- Luz: dia nublado de janela ou quintal (v1, v2, v4). Confirma o `GATE_VISUAL.md` 1.1.

## 6. O que isto muda no nosso processo (leitura, a decidir com o Luigi)

- **O herói colado na lente e a luz neutra não mudam**, e os IA do lote mostram o custo de ignorar.
- **Fala e voz:** tom de quem ensina com entusiasmo, não "apaixonada, como se exigisse ser ouvida".
- **Takes:** `take segue a cena do modelo` já cobre; clipes de passo curtos viram `CENA CURTA` ou
  `B-ROLL` com a fala do vizinho.
- **Bandeira dos EUA em todo K:** nenhum real tem. Em cozinha de receita ela precisa virar detalhe
  natural (ímã, pano de prato, caneca) ou sair. Decisão do Luigi.
- **Cenário:** as âncoras FitWell (garagem, fazenda de mel, jardim de chá) servem de identidade; a
  receita pede bancada. Jamie Anderson tem congruência natural com receita de mel; Lynn Parker com
  chá; Dana Morrison com churrasco no quintal.
- **Venda FitWell pelo molde v2/v4:** receita inteira + "comment yes and I'll send you [mais do
  mesmo]". O que é esse "mais do mesmo" no funil do quiz é decisão do Luigi.
- **Auraly:** sem referência neste lote. Pedir um lote próprio antes de escrever regra.
