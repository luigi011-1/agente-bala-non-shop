---
name: minerar-referencias
description: Minera os vídeos mais virais da semana em inglês por nicho livre, como saúde e beleza ou manifestação/tarot, no Instagram e Facebook, com evidências e links diretos.
---

# Minerar referências por nicho

## Contrato

- **Entrada:** nicho solicitado, filtros opcionais e quantidade desejada. “Minere no nicho de saúde e beleza” e “minere manifestação/tarot” já definem a pesquisa; não exigir produto, ângulo, avatar nem seeds de Luigi.
- **Entrega:** ranking por visualizações confirmadas dos vídeos encontrados, links diretos, perfil, plataforma, idioma, data, métricas e evidências; `resultados.json` e `relatorio.md`. Explicitar a cobertura da descoberta.
- **Limite:** ranking entre candidatos encontrados, sem prometer os maiores vídeos de toda a plataforma. A mineração entrega referências do nicho; adaptação para um produto exige pedido posterior.

Resolver a raiz real deste `SKILL.md`, ler `AGENTS.md` e resolver o nicho em `operacao/nichos.py`, preservando nichos livres. `operacao/angulos.json` identifica ofertas da etapa de adaptação, não termos obrigatórios de mineração. Não inserir Sea Moss, FitWell, Auraly nem Body Hacks nas consultas quando Luigi pediu apenas o nicho.

Default de “semana”: **últimos sete dias de calendário incluindo hoje**, no fuso `America/New_York`; mostrar as datas exatas no resultado. Pesquisar vídeos **em inglês**, exclusivamente no Instagram/Facebook e dos EUA. Permanecem os filtros anteriores: **mais de 800 mil** views, perfil criado há no máximo 30 dias e conteúdo exclusivamente de avatares IA, até Luigi ajustá-los. Não adicionar mínimo de seguidores. Idioma inglês não comprova localização nos EUA; cada filtro exige sua evidência.

## Pesquisa com agentes e coleta

1. O orquestrador entrega o nicho ao `bala-pesquisador`. Usar busca web disponível para descobrir URLs de vídeos/perfis em `instagram.com` e `facebook.com`. Consultar em inglês com termos do nicho, variações e janela temporal; cobrir ambas as plataformas. Não confundir data do snippet/indexação com data do vídeo.
2. O pesquisador escreve `seeds.json` com `{"urls": ["URL", "URL"]}`. Snippets descobrem candidatos, mas não confirmam filtros. Observações verificadas seguem `operacao/schema_mineracao.json` (`$defs.seeds`), com fonte, data e método ligados ao vídeo/perfil correto. Não deduzir criação pela primeira postagem, nem IA exclusiva pela bio ou por um único vídeo.
3. Crawlee é ferramenta de coleta do pesquisador, sem agente extra. Executar com nicho e limites proporcionais:

```sh
python3 "<raiz>/scripts/dispatch.py" minerar --niche "saúde e beleza" --seeds "<job>/seeds.json" --out "<job>/coleta"
python3 "<raiz>/scripts/dispatch.py" minerar --niche "manifestação/tarot" --seeds "<job>/seeds.json" --out "<job>/coleta" --backend browser
```

Usar HTTP para evidências públicas e browser quando necessário e disponível. O browser não garante acesso; usar somente sessão realmente disponível e autorizada. Se houver bloqueio/login/2FA, registrar o estado real e aproveitar evidências públicas acessíveis. Não fabricar sessão, burlar bloqueio ou prometer autonomia de autenticação.

4. Ler `approved`, `candidates`, `rejected` e o estado de coleta. Ordenar o ranking por views confirmadas; não atribuir posição confiável a vídeo sem métrica. Evidência de inglês deve ser ligada ao vídeo (fala, transcrição ou texto do conteúdo); não usar apenas bio, perfil ou país.
5. Preparar taskpack `--task revisar --niche "<nicho>" --artifact ...` e enviar resultados, fontes e seeds ao `bala-revisor` independente. Corrigir achados e registrar nova revisão da versão atual.

## Entregar no chat

Apresentar os aprovados com links clicáveis e métrica/data essenciais. Separar candidatos com filtros desconhecidos, informando exatamente quais faltam. Se nenhum vídeo passar, dizer isso e entregar apenas candidatos identificados e o relatório. Cobrir inglês, janela semanal, views, EUA, criação e IA exclusiva separadamente. `COMPLETE`, `PARTIAL`, `BLOCKED` ou `FAILED` não provam aprovação de nenhum vídeo. Não iniciar roteiro, download de vídeos, publicação ou produção sem pedido correspondente.
