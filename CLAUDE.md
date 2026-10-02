# Roteamento vigente (2026-09-14)

**AGENTS.md tem precedencia.** Angle 1 = Natural Rems Sea Moss (desde 2026-10-02); Angle 2 = FitWell; Angle 3 = Auraly.
Para Auraly, processo, estado, configuracao e formato de resposta vivem somente em
`WORKFLOW_AURALY.md` e no CHECKPOINT da producao. As secoes Auraly abaixo documentam historico e
contexto criativo, nao autorizam reabrir decisoes, juntar K/V ou pular esperas. Consultar o
playbook mestre somente nas secoes criativas indicadas pelo workflow.

Para Angle 1 e Angle 2, as regras classicas abaixo continuam aplicaveis; FitWell usa
`PLAYBOOK_FITYWELL.md`. A configuracao de execucao usa o perfil classico do arquivo Flow,
que substitui os trechos antigos daqui sobre contagem de variacoes e casamento K/V.
Angle 4 = Body Hacks For Men 40+, de volta ao intake em 2026-10-02 (Luigi) para rodar na holistic.brandon
(COACH), ao lado de Dana, Jamie e Lynn (PAR).
Nao perguntar novamente por angulo ou avatar ja definidos. Uma tarefa de analise, organizacao ou
manutencao nao e uma ordem para executar a proxima etapa de producao.

**🔴 ANGULO 1 = NATURAL REMS SEA MOSS (Luigi, 2026-10-02).** Substitui a Korella Saffron, que vira
historico. Doutrina, CTA obrigatorio da marca e compliance na memoria `angulo1-copy-seamoss`. Onde
este arquivo diz "Korella", ler "Sea Moss" para processo e formato; copy, claim, vocabulario e avatar
da Korella nao passam. Tres travas que cortam o pagamento: (1) CTA de venda abre com **"Search Natural
Rems Sea Moss on Amazon" com o frasco em quadro**, link no comentario fixado depois e fim (4 passos do PDF em `producao/_seamoss/`, com o passo 3 trocado pelo
comentario fixado por decisao do Luigi em 2026-10-02), comentario opcional com `yes`, sem DM;
(2) legenda com `#ad #syntheticperformer #naturalrems` no topo e chave de IA ligada, growth incluso;
(3) sem antes/depois, sem medico/jaleco/clinica, sem cura ou resultado garantido, sem remedio nem
concorrente. O linter cobra as tres quando a producao cita Natural Rems ou Sea Moss.

Ferramentas de apoio: `controle/README.md`. Biblioteca e resultados nao substituem o workflow.
**Gate visual transversal (2026-09-22): `GATE_VISUAL.md`** e a fonte unica de realismo anti cara de
IA, composicao do heroi e checklist de gancho visual nos tres angulos. Os gates de realismo e de
composicao citados abaixo apontam para ele.
O grafo e opcional: se `graphify-out/` nao existir, consultar as fontes locais diretamente.

**🔴 VALIDAR ANTES DE VARIAR (Luigi, 2026-09-23), nos tres angulos:** toda producao nova a partir de
video modelo e **RODADA DE VALIDACAO**: um gancho so, o do video modelo, clonado com o maximo de
fidelidade, igual para toda a fila, aprovado junto com o roteiro. **Sem 10 ganchos, sem degrau e sem
escolha de gancho.** As 10 variacoes (Puzzle com degrau) so existem na **RODADA DE VARIACAO**, que
so abre quando o Luigi disser que um video postado performou, e partem do video validado. O resto
do workflow (fila, pacote por avatar, Flow, K/V, transcricoes, checklist, linter) nao muda. Fonte:
`GATE_VISUAL.md` Parte 4, Passo 0. Onde este arquivo fala em "10 ganchos", ler "so na rodada de variacao".

**🔴 ORIGEM DO VIDEO MODELO (Luigi, 2026-09-25), FitWell e Auraly:** no P1, classificar se o video
modelo e de **pessoa real (organico)** ou de avatar IA. Organico = **`PERFIL_ORGANICO.md`**, fonte
unica: gancho visual, copy e estrutura copiados **literalmente**, e **so o CTA muda** conforme angulo e
objetivo (Auraly venda: engajamento com `222` e depois foto de perfil / Stories). Marcador
`origem: organico` no topo do `ROTEIRO.md` (e `Source: ORGANIC` no checkpoint Auraly), com a linha
`CTA original:`. Na origem organica **nao se aplicam** bandeira em todo K, kit de tarologo, carta
SOULMATE, T1 mudo, plano unico com mesa nem o crivo de copy de venda; o resto do workflow, o
`GATE_VISUAL.md` Partes 1 a 3 e as travas de lei e marca continuam.

---

# Operação Vídeos Avatares IA — regras de trabalho

Este arquivo é carregado automaticamente em toda sessão. É a fonte de verdade do PROCESSO.
Copy, ângulos, obstáculos e rotas argumentativas ficam na memória. Aqui fica **como entregar**.

---

## Antes de começar QUALQUER produção

### Atalho operacional: `/watch`

Quando Luigi mandar uma mensagem com `/watch` e caminhos locais do vídeo e das imagens de avatar,
isso já significa: iniciar a produção completa dentro do chat e dos arquivos, sem pedir a frase
longa de briefing. **O ângulo decide o fluxo:** Ângulo 3 (Auraly) segue `AGENTS.md` →
**`WORKFLOW_AURALY.md`** → `CHECKPOINT.md` da produção (o `PLAYBOOK_MESTRE_AURALY.md` é só referência
criativa, e o `AURALY_AGENT.md` foi arquivado em 2026-09-22); Ângulos 1 e 2 seguem o fluxo clássico abaixo.

Formato esperado da mensagem:
```
/watch
video: caminho/do/video.mp4
avatares:
- caminho/do/avatar_1.jpeg
- caminho/do/avatar_2.jpeg
```

Se a mensagem trouxer só os caminhos, inferir o vídeo pelo `.mp4` e os avatares pelos arquivos de
imagem. Criar a produção em `producao/<slug_da_producao>/`, usando o nome do vídeo como base quando
Luigi não der um nome.

Autorização implícita deste atalho:
- rodar a análise do vídeo modelo;
- modelar a copy para a operação atual;
- gerar roteiro, ganchos, prompts de imagem, imagens necessárias quando o chat/ferramenta permitir,
  prompts de vídeo para Flow / Veo 3.1 / Omni Flash e manifest;
- salvar tudo em pastas locais organizadas por produção e por avatar;
- entregar também no chat o que Luigi precisa revisar, colar ou usar.

Avatares podem mudar a qualquer momento. Se Luigi mandar novos caminhos de avatar no meio da produção,
continuar o mesmo processo com os novos avatares, preservando roteiro/copy/hook quando ainda fizerem
sentido e ajustando só identidade, voz, prompts e pastas do avatar. Não estranhar troca de avatar e
não reiniciar o processo do zero sem necessidade.

1. Rodar `/watch` no `.mp4`.
2. **Ler `producao/fitywell_pernas/ROTEIRO.md` e `PROMPTS_PRODUCAO.md`.** São o gabarito vivo dos Ângulos 1, 2 e 4 desde 2026-09-10. Nunca reinventar o formato de memória. O `producao/brandon_angle2/` virou histórico junto com a Brandon.
3. Perguntar o ângulo (1 Sea Moss / 2 FityWell / 3 Auraly / 4 Body Hacks, de volta ao intake em 2026-10-02) e confirmar o avatar.
   **Exceção do avatar:** `.mp4` + imagem de avatar na mesma mensagem já decide para quem é,
   ver a seção do Ângulo 3. Nesse caso só resta perguntar o ângulo.
   **Ângulo 3 tem fluxo próprio**, ver a seção no fim deste arquivo. O passo 1 vira opcional lá.
4. **Ângulos 1, 2 e 4:** criar `producao/<avatar>_<slug>/` e escrever os DOIS arquivos.
   **Ângulo 3:** ver `WORKFLOW_AURALY.md`: pasta `producao/<slug>/`, sem prefixo de avatar,
   marcador `pipeline: auraly` no `ROTEIRO.md`.

## 🔴 LIMITE DA MINHA FUNÇÃO E ORDEM DA ENTREGA (Luigi, 2026-09-08)

**Eu NÃO gero imagem, NÃO abro navegador, NÃO executo Flow e NÃO automatizo browser.**
Minha função termina na entrega do pacote de produção. O Luigi usa o pacote depois, no agente
do Google Flow.

♻️ **DESCONTINUADO nesta operação:** Auraly Studio, bridge local, extensão Chrome, execução
automática no ChatGPT, preflight, browser queue, batch execution, abrir abas, `pacote_browser`
e a identificação de Modo A / B / C. Documentação antiga sobre isso é **HISTÓRICA** e não define
o workflow atual. O que sobrevive do Ângulo 3 é só o **contexto criativo**: público, oferta,
linguagem, copy, avatares, regras visuais, estrutura de roteiro e aprendizados.

**Workflow oficial, igual ao dos Ângulos 1 e 2:**
`.mp4` + âncoras → análise do vídeo → transcrição → análise da estrutura da copy → roteiro
modelado **com o gancho fiel do modelo** → **aprovação do Luigi** → pacote final.
**Só na rodada de variação** (vídeo já validado no perfil, 2026-09-23): roteiro validado →
**10 ganchos visuais** → **escolha dele** (quantidade livre) → pacote final.

**O pacote final sai NESTA ordem, sem pular item:**

1. **`INSTRUÇÕES PARA A MEMÓRIA DO AGENTE — GOOGLE FLOW AI`**, colado INTEIRO no chat, pronto pra
   copiar. Fonte canônica: `producao/_flow/INSTRUCOES_AGENTE_FLOW.md`.
   Configuração vigente: **a tabela de perfis do próprio arquivo (v17, 2026-09-25) manda.** Clássico
   (Ângulos 1 e 2): Nano Banana 2 em 9:16, **4 imagens por K__ com seleção manual** (o Luigi apaga 3 e
   deixa 1); vídeo **só no Omni Flash**, 8 segundos, um único resultado por V__, a partir da imagem que
   sobrou. Auraly: 4 imagens por K__ com seleção manual e Veo 3.1 Lite com 3 variações por V__.
   ⚠️ **No Ângulo 3 (Auraly) vai TODA VEZ, sem exceção** (Luigi, 2026-09-08). O momento é fixo:
   **logo depois de o Luigi aprovar o roteiro com o gancho fiel (rodada de validação) ou escolher
   os ganchos (rodada de variação), e ANTES do primeiro prompt de imagem.**
   ♻️ Isto **revoga** a permissão de "se nada mudou, basta dizer que a memória do agente Flow
   permanece a mesma". Não existe atalho: o bloco é colado por inteiro em cada produção, porque
   ele é colado numa memória de agente nova a cada rodada. Se a configuração mudar, subir a versão
   na tabela do arquivo antes de colar.
2. **[ÂNGULO 3] BLOCO ÚNICO DE IMAGEM, LIMPO PARA MÁQUINA** (Luigi, 2026-09-09)
3. **[ÂNGULO 3] BLOCO ÚNICO DE VÍDEO, LIMPO PARA MÁQUINA** (Luigi, 2026-09-09)
4. Body e CTA entram DENTRO dos dois blocos acima, na ordem do vídeo, nunca como seção solta

### 🔴 GOOGLE FLOW DELIVERY FORMAT (Luigi, 2026-09-09)

♻️ **Revoga o formato de 2026-09-08**, que levava descrição, anexo e ação dentro do bloco copiável.
O agente do Flow é executor e estava **lendo texto auxiliar como se fosse prompt**.

```
IMAGE BLOCK:  UM K__ = UM PROMPT DE IMAGEM EM JSON · K__ SÓ COMO RÓTULO · TODO PROMPT AUTOSSUFICIENTE
VIDEO BLOCK:  UM V__ = UM PROMPT DE VÍDEO  · V__ SÓ COMO RÓTULO · TODO PROMPT AUTOSSUFICIENTE
              K01 casa com V01 PELO NÚMERO

SEM descrição · SEM título · SEM rótulo T__ · SEM metadata · SEM "Prompt:" · SEM "usa K__"
SEM instrução de INITIAL FRAME dentro do bloco · SEM configuração de modelo dentro do bloco
```

- **O rótulo é só o código sozinho numa linha**: `K01`, nunca `K01 · T1 · GANCHO...`.
- **UMA IMAGEM = UM VÍDEO.** Sem exceção. No T1 do Ângulo 3 os cortes do gancho são **internos ao
  clipe**, escritos dentro do `V__` e gerados pelo Veo, então continua `1 K + 1 V`. Ver o P4.
  Se cinco ganchos dividem a mesma fala, **duplicar o prompt de vídeo**,
  um por keyframe. ♻️ Acaba o `V01 usa K01, K02, K03`. E **um keyframe nunca serve dois takes**:
  se dois takes usam o mesmo setup, saem dois `K__` com prompts próprios.
- **Autossuficiência mata o `EDITAR do K__` no bloco do Flow.** Cada prompt de imagem descreve
  sozinho identidade, roupa, ambiente, luz, enquadramento, props, ação e expressão, porque o Flow
  recebe só a âncora mais aquele prompt. Repetir condição importante dentro de cada prompt é certo,
  não redundante. O mesmo vale no vídeo: nada de `same as previous`.
- **`REF-CARTA` e `REF-A` não entram no bloco do Flow.** O prop e a segunda pessoa passam a ser
  **descritos por escrito dentro de cada prompt** que os mostra. O anexo é só a âncora.
  ♻️ **Exceção do MOVIE STYLE (short form e venda, Luigi, 2026-09-23):** cada personagem principal
  ganha um character sheet `REF-P1`, `REF-P2`..., que **entra** no bloco de imagem (gerado e
  aprovado antes dos K) e é **anexado** nos K listados no MAPA DE ANEXOS, fora dos blocos. O K
  continua autossuficiente: descreve cada personagem por escrito também. Workflow em
  `producao/_swipe_movie_style/PROPOSTA_WORKFLOW_MOVIE_STYLE.md`; executor em
  `INSTRUCOES_AGENTE_FLOW.md` (seção MOVIE STYLE, desde a v13).
- **Tabela humana de leitura** (`K01 = coração quebrando`, `K06 = body`) pode existir, mas **sempre
  fora** dos blocos copiáveis. Dentro deles, zero texto auxiliar.
- **O JSON continua sendo a fonte de verdade INTERNA** em `PROMPTS_IMAGEM.md`, que é o que o linter
  lê. O bloco do Flow é a versão de execução, autossuficiente.
- 🔴 **O prompt de imagem entregue é JSON (Luigi, 2026-09-25, contrato do Flow v17).** ♻️ Revoga o
  "texto corrido" do bloco de imagem. Todo `K__` (e `REF-P`) sai como UM objeto JSON em inglês,
  logo abaixo do código, com os campos `format`, `fiction_note`, `reference_use`, `identity_main`,
  `wardrobe`, `scene`, `prop`, `posture`, `composition`, `camera`, `lighting`, `state`, `realism`,
  `aspect_ratio` e `negative`, sem `shot_id` (é metadata). **As regras de conteúdo não mudam**:
  autossuficiência, GATE_VISUAL, trecho de realismo, negative, bandeira, herói colado na lente,
  checklist de envio. Vale nos três ângulos. O vídeo continua texto simples nos 5 blocos.
5. (nos Ângulos 1, 2 e 4 segue valendo um prompt por bloco, com linha curta antes de cada um)
6. Transcrição final completa em **INGLÊS**
7. Transcrição final completa em **PORTUGUÊS**

⚠️ **A transcrição SEMPRE fecha a produção** (Luigi, 2026-09-08). Não é opcional e não é sob pedido:
todo processo de produção termina com as duas transcrições coladas no chat, take a take mais a versão
corrida. Nunca dizer "está no ROTEIRO.md" no lugar de colar.

**Workflow e formato podem espelhar os Ângulos 1 e 2. Copy, produto, nicho e linguagem NÃO se
misturam entre ângulos.**

### GOOGLE FLOW DELIVERY FORMAT (Luigi, 2026-09-09)

Os blocos de execução devem ser estritamente machine-readable: `K__` sozinho, seguido somente de um
prompt de imagem completo e autossuficiente em JSON (desde 2026-09-25); `V__` sozinho, seguido somente de um prompt de vídeo
completo e autossuficiente. Um K = um V pelo mesmo número. Nunca incluir nos blocos títulos,
descrições, T__, metadata, settings, INITIAL FRAME, `uses K__`, caminhos ou notas. Nunca depender de
"edit K__", "same as previous" ou contexto de outro prompt.

### Transcrição por avatar (Luigi, 2026-09-09)

Depois do bloco limpo de imagens e do bloco limpo de vídeos de **cada avatar**, entregar sempre uma
tabela de transcrição final por take, com as colunas `Take`, `English` e `Português`. A tabela vem
fora dos blocos machine-readable e reproduz exatamente as falas aprovadas, sem paráfrase.

## A entrega tem SEMPRE dois arquivos + tudo colado na conversa
(**Ângulo 3 usa o pipeline Auraly, ver `WORKFLOW_AURALY.md`**)

Arquivo não substitui o chat, e chat não substitui o arquivo. **Os dois, sempre.**

### `producao/<avatar>_<slug>/ROTEIRO.md`
Nesta ordem, sem pular seção:
1. Cabeçalho: vídeo modelo, avatar, variável trocada, funil, enquadramento do avatar
2. **Tabela de esqueleto preservado** (`# | Beat | Original | Adaptado`)
3. **Setups de cena** (Setup A, B, C... = os blocos de imagem)
4. Roteiro cena a cena: `### T1 · BEAT · TALKING|B-ROLL · Setup A`
5. Roteiro só-fala (inglês, pra TTS)
6. Notas de produção (duração, herói do hook, compliance, o que cortar se ficar longo)

### `producao/<avatar>_<slug>/PROMPTS_PRODUCAO.md`
Nesta ordem, sem pular seção:
1. Cabeçalho: vídeo modelo, caminho da âncora, funil
2. **Índice de geração** (`Take | Keyframe | Ação de geração`)
3. **Trava de identidade e continuidade** (bloco único, reaproveitado, não repetir em cada JSON)
4. **Trava do prop herói** (se houver)
5. **Trava da 2ª pessoa (REF-A)**, gerar e aprovar ANTES de tudo
6. Prompts de imagem: `K01`, `K02`... JSON
7. **Bloco global de vídeo** (colar em todo prompt)
8. Prompts de vídeo: `V01 · T1 · usa K01`, texto simples
9. **Mapa de âncoras** (`Keyframe | Referências a anexar | Modelo`)
10. **Montagem no CapCut**
11. **Gates de qualidade** (checklist numerado)

## Nomenclatura, nunca misturar

| Prefixo | O que é |
|---|---|
| `T__` | Take do roteiro (a fala) |
| `K__` | Keyframe, a imagem |
| `V__` | Clipe de vídeo |
| `REF-__` | Referência auxiliar (2ª pessoa, prop) |

## MULTI-AVATAR PRODUCTION RULE (Luigi, 2026-09-09)

Quando uma produção começa com um MP4 e N anchors, registrar imediatamente todos os avatares em uma
fila persistente dentro da pasta da produção, com nome, caminho exato da anchor e estado `PENDING`,
`ACTIVE` ou `DONE`. Essa fila é estado obrigatório e não pode depender do histórico da conversa.

Roteiro, takes, falas, análise, hooks selecionados, ordem de K/V e lógica de movimento são aprovados
uma única vez por produção. Cada avatar recebe os mesmos elementos, com adaptação apenas de
identidade, idade, cabelo, roupa, ambiente, iluminação e detalhes da própria anchor.

Concluir um avatar nunca encerra a produção. Depois de cada pacote, consultar a fila, marcar o avatar
atual como `DONE`, avançar automaticamente o próximo `PENDING` para `ACTIVE` e entregar seu pacote.
Somente declarar `PRODUCTION COMPLETE` se não houver `PENDING` nem `ACTIVE`.

Vários `T` podem usar o mesmo `K`. Cada `T` tem seu `V`.

## Imagem: gerar do zero é exceção

`GERAR DO ZERO` só no primeiro keyframe de cada setup. Todo o resto é **`EDITAR do K__`**, que trava rosto, fundo e luz.
Gerar tudo do zero faz a identidade derivar entre blocos.
Estágios sempre a partir do original, **nunca em cascata**.

## Prompt de imagem = JSON. Prompt de vídeo = texto simples.

**Nunca misturar.** O prompt de vídeo não descreve enquadramento, cor nem composição, isso já está na imagem. Ele só carrega fala, ação, câmera e som.

Formato de vídeo (Fase 7), os cinco blocos:
```
o avatar (mulher) fala em inglês com sotaque americano de [avatar], voz autêntica, dinâmica, apaixonada e emocional, como se exigisse ser ouvida, a seguinte frase: "[FALA EXATA DO ROTEIRO]"

o avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: [ação ENXUTA, só o que acontece]

câmera: [fixa / leve push-in / leve handheld]

som ambiente: [ambiente], sem música
```
B-ROLL: trocar a primeira linha por `(sem fala no take: a fala N entra como voz-over na edição)`.

## Regras que quebram a entrega se forem ignoradas

- **8 segundos por take = 13 a 29 palavras.** Contar ANTES de escrever os prompts. Take longo se quebra em fim de frase. **Nunca inventar filler, nunca parafrasear.** Exceção (Luigi, 2026-09-23): no `formato: short-form`, take de DIÁLOGO com ação não tem piso; o teto de 29 continua.
- 🔴 **O take segue a CENA do modelo (Luigi, 2026-09-23).** Cada cena do modelo vira o próprio take:
  **nunca juntar duas cenas num take e nunca cortar frase no meio para caber na faixa.** Cena curta
  no modelo vira take curto, marcado `CENA CURTA` no cabeçalho do `ROTEIRO.md` (o piso de 13 não
  vale para ele; o teto de 29 vale sempre). Plano do modelo com mais de 8s se divide só em fim de
  frase. A frase só atravessa dois takes quando o próprio modelo corta a cena no meio dela.
- **A fala no prompt é cópia literal do roteiro final.**
- **Keyword por ângulo: `yes` nos Ângulos 1, 2 e 4, `222` no Ângulo 3 (Auraly).** Nunca a palavra do vídeo original. No Ângulo 4 a keyword é provisória, ver a seção dele.
- **Zero travessão (`—`)** em copy, roteiro e resposta.
- **Reveal contínuo dentro de um take = UMA imagem** do estado inicial. Se o original corta, aí sim são imagens separadas.
- **Um prompt de imagem por SETUP**, não por take.
- **[TODOS OS ÂNGULOS] Nenhum prompt sai sem o CHECKLIST DE ENVIO 100% aprovado** (memória
  `checklist-envio-prompt`, insights do curso Lib Korella, Luigi 2026-09-22). Ver P9.
- 🔴 **[TODOS OS ÂNGULOS] Nenhum `K__` sem a FICHA DO FRAME e o PLACAR (Luigi, 2026-09-25).** Antes de
  escrever qualquer prompt de imagem, preencher `FICHA_FRAMES.md` olhando o frame do modelo daquele take
  (forma do herói, quanto do quadro, distância da lente, câmera, pose, lista fechada, frame 0) e o
  placar F1 a F6 + G1 a G8 com o trecho LITERAL do K como evidência. O modelo manda no conteúdo, o gate
  no acabamento e no piso de proximidade. `checar_entrega.py` reprova ficha ausente, evidência que não
  está no K, herói sem medida e câmera sem lente e altura. Método em `GATE_VISUAL.md` Parte 6.
- **[TODOS OS ÂNGULOS] `GATE_VISUAL.md` é a fonte única dos dois gates abaixo e do método de gancho**,
  em Korella, FitWell e Auraly, sem exceção de ângulo (Luigi, 2026-09-22). Os bullets abaixo são o resumo.
- **Rodar o GATE DE REALISMO junto com o de composição** (memória `realismo-anti-cara-de-ia`): herói isolado com
  duas ou três âncoras de fundo no máximo, luz **neutra de dia nublado** e nunca quente (**golden hour banida desde 2026-09-22**), negative carregando
  `no warm orange color cast, no yellow tint`, e partir sempre de algo real. Realismo é volume de regeneração.
- **Rodar o gate de composição visual ANTES de escrever os prompts** (memória `checklist-composicao-visual`): herói no lower foreground mais perto que o rosto, sempre mais perto do que parece certo, 2ª pessoa cortada pelo quadro, cenário reconhecível e nunca inventariado. Reduzir fundo é com enquadramento, nunca com blur.
- **Bandeira dos EUA em TODO prompt de imagem, discreta porém VISÍVEL e em foco** (exceção: origem
  orgânica, onde é opcional e só como detalhe natural, `PERFIL_ORGANICO.md`). Escrever no campo
  `scene`, contando como uma das três âncoras de fundo. Única exceção: prompt de REF de prop isolado
  (REF-CARTA, `product.png`), que não tem cenário e contaminaria todo keyframe que anexasse a REF.
- **Prompt entregue é prompt COMPLETO.** Nunca "adicione X em todos os prompts", nunca colar só a linha
  que mudou. Regra nova no meio da produção obriga **reescrever por inteiro todos os prompts afetados**,
  no arquivo e no chat. Alternativa se entrega como dois prompts completos lado a lado, nunca como
  um prompt mais a instrução de como virar o outro.
- **Referências no título do prompt, em CAIXA ALTA, MAIS o bloco visual de anexo** logo abaixo do
  título e acima do código: número de imagens em negrito, cada uma numerada com o caminho, e a ação
  (`🆕 GERAR DO ZERO` ou `✏️ EDITAR`). O título sozinho não resolve para quem gera take a take.
  Formato exato em `prompts-imagem-json`. **A linha que descreve a cena nunca ocupa o lugar dessa.**
- **Ângulo 3, lei do registro: divino, nunca oculto.** O teste é a LEITURA, não o objeto: prop que lê como
  manifestação entra (cartas, cristais, vela, defumador, tigela com pétalas), prop ou fala que lê como pacto não.
  Sem bruxa, feitiço, spell, shield, círculo de proteção. ♻️ **Exceção da ramificação DINHEIRO/ABUNDÂNCIA
  (Luigi, 2026-09-29):** ali a copy pode usar a língua da VSL do funil (ritual, proteção energética,
  escudo invisível, energia negativa, inveja dos outros, banho de limpeza); bruxa, feitiço, spell, hex,
  praga, pacto e amarração continuam proibidos. Detalhe em `angulo3-copy-auraly`. **Cartas HOLOGRÁFICAS / FOIL, arte saturada e chamativa** (2026-08-29, revoga a paleta pálida): borda metálica espelhada com reflexo de arco-íris ou foil dourado, faixa de título na base. **A trava é a LEITURA, não a cor:** casal, coração, rosas, luz. Azul-noite com estrelas entra; caveira, corvo, serpente, espada e símbolo invertido não.
- **Ângulos 2 e 3 não mostram produto.** Ângulos 1 e 4 mostram sempre (no 4 é um **livro FÍSICO**, nunca mockup de ebook nem tela de celular).
- **[FITYWELL] O processo dos Ângulos 2 e 4 vive em `PLAYBOOK_FITYWELL.md`**, que é o equivalente
  do `PLAYBOOK_MESTRE_AURALY.md` para esta marca. Ler antes de produzir.
- **[FITYWELL] Roster por ângulo:** Dana Morrison, Jamie Anderson e Lynn Parker continuam nos
  Ângulos 2 e 4 desde 2026-09-10. Em 2026-09-19, o Ângulo 2 recebeu mais sete avatares: Eva Dall,
  Ivy Carl, Jamie Voss, Lais Collins, Lia Carlla, Robert Alves e Roberta Carvalho. Não estender os
  sete ao Ângulo 4 sem decisão explícita. **No Ângulo 2 todos são COACH**; quando quem fala é homem,
  o crivo de nunca culpar ela roda DUAS vezes. **No Ângulo 4 os três originais são PAR**, com 1ª
  pessoa liberada. ♻️ **2026-10-02: a holistic.brandon roda os Ângulos 1 (Sea Moss), 2 e 4, sempre
  COACH** (no 4 com a moldura dela de 2026-08-27, seção 7 de `angulo4-copy-bodyhacks`), âncora
  `producao/_ancoras/holistic_brandon_ancora.jpg`. Âncoras em `producao/_ancoras/`.
- **[ÂNGULO 4] LIMITE HONESTO É PROIBIDO.** Nenhuma ressalva, nenhum "isso não faz X". A dor prometida
  e o mecanismo do produto são a mesma linha, então toda ressalva encosta na promessa. O take vai pra
  autoridade, prova social, urgência ou escassez. No Ângulo 3 o objeto de desejo do CTA é
  **o rosto da alma gêmea**, nunca o app: ela mandou uma mensagem ao universo, o universo respondeu, ela
  **sela o acordo** (`222` + follow + save), e o **rosto está esperando no STORIES**, revelado pelo botão
  do link. Ângulo de entrada é livre, a **ponte pro rosto é obrigatória**.
- **Roteiro final completo é a ÚLTIMA coisa da entrega**, depois de todos os prompts. E o último bloco de todos é sempre o **roteiro final em INGLÊS**, numerado por take mais a versão corrida só-fala. A tabela bilíngue vem antes dele, não no lugar dele.
- **Os gates de maquina rodam sozinhos no `pre-commit`** (`git config core.hooksPath .githooks`,
uma vez por clone). Ele bloqueia commit com drift de memoria ou FALHA de entrega.
- **Entrega não fecha com FALHA no `checar_entrega.py`.** O linter lê do disco e sobrevive ao resumo
  de contexto de sessão longa, que é exatamente quando eu esqueço regra.
- **Nunca sugerir "tenta de novo"** quando o Luigi reporta bloqueio. Ele já tentou várias vezes.
- **Nunca listar termo sensível no `negative`** (nome de órgão, gore, logo/marca). O classificador lê o token, não a negação.

## PORTÕES DE CONSULTA (ler ANTES de agir, nunca depois)

Regra que gera tudo isto: **eu não abro documento sozinho.** Se a leitura não estiver amarrada a um
momento do fluxo, ela não acontece e eu erro. Cada portão abaixo é obrigatório no seu momento.

### P1 · Ao receber o `.mp4`, ANTES de rodar `/watch`
- `biblioteca-videos` → **este esqueleto já foi produzido?** Se já, qual variável usamos e o que não repetir
- `skill-watch` → como rodar o pipeline
- `erros-recorrentes` → os 3 erros históricos de leitura de hook, pra não repetir o quarto

### P2 · Depois da transcrição, ANTES de tocar em uma vírgula da copy
**Este é o portão que mais paga.** Nada de método puzzle antes de reler estes:
- `metodo-puzzle` → esqueleto, variável, herói, teste do estranho
- `feedback-copy-lapida-estrutura` → **rodar o CRIVO DE COPY**
- `referencia-frameworks-copy` → régua germânica, 3 relevâncias, loop aberto, os 4 vazamentos de venda
- `congruencia-matriz` → usuário x coach, e se o claim exige idade vivida
- `estilo-copy-sem-travessao`
- **Do ângulo:** 1 → `produtos-angulos` · 2 → `angulo2-copy-fitywell` · 3 → `angulo3-copy-auraly` + `angulo3-swipe-padroes` · 4 → `angulo4-copy-bodyhacks`
- **Rodar `python checar_frases.py producao/<pacote>`**: compara o roteiro com os anteriores da
  MESMA conta e aponta frase ja queimada. Ignora clone entre avatares e o beat de CTA
- **Se o roteiro tiver fechamento:** `banco-rotas-argumentativas` (**conferir o LOG de rotação**) + `banco-obstaculos` + `feedback-ponte-argumentada`
- **No beat de CTA:** `feedback-cta-produto`

Só depois disso a copy pode ser modificada e mandada pro Luigi aprovar ou ajustar.

### P3 · ANTES de entregar o roteiro pra aprovação
- `ordem-entrega-padrao` → transcrição, cena a cena, só-fala, tabela bilíngue única
- Contagem de palavras take a take, feita **agora** e não depois
- `compliance-riscos` → qual é o claim mais arriscado deste roteiro

### P3.5 · [TODOS OS ÂNGULOS] ANTES de sugerir os ganchos visuais
- **Primeiro: qual é a rodada?** (`GATE_VISUAL.md` Parte 4, Passo 0, Luigi 2026-09-23). Produção
  nova = **VALIDAÇÃO**: um gancho só, fiel ao modelo, com os desvios obrigatórios declarados, entregue
  junto com o roteiro, e o resto deste portão e do P4 **não roda**. Só a **VARIAÇÃO**, aberta pelo
  Luigi depois de um vídeo postado performar, segue para os itens abaixo, com o vídeo validado no
  lugar do vídeo modelo.
- **`GATE_VISUAL.md` Parte 4, PUZZLE COM DEGRAU**, em Korella, FitWell e Auraly (Luigi, 2026-09-22):
  ação estrutural + peça viral intocáveis, UM degrau no esqueleto, HOOK 1 controle, HOOK 2 a 10 com
  o degrau e uma variável cada, checklist de cada variação, vencedor vira a base da próxima rodada.
- As travas de cada marca continuam: Korella e FitWell com congruência como gate e clickbait
  proibido; Auraly com o P4 abaixo.
- **Skill `gancho-verbal`, modo PRODUCAO, nos três ângulos (Luigi, 2026-09-22):** o Puzzle decide o
  que se VÊ, a skill decide o que se LÊ e OUVE. Topo com tese, sintoma-alvo, direção e banco verbal
  de 5 frases literais do roteiro; texto de tela de até 9 palavras com frase do banco; testes de
  troca, leitura errada, sincronia, print e direção; `Recomendacao: HOOK X` no fim.

### P4 · [ÂNGULO 3] ANTES de sugerir os ganchos visuais

> **2026-09-23:** as 10 desta seção são só da **rodada de variação**. Na rodada de validação o
> gancho é o do modelo, fiel, e o T1 segue a gramática do modelo (mudo com cortes internos ao `V__`
> se o modelo abre assim; falado se o modelo abre falando). As travas do ângulo continuam valendo nas duas.

♻️ **REESCRITO EM 2026-09-20** depois da análise medida de 54 virais do nicho
(`producao/analise_ganchos_maya_claude_2026_09_20/ANALISE_MEDIDA_GANCHOS.md`). Tudo nesta seção vale
**só no Ângulo 3**. FityWell (2 e 4) e Korella (1) não mudam: lá a variação continua pelo MÉTODO
PUZZLE aplicado ao herói do hook, como está na tabela mais abaixo.

#### 🔴 AQUI É PUZZLE, IGUAL AO ÂNGULO 2 (Luigi, 2026-09-20)
♻️ **2026-09-22: virou PUZZLE COM DEGRAU, nos três ângulos** (Luigi mandou fundir o Puzzle com o
*step up* do curso Lib Korella, ficando com o mais forte de cada). Método canônico em
`GATE_VISUAL.md` Parte 4. Em resumo: declarar **ação estrutural + peça viral** (intocáveis), subir
**UM degrau** no esqueleto (`DIFICULDADE`, `CONTRADICAO`, `REACAO`, `EUA` ou `ESCALA`), e só então
as 10: **HOOK 1 = CONTROLE** sem o degrau, **HOOK 2 a 10** com o degrau, **uma variável cada**. O
vencedor vira a base da rodada seguinte, que sobe outro degrau. O resto desta seção continua valendo.
♻️ **Revoga o portfólio `4 + 3 + 3` em três famílias**, que durou menos de um dia, e **revoga** a
distribuição ainda mais antiga de 4 impacto físico / 2 bizarras / 2 reveal / 2 curiosidade.
♻️ **Revoga também** a regra de 2026-09-08 de que o gancho nasce de invenção livre e de que
*"gancho antigo com objeto trocado é entrega reprovada"*. **Trocar uma variável virou o método.**

- **O esqueleto sai do HOOK DO VÍDEO MODELO**, exatamente como na FityWell. Não é invenção, não é
  família escolhida no banco. É o método Puzzle: **extrair a ação estrutural do gancho original,
  manter fidelidade quase total e trocar UMA variável por sugestão.**
- **10 sugestões, todas do MESMO esqueleto:** HOOK 1 é o controle sem degrau, HOOK 2 a 10 levam o
  degrau (2026-09-22). Não existe mais família A/B/C.
- **A ação estrutural não se toca.** Se no modelo ela põe uma peça de roupa numa panela, joga pó e
  depois um creme, a ação estrutural é `põe UMA PEÇA DE ROUPA numa panela, joga UM PÓ e depois UM
  CREME`. Uma variação troca a peça, outra troca o pó, outra troca o recipiente. Nunca dois de uma
  vez: **trocar duas variáveis já é gancho novo e sai da etapa.**
- **Eixos de troca no Ângulo 3** (mais largos que os dois da FityWell, porque aqui o herói não
  carrega argumento): `OBJETO` · `SUBSTÂNCIA` · `LOCAL` · `COR` · `RESULTADO` · `MARCADOR` · `ALVO`.
- **Marcar em cada sugestão qual variável foi trocada.** É o que prova que ainda é Puzzle.
- **O banco `producao/_swipe_auraly/BANCO_GANCHOS_VISUAIS.md` NÃO é a fonte da ideia.** Ele serve
  para **controle de repetição** (não repetir literalmente objeto, texto de tela ou execução já
  publicados), padrão de qualidade e universo visual. A fonte é sempre o vídeo modelo.
- **Por que isto é coerente com a medição:** 81% dos virais da amostra são oito esqueletos repetidos
  com uma variável trocada. A conta que vence não inventa formato novo a cada post, ela varia o
  próprio esqueleto. Puzzle é o nome disso.
- **Custo:** cada variação continua **1 keyframe + 1 clipe**, porque só o T1 muda.
- **O que muda na copy:** só a camada de texto de tela do T1 e, se houver, a voz-over do T2 que
  nomeia o objeto. Do T2 em diante a fala fica idêntica em todas.

**A diferença que sobra para a FityWell:** lá o herói do hook carrega argumento, então congruência
com a fala do T1 é gate e clickbait puro é proibido. **Aqui não.** No Ângulo 3 a congruência trava
**na fala**, nunca no objeto, e **clickbait puro continua liberado**, indo no fim e marcado como tal.
`OUTPUT CONTRACT` dos hooks em `WORKFLOW_AURALY.md`. Gabarito de formato:
`producao/fitywell_pernas/GANCHOS_VISUAIS.md`, que é o exemplo rodado do mesmo método.

#### 🔴 OS CORTES DO GANCHO VÃO DENTRO DO PROMPT DE VÍDEO (Luigi, 2026-09-20)
Medição: o gancho dos virais tem **5 a 7 mudanças de plano em 6 segundos** (cortes em
`0.93 · 1.57 · 2.13 · 4.13 · 6.00`) e o corpo do vídeo tem **zero cortes** pelos 70 a 130 segundos
seguintes. **Correção do Luigi na mesma data:** isso **não** são vários clipes. É **UM clipe só**,
com as mudanças de plano **escritas dentro do prompt de vídeo** e geradas pelo Veo no mesmo take.

- **Continua `1 K + 1 V` no gancho.** ♻️ Isto **revoga** a versão anterior desta mesma seção, que
  mandava fatiar o T1 em 4 a 6 `K__`/`V__` curtos. Não existe exceção ao `UMA IMAGEM = UM VÍDEO`.
  O `K__` do gancho é **o primeiro plano da sequência**, e o resto nasce dentro do `V__`.
- **O bloco `o que acontece no vídeo` passa a carregar a sequência de planos**, nesta ordem fixa:
  **ação já começada** → **corte para MACRO das mãos exatamente no instante do payoff** → **corte de
  volta para o plano de corpo**. O macro nunca é decorativo: entrega recompensa tátil sem entregar
  explicação. ⚠️ Isto é exceção consciente ao *"menos é mais na descrição da ação"* do P6, e vale
  **só no take do gancho**: do T2 em diante a ação volta a ser enxuta.
- **O bloco `câmera` declara que os cortes são internos** ao clipe, em vez de `fixa / push-in`.
- **O T1 nasce MUDO.** Medido: os 3 primeiros segundos dos virais estão de 14 a 17 dB abaixo do
  corpo (-31 a -34 dB contra -17 dB), o que é room tone, não fala baixa. A voz entra por volta de
  3-4s. Marcar `T1 · B-ROLL · MUDO` no `ROTEIRO.md` e abrir o prompt de vídeo com
  `(sem fala no take: ...)`; a fala do T1 vira voz-over no T2 ou é cortada.
  O `checar_entrega.py` já aceita (`:78`, `:138`, `:254`).
- **Split vertical liberado no gancho:** rosto/busto em cima, mãos e ritual embaixo, com costura
  dura, descrito também dentro do `V__`. ♻️ **Abre exceção** ao `PLANO ÚNICO, nunca split screen` da
  seção do Ângulo 3, e **só no T1**. Do T2 em diante o plano único segue obrigatório.
- **Custo do gancho não muda:** continua **1 keyframe + 1 clipe** por variação.

#### O sentimento-alvo: CONSTRANGIMENTO PRODUTIVO, não admiração
Antes de pensar em símbolo de nicho, responder: *"que ação doméstica, fisicamente real e levemente
constrangedora, ela faria sozinha em casa e não contaria pra ninguém?"*. A alma gêmea entra **na
fala**, nunca no objeto.
- A transgressão é **doméstica e corporal**, nunca ocultista: objeto de cozinha ou banheiro no lugar
  errado. Passa na moderação e constrange ao mesmo tempo.
- **Admiração reprova.** Cofre dourado abrindo, moeda dentro da pedra, carta expelida por máquina:
  são bonitos, explicam a cena e por isso deslizam. VFX só entra se **não explicar** (um flash de
  transição entra; um reveal que fecha o sentido não).
- **O significado não fecha no gancho.** A ação física resolve; a consequência pessoal fica aberta.
- `IMPACT FIRST · CURIOSITY SECOND · CONGRUENCE ALWAYS` continua valendo. Gancho em que a avatar
  apenas mostra, segura ou aponta para um objeto reprova, salvo força excepcional.

#### Camada de texto de tela (edição, nunca dentro do `K__`)
Todo gancho declara duas linhas, **fora** dos blocos do Flow, porque são legenda de CapCut:
- **linha de desejo**, concreta e não mística, no padrão `When you need [desejo urgente]:`
- **linha de seleção ou prazo**, no padrão `Be careful on [data]` ou `Don't tell anyone`
O `no captions` do negative **continua correto e não muda**: texto de tela nunca é gerado na imagem.
Os números (`222`, `11:11`) entram pequenos no canto como marca d'água de canal, não como pedido; o
pedido continua vindo na fala, na ordem do P7.

- **Nota silenciosa de 0 a 10** em impacto visual, scroll-stop, movimento/transformação,
  curiosidade, originalidade, clareza visual, aderência ao nicho e viabilidade. Impacto visual e
  scroll-stop são decisivos. Ideia fraca é substituída ANTES de entregar, nunca entregue com ressalva
- Formato: nome curto, `Cena` em 1 ou 2 frases, `Por que para o scroll` em 1 frase, mais a variável
  trocada e o invariante da família. **Zero prompt aqui**
- As três travas do ângulo: **rosto nunca revelado**, **carta na mão depois do gancho**, **registro divino**

### P4.1 · [ÂNGULO 3] Assim que o Luigi APROVAR o roteiro com o gancho fiel (validação) ou ESCOLHER os ganchos (variação), ANTES de qualquer prompt
- `producao/_flow/INSTRUCOES_AGENTE_FLOW.md` → **colar o bloco INTEIRO no chat, toda vez.**
  É o item 1 do pacote e vem antes do primeiro prompt de imagem. Sem atalho, sem "permanece a mesma"

### P5 · Ao receber "roteiro aprovado" e `/produzir`, ANTES do primeiro JSON
**Executar a skill não substitui ler.** A skill é a ordem, isto aqui é o conteúdo:
- **O gabarito vivo:** `producao/fitywell_pernas/ROTEIRO.md` e `PROMPTS_PRODUCAO.md`
- **[FITYWELL] `PLAYBOOK_FITYWELL.md`** → fila de avatares, pacote por ACTIVE, blocos do Flow, gancho pelo Puzzle
- `workflow-entrega-gabarito` → as 8 coisas que eu perdi ao parar de conferir
- **`GATE_VISUAL.md` Partes 1 a 3, em TODOS os ângulos** → realismo, herói colado na lente e trechos prontos
- **`GATE_VISUAL.md` Parte 6 → escrever `FICHA_FRAMES.md` com o placar ANTES do primeiro JSON**, olhando
  cada frame do modelo em `input/frames_modelo/`. O K se escreve a partir da ficha, nunca da memória
- `checklist-composicao-visual` → os 10 itens (o porquê; a versão executável é o `GATE_VISUAL.md`)
- `realismo-anti-cara-de-ia` → os 7 itens do gate de realismo
- `prompts-imagem-json` → campos e blocos padrão
- `erros-recorrentes` → falhas 1 a 7 de geração de imagem
- `avatares-fichas` → traços canônicos e **caminho da âncora**
- `feedback-prompt-imagem-compartilhado` → um keyframe por SETUP, nunca por take
- `feedback-enquadramento-mais-proximo`

### P6 · ANTES de escrever os prompts de VÍDEO (portão que não existia)
- `prompts-video-fase7` → os 5 blocos, e a exceção da regra da fala
- `PLAYBOOK_COMPLETO/11_insights_otimizacao.md` seção 3 → **menos é mais na descrição da ação**, combinação de elementos é o gatilho invisível de moderação, o prop fiel é o ambíguo
- `restricoes-protocolo` → escrever já evitando o que costuma travar

### P7 · [ÂNGULO 3] ANTES do CTA de STORIES
- `PLAYBOOK_MESTRE_AURALY.md` §18 → ordem `222 → save → follow → Stories`, os dois modos declarado/curiosidade, as 3 telas
- `producao/_stories_auraly/STORIES_PADRAO.md` → **os 9 fechamentos validados, as 3 telas do Stories
  e o `rt_ad` do Stories.** O CTA de Stories entra DEPOIS do `222` (o SELO vem antes do destino)
- `banco-obstaculos` → objeções antecipadas
- **Preço: NUNCA dito no Ângulo 3**, nem "one-time", nem "pagamento único", nem valor. Mesmo que o vídeo modelo cite preço, ao clonar o beat de preço é cortado (Luigi, 2026-09-07)

### P8 · Se travar restrição de geração
- `restricoes-protocolo` → **Regra #0: o Luigi já tentou, nunca sugerir retry**
- `PLAYBOOK_COMPLETO/09_troubleshooting_restricoes.md`

### P9 · Fechando a entrega
- **🔴 BLOQUEANTE, TODOS OS ÂNGULOS: rodar o CHECKLIST DE ENVIO** (memória `checklist-envio-prompt`,
  `GATE_VISUAL.md` Parte 5) antes de enviar qualquer gancho, `K__`, `V__`, pacote ou prompt avulso.
  Item reprovado = não envia, corrige e roda de novo. A entrega leva `Checklist de envio: X/X aprovados`
  fora dos blocos copiáveis (Luigi, 2026-09-22).
- **Ficha do frame:** a entrega leva `Ficha: N/N K, placar 14/14 cada` ao lado do checklist. No K do
  gancho, quando o Luigi mandar o resultado gerado, pontuar o resultado com F1 a F6 contra o frame.
- **RODAR O LINTER, e só fechar com zero FALHAS:** `python checar_entrega.py producao/<avatar>_<slug>`
  Ele checa do DISCO o que dá pra checar por máquina, então **não depende de eu lembrar de nada**:
  travessão na copy, keyword do ângulo, 13 a 29 palavras por take, fala do prompt igual palavra por
  palavra ao roteiro, JSON válido, bandeira dos EUA, `no captions`, termo sensível no negative,
  seções na ordem, nomenclatura T/K/V/REF, os 5 blocos do prompt de vídeo, instrução de patch,
  produto em quadro nos ângulos 2 e 3, e as travas do ângulo 3. Falso positivo se conserta no linter,
  nunca se ignora. Falhas de pacotes publicados antes da regra ficam na baseline
  (`controle/linter_baseline.json`, aparecem como `[HIST]`); falha nova sempre conta, e regenerar a
  baseline (`--todos --gerar-baseline`) só com decisão do Luigi.
- **Se a entrega mexeu em memoria, rodar `python checar_memoria.py`**: wikilink quebrado,
  memoria fora do indice, drift do espelho. O `pre-commit` bloqueia, mas rodar antes evita surpresa
- `feedback-prompts-na-conversa` → arquivo E chat, linha curta antes de cada prompt
- `feedback-roteiro-final` → roteiro final em inglês por último
- Gate final da skill `/produzir`, colado preenchido

### P10 · DEPOIS que o vídeo for ao ar (o furo mais caro)
**Ninguém escreve nesses arquivos hoje, então eles envelhecem e eu repito rota sem saber.**
- Escrever no **LOG de rotação** de `banco-rotas-argumentativas`: data, vídeo, ângulo, rota, obstáculo
- Adicionar o vídeo em `biblioteca-videos` com o esqueleto usado
- **Registrar a publicação em `controle/resultados.json`** com `python gerenciar_operacao.py registrar`
  (formato em `controle/README.md`), e de novo a cada coleta de métricas. Sem isso nenhum teste de
  gancho (controle contra degrau) tem resposta. Pedir ao Luigi os números quando ele confirmar a postagem
- **Rodar `python checar_rotacao.py`**: lista o que esta em `producao/` e nao foi registrado no log
  nem na biblioteca. Avisa, nunca reprova, porque o casamento e por heuristica
- **Rodar `python grafo_memoria.py` e `python grafo_producao.py`** para o grafo entrar fresco
- Se alguma prática foi revogada no caminho, **editar a memória velha**, nunca só adicionar

## Onde está o resto

Copy e estratégia estão na memória em `~/.claude/projects/.../memory/`:
`banco-rotas-argumentativas` (fechamento) · `banco-obstaculos` · `angulo2-copy-fitywell` · `feedback-ponte-argumentada` · `metodo-puzzle` · `restricoes-protocolo` · `erros-recorrentes` · `avatares-fichas`

### Montar tudo num PC novo

`SETUP_NOVO_PC.md` tem o caminho inteiro, do clone ate o grafo. O passo que ninguem adivinha e o
`restaurar_memoria.ps1`, porque o clone traz o espelho `memoria/` e **nao** traz a memoria viva,
que mora fora do repo. Sem ele o agente nasce com o processo inteiro e zero copy.

### Espelho da memória no repo, e a regra que vem junto

A pasta `memoria/` deste repositório é um **espelho versionado** da memória viva, para backup e
histórico. **A fonte de verdade continua sendo `~/.claude/projects/.../memory/`.** Nunca editar
`memoria/` na mão, nunca ler dela para decidir nada.

**Antes de todo commit que envolva memória, rodar:**
```
bash sync_memoria.sh                                        # macOS / Linux
powershell -ExecutionPolicy Bypass -File sync_memoria.ps1   # Windows
```

Existe pelo mesmo motivo do PORTÃO P10: documento que ninguém atualiza envelhece em silêncio, e
espelho desatualizado é pior que espelho nenhum, porque parece confiável.

---

## ÂNGULO 3 (Auraly), o que muda em relação aos Ângulos 1 e 2

**O PROCESSO É O MESMO. Nada aqui substitui o fluxo validado.** `/watch` no modelo, método puzzle,
mesma cabeça de copy, mesma ordem de entrega, mesma estrutura de prompts, mesmas travas de realismo,
mesmos 5 blocos no prompt de vídeo. Só troca o que é **do produto**. Doutrina em `angulo3-copy-auraly`,
banco de copy do nicho em `angulo3-swipe-padroes` (o equivalente ao `angulo2-copy-fitywell`).

**Duração, número de takes e gramática visual saem do VÍDEO MODELO**, como sempre. Não existe formato
fixo do ângulo. Se o modelo tem 66s e um reveal mudo de 8s, o clone tem 66s e o reveal mudo. Se o
modelo tem split screen, o clone tem. Fidelidade de estrutura é a regra de sempre.

**Keyword `222`** no lugar de `yes`.

**Não mostra produto.** O objeto de desejo do CTA é **o rosto da alma gêmea**, nunca o app: ela mandou
uma mensagem ao universo, o universo respondeu, e **o rosto está esperando no STORIES**.
O vídeo nunca diz quiz, teste, app, plano nem preço.

**🔄 A INVERSÃO DO FUNIL: o destino é o STORIES, e as três ações viraram o SELO** (Luigi, 2026-09-04).
Palavras dele: *"quase 100% de foco em fazer a pessoa clicar na minha foto de perfil e checar meus
stories, pois a revelação vai estar lá e não na DM."*
- ♻️ **Revoga três regras de 2026-09-01:** ~~o Stories é degrau 2 e lacra a imagem do rosto~~,
  ~~o CTA de Stories é ADITIVO~~ e ~~a DM entrega o rosto~~. **O Stories é a SALA**, e desde
  2026-09-22 o **único destino**: não há mais automação de DM (Luigi). O CTA falado não muda.
- **🔒 A LEI DO SELO (Luigi, 2026-09-04): toda ação pedida carrega a CONSEQUÊNCIA dela, nunca um
  rótulo.** `222` = *"that's how this gets tied to your name"* · like e save = *"and the blessing
  coming to you gets stronger"* · follow = *"so this stays open"*. Três travas:
  **(a)** a frase diz o que a ação provoca **no que já está vindo pra ela**, pra ela querer fazer
  sozinha; **(b)** ⚠️ a consequência tem que ser **congruente com o GESTO REAL**, e comentar é
  **escrever**, então amarra ao nome e **nunca** "fala em voz alta" (erro cortado pelo Luigi);
  **(c)** poucos pedidos, uma linha cada, agrupando quando couber. Lista longa lê como pedido de
  engajamento e mata o efeito. Detalhe em `angulo3-swipe-padroes`.
- ⚠️ **O follow gate perdeu o motivo TÉCNICO e ganhou o motivo do CAMINHO.** *"or it will not let me
  reach you"* era condição de entrega da DM. **Follow sem motivo nenhum continua proibido.**
- ⚠️ **O comentário vem PRIMEIRO, o Stories depois. A razão mudou, o gate não:** o SELO vem antes do
  DESTINO, porque o tap tira ela do vídeo e quem sai pode não voltar pra comentar.
  Se o roteiro estiver curto, fundir no formato do IG14: *"Comment 222, and tap my profile picture to
  watch my stories now."*
- **NOMEAR o rosto ≠ ENTREGAR o rosto.** Esta trava não mudou e é a que sobrou inteira da trava dura:
  o Stories **nomeia** a revelação e **nunca sobe imagem de rosto**, nem obscurecida. O botão entrega.
- **🎚️ Os DOIS MODOS continuam, mas a balança pendeu pro DECLARADO.** **DECLARADO** (*"their face is
  already sitting in there"*) quando a copy **já entregou prova concreta de identidade**: a inicial, o
  traço, o timing, o truque do WhatsApp, ou o instante do pensamento (*"the person who came into your
  head the second I said that"*). **CURIOSIDADE** virou exceção, e só cabe quando a promessa foi
  atmosférica do começo ao fim. **Declarado obriga o Story a ser sobre o rosto**, senão ela sai na
  primeira tela, e o claim vira cobrável.
- **Custa zero keyframe e zero clipe:** fala mais legenda mais seta de edição no CapCut. Cabe até em
  pacote já fechado.
- Nove fechamentos validados, as 3 telas do Stories e o `rt_ad` do Stories em
  `producao/_stories_auraly/STORIES_PADRAO.md`. **É o P7 agora.**

**Ângulo de entrada é livre, a ponte pro rosto é obrigatória.** **Roster ativo desde 2026-09-22 =
SÓ TRÊS: Walt Hensley (homem, 58), Darlene Pruitt (mulher, 56) e Lorraine Vance (mulher, 52)**, cada
um numa conta só. ♻️ **2026-09-30: entrou a Morgan Vance** (mulher, ~25, conta orgânica nova, âncora
`producao/_ancoras/morgan_vance_ancora.jpg`). Ficha na seção ROSTER AURALY ATIVO de `avatares-fichas`. O eixo de variação é
**1 esqueleto × N ângulos de entrada × os avatares anexados na produção** (a fila é sempre o que o
Luigi mandou). ♻️ Todos os avatares anteriores do ângulo foram **descartados** na limpeza de
2026-09-22: fichas, âncoras e pacotes estão em `_arquivo/2026-09-22_limpeza_angulo3/`, que nunca é
fonte de produção.

**Registro: divino, nunca oculto.** Ver a lei em `angulo3-copy-auraly`.

**🃏 Depois do take do gancho, o avatar segura a CARTA SOULMATE** (casal ilustrado, palavra SOULMATE na
faixa da base, borda metálica holográfica, arte saturada) e a mantém na mão até o fim. Gerar uma vez como `REF-CARTA` e anexar sempre, igual
o Ângulo 1 faz com o `product.png`.

**🚫 O ROSTO NUNCA É REVELADO NO VÍDEO.** A revelação vive no **Stories**, e quem entrega é o botão do
link (~~"só na DM, e só depois do `222`"~~, revogado em 2026-09-04). Qualquer gancho que envolva
retrato, foto, polaroid ou desenho tem o rosto **obscurecido**: impressão fora de foco, vidro fosco,
revelação parcial, silhueta, gelo ou névoa. **Descrever sempre como propriedade física do objeto**,
nunca como blur de câmera, senão colide com o `no blur` do negative.

**Âncoras:** Walt em `producao/_ancoras/walt_hensley_ancora.jpg`, Darlene em
`producao/_ancoras/darlene_pruitt_ancora.jpg`, Lorraine em `producao/_ancoras/lorraine_vance_ancora.jpg`.
A âncora oficial é a **imagem de teste em cena real, não fingerprint** (Luigi, 2026-09-22): não gerar
fingerprint para estes três. Anexar a do avatar escolhido como
referência de identidade e cenário em **todo** `K__`. Como o bloco do Flow é autossuficiente (GOOGLE
FLOW DELIVERY FORMAT), cada `K__` descreve o cenário inteiro por escrito (ficha em `avatares-fichas`).
♻️ **Avatar fixo por conta (Luigi, 2026-09-25), nos três ângulos:** a roupa e o cenário-base da âncora
se repetem em todo vídeo e todo gancho da conta; o que varia é o conteúdo e o ângulo de câmera. Só o
movie style / short form não tem avatar fixo. Revoga o cenário e a roupa próprios por gancho do Auraly.

**📎 SINAL DE ENTRADA: `.mp4` + IMAGEM DE AVATAR na mesma mensagem = produzir PARA AQUELE AVATAR primeiro.**
Quando o Luigi manda o vídeo modelo junto de uma âncora, a âncora **diz para quem é**. Não perguntar,
produzir para ela. O ciclo completo (roteiro, ganchos, prompts) sai para esse avatar antes de qualquer outro.

**Depois de fechar o primeiro, o MESMO vídeo modelo pode rodar no próximo avatar**, com:
- **Ajustes de COPY para congruência com o novo avatar.** ⚠️ **Não é copiar palavra por palavra.**
  Idade, gênero e registro mudam o que soa crível na boca de cada uma. Ver `congruencia-matriz`.
- **Ajustes nos prompts de imagem e de vídeo** (identidade, cenário, registro de voz, rastreio).

**PASSO EXTRA (TODOS OS ÂNGULOS desde 2026-09-22: Korella, FityWell e Auraly): sugestões de GANCHO VISUAL antes dos prompts.**

> ♻️ **2026-09-23 (Luigi): este passo só roda na RODADA DE VARIAÇÃO**, sobre um vídeo que já
> performou no perfil dele. Produção nova é rodada de validação: gancho fiel ao modelo, sem as 10.
> O "por que" abaixo continua certo, mas o "roteiro validado" dele é validado **no nosso perfil**,
> não no perfil de quem viralizou. `GATE_VISUAL.md` Parte 4, Passo 0.

♻️ **2026-09-22 (Luigi): a etapa vale também no Ângulo 1 (Korella)**, pelo mesmo `GATE_VISUAL.md` Parte 4.
Travas iguais às da FityWell, porque o herói do hook também carrega argumento: congruência com a fala
do T1 é gate, clickbait puro é proibido, eixos de troca **ingrediente e alvo**. Diferença da Korella:
o produto aparece, então o frasco nunca é a variável trocada e continua em quadro onde o roteiro pede.
Depois do roteiro aprovado e **antes de entregar qualquer prompt**, mandar sugestões de variações de
gancho visual derivadas do mesmo vídeo modelo. **A copy fica idêntica, só os primeiros segundos mudam.**

*Por que:* neste ângulo a copy é o ativo e o gancho visual é descartável. Ele existe só pra parar o
scroll e fazer ela ouvir. Um roteiro validado vira N vídeos trocando só o hook. E como o Ângulo 3
não precisa segmentar público, gancho de clickbait puro converte, então isso é vantagem e não risco.

♻️ **EDITADO EM 2026-09-10 (Luigi). A etapa de variações VALE TAMBÉM NA FITYWELL**, ângulos 2 e 4.
A versão antiga dizia que não valia nos Ângulos 1 e 2 porque o herói do hook carrega argumento. O que
está errado ali é a conclusão, não a premissa: **o herói realmente carrega argumento, e é por isso
que a variação é feita pelo MÉTODO PUZZLE em vez de ser inventada do zero.**

**A DIFERENÇA ENTRE OS DOIS MODOS DE VARIAR O GANCHO:**

♻️ **A coluna do Ângulo 3 foi REESCRITA duas vezes em 2026-09-20.** A versão original dizia que ali
a ideia nascia de invenção pura e que o gancho preservava *nada*; a amostra medida derrubou isso,
porque 81% dos virais do nicho são oito esqueletos repetidos com uma variável trocada. **Decisão
final do Luigi na mesma data: o Ângulo 3 passa a usar o MESMO método do Ângulo 2**, ou seja Puzzle
aplicado ao hook do vídeo modelo. Não são mais "dois modos de variar": é **um método só**, com três
travas diferentes entre as marcas.

| | **Ângulo 3 (Auraly), desde 2026-09-20** | **Korella e FityWell (Ângulos 1, 2 e 4)** |
|---|---|---|
| Origem da ideia | **Puzzle aplicado ao hook do vídeo modelo** | **Puzzle aplicado ao herói do hook** |
| O que se preserva | **a AÇÃO ESTRUTURAL do hook original** | **a AÇÃO ESTRUTURAL do hook original** |
| O que muda | **UMA variável por hook** | **UMA variável por vez** |
| Eixos de troca | objeto, substância, local, cor, resultado, marcador, alvo | **ingrediente e alvo** |
| Distribuição | 1 controle + 9 com o degrau, MESMO esqueleto | 1 controle + 9 com o degrau, MESMO esqueleto |
| Papel do banco | **controle de repetição**, nunca fonte da ideia | não se aplica |
| Clickbait puro | liberado, vai no fim e marcado | **proibido, quebra o argumento** |
| Congruência | trava só na **fala**, não no objeto do gancho | **gate, entra antes de mostrar** |
| Estrutura do T1 | 1 K + 1 V, mas **com os cortes escritos dentro do `V__` e o T1 mudo** (ver P4) | 1 K + 1 V, take normal de 8s |

**Como pensar na prática**, exemplo dado pelo Luigi em 2026-09-10. Herói do hook original: um homem
velho joga bicarbonato em cima de um modelo anatômico de intestino. A ação estrutural é
`avatar joga UM PÓ em cima de UM MODELO ANATÔMICO`, e ela não se toca. As variações trocam uma
variável de cada vez:

1. o avatar joga canela em cima da **própria barriga** (troca o alvo)
2. o avatar joga bicarbonato em cima de um modelo anatômico de **outro órgão**, se houver congruência
3. o avatar joga **canela** em cima do modelo de intestino (troca o ingrediente)
4. o avatar joga **coca-cola** em cima do modelo de intestino (troca o ingrediente e o estado, de pó
   para líquido)

**Os dois eixos de troca são o INGREDIENTE e o ALVO.** Trocar os dois ao mesmo tempo já é gancho
novo, não variação, e sai da etapa.

**A trava que continua valendo:** cada variação precisa continuar congruente com a fala do T1, porque
o herói carrega argumento. Variação que obriga a reescrever a copy foi longe demais e é reprovada
antes de aparecer. Marcar sempre **qual variável foi trocada** em cada sugestão.

**Entregar 10 variações** (dez, fixo desde 2026-09-08), **todas do mesmo esqueleto**, que é o hook
do vídeo modelo **subido um degrau** (HOOK 1 é o controle sem degrau, `GATE_VISUAL.md` Parte 4), ordenadas por congruência e com clickbait puro no fim e marcado (no Ângulo 3, onde
ele é liberado). `producao/_swipe_auraly/BANCO_GANCHOS_VISUAIS.md` continua sendo o P4, mas como
**controle de repetição e padrão de qualidade, nunca como fonte da ideia**. Os 13 mecanismos antigos
seguem como seção HISTÓRICA no mesmo arquivo, para checar repetição.

**O formato das contas do Ângulo 3 é PLANO ÚNICO, com UMA exceção: o T1.** Câmera na altura do peito
do outro lado da mesa: a avatar do peito pra cima em cima, a mesa no terço inferior do MESMO quadro,
e **ela executa a ação do gancho com as próprias mãos**. É a regra 1 do
`checklist-composicao-visual`: herói no lower foreground, mais perto que o rosto.
♻️ **Exceção aberta em 2026-09-20, só no T1:** ali o gancho tem **mudanças de plano dentro do mesmo
clipe**, escritas no prompt de vídeo e geradas pelo Veo, com **corte para macro das mãos obrigatório
no instante do payoff** e **split vertical liberado** (rosto em cima, ritual embaixo). O que a regra
antiga proibia (close isolado, B-roll separado) é justamente o motor do scroll-stop, e agora ele
cabe no mesmo take em vez de virar clipe separado. **Do T2 em diante o plano único segue obrigatório
e sem exceção.**
O gancho vive no **T1**. Do T2 em diante ela segura a carta e os takes **se reaproveitam** entre
variações, então cada gancho novo continua custando **só 1 keyframe + 1 clipe**.

**DM:** não existe mais (Luigi, 2026-09-22, sem automação de DM). Sem `DM.md`, sem DM padrão, sem
`rt_ad` de DM. O CTA de comentário `222` continua nos vídeos exatamente como está.
O `banco-rotas-argumentativas` e o `banco-obstaculos` continuam disponíveis para os beats de fechamento.

---

## ÂNGULO 4 (Body Hacks For Men), o que muda em relação aos outros

**O PROCESSO É O MESMO.** `/watch` no modelo, método puzzle, mesma ordem de entrega, mesma estrutura
de prompts, mesmas travas de realismo, mesmos 5 blocos no prompt de vídeo, **DOIS arquivos** (o
Ângulo 3 também não tem `DM.md`, desde 2026-09-04). Duração, número de takes e gramática visual saem do vídeo modelo.
Só troca o que é **do produto**. Doutrina completa em `angulo4-copy-bodyhacks`.

**Produto:** `Body Hacks for Men 40+`, marca **FITYWELL** (mesma casa do Ângulo 2), um **PLAYBOOK
DIGITAL** de **42 hacks de HÁBITO** em 7 áreas, 4 linhas e 2 minutos cada. Homens 40+ dos EUA.
Landing: `https://bodyhacksformen.netlify.app/` · checkout **Hotmart embutido na própria página** ·
**$9.90 uma vez**, ancorado em $47 launch price, sem renovação, garantia de 30 dias.

**⚠️ NÃO são receitas ancestrais e NÃO é testosterona.** Foi a descrição inicial, e a landing
desmentiu no mesmo dia. Os hacks são hábito e estratégia. Ler a seção 0 da doutrina antes de escrever
qualquer copy, porque prometer receita e entregar hábito **quebra no clique**, que é o pior lugar.

**Avatares: Dana Morrison (52), Jamie Anderson (55) e Lynn Parker (70), e eles são PAR, não coach**
(Luigi, 2026-09-10). Homens negros americanos, os três acima dos 50, falando com homens 40+.
**1ª pessoa liberada:** "when I hit fifty", e no Lynn "in forty years of this". A prova social
agregada empilha por cima. ♻️ **2026-10-02: a holistic.brandon VOLTOU ao Ângulo 4 (Luigi), como
COACH**, com a moldura dela de 2026-08-27 (autoridade por volume observado, nunca idade vivida, e UM
beat de testemunha feminina por roteiro, só na boca dela). Nos três homens o beat continua morto. Fichas, âncoras e a substituição
em teste (relato de casal em 1ª pessoa) em `avatares-fichas` e na seção 7 de `angulo4-copy-bodyhacks`.

**Keyword `yes`**, decidida pelo Luigi em 2026-08-27.

**MOSTRA produto: livro FÍSICO como prop**, nunca print de tela nem mockup. Gerar uma vez como
**`REF-LIVRO`** e anexar sempre, igual o Ângulo 1 faz com o `product.png`. **O nome nunca vem
sozinho**, sempre colado ao descritor, no mesmo take e no mesmo gesto de levantar o livro.
**Mas a FALA nunca promete objeto físico**, porque o produto é digital com entrega instantânea. De
preferência o CTA diz que ele lê hoje à noite, no celular.

**🚫 LIMITE HONESTO É BANIDO.** Ver a regra na lista acima.

**🚫 NUNCA CULPAR A MASCULINIDADE DELE.** Espelho da regra do Ângulo 2 (lá era o esforço dela).
Zero "você se deixou levar", zero "você parou de se cuidar", zero cobrança pelo que ele era aos 25.
Vergonha é o que trava esse cara. O álibi é **o cano e a mesa, nunca o homem**.
**Crivo antes de entregar:** *"essa copy sugere, em algum ponto, que ele deixou isso acontecer?"*

**🔑 ED É O EIXO PRINCIPAL DE TODO VÍDEO DO ÂNGULO 4** (decisão do Luigi, 2026-08-27, reafirmada
depois da análise da landing). A página sustenta: Men's Vitality é uma das 7 áreas e tem 6 hacks só
dela, então "vários body hacks que resolvem isso" é verdade. **A promessa é ED, o mecanismo é o
mostrador, e o produto é "vários hacks só pra isso mais 40 pro resto".** O mecanismo não esvazia a
promessa, ele explica por que tudo que ele tentou falhou. Base fixa, variando a cada roteiro:
promessa de ED → o mostrador → vários hacks pra isso no livro → comenta `yes` → eu mesmo mando na DM.

**No CTA: `fix`, nunca `treat` nem `cure`** (o rodapé da landing diz que o produto não trata nem cura,
e "the hacks for this" tem a mesma força sem o claim médico). E **cuidado com "eu te mando o livro"**:
a DM entrega link de uma página de $9.90, não o livro de graça, e é o mesmo erro do "it is free" do
Ângulo 2. **Dizer o preço joga a favor**, porque $9.90 com garantia de 30 dias mata a suspeita de
upsell antes dela nascer.

**A PONTE já está escrita dentro do produto, usar ela:** *"drive is a readout, not the problem"*
(hack 39). Ele vinha tentando consertar o mostrador, e é por isso que nada pegou, inclusive o que vem
em frasco. O motor é **sono, carga e cintura**, e são as três que ele controla sem receita.
**Nunca usar a estrutura das 3 causas do Ângulo 2 aqui**, e nunca a ponte de testosterona: a própria
página rejeita o frame hormonal por escrito.

**O ÁLIBI também já está na página:** *"It's not your age. It's your playbook."* Mais a tabela
25 playbook contra 40+ playbook, que é device de copy pronto.

**O vazamento do ângulo, e o que o fecha:** o vídeo entrega um hack de graça e o produto tem 42.
O que fecha é que **um hack conserta uma área e ele não sabe qual é a dele**, e que fazer mais coisa
certa isolada **é o playbook dos 25**, que é justamente o erro que o produto nomeia.

**A PONTE VERBAL com a página é obrigatória.** A landing é contida, nunca diz ED, o termo dela é
**`drive and confidence`**. O vídeo pode ser mais quente, mas **o CTA tem que aterrissar nessa frase**,
senão ele cai numa página que não parece falar do que ele acabou de ouvir.

**Vocabulário, quem pode dizer o quê:** `champion`, `your soldier` e "the part of you that stopped
answering" são liberados na boca dele. **`johnson` NUNCA sai na fala**, só em legenda: o motivo de
registro caiu com o avatar masculino, mas o classificador lê o token igual, então segue proibida até
o Luigi decidir. Nome clínico de órgão nunca, em lugar nenhum. ♻️ **O beat de testemunha feminina foi
CORTADO em 2026-09-10**, junto com a Brandon.

**2ª pessoa em cena é homem 45+.** Tratamento no hook: `brother`, `man`, `my guy`.
Nunca `ma'am`, `girl`, `honey`.

## graphify, o grafo de conhecimento da operacao

> ⚠️ **2026-09-22: `graphify-out/` NÃO existe neste Mac.** Enquanto não for reconstruído, pular esta
> seção e consultar as fontes locais (regra do topo deste arquivo). Os portões nunca dependeram dele.

O grafo em `graphify-out/` cobre `memoria/`, `PLAYBOOK_COMPLETO/` e `producao/`:
**1434 nos e 2802 arestas** depois da rodada de 2026-09-01 (`grafo_memoria.py` + `grafo_producao.py`).
Ele liga doutrina a execucao, entao responde coisas que nenhum arquivo sozinho responde: qual rota ja
foi usada em qual video, onde uma regra foi aplicada, se um esqueleto ja rodou.

> ⚠️ **As COMUNIDADES e o `GRAPH_REPORT.md` estao ATRAS da contagem acima.** Os dois scripts sao
> deterministas e so mexem em nos e arestas; comunidade e relatorio pedem reconstrucao semantica,
> que custa subagentes. Ate la, tratar agrupamento e relatorio como datados. Contagem de nos e
> arestas esta fresca.

**Quando o grafo existir, consultar ANTES de responder perguntas amplas sobre a operacao.**

- `graphify query "<pergunta>"` devolve o subgrafo relevante, mais barato que abrir os arquivos.
  Se o resultado vier truncado, subir com `--budget 1500`.
- `graphify path "<A>" "<B>" --undirected` mostra como duas coisas se ligam.
  **O `--undirected` e obrigatorio**: sem ele a busca e direcionada e responde "no path"
  mesmo existindo caminho.
- `graphify explain "<conceito>"` abre um no e a vizinhanca dele.
- `graphify-out/GRAPH_REPORT.md` so para visao geral, nunca como primeira parada.

**O grafo NAO substitui os PORTOES DE CONSULTA.** Ele orienta e cruza; os portoes mandam ler o
arquivo inteiro. Quando o portao diz "ler `producao/fitywell_pernas/ROTEIRO.md`", e ler o arquivo,
nao perguntar ao grafo sobre ele. Precedencia: **PORTAO > grafo > lembranca**.

**Nos com nome de caminho** (`memoria/banco_obstaculos.md`, `memoria/`) sao o esqueleto documental,
nao conceitos. Servem de indice e garantem que nenhum no fique orfao. Ignorar na leitura de conteudo.

**O grafo envelhece igual a memoria, e pelo mesmo motivo do PORTAO P10.** `graphify update` aqui e
AST-only e ignora markdown, entao **nao adianta** neste projeto. Depois de mexer em `memoria/` ou
fechar uma producao, o grafo fica defasado ate uma reconstrucao semantica, que custa subagentes.
Enquanto isso, tratar resposta do grafo como **datada**, e conferir no arquivo o que for decisivo.
