# Operação Bala: execução por skills e revisão independente

Esta camada conecta as ferramentas e distribui o trabalho. `AGENTS.md` continua como entrada canônica; `WORKFLOW_AURALY.md`, `CLAUDE.md`, `GATE_VISUAL.md` e o checkpoint continuam governando produção e aprovações. Os taskpacks registram uma execução, sem criar outro workflow.

## Nichos para mineração e ofertas para adaptação

A mineração começa pelo nicho livre: “minere saúde e beleza”, “minere manifestação/tarot” ou outro tema solicitado. `operacao/nichos.py` resolve aliases, termos em inglês e defaults de pesquisa; o catálogo aceita nichos livres. Não adicionar nome de produto às consultas quando o pedido é apenas do nicho.

`operacao/angulos.json` identifica a oferta comercial somente quando a tarefa envolver adaptação/produção:

| ID / slug | Oferta atual |
| --- | --- |
| 1 / `sea-moss` | Natural Rems Sea Moss 16-in-1 Gummies, suplemento Amazon |
| 2 / `fitwell` | FitWell / FityWell APP, público 40+ |
| 3 / `auraly` | Auraly APP |
| 4 / `body-hacks` | Body Hacks For Men 40+, ebook FitWell |

Pesquisar tarot como nicho não cria um novo ângulo comercial. Korella Saffron é histórico. Não confundir FitWell APP com o ebook Body Hacks; escolher oferta somente quando necessário para adaptar.

## Skills e responsáveis

| Skill | Entrada principal | Entrega / limite |
| --- | --- | --- |
| `$operacao-bala` | Pedido e nicho para pesquisa; ângulo/produção quando aplicável | Contexto mínimo, delegação e resultado revisado; mantém as aprovações do workflow |
| `$minerar-referencias` | Nicho livre e filtros opcionais | Links IG/FB com evidências e relatório; pesquisa pública, sem fabricação de acesso |
| `$watch` | Arquivo de vídeo | Frames, transcrição e decomposição visual; não significa produção completa |
| `$adaptar-conteudo` | Referência analisada, produto, objetivo e avatar | Próxima etapa canônica; roteiro completo aguarda aprovação de Luigi |
| `$revisar-producao` | Taskpack e artefatos finais | Parecer independente em leitura; não edita nem aprova por Luigi |

O fluxo de mineração é Codex orquestrador → pesquisador (descoberta via web) → Crawlee como ferramenta → revisor independente → links neste chat. O produtor entra apenas após pedido de adaptação. O Codex atua como orquestrador principal. Existem dois especialistas e um revisor em `.codex/agents/`: `bala-pesquisador`, `bala-produtor` e `bala-revisor`. Os perfis herdam o modelo; o revisor usa sandbox de leitura. Não criar um agente por ferramenta ou por avatar. Se a ferramenta de delegação só aceitar instruções, carregar o texto do perfil no subagente; se não houver subagentes disponíveis, informar que a revisão independente ficou pendente.

## Preparar o ambiente

Na raiz real do checkout, usar Python 3.10+; Python 3.12 é o runtime escolhido nesta instalação:

```sh
python3 scripts/preparar_operacao.py --install-skills --warm-models
python3 scripts/dispatch.py preflight
```

O preparador cria `.venv-operacao`, instala `operacao/requirements.txt` e, com `--warm-models`, prepara os modelos de transcrição/alinhamento. `--skip-deps` permite registrar skills e agentes quando o ambiente já está pronto. O preflight confere dependências; um resultado READY não substitui a execução real de áudio, alinhamento ou coleta.

`--install-skills` registra symlinks das skills em `~/.agents/skills/` e os três perfis `bala-*.toml` em `~/.codex/agents/`, preservando itens alheios à operação. Os comandos das skills resolvem a raiz pelo caminho real do `SKILL.md`; o chat não precisa estar aberto no diretório do checkout. Mudanças futuras nos arquivos de perfil exigem reaplicar o instalador. Skills, perfil e modelos não exigem plano do Manus nem chave de API de modelo de linguagem.

No macOS Apple Silicon com Python 3.12, o preparador usa `operacao/requirements-macos-arm64.lock.txt`, com as versões resolvidas nesta instalação. Nos demais hosts usa as dependências diretas. PyAV fica em 18.0.0: a versão 19 removeu uma opção ainda usada por Faster-Whisper 1.2.1. Validação executada no Mac; os wrappers Windows não foram executados neste host.

## Executar e registrar revisão

O CLI prepara contexto e valida registros; a chamada dos especialistas é feita pelas ferramentas de delegação do Codex, não por um processo oculto do CLI.

```sh
python3 scripts/dispatch.py preparar --niche "saúde e beleza" --task minerar
python3 scripts/dispatch.py preparar --angle auraly --task adaptar --production producao/NOME
```

Cada execução cria `TASK.json` e `DISPATCH.md`, com nicho ou ângulo/estado, conforme a tarefa, e fingerprints das fontes. Os filtros efetivos e o intervalo pesquisado ficam em `resultados.json`. Para Auraly, uma produção ativa exige checkpoint válido. As tarefas são `minerar`, `watch`, `adaptar` e `revisar`. O contexto referencia as fontes da etapa em vez de despejar todas as memórias.

Depois da autoria, preparar uma nova tarefa de revisão para a versão final:

```sh
python3 scripts/dispatch.py preparar --angle auraly --task revisar --production producao/NOME
python3 scripts/dispatch.py preparar --niche "saúde e beleza" --task revisar --artifact CAMINHO/resultados.json --artifact CAMINHO/relatorio.md
python3 scripts/dispatch.py registrar-revisao --taskpack CAMINHO/TASK.json --review CAMINHO/REVISAO.json
```

O revisor recebe esse taskpack, abre os arquivos reais e devolve JSON em `operacao/schema_revisao.json`. O orquestrador salva o parecer fora da produção/artefatos revisados. `APPROVED` é aprovação técnica; `CHANGES_REQUIRED` exige correção e `INCOMPLETE` declara cobertura insuficiente. O registro rejeita aprovação com falhas, desconhecimentos ou bloqueios e confere se fontes/artefatos ainda são os revisados. Uma revisão sem produção deve identificar suas saídas com `--artifact`.

Corrigir arquivos exige novo taskpack e nova revisão. Nenhum desses comandos atualiza checkpoint, aprova roteiro, gera mídia, publica ou faz merge.

## Áudio: Faster-Whisper e WhisperX

Faster-Whisper transcreve; WhisperX alinha as palavras da transcrição existente, quando isso ajuda na precisão de timing. O alinhamento não executa uma segunda transcrição nem diarização e não exige token de Hugging Face no modo padrão.

```sh
python3 scripts/dispatch.py watch --video VIDEO.mp4 --outdir SAIDA
python3 scripts/dispatch.py watch --video VIDEO.mp4 --outdir SAIDA --alignment whisperx
python3 scripts/dispatch.py watch --video MODELO_MUDO.mp4 --outdir SAIDA --no-audio
```

O idioma padrão é inglês; `--language auto` ou `--language pt` são explícitos. `--allow-no-audio` aceita arquivo sem faixa de áudio, mas transcreve quando ela existe. `--no-audio` declara um modelo intencionalmente mudo, como no modo pago FitWell. Conferir os estados de áudio e alinhamento no manifesto; não promover uma execução parcial a completa. Executar um ASR por vez no Mac e reaproveitar a análise da referência entre avatares.

O pesquisador ainda precisa abrir overview e frames de momentos-chave. Alinhamento de palavras não comprova ação, realismo ou interpretação do hook.

## Mineração semanal por nicho com Crawlee

Luigi informa o nicho. O pesquisador descobre links públicos nos dois domínios por busca web, usando termos em inglês do nicho e escreve `seeds.json`; não exige seeds nem ângulo comercial de Luigi. Crawlee visita essas URLs dentro dos limites e normaliza evidências; não é um indexador de todo o Instagram/Facebook.

```sh
python3 scripts/dispatch.py minerar --niche "saúde e beleza" --seeds CAMINHO/seeds.json --out CAMINHO/coleta
python3 scripts/dispatch.py minerar --niche "manifestação/tarot" --seeds CAMINHO/seeds.json --out CAMINHO/coleta --backend browser
```

O formato de seeds e observações está em `operacao/schema_mineracao.json`. Defaults: Instagram/Facebook, vídeos em inglês dos EUA, **últimos sete dias de calendário incluindo hoje**, no fuso `America/New_York`, **mais de 800 mil** views, conta até 30 dias de criação e conteúdo exclusivamente de avatares IA. Mostrar intervalo e fuso no relatório. Os filtros podem mudar por pedido; 70 mil seguidores não é requisito padrão. Inglês é atributo do conteúdo e não comprova EUA.

O ranking usa visualizações confirmadas entre os vídeos descobertos. O relatório separa aprovados, candidatos com evidência insuficiente e rejeitados. Identidade vídeo/perfil/URL, views, postagem, idioma, criação, país e IA exclusiva exigem fontes próprias. Primeira postagem não prova criação da conta; bio “AI” não prova todos os vídeos; snippet de busca não confirma métrica ou data de publicação. O revisor audita fonte/método e correspondência de cada campo antes da entrega.

HTTP coleta páginas públicas. O backend browser usa Crawlee/Playwright quando disponível; uma sessão autorizada pode ser usada somente se realmente acessível. Não há garantia de acesso às plataformas, nem criação automática de login/2FA. Bloqueios são registrados e evidências públicas acessíveis podem complementar candidatos sem transformar desconhecidos em aprovados. `COMPLETE`, `PARTIAL`, `BLOCKED` e `FAILED` descrevem a coleta, não aprovação dos filtros.

Entrega: links clicáveis e ranking verificado no chat, candidatos identificados com filtros faltantes e arquivos do relatório. Adaptação para Sea Moss, FitWell, Auraly ou Body Hacks é etapa posterior solicitada por Luigi, sem condicionar a descoberta do nicho à oferta.

## Lotes e fronteiras da operação

Um vídeo corresponde a uma produção e a um taskpack; análises independentes podem ocorrer em paralelo, com transcrição serial no Mac. A adaptação aguarda o `/watch` quando depende dele. Antes da entrega, conferir repetição de rota, fala e avatar entre vídeos da mesma conta. Roteiros pendentes saem juntos, numerados e bilíngues.

A aprovação de roteiro permanece com Luigi. Flow continua manual e recebe somente o bloco da produção atual. `PRODUCTION_COMPLETE` continua significando pacote textual entregue; não comprova geração, publicação ou vendas. Não há automação diária criada por esta implementação, e o Manus permanece fora do fluxo.
