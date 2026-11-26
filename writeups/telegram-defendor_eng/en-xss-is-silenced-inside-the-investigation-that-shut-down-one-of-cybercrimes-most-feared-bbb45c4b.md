# 🛑 XSS.IS — One of the Largest Cybercrime Forums — Shut Down

- **Source URL:** https://www.redhotcyber.com/en/post/xss-is-silenced-inside-the-investigation-that-shut-down-one-of-cybercrimes-most-feared-bazaars
- **Fetched from:** https://web.archive.org/web/20260217203940/https://www.redhotcyber.com/en/post/xss-is-silenced-inside-the-investigation-that-shut-down-one-of-cybercrimes-most-feared-bazaars/
- **Fetched:** 2026-11-26
- **Channel:** @defendor_eng
- **Telegram message:** https://t.me/defendor_eng/391 (id 391)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
TIMESTAMPS

The Wayback Machine - https://web.archive.org/web/20260217203940/https://www.redhotcyber.com/en/post/xss-is-silenced-inside-the-investigation-that-shut-down-one-of-cybercrimes-most-feared-bazaars/

Author [Luca Stivali](https://web.archive.org/web/20260217203940/https://www.redhotcyber.com/en/post/author/Luca-Stivali/)

24 July 2025 15:09

Imagine opening your favorite forum bookmark, like every evening, to find new stealer variants or yet another batch of newly breached credentials. Instead of the usual noticeboard, a banner appears with three prominent logos: the French Brigade for the Fight against Cybercrime, the Ukrainian Cyber Intelligence Department, and Europol.

Below, a blunt text: **“This domain has been seized.”** Thus the curtain fell on **XSS.IS**, the clandestine auction room that for twelve years brought [malware](https://web.archive.org/web/20260217203940/https://www.redhotcyber.com/en/post/what-is-malware-between-science-fiction-the-lab-and-reality/) developers, access brokers, and [ransomware](https://web.archive.org/web/20260217203940/https://www.redhotcyber.com/en/post/what-is-ransomware-lets-explore-how-raas-works-and-what-it-means/) affiliates together.

What follows is not just the story of a dawn raid: it is the The story of a timed investigation that, over four years, transformed encrypted chat logs and Bitcoin transactions into an international arrest warrant. This is a behind-the-scenes journey into an operation that, by undermining infrastructure and trust, shook up the entire cybercrime black market. If you think a dark forum is safe from prying eyes, this story might change your mind.

When, on July 2, 2021, the French National Prosecutor’s Office for Cybercrime (JUNALCO) opened a file on XSS.SI, the goal was to understand **how** that forum managed to stay online despite constant references to extortion and intrusions against French companies. Investigators from the Police Prefecture’s Cybercrime Brigade (BL2C) started from the bottom: they listed DNS records, analyzed “fresh” TLS certificates, and reconstructed a map of bulletproof servers in the Netherlands, Russia, and Malaysia.

The key insight came when an analyst noticed that, every time a major deal was closed on the forum, several users cited the same Jabber domain, **thesecure.biz**. BL2C asked the investigating judge to **monitor** that server: not a mass acquisition, but a “surgical log” of the chats used by the staff. The wiretap order reveals the administrator’s work shifts – always between 9 a.m. and 6 p.m. in Kiev – and above all the **Bitcoin wallet**, which receives the 3% commissions withheld from escrow ([AP News](https://web.archive.org/web/20260217203940/https://apnews.com/article/b87867a1880ee80d97a1b2a5bc2daefe?utm_source=chatgpt.com), [SecurityWeek](https://web.archive.org/web/20260217203940/https://www.securityweek.com/france-says-administrator-of-cybercrime-forum-xss-arrested-in-ukraine/?utm_source=chatgpt.com)).

By the end of 2023, the file is already a pile of technical evidence: IP addresses, timestamps, cryptocurrency amounts, backend screenshots, and even the hashes of automatic backups saved by the admin on a remote NAS.

Finding the **real name** behind the nickname requires patience. Europol – entering the scene with its European Cybercrime Centre – cross-references three data sets:

- **[Open source](https://web.archive.org/web/20260217203940/https://www.redhotcyber.com/en/post/the-story-of-open-source-a-success-story-of-humankind/) and leaks**: avatars reused in smaller forums, old commits on GitHub, and a 2014 PGP key generated in Kyiv.
- **Stylometry**: Forensic linguistics experts compare grammar, emojis, and average sentence length with thousands of XSS posts and the aforementioned commits: the match exceeds 90%.
- **Follow-the-money**: Thanks to a European investigative order, two exchanges are providing Know-Your-Customer data on those who converted BTC to **Tether** and then cash at a crypto kiosk in Kyiv. The figures coincide with the admin’s earnings estimated at**over 7 million euros** ([Reuters](https://web.archive.org/web/20260217203940/https://www.reuters.com/technology/suspect-linked-russian-language-cybercrime-forum-arrested-ukraine-2025-07-23/?utm_source=chatgpt.com), [CyberScoop](https://web.archive.org/web/20260217203940/https://cyberscoop.com/xss-cybercrime-forum-admin-arrest/?utm_source=chatgpt.com)).

When Ukrainian internal security (Služba Bezpeky Ukraïny, Department Cyber) verifies that the man actually lives in the neighborhood indicated by the analysis, and the pieces of the puzzle fit together.

At **6:00** in the morning, SBU agents ring the doorbell of a fourth-floor apartment in Kyiv. Inside, they find a Linux laptop, a Synology NAS, and two FIDO tokens: everything is cloned on-site using Europol portable forensic kits. The passphrases—handwritten in a notebook—allow the disks to be decrypted before the suspect even reaches the police station.

In parallel, the registrars managing **xss.**is receive a French seizure order, countersigned by Europol, and redirect the DNS to a server in Paris with a “takeover” banner. The same thing happens with the Jabber node: residual traffic flows into a police-monitored sinkhole, useful for mapping unsuspecting affiliates attempting to connect ([Hackread](https://web.archive.org/web/20260217203940/https://hackread.com/xss-is-cybercrime-forum-seized-ukraine-arrested-admin/?utm_source=chatgpt.com),  [Ars Technica](https://web.archive.org/web/20260217203940/https://arstechnica.com/tech-policy/2025/07/ukrainians-arrest-alleged-admin-of-major-crime-forum-xss/?utm_source=chatgpt.com)).

Within **two hours**, the forum disappears from the web, and the alleged administrator – a thirty-five-year-old Ukrainian – is in pre-trial detention on charges of criminal conspiracy, extortion, and money laundering.

| **Date** | **Event** | **Investigative Detail** | 
|---|---|---|
| 2013 | XSS is born (heir to *DaMaGeLaB*) | [Exploit](https://web.archive.org/web/20260217203940/https://www.redhotcyber.com/en/post/what-are-security-bugs-a-journey-through-pocs-exploits-bug-bounty-programs-and-work/) forum and internal trust score | 
| December 2018 | Rebrand to “XSS” | Access by invitation, paid arbitration | 
| May 2021 | [Ransomware](https://web.archive.org/web/20260217203940/https://www.redhotcyber.com/en/post/what-is-ransomware-lets-explore-how-raas-works-and-what-it-means/) ban | Attempt to lower the Profile after Colonial Pipeline | 
| July 2021 | File opened in Paris | JUNALCO entrusts the case to BL2C ( [infosecurity-magazine.com](https://web.archive.org/web/20260217203940/https://www.infosecurity-magazine.com/news/suspected-xss-forum-admin-arrested/?utm_source=chatgpt.com)) | 
| August 2021 | Wiretap *thesecure.biz* | Selective staff chat logs ( [AP News](https://web.archive.org/web/20260217203940/https://apnews.com/article/b87867a1880ee80d97a1b2a5bc2daefe?utm_source=chatgpt.com)) | 
| 2022-2023 | [OSINT](https://web.archive.org/web/20260217203940/https://www.redhotcyber.com/en/post/what-is-open-source-intelligence-osint-its-importance-and-necessity-in-todays-world/) + blockchain analytics | Alias→wallet→KYC | 
| September 2024 | EU-AU Task Force | Europol creates a mobile office in Kyiv | 
| July 2025 | Arrest and domain seizure | SBU raid, online seizure banner | 

If XSS was the marketplace, its real treasure was the **escrow service**: an administrator-guarantor who held the funds until the buyer and seller said “OK, everything’s fine.” Fixed commission: 3% – sometimes 5% for riskier sales ([securitymagazine.com](https://web.archive.org/web/20260217203940/https://www.securitymagazine.com/articles/93048-digital-shadows-research-escrow-systems-on-cybercriminal-forums?utm_source=chatgpt.com), [ReliaQuest](https://web.archive.org/web/20260217203940/https://reliaquest.com/blog/escrow-systems-on-cybercriminal-forums/?utm_source=chatgpt.com)). Payment was made in Bitcoin, with final approval via Jabber. It’s the same model we see on Exploit and WWH-Club, but XSS had two pluses: fast arbitrators (within 24 hours) and a “VIP” channel for transactions over $50,000.

**thesecure.biz** – the Jabber server used by XSS staff to manage disputes and escrow – is also completely offline. A simple “multioc check” (see screenshot) shows timeouts from all test nodes, from Australia to Finland: no HTTP response, no replacement banner, just network silence.

According to sources close to the investigation, the dump recovered in the raid contains:

- **13 TB** of posts, private messages, and Jabber logs;
- **93,000 escrows** closed (2019-2025) with associated amounts and wallets;
- Over **1,000 arbitrations** with evidence of internal fraud (screenshots, encrypted files, PGP signatures).

For law enforcement, it’s pure gold: by cross-referencing wallets with Chainalysis blacklists and the anti-money laundering complaints database, it’s possible to trace access brokers, [ransomware](https://web.archive.org/web/20260217203940/https://www.redhotcyber.com/en/post/what-is-ransomware-lets-explore-how-raas-works-and-what-it-means/) developers, and even money-laundering mules. Incident responders, however, will be able to notify companies whose data appears among the “packages” sold: a rare opportunity to close the attack chain before it materializes.

With offline XSS, flows migrate to **Exploit** and small Telegram channels. But the “guarantee” is missing: scams are increasing, as demonstrated by the first scam-report threads published on Exploit less than 48 hours after the seizure. It’s the same dynamic seen after the raids against **Genesis Market** (April 2023) and **BreachForums** (2023-2024): without a credible arbiter, the dark web becomes the Wild West and profit margins collapse ([Department of Justice](https://web.archive.org/web/20260217203940/https://www.justice.gov/archives/opa/pr/criminal-marketplace-disrupted-international-cyber-operation?utm_source=chatgpt.com), [CyberScoop](https://web.archive.org/web/20260217203940/https://cyberscoop.com/fbi-seizure-genesis-market-cybercrime/?utm_source=chatgpt.com)).

- **Cascading investigations**– As with Genesis, the seizure banner could soon invite users to “come forward” in exchange for a reduced sentence.
- **Smaller, more private forums**– Operators will migrate to Tox networks, “ghost” sessions in Matrix, and one-to-one Telegram channels.
- **Decentralized escrows**– There’s already talk of smart contracts on anonymous blockchains to avoid relying on a single guarantor. But history teaches us that, without human trust, automated contracts don’t last long.

The seizure of XSS isn’t just another arrest: it’s a direct attack on the **trust mechanism** that supports criminal markets. Without escrow, the dark web risks imploding into suspicious micro-communities. And each new micro-community will, in turn, be an easier target to infiltrate.

Europol, Reuters, Associated Press, SecurityWeek, Infosecurity-Magazine, CyberScoop, ReliaQuest, DigitalShadows, Department of Justice (Genesis Market), TrendMicro (OperationCronos), Europol (OperationEndgame) ([AP News](https://web.archive.org/web/20260217203940/https://apnews.com/article/b87867a1880ee80d97a1b2a5bc2daefe?utm_source=chatgpt.com), [Reuters](https://web.archive.org/web/20260217203940/https://www.reuters.com/technology/suspect-linked-russian-language-cybercrime-forum-arrested-ukraine-2025-07-23/?utm_source=chatgpt.com), [CyberScoop](https://web.archive.org/web/20260217203940/https://cyberscoop.com/xss-cybercrime-forum-admin-arrest/?utm_source=chatgpt.com), [SecurityWeek](https://web.archive.org/web/20260217203940/https://www.securityweek.com/france-says-administrator-of-cybercrime-forum-xss-arrested-in-ukraine/?utm_source=chatgpt.com), [Europol](https://web.archive.org/web/20260217203940/https://www.europol.europa.eu/media-press/newsroom/news/largest-ever-operation-against-botnets-hits-dropper-malware-ecosystem?utm_source=chatgpt.com), [trendmicro.com](https://web.archive.org/web/20260217203940/https://www.trendmicro.com/en_us/research/24/d/operation-cronos-aftermath.html?utm_source=chatgpt.com), [Ministry of Justice](https://web.archive.org/web/20260217203940/https://www.justice.gov/archives/opa/pr/criminal-marketplace-disrupted-international-cyber-operation?utm_source=chatgpt.com), [ReliaQuest](https://web.archive.org/web/20260217203940/https://reliaquest.com/blog/escrow-systems-on-cybercriminal-forums/?utm_source=chatgpt.com))

Follow us on [Google News](https://web.archive.org/web/20260217203940/https://news.google.com/publications/CAAqKggKIiRDQklTRlFnTWFoRUtEM0psWkdodmRHTjVZbVZ5TG1OdmJTZ0FQAQ?hl=en-US&gl=US&ceid=US%3Aen) to receive daily updates on cybersecurity. [Contact us](https://web.archive.org/web/20260217203940/mailto:redazione@redhotcyber.com) if you would like to report news, insights or content for publication.

Cyber Security Enthusiast and entrepreneur in the IT industry for 25 years, expert in network design and management of complex IT systems. Passion for a proactive approach to cyber security: understanding how and what to protect yourself from is crucial.
