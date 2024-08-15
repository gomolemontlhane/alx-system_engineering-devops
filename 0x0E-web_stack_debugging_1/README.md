# Web Stack Debugging #1
This project focuses on troubleshooting and debugging issues related to a web stack setup, particularly focusing on Nginx configuration on Ubuntu 20.04 LTS.

## Scripts
### 0-nginx_likes_port_80
This Bash script checks if Nginx is installed on the system. If Nginx is not installed, it installs it using apt. The script then ensures that Nginx is configured to listen on port 80 by modifying the default Nginx configuration and restarting the Nginx service.

## Usage

Ensure the script is executable:
```bash
chmod +x 0-nginx_likes_port_80
```

Run the script with elevated privileges:
```bash
sudo ./0-nginx_likes_port_80
```
## Requirements
- All scripts are tested on Ubuntu 20.04 LTS.
- Bash scripts must pass ShellCheck without errors and run without any issues.
- Ensure proper permissions (chmod +x) before executing Bash scripts.
- Avoid using wget as per project guidelines.

## AUTHOR
Gomolemo Ntlhane
