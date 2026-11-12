# 📡 Getting Wrecked via Solana RPC, One Lamport at a Time

- **Source URL:** https://arsensecurity.substack.com/p/how-to-get-wrecked-via-solana-rpc
- **Fetched from:** https://newsletter.arsen.ac/p/how-to-get-wrecked-via-solana-rpc
- **Fetched:** 2026-11-12
- **Channel:** @defendor_eng
- **Telegram message:** https://t.me/defendor_eng/2045 (id 2045)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
The service pulls every account the program owns, no filter, and figures out the rest later.

The service needs to know how an account was created.

The account is real.

Its history is real.

It still reads the wrong transaction out of it.

Quick refresh so we’re on the same page.

**On Solana an account stores state.**


Current state, nothing else.

It doesn’t store how it got there.

No created\_at, no origin field, nothing that says which transaction made it.

That’s a good design. Accounts stay small and cheap.

But if you want the creation transaction, you ask an RPC node for the address history.

The tradeoff this bug lives on:

Three words you’ll need:

- **PDA** - the account the program creates for each request.
- **Signature** - the ID of a transaction.
- **Backfill** - the catch-up path. Service was down, now it re-reads what it missed.

Now the service.

The on-chain program was clean.

Zero findings there.

So you’re in the off-chain part. Rust, RPC calls, plumbing.

**First pass**: does it parse the account correctly? It does.

**Second pass**: retries, error handling, deserialization. All fine.

You never ask: what does this RPC actually promise about order?

And who else can write into what it returns?

`.first()`. That’s the whole bug.

And it runs once per account, inside the sweep.

Here’s the interesting part.

There are two ways this service learns about a request.

**Live path: a websocket event arrives and the signature is inside it.**

The service parses that one transaction, and it’s correct by construction.

Nobody picked the signature. It was handed over.

Backfill path: no event.

**So the service asks for every account the program owns, then asks each account for its signatures, then takes the first one, then calls the same parsing function as the live path.**

“Same function at the end. What could go wrong?”

The live path never had to choose.

The backfill path invented a lookup, and it identifies the creation transaction by position in a list.

Position in a list that strangers can push to.


The attack is not complicated:

Who pays for it: the catch-up path itself.

It’s a denial of service on backfill, not one stuck request.

Everything that was waiting to be caught up keeps waiting.

The attacker spends one lamport for that.

When you audit any off-chain service that reads chain state, check:

The model worth keeping:

The account tells you its state. It never tells you its story.


And the story is a list strangers can write to.

Everyone knows not to trust user input.

Almost nobody counts a transaction history as user input.

But that’s what it is.

It’s not the account’s own data. It’s a list a node keeps about an address, and the address is public, so the list is open.

Root cause, one line:

**Off-chain identity taken from position in a list anyone can append to.**


Two fixes.

1. Use `.last()` instead of `.first()`. Fixes the order, and it holds until someone spams the address - `getSignaturesForAddress` returns 1000 signatures max, so `.last()` is the oldest of that page, not the oldest ever.
2. Stop reading history at all. Put the access mode directly in the PDA, so the state answers the question and there is no signature scan left to attack.

The team went with the second one. Design review, program changed, the whole traversal deleted.

Arsen
