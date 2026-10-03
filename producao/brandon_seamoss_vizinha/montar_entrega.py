"""Monta ENTREGA_BRANDON.md (brandon_seamoss_vizinha): o pacote inteiro num arquivo só, na ordem da entrega.

Ordem: instruções do agente Flow (bloco inteiro, v vigente) -> checklist de envio -> mapa de anexos ->
character sheets REF-P -> prompts de imagem (um bloco por K) -> prompts de vídeo (um bloco por V) ->
montagem no CapCut e legenda do post -> transcrição por take -> roteiro final em inglês (numerado +
corrido), sempre o último bloco. Tudo sai de gerar_pacote.py e do disco. Gabarito: brandon_maca_alho.
"""
import re
from pathlib import Path

import gerar_pacote as G

AQUI = Path(__file__).resolve().parent
INSTR = (AQUI.parent / "_flow" / "INSTRUCOES_AGENTE_FLOW.md").read_text(encoding="utf-8")
VERSAO = re.search(r"^Versao (\d+)", INSTR, re.M).group(1)
assert int(VERSAO) >= 17, "o prompt de imagem sai em JSON: precisa do contrato do Flow v17 ou maior"
BLOCO_FLOW = re.search(r"## Bloco para a memoria do executor\n\n(.*?)\n## Historico resumido", INSTR, re.S).group(1).rstrip()

CHECKLIST = ("Checklist de envio: 35/35 aprovados (N/A: A1, A10, A12, A13 e A14 fiéis ao modelo na rodada de "
             "validação, sem arquivo de ganchos; C4 sem selfie; C7 sem motion control)")


def entrega():
    ks, vs, rs = G.keyframes(), G.videos(), G.refs_p()
    L = ["# ENTREGA | holistic.brandon | Natural Rems Sea Moss Venda, a vizinha de 57", "",
         "Produção `brandon_seamoss_vizinha` · Ângulo 1 (Natural Rems Sea Moss) · VENDA · vídeo modelo de avatar IA · "
         "movie style família B · rodada de VALIDAÇÃO · perfil CLÁSSICO", "",
         f"## 1. INSTRUÇÕES PARA A MEMÓRIA DO AGENTE · GOOGLE FLOW AI (v{VERSAO})", "",
         "Colar inteiro na memória do agente antes do primeiro REF-P.", "", "```text", BLOCO_FLOW, "```", "",
         CHECKLIST, "",
         f"Ficha: {len(ks)}/{len(ks)} K conferidos contra o frame do modelo, placar F1 a F6 + G1 a G8 completo em "
         "cada um, com evidência literal (N/A só em G2 no box, sem céu nem janela em quadro, e G8 nos takes sem fala) "
         "(`FICHA_FRAMES.md`, GATE_VISUAL Parte 6)", "",
         "## Mapa de anexos", "",
         "- **REF-P1 a REF-P3:** gerar do zero, sem anexo, e aprovar os três antes do primeiro K.",
         "- **K01 a K15 (esquete):** os REF-P aprovados de quem está em quadro, na ordem abaixo, e por último o frame do modelo (só composição).",
         f"- **K16 a K35 (Brandon):** âncora `{G.ANCORA}` + frame do modelo (só composição); do K31 ao K35 também a foto do produto `{G.FOTO_PRODUTO}`.",
         f"- K01 a K{len(ks):02d} casam com V01 a V{len(ks):02d} pelo número. V01, V02 e V15 são sem fala.", "",
         "| Código | Take | Anexar, nesta ordem |", "|---|---|---|"]
    for r in rs:
        L.append(f"| {r['codigo']} | elenco, {r['nome']} | nenhuma |")
    for k in ks:
        L.append(f"| {k['codigo']} / V{k['codigo'][1:]} | {k['take']}, {k['titulo']} | " + " + ".join(G.anexos(k)) + " |")
    L += ["", "## 2. PROMPTS DE IMAGEM", "", "### Character sheets (gerar e aprovar antes dos K)", ""]
    for r in rs:
        L += [f"### {r['codigo']} · {r['nome']} · sem anexo", "", "```text", r["codigo"], G.texto_flow_ref(r["j"]), "```", ""]
    L += ["### Keyframes (um bloco por K)", ""]
    for k in ks:
        L += [f"### {k['codigo']} · {k['take']}, {k['titulo']} · anexar " + " + ".join(a.split(" `")[0] for a in G.anexos(k)), "",
              "```text", k["codigo"], G.texto_flow(k["j"]), "```", ""]
    L += ["## 3. PROMPTS DE VÍDEO (um bloco por V)", ""]
    for cod, take, kcod, txt in vs:
        L += [f"### {cod} · {take} · frame inicial = a imagem que você deixou no {kcod}", "",
              "```text", cod, txt, "```", ""]
    L += ["## 4. Montagem no CapCut", ""] + G.capcut()
    L += ["", "## 5. Legenda do post", ""] + [f"- {x}" for x in G.LEGENDA]
    L += ["", "## 6. Transcrição final por take", ""] + G.transcricao()
    L += ["", "## 7. Roteiro final em inglês", ""]
    falados = [t for t in G.TAKES if t in G.FALAS]
    for t in G.TAKES:
        L.append(f"{t[1:]}. " + G.FALAS.get(t, "(sem fala)" if t != "T15" else "(voz-over do T14: literally everything)"))
    L += ["", " ".join(G.FALAS[t] for t in falados), ""]
    return "\n".join(L)


if __name__ == "__main__":
    (AQUI / "ENTREGA_BRANDON.md").write_text(entrega(), encoding="utf-8")
    print("ok: ENTREGA_BRANDON.md, Flow v%s" % VERSAO)
