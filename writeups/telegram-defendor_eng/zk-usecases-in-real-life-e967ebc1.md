# 🔐 Zero-Knowledge Proofs in Real Life: Privacy Beyond Blockchain

- **Source URL:** https://hexens.io/blog/zk-usecases-in-real-life
- **Fetched:** 2026-11-12
- **Channel:** @defendor_eng
- **Telegram message:** https://t.me/defendor_eng/203 (id 203)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
Zero Knowledge

Oct 2, 2025

### A Comparison of zkVM DSLs: Halo2, Zirgen, and Plonky3

Deep dive into ZK constraint systems: Halo2's PLONKish circuits, Zirgen's STARK compiler, and Plonky3's direct AIR authoring. Complete with Fibonacci examples.

Jun 24, 2025

When most people hear about zero-knowledge proofs (ZKPs), they think of crypto wallets and blockchain rollups. But ZKPs are quietly powering a new class of privacy-first applications — in everything from AI to cloud infrastructure — far outside the Web3 bubble.

At their core, ZKPs allow one party to prove a statement is true **without revealing why it's true**. That sounds abstract — but in practice, it means you can prove your age without showing your ID, prove a machine learning result without revealing the input, or verify the security of a remote server **without trusting the company that runs it**.

In this article, we’ll explore how ZKPs are being used in real-world systems by major players like:

- **Google**, which uses ZKPs in Wallet to verify **age and ID** without exposing personal details
- **Cloudflare**, which leverages ZKPs for **private web attestation**, proving a browser’s state without leaking user data
- **EZKL**, an open-source zkML toolkit for **privacy-preserving machine learning**
- **TikTok’s privacy innovation team**, which is building a **trustless remote attestation system** for TEEs using ZKPs

Each project shows a different face of what zero-knowledge can do — not just as a tool for financial anonymity, but as a fundamental building block for a more private, verifiable, and user-respecting internet.

Proving sensitive attributes (like “age ≥ 18”) can be a privacy minefield. Traditional approaches suffer from:

- **Data Breaches:** Uploading a driver’s license photo exposes your full identity to any server breach.
- **Tracking via Attestation Keys:** MDOC-style mobile IDs rely on hardware keys for anti-replay, but those same keys can be used to fingerprint and track you across sites.
- **Legacy Hardware & Compatibility:** Many older phones and security keys don’t support modern anonymous-credential schemes (e.g. Idemix, CL-signatures) without firmware updates—leaving users stuck on insecure methods or excluded entirely.

Google’s “Anonymous Credentials from ECDSA” addresses all of the above: it uses the ubiquitous ECDSA hardware interface for broad compatibility, yet delivers true anonymity and zero-knowledge.

When you ask Google Wallet to prove an attribute—say, “age ≥ 18”—it actually constructs a complex statement and then runs two layers of zero-knowledge proofs (sumcheck + Ligero) over that statement. Here’s how it breaks down:

1. **MDOC Transcript Components**
An MDOC (Mobile Driver’s License) proof produces a transcript containing:
  - **Signature 1 (`sig_1`)**: an ECDSA signature by the issuing authority (e.g. DMV) on a hash of the credential data.
  - **Public Attribute Preimage**: a field in the MDL like ```
MDL["valueDigests"]["org.iso.18013.5.1"]["age_over_18"] = True
```
Together with a random **nonce**, this is hashed to produce
$$
h_2 = \mathrm{SHA256}(\mathrm{nonce}\,\|\,\text{"age\_over\_18"}\,\|\,\text{"True"})\,,
$$
proving the attribute without revealing the birthdate itself.
  - **Signature 2 (`sig_2`)**: an ECDSA signature by the device’s hardware key on the server’s challenge transcript, preventing replay.
  - **Validity Range**: two timestamps `time_start` and `time_end`, checked so
`time_start < time_now < time_end`
2. **Sumcheck Prover**
  - The wallet runs the interactive **sumcheck protocol** to convince a (virtual) verifier that indeed the two ECDSA verifications, the SHA-256 preimage check, and the timestamp range check pass.
3. **Non-Interactive Ligero Wrap**
  - After sumcheck, the wallet runs the **Ligero prover** to generate a zero-knowledge proof that the **sumcheck transcript** would be accepted by the sumcheck verifier.
  - The resulting proof is **succinct** and reveals *only* that all checks passed, without exposing `sig_1`, `sig_2`, the nonce, or any other internal data.

By composing sumcheck with Ligero (a technique borrowed from the latest ZK research), Google Wallet delivers **hardware-level security**, **freshness**, and **true anonymity** in a proof that your attribute (e.g. “age ≥ 18”) is valid—without ever leaking your ID, device key, or biometric data.

Cloudflare is reimagining how we prove we're real people on the internet — not with CAPTCHA puzzles or user accounts, but with **hardware-backed proofs** that respect privacy.

Traditionally, websites use **WebAuthn attestation** to verify a user's hardware key (like a YubiKey). This attestation proves the key is authentic and issued by a trusted manufacturer, using a digital signature and a certificate chain. But there’s a privacy catch: the attestation leaks metadata — like the key’s make and model — which can be combined with other browser signals to help fingerprint users.

Even though WebAuthn was designed with privacy policies in mind, Cloudflare wanted to go further. Their goal: **verify that a user holds a trusted hardware key — without learning anything else about it.**

All they really need is a binary answer: **“Is this a real, uncompromised security key?”** They don’t care who made it, what model it is, or how many others like it exist.

Cloudflare designed a custom **zero-knowledge proof (ZKP) protocol** to do exactly that.

Instead of sending the raw attestation signature (which reveals metadata), the browser constructs a ZKP that **proves**:

- The signature was generated by a key from a trusted list (e.g. certified by FIDO), and
- The signature is valid for the message sent by the server

All of this is proven without revealing which key it was. The server learns nothing except: “Yes, a valid, trustworthy key signed this.”

In the protocol, we needed to express elliptic-curve operations as arithmetic constraints inside a zero-knowledge proof. Standard curves like P-256 are defined over a prime field $\mathbb{F}_p$ whose group order $r$ is *different* from $p$. That mismatch creates a major headache:
Group operations (point addition, scalar multiplication) happen modulo the group order $r$. Field operations (add/mul of coordinates) happen modulo the prime $p$.

In a ZK circuit, mixing two moduli means building separate constraint gadgets for modular reduction by $r$ and by $p$, roughly doubling the complexity.

To avoid this, the team set out to **engineer new curves** (nicknamed **Tom curves**) such that the group order of the new curve matches the base field size of the original one. This makes it so that all the arithmetic happens in the same field $F_p$

In practice, generating a Tom curve meant:

1. **Start from the ECDSA Field**
Let $p$ be the prime modulus of the existing ECDSA curve (e.g. P-256’s field prime). Its group order is some other prime $r$.
2. **Search for a Curve Over $\mathbb{F}_q$ with Order $p$**
Find coefficients $a,b$ such that the curve
$E':\; y^2 = x^3 + a\,x + b \quad\text{over }\mathbb{F}_q$
satisfies
$\#E'(\mathbb{F}_q) \;=\; p.$

By reversing the usual design — fixing the order first, then finding the curve — the team unlocked a dramatically more efficient ZK-friendly elliptic curve that powers zkAttest’s high-performance proofs.

1. **Ring Setup**
A**public** ring of trusted attestation public keys
$R = \{\,pk_1, pk_2, \dots, pk_n\}$
representing all hardware keys certified by FIDO (Fast IDentity Online).
2. **Commit to Your Key** The prover holds $(sk, pk)$ where $pk \in R$. They sample randomness $r$ and compute a Pedersen commitment (using group generators $G, H$):
$C_{pk} = pkG + rH$
3. **Produce a Signature** Using ECDSA, the device signs the server’s challenge $m$, yielding $\sigma = (r, s)$.
4. **Generate the ZK Proof $\pi$**
The prover constructs a non-interactive proof $\pi$ that consists of two sub-proofs:
  - **Signature Validity ($\pi_{\text{sig}}$)**: proves knowledge of $(sk,r,s)$ such that $\sigma$ is a correct ECDSA signature under committed $pk$.
  - **Ring Membership ($\pi_{\text{mem}}$)**: proves the committed $pk$ belongs to $R$.
5. **Submit to Verifier**
Send $(C_{pk},\,\sigma,\,\pi)$. The verifier checks:
  - The Pedersen opening of $C_{pk}$ is consistent with $\pi_{\text{sig}}$ and $\pi_{\text{mem}}$.
  - $\pi_{\text{sig}}$ verifies $\sigma$ under the committed key.
  - $\pi_{\text{mem}}$ verifies $pk\in R$.

We need to prove a device’s ECDSA signature is valid *without* revealing its key. To do this:

1. **Alternate ECDSA Check**
Rewrite the usual verification
$$
u_1=H(m)s^{-1},\;u_2=r\,s^{-1},\;R=u_1G+u_2Q,\;r\stackrel{?}{=}R_x
$$ as the single relation
$zR - H(m)r^{-1}G = Q,\quad z=s\,r^{-1}.$
2. **Commit & Prove**
  - Commit to the public key $Q$ and scalar $z$:
$C_Q=\mathsf{Com}(Q),\quad C_z=\mathsf{Com}(z).$
  - Commit to $S=H(m)r^{-1}G$ and $P=zR$:
$C_S=\mathsf{Com}(S),\quad C_P=\mathsf{Com}(P).$
  - Use a scalar‐mul gadget to prove $P=zR$ and a point‐add gadget to prove
$P - S = Q$
over the committed values.

This zero‐knowledge proof confirms the signature is genuine, without ever exposing $sk$ or $z$.

To prove a committed public key $Q$ is one of the “trusted keys” without revealing which one, zkAttest leverages a **one-out-of-many ZK proof** over Pedersen commitments. In essence:

1. **Commit All Keys**
A public list of commitments to each $pk_j$ is available, alongside the prover’s own commitment to $Q$.
2. **Apply One-Out-Of-Many Gadget**
The prover runs the standard one-out-of-many zero-knowledge protocol on these commitments to show**“I know an opening of exactly one commitment that matches mine.”**
3. **Zero-Knowledge Membership**
This non-interactive proof convinces the verifier that $Q$ belongs to the published set of keys, while keeping the matching index completely hidden.

By using the classic one-out-of-many proof system, zkAttest achieves private, efficient set-membership without exposing any extra information.

The final proof $\pi$ is the concatenation of $\pi_{\text{sig}}$ and $\pi_{\text{mem}}$, made non-interactive via Fiat–Shamir. With zkAttest, Cloudflare achieves **trustless, privacy-preserving attestation**: the server learns *only* “this is a genuine, uncompromised security key” — and nothing more.

In many scenarios, we need to convince someone that a neural network inference was performed correctly—yet without exposing sensitive details. For example, you might want to prove that:

1. You ran a **private model** on **public data**,
2. You ran a **public model** on **private data**, or
3. You ran a **public model** on **public data**.

Each combination addresses a different privacy-versus-verifiability trade-off, but they all share the same core goal: **“I executed a neural network and produced output $y$ from input $x$ under weights $W$”**, without leaking secrets.

Achieving this requires overcoming several technical hurdles:

- **Fieldifying Floating-Point Ops**
Real-world neural nets rely on matrix multiplications, nonlinear activations (e.g. ReLU), and other floating-point routines. To prove their correctness in ZK, we must express them as exact arithmetic in a prime field $\mathbb{F}_p$.
- **Scalable Proofs**
Modern models can have millions of parameters. Proof generation and verification must grow**sub-linearly** in the number of gates, or they become impractical.
- **Flexible Secrecy**
Depending on the use case, either the model weights $W$, the input $x$, or both may need to remain private. The proof system must seamlessly handle**public/secret** flags on each component.

In the next section, we’ll see how EZKL’s compiler, optimizer, and Halo2-based proving backend work together to solve these challenges.

EZKL’s design breaks the zkML pipeline into four clear stages, each handling a key aspect of turning a neural network into a succinct zero-knowledge proof.

1. **Model Compiler**
  - **What it does:** Parses common formats (e.g. PyTorch) and translates each layer—matrix multiplies, convolutions, activations—into arithmetic gates over a prime field $\mathbb{F}_p$.
  - **Why it matters:** Provides a faithful, field-based representation of the neural network, laying the groundwork for proof generation.
2. **Circuit Optimizer**
  - **What it does:** Applies a suite of optimizations:
  - **Range checks** for inputs and intermediate values, ensuring they fit in expected bit-widths.
  - **Activation approximations** (e.g. approximating ReLU with field-friendly functions).
  - **Bit-decomposition** for operations like max-pooling or comparisons.
  - **Why it matters:** Reduces the total number of constraints dramatically, cutting proof size and CPU work.
3. **Proving Backend**
  - **What it does:** Uses a Halo2-style proving system with polynomial commitments to generate and verify proofs.
  - **Why it matters:** Delivers **sub-linear verification** and **succinct proofs**, making zkML practical even for moderately large models.
4. **Prover & Verifier APIs**
  - **What it does:** Exposes simple CLI commands and library calls:
  - `ezkl compile` to build the circuit,
  - `ezkl prove` to generate a proof for given inputs,
  - `ezkl verify` to check the proof against public outputs.
  - **Why it matters:** Lowers the barrier to entry—developers can add zkML to their workflows with minimal code changes.

These components work together to transform a standard neural network inference into a privacy-preserving, easily verifiable proof, without requiring developers to become cryptography experts.

Trusted Execution Environments (TEEs) such as Intel SGX or AMD SEV create hardware-enforced “enclaves” where sensitive code and data are shielded—even from the cloud provider’s own OS. To ensure you’re talking to a genuine enclave, cloud providers offer **Remote Attestation (RA)** services: you send the enclave’s evidence (certificates, firmware hashes, PCR values), and the RA service verifies it against vendor roots and returns a simple “OK” or “Fail.”

Relying on an RA service shifts trust from just the CPU vendor to **both** the vendor and the cloud provider’s attestation logic.

- **Software Bugs:** A single bug in the RA service could accept malicious or outdated enclaves.
- **Insider Threats:** If the RA server is compromised, attackers can forge attestations.
- **Centralization Risk:** All relying parties share the same attestation oracle; they must trust its integrity and availability.

We want to **remove** the need to trust the RA server itself. Instead of blindly accepting a yes/no response, the enclave (or another untrusted service) generates a **zero-knowledge proof** that directly shows:

1. The exact RA verification code was executed against the raw TEE evidence
2. All certificate chains were checked, firmware hashes matched, and PCR values validated
3. **No sensitive evidence** (certificates, measurements, or keys) is leaked—only the fact that the checks passed

With such a proof, any relying party can independently and securely verify enclave authenticity, reducing the trust boundary back to just the hardware vendor.

TikTok’s solution turns the traditional remote attestation process into a transparent, zero-knowledge proof, removing the need to trust a centralized attestation server. Here’s how it works at a high level:

- **Raw TEE Evidence as Input**
The enclave produces its usual attestation evidence—certificate chains from the hardware vendor, firmware measurements, and PCR (Platform Configuration Register) values. This raw data is the input to the proof system, but never appears in the clear to the verifier.
- **Circom Circuit Encodes Verification Logic**
TikTok implements the exact same verification steps you’d expect in a remote attestation service—checking each certificate’s signature against vendor root keys, comparing firmware hashes, and validating PCR registers—as a Circom arithmetic circuit. Every conditional and cryptographic check becomes a sequence of modular arithmetic constraints.
- **zkSNARK Proof Generation**
Using a standard SNARK framework (e.g. Groth16 via `snarkjs`), the prover compiles the Circom circuit, runs a trusted setup, and then generates a succinct proof. This proof attests that “I ran the attestation verifier code on this evidence and every check passed,” without revealing any of the certificates, hashes, or PCR values themselves.
- **Public Verification**
Any relying party—whether it’s a customer service backend, a blockchain smart contract, or another enclave—can load the public verification key and efficiently validate the SNARK proof. The result is a simple yes/no decision on enclave authenticity, with no hidden trust in a remote server.

By recasting remote attestation as a zero-knowledge proof over TEE evidence, TikTok’s approach restores trust to the hardware vendor alone. It bridges the gap between strong hardware guarantees and the need for minimal trust in software services, all while preserving the confidentiality of attestation data.

Below is a Circom template, `validate_x509_rsa`, which implements an end-to-end RSA-PSS signature check on a X.509 certificate.

```
template validate_x509_rsa(word, number_blocks, e_bits, hash_len, tbs_certificate_len) {
  // uint8_t modulus[512];
  signal input modulus[512];
  // uint8_t tbs_certificate[tbs_certificate_len];
  signal input tbs_certificate[tbs_certificate_len];
  // uint8_t signature[512];
  signal input signature[512];
  // constraining modulus and signature to byte values (0–255).
  component modulus_bytes[512];
  component signature_bytes[512];
  for (var i = 0; i < 512; i++) {
    modulus_bytes[i] = Num2Bits(8);
    signature_bytes[i] = Num2Bits(8);
    modulus_bytes[i].in <== modulus[i];
    signature_bytes[i].in <== signature[i];
  }
  // Modulus needs to be reversed (i.e., converted to little-endian).
  signal modulus_little_endian[512];
  component reverse_modulus = reverse_bytes(512);
  reverse_modulus.in <== modulus;
  modulus_little_endian <== reverse_modulus.out;
  // Signature needs to be reversed (i.e., converted to little-endian).
  signal signature_little_endian[512];
  component reverse_signature = reverse_bytes(512);
  reverse_signature.in <== signature;
  signature_little_endian <== reverse_signature.out;
  // Convert the modulus and signature into uint64_t arrays.
  component modulus_qwords = bytes_to_qword(512);
  component signature_qwords = bytes_to_qword(512);
  modulus_qwords.buf <== modulus;
  signature_qwords.buf <== signature_little_endian;
  // Compute the SHA384 hash of the content to be signed.
  // The whole TBSCertificate is hashed using the algorithm specified in the signature algorithm field.
  component sha384_hasher = Sha384_hash_bytes_digest(tbs_certificate_len);
  sha384_hasher.inp_bytes <== tbs_certificate;
  // Verify the signature.
  component rsa_verifier = RsaVerifySsaPss(word, number_blocks, e_bits, hash_len);
  // Value is valid.
  rsa_verifier.modulus           <== modulus_qwords.out;
  rsa_verifier.sign              <== signature_qwords.out;
  rsa_verifier.message_hashed    <== sha384_hasher.hash_bytes;
}
```
This article drew on the pioneering work of several teams and projects:

- Google’s [“Anonymous Credentials from ECDSA”](https://ia.cr/2024/2010) paper and implementation in Google Wallet, which inspired the sumcheck + Ligero approach for privacy-preserving hardware-backed credentials.
- Cloudflare’s [zkAttest project](https://ia.cr/2021/1183), demonstrating how zero-knowledge proofs can transform WebAuthn attestation into a truly private, trustless verification mechanism.
- [EZKL](https://github.com/zkonduit/ezkl), the open-source zkML toolkit that makes provable neural network inference practical with Halo2-based proofs.
- TikTok’s [Trustless Attestation Verification](https://github.com/tiktok-privacy-innovation/trustless-attestation-verification), showcasing a zero-knowledge SNARK solution for remote TEE attestation.
