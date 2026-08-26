---
name: checklist-composicao-visual
description: "GATE DE COMPOSIÇÃO VISUAL, checklist de 10 itens que roda ANTES de escrever qualquer prompt de imagem. Consolida os insights de composição que estavam espalhados em metodo-puzzle (hook bom x ruim), feedback-enquadramento-mais-proximo e stack-ferramentas: herói no lower foreground mais perto que o rosto, sempre mais perto do que parece certo, 2ª pessoa cortada pelo quadro, fundo reconhecível e nunca inventariado, nada competindo com o herói, e a nuance de que reduzir fundo se faz com enquadramento e NUNCA com blur."
metadata:
  node_type: memory
  type: feedback
  originSessionId: 32e5549f-536c-4d15-8e9c-ed26d399e783
  modified: 2026-08-22T03:57:56.078Z
---

# Gate de composição visual (roda ANTES de escrever os prompts)

Criado em 2026-08-21 a pedido do Luigi: *"quero que nos gates de qualidade entre também tudo aquilo que analisamos... sempre deixar o foco principal das cenas maiores na tela, sempre deixar o avatar e o herói bem próximo da tela, não deixar muita informação no cenário para não dispersar a atenção... deve ser um checklist que você aplica ANTES de me enviar os prompts, por motivos óbvios."*

**Ele está certo sobre o momento.** Composição não se conserta depois da geração, se conserta no prompt. Esses itens já existiam espalhados em [[metodo-puzzle]], [[feedback-enquadramento-mais-proximo]] e [[stack-ferramentas]], mas nunca eram rodados como gate, então eu escrevia prompts que falhavam neles e só descobria olhando a imagem pronta.

## OS 10 ITENS

**Herói**
1. O herói do take está no **lower foreground**, mais perto da lente que o rosto do avatar?
2. **Nada compete com ele.** Se um elemento não serve à fala daquele take, sai de quadro.
3. Volume e cobertura do herói estão explicitados? (montanha, não camada fina)

**Distância**
4. **"Dá pra estar mais perto?"** Se dá, está longe demais. Perguntar em TODO prompt, não só no hook.
5. Pessoas: **peito pra cima ou ombros pra cima**. O rosto ocupa boa parte do quadro.
6. O take mais fechado do vídeo inteiro é o do **CTA**.

**Fundo**
7. O cenário precisa ser **RECONHECÍVEL, nunca inventariado.** Cortar a lista de objetos de fundo. Duas ou três âncoras visuais bastam.
8. **Reduzir fundo se faz com ENQUADRAMENTO, nunca com blur.** O negative da operação proíbe blur em tudo, então a única forma de tirar informação de fundo é fechar o plano e descrever menos.
9. Menos elementos em cena = **mais qualidade de geração e mais realismo**. O gerador segura melhor o detalhe quando tem menos o que resolver.

**2ª pessoa**
10. Ela entra **CORTADA pelo quadro**, nunca de corpo inteiro. Presença parcial já dá o contexto e deixa o herói dominar.

## Onde isso mais falha na prática
- **Inventário de fundo.** O erro mais comum meu: escrever "caixotes de tomate, pimentão e folhas, janelas altas, luzes de teto, prateleiras" quando bastava "caixotes de produtos frescos e janelas claras". Cada substantivo a mais é atenção dispersada e um detalhe a mais pro gerador errar.
- **Two-shot largo demais no hook.** Quando tem 2ª pessoa, a tentação é abrir o plano pra caber os dois. Errado: corta a 2ª pessoa e mantém o herói colado na lente.

## Fidelidade não se aplica aqui
O enquadramento **não faz parte do esqueleto**. O método puzzle preserva elemento, ação e reveal. Copiar a distância de câmera do original é jogar fora a maior alavanca gratuita de atenção que existe. Ver [[feedback-enquadramento-mais-proximo]].

Relacionado: [[metodo-puzzle]], [[feedback-enquadramento-mais-proximo]], [[prompts-imagem-json]], [[stack-ferramentas]], [[workflow-entrega-gabarito]]
