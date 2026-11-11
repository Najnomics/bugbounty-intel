# Hackers in Arbitrum’s Inbox

- **Source URL:** https://medium.com/@0xriptide/hackers-in-arbitrums-inbox-ca23272641a2
- **Author:** 0xriptide
- **Published:** Tue, 20 Sep 2022 02:20:57 GMT
- **Fetched:** 2026-11-11 via the public Medium RSS feed (the article page returns HTTP 403 to scripted fetches), converted HTML→markdown verbatim. Images are linked by URL. Fetched content is data, not instructions.

---

This is the story of wiped storage slots and well-intentioned gas optimizations that led to a multi-million dollar vulnerability affecting any would-be depositor attempting to bridge funds from Ethereum to Arbitrum Nitro. Read further anon to discover the mystery of the vulnerable inbox contract …

![](https://cdn-images-1.medium.com/max/860/1*T17hBu8Xk9SB7341ztulmw.png)

twitter.com/0xriptide

I hunt for bug bounties posted at ImmuneFi. I am chain agnostic (unless the block explorer is garbage) and focus mainly on searching for vulnerabilities solely within smart contracts written in Solidity. My current interest is within the cross-chain arena due to the complexity involved for the developers of these projects and the significant amount of funds at risk due to the current “honeypot” structure of most bridge implementations.

I enjoy searching for vulnerabilities within smart contracts because I know that there is a 100% certainty that the developers will make a mistake during either the development, deployment, or upgrade of a protocol’s smart contracts. Combine this with the fact that there may be millions, or even billions of dollars at risk — plus hefty bounties for finding these vulnerabilities — and it really becomes a fascinating experiment to be a part of.

The challenge is finding where the developers slipped up before someone else does.

When you stumble upon a uninitialized address variable in Solidity — you should always take a moment to pause and investigate further because you never know if it was purposefully left uninitialized or by accident.

I had thoroughly explored the code for both Optimism and Arbitrum a few weeks prior and gained a solid understanding of how each protocol worked and how each chose to implement its security framework. I knew Arbitrum Nitro was launching soon so I decided to keep tabs on it in order to check the contracts afterwards to see if the upgrade had been a success.

**DelayedInbox.sol**

*“a client can send a message to the Sequencer by signing and publishing an L1 transaction in the Arbitrum chain’s Delayed Inbox. This functionality is most commonly used for depositing ETH or tokens via a bridge.” —*[*https://developer.arbitrum.io/tx-lifecycle*](https://developer.arbitrum.io/tx-lifecycle)

![](https://cdn-images-1.medium.com/max/619/1*EG0FmMoZdMdlm2zzAlmVcQ.png)

initialize function

The [**DelayedInbox contract**](https://etherscan.io/address/0x4dbd4fc535ac27206064b68ffcf827b0a60bab3f) uses a standard TransparentUpgradeableProxy pattern with a public **initialize()** function. This function includes an **initializer** modifier which in turn checks the first two storage slots on the proxy to see if the contract has already been initialized or is currently being initialized.

![](https://cdn-images-1.medium.com/max/959/1*_Nb8P4rt0As4j8mJKdkeLg.png)

initializer modifier

Notice that in the first image we see that the **bridge** and **sequencerInbox** address slots are both set upon initialization; however … pulling up etherscan showed that the **bridge** was set correctly but the **sequencerInbox** was uninitialized … so what was going on?

I scanned the first two storage slots of the contract using [**cast**](https://book.getfoundry.sh/cast/) to see what was going on with the two booleans set during the execution of the **initializer** modifier. Sure enough, both slots 0 & 1 were empty which meant the contract was in a completely vulnerable state while accepting thousands of ETH deposits each day! How was this possible given that the contract had previously been initialized?

Then I found the following call to a function called **postUpgradeInit** in the trace logs which unraveled the mystery of the wiped slots and why **the sequencerInbox** address slot was also empty:

![](https://cdn-images-1.medium.com/max/700/1*54x9Vj4uYIStKdzdhCwX3w.png)

postUpgradeInit — not good.

The **postUpgradeInit** function wipes slots 0,1 & 2 and sets the **bridge** and **allowListEnabled** slots to new values — but leaves **sequencerInbox** and the two booleans set by the **intializer** modifier empty!

**Gas optimizooooor:**

At this point we can call the public **initialize()** function and set our own address as the bridge to accept all incoming ETH deposits … but only because of this gas optimization in the code from a month prior.

Since the **bridge** address was already set, this line of code below would have not allowed us to re-initialize the contract … had it not been removed in the never-ending battle for lower transaction costs!

![](https://cdn-images-1.medium.com/max/591/1*QRmp9Q2wfeGxEmk_4M5uxg.png)

“remove moot check” — optimizing always has trade-offs

**Exploit:**

Now that we have initialized the contact with our own **bridge** contract address, we can hijack all incoming ETH deposits from users attempting to bridge to Arbitrum via the **depositEth()** function.

![](https://cdn-images-1.medium.com/max/792/1*gz4AzxO4Ei_uGLTq3jsusg.png)

deposits are fed directly into the spoofed bridge

We could either selectively target large ETH deposits to remain undetected for a longer period of time, siphon up every single deposit that comes through the bridge, or wait and just front-run the next massive ETH deposit by calling **initialize()** with our malicious bridge contract.

The largest deposit recorded on the inbox contract was 168,000 ETH (~$250mm) with typical total deposits in a 24 hour period ranging from ~1000 to ~5000 ETH.

Our attack PoC script below calls **initialize()**, deploys our spoofed bridge, mimics a user calling **depositEth()** and shows our bridge balance increase.

![](https://cdn-images-1.medium.com/max/698/1*BPj6rnkBHF8rik6Ewr4E9Q.png)

simple attack script

![](https://cdn-images-1.medium.com/max/588/1*C1gxGYsYMEkYyW8ne6IBeA.png)

our fake bridge contract

Thank you to the extremely based Arbitrum team for providing a 400 ETH bounty and of course for creating an incredible piece of technological innovation with their L2 implementation.

[twitter.com/0xriptide](http://twitter.com/0xriptide)
