# ALX System Engineering & DevOps

## Overview

This repository contains comprehensive system engineering and DevOps projects covering shell scripting, networking, web infrastructure, CI/CD pipelines, monitoring, and cloud deployment. The projects progress from fundamental shell commands through advanced infrastructure automation and deployment practices.

## Repository Structure

The repository is organized into 22 progressive system engineering and DevOps projects:

### Core Projects Summary

This repository covers:
- **Shell Scripting** (0x00-0x06) - Bash fundamentals and advanced scripting
- **Networking** (0x07-0x08) - TCP/IP networking concepts
- **Web Infrastructure** (0x09-0x1B) - Web servers, load balancing, monitoring, and debugging

## Detailed Project Breakdown

### Shell Scripting Fundamentals (0x00-0x06)

| # | Project | Focus | Key Concepts |
|---|---------|-------|---------------|
| 0x00 | Shell Basics | Introduction to shell scripting | Bash syntax, variables, commands |
| 0x01 | Shell Permissions | File permissions and chmod | Access control, ownership |
| 0x02 | Shell Redirections | Input/output redirection | stdin, stdout, stderr, pipes |
| 0x03 | Shell Variables | Environment and shell variables | Variable expansion, scope |
| 0x04 | Loops, Conditions & Parsing | Control flow structures | if/else, loops, parameter parsing |
| 0x05 | Processes & Signals | Process management | Background processes, signals, PID |
| 0x06 | Regular Expressions | Pattern matching with regex | grep, sed, awk, pattern syntax |

[View Shell Projects](./0x00-shell_basics)

### Networking & Infrastructure (0x07-0x08)

| # | Project | Focus | Key Concepts |
|---|---------|-------|---------------|
| 0x07 | Networking Basics | TCP/IP fundamentals | OSI model, protocols, DNS |
| 0x08 | Networking Basics 2 | Advanced networking | Ports, services, SSH, telnet |

[View Networking Projects](./0x07-networking_basics)

### Web Infrastructure & DevOps (0x09-0x1B)

| # | Project | Focus | Key Concepts |
|---|---------|-------|---------------|
| 0x09 | Web Infrastructure Design | Architecture planning | Web servers, load balancers, databases |
| 0x0A | Configuration Management | Infrastructure as Code | Puppet, configuration automation |
| 0x0B | SSH | Secure shell administration | SSH keys, authentication, tunneling |
| 0x0C | Web Server | Web server setup | Nginx, Apache configuration |
| 0x0D | Web Stack Debugging 0 | Troubleshooting skills | Log analysis, debugging techniques |
| 0x0E | Web Stack Debugging 1 | Advanced debugging | Performance issues, error tracking |
| 0x0F | Load Balancer | Load balancing setup | HAProxy, traffic distribution |
| 0x10 | HTTPS/SSL | Security implementation | HTTPS, SSL/TLS certificates |
| 0x11 | Firewall | Network security | UFW, iptables, firewalls |
| 0x12 | Web Stack Debugging 2 | Complex troubleshooting | Full stack debugging |
| 0x13 | Firewall Continued | Advanced firewall | Complex firewall rules |
| 0x14 | MySQL Database | Database administration | MySQL setup, optimization, backup |
| 0x15 | API | RESTful API development | API design, implementation |
| 0x16 | API Advanced | Advanced API patterns | Authentication, versioning |
| 0x17 | Web Stack Debugging 3 | Integration debugging | Multi-component debugging |
| 0x18 | Webstack Monitoring | System monitoring | Monitoring tools, alerting |
| 0x19 | Postmortem | Incident analysis | Post-incident reviews, documentation |
| 0x1A | Application Server | App server configuration | Gunicorn, uWSGI, Flask/Django deployment |
| 0x1B | Web Stack Debugging 4 | Final debugging challenges | Complex real-world scenarios |

[View Web Infrastructure Projects](./0x09-web_infrastructure_design)

---

## Technology Stack

### Languages & Scripting
- **Bash/Shell** - Primary scripting language
- **Python** - Scripting and automation
- **Ruby** - Configuration management
- **JavaScript** - Some web scripting

### Infrastructure Tools
- **Nginx** - Web server
- **Apache** - Web server alternative
- **HAProxy** - Load balancer
- **MySQL** - Database server
- **Puppet** - Configuration management
- **UFW** - Firewall management

### Monitoring & DevOps
- **Datadog** - System monitoring
- **New Relic** - Performance monitoring
- **Grafana** - Visualization
- **Prometheus** - Metrics collection

## Learning Outcomes

By working through these projects, you will:

✓ Master Bash/Shell scripting and automation  
✓ Understand TCP/IP networking fundamentals  
✓ Configure and manage web servers (Nginx, Apache)  
✓ Implement load balancing strategies  
✓ Set up and manage databases (MySQL)  
✓ Implement security best practices (HTTPS, firewalls)  
✓ Debug complex system issues  
✓ Monitor and optimize infrastructure  
✓ Design scalable web architectures  
✓ Implement infrastructure as code principles  
✓ Handle incident response and postmortems  
✓ Deploy applications to production  

## Installation & Setup

### Prerequisites
- Linux/Unix environment (Ubuntu/Debian recommended)
- Basic command line knowledge
- sudo access for system configuration
- Text editor (vim/nano)

### Getting Started

1. Clone the repository:
   ```bash
   git clone https://github.com/gomolemontlhane/alx-system_engineering-devops.git
   cd alx-system_engineering-devops
   ```

2. Navigate to a specific project:
   ```bash
   cd 0x00-shell_basics
   ```

3. Review the project requirements:
   ```bash
   cat README.md
   ```

4. Execute scripts:
   ```bash
   bash script_name.sh
   # or
   ./script_name.sh
   ```

## Project Structure (Per Project)

Each project directory typically contains:

- **README.md** - Project documentation and requirements
- **Scripts** - Executable shell/Python scripts (.sh, .py)
- **Configuration files** - Config files for servers/services
- **Test files** - Test scripts for validation
- **Documentation** - Additional reference materials

## Common Tasks & Examples

### Running Shell Scripts
```bash
# Make executable
chmod +x script.sh

# Run the script
./script.sh

# Or with bash
bash script.sh
```

### Testing Infrastructure
```bash
# Check web server status
sudo systemctl status nginx

# Restart services
sudo systemctl restart nginx

# View logs
tail -f /var/log/nginx/error.log
```

### Network Diagnostics
```bash
# Check connections
netstat -an
# or modern alternative
ss -an

# DNS lookups
nslookup example.com
dig example.com

# Network tracing
traceroute example.com
```

## Key Concepts Covered

### Shell Scripting
- Variables and parameter expansion
- Control flow (if/else, loops)
- Functions and scripts
- Input/output redirection
- Regular expressions
- Process management

### Networking
- TCP/IP protocol suite
- DNS and domain names
- Ports and services
- Network tools (netstat, nslookup, traceroute)
- SSH and secure connections

### Web Infrastructure
- Web server configuration
- Load balancing algorithms
- SSL/TLS encryption
- Database design
- Firewalls and security
- Monitoring and alerting
- Application deployment

### DevOps Practices
- Infrastructure as Code (IaC)
- Configuration management
- CI/CD pipelines
- Monitoring and logging
- Incident response
- Automation and scripting

## Resources

### Shell Scripting
- [GNU Bash Manual](https://www.gnu.org/software/bash/manual/)
- [ShellCheck](https://www.shellcheck.net/) - Shell script analysis
- [Regular Expressions Tutorial](https://www.regular-expressions.info/)

### Networking
- [TCP/IP Guide](http://www.tcpipguide.com/)
- [Linux Network Administration](https://linux-training.be/)

### Web Infrastructure
- [Nginx Documentation](https://nginx.org/en/docs/)
- [HAProxy Manual](http://www.haproxy.org/)
- [MySQL Documentation](https://dev.mysql.com/doc/)

### DevOps
- [Puppet Documentation](https://puppet.com/docs/)
- [Infrastructure as Code](https://www.terraform.io/)
- [Linux Academy DevOps](https://linuxacademy.com/)

## Best Practices

### Shell Scripting
- Use `#!/bin/bash` shebang
- Quote variables: `"$var"`
- Check for errors: `set -e`
- Use meaningful names
- Add comments and documentation
- Test scripts thoroughly

### Infrastructure
- Document your architecture
- Use version control for configs
- Implement monitoring early
- Plan for scalability
- Automate everything
- Test in staging first

### Security
- Keep systems updated
- Use strong authentication
- Implement firewalls
- Encrypt data in transit (HTTPS)
- Regular security audits
- Monitor for threats

## Troubleshooting

### Common Issues

| Issue | Solution |
|-------|----------|
| Permission denied | Make script executable: `chmod +x script.sh` |
| Command not found | Ensure script has correct shebang |
| Connection refused | Check service status and firewall rules |
| Timeout errors | Check network connectivity and DNS |
| Database errors | Verify MySQL is running and credentials are correct |

## Contributing

Contributions are welcome! Feel free to:

- Improve existing scripts
- Add documentation
- Report issues
- Suggest optimizations
- Share alternative approaches
- Add additional projects

## Author

**Gomolemo Ntlhane**

- GitHub: [@gomolemontlhane](https://github.com/gomolemontlhane)
- Focus: System engineering, DevOps, infrastructure automation

## License

This project is part of the ALX Software Engineering program curriculum.

---

## Quick Reference

### Important Directories

| Directory | Purpose |
|-----------|----------|
| `/etc` | Configuration files |
| `/var/log` | Log files |
| `/home` | User home directories |
| `/root` | Root home directory |
| `/tmp` | Temporary files |
| `/var/www` | Web server files |

### Essential Commands

| Command | Purpose |
|---------|----------|
| `ls` | List files |
| `cd` | Change directory |
| `sudo` | Run as superuser |
| `systemctl` | Manage services |
| `journalctl` | View logs |
| `netstat/ss` | Network status |
| `grep` | Search text |
| `awk/sed` | Text processing |

### Port Numbers to Remember

| Port | Service |
|------|----------|
| 22 | SSH |
| 80 | HTTP |
| 443 | HTTPS |
| 3306 | MySQL |
| 5432 | PostgreSQL |
| 6379 | Redis |

---

**Last Updated:** 2025  
**Status:** Active Development  
**Difficulty:** Intermediate to Advanced
