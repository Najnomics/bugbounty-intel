# How an IDOR Can Wreak Havoc

- **Source URL:** https://medium.com/@karanshergill_/how-an-idor-can-wreak-havoc-breaking-through-the-front-door-9573bce64e08?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20230308054923/https://medium.com/@karanshergill_/how-an-idor-can-wreak-havoc-breaking-through-the-front-door-9573bce64e08
- **Fetched:** 2026-11-24
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/1873 (id 1873)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# How IDOR’s Can Wreak Havoc: Breaking through the front door!

Insecure Direct Object Reference (IDOR) is a common vulnerability in web applications that can allow an attacker to bypass authorization checks and access resources they shouldn’t be able to.

In this article, we’ll explore an IDOR vulnerability in the “Cap” machine on the Hack The Box platform. We’ll walk through the steps to identify and exploit the vulnerability, ultimately demonstrating how an IDOR vulnerability can lead to a complete compromise of the target system.

By the end of this article, you will have a better understanding of the IDOR vulnerability and how it can be used to exploit web applications. You will also learn about the importance of proper input validation and access control in securing web applications against such attacks. Let’s dive in!

Target IP address: 10.10.10.245


# Reconnaissance:

To begin our assessment of the target, we’ll start with a NMAP scan to identify open ports and services on the target system. This will help us understand the attack surface and identify potential vulnerabilities that we can exploit.

To run the NMAP scan use the following command.


```
> nmap -Pn -p- --max-rate 500 10.10.10.245
# -Pn : skips the ping scan.
# -p- : scan all TCP ports.
# --max-rate : sets the maximum packet rate per second.
```
## Scan Results:

- Port 21 (FTP) — open.
- Port 22 (SSH) — open.
- Port 80 (HTTP) — open.

# Attack Surface:

When conducting reconnaissance it’s important to prioritize the ports that are most likely to contain high-value targets or vulnerabilities. Since port 80 is the default port for HTTP traffic and is therefore a common target for web application vulnerabilities which make it’s a logical starting point for exploring the system’s attack surface.

While ports 21 and 22 may also be worth exploring, they are typically associated with FTP and SSH services, respectively. These ports are less likely to provide direct access to a web application or other high-value targets.

Using a web browser navigate to the IP address of the target system on port 80 to check if there is a web application running.


## Observations:

- The webpage looks like a security dashboard.
- A user “Nathan” is already logged in.
- The panel on the left has three buttons (Security Snapshot, IP Config and Network Status).

Let’s click on each button to understand what is going on and the purpose of the web application.

The Security Snapshot (/capture) hangs for 5 seconds, and then redirects to /data/16 where it returns a list of packets. The page also provides a download functionality which allows the user to download the data. The data is returned in “.pcap” format which can be accessed using “Wireshark”. After viewing the PCAP file it is seen that the file contains all the packets which were sent and received between the attacker and the target machine as below:

Let’s try to change the integer value in the URL to 1 as below:


The attempt was successful and the data is available for download. Let’s download the file and look into it. After inspecting the “1.pcap” file using “Wireshark ” we found that it contains packet exchange data for another user which confirms that an IDOR exists and the web application is vulnerable since we were able to exfiltrate data of another user. However, this data did not provide any useful information so we have to look for other “.pcap” files which can be exfiltrated.

The functionality is worth diving in deep so it would be a better idea to write a bash one-liner which is able to download all the “.pcap” files available on the target system in order to inspect and analyze them.


```
> mkdir pcaps
> seq 0 50 | xargs -I{} -P10 wget -q 10.10.10.245/download/{} -O pcaps/{}.pcap
```
After inspecting all the files, credentials of the user “Nathan” were found in one of them (0.pcap).

## Credentials:

Username: nathan, Password: Buck3tH4TF0RM3!

# Exploitation:

Since we had found during our reconnaissance that FTP and SSH ports are open let’s try to use there credential to login.

## FTP Login:

We managed to successfully login using the credentials found.

## SSH Login:

The same credentials worked for SSH as well and allowed us to successfully login as the user “Nathan”.

# Privilege Escalation:

The `home` directory of the user “Nathan” does not contain any information which can be used to further build our way for privilege escalation neither there are any other users available on the target machine. We will have to look for another route to gain elevated privileges.

Let’s navigate to the `/var/www/html` directory and look for the source code of the web application.

## Source Code Analysis:

The “capture” is using `os.system` to call `tcpdump`with a five second timeout and saves it in the upload directory with the current pcapid prepending the .pcap extension to the file name.

In order to call tcpdump the user must be root, or have certain capabilities. The Python is calling `os.seduid(0)` at the start of the function which makes it root.

Note: Not any application can call `setuid(0)` it should be a privileged process.


After checking sudo permissions, SUID binaries and capabilities that could escalate the privileges by giving us a root shell we found that the python3.8 binary has `cap_setuid` capability set.

`cap_setuid` is a Linux capability that allows a process to change its own user ID to any other UID, including UID 0, which corresponds to the root user. This capability can be useful for privilege escalation attacks, because it allows a process to elevate its privileges to that of the root user without having to obtain root access.

Let’s exploit this using the python command below to gain root access.


`python3 -c 'import os; os.setuid(0); os.system("/bin/bash")'`
The command elevates the privileges of the current process to that of the root user, and then launches a new interactive shell.

Successfully Exploited!


# Wrapping Up!

We successfully exploited the IDOR vulnerability and further elevated our privileges on the target machine! Through this exercise, we have demonstrated the devastating consequences that such a vulnerability can have on a system’s security posture, and highlighted the importance of thoroughly testing web-applications for these types of flaws.

By starting with a simple Nmap scan and leveraging a combination of tools and techniques, we were able to identify and exploit the IDOR vulnerability, ultimately gaining full control of the target machine. This underscores the need for robust testing and secure coding practices, as even a seemingly minor oversight can have severe consequences for the security of an application or system.

**Disclaimer**: The information provided in this article is intended for educational and research purposes only. Any actions and/or activities related to the material contained in this article is solely the read’s responsibility. The author of this article is not responsible for any misuse of the information provided. Always use ethical and legal means to conduct security testing and research.
