# How I Discovered One of My Most Creative Bugs in Google’s Gemini AI Competition

- **Source URL:** https://medium.com/@momenrezkk90/how-i-discovered-one-of-my-most-creative-bugs-in-googles-gemini-ai-competition-1e0315b6fef0
- **Fetched from:** https://medium.com/@momenrezkk90/how-i-discovered-one-of-my-most-creative-bugs-in-googles-gemini-ai-competition-1e0315b6fef0?source=rss-ec3307f5f95a------2
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14896 (id 14896)
- **Method:** medium-rss-feed (full content:encoded) readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- **Author/Published (RSS):** MOAMEN REZK / Wed, 02 Sep 2026 21:55:38 GMT

*Sometimes, a vulnerability starts with nothing more than a simple question: “Why is this happening?”*

When Google launched its Gemini AI competition, teams were invited to build projects using the Gemini API and compete through community voting.

The concept was simple:

Build a project.

Submit it.

Get votes.

Win.

I joined one of the teams — not as a developer, but as the person responsible for security testing.

The plan was to perform a proper penetration test once the project was complete.

There was just one problem.

By the time the team submitted the final build, **there was only one day left before the competition deadline**.

There was no time for a full security assessment.

So I stepped back and focused on learning instead.

At the time, I was exploring topics such as **Host Header attacks, browser behavior, User-Agent manipulation, and creative exploitation techniques**.

I had no idea that what I was learning would become useful only a few days later.

Once voting opened, our team WhatsApp group became surprisingly competitive.

Friends, classmates, and family members were voting for our project, and everyone was watching the numbers.

Then one teammate sent a screenshot.

*“Look! My friend voted twice — once from Chrome and once from Firefox!”*

That immediately caught my attention.

Why would using two different browsers allow the same person to vote more than once?

It was a small observation, but it raised a bigger question:

**How was the voting system identifying a voter?**

At that moment, I started thinking about the things I had been studying.

Could the system be identifying users based on their browser?

Could the User-Agent be involved?

Could changing browser characteristics allow someone to vote repeatedly?

I had a hypothesis.

Now I needed to test it.

My initial theory was straightforward.

If the voting system relied on browser characteristics rather than a stronger server-side identity mechanism, perhaps changing the User-Agent could make the application treat each request as coming from a different browser.

Something like:

Chrome → 1 vote

Firefox → 1 vote

Safari → 1 vote

Opera → 1 vote

And if that worked, automating different User-Agent values could potentially allow a single user to generate many votes.

So I opened Burp Suite.

My plan was simple:

Then I clicked **Vote**.

Nothing.

No request appeared in Burp.

I tried again.

Still nothing.

I refreshed the page. I restarted the browser. I tested again.

At first, I thought I was missing something.

But then I noticed something even more interesting.

It wasn’t the lack of traffic that caught my attention.

It was the **speed**.

When I clicked the Vote button, the interface responded almost instantly.

There was no noticeable network delay.

No loading.

No waiting for a server response.

Just an immediate change in the interface.

That made me rethink my original hypothesis.

Maybe the vote wasn’t being processed through the network at all.

So I started inspecting the client-side behavior.

And eventually, I found it.

The voting state was being stored in the browser’s **localStorage**.

That changed everything.

Instead of trying to manipulate an HTTP request, I was looking at a client-side mechanism controlling the voting state.

During my testing, I found that modifying the client-side voting data allowed me to reproduce additional votes.

In other words, the system’s client-side state could be manipulated to bypass the intended voting restriction.

The important security lesson here wasn’t simply that localStorage existed.

The problem was **trusting client-controlled data for something that should enforce a server-side security boundary**.

A user can control their own browser.

That means a value stored entirely in client-side storage should never be treated as trustworthy proof that an action is legitimate.

In this case, modifying the relevant localStorage data was enough for me to reproduce repeated voting behavior.

I tested the behavior in two ways.

First, I inspected the application’s localStorage through the browser’s developer tools and identified the value associated with the voting state.

By modifying that client-side data and interacting with the application again, I was able to reproduce additional votes.

I then automated the same concept with a small JavaScript-based approach:

The important result was that the restriction could be bypassed repeatedly from the client side.

What was supposed to represent a single user’s vote could be manipulated locally.

From a purely technical perspective, the interesting part wasn’t the localStorage API itself.

The interesting part was the **security assumption behind it**.

The application was relying on information controlled by the client to enforce a rule that should have been enforced by the server.

That’s a fundamental security principle:

***Never trust the client to enforce a security boundary.***

A user can modify JavaScript.

A user can modify browser storage.

A user can modify requests.

A security control that depends entirely on the client can therefore be bypassed by that same client.

After confirming the behavior, I reported the issue to Google through the appropriate security channel.

Google later informed me that the report was a **duplicate of an existing issue**.

Obviously, that meant there would be no reward or unique credit for the report.

But honestly, I wasn’t disappointed.

This was the first Google security issue I had discovered through my own investigation, and the process itself was what mattered most to me.

The vulnerability started with something incredibly simple:

A teammate noticed that someone had voted twice.

I asked why.

Then I formed a hypothesis.

The hypothesis turned out to be wrong.

That failure led me to investigate the application more deeply.

And that investigation led me to the actual issue.

This experience taught me something that no checklist could have taught me.

Security research isn’t always about finding the obvious vulnerability.

Sometimes it’s about noticing something that doesn’t make sense.

A browser behaving differently.

A request that never appears.

A response that happens too quickly.

A tiny inconsistency that everyone else ignores.

Those details can be the beginning of an investigation.

For me, this wasn’t about discovering an XSS or finding a simple misconfiguration.

It was about following a chain of reasoning:

**Observation → Hypothesis → Failed Assumption → Investigation → Discovery**

That process is what made this finding memorable.

The report was a duplicate.

But the experience was still one of my favorite security discoveries.

Not because it earned a reward.

Not because it was a unique vulnerability.

But because it started with a random message in a WhatsApp group and turned into a real security investigation.

It reminded me that developing a **hacker mindset** isn’t necessarily about knowing every technique.

Sometimes, it’s simply about being curious enough to ask:

***“Why is this happening?”***

And then being stubborn enough to keep looking until you find the answer.

That is the lesson I took from this experience.

**Real hacking starts with noticing what others ignore.**

And sometimes, all it takes is one small spark.
