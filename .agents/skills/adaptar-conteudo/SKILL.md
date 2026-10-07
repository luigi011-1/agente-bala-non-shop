---
name: adaptar-conteudo
description: Adapta vídeo ou copy de referência ao produto e avatar de Sea Moss, FitWell, Auraly ou Body Hacks, entregando a próxima etapa canônica e preservando a aprovação do roteiro.
---

# Adaptar conteúdo

## Contrato

- **Entrada:** ângulo definido, referência analisada ou copy fornecida, produção ativa, objetivo e avatar quando a etapa exigir. Recuperar decisões do checkpoint e dos arquivos existentes.
- **Entrega:** somente os artefatos da próxima etapa. Roteiro final em `take | English | Português`, completo e com takes mudos; depois da aprovação, os prompts e o bloco Flow próprios da produção.
- **Limite:** não aprovar o próprio roteiro, reescrever etapa aprovada, inventar dados do produto ou trocar oferta. Pacote textual não significa mídia gerada.

Resolver a raiz real por este `SKILL.md`. Ler `AGENTS.md`, identificar o ângulo por `operacao/angulos.json` e seguir o roteador do preset. Para Auraly, `WORKFLOW_AURALY.md` → `CHECKPOINT.md` → `Next action` é a única cadeia de estado. Para 1, 2 e 4, usar `CLAUDE.md` como índice, com a doutrina atual do produto. Carregar `produzir`, `avatar-realista` ou `gancho-verbal` em `.claude/skills/` somente quando a etapa pedir e com a precedência de `AGENTS.md`.

```sh
python3 "<raiz>/scripts/dispatch.py" preparar --angle 2 --task adaptar --production "<pasta-da-producao>" --out "<pasta-do-job>"
```

## Executar a próxima etapa

- Se o vídeo ainda não foi decomposto, usar `$watch` antes de afirmar ações, herói do hook ou reveals. Transcrição não substitui frames; WhisperX melhora o alinhamento da fala, sem interpretar o visual.
- Classificar a referência conforme as fontes canônicas: pessoa real orgânica usa `PERFIL_ORGANICO.md`; copy de anúncio escalado colada “como base” extrai dores e mecanismo para nossa redação. Essas duas entradas têm regras de fidelidade diferentes.
- Preservar o produto: Sea Moss é suplemento Amazon; FitWell é APP; Auraly é APP; Body Hacks é ebook para homens 40+. O CTA segue o modo orgânico/pago e a exceção Auraly registrados nos roteadores atuais.
- Roteiro novo termina na entrega bilíngue e na espera por aprovação real de Luigi. Não inferir aprovação de um arquivo existente nem de um parecer técnico.
- Prompts e ganchos passam pelo `GATE_VISUAL.md`; FitWell/Auraly levam a ficha do frame e as evidências exigidas. Usar os validadores canônicos apropriados à etapa, sem chamar um teste de pacote antes de o pacote existir.
- Na etapa de pacote, entregar K/V e o bloco Flow apenas desta produção conforme os arquivos canônicos. O executor continua manual. O modo pago FitWell de vídeo para vídeo segue a exceção específica do roteador.

Passar os artefatos a `$revisar-producao` num subagente independente antes do envio final. Corrigir problemas observáveis, preservar decisões aprovadas e registrar a revisão. Estado, entregas e evidências vêm dos arquivos reais; não acrescentar rodadas de variação ou tarefas de publicação por iniciativa própria.
