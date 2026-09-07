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
P7 antes do CTA de STORIES  ·  P8 se travar restricao  ·  P9 ao fechar  ·  P10 depois do video no ar

Antes de entregar qualquer coisa de producao, conferir o gabarito, nao a lembranca dele.

1. LER `producao/brandon_angle2/ROTEIRO.md` e `PROMPTS_PRODUCAO.md`. E o gabarito vivo.
   (Copiar dali o FORMATO, nunca o conteudo. Duas praticas de la foram revogadas:
    frase filler e um keyframe por take.)
2. ESCREVER OS ARQUIVOS em `producao/<slug>/` E colar tudo na conversa.
   ANGULO 3 (Auraly): segue o `PLAYBOOK_MESTRE_AURALY.md`, documento operacional. Pasta
   `producao/<slug>/` sem prefixo de avatar, `ROTEIRO.md` comeca com `pipeline: auraly`,
   arquivos ROTEIRO.md + GANCHOS_VISUAIS.md + PROMPTS_IMAGEM.md. SEM DM.md.
   ANTES dos prompts, mandar SUGESTOES DE GANCHO VISUAL (copy identica, so o hook muda) e esperar
   a escolha. Geracao de imagem: identificar o Modo (A automacao total / B abre Chrome mas nao
   interage / C sem navegador). No Modo B ou C, entregar o `pacote_browser/<avatar>/` do playbook
   secao 13.0, nunca alegar que anexou/gerou/baixou algo sem observar.
   Duracao, takes e gramatica visual saem do VIDEO MODELO. So troca o que e do produto.
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

AUTOCOBRANCA DO GRAFO (desde 2026-08-29, quando o graphify entrou no fluxo):
O grafo devolve rotulo e uma linha de trecho, NUNCA a copy. Ele orienta e cruza; o portao manda LER.
Antes de citar qualquer regra de portao, responder a si mesmo: eu abri esse arquivo NESTA sessao,
ou estou repetindo o que o grafo resumiu? Se foi o grafo, ainda nao li, e a resposta nao sai.
Vale sobretudo para o gabarito, a doutrina do angulo e a ficha do avatar.
Precedencia: PORTAO > grafo > lembranca.
Esta linha existe porque o nudge do graphify se repete a cada busca e ganharia por volume.

ZERO TRAVESSAO tambem na RESPOSTA no chat, nao so na copy entregue.
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
