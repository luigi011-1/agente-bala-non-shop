# Escopo vigente: referencia criativa Auraly

**Processo e estado: somente WORKFLOW_AURALY.md, conforme AGENTS.md.** As instrucoes de processo,
execucao, precedencia e formato de entrega preservadas abaixo sao historicas, inclusive os
avisos que chamam este playbook de operacional. Consultar aqui apenas inteligencia criativa
requerida pela etapa atual. Nao reativar Studio/browser nem aplicar um roteiro de venda a uma
producao explicitamente aprovada como GROWTH. O checkpoint identifica objetivo e avatar.

---

# PLAYBOOK MESTRE DE PRODUÇÃO AURALY

> ## ♻️ SOBRESCRITA DE 2026-09-08 (Luigi), lê antes de qualquer seção deste arquivo
>
> **Auraly Studio, bridge local, extensão Chrome, execução automática no ChatGPT, preflight,
> browser queue, batch, `pacote_browser` e os Modos A / B / C estão DESCONTINUADOS.**
> A **seção 13** deste playbook é **HISTÓRICA** e não define mais nada. Eu não gero imagem, não abro
> navegador e não executo Flow. Minha função termina no pacote de prompts.
>
> **O workflow voltou ao padrão dos Ângulos 1 e 2** (formato, não conteúdo): `.mp4` + âncoras →
> análise → transcrição → estrutura da copy → roteiro → aprovação → **10 ganchos** → escolha →
> pacote final.
>
> **O pacote final começa pelo bloco `INSTRUÇÕES PARA A MEMÓRIA DO AGENTE — GOOGLE FLOW AI`**
> (`producao/_flow/INSTRUCOES_AGENTE_FLOW.md`), obrigatório antes de qualquer prompt, e segue com
> prompts de imagem, prompts de vídeo, body, CTA, transcrição final EN e transcrição final PT.
>
> Do resto deste playbook continua valendo tudo que é **criativo e visual** do Ângulo 3: público,
> oferta, linguagem, copy, avatares, kit do tarólogo, REF-CARTA, travas de reveal, estrutura de
> roteiro e Stories. Regra em `CLAUDE.md`, seção "LIMITE DA MINHA FUNÇÃO E ORDEM DA ENTREGA".


> **Origem:** escrito pelo Codex e entregue pelo Luigi em 2026-09-07. Esta é a cópia versionada no
> repo, com quatro correções aplicadas na mesma data, todas marcadas no texto: preço nunca é dito
> (§4.3), o `negative` da REF-CARTA sem as linhas anti-glow e com a lista de símbolos góticos (§10),
> o playbook entra na precedência acima do `AURALY_AGENT.md` (§26), e o portão P1 antes do Gate 1
> (§5, "Gate 0"). ♻️ **Desde 2026-09-14 é referência CRIATIVA, não roteador:** processo, estado e formato
> do Ângulo 3 vivem em `AGENTS.md` → `WORKFLOW_AURALY.md` → `CHECKPOINT.md`. Em conflito, o workflow vence.

## Agente de vídeos de venda do app de manifestação Auraly

**Escopo exclusivo:** este documento serve somente para produzir vídeos de venda do aplicativo de manifestação e leitura de alma gêmea **Auraly**, chamado internamente de **Ângulo 3**. Ele não deve ser usado para nutracêuticos, FityWell, Korella, Body Hacks, e-commerce genérico, vídeos de crescimento ou qualquer outro produto.

O objetivo é permitir que qualquer IA execute o mesmo processo completo, com a mesma ordem, rastreabilidade, qualidade visual e velocidade operacional: analisar um vídeo vencedor, modelar sua estrutura pelo método Puzzle, validar a copy, propor ganchos visuais, produzir imagens por avatar no ChatGPT web, escrever prompts de vídeo para Flow/Veo 3.1, organizar os arquivos e entregar tudo também na conversa.

Este documento é operacional. Quando uma instrução antiga entrar em conflito com ele, use a regra mais recente registrada aqui. Em especial:

- A keyword do Auraly é `222`, nunca `yes`.
- O destino principal do vídeo é o **Stories**.
- **Não existe automação de DM** (Luigi, 2026-09-22). O Stories é o único destino; o CTA de comentário `222` continua igual.
- O comentário `222`, o follow e o save funcionam como um **selo com o universo**.
- O vídeo pode dizer que o rosto está nos Stories, mas não pode exibir o rosto da alma gêmea.
- O produto ou a interface do app não aparecem no vídeo.
- Prompts de imagem são JSON. Prompts de vídeo são texto simples.

---

## 1. Resultado final esperado

Uma produção concluída deve entregar:

1. análise do vídeo modelo;
2. transcrição fiel;
3. tabela do método Puzzle, mostrando o esqueleto preservado;
4. copy adaptada para o Auraly;
5. validação de copy e contagem de palavras;
6. opções de ganchos visuais para todos os avatares;
7. prompts completos de imagem em JSON;
8. imagens aprovadas, organizadas por avatar e data;
9. prompts de vídeo para cada take no formato Flow/Veo 3.1;
10. mapa de âncoras e continuidade;
11. instruções de montagem no CapCut;
12. gates de qualidade preenchidos;
13. roteiro final em inglês, numerado e corrido;
14. os mesmos conteúdos importantes enviados integralmente no chat.

O arquivo não substitui o chat. O chat não substitui o arquivo. Tudo que Luigi precisa ler, aprovar, copiar ou usar deve aparecer na conversa e ficar salvo no pacote local.

---

## 2. Comando de entrada: `/watch`

Quando Luigi enviar caminhos locais acompanhados de `/watch`, a IA deve iniciar o processo sem pedir o briefing longo.

Formato explícito aceito:

```text
/watch
video: C:\caminho\video_modelo.mp4
avatares:
- C:\caminho\avatar_1.jpeg
- C:\caminho\avatar_2.jpeg
```

Formato curto aceito:

```text
"C:\Users\luigi\Downloads\video_modelo.mp4"
"C:\Users\luigi\Desktop\AVATARES\avatar_1.jpeg"
"C:\Users\luigi\Desktop\AVATARES\avatar_2.jpeg"

/watch
```

Inferência:

- arquivo `.mp4`, `.mov` ou equivalente é o vídeo modelo;
- arquivos `.jpeg`, `.jpg`, `.png` ou `.webp` são âncoras de avatar;
- o nome do vídeo fornece o slug quando nenhum nome de produção for informado;
- como este playbook é exclusivo do Auraly, não é necessário perguntar o ângulo;
- novos avatares enviados no meio da produção substituem ou ampliam o roster sem reiniciar a copy.

O `/watch` autoriza as ações normais do pipeline: ler o vídeo e as imagens locais, extrair frames e áudio, analisar, escrever arquivos dentro da produção, abrir o Chrome definido neste documento, enviar as âncoras escolhidas ao ChatGPT web, gerar e baixar os assets e organizar os resultados nas pastas descritas aqui.

---

## 3. Regra de continuidade quando o avatar muda

O avatar pode mudar a qualquer momento. Isso não é erro e não inicia uma produção nova.

Quando chegar uma nova âncora:

- preservar vídeo modelo, esqueleto, copy aprovada, takes e cinco ganchos escolhidos;
- trocar identidade, características canônicas, roupa, voz e arranjo de cenário;
- gerar um lote novo para o avatar vigente;
- manter a mesma REF-CARTA aprovada;
- criar uma pasta final própria para o novo avatar;
- não misturar imagens ou nomes de avatares entre abas, prompts ou pastas.

---

## 4. Conceito comercial do Ângulo 3

### 4.1. Produto e público

- Produto: app Auraly, com leitura de mapa astral e revelação de alma gêmea.
- Público principal: mulheres nos Estados Unidos.
- Tráfego: orgânico, principalmente Instagram e Facebook.
- Objeto de desejo: o rosto, a identidade e o timing da alma gêmea.
- Mecanismo de crença: signo, posições planetárias reais do dia do nascimento, Vênus, Marte e Casa 7.
- Keyword: `222`.

Roster único desde 2026-09-22: **Walt Hensley** (homem, 58), **Darlene Pruitt** (56) e **Lorraine Vance** (52). Âncoras em `producao/_ancoras/*_ancora.jpg`, fichas em `avatares-fichas`. Todos os avatares anteriores foram descartados e só existem em `_arquivo/`. Imagem de avatar fora do roster: perguntar antes de produzir.

### 4.2. Funil atual

```text
vídeo
  -> selo: comentar 222 + seguir + salvar
  -> tocar na foto de perfil
  -> Stories com a revelação nomeada e o botão
  -> quiz
  -> email gate
  -> VSL
  -> pitch
  -> checkout
```

Sem automação de DM desde 2026-09-22. O roteiro dá todo o peso ao clique na foto de perfil e aos Stories.

### 4.3. O que nunca dizer no vídeo

Não mencionar:

- app;
- quiz ou teste;
- plano;
- assinatura;
- `one-time` ou pagamento único;
- preço, **sempre**. Decisão do Luigi em 2026-09-07: a modelagem Auraly **nunca** fala de preço, mesmo quando o vídeo modelo cita preço. Ao clonar, o beat de preço do original é substituído ou cortado;
- bruxaria, feitiço, pacto, invocação, `spell`, `witch`, `shield` ou manipulação de terceiros.

Existe inconsistência de cobrança nas páginas do funil. Portanto, nunca afirmar que é pagamento único ou que não existe assinatura.

### 4.4. Lei do registro

Tudo deve ser lido como **divino, manifestação, fé, bênção, sinal e lei da atração**. Nada deve parecer ocultismo sombrio, pacto ou controle sobre outra pessoa.

Vocabulário recomendado:

| Evitar | Preferir |
|---|---|
| spell, ritual, witch | prayer, intention, manifestation |
| shield | opening the way |
| protection circle | sealing your agreement with the universe |
| invoke, conjure | ask, declare, claim, receive |
| dark interference | timing, what was not ready yet |

O critério vale para texto e imagem. Cartas, cristais, vela, incenso e sal podem aparecer quando a leitura visual é de manifestação. Caveiras, corvos, serpentes, símbolos invertidos, sigilos e estética gótica de pacto ficam de fora.

---

## 5. Ordem obrigatória do workflow

Nenhuma IA pode pular diretamente da extração de frames para a geração de imagens.

### Gate 0: portão P1, antes de rodar a análise

Quando o projeto completo estiver disponível, antes do Gate 1:

- ler `memoria/biblioteca_videos.md` e checar se este esqueleto já foi clonado, qual variável foi trocada e o que não repetir;
- se o pacote já tiver `ROTEIRO.md` escrito, rodar `python checar_frases.py producao/<slug>` para comparar com os roteiros anteriores da mesma conta e apontar frase já queimada;
- registrar no chat o veredito do P1 (esqueleto novo, ou reuso e o que não repetir).

Fora do projeto, seguir só com o que der: pelo menos cruzar o nome do arquivo e a transcrição contra qualquer histórico disponível.

### Gate 1: análise do vídeo modelo

1. confirmar que o arquivo existe e é legível;
2. extrair metadados: duração, proporção, fps e resolução;
3. extrair áudio e transcrever sem adaptar;
4. extrair frames nos cortes e nos momentos de ação;
5. identificar todos os takes;
6. marcar cada take como `TALKING`, `B-ROLL`, `INSERT` ou `TRANSIÇÃO`;
7. identificar o herói visual do hook;
8. registrar cenário, posição de câmera, props, mudanças de estado e cortes escondidos;
9. distinguir movimento contínuo de uma sequência com cortes;
10. apresentar a análise no chat.

Não interpretar o hook apenas pelo tema. Olhar frame a frame para descobrir qual elemento realmente para o scroll.

### Gate 2: modelagem pelo método Puzzle

Antes de escrever a adaptação, montar a tabela:

| # | Beat | Original | Função | Adaptado Auraly | Variável trocada |
|---|---|---|---|---|---|
| 1 | Hook | o que é visto e dito | interromper o scroll | manifestação equivalente | prop ou promessa |
| 2 | Open loop | pergunta ou aviso | impedir saída | sinal ligado à espectadora | tema |
| 3 | Prova | evidência do original | aumentar crença | detalhe da leitura | mecanismo |
| 4 | Reveal parcial | algo quase aparece | elevar desejo | pista da alma gêmea | objeto |
| 5 | CTA | ação pedida | converter | selo + Stories | destino |

O esqueleto, a ordem e a função dos beats são preservados. Muda-se o mínimo necessário para encaixar o Auraly.

Teste obrigatório:

> Um estranho reconheceria que esta é a mesma estrutura do vídeo modelo, só que aplicada ao Auraly e ao novo avatar?

Se a resposta for não, a adaptação se afastou demais.

Regras do Puzzle:

- nunca transformar uma demonstração visual em talking head;
- nunca inventar beats que não existem no modelo;
- nunca remover um beat por parecer repetitivo;
- manter o mesmo tipo de tensão, reveal e transição;
- permitir enquadramento mais próximo, pois distância de câmera não é parte sagrada do esqueleto;
- adaptar props pelo significado funcional, não apenas pela aparência;
- usar fontes vencedoras frescas ou cross-niche quando houver escolha, evitando clones saturados do próprio nicho.

### Gate 3: lapidação da copy

A copy melhora cada beat sem redesenhar a estrutura.

Checklist do hook:

- relevância nas primeiras 10 a 20 palavras;
- consequência antes do mecanismo;
- loop que não entrega um final previsível;
- stakes claros;
- uma ou duas palavras emocionalmente fortes;
- linguagem simples e falada;
- coerência entre fala e herói visual;
- o objeto de desejo do Auraly já aparece ou começa a ser construído.

Checklist do corpo:

- cada frase avança o loop;
- o mecanismo é concreto e visualizável;
- há prova parcial, pista, timing, inicial ou traço;
- o roteiro não soa como anúncio;
- o avatar possui autoridade congruente com a fala;
- nenhuma frase depende de mostrar o app ou o produto.

Checklist do fechamento:

- a ponte para o rosto da alma gêmea está explícita;
- `222` vem antes do CTA de Stories;
- comentar, seguir e salvar possuem consequência espiritual clara;
- o follow mantém aberto o que foi selado;
- o save fortalece ou preserva o sinal;
- o CTA de Stories é congruente com o grau de revelação da copy;
- a urgência preferencial é `before they disappear`, porque Stories expira de verdade;
- não prometer entrega na DM como destino principal.

### Gate 4: aprovação do roteiro

Entregar no chat, nesta ordem:

1. transcrição do original;
2. leitura do vídeo e do herói do hook;
3. tabela do Puzzle;
4. roteiro cena a cena;
5. tabela bilíngue;
6. roteiro em inglês, só fala;
7. riscos e pontos de validação.

Aguardar aprovação explícita do roteiro antes dos prompts de imagem.

### Gate 5: seleção de ganchos visuais

Depois do roteiro aprovado, sugerir exatamente dez opções em um portfolio de três famílias
estruturais: quatro variações da família A, três da B e três da C. Esta distribuição `4/3/3` é
exclusiva do Auraly/manifestação/alma gêmea.

Antes de escrever, registrar: promessa e primeira linha; três famílias escolhidas; invariante de
cada família; única variável alterada em cada hook; anomalia dominante; arquitetura de captação;
desejo/perigo do texto de tela; marcador de seleção pessoal; significado adiado; resultado do gate
de impacto, legibilidade, congruência, repetibilidade e viabilidade.

Cada sugestão precisa conter:

| Campo | Conteúdo |
|---|---|
| Família | A, B ou C e a quantidade 4/3/3 |
| Invariante | composição, ação, timing, função psicológica e reveal preservados |
| Variável alterada | uma única mudança importante nesta versão |
| Anomalia | física, contextual, transformacional ou semântica |
| Mecanismo | revelar, apagar, quebrar, abrir, puxar, espalhar, cobrir, separar |
| Ação | mudança visível que ocorre no vídeo |
| Prop | objeto usado |
| Congruência | como o visual conversa com a fala |
| Texto de tela | desejo/perigo mais seleção pessoal; camada de edição, não texto no K/V |
| Significado adiado | pergunta que fica aberta para o próximo beat |
| Custo | quantidade de K e V |
| Risco | mãos, fogo, reflexo, moderação ou continuidade |
| Origem | validado, adaptação cross-niche ou novo teste |

Ordenar por família e, dentro dela, por força. Reprovar clickbait sem ponte semântica com a promessa.
Um VFX simples e único pode ser a anomalia; efeitos múltiplos ou cinematográficos são reprovados.

Exemplos válidos de mecanismos Auraly:

- revelação em areia preta;
- vela apagada e cera;
- carta puxada para a câmera;
- cadeado aberto por chave;
- círculo de sal transformado;
- carta virada;
- fumaça cobrindo a lente;
- carta sob água, pétalas, mel ou gelo;
- romã aberta;
- fileira de cartas varrida;
- retrato fisicamente obscurecido.

### Gate 6: geração por avatar

Somente após aprovação do roteiro e escolha dos ganchos:

1. gerar e aprovar a `REF-CARTA`, se ainda não existir;
2. abrir um lote para um avatar por vez;
3. produzir cinco hooks, um body e um CTA;
4. revisar todos os resultados;
5. mostrar o lote a Luigi;
6. aguardar `lote aprovado`;
7. baixar, renomear e organizar;
8. entregar os prompts Flow daquele avatar;
9. passar ao próximo avatar.

---

## 6. Estrutura de arquivos

### 6.1. Pasta de produção

```text
producao/<slug>/
  ROTEIRO.md
  GANCHOS_VISUAIS.md
  PROMPTS_IMAGEM.md
  MANIFEST.json
  watch/
  avatars/
  <avatar>_<YYYY-MM-DD>/
    imagens/
    referencias/
    PROMPTS_VIDEO_FLOW.md
```

A primeira linha de `ROTEIRO.md` deve ser:

```text
pipeline: auraly
```

### 6.2. Pasta final em Downloads

Após aprovação do lote:

```text
C:\Users\luigi\Downloads\<avatar_normalizado>_<YYYY-MM-DD>\
  imagens\
    01_hook_<slug>.png
    02_hook_<slug>.png
    03_hook_<slug>.png
    04_hook_<slug>.png
    05_hook_<slug>.png
    06_body.png
    07_cta.png
  referencias\
    REF-CARTA.png
  PROMPTS_VIDEO_FLOW.md
```

Normalização do avatar:

- minúsculas;
- espaços viram `_`;
- remover pontuação e espaços finais;
- preservar nome e sobrenome;
- data local no formato `YYYY-MM-DD`.

Nunca misturar lotes de datas ou avatares.

---

## 7. Nomenclatura operacional

| Prefixo | Significado |
|---|---|
| `T__` | take do roteiro, fala ou trecho de voz-over |
| `K__` | keyframe, imagem inicial de um setup |
| `V__` | clipe gerado no Flow |
| `REF-__` | referência auxiliar aprovada de pessoa ou prop |

Um keyframe pertence a um **setup**, não automaticamente a um take. Vários `T__` podem usar o mesmo `K__`. Cada take final recebe seu próprio `V__`.

Exemplo:

```text
K06 sustenta T2, T3 e T4.
V06 usa K06 e fala T2.
V07 usa K06 e fala T3.
V08 usa K06 e fala T4.
```

Novo `K__` somente quando houver:

- novo cenário;
- nova posição estrutural;
- novo ângulo de câmera;
- prop entrando ou saindo;
- mudança de estado que o original apresenta com corte;
- composição que não pode ser obtida pelo mesmo frame inicial.

Reveal contínuo dentro de um take usa uma única imagem do estado inicial. O movimento acontece no vídeo.

---

## 8. Âncora do avatar e identidade canônica

Antes de escrever os prompts, inspecionar visualmente a âncora e registrar:

- nome do avatar;
- faixa etária aparente;
- gênero e registro de voz;
- etnia/aparência relevante para continuidade;
- formato do rosto;
- cabelo;
- marcas, sardas, rugas e sinais;
- maquiagem ou ausência dela;
- roupa;
- joias, material e cor;
- mão com anel ou sem anel;
- cenário;
- arranjo do kit de tarólogo;
- posição da bandeira dos EUA;
- fonte e direção da luz;
- distância e altura de câmera.

Não inventar idade, biografia ou autoridade que contradiga a imagem. Se a âncora muda, a ficha também muda.

Em cada prompt, `reference_use` deve explicar exatamente o que cada anexo fornece. A âncora fornece identidade, rosto, roupa e identidade do cenário. Ela não obriga copiar pose ou enquadramento.

Para um `GERAR DO ZERO`, "mesmo cenário" significa a mesma identidade de ambiente e os mesmos objetos canônicos da âncora. A composição pode aproximar a câmera e mudar a pose para cumprir o setup. Para `EDITAR do K__`, cenário, objetos, posições, luz, câmera e enquadramento ficam literalmente idênticos, exceto pelas mudanças autorizadas no JSON.

Formulação recomendada:

```text
Use the first attached image ONLY for [AVATAR]'s face, identity, hair, skin texture, wardrobe and the identity of the real room. Preserve the same real environment and its established objects. Do NOT copy the pose, action or framing of the reference.
```

---

## 9. Kit visual obrigatório do tarólogo Auraly

Todos os keyframes com ambiente devem comunicar imediatamente que o avatar trabalha com leitura espiritual.

As sete categorias obrigatórias são:

1. cristais;
2. incenso aceso com fio fino de fumaça;
3. bandeira dos EUA visível e em foco;
4. cartas de tarô;
5. quadro astrológico, roda zodiacal, fases da lua ou carta natal;
6. cruz ou crucifixo;
7. vela branca.

Para manter realismo, não listar sete objetos como inventário solto. Agrupar em dois blocos:

- bloco da mesa/prateleira: cartas, cristais, incenso e vela;
- bloco da parede: quadro astrológico, cruz e bandeira.

Quando a âncora já traz o kit, preservar seu arranjo real. Não trocar posições arbitrariamente. Quando faltar uma categoria, a adição deve ser discreta e congruente, e passa a integrar o setup aprovado.

A separação entre avatares vem do arranjo fixo, não da presença das categorias.

---

## 10. REF-CARTA canônica do Auraly

A REF-CARTA é gerada uma vez, aprovada e reutilizada. Não regenerar por avatar.

Depois do gancho, o avatar segura a REF-CARTA na mão durante todo o corpo e o CTA. Gestos podem mudar por edição, mas a carta não desaparece, não troca de arte e não muda de escala.

Características obrigatórias:

- carta física de tarô;
- arte de casal ou conexão de almas;
- composição adulta, espiritual e sofisticada;
- cores saturadas e chamativas;
- borda metálica larga;
- acabamento holográfico com reflexo de arco-íris ou foil dourado;
- arabescos ou floreios gravados;
- faixa inferior com `SOULMATE` ou `TWINFLAME`;
- proporção e espessura realistas de carta;
- sem aparência infantil;
- sem estética gótica, caveira, corvo, serpente, espada, sigilo ou símbolo invertido.

Exemplo completo:

## REF-CARTA · ÂNGULO 3 · GERAR DO ZERO · NADA

> ### 📎 ANEXAR: **NADA**
>
> ### 🆕 GERAR DO ZERO

```json
{
  "shot_id": "REF_CARTA_soulmate_holographic",
  "reference_use": "Generate one isolated physical tarot card reference. No person, no hands and no avatar reference.",
  "identity_main": "No person. One premium physical soulmate tarot card only.",
  "prop": "A single vertical tarot card about 10 cm tall, printed on real thick card stock. The illustration shows an elegant adult couple connected by a soft celestial ribbon of light, surrounded by roses, tiny stars and a crescent moon. The artwork is saturated in deep sapphire, magenta, ruby and luminous teal. A wide mirrored silver metallic border produces subtle holographic rainbow reflections, with engraved arabesque flourishes in all four corners. A clean metallic title band at the bottom reads SOULMATE in large legible serif letters. The visual language is sophisticated spiritual tarot art for adults, never childish and never gothic.",
  "scene": "Plain neutral matte tabletop only, no room and no background objects.",
  "composition": "Extreme close-up of the single card lying flat, filling most of the vertical frame, with all four edges visible.",
  "camera": "macro close-up, slightly high toward the card",
  "state": "Start frame: the card lies still on the surface, ready to be reused as a fixed prop reference.",
  "lighting": "Soft neutral diffuse daylight of an overcast day, with realistic reflections on the metallic border.",
  "realism": "UGC realism, real paper texture, tiny edge wear, realistic shadows and reflections, iPhone-footage look, phone camera look not professional photography, no AI polish, no blur anywhere, everything in sharp focus.",
  "aspect_ratio": "9:16 vertical",
  "negative": "no captions, no subtitles, no words overlaid on the image, no person, no hands, no studio, no plastic texture, no childish illustration, no cartoon look, no blur, no artificial lighting, no gothic art, no skulls, no ravens, no snakes, no swords, no inverted symbols, no sigils"
}
```

O texto `SOULMATE` impresso na própria carta é permitido. Texto sobreposto pelo gerador não é.

> ⚠️ **Correção 2026-09-07 (Luigi), duas travas da REF-CARTA que valem sobre este exemplo:**
> 1. **As linhas `no warm orange color cast`, `no yellow tint`, `no golden glow`, `no sparkles` e `no glowing edges` NÃO entram no `negative` da REF-CARTA.** Elas matam o foil, o dourado da borda e o coração luminoso. É a ARMADILHA TÉCNICA 2 da memória `angulo3-copy-auraly`. O brilho é descrito como propriedade impressa do objeto, nunca como luz de cena, e a luz da cena continua neutra de dia nublado.
> 2. **A lista de símbolos góticos FICA no `negative` da REF-CARTA** (`no gothic art, no skulls, no ravens, no snakes, no swords, no inverted symbols, no sigils`). Ela é exceção à regra do §11.3: nomes de símbolo gótico não tropeçam o classificador do jeito que nome de órgão, gore ou marca tropeçam, e a memória sancionou essa lista especificamente para a REF-CARTA.
>
> Nos keyframes da avatar segurando a carta o `negative` volta ao completo e normal, porque lá a arte já vem travada pela REF-CARTA anexada.

---

## 11. Gates de imagem antes de cada JSON

### 11.1. Gate de composição visual

Conferir os dez itens:

1. o herói está no lower foreground, mais perto da lente que o rosto;
2. nada compete com o herói;
3. forma, tamanho, volume e cobertura do herói estão explícitos;
4. a câmera está o mais perto possível sem perder a leitura;
5. pessoas ficam normalmente em chest-up ou shoulders-up;
6. CTA é o plano mais fechado do vídeo;
7. cenário reconhecível, descrito por poucos grupos visuais;
8. fundo reduzido por enquadramento, nunca por blur;
9. quantidade de elementos compatível com geração realista;
10. segunda pessoa, se existir, entra cortada pelo quadro.

### 11.2. Gate de realismo

1. partir de âncora real;
2. usar poucos grupos de elementos;
3. preservar textura de pele, poros, rugas, sinais e fios individuais;
4. usar luz neutra e difusa de dia nublado;
5. evitar cast amarelo, laranja, marrom e glow dourado;
6. manter tudo nítido, inclusive o fundo;
7. aceitar regenerações como parte do processo até obter um frame crível.

Bloco obrigatório:

```json
{
  "realism": "UGC realism, real skin texture with visible pores, individual hair strands, subtle wrinkles, realistic shadows and reflections, iPhone-footage look, phone camera look not professional photography, no AI polish, no beauty smoothing, no blur anywhere, everything in sharp focus including background walls furniture and details."
}
```

### 11.3. Negative base

```json
{
  "negative": "no captions, no subtitles, no words overlaid on the image, no studio, no plastic skin, no extra fingers, no supernatural lighting, no blur, no artificial lighting, no warm orange color cast, no yellow tint, no golden glow"
}
```

Nunca usar apenas `no text`, pois isso pode apagar sinalização canônica ou o título impresso na carta.

Nunca colocar no negative o nome de um conceito sensível que se quer evitar. O classificador pode reagir ao termo mesmo negado. Termos de órgãos, gore, marcas e logos devem ser evitados no texto positivo, não injetados no negative.

---

## 12. Estrutura obrigatória dos prompts de imagem

Todo pacote começa com um índice:

| Take | Keyframe | Ação | Anexos |
|---|---|---|---|
| T1 | K01 | GERAR DO ZERO | âncora + REF-CARTA |
| T1 | K02 | GERAR DO ZERO | âncora + REF-CARTA |
| T2-T4 | K06 | GERAR DO ZERO | âncora + REF-CARTA |
| T5-T8 | K07 | EDITAR do K06 | K06 aprovado |
| CTA | K08 | EDITAR do K06 | K06 aprovado, nunca K07 |

O número do keyframe do CTA depende do roteiro: se o corpo tem **um** setup só (T2 a T4 no mesmo K06), o CTA é EDITAR do K06 e recebe o número seguinte, K07. Se o corpo tem uma variação de gesto que exige K próprio (K07), aí o CTA é K08. Em qualquer caso o CTA **edita o K do body**, nunca uma edição já editada.

Cada prompt possui:

1. título em caixa alta;
2. takes atendidos;
3. ação de geração;
4. referências no título;
5. bloco visual de anexos;
6. linha curta descrevendo a cena;
7. JSON completo.

Formato:

````md
## K01 · T1 · CARTA PUXADA · GERAR DO ZERO · ÂNCORA [AVATAR] + REF-CARTA

> ### 📎 ANEXAR: **2 IMAGENS**
> **1️⃣ ÂNCORA [AVATAR]** `producao/_ancoras/<avatar>_ancora.jpg`
> **2️⃣ REF-CARTA** já aprovada
>
> ### 🆕 GERAR DO ZERO

Carta face-down no primeiro plano, pronta para ser puxada até a lente.

<JSON COMPLETO AQUI>
````

### 12.1. Campos canônicos de geração

Usar:

- `shot_id`;
- `reference_use`;
- `identity_main`;
- `second_person`, quando houver;
- `prop`, quando houver;
- `wardrobe`;
- `scene`;
- `posture`;
- `composition`;
- `camera`;
- `state`;
- `lighting`;
- `realism`;
- `aspect_ratio`;
- `negative`.

Funções:

- `reference_use`: restringe o que cada anexo pode fornecer;
- `identity_main`: trava rosto e traços canônicos;
- `prop`: descreve forma, material, cor, tamanho, espessura e estado;
- `scene`: preserva a identidade do ambiente e seus grupos canônicos;
- `posture`: corrige a pose sem copiar a âncora;
- `composition`: hierarquia visual e distância;
- `camera`: altura, direção e proximidade;
- `state`: somente o primeiro instante da ação;
- `lighting`: luz física e neutra;
- `realism`: bloco completo;
- `negative`: falhas neutras a excluir.

### 12.2. Exemplos trabalhados

Os exemplos antigos (12.2 a 12.4) usavam uma avatar descartada e o formato de título com
`GERAR DO ZERO` / `EDITAR do K__`, revogado pelo GOOGLE FLOW DELIVERY FORMAT. Foram arquivados em
`_arquivo/2026-09-22_limpeza_angulo3/PLAYBOOK_MESTRE_exemplos_antigos_12.2-12.4.md`. O formato vigente
de entrega é o OUTPUT CONTRACT de `WORKFLOW_AURALY.md` (K e V autossuficientes, sem título).

---

## 13. [HISTÓRICO, NÃO USAR] Execução das imagens no Chrome

> ♻️ **Descontinuado em 2026-09-08.** Seção mantida só como registro. Nada aqui entra no workflow atual.

### 13.0. Matriz de capacidade e regra de handoff

O processo não deve presumir que toda IA possui controle do navegador. Antes de executar a etapa de geração, a IA deve identificar qual destes modos está disponível:

| Modo | Capacidade da sessão | O que a IA executa |
|---|---|---|
| A. Automação completa | consegue abrir e controlar abas, anexar arquivos, digitar, enviar, revisar e baixar | executa todo o lote no Chrome |
| B. Automação parcial | consegue abrir Chrome/URLs, mas não interagir com a página | prepara sete abas e entrega um pacote de prompts e anexos por aba para operação manual |
| C. Sem navegador | não consegue abrir ou controlar Chrome | prepara todo o pacote local, com prompts completos e ordem de execução, e faz handoff ao operador |

Não existe um comando universal que transforme uma sessão sem ferramenta de navegador em uma sessão com controle do Chrome. A conexão depende do aplicativo, extensão e ferramentas expostas naquele ambiente. Portanto:

- se a sessão tiver uma ferramenta de navegador ou computer use conectada ao perfil correto, usar o Modo A;
- se a sessão apenas puder executar comandos no terminal, usar o Modo B;
- se não houver nenhuma das duas capacidades, usar o Modo C;
- nunca alegar que anexou, enviou, gerou, revisou ou baixou algo sem conseguir observar essa ação;
- falta de automação do navegador não autoriza pular os gates editoriais nem simplificar os prompts.

No Claude Code sem ferramenta de browser control, o terminal pode abrir o perfil com:

```powershell
Start-Process -FilePath 'C:\Users\luigi\Desktop\Luigi (Luigi - CARDS MELODY) - Chrome.lnk'
```

Isso abre o Chrome, mas não concede ao Claude Code capacidade de clicar, digitar, anexar, enviar ou baixar. Para o Modo A, a sessão precisa expor explicitamente uma ferramenta de automação de navegador conectada ao Chrome. A presença de uma extensão instalada, sozinha, não prova que a sessão atual possui essa ferramenta.

#### Handoff do Modo B ou C

Quando o controle do navegador não existir, a IA deve produzir antes de parar:

```text
pacote_browser/<avatar>/
  01_hook_<slug>.md
  02_hook_<slug>.md
  03_hook_<slug>.md
  04_hook_<slug>.md
  05_hook_<slug>.md
  06_body.md
  07_cta.md
  MAPA_ABAS.md
  CHECKLIST_REVISAO.md
```

Cada arquivo de asset deve conter, nesta ordem:

1. nome sugerido da aba;
2. imagens a anexar, com caminhos absolutos;
3. ação `GERAR DO ZERO` ou `EDITAR do K__`;
4. descrição curta da cena;
5. prompt JSON completo;
6. nome final do arquivo a baixar;
7. checklist visual específico do asset;
8. instrução de recuperação se aquela aba falhar.

`MAPA_ABAS.md` deve funcionar como painel de execução:

| Aba | Asset | Anexo 1 | Anexo 2 | Prompt | Nome do download | Status |
|---|---|---|---|---|---|---|
| 1 | Hook 1 | âncora avatar | REF-CARTA | `01_hook_...md` | `01_hook_....png` | pendente |
| 2 | Hook 2 | âncora avatar | REF-CARTA | `02_hook_...md` | `02_hook_....png` | pendente |
| 6 | Body | âncora avatar | REF-CARTA | `06_body.md` | `06_body.png` | pendente |
| 7 | CTA | K body aprovado | nenhum | `07_cta.md` | `07_cta.png` | pendente |

Depois que Luigi ou outra sessão com controle de navegador gerar os arquivos, a IA retoma a partir da revisão visual e do fechamento do lote. Não refaz análise, Puzzle, copy ou seleção de hooks.

### 13.1. Perfil obrigatório

Abrir o Chrome somente por:

```text
C:\Users\luigi\Desktop\Luigi (Luigi - CARDS MELODY) - Chrome.lnk
```

Perfil esperado: `Luigi - CARDS MELODY`, com login do ChatGPT Plus e extensão de controle autorizada.

### 13.2. Unidade do lote

Lote padrão por avatar:

- cinco ganchos visuais;
- um body;
- um CTA;
- sete conversas novas.

Uma conversa nova por asset evita contaminação de roupa, cenário, pose e objetos pelas gerações anteriores.

⚠️ **Ordem de dependência, não é tudo em paralelo:** a REF-CARTA e, quando houver, a REF de 2ª pessoa são geradas e **aprovadas antes** dos cinco hooks e do body, porque eles anexam a REF-CARTA. O **CTA** é EDITAR do K do body, então a aba dele só roda **depois** do body aprovado. Na prática o paralelo é de **até seis abas** na primeira leva (cinco hooks + body), com a REF-CARTA já pronta e o CTA em espera.

### 13.3. Ordem rápida

1. abrir sete abas do ChatGPT;
2. confirmar avatar e asset de cada aba;
3. anexar a âncora do avatar e a REF-CARTA nos prompts `GERAR DO ZERO`;
4. em prompts `EDITAR`, anexar apenas o K aprovado indicado;
5. colar o prompt completo da aba;
6. enviar uma aba por vez, sem esperar a anterior terminar;
7. deixar as sete gerações correrem em paralelo;
8. voltar às abas para revisar;
9. recuperar apenas as falhas;
10. manter os resultados como rascunho até aprovação do lote.

Anexo rápido autorizado: copiar a imagem local e colar no compositor do ChatGPT. O seletor `Adicionar arquivos e mais` > `Enviar do computador` é a alternativa automática.

Antes de enviar cada aba, verificar:

- conversa nova;
- avatar correto;
- REF-CARTA correta;
- prompt correspondente ao asset;
- anexos efetivamente visíveis no compositor;
- nenhum texto antigo preenchido no campo.

### 13.4. Recuperação de erro

Se a aba mostrar erro de geração:

1. manter a mesma aba do asset;
2. anexar novamente a âncora do avatar;
3. anexar novamente a REF-CARTA, se o prompt exigir;
4. colar novamente o prompt completo daquele asset;
5. verificar os nomes dos anexos no compositor;
6. enviar novamente;
7. não interferir nas abas saudáveis.

Nunca usar apenas o botão de repetir sem renovar as referências. Nunca reenviar somente o texto.

Se a restrição for de conteúdo, não fazer tentativa cega. Reescrever a descrição da ação e da cena, mantendo a fala intacta. Ordem:

1. enxugar a ação;
2. remover detalhes desnecessários de alvo ou posição;
3. neutralizar a ação visual;
4. separar elementos em takes, se preciso;
5. manter a fala exatamente igual ao roteiro.

---

## 14. Revisão visual de cada imagem

Uma imagem só pode entrar no lote aprovado se passar:

- identidade do avatar preservada;
- idade, textura de pele, sinais e rugas preservados;
- cabelo, roupa e joias corretos;
- mãos anatomicamente aceitáveis;
- cinco dedos quando visíveis;
- REF-CARTA com a mesma arte e proporção;
- `SOULMATE` ou `TWINFLAME` legível apenas na carta;
- nenhum texto sobreposto;
- cenário reconhecível e consistente;
- kit de tarólogo presente em dois grupos;
- bandeira dos EUA visível e em foco;
- cruz ou crucifixo coerente;
- luz neutra;
- ausência de blur;
- ausência de polimento plástico;
- herói mais próximo que o rosto;
- estado inicial correto;
- sem rosto legível de alma gêmea;
- sem estética de pacto ou ocultismo sombrio.

Realismo é selecionado por regeneração. Se a composição está correta, mas o rosto ou as mãos ainda parecem sintéticos, gerar outra variação do mesmo setup e da mesma referência.

---

## 15. Aprovação por lote

O processo é sequencial por avatar:

```text
Avatar 1: gerar sete imagens
  -> revisar
  -> mostrar no chat
  -> lote aprovado?
  -> baixar e organizar
  -> entregar prompts Flow

Avatar 2: repetir com mesma copy, hooks e REF-CARTA
```

Não começar o próximo avatar antes de fechar os arquivos do avatar aprovado, salvo ordem expressa de Luigi.

Resultados antigos de um lote reiniciado são rascunhos. Não baixar como finais e não misturar na nova pasta.

---

## 16. Roteiro e divisão em takes

O vídeo modelo determina duração, quantidade de takes e gramática. Não impor formato fixo.

Regras de fala:

- inglês americano;
- copy sem travessão;
- cada take cabe em aproximadamente oito segundos;
- alvo seguro: 13 a 29 palavras;
- referência: cerca de 3,3 palavras por segundo;
- take longo é dividido em fim de frase;
- take curto permanece curto e o silêncio é cortado no CapCut;
- nunca adicionar filler;
- nunca parafrasear depois da aprovação;
- fala do Flow é cópia literal do roteiro final.

### 16.1. Arquitetura Auraly típica

Não é formato fixo, mas a adaptação costuma cumprir:

1. pattern interrupt visual;
2. declaração de que o vídeo encontrou a espectadora por uma razão;
3. sinal, timing ou pessoa que continua voltando;
4. pista verificável ou reveal parcial;
5. `222` com consequência;
6. save com consequência;
7. follow com consequência;
8. Stories como destino da revelação.

### 16.2. Exemplo de CTA atual

```text
Comment two two two. That's how this gets tied to your name. Save this so the sign stays with you, and follow me so the way stays open. Then tap my profile picture and watch my stories before they disappear. His face is already waiting for you there.
```

O CTA só pode declarar o rosto nos Stories quando o corpo da copy já construiu esse objeto de desejo. Quando o roteiro ficou atmosférico, usar curiosidade:

```text
One last thing. Tap my profile picture and watch my stories before they disappear, because the second part of this sign is waiting for you there.
```

---

## 17. Prompts de vídeo Flow/Veo 3.1

Prompt de vídeo é texto simples. Não repetir composição, paleta ou descrição longa do cenário.

### 17.1. Talking

```text
a avatar (mulher) fala em inglês com sotaque americano de [DESCRIÇÃO DO AVATAR], voz autêntica, dinâmica, apaixonada e emocional, como se exigisse ser ouvida, a seguinte frase: "[FALA EXATA DO ROTEIRO]"

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: [continuação simples e natural do estado inicial]. A avatar age naturalmente, com movimentos rápidos e legíveis, mantendo o vídeo engajante. Estilo TikTok nativo, UGC.

câmera: [fixa / leve push-in / leve handheld natural]

som ambiente: [ambiente coerente], sem música, sem ruído de fundo
```

### 17.2. B-roll ou insert

```text
(sem fala no take: a fala T__ do roteiro entra como voz-over na edição)

o que acontece no vídeo: [movimento visual enxuto]

câmera: [macro fixa / top-down fixa / leve handheld]

som ambiente: [som do ambiente], sem música
```

### 17.3. Exemplo: carta puxada

```text
a avatar (mulher) fala em inglês com sotaque americano de mulher branca adulta, voz autêntica, dinâmica, apaixonada e emocional, como se exigisse ser ouvida, a seguinte frase: "Do not skip this. This reading is not for everyone, and if it found you, it found you for a reason."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: a avatar puxa rapidamente a carta virada para baixo em direção à lente e para antes de encostar na câmera. Ela levanta o olhar para a lente enquanto termina a frase.

câmera: fixa, leve push-in

som ambiente: quarto silencioso durante o dia, som leve do papel sobre a mesa, sem música
```

### 17.4. Exemplo: CTA

```text
a avatar (mulher) fala em inglês com sotaque americano de mulher branca adulta, voz autêntica, dinâmica, apaixonada e emocional, como se exigisse ser ouvida, a seguinte frase: "One last thing. His face is already revealed in the reading I left in my stories. Tap my profile picture before it disappears."

a avatar diz todas as palavras corretamente, não pula nenhuma palavra, e diz a última palavra por inteiro sem cortar no final. Lip sync perfeito durante todo o vídeo.

o que acontece no vídeo: a avatar mantém a carta erguida ao lado do rosto, aponta para o canto superior do quadro e termina olhando diretamente para a lente.

câmera: fixa, leve push-in

som ambiente: ambiente silencioso de casa durante o dia, sem música
```

### 17.5. Câmera handheld

Se o avatar simula segurar o celular, indicar qual braço permanece parado:

```text
a avatar não move o braço esquerdo estendido para o lado do quadro, porque essa mão segura a câmera que grava o vídeo.
```

Não incluir essa linha quando o celular está apoiado e a câmera é fixa.

---

## 18. Stories e CTA final

### 18.1. Ordem do CTA

```text
222 -> save -> follow -> Stories
```

O comentário vem antes porque:

- custa pouco e não tira a pessoa do vídeo;
- é o selo que dá sentido ao destino, e é métrica premiada pelo algoritmo;
- quem abre o perfil pode não voltar para comentar.

### 18.2. Dois modos

**Declarado:** usar quando a copy entregou inicial, traço, timing, pessoa específica ou já falou do rosto.

```text
His face is already revealed, and it is sitting in my stories right now. Tap my profile picture and it is the first thing you see.
```

**Curiosidade:** usar quando a promessa ficou em bênção, sinal ou boa notícia.

```text
Do not leave with only half of this message. Tap my profile picture, and you will understand exactly why this message found you today.
```

### 18.3. Três telas de Stories

Story 1, continuidade:

```text
If you just came from the video, you are in the right place.
This is the part I could not put out there. 🤍
```

Story 2, revelação nomeada:

```text
Here he is. The face came through this morning.
He goes by M•••••
One tap away. 👇
```

Story 3, CTA com botão:

- botão do link visível;
- copy curta;
- rastreamento próprio do canal Stories;
- nenhuma imagem de rosto, nem obscurecida.

No modo declarado, Stories 2 e 3 podem ser combinados para reduzir atrito.

### 18.4. Gramática visual no CapCut

Nos segundos finais:

1. fala de Stories;
2. legenda fixa, como `The reveal is in my stories`;
3. seta apontando para o canto da foto de perfil.

Isso não exige keyframe novo. Não colocar celular na mão do avatar para representar o Stories.

---

## 19. Montagem no CapCut

Regras padrão, ajustadas ao vídeo modelo:

- timeline 1080 x 1920, 30 fps;
- cortar silêncio inicial;
- fala começa imediatamente;
- cortes nos mesmos beats do modelo;
- esconder transição quando mão, fumaça, carta ou outro elemento cobre o quadro;
- legenda karaokê de duas ou três palavras;
- não cobrir a REF-CARTA;
- manter `222` isolado visualmente no CTA;
- usar seta para a foto de perfil no CTA de Stories;
- adicionar textos e selos somente na edição, nunca na imagem gerada;
- manter trilha separada e controlável;
- se usar música, volume de referência entre -19 e -20 dB;
- verificar sincronização labial e última palavra de cada take;
- conferir que apenas um dos cinco hooks entra em cada versão final.

Pacote com cinco hooks gera cinco vídeos:

```text
V01A + corpo comum + CTA comum
V01B + corpo comum + CTA comum
V01C + corpo comum + CTA comum
V01D + corpo comum + CTA comum
V01E + corpo comum + CTA comum
```

---

## 20. Entrega dos prompts Flow após aprovação

Assim que Luigi disser `lote aprovado`:

1. baixar todas as imagens aprovadas;
2. criar a pasta do avatar e da data em Downloads;
3. mover e renomear os sete assets;
4. copiar a REF-CARTA para `referencias`;
5. criar `PROMPTS_VIDEO_FLOW.md`;
6. enviar os prompts completos no chat;
7. incluir um prompt para cada hook e cada take do corpo/CTA;
8. indicar qual K cada V usa;
9. fechar com roteiro final em inglês numerado e corrido;
10. só então começar o próximo avatar.

---

## 21. Gates finais da produção

### Copy

- [ ] Esqueleto do modelo preservado.
- [ ] Variável Auraly claramente definida.
- [ ] Hook relevante e imprevisível.
- [ ] Ponte para o rosto da alma gêmea.
- [ ] Keyword `222`.
- [ ] Selo antes de Stories.
- [ ] Stories como destino principal.
- [ ] DM não prometida como sala principal.
- [ ] Sem app, quiz, plano, preço ou pagamento único.
- [ ] Registro divino, sem pacto.
- [ ] Cada fala tem 13 a 29 palavras, salvo exceção deliberada do modelo.
- [ ] Zero filler e zero paráfrase após aprovação.

### Imagem

- [ ] JSON válido e completo.
- [ ] Título e bloco de anexos presentes.
- [ ] `reference_use` separa a função de cada anexo.
- [ ] Um K por setup.
- [ ] Geração do zero somente quando necessária.
- [ ] Edições partem do K inicial correto.
- [ ] REF-CARTA idêntica.
- [ ] Kit Auraly em dois grupos.
- [ ] Bandeira visível e em foco.
- [ ] Herói no lower foreground.
- [ ] CTA é o plano mais fechado.
- [ ] Luz neutra, sem cast quente.
- [ ] Tudo nítido, sem blur.
- [ ] Pele real, sem rejuvenescimento.
- [ ] Nenhum texto sobreposto.
- [ ] Nenhum rosto de alma gêmea legível.

### Vídeo

- [ ] Fala idêntica ao roteiro.
- [ ] Última palavra inteira.
- [ ] Lip sync correto.
- [ ] Ação é continuação do estado inicial.
- [ ] Ação descrita de forma enxuta.
- [ ] Câmera simples.
- [ ] Som ambiente e `sem música` no prompt.
- [ ] B-roll marcado como voz-over.
- [ ] Nenhuma interface do app.
- [ ] CTA aponta para Stories.

### Arquivos

- [ ] Pasta final em Downloads.
- [ ] Sete imagens nomeadas.
- [ ] REF-CARTA salva.
- [ ] `PROMPTS_VIDEO_FLOW.md` presente.
- [ ] Arquivo de produção atualizado.
- [ ] Tudo importante também enviado no chat.

---

## 22. Linter e validação local

Quando o projeto completo estiver disponível, rodar:

```text
python checar_entrega.py producao/<slug>
```

Para o pipeline Auraly, `ROTEIRO.md` precisa começar com `pipeline: auraly`.

Não fechar uma entrega com falhas. O linter deve conferir, entre outros pontos:

- keyword;
- faixa de palavras;
- igualdade entre roteiro e prompts de vídeo;
- JSON válido;
- bandeira dos EUA;
- `no captions`;
- nomenclatura T/K/V/REF;
- ausência de produto;
- ordem das seções;
- CTA de Stories;
- termos proibidos no negative;
- instruções incompletas do tipo patch.

Se houver falso positivo, corrigir o linter ou a estrutura de forma explícita. Não ignorar silenciosamente.

---

## 23. Erros fatais e correção

| Erro | Por que prejudica | Correção |
|---|---|---|
| gerar imagem antes de aprovar copy | congela uma estrutura errada | voltar ao Gate 2 |
| transformar demo em talking head | remove o herói do vencedor | preservar a ação visual |
| gerar um K por take | cria trabalho e deriva | agrupar por setup |
| gerar tudo do zero | muda rosto, fundo e luz | editar do K aprovado |
| editar em cascata | acumula deriva | voltar ao primeiro K do setup |
| prompt natural de imagem | perde travas e rastreabilidade | usar JSON completo |
| usar `no text` | apaga texto canônico da carta | usar `no captions` e equivalentes |
| listar muitos objetos | reduz realismo | agrupar o kit em dois blocos |
| copiar pose da âncora | limita composição | restringir a âncora em `reference_use` |
| cenário novo por prompt | quebra a conta/persona | preservar identidade do ambiente |
| luz quente | cria aparência sintética | luz neutra e negatives de cor |
| blur de fundo | perde estética UGC | fechar enquadramento e manter nitidez |
| rosto da alma gêmea legível | entrega o que deveria vender | obscurecimento físico ou ausência |
| carta gótica/infantil | viola registro e credibilidade | arte adulta, saturada e holográfica |
| CTA de DM | usa arquitetura revogada, e a DM nem roda mais | Stories como único destino |
| Stories antes de `222` | perde o comentário | selo primeiro |
| repetir sem anexos após erro | perde identidade | renovar anexos e prompt completo |
| alterar a fala por moderação | quebra a fonte de verdade | simplificar somente a ação |
| entregar só arquivo | cria atrito | conteúdo integral também no chat |
| entregar só chat | perde registro | salvar o pacote local |

---

## 24. Regra para alterações durante a produção

Quando Luigi adicionar uma regra, ela vale imediatamente para todos os prompts ainda não aprovados.

A IA deve:

1. identificar quais assets são afetados;
2. reescrever cada prompt completo;
3. atualizar o arquivo local;
4. reenviar os prompts completos no chat;
5. não fornecer apenas uma linha para ser adicionada manualmente;
6. preservar assets já aprovados, salvo se a nova regra exigir regeneração.

---

## 25. Modelo de resposta por etapa

### Após `/watch`

```text
Análise concluída.

Vídeo: [nome]
Duração: [tempo]
Herói do hook: [elemento]
Estrutura: [beats]
Variável para Auraly: [variável]

[transcrição]
[tabela Puzzle]
[roteiro adaptado]
[validação]
```

### Depois do roteiro aprovado

```text
Aqui está o portfolio Auraly com 10 ganchos em 3 famílias: 4/3/3.

[família A: invariante + 4 variações]
[família B: invariante + 3 variações]
[família C: invariante + 3 variações]

Escolha cinco. Esses cinco serão repetidos para todos os avatares.
```

### Depois de gerar um lote

```text
Lote de [avatar] concluído:

1. [gancho]
2. [gancho]
3. [gancho]
4. [gancho]
5. [gancho]
6. body
7. CTA

[imagens e revisão]
[prompts de imagem usados]
```

### Depois de `lote aprovado`

```text
Lote organizado em:
C:\Users\luigi\Downloads\<avatar>_<data>\

[todos os prompts Flow]
[mapa K -> T -> V]
[roteiro final numerado]
[roteiro corrido]
```

---

## 26. Fonte de verdade e controle de versões

Ao operar dentro do projeto, consultar materiais vivos apenas quando a etapa atual exigir. A ordem de precedência é:

1. `AGENTS.md` da raiz, como roteador;
2. `WORKFLOW_AURALY.md`, como processo canônico;
3. `CHECKPOINT.md` da produção ativa, como estado e decisão já tomada;
4. instrução explícita mais recente de Luigi que ainda não tenha sido persistida;
5. este playbook, somente como referência criativa da etapa;
6. `angulo3-copy-auraly`, `angulo3-swipe-padroes` e demais memórias indicadas pelo workflow;
7. gabaritos aprovados mais recentes do Ângulo 3;
8. `AURALY_AGENT.md`, `CLAUDE.md` e demais arquivos históricos para Auraly.

Quando este playbook divergir de `WORKFLOW_AURALY.md` ou do checkpoint ativo, o workflow e o
checkpoint ganham.

Arquivos históricos podem conter regras revogadas. Exemplos que não devem retornar:

- rosto entregue principalmente por DM;
- Stories tratado como etapa secundária;
- carta pálida por obrigação;
- keyword `yes`;
- geração de imagem em linguagem natural;
- um keyframe para cada take;
- geração de todos os frames do zero.

Se duas fontes divergirem, registrar a divergência, aplicar a regra mais recente e corrigir o documento antigo quando a manutenção do projeto fizer parte da tarefa.

---

## 27. Definição de pronto

A produção Auraly está pronta somente quando:

- o vídeo modelo foi realmente analisado;
- a copy passou pelo Puzzle e foi aprovada;
- cinco hooks foram escolhidos;
- a REF-CARTA está aprovada;
- um lote completo foi gerado e aprovado para cada avatar;
- as imagens finais estão em Downloads, separadas por avatar e data;
- todos os prompts Flow foram entregues no chat e em arquivo;
- o CTA usa `222`, follow, save e Stories na ordem correta;
- nenhum produto, app ou rosto de alma gêmea aparece no vídeo;
- a identidade e o cenário de cada avatar permanecem consistentes;
- os gates de copy, imagem, vídeo e arquivos passaram;
- o roteiro final em inglês numerado e corrido encerra a entrega.

Até todos esses itens estarem cumpridos, a produção continua aberta.
