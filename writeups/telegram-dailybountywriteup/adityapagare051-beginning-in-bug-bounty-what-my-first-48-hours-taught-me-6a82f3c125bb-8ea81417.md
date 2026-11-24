# Beginning in Bug Bounty

- **Source URL:** https://medium.com/@adityapagare051/beginning-in-bug-bounty-what-my-first-48-hours-taught-me-6a82f3c125bb
- **Fetched from:** https://medium.com/feed/@adityapagare051
- **Fetched:** 2026-11-24
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14997 (id 14997)
- **Method:** medium-rss-content readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
Everyone who starts bug bounty has the same dream: find a bug, submit it, and watch the bounty arrive. I had that dream too.

In the past two days, I found my first four vulnerabilities and reported them on Bugcrowd. I spent around 12 to 15 hours on a single program, testing, reading responses, and writing reports. When the results came in, this is what happened:

- **2 reports were marked duplicate.** Another researcher had already found them.
- **1 report was closed as not applicable.**
- **1 report was accepted, but as P5 (Informational).**

No bounty. No payout. Not what I imagined.

#### The moment I found them

When I found my first vulnerability, I was thrilled. I even asked an AI assistant how much these bugs might pay, and it gave me a range of roughly $1,000 to $1,500. I got even more excited, and that’s the mistake many beginners make, so here’s the lesson: **never count the money before triage.** Payout depends on severity, impact, scope, and above all whether you were first. No estimate, from AI or from people, can promise any of that.

#### Why I wasn’t sad

When the reviews came in, I expected to feel disappointed. I didn’t. Here is why.

**1. Duplicate means valid.** A duplicate means someone else found the same issue, and the triager agreed it was real. As a beginner, finding a bug that experienced researchers also found is a sign my methodology is moving in the right direction.

**2. Informational is still a finding.** A P5 isn’t a reward, but it means I found something real and communicated it well enough for the team to review it.

**3. A “not applicable” teaches more than a payout.** Every rejection shows me where my understanding of impact is off. Understanding why a report was rejected is one of the fastest ways to learn what a program considers a real risk.

**4. I learned the full workflow.** In 48 hours I practiced recon, testing, writing clear reports, reading triage responses, and handling the emotions around all of it. That’s the real work of bug hunting.

#### What I’m taking forward

- **Speed matters.** Popular programs have many researchers, so common issues get found fast. I need to go deeper, not only faster.
- **Impact matters more than existence.** Missing headers or low-risk misconfigurations often end up informational. I want to focus on logic flaws, access control, and chains that show real impact.
- **Write better reports.** Clear steps, clear impact, clear proof.
- **Check for duplicates logic early.** Look at disclosed reports and scope notes before investing hours.
- **Stay consistent.** One accepted report, even a P5, is proof that I can do this.

#### To other beginners

If you’re just starting out, expect duplicates. Expect “informational.” Expect rejections. They don’t mean you’re not good enough. They mean you’re in the game.

Most people never submit a single report. They stay stuck in tutorials, waiting to feel ready. If you’ve submitted even one valid report, you’ve already done something many never do.

This is not the end of a story. It’s the start of my practical bug bounty journey, and I’ll keep researching, improving, and submitting, even if some of them turn out to be duplicates.

*If you’re also starting out, I’d love to hear about your first report. What happened with it? Share in the comments.*
