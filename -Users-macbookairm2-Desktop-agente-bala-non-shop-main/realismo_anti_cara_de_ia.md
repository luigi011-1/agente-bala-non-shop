---
name: realismo-anti-cara-de-ia
description: "GATE DE REALISMO obrigatório antes de fechar qualquer prompt de imagem. As regras que separam 'cara de IA' de UGC crível: isolar o herói é a alavanca nº1, cores quentes e céu claro denunciam, fundo específico nunca borrado, partir sempre de algo real, e realismo é volume de regeneração e não prompt mágico. Extraído do PLAYBOOK_COMPLETO 03 seção 2.5 e 06 seção 4.3b, elevado a regra viva a pedido do Luigi em 2026-08-24."
metadata: 
  node_type: memory
  type: feedback
  modified: 2026-09-22T22:44:35.649Z
  originSessionId: 35741d33-8b83-4947-a661-f71261849cf0
---

# Gate de realismo, rodar antes de fechar qualquer prompt de imagem

> ♻️ **2026-09-22:** a versão executável e transversal (Korella, FitWell e Auraly) agora vive em `GATE_VISUAL.md` na raiz do projeto, que o `WORKFLOW_AURALY.md`, o `PLAYBOOK_FITYWELL.md`, o `AGENTS.md` e o `checar_entrega.py` (aviso `realismo`) passaram a citar. Regra nova de realismo ou composição se escreve LÁ; esta memória guarda o porquê e o histórico.

**Why:** "cara de IA" mata a credibilidade do avatar e derruba a retenção. Isso estava só no playbook, que eu não abro sozinho, então eu vinha escrevendo prompts poluídos e com luz quente. O Luigi mandou aplicar em **todas as produções** a partir de 2026-08-24.

**How to apply:** rodar os 7 itens abaixo **junto com o gate de composição visual**, antes do primeiro JSON.

---

## 1. ISOLAR O HERÓI É A ALAVANCA Nº1
**Quanto menos elementos, mais realista a imagem sai.** Cena poluída faz o gerador estragar a qualidade. Isso vale duas vezes: ganha **retenção** (o olho sabe onde focar) e ganha **qualidade técnica**.

- No hook: `"[hero] fills the lower two-thirds, camera pushed in close, everything else out of frame"`
- **Duas ou três âncoras visuais de fundo, no máximo.** Listar seis objetos é o erro clássico.
- Reduzir fundo é com **enquadramento**, nunca com blur.
- Nuance: close-up é regra do **hook e dos takes de reveal**, não do vídeo inteiro. Takes de fala podem abrir um pouco pra mostrar o cenário que dá autoridade.

### ⚠ NUANCE ADICIONADA EM 2026-08-29: o inimigo é o inventário, não a bagunça
O Luigi aprovou uma âncora do Ângulo 3 com o quarto **visivelmente bagunçado** (cama
desarrumada, cômoda, frascos, corredor ao fundo), porque ela lê como *"abriu a câmera e começou a
gravar"*. Eu tinha reprovado essa âncora por poluição de cenário. **Estava errado sobre o motivo.**

O que degrada a geração não é o cenário ser cheio, é o **prompt descrever muito objeto**. Cada
substantivo novo é um detalhe que o gerador precisa inventar e pode errar. Bagunça que vem de uma
**âncora real e é preservada por `EDITAR do K__`** não é inventada, então não paga esse custo, e ainda
compra credibilidade de UGC, que é a regra-mãe do item 4 deste mesmo gate.

**Como fica na prática:**
- Cenário limpo **não é meta**. Cenário limpo demais lê como anúncio.
- **Duas ou três âncoras de fundo continuam sendo o teto do que se DESCREVE no prompt.**
- Cenário vivido se preserva escrevendo *"the same lived-in room as the reference image, unchanged"*,
  nunca listando a bagunça item a item.
- No **hook e nos takes de reveal**, o herói continua dominando o quadro. Isso não mudou.

Ver [[avatares-fichas]].

### ⚠ SEGUNDA EDIÇÃO, 2026-09-03: o Ângulo 3 tem kit de cenário OBRIGATÓRIO
O Luigi mandou que **todo avatar do Ângulo 3 carregue as 7 categorias do kit de tarólogo** em toda
âncora e todo keyframe: cristais, incenso aceso, bandeira dos EUA, cartas, quadro astrológico, cruz e
vela. **Isso ganha do teto de duas ou três âncoras neste ângulo**, porque ali o cenário é a credencial
do avatar e não decoração: é ele que faz a pessoa bater o olho e saber que é um tarólogo.

**O teto não morreu, mudou de unidade.** Continua valendo como teto do que se **descreve solto**, e o
kit entra **agrupado em dois blocos** ("a prateleira ao lado dela com X, Y e Z" mais "na parede atrás
dela o quadro e a cruz"), que é o que mantém a contagem de substantivos administrável. Fora do Ângulo 3
nada mudou. Regra completa em [[angulo3-copy-auraly]], seção do kit de tarólogo.

## 2. COR E LUZ QUE DENUNCIAM
- **Cores quentes (amarelo, laranja, marrom) deixam com cara de IA.** Evitar "warm and even" como padrão.
- **Céu branco ou claro SEMPRE denuncia.** Preferir `overcast sky` ou `cloudy`.
- Externa: céu nublado com textura ou azul profundo. Interna: luz difusa neutra de dia nublado.
- 🚫 **Golden hour BANIDA em 2026-09-22 (Luigi).** O gate antigo mandava golden hour em externa, o que contradizia o próprio item de tom quente. Pôr do sol e contraluz alaranjado também. O linter reprova.
- Negative útil: `no warm orange color cast, no yellow tint, no golden glow, no golden hour light, no sunset`.

## 3. FUNDO NÃO PODE SAIR BORRADO
Não se conserta editando depois. Tem que sair certo na primeira geração: descrição **muito específica** mais, quando possível, **imagem de referência real**.

## 4. PARTIR SEMPRE DE ALGO REAL (a regra-mãe)
> A IA copia bem o que você mostra e inventa mal o que você só descreve.

- Rosto de pessoa secundária: **referência de rosto real**, nunca só texto
- Fundo: screenshot de casa, rua ou bairro americano real
- Prop que teima: **gerar isolado primeiro**, aprovar, usar como referência de objeto

## 5. A ÂNCORA DO AVATAR É O ATIVO QUE MAIS PESA
Nenhum prompt compensa âncora ruim. Regenerar quantas vezes precisar.

## 6. REALISMO É VOLUME, NÃO PROMPT MÁGICO
Regenerar várias vezes até sair a imagem certa **é o método**, não sinal de que o prompt está errado. **Nano Banana 2 costuma superar o ChatGPT em realismo de avatar.**

## 7. BLOCO DE REALISMO PADRÃO (colar em todo prompt)
```
"realism": "UGC realism, real skin texture with visible pores, individual hair strands, subtle wrinkles, realistic shadows and reflections, iPhone-footage look, phone camera look not professional photography, no AI polish, no beauty smoothing, no blur anywhere, everything in sharp focus including background walls furniture and details."
```

---

## Método Frankie (realismo máximo, quando valer o trabalho)
Gerar os elementos **separados** (fundo, céu, rosto, prop), cada um no seu melhor, e **mesclar** num frame só. Trabalhoso, é o que os creators de realismo máximo fazem.

Ver também: [[checklist-envio-prompt]] (bloqueante, roda antes de todo envio), [[checklist-composicao-visual]], [[erros-recorrentes]], [[prompts-imagem-json]], [[regras-universais]].
Fonte: `PLAYBOOK_COMPLETO/03_ferramentas_e_stack.md` seção 2.5 e `06_prompts_imagem.md` seção 4.3b.
