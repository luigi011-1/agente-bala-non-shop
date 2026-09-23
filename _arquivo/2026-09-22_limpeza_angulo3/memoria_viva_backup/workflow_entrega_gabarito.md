---
name: workflow-entrega-gabarito
description: "REGRA MESTRA de processo: toda produção começa lendo producao/brandon_angle2/ (o gabarito vivo) e entrega DOIS arquivos em producao/<avatar>_<slug>/ mais tudo colado na conversa. Define a nomenclatura T/K/V/REF, a ordem das seções dos dois arquivos, e o diagnóstico das 8 coisas que eu perdi em 2026-08-21 ao parar de seguir o gabarito. O processo agora vive no CLAUDE.md da raiz do projeto, que carrega sozinho toda sessão."
metadata:
  node_type: memory
  type: feedback
  originSessionId: 32e5549f-536c-4d15-8e9c-ed26d399e783
  modified: 2026-08-21T23:12:23.089Z
---

# Workflow de entrega: o gabarito é lei

Criado em 2026-08-21 depois que o Luigi cobrou: *"releia TODA A SUA MEMÓRIA, releia TODOS OS DOCUMENTOS e arrume esse maldito workflow, você está mandando tudo errado e misturado, se perdendo nas informações que acumulamos com o tempo."*

Ele estava certo. Eu tinha abandonado o formato de entrega inteiro.

## O PROCESSO AGORA VIVE NO `CLAUDE.md` DA RAIZ DO PROJETO
`c:\Users\luigi\Desktop\AGENTE NON-SHOP\CLAUDE.md` carrega automaticamente em toda sessão. **Processo vai lá, copy e estratégia ficam na memória.** Antes o processo estava espalhado em seis memórias diferentes e eu recompunha a entrega de cabeça a cada vez, que é exatamente como ela se degradou.

## O GABARITO VIVO
`producao/brandon_angle2/ROTEIRO.md` e `PROMPTS_PRODUCAO.md` (18/08). **Reler os dois antes de começar qualquer produção nova.** Não reinventar o formato de memória.

## As 8 coisas que eu perdi (diagnóstico registrado pra não repetir)

1. **Parei de escrever os arquivos.** Zero arquivos em `producao/` durante a sessão inteira. Li metade de [[feedback-prompts-na-conversa]] ("colar na conversa") e ignorei a outra metade ("o arquivo continua valendo como registro"). São os DOIS.
2. **Perdi a nomenclatura T / K / V / REF.** Inventei "IMAGEM A" e numerei tudo como T, colapsando roteiro, imagem e clipe num namespace só. Some a rastreabilidade.
3. **Perdi o `EDITAR do K__`.** Gerei 8 imagens do zero. O sistema certo gera do zero só o primeiro keyframe de cada setup e edita o resto, o que trava rosto, fundo e luz.
4. **Perdi as TRAVAS globais** (identidade e continuidade, prop herói, 2ª pessoa). Sem elas eu repito a descrição inteira do avatar dentro de cada JSON, o que incha o prompt e dá superfície pro classificador. Provavelmente contribuiu pro bloqueio de 8 prompts de uma vez.
5. **Perdi o Bloco Global de vídeo** e escrevi prompt de vídeo em prosa inglesa começando com "Start from the attached image", re-descrevendo enquadramento e cor. Isso é linguagem de prompt de IMAGEM. Ver [[prompts-video-fase7]].
6. **Perdi três seções inteiras:** Mapa de âncoras, Montagem no CapCut e Gates de qualidade.
7. **Perdi a tabela de esqueleto preservado.** É a prova de que o puzzle foi respeitado, e é justamente onde eu teria enxergado que estava repetindo a copy de um vídeo pro outro.
8. **Não contei as palavras antes.** Escrevi o roteiro sem aplicar os 8s / 13 a 29 palavras, descobri depois de entregar os prompts, e tive que requebrar 15 takes em 21 com os prompts já na mão.

## A CAUSA RAIZ
A memória cresceu muito em COPY (rotas, obstáculos, ponte, ângulo 2) e eu passei a operar por ela, parando de reler as de PROCESSO. Memória nova não substitui memória velha, ela soma.

**Regra que sai daí: antes de entregar, conferir o gabarito, não a lembrança do gabarito.**

Relacionado: [[ordem-entrega-padrao]], [[feedback-prompts-na-conversa]], [[feedback-roteiro-final]], [[processo-7-fases]], [[prompts-video-fase7]], [[prompts-imagem-json]], [[regras-universais]]
