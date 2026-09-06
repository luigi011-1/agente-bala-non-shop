# Homologação 0.6.0 — Chrome e pacote Flow

Status: extensão instalada, recarregada e conectada em 2026-09-06. O primeiro piloto parou antes do envio em Casey K02 e Robin K01 com “A aba saiu do ChatGPT”. Causa: URL ainda não confirmada na aba recém-aberta. Corrigido `waitTab` para aguardar o carregamento sem aceitar navegação externa; 11 testes da extensão passaram. Depois do reload, Casey K02–K05 foram geradas em sequência pelo Chrome, salvas automaticamente, revisadas e exportadas no pacote `auraly-chrome-flow.zip`. Fila pausada. Robin K01 permanece em atenção como pendência isolada; o prompt dela não foi enviado nesse erro antigo.

1. Abrir `Iniciar Auraly Studio.cmd` e entrar em **Gerar no meu Chrome**, ou acessar `http://127.0.0.1:8766/browser` no Chrome. O servidor deve estar na versão 0.6.0.
2. No Chrome com o ChatGPT conectado, abrir `chrome://extensions`, ativar **Modo do desenvolvedor**, clicar **Carregar sem compactação** e selecionar a pasta `studio/chrome-extension` deste projeto.
3. No Studio, expandir **Conectar o Chrome pela primeira vez** e clicar **Mostrar pasta e código**. Colar o código somente na extensão Auraly, em **Código de conexão local**, e clicar **Conectar**. Aguardar **Chrome conectado** no Studio.
4. Conferir os prompts da fila existente antes de retomar. Há uma imagem Casey já salva e tarefas de Casey/Robin pendentes. O seletor “Piloto: primeiras 2” limita novas inclusões; não reduz uma fila que já contém todas as cenas.
5. Para o primeiro teste, selecionar simultaneidade 1 e clicar **Iniciar / retomar**. Pausar novos envios após o primeiro envio confirmado e aguardar a imagem. Não haverá repetição automática de envio incerto.
6. Conferir a imagem salva em tamanho completo, identidade, anatomia, carta, cenário, continuidade e estado inicial. **Aprovar imagem** registra a decisão; **Gerar nova tentativa** preserva o arquivo anterior. Erros oferecem consulta da conversa sem reenvio.
7. Após validar o piloto, retomar as cenas restantes. Para um pacote completo, todas as cenas do plano precisam estar geradas e aprovadas; referências isoladas de objetos são dispensadas no modo Chrome.
8. Baixar o pacote na seção **Pacotes para o Flow**. Conferir imagens, âncora, `ROTEIRO.md`, `PROMPTS_PRODUCAO.md`, `FLOW_PROMPTS.txt`, prompts individuais e `manifest.json`.
9. Testar um clipe manualmente no Flow; registrar qualidade, duração e correções. A homologação do Studio 0.6.0 para imagens e ZIP do Chrome passou com a Casey; o aproveitamento final dos vídeos depende do teste manual no Flow.

## Histórico: homologação 0.3.0 por API

Status: preparado, não executado. Não confundir testes simulados com aprovação visual.

1. Encerrar o servidor antigo quando não houver produção em andamento; abrir pelo atalho. Confirmar /api/config com version 0.3.0 e key_storage Windows DPAPI.
2. Confirmar que os três projetos anteriores continuam presentes. Nunca incluir preferences.json em entregas ou compartilhar suas credenciais.
3. Escolher um único vídeo já extraído. Confirmar fornecedor, limites cumulativos e autorização para uploads temporários se for usar Kie.ai. Custos pertencem às contas de API; o limite de chamadas não é teto monetário.
4. Executar análise. Conferir herói, timestamps e ação de abertura contra o vídeo original; não aprovar se houver ambiguidade não resolvida.
5. Gerar roteiro; conferir fidelidade dos beats, 222 antes de Stories, 13–29 palavras por take, veracidade da oferta e ausência de promessas não sustentadas.
6. Aprovar um único gancho e revisar o plano. Usar o número de frames planejados para limitar o lote inicial; expansões de tentativas requerem decisão explícita.
7. Gerar e revisar referência, gancho, corpo e CTA. Conferir identidade, mãos, texto SOULMATE, sete elementos de cenário, continuidade e estado anterior à ação. Registrar defeitos, sem aprovar apenas porque o revisor automático aprovou.
8. Baixar ZIP e conferir todos os arquivos e a fala exata nos prompts. Gerar os clipes manualmente no Flow e avaliar se a ação e a duração funcionam.

Registrar por etapa: fornecedor/modelo efetivo no histórico, quantidade de chamadas, tempo, custo observado na conta, correções manuais e resultado no Flow. Comparar lotes usando a mesma referência; não declarar equivalência entre provedores sem essa evidência.

Critério de aceitação: nenhum defeito bloqueador de identidade, anatomia, carta, copy ou continuidade; nenhuma geração duplicada inesperada; export completo; ações executáveis no Flow. Se falhar, registrar causa e corrigir antes de aumentar volume.
