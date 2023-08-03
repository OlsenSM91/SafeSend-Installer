# Define the URL of the MSI installer
$msiUrl = "YOUR_MSI_URL_HERE"

# Define the path where the MSI will be downloaded
$downloadPath = "$env:TEMP\installer.msi"

# Download the MSI installer
Invoke-WebRequest -Uri $msiUrl -OutFile $downloadPath

# Install the MSI silently (with progress window but no user interaction)
$installResult = Start-Process -FilePath "msiexec.exe" -ArgumentList "/i `"$downloadPath`" /passive" -Wait -PassThru

# Check if the MSI was successfully installed (exit code 0 means success)
if ($installResult.ExitCode -eq 0) {
    # Run the reg add command
    reg add HKEY_LOCAL_MACHINE\SOFTWARE\WOW6432Node\SafeSend /v SS_LicenseKey /d "New License Key from SafeSend" /f
} else {
    Write-Host "MSI installation failed with exit code $($installResult.ExitCode)"
}

# Optionally, delete the downloaded MSI file
Remove-Item -Path $downloadPath -Force
