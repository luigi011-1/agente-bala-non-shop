# ENTREGA | Avery Knox | Auraly Taylon Branigan (sal na carteira)

Produção `auraly_taylon_branigan` · Ângulo 3 · GROWTH · vídeo modelo de avatar IA · rodada de VALIDAÇÃO · perfil AURALY

## 1. INSTRUÇÕES PARA A MEMÓRIA DO AGENTE · GOOGLE FLOW AI (v19)

Colar inteiro na memória do agente antes do primeiro K.

```text
Voce executa prompts finalizados dentro do Google Flow. Nao reescreva, traduza, resuma nem
altere a copy. Registre o perfil da producao antes de gerar qualquer asset. Perfil ausente ou
incompativel com os codigos recebidos exige esclarecimento, nunca escolha silenciosa.

### Perfis de execucao

| Configuracao | AURALY | CLASSICO (Angle 1/2) |
|---|---|---|
| Imagem | Nano Banana 2 | Nano Banana 2 |
| Formato | 9:16 vertical, imagem e video | 9:16 vertical, imagem e video |
| Referencia de imagem | Anchor em cena real do avatar ativo (ver secao abaixo) | Anchor do avatar ativo |
| Imagens por K | 4, com selecao manual | 4, com selecao manual (o operador apaga 3 e deixa 1) |
| Relacao K/V | Mapa explicito recebido com o pacote; um K pode alimentar varios V | Maior K menor ou igual ao numero de V |
| Video | Veo 3.1 Lite | Omni Flash, e somente ele |
| Prioridade | Lower Priority | Padrao do Omni Flash |
| Duracao por clipe | 8 segundos | 8 segundos |
| Variacoes por V | 1, um unico resultado por prompt | 1, um unico resultado por prompt |
| Anexo do video | INITIAL FRAME | INITIAL FRAME |
| Lote de video | Fechado, no maximo 7 codigos V | Fechado, no maximo 7 codigos V |

REGRA UNICA DE QUANTIDADE E FORMATO (v19, Luigi, 2026-10-05), vale em TODOS os perfis: **4 imagens por K,
1 video por V, e SEMPRE 9:16 vertical tanto na imagem quanto no video**. Antes de cada K e de cada V,
conferir a proporcao 9:16; nunca 16:9, 1:1 nem 4:5. Se a interface nao permitir 9:16, parar e avisar. Antes de cada V, colocar a quantidade de saida do video em 1; nunca gerar duas ou
mais versoes do mesmo V. Os valores Auraly reproduzem as travas de WORKFLOW_AURALY.md (modelo e
prioridade). Nunca transportar o modelo de video classico (Omni Flash) para Auraly. Um pacote historico com outro contrato nao autoriza alterar uma producao
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
Cada codigo V tem uma unica variacao (um resultado), gerada do frame selecionado.

CLASSICO: V usa o maior K disponivel cujo numero nao exceda o de V. Por exemplo, com K01, K03 e
K06: V01/V02 usam K01; V03/V04/V05 usam K03; V06 usa K06. Se nao houver K anterior ou igual,
parar. Nao adivinhar pela aparencia ou ordem da galeria. Cada V tem uma variacao, gerada no Omni
Flash a partir da UNICA imagem que o operador deixou naquele K.

### Videos em lotes fechados

1. Receber e registrar toda a fila V, sem executar tudo automaticamente.
2. Antes de cada V, conferir avatar, perfil e K indicado no MAPA K/V.
3. Usar a imagem exclusivamente como INITIAL FRAME, nunca Element, ingredient ou referencia de objeto.
4. Configurar o modelo do perfil: AURALY em Veo 3.1 Lite, Lower Priority, oito segundos, um
   unico resultado por V; CLASSICO somente em Omni Flash, oito segundos, um unico resultado por V.
5. Iniciar somente o primeiro lote de no maximo sete codigos V. O teto e de codigos, nao uma autorizacao para iniciar codigos adicionais por vaga liberada.
6. Esperar todos os codigos desse lote. Nao preencher vagas com o lote seguinte.
7. Informar concluidos, falhas e pendentes. Se houver pendentes, parar e aguardar `prossiga`.
8. Mesmo quando o lote terminar, esperar `prossiga` para iniciar o proximo lote.
9. Ao retomar, executar somente o trabalho pendente autorizado. Nunca reiniciar um V concluido
   sem pedido explicito. Distinguir o V que falhou dos que ja foram concluidos.
10. Se a interface nao permitir a configuracao requerida, informar a limitacao antes de mudar
    modelo, prioridade, quantidade, duracao ou modo de referencia.

A fala e literal. A acao continua o estado inicial da imagem. Manter camera e som indicados,
sem adicionar musica, legenda, traducao ou texto auxiliar por conta propria.

### Fechamento

Relatar arquivos gerados por avatar, K/V e variacao, com pendencias explicitas. Geracao de um
avatar nao conclui a fila inteira. Entrega de prompts, midia gerada, montagem e publicacao sao
marcos diferentes. Nunca declarar publicacao ou resultado comercial pela existencia de assets.
```

Checklist de envio: 32/32 aprovados (N/A: A1, A2, A7, A9 fiéis ao modelo; A10 growth sem produto; C3 a C7 sem segunda pessoa, selfie, frase curta repetida, cena atuada ou motion control)

Ficha: 2/2 K conferidos contra o frame do modelo, placar 14/14 cada (`FICHA_FRAMES.md`, GATE_VISUAL Parte 6)

## Anexos e mapa

- **Character sheet Avery Knox:** `producao/_ancoras/character_sheets/avery_knox_character_sheet.jpg` no K01 e no K02 (identidade e roupa).
- **Frame do modelo** do mesmo código: `input/frames_modelo/K01_modelo.png` no K01 e `K02_modelo.png` no K02 (cenário, ângulo e enquadramento).

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
V09: K02
V10: K02
V11: K02
V12: K02
V13: K02
V14: K02
V15: K02
V16: K02
V17: K02
V18: K02
```

## 2. PROMPTS DE IMAGEM

### K01 · T1, gancho, saleiro despejando sal na carteira aberta, macro das mãos na varanda · anexar CHARACTER SHEET + FRAME DO MODELO

```text
K01
{
  "format": "IMPORTANT: THIS IS IPHONE FOOTAGE. Vertical 9:16.",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "reference_use": "Use the first attached image (character sheet) only for Avery Knox's exact identity (face, skin, hair, body) and wardrobe; ignore its grey studio background. Use the second attached image (frame of the model video) as the reference for the setting, camera angle and framing; do not copy its person, clothes or on-screen text.",
  "identity_main": "The exact fictional AI character Avery Knox: white American woman around fifty-six, voluminous shaggy layered platinum-blonde hair with visible darker roots, brown eyes, fair skin with crow's feet and fine lines, everyday makeup with defined brows, mascara and pink lipstick. Only the hands and forearms appear in this shot.",
  "wardrobe": "White long-sleeve button-up shirt with a chest pocket and the cuffs rolled, medium-blue bootcut jeans, a large turquoise and silver squash-blossom necklace, several big turquoise rings and silver cuff bracelets set with turquoise on both wrists.",
  "scene": "The front porch of an ordinary American suburban house seen from just above a sturdy wooden bench with visible grain that fills the bottom of the frame: a white painted porch column in the middle behind the hands, a dark wood door frame and a stained wooden front door with a glass pane at the right edge, a woven doormat on the porch floor, a white flowering shrub in a dark pot at the left, and green garden shrubs and flagstone paving behind. A small American flag is tucked into the shrubs at the left, discreet but visible and in focus.",
  "prop": "In one of her fair hands with big turquoise rings and silver cuff bracelets, the cuffs of a white shirt rolled to the forearms, a navy blue cylindrical salt shaker with a plain white perforated lid and no label is tipped, a thin stream of coarse white salt pouring from its lid into a brown leather bifold wallet, plain, no logo, open with its card slots and inner pocket visible, which the other hand holds open from the right edge of the frame, thumb on the wallet's edge, a small pile of salt already at the bottom of the wallet.",
  "posture": "Only Avery Knox's hands and forearms are in the frame, entering from the right edge: one hand tips the shaker from the upper left, the other holds the wallet open in the lower middle. No face is visible.",
  "composition": "Macro of the hands. The wallet is in the lower middle of the frame, very close to the lens, about 12 inches from the lens, taking up about 10 percent of the frame; the navy shaker is in the upper left, about 10 inches from the lens, about 8 percent of the frame, the salt stream falling between them; both are the hero, large in frame, nothing else competing with them. The bench fills the bottom of the frame. Nothing else is in the foreground. The background is reduced by framing, never by blur.",
  "camera": "handheld phone at upper-chest height about 14 inches from the hands, 1x lens, tilted downward about 35 degrees, steady",
  "lighting": "Neutral overcast daylight outdoors, cool and even, soft light on the hands and the wallet, no harsh shadows and no dappled sun patches on the bench.",
  "state": "Start frame: the salt is already pouring in a thin stream from the shaker into the open wallet.",
  "realism": "Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday reality, background fully in focus, everything in sharp focus, no AI polish, no beauty smoothing.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no brand name or logo on the shaker or the wallet, no studio, no grey studio background, no plastic-looking human skin, no extra fingers, no third hand, no supernatural lighting, no blur, no bokeh, no artificial lighting, no warm orange color cast, no yellow tint on the skin, no golden glow, no golden hour light, no sunset, no sun flares, no de-aging, no beauty smoothing, no visible phone, no HDR, no cinematic lighting, no second person in frame, no tarot cards, no candles, no magic effects, no face, no second person, no salt spilled on the bench"
}
```

### K02 · T2 a T18, corpo, sentado na soleira da porta aberta com a carteira nas mãos · anexar CHARACTER SHEET + FRAME DO MODELO

```text
K02
{
  "format": "IMPORTANT: THIS IS IPHONE FOOTAGE. Vertical 9:16.",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "reference_use": "Use the first attached image (character sheet) only for Avery Knox's exact identity (face, skin, hair, body) and wardrobe; ignore its grey studio background. Use the second attached image (frame of the model video) as the reference for the setting, camera angle and framing; do not copy its person, clothes or on-screen text.",
  "identity_main": "The exact fictional AI character Avery Knox: white American woman around fifty-six, voluminous shaggy layered platinum-blonde hair with visible darker roots, brown eyes, fair skin with crow's feet and fine lines, everyday makeup with defined brows, mascara and pink lipstick.",
  "wardrobe": "White long-sleeve button-up shirt with a chest pocket and the cuffs rolled, medium-blue bootcut jeans, a large turquoise and silver squash-blossom necklace, several big turquoise rings and silver cuff bracelets set with turquoise on both wrists.",
  "scene": "The open front doorway of an ordinary American house seen from the porch: the avatar sits on the wooden threshold of the open front door, the dark wood door jamb at the left with green ivy climbing the white porch column at the far left, the open stained-wood front door at the right edge with a black iron lever handle, and behind the avatar through the doorway a living room with a window showing green trees outside and a table lamp switched off beside it, a framed map of the United States on the cream wall at the upper right above a wooden bookshelf full of books, and below the threshold a gray stone step and a woven doormat. A small American flag is tucked into the ivy on the column at the left, discreet but visible and in focus.",
  "prop": "Avery Knox holds a brown leather bifold wallet, plain, no logo, open with its card slots and inner pocket visible, empty, open in both hands at belly height, held forward toward the lens. A navy blue cylindrical salt shaker with a plain white perforated lid and no label stands upright on the wooden threshold at the lower left.",
  "posture": "Avery Knox sits on the wooden threshold of the open front door, leaning slightly forward with the elbows near the knees, holding the open wallet in both hands, looking straight into the lens.",
  "composition": "The open wallet is in the lower middle of the frame, about 30 inches from the lens, taking up about 4 percent of the frame, closer to the camera than her face, nothing else competing with it; the navy salt shaker stands at the lower left. Avery Knox is framed from the top of the head to mid-thigh, her face in the upper third. Nothing else is in the foreground. The background is reduced by framing, never by blur.",
  "camera": "phone resting at chest height about 3.5 feet off the porch floor and about four feet from the doorway, 1x lens, level, fixed",
  "lighting": "Neutral overcast daylight from a window, the outside clearly visible through the window, soft even light on the face with no harsh shadows.",
  "state": "Start frame: Avery Knox caught mid-sentence, lips naturally parted, serious intrigued expression, wallet held open.",
  "realism": "Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday reality, background fully in focus, everything in sharp focus, no AI polish, no beauty smoothing.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no brand name or logo on the shaker or the wallet, no studio, no grey studio background, no plastic-looking human skin, no extra fingers, no third hand, no supernatural lighting, no blur, no bokeh, no artificial lighting, no warm orange color cast, no yellow tint on the skin, no golden glow, no golden hour light, no sunset, no sun flares, no de-aging, no beauty smoothing, no visible phone, no HDR, no cinematic lighting, no second person in frame, no tarot cards, no candles, no magic effects, no salt on the wallet yet, no salt on the floor"
}
```

## 3. PROMPTS DE VÍDEO (um bloco por V)

### V01 · T1 · frame inicial = a imagem escolhida do K01

```text
V01
narração em off: a avatar Avery Knox, mulher, fala em inglês com sotaque americano texano carregado, voz feminina média, levemente rouca e calorosa de uma texana de cinquenta e seis anos, tom baixo e confidencial, como quem conta um segredo, voz autêntica, como se exigisse ser ouvida, a seguinte frase: "Put salt inside your wallet before you leave the house." Ninguém aparece falando em quadro, só as mãos.

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Sem lip sync: a fala é narração em off e nenhum rosto aparece no quadro.

o que acontece no vídeo: plano único contínuo, já em andamento: a mão de Avery Knox inclina o saleiro azul-escuro e o sal grosso cai em fio dentro da carteira marrom aberta, segurada pela outra mão; o fio de sal diminui e para perto do fim, deixando um montinho de sal no fundo da carteira, e as duas mãos ficam paradas até o fim.

câmera: plano único, sem cortes, câmera parada na altura do peito olhando para baixo

som ambiente: varanda residencial silenciosa, som do sal grosso caindo na carteira, sem música
```

### V02 · T2 · frame inicial = a imagem escolhida do K02

```text
V02
a avatar Avery Knox, mulher, fala em inglês com sotaque americano texano carregado, voz feminina média, levemente rouca e calorosa de uma texana de cinquenta e seis anos, séria e intrigante, voz autêntica, como se exigisse ser ouvida, a seguinte frase: "I know it sounds ridiculous, but you'll thank me for the rest of your life."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Avery Knox segura a carteira aberta com uma mão na altura da barriga, sentada na soleira da porta aberta. Avery Knox gesticula com a mão livre, pequenos gestos naturais, olhando direto para a lente. O saleiro azul-escuro continua parado na soleira, no canto inferior esquerdo.

câmera: fixa na altura do peito, sem movimento

som ambiente: varanda residencial silenciosa, sem música
```

### V03 · T3 · frame inicial = a imagem escolhida do K02

```text
V03
a avatar Avery Knox, mulher, fala em inglês com sotaque americano texano carregado, voz feminina média, levemente rouca e calorosa de uma texana de cinquenta e seis anos, convicta e intensa, voz autêntica, como se exigisse ser ouvida, a seguinte frase: "Keep your mouth shut after you watch this. Do not tell anyone. Not everyone is going to see this before this month ends."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Avery Knox segura a carteira aberta com uma mão na altura da barriga, sentada na soleira da porta aberta. Avery Knox gesticula com a mão livre, pequenos gestos naturais, olhando direto para a lente. O saleiro azul-escuro continua parado na soleira, no canto inferior esquerdo.

câmera: fixa na altura do peito, sem movimento

som ambiente: varanda residencial silenciosa, sem música
```

### V04 · T4 · frame inicial = a imagem escolhida do K02

```text
V04
a avatar Avery Knox, mulher, fala em inglês com sotaque americano texano carregado, voz feminina média, levemente rouca e calorosa de uma texana de cinquenta e seis anos, urgente e direta, voz autêntica, como se exigisse ser ouvida, a seguinte frase: "I do not know your name, but do not scroll. Because if this reached you today, it reached you as a final warning."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Avery Knox segura a carteira aberta com uma mão na altura da barriga, sentada na soleira da porta aberta. Avery Knox aponta para a lente com a mão livre. O saleiro azul-escuro continua parado na soleira, no canto inferior esquerdo.

câmera: fixa na altura do peito, sem movimento

som ambiente: varanda residencial silenciosa, sem música
```

### V05 · T5 · frame inicial = a imagem escolhida do K02

```text
V05
a avatar Avery Knox, mulher, fala em inglês com sotaque americano texano carregado, voz feminina média, levemente rouca e calorosa de uma texana de cinquenta e seis anos, solene e firme, voz autêntica, como se exigisse ser ouvida, a seguinte frase: "A powerful wave of prosperity, love and money is heading your way. Don't tell anyone, but the abundance portal has opened."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Avery Knox segura a carteira aberta com uma mão na altura da barriga, sentada na soleira da porta aberta. Avery Knox gesticula com a mão livre, pequenos gestos naturais, olhando direto para a lente. O saleiro azul-escuro continua parado na soleira, no canto inferior esquerdo.

câmera: fixa na altura do peito, sem movimento

som ambiente: varanda residencial silenciosa, sem música
```

### V06 · T6 · frame inicial = a imagem escolhida do K02

```text
V06
a avatar Avery Knox, mulher, fala em inglês com sotaque americano texano carregado, voz feminina média, levemente rouca e calorosa de uma texana de cinquenta e seis anos, aliviada e firme, voz autêntica, como se exigisse ser ouvida, a seguinte frase: "The worst is finally over. I see a lot of money, prosperity and someone incredibly wonderful walking into your life."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Avery Knox segura a carteira aberta com uma mão na altura da barriga, sentada na soleira da porta aberta. Avery Knox abre a mão livre com a palma para cima, aliviada. O saleiro azul-escuro continua parado na soleira, no canto inferior esquerdo.

câmera: fixa na altura do peito, sem movimento

som ambiente: varanda residencial silenciosa, sem música
```

### V07 · T7 · frame inicial = a imagem escolhida do K02

```text
V07
a avatar Avery Knox, mulher, fala em inglês com sotaque americano texano carregado, voz feminina média, levemente rouca e calorosa de uma texana de cinquenta e seis anos, direta e urgente, voz autêntica, como se exigisse ser ouvida, a seguinte frase: "Type 222 in the comments right now, that's how this gets tied to your name. Then stay with me until the end."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Avery Knox segura a carteira aberta com uma mão na altura da barriga, sentada na soleira da porta aberta. Avery Knox aponta para baixo, para os comentários, e depois para a lente. O saleiro azul-escuro continua parado na soleira, no canto inferior esquerdo.

câmera: fixa na altura do peito, sem movimento

som ambiente: varanda residencial silenciosa, sem música
```

### V08 · T8 · frame inicial = a imagem escolhida do K02

```text
V08
a avatar Avery Knox, mulher, fala em inglês com sotaque americano texano carregado, voz feminina média, levemente rouca e calorosa de uma texana de cinquenta e seis anos, intensa e solene, voz autêntica, como se exigisse ser ouvida, a seguinte frase: "Before you scroll, close your right hand and listen until the end. This video isn't for everyone. The universe chose you."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Avery Knox segura a carteira aberta com uma mão na altura da barriga, sentada na soleira da porta aberta. Avery Knox fecha a mão livre devagar em punho, mantém e solta. O saleiro azul-escuro continua parado na soleira, no canto inferior esquerdo.

câmera: fixa na altura do peito, sem movimento

som ambiente: varanda residencial silenciosa, sem música
```

### V09 · T9 · frame inicial = a imagem escolhida do K02

```text
V09
a avatar Avery Knox, mulher, fala em inglês com sotaque americano texano carregado, voz feminina média, levemente rouca e calorosa de uma texana de cinquenta e seis anos, séria, em tom de aviso, voz autêntica, como se exigisse ser ouvida, a seguinte frase: "If you skip right now, the energy breaks. I feel something very unusual happening to you right now."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Avery Knox segura a carteira aberta com uma mão na altura da barriga, sentada na soleira da porta aberta. Avery Knox balança a mão livre de um lado para o outro, como quem manda parar. O saleiro azul-escuro continua parado na soleira, no canto inferior esquerdo.

câmera: fixa na altura do peito, sem movimento

som ambiente: varanda residencial silenciosa, sem música
```

### V10 · T10 · frame inicial = a imagem escolhida do K02

```text
V10
a avatar Avery Knox, mulher, fala em inglês com sotaque americano texano carregado, voz feminina média, levemente rouca e calorosa de uma texana de cinquenta e seis anos, intensa e baixa, voz autêntica, como se exigisse ser ouvida, a seguinte frase: "I see the chains that were keeping you trapped in scarcity being broken."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Avery Knox segura a carteira aberta com uma mão na altura da barriga, sentada na soleira da porta aberta. Avery Knox gesticula com a mão livre, pequenos gestos naturais, olhando direto para a lente. O saleiro azul-escuro continua parado na soleira, no canto inferior esquerdo.

câmera: fixa na altura do peito, sem movimento

som ambiente: varanda residencial silenciosa, sem música
```

### V11 · T11 · frame inicial = a imagem escolhida do K02

```text
V11
a avatar Avery Knox, mulher, fala em inglês com sotaque americano texano carregado, voz feminina média, levemente rouca e calorosa de uma texana de cinquenta e seis anos, calorosa e firme, voz autêntica, como se exigisse ser ouvida, a seguinte frase: "The love that was being held back from you is finally coming straight to you."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Avery Knox segura a carteira aberta com uma mão na altura da barriga, sentada na soleira da porta aberta. Avery Knox gesticula com a mão livre, pequenos gestos naturais, olhando direto para a lente. O saleiro azul-escuro continua parado na soleira, no canto inferior esquerdo.

câmera: fixa na altura do peito, sem movimento

som ambiente: varanda residencial silenciosa, sem música
```

### V12 · T12 · frame inicial = a imagem escolhida do K02

```text
V12
a avatar Avery Knox, mulher, fala em inglês com sotaque americano texano carregado, voz feminina média, levemente rouca e calorosa de uma texana de cinquenta e seis anos, séria e urgente, voz autêntica, como se exigisse ser ouvida, a seguinte frase: "In the next seven minutes, the energy of scarcity that was following you is going to be destroyed forever."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Avery Knox segura a carteira aberta com uma mão na altura da barriga, sentada na soleira da porta aberta. Avery Knox gesticula com a mão livre, pequenos gestos naturais, olhando direto para a lente. O saleiro azul-escuro continua parado na soleira, no canto inferior esquerdo.

câmera: fixa na altura do peito, sem movimento

som ambiente: varanda residencial silenciosa, sem música
```

### V13 · T13 · frame inicial = a imagem escolhida do K02

```text
V13
a avatar Avery Knox, mulher, fala em inglês com sotaque americano texano carregado, voz feminina média, levemente rouca e calorosa de uma texana de cinquenta e seis anos, rápida e prática, voz autêntica, como se exigisse ser ouvida, a seguinte frase: "So send this video to yourself right now, because in seven minutes you're going to come back to confirm the energetic shift for yourself."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Avery Knox segura a carteira aberta com uma mão na altura da barriga, sentada na soleira da porta aberta. Avery Knox gesticula com a mão livre, pequenos gestos naturais, olhando direto para a lente. O saleiro azul-escuro continua parado na soleira, no canto inferior esquerdo.

câmera: fixa na altura do peito, sem movimento

som ambiente: varanda residencial silenciosa, sem música
```

### V14 · T14 · frame inicial = a imagem escolhida do K02

```text
V14
a avatar Avery Knox, mulher, fala em inglês com sotaque americano texano carregado, voz feminina média, levemente rouca e calorosa de uma texana de cinquenta e seis anos, firme e confiante, voz autêntica, como se exigisse ser ouvida, a seguinte frase: "Now open your hand and save this video. That will be your first seal."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Avery Knox segura a carteira aberta com uma mão na altura da barriga, sentada na soleira da porta aberta. Avery Knox abre a mão livre para a lente, com a palma aberta. O saleiro azul-escuro continua parado na soleira, no canto inferior esquerdo.

câmera: fixa na altura do peito, sem movimento

som ambiente: varanda residencial silenciosa, sem música
```

### V15 · T15 · frame inicial = a imagem escolhida do K02

```text
V15
a avatar Avery Knox, mulher, fala em inglês com sotaque americano texano carregado, voz feminina média, levemente rouca e calorosa de uma texana de cinquenta e seis anos, rápida e prática, voz autêntica, como se exigisse ser ouvida, a seguinte frase: "Double tap quickly on your screen. That will be your second seal. And if you haven't typed 222 yet, do it now so I can see you did everything."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Avery Knox segura a carteira aberta com uma mão na altura da barriga, sentada na soleira da porta aberta. Avery Knox toca o ar duas vezes com o dedo indicador, como quem toca a tela, e aponta para baixo, para os comentários. O saleiro azul-escuro continua parado na soleira, no canto inferior esquerdo.

câmera: fixa na altura do peito, sem movimento

som ambiente: varanda residencial silenciosa, sem música
```

### V16 · T16 · frame inicial = a imagem escolhida do K02

```text
V16
a avatar Avery Knox, mulher, fala em inglês com sotaque americano texano carregado, voz feminina média, levemente rouca e calorosa de uma texana de cinquenta e seis anos, calorosa e animada, voz autêntica, como se exigisse ser ouvida, a seguinte frase: "If you did everything right, tomorrow at 11:11 a.m. you're going to receive some incredibly good news. But pay close attention."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Avery Knox segura a carteira aberta com uma mão na altura da barriga, sentada na soleira da porta aberta. Avery Knox gesticula com a mão livre, pequenos gestos naturais, olhando direto para a lente. O saleiro azul-escuro continua parado na soleira, no canto inferior esquerdo.

câmera: fixa na altura do peito, sem movimento

som ambiente: varanda residencial silenciosa, sem música
```

### V17 · T17 · frame inicial = a imagem escolhida do K02

```text
V17
a avatar Avery Knox, mulher, fala em inglês com sotaque americano texano carregado, voz feminina média, levemente rouca e calorosa de uma texana de cinquenta e seis anos, séria e baixa, voz autêntica, como se exigisse ser ouvida, a seguinte frase: "This energy is highly sensitive, and other people's envy can completely break it."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Avery Knox segura a carteira aberta com uma mão na altura da barriga, sentada na soleira da porta aberta. Avery Knox fala mais baixo, com o dedo indicador erguido. O saleiro azul-escuro continua parado na soleira, no canto inferior esquerdo.

câmera: fixa na altura do peito, sem movimento

som ambiente: varanda residencial silenciosa, sem música
```

### V18 · T18 · frame inicial = a imagem escolhida do K02

```text
V18
a avatar Avery Knox, mulher, fala em inglês com sotaque americano texano carregado, voz feminina média, levemente rouca e calorosa de uma texana de cinquenta e seis anos, próxima e urgente, voz autêntica, como se exigisse ser ouvida, a seguinte frase: "So follow me right now, so this stays open, because the second part of this sign is coming to you next."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Avery Knox segura a carteira aberta com uma mão na altura da barriga, sentada na soleira da porta aberta. Avery Knox aponta para a lente com a mão livre. O saleiro azul-escuro continua parado na soleira, no canto inferior esquerdo.

câmera: fixa na altura do peito, sem movimento

som ambiente: varanda residencial silenciosa, sem música
```

## 4. Montagem no CapCut

1. Clipes numerados na ordem: V01 a V18.
2. V01 (gancho, voz-over): usar só os primeiros ~3,1 s, com a narração inteira; deixar o fim da frase ("the house") vazar meio segundo sobre o começo do V02.
3. Entre V01 e V02, corte seco, sem flash (o modelo corta seco aos 3,12 s).
4. V02 a V18: zero tempo morto, todo clipe começa já falando; cortar logo depois da última palavra. Isolate Voice / Keep Vocal. Todos saem do mesmo frame (K02), então a troca de clipe fica no mesmo enquadramento, como no plano único do modelo.
5. Legenda karaokê em caixa alta, palavra atual em amarelo ou vermelho, no meio-baixo do quadro, do V01 ao V18.
6. O pedido de 222 está no V07 (antes da metade); o lembrete no V15. Sem seta para a foto de perfil: o CTA do fim é follow.
7. Sem Voice Changer: a voz vem do prompt de cada V.
8. Música só depois do gancho (a partir do V02), nunca no pré-gancho, entre -19 e -20 dB, fora da biblioteca do TikTok.
9. Rótulo pequeno `AI-generated` num canto do vídeo.

## 5. Transcrição final por take

| Take | English | Português |
|---|---|---|
| T1 | Put salt inside your wallet before you leave the house. | Coloque sal dentro da sua carteira antes de sair de casa. |
| T2 | I know it sounds ridiculous, but you'll thank me for the rest of your life. | Eu sei que parece ridículo, mas você vai me agradecer pelo resto da vida. |
| T3 | Keep your mouth shut after you watch this. Do not tell anyone. Not everyone is going to see this before this month ends. | Fique de boca fechada depois de assistir isto. Não conte pra ninguém. Nem todo mundo vai ver isto antes de este mês acabar. |
| T4 | I do not know your name, but do not scroll. Because if this reached you today, it reached you as a final warning. | Eu não sei o seu nome, mas não passe. Porque se isto chegou até você hoje, chegou como um último aviso. |
| T5 | A powerful wave of prosperity, love and money is heading your way. Don't tell anyone, but the abundance portal has opened. | Uma onda poderosa de prosperidade, amor e dinheiro está vindo na sua direção. Não conte pra ninguém, mas o portal da abundância se abriu. |
| T6 | The worst is finally over. I see a lot of money, prosperity and someone incredibly wonderful walking into your life. | O pior finalmente passou. Eu vejo muito dinheiro, prosperidade e alguém incrivelmente maravilhoso entrando na sua vida. |
| T7 | Type 222 in the comments right now, that's how this gets tied to your name. Then stay with me until the end. | Escreva 222 nos comentários agora, é assim que isto fica amarrado ao seu nome. Depois fique comigo até o fim. |
| T8 | Before you scroll, close your right hand and listen until the end. This video isn't for everyone. The universe chose you. | Antes de passar, feche a mão direita e escute até o fim. Este vídeo não é pra todo mundo. O universo escolheu você. |
| T9 | If you skip right now, the energy breaks. I feel something very unusual happening to you right now. | Se você pular agora, a energia se quebra. Eu sinto algo muito incomum acontecendo com você agora. |
| T10 | I see the chains that were keeping you trapped in scarcity being broken. | Eu vejo as correntes que te prendiam na escassez sendo quebradas. |
| T11 | The love that was being held back from you is finally coming straight to you. | O amor que estava sendo segurado longe de você finalmente está vindo direto pra você. |
| T12 | In the next seven minutes, the energy of scarcity that was following you is going to be destroyed forever. | Nos próximos sete minutos, a energia de escassez que te seguia vai ser destruída para sempre. |
| T13 | So send this video to yourself right now, because in seven minutes you're going to come back to confirm the energetic shift for yourself. | Então mande este vídeo pra você agora, porque em sete minutos você vai voltar pra confirmar a virada de energia com os próprios olhos. |
| T14 | Now open your hand and save this video. That will be your first seal. | Agora abra a mão e salve este vídeo. Esse vai ser o seu primeiro selo. |
| T15 | Double tap quickly on your screen. That will be your second seal. And if you haven't typed 222 yet, do it now so I can see you did everything. | Toque duas vezes rápido na tela. Esse vai ser o seu segundo selo. E se você ainda não escreveu 222, escreva agora pra eu ver que você fez tudo. |
| T16 | If you did everything right, tomorrow at 11:11 a.m. you're going to receive some incredibly good news. But pay close attention. | Se você fez tudo certo, amanhã às 11:11 da manhã você vai receber uma notícia incrivelmente boa. Mas preste muita atenção. |
| T17 | This energy is highly sensitive, and other people's envy can completely break it. | Essa energia é muito sensível, e a inveja dos outros pode quebrá-la por completo. |
| T18 | So follow me right now, so this stays open, because the second part of this sign is coming to you next. | Então me siga agora, pra isso continuar aberto, porque a segunda parte deste sinal chega pra você em seguida. |

## 6. Roteiro final em inglês

1. Put salt inside your wallet before you leave the house.
2. I know it sounds ridiculous, but you'll thank me for the rest of your life.
3. Keep your mouth shut after you watch this. Do not tell anyone. Not everyone is going to see this before this month ends.
4. I do not know your name, but do not scroll. Because if this reached you today, it reached you as a final warning.
5. A powerful wave of prosperity, love and money is heading your way. Don't tell anyone, but the abundance portal has opened.
6. The worst is finally over. I see a lot of money, prosperity and someone incredibly wonderful walking into your life.
7. Type 222 in the comments right now, that's how this gets tied to your name. Then stay with me until the end.
8. Before you scroll, close your right hand and listen until the end. This video isn't for everyone. The universe chose you.
9. If you skip right now, the energy breaks. I feel something very unusual happening to you right now.
10. I see the chains that were keeping you trapped in scarcity being broken.
11. The love that was being held back from you is finally coming straight to you.
12. In the next seven minutes, the energy of scarcity that was following you is going to be destroyed forever.
13. So send this video to yourself right now, because in seven minutes you're going to come back to confirm the energetic shift for yourself.
14. Now open your hand and save this video. That will be your first seal.
15. Double tap quickly on your screen. That will be your second seal. And if you haven't typed 222 yet, do it now so I can see you did everything.
16. If you did everything right, tomorrow at 11:11 a.m. you're going to receive some incredibly good news. But pay close attention.
17. This energy is highly sensitive, and other people's envy can completely break it.
18. So follow me right now, so this stays open, because the second part of this sign is coming to you next.

Put salt inside your wallet before you leave the house. I know it sounds ridiculous, but you'll thank me for the rest of your life. Keep your mouth shut after you watch this. Do not tell anyone. Not everyone is going to see this before this month ends. I do not know your name, but do not scroll. Because if this reached you today, it reached you as a final warning. A powerful wave of prosperity, love and money is heading your way. Don't tell anyone, but the abundance portal has opened. The worst is finally over. I see a lot of money, prosperity and someone incredibly wonderful walking into your life. Type 222 in the comments right now, that's how this gets tied to your name. Then stay with me until the end. Before you scroll, close your right hand and listen until the end. This video isn't for everyone. The universe chose you. If you skip right now, the energy breaks. I feel something very unusual happening to you right now. I see the chains that were keeping you trapped in scarcity being broken. The love that was being held back from you is finally coming straight to you. In the next seven minutes, the energy of scarcity that was following you is going to be destroyed forever. So send this video to yourself right now, because in seven minutes you're going to come back to confirm the energetic shift for yourself. Now open your hand and save this video. That will be your first seal. Double tap quickly on your screen. That will be your second seal. And if you haven't typed 222 yet, do it now so I can see you did everything. If you did everything right, tomorrow at 11:11 a.m. you're going to receive some incredibly good news. But pay close attention. This energy is highly sensitive, and other people's envy can completely break it. So follow me right now, so this stays open, because the second part of this sign is coming to you next.
