# AVATAR QUEUE

**Vídeo modelo:** `C:\Users\luigi\Downloads\8bd57dab-62d3-452a-8809-4b5eb72834d5.mp4` (27,97 s, 6 takes)
**Ângulo:** ANGLE 2, app FityWell (mulheres 40+, funil de quiz, keyword `yes`)
**Estado:** PRODUCTION COMPLETE

| Ordem | Avatar | Âncora | Status |
|---:|---|---|---|
| 1 | Dana Morrison | `producao/_ancoras/dana_morrison_ancora.jpeg` | DONE |
| 2 | Jamie Anderson | `producao/_ancoras/jamie_anderson_ancora.jpeg` | DONE |
| 3 | Lynn Parker | `producao/_ancoras/lynn_parker_ancora.jpeg` | DONE |

## Travas da produção

- **Ângulo 2 foi definido explicitamente pelo Luigi em 2026-09-10. Não perguntar de novo.**
- Os três avatares são **COACH**, nunca usuários. Produto feminino com avatar masculino, regra da
  `congruencia-matriz`. Nunca 1ª pessoa sobre corpo feminino, nunca "at our age".
- **O crivo de nunca culpar ela roda DUAS vezes**, porque quem fala é homem. Regra em
  `avatares-fichas`, seção ROSTER FITYWELL.
- **Não mostra produto.** Sem celular, sem print de tela, sem mockup. O nome FityWell é DITO em voz alta.
- Roteiro, takes, falas, ganchos escolhidos e ordem de K e V são aprovados **uma vez** e valem para
  os três. Muda só identidade, âncora, cenário, registro e a frase de enquadramento do coach.
- `AVATAR DONE != PRODUCTION DONE`. A produção só fecha com os três em `DONE`.

## Nota de arquivo (2026-09-10)

O `PROMPTS_PRODUCAO.md` da pasta é sempre o do avatar **ACTIVE**, para o `checar_entrega.py` rodar
contra o `ROTEIRO.md`, cujo T4 acompanha o avatar da vez. O pacote fechado do avatar anterior fica
arquivado com o nome dele: `PROMPTS_DANA_MORRISON.md`, `PROMPTS_JAMIE_ANDERSON.md` e os dois `FLOW_`.

**Adaptação de cenário do Jamie:** a âncora dele é o banco do motorista, onde não cabe demo com
modelo apoiado. A bancada dele vira o **porta-malas aberto do SUV, no mesmo estacionamento**, que
preserva carro, lojas de tijolo ao fundo e o adesivo da bandeira. Esse enquadramento não existe na
âncora, então o primeiro keyframe dele deve pedir mais regeneração que o do Dana.

**Lynn Parker:** é o avatar mais próximo do vídeo modelo, porque o original também é um herbalista
idoso numa mesa de apotecário. A mesa de madeira escura em frente ao banquinho é a única coisa que
não aparece na âncora, e ela é a gramática do próprio modelo. O pôster de meridianos sai com texto
errado na geração, então entra sempre como gráfico impresso, sem exigir palavra legível.
