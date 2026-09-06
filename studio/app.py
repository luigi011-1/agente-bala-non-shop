import asyncio
import hmac
import io
import json
import os
import secrets
import shutil
import subprocess
from concurrent.futures import ThreadPoolExecutor
from contextlib import asynccontextmanager
from pathlib import Path
from urllib.parse import urlparse

from fastapi import FastAPI, File, Form, HTTPException, Request, UploadFile
from fastapi.responses import FileResponse, HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.exceptions import RequestValidationError
from PIL import Image
from pydantic import BaseModel, Field

from . import console, engine, provider, batches, browser_queue, storage as store
from .rules import ROOT, snapshot, validate_script

TOKEN = secrets.token_urlsafe(32)
POOL = ThreadPoolExecutor(max_workers=2)
STATIC = Path(__file__).parent / 'static'
MAX_UPLOAD = 500 * 1024 * 1024
AVATARS = {
    'shelby': ('Shelby Turner', ROOT / 'producao/_ancoras/ShelbyTurner.us .jpeg'),
    'kris': ('Kris Walker', ROOT / 'producao/_ancoras/Kris.Walker_us .jpeg'),
    'robin': ('Robin Matthews', ROOT / 'producao/_ancoras/Robin.Matthewsus .jpeg'),
    'casey': ('Casey Harrisson', ROOT / 'producao/_ancoras/casey.harrisson_us .jpeg'),
}


@asynccontextmanager
async def lifespan(app):
    provider.load_preferences()
    browser_queue.recover()
    for p in store.all_projects():
        if p.get('busy'):
            store.change(p['id'], busy=False, queue_state='attention', error='Servidor reiniciado. Retome o lote/etapa; resultados anteriores preservados.')
    yield


app = FastAPI(title='Auraly Studio', lifespan=lifespan)


@app.middleware('http')
async def local_boundary(request: Request, call_next):
    host = request.headers.get('host', '').split(':')[0]
    if host not in ['127.0.0.1', 'localhost', 'testserver']:
        return JSONResponse({'detail': 'Somente acesso local.'}, status_code=403)
    origin = request.headers.get('origin')
    bridge = request.url.path.startswith('/api/browser/agent/')
    extension = bool(origin and __import__('re').fullmatch(r'chrome-extension://[a-p]{32}', origin))
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


@app.get('/console', response_class=HTMLResponse)
def console_page():
    return (STATIC / 'console.html').read_text(encoding='utf-8').replace('__TOKEN__', TOKEN)


@app.get('/browser', response_class=HTMLResponse)
def browser_page():
    return (STATIC / 'browser.html').read_text(encoding='utf-8').replace('__TOKEN__', TOKEN)


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


@app.post('/api/browser/jobs/{jid}/review')
def browser_review(jid: str, data: BrowserReview):
    return browser_queue.review(jid, data.decision, data.comment)


@app.get('/api/browser/jobs/{jid}/result')
def browser_result(jid: str):
    return FileResponse(browser_queue.result_file(jid))


@app.post('/api/browser/projects/{pid}/export')
def browser_export(pid: str):
    path = browser_queue.export_package(pid)
    return FileResponse(path, media_type='application/zip', filename=f'auraly-{pid[:8]}-flow.zip')


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


@app.get('/api/browser/agent/state')
def browser_agent_state():
    return browser_queue.heartbeat()


@app.post('/api/browser/agent/claim')
def browser_claim():
    return {'job': browser_queue.claim()}


@app.post('/api/browser/agent/jobs/{jid}')
def browser_update(jid: str, data: BrowserUpdate):
    return browser_queue.update(jid, **data.model_dump())


@app.get('/api/browser/agent/jobs/{jid}/anchor')
def browser_anchor(jid: str):
    return FileResponse(browser_queue.anchor(jid), media_type='image/png')


@app.post('/api/browser/agent/jobs/{jid}/image')
async def browser_image(jid: str, request: Request):
    raw = bytearray()
    async for chunk in request.stream():
        raw.extend(chunk)
        if len(raw) > 35 * 1024 * 1024:
            raise ValueError('Imagem acima de 35 MB.')
    return await asyncio.to_thread(browser_queue.receive, jid, bytes(raw))


class ConsoleQueue(BaseModel):
    ids: list[str] = Field(min_length=1, max_length=8)


class ConsoleStep(BaseModel):
    step: dict


class ClipboardFile(BaseModel):
    path: str


@app.post('/api/console/queue')
def console_queue(data: ConsoleQueue):
    return {'steps': console.queue(data.ids)}


@app.post('/api/console/clipboard')
def console_clipboard(data: ClipboardFile):
    root = str(store.DATA.resolve())
    target = Path(data.path).resolve()
    if not str(target).startswith(root):
        raise ValueError('Caminho fora do diretório do projeto.')
    return {'copied': console.copy_file_to_clipboard(target)}


@app.post('/api/console/watch')
def console_watch(data: ConsoleStep):
    console.start_watch(data.step)
    return console.watch_state()


@app.post('/api/console/watch/stop')
def console_watch_stop():
    console.stop_watch()
    return console.watch_state()


@app.get('/api/console/watch')
def console_watch_state():
    return console.watch_state()


app.mount('/static', StaticFiles(directory=STATIC), name='static')


@app.get('/api/config')
def config():
    ff = shutil.which('ffmpeg') or str(Path(os.environ.get('LOCALAPPDATA', '')) / 'Microsoft/WinGet/Links/ffmpeg.exe')
    return {**provider.settings(), 'ffmpeg': Path(ff).is_file(),
            'avatars': [{'id': key, 'name': v[0]} for key, v in AVATARS.items() if v[1].is_file()],
            'data_dir': str(store.DATA), 'version': '0.6.0'}


class Settings(BaseModel):
    text_provider: str | None = Field(default=None, pattern='^(auto|openai|gemini|kie)$')
    allow_temp_upload: bool | None = None
    api_key: str | None = Field(default=None, max_length=500)
    kie_key: str | None = Field(default=None, max_length=500)
    gemini_key: str | None = Field(default=None, max_length=500)
    text_model: str = Field(default=provider.DEFAULT_MODEL, pattern=r'^[a-zA-Z0-9._-]+$', max_length=80)
    reasoning_effort: str = Field(default='medium', pattern=r'^(low|medium|high|xhigh|max)$')


@app.post('/api/config')
def set_config(data: Settings):
    if any(p.get('busy') for p in store.all_projects()):
        raise ValueError('Aguarde as etapas em andamento antes de trocar a conexão.')
    provider.configure(data.api_key, data.text_model, data.reasoning_effort,
                       kie_key=data.kie_key, gemini_key=data.gemini_key,
                       allow_temp_upload=data.allow_temp_upload, text_provider=data.text_provider)
    provider.save_preferences()
    return provider.settings()


@app.post('/api/config/verify')
def verify_config():
    return provider.verify_access()


@app.get('/api/projects')
def projects():
    return [{k: p.get(k) for k in ['id', 'title', 'avatar', 'status', 'busy', 'updated', 'progress', 'error', 'batch_source', 'batch_id', 'queue_state', 'active_text_provider']}
            for p in store.all_projects()]


@app.get('/api/projects/{pid}')
def project(pid: str):
    return store.get(pid)


class BatchCreate(BaseModel):
    avatars: list[str] = Field(min_length=1, max_length=4)
    variations: int = Field(default=3, ge=1, le=5)
    request_id: str = Field(pattern=r'^[a-f0-9-]{36}$')


class BatchRun(BaseModel):
    ids: list[str] = Field(min_length=1, max_length=4)
    produce: bool = False


@app.post('/api/projects/{pid}/batch')
def create_batch(pid: str, data: BatchCreate):
    return {'ids': batches.create(pid, data.avatars, AVATARS, data.variations, data.request_id)}


@app.post('/api/batches/run')
def run_batch(data: BatchRun):
    return {'queued': batches.enqueue(data.ids, POOL, data.produce)}


@app.post('/api/batches/pause')
def pause_batch(data: BatchRun):
    for pid in data.ids:
        pause(pid)
    return {'paused': data.ids}


@app.post('/api/projects')
async def upload(title: str = Form(...), avatar: str = Form('shelby'),
                 avatar_name: str = Form('Avatar personalizado'), direction: str = Form(''),
                 video: UploadFile = File(...), anchor: UploadFile | None = File(None)):
    # Browsers include an empty file field when an optional upload is untouched.
    if anchor is not None and not anchor.filename:
        await anchor.close()
        anchor = None
    if not (video.filename or '').lower().endswith('.mp4'):
        raise ValueError('Envie um arquivo .mp4.')
    if not title.strip() or len(title) > 120 or len(direction) > 5000 or len(avatar_name) > 100:
        raise ValueError('Título ou briefing inválido.')
    if not anchor and avatar not in AVATARS:
        raise ValueError('Selecione um avatar cadastrado ou envie uma âncora.')
    if anchor:
        raw = await anchor.read(20 * 1024 * 1024 + 1)
        if len(raw) > 20 * 1024 * 1024:
            raise ValueError('Âncora: máximo 20 MB.')
        avatar_label = avatar_name.strip() or 'Avatar personalizado'
    else:
        avatar_label, anchor_path = AVATARS[avatar]
        raw = anchor_path.read_bytes()
    try:
        with Image.open(io.BytesIO(raw)) as im:
            if im.width * im.height > 40_000_000:
                raise ValueError('Âncora muito grande: máximo 40 megapixels.')
            from PIL import ImageOps
            normalized = ImageOps.exif_transpose(im).convert('RGB')
    except Exception:
        raise ValueError('Âncora inválida. Use PNG, JPEG ou WebP.') from None
    p = store.create(title.strip(), avatar_label, direction)
    folder = store.folder(p['id'])
    total = 0
    try:
        with (folder / 'source.mp4').open('wb') as f:
            while chunk := await video.read(1024 * 1024):
                total += len(chunk)
                if total > MAX_UPLOAD:
                    raise ValueError('O vídeo ultrapassou 500 MB.')
                f.write(chunk)
        normalized.save(folder / 'anchor.png')
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
        store.event(p['id'], 'Vídeo e âncora recebidos. Inicie a extração /watch.')
    except Exception as exc:
        store.change(p['id'], status='upload_error', error=str(exc))
        raise
    finally:
        await video.close()
        if anchor:
            await anchor.close()
    return store.get(p['id'])


ALLOWED = {'extract': ['uploaded'], 'analyze': ['extracted'], 'script': ['analysis_approved'],
           'hooks': ['script_approved'], 'plan': ['hooks_selected'],
           'generate': ['plan_ready', 'generating', 'complete']}


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
        if action == 'generate':
            browser_queue.api_generation_allowed(pid)
            provider.require_image_key()
        elif action != 'extract':
            provider.require_think_key()
        if action == 'generate':
            store.change(pid, status='generating', max_attempts=p.get('max_attempts', 2))
        store.change(pid, busy=True, error=None, last_action=action, pause_requested=False)
        POOL.submit(worker, pid, action)
    return {'started': action}


class Approval(BaseModel):
    clarification: str = Field(default='', max_length=5000)
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
        elif stage == 'script' and p['status'] == 'script_ready':
            value = validate_script(data.script or p['script'])
            store.change(pid, script=value, script_approved_at=store.now(), status='script_approved', error=None)
            store.write_json(store.folder(pid) / 'ROTEIRO.json', value)
        elif stage == 'hooks' and p['status'] == 'hooks_ready':
            ids = {h['id'] for h in p['hooks']}
            if not data.selected or len(set(data.selected)) != len(data.selected) or any(i not in ids for i in data.selected):
                raise ValueError('Selecione de 1 a 5 ganchos diferentes.')
            store.change(pid, selected=data.selected, status='hooks_selected', error=None)
        else:
            raise ValueError('Aprovação não disponível para esta etapa.')
        store.event(pid, f'Aprovação registrada: {stage}.')
    return store.get(pid)


class AssetReview(BaseModel):
    decision: str = Field(pattern='^(approve|retry)$')
    correction: str = Field(default='', max_length=2000)


@app.post('/api/projects/{pid}/assets/{fid}/review')
def review_asset(pid: str, fid: str, data: AssetReview):
    with store.LOCK:
        p = store.get(pid)
        if p['busy'] or fid not in p['assets']:
            raise ValueError('Imagem indisponível para revisão.')
        asset = p['assets'][fid]
        if asset['status'] == 'approved':
            raise ValueError('Imagem já aprovada. Crie uma nova produção para alterar dependências aprovadas.')
        if data.decision == 'approve':
            store.artifact(pid, asset.get('file', ''))
            asset.update(status='approved', human_approved_at=store.now())
        else:
            asset['status'] = 'rejected'
            if data.correction.strip():
                asset['correction'] = data.correction.strip()
                asset.setdefault('feedback', []).append({'text': data.correction.strip(), 'time': store.now()})
            limits = p.setdefault('retry_limits', {})
            limits[fid] = max(limits.get(fid, p.get('max_attempts', 2)), len(asset.get('attempts', [])) + 1)
        p.update(error=None, status='generating')
        store.save(p)
        store.event(pid, f'{fid}: {"aprovação manual" if data.decision == "approve" else "nova tentativa autorizada"}.')
    return p


class CallLimits(BaseModel):
    text: int = Field(ge=1, le=1000)
    image: int = Field(ge=1, le=100)


@app.post('/api/projects/{pid}/limits')
def update_limits(pid: str, data: CallLimits):
    with store.LOCK:
        p = store.get(pid)
        if p['busy']:
            raise ValueError('Pause e aguarde a etapa antes de alterar os limites.')
        store.change(pid, call_limits=data.model_dump())
        store.event(pid, f'Limites registrados: {data.text} chamadas de texto e {data.image} de imagem, no projeto inteiro.')
    return store.get(pid)


@app.post('/api/projects/{pid}/pause')
def pause(pid: str):
    store.change(pid, pause_requested=True)
    store.event(pid, 'Pausa solicitada. A chamada já enviada pode concluir e ser cobrada; nenhuma nova chamada será iniciada.')
    return store.get(pid)


@app.get('/api/projects/{pid}/files/{relative:path}')
def files(pid: str, relative: str):
    if relative == 'sources.md':
        raise ValueError('O snapshot de instruções fica disponível apenas na pasta local.')
    path = store.artifact(pid, relative)
    if path.suffix.lower() not in ['.png', '.mp4', '.txt', '.json', '.md', '.log', '.zip']:
        raise ValueError('Tipo de arquivo indisponível.')
    return FileResponse(path, filename=path.name if path.suffix in ['.zip', '.txt', '.json', '.md', '.log'] else None)
