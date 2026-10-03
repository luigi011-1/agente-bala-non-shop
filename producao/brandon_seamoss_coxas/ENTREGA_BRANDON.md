# ENTREGA | holistic.brandon | Natural Rems Sea Moss | Coxa escura

Produção `brandon_seamoss_coxas` · Ângulo 1 · VENDA · vídeo modelo de avatar IA · rodada de VALIDAÇÃO · perfil CLÁSSICO

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

Checklist de envio: 35/35 aprovados (N/A: A1, A2, A7 fiéis ao modelo; C4 a C7 sem selfie, frase repetida, cena atuada ou motion control)

Ficha: 11/11 K conferidos contra o frame do modelo, placar 14/14 cada (`FICHA_FRAMES.md`, GATE_VISUAL Parte 6)

## Anexos

- **Âncora holistic.brandon:** `producao/_ancoras/holistic_brandon_ancora.jpg` em TODOS os K.
- **Em cada K**, anexar também o frame do modelo daquele passo (`producao/brandon_seamoss_coxas/input/frames_modelo/Kxx_modelo.png`), só como referência de composição.
- **K10 e K11:** anexar também a foto do pote `producao/_ancoras/natural_rems_seamoss_produto.jpg` (só o pote da frente vale).
- K01 a K11 casam com V01 a V11 pelo número. Todos os V têm fala.

| Código | Take | Anexos além da âncora |
|---|---|---|
| K01 / V01 | T1, gancho, a coxa escura da cliente colada na lente | `input/frames_modelo/K01_modelo.png` |
| K02 / V02 | T2, virada, mão aberta, a coxa igual | `input/frames_modelo/K02_modelo.png` |
| K03 / V03 | T3, receita, limão na tigela | `input/frames_modelo/K03_modelo.png` |
| K04 / V04 | T4, receita, óleo de coco no conta-gotas | `input/frames_modelo/K04_modelo.png` |
| K05 / V05 | T5, protocolo, mexendo a pasta | `input/frames_modelo/K05_modelo.png` |
| K06 / V06 | T6, resultado, a tigela erguida | `input/frames_modelo/K06_modelo.png` |
| K07 / V07 | T7, ponte, a superfície | `input/frames_modelo/K07_modelo.png` |
| K08 / V08 | T8, mecanismo, causa e consequência | `input/frames_modelo/K08_modelo.png` |
| K09 / V09 | T9, a saída, tigela de lado | `input/frames_modelo/K09_modelo.png` |
| K10 / V10 | T10, pote sobe no nome | `input/frames_modelo/K10_modelo.png` + `producao/_ancoras/natural_rems_seamoss_produto.jpg` |
| K11 / V11 | T11, CTA, pote parado e legível | `input/frames_modelo/K11_modelo.png` + `producao/_ancoras/natural_rems_seamoss_produto.jpg` |

## 2. PROMPTS DE IMAGEM (um bloco por K)

### K01 · T1, gancho, a coxa escura da cliente colada na lente · anexar ÂNCORA HOLISTIC BRANDON + FRAME DO MODELO

```text
K01
{
  "format": "IMPORTANT: THIS IS IPHONE FOOTAGE. Vertical 9:16.",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "reference_use": "Use the first attached image only for Brandon's exact identity, wardrobe and her own garage gym. Use the second attached image only as a composition reference for the camera position, framing and the action; do not copy its older man and woman, aprons, kitchen, marble counter, exam room, framed certificates or the caption text.",
  "identity_main": "The exact fictional AI character holistic.brandon: Black mixed-race American woman around thirty, athletic and toned, medium light-brown skin with light freckles across the nose and cheeks, dark brown eyes, defined eyebrows, full lips, hair in tight cornrows that turn into long loose braids falling over both shoulders, finished with small wooden and gold beads, a black floral blackwork tattoo sleeve on her right arm, a small line tattoo on her left upper arm and small fine-line tattoos on her chest near the collarbones. She reads as an ordinary anonymous American fitness coach, not resembling anyone famous.",
  "wardrobe": "Plain white ribbed tank top with nothing printed or written on it, loose black training shorts ending at mid-thigh, a thin gold chain with a small gold cross pendant and small stud earrings.",
  "scene": "Her own garage gym, the same room as the reference: a white-painted concrete block wall and a dark wooden slat ceiling, a red neon sign reading TRAIN PRAY REPEAT on the wall at the left, a whiteboard with handwritten black marker reading STAY READY. STAY DISCIPLINED. on the right, and a small American flag pinned above the whiteboard, discreet but clearly visible and in focus. The background is reduced by framing, never by blur.",
  "prop": "The client, a fictional American woman around fifty with shoulder-length gray-brown hair, wearing a plain light gray crew-neck t-shirt and loose black athletic shorts that fully cover her hips, lies on her back on a black padded flat gym bench, her head and shoulders at the right edge of the frame, partly cut off by it. Her left leg is bent at the knee with the inner side of the thigh turned toward the camera: the bare inner thigh fills the lower 45 percent of the frame from the lower left to the center, very close to the lens, larger than both faces and closer to the camera than them, nothing else competing with it. On the upper inner thigh, just below the hem of her shorts, a large patch of dark brown, rough, velvety skin about the size of an open hand, clearly darker than the rest of her leg, with a few darker spots around its edge. Brandon's right hand rests flat on the thigh just above the dark patch, her index finger pointing at it.",
  "posture": "Brandon kneels on the black rubber floor at the left side of the bench, leaning in over the thigh, her face in the upper left of the frame.",
  "composition": "Low close shot at bench height: the phone lens is about 25 centimeters from the inner thigh, which fills the lower 45 percent of the frame; Brandon's face is in the upper left and the client's head at the right edge. The background is reduced by framing, never by blur.",
  "camera": "phone held low at bench height about 25 centimeters from the thigh, wide 0.5x lens, level",
  "lighting": "Neutral overcast daylight from a large window out of frame, soft even light on her face, hands and skin with no harsh shadows. The red neon glows on the wall but does not tint anyone's skin.",
  "state": "Start frame: the client lies calm with her eyes half closed. Brandon is caught mid-sentence, lips naturally parted, animated expression, looking straight into the lens.",
  "realism": "Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday reality, background fully in focus, everything in sharp focus, no AI polish, no beauty smoothing.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no studio, no plastic-looking skin, no extra fingers, no third hand, no blur, no bokeh, no warm orange color cast, no yellow tint, no golden glow, no golden hour light, no sunset, no HDR, no cinematic lighting, no de-aging, no beauty smoothing, no visible phone, no apron, no older man, no kitchen cabinets, no white marble counter, no framed certificates, no silver cross, no white coat, no gown, no paper sheet on the bench, no underwear showing, no lightened patch, no even skin on the inner thigh"
}
```

### K02 · T2, virada, mão aberta, a coxa igual · anexar ÂNCORA HOLISTIC BRANDON + FRAME DO MODELO

```text
K02
{
  "format": "IMPORTANT: THIS IS IPHONE FOOTAGE. Vertical 9:16.",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "reference_use": "Use the first attached image only for Brandon's exact identity, wardrobe and her own garage gym. Use the second attached image only as a composition reference for the camera position, framing and the action; do not copy its older man and woman, aprons, kitchen, marble counter, exam room, framed certificates or the caption text.",
  "identity_main": "The exact fictional AI character holistic.brandon: Black mixed-race American woman around thirty, athletic and toned, medium light-brown skin with light freckles across the nose and cheeks, dark brown eyes, defined eyebrows, full lips, hair in tight cornrows that turn into long loose braids falling over both shoulders, finished with small wooden and gold beads, a black floral blackwork tattoo sleeve on her right arm, a small line tattoo on her left upper arm and small fine-line tattoos on her chest near the collarbones. She reads as an ordinary anonymous American fitness coach, not resembling anyone famous.",
  "wardrobe": "Plain white ribbed tank top with nothing printed or written on it, loose black training shorts ending at mid-thigh, a thin gold chain with a small gold cross pendant and small stud earrings.",
  "scene": "Her own garage gym, the same room as the reference: a white-painted concrete block wall and a dark wooden slat ceiling, a red neon sign reading TRAIN PRAY REPEAT on the wall at the left, a whiteboard with handwritten black marker reading STAY READY. STAY DISCIPLINED. on the right, and a small American flag pinned above the whiteboard, discreet but clearly visible and in focus. The background is reduced by framing, never by blur.",
  "prop": "The client, a fictional American woman around fifty with shoulder-length gray-brown hair, wearing a plain light gray crew-neck t-shirt and loose black athletic shorts that fully cover her hips, lies on her back on a black padded flat gym bench, her head and shoulders at the right edge of the frame, partly cut off by it. Her left leg is bent at the knee with the inner side of the thigh turned toward the camera: the bare inner thigh fills the lower 45 percent of the frame from the lower left to the center, very close to the lens, larger than both faces and closer to the camera than them, nothing else competing with it. On the upper inner thigh, just below the hem of her shorts, a large patch of dark brown, rough, velvety skin about the size of an open hand, clearly darker than the rest of her leg, with a few darker spots around its edge. Brandon's left hand is held open, palm up, toward the lens just above the thigh.",
  "posture": "Brandon kneels on the black rubber floor at the left side of the bench, leaning in over the thigh, her face in the upper left of the frame.",
  "composition": "Low close shot at bench height: the phone lens is about 25 centimeters from the inner thigh, which fills the lower 45 percent of the frame; Brandon's face is in the upper left and the client's head at the right edge. The background is reduced by framing, never by blur.",
  "camera": "phone held low at bench height about 25 centimeters from the thigh, wide 0.5x lens, level",
  "lighting": "Neutral overcast daylight from a large window out of frame, soft even light on her face, hands and skin with no harsh shadows. The red neon glows on the wall but does not tint anyone's skin.",
  "state": "Start frame: the dark patch is exactly as before; the client looks at the lens with a faint smile. Brandon is caught mid-sentence, lips naturally parted, animated expression, looking straight into the lens.",
  "realism": "Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday reality, background fully in focus, everything in sharp focus, no AI polish, no beauty smoothing.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no studio, no plastic-looking skin, no extra fingers, no third hand, no blur, no bokeh, no warm orange color cast, no yellow tint, no golden glow, no golden hour light, no sunset, no HDR, no cinematic lighting, no de-aging, no beauty smoothing, no visible phone, no apron, no older man, no kitchen cabinets, no white marble counter, no framed certificates, no silver cross, no white coat, no gown, no paper sheet on the bench, no underwear showing, no lightened patch, no even skin on the inner thigh"
}
```

### K03 · T3, receita, limão na tigela · anexar ÂNCORA HOLISTIC BRANDON + FRAME DO MODELO

```text
K03
{
  "format": "IMPORTANT: THIS IS IPHONE FOOTAGE. Vertical 9:16.",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "reference_use": "Use the first attached image only for Brandon's exact identity, wardrobe and her own garage gym. Use the second attached image only as a composition reference for the camera position, framing and the action; do not copy its older man and woman, aprons, kitchen, marble counter, exam room, framed certificates or the caption text.",
  "identity_main": "The exact fictional AI character holistic.brandon: Black mixed-race American woman around thirty, athletic and toned, medium light-brown skin with light freckles across the nose and cheeks, dark brown eyes, defined eyebrows, full lips, hair in tight cornrows that turn into long loose braids falling over both shoulders, finished with small wooden and gold beads, a black floral blackwork tattoo sleeve on her right arm, a small line tattoo on her left upper arm and small fine-line tattoos on her chest near the collarbones. She reads as an ordinary anonymous American fitness coach, not resembling anyone famous.",
  "wardrobe": "Plain white ribbed tank top with nothing printed or written on it, loose black training shorts ending at mid-thigh, a thin gold chain with a small gold cross pendant and small stud earrings.",
  "scene": "Her own garage gym, the same room as the reference: a white-painted concrete block wall and a dark wooden slat ceiling, a red neon sign reading TRAIN PRAY REPEAT on the wall at the left, a whiteboard with handwritten black marker reading STAY READY. STAY DISCIPLINED. on the right, and a small American flag pinned above the whiteboard, discreet but clearly visible and in focus. The background is reduced by framing, never by blur.",
  "prop": "A clear glass mixing bowl with a heap of white baking soda powder in the center of the black table in front of her, very close to the lens, a metal measuring spoon lying at its left. Her right hand squeezes half a fresh lemon above the bowl; her left hand holds the rim of the bowl.",
  "posture": "Brandon stands behind the black table in front of her, leaning forward over it, seen from the waist up.",
  "composition": "Close shot from just above the table: the phone lens is about 40 centimeters from the bowl, which fills about 25 percent of the frame in the lower center, closer to the camera than her face; her head and torso fill the upper part. Nothing else is on the table. The background is reduced by framing, never by blur.",
  "camera": "phone held just above the table edge at chest height about 40 centimeters from the bowl, standard 1x lens tilted slightly down",
  "lighting": "Neutral overcast daylight from a large window out of frame, soft even light on her face, hands and skin with no harsh shadows. The red neon glows on the wall but does not tint anyone's skin.",
  "state": "Start frame: the first drops of lemon juice are falling into the powder. Brandon is caught mid-sentence, lips naturally parted, animated expression, looking straight into the lens.",
  "realism": "Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday reality, background fully in focus, everything in sharp focus, no AI polish, no beauty smoothing.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no studio, no plastic-looking skin, no extra fingers, no third hand, no blur, no bokeh, no warm orange color cast, no yellow tint, no golden glow, no golden hour light, no sunset, no HDR, no cinematic lighting, no de-aging, no beauty smoothing, no visible phone, no apron, no older man, no kitchen cabinets, no white marble counter, no framed certificates, no silver cross, no white coat, no second person, no readable lettering on the bowl, spoon or dropper bottle"
}
```

### K04 · T4, receita, óleo de coco no conta-gotas · anexar ÂNCORA HOLISTIC BRANDON + FRAME DO MODELO

```text
K04
{
  "format": "IMPORTANT: THIS IS IPHONE FOOTAGE. Vertical 9:16.",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "reference_use": "Use the first attached image only for Brandon's exact identity, wardrobe and her own garage gym. Use the second attached image only as a composition reference for the camera position, framing and the action; do not copy its older man and woman, aprons, kitchen, marble counter, exam room, framed certificates or the caption text.",
  "identity_main": "The exact fictional AI character holistic.brandon: Black mixed-race American woman around thirty, athletic and toned, medium light-brown skin with light freckles across the nose and cheeks, dark brown eyes, defined eyebrows, full lips, hair in tight cornrows that turn into long loose braids falling over both shoulders, finished with small wooden and gold beads, a black floral blackwork tattoo sleeve on her right arm, a small line tattoo on her left upper arm and small fine-line tattoos on her chest near the collarbones. She reads as an ordinary anonymous American fitness coach, not resembling anyone famous.",
  "wardrobe": "Plain white ribbed tank top with nothing printed or written on it, loose black training shorts ending at mid-thigh, a thin gold chain with a small gold cross pendant and small stud earrings.",
  "scene": "Her own garage gym, the same room as the reference: a white-painted concrete block wall and a dark wooden slat ceiling, a red neon sign reading TRAIN PRAY REPEAT on the wall at the left, a whiteboard with handwritten black marker reading STAY READY. STAY DISCIPLINED. on the right, and a small American flag pinned above the whiteboard, discreet but clearly visible and in focus. The background is reduced by framing, never by blur.",
  "prop": "A clear glass mixing bowl with milky white liquid in the center of the black table in front of her, very close to the lens, a squeezed lemon half and a metal measuring spoon beside it. Her right hand holds the glass dropper of a small amber dropper bottle of coconut oil above the bowl.",
  "posture": "Brandon stands behind the black table in front of her, leaning forward over it, seen from the waist up.",
  "composition": "Close shot from just above the table: the phone lens is about 40 centimeters from the bowl, which fills about 25 percent of the frame in the lower center, closer to the camera than her face; her head and torso fill the upper part. Nothing else is on the table. The background is reduced by framing, never by blur.",
  "camera": "phone held just above the table edge at chest height about 40 centimeters from the bowl, standard 1x lens tilted slightly down",
  "lighting": "Neutral overcast daylight from a large window out of frame, soft even light on her face, hands and skin with no harsh shadows. The red neon glows on the wall but does not tint anyone's skin.",
  "state": "Start frame: a drop of oil hangs from the tip of the dropper. Brandon is caught mid-sentence, lips naturally parted, animated expression, looking straight into the lens.",
  "realism": "Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday reality, background fully in focus, everything in sharp focus, no AI polish, no beauty smoothing.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no studio, no plastic-looking skin, no extra fingers, no third hand, no blur, no bokeh, no warm orange color cast, no yellow tint, no golden glow, no golden hour light, no sunset, no HDR, no cinematic lighting, no de-aging, no beauty smoothing, no visible phone, no apron, no older man, no kitchen cabinets, no white marble counter, no framed certificates, no silver cross, no white coat, no second person, no readable lettering on the bowl, spoon or dropper bottle"
}
```

### K05 · T5, protocolo, mexendo a pasta · anexar ÂNCORA HOLISTIC BRANDON + FRAME DO MODELO

```text
K05
{
  "format": "IMPORTANT: THIS IS IPHONE FOOTAGE. Vertical 9:16.",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "reference_use": "Use the first attached image only for Brandon's exact identity, wardrobe and her own garage gym. Use the second attached image only as a composition reference for the camera position, framing and the action; do not copy its older man and woman, aprons, kitchen, marble counter, exam room, framed certificates or the caption text.",
  "identity_main": "The exact fictional AI character holistic.brandon: Black mixed-race American woman around thirty, athletic and toned, medium light-brown skin with light freckles across the nose and cheeks, dark brown eyes, defined eyebrows, full lips, hair in tight cornrows that turn into long loose braids falling over both shoulders, finished with small wooden and gold beads, a black floral blackwork tattoo sleeve on her right arm, a small line tattoo on her left upper arm and small fine-line tattoos on her chest near the collarbones. She reads as an ordinary anonymous American fitness coach, not resembling anyone famous.",
  "wardrobe": "Plain white ribbed tank top with nothing printed or written on it, loose black training shorts ending at mid-thigh, a thin gold chain with a small gold cross pendant and small stud earrings.",
  "scene": "Her own garage gym, the same room as the reference: a white-painted concrete block wall and a dark wooden slat ceiling, a red neon sign reading TRAIN PRAY REPEAT on the wall at the left, a whiteboard with handwritten black marker reading STAY READY. STAY DISCIPLINED. on the right, and a small American flag pinned above the whiteboard, discreet but clearly visible and in focus. The background is reduced by framing, never by blur.",
  "prop": "A clear glass mixing bowl full of thick white paste in the center of the black table in front of her, very close to the lens, two squeezed lemon halves at its left. Her right hand stirs the paste with a metal spoon; her left hand holds the rim of the bowl.",
  "posture": "Brandon stands behind the black table in front of her, leaning forward over it, seen from the waist up.",
  "composition": "Close shot from just above the table: the phone lens is about 40 centimeters from the bowl, which fills about 25 percent of the frame in the lower center, closer to the camera than her face; her head and torso fill the upper part. Nothing else is on the table. The background is reduced by framing, never by blur.",
  "camera": "phone held just above the table edge at chest height about 40 centimeters from the bowl, standard 1x lens tilted slightly down",
  "lighting": "Neutral overcast daylight from a large window out of frame, soft even light on her face, hands and skin with no harsh shadows. The red neon glows on the wall but does not tint anyone's skin.",
  "state": "Start frame: the spoon is mid-stir in the paste. Brandon is caught mid-sentence, lips naturally parted, animated expression, looking straight into the lens.",
  "realism": "Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday reality, background fully in focus, everything in sharp focus, no AI polish, no beauty smoothing.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no studio, no plastic-looking skin, no extra fingers, no third hand, no blur, no bokeh, no warm orange color cast, no yellow tint, no golden glow, no golden hour light, no sunset, no HDR, no cinematic lighting, no de-aging, no beauty smoothing, no visible phone, no apron, no older man, no kitchen cabinets, no white marble counter, no framed certificates, no silver cross, no white coat, no second person, no readable lettering on the bowl, spoon or dropper bottle"
}
```

### K06 · T6, resultado, a tigela erguida · anexar ÂNCORA HOLISTIC BRANDON + FRAME DO MODELO

```text
K06
{
  "format": "IMPORTANT: THIS IS IPHONE FOOTAGE. Vertical 9:16.",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "reference_use": "Use the first attached image only for Brandon's exact identity, wardrobe and her own garage gym. Use the second attached image only as a composition reference for the camera position, framing and the action; do not copy its older man and woman, aprons, kitchen, marble counter, exam room, framed certificates or the caption text.",
  "identity_main": "The exact fictional AI character holistic.brandon: Black mixed-race American woman around thirty, athletic and toned, medium light-brown skin with light freckles across the nose and cheeks, dark brown eyes, defined eyebrows, full lips, hair in tight cornrows that turn into long loose braids falling over both shoulders, finished with small wooden and gold beads, a black floral blackwork tattoo sleeve on her right arm, a small line tattoo on her left upper arm and small fine-line tattoos on her chest near the collarbones. She reads as an ordinary anonymous American fitness coach, not resembling anyone famous.",
  "wardrobe": "Plain white ribbed tank top with nothing printed or written on it, loose black training shorts ending at mid-thigh, a thin gold chain with a small gold cross pendant and small stud earrings.",
  "scene": "Her own garage gym, the same room as the reference: a white-painted concrete block wall and a dark wooden slat ceiling, a red neon sign reading TRAIN PRAY REPEAT on the wall at the left, a whiteboard with handwritten black marker reading STAY READY. STAY DISCIPLINED. on the right, and a small American flag pinned above the whiteboard, discreet but clearly visible and in focus. The background is reduced by framing, never by blur.",
  "prop": "With both hands she holds a clear glass mixing bowl full of thick white paste with a metal spoon in it, raised and tilted toward the lens; on the table below, a lemon half, a metal measuring spoon and a small amber dropper bottle.",
  "posture": "Brandon stands behind the black table in front of her, seen from the waist up, holding the bowl toward the camera.",
  "composition": "Close shot from chest height: the phone lens is about 30 centimeters from the bowl, which fills about 30 percent of the frame in the lower center, closer to the camera than her face; her face fills the upper part. The background is reduced by framing, never by blur.",
  "camera": "phone held at chest height about 30 centimeters from the bowl, standard 1x lens, level",
  "lighting": "Neutral overcast daylight from a large window out of frame, soft even light on her face, hands and skin with no harsh shadows. The red neon glows on the wall but does not tint anyone's skin.",
  "state": "Start frame: the paste is clearly visible inside the tilted bowl. Brandon is caught mid-sentence, lips naturally parted, animated expression, looking straight into the lens, relieved.",
  "realism": "Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday reality, background fully in focus, everything in sharp focus, no AI polish, no beauty smoothing.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no studio, no plastic-looking skin, no extra fingers, no third hand, no blur, no bokeh, no warm orange color cast, no yellow tint, no golden glow, no golden hour light, no sunset, no HDR, no cinematic lighting, no de-aging, no beauty smoothing, no visible phone, no apron, no older man, no kitchen cabinets, no white marble counter, no framed certificates, no silver cross, no white coat, no second person, no readable lettering on the bowl, spoon or dropper bottle"
}
```

### K07 · T7, ponte, a superfície · anexar ÂNCORA HOLISTIC BRANDON + FRAME DO MODELO

```text
K07
{
  "format": "IMPORTANT: THIS IS IPHONE FOOTAGE. Vertical 9:16.",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "reference_use": "Use the first attached image only for Brandon's exact identity, wardrobe and her own garage gym. Use the second attached image only as a composition reference for the camera position, framing and the action; do not copy its older man and woman, aprons, kitchen, marble counter, exam room, framed certificates or the caption text.",
  "identity_main": "The exact fictional AI character holistic.brandon: Black mixed-race American woman around thirty, athletic and toned, medium light-brown skin with light freckles across the nose and cheeks, dark brown eyes, defined eyebrows, full lips, hair in tight cornrows that turn into long loose braids falling over both shoulders, finished with small wooden and gold beads, a black floral blackwork tattoo sleeve on her right arm, a small line tattoo on her left upper arm and small fine-line tattoos on her chest near the collarbones. She reads as an ordinary anonymous American fitness coach, not resembling anyone famous.",
  "wardrobe": "Plain white ribbed tank top with nothing printed or written on it, loose black training shorts ending at mid-thigh, a thin gold chain with a small gold cross pendant and small stud earrings.",
  "scene": "Her own garage gym, the same room as the reference: a white-painted concrete block wall and a dark wooden slat ceiling, a red neon sign reading TRAIN PRAY REPEAT on the wall at the left, a whiteboard with handwritten black marker reading STAY READY. STAY DISCIPLINED. on the right, and a small American flag pinned above the whiteboard, discreet but clearly visible and in focus. The background is reduced by framing, never by blur.",
  "prop": "A clear glass mixing bowl full of thick white paste with a metal spoon resting in it, standing still on the black table in front of her; her right index finger points at the paste.",
  "posture": "Brandon stands behind the black table in front of her, seen from the waist up, both forearms near the table edge.",
  "composition": "Straight-on medium shot from table height: the phone lens is about 45 centimeters from the bowl, which sits in the lower left and fills about 20 percent of the frame, closer to the camera than her face; her face and shoulders fill the upper half. Nothing else is on the table. The background is reduced by framing, never by blur.",
  "camera": "phone propped at table height about 45 centimeters from the bowl, standard 1x lens tilted slightly up",
  "lighting": "Neutral overcast daylight from a large window out of frame, soft even light on her face, hands and skin with no harsh shadows. The red neon glows on the wall but does not tint anyone's skin.",
  "state": "Start frame: Brandon is caught mid-sentence, lips naturally parted, animated expression, looking straight into the lens, serious.",
  "realism": "Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday reality, background fully in focus, everything in sharp focus, no AI polish, no beauty smoothing.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no studio, no plastic-looking skin, no extra fingers, no third hand, no blur, no bokeh, no warm orange color cast, no yellow tint, no golden glow, no golden hour light, no sunset, no HDR, no cinematic lighting, no de-aging, no beauty smoothing, no visible phone, no apron, no older man, no kitchen cabinets, no white marble counter, no framed certificates, no silver cross, no white coat, no second person, no readable lettering on the bowl, spoon or dropper bottle"
}
```

### K08 · T8, mecanismo, causa e consequência · anexar ÂNCORA HOLISTIC BRANDON + FRAME DO MODELO

```text
K08
{
  "format": "IMPORTANT: THIS IS IPHONE FOOTAGE. Vertical 9:16.",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "reference_use": "Use the first attached image only for Brandon's exact identity, wardrobe and her own garage gym. Use the second attached image only as a composition reference for the camera position, framing and the action; do not copy its older man and woman, aprons, kitchen, marble counter, exam room, framed certificates or the caption text.",
  "identity_main": "The exact fictional AI character holistic.brandon: Black mixed-race American woman around thirty, athletic and toned, medium light-brown skin with light freckles across the nose and cheeks, dark brown eyes, defined eyebrows, full lips, hair in tight cornrows that turn into long loose braids falling over both shoulders, finished with small wooden and gold beads, a black floral blackwork tattoo sleeve on her right arm, a small line tattoo on her left upper arm and small fine-line tattoos on her chest near the collarbones. She reads as an ordinary anonymous American fitness coach, not resembling anyone famous.",
  "wardrobe": "Plain white ribbed tank top with nothing printed or written on it, loose black training shorts ending at mid-thigh, a thin gold chain with a small gold cross pendant and small stud earrings.",
  "scene": "Her own garage gym, the same room as the reference: a white-painted concrete block wall and a dark wooden slat ceiling, a red neon sign reading TRAIN PRAY REPEAT on the wall at the left, a whiteboard with handwritten black marker reading STAY READY. STAY DISCIPLINED. on the right, and a small American flag pinned above the whiteboard, discreet but clearly visible and in focus. The background is reduced by framing, never by blur.",
  "prop": "A clear glass mixing bowl full of thick white paste with a metal spoon resting in it, standing still on the black table in front of her; her left hand is open in a small explaining gesture.",
  "posture": "Brandon stands behind the black table in front of her, seen from the waist up, her right hand open on her own chest.",
  "composition": "Straight-on medium shot from table height: the phone lens is about 45 centimeters from the bowl, which sits in the lower left and fills about 20 percent of the frame, closer to the camera than her face; her face and shoulders fill the upper half. Nothing else is on the table. The background is reduced by framing, never by blur.",
  "camera": "phone propped at table height about 45 centimeters from the bowl, standard 1x lens tilted slightly up",
  "lighting": "Neutral overcast daylight from a large window out of frame, soft even light on her face, hands and skin with no harsh shadows. The red neon glows on the wall but does not tint anyone's skin.",
  "state": "Start frame: Brandon is caught mid-sentence, lips naturally parted, animated expression, looking straight into the lens, convinced.",
  "realism": "Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday reality, background fully in focus, everything in sharp focus, no AI polish, no beauty smoothing.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no studio, no plastic-looking skin, no extra fingers, no third hand, no blur, no bokeh, no warm orange color cast, no yellow tint, no golden glow, no golden hour light, no sunset, no HDR, no cinematic lighting, no de-aging, no beauty smoothing, no visible phone, no apron, no older man, no kitchen cabinets, no white marble counter, no framed certificates, no silver cross, no white coat, no second person, no readable lettering on the bowl, spoon or dropper bottle"
}
```

### K09 · T9, a saída, tigela de lado · anexar ÂNCORA HOLISTIC BRANDON + FRAME DO MODELO

```text
K09
{
  "format": "IMPORTANT: THIS IS IPHONE FOOTAGE. Vertical 9:16.",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "reference_use": "Use the first attached image only for Brandon's exact identity, wardrobe and her own garage gym. Use the second attached image only as a composition reference for the camera position, framing and the action; do not copy its older man and woman, aprons, kitchen, marble counter, exam room, framed certificates or the caption text.",
  "identity_main": "The exact fictional AI character holistic.brandon: Black mixed-race American woman around thirty, athletic and toned, medium light-brown skin with light freckles across the nose and cheeks, dark brown eyes, defined eyebrows, full lips, hair in tight cornrows that turn into long loose braids falling over both shoulders, finished with small wooden and gold beads, a black floral blackwork tattoo sleeve on her right arm, a small line tattoo on her left upper arm and small fine-line tattoos on her chest near the collarbones. She reads as an ordinary anonymous American fitness coach, not resembling anyone famous.",
  "wardrobe": "Plain white ribbed tank top with nothing printed or written on it, loose black training shorts ending at mid-thigh, a thin gold chain with a small gold cross pendant and small stud earrings.",
  "scene": "Her own garage gym, the same room as the reference: a white-painted concrete block wall and a dark wooden slat ceiling, a red neon sign reading TRAIN PRAY REPEAT on the wall at the left, a whiteboard with handwritten black marker reading STAY READY. STAY DISCIPLINED. on the right, and a small American flag pinned above the whiteboard, discreet but clearly visible and in focus. The background is reduced by framing, never by blur.",
  "prop": "A clear glass mixing bowl full of thick white paste with a metal spoon resting in it, on the black table in front of her; her right hand rests on the rim of the bowl, about to slide it aside.",
  "posture": "Brandon stands behind the black table in front of her, seen from the waist up, leaning slightly toward the lens.",
  "composition": "Straight-on medium shot from table height: the phone lens is about 45 centimeters from the bowl, which sits in the lower left and fills about 20 percent of the frame, closer to the camera than her face; her face and shoulders fill the upper half. Nothing else is on the table. The background is reduced by framing, never by blur.",
  "camera": "phone propped at table height about 45 centimeters from the bowl, standard 1x lens tilted slightly up",
  "lighting": "Neutral overcast daylight from a large window out of frame, soft even light on her face, hands and skin with no harsh shadows. The red neon glows on the wall but does not tint anyone's skin.",
  "state": "Start frame: Brandon is caught mid-sentence, lips naturally parted, animated expression, looking straight into the lens, firm.",
  "realism": "Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday reality, background fully in focus, everything in sharp focus, no AI polish, no beauty smoothing.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no studio, no plastic-looking skin, no extra fingers, no third hand, no blur, no bokeh, no warm orange color cast, no yellow tint, no golden glow, no golden hour light, no sunset, no HDR, no cinematic lighting, no de-aging, no beauty smoothing, no visible phone, no apron, no older man, no kitchen cabinets, no white marble counter, no framed certificates, no silver cross, no white coat, no second person, no readable lettering on the bowl, spoon or dropper bottle"
}
```

### K10 · T10, pote sobe no nome · anexar ÂNCORA HOLISTIC BRANDON + FRAME DO MODELO + FOTO DO POTE

```text
K10
{
  "format": "IMPORTANT: THIS IS IPHONE FOOTAGE. Vertical 9:16.",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "reference_use": "Use the first attached image only for Brandon's exact identity, wardrobe and her own garage gym. Use the second attached image only as a composition reference for the camera position, framing and the action; do not copy its older man and woman, aprons, kitchen, marble counter, exam room, framed certificates or the caption text. Use the third attached image only for the exact look of the front jar and its label; ignore the MADE IN USA banner, the second jar with the Supplement Facts panel and the loose gummies.",
  "identity_main": "The exact fictional AI character holistic.brandon: Black mixed-race American woman around thirty, athletic and toned, medium light-brown skin with light freckles across the nose and cheeks, dark brown eyes, defined eyebrows, full lips, hair in tight cornrows that turn into long loose braids falling over both shoulders, finished with small wooden and gold beads, a black floral blackwork tattoo sleeve on her right arm, a small line tattoo on her left upper arm and small fine-line tattoos on her chest near the collarbones. She reads as an ordinary anonymous American fitness coach, not resembling anyone famous.",
  "wardrobe": "Plain white ribbed tank top with nothing printed or written on it, loose black training shorts ending at mid-thigh, a thin gold chain with a small gold cross pendant and small stud earrings.",
  "scene": "Her own garage gym, the same room as the reference: a white-painted concrete block wall and a dark wooden slat ceiling, a red neon sign reading TRAIN PRAY REPEAT on the wall at the left, a whiteboard with handwritten black marker reading STAY READY. STAY DISCIPLINED. on the right, and a small American flag pinned above the whiteboard, discreet but clearly visible and in focus. The background is reduced by framing, never by blur.",
  "prop": "Raised with both hands in front of her chest, she holds the Natural Rems Sea Moss Gummies jar exactly as in the attached product photo: a short wide jar of dark amber plastic with a black screw cap, a pale sage-green label with dark green text, the Natural Rems logo with three leaves at the top, the big title Sea Moss Gummies, a pill-shaped badge reading 6000 MG | 16-IN-1, the line GREEN APPLE FLAVOR, two columns of dark green ingredient pills, green seaweed illustrations on the sides and a small 30 Gummies badge. The label is turned straight to the lens and fully readable, her fingers only on the sides of the jar.",
  "posture": "Brandon stands behind the black table in front of her, seen from the waist up, holding the jar toward the camera.",
  "composition": "Straight-on medium shot from table height: the phone lens is about 40 centimeters from the jar, which fills about 25 percent of the frame in the lower center, closer to the camera than her face; her face and shoulders fill the upper half. The table is empty. The background is reduced by framing, never by blur.",
  "camera": "phone propped at table height about 40 centimeters from the jar, standard 1x lens, level",
  "lighting": "Neutral overcast daylight from a large window out of frame, soft even light on her face, hands and skin with no harsh shadows. The red neon glows on the wall but does not tint anyone's skin.",
  "state": "Start frame: Brandon is smiling and caught mid-sentence, lips naturally parted, animated expression, looking straight into the lens.",
  "realism": "Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday reality, background fully in focus, everything in sharp focus, no AI polish, no beauty smoothing.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no studio, no plastic-looking skin, no extra fingers, no third hand, no blur, no bokeh, no warm orange color cast, no yellow tint, no golden glow, no golden hour light, no sunset, no HDR, no cinematic lighting, no de-aging, no beauty smoothing, no visible phone, no apron, no older man, no kitchen cabinets, no white marble counter, no framed certificates, no silver cross, no white coat, no second person, no second jar, no loose gummies, no banner on the jar, no fingers over the label"
}
```

### K11 · T11, CTA, pote parado e legível · anexar ÂNCORA HOLISTIC BRANDON + FRAME DO MODELO + FOTO DO POTE

```text
K11
{
  "format": "IMPORTANT: THIS IS IPHONE FOOTAGE. Vertical 9:16.",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "reference_use": "Use the first attached image only for Brandon's exact identity, wardrobe and her own garage gym. Use the second attached image only as a composition reference for the camera position, framing and the action; do not copy its older man and woman, aprons, kitchen, marble counter, exam room, framed certificates or the caption text. Use the third attached image only for the exact look of the front jar and its label; ignore the MADE IN USA banner, the second jar with the Supplement Facts panel and the loose gummies.",
  "identity_main": "The exact fictional AI character holistic.brandon: Black mixed-race American woman around thirty, athletic and toned, medium light-brown skin with light freckles across the nose and cheeks, dark brown eyes, defined eyebrows, full lips, hair in tight cornrows that turn into long loose braids falling over both shoulders, finished with small wooden and gold beads, a black floral blackwork tattoo sleeve on her right arm, a small line tattoo on her left upper arm and small fine-line tattoos on her chest near the collarbones. She reads as an ordinary anonymous American fitness coach, not resembling anyone famous.",
  "wardrobe": "Plain white ribbed tank top with nothing printed or written on it, loose black training shorts ending at mid-thigh, a thin gold chain with a small gold cross pendant and small stud earrings.",
  "scene": "Her own garage gym, the same room as the reference: a white-painted concrete block wall and a dark wooden slat ceiling, a red neon sign reading TRAIN PRAY REPEAT on the wall at the left, a whiteboard with handwritten black marker reading STAY READY. STAY DISCIPLINED. on the right, and a small American flag pinned above the whiteboard, discreet but clearly visible and in focus. The background is reduced by framing, never by blur.",
  "prop": "Perfectly still with both hands in front of her chest, centered, she holds the Natural Rems Sea Moss Gummies jar exactly as in the attached product photo: a short wide jar of dark amber plastic with a black screw cap, a pale sage-green label with dark green text, the Natural Rems logo with three leaves at the top, the big title Sea Moss Gummies, a pill-shaped badge reading 6000 MG | 16-IN-1, the line GREEN APPLE FLAVOR, two columns of dark green ingredient pills, green seaweed illustrations on the sides and a small 30 Gummies badge. The label is turned straight to the lens, fully readable and with nothing covering it.",
  "posture": "Brandon stands behind the black table in front of her, seen from the chest up, holding the jar toward the camera.",
  "composition": "The tightest shot of the video, straight-on from chest height: the phone lens is about 35 centimeters from the jar, which fills about 30 percent of the frame in the lower center, closer to the camera than her face; her face fills the upper half. The background is reduced by framing, never by blur.",
  "camera": "phone propped at chest height, standard 1x lens, level",
  "lighting": "Neutral overcast daylight from a large window out of frame, soft even light on her face, hands and skin with no harsh shadows. The red neon glows on the wall but does not tint anyone's skin.",
  "state": "Start frame: Brandon is caught mid-sentence, lips naturally parted, animated expression, looking straight into the lens, clear and calm.",
  "realism": "Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday reality, background fully in focus, everything in sharp focus, no AI polish, no beauty smoothing.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no studio, no plastic-looking skin, no extra fingers, no third hand, no blur, no bokeh, no warm orange color cast, no yellow tint, no golden glow, no golden hour light, no sunset, no HDR, no cinematic lighting, no de-aging, no beauty smoothing, no visible phone, no apron, no older man, no kitchen cabinets, no white marble counter, no framed certificates, no silver cross, no white coat, no second person, no second jar, no loose gummies, no banner on the jar, no fingers over the label"
}
```

## 3. PROMPTS DE VÍDEO (um bloco por V)

### V01 · T1 · frame inicial = a imagem que você deixou no K01

```text
V01
a avatar Brandon, mulher, fala em inglês com sotaque americano de uma mulher negra americana, voz feminina clara e firme de uma mulher de uns trinta anos, entonação baixa e séria, como quem conta um segredo de uma cliente, voz autêntica, como se exigisse ser ouvida, a seguinte frase: "She started hiding her legs because of her dark inner thighs."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Brandon, ajoelhada ao lado do banco, passa a mão pela coxa da cliente e aponta a mancha escura com o indicador, olhando para a câmera. A cliente fica deitada e em silêncio. Ela diz a frase em ritmo natural logo no começo e a ação continua em silêncio até o fim.

câmera: leve handheld, baixa, bem perto da coxa

som ambiente: box de treino em casa, tranquilo, sem música
```

### V02 · T2 · frame inicial = a imagem que você deixou no K02

```text
V02
a avatar Brandon, mulher, fala em inglês com sotaque americano de uma mulher negra americana, voz feminina clara e firme de uma mulher de uns trinta anos, entonação de virada, curiosa, com um meio sorriso, voz autêntica, como se exigisse ser ouvida, a seguinte frase: "Then she found this."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Brandon vira a mão aberta, palma para cima, na direção da câmera; a cliente olha para a câmera com um meio sorriso e fica em silêncio. A coxa não muda. Ela diz a frase em ritmo natural logo no começo e a ação continua em silêncio até o fim.

câmera: leve handheld, baixa, bem perto da coxa

som ambiente: box de treino em casa, tranquilo, sem música
```

### V03 · T3 · frame inicial = a imagem que você deixou no K03

```text
V03
a avatar Brandon, mulher, fala em inglês com sotaque americano de uma mulher negra americana, voz feminina clara e firme de uma mulher de uns trinta anos, entonação calma e didática, voz autêntica, como se exigisse ser ouvida, a seguinte frase: "Mix a spoonful of baking soda with the juice of half a lemon"

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Brandon, inclinada sobre a mesa, espreme o meio limão dentro da tigela de bicarbonato.

câmera: leve handheld

som ambiente: box de treino em casa, tranquilo, limão pingando na tigela, sem música
```

### V04 · T4 · frame inicial = a imagem que você deixou no K04

```text
V04
a avatar Brandon, mulher, fala em inglês com sotaque americano de uma mulher negra americana, voz feminina clara e firme de uma mulher de uns trinta anos, entonação calma e didática, voz autêntica, como se exigisse ser ouvida, a seguinte frase: "and two drops of coconut oil until it forms a paste."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Brandon pinga duas gotas de óleo de coco com o conta-gotas dentro da tigela. Ela diz a frase em ritmo natural logo no começo e a ação continua em silêncio até o fim.

câmera: leve handheld

som ambiente: box de treino em casa, tranquilo, gotas caindo na tigela, sem música
```

### V05 · T5 · frame inicial = a imagem que você deixou no K05

```text
V05
a avatar Brandon, mulher, fala em inglês com sotaque americano de uma mulher negra americana, voz feminina clara e firme de uma mulher de uns trinta anos, entonação calma e didática, firme nos números, voz autêntica, como se exigisse ser ouvida, a seguinte frase: "Rub it in gentle circles on your inner thighs for thirty seconds. Let it sit five minutes, then rinse with cold water."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Brandon mexe a pasta com a colher, mostra o movimento em círculos com a ponta dos dedos e abre cinco dedos no five.

câmera: leve handheld, com leve push-in no meio e volta ao plano

som ambiente: box de treino em casa, tranquilo, colher raspando o vidro, sem música
```

### V06 · T6 · frame inicial = a imagem que você deixou no K06

```text
V06
a avatar Brandon, mulher, fala em inglês com sotaque americano de uma mulher negra americana, voz feminina clara e firme de uma mulher de uns trinta anos, entonação aliviada e calorosa, voz autêntica, como se exigisse ser ouvida, a seguinte frase: "The skin breathes again. What took years to darken can start to look lighter in days."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Brandon ergue a tigela de pasta na direção da câmera, depois abaixa e gesticula com a mão livre.

câmera: fixa

som ambiente: box de treino em casa, tranquilo, sem música
```

### V07 · T7 · frame inicial = a imagem que você deixou no K07

```text
V07
a avatar Brandon, mulher, fala em inglês com sotaque americano de uma mulher negra americana, voz feminina clara e firme de uma mulher de uns trinta anos, entonação séria, como quem avisa, voz autêntica, como se exigisse ser ouvida, a seguinte frase: "But the paste only works on the surface, and that darkening keeps coming back when your skin is inflamed underneath."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Brandon, com a tigela parada na mesa, aponta para a pasta e depois abre as mãos.

câmera: fixa

som ambiente: box de treino em casa, tranquilo, sem música
```

### V08 · T8 · frame inicial = a imagem que você deixou no K08

```text
V08
a avatar Brandon, mulher, fala em inglês com sotaque americano de uma mulher negra americana, voz feminina clara e firme de uma mulher de uns trinta anos, entonação didática e convicta, marcando consequence, voz autêntica, como se exigisse ser ouvida, a seguinte frase: "The darkening was never the problem, it's the consequence. Skin under constant inflammation makes extra pigment to protect itself, and it keeps going darker until that stops."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Brandon aponta a tigela no problem e encosta a mão aberta no próprio peito no protect itself.

câmera: fixa

som ambiente: box de treino em casa, tranquilo, sem música
```

### V09 · T9 · frame inicial = a imagem que você deixou no K09

```text
V09
a avatar Brandon, mulher, fala em inglês com sotaque americano de uma mulher negra americana, voz feminina clara e firme de uma mulher de uns trinta anos, entonação firme e segura, voz autêntica, como se exigisse ser ouvida, a seguinte frase: "Calm what's happening underneath, and the skin has no reason to keep making that pigment. That's the part no paste can reach."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Brandon empurra a tigela de pasta devagar para o lado, abrindo espaço na mesa.

câmera: fixa

som ambiente: box de treino em casa, tranquilo, sem música
```

### V10 · T10 · frame inicial = a imagem que você deixou no K10

```text
V10
a avatar Brandon, mulher, fala em inglês com sotaque americano de uma mulher negra americana, voz feminina clara e firme de uma mulher de uns trinta anos, entonação calorosa e confiante, voz autêntica, como se exigisse ser ouvida, a seguinte frase: "That's why I have my clients add Natural Rems Sea Moss. Turmeric, ginger and vitamin C to support your skin from the inside, in one green apple gummy."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Brandon segura o pote de Natural Rems Sea Moss com as duas mãos na altura do peito, rótulo de frente para a câmera, e aproxima o pote um pouco da câmera quando diz o nome.

câmera: fixa

som ambiente: box de treino em casa, tranquilo, sem música
```

### V11 · T11 · frame inicial = a imagem que você deixou no K11

```text
V11
a avatar Brandon, mulher, fala em inglês com sotaque americano de uma mulher negra americana, voz feminina clara e firme de uma mulher de uns trinta anos, entonação clara e pausada, dizendo Natural Rems Sea Moss devagar e por inteiro, voz autêntica, como se exigisse ser ouvida, a seguinte frase: "Search Natural Rems Sea Moss on Amazon. Or you can just tap the link I left right down below, in the caption of this video."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Brandon segura o pote parado com as duas mãos, rótulo de frente e legível, sem nada cobrindo, do começo ao fim; só o rosto e a boca se mexem.

câmera: fixa

som ambiente: box de treino em casa, tranquilo, sem música
```

## 4. Montagem no CapCut

1. Clipes numerados na ordem: V01 a V11.
2. Cortar cada clipe no tempo da cena do modelo: V01 0,0 a 4,7 s; V02 4,7 a 6,2 s; V03 6,2 a 10,2 s; V04 10,2 a 14,0 s; V05 14,0 a 21,8 s; V06 21,8 a 28,8 s; V07 a fala inteira; V08 a fala inteira; V09 a fala inteira; V10 a fala inteira; V11 o CTA inteiro, sem corte.
3. Zero tempo morto: todo clipe começa já falando. Isolate Voice / Keep Vocal no áudio.
4. Nos V01, V02 e V04 (cenas curtas) a fala vem no começo; cortar logo depois da última palavra. O V03 termina sem ponto e o V04 continua a frase: emendar sem pausa.
5. V01 e V02 são o mesmo plano com corte seco entre eles, como no modelo; a coxa não muda de um para o outro.
6. V11 inteiro, sem corte e sem nada cobrindo o pote: é o CTA da marca (frasco parado e legível enquanto o nome é dito). O vídeo acaba nele.
7. Legenda de tela em inglês como no modelo: branca, grossa, palavra a palavra, no meio do quadro.
8. Sem Voice Changer: a voz vem do prompt de cada V.
9. Música só depois do gancho (a partir do V03), nunca no pré-gancho, entre -19 e -20 dB, fora da biblioteca do TikTok.
10. Rótulo pequeno `Synthetic performer` no canto de cima à esquerda, como no modelo.
11. Legenda do post: `#ad #syntheticperformer #naturalrems` na primeira linha e o link da Amazon logo abaixo; chave de conteúdo de IA ligada na plataforma.

## 5. Transcrição final por take

| Take | English | Português |
|---|---|---|
| T1 | She started hiding her legs because of her dark inner thighs. | Ela começou a esconder as pernas por causa da parte interna das coxas escura. |
| T2 | Then she found this. | Aí ela encontrou isto. |
| T3 | Mix a spoonful of baking soda with the juice of half a lemon | Misture uma colher de bicarbonato com o suco de meio limão |
| T4 | and two drops of coconut oil until it forms a paste. | e duas gotas de óleo de coco até formar uma pasta. |
| T5 | Rub it in gentle circles on your inner thighs for thirty seconds. Let it sit five minutes, then rinse with cold water. | Esfregue em círculos suaves na parte interna das coxas por trinta segundos. Deixe agir cinco minutos e depois enxágue com água fria. |
| T6 | The skin breathes again. What took years to darken can start to look lighter in days. | A pele volta a respirar. O que levou anos para escurecer pode começar a parecer mais claro em dias. |
| T7 | But the paste only works on the surface, and that darkening keeps coming back when your skin is inflamed underneath. | Mas a pasta só age na superfície, e esse escurecimento continua voltando quando a sua pele está inflamada por baixo. |
| T8 | The darkening was never the problem, it's the consequence. Skin under constant inflammation makes extra pigment to protect itself, and it keeps going darker until that stops. | O escurecimento nunca foi o problema, é a consequência. A pele sob inflamação constante produz pigmento a mais para se proteger, e continua escurecendo até isso parar. |
| T9 | Calm what's happening underneath, and the skin has no reason to keep making that pigment. That's the part no paste can reach. | Acalme o que está acontecendo por baixo, e a pele não tem mais motivo para continuar produzindo esse pigmento. Essa é a parte que nenhuma pasta alcança. |
| T10 | That's why I have my clients add Natural Rems Sea Moss. Turmeric, ginger and vitamin C to support your skin from the inside, in one green apple gummy. | É por isso que eu faço as minhas clientes acrescentarem o Natural Rems Sea Moss. Cúrcuma, gengibre e vitamina C para apoiar a sua pele por dentro, numa goma de maçã verde. |
| T11 | Search Natural Rems Sea Moss on Amazon. Or you can just tap the link I left right down below, in the caption of this video. | Procure Natural Rems Sea Moss na Amazon. Ou é só tocar no link que eu deixei aqui embaixo, na legenda deste vídeo. |

## 6. Roteiro final em inglês

1. She started hiding her legs because of her dark inner thighs.
2. Then she found this.
3. Mix a spoonful of baking soda with the juice of half a lemon
4. and two drops of coconut oil until it forms a paste.
5. Rub it in gentle circles on your inner thighs for thirty seconds. Let it sit five minutes, then rinse with cold water.
6. The skin breathes again. What took years to darken can start to look lighter in days.
7. But the paste only works on the surface, and that darkening keeps coming back when your skin is inflamed underneath.
8. The darkening was never the problem, it's the consequence. Skin under constant inflammation makes extra pigment to protect itself, and it keeps going darker until that stops.
9. Calm what's happening underneath, and the skin has no reason to keep making that pigment. That's the part no paste can reach.
10. That's why I have my clients add Natural Rems Sea Moss. Turmeric, ginger and vitamin C to support your skin from the inside, in one green apple gummy.
11. Search Natural Rems Sea Moss on Amazon. Or you can just tap the link I left right down below, in the caption of this video.

She started hiding her legs because of her dark inner thighs. Then she found this. Mix a spoonful of baking soda with the juice of half a lemon and two drops of coconut oil until it forms a paste. Rub it in gentle circles on your inner thighs for thirty seconds. Let it sit five minutes, then rinse with cold water. The skin breathes again. What took years to darken can start to look lighter in days. But the paste only works on the surface, and that darkening keeps coming back when your skin is inflamed underneath. The darkening was never the problem, it's the consequence. Skin under constant inflammation makes extra pigment to protect itself, and it keeps going darker until that stops. Calm what's happening underneath, and the skin has no reason to keep making that pigment. That's the part no paste can reach. That's why I have my clients add Natural Rems Sea Moss. Turmeric, ginger and vitamin C to support your skin from the inside, in one green apple gummy. Search Natural Rems Sea Moss on Amazon. Or you can just tap the link I left right down below, in the caption of this video.
