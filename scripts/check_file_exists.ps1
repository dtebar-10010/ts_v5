param(
  [string]$RelativePath = 'scripts\recreate_venv.bat'
)

$scriptRoot = Split-Path -Parent $MyInvocation.MyCommand.Definition
Set-Location -Path (Join-Path $scriptRoot '..')

$full = Join-Path -Path (Get-Location).Path -ChildPath $RelativePath

if (Test-Path $full) {
  Write-Output "Found: $full"
  exit 0
} else {
  Write-Output "Missing: $full"
  exit 1
}
