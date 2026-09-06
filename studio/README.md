# Auraly Studio · 0.7.0

Um pipeline só, do vídeo modelo ao pacote pro Flow, com a geração de imagem feita por
você no ChatGPT do Chrome. O caminho de API de imagem (OpenAI GPT Image 2 / Kie.ai), o
modo de lote e o console manual foram removidos nesta versão.

## O fluxo

1. **Nova produção**: só o vídeo `.mp4` (nome + direção opcional). Sem escolher avatar.
2. **/watch**: extração local por FFmpeg e faster-whisper — cenas, timeline 5 fps, áudio
   e transcrição.
3. **Análise**: percorre todas as grades, primeiros 8 s em frames originais e as janelas
   dos eventos indicados; entrega herói do hook, beats e dúvidas.
4. **Roteiro bilíngue**: copy EN + PT modelada da referência com a doutrina do Ângulo 3
   para vender o app Auraly. **Sem avatar nesta etapa.** Botões: **Aprovar roteiro** e
   **Ajustar a copy** (reescreve com a sua instrução, mantendo toda a doutrina).
5. **Ganchos visuais**: o Studio sugere 8–10, você escolhe até 5. Os ganchos escolhidos
   valem para **todos** os avatares.
6. **Conjunto de imagens**: uma chamada de IA monta, por avatar, uma imagem por gancho
   escolhido (take T1) + uma imagem de BODY + uma de CTA. **Sem REF-CARTA isolada** — a
   carta SOULMATE já está na mesa em toda foto-âncora; o prompt põe o mesmo modelo na
   mão dela.
7. **Avatares**: suba N arquivos `.jpeg` na própria tela. Cada arquivo é um avatar. Sem
   pré-cadastro. Ex.: 4 avatares × 3 ganchos = 12 imagens de gancho + 4 BODY + 4 CTA.
8. **Produção no Chrome**: a fila roda no seu ChatGPT, **uma aba por avatar**, só a
   âncora daquele avatar anexada. Uma pasta por produção em
   `Downloads/Auraly Studio/<data>_<produção>_<id>/`, e dentro dela **uma subpasta por
   avatar** com as imagens, o `manifest.json` e um `PROMPTS_VIDEO_VEO.txt` (prompts de
   vídeo para o Veo 3.1, um por take, na estrutura de cinco blocos, a partir do roteiro
   final). As imagens são revisadas imagem por imagem, e **Baixar pacote** entrega um ZIP
   por avatar (imagens no formato real, âncora, `ROTEIRO.md` bilíngue,
   `PROMPTS_PRODUCAO.md`, `PROMPTS_VIDEO_VEO.txt`, `manifest.json` com
   `source: chatgpt-chrome`).

Pausar impede novos envios; imagens já enviadas podem terminar e ser recebidas.
Reiniciar o servidor pausa a fila, preservando abas e conversas. Envios incertos não são
reenviados automaticamente. Limites do ChatGPT, login e mudanças de interface podem
exigir intervenção. A qualidade e a cota do plano não são garantidas pelo software.

## Extensão do Chrome

Carregue `studio/chrome-extension` sem compactação em `chrome://extensions`, no perfil
que contém sua sessão Plus. Abra **Conectar o Chrome** no Studio, cole o código local na
extensão. A extensão atua só na interface renderizada do ChatGPT — sem endpoints
privados, sem chave de API, sem cookies. Permissões: ChatGPT, imagens em
`oaiusercontent.com`, servidor `127.0.0.1:8766`, armazenamento local e temporizador. O
service worker consulta a fila a cada 5 s e é reativado pelo Chrome a cada 30 s. A aba de
cada avatar é chaveada por produção + avatar, então dois projetos não disputam a mesma
aba.

## Conexão, privacidade e cobrança

- Análise, roteiro, ganchos e conjunto de imagens usam **texto**: OpenAI (`gpt-6-astra`,
  raciocínio configurável) com fallback para Google Gemini (`gemini-3.5-flash`) apenas
  em HTTP 429 tipado. 401/404 e erros de transporte não ativam fallback.
- **Não há geração de imagem por API.** As imagens são geradas por você no ChatGPT.
- As chaves são salvas protegidas por Windows DPAPI, vinculadas ao usuário atual. O
  arquivo não é portável entre usuários/máquinas. Desconectar limpa as duas conexões e
  os valores salvos.
- Preferências legadas são migradas no início: valores legíveis são substituídos pelo
  bloco protegido, sem backup legível.
- O vídeo original fica local. Frames, transcrição e documentos vão ao provedor de
  texto. **Verificar catálogo OpenAI** consulta só o modelo de texto, sem geração.
- Limite cumulativo por projeto: chamadas de texto (padrão 200). Não é orçamento
  monetário; conta chamadas enviadas, inclusive falhas.

## Iniciar

`Iniciar Auraly Studio.cmd` ou o atalho. O servidor usa `http://127.0.0.1:8766` e abre
numa janela WebView2. Fechar a janela não encerra o servidor. O inicializador identifica
versões anteriores e pede o encerramento antes da atualização.

## Testes

```
studio/.venv/Scripts/python.exe -m unittest studio.test_browser_queue studio.test_studio studio.test_providers -q
node studio/chrome-extension/background.test.cjs
node studio/chrome-extension/content.test.cjs
```

37 testes Python + 11 da extensão. Os testes da fila são locais, sem chamadas de
geração. Testes de software não comprovam qualidade visual: um lote real pequeno ainda é
necessário para validar acesso, custo, continuidade e aproveitamento no Flow.

## Escopo

Termina nas imagens e nos prompts de vídeo. Geração de vídeo no Flow, publicação e
automação de DM/Stories não fazem parte da execução automática do Studio.

Referência oficial para tratamento de erros:
https://developers.openai.com/api/docs/guides/error-codes
