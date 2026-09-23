# -*- coding: utf-8 -*-
"""
checar_rotacao.py - O PORTAO P10, que o CLAUDE.md chama de "o furo mais caro".

Depois que um video vai ao ar, alguem tem que escrever no LOG de rotacao do
banco-rotas-argumentativas e na biblioteca-videos. Ninguem escreve, entao os
documentos envelhecem e a rota se repete sem que ninguem perceba.

Este script compara as pastas de producao/ com o que os dois documentos
registram e lista o que ficou de fora.

HEURISTICA, e ele avisa que e: o log usa nome descritivo ("Escalda-pes /
peroxido (Melody)"), nao o slug da pasta. O casamento e feito pelo token
distintivo do slug (melody_pes -> "pes") procurado no texto sem acento. Falso
negativo e possivel, entao a saida e AVISO e nunca FALHA.

RESSALVA DO ANGULO 3: pode legitimamente nao ter beat de rota, porque o
fechamento pode viver no DM.md. O script marca esses a parte.

Uso:
    python checar_rotacao.py

Criado em 2026-08-29.
"""
from __future__ import annotations
import sys
import os
import io
import re
import glob
import unicodedata

import memoria_lib as ML
import checar_entrega as CE

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

DOCS = {
    "rotacao": "banco_rotas_argumentativas.md",
    "biblioteca": "biblioteca_videos.md",
}


def sem_acento(s):
    return "".join(c for c in unicodedata.normalize("NFD", s)
                   if unicodedata.category(c) != "Mn").lower()


def token_do_pacote(nome):
    """melody_pes -> 'pes'. E a parte que distingue o video dentro da conta."""
    partes = nome.split("_", 1)
    return sem_acento(partes[1]) if len(partes) > 1 else sem_acento(nome)


def angulo_do_pacote(pasta):
    roteiro = CE.ler(os.path.join(pasta, "ROTEIRO.md")) or ""
    prompts = CE.ler(os.path.join(pasta, "PROMPTS_PRODUCAO.md")) or ""
    return CE.detectar_angulo(roteiro, prompts)


def main():
    dir_memoria = ML.localizar_memoria_viva(".")
    if not dir_memoria:
        print("ERRO: nao achei a memoria viva. Definir MEMORIA_VIVA.")
        return 2

    textos = {}
    for chave, arquivo in DOCS.items():
        path = os.path.join(dir_memoria, arquivo)
        if not os.path.exists(path):
            print("ERRO: %s nao existe na memoria viva." % arquivo)
            return 2
        textos[chave] = sem_acento(io.open(path, encoding="utf-8").read())

    pacotes = []
    for d in sorted(glob.glob("producao/*")):
        nome = os.path.basename(d)
        if not os.path.isdir(d) or nome.startswith("_"):
            continue
        if not os.path.exists(os.path.join(d, "ROTEIRO.md")):
            continue
        pacotes.append((nome, d))

    faltando_rot, faltando_bib, ok_dois, angulo3 = [], [], [], []
    for nome, pasta in pacotes:
        tok = token_do_pacote(nome)
        no_rot = tok in textos["rotacao"] or sem_acento(nome) in textos["rotacao"]
        no_bib = tok in textos["biblioteca"] or sem_acento(nome) in textos["biblioteca"]
        ang = angulo_do_pacote(pasta)
        if not no_rot and str(ang) == "3":
            angulo3.append((nome, no_bib))
        elif not no_rot:
            faltando_rot.append((nome, ang, no_bib))
        if not no_bib:
            faltando_bib.append(nome)
        if no_rot and no_bib:
            ok_dois.append(nome)

    print("=" * 82)
    print("  PORTAO P10 | %d pacotes de producao com ROTEIRO.md" % len(pacotes))
    print("=" * 82)
    print("  [OK]     nos dois documentos: %d  (%s)"
          % (len(ok_dois), ", ".join(ok_dois) if ok_dois else "nenhum"))

    if faltando_rot:
        print("\n  [AVISO]  sem registro aparente no LOG de rotacao (%d):" % len(faltando_rot))
        for nome, ang, no_bib in faltando_rot:
            print("             %-24s angulo %-3s %s"
                  % (nome, ang or "?", "" if no_bib else "(e tambem fora da biblioteca)"))
        print("           -> escrever data, video, angulo, rota e obstaculo em")
        print("              banco-rotas-argumentativas, secao 'Log de rotas usadas'")

    if angulo3:
        print("\n  [AVISO]  Angulo 3 sem registro de rota (%d), pode ser legitimo:" % len(angulo3))
        for nome, no_bib in angulo3:
            print("             %-24s %s" % (nome, "" if no_bib else "(fora da biblioteca tambem)"))
        print("           -> no Angulo 3 o fechamento pode viver no DM.md. Conferir e,")
        print("              se houver rota no video, registrar mesmo assim")

    if faltando_bib:
        print("\n  [AVISO]  fora da biblioteca-videos (%d): %s"
              % (len(faltando_bib), ", ".join(faltando_bib)))
        print("           -> a biblioteca e o que responde 'esse esqueleto ja rodou?' no P1")

    print("\n" + "-" * 82)
    print("  Heuristica por token do slug. Falso negativo e possivel, por isso AVISO.")
    print()
    return 0


if __name__ == "__main__":
    sys.exit(main())
