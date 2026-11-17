# Fewer Than 1 in 20 Reports Was Real

- **Source URL:** https://medium.com/@tl77/fewer-than-1-in-20-reports-was-real-the-arithmetic-that-closed-curls-bug-bounty-b4f10c01c036
- **Fetched from:** https://medium.com/feed/@tl77
- **Fetched:** 2026-11-17
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14986 (id 14986)
- **Method:** medium-rss-content readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
Writing a plausible bug report became nearly free. Reading one didn’t. That gap is what breaks open projects.

Fewer than 1 in 20.

That’s the share of curl’s bug-bounty reports that turned out to be real vulnerabilities once 2025 started, according to curl’s lead developer, Daniel Stenberg. Before that it was “somewhere north of 15%”, so roughly 1 in 7 or better. On February 1, 2026, the bounty was suspended.

The easy headline is “AI slop killed a bug bounty.” It’s true-ish, and it doesn’t help you much. **What actually broke was a price gap: writing a plausible report got close to free, and reading one didn’t get any cheaper.** That gap doesn’t care who or what wrote the report, and it isn’t limited to security bounties. If you review pull requests, you know it’s already in your queue.

### How a 15% Hit Rate Became Under 5%

curl is the command-line tool and library that moves data over URLs whenever your stack makes a call. It ships inside a ridiculous number of apps and devices, which is exactly why a security report against it matters to you. Someone has to read every one. That someone is a small group of maintainers.

You could track the slide in public the whole way. In May 2025, The Register reported that curl had received 24 reports in the previous 90 days, and none of them led to a payout. The top reward back then was up to $9,200 for a critical vulnerability. Submitters already had to say whether AI was used to generate the report.

In July 2025, Stenberg wrote “Death by a thousand slops.” By that year’s numbers, about 20% of submissions were AI slop, and only about 5% had turned out to be genuine vulnerabilities. He also floated the fix that would come six months later: “Dropping the monetary reward part would make it much less interesting for the general populace to do random AI queries…”

Then January 2026. In the week before the shutdown was announced, the bounty got seven submissions, and none described a vulnerability you could verify. A guest post on Bugcrowd’s blog counts 20 submissions in the first 21 days of the year, with zero real ones. Stenberg told The Register the goal of ending the program was to “remove the incentive for people to submit crap and non-well researched reports to us. AI generated or not.”

Stenberg’s own post on the end of the bounty puts the cost in human terms:

*“The never-ending slop submissions take a serious mental toll to manage and sometimes also a long time to debunk.”*

He also pointed at “lower quality even in the reports that were not obvious slop.” If you’ve ever been on review duty, you’ll recognise this one. The obviously fake stuff was only half the problem, because the whole pile got worse to read.

### The Arithmetic Nobody Puts on the Bounty Page

Every report costs a reviewer some amount of time. Call it X minutes. No public source gives you a clean per-report number, and it swings a lot between a short report and a long one. The ratio is enough to see the problem, though.

At a 15% confirmed rate, you read about 6.7 reports for every real bug you find. At 5%, you read 20. Same reviewer, same X, and the cost of finding one real vulnerability just tripled.

def triage\_minutes\_per\_real\_bug(minutes\_per\_report, confirmed\_rate):

# every report gets read; only some of them are real

return minutes\_per\_report / confirmed\_rate

triage\_minutes\_per\_real\_bug(30, 0.15)  # 200.0

triage\_minutes\_per\_real\_bug(30, 0.05) # 600.0

The 30 is a placeholder. Swap in your own number. Whatever X is, it now gets multiplied by 20.

And X didn’t hold still either. In October 2026, Stenberg wrote: “Every report is now hundreds of lines and the explanations are convoluted and detailed.” So the top of the fraction grew while the bottom shrank. That’s a rough year for a fraction.

Now flip to the submitter’s side. Producing a plausible-looking report costs close to nothing. The top prize was $9,200. The Bugcrowd guest post has the best line on this: “The hackers flooding cURL were not hacking; they were gambling.” A free lottery ticket with a four-figure prize is a great deal. The catch is that the ticket isn’t free. You pay for it from behind the counter, in hours.

According to that same guest post, the bounty paid $86,000 over six years for 78 confirmed vulnerabilities, about $1,100 per confirmed bug. For security work on software your stack uses, that’s cheap. **The expensive part was always the reading.**

*A report that’s cheap to write and expensive to disprove is a bill. The person who wrote it just isn’t the one paying.*

### It Was Never About the Tool

It’s easy to read all this as “AI bad.” curl’s own maintainer doesn’t. His line was “AI generated or not,” and the project’s policy page frames it as incentives: “A bug bounty gives people too strong incentives to find and make up ‘problems’ in bad faith that cause overload and abuse.”

AI-assisted reports have also worked for curl. In October 2025, The Register reported about 50 bugfixes merged from one researcher’s AI-assisted reports, those of Joshua Rogers. Stenberg called several of the findings “quite impressive.” A year later he was blunter: “Ignoring real vulnerabilities because they were found by AI does not make users safe and secure.”

So the tool can find real bugs when the person holding it does the checking. Rogers’s reports held up, which tells you someone checked them before hitting send. The flood skipped that step.

The Bugcrowd guest post puts it as: “AI did not kill cURL’s bug bounty; humans who refused to do the work did.” I mostly agree, with one edit. Lazy reports always existed. What changed is that a lazy report now looks like a careful one from the outside. Hackaday’s coverage names the cause: “the ease with which bogus reports can be generated by anyone who has access to an LLM chatbot.”

A bad report used to be cheap to write and cheap to spot. Now it’s cheap to write and slow to spot, because it’s long, confident and formatted like the real thing.

### Your PR Queue Has the Same Fraction

None of the sources here measure AI-written pull requests clogging review queues, so treat this section as my argument. The equation is the same one curl ran into.

Opening a PR got cheaper for anyone. Reviewing one didn’t get cheaper for you. Review is where the context lives: why that function is weird, which client still calls the old endpoint, what broke the last time someone “cleaned this up.” A machine-written PR can look finished, with tests, a tidy description and a confident summary. None of that tells you whether it’s right, which is the one thing you’re there to check.

Postgres shows the other half of the bill. Robert Haas, a Postgres committer, wrote on Neon’s blog that Postgres 19 is late because “LLMs happened.” Far more bugs are being found, and fixing them takes time. He counts 1,037 commits to master between April 8 and September 25, 2025, against 1,443 in the same window in 2026. That’s about 39% more.

Back-patched commits to the in-progress release were up more than 60%, while commits that weren’t back-patched actually fell slightly. So the extra work is bug fixing, and feature work didn’t grow at all. Three features were reverted between August 27 and September 15. Haas also notes that LLM-drafted fixes “aren’t always correct or compliant with PostgreSQL standards,” so even the fixes need careful review.

**curl drowned in reports that weren’t real, Postgres is drowning in reports that are, and both run out of the same thing: reviewer time.**

*Generation scales with compute. Review scales with people who understand the code, and you can’t spin up more of those on demand.*

### Make the Ticket Cost Something Again

If the problem is that reports got cheaper to write than to read, the fix is to move some of the cost back to the writer. Every option here costs you something, so pick the one you can live with.

curl’s move was the bluntest: take away the prize. No payout, no lottery, much less reason for anyone to spray your repo with reports. The tradeoff is real, because the money also rewarded the careful researchers who did the work. You lose some good reports along with the junk. For a project run by a small group of maintainers, that’s probably the right call. For a large company with a paid triage team, probably not.

The gentler move is to ask for the expensive part up front. Make a reproducer, an exact version and a failing test the price of entry. For someone who found a real bug, that’s work they were going to do either way. For someone pasting chatbot output, it’s the whole job. The cost lands on new contributors with real bugs who don’t know how to write a minimal repro yet, so give them a template that teaches them, and be patient.

A disclosure checkbox on the form doesn’t do much. curl had one by May 2025, and the 2025 confirmed rate still fell below 5%. A checkbox is cheap to tick, which makes it the same kind of ticket as the report.

The last move costs you nothing but nerve: time-box the first read. If a report or PR doesn’t show the problem in the first few minutes, ask for a repro and move on. It feels rude. It’s less rude than letting the queue burn out the people keeping the project alive.

The tradeoff underneath all of this is open contribution against review time. I’d protect the reviewers and make the first step a little harder. Open source runs on people reading things carefully, and that’s the one resource nobody can generate.

Fewer than 1 in 20 was real. The other 19 still had to be read by someone with better things to fix. Next time you open a PR, write it for that person.

### 🧾 Other Bills Someone Else Pays

Somebody always pays for the shortcut. These are the receipts.

- 🐛 [Your AI Wrote the Code. The Bugs Are Still Yours.](https://medium.com/@tl77/the-70-problem-when-ai-code-isnt-production-ready-e5e88c09fdc9) — what happens after the plausible PR gets merged.
- 🛠️ [Cursor vs Copilot vs Claude vs Antigravity (and a Couple More): What I Actually Use](https://medium.com/@tl77/cursor-vs-copilot-vs-claude-vs-antigravity-and-a-couple-more-what-i-actually-use-d90a4eef23bb) — the tools on the cheap side of the equation.
- 🗄️ [Why Postgres Is Enough for 90% of Apps](https://medium.com/@tl77/why-postgres-is-enough-for-90-of-apps-06da873aecdb) — still true, even while its next release waits on reviewers.
