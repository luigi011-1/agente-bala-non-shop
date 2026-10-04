# ENTREGA | Avery Knox | Auraly Oração Repetir

Produção `auraly_oracao_repetir` · Ângulo 3 · GROWTH · vídeo modelo de pessoa real (orgânico) · rodada de VALIDAÇÃO · perfil AURALY

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

Roster Auraly: Walt Hensley, Darlene Pruitt, Lorraine Vance e Morgan Vance (desde 2026-09-30). A referencia de cada um e a anchor
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

Checklist de envio: 33/33 aprovados (N/A: A1, A2, A4, A7, A10 fiéis ao modelo orgânico; C3 sem segunda pessoa; C4 celular apoiado, sem selfie na mão; C6 sem cena atuada; C7 sem motion control)

Ficha: 3/3 K conferidos contra o frame do modelo, placar 14/14 em cada (`FICHA_FRAMES.md`, GATE_VISUAL Parte 6)

## Anexos e mapa

- **Âncora Avery Knox:** `/Users/macbookairm2/Desktop/AVATARES/avatares appyon/avery.knox_ .jpeg` no K01, no K02 e no K03.
- Em cada K, anexar também o frame do modelo do mesmo código (`input/frames_modelo/K01_modelo.png`, `K02_modelo.png`, `K03_modelo.png`), só como composição.

```text
MAPA K/V
V01: K01
V02: K02
V03: K02
V04: K02
V05: K03
V06: K03
V07: K03
V08: K03
```

## 2. PROMPTS DE IMAGEM

### K01 · T1, baralho de tarô dourado nas duas mãos colado na lente · anexar ÂNCORA + FRAME DO MODELO

```text
K01
{
  "format": "IMPORTANT: THIS IS IPHONE FOOTAGE. Vertical 9:16.",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "reference_use": "Use the first attached image only for Avery Knox's exact identity, wardrobe, jewelry and own setting. Use the second attached image only as a composition reference for the camera position, framing and hand position; do not copy its person, clothes, sofa, wall or on-screen text.",
  "identity_main": "The exact fictional AI character Avery Knox: white American woman around fifty-six from Texas, voluminous shaggy layered platinum-blonde hair with visible dark roots, brown eyes, fair skin with crow's feet and fine lines, everyday makeup with defined brows, mascara and pink lipstick.",
  "wardrobe": "White long-sleeve button-up shirt with the cuffs loosely rolled, blue jeans, a large turquoise and silver squash-blossom necklace, several big turquoise rings on the fingers of both hands and a silver cuff bracelet set with turquoise.",
  "scene": "Her own rustic American kitchen with knotty pine wood-paneled walls, the same lived-in kitchen as the reference, unchanged. She sits at her wooden kitchen island; behind her the pine wall with a framed astrological chart and a small wooden crucifix, and the open wooden shelves by the window with glass jars and a small American flag, discreet but visible and in focus.",
  "prop": "The only object is a gold tarot deck with shiny gold foil card edges and dark antique-gold card backs printed with a fine black line drawing of a sun and stars, in her fair hands with big turquoise rings on several fingers, caught mid-pass: most of the deck held in one hand with the gold foil card edges toward the lens and a small packet of cards lifted off the top by the other hand; only the card backs are visible.",
  "posture": "Avery Knox sits at her wooden kitchen island, facing the lens, both forearms raised in front of her body, passing the tarot cards right in front of the phone.",
  "composition": "The hands and the gold tarot deck are in the bottom center of the frame, pushed toward the lens, about 14 inches from the lens, taking up about 30 percent of the frame and touching the bottom edge, closer to the camera than her face, nothing else competing with them. Her face sits in the upper middle of the frame with a little headroom, her chest in the middle, the setting behind in the top third, framed from the top of the head to the waist. Nothing else is in the foreground. The background is reduced by framing, never by blur.",
  "camera": "phone propped on the wooden kitchen island at chest height about two feet away, 1x front lens, straight on, pointing slightly upward, fixed",
  "lighting": "Neutral overcast daylight from a window, the outside clearly visible through the window, never white or blown out, soft even light on the face and hands with no harsh shadows.",
  "state": "Start frame: Avery Knox glances down at the deck, caught mid-sentence, lips naturally parted, calm and focused expression, the hands in motion.",
  "realism": "Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday reality, background fully in focus, everything in sharp focus, no AI polish, no beauty smoothing.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no studio, no plastic-looking human skin, no extra fingers, no third hand, no supernatural lighting, no blur, no bokeh, no artificial lighting, no warm orange color cast, no yellow tint on the skin, no golden glow, no golden hour light, no sunset, no lamp glow, no de-aging, no beauty smoothing, no visible phone, no HDR, no cinematic lighting, no second person in frame, no standing pose, no loose cards falling, no card faces showing, no other objects in the hands"
}
```

### K02 · T2 a T4, a carta da Roda da Fortuna de pé colada na lente · anexar ÂNCORA + FRAME DO MODELO

```text
K02
{
  "format": "IMPORTANT: THIS IS IPHONE FOOTAGE. Vertical 9:16.",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "reference_use": "Use the first attached image only for Avery Knox's exact identity, wardrobe, jewelry and own setting. Use the second attached image only as a composition reference for the camera position, framing and hand position; do not copy its person, clothes, sofa, wall or on-screen text.",
  "identity_main": "The exact fictional AI character Avery Knox: white American woman around fifty-six from Texas, voluminous shaggy layered platinum-blonde hair with visible dark roots, brown eyes, fair skin with crow's feet and fine lines, everyday makeup with defined brows, mascara and pink lipstick.",
  "wardrobe": "White long-sleeve button-up shirt with the cuffs loosely rolled, blue jeans, a large turquoise and silver squash-blossom necklace, several big turquoise rings on the fingers of both hands and a silver cuff bracelet set with turquoise.",
  "scene": "Her own rustic American kitchen with knotty pine wood-paneled walls, the same lived-in kitchen as the reference, unchanged. She sits at her wooden kitchen island; behind her the pine wall with a framed astrological chart and a small wooden crucifix, and the open wooden shelves by the window with glass jars and a small American flag, discreet but visible and in focus.",
  "prop": "The only object is the Wheel of Fortune tarot card from the same gold deck: a shiny gold foil card with a metallic gold border and a saturated illustration of a large orange and red wheel in the center over teal clouds with a red ribbon, in one of her fair hands with big turquoise rings on several fingers, held upright by its top corner between the thumb and fingers, the illustrated face turned straight to the lens; the other hand rests out of frame and the rest of the deck is out of frame.",
  "posture": "Avery Knox sits at her wooden kitchen island, facing the lens, one forearm raised, holding the card up in front of her chest, looking straight into the lens.",
  "composition": "The card and the hand holding it are in the lower center of the frame, pushed toward the lens, about 12 inches from the lens, taking up about 25 percent of the frame, the bottom of the card near the bottom edge, closer to the camera than her face, nothing else competing with it. Her face sits in the upper middle of the frame with a little headroom, her chest in the middle, the setting behind in the top third, framed from the top of the head to the waist. Nothing else is in the foreground. The background is reduced by framing, never by blur.",
  "camera": "phone propped on the wooden kitchen island at chest height about two feet away, 1x front lens, straight on, pointing slightly upward, fixed",
  "lighting": "Neutral overcast daylight from a window, the outside clearly visible through the window, never white or blown out, soft even light on the face and hands with no harsh shadows.",
  "state": "Start frame: Avery Knox looks straight into the lens, caught mid-sentence, lips naturally parted, bright and confident expression.",
  "realism": "Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday reality, background fully in focus, everything in sharp focus, no AI polish, no beauty smoothing.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no studio, no plastic-looking human skin, no extra fingers, no third hand, no supernatural lighting, no blur, no bokeh, no artificial lighting, no warm orange color cast, no yellow tint on the skin, no golden glow, no golden hour light, no sunset, no lamp glow, no de-aging, no beauty smoothing, no visible phone, no HDR, no cinematic lighting, no second person in frame, no standing pose, no loose cards falling, no second card, no other cards in frame, no other objects in the hands"
}
```

### K03 · T5 a T8, a mão espalmada no coração, a carta na borda do quadro · anexar ÂNCORA + FRAME DO MODELO

```text
K03
{
  "format": "IMPORTANT: THIS IS IPHONE FOOTAGE. Vertical 9:16.",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "reference_use": "Use the first attached image only for Avery Knox's exact identity, wardrobe, jewelry and own setting. Use the second attached image only as a composition reference for the camera position, framing and hand position; do not copy its person, clothes, sofa, wall or on-screen text.",
  "identity_main": "The exact fictional AI character Avery Knox: white American woman around fifty-six from Texas, voluminous shaggy layered platinum-blonde hair with visible dark roots, brown eyes, fair skin with crow's feet and fine lines, everyday makeup with defined brows, mascara and pink lipstick.",
  "wardrobe": "White long-sleeve button-up shirt with the cuffs loosely rolled, blue jeans, a large turquoise and silver squash-blossom necklace, several big turquoise rings on the fingers of both hands and a silver cuff bracelet set with turquoise.",
  "scene": "Her own rustic American kitchen with knotty pine wood-paneled walls, the same lived-in kitchen as the reference, unchanged. She sits at her wooden kitchen island; behind her the pine wall with a framed astrological chart and a small wooden crucifix, and the open wooden shelves by the window with glass jars and a small American flag, discreet but visible and in focus.",
  "prop": "In her fair hands with big turquoise rings on several fingers: one hand pressed flat over her heart on the chest, fingers relaxed; the other hand holds the gold Wheel of Fortune card low at the right edge of the frame, partly cut off by the frame edge. The card is the Wheel of Fortune tarot card from the same gold deck: a shiny gold foil card with a metallic gold border and a saturated illustration of a large orange and red wheel in the center over teal clouds with a red ribbon.",
  "posture": "Avery Knox sits at her wooden kitchen island, facing the lens, upright and still, one hand pressed flat over her heart, looking softly into the lens.",
  "composition": "The hand pressed flat over the heart is in the center of the frame on the chest, about 20 inches from the lens, taking up about 10 percent of the frame, closer to the camera than her face; the card is only a sliver at the right edge, partly cut off by the frame edge. Her face sits in the upper middle of the frame with a little headroom, her chest in the middle, the setting behind in the top third, framed from the top of the head to the waist. Nothing else is in the foreground. The background is reduced by framing, never by blur.",
  "camera": "phone propped on the wooden kitchen island at chest height about two feet away, 1x front lens, straight on, pointing slightly upward, fixed",
  "lighting": "Neutral overcast daylight from a window, the outside clearly visible through the window, never white or blown out, soft even light on the face and hands with no harsh shadows.",
  "state": "Start frame: Avery Knox looks softly into the lens, caught mid-sentence, lips naturally parted, calm and sincere expression, as if saying a prayer.",
  "realism": "Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday reality, background fully in focus, everything in sharp focus, no AI polish, no beauty smoothing.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no studio, no plastic-looking human skin, no extra fingers, no third hand, no supernatural lighting, no blur, no bokeh, no artificial lighting, no warm orange color cast, no yellow tint on the skin, no golden glow, no golden hour light, no sunset, no lamp glow, no de-aging, no beauty smoothing, no visible phone, no HDR, no cinematic lighting, no second person in frame, no standing pose, no loose cards falling, no phone screen overlay, no app interface, no other objects in the hands"
}
```

## 3. PROMPTS DE VÍDEO (um bloco por V)

### V01 · T1 · frame inicial = a imagem escolhida do K01

```text
V01
a avatar Avery Knox (mulher) fala em inglês com sotaque americano texano carregado, voz feminina média, levemente rouca e calorosa de uma texana de cinquenta e seis anos, em tom de conversa de quem grava um vídeo no celular para os seguidores, natural, próximo e confiante, calma e direta, como quem dá uma ordem baixinha, no mesmo ritmo do vídeo modelo, a seguinte frase: "Do not move that finger to the person that is watching this. You are about to have the best October."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Avery Knox segura o baralho de tarô dourado com as duas mãos perto da lente, passa algumas cartas de uma mão para a outra, puxa uma única carta e a ergue de pé, colada na lente, com a face virada para a câmera, e levanta o olhar para a lente enquanto fala.

câmera: celular apoiado na altura do peito, fixo, sem movimento

som ambiente: cozinha residencial silenciosa, sem música
```

### V02 · T2 · frame inicial = a imagem escolhida do K02

```text
V02
a avatar Avery Knox (mulher) fala em inglês com sotaque americano texano carregado, voz feminina média, levemente rouca e calorosa de uma texana de cinquenta e seis anos, em tom de conversa de quem grava um vídeo no celular para os seguidores, natural, próximo e confiante, animada e segura, no mesmo ritmo do vídeo modelo, a seguinte frase: "I mean the best month of the entire year, and it is not random if you are seeing this."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Avery Knox segura a carta dourada de pé, colada na lente, com uma mão e, em "not random", ergue o dedo indicador da outra mão.

câmera: celular apoiado na altura do peito, fixo, sem movimento

som ambiente: cozinha residencial silenciosa, sem música
```

### V03 · T3 · frame inicial = a imagem escolhida do K02

```text
V03
a avatar Avery Knox (mulher) fala em inglês com sotaque americano texano carregado, voz feminina média, levemente rouca e calorosa de uma texana de cinquenta e seis anos, em tom de conversa de quem grava um vídeo no celular para os seguidores, natural, próximo e confiante, em voz mais baixa, quase em segredo, no mesmo ritmo do vídeo modelo, a seguinte frase: "Okay, this keeps happening to people who claim it. So send this to yourself right now."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Avery Knox segura a carta dourada de pé na frente do peito com uma mão e gesticula de leve com a outra mão.

câmera: celular apoiado na altura do peito, fixo, sem movimento

som ambiente: cozinha residencial silenciosa, sem música
```

### V04 · T4 · frame inicial = a imagem escolhida do K02

```text
V04
a avatar Avery Knox (mulher) fala em inglês com sotaque americano texano carregado, voz feminina média, levemente rouca e calorosa de uma texana de cinquenta e seis anos, em tom de conversa de quem grava um vídeo no celular para os seguidores, natural, próximo e confiante, calorosa e convidativa, no mesmo ritmo do vídeo modelo, a seguinte frase: "Now I want you to say these words out loud with me, like a little prayer. Do it twice and see what happens."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Avery Knox baixa a carta dourada para a borda do quadro e abre a outra mão para a lente, convidando, enquanto fala.

câmera: celular apoiado na altura do peito, fixo, sem movimento

som ambiente: cozinha residencial silenciosa, sem música
```

### V05 · T5 · frame inicial = a imagem escolhida do K03

```text
V05
a avatar Avery Knox (mulher) fala em inglês com sotaque americano texano carregado, voz feminina média, levemente rouca e calorosa de uma texana de cinquenta e seis anos, em tom de conversa de quem grava um vídeo no celular para os seguidores, natural, próximo e confiante, devagar e sincera, a voz um pouco mais baixa, com uma pausa curta no fim de cada frase, como numa oração, no mesmo ritmo do vídeo modelo, a seguinte frase: "I have decided that everything works out for me. I have decided that I deserve good things. I am the exception."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Avery Knox mantém a mão espalmada sobre o coração, a carta baixa na outra mão, e fala devagar olhando para a lente.

câmera: celular apoiado na altura do peito, fixo, sem movimento

som ambiente: cozinha residencial silenciosa, sem música
```

### V06 · T6 · frame inicial = a imagem escolhida do K03

```text
V06
a avatar Avery Knox (mulher) fala em inglês com sotaque americano texano carregado, voz feminina média, levemente rouca e calorosa de uma texana de cinquenta e seis anos, em tom de conversa de quem grava um vídeo no celular para os seguidores, natural, próximo e confiante, devagar e serena, a voz um pouco mais baixa, com uma pausa curta no fim de cada frase, como numa oração, no mesmo ritmo do vídeo modelo, a seguinte frase: "The more I relax, the more I receive. I am simply deciding that when I wake up tomorrow, I am in my luckiest timeline."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Avery Knox mantém a mão espalmada sobre o coração e fala devagar olhando para a lente; na última frase fecha os olhos por um instante e abre de novo.

câmera: celular apoiado na altura do peito, fixo, sem movimento

som ambiente: cozinha residencial silenciosa, sem música
```

### V07 · T7 · frame inicial = a imagem escolhida do K03

```text
V07
a avatar Avery Knox (mulher) fala em inglês com sotaque americano texano carregado, voz feminina média, levemente rouca e calorosa de uma texana de cinquenta e seis anos, em tom de conversa de quem grava um vídeo no celular para os seguidores, natural, próximo e confiante, sorridente e leve, no mesmo ritmo do vídeo modelo, a seguinte frase: "I want you to save this, and I want you to come back in seven days and just tell me what happens."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Avery Knox tira a mão do peito, sorri, junta o polegar e o indicador num gesto leve e ergue o dedo indicador em "seven days".

câmera: celular apoiado na altura do peito, fixo, sem movimento

som ambiente: cozinha residencial silenciosa, sem música
```

### V08 · T8 · frame inicial = a imagem escolhida do K03

```text
V08
a avatar Avery Knox (mulher) fala em inglês com sotaque americano texano carregado, voz feminina média, levemente rouca e calorosa de uma texana de cinquenta e seis anos, em tom de conversa de quem grava um vídeo no celular para os seguidores, natural, próximo e confiante, próxima e animada, no mesmo ritmo do vídeo modelo, a seguinte frase: "Comment 222 right now so this gets tied to your name, and follow me so you don't miss what comes next."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Avery Knox sorri, aponta de leve para baixo da tela em "Comment 222" e, no fim, ergue a carta dourada para a lente.

câmera: celular apoiado na altura do peito, fixo, sem movimento

som ambiente: cozinha residencial silenciosa, sem música
```

## 4. Montagem no CapCut

1. Clipes numerados na ordem: V01 a V08.
2. Zero tempo morto: todo clipe começa já falando; cortar logo depois da última palavra. Isolate Voice / Keep Vocal no áudio. V02 a V04 saem do K02 e V05 a V08 do K03, então a troca de clipe vira jump cut no mesmo enquadramento, a gramática do próprio formato orgânico.
3. Tarja branca fixa no topo, do V01 ao V08: "💫 you are about to have THE BEST OCTOBER of your life 💫".
4. Legenda branca pequena no meio de baixo, a fala inteira, do V01 ao V08, igual ao modelo.
5. No V05 e no V06 (a oração), um cartão escuro translúcido no centro do peito, no lugar do print do app do modelo, com as linhas da oração em serifa branca e a linha que está sendo falada em destaque, para quem assiste ler e repetir junto. Sem nome nem ícone de app.
6. Sem Voice Changer: a voz vem do prompt de cada V.
7. Música só depois do gancho (a partir do V02), baixa, entre -19 e -20 dB, fora da biblioteca do TikTok; baixar mais ainda na oração (V05 e V06) para a voz ficar na frente.
8. Rótulo pequeno `AI-generated` num canto do vídeo.
9. Postar em outubro de 2026: "the best October" está na fala e na tarja.

## 5. Transcrição final por take

| Take | English | Português |
|---|---|---|
| T1 | Do not move that finger to the person that is watching this. You are about to have the best October. | Não mexa esse dedo, você que está assistindo isto. Você está prestes a ter o melhor outubro. |
| T2 | I mean the best month of the entire year, and it is not random if you are seeing this. | Quer dizer, o melhor mês do ano inteiro, e não é por acaso que você está vendo isto. |
| T3 | Okay, this keeps happening to people who claim it. So send this to yourself right now. | Isso fica acontecendo com quem reivindica. Então mande isto pra você mesma agora. |
| T4 | Now I want you to say these words out loud with me, like a little prayer. Do it twice and see what happens. | Agora eu quero que você diga estas palavras em voz alta comigo, como uma pequena oração. Faça duas vezes e veja o que acontece. |
| T5 | I have decided that everything works out for me. I have decided that I deserve good things. I am the exception. | Eu decidi que tudo dá certo pra mim. Eu decidi que eu mereço coisas boas. Eu sou a exceção. |
| T6 | The more I relax, the more I receive. I am simply deciding that when I wake up tomorrow, I am in my luckiest timeline. | Quanto mais eu relaxo, mais eu recebo. Eu simplesmente decido que, quando eu acordar amanhã, eu estou na minha linha do tempo de mais sorte. |
| T7 | I want you to save this, and I want you to come back in seven days and just tell me what happens. | Eu quero que você salve isto, e quero que você volte daqui a sete dias e só me conte o que aconteceu. |
| T8 | Comment 222 right now so this gets tied to your name, and follow me so you don't miss what comes next. | Comente 222 agora pra isto ficar ligado ao seu nome, e me siga pra não perder o que vem depois. |

## 6. Roteiro final em inglês

1. Do not move that finger to the person that is watching this. You are about to have the best October.
2. I mean the best month of the entire year, and it is not random if you are seeing this.
3. Okay, this keeps happening to people who claim it. So send this to yourself right now.
4. Now I want you to say these words out loud with me, like a little prayer. Do it twice and see what happens.
5. I have decided that everything works out for me. I have decided that I deserve good things. I am the exception.
6. The more I relax, the more I receive. I am simply deciding that when I wake up tomorrow, I am in my luckiest timeline.
7. I want you to save this, and I want you to come back in seven days and just tell me what happens.
8. Comment 222 right now so this gets tied to your name, and follow me so you don't miss what comes next.

Do not move that finger to the person that is watching this. You are about to have the best October. I mean the best month of the entire year, and it is not random if you are seeing this. Okay, this keeps happening to people who claim it. So send this to yourself right now. Now I want you to say these words out loud with me, like a little prayer. Do it twice and see what happens. I have decided that everything works out for me. I have decided that I deserve good things. I am the exception. The more I relax, the more I receive. I am simply deciding that when I wake up tomorrow, I am in my luckiest timeline. I want you to save this, and I want you to come back in seven days and just tell me what happens. Comment 222 right now so this gets tied to your name, and follow me so you don't miss what comes next.
