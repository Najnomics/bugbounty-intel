# VoidRecon

- **Source URL:** https://cyphernova1337.medium.com/voidrecon-recon-the-way-an-attacker-actually-does-it-bbbac1dd91e4
- **Fetched from:** https://cyphernova1337.medium.com/voidrecon-recon-the-way-an-attacker-actually-does-it-bbbac1dd91e4?source=rss-6f03dce4675e------2
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14907 (id 14907)
- **Method:** medium-rss-feed (full content:encoded) readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- **Author/Published (RSS):** CypherNova1337 / Thu, 10 Sep 2026 23:19:26 GMT

How I built a 50-module reconnaissance engine, and what a dozen real engagements taught me about the difference between a lot of output and output you can trust.

Every recon tutorial teaches the same pipeline. subfinder piped to httpx piped to nuclei, a wordlist, a screenshot tool, and a prayer. It works. It also produces exactly what everyone else produces, on exactly the surface everyone else has already picked over.

Real attackers don’t work off a checklist. They start with the organization, not the domain. They exhaust everything they can learn without touching the target before they send a single packet. And they go straight for the forgotten corners — the staging box nobody decommissioned, the S3 bucket named after an internal project, the OAuth flow that quietly leaks a client ID and three trusted redirect hosts.

I wanted a tool that worked that way. So I built VoidRecon.

It’s an adversary-minded reconnaissance engine: 50 modules across 7 phases, one command, a scope conscience, and a built-in analyst that reasons about your targets without an API key. Passive by default. Loud only when you tell it to be. Authorized use only, always.

This is what it does, why it’s different, and — the part I’m actually proud of — how it got hardened on real bug bounty programs until it stopped embarrassing itself.

One command, the whole surface

voidrecon wizard

OR

voidrecon run target.com - profile deep

Under the hood, VoidRecon runs as ordered phases, each enriching one shared, de-duplicated datastore:

A dead source never aborts the run. One rate-limited API doesn’t cost you the engagement.

Here’s the thing about recon output: a thousand assets is useless if you don’t know which three to look at first. Most tools hand you the thousand.

VoidRecon’s Analyst is the built-in brain — and it works with no API key and no rate limits, because the intelligence is in the tool, not in a monthly LLM bill. If you do have a model key, it gets seeded with the Analyst’s reasoning and sharpens it. Optional. Additive.

It doesn’t reason over a flat list of tags. It reasons per host, fusing what a host is (name tokens, HTTP posture, tech) with what was actually found on it, and it recognizes attack chains that only exist when several signals co-occur on the same host:

Attack plan — highest-value plays:

A secret on one host and a login gate on another won’t invent a play. That co-occurrence discipline is the whole point — it’s the difference between a tool that lists things and one that reasons about them. Every promising host gets a dossier: what it is, why it matters, and the exact next move.

Two design choices matter more than any single module.

First: when a source returns nothing, VoidRecon tells you why. A rate limit, a block, a timeout, and a genuinely empty result used to look identical. Now every run ends with a coverage panel:

Recon coverage:

otx: nothing found is a real empty. hackertarget: RATE-LIMITED is a gap you can close. You should never have to guess which.

Second: findings stay inside your scope. If the crawler follows an OAuth redirect onto accounts.google.com, VoidRecon does not report Google’s discovery document as your target’s exposed spec. Findings are confined to the scope domain set; the where to test pointer always aims at the in-scope asset’s own surface. A report you hand a client should never attribute a third party’s asset to them — that’s the fastest way to lose their trust.

Recon is a means to an end, and the end is usually another tool. VoidRecon writes per-class candidate files — sqli.txt, xss.txt, redirect.txt, and so on — deduplicated by injection point, not by URL. Fifty copies of /flows?id=1 through /flows?id=50 collapse to one target: the id parameter on /flows. Each line keeps a real value so nothing chokes:

cat runs/target.com-/candidates/xss.txt | dalfox pipe

sqlmap -m runs/target.com-/candidates/sqli.txt --batch

No copy-paste. No manual dedup. No massive errors when you pipe it into your XSS tool.

Anyone can ship a feature list. What I care about is whether the output holds up when someone who knows what they’re doing reads it critically. So I ran VoidRecon on real authorized programs and had the results torn apart. A few of the lessons:

On a large exchange target, origin-IP discovery ran for three days. It was testing every WAF-fronted host against every discovered IP, and each dead IP burned the full timeout. The fix wasn’t just to bound that module — it was to give every module a wall-clock budget, so no single stage can ever hang a run again.

A data company’s marketing pages tripped the SQLi detector — because the pages literally contain the words “PostgreSQL” and “Oracle error” as product copy. Error-based detection is now differential: the database error has to appear only after the injected quote, never in the baseline.

Next.js static data files got flagged as SQLi. There’s no database behind a static file; the byte-count differences were just single-page-app rehydration noise. Static-asset paths are no longer injection-probed, and boolean detection now requires a reproducible differential.

Possible secrets in JavaScript was eight-for-eight false positives — every one a your\_api\_key placeholder. Secret detection now blocks placeholders, entropy-scores the value, and only escalates a structurally valid vendor token to HIGH. Everything else is an INFO candidate that never poisons an attack plan.

Each of those was the kind of thing that’s fine in a demo and fatal in a client report. Fixing them is what took VoidRecon from promising but noisy to something an operator would actually run on an engagement.

Profiles instead of flag soup: passive, quick, standard, deep, stealth.

Reports that read as a story — dossiers and the attack plan first, findings grouped and collapsed by severity, the raw firehose in JSON for your own tooling.

VoidRecon is built for authorized work — bug bounty programs you’re enrolled in, engagements you’re contracted for. Passive collection is on by default; anything that touches a target is gated behind both an explicit flag and a positive in-scope check. It’s still a work in progress, and it’s powerful. Stay in scope. Stay in the law.

Try it

git clone https://github.com/CypherNova1337/VoidRecon && cd VoidRecon

pip install -e “.\[full\]”

voidrecon setup

voidreon wizard

It’s open source. It’s free. It runs on one command and gets out of your way.

If you hunt, run it on your next in-scope target and tell me where it’s wrong — that feedback loop is exactly what built it.

[GitHub - CypherNova1337/VoidRecon: work in progress](https://github.com/CypherNova1337/VoidRecon)

Built and maintained by VoidSec.
