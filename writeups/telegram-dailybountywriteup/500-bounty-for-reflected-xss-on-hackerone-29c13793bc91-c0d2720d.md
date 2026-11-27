# $500 Bounty for Reflected XSS on HackerOne

- **Source URL:** https://osintteam.blog/500-bounty-for-reflected-xss-on-hackerone-29c13793bc91?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250506033331/https://osintteam.blog/500-bounty-for-reflected-xss-on-hackerone-29c13793bc91
- **Fetched:** 2026-11-27
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/9558 (id 9558)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
Member-only story

# $500 Bounty for Reflected XSS on HackerOne

## How a Security Researcher Earned $500 by Discovering Reflected XSS on HackerOne

## Introduction

Bug bounty platforms are often seen as the most secure hardened places on the internet. After all their audience is security researchers actively looking for vulnerabilities! But even the best platforms aren’t immune to the occasional slip.

In today’s write up we’re covering a reflected XSS vulnerability discovered on HackerOne itself earning a $500 bounty. This bug affected both [www.hackerone.com](http://www.hackerone.com) and resources.hackerone.com two high profile subdomains.

The vulnerability was responsibly reported by Eric (todayisnew) under report ID #840759. Let’s dive into how it worked why it mattered and what we can learn from it

## The Vulnerable Endpoints

Eric identified two endpoints vulnerable to reflected XSS:

These pages allowed embedding mini resource widgets via GET parameters opening the door to reflected user-controlled input.

The vulnerable parameter was part of an embedded widget URL used for reading resources. By…
