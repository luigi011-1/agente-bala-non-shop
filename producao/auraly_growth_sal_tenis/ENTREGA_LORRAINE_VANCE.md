# ENTREGA | Lorraine Vance | Auraly Growth Sal no tênis

Produção `auraly_growth_sal_tenis` · Ângulo 3 · GROWTH · vídeo modelo de avatar IA · rodada de VALIDAÇÃO · perfil AURALY

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

Roster Auraly: Walt Hensley, Darlene Pruitt e Lorraine Vance. A referencia de cada um e a anchor
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

Checklist de envio: 32/32 aprovados (N/A: A1, A2, A7, A9 fiéis ao modelo, gancho sem rosto e com a fala do modelo; A10 growth sem produto; C3 a C7 sem segunda pessoa, selfie, frase curta repetida, cena atuada ou motion control)

Ficha: 2/2 K conferidos contra o frame do modelo, placar 14/14 cada (`FICHA_FRAMES.md`, GATE_VISUAL Parte 6)

## Anexos e mapa

- **Âncora Lorraine Vance:** `producao/_ancoras/lorraine_vance_ancora.jpg` em TODOS os K.
- **Em cada K**, anexar também o frame do modelo daquele K (`input/frames_modelo/Kxx_modelo.png`), só como composição.

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
```

## 2. PROMPTS DE IMAGEM (um bloco por K)

### K01 · T1, gancho, sal caindo dentro do tênis de trabalho · anexar ÂNCORA + FRAME DO MODELO

```text
K01
{
  "format": "IMPORTANT: THIS IS IPHONE FOOTAGE. Vertical 9:16.",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "reference_use": "Use the first attached image only for Lorraine Vance's exact identity, wardrobe, jewelry, SOULMATE card and own setting. Use the second attached image only as a composition reference for the camera position, framing and action; do not copy its person, clothes, room, rug, labels or on-screen text.",
  "identity_main": "The exact fictional AI character Lorraine Vance: white American woman around fifty-two, closely shaved head with grey stubble, freckles and sunspots on her face and scalp, light grey-green eyes, defined jaw, fine lines and no makeup.",
  "wardrobe": "Light-wash denim shirt worn open over a fitted black crew-neck T-shirt, dark jeans, large silver hoop earrings, a thin silver chain necklace and black-framed reading glasses hanging from the T-shirt collar.",
  "scene": "The floor of Lorraine Vance's own home: the light oak wooden floor of her bright white kitchen, seen from above. At the top edge of the frame, a small American flag on a short wooden stick stands in a small glass jar on the floor, discreet but visible and in focus.",
  "prop": "A red running sneaker made of red suede and red mesh, with a light grey heel counter, a white midsole with a thin tan stripe, pale pink-white laces and a dark navy insole, completely plain, sits on the floor, seen from above straight into its heel opening; coarse white kosher salt crystals are falling into the heel opening and a small white pile is forming on the dark navy insole. The other red running sneaker of the pair lies on its side at the right edge, cut by the frame. A second identical tall dark navy-blue cylindrical salt shaker with a round pour lid, completely plain, full of coarse white kosher salt crystals, stands upright at the upper left.",
  "posture": "No face in frame: only the hand and wrist enter from the upper right, her freckled fair hand with bare fingers and the denim cuff at the wrist, tilting a tall dark navy-blue cylindrical salt shaker with a round pour lid, completely plain, full of coarse white kosher salt crystals, so the salt pours into the shoe.",
  "composition": "High-angle shot looking down into the heel opening: the red running sneaker is the hero and fills about 55 percent of the frame, center and lower half, its heel touching the bottom edge, about 10 inches from the lens, the largest thing in frame; the tilted shaker in the hand fills the upper right third; the standing shaker sits at the upper left. Nothing else is on the floor. The background is reduced by framing, never by blur.",
  "camera": "phone held about 16 inches above the floor, 1x lens, pointing down at about sixty degrees",
  "lighting": "Neutral overcast daylight from a window, the outside clearly visible through the window, never white or blown out, soft even light on the face and hands with no harsh shadows.",
  "state": "Start frame: the coarse salt is already falling from the tilted shaker into the shoe, a small white pile on the insole.",
  "realism": "Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday reality, background fully in focus, everything in sharp focus, no AI polish, no beauty smoothing.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no printed labels or lettering on the shaker or the shoe, no studio, no plastic-looking human skin, no extra fingers, no third hand, no supernatural lighting, no blur, no bokeh, no artificial lighting, no warm orange color cast, no yellow tint on the skin, no golden glow, no golden hour light, no sunset, no de-aging, no beauty smoothing, no visible phone, no HDR, no cinematic lighting, no second person in frame, no face in frame, no feet, no shoe being worn, no spilled salt around the shoe"
}
```

### K02 · T2 a T17, corpo, ajoelhado com o tênis, o saleiro e a carta · anexar ÂNCORA + FRAME DO MODELO

```text
K02
{
  "format": "IMPORTANT: THIS IS IPHONE FOOTAGE. Vertical 9:16.",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "reference_use": "Use the first attached image only for Lorraine Vance's exact identity, wardrobe, jewelry, SOULMATE card and own setting. Use the second attached image only as a composition reference for the camera position, framing and action; do not copy its person, clothes, room, rug, labels or on-screen text.",
  "identity_main": "The exact fictional AI character Lorraine Vance: white American woman around fifty-two, closely shaved head with grey stubble, freckles and sunspots on her face and scalp, light grey-green eyes, defined jaw, fine lines and no makeup.",
  "wardrobe": "Light-wash denim shirt worn open over a fitted black crew-neck T-shirt, dark jeans, large silver hoop earrings, a thin silver chain necklace and black-framed reading glasses hanging from the T-shirt collar.",
  "scene": "Her own bright white American kitchen, the same lived-in kitchen as the reference, unchanged, seen from knee height: white walls and white quartz counters; behind her the light wood floating shelves with clear quartz crystal points, a lit incense stick with a thin line of smoke, a white pillar candle and a small American flag, discreet but visible and in focus; on the wall a framed zodiac wheel chart and a small wooden crucifix; a window at the left with the street clearly visible. The light oak wooden floor.",
  "prop": "In the hand on the right side of the frame Lorraine Vance holds a red running sneaker made of red suede and red mesh, with a light grey heel counter, a white midsole with a thin tan stripe, pale pink-white laces and a dark navy insole, completely plain, upright by the heel collar just above the floor, with a small white pile of coarse salt visible inside. A tall dark navy-blue cylindrical salt shaker with a round pour lid, completely plain, full of coarse white kosher salt crystals, stands upright on the floor in the lower left corner. In the other hand, at chest height and facing the lens, she holds the holographic SOULMATE card from the reference: a tarot-sized card with a rainbow mirror-foil border and saturated art of a brown-haired woman and a man embracing under a rainbow glow, a bright heart and red roses at the bottom, with the word SOULMATE on a pale banner at the bottom.",
  "posture": "Lorraine Vance kneels on one knee on the floor, facing the lens, the other knee raised, the whole body visible from head to knee; the hand holding the card is the one that gestures.",
  "composition": "The tall dark navy-blue cylindrical salt shaker is very close to the lens in the lower left corner, about 10 inches from the lens, and takes up about 20 percent of the frame; the red running sneaker sits just behind it in the lower right and fills about 25 percent of the frame; both are closer to the camera than her face, nothing else competing with them. Lorraine Vance kneels right behind them, face in the upper quarter of the frame. Nothing else is on the floor. The background is reduced by framing, never by blur.",
  "camera": "phone on a small tripod on the floor at knee height, 1x lens, about three feet from the face, pointing slightly upward, fixed",
  "lighting": "Neutral overcast daylight from a window, the outside clearly visible through the window, never white or blown out, soft even light on the face and hands with no harsh shadows.",
  "state": "Start frame: Lorraine Vance looks into the lens, caught mid-sentence, lips naturally parted, animated expression.",
  "realism": "Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday reality, background fully in focus, everything in sharp focus, no AI polish, no beauty smoothing.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no printed labels or lettering on the shaker or the shoe, no studio, no plastic-looking human skin, no extra fingers, no third hand, no supernatural lighting, no blur, no bokeh, no artificial lighting, no warm orange color cast, no yellow tint on the skin, no golden glow, no golden hour light, no sunset, no de-aging, no beauty smoothing, no visible phone, no HDR, no cinematic lighting, no second person in frame, no standing pose, no sitting on a chair, no salt spilled on the floor, no second card"
}
```

## 3. PROMPTS DE VÍDEO (um bloco por V)

### V01 · T1 · frame inicial = a imagem escolhida do K01

```text
V01
narração em off: a avatar Lorraine Vance, mulher, fala em inglês com sotaque americano de Chicago, voz feminina grave, direta e de humor seco de uma mulher de cinquenta e dois anos de Chicago, tom baixo e confidencial, como quem conta um segredo, voz autêntica, como se exigisse ser ouvida, a seguinte frase: "Put salt inside your work shoes before you leave the house." Ninguém aparece falando em quadro, só as mãos.

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Sem lip sync: a fala é narração em off e nenhum rosto aparece no quadro.

o que acontece no vídeo: plano 1, já em andamento: a mão de Lorraine Vance inclina o saleiro azul-escuro e o sal grosso cai dentro do tênis vermelho no chão. Corte, perto de um segundo, para um macro da palma aberta cheia de sal grosso logo acima da abertura do tênis: os dedos inclinam e o sal escorre em fio para dentro, formando um montinho branco na palmilha escura. Corte, perto dos três segundos, para o tênis inteiro visto de cima com o monte de sal dentro, parado até o fim.

câmera: cortes internos ao clipe: plano alto olhando para baixo, macro da mão e plano de cima do tênis, cada plano com a câmera parada

som ambiente: cozinha residencial silenciosa, som do sal grosso caindo no tênis, sem música
```

### V02 · T2 · frame inicial = a imagem escolhida do K02

```text
V02
a avatar Lorraine Vance, mulher, fala em inglês com sotaque americano de Chicago, voz feminina grave, direta e de humor seco de uma mulher de cinquenta e dois anos de Chicago, com um meio sorriso, convicta, voz autêntica, como se exigisse ser ouvida, a seguinte frase: "I know it sounds ridiculous, but you'll thank me for the rest of your life."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Lorraine Vance continua ajoelhada segurando o tênis vermelho e a carta, e fala para a câmera com um leve balançar da cabeça.

câmera: fixa, no tripé baixo, sem movimento

som ambiente: cozinha residencial silenciosa, sem música
```

### V03 · T3 · frame inicial = a imagem escolhida do K02

```text
V03
a avatar Lorraine Vance, mulher, fala em inglês com sotaque americano de Chicago, voz feminina grave, direta e de humor seco de uma mulher de cinquenta e dois anos de Chicago, quase sussurrando, séria, voz autêntica, como se exigisse ser ouvida, a seguinte frase: "Keep your mouth shut after you watch this. Do not tell anyone. Not everyone is going to see this before this month ends."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Lorraine Vance se inclina um pouco para a lente e fala baixo, com pequenos gestos da mão que segura a carta.

câmera: fixa, no tripé baixo, sem movimento

som ambiente: cozinha residencial silenciosa, sem música
```

### V04 · T4 · frame inicial = a imagem escolhida do K02

```text
V04
a avatar Lorraine Vance, mulher, fala em inglês com sotaque americano de Chicago, voz feminina grave, direta e de humor seco de uma mulher de cinquenta e dois anos de Chicago, urgente, em tom de alerta, voz autêntica, como se exigisse ser ouvida, a seguinte frase: "I do not know your name, but do not scroll. Because if this reached you today, it reached you as a final warning."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Lorraine Vance aponta para a lente com a mão que segura a carta enquanto fala.

câmera: fixa, no tripé baixo, sem movimento

som ambiente: cozinha residencial silenciosa, sem música
```

### V05 · T5 · frame inicial = a imagem escolhida do K02

```text
V05
a avatar Lorraine Vance, mulher, fala em inglês com sotaque americano de Chicago, voz feminina grave, direta e de humor seco de uma mulher de cinquenta e dois anos de Chicago, animada e contida, confidencial, voz autêntica, como se exigisse ser ouvida, a seguinte frase: "A powerful wave of prosperity, love and money is heading your way. Don't tell anyone, but the abundance portal has opened."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Lorraine Vance segura o tênis vermelho com uma mão e a carta com a outra, e fala para a câmera com pequenos gestos da mão da carta.

câmera: fixa, no tripé baixo, sem movimento

som ambiente: cozinha residencial silenciosa, sem música
```

### V06 · T6 · frame inicial = a imagem escolhida do K02

```text
V06
a avatar Lorraine Vance, mulher, fala em inglês com sotaque americano de Chicago, voz feminina grave, direta e de humor seco de uma mulher de cinquenta e dois anos de Chicago, aliviada e emocionada, voz autêntica, como se exigisse ser ouvida, a seguinte frase: "The worst is finally over. I see a lot of money, prosperity and someone incredibly wonderful walking into your life."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Lorraine Vance segura o tênis vermelho com uma mão e a carta com a outra, e fala para a câmera com pequenos gestos da mão da carta.

câmera: fixa, no tripé baixo, sem movimento

som ambiente: cozinha residencial silenciosa, sem música
```

### V07 · T7 · frame inicial = a imagem escolhida do K02

```text
V07
a avatar Lorraine Vance, mulher, fala em inglês com sotaque americano de Chicago, voz feminina grave, direta e de humor seco de uma mulher de cinquenta e dois anos de Chicago, firme e solene, voz autêntica, como se exigisse ser ouvida, a seguinte frase: "Before you scroll, close your right hand and listen until the end. This video isn't for everyone. The universe chose you."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Lorraine Vance segura o tênis vermelho com uma mão e a carta com a outra, e fala para a câmera com pequenos gestos da mão da carta.

câmera: fixa, no tripé baixo, sem movimento

som ambiente: cozinha residencial silenciosa, sem música
```

### V08 · T8 · frame inicial = a imagem escolhida do K02

```text
V08
a avatar Lorraine Vance, mulher, fala em inglês com sotaque americano de Chicago, voz feminina grave, direta e de humor seco de uma mulher de cinquenta e dois anos de Chicago, urgente, depois intrigada, voz autêntica, como se exigisse ser ouvida, a seguinte frase: "If you skip right now, the energy breaks. I feel something very unusual happening to you right now."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Lorraine Vance franze a testa de leve e aponta para a lente com a mão da carta.

câmera: fixa, no tripé baixo, sem movimento

som ambiente: cozinha residencial silenciosa, sem música
```

### V09 · T9 · frame inicial = a imagem escolhida do K02

```text
V09
a avatar Lorraine Vance, mulher, fala em inglês com sotaque americano de Chicago, voz feminina grave, direta e de humor seco de uma mulher de cinquenta e dois anos de Chicago, intensa e emocionada, voz autêntica, como se exigisse ser ouvida, a seguinte frase: "I see the chains that were keeping you trapped in scarcity being broken."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Lorraine Vance segura o tênis vermelho com uma mão e a carta com a outra, e fala para a câmera com pequenos gestos da mão da carta.

câmera: fixa, no tripé baixo, sem movimento

som ambiente: cozinha residencial silenciosa, sem música
```

### V10 · T10 · frame inicial = a imagem escolhida do K02

```text
V10
a avatar Lorraine Vance, mulher, fala em inglês com sotaque americano de Chicago, voz feminina grave, direta e de humor seco de uma mulher de cinquenta e dois anos de Chicago, calorosa e emocionada, voz autêntica, como se exigisse ser ouvida, a seguinte frase: "The love that was being held back from you is finally coming straight to you."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Lorraine Vance segura o tênis vermelho com uma mão e a carta com a outra, e fala para a câmera com pequenos gestos da mão da carta.

câmera: fixa, no tripé baixo, sem movimento

som ambiente: cozinha residencial silenciosa, sem música
```

### V11 · T11 · frame inicial = a imagem escolhida do K02

```text
V11
a avatar Lorraine Vance, mulher, fala em inglês com sotaque americano de Chicago, voz feminina grave, direta e de humor seco de uma mulher de cinquenta e dois anos de Chicago, firme e intensa, voz autêntica, como se exigisse ser ouvida, a seguinte frase: "In the next seven minutes, the energy of scarcity that was following you is going to be destroyed forever."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Lorraine Vance segura o tênis vermelho com uma mão e a carta com a outra, e fala para a câmera com pequenos gestos da mão da carta.

câmera: fixa, no tripé baixo, sem movimento

som ambiente: cozinha residencial silenciosa, sem música
```

### V12 · T12 · frame inicial = a imagem escolhida do K02

```text
V12
a avatar Lorraine Vance, mulher, fala em inglês com sotaque americano de Chicago, voz feminina grave, direta e de humor seco de uma mulher de cinquenta e dois anos de Chicago, urgente e rápida, voz autêntica, como se exigisse ser ouvida, a seguinte frase: "So send this video to yourself right now, because in seven minutes you're going to come back to confirm the energetic shift for yourself."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Lorraine Vance fala mais rápido, marcando o ritmo com a mão que segura a carta.

câmera: fixa, no tripé baixo, sem movimento

som ambiente: cozinha residencial silenciosa, sem música
```

### V13 · T13 · frame inicial = a imagem escolhida do K02

```text
V13
a avatar Lorraine Vance, mulher, fala em inglês com sotaque americano de Chicago, voz feminina grave, direta e de humor seco de uma mulher de cinquenta e dois anos de Chicago, firme, em ritmo de instrução, voz autêntica, como se exigisse ser ouvida, a seguinte frase: "Now open your hand and save this video. That will be your first seal."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Lorraine Vance mostra a carta para a lente e fala com firmeza.

câmera: fixa, no tripé baixo, sem movimento

som ambiente: cozinha residencial silenciosa, sem música
```

### V14 · T14 · frame inicial = a imagem escolhida do K02

```text
V14
a avatar Lorraine Vance, mulher, fala em inglês com sotaque americano de Chicago, voz feminina grave, direta e de humor seco de uma mulher de cinquenta e dois anos de Chicago, rápida e firme, voz autêntica, como se exigisse ser ouvida, a seguinte frase: "Double tap quickly on your screen. That will be your second seal. Type 222 in the comments so I can see you did everything."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Lorraine Vance marca cada instrução com a mão da carta, falando rápido.

câmera: fixa, no tripé baixo, sem movimento

som ambiente: cozinha residencial silenciosa, sem música
```

### V15 · T15 · frame inicial = a imagem escolhida do K02

```text
V15
a avatar Lorraine Vance, mulher, fala em inglês com sotaque americano de Chicago, voz feminina grave, direta e de humor seco de uma mulher de cinquenta e dois anos de Chicago, animada, depois séria, voz autêntica, como se exigisse ser ouvida, a seguinte frase: "If you did everything right, tomorrow at 9am you're going to receive some incredibly good news. But pay close attention."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Lorraine Vance segura o tênis vermelho com uma mão e a carta com a outra, e fala para a câmera com pequenos gestos da mão da carta.

câmera: fixa, no tripé baixo, sem movimento

som ambiente: cozinha residencial silenciosa, sem música
```

### V16 · T16 · frame inicial = a imagem escolhida do K02

```text
V16
a avatar Lorraine Vance, mulher, fala em inglês com sotaque americano de Chicago, voz feminina grave, direta e de humor seco de uma mulher de cinquenta e dois anos de Chicago, séria e baixa, em alerta, voz autêntica, como se exigisse ser ouvida, a seguinte frase: "This energy is highly sensitive, and telling other people too soon can completely break it."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Lorraine Vance segura o tênis vermelho com uma mão e a carta com a outra, e fala para a câmera com pequenos gestos da mão da carta.

câmera: fixa, no tripé baixo, sem movimento

som ambiente: cozinha residencial silenciosa, sem música
```

### V17 · T17 · frame inicial = a imagem escolhida do K02

```text
V17
a avatar Lorraine Vance, mulher, fala em inglês com sotaque americano de Chicago, voz feminina grave, direta e de humor seco de uma mulher de cinquenta e dois anos de Chicago, firme e próxima, olhando direto na lente, voz autêntica, como se exigisse ser ouvida, a seguinte frase: "So follow me right now, so this stays open, because the second part of this sign is coming to you next."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Lorraine Vance se inclina um pouco para a lente, séria, segurando o tênis e a carta.

câmera: fixa, no tripé baixo, sem movimento

som ambiente: cozinha residencial silenciosa, sem música
```

## 4. Montagem no CapCut

1. Clipes numerados na ordem: V01 a V17.
2. V01 (gancho): usar só os primeiros ~4,1 s, com os três planos e a narração inteira; deixar o fim da frase ("the house") vazar meio segundo sobre o começo do V02, como no modelo.
3. Entre V01 e V02, flash branco de 0,1 s (transição de CapCut, igual ao modelo).
4. V02 a V17: zero tempo morto, todo clipe começa já falando; cortar logo depois da última palavra. Isolate Voice / Keep Vocal no áudio. Como todos saem do mesmo frame, os cortes ficam quase invisíveis, igual ao plano único do modelo.
5. Legenda karaokê em caixa alta, branca, palavra atual em amarelo, no meio do quadro, do V01 ao V17.
6. Do V02 em diante: "222" fixo no canto superior esquerdo e "444 💰" pequeno perto do tênis.
7. Sem Voice Changer: a voz vem do prompt de cada V.
8. Música só depois do gancho (a partir do V02), nunca no pré-gancho, entre -19 e -20 dB, fora da biblioteca do TikTok.
9. Rótulo pequeno `AI-generated` num canto do vídeo.

## 5. Transcrição final por take

| Take | English | Português |
|---|---|---|
| T1 | Put salt inside your work shoes before you leave the house. | Coloque sal dentro dos seus sapatos de trabalho antes de sair de casa. |
| T2 | I know it sounds ridiculous, but you'll thank me for the rest of your life. | Eu sei que parece ridículo, mas você vai me agradecer pelo resto da vida. |
| T3 | Keep your mouth shut after you watch this. Do not tell anyone. Not everyone is going to see this before this month ends. | Fique de boca fechada depois de assistir isto. Não conte pra ninguém. Nem todo mundo vai ver isto antes de este mês acabar. |
| T4 | I do not know your name, but do not scroll. Because if this reached you today, it reached you as a final warning. | Eu não sei o seu nome, mas não passe. Porque se isto chegou até você hoje, chegou como um último aviso. |
| T5 | A powerful wave of prosperity, love and money is heading your way. Don't tell anyone, but the abundance portal has opened. | Uma onda poderosa de prosperidade, amor e dinheiro está vindo na sua direção. Não conte pra ninguém, mas o portal da abundância se abriu. |
| T6 | The worst is finally over. I see a lot of money, prosperity and someone incredibly wonderful walking into your life. | O pior finalmente passou. Eu vejo muito dinheiro, prosperidade e alguém incrivelmente maravilhoso entrando na sua vida. |
| T7 | Before you scroll, close your right hand and listen until the end. This video isn't for everyone. The universe chose you. | Antes de passar, feche a mão direita e escute até o fim. Este vídeo não é pra todo mundo. O universo escolheu você. |
| T8 | If you skip right now, the energy breaks. I feel something very unusual happening to you right now. | Se você pular agora, a energia se quebra. Eu sinto algo muito incomum acontecendo com você agora. |
| T9 | I see the chains that were keeping you trapped in scarcity being broken. | Eu vejo as correntes que te prendiam na escassez sendo quebradas. |
| T10 | The love that was being held back from you is finally coming straight to you. | O amor que estava sendo segurado longe de você finalmente está vindo direto pra você. |
| T11 | In the next seven minutes, the energy of scarcity that was following you is going to be destroyed forever. | Nos próximos sete minutos, a energia de escassez que te seguia vai ser destruída para sempre. |
| T12 | So send this video to yourself right now, because in seven minutes you're going to come back to confirm the energetic shift for yourself. | Então mande este vídeo pra você mesma agora, porque em sete minutos você vai voltar pra confirmar a virada de energia com os próprios olhos. |
| T13 | Now open your hand and save this video. That will be your first seal. | Agora abra a mão e salve este vídeo. Esse vai ser o seu primeiro selo. |
| T14 | Double tap quickly on your screen. That will be your second seal. Type 222 in the comments so I can see you did everything. | Toque duas vezes rápido na tela. Esse vai ser o seu segundo selo. Escreva 222 nos comentários pra eu ver que você fez tudo. |
| T15 | If you did everything right, tomorrow at 9am you're going to receive some incredibly good news. But pay close attention. | Se você fez tudo certo, amanhã às 9 da manhã você vai receber uma notícia incrivelmente boa. Mas preste muita atenção. |
| T16 | This energy is highly sensitive, and telling other people too soon can completely break it. | Essa energia é muito sensível, e contar pra outras pessoas cedo demais pode quebrá-la por completo. |
| T17 | So follow me right now, so this stays open, because the second part of this sign is coming to you next. | Então me siga agora, pra isso continuar aberto, porque a segunda parte deste sinal chega pra você em seguida. |

## 6. Roteiro final em inglês

1. Put salt inside your work shoes before you leave the house.
2. I know it sounds ridiculous, but you'll thank me for the rest of your life.
3. Keep your mouth shut after you watch this. Do not tell anyone. Not everyone is going to see this before this month ends.
4. I do not know your name, but do not scroll. Because if this reached you today, it reached you as a final warning.
5. A powerful wave of prosperity, love and money is heading your way. Don't tell anyone, but the abundance portal has opened.
6. The worst is finally over. I see a lot of money, prosperity and someone incredibly wonderful walking into your life.
7. Before you scroll, close your right hand and listen until the end. This video isn't for everyone. The universe chose you.
8. If you skip right now, the energy breaks. I feel something very unusual happening to you right now.
9. I see the chains that were keeping you trapped in scarcity being broken.
10. The love that was being held back from you is finally coming straight to you.
11. In the next seven minutes, the energy of scarcity that was following you is going to be destroyed forever.
12. So send this video to yourself right now, because in seven minutes you're going to come back to confirm the energetic shift for yourself.
13. Now open your hand and save this video. That will be your first seal.
14. Double tap quickly on your screen. That will be your second seal. Type 222 in the comments so I can see you did everything.
15. If you did everything right, tomorrow at 9am you're going to receive some incredibly good news. But pay close attention.
16. This energy is highly sensitive, and telling other people too soon can completely break it.
17. So follow me right now, so this stays open, because the second part of this sign is coming to you next.

Put salt inside your work shoes before you leave the house. I know it sounds ridiculous, but you'll thank me for the rest of your life. Keep your mouth shut after you watch this. Do not tell anyone. Not everyone is going to see this before this month ends. I do not know your name, but do not scroll. Because if this reached you today, it reached you as a final warning. A powerful wave of prosperity, love and money is heading your way. Don't tell anyone, but the abundance portal has opened. The worst is finally over. I see a lot of money, prosperity and someone incredibly wonderful walking into your life. Before you scroll, close your right hand and listen until the end. This video isn't for everyone. The universe chose you. If you skip right now, the energy breaks. I feel something very unusual happening to you right now. I see the chains that were keeping you trapped in scarcity being broken. The love that was being held back from you is finally coming straight to you. In the next seven minutes, the energy of scarcity that was following you is going to be destroyed forever. So send this video to yourself right now, because in seven minutes you're going to come back to confirm the energetic shift for yourself. Now open your hand and save this video. That will be your first seal. Double tap quickly on your screen. That will be your second seal. Type 222 in the comments so I can see you did everything. If you did everything right, tomorrow at 9am you're going to receive some incredibly good news. But pay close attention. This energy is highly sensitive, and telling other people too soon can completely break it. So follow me right now, so this stays open, because the second part of this sign is coming to you next.
