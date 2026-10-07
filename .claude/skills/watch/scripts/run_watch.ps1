param(
    [Parameter(Mandatory=$true)][string]$Video,
    [string]$OutDir = "",
    [string]$Extra = "",
    [string[]]$PipelineArgs = @()
)
$projectRoot = (Resolve-Path (Join-Path $PSScriptRoot "..\..\..\..")).Path
& (Join-Path $projectRoot ".agents\skills\watch\scripts\run_watch.ps1") -Video $Video -OutDir $OutDir -Extra $Extra -PipelineArgs $PipelineArgs
exit $LASTEXITCODE
