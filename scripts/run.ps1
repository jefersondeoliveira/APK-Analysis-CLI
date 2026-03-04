param(
    [string] $apkPath = ''
)

if (-not (Test-Path -Path .venv)) {
    python -m venv .venv
}
.\.venv\Scripts\Activate.ps1

if ($apkPath -eq '') {
    Write-Host "Usage: .\scripts\run.ps1 <path-to-apk>"
    exit 2
}

python -m apk_analyzer.cli.main $apkPath
