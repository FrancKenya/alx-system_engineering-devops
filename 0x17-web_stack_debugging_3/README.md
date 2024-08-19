WordPress LAMP Stack Debugging and Automation with Puppet
=========================================================

Project Overview

This project involves debugging a WordPress installation running on a LAMP stack (Linux, Apache, MySQL, PHP) and automating the solutions using Puppet. The project is designed for Ubuntu 14.04 LTS and focuses on identifying and resolving common issues that arise within a WordPress environment. The fixes are automated using .pp Puppet manifests, ensuring consistent configurations across environments.

Requirements
General
All files are interpreted on Ubuntu 14.04 LTS.
All files should end with a new line.
A README.md file is mandatory at the root of the project.
Puppet manifests must pass puppet-lint version 2.1.1 without any errors.
Puppet manifests must run without errors.
The first line of each Puppet manifest must be a comment explaining the purpose of the file.
Puppet manifest files must end with the .pp extension.
Files will be checked with Puppet version 3.4.
Project Structure
The project contains multiple .pp manifest files, each focusing on specific aspects of the LAMP stack and WordPress environment. The main manifests address the following:

Apache Setup and Configuration (apache_install.pp):

Ensures Apache is installed, running, and enabled on boot.
PHP and Module Installation (php_install.pp):

Installs PHP and the necessary modules required by WordPress.
MySQL Configuration (mysql_config.pp):

Sets up MySQL, creates the WordPress database, and ensures it is running.
WordPress Setup and Permissions (wordpress_setup.pp):

Configures WordPress files, sets correct ownership and permissions, and automates the deployment.
Debugging with strace (0-strace_is_your_friend.pp):

A manifest that addresses issues discovered using strace, such as file permission errors or missing dependencies, and automates the fix.
Debugging Process
To troubleshoot issues like a 500 Internal Server Error in Apache:

Attach strace to the Apache process.
Analyze the strace logs for errors related to file permissions, missing files, or faulty configurations.
Implement the fix in a Puppet manifest and apply it using puppet apply <manifest>.pp.

Usage
Prerequisites:
apt-get install -y ruby
gem install puppet-lint -v 2.1.1

Applying Manifests
To apply a Puppet manifest:
sudo puppet apply <manifest>.pp

Linting Manifests
To check for syntax issues:
puppet-lint <manifest>.pp

Testing with Apache
After applying any fix, test the Apache response:
curl -I <http://localhost>

ou should receive a 200 OK status if the issue is resolved.

Project Workflow
Identify issues in the LAMP stack or WordPress installation using tools like strace.
Write Puppet manifests to automate the fixes.
Lint and test the manifests to ensure they run error-free.
Reapply the manifests to maintain a consistent and reliable environment.
