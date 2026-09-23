# run_watch.ps1 — wrapper do pipeline /watch
# Recarrega o PATH (ffmpeg/ffprobe entram via WinGet Links) e roda o pipeline.
# Uso: powershell -File run_watch.ps1 -Video "CAMINHO.mp4" [-Extra "--model medium.en"]

param(
    [Parameter(Mandatory=$true)][string]$Video,
    [string]$OutDir = "",
    [string]$Extra = ""
)

$ErrorActionPreference = "Stop"

# PATH atualizado (Machine + User) para achar ffmpeg/ffprobe/python
$env:Path = [System.Environment]::GetEnvironmentVariable("Path","Machine") + ";" +
            [System.Environment]::GetEnvironmentVariable("Path","User")

$projectRoot = (Resolve-Path (Join-Path $PSScriptRoot "..\..\..\..")).Path
$venvPython = Join-Path $projectRoot ".venv\Scripts\python.exe"

if (Test-Path -LiteralPath $venvPython) {
    $py = $venvPython
} else {
    $py = (Get-Command python -ErrorAction SilentlyContinue |
           Where-Object { $_.Source -notlike "*WindowsApps*" } |
           Select-Object -First 1).Source
}

if (-not $py) {
    throw "Python nao encontrado. Rode setup_windows.ps1 antes de usar a skill."
}

if (-not (Get-Command ffmpeg -ErrorAction SilentlyContinue)) {
    throw "FFmpeg nao encontrado no PATH. Rode setup_windows.ps1."
}

if (-not (Get-Command ffprobe -ErrorAction SilentlyContinue)) {
    throw "FFprobe nao encontrado no PATH. Rode setup_windows.ps1."
}

$script = Join-Path $PSScriptRoot "watch_pipeline.py"

$args = @("--video", $Video)
if ($OutDir -ne "") { $args += @("--outdir", $OutDir) }
if ($Extra -ne "")  { $args += $Extra.Split(" ") }

& $py $script @args
exit $LASTEXITCODE
