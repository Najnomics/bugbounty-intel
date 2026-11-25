# Swagger-UI XSS Leading to Account Takeover on Crypto Exchange

- **Source URL:** https://scr1pty.medium.com/how-i-found-xss-in-swagger-ui-leading-to-account-takeover-on-bug-bounty-8d419c6b95d5?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250426141645/https://scr1pty.medium.com/how-i-found-xss-in-swagger-ui-leading-to-account-takeover-on-bug-bounty-8d419c6b95d5?source=rss------bug_bounty-5
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/6194 (id 6194)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Swagger-UI XSS Leading to Account Takeover on Crypto Exchange

# >Hello World!

Hello, scr1pty on touch! I’m a security guy who decided to change his life once and move my career from security management to ethical hacking. I conduct penetration tests full-time but in my free time I search for bugs. It’s my 1st blogpost and I hope you will find it interesting to you. This post is about how I found a Reflected XSS in Swagger-UI which leads to Account Takeover.

# >Recon Stage

As each hacker has their recon approach, I have mine as well *\[btw comment if you wanna a separate post about recon\]*. It’s a simple bash script that automates assetfinder, subfinder to search subdomains, and the httpx tool to probe for alive assets. My next step is always to use nuclei-templates, especially nuclei-templates/http/technologies. In parallel, I open all subdomain URLs with Wappalyzer to manually pick up low-hanging bugs (if there are any).

After one hour of nuclei scanning (as I usually work with large scopes), I found the Swagger-UI path on my target:

[https://redacted.com/swagger-ui/](https://web.archive.org/web/20250426141645/https://redacted.com/swagger-ui/)

I started to research any vulnerabilities for Swagger and immediately tried any authenticated API requests with curl but without authentication. I hoped there might be a misconfiguration that would allow access to user data or other sensitive files without authentication. Unfortunately, that didn’t work, but after some hours of research, I came across the following articles:

- [Hacking Swagger-UI: From XSS to Account Takeovers](https://web.archive.org/web/20250426141645/https://blog.vidocsecurity.com/blog/hacking-swagger-ui-from-xss-to-account-takeovers/)
- [How I Was Able to Steal Users’ Credentials via Swagger-UI DOM XSS](https://web.archive.org/web/20250426141645/https://medium.com/@AlQa3Qa3_M0X0101/how-i-was-able-to-steal-users-credentials-via-swagger-ui-dom-xss-e84255eb8c96)

# >The Exploit Idea

The idea is to create two publicly available files (find templates in the [above references](https://web.archive.org/web/20250426141645/https://medium.com/@AlQa3Qa3_M0X0101/how-i-was-able-to-steal-users-credentials-via-swagger-ui-dom-xss-e84255eb8c96)):

- **scripty.json**: This is a .json file as Swagger-UI configuration files accepted in .json extensions. This .json file refers to our second .yaml file.
- **scripty.yaml**: This .yaml file contains an XSS payload written in JavaScript. My payload for PoC purposes triggers a pop-up alert with document.cookie.

**Here is the tip:** If you don’t wanna host your server with exploit files — just upload them to your GitHub repository and use raw links.


# >Exploiting the Target

Now we are ready to exploit our target if it is vulnerable. We need to input our link to the .json file in the “configUrl” or “url” parameter by the target’s path:

[https://redacted.com/swagger-ui/index.html?configUrl=](https://web.archive.org/web/20250426141645/https://redacted.com/swagger-ui/index.html?configUrl=)

And see what happens:

When a victim accesses the above URL, the XSS payload is executed, which triggers a pop-up window that can capture and send the victim’s cookies to the attacker.

# >Result

As demonstrated, the payload currently triggers a pop-up for proof. Modifying this payload could allow an attacker to capture session tokens or cookies, enabling unauthorized access to the victim’s account, including admin privileges if the session belongs to an administrative user.
