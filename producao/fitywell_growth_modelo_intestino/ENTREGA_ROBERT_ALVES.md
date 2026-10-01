# ENTREGA | Robert Alves | FityWell Growth Modelo de intestino

Produção `fitywell_growth_modelo_intestino` · Ângulo 2 · GROWTH · vídeo modelo de avatar IA · rodada de VALIDAÇÃO · perfil CLÁSSICO

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

Checklist de envio: 33/33 aprovados (N/A: A2, A7, A9 fiéis ao modelo; C3 a C7 sem segunda pessoa, selfie, frase repetida, cena atuada ou motion control)

Ficha: 13/13 K conferidos contra o frame do modelo, placar 14/14 cada (`FICHA_FRAMES.md`, GATE_VISUAL Parte 6)

## Anexos

- **Âncora Robert Alves:** `input/ancoras/04_robert_alves.jpg` em TODOS os K.
- **Em cada K**, anexar também o frame do modelo daquele passo (`input/frames_modelo/Kxx_modelo.png`), só como referência de composição.
- K01 a K13 casam com V01 a V13 pelo número. Todos os V têm fala.

| Código | Take | Frame do modelo |
|---|---|---|
| K01 / V01 | T1, gancho, comidas entrando no modelo transparente | `input/frames_modelo/K01_modelo.png` |
| K02 / V02 | T2, reveal, a bebida faz a massa sair por baixo | `input/frames_modelo/K02_modelo.png` |
| K03 / V03 | T3, limão da tábua para a panela | `input/frames_modelo/K03_modelo.png` |
| K04 / V04 | T4, limão boiando, colher mexendo | `input/frames_modelo/K04_modelo.png` |
| K05 / V05 | T5, colher de chia | `input/frames_modelo/K05_modelo.png` |
| K06 / V06 | T6, cúrcuma, a água amarelando | `input/frames_modelo/K06_modelo.png` |
| K07 / V07 | T7, splash do bitters, galheteiro sem rótulo | `input/frames_modelo/K07_modelo.png` |
| K08 / V08 | T8, close da panela, pimenta | `input/frames_modelo/K08_modelo.png` |
| K09 / V09 | T9, panela sobre a jarra com peneira | `input/frames_modelo/K09_modelo.png` |
| K10 / V10 | T10, copo na altura do peito | `input/frames_modelo/K10_modelo.png` |
| K11 / V11 | T11, copo, gesto com a mão | `input/frames_modelo/K11_modelo.png` |
| K12 / V12 | T12, CTA, copo na mão | `input/frames_modelo/K12_modelo.png` |
| K13 / V13 | T13, follow, plano mais fechado | `input/frames_modelo/K13_modelo.png` |

## 2. PROMPTS DE IMAGEM (um bloco por K)

### K01 · T1, gancho, comidas entrando no modelo transparente · anexar ÂNCORA + FRAME DO MODELO

```text
K01
{
  "format": "IMPORTANT: THIS IS IPHONE FOOTAGE. Vertical 9:16.",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "reference_use": "Use the first attached image only for Robert Alves's exact identity, wardrobe and own setting. Use the second attached image only as a composition reference for the camera position, framing and the action; do not copy its person, cap, clothes, pool, backyard, colors, the brand bottle or the white caption text.",
  "identity_main": "The exact fictional AI character Robert Alves: Black American man around forty-three, medium brown skin, lean healthy build, oval face, green-hazel eyes, black jaw-length locs, short full black beard and thin round tortoiseshell glasses.",
  "wardrobe": "Plain black polo shirt and black trousers.",
  "scene": "His own American timber cabin kitchen seen from a very low angle at counter level: the light butcher-block counter under the model, and behind him the pine ceiling beams, the large windows showing pine forest and the small American flag on a shelf.",
  "prop": "A large hollow clear transparent plastic anatomical teaching model shaped exactly like the complete human intestinal tract seen from the front, about as tall as a man's torso: a thick bulging outer tube with rounded pouch-like segments frames the left side, the top and the right side like an upside-down U; a dense tangle of narrower winding loops fills the whole middle; a short straight clear funnel neck opens at the top center; and a short straight clear tube drops out of the bottom center down to his light butcher-block counter. Every tube and loop is packed full of lumpy, knobby, dark brown and caramel-brown compacted matter with visible chunks and small air bubbles pressed against the clear plastic, so the whole shape reads brown, with only thin clear gaps between the loops. It is clearly a classroom teaching model made of clear plastic. With the other hand Robert Alves holds a small clear plastic cup of diced red and yellow apple tipped right above the funnel neck, close to the lens.",
  "posture": "Robert Alves crouches low behind the counter, NOT standing upright, so only his head, shoulders and arms rise above the model; one hand grips the left edge of the model close to the lens, looking large in frame.",
  "composition": "Extreme low-angle close-up taken with the phone's ultra-wide lens only a few inches from the model: the model is the hero and fills the lower sixty percent of the frame, almost touching the left and right edges, its bottom tube reaching the bottom edge, far closer to the camera than his face and much larger than his head, nothing else competing with it. He crouches right behind it, head and shoulders rising above the model in the upper part of the frame, face centered, leaning toward the lens. The counter around the model is empty. The background is reduced by framing, never by blur.",
  "camera": "phone lying almost flat on the counter, ultra-wide 0.5x lens a few inches from the model, pointing slightly upward, slight wide-angle perspective",
  "lighting": "Neutral overcast daylight from a window, the outside clearly visible through the window, never white or blown out, soft even light on the face and hands with no harsh shadows.",
  "state": "Start frame: the first apple cubes are just falling into the funnel neck; every loop is still packed brown. Robert Alves is caught mid-sentence, lips naturally parted, animated expression.",
  "realism": "Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday reality, background fully in focus, everything in sharp focus, no AI polish, no beauty smoothing.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no printed labels or lettering on any bottle, jar or package, no studio, no plastic-looking human skin, no extra fingers, no third hand, no supernatural lighting, no blur, no bokeh, no artificial lighting, no warm orange color cast, no yellow tint on the skin, no golden glow, no golden hour light, no sunset, no de-aging, no beauty smoothing, no visible phone, no HDR, no cinematic lighting, no second person in frame, no real human body, no simple zigzag tube, no single folded hose, no small toy-sized model, no model standing far from the camera, no items lying on the counter, no clean clear tube yet"
}
```

### K02 · T2, reveal, a bebida faz a massa sair por baixo · anexar ÂNCORA + FRAME DO MODELO

```text
K02
{
  "format": "IMPORTANT: THIS IS IPHONE FOOTAGE. Vertical 9:16.",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "reference_use": "Use the first attached image only for Robert Alves's exact identity, wardrobe and own setting. Use the second attached image only as a composition reference for the camera position, framing and the action; do not copy its person, cap, clothes, pool, backyard, colors, the brand bottle or the white caption text.",
  "identity_main": "The exact fictional AI character Robert Alves: Black American man around forty-three, medium brown skin, lean healthy build, oval face, green-hazel eyes, black jaw-length locs, short full black beard and thin round tortoiseshell glasses.",
  "wardrobe": "Plain black polo shirt and black trousers.",
  "scene": "His own American timber cabin kitchen seen from a very low angle at counter level: the light butcher-block counter under the model, and behind him the pine ceiling beams, the large windows showing pine forest and the small American flag on a shelf.",
  "prop": "A large hollow clear transparent plastic anatomical teaching model shaped exactly like the complete human intestinal tract seen from the front, about as tall as a man's torso: a thick bulging outer tube with rounded pouch-like segments frames the left side, the top and the right side like an upside-down U; a dense tangle of narrower winding loops fills the whole middle; a short straight clear funnel neck opens at the top center; and a short straight clear tube drops out of the bottom center down to his light butcher-block counter. Every tube and loop is packed full of lumpy, knobby, dark brown and caramel-brown compacted matter with visible chunks and small air bubbles pressed against the clear plastic, so the whole shape reads brown, with only thin clear gaps between the loops. It is clearly a classroom teaching model made of clear plastic. With the other hand Robert Alves holds a clear glass measuring jug of golden-amber lemon and turmeric tea tipped right above the funnel neck, the amber stream just starting to fall in.",
  "posture": "Robert Alves crouches low behind the counter, NOT standing upright, so only his head, shoulders and arms rise above the model; one hand grips the left edge of the model close to the lens, looking large in frame.",
  "composition": "Extreme low-angle close-up taken with the phone's ultra-wide lens only a few inches from the model: the model is the hero and fills the lower sixty percent of the frame, almost touching the left and right edges, its bottom tube reaching the bottom edge, far closer to the camera than his face and much larger than his head, nothing else competing with it. He crouches right behind it, head and shoulders rising above the model in the upper part of the frame, face centered, leaning toward the lens. The counter around the model is empty. The background is reduced by framing, never by blur.",
  "camera": "phone lying almost flat on the counter, ultra-wide 0.5x lens a few inches from the model, pointing slightly upward, slight wide-angle perspective",
  "lighting": "Neutral overcast daylight from a window, the outside clearly visible through the window, never white or blown out, soft even light on the face and hands with no harsh shadows.",
  "state": "Start frame: the amber stream is just entering the funnel neck; every loop is still packed brown and nothing has come out yet. Robert Alves is caught mid-sentence, lips naturally parted, animated expression.",
  "realism": "Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday reality, background fully in focus, everything in sharp focus, no AI polish, no beauty smoothing.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no printed labels or lettering on any bottle, jar or package, no studio, no plastic-looking human skin, no extra fingers, no third hand, no supernatural lighting, no blur, no bokeh, no artificial lighting, no warm orange color cast, no yellow tint on the skin, no golden glow, no golden hour light, no sunset, no de-aging, no beauty smoothing, no visible phone, no HDR, no cinematic lighting, no second person in frame, no real human body, no simple zigzag tube, no single folded hose, no small toy-sized model, no model standing far from the camera, no items lying on the counter, no clean clear tube yet"
}
```

### K03 · T3, limão da tábua para a panela · anexar ÂNCORA + FRAME DO MODELO

```text
K03
{
  "format": "IMPORTANT: THIS IS IPHONE FOOTAGE. Vertical 9:16.",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "reference_use": "Use the first attached image only for Robert Alves's exact identity, wardrobe and own setting. Use the second attached image only as a composition reference for the camera position, framing and the action; do not copy its person, cap, clothes, pool, backyard, colors, the brand bottle or the white caption text.",
  "identity_main": "The exact fictional AI character Robert Alves: Black American man around forty-three, medium brown skin, lean healthy build, oval face, green-hazel eyes, black jaw-length locs, short full black beard and thin round tortoiseshell glasses.",
  "wardrobe": "Plain black polo shirt and black trousers.",
  "scene": "His own American timber cabin kitchen with a light butcher-block counter in front of him, pine walls, large windows showing pine forest and a small American flag on a shelf.",
  "prop": "a clear glass cooking pot of boiling water on a small single-burner electric hot plate, standing on his light butcher-block counter, very close to the lens in the lower foreground. Robert Alves holds a wooden cutting board with a fresh lemon chopped into chunks tipped over the pot.",
  "posture": "Robert Alves crouches low behind the counter, NOT standing upright, so his head and shoulders rise just above the pot.",
  "composition": "The phone lens is only a few inches from the pot: the pot and the hot plate fill the lower forty percent of the frame, far closer to the camera than his face and larger than his head, nothing else competing with them. He crouches right behind the pot, head and shoulders above it in the upper half. Nothing else is on the counter. The background is reduced by framing, never by blur.",
  "camera": "phone resting on the counter at the height of the pot rim, wide lens a few inches from the pot, fixed",
  "lighting": "Neutral overcast daylight from a window, the outside clearly visible through the window, never white or blown out, soft even light on the face and hands with no harsh shadows.",
  "state": "Start frame: the first lemon chunks are sliding off the board toward the water, steam rising. Robert Alves is caught mid-sentence, lips naturally parted, animated expression.",
  "realism": "Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday reality, background fully in focus, everything in sharp focus, no AI polish, no beauty smoothing.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no printed labels or lettering on any bottle, jar or package, no studio, no plastic-looking human skin, no extra fingers, no third hand, no supernatural lighting, no blur, no bokeh, no artificial lighting, no warm orange color cast, no yellow tint on the skin, no golden glow, no golden hour light, no sunset, no de-aging, no beauty smoothing, no visible phone, no HDR, no cinematic lighting, no second person in frame, no teaching model in frame"
}
```

### K04 · T4, limão boiando, colher mexendo · anexar ÂNCORA + FRAME DO MODELO

```text
K04
{
  "format": "IMPORTANT: THIS IS IPHONE FOOTAGE. Vertical 9:16.",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "reference_use": "Use the first attached image only for Robert Alves's exact identity, wardrobe and own setting. Use the second attached image only as a composition reference for the camera position, framing and the action; do not copy its person, cap, clothes, pool, backyard, colors, the brand bottle or the white caption text.",
  "identity_main": "The exact fictional AI character Robert Alves: Black American man around forty-three, medium brown skin, lean healthy build, oval face, green-hazel eyes, black jaw-length locs, short full black beard and thin round tortoiseshell glasses.",
  "wardrobe": "Plain black polo shirt and black trousers.",
  "scene": "His own American timber cabin kitchen with a light butcher-block counter in front of him, pine walls, large windows showing pine forest and a small American flag on a shelf.",
  "prop": "a clear glass cooking pot of boiling water on a small single-burner electric hot plate, standing on his light butcher-block counter, very close to the lens in the lower foreground, lemon chunks floating in the water. Robert Alves holds a metal spoon inside the pot.",
  "posture": "Robert Alves crouches low behind the counter, NOT standing upright, so his head and shoulders rise just above the pot.",
  "composition": "The phone lens is only a few inches from the pot: the pot and the hot plate fill the lower forty percent of the frame, far closer to the camera than his face and larger than his head, nothing else competing with them. He crouches right behind the pot, head and shoulders above it in the upper half. Nothing else is on the counter. The background is reduced by framing, never by blur.",
  "camera": "phone resting on the counter at the height of the pot rim, wide lens a few inches from the pot, fixed",
  "lighting": "Neutral overcast daylight from a window, the outside clearly visible through the window, never white or blown out, soft even light on the face and hands with no harsh shadows.",
  "state": "Start frame: the lemon chunks bob in the boiling water, the spoon just starting to stir. Robert Alves is caught mid-sentence, lips naturally parted, animated expression.",
  "realism": "Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday reality, background fully in focus, everything in sharp focus, no AI polish, no beauty smoothing.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no printed labels or lettering on any bottle, jar or package, no studio, no plastic-looking human skin, no extra fingers, no third hand, no supernatural lighting, no blur, no bokeh, no artificial lighting, no warm orange color cast, no yellow tint on the skin, no golden glow, no golden hour light, no sunset, no de-aging, no beauty smoothing, no visible phone, no HDR, no cinematic lighting, no second person in frame, no teaching model in frame"
}
```

### K05 · T5, colher de chia · anexar ÂNCORA + FRAME DO MODELO

```text
K05
{
  "format": "IMPORTANT: THIS IS IPHONE FOOTAGE. Vertical 9:16.",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "reference_use": "Use the first attached image only for Robert Alves's exact identity, wardrobe and own setting. Use the second attached image only as a composition reference for the camera position, framing and the action; do not copy its person, cap, clothes, pool, backyard, colors, the brand bottle or the white caption text.",
  "identity_main": "The exact fictional AI character Robert Alves: Black American man around forty-three, medium brown skin, lean healthy build, oval face, green-hazel eyes, black jaw-length locs, short full black beard and thin round tortoiseshell glasses.",
  "wardrobe": "Plain black polo shirt and black trousers.",
  "scene": "His own American timber cabin kitchen with a light butcher-block counter in front of him, pine walls, large windows showing pine forest and a small American flag on a shelf.",
  "prop": "a clear glass cooking pot of boiling water on a small single-burner electric hot plate, standing on his light butcher-block counter, very close to the lens in the lower foreground, lemon chunks floating in the clear water. Robert Alves holds a teaspoon heaped with black chia seeds right above the water.",
  "posture": "Robert Alves crouches low behind the counter, NOT standing upright, so his head and shoulders rise just above the pot.",
  "composition": "The phone lens is only a few inches from the pot: the pot and the hot plate fill the lower forty percent of the frame, far closer to the camera than his face and larger than his head, nothing else competing with them. He crouches right behind the pot, head and shoulders above it in the upper half. Nothing else is on the counter. The background is reduced by framing, never by blur.",
  "camera": "phone resting on the counter at the height of the pot rim, wide lens a few inches from the pot, fixed",
  "lighting": "Neutral overcast daylight from a window, the outside clearly visible through the window, never white or blown out, soft even light on the face and hands with no harsh shadows.",
  "state": "Start frame: the spoon is tipping and the first chia seeds are falling. Robert Alves is caught mid-sentence, lips naturally parted, animated expression.",
  "realism": "Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday reality, background fully in focus, everything in sharp focus, no AI polish, no beauty smoothing.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no printed labels or lettering on any bottle, jar or package, no studio, no plastic-looking human skin, no extra fingers, no third hand, no supernatural lighting, no blur, no bokeh, no artificial lighting, no warm orange color cast, no yellow tint on the skin, no golden glow, no golden hour light, no sunset, no de-aging, no beauty smoothing, no visible phone, no HDR, no cinematic lighting, no second person in frame, no teaching model in frame"
}
```

### K06 · T6, cúrcuma, a água amarelando · anexar ÂNCORA + FRAME DO MODELO

```text
K06
{
  "format": "IMPORTANT: THIS IS IPHONE FOOTAGE. Vertical 9:16.",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "reference_use": "Use the first attached image only for Robert Alves's exact identity, wardrobe and own setting. Use the second attached image only as a composition reference for the camera position, framing and the action; do not copy its person, cap, clothes, pool, backyard, colors, the brand bottle or the white caption text.",
  "identity_main": "The exact fictional AI character Robert Alves: Black American man around forty-three, medium brown skin, lean healthy build, oval face, green-hazel eyes, black jaw-length locs, short full black beard and thin round tortoiseshell glasses.",
  "wardrobe": "Plain black polo shirt and black trousers.",
  "scene": "His own American timber cabin kitchen with a light butcher-block counter in front of him, pine walls, large windows showing pine forest and a small American flag on a shelf.",
  "prop": "a clear glass cooking pot of boiling water on a small single-burner electric hot plate, standing on his light butcher-block counter, very close to the lens in the lower foreground, lemon chunks and chia seeds in the water. Robert Alves tips a small plain glass jar of bright orange ground turmeric, with no label, over the pot.",
  "posture": "Robert Alves crouches low behind the counter, NOT standing upright, so his head and shoulders rise just above the pot.",
  "composition": "The phone lens is only a few inches from the pot: the pot and the hot plate fill the lower forty percent of the frame, far closer to the camera than his face and larger than his head, nothing else competing with them. He crouches right behind the pot, head and shoulders above it in the upper half. Nothing else is on the counter. The background is reduced by framing, never by blur.",
  "camera": "phone resting on the counter at the height of the pot rim, wide lens a few inches from the pot, fixed",
  "lighting": "Neutral overcast daylight from a window, the outside clearly visible through the window, never white or blown out, soft even light on the face and hands with no harsh shadows.",
  "state": "Start frame: the first turmeric powder hits the water and a yellow cloud starts to spread. Robert Alves is caught mid-sentence, lips naturally parted, animated expression.",
  "realism": "Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday reality, background fully in focus, everything in sharp focus, no AI polish, no beauty smoothing.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no printed labels or lettering on any bottle, jar or package, no studio, no plastic-looking human skin, no extra fingers, no third hand, no supernatural lighting, no blur, no bokeh, no artificial lighting, no warm orange color cast, no yellow tint on the skin, no golden glow, no golden hour light, no sunset, no de-aging, no beauty smoothing, no visible phone, no HDR, no cinematic lighting, no second person in frame, no teaching model in frame"
}
```

### K07 · T7, splash do bitters, galheteiro sem rótulo · anexar ÂNCORA + FRAME DO MODELO

```text
K07
{
  "format": "IMPORTANT: THIS IS IPHONE FOOTAGE. Vertical 9:16.",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "reference_use": "Use the first attached image only for Robert Alves's exact identity, wardrobe and own setting. Use the second attached image only as a composition reference for the camera position, framing and the action; do not copy its person, cap, clothes, pool, backyard, colors, the brand bottle or the white caption text.",
  "identity_main": "The exact fictional AI character Robert Alves: Black American man around forty-three, medium brown skin, lean healthy build, oval face, green-hazel eyes, black jaw-length locs, short full black beard and thin round tortoiseshell glasses.",
  "wardrobe": "Plain black polo shirt and black trousers.",
  "scene": "His own American timber cabin kitchen with a light butcher-block counter in front of him, pine walls, large windows showing pine forest and a small American flag on a shelf.",
  "prop": "a clear glass cooking pot of boiling water on a small single-burner electric hot plate, standing on his light butcher-block counter, very close to the lens in the lower foreground, the water now bright yellow with lemon chunks and chia seeds. Robert Alves tips a small glass kitchen cruet of dark amber herbal bitters, with no label, over the pot.",
  "posture": "Robert Alves crouches low behind the counter, NOT standing upright, so his head and shoulders rise just above the pot.",
  "composition": "The phone lens is only a few inches from the pot: the pot and the hot plate fill the lower forty percent of the frame, far closer to the camera than his face and larger than his head, nothing else competing with them. He crouches right behind the pot, head and shoulders above it in the upper half. Nothing else is on the counter. The background is reduced by framing, never by blur.",
  "camera": "phone resting on the counter at the height of the pot rim, wide lens a few inches from the pot, fixed",
  "lighting": "Neutral overcast daylight from a window, the outside clearly visible through the window, never white or blown out, soft even light on the face and hands with no harsh shadows.",
  "state": "Start frame: a small splash of dark liquid is leaving the spout of the cruet. Robert Alves is caught mid-sentence, lips naturally parted, animated expression.",
  "realism": "Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday reality, background fully in focus, everything in sharp focus, no AI polish, no beauty smoothing.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no printed labels or lettering on any bottle, jar or package, no studio, no plastic-looking human skin, no extra fingers, no third hand, no supernatural lighting, no blur, no bokeh, no artificial lighting, no warm orange color cast, no yellow tint on the skin, no golden glow, no golden hour light, no sunset, no de-aging, no beauty smoothing, no visible phone, no HDR, no cinematic lighting, no second person in frame, no teaching model in frame"
}
```

### K08 · T8, close da panela, pimenta · anexar ÂNCORA + FRAME DO MODELO

```text
K08
{
  "format": "IMPORTANT: THIS IS IPHONE FOOTAGE. Vertical 9:16.",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "reference_use": "Use the first attached image only for Robert Alves's exact identity, wardrobe and own setting. Use the second attached image only as a composition reference for the camera position, framing and the action; do not copy its person, cap, clothes, pool, backyard, colors, the brand bottle or the white caption text.",
  "identity_main": "The exact fictional AI character Robert Alves: Black American man around forty-three, medium brown skin, lean healthy build, oval face, green-hazel eyes, black jaw-length locs, short full black beard and thin round tortoiseshell glasses.",
  "wardrobe": "Plain black polo shirt and black trousers.",
  "scene": "Close view of the pot on his light butcher-block counter; at the top edge of the frame, part of his own kitchen with the small American flag, discreet but visible and in focus.",
  "prop": "The clear glass pot of bright yellow boiling tea with lemon chunks, black chia seeds and a few black pepper flecks floating. Robert Alves's fingers release a pinch of ground black pepper above the water.",
  "posture": "Only his medium brown hands and bare forearms enter from the top of the frame.",
  "composition": "The phone lens is only a few inches from the pot: it fills the frame edge to edge, very large and close. The background is reduced by framing, never by blur.",
  "camera": "phone with a wide lens a few inches from the side of the pot, just above the rim",
  "lighting": "Neutral overcast daylight from a window, the outside clearly visible through the window, never white or blown out, soft even light on the face and hands with no harsh shadows.",
  "state": "Start frame: the pinch of black pepper is falling onto the yellow water.",
  "realism": "Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday reality, background fully in focus, everything in sharp focus, no AI polish, no beauty smoothing.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no printed labels or lettering on any bottle, jar or package, no studio, no plastic-looking human skin, no extra fingers, no third hand, no supernatural lighting, no blur, no bokeh, no artificial lighting, no warm orange color cast, no yellow tint on the skin, no golden glow, no golden hour light, no sunset, no de-aging, no beauty smoothing, no visible phone, no HDR, no cinematic lighting, no second person in frame, no teaching model in frame, no face in frame"
}
```

### K09 · T9, panela sobre a jarra com peneira · anexar ÂNCORA + FRAME DO MODELO

```text
K09
{
  "format": "IMPORTANT: THIS IS IPHONE FOOTAGE. Vertical 9:16.",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "reference_use": "Use the first attached image only for Robert Alves's exact identity, wardrobe and own setting. Use the second attached image only as a composition reference for the camera position, framing and the action; do not copy its person, cap, clothes, pool, backyard, colors, the brand bottle or the white caption text.",
  "identity_main": "The exact fictional AI character Robert Alves: Black American man around forty-three, medium brown skin, lean healthy build, oval face, green-hazel eyes, black jaw-length locs, short full black beard and thin round tortoiseshell glasses.",
  "wardrobe": "Plain black polo shirt and black trousers.",
  "scene": "His own American timber cabin kitchen with a light butcher-block counter in front of him, pine walls, large windows showing pine forest and a small American flag on a shelf.",
  "prop": "Robert Alves lifts the clear glass pot of yellow tea with lemon chunks by both handles, right above a clear glass pitcher with a fine metal mesh strainer on top, standing on his light butcher-block counter next to the small electric hot plate.",
  "posture": "Robert Alves stands behind the counter holding the pot with both hands.",
  "composition": "The phone lens is only a few inches from the pot and the pitcher: they fill the lower half of the frame, large and close, his chest and face at the top edge of the frame, partly cut. Nothing else is on the counter. The background is reduced by framing, never by blur.",
  "camera": "phone resting on the counter at counter height, wide lens a few inches from the pitcher, fixed",
  "lighting": "Neutral overcast daylight from a window, the outside clearly visible through the window, never white or blown out, soft even light on the face and hands with no harsh shadows.",
  "state": "Start frame: the pot is lifted just above the strainer, about to tip. Robert Alves is caught mid-sentence, lips naturally parted, animated expression.",
  "realism": "Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday reality, background fully in focus, everything in sharp focus, no AI polish, no beauty smoothing.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no printed labels or lettering on any bottle, jar or package, no studio, no plastic-looking human skin, no extra fingers, no third hand, no supernatural lighting, no blur, no bokeh, no artificial lighting, no warm orange color cast, no yellow tint on the skin, no golden glow, no golden hour light, no sunset, no de-aging, no beauty smoothing, no visible phone, no HDR, no cinematic lighting, no second person in frame, no teaching model in frame"
}
```

### K10 · T10, copo na altura do peito · anexar ÂNCORA + FRAME DO MODELO

```text
K10
{
  "format": "IMPORTANT: THIS IS IPHONE FOOTAGE. Vertical 9:16.",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "reference_use": "Use the first attached image only for Robert Alves's exact identity, wardrobe and own setting. Use the second attached image only as a composition reference for the camera position, framing and the action; do not copy its person, cap, clothes, pool, backyard, colors, the brand bottle or the white caption text.",
  "identity_main": "The exact fictional AI character Robert Alves: Black American man around forty-three, medium brown skin, lean healthy build, oval face, green-hazel eyes, black jaw-length locs, short full black beard and thin round tortoiseshell glasses.",
  "wardrobe": "Plain black polo shirt and black trousers.",
  "scene": "His own American timber cabin kitchen with a light butcher-block counter in front of him, pine walls, large windows showing pine forest and a small American flag on a shelf.",
  "prop": "Robert Alves holds a tall clear glass full of warm golden-amber lemon and turmeric tea with a few chia seeds floating in it at chest height. No bottle anywhere in frame.",
  "posture": "Robert Alves is standing behind the counter, leaning slightly toward the camera.",
  "composition": "The phone lens is only a few inches from the glass of tea: it sits in the lower foreground and takes up about a third of the frame, closer to the camera than his face, nothing else competing with it. He leans toward the lens right behind it, from the chest up, face clear in the upper half. The background is reduced by framing, never by blur.",
  "camera": "phone resting on the counter at chest height, wide lens a few inches from the glass, fixed",
  "lighting": "Neutral overcast daylight from a window, the outside clearly visible through the window, never white or blown out, soft even light on the face and hands with no harsh shadows.",
  "state": "Start frame: Robert Alves looks into the lens holding the glass, caught mid-sentence, lips naturally parted, animated expression.",
  "realism": "Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday reality, background fully in focus, everything in sharp focus, no AI polish, no beauty smoothing.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no printed labels or lettering on any bottle, jar or package, no studio, no plastic-looking human skin, no extra fingers, no third hand, no supernatural lighting, no blur, no bokeh, no artificial lighting, no warm orange color cast, no yellow tint on the skin, no golden glow, no golden hour light, no sunset, no de-aging, no beauty smoothing, no visible phone, no HDR, no cinematic lighting, no second person in frame, no teaching model in frame"
}
```

### K11 · T11, copo, gesto com a mão · anexar ÂNCORA + FRAME DO MODELO

```text
K11
{
  "format": "IMPORTANT: THIS IS IPHONE FOOTAGE. Vertical 9:16.",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "reference_use": "Use the first attached image only for Robert Alves's exact identity, wardrobe and own setting. Use the second attached image only as a composition reference for the camera position, framing and the action; do not copy its person, cap, clothes, pool, backyard, colors, the brand bottle or the white caption text.",
  "identity_main": "The exact fictional AI character Robert Alves: Black American man around forty-three, medium brown skin, lean healthy build, oval face, green-hazel eyes, black jaw-length locs, short full black beard and thin round tortoiseshell glasses.",
  "wardrobe": "Plain black polo shirt and black trousers.",
  "scene": "His own American timber cabin kitchen with a light butcher-block counter in front of him, pine walls, large windows showing pine forest and a small American flag on a shelf.",
  "prop": "Robert Alves holds a tall clear glass full of warm golden-amber lemon and turmeric tea with a few chia seeds floating in it at chest height in one hand, the other hand open in a natural gesture. No bottle anywhere in frame.",
  "posture": "Robert Alves is standing behind the counter, leaning slightly toward the camera.",
  "composition": "The phone lens is only a few inches from the glass of tea: it sits in the lower foreground and takes up about a third of the frame, closer to the camera than his face, nothing else competing with it. He leans toward the lens right behind it, from the chest up, face clear in the upper half. The background is reduced by framing, never by blur.",
  "camera": "phone resting on the counter at chest height, wide lens a few inches from the glass, fixed",
  "lighting": "Neutral overcast daylight from a window, the outside clearly visible through the window, never white or blown out, soft even light on the face and hands with no harsh shadows.",
  "state": "Start frame: Robert Alves looks into the lens mid-gesture, caught mid-sentence, lips naturally parted, animated expression.",
  "realism": "Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday reality, background fully in focus, everything in sharp focus, no AI polish, no beauty smoothing.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no printed labels or lettering on any bottle, jar or package, no studio, no plastic-looking human skin, no extra fingers, no third hand, no supernatural lighting, no blur, no bokeh, no artificial lighting, no warm orange color cast, no yellow tint on the skin, no golden glow, no golden hour light, no sunset, no de-aging, no beauty smoothing, no visible phone, no HDR, no cinematic lighting, no second person in frame, no teaching model in frame"
}
```

### K12 · T12, CTA, copo na mão · anexar ÂNCORA + FRAME DO MODELO

```text
K12
{
  "format": "IMPORTANT: THIS IS IPHONE FOOTAGE. Vertical 9:16.",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "reference_use": "Use the first attached image only for Robert Alves's exact identity, wardrobe and own setting. Use the second attached image only as a composition reference for the camera position, framing and the action; do not copy its person, cap, clothes, pool, backyard, colors, the brand bottle or the white caption text.",
  "identity_main": "The exact fictional AI character Robert Alves: Black American man around forty-three, medium brown skin, lean healthy build, oval face, green-hazel eyes, black jaw-length locs, short full black beard and thin round tortoiseshell glasses.",
  "wardrobe": "Plain black polo shirt and black trousers.",
  "scene": "His own American timber cabin kitchen with a light butcher-block counter in front of him, pine walls, large windows showing pine forest and a small American flag on a shelf.",
  "prop": "Robert Alves holds a tall clear glass full of warm golden-amber lemon and turmeric tea with a few chia seeds floating in it in one hand, leaning a little toward the lens. No bottle anywhere in frame.",
  "posture": "Robert Alves is standing behind the counter, leaning slightly toward the camera.",
  "composition": "The phone lens is only a few inches from the glass of tea: it sits in the lower foreground and takes up about a third of the frame, closer to the camera than his face, nothing else competing with it. He leans toward the lens right behind it, from the chest up, face clear in the upper half. The background is reduced by framing, never by blur.",
  "camera": "phone resting on the counter at chest height, wide lens a few inches from the glass, fixed",
  "lighting": "Neutral overcast daylight from a window, the outside clearly visible through the window, never white or blown out, soft even light on the face and hands with no harsh shadows.",
  "state": "Start frame: Robert Alves smiles at the lens, caught mid-sentence, lips naturally parted, animated expression.",
  "realism": "Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday reality, background fully in focus, everything in sharp focus, no AI polish, no beauty smoothing.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no printed labels or lettering on any bottle, jar or package, no studio, no plastic-looking human skin, no extra fingers, no third hand, no supernatural lighting, no blur, no bokeh, no artificial lighting, no warm orange color cast, no yellow tint on the skin, no golden glow, no golden hour light, no sunset, no de-aging, no beauty smoothing, no visible phone, no HDR, no cinematic lighting, no second person in frame, no teaching model in frame"
}
```

### K13 · T13, follow, plano mais fechado · anexar ÂNCORA + FRAME DO MODELO

```text
K13
{
  "format": "IMPORTANT: THIS IS IPHONE FOOTAGE. Vertical 9:16.",
  "fiction_note": "This is a fictional AI-generated character, no real person is depicted.",
  "reference_use": "Use the first attached image only for Robert Alves's exact identity, wardrobe and own setting. Use the second attached image only as a composition reference for the camera position, framing and the action; do not copy its person, cap, clothes, pool, backyard, colors, the brand bottle or the white caption text.",
  "identity_main": "The exact fictional AI character Robert Alves: Black American man around forty-three, medium brown skin, lean healthy build, oval face, green-hazel eyes, black jaw-length locs, short full black beard and thin round tortoiseshell glasses.",
  "wardrobe": "Plain black polo shirt and black trousers.",
  "scene": "His own American timber cabin kitchen with a light butcher-block counter in front of him, pine walls, large windows showing pine forest and a small American flag on a shelf.",
  "prop": "Robert Alves holds a tall clear glass full of warm golden-amber lemon and turmeric tea with a few chia seeds floating in it low in one hand. No bottle anywhere in frame.",
  "posture": "Robert Alves is standing behind the counter, leaning slightly toward the camera.",
  "composition": "The tightest shot of the video: his face and upper chest fill the upper two thirds of the frame, close to the lens, and the glass sits at the bottom edge a few inches from the lens. The background is reduced by framing, never by blur.",
  "camera": "phone resting on the counter at chest height, wide lens a few inches from the glass, fixed",
  "lighting": "Neutral overcast daylight from a window, the outside clearly visible through the window, never white or blown out, soft even light on the face and hands with no harsh shadows.",
  "state": "Start frame: Robert Alves looks straight into the lens, serious and close, caught mid-sentence, lips naturally parted, animated expression.",
  "realism": "Real skin with visible pores, irregular texture, fine lines and soft asymmetry, hair in uneven natural clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday reality, background fully in focus, everything in sharp focus, no AI polish, no beauty smoothing.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no printed labels or lettering on any bottle, jar or package, no studio, no plastic-looking human skin, no extra fingers, no third hand, no supernatural lighting, no blur, no bokeh, no artificial lighting, no warm orange color cast, no yellow tint on the skin, no golden glow, no golden hour light, no sunset, no de-aging, no beauty smoothing, no visible phone, no HDR, no cinematic lighting, no second person in frame, no teaching model in frame"
}
```

## 3. PROMPTS DE VÍDEO (um bloco por V)

### V01 · T1 · frame inicial = a imagem que você deixou no K01

```text
V01
o avatar Robert Alves, homem, fala em inglês com sotaque americano de um homem negro americano, voz média e calma de um homem de quarenta e poucos anos, entonação provocadora e convicta, desafiando quem assiste, voz autêntica, como se exigisse ser ouvido, a seguinte frase: "You can eat apples, chicken, spinach, yogurt, anything, and it will not clear what has been sitting inside you for years."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Robert Alves segura o modelo transparente com uma mão e, conforme nomeia cada comida, joga pelo gargalo os cubos de maçã e depois traz de fora do quadro, uma de cada vez, a coxa de frango crua, o maço de espinafre e o copinho de iogurte branco, que ele despeja; a massa marrom dentro das alças não se mexe.

câmera: fixa, rente à bancada, grande angular, leve handheld

som ambiente: cozinha de cabana tranquila, som das comidas caindo no plástico, sem música
```

### V02 · T2 · frame inicial = a imagem que você deixou no K02

```text
V02
o avatar Robert Alves, homem, fala em inglês com sotaque americano de um homem negro americano, voz média e calma de um homem de quarenta e poucos anos, entonação confiante, com um meio sorriso, voz autêntica, como se exigisse ser ouvido, a seguinte frase: "Let me show you what actually works."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Robert Alves despeja a jarrinha da bebida âmbar pelo gargalo; a massa marrom começa a descer pelas alças e escorre para fora pela ponta de baixo, espalhando na bancada, e as alças de cima vão ficando transparentes. Ele diz a frase em ritmo natural logo no começo e continua a ação em silêncio até o fim.

câmera: fixa, rente à bancada, grande angular, leve handheld

som ambiente: cozinha de cabana tranquila, som da bebida caindo e da massa escorrendo, sem música
```

### V03 · T3 · frame inicial = a imagem que você deixou no K03

```text
V03
o avatar Robert Alves, homem, fala em inglês com sotaque americano de um homem negro americano, voz média e calma de um homem de quarenta e poucos anos, entonação calma e didática, voz autêntica, como se exigisse ser ouvido, a seguinte frase: "Get a pot of water going, chop up a fresh lemon,"

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Robert Alves inclina a tábua e os pedaços de limão caem na panela de água fervendo. Ele diz a frase em ritmo natural logo no começo e continua a ação em silêncio até o fim.

câmera: fixa

som ambiente: cozinha de cabana tranquila, água fervendo, sem música
```

### V04 · T4 · frame inicial = a imagem que você deixou no K04

```text
V04
o avatar Robert Alves, homem, fala em inglês com sotaque americano de um homem negro americano, voz média e calma de um homem de quarenta e poucos anos, entonação calma e didática, voz autêntica, como se exigisse ser ouvido, a seguinte frase: "and drop it in the boiling water."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Os pedaços de limão boiam na água fervendo e Robert Alves mexe com a colher. Ele diz a frase em ritmo natural logo no começo e continua a ação em silêncio até o fim.

câmera: fixa

som ambiente: cozinha de cabana tranquila, água fervendo, sem música
```

### V05 · T5 · frame inicial = a imagem que você deixou no K05

```text
V05
o avatar Robert Alves, homem, fala em inglês com sotaque americano de um homem negro americano, voz média e calma de um homem de quarenta e poucos anos, entonação calma e didática, voz autêntica, como se exigisse ser ouvido, a seguinte frase: "Add one teaspoon of chia seed,"

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Robert Alves vira a colher de chia na água e as sementes se espalham. Ele diz a frase em ritmo natural logo no começo e continua a ação em silêncio até o fim.

câmera: fixa

som ambiente: cozinha de cabana tranquila, água fervendo, sem música
```

### V06 · T6 · frame inicial = a imagem que você deixou no K06

```text
V06
o avatar Robert Alves, homem, fala em inglês com sotaque americano de um homem negro americano, voz média e calma de um homem de quarenta e poucos anos, entonação calma e didática, voz autêntica, como se exigisse ser ouvido, a seguinte frase: "a teaspoon of turmeric,"

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Robert Alves inclina o pote de cúrcuma sobre a panela e a água vai ficando amarela. Ele diz a frase em ritmo natural logo no começo e continua a ação em silêncio até o fim.

câmera: fixa

som ambiente: cozinha de cabana tranquila, água fervendo, sem música
```

### V07 · T7 · frame inicial = a imagem que você deixou no K07

```text
V07
o avatar Robert Alves, homem, fala em inglês com sotaque americano de um homem negro americano, voz média e calma de um homem de quarenta e poucos anos, entonação calma e didática, voz autêntica, como se exigisse ser ouvido, a seguinte frase: "a splash or two of soursop bitters,"

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Robert Alves vira o pequeno galheteiro de vidro âmbar e cai um pouco de líquido na panela. Ele diz a frase em ritmo natural logo no começo e continua a ação em silêncio até o fim.

câmera: fixa

som ambiente: cozinha de cabana tranquila, água fervendo, sem música
```

### V08 · T8 · frame inicial = a imagem que você deixou no K08

```text
V08
o avatar Robert Alves, homem, fala em inglês com sotaque americano de um homem negro americano, voz média e calma de um homem de quarenta e poucos anos, entonação calma e didática, voz autêntica, como se exigisse ser ouvido, a seguinte frase: "and finish it with a pinch of black pepper."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: A mão de Robert Alves solta uma pitada de pimenta-do-reino sobre a água amarela, com limão e chia boiando. Ele diz a frase em ritmo natural logo no começo e continua a ação em silêncio até o fim.

câmera: fixa, bem perto da panela

som ambiente: cozinha de cabana tranquila, água fervendo, sem música
```

### V09 · T9 · frame inicial = a imagem que você deixou no K09

```text
V09
o avatar Robert Alves, homem, fala em inglês com sotaque americano de um homem negro americano, voz média e calma de um homem de quarenta e poucos anos, entonação calma e didática, voz autêntica, como se exigisse ser ouvido, a seguinte frase: "Let it boil for ten minutes, then strain it out."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Robert Alves levanta a panela pelas alças sobre a jarra com peneira. Ele diz a frase em ritmo natural logo no começo e continua a ação em silêncio até o fim.

câmera: fixa

som ambiente: cozinha de cabana tranquila, água fervendo, sem música
```

### V10 · T10 · frame inicial = a imagem que você deixou no K10

```text
V10
o avatar Robert Alves, homem, fala em inglês com sotaque americano de um homem negro americano, voz média e calma de um homem de quarenta e poucos anos, entonação animada e convicta, voz autêntica, como se exigisse ser ouvido, a seguinte frase: "This wakes your entire system up. Your gut is cleaned right out, and your body feels lighter and happier."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Robert Alves segura o copo da bebida na altura do peito e fala para a câmera, com pequenos movimentos naturais.

câmera: fixa

som ambiente: cozinha de cabana tranquila, sem música
```

### V11 · T11 · frame inicial = a imagem que você deixou no K11

```text
V11
o avatar Robert Alves, homem, fala em inglês com sotaque americano de um homem negro americano, voz média e calma de um homem de quarenta e poucos anos, entonação calorosa e segura, voz autêntica, como se exigisse ser ouvido, a seguinte frase: "My clients who add this come back telling me their digestion finally feels normal for the first time in years."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Robert Alves segura o copo com uma mão e gesticula com a outra, falando para a câmera.

câmera: fixa

som ambiente: cozinha de cabana tranquila, sem música
```

### V12 · T12 · frame inicial = a imagem que você deixou no K12

```text
V12
o avatar Robert Alves, homem, fala em inglês com sotaque americano de um homem negro americano, voz média e calma de um homem de quarenta e poucos anos, entonação animada e convidativa, sorrindo, voz autêntica, como se exigisse ser ouvido, a seguinte frase: "Comment yes, and I'll send you the exact morning recipe I give to my clients."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Robert Alves segura o copo com uma mão, se inclina um pouco para a câmera e fala direto com ela, sorrindo.

câmera: fixa

som ambiente: cozinha de cabana tranquila, sem música
```

### V13 · T13 · frame inicial = a imagem que você deixou no K13

```text
V13
o avatar Robert Alves, homem, fala em inglês com sotaque americano de um homem negro americano, voz média e calma de um homem de quarenta e poucos anos, entonação firme e próxima, olhando direto na lente, voz autêntica, como se exigisse ser ouvido, a seguinte frase: "But you must be following me so I can message you."

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: Robert Alves olha direto para a lente, sério e próximo, segurando o copo mais abaixo. Ele diz a frase em ritmo natural logo no começo e continua a ação em silêncio até o fim.

câmera: fixa

som ambiente: cozinha de cabana tranquila, sem música
```

## 4. Montagem no CapCut

1. Clipes numerados na ordem: V01 a V13.
2. Cortar cada clipe no tempo da cena do modelo: V01 0,0 a 8,1 s; V02 8,1 a 11,2 s; V03 11,2 a 15,0 s; V04 15,0 a 16,7 s; V05 16,7 a 18,0 s; V06 18,0 a 20,2 s; V07 20,2 a 21,9 s; V08 21,9 a 23,4 s; V09 23,4 a 24,8 s; V10 24,8 a 29,8 s; V11 29,8 a 34,8 s; V12 ~5 s (o bloco do produto do modelo saiu); V13 51,4 a 53,7 s do modelo, ~2,3 s.
3. Zero tempo morto: todo clipe começa já falando. Isolate Voice / Keep Vocal no áudio.
4. Cenas curtas (V02 a V09 e V13): a fala vem no começo do clipe; cortar logo depois da última palavra, no tempo da cena.
5. No V01 e no V02, os zooms de corte do modelo (na coxa de frango, no espinafre, na massa saindo) saem do mesmo clipe: recortar e aproximar na edição.
6. Legenda palavra a palavra, branca, no meio do quadro, com a palavra-chave em serifa itálica, igual ao modelo.
7. Sem Voice Changer: a voz vem do prompt de cada V.
8. Música só depois do gancho (a partir do V03), nunca no pré-gancho, entre -19 e -20 dB, fora da biblioteca do TikTok.
9. Rótulo pequeno `AI-generated` num canto do vídeo.

## 5. Transcrição final por take

| Take | English | Português |
|---|---|---|
| T1 | You can eat apples, chicken, spinach, yogurt, anything, and it will not clear what has been sitting inside you for years. | Você pode comer maçã, frango, espinafre, iogurte, qualquer coisa, e isso não vai limpar o que está parado dentro de você há anos. |
| T2 | Let me show you what actually works. | Deixa eu te mostrar o que realmente funciona. |
| T3 | Get a pot of water going, chop up a fresh lemon, | Coloca uma panela de água no fogo, pica um limão fresco, |
| T4 | and drop it in the boiling water. | e joga na água fervendo. |
| T5 | Add one teaspoon of chia seed, | Coloca uma colher de chá de chia, |
| T6 | a teaspoon of turmeric, | uma colher de chá de cúrcuma, |
| T7 | a splash or two of soursop bitters, | uma ou duas gotas de bitter de graviola, |
| T8 | and finish it with a pinch of black pepper. | e finaliza com uma pitada de pimenta-do-reino. |
| T9 | Let it boil for ten minutes, then strain it out. | Deixa ferver por dez minutos, depois coa. |
| T10 | This wakes your entire system up. Your gut is cleaned right out, and your body feels lighter and happier. | Isso acorda o seu sistema inteiro. Seu intestino fica limpo de verdade, e seu corpo se sente mais leve e mais feliz. |
| T11 | My clients who add this come back telling me their digestion finally feels normal for the first time in years. | Meus clientes que incluem isso voltam me dizendo que a digestão finalmente parece normal pela primeira vez em anos. |
| T12 | Comment yes, and I'll send you the exact morning recipe I give to my clients. | Comenta yes, e eu te mando a receita exata da manhã que eu passo para os meus clientes. |
| T13 | But you must be following me so I can message you. | Mas você precisa estar me seguindo para eu conseguir te mandar mensagem. |

## 6. Roteiro final em inglês

1. You can eat apples, chicken, spinach, yogurt, anything, and it will not clear what has been sitting inside you for years.
2. Let me show you what actually works.
3. Get a pot of water going, chop up a fresh lemon,
4. and drop it in the boiling water.
5. Add one teaspoon of chia seed,
6. a teaspoon of turmeric,
7. a splash or two of soursop bitters,
8. and finish it with a pinch of black pepper.
9. Let it boil for ten minutes, then strain it out.
10. This wakes your entire system up. Your gut is cleaned right out, and your body feels lighter and happier.
11. My clients who add this come back telling me their digestion finally feels normal for the first time in years.
12. Comment yes, and I'll send you the exact morning recipe I give to my clients.
13. But you must be following me so I can message you.

You can eat apples, chicken, spinach, yogurt, anything, and it will not clear what has been sitting inside you for years. Let me show you what actually works. Get a pot of water going, chop up a fresh lemon, and drop it in the boiling water. Add one teaspoon of chia seed, a teaspoon of turmeric, a splash or two of soursop bitters, and finish it with a pinch of black pepper. Let it boil for ten minutes, then strain it out. This wakes your entire system up. Your gut is cleaned right out, and your body feels lighter and happier. My clients who add this come back telling me their digestion finally feels normal for the first time in years. Comment yes, and I'll send you the exact morning recipe I give to my clients. But you must be following me so I can message you.
