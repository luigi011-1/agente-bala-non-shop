---
name: sync-memoria-apaga-readme
description: "O sync_memoria.ps1 apaga memoria/README.md em TODA execucao, porque o README e escrito a mao e nao tem contrapartida na origem. Restaurar com git checkout antes de commitar. Correcao em andamento desde 2026-08-26."
metadata:
  type: project
---

# `sync_memoria.ps1` apaga o `memoria/README.md` em toda execução

Descoberto em 2026-08-26. O script espelha `~/.claude/projects/.../memory/` para `memoria/` e
**apaga do destino tudo que não existe na origem**. O `memoria/README.md` é documentação escrita
à mão sobre o espelho (explica que a pasta não é a fonte de verdade), não é um arquivo espelhado,
então o script o trata como "removido lá" e deleta. A saída mostra `REMOVIDOS (1): - README.md`.

**Enquanto não estiver corrigido, depois de todo sync:**

```
git checkout -- memoria/README.md
```

Conferir no `git status` antes de commitar. Já aconteceu três vezes em um único dia.

**Why:** commitar essa deleção apaga em silêncio a única documentação de como o espelho funciona,
que é justamente o arquivo que impede alguém de editar `memoria/` na mão. Ver [[workflow-entrega-gabarito]].

**How to apply:** rodar o sync, restaurar o README, só então `git add`. Uma correção do script foi
posta em andamento em 2026-08-26 (excluir o README da varredura de deleção). **Se o sync parar de
reportar `REMOVIDOS`, a correção entrou e esta memória pode ser apagada.**
