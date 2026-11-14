# 🔍 Certora's Sunbeam Outperforms Fuzzers on Soroban Bug Detection

- **Source URL:** https://www.certora.com/blog/formal-verification-vs-fuzzing
- **Fetched:** 2026-11-14
- **Channel:** @defendor_eng
- **Telegram message:** https://t.me/defendor_eng/2053 (id 2053)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
[← Engineers' Hub](https://www.certora.com/blog/engineers-hub)

# Comparison of Security Tools for Soroban Smart Contracts: Why Sunbeam Is Superior

We tested cargo-fuzz, Komet, and Certora Sunbeam on the same Soroban contract to compare bug detection with proof of correctness.

This experiment compares fuzzing and [formal verification](https://www.certora.com/blog/what-is-formal-verification) on a small Soroban contract and a simple property. We wanted to see whether each tool can find real bugs and whether it can prove that a variant is correct.

We used a small Soroban adder contract and three tools to check one simple rule: addition should be commutative. That means add(a, b) should always equal add(b, a).

The tools are:

- [cargo-fuzz](https://github.com/rust-fuzz/cargo-fuzz): a fuzzing tool for Rust,
- [Komet](https://github.com/runtimeverification/komet): Runtime Verification's fuzzing and proving tool for Soroban,
- [Certora Sunbeam](https://docs.certora.com/en/latest/docs/sunbeam/index.html): a formal verifier for Soroban contracts.

Each tool got the same code and the same rule. The question is what each one can actually conclude.

## The example

The contract is the adder from [Komet's documentation](https://github.com/runtimeverification/komet). It has one entry point:

The rule is: `add(first, second) == add(second, first)`

This contract is used as an example for Komet, and we made five versions of the contract to test more aspects of the system:

- `noif`: correct, `just first + second`.  This is the original code, which is correct and has only rather simple math.
- `complex`: has a branch that fires only when `second == 1000`, implemented in a roundabout way using `(second / 10 == 100) %% (second % 10 == 0)`; the branch returns `first + 1000`, which, in this case,  equals `first + second` — so the code is still correct.  This is meant to test a system being given somewhat more complex math.
- `zero`: returns `0` when `second == 0`.  This is meant to break commutativity, with an obvious value breaking the test.
- `100`: returns `0` when `second == 100`.  This also falsifies the assertion, using a value that would take brute-force search a bit longer to find than would 0.
- `big`: returns `0` when `second == 2147483622`.  This also falsifies the assertion, using a value that is unlikely to be found by brute force search.

The last three falsify the assertion because one special input changes the result. `zero` breaks visibly: `add(1, 0)` returns `0`, but `add(0, 1)` returns `1`.  `big` has the same bug, but the trigger is one value out of 4 billion, so it is much harder to hit by chance.

## How the rules are written

For Sunbeam, the rule is six lines of Rust:

Here `first` and `second` are symbolic values, so Sunbeam checks the rule for all inputs at once instead of testing them one by one. When the rule fails, `clog!` prints the exact inputs that break it.

`cargo-fuzz` needs a test harness with a mocked contract environment. The harness is about 50 lines, and the contract has to be modified to expose a public test entry point. The fuzzer then tries many inputs until it finds a failure.

Komet can run the property as a contract test (`komet test`) or try to prove it symbolically against its formal semantics of Soroban (`komet prove`).

## What happened

We gave cargo-fuzz 100 seconds per variant, Komet 1,000 test examples plus 150 CPU-seconds of proving, and ran Sunbeam with its defaults.

Within these budgets, cargo-fuzz and `komet test` caught `zero` quickly and `100` fairly quickly, but missed `big`. While big may seem like a silly test, the smart contract world is full of adversaries who will contrive hard-to-find issues.  Sunbeam returned a counterexample for each buggy version and a proof for each correct one.

The main point is this: a clean fuzzing run only means the fuzzer did not find a bug. It does not mean the contract is correct. The prover can either find a real counterexample or prove the rule for all inputs.

## What this shows

This is a small experiment and not a broad comparison. While sampling tools search for specific inputs, provers reason about all of them. Fuzzing is useful: it can find some bugs quickly and can scale to large code. But fuzzing is not the same as proving. Some bugs only occur at one exact input, so they are easy to miss. Symbolic reasoning can find the exact failing value.

A prover can also do something a fuzzer cannot, i.e., a prover can offer a formal guarantee that a correct variant is actually correct. The `complex` version gives an example. Even though its branch looks suspicious, simple arithmetic shows it does not change the result.

We also saw that automated provers can sometimes timeout. While many of them rely on SMT solvers like Z3 and CVC5, a naive encoding to SMT may not always succeed, because the underlying problem is not decidable. Sunbeam, for example, tries to mitigate this to some extent by performing several semantics preserving program transformations that lead to simpler SMT formulae that often lead to faster verification time even when the program is complex. Sunbeam also uses multiple solvers with different configurations (this is known as the portfolio method), which ensures that even when one solver times out, others will still try to produce a result.

## Try it yourself

The [repository](https://github.com/Certora/prover-vs-fuzz) has all five contract versions, each wired up for all three tools, and a run.sh script that runs the full experiment. Once you have all three tools installed, you can run:

To try Sunbeam on your own contracts, see the [installation guide](https://docs.certora.com/en/latest/docs/sunbeam/installation.html).
