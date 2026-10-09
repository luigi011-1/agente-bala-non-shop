"""Coleta de páginas renderizadas; navegador não concede autenticação nem ignora robots."""
import asyncio
from datetime import datetime, timedelta, timezone
from pathlib import Path
import re
import shutil
from urllib.parse import urlsplit
from uuid import uuid4


async def crawl_browser(urls, *, max_pages, max_seconds, concurrency,
                        allow_local_fixtures=False, browser_profile=None):
    from crawlee import ConcurrencySettings
    from crawlee.crawlers import PlaywrightCrawler
    from crawlee.request_loaders import ThrottlingRequestManager
    from crawlee.storage_clients import MemoryStorageClient
    from crawlee.storages import RequestQueue
    from operacao.mineracao import normalize_url, extract_page

    # Mesmo escopo antes de qualquer rede, inclusive quando chamada fora do CLI.
    urls = list(dict.fromkeys(normalize_url(u, allow_local_fixtures=allow_local_fixtures) for u in urls))
    pages, errors = {}, []
    scheduled = set(urls[:max_pages])
    truncated = len(urls) > max_pages
    timed_out = False
    profile = None
    if browser_profile:
        profile = Path(browser_profile).expanduser().resolve()
        dedicated = Path(__file__).resolve().parents[1] / '.cache-operacao/browser'
        if not profile.is_relative_to(dedicated.resolve()):
            raise ValueError('Use um perfil dedicado em .cache-operacao/browser/. O coletor não usa o perfil pessoal do Chrome.')
        profile.mkdir(parents=True, exist_ok=True)
    storage = MemoryStorageClient()
    run_id = 'browser-' + uuid4().hex
    queue = await RequestQueue.open(name=run_id, storage_client=storage)

    async def domain_queue(*, alias, storage_client, configuration):
        return await RequestQueue.open(name=run_id + '-' + re.sub(r'[^a-z0-9-]', '-', alias.lower()),
                                       storage_client=storage_client, configuration=configuration)

    manager = ThrottlingRequestManager(queue, domains=sorted({urlsplit(u).hostname for u in urls}), request_manager_opener=domain_queue)
    chrome = Path('/Applications/Google Chrome.app').is_dir() or shutil.which('google-chrome') or shutil.which('google-chrome-stable')
    crawler = PlaywrightCrawler(
        browser_type='chrome' if chrome else 'chromium', user_data_dir=profile,
        headless=True, fingerprint_generator=None, storage_client=storage, request_manager=manager,
        use_session_pool=False, retry_on_blocked=False, max_session_rotations=0,
        max_request_retries=0, max_requests_per_crawl=max_pages, respect_robots_txt_file=True,
        concurrency_settings=ConcurrencySettings(min_concurrency=1, max_concurrency=concurrency, desired_concurrency=concurrency),
        navigation_timeout=timedelta(seconds=min(20, max_seconds)),
        request_handler_timeout=timedelta(seconds=20), configure_logging=False,
        goto_options={'wait_until': 'domcontentloaded'},
    )

    @crawler.pre_navigation_hook
    async def restrict_navigation(context):
        async def guard(route):
            request = route.request
            if request.is_navigation_request():
                try:
                    normalize_url(request.url, allow_local_fixtures=allow_local_fixtures)
                except ValueError:
                    errors.append({'url': context.request.url, 'reason': 'OUT_OF_SCOPE_NAVIGATION', 'detail': request.url[:300]})
                    await route.abort()
                    return
            if request.resource_type in {'media', 'image', 'font'}:
                await route.abort()
                return
            await route.continue_()
        await context.page.route('**/*', guard)

    @crawler.router.default_handler
    async def handler(context):
        nonlocal truncated
        url = normalize_url(context.page.url, allow_local_fixtures=allow_local_fixtures)
        # Pequena janela limitada para metadados inseridos por JavaScript.
        await context.page.wait_for_timeout(500)
        page = extract_page(await context.page.content(), url, datetime.now(timezone.utc).isoformat(), allow_local_fixtures=allow_local_fixtures)
        page['rendered_with_browser'] = True
        pages[url] = page
        if page['blocked']:
            errors.append({'url': url, 'reason': 'LOGIN_OR_CHALLENGE'})
            return
        for link in ([page['profile_url']] if page['profile_url'] else []) + page['links']:
            if link in scheduled:
                continue
            if len(scheduled) >= max_pages:
                truncated = True
                continue
            scheduled.add(link)
            await context.add_requests([link])

    @crawler.failed_request_handler
    async def failed(context, error):
        errors.append({'url': context.request.url, 'reason': type(error).__name__, 'detail': str(error)[:400]})

    try:
        await asyncio.wait_for(crawler.run(urls[:max_pages]), timeout=max_seconds)
    except asyncio.TimeoutError:
        timed_out = True
        errors.append({'url': None, 'reason': 'TIME_LIMIT'})
    except Exception as error:
        errors.append({'url': None, 'reason': type(error).__name__, 'detail': str(error)[:400]})
    timed_out = timed_out or any('Timeout' in item['reason'] for item in errors)
    for url in sorted(scheduled - set(pages) - {e['url'] for e in errors if e.get('url')}):
        errors.append({'url': url, 'reason': 'NOT_FETCHED_OR_ROBOTS_DENIED'})
    return pages, errors, truncated or timed_out, sorted(scheduled)
