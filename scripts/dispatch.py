#!/usr/bin/env python3
"""Entrada portátil: resolve a raiz real e usa o runtime isolado da operação."""
import os
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]

def main():
    if len(sys.argv) < 2:
        print("Uso: dispatch.py preparar|preflight|registrar-revisao|watch|minerar|instalar ...")
        return 2
    command, args = sys.argv[1], sys.argv[2:]
    if command == "instalar":
        target = [str(ROOT / "scripts" / "preparar_operacao.py")] + args
        executable = sys.executable
    else:
        executable = ROOT / ".venv-operacao" / ("Scripts/python.exe" if os.name == "nt" else "bin/python")
        if not executable.is_file():
            print("Runtime ausente. Execute com Python 3.10+: python3 " + str(ROOT / "scripts/preparar_operacao.py"), file=sys.stderr)
            return 2
        if command in ("preparar", "preflight", "registrar-revisao"):
            target = ["-m", "operacao.orquestrar", command] + args
        elif command == "watch":
            target = [str(ROOT / ".agents/skills/watch/scripts/watch_pipeline.py")] + args
        elif command == "minerar":
            target = ["-m", "operacao.mineracao"] + args
        else:
            print("Comando desconhecido: " + command, file=sys.stderr)
            return 2
    os.chdir(ROOT)
    os.execv(str(executable), [str(executable)] + target)

if __name__ == "__main__":
    sys.exit(main())
