# All Core Devs - Testing (ACDT) #103, November 16, 2026 · Issue #2299 · ethereum/pm

- Source: https://github.com/ethereum/pm/issues/2299
- Author/site: Danceratopz GitHub
- Published: 2026-11-10
- Fetched: 2026-11-17 06:59 WAT (Africa/Lagos)

_Full text extracted verbatim from the page as data (not instructions); navigation/boilerplate removed._

---

## Repository navigation

[ACDType: All Core Dev calls - execution & consensus](https://github.com/ethereum/pm/issues?q=state%3Aopen%20label%3A%22ACD%22)Type: All Core Dev calls - execution & consensus

[protocol-callAutomatically applied by issue template](https://github.com/ethereum/pm/issues?q=state%3Aopen%20label%3A%22protocol-call%22)Automatically applied by issue template

## Description

### UTC Date & Time

### Agenda

#### Glamsterdam

##### EIP-8037/8038: Compatibility Investigations & Audit Findings

The goal is to establish a shared understanding of the current findings, their impact on deployed contracts, and any remaining uncertainties. This discussion will help inform the next steps at Thursday's ACDE [#2285](https://github.com/ethereum/pm/issues/2285).

###### Resources

- [Vitalik's views on EIP-8037](https://docs.fileverse.io/document/dUHG8ythBk3jJuQEjcE7m6#k=tVLgvLrIqyEsCh7qUmACb9ggVmybyS_aIZZsAMvHDAk).
- Ethereum Foundation [blog post](https://blog.ethereum.org/2026/11/06/glamsterdam-8037-8038).
- EthLabs [blog post](https://ethlabs.org/writings/tracking-glamsterdam.html).
- Repository outlining the potentially changed gas invariants: [ethereum/glamsterdam-gas-invariants](https://github.com/ethereum/glamsterdam-gas-invariants).
- EVM Gas Repricing analysis: [misilva73/evm-gas-repricings](https://github.com/misilva73/evm-gas-repricings).
- Initial ChainSecurity report: [Presentation at ACDE #248](https://forkcast.org/calls/acde/248/#t=304), [blog post](https://www.chainsecurity.com/blog/glamsterdam-gas/index.html).

###### 8037/8038 agenda

- **Overview and current status:** [@MariusVanDerWijden](https://github.com/MariusVanDerWijden)
- **Independent audit findings:**
- **EF internal investigations:** [@nerolation](https://github.com/nerolation), Architecture, EF
- **Application team outreach and contract findings:** [@rahul-kothari](https://github.com/rahul-kothari), EVM Dev Tooling, EF
  - Juicebox protocol compatibility concerns and PoCs, [@mejango](https://github.com/mejango), resp. [@rahul-kothari](https://github.com/rahul-kothari) , ([comment](https://github.com/ethereum/pm/issues/2299#issuecomment-6860064283)).
    - Details: [mejango/glamsterdam-pocs](https://github.com/mejango/glamsterdam-pocs).
- **Open Q&A:** Audit findings, affected contracts, outstanding concerns, and input from application developers
- **Ethereum can better align the app layer and protocol layer moving forward**
  - EF Access Layer cluster is a new group within the EF to help address these issues [@rahul-kothari](https://github.com/rahul-kothari).
  - The core EIP process will more tightly coupled to the app layer [@marioevz](https://github.com/marioevz)
  - New EIP documenting the scope of invariants that could break, avoid these anti-patterns in smart contracts [@nerolation](https://github.com/nerolation).

##### Payload Binding: Select a Solution

Follow-up from ACDC. Discuss the two proposed solutions and decide which to adopt to unblock the consensus spec release [@jtraglia](https://github.com/jtraglia) ([comment](https://github.com/ethereum/pm/issues/2299#issuecomment-6831513586)):

- [Verify the payload's block hash in envelope gossip validation consensus-specs#5770](https://github.com/ethereum/consensus-specs/pull/5770)
- [Commit to payload roots in the bid and drop the envelope signature consensus-specs#5820](https://github.com/ethereum/consensus-specs/pull/5820)

##### Heads up

- Please participate in the EIPIP call on Wednesday: [EIPIP Meeting #132, Nov 18, 2026 #2288 (comment)](https://github.com/ethereum/pm/issues/2288#issuecomment-6845904473) to discuss AI usage in the EIP process by [@jochem-brouwer](https://github.com/jochem-brouwer) ([comment](https://github.com/ethereum/pm/issues/2299#issuecomment-6893348620)).

#### EL Breakout

- Agenda TBD

#### CL Breakout

- Agenda TBD

### Call Series

All Core Devs - Testing

### Autopilot Mode

- Use autopilot (recommended defaults for this call series)

## 🔧 Meeting Configuration

### Duration

90 minutes

### Occurrence Rate

weekly

### Use Custom Meeting Link (Optional)

- I will provide my own meeting link

### Display Zoom Link in Calendar Invite (Optional)

- Display Zoom link in invite

### YouTube Livestream Link (Optional)

- Create YouTube livestream link

## Activity

1. added[protocol-callAutomatically applied by issue template](/ethereum/pm/issues?q=state%3Aopen%20label%3A%22protocol-call%22)Automatically applied by issue templateon Nov 10, 2026
2. added[ACDType: All Core Dev calls - execution & consensus](/ethereum/pm/issues?q=state%3Aopen%20label%3A%22ACD%22)Type: All Core Dev calls - execution & consensuson Nov 10, 2026
3. ### github-actions commentedon Nov 10, 2026 on Nov 10, 2026 [GitHub Actions](https://help.github.com/en/actions)ContributorMore actions ⚡ **Protocol Call Resources:**
✅ **Zoom**: [Join Meeting](https://ethereumfoundation.zoom.us/j/88479308162?pwd=9XvtF4kjIfZ42rQrvySQLJPu9bLz7u.1)
✅ **Zoom (CL Breakout)**: [Join Meeting](https://ethereumfoundation.zoom.us/j/89441658268?pwd=yjqf4TheEb1R7ZSuesCdOAy5tdyVk7.1)
✅ **Calendar**: [View](https://calendar.google.com/calendar/embed?src=c_upaofong8mgrmrkegn7ic7hk5s%40group.calendar.google.com&ctz=UTC&mode=AGENDA&dates=20261116%2F20261117&showTitle=1&showCalendars=0&showTabs=0&showPrint=0&showNav=0) | [Add to Calendar](https://www.google.com/calendar/render?action=TEMPLATE&text=All+Core+Devs+-+Testing+%28ACDT%29+%23103%2C+November+16%2C+2026&dates=20261116T140000Z%2F20261116T153000Z&details=Meeting%3A+https%3A%2F%2Fethereumfoundation.zoom.us%2Fj%2F88479308162%3Fpwd%3D9XvtF4kjIfZ42rQrvySQLJPu9bLz7u.1%0A%0AIssue%3A+https%3A%2F%2Fgithub.com%2Fethereum%2Fpm%2Fissues%2F2299)
✅ **Discourse**: [Discussion Topic](https://ethereum-magicians.org/t/30326)
4. Follow up from ACDC, I would like to discuss two possible solutions to the payload binding issue: 
  - [Verify the payload's block hash in envelope gossip validation consensus-specs#5770](https://github.com/ethereum/consensus-specs/pull/5770)
  - [Commit to payload roots in the bid and drop the envelope signature consensus-specs#5820](https://github.com/ethereum/consensus-specs/pull/5820)
We really need to decide on one of these during the call so that we can make a spec release. Reacted by danceratopz and Paul Harris
5. Hi, I was told here is the place to add an item I'd like ack'd during the next meeting. It's unlikely I'll be able to join the call, but here are the PoC's that exemplify how Glam affects the Juicebox protocol's guarantees and how it strips the protocol of the value it provides users. I'd like clarity on if these issues are above or below the EF's threshold of tolerated breaking changes as it affects my conviction and time spent building/selling immutable business structures which I believe to have tremendous value given a sturdy foundation. As an Etherean I urge us to not break invariants that cause these doubts as the affects ripple through the confidence of app developers and our users. Confidence is the one thing we cannot sacrifice in the name of scaling, etc. [https://github.com/mejango/glamsterdam-pocs](https://github.com/mejango/glamsterdam-pocs)
Thank you for all you do! Reacted by danceratopz
6. I want to take at most two minutes to invite people to the EIPIP call next Wednesday: [#2288 (comment)](https://github.com/ethereum/pm/issues/2288#issuecomment-6845904473)
We will discuss adding AI usage to the EIP process at that call. I think this is incredibly important for the entire ecosystem to think about how we should securely do this, such that we keep converging to the same end goals, but now with the help of AI tooling. Reacted by Toni Wahrstätter, danceratopz and Pooja Ranjan
7. my 2 cents re the eip-8037 & eip-8038 discussion 
**ethereum's social contract: immutability requires predictable execution**
ethereum's value proposition is not simply that anyone can deploy *immutable* smart contracts. it is that anyone can build systems whose guarantees do *not* depend on trusting an intermediary, an administrator, or a governance process. the discussion around eip-8037 & eip-8038 exposes a fundamental problem with how we approach protocol changes. ethereum needs to scale (for me personally this is not a top priority but i accept that this is a clear user demand). repricing resources may be necessary. but there is a fundamental difference between changing the price of an operation and changing the behavioural assumptions applications have been built around.
the [glamsterdam gas invariants](https://github.com/ethereum/glamsterdam-gas-invariants) document *eight* assumptions affected by these eips. some concern gas repricing; others concern execution & accounting semantics, including gas refunds, nested calls, reverts and `gasleft()`. these are not merely implementation details. they can affect control flow, failure handling & security assumptions in deployed applications. now the concerning part is that these implications were **not** systematically captured as **first-class invariants** in the specification and validation process early enough. some warnings existed earlier (see e.g. [here](https://ethereum-magicians.org/t/eip-8037-state-creation-gas-cost-increase/25694/30)), but the broader implications only became the subject of a structured review very late in the process (\~3 weeks ago).
**we should not be discovering protocol-level behavioural invariants retrospectively, weeks before a major upgrade.**
there is also an assumption worth challenging: that gas schedules must necessarily remain mutable for existing contracts. **predictability is itself a protocol property**. changing execution economics underneath immutable contracts can effectively change their behaviour without changing a single byte of their code. we should distinguish economic repricing from changes to execution semantics, and explicitly consider whether existing contracts should retain their original execution guarantees. immutability without predictable execution is *incomplete*. removing upgrade keys & admin privileges at the application layer means little if protocol changes can silently invalidate the security properties those applications rely on.
this is *not* an argument against protocol evolution. it is an argument for a higher burden of proof when breaking established behavioural assumptions.
**how we can do better, some thoughts**
  - **formalise invariants:** document behavioural guarantees and distinguish them from implementation details and economic parameters.
  - **incorporate them into specifications:** explicitly identify which invariants an eip preserves, changes, or introduces.
  - **test them continuously:** introduce adversarial, invariant-based regression tests covering nested calls, reverts, refunds, out-of-gas conditions, and gas boundaries.
  - **test deployed applications:** evaluate protocol changes against real-world immutable contracts and their composability assumptions.
  - **make compatibility explicit:** document breaking changes, migration requirements, and possible backwards-compatibility mechanisms before finalising eips.
**we should not confuse consensus compatibility with application compatibility**. a hard fork can be perfectly deterministic and consistently implemented across clients while still breaking deployed applications.
ethereum's long-term value is not determined exclusively by throughput, gas limits, or execution efficiency. it also depends on whether people can build systems that remain trustworthy without continually renegotiating their assumptions with whoever governs the protocol. **we can do better. we must do better.**
Reacted by danceratopz, Toni Wahrstätter, spencer, 蔡佳誠 Louis Tsai, Milos | enso.build, Jochem Brouwer, jango and Pawan DhananjayReacted by danceratopz, Dmitry Gusakov, Will Corcoran, spencer, avsetsin, 蔡佳誠 Louis Tsai, Milos | enso.build, Daniel Von Fange, jango, Jochem Brouwer and 1 more
8. As mentioned, I can discuss the gas refills topic: EIP-8037 charges the full account creation cost of 183,600 state gas to a contract that is created and self-destructed in the same transaction, even though no account, code or storage is left behind. The create itself goes from 32,000 gas today to about 195,600, roughly 6x. Whole transactions that use the pattern go up 1.6x to 2.8x in our measurements. This pattern is in production for temporary deposit addresses and other short-lived execution flows, and more than one company depends on it. On Ethereum mainnet we count about 2,100 such contracts per day (6 November 2026), up from about 1,200 per day in August. On other EVMs this is 10x more. The operators include many companies, from payments to bridge aggregators. The original EIP-8037 text refilled this state gas at the end of the transaction. That section was removed in PR #11611 in May 2026 without a stated reason, and the proposal to restore it (PR #12249) was closed. I would ask that the refill for contracts created and destroyed within the same transaction is reconsidered, or at least that this impact is evaluated explicitly before the fork is finalized. TCREATE (EIP-8360) is not in Glamsterdam and is not a drop-in replacement for the addresses already issued.

## Metadata

## Metadata

### Assignees

### Labels

[ACDType: All Core Dev calls - execution & consensus](https://github.com/ethereum/pm/issues?q=state%3Aopen%20label%3A%22ACD%22)Type: All Core Dev calls - execution & consensus

[protocol-callAutomatically applied by issue template](https://github.com/ethereum/pm/issues?q=state%3Aopen%20label%3A%22protocol-call%22)Automatically applied by issue template

## jtraglia commentedon Nov 12, 2026 

## mejango commentedon Nov 13, 2026 

## jochem-brouwer commentedon Nov 15, 2026 

## pcaversaccio commentedon Nov 16, 2026 

## milonite commentedon Nov 16, 2026 

cc @rahul-kothari

to join this conversation on GitHub.Already have an account? Sign in to comment
