# Reflected XSS on Admin Login Page

- **Source URL:** https://infosecwriteups.com/reflected-xss-on-admin-login-page-94960596ec88?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20230409154745/https://infosecwriteups.com/reflected-xss-on-admin-login-page-94960596ec88
- **Fetched:** 2026-11-19
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/2085 (id 2085)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Reflected XSS on Admin Login Page

Hi! I’m Aswin,security researcher and a penetration tester.Here we are discussing reflected XSS in a private bug bounty program.

On the website [https://xyz.redacted.com/a6,](https://xyz.redacted.com/a6,) when you attempt to access secret sections,The URL on the parameter “win” redirects you to a login page with values from the URL mirrored in the DOM.

A cross-site scripting attack might be launched against the application since there is no adequate handle for the data reflected, making it susceptible.


# What is reflected cross-site scripting?

Reflected Cross-Site Scripting occurs when the injected script is mirrored off the website, such as an error message, search result, or other response.

Reflected type assaults are given to victims or targets through another channel, such as email or phishing.

When the user is duped into clicking the malicious script or link, the browser is triggered.

The search field is a basic example of Reflected XSS.

To launch a successful Reflected XSS attack, an attacker looks for instances where user input is utilised directly to create a response.

This frequently includes the inclusion of event attributes such as onload and onmouseover to elements that are not supposed to host scripts, such as image tags (img>).

# Proof of Concept:

When you visit the current URL, an alert with your cookie will appear on the screen.

# Steps To Reproduce:

1. Navigate to [https://xyz.redacted.com/a6](https://td.intelliresponse.com/a6)
2. Now that you’ve been forwarded to the login page, look for the win parameter on the URL and replace it with some payload beginning with “>” and some text or script in front.
3. See the completed payload on your screen.

# Recommendation:

Remediation for XSS often entails cleaning data input (to ensure that no code is present), escaping all output (to ensure that data is not shown as code), and re-structuring applications such that code is loaded from well-defined destinations.

# Impact:

- Accessing sensitive data, or even gaining control of user accounts
- An attacker may create a payload to extract a user’s admin credentials or steal his session.

Happy Hacking..
