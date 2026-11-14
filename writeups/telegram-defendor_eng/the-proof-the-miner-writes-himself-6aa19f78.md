# 🔍 How to Hack a Bitcoin Light Client

- **Source URL:** https://arsensecurity.substack.com/p/the-proof-the-miner-writes-himself
- **Fetched from:** https://newsletter.arsen.ac/p/the-proof-the-miner-writes-himself
- **Fetched:** 2026-11-14
- **Channel:** @defendor_eng
- **Telegram message:** https://t.me/defendor_eng/2073 (id 2073)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
The light client verifies one merkle proof before it accepts a block.

That proof is correct.

The value it then goes looking for is one the submitter computed himself.

And it goes looking for it with a text search.

Quick refresh so we’re on the same page.

Some chains don’t mine their own blocks.

Dogecoin is one.

Miners point their hardware at Litecoin, and the same work counts for both chains at once.

That’s merged mining, and it’s a good deal.

One machine, two rewards, no extra electricity.

The proof has to live somewhere, and it lives on the parent chain:

- Every block starts with a coinbase, the transaction that pays the miner.
- The coinbase has a field with no consensus meaning at all. Free space.
- The child chain’s commitment gets written into that free space.
- Whoever mines the parent block writes that field. By hand. Anything they want.

Three words you’ll need:

- **Coinbase** - the first transaction in a block. Pays the miner.
- **script\_sig** - the free-space field inside it.
- **chain\_root** - the commitment that says which child block this work belongs to.

Now the light client.

You review the aux path and it looks like the strongest code in the file.

Merkle tooling everywhere.

Four steps, one after another.

**Step one:** this parent block hasn’t been used before.

**Step two:** the coinbase transaction is proven into the parent block’s merkle root. That one is real.

**Step three:** a chain\_root is computed. Not verified. Computed, out of the child block hash, a chain id, and a merkle proof.

All three of those come from whoever is submitting.

“It’s covered in merkle proofs. What could go wrong?”

Read step four.

`.contains()`.

Step two proves structure. Step three derives a number out of attacker input. Step four searches for that number.

Only one of the four is a check.

It renders the script to a hex string and asks whether the derived root appears somewhere inside it.

Somewhere.

Not at the offset the format specifies. Not once. Not after the marker bytes that say the merged mining section starts here.

Anywhere in the string is a pass.

And the field it searches is the one field on the parent chain that a miner fills in freely.

The attack is not complicated:

- miner writes their own chain\_root into script\_sig
- writes the honest one in after it
- both are present in the hex
- `.contains()` finds whichever it is asked about
- the same parent block now attests to two different child blocks
- the light client accepts the one it was handed

The merged mining format exists to stop exactly this.

There are marker bytes, a position rule, a size and a nonce, and a requirement that the commitment appear once.

None of that is checked here.

The format was replaced by a substring search.

There’s a second problem in the same line, pointing at the same cause.

`.to_hex_string()` and `.to_string()` are two renderings by two different types.

Bitcoin stores hashes little endian.

Display prints them the other way round.

So an honest submitter, handing over correct data in the byte order the chain actually uses, fails this check.

The search is wrong in both directions. It admits what it shouldn’t, and it rejects what it should take.

When you audit a commitment check, ask:

- Is this comparing bytes, or comparing strings that describe bytes?
- Does the format specify a position, and is the position enforced?
- Can the field appear twice? What happens if it does?
- Who writes the field being searched? If the answer is a miner, it is attacker input.
- Are the two sides of the comparison the same type, rendered the same way?

Most reviews check whether the value is there.

Finding a value is not the same as validating where it sits.


The usual version of this finding is a missing check.

Something absent, you grep for it, you find the gap.

Here the check is present, and it runs, and it passes for the honest case in every test.

It is the wrong kind of check, and the wrong kind of check looks exactly like the right kind until someone writes a second value into the same field.

Root cause: a structural commitment verified by substring search.


Two fixes.

1. Parse the script instead of searching it. Find the marker, read the commitment at the offset the format defines, reject the block if it appears more than once.
2. Compare bytes to bytes. The hex round trip is what let two different orderings look comparable in the first place.

The fix that shipped was neither. Access control, so only the relayer can submit blocks.

That closes the door. It doesn’t fix the lock.

Arsen
