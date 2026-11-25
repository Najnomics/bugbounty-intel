# How Use 6 Step To Find Ssrf — Bug Bounty Tuesday

- **Source URL:** https://medium.com/@kerstan/how-use-6-step-to-find-ssrf-bug-bounty-tuesday-acc44d806c08?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20240721001646/https://medium.com/@kerstan/how-use-6-step-to-find-ssrf-bug-bounty-tuesday-acc44d806c08?source=rss------bug_bounty-5
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/6715 (id 6715)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
Subscribed to: [https://medium.com/@kerstan](https://web.archive.org/web/20240721001646/https://medium.com/@kerstan)

Hello everyone, I’m Kerstan.

Today is Bug bounty Tuesday, I will share with you about how use 6 step to find ssrf in bug bounty.

So, let’s dive right in.

# Step 1: Subdomain Enumeration

- DNS Dumpster
- Sublist3r
- Amass
- Google Dorking
- Certificate Transparency Logs
- subdomainer

# Step 2: Find Live Domains

`cat all-domains.txt | httpx > all-live.txt`
# Step 3: Identify All URLs

`cat all-live.txt | gauplus -subs -b png,jpg,gif,jpeg,swf,woff,gif,svg -o allUrls.txt`
# Step 4: Injection Burp Collaborator URL in Parameters

`cat httpx.txt | grep “=” | ./qsreplace http://40ga7gynfy6pcg06ov.oastify.com > ssrf.txt`
# Step 5: Test for SSRF Vulnerabilities

`cat ssrf.txt | httpx -fr`
