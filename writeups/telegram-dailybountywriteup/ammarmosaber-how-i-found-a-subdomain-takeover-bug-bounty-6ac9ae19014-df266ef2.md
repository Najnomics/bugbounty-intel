# How I Found a Subdomain Takeover | Bug bounty

- **Source URL:** https://medium.com/@ammarmosaber/how-i-found-a-subdomain-takeover-bug-bounty-6ac9ae19014?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20230725004701/https://medium.com/@ammarmosaber/how-i-found-a-subdomain-takeover-bug-bounty-6ac9ae19014
- **Fetched:** 2026-11-22
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/3256 (id 3256)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
**My Simple approach of how i found a subdomain takeover.**


Hi Bug Hunters,

My name is **Ammar Mo Saber** aka (xLe0x). Living in Egypt, and this is my first writeup in the community, So Let’s Jump into it.

# **What is Subdomain Takeover?**

According to MDN: *A subdomain takeover occurs when an attacker gains control over a subdomain of a target domain. Typically, this happens when the subdomain has a canonical name (CNAME) in the Domain Name System (DNS), but no host is providing content for it. This can happen because either a virtual host hasn’t been published yet or a virtual host has been removed. An attacker can take over that subdomain by providing their own virtual host and then hosting their own content for it.*

*If an attacker can do this, they can potentially read cookies set from the main domain, perform cross-site scripting, or circumvent content security policies, thereby enabling them to capture protected information (including logins) or send malicious content to unsuspecting users.*

*A subdomain is like an electrical outlet. If you have your own appliance (host) plugged into it, everything is fine. However, if you remove your appliance from the outlet (or haven’t plugged one in yet), someone can plug in a different one. You must cut power at the breaker or fuse box (DNS) to prevent the outlet from being used by someone else.*

# **So How i find subdomain takeovers?**

I was doing recon on a target with a huge scope and assets on hackerone. i fired up my VPS. collected the domains in scope and added them to a file and launched my script to do the easy recon.

First I did Subdomain Enumeration with subfinder and assetfinder.

```
subfinder -dL domains.txt -all -recursive -o subs.txt
cat domains.txt | assetfinder --subs-only | tee -a subs2.txt
```
Then started combining and filtering them. Then I did a HTTP Probing with httpx.

```
cat subs.txt subs2.txt | sort -u | tee -a all-subs.txt
cat all-subs.txt | httpx | tee -a live-subs.txt
```
Let’s Do Some HTTP Screenshotting with httpx.

`cat live-subs.txt | httpx -screenshot`
It will screenshot every live subdomain and save it to output/screenshot

After Doing all of this. let’s check the images taken by httpx. and a one caught my eyes.

It was an unclaimed AWS Bucket. after some search i found a great resource [https://github.com/EdOverflow/can-i-take-over-xyz](https://github.com/EdOverflow/can-i-take-over-xyz) and it says it’s a possible subdomain takeover. after creating an AWS account and some trying to takeover it. finally i did it!!

I reported it and after 3 days. It’s Resolved. 🟢

Thanks For Following up. if you want to follow me.

Twitter: [https://twitter.com/ammarxle0x](https://twitter.com/ammarxle0x)
