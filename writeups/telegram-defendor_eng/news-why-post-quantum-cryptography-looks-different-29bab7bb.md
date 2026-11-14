# 🔐 OpenZeppelin: Why Quantum Risk Isn't Just a Future Problem

- **Source URL:** https://www.openzeppelin.com/news/why-post-quantum-cryptography-looks-different
- **Fetched:** 2026-11-14
- **Channel:** @defendor_eng
- **Telegram message:** https://t.me/defendor_eng/2097 (id 2097)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# From Algebra to Noise: Why Post-Quantum Cryptography Looks Different

- OpenZeppelin Security

Quantum risk is often discussed as if it were a distant cryptography problem: something for standards bodies, researchers, and infrastructure vendors to worry about later. For tokenized finance, that framing is too narrow. If a cryptographically relevant quantum computer (CRQC) becomes available, the first institutional crisis will not be that every hash function immediately fails. It will be that exposed classical public keys — especially those behind wallets, custody systems, bridges, validators, governance executors, and smart-contract admin roles — may become liabilities.

The point is to ask a practical question:

“**If Q-Day arrived sooner than expected, which of your keys, wallets, contracts, bridges, and governance paths would fail first?**”

“**Who should read this?** Executives, risk leaders, custody teams, treasury teams, tokenization platforms, protocol governors, and security leads who need to understand why quantum risk matters operationally before diving into the mathematics.”

## The thesis in one diagram

This diagram is intentionally simple because the first-order risk is simple. Quantum risk does not have to break every component of a blockchain at once. It only needs to turn the wrong exposed public key into a usable private key. Once that happens, the attacker does not merely understand the system better; they may be able to act as an authorized participant inside it.

For on-chain systems, the threat model is especially unforgiving:

“**Expose now, forge later.**

Once a public key is permanently exposed on-chain, a future quantum attacker may be able to recover the corresponding private key and forge authorizations - unless assets and authorities have already migrated.”

That is the blockchain analogue of "harvest now, decrypt later." In confidentiality settings, an attacker records encrypted traffic today and decrypts it in the future. In tokenized finance, the attacker may instead observe exposed public keys today and forge authorizations in the future. The recorded object is not a ciphertext, but an authority-bearing public key.

[A Practical Guide to Quantum Risk in Blockchain](https://www.openzeppelin.com/news/a-practical-guide-to-quantum-risk-in-blockchain) set out this risk and the standards that answer it. What follows goes underneath both: the cryptographic reason exposed keys become recoverable, and what a migration actually costs.

## Classical Crypto Hides Secrets in Algebra

To understand why, we need one central idea:

“Classical public-key cryptography loves clean algebra.”

Technical note: two classical one-way streets.

Non-technical readers can skip this box and keep the main idea: **RSA and elliptic-curve cryptography both rely on operations that are easy in one direction and hard to reverse classically.**

RSA is based on multiplication of large primes:

*N* = *pq*

Given *p* and *q*, computing *N* is easy. Given only *N*, factoring it back into *p* and *q* is believed to be hard for classical computers.

Elliptic-curve cryptography is based on scalar multiplication:

*Q* = *dG*

Given *d* and *G*, computing *Q* is easy. Given *Q* and *G*, recovering *d* is believed to be hard for classical computers.

Most widely used public-key algorithms follow this beautiful design pattern:

1. Choose a mathematical operation that is easy to compute forward.
2. Make the reverse direction infeasible.
3. Use the forward operation to create public keys from a secret.
4. Use the secret as private key to sign, decrypt, or derive shared keys.

This design pattern is elegant, but the elegance is also structure. And Shor's algorithm is a structure detector. This is why the post-quantum transition is not simply "use bigger curves". The old parameters aren’t the problem, but rather the kind of hardness they rely on is the wrong kind against quantum computers.

## Shor's Algorithm: The Structure Detector

Shor's algorithm is often described as "the quantum algorithm that breaks RSA". That is true, but too narrow. The deeper point is:

“Shor's algorithm breaks cryptosystems whose hardness comes from certain kinds of clean algebraic structure.”

It applies to:

- integer factoring,
- finite-field discrete logarithms,
- elliptic-curve discrete logarithms,
- and therefore many public-key systems built from them.

For crypto-native systems, exposed classical public keys become dangerous in a post-quantum world with sufficiently powerful quantum attackers:

exposed elliptic-curve public key → recoverable private key

The full algorithm involves the quantum Fourier transform and period finding. For intuition, the key idea is that Shor turns hidden algebraic regularity into measurable information. Factoring can be reduced to finding a period in modular arithmetic, and discrete logarithms can be viewed as finding hidden structure inside a group. Quantum Fourier techniques are unusually good at extracting this kind of hidden regularity, as they turn algebraic periodicity into something a measurement can read directly.

This is why RSA, DSA, Diffie-Hellman, ECDSA, EdDSA, and pairing-based cryptography all share the same vulnerability: they rest on the algebraic structure Shor was designed to exploit.

Technical note: what "structure" really means here.

Non-technical readers can skip this box and keep the main idea: **"structure is quantumly weak" is a useful heuristic, not a theorem - Shor exploits one very specific kind of structure, and many structured problems resist quantum attack.**

"Shor detects structure" is a metaphor, and its limits matter. There is no theorem - and no real consensus - that structured problems are generically easy for quantum computers. What Shor exploits is narrow: factoring and both flavors of discrete logarithm reduce to finding periodicity in a finite cyclic (abelian) group - the *abelian hidden subgroup problem* - which the quantum Fourier transform solves efficiently. That is a specific property of commutative group structure, not of "algebra" in general.

Plenty of richly structured problems have no known quantum speedup. Graph isomorphism is highly structured yet has no efficient quantum algorithm. And lattice problems themselves can be phrased as a *non-abelian* (dihedral) hidden subgroup problem, where the Fourier technique that defeats factoring does not apply. Lattices are therefore not safe because they lack structure - they are safe because their structure is not the kind Shor's machinery can unlock.

## Grover's Algorithm: The Brute-Force Discount

Grover's algorithm is different. It does not exploit algebraic structure in the same catastrophic way as Shor. Grover weakens brute force search, but does not destroy hashes the way Shor destroys elliptic-curve signatures. If a classical attacker needs about 2*n* steps to search a space, Grover can reduce that to about 2*n*/2. This matters for:

- symmetric-key search,
- hash preimage search,
- some mining-like search processes,
- and brute-force attacks.

But it is not the same as Shor. For a 256-bit hash function preimage-search security degrades from 2256 to 2128. That is a large reduction, but 2128 remains a serious security level:

“Shor finds the secret door. Grover only helps you check doors faster.”

Technical note: why 2*n*/2 overstates Grover's real-world threat.

Non-technical readers can skip this box and keep the main idea: **the headline "halving" is an idealized bound; real quantum search is far costlier - but hash sizing is still an engineering tradeoff, not a solved problem.**

The 2*n*/2 figure is a *query* bound: it counts calls to the function, not wall-clock cost. Three practical facts push the real attack cost much higher:

- **Grover barely parallelizes.** Splitting the search across *P* quantum machines speeds it up only by √*P*, versus the linear *P* that classical brute force enjoys.
- **Quantum gates are slow and the search is sequential.** A Grover attack needs about 2*n*/2 *sequential* iterations on an error-corrected machine, each logical operation far slower than a classical one. For *n* = 256 that sequential depth alone is prohibitive for the foreseeable future.
- **Hardware speed is unknown.** Future clock rates and error-correction overheads are not yet known, so "just double the output" is a rule of thumb, not a guarantee of an exact security level.

These caveats mostly cut in the defender's favor; they are why NIST treats even AES-128 and SHA-256 as far from trivially broken. But they also mean hash sizing is a tradeoff: in the early quantum era most users still run classical hardware, where larger outputs and longer hashes carry real cost.

This is why SHA-256 and Keccak-256 do not need to be thrown away in the same way ECDSA does. They may need larger margins in some contexts, but they are not structurally destroyed by quantum algorithms. Therefore for blockchains, the practical message in the face of Shor and Grover quantum algorithms is:

- signature schemes are the urgent public-key problem,
- hashes are weakened but still usable with adequate parameters,
- symmetric encryption should prefer larger keys such as AES-256 for long-term security,
- and protocol designers should avoid relying on short hash outputs for long-lived high-value commitments.

## From Algebra to Noise

Post-quantum cryptography (PQC) does not solve the problem by choosing a larger elliptic curve. That would still be algebra. Instead, it changes the hiding place. The major post-quantum families hide secrets in "noise":

- noisy linear algebra,
- high-dimensional lattices,
- error-correcting codes,
- and hash-based constructions.

PQC changes the kind of hardness we rely on:

clean algebraic structure → noise, combinatorics, and hashes

That is why post-quantum cryptography looks so different. It is not aesthetically similar to ECC. It has larger keys, larger signatures, more complicated implementation constraints, and more awkward engineering tradeoffs. Those differences are not accidental though - they are the point.

## Learning With Errors and Lattices: Hiding Secrets in Noise

The central intuition behind many modern post-quantum schemes is Learning With Errors, or LWE.

The idea is easy to state. Start with a large system of linear equations in some unknown secret values - the kind of system you learned to solve in school by elimination and substitution. On its own such a system is easy: given enough equations, ordinary linear algebra recovers the secret quickly. LWE takes this easy problem and deliberately breaks it. To each equation it adds a small, random error: a little nudge that leaves every equation only *almost* correct. Publicly, an attacker sees the equations (a public table of coefficients together with their slightly-off results) and knows the typical size of the errors, but never sees the secret or the exact errors that were added. The secret is now buried inside a haystack of nearly-correct equations, and recovering it becomes, as far as anyone knows, intractable for both classical and quantum computers.

Technical note: the LWE equation.

Non-technical readers can skip this box and keep the main idea: **lattice cryptography makes recovery hard by adding carefully controlled noise to otherwise solvable equations**.

A simplified LWE equation looks like this:

*b* = *As* + *e* (mod *q*)

where:

- *A* ∈ ℤ*qm*×*n* is a public matrix whose entries are sampled modulo *q* - a large public table of coefficients;
- *s* ∈ ℤ*qn* is the secret vector (secret key);
- *e* is a small error/noise vector;
- *b* ∈ ℤ*qm* is a public vector computed as *b* = *As* + *e* (mod *q*);
- and the attacker sees (*A*, *b*) and knows how *e* is sampled (its distribution), but does not see the actual *s* or *e*.

If there were no noise, we would have:

*b* = *As* (mod *q*)

and recovering *s* would be a linear-algebra problem. The noise changes everything.

Recovering *s* means solving a linear system, and this can be done efficiently using, for example, Gaussian elimination. But with noise, that approach breaks down. As we solve the system, we have to divide by the coefficients of *A*, and since its entries are random, these coefficients can be large, causing them to amplify the error when we multiply through. As a result, any approximate solution we find may be far from the true one.

More precisely: suppose *b* = *As*′, where *s*′ is an approximate solution. Subtracting both sides from the true equation and multiplying by the inverse of *A* (for simplicity, assume A is a square matrix and since its entries are random, it is invertible with high probability, though the general case is similar) gives:

*s*′ − *s* = *A*−1*e*

Even if the noise vector *e* is small, multiplying by *A*−1 can make the difference *s*′ − *s* large.

It is worth being precise about what noise actually breaks. The linear algebra itself does not stop working: a random square system is almost surely invertible, so the equations still have a unique exact solution - it simply is not the secret. Solving *As*′ = *b* as if it were exact returns *s*′ = *s* + *A*−1*e*, and because *A* is random, *A*−1*e* is typically large modulo *q*, throwing *s*′ far from the true *s*. The secret itself stays well-defined - with enough samples it is the unique solution whose error vector is small - but the fast exact-arithmetic method no longer finds it, and no efficient method is known to. What noise destroys is efficient recovery, not the underlying algebra.

Each equation is only almost correct: it is slightly off, perturbed by a small noise term. Remarkably, the whole collection of these noisy equations is believed to be computationally indistinguishable from equations whose results are entirely random, meaning it reveals no useful information about the secret. This property can be used directly for encryption: for example, one can encrypt a message simply by adding it to one of these "random-looking" results.

Now, to get a feel for why even a tiny amount of noise changes the picture so dramatically, consider the simplest possible case where the error added to each equation takes only the values 0 or 1, each with nonzero probability. Then every single equation actually corresponds to two possible equations: one where the error is 0 and one where it is 1. This means that for a system of *m* equations, there are 2*m* possible underlying systems consistent with what you observe, and since the number of equations *m* in practice grows with the security parameter, the number of possibilities explodes exponentially. The attacker has no efficient way to determine which combination of noise values was actually used, and so the system remains secure.

This is the leap from algebra to noise.

But where do *lattices* come in? Picture all the results the noise-free equations could produce as the secret ranges over its possible values. They do not fill space smoothly; they land on a perfectly regular grid of points - a *lattice*, the higher-dimensional cousin of the evenly spaced dots on a sheet of graph paper. The true, noise-free answer sits exactly on a lattice point. Adding the small error nudges what the attacker actually observes slightly *off* that grid point. So recovering the secret is the same as taking the observed, off-grid point and finding the lattice point nearest to it.

That is a famous, well-studied geometric problem - the *closest vector problem* - and in high dimensions it is believed to be hard for classical and quantum computers alike. This is the bedrock the security rests on: LWE is just a convenient, randomized way of dressing up a hard lattice problem. "Adding noise to equations" and "landing just off a grid point" are two descriptions of the same thing - which is why this whole family is called *lattice cryptography*.

Another way to understand the appeal of lattice-based cryptography is to put it side by side with the classical schemes - both how it looks and how its hardness is grounded.

Technical note: classical vs. lattice hardness, side by side.

Non-technical readers can skip this box and keep the main idea: **the old world hides secrets in clean algebra that quantum computers can unravel; the new world hides them in noisy lattice problems that have a stronger worst-case hardness story and no known quantum shortcut.**

Classical ECC hides the secret in a clean algebraic operation:

*Q* = *dG*

Lattice cryptography hides it in noisy relations:

*b* = *As* + *e* (mod *q*)

The first is elegant and algebraic; the second is messy on purpose. That difference runs deeper than appearance - all the way down to complexity theory.

Factoring and the discrete logarithm have resisted classical attacks for decades, but they are not known to be NP-hard and are not believed to be NP-complete. They occupy a somewhat unusual middle ground: hard enough that no efficient classical algorithm is known, yet not "complete" for the whole class of efficiently verifiable problems. It remains conceivable that a clever classical algorithm could one day solve them efficiently - and on a quantum computer Shor's algorithm already does, precisely by exploiting their hidden algebraic structure.

Lattice problems have a different complexity-theoretic flavor. The Shortest Vector Problem (SVP) asks for a shortest nonzero vector in a lattice, and SVP - along with related problems - is known to be NP-hard in its exact form and for small approximation factors. The approximation factors that cryptography actually relies on are much larger, and in that regime the problems are not believed to be NP-hard; so this is evidence of robustness, not a proof of security. What matters more for cryptography is that the security of LWE is tied, through worst-case-to-average-case reductions, to the hardness of approximate lattice problems such as GapSVP and SIVP: an efficient solver for *random* LWE instances would yield an efficient solver for those lattice problems in the worst case.

This does not make LWE "proven secure", nor is breaking a concrete NIST parameter set literally the same as solving an NP-complete problem. But it does anchor lattice cryptography in a family of problems with a far stronger worst-case hardness story than factoring or discrete logarithms. The gap may even be partly classical, not only quantum: the best known classical algorithms for LWE at cryptographic parameters run in essentially exponential time, whereas factoring enjoys sub-exponential ones - so LWE may be harder than factoring on ordinary computers too, before any quantum speedup enters the picture.

The high-level intuition is this: Shor's algorithm needs clean algebraic structure to exploit - exactly the structure RSA and elliptic-curve cryptography rely on. Lattice cryptography instead rests on noisy, high-dimensional geometric problems; they still have structure, especially in their efficient variants, but it is combined with noise in a way that currently resists known classical and quantum attacks, with no Shor-like quantum shortcut in sight. That is one reason lattices became the main foundation for NIST's post-quantum standards. It does not mean LWE is unconditionally secure, but rather that no efficient Shor-like quantum algorithm is known for solving the LWE-type problems underlying NIST's lattice standards at their chosen parameters.

This is the practical meaning of "quantum-resistant".

## NIST PQC: The Replacement Toolbox

After a multi-year standardization process, NIST finalized its first post-quantum cryptography standards in August 2024:

- **FIPS 203: ML-KEM**, based on CRYSTALS-Kyber,
- **FIPS 204: ML-DSA**, based on CRYSTALS-Dilithium,
- **FIPS 205: SLH-DSA**, based on SPHINCS+.

NIST has also selected Falcon for future standardization under the name **FN-DSA**, and HQC as an additional post-quantum KEM. The standards are not interchangeable. They solve different problems.

## High-level Overview of NIST's PQC Standards

### ML-KEM: Replacing Diffie-Hellman-Style Key Establishment

ML-KEM is a key encapsulation mechanism. It does not directly replace ECDSA wallet signatures. It replaces key-establishment mechanisms such as Diffie-Hellman-style exchanges. At a high level:

1. A receiver publishes a public key.
2. A sender uses that public key to encapsulate a fresh randomly generated shared secret, producing a ciphertext.
3. The receiver uses the secret key to decapsulate the same shared secret from the ciphertext.

Technical note: KEM notation.

Non-technical readers can skip this box and keep the main idea: **ML-KEM lets two parties arrive at the same shared secret without using quantum-vulnerable Diffie-Hellman**.

Conceptually:

(*c*, *K*) = Encaps(*pk*)

and:

*K* = Decaps(*sk*, *c*)

where:

- *pk* is the public key,
- *sk* is the secret key,
- *c* is the ciphertext sent to the receiver,
- *K* is the shared secret.

Note that, unlike general public-key encryption where the sender chooses the message, here the sender does not choose *K*: it is sampled randomly inside Encaps, which returns the pair (*c*, *K*) as local outputs to the sender. Only the ciphertext *c* is sent over the wire - the secret *K* is never transmitted. The receiver does not read *K* out of *c* directly; instead, *c* encapsulates the randomness that determined *K*, and running Decaps with the secret key *sk* reconstructs the very same *K*. An eavesdropper who captures *c* but lacks *sk* cannot recover *K*.

More precisely, *K* is not the raw randomness itself but a hash of it (together with *c*), and Decaps re-encrypts its recovered value and checks it against *c* before deriving *K*. This is the Fujisaki-Okamoto transform, and it is what hardens the scheme against attackers who submit malformed ciphertexts to probe the secret key.

Engineering intuition:

“ML-KEM is what you use when two systems need to agree on a secret in a quantum-resistant way.”

Institutionally, ML-KEM matters for secure channels: TLS-like connections, custody backend communication, VPNs, confidential APIs, and secure service-to-service messaging. In onchain terms, ML-KEM is not the main answer to "how do we replace ECDSA wallets?", but is rather the answer to:

“How do our systems establish encrypted channels without relying on quantum-vulnerable Diffie-Hellman?”

### ML-DSA: The Practical Lattice Signature Workhorse

ML-DSA is NIST's lattice-based digital signature standard, derived from CRYSTALS-Dilithium. It is one of the main candidates for replacing classical digital signatures in general-purpose systems. A useful high-level analogy is [Schnorr signatures](https://en.wikipedia.org/wiki/Schnorr_signature), but over lattice relations rather than elliptic-curve groups. ML-DSA follows the same commit-challenge-respond rhythm as Schnorr-like signatures, but the arithmetic lives in lattice/module structures, and the security relies on lattice assumptions rather than discrete logarithms. Think of it as:

“Instead of proving knowledge of a secret scalar behind an elliptic-curve public key, the signer proves knowledge of short secret information consistent with public lattice data.”

ML-DSA has larger signatures and public keys than ECDSA or EdDSA, but it is designed to be practical and comparatively robust among post-quantum signature schemes. Engineering intuition:

“ML-DSA is what you use when you need a general-purpose post-quantum signature and can absorb the size cost.”

Institutionally, it is the general-purpose post-quantum signature workhorse for software signing, credentials, document signing, API authentication, and approval workflows where size constraints are manageable. For blockchain systems, the key challenge is not simply whether ML-DSA is secure, but

“can we afford to verify it and carry its signatures inside the protocol?”

That depends on the execution environment, gas model, calldata cost, and whether verification can be optimized, aggregated, or moved off-chain.

### SLH-DSA: The Conservative Hash-Based Backup

SLH-DSA is based on SPHINCS+, a stateless hash-based signature scheme. Its philosophical appeal is simple:

“If we trust hash functions, we can build signatures from hashes.”

Hash-based signatures use one-time or few-time signing components and organize them with Merkle-tree-like structures. Instead of relying on lattices or number theory, they rely on hash-function properties such as preimage resistance and collision resistance. As an analogy:

“Imagine a huge book of single-use wax seals. Each seal can authorize one message. A hash tree lets the verifier check that a given seal belongs to the official book without storing the whole book.”

SLH-DSA is attractive because it is mathematically conservative. It is also expensive:

- signatures are large,
- signing and verification are heavier,
- and many blockchain environments will find it costly.

So SLH-DSA is not necessarily the most convenient blockchain signature scheme. But if lattice assumptions were ever weakened, hash-based signatures provide algorithmic diversity. From an engineering perspective:

“SLH-DSA is what you use when you want hash-based conservatism for keys you rarely touch.”

Institutionally, SLH-DSA is best viewed as a conservative backup for rare but high-value operations: root certificates, long-term offline keys, emergency authorization keys, and backup trust anchors.

### Falcon / FN-DSA: Compact but Delicate

Falcon is another lattice-based signature scheme selected by NIST for future standardization under the name FN-DSA. Its main attraction is compactness. Compared with ML-DSA, Falcon signatures are much smaller. That matters for environments where bandwidth, calldata, storage, and verification footprint are expensive. This naturally makes Falcon interesting for blockchains. Falcon achieves compactness using more delicate machinery, including lattice Gaussian sampling, so secure implementation is more subtle. This does not mean Falcon is bad. It means that its engineering risk profile differs from ML-DSA:

“Falcon is what you use when signature size matters more than implementation simplicity.”

For auditors, the relevant questions are:

- Is the sampler implemented correctly?
- Is it constant-time?
- Are there side-channel risks?
- Are floating-point or precision issues avoided or controlled?
- Is the implementation using a well-reviewed library?
- Are randomness and fault attacks considered?

In a blockchain context, Falcon's compactness may be appealing, but implementation fragility must be taken seriously.

This is not hypothetical. Working with OpenZeppelin, Starknet has deployed Cairo account contracts that verify Falcon-512 signatures, and a spec-compliant Falcon-512 account has already executed a live transfer on Mainnet.

### HQC: Code-Based Diversity

HQC is a code-based key encapsulation mechanism selected by NIST as an additional post-quantum encryption/KEM algorithm. Its role is the same as ML-KEM and is added for diversity. Lattices are currently the dominant practical PQC family, but cryptographic monocultures are dangerous. If a major breakthrough weakened lattice assumptions, systems relying exclusively on lattice cryptography would face correlated risk. Code-based cryptography uses a different kind of hardness. Very roughly, it hides secrets in error-correcting-code problems. Error-correcting codes are normally used to recover messages from noise. Code-based cryptography turns that idea around:

“The noise becomes the lock.”

This mirrors the lesson from LWE: where lattice cryptography buries the secret by adding noise to otherwise-solvable equations, code-based cryptography buries the message inside a deliberate error pattern that only the legitimate structure can decode.

“HQC is what you choose when you want algorithmic diversity alongside lattice-based KEMs.”

HQC is relevant to institutions because it gives backup diversity for key establishment.

## What to do next

Map the NIST toolbox to your own stack. The first question is not "which algorithm wins?" - it is "where does each tool actually fit?" A practical first step is to walk through four categories of cryptographic use and identify the candidates that match each one:

1. **Key establishment.** Where do you currently rely on Diffie-Hellman-style exchanges - TLS connections, custody backend communication, VPNs, internal APIs, service-to-service messaging? These are ML-KEM candidates, with HQC available for algorithmic diversity.
2. **General-purpose signatures.** Where do you sign software, firmware, credentials, documents, or off-chain approval workflows? These are ML-DSA candidates, where size constraints are usually manageable.
3. **Trust anchors and emergency keys.** Where do you keep long-term offline keys, root certificates, or rarely-used recovery paths? These are SLH-DSA candidates, where mathematical conservatism matters more than signature size.
4. **Compact signatures.** Where is signature size or calldata genuinely scarce - typically on-chain verification or bandwidth-constrained environments? These are Falcon/FN-DSA candidates, with appropriate scrutiny of sampler correctness and side-channel exposure.

This mapping is the input to a migration plan, not the plan itself.

## What This Means for Blockchain and Onchain Systems

### Costs in Blockchain Terms

If the substitution were free, this conversation would be over. It is not free. The costs are concrete and worth quoting to your engineering and operations teams.

**Signature size.** A raw secp256k1 ECDSA signature is measured in tens of bytes. ML-DSA signatures are measured in kilobytes. FN-DSA/Falcon is more compact once standardized, but harder to implement safely. SLH-DSA signatures can be much larger still, reaching tens of kilobytes depending on parameters. On a chain where every byte of every transaction is paid for and stored forever, this moves from implementation detail to full redesign.

| Scheme | Signature size | Blockchain implication | 
|---|---|---|
| ECDSA / secp256k1 | Tens of bytes | Cheap and deeply optimized | 
| ML-DSA | Low single-digit kilobytes | Calldata and verification become material costs | 
| Falcon / FN-DSA | Sub-kilobyte | Compact, but implementation-sensitive | 
| SLH-DSA | Tens of kilobytes | Conservative, but expensive for frequent on-chain use | 

**Verification cost.** Lattice signature verification is computationally heavier than ECDSA verification. On-chain verification, already expensive in gas, becomes substantially more so.

**Public key size.** ML-DSA public keys are roughly 1.3 KB versus 33 bytes for compressed secp256k1. For account-abstraction wallets that store keys on-chain, this matters.

**The on-chain-forever problem.** Every signature, every public key, every transaction is recorded permanently. A migration is not "switch over and move on." Old addresses with funds remain exposed forever unless their funds are moved to new, post-quantum addresses *before* a cryptographically relevant quantum computer exists. For signatures, the better phrase is *expose-now-forge-later*: once a public key is permanently exposed on-chain, a future quantum attacker may be able to recover the corresponding private key and forge authorizations unless the assets and authorities have already migrated.

**No drop-in replacement.** Bitcoin and Ethereum both face open governance questions about *which* PQC signature scheme to adopt, how to handle account migration, whether to use STARK-style aggregation, and how to subsidize the transition. There is no consensus today. Institutions cannot wait for one.

Some migration paths will be ugly. Immutable contracts may not be able to change verification logic. Old EOAs and forgotten UTXOs may never move. Assets controlled by exposed keys may require expensive coordination, governance intervention, or emergency migration mechanisms. Post-quantum readiness is therefore not only about choosing a new signature scheme; it is about knowing which parts of the system can actually move.

### The Protocol-Level Dependency

There is a ceiling on what any single institution can do alone. The signature scheme that secures base-layer transactions - elliptic-curve signatures over secp256k1 on both Bitcoin and Ethereum - is fixed by protocol consensus, not by individual wallet owners. No institution can unilaterally teach the base layer to verify a post-quantum signature on an ordinary externally owned account or UTXO. That requires a protocol-level change: new signature-verification logic at the base layer, plus a sanctioned process for migrating existing addresses onto it.

This bounds everything else in this playbook. Inventory, classification, crypto-agility, and hybrid modules are necessary, but they are not sufficient. On a programmable chain an institution has real agency - it can move value into a smart-contract account whose own logic enforces post-quantum verification, without waiting for a fork. But two things stay outside any single institution's control:

- **Already-exposed base-layer keys.** Funds in an exposed EOA, or in a UTXO whose public key is already exposed, cannot be retrofitted with post-quantum protection; they can only be *moved* to a safer destination before Q-Day. If the owner is gone, the keys are lost, or the assets are immobilized, no institutional process recovers them.
- **The base-layer signing scheme itself.** Until the protocol offers post-quantum transaction signing and an address-migration path, every plain EOA and UTXO remains structurally exposed - including those of the counterparties, custodians, and bridges an institution depends on.

This is a systemic, coordination-bound risk, not a per-institution one. It is also why protocol-level efforts - Bitcoin proposals for new address and opcode formats, and Ethereum work such as LeanSig and the Lean Ethereum direction - matter as much as anything on an institution's own checklist. An institution should track that work and support it where it can, because its own migration ultimately depends on it.

## Platform-Specific Considerations

### Ethereum: Why Account Abstraction Matters

Ethereum may have one major advantage in a post-quantum migration: programmability. Smart-contract wallets and account abstraction can allow different verification logic. Instead of being permanently tied to one signature scheme, an account can potentially upgrade or support multiple schemes. This makes hybrid signatures, staged migration, quantum-safe authorization modules, off-chain proof systems, and contract-level policy enforcement possible. Crucially, it makes social recovery available as a fallback when on-chain keys cannot move quickly enough.

During migration, systems can require both old and new cryptographic checks. That's captured by hybrid signatures, which require both:

ECDSA signature + post-quantum signature

before accepting an operation. This is especially useful during transition periods. If the PQ scheme later has problems, the classical scheme still helps. If the classical scheme becomes quantum-vulnerable, the PQ scheme helps. But hybrid systems are not free: they increase signature size and verification cost, complicate wallet UX, and create new failure modes.

For Ethereum, the long-term challenge is not only choosing a PQ signature scheme. It is making the account system, wallet ecosystem, and contract layer agile enough to survive cryptographic change. Further note that while account abstraction helps future wallets and migration paths, it does not automatically save old EOAs whose public keys are already exposed and whose assets remain unmoved.

### Bitcoin: Why Consensus and UTXOs Make Migration Different

Bitcoin's situation is different from Ethereum's. Its UTXO model can delay public-key exposure, but its consensus model makes coordinated migration deliberately hard. Migration questions include new address formats, new script capabilities, new signature verification opcodes, handling already exposed public keys, incentivizing users to move old coins, and avoiding chaos during a quantum emergency.

That is a feature for stability, but a challenge for cryptographic agility. Ethereum's programmability is a migration advantage; Bitcoin's stability is a migration constraint. Both will need to migrate, but the playbooks will differ.

Ethereum consensus currently uses BLS signatures, which are pairing-based and therefore not post-quantum secure. This motivates research into post-quantum consensus signatures and aggregation-friendly alternatives. This is where Ethereum-specific work such as [LeanSig](https://registry.projecteleven.com/algorithms/leansig) becomes important.

### LeanSig and Blockchain-Specific PQ Signatures

NIST standards are general-purpose. Blockchains are not general-purpose environments. They meter bytes, verification time, state, calldata, aggregation, and consensus overhead. This motivates blockchain-specific post-quantum signature research, including LeanSig and related work in the Lean Ethereum direction. The basic motivation is:

“Ethereum does not merely need a post-quantum signature. It needs a post-quantum signature system that fits consensus, aggregation, verification, and blockchain economics.”

LeanSig is especially interesting because it is designed with Ethereum's post-quantum consensus needs in mind, rather than as a general-purpose internet standard. LeanSig should be treated as early-stage research rather than a production-ready replacement for standardized post-quantum signatures. For a broad institutional audience, the key takeaway is:

“NIST standards are the foundation, but blockchain deployments may need protocol-level adaptations beyond what general-purpose standards provide.”

This is not unusual. Classical cryptography also looks different when adapted to blockchains. The same will be true for PQC.

## What Your Team Should Start Doing in 2026

The reason to think about this now, in 2026, rather than in 2032, is that quantum-safe migration on a blockchain is not an upgrade, it is a key rotation across every address that holds value. Doing it under immediate danger is doing it badly. Below we list the minimum steps for a proactive defense approach that your institution should consider today.

### 1. Build a cryptographic asset inventory

Institutions should know exactly where they use classical signature schemes (ECDSA, EdDSA, RSA, BLS), classical key exchange, TLS and SSH certificates, pairing-based cryptography, smart-contract signature verification, and privileged off-chain approval keys. You cannot migrate what you have not inventoried.

### 2. Classify public-key exposure

For each wallet or key, classify:

| Category | Meaning | 
|---|---|
| Hidden public key | Lower immediate quantum exposure | 
| Exposed public key | Vulnerable once cryptographically relevant quantum computer exists | 
| Reused signer | High risk | 
| Long-lived admin key | Critical risk | 
| Upgradeable contract wallet | Migration candidate | 
| Immutable verifier | Hard migration problem | 

### 3. Identify authority concentration

Find keys that control treasuries, bridges, mints, burns, pauses, upgrades, governance execution, validators, oracle feeds, or custody withdrawals. These are quantum high-value targets.

### 4. Introduce crypto-agility

Systems should be designed so that algorithms can be changed without full architectural replacement. Abstract signature verification, hybrid-signature support, upgradeable wallet modules, configurable key policies, versioned address formats, and explicit migration windows are all parts of that pattern.

### 5. Test hybrid modes

Hybrid systems combine classical and post-quantum mechanisms, so that both have to fail for the system to fail. For signatures:

Accept ⇔ Verifyclassical = 1 and VerifyPQ = 1

For key establishment:

*K* = *H*(*K*classical ‖ *K*PQ)

The idea is defense in depth during transition.

### 6. Conduct security audits of post-quantum implementations differently

PQC introduces new failure modes. PQC implementation risk is not limited to Falcon: lattice schemes more generally introduce side-channel, randomness, rejection-sampling, invalid-input, and fault-injection considerations. For lattice schemes, the highest-impact failure modes are side-channel resistance, randomness quality, and invalid-input handling. For hash-based signatures, the priorities are domain separation, parameter selection, and signature-size budgeting. For Falcon-like signatures, the priorities are Gaussian-sampler correctness, constant-time implementation, and side-channel leakage.

### 7. Prepare governance and communication

A PQ migration is not only technical. It touches legal risk, regulatory disclosures, customer communication, custody agreements, insurance, board-level risk governance, and incident response. An institution that waits until Q-Day will not be migrating cryptography, but will be managing a crisis.

## What Security Auditors Should Ask Now

A post-quantum security audit should begin with a small set of concrete questions:

| Area | Question | 
|---|---|
| Wallets | Which signature schemes authorize asset movement? | 
| Exposure | Which public keys are already exposed? | 
| Authority | Which keys control upgrades, pauses, mints, burns, withdrawals, or governance execution? | 
| Bridges | Are validator, committee, or multisig signatures quantum-vulnerable? | 
| Custody | Can signing keys rotate without operational disruption? | 
| Contracts | Can signature verification logic be upgraded or replaced? | 
| Infrastructure | Are TLS, SSH, API, and internal approval systems PQ-ready or hybrid-ready? | 
| Dependencies | Are post-quantum candidates standardized, experimental, or blockchain-specific? | 
| Diversity | Has the organization considered algorithmic diversity? | 
| Migration | Is there a documented and tested post-quantum migration plan? | 

The purpose of these questions is prioritization, rather than panic.

## Conclusion: Crypto-Agility Before Q-Day

The post-quantum transition is not a routine cryptographic upgrade. For tokenized finance, it is a migration of authority before exposed public keys become operational liabilities. The systems most at risk are not necessarily the ones with the most elegant cryptography, but the ones where exposed classical public keys control assets, bridges, mints, burns, upgrades, validators, or governance execution. The exact arrival date of a cryptographically relevant quantum computer is uncertain, but that is the wrong question to fixate on. The exposure map can be built today. The right question is:

"If it arrived sooner than expected, which of our keys, contracts, wallets, bridges, and governance paths would fail first?"

That question should be answered before Q-Day, not during it.

## FAQs

## What is the "expose-now, forge-later" risk in blockchain?

It's the onchain analogue of harvest-now-decrypt-later. Once a public key is exposed on a blockchain, a future quantum computer may be able to derive the private key and forge authorizations, unless the assets tied to that key have already migrated to a quantum-safe address.

## Does quantum computing break blockchain hash functions like SHA-256?

No. Grover's algorithm only weakens hash-based search (roughly halving effective bit security), while Shor's algorithm is what breaks the algebraic structure behind signature schemes like ECDSA. A 256-bit hash still retains strong effective security against Grover.

## Which NIST post-quantum standards apply to blockchain systems?

ML-KEM (FIPS 203) replaces Diffie-Hellman-style key establishment, ML-DSA (FIPS 204) is the general-purpose lattice signature standard, and SLH-DSA (FIPS 205) is a conservative hash-based signature scheme for high-value or rarely-used keys. Falcon (FN-DSA) and HQC are additional NIST selections offering compactness and code-based diversity, respectively.

## Why can't institutions just wait for Bitcoin or Ethereum to upgrade their base-layer cryptography?

Base-layer signature schemes are fixed by protocol consensus, not individual wallet owners. Already-exposed keys cannot be retrofitted; they can only be moved to safer destinations before a cryptographically relevant quantum computer exists. Institutions need their own migration and inventory work regardless of protocol-level timelines.

## What should an institution's post-quantum audit actually check?

A post-quantum security audit should map which signature schemes authorize asset movement, which public keys are already exposed, which keys control upgrades or governance execution, whether bridge and custody signatures are quantum-vulnerable, and whether a tested migration plan exists.

## Why is Ethereum's account abstraction relevant to post-quantum migration?

Smart-contract wallets let an account enforce custom verification logic, including hybrid signatures that require both a classical and a post-quantum check to pass. This allows staged migration without waiting for a protocol fork, though it doesn't retroactively protect old EOAs with already-exposed keys.
