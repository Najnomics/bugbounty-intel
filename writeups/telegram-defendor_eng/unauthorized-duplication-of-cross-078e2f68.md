# 🌉 Vulnerability in Cross-Chain Messages

- **Source URL:** https://bountyhunt3rzdeclassified.substack.com/p/unauthorized-duplication-of-cross
- **Fetched:** 2026-11-17
- **Channel:** @defendor_eng
- **Telegram message:** https://t.me/defendor_eng/239 (id 239)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# **OBSERVATIONS FROM THE BLOCKCHAIN**

Have you heard anon? The Blackhats are stalking the governance forums, running simulations on proposed changes and watching protocol deployments like vultures eyeballing their prey. Anonymous contributors and anonymous voters all participating by providing input to shape the direction of proposals, some nefarious, and some no doubt mean well, but all are ultimately incentivized to influence in a way that benefits their personal financial situation.

[Resupply](https://resupply.fi/) was hacked for $10MM after the contract digital ink barely dried on the blockchain less than 2 hours after deployment. (nice write-up by Blocksec @ [https://blocksec.com/blog/in-depth-analysis-and-reflections-on-the-resupply-protocol-attack-incident](https://blocksec.com/blog/in-depth-analysis-and-reflections-on-the-resupply-protocol-attack-incident))

Silo Finance hacked for 224 ETH ($545k) just 7 days after deployment (“testing” contract loaded with half a milly!) due to this “testing” contract not validating user-provided calldata. I understand the advantages of testing “in-prod” but how naive must you be to assume no one is watching your deployer and everything that touches anything with value attached to it?

This is MAINNET ser, not BSC!

How to use this information constructively as a Whitehat? Well, it is a fresh reminder that the contracts only tell one part of the story! One of the best places for finding fresh bugs is obviously looking at new, untested code, especially when changes are introduced to complex systems. Ask yourself: how are the new contracts being deployed? What changes are being proposed and how does that affect existing and new logic flows? Are existing storage patterns being considered? Has everything been simulated and audited?

Remember this when you have moments where you cannot find anything: you are looking for the needle in the haystack - **no one is going to pay you big bounty money for looking where everyone else is looking.**

# **WHERE'S RIPTIDE?**

Open Search Mode Activated.

I am blindly exploring on the chain, only motivated by my curiosity, which is actually a lot of fun and can be a source of incredible alpha when you think about it. If you look for patterns or bugs others have found and shared it can be a detriment since you actually narrow your field of view and will focus just on finding those bugs while missing everything else.

Instead, if you start with a blank slate, an open mind, and a strong espresso you can pick a random block and just dive in to read and understand a random transaction to find out what it does and why the user is doing it. This is a core concept of “hacking” in my view, to be just curious and follow the trail down the rabbit hole to see where it goes and how everything works. If you get too focused on the money aspect of it the “coolness factor” will wear off and you will run yourself ragged chasing tokens, likely losing interest and moving onto something else.

I hope you are enjoying your summer anon …

I am locked in for on average 5 hours each day, 7 days a week hunting for bugs.

But when the Aperol Spritz calls me, I must answer.

Suggest you do the same …

# **THE GLENGARRY LEADS**

### **Unauthorized Duplication of Cross-Chain Messages**

I am providing a raw bug report …
