---
name: edicao-licoes-teste
description: "Edição automática dos takes do Flow: o que FAZER e o que NÃO fazer, aprendido nos testes de 2026-10-09/10 (erros meus e do editor). Ler antes de toda edição e antes de mexer no editar.py"
metadata:
  node_type: memory
  type: feedback
  originSessionId: c642df4f-f1fb-40d0-8d3c-047fd36bab5f
  modified: 2026-10-10T03:24:28.829Z
---

Testes de 2026-10-09 e 10 no Mac do Luigi, antes da primeira produção real com edição automática:
takes crus do v04 (FitWell growth, gengibre e limão), takes fabricados a partir de vídeos modelo e das
edições de referência dele. Detalhe técnico de cada erro (8 a 26) em `docs/pos-producao-edicao-regras.md`;
padrão de gosto dele em `docs/pos-producao-referencias-luigi.md`. Pedido do Luigi: *"saber o que você NÃO
deve fazer é tão importante quanto saber o que você DEVE fazer"*.

**Why:** cada erro abaixo passou por mim ou pelo editor pelo menos uma vez. Quatro deles (ordem do insert,
legenda em cima do insert, insert virando piscada, repetição escondida) passaram em TODAS as conferências
automáticas e só apareceram quando eu olhei as imagens ou fabriquei o caso.

**How to apply:**

FAZER
- Conferir a fala de cada take PALAVRA POR PALAVRA com o roteiro. O Flow inventa, remove e repete fala no
  mesmo take. Inventou, repetiu ou silêncio: corta em qualquer ponto. Faltou ou trocou: aquele vídeo para,
  avisar qual take refazer e seguir a fila.
- Olhar `cortes.png`, `legendas.png` e uma folha de quadros do vídeo final ANTES de dizer que está pronto.
  RELATORIO todo OK não prova que está certo.
- Renomear take mudo com o número DO TAKE (`t07_pimenta.mp4`) antes de rodar; eu mesmo renomeio, sem perguntar.
- Testar o caso negativo e o positivo: o detector precisa pegar o erro E deixar passar o take limpo.
  Sem take real, fabricar o erro com ffmpeg a partir de um vídeo com fala limpa.
- Editar um vídeo atrás do outro, avisando a cada um concluído. No Mac, uma edição por vez (~10 min cada).
- Mudança no editor vai junto com a regra no `docs/pos-producao-edicao-regras.md` e para o GitHub em
  branch + PR; merge só com ok do Luigi.

NÃO FAZER
- Não confiar em nota de semelhança da fala (90% deixou passar repetição curta e palavra faltando).
- Não confiar que a transcrição do whisper mostra repetição: ele SUPRIME fala repetida e estica a palavra
  anterior por cima dela. Cruzar com o áudio (`fala_sem_texto`) e transcrever o trecho suspeito sozinho.
- Não achar pausa pelo tempo das palavras do whisper (ele estica a palavra até a seguinte).
- Não tratar o fim de uma palavra falada devagar como "fala escondida": só cortar quando o trecho, transcrito
  sozinho, tiver OUTRA palavra (V01 temperos, 2026-10-10: o "Why?" perdeu o fim e o take travou).
- Não usar limiar de silêncio fixo nem pelo pico (`silencedetect -35dB`): pausa com chiado do Flow ficava.
  E não baixar o piso do limiar para salvar palavra fraca (as pausas voltam): proteger a palavra das pontas
  do take pelo tempo dela (o "one." final do V01 temperos sumia).
- Não proteger a última palavra pelo tempo do whisper (ele estica): só até onde ainda há voz no áudio.
- Não juntar página curta de legenda que fecha frase à página seguinte ("stay i"): vai para a anterior.
- "If you have any questions, please feel free..." num trecho escondido é alucinação do whisper em ruído.
- Não proteger palavra no INÍCIO do take (o whisper começa a 1ª palavra em 0,0s): só na ponta final.
- Não gerar trecho com menos de 2 quadros (pausa curta do take-herói acelerada 5x quebrava a montagem).
- Não deixar página de legenda com duração zero: o HyperFrames deixa ela na tela (o "why" do T3 apareceu no T5).
- Não juntar trecho curto com vizinho que está longe: um estalo depois de 1,5s de pausa trazia a pausa junto.
- Não numerar take falado e take mudo em sistemas diferentes (falas x takes): o limão caiu depois do Boil.
- Não deixar insert mudo entrar inteiro, nem passar pelo corte de fala, nem com a legenda anterior por cima.
- Não aceitar "voz-over" em take mudo na produção: a fala some do vídeo ([[take-mudo-so-sem-voz]]).
- Não usar edição já pronta (com legenda, selo ou flash gravados) como material de teste sem descontar:
  gera texto dobrado e falso "quadro fantasma".
- Não cortar material de teste com `-to` depois do `-i` quando a duração muda (ele corta a saída e some o fim).
- Não presumir que takes ou pastas do Luigi continuam no lugar: ele apaga e move (o `~/Desktop/v04` sumiu
  no meio do teste). Conferir antes de usar.
- Não seguir sem música calado, nem com caminho da nuvem no Mac: o editor agora para.

Ambiente e armadilhas do Mac em [[ambiente-mac-luigi]]. Leitura de hook continua em [[erros-recorrentes]].
