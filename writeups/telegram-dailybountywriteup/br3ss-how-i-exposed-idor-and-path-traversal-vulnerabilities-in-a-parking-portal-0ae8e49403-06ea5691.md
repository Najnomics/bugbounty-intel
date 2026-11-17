# How I Exposed IDOR and Path Traversal Vulnerabilities in a Parking Portal

- **Source URL:** https://medium.com/@br3ss/how-i-exposed-idor-and-path-traversal-vulnerabilities-in-a-parking-portal-0ae8e4940306?source=rss------bug_bounty-5
- **Fetched from:** https://medium.com/feed/@br3ss
- **Fetched:** 2026-11-17
- **Channel:** @dailybountywriteup
- **Telegram message:**  (id 8409)
- **Method:** medium-rss-content readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
As a curious penetration tester with a knack for finding bugs where they least expect it, I recently stumbled upon a vulnerability that turned out to be more of a Pandora’s box than I initially imagined. Here’s the tale of how my innocent attempt to renew a parking permit led to uncovering some serious security flaws in a portal that manages parking payments and access to a limited traffic zone in my town.

### The Curious Case of the URL Parameter

It all started with a routine visit to the portal. I needed to renew my annual permit to access the limited traffic zone, so I logged into my personal account.

Once inside, I noticed something intriguing: the URL of my personal page included an identifier, something like:

[https://vulnerabledomain.com/manage/edit/1234](https://vulnerabledomain/manage/edit/1234)

Naturally, I was “user 1234.”

Now, if you’re familiar with the basics of security testing, you’ll know that seeing a numeric ID in a URL is like finding a big, red button that says, “Do Not Press.” So, I did what any curious hacker would do — **I pressed it**.

I replaced 1234 with another number and hit Enter. Voilà! I was redirected to another user’s profile page. Just like that, I had access to someone else’s personal information: their full name, address, phone number, and more.

An **Insecure Direct Object Reference (IDOR)** vulnerability was in the bag. I was pretty pleased with myself at this point. But as they say, the best was yet to come.

### The Receipt Revelation

After completing my renewal process, the system generated a payment receipt for me to download. The endpoint for this receipt looked like this:

[https://](https://entitlement.iamwebbing.com/subscription/generateFileStream?filePath=/date/receipt_number_1234.pdf)[vulnerabledomain.com](https://vulnerabledomain/manage/edit/1234)[/subscription/generateFileStream?filePath=/town/date/receipt\_number\_XXXX.pdf](https://entitlement.iamwebbing.com/subscription/generateFileStream?filePath=/date/receipt_number_1234.pdf)

Now, given the IDOR issue I’d just discovered, I couldn’t help but wonder: What happens if I tweak this endpoint? Could I access other users’ receipts? Could I go even further?

### A Path Traversal Adventure

I started testing for **Path Traversal** vulnerabilities. Using Burp Suite to analyze responses, I noticed that the server header indicated:

Server: Microsoft-IIS

Hmm, a Microsoft server. My next move was clear: time to hunt for configuration files. I tried accessing various paths, and after a few attempts, I hit the jackpot:

%2Fweb.config

Drumroll, please…

Puff! There it was — fully accessible, containing sensitive configuration data. And when I say sensitive, I mean *really sensitive*:

- Credentials for external services
- Credential of administrator user (in plain text!)
- Tokens for PayPal access
- Database connection strings

Suddenly, I was staring at a treasure trove of information that no one should have access to.

### The Emotional Rollercoaster

At this point, I felt a mix of emotions:

- **Excitement** because my persistence had paid off.
- **Terror** because I’d just stumbled upon a massive security flaw.

The portal wasn’t part of any bug bounty program, so I had no idea how to approach them without looking like a malicious actor. I decided to tread carefully.

### Responsible Disclosure (a.k.a. Not Getting Arrested)

I drafted a polite email to their technical team, explaining the issue with as much delicacy as I could muster. To my relief, they were understanding and appreciative of my report. While I didn’t receive a monetary reward, I did earn the satisfaction of knowing I’d helped make their system a little safer.

**How would you approach reporting a critical bug to a company that doesn’t have a bug bounty program?** It’s not an easy question — let me know your thoughts in the comments!

### Lessons Learned

1. Always test responsibly. Curiosity is great, but ethics matter even more.
2. Path Traversal and IDOR vulnerabilities can coexist in surprising ways.
3. If a system isn’t part of a bug bounty program, approach with caution and kindness.

Although I didn’t walk away with a reward, this experience gave me invaluable insights and an exciting story to share. If you’re reading this, consider it a nudge to secure your systems better — and maybe launch a bug bounty program while you’re at it.

Working to make the internet a safer place. Happy hacking! 👨💻
