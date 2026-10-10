"""Pacote do Flow no padrão único e mínimo (AGENTS.md, Luigi 2026-10-09) para produções clássicas com a
holistic.brandon (FitWell, avatar fixo da conta). Cada produção chama `gerar(...)` com os seus takes.

Escreve na pasta da produção: ENTREGA_AVATAR_FITWELL.md (copiável), AGENTE_FLOW.md, FICHA_FRAMES.md e
PROMPTS_PRODUCAO.md (seções que o checar_entrega.py cobra). K = um parágrafo; V = só a fala.
"""
import os
import re
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
import flow_seguro as FS  # noqa: E402

ANEXO = "holistic brandon.jpg"
ID = ("Match the attached image exactly for the woman's identity and outfit: a woman in her early thirties with long "
      "cornrow braids ending in wooden and gold beads, light freckles across her nose and cheeks, natural skin, a thin "
      "gold chain with a small gold cross, a floral blackwork tattoo sleeve on her right arm, a white ribbed fitted tank "
      "top and loose black athletic shorts.")
SET = ("She is in her gym behind a black table: white painted cinder-block wall, dark wood slat ceiling, a red neon "
       "sign reading TRAIN PRAY REPEAT on the left and a small American flag high on the wall at the right, both in "
       "sharp focus.")
CAM = "Vertical smartphone shot, 26mm lens, camera at chest height about one meter from the table, level, front facing."
END = ("Soft neutral even daylight, true neutral colors, real skin texture with visible pores, smartphone footage look, "
       "everything in sharp focus, 9:16 vertical.")


def k_texto(hero):
    return f"{ID} {SET} {hero} {CAM} {END}"


def v_texto(fala):
    return (f'The person in the image speaks in American English, looking at the camera: "{fala}"\n'
            "Fixed camera. Natural lip sync, no music.")


def gerar(pasta, titulo, qual, mapa, takes, ks, ficha_cam, notas_capcut):
    """takes: [(T, beat, cena_pt, fala_en, fala_pt, k_num)]; ks: {k_num: (cena_pt, hero_en, ficha)}.
    ficha = (frame do modelo, forma do herói, % do quadro, distância da lente, pose)."""
    nome = os.path.basename(pasta.rstrip("/"))
    checks, falhas = [], []
    for n, (cena, hero, _f) in ks.items():
        k = k_texto(hero)
        neg = len(FS.RE_NEGACAO.findall(k))
        gat = [a for a in FS.varrer_k(k)]
        checks.append((f"K{n:02d}", len(k), neg, "American flag" in k, "9:16" in k, gat))
        if len(k) > 1900 or neg > 2 or gat or "American flag" not in k:
            falhas.append(f"K{n:02d}")
    for t in takes:
        if FS.varrer_v(v_texto(t[3])):
            falhas.append(t[0])

    mapa_txt = "\n".join(f"V{int(t[0][1:]):02d}: K{t[5]:02d}" for t in takes)
    ent = [f"# ENTREGA | holistic.brandon | {titulo}\n", "flow_seguro: v1\n",
           f"Produção `{nome}` · Ângulo 2 FitWell · GROWTH · rodada de VALIDAÇÃO (clone fiel) · formato mínimo de prompt do Flow\n",
           "## Qual vídeo é este\n", qual + "\n",
           "## 1. Anexos e mapa\n",
           f"- **Imagem (K):** anexar SÓ a imagem da avatar (`{ANEXO}`) e colar o prompt. 4 variações, 9:16. Nada de frame do modelo.",
           "- **Vídeo (V):** anexar SÓ a imagem escolhida do K indicado no mapa e colar o prompt de vídeo. 1 variação, 9:16.",
           "- Bloco do agente Flow desta produção: `AGENTE_FLOW.md`.\n",
           mapa + "\n", "```text\nMAPA K/V\n" + mapa_txt + "\n```\n",
           "## 2. PROMPTS DE IMAGEM (um bloco por K)\n"]
    for n, (cena, hero, _f) in ks.items():
        ent.append(f"### K{n:02d} · anexar SÓ a imagem da avatar\n\nCena: {cena}\n\n```text\nK{n:02d}\n{k_texto(hero)}\n```\n")
    ent.append("## 3. PROMPTS DE VÍDEO (um bloco por V)\n")
    for t in takes:
        v = int(t[0][1:])
        ent.append(f"### V{v:02d} · {t[0]}, {t[1]} · anexar SÓ a imagem escolhida do K{t[5]:02d}\n\n"
                   f"Cena: {t[2]} Fala: \"{t[4]}\"\n\n```text\nV{v:02d}\n{v_texto(t[3])}\n```\n")
    ent.append("## 4. Transcrição final\n\n| Take | English | Português |\n|---|---|---|")
    ent += [f"| {t[0]} | {t[3]} | {t[4]} |" for t in takes]
    ent.append("\n**EN corrido:** " + " ".join(t[3] for t in takes))
    ent.append("\n**PT corrido:** " + " ".join(t[4] for t in takes) + "\n")
    open(os.path.join(pasta, "ENTREGA_AVATAR_FITWELL.md"), "w", encoding="utf8").write("\n".join(ent))

    nk, nv = len(ks), len(takes)
    regra_v = ("Cada V usa a imagem que sobrou do K indicado no MAPA K/V da entrega." if any(
        int(t[0][1:]) != t[5] for t in takes) else "Cada V usa a imagem que sobrou do K de mesmo número (V01 usa K01).")
    ag = f"""# Agente do Flow, produção atual: {titulo}

Você é o executor do Google Flow. Você só gera imagens e vídeos a partir de prompts prontos. Você não cria, não edita e não melhora prompt.

## Produção atual
- Conta: FitWell, vídeo de crescimento (growth). {titulo}.
- Um avatar só: a mulher de tranças com contas (arquivo `{ANEXO}`). Imagens K01 a K{nk:02d}; vídeos V01 a V{nv:02d}.

## O que é anexado (só isto, nada mais)
- IMAGEM (K): anexe só a imagem da avatar e cole o prompt.
- VÍDEO (V): anexe só a imagem que o operador escolheu do K indicado e cole o prompt de vídeo.
- Não existe frame modelo nem segunda imagem. Cenário, pose, câmera e objeto já estão escritos em cada prompt. Pare só se faltar a imagem da avatar (K) ou a imagem escolhida (V).

## Imagens (K01 a K{nk:02d})
1. Modelo: Nano Banana 2.1. Formato: 9:16 vertical.
2. Gere 4 variações por prompt. Confira o 4 e o 9:16 antes de CADA K, porque a tela volta sozinha para 1.
3. Cole o parágrafo inteiro, sem o código K, sem resumir, sem alterar uma palavra.
4. Nomeie as quatro: `K01-1`, `K01-2`, `K01-3`, `K01-4`.
5. Se saírem menos de 4, ou formato diferente de 9:16, gere de novo com o MESMO prompt e a MESMA imagem até existirem 4 em 9:16.
6. Gere todos os K e PARE. Avise: "K01 a K{nk:02d} prontos, 4 por K. Aguardando sua escolha." Não escolha, não apague e não gere vídeo.
7. O operador apaga 3 de cada K e deixa 1 escolhida a dedo. Nunca questione e nunca recrie uma imagem apagada.

## Vídeos (V01 a V{nv:02d})
1. Só começa quando o operador mandar. {regra_v} Se o K tiver mais de uma imagem ou nenhuma, pare e pergunte qual.
2. Modelo: Omni 1.1 Flash (use só esse). Duração: 8 segundos. Formato: 9:16. A imagem entra como imagem inicial.
3. Gere 1 variação por V. Confira o 1 antes de cada V.
4. O campo de texto recebe só o prompt V, inteiro, sem alterar uma palavra. O prompt V é curto e começa com `The person in the image`. Se começar com `Match the attached image`, é prompt de imagem: pare e avise.
5. Nomeie cada vídeo com o código do V (`V01`, `V02`...), que é a ordem da montagem.
6. No máximo 7 V por vez. Terminou o lote, relate e espere o operador dizer `prossiga`.

## Falhou, censura ou bloqueio
- Se a geração falhar, cair na censura, der erro ou o prompt for bloqueado: refaça com o MESMO prompt, sem trocar, cortar ou suavizar uma palavra, e tente de novo até aquele item sair.
- Não passe para o próximo item sem avisar qual está pendente: "K03 ainda pendente, tentativas: N."
- Você nunca reescreve prompt. Só o operador altera.
- Se o mesmo item falhar 3 vezes seguidas com "might violate our policies" (ou parecida), continue tentando com o MESMO prompt, mas avise na hora: código, quantas tentativas e a mensagem exata. O operador decide se reescreve.
- Se a interface não permitir 9:16, 4 variações (imagem) ou 1 variação (vídeo), avise antes de mudar qualquer configuração.

## Relatório de status
Depois de cada K ou V, diga: código, resultado (pronto, tentando de novo, pendente) e quantas tentativas. No fim do lote, liste concluídos e pendentes.

## Regras gerais
- Não adicione música, legenda, texto ou tradução.
- A fala do prompt é literal. Não corrija nem complete.
- Em caso de dúvida real (pacote incompleto, código duplicado, anexo faltando), pare e pergunte em uma linha.
"""
    open(os.path.join(pasta, "AGENTE_FLOW.md"), "w", encoding="utf8").write(ag)

    fi = [f"# Ficha dos frames · {titulo}\n",
          f"Frames do modelo em `_watch/frames/` (cenas e linha do tempo). {ficha_cam}\n",
          "| K | Frame do modelo | Herói e forma | % do quadro | Distância da lente | Câmera | Pose |",
          "|---|---|---|---|---|---|---|"]
    for n, (_c, hero, f) in ks.items():
        fi.append(f"| K{n:02d} | {f[0]} | {f[1]} | {f[2]} | {f[3]} | 26mm, altura do peito, ~1 m, frontal | {f[4]} |")
    fi.append("\nPlacar (F1-F6 e G1-G8 do `GATE_VISUAL.md` Parte 6), com evidência literal comum a todo K: "
              "F1 forma do herói = coluna 'Herói e forma' escrita no K; F2 medida = 'very close to the lens' / 'large in frame'; "
              "F3 distância = 'closer to the camera than her face'; F4 câmera = '26mm lens, camera at chest height'; "
              "F5 pose = descrita no K; F6 lista fechada = só os objetos da coluna 'Herói'. "
              "G1 luz = 'Soft neutral even daylight'; G2 sem tom quente = 'true neutral colors'; G3 âncoras de fundo = "
              "'red neon sign reading TRAIN PRAY REPEAT' + 'small American flag'; G4 foco = 'everything in sharp focus'; "
              "G5 realismo = 'real skin texture with visible pores, smartphone footage look'; G6 avatar fixo = 'Match the attached image exactly'; "
              "G7 boca de fala = 'mid-sentence'; G8 formato = '9:16 vertical'.\n")
    fi.append("Verificado por script (tamanho, negações, gatilhos do Flow seguro, bandeira e 9:16):\n")
    fi += [f"- {c[0]}: {c[1]} caracteres, {c[2]} negações, bandeira {'sim' if c[3] else 'NÃO'}, 9:16 {'sim' if c[4] else 'NÃO'}, gatilhos {c[5] or 'nenhum'}" for c in checks]
    open(os.path.join(pasta, "FICHA_FRAMES.md"), "w", encoding="utf8").write("\n".join(fi) + "\n")

    pp = [f"# PROMPTS | {titulo}\n", "flow_seguro: v1\n",
          f"Vídeo modelo: `input/modelo.mp4`. Âncora: `producao/_ancoras/holistic_brandon_ancora.jpg` (no Flow: `{ANEXO}`). Funil: growth.\n",
          "Os blocos copiáveis (K em parágrafo, V só com a fala) estão em `ENTREGA_AVATAR_FITWELL.md`. Este arquivo guarda o índice e as regras.\n",
          "## Índice de geração\n", "| Take | Keyframe | Ação de geração |", "|---|---|---|"]
    pp += [f"| {t[0]} | K{t[5]:02d} | {'gerar K' if all(x[5] != t[5] for x in takes[:i]) else 'reaproveita a imagem do K'} + V{int(t[0][1:]):02d} |"
           for i, t in enumerate(takes)]
    pp += ["\n## Trava de identidade e continuidade\n",
           "Todo K abre com a mesma descrição da avatar e do box de treino (avatar fixo da conta) e anexa só a imagem dela. "
           "Mesma roupa, mesma corrente com cruz de ouro, mesmo neon e bandeira em todo K.\n",
           "## Bloco global de vídeo\n",
           "Todo V: `The person in the image speaks in American English, looking at the camera: \"<fala literal>\"` + "
           "`Fixed camera. Natural lip sync, no music.` Padrão único do Flow (AGENTS.md, 2026-10-09): sem cena, roupa, objeto nem tom de voz no V.\n",
           "## Mapa de âncoras\n", "| Keyframe | Referências a anexar | Modelo |", "|---|---|---|"]
    pp += [f"| K{n:02d} | só `{ANEXO}` | Nano Banana 2.1, 4 variações, 9:16 |" for n in ks]
    pp += ["\n## Montagem no CapCut\n", notas_capcut + "\n",
           "## Gates de qualidade\n",
           "1. `python3 checar_entrega.py` e `python3 flow_seguro.py` sem falha.",
           "2. Ficha dos frames escrita antes dos K (`FICHA_FRAMES.md`).",
           "3. Checklist de envio rodado e informado fora dos blocos.",
           "4. Na edição: fala de cada take conferida palavra por palavra com o roteiro.\n"]
    open(os.path.join(pasta, "PROMPTS_PRODUCAO.md"), "w", encoding="utf8").write("\n".join(pp))

    for c in checks:
        print(c[0], c[1], "chars", c[2], "neg", "flag" if c[3] else "SEM BANDEIRA", "9:16" if c[4] else "SEM 9:16", c[5] or "")
    print("FALHAS:", falhas or "nenhuma")
    return not falhas
