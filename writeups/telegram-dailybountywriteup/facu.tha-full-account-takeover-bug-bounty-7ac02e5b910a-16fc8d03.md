# Full account takeover — Bug bounty

- **Source URL:** https://medium.com/@facu.tha/full-account-takeover-bug-bounty-7ac02e5b910a?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20231111172123/https://medium.com/@facu.tha/full-account-takeover-bug-bounty-7ac02e5b910a
- **Fetched:** 2026-11-19
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/4198 (id 4198)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Full account takeover — Never give up

--

Hi everyone,

I’d like to share a brief story about how I managed to gain control of the administrative account for this application.

The scope of work was this page, which I am going to call **target.com.** It was an empty login page.

I started off by doing some fuzzing. **Dirsearch/Gobuster/Waybackurls** gave me nothing. I tried to manually input parameters, and nothing.

I started playing with Burp Suite, and here things get interesting! Che

I tried login in:

I tried resetting the password:

**I was able to try different emails and I would tell me if it existed or not.**

I changed the POST request to GET and I got:

But then I thought to myself, what if I do a GET request to API/USERS?

I got 64 records!!

I felt like 👇🏼👇🏼 haha

Then I made a request to

`main.js`
Found several paths from the app. But I did not think it was going to work, HOWEVER, admin/country-dashboard bypassed all the access controls and I was inside of the app as an **ADMIN**

At this point I was already writing my report, but I kept digging with Burp Suite, and found more info:

**Encrypted password of the admin account! No need to decrypt it at this point.**

I was also able to create a new account from the admin’s panel. But this was enough to show the critical impact of all the vulnerabilities found.

**Tools used:**

```
Dirsearch
Gobuster
waybackurls
Burp Suite
```
`Thanks for reading!`
