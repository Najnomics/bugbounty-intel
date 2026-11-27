# Subdomain Takeover

- **Source URL:** https://medium.com/@ibnibrahim/subdomain-takeover-34bd662b5a7a?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20240817003546/https://medium.com/@ibnibrahim/subdomain-takeover-34bd662b5a7a
- **Fetched:** 2026-11-27
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/6813 (id 6813)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Subdomain Takeover

# بسم الله الرحمـن الرحيم

## What are subdomains?

A web application(test.com) has multiple subdomains(mail.test.com, calendar.test.com, inventory.test.com)

basically each subdomain is configured for certain tasks. Sometimes these subdomains are only accessible with certain privileges.

## What’s subdomain takeover?

Long story short, some subdomains may have aliases which are basically other names that redirect to the same subdomain, so if someone takes over an alias he theoretically took over the original subdomain as the clients will get redirected to the hacker’s subdomain.

## How to find them?

The subdomain’s alias should be unused; hence, a script could be written to automate the process of finding the subdomains that are vulnerable to takeover by checking the HTTP code they’re returning, and as you may have guessed, subdomains which return a **404 Not Found****nmap -p \[443/80 or http(s)’s port\] -A \[subdomain\]**

## How to exploit them?

Create an account on the web hosting service and claim a subdomain of the alias of that subdomain and just add any `index.html` file to prove you've gained access.

## PoC

[Behrouz Sadeghipour](https://medium.com/u/9a72584d6865?source=post_page-----34bd662b5a7a--------------------------------) has written a script in ruby that automates the process of finding unused subdomains for a specific domain, and you can find it here [HostileSubBruteforcer](https://github.com/nahamsec/HostileSubBruteforcer)

وَقُل رَّبِّ زِدْنِي عِلْمًا
