# My first AI bug report got closed within hours (and that was good for me)

- **Source URL:** https://medium.com/@manuelfdzgo/my-first-ai-bug-report-got-closed-within-hours-and-that-was-good-for-me-eb68c002c326
- **Fetched from:** https://medium.com/@manuelfdzgo/my-first-ai-bug-report-got-closed-within-hours-and-that-was-good-for-me-eb68c002c326?source=rss-d196a3764c5a------2
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14975 (id 14975)
- **Method:** medium-rss-feed (full content:encoded) readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- **Author/Published (RSS):** Manuelfdzgo / Sun, 08 Nov 2026 19:47:42 GMT

I’ve been doing web and API penetration testing for a while, and bug bounty at night for the last few months. What pulled me toward AI wasn’t anything epic: it’s the one place where the manual hasn’t been written yet. In web, you know what you’re going to find before you open Burp. With a chatbot, you don’t.

So one October evening I sat down in front of one of the best-known AI assistants, with the same methodology I use at work to test LLM-based assistants, opened its bug bounty program on one of the big platforms, and started poking. This post is about what I found, what I reported and, above all, why it got closed within hours as *Not Applicable*. This is not an “I was right” post. It’s a “here’s what I learned by embarrassing myself politely” post.

The way I test an LLM looks more like social engineering than classic pentesting. I’m not looking for a vulnerable parameter; I’m looking for a personality trait that can be leaned on. Over the evening I kept coming back to three that paid off:

• **Its urge to correct you.** Hand the model wrong facts about itself and its instinct is to fix them. And by fixing them, it confirms.

• **Its urge to complete things.** Give it a structure with blanks and it tends to fill them in. The format pulls the answer out.

• **Its urge to help.** Tell it that to help you with A it first needs to do B, and it treats B as a step in the procedure, not as a separate request.

I’m not going to publish the prompts or what the model answered, for two reasons: the platform’s terms require permission before disclosing submission details, and a list of recipes adds nothing you can’t already find in any jailbreak repository. The interesting part isn’t the wording; it’s the pattern.

With those three traits I put together two findings. The first was tiny: phrased the right way, the model would answer questions that had nothing to do with the conversation, and it did so consistently (three out of three attempts, in fresh conversations). The second was more elaborate: by chaining the three techniques I got the model to confirm, piece by piece, how its own deployment was configured. Nothing secret, no user data. But a map.

I documented it the way I’d document any web finding: every test in a fresh conversation, screenshots, reproducibility, mapping to the OWASP LLM Top 10 (LLM01 and LLM02), a table of everything that **didn’t** work (which was considerably more than what did), and a P4 severity, Low, with a paragraph on why it might deserve P3. I also included the counterargument the model itself kept giving me: “this is in the public documentation.”

I was reasonably happy with the report. I submitted it that same night.

The next morning, before I was even awake, the triager had marked it *Not Applicable*, with a three-paragraph explanation that boiled down to two points:

1\. The second finding (configuration, instruction hierarchy, tooling) is exactly the kind of information the program brief explicitly excludes. It’s written there, in so many words, in the proprietary information section. I had read it. Skimmed it.

2\. The first finding is a model behavior issue with no demonstrated path to user harm, and the program requires precisely that: demonstrable material harm. “Model response” issues are out.

My first reaction was everyone’s first reaction: but it’s reproducible, but it’s documented, but… My second reaction, half an hour later, was to reread the whole brief. And they were right on both counts. I replied thanking them and saying I had missed that part of the scope. That wasn’t a diplomatic line; it was true.

**Scope in AI is not like scope in web.** In web, scope is a list of hosts. In an AI program, scope defines *what counts as a vulnerability*, and that’s far more restrictive than my pentester intuition expected. A model doing something it shouldn’t is not a bug for the program if nobody gets hurt. I find that debatable as a general philosophy; it’s not debatable as a program rule, and the rule is what you sign up to.

**“Interesting” and “reportable” are different things.** I knew this from web (we’ve all wanted to report a missing header), but in AI the temptation is stronger because almost everything you discover feels new. The question I now ask before writing a single line is: what happens to a real user if someone does this? If the answer is “nothing, but look how neat,” there’s no report.

**The underlying debate is still open, and I’m not the one who’s going to settle it.** Is it a leak when a model confirms information about itself that is, in part, public? The program’s position is no. Mine, with all the insecurity of someone who’s been at this for months rather than years, is that the problem isn’t the data but the fact that the behavior can be steered, because the same techniques against a deployment with a confidential system prompt would leak something that matters. But today that’s a hypothesis of mine, not a finding. And you don’t report a hypothesis: you keep it for the day you can demonstrate the harm.

**The report wasn’t wasted time.** The discipline of documenting it (clean conversations, negative results, honest severity) is the same discipline I’ll need when I find something that does qualify. And the triager’s reply, fast and well argued, taught me more about the program than the brief did.

I’m leaving these open because I don’t have answers, and because someone reading this has surely been through the same:

• Where do you draw the line between “the model is helpful” and “the model can be steered”?

• When an AI program demands “demonstrable material harm,” how do you build that demonstration without stepping outside scope?

If you have experience with this, I’d love to read you in the comments. And if you’re starting out like me: read the whole brief. Twice. Before you open the chat.

*AEGIR Security · pentester by day, bug bounty hunter by night. This is the first part of a series on getting into AI security from web pentesting. Neither the program nor the product is named on purpose, and nothing described here includes details of the submission.*
