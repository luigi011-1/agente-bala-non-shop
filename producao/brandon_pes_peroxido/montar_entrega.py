"""Monta ENTREGA_BRANDON.md (brandon_pes_peroxido): o pacote inteiro num arquivo só, na ordem da entrega.

Ordem: instruções do agente Flow (bloco inteiro, v vigente) -> checklist de envio -> mapa de anexos ->
prompts de imagem (um bloco por K) -> prompts de vídeo (um bloco por V) -> montagem no CapCut ->
transcrição por take -> roteiro final em inglês (numerado + corrido), sempre o último bloco.
Tudo sai de gerar_pacote.py e do disco. Gabarito: fitywell_growth_modelo_intestino/montar_entrega.py.

O contrato do Flow vigente (v17, imagem em JSON) ainda está só no branch claude/ola-d0d6f0; enquanto
ele não entra no main, o texto é lido de lá pelo git, e o arquivo local serve de reserva.
"""
import re
import subprocess
from pathlib import Path

import gerar_pacote as G

AQUI = Path(__file__).resolve().parent
try:
    INSTR = subprocess.run(["git", "show", "origin/claude/ola-d0d6f0:producao/_flow/INSTRUCOES_AGENTE_FLOW.md"],
                           cwd=AQUI, capture_output=True, text=True, check=True).stdout
except subprocess.CalledProcessError:
    INSTR = (AQUI.parent / "_flow" / "INSTRUCOES_AGENTE_FLOW.md").read_text(encoding="utf-8")
VERSAO = re.search(r"^Versao (\d+)", INSTR, re.M).group(1)
assert int(VERSAO) >= 17, "o prompt de imagem sai em JSON: precisa do contrato do Flow v17 ou maior"
BLOCO_FLOW = re.search(r"## Bloco para a memoria do executor\n\n(.*?)\n## Historico resumido", INSTR, re.S).group(1).rstrip()

CHECKLIST = ("Checklist de envio: 34/34 aprovados (N/A: A1, A2, A7 fiéis ao modelo; C3 a C7 sem segunda pessoa, "
             "selfie, frase repetida, cena atuada ou motion control)")


def entrega(a):
    ks, vs = G.keyframes(a), G.videos(a)
    L = ["# ENTREGA | holistic.brandon | FityWell Growth Pés com água oxigenada", "",
         "Produção `brandon_pes_peroxido` · Ângulo 2 · GROWTH · vídeo modelo de avatar IA · rodada de VALIDAÇÃO · perfil CLÁSSICO", "",
         f"## 1. INSTRUÇÕES PARA A MEMÓRIA DO AGENTE · GOOGLE FLOW AI (v{VERSAO})", "",
         "Colar inteiro na memória do agente antes do primeiro K.", "", "```text", BLOCO_FLOW, "```", "",
         CHECKLIST, "", "Ficha: 9/9 K conferidos contra o frame do modelo, placar 14/14 cada (`FICHA_FRAMES.md`, GATE_VISUAL Parte 6)", "",
         "## Anexos", "",
         f"- **Âncora holistic.brandon:** `{a['ancora']}` em TODOS os K (no K05, macro dos pés, ela entra pela pele e pelo cenário).",
         "- **Em cada K**, anexar também o frame do modelo daquele passo (`producao/brandon_pes_peroxido/input/frames_modelo/Kxx_modelo.png`), "
         "só como referência de composição.",
         "- K01 a K09 casam com V01 a V09 pelo número. Todos os V têm fala.", "",
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
        L.append(f"{i}. " + G.FALAS[t])
    L += ["", " ".join(G.FALAS[t] for t in G.TAKES), ""]
    return "\n".join(L)


if __name__ == "__main__":
    for a in G.AVATARES:
        (AQUI / f"ENTREGA_{a['arquivo']}.md").write_text(entrega(a), encoding="utf-8")
    print("ok: %d entrega(s), Flow v%s" % (len(G.AVATARES), VERSAO))
