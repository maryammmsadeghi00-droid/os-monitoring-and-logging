# A Comparative Study of Security Mechanisms in Windows and Linux Operating Systems

This repository contains practical scripts used to analyze and compare
security mechanisms in Windows and Linux operating systems.

## Topics Covered
- User & Permission Management
- Kernel Security
- Update & Patch Management

## Structure
- windows/: PowerShell scripts for Windows security analysis
- linux/: Bash scripts for Linux security analysis

## Author
Student Project – OS Security

---

## How to Run (Local Test)

### Windows (PowerShell)
1. Open **PowerShell** as Administrator.
2. Navigate to the project directory:
   ```powershell
   cd "PATH_TO_PROJECT"
3. Run the scripts:

```powershell
powershell -ExecutionPolicy Bypass -File .\windows\user_permission.ps1
powershell -ExecutionPolicy Bypass -File .\windows\kernel_security.ps1
powershell -ExecutionPolicy Bypass -File .\windows\update_patch.ps1

---

### Linux (Bash)

1. Open Terminal.
2. Navigate to the project directory:
```bash
cd /path/to/project
3. Make scripts executable:
```bash
chmod +x linux/*.sh
./linux/user_permission.sh
./linux/kernel_security.sh
./linux/update_patch.sh
