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
TENTATIVAS = 3


def abrir(headless=False):
    from playwright.sync_api import sync_playwright
    pw = sync_playwright().start()
    ctx = pw.chromium.launch_persistent_context(
        str(PERFIL), channel="chrome", headless=headless, accept_downloads=True,
        viewport={"width": 1400, "height": 900})
    page = ctx.pages[0] if ctx.pages else ctx.new_page()
    return pw, ctx, page


def achar(page, chave, perfil=None, obrigatorio=True, timeout=4000):
    estr = SEL[chave]
    if isinstance(estr, dict):
        estr = estr[perfil]
    for e in estr:
        if "role" in e:
            loc = page.get_by_role(e["role"], name=e["name"]) if "name" in e else page.get_by_role(e["role"])
        elif "text" in e:
            loc = page.get_by_text(e["text"], exact=False)
        elif "label" in e:
            loc = page.get_by_label(e["label"])
        elif "placeholder" in e:
            loc = page.get_by_placeholder(e["placeholder"])
        else:
            loc = page.locator(e["css"])
        try:
            loc.first.wait_for(state="visible" if "css" not in e or "file" not in e["css"] else "attached", timeout=timeout)
            return loc.first
        except Exception:
            continue
    if obrigatorio:
        raise RuntimeError("seletor nao encontrado: %s (ajuste seletores.json com 'calibrar')" % chave)
    return None


def clicar(page, chave, perfil=None, obrigatorio=True):
    el = achar(page, chave, perfil, obrigatorio)
    if el:
        el.click()
    return el


def texto_pagina(page):
    try:
        return page.inner_text("body").lower()
    except Exception:
        return ""


def esperar_resultado(page, chave, antes, n, timeout_s, texto_antes):
    """Espera `n` itens novos. Levanta RuntimeError('BLOQUEIO: ...') ou RuntimeError('FALHA: ...')."""
    fim = time.time() + timeout_s
    while time.time() < fim:
        time.sleep(4)
        agora = page.locator(SEL[chave][0]["css"]).count()
        if agora - antes >= n:
            time.sleep(2)
            return agora
        novo = texto_pagina(page).replace(texto_antes, "") if texto_antes else texto_pagina(page)
        for t in SEL["bloqueio_texto"]:
            if t in novo and t not in texto_antes:
                raise RuntimeError("BLOQUEIO: mensagem contendo %r" % t)
        for t in SEL["erro_texto"]:
            if t in novo and t not in texto_antes:
                raise RuntimeError("FALHA: mensagem contendo %r" % t)
    raise RuntimeError("FALHA: tempo esgotado esperando resultado")


def baixar(page, ctx, chave, indices, destinos, atributo="src"):
    itens = page.locator(SEL[chave][0]["css"])
    for i, dest in zip(indices, destinos):
        url = itens.nth(i).get_attribute(atributo)
        if not url:
            raise RuntimeError("FALHA: item sem url para baixar")
        if url.startswith("blob:"):
            dados = page.evaluate("async u => Array.from(new Uint8Array(await (await fetch(u)).arrayBuffer()))", url)
            Path(dest).write_bytes(bytes(dados))
        else:
            Path(dest).write_bytes(ctx.request.get(url).body())


def configurar_geracao(page, modo, perfil, saidas):
    clicar(page, "modo_imagem" if modo == "imagem" else "modo_video", obrigatorio=False)
    if clicar(page, "abrir_config", obrigatorio=False):
        if modo == "imagem":
            clicar(page, "modelo_imagem_opcao", obrigatorio=False)
        else:
            clicar(page, "modelo_video_opcao", perfil, obrigatorio=False)
        clicar(page, "aspecto_9_16", obrigatorio=False)
        clicar(page, "saidas_4" if saidas == 4 else "saidas_1", obrigatorio=False)
        page.keyboard.press("Escape")


def preencher(page, prompt, anexos):
    if anexos:
        achar(page, "anexar_input").set_input_files([str(a) for a in anexos])
        time.sleep(3)
    campo = achar(page, "campo_prompt")
    campo.click()
    campo.fill(prompt)


def gerar_k(page, ctx, cod, prompt, anexos, saida):
    configurar_geracao(page, "imagem", None, 4)
    antes = page.locator(SEL["resultado_imagem"][0]["css"]).count()
    txt = texto_pagina(page)
    preencher(page, prompt, anexos)
    clicar(page, "gerar")
    total = esperar_resultado(page, "resultado_imagem", antes, 4, SEL["timeout_imagem_s"], txt)
    baixar(page, ctx, "resultado_imagem", range(antes, antes + 4),
           [saida / ("%s-%d.png" % (cod, i)) for i in range(1, 5)])


def gerar_v(page, ctx, cod, prompt, frame, perfil, saida):
    configurar_geracao(page, "video", perfil, 1)
    antes = page.locator(SEL["resultado_video"][0]["css"]).count()
    txt = texto_pagina(page)
    preencher(page, prompt, [frame])
    clicar(page, "gerar")
    esperar_resultado(page, "resultado_video", antes, 1, SEL["timeout_video_s"], txt)
    baixar(page, ctx, "resultado_video", [antes], [saida / (cod + ".mp4")])


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
    input("Faca login no Flow na janela aberta e aperte Enter aqui...")
    ctx.close(); pw.stop()


def cmd_calibrar(a):
    pw, ctx, page = abrir()
    page.goto(SEL["url"])
    input("Abra um projeto no Flow, deixe na tela de gerar imagem e aperte Enter...")
    out = {}
    for etapa in ("tela_imagem", "tela_video"):
        out[etapa] = page.evaluate("""() => [...document.querySelectorAll('button,[role=tab],[role=option],[role=menuitem],input,textarea,[contenteditable],video,img')]
          .slice(0,400).map(e => ({tag: e.tagName, role: e.getAttribute('role'), aria: e.getAttribute('aria-label'),
          text: (e.innerText||'').trim().slice(0,60), type: e.getAttribute('type'), src: (e.getAttribute('src')||'').slice(0,80)}))""")
        page.screenshot(path=str(AQUI / (etapa + ".png")))
        if etapa == "tela_imagem":
            input("Agora va para a tela de VIDEO (com frame inicial) e aperte Enter...")
    (AQUI / "calibragem.json").write_text(json.dumps(out, indent=1, ensure_ascii=False))
    print("Gravado flow_ui/calibragem.json e prints. Ajuste seletores.json.")
    ctx.close(); pw.stop()


def cmd_imagens(a, so=None):
    ks, _, _ = ler_entrega(a.entrega)
    est = Estado(a.saida)
    pw, ctx, page = abrir()
    page.goto(SEL["url"])
    input("Abra/crie o projeto do Flow, deixe na tela de imagem e aperte Enter...")
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
    ctx.close(); pw.stop()


def cmd_videos(a, so=None):
    _, vs, mapa = ler_entrega(a.entrega)
    est = Estado(a.saida)
    ef = est.dir / "escolhas.json"
    escolhas = json.loads(ef.read_text()) if ef.exists() else {}
    pw, ctx, page = abrir()
    page.goto(SEL["url"])
    input("Abra o projeto do Flow, deixe na tela de video e aperte Enter...")
    for cod, prompt in vs.items():
        if so and cod not in so:
            continue
        if not so and est.get(cod)["status"] in ("PRONTO", "BLOQUEADO"):
            continue
        img = escolhas.get(mapa.get(cod))
        if not img or not (est.dir / img).exists():
            est.set(cod, "PENDENTE", "falta escolher a imagem de %s" % mapa.get(cod)); print(cod, "falta escolha"); continue
        laco(est, cod, lambda: gerar_v(page, ctx, cod, prompt, est.dir / img, a.perfil, est.dir))
    ctx.close(); pw.stop()


def cmd_refaz(a):
    est = Estado(a.saida)
    alvo = a.codigos or [c for c, r in est.d.items() if r["status"] == "FALHOU"]
    for c in alvo:
        est.d[c]["tentativas"] = 0
        if c.startswith("K"):
            for f in est.dir.glob(c + "-*.png"):
                f.unlink()
    ks = {c for c in alvo if c.startswith("K")}; vs = {c for c in alvo if c.startswith("V")}
    if ks: cmd_imagens(a, ks)
    if vs: cmd_videos(a, vs)


def main():
    ap = argparse.ArgumentParser(); sp = ap.add_subparsers(dest="cmd", required=True)
    for nome in ("login", "calibrar", "imagens", "escolher", "videos", "status", "refaz"):
        p = sp.add_parser(nome)
        if nome in ("imagens", "videos", "refaz"): p.add_argument("entrega")
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
