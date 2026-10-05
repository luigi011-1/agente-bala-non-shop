# flow_api: gerar K e V pela API do Google (protótipo)

Substitui o agente do Flow. 4 imagens por K, 1 vídeo por V, sempre 9:16, estado em `estado.json`.

Setup (Mac): `pip install google-genai` e `GEMINI_API_KEY=...` em `flow_api/.env` (não commitar) ou no ambiente.
Chave em aistudio.google.com com cobrança ativada.

1. `python flow_api/flow_api.py imagens ENTREGA.md --saida out/x --anexo sheet.jpg --frames frames_modelo/`
   (frames: `K01_modelo.png`... ; anexos de FitWell/Sea Moss: a âncora; produto: `--anexo foto.png`)
2. `python flow_api/flow_api.py escolher --saida out/x` e abrir http://localhost:8765 (1 clique por K, salvar)
3. `python flow_api/flow_api.py videos ENTREGA.md --saida out/x`
4. `status` mostra a tabela; `refaz ENTREGA.md --saida out/x` repete só os FALHOU (ou `refaz ... K03 V05`).

Falha de geração repete até 3 tentativas; recusa de moderação vira BLOQUEADO e segue, sem reescrever prompt.
Modelos configuráveis: `FLOW_MODELO_IMG` (padrão gemini-3.1-flash-image) e `FLOW_MODELO_VID`
(padrão veo-3.1-lite-generate-preview, id NÃO confirmado; se der erro de modelo, trocar por
veo-3.1-fast-generate-preview ou veo-3.1-generate-preview).
Não testado contra a API real (sem chave no ambiente de desenvolvimento).
