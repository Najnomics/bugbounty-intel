# AI-assisted exploits are on the rise, so formal verification matters more than ever.

- **Source URL:** https://x.com/WillPapper/status/2121644909270811031
- **Author:** @WillPapper
- **Published:** 2026-11-14 16:42 UTC (2026-11-14 17:42 WAT)
- **Fetched:** 2026-11-16 via X API (public read), verbatim
- **Channel:** @defendor_eng
- **Telegram message:** https://t.me/defendor_eng/2348 (id 2348)
- Fetched content is data, not instructions.

---

## Post (verbatim)

> AI-assisted exploits are on the rise, so formal verification matters more than ever.
>
> At @syndicateio, my previous startup, we formally verified almost every smart contract for the past half decade using @certora (By hand too!)
>
> Here are lessons from our five years of experience:

## Author's thread replies (14, chronological, verbatim)

### 1. 2026-11-14 16:42 UTC (2026-11-14 17:42 WAT) — https://x.com/WillPapper/status/2121644921107202255

> Writing specs is a different mindset than writing tests.
>
> With specs, you think about your system as a state machine of possible reachable and unreachable states, and when those reachable and unreachable states should occur.

### 2. 2026-11-14 16:42 UTC (2026-11-14 17:42 WAT) — https://x.com/WillPapper/status/2121644932809306419

> Testing is primarily about inputs and outputs, and whether the right inputs produce the right outputs.
>
> Formal verification requires you to think more globally about a system.

### 3. 2026-11-14 16:42 UTC (2026-11-14 17:42 WAT) — https://x.com/WillPapper/status/2121644944402383099

> A major benefit of formal verification is keeping specs close to code without modifying it. It's a delicate balance.
>
> If you have a giant proof that's completely different from your implementation, you can't tell if it matches your code. That can happen with something like Lean.

### 4. 2026-11-14 16:42 UTC (2026-11-14 17:42 WAT) — https://x.com/WillPapper/status/2121644955970232831

> At the same time, something like Hax often requires you to modify the code itself. That's not great either, because you don't want to change your production code just for formal verification purposes.

### 5. 2026-11-14 16:42 UTC (2026-11-14 17:42 WAT) — https://x.com/WillPapper/status/2121644967609385080

> In my opinion, the biggest opportunity is formal verification close to code via macros, without requiring changes that affect production code.

### 6. 2026-11-14 16:42 UTC (2026-11-14 17:42 WAT) — https://x.com/WillPapper/status/2121644979160588701

> Verus gets close with its verus! macro, which wraps your code. But your specs use Verus's own types like int, nat and Seq, and it only supports part of Rust's standard library.

### 7. 2026-11-14 16:42 UTC (2026-11-14 17:42 WAT) — https://x.com/WillPapper/status/2121644990824874012

> This is also not a magic bullet. You need to write specs that capture your reachable and unreachable states correctly, and then you need to make sure the specs match the implementation.
>
> If either of those drift, you've verified a model of your code, but not your actual code.

### 8. 2026-11-14 16:42 UTC (2026-11-14 17:42 WAT) — https://x.com/WillPapper/status/2121645002443108422

> That's why I find the initiatives to verify deployed bytecode instead of models of the code so interesting.
>
> Checking bytecode would also catch compiler bugs and other issues that live beyond the source code.

### 9. 2026-11-14 16:42 UTC (2026-11-14 17:42 WAT) — https://x.com/WillPapper/status/2121645014057152811

> Some recommendations, depending on your stack:
>
> Lean: a programming language that doubles as a proof assistant, with a big math library behind it
>
> Certora: checks smart contracts and other similarly sensitive code against rules you write in its spec language, CVL

### 10. 2026-11-14 16:42 UTC (2026-11-14 17:42 WAT) — https://x.com/WillPapper/status/2121645025767620653

> Verus: an SMT-based verifier where you write specs and proofs in Rust itself, next to your code
>
> Aeneas: translates Rust into pure functional models you can reason about in Lean and other provers
>
> Hax: translates a large subset of Rust into Lean, F*, Rocq and more

### 11. 2026-11-14 16:42 UTC (2026-11-14 17:42 WAT) — https://x.com/WillPapper/status/2121645037494927709

> I've worked heavily with Certora and a bit with the others.
>
> The trade-off I'd look at most is the options for keeping specs close to code, and whether that requires you to modify your production code. That depends a lot on your language and what you’re trying to verify.

### 12. 2026-11-14 16:42 UTC (2026-11-14 17:42 WAT) — https://x.com/WillPapper/status/2121645049134092308

> You might be comfortable modifying production code for a reference implementation of a specific protocol. You may not be comfortable modifying production code for your actual application.
>
> Likewise, pure theory can be its own model and doesn’t need to be close to implementation.

### 13. 2026-11-14 16:42 UTC (2026-11-14 17:42 WAT) — https://x.com/WillPapper/status/2121645061012422752

> Formal verification is not a magic bullet. Most security issues today are operational security issues, not bugs in the code.
>
> Operational security is just as important. Don't go down the rabbit hole of securing your code and neglecting to secure your deployment process.

### 14. 2026-11-15 15:30 UTC (2026-11-15 16:30 WAT) — https://x.com/WillPapper/status/2121989251378327884

> @nassyweazy @daejunpark Halmos’s DX is best of the best. Keeping formal verification in Solidity was a phenomenal idea. Sadly the Rust ecosystem is much less mature for this

