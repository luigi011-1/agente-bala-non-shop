# ENTREGA | Jordan Vale | Auraly Venda Familiar Corredor

Produção `auraly_venda_familiar_corredor` · Ângulo 3 · GROWTH · vídeo modelo de avatar IA · rodada de VALIDAÇÃO · perfil AURALY

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

Checklist de envio: 32/32 aprovados (N/A: A1, A2, A7, A9 fiéis ao modelo, gancho mudo; A10 growth sem produto; C3 a C7 sem segunda pessoa, selfie na mão fora de quadro, frase curta repetida, cena atuada ou motion control)

Ficha: 2/2 K conferidos contra o frame do modelo, placar 14/14 cada (`FICHA_FRAMES.md`, GATE_VISUAL Parte 6)

## Anexos e mapa

- **Character sheet Jordan Vale:** `producao/_ancoras/character_sheets/jordan_vale_character_sheet.jpg` no K01 e no K02 (identidade e roupa).
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
```

## 2. PROMPTS DE IMAGEM

### K01 · T1, gancho mudo, fileira de sal e folhas no chão do corredor, câmera no chão · anexar CHARACTER SHEET + FRAME DO MODELO

```text
K01
{
  "format": "IMPORTANT: THIS IS IPHONE FOOTAGE. Vertical 9:16.",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "reference_use": "Use the first attached image (character sheet) only for Jordan Vale's exact identity (face, skin, hair, body) and wardrobe; ignore its grey studio background. Use the second attached image (frame of the model video) as the reference for the setting, camera angle and framing; do not copy its person, clothes or on-screen text.",
  "identity_main": "The exact fictional AI character Jordan Vale, explicitly male: white American man around fifty-eight, long grey-white beard down to mid-chest, grey moustache, grey hair combed back short on the sides, sun-weathered skin with freckles and deep crow's feet, light grey eyes, both forearms covered in faded traditional American tattoos with no lettering, a swallow and a red rose on the left forearm.",
  "wardrobe": "Black leather vest over a heather grey crew-neck T-shirt, dark blue straight jeans, barefoot.",
  "scene": "The ordinary American hallway of the reference video: cream-painted walls, white baseboards, red-oak plank flooring, a six-panel wooden door at the far end of the hallway and another wooden door set into the right wall. On the left wall near the far door hangs a small American flag, discreet but visible and in focus.",
  "prop": "The only object is a thin straight line of coarse white salt with dried leaves mixed into the salt, laid along the oak floor from the avatar's knees in a dead-straight line all the way to the far door, still unlit except for a tiny flame at its near end, where Jordan Vale holds a small plain lighter in his weathered hands with faded tattoos on the forearms. The floor around the line is empty and clean.",
  "posture": "Jordan Vale kneels on the hallway floor at the left of the frame, sitting back on his heels, body turned toward the line of salt, both hands together at its near end holding the lighter, eyes on the flame, mouth closed.",
  "composition": "The thin straight line of coarse white salt runs from the bottom center of the frame straight to the six-panel door at the far end, about 20 percent of the frame, its near end about 48 inches from the lens, closer to the camera than his face, which is about 60 inches from the lens, nothing else competing with it. Jordan Vale is framed from the top of the head down to the knees on the left side of the frame. Nothing else is in the foreground. The background is reduced by framing, never by blur.",
  "camera": "phone resting on the hallway floor, lens at floor level about four feet from the near end of the line of salt, 0.5x lens, looking along the hallway toward the far door, fixed",
  "lighting": "Neutral overcast daylight coming in from a window just out of frame, cool and even, the ceiling lights switched off, soft even light on the face and hands with no harsh shadows.",
  "state": "Start frame: Jordan Vale has just lit the lighter at the near end of the line, a tiny flame, mouth closed.",
  "realism": "Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday reality, background fully in focus, everything in sharp focus, no AI polish, no beauty smoothing.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no studio, no grey studio background, no plastic-looking human skin, no extra fingers, no extra toes, no third hand, no supernatural lighting, no blur, no bokeh, no artificial lighting, no warm orange color cast, no yellow tint on the skin, no golden glow, no golden hour light, no sunset, no de-aging, no beauty smoothing, no visible phone, no HDR, no cinematic lighting, no second person in frame, no figure or silhouette in any doorway, no shoes, no socks, no tarot cards, no candles, no fire running along the line yet, no open door, no smoke, no salt circle, no jar"
}
```

### K02 · T2 a T15, corpo, selfie de perto agachado no corredor, restos da fileira de sal no canto · anexar CHARACTER SHEET + FRAME DO MODELO

```text
K02
{
  "format": "IMPORTANT: THIS IS IPHONE FOOTAGE. Vertical 9:16.",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "reference_use": "Use the first attached image (character sheet) only for Jordan Vale's exact identity (face, skin, hair, body) and wardrobe; ignore its grey studio background. Use the second attached image (frame of the model video) as the reference for the setting, camera angle and framing; do not copy its person, clothes or on-screen text.",
  "identity_main": "The exact fictional AI character Jordan Vale, explicitly male: white American man around fifty-eight, long grey-white beard down to mid-chest, grey moustache, grey hair combed back short on the sides, sun-weathered skin with freckles and deep crow's feet, light grey eyes, both forearms covered in faded traditional American tattoos with no lettering, a swallow and a red rose on the left forearm.",
  "wardrobe": "Black leather vest over a heather grey crew-neck T-shirt, dark blue straight jeans, barefoot.",
  "scene": "The ordinary American hallway of the reference video: cream-painted walls, white baseboards, red-oak plank flooring, a six-panel wooden door at the far end of the hallway and another wooden door set into the right wall. On the left wall near the far door hangs a small American flag, discreet but visible and in focus.",
  "prop": "In the lower right corner of the frame, on the oak floor, lie the remains of a thin line of coarse white salt with dried leaves mixed into the salt, a pale streak with small leaf shapes on the oak floor. No hands and no other objects are in frame.",
  "posture": "Jordan Vale crouches in the hallway facing the lens, his left shoulder closer to the camera, looking straight into the lens with a calm intimate expression.",
  "composition": "His face and shoulders fill the center of the frame, about 60 percent of the frame, about 18 inches from the lens, the face in the upper middle with a little headroom, framed from the top of the head to the chest; the remains of the line of salt in the lower right corner, about 20 inches from the lens, about 10 percent of the frame; the hallway recedes sharply behind his head toward the far door. Nothing else is in the foreground. The background is reduced by framing, never by blur.",
  "camera": "selfie angle, phone held at chest height in an outstretched hand just out of frame, about 18 inches from the face, 1x front lens, pointing slightly upward, fixed",
  "lighting": "Neutral overcast daylight coming in from a window just out of frame, cool and even, the ceiling lights switched off, soft even light on the face and hands with no harsh shadows.",
  "state": "Start frame: Jordan Vale looks straight into the lens, caught mid-sentence, lips naturally parted, calm intimate expression.",
  "realism": "Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday reality, background fully in focus, everything in sharp focus, no AI polish, no beauty smoothing.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no studio, no grey studio background, no plastic-looking human skin, no extra fingers, no extra toes, no third hand, no supernatural lighting, no blur, no bokeh, no artificial lighting, no warm orange color cast, no yellow tint on the skin, no golden glow, no golden hour light, no sunset, no de-aging, no beauty smoothing, no visible phone, no HDR, no cinematic lighting, no second person in frame, no figure or silhouette in any doorway, no shoes, no socks, no tarot cards, no candles, no smoke, no flames, no ash, no hands in frame"
}
```

## 3. PROMPTS DE VÍDEO (um bloco por V)

### V01 · T1 · frame inicial = a imagem escolhida do K01

```text
V01
(sem fala no take: gancho mudo, o avatar fica em silêncio o clipe inteiro, boca fechada)

o que acontece no vídeo: plano 1, Jordan Vale de joelhos no chão do corredor acende com um isqueiro a ponta da fileira fina de sal e folhas secas e a primeira chama sobe, bem na frente da lente; corte seco para o plano 2, plano aberto do corredor sem ninguém em quadro, o fogo corre pela fileira até o fundo, deixa cinzas e brasas no piso e perde força perto da porta de madeira; corte seco para o plano 3, a porta do fundo abre sozinha, devagar, para um cômodo escuro e a fumaça branca sai e rola pelo chão em direção à lente; corte seco para o plano 4, Jordan Vale volta ao quadro pela esquerda, ainda de joelhos, e olha para a lente.

câmera: fixa no chão, olhando ao longo do corredor, com três cortes secos internos ao clipe, sem movimento

som ambiente: corredor silencioso, o clique do isqueiro, o fogo estalando e a porta rangendo, sem música
```

### V02 · T2 · frame inicial = a imagem escolhida do K02

```text
V02
o avatar Jordan Vale, homem, fala em inglês com sotaque americano do Tennessee, voz masculina grave, devagar e gentil de um homem de cinquenta e oito anos do Tennessee, em tom de conversa de selfie, baixo e solene, como quem traz uma mensagem delicada, voz autêntica, como se exigisse ser ouvido, a seguinte frase: "A family member of yours who is in heaven asked me to bring you a very important message. If you are ready to hear it, stay until the end."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Jordan Vale fala olhando para a lente, com pequenas inclinações naturais da cabeça, sem nenhuma mão visível.

câmera: selfie de perto, fixa, sem movimento

som ambiente: corredor silencioso, sem música
```

### V03 · T3 · frame inicial = a imagem escolhida do K02

```text
V03
o avatar Jordan Vale, homem, fala em inglês com sotaque americano do Tennessee, voz masculina grave, devagar e gentil de um homem de cinquenta e oito anos do Tennessee, em tom de conversa de selfie, em voz mais baixo, quase em segredo, voz autêntica, como se exigisse ser ouvido, a seguinte frase: "You will be left speechless when you hear it. This one is only for you. Not everyone will see this video before the week is over."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Jordan Vale fala olhando para a lente, com pequenas inclinações naturais da cabeça, sem nenhuma mão visível.

câmera: selfie de perto, fixa, sem movimento

som ambiente: corredor silencioso, sem música
```

### V04 · T4 · frame inicial = a imagem escolhida do K02

```text
V04
o avatar Jordan Vale, homem, fala em inglês com sotaque americano do Tennessee, voz masculina grave, devagar e gentil de um homem de cinquenta e oito anos do Tennessee, em tom de conversa de selfie, calmo e próximo, voz autêntica, como se exigisse ser ouvido, a seguinte frase: "I can't see your name, but I can feel you, and if this reached your screen today, it came as one last call to listen."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Jordan Vale fala olhando para a lente, com pequenas inclinações naturais da cabeça, sem nenhuma mão visível.

câmera: selfie de perto, fixa, sem movimento

som ambiente: corredor silencioso, sem música
```

### V05 · T5 · frame inicial = a imagem escolhida do K02

```text
V05
o avatar Jordan Vale, homem, fala em inglês com sotaque americano do Tennessee, voz masculina grave, devagar e gentil de um homem de cinquenta e oito anos do Tennessee, em tom de conversa de selfie, sereno e esperançoso, voz autêntica, como se exigisse ser ouvido, a seguinte frase: "A strong current of abundance, love and money is turning your way. Quietly, between us, the road to it just cleared. Everything heavy is behind you."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Jordan Vale fala olhando para a lente, com pequenas inclinações naturais da cabeça, sem nenhuma mão visível.

câmera: selfie de perto, fixa, sem movimento

som ambiente: corredor silencioso, sem música
```

### V06 · T6 · frame inicial = a imagem escolhida do K02

```text
V06
o avatar Jordan Vale, homem, fala em inglês com sotaque americano do Tennessee, voz masculina grave, devagar e gentil de um homem de cinquenta e oito anos do Tennessee, em tom de conversa de selfie, firme e acolhedor, voz autêntica, como se exigisse ser ouvido, a seguinte frase: "I see a great deal of money and prosperity coming into your life. Before you comment, rest your right hand over your heart and listen to the end."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Jordan Vale fala olhando para a lente, com pequenas inclinações naturais da cabeça, sem nenhuma mão visível.

câmera: selfie de perto, fixa, sem movimento

som ambiente: corredor silencioso, sem música
```

### V07 · T7 · frame inicial = a imagem escolhida do K02

```text
V07
o avatar Jordan Vale, homem, fala em inglês com sotaque americano do Tennessee, voz masculina grave, devagar e gentil de um homem de cinquenta e oito anos do Tennessee, em tom de conversa de selfie, direto e convidativo, voz autêntica, como se exigisse ser ouvido, a seguinte frase: "Now write 222 below, so this message is marked with your name and the abundance I see knows where to land."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Jordan Vale olha de relance para baixo, para onde ficam os comentários, e volta o olhar para a lente.

câmera: selfie de perto, fixa, sem movimento

som ambiente: corredor silencioso, sem música
```

### V08 · T8 · frame inicial = a imagem escolhida do K02

```text
V08
o avatar Jordan Vale, homem, fala em inglês com sotaque americano do Tennessee, voz masculina grave, devagar e gentil de um homem de cinquenta e oito anos do Tennessee, em tom de conversa de selfie, sério, em tom de aviso, voz autêntica, como se exigisse ser ouvido, a seguinte frase: "Not everyone is meant to hear this, and you were picked to hear it. If you skip ahead now, the energy around you will scatter."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Jordan Vale fala olhando para a lente, com pequenas inclinações naturais da cabeça, sem nenhuma mão visível.

câmera: selfie de perto, fixa, sem movimento

som ambiente: corredor silencioso, sem música
```

### V09 · T9 · frame inicial = a imagem escolhida do K02

```text
V09
o avatar Jordan Vale, homem, fala em inglês com sotaque americano do Tennessee, voz masculina grave, devagar e gentil de um homem de cinquenta e oito anos do Tennessee, em tom de conversa de selfie, intenso e solene, voz autêntica, como se exigisse ser ouvido, a seguinte frase: "Something unusual is moving around you right now, and I can sense it. I see the chains that kept your prosperity locked away finally breaking apart."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Jordan Vale fala olhando para a lente, com pequenas inclinações naturais da cabeça, sem nenhuma mão visível.

câmera: selfie de perto, fixa, sem movimento

som ambiente: corredor silencioso, sem música
```

### V10 · T10 · frame inicial = a imagem escolhida do K02

```text
V10
o avatar Jordan Vale, homem, fala em inglês com sotaque americano do Tennessee, voz masculina grave, devagar e gentil de um homem de cinquenta e oito anos do Tennessee, em tom de conversa de selfie, firme e tranquilizador, voz autêntica, como se exigisse ser ouvido, a seguinte frase: "The envy others sent your way is losing its hold on you. In the next 7 minutes, the heavy energy around you will be cleared away for good."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Jordan Vale fala olhando para a lente, com pequenas inclinações naturais da cabeça, sem nenhuma mão visível.

câmera: selfie de perto, fixa, sem movimento

som ambiente: corredor silencioso, sem música
```

### V11 · T11 · frame inicial = a imagem escolhida do K02

```text
V11
o avatar Jordan Vale, homem, fala em inglês com sotaque americano do Tennessee, voz masculina grave, devagar e gentil de um homem de cinquenta e oito anos do Tennessee, em tom de conversa de selfie, urgente e próximo, voz autêntica, como se exigisse ser ouvido, a seguinte frase: "So forward this one to yourself this minute, because in 7 minutes you will return here to confirm this shift in your life."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Jordan Vale fala olhando para a lente, com pequenas inclinações naturais da cabeça, sem nenhuma mão visível.

câmera: selfie de perto, fixa, sem movimento

som ambiente: corredor silencioso, sem música
```

### V12 · T12 · frame inicial = a imagem escolhida do K02

```text
V12
o avatar Jordan Vale, homem, fala em inglês com sotaque americano do Tennessee, voz masculina grave, devagar e gentil de um homem de cinquenta e oito anos do Tennessee, em tom de conversa de selfie, rápido e prático, voz autêntica, como se exigisse ser ouvido, a seguinte frase: "Now lower your hand and press save, so this message stays with you. Then tap the screen fast, so it stays open."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Jordan Vale baixa o olhar por um instante, para a tela, em "press save" e em "tap the screen", e volta a olhar para a lente.

câmera: selfie de perto, fixa, sem movimento

som ambiente: corredor silencioso, sem música
```

### V13 · T13 · frame inicial = a imagem escolhida do K02

```text
V13
o avatar Jordan Vale, homem, fala em inglês com sotaque americano do Tennessee, voz masculina grave, devagar e gentil de um homem de cinquenta e oito anos do Tennessee, em tom de conversa de selfie, caloroso e firme, voz autêntica, como se exigisse ser ouvido, a seguinte frase: "Do all of it, and tomorrow at 11 in the morning you will hear very good news. Do not skip a single step."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Jordan Vale fala olhando para a lente, com pequenas inclinações naturais da cabeça, sem nenhuma mão visível.

câmera: selfie de perto, fixa, sem movimento

som ambiente: corredor silencioso, sem música
```

### V14 · T14 · frame inicial = a imagem escolhida do K02

```text
V14
o avatar Jordan Vale, homem, fala em inglês com sotaque americano do Tennessee, voz masculina grave, devagar e gentil de um homem de cinquenta e oito anos do Tennessee, em tom de conversa de selfie, sério e baixo, voz autêntica, como se exigisse ser ouvido, a seguinte frase: "Pay close attention. This energy is very delicate, and the envy of others could break it completely."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Jordan Vale fala olhando para a lente, com pequenas inclinações naturais da cabeça, sem nenhuma mão visível.

câmera: selfie de perto, fixa, sem movimento

som ambiente: corredor silencioso, sem música
```

### V15 · T15 · frame inicial = a imagem escolhida do K02

```text
V15
o avatar Jordan Vale, homem, fala em inglês com sotaque americano do Tennessee, voz masculina grave, devagar e gentil de um homem de cinquenta e oito anos do Tennessee, em tom de conversa de selfie, próximo e acolhedor, voz autêntica, como se exigisse ser ouvido, a seguinte frase: "Now follow me, so the second part of this message can reach you, because it is already on its way."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Jordan Vale fala olhando para a lente, com pequenas inclinações naturais da cabeça, sem nenhuma mão visível.

câmera: selfie de perto, fixa, sem movimento

som ambiente: corredor silencioso, sem música
```

## 4. Montagem no CapCut

1. Clipes numerados na ordem: V01 a V15.
2. V01 (gancho mudo): usar ~4,5 s, até ela olhar para a lente, que é a transição para o V02. Sem tarja no topo: o modelo não tem.
3. V02 a V15: zero tempo morto, todo clipe começa já falando; cortar logo depois da última palavra. Isolate Voice / Keep Vocal. Todos saem do mesmo frame (K02), então a troca de clipe fica no mesmo enquadramento, como no modelo.
4. Do V02 ao V15, legenda branca karaokê no meio do quadro, a palavra falada em amarelo.
5. Sem seta para a foto de perfil: o CTA é follow. O `222` do V07 (antes da metade) pode levar um sinal de comentário pequeno na legenda.
6. Sem Voice Changer: a voz vem do prompt de cada V.
7. Música baixa por baixo da fala a partir do V02, entre -19 e -20 dB, fora da biblioteca do TikTok.
8. Rótulo pequeno `AI-generated` num canto do vídeo.

## 5. Transcrição final por take

| Take | English | Português |
|---|---|---|
| T1 | (sem fala) | (sem fala) |
| T2 | A family member of yours who is in heaven asked me to bring you a very important message. If you are ready to hear it, stay until the end. | Um familiar seu que está no céu me pediu para trazer uma mensagem muito importante pra você. Se você está pronta para ouvir, fique até o final. |
| T3 | You will be left speechless when you hear it. This one is only for you. Not everyone will see this video before the week is over. | Você vai ficar sem palavras quando ouvir isto. Esta é só pra você. Nem todo mundo vai ver este vídeo antes de a semana acabar. |
| T4 | I can't see your name, but I can feel you, and if this reached your screen today, it came as one last call to listen. | Eu não consigo ver o seu nome, mas eu sinto você, e se isto chegou na sua tela hoje, veio como um último chamado para ouvir. |
| T5 | A strong current of abundance, love and money is turning your way. Quietly, between us, the road to it just cleared. Everything heavy is behind you. | Uma forte corrente de abundância, amor e dinheiro está virando na sua direção. Em silêncio, só entre nós, o caminho até ela acabou de se abrir. Tudo que era pesado ficou pra trás. |
| T6 | I see a great deal of money and prosperity coming into your life. Before you comment, rest your right hand over your heart and listen to the end. | Eu vejo muito dinheiro e prosperidade entrando na sua vida. Antes de comentar, ponha a mão direita sobre o coração e ouça até o final. |
| T7 | Now write 222 below, so this message is marked with your name and the abundance I see knows where to land. | Agora escreva 222 aí embaixo, para esta mensagem ficar marcada com o seu nome e a abundância que eu vejo saber onde pousar. |
| T8 | Not everyone is meant to hear this, and you were picked to hear it. If you skip ahead now, the energy around you will scatter. | Nem todo mundo está destinado a ouvir isto, e você foi escolhida para ouvir. Se você pular agora, a energia ao seu redor vai se dispersar. |
| T9 | Something unusual is moving around you right now, and I can sense it. I see the chains that kept your prosperity locked away finally breaking apart. | Algo incomum está se movendo ao seu redor agora mesmo, e eu consigo sentir. Vejo as correntes que mantinham a sua prosperidade trancada finalmente se partindo. |
| T10 | The envy others sent your way is losing its hold on you. In the next 7 minutes, the heavy energy around you will be cleared away for good. | A inveja que os outros mandaram na sua direção está perdendo a força sobre você. Nos próximos 7 minutos, a energia pesada ao seu redor vai ser limpa de vez. |
| T11 | So forward this one to yourself this minute, because in 7 minutes you will return here to confirm this shift in your life. | Então encaminhe este pra você mesma neste minuto, porque em 7 minutos você vai retornar aqui para confirmar esta mudança na sua vida. |
| T12 | Now lower your hand and press save, so this message stays with you. Then tap the screen fast, so it stays open. | Agora abaixe a mão e aperte salvar, para esta mensagem ficar com você. Depois toque na tela rápido, para ela ficar aberta. |
| T13 | Do all of it, and tomorrow at 11 in the morning you will hear very good news. Do not skip a single step. | Faça tudo, e amanhã às 11 da manhã você vai ouvir uma notícia muito boa. Não pule nenhum passo. |
| T14 | Pay close attention. This energy is very delicate, and the envy of others could break it completely. | Preste muita atenção. Esta energia é muito delicada, e a inveja dos outros pode quebrá-la por completo. |
| T15 | Now follow me, so the second part of this message can reach you, because it is already on its way. | Agora me siga, para a segunda parte desta mensagem poder chegar até você, porque ela já está a caminho. |

## 6. Roteiro final em inglês

1. (sem fala: gancho mudo)
2. A family member of yours who is in heaven asked me to bring you a very important message. If you are ready to hear it, stay until the end.
3. You will be left speechless when you hear it. This one is only for you. Not everyone will see this video before the week is over.
4. I can't see your name, but I can feel you, and if this reached your screen today, it came as one last call to listen.
5. A strong current of abundance, love and money is turning your way. Quietly, between us, the road to it just cleared. Everything heavy is behind you.
6. I see a great deal of money and prosperity coming into your life. Before you comment, rest your right hand over your heart and listen to the end.
7. Now write 222 below, so this message is marked with your name and the abundance I see knows where to land.
8. Not everyone is meant to hear this, and you were picked to hear it. If you skip ahead now, the energy around you will scatter.
9. Something unusual is moving around you right now, and I can sense it. I see the chains that kept your prosperity locked away finally breaking apart.
10. The envy others sent your way is losing its hold on you. In the next 7 minutes, the heavy energy around you will be cleared away for good.
11. So forward this one to yourself this minute, because in 7 minutes you will return here to confirm this shift in your life.
12. Now lower your hand and press save, so this message stays with you. Then tap the screen fast, so it stays open.
13. Do all of it, and tomorrow at 11 in the morning you will hear very good news. Do not skip a single step.
14. Pay close attention. This energy is very delicate, and the envy of others could break it completely.
15. Now follow me, so the second part of this message can reach you, because it is already on its way.

A family member of yours who is in heaven asked me to bring you a very important message. If you are ready to hear it, stay until the end. You will be left speechless when you hear it. This one is only for you. Not everyone will see this video before the week is over. I can't see your name, but I can feel you, and if this reached your screen today, it came as one last call to listen. A strong current of abundance, love and money is turning your way. Quietly, between us, the road to it just cleared. Everything heavy is behind you. I see a great deal of money and prosperity coming into your life. Before you comment, rest your right hand over your heart and listen to the end. Now write 222 below, so this message is marked with your name and the abundance I see knows where to land. Not everyone is meant to hear this, and you were picked to hear it. If you skip ahead now, the energy around you will scatter. Something unusual is moving around you right now, and I can sense it. I see the chains that kept your prosperity locked away finally breaking apart. The envy others sent your way is losing its hold on you. In the next 7 minutes, the heavy energy around you will be cleared away for good. So forward this one to yourself this minute, because in 7 minutes you will return here to confirm this shift in your life. Now lower your hand and press save, so this message stays with you. Then tap the screen fast, so it stays open. Do all of it, and tomorrow at 11 in the morning you will hear very good news. Do not skip a single step. Pay close attention. This energy is very delicate, and the envy of others could break it completely. Now follow me, so the second part of this message can reach you, because it is already on its way.
