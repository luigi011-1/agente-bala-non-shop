# flow_ui: automação do Flow pela interface web (Playwright)

Faz o trabalho manual dentro do Flow no seu Chrome logado, sem o agente do Flow. ESQUELETO: os seletores
em `seletores.json` são palpites e precisam ser calibrados na tela real (comando `calibrar`).

Setup único (Mac): `pip install playwright` e `playwright install chromium`. Chrome instalado.
1. `python flow_ui/flow_ui.py login` (loga no Flow; a sessão fica em ~/.flow_ui_perfil)
2. `python flow_ui/flow_ui.py calibrar` (gera calibragem.json e prints; ajustar seletores.json)
3. `imagens ENTREGA.md --saida out/x --anexo sheet.jpg --frames frames_modelo/`: por K, modelo Nano Banana 2, x4, 9:16, baixa as 4 como K01-1..4.
4. `escolher --saida out/x`: página em http://localhost:8765, 1 clique por K.
5. `videos ENTREGA.md --saida out/x --perfil auraly|classico`: por V, frame inicial = imagem escolhida, 1 saída, modelo do perfil, baixa V01.mp4.
6. `status` e `refaz ENTREGA.md --saida out/x [K03 V05]` (sem códigos: só os FALHOU).

Falha repete o MESMO prompt até 3 vezes; moderação ou seletor não achado vira BLOQUEADO e segue. Estado em estado.json.
