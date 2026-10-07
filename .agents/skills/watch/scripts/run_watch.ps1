param(
    [Parameter(Mandatory=$true)][string]$Video,
    [string]$OutDir = "",
    [string]$Extra = "",
    [string[]]$PipelineArgs = @()
)
$ErrorActionPreference = "Stop"
$projectRoot = (Resolve-Path (Join-Path $PSScriptRoot "..\..\..\..")).Path
$python = $env:BALA_PYTHON
if (-not $python) {
    foreach ($candidate in @(
        (Join-Path $projectRoot ".venv-operacao\Scripts\python.exe"),
        (Join-Path $projectRoot ".venv\Scripts\python.exe")
    )) {
        if (Test-Path -LiteralPath $candidate) { $python = $candidate; break }
    }
}
if (-not $python) {
    $python = (Get-Command python -ErrorAction SilentlyContinue | Where-Object { $_.Source -notlike "*WindowsApps*" } | Select-Object -First 1).Source
}
if (-not $python) { throw "Python ausente. Prepare scripts/preparar_operacao.py." }
$watchArgs = @("--video", $Video)
if ($OutDir) { $watchArgs += @("--outdir", $OutDir) }
# Compatibility for old simple Extra flags. Use PipelineArgs for quoted paths or multiword values.
if ($Extra) { $watchArgs += ($Extra -split '\s+' | Where-Object { $_ }) }
$watchArgs += $PipelineArgs
& $python (Join-Path $PSScriptRoot "watch_pipeline.py") @watchArgs
exit $LASTEXITCODE
