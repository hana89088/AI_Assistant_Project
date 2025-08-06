# Script to open 300 tabs in Microsoft Edge
# Warning: This will use significant system resources

Write-Host "Starting to open 300 tabs in Microsoft Edge..."
Write-Host "This may take a while and use significant system resources."
Write-Host ""

# Start Microsoft Edge if not already running
Start-Process "msedge.exe"

# Wait a moment for Edge to start
Start-Sleep -Seconds 2

# Open 300 tabs
for ($i = 1; $i -le 300; $i++) {
    # Open a new tab with about:blank to minimize resource usage
    Start-Process "msedge.exe" -ArgumentList "about:blank"
    
    # Small delay to prevent overwhelming the system
    Start-Sleep -Milliseconds 50
    
    # Show progress every 10 tabs
    if ($i % 10 -eq 0) {
        Write-Host "Opened $i tabs..."
    }
}

Write-Host ""
Write-Host "Completed! Opened 300 tabs in Microsoft Edge."
Write-Host "Note: Your system may be slow due to resource usage."
