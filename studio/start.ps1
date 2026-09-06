$ErrorActionPreference = 'Stop'
trap {
    Add-Type -AssemblyName System.Windows.Forms
    [System.Windows.Forms.MessageBox]::Show($_.Exception.Message, 'Auraly Studio — inicialização') | Out-Null
    exit 1
}
$studioRoot = Split-Path -Parent $PSScriptRoot
$studioPython = Join-Path $PSScriptRoot '.venv\Scripts\python.exe'
$studioPythonWindow = Join-Path $PSScriptRoot '.venv\Scripts\pythonw.exe'
$studioUrl = 'http://127.0.0.1:8766'
function Open-StudioWindow {
    Start-Process -WindowStyle Normal -FilePath $studioPythonWindow -WorkingDirectory $studioRoot -ArgumentList @('-m', 'studio.desktop')
}
try {
    $studioHealth = Invoke-RestMethod "$studioUrl/api/config" -TimeoutSec 2
    if ($studioHealth.version -eq '0.6.0') { Open-StudioWindow; exit 0 }
} catch { }
if ($studioHealth -and $studioHealth.version -ne '0.6.0') {
    throw 'Há uma versão anterior aberta. Encerre o servidor antigo antes de iniciar a 0.6.0. Fechar apenas a aba não encerra o servidor.'
}
if (-not (Test-Path -LiteralPath $studioPython)) {
    & python -m venv --system-site-packages (Join-Path $PSScriptRoot '.venv')
    if ($LASTEXITCODE -ne 0) { throw 'Não foi possível criar o ambiente Python.' }
}
& $studioPython -c 'import fastapi, uvicorn, multipart, httpx, PIL, faster_whisper, webview' 2>$null
if ($LASTEXITCODE -ne 0) {
    & $studioPython -m pip install -r (Join-Path $PSScriptRoot 'requirements.txt')
    if ($LASTEXITCODE -ne 0) { throw 'Instalação das dependências falhou.' }
}
$studioLogs = Join-Path $PSScriptRoot 'data'
New-Item -ItemType Directory -Force -Path $studioLogs | Out-Null
$studioProcess = Start-Process -WindowStyle Hidden -FilePath $studioPython -WorkingDirectory $studioRoot -ArgumentList @('-m','uvicorn','studio.app:app','--host','127.0.0.1','--port','8766') -RedirectStandardOutput (Join-Path $studioLogs 'server-06.log') -RedirectStandardError (Join-Path $studioLogs 'server-06-error.log') -PassThru
for ($studioAttempt=0; $studioAttempt -lt 30; $studioAttempt++) {
    Start-Sleep -Milliseconds 500
    if ($studioProcess.HasExited) { throw 'O servidor não iniciou. Consulte studio/data/server-06-error.log.' }
    try { $studioReady = Invoke-RestMethod "$studioUrl/api/config" -TimeoutSec 1 } catch { continue }
    if ($studioReady.version -eq '0.6.0') { Open-StudioWindow; exit 0 }
}
throw 'Servidor demorou para iniciar. Consulte studio/data/server-06-error.log.'
