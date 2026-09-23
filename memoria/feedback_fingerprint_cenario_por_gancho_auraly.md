---
name: feedback-fingerprint-cenario-por-gancho-auraly
description: "Ângulo 3 (Auraly): cenário/roupa/ângulo de câmera PRÓPRIO por gancho escolhido, nunca um corpo compartilhado pela fila (vigente desde 2026-09-14). A parte da FINGERPRINT foi revogada em 2026-09-22: o roster ativo (Walt, Darlene, Lorraine) usa a imagem em cena real como âncora, com a instrução de usar só a identidade quando o gancho pede cenário novo."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 37f5dc01-94f1-4f0f-ac54-6fbe3c922eec
  modified: 2026-09-15T02:20:26.124Z
---

# Cenário por gancho é o padrão do Ângulo 3 (a fingerprint caiu em 2026-09-22)

> ♻️ **2026-09-22 (Luigi):** *"não gostei do resultado dos fingerprints, pra produzir os vídeos eu irei
> usar as imagens que te enviei anteriormente"*. Para o roster ativo (Walt, Darlene, Lorraine) a âncora
> é a **imagem em cena real** (`producao/_ancoras/*_ancora.jpg`). Quando o gancho pedir cenário ou roupa
> novos, o `K__` diz `use the attached image only for his/her identity (face, eyes, hair, skin, body,
> signature); ignore its clothing, background and props` e descreve o cenário novo inteiro. **O cenário
> próprio por gancho, abaixo, continua valendo.** Tudo o que fala de fingerprint abaixo é histórico.

Testado em 2026-09-14 com um avatar hoje descartado: 5 cenários totalmente
diferentes (cozinha câmera de cima, varanda câmera deitada olhando pra cima, escritório três-quartos
com leve inclinação holandesa, ateliê câmera baixa lateral tipo worm's-eye, sala de meditação câmera
alta no canto em diagonal), um por gancho escolhido. Luigi aprovou: "deu tudo certo da maneira que
fizemos agora, gostei bastante do resultado e fluiu bem, vamos produzir dessa maneira sempre".

**Why:** contas que estão viralizando de verdade variam MUITO o cenário por vídeo, mantendo só a
psicologia visual fixa (cartas, bandeira, cristal, incenso). O modelo antigo (1 âncora de ambiente
real + corpo compartilhado por 5 hooks) deixava a conta repetitiva demais.

**How to apply, sempre no Ângulo 3 daqui pra frente:**

1. **A referência de identidade é uma FINGERPRINT**, não mais foto de ambiente real: grade de
   estúdio, fundo neutro, rosto em vários ângulos (frente, 3/4, perfil, cima, baixo), corpo de
   frente/lado/costas, macro de pele. Ela trava SÓ rosto, pele, corpo e cabelo. Roupa e cenário
   nunca vêm dela, vêm do texto de cada `K__`.
2. **Cada gancho aprovado ganha cenário PRÓPRIO do T1 ao CTA**: seu próprio `K` de hook, seu
   próprio `K` de corpo (serve T2 a T5), seu próprio `K` de CTA. Não existe mais "corpo comum K06
   compartilhado pelos 5 hooks".
3. **Roupa livre por cenário**, sem obrigação de repetir a roupa da fingerprint.
4. **Ângulo de câmera sempre exótico e diferente entre os cenários da mesma fila.** Nunca o padrão
   de rosto na altura da câmera falando reto em todos. Ver [[feedback-angulos-camera-avatar]], que
   já apontava isso pra variações de avatar isoladas; agora vale pra dentro da MESMA fila de ganchos
   de UM avatar.
5. **Kit de tarólogo continua obrigatório em todo `K`** (cartas, cristal, incenso, vela, cruz,
   bandeira dos EUA), só o arranjo muda por cenário.
6. **Copy e ganchos continuam aprovados uma vez só pra fila inteira.** Isso não muda: só a pele
   visual varia por cenário, nunca a fala.
7. **Custo sobe de propósito**, de ~7 K / 10 V por avatar pra ~15 K e o mesmo total de V (6 V por
   cenário: 1 mudo + 4 falados + 1 CTA). Confirmado que vale.

**Entrada do `/watch` a partir de 2026-09-14 (Luigi):** ele já gerou o blueprint de todos os
avatares. Quando mandar o `.mp4` de agora em diante, os `.jpeg`/`.png` anexados na mesma mensagem
JÁ SÃO fingerprints, nunca mais fotos de ambiente real tipo as âncoras antigas. Não perguntar, não
tratar como "foto do quarto dele": elas travam só rosto, corpo e pele, e cenário/roupa nascem do
zero por gancho.

**Fonte de verdade do processo (dentro do repo):** `WORKFLOW_AURALY.md`, seção "Fingerprint e
cenário por gancho". **Instruções do agente Flow correspondentes: v7**, em
`producao/_flow/INSTRUCOES_AGENTE_FLOW.md`. Pacote de exemplo arquivado em
`_arquivo/2026-09-22_limpeza_angulo3/producao/oliviamadison671/`.

Ver também [[angulo3-copy-auraly]], [[feedback-angulos-camera-avatar]].
