# My first Hall Of Fame with a chained Broken Access Control

- **Source URL:** https://infosecwriteups.com/my-first-hall-of-fame-with-a-chained-broken-access-control-76f9e2e0e467?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20230202215557/https://infosecwriteups.com/my-first-hall-of-fame-with-a-chained-broken-access-control-76f9e2e0e467
- **Fetched:** 2026-11-19
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/1596 (id 1596)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# My first Hall Of Fame with a chained Broken Access Control

This blog is about how I got my first HOF after chaining multiple bugs.

Let’s get started.

# What is Broken Access Control

In simple words, BAC means you are able to perform certain actions or fetch certain files which you are not authorized to.


# The Bug

Let’s name the program ***redacted.com***. After some enumeration I found a support page i.e. ***redacted.com/support*** which has a login feature. I created an account i.e. **Attacker1** and started exploring with it.

Later I found that you can create ticket in the help desk section. I simply files a test complaint and created a ticket and checked the Burp History I was a parameter named opener ID. Then I got two ideas, Rate Limit and IDOR.

## Bug 1: Rate Limit

For this, capture the request in Burp while submitting the ticket > send the request to intruder > add the position > start the attack. As expected, there was not Rate Limit and I was able to create as many tickets I want.

## Bug 2: IDOR

Since I already the ID parameter in request, I created another account i.e. **Attacker2** without wasting any time.

I created a ticket with the Attacker1’s account > Captured the request > changed the ID number with Attacker2’s ID > send the request to intruder > add the position > start the attack.

And as expected, It worked. I was able to create as many tickets as I want in other users help desk portal.

# Impact

By Doing so, an attacker can create many unwanted tickets which can be a hectic for the support team to close the tickets as well as the user’s too and can also spam the user’s email.
