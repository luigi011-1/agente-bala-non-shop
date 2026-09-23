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

$py = "C:\Users\luigi\AppData\Local\Programs\Python\Python312\python.exe"
if (-not (Test-Path $py)) {
    $py = (Get-Command python -ErrorAction SilentlyContinue |
           Where-Object { $_.Source -notlike "*WindowsApps*" } |
           Select-Object -First 1).Source
}
if (-not $py) { throw "Python nao encontrado." }

$script = Join-Path $PSScriptRoot "watch_pipeline.py"

$args = @("--video", $Video)
if ($OutDir -ne "") { $args += @("--outdir", $OutDir) }
if ($Extra -ne "")  { $args += $Extra.Split(" ") }

& $py $script @args
exit $LASTEXITCODE
