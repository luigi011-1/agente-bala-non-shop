"""Monta ENTREGA_HOLISTIC_BRANDON.md: o pacote inteiro num arquivo só, na ordem da entrega.

Ordem: instruções do agente Flow (bloco inteiro, v vigente) -> checklist e ficha -> anexos e mapa K/V ->
PROMPTS DE IMAGEM (um bloco por K, em JSON) -> PROMPTS DE VÍDEO (um bloco por V) -> montagem no CapCut ->
transcrição por take -> roteiro final em inglês (numerado + corrido), sempre o último bloco.
"""
import re
from pathlib import Path

import gerar_pacote as G

AQUI = Path(__file__).resolve().parent
INSTR = (AQUI.parent / "_flow" / "INSTRUCOES_AGENTE_FLOW.md").read_text(encoding="utf-8")
VERSAO = re.search(r"^Versao (\d+)", INSTR, re.M).group(1)
BLOCO_FLOW = re.search(r"## Bloco para a memoria do executor\n\n(.*?)\n## Historico resumido", INSTR, re.S).group(1).rstrip()

CHECKLIST = ("Checklist de envio: 37/37 aprovados (N/A: A2 e A7 fiéis ao modelo; C3, C6 e C7 sem segunda "
             "pessoa, cena atuada ou motion control)")
FICHA = "Ficha: 10/10 K, placar 14/14 cada (N/A com motivo: G2 em todos, G8 nos closes sem rosto K02 a K08)"


def entrega():
    vs = G.videos()
    L = ["# ENTREGA | holistic.brandon | FityWell Venda Brownie de feijão preto", "",
         "Produção `fitywell_brownie_feijao` · Ângulo 2 · VENDA · rodada de VALIDAÇÃO · perfil CLÁSSICO", "",
         f"## 1. INSTRUÇÕES PARA A MEMÓRIA DO AGENTE · GOOGLE FLOW AI (v{VERSAO})", "",
         "Colar inteiro na memória do agente antes do primeiro K.", "", "```text", BLOCO_FLOW, "```", "",
         CHECKLIST, "", FICHA, "",
         "## Anexos e mapa K/V", "",
         f"- **Âncora holistic.brandon:** `{G.ANCORA}` em TODOS os K.",
         "- **Só no K01**, anexar também `input/frames_modelo/K01_modelo.png` (referência de composição, nada além disso).",
         "- Perfil clássico: cada V usa a imagem que sobrou no maior K de número menor ou igual ao dele.", "",
         "| V | Frame inicial | Take |", "|---|---|---|"]
    for cod, t, kc, _ in vs:
        k = next(x for x in G.KS if x["codigo"] == kc)
        L.append(f"| {cod} | {kc} | {t}{', ' + k['titulo'] if k['take'] == t else ', mesmo quadro do ' + kc} |")
    L += ["", "## 2. PROMPTS DE IMAGEM (um bloco por K)", ""]
    for k in G.KS:
        anex = "ÂNCORA + FRAME DO MODELO" if k["anexos"] > 1 else "ÂNCORA"
        L += [f"### {k['codigo']} · {k['take']}, {k['titulo']} · anexar {anex}", "",
              "```text", k["codigo"], G.json_flow(G.k_json(k)), "```", ""]
    L += ["## 3. PROMPTS DE VÍDEO (um bloco por V)", ""]
    for cod, t, kc, txt in vs:
        L += [f"### {cod} · {t} · frame inicial = a imagem que você deixou no {kc}", "", "```text", cod, txt, "```", ""]
    L += ["## 4. Montagem no CapCut", "", *G.montagem(), "",
          "## 5. Transcrição final por take", "", "| Take | English | Português |", "|---|---|---|"]
    for t in G.TAKES:
        L.append(f"| {t} | {G.FALAS.get(t, '(B-roll, sem fala)')} | {G.TRANSCRICAO_PT[t]} |")
    L += ["", "## 6. Roteiro final em inglês", ""]
    falados = [t for t in G.TAKES if t in G.FALAS]
    for t in falados:
        L.append(f"{t[1:]}. {G.FALAS[t]}")
    L += ["", " ".join(G.FALAS[t] for t in falados), ""]
    return "\n".join(L)


if __name__ == "__main__":
    (AQUI / "ENTREGA_HOLISTIC_BRANDON.md").write_text(entrega(), encoding="utf-8")
    print("ok: entrega Brandon, Flow v%s" % VERSAO)
