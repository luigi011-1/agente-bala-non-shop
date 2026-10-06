# ENTREGA | holistic.brandon | Natural Rems Sea Moss | Pãezinhos de batata com abacate

Produção `brandon_seamoss_paes_abacate` · Ângulo 1 · VENDA · vídeo modelo de pessoa real · rodada de VALIDAÇÃO · perfil CLÁSSICO

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

Checklist de envio: 36/36 aprovados (N/A: A1, A2, A7 fiéis ao modelo; C3 sem segunda pessoa, C6 sem cena atuada, C7 sem motion control)

Ficha: 13/13 K conferidos contra o frame do modelo, placar 14/14 cada (`FICHA_FRAMES.md`, GATE_VISUAL Parte 6)

## Anexos

- **Âncora holistic.brandon:** `producao/_ancoras/holistic_brandon_ancora.jpg` em TODOS os K.
- **Em cada K**, anexar também o frame do modelo daquele passo (`producao/brandon_seamoss_paes_abacate/input/frames_modelo/Kxx_modelo.png`), só como referência de composição.
- **K11 a K13:** anexar também a foto do pote `producao/_ancoras/natural_rems_seamoss_produto.jpg` (só o pote da frente vale).
- K01 a K13 casam com V01 a V13 pelo número. V02 e V04 são B-roll com voz-over fora de quadro; os demais têm fala em quadro.

| Código | Take | Anexos além da âncora |
|---|---|---|
| K01 / V01 | T1, gancho, tigela de vidro colada na lente com a batata sendo amassada | `input/frames_modelo/K01_modelo.png` |
| K02 / V02 | T2, mãos moldando a bolinha de massa | `input/frames_modelo/K02_modelo.png` |
| K03 / V03 | T3, gergelim sobre as bolinhas | `input/frames_modelo/K03_modelo.png` |
| K04 / V04 | T4, assadeira entrando no forno de bancada | `input/frames_modelo/K04_modelo.png` |
| K05 / V05 | T5, assadeira dourada no colo | `input/frames_modelo/K05_modelo.png` |
| K06 / V06 | T6, pãozinho erguido na lente | `input/frames_modelo/K06_modelo.png` |
| K07 / V07 | T7, pão aberto ao meio na lente | `input/frames_modelo/K07_modelo.png` |
| K08 / V08 | T8, selfie, autoridade | `input/frames_modelo/K08_modelo.png` |
| K09 / V09 | T9, selfie, o corpo em guarda | `input/frames_modelo/K09_modelo.png` |
| K10 / V10 | T10, selfie, pergunta sem saída | `input/frames_modelo/K10_modelo.png` |
| K11 / V11 | T11, pote sobe no nome | `input/frames_modelo/K11_modelo.png` + `producao/_ancoras/natural_rems_seamoss_produto.jpg` |
| K12 / V12 | T12, comentário e follow, pote parado | `input/frames_modelo/K12_modelo.png` + `producao/_ancoras/natural_rems_seamoss_produto.jpg` |
| K13 / V13 | T13, CTA, pote parado e legível | `input/frames_modelo/K13_modelo.png` + `producao/_ancoras/natural_rems_seamoss_produto.jpg` |

## 2. PROMPTS DE IMAGEM (um bloco por K)

### K01 · T1, gancho, tigela de vidro colada na lente com a batata sendo amassada · anexar ÂNCORA HOLISTIC BRANDON + FRAME DO MODELO

```text
K01
{
  "format": "IMPORTANT: THIS IS IPHONE FOOTAGE. Vertical 9:16.",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "reference_use": "Use the first attached image only for Brandon's exact identity, wardrobe and her own garage gym. Use the second attached image only as a composition reference for the camera position, framing and the action; do not copy its man, his dreadlocks, his navy baseball cap, his white tank top, his kitchen or the caption text.",
  "identity_main": "The exact fictional AI character holistic.brandon: Black mixed-race American woman around thirty, athletic and toned, medium light-brown skin with light freckles across the nose and cheeks, dark brown eyes, defined eyebrows, full lips, hair in tight cornrows that turn into long loose braids falling over both shoulders, finished with small wooden and gold beads, a black floral blackwork tattoo sleeve on her right arm, a small line tattoo on her left upper arm and small fine-line tattoos on her chest near the collarbones. She reads as an ordinary anonymous American fitness coach, not resembling anyone famous.",
  "wardrobe": "Plain white ribbed tank top with nothing printed or written on it, loose black training shorts ending at mid-thigh, a thin gold chain with a small gold cross pendant and small stud earrings.",
  "scene": "Her own garage gym, the same room as the reference: a white-painted concrete block wall and a dark wooden slat ceiling, a red neon sign reading TRAIN PRAY REPEAT on the wall at the left, a whiteboard with handwritten black marker reading STAY READY. STAY DISCIPLINED. on the right, and a small American flag pinned above the whiteboard, discreet but clearly visible and in focus. The background is reduced by framing, never by blur.",
  "prop": "A large clear glass mixing bowl stands on the black table in front of her very close to the lens, holding three whole boiled yellow potatoes, one of them already half mashed. She grips a stainless steel potato masher in her right fist and presses it into the half mashed potato.",
  "posture": "Brandon stands behind the black table in front of her, leaning forward over it, seen from the waist up.",
  "composition": "Close shot from chest height: the phone lens is about 30 centimeters from the bowl, which fills the lower 50 percent of the frame almost edge to edge, closer to the camera than her face; her face and shoulders fill the upper part. Nothing else is on the table. The background is reduced by framing, never by blur.",
  "camera": "phone held at chest height about 30 centimeters from the bowl, standard 1x lens tilted slightly down",
  "lighting": "Neutral overcast daylight from a large window out of frame, soft even light on her face and hands with no harsh shadows. The red neon glows on the wall but does not tint her skin.",
  "state": "Start frame: the masher is pressed into the potato and the bowl has no avocado, eggs or yogurt yet. Brandon is caught mid-sentence, lips naturally parted, animated expression, looking straight into the lens.",
  "realism": "Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday reality, background fully in focus, everything in sharp focus, no AI polish, no beauty smoothing.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no studio, no plastic-looking skin, no extra fingers, no third hand, no blur, no bokeh, no warm orange color cast, no yellow tint, no golden glow, no golden hour light, no sunset, no HDR, no cinematic lighting, no de-aging, no beauty smoothing, no visible phone, no baseball cap, no kitchen cabinets, no man, no white marble counter, no second person, no readable lettering on the bowl, tray, oven or jars, no avocado in the bowl yet"
}
```

### K02 · T2, mãos moldando a bolinha de massa · anexar ÂNCORA HOLISTIC BRANDON + FRAME DO MODELO

```text
K02
{
  "format": "IMPORTANT: THIS IS IPHONE FOOTAGE. Vertical 9:16.",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "reference_use": "Use the first attached image only for Brandon's exact identity, wardrobe and her own garage gym. Use the second attached image only as a composition reference for the camera position, framing and the action; do not copy its man, his dreadlocks, his navy baseball cap, his white tank top, his kitchen or the caption text.",
  "identity_main": "The exact fictional AI character holistic.brandon: Black mixed-race American woman around thirty, athletic and toned, medium light-brown skin with light freckles across the nose and cheeks, dark brown eyes, defined eyebrows, full lips, hair in tight cornrows that turn into long loose braids falling over both shoulders, finished with small wooden and gold beads, a black floral blackwork tattoo sleeve on her right arm, a small line tattoo on her left upper arm and small fine-line tattoos on her chest near the collarbones. She reads as an ordinary anonymous American fitness coach, not resembling anyone famous.",
  "wardrobe": "Plain white ribbed tank top with nothing printed or written on it, loose black training shorts ending at mid-thigh, a thin gold chain with a small gold cross pendant and small stud earrings.",
  "scene": "Her own garage gym, the same room as the reference: a white-painted concrete block wall and a dark wooden slat ceiling, a red neon sign reading TRAIN PRAY REPEAT on the wall at the left, a whiteboard with handwritten black marker reading STAY READY. STAY DISCIPLINED. on the right, and a small American flag pinned above the whiteboard, discreet but clearly visible and in focus. The background is reduced by framing, never by blur.",
  "prop": "Her two hands shape one smooth pale dough ball over the black table in front of her; beside it lies a rectangular silver metal baking tray with five more pale round dough balls lined up on it.",
  "posture": "Brandon stands behind the black table in front of her, bent slightly forward, only her neck, chest and arms in frame, her chin just out of frame.",
  "composition": "Close shot from chest height: the phone lens is about 30 centimeters from her hands, which fill the lower 50 percent of the frame, closer to the camera than her chest; the upper part shows her tank top and chest. Nothing else is on the table. The background is reduced by framing, never by blur.",
  "camera": "phone held at chest height about 30 centimeters from her hands, standard 1x lens tilted slightly down",
  "lighting": "Neutral overcast daylight from a large window out of frame, soft even light on her face and hands with no harsh shadows. The red neon glows on the wall but does not tint her skin.",
  "state": "Start frame: the dough ball sits in her cupped hands, smooth and round. No speech in this take.",
  "realism": "Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday reality, background fully in focus, everything in sharp focus, no AI polish, no beauty smoothing.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no studio, no plastic-looking skin, no extra fingers, no third hand, no blur, no bokeh, no warm orange color cast, no yellow tint, no golden glow, no golden hour light, no sunset, no HDR, no cinematic lighting, no de-aging, no beauty smoothing, no visible phone, no baseball cap, no kitchen cabinets, no man, no white marble counter, no second person, no readable lettering on the bowl, tray, oven or jars"
}
```

### K03 · T3, gergelim sobre as bolinhas · anexar ÂNCORA HOLISTIC BRANDON + FRAME DO MODELO

```text
K03
{
  "format": "IMPORTANT: THIS IS IPHONE FOOTAGE. Vertical 9:16.",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "reference_use": "Use the first attached image only for Brandon's exact identity, wardrobe and her own garage gym. Use the second attached image only as a composition reference for the camera position, framing and the action; do not copy its man, his dreadlocks, his navy baseball cap, his white tank top, his kitchen or the caption text.",
  "identity_main": "The exact fictional AI character holistic.brandon: Black mixed-race American woman around thirty, athletic and toned, medium light-brown skin with light freckles across the nose and cheeks, dark brown eyes, defined eyebrows, full lips, hair in tight cornrows that turn into long loose braids falling over both shoulders, finished with small wooden and gold beads, a black floral blackwork tattoo sleeve on her right arm, a small line tattoo on her left upper arm and small fine-line tattoos on her chest near the collarbones. She reads as an ordinary anonymous American fitness coach, not resembling anyone famous.",
  "wardrobe": "Plain white ribbed tank top with nothing printed or written on it, loose black training shorts ending at mid-thigh, a thin gold chain with a small gold cross pendant and small stud earrings.",
  "scene": "Her own garage gym, the same room as the reference: a white-painted concrete block wall and a dark wooden slat ceiling, a red neon sign reading TRAIN PRAY REPEAT on the wall at the left, a whiteboard with handwritten black marker reading STAY READY. STAY DISCIPLINED. on the right, and a small American flag pinned above the whiteboard, discreet but clearly visible and in focus. The background is reduced by framing, never by blur.",
  "prop": "A rectangular silver metal baking tray stands on the black table in front of her very close to the lens with six round pale dough buns in two rows. Her right hand, raised above the tray, pinches white sesame seeds that are just starting to fall.",
  "posture": "Brandon stands behind the black table in front of her, leaning forward over it, seen from the waist up.",
  "composition": "Close shot from chest height: the phone lens is about 35 centimeters from the tray, which fills the lower 45 percent of the frame almost edge to edge, closer to the camera than her face; her face and shoulders fill the upper part. Nothing else is on the table. The background is reduced by framing, never by blur.",
  "camera": "phone held at chest height about 35 centimeters from the tray, standard 1x lens tilted slightly down",
  "lighting": "Neutral overcast daylight from a large window out of frame, soft even light on her face and hands with no harsh shadows. The red neon glows on the wall but does not tint her skin.",
  "state": "Start frame: only a few sesame seeds are on the buns. Brandon is caught mid-sentence, lips naturally parted, animated expression, looking straight into the lens, smiling.",
  "realism": "Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday reality, background fully in focus, everything in sharp focus, no AI polish, no beauty smoothing.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no studio, no plastic-looking skin, no extra fingers, no third hand, no blur, no bokeh, no warm orange color cast, no yellow tint, no golden glow, no golden hour light, no sunset, no HDR, no cinematic lighting, no de-aging, no beauty smoothing, no visible phone, no baseball cap, no kitchen cabinets, no man, no white marble counter, no second person, no readable lettering on the bowl, tray, oven or jars, no oven in the frame"
}
```

### K04 · T4, assadeira entrando no forno de bancada · anexar ÂNCORA HOLISTIC BRANDON + FRAME DO MODELO

```text
K04
{
  "format": "IMPORTANT: THIS IS IPHONE FOOTAGE. Vertical 9:16.",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "reference_use": "Use the first attached image only for Brandon's exact identity, wardrobe and her own garage gym. Use the second attached image only as a composition reference for the camera position, framing and the action; do not copy its man, his dreadlocks, his navy baseball cap, his white tank top, his kitchen or the caption text.",
  "identity_main": "The exact fictional AI character holistic.brandon: Black mixed-race American woman around thirty, athletic and toned, medium light-brown skin with light freckles across the nose and cheeks, dark brown eyes, defined eyebrows, full lips, hair in tight cornrows that turn into long loose braids falling over both shoulders, finished with small wooden and gold beads, a black floral blackwork tattoo sleeve on her right arm, a small line tattoo on her left upper arm and small fine-line tattoos on her chest near the collarbones. She reads as an ordinary anonymous American fitness coach, not resembling anyone famous.",
  "wardrobe": "Plain white ribbed tank top with nothing printed or written on it, loose black training shorts ending at mid-thigh, a thin gold chain with a small gold cross pendant and small stud earrings.",
  "scene": "Her own garage gym, the same room as the reference: a white-painted concrete block wall and a dark wooden slat ceiling, a red neon sign reading TRAIN PRAY REPEAT on the wall at the left, a whiteboard with handwritten black marker reading STAY READY. STAY DISCIPLINED. on the right, and a small American flag pinned above the whiteboard, discreet but clearly visible and in focus. The background is reduced by framing, never by blur.",
  "prop": "A small silver countertop electric oven stands at the left end of the black table in front of her, closer to the camera than she is, its glass door open. In profile, she slides a rectangular silver metal baking tray holding six pale sesame buns into it with both hands.",
  "posture": "Brandon stands in profile at the left end of the table, bent slightly forward, seen from the thighs up, not looking at the lens.",
  "composition": "Wide side shot from table height: the phone lens is about 1.2 meters from her and the oven is about 70 centimeters from the lens; the oven and the tray fill the lower 40 percent of the frame on the left, closer to the camera than her face; she fills the middle of the frame. The background is reduced by framing, never by blur.",
  "camera": "phone propped at table height about 1.2 meters from her, standard 1x lens, level",
  "lighting": "Neutral overcast daylight from a large window out of frame, soft even light on her face and hands with no harsh shadows. The red neon glows on the wall but does not tint her skin.",
  "state": "Start frame: the tray is half inside the oven. No speech in this take.",
  "realism": "Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday reality, background fully in focus, everything in sharp focus, no AI polish, no beauty smoothing.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no studio, no plastic-looking skin, no extra fingers, no third hand, no blur, no bokeh, no warm orange color cast, no yellow tint, no golden glow, no golden hour light, no sunset, no HDR, no cinematic lighting, no de-aging, no beauty smoothing, no visible phone, no baseball cap, no kitchen cabinets, no man, no white marble counter, no second person, no readable lettering on the bowl, tray, oven or jars, no smoke, no flames"
}
```

### K05 · T5, assadeira dourada no colo · anexar ÂNCORA HOLISTIC BRANDON + FRAME DO MODELO

```text
K05
{
  "format": "IMPORTANT: THIS IS IPHONE FOOTAGE. Vertical 9:16.",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "reference_use": "Use the first attached image only for Brandon's exact identity, wardrobe and her own garage gym. Use the second attached image only as a composition reference for the camera position, framing and the action; do not copy its man, his dreadlocks, his navy baseball cap, his white tank top, his kitchen or the caption text.",
  "identity_main": "The exact fictional AI character holistic.brandon: Black mixed-race American woman around thirty, athletic and toned, medium light-brown skin with light freckles across the nose and cheeks, dark brown eyes, defined eyebrows, full lips, hair in tight cornrows that turn into long loose braids falling over both shoulders, finished with small wooden and gold beads, a black floral blackwork tattoo sleeve on her right arm, a small line tattoo on her left upper arm and small fine-line tattoos on her chest near the collarbones. She reads as an ordinary anonymous American fitness coach, not resembling anyone famous.",
  "wardrobe": "Plain white ribbed tank top with nothing printed or written on it, loose black training shorts ending at mid-thigh, a thin gold chain with a small gold cross pendant and small stud earrings.",
  "scene": "Her own garage gym, the same room as the reference: a white-painted concrete block wall and a dark wooden slat ceiling, a red neon sign reading TRAIN PRAY REPEAT on the wall at the left, a whiteboard with handwritten black marker reading STAY READY. STAY DISCIPLINED. on the right, and a small American flag pinned above the whiteboard, discreet but clearly visible and in focus. The background is reduced by framing, never by blur.",
  "prop": "On her lap she holds a rectangular silver metal baking tray with both hands, with six golden-brown buns topped with sesame seeds, the tray tilted slightly toward the lens.",
  "posture": "Brandon sits on the edge of the black table in front of her, seen from the thighs up, the tray resting on her lap, her elbows out.",
  "composition": "Straight-on medium shot from table height: the phone lens is about 80 centimeters from her and the tray fills the lower 35 percent of the frame, closer to the camera than her face; her face and shoulders fill the upper two thirds. The background is reduced by framing, never by blur.",
  "camera": "phone propped at table height about 80 centimeters from her, standard 1x lens, level",
  "lighting": "Neutral overcast daylight from a large window out of frame, soft even light on her face and hands with no harsh shadows. The red neon glows on the wall but does not tint her skin.",
  "state": "Start frame: the golden buns are clearly visible on the tray. Brandon is caught mid-sentence, lips naturally parted, animated expression, looking straight into the lens.",
  "realism": "Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday reality, background fully in focus, everything in sharp focus, no AI polish, no beauty smoothing.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no studio, no plastic-looking skin, no extra fingers, no third hand, no blur, no bokeh, no warm orange color cast, no yellow tint, no golden glow, no golden hour light, no sunset, no HDR, no cinematic lighting, no de-aging, no beauty smoothing, no visible phone, no baseball cap, no kitchen cabinets, no man, no white marble counter, no second person, no readable lettering on the bowl, tray, oven or jars"
}
```

### K06 · T6, pãozinho erguido na lente · anexar ÂNCORA HOLISTIC BRANDON + FRAME DO MODELO

```text
K06
{
  "format": "IMPORTANT: THIS IS IPHONE FOOTAGE. Vertical 9:16.",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "reference_use": "Use the first attached image only for Brandon's exact identity, wardrobe and her own garage gym. Use the second attached image only as a composition reference for the camera position, framing and the action; do not copy its man, his dreadlocks, his navy baseball cap, his white tank top, his kitchen or the caption text.",
  "identity_main": "The exact fictional AI character holistic.brandon: Black mixed-race American woman around thirty, athletic and toned, medium light-brown skin with light freckles across the nose and cheeks, dark brown eyes, defined eyebrows, full lips, hair in tight cornrows that turn into long loose braids falling over both shoulders, finished with small wooden and gold beads, a black floral blackwork tattoo sleeve on her right arm, a small line tattoo on her left upper arm and small fine-line tattoos on her chest near the collarbones. She reads as an ordinary anonymous American fitness coach, not resembling anyone famous.",
  "wardrobe": "Plain white ribbed tank top with nothing printed or written on it, loose black training shorts ending at mid-thigh, a thin gold chain with a small gold cross pendant and small stud earrings.",
  "scene": "Her own garage gym, the same room as the reference: a white-painted concrete block wall and a dark wooden slat ceiling, a red neon sign reading TRAIN PRAY REPEAT on the wall at the left, a whiteboard with handwritten black marker reading STAY READY. STAY DISCIPLINED. on the right, and a small American flag pinned above the whiteboard, discreet but clearly visible and in focus. The background is reduced by framing, never by blur.",
  "prop": "Raised with both hands in front of her chest she holds one round golden-brown bun with a shiny crust and a few sesame seeds, close to the lens.",
  "posture": "Brandon stands behind the black table in front of her, seen from the chest up, the bun held toward the camera.",
  "composition": "Close shot from chest height: the phone lens is about 25 centimeters from the bun, which fills about 35 percent of the frame in the lower center, closer to the camera than her face; her face fills the upper half. The table is empty. The background is reduced by framing, never by blur.",
  "camera": "phone held at chest height about 25 centimeters from the bun, standard 1x lens, level",
  "lighting": "Neutral overcast daylight from a large window out of frame, soft even light on her face and hands with no harsh shadows. The red neon glows on the wall but does not tint her skin.",
  "state": "Start frame: the bun is raised and its crust is clearly visible. Brandon is caught mid-sentence, lips naturally parted, animated expression, looking straight into the lens.",
  "realism": "Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday reality, background fully in focus, everything in sharp focus, no AI polish, no beauty smoothing.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no studio, no plastic-looking skin, no extra fingers, no third hand, no blur, no bokeh, no warm orange color cast, no yellow tint, no golden glow, no golden hour light, no sunset, no HDR, no cinematic lighting, no de-aging, no beauty smoothing, no visible phone, no baseball cap, no kitchen cabinets, no man, no white marble counter, no second person, no readable lettering on the bowl, tray, oven or jars"
}
```

### K07 · T7, pão aberto ao meio na lente · anexar ÂNCORA HOLISTIC BRANDON + FRAME DO MODELO

```text
K07
{
  "format": "IMPORTANT: THIS IS IPHONE FOOTAGE. Vertical 9:16.",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "reference_use": "Use the first attached image only for Brandon's exact identity, wardrobe and her own garage gym. Use the second attached image only as a composition reference for the camera position, framing and the action; do not copy its man, his dreadlocks, his navy baseball cap, his white tank top, his kitchen or the caption text.",
  "identity_main": "The exact fictional AI character holistic.brandon: Black mixed-race American woman around thirty, athletic and toned, medium light-brown skin with light freckles across the nose and cheeks, dark brown eyes, defined eyebrows, full lips, hair in tight cornrows that turn into long loose braids falling over both shoulders, finished with small wooden and gold beads, a black floral blackwork tattoo sleeve on her right arm, a small line tattoo on her left upper arm and small fine-line tattoos on her chest near the collarbones. She reads as an ordinary anonymous American fitness coach, not resembling anyone famous.",
  "wardrobe": "Plain white ribbed tank top with nothing printed or written on it, loose black training shorts ending at mid-thigh, a thin gold chain with a small gold cross pendant and small stud earrings.",
  "scene": "Her own garage gym, the same room as the reference: a white-painted concrete block wall and a dark wooden slat ceiling, a red neon sign reading TRAIN PRAY REPEAT on the wall at the left, a whiteboard with handwritten black marker reading STAY READY. STAY DISCIPLINED. on the right, and a small American flag pinned above the whiteboard, discreet but clearly visible and in focus. The background is reduced by framing, never by blur.",
  "prop": "She holds a golden-brown bun torn open in two halves, one half in each hand, side by side in front of her chest, showing a soft airy fluffy crumb with small holes.",
  "posture": "Brandon stands behind the black table in front of her, seen from the chest up, the two halves held toward the camera.",
  "composition": "Close shot from chest height: the phone lens is about 20 centimeters from the two halves, which fill about 40 percent of the frame in the lower center, closer to the camera than her face; her face fills the upper half. The table is empty. The background is reduced by framing, never by blur.",
  "camera": "phone held at chest height about 20 centimeters from the buns, standard 1x lens, level",
  "lighting": "Neutral overcast daylight from a large window out of frame, soft even light on her face and hands with no harsh shadows. The red neon glows on the wall but does not tint her skin.",
  "state": "Start frame: the two torn halves are side by side and the crumb is clearly visible. Brandon is caught mid-sentence, lips naturally parted, animated expression, looking straight into the lens.",
  "realism": "Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday reality, background fully in focus, everything in sharp focus, no AI polish, no beauty smoothing.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no studio, no plastic-looking skin, no extra fingers, no third hand, no blur, no bokeh, no warm orange color cast, no yellow tint, no golden glow, no golden hour light, no sunset, no HDR, no cinematic lighting, no de-aging, no beauty smoothing, no visible phone, no baseball cap, no kitchen cabinets, no man, no white marble counter, no second person, no readable lettering on the bowl, tray, oven or jars"
}
```

### K08 · T8, selfie, autoridade · anexar ÂNCORA HOLISTIC BRANDON + FRAME DO MODELO

```text
K08
{
  "format": "IMPORTANT: THIS IS IPHONE FOOTAGE. Vertical 9:16.",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "reference_use": "Use the first attached image only for Brandon's exact identity, wardrobe and her own garage gym. Use the second attached image only as a composition reference for the camera position, framing and the action; do not copy its man, his dreadlocks, his navy baseball cap, his white tank top, his kitchen or the caption text.",
  "identity_main": "The exact fictional AI character holistic.brandon: Black mixed-race American woman around thirty, athletic and toned, medium light-brown skin with light freckles across the nose and cheeks, dark brown eyes, defined eyebrows, full lips, hair in tight cornrows that turn into long loose braids falling over both shoulders, finished with small wooden and gold beads, a black floral blackwork tattoo sleeve on her right arm, a small line tattoo on her left upper arm and small fine-line tattoos on her chest near the collarbones. She reads as an ordinary anonymous American fitness coach, not resembling anyone famous.",
  "wardrobe": "Plain white ribbed tank top with nothing printed or written on it, loose black training shorts ending at mid-thigh, a thin gold chain with a small gold cross pendant and small stud earrings.",
  "scene": "Her own garage gym, the same room as the reference: a white-painted concrete block wall and a dark wooden slat ceiling, a red neon sign reading TRAIN PRAY REPEAT on the wall at the left, a whiteboard with handwritten black marker reading STAY READY. STAY DISCIPLINED. on the right, and a small American flag pinned above the whiteboard, discreet but clearly visible and in focus. The background is reduced by framing, never by blur.",
  "prop": "In her low right hand she holds one round golden-brown bun with a shiny crust and a few sesame seeds, held low at the bottom of the frame.",
  "posture": "Brandon stands in her garage gym in front of the whiteboard, seen from the chest up, one arm extended holding the phone.",
  "composition": "Selfie shot: the phone lens is about 50 centimeters from her face; her face and shoulders fill the frame down to the chest and the bun in her low hand sits in the lower-left corner, closer to the camera than her face. The background is reduced by framing, never by blur.",
  "camera": "phone held at arm's length at eye height about 50 centimeters from her face, standard 1x lens, level, slightly handheld",
  "lighting": "Neutral overcast daylight from a large window out of frame, soft even light on her face and hands with no harsh shadows. The red neon glows on the wall but does not tint her skin.",
  "state": "Start frame: Brandon is caught mid-sentence, lips naturally parted, animated expression, looking straight into the lens, sincere and close.",
  "realism": "Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday reality, background fully in focus, everything in sharp focus, no AI polish, no beauty smoothing.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no studio, no plastic-looking skin, no extra fingers, no third hand, no blur, no bokeh, no warm orange color cast, no yellow tint, no golden glow, no golden hour light, no sunset, no HDR, no cinematic lighting, no de-aging, no beauty smoothing, no visible phone, no baseball cap, no kitchen cabinets, no man, no white marble counter, no second person"
}
```

### K09 · T9, selfie, o corpo em guarda · anexar ÂNCORA HOLISTIC BRANDON + FRAME DO MODELO

```text
K09
{
  "format": "IMPORTANT: THIS IS IPHONE FOOTAGE. Vertical 9:16.",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "reference_use": "Use the first attached image only for Brandon's exact identity, wardrobe and her own garage gym. Use the second attached image only as a composition reference for the camera position, framing and the action; do not copy its man, his dreadlocks, his navy baseball cap, his white tank top, his kitchen or the caption text.",
  "identity_main": "The exact fictional AI character holistic.brandon: Black mixed-race American woman around thirty, athletic and toned, medium light-brown skin with light freckles across the nose and cheeks, dark brown eyes, defined eyebrows, full lips, hair in tight cornrows that turn into long loose braids falling over both shoulders, finished with small wooden and gold beads, a black floral blackwork tattoo sleeve on her right arm, a small line tattoo on her left upper arm and small fine-line tattoos on her chest near the collarbones. She reads as an ordinary anonymous American fitness coach, not resembling anyone famous.",
  "wardrobe": "Plain white ribbed tank top with nothing printed or written on it, loose black training shorts ending at mid-thigh, a thin gold chain with a small gold cross pendant and small stud earrings.",
  "scene": "Her own garage gym, the same room as the reference: a white-painted concrete block wall and a dark wooden slat ceiling, a red neon sign reading TRAIN PRAY REPEAT on the wall at the left, a whiteboard with handwritten black marker reading STAY READY. STAY DISCIPLINED. on the right, and a small American flag pinned above the whiteboard, discreet but clearly visible and in focus. The background is reduced by framing, never by blur.",
  "prop": "In her low right hand she holds one round golden-brown bun with a shiny crust and a few sesame seeds, lowered and relaxed at the bottom of the frame.",
  "posture": "Brandon stands in her garage gym in front of the whiteboard, seen from the chest up, one arm extended holding the phone.",
  "composition": "Selfie shot: the phone lens is about 50 centimeters from her face; her face and shoulders fill the frame down to the chest and the bun in her low hand sits in the lower-left corner, closer to the camera than her face. The background is reduced by framing, never by blur.",
  "camera": "phone held at arm's length at eye height about 50 centimeters from her face, standard 1x lens, level, slightly handheld",
  "lighting": "Neutral overcast daylight from a large window out of frame, soft even light on her face and hands with no harsh shadows. The red neon glows on the wall but does not tint her skin.",
  "state": "Start frame: Brandon is caught mid-sentence, lips naturally parted, animated expression, looking straight into the lens, warm and sure of herself.",
  "realism": "Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday reality, background fully in focus, everything in sharp focus, no AI polish, no beauty smoothing.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no studio, no plastic-looking skin, no extra fingers, no third hand, no blur, no bokeh, no warm orange color cast, no yellow tint, no golden glow, no golden hour light, no sunset, no HDR, no cinematic lighting, no de-aging, no beauty smoothing, no visible phone, no baseball cap, no kitchen cabinets, no man, no white marble counter, no second person"
}
```

### K10 · T10, selfie, pergunta sem saída · anexar ÂNCORA HOLISTIC BRANDON + FRAME DO MODELO

```text
K10
{
  "format": "IMPORTANT: THIS IS IPHONE FOOTAGE. Vertical 9:16.",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "reference_use": "Use the first attached image only for Brandon's exact identity, wardrobe and her own garage gym. Use the second attached image only as a composition reference for the camera position, framing and the action; do not copy its man, his dreadlocks, his navy baseball cap, his white tank top, his kitchen or the caption text.",
  "identity_main": "The exact fictional AI character holistic.brandon: Black mixed-race American woman around thirty, athletic and toned, medium light-brown skin with light freckles across the nose and cheeks, dark brown eyes, defined eyebrows, full lips, hair in tight cornrows that turn into long loose braids falling over both shoulders, finished with small wooden and gold beads, a black floral blackwork tattoo sleeve on her right arm, a small line tattoo on her left upper arm and small fine-line tattoos on her chest near the collarbones. She reads as an ordinary anonymous American fitness coach, not resembling anyone famous.",
  "wardrobe": "Plain white ribbed tank top with nothing printed or written on it, loose black training shorts ending at mid-thigh, a thin gold chain with a small gold cross pendant and small stud earrings.",
  "scene": "Her own garage gym, the same room as the reference: a white-painted concrete block wall and a dark wooden slat ceiling, a red neon sign reading TRAIN PRAY REPEAT on the wall at the left, a whiteboard with handwritten black marker reading STAY READY. STAY DISCIPLINED. on the right, and a small American flag pinned above the whiteboard, discreet but clearly visible and in focus. The background is reduced by framing, never by blur.",
  "prop": "Her hands are empty and out of frame.",
  "posture": "Brandon stands in her garage gym in front of the whiteboard, seen from the chest up, one arm extended holding the phone, her head tilted slightly.",
  "composition": "Selfie shot: the phone lens is about 45 centimeters from her face; her face and shoulders fill the frame down to the chest and her extended forearm crosses the lower-left corner, closer to the camera than her face. The background is reduced by framing, never by blur.",
  "camera": "phone held at arm's length at eye height about 45 centimeters from her face, standard 1x lens, level, slightly handheld",
  "lighting": "Neutral overcast daylight from a large window out of frame, soft even light on her face and hands with no harsh shadows. The red neon glows on the wall but does not tint her skin.",
  "state": "Start frame: Brandon is caught mid-sentence, lips naturally parted, animated expression, looking straight into the lens, curious, with a hint of a question in her eyes.",
  "realism": "Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday reality, background fully in focus, everything in sharp focus, no AI polish, no beauty smoothing.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no studio, no plastic-looking skin, no extra fingers, no third hand, no blur, no bokeh, no warm orange color cast, no yellow tint, no golden glow, no golden hour light, no sunset, no HDR, no cinematic lighting, no de-aging, no beauty smoothing, no visible phone, no baseball cap, no kitchen cabinets, no man, no white marble counter, no second person"
}
```

### K11 · T11, pote sobe no nome · anexar ÂNCORA HOLISTIC BRANDON + FRAME DO MODELO + FOTO DO POTE

```text
K11
{
  "format": "IMPORTANT: THIS IS IPHONE FOOTAGE. Vertical 9:16.",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "reference_use": "Use the first attached image only for Brandon's exact identity, wardrobe and her own garage gym. Use the second attached image only as a composition reference for the camera position, framing and the action; do not copy its man, his dreadlocks, his navy baseball cap, his white tank top, his kitchen or the caption text. Use the third attached image only for the exact look of the front jar and its label; ignore the MADE IN USA banner, the second jar with the Supplement Facts panel and the loose gummies.",
  "identity_main": "The exact fictional AI character holistic.brandon: Black mixed-race American woman around thirty, athletic and toned, medium light-brown skin with light freckles across the nose and cheeks, dark brown eyes, defined eyebrows, full lips, hair in tight cornrows that turn into long loose braids falling over both shoulders, finished with small wooden and gold beads, a black floral blackwork tattoo sleeve on her right arm, a small line tattoo on her left upper arm and small fine-line tattoos on her chest near the collarbones. She reads as an ordinary anonymous American fitness coach, not resembling anyone famous.",
  "wardrobe": "Plain white ribbed tank top with nothing printed or written on it, loose black training shorts ending at mid-thigh, a thin gold chain with a small gold cross pendant and small stud earrings.",
  "scene": "Her own garage gym, the same room as the reference: a white-painted concrete block wall and a dark wooden slat ceiling, a red neon sign reading TRAIN PRAY REPEAT on the wall at the left, a whiteboard with handwritten black marker reading STAY READY. STAY DISCIPLINED. on the right, and a small American flag pinned above the whiteboard, discreet but clearly visible and in focus. The background is reduced by framing, never by blur.",
  "prop": "Raised with both hands in front of her chest, she holds the Natural Rems Sea Moss Gummies jar exactly as in the attached product photo: a short wide jar of dark amber plastic with a black screw cap, a pale sage-green label with dark green text, the Natural Rems logo with three leaves at the top, the big title Sea Moss Gummies, a pill-shaped badge reading 6000 MG | 16-IN-1, the line GREEN APPLE FLAVOR, two columns of dark green ingredient pills, green seaweed illustrations on the sides and a small 30 Gummies badge. The label is turned straight to the lens and fully readable, her fingers only on the sides of the jar.",
  "posture": "Brandon stands behind the black table in front of her, seen from the waist up, holding the jar toward the camera.",
  "composition": "Straight-on medium shot from table height: the phone lens is about 40 centimeters from the jar, which fills about 25 percent of the frame in the lower center, closer to the camera than her face; her face and shoulders fill the upper half. The table is empty. The background is reduced by framing, never by blur.",
  "camera": "phone propped at table height about 40 centimeters from the jar, standard 1x lens, level",
  "lighting": "Neutral overcast daylight from a large window out of frame, soft even light on her face and hands with no harsh shadows. The red neon glows on the wall but does not tint her skin.",
  "state": "Start frame: Brandon is smiling and caught mid-sentence, lips naturally parted, animated expression, looking straight into the lens.",
  "realism": "Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday reality, background fully in focus, everything in sharp focus, no AI polish, no beauty smoothing.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no studio, no plastic-looking skin, no extra fingers, no third hand, no blur, no bokeh, no warm orange color cast, no yellow tint, no golden glow, no golden hour light, no sunset, no HDR, no cinematic lighting, no de-aging, no beauty smoothing, no visible phone, no baseball cap, no kitchen cabinets, no man, no white marble counter, no second person, no second jar, no loose gummies, no banner on the jar, no fingers over the label"
}
```

### K12 · T12, comentário e follow, pote parado · anexar ÂNCORA HOLISTIC BRANDON + FRAME DO MODELO + FOTO DO POTE

```text
K12
{
  "format": "IMPORTANT: THIS IS IPHONE FOOTAGE. Vertical 9:16.",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "reference_use": "Use the first attached image only for Brandon's exact identity, wardrobe and her own garage gym. Use the second attached image only as a composition reference for the camera position, framing and the action; do not copy its man, his dreadlocks, his navy baseball cap, his white tank top, his kitchen or the caption text. Use the third attached image only for the exact look of the front jar and its label; ignore the MADE IN USA banner, the second jar with the Supplement Facts panel and the loose gummies.",
  "identity_main": "The exact fictional AI character holistic.brandon: Black mixed-race American woman around thirty, athletic and toned, medium light-brown skin with light freckles across the nose and cheeks, dark brown eyes, defined eyebrows, full lips, hair in tight cornrows that turn into long loose braids falling over both shoulders, finished with small wooden and gold beads, a black floral blackwork tattoo sleeve on her right arm, a small line tattoo on her left upper arm and small fine-line tattoos on her chest near the collarbones. She reads as an ordinary anonymous American fitness coach, not resembling anyone famous.",
  "wardrobe": "Plain white ribbed tank top with nothing printed or written on it, loose black training shorts ending at mid-thigh, a thin gold chain with a small gold cross pendant and small stud earrings.",
  "scene": "Her own garage gym, the same room as the reference: a white-painted concrete block wall and a dark wooden slat ceiling, a red neon sign reading TRAIN PRAY REPEAT on the wall at the left, a whiteboard with handwritten black marker reading STAY READY. STAY DISCIPLINED. on the right, and a small American flag pinned above the whiteboard, discreet but clearly visible and in focus. The background is reduced by framing, never by blur.",
  "prop": "Perfectly still with both hands in front of her chest, centered, she holds the Natural Rems Sea Moss Gummies jar exactly as in the attached product photo: a short wide jar of dark amber plastic with a black screw cap, a pale sage-green label with dark green text, the Natural Rems logo with three leaves at the top, the big title Sea Moss Gummies, a pill-shaped badge reading 6000 MG | 16-IN-1, the line GREEN APPLE FLAVOR, two columns of dark green ingredient pills, green seaweed illustrations on the sides and a small 30 Gummies badge. The label is turned straight to the lens, fully readable and with nothing covering it.",
  "posture": "Brandon stands behind the black table in front of her, seen from the waist up, holding the jar toward the camera.",
  "composition": "Straight-on medium shot from table height: the phone lens is about 40 centimeters from the jar, which fills about 25 percent of the frame in the lower center, closer to the camera than her face; her face and shoulders fill the upper half. The table is empty. The background is reduced by framing, never by blur.",
  "camera": "phone propped at table height about 40 centimeters from the jar, standard 1x lens, level",
  "lighting": "Neutral overcast daylight from a large window out of frame, soft even light on her face and hands with no harsh shadows. The red neon glows on the wall but does not tint her skin.",
  "state": "Start frame: Brandon is caught mid-sentence, lips naturally parted, animated expression, looking straight into the lens, warm and inviting.",
  "realism": "Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday reality, background fully in focus, everything in sharp focus, no AI polish, no beauty smoothing.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no studio, no plastic-looking skin, no extra fingers, no third hand, no blur, no bokeh, no warm orange color cast, no yellow tint, no golden glow, no golden hour light, no sunset, no HDR, no cinematic lighting, no de-aging, no beauty smoothing, no visible phone, no baseball cap, no kitchen cabinets, no man, no white marble counter, no second person, no second jar, no loose gummies, no banner on the jar, no fingers over the label"
}
```

### K13 · T13, CTA, pote parado e legível · anexar ÂNCORA HOLISTIC BRANDON + FRAME DO MODELO + FOTO DO POTE

```text
K13
{
  "format": "IMPORTANT: THIS IS IPHONE FOOTAGE. Vertical 9:16.",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "reference_use": "Use the first attached image only for Brandon's exact identity, wardrobe and her own garage gym. Use the second attached image only as a composition reference for the camera position, framing and the action; do not copy its man, his dreadlocks, his navy baseball cap, his white tank top, his kitchen or the caption text. Use the third attached image only for the exact look of the front jar and its label; ignore the MADE IN USA banner, the second jar with the Supplement Facts panel and the loose gummies.",
  "identity_main": "The exact fictional AI character holistic.brandon: Black mixed-race American woman around thirty, athletic and toned, medium light-brown skin with light freckles across the nose and cheeks, dark brown eyes, defined eyebrows, full lips, hair in tight cornrows that turn into long loose braids falling over both shoulders, finished with small wooden and gold beads, a black floral blackwork tattoo sleeve on her right arm, a small line tattoo on her left upper arm and small fine-line tattoos on her chest near the collarbones. She reads as an ordinary anonymous American fitness coach, not resembling anyone famous.",
  "wardrobe": "Plain white ribbed tank top with nothing printed or written on it, loose black training shorts ending at mid-thigh, a thin gold chain with a small gold cross pendant and small stud earrings.",
  "scene": "Her own garage gym, the same room as the reference: a white-painted concrete block wall and a dark wooden slat ceiling, a red neon sign reading TRAIN PRAY REPEAT on the wall at the left, a whiteboard with handwritten black marker reading STAY READY. STAY DISCIPLINED. on the right, and a small American flag pinned above the whiteboard, discreet but clearly visible and in focus. The background is reduced by framing, never by blur.",
  "prop": "Perfectly still with both hands in front of her chest, centered, she holds the Natural Rems Sea Moss Gummies jar exactly as in the attached product photo: a short wide jar of dark amber plastic with a black screw cap, a pale sage-green label with dark green text, the Natural Rems logo with three leaves at the top, the big title Sea Moss Gummies, a pill-shaped badge reading 6000 MG | 16-IN-1, the line GREEN APPLE FLAVOR, two columns of dark green ingredient pills, green seaweed illustrations on the sides and a small 30 Gummies badge. The label is turned straight to the lens, fully readable and with nothing covering it.",
  "posture": "Brandon stands behind the black table in front of her, seen from the chest up, holding the jar toward the camera.",
  "composition": "The tightest shot of the video, straight-on from chest height: the phone lens is about 35 centimeters from the jar, which fills about 30 percent of the frame in the lower center, closer to the camera than her face; her face fills the upper half. The background is reduced by framing, never by blur.",
  "camera": "phone propped at chest height, standard 1x lens, level",
  "lighting": "Neutral overcast daylight from a large window out of frame, soft even light on her face and hands with no harsh shadows. The red neon glows on the wall but does not tint her skin.",
  "state": "Start frame: Brandon is caught mid-sentence, lips naturally parted, animated expression, looking straight into the lens, clear and calm.",
  "realism": "Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday reality, background fully in focus, everything in sharp focus, no AI polish, no beauty smoothing.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no studio, no plastic-looking skin, no extra fingers, no third hand, no blur, no bokeh, no warm orange color cast, no yellow tint, no golden glow, no golden hour light, no sunset, no HDR, no cinematic lighting, no de-aging, no beauty smoothing, no visible phone, no baseball cap, no kitchen cabinets, no man, no white marble counter, no second person, no second jar, no loose gummies, no banner on the jar, no fingers over the label"
}
```

## 3. PROMPTS DE VÍDEO (um bloco por V)

### V01 · T1 · frame inicial = a imagem que você deixou no K01

```text
V01
a avatar Brandon, mulher, fala em inglês com sotaque americano de uma mulher negra americana, voz feminina clara e firme de uma mulher de uns trinta anos, entonação intrigante, como quem vai mostrar um truque de cozinha, voz autêntica, como se exigisse ser ouvida, a seguinte frase: "Did you know that if you mash one boiled potato with avocado, add eggs, Greek yogurt, baking powder, salt, and mix everything"

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Brandon amassa uma batata cozida com o espremedor e a câmera acompanha a tigela: entram metades de abacate, ovos, uma colherada de iogurte grego, uma pitada de fermento e de sal, e ela mistura tudo com uma colher de madeira até virar uma massa verde-clara.

câmera: leve handheld

som ambiente: box de treino em casa, tranquilo, colher batendo no vidro, sem música
```

### V02 · T2 · frame inicial = a imagem que você deixou no K02

```text
V02
a voz da avatar Brandon, fora de quadro (voz-over, ela não aparece falando), em inglês com sotaque americano de uma mulher negra americana, voz feminina clara e firme de uma mulher de uns trinta anos, entonação didática e rápida, voz-over calma, diz a seguinte frase: "together until smooth, then shape it into buns,"

a voz diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Nenhuma boca visível no quadro.

o que acontece no vídeo: As mãos de Brandon sovam a massa lisa numa bolinha clara e a pousam na assadeira ao lado de outras bolinhas.

câmera: leve handheld

som ambiente: box de treino em casa, tranquilo, massa sendo sovada, sem música
```

### V03 · T3 · frame inicial = a imagem que você deixou no K03

```text
V03
a avatar Brandon, mulher, fala em inglês com sotaque americano de uma mulher negra americana, voz feminina clara e firme de uma mulher de uns trinta anos, entonação alegre, sorrindo enquanto polvilha, voz autêntica, como se exigisse ser ouvida, a seguinte frase: "sprinkle on some sesame seeds, and bake them"

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Brandon polvilha sementes de gergelim com as pontas dos dedos sobre as bolinhas da assadeira, sorrindo para a câmera.

câmera: leve handheld

som ambiente: box de treino em casa, tranquilo, sementes caindo na bandeja, sem música
```

### V04 · T4 · frame inicial = a imagem que você deixou no K04

```text
V04
a voz da avatar Brandon, fora de quadro (voz-over, ela não aparece falando), em inglês com sotaque americano de uma mulher negra americana, voz feminina clara e firme de uma mulher de uns trinta anos, entonação didática, voz-over curta, diz a seguinte frase: "till golden,"

a voz diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Nenhuma boca visível no quadro.

o que acontece no vídeo: Brandon, de perfil, enfia a assadeira com as bolinhas no forno elétrico de bancada e para com a mão na porta.

câmera: leve handheld

som ambiente: box de treino em casa, tranquilo, bandeja deslizando no forno, sem música
```

### V05 · T5 · frame inicial = a imagem que você deixou no K05

```text
V05
a avatar Brandon, mulher, fala em inglês com sotaque americano de uma mulher negra americana, voz feminina clara e firme de uma mulher de uns trinta anos, entonação orgulhosa e animada, marcando softest e fluffiest, voz autêntica, como se exigisse ser ouvida, a seguinte frase: "you get the softest, fluffiest avocado potato buns. And because there's no flour in them,"

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Brandon inclina a assadeira dos pãezinhos dourados em direção à câmera e volta a olhar a lente.

câmera: leve handheld

som ambiente: box de treino em casa, tranquilo, sem música
```

### V06 · T6 · frame inicial = a imagem que você deixou no K06

```text
V06
a avatar Brandon, mulher, fala em inglês com sotaque americano de uma mulher negra americana, voz feminina clara e firme de uma mulher de uns trinta anos, entonação animada, mostrando o pãozinho, voz autêntica, como se exigisse ser ouvida, a seguinte frase: "they feel so much lighter. Also, the avocado gives you fiber. That helps support the good bacteria"

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Brandon ergue o pãozinho dourado com as duas mãos, quase na câmera, e o vira de leve para mostrar a crosta.

câmera: leve handheld

som ambiente: box de treino em casa, tranquilo, sem música
```

### V07 · T7 · frame inicial = a imagem que você deixou no K07

```text
V07
a avatar Brandon, mulher, fala em inglês com sotaque americano de uma mulher negra americana, voz feminina clara e firme de uma mulher de uns trinta anos, entonação calma e confiante, voz autêntica, como se exigisse ser ouvida, a seguinte frase: "in your gut. And the Greek yogurt adds beneficial cultures, too."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Brandon abre o pão ao meio e aproxima as duas metades da câmera, mostrando o miolo macio e aerado.

câmera: leve handheld

som ambiente: box de treino em casa, tranquilo, sem música
```

### V08 · T8 · frame inicial = a imagem que você deixou no K08

```text
V08
a avatar Brandon, mulher, fala em inglês com sotaque americano de uma mulher negra americana, voz feminina clara e firme de uma mulher de uns trinta anos, entonação próxima e sincera, como quem divide o que faz todo dia, voz autêntica, como se exigisse ser ouvida, a seguinte frase: "I share real recipes to support your gut, your energy, your immunity, and just feel better day to day."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Brandon fala para a câmera de selfie, segurando o pãozinho na mão direita baixa; a mão que segura o celular nunca se mexe, só a outra gesticula.

câmera: leve handheld

som ambiente: box de treino em casa, tranquilo, sem música
```

### V09 · T9 · frame inicial = a imagem que você deixou no K09

```text
V09
a avatar Brandon, mulher, fala em inglês com sotaque americano de uma mulher negra americana, voz feminina clara e firme de uma mulher de uns trinta anos, entonação calorosa e firme, como quem revela algo que ninguém conta, voz autêntica, como se exigisse ser ouvida, a seguinte frase: "Here is what nobody tells you about eating clean. When stress stays high, your body stays on guard. It is not working against you, it is protecting you."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Brandon fala para a câmera de selfie, o pãozinho na mão baixa; só o rosto e os ombros se mexem, com um aceno de cabeça no it is protecting you; a mão que segura o celular nunca se mexe.

câmera: leve handheld

som ambiente: box de treino em casa, tranquilo, sem música
```

### V10 · T10 · frame inicial = a imagem que você deixou no K10

```text
V10
a avatar Brandon, mulher, fala em inglês com sotaque americano de uma mulher negra americana, voz feminina clara e firme de uma mulher de uns trinta anos, entonação pausada e curiosa, deixando a pergunta no ar, voz autêntica, como se exigisse ser ouvida, a seguinte frase: "So if your food is already clean and you still feel off, what exactly is your body trying to guard you from?"

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Brandon fala para a câmera de selfie, sem nada nas mãos, e inclina a cabeça de leve no final da pergunta; a mão que segura o celular nunca se mexe.

câmera: leve handheld

som ambiente: box de treino em casa, tranquilo, sem música
```

### V11 · T11 · frame inicial = a imagem que você deixou no K11

```text
V11
a avatar Brandon, mulher, fala em inglês com sotaque americano de uma mulher negra americana, voz feminina clara e firme de uma mulher de uns trinta anos, entonação clara e sincera, dizendo Natural Rems Sea Moss devagar e por inteiro, voz autêntica, como se exigisse ser ouvida, a seguinte frase: "That is why I take Natural Rems Sea Moss with dinner. Ashwagandha is in it, and so are fifteen more ingredients, all in one chewy apple gummy."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Brandon segura o pote de Natural Rems Sea Moss com as duas mãos na altura do peito, rótulo de frente para a câmera, e aproxima o pote um pouco da câmera quando diz o nome.

câmera: fixa

som ambiente: box de treino em casa, tranquilo, sem música
```

### V12 · T12 · frame inicial = a imagem que você deixou no K12

```text
V12
a avatar Brandon, mulher, fala em inglês com sotaque americano de uma mulher negra americana, voz feminina clara e firme de uma mulher de uns trinta anos, entonação calorosa e convidativa, voz autêntica, como se exigisse ser ouvida, a seguinte frase: "Comment yes if you want more like this, and follow me so you don't miss the next one."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Brandon segura o pote parado com as duas mãos, rótulo de frente e legível; só o rosto e a boca se mexem.

câmera: fixa

som ambiente: box de treino em casa, tranquilo, sem música
```

### V13 · T13 · frame inicial = a imagem que você deixou no K13

```text
V13
a avatar Brandon, mulher, fala em inglês com sotaque americano de uma mulher negra americana, voz feminina clara e firme de uma mulher de uns trinta anos, entonação clara e pausada, dizendo Natural Rems Sea Moss devagar e por inteiro, voz autêntica, como se exigisse ser ouvida, a seguinte frase: "Search Natural Rems Sea Moss on Amazon. Or you can just tap the link I left right down below, in the caption of this video."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Brandon segura o pote parado com as duas mãos, rótulo de frente e legível, sem nada cobrindo, do começo ao fim; só o rosto e a boca se mexem.

câmera: fixa

som ambiente: box de treino em casa, tranquilo, sem música
```

## 4. Montagem no CapCut

1. Clipes numerados na ordem: V01 a V13.
2. Cortar cada clipe no tempo da cena do modelo: V01 0,0 a 7,4 s; V02 7,4 a 9,9 s; V03 9,9 a 12,5 s; V04 12,5 a 13,8 s; V05 13,8 a 19,6 s; V06 19,6 a 24,0 s; V07 24,0 a 27,4 s; V08 a fala inteira; V09 a fala inteira; V10 a fala inteira; V11 a fala inteira; V12 a fala inteira; V13 o CTA inteiro, sem corte.
3. Zero tempo morto: todo clipe começa já falando. Isolate Voice / Keep Vocal no áudio.
4. V02 e V04 são B-roll com voz-over da avatar fora de quadro: a voz já vem gerada no próprio clipe. Se alguma ficar fraca, cortar o áudio dela do clipe vizinho do mesmo tom.
5. Dentro do V01 (a receita inteira em um clipe), jump cuts curtos de ritmo como no modelo, se quiser; o clipe é contínuo.
6. V13 inteiro, sem corte e sem nada cobrindo o pote: é o CTA da marca (frasco parado e legível enquanto o nome é dito). O vídeo acaba nele.
7. Legenda de tela como no modelo: serifada branca, palavra a palavra, no meio do quadro, com a palavra carregada maior; no começo do V01, "mash one boiled potato".
8. Sem Voice Changer: a voz vem do prompt de cada V.
9. Música só depois do gancho (a partir do V02), nunca no pré-gancho, entre -19 e -20 dB, fora da biblioteca do TikTok.
10. Rótulo pequeno `Synthetic performer` num canto do vídeo.
11. Legenda do post: `#ad #syntheticperformer #naturalrems` na primeira linha e o link da Amazon logo abaixo; chave de conteúdo de IA ligada na plataforma.

## 5. Transcrição final por take

| Take | English | Português |
|---|---|---|
| T1 | Did you know that if you mash one boiled potato with avocado, add eggs, Greek yogurt, baking powder, salt, and mix everything | Você sabia que se amassar uma batata cozida com abacate, juntar ovos, iogurte grego, fermento, sal e misturar tudo |
| T2 | together until smooth, then shape it into buns, | até ficar liso, depois modelar em pãezinhos, |
| T3 | sprinkle on some sesame seeds, and bake them | polvilhar gergelim e assar |
| T4 | till golden, | até dourar, |
| T5 | you get the softest, fluffiest avocado potato buns. And because there's no flour in them, | você ganha os pãezinhos de batata com abacate mais macios e fofinhos. E como não levam farinha, |
| T6 | they feel so much lighter. Also, the avocado gives you fiber. That helps support the good bacteria | eles ficam muito mais leves. Além disso, o abacate dá fibra. Isso ajuda a apoiar as bactérias boas |
| T7 | in your gut. And the Greek yogurt adds beneficial cultures, too. | do seu intestino. E o iogurte grego traz culturas benéficas também. |
| T8 | I share real recipes to support your gut, your energy, your immunity, and just feel better day to day. | Eu compartilho receitas de verdade para apoiar seu intestino, sua energia, sua imunidade, e se sentir melhor no dia a dia. |
| T9 | Here is what nobody tells you about eating clean. When stress stays high, your body stays on guard. It is not working against you, it is protecting you. | Eis o que ninguém conta sobre comer limpo. Quando o estresse fica alto, o corpo fica em guarda. Ele não está trabalhando contra você, está te protegendo. |
| T10 | So if your food is already clean and you still feel off, what exactly is your body trying to guard you from? | Então, se a sua comida já é limpa e você ainda se sente meio fora do eixo, do que exatamente o seu corpo está tentando te proteger? |
| T11 | That is why I take Natural Rems Sea Moss with dinner. Ashwagandha is in it, and so are fifteen more ingredients, all in one chewy apple gummy. | É por isso que eu tomo Natural Rems Sea Moss no jantar. Tem ashwagandha, e mais quinze ingredientes, tudo numa goma macia de maçã. |
| T12 | Comment yes if you want more like this, and follow me so you don't miss the next one. | Comente yes se quiser mais assim, e me siga para não perder a próxima. |
| T13 | Search Natural Rems Sea Moss on Amazon. Or you can just tap the link I left right down below, in the caption of this video. | Procure Natural Rems Sea Moss na Amazon. Ou é só tocar no link que eu deixei aqui embaixo, na legenda deste vídeo. |

## 6. Roteiro final em inglês

1. Did you know that if you mash one boiled potato with avocado, add eggs, Greek yogurt, baking powder, salt, and mix everything
2. together until smooth, then shape it into buns,
3. sprinkle on some sesame seeds, and bake them
4. till golden,
5. you get the softest, fluffiest avocado potato buns. And because there's no flour in them,
6. they feel so much lighter. Also, the avocado gives you fiber. That helps support the good bacteria
7. in your gut. And the Greek yogurt adds beneficial cultures, too.
8. I share real recipes to support your gut, your energy, your immunity, and just feel better day to day.
9. Here is what nobody tells you about eating clean. When stress stays high, your body stays on guard. It is not working against you, it is protecting you.
10. So if your food is already clean and you still feel off, what exactly is your body trying to guard you from?
11. That is why I take Natural Rems Sea Moss with dinner. Ashwagandha is in it, and so are fifteen more ingredients, all in one chewy apple gummy.
12. Comment yes if you want more like this, and follow me so you don't miss the next one.
13. Search Natural Rems Sea Moss on Amazon. Or you can just tap the link I left right down below, in the caption of this video.

Did you know that if you mash one boiled potato with avocado, add eggs, Greek yogurt, baking powder, salt, and mix everything together until smooth, then shape it into buns, sprinkle on some sesame seeds, and bake them till golden, you get the softest, fluffiest avocado potato buns. And because there's no flour in them, they feel so much lighter. Also, the avocado gives you fiber. That helps support the good bacteria in your gut. And the Greek yogurt adds beneficial cultures, too. I share real recipes to support your gut, your energy, your immunity, and just feel better day to day. Here is what nobody tells you about eating clean. When stress stays high, your body stays on guard. It is not working against you, it is protecting you. So if your food is already clean and you still feel off, what exactly is your body trying to guard you from? That is why I take Natural Rems Sea Moss with dinner. Ashwagandha is in it, and so are fifteen more ingredients, all in one chewy apple gummy. Comment yes if you want more like this, and follow me so you don't miss the next one. Search Natural Rems Sea Moss on Amazon. Or you can just tap the link I left right down below, in the caption of this video.
