$ErrorActionPreference = 'Stop'

$root = 'C:\Users\kisel\IdeaProjects\Book'

Get-ChildItem -LiteralPath $root -Directory | Where-Object {
    $_.Name -match '^\d{2}\. '
} | ForEach-Object {
    $bookDir = $_.FullName
    $bookName = $_.Name
    Write-Host "Processing: $bookName"

    $formatDirs = @('pdf', 'epub', 'fb2', 'docx', 'txt')
    foreach ($dir in $formatDirs) {
        $path = Join-Path -Path $bookDir -ChildPath $dir
        if (-not (Test-Path -LiteralPath $path)) {
            New-Item -ItemType Directory -Path $path -Force | Out-Null
        }
    }

    $extMap = @{
        '.pdf'  = 'pdf'
        '.epub' = 'epub'
        '.fb2'  = 'fb2'
        '.docx' = 'docx'
        '.txt'  = 'txt'
    }

    Get-ChildItem -LiteralPath $bookDir -File | Where-Object {
        $extMap.ContainsKey($_.Extension.ToLower())
    } | ForEach-Object {
        $targetDir = Join-Path -Path $bookDir -ChildPath $extMap[$_.Extension.ToLower()]
        $targetPath = Join-Path -Path $targetDir -ChildPath $_.Name
        Write-Host "  Moving: $($_.Name) -> $($extMap[$_.Extension.ToLower()])/"
        Move-Item -LiteralPath $_.FullName -Destination $targetPath -Force
    }

    Get-ChildItem -LiteralPath $bookDir -Filter '.gitkeep' -File | ForEach-Object {
        Write-Host "  Removing: $($_.Name)"
        Remove-Item -LiteralPath $_.FullName -Force
    }
}

Write-Host "Done."
