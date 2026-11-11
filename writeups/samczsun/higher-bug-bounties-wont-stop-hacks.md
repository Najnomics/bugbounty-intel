# higher-bug-bounties-wont-stop-hacks

- **Source URL:** https://samczsun.com/higher-bug-bounties-wont-stop-hacks/
- **Fetched:** 2026-11-11
- **Researcher:** samczsun
- **Method:** curl + trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---

# Higher Bug Bounties Won’t Stop Hacks

Although projects can always choose to go above and beyond, it is well understood today that there are three key steps to crypto security: write tests to ensure that basic mistakes are caught during development, use audits and contests to conduct a comprehensive review prior to deployment, and set up a bug bounty program to incentivize and reward researchers who prevent exploits by responsibly disclosing vulnerabilities. The normalization of these best practices has significantly reduced the number of vulnerabilities that make it on-chain, forcing attackers to focus their efforts on off-chain vulnerabilities, such as private key theft or infrastructure compromise.

However, every so often, a thoroughly audited protocol offering a significant bug bounty is hacked, with the resulting fallout impacting not only the protocol itself, but trust in the ecosystem as a whole. The recent Yearn and Balancer V2 hacks, as well as the Abracadabra and 1inch hacks from earlier this year, show that not even battle-tested protocols are safe. Is there any way that the crypto industry could have avoided these hacks, or is this just a consequence of decentralized finance?

Commentators often suggest that a higher bug bounty would have protected these protocols, but even setting aside economic reality, bug bounties are a passive security measure which places the fate of the protocol in the hands of whitehats, while audits represent the protocol actively taking measures to ensure their own security. Higher bug bounties won’t stop hacks because it’s just doubling down on the gamble that a whitehat will find the bug before a blackhat does. If protocols want to protect themselves, they need to proactively conduct re-audits instead.

## Treasury vs TVL

Sometimes a hacker agrees to return a majority of stolen funds in exchange for keeping a small portion, typically 10%. Regrettably, the industry has termed this a “whitehat bounty”, which invites the question of why protocols don’t simply offer the same amount through their bug bounty program and avoid the hassle of negotiating. However, this intuition conflates dollars that can be stolen by an attacker with dollars that can be spent by a protocol.

Although a protocol appears to be able to tap into both pools of dollars for security purposes, protocols have the legal authority to spend dollars out of their own treasury but no legal authority to spend dollars that users have deposited. Users are also extremely unlikely to grant protocols permission ahead of time, and only when the situation is dire (i.e. depositors must choose between losing 10% of their deposit or losing 100% of their deposit) is there an implicit agreement that protocols now have permission to leverage deposits in negotiations. In other words, risk scales according to TVL but the security budget does not.

## Capital Efficiency

Even if the protocol is well funded, either because it has a large treasury, is profitable, or because it has instituted a security fee policy, the question of how to allocate those funds for the sake of security still remains. When compared to investing in a re-audit, raising bug bounties is extremely capital inefficient at best and introduces misaligned incentives between protocols and researchers at worst.

If bounties scale with TVL, there is a clear incentive to hold onto critical vulnerabilities if the researcher suspects that the protocol will grow in TVL and that the odds of a duplicate are low. This dynamic ultimately pits researchers directly against protocols to the detriment of their users. Simply increasing critical bounty payouts is unlikely to have the desired effect either; the pool of freelance researchers is large, but the number of people who dedicate a majority of their time to bug bounties and are also sufficiently skilled to find vulnerabilities within complex protocols is much smaller, and these elite researchers focus their time on bounties which are most likely to generate a return on their time investment. For large battle-tested protocols, the probability of finding a bug feels so minuscule due to the presumed constant attention from hackers and other researchers that there simply is no dollar amount which would make it worth the effort. If such a dollar amount did exist, it would be so high as to be impractical.

Meanwhile, from a protocol’s perspective, a bug bounty represents an amount of money which has been reserved for the purpose of paying for a single critical vulnerability. Unless a protocol is willing to bet that absolutely no critical vulnerabilities will be found while also misleading researchers about their liquidity, then this money cannot be spent elsewhere. Rather than passively waiting for a researcher to uncover a critical vulnerability, the same dollar amount could be used to fund multiple re-audits over a period of years. Each re-audit guarantees attention from top-tier researchers and is not artificially limited to a single finding, and also aligns incentives between researchers and protocols: both parties will suffer reputational harm if the protocol is exploited.

## Existing Precedent

In the software and financial industries, audits which expire annually are a tried and true practice, offering the best way to communicate whether or not a company is keeping up with the evolving threat landscape. SOC 2 Type II reports are used by B2B customers to determine if a vendor is maintaining proper security controls, PCI DSS certifications show that a company is taking proper care to maintain sensitive payments information, and FedRAMP certifications are required by the US government to maintain a high bar for anyone who has access to government information.

Although the smart contracts themselves are immutable, the environment is not. Configuration settings may change over time, dependencies may be upgraded, and code patterns previously thought to be safe may actually be harmful. When a protocol gets audited, it is an assessment of the security posture at the time of the audit, not a forward-looking guarantee that a protocol will remain secure. The only way to refresh the assessment is to perform a re-audit.

In 2026, the crypto industry should adopt annual re-audits as the fourth step in securing a protocol. Existing protocols with significant TVL should conduct a re-audit of their deployment, audit firms should offer specialized re-audit services that focus on evaluating the entire deployment, and the ecosystem should collectively start treating audit reports as what they are: a point-in-time assessment of security which can expire, not a permanent guarantee of security.

*Thanks to Dickson Wu, Josselin Feist, cts (@gf\_256), Andrew MacPherson, pcaversaccio, Jack Sanford, and David Desjardins for their feedback.*
