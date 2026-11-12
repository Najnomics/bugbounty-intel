# 🛡️ EIP-7732: Controversial Ethereum Scaling

- **Source URL:** https://blog.sigmaprime.io/glamsterdam-eip7732.html
- **Fetched from:** https://sigmaprime.io/blog/glamsterdam-eip7732/
- **Fetched:** 2026-11-12
- **Channel:** @defendor_eng
- **Telegram message:** https://t.me/defendor_eng/395 (id 395)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
## The case against EIP-7732 for Glamsterdam

**TLDR**: Enshrining proposer-builder separation (PBS) today is unnecessary. However, if we aim to scale massively in the short term, we can implement EIP-7732 without trustless payments.

My criteria to vouch for the inclusion of an EIP are:

- The EIP is time sensitive and must be implemented in fork X and not later
- There are no better alternatives
- There are no simpler alternatives

The merits of EIP-7732 are well outlined here [SigP's prior blog post](https://sigmaprime.io/blog/glamsterdam-headliner/), but in summary, it allows further scaling by giving more time to stakers to perform their duties.

However, my reservations with EIP-7732 can be summarized as:

1. No demonstrable urgency to enshrine a flavor of PBS today.
2. Main scaling wins (payload split + delayed execution) can be delivered without trustless payments (ePBS).
3. Even those tweaks may be premature, the chain has sufficient headroom for the next fork cycle.
4. Active research on slot auctions, execution layer payment paths, and MEV-Burn integration suggests holding off for better design flexibility.
5. Staked builder requirement raises capital barriers

### No demonstrable urgency to enshrine

MEV-boost has been performing well, with infrequent incidents that have had little to no impact. In my opinion, the very few incidents it has suffered aren't solved by ePBS and don't justify an urgency to change it.

### Main scaling wins are possible without ePBS

If there's no urgency to enshrine a specific flavor of ePBS, we can do slot restructuring and payload decoupling without committing to a specific bidding market and introducing the role of a builder.

The fact that there's no spec for such an approach today should not be a reason to discard this idea. Even then, we may not need to do slot restructuring **and** payload decoupling now.

### Even slot restructuring + decoupling may be premature

The main selling point of EIP 7732 is scaling, specifically:

- *Goal-1*: More time to validate the execution payload
- *Goal-2*: More time to propagate the execution payload

In essence, we can have bigger blocks and more expensive blocks to verify without forcing stakers to invest in more bandwidth or better CPUs. We want to avoid a situation where we scale the chain at the expense of the stakers running on less powerful hardware.

Let's look first at the anatomy of a slot today.

There are 4 seconds to compute, propagate, validate, and vote for a block. However, if the proposer wants to maximize its revenue, it will commit to the execution payload as late as possible. This shrinks the time to broadcast and validate the execution payload to a time such that at least 40% of the slot committee can attest to that block.

Now, how does the diagram look for attesters with fewer resources?

Notice that slow attesters won't get to set the block as head in time, resulting in an incorrect head vote and losing 1/8 of rewards.

Our goal is to ensure that all stakers (given some minimum spec requirements) can process *most* blocks in time to correctly attest to them. However, blocks require widely different amounts of resources. We have to account for the worst-case processing time, so that it bounds how much we can safely increase the block gas limit. We are addressing this variance in a separate scaling effort. Then, by minimizing the worst case, we can scale the block gas limit without requiring slot restructuring.

To put some numbers, consider that creating a worst-case block takes 1 second, propagating it takes 1 second, then we have $4-1-1 = 2$ seconds to verify the block.

Eventually, we will reach a limit where the time between the start of the slot and the attestation deadline is not enough to produce, propagate, and validate a full block. **Then**, we must implement some flavor of slot restructuring to safely increase the gas limit further.

#### Delayed execution

The first strategy is to implement delayed execution. Currently, we need to execute a block during its slot to attest if its payload is valid or not. Instead, we can attest at slot $N$ that the payload for block $N$ was available, and attest to its validity in slot $N+1$. With the example numbers above, we have:

- 3 seconds to propagate the full block
- 12 extra seconds to validate the payload (attesters)
- or 8 extra seconds to validate the payload (next slot proposer)

So in this example, we could increase the max block size by 3x and the gas limit by some factor such that the worst time increases by 12x. Note that EIP-7732 and EIP-7886 both implement different flavors of delayed execution. This section refers to the general concept, not a specific implementation.

#### Payload decoupling

Note that in *delayed execution* we still require attesters to receive the payload before the attestation deadline. We could remove that requirement by decoupling the execution payload from the block. Now, attesters just vote on the availability and validity of the consensus block.

Now they must receive and validate the execution payload before the attestation deadline, or before the end of the slot for the proposer. Using the same example numbers as above:

- 3+12 seconds to propagate and validate the payload (attesters)
- 3+8 seconds to propagate and validate the payload (next slot proposer)

However, to implement payload decoupling, we must modify the fork-choice and introduce a new role in the protocol: the **payload timeliness committee (PTC)**. We don't know what will dominate in the future: payload propagation times or payload validation times. If we maintain a ratio of `payload propagation time/payload validation time` with proper opcode pricing, payload decoupling doesn't yield additional **block gas limit** scaling benefits.

Payload decoupling also extends the maximum time to receive blobs from 3 seconds to the same numbers as above. However, PeerDAS and sampling are active areas of research that can significantly impact this effect.

## ePBS is still in active research

There has been extensive research on ePBS in the last 3 years. Topics like slot auctions, execution layer payment paths, and MEV Burn integration are still in active research. I feel that it's too early to commit to a specific flavor of ePBS. Since there is no urgency, we must consider the cost of committing early and losing flexibility.

## Staked-builder requirement

EIP-7732 enshrines a capital requirement for builders. While this has benefits for accountability, it adds friction to new players for an already highly centralized market. Refer back to the previous point and note that there exist ePBS designs without this requirement.

# Closing remarks

EIP-7732 is possibly the best and most ready spec of enshrined proposer-builder separation (ePBS). If we must ship some form of ePBS **ASAP**, I will vote to schedule EIP-7732 for Glamsterdam.

However, I don't see demonstrable urgency to enshrine a flavor of PBS today. Its main scaling wins (payload split + delayed execution) can be delivered without trustless payment. And even those tweaks may be premature for a few years. Active research on slot auctions, execution layer payment paths, and MEV Burn integration suggests holding off to preserve design flexibility.

*NB: Opinion posts reflect the ideas and experiences of Sigma Prime engineers. These are informed opinions from respected core developers and security researchers however they are not necessarily representative of the organisation as a whole.*
