# 🛡️ Ethereum EIP-7702: Risks and Vulnerabilities

- **Source URL:** https://blog.theredguild.org/deep-dive-into-ethereum-eip-7702-smart-accounts-security-risks-footguns-and-testing
- **Fetched:** 2026-11-12
- **Channel:** @defendor_eng
- **Telegram message:** https://t.me/defendor_eng/377 (id 377)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
We’ve spent weeks hacking through Ethereum’s [EIP-7702](https://eips.ethereum.org/EIPS/eip-7702) proposal—a upgrade that will allow regular accounts (EOAs) act as smart contracts. Its goal? To unlock features like gasless transactions, batch operations, role-based permissions, and a big etc. But there's a catch.

Just kidding. There are many.

This EIP is rolling out soon, and while you're all pumped about the brightest of futures for programmable accounts, we decided to show the real deal. After a weeks-long rabbit-hole, today we're out with **a gift for you**:

**A +1 hour video on 7702 accounts: security risks, footguns and a loooot of testing broken smart account code.**

Throughout several implementations that increase in complexity, we cover issues with **access controls, signature-based authorizations, constructors, initialization patterns, inheritance, upgrades, and more.**

**Code and tests are all open-source in our new 7702 GOAT repository:**

During the video we also share a [**blind spot in Foundry**](https://github.com/foundry-rs/foundry/issues/9800) when using 7702 accounts, as well as **an** [**issue we reported in a public testnet**](https://github.com/ithacaxyz/odyssey/issues/137).

But that's not enough. On top of all of that broken code, we **highlight promising implementations of 7702 smart accounts**. And close with a **walkthrough of 7702 in** [**go-ethereum**](https://github.com/ethereum/go-ethereum/).

Enjoy, like and share!
