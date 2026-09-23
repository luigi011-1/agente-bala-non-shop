---
name: validar-antes-de-variar
description: "Producao nova a partir de video modelo e RODADA DE VALIDACAO: um gancho so, fiel ao modelo, sem as 10 variacoes. As 10 (Puzzle com degrau) so existem depois que o Luigi disser que um video postado performou, e partem do video validado. Vale nos tres angulos (Luigi, 2026-09-23)"
metadata:
  type: feedback
---

Em 2026-09-23 o Luigi mudou o comeco do workflow: **validar antes de variar**, nos tres angulos.
Fonte canonica: `GATE_VISUAL.md` Parte 4, Passo 0.

**Why:** os videos nao estavam pegando views e ele identificou a causa em falta de teste. Ele gerava
em media 5 variacoes do mesmo roteiro por avatar, mudando so o gancho, sobre um video que viralizou
no perfil de OUTRA pessoa e nunca tinha sido validado no dele. Palavras dele: *"como posso ja estar
criando variacoes sendo que nem validei no meu perfil primeiro?"*. Se a base nao pega com o publico
dele, as 5 flopam juntas e nao se aprende nada; se uma vai bem, nao ha base validada para comparar.

**How to apply:**
- Producao nova = `Round: VALIDATION` / `Rodada: VALIDACAO`. UM gancho, o do video modelo, com o
  maximo de fidelidade (acao, heroi, objeto, local, enquadramento, cortes, timing, abertura muda ou
  falada, texto de tela traduzido). So muda o obrigatorio (identidade, travas do angulo, moderacao,
  realismo), e cada desvio vai declarado com o motivo.
- O gancho fiel e aprovado **junto com o roteiro**. Sem 10, sem degrau, sem controle, sem espera de
  selecao de gancho. Aprovado o roteiro, direto para os prompts.
- **O resto do workflow nao muda** (fila de avatares, pacote por avatar, bloco do Flow, K/V,
  transcricoes, checklist de envio, linter). Ele disse isso explicitamente.
- A rodada de variacao so abre quando o Luigi disser que um video postado performou. **Nunca por
  iniciativa minha** e o criterio de "performou" e dele. Base = o video validado como foi postado,
  registrado em `Base validada:` / `Validated from:` e em `controle/resultados.json` (P10).
- Revoga, so na validacao, o *"nunca refazer o viral igual"* do step up e a pergunta de
  [[feedback-perguntar-ganchos-fisicos]]. O Puzzle com degrau de [[ganchos-variacao-puzzle]] continua
  inteiro para a rodada de variacao.
- O linter cobra: `Rodada:` no `GANCHOS_VISUAIS.md` e `Round:` no checkpoint Auraly
  (`auraly_validacao.py`).
