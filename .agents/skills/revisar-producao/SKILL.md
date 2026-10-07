---
name: revisar-producao
description: Revisa de forma independente evidências de mineração e artefatos de vídeo da Operação Bala, identifica bloqueios e devolve um parecer estruturado sem editar a produção.
---

# Revisar produção

## Contrato

- **Entrada:** taskpack, arquivos reais da entrega, nicho/filtros para mineração ou ângulo/etapa para produção e fontes relevantes. Abrir os arquivos e formar a própria avaliação antes de aceitar as conclusões do autor.
- **Entrega:** parecer no schema `operacao/schema_revisao.json`, com status, arquivos examinados, verificações realizadas, achados com evidência e limitações de cobertura.
- **Limite:** revisão em leitura. Não corrigir arquivos, aprovar roteiro em nome de Luigi, atualizar checkpoint, executar Flow ou certificar mídia que não viu. O orquestrador salva e registra o parecer.

Resolver a raiz real por este `SKILL.md` e ler `AGENTS.md`. Em mineração, conferir o nicho e filtros do taskpack, sem exigir produto; em produção, conferir o produto pelo catálogo e o estado pelo roteador; para Auraly, ler `WORKFLOW_AURALY.md` e o checkpoint da produção antes do artefato. Não exigir um pacote final durante uma revisão de roteiro.

## Verificações relevantes

| Entrega | Conferir independentemente |
| --- | --- |
| Mineração | Nicho solicitado sem restrição indevida a produto, URLs e identidade do vídeo/perfil, ranking por views confirmadas, datas no intervalo/fuso solicitado (padrão sete dias incluindo hoje), inglês do conteúdo, EUA, criação e IA exclusiva. Conferir fonte/método de cada campo; desconhecidos não aprovam filtros. |
| `/watch` | Status real de áudio/alinhamento, cobertura da timeline, trechos-chave nos frames e correspondência de fala/timestamps; amostragem não equivale a assistir cada frame. |
| Roteiro | Oferta e mecanismo do ângulo, origem da referência, objetivo/CTA, fidelidade aplicável, sequência/timing, tabela bilíngue completa e aprovação ainda pendente quando necessária. |
| Prompts/pacote | Aprovação prévia real, fichas e evidências visuais exigidas, `GATE_VISUAL.md`, K/V e bloco Flow da produção; aplicar os validadores que os roteadores exigem. |

Uma checagem mecânica confirma apenas o que mede. Não certificar realismo de imagens não geradas, conformidade de alegações sem fonte ou resultados comerciais. Um artefato fora da etapa pedida não é evidência de aprovação. Achados precisam indicar arquivo/campo ou trecho observado e a consequência operacional, não apenas preferências de estilo.

O parecer usa `task_id` do taskpack, `reviewer: "bala-revisor"`, `independent: true`, `status`, `checks` e `findings`. Os estados são `APPROVED` (revisão técnica), `CHANGES_REQUIRED` ou `INCOMPLETE`. Cada check contém `name`, `result` (`PASS`, `FAIL`, `UNKNOWN` ou `NOT_APPLICABLE`) e `evidence`; cada achado contém `severity` (`BLOCKER` ou `WARNING`), `message` e `evidence`. `APPROVED` não aceita checks `FAIL`/`UNKNOWN` nem bloqueios.

Devolver o JSON do parecer ao orquestrador. Ele prepara o taskpack **depois da autoria** usando `--production` ou `--artifact` repetível, salva o parecer fora dos artefatos revisados e registra com:

```sh
python3 "<raiz>/scripts/dispatch.py" registrar-revisao --taskpack "<TASK.json>" --review "<REVISAO.json>"
```

O registro confere identidade e integridade dos artefatos; não muda o checkpoint nem substitui a aprovação de Luigi. Após correção, revisar os arquivos alterados novamente. Se faltarem fontes ou ferramentas necessárias, registrar a cobertura incompleta em vez de emitir aprovação total.
