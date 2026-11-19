# Four Redirects, One URL, Full Account Takeover

- **Source URL:** https://medium.com/codetodeploy/four-redirects-one-url-full-account-takeover-an-oauth-chain-autopsy-426b0f65f73f
- **Fetched from:** https://web.archive.org/web/20261111075314/https://medium.com/codetodeploy/four-redirects-one-url-full-account-takeover-an-oauth-chain-autopsy-426b0f65f73f
- **Fetched:** 2026-11-19
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14962 (id 14962)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
Member-only story

# Four Redirects, One URL, Full Account Takeover: An OAuth Chain Autopsy

*Not one sophisticated bug. Three string comparisons that were each almost right.*

*Uber paid $7,500 for the cleanest version of this chain in 2017. The first report in the class is from 2014, and the newest version of it shipped seven days ago. Every version dies at the same place: a string comparison that was clever instead of exact.*


In April 2014, a researcher named **melvin** reported that a Meteor-built app called Respondly had an open redirect in its Twitter OAuth flow — *“obtaining the OAuth token and verifier of the victim,”* as the report puts it. A month later, the OAuth working group published Security Advisory 2014.1 and gave the pattern a name: **Covert Redirect.**

Twelve years later, in April 2026, LY Corporation paid $1,000 for an open redirect on page.line.me that sent an OAuth authorization code to an attacker-controlled endpoint. Same class. Same year the class turned twelve.

The chain never died, and I want to show you why — hop by hop, through the reports that got paid for it.

*⚠️ Verification note: HackerOne’s report pages loaded this session but returned truncated content — I could confirm titles, reporter handles, and the technical mechanism for several reports, but not the specific severity ratings, bounty*…
