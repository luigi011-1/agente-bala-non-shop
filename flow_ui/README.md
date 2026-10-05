# flow_ui: automação do Flow pela interface web (Playwright)

Faz o trabalho manual dentro do Flow no seu Chrome logado, sem o agente do Flow. Seletores CALIBRADOS no Flow real (2026-10-05, flow.google.com). Se o Google mudar a tela, rode `calibrar` e ajuste `seletores.json`.

Setup único (Mac): `bash flow_ui/setup.sh` (instala Playwright). Chrome instalado.
1. `python3 flow_ui/flow_ui.py login` (abre o Chrome com perfil próprio ~/.flow_ui_perfil, porta 9222; logue uma vez, a sessão fica salva)
2. `python flow_ui/flow_ui.py calibrar` (gera calibragem.json e prints; ajustar seletores.json)
3. `imagens ENTREGA.md --saida out/x --anexo sheet.jpg --frames frames_modelo/`: por K, modelo Nano Banana 2, x4, 9:16, baixa as 4 como K01-1..4.
4. `escolher --saida out/x`: página em http://localhost:8765, 1 clique por K.
5. `videos ENTREGA.md --saida out/x --perfil auraly|classico`: por V, frame inicial = imagem escolhida, 1 saída, modelo do perfil, baixa V01.mp4.
6. `status` e `refaz ENTREGA.md --saida out/x [K03 V05]` (sem códigos: só os FALHOU).

Falha repete o MESMO prompt até 3 vezes; moderação ou seletor não achado vira BLOQUEADO e segue. Estado em estado.json.

Notas da calibragem: botão Agent fica desligado (sem agente do Flow). Imagem: modelo `Nano Banana 2.1` (não existe 'Nano Banana 2' no menu: Pro, 2 Lite, 2.1), 9:16, x4, download pela URL direta do tile (JPG 768x1376). Vídeo: modo Frames, frame inicial = botão Start, 9:16, x1, 720p 8s; classico = `Omni 1.1 Flash`, auraly = `Veo 3.1 - Lite` (o menu não mostra 'Lower Priority'). Todos os arquivos anexados são enviados com nome único. `--projeto URL` reaproveita um projeto; sem ele usa a aba atual ou cria um novo.
