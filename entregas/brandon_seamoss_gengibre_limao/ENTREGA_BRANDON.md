# ENTREGA | holistic.brandon | Natural Rems Sea Moss Venda, gengibre e limão em cubos de freezer

Produção `brandon_seamoss_gengibre_limao` · Ângulo 1 (Natural Rems Sea Moss) · VENDA · rodada de VALIDAÇÃO · perfil CLÁSSICO

## 1. INSTRUÇÕES PARA A MEMÓRIA DO AGENTE · GOOGLE FLOW AI (v18)

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

### AURALY, character sheet e cenario do video modelo (Luigi, 2026-10-04; vale SO no Auraly)

Roster Auraly: Avery Knox, Devon Price, Jordan Vale e Morgan Vance. Desde a v18 todo K Auraly leva
DOIS anexos: 1) o CHARACTER SHEET do avatar ativo (close do rosto mais frente, costas e os dois lados,
fundo cinza), que trava identidade, corpo e roupa; 2) o frame do video modelo do mesmo codigo, que e a
referencia de cenario, angulo de camera e enquadramento. O cenario e o angulo sao os do video modelo,
quase 100% fieis, e vem tambem escritos no texto do K. Nunca copiar o fundo cinza do sheet para a
cena, nunca trocar o cenario descrito no K e nunca copiar a pessoa, a roupa ou o texto de tela do
frame do modelo. Tudo organico: nada sobrenatural (brilho magico, aura, particulas, objeto flutuando,
efeito visual) que o texto do K nao peca. FitWell e Sea Moss (perfil CLASSICO) continuam com a anchor em cena
real e o avatar fixo por conta abaixo.

(Historico ate a v17:) A referencia de cada um era a anchor em cena real, anexada em todo K.

AVATAR FIXO POR CONTA (v16, 2026-09-25; no Auraly so a ROUPA continua fixa desde a v18): cada conta usa o mesmo avatar com a roupa e o cenario-base
da anchor em todo video e em todo gancho. O texto do K descreve esse cenario e essa roupa. Quando o
video modelo tem uma cena em outro lugar, o texto do K descreve o lugar novo e manda usar a anchor
para identidade e roupa; a pessoa e a roupa nunca mudam. O angulo de camera serve a acao estrutural
preservada: pode ser exotico quando aumenta a anomalia, mas pode se repetir entre variacoes para
preservar composicao e timing. Mudar o angulo conta como a unica variavel dessa variacao.

No T1, a anomalia visual domina. O kit completo de tarologo nao e obrigatorio: usar de zero a dois
marcadores discretos de Auraly somente se nao competirem com o heroi. Desde a v18 (Luigi, 2026-10-04)
nao ha efeito visual nem nada sobrenatural, salvo quando o proprio video modelo tem e o texto do V
pede; efeitos multiplos ou cinematograficos continuam proibidos. Do T2 ao CTA, volta o kit de credencial visual
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

Checklist de envio: 32/32 aprovados (N/A: A1 a A4, A10 e A13 fiéis ao modelo na rodada de validação, sem arquivo de ganchos de variação; C3 sem segunda pessoa; C4 sem selfie; C6 sem cena atuada; C7 sem motion control)

Ficha: 16/16 K conferidos contra o frame do modelo, placar F1 a F6 + G1 a G8 completo em cada um, com evidência literal (G2 N/A: sem céu nem janela em quadro) (`FICHA_FRAMES.md`, GATE_VISUAL Parte 6)

## Mapa de anexos

- **Todos os K:** âncora `producao/_ancoras/holistic_brandon_ancora.jpg` + frame do modelo de mesmo número (só composição).
- **K13 a K16:** também a foto do produto `producao/_ancoras/natural_rems_seamoss_produto.jpg` (só o pote da frente).
- K01 a K16 casam com V01 a V16 pelo número. V03, V05, V06 e V09 são inserts mudos; V02, V04, V07 e V11 são B-roll com a fala como voz-over na edição.

| Código | Take | Anexar, nesta ordem |
|---|---|---|
| K01 / V01 | T1, gancho, limão e zester colados na lente | ÂNCORA HOLISTIC BRANDON `producao/_ancoras/holistic_brandon_ancora.jpg` + FRAME DO MODELO `input/frames_modelo/K01_modelo.png` (só composição) |
| K02 / V02 | T2, receita, faca cortando o limão | ÂNCORA HOLISTIC BRANDON `producao/_ancoras/holistic_brandon_ancora.jpg` + FRAME DO MODELO `input/frames_modelo/K02_modelo.png` (só composição) |
| K03 / V03 | T3, insert, gomos de limão em macro | ÂNCORA HOLISTIC BRANDON `producao/_ancoras/holistic_brandon_ancora.jpg` + FRAME DO MODELO `input/frames_modelo/K03_modelo.png` (só composição) |
| K04 / V04 | T4, receita, descascando o gengibre | ÂNCORA HOLISTIC BRANDON `producao/_ancoras/holistic_brandon_ancora.jpg` + FRAME DO MODELO `input/frames_modelo/K04_modelo.png` (só composição) |
| K05 / V05 | T5, insert, limão e gengibre no copo | ÂNCORA HOLISTIC BRANDON `producao/_ancoras/holistic_brandon_ancora.jpg` + FRAME DO MODELO `input/frames_modelo/K05_modelo.png` (só composição) |
| K06 / V06 | T6, insert, a água medida entrando | ÂNCORA HOLISTIC BRANDON `producao/_ancoras/holistic_brandon_ancora.jpg` + FRAME DO MODELO `input/frames_modelo/K06_modelo.png` (só composição) |
| K07 / V07 | T7, bate, copo no liquidificador | ÂNCORA HOLISTIC BRANDON `producao/_ancoras/holistic_brandon_ancora.jpg` + FRAME DO MODELO `input/frames_modelo/K07_modelo.png` (só composição) |
| K08 / V08 | T8, resultado, copinho liso colado na lente | ÂNCORA HOLISTIC BRANDON `producao/_ancoras/holistic_brandon_ancora.jpg` + FRAME DO MODELO `input/frames_modelo/K08_modelo.png` (só composição) |
| K09 / V09 | T9, insert, despejando nas forminhas | ÂNCORA HOLISTIC BRANDON `producao/_ancoras/holistic_brandon_ancora.jpg` + FRAME DO MODELO `input/frames_modelo/K09_modelo.png` (só composição) |
| K10 / V10 | T10, fecha, plano aberto das forminhas cheias | ÂNCORA HOLISTIC BRANDON `producao/_ancoras/holistic_brandon_ancora.jpg` + FRAME DO MODELO `input/frames_modelo/K10_modelo.png` (só composição) |
| K11 / V11 | T11, uso, cubo caindo na caneca | ÂNCORA HOLISTIC BRANDON `producao/_ancoras/holistic_brandon_ancora.jpg` + FRAME DO MODELO `input/frames_modelo/K11_modelo.png` (só composição) |
| K12 / V12 | T12, autodiagnóstico, caneca na mão | ÂNCORA HOLISTIC BRANDON `producao/_ancoras/holistic_brandon_ancora.jpg` + FRAME DO MODELO `input/frames_modelo/K12_modelo.png` (só composição) |
| K13 / V13 | T13, oferta, o frasco sobe no nome | ÂNCORA HOLISTIC BRANDON `producao/_ancoras/holistic_brandon_ancora.jpg` + FRAME DO MODELO `input/frames_modelo/K13_modelo.png` (só composição) + FOTO DO PRODUTO `producao/_ancoras/natural_rems_seamoss_produto.jpg` (só o pote da frente) |
| K14 / V14 | T14, prova social da coach | ÂNCORA HOLISTIC BRANDON `producao/_ancoras/holistic_brandon_ancora.jpg` + FRAME DO MODELO `input/frames_modelo/K14_modelo.png` (só composição) + FOTO DO PRODUTO `producao/_ancoras/natural_rems_seamoss_produto.jpg` (só o pote da frente) |
| K15 / V15 | T15, comment yes + follow | ÂNCORA HOLISTIC BRANDON `producao/_ancoras/holistic_brandon_ancora.jpg` + FRAME DO MODELO `input/frames_modelo/K15_modelo.png` (só composição) + FOTO DO PRODUTO `producao/_ancoras/natural_rems_seamoss_produto.jpg` (só o pote da frente) |
| K16 / V16 | T16, CTA da marca | ÂNCORA HOLISTIC BRANDON `producao/_ancoras/holistic_brandon_ancora.jpg` + FRAME DO MODELO `input/frames_modelo/K16_modelo.png` (só composição) + FOTO DO PRODUTO `producao/_ancoras/natural_rems_seamoss_produto.jpg` (só o pote da frente) |

## 2. PROMPTS DE IMAGEM (um bloco por K)

### K01 · T1, gancho, limão e zester colados na lente · anexar ÂNCORA HOLISTIC BRANDON + FRAME DO MODELO

```text
K01
{
  "format": "IMPORTANT: THIS IS IPHONE FOOTAGE. Vertical 9:16.",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "reference_use": "Use the first attached image only for Brandon's exact identity, wardrobe and own garage gym with the black table. Use the second attached image only as a composition reference for the camera position, framing and the action; do not copy its man, his suspenders, bare chest, log cabin, wooden counter or the caption text.",
  "identity_main": "The exact fictional AI character holistic.brandon: Black mixed-race American woman around thirty, athletic and toned, medium light-brown skin with light freckles across the nose and cheeks, dark brown eyes, defined eyebrows, full lips, hair in tight cornrows that turn into long loose braids falling over both shoulders, finished with small wooden and gold beads, a black floral blackwork tattoo sleeve on her right arm, a fine line tattoo on her left inner arm and a small fine-line floral tattoo below her left collarbone.",
  "wardrobe": "Plain white ribbed tank top with nothing printed on it, loose black training shorts, a thin gold chain with a small gold cross pendant and small stud earrings.",
  "scene": "Her own garage gym: a white-painted concrete block wall behind her, a red neon sign reading TRAIN PRAY REPEAT on the wall at the left, a whiteboard with handwritten black marker reading STAY READY. STAY DISCIPLINED. on the right, and a small American flag pinned above the whiteboard, discreet but clearly visible and in focus. In front of her stands a plain matte black table she uses as a kitchen counter.",
  "prop": "In her hands in front of her chest, a bright yellow lemon and a small metal zester that she drags down the lemon skin, one thin curl of yellow peel already hanging off it. On the black table below, a rustic wooden cutting board with a natural wavy edge with a chef's knife on it, two tan ginger roots, a tall empty clear blender cup and a small wicker basket of lemons. Nothing else is on the table.",
  "posture": "Brandon stands upright behind the black table, zesting the lemon at chest height.",
  "composition": "Medium shot from chest height: the phone lens is about 45 centimeters from the lemon and zester, which fill the lower 35 percent of the frame at the center, closer to the camera than her face; her face, shoulders and torso fill the upper part and the table items sit along the bottom edge. The background is reduced by framing, never by blur.",
  "camera": "phone at her chest height, straight-on, standard 1x lens, light handheld",
  "lighting": "Neutral overcast daylight from a large window out of frame, soft even light on her face, hands and the table with no harsh shadows. The red neon glows on the wall but does not tint her skin.",
  "state": "Start frame: Brandon is caught mid-sentence, lips naturally parted, animated expression, looking straight into the lens, eyebrows raised, as if sharing a trick.",
  "realism": "Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday reality, background fully in focus, everything in sharp focus, no AI polish, no beauty smoothing.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no plastic-looking skin, no extra fingers, no third hand, no blur, no bokeh, no warm orange color cast, no yellow tint, no golden glow, no golden hour light, no sunset, no HDR, no cinematic lighting, no beauty smoothing, no visible phone, no studio, no second person, no eyeglasses, no grey t-shirt, no white kitchen cabinets, no marble countertop, no silver cross, no log cabin, no suspenders, no shirtless man, no printed labels or lettering on the cups, trays, board, knife or measuring cup"
}
```

### K02 · T2, receita, faca cortando o limão · anexar ÂNCORA HOLISTIC BRANDON + FRAME DO MODELO

```text
K02
{
  "format": "IMPORTANT: THIS IS IPHONE FOOTAGE. Vertical 9:16.",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "reference_use": "Use the first attached image only for Brandon's exact identity, wardrobe and own garage gym with the black table. Use the second attached image only as a composition reference for the camera position, framing and the action; do not copy its man, his suspenders, bare chest, log cabin, wooden counter or the caption text.",
  "identity_main": "The exact fictional AI character holistic.brandon: Black mixed-race American woman around thirty, athletic and toned, medium light-brown skin with light freckles across the nose and cheeks, dark brown eyes, defined eyebrows, full lips, hair in tight cornrows that turn into long loose braids falling over both shoulders, finished with small wooden and gold beads, a black floral blackwork tattoo sleeve on her right arm, a fine line tattoo on her left inner arm and a small fine-line floral tattoo below her left collarbone.",
  "wardrobe": "Plain white ribbed tank top with nothing printed on it, loose black training shorts, a thin gold chain with a small gold cross pendant and small stud earrings.",
  "scene": "Her own garage gym: a white-painted concrete block wall behind her, a red neon sign reading TRAIN PRAY REPEAT on the wall at the left, a whiteboard with handwritten black marker reading STAY READY. STAY DISCIPLINED. on the right, and a small American flag pinned above the whiteboard, discreet but clearly visible and in focus. In front of her stands a plain matte black table she uses as a kitchen counter.",
  "prop": "On a rustic wooden cutting board with a natural wavy edge in the lower foreground, a bright yellow lemon halfway through being cut in half by a chef's knife held in her right hand while her left hand holds the lemon steady, a curl of peel beside it. Nothing else is on the table.",
  "posture": "Brandon leans over the black table, only her hands, forearms and white tank top visible, cutting the lemon.",
  "composition": "Close shot from chest height: the phone lens is about 30 centimeters from the board, which with the lemon and knife fills the lower 55 percent of the frame, closer to the camera than her torso; her torso and the tattoo sleeve on her right forearm fill the upper part and her face is out of frame. The background is reduced by framing, never by blur.",
  "camera": "phone at her chest height, tilted down toward the board, standard 1x lens, light handheld",
  "lighting": "Neutral overcast daylight from a large window out of frame, soft even light on her face, hands and the table with no harsh shadows. The red neon glows on the wall but does not tint her skin.",
  "state": "Start frame: a faca já na metade do limão.",
  "realism": "Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday reality, background fully in focus, everything in sharp focus, no AI polish, no beauty smoothing.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no plastic-looking skin, no extra fingers, no third hand, no blur, no bokeh, no warm orange color cast, no yellow tint, no golden glow, no golden hour light, no sunset, no HDR, no cinematic lighting, no beauty smoothing, no visible phone, no studio, no second person, no eyeglasses, no grey t-shirt, no white kitchen cabinets, no marble countertop, no silver cross, no log cabin, no suspenders, no shirtless man, no printed labels or lettering on the cups, trays, board, knife or measuring cup"
}
```

### K03 · T3, insert, gomos de limão em macro · anexar ÂNCORA HOLISTIC BRANDON + FRAME DO MODELO

```text
K03
{
  "format": "IMPORTANT: THIS IS IPHONE FOOTAGE. Vertical 9:16.",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "reference_use": "Use the first attached image only for Brandon's exact identity, wardrobe and own garage gym with the black table. Use the second attached image only as a composition reference for the camera position, framing and the action; do not copy its man, his suspenders, bare chest, log cabin, wooden counter or the caption text.",
  "identity_main": "The exact fictional AI character holistic.brandon: Black mixed-race American woman around thirty, athletic and toned, medium light-brown skin with light freckles across the nose and cheeks, dark brown eyes, defined eyebrows, full lips, hair in tight cornrows that turn into long loose braids falling over both shoulders, finished with small wooden and gold beads, a black floral blackwork tattoo sleeve on her right arm, a fine line tattoo on her left inner arm and a small fine-line floral tattoo below her left collarbone.",
  "wardrobe": "Plain white ribbed tank top with nothing printed on it, loose black training shorts, a thin gold chain with a small gold cross pendant and small stud earrings.",
  "scene": "Her own garage gym: a white-painted concrete block wall behind her, a red neon sign reading TRAIN PRAY REPEAT on the wall at the left, a whiteboard with handwritten black marker reading STAY READY. STAY DISCIPLINED. on the right, and a small American flag pinned above the whiteboard, discreet but clearly visible and in focus. In front of her stands a plain matte black table she uses as a kitchen counter.",
  "prop": "On a rustic wooden cutting board with a natural wavy edge, a heap of freshly cut lemon wedges with glistening juicy flesh and thin white pith, one half lemon with its cut face turned to the lens. Her fingertips rest at the edge of the pile. Nothing else is on the table.",
  "posture": "Brandon leans over the black table, only her fingertips visible beside the wedges.",
  "composition": "Extreme close shot: the phone lens is about 20 centimeters from the wedges, which fill about 85 percent of the frame, closer to the camera than anything else; only a strip of her white tank top shows at the top edge and her face is out of frame. The background is reduced by framing, never by blur.",
  "camera": "phone at table height, tilted down toward the wedges, standard 1x lens, light handheld",
  "lighting": "Neutral overcast daylight from a large window out of frame, soft even light on her face, hands and the table with no harsh shadows. The red neon glows on the wall but does not tint her skin.",
  "state": "Start frame: a pilha de gomos de limão preenchendo o quadro.",
  "realism": "Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday reality, background fully in focus, everything in sharp focus, no AI polish, no beauty smoothing.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no plastic-looking skin, no extra fingers, no third hand, no blur, no bokeh, no warm orange color cast, no yellow tint, no golden glow, no golden hour light, no sunset, no HDR, no cinematic lighting, no beauty smoothing, no visible phone, no studio, no second person, no eyeglasses, no grey t-shirt, no white kitchen cabinets, no marble countertop, no silver cross, no log cabin, no suspenders, no shirtless man, no printed labels or lettering on the cups, trays, board, knife or measuring cup"
}
```

### K04 · T4, receita, descascando o gengibre · anexar ÂNCORA HOLISTIC BRANDON + FRAME DO MODELO

```text
K04
{
  "format": "IMPORTANT: THIS IS IPHONE FOOTAGE. Vertical 9:16.",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "reference_use": "Use the first attached image only for Brandon's exact identity, wardrobe and own garage gym with the black table. Use the second attached image only as a composition reference for the camera position, framing and the action; do not copy its man, his suspenders, bare chest, log cabin, wooden counter or the caption text.",
  "identity_main": "The exact fictional AI character holistic.brandon: Black mixed-race American woman around thirty, athletic and toned, medium light-brown skin with light freckles across the nose and cheeks, dark brown eyes, defined eyebrows, full lips, hair in tight cornrows that turn into long loose braids falling over both shoulders, finished with small wooden and gold beads, a black floral blackwork tattoo sleeve on her right arm, a fine line tattoo on her left inner arm and a small fine-line floral tattoo below her left collarbone.",
  "wardrobe": "Plain white ribbed tank top with nothing printed on it, loose black training shorts, a thin gold chain with a small gold cross pendant and small stud earrings.",
  "scene": "Her own garage gym: a white-painted concrete block wall behind her, a red neon sign reading TRAIN PRAY REPEAT on the wall at the left, a whiteboard with handwritten black marker reading STAY READY. STAY DISCIPLINED. on the right, and a small American flag pinned above the whiteboard, discreet but clearly visible and in focus. In front of her stands a plain matte black table she uses as a kitchen counter.",
  "prop": "In her hands, a knobby tan ginger root that she peels with a small paring knife held in her right hand, thin tan shavings falling onto the cutting board in the lower foreground. Nothing else is on the table.",
  "posture": "Brandon leans over the black table, only her hands, forearms and white tank top visible, peeling the ginger.",
  "composition": "Close shot from chest height: the phone lens is about 25 centimeters from her hands and the ginger root, which fill the lower 60 percent of the frame, closer to the camera than her torso; her torso fills the upper part and her face is out of frame. The background is reduced by framing, never by blur.",
  "camera": "phone at her chest height, tilted down toward her hands, standard 1x lens, light handheld",
  "lighting": "Neutral overcast daylight from a large window out of frame, soft even light on her face, hands and the table with no harsh shadows. The red neon glows on the wall but does not tint her skin.",
  "state": "Start frame: a faquinha no meio da casca, primeiras casquinhas na tábua.",
  "realism": "Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday reality, background fully in focus, everything in sharp focus, no AI polish, no beauty smoothing.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no plastic-looking skin, no extra fingers, no third hand, no blur, no bokeh, no warm orange color cast, no yellow tint, no golden glow, no golden hour light, no sunset, no HDR, no cinematic lighting, no beauty smoothing, no visible phone, no studio, no second person, no eyeglasses, no grey t-shirt, no white kitchen cabinets, no marble countertop, no silver cross, no log cabin, no suspenders, no shirtless man, no printed labels or lettering on the cups, trays, board, knife or measuring cup"
}
```

### K05 · T5, insert, limão e gengibre no copo · anexar ÂNCORA HOLISTIC BRANDON + FRAME DO MODELO

```text
K05
{
  "format": "IMPORTANT: THIS IS IPHONE FOOTAGE. Vertical 9:16.",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "reference_use": "Use the first attached image only for Brandon's exact identity, wardrobe and own garage gym with the black table. Use the second attached image only as a composition reference for the camera position, framing and the action; do not copy its man, his suspenders, bare chest, log cabin, wooden counter or the caption text.",
  "identity_main": "The exact fictional AI character holistic.brandon: Black mixed-race American woman around thirty, athletic and toned, medium light-brown skin with light freckles across the nose and cheeks, dark brown eyes, defined eyebrows, full lips, hair in tight cornrows that turn into long loose braids falling over both shoulders, finished with small wooden and gold beads, a black floral blackwork tattoo sleeve on her right arm, a fine line tattoo on her left inner arm and a small fine-line floral tattoo below her left collarbone.",
  "wardrobe": "Plain white ribbed tank top with nothing printed on it, loose black training shorts, a thin gold chain with a small gold cross pendant and small stud earrings.",
  "scene": "Her own garage gym: a white-painted concrete block wall behind her, a red neon sign reading TRAIN PRAY REPEAT on the wall at the left, a whiteboard with handwritten black marker reading STAY READY. STAY DISCIPLINED. on the right, and a small American flag pinned above the whiteboard, discreet but clearly visible and in focus. In front of her stands a plain matte black table she uses as a kitchen counter.",
  "prop": "On the black table in the lower center, a tall clear plastic blender cup with a ridged wall filled to the top with chopped lemon wedges and small pieces of ginger, clear plastic walls and a wide open mouth, her hand just lifting away from the rim. Nothing else is on the table.",
  "posture": "Brandon stands behind the black table, torso visible, one hand just lifting away from the blender cup.",
  "composition": "Straight-on close shot from table height: the phone lens is about 40 centimeters from the cup, which fills the lower 65 percent of the frame, closer to the camera than her torso; her torso fills the upper part and her face is out of frame. The background is reduced by framing, never by blur.",
  "camera": "phone propped at table height, straight-on, standard 1x lens, light handheld",
  "lighting": "Neutral overcast daylight from a large window out of frame, soft even light on her face, hands and the table with no harsh shadows. The red neon glows on the wall but does not tint her skin.",
  "state": "Start frame: o copo cheio, a mão se afastando da borda.",
  "realism": "Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday reality, background fully in focus, everything in sharp focus, no AI polish, no beauty smoothing.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no plastic-looking skin, no extra fingers, no third hand, no blur, no bokeh, no warm orange color cast, no yellow tint, no golden glow, no golden hour light, no sunset, no HDR, no cinematic lighting, no beauty smoothing, no visible phone, no studio, no second person, no eyeglasses, no grey t-shirt, no white kitchen cabinets, no marble countertop, no silver cross, no log cabin, no suspenders, no shirtless man, no printed labels or lettering on the cups, trays, board, knife or measuring cup"
}
```

### K06 · T6, insert, a água medida entrando · anexar ÂNCORA HOLISTIC BRANDON + FRAME DO MODELO

```text
K06
{
  "format": "IMPORTANT: THIS IS IPHONE FOOTAGE. Vertical 9:16.",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "reference_use": "Use the first attached image only for Brandon's exact identity, wardrobe and own garage gym with the black table. Use the second attached image only as a composition reference for the camera position, framing and the action; do not copy its man, his suspenders, bare chest, log cabin, wooden counter or the caption text.",
  "identity_main": "The exact fictional AI character holistic.brandon: Black mixed-race American woman around thirty, athletic and toned, medium light-brown skin with light freckles across the nose and cheeks, dark brown eyes, defined eyebrows, full lips, hair in tight cornrows that turn into long loose braids falling over both shoulders, finished with small wooden and gold beads, a black floral blackwork tattoo sleeve on her right arm, a fine line tattoo on her left inner arm and a small fine-line floral tattoo below her left collarbone.",
  "wardrobe": "Plain white ribbed tank top with nothing printed on it, loose black training shorts, a thin gold chain with a small gold cross pendant and small stud earrings.",
  "scene": "Her own garage gym: a white-painted concrete block wall behind her, a red neon sign reading TRAIN PRAY REPEAT on the wall at the left, a whiteboard with handwritten black marker reading STAY READY. STAY DISCIPLINED. on the right, and a small American flag pinned above the whiteboard, discreet but clearly visible and in focus. In front of her stands a plain matte black table she uses as a kitchen counter.",
  "prop": "On the black table in the lower center, a tall clear plastic blender cup with a ridged wall full of lemon wedges and ginger. From above, her right hand tilts a small metal measuring cup with a handle and a thin stream of clear water starts pouring into the blender cup. Nothing else is on the table.",
  "posture": "Brandon stands behind the black table, torso visible, pouring water from the measuring cup.",
  "composition": "Straight-on close shot from table height: the phone lens is about 40 centimeters from the cup, which fills the lower 60 percent of the frame, closer to the camera than her torso; the measuring cup enters from the top; her face is out of frame. The background is reduced by framing, never by blur.",
  "camera": "phone propped at table height, straight-on, standard 1x lens, light handheld",
  "lighting": "Neutral overcast daylight from a large window out of frame, soft even light on her face, hands and the table with no harsh shadows. The red neon glows on the wall but does not tint her skin.",
  "state": "Start frame: o primeiro fio de água saindo da medida.",
  "realism": "Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday reality, background fully in focus, everything in sharp focus, no AI polish, no beauty smoothing.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no plastic-looking skin, no extra fingers, no third hand, no blur, no bokeh, no warm orange color cast, no yellow tint, no golden glow, no golden hour light, no sunset, no HDR, no cinematic lighting, no beauty smoothing, no visible phone, no studio, no second person, no eyeglasses, no grey t-shirt, no white kitchen cabinets, no marble countertop, no silver cross, no log cabin, no suspenders, no shirtless man, no printed labels or lettering on the cups, trays, board, knife or measuring cup"
}
```

### K07 · T7, bate, copo no liquidificador · anexar ÂNCORA HOLISTIC BRANDON + FRAME DO MODELO

```text
K07
{
  "format": "IMPORTANT: THIS IS IPHONE FOOTAGE. Vertical 9:16.",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "reference_use": "Use the first attached image only for Brandon's exact identity, wardrobe and own garage gym with the black table. Use the second attached image only as a composition reference for the camera position, framing and the action; do not copy its man, his suspenders, bare chest, log cabin, wooden counter or the caption text.",
  "identity_main": "The exact fictional AI character holistic.brandon: Black mixed-race American woman around thirty, athletic and toned, medium light-brown skin with light freckles across the nose and cheeks, dark brown eyes, defined eyebrows, full lips, hair in tight cornrows that turn into long loose braids falling over both shoulders, finished with small wooden and gold beads, a black floral blackwork tattoo sleeve on her right arm, a fine line tattoo on her left inner arm and a small fine-line floral tattoo below her left collarbone.",
  "wardrobe": "Plain white ribbed tank top with nothing printed on it, loose black training shorts, a thin gold chain with a small gold cross pendant and small stud earrings.",
  "scene": "Her own garage gym: a white-painted concrete block wall behind her, a red neon sign reading TRAIN PRAY REPEAT on the wall at the left, a whiteboard with handwritten black marker reading STAY READY. STAY DISCIPLINED. on the right, and a small American flag pinned above the whiteboard, discreet but clearly visible and in focus. In front of her stands a plain matte black table she uses as a kitchen counter.",
  "prop": "On the black table, the blender cup turned upside down and locked on a black blender base, the chopped lemon and ginger inside swirling, her right palm pressed flat on top of the cup. Nothing else is on the table.",
  "posture": "Brandon stands behind the black table, torso visible, her right palm pressed flat on top of the blender.",
  "composition": "Straight-on close shot from table height: the phone lens is about 35 centimeters from the blender, which fills the lower 70 percent of the frame, closer to the camera than her torso; her torso fills the top strip and her face is out of frame. The background is reduced by framing, never by blur.",
  "camera": "phone propped at table height, straight-on, standard 1x lens, light handheld",
  "lighting": "Neutral overcast daylight from a large window out of frame, soft even light on her face, hands and the table with no harsh shadows. The red neon glows on the wall but does not tint her skin.",
  "state": "Start frame: o limão e o gengibre já girando dentro do copo.",
  "realism": "Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday reality, background fully in focus, everything in sharp focus, no AI polish, no beauty smoothing.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no plastic-looking skin, no extra fingers, no third hand, no blur, no bokeh, no warm orange color cast, no yellow tint, no golden glow, no golden hour light, no sunset, no HDR, no cinematic lighting, no beauty smoothing, no visible phone, no studio, no second person, no eyeglasses, no grey t-shirt, no white kitchen cabinets, no marble countertop, no silver cross, no log cabin, no suspenders, no shirtless man, no printed labels or lettering on the cups, trays, board, knife or measuring cup"
}
```

### K08 · T8, resultado, copinho liso colado na lente · anexar ÂNCORA HOLISTIC BRANDON + FRAME DO MODELO

```text
K08
{
  "format": "IMPORTANT: THIS IS IPHONE FOOTAGE. Vertical 9:16.",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "reference_use": "Use the first attached image only for Brandon's exact identity, wardrobe and own garage gym with the black table. Use the second attached image only as a composition reference for the camera position, framing and the action; do not copy its man, his suspenders, bare chest, log cabin, wooden counter or the caption text.",
  "identity_main": "The exact fictional AI character holistic.brandon: Black mixed-race American woman around thirty, athletic and toned, medium light-brown skin with light freckles across the nose and cheeks, dark brown eyes, defined eyebrows, full lips, hair in tight cornrows that turn into long loose braids falling over both shoulders, finished with small wooden and gold beads, a black floral blackwork tattoo sleeve on her right arm, a fine line tattoo on her left inner arm and a small fine-line floral tattoo below her left collarbone.",
  "wardrobe": "Plain white ribbed tank top with nothing printed on it, loose black training shorts, a thin gold chain with a small gold cross pendant and small stud earrings.",
  "scene": "Her own garage gym: a white-painted concrete block wall behind her, a red neon sign reading TRAIN PRAY REPEAT on the wall at the left, a whiteboard with handwritten black marker reading STAY READY. STAY DISCIPLINED. on the right, and a small American flag pinned above the whiteboard, discreet but clearly visible and in focus. In front of her stands a plain matte black table she uses as a kitchen counter.",
  "prop": "In her hands, held toward the lens, a small clear plastic blender cup with a lid ring, about a third full of a smooth pale cream-yellow mixture with tiny flecks of fiber. Her other hand gestures open. Nothing else is on the table.",
  "posture": "Brandon leans forward over the black table toward the lens, holding the small cup of mixture.",
  "composition": "Close shot from chest height: the phone lens is about 30 centimeters from the cup, which fills the lower 35 percent of the frame in the lower right, closer to the camera than her face; her face fills the upper half. The background is reduced by framing, never by blur.",
  "camera": "phone at her chest height, straight-on, standard 1x lens, light handheld",
  "lighting": "Neutral overcast daylight from a large window out of frame, soft even light on her face, hands and the table with no harsh shadows. The red neon glows on the wall but does not tint her skin.",
  "state": "Start frame: Brandon is caught mid-sentence, lips naturally parted, animated expression, looking straight into the lens, lively, relaxed, a little proud.",
  "realism": "Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday reality, background fully in focus, everything in sharp focus, no AI polish, no beauty smoothing.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no plastic-looking skin, no extra fingers, no third hand, no blur, no bokeh, no warm orange color cast, no yellow tint, no golden glow, no golden hour light, no sunset, no HDR, no cinematic lighting, no beauty smoothing, no visible phone, no studio, no second person, no eyeglasses, no grey t-shirt, no white kitchen cabinets, no marble countertop, no silver cross, no log cabin, no suspenders, no shirtless man, no printed labels or lettering on the cups, trays, board, knife or measuring cup"
}
```

### K09 · T9, insert, despejando nas forminhas · anexar ÂNCORA HOLISTIC BRANDON + FRAME DO MODELO

```text
K09
{
  "format": "IMPORTANT: THIS IS IPHONE FOOTAGE. Vertical 9:16.",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "reference_use": "Use the first attached image only for Brandon's exact identity, wardrobe and own garage gym with the black table. Use the second attached image only as a composition reference for the camera position, framing and the action; do not copy its man, his suspenders, bare chest, log cabin, wooden counter or the caption text.",
  "identity_main": "The exact fictional AI character holistic.brandon: Black mixed-race American woman around thirty, athletic and toned, medium light-brown skin with light freckles across the nose and cheeks, dark brown eyes, defined eyebrows, full lips, hair in tight cornrows that turn into long loose braids falling over both shoulders, finished with small wooden and gold beads, a black floral blackwork tattoo sleeve on her right arm, a fine line tattoo on her left inner arm and a small fine-line floral tattoo below her left collarbone.",
  "wardrobe": "Plain white ribbed tank top with nothing printed on it, loose black training shorts, a thin gold chain with a small gold cross pendant and small stud earrings.",
  "scene": "Her own garage gym: a white-painted concrete block wall behind her, a red neon sign reading TRAIN PRAY REPEAT on the wall at the left, a whiteboard with handwritten black marker reading STAY READY. STAY DISCIPLINED. on the right, and a small American flag pinned above the whiteboard, discreet but clearly visible and in focus. In front of her stands a plain matte black table she uses as a kitchen counter.",
  "prop": "On the black table in the lower foreground, two white plastic ice cube trays side by side, each cavity partly filled with smooth pale cream-yellow mixture. From the upper right, her hand tilts a small clear plastic blender cup and the last of the mixture runs into the trays. Nothing else is on the table.",
  "posture": "Brandon stands behind the black table, torso visible, pouring the mixture into the ice trays.",
  "composition": "Straight-on close shot from table height: the phone lens is about 35 centimeters from the trays, which fill the lower 55 percent of the frame, closer to the camera than her torso; the cup enters from the upper right and her face is out of frame. The background is reduced by framing, never by blur.",
  "camera": "phone propped at table height, straight-on, standard 1x lens, light handheld",
  "lighting": "Neutral overcast daylight from a large window out of frame, soft even light on her face, hands and the table with no harsh shadows. The red neon glows on the wall but does not tint her skin.",
  "state": "Start frame: a mistura caindo na última cavidade.",
  "realism": "Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday reality, background fully in focus, everything in sharp focus, no AI polish, no beauty smoothing.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no plastic-looking skin, no extra fingers, no third hand, no blur, no bokeh, no warm orange color cast, no yellow tint, no golden glow, no golden hour light, no sunset, no HDR, no cinematic lighting, no beauty smoothing, no visible phone, no studio, no second person, no eyeglasses, no grey t-shirt, no white kitchen cabinets, no marble countertop, no silver cross, no log cabin, no suspenders, no shirtless man, no printed labels or lettering on the cups, trays, board, knife or measuring cup"
}
```

### K10 · T10, fecha, plano aberto das forminhas cheias · anexar ÂNCORA HOLISTIC BRANDON + FRAME DO MODELO

```text
K10
{
  "format": "IMPORTANT: THIS IS IPHONE FOOTAGE. Vertical 9:16.",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "reference_use": "Use the first attached image only for Brandon's exact identity, wardrobe and own garage gym with the black table. Use the second attached image only as a composition reference for the camera position, framing and the action; do not copy its man, his suspenders, bare chest, log cabin, wooden counter or the caption text.",
  "identity_main": "The exact fictional AI character holistic.brandon: Black mixed-race American woman around thirty, athletic and toned, medium light-brown skin with light freckles across the nose and cheeks, dark brown eyes, defined eyebrows, full lips, hair in tight cornrows that turn into long loose braids falling over both shoulders, finished with small wooden and gold beads, a black floral blackwork tattoo sleeve on her right arm, a fine line tattoo on her left inner arm and a small fine-line floral tattoo below her left collarbone.",
  "wardrobe": "Plain white ribbed tank top with nothing printed on it, loose black training shorts, a thin gold chain with a small gold cross pendant and small stud earrings.",
  "scene": "Her own garage gym: a white-painted concrete block wall behind her, a red neon sign reading TRAIN PRAY REPEAT on the wall at the left, a whiteboard with handwritten black marker reading STAY READY. STAY DISCIPLINED. on the right, and a small American flag pinned above the whiteboard, discreet but clearly visible and in focus. In front of her stands a plain matte black table she uses as a kitchen counter.",
  "prop": "On the black table in the lower foreground, two white plastic ice cube trays side by side full of pale cream-yellow cubes, and a tall empty clear blender cup on the left. Her hands rest on the table edge. Nothing else is on the table.",
  "posture": "Brandon stands behind the black table leaning slightly forward with both hands on the table edge.",
  "composition": "Straight-on wide shot from table height: the phone lens is about 60 centimeters from the trays, which fill the lower 30 percent of the frame, closer to the camera than her face, and she fills the upper two thirds from the thighs up. The background is reduced by framing, never by blur.",
  "camera": "phone propped at table height about 1 meter from her, standard 1x lens, level",
  "lighting": "Neutral overcast daylight from a large window out of frame, soft even light on her face, hands and the table with no harsh shadows. The red neon glows on the wall but does not tint her skin.",
  "state": "Start frame: Brandon is caught mid-sentence, lips naturally parted, animated expression, looking straight into the lens, smiling, satisfied.",
  "realism": "Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday reality, background fully in focus, everything in sharp focus, no AI polish, no beauty smoothing.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no plastic-looking skin, no extra fingers, no third hand, no blur, no bokeh, no warm orange color cast, no yellow tint, no golden glow, no golden hour light, no sunset, no HDR, no cinematic lighting, no beauty smoothing, no visible phone, no studio, no second person, no eyeglasses, no grey t-shirt, no white kitchen cabinets, no marble countertop, no silver cross, no log cabin, no suspenders, no shirtless man, no printed labels or lettering on the cups, trays, board, knife or measuring cup"
}
```

### K11 · T11, uso, cubo caindo na caneca · anexar ÂNCORA HOLISTIC BRANDON + FRAME DO MODELO

```text
K11
{
  "format": "IMPORTANT: THIS IS IPHONE FOOTAGE. Vertical 9:16.",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "reference_use": "Use the first attached image only for Brandon's exact identity, wardrobe and own garage gym with the black table. Use the second attached image only as a composition reference for the camera position, framing and the action; do not copy its man, his suspenders, bare chest, log cabin, wooden counter or the caption text.",
  "identity_main": "The exact fictional AI character holistic.brandon: Black mixed-race American woman around thirty, athletic and toned, medium light-brown skin with light freckles across the nose and cheeks, dark brown eyes, defined eyebrows, full lips, hair in tight cornrows that turn into long loose braids falling over both shoulders, finished with small wooden and gold beads, a black floral blackwork tattoo sleeve on her right arm, a fine line tattoo on her left inner arm and a small fine-line floral tattoo below her left collarbone.",
  "wardrobe": "Plain white ribbed tank top with nothing printed on it, loose black training shorts, a thin gold chain with a small gold cross pendant and small stud earrings.",
  "scene": "Her own garage gym: a white-painted concrete block wall behind her, a red neon sign reading TRAIN PRAY REPEAT on the wall at the left, a whiteboard with handwritten black marker reading STAY READY. STAY DISCIPLINED. on the right, and a small American flag pinned above the whiteboard, discreet but clearly visible and in focus. In front of her stands a plain matte black table she uses as a kitchen counter.",
  "prop": "On the black table in the lower center, a clear thick glass mug with a handle, empty, with a bright yellow lemon beside it. One pale cream-yellow ice cube dropped from her fingers is falling into the mug from above. Nothing else is on the table.",
  "posture": "Brandon stands behind the black table, torso visible, her fingers just letting go of the cube above the mug.",
  "composition": "Straight-on close shot from table height: the phone lens is about 30 centimeters from the mug, which fills the lower 60 percent of the frame, closer to the camera than her torso; her torso fills the upper part and her face is out of frame. The background is reduced by framing, never by blur.",
  "camera": "phone propped at table height, straight-on, standard 1x lens, light handheld",
  "lighting": "Neutral overcast daylight from a large window out of frame, soft even light on her face, hands and the table with no harsh shadows. The red neon glows on the wall but does not tint her skin.",
  "state": "Start frame: o cubo no ar, logo acima da caneca.",
  "realism": "Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday reality, background fully in focus, everything in sharp focus, no AI polish, no beauty smoothing.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no plastic-looking skin, no extra fingers, no third hand, no blur, no bokeh, no warm orange color cast, no yellow tint, no golden glow, no golden hour light, no sunset, no HDR, no cinematic lighting, no beauty smoothing, no visible phone, no studio, no second person, no eyeglasses, no grey t-shirt, no white kitchen cabinets, no marble countertop, no silver cross, no log cabin, no suspenders, no shirtless man, no printed labels or lettering on the cups, trays, board, knife or measuring cup"
}
```

### K12 · T12, autodiagnóstico, caneca na mão · anexar ÂNCORA HOLISTIC BRANDON + FRAME DO MODELO

```text
K12
{
  "format": "IMPORTANT: THIS IS IPHONE FOOTAGE. Vertical 9:16.",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "reference_use": "Use the first attached image only for Brandon's exact identity, wardrobe and own garage gym with the black table. Use the second attached image only as a composition reference for the camera position, framing and the action; do not copy its man, his suspenders, bare chest, log cabin, wooden counter or the caption text.",
  "identity_main": "The exact fictional AI character holistic.brandon: Black mixed-race American woman around thirty, athletic and toned, medium light-brown skin with light freckles across the nose and cheeks, dark brown eyes, defined eyebrows, full lips, hair in tight cornrows that turn into long loose braids falling over both shoulders, finished with small wooden and gold beads, a black floral blackwork tattoo sleeve on her right arm, a fine line tattoo on her left inner arm and a small fine-line floral tattoo below her left collarbone.",
  "wardrobe": "Plain white ribbed tank top with nothing printed on it, loose black training shorts, a thin gold chain with a small gold cross pendant and small stud earrings.",
  "scene": "Her own garage gym: a white-painted concrete block wall behind her, a red neon sign reading TRAIN PRAY REPEAT on the wall at the left, a whiteboard with handwritten black marker reading STAY READY. STAY DISCIPLINED. on the right, and a small American flag pinned above the whiteboard, discreet but clearly visible and in focus. In front of her stands a plain matte black table she uses as a kitchen counter.",
  "prop": "In her right hand, held at chest height, a clear thick glass mug with a handle about half full of a pale cream-yellow drink. On the black table in the lower foreground, two white plastic ice cube trays side by side full of cubes and a tall empty clear blender cup. Nothing else is on the table.",
  "posture": "Brandon stands behind the black table with the mug in her right hand, her left hand open.",
  "composition": "Straight-on medium shot: the phone lens is about 55 centimeters from the mug, which she holds at chest height and which fills about 20 percent of the frame at the lower right, closer to the camera than her face; the trays fill the lower 25 percent of the frame; her face and shoulders fill the upper half. The background is reduced by framing, never by blur.",
  "camera": "phone propped at chest height, straight-on, standard 1x lens, light handheld",
  "lighting": "Neutral overcast daylight from a large window out of frame, soft even light on her face, hands and the table with no harsh shadows. The red neon glows on the wall but does not tint her skin.",
  "state": "Start frame: Brandon is caught mid-sentence, lips naturally parted, animated expression, looking straight into the lens, honest, a little challenging, eyebrows raised.",
  "realism": "Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday reality, background fully in focus, everything in sharp focus, no AI polish, no beauty smoothing.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no plastic-looking skin, no extra fingers, no third hand, no blur, no bokeh, no warm orange color cast, no yellow tint, no golden glow, no golden hour light, no sunset, no HDR, no cinematic lighting, no beauty smoothing, no visible phone, no studio, no second person, no eyeglasses, no grey t-shirt, no white kitchen cabinets, no marble countertop, no silver cross, no log cabin, no suspenders, no shirtless man, no printed labels or lettering on the cups, trays, board, knife or measuring cup"
}
```

### K13 · T13, oferta, o frasco sobe no nome · anexar ÂNCORA HOLISTIC BRANDON + FRAME DO MODELO + FOTO DO PRODUTO

```text
K13
{
  "format": "IMPORTANT: THIS IS IPHONE FOOTAGE. Vertical 9:16.",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "reference_use": "Use the first attached image only for Brandon's exact identity, wardrobe and own garage gym with the black table. Use the second attached image only as a composition reference for the camera position, framing and the action; do not copy its man, his suspenders, bare chest, log cabin, wooden counter or the caption text. Use the third attached image only for the Natural Rems Sea Moss jar: copy ONLY the front jar, without the MADE IN USA banner at the top, without the second jar behind it and without the loose gummies.",
  "identity_main": "The exact fictional AI character holistic.brandon: Black mixed-race American woman around thirty, athletic and toned, medium light-brown skin with light freckles across the nose and cheeks, dark brown eyes, defined eyebrows, full lips, hair in tight cornrows that turn into long loose braids falling over both shoulders, finished with small wooden and gold beads, a black floral blackwork tattoo sleeve on her right arm, a fine line tattoo on her left inner arm and a small fine-line floral tattoo below her left collarbone.",
  "wardrobe": "Plain white ribbed tank top with nothing printed on it, loose black training shorts, a thin gold chain with a small gold cross pendant and small stud earrings.",
  "scene": "Her own garage gym: a white-painted concrete block wall behind her, a red neon sign reading TRAIN PRAY REPEAT on the wall at the left, a whiteboard with handwritten black marker reading STAY READY. STAY DISCIPLINED. on the right, and a small American flag pinned above the whiteboard, discreet but clearly visible and in focus. In front of her stands a plain matte black table she uses as a kitchen counter.",
  "prop": "In her right hand, held low just above the black table, the Natural Rems Sea Moss jar: a short wide jar of dark amber plastic with a black screw cap, a pale cream-green label with dark green text, the Natural Rems logo with three leaves, the big title Sea Moss Gummies, a 6000 MG | 16-IN-1 badge, the words GREEN APPLE FLAVOR, a list of ingredients in dark green pill shapes and green seaweed illustrations on both sides, label facing the camera, fully readable. Nothing else is on the table.",
  "posture": "Brandon holds the jar low in her right hand, about to raise it beside her face.",
  "composition": "Straight-on medium shot: the phone lens is about 35 centimeters from the jar, which she holds low in her right hand just above the black table and fills the lower right 20 percent of the frame, closer to the camera than her face; her face and shoulders fill the upper half of the frame. The background is reduced by framing, never by blur.",
  "camera": "phone at her chest height, straight-on, standard 1x lens, light handheld",
  "lighting": "Neutral overcast daylight from a large window out of frame, soft even light on her face, hands and the table with no harsh shadows. The red neon glows on the wall but does not tint her skin.",
  "state": "Start frame: Brandon is caught mid-sentence, lips naturally parted, animated expression, looking straight into the lens, proud, about to show it.",
  "realism": "Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday reality, background fully in focus, everything in sharp focus, no AI polish, no beauty smoothing.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no plastic-looking skin, no extra fingers, no third hand, no blur, no bokeh, no warm orange color cast, no yellow tint, no golden glow, no golden hour light, no sunset, no HDR, no cinematic lighting, no beauty smoothing, no visible phone, no studio, no second person, no eyeglasses, no grey t-shirt, no white kitchen cabinets, no marble countertop, no silver cross, no log cabin, no suspenders, no shirtless man, no second jar, no other bottles, no loose gummies, no banner above the jar, no hand covering the label, no lemons or ginger on the table"
}
```

### K14 · T14, prova social da coach · anexar ÂNCORA HOLISTIC BRANDON + FRAME DO MODELO + FOTO DO PRODUTO

```text
K14
{
  "format": "IMPORTANT: THIS IS IPHONE FOOTAGE. Vertical 9:16.",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "reference_use": "Use the first attached image only for Brandon's exact identity, wardrobe and own garage gym with the black table. Use the second attached image only as a composition reference for the camera position, framing and the action; do not copy its man, his suspenders, bare chest, log cabin, wooden counter or the caption text. Use the third attached image only for the Natural Rems Sea Moss jar: copy ONLY the front jar, without the MADE IN USA banner at the top, without the second jar behind it and without the loose gummies.",
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
  "negative": "no captions, no subtitles, no words overlaid on the image, no plastic-looking skin, no extra fingers, no third hand, no blur, no bokeh, no warm orange color cast, no yellow tint, no golden glow, no golden hour light, no sunset, no HDR, no cinematic lighting, no beauty smoothing, no visible phone, no studio, no second person, no eyeglasses, no grey t-shirt, no white kitchen cabinets, no marble countertop, no silver cross, no log cabin, no suspenders, no shirtless man, no second jar, no other bottles, no loose gummies, no banner above the jar, no hand covering the label, no lemons or ginger on the table"
}
```

### K15 · T15, comment yes + follow · anexar ÂNCORA HOLISTIC BRANDON + FRAME DO MODELO + FOTO DO PRODUTO

```text
K15
{
  "format": "IMPORTANT: THIS IS IPHONE FOOTAGE. Vertical 9:16.",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "reference_use": "Use the first attached image only for Brandon's exact identity, wardrobe and own garage gym with the black table. Use the second attached image only as a composition reference for the camera position, framing and the action; do not copy its man, his suspenders, bare chest, log cabin, wooden counter or the caption text. Use the third attached image only for the Natural Rems Sea Moss jar: copy ONLY the front jar, without the MADE IN USA banner at the top, without the second jar behind it and without the loose gummies.",
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
  "negative": "no captions, no subtitles, no words overlaid on the image, no plastic-looking skin, no extra fingers, no third hand, no blur, no bokeh, no warm orange color cast, no yellow tint, no golden glow, no golden hour light, no sunset, no HDR, no cinematic lighting, no beauty smoothing, no visible phone, no studio, no second person, no eyeglasses, no grey t-shirt, no white kitchen cabinets, no marble countertop, no silver cross, no log cabin, no suspenders, no shirtless man, no second jar, no other bottles, no loose gummies, no banner above the jar, no hand covering the label, no lemons or ginger on the table"
}
```

### K16 · T16, CTA da marca · anexar ÂNCORA HOLISTIC BRANDON + FRAME DO MODELO + FOTO DO PRODUTO

```text
K16
{
  "format": "IMPORTANT: THIS IS IPHONE FOOTAGE. Vertical 9:16.",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "reference_use": "Use the first attached image only for Brandon's exact identity, wardrobe and own garage gym with the black table. Use the second attached image only as a composition reference for the camera position, framing and the action; do not copy its man, his suspenders, bare chest, log cabin, wooden counter or the caption text. Use the third attached image only for the Natural Rems Sea Moss jar: copy ONLY the front jar, without the MADE IN USA banner at the top, without the second jar behind it and without the loose gummies.",
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
  "negative": "no captions, no subtitles, no words overlaid on the image, no plastic-looking skin, no extra fingers, no third hand, no blur, no bokeh, no warm orange color cast, no yellow tint, no golden glow, no golden hour light, no sunset, no HDR, no cinematic lighting, no beauty smoothing, no visible phone, no studio, no second person, no eyeglasses, no grey t-shirt, no white kitchen cabinets, no marble countertop, no silver cross, no log cabin, no suspenders, no shirtless man, no second jar, no other bottles, no loose gummies, no banner above the jar, no hand covering the label, no lemons or ginger on the table"
}
```

## 3. PROMPTS DE VÍDEO (um bloco por V)

### V01 · T1 · frame inicial = a imagem que você deixou no K01

```text
V01
a avatar Brandon, mulher, fala em inglês com sotaque americano de uma mulher negra americana, voz feminina clara e firme de uma mulher de uns trinta anos, entonação animada e intrigante, como quem conta um truque de cozinha, voz autêntica, como se exigisse ser ouvida, a seguinte frase: "This is my trick for feeling my best all winter and summer."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Brandon rala a casca do limão com o zester, uma tira fina de casca amarela pendurada, e olha para a câmera enquanto fala. Ela diz a frase em ritmo natural logo no começo e a ação continua até o fim.

câmera: leve handheld natural

som ambiente: box de treino em casa, tranquilo, zester raspando a casca, sem música
```

### V02 · T2 · frame inicial = a imagem que você deixou no K02

```text
V02
(sem fala no take: a fala 2 entra como voz-over na edição)

o que acontece no vídeo: A faca corta o limão ao meio na tábua; só as mãos e o antebraço com a tatuagem aparecem.

câmera: leve handheld natural

som ambiente: box de treino em casa, tranquilo, faca cortando o limão na tábua, sem música
```

### V03 · T3 · frame inicial = a imagem que você deixou no K03

```text
V03
(sem fala no take: insert mudo, a voz da fala 2 e da fala 4 segue por cima na edição)

o que acontece no vídeo: Os gomos de limão cortados brilham em macro; uma ponta de dedo ajeita um gomo na pilha.

câmera: leve handheld natural

som ambiente: box de treino em casa, tranquilo, gomos de limão suculentos, sem música
```

### V04 · T4 · frame inicial = a imagem que você deixou no K04

```text
V04
(sem fala no take: a fala 4 entra como voz-over na edição)

o que acontece no vídeo: As mãos descascam a raiz de gengibre com a faquinha, casquinhas finas caindo na tábua.

câmera: leve handheld natural

som ambiente: box de treino em casa, tranquilo, faquinha descascando o gengibre, sem música
```

### V05 · T5 · frame inicial = a imagem que você deixou no K05

```text
V05
(sem fala no take: insert mudo, a voz da fala 4 segue por cima na edição)

o que acontece no vídeo: O copo do liquidificador cheio de limão picado e gengibre; a mão se afasta da borda.

câmera: leve handheld natural

som ambiente: box de treino em casa, tranquilo, pedaços caindo no copo, sem música
```

### V06 · T6 · frame inicial = a imagem que você deixou no K06

```text
V06
(sem fala no take: insert mudo, a voz da fala 4 segue por cima na edição)

o que acontece no vídeo: A medida de metal despeja um fio de água dentro do copo cheio de limão e gengibre.

câmera: leve handheld natural

som ambiente: box de treino em casa, tranquilo, água entrando no copo, sem música
```

### V07 · T7 · frame inicial = a imagem que você deixou no K07

```text
V07
(sem fala no take: a fala 7 entra como voz-over na edição)

o que acontece no vídeo: A palma da mão por cima do copo travado na base; o limão e o gengibre giram e batem dentro do copo.

câmera: leve handheld natural

som ambiente: box de treino em casa, tranquilo, liquidificador batendo, sem música
```

### V08 · T8 · frame inicial = a imagem que você deixou no K08

```text
V08
a avatar Brandon, mulher, fala em inglês com sotaque americano de uma mulher negra americana, voz feminina clara e firme de uma mulher de uns trinta anos, entonação relaxada e satisfeita, voz autêntica, como se exigisse ser ouvida, a seguinte frase: "Nice and smooth. If you want it super smooth, you can strain it, but I don't mind the fiber."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Brandon inclina o copinho com a mistura lisa na direção da câmera e abre a outra mão enquanto fala.

câmera: leve handheld natural

som ambiente: box de treino em casa, tranquilo, sem música
```

### V09 · T9 · frame inicial = a imagem que você deixou no K09

```text
V09
(sem fala no take: insert mudo, a voz da fala 8 termina por cima na edição)

o que acontece no vídeo: A mão inclina o copinho e a última mistura escorre para dentro das duas forminhas de gelo.

câmera: leve handheld natural

som ambiente: box de treino em casa, tranquilo, mistura escorrendo nas forminhas, sem música
```

### V10 · T10 · frame inicial = a imagem que você deixou no K10

```text
V10
a avatar Brandon, mulher, fala em inglês com sotaque americano de uma mulher negra americana, voz feminina clara e firme de uma mulher de uns trinta anos, entonação curta e sorridente, voz autêntica, como se exigisse ser ouvida, a seguinte frase: "And that's it."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Brandon sorri para a câmera atrás das forminhas cheias, com as mãos na borda da mesa. Ela diz a frase em ritmo natural logo no começo e a ação continua até o fim.

câmera: leve handheld natural

som ambiente: box de treino em casa, tranquilo, sem música
```

### V11 · T11 · frame inicial = a imagem que você deixou no K11

```text
V11
(sem fala no take: a fala 11 entra como voz-over na edição)

o que acontece no vídeo: Os dedos soltam um cubo de gelo creme que cai dentro da caneca de vidro vazia, o limão ao lado.

câmera: leve handheld natural

som ambiente: box de treino em casa, tranquilo, cubo batendo no vidro, sem música
```

### V12 · T12 · frame inicial = a imagem que você deixou no K12

```text
V12
a avatar Brandon, mulher, fala em inglês com sotaque americano de uma mulher negra americana, voz feminina clara e firme de uma mulher de uns trinta anos, entonação sincera e desafiadora, com as sobrancelhas levantadas, voz autêntica, como se exigisse ser ouvida, a seguinte frase: "But be honest with me. Will you still be peeling ginger and cutting lemons on a busy Thursday night? That is the night my clients' routines usually die."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Brandon fala para a câmera segurando a caneca com a mão direita, a mão esquerda aberta, as forminhas cheias na mesa.

câmera: leve handheld natural

som ambiente: box de treino em casa, tranquilo, sem música
```

### V13 · T13 · frame inicial = a imagem que você deixou no K13

```text
V13
a avatar Brandon, mulher, fala em inglês com sotaque americano de uma mulher negra americana, voz feminina clara e firme de uma mulher de uns trinta anos, entonação orgulhosa, dizendo Natural Rems Sea Moss devagar e por inteiro, voz autêntica, como se exigisse ser ouvida, a seguinte frase: "That is why my clients keep one simple thing instead: Natural Rems Sea Moss. Ginger is in there, plus fifteen other things, in one green apple gummy."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Brandon ergue o frasco devagar da altura da cintura até o lado do rosto no nome do produto e o deixa parado, rótulo de frente.

câmera: fixa

som ambiente: box de treino em casa, tranquilo, sem música
```

### V14 · T14 · frame inicial = a imagem que você deixou no K14

```text
V14
a avatar Brandon, mulher, fala em inglês com sotaque americano de uma mulher negra americana, voz feminina clara e firme de uma mulher de uns trinta anos, entonação calorosa e segura, voz autêntica, como se exigisse ser ouvida, a seguinte frase: "Most of them tell me this is the one habit that finally stuck, because it takes ten seconds."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Brandon fala para a câmera com o frasco parado ao lado do rosto, rótulo de frente.

câmera: fixa

som ambiente: box de treino em casa, tranquilo, sem música
```

### V15 · T15 · frame inicial = a imagem que você deixou no K15

```text
V15
a avatar Brandon, mulher, fala em inglês com sotaque americano de uma mulher negra americana, voz feminina clara e firme de uma mulher de uns trinta anos, entonação convidativa, sorrindo no yes, voz autêntica, como se exigisse ser ouvida, a seguinte frase: "Comment yes if you like simple routines like this, and follow me so the next one reaches you."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Brandon fala para a câmera com o frasco parado ao lado do rosto, sorrindo no yes.

câmera: fixa

som ambiente: box de treino em casa, tranquilo, sem música
```

### V16 · T16 · frame inicial = a imagem que você deixou no K16

```text
V16
a avatar Brandon, mulher, fala em inglês com sotaque americano de uma mulher negra americana, voz feminina clara e firme de uma mulher de uns trinta anos, entonação clara, dizendo Natural Rems Sea Moss devagar e por inteiro, voz autêntica, como se exigisse ser ouvida, a seguinte frase: "Search Natural Rems Sea Moss on Amazon. Or you can just tap the link I left right down below, in the caption of this video."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Brandon fala para a câmera com o frasco parado ao lado do rosto, rótulo de frente, do começo ao fim, sem baixar o frasco.

câmera: fixa

som ambiente: box de treino em casa, tranquilo, sem música
```

## 4. Montagem no CapCut

1. Clipes numerados na ordem: V01 a V16.
2. Do V01 ao V11, cortar no tempo da cena do modelo: V01 0,0 a 3,8 s; V02 3,8 a 5,6 s; V03 5,6 a 6,7 s; V04 6,7 a 7,8 s; V05 7,8 a 8,7 s; V06 8,7 a 9,9 s; V07 9,9 a 14,0 s; V08 14,0 a 16,5 s; V09 16,5 a 18,0 s; V10 18,0 a 19,4 s; V11 19,4 a 22,9 s. Do V12 ao V16, cortar logo depois da última palavra.
3. Voz: V01, V08, V10 e V12 a V16 têm fala e lip sync. V02, V04, V07 e V11 são B-roll com a fala de mesmo número como voz-over (usar o áudio do V que tem a fala escrita no roteiro, ou gravar a voz na edição). V03, V05, V06 e V09 são inserts mudos. Isolate Voice / Keep Vocal no áudio.
4. A voz dos takes B-roll segue a fala do roteiro, na ordem: 1, 2, 4, 7, 8, 10, 11, sobre as imagens do modelo.
5. Legenda branca serifada, duas a três palavras por vez, com a palavra de peso maior, no meio do quadro, igual ao modelo. Texto fixo no topo do V01: "My trick for feeling my best". No V15, `yes` grande e isolado na tela. No V16, setas apontando para a legenda do post.
6. Sem Voice Changer: a voz vem do prompt de cada V.
7. Música só depois do gancho (a partir do V02), entre -19 e -20 dB, fora da biblioteca do TikTok.
8. Rótulo pequeno `Synthetic performer` num canto do vídeo.
9. Do V13 ao V16 o frasco não pode ser cortado nem coberto: nenhum B-roll por cima (regra da marca).

## 5. Legenda do post

- Primeira linha, sempre: `#ad #syntheticperformer #naturalrems`
- Logo abaixo: o link da Amazon do Natural Rems Sea Moss (o V16 manda tocar no link da legenda).
- Chave de conteúdo de IA da plataforma LIGADA.

## 6. Transcrição final por take

| Take | English | Português |
|---|---|---|
| T1 | This is my trick for feeling my best all winter and summer. | Esse é o meu truque para me sentir no meu melhor o inverno e o verão inteiros. |
| T2 | All you need is two ingredients. | Você só precisa de dois ingredientes. |
| T3 | (sem fala) | (sem fala) |
| T4 | Lemon, ginger, and a splash of water to loosen it up. | Limão, gengibre e um pouquinho de água para soltar. |
| T5 | (sem fala) | (sem fala) |
| T6 | (sem fala) | (sem fala) |
| T7 | And there we have it. | E está pronto. |
| T8 | Nice and smooth. If you want it super smooth, you can strain it, but I don't mind the fiber. | Bem lisinho. Se você quiser bem liso, pode coar, mas eu não me importo com a fibra. |
| T9 | (sem fala) | (sem fala) |
| T10 | And that's it. | E é só isso. |
| T11 | We pop it in the freezer and you can enjoy hot or cold. | A gente põe no freezer e você pode tomar quente ou gelado. |
| T12 | But be honest with me. Will you still be peeling ginger and cutting lemons on a busy Thursday night? That is the night my clients' routines usually die. | Mas seja sincera comigo. Você ainda vai estar descascando gengibre e cortando limão numa quinta à noite corrida? É a noite em que a rotina das minhas clientes costuma morrer. |
| T13 | That is why my clients keep one simple thing instead: Natural Rems Sea Moss. Ginger is in there, plus fifteen other things, in one green apple gummy. | Por isso as minhas clientes ficam com uma coisa simples no lugar: Natural Rems Sea Moss. O gengibre está lá, mais quinze outras coisas, numa goma de maçã verde. |
| T14 | Most of them tell me this is the one habit that finally stuck, because it takes ten seconds. | A maioria me diz que esse é o único hábito que finalmente pegou, porque leva dez segundos. |
| T15 | Comment yes if you like simple routines like this, and follow me so the next one reaches you. | Comente yes se você gosta de rotinas simples como essa, e me siga para a próxima chegar até você. |
| T16 | Search Natural Rems Sea Moss on Amazon. Or you can just tap the link I left right down below, in the caption of this video. | Procure Natural Rems Sea Moss na Amazon. Ou é só tocar no link que eu deixei aqui embaixo, na legenda deste vídeo. |

## 7. Roteiro final em inglês

1. This is my trick for feeling my best all winter and summer.
2. All you need is two ingredients.
3. (insert mudo, sem fala)
4. Lemon, ginger, and a splash of water to loosen it up.
5. (insert mudo, sem fala)
6. (insert mudo, sem fala)
7. And there we have it.
8. Nice and smooth. If you want it super smooth, you can strain it, but I don't mind the fiber.
9. (insert mudo, sem fala)
10. And that's it.
11. We pop it in the freezer and you can enjoy hot or cold.
12. But be honest with me. Will you still be peeling ginger and cutting lemons on a busy Thursday night? That is the night my clients' routines usually die.
13. That is why my clients keep one simple thing instead: Natural Rems Sea Moss. Ginger is in there, plus fifteen other things, in one green apple gummy.
14. Most of them tell me this is the one habit that finally stuck, because it takes ten seconds.
15. Comment yes if you like simple routines like this, and follow me so the next one reaches you.
16. Search Natural Rems Sea Moss on Amazon. Or you can just tap the link I left right down below, in the caption of this video.

This is my trick for feeling my best all winter and summer. All you need is two ingredients. Lemon, ginger, and a splash of water to loosen it up. And there we have it. Nice and smooth. If you want it super smooth, you can strain it, but I don't mind the fiber. And that's it. We pop it in the freezer and you can enjoy hot or cold. But be honest with me. Will you still be peeling ginger and cutting lemons on a busy Thursday night? That is the night my clients' routines usually die. That is why my clients keep one simple thing instead: Natural Rems Sea Moss. Ginger is in there, plus fifteen other things, in one green apple gummy. Most of them tell me this is the one habit that finally stuck, because it takes ten seconds. Comment yes if you like simple routines like this, and follow me so the next one reaches you. Search Natural Rems Sea Moss on Amazon. Or you can just tap the link I left right down below, in the caption of this video.
