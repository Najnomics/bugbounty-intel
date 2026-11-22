# Discovering Login Panels and Detecting SQL Injection with Logsensor

- **Source URL:** https://medium.com/@qaafqasim/discovering-login-panels-and-detecting-sql-injection-with-logsensor-42842e337244?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20241219152141/https://medium.com/@qaafqasim/discovering-login-panels-and-detecting-sql-injection-with-logsensor-42842e337244
- **Fetched:** 2026-11-22
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/3086 (id 3086)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Discovering Login Panels and Detecting SQL Injection with Logsensor

## Great Tool for Web Application Security Testing

# Features

**1. Login Panel Scanning for Multiple Hosts**

Logsensor empowers you to scan multiple hosts and detect login panels seamlessly. By analyzing the content length and employing advanced techniques, it effectively identifies potential login pages.

**2. Proxy Compatibility**

Logsensor offers proxy compatibility for both HTTP and HTTPS protocols. You can configure the tool to utilize proxies, enhancing your ability to analyze and monitor network traffic.

**3. Efficient Multithreading**

The tool’s scanning process leverages multiprocessing, enabling it to handle a large number of URLs swiftly. This multithreaded approach ensures efficient and speedy login panel detection.

# Installation

To get started with Logsensor, follow these simple steps:

Clone the Logsensor repository from GitHub

*git clone https://github.com/Mr-Robert0/Logsensor.git*

Set the necessary permissions for the execution scripts

`sudo chmod +x logsensor.py install.sh`
Install the required dependencies

`pip install -r requirements.txt`
Execute the installation script

`./install.sh`
# Quick Tutorial

# 1. Multiple Hosts Scanning to Detect Login Panels

You can use Logsensor to scan multiple hosts and detect potential login panels. By default, the tool utilizes 30 threads for scanning. You can adjust the thread count as per your requirements.

- Run the login detector module with a subdomains list

`python3 logsensor.py -f <subdomains-list>`
- Increase the number of threads to 50 (or any desired value)

`python3 logsensor.py -f <subdomains-list> -t 50`
- Run only the login panel detection module

`python3 logsensor.py -f <subdomains-list> --login`
# 2. Targeted SQLi Form Scanning

Logsensor also offers the ability to perform targeted SQLi form scanning on specific login panel URLs. You can customize various parameters to suit your needs.

- Provide the URL of the login panel and run SQLi form scanning

`python logsensor.py -u www.example.com/login --sqli`
- Enable proxy support to monitor requests (using 127.0.0.1:8080 as an example)

`python logsensor.py -u www.example.com/login -s --proxy http://127.0.0.1:8080`
- Customize the user input name of the login panel (default: “username”)

`python logsensor.py -u www.example.com/login -s --inputname email`
*For detailed tutorials, bug bounty tips, Ethical hacking, cybersecurity, and infosec-related work make sure to check out the My Medium Profile https://medium.com/@qaafqasim*

#bugbounty #cybersecurity #bughunting #pentesting #logsensor #securitytools #ethiclahacking #cybersecuirty #infosec
