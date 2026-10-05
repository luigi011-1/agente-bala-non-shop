"""Monta ENTREGA_BRANDON.md (brandon_seamoss_gengibre_limao): o pacote inteiro num arquivo só, na ordem da entrega.

Ordem: instruções do agente Flow (bloco inteiro, v vigente) -> checklist de envio -> mapa de anexos ->
prompts de imagem (um bloco por K) -> prompts de vídeo (um bloco por V) -> montagem no CapCut e legenda
do post -> transcrição por take -> roteiro final em inglês (numerado + corrido), sempre o último bloco.
Gabarito: brandon_seamoss_vizinha/montar_entrega.py.
"""
import re
from pathlib import Path

import gerar_pacote as G

AQUI = Path(__file__).resolve().parent
INSTR = (AQUI.parent / "_flow" / "INSTRUCOES_AGENTE_FLOW.md").read_text(encoding="utf-8")
VERSAO = re.search(r"^Versao (\d+)", INSTR, re.M).group(1)
assert int(VERSAO) >= 17, "o prompt de imagem sai em JSON: precisa do contrato do Flow v17 ou maior"
BLOCO_FLOW = re.search(r"## Bloco para a memoria do executor\n\n(.*?)\n## Historico resumido", INSTR, re.S).group(1).rstrip()

CHECKLIST = ("Checklist de envio: 32/32 aprovados (N/A: A1 a A4, A10 e A13 fiéis ao modelo na rodada de validação, "
             "sem arquivo de ganchos de variação; C3 sem segunda pessoa; C4 sem selfie; C6 sem cena atuada; C7 sem motion control)")


def entrega():
    ks, vs = G.keyframes(), G.videos()
    L = ["# ENTREGA | holistic.brandon | Natural Rems Sea Moss Venda, gengibre e limão em cubos de freezer", "",
         "Produção `brandon_seamoss_gengibre_limao` · Ângulo 1 (Natural Rems Sea Moss) · VENDA · rodada de VALIDAÇÃO · perfil CLÁSSICO", "",
         f"## 1. INSTRUÇÕES PARA A MEMÓRIA DO AGENTE · GOOGLE FLOW AI (v{VERSAO})", "",
         "Colar inteiro na memória do agente antes do primeiro K.", "", "```text", BLOCO_FLOW, "```", "",
         CHECKLIST, "",
         f"Ficha: {len(ks)}/{len(ks)} K conferidos contra o frame do modelo, placar F1 a F6 + G1 a G8 completo em cada "
         "um, com evidência literal (G2 N/A: sem céu nem janela em quadro) (`FICHA_FRAMES.md`, GATE_VISUAL Parte 6)", "",
         "## Mapa de anexos", "",
         f"- **Todos os K:** âncora `{G.ANCORA}` + frame do modelo de mesmo número (só composição).",
         f"- **K13 a K16:** também a foto do produto `{G.FOTO_PRODUTO}` (só o pote da frente).",
         f"- K01 a K{len(ks):02d} casam com V01 a V{len(ks):02d} pelo número. V03, V05, V06 e V09 são inserts mudos; V02, V04, V07 e V11 são B-roll com a fala como voz-over na edição.", "",
         "| Código | Take | Anexar, nesta ordem |", "|---|---|---|"]
    for k in ks:
        L.append(f"| {k['codigo']} / V{k['codigo'][1:]} | {k['take']}, {k['titulo']} | " + " + ".join(G.anexos(k)) + " |")
    L += ["", "## 2. PROMPTS DE IMAGEM (um bloco por K)", ""]
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
    for t in G.TAKES:
        L.append(f"{t[1:]}. " + G.FALAS.get(t, "(insert mudo, sem fala)"))
    L += ["", " ".join(G.FALAS[t] for t in G.TAKES if t in G.FALAS), ""]
    return "\n".join(L)


if __name__ == "__main__":
    (AQUI / "ENTREGA_BRANDON.md").write_text(entrega(), encoding="utf-8")
    print("ok: ENTREGA_BRANDON.md, Flow v%s" % VERSAO)
