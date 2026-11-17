param(
    [Parameter(Mandatory = $true)][string]$Entrada,
    [Parameter(Mandatory = $true)][string]$Saida
)

if (Test-Path $Saida) { Remove-Item $Saida -Force }

$word = New-Object -ComObject Word.Application
$word.Visible = $false
$word.DisplayAlerts = 0

try {
    $doc = $word.Documents.Open($Entrada, [ref]$false, [ref]$true)
    $doc.Repaginate()
    $paginas = $doc.ComputeStatistics(2)      # wdStatisticPages

    # wdExportFormatPDF = 17, wdExportOptimizeForPrint = 0, wdExportAllDocument = 0
    $doc.ExportAsFixedFormat($Saida, 17, $false, 0, 0, 1, 1, 0, $true, $true, 0)

    $doc.Close([ref]0)
    Write-Output "PAGINAS=$paginas"
}
finally {
    $word.Quit()
    [System.Runtime.InteropServices.Marshal]::ReleaseComObject($word) | Out-Null
    [GC]::Collect()
}
