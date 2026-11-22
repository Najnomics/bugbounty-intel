# Arbitrum Saved From a Bug That Could Have Led to the Loss of $540M in Ethereum

- **Source URL:** https://medium.com/@CryptoSavingExpert/arbitrum-saved-from-a-bug-that-could-have-led-to-the-loss-of-540m-in-ethereum-e6fccd4941e3?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20230202215557/https://medium.com/@CryptoSavingExpert/arbitrum-saved-from-a-bug-that-could-have-led-to-the-loss-of-540m-in-ethereum-e6fccd4941e3
- **Fetched:** 2026-11-22
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/276 (id 276)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Arbitrum Saved From a Bug That Could Have Led to the Loss of $540M in Ethereum

A white hat hacker discovered and disclosed a bug on Arbitrum’s latest upgrade, Nitro, that could have resulted in the loss of $540 million in Ethereum.

The layer-2 scaling solution Arbitrum just rewarded a white hat hacker with a bounty of 400 Ethereum (ETH) for discovering and sharing a critical vulnerability of its latest Nitro upgrade that could have resulted in the loss of $540 million in ETH.

# Arbitrum Had an Uninitialised Address Variable

[According to](/@0xriptide/hackers-in-arbitrums-inbox-ca23272641a2) the hacker, who goes by the pseudonym [@oxriptide](https://twitter.com/0xriptide) on Twitter, Arbitrum had an uninitialised address variable in its Nitro upgrade solidity code. As a hacker who hunts for bounties posted on ImmuneFi, they decided to investigate whether the variable was purposely left uninitialised or by accident.

Upon further investigations, they discovered a flaw in the bridge between Arbitrum and the Ethereum mainnet that could have led to a hacker hijacking the flow of funds between the two. A potential hacker could have replaced Arbitrum’s destination address with another of their choosing. Consequently, any funds meant to flow from Ethereum to Arbitrum would have been redirected to the added address.

@oxriptide further explained that a malicious hacker could have decided to be selective in picking transactions to divert to their address to avoid detection. Alternatively, a hacker could have chosen to drain all the incoming funds.

# The Bug Could Have Cose Arbitrum $540 Million in Ethereum.

The vulnerability was live for almost three weeks, and @oxtriptide had noted that the single largest deposit to Arbitrum was 168k ETH, estimated to be worth $229 million using Ethereum’s current value of $1,366.

In addition, [an estimated](https://dune.com/gm365/L2) 400,000 ETH worth $540 million moved between Ethereum and Arbitrum when the bug was live. Luckily, no other individual had detected the vulnerability and decided to exploit it.

# Was 400 ETH Too Small of a Bounty?

However, the crypto Twitter community has pointed out that 400 ETH or roughly $546,000, was perhaps too small of a bounty given that @oxriptide saved Arbitrum from losses that were 1,000 times larger.

One such user, [@BowTiedIguana](https://twitter.com/BowTiedIguana/status/1572633705885372417), told @oxriptide that they ‘got short-changed.’ They believed the bounty paid out could have been at least $2 million since the exploit could have resulted in a direct loss of $20 million.

\~ By John P. Njui \~
