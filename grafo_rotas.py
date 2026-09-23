# -*- coding: utf-8 -*-
"""
grafo_rotas.py - Costura doutrina e producao pelo vocabulario controlado.

Este e o substituto barato da passada semantica que ficaria pendente. Em vez de
~5M de tokens em subagentes, custa zero: rota, gatilho de obstaculo e gatilho de
virada sao vocabulario FECHADO e NUMERADO, entao os dois lados do grafo podem
ser casados por nome.

O grafo ja tinha os dois lados, sem nenhuma aresta entre eles:

    repo::memoria_banco_rotas_argumentativas_rota1...  "Rota 1: a ordem errada"
    repo-2::melody_pes_roteiro_rota1_ordem_errad       "Rota 1, a ordem errada"

Dois mecanismos, nesta ordem:

  1. NO x NO. Casa nos dos dois lados pelo numero da rota/gatilho. Quando o lado
     da producao nao traz numero ("Gatilho de virada: perda ativa"), casa pelo
     texto descritivo normalizado.
  2. ARQUIVO x DOUTRINA. Varre os ROTEIRO.md por mencao literal ("Rota 4",
     "gatilho 3") e liga o no do arquivo a doutrina. Pega os pacotes cuja
     extracao por LLM nao criou no de rota.

Nao inventa nada: os dois lados escrevem o mesmo nome, e o nome vem de uma lista
fechada que vive no banco-rotas-argumentativas e no banco-obstaculos.

Uso:
    python grafo_rotas.py --dry-run
    python grafo_rotas.py

LIMITE: nao regenera o GRAPH_REPORT.md, igual aos irmaos.

Criado em 2026-08-29.
"""
from __future__ import annotations
import sys
import os
import io
import re
import json
import glob
import unicodedata

import checar_entrega as CE

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

GRAFO = os.path.join("graphify-out", "graph.json")
ORIGEM = "rotas"


def norm(s):
    s = "".join(c for c in unicodedata.normalize("NFD", s or "")
                if unicodedata.category(c) != "Mn").lower()
    return re.sub(r"[^a-z0-9 ]+", " ", re.sub(r"\s+", " ", s)).strip()


# "Gatilho de virada 3" e "Gatilho 3" sao coisas DIFERENTES: um e escalada do
# fechamento, o outro e obstaculo. A ordem das alternativas importa.
RE_LABEL = re.compile(
    r"^\s*(?:(rota)|(gatilho\s+de\s+virada)|(gatilho))\s*(\d+)?\s*[:,\-]?\s*(.*)$",
    re.I)


def classificar(label):
    """('rota'|'virada'|'gatilho', numero_ou_None, descricao) ou None."""
    m = RE_LABEL.match(norm(label))
    if not m:
        return None
    tipo = "rota" if m.group(1) else ("virada" if m.group(2) else "gatilho")
    num = int(m.group(4)) if m.group(4) else None
    desc = m.group(5).strip()
    if num is None and not desc:
        return None
    return tipo, num, desc


def lado(node):
    """'doutrina' quando o no vem de memoria/PLAYBOOK, 'producao' caso contrario."""
    sf = (node.get("source_file") or "").replace("\\", "/").lower()
    if sf.startswith("memoria/") or sf.startswith("playbook_completo/"):
        return "doutrina"
    return "producao"


def main():
    dry = "--dry-run" in sys.argv[1:]
    if not os.path.exists(GRAFO):
        print("ERRO: %s nao existe." % GRAFO)
        return 2

    g = json.loads(io.open(GRAFO, encoding="utf-8").read())
    antes = len(g["links"])
    g["links"] = [e for e in g["links"] if e.get("origem") != ORIGEM]
    removidas = antes - len(g["links"])

    dout, prod = [], []
    por_id = {}
    for n in g["nodes"]:
        por_id[n["id"]] = n
        c = classificar(n.get("label") or "")
        if not c:
            continue
        (dout if lado(n) == "doutrina" else prod).append((c, n))

    # indices da doutrina
    por_num, por_desc = {}, {}
    for (tipo, num, desc), n in dout:
        if num is not None:
            por_num.setdefault((tipo, num), n)
        if desc:
            por_desc.setdefault((tipo, desc), n)

    arestas, exemplos = [], []
    vistos = set()

    def liga(src, tgt, conf, score, sf, motivo):
        if src == tgt or (src, tgt) in vistos:
            return
        vistos.add((src, tgt))
        arestas.append({
            "source": src, "target": tgt, "relation": "conceptually_related_to",
            "confidence": conf, "confidence_score": score,
            "source_file": sf, "source_location": None, "weight": 1.0,
            "origem": ORIGEM,
        })
        if len(exemplos) < 8:
            exemplos.append(motivo)

    # ---------------------------------------------------- 1. no x no
    casados_num = casados_desc = 0
    for (tipo, num, desc), n in prod:
        alvo = por_num.get((tipo, num)) if num is not None else None
        if alvo is not None:
            casados_num += 1
            liga(n["id"], alvo["id"], "EXTRACTED", 1.0, n.get("source_file"),
                 "%s  ->  %s" % ((n.get("label") or "")[:40], (alvo.get("label") or "")[:40]))
            continue
        alvo = por_desc.get((tipo, desc)) if desc else None
        if alvo is not None:
            casados_desc += 1
            liga(n["id"], alvo["id"], "INFERRED", 0.95, n.get("source_file"),
                 "%s  ~>  %s" % ((n.get("label") or "")[:40], (alvo.get("label") or "")[:40]))

    # ------------------------------------------- 2. arquivo x doutrina
    RE_MENCAO = re.compile(
        r"\b(?:(rota)|(gatilho\s+de\s+virada)|(gatilho))\s*(\d+)\b", re.I)
    mencoes = 0
    for d in sorted(glob.glob("producao/*")):
        pkg = os.path.basename(d)
        if not os.path.isdir(d) or pkg.startswith("_"):
            continue
        roteiro = CE.ler(os.path.join(d, "ROTEIRO.md"))
        if not roteiro:
            continue
        nid = "arquivo_" + re.sub(r"[^a-z0-9]+", "_",
                                  ("%s/ROTEIRO.md" % pkg).lower()).strip("_")
        if nid not in por_id:
            continue
        for m in RE_MENCAO.finditer(norm(roteiro)):
            tipo = "rota" if m.group(1) else ("virada" if m.group(2) else "gatilho")
            alvo = por_num.get((tipo, int(m.group(4))))
            if alvo is None:
                continue
            mencoes += 1
            liga(nid, alvo["id"], "EXTRACTED", 1.0, "%s/ROTEIRO.md" % pkg,
                 "%s/ROTEIRO.md  ->  %s" % (pkg, (alvo.get("label") or "")[:40]))

    g["links"].extend(arestas)

    print("nos de vocabulario: %d na doutrina, %d na producao" % (len(dout), len(prod)))
    print("casamento por numero  : %d" % casados_num)
    print("casamento por texto   : %d" % casados_desc)
    print("mencoes em ROTEIRO.md : %d" % mencoes)
    if removidas:
        print("substituidas          : %d arestas da rodada anterior" % removidas)
    print("arestas novas         : %d" % len(arestas))
    if exemplos:
        print("\nexemplos:")
        for e in exemplos:
            print("   %s" % e)

    if dry:
        print("\n--dry-run: nada foi escrito.")
        return 0

    io.open(GRAFO, "w", encoding="utf-8").write(json.dumps(g, ensure_ascii=False))
    print("\n%s: %d nos, %d arestas" % (GRAFO, len(g["nodes"]), len(g["links"])))
    print("GRAPH_REPORT.md NAO foi regenerado e agora esta atras na contagem.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
