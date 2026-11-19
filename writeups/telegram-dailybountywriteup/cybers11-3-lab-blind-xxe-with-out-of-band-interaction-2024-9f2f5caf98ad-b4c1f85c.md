# cybers11.3 Lab

- **Source URL:** https://infosecwriteups.com/cybers11-3-lab-blind-xxe-with-out-of-band-interaction-2024-9f2f5caf98ad?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20240304060508/https://infosecwriteups.com/cybers11-3-lab-blind-xxe-with-out-of-band-interaction-2024-9f2f5caf98ad
- **Fetched:** 2026-11-19
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/5417 (id 5417)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# 11.3 Lab: Blind XXE with out-of-band interaction | 2024

## This lab has a “Check stock” feature that parses XML input but does not display the result. You can detect the blind XXE vulnerability by triggering out-of-band interactions with an external domain. To solve the lab, use an external entity to make the XML parser issue a DNS lookup and HTTP request to Burp Collaborator | Karthikeyan Nagaraj

# Description

This lab has a “Check stock” feature that parses XML input but does not display the result.

You can detect the blind XXE vulnerability by triggering out-of-band interactions with an external domain.

To solve the lab, use an external entity to make the XML parser issue a DNS lookup and HTTP request to Burp Collaborator.

# Solution

1. Visit a product page, click “Check stock” and intercept the resulting POST request in [Burp Suite Professional](https://portswigger.net/burp/pro).
2. Insert the following external entity definition in between the XML declaration and the `stockCheck` element.
3. Right-click and select "Insert Collaborator payload" to insert a Burp Collaborator subdomain where indicated:

4\. Replace the `productId` number with a reference to the external entity: `&xxe;`

5\. Go to the Collaborator tab, and click “Poll now”. If you don’t see any interactions listed, wait a few seconds and try again. You should see some DNS and HTTP interactions that were initiated by the application as the result of your payload.

A YouTube Channel for Cybersecurity Lab’s Poc and Write-ups

Telegram Channel for Free Ethical Hacking Dumps

Thank you for Reading!

Happy Ethical Hacking \~

`Author: Karthikeyan Nagaraj ~ Cyberw1ng`
