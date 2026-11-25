# 🛡 Fuzzing Solana: A Practical Guide

- **Source URL:** https://zokyo.io/blog/guide-to-fuzzing-solana
- **Fetched from:** https://web.archive.org/web/20260129075903/https://zokyo.io/blog/guide-to-fuzzing-solana/
- **Fetched:** 2026-11-25
- **Channel:** @defendor_eng
- **Telegram message:** https://t.me/defendor_eng/1017 (id 1017)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
### A Practical Guide to Fuzzing Solana Smart Contracts with Honggfuzz

Oct 13, 2025

20 Minutes

Security testing for blockchain programs is not optional, it’s an operational requirement. In this article, we will show a practical, developer walkthrough for fuzzing a Solana Vault program written with the Pinocchio library, using Honggfuzz to generate random adversarial inputs that should pick up edge cases and find bugs you might not catch by utilizing ordinary unit tests.

This is not a theoretical primer, it’s a hands-on guide built around a minimal, reproducible fuzzing harness you can drop into a workspace and run. In this post we cover: short, pragmatic description of the program surface we will fuzz. 

In addition, we show how to arrange a Rust workspace where the program and fuzz target co-exist, the Cargo.toml essentials, and why Honggfuzz is a good fit for fuzzing of Solana programs. Then we go through a line-by-line explanation of the fuzz target, how we craft randomized instruction data. We see how to catch a crash example and reproduce it.

#### The vault - Test Subject


Pinocchio is a lightweight Rust library for writing Solana on-chain programs with a tiny dependency overhead: it gives you the usual Solana primitives (accounts, entrypoint, instruction deserialization) with a small, auditable footprint that’s convenient for developers. Finally, since pinocchio programs are plain rust with solana primitives, they make excellent targets for rust native fuzzers like Honggfuzz.


Shoutout to `4rjunc`; the Vault implementation used throughout this post was authored by them; thanks for producing a clean, tested codebase we can reason about.


This is a Solana Vault: users send SOL into a freshly derived vault account (PDA) to be held and withdrawn later. The typical flow is: a depositor signs a deposit instruction while a payer pays for the compute cost, the program transfers lamports into the vault PDA, and later an authorized withdrawal moves lamports back out. The code we are most interested in fuzzing lives in `deposit.rs`, specifically the `process_deposit()` function; since it touches transfer invariants, if mishandled, can lead to incorrect balances or lost funds.


Our goal when fuzzing `process_deposit()` is straightforward: ensure the lamport balances of the payer, the depositor account, and the vault PDA remain consistent with the requested transfer amount and program invariants (no unexpected drains, no double-spend, no under/overflows).


Here is the exact snippet we'll target:

#### Setting up the Fuzzing Workspace


Honggfuzz is a high-performance, feedback-driven fuzzer written in C and designed for native binaries, including those built from Rust. It acts smartly by using coverage to learn which execution paths have been explored and mutates future inputs to reach deeper branches of the code. 

Unlike black-box fuzzers, it observes program behavior through compiler-inserted hooks, collects coverage maps, and aggressively evolves inputs to trigger crashes, panics, or unexpected states. Its speed and simplicity make it suited for fuzzing Solana programs.

Our setup is organized into two Rust projects inside a single Cargo workspace:

- `pinocchio_vault` — the main Solana Vault program (our test subject).
- `fuzz_vault` — the fuzzing harness that utilizes Honggfuzz to generate inputs and invoke the functions to be tested.


The outer `Cargo.toml` ties both projects together as workspace members:

The \[workspace\] section simply groups both crates under one coordinated build environment allowing for better organization of rust projects.

Below is the Cargo.toml for our fuzz target:


`pinocchio_vault = { path = "../pinocchio_vault/" }` points directly to the Vault program we’re testing, which the fuzzer will import and execute its logic.


The inclusion of `litesvm` means we’ll be running the fuzzed transactions in a lightweight local Solana virtual machine, perfect for isolated, deterministic execution.


The `[[bin]]` section defines the fuzz target as a binary, making it runnable like any executable rather than a conventional test suite. This is basically what the fuzzer itself requires to run.


You can think of this setup as a “supercharged” unit test built on top of LiteSVM, where Honggfuzz continuously feeds random inputs instead of predefined test cases.

#### Running Honggfuzz

##### Generic Scaffold


With the project structure ready, the next step is wiring up a minimal fuzz target that actually runs from the CLI. At this stage, our goal is not to test anything specific yet, we just want a working setup that Honggfuzz can hook into, feed random bytes, and execute our logic inside an async runtime. This serves as a scaffold for any project.


Below is the scaffold that makes the fuzzing setup work:


At first glance, you realize there are two `main()` functions. Those two functions define how the executable behaves depending on whether the honggfuzz feature is enabled or not. When we build with that feature on, the first `main()` is compiled, and the fuzz! macro takes over the execution flow: it continuously supplies randomized byte slices (data: &\[u8\]) generated by Honggfuzz.

If the feature isn’t enabled, Cargo runs the second `main()` instead which is a lightweight smoke-test that executes a single call with dummy data entered in the body of the function `[1u8;64]`. It’s a quick sanity check that lets you verify your harness runs correctly before letting Honggfuzz hammer it. Think of it as a unit test with specified inputs.


Now, notice the RT static variable defined at the top. This initializes a Tokio runtime, created once and shared across all iterations. Without it, you’d have to spin up a new async runtime for every fuzz case, which would kill performance and stability. Using once\_cell::sync::Lazy ensures that the runtime is built once, reused safely, and torn down only when the process exits. 

The runtime itself is single-threaded `(new_current_thread())`, which is ideal for fuzzing because it avoids nondeterminism caused by concurrency and race conditions. The constant array reference `PROGRAM_BYTECODE` embeds the compiled Vault program (.so file) directly into the fuzzer binary, allowing each fuzz iteration to load and execute the on-chain code locally without relying on an external deployment. In other words the program under test is hardcoded into the fuzzer itself.


The function `run_case(data: &[u8])` is where the real test takes place. It receives the raw bytes from the fuzzer, parses them into structured parameters (like deposit amounts, bumps, or account seeds), and then simulates the deposit flow inside a local execution environment such as LiteSVM. In this section, we fill this function with the logic that drives the Vault’s `process_deposit()` instruction and asserts lamport balances match the expected values.


Returning to the fuzzer’s main() function, we refine it to shape the random input into something meaningful for our test harness:


Here, we start by filtering out any input shorter than 64 bytes for being too short to form valid test parameters. From each fuzzed data slice, we split the first 64 bytes into two fixed-size arrays, `a` and `b`, each 32 bytes long. These values are then passed into `run_case()`, replacing the raw byte slice with two structured inputs that the test logic can interpret as public keys, seeds, or other deterministic parameters. This small transformation makes the fuzzing loop cleaner and the test cases more controlled without undermining randomness.

#### Building the Test Case


Now that things are in place, it’s time to put some actual logic inside our test body. Here’s what it looks like in our setup:

We start by spinning up a lightweight Solana virtual machine LiteSVM giving us a fast sandbox to execute the program bytecode without touching a real network which won't be suitable for a fuzz run. Each fuzz iteration begins with a clean state; this could be improved further but not in scope of this writeup. The Vault program loaded directly from its compiled .so binary, and two random accounts derived from the input seeds `a` and `b`.


The payer and depositor are created using Keypair::from\_seed(), meaning their identities depend entirely on the random bytes Honggfuzz generated. After that, both accounts receive an airdrop of SOL amounts, ensuring they have enough balance to interact with the Vault.


You might wonder why we didn’t let the depositor also act as the payer (i.e., the same address signs and funds the transaction). That’s a perfectly valid, more general test case to include and one worth keeping as a deliberate edge-case (an “easter egg”) that we’ll revisit later in the post to show how these subtle details can change test outcomes.


Next, we include a simple check retrieving the depositor’s account from the VM and asserting that the balance matches what we just airdropped. It’s a minimal test and might be unnecessary to put here but it confirms that the SVM environment behaves predictably before we move on to calling real program instructions like `process_deposit()`.


With accounts in place, the next step is to craft the exact instruction our Vault expects. We begin by deriving the vault PDA using the same seeds the program uses on-chain here, the literal tag "vault" and the depositor’s public key. This yields both the PDA and its bump, which we must echo back in the instruction data so the program can verify that the provided vault matches the derived address.

To keep the payload making sense for us, we define a struct for the deposit parameters: amount (in lamports) and the PDA bump. In this example we send 1 SOL (1\_000\_000\_000 lamports). We then serialize it explicitly: 8 bytes little-endian for the amount, 1 byte for the bump, and 7 bytes of padding. Finally, we prefix the buffer with an instruction discriminator (0u8 here stands for VaultInstruction::Deposit) so the program can route to the correct handler.

With data encoded, we assemble the Solana Instruction. The accounts follow the program’s expectations: the depositor as a signer (source of funds), the vault PDA as the recipient, and the system program for the native lamports transfer. This is exactly what our fuzz harness will invoke via varying seeds to verify final balances.

With the instruction assembled, we package it into a signed transaction and run it through LiteSVM. First we fetch a recent blockhash, build a Message that includes our `deposit_instruction`, and sign with both the payer and depositor since that the depositor authorizes the lamport transfer while payer pays for the gas. Before sending, we snapshot the depositor’s lamports so we can verify the effect on balance after execution.

We then submit the transaction to the SVM and fail fast if anything goes wrong. A successful result means the program accepted our PDA derivation, signature set, serialized DepositData and most importantly the SOL transfer.

Finally, we read back the accounts and assert the core invariant of this post: the lamports that left the depositor must equal what landed in the vault. By recomputing post-state for payer, depositor, and the vault\_pda, we can validate this as a tight equality check, fast, and exactly the kind of property Honggfuzz is good at breaking if anything in `process_deposit()` is off by a dust amount.

This closes the loop: we derive addresses, build the instruction, sign and submit, then verify that expected lamports balances hold.

#### Running the Test Case


With everything in place, we can finally run the fuzzer:


`--features=honggfuzz` enables the fuzzing entrypoint (main() with the fuzz! loop), while `--exit_upon_crash` tells Honggfuzz to stop immediately when it finds the first invariant violation, a helpful setting when you’re still diagnosing root causes instead of collecting many redundant crashes.


When a crash occurs, Honggfuzz saves the bad input under hfuzz\_workspace/fuzz\_vault/SIGABRT.\*.fuzz. You can replay the input later, but it's preferable to inspect it first with `xxd`:


Expected output:


We inspect only the first 64 bytes because this is what affects the test. You can see simply all zeroes. You might be teased to assume that this is because of seed forming address being zero is not allowed but that is not true here. If you want to debug that we can change the second `main()` aiming to reproduce this case:


After `cargo run` we basically treat it as a unit test in which inputs are `payer` and `depositor` addresses derived from a zero seed. Wait a second now you see where this goes , the issue here is that `a` and `b` are equal which results in having the same `depositor` and `payer` addresses. What happens here is that `depositor` not only transfers that `1 SOL` amount to vault, they also pay for that transaction gas cost in SOL, hence the balance deducted is little bit more that `1 SOL`.


So the issue isn’t in the Vault code at all, it is in the test logic, which simply do not account for the edge case we just triggered. That might seem like a mistake from my side, but it is actually a positive sign: it proves the fuzzer is doing its job, detecting real inconsistencies when they appear. In fact, once you see it working, it is worth to deliberately introduce small bugs and watch how the fuzzer hunts them down.


We fold that lesson back into the harness by skipping degenerate inputs where a == b, keeping the fuzzer focused on meaningful cases:


After this adjustment, the harness runs through thousands of iterations without violations; when a real bug surfaces, `--exit_upon_crash` will freeze the first witness so we can root-cause it on the spot. If you ever manage to trigger an invariant violation for that scenario, do not hesitate to ping me about it.

Finally we find out that this first run proves the setup works, the fuzzer sees through edge cases, flags real inconsistencies, and gives us confidence that our Vault logic holds steady under unpredictable inputs.

#### Conclusion


This walkthrough gave us an example of fuzzing a Solana Vault program built with Pinocchio using Honggfuzz. We started from the program structure, built a fuzz harness over LiteSVM, watched Honggfuzz uncover an edge case caused by identical seeds of 32 byte length that is unlikely, and refined the harness until it ran thousands of iterations cleanly, confirming that the setup works and the fuzzer truly executes the program logic.

That said, this example comes with clear limitations. The test setup is repeated for every iteration, meaning each run rebuilds the same initial conditions rather than reusing state between cases. More importantly, because we’re fuzzing against a precompiled `.so` binary not instrumented for coverage, we can not yet measure which parts of the Vault code are being hit. That is a critical piece for deeper analysis.


Future work should focus on adding proper coverage instrumentation to the build process so the fuzzer can report which branches and code paths it explores. Once coverage data is available, we can generate detailed reports, figure out scenarios for unexplored areas, and evolve this harness into a full proper feedback-driven fuzzing workflow for Solana programs.

The full example and harness code are available in the repo: 

[https://github.com/beber89/fuzz-pinocchio-vault-example](https://web.archive.org/web/20260129075903/https://github.com/beber89/fuzz-pinocchio-vault-example)
