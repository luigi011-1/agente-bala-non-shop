# sync_memoria.ps1
#
# Espelha a memoria viva do Claude Code para dentro do repositorio, em memoria/.
#
# POR QUE ISTO EXISTE
# A memoria de verdade vive em ~/.claude/projects/<projeto>/memory/ e e la que o
# agente escreve. A pasta memoria/ do repo e SO UM ESPELHO, para backup e historico.
# Sem este script viram duas fontes de verdade e o espelho apodrece, que e exatamente
# o problema que fez o PORTAO P10 existir.
#
# REGRA: rodar ANTES de todo commit que envolva memoria. Nunca editar memoria/ na mao.
#
# Uso:  powershell -ExecutionPolicy Bypass -File sync_memoria.ps1

$ErrorActionPreference = 'Stop'

$repoRoot = Split-Path -Parent $MyInvocation.MyCommand.Path
$destino  = Join-Path $repoRoot 'memoria'

# O Claude Code deriva o nome da pasta do projeto do caminho: ':' e '\' e ' ' viram '-'
$slug   = $repoRoot -replace ':', '-' -replace '\\', '-' -replace ' ', '-'
$origem = Join-Path $env:USERPROFILE ".claude\projects\$slug\memory"

if (-not (Test-Path $origem)) {
    # fallback: procura qualquer pasta de projeto que contenha um MEMORY.md
    $candidatos = Get-ChildItem (Join-Path $env:USERPROFILE '.claude\projects') -Directory -ErrorAction SilentlyContinue |
                  Where-Object { Test-Path (Join-Path $_.FullName 'memory\MEMORY.md') }
    if ($candidatos.Count -eq 1) {
        $origem = Join-Path $candidatos[0].FullName 'memory'
        Write-Host "Aviso: caminho derivado nao existia, usando $origem" -ForegroundColor Yellow
    } else {
        Write-Host "ERRO: nao achei a pasta de memoria." -ForegroundColor Red
        Write-Host "Esperava: $origem"
        exit 1
    }
}

if (-not (Test-Path $destino)) { New-Item -ItemType Directory -Path $destino | Out-Null }

$fonte  = @(Get-ChildItem $origem  -Filter *.md -File)
$espelho = @(Get-ChildItem $destino -Filter *.md -File)

$novos     = @()
$mudados   = @()
$removidos = @()

foreach ($f in $fonte) {
    $alvo = Join-Path $destino $f.Name
    if (-not (Test-Path $alvo)) {
        Copy-Item $f.FullName $alvo
        $novos += $f.Name
    } else {
        $hashA = (Get-FileHash $f.FullName -Algorithm SHA256).Hash
        $hashB = (Get-FileHash $alvo      -Algorithm SHA256).Hash
        if ($hashA -ne $hashB) {
            Copy-Item $f.FullName $alvo -Force
            $mudados += $f.Name
        }
    }
}

# Arquivos que sao SO DO REPO e nunca existiram na memoria viva. Sem esta lista o
# laco abaixo os apaga em TODO sync, porque "nao esta na origem" e exatamente a
# condicao de remover. Era o caso do README.md: morria a cada rodada e exigia um
# `git checkout -- memoria/README.md` na mao depois. Corrigido em 2026-08-28.
$preservados = @('README.md')

# espelho de verdade: apaga o que nao existe mais na origem
$nomesFonte = $fonte | ForEach-Object { $_.Name }
$mantidos   = @()
foreach ($e in $espelho) {
    if ($preservados -contains $e.Name) {
        $mantidos += $e.Name
        continue
    }
    if ($nomesFonte -notcontains $e.Name) {
        Remove-Item $e.FullName -Confirm:$false
        $removidos += $e.Name
    }
}

Write-Host ""
Write-Host "Origem : $origem"
Write-Host "Destino: $destino"
Write-Host "Total  : $($fonte.Count) arquivos de memoria"
Write-Host ""

if ($novos.Count)     { Write-Host "NOVOS ($($novos.Count)):"       -ForegroundColor Green;  $novos     | ForEach-Object { Write-Host "  + $_" } }
if ($mudados.Count)   { Write-Host "MUDADOS ($($mudados.Count)):"   -ForegroundColor Cyan;   $mudados   | ForEach-Object { Write-Host "  ~ $_" } }
if ($removidos.Count) { Write-Host "REMOVIDOS ($($removidos.Count)):" -ForegroundColor Yellow; $removidos | ForEach-Object { Write-Host "  - $_" } }
if ($mantidos.Count)  { Write-Host "PRESERVADOS ($($mantidos.Count)):"  -ForegroundColor DarkGray; $mantidos  | ForEach-Object { Write-Host "  = $_ (arquivo do repo, nao da memoria)" } }

if (-not ($novos.Count -or $mudados.Count -or $removidos.Count)) {
    Write-Host "Espelho ja estava em dia. Nada a fazer." -ForegroundColor DarkGray
} else {
    Write-Host ""
    Write-Host "Pronto. Agora: git add memoria/ && git commit" -ForegroundColor Green
}
Write-Host ""
