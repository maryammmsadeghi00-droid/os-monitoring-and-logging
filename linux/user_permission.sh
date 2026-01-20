#!/bin/bash

# List users
cut -d: -f1 /etc/passwd

# Show current user
whoami

# Show groups of current user
groups

# Check permissions of system directory
ls -ld /etc /bin /usr
