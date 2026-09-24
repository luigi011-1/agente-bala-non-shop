"""Monta ENTREGA_<AVATAR>.md: o pacote inteiro de cada avatar num arquivo só, na ordem da entrega.

Ordem: instruções do agente Flow (bloco inteiro, v vigente) -> checklist de envio -> mapa de anexos ->
BLOCO DE IMAGEM -> BLOCO DE VÍDEO -> montagem no CapCut -> transcrição por take -> roteiro final em
inglês (numerado + corrido), que é sempre o último bloco. Tudo sai de gerar_pacote.py e do disco.
"""
import re
from pathlib import Path

import gerar_pacote as G

AQUI = Path(__file__).resolve().parent
INSTR = (AQUI.parent / "_flow" / "INSTRUCOES_AGENTE_FLOW.md").read_text(encoding="utf-8")
VERSAO = re.search(r"^Versao (\d+)", INSTR, re.M).group(1)
BLOCO_FLOW = re.search(r"## Bloco para a memoria do executor\n\n(.*?)\n## Historico resumido", INSTR, re.S).group(1).rstrip()

CHECKLIST = ("Checklist de envio: 32/32 aprovados (N/A: A1, A2, A7 fiéis ao modelo; C3 a C7 sem segunda pessoa, "
             "selfie, frase repetida ou motion control; E4 roteiro aprovado literal do modelo)")


def entrega(a):
    ks, vs = G.keyframes(a), G.videos(a)
    f, pt = G.falas(a)
    L = [f"# ENTREGA | {a['nome']} | FityWell Growth Água no modelo dental", "",
         "Produção `fitywell_growth_dentes_agua` · Ângulo 2 · GROWTH · rodada de VALIDAÇÃO · perfil CLÁSSICO", "",
         f"## 1. INSTRUÇÕES PARA A MEMÓRIA DO AGENTE · GOOGLE FLOW AI (v{VERSAO})", "",
         "Colar inteiro na memória do agente antes do primeiro K.", "", "```text", BLOCO_FLOW, "```", "",
         CHECKLIST, "",
         "## Anexos", "",
         f"- **Âncora {a['nome']}:** `{a['ancora']}` em TODOS os K.",
         f"- **Só no K01**, anexar também `{G.FRAME_MODELO}` (referência de composição, nada além disso).",
         "- K01 a K07 casam com V01 a V07 pelo número.", "",
         "| Código | Take |", "|---|---|"]
    for k in ks:
        L.append(f"| {k['codigo']} / V{k['codigo'][1:]} | {k['take']}, {k['titulo']} |")
    # Um bloco copiável por prompt (Luigi, 2026-09-24). O título fica FORA do bloco; dentro, só o
    # código sozinho na primeira linha e o prompt completo, no formato de sempre do Flow.
    L += ["", "## 2. PROMPTS DE IMAGEM (um bloco por K)", ""]
    for k in ks:
        anex = "ÂNCORA + FRAME DO MODELO" if k["anexos"] > 1 else "ÂNCORA"
        L += [f"### {k['codigo']} · {k['take']}, {k['titulo']} · anexar {anex}", "",
              "```text", k["codigo"], G.texto_flow(k["j"]), "```", ""]
    L += ["## 3. PROMPTS DE VÍDEO (um bloco por V)", ""]
    for cod, take, kcod, txt in vs:
        L += [f"### {cod} · {take} · frame inicial = a imagem que você deixou no {kcod}", "",
              "```text", cod, txt, "```", ""]
    L += ["## 4. Montagem no CapCut", "",
          "1. Clipes na ordem: V01, V02, V03, V04, V05, V06, V07.",
          "2. Cortar cada clipe no tempo da cena do modelo: " + "; ".join(f"V{t[1:].zfill(2)} {G.CORTE[t]}" for t in G.TAKES) + ".",
          "3. Zero tempo morto: todo clipe começa já falando. Isolate Voice / Keep Vocal no áudio.",
          "4. V03 é cena curta: cortar logo depois de \"paste\".",
          "5. Legenda palavra a palavra em serifa itálica branca no meio do quadro, igual ao modelo, do começo ao fim.",
          "6. Sem Voice Changer: a voz vem do prompt de cada V.",
          "7. Música só do V02 em diante, nunca no gancho, entre -19 e -20 dB, fora da biblioteca do TikTok.",
          "8. Rótulo pequeno `AI-generated` num canto do vídeo.", "",
          "## 5. Transcrição final por take", "", "| Take | English | Português |", "|---|---|---|"]
    for t in G.TAKES:
        L.append(f"| {t} | {f[t]} | {pt[t]} |")
    L += ["", "## 6. Roteiro final em inglês", ""]
    for i, t in enumerate(G.TAKES, 1):
        L.append(f"{i}. {f[t]}")
    L += ["", " ".join(f[t] for t in G.TAKES), ""]
    return "\n".join(L)


if __name__ == "__main__":
    for a in G.AVATARES:
        (AQUI / f"ENTREGA_{a['arquivo']}.md").write_text(entrega(a), encoding="utf-8")
    print("ok: %d entregas, Flow v%s" % (len(G.AVATARES), VERSAO))
