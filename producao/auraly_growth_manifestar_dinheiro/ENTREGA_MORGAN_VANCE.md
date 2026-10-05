# ENTREGA | Morgan Vance | Auraly Growth Manifestar Dinheiro

Produção `auraly_growth_manifestar_dinheiro` · Ângulo 3 · GROWTH · vídeo modelo de avatar IA · rodada de VALIDAÇÃO · perfil AURALY

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

Checklist de envio: 32/32 aprovados (N/A: A1, A2, A7, A9 fiéis ao modelo, gancho mudo; A10 growth sem produto; C3 a C7 sem segunda pessoa, selfie, frase curta repetida, cena atuada ou motion control)

Ficha: 2/2 K conferidos contra o frame do modelo, placar 14/14 cada (`FICHA_FRAMES.md`, GATE_VISUAL Parte 6)

## Anexos e mapa

- **Character sheet Morgan Vance:** `producao/_ancoras/character_sheets/morgan_vance_character_sheet.jpg` no K01 e no K02 (identidade e roupa).
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
```

## 2. PROMPTS DE IMAGEM

### K01 · T1, gancho mudo, pote de sal e louro colado na lente, câmera no chão do banheiro · anexar CHARACTER SHEET + FRAME DO MODELO

```text
K01
{
  "format": "IMPORTANT: THIS IS IPHONE FOOTAGE. Vertical 9:16.",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "reference_use": "Use the first attached image (character sheet) only for Morgan Vance's exact identity (face, skin, hair, body) and wardrobe; ignore its grey studio background. Use the second attached image (frame of the model video) as the reference for the setting, camera angle and framing; do not copy its person, clothes or on-screen text.",
  "identity_main": "The exact fictional AI character Morgan Vance: Black American woman around twenty-five, long knotless box braids down to the waist with a middle part and a few small gold cuffs in the braids, neat baby hairs, dark brown skin with real texture, visible pores and acne marks on the forehead and cheeks, dark brown eyes, long lashes, defined brows, glossy lips, a small gold hoop in her nostril and small gold earrings.",
  "wardrobe": "Cobalt blue ribbed long-sleeve top with a scoop neckline, a thin gold chain necklace with a small gold heart pendant, medium-blue bootcut jeans, barefoot.",
  "scene": "The ordinary American bathroom of the reference video: white shaker-style vanity cabinets with drawers and a light speckled countertop on the right side, a stack of folded grey towels on the countertop, a framed botanical print of a green plant in a thin wooden frame on the cream wall at the left, the vanity mirror with a three-bulb light fixture above it, and large light grey porcelain floor tiles. On the vanity countertop a small American flag stands in a drinking glass, discreet but visible and in focus.",
  "prop": "The only object is a clear glass mason jar filled with coarse white salt, with a handful of dried green bay leaves on top of the salt, no lid, held out in one of her dark brown hands with short natural nails toward the lens; the other hand rests on her thigh. The floor in front of Morgan Vance is still empty and clean.",
  "posture": "Morgan Vance kneels on the bathroom floor sitting back on her heels, facing the lens, holding the jar out toward the phone, smiling softly and looking down at the lens, mouth closed.",
  "composition": "The glass jar of salt and bay leaves is in the lower right of the frame, very close to the lens, about 14 inches from the lens, taking up about 20 percent of the frame, closer to the camera than her face, nothing else competing with it. Morgan Vance is framed from the top of the head down to the knees, her face in the upper third. Nothing else is in the foreground. The background is reduced by framing, never by blur.",
  "camera": "phone resting on the bathroom floor, lens at floor level about three feet away, 1x lens, pointing slightly upward, fixed",
  "lighting": "Neutral overcast daylight coming in from a window just out of frame on the left, cool and even, the vanity lights switched off, soft even light on the face, hands and feet with no harsh shadows.",
  "state": "Start frame: Morgan Vance holds the full jar still, about to tip it toward the floor, mouth closed.",
  "realism": "Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday reality, background fully in focus, everything in sharp focus, no AI polish, no beauty smoothing.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no label on the jar, no studio, no grey studio background, no plastic-looking human skin, no extra fingers, no extra toes, no third hand, no supernatural lighting, no blur, no bokeh, no artificial lighting, no warm orange color cast, no yellow tint on the skin, no golden glow, no golden hour light, no sunset, no de-aging, no beauty smoothing, no visible phone, no HDR, no cinematic lighting, no second person in frame, no shoes, no socks, no tarot cards, no candles, no fire, no flames, no smoke, no salt on the floor yet"
}
```

### K02 · T2 a T11, corpo, ajoelhada atrás do círculo de sal e louro em chamas, câmera no chão · anexar CHARACTER SHEET + FRAME DO MODELO

```text
K02
{
  "format": "IMPORTANT: THIS IS IPHONE FOOTAGE. Vertical 9:16.",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "reference_use": "Use the first attached image (character sheet) only for Morgan Vance's exact identity (face, skin, hair, body) and wardrobe; ignore its grey studio background. Use the second attached image (frame of the model video) as the reference for the setting, camera angle and framing; do not copy its person, clothes or on-screen text.",
  "identity_main": "The exact fictional AI character Morgan Vance: Black American woman around twenty-five, long knotless box braids down to the waist with a middle part and a few small gold cuffs in the braids, neat baby hairs, dark brown skin with real texture, visible pores and acne marks on the forehead and cheeks, dark brown eyes, long lashes, defined brows, glossy lips, a small gold hoop in her nostril and small gold earrings.",
  "wardrobe": "Cobalt blue ribbed long-sleeve top with a scoop neckline, a thin gold chain necklace with a small gold heart pendant, medium-blue bootcut jeans, barefoot.",
  "scene": "The ordinary American bathroom of the reference video: white shaker-style vanity cabinets with drawers and a light speckled countertop on the right side, a stack of folded grey towels on the countertop, a framed botanical print of a green plant in a thin wooden frame on the cream wall at the left, the vanity mirror with a three-bulb light fixture above it, and large light grey porcelain floor tiles. On the vanity countertop a small American flag stands in a drinking glass, discreet but visible and in focus.",
  "prop": "In the lower part of the frame, right in front of the lens, lies a wide ring of coarse white salt poured on the porcelain floor, about two feet across, with a crown of dried bay leaves laid along it, the bay leaves burning with small low flames all around the ring and the empty grey tile showing in the middle. One of her dark brown hands with short natural nails rests flat on the floor beside the ring; the other hand points at the lens.",
  "posture": "Morgan Vance kneels on the bathroom floor right behind the burning ring, leaning slightly toward the lens, one hand flat on the tiles, the other hand pointing at the lens, looking straight into the lens.",
  "composition": "The burning ring of salt and bay leaves fills the bottom quarter of the frame, about 25 percent of the frame, touching the bottom edge, its near edge about 10 inches from the lens, closer to the camera than her face, nothing else competing with it. Morgan Vance is framed from the top of the head down to the knees, her face in the upper third. Nothing else is in the foreground. The background is reduced by framing, never by blur.",
  "camera": "phone resting on the bathroom floor, lens at floor level about three feet away, 1x lens, pointing slightly upward, fixed",
  "lighting": "Neutral overcast daylight coming in from a window just out of frame on the left, cool and even, the vanity lights switched off, soft even light on the face, hands and feet with no harsh shadows.",
  "state": "Start frame: Morgan Vance points at the lens, caught mid-sentence, lips naturally parted, serious expression.",
  "realism": "Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday reality, background fully in focus, everything in sharp focus, no AI polish, no beauty smoothing.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no label on the jar, no studio, no grey studio background, no plastic-looking human skin, no extra fingers, no extra toes, no third hand, no supernatural lighting, no blur, no bokeh, no artificial lighting, no warm orange color cast, no yellow tint on the skin, no golden glow, no golden hour light, no sunset, no de-aging, no beauty smoothing, no visible phone, no HDR, no cinematic lighting, no second person in frame, no shoes, no socks, no tarot cards, no candles, no smoke cloud, no tall flames, no fire on the person"
}
```

## 3. PROMPTS DE VÍDEO (um bloco por V)

### V01 · T1 · frame inicial = a imagem escolhida do K01

```text
V01
(sem fala no take: gancho mudo, a avatar fica em silêncio o clipe inteiro, boca fechada)

o que acontece no vídeo: plano 1, Morgan Vance ajoelhada no chão do banheiro inclina o pote de vidro e despeja o sal grosso com as folhas de louro em um círculo no chão, bem na frente da lente; corte seco para o plano 2, Morgan Vance agachada atrás do círculo pronto acende um isqueiro na borda e o círculo inteiro pega fogo; corte seco para o plano 3, Morgan Vance de pé pisa descalça dentro do círculo em chamas, sobe uma nuvem de fumaça branca, Morgan Vance se ajoelha dentro da fumaça com as duas mãos abertas para a lente e a fumaça cobre a câmera.

câmera: fixa no chão, olhando levemente para cima, com dois cortes secos internos ao clipe, sem movimento

som ambiente: banheiro silencioso, o sal caindo no piso, o clique do isqueiro e o fogo estalando, sem música
```

### V02 · T2 · frame inicial = a imagem escolhida do K02

```text
V02
a avatar Morgan Vance, mulher, fala em inglês com sotaque americano leve de Atlanta, voz feminina média e jovem, confiante e direta, de uma mulher de vinte e cinco anos de Atlanta, séria e intrigante, voz autêntica, como se exigisse ser ouvida, a seguinte frase: "Pay very close attention if this video showed up for you today or tomorrow."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Morgan Vance aponta para a lente com uma mão, com a outra apoiada no chão, e fala com pequenos gestos naturais. As chamas baixas do círculo de sal à frente continuam queimando.

câmera: fixa no chão, olhando levemente para cima, sem movimento

som ambiente: banheiro silencioso, o fogo estalando baixinho, sem música
```

### V03 · T3 · frame inicial = a imagem escolhida do K02

```text
V03
a avatar Morgan Vance, mulher, fala em inglês com sotaque americano leve de Atlanta, voz feminina média e jovem, confiante e direta, de uma mulher de vinte e cinco anos de Atlanta, convicta e intensa, voz autêntica, como se exigisse ser ouvida, a seguinte frase: "Because in the next three minutes, all scarcity is going to be wiped out of your life, and the proof speaks for itself."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Morgan Vance aponta para a lente com uma mão, com a outra apoiada no chão, e fala com pequenos gestos naturais. As chamas baixas do círculo de sal à frente continuam queimando.

câmera: fixa no chão, olhando levemente para cima, sem movimento

som ambiente: banheiro silencioso, o fogo estalando baixinho, sem música
```

### V04 · T4 · frame inicial = a imagem escolhida do K02

```text
V04
a avatar Morgan Vance, mulher, fala em inglês com sotaque americano leve de Atlanta, voz feminina média e jovem, confiante e direta, de uma mulher de vinte e cinco anos de Atlanta, urgente e direta, voz autêntica, como se exigisse ser ouvida, a seguinte frase: "Send this one to yourself this second, because in three minutes you'll be back to confirm how you felt the doors open again,"

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Morgan Vance aponta para a lente com uma mão, com a outra apoiada no chão, e fala com pequenos gestos naturais. As chamas baixas do círculo de sal à frente continuam queimando.

câmera: fixa no chão, olhando levemente para cima, sem movimento

som ambiente: banheiro silencioso, o fogo estalando baixinho, sem música
```

### V05 · T5 · frame inicial = a imagem escolhida do K02

```text
V05
a avatar Morgan Vance, mulher, fala em inglês com sotaque americano leve de Atlanta, voz feminina média e jovem, confiante e direta, de uma mulher de vinte e cinco anos de Atlanta, aliviada e firme, voz autêntica, como se exigisse ser ouvida, a seguinte frase: "how the scarcity ended and how abundance started flowing in. The worst is finally over. The universe has already chosen you."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Morgan Vance abre a mão livre para a lente, aliviada, com a outra mão apoiada no chão. As chamas baixas do círculo de sal à frente continuam queimando.

câmera: fixa no chão, olhando levemente para cima, sem movimento

som ambiente: banheiro silencioso, o fogo estalando baixinho, sem música
```

### V06 · T6 · frame inicial = a imagem escolhida do K02

```text
V06
a avatar Morgan Vance, mulher, fala em inglês com sotaque americano leve de Atlanta, voz feminina média e jovem, confiante e direta, de uma mulher de vinte e cinco anos de Atlanta, séria, em tom de aviso, voz autêntica, como se exigisse ser ouvida, a seguinte frase: "In 33 minutes, you're going to receive some very good news, but don't stop watching or that news could turn against you."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Morgan Vance aponta para a lente com uma mão, com a outra apoiada no chão, e fala com pequenos gestos naturais. As chamas baixas do círculo de sal à frente continuam queimando.

câmera: fixa no chão, olhando levemente para cima, sem movimento

som ambiente: banheiro silencioso, o fogo estalando baixinho, sem música
```

### V07 · T7 · frame inicial = a imagem escolhida do K02

```text
V07
a avatar Morgan Vance, mulher, fala em inglês com sotaque americano leve de Atlanta, voz feminina média e jovem, confiante e direta, de uma mulher de vinte e cinco anos de Atlanta, intensa e solene, voz autêntica, como se exigisse ser ouvida, a seguinte frase: "A powerful blessing is coming your way with incredible force. This is the universe's final message, so take it seriously."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Morgan Vance aponta para a lente com uma mão, com a outra apoiada no chão, e fala com pequenos gestos naturais. As chamas baixas do círculo de sal à frente continuam queimando.

câmera: fixa no chão, olhando levemente para cima, sem movimento

som ambiente: banheiro silencioso, o fogo estalando baixinho, sem música
```

### V08 · T8 · frame inicial = a imagem escolhida do K02

```text
V08
a avatar Morgan Vance, mulher, fala em inglês com sotaque americano leve de Atlanta, voz feminina média e jovem, confiante e direta, de uma mulher de vinte e cinco anos de Atlanta, rápida e prática, voz autêntica, como se exigisse ser ouvida, a seguinte frase: "Now hit save on this video. That's seal number one. Tap your screen two times, quickly. That's seal number two."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Morgan Vance toca o ar duas vezes com o dedo indicador, como quem toca a tela, com a outra mão apoiada no chão. As chamas baixas do círculo de sal à frente continuam queimando.

câmera: fixa no chão, olhando levemente para cima, sem movimento

som ambiente: banheiro silencioso, o fogo estalando baixinho, sem música
```

### V09 · T9 · frame inicial = a imagem escolhida do K02

```text
V09
a avatar Morgan Vance, mulher, fala em inglês com sotaque americano leve de Atlanta, voz feminina média e jovem, confiante e direta, de uma mulher de vinte e cinco anos de Atlanta, firme e confiante, voz autêntica, como se exigisse ser ouvida, a seguinte frase: "Then leave 222 in the comments so I know every step is done. Do it right, and in 33 minutes your good news arrives."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Morgan Vance aponta para baixo, para os comentários, e depois para a lente. As chamas baixas do círculo de sal à frente continuam queimando.

câmera: fixa no chão, olhando levemente para cima, sem movimento

som ambiente: banheiro silencioso, o fogo estalando baixinho, sem música
```

### V10 · T10 · frame inicial = a imagem escolhida do K02

```text
V10
a avatar Morgan Vance, mulher, fala em inglês com sotaque americano leve de Atlanta, voz feminina média e jovem, confiante e direta, de uma mulher de vinte e cinco anos de Atlanta, séria e baixa, voz autêntica, como se exigisse ser ouvida, a seguinte frase: "But pay close attention. The spiritual world is fair, and if you turn your back on its message, the blessings will also turn their back on you."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Morgan Vance fala devagar, com o dedo indicador erguido, a outra mão apoiada no chão. As chamas baixas do círculo de sal à frente continuam queimando.

câmera: fixa no chão, olhando levemente para cima, sem movimento

som ambiente: banheiro silencioso, o fogo estalando baixinho, sem música
```

### V11 · T11 · frame inicial = a imagem escolhida do K02

```text
V11
a avatar Morgan Vance, mulher, fala em inglês com sotaque americano leve de Atlanta, voz feminina média e jovem, confiante e direta, de uma mulher de vinte e cinco anos de Atlanta, próxima e urgente, voz autêntica, como se exigisse ser ouvida, a seguinte frase: "So follow me right now, before this disappears, because the next piece of this message is already headed your way."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Morgan Vance se inclina um pouco para a lente e aponta para ela. As chamas baixas do círculo de sal à frente continuam queimando.

câmera: fixa no chão, olhando levemente para cima, sem movimento

som ambiente: banheiro silencioso, o fogo estalando baixinho, sem música
```

## 4. Montagem no CapCut

1. Clipes numerados na ordem: V01 a V11.
2. V01 (gancho mudo): usar ~6 s, até a fumaça cobrir a lente, que é a transição para o V02. Texto branco no topo: "When you urgently need unexpected money!".
3. V02 a V11: zero tempo morto, todo clipe começa já falando; cortar logo depois da última palavra. Isolate Voice / Keep Vocal. Todos saem do mesmo frame (K02), então a troca de clipe fica no mesmo enquadramento, como no modelo. V04 termina na vírgula e o V05 continua a frase: juntar sem pausa.
4. Do V02 ao V11, "11:11 ✨" no canto superior esquerdo e legenda branca da fala no meio do quadro.
5. Sem seta para a foto de perfil: o CTA é follow.
6. Sem Voice Changer: a voz vem do prompt de cada V.
7. Música no V01 (o modelo abre com música) e baixa por baixo da fala a partir do V02, entre -19 e -20 dB, fora da biblioteca do TikTok.
8. Rótulo pequeno `AI-generated` num canto do vídeo.

## 5. Transcrição final por take

| Take | English | Português |
|---|---|---|
| T1 | (sem fala) | (sem fala) |
| T2 | Pay very close attention if this video showed up for you today or tomorrow. | Preste muita atenção se este vídeo apareceu pra você hoje ou amanhã. |
| T3 | Because in the next three minutes, all scarcity is going to be wiped out of your life, and the proof speaks for itself. | Porque nos próximos três minutos toda a escassez vai ser apagada da sua vida, e a prova fala por si. |
| T4 | Send this one to yourself this second, because in three minutes you'll be back to confirm how you felt the doors open again, | Mande este pra você mesma neste segundo, porque em três minutos você vai estar de volta pra confirmar como sentiu as portas se abrirem de novo, |
| T5 | how the scarcity ended and how abundance started flowing in. The worst is finally over. The universe has already chosen you. | como a escassez acabou e como a abundância começou a entrar. O pior finalmente passou. O universo já escolheu você. |
| T6 | In 33 minutes, you're going to receive some very good news, but don't stop watching or that news could turn against you. | Em 33 minutos você vai receber uma notícia muito boa, mas não pare de assistir, senão essa notícia pode se virar contra você. |
| T7 | A powerful blessing is coming your way with incredible force. This is the universe's final message, so take it seriously. | Uma bênção poderosa está vindo na sua direção com uma força incrível. Esta é a mensagem final do universo, então leve a sério. |
| T8 | Now hit save on this video. That's seal number one. Tap your screen two times, quickly. That's seal number two. | Agora aperte salvar neste vídeo. Esse é o selo número um. Toque duas vezes na tela, rápido. Esse é o selo número dois. |
| T9 | Then leave 222 in the comments so I know every step is done. Do it right, and in 33 minutes your good news arrives. | Depois deixe 222 nos comentários pra eu saber que cada passo foi feito. Faça certo, e em 33 minutos a sua boa notícia chega. |
| T10 | But pay close attention. The spiritual world is fair, and if you turn your back on its message, the blessings will also turn their back on you. | Mas preste muita atenção. O mundo espiritual é justo, e se você der as costas pra mensagem dele, as bênçãos também vão dar as costas pra você. |
| T11 | So follow me right now, before this disappears, because the next piece of this message is already headed your way. | Então me siga agora, antes que isto suma, porque a próxima parte desta mensagem já está vindo na sua direção. |

## 6. Roteiro final em inglês

1. (sem fala: gancho mudo)
2. Pay very close attention if this video showed up for you today or tomorrow.
3. Because in the next three minutes, all scarcity is going to be wiped out of your life, and the proof speaks for itself.
4. Send this one to yourself this second, because in three minutes you'll be back to confirm how you felt the doors open again,
5. how the scarcity ended and how abundance started flowing in. The worst is finally over. The universe has already chosen you.
6. In 33 minutes, you're going to receive some very good news, but don't stop watching or that news could turn against you.
7. A powerful blessing is coming your way with incredible force. This is the universe's final message, so take it seriously.
8. Now hit save on this video. That's seal number one. Tap your screen two times, quickly. That's seal number two.
9. Then leave 222 in the comments so I know every step is done. Do it right, and in 33 minutes your good news arrives.
10. But pay close attention. The spiritual world is fair, and if you turn your back on its message, the blessings will also turn their back on you.
11. So follow me right now, before this disappears, because the next piece of this message is already headed your way.

Pay very close attention if this video showed up for you today or tomorrow. Because in the next three minutes, all scarcity is going to be wiped out of your life, and the proof speaks for itself. Send this one to yourself this second, because in three minutes you'll be back to confirm how you felt the doors open again, how the scarcity ended and how abundance started flowing in. The worst is finally over. The universe has already chosen you. In 33 minutes, you're going to receive some very good news, but don't stop watching or that news could turn against you. A powerful blessing is coming your way with incredible force. This is the universe's final message, so take it seriously. Now hit save on this video. That's seal number one. Tap your screen two times, quickly. That's seal number two. Then leave 222 in the comments so I know every step is done. Do it right, and in 33 minutes your good news arrives. But pay close attention. The spiritual world is fair, and if you turn your back on its message, the blessings will also turn their back on you. So follow me right now, before this disappears, because the next piece of this message is already headed your way.
