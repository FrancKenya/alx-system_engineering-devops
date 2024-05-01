# x0E. Web stack debugging #1

This project focuses on debugging and fixing issues related to Nginx installation on an Ubuntu 20.04 LTS server. Through two tasks, you'll hone your debugging skills and craft efficient Bash scripts to ensure Nginx is running and listening on port 80.

## General Requirements:
- Allowed editors: vi, vim, emacs
- All files will be interpreted on Ubuntu 20.04 LTS
- All files should end with a new line
- A README.md file at the root of the folder of the project is mandatory
- All Bash script files must be executable
- Bash scripts must pass Shellcheck without any error
- Bash scripts must run without error
- The first line of all Bash scripts should be exactly `#!/usr/bin/env bash`
- The second line of all Bash scripts should be a comment explaining what the script is doing
- You are not allowed to use wget

## Task 0: Debugging Nginx Listening Issue
Using your debugging skills, find out what’s preventing your Ubuntu container’s Nginx installation from listening on port 80. Then, write a Bash script to automate the fix.

Requirements:
- Nginx must be running and listening on port 80 of all the server’s active IPv4 IPs
- Write a Bash script that configures a server to meet the above requirements

## Task 1: Concise Fix Implementation
Using the solution from Task 0, make your fix concise.

Requirements:
- Your Bash script must be 5 lines long or less
- There must be a new line at the end of the file
- You must respect usual Bash script requirements
- You cannot use `;`
- You cannot use `&&`
- You cannot use `wget`
- You cannot execute your previous answer file
- Service (init) must report that nginx is not running
