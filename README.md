# Project Title:Todo Master

**Project Description:**
This project is a comprehensive guide on setting up and configuring a basic web server using the Apache HTTP
Server.

## Table of Contents

- [Introduction](#introduction)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Testing](#testing)
- [License](#license)
- [Contact](#contact)

## Introduction
This project provides step-by-step instructions on how to install and configure Apache HTTP Server on a Linux
system. It covers everything from downloading the source code to running your first web page.

## Prerequisites
Before you begin, ensure that you have the following installed on your system:

- A Linux distribution (e.g., Ubuntu, CentOS)
- Basic knowledge of command-line operations

## Installation

### Step 1: Update Your Package Manager
First, update your package manager to make sure you get the latest versions of packages and their dependencies.

```bash
sudo apt-get update
```

### Step 2: Install Apache HTTP Server
Install Apache HTTP Server using your distribution's package manager.

For Ubuntu/Debian:
```bash
sudo apt-get install apache2
```

For CentOS/RHEL:
```bash
sudo yum install httpd
```

## Configuration

1. **Enable Apache to Start on Boot**
   ```bash
   sudo systemctl enable apache2  # For Ubuntu/Debian
   sudo systemctl enable httpd    # For CentOS/RHEL
   ```

2. **Start the Apache Service**
   ```bash
   sudo systemctl start apache2  # For Ubuntu/Debian
   sudo systemctl start httpd    # For CentOS/RHEL
   ```

3. **Configure Firewall**
   If you have a firewall enabled, make sure to allow traffic on port 80 (HTTP).

   For Ubuntu/Debian:
   ```bash
   sudo ufw allow 'Apache'
   ```

   For CentOS/RHEL:
   ```bash
   sudo firewall-cmd --permanent --zone=public --add-service=http
   sudo firewall-cmd --reload
   ```

## Usage

Once Apache is running, you can access your server by navigating to `http://<your_server_ip>` in a web browser.

To serve a custom website:
1. Create an HTML file:
   ```bash
   echo "<html><body><h1>Welcome to My Website!</h1></body></html>" > /var/www/html/index.html
   ```

2. Access your new website via the browser.

## Testing

You can test if Apache is serving files correctly by checking the default index page:

```bash
curl http://localhost
```

If you see the "Welcome to My Website!" message, then Apache is working as expected.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

For any questions or feedback, feel free to contact us at:

- Email: saeedurooj0@gmail.com
- GitHub Issues: (https://github.com/Urooj1112)

---


**Note:** This is a basic guide. Depending on your specific needs, further configuration and security measures may
be required.