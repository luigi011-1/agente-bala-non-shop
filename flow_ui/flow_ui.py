#!/usr/bin/env python3
"""Automacao do Google Flow pela interface web (faz o trabalho manual do Luigi, sem o agente do Flow).

Setup unico (Mac): pip install playwright && playwright install chromium
Primeiro uso: python flow_ui/flow_ui.py login        (loga no Flow na janela aberta; a sessao fica no perfil)
Depois:
  python flow_ui/flow_ui.py calibrar                 (gera flow_ui/calibragem.json e print, para ajustar seletores.json)
  python flow_ui/flow_ui.py imagens ENTREGA.md --saida out/x --anexo sheet.jpg --frames frames_modelo/
  python flow_ui/flow_ui.py escolher --saida out/x   (pagina local, 1 clique por K)
  python flow_ui/flow_ui.py videos ENTREGA.md --saida out/x --perfil auraly|classico
  python flow_ui/flow_ui.py status|refaz  (iguais ao flow_api)
Falha repete o MESMO prompt ate 3 vezes; politica/moderacao vira BLOQUEADO e segue. Nunca reescreve prompt.
"""
import argparse, json, re, sys, time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "flow_api"))
from flow_api import ler_entrega, Estado, cmd_status, cmd_escolher  # noqa: E402

AQUI = Path(__file__).resolve().parent
SEL = json.loads((AQUI / "seletores.json").read_text(encoding="utf-8"))
PERFIL = Path.home() / ".flow_ui_perfil"
PORTA = 9222
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
TENTATIVAS = 3


def abrir(headless=False):
    """Conecta ao Chrome real do Luigi (perfil persistente, porta 9222). Se nao estiver aberto, abre.
    Chrome comum (sem flags de automacao) evita bloqueio de login do Google."""
    import subprocess, urllib.request
    from playwright.sync_api import sync_playwright
    def vivo():
        try:
            urllib.request.urlopen("http://localhost:%d/json/version" % PORTA, timeout=1); return True
        except Exception:
            return False
    if not vivo():
        PERFIL.mkdir(parents=True, exist_ok=True)
        subprocess.Popen([CHROME, "--user-data-dir=%s" % PERFIL, "--remote-debugging-port=%d" % PORTA,
                          "--no-first-run", SEL["url"]], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        for _ in range(30):
            if vivo(): break
            time.sleep(1)
        else:
            raise RuntimeError("Chrome nao abriu")
    pw = sync_playwright().start()
    browser = pw.chromium.connect_over_cdp("http://localhost:%d" % PORTA)
    ctx = browser.contexts[0]
    page = ctx.pages[0] if ctx.pages else ctx.new_page()
    return pw, ctx, page


def logado(page):
    return "accounts.google.com" not in page.url


def abrir_projeto(page, url_projeto=None, nome=None):
    """Vai para o Flow (loga se preciso, esperando o Luigi) e entra num projeto (existente ou novo)."""
    if url_projeto:
        page.goto(url_projeto)
    elif "/project/" not in page.url:
        page.goto(SEL["url"])
    page.wait_for_timeout(3000)
    if not logado(page):
        print("Faca login no Flow na janela do Chrome; aguardando...")
        while not logado(page):
            time.sleep(2)
        page.wait_for_timeout(3000)
    if "/project/" not in page.url:
        page.locator("button, a").filter(has_text=re.compile(SEL["novo_projeto_texto"])).first.click()
        page.wait_for_url("**/project/**", timeout=30000)
    page.wait_for_selector(SEL["campo_prompt"], timeout=30000)
    if nome:
        pass  # nome do projeto fica o padrao (data/hora)
    print("Projeto:", page.url)


def fechar_overlays(page):
    for _ in range(4):
        if not page.locator(".cdk-overlay-backdrop").count():
            break
        page.keyboard.press("Escape"); page.wait_for_timeout(300)
        if page.locator(".cdk-overlay-backdrop").count():
            page.mouse.click(1100, 450); page.wait_for_timeout(300)


def radio(page, texto):
    return page.locator("button[role=radio]").filter(has_text=re.compile(re.escape(texto) + "$")).first


def configurar(page, modo, perfil, saidas):
    """modo: 'imagem' ou 'video'. Define modo, 9:16, modelo, Frames (video) e numero de saidas."""
    fechar_overlays(page)
    gatilho = page.get_by_role("button", name=SEL["gatilho_config"])
    gatilho.click(); page.wait_for_timeout(800)
    if not page.locator("button[role=radio]").first.is_visible():
        gatilho.click(); page.wait_for_timeout(800)
    radio(page, "Image" if modo == "imagem" else "Video").click(); page.wait_for_timeout(400)
    if modo == "video":
        radio(page, "Frames").click()
    radio(page, "9:16").click()
    modelo = SEL["modelo_imagem"] if modo == "imagem" else SEL["modelo_video"][perfil]
    page.get_by_role("button", name=SEL["menu_modelo"]).click(); page.wait_for_timeout(500)
    page.get_by_role("menuitem").filter(has_text=modelo).first.click(); page.wait_for_timeout(500)
    radio(page, "x%d" % saidas).click()
    fechar_overlays(page)
    resumo = gatilho.inner_text().replace("\n", " ")
    print("config:", resumo)
    if not re.search(r"x%d$" % saidas, resumo.strip()):
        radio(page, "x%d" % saidas).click(); fechar_overlays(page)
        resumo = gatilho.inner_text().replace("\n", " ")
        if not re.search(r"x%d$" % saidas, resumo.strip()):
            raise RuntimeError("FALHA: saidas nao ficaram x%d (%s)" % (saidas, resumo))
    if "9_16" not in gatilho.inner_html() and "9:16" not in resumo and "crop_9_16" not in resumo:
        raise RuntimeError("FALHA: config nao ficou 9:16 (%s)" % resumo)


def limpar_prompt(page):
    b = page.get_by_role("button", name="Clear prompt")
    if b.count() and b.first.is_visible():
        b.first.click(); page.wait_for_timeout(600)
    fechar_overlays(page)


def anexar(page, arquivo, modo):
    """Abre o seletor de midia (reference/ingredient na imagem, Start no video), sobe o arquivo e adiciona."""
    if modo == "video":
        page.get_by_role("button", name="Start", exact=True).click()
    else:
        page.get_by_role("button", name=SEL["botao_ingrediente"]).click()
    page.wait_for_timeout(1500)
    with page.expect_file_chooser() as fc:
        page.locator("button").filter(has_text="Upload media").first.click()
    # copia com nome unico: o Flow guarda todo upload e nomes repetidos ficariam ambiguos
    import shutil, tempfile
    arquivo = Path(arquivo)
    unico = Path(tempfile.mkdtemp()) / ("%d_%s" % (int(time.time() * 1000), arquivo.name))
    shutil.copy(arquivo, unico)
    fc.value.set_files(str(unico))
    item = page.locator("button").filter(has_text=re.compile("^" + re.escape(unico.name) + "(Image|Video)?$")).first
    item.wait_for(state="visible", timeout=90000)   # o item so ganha esse texto quando o upload termina
    item.click(); page.wait_for_timeout(600)
    page.get_by_role("button", name="Add to prompt").click()
    page.wait_for_timeout(2000)
    fechar_overlays(page)


def preencher(page, prompt):
    ed = page.locator(SEL["campo_prompt"]).first
    ed.click()
    page.keyboard.press("Meta+A"); page.keyboard.press("Backspace")
    page.keyboard.insert_text(prompt)


def srcs(page, seletor):
    return page.evaluate("s => [...document.querySelectorAll(s)].map(e => e.src)", seletor)


def texto_pagina(page):
    try:
        return page.inner_text("body").lower()
    except Exception:
        return ""


def esperar_novos(page, seletor, antes, n, timeout_s, texto_antes):
    """Espera `n` itens novos (src fora de `antes`). Levanta RuntimeError('BLOQUEIO...') ou ('FALHA...')."""
    fim = time.time() + timeout_s
    while time.time() < fim:
        time.sleep(4)
        novos = [u for u in srcs(page, seletor) if u not in antes]
        if len(novos) >= n:
            time.sleep(2)
            return [u for u in srcs(page, seletor) if u not in antes][:n]
        novo = texto_pagina(page)
        for t in SEL["bloqueio_texto"]:
            if t in novo and t not in texto_antes:
                raise RuntimeError("BLOQUEIO: mensagem contendo %r" % t)
        for t in SEL["erro_texto"]:
            if t in novo and t not in texto_antes:
                raise RuntimeError("FALHA: mensagem contendo %r" % t)
    raise RuntimeError("FALHA: tempo esgotado esperando resultado")


def baixar(ctx, urls, destinos):
    for u, dest in zip(urls, destinos):
        r = ctx.request.get(u)
        if not r.ok:
            raise RuntimeError("FALHA: download HTTP %s" % r.status)
        Path(dest).write_bytes(r.body())


def ext_imagem(corpo):
    return ".png" if corpo[:4] == b"\x89PNG" else ".jpg"


def gerar_k(page, ctx, cod, prompt, anexos, saida):
    configurar(page, "imagem", None, 4)
    limpar_prompt(page)
    for a in anexos:
        anexar(page, a, "imagem")
    preencher(page, prompt)
    antes, txt = set(srcs(page, SEL["resultado_imagem"])), texto_pagina(page)
    page.get_by_role("button", name="Start generation").click()
    urls = esperar_novos(page, SEL["resultado_imagem"], antes, 4, SEL["timeout_imagem_s"], txt)
    for i, u in enumerate(urls, 1):
        r = ctx.request.get(u)
        if not r.ok:
            raise RuntimeError("FALHA: download HTTP %s" % r.status)
        (saida / ("%s-%d%s" % (cod, i, ext_imagem(r.body())))).write_bytes(r.body())


def gerar_v(page, ctx, cod, prompt, frame, perfil, saida):
    configurar(page, "video", perfil, 1)
    limpar_prompt(page)
    anexar(page, frame, "video")
    preencher(page, prompt)
    antes, txt = set(srcs(page, SEL["miniatura_video"])), texto_pagina(page)
    page.get_by_role("button", name="Start generation").click()
    thumb = esperar_novos(page, SEL["miniatura_video"], antes, 1, SEL["timeout_video_s"], txt)[0]
    # o <video> so existe com o mouse em cima do tile; o id e o mesmo da miniatura
    video_id = re.search(r"/image/([0-9a-f-]+)", thumb).group(1)
    url = None
    for _ in range(10):
        page.mouse.move(1100, 1000)
        page.locator("img[src*='%s']" % video_id).first.hover()
        page.wait_for_timeout(1500)
        url = page.evaluate("id => { const v=[...document.querySelectorAll('video')].find(e=>e.src.includes(id)); return v ? v.src : null }", video_id)
        if url:
            break
    if not url:
        raise RuntimeError("FALHA: video pronto mas sem URL para baixar")
    baixar(ctx, [url], [saida / (cod + ".mp4")])


def laco(est, cod, fn):
    tent = est.get(cod)["tentativas"]
    for _ in range(TENTATIVAS):
        tent += 1
        est.set(cod, "GERANDO", tent=tent)
        try:
            fn()
            est.set(cod, "PRONTO", "", tent)
            break
        except Exception as e:
            msg = str(e)[:300]
            if msg.startswith("BLOQUEIO") or "seletor nao encontrado" in msg:
                est.set(cod, "BLOQUEADO", msg, tent); break
            est.set(cod, "FALHOU", msg, tent); time.sleep(5)
    print(cod, est.get(cod)["status"])


def cmd_login(a):
    pw, ctx, page = abrir()
    page.goto(SEL["url"])
    page.wait_for_timeout(3000)
    while not logado(page):
        print("Faca login no Flow na janela do Chrome; aguardando..."); time.sleep(3)
    print("Logado.")
    pw.stop()


def cmd_calibrar(a):
    """Despeja botoes/campos da tela atual do Flow em calibragem.json (para reajustar seletores.json)."""
    pw, ctx, page = abrir()
    abrir_projeto(page, a.projeto)
    out = page.evaluate("""() => [...document.querySelectorAll('button,[role=tab],[role=radio],[role=menuitem],[role=combobox],input,[contenteditable=true],video,img')]
      .filter(e => e.offsetParent !== null).map(e => ({tag: e.tagName, role: e.getAttribute('role'), aria: e.getAttribute('aria-label'),
      text: (e.innerText||'').trim().slice(0,60), alt: e.getAttribute('alt'), src: (e.getAttribute('src')||'').slice(0,80)}))""")
    page.screenshot(path=str(AQUI / "tela.png"))
    (AQUI / "calibragem.json").write_text(json.dumps(out, indent=1, ensure_ascii=False))
    print("Gravado flow_ui/calibragem.json e tela.png")
    pw.stop()


def cmd_imagens(a, so=None):
    ks, _, _ = ler_entrega(a.entrega)
    est = Estado(a.saida)
    pw, ctx, page = abrir()
    abrir_projeto(page, a.projeto)
    for cod, prompt in ks.items():
        if so and cod not in so:
            continue
        if not so and est.get(cod)["status"] in ("PRONTO", "SELECIONADO", "BLOQUEADO"):
            continue
        anexos = list(a.anexo or [])
        if a.frames:
            for ext in ("png", "jpg", "jpeg"):
                fr = Path(a.frames) / ("%s_modelo.%s" % (cod, ext))
                if fr.exists():
                    anexos.append(fr); break
        laco(est, cod, lambda: gerar_k(page, ctx, cod, prompt, anexos, est.dir))
    pw.stop()


def cmd_videos(a, so=None):
    _, vs, mapa = ler_entrega(a.entrega)
    est = Estado(a.saida)
    ef = est.dir / "escolhas.json"
    escolhas = json.loads(ef.read_text()) if ef.exists() else {}
    pw, ctx, page = abrir()
    abrir_projeto(page, a.projeto)
    for cod, prompt in vs.items():
        if so and cod not in so:
            continue
        if not so and est.get(cod)["status"] in ("PRONTO", "BLOQUEADO"):
            continue
        img = escolhas.get(mapa.get(cod))
        if not img or not (est.dir / img).exists():
            est.set(cod, "PENDENTE", "falta escolher a imagem de %s" % mapa.get(cod)); print(cod, "falta escolha"); continue
        laco(est, cod, lambda: gerar_v(page, ctx, cod, prompt, est.dir / img, a.perfil, est.dir))
    pw.stop()


def cmd_refaz(a):
    est = Estado(a.saida)
    alvo = a.codigos or [c for c, r in est.d.items() if r["status"] == "FALHOU"]
    for c in alvo:
        est.d[c]["tentativas"] = 0
        if c.startswith("K"):
            for f in list(est.dir.glob(c + "-*.png")) + list(est.dir.glob(c + "-*.jpg")):
                f.unlink()
    ks = {c for c in alvo if c.startswith("K")}; vs = {c for c in alvo if c.startswith("V")}
    if ks: cmd_imagens(a, ks)
    if vs: cmd_videos(a, vs)


def main():
    ap = argparse.ArgumentParser(); sp = ap.add_subparsers(dest="cmd", required=True)
    for nome in ("login", "calibrar", "imagens", "escolher", "videos", "status", "refaz"):
        p = sp.add_parser(nome)
        if nome in ("imagens", "videos", "refaz"): p.add_argument("entrega")
        if nome in ("calibrar", "imagens", "videos", "refaz"):
            p.add_argument("--projeto", help="URL de um projeto do Flow (padrao: cria um novo)")
        if nome not in ("login", "calibrar"): p.add_argument("--saida", required=True)
        if nome in ("imagens", "refaz"):
            p.add_argument("--anexo", action="append"); p.add_argument("--frames")
        if nome in ("videos", "refaz"): p.add_argument("--perfil", choices=["auraly", "classico"], default="classico")
        if nome == "refaz": p.add_argument("codigos", nargs="*")
    a = ap.parse_args()
    {"login": cmd_login, "calibrar": cmd_calibrar, "imagens": cmd_imagens, "escolher": cmd_escolher,
     "videos": cmd_videos, "status": cmd_status, "refaz": cmd_refaz}[a.cmd](a)


if __name__ == "__main__":
    main()
