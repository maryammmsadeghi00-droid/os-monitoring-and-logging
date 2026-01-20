#!/usr/bin/env python3
import subprocess
import time

# --- Configuration ---
CRITICAL_SERVICES = ["Spooler", "wuauserv", "WinDefend"]
CHECK_INTERVAL = 10  # seconds


def run_powershell(command):
    """Run PowerShell command and return output"""
    try:
        result = subprocess.check_output(
            ["powershell", "-Command", command],
            stderr=subprocess.DEVNULL,
            text=True
        )
        return result.strip()
    except subprocess.CalledProcessError:
        return ""


def list_services():
    """List Windows services and their status"""
    cmd = "Get-Service | Select-Object Name, Status"
    output = run_powershell(cmd)
    services = []
    for line in output.splitlines()[2:]:
        parts = line.split()
        if len(parts) >= 2:
            services.append({
                "name": parts[0],
                "status": parts[-1]
            })
    return services


def check_critical_services():
    """Check critical services and warn if stopped"""
    for service in CRITICAL_SERVICES:
        status = run_powershell(f"(Get-Service -Name {service}).Status")
        if status.lower() != "running":
            print(f"[ALERT] Critical service stopped: {service}")


def eventlog_errors():
    """Show recent warning and error logs"""
    cmd = (
        "Get-WinEvent -LogName System -MaxEvents 10 | "
        "Where-Object {$_.LevelDisplayName -in @('Error','Warning')} | "
        "Select-Object TimeCreated, LevelDisplayName, Message"
    )
    logs = run_powershell(cmd)
    if logs:
        print("\n[EVENT LOGS - WARNING & ERROR]")
        print(logs)


def main():
    print("Simple Windows Service Monitoring Tool\n")

    services = list_services()
    print("Service Status (first 10):")
    for s in services[:10]:
        print(f"{s['name']} -> {s['status']}")

    eventlog_errors()

    print("\nMonitoring critical services...")
    while True:
        check_critical_services()
        time.sleep(CHECK_INTERVAL)


if __name__ == "__main__":
    main()
