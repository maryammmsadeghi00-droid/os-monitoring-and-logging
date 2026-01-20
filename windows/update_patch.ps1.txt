# Check Windows Update service status
Get-Service wuauserv

# List installed updates
Get-HotFix

# Last update installation date
(Get-HotFix | Sort-Object InstalledOn -Descending)[0]
