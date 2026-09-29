# ENTREGA | Darlene Pruitt | Auraly Growth Prece

Produção `auraly_growth_prece` · Ângulo 3 · GROWTH · vídeo modelo de pessoa real (orgânico) · rodada de VALIDAÇÃO · perfil AURALY

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

Checklist de envio: 32/32 aprovados (N/A: A1, A2, A7, A9 fiéis ao modelo orgânico; A10 growth sem produto; C3 a C7 sem segunda pessoa, selfie na mão, frase curta repetida, cena atuada ou motion control)

Ficha: 1/1 K conferido contra o frame do modelo, placar 14/14 (`FICHA_FRAMES.md`, GATE_VISUAL Parte 6)

## Anexos e mapa

- **Âncora Darlene Pruitt:** `producao/_ancoras/darlene_pruitt_ancora.jpg` no K01.
- **No K01**, anexar também `input/frames_modelo/K01_modelo.png`, só como composição.

```text
MAPA K/V
V01: K01
V02: K01
V03: K01
V04: K01
V05: K01
V06: K01
V07: K01
V08: K01
V09: K01
V10: K01
V11: K01
V12: K01
V13: K01
V14: K01
```

## 2. PROMPT DE IMAGEM

### K01 · T1 a T14, selfie apoiada, mãos em prece coladas na lente · anexar ÂNCORA + FRAME DO MODELO

```text
K01
{
  "format": "IMPORTANT: THIS IS IPHONE FOOTAGE. Vertical 9:16.",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "reference_use": "Use the first attached image only for Darlene Pruitt's exact identity, wardrobe, jewelry and own setting. Use the second attached image only as a composition reference for the camera position, framing and pose; do not copy its person, clothes, bedroom, lamp or on-screen text.",
  "identity_main": "The exact fictional AI character Darlene Pruitt: white American woman around fifty-six from Texas, voluminous shaggy layered platinum-blonde hair with visible dark roots, brown eyes, fair skin with crow's feet and fine lines, everyday makeup with defined brows, mascara and pink lipstick.",
  "wardrobe": "White long-sleeve button-up shirt with the cuffs loosely rolled, blue jeans, a large turquoise and silver squash-blossom necklace, several big turquoise rings on the fingers of both hands and a silver cuff bracelet set with turquoise.",
  "scene": "Her own rustic American kitchen with knotty pine wood-paneled walls, the same lived-in kitchen as the reference, unchanged. She sits at her wooden kitchen island; behind her the pine wall with a framed astrological chart and a small wooden crucifix, and the open wooden shelves by the window with glass jars and a small American flag, discreet but visible and in focus.",
  "prop": "No objects: her fair hands with big turquoise rings on several fingers are the only thing in the foreground, hands pressed together in prayer with the fingers interlaced and the fingertips pointing up.",
  "posture": "Darlene Pruitt sits facing the lens, elbows resting in front of her chest, hands pressed together in prayer right in front of the phone, looking straight into the lens.",
  "composition": "Casual selfie framing: the hands pressed together in prayer are very close to the lens in the bottom center, about 8 inches from the lens, and take up about 20 percent of the frame, touching the bottom edge, closer to the camera than her face, nothing else competing with them. Her face sits in the upper middle of the frame, shoulders and chest in the middle, the setting behind in the top third. Nothing else is in the foreground. The background is reduced by framing, never by blur.",
  "camera": "phone propped on the surface just below the chin, at chest height, 1x front lens, pointing slightly upward, fixed",
  "lighting": "Neutral overcast daylight from a window, the outside clearly visible through the window, never white or blown out, soft even light on the face and hands with no harsh shadows.",
  "state": "Start frame: Darlene Pruitt looks into the lens, caught mid-sentence, lips naturally parted, calm and intimate expression.",
  "realism": "Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday reality, background fully in focus, everything in sharp focus, no AI polish, no beauty smoothing.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no studio, no plastic-looking human skin, no extra fingers, no third hand, no supernatural lighting, no blur, no bokeh, no artificial lighting, no warm orange color cast, no yellow tint on the skin, no golden glow, no golden hour light, no sunset, no lamp glow, no de-aging, no beauty smoothing, no visible phone, no HDR, no cinematic lighting, no second person in frame, no card in hand, no props in the hands, no standing pose"
}
```

## 3. PROMPTS DE VÍDEO (um bloco por V)

### V01 · T1 · frame inicial = a imagem escolhida do K01

```text
V01
a avatar Darlene Pruitt (mulher) fala em inglês com sotaque americano texano carregado, voz feminina média, levemente rouca e calorosa de uma texana de cinquenta e seis anos, em tom de conversa de quem grava um vídeo no celular para os seguidores, natural, próximo e confiante, quase em segredo, no mesmo ritmo do vídeo modelo, a seguinte frase: "Once you watch this, you keep it to yourself. Tell nobody. Very few people will get to see this before the month is out."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Darlene Pruitt mantém as mãos juntas em prece perto da lente e fala baixo olhando para a lente.

câmera: celular apoiado, fixo, sem movimento

som ambiente: cozinha residencial silenciosa, sem música
```

### V02 · T2 · frame inicial = a imagem escolhida do K01

```text
V02
a avatar Darlene Pruitt (mulher) fala em inglês com sotaque americano texano carregado, voz feminina média, levemente rouca e calorosa de uma texana de cinquenta e seis anos, em tom de conversa de quem grava um vídeo no celular para os seguidores, natural, próximo e confiante, séria, em tom de aviso, no mesmo ritmo do vídeo modelo, a seguinte frase: "I have no idea who you are, but don't swipe away. If this landed in front of you today, it came as a last call."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Darlene Pruitt mantém as mãos juntas em prece perto da lente e fala olhando para a lente, piscando devagar.

câmera: celular apoiado, fixo, sem movimento

som ambiente: cozinha residencial silenciosa, sem música
```

### V03 · T3 · frame inicial = a imagem escolhida do K01

```text
V03
a avatar Darlene Pruitt (mulher) fala em inglês com sotaque americano texano carregado, voz feminina média, levemente rouca e calorosa de uma texana de cinquenta e seis anos, em tom de conversa de quem grava um vídeo no celular para os seguidores, natural, próximo e confiante, baixa e animada, no mesmo ritmo do vídeo modelo, a seguinte frase: "A strong tide of blessings, love and money is moving toward you. Keep quiet about it, but the doorway of abundance just opened."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Darlene Pruitt mantém as mãos juntas em prece perto da lente e fala olhando para a lente, piscando devagar.

câmera: celular apoiado, fixo, sem movimento

som ambiente: cozinha residencial silenciosa, sem música
```

### V04 · T4 · frame inicial = a imagem escolhida do K01

```text
V04
a avatar Darlene Pruitt (mulher) fala em inglês com sotaque americano texano carregado, voz feminina média, levemente rouca e calorosa de uma texana de cinquenta e seis anos, em tom de conversa de quem grava um vídeo no celular para os seguidores, natural, próximo e confiante, aliviada e emocionada, no mesmo ritmo do vídeo modelo, a seguinte frase: "The hardest part is behind you now. There is money, abundance and someone truly amazing on the way into your life."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Darlene Pruitt mantém as mãos juntas em prece perto da lente e fala olhando para a lente, piscando devagar.

câmera: celular apoiado, fixo, sem movimento

som ambiente: cozinha residencial silenciosa, sem música
```

### V05 · T5 · frame inicial = a imagem escolhida do K01

```text
V05
a avatar Darlene Pruitt (mulher) fala em inglês com sotaque americano texano carregado, voz feminina média, levemente rouca e calorosa de uma texana de cinquenta e seis anos, em tom de conversa de quem grava um vídeo no celular para os seguidores, natural, próximo e confiante, firme e calma, no mesmo ritmo do vídeo modelo, a seguinte frase: "Before you swipe, squeeze your right hand shut and stay with me to the last second. This message was not meant for everybody."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Darlene Pruitt aperta de leve as mãos juntas em prece enquanto fala.

câmera: celular apoiado, fixo, sem movimento

som ambiente: cozinha residencial silenciosa, sem música
```

### V06 · T6 · frame inicial = a imagem escolhida do K01

```text
V06
a avatar Darlene Pruitt (mulher) fala em inglês com sotaque americano texano carregado, voz feminina média, levemente rouca e calorosa de uma texana de cinquenta e seis anos, em tom de conversa de quem grava um vídeo no celular para os seguidores, natural, próximo e confiante, séria, depois intrigada, no mesmo ritmo do vídeo modelo, a seguinte frase: "The universe picked you out. Walk away now and the energy snaps. Something very rare is unfolding around you at this moment."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Darlene Pruitt fecha os olhos por um instante e volta a olhar para a lente, com as mãos em prece.

câmera: celular apoiado, fixo, sem movimento

som ambiente: cozinha residencial silenciosa, sem música
```

### V07 · T7 · frame inicial = a imagem escolhida do K01

```text
V07
a avatar Darlene Pruitt (mulher) fala em inglês com sotaque americano texano carregado, voz feminina média, levemente rouca e calorosa de uma texana de cinquenta e seis anos, em tom de conversa de quem grava um vídeo no celular para os seguidores, natural, próximo e confiante, intensa, no mesmo ritmo do vídeo modelo, a seguinte frase: "I can see the chains of lack that held you back finally snapping apart."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Darlene Pruitt mantém as mãos juntas em prece perto da lente e fala olhando para a lente, piscando devagar.

câmera: celular apoiado, fixo, sem movimento

som ambiente: cozinha residencial silenciosa, sem música
```

### V08 · T8 · frame inicial = a imagem escolhida do K01

```text
V08
a avatar Darlene Pruitt (mulher) fala em inglês com sotaque americano texano carregado, voz feminina média, levemente rouca e calorosa de uma texana de cinquenta e seis anos, em tom de conversa de quem grava um vídeo no celular para os seguidores, natural, próximo e confiante, calorosa, no mesmo ritmo do vídeo modelo, a seguinte frase: "The love that was delayed for you is finally finding its way back to your door."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Darlene Pruitt mantém as mãos juntas em prece perto da lente e fala olhando para a lente, piscando devagar.

câmera: celular apoiado, fixo, sem movimento

som ambiente: cozinha residencial silenciosa, sem música
```

### V09 · T9 · frame inicial = a imagem escolhida do K01

```text
V09
a avatar Darlene Pruitt (mulher) fala em inglês com sotaque americano texano carregado, voz feminina média, levemente rouca e calorosa de uma texana de cinquenta e seis anos, em tom de conversa de quem grava um vídeo no celular para os seguidores, natural, próximo e confiante, firme, no mesmo ritmo do vídeo modelo, a seguinte frase: "Within seven minutes, the lack that kept following you will be wiped out for good."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Darlene Pruitt mantém as mãos juntas em prece perto da lente e fala olhando para a lente, piscando devagar.

câmera: celular apoiado, fixo, sem movimento

som ambiente: cozinha residencial silenciosa, sem música
```

### V10 · T10 · frame inicial = a imagem escolhida do K01

```text
V10
a avatar Darlene Pruitt (mulher) fala em inglês com sotaque americano texano carregado, voz feminina média, levemente rouca e calorosa de uma texana de cinquenta e seis anos, em tom de conversa de quem grava um vídeo no celular para os seguidores, natural, próximo e confiante, urgente e próxima, no mesmo ritmo do vídeo modelo, a seguinte frase: "So share this video with yourself now, because seven minutes from now you'll come back and see the shift for yourself."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Darlene Pruitt mantém as mãos juntas em prece perto da lente e fala olhando para a lente, piscando devagar.

câmera: celular apoiado, fixo, sem movimento

som ambiente: cozinha residencial silenciosa, sem música
```

### V11 · T11 · frame inicial = a imagem escolhida do K01

```text
V11
a avatar Darlene Pruitt (mulher) fala em inglês com sotaque americano texano carregado, voz feminina média, levemente rouca e calorosa de uma texana de cinquenta e seis anos, em tom de conversa de quem grava um vídeo no celular para os seguidores, natural, próximo e confiante, em ritmo de instrução, no mesmo ritmo do vídeo modelo, a seguinte frase: "Now open your hand and hit save. That's your first seal. Tap the screen twice, fast. That's your second seal."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Darlene Pruitt abre as mãos por um instante e junta de novo em prece enquanto fala.

câmera: celular apoiado, fixo, sem movimento

som ambiente: cozinha residencial silenciosa, sem música
```

### V12 · T12 · frame inicial = a imagem escolhida do K01

```text
V12
a avatar Darlene Pruitt (mulher) fala em inglês com sotaque americano texano carregado, voz feminina média, levemente rouca e calorosa de uma texana de cinquenta e seis anos, em tom de conversa de quem grava um vídeo no celular para os seguidores, natural, próximo e confiante, firme, depois animada, no mesmo ritmo do vídeo modelo, a seguinte frase: "Then drop 222 below so I know you did every step. Do it all, and tomorrow at 11:11 a.m. some beautiful news will reach you."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Darlene Pruitt mantém as mãos juntas em prece perto da lente e fala olhando para a lente, piscando devagar.

câmera: celular apoiado, fixo, sem movimento

som ambiente: cozinha residencial silenciosa, sem música
```

### V13 · T13 · frame inicial = a imagem escolhida do K01

```text
V13
a avatar Darlene Pruitt (mulher) fala em inglês com sotaque americano texano carregado, voz feminina média, levemente rouca e calorosa de uma texana de cinquenta e seis anos, em tom de conversa de quem grava um vídeo no celular para os seguidores, natural, próximo e confiante, baixa e séria, no mesmo ritmo do vídeo modelo, a seguinte frase: "But listen closely. This energy is delicate, and sharing it with others too early can shatter it."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Darlene Pruitt mantém as mãos juntas em prece perto da lente e fala olhando para a lente, piscando devagar.

câmera: celular apoiado, fixo, sem movimento

som ambiente: cozinha residencial silenciosa, sem música
```

### V14 · T14 · frame inicial = a imagem escolhida do K01

```text
V14
a avatar Darlene Pruitt (mulher) fala em inglês com sotaque americano texano carregado, voz feminina média, levemente rouca e calorosa de uma texana de cinquenta e seis anos, em tom de conversa de quem grava um vídeo no celular para os seguidores, natural, próximo e confiante, próxima e firme, no mesmo ritmo do vídeo modelo, a seguinte frase: "So follow me now, so this door stays open for you, because the next part of this sign is on its way."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Darlene Pruitt se inclina um pouco para a lente, com as mãos em prece.

câmera: celular apoiado, fixo, sem movimento

som ambiente: cozinha residencial silenciosa, sem música
```

## 4. Montagem no CapCut

1. Clipes numerados na ordem: V01 a V14.
2. Zero tempo morto: todo clipe começa já falando; cortar logo depois da última palavra. Isolate Voice / Keep Vocal no áudio. Todos saem do mesmo frame, então a troca de clipe vira jump cut no mesmo enquadramento, a gramática do próprio formato orgânico.
3. Legenda em serifa branca, 3 a 4 palavras por vez, no meio do quadro, do V01 ao V14, igual ao modelo.
4. "222" fixo no canto superior esquerdo e "11:11" no canto superior direito, o vídeo inteiro.
5. Sem Voice Changer: a voz vem do prompt de cada V.
6. Música só depois do gancho (a partir do V02), baixa, entre -19 e -20 dB, fora da biblioteca do TikTok.
7. Rótulo pequeno `AI-generated` num canto do vídeo.

## 5. Transcrição final por take

| Take | English | Português |
|---|---|---|
| T1 | Once you watch this, you keep it to yourself. Tell nobody. Very few people will get to see this before the month is out. | Depois de assistir isto, guarde pra você. Não conte pra ninguém. Pouquíssimas pessoas vão ver isto antes de o mês acabar. |
| T2 | I have no idea who you are, but don't swipe away. If this landed in front of you today, it came as a last call. | Eu não faço ideia de quem você é, mas não passe. Se isto caiu na sua frente hoje, chegou como um último chamado. |
| T3 | A strong tide of blessings, love and money is moving toward you. Keep quiet about it, but the doorway of abundance just opened. | Uma maré forte de bênçãos, amor e dinheiro está vindo na sua direção. Fique quieta sobre isso, mas a porta da abundância acabou de se abrir. |
| T4 | The hardest part is behind you now. There is money, abundance and someone truly amazing on the way into your life. | A parte mais difícil ficou pra trás. Tem dinheiro, abundância e alguém realmente incrível a caminho da sua vida. |
| T5 | Before you swipe, squeeze your right hand shut and stay with me to the last second. This message was not meant for everybody. | Antes de passar, feche bem a mão direita e fique comigo até o último segundo. Esta mensagem não era pra todo mundo. |
| T6 | The universe picked you out. Walk away now and the energy snaps. Something very rare is unfolding around you at this moment. | O universo escolheu você. Se sair agora, a energia se rompe. Algo muito raro está acontecendo ao seu redor neste momento. |
| T7 | I can see the chains of lack that held you back finally snapping apart. | Eu consigo ver as correntes da falta que te seguravam finalmente se partindo. |
| T8 | The love that was delayed for you is finally finding its way back to your door. | O amor que estava atrasado pra você finalmente está achando o caminho de volta até a sua porta. |
| T9 | Within seven minutes, the lack that kept following you will be wiped out for good. | Em até sete minutos, a falta que vivia te seguindo vai ser apagada de vez. |
| T10 | So share this video with yourself now, because seven minutes from now you'll come back and see the shift for yourself. | Então mande este vídeo pra você mesma agora, porque daqui a sete minutos você vai voltar e ver a virada com os próprios olhos. |
| T11 | Now open your hand and hit save. That's your first seal. Tap the screen twice, fast. That's your second seal. | Agora abra a mão e aperte salvar. Esse é o seu primeiro selo. Toque na tela duas vezes, rápido. Esse é o seu segundo selo. |
| T12 | Then drop 222 below so I know you did every step. Do it all, and tomorrow at 11:11 a.m. some beautiful news will reach you. | Depois deixe 222 aqui embaixo pra eu saber que você fez cada passo. Faça tudo, e amanhã às 11:11 da manhã uma notícia linda vai chegar até você. |
| T13 | But listen closely. This energy is delicate, and sharing it with others too early can shatter it. | Mas escute com atenção. Essa energia é delicada, e contar pra outras pessoas cedo demais pode quebrá-la. |
| T14 | So follow me now, so this door stays open for you, because the next part of this sign is on its way. | Então me siga agora, pra essa porta continuar aberta pra você, porque a próxima parte deste sinal está a caminho. |

## 6. Roteiro final em inglês

1. Once you watch this, you keep it to yourself. Tell nobody. Very few people will get to see this before the month is out.
2. I have no idea who you are, but don't swipe away. If this landed in front of you today, it came as a last call.
3. A strong tide of blessings, love and money is moving toward you. Keep quiet about it, but the doorway of abundance just opened.
4. The hardest part is behind you now. There is money, abundance and someone truly amazing on the way into your life.
5. Before you swipe, squeeze your right hand shut and stay with me to the last second. This message was not meant for everybody.
6. The universe picked you out. Walk away now and the energy snaps. Something very rare is unfolding around you at this moment.
7. I can see the chains of lack that held you back finally snapping apart.
8. The love that was delayed for you is finally finding its way back to your door.
9. Within seven minutes, the lack that kept following you will be wiped out for good.
10. So share this video with yourself now, because seven minutes from now you'll come back and see the shift for yourself.
11. Now open your hand and hit save. That's your first seal. Tap the screen twice, fast. That's your second seal.
12. Then drop 222 below so I know you did every step. Do it all, and tomorrow at 11:11 a.m. some beautiful news will reach you.
13. But listen closely. This energy is delicate, and sharing it with others too early can shatter it.
14. So follow me now, so this door stays open for you, because the next part of this sign is on its way.

Once you watch this, you keep it to yourself. Tell nobody. Very few people will get to see this before the month is out. I have no idea who you are, but don't swipe away. If this landed in front of you today, it came as a last call. A strong tide of blessings, love and money is moving toward you. Keep quiet about it, but the doorway of abundance just opened. The hardest part is behind you now. There is money, abundance and someone truly amazing on the way into your life. Before you swipe, squeeze your right hand shut and stay with me to the last second. This message was not meant for everybody. The universe picked you out. Walk away now and the energy snaps. Something very rare is unfolding around you at this moment. I can see the chains of lack that held you back finally snapping apart. The love that was delayed for you is finally finding its way back to your door. Within seven minutes, the lack that kept following you will be wiped out for good. So share this video with yourself now, because seven minutes from now you'll come back and see the shift for yourself. Now open your hand and hit save. That's your first seal. Tap the screen twice, fast. That's your second seal. Then drop 222 below so I know you did every step. Do it all, and tomorrow at 11:11 a.m. some beautiful news will reach you. But listen closely. This energy is delicate, and sharing it with others too early can shatter it. So follow me now, so this door stays open for you, because the next part of this sign is on its way.
