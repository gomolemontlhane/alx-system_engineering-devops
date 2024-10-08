# Task 2: Secured and Monitored Web Infrastructure

This project focuses on designing a secured and monitored web infrastructure for hosting the website www.foobar.com.

## Design Overview

The infrastructure comprises multiple servers and additional security and monitoring components:

- **3 servers**: Provide redundancy and scalability.
- **3 firewalls**: Enhance security by filtering network traffic.
- **1 SSL certificate**: Enables HTTPS encryption for secure communication.
- **3 monitoring clients**: Collect data for performance monitoring and security analysis.
- **1 web server (Nginx)**: Handles incoming HTTP requests.
- **1 application server**: Executes the application logic.
- **1 database (MySQL)**: Stores and manages structured data.

## Specifics Explained

- **Additional elements**: Added for enhanced security and monitoring.
- **Firewalls**: Filter network traffic to prevent unauthorized access and protect against security threats.
- **SSL certificate**: Encrypts data exchanged between the server and clients to ensure confidentiality and integrity.
- **Monitoring clients**: Collect data on system performance and security events for proactive management and troubleshooting.
- **Monitoring tool**: Used to collect and analyze data collected by monitoring clients for insights into system health and security.

## Issues Identified

- **Terminating SSL at the load balancer level**: Exposes traffic to potential eavesdropping and compromises confidentiality.
- **Single MySQL server capable of accepting writes**: May lead to downtime and data loss if the server fails.
- **Homogeneous server components**: Increases vulnerability to widespread failures or exploits due to uniformity.

## Screenshots

Screenshot of the whiteboard diagram for Task 2 can be found https://imgur.com/cXw5F6d.
