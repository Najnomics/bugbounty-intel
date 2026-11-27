# CSRF On Delete Profile

- **Source URL:** https://medium.com/@josuofficial327/csrf-on-delete-profile-high-severity-7-1-hackerone-33bdb598ef67?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20241223134052/https://medium.com/@josuofficial327/csrf-on-delete-profile-high-severity-7-1-hackerone-33bdb598ef67
- **Fetched:** 2026-11-27
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/8230 (id 8230)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# CSRF On Delete Profile: High Severity(7.1) HackerOne

I have been hunting on bugs almost for a year now and this is my first high severity bug on hacker-one with a severity rating 7.1.

Like every other day, I was checking for some bugs on a private program which I figured out the same day. After checking its features for some time I came to understand it was a website for paying the taxes and other community programs. Their was an option to create account , I tried some easy bugs like hyperlink injection, ssrf and some open redirects but none working out…

I know always we need to analyse patiently for understanding the working of anything, so even though none of my techniques was working out initially I just browsed the website. At that time I found a delete account option, I thought to check for “no verification on sensitive actions” I clicked the delete account and to my surprise my account was deleted and I was in the login page.

I knew something is coming on, I suddenly went to my burp and created another account their and captured the delete account request and created a csrf poc and saved it in my desktop on .html file(make sure to save it on all files). Then on my chrome I created another account and logged in, then. I clicked the submit button from the csrf poc and 🤯 MY ACCOUNT WAS DELETED .

I submitted the bug putting the severity medium on csrf and after one day they triaged the report and moved the severity to High 7.1.
