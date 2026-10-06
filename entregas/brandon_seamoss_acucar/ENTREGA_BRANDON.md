# ENTREGA | holistic.brandon | Natural Rems Sea Moss Venda, açúcar no sea moss

Produção `brandon_seamoss_acucar` · Ângulo 1 (Natural Rems Sea Moss) · VENDA · vídeo modelo de avatar IA · talking head com demonstração de dose · rodada de VALIDAÇÃO · perfil CLÁSSICO

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

Checklist de envio: 11/11 aprovados (N/A: A1, A10, A12, A13 e A14 fiéis ao modelo na rodada de validação, sem arquivo de ganchos; C4 sem selfie; C7 sem motion control)

Ficha: 11/11 K conferidos contra o frame do modelo, placar F1 a F6 + G1 a G8 completo em cada um, com evidência literal (N/A só em G2 no box, sem céu nem janela em quadro, e G8 nos takes sem fala) (`FICHA_FRAMES.md`, GATE_VISUAL Parte 6)

## Mapa de anexos

- **K01 a K11 (Brandon):** âncora `producao/_ancoras/holistic_brandon_ancora.jpg` + frame do modelo (só composição); do K09 ao K11 também a foto do produto `producao/_ancoras/natural_rems_seamoss_produto.jpg`.
- K01 a K11 casam com V01 a V11 pelo número.

| Código | Take | Anexar, nesta ordem |
|---|---|---|
| K01 / V01 | T1, gancho 1, a dose da goma na colher | ÂNCORA HOLISTIC BRANDON `producao/_ancoras/holistic_brandon_ancora.jpg` + FRAME DO MODELO `input/frames_modelo/K01_modelo.png` (só composição) |
| K02 / V02 | T2, gancho 2, o despejo grande no pote | ÂNCORA HOLISTIC BRANDON `producao/_ancoras/holistic_brandon_ancora.jpg` + FRAME DO MODELO `input/frames_modelo/K02_modelo.png` (só composição) |
| K03 / V03 | T3, gancho 3, o despejo continua e o pote enche | ÂNCORA HOLISTIC BRANDON `producao/_ancoras/holistic_brandon_ancora.jpg` + FRAME DO MODELO `input/frames_modelo/K03_modelo.png` (só composição) |
| K04 / V04 | T4, pontos 1 e 2 | ÂNCORA HOLISTIC BRANDON `producao/_ancoras/holistic_brandon_ancora.jpg` + FRAME DO MODELO `input/frames_modelo/K04_modelo.png` (só composição) |
| K05 / V05 | T5, pontos 3 e 4 | ÂNCORA HOLISTIC BRANDON `producao/_ancoras/holistic_brandon_ancora.jpg` + FRAME DO MODELO `input/frames_modelo/K05_modelo.png` (só composição) |
| K06 / V06 | T6, ponto 5, a virada | ÂNCORA HOLISTIC BRANDON `producao/_ancoras/holistic_brandon_ancora.jpg` + FRAME DO MODELO `input/frames_modelo/K06_modelo.png` (só composição) |
| K07 / V07 | T7, autoridade da coach | ÂNCORA HOLISTIC BRANDON `producao/_ancoras/holistic_brandon_ancora.jpg` + FRAME DO MODELO `input/frames_modelo/K07_modelo.png` (só composição) |
| K08 / V08 | T8, o princípio | ÂNCORA HOLISTIC BRANDON `producao/_ancoras/holistic_brandon_ancora.jpg` + FRAME DO MODELO `input/frames_modelo/K08_modelo.png` (só composição) |
| K09 / V09 | T9, o produto, o frasco sobe no nome | ÂNCORA HOLISTIC BRANDON `producao/_ancoras/holistic_brandon_ancora.jpg` + FRAME DO MODELO `input/frames_modelo/K09_modelo.png` (só composição) + FOTO DO PRODUTO `producao/_ancoras/natural_rems_seamoss_produto.jpg` (só o pote da frente) |
| K10 / V10 | T10, comment yes + follow | ÂNCORA HOLISTIC BRANDON `producao/_ancoras/holistic_brandon_ancora.jpg` + FRAME DO MODELO `input/frames_modelo/K10_modelo.png` (só composição) + FOTO DO PRODUTO `producao/_ancoras/natural_rems_seamoss_produto.jpg` (só o pote da frente) |
| K11 / V11 | T11, CTA da marca, Amazon e legenda | ÂNCORA HOLISTIC BRANDON `producao/_ancoras/holistic_brandon_ancora.jpg` + FRAME DO MODELO `input/frames_modelo/K11_modelo.png` (só composição) + FOTO DO PRODUTO `producao/_ancoras/natural_rems_seamoss_produto.jpg` (só o pote da frente) |

## 2. PROMPTS DE IMAGEM

### Keyframes (um bloco por K)

### K01 · T1, gancho 1, a dose da goma na colher · anexar ÂNCORA HOLISTIC BRANDON + FRAME DO MODELO

```text
K01
{
  "format": "IMPORTANT: THIS IS IPHONE FOOTAGE. Vertical 9:16.",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "reference_use": "Use the first attached image only for Brandon's exact identity, wardrobe and own garage gym with the black table. Use the second attached image only as a composition reference for the camera position, framing and how the objects are held and poured; do not copy its person, wooden courtyard, red robe, bottle brand, table or the caption text.",
  "identity_main": "The exact fictional AI character holistic.brandon: Black mixed-race American woman around thirty, athletic and toned, medium light-brown skin with light freckles across the nose and cheeks, dark brown eyes, defined eyebrows, full lips, hair in tight cornrows that turn into long loose braids falling over both shoulders, finished with small wooden and gold beads, a black floral blackwork tattoo sleeve on her right arm, a fine line tattoo on her left inner arm and a small fine-line floral tattoo below her left collarbone.",
  "wardrobe": "Plain white ribbed tank top with nothing printed on it, loose black training shorts, a thin gold chain with a small gold cross pendant and small stud earrings.",
  "scene": "Her own garage gym: a white-painted concrete block wall behind her, a red neon sign reading TRAIN PRAY REPEAT on the wall at the left, a whiteboard with handwritten black marker reading STAY READY. STAY DISCIPLINED. on the right, and a small American flag pinned above the whiteboard, discreet but clearly visible and in focus. In front of her stands a plain matte black table.",
  "prop": "A tall clear glass bottle with a narrow neck filled with white granulated sugar, with a plain blank kraft-paper label that has no text on it, tilted in her right hand with a thin stream of sugar falling onto a metal spoon held below the neck in her left hand; a small clear shot glass stands on the black table and the edge of a large clear glass jar with a wide mouth, no lid, no label is cut by the lower left corner of the frame.",
  "posture": "Brandon stands behind the black table, tilting the bottle toward the lens with her right hand and holding the spoon under the neck with her left.",
  "composition": "Straight-on medium shot: the phone lens is about 40 centimeters from the bottle, which she tilts toward the lens in her right hand and which fills the right 35 percent of the frame, closer to the camera than her face; her face and shoulders fill the upper half of the frame, the black table edge is at the bottom. The background is reduced by framing, never by blur.",
  "camera": "phone at her chest height, straight-on, standard 1x lens, light handheld",
  "lighting": "Neutral overcast daylight from a large window out of frame, soft even light on her face, hands and the table with no harsh shadows. The red neon glows on the wall but does not tint her skin.",
  "state": "Start frame: Brandon is caught mid-sentence, lips naturally parted, animated expression, looking straight into the lens, calm and a little playful, talking while she pours.",
  "realism": "Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday reality, background fully in focus, everything in sharp focus, no AI polish, no beauty smoothing.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no plastic-looking skin, no extra fingers, no third hand, no blur, no bokeh, no warm orange color cast, no yellow tint, no golden glow, no golden hour light, no sunset, no HDR, no cinematic lighting, no beauty smoothing, no visible phone, no studio, no second person, no eyeglasses, no grey curly hair, no wooden bench, no street, no houses, no silver cross, no printed labels or lettering on the glass, bottle or jars"
}
```

### K02 · T2, gancho 2, o despejo grande no pote · anexar ÂNCORA HOLISTIC BRANDON + FRAME DO MODELO

```text
K02
{
  "format": "IMPORTANT: THIS IS IPHONE FOOTAGE. Vertical 9:16.",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "reference_use": "Use the first attached image only for Brandon's exact identity, wardrobe and own garage gym with the black table. Use the second attached image only as a composition reference for the camera position, framing and how the objects are held and poured; do not copy its person, wooden courtyard, red robe, bottle brand, table or the caption text.",
  "identity_main": "The exact fictional AI character holistic.brandon: Black mixed-race American woman around thirty, athletic and toned, medium light-brown skin with light freckles across the nose and cheeks, dark brown eyes, defined eyebrows, full lips, hair in tight cornrows that turn into long loose braids falling over both shoulders, finished with small wooden and gold beads, a black floral blackwork tattoo sleeve on her right arm, a fine line tattoo on her left inner arm and a small fine-line floral tattoo below her left collarbone.",
  "wardrobe": "Plain white ribbed tank top with nothing printed on it, loose black training shorts, a thin gold chain with a small gold cross pendant and small stud earrings.",
  "scene": "Her own garage gym: a white-painted concrete block wall behind her, a red neon sign reading TRAIN PRAY REPEAT on the wall at the left, a whiteboard with handwritten black marker reading STAY READY. STAY DISCIPLINED. on the right, and a small American flag pinned above the whiteboard, discreet but clearly visible and in focus. In front of her stands a plain matte black table.",
  "prop": "A large clear glass jar with a wide mouth, no lid, no label, gripped by its side in her left hand, already half full of white granulated sugar, with a tall clear glass bottle with a narrow neck filled with white granulated sugar, with a plain blank kraft-paper label that has no text on it tilted in her right hand pouring a thick stream of sugar into it; a small clear shot glass and a metal spoon lie on the black table.",
  "posture": "Brandon leans forward over the black table, gripping the jar with her left hand and pouring the bottle into it with her right.",
  "composition": "Straight-on close medium shot: the phone lens is about 30 centimeters from the large jar, which she grips with her left hand and which fills the lower left 30 percent of the frame, closer to the camera than her face; the bottle pours into it from the upper right; her face and shoulders fill the upper half of the frame. The background is reduced by framing, never by blur.",
  "camera": "phone at her chest height, straight-on, standard 1x lens, light handheld",
  "lighting": "Neutral overcast daylight from a large window out of frame, soft even light on her face, hands and the table with no harsh shadows. The red neon glows on the wall but does not tint her skin.",
  "state": "Start frame: Brandon is caught mid-sentence, lips naturally parted, animated expression, looking straight into the lens, animated, eyebrows raised, talking while she pours.",
  "realism": "Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday reality, background fully in focus, everything in sharp focus, no AI polish, no beauty smoothing.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no plastic-looking skin, no extra fingers, no third hand, no blur, no bokeh, no warm orange color cast, no yellow tint, no golden glow, no golden hour light, no sunset, no HDR, no cinematic lighting, no beauty smoothing, no visible phone, no studio, no second person, no eyeglasses, no grey curly hair, no wooden bench, no street, no houses, no silver cross, no printed labels or lettering on the glass, bottle or jars"
}
```

### K03 · T3, gancho 3, o despejo continua e o pote enche · anexar ÂNCORA HOLISTIC BRANDON + FRAME DO MODELO

```text
K03
{
  "format": "IMPORTANT: THIS IS IPHONE FOOTAGE. Vertical 9:16.",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "reference_use": "Use the first attached image only for Brandon's exact identity, wardrobe and own garage gym with the black table. Use the second attached image only as a composition reference for the camera position, framing and how the objects are held and poured; do not copy its person, wooden courtyard, red robe, bottle brand, table or the caption text.",
  "identity_main": "The exact fictional AI character holistic.brandon: Black mixed-race American woman around thirty, athletic and toned, medium light-brown skin with light freckles across the nose and cheeks, dark brown eyes, defined eyebrows, full lips, hair in tight cornrows that turn into long loose braids falling over both shoulders, finished with small wooden and gold beads, a black floral blackwork tattoo sleeve on her right arm, a fine line tattoo on her left inner arm and a small fine-line floral tattoo below her left collarbone.",
  "wardrobe": "Plain white ribbed tank top with nothing printed on it, loose black training shorts, a thin gold chain with a small gold cross pendant and small stud earrings.",
  "scene": "Her own garage gym: a white-painted concrete block wall behind her, a red neon sign reading TRAIN PRAY REPEAT on the wall at the left, a whiteboard with handwritten black marker reading STAY READY. STAY DISCIPLINED. on the right, and a small American flag pinned above the whiteboard, discreet but clearly visible and in focus. In front of her stands a plain matte black table.",
  "prop": "A large clear glass jar with a wide mouth, no lid, no label, gripped by its side in her left hand, now three quarters full of white granulated sugar, with a tall clear glass bottle with a narrow neck filled with white granulated sugar, with a plain blank kraft-paper label that has no text on it tilted in her right hand still pouring sugar into it; a small clear shot glass and a metal spoon lie on the black table.",
  "posture": "Brandon leans forward over the black table, gripping the jar with her left hand and finishing the pour with her right.",
  "composition": "Straight-on close medium shot: the phone lens is about 30 centimeters from the large jar, which she grips with her left hand and which fills the lower left 35 percent of the frame, closer to the camera than her face; the bottle pours into it from the upper right; her face and shoulders fill the upper half of the frame. The background is reduced by framing, never by blur.",
  "camera": "phone at her chest height, straight-on, standard 1x lens, light handheld",
  "lighting": "Neutral overcast daylight from a large window out of frame, soft even light on her face, hands and the table with no harsh shadows. The red neon glows on the wall but does not tint her skin.",
  "state": "Start frame: Brandon is caught mid-sentence, lips naturally parted, animated expression, looking straight into the lens, knowing and confident, a small smile, talking while she pours.",
  "realism": "Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday reality, background fully in focus, everything in sharp focus, no AI polish, no beauty smoothing.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no plastic-looking skin, no extra fingers, no third hand, no blur, no bokeh, no warm orange color cast, no yellow tint, no golden glow, no golden hour light, no sunset, no HDR, no cinematic lighting, no beauty smoothing, no visible phone, no studio, no second person, no eyeglasses, no grey curly hair, no wooden bench, no street, no houses, no silver cross, no printed labels or lettering on the glass, bottle or jars"
}
```

### K04 · T4, pontos 1 e 2 · anexar ÂNCORA HOLISTIC BRANDON + FRAME DO MODELO

```text
K04
{
  "format": "IMPORTANT: THIS IS IPHONE FOOTAGE. Vertical 9:16.",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "reference_use": "Use the first attached image only for Brandon's exact identity, wardrobe and own garage gym with the black table. Use the second attached image only as a composition reference for the camera position, framing and how the objects are held and poured; do not copy its person, wooden courtyard, red robe, bottle brand, table or the caption text.",
  "identity_main": "The exact fictional AI character holistic.brandon: Black mixed-race American woman around thirty, athletic and toned, medium light-brown skin with light freckles across the nose and cheeks, dark brown eyes, defined eyebrows, full lips, hair in tight cornrows that turn into long loose braids falling over both shoulders, finished with small wooden and gold beads, a black floral blackwork tattoo sleeve on her right arm, a fine line tattoo on her left inner arm and a small fine-line floral tattoo below her left collarbone.",
  "wardrobe": "Plain white ribbed tank top with nothing printed on it, loose black training shorts, a thin gold chain with a small gold cross pendant and small stud earrings.",
  "scene": "Her own garage gym: a white-painted concrete block wall behind her, a red neon sign reading TRAIN PRAY REPEAT on the wall at the left, a whiteboard with handwritten black marker reading STAY READY. STAY DISCIPLINED. on the right, and a small American flag pinned above the whiteboard, discreet but clearly visible and in focus. In front of her stands a plain matte black table.",
  "prop": "On the black table, at the left a large clear glass jar with a wide mouth, no lid, no label, now full of white granulated sugar, at the right a tall clear glass bottle with a narrow neck filled with white granulated sugar, with a plain blank kraft-paper label that has no text on it, between them a small clear shot glass and a metal spoon.",
  "posture": "Brandon sits back from the table and counts on one raised finger with her right hand, left hand open.",
  "composition": "Straight-on medium shot from the chest up: the phone lens is about 45 centimeters from the large sugar jar on the table, which fills the lower left 25 percent of the frame, closer to the camera than her face; the bottle stands at the right edge; her face and shoulders fill the upper 55 percent of the frame. The background is reduced by framing, never by blur.",
  "camera": "phone at her chest height, straight-on, standard 1x lens, light handheld",
  "lighting": "Neutral overcast daylight from a large window out of frame, soft even light on her face, hands and the table with no harsh shadows. The red neon glows on the wall but does not tint her skin.",
  "state": "Start frame: Brandon is caught mid-sentence, lips naturally parted, animated expression, looking straight into the lens, lively, counting on one finger.",
  "realism": "Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday reality, background fully in focus, everything in sharp focus, no AI polish, no beauty smoothing.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no plastic-looking skin, no extra fingers, no third hand, no blur, no bokeh, no warm orange color cast, no yellow tint, no golden glow, no golden hour light, no sunset, no HDR, no cinematic lighting, no beauty smoothing, no visible phone, no studio, no second person, no eyeglasses, no grey curly hair, no wooden bench, no street, no houses, no silver cross, no printed labels or lettering on the glass, bottle or jars"
}
```

### K05 · T5, pontos 3 e 4 · anexar ÂNCORA HOLISTIC BRANDON + FRAME DO MODELO

```text
K05
{
  "format": "IMPORTANT: THIS IS IPHONE FOOTAGE. Vertical 9:16.",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "reference_use": "Use the first attached image only for Brandon's exact identity, wardrobe and own garage gym with the black table. Use the second attached image only as a composition reference for the camera position, framing and how the objects are held and poured; do not copy its person, wooden courtyard, red robe, bottle brand, table or the caption text.",
  "identity_main": "The exact fictional AI character holistic.brandon: Black mixed-race American woman around thirty, athletic and toned, medium light-brown skin with light freckles across the nose and cheeks, dark brown eyes, defined eyebrows, full lips, hair in tight cornrows that turn into long loose braids falling over both shoulders, finished with small wooden and gold beads, a black floral blackwork tattoo sleeve on her right arm, a fine line tattoo on her left inner arm and a small fine-line floral tattoo below her left collarbone.",
  "wardrobe": "Plain white ribbed tank top with nothing printed on it, loose black training shorts, a thin gold chain with a small gold cross pendant and small stud earrings.",
  "scene": "Her own garage gym: a white-painted concrete block wall behind her, a red neon sign reading TRAIN PRAY REPEAT on the wall at the left, a whiteboard with handwritten black marker reading STAY READY. STAY DISCIPLINED. on the right, and a small American flag pinned above the whiteboard, discreet but clearly visible and in focus. In front of her stands a plain matte black table.",
  "prop": "On the black table, at the left a large clear glass jar with a wide mouth, no lid, no label, now full of white granulated sugar, at the right a tall clear glass bottle with a narrow neck filled with white granulated sugar, with a plain blank kraft-paper label that has no text on it, between them a small clear shot glass and a metal spoon.",
  "posture": "Brandon gestures with both open hands, then counts on two fingers.",
  "composition": "Straight-on medium shot from the chest up: the phone lens is about 45 centimeters from the large sugar jar on the table, which fills the lower left 25 percent of the frame, closer to the camera than her face; the bottle stands at the right edge; her face and shoulders fill the upper 55 percent of the frame. The background is reduced by framing, never by blur.",
  "camera": "phone at her chest height, straight-on, standard 1x lens, light handheld",
  "lighting": "Neutral overcast daylight from a large window out of frame, soft even light on her face, hands and the table with no harsh shadows. The red neon glows on the wall but does not tint her skin.",
  "state": "Start frame: Brandon is caught mid-sentence, lips naturally parted, animated expression, looking straight into the lens, lively and a little teasing.",
  "realism": "Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday reality, background fully in focus, everything in sharp focus, no AI polish, no beauty smoothing.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no plastic-looking skin, no extra fingers, no third hand, no blur, no bokeh, no warm orange color cast, no yellow tint, no golden glow, no golden hour light, no sunset, no HDR, no cinematic lighting, no beauty smoothing, no visible phone, no studio, no second person, no eyeglasses, no grey curly hair, no wooden bench, no street, no houses, no silver cross, no printed labels or lettering on the glass, bottle or jars"
}
```

### K06 · T6, ponto 5, a virada · anexar ÂNCORA HOLISTIC BRANDON + FRAME DO MODELO

```text
K06
{
  "format": "IMPORTANT: THIS IS IPHONE FOOTAGE. Vertical 9:16.",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "reference_use": "Use the first attached image only for Brandon's exact identity, wardrobe and own garage gym with the black table. Use the second attached image only as a composition reference for the camera position, framing and how the objects are held and poured; do not copy its person, wooden courtyard, red robe, bottle brand, table or the caption text.",
  "identity_main": "The exact fictional AI character holistic.brandon: Black mixed-race American woman around thirty, athletic and toned, medium light-brown skin with light freckles across the nose and cheeks, dark brown eyes, defined eyebrows, full lips, hair in tight cornrows that turn into long loose braids falling over both shoulders, finished with small wooden and gold beads, a black floral blackwork tattoo sleeve on her right arm, a fine line tattoo on her left inner arm and a small fine-line floral tattoo below her left collarbone.",
  "wardrobe": "Plain white ribbed tank top with nothing printed on it, loose black training shorts, a thin gold chain with a small gold cross pendant and small stud earrings.",
  "scene": "Her own garage gym: a white-painted concrete block wall behind her, a red neon sign reading TRAIN PRAY REPEAT on the wall at the left, a whiteboard with handwritten black marker reading STAY READY. STAY DISCIPLINED. on the right, and a small American flag pinned above the whiteboard, discreet but clearly visible and in focus. In front of her stands a plain matte black table.",
  "prop": "On the black table, at the left a large clear glass jar with a wide mouth, no lid, no label, now full of white granulated sugar, at the right a tall clear glass bottle with a narrow neck filled with white granulated sugar, with a plain blank kraft-paper label that has no text on it, between them a small clear shot glass and a metal spoon.",
  "posture": "Brandon leans a little toward the lens with both hands open above the table.",
  "composition": "Straight-on medium shot from the chest up: the phone lens is about 45 centimeters from the large sugar jar on the table, which fills the lower left 25 percent of the frame, closer to the camera than her face; the bottle stands at the right edge; her face and shoulders fill the upper 55 percent of the frame. The background is reduced by framing, never by blur.",
  "camera": "phone at her chest height, straight-on, standard 1x lens, light handheld",
  "lighting": "Neutral overcast daylight from a large window out of frame, soft even light on her face, hands and the table with no harsh shadows. The red neon glows on the wall but does not tint her skin.",
  "state": "Start frame: Brandon is caught mid-sentence, lips naturally parted, animated expression, looking straight into the lens, serious and warm, lowering her voice.",
  "realism": "Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday reality, background fully in focus, everything in sharp focus, no AI polish, no beauty smoothing.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no plastic-looking skin, no extra fingers, no third hand, no blur, no bokeh, no warm orange color cast, no yellow tint, no golden glow, no golden hour light, no sunset, no HDR, no cinematic lighting, no beauty smoothing, no visible phone, no studio, no second person, no eyeglasses, no grey curly hair, no wooden bench, no street, no houses, no silver cross, no printed labels or lettering on the glass, bottle or jars"
}
```

### K07 · T7, autoridade da coach · anexar ÂNCORA HOLISTIC BRANDON + FRAME DO MODELO

```text
K07
{
  "format": "IMPORTANT: THIS IS IPHONE FOOTAGE. Vertical 9:16.",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "reference_use": "Use the first attached image only for Brandon's exact identity, wardrobe and own garage gym with the black table. Use the second attached image only as a composition reference for the camera position, framing and how the objects are held and poured; do not copy its person, wooden courtyard, red robe, bottle brand, table or the caption text.",
  "identity_main": "The exact fictional AI character holistic.brandon: Black mixed-race American woman around thirty, athletic and toned, medium light-brown skin with light freckles across the nose and cheeks, dark brown eyes, defined eyebrows, full lips, hair in tight cornrows that turn into long loose braids falling over both shoulders, finished with small wooden and gold beads, a black floral blackwork tattoo sleeve on her right arm, a fine line tattoo on her left inner arm and a small fine-line floral tattoo below her left collarbone.",
  "wardrobe": "Plain white ribbed tank top with nothing printed on it, loose black training shorts, a thin gold chain with a small gold cross pendant and small stud earrings.",
  "scene": "Her own garage gym: a white-painted concrete block wall behind her, a red neon sign reading TRAIN PRAY REPEAT on the wall at the left, a whiteboard with handwritten black marker reading STAY READY. STAY DISCIPLINED. on the right, and a small American flag pinned above the whiteboard, discreet but clearly visible and in focus. In front of her stands a plain matte black table.",
  "prop": "On the black table, at the left a large clear glass jar with a wide mouth, no lid, no label, now full of white granulated sugar, at the right a tall clear glass bottle with a narrow neck filled with white granulated sugar, with a plain blank kraft-paper label that has no text on it, between them a small clear shot glass and a metal spoon.",
  "posture": "Brandon rests both forearms on the black table edge and speaks straight to the lens.",
  "composition": "Straight-on medium shot from the chest up: the phone lens is about 45 centimeters from the large sugar jar on the table, which fills the lower left 25 percent of the frame, closer to the camera than her face; the bottle stands at the right edge; her face and shoulders fill the upper 55 percent of the frame. The background is reduced by framing, never by blur.",
  "camera": "phone at her chest height, straight-on, standard 1x lens, light handheld",
  "lighting": "Neutral overcast daylight from a large window out of frame, soft even light on her face, hands and the table with no harsh shadows. The red neon glows on the wall but does not tint her skin.",
  "state": "Start frame: Brandon is caught mid-sentence, lips naturally parted, animated expression, looking straight into the lens, calm and sure.",
  "realism": "Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday reality, background fully in focus, everything in sharp focus, no AI polish, no beauty smoothing.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no plastic-looking skin, no extra fingers, no third hand, no blur, no bokeh, no warm orange color cast, no yellow tint, no golden glow, no golden hour light, no sunset, no HDR, no cinematic lighting, no beauty smoothing, no visible phone, no studio, no second person, no eyeglasses, no grey curly hair, no wooden bench, no street, no houses, no silver cross, no printed labels or lettering on the glass, bottle or jars"
}
```

### K08 · T8, o princípio · anexar ÂNCORA HOLISTIC BRANDON + FRAME DO MODELO

```text
K08
{
  "format": "IMPORTANT: THIS IS IPHONE FOOTAGE. Vertical 9:16.",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "reference_use": "Use the first attached image only for Brandon's exact identity, wardrobe and own garage gym with the black table. Use the second attached image only as a composition reference for the camera position, framing and how the objects are held and poured; do not copy its person, wooden courtyard, red robe, bottle brand, table or the caption text.",
  "identity_main": "The exact fictional AI character holistic.brandon: Black mixed-race American woman around thirty, athletic and toned, medium light-brown skin with light freckles across the nose and cheeks, dark brown eyes, defined eyebrows, full lips, hair in tight cornrows that turn into long loose braids falling over both shoulders, finished with small wooden and gold beads, a black floral blackwork tattoo sleeve on her right arm, a fine line tattoo on her left inner arm and a small fine-line floral tattoo below her left collarbone.",
  "wardrobe": "Plain white ribbed tank top with nothing printed on it, loose black training shorts, a thin gold chain with a small gold cross pendant and small stud earrings.",
  "scene": "Her own garage gym: a white-painted concrete block wall behind her, a red neon sign reading TRAIN PRAY REPEAT on the wall at the left, a whiteboard with handwritten black marker reading STAY READY. STAY DISCIPLINED. on the right, and a small American flag pinned above the whiteboard, discreet but clearly visible and in focus. In front of her stands a plain matte black table.",
  "prop": "On the black table, at the left a large clear glass jar with a wide mouth, no lid, no label, now full of white granulated sugar, at the right a tall clear glass bottle with a narrow neck filled with white granulated sugar, with a plain blank kraft-paper label that has no text on it, between them a small clear shot glass and a metal spoon.",
  "posture": "Brandon opens both hands slowly in front of her as if offering something.",
  "composition": "Straight-on medium shot from the chest up: the phone lens is about 45 centimeters from the large sugar jar on the table, which fills the lower left 25 percent of the frame, closer to the camera than her face; the bottle stands at the right edge; her face and shoulders fill the upper 55 percent of the frame. The background is reduced by framing, never by blur.",
  "camera": "phone at her chest height, straight-on, standard 1x lens, light handheld",
  "lighting": "Neutral overcast daylight from a large window out of frame, soft even light on her face, hands and the table with no harsh shadows. The red neon glows on the wall but does not tint her skin.",
  "state": "Start frame: Brandon is caught mid-sentence, lips naturally parted, animated expression, looking straight into the lens, warm and certain.",
  "realism": "Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday reality, background fully in focus, everything in sharp focus, no AI polish, no beauty smoothing.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no plastic-looking skin, no extra fingers, no third hand, no blur, no bokeh, no warm orange color cast, no yellow tint, no golden glow, no golden hour light, no sunset, no HDR, no cinematic lighting, no beauty smoothing, no visible phone, no studio, no second person, no eyeglasses, no grey curly hair, no wooden bench, no street, no houses, no silver cross, no printed labels or lettering on the glass, bottle or jars"
}
```

### K09 · T9, o produto, o frasco sobe no nome · anexar ÂNCORA HOLISTIC BRANDON + FRAME DO MODELO + FOTO DO PRODUTO

```text
K09
{
  "format": "IMPORTANT: THIS IS IPHONE FOOTAGE. Vertical 9:16.",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "reference_use": "Use the first attached image only for Brandon's exact identity, wardrobe and own garage gym with the black table. Use the second attached image only as a composition reference for the camera position, framing and how the objects are held and poured; do not copy its person, wooden courtyard, red robe, bottle brand, table or the caption text. Use the third attached image only for the Natural Rems Sea Moss jar: copy ONLY the front jar, without the MADE IN USA banner at the top, without the second jar behind it and without the loose gummies.",
  "identity_main": "The exact fictional AI character holistic.brandon: Black mixed-race American woman around thirty, athletic and toned, medium light-brown skin with light freckles across the nose and cheeks, dark brown eyes, defined eyebrows, full lips, hair in tight cornrows that turn into long loose braids falling over both shoulders, finished with small wooden and gold beads, a black floral blackwork tattoo sleeve on her right arm, a fine line tattoo on her left inner arm and a small fine-line floral tattoo below her left collarbone.",
  "wardrobe": "Plain white ribbed tank top with nothing printed on it, loose black training shorts, a thin gold chain with a small gold cross pendant and small stud earrings.",
  "scene": "Her own garage gym: a white-painted concrete block wall behind her, a red neon sign reading TRAIN PRAY REPEAT on the wall at the left, a whiteboard with handwritten black marker reading STAY READY. STAY DISCIPLINED. on the right, and a small American flag pinned above the whiteboard, discreet but clearly visible and in focus. In front of her stands a plain matte black table.",
  "prop": "In her right hand, held low just above the black table, the Natural Rems Sea Moss jar: a short wide jar of dark amber plastic with a black screw cap, a pale cream-green label with dark green text, the Natural Rems logo with three leaves, the big title Sea Moss Gummies, a 6000 MG | 16-IN-1 badge, the words GREEN APPLE FLAVOR, a list of ingredients in dark green pill shapes and green seaweed illustrations on both sides, label facing the camera, fully readable. Nothing else on the table.",
  "posture": "Brandon holds the jar low in her right hand, about to raise it beside her face.",
  "composition": "Straight-on medium shot: the phone lens is about 35 centimeters from the jar, which she holds low in her right hand just above the black table and fills the lower right 20 percent of the frame, closer to the camera than her face; her face and shoulders fill the upper half of the frame. The black table is empty. The background is reduced by framing, never by blur.",
  "camera": "phone at her chest height, straight-on, standard 1x lens, light handheld",
  "lighting": "Neutral overcast daylight from a large window out of frame, soft even light on her face, hands and the table with no harsh shadows. The red neon glows on the wall but does not tint her skin.",
  "state": "Start frame: Brandon is caught mid-sentence, lips naturally parted, animated expression, looking straight into the lens, proud, about to show it.",
  "realism": "Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday reality, background fully in focus, everything in sharp focus, no AI polish, no beauty smoothing.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no plastic-looking skin, no extra fingers, no third hand, no blur, no bokeh, no warm orange color cast, no yellow tint, no golden glow, no golden hour light, no sunset, no HDR, no cinematic lighting, no beauty smoothing, no visible phone, no studio, no second person, no eyeglasses, no grey curly hair, no wooden bench, no street, no houses, no silver cross, no second jar, no other bottles, no loose gummies, no banner above the jar, no hand covering the label"
}
```

### K10 · T10, comment yes + follow · anexar ÂNCORA HOLISTIC BRANDON + FRAME DO MODELO + FOTO DO PRODUTO

```text
K10
{
  "format": "IMPORTANT: THIS IS IPHONE FOOTAGE. Vertical 9:16.",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "reference_use": "Use the first attached image only for Brandon's exact identity, wardrobe and own garage gym with the black table. Use the second attached image only as a composition reference for the camera position, framing and how the objects are held and poured; do not copy its person, wooden courtyard, red robe, bottle brand, table or the caption text. Use the third attached image only for the Natural Rems Sea Moss jar: copy ONLY the front jar, without the MADE IN USA banner at the top, without the second jar behind it and without the loose gummies.",
  "identity_main": "The exact fictional AI character holistic.brandon: Black mixed-race American woman around thirty, athletic and toned, medium light-brown skin with light freckles across the nose and cheeks, dark brown eyes, defined eyebrows, full lips, hair in tight cornrows that turn into long loose braids falling over both shoulders, finished with small wooden and gold beads, a black floral blackwork tattoo sleeve on her right arm, a fine line tattoo on her left inner arm and a small fine-line floral tattoo below her left collarbone.",
  "wardrobe": "Plain white ribbed tank top with nothing printed on it, loose black training shorts, a thin gold chain with a small gold cross pendant and small stud earrings.",
  "scene": "Her own garage gym: a white-painted concrete block wall behind her, a red neon sign reading TRAIN PRAY REPEAT on the wall at the left, a whiteboard with handwritten black marker reading STAY READY. STAY DISCIPLINED. on the right, and a small American flag pinned above the whiteboard, discreet but clearly visible and in focus. In front of her stands a plain matte black table.",
  "prop": "In her right hand, held still beside her right cheek, the Natural Rems Sea Moss jar: a short wide jar of dark amber plastic with a black screw cap, a pale cream-green label with dark green text, the Natural Rems logo with three leaves, the big title Sea Moss Gummies, a 6000 MG | 16-IN-1 badge, the words GREEN APPLE FLAVOR, a list of ingredients in dark green pill shapes and green seaweed illustrations on both sides, label facing the camera, fully readable. Her left hand rests on the black table.",
  "posture": "Brandon holds the jar still beside her right cheek, label toward the lens.",
  "composition": "Straight-on medium shot: the jar is held up beside her right cheek and pushed slightly toward the camera, the phone lens is about 30 centimeters from the jar, which fills 20 percent of the frame at the right of her face, closer to the camera than her face, label facing the camera and fully readable. The background is reduced by framing, never by blur.",
  "camera": "phone at her chest height, straight-on, standard 1x lens, light handheld",
  "lighting": "Neutral overcast daylight from a large window out of frame, soft even light on her face, hands and the table with no harsh shadows. The red neon glows on the wall but does not tint her skin.",
  "state": "Start frame: Brandon is caught mid-sentence, lips naturally parted, animated expression, looking straight into the lens, inviting, smiling on yes.",
  "realism": "Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday reality, background fully in focus, everything in sharp focus, no AI polish, no beauty smoothing.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no plastic-looking skin, no extra fingers, no third hand, no blur, no bokeh, no warm orange color cast, no yellow tint, no golden glow, no golden hour light, no sunset, no HDR, no cinematic lighting, no beauty smoothing, no visible phone, no studio, no second person, no eyeglasses, no grey curly hair, no wooden bench, no street, no houses, no silver cross, no second jar, no other bottles, no loose gummies, no banner above the jar, no hand covering the label"
}
```

### K11 · T11, CTA da marca, Amazon e legenda · anexar ÂNCORA HOLISTIC BRANDON + FRAME DO MODELO + FOTO DO PRODUTO

```text
K11
{
  "format": "IMPORTANT: THIS IS IPHONE FOOTAGE. Vertical 9:16.",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "reference_use": "Use the first attached image only for Brandon's exact identity, wardrobe and own garage gym with the black table. Use the second attached image only as a composition reference for the camera position, framing and how the objects are held and poured; do not copy its person, wooden courtyard, red robe, bottle brand, table or the caption text. Use the third attached image only for the Natural Rems Sea Moss jar: copy ONLY the front jar, without the MADE IN USA banner at the top, without the second jar behind it and without the loose gummies.",
  "identity_main": "The exact fictional AI character holistic.brandon: Black mixed-race American woman around thirty, athletic and toned, medium light-brown skin with light freckles across the nose and cheeks, dark brown eyes, defined eyebrows, full lips, hair in tight cornrows that turn into long loose braids falling over both shoulders, finished with small wooden and gold beads, a black floral blackwork tattoo sleeve on her right arm, a fine line tattoo on her left inner arm and a small fine-line floral tattoo below her left collarbone.",
  "wardrobe": "Plain white ribbed tank top with nothing printed on it, loose black training shorts, a thin gold chain with a small gold cross pendant and small stud earrings.",
  "scene": "Her own garage gym: a white-painted concrete block wall behind her, a red neon sign reading TRAIN PRAY REPEAT on the wall at the left, a whiteboard with handwritten black marker reading STAY READY. STAY DISCIPLINED. on the right, and a small American flag pinned above the whiteboard, discreet but clearly visible and in focus. In front of her stands a plain matte black table.",
  "prop": "In her right hand, held still beside her right cheek, the Natural Rems Sea Moss jar: a short wide jar of dark amber plastic with a black screw cap, a pale cream-green label with dark green text, the Natural Rems logo with three leaves, the big title Sea Moss Gummies, a 6000 MG | 16-IN-1 badge, the words GREEN APPLE FLAVOR, a list of ingredients in dark green pill shapes and green seaweed illustrations on both sides, label facing the camera, fully readable. Her left hand rests on the black table.",
  "posture": "Brandon holds the jar still beside her right cheek, label toward the lens.",
  "composition": "Straight-on medium shot: the jar is held up beside her right cheek and pushed slightly toward the camera, the phone lens is about 30 centimeters from the jar, which fills 20 percent of the frame at the right of her face, closer to the camera than her face, label facing the camera and fully readable. The background is reduced by framing, never by blur.",
  "camera": "phone at her chest height, straight-on, standard 1x lens, light handheld",
  "lighting": "Neutral overcast daylight from a large window out of frame, soft even light on her face, hands and the table with no harsh shadows. The red neon glows on the wall but does not tint her skin.",
  "state": "Start frame: Brandon is caught mid-sentence, lips naturally parted, animated expression, looking straight into the lens, clear and slow on the brand name.",
  "realism": "Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday reality, background fully in focus, everything in sharp focus, no AI polish, no beauty smoothing.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no plastic-looking skin, no extra fingers, no third hand, no blur, no bokeh, no warm orange color cast, no yellow tint, no golden glow, no golden hour light, no sunset, no HDR, no cinematic lighting, no beauty smoothing, no visible phone, no studio, no second person, no eyeglasses, no grey curly hair, no wooden bench, no street, no houses, no silver cross, no second jar, no other bottles, no loose gummies, no banner above the jar, no hand covering the label"
}
```

## 3. PROMPTS DE VÍDEO (um bloco por V)

### V01 · T1 · frame inicial = a imagem que você deixou no K01

```text
V01
a avatar Brandon, mulher, fala em inglês com sotaque americano de uma mulher negra americana, voz feminina clara e firme de uma mulher de uns trinta anos, entonação calma e um pouco brincalhona, mostrando a dose pequena, voz autêntica, como se exigisse ser ouvida, a seguinte frase: "This is how much sugar is in my sea moss gummy."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Brandon despeja uma fina linha de açúcar da garrafa na colher e a colher pinga uma pitada no copinho de shot, falando para a câmera. Ela diz a frase em ritmo natural logo no começo e a ação continua até o fim.

câmera: fixa, leve handheld natural

som ambiente: box de treino em casa, tranquilo, sem música
```

### V02 · T2 · frame inicial = a imagem que você deixou no K02

```text
V02
a avatar Brandon, mulher, fala em inglês com sotaque americano de uma mulher negra americana, voz feminina clara e firme de uma mulher de uns trinta anos, entonação animada, sobrancelhas erguidas, mostrando o tanto, voz autêntica, como se exigisse ser ouvida, a seguinte frase: "And this is how much sugar is packed into most sea moss gummies on the shelf."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Brandon segura o pote grande pela lateral e despeja a garrafa de açúcar dentro dele em jato grosso, falando para a câmera.

câmera: fixa, leve handheld natural

som ambiente: box de treino em casa, tranquilo, sem música
```

### V03 · T3 · frame inicial = a imagem que você deixou no K03

```text
V03
a avatar Brandon, mulher, fala em inglês com sotaque americano de uma mulher negra americana, voz feminina clara e firme de uma mulher de uns trinta anos, entonação confiante, como quem promete uma virada, voz autêntica, como se exigisse ser ouvida, a seguinte frase: "And after this video, you are never going to want to buy the wrong one again."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Brandon continua o despejo até o pote ficar quase cheio, falando para a câmera.

câmera: fixa, leve handheld natural

som ambiente: box de treino em casa, tranquilo, sem música
```

### V04 · T4 · frame inicial = a imagem que você deixou no K04

```text
V04
a avatar Brandon, mulher, fala em inglês com sotaque americano de uma mulher negra americana, voz feminina clara e firme de uma mulher de uns trinta anos, entonação animada, contando nos dedos, voz autêntica, como se exigisse ser ouvida, a seguinte frase: "Number one, the average gummy is mostly sugar and fillers, so it is candy. Number two, you need real wild Irish sea moss, not a sprinkle."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Brandon fala para a câmera contando um ponto de cada vez nos dedos.

câmera: fixa, leve handheld natural

som ambiente: box de treino em casa, tranquilo, sem música
```

### V05 · T5 · frame inicial = a imagem que você deixou no K05

```text
V05
a avatar Brandon, mulher, fala em inglês com sotaque americano de uma mulher negra americana, voz feminina clara e firme de uma mulher de uns trinta anos, entonação animada e um pouco provocadora, voz autêntica, como se exigisse ser ouvida, a seguinte frase: "Number three, it should be made in the USA, not who knows where. Number four, if it tastes like seaweed, you will quit by Friday."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Brandon fala para a câmera gesticulando com as duas mãos e contando nos dedos.

câmera: fixa, leve handheld natural

som ambiente: box de treino em casa, tranquilo, sem música
```

### V06 · T6 · frame inicial = a imagem que você deixou no K06

```text
V06
a avatar Brandon, mulher, fala em inglês com sotaque americano de uma mulher negra americana, voz feminina clara e firme de uma mulher de uns trinta anos, entonação séria e acolhedora, baixando a voz, voz autêntica, como se exigisse ser ouvida, a seguinte frase: "And last, but certainly not least, if your body is already running on stress, a pile of sugar is the last thing it needs."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Brandon se inclina um pouco para a câmera e fala com as mãos abertas.

câmera: fixa, leve handheld natural

som ambiente: box de treino em casa, tranquilo, sem música
```

### V07 · T7 · frame inicial = a imagem que você deixou no K07

```text
V07
a avatar Brandon, mulher, fala em inglês com sotaque americano de uma mulher negra americana, voz feminina clara e firme de uma mulher de uns trinta anos, entonação calma e segura de quem tem autoridade, voz autêntica, como se exigisse ser ouvida, a seguinte frase: "For years I have coached women, and most of what gets sold to them was never built for a body running on stress."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Brandon fala para a câmera com os antebraços na borda da mesa.

câmera: fixa, leve handheld natural

som ambiente: box de treino em casa, tranquilo, sem música
```

### V08 · T8 · frame inicial = a imagem que você deixou no K08

```text
V08
a avatar Brandon, mulher, fala em inglês com sotaque americano de uma mulher negra americana, voz feminina clara e firme de uma mulher de uns trinta anos, entonação calorosa e firme, voz autêntica, como se exigisse ser ouvida, a seguinte frase: "One lesson remains true. Your body does better when you stop feeding what keeps it stuck, and start giving it what it was missing."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Brandon fala para a câmera abrindo as duas mãos devagar.

câmera: fixa, leve handheld natural

som ambiente: box de treino em casa, tranquilo, sem música
```

### V09 · T9 · frame inicial = a imagem que você deixou no K09

```text
V09
a avatar Brandon, mulher, fala em inglês com sotaque americano de uma mulher negra americana, voz feminina clara e firme de uma mulher de uns trinta anos, entonação orgulhosa, dizendo Natural Rems Sea Moss devagar e por inteiro, voz autêntica, como se exigisse ser ouvida, a seguinte frase: "So I take Natural Rems Sea Moss. It is wild Irish, made in the USA, under one gram of sugar, and sixteen ingredients inside a green apple gummy."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Brandon ergue o frasco devagar da altura da cintura até o lado do rosto no nome do produto e o deixa parado, rótulo de frente.

câmera: fixa

som ambiente: box de treino em casa, tranquilo, sem música
```

### V10 · T10 · frame inicial = a imagem que você deixou no K10

```text
V10
a avatar Brandon, mulher, fala em inglês com sotaque americano de uma mulher negra americana, voz feminina clara e firme de uma mulher de uns trinta anos, entonação convidativa, sorrindo no yes, voz autêntica, como se exigisse ser ouvida, a seguinte frase: "Comment yes if your sweet cravings are winning every night, and follow me so this one stays on your profile."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Brandon fala para a câmera com o frasco parado ao lado do rosto, rótulo de frente, sorrindo no yes.

câmera: fixa

som ambiente: box de treino em casa, tranquilo, sem música
```

### V11 · T11 · frame inicial = a imagem que você deixou no K11

```text
V11
a avatar Brandon, mulher, fala em inglês com sotaque americano de uma mulher negra americana, voz feminina clara e firme de uma mulher de uns trinta anos, entonação clara, dizendo Natural Rems Sea Moss devagar e por inteiro, voz autêntica, como se exigisse ser ouvida, a seguinte frase: "Search Natural Rems Sea Moss on Amazon. Or you can just tap the link I left in the caption."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Brandon fala para a câmera com o frasco parado ao lado do rosto, rótulo de frente, do começo ao fim, sem baixar o frasco.

câmera: fixa

som ambiente: box de treino em casa, tranquilo, sem música
```

## 4. Montagem no CapCut

1. Clipes numerados na ordem: V01 a V11.
2. Gancho no tempo do modelo: V01 0,00 a 4,40 s; V02 4,40 a ~9,80 s; V03 ~9,80 a 14,30 s. Cortar logo depois da última palavra de cada clipe.
3. Corte seco entre clipes, sem transição. Zero tempo morto: todo clipe começa já falando. Isolate Voice / Keep Vocal no áudio.
4. Legenda de tela branca sem serifa, duas a três palavras por vez, no meio do quadro, igual ao modelo. No V10, `yes` grande e isolado na tela. No V11, duas setas vermelhas apontando para baixo (para a legenda do post).
5. Sem Voice Changer: a voz da Brandon vem do prompt de cada V.
6. Música opcional só a partir do V04, nunca no gancho, entre -19 e -20 dB, fora da biblioteca do TikTok.
7. Rótulo pequeno `AI-generated` num canto do vídeo.
8. No V09 a V11 o frasco não pode ser cortado nem coberto: nenhum B-roll por cima (regra da marca).

## 5. Legenda do post

- Primeira linha, sempre: `#ad #syntheticperformer #naturalrems`
- Logo abaixo: o link da Amazon do Natural Rems Sea Moss (o V11 manda tocar no link da legenda).
- Chave de conteúdo de IA da plataforma LIGADA.

## 6. Transcrição final por take

| Take | English | Português |
|---|---|---|
| T1 | This is how much sugar is in my sea moss gummy. | Essa é a quantidade de açúcar que tem no meu sea moss em goma. |
| T2 | And this is how much sugar is packed into most sea moss gummies on the shelf. | E essa é a quantidade de açúcar enfiada na maioria das gomas de sea moss da prateleira. |
| T3 | And after this video, you are never going to want to buy the wrong one again. | E depois deste vídeo, você nunca mais vai querer comprar a errada. |
| T4 | Number one, the average gummy is mostly sugar and fillers, so it is candy. Number two, you need real wild Irish sea moss, not a sprinkle. | Número um, a goma média é quase só açúcar e enchimento, então é bala. Número dois, você precisa de sea moss irlandês selvagem de verdade, não de uma pitada. |
| T5 | Number three, it should be made in the USA, not who knows where. Number four, if it tastes like seaweed, you will quit by Friday. | Número três, tem que ser feito nos EUA, não sei onde. Número quatro, se tem gosto de alga, você larga até sexta. |
| T6 | And last, but certainly not least, if your body is already running on stress, a pile of sugar is the last thing it needs. | E por último, mas não menos importante, se o seu corpo já roda no estresse, uma pilha de açúcar é a última coisa de que ele precisa. |
| T7 | For years I have coached women, and most of what gets sold to them was never built for a body running on stress. | Faz anos que eu treino mulheres, e a maior parte do que é vendido pra elas nunca foi feita pra um corpo que roda no estresse. |
| T8 | One lesson remains true. Your body does better when you stop feeding what keeps it stuck, and start giving it what it was missing. | Uma lição continua verdadeira. O seu corpo funciona melhor quando você para de alimentar o que o trava e começa a dar o que faltava. |
| T9 | So I take Natural Rems Sea Moss. It is wild Irish, made in the USA, under one gram of sugar, and sixteen ingredients inside a green apple gummy. | Então eu tomo o Natural Rems Sea Moss. É irlandês selvagem, feito nos EUA, menos de um grama de açúcar, e dezesseis ingredientes dentro de uma goma de maçã verde. |
| T10 | Comment yes if your sweet cravings are winning every night, and follow me so this one stays on your profile. | Comente yes se a vontade de doce vem ganhando todas as noites, e me siga pra este vídeo continuar no seu perfil. |
| T11 | Search Natural Rems Sea Moss on Amazon. Or you can just tap the link I left in the caption. | Procure Natural Rems Sea Moss na Amazon. Ou é só tocar no link que eu deixei na legenda. |

## 7. Roteiro final em inglês

1. This is how much sugar is in my sea moss gummy.
2. And this is how much sugar is packed into most sea moss gummies on the shelf.
3. And after this video, you are never going to want to buy the wrong one again.
4. Number one, the average gummy is mostly sugar and fillers, so it is candy. Number two, you need real wild Irish sea moss, not a sprinkle.
5. Number three, it should be made in the USA, not who knows where. Number four, if it tastes like seaweed, you will quit by Friday.
6. And last, but certainly not least, if your body is already running on stress, a pile of sugar is the last thing it needs.
7. For years I have coached women, and most of what gets sold to them was never built for a body running on stress.
8. One lesson remains true. Your body does better when you stop feeding what keeps it stuck, and start giving it what it was missing.
9. So I take Natural Rems Sea Moss. It is wild Irish, made in the USA, under one gram of sugar, and sixteen ingredients inside a green apple gummy.
10. Comment yes if your sweet cravings are winning every night, and follow me so this one stays on your profile.
11. Search Natural Rems Sea Moss on Amazon. Or you can just tap the link I left in the caption.

This is how much sugar is in my sea moss gummy. And this is how much sugar is packed into most sea moss gummies on the shelf. And after this video, you are never going to want to buy the wrong one again. Number one, the average gummy is mostly sugar and fillers, so it is candy. Number two, you need real wild Irish sea moss, not a sprinkle. Number three, it should be made in the USA, not who knows where. Number four, if it tastes like seaweed, you will quit by Friday. And last, but certainly not least, if your body is already running on stress, a pile of sugar is the last thing it needs. For years I have coached women, and most of what gets sold to them was never built for a body running on stress. One lesson remains true. Your body does better when you stop feeding what keeps it stuck, and start giving it what it was missing. So I take Natural Rems Sea Moss. It is wild Irish, made in the USA, under one gram of sugar, and sixteen ingredients inside a green apple gummy. Comment yes if your sweet cravings are winning every night, and follow me so this one stays on your profile. Search Natural Rems Sea Moss on Amazon. Or you can just tap the link I left in the caption.
