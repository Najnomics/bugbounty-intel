# 🛡️ North Korean Hackers Attack the Web3 Ecosystem via npm

- **Source URL:** https://decrypt.co/344482/north-korean-hackers-crypto-open-source-software-hub
- **Fetched:** 2026-11-16
- **Channel:** @defendor_eng
- **Telegram message:** https://t.me/defendor_eng/1016 (id 1016)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
#### In brief

- More than 300 malicious code packages were uploaded to npm in what researchers call the “Contagious Interview” campaign.
- The fake job-recruitment lures targeted Web3 and crypto developers, stealing credentials and wallet keys.
- Security experts warn that software supply-chain attacks are becoming a preferred tool of state actors.

A U.S. cybersecurity firm says North Korean hackers have turned one of the world’s most widely used software libraries into a delivery system for malware. In a [report](https://socket.dev/blog/north-korea-contagious-interview-campaign-338-malicious-npm-packages) last week, researchers at [Socket](http://socket.dev'), a supply-chain security company, said they had found more than 300 malicious code packages uploaded to the npm registry, a central repository used by millions of developers to share and install JavaScript software.

The packages—small pieces of reusable code used in everything from websites to crypto applications—were designed to look harmless. But once downloaded, they installed malware capable of stealing passwords, browser data, and cryptocurrency wallet keys. Socket said the campaign, which it calls “Contagious Interview,” was part of a sophisticated operation run by North Korean state-sponsored hackers who pose as tech recruiters to target developers working in blockchain, Web3, and related industries.

Why it matters: [npm](https://docs.npmjs.com/about-npm) is essentially the backbone of the modern web. Compromising it allows attackers to slip malicious code into countless downstream apps. Security experts have warned for years that such “software supply-chain” attacks are among the most dangerous in cyberspace because they spread invisibly through legitimate updates and dependencies.

The trail to North Korea

Socket’s researchers traced the campaign through a cluster of look-alike package names—misspelled versions of popular libraries such as express, dotenv, and hardhat—and through code patterns linked to previously identified North Korean malware families known as BeaverTail and InvisibleFerret. The attackers used encrypted “loader” scripts that decrypted and executed hidden payloads directly in memory, leaving few traces on disk.

The firm said roughly 50,000 downloads of the malicious packages occurred before many were removed, though some remain online. The hackers also used fake LinkedIn recruiter accounts, a tactic consistent with previous DPRK cyber-espionage campaigns documented by the [U.S. Cybersecurity and Infrastructure Security Agency](https://www.cisa.gov/search?g=north+korean#gsc.tab=0&gsc.q=north%20korean&gsc.page=1) (CISA) and previously reported in [*Decrypt*](https://decrypt.co/329225/inside-north-korea-hiring-scams-crypto-firms). The ultimate targets, investigators believe, were machines holding access credentials and digital wallets.

While Socket’s findings line up with reports from other security groups and government agencies linking North Korea to cryptocurrency thefts totaling billions of dollars, independent verification of every detail—such as the exact number of compromised packages—remains pending. Still, the technical evidence and patterns described are consistent with prior incidents attributed to Pyongyang.

Npm’s owner, [GitHub, has said](https://github.blog/security/supply-chain-security/our-plan-for-a-more-secure-npm-supply-chain/) it removes malicious packages when discovered and is improving account-verification requirements. But the pattern, researchers say, is whack-a-mole: take down one set of malicious packages, and hundreds more soon take their place.

For developers and crypto startups, the episode underscores how vulnerable the software supply chain has become. Security researchers urge teams to treat every “npm install” command as potential code execution, scan dependencies before merging them into projects, and use automated vetting tools to catch tampered packages. The open-source ecosystem’s strength—its openness—remains its greatest weakness when adversaries decide to weaponize it.

## Daily Debrief Newsletter

Start every day with the top news stories right now, plus original features, a podcast, videos and more.

[Add on Google](https://www.google.com/preferences/source?q=decrypt.co)
