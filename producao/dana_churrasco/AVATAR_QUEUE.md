# AVATAR_QUEUE · producao/dana_churrasco

Produção multi-avatar. **A fila é estado em disco, nunca conversa.**
Roteiro, takes, falas, gancho e ordem de K e V foram aprovados **uma vez**, em 2026-09-12, e valem
para todos. Cada avatar muda identidade, âncora, cenário, registro e as frases que dependem de idade.

| # | Avatar | Âncora | Estado | Pacote |
|---|---|---|---|---|
| 1 | **Dana Morrison** (52) | `producao/_ancoras/dana_morrison_ancora.jpeg` | `DONE` | `PROMPTS_DANA_MORRISON.md` |
| 2 | **Lynn Parker** (70) | `producao/_ancoras/lynn_parker_ancora.jpeg` | `ACTIVE` | `PROMPTS_PRODUCAO.md` |
| 3 | **Jamie Anderson** (55) | `producao/_ancoras/jamie_anderson_ancora.jpeg` | `PENDING` | ainda não escrito |

**Concluir um avatar nunca encerra a produção.** Só existe `PRODUCTION COMPLETE` quando não houver
`PENDING` nem `ACTIVE`.

---

## 🔑 O QUE SE REAPROVEITA ENTRE AVATARES, e é muito

No movie style integral, **os atos que não têm o avatar em quadro são os mesmos para todos.** O ato
1 no quintal e o ato 2 no consultório e na picape são Nia, Keith e Terrell, e nenhum deles muda.

| Ativo | Dana | Lynn | Jamie |
|---|---|---|---|
| REF-NIA, REF-KEITH, REF-TERRELL, REF-LIVRO | gerar | **reusar** | **reusar** |
| K01, K02, K03, K04 | gerar | **reusar** | **reusar** |
| V01, V02, V03, V04, V05 | gerar | **reusar** | **reusar** |
| K06, K11, K12, K13 | gerar | gerar | gerar |
| V06 a V13 | gerar | gerar | gerar |

**Custo do primeiro avatar:** 4 REF, 8 keyframes, 13 clipes.
**Custo de cada avatar seguinte:** 4 keyframes e 8 clipes. Menos da metade.

⚠️ **O K11 entra na lista de regerar** mesmo sendo o Terrell, porque ele acontece dentro do cenário
do mentor e a fala dele cita a idade do mentor.

---

## AS FALAS QUE MUDAM POR AVATAR

Três takes dependem do avatar. O resto é idêntico, palavra por palavra.

| Take | Dana Morrison (52) | Lynn Parker (70) |
|---|---|---|
| **T6** | "You have been sitting at the end of my driveway for ten minutes, brother. Come in, or go home." | "You have been standing in my doorway for ten minutes, brother. Sit down, or go home." |
| **T11** | "How do you know that? You are **fifty two** and you talk like it never left. So what changed it for you?" | "How do you know that? You are **seventy** and you talk like it never left. So what changed it for you?" |
| **T12** | "...That is where I started." | "...**Forty years, and nobody ever handed me that list.**" |

**Por que o T12 muda.** O Lynn é o único do roster que pode dizer *"em quarenta anos eu vi"*, e a
ficha dele define autoridade por vivência pura. Trocar o fecho aproveita o ativo dele em vez de
repetir a frase do Dana, que era de par de idade próxima.

**Por que o T6 muda.** O Dana tem garagem com entrada de carro. O Lynn tem apotecário dentro de
casa, sem garagem e sem entrada, então *driveway* viraria incongruência de cenário.
