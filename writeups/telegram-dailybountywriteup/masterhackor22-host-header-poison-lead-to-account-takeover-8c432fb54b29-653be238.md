# Host Header Poison lead to account takeover

- **Source URL:** https://medium.com/@masterhackor22/host-header-poison-lead-to-account-takeover-8c432fb54b29?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20240306180943/https://medium.com/@masterhackor22/host-header-poison-lead-to-account-takeover-8c432fb54b29?source=rss------bug_bounty-5
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/5481 (id 5481)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Host Header Poison lead to account takeover

Just now

While iam testing private program at hackerone i told to myself to start with host header poison in reset password (my lovely bug)

I have a list of ways that i do at any bounty program in host header to bypass host validations.

ways:

1- Host: attacker.com/target.com

2-attacker.com/.target.com

3-target.com.net or target.cc or attacker.target.com

and another ways that i use

In our private program i bypass host validation with target.io.burpcollabrator.oastify.com

and as expected i got host header poison at reset password that leads to account takeover
