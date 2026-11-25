# Brute Force

- **Source URL:** https://medium.com/@raksharoot/brute-force-the-least-clever-attack-that-still-wins-a1353a1508cd
- **Fetched from:** https://medium.com/@raksharoot/brute-force-the-least-clever-attack-that-still-wins-a1353a1508cd?source=rss-4206d471b207------2
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14959 (id 14959)
- **Method:** medium-rss-feed (full content:encoded) readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- **Author/Published (RSS):** Raksharoot / Sun, 25 Oct 2026 18:01:20 GMT

Disclaimer: Educational content only. Brute forcing accounts you don’t own is illegal and can DoS services. Test only on systems you own or have written authorization for. Be aware that most production systems have account lockout, you can lock out real users by accident.

Brute force is the attack everyone dismisses and nobody actually tests properly.

***The logic goes:*** “modern passwords are long, rate limits exist, brute force is dead.” And then a company gets owned because admin:admin was still set on an internal dashboard.

***The truth is boring:*** brute force is not clever, but it’s persistent. And most of the value doesn’t come from guessing hard, it comes from the things people skip:

This isn’t a tool reference, the actual command syntax for hydra, medusa, ncrack, and legba for forty services is a click away on any cheat sheet. This is about how to think about credential attacks so you don’t waste a week running rockyou.txt against a login page that was never going to work.

Before you brute force anything, check if the target shipped with default credentials.

Every appliance has them. Routers, NAS devices, CMS installers, CI/CD servers, monitoring dashboards, printers, IoT cameras. Developers install them for setup and then forget to change them.

Look up the product name and version in one of these:

I’ve seen internal admin panels on *admin/admin* in production environments, the app was “internal only” and the team assumed nobody could reach it. Internal networks leak. Default credentials are the cheapest win in the engagement.

**Do this first.** Before you write a single script.

Here’s the thing about brute force: **rockyou.txt is a starting point**, not a strategy. It’s a leaked collection of passwords from 2009. Every rate-limited, correctly-configured target is immune to it. Every well-designed password policy defeats it.

What actually works is a **target-specific wordlist**.

*cewl* scrapes the target site and extracts words:

The *-m 5* means minimum word length of 5. Shorter words are usually noise. Then mutate the output with leetspeak, case variations, and append years.

If the site has a lot of JavaScript, run tok over the JS URLs to pull identifiers, function names, and string constants:

And *getjswords.py* does the same thing for JS-specific content:

You’d be surprised how many password reset questions, internal project names, and API keys leak through JS comments.

CUPP generates passwords from personal information — names, dates, pets, teams, cities:

*python3 cupp.py -i*

If the target’s main page says “Founded by Jane Doe in Madrid, 2018, big fan of Real Madrid,” you now have material. If there’s an HR page with employee names, cross-reference with LinkedIn for personal details.

This is OSINT feeding a wordlist. It’s boring, it’s manual, and it works.

Wister takes a set of seed words and generates all reasonable combinations:

The *-c 1 2 3 4 5* controls combination depth. Ten seed words can produce tens of thousands of candidates, but they’re all plausible candidates.

*crunch* generates patterns from a charset:

The *-t* flag uses placeholders:

So, *@@^^%%* generates candidates that match a specific structure (capital letter, two lowercase, two specials, two digits). That’s useful when you know a password policy and want to stay inside the accepted rules without generating 2^20 candidates.

Start from rockyou. Then layer in:

Don’t use all of them together. Pick a set based on the target’s apparent era and complexity. An old internal PHP app installed in 2015 is different from a modern SaaS product.

This is where people get fired.

**Brute forcing** means trying many passwords against one account. Almost every login form has a lockout after 5 or 10 attempts. You will lock out real users. You will probably get caught.

**Password spraying** means trying one password against many accounts. It’s designed to stay under lockout thresholds. The math:

If even one user has a common password, you win. And you never tripped any single account’s lockout.

**Always spray, don’t brute.** The exception is when you’re testing a single high-value account (like the admin) with a small, carefully-chosen password list, and you should confirm the lockout threshold before you do, ideally on a test account you control.

Before you write a wordlist, test the rate limit.

Create a test account. Submit wrong credentials ten times. Then a hundred. Then a thousand.

Watch for:

The last case is more common than you’d think on internal applications. Dev teams add a “forgot password” page and assume rate limiting is a default of the framework. It’s usually not.

If there is a rate limit, look for bypasses:

This is the part I find genuinely interesting — how the industrial-scale brute forcers actually work.

A 2024 era piece of malware called *GoBruteforcer* was caught running an internet-wide scanning workflow. It’s a good model for how automated credential attacks operate, because it’s not clever — it’s systematic.

It maintains a fleet of concurrent workers sized to the target architecture:

Every second it checks the active worker count and spawns replacements to maintain the target. Each worker handles **one target IP** and then exits — no reuse of connections, no patterns for defenders to spot.

It generates random public IPv4 addresses and filters them:

The logic is: **avoid infrastructure that’s likely monitored**. Hitting AWS us-east-1 with thousands of login attempts gets you blocked in seconds. Hitting random residential ranges in smaller countries gets you a longer run.

Before it tries to log in, it probes the service port with a short timeout (\~2 seconds):

If the port doesn’t respond, it moves on. If it does, it starts cleartext login attempts.

If it can’t fetch its credential list from the C2 server, it falls back to a small built-in list. Even malware has a fallback wordlist.

Every successful hit fires an HTTP GET beacon to the C2:

Service codes are simple: 1 = phpMyAdmin, 2 = MySQL, 3 = FTP, 4 = PostgreSQL. The browser User-Agent is standard Chrome, so the traffic blends into normal web noise.

The phpMyAdmin spray is particularly sophisticated:

This matters because most brute-force scripts assume one auth pattern. The good ones fingerprint the version and adapt.

If you’re on the defensive side:

If you’re on the offensive side (in an authorized engagement):

The full command for every service is in any cheat sheet. Thematically, here’s what actually matters:

For every hash you can’t crack locally, there’s a website that’s already tried.

Before you spin up a GPU cluster, paste the hash. Fifty percent of the time, it’s already cracked.

For NTLM/NetNTLMv1 with custom challenge-response, *shuck.sh* handles the ESS/SSP variations that break most tools.

Order I go in:

Brute force is not a technical attack. It’s a ***discipline*** attack.

The value isn’t in a clever payload or a fast GPU. It’s in the operations that most testers skip:

The industrial scanners do all of this. That’s why they work. They’re not smarter than you, they just don’t skip steps.

And on the defensive side: if a login endpoint has no rate limit, no lockout, and default credentials, no amount of “we’re internal” changes the outcome. Someone with a VPS and a wordlist will find it.

Test on your own systems. Be aware of lockout risk. **Never run internet-wide scans — that’s abuse, not research.** And when you find weak credentials, report them as critical, because that’s what they are.

**Thanks for reading. If this was useful, Raksharoot has more where this came from.**
