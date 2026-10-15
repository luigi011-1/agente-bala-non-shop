"""Edição automática da fila de um lote, 3 vídeos por vez (Luigi, 2026-10-15).

A ordem é a da fila aprovada na conversa (FILA_EDICAO.json do lote, campo "order"). Os 3 primeiros vídeos
prontos para editar rodam juntos; o próximo lote de 3 só começa quando os 3 terminam. Sem pergunta, sem
pensar: roda o editar.py, entrega, anota o estado e segue.

    .venv-operacao/bin/python .claude/skills/edicao-lote/fila_edicao.py producao/<lote>/FILA_EDICAO.json [--paralelo 3]

Estados de "editing_status" (os que este script escreve):
    PENDING -> EDITING -> EDITED (fala OK, vídeo entregue; falta a revisão visual do orquestrador)
                       -> BLOCKED_FALA (take com fala diferente do roteiro; resolvedor-fala decide)
                       -> FAILED (erro de execução; ver log)
O orquestrador (Claude) marca APPROVED / REVIEW_FAIL depois do revisor-visual e devolve para PENDING o que
foi consertado. Item com takes_status diferente de RECEIVED fica na fila e não trava os outros.
"""
import argparse
import datetime
import glob
import json
import os
import shutil
import subprocess
import sys
import time

REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
PY = f"{REPO}/.venv-operacao/bin/python"
EDITAR = f"{REPO}/.claude/skills/edicao/template/editar.py"
GB_POR_VIDEO = 2.5   # pasta de trabalho com acabamento HyperFrames (~2 GB) + folga


def agora():
    return datetime.datetime.now().strftime("%H:%M:%S")


def carrega(caminho):
    return json.load(open(caminho, encoding="utf8"))


def salva(caminho, fila, meus=None):
    """Grava a fila. Com `meus`, relê o disco e troca só esses itens: o resolvedor-fala pode ter mexido em outro
    item enquanto o lote rodava."""
    if meus is not None:
        disco = carrega(caminho)
        por_ordem = {it["order"]: it for it in meus}
        disco["items"] = [por_ordem.get(it["order"], it) for it in disco["items"]]
        for k in ("execution", "parallel"):
            disco[k] = fila.get(k)
        fila = disco
    tmp = caminho + ".tmp"
    json.dump(fila, open(tmp, "w", encoding="utf8"), indent=2, ensure_ascii=False)
    os.replace(tmp, caminho)


def status_md(caminho, fila):
    linhas = [f"# Status da edição · {fila.get('batch', '')}", "",
              f"Execução: lotes de {fila.get('parallel', 3)} em paralelo, na ordem da fila. Atualizado {agora()}.", "",
              "| Ordem | Modelo | Avatar | Takes | Edição | Arquivo | Observação |", "|---|---|---|---|---|---|---|"]
    for it in sorted(fila["items"], key=lambda x: x["order"]):
        linhas.append(f"| {it['order']} | {it.get('model', '')} | {it.get('avatar', '')} | {it.get('takes_status', '')} | "
                      f"{it.get('editing_status', '')} | {it.get('final_file', '')} | {it.get('note', '')} |")
    open(os.path.join(os.path.dirname(caminho), "STATUS_EDICAO.md"), "w", encoding="utf8").write("\n".join(linhas) + "\n")


def livre_gb():
    st = os.statvfs("/tmp")
    return st.f_bavail * st.f_frsize / 1e9


def materializa(pasta):
    """Desktop no iCloud com disco cheio deixa takes 'dataless' (memória ambiente-mac-luigi): baixa e abre cada um."""
    for f in sorted(glob.glob(f"{pasta}/*.mp4")):
        for _ in range(6):
            subprocess.run(["brctl", "download", f], capture_output=True)
            r = subprocess.run(["ffmpeg", "-v", "error", "-i", f, "-f", "null", "-"], capture_output=True, text=True)
            if r.returncode == 0 and not r.stderr.strip():
                break
            time.sleep(5)


def detecta_takes(fila, estavel=120):
    """Marca RECEIVED sozinho: a pasta existe, tem pelo menos `take_count` .mp4 (se o item disser quantos) e nenhum
    arquivo mudou nos últimos `estavel` segundos (o Luigi pode estar copiando). Devolve as ordens marcadas."""
    marcadas = []
    for it in fila["items"]:
        if it.get("takes_status") == "RECEIVED" or not it.get("takes_folder"):
            continue
        pasta = os.path.expanduser(it["takes_folder"])
        mp4 = glob.glob(f"{pasta}/*.mp4")
        if not mp4 or len(mp4) < int(it.get("take_count") or 1):
            continue
        if time.time() - max(os.path.getmtime(f) for f in mp4) < estavel:
            continue
        it["takes_status"] = "RECEIVED"
        marcadas.append(it["order"])
    return marcadas


def nome_saida(it):
    return it.get("nome") or f"v{int(it['order']):02d}_{it.get('avatar', 'video')}"


def inicia(it, lote_dir, workers):
    pasta = os.path.expanduser(it["takes_folder"])
    materializa(pasta)
    trabalho = f"/tmp/edicao/{os.path.basename(lote_dir)}_{int(it['order']):02d}"
    shutil.rmtree(trabalho, ignore_errors=True)
    cmd = [PY, EDITAR, pasta, "--producao", it["production"], "--nome", nome_saida(it), "--trabalho", trabalho]
    exc = it.get("exceptions_file")
    if exc:
        cmd += ["--excecoes-fala", exc if os.path.isabs(exc) else os.path.join(lote_dir, exc)]
    cmd += it.get("extra_args", [])
    os.makedirs(f"{lote_dir}/logs", exist_ok=True)
    log = open(f"{lote_dir}/logs/{int(it['order']):02d}_{nome_saida(it)}.log", "w")
    env = dict(os.environ, EDICAO_WORKERS=str(workers))
    return subprocess.Popen(cmd, cwd=REPO, stdout=log, stderr=subprocess.STDOUT, env=env), trabalho, log.name


def fecha(it, code, trabalho, log, lote_dir):
    rel = f"{trabalho}/RELATORIO.md"
    texto = open(rel, encoding="utf8").read() if os.path.exists(rel) else ""
    saida = open(log, encoding="utf8", errors="replace").read()
    destino_rel = f"{REPO}/producao/{it['production']}/edicao/{nome_saida(it)}"
    os.makedirs(destino_rel, exist_ok=True)
    for f in ("RELATORIO.md", "cortes.png", "legendas.png"):
        if os.path.exists(f"{trabalho}/{f}"):
            shutil.copy2(f"{trabalho}/{f}", destino_rel)
    it["report_folder"] = destino_rel
    final = next(iter(glob.glob(f"{trabalho}/*_editado.mp4")), None)
    if "fala diferente" in saida:
        it["editing_status"] = "BLOCKED_FALA"
        it["note"] = "fala diferente do roteiro; ver RELATORIO.md"
    elif final and "palavra por palavra: OK" in texto:
        # entrega na pasta dos takes (regra 22); sem recompressão até 100 MB (regra 21)
        destino = os.path.join(os.path.expanduser(it["takes_folder"]), f"{nome_saida(it)}_editado.mp4")
        shutil.copy2(final, destino)
        it["final_file"] = destino
        it["size_bytes"] = os.path.getsize(destino)
        falhas = [l[2:] for l in texto.splitlines() if l.endswith(": FALHA")]
        it["editing_status"] = "EDITED"
        it["note"] = ("conferências com falha: " + "; ".join(falhas)) if falhas else "conferências OK"
        shutil.rmtree(trabalho, ignore_errors=True)   # ~2 GB por vídeo; o que importa já foi copiado
    else:
        it["editing_status"] = "FAILED"
        it["note"] = (saida.strip().splitlines() or ["sem saída"])[-1][:200]
    it["log_file"] = log


def adicionar(caminho, a):
    """Chamado pela /produzir a cada pacote de avatar fechado: a ordem de chegada na fila = ordem aprovada.
    Idempotente por (produção, avatar). Cria a pasta onde o Luigi solta os takes."""
    fila = carrega(caminho) if os.path.exists(caminho) else {
        "batch": os.path.basename(os.path.dirname(caminho)), "parallel": 3, "execution": "batches_of_3", "items": []}
    if any(it["production"] == a.producao and it.get("avatar") == a.avatar for it in fila["items"]):
        print(f"já na fila: {a.producao} / {a.avatar}")
        return
    ordem = max([it["order"] for it in fila["items"]] or [0]) + 1
    pasta = a.pasta_takes or f"~/Desktop/{fila['batch']}/{ordem:02d}_{a.modelo}_{a.avatar}"
    os.makedirs(os.path.expanduser(pasta), exist_ok=True)
    fila["items"].append({"order": ordem, "model": a.modelo, "avatar": a.avatar, "production": a.producao,
                          "nome": a.nome or f"{a.modelo.lower()}_{a.avatar}", "takes_folder": pasta,
                          "take_count": a.take_count, "takes_status": "NOT_RECEIVED", "editing_status": "PENDING"})
    os.makedirs(os.path.dirname(caminho), exist_ok=True)
    salva(caminho, fila); status_md(caminho, fila)
    print(f"ordem {ordem}: {a.modelo} / {a.avatar} → takes em {pasta}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("fila")
    ap.add_argument("--adicionar", action="store_true", help="acrescenta um vídeo no fim da fila e sai")
    ap.add_argument("--producao"); ap.add_argument("--avatar"); ap.add_argument("--modelo", default="V01")
    ap.add_argument("--nome", help="nome do arquivo final (padrão: <modelo>_<avatar>)")
    ap.add_argument("--pasta-takes", help="padrão: ~/Desktop/<lote>/<NN>_<modelo>_<avatar>")
    ap.add_argument("--take-count", type=int, help="quantos .mp4 o vídeo tem (número de V__ do pacote)")
    ap.add_argument("--paralelo", type=int, default=3)
    ap.add_argument("--so-um-lote", action="store_true", help="roda só o próximo lote de N e sai")
    ap.add_argument("--esperar-takes", type=int, default=0, metavar="MIN",
                    help="sem nada pronto, espera até MIN minutos por takes novos antes de encerrar (0 = encerra)")
    a = ap.parse_args()
    caminho = os.path.abspath(a.fila)
    if a.adicionar:
        if not (a.producao and a.avatar):
            sys.exit("--adicionar precisa de --producao e --avatar")
        return adicionar(caminho, a)
    lote_dir = os.path.dirname(caminho)
    workers = max(1, (os.cpu_count() or 8) // a.paralelo)
    # o Mac não dorme enquanto a fila roda (tampa aberta; com a tampa fechada só na tomada e com monitor externo)
    subprocess.Popen(["caffeinate", "-i", "-s", "-w", str(os.getpid())])
    espera_ate = None
    while True:
        fila = carrega(caminho)
        fila["execution"] = f"batches_of_{a.paralelo}"
        fila["parallel"] = a.paralelo
        novas = detecta_takes(fila)
        if novas:
            print(f"[{agora()}] TAKES_RECEBIDOS ordens {novas}", flush=True)
        prontos = [it for it in sorted(fila["items"], key=lambda x: x["order"])
                   if it.get("takes_status") == "RECEIVED" and it.get("editing_status", "PENDING") == "PENDING"]
        if not prontos:
            salva(caminho, fila); status_md(caminho, fila)
            faltam = [it["order"] for it in fila["items"] if it.get("editing_status", "PENDING") == "PENDING"]
            if faltam and a.esperar_takes:
                espera_ate = espera_ate or time.time() + a.esperar_takes * 60
                if time.time() < espera_ate:
                    time.sleep(60)
                    continue
            print(f"[{agora()}] FILA_FIM nada pendente com takes recebidos; aguardando takes: {faltam}", flush=True)
            return
        espera_ate = None
        lote = prontos[:a.paralelo]
        precisa = GB_POR_VIDEO * len(lote) + 3
        if livre_gb() < precisa:
            print(f"[{agora()}] DISCO_CHEIO livre {livre_gb():.1f} GB < {precisa:.1f} GB; parei antes do lote", flush=True)
            sys.exit(4)
        print(f"[{agora()}] LOTE_INICIO ordens {[it['order'] for it in lote]}", flush=True)
        rodando = []
        for it in lote:
            it["editing_status"] = "EDITING"; it["note"] = f"iniciado {agora()}"
            rodando.append((it, *inicia(it, lote_dir, workers), time.time()))
        salva(caminho, fila, lote); status_md(caminho, carrega(caminho))
        for it, proc, trabalho, log, t0 in rodando:
            code = proc.wait()
            fecha(it, code, trabalho, log, lote_dir)
            it["edit_seconds"] = round(time.time() - t0)
            print(f"[{agora()}] VIDEO_FIM ordem {it['order']} {it['editing_status']} {it.get('final_file', '')}", flush=True)
            salva(caminho, fila, lote); status_md(caminho, carrega(caminho))
        print(f"[{agora()}] LOTE_FIM ordens {[it['order'] for it in lote]} → "
              f"{[it['editing_status'] for it in lote]}", flush=True)
        if a.so_um_lote:
            return


if __name__ == "__main__":
    main()
