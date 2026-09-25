"""Monta ENTREGA_<AVATAR>.md: o pacote inteiro de cada avatar num arquivo só, na ordem da entrega.

Ordem: instruções do agente Flow (bloco inteiro, v vigente) -> checklist de envio -> mapa de anexos ->
prompts de imagem (um bloco por K) -> prompts de vídeo (um bloco por V) -> montagem no CapCut ->
transcrição por take -> roteiro final em inglês (numerado + corrido), sempre o último bloco.
Tudo sai de gerar_pacote.py e do disco. Gabarito: fitywell_growth_froyo_bites/montar_entrega.py.
"""
import re
from pathlib import Path

import gerar_pacote as G

AQUI = Path(__file__).resolve().parent
INSTR = (AQUI.parent / "_flow" / "INSTRUCOES_AGENTE_FLOW.md").read_text(encoding="utf-8")
VERSAO = re.search(r"^Versao (\d+)", INSTR, re.M).group(1)
BLOCO_FLOW = re.search(r"## Bloco para a memoria do executor\n\n(.*?)\n## Historico resumido", INSTR, re.S).group(1).rstrip()

CHECKLIST = ("Checklist de envio: 33/33 aprovados (N/A: A2, A7, A9 fiéis ao modelo; C3 a C7 sem segunda pessoa, "
             "selfie, frase repetida, cena atuada ou motion control)")


def entrega(a):
    ks, vs = G.keyframes(a), G.videos(a)
    L = [f"# ENTREGA | {a['nome']} | FityWell Growth Modelo de intestino", "",
         "Produção `fitywell_growth_modelo_intestino` · Ângulo 2 · GROWTH · vídeo modelo de avatar IA · rodada de VALIDAÇÃO · perfil CLÁSSICO", "",
         f"## 1. INSTRUÇÕES PARA A MEMÓRIA DO AGENTE · GOOGLE FLOW AI (v{VERSAO})", "",
         "Colar inteiro na memória do agente antes do primeiro K.", "", "```text", BLOCO_FLOW, "```", "",
         CHECKLIST, "",
         "## Anexos", "",
         f"- **Âncora {a['nome']}:** `{a['ancora']}` em TODOS os K.",
         "- **Em cada K**, anexar também o frame do modelo daquele passo (`input/frames_modelo/Kxx_modelo.png`), "
         "só como referência de composição.",
         "- K01 a K13 casam com V01 a V13 pelo número. Todos os V têm fala.", "",
         "| Código | Take | Frame do modelo |", "|---|---|---|"]
    for k in ks:
        L.append(f"| {k['codigo']} / V{k['codigo'][1:]} | {k['take']}, {k['titulo']} | `{G.frame_modelo(k['codigo'])}` |")
    L += ["", "## 2. PROMPTS DE IMAGEM (um bloco por K)", ""]
    for k in ks:
        L += [f"### {k['codigo']} · {k['take']}, {k['titulo']} · anexar ÂNCORA + FRAME DO MODELO", "",
              "```text", k["codigo"], G.texto_flow(k["j"]), "```", ""]
    L += ["## 3. PROMPTS DE VÍDEO (um bloco por V)", ""]
    for cod, take, kcod, txt in vs:
        L += [f"### {cod} · {take} · frame inicial = a imagem que você deixou no {kcod}", "",
              "```text", cod, txt, "```", ""]
    L += ["## 4. Montagem no CapCut", ""] + G.capcut()
    L += ["", "## 5. Transcrição final por take", ""] + G.transcricao()
    L += ["", "## 6. Roteiro final em inglês", ""]
    for i, t in enumerate(G.TAKES, 1):
        L.append(f"{i}. " + (G.FALAS[t] if t in G.FALAS else f"(sem fala: voz-over do {G.VOZ_DE[t]})"))
    L += ["", " ".join(G.FALAS[t] for t in G.TAKES if t in G.FALAS), ""]
    return "\n".join(L)


if __name__ == "__main__":
    for a in G.AVATARES:
        (AQUI / f"ENTREGA_{a['arquivo']}.md").write_text(entrega(a), encoding="utf-8")
    print("ok: %d entregas, Flow v%s" % (len(G.AVATARES), VERSAO))
