"""Mineração limitada de páginas públicas Meta, com provas e lacunas explícitas.

Não autentica, não contorna bloqueios e não automatiza Google Flow. Seeds são
descobertas por nicho pelo agente de pesquisa; Crawlee coleta com navegador ou
HTTP auditável. A janela padrão inclui hoje e os seis dias anteriores em Nova
York; só inglês inspecionado e visualizações confirmadas entram como provas.
"""
from __future__ import annotations

import argparse
import asyncio
from datetime import date, datetime, timedelta, timezone
import importlib.metadata
import json
import logging
from pathlib import Path
import re
import sys
from typing import Any
from urllib.parse import parse_qs, urlencode, urljoin, urlsplit, urlunsplit
from uuid import uuid4
from zoneinfo import ZoneInfo

from operacao.nichos import mining_defaults, resolve_niche

ANGLES = ("sea-moss", "fitwell", "auraly", "body-hacks")
FIELDS = ("posted_at", "views", "profile_created_at", "profile_country", "profile_ai_only", "niche_match", "language")
META_HOSTS = {"instagram.com", "www.instagram.com", "m.instagram.com", "facebook.com", "www.facebook.com", "m.facebook.com", "web.facebook.com"}


def normalize_url(url: str, *, allow_local_fixtures: bool = False) -> str:
    """Restrict hosts exactly, remove tracking; preserve Facebook video identity."""
    parts = urlsplit(url.strip())
    host = (parts.hostname or "").lower()
    local = allow_local_fixtures and host in {"127.0.0.1", "localhost", "::1"}
    if parts.username or parts.password or parts.fragment and not host:
        raise ValueError("URL inválida")
    if local:
        if parts.scheme != "http":
            raise ValueError("Fixture local exige HTTP explícito")
        return urlunsplit(("http", parts.netloc.lower(), parts.path or "/", parts.query, ""))
    if host not in META_HOSTS or parts.scheme != "https" or parts.port not in {None, 443}:
        raise ValueError("Somente URLs HTTPS oficiais de instagram.com e facebook.com")
    host = "www.instagram.com" if host.endswith("instagram.com") else "www.facebook.com"
    path = re.sub(r"/+", "/", parts.path) or "/"
    query = parse_qs(parts.query)
    kept = {k: query[k][0] for k in ("v", "id", "story_fbid") if k in query}
    if host.endswith("instagram.com"):
        kept = {}
    return urlunsplit(("https", host, path.rstrip("/") + "/", urlencode(kept), ""))


def is_video_url(url: str) -> bool:
    parts = urlsplit(url)
    return bool(re.match(r"^/(?:reel|reels|p|tv)/[^/]+/?$", parts.path)
                or "/videos/" in parts.path
                or (parts.path.rstrip("/") == "/watch" and parse_qs(parts.query).get("v")))


def platform(url: str) -> str:
    host = urlsplit(url).hostname or ""
    return "instagram" if host.endswith("instagram.com") else "facebook" if host.endswith("facebook.com") else "fixture"


def timestamp(value: Any) -> datetime | None:
    try:
        if isinstance(value, (int, float)) and not isinstance(value, bool):
            return datetime.fromtimestamp(value, timezone.utc)
        parsed = datetime.fromisoformat(str(value).strip().replace("Z", "+00:00"))
        # A calendar date alone is kept for profile creation, never silently used
        # as a video publication timestamp across time zones.
        return parsed if parsed.tzinfo else parsed.replace(tzinfo=timezone.utc)
    except (ValueError, TypeError, OverflowError, OSError):
        return None


def exact_count(value: Any) -> int | None:
    if isinstance(value, bool):
        return None
    if isinstance(value, int) and value >= 0:
        return value
    if isinstance(value, str) and re.fullmatch(r"\d+", value):
        return int(value)
    return None


def evidence(value: Any, source_url: str, observed_at: str, method: str, *, excerpt: str = "") -> dict:
    return {"value": value, "source_url": source_url, "observed_at": observed_at, "method": method, "excerpt": excerpt[:600]}


def _objects(value: Any):
    if isinstance(value, dict):
        yield value
        for child in value.values():
            yield from _objects(child)
    elif isinstance(value, list):
        for child in value:
            yield from _objects(child)


def extract_page(html: str, url: str, observed_at: str, *, allow_local_fixtures: bool = False) -> dict:
    """Read documented JSON-LD and public embedded video metadata conservatively."""
    from bs4 import BeautifulSoup

    soup = BeautifulSoup(html, "html.parser")
    meta = {tag.get("property", tag.get("name", "")): tag.get("content", "") for tag in soup.select("meta[content]")}
    title = meta.get("og:title") or (soup.title.get_text(" ", strip=True) if soup.title else "")
    visible = soup.get_text(" ", strip=True)
    blocked = any(token in title.lower() for token in ("log in", "login", "checkpoint", "captcha", "access denied"))
    if soup.select('input[type="password"], form[action*="login"], form[action*="checkpoint"]'):
        blocked = True
    if any(token in visible.lower() for token in ("you must log in", "log in to continue", "verify you are human", "confirm you're human", "temporarily blocked")):
        blocked = True
    result: dict[str, Any] = {"url": url, "title": title, "blocked": blocked, "evidence": {}, "profile_url": None, "links": []}
    for tag in soup.select("a[href]"):
        try:
            link = normalize_url(urljoin(url, tag["href"]), allow_local_fixtures=allow_local_fixtures)
            if is_video_url(link):
                result["links"].append(link)
        except ValueError:
            pass
    if blocked:
        return result

    def record(field: str, value: Any, method: str, excerpt: str = ""):
        if value is not None:
            result["evidence"].setdefault(field, []).append(evidence(value, url, observed_at, method, excerpt=excerpt))

    def valid_profile(value: Any) -> str | None:
        if not isinstance(value, str):
            return None
        try:
            normalized = normalize_url(urljoin(url, value), allow_local_fixtures=allow_local_fixtures)
            return None if is_video_url(normalized) else normalized
        except ValueError:
            return None

    objects = []
    root_objects = []
    for script in soup.select("script"):
        raw = script.string or script.get_text()
        if not raw.strip().startswith(("{", "[")):
            continue
        try:
            decoded = json.loads(raw)
            if isinstance(decoded, dict):
                root_objects.append(decoded)
            objects.extend(_objects(decoded))
        except (ValueError, TypeError):
            continue
    video_objects = [obj for obj in objects if obj.get("@type") == "VideoObject" or isinstance(obj.get("@type"), list) and "VideoObject" in obj["@type"]]
    canonical = meta.get("og:url") or (soup.select_one('link[rel="canonical"]').get("href") if soup.select_one('link[rel="canonical"]') else None)
    try:
        canonical_matches = bool(canonical and normalize_url(urljoin(url, canonical), allow_local_fixtures=allow_local_fixtures) == url)
    except ValueError:
        canonical_matches = False
    for obj in objects:
        types = obj.get("@type", [])
        types = [types] if isinstance(types, str) else types
        if "VideoObject" in types and is_video_url(url):
            declared_url = obj.get("url") or obj.get("mainEntityOfPage")
            if isinstance(declared_url, dict):
                declared_url = declared_url.get("@id") or declared_url.get("url")
            if isinstance(declared_url, str):
                try:
                    if normalize_url(declared_url, allow_local_fixtures=allow_local_fixtures) != url:
                        continue
                except ValueError:
                    continue
            elif not (len(video_objects) == 1 and any(obj is root for root in root_objects) and canonical_matches):
                # ItemList/recommendation JSON without an identity must never
                # lend its metrics, date or creator to the requested reel.
                continue
            record("media_type", "video", "jsonld", "Identity-matched VideoObject")
            record("posted_at", obj.get("uploadDate") or obj.get("datePublished"), "jsonld", "VideoObject.uploadDate/datePublished")
            interactions = obj.get("interactionStatistic", [])
            interactions = [interactions] if isinstance(interactions, dict) else interactions
            for item in interactions:
                kind = item.get("interactionType", "") if isinstance(item, dict) else ""
                kind = kind.get("@type", "") if isinstance(kind, dict) else kind
                if str(kind).rstrip("/").endswith("WatchAction"):
                    record("views", exact_count(item.get("userInteractionCount")), "jsonld", "VideoObject.interactionStatistic.WatchAction")
            author = obj.get("author") or obj.get("creator")
            if isinstance(author, dict):
                result["profile_url"] = valid_profile(author.get("url") or author.get("sameAs"))
        if any(item in types for item in ("Person", "Organization")) and not is_video_url(url):
            declared = valid_profile(obj.get("url") or obj.get("sameAs"))
            if declared != url:
                continue
            address = obj.get("address", {})
            country = address.get("addressCountry") if isinstance(address, dict) else None
            country = country.get("name") if isinstance(country, dict) else country
            record("profile_country", country, "jsonld", "Profile.address.addressCountry (declared location)")
            # foundingDate means account creation only when the page explicitly
            # identifies the entity as a SocialMediaAccount, not company age.
        # These fields occur in public Meta video state. Tie them to this reel's
        # shortcode or URL instead of grabbing an unrelated recommendation/ad.
        shortcode = urlsplit(url).path.rstrip("/").split("/")[-1]
        same_video = is_video_url(url) and (str(obj.get("shortcode", "")) == shortcode or obj.get("permalink_url") == url)
        if same_video:
            if obj.get("is_video") is True or obj.get("__typename") in {"GraphVideo", "XDTGraphVideo"}:
                record("media_type", "video", "public_video_state", "is_video/__typename")
            record("views", exact_count(obj.get("video_view_count", obj.get("video_play_count"))), "public_video_state", "video_view_count/video_play_count")
            record("posted_at", obj.get("taken_at_timestamp"), "public_video_state", "taken_at_timestamp")
            owner = obj.get("owner") or obj.get("user")
            if isinstance(owner, dict) and isinstance(owner.get("username"), str) and platform(url) == "instagram":
                username = owner["username"]
                if re.fullmatch(r"[A-Za-z0-9_.]+", username):
                    result["profile_url"] = valid_profile("https://www.instagram.com/" + username + "/")
        if "SocialMediaAccount" in types and not is_video_url(url):
            if valid_profile(obj.get("url")) == url:
                record("profile_created_at", obj.get("dateCreated"), "public_account_metadata", "SocialMediaAccount.dateCreated")
                record("profile_country", obj.get("location", {}).get("addressCountry") if isinstance(obj.get("location"), dict) else None, "public_account_metadata", "SocialMediaAccount.location.addressCountry")
    if is_video_url(url) and meta.get("video:release_date"):
        record("posted_at", meta["video:release_date"], "public_meta", "video:release_date")
    result["links"] = list(dict.fromkeys(result["links"]))
    result["insufficient_metadata"] = not result["evidence"]
    return result


def load_seeds(path: Path, *, allow_local_fixtures: bool = False) -> tuple[list[str], list[dict]]:
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, (dict, list)):
        raise ValueError("Seeds deve ser lista de URLs ou objeto com urls")
    urls, observations = (data, []) if isinstance(data, list) else (data.get("urls", []), data.get("observations", []))
    if not isinstance(urls, list) or not urls or len(urls) > 100:
        raise ValueError("Seeds exige de 1 a 100 URLs")
    if not all(isinstance(url, str) for url in urls) or not isinstance(observations, list) or len(observations) > 1000:
        raise ValueError("Formato inválido de seeds/observations")
    normalized = list(dict.fromkeys(normalize_url(url, allow_local_fixtures=allow_local_fixtures) for url in urls))
    checked = []
    for item in observations:
        if not isinstance(item, dict) or item.get("field") not in FIELDS or item.get("verified") is not True:
            raise ValueError("Observação exige field válido e verified=true")
        for key in ("subject_url", "source_url"):
            item[key] = normalize_url(item[key], allow_local_fixtures=allow_local_fixtures)
        if not isinstance(item.get("observed_at"), str) or not re.search(r"T.*(?:Z|[+-]\d\d:?\d\d)$", item["observed_at"]) or not timestamp(item["observed_at"]) or not isinstance(item.get("note"), str) or not item["note"].strip():
            raise ValueError("Observação exige horário e nota concreta")
        expected = {"profile_ai_only": ("visual_audit", "all_public_posts"), "niche_match": ("content_audit", "profile_content"), "language": ("content_audit", "video_content")}
        if item["field"] not in expected or ((item.get("method"), item.get("scope")) != expected[item["field"]] and not (item["field"] == "language" and (item.get("method"), item.get("scope")) == ("asr", "video_content"))):
            raise ValueError("Observações externas só complementam auditoria de conteúdo/nicho e avatar IA")
        if item["field"] != "language" and not isinstance(item.get("value"), bool):
            raise ValueError("Valor da auditoria deve ser booleano")
        if item["field"] == "language":
            if not isinstance(item.get("value"), str) or not re.fullmatch(r"[a-z]{2,3}(?:-[A-Za-z]{2})?", item["value"]) or not is_video_url(item["subject_url"]):
                raise ValueError("Idioma exige código de idioma e auditoria do vídeo específico")
        if item["field"] == "niche_match":
            if item.get("niche"):
                item["niche"] = resolve_niche(item["niche"])["slug"]
            elif item.get("angle") not in ANGLES:
                raise ValueError("Auditoria de nicho exige niche ou angle explícito")
        checked.append(item)
    return normalized, checked


def _criterion(items: list[dict], convert, predicate) -> dict:
    converted = []
    for item in items:
        value = convert(item.get("value"))
        if value is not None:
            converted.append((value, item))
    if not converted:
        return {"status": "unknown", "evidence": items}
    passes = [bool(predicate(value)) for value, _ in converted]
    if any(passes) and not all(passes):
        return {"status": "conflict", "evidence": items}
    return {"status": "confirmed" if all(passes) else "rejected", "evidence": items}


def classify_video(video: dict, profiles: dict[str, dict], observations: list[dict], filters: dict, now: datetime) -> dict:
    proof = {field: list(video.get("evidence", {}).get(field, [])) for field in FIELDS}
    profile_url = video.get("profile_url")
    profile_page = profiles.get(profile_url, {})
    if not profile_page.get("blocked"):
        for field in ("profile_created_at", "profile_country"):
            proof[field].extend(profile_page.get("evidence", {}).get(field, []))
    # Audit attestations remain distinguishable from fetched metadata, so an
    # independent reviewer can check the cited posts and the stated coverage.
    for item in observations:
        observed = timestamp(item["observed_at"])
        if item["subject_url"] in ({video["url"]} if item["field"] == "language" else {video["url"], profile_url}) and observed and timedelta(0) <= now.astimezone(timezone.utc) - observed <= timedelta(days=2):
            proof[item["field"]].append(evidence(item["value"], item["source_url"], item["observed_at"], item["method"], excerpt=item["note"]) | {"scope": item["scope"]} | ({"niche": item["niche"]} if item.get("niche") else {"angle": item["angle"]} if item.get("angle") else {}))
    tz = ZoneInfo(filters["timezone"])
    today = date.fromisoformat(filters["today"])
    earliest = today - timedelta(days=filters["lookback_days"] - 1)

    def post_stamp(value):
        # A date without an explicit zone/time is insufficient for the weekly window.
        if isinstance(value, str) and not re.search(r"T.*(?:Z|[+-]\d\d:?\d\d)$", value):
            return None
        return timestamp(value)

    criteria = {
        "posted_at": _criterion(proof["posted_at"], post_stamp, lambda value: earliest <= value.astimezone(tz).date() <= today and value <= now.astimezone(timezone.utc)),
        "views": _criterion(proof["views"], exact_count, lambda value: value > filters["min_views"]),
        "profile_created_at": _criterion(proof["profile_created_at"], timestamp, lambda value: timedelta(0) <= now.astimezone(timezone.utc) - value <= timedelta(days=filters["max_profile_age_days"])),
        "profile_country": _criterion(proof["profile_country"], lambda v: str(v).upper() if v else None, lambda value: value in {"US", "USA", "UNITED STATES", "UNITED STATES OF AMERICA"}),
        "profile_ai_only": _criterion(proof["profile_ai_only"], lambda v: v if isinstance(v, bool) else None, lambda v: v),
        "niche_match": _criterion(proof["niche_match"], lambda v: v if isinstance(v, bool) else None, lambda v: v),
        "language": _criterion(proof["language"], lambda v: v.split("-")[0].lower() if isinstance(v, str) else None, lambda v: v == filters.get("language", "en")),
    }
    media_evidence = list(video.get("evidence", {}).get("media_type", []))
    if re.match(r"^/(?:reel|reels|tv)/", urlsplit(video["url"]).path) or "/videos/" in urlsplit(video["url"]).path or urlsplit(video["url"]).path.rstrip("/") == "/watch":
        media_evidence.append(evidence("video", video["url"], now.isoformat(), "public_url", excerpt="Video route; /p alone does not prove video"))
    criteria["media_type"] = _criterion(media_evidence, lambda value: value if isinstance(value, str) else None, lambda value: value == "video")
    state = "rejected" if any(c["status"] == "rejected" for c in criteria.values()) else "approved" if all(c["status"] == "confirmed" for c in criteria.values()) else "candidate"
    if video.get("blocked"):
        state = "candidate"
    return {"url": video["url"], "platform": platform(video["url"]), "title": video.get("title", ""), "profile_url": profile_url,
            "status": state, "criteria": criteria, "missing": [field for field, c in criteria.items() if c["status"] in {"unknown", "conflict"}], "blocked": bool(video.get("blocked"))}


async def crawl_pages(urls: list[str], *, max_pages: int, max_seconds: float, concurrency: int, allow_local_fixtures: bool = False) -> tuple[dict[str, dict], list[dict], bool, list[str]]:
    from crawlee import ConcurrencySettings
    from crawlee.crawlers import BeautifulSoupCrawler, BeautifulSoupCrawlingContext
    from crawlee.http_clients import HttpxHttpClient
    from crawlee.request_loaders import ThrottlingRequestManager
    from crawlee.storage_clients import MemoryStorageClient
    from crawlee.storages import RequestQueue

    pages: dict[str, dict] = {}
    errors: list[dict] = []
    scheduled = set(urls[:max_pages])
    truncated = len(urls) > max_pages
    timed_out = False

    async def guard(request):
        # HTTPX invokes request hooks on every redirect hop, before sending it.
        normalize_url(str(request.url), allow_local_fixtures=allow_local_fixtures)

    client = HttpxHttpClient(event_hooks={"request": [guard]}, follow_redirects=True, trust_env=False, header_generator=None)
    storage = MemoryStorageClient()
    run_id = "mining-" + uuid4().hex
    queue = await RequestQueue.open(name=run_id, storage_client=storage)

    async def open_domain_queue(*, alias, storage_client, configuration):
        # A unique queue per run prevents an earlier crawl in the same Python
        # process from suppressing freshly collected URLs/updated metrics.
        return await RequestQueue.open(name=run_id + "-" + re.sub(r"[^a-z0-9-]", "-", alias.lower()), storage_client=storage_client, configuration=configuration)

    manager = ThrottlingRequestManager(queue, domains=sorted({urlsplit(url).hostname for url in urls}), request_manager_opener=open_domain_queue)
    crawler = BeautifulSoupCrawler(
        http_client=client, storage_client=storage, request_manager=manager,
        max_requests_per_crawl=max_pages, max_request_retries=0,
        max_session_rotations=0, use_session_pool=False, retry_on_blocked=False,
        respect_robots_txt_file=True,
        concurrency_settings=ConcurrencySettings(min_concurrency=1, max_concurrency=concurrency, desired_concurrency=concurrency),
        navigation_timeout=timedelta(seconds=min(20, max_seconds)),
        request_handler_timeout=timedelta(seconds=20), configure_logging=False,
    )

    @crawler.router.default_handler
    async def handler(context: BeautifulSoupCrawlingContext):
        nonlocal truncated
        url = normalize_url(context.request.loaded_url or context.request.url, allow_local_fixtures=allow_local_fixtures)
        observed_at = datetime.now(timezone.utc).isoformat()
        page = extract_page(str(context.soup), url, observed_at, allow_local_fixtures=allow_local_fixtures)
        pages[url] = page
        if page["blocked"]:
            errors.append({"url": url, "reason": "LOGIN_OR_CHALLENGE", "observed_at": observed_at})
            return
        for link in ([page["profile_url"]] if page["profile_url"] else []) + page["links"]:
            if link in scheduled:
                continue
            if len(scheduled) >= max_pages:
                truncated = True
                continue
            scheduled.add(link)
            await context.add_requests([link])

    @crawler.failed_request_handler
    async def failed(context, error):
        errors.append({"url": context.request.url, "reason": type(error).__name__, "detail": str(error)[:400], "observed_at": datetime.now(timezone.utc).isoformat()})

    try:
        await asyncio.wait_for(crawler.run(urls[:max_pages]), timeout=max_seconds)
    except asyncio.TimeoutError:
        timed_out = True
        errors.append({"url": None, "reason": "TIME_LIMIT", "detail": f"Limite de {max_seconds}s atingido"})
    except Exception as error:
        errors.append({"url": None, "reason": type(error).__name__, "detail": str(error)[:400]})
    finally:
        await client.cleanup()
    timed_out = timed_out or any("Timeout" in error["reason"] for error in errors)
    missing = sorted(scheduled - set(pages) - {e["url"] for e in errors if e.get("url")})
    for url in missing:
        errors.append({"url": url, "reason": "NOT_FETCHED_OR_ROBOTS_DENIED"})
    return pages, errors, bool(truncated or timed_out), sorted(scheduled)


def render_report(result: dict) -> str:
    def escape_label(value):
        return str(value).replace("\\", "\\\\").replace("[", "\\[").replace("]", "\\]").replace("<", "&lt;").replace(">", "&gt;").replace("\n", " ")

    text = [f"# Mineração — {result.get('niche', {}).get('label') or result.get('angle')}", "", f"Estado: **{result['status']}**. Coleta: {result['started_at']}.",
            f"Páginas: {result['counts']['pages']}; aprovados: {len(result['approved'])}; candidatos: {len(result['candidates'])}; rejeitados: {len(result['rejected'])}.",
            "", "Filtros: " + json.dumps(result["filters"], ensure_ascii=False) + ".", "",
            "Ranking por visualizações confirmadas entre os vídeos consultados; não representa os mais virais de toda a rede. Inglês exige inspeção do conteúdo do vídeo. EUA é a localização declarada do perfil, não uma inferência pelo idioma nem pela audiência. Avatar IA exige auditoria visual de todos os posts públicos; a bio sozinha não prova exclusividade."]
    for group, label in (("approved", "Aprovados com evidências"), ("candidates", "Candidatos com lacunas"), ("rejected", "Rejeitados pelos filtros")):
        text += ["", "## " + label, ""]
        if not result[group]:
            text.append("Nenhum.")
        for item in result[group]:
            text.append(f"- [{item['platform']} — {escape_label(item['title'] or 'vídeo')}]({item['url']})")
            if item["profile_url"]:
                text.append(f"  Perfil: [abrir]({item['profile_url']}).")
            if item["missing"]:
                text.append("  Sem confirmação: " + ", ".join(item["missing"]) + ".")
            for field, criterion in item["criteria"].items():
                for proof in criterion["evidence"]:
                    text.append(f"  {field}: {proof['value']} — [fonte]({proof['source_url']}), observada em {proof['observed_at']}; {proof['method']}.")
    if result["errors"]:
        text += ["", "## Bloqueios e cobertura incompleta", ""]
        text += [f"- {e.get('url') or 'execução'}: {e['reason']}. {e.get('detail', '')}" for e in result["errors"]]
    if result["limits_reached"]:
        text += ["", "O limite de páginas/tempo foi atingido; a pesquisa não cobre toda a rede."]
    return "\n".join(text) + "\n"


def defaults_for_angle(angle: str | None) -> dict:
    """Compatibility entrypoint: editorial defaults no longer depend on offer."""
    return mining_defaults()


def rank_videos(videos: list[dict]) -> list[dict]:
    def key(video):
        criterion = video['criteria']['views']
        values = [exact_count(proof.get('value')) for proof in criterion['evidence']]
        values = [value for value in values if value is not None]
        # Conflicting or rejected views are never presented as confirmed rank.
        confirmed = min(values) if values and criterion['status'] == 'confirmed' else None
        video['confirmed_views'] = confirmed
        return (confirmed is None, -(confirmed or 0), video['url'])
    return sorted(videos, key=key)


async def mine(args: argparse.Namespace) -> dict:
    urls, observations = load_seeds(args.seeds, allow_local_fixtures=args.allow_local_fixtures)
    now = datetime.now(timezone.utc)
    angle = getattr(args, "angle", None)
    niche = resolve_niche(getattr(args, "niche", None), angle=angle)
    filters = defaults_for_angle(angle)
    for name in ("min_views", "lookback_days", "max_profile_age_days", "timezone"):
        if getattr(args, name) is not None:
            filters[name] = getattr(args, name)
    filters["today"] = args.today or now.astimezone(ZoneInfo(filters["timezone"])).date().isoformat()
    reference_day = date.fromisoformat(filters["today"])
    filters["window_start"] = (reference_day - timedelta(days=filters["lookback_days"] - 1)).isoformat()
    filters["window_end"] = reference_day.isoformat()
    observations = [item for item in observations if item["field"] != "niche_match" or (item.get("niche") == niche["slug"] if item.get("niche") else bool(angle and item.get("angle") == angle and resolve_niche(angle=angle)["slug"] == niche["slug"]))]
    backend = getattr(args, "backend", "http")
    crawl_options = dict(max_pages=args.max_pages, max_seconds=args.max_seconds, concurrency=args.concurrency, allow_local_fixtures=args.allow_local_fixtures)
    if backend == "browser":
        from operacao.coleta_browser import crawl_browser
        pages, errors, limits, scheduled = await crawl_browser(urls, browser_profile=getattr(args, "browser_profile", None), **crawl_options)
    else:
        pages, errors, limits, scheduled = await crawl_pages(urls, **crawl_options)
    profiles = {url: page for url, page in pages.items() if not is_video_url(url)}
    videos = [page for url, page in pages.items() if is_video_url(url)]
    # Direct video seeds still appear in the report when the endpoint is blocked.
    videos.extend({"url": url, "blocked": True} for url in scheduled if is_video_url(url) and url not in pages)
    classified = [classify_video(video, profiles, observations, filters, now) for video in videos]
    approved = rank_videos([v for v in classified if v["status"] == "approved"])
    candidates = rank_videos([v for v in classified if v["status"] == "candidate"])
    rejected = [v for v in classified if v["status"] == "rejected"]
    # COMPLETE describes coverage of scheduled URLs and proof, never claims an
    # exhaustive Instagram/Facebook search. Unknown filters keep it PARTIAL.
    blocked = not pages or all(page.get("blocked") for page in pages.values())
    fatal = any(error.get("url") is None and error["reason"] != "TIME_LIMIT" for error in errors)
    status = "FAILED" if fatal else "BLOCKED" if blocked else "PARTIAL" if errors or limits or candidates or any(page.get("insufficient_metadata") for page in pages.values()) else "COMPLETE"
    return {"schema_version": 2, "angle": angle, "niche": niche, "ranking_scope": "among_collected_videos", "status": status, "started_at": now.isoformat(), "finished_at": datetime.now(timezone.utc).isoformat(),
            "filters": filters, "limits": {"max_pages": args.max_pages, "max_seconds": args.max_seconds, "concurrency": args.concurrency}, "limits_reached": limits,
            "counts": {"seeds": len(urls), "scheduled": len(scheduled), "pages": len(pages)}, "test_fixture_mode": args.allow_local_fixtures,
            "crawler": {"name": "Crawlee PlaywrightCrawler" if backend == "browser" else "Crawlee BeautifulSoupCrawler", "backend": backend, "version": importlib.metadata.version("crawlee")},
            "approved": approved, "candidates": candidates, "rejected": rejected, "errors": errors}


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--angle", choices=ANGLES, help="Compatibilidade legada: resolve um nicho amplo, sem buscar produto")
    parser.add_argument("--niche", help="Nicho editorial textual: saúde e beleza, manifestação/tarot, ou outro")
    parser.add_argument("--seeds", required=True, type=Path)
    parser.add_argument("--backend", choices=("http", "browser"), default="browser", help="Browser renderiza JavaScript; HTTP é alternativa leve")
    parser.add_argument("--browser-profile", type=Path, help="Perfil de navegador dedicado com sessão autorizada; não cria login")
    parser.add_argument("--out", required=True, type=Path, help="Pasta de resultados; não deve existir")
    parser.add_argument("--timezone")
    parser.add_argument("--today", help="Data de referência YYYY-MM-DD; não altera horário observado das provas")
    parser.add_argument("--min-views", type=int)
    parser.add_argument("--lookback-days", type=int)
    parser.add_argument("--max-profile-age-days", type=int)
    parser.add_argument("--max-pages", type=int, default=20)
    parser.add_argument("--max-seconds", type=float, default=120)
    parser.add_argument("--concurrency", type=int, default=2)
    parser.add_argument("--allow-local-fixtures", action="store_true", help="Somente testes: permite HTTP loopback; marcado no relatório")
    args = parser.parse_args(argv)
    if not args.niche and not args.angle:
        parser.error("Informe --niche ou --angle legado")
    if not 1 <= args.max_pages <= 100 or not 1 <= args.max_seconds <= 600 or not 1 <= args.concurrency <= 4:
        parser.error("Limites: páginas 1..100, segundos 1..600, concorrência 1..4")
    if args.min_views is not None and args.min_views < 0 or args.lookback_days is not None and not 1 <= args.lookback_days <= 30 or args.max_profile_age_days is not None and not 1 <= args.max_profile_age_days <= 365:
        parser.error("Filtros numéricos fora do intervalo")
    if args.out.exists():
        parser.error("Pasta de saída já existe; use uma pasta nova para preservar provas anteriores")
    logging.basicConfig(level=logging.WARNING, format="%(levelname)s: %(message)s")
    try:
        result = asyncio.run(mine(args))
    except (ValueError, OSError, ImportError, KeyError, TypeError) as error:
        print(f"Mineração não executada: {error}", file=sys.stderr)
        return 1
    args.out.mkdir(parents=True)
    (args.out / "resultados.json").write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (args.out / "relatorio.md").write_text(render_report(result), encoding="utf-8")
    print(json.dumps({"status": result["status"], "approved": len(result["approved"]), "candidates": len(result["candidates"]), "out": str(args.out.resolve())}, ensure_ascii=False))
    return 0 if result["status"] == "COMPLETE" else 1 if result["status"] == "FAILED" else 2


if __name__ == "__main__":
    raise SystemExit(main())
