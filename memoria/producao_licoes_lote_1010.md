---
name: producao-licoes-lote-1010
description: "Primeiro lote completo no Mac (2026-10-10, 3 vídeos FitWell growth da holistic.brandon, do /watch ao vídeo editado): o que FAZER e o que NÃO fazer no processo de produção (roteiro, pacote, Flow, entrega e fila de edição). Ler no começo de toda produção dos Ângulos 1, 2 e 4"
metadata:
  node_type: memory
  type: feedback
  originSessionId: c642df4f-f1fb-40d0-8d3c-047fd36bab5f
  modified: 2026-10-10T06:20:46.840Z
---

Lote de 2026-10-10: `fitywell_growth_temperos_falsos`, `fitywell_growth_chips_azeite` e
`fitywell_growth_canela_saude` (holistic.brandon, growth), do vídeo modelo até o vídeo editado. Lições da
edição em [[edicao-licoes-teste]]; ambiente do Mac em [[ambiente-mac-luigi]].

**Why:** cada item abaixo custou retrabalho ou quase saiu errado neste lote. Pedido do Luigi: registrar erros
E acertos para os próximos vídeos saírem certos de primeira.

**How to apply:**

FAZER (acertos que viram regra)
- Antes de produzir: memória viva restaurada (`restaurar_memoria.sh`) e ambiente do `/watch` pronto.
- `/watch` em todos os vídeos e abrir as folhas de cenas ANTES da copy; classificar origem (IA x real) e
  objetivo (growth x venda) logo no começo.
- Growth: clonar quase palavra por palavra; mudar só o que não cabe na boca do avatar (o "In Japan" virou
  frase de coach). Registro de outra oferta (manifestação, universo, selos, Stories) é reescrito para o
  registro da marca mantendo estrutura e ritmo ([[feedback-growth-video-sem-venda]]).
- Riscos (álcool no gancho, claim de saúde) vão listados no roteiro para o Luigi decidir, nunca cortados calado.
- Contar palavras por SCRIPT, não de cabeça (três contagens da tabela estavam erradas).
- `checar_frases.py` em cada roteiro do lote: pegou o CTA idêntico entre dois vídeos da mesma conta.
- Pacote pelo gerador comum `producao/_flow/pacote_minimo.py` (K em parágrafo, V só com a fala, ENTREGA,
  AGENTE_FLOW, FICHA_FRAMES e PROMPTS_PRODUCAO): todos os K saíram com 0 negações, 0 gatilhos e bandeira.
- Vídeo de plano único no modelo: 1 K para o gancho + 1 K para o plano, e vários V da mesma imagem
  (canela: 2 K para 14 V). Menos imagem para gerar e continuidade de plano igual ao modelo.
- Nenhum take mudo com fala por cima ([[take-mudo-so-sem-voz]]): todos os takes falados, a edição não travou.
- Edição em fila, um vídeo depois do outro, avisando a cada um com caminho e segundos das emendas.

NÃO FAZER (erros cometidos)
- Não escrever o ROTEIRO só com tabelas: o linter e o `checar_frases.py` só leem `### T1 · BEAT · TALKING ·
  Setup A` + `> "fala"`. Escrever as seções desde o início.
- Não esquecer no ROTEIRO a seção `## Notas de produção` (com esse nome) e "Ângulo 2" no cabeçalho: sem
  isso o linter reprova as seções e pula a checagem da keyword (o v5 de 2026-10-09 saiu assim).
- Não mandar o agente do Flow "olhar o mapa na entrega": ele só tem a memória e os prompts. Mapa K/V por
  extenso dentro do bloco do agente.
- Não confiar que as pastas de takes continuam no Desktop: o Luigi pega o vídeo e move a pasta. Copiar o
  editado para a pasta assim que sair e re-renderizar logo, antes de passar para o próximo.
- Não montar laço de shell com `set -- $var` no zsh (não separa os argumentos): rodar os comandos explícitos.
- Não reaproveitar itens velhos do checklist de envio que o padrão novo do Flow revogou (C2 voz no V, C8
  5 blocos): marcar N/A com o motivo.
