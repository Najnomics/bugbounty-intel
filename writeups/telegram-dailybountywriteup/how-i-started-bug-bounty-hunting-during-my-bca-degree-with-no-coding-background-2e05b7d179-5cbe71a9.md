# How I Started Bug Bounty Hunting During My BCA Degree (With No Coding Background)

- **Source URL:** https://sukhveersingh97997.medium.com/how-i-started-bug-bounty-hunting-during-my-bca-degree-with-no-coding-background-2e05b7d179f4
- **Fetched from:** https://sukhveersingh97997.medium.com/how-i-started-bug-bounty-hunting-during-my-bca-degree-with-no-coding-background-2e05b7d179f4?source=rss-8b2cfce9f882------2
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14927 (id 14927)
- **Method:** medium-rss-feed (full content:encoded) readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- **Author/Published (RSS):** Sukhveer Singh / Tue, 29 Sep 2026 05:04:47 GMT

Let me set the record straight before we begin.

I did not earn lakhs during college. I did not find a critical bug on Facebook in my first month. I did not get a job offer from Google because of my HackerOne profile.

What actually happened was far less glamorous — and far more useful to you.

I was a BCA student with average marks, a slow laptop, and no idea what I wanted to do after graduation. I started bug bounty hunting because I was curious. I kept going because it was the first thing in my degree that felt real. And by the time I graduated, I had learned more about web security than any classroom ever taught me.

This is that story — the honest version.

For educational purposes only. Only test systems you own or have permission to test.

I was in my second year of BCA when I first heard the term “bug bounty.” A senior mentioned it casually in the corridor — something about “companies paying you to hack them.” I nodded like I understood and then went straight to YouTube that night.

What I found confused me more than it inspired me. People were talking about Burp Suite, recon, subdomains, XSS, IDOR — words I had never heard in any lecture. I remember closing my laptop thinking, *“This is for people way smarter than me.”*

That feeling lasted about two weeks. Then it turned into irritation. I was tired of not understanding things.

So I started small. Not with a bug bounty program — with the basics.

My first real attempt at bug bounty was a disaster.

I picked a program on a public platform because it had the biggest payout listed. I opened the target, clicked around for two hours, ran a scanner I didn’t understand, found nothing, and closed the tab.

I repeated this for almost a month with different programs. Every session ended the same way — exhausted, confused, and quietly convinced I wasn’t cut out for this.

The problem wasn’t the target. The problem was me.

I was trying to hunt before I understood what I was hunting *for*.

If I could go back and restart my BCA years, here’s exactly what I’d do in the first month — nothing more:

1\. Learn how the web actually works.

Not theory. Just open DevTools on any website and stare at the Network tab. Watch what a login does. Watch what a search query sends. That single habit taught me more than three semesters of lectures.

2\. Understand HTTP requests and responses.

Methods, status codes, headers, cookies. Once I understood that a web app is just a conversation between a browser and a server, everything else started making sense.

3\. Pick ONE vulnerability and go deep.

For me, it was IDOR. I read about it for a week, watched every video I could find, and then opened a practice lab and tested it myself until it clicked.

4\. Use free tools only.

Burp Suite Community Edition. Browser DevTools. That’s it. I didn’t need a paid setup — I needed to understand the tools I already had.

5\. Practice on legal labs.

PortSwigger Web Security Academy and TryHackMe. Not real targets. Labs. Because the goal in month one isn’t to find a bug — it’s to learn how a bug feels when you find it.

I skipped all five of these. That’s why my first month was wasted. Don’t repeat that.

I want to be precise here, because this is where most stories get exaggerated.

The first bug I found was not a critical. It was not a big payout. It was a low-severity issue on a small program with a small scope — the kind most hunters skip.

It was an access control flaw. A parameter that should have been locked down wasn’t. Another user’s data was visible when it shouldn’t have been. Nothing dramatic. Nothing that made headlines.

But when I submitted it and saw the status change to “Triaged” — that was the moment bug bounty stopped being a fantasy and became a skill.

Not because of money. Because I finally had proof that the process worked.

That one small bug taught me more than the previous six months of watching tutorials. It taught me that bug bounty rewards patience and process, not cleverness.

Here’s the part nobody talks about: college doesn’t pause for your side interests.

I had classes, assignments, internal exams, practicals, and the constant pressure of “what will you do after BCA.” Bug bounty had to fit into the gaps.

My honest schedule during those months:

I wasn’t consistent every day. Some weeks I did nothing. But I never fully stopped — and that’s the only reason I improved.

If you’re a student reading this, don’t try to hunt five hours a day. You’ll burn out in two weeks. One focused hour, most days, for a year, will beat three months of obsessive effort every time.

You don’t need to be a great coder.

I was average at programming. What mattered was understanding how web apps behave, not writing perfect code.

Duplicates are not failure.

Every duplicate means you found a real bug — someone just found it first. That’s progress, not rejection.

Reading writeups is not cheating.

I learned more from other people’s reports than from any course. Read them constantly.

Small programs are better for beginners.

Big companies have thousands of hunters. Smaller programs have fewer eyes — and triagers who actually reply.

Boring bugs pay.

IDOR. Access control. Misconfigurations. Not flashy, but they’re everywhere and they get accepted.

Consistency beats intensity.

One hour a day, most days, for a year. That’s the whole secret. There isn’t a bigger one.

You have an advantage most people don’t: time.

You don’t need to rush. You don’t need to prove anything to anyone. Start with fundamentals. Practice on labs. Pick one vulnerability and understand it properly. Then hunt small, hunt patiently, and write clear reports.

Your first valid bug might take weeks. It might take months. That’s normal — and it’s fine.

What matters is that you build the habit now, while you have the freedom to be bad at it. Because that’s how everyone starts.

Bug bounty didn’t make me rich during BCA. It made me *capable* — and that turned out to be worth far more.

If you’re a student sitting in a classroom right now, wondering whether you’re “smart enough” for this field, hear this clearly: you are. You just haven’t started properly yet.

Start small. Start today. Stay honest about your progress.

*Hack to learn. Don’t learn to hack. 🛡️ — Sukhveer Singh*
