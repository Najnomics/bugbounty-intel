# How I Stumbled Into an SQLi at 2 AM (Instead of Doing My Job)

- **Source URL:** https://medium.com/@ramshath1999/how-i-stumbled-into-an-sqli-at-2-am-instead-of-doing-my-job-4506135dea3a?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250501130106/https://medium.com/@ramshath1999/how-i-stumbled-into-an-sqli-at-2-am-instead-of-doing-my-job-4506135dea3a
- **Fetched:** 2026-11-19
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/9297 (id 9297)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# How I Stumbled Into an SQLi at 2 AM (Instead of Doing My Job)

# Or: Why Cybersecurity Training Institutes Should Practice What They Preach

# 1. The Setup: A Pentester, a Network Scan & the Sleep-Deprived Brain of Doom™

**Time:** 2:37 AM

**Location:** My dimly lit home office, lit only by screens and poor life choices

**Mood:** One espresso away from thinking I’m Batman

I was deep into a routine network pentest — tools running, logs flying, and Nessus doing its usual *“I’ll be done when I’m done, bro”* routine.

That’s when my brain whispered:

*“Hey… why not multitask and do something mildly reckless?”*


And like every great story that starts with *“I probably shouldn’t, but…”* — I listened.

# 2. The Rabbit Hole: “Just a Little Google, What Could Go Wrong?”

I typed *“top cybersecurity training institutes in Kerala”* into Google, purely out of boredom.

(Also maybe to judge their web security — let’s be honest.)

A few clicks later, I landed on a website that looked polished, professional, and just *a little too confident*.

Then I saw it.

A juicy little GET parameter in the URL.

`https://example[.]com/page?id=42`
At 2 AM, this isn’t just a URL — it’s a **challenge**.

That `id=` whispered to me like a shady stranger in a hoodie:

*“Psst… Try a single quote. You know you want to.”*


# 3. The Discovery: One Quote to Rule Them All

I did what any curious, definitely-overcaffeinated pentester would do:

I added a `'` at the end.

Boom.

`ERROR 1064: You have an error in your SQL syntax...`
I tried `''` next. The error *vanished*. Suspiciously quiet.

At this point, the website wasn’t just vulnerable — it was **practically flirting**.

# 4. The Confirmation: Burp Suite Joins the Party

No late-night hacking adventure is complete without summoning the mighty **Burp Suite**.

So I fired it up, intercepted the request, and started poking it like it owed me money.

A few payloads later — BOOM:

**Boolean-based blind SQLi confirmed.**

The website started answering logic questions like a confused oracle:

- Me: *“Is 1=1?”*
- Site: *“Yup!”*
- Me: *“Is 1=2?”*
- Site: *“Nope.”*

Then came SQLMap. I barely typed the command before it responded like:

```
[INFO] the back-end DBMS is MySQL  
[INFO] fetching database names...
```
It was like the website had been *waiting* to confess its secrets. Therapy session unlocked.

# 5. The Irony: Cybersecurity Institute, Meet SQL Injection

Let me set the scene again:

- **Target:** A popular cybersecurity training institute
- **Vulnerability:** SQL Injection so basic it probably came free with the domain
- **Time to exploit:** Under 10 minutes
- **Effort required:** Less than making instant noodles

And the worst part?

I wasn’t even trying to hack them. I was just trying to stay awake.

Imagine if someone malicious had found this.

(Or worse — an intern.)

# 6. The Responsible (and Slightly Smug) Ending

Let me be clear:

✅ I stopped immediately

✅ I reported the issue responsibly

✅ I didn’t go any deeper

✅ I resisted the temptation to rename their tables to “pls\_secure\_me”

But man… the irony hit hard.

A place that *teaches* people to find SQLi had one *just sitting out in the open like a forgotten cookie*.

# Moral of the Story?

- Don’t leave a bored pentester alone at 2 AM
- If you run a cybersecurity institute, maybe audit your site before selling “Certified Hacker Ninja Guru” courses
- SQLi is like glitter — still everywhere, and somehow still getting into places it shouldn’t
- Sanitize your inputs. Seriously. This isn’t 2005

# Final Thoughts

This isn’t a flex. It’s a **facepalm moment**.

The fact that I could walk into an SQLi without even trying says a lot about the state of web security — and yes, even the state of education around it.

If you teach people to secure applications, your website shouldn’t be coughing up database names like a magician doing card tricks.

# Bonus Section: Ideas I Almost Followed at 3 AM

- Make a fake login page that just says *“Welcome to SQL 101 — You Already Passed!”*
- Rename all their tables to “unprotected\_db\_baby”
- Leave a SQL comment: `-- This site was tested by a sleepy dude at 2:47AM`

(But again — responsibility > mischief. Barely.)
