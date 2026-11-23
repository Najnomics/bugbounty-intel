# The OAuth Oversight

- **Source URL:** https://medium.com/@nightcoders0/the-oauth-oversight-when-configuration-errors-turn-into-account-hijacks-5ed1f9c83d16?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20241104100629/https://medium.com/@nightcoders0/the-oauth-oversight-when-configuration-errors-turn-into-account-hijacks-5ed1f9c83d16
- **Fetched:** 2026-11-23
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/7761 (id 7761)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# The OAuth Oversight: When Configuration Errors Turn into Account Hijacks

Hey folks I hope you are doing well. I am back with another writeup on OAuth misconfiguration leads to account takeover. The premiere is set on YouTube for a PoC for in depth detailing.

While searching on for some program on Bugcrowd, I came across a program whose name I will not disclose here but have disclosed in my PoC on YouTube which will be uploaded soon. Make sure you watch it. I will keep the name here as **redacted.com,** now since I created an account using OAuth I noticed that there is a flaw in OAuth and it is misconfigured

**Steps To Reproduce:**

1. Go to the **redacted.com** and create an account using OAuth

2\. Attacker changes the email address to that of the victim email address

3\. Attacker then logs out of the account and then goes onto the OAuth and uses the previous email and gets logged into the victim account

4\. Attacker logs into the victim account, thus granting the whole account takeover

I got rewarded $$$ for this submission and I hope you all understood the steps. The premiere of the PoC is set and will release in 1–2 days. Follow me up for more writeup guys. Thank you!!!

LinkedIn: [https://www.linkedin.com/in/akash-suman-7b95572a1/](https://www.linkedin.com/in/akash-suman-7b95572a1/)

Twitter: [https://x.com/CyberGhostOps](https://x.com/CyberGhostOps)
