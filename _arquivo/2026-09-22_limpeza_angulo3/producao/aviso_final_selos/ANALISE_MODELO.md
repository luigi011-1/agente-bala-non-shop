# Analise do video modelo - aviso_final_selos

Arquivo: `producao/aviso_final_selos/VIDEO_MODELO.mp4` · 101,4s · 720x1280 (9:16)
Angulo 3 / Auraly · Objetivo declarado: **GROWTH**
Metodo: medicao com `ffmpeg` (deteccao de corte, `volumedetect`) mais leitura das legendas
queimadas no video. Nao havia ferramenta de transcricao de audio na maquina, entao a fala foi
reconstruida a partir das legendas karaoke, quadro a quadro.

---

## 1. Classificacao: CRESCIMENTO

Fecha com like, save, share, comentario e visita ao Stories. **Nao tem produto, link, oferta,
preco nem keyword de conversao.** Confirma o que o Luigi declarou no intake.

Consequencia, por `feedback-growth-video-sem-venda`: o roteiro clona quase palavra por palavra.
Nada de ponte de causas, alibi, CTA de produto ou follow gate com motivo de entrega. O CTA final e
o do proprio original.

## 2. Estrutura medida

**Cortes** (limiar `scene > 0.12`): `1.47 · 3.73 · 4.07 · 4.40 · 7.57 · 7.73 · 7.90 · 8.07 · 10.00`

Nove mudancas de plano nos primeiros 10 segundos e **zero cortes nos 91 segundos seguintes**.
E exatamente o padrao medido na amostra de 54 virais do nicho: todo o orcamento de edicao vive no
gancho, e o corpo e um plano unico.

**Volume medio por janela de 3s:**

| janela | 0-3s | 3-6s | 6-9s | 9-12s | 20s | 40s | 60s | 80s | 95s |
|---|---|---|---|---|---|---|---|---|---|
| dB | -20,5 | -29,2 | **-38,8** | -15,8 | -16,0 | -17,2 | -16,3 | -16,3 | -16,7 |

O trecho de 6 a 9 segundos esta a **-38,8 dB**, que e silencio. A fala so comeca por volta de 9,8s.
**O gancho inteiro e mudo**, e o que segura o scroll e a imagem mais o texto de tela.

## 3. O gancho, plano a plano (0 a 10s)

Cozinha domestica real, luz de janela, fogao com uma panela de agua fervendo e um pote grande de
vaselina sobre a boca do fogao.

| t | plano | o que acontece |
|---|---|---|
| 0,2s | medio, ela de pe na cozinha | segura uma **calcinha vermelha** aberta com as duas maos · panela fervendo ao lado |
| 1,5s | **corte para MACRO** | close fechado na calcinha vermelha ocupando o quadro |
| 3,7s | macro continua | ela vira a peca, mostra frente e verso |
| 4,4s | medio | aproxima a calcinha do pote de vaselina |
| 5,8s | medio baixo | **mergulha a calcinha dentro da vaselina** |
| 7,6s | **corte para MACRO** | puxa a peca coberta, a vaselina escorre em fio longo |
| 8,1s | medio | leva a peca escorrendo para cima da panela |
| 10,0s | plano de corpo, fixo | **comeca a falar** e fica ai ate o fim |

**Texto de tela fixo durante todo o gancho:** `This is your last warning!`
Nao ha outro overlay estatico no video. Do segundo 10 em diante so existem as legendas karaoke.

**A acao estrutural do hook**, que e o que o metodo Puzzle preserva:

> a avatar segura UMA PECA INTIMA, mergulha ela dentro de UM POTE DE PRODUTO DOMESTICO GORDUROSO
> e levanta a peca escorrendo por cima de UMA PANELA FERVENDO, e continua segurando a peca ate o
> fim do video

Os eixos de troca disponiveis: `OBJETO` (a peca), `SUBSTANCIA` (o produto do pote), `LOCAL`
(o comodo e o aparelho), `COR` (da peca), `RESULTADO` (o que acontece com a peca) e `MARCADOR`.

## 4. O corpo (10 a 101s)

**Um unico plano fixo, sem nenhum corte.** Ela fica de pe na cozinha, segurando a calcinha
coberta de vaselina acima da panela fervendo, falando direto para a camera, do segundo 10 ao fim.
A peca **nunca chega a ser solta dentro da panela**: fica na mao o video inteiro, exatamente como
a CARTA SOULMATE fica na mao nas nossas producoes Auraly.

## 5. Transcricao reconstruida (ingles)

Lida das legendas karaoke, com amostragem de 0,7s e verificacao fina nos pontos ambiguos.

> I don't know your name, but if this video found you today, it was 100% meant for you. When you
> receive these blessings, keep your mouth shut, because something truly huge is coming into your
> life. If this video appeared for you right now, don't skip it, or these blessings will turn
> against you. Send this video to yourself right now to seal this energy within the next 33 minutes.
> Two extraordinary things will happen at the same time that will change your life forever. The
> 11:11 portal is aligning right now at this exact moment, and all of this comes from Saint Michael.
> I see great good luck and a transformative love coming your way. Your twin flame will contact
> you, and you will receive a massive amount of money tomorrow at 11:11 in the morning. A young fit
> handsome man thinks about you every single day, but something is blocking this connection from
> happening. Three seals to unlock this frequency: like this video, save this video, and share it
> with one person. Then comment 222 so I can see that you completed all three seals. If you sealed
> it correctly, your good news will arrive within 33 minutes. Can't forget one final detail: tap my
> profile picture and check my stories immediately, because the second part of this sign is waiting
> for you there.

⚠️ **O unico ponto que eu inferi em vez de ler:** o numero do comentario. As legendas mostram os
grupos `THEN COMMENT 2` e depois `2 SO I`, que e o que o agrupador de karaoke imprimiu. Dois digitos
aparecem na tela; o padrao do nicho e do nosso angulo e `222`. Adotei **222**. Se o Luigi ouvir o
audio e for outro numero, a troca e de uma palavra em um take.

## 6. Esqueleto de copy preservado

| # | Beat | O que faz |
|---|---|---|
| 1 | Aviso e selecao | nao sei seu nome, mas este video achou voce hoje, foi 100% para voce |
| 2 | Sigilo | fique de boca fechada, porque vem algo enorme |
| 3 | Punicao por inacao | nao pule, ou as bencaos se viram contra voce |
| 4 | Primeira acao com prazo | mande o video para si mesma, selar em 33 minutos |
| 5 | Promessa dupla | duas coisas extraordinarias ao mesmo tempo |
| 6 | Autoridade divina e portal | portal 11:11 alinhando agora, tudo vem de Sao Miguel |
| 7 | Leitura de amor e dinheiro | sorte, amor transformador, chama gemea, dinheiro amanha as 11:11 |
| 8 | O rosto nomeado, nunca mostrado | um homem jovem e bonito pensa em voce todo dia |
| 9 | O obstaculo | algo esta bloqueando essa conexao |
| 10 | Os tres selos | like, save, share com uma pessoa |
| 11 | O comentario | comente 222 para eu ver que voce selou |
| 12 | Prazo do retorno | boa noticia em 33 minutos |
| 13 | Destino Stories | toque na foto do perfil, a segunda parte do sinal esta la |

**Observacoes de congruencia com a nossa doutrina:**

- O modelo **ja faz a inversao do funil** que o Angulo 3 adotou em 2026-09-04: o destino final e o
  **Stories**, e as acoes sao o selo. Nao precisamos adaptar nada nesse ponto.
- O beat 8 **nomeia o rosto sem entregar o rosto**, que e a trava que nunca mudou.
- Registro **divino, nunca oculto**: Sao Miguel, bencaos, portal, frequencia. Nenhuma palavra de
  pacto, feitico ou bruxaria. Passa na lei do registro sem ajuste.
- O modelo **nao pede follow**. Como e crescimento, nao acrescento follow: clonar e a regra.
- O modelo **nao cita preco, produto, quiz nem app**. Nada a cortar.

## 7. Congruencia de avatar

A avatar do modelo e uma mulher. Os seis avatares desta producao sao **homens**. O publico continua
sendo mulher, entao o beat 8 (`a young fit handsome man thinks about you`) continua correto na boca
deles: e o leitor falando para a espectadora sobre um terceiro homem.

Unico ajuste de voz por avatar, permitido pela regra de crescimento: o registro e a idade aparente
mudam o quanto de autoridade cabe em cada frase. A fala em si nao muda.
