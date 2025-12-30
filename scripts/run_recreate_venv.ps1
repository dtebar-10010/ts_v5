# Change to repo root and run the batch script via cmd.exe
$scriptRoot = Split-Path -Parent $MyInvocation.MyCommand.Definition
if (-not $scriptRoot) { $scriptRoot = (Get-Location).Path }
$repoRoot = Resolve-Path (Join-Path $scriptRoot '..')
Set-Location $repoRoot
$bat = Join-Path $repoRoot 'scripts\recreate_venv.bat'
if (-not (Test-Path $bat)) {
  Write-Error "Batch script not found: $bat"
  exit 1
}
Write-Output "Running: $bat"
cmd /c "`"$bat`""
exit $LASTEXITCODE
