"""Gera os ROTEIRO.md do lote Sea Moss receitas (2026-10-13). Rodar da raiz: python3 producao/seamoss_receitas_lote_2026_10_13/gerar_roteiros.py"""
import os, re
D = os.path.dirname(os.path.abspath(__file__))
exec(open(os.path.join(D, "textos.py")).read())

AV = {
 "meredith": ("Meredith Callahan", "producao/_ancoras/meredith_callahan_ancora.png",
              "cozinha pequena do Brooklyn, mesa de fórmica verde-menta, potes de sea moss e liquidificador de vidro no balcão, janela com prédio de tijolo e bandeirinha dos EUA no parapeito",
              "fogão e forno da própria cozinha; freezer = geladeira da cozinha"),
 "marshall": ("Marshall Beckett", "producao/_ancoras/marshall_beckett_ancora.jpg",
              "galpão de zinco na costa de lava do Havaí, mesa de tábua cinza, esteiras com alga secando, mar turquesa, bandeira dos EUA no pilar da direita",
              "aparelhos de bancada na mesa do galpão (forninho elétrico, fogareiro de uma boca, liquidificador, freezer horizontal pequeno encostado no pilar)"),
 "cassidy": ("Cassidy Hargrove", "producao/_ancoras/cassidy_hargrove_ancora.jpg",
             "galpão de cedro no cais do Maine, bancada de tábua gasta, estante com alga roxa secando, mar cinza-azulado, bandeira dos EUA na parede ao lado da porta",
             "aparelhos de bancada na bancada do cais (forninho elétrico, fogareiro de uma boca, liquidificador, freezer horizontal pequeno dentro da porta do galpão)"),
}
ORDEM_V = ["canela_limao", "bolinho_maca", "wrap_lentilha", "sorvete_banana"]
ORDEM_A = ["meredith", "marshall", "cassidy"]

NOTAS = {
 "canela_limao": [
  "Claim mais arriscado: o T8 do modelo prometia resultado por dia (\"by day three... day five... after only a week\"). Linha do tempo de resultado é proibida no Sea Moss (sem antes/depois), então virou presente sem prazo.",
  "\"calm the inflammation\" e \"get your digestion moving\" ficam na boca da RECEITA, como no modelo; o produto só ecoa ingredientes e rótulo.",
  "\"so your body holds onto water instead of bloat\" do modelo saiu (afirmação fisiológica confusa e o take passava de 29 palavras).",
  "Canela não está entre os 16 do Natural Rems: a ponte espelha só o que existe (gengibre, cúrcuma, mel de manuka, vitamina C no lugar do limão). Nunca dizer que a goma tem canela.",
  "Gancho fiel: boneco humano de açúcar recebendo canela por cima (T1, ela fala) e se desfazendo (T2, mudo, sem nenhuma fala por cima).",
 ],
 "bolinho_maca": [
  "Claim mais arriscado: \"burning off that stubborn belly fat\" do modelo virou \"gets a chance to let go of that stubborn belly fat\" (receita, não produto). O produto nunca promete gordura.",
  "Temperatura: o modelo diz 180 graus (Celsius); para o público dos EUA virou 350 graus (Fahrenheit, o equivalente).",
  "Receita em 9 cenas curtas, como o modelo: cada corte é um take (CENA CURTA).",
  "Ponte: maçã do bolinho → maçã e vinagre de maçã dentro da goma (dos 16 do rótulo), dor = vontade de doce, obstáculo = goma com açúcar devolve a vontade.",
 ],
 "wrap_lentilha": [
  "Claim mais arriscado: \"brain fog\" do CTA do modelo saiu (não é claim do rótulo). Ficaram inchaço e imunidade (sabugueiro, vitamina C e D3 estão nos 16).",
  "O beat \"I share real recipes to boost your health...\" do modelo virou a dobradiça da ponte.",
 ],
 "sorvete_banana": [
  "Modelo em espanhol, transcrição multilíngue em `r_1791928419561/watch_es/`. Roteiro final em inglês americano, tradução fiel da sequência.",
  "O modelo fecha com um prato de BROWNIE dizendo \"solo plátanos\" (erro do próprio modelo). No clone o take mostra a tigela de sorvete.",
  "Keyword do modelo (`scoop`) virou `yes`, a do Ângulo 1.",
  "\"packed with potassium\" fica na boca da receita (banana), nunca do produto.",
  "As transições de glitch do modelo são efeito de edição, não takes.",
 ],
}

NOTA_AV = {("meredith", "bolinho_maca"): [
    "- 2026-10-14: o V16 gerado cortou em \"no\" (o \"oven\" ficou fora dos 8s). Mesmo critério da opção 1 do Luigi: o T16 termina em \"It feeds that same gut.\" (OVR em textos.py).",
    "- 2026-10-14: no V03 o Flow inventou fala em volta de \"add cinnamon\"; o take foi cortado em 1,62-2,75s (original em ~/Desktop/Meredith - V02/_originais/).", ""],
    ("cassidy", "canela_limao"): [
    "- 2026-10-14 (Luigi, opção 1, mesma decisão da Marshall): o V09 gerado cortou em \"and no\". O T9 dela termina em \"is annoying.\" (exceção OVR em textos.py).", ""],
    ("marshall", "canela_limao"): [
    "- 2026-10-13 (Luigi): T2/V02 (boneco de açúcar se desfazendo, mudo) NÃO gerou no Flow para a Marshall, nem nas variações. Take IGNORADO: a montagem vai do V01 direto para o V03.",
    "- 2026-10-14 (Luigi, opção 1): o V09 gerado cortou em \"and no\" (26 palavras não couberam em 8s). O T9 dela termina em \"is annoying.\" (exceção OVR em textos.py).", ""]}


def palavras(s):
    return len(re.findall(r"[A-Za-z0-9']+", s))

def main():
    for v in ORDEM_V:
        m = MODELO[v]
        for a in ORDEM_A:
            nome, anc, cen, aparelhos = AV[a]
            takes = []
            for (beat, setup, curta, en, pt) in VID[v]:
                if "AUTORIDADE" in beat:
                    en, pt = AUT[v][a]
                en, pt = OVR.get((v, a, len(takes) + 1), (en, pt))
                takes.append((beat, setup, curta, en, pt))
            slug = f"{a}_seamoss_{v}"
            d = os.path.join(D, "..", slug)
            os.makedirs(d, exist_ok=True)
            n_prod = next(i for i, t in enumerate(takes, 1) if "PRODUTO" in t[0])
            L = [f"# {nome} | Ângulo 1 (Natural Rems Sea Moss) | {m['titulo']} | Roteiro\n",
                 "pipeline: classico",
                 "tipo: venda · Ângulo 1 (Natural Rems Sea Moss) · rodada de VALIDAÇÃO (gancho e receita fiéis ao modelo, ponte para o produto no fim)",
                 "origem: avatar IA (watermark/acabamento sintético no modelo)",
                 f"CTA original: \"{m['cta_orig']}\"\n",
                 f"Vídeo modelo: `~/Downloads/{m['arq']}` ({m['dur']}): {m['desc']}. Evidências em `producao/seamoss_receitas_lote_2026_10_13/{m['pasta']}/`.",
                 f"Avatar: {nome}, USUÁRIA / PAR (1ª pessoa liberada, 2026-10-10), conta própria. Âncora `{anc}`.",
                 "Fila do lote: 4 modelos × 3 avatares = 12 vídeos (ver `producao/seamoss_receitas_lote_2026_10_13/LOTE.md`).",
                 "Variável trocada: nenhuma no gancho nem na receita (validação). Trocas obrigatórias: identidade e cenário fixo da conta; CTA do modelo → ponte para Natural Rems Sea Moss com os pontos fracos de fazer a receita (pedido do Luigi, 2026-10-13) e o CTA da marca.",
                 f"Funil: VENDA. Frasco em quadro do T{n_prod} até o fim. Comment `yes` antes da Amazon (sem DM), \"Search Natural Rems Sea Moss on Amazon\", Stories e bio, follow como última frase. Legenda: `#ad #syntheticperformer #naturalrems` no topo, sem link.",
                 f"Enquadramento: {nome} no cenário fixo da conta ({cen}); cozinha da receita = {aparelhos}. Ingrediente da vez colado na lente nos closes, como no modelo.",
                 "Divisão dos takes: um take por cena do modelo; plano longo dividido só em fim de frase; a ponte entra no último plano do modelo (avatar com o resultado da receita na mão, depois o frasco). Takes curtos marcados CENA CURTA.\n",
                 "## Tabela de esqueleto preservado\n", "| # | Beat | Original | Adaptado |", "|---|---|---|---|"]
            for i, (beat, setup, curta, en, pt) in enumerate(takes, 1):
                orig = "idêntico ao modelo" if beat.startswith(("GANCHO", "RECEITA", "RESULTADO", "MECANISMO", "PROTOCOLO", "DOR")) else "novo (ponte de venda)"
                txt = en if en else "(sem fala)"
                L.append(f"| {i} | {beat} | {orig} | {txt[:70]}{'…' if len(txt) > 70 else ''} |")
            L += ["\n## Setups de cena\n"]
            vistos = []
            for i, t in enumerate(takes, 1):
                if t[1] not in vistos:
                    vistos.append(t[1])
            for s in vistos:
                idx = [str(i) for i, t in enumerate(takes, 1) if t[1] == s]
                L.append(f"- **Setup {s} (T{', T'.join(idx)}):** plano do modelo no cenário da conta; detalhe na FICHA_FRAMES do pacote.")
            L += ["", "## Roteiro cena a cena (takes)\n"]
            for i, (beat, setup, curta, en, pt) in enumerate(takes, 1):
                mudo = "MUDO" in beat
                tipo = "B-ROLL" if mudo else "TALKING"
                cur = " · CENA CURTA" if (curta and not mudo) else ""
                L.append(f"### T{i} · {beat.replace(' · MUDO', '')} · {tipo}{' · MUDO' if mudo else ''} · Setup {setup}{cur}\n")
                if mudo:
                    L.append(f"(sem fala) {pt}\n")
                else:
                    L += [f"> \"{en}\"\n", f"PT: {pt}\n", f"Palavras: {palavras(en)}\n"]
            L += ["## Roteiro só-fala (inglês, pra TTS)\n", " ".join(t[3] for t in takes if t[3]) + "\n",
                  "## Notas de produção\n"]
            L += [f"- {n}" for n in NOTAS[v]]
            L += ["- Compliance Sea Moss: nada médico, sem antes/depois, sem cura nem resultado garantido do produto, sem remédio nem concorrente. Produto só ecoa ingredientes e rótulo (wild Irish sea moss, made in USA, <1 g de açúcar, 4 calorias, maçã verde, manuka).",
                  "- Ordem do CTA da marca: comment yes → Amazon → Stories/bio → follow (última frase).",
                  "- Se ficar longo: cortar primeiro o take de DIFERENCIAL; nunca o obstáculo nem o CTA.", ""]
            L += NOTA_AV.get((a, v), [])
            open(os.path.join(d, "ROTEIRO.md"), "w").write("\n".join(L))
            print(slug)

main()
