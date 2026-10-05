#!/usr/bin/env python3
"""Gera a FILA do agente do Flow (v20) a partir de uma ENTREGA_*.md ou FLOW_*.md.

Uso: python gerar_fila.py producao/<pacote>/ENTREGA_X.md [-o FILA_X.md]
Sem -o, imprime na tela. Le os codigos REF-P, K e V dos titulos `### K01 ·` e `### V01 ·`
e o MAPA K/V (se houver). O agente do Flow atualiza a coluna Status a cada geracao.
"""
import argparse
import re
import sys
from pathlib import Path

RE_TITULO = re.compile(r"^###\s+(REF-P\d+|K\d+|V\d+)\b[^\n]*", re.M)
RE_MAPA = re.compile(r"^(V\d+):\s*(K\d+)\s*$", re.M)


def extrair(texto):
    codigos, vistos = [], set()
    for m in RE_TITULO.finditer(texto):
        c = m.group(1)
        if c in vistos:
            continue
        vistos.add(c)
        codigos.append((c, m.group(0)[4:].strip()))
    ordem = {"R": 0, "K": 1, "V": 2}
    codigos.sort(key=lambda x: (ordem[x[0][0]], int(re.search(r"\d+", x[0]).group())))
    return codigos, dict(RE_MAPA.findall(texto))


def montar(titulo, codigos, mapa):
    ks = [c for c, _ in codigos if c.startswith("K")]
    linhas = [
        "# FILA DO AGENTE DO FLOW | " + titulo, "",
        "Atualize a linha depois de CADA geracao e cole a tabela inteira no chat.",
        "Status: PENDENTE, GERANDO, PRONTO, FALHOU, BLOQUEADO, SELECIONADO (so o operador marca).", "",
        "| Codigo | Tipo | Alimenta/usa | Status | Tentativas | Nota |", "|---|---|---|---|---|---|",
    ]
    for c, _ in codigos:
        if c.startswith("V"):
            k = mapa.get(c)
            if not k:
                menores = [x for x in ks if int(x[1:]) <= int(c[1:])]
                k = menores[-1] if menores else "?"
            tipo, uso = "video", "INITIAL FRAME = imagem selecionada de " + k
        elif c.startswith("K"):
            tipo, uso = "imagem", "4 imagens, 9:16"
        else:
            tipo, uso = "character sheet", "sem anexo, aprovar antes dos K"
        linhas.append("| %s | %s | %s | PENDENTE | 0 | |" % (c, tipo, uso))
    linhas += ["", "Comandos: `status`, `proximo`, `refaz FALHOU`, `refaz K03`, `prossiga`, `parar`.", ""]
    return "\n".join(linhas)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("entrega")
    ap.add_argument("-o", "--saida")
    a = ap.parse_args()
    p = Path(a.entrega)
    codigos, mapa = extrair(p.read_text(encoding="utf-8"))
    if not codigos:
        sys.exit("nenhum codigo K/V encontrado em %s" % p)
    saida = montar(p.stem, codigos, mapa)
    if a.saida:
        Path(a.saida).write_text(saida, encoding="utf-8")
        print("%d codigos -> %s" % (len(codigos), a.saida))
    else:
        print(saida)


if __name__ == "__main__":
    main()
