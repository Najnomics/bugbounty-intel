# $500 Bounty on Reflected XSS on Shopify

- **Source URL:** https://medium.com/bug-bounty-writeups/500-bounty-on-reflected-xss-on-shopify-083925879077?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20240227005702/https://medium.com/bug-bounty-writeups/500-bounty-on-reflected-xss-on-shopify-083925879077
- **Fetched:** 2026-11-24
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/5356 (id 5356)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# $500 Bounty on Reflected XSS on Shopify

# What is XSS?

XSS stands for Cross Site Scripting. It is a vulnerability in web application where the attacker injects a malicious payload into the code of a website to gather valuable information of the victim or to lure the victim to take different action.

# what is Same Origin Policy and why does it matter?

Same Origin Policy (SOP) is a security mechanism where the browser prevents scripts to run from origin X to access the data with origin Y. Cross Site Scripting abuses this functionality to gain information of the victim and exploits it to steal sensitive information, perform unauthorized actions on behalf of users or hijack user sessions. On worse cases, it could also lead to Cross Site request forgery (CSRF) and data breaches.

# How does it work?

Three steps are included in XSS attack.

Step 1: The attacker injects malicious code into the vulnerable website.

Step 2: The victim logs into the application. As soon as the victim logs into the application, the malicious code is triggered.

Step 3: As soon as the code is executed, sensitive information is sent to the attacker who can impersonate the victim.

## What will you need to look for to find XSS?

You will need a parameter in the application where you can inject malicious code into the application.

So what was the vulnerable parameter in the Shopify application? It was `returnTo` parameter URL on help.shopify.com/en/support/confirm-account-details while trying to sign up for the account. So you’ll need an unverified account in order to perform the attack.

## What were the steps?

1. Open the link and change it to [https://help.shopify.com/en/support/confirm-account-details?returnTo=javascript:alert(document.cookie)](https://help.shopify.com/en/support/confirm-account-details?returnTo=javascript%3Aalert%28document.cookie%29)
2. It will prompt a login page. Log in to the application.
3. Press the back button to…
