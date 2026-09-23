Voce executa prompts finalizados dentro do Google Flow. Nao reescreva, traduza, resuma nem
altere a copy. Registre o perfil da producao antes de gerar qualquer asset. Perfil ausente ou
incompativel com os codigos recebidos exige esclarecimento, nunca escolha silenciosa.

### Perfis de execucao

| Configuracao | AURALY | CLASSICO (Angle 1/2) |
|---|---|---|
| Imagem | Nano Banana 2 | Nano Banana 2 |
| Formato | 9:16 | 9:16 |
| Referencia de imagem | Fingerprint do avatar (identidade/corpo/pele apenas, ver secao abaixo) | Anchor do avatar ativo |
| Imagens por K | 4, com selecao manual | 1 imagem final |
| Relacao K/V | Mesmo numero: V01 usa K01 | Maior K menor ou igual ao numero de V |
| Video | Veo 3.1 Lite | Veo 3.1 Lite |
| Prioridade | Lower Priority | Lower Priority |
| Duracao por clipe | 8 segundos | 8 segundos |
| Variacoes por V | 3 | 1 |
| Anexo do video | INITIAL FRAME | INITIAL FRAME |
| Lote de video | Fechado, no maximo 7 codigos V | Fechado, no maximo 7 codigos V |

Os valores Auraly reproduzem as travas de WORKFLOW_AURALY.md. Nunca transportar as configuracoes
classicas para Auraly. Um pacote historico com outro contrato nao autoriza alterar uma producao
nova; preservar seu contrato aprovado quando o usuario solicitar especificamente sua retomada.

### AURALY, fingerprint e cenario por gancho (Luigi, 2026-09-14, padrao vigente)

A anchor de ambiente real foi substituida por uma FINGERPRINT: grade de estudio, fundo neutro,
rosto em varios angulos, corpo de frente/lado/costas, macro de pele. Ela trava somente identidade,
corpo e pele. Nunca trava roupa, cenario, pose ou luz; isso vem do texto de cada K.

Cada gancho escolhido passa a ter CENARIO PROPRIO do T1 ao CTA (K de hook + K de corpo + K de CTA
por cenario), nunca mais um corpo compartilhado pela fila inteira. Angulo de camera sempre exotico
e diferente entre os cenarios da mesma fila, nunca o padrao de rosto na altura da camera falando
reto. Roupa livre por cenario, sem obrigacao de repetir a roupa da fingerprint. Kit de tarologo
(cartas, cristal, incenso, vela, cruz, bandeira dos EUA) continua obrigatorio em todo K, so o
arranjo muda. Doutrina completa em WORKFLOW_AURALY.md.

### AURALY, excecao dos avatares de luxo (Luigi, 2026-09-18, v9)

Grant Whitmore, Marcus Sterling, Victor Ashford e Lorenzo Vale sao Auraly mas NAO usam o kit de
tarologo: sem cartas, cristal, incenso, vela ou cruz obrigatorios. O cenario de luxo descrito no
texto de cada K e a prova. A bandeira dos EUA continua, discreta e em foco. A referencia continua
sendo a fingerprint (blueprint): trava so identidade, corpo, pele e a assinatura de acessorio
(relogio e anel) descrita no prompt; roupa e cenario vem do texto.

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
Nao selecionar automaticamente nem avancar para video sem selecao. No classico, uma imagem
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

AURALY: V01 usa exclusivamente a imagem aprovada K01, V02 usa K02, e assim por diante. K01
nao substitui K02 ausente. Cada codigo V tem tres variacoes do mesmo prompt e frame selecionado.

CLASSICO: V usa o maior K disponivel cujo numero nao exceda o de V. Por exemplo, com K01, K03 e
K06: V01/V02 usam K01; V03/V04/V05 usam K03; V06 usa K06. Se nao houver K anterior ou igual,
parar. Nao adivinhar pela aparencia ou ordem da galeria. Cada V tem uma variacao.

### Videos em lotes fechados

1. Receber e registrar toda a fila V, sem executar tudo automaticamente.
2. Antes de cada V, conferir avatar, perfil e K correspondente.
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
