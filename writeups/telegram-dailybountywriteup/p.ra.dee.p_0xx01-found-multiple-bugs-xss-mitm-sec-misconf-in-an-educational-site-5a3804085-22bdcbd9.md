# Found Multiple Bugs

- **Source URL:** https://medium.com/@p.ra.dee.p_0xx01/found-multiple-bugs-xss-mitm-sec-misconf-in-an-educational-site-5a3804085da0?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250121091050/https://medium.com/@p.ra.dee.p_0xx01/found-multiple-bugs-xss-mitm-sec-misconf-in-an-educational-site-5a3804085da0
- **Fetched:** 2026-11-23
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/5953 (id 5953)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Found Multiple Bugs :: XSS, MITM, Sec-MisConf :: In a GOVT Educational Site

Hello Hackers…….!!!! Hope you all are good.

*Intro: I am p\_ra\_dee\_p whom you all know as Professor0xx01. Today I am gonna to explain you my story about finding multiple bugs in an educational (College) Website. So, let’s dive into it.*

## **First Bug :: Cross Site Scripting (Xss)**

During the enumeration phrase, i have detected some open **“CkeEditor” (webeditor).** In this editor, a user can insert and run html codes into the browser according to their need.

Let’s Check how it looks like……

After searching some instances in google, i got a CVE: **CVE-2022–24728** defines that it’s vulnerable to XSS & instantly i switched to Burp to get the result.

## CVE-2022–24728:

*CKEditor4 is an open source what-you-see-is-what-you-get HTML editor. A vulnerability has been discovered in the core HTML processing module and may affect all plugins used by CKEditor 4 prior to version 4.18.0. The vulnerability allows someone to inject malformed HTML bypassing content sanitization, which could result in executing JavaScript code. This problem has been patched in version 4.18.0. There are currently no known workarounds.*

After going to Burp……………….

I found that there are multiple **Xss** vulnerability exists on this **ckeditor** page…!!!!!! Here I also detected the version of **CkeEditor is 4.3.3** which was a Vulnerable Javascript Dependency,,,, confirms the severity is serious.

## **Proof Of Concept :: XSS by Professor0xx01**

```
Xss<!--{cke_protected} --!><img src=x onerror=alert(`Professor0xx01`)> -->Attack
Xss<!--{cke{cke_protected}_protected} --!><img src=x onerror=alert(`Professor0xx01`)> Attack
```
**Note*: I have attached only one POC image (unless article will be too long); even though all the CVEs are valid for this “CKEDITOR — 4.3.3” web editor.***

## **Detected CVEs:**

## **Second Issue :: Man-In-The-Middle Attack (MITM-Terrapin Attack)**

During Recon, i have also detected that SSH port 22 is open. Here I have noticed the auth-methods & ssh version. But, the more interesting thing is that this SSH protocol is vulnerable to **CVE-2023–48795.**

# CVE-2023–48795

The SSH transport protocol with certain OpenSSH extensions, found in OpenSSH before 9.6 and other products, allows remote attackers to bypass integrity checks such that some packets are omitted (from the extension negotiation message), and a client and server may consequently end up with a connection for which some security features have been downgraded or disabled, aka a Terrapin attack. This occurs because the SSH Binary Packet Protocol (BPP), implemented by these extensions, mishandles the handshake phase and mishandles use of sequence numbers.

Learn More about …..…….

**NOTE**: *I didn’t go further for breaking the integrity of SSH, cause I don’t wish to do anything illegal.*

## **Third Issue: Security Misconfiguration**

When i am reviewing the endpoints, i also noticed that there is one another security misconfiguration exists.

**The Issue is** : *If the secure flag is set on a cookie, then browsers will not submit the cookie in any requests that use an unencrypted HTTP connection, thereby preventing the cookie from being trivially intercepted by an attacker monitoring network traffic. If the secure flag is not set, then the cookie will be transmitted in clear-text if the user visits any HTTP URLs within the cookie’s scope. An attacker may be able to induce this event by feeding a user suitable links, either directly or via another web site. Even if the domain that issued the cookie does not host any content that is accessed over HTTP, an attacker may be able to use links of the form http://example.com:443/ to perform the same attack.*

That’s all for this article nowwww….!!!!

*Thanks for reading !! follow me for more insightful writeups !!*

See you in the next article !! Bye !!

Happy Hunting\~\~

Keep Learning & Keep Securing \~\~
