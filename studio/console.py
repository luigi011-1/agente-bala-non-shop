"""Manual generation console: ordered prompt queue plus Downloads filing.

The operator generates each image themselves in their own ChatGPT session; this module
only removes the two steps that actually cause damage, picking the wrong prompt for an
avatar and filing the result by hand.
"""
import json
import re
import shutil
import subprocess
import threading
import time
from datetime import date
from pathlib import Path

from . import storage as store

IMAGE_SUFFIXES = {'.png', '.webp', '.jpg', '.jpeg'}
DOWNLOADS = Path.home() / 'Downloads'
_watch = {'thread': None, 'stop': None, 'filed': []}


def slug(value):
    value = re.sub(r'[^a-z0-9]+', '-', (value or '').lower()).strip('-')
    return value or 'avatar'


def _action(frame, seen):
    parent = frame.get('parent')
    if frame.get('role') == 'reference':
        return 'GERAR DO ZERO', 'Prop isolado, sem cenário.'
    if parent and parent in seen:
        return f'EDITAR do {parent}', 'Anexe a imagem já gerada do keyframe de origem.'
    return 'GERAR DO ZERO', 'Primeiro keyframe do setup; anexe a âncora do avatar.'


def queue(project_ids):
    """Flat, ordered step list across the chosen projects, in plan order."""
    steps = []
    for pid in project_ids:
        p = store.get(pid)
        plan = p.get('plan') or {}
        frames = plan.get('frames') or []
        if not frames:
            continue
        avatar = p.get('avatar') or 'Avatar'
        folder = store.folder(pid)
        anchor = folder / 'anchor.png'
        seen = set()
        for frame in frames:
            action, hint = _action(frame, seen)
            seen.add(frame.get('id'))
            attach = []
            if frame.get('role') != 'reference':
                attach.append({'label': f'Âncora de {avatar}', 'path': str(anchor)})
            parent = frame.get('parent')
            if parent:
                attach.append({'label': f'Keyframe de origem {parent}',
                               'path': str(folder / 'imagens' / f'{parent}.png')})
            steps.append({
                'project': pid, 'avatar': avatar, 'title': p.get('title', ''),
                'id': frame.get('id'), 'role': frame.get('role'),
                'frame_title': frame.get('title', ''), 'takes': frame.get('takes', []),
                'action': action, 'hint': hint, 'attach': attach,
                'prompt': json.dumps(frame.get('prompt', {}), ensure_ascii=False, indent=2),
                'destination': str(folder / 'imagens' / f'{frame.get("id")}.png'),
            })
    for index, step in enumerate(steps):
        step.update(index=index, total=len(steps))
    return steps


def copy_file_to_clipboard(path):
    """Windows only: puts the actual file on the clipboard so it can be pasted or dragged."""
    path = Path(path)
    if not path.is_file():
        raise ValueError('Arquivo indisponível para a área de transferência.')
    # Set-Clipboard needs one command string in an STA host; split arguments are not parsed.
    quoted = str(path).replace("'", "''")
    done = subprocess.run(['powershell', '-NoProfile', '-STA', '-Command', f"Set-Clipboard -Path '{quoted}'"],
                          capture_output=True, timeout=20)
    if done.returncode:
        raise ValueError('Não foi possível copiar o arquivo: ' + done.stderr.decode('utf-8', 'replace')[:200])
    return str(path)


def file_download(source, step):
    """Move one finished download into the project, named for its keyframe."""
    source = Path(source)
    if source.suffix.lower() not in IMAGE_SUFFIXES:
        raise ValueError('Só imagens são arquivadas.')
    destination = Path(step['destination'])
    destination.parent.mkdir(parents=True, exist_ok=True)
    stamp = date.today().isoformat()
    named = destination.with_name(f'{step["id"]}_{slug(step["avatar"])}_{stamp}{source.suffix.lower()}')
    if named.exists():
        named = named.with_name(f'{named.stem}_{int(time.time())}{named.suffix}')
    shutil.move(str(source), str(named))
    # The plan references <id>.png; keep that exact name pointing at the newest take.
    if named.suffix.lower() == '.png':
        shutil.copy2(named, destination)
    return str(named)


def _newest_image(after):
    if not DOWNLOADS.is_dir():
        return None
    candidates = [f for f in DOWNLOADS.iterdir()
                  if f.is_file() and f.suffix.lower() in IMAGE_SUFFIXES
                  and f.stat().st_mtime > after and not f.name.endswith('.crdownload')]
    if not candidates:
        return None
    newest = max(candidates, key=lambda f: f.stat().st_mtime)
    size = newest.stat().st_size
    time.sleep(1.5)
    return newest if newest.is_file() and newest.stat().st_size == size else None


def watch_once(step, timeout=900):
    """Block until one new image lands in Downloads, then file it against this step."""
    started = time.time()
    deadline = started + timeout
    while time.time() < deadline:
        if _watch['stop'] and _watch['stop'].is_set():
            return None
        found = _newest_image(started)
        if found:
            return file_download(found, step)
        time.sleep(1)
    return None


def start_watch(step):
    stop_watch()
    stop = threading.Event()
    result = {}

    def run():
        try:
            filed = watch_once(step)
            if filed:
                result['filed'] = filed
                _watch['filed'].append({'id': step['id'], 'avatar': step['avatar'], 'path': filed})
        except Exception as exc:
            result['error'] = str(exc)

    thread = threading.Thread(target=run, daemon=True)
    _watch.update(thread=thread, stop=stop, result=result)
    thread.start()
    return True


def stop_watch():
    if _watch['stop']:
        _watch['stop'].set()
    _watch.update(thread=None, stop=None)


def watch_state():
    thread = _watch['thread']
    return {'running': bool(thread and thread.is_alive()),
            'filed': _watch['filed'][-12:],
            'result': _watch.get('result', {})}
