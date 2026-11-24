# Day 04

- **Source URL:** https://iamrudhh.medium.com/day-04-bug-bounty-introduction-to-reconnaissance-43d041655c37
- **Fetched from:** https://iamrudhh.medium.com/feed
- **Fetched:** 2026-11-24
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14997 (id 14997)
- **Method:** medium-rss-content readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
Most bug bounty wins don’t come from clever payloads. They come from finding the thing nobody else looked at. That’s what recon is for. Here’s what Day 04 of the series covers.

### 1. What is Recon?

Reconnaissance is information gathering before you test anything. The goal is to map the attack surface: every domain, endpoint, technology, and entry point that could be tested.

There are two types:

- **Passive recon**: collecting information without touching the target’s systems (search engines, public records, archives)
- **Active recon**: directly interacting with the target (port scans, crawling, probing endpoints)

Always read the program’s scope first. If it’s not in scope, don’t touch it.

### 2. Find Subdomains

The main domain is usually the most hardened. Subdomains are where forgotten apps, staging servers, and old admin panels live. Every subdomain you find expands your scope.

- **crt.sh**: search certificate transparency logs for %.target.com
- **subfinder**: fast passive subdomain enumeration
- **amass**: deeper enumeration with multiple data sources

bash

subfinder -d target.com -o subs.txt

Save everything to a file. You’ll feed it into the next steps.

### 3. Technology Detection

Once you know what exists, find out what it runs on. Knowing the stack tells you which vulnerabilities and misconfigurations to look for.

- **Wappalyzer**: browser extension for frameworks, CMS, server, and analytics
- **WhatWeb**: command-line fingerprinting
- **Response headers**: Server, X-Powered-By, and cookie names often give it away

bash

whatweb target.com

A WordPress site, an old Apache version, and a Laravel app each call for a different approach.

### 4. Public Information

This is passive recon at its purest: collect what’s already public, without interacting with the target.

- **Google dorking**: site:target.com filetype:pdf, site:target.com inurl:admin
- **Wayback Machine**: old pages, removed endpoints, forgotten files
- **GitHub**: leaked repos, config files, exposed keys in public commits
- **Shodan**: exposed services and internet-facing assets

Log everything. A random old endpoint today can be your finding next week.

### Quick Recap

1. Recon = mapping the attack surface
2. Subdomains = more scope, more opportunities
3. Tech detection = know the stack before you test
4. Public info = free intel with zero interaction

Stay in scope, take notes, and build a repeatable recon workflow.

Following along? Next up: Day 05.

**@iamrudhh**
