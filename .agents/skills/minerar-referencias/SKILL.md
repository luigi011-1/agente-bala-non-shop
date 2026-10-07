---
name: minerar-referencias
description: Pesquisa referências de vídeos dos EUA no Instagram e Facebook para Sea Moss, FitWell, Auraly ou Body Hacks, coleta evidências com Crawlee e entrega links diretos com filtros verificados.
---

# Minerar referências

## Contrato

- **Entrada:** ângulo ou nicho explicitamente solicitado, filtros opcionais e quantidade desejada. URLs iniciais podem vir do pedido; quando não vierem, o pesquisador as encontra, sem pedir que Luigi prepare um arquivo.
- **Entrega:** links diretos dos vídeos, perfil, plataforma, data, visualizações, evidências dos filtros e relevância para o ângulo; incluir os caminhos de `resultados.json` e `relatorio.md`.
- **Limite:** pesquisa pública. Sessão, país, data de criação e uso exclusivo de avatares IA precisam de evidência; login, bloqueio ou informação oculta não autorizam contorno nem suposição.

Resolver a raiz real por este `SKILL.md`, ler `AGENTS.md` e o preset em `operacao/angulos.json`. Os defaults são Instagram/Facebook, EUA, vídeos de hoje e ontem, **mais de 800 mil** views, perfil criado há no máximo 30 dias e apenas avatares IA. “Hoje” usa `America/New_York` e aparece no relatório; respeitar outro fuso/filtro que Luigi solicitar. Não acrescentar um mínimo de seguidores de um exemplo antigo.

## Pesquisar e coletar

1. Usar a busca web disponível para descobrir URLs públicas de vídeos e perfis nos dois domínios oficiais. Fazer consultas em inglês adequadas ao preset. Auraly pode pesquisar tarot se solicitado; a oferta permanece Auraly. Não presumir que a pesquisa encontrou todos os vídeos existentes.
2. Escrever `seeds.json` com `{"urls": ["URL", "URL"]}` no job. Snippets de buscador descobrem candidatos, mas não confirmam métricas ou filtros. Quando houver observações verificadas, seguir `operacao/schema_mineracao.json` (`$defs.seeds`); registrar fonte, data de observação e método. Não marcar IA exclusiva só pela bio ou aparência de um único vídeo. A primeira publicação visível não é a criação da conta.
3. Executar coleta limitada; `--angle` recebe o slug do catálogo:

```sh
python3 "<raiz>/scripts/dispatch.py" minerar --angle sea-moss --seeds "<job>/seeds.json" --out "<job>/coleta"
```

Opções reais: `--timezone`, `--today YYYY-MM-DD`, `--max-pages`, `--max-seconds`, `--concurrency`, `--min-views`, `--lookback-days` e `--max-profile-age-days`. Manter limites proporcionais à pesquisa; o default não inicia uma varredura ilimitada.
4. Ler o resultado. `approved` reúne quem satisfaz os filtros com evidência; `candidates` reúne campos desconhecidos; `rejected` registra filtros incompatíveis. `BLOCKED`, `PARTIAL` ou `FAILED` são estados de coleta, sem virar uma pesquisa concluída por redação.

## Entregar

Enviar primeiro os vídeos aprovados numa lista ou tabela curta com links clicáveis e a evidência essencial. Se só houver candidatos, declarar quais filtros ainda faltam e entregar os links como candidatos, sem relaxar silenciosamente os critérios. Quando nenhum vídeo puder ser aprovado, dizer isso e manter o relatório acessível. Não iniciar roteiro, downloads de vídeo, publicação ou produção a partir desta skill sem pedido correspondente.
