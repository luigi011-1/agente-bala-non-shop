# Homologação 0.7.0 — pipeline único, imagens no Chrome

Status: implementado, não homologado em produção real. 37 testes Python + 11 da extensão
passam com provedores simulados. Testes de software não comprovam qualidade visual.

A 0.7.0 removeu o caminho de API de imagem, o modo de lote e o console manual. O modelo
de dados agora é **um projeto = um roteiro + N avatares**; não há mais migração dos
projetos antigos (status `plan_ready` etc. em `data/`), que podem ser ignorados ou
apagados.

## Roteiro de homologação

1. Abrir `Iniciar Auraly Studio.cmd`. Confirmar `/api/config` com `version` `0.7.0`.
   Encerrar qualquer servidor 0.6.0 antes (o inicializador avisa).
2. **Nova produção** com um `.mp4` curto (30–60 s). Rodar **/watch** e conferir a
   contagem de frames e a transcrição.
3. **Analisar**. Conferir herói, timestamps e ação de abertura contra o vídeo. Não
   aprovar com ambiguidade em aberto.
4. **Roteiro**: conferir 222 antes de Stories, 13–29 palavras por take, EN + PT, oferta
   verdadeira. Testar **Ajustar a copy** com uma instrução curta e reaprovar.
5. **Ganchos**: escolher 3. Confirmar que o texto não nomeia avatar.
6. **Conjunto de imagens** monta sozinho: conferir K01/K02/K03 (um por gancho), BODY e
   CTA; cada prompt cita o kit de cena, a bandeira e "sem legendas", e manda pôr a carta
   da mesa na mão dela.
7. **Avatares**: subir 2 `.jpeg`. Confirmar 2 avatares e, ao **Preparar fila**, 10 jobs
   (2 × 5). O seletor "Piloto: primeiras 2" limita a inclusão a 2 frames por avatar.
8. Carregar `studio/chrome-extension` em `chrome://extensions` (Modo do desenvolvedor →
   Carregar sem compactação), abrir **Conectar o Chrome**, colar o código. Aguardar
   **Chrome conectado**.
9. Simultaneidade 1, **Iniciar / retomar**. Após o primeiro envio confirmado, **Pausar**
   e aguardar a imagem. Não há reenvio automático de envio incerto.
10. Revisar a imagem em tamanho completo: identidade, mãos, carta, cenário, continuidade,
    estado inicial. **Aprovar imagem** ou **Gerar nova tentativa** (preserva o arquivo
    anterior, refaz só aquele avatar+cena).
11. Gerar o restante de um avatar, **Baixar pacote**. Conferir `imagens/*`, `ancora/`,
    `ROTEIRO.md` bilíngue, `PROMPTS_PRODUCAO.md`, `FLOW_PROMPTS.txt` com a fala exata por
    take e `manifest.json` com `source: chatgpt-chrome` e o nome do avatar.
12. Testar um clipe manualmente no Flow; registrar qualidade, duração e correções.

Critério de aceitação: nenhum defeito bloqueador de identidade, anatomia, carta, copy ou
continuidade; nenhuma geração duplicada inesperada; ZIP completo por avatar; ações
executáveis no Flow. Falhou: registrar causa e corrigir antes de aumentar volume.
