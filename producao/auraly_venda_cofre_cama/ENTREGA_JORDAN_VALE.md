# ENTREGA | Jordan Vale | Auraly Venda Cofre Cama (growth)

Produção `auraly_venda_cofre_cama` · Ângulo 3 · GROWTH · vídeo modelo de avatar IA · rodada de VALIDAÇÃO · perfil AURALY

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

Checklist de envio: 32/32 aprovados (N/A: A1, A2, A4, A9 fiéis ao modelo; A10 growth sem produto; C3 a C7 sem segunda pessoa, selfie, frase curta repetida, cena atuada ou motion control)

Ficha: 3/3 K conferidos contra o frame do modelo, placar 14/14 cada (`FICHA_FRAMES.md`, GATE_VISUAL Parte 6)

## Anexos e mapa

- **Character sheet Jordan Vale:** `producao/_ancoras/character_sheets/jordan_vale_character_sheet.jpg` no K01, K02 e K03 (identidade e roupa).
- **Frame do modelo** do mesmo código: `input/frames_modelo/K01_modelo.png`, `K02_modelo.png` e `K03_modelo.png` (cenário, ângulo e enquadramento).

```text
MAPA K/V
V01: K01
V02: K02
V03: K03
V04: K03
V05: K03
V06: K03
V07: K03
V08: K03
V09: K03
V10: K03
V11: K03
```

## 2. PROMPTS DE IMAGEM

### K01 · T1, gancho mudo, a cama de baú estofada colada na lente e o avatar prestes a levantá-la · anexar CHARACTER SHEET + FRAME DO MODELO

```text
K01
{
  "format": "IMPORTANT: THIS IS IPHONE FOOTAGE. Vertical 9:16.",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "reference_use": "Use the first attached image (character sheet) only for Jordan Vale's exact identity (face, skin, hair, body) and wardrobe; ignore its grey studio background. Use the second attached image (frame of the model video) as the reference for the setting, camera angle and framing; do not copy its person, clothes or on-screen text.",
  "identity_main": "The exact fictional AI character Jordan Vale, explicitly male: white American man around fifty-eight, long grey-white beard down to mid-chest, grey moustache, grey hair combed back short on the sides, sun-weathered skin with freckles and deep crow's feet, light grey eyes, both forearms covered in faded traditional American tattoos with no lettering, a swallow and a red rose on the left forearm.",
  "wardrobe": "Black leather vest over a heather grey crew-neck T-shirt, dark blue straight jeans, barefoot.",
  "scene": "The ordinary American master bedroom of the reference video: a charcoal-grey upholstered storage bed with a tufted headboard, made with a light grey-white duvet, a dark wooden nightstand on each side of the bed with a table lamp switched off, cream-beige walls and wall-to-wall beige carpet. On the right nightstand, next to the lamp, a small American flag (discreet but visible and in focus) stands in a small glass.",
  "prop": "The only object is the charcoal-grey upholstered storage bed, closed and made, with nothing visible underneath it. Jordan Vale rests one of his weathered hands with faded tattoos on the forearms on the edge of the duvet; the other hand hangs at his side.",
  "posture": "Jordan Vale stands upright beside the bed on the right side, one hand resting on the edge of the duvet, looking at the lens, mouth closed, about to lift the bed.",
  "composition": "The charcoal-grey upholstered storage bed with its tufted headboard is very close to the lens in the lower left foreground, about 40 percent of the frame, its near corner about 30 inches from the lens, closer to the camera than his face, nothing else competing with it. Jordan Vale is framed from the top of the head to the feet. Nothing else is in the foreground. The background is reduced by framing, never by blur.",
  "camera": "phone fixed on a tripod about four feet above the carpet, about eight feet from the bed, 1x lens, pointing level, fixed",
  "lighting": "Neutral overcast daylight coming in from a window just out of frame on the left, cool and even, the bedside lamps switched off, soft even light on the face and body with no harsh shadows.",
  "state": "Start frame: Jordan Vale stands with one hand on the duvet, the bed still closed, mouth closed.",
  "realism": "Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday reality, background fully in focus, everything in sharp focus, no AI polish, no beauty smoothing.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no studio, no grey studio background, no plastic-looking human skin, no extra fingers, no extra toes, no third hand, no supernatural lighting, no glowing objects, no blur, no bokeh, no artificial lighting, no warm orange color cast, no yellow tint on the skin, no golden glow, no golden hour light, no sunset, no de-aging, no beauty smoothing, no visible phone, no HDR, no cinematic lighting, no second person in frame, no tarot cards, no candles, no open hatch, no staircase yet, no money, no shoes, no socks"
}
```

### K02 · T2, descida, a escada de tábuas escondida vista de costas entre paredes de terra · anexar CHARACTER SHEET + FRAME DO MODELO

```text
K02
{
  "format": "IMPORTANT: THIS IS IPHONE FOOTAGE. Vertical 9:16.",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "reference_use": "Use the first attached image (character sheet) only for Jordan Vale's exact identity (face, skin, hair, body) and wardrobe; ignore its grey studio background. Use the second attached image (frame of the model video) as the reference for the setting, camera angle and framing; do not copy its person, clothes or on-screen text.",
  "identity_main": "The exact fictional AI character Jordan Vale, explicitly male: white American man around fifty-eight, long grey-white beard down to mid-chest, grey moustache, grey hair combed back short on the sides, sun-weathered skin with freckles and deep crow's feet, light grey eyes, both forearms covered in faded traditional American tattoos with no lettering, a swallow and a red rose on the left forearm.",
  "wardrobe": "Black leather vest over a heather grey crew-neck T-shirt, dark blue straight jeans, barefoot.",
  "scene": "The hidden cellar shaft of the reference video, seen from the bedroom above: a narrow wooden staircase of plain plank treads going down between rough brown earth walls held by dark wooden beams, with a bare white bulb hanging below and, at the top, the underside of the lifted grey bed platform with its wooden slats. On a wooden beam beside the stairs, a small American flag (discreet but visible and in focus) is pinned.",
  "prop": "The only object is the narrow wooden staircase going down between rough brown earth walls into the cellar shaft. Jordan Vale is already on it, seen from behind, one of his weathered hands with faded tattoos on the forearms on the wooden beam beside the stairs.",
  "posture": "Jordan Vale descends the staircase with his back to the lens, one foot already on a lower tread, the other hand reaching back toward the lifted bed platform, his head slightly turned down the stairs.",
  "composition": "The narrow wooden staircase fills the lower half of the frame, about 50 percent of the frame, its top tread about 24 inches from the lens, closer to the camera than his back, nothing else competing with it. Jordan Vale is framed from the top of the head to the hips, from behind. Nothing else is in the foreground. The background is reduced by framing, never by blur.",
  "camera": "phone held above and behind the person at the top of the stairs, about five feet above the carpet, 1x lens, pointing down the staircase, fixed",
  "lighting": "Neutral overcast daylight coming in from a window just out of frame on the left, cool and even, the bedside lamps switched off, soft even light on the face and body with no harsh shadows.",
  "state": "Start frame: Jordan Vale one step down the stairs, seen from behind, mid-stride.",
  "realism": "Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday reality, background fully in focus, everything in sharp focus, no AI polish, no beauty smoothing.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no studio, no grey studio background, no plastic-looking human skin, no extra fingers, no extra toes, no third hand, no supernatural lighting, no glowing objects, no blur, no bokeh, no artificial lighting, no warm orange color cast, no yellow tint on the skin, no golden glow, no golden hour light, no sunset, no de-aging, no beauty smoothing, no visible phone, no HDR, no cinematic lighting, no second person in frame, no tarot cards, no candles, no money yet, no face visible, no shoes, no socks, no smoke"
}
```

### K03 · T3 a T11, corpo, o avatar de pé no cofre segurando um maço de notas de 100 dólares na lente · anexar CHARACTER SHEET + FRAME DO MODELO

```text
K03
{
  "format": "IMPORTANT: THIS IS IPHONE FOOTAGE. Vertical 9:16.",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "reference_use": "Use the first attached image (character sheet) only for Jordan Vale's exact identity (face, skin, hair, body) and wardrobe; ignore its grey studio background. Use the second attached image (frame of the model video) as the reference for the setting, camera angle and framing; do not copy its person, clothes or on-screen text.",
  "identity_main": "The exact fictional AI character Jordan Vale, explicitly male: white American man around fifty-eight, long grey-white beard down to mid-chest, grey moustache, grey hair combed back short on the sides, sun-weathered skin with freckles and deep crow's feet, light grey eyes, both forearms covered in faded traditional American tattoos with no lettering, a swallow and a red rose on the left forearm.",
  "wardrobe": "Black leather vest over a heather grey crew-neck T-shirt, dark blue straight jeans, barefoot.",
  "scene": "The underground cellar vault of the reference video: rough brown earth walls, dark wooden posts and ceiling beams, a string of bare white bulbs hanging overhead, and behind the person plain wooden shelves holding stacks of hundred-dollar bills. On the wooden post at the left, a small American flag (discreet but visible and in focus) is pinned.",
  "prop": "The only object is a stack of hundred-dollar bills, thick, held together by an orange-tan paper strap around the middle, the top bill showing a portrait and the number 100, held up in one of his weathered hands with faded tattoos on the forearms toward the lens at chest height; the other hand hangs at his side.",
  "posture": "Jordan Vale stands inside the cellar vault facing the lens, holding the stack of bills up at chest height on the left of the frame, looking straight into the lens.",
  "composition": "The stack of hundred-dollar bills is very close to the lens in the lower left of the frame, about 15 percent of the frame, about 16 inches from the lens, closer to the camera than his face, nothing else competing with it. Jordan Vale is framed from the top of the head to the waist, his face in the upper half. Nothing else is in the foreground. The background is reduced by framing, never by blur.",
  "camera": "phone fixed on a small stand about five feet above the floor of the vault, about three feet from the person, 1x lens, pointing level, fixed",
  "lighting": "Neutral cool white light as flat and even as overcast daylight, from the bare bulbs overhead and from the open hatch above, no orange or amber glow on the walls or the skin, soft even light on the face with no harsh shadows.",
  "state": "Start frame: Jordan Vale caught mid-sentence, lips naturally parted, serious expression, the stack held still.",
  "realism": "Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday reality, background fully in focus, everything in sharp focus, no AI polish, no beauty smoothing.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no studio, no grey studio background, no plastic-looking human skin, no extra fingers, no extra toes, no third hand, no supernatural lighting, no glowing objects, no blur, no bokeh, no artificial lighting, no warm orange color cast, no yellow tint on the skin, no golden glow, no golden hour light, no sunset, no de-aging, no beauty smoothing, no visible phone, no HDR, no cinematic lighting, no second person in frame, no tarot cards, no candles, no money on the floor, no bills in the other hand, no shoes, no socks"
}
```

## 3. PROMPTS DE VÍDEO (um bloco por V)

### V01 · T1 · frame inicial = a imagem escolhida do K01

```text
V01
(sem fala no take: gancho mudo, o avatar fica em silêncio o clipe inteiro, boca fechada)

o que acontece no vídeo: Jordan Vale aperta a borda do colchão com as duas mãos e levanta a plataforma da cama de baú, que sobe devagar com um pistão e abre por baixo um poço retangular com uma escada de tábuas e uma lâmpada acesa lá no fundo; Jordan Vale segura a plataforma erguida com uma mão, olha para a lente e passa uma perna para dentro do poço.

câmera: fixa, sem movimento, um plano só, sem cortes

som ambiente: quarto silencioso, o pistão da cama subindo e o ranger leve da madeira, sem música
```

### V02 · T2 · frame inicial = a imagem escolhida do K02

```text
V02
(sem fala no take: o avatar fica em silêncio o clipe inteiro, boca fechada)

o que acontece no vídeo: plano 1, Jordan Vale de costas desce a escada de tábuas entre as paredes de terra; corte seco para o plano 2, o cofre subterrâneo aberto, Jordan Vale de costas no pé da escada com uma mão na parede, com prateleiras de madeira cheias de pilhas de notas de 100 dólares e um fio de lâmpadas brancas; corte seco para o plano 3, macro das pilhas de notas de 100 dólares com cinta de papel laranja, colado na lente; corte seco para o plano 4, de costas, a mão de Jordan Vale pega um maço da prateleira e Jordan Vale se vira para a lente segurando o maço no peito.

câmera: fixa, com três cortes secos internos ao clipe, sem movimento

som ambiente: passos na madeira, o eco leve do cofre e o papel das notas, sem música
```

### V03 · T3 · frame inicial = a imagem escolhida do K03

```text
V03
o avatar Jordan Vale, homem, fala em inglês com sotaque americano do Tennessee, voz masculina grave, devagar e gentil de um homem de cinquenta e oito anos do Tennessee, baixo, sério e conspiratório, voz autêntica, como se exigisse ser ouvido, a seguinte frase: "If you are watching this video today, stay silent after you watch it. No matter what happens, keep this to yourself."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Jordan Vale fala olhando fixo para a lente, com um pequeno aceno de cabeça. O maço de notas continua erguido na outra mão e o cofre atrás não muda.

câmera: fixa, sem movimento

som ambiente: cofre subterrâneo silencioso, um eco leve, sem música
```

### V04 · T4 · frame inicial = a imagem escolhida do K03

```text
V04
o avatar Jordan Vale, homem, fala em inglês com sotaque americano do Tennessee, voz masculina grave, devagar e gentil de um homem de cinquenta e oito anos do Tennessee, convicto e intenso, voz autêntica, como se exigisse ser ouvido, a seguinte frase: "Not your sister, not your best friend, not a single soul. Listen closely, because the most transformative day of your life is about to begin."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Jordan Vale balança a cabeça devagar, olhando fixo para a lente. O maço de notas continua erguido na outra mão e o cofre atrás não muda.

câmera: fixa, sem movimento

som ambiente: cofre subterrâneo silencioso, um eco leve, sem música
```

### V05 · T5 · frame inicial = a imagem escolhida do K03

```text
V05
o avatar Jordan Vale, homem, fala em inglês com sotaque americano do Tennessee, voz masculina grave, devagar e gentil de um homem de cinquenta e oito anos do Tennessee, urgente e direto, voz autêntica, como se exigisse ser ouvido, a seguinte frase: "Right now, comment 222 on this video, so the blessing knows where to find you. But if you keep scrolling, it could slip right through your fingers."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Jordan Vale aponta para baixo com a mão livre, para os comentários, e depois para a lente. O maço de notas continua erguido na outra mão e o cofre atrás não muda.

câmera: fixa, sem movimento

som ambiente: cofre subterrâneo silencioso, um eco leve, sem música
```

### V06 · T6 · frame inicial = a imagem escolhida do K03

```text
V06
o avatar Jordan Vale, homem, fala em inglês com sotaque americano do Tennessee, voz masculina grave, devagar e gentil de um homem de cinquenta e oito anos do Tennessee, firme e revelador, voz autêntica, como se exigisse ser ouvido, a seguinte frase: "Not everyone will see this before the week is over. I can't tell who you are, but I see wealth and prosperity coming into your life."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Jordan Vale fala olhando para a lente, com pequenos gestos naturais da mão livre. O maço de notas continua erguido na outra mão e o cofre atrás não muda.

câmera: fixa, sem movimento

som ambiente: cofre subterrâneo silencioso, um eco leve, sem música
```

### V07 · T7 · frame inicial = a imagem escolhida do K03

```text
V07
o avatar Jordan Vale, homem, fala em inglês com sotaque americano do Tennessee, voz masculina grave, devagar e gentil de um homem de cinquenta e oito anos do Tennessee, solene e intenso, voz autêntica, como se exigisse ser ouvido, a seguinte frase: "This message comes directly from Saint Michael, and it also calls for action. Something is shifting in your favor. A powerful blessing is heading your way with incredible force."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Jordan Vale fala olhando para a lente, com pequenos gestos naturais da mão livre. O maço de notas continua erguido na outra mão e o cofre atrás não muda.

câmera: fixa, sem movimento

som ambiente: cofre subterrâneo silencioso, um eco leve, sem música
```

### V08 · T8 · frame inicial = a imagem escolhida do K03

```text
V08
o avatar Jordan Vale, homem, fala em inglês com sotaque americano do Tennessee, voz masculina grave, devagar e gentil de um homem de cinquenta e oito anos do Tennessee, sério, em tom de aviso, voz autêntica, como se exigisse ser ouvido, a seguinte frase: "Acknowledge that this message is for you. But don't stop watching, or the news could pass you by. One last word from the universe, so take it seriously."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Jordan Vale ergue o dedo indicador da mão livre, como quem pede atenção. O maço de notas continua erguido na outra mão e o cofre atrás não muda.

câmera: fixa, sem movimento

som ambiente: cofre subterrâneo silencioso, um eco leve, sem música
```

### V09 · T9 · frame inicial = a imagem escolhida do K03

```text
V09
o avatar Jordan Vale, homem, fala em inglês com sotaque americano do Tennessee, voz masculina grave, devagar e gentil de um homem de cinquenta e oito anos do Tennessee, rápido e prático, voz autêntica, como se exigisse ser ouvido, a seguinte frase: "Tap like on this video, then save it, then send it to yourself. Each one locks this blessing in a little tighter."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Jordan Vale conta nos dedos da mão livre, um, dois, três, enquanto fala. O maço de notas continua erguido na outra mão e o cofre atrás não muda.

câmera: fixa, sem movimento

som ambiente: cofre subterrâneo silencioso, um eco leve, sem música
```

### V10 · T10 · frame inicial = a imagem escolhida do K03

```text
V10
o avatar Jordan Vale, homem, fala em inglês com sotaque americano do Tennessee, voz masculina grave, devagar e gentil de um homem de cinquenta e oito anos do Tennessee, calmo e confiante, voz autêntica, como se exigisse ser ouvido, a seguinte frase: "Do all three, and tomorrow, when you wake up, check your phone. You will receive good news."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Jordan Vale fala devagar, com um pequeno aceno de cabeça. O maço de notas continua erguido na outra mão e o cofre atrás não muda.

câmera: fixa, sem movimento

som ambiente: cofre subterrâneo silencioso, um eco leve, sem música
```

### V11 · T11 · frame inicial = a imagem escolhida do K03

```text
V11
o avatar Jordan Vale, homem, fala em inglês com sotaque americano do Tennessee, voz masculina grave, devagar e gentil de um homem de cinquenta e oito anos do Tennessee, próximo e urgente, voz autêntica, como se exigisse ser ouvido, a seguinte frase: "Now pay attention. Follow me before this disappears, because the next part of this message is already on its way to you."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Jordan Vale se inclina um pouco para a lente e aponta para ela com a mão livre. O maço de notas continua erguido na outra mão e o cofre atrás não muda.

câmera: fixa, sem movimento

som ambiente: cofre subterrâneo silencioso, um eco leve, sem música
```

## 4. Montagem no CapCut

1. Clipes numerados na ordem: V01 a V11.
2. V01 e V02 (gancho mudo): usar ~5,2 s do V01 e ~4,3 s do V02, emendados no corte da descida, como o modelo (~9,5 s no total). Texto no topo, duas linhas: "I see wealth coming into your life." / "Not a single soul.".
3. V03 a V11: zero tempo morto, todo clipe começa já falando; cortar logo depois da última palavra. Isolate Voice / Keep Vocal. Todos saem do mesmo frame (K03), então a troca de clipe fica no mesmo enquadramento, como no modelo.
4. Do V03 ao V11, legenda karaokê branca com a palavra falada em amarelo, no meio do quadro, como o modelo.
5. No V11, seta vermelha para baixo no canto inferior esquerdo. Sem seta para a foto de perfil: o CTA é follow.
6. Sem Voice Changer: a voz vem do prompt de cada V.
7. Som ambiente baixo no V01 e no V02 (pistão, passos); sem música por baixo da fala.
8. Rótulo pequeno `AI-generated` num canto do vídeo.

## 5. Transcrição final por take

| Take | English | Português |
|---|---|---|
| T1 | (sem fala) | (sem fala) |
| T2 | (sem fala) | (sem fala) |
| T3 | If you are watching this video today, stay silent after you watch it. No matter what happens, keep this to yourself. | Se você está assistindo a este vídeo hoje, fique em silêncio depois de assistir. Aconteça o que acontecer, guarde isto só pra você. |
| T4 | Not your sister, not your best friend, not a single soul. Listen closely, because the most transformative day of your life is about to begin. | Nem sua irmã, nem sua melhor amiga, nem uma única alma. Escute com atenção, porque o dia mais transformador da sua vida está prestes a começar. |
| T5 | Right now, comment 222 on this video, so the blessing knows where to find you. But if you keep scrolling, it could slip right through your fingers. | Agora mesmo, comente 222 neste vídeo, pra bênção saber onde te encontrar. Mas se você continuar rolando, ela pode escorrer pelos seus dedos. |
| T6 | Not everyone will see this before the week is over. I can't tell who you are, but I see wealth and prosperity coming into your life. | Nem todo mundo vai ver isto antes de a semana acabar. Eu não consigo dizer quem você é, mas vejo riqueza e prosperidade chegando na sua vida. |
| T7 | This message comes directly from Saint Michael, and it also calls for action. Something is shifting in your favor. A powerful blessing is heading your way with incredible force. | Esta mensagem vem direto de São Miguel, e ela também pede uma ação. Algo está mudando a seu favor. Uma bênção poderosa está indo na sua direção com uma força incrível. |
| T8 | Acknowledge that this message is for you. But don't stop watching, or the news could pass you by. One last word from the universe, so take it seriously. | Reconheça que esta mensagem é para você. Mas não pare de assistir, ou a notícia pode passar por você. Uma última palavra do universo, então leve isso a sério. |
| T9 | Tap like on this video, then save it, then send it to yourself. Each one locks this blessing in a little tighter. | Toque em curtir neste vídeo, depois salve, depois mande pra você mesma. Cada um deles prende esta bênção um pouco mais forte. |
| T10 | Do all three, and tomorrow, when you wake up, check your phone. You will receive good news. | Faça os três, e amanhã, quando acordar, olhe o seu celular. Você vai receber uma boa notícia. |
| T11 | Now pay attention. Follow me before this disappears, because the next part of this message is already on its way to you. | Agora preste atenção. Siga-me antes que isto desapareça, porque a próxima parte desta mensagem já está a caminho de você. |

## 6. Roteiro final em inglês

1. (sem fala: gancho mudo)
2. (sem fala: gancho mudo)
3. If you are watching this video today, stay silent after you watch it. No matter what happens, keep this to yourself.
4. Not your sister, not your best friend, not a single soul. Listen closely, because the most transformative day of your life is about to begin.
5. Right now, comment 222 on this video, so the blessing knows where to find you. But if you keep scrolling, it could slip right through your fingers.
6. Not everyone will see this before the week is over. I can't tell who you are, but I see wealth and prosperity coming into your life.
7. This message comes directly from Saint Michael, and it also calls for action. Something is shifting in your favor. A powerful blessing is heading your way with incredible force.
8. Acknowledge that this message is for you. But don't stop watching, or the news could pass you by. One last word from the universe, so take it seriously.
9. Tap like on this video, then save it, then send it to yourself. Each one locks this blessing in a little tighter.
10. Do all three, and tomorrow, when you wake up, check your phone. You will receive good news.
11. Now pay attention. Follow me before this disappears, because the next part of this message is already on its way to you.

If you are watching this video today, stay silent after you watch it. No matter what happens, keep this to yourself. Not your sister, not your best friend, not a single soul. Listen closely, because the most transformative day of your life is about to begin. Right now, comment 222 on this video, so the blessing knows where to find you. But if you keep scrolling, it could slip right through your fingers. Not everyone will see this before the week is over. I can't tell who you are, but I see wealth and prosperity coming into your life. This message comes directly from Saint Michael, and it also calls for action. Something is shifting in your favor. A powerful blessing is heading your way with incredible force. Acknowledge that this message is for you. But don't stop watching, or the news could pass you by. One last word from the universe, so take it seriously. Tap like on this video, then save it, then send it to yourself. Each one locks this blessing in a little tighter. Do all three, and tomorrow, when you wake up, check your phone. You will receive good news. Now pay attention. Follow me before this disappears, because the next part of this message is already on its way to you.
