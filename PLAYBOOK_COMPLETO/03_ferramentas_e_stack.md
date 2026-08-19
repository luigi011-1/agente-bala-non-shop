# 03 — Ferramentas e Stack de Produção

> **Lembrete:** todas as ferramentas abaixo são usadas para produzir vídeos de **avatares de IA — pessoas que não existem**.

Este documento apresenta **todas as ferramentas** da operação, divididas em três grupos: geração de imagem, geração de vídeo, e a stack técnica local (os programas instalados no computador para a ferramenta `/watch` funcionar). O documento 04 detalha a `/watch` em si; aqui você entende o papel de cada peça.

---

## 1. Geração de imagem — o "frame inicial" de cada take

Cada take de vídeo começa como uma **imagem estática** (o frame inicial). Essas imagens são geradas por dois modelos:

### Nano Banana 2
- Modelo de geração de imagem usado para a **maior parte do volume**.
- Recebe a **foto do avatar como âncora de identidade** (pra manter rosto/roupa/cenário sempre iguais) e um prompt descrevendo a cena.
- É onde criamos o frame inicial da maioria dos takes.

### Nano Banana Pro
- Versão superior, usada para os **frames-herói** (os mais importantes, tipo o hook), onde a qualidade precisa ser máxima.
- **Fluxo recomendado:** volume no Nano Banana 2, frames-herói no Pro.
- O hook é o que mais paga; vale gerar várias variações no Pro até acertar.

### Comandos de edição (essencial para transformações)
- Ambos os modelos aceitam **comandos de edição**: você pega uma imagem já gerada e pede *"mude só X, mantenha o resto idêntico"*.
- Isso é **essencial** para gerar os "estágios" de uma transformação (braço encolhendo, banana murcha→firme, crosta→limpo, manequim liso→musculoso). Ver documento 02 seção 4, e documento 06.

> **Limitação conhecida do gerador de imagem:** ele tende a "defaultar" para a forma mais comum que conhece quando você só dá o **nome** de um objeto. Pedir "modelo do aparelho reprodutor feminino" pode sair como um coração; pedir "estrutura vascular ramificada" pode sair como uma estrela-do-mar ou uma raiz de árvore. A solução é sempre descrever a **forma e a geometria**, não só o nome. Ver documento 06 e 09.

---

## 2. Geração de vídeo — animar a imagem em um clipe falado

### Veo 3.1 via Flow
- Ferramenta de **imagem-para-vídeo** (image-to-video).
- Você dá a **imagem** (frame inicial) + um **prompt** descrevendo o que acontece e a fala, e ela gera o clipe de aproximadamente 8 segundos com o avatar falando/agindo.
- "Flow" é a interface; "Veo 3.1" é o modelo de vídeo por trás.

### Veo 3.1 Lite / Lower Priority
- Versão que roda **sem consumir créditos** (fila mais lenta, 720p).
- Ideal para **volume**. Use para gerar muitos takes sem gastar; guarde a fila rápida/paga para os takes que mais importam.

### O "Agent" do Flow (uma armadilha a evitar)
- O Flow tem um "Agent" (movido a Gemini) feito para **geração**, não para análise.
- Ele usa "Agent Instructions" como uma ficha de personagem persistente e permite marcar assets com @ para manter consistência. Serve pra manter o avatar constante entre gerações.
- **Ele NÃO serve para "assistir" e analisar vídeos.** Não confie nele para decompor um vídeo modelo. Para isso usamos a `/watch` (documento 04).

### Alternativas de geração de vídeo
Além do Veo/Flow, valem teste conforme o caso:
- **SeaDance** — às vezes mais realista que as demais para animar o avatar.
- **OmniHuman** — usado por contas de alto realismo; o segredo é dar **instruções detalhadas do movimento**.
- **Kling** — outra opção de image-to-video.
- Regra comum a todos: quanto mais **específica** a descrição do que o avatar faz (movimento, gesto), melhor; descrição vaga → movimento genérico.

---

## 2.5. Realismo — como não sair com "cara de IA"

Esta é a seção que mais ataca o gargalo de qualidade. "Cara de IA" mata a credibilidade do avatar e derruba a retenção. As regras abaixo valem tanto para a **geração de imagem** quanto para a de **vídeo**.

- **Close-up + poucos elementos = mais qualidade E mais realismo.** Uma cena poluída (muitos objetos, muito fundo, muita gente) faz o gerador — seja ChatGPT, seja Nano Banana — **estragar a qualidade**. **Isolar é a alavanca nº1.** É a mesma lição do hook (documento 06), agora pela ótica técnica: menos elementos, imagem e vídeo mais nítidos.
- **Nano Banana 2 costuma superar o ChatGPT** em realismo de avatar. E realismo não vem de um "prompt mágico" — vem de **regenerar várias vezes** até sair a imagem perfeita.
- **O ativo mais importante é a imagem-âncora do avatar muito realista.** Nenhum prompt compensa uma âncora ruim.
- **Pessoas secundárias na cena** (a segunda pessoa, os personagens do movie style): use **referência de rosto REAL do Pinterest** — evita a "cara genérica de IA". As referências devem ser orgânicas (tiradas direto do TikTok, com iluminação boa).
- **Cores e luz que denunciam IA:** cores quentes (amarelo/marrom/laranja) deixam a imagem mais "cara de IA"; **céu branco ou claro SEMPRE denuncia**. Prefira **céu nublado** e cenas em **golden hour** (fim de tarde) — contas de alto realismo filmam nesses horários.
- **Fundo borrado não se conserta editando depois** — tem que sair certo na primeira geração: descrição de fundo **muito específica** + uma **imagem de referência real** (casa/rua/bairro americano tirado de Pinterest, Pexels ou Google). Alternativa: dar um screenshot de um fundo real e pôr a pessoa falando na frente dele.
- **Realismo avançado ("método Frankie"):** gerar os elementos **separados** (o céu, as árvores, as casas, o rosto), cada um no seu melhor, e depois **mesclar** num frame só mantendo a qualidade de cada um. Trabalhoso, mas é o que os creators de realismo máximo fazem.

> Regra-mãe de realismo: **para gerar algo realista, parta sempre de algo real** — referência de rosto real, de fundo real, de luz real. A IA copia bem o que você mostra; inventa mal o que você só descreve.

---

## 3. Análise do vídeo modelo — a ferramenta `/watch` e sua stack

Para **decompor** o vídeo vencedor (analisar frame a frame + transcrever o áudio), construímos uma ferramenta própria chamada `/watch`. O documento 04 explica como ela foi criada e como usá-la. Aqui está a **stack técnica** que ela precisa — os programas que foram instalados no computador.

> **Contexto importante:** uma IA que ajuda a decompor um vídeo **não "assiste" continuamente e não ouve áudio nativamente.** Por baixo, qualquer análise de vídeo por IA é **amostragem de frames** (extrair quadros e olhar as imagens). A `/watch` faz essa amostragem de forma densa e organizada, e ainda transcreve o áudio separadamente com um modelo de voz. Não existe um modo mágico de "assistir de verdade" — o que existe é fazer a amostragem tão densa e a transcrição tão boa que nada se perca.

### Os programas instalados (e o papel de cada um)

| Programa | Versão | Para que serve |
|---|---|---|
| **Python** | 3.12 | Linguagem que roda o script do pipeline |
| **ffmpeg / ffprobe** | 9.0 (build Gyan) | Extrai frames do vídeo e o áudio; sonda duração/fps/resolução |
| **faster-whisper** | 1.2.x | Modelo de reconhecimento de voz que transcreve o áudio na CPU |
| **modelo `small.en`** | — | O modelo de transcrição em inglês (bom equilíbrio precisão/velocidade) |
| **Pillow** | 12.x | Biblioteca Python que monta as grades (contact sheets) legíveis |

### Como foram instalados (Windows, via winget e pip)

O sistema tinha `winget` disponível (gerenciador de pacotes do Windows), o que permitiu instalar tudo sem precisar de administrador em alguns casos. Os comandos exatos:

```powershell
# Python 3.12 (escopo de usuário, evita pedir admin)
winget install --id Python.Python.3.12 -e --scope user --silent --accept-package-agreements --accept-source-agreements

# ffmpeg (build completo do Gyan)
winget install --id Gyan.FFmpeg -e --silent --accept-package-agreements --accept-source-agreements

# faster-whisper e Pillow (via pip do Python instalado)
python -m pip install faster-whisper Pillow
```

**Caminhos reais onde os programas ficaram instalados nesta máquina:**
- Python: `C:\Users\luigi\AppData\Local\Programs\Python\Python312\python.exe`
- ffmpeg / ffprobe: `%LOCALAPPDATA%\Microsoft\WinGet\Links\` (ex.: `...\WinGet\Links\ffmpeg.exe`)
- Modelo `small.en` do Whisper: baixado automaticamente no primeiro uso, fica em cache do HuggingFace.

### Detalhe técnico importante: recarregar o PATH

Quando o `ffmpeg` é instalado via winget, ele avisa que o `PATH` (a lista de pastas onde o Windows procura programas) foi modificado e que é preciso **reiniciar o shell** para usá-lo. Um terminal aberto antes da instalação não "enxerga" o ffmpeg. A solução usada no wrapper da `/watch` é recarregar o PATH do registro no início de cada execução:

```powershell
$env:Path = [System.Environment]::GetEnvironmentVariable("Path","Machine") + ";" +
            [System.Environment]::GetEnvironmentVariable("Path","User")
```

Isso garante que o `ffmpeg`, `ffprobe` e `python` sejam sempre encontrados, mesmo num terminal recém-aberto.

### Outra pegadinha técnica: ffmpeg 9.0 removeu `-vsync`

Na versão 9.0 do ffmpeg, a opção antiga `-vsync` foi removida e substituída por `-fps_mode`. Um script escrito para versões antigas do ffmpeg quebra. O script da `/watch` usa `-fps_mode vfr` na detecção de cena.

---

## 4. Legendas e edição final

- As legendas grandes estilo "Captions.ai Prism Pro" são uma **referência de estilo** (letras grandes, palavra por palavra, cores contrastantes tipo branco+amarelo ou branco+rosa). Os vídeos modelo geralmente já vêm com esse tipo de legenda queimada; você imita o estilo na sua edição.
- A **montagem final** (juntar takes, pôr legenda, pôr locução quando necessário, pôr trilha) é feita num editor de vídeo padrão.
- Exportação sempre em **9:16 vertical**.

---

## 5. Resumo do fluxo de ferramentas

```
VÍDEO MODELO (.mp4)
      │
      ▼  /watch  (Python + ffmpeg + faster-whisper + Pillow)
DECOMPOSIÇÃO (frames densos + transcrição + grades)
      │
      ▼  análise humana/IA
ROTEIRO + PROMPTS
      │
      ▼  Nano Banana 2 / Pro
IMAGENS (frames iniciais)
      │
      ▼  Veo 3.1 via Flow (Lite pra volume)
CLIPES (~8s cada)
      │
      ▼  editor de vídeo
VÍDEO FINAL 9:16
```

Próximo documento: **04 — A Skill `/watch`**, que detalha a ferramenta que criamos para a etapa de decomposição.
