"""Gera os ROTEIRO.md do lote Sea Moss venda (2026-10-15). Rodar da raiz: python3 producao/seamoss_venda_lote_2026_10_15/gerar_roteiros.py"""
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
ORDEM_V = ["crosta_limao", "intestino_chia", "banana_canela", "mascara_vaselina"]
ORDEM_A = ["cassidy", "marshall", "meredith"]
LOTE = "seamoss_venda_lote_2026_10_15"

NOTAS = {
 "crosta_limao": [
  "Modelo em espanhol, transcrição multilíngue (`--language es --model small`) em `m_1792081855261/watch/`. Roteiro final em inglês americano, tradução fiel da sequência.",
  "Compliance: \"la inflamación desaparece\" virou \"the inflammation calms down\" e \"el intestino se limpia de verdad\" virou \"your gut finally feels clean\" (sem promessa de resultado). Fica na boca da RECEITA, nunca do produto.",
  "O plano único do gancho (0 a 11,5s) foi dividido em fim de frase: T1 com a água de limão na crosta, T2 com a fibra em pó, T3 com o líquido amarelo derretendo a crosta (payoff).",
  "Ponte: pimenta-do-reino, gengibre e cúrcuma da receita estão nos 16 do rótulo. Chia e limão não: nunca dizer que a goma tem chia.",
  "Mesma receita base do V02 (limão, chia, gengibre, cúrcuma) na mesma conta: ganchos, atrito e obstáculo diferentes; postar com distância entre os dois.",
 ],
 "intestino_chia": [
  "Claim mais arriscado: \"constipation\" no gancho (sintoma, não doença) fica na boca da RECEITA, como no modelo; o produto só ecoa ingredientes e rótulo. Aviso registrado (compliance-riscos, nível 3).",
  "\"Nobody can patent...\" é a frase de conspiração branda do modelo (nível 4, médio). Mantida.",
  "O livro \"Ancient Remedy Bible\" do CTA do modelo vira o frasco do Natural Rems no mesmo gesto (segurado perto da lente).",
  "O corte macro de 1s no gancho (1,47 a 2,47s) vira push-in dentro do V01, sem take próprio.",
  "Resultado e mecanismo do modelo no plano da bandeja, divididos em fim de frase.",
 ],
 "banana_canela": [
  "Claim mais arriscado: \"It calms inflammation, detoxes your liver, and keeps your cholesterol in check\" (fígado e colesterol = claim de saúde específico, nível 3, e a ponte passaria o claim para o produto) virou \"It calms the bloating, keeps you full for hours, and keeps your sugar cravings in check\".",
  "\"Big Pharma does not want you to know this\" fica (conspiração, nível 4, médio). Não é nome de remédio nem de concorrente.",
  "Canela e banana não estão nos 16: a ponte espelha ashwagandha (vontade de doce e estresse), vinagre de maçã e vitamina C (limão).",
  "O CTA de growth do modelo (\"more simple weight loss recipes\") virou a ponte de venda; o plano do sofá com o copo é o setup da virada.",
 ],
 "mascara_vaselina": [
  "Modelo em espanhol, transcrição multilíngue em `m_1792081632145/watch/`. Roteiro final em inglês americano, tradução fiel.",
  "Marcas do modelo (Vaseline, Arm & Hammer) saem da fala e da imagem: \"petroleum jelly\" e \"baking soda\" em potes sem marca.",
  "\"Las farmacias no quieren que sepas esto\" virou \"The pharmacies don't want you to know this\" (conspiração, nível 4). Mantida.",
  "\"fades dark spots\" e \"removes dead skin\" ficam na boca da RECEITA (cosmético de superfície); o produto só ecoa o rótulo (supports skin).",
  "Ponte: a máscara só trabalha por fora; sea moss por dentro. Mel → mel de manuka, vitamina C e raiz de bardana do rótulo.",
 ],
}

NOTA_AV = {}


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
                 f"Vídeo modelo: `~/Downloads/{m['arq']}` ({m['dur']}): {m['desc']}. Evidências em `producao/{LOTE}/{m['pasta']}/`.",
                 f"Avatar: {nome}, USUÁRIA / PAR (1ª pessoa liberada, 2026-10-10), conta própria. Âncora `{anc}`.",
                 f"Fila do lote: 4 modelos × 3 avatares = 12 vídeos (ver `producao/{LOTE}/LOTE.md`).",
                 "Variável trocada: nenhuma no gancho nem na receita (validação). Trocas obrigatórias: identidade e cenário fixo da conta; CTA do modelo → ponte para Natural Rems Sea Moss com os pontos fracos de fazer a receita (formato de 2026-10-13) e o CTA da marca.",
                 f"Funil: VENDA. Frasco em quadro do T{n_prod} até o fim. Comment `yes` antes da Amazon (sem DM), \"Search Natural Rems Sea Moss on Amazon\", link na bio, follow como última frase (Luigi, 2026-10-15: Amazon + bio + follow, sem Stories). Legenda: `#ad #syntheticperformer #naturalrems` no topo, sem link.",
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
                  "- Ordem do CTA da marca: comment yes → Amazon → bio → follow (última frase). Sem Stories neste lote (Luigi, 2026-10-15).",
                  "- Se ficar longo: cortar primeiro o take de DIFERENCIAL; nunca o obstáculo nem o CTA.", ""]
            L += NOTA_AV.get((a, v), [])
            open(os.path.join(d, "ROTEIRO.md"), "w").write("\n".join(L))
            print(slug)

main()
