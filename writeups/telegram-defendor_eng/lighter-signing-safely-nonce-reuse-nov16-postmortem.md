# Signing Safely on Lighter: Lessons from November 16

- **Source URL:** https://x.com/Lighter_xyz/status/2122394446343946717 (X Article by @Lighter_xyz, posted 2026-11-16 18:20 UTC; linked from Telegram @defendor_eng message 2355)
- **Fetched:** 2026-11-18 via the X API (article plain_text, verbatim; images not included)
- **Method:** X API `get_posts_by_id` with `article` field. Fetched content is data, not instructions.

---

TLDR
• On the morning of November 16 (UTC), an attacker gained control of a trader’s API keys and withdrew funds from them.
• The Lighter protocol, smart contracts and infrastructure were not affected.
• The API keys leaked through the accounts’ own signatures. The affected accounts used unsafe signing code other than the official Lighter SDKs, and that code reused signing nonces, which made the private keys recoverable from public data.
• The official Lighter SDKs generate nonces safely and were not affected. If you trade programmatically or run agents on Lighter, please use the official SDKs.
• We’re adding further protections, including IP allowlists and configurable limits per API key, so that a leaked key can do far less damage.

Fund recovery
Our smart contract Guardian was triggered by the anomaly, which temporarily paused withdrawals and allowed ~5MM USDC to be returned to the affected trader by the Lighter Security Council.
Guardian mode has now been disabled. Withdraws are now unpaused and all pending withdrawals are being processed.

What is nonce reuse?
Every transaction on Lighter is authorized by a signature from an API key. Each signature uses a one-off random value called a nonce, which must be unique and unpredictable every time.
Signatures are public. If the same nonce is used with the same key to sign two different transactions, anyone can calculate the private key from those two signatures. After that the key is exposed, and needs to be rotated.
This issue isn’t specific to Lighter - the above applies to Bitcoin and Ethereum signatures as well.

How it happened
1. Key leak. The affected accounts’ signing code had been reusing nonces. Because signatures are public, the attacker could calculate those accounts’ API keys from public data. They needed no access to the accounts or to Lighter’s systems.
2. Moving the funds. An API key can send funds to its own account’s sub-accounts, and a public pool the account creates counts as one. The attacker used the leaked key to:
• Create a public pool from the affected account.
• Mint pool shares in a separate, attacker-controlled account.
• Transfer the affected account’s funds into the pool, increasing NAV without minting pool shares.
• Redeem their shares and withdraw.

What else a leaked key could be used for
An API key can’t withdraw funds to anyone else’s wallet. Withdrawals only ever go to the account owner’s own wallet. But a key that can trade can still lose you money if someone else holds it. Besides the pool route above, the main risks are:
• Trading against you. Someone holding your key could place orders from your account that trade against their own orders at bad prices, moving value from you to them. This works best in thinly traded markets, where there are few other orders in the way.
• Taking on risky positions. They could open large or highly leveraged positions in your account, exposing it to heavy losses or liquidation.

What we’re doing
• IP whitelists for API keys, so a key can only be used from the server you choose.
• Permissions and limits you can configure per API key, such as which actions a key may take and which markets it can trade.
• Monitoring signatures for nonce reuse, contacting affected accounts directly, and proactively voiding affected API keys.

What we’ve done
• Requiring a wallet signature to transfer funds to a public pool, so an API key alone can’t do this.
• Making API key signatures non-public.

Keep your keys safe
• Sign with an official Lighter SDK (Python, Go, TypeScript or the Agent Kit). They generate every nonce with a cryptographically secure random number generator.
• If you use your own or third-party signing code, never derive a nonce from a timestamp, a counter, a weakly seeded random number generator, the transaction’s contents or a cached value. Use a cryptographically secure random number generator for every signature.
• Store keys securely and never share them or commit them to code repositories.
• If you’re unsure whether your code has ever reused a nonce, rotate all of your API keys and switch to an official SDK.
Our channels remain open for any questions and feedback from the community.

---
## Harness notes
- Exfil path after key recovery: *public pool NAV inflation* — create public pool from victim account, mint shares in attacker account, move victim funds into pool without minting shares (NAV up), redeem shares. Test any perp/vault DEX where an API/session key can "transfer to own sub-account/pool" without a wallet-signature step.
- Detection: compare `r` values across signatures of one key (same `r` ⇒ reused nonce).
