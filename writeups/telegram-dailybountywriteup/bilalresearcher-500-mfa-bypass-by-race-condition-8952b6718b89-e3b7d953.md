# 500$

- **Source URL:** https://medium.com/@bilalresearcher/500-mfa-bypass-by-race-condition-8952b6718b89?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20240817022217/https://medium.com/@bilalresearcher/500-mfa-bypass-by-race-condition-8952b6718b89
- **Fetched:** 2026-11-27
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/7002 (id 7002)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# 500$: MFA bypass By Race Condition

The article is about a bug I found when I was trying to break the other logic in the software. But instead i founded a way to bypass the MFA by Race Condition.

Last year I was hunting on a private program and I hit a point where it asked for MFA to generate the API key, and there was a limit of 10 API keys. I tried to make more than 10, and I found that using Race Condition I could bypass the MFA without code.

*The Flow*


The API keys generated in the integration process are crucial for accessing and controlling Exendly accounts. MFA is implemented to ensure that only genuine users can generate these keys, preventing unauthorized access and potential misuse. The discovered vulnerability compromises the integrity of MFA, potentially granting unauthorized users control over admin accounts.

*Bug Description*


My testing has uncovered a significant security issue within Exendly’s(Virtual name of bbp) integration platform, specifically related to Multi-Factor Authentication (MFA). The bug allows an attacker to exploit a race condition during the generation of API tokens, potentially leading to unauthorized access and compromising the security of Exendly’s accounts.

When users attempt to generate API tokens on the integration platform, the MFA process is initiated to enhance account security. However, a flaw in the system allows attackers to manipulate the sequence of events, exploiting a race condition. This manipulation can lead to the generation of API tokens without the need for a valid MFA code.

*Before we move on, if you like my write-ups, please support me by liking, sharing, and clapping up to 50 times here on Medium, it’s free. Thank you.*


# STEPS TO REPRODUCE

1. Visit [https://exendly.com/integrations/api\_webhooks](https://calendly.com/integrations/api_webhooks).
2. Click the “Generate Token” button to trigger the MFA challenge.
3. Intercept the request to POST /api/integrations/personal\_access\_tokens.

```
POST /api/integrations/personal_access_tokens HTTP/2
Host: Exendly.com
Cookie: 
Dnt: 1
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: same-origin
Te: trailers
```
`{"label":"aa"}`
4\. Employ a tool like Turbo Intruder to initiate a race condition attack.

5\. Observe responses, identifying instances where API tokens are generated without a valid MFA code, signified by 200 OK responses.

*The Bounty*


The Exendly team paid me 500$ for the bug i found and submitted as a token of appreciation.

*Takeaway*


The takeaway from this article is always try something maybe you won;t get what you are looking for maybe you get something else and important than what you are looking for as i m just trying to bypass the max 10 api key limits and i got a MFA bypass.

Leave some clap if you enjoyed this read, leave your feedback in comment and consider following me for more exciting findings.


**Find me on Twitter**: @[bilalresearcher](https://x.com/bilalresearcher)
