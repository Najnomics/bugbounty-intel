# Server-Side Request Forgery $(SSRF)$ allows internal ports scanning

- **Source URL:** https://medium.com/h7w/server-side-request-forgery-ssrf-allows-internal-ports-scanning-ef7edf6534b7?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20241211184419/https://medium.com/h7w/server-side-request-forgery-ssrf-allows-internal-ports-scanning-ef7edf6534b7
- **Fetched:** 2026-11-19
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/7865 (id 7865)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Server-Side Request Forgery $(SSRF)$ allows internal ports scanning

Read For Free- [https://nexguardians.com/blind-ssrf-allows-internal-ports-scanning/](https://nexguardians.com/blind-ssrf-allows-internal-ports-scanning/)

Hi everyone, I am socalledhacker, i am a security researcher , penetration tester, certified ethical hacker and a web3 noob. In past months, I have discover lots of bugs but in today’s article we are going to discuss about low hanging fruits or P4 vuln’s as they are very easy to find and also present in almost every website. So let’s start with our first vulnerability.

# Server-Side Request Forgery (SSRF) allows internal ports scanning

Recently I was hunting on a large wide scope program and i found an interesting server side request forgery bug in form field and then i escalate it to make it’s bigger impact, so let’s dive into how i found this bug and how you can try to find this similar issue on other applications.

Let’s say the program name is example.com and there is a subdomain like helpdesk.example.com in this subdomain user can submit their queries by filling a form, I thought that there is a possibility of SSRF there. So, i fire up my burpsuite and put my collaborator URL in first, last name, subject, description and also insert collaborator URL in description insert link section, and submit the form.
