#!/usr/bin/env python3
"""Substituto do agente do Flow: gera K (4 imagens) e V (1 video) pela API do Google.

Uso (no Mac do Luigi, com GEMINI_API_KEY no ambiente ou em flow_api/.env):
  python flow_api/flow_api.py imagens  ENTREGA.md --saida out/cofre --anexo sheet.jpg --frames frames_modelo/
  python flow_api/flow_api.py escolher --saida out/cofre          # abre pagina local, 1 clique por K
  python flow_api/flow_api.py videos   ENTREGA.md --saida out/cofre
  python flow_api/flow_api.py status   --saida out/cofre
  python flow_api/flow_api.py refaz    ENTREGA.md --saida out/cofre [K03 V05 ...]   # sem codigos = so os FALHOU

Estado em <saida>/estado.json. Nunca reescreve prompt. Falha repete 2 vezes e vira FALHOU/BLOQUEADO.
"""
import argparse, json, os, re, sys, time
from pathlib import Path

MODELO_IMG = os.environ.get("FLOW_MODELO_IMG", "gemini-3.1-flash-image")
MODELO_VID = os.environ.get("FLOW_MODELO_VID", "veo-3.1-lite-generate-preview")
N_IMG = 4
TENTATIVAS = 3
RE_K = re.compile(r"^###\s+(K\d+)\b[^\n]*\n+```text\n(.*?)\n```", re.M | re.S)
RE_V = re.compile(r"^###\s+(V\d+)\b[^\n]*\n+```text\n(.*?)\n```", re.M | re.S)
RE_MAPA = re.compile(r"^(V\d+):\s*(K\d+)\s*$", re.M)


def carregar_env():
    f = Path(__file__).with_name(".env")
    if f.exists():
        for l in f.read_text().splitlines():
            if "=" in l and not l.startswith("#"):
                k, v = l.split("=", 1)
                os.environ.setdefault(k.strip(), v.strip())


def cliente():
    carregar_env()
    from google import genai
    if not os.environ.get("GEMINI_API_KEY"):
        sys.exit("Falta GEMINI_API_KEY (ambiente ou flow_api/.env)")
    return genai.Client(api_key=os.environ["GEMINI_API_KEY"])


def ler_entrega(p):
    t = Path(p).read_text(encoding="utf-8")
    ks = {c: re.sub(r"^%s\n" % c, "", b) for c, b in RE_K.findall(t)}
    vs = {c: re.sub(r"^%s\n" % c, "", b) for c, b in RE_V.findall(t)}
    mapa = dict(RE_MAPA.findall(t))
    for v in vs:
        if v not in mapa:  # classico: maior K <= numero do V
            menores = [k for k in ks if int(k[1:]) <= int(v[1:])]
            mapa[v] = sorted(menores, key=lambda x: int(x[1:]))[-1] if menores else None
    return ks, vs, mapa


class Estado:
    def __init__(self, saida):
        self.dir = Path(saida); self.dir.mkdir(parents=True, exist_ok=True)
        self.f = self.dir / "estado.json"
        self.d = json.loads(self.f.read_text()) if self.f.exists() else {}

    def set(self, cod, status, nota="", tent=None):
        r = self.d.setdefault(cod, {"status": "PENDENTE", "tentativas": 0, "nota": ""})
        r["status"] = status; r["nota"] = nota
        if tent is not None:
            r["tentativas"] = tent
        self.f.write_text(json.dumps(self.d, indent=1, ensure_ascii=False))

    def get(self, cod):
        return self.d.get(cod, {"status": "PENDENTE", "tentativas": 0})


def bloqueio(e):
    s = str(e).lower()
    return any(x in s for x in ("safety", "blocked", "policy", "prohibited", "sensitive", "responsible ai"))


def gerar_k(cli, cod, prompt, anexos, saida, n):
    from google.genai import types
    partes = [types.Part.from_bytes(data=Path(a).read_bytes(),
              mime_type="image/png" if str(a).lower().endswith("png") else "image/jpeg") for a in anexos]
    partes.append(prompt)
    arquivos = []
    for i in range(1, n + 1):
        dest = saida / ("%s-%d.png" % (cod, i))
        if dest.exists():
            arquivos.append(dest); continue
        r = cli.models.generate_content(
            model=MODELO_IMG, contents=partes,
            config=types.GenerateContentConfig(
                response_modalities=["IMAGE"],
                image_config=types.ImageConfig(aspect_ratio="9:16")))
        img = next((p.inline_data.data for c in (r.candidates or []) for p in (c.content.parts or [])
                    if getattr(p, "inline_data", None) and p.inline_data.data), None)
        if not img:
            raise RuntimeError("sem imagem na resposta: %s" % str(r)[:300])
        dest.write_bytes(img); arquivos.append(dest)
    return arquivos


def cmd_imagens(a, so=None):
    ks, _, _ = ler_entrega(a.entrega)
    cli, est = cliente(), Estado(a.saida)
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
        tent = est.get(cod)["tentativas"]
        for _ in range(TENTATIVAS):
            tent += 1; est.set(cod, "GERANDO", tent=tent)
            try:
                gerar_k(cli, cod, prompt, anexos, est.dir, N_IMG)
                est.set(cod, "PRONTO", "4 imagens", tent); break
            except Exception as e:
                if bloqueio(e):
                    est.set(cod, "BLOQUEADO", str(e)[:300], tent); break
                est.set(cod, "FALHOU", str(e)[:300], tent); time.sleep(5)
        print(cod, est.get(cod)["status"])


def cmd_videos(a, so=None):
    from google.genai import types
    _, vs, mapa = ler_entrega(a.entrega)
    cli, est = cliente(), Estado(a.saida)
    escolhas = json.loads((est.dir / "escolhas.json").read_text()) if (est.dir / "escolhas.json").exists() else {}
    for cod, prompt in vs.items():
        if so and cod not in so:
            continue
        if not so and est.get(cod)["status"] in ("PRONTO", "BLOQUEADO"):
            continue
        k = mapa.get(cod); img = escolhas.get(k)
        if not img or not (est.dir / img).exists():
            est.set(cod, "PENDENTE", "falta escolher a imagem de %s" % k); print(cod, "falta escolha de", k); continue
        tent = est.get(cod)["tentativas"]
        for _ in range(TENTATIVAS):
            tent += 1; est.set(cod, "GERANDO", tent=tent)
            try:
                op = cli.models.generate_videos(
                    model=MODELO_VID, prompt=prompt,
                    image=types.Image(image_bytes=(est.dir / img).read_bytes(), mime_type="image/png"),
                    config=types.GenerateVideosConfig(aspect_ratio="9:16", duration_seconds=8, number_of_videos=1))
                while not op.done:
                    time.sleep(10); op = cli.operations.get(op)
                if getattr(op, "error", None):
                    raise RuntimeError(str(op.error))
                vid = op.response.generated_videos[0].video
                cli.files.download(file=vid)
                vid.save(str(est.dir / (cod + ".mp4")))
                est.set(cod, "PRONTO", "", tent); break
            except Exception as e:
                if bloqueio(e):
                    est.set(cod, "BLOQUEADO", str(e)[:300], tent); break
                est.set(cod, "FALHOU", str(e)[:300], tent); time.sleep(5)
        print(cod, est.get(cod)["status"])


def cmd_status(a):
    est = Estado(a.saida)
    print("| Codigo | Status | Tentativas | Nota |\n|---|---|---|---|")
    for c, r in sorted(est.d.items(), key=lambda x: (x[0][0], int(x[0][1:]))):
        print("| %s | %s | %s | %s |" % (c, r["status"], r["tentativas"], r["nota"][:80]))


def cmd_refaz(a):
    est = Estado(a.saida)
    alvo = a.codigos or [c for c, r in est.d.items() if r["status"] == "FALHOU"]
    for c in alvo:
        est.d[c]["tentativas"] = 0
        if c.startswith("K"):
            for f in est.dir.glob(c + "-*.png"):
                f.unlink()
    ks = [c for c in alvo if c.startswith("K")]; vs = [c for c in alvo if c.startswith("V")]
    if ks: cmd_imagens(a, set(ks))
    if vs: cmd_videos(a, set(vs))


PAGINA = """<!doctype html><meta charset=utf-8><meta name=viewport content="width=device-width">
<title>Escolher imagens</title><style>body{font-family:sans-serif;background:#111;color:#eee;margin:16px}
.k{margin:0 0 24px}.row{display:flex;gap:8px}.row img{width:23%;border:4px solid transparent;border-radius:6px;cursor:pointer}
.row img.sel{border-color:#3ddc84}button{padding:12px 20px;font-size:16px}</style>
<h2>Clique em 1 imagem por K</h2><div id=a></div><button onclick=salvar()>Salvar escolhas</button> <span id=m></span>
<script>let esc={};fetch('/dados').then(r=>r.json()).then(d=>{esc=d.escolhas;const a=document.getElementById('a');
for(const k in d.imgs){const w=document.createElement('div');w.className='k';w.innerHTML='<b>'+k+'</b><div class=row></div>';
for(const f of d.imgs[k]){const i=document.createElement('img');i.src='/img/'+f;if(esc[k]==f)i.className='sel';
i.onclick=()=>{esc[k]=f;w.querySelectorAll('img').forEach(x=>x.className='');i.className='sel'};w.lastChild.appendChild(i)}a.appendChild(w)}});
function salvar(){fetch('/salvar',{method:'POST',body:JSON.stringify(esc)}).then(()=>document.getElementById('m').textContent='Salvo. Pode fechar e rodar: videos')}</script>"""


def cmd_escolher(a):
    from http.server import BaseHTTPRequestHandler, HTTPServer
    est = Estado(a.saida); ef = est.dir / "escolhas.json"

    class H(BaseHTTPRequestHandler):
        def log_message(self, *x): pass
        def _o(self, body, tipo="text/html"):
            self.send_response(200); self.send_header("Content-Type", tipo); self.end_headers(); self.wfile.write(body)
        def do_GET(self):
            if self.path == "/":
                self._o(PAGINA.encode())
            elif self.path == "/dados":
                imgs = {}
                for f in sorted(est.dir.glob("K*-*.png")):
                    imgs.setdefault(f.name.split("-")[0], []).append(f.name)
                self._o(json.dumps({"imgs": imgs, "escolhas": json.loads(ef.read_text()) if ef.exists() else {}}).encode(), "application/json")
            elif self.path.startswith("/img/"):
                self._o((est.dir / Path(self.path[5:]).name).read_bytes(), "image/png")
        def do_POST(self):
            esc = json.loads(self.rfile.read(int(self.headers["Content-Length"])))
            ef.write_text(json.dumps(esc, indent=1))
            for k in esc: est.set(k, "SELECIONADO", esc[k], est.get(k)["tentativas"])
            self._o(b"ok")
    print("Abra http://localhost:8765 (Ctrl+C para sair)")
    HTTPServer(("127.0.0.1", 8765), H).serve_forever()


def main():
    ap = argparse.ArgumentParser(); sp = ap.add_subparsers(dest="cmd", required=True)
    for nome in ("imagens", "videos", "status", "refaz", "escolher"):
        p = sp.add_parser(nome)
        if nome in ("imagens", "videos", "refaz"): p.add_argument("entrega")
        p.add_argument("--saida", required=True)
        if nome in ("imagens", "refaz"):
            p.add_argument("--anexo", action="append"); p.add_argument("--frames")
        if nome == "refaz": p.add_argument("codigos", nargs="*")
    a = ap.parse_args()
    {"imagens": cmd_imagens, "videos": cmd_videos, "status": cmd_status, "refaz": cmd_refaz, "escolher": cmd_escolher}[a.cmd](a)


if __name__ == "__main__":
    main()
