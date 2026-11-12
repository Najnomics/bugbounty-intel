# 🛡️ Off-Chain Security in Ethereum: Key Takeaways from 1TS at Devconnect

- **Source URL:** https://blog.theredguild.org/off-chain-layer-champions-at-on-initiative-conference-devconnect-argentina
- **Fetched:** 2026-11-12
- **Channel:** @defendor_eng
- **Telegram message:** https://t.me/defendor_eng/991 (id 991)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
In our previous article, we briefly mentioned participating in the **Trillion Dollar Security** gathering at **Devconnect**. In this article, we delve deeper into its importance, our key role there, and insights from our involvement.

"Trillion Dollar Security" at **Secureum TrustX** was a one-day technical event dedicated to the Ethereum Security Ecosystem, held on November 22, 2025, at La Rural in Buenos Aires, Argentina. This was part of the Devconnect week, but independently hosted by Secureum.

Trillion Dollar Security (1TS) is an ecosystem-wide effort to upgrade Ethereum's security, spearheaded by EF. Reaching “Trillion Dollar security” means a world where:

1. Billions of individuals are comfortable storing more than $1000 on-chain, collectively securing trillions of dollars on Ethereum.
2. Companies, institutions, or governments are comfortable storing more than 1 trillion dollars of value inside a single contract or application.

The broad goals were:

1. Evaluating the security landscape across every layer of Ethereum’s technology stack to identify and communicate current status, gaps, challenges, opportunities, and priorities
2. Enabling execution of short-term priorities by working rapidly and closely with the ecosystem
3. Enhancing long-term security posture via ecosystem engagement and empowerment

The event consisted of Roundtable Discussions (Invite-only) and Report-out Presentations (Open to all Devconnect attendees). The invitation was extended to Ethereum Security Ecosystem projects across 13 layers: Layer One, Layer Two, Interop, Wallet, Infrastructure, Onchain, Offchain, Monitoring, Response, Enterprise, Protocol, Privacy, and Social.

Here are a few articles in case you want to understand a bit better the context we had for the day:

- [https://blog.ethereum.org/2025/05/14/trillion-dollar-security](https://blog.ethereum.org/2025/05/14/trillion-dollar-security)
- [https://blog.ethereum.org/2025/08/20/trillion-dollar-sec-2](https://blog.ethereum.org/2025/08/20/trillion-dollar-sec-2)
- [https://ethereum.org/trillion-dollar-security](https://ethereum.org/trillion-dollar-security/)

## Off-chain security champions

We received an invitation for all the work we've done across different layers. However, we only led the off-chain layer, with support from peers such as Pablo from **Opsek** and Patrick from **Cyfrin**, whom we invited to merge, given the Social layer had little to no participants.

The organization had doubled the seats for the off-chain layer, expecting it to be one of the most popular layers, but we barely managed to fill half the space after merging. I do not think this is because there was no interest; after all, there was an obvious overlap with the **Wallet** and **Infrastructure** layers, for example.

Invited "Layer Champions" are expected to present highlights, lead/moderate their layer discussions+writeups and final presentations.

**As champions**, our objective was to serve as a moderator. We have extensive experience coordinating breakout sessions. If there's something we've learnt, it's not that it is difficult to gather people to discuss, but how to make something valuable out of it, allowing for insightful and constructive conversations.

We were given a template to follow, based on a few simple questions, such as: *What is working well, what is not, and why? How do we solve these challenges, and who should solve them?*

## Insights from the gathering

We were supposed to start at 10 AM, so after my daily *oatmeal berry matcha latte*, I headed to the venue with the last batch of the OpSec whil traveling guides so I could share it with some of the most influential security folks. This was as per the agreement with the organization, and in case attendees did not have the chance to grab one on another occasion.

I arrived early, so around 9.45, I had already handed out the books and drafted some initial notes on the whiteboard I was assigned to. The whiteboard read similarly to what I've left below.

##### **Top 10 defi attacks by risk — Blockthreat**

1\. Multisig Hijacking — $1,500,000,000 (3)

2. Stolen Private Keys — $124,000,000 (32)

...

9. Malicious insider — $53,000,000 (6)

##### **Top 911 ticket categories — SEAL**

**1. Infostealers**: devices and seeds compromised through the download of malware during Zoom calls, fake crypto games, malicious GH repos, fake devconnect invites, etc

**2. Standard phishing**: campaigns from drainers such as AngelFerno, Eleven Drainer

**3. Social Engineering**: fake CEX support (Binance, Coinbase, Kraken, etc)

**4. Sha Zhu Pan**: fake investment schemes, fake law companies "helping victims", fake recoveries

## Our first go at it

Something funny that happened while trying to answer the first question was that ***it was hard as hell***. How can a group of specialists in finding what's wrong focus on what's right? It's not that we cannot recognize good things happening, but our neurological pathways are mostly used to travel in the opposite direction — or that's the silliest excuse I could find to justify myself.

How often DO YOU stop to think and analyze all the things that have been working well?

At the moment of this writing, we've had +10 years of uptime, and building in L1 can become a reality again, with 12 cents for a USDC transfer and less than 5 cents for a native transfer.

### What is working well and why?

After a lot of debate and feeling overly insecure to mention anything in particular, I came up with the idea of saying things that, in concept, look great but that we might be failing to execute correctly.

This was also obvious to suggest after Pablo stated, "Some technologies work exactly as expected, even when there's an incident."

We all agreed that the **<u>concept</u>** of security councils and the use of technologies like **hardware wallets** and **multisigs** to secure transactions are a **significant step toward** a better future. Regardless of situations such as the Bybit exploit, the **technologies worked as expected.** Issues arise when situations like blind signing appear.  To date, no security council using different signers via a multisig with experienced members has been breached — or at least that we know of.

Because of this, the group concluded **the problem is in the implementation:** the lack of experienced, trained folks on councils, sitting on top of a multi-million-dollar treasury, who sign whatever the rest of the rest signed without checking the calldata because they were at a bachelor party.

The conversation drifted into the classic theoretical rabbit hole of collateral concentration. Someone raised the scenario of a major issuer, like USDT, shifting liquidity away from **Ethereum**. The point is not that "DeFi would break" in a Hollywood sense. The real issue is "systemic liquidity contraction". A huge amount of routing, lending, and collateral logic implicitly assumes that deep USDT liquidity is present on mainnet. Pull that out, and you trigger a chain of second-order effects: oracle instability, liquidation spikes, broken arbitrage paths, and a painful repricing across AMMs and lending markets.

The lesson is the same as before. The fragility doesn’t come from the technology. It comes from how we build on top of it, the assumptions we lock in, and the operational decisions made by humans.

All those theoretical rabbit holes faded once we talked them through. **What stood out was the strength of the coordination layer and the core values shared by the people actually building Ethereum.** The tech matters, but the shared norms and the ecosystem's alignment matter just as much.

Speaking about shared norms, exposing criminals and pursuing them, freezing and recovering funds, are some of the tasks that organizations are actively executing. Thanks to this, we're creating a less attractive landscape for threat actors, thus reducing their incentive.

**Hardware wallets** came up again. The shared view was simple. The devices **are mature enough** that attackers don’t bother going after firmware or supply-chain compromises. That path is expensive and slow. **It’s easier to poison the user**. Blind signing, malware on the host machine, UI spoofing that shows one thing while the actual calldata says another. That’s where the real action is.

When the complex parts get solid, the weak links stand out. It becomes clearer where attackers shift their focus. With current threat intel and TTPs, we can almost see the frustration. They can’t beat the hardware, so they go after the humans around it. Still the weakest link of the chain?

### My personal highlights

I left this phase of the session having validated some of my perceptions: **there are strong community values and a genuine interest in the technology**, regardless of the token price.

We briefly discussed how we are going to convince the rest of the world to participate in this. If we cannot prove that this can be a safe place, how can we confidently onboard users? There's a clear need to understand the current needs and pain points to be able to reach a more mature state in terms of security.

There’s also something about realizing how wild this ecosystem is, **web2 until not long ago, avoided post-mortems**, and <u>here we embrace them!</u> Making audit reports public and creating standards, frameworks, and tools for free, which is atypical in other fields.

### **What is working wrong and why?**

A lot...? 😅

Most of the most **critical work** that directly impacts the whole ecosystem positively is being done by **non-profits.** Unfortunately, there’s **no economic alignment** to help these lone wolves become **sustainable** in the long term. As a consequence, there's **little to no motivation to continue doing public good**.

Despite feeling SUPER identified with that point, I was still pretty surprised to have an entire table agree with our struggles. I saw a glimpse of the same when we were curating Ethereum Rangers' applications and reading each submission.

**There's a lot of false sense of security** because we stamp ‘security’ solutions on top of products without really understanding how to use them. That applies to technologies in general! A clear example, which, personally, was an eye-opener to me, was realizing after Shalai Hulud's worm that many devs did not really understand how npm dependency pinning worked. Our latest research on [devcontainers, VSCode-like IDEs](https://blog.theredguild.org/leveraging-vscode-internals-to-escape-containers/), and Adversarial Intelligence is another example of how ignorant we are about the technologies we interact with daily. And I am no exception to this!

There are **no security-experienced folks in most organizations**. Even if we create initiatives that showcase best practices, unless someone is dedicated to implementing them, it’s not feasible.

There is **no public pressure** or **accountability for crypto companies regarding web2 vulnerabilities**. The community does not care about DNS hijacks—only that the smart contracts are safe. But off-chain is just as crucial as web3. The community needs to care just as much about smart contract audits as about off-chain audits. This reminds me of a talk we selected at Ekoparty #pwndemic that focused on the impact on stock prices after incidents (breaches, leaks, compromises) in several companies. Spoiler alert: if they were impacted, it was briefly, and stock prices always recovered—a lot to unpack from that.

Today, **we cannot run nodes with Tor for** many reasons. There's a mismatch in how they both operate that makes it currently impossible for them to work together correctly.

- Traffic fingerprinting is trivial; Ethereum's P2p protocol leaks patterns through message size, ordering, and timing.
- Tor hides IPs but does not hide protocol fingerprints. We need to understand how to obfuscate requests so we can use such technologies.
- Governments only need metadata; just by running timing analysis and checking request sizes, they can understand what’s being done.
- How Nym functions as a mix-net of package requests, particularly heavily based on blockchain, makes it super interesting to explore—also, projects like Snowstorm.

**We lack mechanisms to incentivize** organizations and individuals who focus solely on providing security as a public good—oh, hi there ^^.

Something that was quite a surprise to me was when sharing experiences with other security researchers in the field, the first time I was introducing myself to Ethereum, hearing them speak only about Solidity-related topics only... no red teaming, malware reverse, opsec, devsecops... **Most security researchers or auditor profiles are not web2 experienced**. Security in web3 is mainly focused on decentralized technologies, mainly on-chain. Onboarding is always done on-chain. Also, **people over exaggerate the complexity of web3 security.**  People over-emphasize their expertise, knowing just one thing.

**The current differentiation between Web2 and Web3 does more harm than good**. I've said this many, many times. Except for when we’re speaking about moving from read/write to own and decentralization.

Many **compromises are being made in order to satisfy people**… organizations have pivoted from decentralized, permissionless, privacy-compliant solutions to centralized, permission-based, and non-privacy-compliant solutions...all this to satisfy users' needs in terms of wanting fast and easy-to-use technologies.

**Products leak a lot of user information.** Don't get me started on wallets... I will defer to our friends at Coinspect, who have run thorough analyses of all of them, finding unbelievable things, like Google Tag Manager being a single source of failures, since it's injected into most of them, for example.

And then, something that's just the current state of affairs: there's too great a **technological gap between consumers and products. Same for technical profiles, still l**ots of **ignorance or deep understanding** of the tools we’re using.

### How do we solve these challenges?!

I wish I knew a one-liner to impress you tbh.

Here are some bullets on the things we found worth exploring.

- As mentioned earlier, in the case of nodes not being able to run through **Tor**, we’ll need to think of how **technologies like Nym** or **Snowstorm** can be an advantage and/or if there's anything we could learn from them.
- We need to raise **awareness** of the number of **hostile environments** and **attacks** we’re constantly exposed to, particularly directed at developers.
- We need to push forward with initiatives such as SEAL's **Security Frameworks** and **Certifications,** which take a **proactive stance in educating** and providing resources to counteract these issues.
- The idea of relying on approaches like Certifications to generate individual certs for folks to prove they really do know security popped up at some point. Particularly when hiring.
- **Offloading the responsibility to users as little as possible.** In other words, loading the responsibility to product creators as much as possible. This should be a movement, not just an objective.
- We need **more cypherpunk propaganda**! Yes!
- Most of the **issues** we **discussed** are **not** just **web3**-specific, but **IT-specific** in general, and these speak to their current state of awareness.
- We should be actively advocating for **Opsec** and **privacy topics** to be incorporated into **education**. We’ve reached a point in time where **we cannot deny** that this is **relevant enough** to be introduced into the **educational system**. Schools, colleges/universities, even families!
- If we were to **address this and find applicable solutions from the root,** maybe we’re tackling something **bigger than us.** What would we do? Literally, try to <u>create a movement in education from the early stages of childhood?</u>

### Who could solve this and how?

The layer concluded very succinctly: A **synergy** must be created between **private** companies and **non-profit** organizations, as well as between organizations/initiatives focused strictly on **education**.

### Next Steps (what needs to be done?)

We need to continue exploring programs such as Ethereum Rangers, taking our pilot's experiences, and moving forward.

The need for larger actors to come to the rescue, coordinating joint efforts to create Security Funds, offloading the responsibilities of impact teams that need to focus on delivering outputs rather than reinventing business models that do not work, as a consequence of the characteristics of their work.

Private companies are hesitant to contribute money directly, so we need to explore different dynamics that are more suitable without the need for bureaucratic processes, and also provide clout while making an impact. Here's my personal take and ones that we were and will continue to explore at The Red Guild:

1. **Assigning public goods hours to your employees**: You don't need to leave your organization to deliver an impact. Similar to those organizations that allow employees to work a day a week on a pet project, you could assign hours to start fostering public-good projects within your organization.
2. **Assigning human power to public good organizations:** You don't need to start something from scratch; there are already impactful organizations, such as the [**World Ethical Data Foundation**](https://worldethicaldata.org/), the [**Security Alliance**](https://securityalliance.org), and [**The Red Guild**](https://theredguild.org) that could use a hand or two (or maybe twelve... thousand? haha). There's no need to contribute money directly when you can lend us an employee a few hours a week.

## Final thoughts

### The stakes have shifted.

We have **moved from speculative mechanisms and abstractions straight into the civic layer**: identity, verification, privacy; the machinery determining who is legible, to whom, and under what terms.

**With this shift, failure modes shift as well**. It's no longer just drained treasuries or protocol embarrassment; it's just **structural harm** that propagates directly through institutions and **into people's actual lives**.

Suppose Ethereum presents itself as a legitimate candidate for infrastructure, which, for me, it already is, meaning governments, civil society, and ordinary users will eventually depend on it. In that case, security 100% has to precede the ambition. **Security isn’t just some service industry here or aesthetic; it’s the prerequisite for having any moral right to build at this layer at all.** Web2 has shown us exactly what happens when these concerns are treated as optional, or worse.

Speaking with John Marshall, one thing that hit us in Buenos Aires, which he expresses much better than I, was **how much of the work we’re doing already touches questions that are basically constitutional**. Who gets recognized, who gets represented, who has agency, who has any recourse when things break. These aren’t “features”. They’re the foundations. **Once you step into that territory, respecting the architecture and the people who depend on it becomes non-negotiable.** That becomes the actual job. And that respect is part of security, whether we admit it or not.

### The ecosystem keeps trading core principles for convenience.

How much are we willing to sacrifice to build things faster and easier?

What began as a push for decentralized, permissionless, privacy-respecting systems has drifted toward centralized, permissioned, data-hungry platforms. All of it justified by the need to satisfy users who demand speed and simplicity above everything else.

### The cost of building what no one can monetize.

Most of the work that actually keeps this ecosystem alive is done by people who aren’t optimizing for revenue. Public-good teams operate in a world built for profit, yet they’re the ones taking on the most complex, least glamorous problems. The irony is brutal. The more value they create for everyone else, the harder it is for them to sustain themselves. But without them, none of this moves forward.

Approaching the end of the event, I finished our presentation with a phrase that felt cool, since we're always speaking that security is a business:

We will only **succeed** if security is **no longer a business.** So let's **destroy** the industry.

I want to clarify that I will not die down that hill; I just wanted a dramatic effect to counteract the fact that I had no time to prepare to present the slides 😄.

Thanks for reading this recap!

*When you are losing a game that you cannot afford to lose, change the rules. The central rule today has been to have a shield for every arrow. But you can't carry enough shields and you can run faster with fewer anyhow.*
