import re,os,sys
exec(open(sys.argv[1]).read())
AV={"meredith":("Meredith Callahan","producao/_ancoras/meredith_callahan_ancora.png","cozinha pequena do Brooklyn, mesa de fórmica verde-menta, potes de sea moss e liquidificador no balcão, janela com prédio de tijolo e bandeirinha dos EUA no parapeito","40 anos fazendo sea moss para o bairro"),
"marshall":("Marshall Beckett","producao/_ancoras/marshall_beckett_ancora.jpg","galpão de zinco no Havaí, mesa de tábua cinza, esteiras com alga secando, mar turquesa, bandeira dos EUA no pilar da direita","50 anos mergulhando atrás de alga"),
"cassidy":("Cassidy Hargrove","producao/_ancoras/cassidy_hargrove_ancora.jpg","galpão de cedro no cais do Maine, bancada de tábua gasta, bandeira dos EUA na parede ao lado da porta","30 anos colhendo Irish moss no Maine")}
MOD={"rins":("sc_1 = SaveClip AQOj96… (168,2s), mulher de coque em estúdio de podcast; pilha de notícia do doc do Lucas (ângulo rins)","pior BEBIDA para os rins = refrigerante diet","metabolismo lento e inflamação → barriga que não baixa","vitamina D3, gengibre (intestino), cúrcuma, óleo de semente preta"),
"seios":("sc_2 = SaveClip AQPp0v… (170,5s), mulher de óculos com bandeira ao fundo; versão amaciada. Referência secundária: snapinsta-1791906347184 (homem, mesma copy)","pior COMIDA para os seios = laticínio","inflamação → colágeno e tecido → peito perde firmeza","vitamina C (formação normal de colágeno), cúrcuma com pimenta-do-reino, gengibre")}
B={"rins":BR,"seios":BS}
for (a,t),takes in V.items():
    nome,anc,cen,aut=AV[a]; mod=MOD[t]; slug=f"{a}_seamoss_{t}_noticia"
    d=f"producao/{slug}"; os.makedirs(d,exist_ok=True)
    def setup(i): return "A" if i==1 else ("B" if i<15 else "C")
    L=[f"# {nome} | Ângulo 1 (Natural Rems Sea Moss) | Pilha de notícia: {mod[1]} | Roteiro\n",
    "pipeline: classico","tipo: venda · Ângulo 1 (Natural Rems Sea Moss) · rodada de VALIDAÇÃO (blocos do modelo, frases reescritas)",
    "origem: avatar IA (âncora de telejornal + especialista em estúdio de podcast)",
    "CTA original: \"If you're ready to try Jupy Hydration, search for it on Amazon. I'll also leave the link in my bio and in the comments... comment Jupy and I'll send you the complete daily hydration routine... Just make sure you follow me first so you don't miss my message.\"\n",
    f"Vídeo modelo: {mod[0]}. Evidências em `producao/seamoss_venda_lote_2026_10_13/`.",
    "Referência de formato: doc \"NATURAL REMS, Copy de Referência, Pilha de Notícia\" (Lucas, @wyn.lucas), 14 blocos. Regra do doc: manter os blocos, reescrever as frases (cada avatar com frase própria).",
    f"Avatar: {nome}, USUÁRIA / PAR (1ª pessoa liberada, 2026-10-10), conta própria. Âncora `{anc}`. Autoridade de ofício fixa da conta: {aut} (mesmo número nos dois vídeos dela).",
    "Fila do lote: Meredith Callahan, Marshall Beckett, Cassidy Hargrove × (rins, seios) = 6 vídeos. Ordem: rins/Meredith, rins/Marshall, rins/Cassidy, seios/Meredith, seios/Marshall, seios/Cassidy.",
    "Variável trocada: Jupy Hydration → Natural Rems Sea Moss; \"health expert, 25 years of practice\" → autoridade de ofício com alga (nada médico); estúdio de podcast → cenário fixo da conta; emissora real → telejornal de emissora INVENTADA, sem logo real (decisão do Luigi, 2026-10-13); ingredientes só do rótulo (sem potássio e magnésio do doc).",
    "Funil: VENDA. Frasco em quadro de T15 até o fim. Comment `yes` antes da Amazon (oferece a rotina da manhã no próximo vídeo, sem DM), \"Search Natural Rems Sea Moss on Amazon\", Stories e bio, follow como última frase. Legenda: `#ad #syntheticperformer #naturalrems` no topo, sem link.",
    f"Enquadramento: T1 = âncora de telejornal num estúdio com skyline à noite, imagem de choque no quadro ao lado. T2 em diante = {nome} no cenário fixo da conta ({cen}), câmera de celular na altura do peito, plano único como o modelo; frasco na mão colado na lente de T15 a T21.",
    "Divisão dos takes: modelo = 1 plano de telejornal (0 a ~7,8s) + 1 plano único de fala até o fim; o plano longo dividido só em fim de frase. T21 = CENA CURTA (a última frase do modelo também é curta).\n",
    "## Tabela de esqueleto preservado\n","| # | Beat | Original | Adaptado |","|---|---|---|---|"]
    orig={"rins":["Breaking news in New York... most poisonous drink for the kidneys","not alcohol, not energy drinks, not apple or orange juice","probably sitting in your fridge right now","not your fault, you were manipulated","Watch this carefully","chemical factory, artificial sweeteners, toxin","inflammation, kidneys work overtime","how much stress on the kidneys","it's diet soda, zero sugar, diet cola","don't give clean energy, steal from your future","fight or flight drains you","fix the root cause: your metabolism","metabolism slows, fluid balance, stubborn weight","belly keeps growing","25 years of working with my clients, one thing","electrolytes, ginger, turmeric... Jupy Hydration","easy to make, refreshing","shouldn't mean a cabinet full of ingredients","comment Jupy, I'll send you the routine","search on Amazon, link in bio and comments","follow me first"],
          "seios":["Breaking news in New York... most poisonous food for your breasts","not burgers, not pizza, not ice cream","hiding in your fridge","not your fault, manipulated by the media","(ordem implícita)","hormones and growth factors, inflammation","attacks collagen and connective tissue","antibiotics, excess estrogen","calcium barely absorbs","it is any kind of dairy","collagen breaks down, tissue thins and sags","no bra, no weight loss, avoid tops, mirror","blame yourself, not gravity or aging","good news, right support","I have found one simple way","turmeric, vitamin C, electrolytes... Jupy Hydration","supporting your skin from the inside out","(implícito)","comment JUPY, I'll send the protocol","search on Amazon, link in caption/comments/profile","follow me"]}[t]
    for i,(e,p) in enumerate(takes,1):
        L.append(f"| {i} | {B[t][i-1]} | {orig[i-1]} | {e[:70]}{'…' if len(e)>70 else ''} |")
    L+=["\n## Setups de cena\n",
        "- **Setup A (T1):** telejornal de emissora inventada. Âncora de TV (mulher ~45, blazer) na bancada, skyline noturno de cidade ao fundo, faixa \"BREAKING NEWS\" e caixa de imagem ao lado dela com a imagem de choque do tema"+(" (rim em corte com pedra escura, a definir no K com segurança)" if t=="rins" else " (dois cocos verdes no tronco do coqueiro, como no modelo)")+". Texto de tela de abertura no CapCut.",
        f"- **Setup B (T2 a T14):** {nome} no cenário fixo da conta, sem frasco, mãos gesticulando (dedo indicador como no modelo).",
        f"- **Setup C (T15 a T21):** {nome} no mesmo plano, segurando o frasco do Natural Rems Sea Moss colado na lente, rótulo legível, parado do T20 ao T21.\n",
        "## Roteiro cena a cena (takes)\n"]
    for i,(e,p) in enumerate(takes,1):
        n=len(re.findall(r"[A-Za-z0-9']+",e)); cur=" · CENA CURTA" if i==21 else ""
        L+=[f"### T{i} · {B[t][i-1]} · TALKING · Setup {setup(i)}{cur}\n",f"> \"{e}\"\n",f"PT: {p}\n",f"Palavras: {n}\n"]
    L+=["## Roteiro só-fala (inglês, pra TTS)\n"," ".join(e for e,p in takes)+"\n",
        "## Notas de produção\n",
        "- Duração prevista: 21 takes de até 8s (~165s), igual ao modelo (~170s). Se ficar longo, cortar primeiro T5 (ordem de assistir) e T18 (custo).",
        "- T1 é falado pela ÂNCORA (2ª pessoa), não pela avatar. \"she\" = a avatar.",
        "- Emissora inventada, sem logo nem nome de rede real; nada imita jornal existente.",
        "- Compliance: nenhum médico, clínica ou credencial; autoridade é o ofício com alga. Nenhuma promessa de resultado do produto; o produto só ecoa o rótulo (supports energy, skin & gut health). O mecanismo fala do vilão (refrigerante diet / laticínio), não do produto.",
        "- Claim mais arriscado: "+("\"toxin\" e \"kidneys work overtime\" sobre o refrigerante diet (opinião sobre categoria, sem marca)." if t=="rins" else "o bloco de colágeno e seios: fica no vilão; no produto só \"vitamin C supports normal collagen formation\" e \"supporting your skin\". Nunca firmar, levantar ou devolver o peito."),
        "- Risco de moderação: palavra \"breasts\" no T1 e T2; \"chest\" no resto." if t=="seios" else "- Risco de moderação no K1: imagem de órgão. Se travar, trocar por lata de refrigerante diet efervescendo (decidir no pacote).",
        "- Ordem do CTA da marca (comment antes da Amazon, follow por último) prevalece sobre a ordem do doc do Lucas.",""]
    open(f"{d}/ROTEIRO.md","w").write("\n".join(L)); print(d)
