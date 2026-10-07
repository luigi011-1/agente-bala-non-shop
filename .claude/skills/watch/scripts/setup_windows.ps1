# setup_windows.ps1 - prepara um ambiente reproduzivel para a skill /watch.

param(
    [switch]$SkipPackageInstall
)

$ErrorActionPreference = "Stop"

$env:Path = [System.Environment]::GetEnvironmentVariable("Path","Machine") + ";" +
            [System.Environment]::GetEnvironmentVariable("Path","User")

if (-not $SkipPackageInstall) {
    if (-not (Get-Command python -ErrorAction SilentlyContinue)) {
        winget install --id Python.Python.3.12 -e --scope user --silent `
            --accept-package-agreements --accept-source-agreements
        $env:Path = [System.Environment]::GetEnvironmentVariable("Path","Machine") + ";" +
                    [System.Environment]::GetEnvironmentVariable("Path","User")
    }

    if (-not (Get-Command ffmpeg -ErrorAction SilentlyContinue)) {
        winget install --id Gyan.FFmpeg -e --silent `
            --accept-package-agreements --accept-source-agreements
        $env:Path = [System.Environment]::GetEnvironmentVariable("Path","Machine") + ";" +
                    [System.Environment]::GetEnvironmentVariable("Path","User")
    }
}

$python = (Get-Command python -ErrorAction SilentlyContinue |
           Where-Object { $_.Source -notlike "*WindowsApps*" } |
           Select-Object -First 1).Source

if (-not $python) {
    throw "Python 3.12 nao foi encontrado."
}

if (-not (Get-Command ffmpeg -ErrorAction SilentlyContinue)) {
    throw "FFmpeg nao foi encontrado."
}

if (-not (Get-Command ffprobe -ErrorAction SilentlyContinue)) {
    throw "FFprobe nao foi encontrado."
}

$projectRoot = (Resolve-Path (Join-Path $PSScriptRoot "..\..\..\..")).Path
$venvDir = Join-Path $projectRoot ".venv-operacao"
$venvPython = Join-Path $venvDir "Scripts\python.exe"
$requirements = Join-Path $PSScriptRoot "..\requirements.txt"

if (-not (Test-Path -LiteralPath $venvPython)) {
    & $python -m venv $venvDir
}

& $venvPython -m pip install --upgrade pip
& $venvPython -m pip install -r $requirements
& $venvPython -c "import faster_whisper, ctranslate2, PIL, av; print('Ambiente /watch OK')"

Write-Output "Ambiente pronto: $venvDir"
