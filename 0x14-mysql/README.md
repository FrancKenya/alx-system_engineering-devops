0x14. MySQL
MySQL is a relational database management system that uses structured query language for managing ang manipulating data
This project focuses on setting up and configuring MySQL in the provided servers.
It consists of executable bash scripts with to carry the requirements

MySQL 5.7 installation guide:
1. Download the MySQL repository by executing the following command
wget https://dev.mysql.com/get/mysql-apt-config_0.8.12-1_all.deb
2. Install the package with the following command
sudo dpkg -i mysql-apt-config_0.8.12-1_all.deb
3. Select ubuntu bionic, MySQL Server & Cluster,  mysql-5.7 and ok to finish
4. Update APT repo using the following command
sudo apt update
5. To check whether MySQL 5.7 repository has been successfully installed, execute:
sudo apt-cache policy mysql-server
6. Install MySQL 5.7 and set root password:
sudo apt install -f mysql-client=5.7* mysql-community-server=5.7* mysql-server=5.7*


The project was guided by the following guidelines and objectives:
Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

General
What is the main role of a database
What is a database replica
What is the purpose of a database replica
Why database backups need to be stored in different physical locations
What operation should you regularly perform to make sure that your database backup strategy actually works

Requirements
General
Allowed editors: vi, vim, emacs
All your files will be interpreted on Ubuntu 16.04 LTS
All your files should end with a new line
A README.md file, at the root of the folder of the project, is mandatory
All your Bash script files must be executable
Your Bash script must pass Shellcheck (version 0.3.7-5~ubuntu16.04.1 via apt-get) without any error
The first line of all your Bash scripts should be exactly #!/usr/bin/env bash
The second line of all your Bash scripts should be a comment explaining what is the script doing
