# SafeSend Installer

## Usage
Download the binary for `ssdeploy.exe` and provide the MSI URL and License key

# Windows Binary to Run a SafeSend Installer
## ssdeploy.exe

## Usage

To use this application, all you need to do is open an admin Powershell and run the following:
```
ssdeploy.exe --Installer-URL 'https://github.com/OlsenSM91/SafeSend-Installer/releases/download/initial/SafeSendSetup.msi' --SSLic 'LICENSE_KEY_HERE'
```
The script will fail if both arguments aren't supplied. The script will download, execute and verify the MSI installation and then it will add the SafeSend license key to the registry
