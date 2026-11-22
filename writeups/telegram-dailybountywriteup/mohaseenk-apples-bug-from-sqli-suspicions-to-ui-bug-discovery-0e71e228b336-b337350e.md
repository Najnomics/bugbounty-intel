# Apple’s Bug

- **Source URL:** https://medium.com/@MohaseenK/apples-bug-from-sqli-suspicions-to-ui-bug-discovery-0e71e228b336?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20260622050445/https://medium.com/@MohaseenK/apples-bug-from-sqli-suspicions-to-ui-bug-discovery-0e71e228b336
- **Fetched:** 2026-11-22
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/5762 (id 5762)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Apple’s Bug: From SQLi Suspicions to UI Bug Discovery

Greetings, everyone!

Thank you for joining me as I discuss a recent discovery I made regarding a bug in Apple’s systems. In this article, I’ll share the journey of how I stumbled upon what initially appeared to be a SQL injection (SQLi) vulnerability, only to have it categorized by Apple as a UI bug. Despite the reclassification, my findings led to a valuable acknowledgment from Apple in their Hall of Fame.

Without further delay, let’s delve into the intricacies of this discovery.

Wait…. Lets have a small introduction about me:

My name is Mohaseen , I’m a cyber security enthusiast and a bug bounty hunter. I am learning about bug bounty and web application hacking from 2019 . And I love what I do.

Now let’s understand the bug.

## The BUG:-

As I embarked on my bug bounty journey, I began learning about SQL injection (SQLi) techniques. After gaining some proficiency by solving labs and studying articles, I felt ready to test my skills in a live environment.

Using Google dorks, I identified several potential targets to practice SQLi techniques. Among them, I decided to include Apple in my exploration. After conducting reconnaissance, I landed on a subdomain belonging to Apple, which I’ll refer to as redacted.apple.com.

While navigating through the subdomain, I stumbled upon a search feature. Intrigued, I decided to experiment with it. After hours of trial and error, I made a curious discovery — the search feature behaved differently when I inserted the characters ‘#’ and ‘ — ‘ into the search field. It returned additional content on the screen, signaling potential irregularities in its processing mechanism.

This behavior prompted me to suspect the presence of a blind SQLi vulnerability. Eager to test my hypothesis, I attempted to escalate the issue. However, as a newcomer to the field, my attempts were met with limited success.

## What’s the impact?

The bug, initially thought to be an SQL Injection vulnerability, turned out to be a UI issue in Apple’s search feature. While it didn’t expose data, fixing such UI bugs is crucial for user experience. Apple’s recognition of the report highlights the importance of swift bug resolution and collaboration for platform security.

## RESULT:

After an 8-month wait, I received confirmation from Apple that the report was valid, and they have added me to their Hall of Fame.

Getting HOF from apple is very great feeling. Thank you Infosec community for sharing the knowledge.

I hope you learned something new reading this. Thank you so much for reading. Have a great day😊!
