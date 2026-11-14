# 🛠 LayerZero Unveils Otter, an MEV-Resistant AMM Design

- **Source URL:** https://layerzero.network/blog/otter-the-mev-resilient-amm
- **Fetched:** 2026-11-14
- **Channel:** @defendor_eng
- **Telegram message:** https://t.me/defendor_eng/2049 (id 2049)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
We’re sharing a new paper from the LayerZero research team in collaboration with Oblivious Labs and CMU – authored by LayerZero researcher Hao Chung and our collaborators Yuhao Li, Elaine Shi, and Mengqian Zhang – exploring a new AMM mechanism built to be resilient against MEV.

We call it OTTER, or Optimal Truthful Trading with Excess Redistribution.

Otter’s name captures its two central benefits:

- The paper formally proves that truthful behavior is a dominant strategy for both traders and block builders.
- Otter redirects excess value that would otherwise be captured as MEV to benefit liquidity providers, traders, the liquidity pool, or validators securing the underlying chain.

Otter's guarantees hold when the underlying consensus layer provides censorship resistance. In fact, the assumption is necessary. We show that if a builder can censor bids and block space is finite, no non-trivial AMM mechanism can simultaneously guarantee truthful reporting for users and strategy-proofness for a builder-as-user. The result formally connects consensus-layer guarantees to what's achievable in application-layer mechanism design.

### **Truthful trading and MEV-resilient block building**

Otter clears all bids in a block together through a VCG-style auction—a gold-standard approach in mechanism design for eliciting truthful reports. The paper proves that traders maximize their profit by truthfully reporting their valuations and budgets. Truthfulness is not an assumption about how traders behave; it is their dominant strategy.

Batch clearing also neutralizes a block builder’s privileged position. In traditional sequential AMMs, builders can profit by rearranging transactions to front-run or sandwich traders. In Otter, the outcome depends on the set of bids rather than their order, so rearranging them provides no advantage. Nor can a builder profit by injecting fabricated bids through pseudonymous accounts to manipulate the batch outcome.

Put simply, Otter makes block manipulation unprofitable. A builder cannot benefit from reordering transactions, injecting Sybil bids, or misreporting its own valuation or budget—even when the builder is itself a trader. This is what makes Otter resilient to these forms of MEV.

### **A new approach to value capture: surplus redistribution**

Batch execution does more than neutralize transaction ordering.

Most popular AMMs settle each trade separately: every individual trade moves the pool from one point on its pricing curve to another, and all tokens output by the pool are paid to the trader. Otter instead requires only that the pool end on its pricing curve after the batch as a whole. It also does not require all of the pool’s output to be paid to traders in the current batch.

This creates a residual surplus—value that could otherwise be captured as MEV. Otter can instead use it to reward liquidity providers, deepen the pool and reduce future slippage, subsidize trader fees, or support the underlying chain and its stakeholders.

### **The MEV-Resilient AMM**

MEV extraction today is concentrated: a small number of block builders produce the overwhelming majority of blocks, and that concentration is self-reinforcing: dominant builders get better order flow, which makes them more dominant.

Otter is a different bet: redesign the AMM so that a builder’s privileged position no longer translates into private extraction. Truthful participation becomes the dominant strategy, manipulation is unprofitable, and excess value is redistributed to the broader ecosystem rather than reinforcing builder dominance.

Read the full paper on [arXiv](https://arxiv.org/abs/2609.03474).
