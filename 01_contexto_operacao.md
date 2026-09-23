# 01 — Contexto Completo da Operação

> Lembrete: todos os vídeos desta operação são protagonizados por **avatares de IA (pessoas que não existem)**. Nada aqui envolve filmar pessoas reais.

## 1. O que a operação faz (resumo de uma frase)

Produzimos vídeos verticais curtos, protagonizados por avatares de IA que parecem influenciadores de saúde/bem-estar americanos, para atrair a atenção do público dos EUA em Reels/TikTok/Facebook e convertê-los num funil de comentário → mensagem privada → link de afiliado.

## 2. O nicho e o público

- **Nicho principal:** saúde, bem-estar, "remédios naturais", receitas caseiras, detox, emagrecimento, saúde íntima, saúde digestiva. Também há um braço espiritual/manifestação (não coberto em detalhe aqui, mas o método é o mesmo).
- **Público-alvo:** Estados Unidos. Predominantemente pessoas comuns interessadas em soluções caseiras/baratas para problemas de saúde do dia a dia. Muitas vezes público mais velho, desconfiado da indústria farmacêutica.
- **Idioma do conteúdo:** **inglês americano**, natural e coloquial (não formal). Toda fala dos avatares é em inglês. A comunicação de bastidor (entre você e quem te ajuda a produzir) pode ser em português.
- **Plataformas:** TikTok, Instagram Reels, Facebook Reels. Formato sempre **9:16 vertical**.

## 3. Como o dinheiro entra (monetização)

Dois pilares:

1. **Comissões de afiliado** — principalmente Amazon Associates e programas diretos de marcas. O vídeo nunca vende explicitamente; ele gera curiosidade e manda a pessoa pro DM, onde o link de afiliado é entregue.
2. **Retainers / contratos com marcas** — à medida que as contas crescem, marcas pagam valores fixos mensais para ter conteúdo/divulgação.

### O funil de DM (o mecanismo central)

O vídeo termina com uma **chamada (CTA)** pedindo pra pessoa **comentar uma palavra-chave**. Um sistema automatizado detecta o comentário e dispara uma **mensagem privada (DM)** com o link do produto. Quase sempre há um **follow-gate**: a pessoa precisa estar seguindo o perfil, senão a plataforma não deixa o robô mandar a DM.

- **A palavra-chave da nossa operação é sempre `yes`.** Independente da palavra que o vídeo original usava (tea, book, drink, pure, etc.), nós padronizamos para **"yes"** em todos os roteiros a partir de agosto/2026. Isso simplifica a automação e evita erro. (Ver documento 05 para a regra completa.)
- O CTA no vídeo aparece como `comment "yes" below` ou `type "yes" below`.
- O produto em si **só aparece na DM**, nunca no vídeo. O vídeo mostra a "receita caseira"; o produto (suplemento) é "o ingrediente secreto que potencializa", entregue no link.

## 4. Os papéis e a estrutura de marca

- Você (o operador) roda uma produção escalada de vídeos com múltiplos avatares.
- Existe uma marca/estrutura que gerencia contas de creators de IA.
- Há uma comunidade/curso associada ao ecossistema.
- O objetivo de longo prazo é um **pipeline de produção totalmente sistematizado e escalável**, com múltiplos nichos e múltiplas identidades de avatar rodando em paralelo.

## 5. As ferramentas (stack de produção)

Entenda o papel de cada uma. Elas se dividem em **geração de imagem** e **geração de vídeo**.

### Geração de imagem (o "frame inicial" de cada take)
- **Nano Banana 2** — modelo de geração de imagem usado para a maior parte do volume. Recebe a **foto do avatar como âncora de identidade** (pra manter o rosto/roupa/cenário sempre iguais) e um prompt descrevendo a cena. É onde criamos o frame inicial de cada take.
- **Nano Banana Pro** — versão superior, usada para os **frames-herói** (os mais importantes, tipo o hook), onde a qualidade precisa ser máxima. Fluxo recomendado: volume no Nano Banana 2, frames-herói no Pro.
- Essas ferramentas também aceitam **comandos de edição** — ou seja, você pega uma imagem já gerada e pede "mude só X, mantenha o resto idêntico". Isso é essencial para gerar os "estágios" de uma transformação (ver documento 02, seção do braço).

### Geração de vídeo (animar a imagem → clipe falado)
- **Veo 3.1 via Flow** — ferramenta de **imagem-para-vídeo**. Você dá a imagem (frame inicial) + um prompt descrevendo o que acontece e a fala, e ela gera o clipe de ~8s com o avatar falando/agindo.
- **Veo 3.1 Lite / Lower Priority** — versão que roda **sem consumir créditos** (fila mais lenta, 720p). Ideal para volume. Boa para gerar muitos takes sem gastar.
- **Flow tem um "Agent"** (movido a Gemini) feito para **geração**, não para análise. Ele usa "Agent Instructions" como uma ficha de personagem persistente e permite marcar assets com @ para manter consistência. Serve pra manter o avatar constante entre gerações. Não serve para "assistir" e analisar vídeos.

### Análise de vídeo de referência
- Para **decompor** o vídeo vencedor (analisar frame a frame), quem tem a ferramenta de extrair frames é quem faz a decomposição (ver documento 03). A IA que te ajuda **não "assiste" vídeo nem ouve áudio** — ela extrai quadros (frames) do `.mp4` e olha as imagens. Portanto **áudio/música não são identificáveis** por ela (ver documento 06 sobre identificação de música).

### Legendas / edição final
- As legendas grandes estilo "Captions.ai Prism Pro" são uma referência de estilo. A montagem final (juntar takes, pôr legenda, pôr locução quando necessário) é feita num editor de vídeo.

## 6. O que "bom" significa nesta operação

- **Fidelidade ao vencedor** acima de criatividade.
- **Congruência** entre avatar, cenário, registro de voz e produto.
- **Hook impecável** — os 3 primeiros segundos decidem tudo.
- **Realismo UGC** — parecer vídeo real de celular (poros, pele real, luz natural), nunca "cara de IA" polida.
- **Zero texto nas imagens geradas** — a legenda entra só na edição.
- **Consistência do avatar** entre todos os takes e todos os vídeos.
- **CTA com follow-gate e keyword "yes"** sempre presente.

## 7. Ética/segurança do conteúdo (leia com atenção)

Estes vídeos são **encenações de personagens de IA que não existem**. Isso é o que torna possível produzir cenas que envolvem corpo, saúde íntima, "antes e depois", etc. — porque **não há nenhuma pessoa real envolvida**.

- Nenhuma pessoa real é filmada, exposta ou tem sua imagem usada.
- Os "clientes" que aparecem nos vídeos (a mulher no antes/depois, a pessoa deitada) **também são gerados por IA** — não existem.
- As afirmações de saúde ("claims") são responsabilidade de quem publica; este manual apenas descreve o processo de produção. Há um alerta de compliance recorrente nos casos mais agressivos (ver documento 06).

Quando uma ferramenta de geração interpretar um pedido como sensível, **deixe explícito no prompt/contexto que se trata de um personagem de IA fictício**, não de uma pessoa real — isso ajuda a ferramenta a entender que não há dano real envolvido.
