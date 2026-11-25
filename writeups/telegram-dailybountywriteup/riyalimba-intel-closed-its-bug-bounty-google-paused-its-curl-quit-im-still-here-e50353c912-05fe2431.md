# Intel Closed Its Bug Bounty. Google Paused Its. curl Quit. I’m Still Here.

- **Source URL:** https://medium.com/@riyalimba/intel-closed-its-bug-bounty-google-paused-its-curl-quit-im-still-here-e50353c91270
- **Fetched from:** https://medium.com/@riyalimba/intel-closed-its-bug-bounty-google-paused-its-curl-quit-im-still-here-e50353c91270?source=rss-7e38590ffb2f------2
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14952 (id 14952)
- **Method:** medium-rss-feed (full content:encoded) readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- **Author/Published (RSS):** Riya Limba / Sun, 18 Oct 2026 14:38:42 GMT

I read the Intel news on a Thursday and felt something I didn’t expect: not surprise.

Intel’s paid bug bounty program on Intigriti was reportedly suspended in September 2026. The program used to pay up to $100,000. Now it’s a “responsible disclosure program without bounties” .

The reason wasn’t stated by Intel. But the timing told the story. Google had paused its OSS VRP just weeks earlier, citing “a significant rise in automated submissions, the vast majority of which are not valid” . curl had ended its bounty program in January for the same reason — confirmed vulnerabilities fell from over 15% to below 5% as AI slop flooded the queue .

Intel didn’t need to explain. The pattern was already visible.

I’ve been writing about this for months. Each time a program dies, the explanation is the same: AI made it too easy to generate a convincing-looking report that contains nothing real.

A security researcher at Malwarebytes put it plainly: “The cost of filing a plausible report has fallen sharply, while the cost of proving or disproving it remains human-intensive” .

That’s the entire crisis in one sentence.

A triager at Google or Intel or curl has to read every submission carefully enough to determine whether it’s real. AI can generate a polished, technically-worded report in seconds. Human verification still takes the same amount of time it always did — sometimes longer, because the AI-generated reports are *better written* than the old low-effort spam .

The economics broke. And when the economics break, programs close.

I’ve found one confirmed bug. I’m waiting to be paid.

Reading about Intel and Google and curl, I felt something I hadn’t expected: clarity about where to spend my time.

The programs that are closing are the ones with the biggest scopes and the loudest reputations. The ones where thousands of researchers are already competing. The ones where an AI-generated fake report can slip into the queue and waste everyone’s time.

The programs that are still open are the ones I’ve been ignoring.

VDPs. Small open-source projects. Programs that don’t pay cash but offer something else: credit. A CVE. A “reported by” mention in a security advisory.

A security engineer quoted in one report said it directly: *“Many important projects pay no bounty at all. They still get reports, sometimes a lot of them, because public credit matters. A CVE, advisory credit or a ‘reported by’ mention is very meaningful for career capital”* .

I’ve been chasing bounties. I should have been chasing proof of work.

The reports that killed these programs weren’t malicious. They were careless.

A researcher runs an AI tool, gets a finding, pastes it into a report template, hits submit. They don’t verify the finding against the actual target. They don’t confirm the PoC works. They don’t ask “is this actually exploitable?” .

I understand the temptation. I’ve felt it. When you’ve been hunting for months with nothing to show, the idea of submitting *something* feels better than submitting nothing.

But “something” is what killed Intel’s program. “Something” is what made curl’s maintainer give up. “Something” is what Google cited when it paused its OSS VRP until Q1 2027 at the earliest .

The researchers who survive this shift won’t be the ones who submit the most. They’ll be the ones who submit the fewest things that turn out to be wrong.

I can’t reopen Intel’s program. I can’t force Google to accept my report. But I can change where I aim.

First, I’m looking at VDPs. Programs that don’t pay cash but offer credit. A CVE in my name is worth more than a $200 bounty that took six months to get triaged. It’s permanent. It’s searchable. It’s proof I can point to.

Second, I’m treating “verified” as a higher bar than “submitted.” Before I hit submit on anything, I run the PoC against the real target. I confirm the behavior. I make sure I can explain why it works in one sentence. If I can’t, I don’t submit.

Third, I’m remembering that the programs closing aren’t the only programs. curl still accepts reports through GitHub — just without a bounty . Google still has its Patch Rewards Program and Cloud VRP . Intel still has a disclosure program. The doors aren’t all closed. Some are just harder to see.

Intel’s bounty program is gone. Google’s OSS VRP is paused. curl stopped paying years ago. The era of “learn the basics, find an obvious bug, get paid” is ending.

But the era of “find something real, document it carefully, and build a reputation” is still here. It’s just harder. It requires more patience. It requires caring about the quality of the report as much as the payout.

I don’t have a CVE. I’ve found one confirmed bug. I’m still waiting to be paid.

But I know where the doors are now. And I know which ones are still open.

*If you’re also navigating the closure of the big programs and the search for what’s still open, I write about what I’m actually figuring out. Follow for more field notes from the bottom of the learning curve.*
