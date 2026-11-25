# A one-tap token drain in Unstoppable Wallet, and the $20 bug bounty it earned

- **Source URL:** https://medium.com/@mikeystrauss/a-one-tap-token-drain-in-unstoppable-wallet-and-the-20-bug-bounty-it-earned-a6891afef3f1
- **Fetched from:** https://medium.com/@mikeystrauss/a-one-tap-token-drain-in-unstoppable-wallet-and-the-20-bug-bounty-it-earned-a6891afef3f1?source=rss-834e1f70619------2
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14948 (id 14948)
- **Method:** medium-rss-feed (full content:encoded) readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- **Author/Published (RSS):** Mikey Strauss / Wed, 14 Oct 2026 13:09:49 GMT

The short version: One tap on a real, shipping crypto wallet lets a stranger take the entire balance of one of your tokens — and everything you ever receive in it afterward. No password. No malware. Nothing more from you after that single tap. The catch is that the tap is on a screen that won’t tell you what you’re approving. The wallet’s own makers confirmed the bug, agreed the code behind it has “no legitimate use case,” and said they’d remove it. Then their bug bounty rated its severity none and paid the finder a twenty-dollar reward. Here’s how all of that is true at once.

A self-custody crypto wallet is an app that holds your keys — the secrets that control your money on a blockchain. You don’t “log in” to move funds. Instead the wallet *signs* things with your key. A signature is a cryptographic yes: proof that the key-holder approved a specific piece of data. Approve the wrong data, and you’ve authorized something you never meant to.

Wallets talk to websites through a standard called **WalletConnect**: scan a QR code, and a site can now ask your wallet to sign things. That’s normal and useful — it’s how you use a decentralized exchange (a website for swapping one token for another), a blockchain game, and so on. The wallet’s one job at that moment is to show you *what* you’re about to approve, so you can refuse anything shady. Unstoppable Wallet skips that part.

When a connected site asks Unstoppable Wallet to sign something, the app shows one generic screen. It even runs a “Scam Protection” check when you first connect:

But once you’re connected, the signing prompt tells you nothing. Harmless login or a demand for everything you own, the message field reads the same hardcoded word: Unknown.

No warning. No breakdown. Just *Unknown*, and a Confirm button — which looks like the whole problem, and isn’t. (The real one is worse, and we’ll get to it.)

Ethereum wallets support several signing methods. Most add safety rails. They scramble your message into a fixed fingerprint first, or stamp a human-readable prefix on it, so a signature meant for a login can’t be reused as a signature for a payment. One legacy method has none of those rails: eth\_sign. It does exactly one thing — take 32 raw bytes and sign them. No questions, no interpretation, no prefix. Hand it any 32 bytes and it gives back a valid signature over them.

This is dangerous enough that most modern wallets, MetaMask included, removed eth\_sign years ago or buried it behind a red warning. Unstoppable Wallet supported it, with no extra warning at all, treated exactly like every safer method — until the removal described below.

On Ethereum you can grant someone an **allowance**: permission to move some of your tokens for you. A modern shortcut called a **permit** lets you grant that permission with just a signature, no separate transaction. Grant an *unlimited* allowance and the holder can take the entire balance of that token — now, and anything you ever hold in it later.

To be signed, a permit is boiled down to a single 32-byte fingerprint (a “digest”). And an eth\_sign request is also just 32 bytes. So an attacker computes the fingerprint of an unlimited-allowance permit — entirely offline, from public information alone — and hands those 32 bytes to your wallet as an ordinary eth\_sign request. The wallet shows “Unknown.” You tap Confirm. You’ve signed a blank cheque against one of your tokens, and no token name, amount, or recipient was ever shown, because the wallet never looked at what those 32 bytes meant. (Each token an attacker wants needs its own request and its own tap; native ETH, which has no permit, is out of reach this way. One tap, one token — but a total one.)

The “Unknown” screen is the part everyone notices, but it’s a symptom, not the bug — and it’s why this was never an intended, sign-at-your-own-risk feature. Every Ethereum signature signs a single 32-byte number, and what stops a signature meant for one purpose from being reused for another is *what that number is built from*.

When you sign a message with personal\_sign, the wallet doesn’t sign your text — it signs keccak256(“\x19Ethereum Signed Message:\n” + text). That fixed prefix is a labeled envelope: the result lives in “message” space and can never equal a token approval’s number, because you can’t work backwards through a hash to find text that lands on one. eth\_signTypedData is the same idea — keccak256(“\x19\x01” + domainSeparator + struct), the exact format a permit uses — except the wallet parses the fields, so it can show you “unlimited approval to 0xATTACKER.” Either way, the safe methods make it impossible for a “sign this message” signature and a “move my tokens” signature to be the same bytes.

eth\_sign throws the envelope away. It signs the 32 bytes you hand it, exactly as they are. So the attacker computes the number that *is* a permit and hands it over. That’s why a clearer prompt can’t save it: eth\_sign is being asked to sign an opaque 32-byte number, and an opaque number is precisely what the attacker needs — there is nothing a screen could meaningfully show. The fix isn’t a better warning. It’s removing the method, which is what the vendor has since done.

It was reproduced end to end against the real, unmodified, published app — no rooted phone, no modified build — over a genuine WalletConnect session, with the same tools any real website uses. The only “attacker” code is a short script that computes the permit fingerprint offline and sends it as a standard eth\_sign request. If you’re not a coder, it does two things: build the fingerprint of an unlimited approval, then ask the wallet to sign it.

```
const digest = ethers.TypedDataEncoder.hash(domain, types, {
  owner: victimAddress,
  spender: attackerAddress,
  value: ethers.MaxUint256,   // unlimited allowance
  nonce, deadline,            // routine anti-replay bookkeeping the permit standard requires
});
```
```
const signature = await signClient.request({
  topic: session.topic,
  chainId: "eip155:1",        // just metadata in the request; the test ran on a mainnet-forked local net
  request: { method: "eth_sign", params: [victimAddress, digest] },
});
// Real result from the device: a valid signature, returned in 1941ms.
```
The phone showed the “Sign Request — Message: Unknown” screen from earlier. One tap on Confirm, and a valid signature came back. That signature was then submitted to the blockchain by the attacker — the victim does nothing — on a private, funds-free test network, calling the token’s real permit and transfer functions. Nothing simulated:

Balance before: 1,000 tokens. After: 0. Off one signature, with nothing more from the victim. And because the allowance is unlimited, that one tap keeps working: it takes anything the victim ever holds in that token afterward. The wallet doesn’t even quietly check with a fraud-detection service first — an operating-system-level look at its network traffic showed only ordinary background noise. It just signs.

The dangerous method isn’t some forgotten corner, and its origin is oddly mundane. In April 2022, a user filed a public request (a GitHub issue, [#4780](https://github.com/horizontalsystems/unstoppable-wallet-android/issues/4780)) asking Unstoppable to support a feature on **SushiSwap**, a popular decentralized exchange. At the time Sushi had a “gas refunder” — “gas” being the fee you pay to use Ethereum — that could cut those fees sharply, and it needed the wallet to support a “custom transaction signature.” Built the way it was, that meant supporting the no-questions-asked raw signer.

The next day, a code change (pull request [#4788](https://github.com/horizontalsystems/unstoppable-wallet-android/pull/4788), “Handle legacy eth\_sign WalletConnect request”) was opened and merged to satisfy it. It routed such requests straight into that raw signer — the exact eth\_sign behaviour behind this drain. No security review is referenced in the change. A [2024 cleanup](https://github.com/horizontalsystems/unstoppable-wallet-android/commit/3081d6f354ba83aedf8cad879c5bb72721c16b57) carried it into the signing code, where it stayed until it was [removed in the 0.50.0 release](https://github.com/horizontalsystems/unstoppable-wallet-android/releases/tag/0.50.1) (August 2026).

So the thing that lets a stranger empty one of your tokens with a blind tap shipped for roughly four years. It took a day to add. It was there to save fees on one exchange.

The finding went to Unstoppable Wallet’s bug bounty program, through Immunefi, with a complete, reproducible proof of concept: the exact source, a live WalletConnect session against the real app, a signature made on a real device, and an on-chain replay taking a test wallet from 1,000 tokens to zero. Over about four hours on one day, the report was:

For the record: the impact reported here — “Wallet interaction modification resulting in financial loss” — is listed in the program’s own published scope as Critical, and its two nearest categories carry the same rating. There is no lower tier for it anywhere in that scope.

The stated reason it carries “no severity” is that the user connects and approves. But look again at what the user approves: the screen from earlier, the one that reads “Unknown.” Same screen for a harmless login. Same screen for an unlimited, permanent claim on a token. And the agreed fix wasn’t to make that screen honest — it was to delete eth\_sign outright, which it now has. It’s hard to read that as anything but the vendor’s own verdict on how much the “approval” was ever worth.

The finder referred the reward decision to Immunefi’s mediation. The outcome upheld the program: the report was ruled out of scope under its social-engineering exclusion — a ground the wallet’s team had not itself raised, having argued only that the user chooses which site to connect to — and the $20 was reclassified as a discretionary payment outside mediation’s remit, closing any further dispute over the reward.

Two things make that reading hard to buy. Connecting a wallet to a dApp and approving a request is the one thing WalletConnect is for — and the program’s own scope rates “malicious transactions to an already-connected wallet” as Critical. If being connected and tapping Approve were themselves the disqualifying “social engineering,” that Critical category could never be met. And the attack doesn’t need anyone to be tricked: any dApp you’re already connected to — including a legitimate one that later gets compromised — can send the very same request. Being a connected user isn’t the attack; it’s the precondition every signing feature already has. The attack is that the wallet signs a blank cheque and calls it “Unknown.”

A four-year-old, fully reproduced way to empty one of a wallet’s tokens with a single blind tap — born from a one-day convenience change, confirmed by its own makers, and settled with a twenty-dollar bounty.
