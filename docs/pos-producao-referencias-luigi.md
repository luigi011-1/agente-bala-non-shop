# Edições de referência do Luigi (2026-10-09)

Duas edições feitas à mão pelo Luigi, mandadas como **o padrão de edição que ele gosta**. A edição
automática mira nelas. Os vídeos ficam fora do repo (pastas dele no Mac).

| | FitWell | Auraly |
|---|---|---|
| Arquivo | `AVATARES/avatares fitywell/holistic brandon/POSTADOS/esse ta do krl pro fitywell - 30.09.mp4` | `AVATARES/avatares appyon/Avery Knox/ctvs Avery Knox - 09.10-1.mp4` |
| Vídeo | holistic.brandon, brownie de feijão preto (growth com CTA `yes` + link) | Avery Knox, "porch light seal" (venda, `222` + Stories) |
| Duração / palavras | 63,9s / 242 | 94,3s / 380 |
| **Ritmo** | **3,8 palavras/s** | **4,0 palavras/s** |
| Silêncio > 0,15s | nenhum (nem a -45 dB) | nenhum (nem a -45 dB) |
| Volume final | -15,2 LUFS | -12,8 LUFS |
| Cortes de cena | receita em cortes de 1,5 a 2s (amassar, ovos, cacau, mel, canela, forma, forno) e depois um plano só falando com o brownie na mão | praticamente um plano só (cartas na mão no gancho, depois só ela falando) |
| Flash / light leak | **nenhum** | **um flash claro** na saída do gancho (6,4s) |
| Zoom | nenhum | nenhum |

## Legenda

**FitWell = o estilo v3 que o editor já faz.** Serifada branca em negrito, minúscula, sombra suave,
2 a 3 palavras por página, estática, no centro da altura do peito. Nos planos da receita (mãos e
tigela) fica no meio do quadro, acima do ingrediente.

**Auraly = estilo próprio, diferente do FitWell:**
- A página se monta **palavra por palavra no tempo da fala** e empilha até 3 linhas curtas
  (`it's` → `it's / meant` → `it's / meant / for you`), depois limpa e começa outra.
- **Uma palavra-chave por página fica bem maior** (cerca de 2,5x): `next`, `money`, `found`,
  `resumes`, `212`, `somewhere`, `isn't`. É a palavra de peso da frase (número, dinheiro, ação).
- Mesma fonte serifada branca, minúscula, com sombra/brilho suave; no centro do peito, sobre o colar.
- **Selos fixos do canal** o vídeo inteiro: `🇺🇸777🇺🇸` pequeno à direita na altura do rosto e
  `🔮222🔮` pequeno à esquerda na altura do peito (marca d'água do número, como manda o CLAUDE.md).
  **Valem para TODOS os avatares do Auraly** (Avery, Jordan, Devon e os próximos; Luigi, 2026-10-10).

## No editor (aprovado e implementado, Luigi, 2026-10-10)

1. **Ritmo dopaminérgico:** a velocidade é calculada em cada vídeo para chegar a **3,8 palavras/s**
   (FitWell e os outros ângulos) ou **4,0** (Auraly), entre 1,0x e 1,25x. Vídeo que já fala nesse ritmo
   fica em 1,0x. `--ritmo` muda o alvo.
2. **Sem light leak no FitWell.** No Auraly, um flash claro só na saída do gancho (entrada do take 2).
3. **Legenda do Auraly no estilo da referência:** monta palavra por palavra, empilha até 4 palavras,
   palavra-chave grande (número, palavra forte ou a mais longa), selos `🇺🇸777🇺🇸` e `🔮222🔮`.
   O estilo é escolhido sozinho pela produção (pasta com `auraly` ou `pipeline: auraly`); `--estilo` força.
4. **Música:** continua a -25 dB da voz.
5. Os selos usam a fonte de emoji do sistema: no Mac sai certo; numa máquina sem fonte de emoji colorido
   (nuvem Linux sem Noto Color Emoji) as bandeiras e a bola de cristal podem sair sem desenho.

Mais referências dos dois nichos vão chegar (Luigi, 2026-10-10): medir e ajustar estes números.
