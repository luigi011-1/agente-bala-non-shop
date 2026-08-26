# memoria/ — ESPELHO, não é a fonte de verdade

**Não edite nada aqui.** Toda edição feita nesta pasta é perdida no próximo sync.

## O que é isto

A memória viva do agente fica em:

```
~/.claude/projects/C--Users-luigi-Desktop-AGENTE-NON-SHOP/memory/
```

É lá que o Claude Code lê e escreve. Esta pasta é só um **espelho versionado**, que existe
por dois motivos: backup fora da máquina, e histórico de como a doutrina foi mudando ao
longo do tempo (`git log memoria/banco_rotas_argumentativas.md` mostra cada regra nascendo).

## Como atualizar

```
powershell -ExecutionPolicy Bypass -File sync_memoria.ps1
```

Roda da raiz do repo. Ele compara por hash, copia o que mudou, apaga daqui o que foi
apagado lá, e imprime o que entrou, o que mudou e o que saiu.

**Rodar ANTES de todo commit que envolva memória.**

## Por que isso é uma regra e não uma sugestão

Este projeto já foi mordido exatamente por isto. O `PORTÃO P10` do `CLAUDE.md` existe porque
documentos que ninguém atualiza envelhecem em silêncio, e aí o agente repete decisão achando
que é nova. Um espelho desatualizado é pior que espelho nenhum: ele parece confiável.

Se você abrir um arquivo daqui e ele contradisser o comportamento do agente, **o agente está
certo e o espelho está velho.** Rode o sync.
