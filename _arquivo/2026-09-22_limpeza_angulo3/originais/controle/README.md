# Biblioteca e resultados

Este diretório apoia consulta e medição. A operação continua nos roteadores do projeto: AGENTS.md, WORKFLOW_AURALY.md e checkpoint para Auraly; CLAUDE.md para Angle 1/2. Nenhum comando aqui inicia geração, publica vídeo ou aprova uma etapa.

A [biblioteca criativa](BIBLIOTECA_CRIATIVA.md) indexa os 36 roteiros encontrados inicialmente, com oferta, objetivo explícito, variável/ponte e enquadramento. O JSON inclui referência, avatares, abertura e estado documentado. É uma extração dos documentos, não confirmação de suas alegações ou resultados. Objetivos ausentes ficam vazios; um funil com link, por si só, não foi convertido em aprovação formal de SALE. Angle 4 fica separado como histórico.

As [rotas de consulta](ROTAS_DE_CONSULTA.md) ajudam a encontrar exemplos e a formular testes criativos. Os [resultados](RESULTADOS.md) só mostram métricas fornecidas pelo operador.

## Comandos

Execute na raiz do projeto, com Python 3.10 ou superior. Não há dependências externas.

```sh
python3 gerenciar_operacao.py atualizar
python3 gerenciar_operacao.py buscar --angulo 2
python3 gerenciar_operacao.py buscar --angulo 3 --termo segredo
python3 gerenciar_operacao.py validar
python3 -m unittest discover -s tests -v
python3 checar_entrega.py producao/barbie_the_aries_1_kris_robin_shelby_casey --estrito
```

`atualizar` valida resultados antes de regenerar os índices e o relatório. Edite os documentos fonte, nunca os índices gerados. Em Windows, use `python` se esse for o executável instalado.

Para conferir uma fila derivada antes de aplicar:

```sh
python3 gerenciar_operacao.py sincronizar-fila producao/barbie_the_aries_1_kris_robin_shelby_casey
```

Adicionar `--aplicar` grava apenas a vista AVATAR_QUEUE.md, preservando nomes e anchors. O comando recusa identidades diferentes. Ele não decide quem terminou; copia estados do checkpoint. Sem checkpoint, registre primeiro a decisão real pelo workflow, sem inventar aprovações históricas.

## Como registrar uma publicação

`resultados.json` começa vazio. Adicione em `publicacoes` um objeto por vídeo efetivamente publicado. O mesmo vídeo em outra conta ou canal recebe outro ID. Ao atualizar uma coleta, substitua as métricas da mesma publicação; não acrescente uma segunda linha que conte novamente suas visualizações. Guarde exportações brutas separadamente e cite a origem em `observacoes`.

Campos obrigatórios:

| Campo | Conteúdo |
|---|---|
| id | ID estável da publicação, incluindo conta/plataforma quando necessário |
| producao_id | Nome exato da pasta de produção |
| avatar_id | Identidade estável do avatar; nunca posição na fila |
| hook_id | Código do hook efetivamente usado, por exemplo K01 |
| objetivo | SALE ou GROWTH, conforme decisão da produção |
| canal | Plataforma e conta |
| publicado_em / coletado_em | Data/hora ISO 8601 com fuso, como `2026-09-14T10:00:00-03:00` |

Campos opcionais, omitidos ou `null` quando desconhecidos:

- Contagens inteiras: `impressoes`, `visualizacoes`, `reproducoes_3s`, `conclusoes`, `curtidas`, `comentarios`, `salvamentos`, `compartilhamentos`, `seguidores`, `cliques`, `visitas_destino`, `compras`.
- Valores não negativos: `receita`, `custo`, `minutos_trabalho`. Receita/custo exigem `moeda`, como BRL ou USD. Use o mesmo escopo de custos entre comparações.
- Contexto: `url`, `observacoes`. Anote origem, janela de atribuição e definições de métricas. Seguidores significa novos seguidores atribuídos ao vídeo, não total da conta.

Zero significa que o valor foi medido e é zero. `null` significa que não há dado. Não atribua vendas agregadas da conta a um vídeo sem rastreamento. Não some diferentes moedas ou publicações com períodos sobrepostos para inferir retorno.

O relatório calcula 3s/visualizações, conclusões/visualizações, cliques/impressões, compras/visitas e receita/custo somente quando existe denominador positivo. As definições precisam ser compatíveis na plataforma; a validação estrutural não verifica isso. Compare hooks da mesma oferta, objetivo, conta e janela. Um vídeo de crescimento não deve ser julgado apenas por vendas.

## Limites do gate de entrega

O gate verifica texto, códigos, cobertura de falas, correspondência de K/V e coerência documental do estado. Não inspeciona vídeos renderizados, fidelidade visual, seleção manual de imagens ou desempenho. Arquivos históricos sem checkpoint recebem aviso; `--estrito` exige checkpoint. Pacotes parciais devem ter `lote` ou `ciclo` no nome e não comprovam cobertura integral do roteiro. Falhas históricas não autorizam reescrever copy aprovada automaticamente.
