# Task 1: Distributed Web Infrastructure

This project focuses on designing a distributed web infrastructure for hosting the website www.foobar.com.

## Design Overview

The infrastructure comprises multiple servers and components for redundancy, scalability, and fault tolerance:

- **2 servers**: Provide redundancy and scalability.
- **1 web server (Nginx)**: Handles incoming HTTP requests.
- **1 application server**: Executes the application logic.
- **1 load balancer (HAproxy)**: Distributes incoming traffic among servers.
- **1 set of application files (code base)**: Contains the codebase for the website.
- **1 database (MySQL)**: Stores and manages structured data.

## Specifics Explained

- **Additional elements**: Added for redundancy, scalability, and fault tolerance.
- **Distribution algorithm for load balancer**: Configured with round-robin to evenly distribute incoming requests.
- **Active-Active setup**: All servers actively handle incoming requests, ensuring high availability.
- **Primary-Replica database cluster**: Primary node accepts writes, replica nodes serve reads, ensuring scalability and fault tolerance.
- **Difference between Primary and Replica nodes**: Primary handles writes, ensuring data consistency, while replicas serve reads, improving scalability.

## Issues Identified

- **Single Point of Failure (SPOF)**: Load balancer or database can become a single point of failure.
- **Security concerns**: Lack of firewall and HTTPS encryption expose the infrastructure to security threats.
- **No monitoring**: Without monitoring, it's challenging to detect and address performance issues or security breaches.

## Screenshots

Screenshot of the whiteboard diagram for Task 1 can be found at https://imgur.com/tAmWqFz.

