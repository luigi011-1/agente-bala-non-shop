---
name: operacao-bala
description: Orquestra mineração semanal por nicho no Instagram/Facebook, análise /watch e produção dos quatro ângulos, com pesquisador, produtor e revisão independente.
---

# Operação Bala

## Contrato

- **Entrada:** pedido de Luigi e nicho para mineração; ângulo, vídeo, pasta de produção, conta e avatar conforme a etapa de produção. Mineração por nicho não exige escolher produto ou ângulo. Reaproveitar informações do pedido/checkpoint; perguntar somente pelo que impede a próxima ação.
- **Entrega:** a próxima etapa completa do workflow canônico, com arquivos, referências, revisão independente e o estado real. Em mineração, entregar links diretos no chat; em roteiro, a tabela bilíngue completa para aprovação.
- **Limite:** esta skill organiza execução e contexto. O roteiro continua dependendo da aprovação de Luigi; gerar mídia, executar Flow, publicar ou fazer merge não fazem parte dela.

## Preparar e rotear

Resolver o caminho real deste `SKILL.md` (inclusive quando instalado por symlink) e localizar a raiz que contém `AGENTS.md` e `operacao/angulos.json`. Executar comandos com caminhos absolutos, sem depender da pasta atual do chat.

1. Ler `AGENTS.md`. Em mineração, resolver o nicho solicitado em `operacao/nichos.py` ou preservar o nicho livre e seguir `$minerar-referencias`; “saúde e beleza” e “manifestação/tarot” bastam. Consultas não recebem termos do produto sem pedido. Em adaptação, resolver o ângulo em `operacao/angulos.json`: Sea Moss é suplemento, FitWell e Auraly são APPs, Body Hacks é ebook; Korella é histórico. Definir oferta antes de adaptar, nunca antes da pesquisa independente de nicho.
2. Em produção Auraly: `WORKFLOW_AURALY.md` → `CHECKPOINT.md` da produção → somente `Next action` e as fontes indicadas para essa etapa. Nos demais ângulos, `CLAUDE.md` roteia os arquivos necessários. Não carregar todas as memórias nem reabrir etapas aprovadas.
3. Preparar um taskpack por tarefa e produção:

```sh
python3 "<raiz>/scripts/dispatch.py" preparar --niche "saúde e beleza" --task minerar --out "<pasta-do-job>"
python3 "<raiz>/scripts/dispatch.py" preparar --angle 3 --task adaptar --production "<pasta-da-producao>" --out "<pasta-do-job>"
```

As tarefas são `minerar`, `watch`, `adaptar` e `revisar`. O taskpack registra o escopo e as fontes; não é aprovação nem outro checkpoint. Se o preflight indicar dependência ausente, usar a preparação do ambiente descrita em `OPERACAO_AGENTES.md` e conferir novamente antes de afirmar que o recurso funciona.

## Delegar com contexto mínimo

Usar só estes perfis em `.codex/agents/`:

| Perfil | Trabalho e saída |
| --- | --- |
| `bala-pesquisador` | Descobre vídeos por nicho com busca web, usa Crawlee como ferramenta e verifica métricas/idioma; ou decompõe vídeo com `$watch`. Entrega links, timestamps, evidências e incertezas. |
| `bala-produtor` | `$adaptar-conteudo`; somente os artefatos da próxima etapa autorizada. |
| `bala-revisor` | `$revisar-producao`; leitura independente e parecer estruturado, sem editar os artefatos. |

Quando a ferramenta permitir escolher agente customizado, usar o perfil. Quando aceitar apenas uma instrução, enviar ao subagente as `developer_instructions` do TOML correspondente, o taskpack e os caminhos necessários. Não inventar uma ferramenta de delegação indisponível.

A mineração percorre pesquisador → ferramenta Crawlee → revisor independente → entrega no chat. Crawlee não recebe um agente próprio. O produtor só participa quando Luigi pedir adaptação de uma referência para uma oferta. Pesquisar e adaptar podem ocorrer em paralelo apenas se não houver dependência entre as tarefas. A adaptação que depende do `/watch` aguarda a análise. Executar um ASR por vez no Mac; não duplicar transcrição para cada avatar. Em lote, um taskpack e uma produção por vídeo; conferir repetições na mesma conta e agrupar roteiros pendentes numa mensagem numerada.

Depois da autoria, preparar um novo taskpack `--task revisar` para capturar os artefatos finais: usar `--production` para a produção ou `--artifact` repetível para saídas de mineração e `/watch`; revisão de mineração usa `--niche` e mantém filtros/intervalo da pesquisa. Enviar esse taskpack e os arquivos reais a um revisor separado. O autor corrige achados e prepara nova revisão do que mudou. Registrar o parecer com `registrar-revisao` conforme `$revisar-producao`; uma aprovação mecânica não substitui essa leitura. Se não houver ferramenta de subagente, a execução pode avançar nas partes independentes, mas informar que a revisão independente está pendente.

## Encerrar a etapa

Entregar resultado e links no chat; atualizar estado canônico somente por fatos e ações já autorizadas. `WAITING_SCRIPT_APPROVAL` aguarda Luigi. `PRODUCTION_COMPLETE` é entrega textual do pacote, sem inferir mídia gerada ou publicada. Mineração, extração de frames e transcrição não provam qualidade criativa nem resultado comercial.
