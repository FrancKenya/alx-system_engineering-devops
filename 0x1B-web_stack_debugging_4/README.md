# Webstack Debugging Project

This project focuses on debugging a web stack running Nginx and making OS-level configuration changes using Puppet. The goal is to enhance server reliability under load and address file handling issues for specific users.

## Requirements

1. **Fix Nginx Server Failures Under Load:**
   The Nginx server was failing when tested with ApacheBench, showing 943 failed requests out of 2000. The task was to update the Nginx configuration to handle more connections and reduce these failures to zero.

2. **Adjust OS Configuration for the `holberton` User:**
   The `holberton` user encountered issues when logging in and opening files, specifically due to insufficient `nofile` limits. The task was to modify the system limits to allow seamless file access.

## Solutions

### 1. Nginx Configuration Update

To improve Nginx performance, we increased the `worker_connections` value from 15 to 4096. A Puppet manifest was created to automate this change and ensure the Nginx service is restarted whenever the configuration is modified.

### 2. OS Configuration Update

To resolve file handling issues for the `holberton` user, the `nofile` limits in `/etc/security/limits.conf` were adjusted. The hard limit was set to 50000, and the soft limit was set to 40000. A Puppet manifest was used to make these changes idempotent and maintainable.
