# restaurar_memoria.ps1
#
# O CAMINHO DE VOLTA do sync_memoria.ps1: copia o espelho memoria/ do repo para a
# memoria viva do Claude Code, em ~/.claude/projects/<projeto>/memory/.
#
# POR QUE ISTO EXISTE
# O clone do GitHub traz memoria/, que e SO O ESPELHO. A memoria que o agente
# realmente le vive fora do repo, no perfil do usuario. Num PC novo aquela pasta
# nasce vazia, entao o agente clona sem copy, sem rotas, sem fichas de avatar e
# sem os bancos: mesmo repo, cabeca vazia. Este script fecha esse buraco.
#
# RODAR UMA VEZ POR PC NOVO, logo depois do clone. Depois disso o sync_memoria.ps1
# volta a ser o unico sentido que importa, porque a fonte de verdade e a memoria viva.
#
# SEGURANCA: nunca apaga nada no destino e nunca sobrescreve arquivo diferente sem
# -Force. O destino e o cerebro vivo, e sobrescrever ele por engano custa mais caro
# que sobrescrever o espelho.
#
# Uso:  powershell -ExecutionPolicy Bypass -File restaurar_memoria.ps1
#       powershell -ExecutionPolicy Bypass -File restaurar_memoria.ps1 -Force
#
# Criado em 2026-09-12.

param(
    [switch]$Force
)

$ErrorActionPreference = 'Stop'

$repoRoot = Split-Path -Parent $MyInvocation.MyCommand.Path
$origem   = Join-Path $repoRoot 'memoria'

# Mesma derivacao do sync_memoria.ps1: ':' e '\' e ' ' viram '-'
$slug    = $repoRoot.Replace(':', '-').Replace('\', '-').Replace(' ', '-')
$destino = Join-Path $env:USERPROFILE ".claude\projects\$slug\memory"

if (-not (Test-Path $origem)) {
    Write-Host "ERRO: nao achei o espelho em $origem" -ForegroundColor Red
    Write-Host "      Rodar este script de dentro do clone do repositorio."
    exit 1
}

if (-not (Test-Path $destino)) {
    New-Item -ItemType Directory -Path $destino -Force | Out-Null
    Write-Host "Criei a pasta de memoria viva: $destino" -ForegroundColor Green
}

# Arquivos que sao SO DO REPO e nunca existiram na memoria viva. Mesma lista do
# sync_memoria.ps1, pelo mesmo motivo, so que no sentido contrario: sem ela o
# README.md do repo vira uma memoria falsa que o agente leria como fato.
$soDoRepo = @('README.md')

$fonte = @(Get-ChildItem $origem -Filter *.md -File | Where-Object { $soDoRepo -notcontains $_.Name })

$novos     = @()
$mudados   = @()
$iguais    = @()
$conflitos = @()

foreach ($f in $fonte) {
    $alvo = Join-Path $destino $f.Name
    if (-not (Test-Path $alvo)) {
        Copy-Item $f.FullName $alvo
        $novos += $f.Name
        continue
    }

    $hashA = (Get-FileHash $f.FullName -Algorithm SHA256).Hash
    $hashB = (Get-FileHash $alvo       -Algorithm SHA256).Hash

    if ($hashA -eq $hashB) {
        $iguais += $f.Name
    } elseif ($Force) {
        Copy-Item $f.FullName $alvo -Force
        $mudados += $f.Name
    } else {
        $conflitos += $f.Name
    }
}

Write-Host ""
Write-Host "Origem (espelho do repo): $origem"
Write-Host "Destino (memoria viva)  : $destino"
Write-Host "Total no espelho        : $($fonte.Count) arquivos de memoria"
Write-Host ""

if ($novos.Count)   { Write-Host "RESTAURADOS ($($novos.Count)):" -ForegroundColor Green;    $novos   | ForEach-Object { Write-Host "  + $_" } }
if ($mudados.Count) { Write-Host "SOBRESCRITOS ($($mudados.Count)):" -ForegroundColor Cyan;  $mudados | ForEach-Object { Write-Host "  ~ $_" } }
if ($iguais.Count)  { Write-Host "JA IGUAIS ($($iguais.Count))" -ForegroundColor DarkGray }

if ($conflitos.Count) {
    Write-Host ""
    Write-Host "DIVERGENTES ($($conflitos.Count)), nao toquei:" -ForegroundColor Yellow
    $conflitos | ForEach-Object { Write-Host "  ! $_" }
    Write-Host ""
    Write-Host "A memoria viva deste PC tem versao diferente do espelho." -ForegroundColor Yellow
    Write-Host "Se o espelho e que esta certo, rodar de novo com -Force."
    Write-Host "Se a memoria viva e que esta certa, rodar sync_memoria.ps1 e commitar."
}

$indice = Join-Path $destino 'MEMORY.md'
if (-not (Test-Path $indice)) {
    Write-Host ""
    Write-Host "ATENCAO: o MEMORY.md nao chegou no destino." -ForegroundColor Red
    Write-Host "         Sem o indice o agente nao abre memoria nenhuma."
    exit 1
}

Write-Host ""
Write-Host "Memoria viva pronta. Confirmar com: python checar_memoria.py" -ForegroundColor Green
