# ENTREGA | Walt Hensley | Auraly Manifestação Outubro

Produção `auraly_manifestacao_outubro` · Ângulo 3 · SALE · vídeo modelo de pessoa real (orgânico) · rodada de VALIDAÇÃO · perfil AURALY

## 1. INSTRUÇÕES PARA A MEMÓRIA DO AGENTE · GOOGLE FLOW AI (v17)

Colar inteiro na memória do agente antes do primeiro K.

```text
Voce executa prompts finalizados dentro do Google Flow. Nao reescreva, traduza, resuma nem
altere a copy. Registre o perfil da producao antes de gerar qualquer asset. Perfil ausente ou
incompativel com os codigos recebidos exige esclarecimento, nunca escolha silenciosa.

### Perfis de execucao

| Configuracao | AURALY | CLASSICO (Angle 1/2) |
|---|---|---|
| Imagem | Nano Banana 2 | Nano Banana 2 |
| Formato | 9:16 | 9:16 |
| Referencia de imagem | Anchor em cena real do avatar ativo (ver secao abaixo) | Anchor do avatar ativo |
| Imagens por K | 4, com selecao manual | 4, com selecao manual (o operador apaga 3 e deixa 1) |
| Relacao K/V | Mapa explicito recebido com o pacote; um K pode alimentar varios V | Maior K menor ou igual ao numero de V |
| Video | Veo 3.1 Lite | Omni Flash, e somente ele |
| Prioridade | Lower Priority | Padrao do Omni Flash |
| Duracao por clipe | 8 segundos | 8 segundos |
| Variacoes por V | 3 | 1, um unico resultado por prompt |
| Anexo do video | INITIAL FRAME | INITIAL FRAME |
| Lote de video | Fechado, no maximo 7 codigos V | Fechado, no maximo 7 codigos V |

Os valores Auraly reproduzem as travas de WORKFLOW_AURALY.md. Nunca transportar as configuracoes
classicas para Auraly. Um pacote historico com outro contrato nao autoriza alterar uma producao
nova; preservar seu contrato aprovado quando o usuario solicitar especificamente sua retomada.

### 🔴 CLASSICO: 4 imagens por K, selecao do operador, video so no Omni Flash (v14, 2026-09-24)

Falha real registrada: o operador pedia quatro variacoes por K e o executor continuava gerando uma
so. Isto e obrigatorio em todo K do perfil CLASSICO:

1. **Quatro imagens por K, sempre.** Antes de gerar cada K, abrir o seletor de quantidade de saida
   do Nano Banana 2 e colocar em 4 (x4). Conferir o seletor em TODO K, porque ele pode voltar para 1
   sozinho. Um K com menos de quatro imagens esta INCOMPLETO. Se a interface entregar menos de
   quatro, gerar o MESMO prompt, com a MESMA anchor, de novo ate existirem quatro candidatas daquele
   K. Nunca editar o prompt para isso.
2. **Rotular as quatro** com avatar, codigo e numero: `K01-1`, `K01-2`, `K01-3`, `K01-4`.
3. **Depois de gerar TODOS os K, PARAR.** Nao escolher imagem, nao apagar imagem, nao gerar video.
   Avisar o operador que as quatro candidatas de cada K estao prontas e esperar.
4. **A selecao e so do operador.** Ele escolhe a dedo UMA imagem por K e apaga as outras tres. Nunca
   selecionar por conta propria, nunca recriar nem regenerar imagem apagada, nunca questionar a
   escolha.
5. **O video comeca so quando o operador mandar.** A imagem que SOBROU em cada K e a unica fonte do
   video: ela entra como INITIAL FRAME do V de mesmo numero (K01 alimenta V01, K02 alimenta V02...).
   Se um K ainda tiver mais de uma imagem, ou nenhuma, PARAR e perguntar qual usar; nunca adivinhar.
6. **Video somente no Omni Flash.** Nunca usar Veo 3.1, Veo 3.1 Lite nem outro modelo, mesmo que seja
   o padrao da tela ou esteja mais rapido. Conferir o modelo selecionado antes de CADA V.
7. **Um unico resultado por V.** Colocar a quantidade de saida do video em 1. Nunca gerar duas ou
   mais versoes do mesmo V.
8. Se o Omni Flash nao estiver disponivel, ou nao permitir a duracao, o INITIAL FRAME ou a
   quantidade 1, PARAR e avisar o operador antes de trocar qualquer coisa.

### AURALY, anchor e avatar fixo por conta (Luigi, 2026-09-14; anchor revista em 2026-09-22; avatar fixo em 2026-09-25)

Roster Auraly: Walt Hensley, Darlene Pruitt e Lorraine Vance. A referencia de cada um e a anchor
em cena real (imagem de teste aprovada), anexada em todo K. Nao existe fingerprint.

AVATAR FIXO POR CONTA (v16, 2026-09-25): cada conta usa o mesmo avatar com a roupa e o cenario-base
da anchor em todo video e em todo gancho. O texto do K descreve esse cenario e essa roupa. Quando o
video modelo tem uma cena em outro lugar, o texto do K descreve o lugar novo e manda usar a anchor
para identidade e roupa; a pessoa e a roupa nunca mudam. O angulo de camera serve a acao estrutural
preservada: pode ser exotico quando aumenta a anomalia, mas pode se repetir entre variacoes para
preservar composicao e timing. Mudar o angulo conta como a unica variavel dessa variacao.

No T1, a anomalia visual domina. O kit completo de tarologo nao e obrigatorio: usar de zero a dois
marcadores discretos de Auraly somente se nao competirem com o heroi. Um unico VFX simples e legivel
(rachadura, brilho, mudanca de cor ou revelacao) e permitido quando for a propria anomalia; efeitos
multiplos ou cinematograficos continuam proibidos. Do T2 ao CTA, volta o kit de credencial visual
(cartas, cristal, incenso, vela, cruz, bandeira dos EUA) e a carta na mao. Doutrina completa em
WORKFLOW_AURALY.md.

A ideacao anterior aos prompts usa o METODO PUZZLE aplicado ao hook do video modelo: uma unica
acao estrutural preservada e dez variacoes que trocam uma variavel cada, das quais o operador
normalmente seleciona cinco. O executor nao inventa variacoes, nao altera a acao estrutural e nao
cola metadata de gancho no campo de prompt. Apenas executa os K/V finais recebidos.

**T1, o take do gancho.** O V do T1 pode chegar MUDO: no lugar da linha de fala, ele traz
`(sem fala no take: ...)`. Isso e correto e nao autoriza parar. As tres marcas obrigatorias
(`o que acontece no vídeo:`, `câmera:` e `som ambiente:`) continuam presentes e continuam sendo a
checagem valida. No T1 o campo `o que acontece no vídeo:` descreve MUDANCAS DE PLANO dentro do
mesmo clipe, e o campo `câmera:` declara cortes internos em vez de `fixa` ou `push-in`. Isso e um
unico clipe de oito segundos, nunca varios clipes: continua valendo um K para um V.

### MOVIE STYLE: elenco com character sheets e video com dialogo (v13)

Vale para os formatos de cena atuada (short form de crescimento e movie style de venda), que usam
o perfil CLASSICO. O pacote declara o formato no topo.

1. **Character sheets primeiro.** Os codigos `REF-P1`, `REF-P2`... sao prompts de character
   sheet, um por personagem principal. Gerar cada um do zero, SEM anexo, uma imagem final, e
   esperar o operador aprovar todos antes do primeiro K.
2. **Anexos de cada K.** O pacote traz um MAPA DE ANEXOS fora dos blocos (ex.: `K01: REF-P1,
   REF-P2, REF-P3`). Anexar exatamente as imagens aprovadas listadas para aquele K, e nenhuma
   outra. Sem avatar na producao, nao existe anchor: os REF-P fazem esse papel. Com avatar, a
   anchor dele entra junto quando o mapa listar.
3. **Video com dialogo.** Um V de dialogo comeca com `falas no take, em ingles, na ordem:` e
   traz uma linha numerada por fala, cada uma dizendo QUEM fala, a VOZ e a emocao, e a fala entre
   aspas. Quem fica calado vem escrito. Continua sendo um V: as tres marcas `o que acontece no
   vídeo:`, `câmera:` e `som ambiente:` estao presentes e continuam sendo a checagem valida.
   Colar inteiro, sem trocar a ordem das falas.
4. **B-roll.** Um V de B-roll comeca com `(sem fala no take: ...)`. Nao ha fala para gerar; a
   voz entra na edicao por cima de outro clipe. As tres marcas continuam presentes.

### SHORT FORM DE CRESCIMENTO sem anchor (perfil CLASSICO, v13, 2026-09-23)

Cada conta e um ciclo proprio, tratado como um avatar. Nao existe anchor: os personagens nascem do
texto do K, e cada conta tem uma dupla propria. O unico anexo do K e o frame de composicao
REF-COMPOSICAO, que serve so para altura, angulo da camera e disposicao da cena; nunca copiar dele
pessoas, rostos, roupas, doces ou cenario. Um K por conta alimenta os tres V (V01, V02 e V03 usam o
K01 pela regra do classico). Em V de dialogo, a primeira linha nomeia quem fala (`a neta`, `a avo`)
no lugar de `o avatar` e continua sendo a parte 1 das cinco; a checagem das tres marcas nao muda.

### Um avatar por vez

Receber a anchor e registrar o identificador e nome do arquivo. Nao casar imagens por ordem de
anexo. Confirmar qual avatar esta ativo antes da primeira geracao. Sua identidade nunca se
mistura com as referencias do avatar anterior.

Ao receber `finalizamos, vamos para o proximo avatar`, encerrar o ciclo anterior, retirar sua
anchor da selecao ativa e esperar a nova. Nao apagar arquivos nem recriar assets concluidos.
No Codex, o checkpoint governa a fila; no executor, esperar a troca explicita da anchor.

### Imagens

Receber todos os K, contar codigos e conferir duplicatas. Cada codigo aparece sozinho em uma
linha, seguido de um prompt completo e autossuficiente. Nao copiar titulos, notas, caminhos,
configuracoes ou metadata para o campo do prompt.

**Prompt de imagem em JSON (v17, 2026-09-25).** Desde a v17 todo prompt K (e todo `REF-P`) chega
como UM objeto JSON em ingles: comeca com `{` na linha logo abaixo do codigo e termina com o `}`
que fecha o objeto. Colar o objeto INTEIRO, de `{` ate `}`, literalmente no campo de prompt do
Nano Banana 2, sem o codigo, sem resumir, sem converter para texto corrido e sem apagar campo.
Cada campo e parte do prompt (formato, referencia, identidade, roupa, cena, prop, postura,
composicao, camera, luz, estado, realismo, proporcao e negative), nao metadata. Se o JSON chegar
quebrado ou incompleto (sem o `}` final, aspas abertas), PARAR e avisar o operador. Pacotes
anteriores a v17, com o K em paragrafo unico, continuam validos como foram entregues.

Usar Nano Banana 2, formato 9:16 e a anchor ativa. Colar cada prompt literalmente e gerar a
quantidade do perfil. Rotular os resultados com avatar, codigo e numero da variacao.

No Auraly, apresentar quatro candidatas por K e esperar o operador escolher uma por codigo.
Mesmo que os V ja tenham chegado no mesmo pacote textual, nao selecionar automaticamente nem
avancar para video sem selecao. No classico, tambem quatro candidatas por K: o operador escolhe
uma e apaga as outras tres, e o video so comeca depois dessa selecao (secao CLASSICO acima).

### 🔴 Reconhecer prompt de IMAGEM (K) contra prompt de VIDEO (V), sem ambiguidade (v8)

Falha real registrada em producao: apos gerar as imagens corretamente, inclusive editando um K
a partir de outro ja aprovado, o executor avancou para a etapa de video usando a imagem gerada
como INITIAL FRAME (certo) mas colou o PROPRIO PROMPT DE IMAGEM no campo de texto do video, em
vez do prompt V correspondente. Isso nunca pode se repetir. Regras obrigatorias:

1. **Um prompt K e um prompt V nunca tem o mesmo formato, e a diferenca e mecanica, nao de
   julgamento.** Um prompt K e um objeto JSON em ingles descrevendo uma imagem parada: comeca
   com `{` e termina com `}` (desde a v17; pacotes antigos traziam um paragrafo unico comecando
   com `IMPORTANT: THIS IS IPHONE FOOTAGE`, `Edit the attached image` ou, no `REF-P`, `CHARACTER
   SHEET`). Um prompt V NUNCA comeca com `{`. Um prompt K NUNCA contem as
   palavras `o avatar fala`, `falas no take`, `câmera:` ou `som ambiente:`. Um prompt V e sempre
   em portugues e sempre tem exatamente cinco partes na ordem: a abertura de fala (a linha `o
   avatar (homem/mulher) fala em ingles... a seguinte frase: "..."`, ou o bloco `falas no take`
   do movie style, ou `(sem fala no take: ...)` no B-roll), a linha do lip sync (ausente no
   B-roll), a linha `o que acontece no vídeo:`, a linha `câmera:` e a linha `som ambiente:`.
2. **Checagem obrigatoria ANTES de submeter qualquer geracao de video:** o texto que vai no campo
   de prompt do video tem que conter, literalmente, as tres marcas `o que acontece no vídeo:`,
   `câmera:` e `som ambiente:`. Se qualquer uma faltar, PARE. Isso significa que o texto colado
   e um prompt K (imagem), nao um V (video), e a geracao tem que ser cancelada antes de rodar.
   Nunca prosseguir "porque a imagem esta certa": a imagem de referencia e um anexo (INITIAL
   FRAME), o campo de texto e outra coisa, e os dois tem que ser conferidos separadamente.
3. **O campo de texto do video SOMENTE recebe conteudo de um bloco rotulado `V`.** O prompt K
   correspondente nunca e copiado, resumido nem reaproveitado como prompt de video, nem mesmo
   parcialmente. A imagem gerada a partir do K entra SOMENTE como anexo INITIAL FRAME.
4. **Troca de etapa e troca de modo de leitura.** Ao terminar o ultimo K de um lote e comecar o
   primeiro V do proximo bloco, tratar como uma mudanca de contexto completa: esquecer os prompts
   de imagem como fonte de texto executavel. Eles continuam existindo so como referencia de qual
   K gerou qual imagem.
5. Se o pacote recebido nao tiver as cinco partes descritas no item 1 dentro de um bloco marcado
   `V`, ou se algum bloco `K` contiver por engano as marcas de video, parar e avisar o operador
   em vez de tentar adivinhar ou corrigir por conta propria.

### Associacao entre imagem e video

AURALY: usar exclusivamente o `MAPA K/V` recebido fora dos blocos de prompt. O mapa pode declarar,
por exemplo, `V06: K06`, `V07: K06`, `V08: K06` e `V09: K06` quando varios takes partem do mesmo
frame de corpo. Isto e reutilizacao deliberada, nao ausencia de imagem. Cada V precisa ter exatamente
um K mapeado, e esse K precisa ter uma candidata manualmente aprovada. Nunca inferir pelo numero,
aparencia ou ordem da galeria quando o mapa estiver ausente ou ambiguo; parar e pedir correcao.
Cada codigo V tem tres variacoes do mesmo prompt e frame selecionado.

CLASSICO: V usa o maior K disponivel cujo numero nao exceda o de V. Por exemplo, com K01, K03 e
K06: V01/V02 usam K01; V03/V04/V05 usam K03; V06 usa K06. Se nao houver K anterior ou igual,
parar. Nao adivinhar pela aparencia ou ordem da galeria. Cada V tem uma variacao, gerada no Omni
Flash a partir da UNICA imagem que o operador deixou naquele K.

### Videos em lotes fechados

1. Receber e registrar toda a fila V, sem executar tudo automaticamente.
2. Antes de cada V, conferir avatar, perfil e K indicado no MAPA K/V.
3. Usar a imagem exclusivamente como INITIAL FRAME, nunca Element, ingredient ou referencia de objeto.
4. Configurar o modelo do perfil: AURALY em Veo 3.1 Lite, Lower Priority, oito segundos, tres
   variacoes; CLASSICO somente em Omni Flash, oito segundos, um unico resultado por V.
5. Iniciar somente o primeiro lote de no maximo sete codigos V. Variacoes pertencem ao codigo;
   o teto e de codigos, nao uma autorizacao para iniciar codigos adicionais por vaga liberada.
6. Esperar todos os codigos e variacoes desse lote. Nao preencher vagas com o lote seguinte.
7. Informar concluidos, falhas e pendentes. Se houver pendentes, parar e aguardar `prossiga`.
8. Mesmo quando o lote terminar, esperar `prossiga` para iniciar o proximo lote.
9. Ao retomar, executar somente o trabalho pendente autorizado. Nunca reiniciar um V concluido
   sem pedido explicito. Distinguir a variacao que falhou das que ja foram concluidas.
10. Se a interface nao permitir a configuracao requerida, informar a limitacao antes de mudar
    modelo, prioridade, quantidade, duracao ou modo de referencia.

A fala e literal. A acao continua o estado inicial da imagem. Manter camera e som indicados,
sem adicionar musica, legenda, traducao ou texto auxiliar por conta propria.

### Fechamento

Relatar arquivos gerados por avatar, K/V e variacao, com pendencias explicitas. Geracao de um
avatar nao conclui a fila inteira. Entrega de prompts, midia gerada, montagem e publicacao sao
marcos diferentes. Nunca declarar publicacao ou resultado comercial pela existencia de assets.
```

Checklist de envio: 33/33 aprovados (N/A: A1, A2, A4, A7, A10 fiéis ao modelo orgânico; C3 sem segunda pessoa; C4 celular no tripé, sem selfie na mão; C6 sem cena atuada; C7 sem motion control)

Ficha: 2/2 K conferidos contra o frame do modelo, placar 14/14 em cada (`FICHA_FRAMES.md`, GATE_VISUAL Parte 6)

## Anexos e mapa

- **Âncora Walt Hensley:** `producao/_ancoras/walt_hensley_ancora.jpg` no K01 e no K02.
- **No K01**, anexar também `input/frames_modelo/K01_modelo.png`; **no K02**, `input/frames_modelo/K02_modelo.png`. Os dois só como composição.

```text
MAPA K/V
V01: K01
V02: K02
V03: K02
V04: K02
V05: K02
V06: K02
V07: K02
V08: K02
```

## 2. PROMPTS DE IMAGEM

### K01 · T1, embaralhando o baralho de tarô colado na lente · anexar ÂNCORA + FRAME DO MODELO

```text
K01
{
  "format": "IMPORTANT: THIS IS IPHONE FOOTAGE. Vertical 9:16.",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "reference_use": "Use the first attached image only for Walt Hensley's exact identity, wardrobe, jewelry and own setting. Use the second attached image only as a composition reference for the camera position, framing, hand position and the way the deck is held; do not copy its person, clothes, grey wall, framed art or on-screen text.",
  "identity_main": "The exact fictional AI character Walt Hensley, explicitly male: white American man around fifty-eight, long grey-white beard down to mid-chest, grey moustache, grey hair combed back short on the sides, sun-weathered skin with freckles and deep crow's feet, light grey eyes, both forearms covered in faded traditional American tattoos with no lettering, a swallow and a red rose on the left forearm.",
  "wardrobe": "Black leather vest over a heather grey crew-neck T-shirt and dark blue jeans.",
  "scene": "His own American front porch with grey weathered wooden siding, the same lived-in porch as the reference, unchanged. He sits in his old wooden rocking chair; behind him the siding with the framed astrological chart and a small wooden crucifix, and at the right a small American flag on the porch post against the overcast sky, discreet but visible and in focus.",
  "prop": "The only object is a standard-size tarot deck with matching card backs printed with a green leafy pattern and small lilac flowers, pale cream card edges; only the card backs are visible, never the card faces, in his weathered hands with faded tattoos on the forearms, caught mid-shuffle: the tarot deck split into two stacks, one stack in each hand, the top stack lifted and tilted toward the lens.",
  "posture": "Walt Hensley sits facing the lens, both forearms raised in front of his body, shuffling the tarot deck right in front of the phone, looking straight into the lens.",
  "composition": "The hands and the tarot deck split into two stacks are in the bottom center of the frame, pushed toward the lens, about 12 inches from the lens, taking up about 25 percent of the frame and touching the bottom edge, closer to the camera than his face, nothing else competing with them. His face sits in the upper middle of the frame with a little headroom, his chest in the middle, the setting behind in the top third, framed from the top of the head to the waist. Nothing else is in the foreground. The background is reduced by framing, never by blur.",
  "camera": "phone fixed on a small tripod at chest height about two feet away, 1x front lens, straight on, pointing very slightly upward, fixed",
  "lighting": "Overcast sky with visible cloud texture, never white or blown out, neutral daylight, soft even light on the face and hands with no harsh shadows.",
  "state": "Start frame: Walt Hensley looks into the lens, caught mid-sentence, lips naturally parted, calm and confident expression, the hands in motion mid-shuffle.",
  "realism": "Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday reality, background fully in focus, everything in sharp focus, no AI polish, no beauty smoothing.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no studio, no plastic-looking human skin, no extra fingers, no third hand, no supernatural lighting, no blur, no bokeh, no artificial lighting, no warm orange color cast, no yellow tint on the skin, no golden glow, no golden hour light, no sunset, no lamp glow, no de-aging, no beauty smoothing, no visible phone, no HDR, no cinematic lighting, no second person in frame, no card faces showing, no loose cards falling, no other objects in the hands, no standing pose"
}
```

### K02 · T2 a T8, baralho de tarô fechado nas duas mãos colado na lente · anexar ÂNCORA + FRAME DO MODELO

```text
K02
{
  "format": "IMPORTANT: THIS IS IPHONE FOOTAGE. Vertical 9:16.",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "reference_use": "Use the first attached image only for Walt Hensley's exact identity, wardrobe, jewelry and own setting. Use the second attached image only as a composition reference for the camera position, framing, hand position and the way the deck is held; do not copy its person, clothes, grey wall, framed art or on-screen text.",
  "identity_main": "The exact fictional AI character Walt Hensley, explicitly male: white American man around fifty-eight, long grey-white beard down to mid-chest, grey moustache, grey hair combed back short on the sides, sun-weathered skin with freckles and deep crow's feet, light grey eyes, both forearms covered in faded traditional American tattoos with no lettering, a swallow and a red rose on the left forearm.",
  "wardrobe": "Black leather vest over a heather grey crew-neck T-shirt and dark blue jeans.",
  "scene": "His own American front porch with grey weathered wooden siding, the same lived-in porch as the reference, unchanged. He sits in his old wooden rocking chair; behind him the siding with the framed astrological chart and a small wooden crucifix, and at the right a small American flag on the porch post against the overcast sky, discreet but visible and in focus.",
  "prop": "The only object is a standard-size tarot deck with matching card backs printed with a green leafy pattern and small lilac flowers, pale cream card edges; only the card backs are visible, never the card faces, in his weathered hands with faded tattoos on the forearms: the closed tarot deck squared and held in both hands, the fingers wrapped around it, the card backs angled toward the lens.",
  "posture": "Walt Hensley sits facing the lens, both forearms raised in front of his body, holding the closed tarot deck in front of his chest, looking straight into the lens.",
  "composition": "The hands and the closed tarot deck are in the bottom center of the frame, pushed toward the lens, about 12 inches from the lens, taking up about 20 percent of the frame and touching the bottom edge, closer to the camera than his face, nothing else competing with them. His face sits in the upper middle of the frame with a little headroom, his chest in the middle, the setting behind in the top third, framed from the top of the head to the waist. Nothing else is in the foreground. The background is reduced by framing, never by blur.",
  "camera": "phone fixed on a small tripod at chest height about two feet away, 1x front lens, straight on, pointing very slightly upward, fixed",
  "lighting": "Overcast sky with visible cloud texture, never white or blown out, neutral daylight, soft even light on the face and hands with no harsh shadows.",
  "state": "Start frame: Walt Hensley looks into the lens, caught mid-sentence, lips naturally parted, serious and confident expression, the hands still around the deck.",
  "realism": "Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday reality, background fully in focus, everything in sharp focus, no AI polish, no beauty smoothing.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no studio, no plastic-looking human skin, no extra fingers, no third hand, no supernatural lighting, no blur, no bokeh, no artificial lighting, no warm orange color cast, no yellow tint on the skin, no golden glow, no golden hour light, no sunset, no lamp glow, no de-aging, no beauty smoothing, no visible phone, no HDR, no cinematic lighting, no second person in frame, no card faces showing, no loose cards falling, no other objects in the hands, no standing pose"
}
```

## 3. PROMPTS DE VÍDEO (um bloco por V)

### V01 · T1 · frame inicial = a imagem escolhida do K01

```text
V01
o avatar Walt Hensley (homem) fala em inglês com sotaque americano do Tennessee, voz masculina grave, devagar e gentil de um homem de cinquenta e oito anos do Tennessee, em tom de conversa de quem grava um vídeo no celular para os seguidores, natural, próximo e confiante, calmo e confiante, quase em segredo, no mesmo ritmo do vídeo modelo, a seguinte frase: "I don't know your name, but if this video found you on October 1st, 2nd or 3rd, it's because it was 100% meant for you."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Walt Hensley embaralha o baralho de tarô sem parar, cortando e juntando os dois montes com as duas mãos perto da lente, e fala olhando para a lente.

câmera: celular fixo num tripé na altura do peito, sem movimento

som ambiente: varanda tranquila, leve vento e passarinhos ao longe, o leve som das cartas, sem música
```

### V02 · T2 · frame inicial = a imagem escolhida do K02

```text
V02
o avatar Walt Hensley (homem) fala em inglês com sotaque americano do Tennessee, voz masculina grave, devagar e gentil de um homem de cinquenta e oito anos do Tennessee, em tom de conversa de quem grava um vídeo no celular para os seguidores, natural, próximo e confiante, sério, em tom de aviso baixo, no mesmo ritmo do vídeo modelo, a seguinte frase: "Keep this between us after watching. Say nothing to anyone. If this video found you today, the universe placed it on your screen."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Walt Hensley segura o baralho de tarô fechado com as duas mãos na frente do peito, ajeitando as cartas de leve, e fala olhando para a lente.

câmera: celular fixo num tripé na altura do peito, sem movimento

som ambiente: varanda tranquila, leve vento e passarinhos ao longe, o leve som das cartas, sem música
```

### V03 · T3 · frame inicial = a imagem escolhida do K02

```text
V03
o avatar Walt Hensley (homem) fala em inglês com sotaque americano do Tennessee, voz masculina grave, devagar e gentil de um homem de cinquenta e oito anos do Tennessee, em tom de conversa de quem grava um vídeo no celular para os seguidores, natural, próximo e confiante, firme, em tom de alerta, no mesmo ritmo do vídeo modelo, a seguinte frase: "If you ignore this lucky video, you will remain unlucky for the next six months."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Walt Hensley segura o baralho de tarô fechado com as duas mãos na frente do peito, ajeitando as cartas de leve, e fala olhando para a lente.

câmera: celular fixo num tripé na altura do peito, sem movimento

som ambiente: varanda tranquila, leve vento e passarinhos ao longe, o leve som das cartas, sem música
```

### V04 · T4 · frame inicial = a imagem escolhida do K02

```text
V04
o avatar Walt Hensley (homem) fala em inglês com sotaque americano do Tennessee, voz masculina grave, devagar e gentil de um homem de cinquenta e oito anos do Tennessee, em tom de conversa de quem grava um vídeo no celular para os seguidores, natural, próximo e confiante, animado e confiante, no mesmo ritmo do vídeo modelo, a seguinte frase: "However, if you send it to yourself right now, mark the date, October 3rd, 2026 is gonna be your luckiest day in history."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Walt Hensley segura o baralho de tarô fechado com as duas mãos na frente do peito, ajeitando as cartas de leve, e fala olhando para a lente.

câmera: celular fixo num tripé na altura do peito, sem movimento

som ambiente: varanda tranquila, leve vento e passarinhos ao longe, o leve som das cartas, sem música
```

### V05 · T5 · frame inicial = a imagem escolhida do K02

```text
V05
o avatar Walt Hensley (homem) fala em inglês com sotaque americano do Tennessee, voz masculina grave, devagar e gentil de um homem de cinquenta e oito anos do Tennessee, em tom de conversa de quem grava um vídeo no celular para os seguidores, natural, próximo e confiante, caloroso, depois sério no aviso, no mesmo ritmo do vídeo modelo, a seguinte frase: "There is wealth and victory that is already waiting for you. But this is the final warning, miss it and the blessing reverses."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Walt Hensley segura o baralho de tarô fechado com as duas mãos, abre uma das mãos num gesto curto enquanto fala e volta a segurar o baralho.

câmera: celular fixo num tripé na altura do peito, sem movimento

som ambiente: varanda tranquila, leve vento e passarinhos ao longe, o leve som das cartas, sem música
```

### V06 · T6 · frame inicial = a imagem escolhida do K02

```text
V06
o avatar Walt Hensley (homem) fala em inglês com sotaque americano do Tennessee, voz masculina grave, devagar e gentil de um homem de cinquenta e oito anos do Tennessee, em tom de conversa de quem grava um vídeo no celular para os seguidores, natural, próximo e confiante, firme, em ritmo de instrução, no mesmo ritmo do vídeo modelo, a seguinte frase: "Three seals to claim it. Like this video, save this video, share this with one person."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Walt Hensley segura o baralho de tarô fechado com as duas mãos na frente do peito, ajeitando as cartas de leve, e fala olhando para a lente.

câmera: celular fixo num tripé na altura do peito, sem movimento

som ambiente: varanda tranquila, leve vento e passarinhos ao longe, o leve som das cartas, sem música
```

### V07 · T7 · frame inicial = a imagem escolhida do K02

```text
V07
o avatar Walt Hensley (homem) fala em inglês com sotaque americano do Tennessee, voz masculina grave, devagar e gentil de um homem de cinquenta e oito anos do Tennessee, em tom de conversa de quem grava um vídeo no celular para os seguidores, natural, próximo e confiante, firme, depois animado, no mesmo ritmo do vídeo modelo, a seguinte frase: "Then comment 222 so it gets tied to your name. If you sealed it correctly, your good news arrives in 33 minutes."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Walt Hensley segura o baralho de tarô fechado com as duas mãos na frente do peito, ajeitando as cartas de leve, e fala olhando para a lente.

câmera: celular fixo num tripé na altura do peito, sem movimento

som ambiente: varanda tranquila, leve vento e passarinhos ao longe, o leve som das cartas, sem música
```

### V08 · T8 · frame inicial = a imagem escolhida do K02

```text
V08
o avatar Walt Hensley (homem) fala em inglês com sotaque americano do Tennessee, voz masculina grave, devagar e gentil de um homem de cinquenta e oito anos do Tennessee, em tom de conversa de quem grava um vídeo no celular para os seguidores, natural, próximo e confiante, próximo e urgente, no mesmo ritmo do vídeo modelo, a seguinte frase: "Now tap my profile picture and check my stories immediately. The other half of this sign is already waiting for you there."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Walt Hensley segura o baralho de tarô fechado com as duas mãos na frente do peito e inclina um pouco a cabeça para a lente enquanto fala.

câmera: celular fixo num tripé na altura do peito, sem movimento

som ambiente: varanda tranquila, leve vento e passarinhos ao longe, o leve som das cartas, sem música
```

## 4. Montagem no CapCut

1. Clipes numerados na ordem: V01 a V08.
2. Zero tempo morto: todo clipe começa já falando; cortar logo depois da última palavra. Isolate Voice / Keep Vocal no áudio. V02 a V08 saem do mesmo frame (K02), então a troca de clipe vira jump cut no mesmo enquadramento, a gramática do próprio formato orgânico.
3. Tarja branca fixa no topo, só no V01: "If you see this video on Oct 1st, 2nd or 3rd...".
4. Legenda branca em negrito, 2 a 3 palavras por vez, no meio do quadro, do V01 ao V08, igual ao modelo.
5. Do V02 ao V08, "1111", "888" e "222" pequenos à direita do quadro, na altura da parede.
6. No V08, seta vermelha para baixo à esquerda (onde fica a foto de perfil), em "tap my profile picture".
7. Sem Voice Changer: a voz vem do prompt de cada V.
8. Música só depois do gancho (a partir do V02), baixa, entre -19 e -20 dB, fora da biblioteca do TikTok.
9. Rótulo pequeno `AI-generated` num canto do vídeo.
10. Postar entre 1º e 3 de outubro de 2026: as datas estão cravadas na fala e na tarja.

## 5. Transcrição final por take

| Take | English | Português |
|---|---|---|
| T1 | I don't know your name, but if this video found you on October 1st, 2nd or 3rd, it's because it was 100% meant for you. | Eu não sei o seu nome, mas se este vídeo te encontrou no dia 1º, 2 ou 3 de outubro, é porque ele era 100% pra você. |
| T2 | Keep this between us after watching. Say nothing to anyone. If this video found you today, the universe placed it on your screen. | Depois de assistir, isto fica entre nós. Não diga nada a ninguém. Se este vídeo te encontrou hoje, foi o universo que o colocou na sua tela. |
| T3 | If you ignore this lucky video, you will remain unlucky for the next six months. | Se você ignorar este vídeo da sorte, vai continuar sem sorte pelos próximos seis meses. |
| T4 | However, if you send it to yourself right now, mark the date, October 3rd, 2026 is gonna be your luckiest day in history. | Mas, se você mandar ele pra você mesma agora, marque a data: 3 de outubro de 2026 vai ser o dia de mais sorte da sua história. |
| T5 | There is wealth and victory that is already waiting for you. But this is the final warning, miss it and the blessing reverses. | Tem riqueza e vitória que já estão te esperando. Mas este é o último aviso: se deixar passar, a bênção se inverte. |
| T6 | Three seals to claim it. Like this video, save this video, share this with one person. | Três selos para reivindicar. Curta este vídeo, salve este vídeo, compartilhe com uma pessoa. |
| T7 | Then comment 222 so it gets tied to your name. If you sealed it correctly, your good news arrives in 33 minutes. | Depois comente 222 para isso ficar ligado ao seu nome. Se você selou do jeito certo, a sua boa notícia chega em 33 minutos. |
| T8 | Now tap my profile picture and check my stories immediately. The other half of this sign is already waiting for you there. | Agora toque na minha foto de perfil e veja os meus stories imediatamente. A outra metade deste sinal já está te esperando lá. |

## 6. Roteiro final em inglês

1. I don't know your name, but if this video found you on October 1st, 2nd or 3rd, it's because it was 100% meant for you.
2. Keep this between us after watching. Say nothing to anyone. If this video found you today, the universe placed it on your screen.
3. If you ignore this lucky video, you will remain unlucky for the next six months.
4. However, if you send it to yourself right now, mark the date, October 3rd, 2026 is gonna be your luckiest day in history.
5. There is wealth and victory that is already waiting for you. But this is the final warning, miss it and the blessing reverses.
6. Three seals to claim it. Like this video, save this video, share this with one person.
7. Then comment 222 so it gets tied to your name. If you sealed it correctly, your good news arrives in 33 minutes.
8. Now tap my profile picture and check my stories immediately. The other half of this sign is already waiting for you there.

I don't know your name, but if this video found you on October 1st, 2nd or 3rd, it's because it was 100% meant for you. Keep this between us after watching. Say nothing to anyone. If this video found you today, the universe placed it on your screen. If you ignore this lucky video, you will remain unlucky for the next six months. However, if you send it to yourself right now, mark the date, October 3rd, 2026 is gonna be your luckiest day in history. There is wealth and victory that is already waiting for you. But this is the final warning, miss it and the blessing reverses. Three seals to claim it. Like this video, save this video, share this with one person. Then comment 222 so it gets tied to your name. If you sealed it correctly, your good news arrives in 33 minutes. Now tap my profile picture and check my stories immediately. The other half of this sign is already waiting for you there.
