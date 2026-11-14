# 🔍 ERC-7730 Clear Signing Makes Intent Legible, Not Honest

- **Source URL:** http://certik.com/blog/clear-signing-under-the-hood-a-technical-guide-to-erc-7730
- **Fetched from:** https://www.certik.com/blog/clear-signing-under-the-hood-a-technical-guide-to-erc-7730
- **Fetched:** 2026-11-14
- **Channel:** @defendor_eng
- **Telegram message:** https://t.me/defendor_eng/2317 (id 2317)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
ERC-7730 is a JSON specification that tells a wallet how to translate raw transaction data into a human-readable description before a user signs it. It addresses blind signing — the act of authorizing a transaction whose true effect the signer cannot see, which has been the final step in incidents such as the Bybit, WazirX, and Radiant Capital losses. The standard originated at Ledger; on May 12, 2026, stewardship of it and its registry moved to the Ethereum Foundation's Trillion Dollar Security Initiative.

The standard introduces a new kind of artifact: a file that lives alongside the contract, describes how the contract's calls should be presented to users, and can itself be incorrect in ways that affect security. This post walks through what the standard is, how it works, the best practices and security considerations around it, its limitations, and the specific attack surfaces it introduces. The perspective throughout is a security review one — the questions worth asking when a descriptor is part of what you ship.

## What is ERC-7730

ERC-7730, titled "Structured Data Clear Signing Format," is a JSON specification that tells a wallet how to translate raw transaction data into a human-readable description before a user signs it. Instead of presenting 0xa9059cbb000000000000000000000000d8da...05f5e100, a compatible wallet reads the ERC-7730 descriptor for that contract and renders something a person can actually evaluate:

*Send 100 USDT to vitalik.eth*

The key structural fact is this: ERC-7730 is a presentation layer, not a protocol change. It does not touch the EVM. It does not require a hard fork. It does not require contracts to be redeployed or even modified. The signature a wallet produces is byte-for-byte identical whether or not the wallet understands ERC-7730 — only the display changes. This is why the standard could launch with descriptors for dozens of existing protocols already in place: a contract immutably deployed in 2017 becomes clear-signable the moment someone writes a descriptor for it and publishes that descriptor to the registry.

It is worth being precise about the vocabulary, because the surrounding initiative bundles several pieces together:

- ERC-7730 is the descriptor format itself — the JSON file.
- The registry is the Ethereum-Foundation-hosted, publicly mirrorable repository where descriptors live.
- ERC-8176 is a companion standard defining attestations, so independent auditors can cryptographically vouch that a descriptor faithfully represents the contract.
- ERC-8213 is a companion standard defining bytes-level calldata digests — a fallback for the cases ERC-7730 cannot describe.

"Clear Signing" is the umbrella term for all of it. ERC-7730 is the specific format that most audit attention falls on.

## How It Works

### The shape of a descriptor

Every ERC-7730 file has three meaningful top-level sections, plus a schema pointer and an optional includes key for pulling in shared definitions. The schema pointer below uses the v2 alias, which always resolves to the newest v2 release — currently v2.1.0 — while a v3 schema is still in draft:

```
{
```
"$schema": "[https://eips.ethereum.org/assets/eip-7730/erc7730-v2.schema.json (opens in a new tab)](https://eips.ethereum.org/assets/eip-7730/erc7730-v2.schema.json)",
"context":  { /\* which contract, on which chains, this file is valid for */ },
"metadata": { /* owner name, token info, reusable constants, enums, maps */ },
"display":  { /* per-function intent and per-field formatting rules \*/ }
}

The `context` section is a set of constraints. It tells the wallet exactly which structured data this descriptor is allowed to format — typically a list of `(chainId, address)` pairs for an EVM contract, or an EIP-712 domain for a typed message. A wallet must verify these constraints before it applies any formatting. This binding is the first line of defense against a descriptor being misapplied to the wrong contract.

The `metadata` section carries the trusted constants: the protocol's display name, ERC-20 token details when the contract does not expose them on-chain, and reusable `enums`, `constants`, and `maps` that the display section references.

The `display.formats` section is the heart of the file. Each key is a Solidity function signature with parameter names — `transfer(address to,uint256 value)` — and each value describes how to render that call: an `intent` string ("Send"), an optional `interpolatedIntent` template ("Send {value} to {to}"), and a `fields` array that says how to format each parameter.

### The matching and rendering flow

When a user initiates a transaction, a clear-signing wallet does the following:

1. It receives the raw calldata, the destination address, and the chain ID.
2. It finds a descriptor whose context constraints match that `(chainId, address)`.
3. It walks the `display.formats` keys, strips the parameter names to get a canonical type signature (`transfer(address,uint256)`), hashes it, and matches the resulting 4-byte selector against the calldata.
4. It decodes the arguments using the types from the matched key, then applies each field's formatter — converting a raw integer into "100 USDT" using the token's decimals, resolving an address to an ENS name, formatting a timestamp as a date.
5. It displays the intent, the user reads it, and the user signs the unchanged raw bytes.

### The three path roots

There is one piece of the syntax that confuses nearly everyone on first contact, and it is worth understanding precisely because it has security implications. When a formatter needs a value, it references that value with a path, and the path begins with one of three roots that tell the wallet which source to look in:

- `#` — the decoded transaction data. These are the actual function arguments being signed right now. `#.to` is the live recipient argument; `#.value` is the live amount. Omitting the root entirely defaults to `#`.
- `$` — the descriptor file itself. This reaches the constants, enums, and maps defined in the file. `$.metadata.enums.interestRateMode` looks inside this JSON file.
- `@` — the transaction container. These are the envelope fields that wrap the calldata: `@.from`, `@.to`, `@.value`, `@.chainId`.

The distinction between `#.to` and `@.to` is the one to internalize. `#.to` is the `to` argument of the function — the recipient of the tokens. `@.to` is the contract the transaction is being sent to — the token contract itself. They are different values, and conflating them is a class of authoring bug.

Look at the canonical example with this lens:

{ "path": "value", "format": "tokenAmount", "params": { "tokenPath": "@.to" } }

This reads: take the `value` argument from the decoded data (`path` defaults to `#`), format it as a token amount, and to determine which token's decimals and ticker to apply, look at `@.to` — the contract this transaction is hitting. Because the transaction targets the USDT contract, `@.to` resolves to USDT's address, the wallet fetches its six decimals and "USDT" ticker, and the raw integer renders as "100 USDT."

A useful shorthand: `#` is what is being signed, `@` is the envelope it arrived in, `$` is the reference sheet in the descriptor.

## Best Practices

These are the patterns that the Ethereum Foundation tutorial, the Ledger developer documentation, Trail of Bits, and Cyfrin converge on. They apply whether you are authoring a descriptor or checking one before it ships.

Bind the context tightly. Always specify explicit `(chainId, address)` pairs. For EIP-712 messages, never bind on `domain.name` alone — include deployments or a `domainSeparator`. A loose binding lets one descriptor apply to contracts it was never meant for.

Make every execution-affecting field visible. Any parameter that changes what the transaction actually does — a destination address, a value, a deadline, a chain ID, and above all an operation or mode flag — should be `visible: "always"`. The visibility system allows fields to be hidden for screen-space reasons, but hiding a semantically critical field recreates the Bybit vulnerability inside a descriptor that otherwise looks clean.

Use enums for opaque integers. A `uint8 mode` that takes values `0`, `1`, `2` should always carry an enum mapping in metadata, so the user sees "variable rate" rather than "2."

Author generic interfaces once and include them. Rather than repeating ERC-20 boilerplate in every token descriptor, write a shared interface descriptor and pull it in with `includes`. Less duplication means fewer places for an error to hide.

Ship golden test cases. The registry expects a test file pairing sample calldata with the expected rendered output. These are what catch a regression when a descriptor is updated after a contract upgrade.

Author from a verified contract and publish to the registry — not to a self-hosted CDN. The contract should be verified on Sourcify, which is a prerequisite for registry inclusion. The descriptor belongs in the Ethereum-Foundation-hosted registry, not served live from the dApp's own infrastructure. This last point is subtle but important: if a wallet fetched the descriptor from the dApp at signing time, a compromised front-end could swap in a malicious descriptor — which is exactly the attack clear signing is meant to prevent. Publishing to a curated, attested registry breaks that link.

Treat the descriptor as versioned protocol surface. When a contract upgrade ships behind a proxy, the descriptor must be updated in lockstep, or it will decode the new ABI against stale assumptions.

## Security Considerations and Shortcomings

ERC-7730 does not eliminate risk; it relocates it. A readable transaction prompt is only as trustworthy as the descriptor that produced it, and the standard introduces a new artifact that can be wrong, stale, or adversarial.

A central distinction is that readable is not the same as verified. A descriptor can render a perfectly clear, perfectly honest-looking sentence for a transaction that drains a wallet. The standard makes intent legible; it does nothing to make the underlying contract behavior correct. As Trail of Bits put it plainly, the most direct attack vector remains exploiting the smart contract itself. Clear signing offers no protection there.

There are also entire categories of transaction the standard simply cannot describe. Contracts using custom packed encodings — Safe MultiSend, the Uniswap Universal Router, certain cross-chain system messages — do not fit the selector-plus-ABI model ERC-7730 assumes. For these, there is no descriptor that can ever work, which is precisely why the ERC-8213 calldata-digest fallback exists: it lets a signer verify the exact bytes on an independent device rather than relying on a human-readable description. A brand-new contract has no descriptor at all until one is written and merged, so the window between deployment and registry coverage is blind signing for its entire duration.

Beyond these structural limits, the standard's own Security Considerations section enumerates a new attack surface that did not exist before clear signing: parameter injection, registry poisoning, and front-end compromise that prompts for unexpected contracts. The sections below treat each of these concretely.

## Attack Surfaces in Practice

When a descriptor is part of a system you build or depend on, these are the concrete failure modes to examine, ordered roughly by how often they will actually matter.

### 1. Token and name resolution spoofing

This is the threat to assume by default. When a `tokenAmount` formatter resolves a token's ticker and decimals dynamically — via `@.to` or a `tokenPath` — it trusts whatever that token contract reports. A worthless token deployed by an attacker can return "USDT" from `symbol()` and `6` from `decimals()`, and the wallet will faithfully render a transfer of that token as "100 USDT." The descriptor's `context` binding pins the outer contract, but the dynamically resolved token is exactly the part that is not pinned.

What makes this more dangerous than plain blind signing is the confidence inversion. A user faced with unreadable hex is cautious. A user shown "100 USDT" by a wallet they trust is relaxed. The standard manufactures false confidence in precisely the scenario it was meant to protect. The same logic applies to ENS and other name resolution: a compromised or adversarial resolver can substitute a malicious address behind a familiar name. Mitigations exist — curated allowlists of well-known tokens, displaying full addresses alongside resolved names, clearly indicating the source of a name — but these have to be confirmed in the wallet and descriptor rather than assumed.

### 2. Descriptor drift and stale caches

This one requires no attacker at all. Descriptors are cached by wallets. Contracts are upgraded behind proxies. When a proxy upgrade changes the ABI and the descriptor is not updated in lockstep — or the update is published but wallets have not pulled it — the wallet decodes new calldata against stale assumptions and renders a confident, wrong description. The base standard has no on-chain revocation mechanism. ERC-8176 attestations can be revoked on-chain through EAS, but revoking an attestation does not pull a descriptor out of a wallet's cache, so there is still no authoritative signal that forces a stale descriptor out of circulation. For any upgradeable protocol, descriptor-versus-implementation synchronization is a live operational risk worth raising explicitly.

### 3. Hidden execution-affecting fields

This is the Bybit class, encoded into a descriptor. The visibility system permits a field to be marked so it never displays. If a field that changes execution semantics — an operation flag, a delegatecall target, a mode selector — is hidden, the descriptor reproduces the exact vulnerability that drained Bybit, except now wrapped in a prompt that looks trustworthy. The frequency of such attacks is low; they tend to be the work of sophisticated, well-resourced actors. But the consequence is severe enough that any hidden field touching execution semantics should be treated as a serious red flag. Prefer enforcement (`mustMatch`, which hides a field but checks its value) over silent omission.

### 4. Interpolated-intent injection

The `interpolatedIntent` template builds a sentence by substituting field values into a string. If one of those values is attacker-controlled — a token name, say — it can be crafted to forge the appearance of legitimate intent. A token whose name contains the text " to vitalik.eth" can turn "Send {value} to {recipient}" into a string where the malicious recipient scrolls off-screen and a trustworthy-looking name takes its place. The standard's defense is to require that interpolated values be formatted and validated identically to how they would be shown as standalone fields, and to make the individual fields independently inspectable. Whether a given wallet implements that defense correctly is an implementation question worth checking.

### 5. Binding and proxy abuse

Loose context binding lets a descriptor apply where it should not. The proxy patterns deserve specific attention: for upgradeable proxies, a descriptor bound to the proxy address can go stale across an upgrade; for multi-instance factory patterns, descriptors bind to the shared implementation — or, through the factory context, to every contract a given factory deploys — which means any instance running that code inherits clear-signing trust, including one an attacker deployed with their own owner, modules, or configuration, none of which the descriptor shows. For EIP-712, binding on domain name without the verifying contract lets any contract reusing that domain name borrow legitimacy.

### 6. Registry and attestation trust

Registry poisoning — slipping a well-formed but misleading descriptor into the canonical registry — is realistic enough that the standard explicitly says any registry must assume it will be targeted, and lists the provenance, attestation, and governance controls a secure registry should have. The Ethereum Foundation registry mitigates this with CI checks, mandatory Sourcify verification, reviewer approval, and the ERC-8176 attestation layer. But ERC-8176 introduces its own question: each wallet decides which attesters it honors, and there is no universal trust set. As the attestation ecosystem matures, inconsistent trust decisions across wallets are likely to be a more practical problem than a poisoned merge slipping through review.

### 7. Hardware wallet display constraints

Small screens cannot show everything. A batch with thirty approvals, or a deeply nested recursive `calldata` decode, will exceed a hardware device's display budget. The standard acknowledges this and provides mechanisms to flatten and prioritize fields, but the user does not see what was elided. An attacker who knows a particular device truncates after N entries can position a malicious entry at N+1. The recursive embedded-calldata decode that the Bybit-style nested transaction requires is also, by the spec's own admission, expected to work "with restrictions at first" on hardware wallets — meaning the very transactions most in need of clear signing are the ones most likely to fall back to a hash.

## Conclusion

ERC-7730 operates on the transaction-authorization step by turning opaque calldata into a readable intent, addressing the blind-signing gap involved in the Bybit, WazirX, and Radiant incidents. Because it is a presentation layer rather than a protocol change, it can be applied to existing contracts without redeployment.

In security terms, the standard relocates risk into a new artifact — one that can be stale, spoofable, or adversarial, and that has to be evaluated in its own right. Clear signing makes intent legible; it does not make intent honest, and it does not make the underlying contract safe. It functions as one layer alongside contract review, transaction simulation, multisig controls, and independent cross-device verification through ERC-8213 digests. Reviewing a descriptor answers a different question from reviewing a contract: not "what does this code do?" but "does the description a user will see faithfully represent what this code does?" Those are separate evaluations, and the ERC-8176 attestation flow assigns the second one to whoever signs off on the descriptor.

One scope note is worth stating. The standard moved under Ethereum Foundation stewardship recently, and at the time of writing there is no substantial body of post-deployment incident data specific to ERC-7730. The attack surface described here is derived from the standard's mechanics and from the pre-existing blind-signing patterns it inherits, not from a catalogue of observed ERC-7730 exploits. The relative ranking of these risks may shift as the standard sees adversarial attention at scale.
