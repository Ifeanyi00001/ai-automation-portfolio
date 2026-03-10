$apiKey = '
$jsonFile = 'C:\Users\USER\.gemini\antigravity\scratch\portfolio\project-02-contract-compliance\workflow.json'
$url = 'http://localhost:5678/api/v1/workflows'
$headers = @{ 'X-N8N-API-KEY' = $apiKey; 'Content-Type' = 'application/json' }
$body = [System.IO.File]::ReadAllText($jsonFile, [System.Text.Encoding]::UTF8)

try {
    $resp = Invoke-RestMethod -Uri $url -Method POST -Headers $headers -Body $body
    Write-Host "SUCCESS"
    Write-Host ("ID:  " + $resp.id)
    Write-Host ("URL: http://localhost:5678/workflow/" + $resp.id)
}
catch {
    Write-Host ("ERROR: " + $_.Exception.Message)
    if ($_.ErrorDetails.Message) { Write-Host $_.ErrorDetails.Message }
}
