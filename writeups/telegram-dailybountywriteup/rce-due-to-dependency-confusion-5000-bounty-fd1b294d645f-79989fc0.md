# RCE due to Dependency Confusion — $5000 bounty!

- **Source URL:** https://chevonphillip.medium.com/rce-due-to-dependency-confusion-5000-bounty-fd1b294d645f?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20251004091523/https://chevonphillip.medium.com/rce-due-to-dependency-confusion-5000-bounty-fd1b294d645f
- **Fetched:** 2026-11-27
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/2641 (id 2641)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
Member-only story

# RCE due to Dependency Confusion — $5000 bounty!

Hey everyone! I’m back with another cool write-up about a bug bounty report I submitted to a private program on HackerOne. Guess what? **I got a $5,000 reward and they took care of it in just 30 minutes!**

I won’t go into the nitty-gritty of dependency confusion since there are plenty of awesome [write-ups](https://medium.com/@alex.birsan/dependency-confusion-4a5d60fec610) out there that cover it.

So, I was checking out this custom auth portal where you can get into multiple internal apps after logging in. Bummer, though, they didn’t give us credentials during testing, so only company employees could log in.

But hey, I didn’t give up! I looked at the .js files the app loaded, using the network tab in my browser. I saw that when the auth login page loaded, it bundled an ***app.\[random\_characters\].js*** file.

I remembered reading about [source maps](https://pulsesecurity.co.nz/articles/javascript-from-sourcemaps) and how you can put front-end source code back together with them. So, I used this cool tool called **Sourcemapper** ([https://github.com/denandz/sourcemapper](https://github.com/denandz/sourcemapper)) that helps do just that.

With the source code in hand, I started hunting for vulnerabilities. I found a few interesting ones, but what really caught my eye in the code were the import statements.
