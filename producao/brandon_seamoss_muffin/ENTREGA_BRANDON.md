# ENTREGA | holistic.brandon | Natural Rems Sea Moss Venda, muffin de cenoura

Produção `brandon_seamoss_muffin` · Ângulo 1 (Natural Rems Sea Moss) · VENDA · rodada de VALIDAÇÃO · perfil CLÁSSICO

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

Checklist de envio: 36/36 aprovados (N/A: A1, A10, A12 e A13 fiéis ao modelo na rodada de validação, sem arquivo de ganchos; C3 sem segunda pessoa; C4 sem selfie; C6 sem cena atuada; C7 sem motion control)

Ficha: 17/17 K conferidos contra o frame do modelo, placar F1 a F6 + G1 a G8 completo em cada um, com evidência literal (G2 N/A: sem céu nem janela em quadro) (`FICHA_FRAMES.md`, GATE_VISUAL Parte 6)

## Mapa de anexos

- **Todos os K:** âncora `producao/_ancoras/holistic_brandon_ancora.jpg` + frame do modelo de mesmo número (só composição).
- **K13 a K17:** também a foto do produto `producao/_ancoras/natural_rems_seamoss_produto.jpg` (só o pote da frente).
- K01 a K17 casam com V01 a V17 pelo número. Todos os V têm fala.

| Código | Take | Anexar, nesta ordem |
|---|---|---|
| K01 / V01 | T1, gancho, cenoura no ralador colada na lente | ÂNCORA HOLISTIC BRANDON `producao/_ancoras/holistic_brandon_ancora.jpg` + FRAME DO MODELO `input/frames_modelo/K01_modelo.png` (só composição) |
| K02 / V02 | T2, receita, aveia na tigela | ÂNCORA HOLISTIC BRANDON `producao/_ancoras/holistic_brandon_ancora.jpg` + FRAME DO MODELO `input/frames_modelo/K02_modelo.png` (só composição) |
| K03 / V03 | T3, receita, ovo | ÂNCORA HOLISTIC BRANDON `producao/_ancoras/holistic_brandon_ancora.jpg` + FRAME DO MODELO `input/frames_modelo/K03_modelo.png` (só composição) |
| K04 / V04 | T4, receita, mel | ÂNCORA HOLISTIC BRANDON `producao/_ancoras/holistic_brandon_ancora.jpg` + FRAME DO MODELO `input/frames_modelo/K04_modelo.png` (só composição) |
| K05 / V05 | T5, receita, canela | ÂNCORA HOLISTIC BRANDON `producao/_ancoras/holistic_brandon_ancora.jpg` + FRAME DO MODELO `input/frames_modelo/K05_modelo.png` (só composição) |
| K06 / V06 | T6, receita, massa na forma | ÂNCORA HOLISTIC BRANDON `producao/_ancoras/holistic_brandon_ancora.jpg` + FRAME DO MODELO `input/frames_modelo/K06_modelo.png` (só composição) |
| K07 / V07 | T7, resultado, muffin na mão | ÂNCORA HOLISTIC BRANDON `producao/_ancoras/holistic_brandon_ancora.jpg` + FRAME DO MODELO `input/frames_modelo/K07_modelo.png` (só composição) |
| K08 / V08 | T8, mecanismo, a aveia | ÂNCORA HOLISTIC BRANDON `producao/_ancoras/holistic_brandon_ancora.jpg` + FRAME DO MODELO `input/frames_modelo/K08_modelo.png` (só composição) |
| K09 / V09 | T9, mecanismo e a tarde lenta | ÂNCORA HOLISTIC BRANDON `producao/_ancoras/holistic_brandon_ancora.jpg` + FRAME DO MODELO `input/frames_modelo/K09_modelo.png` (só composição) |
| K10 / V10 | T10, rotina e virada | ÂNCORA HOLISTIC BRANDON `producao/_ancoras/holistic_brandon_ancora.jpg` + FRAME DO MODELO `input/frames_modelo/K10_modelo.png` (só composição) |
| K11 / V11 | T11, ponte, o sea moss | ÂNCORA HOLISTIC BRANDON `producao/_ancoras/holistic_brandon_ancora.jpg` + FRAME DO MODELO `input/frames_modelo/K11_modelo.png` (só composição) |
| K12 / V12 | T12, obstáculo, as gomas com açúcar | ÂNCORA HOLISTIC BRANDON `producao/_ancoras/holistic_brandon_ancora.jpg` + FRAME DO MODELO `input/frames_modelo/K12_modelo.png` (só composição) |
| K13 / V13 | T13, produto, o frasco sobe no nome | ÂNCORA HOLISTIC BRANDON `producao/_ancoras/holistic_brandon_ancora.jpg` + FRAME DO MODELO `input/frames_modelo/K13_modelo.png` (só composição) + FOTO DO PRODUTO `producao/_ancoras/natural_rems_seamoss_produto.jpg` (só o pote da frente) |
| K14 / V14 | T14, diferencial | ÂNCORA HOLISTIC BRANDON `producao/_ancoras/holistic_brandon_ancora.jpg` + FRAME DO MODELO `input/frames_modelo/K14_modelo.png` (só composição) + FOTO DO PRODUTO `producao/_ancoras/natural_rems_seamoss_produto.jpg` (só o pote da frente) |
| K15 / V15 | T15, prova social da coach | ÂNCORA HOLISTIC BRANDON `producao/_ancoras/holistic_brandon_ancora.jpg` + FRAME DO MODELO `input/frames_modelo/K15_modelo.png` (só composição) + FOTO DO PRODUTO `producao/_ancoras/natural_rems_seamoss_produto.jpg` (só o pote da frente) |
| K16 / V16 | T16, comment yes + follow | ÂNCORA HOLISTIC BRANDON `producao/_ancoras/holistic_brandon_ancora.jpg` + FRAME DO MODELO `input/frames_modelo/K16_modelo.png` (só composição) + FOTO DO PRODUTO `producao/_ancoras/natural_rems_seamoss_produto.jpg` (só o pote da frente) |
| K17 / V17 | T17, CTA da marca | ÂNCORA HOLISTIC BRANDON `producao/_ancoras/holistic_brandon_ancora.jpg` + FRAME DO MODELO `input/frames_modelo/K17_modelo.png` (só composição) + FOTO DO PRODUTO `producao/_ancoras/natural_rems_seamoss_produto.jpg` (só o pote da frente) |

## 2. PROMPTS DE IMAGEM (um bloco por K)

### K01 · T1, gancho, cenoura no ralador colada na lente · anexar ÂNCORA HOLISTIC BRANDON + FRAME DO MODELO

```text
K01
{
  "format": "IMPORTANT: THIS IS IPHONE FOOTAGE. Vertical 9:16.",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "reference_use": "Use the first attached image only for Brandon's exact identity, wardrobe and own garage gym with the black table. Use the second attached image only as a composition reference for the camera position, framing and the action; do not copy its person, eyeglasses, grey t-shirt, white kitchen, marble countertop, refrigerator decorations or the caption text.",
  "identity_main": "The exact fictional AI character holistic.brandon: Black mixed-race American woman around thirty, athletic and toned, medium light-brown skin with light freckles across the nose and cheeks, dark brown eyes, defined eyebrows, full lips, hair in tight cornrows that turn into long loose braids falling over both shoulders, finished with small wooden and gold beads, a black floral blackwork tattoo sleeve on her right arm, a fine line tattoo on her left inner arm and a small fine-line floral tattoo below her left collarbone.",
  "wardrobe": "Plain white ribbed tank top with nothing printed on it, loose black training shorts, a thin gold chain with a small gold cross pendant and small stud earrings.",
  "scene": "Her own garage gym: a white-painted concrete block wall behind her, a red neon sign reading TRAIN PRAY REPEAT on the wall at the left, a whiteboard with handwritten black marker reading STAY READY. STAY DISCIPLINED. on the right, and a small American flag pinned above the whiteboard, discreet but clearly visible and in focus. In front of her stands a plain matte black table she uses as a kitchen counter.",
  "prop": "In the lower foreground, a large white ceramic mixing bowl half full of bright orange finely grated carrot, with a tall stainless steel four-sided box grater standing upright inside it; her right hand presses a large peeled orange carrot against the grater blades, her left hand steadies the grater handle. Nothing else on the table.",
  "posture": "Brandon leans over the black table toward the lens, grating the carrot into the bowl.",
  "composition": "Close shot from chest height: the phone lens is about 30 centimeters from the bowl and the grater, which fill the lower 45 percent of the frame, closer to the camera than her face and larger than her head; her face and shoulders are in the upper third. The background is reduced by framing, never by blur.",
  "camera": "phone at her chest height, tilted down toward the bowl, standard 1x lens, light handheld",
  "lighting": "Neutral overcast daylight from a large window out of frame, soft even light on her face, hands and the table with no harsh shadows. The red neon glows on the wall but does not tint her skin.",
  "state": "Start frame: Brandon is caught mid-sentence, lips naturally parted, animated expression, looking straight into the lens, eyebrows raised, as if sharing a secret.",
  "realism": "Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday reality, background fully in focus, everything in sharp focus, no AI polish, no beauty smoothing.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no plastic-looking skin, no extra fingers, no third hand, no blur, no bokeh, no warm orange color cast, no yellow tint, no golden glow, no golden hour light, no sunset, no HDR, no cinematic lighting, no beauty smoothing, no visible phone, no studio, no second person, no eyeglasses, no grey t-shirt, no white kitchen cabinets, no marble countertop, no silver cross, no printed labels or lettering on the bowls, cups, grater or muffin tin"
}
```

### K02 · T2, receita, aveia na tigela · anexar ÂNCORA HOLISTIC BRANDON + FRAME DO MODELO

```text
K02
{
  "format": "IMPORTANT: THIS IS IPHONE FOOTAGE. Vertical 9:16.",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "reference_use": "Use the first attached image only for Brandon's exact identity, wardrobe and own garage gym with the black table. Use the second attached image only as a composition reference for the camera position, framing and the action; do not copy its person, eyeglasses, grey t-shirt, white kitchen, marble countertop, refrigerator decorations or the caption text.",
  "identity_main": "The exact fictional AI character holistic.brandon: Black mixed-race American woman around thirty, athletic and toned, medium light-brown skin with light freckles across the nose and cheeks, dark brown eyes, defined eyebrows, full lips, hair in tight cornrows that turn into long loose braids falling over both shoulders, finished with small wooden and gold beads, a black floral blackwork tattoo sleeve on her right arm, a fine line tattoo on her left inner arm and a small fine-line floral tattoo below her left collarbone.",
  "wardrobe": "Plain white ribbed tank top with nothing printed on it, loose black training shorts, a thin gold chain with a small gold cross pendant and small stud earrings.",
  "scene": "Her own garage gym: a white-painted concrete block wall behind her, a red neon sign reading TRAIN PRAY REPEAT on the wall at the left, a whiteboard with handwritten black marker reading STAY READY. STAY DISCIPLINED. on the right, and a small American flag pinned above the whiteboard, discreet but clearly visible and in focus. In front of her stands a plain matte black table she uses as a kitchen counter.",
  "prop": "On the black table, a large white ceramic mixing bowl half full of bright orange finely grated carrot in the lower center. Around the bowl on the black table: a clear glass measuring cup of rolled oats, two white eggs, a small clear glass cup of amber raw honey and a small clear glass bowl of ground cinnamon with a metal measuring spoon. She tips the measuring cup of rolled oats over the bowl.",
  "posture": "Brandon stands behind the black table, tipping the cup of oats into the bowl.",
  "composition": "Standing medium shot from chest height: the phone lens is about 55 centimeters from the bowl, which fills the lower 30 percent of the frame with the ingredients around it, closer to the camera than her face; her face and torso fill the upper half. The background is reduced by framing, never by blur.",
  "camera": "phone at her chest height, tilted slightly down toward the table, standard 1x lens, light handheld",
  "lighting": "Neutral overcast daylight from a large window out of frame, soft even light on her face, hands and the table with no harsh shadows. The red neon glows on the wall but does not tint her skin.",
  "state": "Start frame: Brandon is caught mid-sentence, lips naturally parted, animated expression, looking straight into the lens, lively, explaining.",
  "realism": "Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday reality, background fully in focus, everything in sharp focus, no AI polish, no beauty smoothing.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no plastic-looking skin, no extra fingers, no third hand, no blur, no bokeh, no warm orange color cast, no yellow tint, no golden glow, no golden hour light, no sunset, no HDR, no cinematic lighting, no beauty smoothing, no visible phone, no studio, no second person, no eyeglasses, no grey t-shirt, no white kitchen cabinets, no marble countertop, no silver cross, no printed labels or lettering on the bowls, cups, grater or muffin tin"
}
```

### K03 · T3, receita, ovo · anexar ÂNCORA HOLISTIC BRANDON + FRAME DO MODELO

```text
K03
{
  "format": "IMPORTANT: THIS IS IPHONE FOOTAGE. Vertical 9:16.",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "reference_use": "Use the first attached image only for Brandon's exact identity, wardrobe and own garage gym with the black table. Use the second attached image only as a composition reference for the camera position, framing and the action; do not copy its person, eyeglasses, grey t-shirt, white kitchen, marble countertop, refrigerator decorations or the caption text.",
  "identity_main": "The exact fictional AI character holistic.brandon: Black mixed-race American woman around thirty, athletic and toned, medium light-brown skin with light freckles across the nose and cheeks, dark brown eyes, defined eyebrows, full lips, hair in tight cornrows that turn into long loose braids falling over both shoulders, finished with small wooden and gold beads, a black floral blackwork tattoo sleeve on her right arm, a fine line tattoo on her left inner arm and a small fine-line floral tattoo below her left collarbone.",
  "wardrobe": "Plain white ribbed tank top with nothing printed on it, loose black training shorts, a thin gold chain with a small gold cross pendant and small stud earrings.",
  "scene": "Her own garage gym: a white-painted concrete block wall behind her, a red neon sign reading TRAIN PRAY REPEAT on the wall at the left, a whiteboard with handwritten black marker reading STAY READY. STAY DISCIPLINED. on the right, and a small American flag pinned above the whiteboard, discreet but clearly visible and in focus. In front of her stands a plain matte black table she uses as a kitchen counter.",
  "prop": "On the black table, a large white ceramic mixing bowl half full of bright orange finely grated carrot topped with rolled oats in the lower center. Around the bowl on the black table: a clear glass measuring cup of rolled oats, two white eggs, a small clear glass cup of amber raw honey and a small clear glass bowl of ground cinnamon with a metal measuring spoon. She holds one white egg cracked open over the bowl with both hands.",
  "posture": "Brandon stands behind the black table, cracking an egg over the bowl with both hands.",
  "composition": "Standing medium shot from chest height: the phone lens is about 55 centimeters from the bowl, which fills the lower 30 percent of the frame, closer to the camera than her face; her face and torso fill the upper half. The background is reduced by framing, never by blur.",
  "camera": "phone at her chest height, tilted slightly down toward the table, standard 1x lens, light handheld",
  "lighting": "Neutral overcast daylight from a large window out of frame, soft even light on her face, hands and the table with no harsh shadows. The red neon glows on the wall but does not tint her skin.",
  "state": "Start frame: Brandon is caught mid-sentence, lips naturally parted, animated expression, looking straight into the lens, lively.",
  "realism": "Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday reality, background fully in focus, everything in sharp focus, no AI polish, no beauty smoothing.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no plastic-looking skin, no extra fingers, no third hand, no blur, no bokeh, no warm orange color cast, no yellow tint, no golden glow, no golden hour light, no sunset, no HDR, no cinematic lighting, no beauty smoothing, no visible phone, no studio, no second person, no eyeglasses, no grey t-shirt, no white kitchen cabinets, no marble countertop, no silver cross, no printed labels or lettering on the bowls, cups, grater or muffin tin"
}
```

### K04 · T4, receita, mel · anexar ÂNCORA HOLISTIC BRANDON + FRAME DO MODELO

```text
K04
{
  "format": "IMPORTANT: THIS IS IPHONE FOOTAGE. Vertical 9:16.",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "reference_use": "Use the first attached image only for Brandon's exact identity, wardrobe and own garage gym with the black table. Use the second attached image only as a composition reference for the camera position, framing and the action; do not copy its person, eyeglasses, grey t-shirt, white kitchen, marble countertop, refrigerator decorations or the caption text.",
  "identity_main": "The exact fictional AI character holistic.brandon: Black mixed-race American woman around thirty, athletic and toned, medium light-brown skin with light freckles across the nose and cheeks, dark brown eyes, defined eyebrows, full lips, hair in tight cornrows that turn into long loose braids falling over both shoulders, finished with small wooden and gold beads, a black floral blackwork tattoo sleeve on her right arm, a fine line tattoo on her left inner arm and a small fine-line floral tattoo below her left collarbone.",
  "wardrobe": "Plain white ribbed tank top with nothing printed on it, loose black training shorts, a thin gold chain with a small gold cross pendant and small stud earrings.",
  "scene": "Her own garage gym: a white-painted concrete block wall behind her, a red neon sign reading TRAIN PRAY REPEAT on the wall at the left, a whiteboard with handwritten black marker reading STAY READY. STAY DISCIPLINED. on the right, and a small American flag pinned above the whiteboard, discreet but clearly visible and in focus. In front of her stands a plain matte black table she uses as a kitchen counter.",
  "prop": "On the black table, a large white ceramic mixing bowl half full of bright orange finely grated carrot topped with rolled oats and egg in the lower center. Her right hand tilts a small clear glass cup of amber raw honey over the bowl, a thick stream of honey starting to pour. A small clear glass bowl of ground cinnamon with a metal measuring spoon stands beside the bowl.",
  "posture": "Brandon stands behind the black table, pouring honey from the glass cup into the bowl.",
  "composition": "Standing medium shot from chest height: the phone lens is about 50 centimeters from the bowl, which fills the lower 30 percent of the frame, closer to the camera than her face; her face and torso fill the upper half. The background is reduced by framing, never by blur.",
  "camera": "phone at her chest height, tilted slightly down toward the table, standard 1x lens, light handheld",
  "lighting": "Neutral overcast daylight from a large window out of frame, soft even light on her face, hands and the table with no harsh shadows. The red neon glows on the wall but does not tint her skin.",
  "state": "Start frame: Brandon is caught mid-sentence, lips naturally parted, animated expression, looking straight into the lens, lively.",
  "realism": "Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday reality, background fully in focus, everything in sharp focus, no AI polish, no beauty smoothing.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no plastic-looking skin, no extra fingers, no third hand, no blur, no bokeh, no warm orange color cast, no yellow tint, no golden glow, no golden hour light, no sunset, no HDR, no cinematic lighting, no beauty smoothing, no visible phone, no studio, no second person, no eyeglasses, no grey t-shirt, no white kitchen cabinets, no marble countertop, no silver cross, no printed labels or lettering on the bowls, cups, grater or muffin tin"
}
```

### K05 · T5, receita, canela · anexar ÂNCORA HOLISTIC BRANDON + FRAME DO MODELO

```text
K05
{
  "format": "IMPORTANT: THIS IS IPHONE FOOTAGE. Vertical 9:16.",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "reference_use": "Use the first attached image only for Brandon's exact identity, wardrobe and own garage gym with the black table. Use the second attached image only as a composition reference for the camera position, framing and the action; do not copy its person, eyeglasses, grey t-shirt, white kitchen, marble countertop, refrigerator decorations or the caption text.",
  "identity_main": "The exact fictional AI character holistic.brandon: Black mixed-race American woman around thirty, athletic and toned, medium light-brown skin with light freckles across the nose and cheeks, dark brown eyes, defined eyebrows, full lips, hair in tight cornrows that turn into long loose braids falling over both shoulders, finished with small wooden and gold beads, a black floral blackwork tattoo sleeve on her right arm, a fine line tattoo on her left inner arm and a small fine-line floral tattoo below her left collarbone.",
  "wardrobe": "Plain white ribbed tank top with nothing printed on it, loose black training shorts, a thin gold chain with a small gold cross pendant and small stud earrings.",
  "scene": "Her own garage gym: a white-painted concrete block wall behind her, a red neon sign reading TRAIN PRAY REPEAT on the wall at the left, a whiteboard with handwritten black marker reading STAY READY. STAY DISCIPLINED. on the right, and a small American flag pinned above the whiteboard, discreet but clearly visible and in focus. In front of her stands a plain matte black table she uses as a kitchen counter.",
  "prop": "On the black table, a large white ceramic mixing bowl half full of bright orange finely grated carrot topped with oats, egg and honey in the lower center. Her right hand holds a metal measuring teaspoon heaped with ground cinnamon right above the bowl; the small glass bowl of cinnamon stands beside it.",
  "posture": "Brandon stands behind the black table, holding the teaspoon of cinnamon over the bowl.",
  "composition": "Standing medium shot from chest height: the phone lens is about 50 centimeters from the bowl, which fills the lower 30 percent of the frame, closer to the camera than her face; her face and torso fill the upper half. The background is reduced by framing, never by blur.",
  "camera": "phone at her chest height, tilted slightly down toward the table, standard 1x lens, light handheld",
  "lighting": "Neutral overcast daylight from a large window out of frame, soft even light on her face, hands and the table with no harsh shadows. The red neon glows on the wall but does not tint her skin.",
  "state": "Start frame: Brandon is caught mid-sentence, lips naturally parted, animated expression, looking straight into the lens, lively.",
  "realism": "Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday reality, background fully in focus, everything in sharp focus, no AI polish, no beauty smoothing.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no plastic-looking skin, no extra fingers, no third hand, no blur, no bokeh, no warm orange color cast, no yellow tint, no golden glow, no golden hour light, no sunset, no HDR, no cinematic lighting, no beauty smoothing, no visible phone, no studio, no second person, no eyeglasses, no grey t-shirt, no white kitchen cabinets, no marble countertop, no silver cross, no printed labels or lettering on the bowls, cups, grater or muffin tin"
}
```

### K06 · T6, receita, massa na forma · anexar ÂNCORA HOLISTIC BRANDON + FRAME DO MODELO

```text
K06
{
  "format": "IMPORTANT: THIS IS IPHONE FOOTAGE. Vertical 9:16.",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "reference_use": "Use the first attached image only for Brandon's exact identity, wardrobe and own garage gym with the black table. Use the second attached image only as a composition reference for the camera position, framing and the action; do not copy its person, eyeglasses, grey t-shirt, white kitchen, marble countertop, refrigerator decorations or the caption text.",
  "identity_main": "The exact fictional AI character holistic.brandon: Black mixed-race American woman around thirty, athletic and toned, medium light-brown skin with light freckles across the nose and cheeks, dark brown eyes, defined eyebrows, full lips, hair in tight cornrows that turn into long loose braids falling over both shoulders, finished with small wooden and gold beads, a black floral blackwork tattoo sleeve on her right arm, a fine line tattoo on her left inner arm and a small fine-line floral tattoo below her left collarbone.",
  "wardrobe": "Plain white ribbed tank top with nothing printed on it, loose black training shorts, a thin gold chain with a small gold cross pendant and small stud earrings.",
  "scene": "Her own garage gym: a white-painted concrete block wall behind her, a red neon sign reading TRAIN PRAY REPEAT on the wall at the left, a whiteboard with handwritten black marker reading STAY READY. STAY DISCIPLINED. on the right, and a small American flag pinned above the whiteboard, discreet but clearly visible and in focus. In front of her stands a plain matte black table she uses as a kitchen counter.",
  "prop": "Her left hand tilts the white mixing bowl full of thick orange carrot oat batter toward the lens; her right hand drops a spoonful of batter into an empty dark nonstick 12-cup muffin tin lined with white paper cups, the tin on the black table in the lower foreground.",
  "posture": "Brandon leans over the black table, spooning batter from the tilted bowl into the muffin tin.",
  "composition": "Close shot from chest height: the phone lens is about 35 centimeters from the tilted bowl and the muffin tin, which together fill the lower 50 percent of the frame, closer to the camera than her face; her face is in the upper third. The background is reduced by framing, never by blur.",
  "camera": "phone at her chest height, tilted down toward the tin, standard 1x lens, light handheld",
  "lighting": "Neutral overcast daylight from a large window out of frame, soft even light on her face, hands and the table with no harsh shadows. The red neon glows on the wall but does not tint her skin.",
  "state": "Start frame: Brandon is caught mid-sentence, lips naturally parted, animated expression, looking straight into the lens, focused, explaining.",
  "realism": "Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday reality, background fully in focus, everything in sharp focus, no AI polish, no beauty smoothing.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no plastic-looking skin, no extra fingers, no third hand, no blur, no bokeh, no warm orange color cast, no yellow tint, no golden glow, no golden hour light, no sunset, no HDR, no cinematic lighting, no beauty smoothing, no visible phone, no studio, no second person, no eyeglasses, no grey t-shirt, no white kitchen cabinets, no marble countertop, no silver cross, no printed labels or lettering on the bowls, cups, grater or muffin tin"
}
```

### K07 · T7, resultado, muffin na mão · anexar ÂNCORA HOLISTIC BRANDON + FRAME DO MODELO

```text
K07
{
  "format": "IMPORTANT: THIS IS IPHONE FOOTAGE. Vertical 9:16.",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "reference_use": "Use the first attached image only for Brandon's exact identity, wardrobe and own garage gym with the black table. Use the second attached image only as a composition reference for the camera position, framing and the action; do not copy its person, eyeglasses, grey t-shirt, white kitchen, marble countertop, refrigerator decorations or the caption text.",
  "identity_main": "The exact fictional AI character holistic.brandon: Black mixed-race American woman around thirty, athletic and toned, medium light-brown skin with light freckles across the nose and cheeks, dark brown eyes, defined eyebrows, full lips, hair in tight cornrows that turn into long loose braids falling over both shoulders, finished with small wooden and gold beads, a black floral blackwork tattoo sleeve on her right arm, a fine line tattoo on her left inner arm and a small fine-line floral tattoo below her left collarbone.",
  "wardrobe": "Plain white ribbed tank top with nothing printed on it, loose black training shorts, a thin gold chain with a small gold cross pendant and small stud earrings.",
  "scene": "Her own garage gym: a white-painted concrete block wall behind her, a red neon sign reading TRAIN PRAY REPEAT on the wall at the left, a whiteboard with handwritten black marker reading STAY READY. STAY DISCIPLINED. on the right, and a small American flag pinned above the whiteboard, discreet but clearly visible and in focus. In front of her stands a plain matte black table she uses as a kitchen counter.",
  "prop": "In her right hand, held up at chest height, a baked carrot oat muffin with a domed golden orange top, flecks of grated carrot and oats, no paper liner. On the black table in the lower foreground, a dark nonstick 12-cup muffin tin filled with baked golden orange carrot muffins. Her left hand gestures.",
  "posture": "Brandon stands behind the black table holding up one muffin toward the lens.",
  "composition": "Straight-on medium shot: the phone lens is about 25 centimeters from the muffin, which she holds up in her right hand at chest height and which fills about 18 percent of the frame, closer to the camera than her face; the muffin tin fills the lower 30 percent of the frame on the black table. Her face and shoulders fill the upper half. The background is reduced by framing, never by blur.",
  "camera": "phone at her eye level, straight-on, standard 1x lens, light handheld",
  "lighting": "Neutral overcast daylight from a large window out of frame, soft even light on her face, hands and the table with no harsh shadows. The red neon glows on the wall but does not tint her skin.",
  "state": "Start frame: Brandon is caught mid-sentence, lips naturally parted, animated expression, looking straight into the lens, proud, showing the muffin.",
  "realism": "Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday reality, background fully in focus, everything in sharp focus, no AI polish, no beauty smoothing.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no plastic-looking skin, no extra fingers, no third hand, no blur, no bokeh, no warm orange color cast, no yellow tint, no golden glow, no golden hour light, no sunset, no HDR, no cinematic lighting, no beauty smoothing, no visible phone, no studio, no second person, no eyeglasses, no grey t-shirt, no white kitchen cabinets, no marble countertop, no silver cross, no printed labels or lettering on the bowls, cups, grater or muffin tin"
}
```

### K08 · T8, mecanismo, a aveia · anexar ÂNCORA HOLISTIC BRANDON + FRAME DO MODELO

```text
K08
{
  "format": "IMPORTANT: THIS IS IPHONE FOOTAGE. Vertical 9:16.",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "reference_use": "Use the first attached image only for Brandon's exact identity, wardrobe and own garage gym with the black table. Use the second attached image only as a composition reference for the camera position, framing and the action; do not copy its person, eyeglasses, grey t-shirt, white kitchen, marble countertop, refrigerator decorations or the caption text.",
  "identity_main": "The exact fictional AI character holistic.brandon: Black mixed-race American woman around thirty, athletic and toned, medium light-brown skin with light freckles across the nose and cheeks, dark brown eyes, defined eyebrows, full lips, hair in tight cornrows that turn into long loose braids falling over both shoulders, finished with small wooden and gold beads, a black floral blackwork tattoo sleeve on her right arm, a fine line tattoo on her left inner arm and a small fine-line floral tattoo below her left collarbone.",
  "wardrobe": "Plain white ribbed tank top with nothing printed on it, loose black training shorts, a thin gold chain with a small gold cross pendant and small stud earrings.",
  "scene": "Her own garage gym: a white-painted concrete block wall behind her, a red neon sign reading TRAIN PRAY REPEAT on the wall at the left, a whiteboard with handwritten black marker reading STAY READY. STAY DISCIPLINED. on the right, and a small American flag pinned above the whiteboard, discreet but clearly visible and in focus. In front of her stands a plain matte black table she uses as a kitchen counter.",
  "prop": "In her right hand, held up at chest height, a baked carrot oat muffin with a domed golden orange top, flecks of grated carrot and oats, no paper liner. On the black table in the lower foreground, a dark nonstick 12-cup muffin tin filled with baked golden orange carrot muffins. Her left hand gestures.",
  "posture": "Brandon stands behind the black table holding up one muffin toward the lens.",
  "composition": "Straight-on medium shot: the phone lens is about 25 centimeters from the muffin, which she holds up in her right hand at chest height and which fills about 18 percent of the frame, closer to the camera than her face; the muffin tin fills the lower 30 percent of the frame on the black table. Her face and shoulders fill the upper half. The background is reduced by framing, never by blur.",
  "camera": "phone at her eye level, straight-on, standard 1x lens, light handheld",
  "lighting": "Neutral overcast daylight from a large window out of frame, soft even light on her face, hands and the table with no harsh shadows. The red neon glows on the wall but does not tint her skin.",
  "state": "Start frame: Brandon is caught mid-sentence, lips naturally parted, animated expression, looking straight into the lens, explaining.",
  "realism": "Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday reality, background fully in focus, everything in sharp focus, no AI polish, no beauty smoothing.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no plastic-looking skin, no extra fingers, no third hand, no blur, no bokeh, no warm orange color cast, no yellow tint, no golden glow, no golden hour light, no sunset, no HDR, no cinematic lighting, no beauty smoothing, no visible phone, no studio, no second person, no eyeglasses, no grey t-shirt, no white kitchen cabinets, no marble countertop, no silver cross, no printed labels or lettering on the bowls, cups, grater or muffin tin"
}
```

### K09 · T9, mecanismo e a tarde lenta · anexar ÂNCORA HOLISTIC BRANDON + FRAME DO MODELO

```text
K09
{
  "format": "IMPORTANT: THIS IS IPHONE FOOTAGE. Vertical 9:16.",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "reference_use": "Use the first attached image only for Brandon's exact identity, wardrobe and own garage gym with the black table. Use the second attached image only as a composition reference for the camera position, framing and the action; do not copy its person, eyeglasses, grey t-shirt, white kitchen, marble countertop, refrigerator decorations or the caption text.",
  "identity_main": "The exact fictional AI character holistic.brandon: Black mixed-race American woman around thirty, athletic and toned, medium light-brown skin with light freckles across the nose and cheeks, dark brown eyes, defined eyebrows, full lips, hair in tight cornrows that turn into long loose braids falling over both shoulders, finished with small wooden and gold beads, a black floral blackwork tattoo sleeve on her right arm, a fine line tattoo on her left inner arm and a small fine-line floral tattoo below her left collarbone.",
  "wardrobe": "Plain white ribbed tank top with nothing printed on it, loose black training shorts, a thin gold chain with a small gold cross pendant and small stud earrings.",
  "scene": "Her own garage gym: a white-painted concrete block wall behind her, a red neon sign reading TRAIN PRAY REPEAT on the wall at the left, a whiteboard with handwritten black marker reading STAY READY. STAY DISCIPLINED. on the right, and a small American flag pinned above the whiteboard, discreet but clearly visible and in focus. In front of her stands a plain matte black table she uses as a kitchen counter.",
  "prop": "In her right hand, held up at chest height, a baked carrot oat muffin with a domed golden orange top, flecks of grated carrot and oats, no paper liner. On the black table in the lower foreground, a dark nonstick 12-cup muffin tin filled with baked golden orange carrot muffins. Her left hand gestures.",
  "posture": "Brandon stands behind the black table holding up one muffin toward the lens.",
  "composition": "Straight-on medium shot: the phone lens is about 25 centimeters from the muffin, which she holds up in her right hand at chest height and which fills about 18 percent of the frame, closer to the camera than her face; the muffin tin fills the lower 30 percent of the frame on the black table. Her face and shoulders fill the upper half. The background is reduced by framing, never by blur.",
  "camera": "phone at her eye level, straight-on, standard 1x lens, light handheld",
  "lighting": "Neutral overcast daylight from a large window out of frame, soft even light on her face, hands and the table with no harsh shadows. The red neon glows on the wall but does not tint her skin.",
  "state": "Start frame: Brandon is caught mid-sentence, lips naturally parted, animated expression, looking straight into the lens, relatable, a little playful.",
  "realism": "Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday reality, background fully in focus, everything in sharp focus, no AI polish, no beauty smoothing.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no plastic-looking skin, no extra fingers, no third hand, no blur, no bokeh, no warm orange color cast, no yellow tint, no golden glow, no golden hour light, no sunset, no HDR, no cinematic lighting, no beauty smoothing, no visible phone, no studio, no second person, no eyeglasses, no grey t-shirt, no white kitchen cabinets, no marble countertop, no silver cross, no printed labels or lettering on the bowls, cups, grater or muffin tin"
}
```

### K10 · T10, rotina e virada · anexar ÂNCORA HOLISTIC BRANDON + FRAME DO MODELO

```text
K10
{
  "format": "IMPORTANT: THIS IS IPHONE FOOTAGE. Vertical 9:16.",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "reference_use": "Use the first attached image only for Brandon's exact identity, wardrobe and own garage gym with the black table. Use the second attached image only as a composition reference for the camera position, framing and the action; do not copy its person, eyeglasses, grey t-shirt, white kitchen, marble countertop, refrigerator decorations or the caption text.",
  "identity_main": "The exact fictional AI character holistic.brandon: Black mixed-race American woman around thirty, athletic and toned, medium light-brown skin with light freckles across the nose and cheeks, dark brown eyes, defined eyebrows, full lips, hair in tight cornrows that turn into long loose braids falling over both shoulders, finished with small wooden and gold beads, a black floral blackwork tattoo sleeve on her right arm, a fine line tattoo on her left inner arm and a small fine-line floral tattoo below her left collarbone.",
  "wardrobe": "Plain white ribbed tank top with nothing printed on it, loose black training shorts, a thin gold chain with a small gold cross pendant and small stud earrings.",
  "scene": "Her own garage gym: a white-painted concrete block wall behind her, a red neon sign reading TRAIN PRAY REPEAT on the wall at the left, a whiteboard with handwritten black marker reading STAY READY. STAY DISCIPLINED. on the right, and a small American flag pinned above the whiteboard, discreet but clearly visible and in focus. In front of her stands a plain matte black table she uses as a kitchen counter.",
  "prop": "In her right hand, held up at chest height, a baked carrot oat muffin with a domed golden orange top, flecks of grated carrot and oats, no paper liner. On the black table in the lower foreground, a dark nonstick 12-cup muffin tin filled with baked golden orange carrot muffins. Her left hand gestures.",
  "posture": "Brandon stands behind the black table holding up one muffin toward the lens.",
  "composition": "Straight-on medium shot: the phone lens is about 30 centimeters from the muffin, which she holds up in her right hand at chest height and which fills about 15 percent of the frame, closer to the camera than her face; the muffin tin fills the lower 30 percent of the frame on the black table. Her face and shoulders fill the upper half. The background is reduced by framing, never by blur.",
  "camera": "phone at her eye level, straight-on, standard 1x lens, light handheld",
  "lighting": "Neutral overcast daylight from a large window out of frame, soft even light on her face, hands and the table with no harsh shadows. The red neon glows on the wall but does not tint her skin.",
  "state": "Start frame: Brandon is caught mid-sentence, lips naturally parted, animated expression, looking straight into the lens, warm, then a little serious.",
  "realism": "Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday reality, background fully in focus, everything in sharp focus, no AI polish, no beauty smoothing.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no plastic-looking skin, no extra fingers, no third hand, no blur, no bokeh, no warm orange color cast, no yellow tint, no golden glow, no golden hour light, no sunset, no HDR, no cinematic lighting, no beauty smoothing, no visible phone, no studio, no second person, no eyeglasses, no grey t-shirt, no white kitchen cabinets, no marble countertop, no silver cross, no printed labels or lettering on the bowls, cups, grater or muffin tin"
}
```

### K11 · T11, ponte, o sea moss · anexar ÂNCORA HOLISTIC BRANDON + FRAME DO MODELO

```text
K11
{
  "format": "IMPORTANT: THIS IS IPHONE FOOTAGE. Vertical 9:16.",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "reference_use": "Use the first attached image only for Brandon's exact identity, wardrobe and own garage gym with the black table. Use the second attached image only as a composition reference for the camera position, framing and the action; do not copy its person, eyeglasses, grey t-shirt, white kitchen, marble countertop, refrigerator decorations or the caption text.",
  "identity_main": "The exact fictional AI character holistic.brandon: Black mixed-race American woman around thirty, athletic and toned, medium light-brown skin with light freckles across the nose and cheeks, dark brown eyes, defined eyebrows, full lips, hair in tight cornrows that turn into long loose braids falling over both shoulders, finished with small wooden and gold beads, a black floral blackwork tattoo sleeve on her right arm, a fine line tattoo on her left inner arm and a small fine-line floral tattoo below her left collarbone.",
  "wardrobe": "Plain white ribbed tank top with nothing printed on it, loose black training shorts, a thin gold chain with a small gold cross pendant and small stud earrings.",
  "scene": "Her own garage gym: a white-painted concrete block wall behind her, a red neon sign reading TRAIN PRAY REPEAT on the wall at the left, a whiteboard with handwritten black marker reading STAY READY. STAY DISCIPLINED. on the right, and a small American flag pinned above the whiteboard, discreet but clearly visible and in focus. In front of her stands a plain matte black table she uses as a kitchen counter.",
  "prop": "In her right hand, held up at chest height, a baked carrot oat muffin with a domed golden orange top, flecks of grated carrot and oats, no paper liner. On the black table in the lower foreground, a dark nonstick 12-cup muffin tin filled with baked golden orange carrot muffins. Her left hand gestures.",
  "posture": "Brandon stands behind the black table holding up one muffin toward the lens.",
  "composition": "Straight-on medium shot: the phone lens is about 30 centimeters from the muffin, which she holds up in her right hand at chest height and which fills about 15 percent of the frame, closer to the camera than her face; the muffin tin fills the lower 30 percent of the frame on the black table. Her face and shoulders fill the upper half. The background is reduced by framing, never by blur.",
  "camera": "phone at her eye level, straight-on, standard 1x lens, light handheld",
  "lighting": "Neutral overcast daylight from a large window out of frame, soft even light on her face, hands and the table with no harsh shadows. The red neon glows on the wall but does not tint her skin.",
  "state": "Start frame: Brandon is caught mid-sentence, lips naturally parted, animated expression, looking straight into the lens, like sharing a simple trick.",
  "realism": "Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday reality, background fully in focus, everything in sharp focus, no AI polish, no beauty smoothing.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no plastic-looking skin, no extra fingers, no third hand, no blur, no bokeh, no warm orange color cast, no yellow tint, no golden glow, no golden hour light, no sunset, no HDR, no cinematic lighting, no beauty smoothing, no visible phone, no studio, no second person, no eyeglasses, no grey t-shirt, no white kitchen cabinets, no marble countertop, no silver cross, no printed labels or lettering on the bowls, cups, grater or muffin tin"
}
```

### K12 · T12, obstáculo, as gomas com açúcar · anexar ÂNCORA HOLISTIC BRANDON + FRAME DO MODELO

```text
K12
{
  "format": "IMPORTANT: THIS IS IPHONE FOOTAGE. Vertical 9:16.",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "reference_use": "Use the first attached image only for Brandon's exact identity, wardrobe and own garage gym with the black table. Use the second attached image only as a composition reference for the camera position, framing and the action; do not copy its person, eyeglasses, grey t-shirt, white kitchen, marble countertop, refrigerator decorations or the caption text.",
  "identity_main": "The exact fictional AI character holistic.brandon: Black mixed-race American woman around thirty, athletic and toned, medium light-brown skin with light freckles across the nose and cheeks, dark brown eyes, defined eyebrows, full lips, hair in tight cornrows that turn into long loose braids falling over both shoulders, finished with small wooden and gold beads, a black floral blackwork tattoo sleeve on her right arm, a fine line tattoo on her left inner arm and a small fine-line floral tattoo below her left collarbone.",
  "wardrobe": "Plain white ribbed tank top with nothing printed on it, loose black training shorts, a thin gold chain with a small gold cross pendant and small stud earrings.",
  "scene": "Her own garage gym: a white-painted concrete block wall behind her, a red neon sign reading TRAIN PRAY REPEAT on the wall at the left, a whiteboard with handwritten black marker reading STAY READY. STAY DISCIPLINED. on the right, and a small American flag pinned above the whiteboard, discreet but clearly visible and in focus. In front of her stands a plain matte black table she uses as a kitchen counter.",
  "prop": "In her right hand, held up at chest height, a baked carrot oat muffin with a domed golden orange top, flecks of grated carrot and oats, no paper liner. On the black table in the lower foreground, a dark nonstick 12-cup muffin tin filled with baked golden orange carrot muffins. Her left hand gestures.",
  "posture": "Brandon stands behind the black table holding up one muffin toward the lens.",
  "composition": "Straight-on medium shot: the phone lens is about 30 centimeters from the muffin, which she holds up in her right hand at chest height and which fills about 15 percent of the frame, closer to the camera than her face; the muffin tin fills the lower 30 percent of the frame on the black table. Her face and shoulders fill the upper half. The background is reduced by framing, never by blur.",
  "camera": "phone at her eye level, straight-on, standard 1x lens, light handheld",
  "lighting": "Neutral overcast daylight from a large window out of frame, soft even light on her face, hands and the table with no harsh shadows. The red neon glows on the wall but does not tint her skin.",
  "state": "Start frame: Brandon is caught mid-sentence, lips naturally parted, animated expression, looking straight into the lens, warning, a little disgusted.",
  "realism": "Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday reality, background fully in focus, everything in sharp focus, no AI polish, no beauty smoothing.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no plastic-looking skin, no extra fingers, no third hand, no blur, no bokeh, no warm orange color cast, no yellow tint, no golden glow, no golden hour light, no sunset, no HDR, no cinematic lighting, no beauty smoothing, no visible phone, no studio, no second person, no eyeglasses, no grey t-shirt, no white kitchen cabinets, no marble countertop, no silver cross, no printed labels or lettering on the bowls, cups, grater or muffin tin"
}
```

### K13 · T13, produto, o frasco sobe no nome · anexar ÂNCORA HOLISTIC BRANDON + FRAME DO MODELO + FOTO DO PRODUTO

```text
K13
{
  "format": "IMPORTANT: THIS IS IPHONE FOOTAGE. Vertical 9:16.",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "reference_use": "Use the first attached image only for Brandon's exact identity, wardrobe and own garage gym with the black table. Use the second attached image only as a composition reference for the camera position, framing and the action; do not copy its person, eyeglasses, grey t-shirt, white kitchen, marble countertop, refrigerator decorations or the caption text. Use the third attached image only for the Natural Rems Sea Moss jar: copy ONLY the front jar, without the MADE IN USA banner at the top, without the second jar behind it and without the loose gummies.",
  "identity_main": "The exact fictional AI character holistic.brandon: Black mixed-race American woman around thirty, athletic and toned, medium light-brown skin with light freckles across the nose and cheeks, dark brown eyes, defined eyebrows, full lips, hair in tight cornrows that turn into long loose braids falling over both shoulders, finished with small wooden and gold beads, a black floral blackwork tattoo sleeve on her right arm, a fine line tattoo on her left inner arm and a small fine-line floral tattoo below her left collarbone.",
  "wardrobe": "Plain white ribbed tank top with nothing printed on it, loose black training shorts, a thin gold chain with a small gold cross pendant and small stud earrings.",
  "scene": "Her own garage gym: a white-painted concrete block wall behind her, a red neon sign reading TRAIN PRAY REPEAT on the wall at the left, a whiteboard with handwritten black marker reading STAY READY. STAY DISCIPLINED. on the right, and a small American flag pinned above the whiteboard, discreet but clearly visible and in focus. In front of her stands a plain matte black table she uses as a kitchen counter.",
  "prop": "In her right hand, held low just above the black table, the Natural Rems Sea Moss jar: a short wide jar of dark amber plastic with a black screw cap, a pale cream-green label with dark green text, the Natural Rems logo with three leaves, the big title Sea Moss Gummies, a 6000 MG | 16-IN-1 badge, the words GREEN APPLE FLAVOR, a list of ingredients in dark green pill shapes and green seaweed illustrations on both sides, label facing the camera, fully readable. Nothing else on the table.",
  "posture": "Brandon holds the jar low in her right hand, about to raise it beside her face.",
  "composition": "Straight-on medium shot: the phone lens is about 35 centimeters from the jar, which she holds low in her right hand just above the black table and fills the lower right 20 percent of the frame, closer to the camera than her face; her face and shoulders fill the upper half of the frame. The background is reduced by framing, never by blur.",
  "camera": "phone at her chest height, straight-on, standard 1x lens, light handheld",
  "lighting": "Neutral overcast daylight from a large window out of frame, soft even light on her face, hands and the table with no harsh shadows. The red neon glows on the wall but does not tint her skin.",
  "state": "Start frame: Brandon is caught mid-sentence, lips naturally parted, animated expression, looking straight into the lens, proud, about to show it.",
  "realism": "Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday reality, background fully in focus, everything in sharp focus, no AI polish, no beauty smoothing.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no plastic-looking skin, no extra fingers, no third hand, no blur, no bokeh, no warm orange color cast, no yellow tint, no golden glow, no golden hour light, no sunset, no HDR, no cinematic lighting, no beauty smoothing, no visible phone, no studio, no second person, no eyeglasses, no grey t-shirt, no white kitchen cabinets, no marble countertop, no silver cross, no second jar, no other bottles, no loose gummies, no banner above the jar, no hand covering the label, no muffins on the table"
}
```

### K14 · T14, diferencial · anexar ÂNCORA HOLISTIC BRANDON + FRAME DO MODELO + FOTO DO PRODUTO

```text
K14
{
  "format": "IMPORTANT: THIS IS IPHONE FOOTAGE. Vertical 9:16.",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "reference_use": "Use the first attached image only for Brandon's exact identity, wardrobe and own garage gym with the black table. Use the second attached image only as a composition reference for the camera position, framing and the action; do not copy its person, eyeglasses, grey t-shirt, white kitchen, marble countertop, refrigerator decorations or the caption text. Use the third attached image only for the Natural Rems Sea Moss jar: copy ONLY the front jar, without the MADE IN USA banner at the top, without the second jar behind it and without the loose gummies.",
  "identity_main": "The exact fictional AI character holistic.brandon: Black mixed-race American woman around thirty, athletic and toned, medium light-brown skin with light freckles across the nose and cheeks, dark brown eyes, defined eyebrows, full lips, hair in tight cornrows that turn into long loose braids falling over both shoulders, finished with small wooden and gold beads, a black floral blackwork tattoo sleeve on her right arm, a fine line tattoo on her left inner arm and a small fine-line floral tattoo below her left collarbone.",
  "wardrobe": "Plain white ribbed tank top with nothing printed on it, loose black training shorts, a thin gold chain with a small gold cross pendant and small stud earrings.",
  "scene": "Her own garage gym: a white-painted concrete block wall behind her, a red neon sign reading TRAIN PRAY REPEAT on the wall at the left, a whiteboard with handwritten black marker reading STAY READY. STAY DISCIPLINED. on the right, and a small American flag pinned above the whiteboard, discreet but clearly visible and in focus. In front of her stands a plain matte black table she uses as a kitchen counter.",
  "prop": "In her right hand, held still beside her right cheek, the Natural Rems Sea Moss jar: a short wide jar of dark amber plastic with a black screw cap, a pale cream-green label with dark green text, the Natural Rems logo with three leaves, the big title Sea Moss Gummies, a 6000 MG | 16-IN-1 badge, the words GREEN APPLE FLAVOR, a list of ingredients in dark green pill shapes and green seaweed illustrations on both sides, label facing the camera, fully readable. Her left hand rests on the black table.",
  "posture": "Brandon holds the jar still beside her right cheek, label toward the lens.",
  "composition": "Straight-on medium shot: the jar is held up beside her right cheek and pushed slightly toward the camera, the phone lens is about 30 centimeters from the jar, which fills 20 percent of the frame at the right of her face, closer to the camera than her face, label facing the camera and fully readable. The background is reduced by framing, never by blur.",
  "camera": "phone at her chest height, straight-on, standard 1x lens, light handheld",
  "lighting": "Neutral overcast daylight from a large window out of frame, soft even light on her face, hands and the table with no harsh shadows. The red neon glows on the wall but does not tint her skin.",
  "state": "Start frame: Brandon is caught mid-sentence, lips naturally parted, animated expression, looking straight into the lens, lively, listing.",
  "realism": "Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday reality, background fully in focus, everything in sharp focus, no AI polish, no beauty smoothing.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no plastic-looking skin, no extra fingers, no third hand, no blur, no bokeh, no warm orange color cast, no yellow tint, no golden glow, no golden hour light, no sunset, no HDR, no cinematic lighting, no beauty smoothing, no visible phone, no studio, no second person, no eyeglasses, no grey t-shirt, no white kitchen cabinets, no marble countertop, no silver cross, no second jar, no other bottles, no loose gummies, no banner above the jar, no hand covering the label, no muffins on the table"
}
```

### K15 · T15, prova social da coach · anexar ÂNCORA HOLISTIC BRANDON + FRAME DO MODELO + FOTO DO PRODUTO

```text
K15
{
  "format": "IMPORTANT: THIS IS IPHONE FOOTAGE. Vertical 9:16.",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "reference_use": "Use the first attached image only for Brandon's exact identity, wardrobe and own garage gym with the black table. Use the second attached image only as a composition reference for the camera position, framing and the action; do not copy its person, eyeglasses, grey t-shirt, white kitchen, marble countertop, refrigerator decorations or the caption text. Use the third attached image only for the Natural Rems Sea Moss jar: copy ONLY the front jar, without the MADE IN USA banner at the top, without the second jar behind it and without the loose gummies.",
  "identity_main": "The exact fictional AI character holistic.brandon: Black mixed-race American woman around thirty, athletic and toned, medium light-brown skin with light freckles across the nose and cheeks, dark brown eyes, defined eyebrows, full lips, hair in tight cornrows that turn into long loose braids falling over both shoulders, finished with small wooden and gold beads, a black floral blackwork tattoo sleeve on her right arm, a fine line tattoo on her left inner arm and a small fine-line floral tattoo below her left collarbone.",
  "wardrobe": "Plain white ribbed tank top with nothing printed on it, loose black training shorts, a thin gold chain with a small gold cross pendant and small stud earrings.",
  "scene": "Her own garage gym: a white-painted concrete block wall behind her, a red neon sign reading TRAIN PRAY REPEAT on the wall at the left, a whiteboard with handwritten black marker reading STAY READY. STAY DISCIPLINED. on the right, and a small American flag pinned above the whiteboard, discreet but clearly visible and in focus. In front of her stands a plain matte black table she uses as a kitchen counter.",
  "prop": "In her right hand, held still beside her right cheek, the Natural Rems Sea Moss jar: a short wide jar of dark amber plastic with a black screw cap, a pale cream-green label with dark green text, the Natural Rems logo with three leaves, the big title Sea Moss Gummies, a 6000 MG | 16-IN-1 badge, the words GREEN APPLE FLAVOR, a list of ingredients in dark green pill shapes and green seaweed illustrations on both sides, label facing the camera, fully readable. Her left hand rests on the black table.",
  "posture": "Brandon holds the jar still beside her right cheek, label toward the lens.",
  "composition": "Straight-on medium shot: the jar is held up beside her right cheek and pushed slightly toward the camera, the phone lens is about 30 centimeters from the jar, which fills 20 percent of the frame at the right of her face, closer to the camera than her face, label facing the camera and fully readable. The background is reduced by framing, never by blur.",
  "camera": "phone at her chest height, straight-on, standard 1x lens, light handheld",
  "lighting": "Neutral overcast daylight from a large window out of frame, soft even light on her face, hands and the table with no harsh shadows. The red neon glows on the wall but does not tint her skin.",
  "state": "Start frame: Brandon is caught mid-sentence, lips naturally parted, animated expression, looking straight into the lens, warm and certain.",
  "realism": "Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday reality, background fully in focus, everything in sharp focus, no AI polish, no beauty smoothing.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no plastic-looking skin, no extra fingers, no third hand, no blur, no bokeh, no warm orange color cast, no yellow tint, no golden glow, no golden hour light, no sunset, no HDR, no cinematic lighting, no beauty smoothing, no visible phone, no studio, no second person, no eyeglasses, no grey t-shirt, no white kitchen cabinets, no marble countertop, no silver cross, no second jar, no other bottles, no loose gummies, no banner above the jar, no hand covering the label, no muffins on the table"
}
```

### K16 · T16, comment yes + follow · anexar ÂNCORA HOLISTIC BRANDON + FRAME DO MODELO + FOTO DO PRODUTO

```text
K16
{
  "format": "IMPORTANT: THIS IS IPHONE FOOTAGE. Vertical 9:16.",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "reference_use": "Use the first attached image only for Brandon's exact identity, wardrobe and own garage gym with the black table. Use the second attached image only as a composition reference for the camera position, framing and the action; do not copy its person, eyeglasses, grey t-shirt, white kitchen, marble countertop, refrigerator decorations or the caption text. Use the third attached image only for the Natural Rems Sea Moss jar: copy ONLY the front jar, without the MADE IN USA banner at the top, without the second jar behind it and without the loose gummies.",
  "identity_main": "The exact fictional AI character holistic.brandon: Black mixed-race American woman around thirty, athletic and toned, medium light-brown skin with light freckles across the nose and cheeks, dark brown eyes, defined eyebrows, full lips, hair in tight cornrows that turn into long loose braids falling over both shoulders, finished with small wooden and gold beads, a black floral blackwork tattoo sleeve on her right arm, a fine line tattoo on her left inner arm and a small fine-line floral tattoo below her left collarbone.",
  "wardrobe": "Plain white ribbed tank top with nothing printed on it, loose black training shorts, a thin gold chain with a small gold cross pendant and small stud earrings.",
  "scene": "Her own garage gym: a white-painted concrete block wall behind her, a red neon sign reading TRAIN PRAY REPEAT on the wall at the left, a whiteboard with handwritten black marker reading STAY READY. STAY DISCIPLINED. on the right, and a small American flag pinned above the whiteboard, discreet but clearly visible and in focus. In front of her stands a plain matte black table she uses as a kitchen counter.",
  "prop": "In her right hand, held still beside her right cheek, the Natural Rems Sea Moss jar: a short wide jar of dark amber plastic with a black screw cap, a pale cream-green label with dark green text, the Natural Rems logo with three leaves, the big title Sea Moss Gummies, a 6000 MG | 16-IN-1 badge, the words GREEN APPLE FLAVOR, a list of ingredients in dark green pill shapes and green seaweed illustrations on both sides, label facing the camera, fully readable. Her left hand rests on the black table.",
  "posture": "Brandon holds the jar still beside her right cheek, label toward the lens.",
  "composition": "Straight-on medium shot: the jar is held up beside her right cheek and pushed slightly toward the camera, the phone lens is about 30 centimeters from the jar, which fills 20 percent of the frame at the right of her face, closer to the camera than her face, label facing the camera and fully readable. The background is reduced by framing, never by blur.",
  "camera": "phone at her chest height, straight-on, standard 1x lens, light handheld",
  "lighting": "Neutral overcast daylight from a large window out of frame, soft even light on her face, hands and the table with no harsh shadows. The red neon glows on the wall but does not tint her skin.",
  "state": "Start frame: Brandon is caught mid-sentence, lips naturally parted, animated expression, looking straight into the lens, inviting, smiling on yes.",
  "realism": "Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday reality, background fully in focus, everything in sharp focus, no AI polish, no beauty smoothing.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no plastic-looking skin, no extra fingers, no third hand, no blur, no bokeh, no warm orange color cast, no yellow tint, no golden glow, no golden hour light, no sunset, no HDR, no cinematic lighting, no beauty smoothing, no visible phone, no studio, no second person, no eyeglasses, no grey t-shirt, no white kitchen cabinets, no marble countertop, no silver cross, no second jar, no other bottles, no loose gummies, no banner above the jar, no hand covering the label, no muffins on the table"
}
```

### K17 · T17, CTA da marca · anexar ÂNCORA HOLISTIC BRANDON + FRAME DO MODELO + FOTO DO PRODUTO

```text
K17
{
  "format": "IMPORTANT: THIS IS IPHONE FOOTAGE. Vertical 9:16.",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "reference_use": "Use the first attached image only for Brandon's exact identity, wardrobe and own garage gym with the black table. Use the second attached image only as a composition reference for the camera position, framing and the action; do not copy its person, eyeglasses, grey t-shirt, white kitchen, marble countertop, refrigerator decorations or the caption text. Use the third attached image only for the Natural Rems Sea Moss jar: copy ONLY the front jar, without the MADE IN USA banner at the top, without the second jar behind it and without the loose gummies.",
  "identity_main": "The exact fictional AI character holistic.brandon: Black mixed-race American woman around thirty, athletic and toned, medium light-brown skin with light freckles across the nose and cheeks, dark brown eyes, defined eyebrows, full lips, hair in tight cornrows that turn into long loose braids falling over both shoulders, finished with small wooden and gold beads, a black floral blackwork tattoo sleeve on her right arm, a fine line tattoo on her left inner arm and a small fine-line floral tattoo below her left collarbone.",
  "wardrobe": "Plain white ribbed tank top with nothing printed on it, loose black training shorts, a thin gold chain with a small gold cross pendant and small stud earrings.",
  "scene": "Her own garage gym: a white-painted concrete block wall behind her, a red neon sign reading TRAIN PRAY REPEAT on the wall at the left, a whiteboard with handwritten black marker reading STAY READY. STAY DISCIPLINED. on the right, and a small American flag pinned above the whiteboard, discreet but clearly visible and in focus. In front of her stands a plain matte black table she uses as a kitchen counter.",
  "prop": "In her right hand, held still beside her right cheek, the Natural Rems Sea Moss jar: a short wide jar of dark amber plastic with a black screw cap, a pale cream-green label with dark green text, the Natural Rems logo with three leaves, the big title Sea Moss Gummies, a 6000 MG | 16-IN-1 badge, the words GREEN APPLE FLAVOR, a list of ingredients in dark green pill shapes and green seaweed illustrations on both sides, label facing the camera, fully readable. Her left hand rests on the black table.",
  "posture": "Brandon holds the jar still beside her right cheek, label toward the lens.",
  "composition": "Straight-on medium shot: the jar is held up beside her right cheek and pushed slightly toward the camera, the phone lens is about 30 centimeters from the jar, which fills 20 percent of the frame at the right of her face, closer to the camera than her face, label facing the camera and fully readable. The background is reduced by framing, never by blur.",
  "camera": "phone at her chest height, straight-on, standard 1x lens, light handheld",
  "lighting": "Neutral overcast daylight from a large window out of frame, soft even light on her face, hands and the table with no harsh shadows. The red neon glows on the wall but does not tint her skin.",
  "state": "Start frame: Brandon is caught mid-sentence, lips naturally parted, animated expression, looking straight into the lens, clear and slow on the brand name.",
  "realism": "Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday reality, background fully in focus, everything in sharp focus, no AI polish, no beauty smoothing.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no plastic-looking skin, no extra fingers, no third hand, no blur, no bokeh, no warm orange color cast, no yellow tint, no golden glow, no golden hour light, no sunset, no HDR, no cinematic lighting, no beauty smoothing, no visible phone, no studio, no second person, no eyeglasses, no grey t-shirt, no white kitchen cabinets, no marble countertop, no silver cross, no second jar, no other bottles, no loose gummies, no banner above the jar, no hand covering the label, no muffins on the table"
}
```

## 3. PROMPTS DE VÍDEO (um bloco por V)

### V01 · T1 · frame inicial = a imagem que você deixou no K01

```text
V01
a avatar Brandon, mulher, fala em inglês com sotaque americano de uma mulher negra americana, voz feminina clara e firme de uma mulher de uns trinta anos, entonação animada e intrigante, como quem conta um segredo de cozinha, voz autêntica, como se exigisse ser ouvida, a seguinte frase: "Did you know, if you grate two large carrots into a bowl,"

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Brandon rala a cenoura no ralador dentro da tigela, a cenoura ralada caindo, e olha para a câmera enquanto fala. Ela diz a frase em ritmo natural logo no começo e a ação continua até o fim.

câmera: leve handheld natural

som ambiente: box de treino em casa, tranquilo, cenoura raspando no ralador, sem música
```

### V02 · T2 · frame inicial = a imagem que você deixou no K02

```text
V02
a avatar Brandon, mulher, fala em inglês com sotaque americano de uma mulher negra americana, voz feminina clara e firme de uma mulher de uns trinta anos, entonação animada e didática, rápida, voz autêntica, como se exigisse ser ouvida, a seguinte frase: "mix in one cup of oats,"

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Brandon despeja a aveia do copo medidor dentro da tigela. Ela diz a frase em ritmo natural logo no começo e a ação continua até o fim.

câmera: leve handheld natural

som ambiente: box de treino em casa, tranquilo, aveia caindo na tigela, sem música
```

### V03 · T3 · frame inicial = a imagem que você deixou no K03

```text
V03
a avatar Brandon, mulher, fala em inglês com sotaque americano de uma mulher negra americana, voz feminina clara e firme de uma mulher de uns trinta anos, entonação animada e didática, rápida, voz autêntica, como se exigisse ser ouvida, a seguinte frase: "two eggs,"

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Brandon abre o ovo e deixa cair dentro da tigela. Ela diz a frase em ritmo natural logo no começo e a ação continua até o fim.

câmera: leve handheld natural

som ambiente: box de treino em casa, tranquilo, casca de ovo quebrando, sem música
```

### V04 · T4 · frame inicial = a imagem que você deixou no K04

```text
V04
a avatar Brandon, mulher, fala em inglês com sotaque americano de uma mulher negra americana, voz feminina clara e firme de uma mulher de uns trinta anos, entonação animada e didática, rápida, voz autêntica, como se exigisse ser ouvida, a seguinte frase: "a quarter cup of raw honey,"

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Brandon despeja o mel do copinho dentro da tigela. Ela diz a frase em ritmo natural logo no começo e a ação continua até o fim.

câmera: leve handheld natural

som ambiente: box de treino em casa, tranquilo, sem música
```

### V05 · T5 · frame inicial = a imagem que você deixou no K05

```text
V05
a avatar Brandon, mulher, fala em inglês com sotaque americano de uma mulher negra americana, voz feminina clara e firme de uma mulher de uns trinta anos, entonação animada e didática, rápida, voz autêntica, como se exigisse ser ouvida, a seguinte frase: "and a teaspoon of cinnamon."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Brandon vira a colher de canela dentro da tigela. Ela diz a frase em ritmo natural logo no começo e a ação continua até o fim.

câmera: leve handheld natural

som ambiente: box de treino em casa, tranquilo, colher batendo de leve na tigela, sem música
```

### V06 · T6 · frame inicial = a imagem que você deixou no K06

```text
V06
a avatar Brandon, mulher, fala em inglês com sotaque americano de uma mulher negra americana, voz feminina clara e firme de uma mulher de uns trinta anos, entonação animada e didática, voz autêntica, como se exigisse ser ouvida, a seguinte frase: "Then pour the batter into a muffin tin."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Brandon põe colheradas de massa nas forminhas. Ela diz a frase em ritmo natural logo no começo e a ação continua até o fim.

câmera: leve handheld natural

som ambiente: box de treino em casa, tranquilo, colher raspando a tigela, sem música
```

### V07 · T7 · frame inicial = a imagem que você deixou no K07

```text
V07
a avatar Brandon, mulher, fala em inglês com sotaque americano de uma mulher negra americana, voz feminina clara e firme de uma mulher de uns trinta anos, entonação orgulhosa e animada, voz autêntica, como se exigisse ser ouvida, a seguinte frase: "You end up with soft, moist muffins that taste like carrot cake but are loaded with fiber and have zero flour and zero refined sugar."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Brandon ergue o muffin na direção da câmera e fala, com a forma cheia na mesa.

câmera: fixa, leve handheld natural

som ambiente: box de treino em casa, tranquilo, sem música
```

### V08 · T8 · frame inicial = a imagem que você deixou no K08

```text
V08
a avatar Brandon, mulher, fala em inglês com sotaque americano de uma mulher negra americana, voz feminina clara e firme de uma mulher de uns trinta anos, entonação didática, voz autêntica, como se exigisse ser ouvida, a seguinte frase: "The oats feed the good bacteria in your gut"

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Brandon fala para a câmera segurando o muffin. Ela diz a frase em ritmo natural logo no começo e a ação continua até o fim.

câmera: fixa, leve handheld natural

som ambiente: box de treino em casa, tranquilo, sem música
```

### V09 · T9 · frame inicial = a imagem que você deixou no K09

```text
V09
a avatar Brandon, mulher, fala em inglês com sotaque americano de uma mulher negra americana, voz feminina clara e firme de uma mulher de uns trinta anos, entonação próxima e bem-humorada, voz autêntica, como se exigisse ser ouvida, a seguinte frase: "and the carrots are full of prebiotic fiber. It keeps everything moving so you stop feeling backed up and sluggish by the afternoon."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Brandon fala para a câmera segurando o muffin, com um pequeno gesto da outra mão.

câmera: fixa, leve handheld natural

som ambiente: box de treino em casa, tranquilo, sem música
```

### V10 · T10 · frame inicial = a imagem que você deixou no K10

```text
V10
a avatar Brandon, mulher, fala em inglês com sotaque americano de uma mulher negra americana, voz feminina clara e firme de uma mulher de uns trinta anos, entonação calorosa, ficando séria no fim, voz autêntica, como se exigisse ser ouvida, a seguinte frase: "I make a batch every Sunday morning and eat them all week. But some weeks the batch runs out early, and that sluggish afternoon comes right back."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Brandon fala para a câmera segurando o muffin.

câmera: fixa, leve handheld natural

som ambiente: box de treino em casa, tranquilo, sem música
```

### V11 · T11 · frame inicial = a imagem que você deixou no K11

```text
V11
a avatar Brandon, mulher, fala em inglês com sotaque americano de uma mulher negra americana, voz feminina clara e firme de uma mulher de uns trinta anos, entonação de quem conta um truque simples, voz autêntica, como se exigisse ser ouvida, a seguinte frase: "So I added one thing that does the same job with no oven: sea moss. It's a sea plant that feeds the same good bacteria in your gut."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Brandon fala para a câmera segurando o muffin, levantando um dedo da outra mão.

câmera: fixa, leve handheld natural

som ambiente: box de treino em casa, tranquilo, sem música
```

### V12 · T12 · frame inicial = a imagem que você deixou no K12

```text
V12
a avatar Brandon, mulher, fala em inglês com sotaque americano de uma mulher negra americana, voz feminina clara e firme de uma mulher de uns trinta anos, entonação de alerta, com um leve desgosto, voz autêntica, como se exigisse ser ouvida, a seguinte frase: "But be careful, most sea moss gummies are loaded with sugar, which undoes the whole point of a zero sugar muffin, and the raw stuff tastes like seawater."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Brandon balança a cabeça de leve e fala para a câmera, segurando o muffin.

câmera: fixa, leve handheld natural

som ambiente: box de treino em casa, tranquilo, sem música
```

### V13 · T13 · frame inicial = a imagem que você deixou no K13

```text
V13
a avatar Brandon, mulher, fala em inglês com sotaque americano de uma mulher negra americana, voz feminina clara e firme de uma mulher de uns trinta anos, entonação orgulhosa, dizendo Natural Rems Sea Moss devagar e por inteiro, voz autêntica, como se exigisse ser ouvida, a seguinte frase: "The one I trust is Natural Rems Sea Moss. It's made in the USA with wild Irish sea moss, plus ginger, dandelion and apple cider vinegar."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Brandon ergue o frasco devagar da altura da cintura até o lado do rosto no nome do produto e o deixa parado, rótulo de frente.

câmera: fixa

som ambiente: box de treino em casa, tranquilo, sem música
```

### V14 · T14 · frame inicial = a imagem que você deixou no K14

```text
V14
a avatar Brandon, mulher, fala em inglês com sotaque americano de uma mulher negra americana, voz feminina clara e firme de uma mulher de uns trinta anos, entonação animada, listando, voz autêntica, como se exigisse ser ouvida, a seguinte frase: "One green apple gummy a day, under a gram of sugar, no seaweed taste. It covers the days the muffins run out, and every other day too."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Brandon fala para a câmera com o frasco parado ao lado do rosto, rótulo de frente.

câmera: fixa

som ambiente: box de treino em casa, tranquilo, sem música
```

### V15 · T15 · frame inicial = a imagem que você deixou no K15

```text
V15
a avatar Brandon, mulher, fala em inglês com sotaque americano de uma mulher negra americana, voz feminina clara e firme de uma mulher de uns trinta anos, entonação calorosa e segura, voz autêntica, como se exigisse ser ouvida, a seguinte frase: "My clients keep it right next to their Sunday muffins, and the ones who stuck with it tell me their afternoons finally feel light."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Brandon fala para a câmera com o frasco parado ao lado do rosto, rótulo de frente.

câmera: fixa

som ambiente: box de treino em casa, tranquilo, sem música
```

### V16 · T16 · frame inicial = a imagem que você deixou no K16

```text
V16
a avatar Brandon, mulher, fala em inglês com sotaque americano de uma mulher negra americana, voz feminina clara e firme de uma mulher de uns trinta anos, entonação convidativa, sorrindo no yes, voz autêntica, como se exigisse ser ouvida, a seguinte frase: "Comment yes if your afternoons feel sluggish too, and follow me so you have this recipe when Sunday comes."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Brandon fala para a câmera com o frasco parado ao lado do rosto, sorrindo no yes.

câmera: fixa

som ambiente: box de treino em casa, tranquilo, sem música
```

### V17 · T17 · frame inicial = a imagem que você deixou no K17

```text
V17
a avatar Brandon, mulher, fala em inglês com sotaque americano de uma mulher negra americana, voz feminina clara e firme de uma mulher de uns trinta anos, entonação clara, dizendo Natural Rems Sea Moss devagar e por inteiro, voz autêntica, como se exigisse ser ouvida, a seguinte frase: "Search Natural Rems Sea Moss on Amazon. Or you can just tap the link I left in the caption."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Brandon fala para a câmera com o frasco parado ao lado do rosto, rótulo de frente, do começo ao fim, sem baixar o frasco.

câmera: fixa

som ambiente: box de treino em casa, tranquilo, sem música
```

## 4. Montagem no CapCut

1. Clipes numerados na ordem: V01 a V17.
2. Do V01 ao V09, cortar no tempo da cena do modelo: V01 0,0 a 3,7 s; V02 3,7 a 6,1 s; V03 6,1 a 7,5 s; V04 7,5 a 9,5 s; V05 9,5 a 10,9 s; V06 10,9 a 12,9 s; V07 12,9 a 20,3 s; V08 20,3 a 23,2 s; V09 23,2 a 29,3 s. Do V10 ao V17, cortar logo depois da última palavra.
3. Zero tempo morto: todo clipe começa já falando. Isolate Voice / Keep Vocal no áudio.
4. Nos V01 a V06 e no V08 (cenas curtas) a fala vem no começo; manter a ação até o tempo da cena do modelo.
5. Legenda branca serifada, duas a três palavras por vez, com a palavra de peso maior, no meio do quadro, igual ao modelo. No V16, `yes` grande e isolado na tela. No V17, setas apontando para a legenda do post.
6. Sem Voice Changer: a voz vem do prompt de cada V.
7. Música só depois do gancho (a partir do V02), entre -19 e -20 dB, fora da biblioteca do TikTok.
8. Rótulo pequeno `AI-generated` num canto do vídeo.
9. Do V13 ao V17 o frasco não pode ser cortado nem coberto: nenhum B-roll por cima (regra da marca).

## 5. Legenda do post

- Primeira linha, sempre: `#ad #syntheticperformer #naturalrems`
- Logo abaixo: o link da Amazon do Natural Rems Sea Moss (o V17 manda tocar no link da legenda).
- Chave de conteúdo de IA da plataforma LIGADA.

## 6. Transcrição final por take

| Take | English | Português |
|---|---|---|
| T1 | Did you know, if you grate two large carrots into a bowl, | Você sabia que, se você ralar duas cenouras grandes numa tigela, |
| T2 | mix in one cup of oats, | misturar uma xícara de aveia, |
| T3 | two eggs, | dois ovos, |
| T4 | a quarter cup of raw honey, | um quarto de xícara de mel cru |
| T5 | and a teaspoon of cinnamon. | e uma colher de chá de canela. |
| T6 | Then pour the batter into a muffin tin. | Depois coloque a massa numa forma de muffin. |
| T7 | You end up with soft, moist muffins that taste like carrot cake but are loaded with fiber and have zero flour and zero refined sugar. | Você fica com muffins macios e úmidos com gosto de bolo de cenoura, mas cheios de fibra, com zero farinha e zero açúcar refinado. |
| T8 | The oats feed the good bacteria in your gut | A aveia alimenta as bactérias boas do seu intestino |
| T9 | and the carrots are full of prebiotic fiber. It keeps everything moving so you stop feeling backed up and sluggish by the afternoon. | e a cenoura é cheia de fibra prebiótica. Isso mantém tudo andando, e você para de se sentir travada e lenta à tarde. |
| T10 | I make a batch every Sunday morning and eat them all week. But some weeks the batch runs out early, and that sluggish afternoon comes right back. | Eu faço uma fornada todo domingo de manhã e como a semana inteira. Mas tem semana que a fornada acaba antes, e aquela tarde lenta volta na hora. |
| T11 | So I added one thing that does the same job with no oven: sea moss. It's a sea plant that feeds the same good bacteria in your gut. | Então eu acrescentei uma coisa que faz o mesmo trabalho sem forno: sea moss. É uma planta do mar que alimenta as mesmas bactérias boas do seu intestino. |
| T12 | But be careful, most sea moss gummies are loaded with sugar, which undoes the whole point of a zero sugar muffin, and the raw stuff tastes like seawater. | Mas cuidado: a maioria das gomas de sea moss vem cheia de açúcar, o que estraga todo o sentido de um muffin sem açúcar, e o sea moss cru tem gosto de água do mar. |
| T13 | The one I trust is Natural Rems Sea Moss. It's made in the USA with wild Irish sea moss, plus ginger, dandelion and apple cider vinegar. | O que eu confio é o Natural Rems Sea Moss. É feito nos EUA com sea moss irlandês selvagem, mais gengibre, dente-de-leão e vinagre de maçã. |
| T14 | One green apple gummy a day, under a gram of sugar, no seaweed taste. It covers the days the muffins run out, and every other day too. | Uma goma de maçã verde por dia, menos de um grama de açúcar, sem gosto de alga. Ela cobre os dias em que os muffins acabam, e todos os outros dias também. |
| T15 | My clients keep it right next to their Sunday muffins, and the ones who stuck with it tell me their afternoons finally feel light. | Minhas clientes deixam ele do lado dos muffins de domingo, e as que mantiveram me dizem que as tardes finalmente ficaram leves. |
| T16 | Comment yes if your afternoons feel sluggish too, and follow me so you have this recipe when Sunday comes. | Comente yes se as suas tardes também são lentas, e me siga pra ter essa receita quando o domingo chegar. |
| T17 | Search Natural Rems Sea Moss on Amazon. Or you can just tap the link I left in the caption. | Procure Natural Rems Sea Moss na Amazon. Ou é só tocar no link que eu deixei na legenda. |

## 7. Roteiro final em inglês

1. Did you know, if you grate two large carrots into a bowl,
2. mix in one cup of oats,
3. two eggs,
4. a quarter cup of raw honey,
5. and a teaspoon of cinnamon.
6. Then pour the batter into a muffin tin.
7. You end up with soft, moist muffins that taste like carrot cake but are loaded with fiber and have zero flour and zero refined sugar.
8. The oats feed the good bacteria in your gut
9. and the carrots are full of prebiotic fiber. It keeps everything moving so you stop feeling backed up and sluggish by the afternoon.
10. I make a batch every Sunday morning and eat them all week. But some weeks the batch runs out early, and that sluggish afternoon comes right back.
11. So I added one thing that does the same job with no oven: sea moss. It's a sea plant that feeds the same good bacteria in your gut.
12. But be careful, most sea moss gummies are loaded with sugar, which undoes the whole point of a zero sugar muffin, and the raw stuff tastes like seawater.
13. The one I trust is Natural Rems Sea Moss. It's made in the USA with wild Irish sea moss, plus ginger, dandelion and apple cider vinegar.
14. One green apple gummy a day, under a gram of sugar, no seaweed taste. It covers the days the muffins run out, and every other day too.
15. My clients keep it right next to their Sunday muffins, and the ones who stuck with it tell me their afternoons finally feel light.
16. Comment yes if your afternoons feel sluggish too, and follow me so you have this recipe when Sunday comes.
17. Search Natural Rems Sea Moss on Amazon. Or you can just tap the link I left in the caption.

Did you know, if you grate two large carrots into a bowl, mix in one cup of oats, two eggs, a quarter cup of raw honey, and a teaspoon of cinnamon. Then pour the batter into a muffin tin. You end up with soft, moist muffins that taste like carrot cake but are loaded with fiber and have zero flour and zero refined sugar. The oats feed the good bacteria in your gut and the carrots are full of prebiotic fiber. It keeps everything moving so you stop feeling backed up and sluggish by the afternoon. I make a batch every Sunday morning and eat them all week. But some weeks the batch runs out early, and that sluggish afternoon comes right back. So I added one thing that does the same job with no oven: sea moss. It's a sea plant that feeds the same good bacteria in your gut. But be careful, most sea moss gummies are loaded with sugar, which undoes the whole point of a zero sugar muffin, and the raw stuff tastes like seawater. The one I trust is Natural Rems Sea Moss. It's made in the USA with wild Irish sea moss, plus ginger, dandelion and apple cider vinegar. One green apple gummy a day, under a gram of sugar, no seaweed taste. It covers the days the muffins run out, and every other day too. My clients keep it right next to their Sunday muffins, and the ones who stuck with it tell me their afternoons finally feel light. Comment yes if your afternoons feel sluggish too, and follow me so you have this recipe when Sunday comes. Search Natural Rems Sea Moss on Amazon. Or you can just tap the link I left in the caption.
