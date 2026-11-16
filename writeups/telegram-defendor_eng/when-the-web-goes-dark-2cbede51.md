# 🌐 Internet outage caused by a single Cloudflare error

- **Source URL:** https://rekt.news/when-the-web-goes-dark
- **Fetched:** 2026-11-16
- **Channel:** @defendor_eng
- **Telegram message:** https://t.me/defendor_eng/863 (id 863)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# When the Web Goes Dark

*November 18, 2025, 6:20 AM ET. [The internet stopped working for many of us](https://www.theguardian.com/technology/live/2025/nov/18/cloudflare-down-internet-outage-latest-live-news-updates).*

**Not gradually. Not with warning signs. One moment you're scrolling, trading, chatting with AI - the next, [500 errors almost everywhere you looked](https://x.com/jonypopov/status/1990759153086980567).**

[X went dark mid-tweet. ChatGPT died mid-sentence](https://www.pcmag.com/news/cloudflare-outage-takes-down-chatgpt-uber-x-more-heres-what-happened). Claude froze.

[Even Downdetector](https://www.itpro.com/infrastructure/a-massive-cloudflare-outage-has-taken-down-x-and-openai-and-even-bricked-outage-tracker-site-downdetector) - the site you check when everything breaks - couldn't load to tell you everything was broken.

[Twenty percent of the web just vanished because Cloudflare](https://www.cnbc.com/2025/11/18/cloudflare-down-outage-traffic-spike-x-chatgpt.html), the company that protects the internet from attacks, accidentally attacked itself.

A routine configuration change [database permissions update](https://blog.cloudflare.com/18-november-2025-outage/) triggered a [hidden bug in their bot mitigation system](https://techcrunch.com/2025/11/18/cloudflare-blames-massive-internet-outage-on-latent-bug/), and suddenly the guardian at the gate had locked everyone out.

**Crypto Twitter spent October mocking centralization [when AWS took down Coinbase](https://rekt.news/we-have-centralization-issue).**

November's Cloudflare outage? Crickets, at least for a few hours.

Hard to tweet about infrastructure fragility when Twitter runs on the infrastructure that just died.

[Several essential services faltered (transit sites went down), some corporate web interfaces glitched](https://apnews.com/article/cloudflare-outage-x-openai-9335e8e0da2a0027d1fbac5eb97d11ae), and [blockchain explorers like Arbiscan and DeFiLlama experienced 500 errors](https://www.coindesk.com/business/2025/11/18/cloudflare-global-outage-spreads-to-crypto-multiple-front-ends-down) - while the blockchains themselves showed no signs of consensus disruption.

*When your "decentralized" revolution can't function because one company's config file grew too large, who's really in control?*

*Credit:[The Guardian](https://www.theguardian.com/technology/live/2025/nov/18/cloudflare-down-internet-outage-latest-live-news-updates), [Jony Popov](https://x.com/jonypopov/status/1990759153086980567), [PC Mag](https://www.pcmag.com/news/cloudflare-outage-takes-down-chatgpt-uber-x-more-heres-what-happened), [ITPro](https://www.itpro.com/infrastructure/a-massive-cloudflare-outage-has-taken-down-x-and-openai-and-even-bricked-outage-tracker-site-downdetector), [CNBC](https://www.cnbc.com/2025/11/18/cloudflare-down-outage-traffic-spike-x-chatgpt.html), [Cloudflare](https://blog.cloudflare.com/18-november-2025-outage/), [TechCrunch](https://techcrunch.com/2025/11/18/cloudflare-blames-massive-internet-outage-on-latent-bug/), [AP News](https://apnews.com/article/cloudflare-outage-x-openai-9335e8e0da2a0027d1fbac5eb97d11ae), [CoinDesk](https://www.coindesk.com/business/2025/11/18/cloudflare-global-outage-spreads-to-crypto-multiple-front-ends-down), [Tom’s Hardware](https://www.tomshardware.com/service-providers/cloudflare-apologizes-after-outage-takes-major-websites-offline), [Dane Knecht](https://x.com/dok2001/status/1990791419653484646?s=20), [Tom’s Guide](https://www.tomsguide.com/news/live/cloudfare-outage-november-2025-x-chatgpt), [Surya](https://x.com/sunlight_30/status/1990766080911188445), [Sheep Esports](https://x.com/Sheep_Esports/status/1990801241501532485), [TheBlock](https://www.theblock.co/post/379242/cloudflare-global-network-outage-hits-multiple-crypto-front-ends-in-widespread-disruption), [Kraken](https://status.kraken.com/incidents/p03qp5y0rnw4), [BitMEX](https://status.bitmex.com/), [Ledger](https://status.ledger.com/incidents/bvjd0fw4nbwv), [Blockchain News](https://blockchain.news/flashnews/cloudflare-outage-2025-internet-disruptions-while-blockchain-stays-online-what-crypto-traders-should-watch), [Statista](https://www.statista.com/statistics/985443/worldwide-ddos-bot-protection-market-share/), [Bleeping Computer](https://www.bleepingcomputer.com/news/technology/cloudflare-hit-by-outage-affecting-global-network-services/), [Jameson Lopp](https://x.com/lopp/status/1990756066653843861), [Ben Schiller](https://x.com/btschiller/status/1980408035156914483), [Article 19](https://www.article19.org/resources/aws-outage-exposes-democratic-failure-of-concentration-in-cloud-computing/), [CoinTelegraph](https://cointelegraph.com/news/amazon-aws-outage-coinbase-app-robinhood)*

[11:05 UTC](https://blog.cloudflare.com/18-november-2025-outage/): Database access control change deployed.

[23 minutes later, at 11:28 UTC](https://blog.cloudflare.com/18-november-2025-outage/), Deployment reaches customer environments, first errors observed on customer HTTP traffic.

Translation: something broke, they just didn't know what yet.

By 11:48 UTC, [Cloudflare's official status site acknowledged “internal service degradation”](https://www.tomshardware.com/service-providers/cloudflare-apologizes-after-outage-takes-major-websites-offline) - corporate shorthand for: everything is on fire and everyone can see the smoke.

[The cascade happened fast](https://blog.cloudflare.com/18-november-2025-outage/): the change broke Cloudflare’s bot-management layer - its proxy panicked when it loaded a doubled-size feature file.

[Downstream systems failed](https://blog.cloudflare.com/18-november-2025-outage/): Workers KV and Access couldn’t reach the proxy. Error rates spiked across the network, and CPU usage surged as observability tools heated up.

[Traffic still hit Cloudflare’s edge](https://blog.cloudflare.com/18-november-2025-outage/) - but the proxy couldn’t answer.

[Cloudflare initially thought they were under attack](https://blog.cloudflare.com/18-november-2025-outage/). A hyper-scale DDoS attack, specifically.

[When their status page](https://blog.cloudflare.com/18-november-2025-outage/) - hosted completely off Cloudflare's infrastructure - went down simultaneously, engineers suspected a coordinated assault targeting both their systems and their monitoring.

*But, they weren't being attacked. They'd attacked themselves.*

**The company’s CTO, Dane Knecht, [posted](https://x.com/dok2001/status/1990791419653484646?s=20) a public apology shortly after services were restored, calling the incident "unacceptable" and attributing the disruption to a routine configuration change that triggered a crash in its bot mitigation layer.**

"We failed our customers and the broader internet," [Knecht wrote](https://www.tomshardware.com/service-providers/cloudflare-apologizes-after-outage-takes-major-websites-offline). "A latent bug in a service underpinning our bot mitigation capability started to crash after a routine configuration change. That cascaded into a broad degradation to our network and other services. This was not an attack."

[11,183 outage reports flooded Downdetector](https://www.tomsguide.com/news/live/cloudfare-outage-november-2025-x-chatgpt) at peak.

Over five and a half hours of digital darkness passed [before full restoration at 17:06 UTC](https://blog.cloudflare.com/18-november-2025-outage/), though [the worst of the impact had eased by 14:30](https://blog.cloudflare.com/18-november-2025-outage/) when the correct Bot Management configuration file was deployed globally.

**Web2 took the hit first:**

*X logged [9,706 outage reports](https://www.tomsguide.com/news/live/cloudfare-outage-november-2025-x-chatgpt).*

Users got "[Oops, something went wrong](https://x.com/sunlight_30/status/1990766080911188445)" messages instead of their timeline.

[ChatGPT went silent](https://www.pcmag.com/news/cloudflare-outage-takes-down-chatgpt-uber-x-more-heres-what-happened) mid-conversation.

[Spotify stopped streaming](https://www.tomsguide.com/news/live/cloudfare-outage-november-2025-x-chatgpt). Canva locked out designers. Uber and Door Dash experienced issues.

Even gamers were impacted, [as League of Legends got disconnected](https://x.com/Sheep_Esports/status/1990801241501532485) mid-game.

Even [McDonald's self-service kiosks allegedly displayed error screens](https://www.reddit.com/r/CloudFlare/comments/1p0awqw/even_my_local_mcdonald_is_broken_lol/). Lunch rush meets infrastructure failure.

*Crypto wasn’t marked safe either.*

[Coinbase’s front-end blinked out](https://www.theblock.co/post/379242/cloudflare-global-network-outage-hits-multiple-crypto-front-ends-in-widespread-disruption), leaving users staring at broken login pages.

[Kraken's web and mobile apps](https://status.kraken.com/incidents/p03qp5y0rnw4) - both dead. Direct result of Cloudflare's global faceplant.

[BitMEX posted on their status page](https://status.bitmex.com/): investigating outage, degraded performance, funds safe. Same script, different exchange.

[Etherscan couldn't load](https://www.theblock.co/post/379242/cloudflare-global-network-outage-hits-multiple-crypto-front-ends-in-widespread-disruption). [Arbiscan went down](https://status.arbitrum.io/cmi4j4lhg00nry2xtno7vp9rg).

DeFiLlama's analytics dashboard [served intermittent internal server errors](https://www.coindesk.com/business/2025/11/18/cloudflare-global-outage-spreads-to-crypto-multiple-front-ends-down).

Even [Ledger reported degraded availability of some services due to Cloudflare outage](https://status.ledger.com/incidents/bvjd0fw4nbwv).

**But here's what didn't break:**

[Major exchanges like Binance, OKX, Bybit, Crypto.com, and KuCoin reportedly experienced no front-end outages](https://coinstats.app/news/6e838976c3bfe9b30cc97c309a088cd7f833d1045cab9619fc542a48133a4387_Cloudflare-Outage-Resolved-After-Disrupting-BitMEX-and-Kraken-FrontEnds/), and on-chain trading kept running - all while blockchains themselves remained fully functional, with no evidence of consensus disruption.

**Blockchain protocols continued operating independently - the issue wasn't on-chain, [but in the Web2 infrastructure people use to access them](https://blockchain.news/flashnews/cloudflare-outage-2025-internet-disruptions-while-blockchain-stays-online-what-crypto-traders-should-watch).**

*If blockchains kept working but nobody could access them, did crypto really stay online?*

### How One Database Query Killed 20% of the Web

*Cloudflare doesn't host websites. They don't run cloud servers like AWS.*

**They sit between you and the internet - a middleman for [24 million websites](https://backlinko.com/cloudflare-users), handling [20% of global web traffic](https://www.cloudflare.com/press/press-releases/2025/cloudflare-just-changed-how-ai-crawlers-scrape-the-internet-at-large/) through [330 cities across 120 countries](https://cf-assets.www.cloudflare.com/slt3lc6tev37/2wdhbwL52YTheg2uErH2VG/d0db20e0236f2ecc20d2347f531d6816/Intro_to_Cloudflare__2025_.pdf).**

**[Their pitch](https://www.cloudflare.com/application-services/products/):** Cloudflare pitches itself as a shield and accelerator: always-on DDoS protection, bot-mitigation, traffic routing, a global WAF, TLS termination, edge compute via Workers, and DNS services - all running on a unified security-performance network.

**The reality:**  [82% market share in DDoS protection](https://www.statista.com/statistics/985443/worldwide-ddos-bot-protection-market-share/). [449 Tbps of edge capacity](https://www.cloudflare.com/nl-nl/integrations/google-cloud/). Connected to [many major ISP and cloud providers on earth](https://www.bleepingcomputer.com/news/technology/cloudflare-hit-by-outage-affecting-global-network-services/).

**The problem:** When the middleman falls, everything behind them becomes unreachable simultaneously.

**Cloudflare CTO [Dane Knecht didn't sugarcoat it on X](https://x.com/dok2001/status/1990791419653484646):**

*"I won't mince words: earlier today we failed our customers and the broader Internet when a problem in Cloudflare network impacted large amounts of traffic that rely on us."*

[CEO Matthew Prince was even blunter](https://blog.cloudflare.com/18-november-2025-outage/):

*"Today was Cloudflare's worst outage since 2019... in the last 6+ years we've not had another outage that has caused the majority of core traffic to stop flowing through our network."*

**What actually broke:**

[Routine database permissions update](https://blog.cloudflare.com/18-november-2025-outage/). At 11:05 UTC, Cloudflare deployed a change to their ClickHouse database cluster to improve security and reliability. The change made table metadata explicitly visible to users who already had implicit access.

The problem? A database query that generated Cloudflare's [bot mitigation service](https://www.nbcnews.com/tech/internet/cloudflare-internet-services-disrupted-x-spotify-rcna244577) configuration file didn't filter for database name.

[The query](https://blog.cloudflare.com/18-november-2025-outage/) that manages threat traffic started returning duplicate entries - one set from the default database, another from the underlying r0 storage database. The feature file doubled in size. From approximately 60 features to over 200.

*Cloudflare had set a [hardcoded limit of 200 features](https://blog.cloudflare.com/18-november-2025-outage/) for memory preallocation - "well above our current use of \~60 features." Classic engineering: set a safety margin you think is generous, until it isn't.*

**The oversized file hit that limit. The [Rust code panicked](https://blog.cloudflare.com/18-november-2025-outage/). "thread fl2\_worker\_thread panicked: called Result::unwrap() on an Err value"**

Bot mitigation sits deep in Cloudflare's control layer. When it died, the [health check system](https://techcabal.com/2025/11/18/how-a-cloudflare-outage-rippled-across-the-internet/) that tells load balancers which servers are healthy lost its mind.

**Here's where it gets worse:** [the file regenerated every five minutes](https://blog.cloudflare.com/18-november-2025-outage/).

Bad data only generated if the query ran on an updated cluster node. So every five minutes, Cloudflare's network would either get a good file or a bad file, causing it to flicker between working and failing.

This made engineers think they were under a DDoS attack - systems don't usually recover and fail repeatedly from internal errors.

Eventually, every ClickHouse node was updated. Every file generated was bad. The flickering stopped. Complete, stable failure.

*No accurate signals. System defaults to conservative mode. Treats most servers as unhealthy. Traffic arrives but can't be routed properly.*

**Cloudflare's edge could receive your request - it just couldn't do anything with it.**

"This was not an attack," [Knecht emphasized](https://x.com/dok2001/status/1990791419653484646). Not malicious. Not a DDoS. Just a database query missing a filter meeting a permissions update at exactly the wrong moment.

**The promise that didn't deliver:** "99.99% uptime guarantee"

**Narrator:** it wasn't.

**This keeps happening:**

**[October 20, 2025](https://rekt.news/we-have-centralization-issue)** - AWS down 15 hours. DynamoDB DNS resolution failed in US-EAST-1. Coinbase froze. Robinhood stuttered. Infura disrupted MetaMask. Base, Polygon, Optimism, Arbitrum, Linea, Scroll - all offline. Users saw zero balances despite their funds sitting safely on-chain.

**[October 29, 2025](https://apnews.com/article/microsoft-azure-downdetector-service-disruption-0deffbd09c09ca4640c2f5452a9e483e)** - Microsoft Azure outage. Configuration propagation problems in Azure Front Door. Microsoft 365 down. Xbox Live dark. Business services interrupted.

**[July 2024](https://www.cnbc.com/2024/07/19/crowdstrike-suffers-major-outage-affecting-businesses-around-the-world.html)** - CrowdStrike's faulty Windows update. Flights halted. Hospitals delayed procedures. Financial services frozen. Multi-day recovery for full restoration.

**[June 2022](https://techcrunch.com/2022/06/21/cloudflare-outage-crypto-exchanges/)** - Previous Cloudflare outage. Several crypto exchanges halted. Same pattern, different year.

**[July 2019](https://investorplace.com/2019/07/cloudflare-outage-july-2-2019/)** - Even earlier Cloudflare failure. Coinbase offline. CoinMarketCap unreachable. The first warning nobody heeded.

Four major infrastructure outages in just the last 18 months.

Four times the same lesson: centralized infrastructure creates centralized failure.

**Four times crypto could have pivoted more towards decentralization while running on pipes owned by three companies.**

*How many warnings does it take before "assume outages will happen" becomes "build like outages are guaranteed"?*

### The Decentralization Lie

*They sold you a vision.*

**Decentralized finance. Censorship-resistant money. Trustless systems. No single point of failure. Not your keys, not your coins. Code is law.**

[November 18th delivered the reality](https://blog.cloudflare.com/18-november-2025-outage/): Cloudflare had a bad morning and some of crypto stopped working for a few hours.

*No blockchain protocol failures were reported. Bitcoin kept running. Ethereum kept running. The chains themselves worked fine.*

*Exchange UIs died. Block explorers went dark. Wallet interfaces failed. Analytics platforms crashed. Trading interfaces returned 500 errors.*

Users couldn't access the "decentralized" blockchains they supposedly owned. Protocol worked perfectly - if you could reach it.

*Here are some quotes that hurt…*

**David Schwed, SovereignAI COO, [didn't hold back](https://www-theblock-co.cdn.ampproject.org/c/s/www.theblock.co/amp/post/379242/cloudflare-global-network-outage-hits-multiple-crypto-front-ends-in-widespread-disruption):**

*"With Cloudflare down today and AWS just a few weeks ago, it's evident we can't simply outsource resiliency in our infrastructure to a single vendor. If your organization needs to be up 24/7, you have to build your infrastructure assuming these outages will happen. A business continuity plan comprised of 'wait for vendor to restore' is pure negligence."*

Pure negligence. Not an accident. Not an oversight. Negligence.

[Jameson Lopp captured it perfectly](https://x.com/lopp/status/1990756066653843861):

*"We took an amazing decentralized technology and have made it incredibly fragile by centralizing most services behind a handful of providers."*

[Ben Schiller said this during the AWS outage](https://x.com/btschiller/status/1980408035156914483), but it applies here too:

*"If your blockchain is down because of the AWS outage, you're not sufficiently decentralized."*

Replace AWS with Cloudflare. Same problem. Same failure to learn.

Why everyone chose convenience over principles:

Running your own infrastructure means buying expensive hardware, securing stable electricity, maintaining dedicated bandwidth, hiring security experts, implementing geographic redundancy, building disaster recovery systems, monitoring 24/7.

*Using Cloudflare means clicking a button, entering a credit card, deploying in minutes.*

**Someone else handles DDoS attacks. Someone else maintains uptime. Someone else worries about scaling.**

Startups chose speed to market. VCs demanded capital efficiency. Everyone picked easy over resilient.

Until it wasn't easy anymore.

[October's AWS outage](https://rekt.news/we-have-centralization-issue) sparked endless Twitter discourse about decentralization.

*November's Cloudflare outage? Crickets.*

Not philosophical silence. Not contemplative quiet.

Just the silence of people who can't tweet because Twitter runs on the infrastructure that died.

Can't mock the single point of failure when the single point of failure is the mockery platform.

**Protocol-level decentralization means nothing when your access layer runs on three companies' infrastructure - and two of them failed in the same month.**

*What exactly are we decentralizing if users can't reach it?*

### Monopolized Stranglehold

[AWS controls roughly 30% of global cloud infrastructure](https://www.statista.com/chart/18819/worldwide-market-share-of-leading-cloud-infrastructure-service-providers/). Microsoft Azure holds 20%. Google Cloud claims 13%.

**Three companies. [Over 60% of the cloud infrastructure that underpins the modern internet](https://www.statista.com/chart/18819/worldwide-market-share-of-leading-cloud-infrastructure-service-providers/).**

Crypto's supposed to fix centralization. Instead, it runs on the most centralized infrastructure on earth.

**Check the dependencies:**

[Coinbase - AWS](https://aws.amazon.com/solutions/case-studies/coinbase-migration-case-study/). [Binance - AWS. BitMEX - AWS. Huobi - AWS. Crypto.com - AWS](https://cointelegraph.com/news/amazon-aws-outage-coinbase-app-robinhood). [Kraken - AWS infrastructure](https://octoenergy-production-media.s3.amazonaws.com/documents/A0659_Kraken_Technologies_AR_2023_prf9_ForPublication.pdf), hit by Cloudflare's CDN failure anyway.

Many "decentralized" exchanges run on centralized pipes.

The difference between October and November:

**When AWS died, X stayed up. Crypto Twitter had a field day mocking infrastructure fragility.**

*When Cloudflare died, X died with it.*

Hard to laugh about single points of failure when the laughing platform is also the failure point.

The irony killed the discourse before it could start.

Three major outages in 30 days. Regulators noticed.

**Questions that should be asked in government offices:**

*Are these companies "systemically important"?
Should internet backbone services face utility-style regulation?
What happens when "too big to fail" meets tech infrastructure?
If Cloudflare controls 20% of web traffic, is that a monopoly problem?*

[Article 19's Corinne Cath-Speth wasn't subtle back when the last AWS outage occured](https://www.article19.org/resources/aws-outage-exposes-democratic-failure-of-concentration-in-cloud-computing/): "When a single provider goes dark, critical services go offline with it – media outlets become inaccessible, secure communication apps like Signal stop functioning, and the infrastructure that serves our digital society crumbles. We urgently need diversification in cloud computing."

**Translation:** Governments are realizing a handful of companies can shut down the internet.

Decentralized alternatives exist. Nobody uses them.

Arweave for storage. IPFS for distributed files. Akash for compute. Filecoin for decentralized hosting.

**The problems:**

*Performance lags behind centralized options. Latency issues users notice immediately.*

Adoption remains minimal. User experience feels clunky compared to clicking "Deploy to AWS."

Cost often runs higher than renting from the big three.

**The reality:**

*Building genuinely decentralized infrastructure is hard. Really hard.*

Most projects talk about decentralization. Few implement it. Centralized stays easier and cheaper.

Until 4 outages in 18 months reminds everyone that easier and cheaper comes with a price.

**Dr. Max Li, CEO of OORT, [called out the hypocrisy in a recent CoinDesk op-ed](https://www.coindesk.com/opinion/2025/11/01/the-aws-outage-shows-why-crypto-can-t-keep-relying-on-centralized-infrastructure):**

*"For an industry that prides itself on decentralization and constantly lauds its benefits, to be so reliant on vulnerable centralized cloud platforms for their own infrastructure feels like hypocrisy."*

His solution? Hybrid cloud strategies where exchanges distribute critical systems across decentralized networks.

Centralized clouds will always have their place for performance and scale - but they'll never match the resilience of distributed alternatives when billions of dollars are at stake and every second counts.

Philosophy doesn't compete with convenience until convenience fails catastrophically enough to change behavior.

**November 18th wasn't catastrophic enough. Neither was October 20th. Neither was July 2024.**

*How bad does it have to get before "decentralized infrastructure" stops being a talking point and becomes a requirement?*

*Crypto didn't fail on November 18th. The blockchains worked perfectly.*

**What failed was the comfortable lie everyone kept telling themselves - that you can build unstoppable applications on stoppable infrastructure, that censorship resistance matters when three companies control the roads to access it, that "decentralized" means anything when Cloudflare's config file determines whether millions can trade.**

If a blockchain produces blocks but nobody can submit transactions, did it really stay online?

There's no backup plan.

Wait for Cloudflare to fix it. Wait for AWS to restore service. Wait for Azure to deploy patches.

*That's the disaster recovery strategy.*

**Now imagine this with digital IDs.**

Treasury's pushing identity credentials into smart contracts. Mandatory KYC gates on every DeFi interaction.

When the next outage hits, you won't just lose access to trading - you'll lose access to proving you exist in the financial system.

Three hours became three hours of "verify you're human" screens that can't load because the verification service runs on infrastructure that's down.

*The guardrails regulators want to build assume the infrastructure stays up. November 18th proved that assumption wrong.*

**Tech builders pivoted to privacy when surveillance overreach became obvious.**

Maybe it's time to add infrastructure resilience to that list.

Not as a nice-to-have. As the foundational requirement that makes everything else possible.

The next outage is coming - AWS, Azure, Google Cloud, Cloudflare round two.

*Could be next month. Could be next week. Infrastructure hasn't changed. Dependencies haven't changed. Incentives haven't changed.*

**Centralized stays cheaper, faster, easier. Until it isn't.**

And when Cloudflare's next routine configuration change triggers the next hidden bug in the next critical service, we'll watch the same movie again: 500 errors everywhere, trading halted, blockchains running but unreachable, tweets about decentralization that can't get posted because Twitter's down, promises to do better that won't get kept.

Nothing will change because convenience always wins - until the day the cost of convenience becomes too obvious to ignore.

The guardian fell for three and a half hours.

**Next time might be longer. Next time might hit during a market crash when every second of trading access matters. Next time might catch identity verification systems in the crossfire.**

*When the infrastructure you didn't build fails at the moment you can't afford it to, whose fault is it really?*

REKT serves as a public platform for anonymous authors, we take no responsibility for the views or content hosted on REKT.

**donate (ETH / ERC20): [0x3C5c2F4bCeC51a36494682f91Dbc6cA7c63B514C](https://etherscan.io/address/0x3C5c2F4bCeC51a36494682f91Dbc6cA7c63B514C)**

disclaimer:

REKT is not responsible or liable in any manner for any Content posted on our Website or in connection with our Services, whether posted or caused by ANON Author of our Website, or by REKT. Although we provide rules for Anon Author conduct and postings, we do not control and are not responsible for what Anon Author post, transmit or share on our Website or Services, and are not responsible for any offensive, inappropriate, obscene, unlawful or otherwise objectionable content you may encounter on our Website or Services. REKT is not responsible for the conduct, whether online or offline, of any user of our Website or Services.
