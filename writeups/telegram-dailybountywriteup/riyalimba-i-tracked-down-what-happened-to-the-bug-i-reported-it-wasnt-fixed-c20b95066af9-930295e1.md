# I Tracked Down What Happened to the Bug I Reported. It Wasn’t Fixed.

- **Source URL:** https://medium.com/@riyalimba/i-tracked-down-what-happened-to-the-bug-i-reported-it-wasnt-fixed-c20b95066af9
- **Fetched from:** https://medium.com/@riyalimba/i-tracked-down-what-happened-to-the-bug-i-reported-it-wasnt-fixed-c20b95066af9?source=rss-7e38590ffb2f------2
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14958 (id 14958)
- **Method:** medium-rss-feed (full content:encoded) readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- **Author/Published (RSS):** Riya Limba / Sat, 24 Oct 2026 14:03:13 GMT

I found my first confirmed bug four months ago.

It was a broken access control issue. Nothing dramatic — an API endpoint that returned more data than it should have. I wrote the report, included the raw requests, explained the impact in one sentence. The triager confirmed it. Paid me.

I felt good about that. I thought I had contributed something. Made a system a little safer.

Then I read HackerOne’s annual report last week and found a number I couldn’t stop thinking about.

Exposure debt rose 131% .

Not technical debt. Not financial debt. Exposure debt — the accumulated pile of vulnerabilities that organizations know about but haven’t fixed yet.

I went back and checked the status of my report. It was closed. Paid. Resolved.

But the bug? I don’t know if it was ever actually patched. The report was “resolved” from the platform’s perspective. That doesn’t mean the vulnerability was fixed.

I had to read the report twice to understand the mechanics.

HackerOne says average resolution time improved by 54% — from 135 days down to 62 days . Organizations are fixing individual bugs faster than ever.

But the backlog still grew. Because new findings are arriving faster than teams can clear them.

Nearly 70% of security leaders confirmed this: validated findings are entering their systems faster than their teams can remediate them .

A team can get better at fixing bugs and still watch the pile grow. That’s the trap. The drain is wider than it’s ever been. The faucet is running at a rate the drain was never designed for.

I’ve found one confirmed bug. I’m waiting to be paid on a second.

Reading about exposure debt, I felt something shift.

The question I’d been asking was: *How do I find more bugs?*

The better question — the one the data points to — is: What happens to the bugs I find after I submit them?

If my report enters a backlog and never gets fixed, I got paid. The triager did their job. But the vulnerability is still there. The data is still exposed. The system is still vulnerable.

I contributed to someone’s backlog. Not to their security.

The HackerOne report includes data that feels personal.

85% of surveyed researchers are actively developing AI skills. Nearly three-quarters said AI meaningfully increased the valid findings they produce .

But 68% said they’ve shifted toward more complex bugs with higher bounties .

That’s the signal. The researchers who are succeeding are going deeper, not wider. They’re using AI to cover more ground, then focusing human judgment on the bugs that require creativity and context.

A top-earning researcher put it plainly: *“AI hasn’t replaced how I think as a security researcher. It’s changed how much ground I can cover”* .

I can’t fix the remediation crisis. I can’t force organizations to patch faster. But I can change three things.

First, I’m treating “reproducible” as a higher bar than “valid.” A valid bug that takes an hour to reproduce is less useful than a valid bug with a one-line PoC. The easier I make it for a developer to fix, the more likely it actually gets fixed.

Second, I’m looking at remediation history, not just bounty size. A program that pays well but never patches is accumulating debt. A program with lower payouts but active patching is contributing to actual security. HackerOne’s CEO said it directly: pausing programs may ease volume, but it loses the work of researchers finding real issues .

Third, I’m remembering that the bottleneck isn’t me. The report says nearly 70% of security leaders confirmed that validated findings are arriving faster than teams can fix them . My job isn’t just to find bugs. It’s to make the fix as easy as possible.

HackerOne paid a record $89 million to researchers this year. That’s genuinely good news. The work is valued. Companies are still investing in finding bugs before attackers do .

But the 131% exposure debt increase tells a different story. It says the system is finding faster than it’s fixing. It says the gap is growing.

The bugs I find aren’t just entries in my report history. They’re entries in someone’s backlog. And if that backlog keeps growing, the whole system becomes unsustainable.

I don’t have a CVE. I’ve found one confirmed bug. I’m still learning.

But I know what exposure debt means now. And I don’t want to add to it.

*If you’re also learning bug bounty in a system where discovery outruns remediation, I write about what I’m actually figuring out — numbers included. Follow for more field notes from the bottom of the learning curve.*
