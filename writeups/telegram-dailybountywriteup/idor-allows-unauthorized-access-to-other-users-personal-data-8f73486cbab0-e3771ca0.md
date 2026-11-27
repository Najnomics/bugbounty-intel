# IDOR Allows Unauthorized Access to Other Users’ Personal Data

- **Source URL:** https://brbr0s.medium.com/idor-allows-unauthorized-access-to-other-users-personal-data-8f73486cbab0?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250821171932/https://brbr0s.medium.com/idor-allows-unauthorized-access-to-other-users-personal-data-8f73486cbab0
- **Fetched:** 2026-11-27
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/9561 (id 9561)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# IDOR Allows Unauthorized Access to Other Users Personal Data

**﷽**

Hi mates, I’m Mahmoud — aka [**brbr0s**](https://x.com/brbr0s) — . I’m a bug hunter who’s always trying to learn more and get better at what I do. I’m mainly focused on red teaming fields and hope to go deeper in this track in the future.

In this blog, I’ll be sharing some of the bugs I find and the things I learn along the way.

Let’s get started

In this writeup I’ll demonstrate how I got an IDOR that allows me to fetch other users Personally Identifiable Information (PII): `Email`, `Phone`, `Name`, `Country`,..etc.

I’ll hide the site behind `example.com` to maintain company privacy.

**Detecting the vulnerable field**

I spend a while exploring the website’s functions with the burp proxy in the background, first section I decided to test is the profile user for some opening bugs like: CSRF, IDOR, Cache P/D,…

While moving to IDOR, I notice a POST request that have a `userId` with a value -in a Salesforce format- like this `005VM000007BILCYA4` with 18-digits length

The Original Request Looks Like:

```
POST /webruntime/api/apex/execute
Host: my.example.com
Content-Type: application/json
{
  "namespace": "",
  "classname": "@udd/01p6S000009d5Kp",
  "method": "getUserinfo",
  "isContinuation": false,
  "params": {
    "userId": "005VM000007BILCYA4",
    "networkId": "0DB6S000000TOwlWAG"
  },
  "cacheable": false
}
```
I tried using another `userId` for an account I own, it works!!

**Publish hacking approach**

I notice that the first 11-digit `005VM000007` are fixed in each of other accounts, so we still have 7-digits and bruteforcing is useless here.

Through burp-search I notice a request that used a slightly similar ID `005VM000007BILC`, but It looks shorter than normal

So yep it strips the last 3-digits `YA4`, and It also works in the previous request.

*A new thing noted about Salesforce format:*

\- The **first 15 characters** are the **core object ID**.

\- The **last 3 characters** are just a **case-insensitive checksum**.

\- Internally, Salesforce will still recognize the record using just the 15-character version.


so we simply have 4-digits `BILC` to bruteforce on, with a simple wordlist from a wordlist generator [crunch](https://github.com/jim3ma/crunch)

`crunch 4 4 ABCDEFGHIJKLMNOPQRSTUVWXYZ -d 1 -o wordlist.txt`
Launch our Intruder we got 200 OK with A real User IDs

Appending it into the POST request, we got the user PII

tips

1. Don’t trust UUIDs, check if u can shorten it to apply bruteforcing.
2. Use the Old School Technique and spend a while browsing the site’s functions, don’t don’t don’t rely only on automation

Let’s connect on [X](https://x.com/brbr0s)
