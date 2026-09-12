# PRODUCTION AVATAR QUEUE

**Vídeo modelo:** `C:\Users\luigi\Downloads\manifestselizabeth.mp4`
**Produção:** `producao/manifestselizabeth/` · Ângulo 3 (Auraly) · aberta em 2026-09-11

Os dois avatares foram identificados pelas imagens enviadas junto do `.mp4`, na ordem em que vieram.
A fila é estado obrigatório e não depende do histórico da conversa.

| Ordem | Avatar | Âncora | Status |
|---:|---|---|---|
| 1 | **Robin Matthews** (72) | `producao/_ancoras/Robin.Matthewsus .jpeg` | DONE, 2026-09-11 |
| 2 | **Kris Walker** (24) | `producao/_ancoras/Kris.Walker_us .jpeg` | ACTIVE, desde 2026-09-11 |

## Como a fila anda

1. Entregar o pacote completo do avatar `ACTIVE`.
2. Marcar ele como `DONE`.
3. Promover o próximo `PENDING` a `ACTIVE` automaticamente e entregar o pacote dele.
4. Só declarar `PRODUCTION COMPLETE` quando não houver nenhum `PENDING` nem `ACTIVE`.

## Elementos bloqueados para toda a produção

Aprovados uma única vez, valem para os dois avatares:

- Roteiro de 7 takes, 153 palavras (`ROTEIRO.md`)
- Os ganchos visuais escolhidos pelo Luigi
- Ordem e associação de `K__` e `V__`
- Lógica de movimento e enquadramento (plano único, mesa no terço inferior, Setup A/B/C)
- Overlays do CapCut (`222 ✨`, caixa branca do hook, karaokê, seta vermelha)

## O que varia por avatar

- Identidade, idade, cabelo, pele, roupa, joia
- Cenário canônico e arranjo do kit de tarólogo da âncora dela
- Registro de voz no prompt de vídeo
- **Ajuste de congruência da copy** nos takes T1, T2 e T3, conforme as notas do `ROTEIRO.md`.
  T4 a T7 são idênticos, porque mecânica de funil não tem idade nem registro.

## Separação obrigatória em quadro (as duas não podem parecer a mesma conta)

| | Robin Matthews | Kris Walker |
|---|---|---|
| Idade | 72 | 24 |
| Marca do rosto | manchas de idade, óculos de aro dourado baixos no nariz | sinais escuros na testa, bochecha e acima do lábio |
| Cabelo | bob branco-prateado, risca de lado | box braids na altura do peito, castanho escuro com mechas mel |
| Roupa | cardigã cinza sobre blusa branca | camiseta canelada marrom |
| Joia | cruz de prata **mais aliança de ouro lisa** | cruz de prata e argolas pequenas de prata |
| Cenário | **cozinha** de armários de carvalho, duas janelas | quarto de dia, cama de colcha floral, jiboia |
| Cartas da mesa | **cavalete de madeira**, baralho clássico de borda branca | **três em fila**, baralho clássico de borda branca |
| Bandeira US | pequena em suporte preto no peitoril da janela esquerda | **grande esticada** na parede à esquerda |

Cozinha e óculos são só da Robin. Box braids são só da Kris no roster do Ângulo 3.
**A REF-CARTA que as duas seguram é holográfica**, diferente do baralho clássico da mesa das duas.
Nunca escrever que a carta saiu daquele baralho.

## A regra do arquivo, que existe por causa do linter

O `checar_entrega.py` compara a fala de todo `PROMPTS_VIDEO_FLOW.md` da produção contra o `ROTEIRO.md`,
e o `ROTEIRO.md` é um só. Como a copy muda por congruência entre avatares, os dois não cabem vivos ao
mesmo tempo.

- **O `ROTEIRO.md` carrega sempre a fala do avatar `ACTIVE`.** Hoje o T2 está na versão da Kris.
- **O `PROMPTS_IMAGEM.md` da raiz é sempre o do `ACTIVE`.** O anterior vira `PROMPTS_IMAGEM_<NOME>.md`.
- **Ao fechar um avatar, o `PROMPTS_VIDEO_FLOW.md` dele é renomeado para
  `PROMPTS_VIDEO_FLOW_<NOME>.md`** dentro da pasta dele. Nada se apaga, o arquivo continua no disco e
  o linter para de cobrar aquele pacote contra um roteiro que já virou de outra pessoa.

Estado atual:

| Avatar | Pasta | Arquivos |
|---|---|---|
| Robin Matthews, `DONE` | `robin_matthews_2026-09-11/` | `PROMPTS_IMAGEM.md`, `PROMPTS_VIDEO_FLOW_ROBIN_MATTHEWS.md`, os dois blocos do Flow |
| Kris Walker, `ACTIVE` | `kris_walker_2026-09-11/` | `PROMPTS_IMAGEM.md`, `PROMPTS_VIDEO_FLOW.md`, os dois blocos do Flow |

**A diferença de copy entre as duas é uma linha só, o fecho do T2:** `honey` na Robin,
`I am telling you` na Kris. Todo o resto é idêntico.
