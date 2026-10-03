# ENTREGA | holistic.brandon | Natural Rems Sea Moss | Joelho que espuma

Produção `brandon_seamoss_joelho` · Ângulo 1 · VENDA · vídeo modelo de pessoa real · rodada de VALIDAÇÃO · perfil CLÁSSICO

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

Checklist de envio: 34/34 aprovados (N/A: A1, A2, A7 fiéis ao modelo; C4 a C7 sem selfie, frase repetida, cena atuada ou motion control; E4 copy literal do modelo orgânico, aprovada no roteiro)

Ficha: 14/14 K conferidos contra o frame do modelo, placar 14/14 cada (`FICHA_FRAMES.md`, GATE_VISUAL Parte 6)

## Anexos

- **Âncora holistic.brandon:** `producao/_ancoras/holistic_brandon_ancora.jpg` em TODOS os K.
- **Em cada K**, anexar também o frame do modelo daquele passo (`producao/brandon_seamoss_joelho/input/frames_modelo/Kxx_modelo.png`), só como referência de composição.
- **K12, K13 e K14:** anexar também a foto do pote `producao/_ancoras/natural_rems_seamoss_produto.jpg` (só o pote da frente vale).
- K01 a K14 casam com V01 a V14 pelo número. Todos os V têm fala.

| Código | Take | Anexos além da âncora |
|---|---|---|
| K01 / V01 | T1, gancho, água oxigenada no joelho colado na lente | `input/frames_modelo/K01_modelo.png` |
| K02 / V02 | T2, receita, frasco na tigela | `input/frames_modelo/K02_modelo.png` |
| K03 / V03 | T3, receita, duas canecas e bicarbonato | `input/frames_modelo/K03_modelo.png` |
| K04 / V04 | T4, protocolo, o pano entregue pela direita | `input/frames_modelo/K04_modelo.png` |
| K05 / V05 | T5, reveal, o pano saindo do joelho | `input/frames_modelo/K05_modelo.png` |
| K06 / V06 | T6, os dois modelos de joelho | `input/frames_modelo/K06_modelo.png` |
| K07 / V07 | T7, mesa, dor | `input/frames_modelo/K07_modelo.png` |
| K08 / V08 | T8, mesa, objeção | `input/frames_modelo/K08_modelo.png` |
| K09 / V09 | T9, mesa, virada | `input/frames_modelo/K09_modelo.png` |
| K10 / V10 | T10, mesa, mecanismo | `input/frames_modelo/K10_modelo.png` |
| K11 / V11 | T11, mesa, solução | `input/frames_modelo/K11_modelo.png` |
| K12 / V12 | T12, pote sobe no nome | `input/frames_modelo/K12_modelo.png` + `producao/_ancoras/natural_rems_seamoss_produto.jpg` |
| K13 / V13 | T13, pote, ingredientes | `input/frames_modelo/K13_modelo.png` + `producao/_ancoras/natural_rems_seamoss_produto.jpg` |
| K14 / V14 | T14, CTA, pote parado e legível | `input/frames_modelo/K14_modelo.png` + `producao/_ancoras/natural_rems_seamoss_produto.jpg` |

## 2. PROMPTS DE IMAGEM (um bloco por K)

### K01 · T1, gancho, água oxigenada no joelho colado na lente · anexar ÂNCORA HOLISTIC BRANDON + FRAME DO MODELO

```text
K01
{
  "format": "IMPORTANT: THIS IS IPHONE FOOTAGE. Vertical 9:16.",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "reference_use": "Use the first attached image only for Brandon's exact identity, wardrobe and her own garage gym. Use the second attached image only as a composition reference for the camera position, framing and the action; do not copy its man, glasses, gray t-shirt, kitchen, marble counter, cartoon magnet or the caption text.",
  "identity_main": "The exact fictional AI character holistic.brandon: Black mixed-race American woman around thirty, athletic and toned, medium light-brown skin with light freckles across the nose and cheeks, dark brown eyes, defined eyebrows, full lips, hair in tight cornrows that turn into long loose braids falling over both shoulders, finished with small wooden and gold beads, a black floral blackwork tattoo sleeve on her right arm, a small line tattoo on her left upper arm and small fine-line tattoos on her chest near the collarbones. She reads as an ordinary anonymous American fitness coach, not resembling anyone famous.",
  "wardrobe": "Plain white ribbed tank top with nothing printed or written on it, loose black training shorts ending at mid-thigh, a thin gold chain with a small gold cross pendant and small stud earrings.",
  "scene": "Her own garage gym, the same room as the reference: a white-painted concrete block wall and a dark wooden slat ceiling, a red neon sign reading TRAIN PRAY REPEAT on the wall at the left, a whiteboard with handwritten black marker reading STAY READY. STAY DISCIPLINED. on the right, and a small American flag pinned above the whiteboard, discreet but clearly visible and in focus. The background is reduced by framing, never by blur.",
  "prop": "Above her knee, a second person's slim bare forearm and hand in a plain navy t-shirt sleeve, cut off by the right edge of the frame, tilts a plain dark brown plastic bottle of hydrogen peroxide, the cap off, with a blank white label and nothing written on it. Her bare right knee, bent and raised toward the camera, smooth skin, fills the lower 40 percent of the frame at the lower left, very close to the lens, larger than her head and closer to the camera than her face, nothing else competing with it.",
  "posture": "Brandon sits on a black padded gym bench, leaning slightly forward, her right foot up on the edge of the bench so her right knee rises toward the lens, her left hand resting on her left thigh.",
  "composition": "Close straight-on shot: the phone lens is about 30 centimeters from her knee; the knee fills the lower 40 percent of the frame, her face and shoulders fill the upper part. The background is reduced by framing, never by blur.",
  "camera": "phone held at chest height about 30 centimeters in front of her knee, standard 1x lens tilted slightly down",
  "lighting": "Neutral overcast daylight from a large window out of frame, soft even light on her face, hands and knees with no harsh shadows. The red neon glows on the wall but does not tint her skin.",
  "state": "Start frame: the first thin stream of clear liquid is just leaving the bottle toward the top of the knee; the skin is still clean and dry, no foam yet. Brandon is caught mid-sentence, lips naturally parted, animated expression, looking straight into the lens.",
  "realism": "Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday reality, background fully in focus, everything in sharp focus, no AI polish, no beauty smoothing.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no studio, no plastic-looking skin, no extra fingers, no third hand, no blur, no bokeh, no warm orange color cast, no yellow tint, no golden glow, no golden hour light, no sunset, no HDR, no cinematic lighting, no de-aging, no beauty smoothing, no visible phone, no glasses, no kitchen, no white marble counter, no silver cross, no white coat, no second face in frame, no full second body, no foam yet, no readable label on the bottle"
}
```

### K02 · T2, receita, frasco na tigela · anexar ÂNCORA HOLISTIC BRANDON + FRAME DO MODELO

```text
K02
{
  "format": "IMPORTANT: THIS IS IPHONE FOOTAGE. Vertical 9:16.",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "reference_use": "Use the first attached image only for Brandon's exact identity, wardrobe and her own garage gym. Use the second attached image only as a composition reference for the camera position, framing and the action; do not copy its man, glasses, gray t-shirt, kitchen, marble counter, cartoon magnet or the caption text.",
  "identity_main": "The exact fictional AI character holistic.brandon: Black mixed-race American woman around thirty, athletic and toned, medium light-brown skin with light freckles across the nose and cheeks, dark brown eyes, defined eyebrows, full lips, hair in tight cornrows that turn into long loose braids falling over both shoulders, finished with small wooden and gold beads, a black floral blackwork tattoo sleeve on her right arm, a small line tattoo on her left upper arm and small fine-line tattoos on her chest near the collarbones. She reads as an ordinary anonymous American fitness coach, not resembling anyone famous.",
  "wardrobe": "Plain white ribbed tank top with nothing printed or written on it, loose black training shorts ending at mid-thigh, a thin gold chain with a small gold cross pendant and small stud earrings.",
  "scene": "Her own garage gym, the same room as the reference: a white-painted concrete block wall and a dark wooden slat ceiling, a red neon sign reading TRAIN PRAY REPEAT on the wall at the left, a whiteboard with handwritten black marker reading STAY READY. STAY DISCIPLINED. on the right, and a small American flag pinned above the whiteboard, discreet but clearly visible and in focus. The background is reduced by framing, never by blur.",
  "prop": "A large plain white ceramic mixing bowl, empty, in the center of the black table in front of her, very close to the lens; two plain white ceramic mugs full of warm water at its left; a small clear glass dish of white baking soda with a metal teaspoon at its right. Her right hand tilts a plain dark brown plastic bottle of hydrogen peroxide, the cap off, with a blank white label and nothing written on it into the bowl from the right side.",
  "posture": "Brandon stands behind the black table in front of her, leaning forward over it, her forearms close to the table edge. Her left hand rests on the table next to the mugs.",
  "composition": "Close shot from just above the table: the phone lens is about 40 centimeters from the bowl, which with the mugs and the glass dish fills the lower 40 percent of the frame, closer to the camera than her face; her head and torso fill the upper part. Nothing else is on the table. The background is reduced by framing, never by blur.",
  "camera": "phone held just above the table edge at chest height, standard 1x lens tilted slightly down",
  "lighting": "Neutral overcast daylight from a large window out of frame, soft even light on her face, hands and knees with no harsh shadows. The red neon glows on the wall but does not tint her skin.",
  "state": "Start frame: clear liquid is starting to pour from the bottle into the empty bowl. Brandon is caught mid-sentence, lips naturally parted, animated expression, looking straight into the lens.",
  "realism": "Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday reality, background fully in focus, everything in sharp focus, no AI polish, no beauty smoothing.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no studio, no plastic-looking skin, no extra fingers, no third hand, no blur, no bokeh, no warm orange color cast, no yellow tint, no golden glow, no golden hour light, no sunset, no HDR, no cinematic lighting, no de-aging, no beauty smoothing, no visible phone, no glasses, no kitchen, no white marble counter, no silver cross, no white coat, no second person, no readable lettering on the bowl, mugs, glass dish or spoon, no readable label on the bottle"
}
```

### K03 · T3, receita, duas canecas e bicarbonato · anexar ÂNCORA HOLISTIC BRANDON + FRAME DO MODELO

```text
K03
{
  "format": "IMPORTANT: THIS IS IPHONE FOOTAGE. Vertical 9:16.",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "reference_use": "Use the first attached image only for Brandon's exact identity, wardrobe and her own garage gym. Use the second attached image only as a composition reference for the camera position, framing and the action; do not copy its man, glasses, gray t-shirt, kitchen, marble counter, cartoon magnet or the caption text.",
  "identity_main": "The exact fictional AI character holistic.brandon: Black mixed-race American woman around thirty, athletic and toned, medium light-brown skin with light freckles across the nose and cheeks, dark brown eyes, defined eyebrows, full lips, hair in tight cornrows that turn into long loose braids falling over both shoulders, finished with small wooden and gold beads, a black floral blackwork tattoo sleeve on her right arm, a small line tattoo on her left upper arm and small fine-line tattoos on her chest near the collarbones. She reads as an ordinary anonymous American fitness coach, not resembling anyone famous.",
  "wardrobe": "Plain white ribbed tank top with nothing printed or written on it, loose black training shorts ending at mid-thigh, a thin gold chain with a small gold cross pendant and small stud earrings.",
  "scene": "Her own garage gym, the same room as the reference: a white-painted concrete block wall and a dark wooden slat ceiling, a red neon sign reading TRAIN PRAY REPEAT on the wall at the left, a whiteboard with handwritten black marker reading STAY READY. STAY DISCIPLINED. on the right, and a small American flag pinned above the whiteboard, discreet but clearly visible and in focus. The background is reduced by framing, never by blur.",
  "prop": "A large plain white ceramic mixing bowl in the center of the black table in front of her, very close to the lens, with a little clear liquid in it; a small clear glass dish of white baking soda with a metal teaspoon at its right. She holds one plain white ceramic mug full of warm water in each hand, tilted above the bowl.",
  "posture": "Brandon stands behind the black table in front of her, leaning forward over it, her forearms close to the table edge.",
  "composition": "Close shot from just above the table: the phone lens is about 40 centimeters from the bowl, which with the mugs and the glass dish fills the lower 40 percent of the frame, closer to the camera than her face; her head and torso fill the upper part. Nothing else is on the table. The background is reduced by framing, never by blur.",
  "camera": "phone held just above the table edge at chest height, standard 1x lens tilted slightly down",
  "lighting": "Neutral overcast daylight from a large window out of frame, soft even light on her face, hands and knees with no harsh shadows. The red neon glows on the wall but does not tint her skin.",
  "state": "Start frame: the water is just starting to pour from both mugs into the bowl. Brandon is caught mid-sentence, lips naturally parted, animated expression, looking straight into the lens.",
  "realism": "Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday reality, background fully in focus, everything in sharp focus, no AI polish, no beauty smoothing.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no studio, no plastic-looking skin, no extra fingers, no third hand, no blur, no bokeh, no warm orange color cast, no yellow tint, no golden glow, no golden hour light, no sunset, no HDR, no cinematic lighting, no de-aging, no beauty smoothing, no visible phone, no glasses, no kitchen, no white marble counter, no silver cross, no white coat, no second person, no readable lettering on the bowl, mugs, glass dish or spoon, no bottle in frame"
}
```

### K04 · T4, protocolo, o pano entregue pela direita · anexar ÂNCORA HOLISTIC BRANDON + FRAME DO MODELO

```text
K04
{
  "format": "IMPORTANT: THIS IS IPHONE FOOTAGE. Vertical 9:16.",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "reference_use": "Use the first attached image only for Brandon's exact identity, wardrobe and her own garage gym. Use the second attached image only as a composition reference for the camera position, framing and the action; do not copy its man, glasses, gray t-shirt, kitchen, marble counter, cartoon magnet or the caption text.",
  "identity_main": "The exact fictional AI character holistic.brandon: Black mixed-race American woman around thirty, athletic and toned, medium light-brown skin with light freckles across the nose and cheeks, dark brown eyes, defined eyebrows, full lips, hair in tight cornrows that turn into long loose braids falling over both shoulders, finished with small wooden and gold beads, a black floral blackwork tattoo sleeve on her right arm, a small line tattoo on her left upper arm and small fine-line tattoos on her chest near the collarbones. She reads as an ordinary anonymous American fitness coach, not resembling anyone famous.",
  "wardrobe": "Plain white ribbed tank top with nothing printed or written on it, loose black training shorts ending at mid-thigh, a thin gold chain with a small gold cross pendant and small stud earrings.",
  "scene": "Her own garage gym, the same room as the reference: a white-painted concrete block wall and a dark wooden slat ceiling, a red neon sign reading TRAIN PRAY REPEAT on the wall at the left, a whiteboard with handwritten black marker reading STAY READY. STAY DISCIPLINED. on the right, and a small American flag pinned above the whiteboard, discreet but clearly visible and in focus. The background is reduced by framing, never by blur.",
  "prop": "A second person's slim bare forearm and hand in a plain navy t-shirt sleeve, cut off by the right edge of the frame, holds out a folded white cotton cloth toward her; at the lower right a large plain white ceramic mixing bowl full of clear liquid is held up by the second person's other hand. Her bare right knee, bent and raised toward the camera, smooth skin, fills the lower 40 percent of the frame at the lower left, very close to the lens, larger than her head and closer to the camera than her face, nothing else competing with it.",
  "posture": "Brandon sits on a black padded gym bench, leaning slightly forward, her right foot up on the edge of the bench so her right knee rises toward the lens, her left hand reaching for the cloth.",
  "composition": "Close straight-on shot: the phone lens is about 30 centimeters from her knee; the knee fills the lower 40 percent of the frame, her face and shoulders fill the upper part. The background is reduced by framing, never by blur.",
  "camera": "phone held at chest height about 30 centimeters in front of her knee, standard 1x lens tilted slightly down",
  "lighting": "Neutral overcast daylight from a large window out of frame, soft even light on her face, hands and knees with no harsh shadows. The red neon glows on the wall but does not tint her skin.",
  "state": "Start frame: the cloth is dry and folded, just reaching her hand. Brandon is caught mid-sentence, lips naturally parted, animated expression, looking straight into the lens.",
  "realism": "Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday reality, background fully in focus, everything in sharp focus, no AI polish, no beauty smoothing.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no studio, no plastic-looking skin, no extra fingers, no third hand, no blur, no bokeh, no warm orange color cast, no yellow tint, no golden glow, no golden hour light, no sunset, no HDR, no cinematic lighting, no de-aging, no beauty smoothing, no visible phone, no glasses, no kitchen, no white marble counter, no silver cross, no white coat, no second face in frame, no full second body, no foam on the knee"
}
```

### K05 · T5, reveal, o pano saindo do joelho · anexar ÂNCORA HOLISTIC BRANDON + FRAME DO MODELO

```text
K05
{
  "format": "IMPORTANT: THIS IS IPHONE FOOTAGE. Vertical 9:16.",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "reference_use": "Use the first attached image only for Brandon's exact identity, wardrobe and her own garage gym. Use the second attached image only as a composition reference for the camera position, framing and the action; do not copy its man, glasses, gray t-shirt, kitchen, marble counter, cartoon magnet or the caption text.",
  "identity_main": "The exact fictional AI character holistic.brandon: Black mixed-race American woman around thirty, athletic and toned, medium light-brown skin with light freckles across the nose and cheeks, dark brown eyes, defined eyebrows, full lips, hair in tight cornrows that turn into long loose braids falling over both shoulders, finished with small wooden and gold beads, a black floral blackwork tattoo sleeve on her right arm, a small line tattoo on her left upper arm and small fine-line tattoos on her chest near the collarbones. She reads as an ordinary anonymous American fitness coach, not resembling anyone famous.",
  "wardrobe": "Plain white ribbed tank top with nothing printed or written on it, loose black training shorts ending at mid-thigh, a thin gold chain with a small gold cross pendant and small stud earrings.",
  "scene": "Her own garage gym, the same room as the reference: a white-painted concrete block wall and a dark wooden slat ceiling, a red neon sign reading TRAIN PRAY REPEAT on the wall at the left, a whiteboard with handwritten black marker reading STAY READY. STAY DISCIPLINED. on the right, and a small American flag pinned above the whiteboard, discreet but clearly visible and in focus. The background is reduced by framing, never by blur.",
  "prop": "A wet white cotton cloth lies spread over her bare right knee, covering it completely; the two hands of a second person, slim bare forearms in plain navy t-shirt sleeves cut off by the right edge of the frame, hold its two upper corners, ready to lift it. Her bare right knee, bent and raised toward the camera, under the cloth, fills the lower 40 percent of the frame at the lower left, very close to the lens, larger than her head and closer to the camera than her face, nothing else competing with it.",
  "posture": "Brandon sits on a black padded gym bench, leaning slightly forward, her right foot up on the edge of the bench so her right knee rises toward the lens, her right index finger raised, ready to point at the knee.",
  "composition": "Close straight-on shot: the phone lens is about 30 centimeters from her knee; the knee fills the lower 40 percent of the frame, her face and shoulders fill the upper part. The background is reduced by framing, never by blur.",
  "camera": "phone held at chest height about 30 centimeters in front of her knee, standard 1x lens tilted slightly down",
  "lighting": "Neutral overcast daylight from a large window out of frame, soft even light on her face, hands and knees with no harsh shadows. The red neon glows on the wall but does not tint her skin.",
  "state": "Start frame: the cloth still covers the knee completely, nothing visible under it yet. Brandon is caught mid-sentence, lips naturally parted, animated expression, looking straight into the lens.",
  "realism": "Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday reality, background fully in focus, everything in sharp focus, no AI polish, no beauty smoothing.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no studio, no plastic-looking skin, no extra fingers, no third hand, no blur, no bokeh, no warm orange color cast, no yellow tint, no golden glow, no golden hour light, no sunset, no HDR, no cinematic lighting, no de-aging, no beauty smoothing, no visible phone, no glasses, no kitchen, no white marble counter, no silver cross, no white coat, no second face in frame, no full second body"
}
```

### K06 · T6, os dois modelos de joelho · anexar ÂNCORA HOLISTIC BRANDON + FRAME DO MODELO

```text
K06
{
  "format": "IMPORTANT: THIS IS IPHONE FOOTAGE. Vertical 9:16.",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "reference_use": "Use the first attached image only for Brandon's exact identity, wardrobe and her own garage gym. Use the second attached image only as a composition reference for the camera position, framing and the action; do not copy its man, glasses, gray t-shirt, kitchen, marble counter, cartoon magnet or the caption text.",
  "identity_main": "The exact fictional AI character holistic.brandon: Black mixed-race American woman around thirty, athletic and toned, medium light-brown skin with light freckles across the nose and cheeks, dark brown eyes, defined eyebrows, full lips, hair in tight cornrows that turn into long loose braids falling over both shoulders, finished with small wooden and gold beads, a black floral blackwork tattoo sleeve on her right arm, a small line tattoo on her left upper arm and small fine-line tattoos on her chest near the collarbones. She reads as an ordinary anonymous American fitness coach, not resembling anyone famous.",
  "wardrobe": "Plain white ribbed tank top with nothing printed or written on it, loose black training shorts ending at mid-thigh, a thin gold chain with a small gold cross pendant and small stud earrings.",
  "scene": "Her own garage gym, the same room as the reference: a white-painted concrete block wall and a dark wooden slat ceiling, a red neon sign reading TRAIN PRAY REPEAT on the wall at the left, a whiteboard with handwritten black marker reading STAY READY. STAY DISCIPLINED. on the right, and a small American flag pinned above the whiteboard, discreet but clearly visible and in focus. The background is reduced by framing, never by blur.",
  "prop": "Two life-size anatomical knee joint models stand upright side by side on two small white square bases on the black table in front of her, very close to the lens: each one a bone-colored femur on top and tibia and fibula below, joined at the knee. The left model has the joint cartilage worn rough and eroded, with red inflamed patches and frayed tissue across the joint surface; the right model has smooth white cartilage, a clean joint and small pink ligaments. Her right index finger points at the red patches of the left model.",
  "posture": "Brandon leans in behind the two models, her face just above and between them.",
  "composition": "Very close shot at table height: the phone lens is about 25 centimeters from the models, which fill the lower 60 percent of the frame almost edge to edge, taller than her head, closer to the camera than her face; her face is in the upper third between their tops. Nothing else is on the table. The background is reduced by framing, never by blur.",
  "camera": "phone propped at table height, standard 1x lens, level",
  "lighting": "Neutral overcast daylight from a large window out of frame, soft even light on her face, hands and knees with no harsh shadows. The red neon glows on the wall but does not tint her skin.",
  "state": "Start frame: her finger touches the red patches of the left model. Brandon is caught mid-sentence, lips naturally parted, animated expression, looking straight into the lens.",
  "realism": "Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday reality, background fully in focus, everything in sharp focus, no AI polish, no beauty smoothing.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no studio, no plastic-looking skin, no extra fingers, no third hand, no blur, no bokeh, no warm orange color cast, no yellow tint, no golden glow, no golden hour light, no sunset, no HDR, no cinematic lighting, no de-aging, no beauty smoothing, no visible phone, no glasses, no kitchen, no white marble counter, no silver cross, no white coat, no second person, no plastic skeleton, no extra bones"
}
```

### K07 · T7, mesa, dor · anexar ÂNCORA HOLISTIC BRANDON + FRAME DO MODELO

```text
K07
{
  "format": "IMPORTANT: THIS IS IPHONE FOOTAGE. Vertical 9:16.",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "reference_use": "Use the first attached image only for Brandon's exact identity, wardrobe and her own garage gym. Use the second attached image only as a composition reference for the camera position, framing and the action; do not copy its man, glasses, gray t-shirt, kitchen, marble counter, cartoon magnet or the caption text.",
  "identity_main": "The exact fictional AI character holistic.brandon: Black mixed-race American woman around thirty, athletic and toned, medium light-brown skin with light freckles across the nose and cheeks, dark brown eyes, defined eyebrows, full lips, hair in tight cornrows that turn into long loose braids falling over both shoulders, finished with small wooden and gold beads, a black floral blackwork tattoo sleeve on her right arm, a small line tattoo on her left upper arm and small fine-line tattoos on her chest near the collarbones. She reads as an ordinary anonymous American fitness coach, not resembling anyone famous.",
  "wardrobe": "Plain white ribbed tank top with nothing printed or written on it, loose black training shorts ending at mid-thigh, a thin gold chain with a small gold cross pendant and small stud earrings.",
  "scene": "Her own garage gym, the same room as the reference: a white-painted concrete block wall and a dark wooden slat ceiling, a red neon sign reading TRAIN PRAY REPEAT on the wall at the left, a whiteboard with handwritten black marker reading STAY READY. STAY DISCIPLINED. on the right, and a small American flag pinned above the whiteboard, discreet but clearly visible and in focus. The background is reduced by framing, never by blur.",
  "prop": "No prop. The black table is empty; the bowl, the bottle and the jar are out of frame.",
  "posture": "Brandon stands behind the black table in front of her, leaning on her forearms on the table edge, seen from the waist up, her bare hands resting on the table near the lens. Both palms open upward, spread apart.",
  "composition": "Straight-on medium shot from table height: the phone lens is about 50 centimeters from her; her hands on the table fill about 30 percent of the frame at the bottom, closer to the camera than her face, and her face and shoulders fill the upper half. The table is empty. The background is reduced by framing, never by blur.",
  "camera": "phone propped at table height about 50 centimeters from her, standard 1x lens tilted slightly up",
  "lighting": "Neutral overcast daylight from a large window out of frame, soft even light on her face, hands and knees with no harsh shadows. The red neon glows on the wall but does not tint her skin.",
  "state": "Start frame: Brandon is caught mid-sentence, lips naturally parted, animated expression, looking straight into the lens, understanding and warm.",
  "realism": "Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday reality, background fully in focus, everything in sharp focus, no AI polish, no beauty smoothing.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no studio, no plastic-looking skin, no extra fingers, no third hand, no blur, no bokeh, no warm orange color cast, no yellow tint, no golden glow, no golden hour light, no sunset, no HDR, no cinematic lighting, no de-aging, no beauty smoothing, no visible phone, no glasses, no kitchen, no white marble counter, no silver cross, no white coat, no second person"
}
```

### K08 · T8, mesa, objeção · anexar ÂNCORA HOLISTIC BRANDON + FRAME DO MODELO

```text
K08
{
  "format": "IMPORTANT: THIS IS IPHONE FOOTAGE. Vertical 9:16.",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "reference_use": "Use the first attached image only for Brandon's exact identity, wardrobe and her own garage gym. Use the second attached image only as a composition reference for the camera position, framing and the action; do not copy its man, glasses, gray t-shirt, kitchen, marble counter, cartoon magnet or the caption text.",
  "identity_main": "The exact fictional AI character holistic.brandon: Black mixed-race American woman around thirty, athletic and toned, medium light-brown skin with light freckles across the nose and cheeks, dark brown eyes, defined eyebrows, full lips, hair in tight cornrows that turn into long loose braids falling over both shoulders, finished with small wooden and gold beads, a black floral blackwork tattoo sleeve on her right arm, a small line tattoo on her left upper arm and small fine-line tattoos on her chest near the collarbones. She reads as an ordinary anonymous American fitness coach, not resembling anyone famous.",
  "wardrobe": "Plain white ribbed tank top with nothing printed or written on it, loose black training shorts ending at mid-thigh, a thin gold chain with a small gold cross pendant and small stud earrings.",
  "scene": "Her own garage gym, the same room as the reference: a white-painted concrete block wall and a dark wooden slat ceiling, a red neon sign reading TRAIN PRAY REPEAT on the wall at the left, a whiteboard with handwritten black marker reading STAY READY. STAY DISCIPLINED. on the right, and a small American flag pinned above the whiteboard, discreet but clearly visible and in focus. The background is reduced by framing, never by blur.",
  "prop": "No prop. The black table is empty; the bowl, the bottle and the jar are out of frame.",
  "posture": "Brandon stands behind the black table in front of her, leaning on her forearms on the table edge, seen from the waist up, her bare hands resting on the table near the lens. Both palms open upward, lifted a little as in a question.",
  "composition": "Straight-on medium shot from table height: the phone lens is about 50 centimeters from her; her hands on the table fill about 30 percent of the frame at the bottom, closer to the camera than her face, and her face and shoulders fill the upper half. The table is empty. The background is reduced by framing, never by blur.",
  "camera": "phone propped at table height about 50 centimeters from her, standard 1x lens tilted slightly up",
  "lighting": "Neutral overcast daylight from a large window out of frame, soft even light on her face, hands and knees with no harsh shadows. The red neon glows on the wall but does not tint her skin.",
  "state": "Start frame: Brandon is caught mid-sentence, lips naturally parted, animated expression, looking straight into the lens, eyebrows raised.",
  "realism": "Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday reality, background fully in focus, everything in sharp focus, no AI polish, no beauty smoothing.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no studio, no plastic-looking skin, no extra fingers, no third hand, no blur, no bokeh, no warm orange color cast, no yellow tint, no golden glow, no golden hour light, no sunset, no HDR, no cinematic lighting, no de-aging, no beauty smoothing, no visible phone, no glasses, no kitchen, no white marble counter, no silver cross, no white coat, no second person"
}
```

### K09 · T9, mesa, virada · anexar ÂNCORA HOLISTIC BRANDON + FRAME DO MODELO

```text
K09
{
  "format": "IMPORTANT: THIS IS IPHONE FOOTAGE. Vertical 9:16.",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "reference_use": "Use the first attached image only for Brandon's exact identity, wardrobe and her own garage gym. Use the second attached image only as a composition reference for the camera position, framing and the action; do not copy its man, glasses, gray t-shirt, kitchen, marble counter, cartoon magnet or the caption text.",
  "identity_main": "The exact fictional AI character holistic.brandon: Black mixed-race American woman around thirty, athletic and toned, medium light-brown skin with light freckles across the nose and cheeks, dark brown eyes, defined eyebrows, full lips, hair in tight cornrows that turn into long loose braids falling over both shoulders, finished with small wooden and gold beads, a black floral blackwork tattoo sleeve on her right arm, a small line tattoo on her left upper arm and small fine-line tattoos on her chest near the collarbones. She reads as an ordinary anonymous American fitness coach, not resembling anyone famous.",
  "wardrobe": "Plain white ribbed tank top with nothing printed or written on it, loose black training shorts ending at mid-thigh, a thin gold chain with a small gold cross pendant and small stud earrings.",
  "scene": "Her own garage gym, the same room as the reference: a white-painted concrete block wall and a dark wooden slat ceiling, a red neon sign reading TRAIN PRAY REPEAT on the wall at the left, a whiteboard with handwritten black marker reading STAY READY. STAY DISCIPLINED. on the right, and a small American flag pinned above the whiteboard, discreet but clearly visible and in focus. The background is reduced by framing, never by blur.",
  "prop": "No prop. The black table is empty; the bowl, the bottle and the jar are out of frame.",
  "posture": "Brandon stands behind the black table in front of her, leaning on her forearms on the table edge, seen from the waist up, her bare hands resting on the table near the lens. Her fingertips touch together above the table.",
  "composition": "Straight-on medium shot from table height: the phone lens is about 50 centimeters from her; her hands on the table fill about 30 percent of the frame at the bottom, closer to the camera than her face, and her face and shoulders fill the upper half. The table is empty. The background is reduced by framing, never by blur.",
  "camera": "phone propped at table height about 50 centimeters from her, standard 1x lens tilted slightly up",
  "lighting": "Neutral overcast daylight from a large window out of frame, soft even light on her face, hands and knees with no harsh shadows. The red neon glows on the wall but does not tint her skin.",
  "state": "Start frame: Brandon leans slightly toward the lens and is caught mid-sentence, lips naturally parted, animated expression, looking straight into the lens.",
  "realism": "Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday reality, background fully in focus, everything in sharp focus, no AI polish, no beauty smoothing.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no studio, no plastic-looking skin, no extra fingers, no third hand, no blur, no bokeh, no warm orange color cast, no yellow tint, no golden glow, no golden hour light, no sunset, no HDR, no cinematic lighting, no de-aging, no beauty smoothing, no visible phone, no glasses, no kitchen, no white marble counter, no silver cross, no white coat, no second person"
}
```

### K10 · T10, mesa, mecanismo · anexar ÂNCORA HOLISTIC BRANDON + FRAME DO MODELO

```text
K10
{
  "format": "IMPORTANT: THIS IS IPHONE FOOTAGE. Vertical 9:16.",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "reference_use": "Use the first attached image only for Brandon's exact identity, wardrobe and her own garage gym. Use the second attached image only as a composition reference for the camera position, framing and the action; do not copy its man, glasses, gray t-shirt, kitchen, marble counter, cartoon magnet or the caption text.",
  "identity_main": "The exact fictional AI character holistic.brandon: Black mixed-race American woman around thirty, athletic and toned, medium light-brown skin with light freckles across the nose and cheeks, dark brown eyes, defined eyebrows, full lips, hair in tight cornrows that turn into long loose braids falling over both shoulders, finished with small wooden and gold beads, a black floral blackwork tattoo sleeve on her right arm, a small line tattoo on her left upper arm and small fine-line tattoos on her chest near the collarbones. She reads as an ordinary anonymous American fitness coach, not resembling anyone famous.",
  "wardrobe": "Plain white ribbed tank top with nothing printed or written on it, loose black training shorts ending at mid-thigh, a thin gold chain with a small gold cross pendant and small stud earrings.",
  "scene": "Her own garage gym, the same room as the reference: a white-painted concrete block wall and a dark wooden slat ceiling, a red neon sign reading TRAIN PRAY REPEAT on the wall at the left, a whiteboard with handwritten black marker reading STAY READY. STAY DISCIPLINED. on the right, and a small American flag pinned above the whiteboard, discreet but clearly visible and in focus. The background is reduced by framing, never by blur.",
  "prop": "No prop. The black table is empty; the bowl, the bottle and the jar are out of frame.",
  "posture": "Brandon stands behind the black table in front of her, leaning on her forearms on the table edge, seen from the waist up, her bare hands resting on the table near the lens. Both hands open, a little apart, mid-gesture.",
  "composition": "Straight-on medium shot from table height: the phone lens is about 50 centimeters from her; her hands on the table fill about 30 percent of the frame at the bottom, closer to the camera than her face, and her face and shoulders fill the upper half. The table is empty. The background is reduced by framing, never by blur.",
  "camera": "phone propped at table height about 50 centimeters from her, standard 1x lens tilted slightly up",
  "lighting": "Neutral overcast daylight from a large window out of frame, soft even light on her face, hands and knees with no harsh shadows. The red neon glows on the wall but does not tint her skin.",
  "state": "Start frame: Brandon is caught mid-sentence, lips naturally parted, animated expression, looking straight into the lens, explaining.",
  "realism": "Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday reality, background fully in focus, everything in sharp focus, no AI polish, no beauty smoothing.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no studio, no plastic-looking skin, no extra fingers, no third hand, no blur, no bokeh, no warm orange color cast, no yellow tint, no golden glow, no golden hour light, no sunset, no HDR, no cinematic lighting, no de-aging, no beauty smoothing, no visible phone, no glasses, no kitchen, no white marble counter, no silver cross, no white coat, no second person"
}
```

### K11 · T11, mesa, solução · anexar ÂNCORA HOLISTIC BRANDON + FRAME DO MODELO

```text
K11
{
  "format": "IMPORTANT: THIS IS IPHONE FOOTAGE. Vertical 9:16.",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "reference_use": "Use the first attached image only for Brandon's exact identity, wardrobe and her own garage gym. Use the second attached image only as a composition reference for the camera position, framing and the action; do not copy its man, glasses, gray t-shirt, kitchen, marble counter, cartoon magnet or the caption text.",
  "identity_main": "The exact fictional AI character holistic.brandon: Black mixed-race American woman around thirty, athletic and toned, medium light-brown skin with light freckles across the nose and cheeks, dark brown eyes, defined eyebrows, full lips, hair in tight cornrows that turn into long loose braids falling over both shoulders, finished with small wooden and gold beads, a black floral blackwork tattoo sleeve on her right arm, a small line tattoo on her left upper arm and small fine-line tattoos on her chest near the collarbones. She reads as an ordinary anonymous American fitness coach, not resembling anyone famous.",
  "wardrobe": "Plain white ribbed tank top with nothing printed or written on it, loose black training shorts ending at mid-thigh, a thin gold chain with a small gold cross pendant and small stud earrings.",
  "scene": "Her own garage gym, the same room as the reference: a white-painted concrete block wall and a dark wooden slat ceiling, a red neon sign reading TRAIN PRAY REPEAT on the wall at the left, a whiteboard with handwritten black marker reading STAY READY. STAY DISCIPLINED. on the right, and a small American flag pinned above the whiteboard, discreet but clearly visible and in focus. The background is reduced by framing, never by blur.",
  "prop": "No prop. The black table is empty; the bowl, the bottle and the jar are out of frame.",
  "posture": "Brandon stands behind the black table in front of her, leaning on her forearms on the table edge, seen from the waist up, her bare hands resting on the table near the lens. Her hands are loosely clasped together on the table.",
  "composition": "Straight-on medium shot from table height: the phone lens is about 50 centimeters from her; her hands on the table fill about 30 percent of the frame at the bottom, closer to the camera than her face, and her face and shoulders fill the upper half. The table is empty. The background is reduced by framing, never by blur.",
  "camera": "phone propped at table height about 50 centimeters from her, standard 1x lens tilted slightly up",
  "lighting": "Neutral overcast daylight from a large window out of frame, soft even light on her face, hands and knees with no harsh shadows. The red neon glows on the wall but does not tint her skin.",
  "state": "Start frame: Brandon is caught mid-sentence, lips naturally parted, animated expression, looking straight into the lens, firm and sure.",
  "realism": "Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday reality, background fully in focus, everything in sharp focus, no AI polish, no beauty smoothing.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no studio, no plastic-looking skin, no extra fingers, no third hand, no blur, no bokeh, no warm orange color cast, no yellow tint, no golden glow, no golden hour light, no sunset, no HDR, no cinematic lighting, no de-aging, no beauty smoothing, no visible phone, no glasses, no kitchen, no white marble counter, no silver cross, no white coat, no second person"
}
```

### K12 · T12, pote sobe no nome · anexar ÂNCORA HOLISTIC BRANDON + FRAME DO MODELO + FOTO DO POTE

```text
K12
{
  "format": "IMPORTANT: THIS IS IPHONE FOOTAGE. Vertical 9:16.",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "reference_use": "Use the first attached image only for Brandon's exact identity, wardrobe and her own garage gym. Use the second attached image only as a composition reference for the camera position, framing and the action; do not copy its man, glasses, gray t-shirt, kitchen, marble counter, cartoon magnet or the caption text. Use the third attached image only for the exact look of the front jar and its label; ignore the MADE IN USA banner, the second jar with the Supplement Facts panel and the loose gummies.",
  "identity_main": "The exact fictional AI character holistic.brandon: Black mixed-race American woman around thirty, athletic and toned, medium light-brown skin with light freckles across the nose and cheeks, dark brown eyes, defined eyebrows, full lips, hair in tight cornrows that turn into long loose braids falling over both shoulders, finished with small wooden and gold beads, a black floral blackwork tattoo sleeve on her right arm, a small line tattoo on her left upper arm and small fine-line tattoos on her chest near the collarbones. She reads as an ordinary anonymous American fitness coach, not resembling anyone famous.",
  "wardrobe": "Plain white ribbed tank top with nothing printed or written on it, loose black training shorts ending at mid-thigh, a thin gold chain with a small gold cross pendant and small stud earrings.",
  "scene": "Her own garage gym, the same room as the reference: a white-painted concrete block wall and a dark wooden slat ceiling, a red neon sign reading TRAIN PRAY REPEAT on the wall at the left, a whiteboard with handwritten black marker reading STAY READY. STAY DISCIPLINED. on the right, and a small American flag pinned above the whiteboard, discreet but clearly visible and in focus. The background is reduced by framing, never by blur.",
  "prop": "Raised with both hands in front of her chest, she holds the Natural Rems Sea Moss Gummies jar exactly as in the attached product photo: a short wide jar of dark amber plastic with a black screw cap, a pale sage-green label with dark green text, the Natural Rems logo with three leaves at the top, the big title Sea Moss Gummies, a pill-shaped badge reading 6000 MG | 16-IN-1, the line GREEN APPLE FLAVOR, two columns of dark green ingredient pills, green seaweed illustrations on the sides and a small 30 Gummies badge. The label is turned straight to the lens and fully readable, her fingers only on the sides of the jar.",
  "posture": "Brandon stands behind the black table in front of her, seen from the waist up, holding the jar toward the camera.",
  "composition": "Straight-on medium shot from table height: the phone lens is about 40 centimeters from the jar, which fills about 25 percent of the frame in the lower center, closer to the camera than her face; her face and shoulders fill the upper half. The table is empty. The background is reduced by framing, never by blur.",
  "camera": "phone propped at table height about 40 centimeters from the jar, standard 1x lens, level",
  "lighting": "Neutral overcast daylight from a large window out of frame, soft even light on her face, hands and knees with no harsh shadows. The red neon glows on the wall but does not tint her skin.",
  "state": "Start frame: Brandon is smiling and caught mid-sentence, lips naturally parted, animated expression, looking straight into the lens.",
  "realism": "Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday reality, background fully in focus, everything in sharp focus, no AI polish, no beauty smoothing.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no studio, no plastic-looking skin, no extra fingers, no third hand, no blur, no bokeh, no warm orange color cast, no yellow tint, no golden glow, no golden hour light, no sunset, no HDR, no cinematic lighting, no de-aging, no beauty smoothing, no visible phone, no glasses, no kitchen, no white marble counter, no silver cross, no white coat, no second person, no second jar, no loose gummies, no banner on the jar, no fingers over the label"
}
```

### K13 · T13, pote, ingredientes · anexar ÂNCORA HOLISTIC BRANDON + FRAME DO MODELO + FOTO DO POTE

```text
K13
{
  "format": "IMPORTANT: THIS IS IPHONE FOOTAGE. Vertical 9:16.",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "reference_use": "Use the first attached image only for Brandon's exact identity, wardrobe and her own garage gym. Use the second attached image only as a composition reference for the camera position, framing and the action; do not copy its man, glasses, gray t-shirt, kitchen, marble counter, cartoon magnet or the caption text. Use the third attached image only for the exact look of the front jar and its label; ignore the MADE IN USA banner, the second jar with the Supplement Facts panel and the loose gummies.",
  "identity_main": "The exact fictional AI character holistic.brandon: Black mixed-race American woman around thirty, athletic and toned, medium light-brown skin with light freckles across the nose and cheeks, dark brown eyes, defined eyebrows, full lips, hair in tight cornrows that turn into long loose braids falling over both shoulders, finished with small wooden and gold beads, a black floral blackwork tattoo sleeve on her right arm, a small line tattoo on her left upper arm and small fine-line tattoos on her chest near the collarbones. She reads as an ordinary anonymous American fitness coach, not resembling anyone famous.",
  "wardrobe": "Plain white ribbed tank top with nothing printed or written on it, loose black training shorts ending at mid-thigh, a thin gold chain with a small gold cross pendant and small stud earrings.",
  "scene": "Her own garage gym, the same room as the reference: a white-painted concrete block wall and a dark wooden slat ceiling, a red neon sign reading TRAIN PRAY REPEAT on the wall at the left, a whiteboard with handwritten black marker reading STAY READY. STAY DISCIPLINED. on the right, and a small American flag pinned above the whiteboard, discreet but clearly visible and in focus. The background is reduced by framing, never by blur.",
  "prop": "In her left hand, in front of her chest, she holds the Natural Rems Sea Moss Gummies jar exactly as in the attached product photo: a short wide jar of dark amber plastic with a black screw cap, a pale sage-green label with dark green text, the Natural Rems logo with three leaves at the top, the big title Sea Moss Gummies, a pill-shaped badge reading 6000 MG | 16-IN-1, the line GREEN APPLE FLAVOR, two columns of dark green ingredient pills, green seaweed illustrations on the sides and a small 30 Gummies badge. The label is turned straight to the lens and fully readable, her right index finger pointing at the ingredient pills on the label.",
  "posture": "Brandon stands behind the black table in front of her, seen from the waist up, holding the jar toward the camera.",
  "composition": "Straight-on medium shot from table height: the phone lens is about 40 centimeters from the jar, which fills about 25 percent of the frame in the lower center, closer to the camera than her face; her face and shoulders fill the upper half. The table is empty. The background is reduced by framing, never by blur.",
  "camera": "phone propped at table height about 40 centimeters from the jar, standard 1x lens, level",
  "lighting": "Neutral overcast daylight from a large window out of frame, soft even light on her face, hands and knees with no harsh shadows. The red neon glows on the wall but does not tint her skin.",
  "state": "Start frame: Brandon is caught mid-sentence, lips naturally parted, animated expression, looking straight into the lens, upbeat.",
  "realism": "Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday reality, background fully in focus, everything in sharp focus, no AI polish, no beauty smoothing.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no studio, no plastic-looking skin, no extra fingers, no third hand, no blur, no bokeh, no warm orange color cast, no yellow tint, no golden glow, no golden hour light, no sunset, no HDR, no cinematic lighting, no de-aging, no beauty smoothing, no visible phone, no glasses, no kitchen, no white marble counter, no silver cross, no white coat, no second person, no second jar, no loose gummies, no banner on the jar, no fingers over the label"
}
```

### K14 · T14, CTA, pote parado e legível · anexar ÂNCORA HOLISTIC BRANDON + FRAME DO MODELO + FOTO DO POTE

```text
K14
{
  "format": "IMPORTANT: THIS IS IPHONE FOOTAGE. Vertical 9:16.",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "reference_use": "Use the first attached image only for Brandon's exact identity, wardrobe and her own garage gym. Use the second attached image only as a composition reference for the camera position, framing and the action; do not copy its man, glasses, gray t-shirt, kitchen, marble counter, cartoon magnet or the caption text. Use the third attached image only for the exact look of the front jar and its label; ignore the MADE IN USA banner, the second jar with the Supplement Facts panel and the loose gummies.",
  "identity_main": "The exact fictional AI character holistic.brandon: Black mixed-race American woman around thirty, athletic and toned, medium light-brown skin with light freckles across the nose and cheeks, dark brown eyes, defined eyebrows, full lips, hair in tight cornrows that turn into long loose braids falling over both shoulders, finished with small wooden and gold beads, a black floral blackwork tattoo sleeve on her right arm, a small line tattoo on her left upper arm and small fine-line tattoos on her chest near the collarbones. She reads as an ordinary anonymous American fitness coach, not resembling anyone famous.",
  "wardrobe": "Plain white ribbed tank top with nothing printed or written on it, loose black training shorts ending at mid-thigh, a thin gold chain with a small gold cross pendant and small stud earrings.",
  "scene": "Her own garage gym, the same room as the reference: a white-painted concrete block wall and a dark wooden slat ceiling, a red neon sign reading TRAIN PRAY REPEAT on the wall at the left, a whiteboard with handwritten black marker reading STAY READY. STAY DISCIPLINED. on the right, and a small American flag pinned above the whiteboard, discreet but clearly visible and in focus. The background is reduced by framing, never by blur.",
  "prop": "Perfectly still with both hands in front of her chest, centered, she holds the Natural Rems Sea Moss Gummies jar exactly as in the attached product photo: a short wide jar of dark amber plastic with a black screw cap, a pale sage-green label with dark green text, the Natural Rems logo with three leaves at the top, the big title Sea Moss Gummies, a pill-shaped badge reading 6000 MG | 16-IN-1, the line GREEN APPLE FLAVOR, two columns of dark green ingredient pills, green seaweed illustrations on the sides and a small 30 Gummies badge. The label is turned straight to the lens, fully readable and with nothing covering it.",
  "posture": "Brandon stands behind the black table in front of her, seen from the chest up, holding the jar toward the camera.",
  "composition": "The tightest shot of the video, straight-on from chest height: the phone lens is about 35 centimeters from the jar, which fills about 30 percent of the frame in the lower center, closer to the camera than her face; her face fills the upper half. The background is reduced by framing, never by blur.",
  "camera": "phone propped at chest height, standard 1x lens, level",
  "lighting": "Neutral overcast daylight from a large window out of frame, soft even light on her face, hands and knees with no harsh shadows. The red neon glows on the wall but does not tint her skin.",
  "state": "Start frame: Brandon is caught mid-sentence, lips naturally parted, animated expression, looking straight into the lens, clear and calm.",
  "realism": "Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday reality, background fully in focus, everything in sharp focus, no AI polish, no beauty smoothing.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no studio, no plastic-looking skin, no extra fingers, no third hand, no blur, no bokeh, no warm orange color cast, no yellow tint, no golden glow, no golden hour light, no sunset, no HDR, no cinematic lighting, no de-aging, no beauty smoothing, no visible phone, no glasses, no kitchen, no white marble counter, no silver cross, no white coat, no second person, no second jar, no loose gummies, no banner on the jar, no fingers over the label"
}
```

## 3. PROMPTS DE VÍDEO (um bloco por V)

### V01 · T1 · frame inicial = a imagem que você deixou no K01

```text
V01
a avatar Brandon, mulher, fala em inglês com sotaque americano de uma mulher negra americana, voz feminina clara e firme de uma mulher de uns trinta anos, entonação intrigante e desafiadora, como quem avisa, voz autêntica, como se exigisse ser ouvida, a seguinte frase: "Rub hydrogen peroxide on your knees and watch what happens. If it starts foaming, it just found what has been living inside your joints."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Uma mão que entra pela borda direita derrama a água oxigenada do frasco marrom sobre o joelho dela; por volta de 2 segundos o líquido toca a pele, uma espuma branca nasce, cresce em bolhas grossas e depois escorre em gotas pela canela. Brandon fala olhando para a câmera. A pessoa da mão fica em silêncio.

câmera: leve handheld, bem perto do joelho

som ambiente: box de treino em casa, tranquilo, líquido caindo e espuma estalando, sem música
```

### V02 · T2 · frame inicial = a imagem que você deixou no K02

```text
V02
a avatar Brandon, mulher, fala em inglês com sotaque americano de uma mulher negra americana, voz feminina clara e firme de uma mulher de uns trinta anos, entonação calma e didática, voz autêntica, como se exigisse ser ouvida, a seguinte frase: "Half a cup of hydrogen peroxide,"

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Brandon, inclinada sobre a mesa, derrama o frasco marrom dentro da tigela branca. Ela diz a frase em ritmo natural logo no começo e a ação continua em silêncio até o fim.

câmera: leve handheld

som ambiente: box de treino em casa, tranquilo, líquido caindo na tigela, sem música
```

### V03 · T3 · frame inicial = a imagem que você deixou no K03

```text
V03
a avatar Brandon, mulher, fala em inglês com sotaque americano de uma mulher negra americana, voz feminina clara e firme de uma mulher de uns trinta anos, entonação calma e didática, voz autêntica, como se exigisse ser ouvida, a seguinte frase: "two cups of warm water, and a spoonful of baking soda."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Brandon despeja as duas canecas de água na tigela ao mesmo tempo, larga as canecas, pega a colher de bicarbonato e vira dentro da tigela. Ela diz a frase em ritmo natural logo no começo e a ação continua em silêncio até o fim.

câmera: leve handheld

som ambiente: box de treino em casa, tranquilo, água caindo na tigela e a colher batendo na cerâmica, sem música
```

### V04 · T4 · frame inicial = a imagem que você deixou no K04

```text
V04
a avatar Brandon, mulher, fala em inglês com sotaque americano de uma mulher negra americana, voz feminina clara e firme de uma mulher de uns trinta anos, entonação calma e didática, voz autêntica, como se exigisse ser ouvida, a seguinte frase: "Soak a cloth and press it firmly onto your knees for ten minutes."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Brandon pega o pano branco da mão que entra pela direita, mergulha o pano na tigela e torce de leve. A pessoa da mão fica em silêncio.

câmera: leve handheld, bem perto do joelho

som ambiente: box de treino em casa, tranquilo, pano pingando na tigela, sem música
```

### V05 · T5 · frame inicial = a imagem que você deixou no K05

```text
V05
a avatar Brandon, mulher, fala em inglês com sotaque americano de uma mulher negra americana, voz feminina clara e firme de uma mulher de uns trinta anos, entonação séria e convicta, baixando a voz em rotting, voz autêntica, como se exigisse ser ouvida, a seguinte frase: "That foam is bacteria and inflammation. It has been rotting inside your joints for years."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: As duas mãos que entram pela direita levantam o pano do joelho dela e revelam uma espuma branca de bolhas grossas sobre o joelho; Brandon aponta para a espuma com o indicador. A pessoa das mãos fica em silêncio.

câmera: leve handheld, bem perto do joelho

som ambiente: box de treino em casa, tranquilo, espuma estalando baixinho, sem música
```

### V06 · T6 · frame inicial = a imagem que você deixou no K06

```text
V06
a avatar Brandon, mulher, fala em inglês com sotaque americano de uma mulher negra americana, voz feminina clara e firme de uma mulher de uns trinta anos, entonação séria e didática, voz autêntica, como se exigisse ser ouvida, a seguinte frase: "This is what roughs up the joint lining, adds to the grinding, and keeps causing that stiffness every morning."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Brandon aponta para as manchas vermelhas do modelo de joelho da esquerda e depois toca o modelo liso da direita.

câmera: fixa, bem perto dos modelos

som ambiente: box de treino em casa, tranquilo, sem música
```

### V07 · T7 · frame inicial = a imagem que você deixou no K07

```text
V07
a avatar Brandon, mulher, fala em inglês com sotaque americano de uma mulher negra americana, voz feminina clara e firme de uma mulher de uns trinta anos, entonação compreensiva e próxima, voz autêntica, como se exigisse ser ouvida, a seguinte frase: "If you're dealing with knee joint discomfort, everyone tells you to just get up and move more."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Brandon, com os antebraços apoiados na mesa, abre as mãos com as palmas para cima enquanto fala.

câmera: fixa

som ambiente: box de treino em casa, tranquilo, sem música
```

### V08 · T8 · frame inicial = a imagem que você deixou no K08

```text
V08
a avatar Brandon, mulher, fala em inglês com sotaque americano de uma mulher negra americana, voz feminina clara e firme de uma mulher de uns trinta anos, entonação indignada, como quem defende quem assiste, voz autêntica, como se exigisse ser ouvida, a seguinte frase: "But how are you supposed to exercise when you're constantly sluggish, running on zero energy, and feeling bloated and inflamed?"

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Brandon levanta um pouco as duas mãos abertas, palmas para cima, num gesto de pergunta.

câmera: fixa

som ambiente: box de treino em casa, tranquilo, sem música
```

### V09 · T9 · frame inicial = a imagem que você deixou no K09

```text
V09
a avatar Brandon, mulher, fala em inglês com sotaque americano de uma mulher negra americana, voz feminina clara e firme de uma mulher de uns trinta anos, entonação de quem conta um segredo, firme, voz autêntica, como se exigisse ser ouvida, a seguinte frase: "Here's what most people miss. Joint stiffness is often driven by systemic inflammation that starts right in your gut."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Brandon junta as pontas dos dedos sobre a mesa e se inclina um pouco para a câmera.

câmera: fixa

som ambiente: box de treino em casa, tranquilo, sem música
```

### V10 · T10 · frame inicial = a imagem que você deixou no K10

```text
V10
a avatar Brandon, mulher, fala em inglês com sotaque americano de uma mulher negra americana, voz feminina clara e firme de uma mulher de uns trinta anos, entonação didática e convicta, voz autêntica, como se exigisse ser ouvida, a seguinte frase: "When your digestion is out of balance, your body spends all its energy fighting inflammation, leaving you too drained to stay active, which only makes your joints feel tighter."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Brandon fala para a câmera abrindo e fechando as mãos devagar sobre a mesa, com pequenos gestos naturais.

câmera: fixa

som ambiente: box de treino em casa, tranquilo, sem música
```

### V11 · T11 · frame inicial = a imagem que você deixou no K11

```text
V11
a avatar Brandon, mulher, fala em inglês com sotaque americano de uma mulher negra americana, voz feminina clara e firme de uma mulher de uns trinta anos, entonação firme e segura, voz autêntica, como se exigisse ser ouvida, a seguinte frase: "To give your knees real relief, you have to cool the gut inflammation draining your energy."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Brandon junta as mãos sobre a mesa e olha firme para a câmera.

câmera: fixa

som ambiente: box de treino em casa, tranquilo, sem música
```

### V12 · T12 · frame inicial = a imagem que você deixou no K12

```text
V12
a avatar Brandon, mulher, fala em inglês com sotaque americano de uma mulher negra americana, voz feminina clara e firme de uma mulher de uns trinta anos, entonação calorosa e confiante, voz autêntica, como se exigisse ser ouvida, a seguinte frase: "That's why I put my clients on Natural Rems Sea Moss. Sixteen ingredients in one green apple gummy a day."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Brandon segura o pote de Natural Rems Sea Moss com as duas mãos na altura do peito, rótulo de frente para a câmera, e aproxima o pote um pouco da câmera quando diz o nome.

câmera: fixa

som ambiente: box de treino em casa, tranquilo, sem música
```

### V13 · T13 · frame inicial = a imagem que você deixou no K13

```text
V13
a avatar Brandon, mulher, fala em inglês com sotaque americano de uma mulher negra americana, voz feminina clara e firme de uma mulher de uns trinta anos, entonação animada e segura, voz autêntica, como se exigisse ser ouvida, a seguinte frase: "Turmeric, ginger and black seed oil to support your gut, and sea moss to help bring your energy back."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Brandon segura o pote parado na mão esquerda, rótulo de frente, e aponta para o rótulo com o indicador direito.

câmera: fixa

som ambiente: box de treino em casa, tranquilo, sem música
```

### V14 · T14 · frame inicial = a imagem que você deixou no K14

```text
V14
a avatar Brandon, mulher, fala em inglês com sotaque americano de uma mulher negra americana, voz feminina clara e firme de uma mulher de uns trinta anos, entonação clara e pausada, dizendo Natural Rems Sea Moss devagar e por inteiro, voz autêntica, como se exigisse ser ouvida, a seguinte frase: "Search Natural Rems Sea Moss on Amazon. Or you can just tap the link I left in the pinned comment on this video."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Brandon segura o pote parado com as duas mãos, rótulo de frente e legível, sem nada cobrindo, do começo ao fim; só o rosto e a boca se mexem.

câmera: fixa

som ambiente: box de treino em casa, tranquilo, sem música
```

## 4. Montagem no CapCut

1. Clipes numerados na ordem: V01 a V14.
2. Cortar cada clipe no tempo da cena do modelo: V01 0,0 a 7,6 s; V02 7,6 a 9,2 s; V03 9,2 a 13,2 s; V04 13,2 a 17,7 s; V05 17,7 a 23,4 s; V06 23,4 a 30,3 s; V07 30,3 a 35,7 s; V08 35,7 a 43,2 s; V09 43,2 a 50,4 s; V10 50,4 a 59,5 s; V11 59,5 a 64,8 s; V12 64,8 a ~70 s; V13 ~70 a ~74,5 s; V14 o CTA inteiro, sem corte (~7 s).
3. Zero tempo morto: todo clipe começa já falando. Isolate Voice / Keep Vocal no áudio.
4. Nos V02 e V03 (cenas curtas) a fala vem no começo; cortar logo depois da última palavra. O V02 termina em vírgula e o V03 continua a lista: emendar sem pausa.
5. V07 a V11 são o plano único de 34 s do modelo: emendar com corte seco, sem transição.
6. V14 inteiro, sem corte e sem nada cobrindo o pote: é o CTA da marca (frasco parado e legível enquanto o nome é dito). O vídeo acaba nele.
7. Legenda de tela como no modelo: serifada branca, palavra a palavra, no meio do quadro, com a palavra carregada maior (foaming, joints, bacteria, gut, Natural Rems Sea Moss).
8. Sem Voice Changer: a voz vem do prompt de cada V.
9. Música só depois do gancho (a partir do V02), nunca no pré-gancho, entre -19 e -20 dB, fora da biblioteca do TikTok.
10. Rótulo pequeno `Synthetic performer` num canto do vídeo (a marca não exige mais, mas não custa).
11. Legenda do post: `#ad #syntheticperformer #naturalrems` na primeira linha, e a chave de conteúdo de IA ligada na plataforma. O link da Amazon vai no comentário fixado.

## 5. Transcrição final por take

| Take | English | Português |
|---|---|---|
| T1 | Rub hydrogen peroxide on your knees and watch what happens. If it starts foaming, it just found what has been living inside your joints. | Passe água oxigenada nos joelhos e veja o que acontece. Se começar a espumar, ela acabou de achar o que anda vivendo dentro das suas articulações. |
| T2 | Half a cup of hydrogen peroxide, | Meia xícara de água oxigenada, |
| T3 | two cups of warm water, and a spoonful of baking soda. | duas xícaras de água morna e uma colher de bicarbonato. |
| T4 | Soak a cloth and press it firmly onto your knees for ten minutes. | Molhe um pano e aperte com firmeza nos joelhos por dez minutos. |
| T5 | That foam is bacteria and inflammation. It has been rotting inside your joints for years. | Essa espuma é bactéria e inflamação. Ela está apodrecendo dentro das suas articulações há anos. |
| T6 | This is what roughs up the joint lining, adds to the grinding, and keeps causing that stiffness every morning. | É isso que desgasta o revestimento da articulação, aumenta o atrito e continua causando aquela rigidez toda manhã. |
| T7 | If you're dealing with knee joint discomfort, everyone tells you to just get up and move more. | Se você vive com incômodo no joelho, todo mundo te diz pra simplesmente levantar e se mexer mais. |
| T8 | But how are you supposed to exercise when you're constantly sluggish, running on zero energy, and feeling bloated and inflamed? | Mas como você vai se exercitar se vive arrastada, sem energia nenhuma, e se sentindo inchada e inflamada? |
| T9 | Here's what most people miss. Joint stiffness is often driven by systemic inflammation that starts right in your gut. | Aqui está o que quase todo mundo deixa passar. A rigidez nas articulações muitas vezes vem de uma inflamação no corpo todo que começa bem no seu intestino. |
| T10 | When your digestion is out of balance, your body spends all its energy fighting inflammation, leaving you too drained to stay active, which only makes your joints feel tighter. | Quando a sua digestão sai do eixo, o corpo gasta toda a energia brigando com a inflamação, te deixa esgotada demais pra se manter ativa, e isso só deixa as articulações mais travadas. |
| T11 | To give your knees real relief, you have to cool the gut inflammation draining your energy. | Pra dar alívio de verdade aos seus joelhos, você precisa acalmar a inflamação do intestino que está drenando a sua energia. |
| T12 | That's why I put my clients on Natural Rems Sea Moss. Sixteen ingredients in one green apple gummy a day. | É por isso que eu coloco as minhas clientes no Natural Rems Sea Moss. Dezesseis ingredientes numa goma de maçã verde por dia. |
| T13 | Turmeric, ginger and black seed oil to support your gut, and sea moss to help bring your energy back. | Cúrcuma, gengibre e óleo de semente preta pra apoiar o seu intestino, e sea moss pra ajudar a trazer a sua energia de volta. |
| T14 | Search Natural Rems Sea Moss on Amazon. Or you can just tap the link I left in the pinned comment on this video. | Procure Natural Rems Sea Moss na Amazon. Ou é só tocar no link que eu deixei no comentário fixado deste vídeo. |

## 6. Roteiro final em inglês

1. Rub hydrogen peroxide on your knees and watch what happens. If it starts foaming, it just found what has been living inside your joints.
2. Half a cup of hydrogen peroxide,
3. two cups of warm water, and a spoonful of baking soda.
4. Soak a cloth and press it firmly onto your knees for ten minutes.
5. That foam is bacteria and inflammation. It has been rotting inside your joints for years.
6. This is what roughs up the joint lining, adds to the grinding, and keeps causing that stiffness every morning.
7. If you're dealing with knee joint discomfort, everyone tells you to just get up and move more.
8. But how are you supposed to exercise when you're constantly sluggish, running on zero energy, and feeling bloated and inflamed?
9. Here's what most people miss. Joint stiffness is often driven by systemic inflammation that starts right in your gut.
10. When your digestion is out of balance, your body spends all its energy fighting inflammation, leaving you too drained to stay active, which only makes your joints feel tighter.
11. To give your knees real relief, you have to cool the gut inflammation draining your energy.
12. That's why I put my clients on Natural Rems Sea Moss. Sixteen ingredients in one green apple gummy a day.
13. Turmeric, ginger and black seed oil to support your gut, and sea moss to help bring your energy back.
14. Search Natural Rems Sea Moss on Amazon. Or you can just tap the link I left in the pinned comment on this video.

Rub hydrogen peroxide on your knees and watch what happens. If it starts foaming, it just found what has been living inside your joints. Half a cup of hydrogen peroxide, two cups of warm water, and a spoonful of baking soda. Soak a cloth and press it firmly onto your knees for ten minutes. That foam is bacteria and inflammation. It has been rotting inside your joints for years. This is what roughs up the joint lining, adds to the grinding, and keeps causing that stiffness every morning. If you're dealing with knee joint discomfort, everyone tells you to just get up and move more. But how are you supposed to exercise when you're constantly sluggish, running on zero energy, and feeling bloated and inflamed? Here's what most people miss. Joint stiffness is often driven by systemic inflammation that starts right in your gut. When your digestion is out of balance, your body spends all its energy fighting inflammation, leaving you too drained to stay active, which only makes your joints feel tighter. To give your knees real relief, you have to cool the gut inflammation draining your energy. That's why I put my clients on Natural Rems Sea Moss. Sixteen ingredients in one green apple gummy a day. Turmeric, ginger and black seed oil to support your gut, and sea moss to help bring your energy back. Search Natural Rems Sea Moss on Amazon. Or you can just tap the link I left in the pinned comment on this video.
