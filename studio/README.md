# Auraly Studio · 0.6.0

## Revisão e pacote do Chrome

Em **Gerar no meu Chrome**, cada imagem salva agora tem prévia, abertura em tamanho completo e **Aprovar imagem**. **Gerar nova tentativa** preserva o arquivo anterior e prepara somente aquela cena, sem ampliar um piloto para o projeto inteiro. Tarefas em atenção oferecem **Verificar resultado sem reenviar** e **Autorizar novo envio**; uma nova tentativa usa outra aba e preserva a conversa incerta.

Após gerar e aprovar todas as cenas do plano (exceto referências isoladas de objetos), **Baixar pacote completo** entrega um ZIP com imagens no formato original, âncora, prompts exatos de imagem, roteiro, prompts de vídeo e manifest com hashes e aprovações. Arquivo, plano ou âncora alterados invalidam a exportação. O pacote identifica a origem como ChatGPT Chrome; não presume qual modelo foi usado pela interface.

Validação 0.6.0: 53 testes Python e 11 testes da extensão. Extensão instalada, recarregada e conectada no perfil real. O primeiro piloto detectou uma condição de corrida: uma aba recém-criada pode não ter URL confirmada ainda. A espera foi corrigida e recebeu quatro testes; depois do reload, a Casey gerou K02-K05 em sequência pelo ChatGPT no Chrome, salvou os arquivos automaticamente, passou pela revisão e exportou `auraly-chrome-flow.zip`. Robin K01 ficou em atenção pelo erro antigo, sem envio de prompt. Veja `PILOTO.md` para a retomada atual.

## Janela Windows e ChatGPT no Chrome (piloto)

O inicializador agora abre uma janela própria com WebView2, preservando a interface e o servidor local. O ChatGPT continua no Chrome do usuário, com o perfil e login existentes. Não copie perfis, cookies ou credenciais. Implementação de janela baseada na API oficial: https://pywebview.flowrl.com/api/.

Em **Gerar no meu Chrome**, selecione produções com plano pronto, prepare a fila e escolha até quatro avatares simultâneos. O padrão é um piloto com as primeiras duas cenas por avatar. A fila pula referências isoladas de objetos: usa a descrição textual do objeto e anexa somente a âncora original. Dependências entre cenas são incluídas como contexto textual completo. Prompts preparados ficam disponíveis para revisão antes de Iniciar.

Para execução independente deste chat, carregue `studio/chrome-extension` como extensão sem compactação em `chrome://extensions`, no perfil do Chrome que contém sua sessão Plus. Abra a extensão Auraly Studio e cole o código local exibido em **Conectar o Chrome pela primeira vez**. A extensão atua na interface renderizada do ChatGPT; não usa endpoints privados nem chaves de API. A instalação/ativação precisa ser feita pelo usuário quando a política de controle do navegador bloquear páginas internas do Chrome.

As permissões da extensão abrangem apenas ChatGPT, imagens em oaiusercontent.com, servidor 127.0.0.1:8766, armazenamento da conexão local e temporizador. O código local dá acesso à fila de prompts, âncoras e recebimento de resultados; não é senha do ChatGPT. Não compartilhe o código. Mantenha o servidor e o Chrome abertos. O service worker consulta a fila a cada 5 segundos enquanto ativo e é reativado pelo Chrome a cada 30 segundos.

Os resultados são preservados em `Downloads/Auraly Studio/Avatar_DATA/ID-PRODUCAO/`, com número da cena, keyframe e identificador da tentativa, extensão real PNG/JPEG/WebP, prompt e manifest com hashes. Não monitora o “último download” e não move arquivos alheios. Gerar e salvar não equivale a aprovação automática: revise as imagens na fila. O modo Chrome tem revisão e ZIP próprios, sem modificar as imagens do pipeline de API.

Pausar impede novos envios; imagens já enviadas podem terminar e ser recebidas. Reiniciar o servidor pausa a fila, preservando abas e conversas. Envios incertos não são repetidos automaticamente. Limites do ChatGPT, login, mudanças de interface e abas alteradas podem exigir intervenção. A qualidade e a cota do plano não são garantidas pelo software. A extensão foi homologada ponta a ponta no perfil real para um pacote completo da Casey; novos avatares ainda devem ser revisados imagem por imagem.

Validação: `studio/.venv/Scripts/python.exe -m unittest studio.test_browser_queue studio.test_studio studio.test_providers studio.test_batches -q`. Os testes da fila são locais, sem chamadas de geração. Registros das versões anteriores abaixo descrevem o pipeline de API.

## Novo: lotes e fornecedores de análise

Depois de concluir /watch, use **Aprovar análise para lote**, selecione até quatro avatares cadastrados e 1–5 ganchos por avatar. **Criar lote e preparar roteiros** reutiliza a análise e cria projetos isolados por avatar. Revise cada roteiro; **Autorizar produção / retomar lote** aprova os roteiros atuais, seleciona os primeiros ganchos por congruência e avança até as imagens/ZIP, parando em erros ou revisão manual necessária. Os dois workers existentes limitam a concorrência global a dois projetos. Uma falha de avatar não cancela os demais.

Os limites iniciais são 100 chamadas de texto e 32 de imagem POR AVATAR, cumulativos; quatro avatares podem consumir até 400 chamadas de texto e 128 de imagem nesses limites. Não há teto monetário. Cada tentativa HTTP conta; resultados incertos não são reenviados automaticamente. Reinícios preservam a fila, mas exigem **Retomar** para autorizar sua execução novamente.

Em Conexão, escolha Automático, somente OpenAI, somente Google Gemini ou somente Kie.ai Gemini. Automático usa OpenAI → Google → Kie.ai quando as chaves estão configuradas; mantém o fornecedor alternativo no projeto para não insistir no fornecedor recusado a cada grade. Seleção explícita substitui essa preferência. HTTP 502/503/504 de texto têm até três tentativas, com espera exponencial e variação aleatória, respeitando Retry-After numérico até 120s; pausas interrompem a espera. HTTP 429 troca de provedor, sem repetir cegamente uma possível recusa financeira. Códigos e detalhes de erro OpenAI são guardados sem credenciais.

Kie.ai: endpoint documentado /gemini-3-5-flash-openai/v1/chat/completions, identificador gemini-3-5-flash-thinking. O adaptador envia imagens inline em data URLs, sem tmpfiles para análise, e aceita retorno choices ou candidates. Integração testada com respostas simuladas; suporte efetivo a data URLs, cobrança, capacidade e qualidade ainda precisam de homologação real. A documentação confirma entrada de imagens, mas seus exemplos usam URLs HTTPS. Nenhuma garantia de capacidade independente da Google. Referência: https://docs.kie.ai/market/gemini/gemini-3-5-flash-openai

Validação 0.4.0: 36 testes locais; comando: studio/.venv/Scripts/python.exe -m unittest studio.test_studio studio.test_providers studio.test_batches -v. Nenhuma chamada paga feita nesta atualização.

As seções abaixo descrevem a base 0.3.0; as regras de fornecedores e retentativas desta seção prevalecem.

Programa local: MP4 → /watch → aprovação da análise → roteiro → aprovação → ganchos → plano → imagens revisadas → ZIP para Flow / Omni Flash.

## Iniciar

Abra Iniciar Auraly Studio.cmd ou o atalho da área de trabalho. O servidor usa http://127.0.0.1:8766. Fechar a aba não encerra o servidor. O inicializador identifica versões anteriores e pede seu encerramento antes da atualização.

## Conexão, privacidade e cobrança

- Padrão OpenAI: gpt-6-astra com reasoning.effort=medium; imagens gpt-image-2 em PNG, alta qualidade, 1152×2048.
- Sem chave OpenAI, Gemini pode executar análise, roteiro, ganchos, plano e revisão; Kie.ai pode gerar imagens. Uma geração completa também requer um provedor de texto para revisão.
- Com OpenAI configurada, o fallback ocorre somente após resposta HTTP 429: Gemini para texto e Kie.ai para imagem. 401, 404 e erros de transporte não ativam fallback. Não presumimos que todo 429 signifique falta de crédito.
- Gemini está configurado como gemini-3.5-flash, sem equivalência garantida ao raciocínio médio do Astra. A disponibilidade real depende da conta e não foi homologada nesta atualização.
- Kie.ai usa os identificadores gpt-image-2-text-to-image / gpt-image-2-image-to-image, 9:16, 2K. Cobrança e qualidade dependem do serviço. Não existe promessa de gratuidade.
- As chaves são salvas protegidas por Windows DPAPI, vinculadas ao usuário Windows atual. O arquivo não é portável entre usuários/máquinas. Isso não protege contra programas maliciosos executados como o mesmo usuário.
- Preferências legadas são migradas no início: valores legíveis são substituídos pelo bloco protegido, sem criar backup legível. Cópias antigas e chaves já publicadas devem ser tratadas separadamente.
- Desconectar limpa as três conexões e os valores salvos. Não altera variáveis de ambiente do sistema.
- O vídeo original permanece local. Frames, transcrição e documentos do projeto são enviados ao provedor de análise. A geração recebe prompts e referências.
- Edições pela Kie.ai exigem autorização explícita no painel para enviar referências ao tmpfiles.org. Os links externos são repassados à Kie.ai; o Studio não controla a remoção no serviço. Uploads são bloqueados antes do envio quando há pausa, falta de autorização ou limite esgotado.
- Verificar catálogo OpenAI consulta somente OpenAI, sem geração. Não valida Gemini, Kie.ai, saldo nem qualidade. Nenhuma chave é devolvida pela API local ou incluída intencionalmente nos exports.

## Controle e recuperação

Chamadas de imagem incluem OpenAI e Kie.ai, inclusive histórico anterior kie/images. Limites são cumulativos por projeto: padrão 100 texto e 32 imagem, não orçamento monetário. Falhas e chamadas incertas contam. Gemini não faz retentativas automáticas de 503; o operador controla a retomada.

Pausa impede novas gerações; trabalho já enviado pode continuar e ser cobrado. Kie.ai salva task_id imediatamente após a criação. Em caso de interrupção, Retomar lote consulta essa tarefa e recupera a imagem sem criar outra geração, mesmo com o limite de geração atingido. A imagem recuperada requer aprovação visual manual. Se a criação foi enviada mas nenhum identificador chegou, não há recuperação garantida: confira a conta antes de autorizar outra tentativa. Tarefas antigas sem identificador salvo não podem ser reconstruídas.

## Produção

- Extração local por FFmpeg e faster-whisper: cenas, 5 fps, áudio, transcrição e grades.
- Análise percorre todas as grades, primeiros 8 segundos em frames originais e janelas dos eventos indicados.
- Cada projeto recebe snapshot dos documentos, skills e referências com hashes.
- Regras editoriais de Auraly e prompts de ganchos preservados nesta atualização.
- Aprovações de análise, roteiro, ganchos e geração continuam explícitas.
- Âncora original acompanha cenas e edições; corpo e CTA são compartilhados entre hooks.
- Revisão automática por critérios; até duas tentativas por frame, com autorização para tentativas adicionais.
- ZIP contém imagens aprovadas, roteiro, prompts de imagem/vídeo, análise e manifest.
- O aplicativo não gera vídeos no Flow e não publica conteúdo.

## Testes e homologação

Execute: studio/.venv/Scripts/python.exe -m unittest studio.test_studio studio.test_providers -v

28 testes locais aprovados nesta atualização, com provedores simulados e pastas temporárias. Incluem proteção/migração de credenciais, desconexão dos valores salvos, roteamento Gemini, fallback HTTP tipado, limite Kie.ai, consentimento/pausa de uploads e recuperação de tarefa sem novo POST.

Nenhuma chamada paga foi executada nesta atualização. Lote real pequeno ainda é necessário para validar acesso aos provedores, custo, identidade, ações, continuidade e aproveitamento no Flow. Testes de software não comprovam qualidade visual.

Ainda pendentes: análise adaptativa a 15 fps, integração completa de checar_entrega.py, revisão editorial integral, memória entre projetos, orçamento monetário e comparação global de continuidade.

Referência oficial para tratamento de erros: https://developers.openai.com/api/docs/guides/error-codes
