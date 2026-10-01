#!/usr/bin/env python3
"""Roteamento UserPromptSubmit. Nao duplica workflow nem configuracoes."""
import json
import sys

GATILHOS = ("mp4", "watch", "prompt", "roteiro", "producao", "produção", "avatar", "video", "vídeo", "copy", "hook", "angulo", "ângulo", "continue", "status",
            "gancho", "imagem", "keyframe", "cenario", "cenário", "pacote", "produzir", "flow", "take")
GABARITO = """[ROTEAMENTO DA OPERACAO]
Leia AGENTS.md e identifique o pedido atual. Analise/manutencao nao inicia producao.
Auraly: WORKFLOW_AURALY.md -> CHECKPOINT.md -> somente Next action. Respeite WAITING_*.
Oferta e objetivo sao distintos: SALE ou GROWTH conforme decisao registrada. Nao inferir growth
pela referencia, nao misturar ofertas e nao exigir Stories de growth explicitamente aprovado.
O checkpoint governa estado e fila; AVATAR_QUEUE e vista derivada. AVATAR DONE != PRODUCTION DONE.
Para Angle 1/2: CLAUDE.md e PLAYBOOK_FITYWELL.md quando aplicavel. Angle 4 e historico.
O playbook mestre Auraly e referencia criativa, nunca roteador operacional.
Nao reconstruir configuracao de memoria: ler o contrato indicado pelo workflow da oferta.
Imagem e ganchos, em qualquer angulo: rodar GATE_VISUAL.md antes (luz neutra/ceu com cor, sem tom
quente, heroi colado na lente, 2-3 ancoras de fundo, sem blur, trecho de realismo em todo K).
BLOQUEANTE, qualquer angulo: nenhum K sem FICHA_FRAMES.md escrita olhando o frame do modelo
(forma do heroi, % do quadro, distancia da lente, camera, pose, lista fechada) e o placar
F1-F6 + G1-G8 com o trecho literal do K como evidencia (GATE_VISUAL.md Parte 6). Modelo manda
no conteudo, gate no acabamento. Nunca genericizar a forma do heroi por medo de censura.
Ganchos, em qualquer angulo: a camada verbal (fala do T1, texto de tela) segue a skill
gancho-verbal (tese, sintoma-alvo, banco verbal de 5 frases literais, tela <= 9 palavras).
BLOQUEANTE, qualquer angulo: antes de ENVIAR gancho, K, V, pacote ou prompt avulso, rodar o
CHECKLIST DE ENVIO da memoria checklist-envio-prompt (blocos A gancho, B imagem, C video, D
montagem, E marca). Item reprovado = corrigir e rodar de novo; nunca enviar com ressalva. A
entrega leva, fora dos blocos copiaveis: "Checklist de envio: X/X aprovados (N/A: ...)".
Validar antes da entrega com checar_entrega.py. Nao pedir ao usuario que fiscalize o processo.
Nao gerar imagens nem executar navegador/Flow. Nao reabrir decisoes aprovadas.
"""

def main():
    try:
        payload = json.load(sys.stdin)
    except (ValueError, TypeError):
        return 0
    if not isinstance(payload, dict):
        return 0
    if any(g in str(payload.get("prompt", "")).lower() for g in GATILHOS):
        json.dump({"hookSpecificOutput": {"hookEventName": "UserPromptSubmit", "additionalContext": GABARITO}, "suppressOutput": True}, sys.stdout)
    return 0

if __name__ == "__main__":
    sys.exit(main())
