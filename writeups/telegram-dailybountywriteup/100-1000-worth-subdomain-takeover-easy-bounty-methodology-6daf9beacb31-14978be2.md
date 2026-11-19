# $100-$1000 Worth Subdomain Takeover | Easy Bounty Methodology

- **Source URL:** https://infosecwriteups.com/100-1000-worth-subdomain-takeover-easy-bounty-methodology-6daf9beacb31?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250511133738/https://infosecwriteups.com/100-1000-worth-subdomain-takeover-easy-bounty-methodology-6daf9beacb31
- **Fetched:** 2026-11-19
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/9315 (id 9315)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
Member-only story

# $100-$1000 Worth Subdomain Takeover | Easy Bounty Methodology

Practical & Step-by-Step guide to find Subdomain Takeover Vulnerability

Hi geeks, ***it4chis3c*** ([Twitter](https://x.com/it4chis3c)) came-up with another bounty earning write-up in the Bug Bounty Hunting Series:

# Step-by-Step Process

## Step 1: Recon

Collect subdomains (you can use more tools if you want to discover more subdomains)

```
subfinder -d example.com -silent | anew subs.txt  
amass enum -passive -d example.com | anew subs.txt  
```
Errors to look for majorly:

**AWS S3**: `NoSuchBucket` error in response.

**GitHub Pages**: `404 There isn't a GitHub Pages site here`.

**Heroku**: `No such app` error.

`cat subs.txt | dnsx -cname -resp | grep -iE 's3|github|heroku' > cnames.txt`
