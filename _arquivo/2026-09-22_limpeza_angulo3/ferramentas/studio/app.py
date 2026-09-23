import asyncio
import hmac
import io
import json
import os
import re
import secrets
import shutil
import subprocess
import uuid
from concurrent.futures import ThreadPoolExecutor
from contextlib import asynccontextmanager
from pathlib import Path
from urllib.parse import urlparse

from fastapi import FastAPI, File, Form, HTTPException, Request, UploadFile
from fastapi.responses import FileResponse, HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.exceptions import RequestValidationError
from PIL import Image, ImageOps
from pydantic import BaseModel, Field

from . import engine, provider, browser_queue, storage as store
from .rules import snapshot, validate_script

TOKEN = secrets.token_urlsafe(32)
POOL = ThreadPoolExecutor(max_workers=2)
STATIC = Path(__file__).parent / 'static'
MAX_UPLOAD = 500 * 1024 * 1024
VERSION = '0.7.0'


@asynccontextmanager
async def lifespan(app):
    provider.load_preferences()
    browser_queue.recover()
    for p in store.all_projects():
        if p.get('busy'):
            store.change(p['id'], busy=False, error='Servidor reiniciado. Retome a etapa; resultados anteriores preservados.')
    yield


app = FastAPI(title='Auraly Studio', lifespan=lifespan)


@app.middleware('http')
async def local_boundary(request: Request, call_next):
    host = request.headers.get('host', '').split(':')[0]
    if host not in ['127.0.0.1', 'localhost', 'testserver']:
        return JSONResponse({'detail': 'Somente acesso local.'}, status_code=403)
    origin = request.headers.get('origin')
    bridge = request.url.path.startswith('/api/browser/agent/')
    extension = bool(origin and re.fullmatch(r'chrome-extension://[a-p]{32}', origin))
    if bridge and request.method == 'OPTIONS' and extension:
        return JSONResponse({}, headers={'Access-Control-Allow-Origin': origin,
            'Access-Control-Allow-Headers': 'content-type,x-auraly-browser-token',
            'Access-Control-Allow-Methods': 'GET,POST,OPTIONS', 'Access-Control-Allow-Private-Network': 'true'})
    if bridge and not hmac.compare_digest(request.headers.get('x-auraly-browser-token', ''), browser_queue.token()):
        return JSONResponse({'detail': 'Conecte a extensão com o código do Studio.'}, status_code=403)
    if origin and urlparse(origin).netloc != request.headers.get('host') and not (bridge and extension):
        return JSONResponse({'detail': 'Origem não permitida.'}, status_code=403)
    if request.method not in ['GET', 'HEAD', 'OPTIONS']:
        if not bridge and not hmac.compare_digest(request.headers.get('x-studio-token', ''), TOKEN):
            return JSONResponse({'detail': 'Recarregue o programa para renovar a sessão local.'}, status_code=403)
        try:
            size = int(request.headers.get('content-length', '0'))
        except ValueError:
            return JSONResponse({'detail': 'Tamanho inválido.'}, status_code=400)
        if size > MAX_UPLOAD + 30 * 1024 * 1024:
            return JSONResponse({'detail': 'Upload máximo: 500 MB de vídeo e 20 MB de imagem.'}, status_code=413)
    response = await call_next(request)
    if bridge and extension:
        response.headers['Access-Control-Allow-Origin'] = origin
    response.headers['X-Content-Type-Options'] = 'nosniff'
    response.headers['Referrer-Policy'] = 'no-referrer'
    response.headers['Cache-Control'] = 'no-store'
    response.headers['Content-Security-Policy'] = "default-src 'self'; img-src 'self' blob: data:; media-src 'self' blob:; style-src 'self'; script-src 'self'; connect-src 'self'; frame-ancestors 'none'"
    return response


@app.exception_handler(ValueError)
async def value_error(request, exc):
    return JSONResponse({'detail': provider.safe_error(exc)}, status_code=400)


@app.exception_handler(RequestValidationError)
async def invalid_request(request, exc):
    # Pydantic's default response echoes rejected values, including API keys.
    return JSONResponse({'detail': 'Campos inválidos: ' + ', '.join(
        '.'.join(str(x) for x in e['loc']) for e in exc.errors())}, status_code=422)


@app.exception_handler(KeyError)
async def key_error(request, exc):
    return JSONResponse({'detail': 'Projeto não encontrado.'}, status_code=404)


@app.get('/', response_class=HTMLResponse)
def index():
    return (STATIC / 'index.html').read_text(encoding='utf-8').replace('__TOKEN__', TOKEN)


@app.get('/browser', response_class=HTMLResponse)
def browser_page():
    return (STATIC / 'browser.html').read_text(encoding='utf-8').replace('__TOKEN__', TOKEN)


# ------------------------------------------------------------------ browser queue

class BrowserQueue(BaseModel):
    ids: list[str] = Field(min_length=1, max_length=4)
    limit: int | None = Field(default=None, ge=1, le=30)


class BrowserControl(BaseModel):
    running: bool
    concurrency: int = Field(default=2, ge=1, le=4)


class BrowserUpdate(BaseModel):
    status: str
    tab_id: int | None = None
    conversation_url: str | None = None
    error: str | None = Field(default=None, max_length=1000)


class BrowserRecovery(BaseModel):
    action: str = Field(pattern='^(inspect|retry)$')


class BrowserReview(BaseModel):
    decision: str = Field(pattern='^(approve|retry)$')
    comment: str = Field(default='', max_length=2000)


class BrowserPreflight(BaseModel):
    job_id: str = Field(min_length=1, max_length=100)
    canonical_asset_fingerprint: str = Field(pattern='^[a-f0-9]{64}$')
    tab_id: int
    window_id: int
    url: str = Field(max_length=500)
    extension_session_id: str = Field(min_length=16, max_length=200)
    nonce: str = Field(min_length=16, max_length=200)
    content_script_ready: bool
    composer_ready: bool
    upload_ready: bool
    draft_empty: bool
    generation_idle: bool
    modal_clear: bool
    conversation_clean: bool


class BrowserActivation(BaseModel):
    canonical_asset_fingerprint: str = Field(pattern='^[a-f0-9]{64}$')
    preflight_id: str = Field(pattern='^[a-f0-9]{32}$')
    revalidation: BrowserPreflight


class BrowserSession(BaseModel):
    extension_session_id: str = Field(min_length=16, max_length=200)
    agent_protocol_version: str | None = Field(default=None, max_length=50)
    agent_capabilities: list[str] | None = Field(default=None, max_length=32)


class BrowserPreflightRequest(BaseModel):
    canonical_asset_fingerprint: str = Field(pattern='^[a-f0-9]{64}$')
    requested_tab_id: int | None = None


class BrowserPreflightChecking(BaseModel):
    request_id: str = Field(pattern='^[a-f0-9]{32}$')
    job_id: str = Field(min_length=1, max_length=100)
    canonical_asset_fingerprint: str = Field(pattern='^[a-f0-9]{64}$')
    extension_session_id: str = Field(min_length=16, max_length=200)


class BrowserPreflightFailure(BaseModel):
    request_id: str = Field(pattern='^[a-f0-9]{32}$')
    extension_session_id: str = Field(min_length=16, max_length=200)
    error: str = Field(min_length=1, max_length=1000)


@app.post('/api/browser/jobs/{jid}/review')
def browser_review(jid: str, data: BrowserReview):
    return browser_queue.review(jid, data.decision, data.comment)


@app.get('/api/browser/jobs/{jid}/result')
def browser_result(jid: str):
    return FileResponse(browser_queue.result_file(jid))


@app.post('/api/browser/projects/{pid}/avatars/{aid}/export')
def browser_export(pid: str, aid: str):
    path = browser_queue.export_package(pid, aid)
    return FileResponse(path, media_type='application/zip', filename=path.name)


@app.post('/api/browser/jobs/{jid}/recover')
def browser_recover(jid: str, data: BrowserRecovery):
    return browser_queue.recover_job(jid, data.action)


@app.get('/api/browser/state')
def browser_state():
    return browser_queue.load()


@app.post('/api/browser/connection')
def browser_connection():
    return {'token': browser_queue.token(), 'extension_dir': str(STATIC.parent / 'chrome-extension')}


@app.post('/api/browser/queue')
def browser_enqueue(data: BrowserQueue):
    return browser_queue.enqueue(data.ids, data.limit)


@app.post('/api/browser/control')
def browser_control(data: BrowserControl):
    return browser_queue.control(data.running, data.concurrency)


REQUIRED_CAPABILITIES = {
    'canonical_materialized_jobs', 'multiple_references', 'preflight_handshake',
    'preflight_polling', 'batch_preflight', 'dedicated_tab_creation',
}


@app.post('/api/browser/agent/state')
def browser_agent_state(data: BrowserSession):
    reported = set(data.agent_capabilities or [])
    missing = REQUIRED_CAPABILITIES - reported
    state = browser_queue.heartbeat(
        data.extension_session_id,
        agent_protocol_version=data.agent_protocol_version,
        agent_capabilities=list(reported),
    )
    if missing:
        state['extension_reload_required'] = True
        state['missing_capabilities'] = sorted(missing)
    else:
        state['extension_reload_required'] = False
        state['missing_capabilities'] = []
    return state


@app.post('/api/browser/agent/preflight')
def browser_preflight(data: BrowserPreflight):
    return browser_queue.register_preflight(data.model_dump())


@app.post('/api/browser/jobs/{jid}/preflight-request')
def browser_preflight_request(jid: str, data: BrowserPreflightRequest):
    return browser_queue.request_preflight(jid, data.canonical_asset_fingerprint, data.requested_tab_id)


@app.post('/api/browser/agent/preflight-requests/checking')
def browser_preflight_checking(data: BrowserPreflightChecking):
    return browser_queue.mark_preflight_checking(data.request_id, data.job_id,
                                                  data.canonical_asset_fingerprint, data.extension_session_id)


@app.post('/api/browser/agent/preflight-requests/failed')
def browser_preflight_failed(data: BrowserPreflightFailure):
    return browser_queue.fail_preflight_request(data.request_id, data.extension_session_id, data.error)


@app.post('/api/browser/agent/jobs/{jid}/activate')
def browser_activate(jid: str, data: BrowserActivation):
    if data.revalidation.job_id != jid or data.revalidation.canonical_asset_fingerprint != data.canonical_asset_fingerprint:
        raise ValueError('A revalidação não corresponde ao job solicitado.')
    return browser_queue.activate_materialized(jid, data.canonical_asset_fingerprint,
                                               data.preflight_id, data.revalidation.model_dump())


class BatchAuthorization(BaseModel):
    production_id: str = Field(min_length=1, max_length=200)
    pipeline: str = Field(pattern='^auraly_soulmate$')
    avatar_id: str = Field(min_length=1, max_length=200)
    asset_fingerprints: dict[str, str]  # asset_id -> canonical_asset_fingerprint


@app.post('/api/browser/batches')
def create_batch(data: BatchAuthorization):
    for fp in data.asset_fingerprints.values():
        if not re.fullmatch(r'[a-f0-9]{64}', fp):
            raise ValueError('Fingerprint inválido; esperado sha256 hex de 64 caracteres.')
    return browser_queue.authorize_batch(
        data.production_id, data.pipeline, data.avatar_id, data.asset_fingerprints)


@app.post('/api/browser/batches/{batch_id}/dispatch')
def dispatch_batch(batch_id: str):
    return browser_queue.dispatch_batch(batch_id)


@app.get('/api/browser/batches/{batch_id}')
def get_batch(batch_id: str):
    return browser_queue.get_batch(batch_id)


@app.post('/api/browser/agent/claim')
def browser_claim():
    return {'job': browser_queue.claim()}


@app.post('/api/browser/agent/jobs/{jid}')
def browser_update(jid: str, data: BrowserUpdate):
    return browser_queue.update(jid, **data.model_dump())


@app.get('/api/browser/agent/jobs/{jid}/anchor')
def browser_anchor(jid: str):
    return FileResponse(browser_queue.anchor(jid), media_type='image/png')


@app.get('/api/browser/agent/jobs/{jid}/references/{role}')
def browser_reference(jid: str, role: str):
    if role not in {'avatar_anchor', 'shared_card_reference', 'parent_approved_result'}:
        raise ValueError('Papel de referência inválido.')
    return FileResponse(browser_queue.reference(jid, role), media_type='application/octet-stream')


@app.post('/api/browser/agent/jobs/{jid}/image')
async def browser_image(jid: str, request: Request):
    raw = bytearray()
    async for chunk in request.stream():
        raw.extend(chunk)
        if len(raw) > 35 * 1024 * 1024:
            raise ValueError('Imagem acima de 35 MB.')
    return await asyncio.to_thread(browser_queue.receive, jid, bytes(raw))


app.mount('/static', StaticFiles(directory=STATIC), name='static')


# ------------------------------------------------------------------ config

@app.get('/api/config')
def config():
    ff = shutil.which('ffmpeg') or str(Path(os.environ.get('LOCALAPPDATA', '')) / 'Microsoft/WinGet/Links/ffmpeg.exe')
    return {**provider.settings(), 'ffmpeg': Path(ff).is_file(),
            'data_dir': str(store.DATA), 'version': VERSION}


class Settings(BaseModel):
    text_provider: str | None = Field(default=None, pattern='^(auto|openai|gemini|groq)$')
    api_key: str | None = Field(default=None, max_length=500)
    gemini_key: str | None = Field(default=None, max_length=500)
    groq_key: str | None = Field(default=None, max_length=500)
    text_model: str = Field(default=provider.DEFAULT_MODEL, pattern=r'^[a-zA-Z0-9._-]+$', max_length=80)
    reasoning_effort: str = Field(default='medium', pattern=r'^(low|medium|high|xhigh|max)$')


@app.post('/api/config')
def set_config(data: Settings):
    if any(p.get('busy') for p in store.all_projects()):
        raise ValueError('Aguarde as etapas em andamento antes de trocar a conexão.')
    provider.configure(data.api_key, data.text_model, data.reasoning_effort,
                       gemini_key=data.gemini_key, groq_key=data.groq_key,
                       text_provider=data.text_provider)
    provider.save_preferences()
    return provider.settings()


@app.post('/api/config/verify')
def verify_config():
    return provider.verify_access()


# ------------------------------------------------------------------ projects

@app.get('/api/projects')
def projects():
    return [{k: p.get(k) for k in ['id', 'title', 'status', 'busy', 'updated', 'progress',
                                   'error', 'queue_state', 'active_text_provider']}
            | {'avatars': len(p.get('avatars', []))}
            for p in store.all_projects()]


@app.get('/api/projects/{pid}')
def project(pid: str):
    return store.get(pid)


@app.post('/api/projects')
async def upload(title: str = Form(...), direction: str = Form(''), video: UploadFile = File(...)):
    if not (video.filename or '').lower().endswith('.mp4'):
        raise ValueError('Envie um arquivo .mp4.')
    if not title.strip() or len(title) > 120 or len(direction) > 5000:
        raise ValueError('Título ou briefing inválido.')
    p = store.create(title.strip(), direction)
    folder = store.folder(p['id'])
    total = 0
    try:
        with (folder / 'source.mp4').open('wb') as f:
            while chunk := await video.read(1024 * 1024):
                total += len(chunk)
                if total > MAX_UPLOAD:
                    raise ValueError('O vídeo ultrapassou 500 MB.')
                f.write(chunk)
        ffprobe = shutil.which('ffprobe') or str(Path(os.environ.get('LOCALAPPDATA', '')) / 'Microsoft/WinGet/Links/ffprobe.exe')
        result = await asyncio.to_thread(subprocess.run,
            [ffprobe, '-v', 'error', '-show_format', '-show_streams', '-of', 'json', str(folder / 'source.mp4')],
            capture_output=True, text=True, timeout=30)
        info = json.loads(result.stdout or '{}')
        if result.returncode or not any(s.get('codec_type') == 'video' for s in info.get('streams', [])):
            raise ValueError('O arquivo enviado não contém vídeo legível.')
        duration = float(info.get('format', {}).get('duration', 0))
        if not 0 < duration <= 180:
            raise ValueError('Nesta versão, envie vídeos de até 3 minutos.')
        sources = await asyncio.to_thread(snapshot, folder / 'sources.md')
        store.change(p['id'], sources=sources, duration=duration, original_name=video.filename,
                     status='uploaded')
        store.event(p['id'], 'Vídeo recebido. Inicie a extração /watch.')
    except Exception as exc:
        store.change(p['id'], status='upload_error', error=str(exc))
        raise
    finally:
        await video.close()
    return store.get(p['id'])


def _normalize_anchor(raw):
    try:
        with Image.open(io.BytesIO(raw)) as im:
            if im.width * im.height > 40_000_000:
                raise ValueError('Âncora muito grande: máximo 40 megapixels.')
            return ImageOps.exif_transpose(im).convert('RGB')
    except ValueError:
        raise
    except Exception:
        raise ValueError('Âncora inválida. Use PNG, JPEG ou WebP.') from None


@app.post('/api/projects/{pid}/avatars')
async def add_avatars(pid: str, files: list[UploadFile] = File(...)):
    with store.LOCK:
        p = store.get(pid)
        if p['status'] not in ('imageset_ready',) or p.get('busy'):
            raise ValueError('Suba as âncoras depois que o conjunto de imagens estiver pronto.')
        if browser_queue.has_jobs(pid):
            raise ValueError('A fila já foi preparada. Pause e limpe a fila para trocar os avatares.')
    if not 1 <= len(files) <= 8:
        raise ValueError('Envie de 1 a 8 arquivos .jpeg de avatar.')
    added = []
    for upload in files:
        raw = await upload.read(20 * 1024 * 1024 + 1)
        await upload.close()
        if len(raw) > 20 * 1024 * 1024:
            raise ValueError('Cada âncora tem no máximo 20 MB.')
        normalized = _normalize_anchor(raw)
        aid = uuid.uuid4().hex[:8]
        folder = store.folder(pid) / 'avatars'
        folder.mkdir(exist_ok=True)
        normalized.save(folder / f'{aid}.png')
        name = re.sub(r'\.[a-zA-Z0-9]+$', '', upload.filename or '').strip() or f'Avatar {aid}'
        added.append({'id': aid, 'name': name[:80], 'file': f'avatars/{aid}.png'})
    with store.LOCK:
        p = store.get(pid)
        p.setdefault('avatars', []).extend(added)
        store.save(p)
        store.event(pid, f'{len(added)} avatar(es) adicionado(s): {", ".join(a["name"] for a in added)}.')
    return store.get(pid)


@app.delete('/api/projects/{pid}/avatars/{aid}')
def remove_avatar(pid: str, aid: str):
    with store.LOCK:
        p = store.get(pid)
        if browser_queue.has_jobs(pid):
            raise ValueError('A fila já foi preparada. Pause e limpe a fila para remover avatares.')
        p['avatars'] = [a for a in p.get('avatars', []) if a['id'] != aid]
        store.save(p)
    path = store.folder(pid) / 'avatars' / f'{aid}.png'
    if path.is_file():
        path.unlink()
    return store.get(pid)


@app.post('/api/projects/{pid}/queue')
def prepare_queue(pid: str, data: BrowserQueue | None = None):
    with store.LOCK:
        p = store.get(pid)
        if p['status'] != 'imageset_ready':
            raise ValueError('Monte o conjunto de imagens antes de preparar a fila.')
        if not p.get('avatars'):
            raise ValueError('Suba ao menos uma âncora de avatar.')
    limit = data.limit if data else None
    return browser_queue.enqueue([pid], limit)


@app.post('/api/projects/{pid}/queue/clear')
def clear_queue(pid: str):
    store.get(pid)
    return browser_queue.clear(pid)


ALLOWED = {'extract': ['uploaded'], 'analyze': ['extracted'],
           'script': ['analysis_approved', 'script_ready', 'script_approved'],
           'hooks': ['script_approved'], 'imageset': ['hooks_selected']}


def worker(pid, action):
    try:
        engine.ACTIONS[action](pid)
    except Exception as exc:
        message = provider.safe_error(exc)
        store.change(pid, error=message)
        store.event(pid, 'Atenção: ' + message)
    finally:
        store.change(pid, busy=False)


@app.post('/api/projects/{pid}/run/{action}')
def run(pid: str, action: str):
    with store.LOCK:
        p = store.get(pid)
        if action not in ALLOWED or p['status'] not in ALLOWED[action]:
            raise ValueError('Etapa indisponível. Conclua e aprove a etapa anterior.')
        if p['busy']:
            raise HTTPException(409, 'Este projeto já possui uma etapa em andamento.')
        if action != 'extract':
            provider.require_think_key()
        store.change(pid, busy=True, error=None, last_action=action, pause_requested=False)
        POOL.submit(worker, pid, action)
    return {'started': action}


class Approval(BaseModel):
    clarification: str = Field(default='', max_length=5000)
    copy_note: str = Field(default='', max_length=5000)
    script: dict | None = None
    selected: list[str] = Field(default_factory=list, max_length=5)


@app.post('/api/projects/{pid}/approve/{stage}')
def approve(pid: str, stage: str, data: Approval):
    with store.LOCK:
        p = store.get(pid)
        if p['busy']:
            raise ValueError('Aguarde a etapa em andamento.')
        if stage == 'analysis' and p['status'] == 'analysis_ready':
            if p['analysis']['ambiguity'] and not data.clarification.strip():
                raise ValueError('Responda à dúvida sobre o hook/reveal antes de aprovar.')
            store.change(pid, clarification=data.clarification, status='analysis_approved', error=None)
        elif stage == 'script' and p['status'] in ('script_ready', 'script_approved'):
            value = validate_script(data.script or p['script'])
            store.change(pid, script=value, script_approved_at=store.now(), status='script_approved',
                         copy_note='', error=None)
            store.write_json(store.folder(pid) / 'ROTEIRO.json', value)
        elif stage == 'hooks' and p['status'] in ('hooks_ready', 'hooks_selected'):
            ids = {h['id'] for h in p['hooks']}
            if not data.selected or len(set(data.selected)) != len(data.selected) or any(i not in ids for i in data.selected):
                raise ValueError('Selecione de 1 a 5 ganchos diferentes.')
            store.change(pid, selected=data.selected, status='hooks_selected', error=None)
        else:
            raise ValueError('Aprovação não disponível para esta etapa.')
        store.event(pid, f'Aprovação registrada: {stage}.')
    return store.get(pid)


@app.post('/api/projects/{pid}/adjust-copy')
def adjust_copy(pid: str, data: Approval):
    with store.LOCK:
        p = store.get(pid)
        if p['busy'] or p['status'] not in ('script_ready', 'script_approved'):
            raise ValueError('O roteiro precisa estar entregue para ajustar a copy.')
        if not data.copy_note.strip():
            raise ValueError('Descreva o ajuste desejado na copy.')
        provider.require_think_key()
        store.change(pid, copy_note=data.copy_note.strip(), busy=True, error=None,
                     last_action='script', pause_requested=False)
        POOL.submit(worker, pid, 'script')
    return {'started': 'script'}


class MoreHooks(BaseModel):
    keep: list[str] = Field(default_factory=list, max_length=5)


@app.post('/api/projects/{pid}/hooks/more')
def more_hooks(pid: str, data: MoreHooks):
    with store.LOCK:
        p = store.get(pid)
        if p['busy'] or p['status'] not in ('hooks_ready', 'hooks_selected'):
            raise ValueError('Os ganchos precisam estar na tela de escolha.')
        ids = {h['id'] for h in p.get('hooks', [])}
        if any(k not in ids for k in data.keep):
            raise ValueError('Gancho a manter não existe mais na lista.')
        provider.require_think_key()
        store.change(pid, hooks_keep=list(dict.fromkeys(data.keep)), busy=True, error=None,
                     last_action='more_hooks', pause_requested=False)
        POOL.submit(worker, pid, 'more_hooks')
    return {'started': 'more_hooks'}


class CallLimits(BaseModel):
    text: int = Field(ge=1, le=1000)


@app.post('/api/projects/{pid}/limits')
def update_limits(pid: str, data: CallLimits):
    with store.LOCK:
        p = store.get(pid)
        if p['busy']:
            raise ValueError('Pause e aguarde a etapa antes de alterar os limites.')
        store.change(pid, call_limits=data.model_dump())
        store.event(pid, f'Limite registrado: {data.text} chamadas de texto no projeto inteiro.')
    return store.get(pid)


@app.post('/api/projects/{pid}/pause')
def pause(pid: str):
    store.change(pid, pause_requested=True)
    store.event(pid, 'Pausa solicitada. A chamada já enviada pode concluir; nenhuma nova chamada será iniciada.')
    return store.get(pid)


@app.get('/api/projects/{pid}/files/{relative:path}')
def files(pid: str, relative: str):
    if relative == 'sources.md':
        raise ValueError('O snapshot de instruções fica disponível apenas na pasta local.')
    path = store.artifact(pid, relative)
    if path.suffix.lower() not in ['.png', '.mp4', '.txt', '.json', '.md', '.log', '.zip']:
        raise ValueError('Tipo de arquivo indisponível.')
    return FileResponse(path, filename=path.name if path.suffix in ['.zip', '.txt', '.json', '.md', '.log'] else None)
