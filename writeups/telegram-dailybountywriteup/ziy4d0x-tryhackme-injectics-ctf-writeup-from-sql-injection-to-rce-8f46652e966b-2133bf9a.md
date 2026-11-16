# TryHackMe Injectics CTF Writeup

- **Source URL:** https://medium.com/@ziy4d0x/tryhackme-injectics-ctf-writeup-from-sql-injection-to-rce-8f46652e966b
- **Fetched from:** https://medium.com/feed/@ziy4d0x
- **Fetched:** 2026-11-16
- **Channel:** @dailybountywriteup
- **Telegram message:**  (id 14905)
- **Method:** medium-rss-content readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
### TryHackMe Injectics: From SQLi to RCE

### Introduction

*In this write-up, I will walk through my approach to solving the Injectics CTF on TryHackMe \[*[https://tryhackme.com/room/injectics](https://tryhackme.com/room/injectics)*\].*

*I’ll cover the reconnaissance process, vulnerability discovery, exploitation, and how the vulnerabilities can be chained together to achieve command execution.*

🎯The goal is to retrieve the admin flag and discover the hidden text file inside the flags directory.

### Stage 1: Reconnaissance

Let’s start with an Nmap Scan:

nmap \<Tareget-Ip> -p- -sV

Results

Since our entry point is probably the web server, we scan for possible directories and pages using gobuster

gobuster dir -u http://\<target IP> -w \<wordlist> -x php,json,html,txt

This reveals that a flags folder exists for the 2nd flag, but when I try to open it

Next, I went to the composer.json directory to see what versions of libraries are allowed.

### Stage 2: Web Enumeration

Since HTTP is available on the target, I opened Firefox and navigated to http://\<Target-IP>. The web application loaded successfully, displaying the default webpage.

After manually investigating the website, I found that, as a regular visitor, I could access only two main pages: **Home** and **Login**.

As part of my usual enumeration process, I also inspected the page source for any interesting comments or information left by the developer. As expected, I found a critical comment that could potentially open a new path for further investigation.

\<!-- Website developed by John Tim - dev@injectics.thm-->

\<!-- Mails are stored in mail.log file-->

Comments leaved by developer in home page source code

When try to open the “mail.log” file, I was able to see a message written by the developers.

The mail revealed an interesting detail: a background monitoring service named **Injectics** runs every minute and restores the users table with default credentials if the table is deleted or corrupted.

This gave me an interesting attack path. If I could delete the users table through SQL Injection, the monitoring service would recreate it with the default credentials, potentially allowing me to authenticate as the **superadmin** user.

Next, I inspected the source code of the **Login** page. There, I discovered a JavaScript file named script.js that implements a client-side filter intended to prevent SQL Injection.

```
$("#login-form").on("submit", function(e) {
    e.preventDefault();
    var username = $("#email").val();
    var password = $("#pwd").val();
 const invalidKeywords = ['or', 'and', 'union', 'select', '"', "'"];
            for (let keyword of invalidKeywords) {
                if (username.includes(keyword)) {
                    alert('Invalid keywords detected');
                   return false;
                }
            }
    $.ajax({
        url: 'functions.php',
        type: 'POST',
        data: {
            username: username,
            password: password,
            function: "login"
        },
        dataType: 'json',
        success: function(data) {
            if (data.status == "success") {
                if (data.auth_type == 0){
                    window.location = 'dashboard.php';
                }else{
                    window.location = 'dashboard.php';
                }
            } else {
                $("#messagess").html('<div class="alert alert-danger" role="alert">' + data.message + '</div>');
            }
        }
    });
});
```
The script handles the login process entirely through JavaScript. Instead of allowing the form to submit normally, it intercepts the request and checks the username against a list of SQL-related keywords.

If the input passes the filter, the username and password are sent to functions.php through an AJAX request. A successful response redirects the user to dashboard.php, while an unsuccessful attempt displays an error message.

*💡* ***Hint:*** *The filter runs* ***client-side****, so inspect how script.js checks and blocks SQL-related keywords before the request reaches the server.*

### Stage 3: SQL Injection Discovery & Exploitation

To automate the SQL Injection discovery process, I used **SQLMap** against the captured login request.

Then, I tried **MySQL-specific SQL Injection payloads** manually in the login form, but I couldn’t bypass it because of the **client-side JS filter**

So, using Burp Suite, I intercepted a login request and sent it to Intruder to try multiple SQLi payloads from My SQL payloads wordlist to bypass &logging in.

### Stage 4: Logging in as Superadmin & Retrieving the First Flag

After bypassing the login filter and gaining access as a **developer-level user**, I investigated the available functionality. The **Edit** feature provided an opportunity to interact with the database, which I used to trigger the SQL Injection and delete the users table.

Once the users table was deleted, I waited for the Injectics service to restore it. The table was recreated with the default credentials mentioned by the hint, allowing me to log in as the **superadmin** and retrieve the admin-panel flag.

| Email                     | Password                |

|---------------------------|-------------------------|

| superadmin@injectics.thm | superSecurePasswd101 |

| dev@injectics.thm | devPasswd123 |

### Stage 5: Discovering and Exploiting Twig SSTI

**During enumeration, I inspected the application’s configuration and discovered it was using Twig 2.14.0.**

While testing the **Update Profile** section, I then try the following payload **{{7\*’7’}}** to see if it is indeed susceptible to SSTI. If we get 49 as a result, then the webserver has a SSTI vulnerability.

### Stage 6: SSTI to RCE & Gets Second Flag

Next, I researched the **Twig 2.14.0** vulnerability and found that the sort filter is affected by [**CVE-2022-23614**](https://nvd.nist.gov/vuln/detail/cve-2022-23614).

I tested the CVE payload:

`{{ ['whoami',' ']|sort('passthru') }}`
- \['whoami', ' '\] ⇒ provides the command string.
- sort('passthru') ⇒ in the vulnerable Twig behavior, treats passthru as a PHP callable.
- passthru ⇒ executes the supplied string as an OS command.

So the chain is:

**SSTI ⇒ vulnerable** ***sort* ⇒ PHP callable ⇒** ***passthru()* ⇒ OS command execution.**

#### Getting the Second Flag

First, I used ls to check the files in the current directory and understand the available paths.

Then, I ran ls -al flags to inspect the /flags directory, which revealed a .txt file containing the second flag.

But before displaying the hidden file, I knew the current working directory through “**pwd**”

`{{ ['pwd',' ']|sort('passthru') }}`
Finally, I used cat to read the file and retrieve the flag.

`{{ ['cat /var/www/html/flags/5d8af1dc14503c7e4bdc8e51a3469f48.txt',' ']|sort('passthru') }}`
The command executed successfully, revealing the **second flag**.

At the end, I hope you enjoyed reading this write-up and found it useful and informative.
