#!/bin/bash

# Kernel version
uname -r

# Kernel security parameters
sysctl kernel.kptr_restrict
sysctl kernel.dmesg_restrict

# Check SELinux status (if available)
sestatus 2>/dev/null
