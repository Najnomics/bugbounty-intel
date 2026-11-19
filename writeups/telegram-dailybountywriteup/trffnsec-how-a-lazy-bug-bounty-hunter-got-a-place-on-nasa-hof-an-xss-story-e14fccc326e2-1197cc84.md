# How a Lazy Bug Bounty Hunter got a place on NASA HOF ( An XSS Story).

- **Source URL:** https://medium.com/@trffnsec/how-a-lazy-bug-bounty-hunter-got-a-place-on-nasa-hof-an-xss-story-e14fccc326e2?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20241122031811/https://medium.com/@trffnsec/how-a-lazy-bug-bounty-hunter-got-a-place-on-nasa-hof-an-xss-story-e14fccc326e2
- **Fetched:** 2026-11-19
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/7029 (id 7029)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
Hey Amazing Hackers, This is **TrffnSec**

Nasa’s In-Scope Wildcards —

Let’s dive in…

I rolled out of bed around 1 pm, lazily lingering for another 30 minutes before finally grabbing my laptop. The day before, I had collected a bunch of NASA’s subdomains using Subfinder — because why not, right?

With nothing better to do, I thought, “Let’s take a peek at those subdomains.” So, I ran:

`cat nasa-subs.txt | https-toolkit -sc`

Boom! I had all the status codes at my fingertips. Slowly, I started testing each subdomain, one by one, until I stumbled upon a particularly intriguing one (let’s call it **abcd.nasa.gov**).

There it was — a search bar, just sitting there, tempting me. The first vulnerability that popped into my mind? You guessed it — XSS. I typed in **abcd**, and voilà, it reflected on the page.

Time to get a little creative. I tried **abcd\<h1>abcd\</h1>** — the HTML reflected too. Even the **\<img>** tag worked. But **\<script>alert()\</script>**? No luck.

Alright, time to dig deeper. I fired up [**xsstrike**](https://github.com/s0md3v/XSStrike) to hunt for that elusive XSS. The result? Over 500+ false positives. Sifting through each one? No thanks.

So, I took to Twitter for a little collaboration. Sent out a tweet,

but… crickets.

No one responded.

I thought to Report that HTML Injection.

And P5’s , they wont accept. 🤐

Then, out of nowhere, the creator of the tool, [Ibrahim](https://x.com/ibrahimxss_), messaged me directly.

He suggested buying the tool for full access. I waited a bit longer, and guess what? He started offering trial usage of the tool, promoting through twitter.

You bet I grabbed it. Time to see what this tool could do…

With IbrahimXSS ready to roll, I needed some serious firepower.

So, I grabbed XSS payloads from every corner of the web — Twitter ( [LostSec](https://x.com/coffinxp7) ), GitHub, Telegram, PortSwigger, HackerOne reports — you name it. I combined them all into one main file.

After skimming through the tool’s manual, I realized it could inject payloads into parameters.. and thats how a tool works.

But It should be with 0 False Positives.

That’s why i’m Choosing [IbrahimXSS](https://x.com/ibrahimxss_). I noticed one more Usage: I could inject payloads directly by tagging `{payload}` in the requests, This one is so useful to POST Requests.

So, I saved the target URL to a file named `url.txt`:

[https://abcd.nasa.gov/?searchgov=abcd{payload}&submit=abcd](https://abcd.nasa.gov/?searchgov=abcd%7Bpayload%7D&submit=abcd){payload}

Without The ‘{payload}\` , The Tool will work on all the parameters.

With everything set, I unleashed the [IbrahimXSS tool](https://x.com/ibrahimxss_). It started churning through my massive 30k lines XSS payloads file. After some time…

**BOOM**. It was done.

The output file revealed five successful XSS hits. I opened them, and there it was — a shiny, exploitable XSS vulnerability on a NASA subdomain.

Feeling pumped, I reported the bug. But then, NASA hit me with a curveball — they marked it as “informative” and a duplicate of my previous HTML injection report.

I asked them to Re-Verify it.

They Accepted my Report.

And thats how I got Placed in NASA’s HOF

Thanks for joining me on this bug-hunting journey! Your support rocks. Let’s keep squashing bugs together! 🐜🛠️

Next Coming WriteUp is Apple’s HOF

Follow for more
