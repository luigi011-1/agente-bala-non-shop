# ENTREGA | Lorraine Vance | Auraly Growth Dinheiro

Produção `auraly_growth_dinheiro` · Ângulo 3 · GROWTH · vídeo modelo de avatar IA · rodada de VALIDAÇÃO · perfil AURALY

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

Checklist de envio: 32/32 aprovados (N/A: A1, A2, A7, A9 fiéis ao modelo, gancho mudo; A10 growth sem produto; C3 a C7 sem segunda pessoa, selfie, frase curta repetida, cena atuada ou motion control)

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
V18: K02
V19: K02
```

## 2. PROMPTS DE IMAGEM (um bloco por K)

### K01 · T1, gancho mudo, perfume no pé descalço colado na lente · anexar ÂNCORA + FRAME DO MODELO

```text
K01
{
  "format": "IMPORTANT: THIS IS IPHONE FOOTAGE. Vertical 9:16.",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "reference_use": "Use the first attached image only for Lorraine Vance's exact identity, wardrobe, jewelry, SOULMATE card and own setting. Use the second attached image only as a composition reference for the camera position, framing and pose; do not copy its person, robe, bathroom, gold fixtures, labels or on-screen text.",
  "identity_main": "The exact fictional AI character Lorraine Vance: white American woman around fifty-two, closely shaved head with grey stubble, freckles and sunspots on her face and scalp, light grey-green eyes, defined jaw, fine lines and no makeup.",
  "wardrobe": "Light-wash denim shirt worn open over a fitted black crew-neck T-shirt, dark jeans rolled up at the ankles, barefoot, large silver hoop earrings, a thin silver chain necklace and black-framed reading glasses hanging from the T-shirt collar.",
  "scene": "Her own bright white American kitchen, the same lived-in kitchen as the reference, unchanged: white walls and white quartz counters, the light wood floating shelves with clear quartz crystal points, a lit incense stick, a white pillar candle and a small American flag, discreet but visible and in focus, a framed zodiac wheel chart and a small wooden crucifix on the wall, and a window with the street clearly visible.",
  "prop": "The sole of the bare foot of Lorraine Vance rests on the edge of her white quartz kitchen counter, right in front of the lens, toes up. In one hand Lorraine Vance holds a tall faceted gold perfume bottle with an ornate embossed pattern and a gold cap, completely plain with no label, and sprays it toward the sole of the bare foot.",
  "posture": "Lorraine Vance sits right behind the foot on a low stool beside her kitchen counter, one leg stretched out with the bare foot resting on the edge, leaning back slightly, spraying the perfume, looking at the lens with a calm, serious face, mouth closed.",
  "composition": "Extreme low-angle close-up: the sole of the bare foot is very close to the lens, about 6 inches from the lens, filling the right half of the frame, about 45 percent of the frame, touching the right edge, far larger than her head, nothing else competing with it. Lorraine Vance sits behind it, left of center, face in the upper third; the gold perfume bottle in her hand at chest height on the left. Nothing else is on the edge. The background is reduced by framing, never by blur.",
  "camera": "phone resting low, at the height of the table edge, 0.5x ultra-wide lens, pointing slightly upward, fixed",
  "lighting": "Neutral overcast daylight from a window, the outside clearly visible through the window, never white or blown out, soft even light on the face, hands and feet with no harsh shadows.",
  "state": "Start frame: a fine mist of perfume is leaving the bottle toward the sole of the bare foot.",
  "realism": "Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday reality, background fully in focus, everything in sharp focus, no AI polish, no beauty smoothing.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no printed lettering or brand on the perfume bottle, no studio, no plastic-looking human skin, no extra fingers, no extra toes, no third hand, no supernatural lighting, no blur, no bokeh, no artificial lighting, no warm orange color cast, no yellow tint on the skin, no golden glow, no golden hour light, no sunset, no red neon, no de-aging, no beauty smoothing, no visible phone, no HDR, no cinematic lighting, no second person in frame, no bathroom, no bathtub, no card in frame, no shoes, no socks"
}
```

### K02 · T2 a T19, corpo, câmera alta, apontando para a lente · anexar ÂNCORA + FRAME DO MODELO

```text
K02
{
  "format": "IMPORTANT: THIS IS IPHONE FOOTAGE. Vertical 9:16.",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "reference_use": "Use the first attached image only for Lorraine Vance's exact identity, wardrobe, jewelry, SOULMATE card and own setting. Use the second attached image only as a composition reference for the camera position, framing and pose; do not copy its person, robe, bathroom, gold fixtures, labels or on-screen text.",
  "identity_main": "The exact fictional AI character Lorraine Vance: white American woman around fifty-two, closely shaved head with grey stubble, freckles and sunspots on her face and scalp, light grey-green eyes, defined jaw, fine lines and no makeup.",
  "wardrobe": "Light-wash denim shirt worn open over a fitted black crew-neck T-shirt, dark jeans rolled up at the ankles, barefoot, large silver hoop earrings, a thin silver chain necklace and black-framed reading glasses hanging from the T-shirt collar.",
  "scene": "Her own bright white American kitchen, the same lived-in kitchen as the reference, unchanged: white walls and white quartz counters, the light wood floating shelves with clear quartz crystal points, a lit incense stick, a white pillar candle and a small American flag, discreet but visible and in focus, a framed zodiac wheel chart and a small wooden crucifix on the wall, and a window with the street clearly visible.",
  "prop": "On the edge of her white quartz kitchen counter in the lower left corner stands a tall faceted gold perfume bottle with an ornate embossed pattern and a gold cap, completely plain with no label. With one hand Lorraine Vance points at the lens; in the other hand, at chest height and facing the lens, she holds the holographic SOULMATE card from the reference: a tarot-sized card with a rainbow mirror-foil border and saturated art of a brown-haired woman and a man embracing under a rainbow glow, a bright heart and red roses at the bottom, with the word SOULMATE on a pale banner at the bottom.",
  "posture": "Lorraine Vance sits on a low seat, a low stool beside her kitchen counter, leaning forward toward the lens, bare feet on the floor, one hand pointing at the lens.",
  "composition": "High-angle shot: the gold perfume bottle is very close to the lens in the lower left corner, about 12 inches from the lens, and takes up about 15 percent of the frame, closer to the camera than her face. Lorraine Vance sits low in the center, seen from the top of the head down to the bare feet, face in the upper third, one hand pointing at the lens. Nothing else is on the edge. The background is reduced by framing, never by blur.",
  "camera": "phone held up high, high angle from above looking down at about forty-five degrees, 1x lens, fixed",
  "lighting": "Neutral overcast daylight from a window, the outside clearly visible through the window, never white or blown out, soft even light on the face, hands and feet with no harsh shadows.",
  "state": "Start frame: Lorraine Vance points at the lens, caught mid-sentence, lips naturally parted, animated expression.",
  "realism": "Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday reality, background fully in focus, everything in sharp focus, no AI polish, no beauty smoothing.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no printed lettering or brand on the perfume bottle, no studio, no plastic-looking human skin, no extra fingers, no extra toes, no third hand, no supernatural lighting, no blur, no bokeh, no artificial lighting, no warm orange color cast, no yellow tint on the skin, no golden glow, no golden hour light, no sunset, no red neon, no de-aging, no beauty smoothing, no visible phone, no HDR, no cinematic lighting, no second person in frame, no bathroom, no bathtub, no second card, no standing pose"
}
```

## 3. PROMPTS DE VÍDEO (um bloco por V)

### V01 · T1 · frame inicial = a imagem escolhida do K01

```text
V01
(sem fala no take: gancho mudo, a avatar fica em silêncio o clipe inteiro, boca fechada)

o que acontece no vídeo: Lorraine Vance borrifa o frasco dourado de perfume na sola do pé descalço, que está colado na lente; depois larga o frasco e esfrega o pé devagar com as duas mãos.

câmera: fixa, rente à superfície, grande angular, sem movimento

som ambiente: cozinha residencial silenciosa, som do borrifo do perfume, sem música
```

### V02 · T2 · frame inicial = a imagem escolhida do K02

```text
V02
a avatar Lorraine Vance, mulher, fala em inglês com sotaque americano de Chicago, voz feminina grave, direta e de humor seco de uma mulher de cinquenta e dois anos de Chicago, confiante e direta, apontando para quem assiste, voz autêntica, como se exigisse ser ouvida, a seguinte frase: "If you need urgent and unexpected money, start putting perfume on your feet."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Lorraine Vance aponta para a lente com uma mão, segurando a carta com a outra, e fala.

câmera: fixa, de cima, sem movimento

som ambiente: cozinha residencial silenciosa, sem música
```

### V03 · T3 · frame inicial = a imagem escolhida do K02

```text
V03
a avatar Lorraine Vance, mulher, fala em inglês com sotaque americano de Chicago, voz feminina grave, direta e de humor seco de uma mulher de cinquenta e dois anos de Chicago, baixa, como quem conta um segredo de gente rica, voz autêntica, como se exigisse ser ouvida, a seguinte frase: "This is the secret that millionaires in Dubai use every single day to attract prosperity and abundance, but almost nobody talks about it."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Lorraine Vance aponta para a lente com uma mão e segura a carta com a outra, falando com pequenos gestos naturais.

câmera: fixa, de cima, sem movimento

som ambiente: cozinha residencial silenciosa, sem música
```

### V04 · T4 · frame inicial = a imagem escolhida do K02

```text
V04
a avatar Lorraine Vance, mulher, fala em inglês com sotaque americano de Chicago, voz feminina grave, direta e de humor seco de uma mulher de cinquenta e dois anos de Chicago, firme, voz autêntica, como se exigisse ser ouvida, a seguinte frase: "If you do not have this habit yet, start today, and keep it to yourself. Not a word to anyone."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Lorraine Vance aponta para a lente com uma mão e segura a carta com a outra, falando com pequenos gestos naturais.

câmera: fixa, de cima, sem movimento

som ambiente: cozinha residencial silenciosa, sem música
```

### V05 · T5 · frame inicial = a imagem escolhida do K02

```text
V05
a avatar Lorraine Vance, mulher, fala em inglês com sotaque americano de Chicago, voz feminina grave, direta e de humor seco de uma mulher de cinquenta e dois anos de Chicago, séria, voz autêntica, como se exigisse ser ouvida, a seguinte frase: "Only a few people will ever come across this video before this week is over."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Lorraine Vance aponta para a lente com uma mão e segura a carta com a outra, falando com pequenos gestos naturais.

câmera: fixa, de cima, sem movimento

som ambiente: cozinha residencial silenciosa, sem música
```

### V06 · T6 · frame inicial = a imagem escolhida do K02

```text
V06
a avatar Lorraine Vance, mulher, fala em inglês com sotaque americano de Chicago, voz feminina grave, direta e de humor seco de uma mulher de cinquenta e dois anos de Chicago, séria e próxima, voz autêntica, como se exigisse ser ouvida, a seguinte frase: "I have no clue who is watching, but don't move on, because if this message found you today, it arrived as a sign."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Lorraine Vance aponta para a lente com uma mão e segura a carta com a outra, falando com pequenos gestos naturais.

câmera: fixa, de cima, sem movimento

som ambiente: cozinha residencial silenciosa, sem música
```

### V07 · T7 · frame inicial = a imagem escolhida do K02

```text
V07
a avatar Lorraine Vance, mulher, fala em inglês com sotaque americano de Chicago, voz feminina grave, direta e de humor seco de uma mulher de cinquenta e dois anos de Chicago, intrigante, marcando "It is about your feet", voz autêntica, como se exigisse ser ouvida, a seguinte frase: "There is one detail about this blessing that almost nobody explains. Pay attention, because this is not really about the perfume. It is about your feet."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Lorraine Vance aponta para os próprios pés descalços enquanto fala.

câmera: fixa, de cima, sem movimento

som ambiente: cozinha residencial silenciosa, sem música
```

### V08 · T8 · frame inicial = a imagem escolhida do K02

```text
V08
a avatar Lorraine Vance, mulher, fala em inglês com sotaque americano de Chicago, voz feminina grave, direta e de humor seco de uma mulher de cinquenta e dois anos de Chicago, calma e convicta, voz autêntica, como se exigisse ser ouvida, a seguinte frase: "Your feet are what carry you toward every opportunity, every open door, every meeting, and every place where your life can change."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Lorraine Vance aponta para a lente com uma mão e segura a carta com a outra, falando com pequenos gestos naturais.

câmera: fixa, de cima, sem movimento

som ambiente: cozinha residencial silenciosa, sem música
```

### V09 · T9 · frame inicial = a imagem escolhida do K02

```text
V09
a avatar Lorraine Vance, mulher, fala em inglês com sotaque americano de Chicago, voz feminina grave, direta e de humor seco de uma mulher de cinquenta e dois anos de Chicago, suave, voz autêntica, como se exigisse ser ouvida, a seguinte frase: "And when you put perfume on your feet, you are not just perfuming your skin."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Lorraine Vance aponta para a lente com uma mão e segura a carta com a outra, falando com pequenos gestos naturais.

câmera: fixa, de cima, sem movimento

som ambiente: cozinha residencial silenciosa, sem música
```

### V10 · T10 · frame inicial = a imagem escolhida do K02

```text
V10
a avatar Lorraine Vance, mulher, fala em inglês com sotaque americano de Chicago, voz feminina grave, direta e de humor seco de uma mulher de cinquenta e dois anos de Chicago, calma e inspirada, voz autêntica, como se exigisse ser ouvida, a seguinte frase: "You are symbolically perfuming the path you are about to walk, putting intention into your steps and declaring that you are ready to walk toward prosperity."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Lorraine Vance aponta para a lente com uma mão e segura a carta com a outra, falando com pequenos gestos naturais.

câmera: fixa, de cima, sem movimento

som ambiente: cozinha residencial silenciosa, sem música
```

### V11 · T11 · frame inicial = a imagem escolhida do K02

```text
V11
a avatar Lorraine Vance, mulher, fala em inglês com sotaque americano de Chicago, voz feminina grave, direta e de humor seco de uma mulher de cinquenta e dois anos de Chicago, reverente, como quem ora, voz autêntica, como se exigisse ser ouvida, a seguinte frase: "So take your perfume, spray a little on your feet and say, I perfume the path I'm about to walk. Lord, bless my steps."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Lorraine Vance fecha os olhos por um instante, como quem ora, e volta a olhar para a lente.

câmera: fixa, de cima, sem movimento

som ambiente: cozinha residencial silenciosa, sem música
```

### V12 · T12 · frame inicial = a imagem escolhida do K02

```text
V12
a avatar Lorraine Vance, mulher, fala em inglês com sotaque americano de Chicago, voz feminina grave, direta e de humor seco de uma mulher de cinquenta e dois anos de Chicago, reverente e emocionada, voz autêntica, como se exigisse ser ouvida, a seguinte frase: "Open the doors to prosperity. Guide me toward the opportunities prepared for me and allow abundance to follow me wherever I go."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Lorraine Vance fala de olhos semicerrados, com a mão livre no peito.

câmera: fixa, de cima, sem movimento

som ambiente: cozinha residencial silenciosa, sem música
```

### V13 · T13 · frame inicial = a imagem escolhida do K02

```text
V13
a avatar Lorraine Vance, mulher, fala em inglês com sotaque americano de Chicago, voz feminina grave, direta e de humor seco de uma mulher de cinquenta e dois anos de Chicago, calorosa, depois animada, voz autêntica, como se exigisse ser ouvida, a seguinte frase: "Do this with faith and gratitude. And if you are wondering which perfume to use, use the most expensive perfume you have."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Lorraine Vance aponta para a lente com uma mão e segura a carta com a outra, falando com pequenos gestos naturais.

câmera: fixa, de cima, sem movimento

som ambiente: cozinha residencial silenciosa, sem música
```

### V14 · T14 · frame inicial = a imagem escolhida do K02

```text
V14
a avatar Lorraine Vance, mulher, fala em inglês com sotaque americano de Chicago, voz feminina grave, direta e de humor seco de uma mulher de cinquenta e dois anos de Chicago, firme e convicta, voz autêntica, como se exigisse ser ouvida, a seguinte frase: "The brand does not matter. If you are asking life to open the best doors for you, put on your steps what represents your best."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Lorraine Vance aponta para a lente com uma mão e segura a carta com a outra, falando com pequenos gestos naturais.

câmera: fixa, de cima, sem movimento

som ambiente: cozinha residencial silenciosa, sem música
```

### V15 · T15 · frame inicial = a imagem escolhida do K02

```text
V15
a avatar Lorraine Vance, mulher, fala em inglês com sotaque americano de Chicago, voz feminina grave, direta e de humor seco de uma mulher de cinquenta e dois anos de Chicago, animada, voz autêntica, como se exigisse ser ouvida, a seguinte frase: "And once you finish, there are three things you need to do to mark that you are ready to receive the prosperity you just asked for."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Lorraine Vance aponta para a lente com uma mão e segura a carta com a outra, falando com pequenos gestos naturais.

câmera: fixa, de cima, sem movimento

som ambiente: cozinha residencial silenciosa, sem música
```

### V16 · T16 · frame inicial = a imagem escolhida do K02

```text
V16
a avatar Lorraine Vance, mulher, fala em inglês com sotaque americano de Chicago, voz feminina grave, direta e de humor seco de uma mulher de cinquenta e dois anos de Chicago, firme, em ritmo de instrução, voz autêntica, como se exigisse ser ouvida, a seguinte frase: "Like this video. That's the first seal. Save this post so you can come back to this blessing whenever you need it."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Lorraine Vance mostra a carta para a lente e fala com firmeza.

câmera: fixa, de cima, sem movimento

som ambiente: cozinha residencial silenciosa, sem música
```

### V17 · T17 · frame inicial = a imagem escolhida do K02

```text
V17
a avatar Lorraine Vance, mulher, fala em inglês com sotaque americano de Chicago, voz feminina grave, direta e de humor seco de uma mulher de cinquenta e dois anos de Chicago, firme e rápida, voz autêntica, como se exigisse ser ouvida, a seguinte frase: "That's the second seal. Send this video to yourself so you do not lose this message. That's the third seal."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Lorraine Vance aponta para a lente com uma mão e segura a carta com a outra, falando com pequenos gestos naturais.

câmera: fixa, de cima, sem movimento

som ambiente: cozinha residencial silenciosa, sem música
```

### V18 · T18 · frame inicial = a imagem escolhida do K02

```text
V18
a avatar Lorraine Vance, mulher, fala em inglês com sotaque americano de Chicago, voz feminina grave, direta e de humor seco de uma mulher de cinquenta e dois anos de Chicago, firme, depois séria, voz autêntica, como se exigisse ser ouvida, a seguinte frase: "Then comment 222, so I know you completed all three, but do not stop here, because these three seals only prepare your intention."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Lorraine Vance aponta para a lente com uma mão e segura a carta com a outra, falando com pequenos gestos naturais.

câmera: fixa, de cima, sem movimento

som ambiente: cozinha residencial silenciosa, sem música
```

### V19 · T19 · frame inicial = a imagem escolhida do K02

```text
V19
a avatar Lorraine Vance, mulher, fala em inglês com sotaque americano de Chicago, voz feminina grave, direta e de humor seco de uma mulher de cinquenta e dois anos de Chicago, próxima e urgente, olhando direto na lente, voz autêntica, como se exigisse ser ouvida, a seguinte frase: "There is still one final step that completes this process. Follow me right now, because I will share that final step in my next video."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Lorraine Vance se inclina para a lente e aponta para ela, segurando a carta.

câmera: fixa, de cima, sem movimento

som ambiente: cozinha residencial silenciosa, sem música
```

## 4. Montagem no CapCut

1. Clipes numerados na ordem: V01 a V19.
2. V01 (gancho mudo): usar ~2,6 s. Tarja "PUT PERFUME ON YOUR FEET" em amarelo no alto e "Millionaire mode: Unlocked 🔒" num balão branco no meio. Flash de luz de 0,1 s no corte para o V02.
3. V02 a V19: zero tempo morto, todo clipe começa já falando; cortar logo depois da última palavra. Isolate Voice / Keep Vocal. Todos saem do mesmo frame, então a troca de clipe fica no mesmo enquadramento, como no modelo.
4. Legenda karaokê amarela e branca, do V02 ao V19; "222 ✨" fixo no canto superior esquerdo do V02 ao V19.
5. Setas vermelhas apontando para cima no V19.
6. Sem Voice Changer: a voz vem do prompt de cada V.
7. Música só a partir do V02, entre -19 e -20 dB, fora da biblioteca do TikTok.
8. Rótulo pequeno `AI-generated` num canto do vídeo.

## 5. Transcrição final por take

| Take | English | Português |
|---|---|---|
| T1 | (sem fala) | (sem fala) |
| T2 | If you need urgent and unexpected money, start putting perfume on your feet. | Se você precisa de dinheiro urgente e inesperado, comece a passar perfume nos pés. |
| T3 | This is the secret that millionaires in Dubai use every single day to attract prosperity and abundance, but almost nobody talks about it. | Esse é o segredo que os milionários de Dubai usam todo santo dia para atrair prosperidade e abundância, mas quase ninguém fala disso. |
| T4 | If you do not have this habit yet, start today, and keep it to yourself. Not a word to anyone. | Se você ainda não tem esse hábito, comece hoje, e guarde pra você. Nem uma palavra pra ninguém. |
| T5 | Only a few people will ever come across this video before this week is over. | Só algumas pessoas vão encontrar este vídeo antes de esta semana acabar. |
| T6 | I have no clue who is watching, but don't move on, because if this message found you today, it arrived as a sign. | Eu não faço ideia de quem está assistindo, mas não passe, porque se esta mensagem te encontrou hoje, ela chegou como um sinal. |
| T7 | There is one detail about this blessing that almost nobody explains. Pay attention, because this is not really about the perfume. It is about your feet. | Tem um detalhe dessa bênção que quase ninguém explica. Preste atenção, porque isso não é bem sobre o perfume. É sobre os seus pés. |
| T8 | Your feet are what carry you toward every opportunity, every open door, every meeting, and every place where your life can change. | Os seus pés são o que te levam até cada oportunidade, cada porta aberta, cada encontro e cada lugar onde a sua vida pode mudar. |
| T9 | And when you put perfume on your feet, you are not just perfuming your skin. | E quando você passa perfume nos pés, não está só perfumando a pele. |
| T10 | You are symbolically perfuming the path you are about to walk, putting intention into your steps and declaring that you are ready to walk toward prosperity. | Você está perfumando simbolicamente o caminho que vai percorrer, colocando intenção nos seus passos e declarando que está pronta para caminhar rumo à prosperidade. |
| T11 | So take your perfume, spray a little on your feet and say, I perfume the path I'm about to walk. Lord, bless my steps. | Então pegue o seu perfume, borrife um pouco nos pés e diga: eu perfumo o caminho que vou percorrer. Senhor, abençoe os meus passos. |
| T12 | Open the doors to prosperity. Guide me toward the opportunities prepared for me and allow abundance to follow me wherever I go. | Abra as portas da prosperidade. Me guie até as oportunidades preparadas pra mim e permita que a abundância me siga aonde eu for. |
| T13 | Do this with faith and gratitude. And if you are wondering which perfume to use, use the most expensive perfume you have. | Faça isso com fé e gratidão. E se você está se perguntando qual perfume usar, use o perfume mais caro que você tem. |
| T14 | The brand does not matter. If you are asking life to open the best doors for you, put on your steps what represents your best. | A marca não importa. Se você está pedindo pra vida abrir as melhores portas pra você, coloque nos seus passos o que representa o seu melhor. |
| T15 | And once you finish, there are three things you need to do to mark that you are ready to receive the prosperity you just asked for. | E assim que terminar, tem três coisas que você precisa fazer pra marcar que está pronta pra receber a prosperidade que acabou de pedir. |
| T16 | Like this video. That's the first seal. Save this post so you can come back to this blessing whenever you need it. | Curta este vídeo. Esse é o primeiro selo. Salve este post pra poder voltar a essa bênção sempre que precisar. |
| T17 | That's the second seal. Send this video to yourself so you do not lose this message. That's the third seal. | Esse é o segundo selo. Mande este vídeo pra você mesma pra não perder esta mensagem. Esse é o terceiro selo. |
| T18 | Then comment 222, so I know you completed all three, but do not stop here, because these three seals only prepare your intention. | Depois comente 222, pra eu saber que você fez os três, mas não pare aqui, porque esses três selos só preparam a sua intenção. |
| T19 | There is still one final step that completes this process. Follow me right now, because I will share that final step in my next video. | Ainda falta um último passo que completa esse processo. Me siga agora, porque vou mostrar esse último passo no meu próximo vídeo. |

## 6. Roteiro final em inglês

1. (sem fala: gancho mudo)
2. If you need urgent and unexpected money, start putting perfume on your feet.
3. This is the secret that millionaires in Dubai use every single day to attract prosperity and abundance, but almost nobody talks about it.
4. If you do not have this habit yet, start today, and keep it to yourself. Not a word to anyone.
5. Only a few people will ever come across this video before this week is over.
6. I have no clue who is watching, but don't move on, because if this message found you today, it arrived as a sign.
7. There is one detail about this blessing that almost nobody explains. Pay attention, because this is not really about the perfume. It is about your feet.
8. Your feet are what carry you toward every opportunity, every open door, every meeting, and every place where your life can change.
9. And when you put perfume on your feet, you are not just perfuming your skin.
10. You are symbolically perfuming the path you are about to walk, putting intention into your steps and declaring that you are ready to walk toward prosperity.
11. So take your perfume, spray a little on your feet and say, I perfume the path I'm about to walk. Lord, bless my steps.
12. Open the doors to prosperity. Guide me toward the opportunities prepared for me and allow abundance to follow me wherever I go.
13. Do this with faith and gratitude. And if you are wondering which perfume to use, use the most expensive perfume you have.
14. The brand does not matter. If you are asking life to open the best doors for you, put on your steps what represents your best.
15. And once you finish, there are three things you need to do to mark that you are ready to receive the prosperity you just asked for.
16. Like this video. That's the first seal. Save this post so you can come back to this blessing whenever you need it.
17. That's the second seal. Send this video to yourself so you do not lose this message. That's the third seal.
18. Then comment 222, so I know you completed all three, but do not stop here, because these three seals only prepare your intention.
19. There is still one final step that completes this process. Follow me right now, because I will share that final step in my next video.

If you need urgent and unexpected money, start putting perfume on your feet. This is the secret that millionaires in Dubai use every single day to attract prosperity and abundance, but almost nobody talks about it. If you do not have this habit yet, start today, and keep it to yourself. Not a word to anyone. Only a few people will ever come across this video before this week is over. I have no clue who is watching, but don't move on, because if this message found you today, it arrived as a sign. There is one detail about this blessing that almost nobody explains. Pay attention, because this is not really about the perfume. It is about your feet. Your feet are what carry you toward every opportunity, every open door, every meeting, and every place where your life can change. And when you put perfume on your feet, you are not just perfuming your skin. You are symbolically perfuming the path you are about to walk, putting intention into your steps and declaring that you are ready to walk toward prosperity. So take your perfume, spray a little on your feet and say, I perfume the path I'm about to walk. Lord, bless my steps. Open the doors to prosperity. Guide me toward the opportunities prepared for me and allow abundance to follow me wherever I go. Do this with faith and gratitude. And if you are wondering which perfume to use, use the most expensive perfume you have. The brand does not matter. If you are asking life to open the best doors for you, put on your steps what represents your best. And once you finish, there are three things you need to do to mark that you are ready to receive the prosperity you just asked for. Like this video. That's the first seal. Save this post so you can come back to this blessing whenever you need it. That's the second seal. Send this video to yourself so you do not lose this message. That's the third seal. Then comment 222, so I know you completed all three, but do not stop here, because these three seals only prepare your intention. There is still one final step that completes this process. Follow me right now, because I will share that final step in my next video.
