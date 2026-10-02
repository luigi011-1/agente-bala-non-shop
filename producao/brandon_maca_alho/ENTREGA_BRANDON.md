# ENTREGA | holistic.brandon | FityWell Venda Alho na maçã

Produção `brandon_maca_alho` · Ângulo 2 · VENDA · vídeo modelo de avatar IA · rodada de VALIDAÇÃO · perfil CLÁSSICO

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

Checklist de envio: 35/35 aprovados (N/A: A1, A2 fiéis ao modelo; C3 a C7 sem segunda pessoa, selfie, frase repetida, cena atuada ou motion control)

Ficha: 13/13 K conferidos contra o frame do modelo, placar 14/14 cada (`FICHA_FRAMES.md`, GATE_VISUAL Parte 6)

## Anexos

- **Âncora holistic.brandon:** `producao/_ancoras/holistic_brandon_ancora.jpg` em TODOS os K.
- **Em cada K**, anexar também o frame do modelo daquele passo (`producao/brandon_maca_alho/input/frames_modelo/Kxx_modelo.png`), só como referência de composição.
- K01 a K13 casam com V01 a V13 pelo número. Todos os V têm fala.

| Código | Take | Frame do modelo |
|---|---|---|
| K01 / V01 | T1, gancho, alho na maçã colada na lente | `input/frames_modelo/K01_modelo.png` |
| K02 / V02 | T2, receita, maçã picada na jarra | `input/frames_modelo/K02_modelo.png` |
| K03 / V03 | T3, receita, alho e limão | `input/frames_modelo/K03_modelo.png` |
| K04 / V04 | T4, receita, copo de água | `input/frames_modelo/K04_modelo.png` |
| K05 / V05 | T5, despeja o suco no copo | `input/frames_modelo/K05_modelo.png` |
| K06 / V06 | T6, copo na mão, resultado | `input/frames_modelo/K06_modelo.png` |
| K07 / V07 | T7, copo na mão, quinto ingrediente | `input/frames_modelo/K07_modelo.png` |
| K08 / V08 | T8, copo na mão, a frase das clientes | `input/frames_modelo/K08_modelo.png` |
| K09 / V09 | T9, copo na mão, as três causas | `input/frames_modelo/K09_modelo.png` |
| K10 / V10 | T10, copo na mão, álibi | `input/frames_modelo/K10_modelo.png` |
| K11 / V11 | T11, copo na mão, o app | `input/frames_modelo/K11_modelo.png` |
| K12 / V12 | T12, copo na mão, comment yes + follow | `input/frames_modelo/K12_modelo.png` |
| K13 / V13 | T13, CTA, plano mais fechado | `input/frames_modelo/K13_modelo.png` |

## 2. PROMPTS DE IMAGEM (um bloco por K)

### K01 · T1, gancho, alho na maçã colada na lente · anexar ÂNCORA + FRAME DO MODELO

```text
K01
{
  "format": "IMPORTANT: THIS IS IPHONE FOOTAGE. Vertical 9:16.",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "reference_use": "Use the first attached image only for Brandon's exact identity, wardrobe and own garage gym with the black table. Use the second attached image only as a composition reference for the camera position, framing and the action; do not copy its person, eyeglasses, gray t-shirt, white kitchen, marble countertop, wall decorations or the caption text.",
  "identity_main": "The exact fictional AI character holistic.brandon: Black mixed-race American woman around thirty, athletic and toned, medium light-brown skin with light freckles across the nose and cheeks, dark brown eyes, defined eyebrows, full lips, hair in tight cornrows that turn into long loose braids falling over both shoulders, finished with small wooden and gold beads, a black floral blackwork tattoo sleeve on her right arm, a fine line tattoo on her left inner arm and a small fine-line floral tattoo below her left collarbone.",
  "wardrobe": "Plain white ribbed tank top with nothing printed on it, loose black training shorts, a thin gold chain with a small gold cross pendant and small stud earrings.",
  "scene": "Her own garage gym: a white-painted concrete block wall behind her, a red neon sign reading TRAIN PRAY REPEAT on the wall at the left, a whiteboard with handwritten black marker reading STAY READY. STAY DISCIPLINED. on the right, and a small American flag pinned above the whiteboard, discreet but clearly visible and in focus. In front of her stands a plain matte black table she uses as a counter.",
  "prop": "A whole shiny red apple with its core scooped out from the top, leaving a round hole about 3 centimeters wide that shows clean pale cream flesh inside, resting in her right palm on the left side of the frame; in her left hand, between thumb and index finger, a single peeled garlic clove, held just above the hole. There is nothing else in her hands and the black table below is empty.",
  "posture": "Brandon leans over the black table toward the lens, holding the apple out toward the camera.",
  "composition": "Close-up from chest height: the phone lens is about 15 centimeters from the apple, which fills the lower 35 percent of the frame at the left of center, far closer to the camera than her face and larger than her head, nothing else competing with it; the garlic clove is just above it and her face is in the upper third. The background is reduced by framing, never by blur.",
  "camera": "phone held at her chest height, tilted down toward the apple, wide 0.5x lens, light handheld",
  "lighting": "Neutral overcast daylight from a large window out of frame, soft even light on her face, hands and the table with no harsh shadows. The red neon glows on the wall but does not tint her skin.",
  "state": "Start frame: the garlic clove is held just above the hole, not yet inside; the hole shows only clean pale flesh, no foam yet. Brandon is caught mid-sentence, lips naturally parted, animated expression, looking straight into the lens.",
  "realism": "Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday reality, background fully in focus, everything in sharp focus, no AI polish, no beauty smoothing.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no printed labels or lettering on the blender, bowl, glass or apple, no studio, no plastic-looking skin, no extra fingers, no third hand, no blur, no bokeh, no warm orange color cast, no yellow tint, no golden glow, no golden hour light, no sunset, no HDR, no cinematic lighting, no beauty smoothing, no visible phone, no second person, no eyeglasses, no gray t-shirt, no white kitchen cabinets, no marble countertop, no silver cross, no foam yet, no bubbles yet"
}
```

### K02 · T2, receita, maçã picada na jarra · anexar ÂNCORA + FRAME DO MODELO

```text
K02
{
  "format": "IMPORTANT: THIS IS IPHONE FOOTAGE. Vertical 9:16.",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "reference_use": "Use the first attached image only for Brandon's exact identity, wardrobe and own garage gym with the black table. Use the second attached image only as a composition reference for the camera position, framing and the action; do not copy its person, eyeglasses, gray t-shirt, white kitchen, marble countertop, wall decorations or the caption text.",
  "identity_main": "The exact fictional AI character holistic.brandon: Black mixed-race American woman around thirty, athletic and toned, medium light-brown skin with light freckles across the nose and cheeks, dark brown eyes, defined eyebrows, full lips, hair in tight cornrows that turn into long loose braids falling over both shoulders, finished with small wooden and gold beads, a black floral blackwork tattoo sleeve on her right arm, a fine line tattoo on her left inner arm and a small fine-line floral tattoo below her left collarbone.",
  "wardrobe": "Plain white ribbed tank top with nothing printed on it, loose black training shorts, a thin gold chain with a small gold cross pendant and small stud earrings.",
  "scene": "Her own garage gym: a white-painted concrete block wall behind her, a red neon sign reading TRAIN PRAY REPEAT on the wall at the left, a whiteboard with handwritten black marker reading STAY READY. STAY DISCIPLINED. on the right, and a small American flag pinned above the whiteboard, discreet but clearly visible and in focus. In front of her stands a plain matte black table she uses as a counter.",
  "prop": "On the black table in the lower foreground, a glass blender jar on a stainless steel base, empty. In her hands, a white ceramic bowl full of apple chunks with red skin, tilted over the open jar so the first chunks slide toward it. On the table beside the blender: half a lemon cut side up, one peeled garlic clove and a clear drinking glass full of water.",
  "posture": "Brandon stands behind the black table, both hands holding the bowl tilted over the jar.",
  "composition": "Standing medium shot from chest height: the phone lens is about 40 centimeters from the blender jar, which fills the lower 35 percent of the frame at the left, closer to the camera than her face; the tilted bowl is at the upper right, close to the lens; her face and shoulders are in the upper part of the frame. Nothing else is on the table. The background is reduced by framing, never by blur.",
  "camera": "phone held at her chest height, tilted slightly down toward the table, standard 1x lens, light handheld",
  "lighting": "Neutral overcast daylight from a large window out of frame, soft even light on her face, hands and the table with no harsh shadows. The red neon glows on the wall but does not tint her skin.",
  "state": "Start frame: the first apple chunks are sliding from the bowl into the empty jar. Brandon is caught mid-sentence, lips naturally parted, animated expression, looking straight into the lens.",
  "realism": "Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday reality, background fully in focus, everything in sharp focus, no AI polish, no beauty smoothing.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no printed labels or lettering on the blender, bowl, glass or apple, no studio, no plastic-looking skin, no extra fingers, no third hand, no blur, no bokeh, no warm orange color cast, no yellow tint, no golden glow, no golden hour light, no sunset, no HDR, no cinematic lighting, no beauty smoothing, no visible phone, no second person, no eyeglasses, no gray t-shirt, no white kitchen cabinets, no marble countertop, no silver cross"
}
```

### K03 · T3, receita, alho e limão · anexar ÂNCORA + FRAME DO MODELO

```text
K03
{
  "format": "IMPORTANT: THIS IS IPHONE FOOTAGE. Vertical 9:16.",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "reference_use": "Use the first attached image only for Brandon's exact identity, wardrobe and own garage gym with the black table. Use the second attached image only as a composition reference for the camera position, framing and the action; do not copy its person, eyeglasses, gray t-shirt, white kitchen, marble countertop, wall decorations or the caption text.",
  "identity_main": "The exact fictional AI character holistic.brandon: Black mixed-race American woman around thirty, athletic and toned, medium light-brown skin with light freckles across the nose and cheeks, dark brown eyes, defined eyebrows, full lips, hair in tight cornrows that turn into long loose braids falling over both shoulders, finished with small wooden and gold beads, a black floral blackwork tattoo sleeve on her right arm, a fine line tattoo on her left inner arm and a small fine-line floral tattoo below her left collarbone.",
  "wardrobe": "Plain white ribbed tank top with nothing printed on it, loose black training shorts, a thin gold chain with a small gold cross pendant and small stud earrings.",
  "scene": "Her own garage gym: a white-painted concrete block wall behind her, a red neon sign reading TRAIN PRAY REPEAT on the wall at the left, a whiteboard with handwritten black marker reading STAY READY. STAY DISCIPLINED. on the right, and a small American flag pinned above the whiteboard, discreet but clearly visible and in focus. In front of her stands a plain matte black table she uses as a counter.",
  "prop": "On the black table in the lower foreground, a glass blender jar on a stainless steel base, half full of apple chunks with red skin. Her right hand holds a single peeled garlic clove right above the open jar. Half a lemon, still whole and unsqueezed, lies cut side up on the table next to the jar, and a clear drinking glass full of water stands behind it.",
  "posture": "Brandon stands behind the black table; her right hand holds the garlic clove right above the open jar and her left hand rests on the table edge.",
  "composition": "Standing medium shot from chest height: the phone lens is about 45 centimeters from the blender jar, which fills the lower 40 percent of the frame at the left of center, closer to the camera than her face; her face and torso fill the upper part of the frame. Nothing else is on the table. The background is reduced by framing, never by blur.",
  "camera": "phone held at her chest height, tilted slightly down toward the table, standard 1x lens, light handheld",
  "lighting": "Neutral overcast daylight from a large window out of frame, soft even light on her face, hands and the table with no harsh shadows. The red neon glows on the wall but does not tint her skin.",
  "state": "Start frame: the garlic clove is about to drop into the jar. Brandon is caught mid-sentence, lips naturally parted, animated expression, looking straight into the lens.",
  "realism": "Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday reality, background fully in focus, everything in sharp focus, no AI polish, no beauty smoothing.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no printed labels or lettering on the blender, bowl, glass or apple, no studio, no plastic-looking skin, no extra fingers, no third hand, no blur, no bokeh, no warm orange color cast, no yellow tint, no golden glow, no golden hour light, no sunset, no HDR, no cinematic lighting, no beauty smoothing, no visible phone, no second person, no eyeglasses, no gray t-shirt, no white kitchen cabinets, no marble countertop, no silver cross"
}
```

### K04 · T4, receita, copo de água · anexar ÂNCORA + FRAME DO MODELO

```text
K04
{
  "format": "IMPORTANT: THIS IS IPHONE FOOTAGE. Vertical 9:16.",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "reference_use": "Use the first attached image only for Brandon's exact identity, wardrobe and own garage gym with the black table. Use the second attached image only as a composition reference for the camera position, framing and the action; do not copy its person, eyeglasses, gray t-shirt, white kitchen, marble countertop, wall decorations or the caption text.",
  "identity_main": "The exact fictional AI character holistic.brandon: Black mixed-race American woman around thirty, athletic and toned, medium light-brown skin with light freckles across the nose and cheeks, dark brown eyes, defined eyebrows, full lips, hair in tight cornrows that turn into long loose braids falling over both shoulders, finished with small wooden and gold beads, a black floral blackwork tattoo sleeve on her right arm, a fine line tattoo on her left inner arm and a small fine-line floral tattoo below her left collarbone.",
  "wardrobe": "Plain white ribbed tank top with nothing printed on it, loose black training shorts, a thin gold chain with a small gold cross pendant and small stud earrings.",
  "scene": "Her own garage gym: a white-painted concrete block wall behind her, a red neon sign reading TRAIN PRAY REPEAT on the wall at the left, a whiteboard with handwritten black marker reading STAY READY. STAY DISCIPLINED. on the right, and a small American flag pinned above the whiteboard, discreet but clearly visible and in focus. In front of her stands a plain matte black table she uses as a counter.",
  "prop": "On the black table, a glass blender jar on a stainless steel base, half full of apple chunks with a garlic clove and lemon juice. Her right hand lifts the clear drinking glass full of water above the open top of the jar. The squeezed lemon half lies cut side up at the lower left corner of the table.",
  "posture": "Brandon stands behind the black table; her right hand lifts the clear drinking glass over the jar.",
  "composition": "Standing medium shot from chest height: the squeezed lemon half is about 15 centimeters from the lens at the lower left corner and the blender jar, about 40 centimeters away, fills the lower 40 percent of the frame at the center, both closer to the camera than her face; her face and torso fill the upper part of the frame. Nothing else is on the table. The background is reduced by framing, never by blur.",
  "camera": "phone held at her chest height, tilted slightly down toward the table, standard 1x lens, light handheld",
  "lighting": "Neutral overcast daylight from a large window out of frame, soft even light on her face, hands and the table with no harsh shadows. The red neon glows on the wall but does not tint her skin.",
  "state": "Start frame: the glass of water is tilted just above the jar, the water not poured yet. Brandon is caught mid-sentence, lips naturally parted, animated expression, looking straight into the lens.",
  "realism": "Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday reality, background fully in focus, everything in sharp focus, no AI polish, no beauty smoothing.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no printed labels or lettering on the blender, bowl, glass or apple, no studio, no plastic-looking skin, no extra fingers, no third hand, no blur, no bokeh, no warm orange color cast, no yellow tint, no golden glow, no golden hour light, no sunset, no HDR, no cinematic lighting, no beauty smoothing, no visible phone, no second person, no eyeglasses, no gray t-shirt, no white kitchen cabinets, no marble countertop, no silver cross"
}
```

### K05 · T5, despeja o suco no copo · anexar ÂNCORA + FRAME DO MODELO

```text
K05
{
  "format": "IMPORTANT: THIS IS IPHONE FOOTAGE. Vertical 9:16.",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "reference_use": "Use the first attached image only for Brandon's exact identity, wardrobe and own garage gym with the black table. Use the second attached image only as a composition reference for the camera position, framing and the action; do not copy its person, eyeglasses, gray t-shirt, white kitchen, marble countertop, wall decorations or the caption text.",
  "identity_main": "The exact fictional AI character holistic.brandon: Black mixed-race American woman around thirty, athletic and toned, medium light-brown skin with light freckles across the nose and cheeks, dark brown eyes, defined eyebrows, full lips, hair in tight cornrows that turn into long loose braids falling over both shoulders, finished with small wooden and gold beads, a black floral blackwork tattoo sleeve on her right arm, a fine line tattoo on her left inner arm and a small fine-line floral tattoo below her left collarbone.",
  "wardrobe": "Plain white ribbed tank top with nothing printed on it, loose black training shorts, a thin gold chain with a small gold cross pendant and small stud earrings.",
  "scene": "Her own garage gym: a white-painted concrete block wall behind her, a red neon sign reading TRAIN PRAY REPEAT on the wall at the left, a whiteboard with handwritten black marker reading STAY READY. STAY DISCIPLINED. on the right, and a small American flag pinned above the whiteboard, discreet but clearly visible and in focus. In front of her stands a plain matte black table she uses as a counter.",
  "prop": "The glass blender jar, lifted off its base and full of a thick pale creamy yellow-green apple drink, tilted in her right hand over an empty clear drinking glass that she holds in her left hand just above the black table.",
  "posture": "Brandon is leaning over the black table toward the lens, jar in one hand and glass in the other.",
  "composition": "Close shot from chest height: the phone lens is about 30 centimeters from the jar and the glass, which together fill the lower 45 percent of the frame at the center right, larger than her head and closer to the camera than her face; her face and shoulders are in the upper third. Nothing else is on the table. The background is reduced by framing, never by blur.",
  "camera": "phone held at her chest height, tilted slightly down toward the table, standard 1x lens, light handheld",
  "lighting": "Neutral overcast daylight from a large window out of frame, soft even light on her face, hands and the table with no harsh shadows. The red neon glows on the wall but does not tint her skin.",
  "state": "Start frame: the first stream of the thick drink is starting to fall into the empty glass. Brandon is caught mid-sentence, lips naturally parted, animated expression, looking straight into the lens.",
  "realism": "Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday reality, background fully in focus, everything in sharp focus, no AI polish, no beauty smoothing.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no printed labels or lettering on the blender, bowl, glass or apple, no studio, no plastic-looking skin, no extra fingers, no third hand, no blur, no bokeh, no warm orange color cast, no yellow tint, no golden glow, no golden hour light, no sunset, no HDR, no cinematic lighting, no beauty smoothing, no visible phone, no second person, no eyeglasses, no gray t-shirt, no white kitchen cabinets, no marble countertop, no silver cross"
}
```

### K06 · T6, copo na mão, resultado · anexar ÂNCORA + FRAME DO MODELO

```text
K06
{
  "format": "IMPORTANT: THIS IS IPHONE FOOTAGE. Vertical 9:16.",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "reference_use": "Use the first attached image only for Brandon's exact identity, wardrobe and own garage gym with the black table. Use the second attached image only as a composition reference for the camera position, framing and the action; do not copy its person, eyeglasses, gray t-shirt, white kitchen, marble countertop, wall decorations or the caption text.",
  "identity_main": "The exact fictional AI character holistic.brandon: Black mixed-race American woman around thirty, athletic and toned, medium light-brown skin with light freckles across the nose and cheeks, dark brown eyes, defined eyebrows, full lips, hair in tight cornrows that turn into long loose braids falling over both shoulders, finished with small wooden and gold beads, a black floral blackwork tattoo sleeve on her right arm, a fine line tattoo on her left inner arm and a small fine-line floral tattoo below her left collarbone.",
  "wardrobe": "Plain white ribbed tank top with nothing printed on it, loose black training shorts, a thin gold chain with a small gold cross pendant and small stud earrings.",
  "scene": "Her own garage gym: a white-painted concrete block wall behind her, a red neon sign reading TRAIN PRAY REPEAT on the wall at the left, a whiteboard with handwritten black marker reading STAY READY. STAY DISCIPLINED. on the right, and a small American flag pinned above the whiteboard, discreet but clearly visible and in focus. In front of her stands a plain matte black table she uses as a counter.",
  "prop": "A clear drinking glass full of a pale creamy yellow apple drink, held up in her right hand at chest height, close to the lens in the lower foreground. The apple, the blender and the bowl are out of frame.",
  "posture": "Brandon stands behind the black table, leaning on its edge with both forearms, holding the glass up in her right hand, her left hand open in a small gesture.",
  "composition": "Straight-on medium shot: the phone lens is about 40 centimeters from the glass, which fills the lower left 20 percent of the frame, closer to the camera than her face; her face and shoulders fill the upper half of the frame and her forearms rest on the edge of the black table at the bottom. Nothing else is on the table. The background is reduced by framing, never by blur.",
  "camera": "phone at her eye level, standard 1x lens, straight-on, fixed",
  "lighting": "Neutral overcast daylight from a large window out of frame, soft even light on her face, hands and the table with no harsh shadows. The red neon glows on the wall but does not tint her skin.",
  "state": "Start frame: Brandon is caught mid-sentence, lips naturally parted, animated expression, looking straight into the lens, calm and sure.",
  "realism": "Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday reality, background fully in focus, everything in sharp focus, no AI polish, no beauty smoothing.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no printed labels or lettering on the blender, bowl, glass or apple, no studio, no plastic-looking skin, no extra fingers, no third hand, no blur, no bokeh, no warm orange color cast, no yellow tint, no golden glow, no golden hour light, no sunset, no HDR, no cinematic lighting, no beauty smoothing, no visible phone, no second person, no eyeglasses, no gray t-shirt, no white kitchen cabinets, no marble countertop, no silver cross"
}
```

### K07 · T7, copo na mão, quinto ingrediente · anexar ÂNCORA + FRAME DO MODELO

```text
K07
{
  "format": "IMPORTANT: THIS IS IPHONE FOOTAGE. Vertical 9:16.",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "reference_use": "Use the first attached image only for Brandon's exact identity, wardrobe and own garage gym with the black table. Use the second attached image only as a composition reference for the camera position, framing and the action; do not copy its person, eyeglasses, gray t-shirt, white kitchen, marble countertop, wall decorations or the caption text.",
  "identity_main": "The exact fictional AI character holistic.brandon: Black mixed-race American woman around thirty, athletic and toned, medium light-brown skin with light freckles across the nose and cheeks, dark brown eyes, defined eyebrows, full lips, hair in tight cornrows that turn into long loose braids falling over both shoulders, finished with small wooden and gold beads, a black floral blackwork tattoo sleeve on her right arm, a fine line tattoo on her left inner arm and a small fine-line floral tattoo below her left collarbone.",
  "wardrobe": "Plain white ribbed tank top with nothing printed on it, loose black training shorts, a thin gold chain with a small gold cross pendant and small stud earrings.",
  "scene": "Her own garage gym: a white-painted concrete block wall behind her, a red neon sign reading TRAIN PRAY REPEAT on the wall at the left, a whiteboard with handwritten black marker reading STAY READY. STAY DISCIPLINED. on the right, and a small American flag pinned above the whiteboard, discreet but clearly visible and in focus. In front of her stands a plain matte black table she uses as a counter.",
  "prop": "A clear drinking glass full of a pale creamy yellow apple drink, held up in her right hand at chest height, close to the lens in the lower foreground. The apple, the blender and the bowl are out of frame.",
  "posture": "Brandon stands behind the black table, leaning on its edge with both forearms, holding the glass up in her right hand, her left hand raised with the index finger up.",
  "composition": "Straight-on medium shot from slightly above: the phone lens is about 40 centimeters from the glass, which fills the lower left 20 percent of the frame, closer to the camera than her face; her face and shoulders fill the upper half of the frame and her forearms rest on the edge of the black table at the bottom. Nothing else is on the table. The background is reduced by framing, never by blur.",
  "camera": "phone just above her eye level, tilted slightly down, standard 1x lens, fixed",
  "lighting": "Neutral overcast daylight from a large window out of frame, soft even light on her face, hands and the table with no harsh shadows. The red neon glows on the wall but does not tint her skin.",
  "state": "Start frame: Brandon is caught mid-sentence, lips naturally parted, animated expression, looking straight into the lens, intrigued, as if about to tell a secret.",
  "realism": "Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday reality, background fully in focus, everything in sharp focus, no AI polish, no beauty smoothing.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no printed labels or lettering on the blender, bowl, glass or apple, no studio, no plastic-looking skin, no extra fingers, no third hand, no blur, no bokeh, no warm orange color cast, no yellow tint, no golden glow, no golden hour light, no sunset, no HDR, no cinematic lighting, no beauty smoothing, no visible phone, no second person, no eyeglasses, no gray t-shirt, no white kitchen cabinets, no marble countertop, no silver cross"
}
```

### K08 · T8, copo na mão, a frase das clientes · anexar ÂNCORA + FRAME DO MODELO

```text
K08
{
  "format": "IMPORTANT: THIS IS IPHONE FOOTAGE. Vertical 9:16.",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "reference_use": "Use the first attached image only for Brandon's exact identity, wardrobe and own garage gym with the black table. Use the second attached image only as a composition reference for the camera position, framing and the action; do not copy its person, eyeglasses, gray t-shirt, white kitchen, marble countertop, wall decorations or the caption text.",
  "identity_main": "The exact fictional AI character holistic.brandon: Black mixed-race American woman around thirty, athletic and toned, medium light-brown skin with light freckles across the nose and cheeks, dark brown eyes, defined eyebrows, full lips, hair in tight cornrows that turn into long loose braids falling over both shoulders, finished with small wooden and gold beads, a black floral blackwork tattoo sleeve on her right arm, a fine line tattoo on her left inner arm and a small fine-line floral tattoo below her left collarbone.",
  "wardrobe": "Plain white ribbed tank top with nothing printed on it, loose black training shorts, a thin gold chain with a small gold cross pendant and small stud earrings.",
  "scene": "Her own garage gym: a white-painted concrete block wall behind her, a red neon sign reading TRAIN PRAY REPEAT on the wall at the left, a whiteboard with handwritten black marker reading STAY READY. STAY DISCIPLINED. on the right, and a small American flag pinned above the whiteboard, discreet but clearly visible and in focus. In front of her stands a plain matte black table she uses as a counter.",
  "prop": "A clear drinking glass full of a pale creamy yellow apple drink, held up in her right hand at chest height, close to the lens in the lower foreground. The apple, the blender and the bowl are out of frame.",
  "posture": "Brandon stands behind the black table, leaning on its edge with both forearms, holding the glass up in her right hand, her left hand resting flat on the table.",
  "composition": "Straight-on medium shot: the phone lens is about 35 centimeters from the glass, which fills the lower left 22 percent of the frame, closer to the camera than her face; her face and shoulders fill the upper half of the frame and her forearms rest on the edge of the black table at the bottom. Nothing else is on the table. The background is reduced by framing, never by blur.",
  "camera": "phone at her eye level, standard 1x lens, straight-on, fixed",
  "lighting": "Neutral overcast daylight from a large window out of frame, soft even light on her face, hands and the table with no harsh shadows. The red neon glows on the wall but does not tint her skin.",
  "state": "Start frame: Brandon is caught mid-sentence, lips naturally parted, animated expression, looking straight into the lens, warm and knowing.",
  "realism": "Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday reality, background fully in focus, everything in sharp focus, no AI polish, no beauty smoothing.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no printed labels or lettering on the blender, bowl, glass or apple, no studio, no plastic-looking skin, no extra fingers, no third hand, no blur, no bokeh, no warm orange color cast, no yellow tint, no golden glow, no golden hour light, no sunset, no HDR, no cinematic lighting, no beauty smoothing, no visible phone, no second person, no eyeglasses, no gray t-shirt, no white kitchen cabinets, no marble countertop, no silver cross"
}
```

### K09 · T9, copo na mão, as três causas · anexar ÂNCORA + FRAME DO MODELO

```text
K09
{
  "format": "IMPORTANT: THIS IS IPHONE FOOTAGE. Vertical 9:16.",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "reference_use": "Use the first attached image only for Brandon's exact identity, wardrobe and own garage gym with the black table. Use the second attached image only as a composition reference for the camera position, framing and the action; do not copy its person, eyeglasses, gray t-shirt, white kitchen, marble countertop, wall decorations or the caption text.",
  "identity_main": "The exact fictional AI character holistic.brandon: Black mixed-race American woman around thirty, athletic and toned, medium light-brown skin with light freckles across the nose and cheeks, dark brown eyes, defined eyebrows, full lips, hair in tight cornrows that turn into long loose braids falling over both shoulders, finished with small wooden and gold beads, a black floral blackwork tattoo sleeve on her right arm, a fine line tattoo on her left inner arm and a small fine-line floral tattoo below her left collarbone.",
  "wardrobe": "Plain white ribbed tank top with nothing printed on it, loose black training shorts, a thin gold chain with a small gold cross pendant and small stud earrings.",
  "scene": "Her own garage gym: a white-painted concrete block wall behind her, a red neon sign reading TRAIN PRAY REPEAT on the wall at the left, a whiteboard with handwritten black marker reading STAY READY. STAY DISCIPLINED. on the right, and a small American flag pinned above the whiteboard, discreet but clearly visible and in focus. In front of her stands a plain matte black table she uses as a counter.",
  "prop": "A clear drinking glass full of a pale creamy yellow apple drink, held up in her right hand at chest height, close to the lens in the lower foreground. The apple, the blender and the bowl are out of frame.",
  "posture": "Brandon stands behind the black table, leaning on its edge with both forearms, holding the glass up in her right hand, her left hand counting on her fingers.",
  "composition": "Straight-on medium shot from a slight angle at her left: the phone lens is about 35 centimeters from the glass, which fills the lower left 22 percent of the frame, closer to the camera than her face; her face and shoulders fill the upper half of the frame and her forearms rest on the edge of the black table at the bottom. Nothing else is on the table. The background is reduced by framing, never by blur.",
  "camera": "phone at her eye level, slightly to her left, standard 1x lens, fixed",
  "lighting": "Neutral overcast daylight from a large window out of frame, soft even light on her face, hands and the table with no harsh shadows. The red neon glows on the wall but does not tint her skin.",
  "state": "Start frame: Brandon is caught mid-sentence, lips naturally parted, animated expression, looking straight into the lens, serious and focused.",
  "realism": "Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday reality, background fully in focus, everything in sharp focus, no AI polish, no beauty smoothing.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no printed labels or lettering on the blender, bowl, glass or apple, no studio, no plastic-looking skin, no extra fingers, no third hand, no blur, no bokeh, no warm orange color cast, no yellow tint, no golden glow, no golden hour light, no sunset, no HDR, no cinematic lighting, no beauty smoothing, no visible phone, no second person, no eyeglasses, no gray t-shirt, no white kitchen cabinets, no marble countertop, no silver cross"
}
```

### K10 · T10, copo na mão, álibi · anexar ÂNCORA + FRAME DO MODELO

```text
K10
{
  "format": "IMPORTANT: THIS IS IPHONE FOOTAGE. Vertical 9:16.",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "reference_use": "Use the first attached image only for Brandon's exact identity, wardrobe and own garage gym with the black table. Use the second attached image only as a composition reference for the camera position, framing and the action; do not copy its person, eyeglasses, gray t-shirt, white kitchen, marble countertop, wall decorations or the caption text.",
  "identity_main": "The exact fictional AI character holistic.brandon: Black mixed-race American woman around thirty, athletic and toned, medium light-brown skin with light freckles across the nose and cheeks, dark brown eyes, defined eyebrows, full lips, hair in tight cornrows that turn into long loose braids falling over both shoulders, finished with small wooden and gold beads, a black floral blackwork tattoo sleeve on her right arm, a fine line tattoo on her left inner arm and a small fine-line floral tattoo below her left collarbone.",
  "wardrobe": "Plain white ribbed tank top with nothing printed on it, loose black training shorts, a thin gold chain with a small gold cross pendant and small stud earrings.",
  "scene": "Her own garage gym: a white-painted concrete block wall behind her, a red neon sign reading TRAIN PRAY REPEAT on the wall at the left, a whiteboard with handwritten black marker reading STAY READY. STAY DISCIPLINED. on the right, and a small American flag pinned above the whiteboard, discreet but clearly visible and in focus. In front of her stands a plain matte black table she uses as a counter.",
  "prop": "A clear drinking glass full of a pale creamy yellow apple drink, held up in her right hand at chest height, close to the lens in the lower foreground. The apple, the blender and the bowl are out of frame.",
  "posture": "Brandon stands behind the black table, leaning on its edge with both forearms, holding the glass up in her right hand, her left hand open with the palm up.",
  "composition": "Straight-on medium shot: the phone lens is about 35 centimeters from the glass, which fills the lower left 22 percent of the frame, closer to the camera than her face; her face and shoulders fill the upper half of the frame and her forearms rest on the edge of the black table at the bottom. Nothing else is on the table. The background is reduced by framing, never by blur.",
  "camera": "phone at her eye level, standard 1x lens, straight-on, fixed",
  "lighting": "Neutral overcast daylight from a large window out of frame, soft even light on her face, hands and the table with no harsh shadows. The red neon glows on the wall but does not tint her skin.",
  "state": "Start frame: Brandon is caught mid-sentence, lips naturally parted, animated expression, looking straight into the lens, firm and reassuring.",
  "realism": "Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday reality, background fully in focus, everything in sharp focus, no AI polish, no beauty smoothing.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no printed labels or lettering on the blender, bowl, glass or apple, no studio, no plastic-looking skin, no extra fingers, no third hand, no blur, no bokeh, no warm orange color cast, no yellow tint, no golden glow, no golden hour light, no sunset, no HDR, no cinematic lighting, no beauty smoothing, no visible phone, no second person, no eyeglasses, no gray t-shirt, no white kitchen cabinets, no marble countertop, no silver cross"
}
```

### K11 · T11, copo na mão, o app · anexar ÂNCORA + FRAME DO MODELO

```text
K11
{
  "format": "IMPORTANT: THIS IS IPHONE FOOTAGE. Vertical 9:16.",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "reference_use": "Use the first attached image only for Brandon's exact identity, wardrobe and own garage gym with the black table. Use the second attached image only as a composition reference for the camera position, framing and the action; do not copy its person, eyeglasses, gray t-shirt, white kitchen, marble countertop, wall decorations or the caption text.",
  "identity_main": "The exact fictional AI character holistic.brandon: Black mixed-race American woman around thirty, athletic and toned, medium light-brown skin with light freckles across the nose and cheeks, dark brown eyes, defined eyebrows, full lips, hair in tight cornrows that turn into long loose braids falling over both shoulders, finished with small wooden and gold beads, a black floral blackwork tattoo sleeve on her right arm, a fine line tattoo on her left inner arm and a small fine-line floral tattoo below her left collarbone.",
  "wardrobe": "Plain white ribbed tank top with nothing printed on it, loose black training shorts, a thin gold chain with a small gold cross pendant and small stud earrings.",
  "scene": "Her own garage gym: a white-painted concrete block wall behind her, a red neon sign reading TRAIN PRAY REPEAT on the wall at the left, a whiteboard with handwritten black marker reading STAY READY. STAY DISCIPLINED. on the right, and a small American flag pinned above the whiteboard, discreet but clearly visible and in focus. In front of her stands a plain matte black table she uses as a counter.",
  "prop": "A clear drinking glass full of a pale creamy yellow apple drink, held up in her right hand at chest height, close to the lens in the lower foreground. The apple, the blender and the bowl are out of frame.",
  "posture": "Brandon stands behind the black table, leaning on its edge with both forearms, holding the glass up in her right hand, her left hand pointing loosely toward the lens.",
  "composition": "Straight-on medium shot from slightly above: the phone lens is about 35 centimeters from the glass, which fills the lower left 22 percent of the frame, closer to the camera than her face; her face and shoulders fill the upper half of the frame and her forearms rest on the edge of the black table at the bottom. Nothing else is on the table. The background is reduced by framing, never by blur.",
  "camera": "phone just above her eye level, tilted slightly down, standard 1x lens, fixed",
  "lighting": "Neutral overcast daylight from a large window out of frame, soft even light on her face, hands and the table with no harsh shadows. The red neon glows on the wall but does not tint her skin.",
  "state": "Start frame: Brandon is caught mid-sentence, lips naturally parted, animated expression, looking straight into the lens, direct and slightly indignant.",
  "realism": "Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday reality, background fully in focus, everything in sharp focus, no AI polish, no beauty smoothing.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no printed labels or lettering on the blender, bowl, glass or apple, no studio, no plastic-looking skin, no extra fingers, no third hand, no blur, no bokeh, no warm orange color cast, no yellow tint, no golden glow, no golden hour light, no sunset, no HDR, no cinematic lighting, no beauty smoothing, no visible phone, no second person, no eyeglasses, no gray t-shirt, no white kitchen cabinets, no marble countertop, no silver cross"
}
```

### K12 · T12, copo na mão, comment yes + follow · anexar ÂNCORA + FRAME DO MODELO

```text
K12
{
  "format": "IMPORTANT: THIS IS IPHONE FOOTAGE. Vertical 9:16.",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "reference_use": "Use the first attached image only for Brandon's exact identity, wardrobe and own garage gym with the black table. Use the second attached image only as a composition reference for the camera position, framing and the action; do not copy its person, eyeglasses, gray t-shirt, white kitchen, marble countertop, wall decorations or the caption text.",
  "identity_main": "The exact fictional AI character holistic.brandon: Black mixed-race American woman around thirty, athletic and toned, medium light-brown skin with light freckles across the nose and cheeks, dark brown eyes, defined eyebrows, full lips, hair in tight cornrows that turn into long loose braids falling over both shoulders, finished with small wooden and gold beads, a black floral blackwork tattoo sleeve on her right arm, a fine line tattoo on her left inner arm and a small fine-line floral tattoo below her left collarbone.",
  "wardrobe": "Plain white ribbed tank top with nothing printed on it, loose black training shorts, a thin gold chain with a small gold cross pendant and small stud earrings.",
  "scene": "Her own garage gym: a white-painted concrete block wall behind her, a red neon sign reading TRAIN PRAY REPEAT on the wall at the left, a whiteboard with handwritten black marker reading STAY READY. STAY DISCIPLINED. on the right, and a small American flag pinned above the whiteboard, discreet but clearly visible and in focus. In front of her stands a plain matte black table she uses as a counter.",
  "prop": "A clear drinking glass full of a pale creamy yellow apple drink, held up in her right hand at chest height, close to the lens in the lower foreground. The apple, the blender and the bowl are out of frame.",
  "posture": "Brandon stands behind the black table, leaning on its edge with both forearms, holding the glass up in her right hand, her left hand resting on the table.",
  "composition": "Straight-on medium shot, tighter: the phone lens is about 30 centimeters from the glass, which fills the lower left 25 percent of the frame, closer to the camera than her face; her face and shoulders fill the upper half of the frame and her forearms rest on the edge of the black table at the bottom. Nothing else is on the table. The background is reduced by framing, never by blur.",
  "camera": "phone at her eye level, standard 1x lens, straight-on, fixed",
  "lighting": "Neutral overcast daylight from a large window out of frame, soft even light on her face, hands and the table with no harsh shadows. The red neon glows on the wall but does not tint her skin.",
  "state": "Start frame: Brandon is caught mid-sentence, lips naturally parted, animated expression, looking straight into the lens, warm and inviting.",
  "realism": "Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday reality, background fully in focus, everything in sharp focus, no AI polish, no beauty smoothing.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no printed labels or lettering on the blender, bowl, glass or apple, no studio, no plastic-looking skin, no extra fingers, no third hand, no blur, no bokeh, no warm orange color cast, no yellow tint, no golden glow, no golden hour light, no sunset, no HDR, no cinematic lighting, no beauty smoothing, no visible phone, no second person, no eyeglasses, no gray t-shirt, no white kitchen cabinets, no marble countertop, no silver cross"
}
```

### K13 · T13, CTA, plano mais fechado · anexar ÂNCORA + FRAME DO MODELO

```text
K13
{
  "format": "IMPORTANT: THIS IS IPHONE FOOTAGE. Vertical 9:16.",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "reference_use": "Use the first attached image only for Brandon's exact identity, wardrobe and own garage gym with the black table. Use the second attached image only as a composition reference for the camera position, framing and the action; do not copy its person, eyeglasses, gray t-shirt, white kitchen, marble countertop, wall decorations or the caption text.",
  "identity_main": "The exact fictional AI character holistic.brandon: Black mixed-race American woman around thirty, athletic and toned, medium light-brown skin with light freckles across the nose and cheeks, dark brown eyes, defined eyebrows, full lips, hair in tight cornrows that turn into long loose braids falling over both shoulders, finished with small wooden and gold beads, a black floral blackwork tattoo sleeve on her right arm, a fine line tattoo on her left inner arm and a small fine-line floral tattoo below her left collarbone.",
  "wardrobe": "Plain white ribbed tank top with nothing printed on it, loose black training shorts, a thin gold chain with a small gold cross pendant and small stud earrings.",
  "scene": "Her own garage gym: a white-painted concrete block wall behind her, a red neon sign reading TRAIN PRAY REPEAT on the wall at the left, a whiteboard with handwritten black marker reading STAY READY. STAY DISCIPLINED. on the right, and a small American flag pinned above the whiteboard, discreet but clearly visible and in focus. In front of her stands a plain matte black table she uses as a counter.",
  "prop": "A clear drinking glass full of a pale creamy yellow apple drink, held up in her right hand at chest height, close to the lens in the lower foreground. The apple, the blender and the bowl are out of frame.",
  "posture": "Brandon stands behind the black table, leaning on its edge with both forearms, holding the glass up in her right hand, her left hand resting on the table.",
  "composition": "Straight-on medium shot, the tightest of the video: the phone lens is about 25 centimeters from the glass, which fills the lower left 28 percent of the frame, closer to the camera than her face; her face and shoulders fill the upper half of the frame and her forearms rest on the edge of the black table at the bottom. Nothing else is on the table. The background is reduced by framing, never by blur.",
  "camera": "phone at her eye level, standard 1x lens, straight-on, fixed",
  "lighting": "Neutral overcast daylight from a large window out of frame, soft even light on her face, hands and the table with no harsh shadows. The red neon glows on the wall but does not tint her skin.",
  "state": "Start frame: Brandon is caught mid-sentence, lips naturally parted, animated expression, looking straight into the lens, intense and certain.",
  "realism": "Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday reality, background fully in focus, everything in sharp focus, no AI polish, no beauty smoothing.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no printed labels or lettering on the blender, bowl, glass or apple, no studio, no plastic-looking skin, no extra fingers, no third hand, no blur, no bokeh, no warm orange color cast, no yellow tint, no golden glow, no golden hour light, no sunset, no HDR, no cinematic lighting, no beauty smoothing, no visible phone, no second person, no eyeglasses, no gray t-shirt, no white kitchen cabinets, no marble countertop, no silver cross"
}
```

## 3. PROMPTS DE VÍDEO (um bloco por V)

### V01 · T1 · frame inicial = a imagem que você deixou no K01

```text
V01
a avatar Brandon, mulher, fala em inglês com sotaque americano de uma mulher negra americana, voz feminina clara e firme de uma mulher de uns trinta anos, entonação animada e intrigante, com espanto no fim, como quem revela um segredo, voz autêntica, como se exigisse ser ouvida, a seguinte frase: "Put garlic in an apple and watch what happens. Pharmacies hate this because half their customers would disappear overnight."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Brandon empurra o dente de alho para dentro do buraco da maçã; por volta de 2 segundos uma espuma branca começa a subir do buraco e cresce em bolhas grandes, cobrindo o topo da maçã e escorrendo pelos lados até o fim do clipe; ela olha da maçã para a câmera, espantada.

câmera: fixa, levemente de cima, colada na maçã, leve handheld natural

som ambiente: box de treino em casa, tranquilo, espuma chiando baixinho, sem música
```

### V02 · T2 · frame inicial = a imagem que você deixou no K02

```text
V02
a avatar Brandon, mulher, fala em inglês com sotaque americano de uma mulher negra americana, voz feminina clara e firme de uma mulher de uns trinta anos, entonação animada e didática, rápida, voz autêntica, como se exigisse ser ouvida, a seguinte frase: "Blend one apple with the skin on,"

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Brandon vira a tigela e os pedaços de maçã caem dentro da jarra do liquidificador. Ela diz a frase em ritmo natural logo no começo e a ação continua em silêncio até o fim.

câmera: leve handheld natural

som ambiente: box de treino em casa, tranquilo, pedaços de maçã batendo no vidro, sem música
```

### V03 · T3 · frame inicial = a imagem que você deixou no K03

```text
V03
a avatar Brandon, mulher, fala em inglês com sotaque americano de uma mulher negra americana, voz feminina clara e firme de uma mulher de uns trinta anos, entonação animada e didática, rápida, voz autêntica, como se exigisse ser ouvida, a seguinte frase: "one small garlic clove, the juice of half a lemon,"

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Brandon solta o dente de alho dentro da jarra e espreme o meio limão por cima. Ela diz a frase em ritmo natural logo no começo e a ação continua em silêncio até o fim.

câmera: leve handheld natural

som ambiente: box de treino em casa, tranquilo, limão sendo espremido, sem música
```

### V04 · T4 · frame inicial = a imagem que você deixou no K04

```text
V04
a avatar Brandon, mulher, fala em inglês com sotaque americano de uma mulher negra americana, voz feminina clara e firme de uma mulher de uns trinta anos, entonação animada e didática, rápida, voz autêntica, como se exigisse ser ouvida, a seguinte frase: "and one glass of water."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Brandon despeja o copo de água dentro da jarra. Ela diz a frase em ritmo natural logo no começo e a ação continua em silêncio até o fim.

câmera: leve handheld natural

som ambiente: box de treino em casa, tranquilo, água caindo na jarra, sem música
```

### V05 · T5 · frame inicial = a imagem que você deixou no K05

```text
V05
a avatar Brandon, mulher, fala em inglês com sotaque americano de uma mulher negra americana, voz feminina clara e firme de uma mulher de uns trinta anos, entonação convicta e entusiasmada, voz autêntica, como se exigisse ser ouvida, a seguinte frase: "This mixture goes straight into your circulation and starts working where your blood moves more slowly."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Brandon despeja o suco batido, grosso e amarelo-claro, da jarra dentro do copo, olhando para a câmera.

câmera: leve handheld natural

som ambiente: box de treino em casa, tranquilo, suco grosso caindo no copo, sem música
```

### V06 · T6 · frame inicial = a imagem que você deixou no K06

```text
V06
a avatar Brandon, mulher, fala em inglês com sotaque americano de uma mulher negra americana, voz feminina clara e firme de uma mulher de uns trinta anos, entonação convicta e animada, voz autêntica, como se exigisse ser ouvida, a seguinte frase: "It helps move the fluid that pools in your ankles by night, takes the heaviness out of your legs, and lets your blood flow more easily."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Brandon fala para a câmera segurando o copo do suco, com pequenos gestos da outra mão.

câmera: fixa

som ambiente: box de treino em casa, tranquilo, sem música
```

### V07 · T7 · frame inicial = a imagem que você deixou no K07

```text
V07
a avatar Brandon, mulher, fala em inglês com sotaque americano de uma mulher negra americana, voz feminina clara e firme de uma mulher de uns trinta anos, entonação intrigante, baixando um pouco a voz no fim, voz autêntica, como se exigisse ser ouvida, a seguinte frase: "If you want this drink to actually work, there is a fifth ingredient, and it is the one that decides everything. It never goes in the blender."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Brandon levanta o dedo indicador da mão livre e fala para a câmera, segurando o copo.

câmera: fixa

som ambiente: box de treino em casa, tranquilo, sem música
```

### V08 · T8 · frame inicial = a imagem que você deixou no K08

```text
V08
a avatar Brandon, mulher, fala em inglês com sotaque americano de uma mulher negra americana, voz feminina clara e firme de uma mulher de uns trinta anos, entonação calorosa, imitando a cliente na frase citada, voz autêntica, como se exigisse ser ouvida, a seguinte frase: "Every woman over forty I train says the same sentence to me: my legs feel like concrete by dinner. This drink moves what already pooled there."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Brandon fala para a câmera segurando o copo, com a mão livre apoiada na mesa.

câmera: fixa

som ambiente: box de treino em casa, tranquilo, sem música
```

### V09 · T9 · frame inicial = a imagem que você deixou no K09

```text
V09
a avatar Brandon, mulher, fala em inglês com sotaque americano de uma mulher negra americana, voz feminina clara e firme de uma mulher de uns trinta anos, entonação séria e firme, voz autêntica, como se exigisse ser ouvida, a seguinte frase: "But something keeps sending it back every single night, and after forty that something is one of three things: your hormones, your metabolism, or your gut."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Brandon conta nos dedos da mão livre enquanto fala, segurando o copo.

câmera: fixa

som ambiente: box de treino em casa, tranquilo, sem música
```

### V10 · T10 · frame inicial = a imagem que você deixou no K10

```text
V10
a avatar Brandon, mulher, fala em inglês com sotaque americano de uma mulher negra americana, voz feminina clara e firme de uma mulher de uns trinta anos, entonação firme e acolhedora, com ênfase em You didn't, voz autêntica, como se exigisse ser ouvida, a seguinte frase: "Guess the wrong one and you drink this for a month, feel nothing, and think you failed. You didn't. You got a prescription without a diagnosis."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Brandon abre a mão livre com a palma para cima e fala para a câmera, segurando o copo.

câmera: fixa

som ambiente: box de treino em casa, tranquilo, sem música
```

### V11 · T11 · frame inicial = a imagem que você deixou no K11

```text
V11
a avatar Brandon, mulher, fala em inglês com sotaque americano de uma mulher negra americana, voz feminina clara e firme de uma mulher de uns trinta anos, entonação direta, levemente indignada, voz autêntica, como se exigisse ser ouvida, a seguinte frase: "And every free app on your phone writes that same prescription, the same numbers for every woman, without ever asking what is holding yours."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Brandon aponta de leve para a câmera com a mão livre e fala, segurando o copo.

câmera: fixa

som ambiente: box de treino em casa, tranquilo, sem música
```

### V12 · T12 · frame inicial = a imagem que você deixou no K12

```text
V12
a avatar Brandon, mulher, fala em inglês com sotaque americano de uma mulher negra americana, voz feminina clara e firme de uma mulher de uns trinta anos, entonação calorosa e convidativa, com ênfase no yes, voz autêntica, como se exigisse ser ouvida, a seguinte frase: "That is your fifth ingredient: knowing which of the three is yours. Comment yes if that concrete feeling sounds like you, and follow me so you don't lose this."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Brandon fala direto com quem assiste, sorrindo no yes, segurando o copo.

câmera: fixa

som ambiente: box de treino em casa, tranquilo, sem música
```

### V13 · T13 · frame inicial = a imagem que você deixou no K13

```text
V13
a avatar Brandon, mulher, fala em inglês com sotaque americano de uma mulher negra americana, voz feminina clara e firme de uma mulher de uns trinta anos, entonação intensa e segura, com urgência no fim, voz autêntica, como se exigisse ser ouvida, a seguinte frase: "Only your personalized FityWell Metabolic Reset plan tells you which one is weighing your legs down. Tap the link in the pinned comment before it starts again tonight."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Brandon se inclina um pouco para a câmera e fala, séria e segura, segurando o copo.

câmera: fixa, leve push-in

som ambiente: box de treino em casa, tranquilo, sem música
```

## 4. Montagem no CapCut

1. Clipes numerados na ordem: V01 a V13.
2. Cortar os seis primeiros no tempo da cena do modelo: V01 0,0 a 7,5 s; V02 7,5 a 9,5 s; V03 9,5 a 12,7 s; V04 12,7 a 14,1 s; V05 14,1 a 21,0 s; V06 21,0 a 27,8 s. Do V07 ao V13, cortar logo depois da última palavra de cada um.
3. Zero tempo morto: todo clipe começa já falando. Isolate Voice / Keep Vocal no áudio.
4. Nos V02, V03 e V04 (cenas curtas) a fala vem no começo; cortar logo depois da última palavra, mantendo a ação até o tempo da cena do modelo.
5. Legenda branca serifada, duas a três palavras por vez, com a palavra-chave maior, no meio-baixo do quadro, igual ao modelo. No V12, `yes` grande e isolado na tela.
6. Sem Voice Changer: a voz vem do prompt de cada V.
7. Música só depois do gancho (a partir do V02), nunca no pré-gancho, entre -19 e -20 dB, fora da biblioteca do TikTok.
8. Rótulo pequeno `AI-generated` num canto do vídeo.
9. Ao publicar, fixar o comentário com o link do plano personalizado FityWell Metabolic Reset (o V13 manda tocar nele).

## 5. Transcrição final por take

| Take | English | Português |
|---|---|---|
| T1 | Put garlic in an apple and watch what happens. Pharmacies hate this because half their customers would disappear overnight. | Coloque alho dentro de uma maçã e veja o que acontece. As farmácias odeiam isso porque metade dos clientes delas sumiria da noite pro dia. |
| T2 | Blend one apple with the skin on, | Bata uma maçã com casca, |
| T3 | one small garlic clove, the juice of half a lemon, | um dente de alho pequeno, o suco de meio limão, |
| T4 | and one glass of water. | e um copo de água. |
| T5 | This mixture goes straight into your circulation and starts working where your blood moves more slowly. | Essa mistura vai direto pra sua circulação e começa a agir onde o seu sangue anda mais devagar. |
| T6 | It helps move the fluid that pools in your ankles by night, takes the heaviness out of your legs, and lets your blood flow more easily. | Ela ajuda a mover o líquido que se acumula nos seus tornozelos à noite, tira o peso das suas pernas e deixa o seu sangue correr com mais facilidade. |
| T7 | If you want this drink to actually work, there is a fifth ingredient, and it is the one that decides everything. It never goes in the blender. | Se você quer que essa bebida funcione de verdade, existe um quinto ingrediente, e é ele que decide tudo. Ele nunca vai no liquidificador. |
| T8 | Every woman over forty I train says the same sentence to me: my legs feel like concrete by dinner. This drink moves what already pooled there. | Toda mulher acima dos quarenta que eu treino me diz a mesma frase: na hora do jantar minhas pernas parecem de concreto. Essa bebida move o que já se acumulou ali. |
| T9 | But something keeps sending it back every single night, and after forty that something is one of three things: your hormones, your metabolism, or your gut. | Mas alguma coisa manda tudo de volta toda santa noite, e depois dos quarenta essa coisa é uma de três: seus hormônios, seu metabolismo ou seu intestino. |
| T10 | Guess the wrong one and you drink this for a month, feel nothing, and think you failed. You didn't. You got a prescription without a diagnosis. | Chute a errada e você toma isso por um mês, não sente nada e acha que falhou. Você não falhou. Você recebeu uma receita sem diagnóstico. |
| T11 | And every free app on your phone writes that same prescription, the same numbers for every woman, without ever asking what is holding yours. | E todo app de graça do seu celular escreve essa mesma receita, os mesmos números pra toda mulher, sem nunca perguntar o que está segurando as suas. |
| T12 | That is your fifth ingredient: knowing which of the three is yours. Comment yes if that concrete feeling sounds like you, and follow me so you don't lose this. | Esse é o seu quinto ingrediente: saber qual das três é a sua. Comente yes se essa sensação de concreto parece com você, e me siga pra não perder isso. |
| T13 | Only your personalized FityWell Metabolic Reset plan tells you which one is weighing your legs down. Tap the link in the pinned comment before it starts again tonight. | Só o seu plano personalizado Metabolic Reset da FityWell te diz qual delas está pesando nas suas pernas. Toque no link do comentário fixado antes que comece de novo hoje à noite. |

## 6. Roteiro final em inglês

1. Put garlic in an apple and watch what happens. Pharmacies hate this because half their customers would disappear overnight.
2. Blend one apple with the skin on,
3. one small garlic clove, the juice of half a lemon,
4. and one glass of water.
5. This mixture goes straight into your circulation and starts working where your blood moves more slowly.
6. It helps move the fluid that pools in your ankles by night, takes the heaviness out of your legs, and lets your blood flow more easily.
7. If you want this drink to actually work, there is a fifth ingredient, and it is the one that decides everything. It never goes in the blender.
8. Every woman over forty I train says the same sentence to me: my legs feel like concrete by dinner. This drink moves what already pooled there.
9. But something keeps sending it back every single night, and after forty that something is one of three things: your hormones, your metabolism, or your gut.
10. Guess the wrong one and you drink this for a month, feel nothing, and think you failed. You didn't. You got a prescription without a diagnosis.
11. And every free app on your phone writes that same prescription, the same numbers for every woman, without ever asking what is holding yours.
12. That is your fifth ingredient: knowing which of the three is yours. Comment yes if that concrete feeling sounds like you, and follow me so you don't lose this.
13. Only your personalized FityWell Metabolic Reset plan tells you which one is weighing your legs down. Tap the link in the pinned comment before it starts again tonight.

Put garlic in an apple and watch what happens. Pharmacies hate this because half their customers would disappear overnight. Blend one apple with the skin on, one small garlic clove, the juice of half a lemon, and one glass of water. This mixture goes straight into your circulation and starts working where your blood moves more slowly. It helps move the fluid that pools in your ankles by night, takes the heaviness out of your legs, and lets your blood flow more easily. If you want this drink to actually work, there is a fifth ingredient, and it is the one that decides everything. It never goes in the blender. Every woman over forty I train says the same sentence to me: my legs feel like concrete by dinner. This drink moves what already pooled there. But something keeps sending it back every single night, and after forty that something is one of three things: your hormones, your metabolism, or your gut. Guess the wrong one and you drink this for a month, feel nothing, and think you failed. You didn't. You got a prescription without a diagnosis. And every free app on your phone writes that same prescription, the same numbers for every woman, without ever asking what is holding yours. That is your fifth ingredient: knowing which of the three is yours. Comment yes if that concrete feeling sounds like you, and follow me so you don't lose this. Only your personalized FityWell Metabolic Reset plan tells you which one is weighing your legs down. Tap the link in the pinned comment before it starts again tonight.
