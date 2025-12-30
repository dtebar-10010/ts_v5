# Run the batch via cmd.exe so PowerShell doesn't try to interpret batch syntax.
$full = Join-Path -Path (Split-Path -Parent $MyInvocation.MyCommand.Definition) -ChildPath 'recreate_venv.bat'
if (-not (Test-Path $full)) {
  Write-Error "Batch script not found: $full"
  exit 1
}
cmd /c "`"$full`""
exit $LASTEXITCODE
