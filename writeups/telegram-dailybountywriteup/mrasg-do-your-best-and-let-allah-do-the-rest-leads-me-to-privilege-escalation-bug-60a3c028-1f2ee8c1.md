# “Do Your Best, and Let Allah Do the Rest” led me to a Privilege Escalation Bug

- **Source URL:** https://medium.com/@mrasg/do-your-best-and-let-allah-do-the-rest-leads-me-to-privilege-escalation-bug-60a3c028c802?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20241221113535/https://medium.com/@mrasg/do-your-best-and-let-allah-do-the-rest-leads-me-to-privilege-escalation-bug-60a3c028c802
- **Fetched:** 2026-11-21
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/8229 (id 8229)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# “Do Your Best, and Let Allah Do the Rest” led me to a Privilege Escalation Bug

Hey, folks!

This is a story about a privilege escalation vulnerability (or a pre-account takeover scenario) I stumbled upon. But rather than diving headfirst into technical jargon, I want to take you on a fun, inspiring journey — a tale of doing your best, trusting that Allah will handle the rest.

The moral? Don’t give up. Even when faced with setbacks or the dreaded “Duplicate” tag, keep going. Success often lurks just around the corner.

# Chapter 1: The Hunt Begins

The target? A public program on HackerOne, brimming with juicy subdomains. Why this program? Well, it pays well. And seriously, who wants to spend countless hours on a program that doesn’t reward your effort?

Among the subdomains, two caught my eye:

1. **org.example.com:** Used to create and manage organizations. Fun fact: You don’t need to verify your email to set up an account. This platform allows users to create projects and invite others with roles like Owner, Admin, or Member Manager via invitation links sent to their emails.
2. **account.example.com**: Dedicated to managing user accounts and security features (think 2FA, phone numbers, etc.).

# Chapter 2: The Frustrating Grind

I started testing **account.example.com**, exploring everything — unverified emails, bypassing email confirmation, password recovery, and bypassing invitation links. I even tried swapping email addresses or duplicating them across accounts. Nothing. Nada. Zilch.

But persistence is key, right?

While testing the 2FA phone number feature, I noticed this HTTP request during the SMS confirmation step:

`sms_auth%5Bdelivery_method%5D: +201001234567`
What if I changed the phone number and sent the request?

Bingo!

The server accepted my modified phone number without needing to verify it.

Cool! But what was the impact?

This is awesome, but what’s the impact? Every program needs an impact, at least on one of the three: Confidentiality, Integrity, or Availability

# Initial Impact Analysis

I brainstormed possible scenarios, eventually landing on this:

**Preventing Specific Users from Logging In**

An attacker could:

1. Add a victim’s phone number to a new account.
2. Use a Python script to exhaust the SMS confirmation attempts, Preventing the victim from access their account.

I reported this low-severity issue with detailed steps. The response? **Duplicate.** Worse, the original report was submitted only 18 hours before mine! Ouch.

# Chapter 3: Rising from the Ashes

Naturally, I was disappointed. 18 hours! That’s less than a day. I felt dejected and unmotivated. But then I remembered the noble saying (Hadith) of Prophet Muhammad (ﷺ):

*“*لو أنكم تتوكلون على الله حق توكله، لرزقكم كما يرزق الطير، تغدو خماصًا وتروح بطانًا*.”*


The message? Keep working hard, trust in Allah, and believe that your efforts will bear fruit. So, I dusted myself off and moved on to another program.

# Chapter 4: The Unexpected Twist

Weeks later, while working on a completely different program, I needed to integrate it with the first platform (yes, the one where I got the “Duplicate”). I logged into **org.example.com** using one of my old accounts and noticed something new: a pending invitation to join an organization.

This wasn’t here before!

I’m sure it was added recently — it’s new, I can feel it!

I checked the platform’s update logs. There is a recent change allowing users to accept invitations directly through their accounts or through invitation email.

Wait… What? My email in this account wasn’t even verified. And yet, I can got the invitation acceptance form!

# The Eureka Moment

I realized this:

1. If an organization owner invites an email address to their team, anyone can create an account using that email and accept the invitation.
2. This could lead to two attack scenarios:

- **Internal Attack**: A low-privilege user in the organization creates a new account using an invited higher-privilege member’s email and accepts the invitation, escalating their privileges.
- **External Attack**: A bad actor guesses or collects potential invitee emails, creates accounts with those emails, and waits for invitations to roll in.

This was huge! A privilege escalation vulnerability with wide-reaching implications.

This is such a cool vulnerability! What’s even better is that it’s scalable, meaning an attacker can target a huge number of organizations using the site, just by gathering information to get the potential emails of employees in those organizations. And the best part? It came with almost no effort on my part! I’m a bit shy if I say it’s due to my skills or expertise… but honestly, it’s just a help of Allah !

*“*لو أنكم تتوكلون على الله حق توكله، لرزقكم كما يرزق الطير، تغدو خماصًا وتروح بطانًا*.”*


# Chapter 5: The Sweet Victory

I submitted a detailed report with:

1. Clear attack scenarios.
2. A Python script to automate email account creation and monitor invitations.
3. A video walkthrough of the exploit.

The result? Accepted with a **Medium severity rating** for the following reasons:

But what truly warmed my heart were the notifications I received about my report later on.

More than 10 duplicate reports of my original masterpiece!

On a serious note, I truly felt that Allah compensated me with something far better than what I was upset about, and none of my efforts went in vain

# Final Thoughts

This journey taught me a valuable lesson: persistence pays off. Sometimes, it’s not about skill or experience but simply about showing up, putting in the effort, and trusting Allah .

So, to all bug hunters out there: keep going. Your next big find might just be around the corner.

Happy hunting, and thank you for reading!
