#!/usr/bin/env python3
"""Instala runtime isolado e, opcionalmente, registra skills/agentes locais da operação."""
import argparse
import json
import os
from pathlib import Path
import platform
import shutil
import subprocess
import sys
import venv

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ("operacao-bala", "minerar-referencias", "adaptar-conteudo", "revisar-producao", "watch")
AGENTS = ("bala-pesquisador.toml", "bala-produtor.toml", "bala-revisor.toml")

def run(command):
    subprocess.run([str(x) for x in command], cwd=ROOT, check=True)

def ensure_python():
    if sys.version_info >= (3, 10):
        return
    choices = [shutil.which(n) for n in ("python3.12", "python3.11", "python3.10")]
    # Runtime fornecido pelo aplicativo, quando presente; nada é instalado no sistema.
    choices.append(Path.home() / ".cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3")
    for item in choices:
        if item and Path(item).is_file():
            result = subprocess.run([str(item), "-c", "import sys; sys.exit(0 if sys.version_info >= (3,10) else 1)"])
            if result.returncode == 0:
                os.execv(str(item), [str(item), str(Path(__file__).resolve())] + sys.argv[1:])
    raise RuntimeError("É necessário Python 3.10+; recomendado 3.12. Não encontrei runtime compatível.")

def link_plan(user_home):
    home = Path(user_home)
    return [(ROOT / ".agents/skills" / name, home / ".agents/skills" / name) for name in SKILLS] + [
        (ROOT / ".codex/agents" / name, home / ".codex/agents" / name) for name in AGENTS]

def install_links(user_home):
    plan = link_plan(user_home)
    # Verifica tudo antes de modificar; preserva skills e agentes que já existiam.
    for source, target in plan:
        if not source.exists():
            raise RuntimeError(f"Fonte ausente: {source}")
        if (target.exists() or target.is_symlink()) and target.resolve() != source.resolve():
            raise RuntimeError(f"Destino já pertence a outra instalação: {target}. Nenhum arquivo foi sobrescrito.")
    installed = []
    for source, target in plan:
        target.parent.mkdir(parents=True, exist_ok=True)
        if not target.is_symlink():
            target.symlink_to(source, target_is_directory=source.is_dir())
        installed.append(str(target))
    return installed

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--skip-deps", action="store_true", help="Só verificar e registrar; não reinstala pacotes.")
    parser.add_argument("--install-skills", action="store_true", help="Registra as cinco skills e três agentes no usuário local.")
    parser.add_argument("--warm-models", action="store_true", help="Baixa/cacheia small.en e o alinhador inglês; sem token.")
    parser.add_argument("--home", type=Path, default=Path.home(), help=argparse.SUPPRESS)
    args = parser.parse_args()
    try:
        ensure_python()
        environment = ROOT / ".venv-operacao"
        python = environment / ("Scripts/python.exe" if os.name == "nt" else "bin/python")
        if not python.exists():
            venv.EnvBuilder(with_pip=True).create(environment)
        if not args.skip_deps:
            requirements = ROOT / "operacao/requirements.txt"
            lock = ROOT / "operacao/requirements-macos-arm64.lock.txt"
            if sys.platform == "darwin" and platform.machine() == "arm64" and sys.version_info[:2] == (3, 12) and lock.is_file():
                requirements = lock
            run([python, "-m", "pip", "install", "--disable-pip-version-check", "-r", requirements])
            if not (Path('/Applications/Google Chrome.app').is_dir() or shutil.which('google-chrome') or shutil.which('google-chrome-stable')):
                run([python, '-m', 'playwright', 'install', 'chromium'])
        run([python, "-m", "pip", "check"])
        missing = [name for name in ("ffmpeg", "ffprobe") if not shutil.which(name)]
        if missing:
            raise RuntimeError("Instale FFmpeg no host antes de rodar /watch. Ausentes: " + ", ".join(missing))
        if args.warm_models:
            run([python, "-c", "from faster_whisper import WhisperModel; WhisperModel('small.en', device='cpu', compute_type='int8', cpu_threads=4); import whisperx; whisperx.load_align_model(language_code='en', device='cpu'); print('Modelos prontos no cache local.')"])
        installed = install_links(args.home) if args.install_skills else []
        run([python, "-m", "operacao.orquestrar", "preflight"])
        print(json.dumps({"runtime": str(python), "registered": installed}, ensure_ascii=False, indent=2))
    except (RuntimeError, OSError, subprocess.CalledProcessError) as error:
        print(f"ERRO: {error}", file=sys.stderr)
        return 2
    return 0

if __name__ == "__main__":
    sys.exit(main())
