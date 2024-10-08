# Task 0: Simple Web Stack

This project focuses on designing a simple web stack comprising various components to host the website www.foobar.com.

## Design Overview

The infrastructure consists of the following components:

- **1 server**: Hosts all the necessary components.
- **1 web server (Nginx)**: Handles incoming HTTP requests.
- **1 application server**: Executes the application logic.
- **1 application files (code base)**: Contains the codebase for the website.
- **1 database (MySQL)**: Stores and manages structured data.

## Specifics Explained

- **What is a server?**: A server is a computer or system that provides services or resources to other computers, known as clients, over a network.
- **Role of the domain name**: The domain name maps to the IP address of the server, making it easier for users to access the website.
- **Type of DNS record for www.foobar.com**: www is typically a CNAME record pointing to the main domain, foobar.com.
- **Role of the web server (Nginx)**: Handles incoming HTTP requests and serves web pages or application content.
- **Role of the application server**: Executes the application logic and processes dynamic content.
- **Role of the database**: Stores and manages structured data used by the application.
- **Communication with the user's computer**: The server communicates with the user's computer over the Internet using the HTTP protocol.

## Issues Identified

- **Single Point of Failure (SPOF)**: Any component failure can lead to the website being inaccessible.
- **Downtime during maintenance**: Performing maintenance tasks like deploying new code may result in temporary downtime.
- **Scalability concerns**: The infrastructure may not handle high incoming traffic efficiently.

## Screenshots

Screenshot of the whiteboard diagram for Task 0 can be found at https://imgur.com/ZvPZV9t
