# Entrega · Conta 4 · HOOK 4 · DOCE: chocolate chip cookie

Checklist de envio: 32/32 aprovados (N/A: A1, A9, A10, B9, C4, C5, C7, E1, E2)

## INSTRUÇÕES PARA A MEMÓRIA DO AGENTE · GOOGLE FLOW AI

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
| Imagens por K | 4, com selecao manual | 1 imagem final |
| Relacao K/V | Mapa explicito recebido com o pacote; um K pode alimentar varios V | Maior K menor ou igual ao numero de V |
| Video | Veo 3.1 Lite | Veo 3.1 Lite |
| Prioridade | Lower Priority | Lower Priority |
| Duracao por clipe | 8 segundos | 8 segundos |
| Variacoes por V | 3 | 1 |
| Anexo do video | INITIAL FRAME | INITIAL FRAME |
| Lote de video | Fechado, no maximo 7 codigos V | Fechado, no maximo 7 codigos V |

Os valores Auraly reproduzem as travas de WORKFLOW_AURALY.md. Nunca transportar as configuracoes
classicas para Auraly. Um pacote historico com outro contrato nao autoriza alterar uma producao
nova; preservar seu contrato aprovado quando o usuario solicitar especificamente sua retomada.

### AURALY, anchor e cenario por gancho (Luigi, 2026-09-14; anchor revista em 2026-09-22)

Roster Auraly: Walt Hensley, Darlene Pruitt e Lorraine Vance. A referencia de cada um e a anchor
em cena real (imagem de teste aprovada), anexada em todo K. Nao existe fingerprint. Quando o K
mantem o cenario da anchor, o texto do K descreve esse cenario. Quando o K pede cenario ou roupa
novos, o texto manda usar a anchor so para a identidade; siga o texto e ignore roupa, fundo e props
da anchor.

Cada gancho escolhido passa a ter CENARIO PROPRIO do T1 ao CTA (K de hook + K de corpo + K de CTA
por cenario), nunca mais um corpo compartilhado pela fila inteira. O angulo de camera serve a
acao estrutural preservada: pode ser exotico quando aumenta a anomalia, mas pode se repetir entre
variacoes para preservar composicao e timing. Mudar o angulo conta como a unica variavel dessa
variacao. Roupa livre por cenario, sem obrigacao de repetir a roupa da anchor.

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

Usar Nano Banana 2, formato 9:16 e a anchor ativa. Colar cada prompt literalmente e gerar a
quantidade do perfil. Rotular os resultados com avatar, codigo e numero da variacao.

No Auraly, apresentar quatro candidatas por K e esperar o operador escolher uma por codigo.
Mesmo que os V ja tenham chegado no mesmo pacote textual, nao selecionar automaticamente nem
avancar para video sem selecao. No classico, uma imagem
final por K; ainda assim esperar o pacote de video antes de executar essa fase.

### 🔴 Reconhecer prompt de IMAGEM (K) contra prompt de VIDEO (V), sem ambiguidade (v8)

Falha real registrada em producao: apos gerar as imagens corretamente, inclusive editando um K
a partir de outro ja aprovado, o executor avancou para a etapa de video usando a imagem gerada
como INITIAL FRAME (certo) mas colou o PROPRIO PROMPT DE IMAGEM no campo de texto do video, em
vez do prompt V correspondente. Isso nunca pode se repetir. Regras obrigatorias:

1. **Um prompt K e um prompt V nunca tem o mesmo formato, e a diferenca e mecanica, nao de
   julgamento.** Um prompt K e um UNICO paragrafo denso em ingles descrevendo uma imagem parada:
   comeca tipicamente com `IMPORTANT: THIS IS IPHONE FOOTAGE` (geracao do zero) ou `Edit the
   attached image` (edicao). NUNCA contem as palavras `o avatar fala`, `câmera:` ou `som
   ambiente:`. Um prompt V e sempre em portugues e sempre tem exatamente cinco partes na ordem:
   a linha `o avatar (homem/mulher) fala em ingles... a seguinte frase: "..."`, a linha do lip
   sync (`o avatar diz todas as palavras corretamente...`), a linha `o que acontece no vídeo:`,
   a linha `câmera:` e a linha `som ambiente:`.
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
parar. Nao adivinhar pela aparencia ou ordem da galeria. Cada V tem uma variacao.

### Videos em lotes fechados

1. Receber e registrar toda a fila V, sem executar tudo automaticamente.
2. Antes de cada V, conferir avatar, perfil e K indicado no MAPA K/V.
3. Usar a imagem exclusivamente como INITIAL FRAME, nunca Element, ingredient ou referencia de objeto.
4. Configurar Veo 3.1 Lite, Lower Priority, oito segundos e a quantidade de variacoes do perfil.
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

**Anexar no K01:** 1 imagem, `producao/sf_torta_vovo/REF_COMPOSICAO_frame_2s.jpg` (só câmera e disposição). Perfil clássico, 1 imagem
final; V01, V02 e V03 usam o K01 como INITIAL FRAME.

## Bloco de imagem

```text
K01
IMPORTANT: THIS IS IPHONE FOOTAGE, a vertical 9:16 phone video frame. Use the attached reference frame ONLY for camera height, camera angle and the layout of the table and the two people. Do NOT copy the people, faces, hair, skin tone, clothing, desserts or room from it. Both people are fictional AI-generated characters, no real person is depicted. A Black American grandmother around seventy-five, dark brown skin, short natural white afro, high cheekbones, deep wrinkles and a warm gap-toothed smile, standing behind the kitchen island, her age fully visible and never smoothed. A small granddaughter: a Black American girl about three years old, medium brown skin, box braids with small white beads at the ends, standing on the ground in front of the right end of the kitchen island, so small that her head only reaches the edge of the kitchen island. Grandmother: a mustard yellow cardigan over a cream blouse under a denim apron, no jewelry. Granddaughter: a mint green tulle dress with short puff sleeves, barefoot. The quantity is absurd, like a small bakery inside a home: the whole kitchen island is covered edge to edge with baking trays of big chocolate chip cookies with melty chocolate chunks, hundreds of them, with more trays stacked on two-tier metal stands and the back counter also lined with full trays. The nearest trays are very close to the lens in the lower foreground, large in frame, closer to the camera than the grandmother's face, nothing else competing with them. A bright American home kitchen with white shaker cabinets and a large window behind the grandmother letting in neutral overcast daylight, the backyard trees and a grey-blue cloudy sky clearly visible through the window, never white or blown out, a light wood floor, and a small American flag standing in a mason jar on the windowsill, discreet but clearly visible and in sharp focus. The grandmother stands behind the kitchen island with both hands resting on its edge, leaning slightly forward and looking down at her granddaughter with an amused smile. The granddaughter stands on her tiptoes at the right end of the kitchen island stretching one arm up toward one of the chocolate chip cookies on the nearest tray, her face turned up to her grandmother. The trays of chocolate chip cookies fill the lower left and lower middle of the frame, closest to the lens. The grandmother is seen from the waist up behind them in the upper middle. The granddaughter is seen head to toe at the lower right. Camera: phone held high at adult head height, angled slightly down, straight-on across the kitchen island, as in the reference frame. Start frame: the granddaughter is already reaching and already asking, caught mid-sentence, lips naturally parted, eager pleading expression with wide eyes; the grandmother is holding back a laugh. Neutral overcast daylight, soft even light on both faces with no harsh shadows, no warm orange cast and no yellow tint. Real skin with visible pores, irregular texture, fine lines and soft asymmetry on both faces, hair in uneven natural clumps, iPhone footage look, flat natural light, low contrast, slight JPEG compression, boring everyday reality, background fully in focus, everything in sharp focus, no blur, no bokeh, no AI polish, no beauty smoothing, no warm orange color cast, no yellow tint, no golden glow, no golden hour light, no sunset, no captions, no subtitles, no words overlaid on the image. Negative: no captions, no subtitles, no words overlaid on the image, no plastic skin, no extra fingers, no blur, no bokeh, no warm orange color cast, no yellow tint, no golden glow, no night scene, no dark windows, no beauty smoothing, no de-aging, no third person, no people copied from the reference frame.
```

## Bloco de vídeo

```text
V01
a neta (menina de uns três anos, a criança na frente da bancada) fala em inglês com sotaque americano, voz infantil doce e um pouco rouquinha de menina de uns três anos, falando devagar, pidona, pedindo com muita vontade, a seguinte frase: "Grandma, please let me eat that chocolate chip cookie now. I really want it."

a neta diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo. A avó fica calada enquanto a neta fala.

o que acontece no vídeo: a neta estica a mão para um dos doces da bandeja mais próxima olhando para a avó enquanto pede; quando a neta termina, a avó joga a cabeça para trás e solta uma risada alta, com a mesma voz dela (voz de avó americana de uns setenta e cinco anos, grave e lenta, de risada gostosa, com sotaque do Sul).

câmera: fixa, na mão de alguém da família, com leve tremor natural de celular

som ambiente: cozinha de casa silenciosa, sem música

V02
a avó (a senhora atrás da bancada) fala em inglês com sotaque americano, voz de avó americana de uns setenta e cinco anos, grave e lenta, de risada gostosa, com sotaque do Sul, ainda rindo e em tom de brincadeira, olhando para a câmera, a seguinte frase: "Okay, if people comment yes and follow this page, you can choose first."

a avó diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo. A neta fica calada, só olhando para a avó.

o que acontece no vídeo: a avó tira os olhos da neta, vira o rosto para a câmera e fala com quem está assistindo, no fim aponta de leve para a neta; a neta continua com a mão perto da bandeja, olhando para cima para a avó.

câmera: fixa, na mão de alguém da família, com leve tremor natural de celular

som ambiente: cozinha de casa silenciosa, sem música

V03
a neta (menina de uns três anos, a criança na frente da bancada) fala em inglês com sotaque americano, voz infantil doce e um pouco rouquinha de menina de uns três anos, falando devagar, pidona, implorando com os olhos arregalados, a seguinte frase: "Please comment yes and follow. I want to choose this chocolate chip cookie right now."

a neta diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo. A avó fica calada, só sorrindo.

o que acontece no vídeo: a neta vira de frente para a câmera, junta as duas mãos na frente do peito em súplica e dá pulinhos no lugar enquanto pede; a avó sorri atrás da bancada.

câmera: fixa, na mão de alguém da família, com leve tremor natural de celular

som ambiente: cozinha de casa silenciosa, sem música
```

## Montagem no CapCut
V01, V02, V03 na ordem · cortar o início de V02 e V03 até o primeiro movimento · texto de tela só
no T1: `Grandma, please let me eat that cookie` · legenda da fala nos três · sem música e sem Voice Changer · rótulo
`AI-generated` num canto.

## Transcrição final

| Take | English | Português |
|---|---|---|
| T1 | Grandma, please let me eat that chocolate chip cookie now. I really want it. | Vovó, por favor, me deixa comer aquele cookie de gotas de chocolate agora. Eu quero muito. |
| T2 | Okay, if people comment yes and follow this page, you can choose first. | Tá bom, se o pessoal comentar yes e seguir esta página, você escolhe primeiro. |
| T3 | Please comment yes and follow. I want to choose this chocolate chip cookie right now. | Por favor, comenta yes e segue. Eu quero escolher esse cookie de gotas de chocolate agora mesmo. |

## Roteiro final em inglês

1. Grandma, please let me eat that chocolate chip cookie now. I really want it.
2. Okay, if people comment yes and follow this page, you can choose first.
3. Please comment yes and follow. I want to choose this chocolate chip cookie right now.

Grandma, please let me eat that chocolate chip cookie now. I really want it. Okay, if people comment yes and follow this page, you can choose first. Please comment yes and follow. I want to choose this chocolate chip cookie right now.
