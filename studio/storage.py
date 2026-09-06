import json
import os
import re
import sqlite3
import threading
import uuid
from contextlib import contextmanager
from datetime import datetime, timezone
from pathlib import Path

DATA = Path(os.environ.get('AURALY_DATA_DIR', Path(__file__).parent / 'data')).resolve()
LOCK = threading.RLock()


def now():
    return datetime.now(timezone.utc).isoformat()


@contextmanager
def connect():
    DATA.mkdir(parents=True, exist_ok=True)
    db = sqlite3.connect(DATA / 'studio.sqlite3', timeout=30)
    db.execute('CREATE TABLE IF NOT EXISTS projects (id TEXT PRIMARY KEY, updated TEXT, body TEXT)')
    try:
        yield db
        db.commit()
    except Exception:
        db.rollback()
        raise
    finally:
        db.close()


def folder(pid):
    if not re.fullmatch(r'[a-f0-9]{32}', pid):
        raise ValueError('Projeto inválido.')
    return DATA / pid


def get(pid):
    folder(pid)
    with connect() as db:
        row = db.execute('SELECT body FROM projects WHERE id=?', (pid,)).fetchone()
    if not row:
        raise KeyError('Projeto não encontrado.')
    return json.loads(row[0])


def save(project):
    project['updated'] = now()
    with LOCK, connect() as db:
        db.execute('INSERT OR REPLACE INTO projects VALUES(?,?,?)',
                   (project['id'], project['updated'], json.dumps(project, ensure_ascii=False)))
    return project


def change(pid, **fields):
    with LOCK:
        p = get(pid)
        p.update(fields)
        return save(p)


def event(pid, message):
    with LOCK:
        p = get(pid)
        p['events'].append({'time': now(), 'message': message})
        p['progress'] = message
        save(p)


def all_projects():
    with connect() as db:
        rows = db.execute('SELECT body FROM projects ORDER BY updated DESC').fetchall()
    return [json.loads(row[0]) for row in rows]


def create(title, avatar, direction):
    pid = uuid.uuid4().hex
    folder(pid).mkdir()
    return save({'id': pid, 'title': title, 'avatar': avatar, 'direction': direction,
                 'status': 'uploaded', 'busy': False, 'events': [], 'assets': {},
                 'calls': [], 'selected': [], 'created': now(), 'error': None})


def artifact(pid, relative):
    root = folder(pid).resolve()
    path = (root / relative).resolve()
    if not path.is_relative_to(root) or not path.is_file():
        raise ValueError('Arquivo indisponível.')
    return path


def write_json(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    temp = path.with_suffix(path.suffix + '.tmp')
    temp.write_text(json.dumps(value, ensure_ascii=False, indent=2), encoding='utf-8')
    temp.replace(path)
