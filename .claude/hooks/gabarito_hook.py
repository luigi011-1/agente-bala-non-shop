#!/usr/bin/env python3
"""
Hook UserPromptSubmit da operacao de videos.

Le o JSON do hook no stdin. Se a mensagem do Luigi mencionar producao de video,
injeta o gabarito de entrega no contexto do modelo, para que ele nunca dependa
de lembrar de abrir a memoria.

Criado em 2026-08-21 depois que o formato de entrega se degradou por eu ter
parado de reler as memorias de processo.
"""
import json
import sys

GATILHOS = (
    "mp4", "watch", "prompt", "roteiro", "producao", "produção",
    "keyframe", "take", "avatar", "imagem", "video", "vídeo",
    "copy", "hook", "cta", "angulo", "ângulo",
)

GABARITO = """[LEMBRETE AUTOMATICO DE PROCESSO - operacao de videos]

PORTOES DE CONSULTA (secao propria no CLAUDE.md). Ler ANTES de agir, nunca depois:
P1 antes do /watch  ·  P2 antes de tocar na copy  ·  P3 antes de entregar o roteiro
P4 antes dos ganchos (angulo 3)  ·  P5 antes do primeiro JSON  ·  P6 antes dos prompts de video
P7 antes do DM.md  ·  P8 se travar restricao  ·  P9 ao fechar  ·  P10 depois do video no ar

Antes de entregar qualquer coisa de producao, conferir o gabarito, nao a lembranca dele.

1. LER `producao/brandon_angle2/ROTEIRO.md` e `PROMPTS_PRODUCAO.md`. E o gabarito vivo.
   (Copiar dali o FORMATO, nunca o conteudo. Duas praticas de la foram revogadas:
    frase filler e um keyframe por take.)
2. ESCREVER OS DOIS ARQUIVOS em `producao/<avatar>_<slug>/` E colar tudo na conversa.
   ANGULO 3: ANTES dos prompts, mandar SUGESTOES DE GANCHO VISUAL do mesmo modelo (copy identica,
   so o hook muda) e esperar o Luigi escolher.
   ANGULO 3 (Auraly) = TRES arquivos (mais DM.md). O PROCESSO E O MESMO dos angulos 1 e 2:
   duracao, takes e gramatica visual saem do VIDEO MODELO. So troca o que e do produto.
   Arquivo nao substitui chat, chat nao substitui arquivo.

ROTEIRO.md, nesta ordem: cabecalho / tabela de esqueleto preservado (Original x Adaptado) /
setups de cena / roteiro cena a cena (### T1 - BEAT - TALKING|B-ROLL - Setup A) /
roteiro so-fala / notas de producao.

PROMPTS_PRODUCAO.md, nesta ordem: cabecalho / indice de geracao (Take|Keyframe|Acao) /
trava de identidade e continuidade / trava do prop heroi / trava da 2a pessoa (REF-A) /
prompts de imagem K01.. (JSON) / bloco global de video / prompts de video V01 - T1 - usa K01
(texto simples, 5 blocos) / mapa de ancoras / montagem no CapCut / gates de qualidade.

NOMENCLATURA: T = take do roteiro, K = keyframe (imagem), V = clipe, REF = referencia auxiliar.
Nunca colapsar num namespace so.

IMAGEM = JSON. VIDEO = texto simples com os 5 blocos (fala com sotaque / trava de lip sync e
ultima palavra / o que acontece / camera / som ambiente sem musica). NUNCA misturar os dois.
Prompt de video nao descreve enquadramento, cor nem composicao.

CONTAR PALAVRAS ANTES: 8s por take = 13 a 29 palavras (teto subiu em 2026-08-26). Take longo se quebra em fim de frase.
Nunca inventar filler, nunca parafrasear.

GERAR DO ZERO so no primeiro keyframe de cada setup. Todo o resto e EDITAR do K__.

NEGATIVE: nunca listar termo sensivel (nome de orgao, gore, logo, brand name). O classificador
le o token, nao a negacao. E nunca sugerir "tenta de novo": o Luigi ja tentou varias vezes.

FECHAMENTO: conferir o log de rotacao em banco-rotas-argumentativas e NAO repetir a rota nem as
frases do video anterior. Beat de virada olha pra frente (escalada), nunca resume.

Keyword por angulo: `yes` nos angulos 1, 2 e 4, `222` no angulo 3 (Auraly). Zero travessao.
Angulos 2 e 3 NAO mostram produto (no 3 o CTA promete o ROSTO da alma gemea, nunca o app).
Roteiro final por ultimo.
"""


def main() -> int:
    try:
        payload = json.load(sys.stdin)
    except Exception:
        return 0

    prompt = str(payload.get("prompt", "")).lower()
    if not any(g in prompt for g in GATILHOS):
        return 0

    json.dump(
        {
            "hookSpecificOutput": {
                "hookEventName": "UserPromptSubmit",
                "additionalContext": GABARITO,
            },
            "suppressOutput": True,
        },
        sys.stdout,
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
