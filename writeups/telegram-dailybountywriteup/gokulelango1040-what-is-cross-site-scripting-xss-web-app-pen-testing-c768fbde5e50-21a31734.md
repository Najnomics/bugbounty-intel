# What is cross-site scripting (XSS)? Web App Pen-testing

- **Source URL:** https://medium.com/@gokulelango1040/what-is-cross-site-scripting-xss-web-app-pen-testing-c768fbde5e50?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20230122001442/https://medium.com/@gokulelango1040/what-is-cross-site-scripting-xss-web-app-pen-testing-c768fbde5e50
- **Fetched:** 2026-11-24
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/1476 (id 1476)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# What is cross-site scripting (XSS)? Web App Pen-testing

Cross-site scripting (also known as XSS) is a web security vulnerability that allows an attacker to compromise the interactions that users have with a vulnerable application.

# How does XSS work?

Cross-site scripting works by tricking a vulnerable website into returning harmful JavaScript to users. The attacker has complete control over the victim’s ability to interact with the application once the malicious code has been allowed to run inside the victim’s browser.

# What are the types of XSS attacks?

1. Reflected XSS
2. Stored XSS
3. DOM-based XSS

# Reflected XSS

where the malicious script comes from the current HTTP request.

Example

Suppose a website has a search function like this

[https://iScanMe](https://iScanMe).com/search?term=nmap

If any other search validation functions are not performed then the attacker can able to write an malicious java script code in that field.

`https://iScanMe.com/search?term=<script>/*+Bad+stuff+here...+*/</script>`

If you send this URL to victim,then them machine will be compromised.You can able to redirect your victim to your malicious websites.

# Stored XSS

Also known as Persistent XSS, this type of vulnerability occurs when untrusted or unverified user input is stored on a target server

`<p><script>/* Bad stuff here... */</script></p>`

# DOM-based XSS

Document Object Model-based Cross-site Scripting is often known as DOM XSS. If the web application writes data to the Document Object Model without sufficient sanitization, a DOM-based XSS attack may be conceivable. The attacker can use this data to insert XSS material, such as malicious JavaScript code, on the website.

*Thank you for Reading This content.I hope you got some Knowledge from this post.Grow your Knowledge with medium.*
