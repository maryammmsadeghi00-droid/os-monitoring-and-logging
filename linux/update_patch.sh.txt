#!/bin/bash

# Check OS release
cat /etc/os-release

# Check available updates (Debian/Ubuntu based)
sudo apt update
apt list --upgradable

# Show last installed packages
grep " install " /var/log/dpkg.log | tail -n 5
