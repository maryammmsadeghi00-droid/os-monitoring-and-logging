# Show Windows version and kernel info
systeminfo | findstr /B /C:"OS Name" /C:"OS Version"

# Check if Secure Boot is enabled
Confirm-SecureBootUEFI

# Check Device Guard status
Get-CimInstance -ClassName Win32_DeviceGuard
