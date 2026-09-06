# Evolução do Auraly Studio

## Atualização 0.7.0 — 2026-09-06

- Pedido do Luigi: um pipeline único, linear, com a geração feita por ele no ChatGPT do
  Chrome. Fim do caminho de API de imagem.
- **Removidos**: geração/edição de imagem OpenAI, todo o adaptador Kie.ai (imagem e
  texto), upload tmpfiles, `engine.generate`/`engine.plan`, `batches.py` e o modo de
  lote, `console.py` e a página `/console`, o registro fixo de avatares (`AVATARS`).
- **Fluxo novo**: upload só do `.mp4` → /watch → análise → **roteiro bilíngue
  avatar-agnóstico** (com "Ajustar a copy") → **ganchos** (escolher até 5, valem para
  todos) → **conjunto de imagens** (`engine.imageset`: 1 por gancho + BODY + CTA, sem
  REF-CARTA) → **subir N âncoras .jpeg na própria tela** → fila do Chrome, uma aba por
  avatar.
- `browser_queue` agora fan-out por `(projeto, avatar, frame)`; âncora por avatar,
  `avatar_key` = produção+avatar, ZIP por avatar. `standalone_prompt` simplificado:
  único anexo é a âncora, e a carta da mesa entra na mão dela.
- Downloads: uma pasta por produção (`<data>_<título>_<id>`), com uma subpasta por
  avatar contendo as imagens e um `PROMPTS_VIDEO_VEO.txt` (um prompt por take, cinco
  blocos, Veo 3.1, do roteiro final). O ZIP por avatar carrega os mesmos arquivos.
- Só texto: OpenAI Astra com fallback Gemini em 429 tipado. Limite por projeto vira só
  chamadas de texto (padrão 200).
- 37 testes Python + 11 da extensão aprovados. Sem chamada paga nesta atualização.
- Próximo passo: rodar uma produção real pequena ponta a ponta (vídeo → roteiro → 2
  avatares → ZIP) e testar os clipes manualmente no Flow.

## Atualização 0.6.0 — 2026-09-06

- Prioridade confirmada por Luigi nesta sessão: finalizar a geração pelo ChatGPT no Chrome e o pacote para Flow.
- Prévia e aprovação por imagem na fila, recuperação de envios incertos visível e nova tentativa preservando resultados anteriores.
- ZIP próprio do Chrome com imagens no formato real, âncora, roteiro, prompts de imagem/vídeo e manifest; exige todas as cenas aprovadas e arquivos/âncora/plano consistentes.
- 53 testes Python e 11 testes JavaScript aprovados. Extensão instalada, recarregada e conectada por Luigi; o piloto real da Casey gerou K02-K05 em sequência pelo ChatGPT no Chrome, recebeu os arquivos automaticamente e preservou a fila sem envio duplicado.
- Estado atual: Casey com K01-K05 geradas, aprovadas para piloto e exportadas em `auraly-chrome-flow.zip`; Robin K01 permanece em atenção pelo erro antigo de URL antes do envio, bloqueando apenas a fila da Robin. Shelby e Kris seguem com planos prontos.
- Próximo passo: testar clipes da Casey manualmente no Flow, registrar aproveitamento de ação/duração e depois retomar a Robin com uma nova tentativa no Chrome. A geração de clipes no Flow permanece manual.

## Atualização 0.4.0

- Lotes a partir de análise aprovada: até quatro avatares, 1–5 hooks cada, scripts preparados juntos e produção autorizada em conjunto.
- Concorrência global limitada a dois projetos, progresso por avatar, pausa/retomada e ZIP por avatar.
- Gemini 3.5 Flash via Kie.ai integrado como rota opcional; homologação real pendente, inclusive imagens inline.
- Seleção explícita do provedor, fallback mantido no projeto, retentativas temporárias contabilizadas e interrompíveis.
- 36 testes locais; instância de interface isolada sem chaves. Sem geração paga nesta atualização.

## Atualização 0.3.0

- Windows DPAPI com migração de credenciais legadas e desconexão das três contas.
- Gemini e Kie.ai integrados às checagens das etapas; fallback somente por HTTP 429 tipado.
- Contagem corrigida para Kie.ai; Gemini sem retries automáticos ocultos.
- Autorização explícita e checagem prévia de pausa/limite para uploads temporários.
- Identificador Kie.ai persistido imediatamente; recuperação sem nova geração, seguida de revisão manual.
- Interface e README alinhados; 28 testes locais aprovados, sem chamadas pagas.
- Próximo passo: lote piloto real pequeno, com orçamento/escopo acordados com Luigi. Ainda não homologado.

Os registros da 0.2.0 abaixo são históricos; armazenamento e fornecedores foram substituídos pelas regras da 0.3.0.

## Implementado na 0.2.0

- GPT-6 Astra médio como padrão de todas as etapas de análise/texto/revisão; GPT Image 2 preservado para imagens.
- Preferências persistentes sem chave, erros com ocultação de credenciais e verificação de catálogo dos modelos.
- Limites cumulativos de chamadas por projeto e pausa antes de novas chamadas.
- Correção orientada por texto usando a imagem recebida; âncora original também nas edições e revisões.
- Validação de cobertura temporal, timestamps, ordem de takes e separação de setups.
- Registro por chamada de modelo, raciocínio e uso retornado pelo provedor.
- 21 testes locais com provedores simulados.

## Próximo marco: primeiro lote real

1. Revogar a chave que foi publicada na conversa e configurar a substituta dentro do Studio.
2. Verificar conexão salva; a consulta de catálogo não equivale a geração testada.
3. Executar a análise do projeto de validação já extraído; comparar herói e beats com o vídeo.
4. Aprovar roteiro e selecionar um gancho para um lote piloto pequeno.
5. Gerar referência, gancho, corpo e CTA; registrar custo real, tempo e correções.
6. Luigi gerar os clipes no Flow / Omni Flash e informar quais ações funcionaram.

## Ainda não implementado / não homologado

- Integração completa do `checar_entrega.py` com perfil explícito de imagens + prompts, preservando suas verificações e excluindo apenas escopos não contratados (DM/Stories).
- Matriz versionada e completa de precedência entre regras vigentes e revogadas. A política atual resolve parte das divergências, não todas.
- Re-extração automática a 15 fps em janelas ambíguas e nova análise antes de escalar ao operador.
- Conferência editorial sistemática da fidelidade dos beats, duração e congruência, além da validação estrutural.
- Atualização coordenada de tradução e ações quando a fala é editada.
- Correção com máscara/região e comparação global de continuidade entre todas as imagens do lote.
- Biblioteca operacional entre projetos: rotação de copy/hooks, assets reaproveitáveis e feedback validado no Flow. Comentários por imagem já são preservados, mas não viram regras automaticamente.
- Orçamento monetário, estimativa de custo antes da execução e comparação de desempenho entre lotes. Os limites atuais são de chamadas.
- Retomar somente a revisão de uma imagem sem exigir aprovação manual após falha de revisão.
- Modo de avanço automático entre etapas com critérios de aprovação calibrados em lotes reais.
- Piloto com 10–20 referências variadas, medindo intervenção humana, custo, tempo e aproveitamento no Flow. Não confundir volume de testes de software com qualidade visual comprovada.

O escopo atual termina nas imagens e prompts. Geração de vídeo no Flow, publicação e automação de DM/Stories não fazem parte da execução automática do Studio.
