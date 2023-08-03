import argparse
import os
import subprocess
import requests

def download_file(url, destination):
    response = requests.get(url, stream=True)
    response.raise_for_status()
    with open(destination, 'wb') as file:
        for chunk in response.iter_content(chunk_size=8192):
            file.write(chunk)

def main():
    parser = argparse.ArgumentParser(description="SafeSend Installer and License Key Setter")
    parser.add_argument('--Installer-URL', required=True, help='URL of the MSI installer to download and install')
    parser.add_argument('--SSLic', required=True, help='License key for SafeSend to set in the registry')
    args = parser.parse_args()

    # Define the path where the MSI will be downloaded
    download_path = os.path.join(os.getenv('TEMP'), 'installer.msi')

    # Download the MSI installer
    print(f"Downloading installer from {args.Installer_URL}...")
    download_file(args.Installer_URL, download_path)

    # Install the MSI silently (with progress window but no user interaction)
    print("Installing MSI...")
    result = subprocess.run(['msiexec.exe', '/i', download_path, '/passive'], capture_output=True)

    # Check if the MSI was successfully installed (exit code 0 means success)
    if result.returncode == 0:
        # Run the reg add command
        print("Setting license key in registry...")
        subprocess.run(['reg', 'add', 'HKEY_LOCAL_MACHINE\\SOFTWARE\\WOW6432Node\\SafeSend', '/v', 'SS_LicenseKey', '/d', args.SSLic, '/f'], capture_output=True)
    else:
        print(f"MSI installation failed with exit code {result.returncode}")

    # Optionally, delete the downloaded MSI file
    os.remove(download_path)

if __name__ == "__main__":
    main()
