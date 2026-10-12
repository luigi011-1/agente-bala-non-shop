# Referências de edição V01 e V02 — 2026-10-11

Escopo autorizado: aprender edição para FitWell e Sea Moss da holistic.brandon;
Auraly exige adaptação própria. Não são os modelos da próxima produção comercial.
Fontes locais e hashes estão em `evidencias-edicao-2026-10-11/v01` e `v02`.

Método: `/watch`, 5 fps em todo o vídeo, grades de cenas e timeline abertas,
frames críticos em resolução 720×1280, Faster-Whisper small.en com palavras.
Registro pessoal em `visual_review.json`, separado do manifest mecânico que
corretamente continua `PENDING_VISUAL_REVIEW`. Amostragem não significa playback
de todos os frames. Transcrição é ASR não revisado por escuta; contagem aproximada.

| Referência | Arquivo | Duração | Palavras ASR regex | Palavras/s no vídeo inteiro | Primeira palavra ASR | LUFS do mix |
|---|---|---:|---:|---:|---:|---:|
| V01 | snapinsta-1791763841045.mp4 | 43,47 s | 132 | 3,04 | 2,26 s | -14,39 |
| V02 | snapinsta-1791764012212.mp4 | 55,22 s | 185 | 3,35 | 2,58 s | -14,34 |

Palavras/s globais incluem ações sem fala. Não revelam fator de aceleração do
editor original nem justificam acelerar todos os nossos takes até um alvo fixo.

## V01 — proximidade, ação e hierarquia de legenda

| Tempo aproximado | Evidência visual examinada | Função editorial | Aplicação |
|---|---|---|---|
| 0–2,2 s | Grades 01; caneca no primeiro plano, personagem inclinado, canudo na boca, sem legenda | Ação abre a curiosidade antes da fala | Proteger o gancho visual quando existir; não exigir fala no frame zero |
| 2,6–5,2 s | Grades 01–02; rosto próximo, braço em diagonal, palavras alternam tamanhos | Conversa direta e hierarquia semântica | Distância e direção do olhar entram no K; não é necessário zoom artificial contínuo |
| 5,4–12,0 s | Grades 02–03, frame 11,8; panela e ingrediente sobem para o primeiro plano | A fala acompanha a demonstração | Planejar quadro com rosto, mãos e produto; preservar início/meio/fim da ação |
| 12,2–16,6 s | Grade 04; mãos trocam para canela; corte seco | Nova etapa física justifica a troca | Cortar em mudanças de ação e ideia, sem calendário de efeito a cada segundo |
| 16,8–20,8 s | Grades 05–06, frame 17,4; colher com erva, texto à esquerda | Termo central cresce; palavras de ligação ficam pequenas | Destaque semântico escolhido, não todas as palavras com igual intensidade |
| 21–25,6 s | Grades 06–07; gesto explica, objeto permanece visível | Continuidade durante a explicação | Não trocar plano apenas por uma pausa respiratória mínima |
| 25,8–30,4 s | Grades 07–08; retorna à caneca e rosto inclinado | Retoma objeto e relação com câmera | Fechar o arco visual do objeto sem inventar cenário |
| 30,6–37,8 s | Grades 08–10; gestos, mesma caneca, microcortes | Divide recomendações em frases | Preservar finais de sílaba e frases; ASR esticado não é detector de silêncio |
| 38–43,3 s | Grades 10–11, frame 38,2; plano mais aberto com tronco e mãos livres | CTA ganha gesto e respiro espacial | Abrir o enquadramento quando necessário para gesto e legibilidade; manter CTA da oferta |

Legenda creme/branca na região esquerda intermediária. Mistura sans grande e
pesada, serifada forte e palavras menores em itálico/sans. Acumula complemento
em volta do termo importante. Entradas com blur em alguns frames (4,6; 17,4 s);
não são motivo para pôr transição em todo corte. O tamanho reage à palavra/ideia,
não a uma tipografia uniforme no centro. O texto em 38,2 s ocupa quase toda a
largura e encosta na região inferior do rosto: aprendizado de hierarquia, mas
nossa conferência continua exigindo rosto e produto livres.

## V02 — contraste útil com V01

| Tempo aproximado | Evidência examinada | Função editorial | Aplicação |
|---|---|---|---|
| 0–2,4 s | Grade 01; close facial tomando bebida | Curiosidade com ação | Proteção visual explícita, não silêncio descartável por definição |
| 2,8–5,4 s | Grades 01–02, frame 3,4; rosto muito perto, cursiva grande | Gancho verbal muda o estado | Escolher área de legenda que não atravesse a boca, mesmo que original atravesse |
| 5,6–17,2 s | Grades 02–05; plano mais aberto mostra panela, mão, colher/ingredientes | Informação e ação no mesmo quadro | Enquadramento de demonstração, câmera na altura do objeto e rosto acima |
| 17,4–29,4 s | Grades 05–08, frames 17,6 e 29,4; colher e vapor visíveis | Continuidade física enquanto explica | Proteger o objeto e as mãos contra crop e legenda |
| 29,6–48,8 s | Grades 08–13; corte volta ao rosto próximo segurando copo | Encerramento da demonstração | Mudança de escala no payoff, sem inserir zoom arbitrário por palavra |
| 49–55 s | Grades 13–14, frame 49,4; mantém caneca e contato visual | CTA dentro da mesma conversa | Não obrigar plano aberto em todo CTA; seguir o modelo e o objeto |

Cursiva branca grande, com termos curtos em sans amarela ao lado; normalmente
poucas palavras visíveis e frequentes substituições. Não se deve copiar a
posição sobre boca/panela. Para nosso editor, priorizar estilos legíveis do
catálogo HyperFrames já disponíveis e verificar o resultado em frame; fonte
exata não foi identificada. Pequenas pausas ASR entre frases não comprovam cortes
do original. O detector a 0,2 perdeu mudanças evidentes em 5,6 e 29,6 s; lista
automática de cenas é candidata, não inventário certificado de cortes.

## Música e voz — o que está e não está confirmado

`metricas.json` contém energia RMS do áudio misturado a cada segundo, LUFS e
intervalos sem palavra ASR. Há sinal de áudio antes da primeira fala. Isso não
isola música de som de objeto/ambiente. Não houve escuta perceptiva: identidade,
instrumentos, BPM, crescendos, efeito emocional e sincronização de batidas da
trilha original ficam NÃO CONFIRMADOS. Não afirmar que uma queda de RMS é um
duck de música: pode ser apenas a pausa da voz.

Proposta implementável, separada da observação: planejar cama por beats do
roteiro (curiosidade → demonstração → payoff → CTA), escolher trecho de entrada
da faixa da biblioteca, criar curvas suaves de volume e baixar nos trechos que
pedem entendimento. Manter ganho máximo da cama em -18 dB após normalizar a
fonte para a mesma referência da voz, conforme regra vigente; reduzir até -30
dB quando escolhido. Isso é configuração de mix, não SNR medida no original.
Teste de FFmpeg comprova execução, duração e continuidade; emoção exige escuta.

## Enquadramento para futuros prompts K

- Especificar altura/distância da câmera, posição do rosto e distância do
  produto à lente; não usar só “close-up”.
- No gancho, dar ao produto uma ação visível e uma silhueta reconhecível.
- Durante demonstração, mostrar mãos completas, rosto e produto sem cortar
  rótulo; reservar uma região de legenda longe desses três elementos.
- O enquadramento do CTA acompanha o modelo e o gesto necessário. V01 abre,
  V02 continua próximo: não há regra universal de plano aberto.
- Repetir descrição do objeto para continuidade. O roteiro/K planeja a ação;
  o V entregue mantém o padrão curto atual. Sem prompt avulso nesta análise.
- Só engenharia editorial atravessa ofertas. Alegações da receita, ingredientes
  e promessa da referência não entram na copy Sea Moss/FitWell por empréstimo.

Os achados estão consolidados em `pos-producao-aprendizado-2026-10-11.md`.
