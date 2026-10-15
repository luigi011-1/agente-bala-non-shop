"""Pacotes do lote Sea Moss VENDA, formato pilha de notícia (2026-10-13).
2 roteiros (rins, seios) x 3 avatares (Meredith, Marshall, Cassidy) = 6 produções em producao/<avatar>_seamoss_<tema>_noticia/.
Textos aprovados em textos.py (mesma fonte do ROTEIRO.md). Gerador comum: producao/_flow/pacote_minimo.py.

Plano do modelo: 1 plano de telejornal (T1) + 1 plano único de fala até o fim. Por isso 3 K por vídeo:
K01 telejornal (sem avatar), K02 avatar falando (T2 a T14), K03 avatar com o frasco (T15 a T21).
"""
import importlib.util
import os
import sys

D = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.abspath(os.path.join(D, "..", ".."))
sys.path.insert(0, os.path.join(RAIZ, "producao", "_flow"))
from pacote_minimo import gerar, CAM, END  # noqa: E402

exec(open(os.path.join(D, "textos.py"), encoding="utf8").read())


def _avatar(pasta):
    spec = importlib.util.spec_from_file_location("g_" + pasta, os.path.join(RAIZ, "producao", pasta, "gerar_pacote.py"))
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m.AVATAR


AV = {"meredith": _avatar("meredith_bolo_coco"), "marshall": _avatar("marshall_cheesecake_chocolate"),
      "cassidy": _avatar("cassidy_paes_batata_abacate")}
PRODUTO = "natural_rems_seamoss_produto.jpg"
ANCORAS = {  # âncora de TV diferente por conta (frases e rostos não se repetem entre contas)
    "meredith": "a news anchor woman in her late forties with a sleek blonde bob, a sage-green blazer over a black top",
    "marshall": "a news anchor woman in her early fifties with shoulder-length dark brown hair, a navy-blue blazer over a white top",
    "cassidy": "a news anchor woman in her mid forties with deep brown skin and short natural curls, a deep red blazer over a black top",
}
CHOQUE = {
    "rins": ("a large inset photo box beside her showing a close-up photo of a kidney cut in half, pink-orange tissue with "
             "a big shiny black stone lodged in the middle"),
    "seios": ("a large inset photo box beside her showing a close-up photo of two big round green coconuts hanging side by "
              "side from the top of a palm trunk, under the palm fronds, a funny suggestive shape"),
}


def k01(a, t):
    return (f"Television news studio frame, vertical 9:16. {ANCORAS[a].capitalize()}, seated at a glossy news desk with her "
            "hands resting on a few papers, looking straight into the camera, caught mid-sentence with lips naturally parted. "
            f"Behind her a large window wall shows a city skyline at blue hour, deep blue sky with lit towers. On the left, {CHOQUE[t]}, filling "
            "about a third of the frame. Across the bottom a red lower-third banner reads BREAKING NEWS in bold white letters "
            "with a white strip reading HEALTH ALERT. A small American flag stands on the desk at the right, in sharp focus. "
            "Broadcast camera at eye level, 35mm lens, front facing, medium shot from the chest up. Clean even studio light, "
            "true neutral colors, real skin texture with visible pores, everything in sharp focus, 9:16 vertical.")


MID = "She looks straight at the camera, caught mid-sentence, lips naturally parted, serious and animated expression."
POTE = ("the Natural Rems Sea Moss Gummies jar exactly as in the second attached image: a short wide jar of dark amber plastic "
        "with a black screw cap, a pale sage-green label with dark green text, the Natural Rems logo with three leaves, the "
        "big title Sea Moss Gummies, a pill-shaped badge reading 6000 MG | 16-IN-1, and the line GREEN APPLE FLAVOR")
REF_POTE = "Second image: front jar only."


def ks(a, t):
    av = AV[a]
    k3_hero = (f"Hero: she holds {POTE} in her right hand out toward the camera, very close to the lens, large in frame and "
               "closer to the camera than her face, label fully readable, fingers on the sides. {MID} {REF_POTE}")
    return {
        1: ("Telejornal de emissora inventada: âncora na bancada, skyline noturno, caixa de imagem de choque, faixa BREAKING NEWS.",
            "", ("0,0 a 7,8s (cena 1)", "âncora na bancada + caixa de imagem de choque ao lado + faixa BREAKING NEWS",
                 "caixa ~33%", "âncora no plano médio, caixa colada na borda", "sentada, mãos nos papéis, fala para a câmera"),
            {"raw": k01(a, t), "anexos": ["-"]}),
        2: (f"{av['nome']} no cenário fixo da conta falando, mão direita erguida com o indicador para cima perto da lente.",
            ("Hero: her right hand raised in the lower foreground, very close to the lens, large in frame and closer to the camera "
             f"than her face, index finger pointing up as she makes a point. {MID}"),
            ("7,8 a 130s (plano único de fala)", "mão direita com o indicador erguido (gesto do modelo)", "~20%", "colada",
             "em pé atrás da mesa, indicador erguido")),
        3: (f"{av['nome']} no mesmo plano segurando o frasco do Natural Rems Sea Moss colado na lente, rótulo legível.",
            k3_hero,
            ("132 a 170s (produto na mão)", "pote do Natural Rems Sea Moss, rótulo de frente", "~25%", "colado",
             "segura o pote com a mão direita estendida para a câmera"),
            {"anexos": [av["anexo"], PRODUTO]}),
    }


CENA = {1: "A âncora dá a notícia.", 2: "Ela fala para a câmera.", 3: "Ela segura o pote parado, rótulo legível."}
TEMA = {"rins": "a pior bebida para os rins (refrigerante diet)", "seios": "a pior comida para os seios (laticínio)"}


def takes(a, t):
    out = []
    for i, (en, pt) in enumerate(V[a, t], 1):
        k = 1 if i == 1 else (2 if i < 15 else 3)
        beat = (BR if t == "rins" else BS)[i - 1].capitalize()
        out.append((f"T{i}", beat, CENA[k], en, pt, k))
    return out


def main():
    ok = True
    for t in ("rins", "seios"):
        for a in ("meredith", "marshall", "cassidy"):
            av = AV[a]
            pasta = os.path.join(RAIZ, "producao", f"{a}_seamoss_{t}_noticia")
            qual = (f"**Vídeo: pilha de notícia, {TEMA[t]}.**\n\n"
                    f"**O que acontece:** abre num telejornal de emissora inventada (a âncora noticia que um vídeo viralizou). "
                    f"Corta para {av['nome']} no cenário fixo da conta, que elimina três suspeitos, absolve, explica o mecanismo, "
                    "revela o vilão, vira para a causa raiz e, com o pote na mão, apresenta o Natural Rems Sea Moss. "
                    "Fecha com comment yes, Amazon, Stories e bio, e o lembrete do follow.\n\n"
                    "**Gancho:** a âncora do telejornal com a imagem de choque e a faixa BREAKING NEWS.")
            mapa = "V01 usa K01; V02 a V14 usam a mesma imagem escolhida do K02; V15 a V21 usam a mesma imagem escolhida do K03."
            capcut = ("Edição automática (`editar.py`, acabamento HyperFrames): legenda palavra por palavra, cortes de pausa, "
                      "música a -18 dB da voz. Texto de tela no V01 (gancho), em cima: \"She exposed the WORST "
                      + ("drink for your kidneys" if t == "rins" else "food for your breasts")
                      + "\" e, embaixo, \"(listen carefully and share with your loved ones)\". O pote fica parado e legível de "
                      "V20 até o fim, sem corte para outro plano. Legenda do post: `#ad #syntheticperformer #naturalrems` no "
                      "topo, sem link; chave de conteúdo de IA ligada; Story no ar com o link da Amazon.")
            ok &= gerar(pasta, f"Sea Moss Venda · pilha de notícia · {t}", qual, mapa, takes(a, t), ks(a, t),
                        "Modelo: âncora de telejornal (plano médio) e depois plano único de podcast com microfone; o estúdio "
                        "vira o cenário fixo da avatar (avatar fixo da conta), sem microfone.",
                        capcut, avatar=av, tipo="VENDA")
            # O bloco do agente Flow vai INTEIRO no topo da entrega (CLAUDE.md, item 1 do pacote), não só em arquivo à parte.
            ent_p = os.path.join(pasta, av["entrega"])
            ent = open(ent_p, encoding="utf8").read()
            ag = open(os.path.join(pasta, "AGENTE_FLOW.md"), encoding="utf8").read()
            cab, resto = ent.split("## Qual vídeo é este", 1)
            novo = (cab + "## 0. INSTRUÇÕES PARA A MEMÓRIA DO AGENTE · GOOGLE FLOW (colar inteiro antes do primeiro K)\n\n"
                    "```text\n" + ag.strip() + "\n```\n\n## Qual vídeo é este" + resto)
            open(ent_p, "w", encoding="utf8").write(novo)
    return ok


if __name__ == "__main__":
    sys.exit(0 if main() else 1)
