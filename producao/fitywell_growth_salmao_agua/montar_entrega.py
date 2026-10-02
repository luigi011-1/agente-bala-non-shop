"""Monta ENTREGA_<AVATAR>.md: o pacote inteiro de cada avatar num arquivo só, na ordem da entrega.

Ordem: instruções do agente Flow (bloco inteiro, v vigente) -> checklist de envio e ficha -> anexos ->
PROMPTS DE IMAGEM (um bloco por K, em JSON) -> PROMPTS DE VÍDEO (um bloco por V) -> montagem no
CapCut -> transcrição por take -> roteiro final em inglês (numerado + corrido), sempre o último bloco.
Tudo sai de gerar_pacote.py e do disco.
"""
import re
from pathlib import Path

import gerar_pacote as G

AQUI = Path(__file__).resolve().parent
INSTR = (AQUI.parent / "_flow" / "INSTRUCOES_AGENTE_FLOW.md").read_text(encoding="utf-8")
VERSAO = re.search(r"^Versao (\d+)", INSTR, re.M).group(1)
BLOCO_FLOW = re.search(r"## Bloco para a memoria do executor\n\n(.*?)\n## Historico resumido", INSTR, re.S).group(1).rstrip()

CHECKLIST = ("Checklist de envio: 34/34 aprovados (N/A: A2, A7 e A10 fiéis ao modelo e sem produto; "
             "C3, C4, C6 e C7 sem segunda pessoa, selfie, cena atuada ou motion control; "
             "E2 sem mecanismo, vídeo de growth)")
FICHA = "Ficha: 5/5 K, placar 14/14 cada (N/A com motivo: G2 em todos, G8 no K02)"


def entrega(a):
    ks, vs = G.keyframes(a), G.videos(a)
    L = [f"# ENTREGA | {a['nome']} | FityWell Growth Salmão na água", "",
         "Produção `fitywell_growth_salmao_agua` · Ângulo 2 · GROWTH · rodada de VALIDAÇÃO · perfil CLÁSSICO", "",
         f"## 1. INSTRUÇÕES PARA A MEMÓRIA DO AGENTE · GOOGLE FLOW AI (v{VERSAO})", "",
         "Colar inteiro na memória do agente antes do primeiro K.", "", "```text", BLOCO_FLOW, "```", "",
         CHECKLIST, "", FICHA, "",
         "## Anexos", "",
         f"- **Âncora {a['nome']}:** `{a['ancora']}` em TODOS os K.",
         f"- **Só no K01**, anexar também `{G.FRAME}` (referência de composição, nada além disso).",
         "- K01 a K05 casam com V01 a V05 pelo número.", "",
         "| Código | Take |", "|---|---|"]
    for k in ks:
        L.append(f"| {k['codigo']} / V{k['codigo'][1:]} | {k['take']}, {k['titulo']} |")
    L += ["", "## 2. PROMPTS DE IMAGEM (um bloco por K)", ""]
    for k in ks:
        anex = "ÂNCORA + FRAME DO MODELO" if k["anexos"] > 1 else "ÂNCORA"
        L += [f"### {k['codigo']} · {k['take']}, {k['titulo']} · anexar {anex}", "",
              "```text", k["codigo"], G.json_flow(k["j"]), "```", ""]
    L += ["## 3. PROMPTS DE VÍDEO (um bloco por V)", ""]
    for cod, take, kcod, txt in vs:
        L += [f"### {cod} · {take} · frame inicial = a imagem que você deixou no {kcod}", "",
              "```text", cod, txt, "```", ""]
    L += ["## 4. Montagem no CapCut", "", *G.montagem(), "",
          "## 5. Transcrição final por take", "", "| Take | English | Português |", "|---|---|---|"]
    for t in G.TAKES:
        L.append(f"| {t} | {G.FALAS[t]} | {G.TRANSCRICAO_PT[t]} |")
    L += ["", "## 6. Roteiro final em inglês", ""]
    for i, t in enumerate(G.TAKES, 1):
        L.append(f"{i}. {G.FALAS[t]}")
    L += ["", " ".join(G.FALAS[t] for t in G.TAKES), ""]
    return "\n".join(L)


if __name__ == "__main__":
    for a in G.AVATARES:
        (AQUI / f"ENTREGA_{a['arquivo']}.md").write_text(entrega(a), encoding="utf-8")
    print("ok: %d entregas, Flow v%s" % (len(G.AVATARES), VERSAO))
