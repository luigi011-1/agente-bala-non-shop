# Operação Bala: execução por skills e revisão independente

Esta camada conecta as ferramentas e distribui o trabalho. `AGENTS.md` continua como entrada canônica; `WORKFLOW_AURALY.md`, `CLAUDE.md`, `GATE_VISUAL.md` e o checkpoint continuam governando produção e aprovações. Os taskpacks registram uma execução, sem criar outro workflow.

## Ângulos

`operacao/angulos.json` é o catálogo consumido pelos comandos. Seus presets identificam o produto e apontam as doutrinas existentes.

| ID / slug | Oferta atual | Pesquisa padrão |
| --- | --- | --- |
| 1 / `sea-moss` | Natural Rems Sea Moss 16-in-1 Gummies, suplemento Amazon | Saúde, nutrição, bem-estar, sea moss e envelhecimento saudável |
| 2 / `fitwell` | FitWell / FityWell APP, público 40+ | Saúde, fitness, perda de peso e hábitos 40+ |
| 3 / `auraly` | Auraly APP | Manifestação, soulmate, sincronicidade, sinais e prosperidade; tarot quando solicitado |
| 4 / `body-hacks` | Body Hacks For Men 40+, ebook FitWell | Saúde e hábitos de homens 40+ |

Korella Saffron é histórico e não resolve silenciosamente para uma oferta ativa. Não confundir o APP FitWell com o ebook Body Hacks.

## Skills e responsáveis

| Skill | Entrada principal | Entrega / limite |
| --- | --- | --- |
| `$operacao-bala` | Pedido e ângulo, produção quando aplicável | Contexto mínimo, delegação e resultado revisado; mantém as aprovações do workflow |
| `$minerar-referencias` | Ângulo ou nicho e filtros opcionais | Links IG/FB com evidências e relatório; pesquisa pública, sem fabricação de acesso |
| `$watch` | Arquivo de vídeo | Frames, transcrição e decomposição visual; não significa produção completa |
| `$adaptar-conteudo` | Referência analisada, produto, objetivo e avatar | Próxima etapa canônica; roteiro completo aguarda aprovação de Luigi |
| `$revisar-producao` | Taskpack e artefatos finais | Parecer independente em leitura; não edita nem aprova por Luigi |

O Codex atua como orquestrador principal. Existem dois especialistas e um revisor em `.codex/agents/`: `bala-pesquisador`, `bala-produtor` e `bala-revisor`. Os perfis herdam o modelo; o revisor usa sandbox de leitura. Não criar um agente por ferramenta ou por avatar. Se a ferramenta de delegação só aceitar instruções, carregar o texto do perfil no subagente; se não houver subagentes disponíveis, informar que a revisão independente ficou pendente.

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
python3 scripts/dispatch.py preparar --angle sea-moss --task minerar
python3 scripts/dispatch.py preparar --angle auraly --task adaptar --production producao/NOME
```

Cada execução cria `TASK.json` e `DISPATCH.md`, com ângulo, estado e fingerprints das fontes. Para Auraly, uma produção ativa exige checkpoint válido. As tarefas são `minerar`, `watch`, `adaptar` e `revisar`. O contexto referencia as fontes da etapa em vez de despejar todas as memórias.

Depois da autoria, preparar uma nova tarefa de revisão para a versão final:

```sh
python3 scripts/dispatch.py preparar --angle auraly --task revisar --production producao/NOME
python3 scripts/dispatch.py preparar --angle sea-moss --task revisar --artifact CAMINHO/resultados.json --artifact CAMINHO/relatorio.md
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

## Mineração com Crawlee

O pesquisador descobre links públicos via busca web e escreve `seeds.json`; Luigi não precisa preparar seeds. O coletor visita as URLs dentro dos limites e normaliza as evidências. Não é um indexador de todo o Instagram/Facebook.

```sh
python3 scripts/dispatch.py minerar --angle sea-moss --seeds CAMINHO/seeds.json --out CAMINHO/coleta
```

O formato de seeds e das observações está em `operacao/schema_mineracao.json`. Defaults: Instagram/Facebook, EUA, vídeos de hoje e ontem no fuso `America/New_York`, **mais de 800 mil** views, conta com até 30 dias de criação e conteúdo exclusivamente de avatares IA. Os filtros podem ser ajustados no pedido; 70 mil seguidores não é um requisito padrão.

O relatório contém aprovados, candidatos com dados desconhecidos e rejeitados. Métricas, criação, país e IA exclusiva exigem provas; a primeira postagem não prova a criação da conta e uma bio “AI” não prova todos os vídeos. Se a plataforma ocultar dados ou bloquear a consulta, registrar essa condição e entregar candidatos claramente identificados. O estado de coleta `COMPLETE`, `PARTIAL`, `BLOCKED` ou `FAILED` não significa que algum vídeo necessariamente passou nos filtros.

## Lotes e fronteiras da operação

Um vídeo corresponde a uma produção e a um taskpack; análises independentes podem ocorrer em paralelo, com transcrição serial no Mac. A adaptação aguarda o `/watch` quando depende dele. Antes da entrega, conferir repetição de rota, fala e avatar entre vídeos da mesma conta. Roteiros pendentes saem juntos, numerados e bilíngues.

A aprovação de roteiro permanece com Luigi. Flow continua manual e recebe somente o bloco da produção atual. `PRODUCTION_COMPLETE` continua significando pacote textual entregue; não comprova geração, publicação ou vendas. Não há automação diária criada por esta implementação, e o Manus permanece fora do fluxo.
