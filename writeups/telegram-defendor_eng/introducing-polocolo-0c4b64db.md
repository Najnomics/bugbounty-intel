# 🔒 Polocolo — an efficient ZK-friendly hash function

- **Source URL:** https://www.zellic.io/blog/introducing-polocolo
- **Fetched:** 2026-11-12
- **Channel:** @defendor_eng
- **Telegram message:** https://t.me/defendor_eng/371 (id 371)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
I designed a new ZK-friendly hash function: [Polocolo↗](https://eprint.iacr.org/2025/926).

Conventional hash functions often struggle with inefficiency in zero-knowledge (ZK) proof settings, leading to the design of several ZK-friendly hash functions. On the other hand, lookup arguments have recently been incorporated into ZK protocols, allowing for more efficient handling of *ZK-unfriendly* operations. As a result, ZK-friendly hash functions based on lookup tables have been proposed.

Polocolo is targeted to a [PlonKup↗](https://eprint.iacr.org/2022/086), an extension of [PLONK↗](https://eprint.iacr.org/2019/953) with [plookup↗](https://eprint.iacr.org/2020/315). Polocolo requires fewer PLONK gates compared to the state-of-the-art ZK-friendly hash functions. For example, when $t = 8$, Polocolo requires 21% less PLONK gates compared to [Anemoi↗](https://eprint.iacr.org/2022/840), which is currently the most efficient ZK-friendly hash function, where $t$ denotes the size of the underlying permutation. For $t = 3$, Polocolo requires 24% less PLONK gates than [Reinforced Concrete↗](https://eprint.iacr.org/2021/1038), which is one of the recent lookup-based ZK-friendly hash functions. Polocolo was presented at [Eurocrypt 2025↗](https://eurocrypt.iacr.org/2025/).

Part 1 of this post discusses the theoretical foundations of PLONK and PlonKup. After forming these foundations, we’ll build on top of it in part 2 to explore how exactly Polocolo works.

## A Review of ZK-Friendly Hash Functions[](https://www.zellic.io/blog/introducing-polocolo#a-review-of-zk-friendly-hash-functions)

Earlier, we discussed ZK-friendly hash functions and algebraic attacks against them in the posts “[ZK-Friendly Hash Functions↗](https://www.zellic.io/blog/zk-friendly-hash-functions/)” and “[Algebraic Attacks on ZK-Friendly Hash Functions↗](https://www.zellic.io/blog/algebraic-attacks-on-zk-hash-functions/)”. For those who haven’t read them, here’s a brief summary.

Hash functions are used in ZK protocols for cryptographic purposes such as commitment schemes and pseudorandom number generation. While SHA-2 and SHA-3 are standardized and extensively studied, their efficiency in ZK protocols is highly inefficient because bitwise operations — though fast on traditional CPUs — are poorly suited to ZK proof systems. This inefficiency has motivated the development of ZK-friendly hash functions, which are optimized for performance in ZK settings.

Intuitively, ZK-friendly hash functions prioritize algebraic simplicity. We introduced [MiMC↗](https://eprint.iacr.org/2016/492), [Poseidon↗](https://eprint.iacr.org/2019/458), [Vision↗](https://eprint.iacr.org/2019/426), and [Rescue↗](https://eprint.iacr.org/2019/426) in a [previous post↗](https://www.zellic.io/blog/zk-friendly-hash-functions/). Additionally, newer proposals such as [Anemoi↗](https://eprint.iacr.org/2022/840), [Griffin↗](https://eprint.iacr.org/2022/403), and [Arion↗](https://arxiv.org/abs/2303.04639) have emerged as advanced ZK-friendly hash functions.

### Sponge Construction[](https://www.zellic.io/blog/introducing-polocolo#sponge-construction)

The common approach for designing ZK-friendly hash functions is to first construct a permutation (a bijective function $\mathbb{F}_p^t \rightarrow \mathbb{F}_p^t$, where $t$ denotes the size of the permutation) and then convert it to a hash function using [sponge construction↗](https://en.wikipedia.org/wiki/Sponge_function).

| The sponge construction — $P_i$ is input and $Z_i$ is hashed output. The unused *capacity* $c$ should be twice the desired collision or preimage attacks. Image from [Wikipedia↗](https://en.wikipedia.org/wiki/SHA-3). | 

The sponge construction operates in two phases:

1. **Absorbing phase.** Message blocks are processed and integrated into the internal state.
2. **Squeezing phase.** Hash digests are extracted from the state.

And key advantages of this framework include

- Arbitrary input/output lengths — which supports variable-length inputs and outputs for the hash function.
- Provable security — the sponge construction’s security is formally reduced to the underlying permutation’s security.

From a designer’s perspective, the primary task simplifies to optimizing the permutation’s structure.

### Algebraic Attacks[](https://www.zellic.io/blog/introducing-polocolo#algebraic-attacks)

If permutation is an ideal permutation (where outputs of permutation are uniformly random), the hash function derived via the sponge construction is secure. However, real-world permutations use deterministic mathematical structures; the output of a permutation is not random. Any bias in the output can lead to an attack on the hash function.

An attack against a ZK-friendly hash function focuses on the **constrained-input constrained-output (CICO) problem**. For a permutation $P : \mathbb{F}_p^t \rightarrow \mathbb{F}_p^t$, the CICO problem involves finding $x_1, \dots, x_{t-1}, y_1, \dots, y_{t-1} \in \mathbb{F}_p$ such that $P(x_1, \dots, x_{t-1}, 0) = (y_1, \dots, y_{t-1}, 0).$
Solving this proplem enables collision or preimage attacks against the hash function.

A simple brute-force attack without using characteristics of $P$ is to set $x_1, \dots, x_{t-1}$ arbitrarily and check whether the last element of $P(x_1, \dots, x_{t-1}, 0)$ is zero. This requires $O(\vert \mathbb{F}_p \vert) = O(p)$ attempts. If the CICO probem can be solved faster than $O(2^\kappa)$ for certian security parameter $\kappa$, then the hash function derived from that permutation is considered insecure. In ZK-friendly hash functions, designers typically consider $\kappa=128$, meaning that expected attack complexity is at least $2^{128}$.

In ZK-friendly hash functions, the function is algebraically simple. Therefore, the algebraic attack that involves representing the CICO problem as the system of the equations and solving it is usually the most effective attack against ZK-friendly hash functions. We introduced several attacks in the [previous post↗](https://www.zellic.io/blog/algebraic-attacks-on-zk-hash-functions/).

The designers carefully choose their structures and the parameters after considering all of the proposed attacks, including even security margins. Unfortunately, as attack techniques continue to evolve, it is common for proposed ZK-friendly hash functions to be attacked, even if the hash function is peer-reviewed and introduced in a top conference.

| Here is the timeline of the ZK-friendly hash function. Red flash signs denote the original specification is broken by algebraic attacks. | 

## How Does PLONK Work?[](https://www.zellic.io/blog/introducing-polocolo#how-does-plonk-work)

[PLONK↗](https://eprint.iacr.org/2019/953) is a universal and succinct ZK protocol. Among various ZK protocols, we’ll focus on PLONK, as Polocolo targets PLONK with lookup.

A zero-knowledge proof system is a two-party cryptographic protocol between a prover and a verifier that allows the prover to convince the verifier of their knowledge without revealing itself. For example, given a hash function $h$ and the hash value $y$, the prover can convince the verifier their knowledge of preimage $x$ such that $h(x) = y$. Performance metrics for the protocol, including prover time, verifier time, and proof size, are influenced by the function $h$. Generally, the simpler the $h$ can be expressed algebraically, the more efficient the protocol becomes.

Comparing PLONK to [Groth16↗](https://eprint.iacr.org/2016/260.pdf), proof size and verifier complexity still remains $O(1)$ (though slightly less efficient), and the structured reference string (SRS) is universal and updatable. Therefore, the trusted setup can be performed in a **universal manner**. In Groth16, the trusted setup must be performed for each circuit. PLONK also has several variants, such as [HyperPlonk↗](https://eprint.iacr.org/2022/1355) and [PlonKup↗](https://eprint.iacr.org/2022/086), which support custom gates and lookup gates, respectively. However, unlike Groth16 and zkSTARK, addition is not free. Moreover, PLONK lacks quantum resistance.

Let’s delve into how PLONK works by exploring its arithmetization technique. This will give us insight into how a prover’s complexity is determined.

### Arithmetization[](https://www.zellic.io/blog/introducing-polocolo#arithmetization)

PLONK employs its own arithmetization technique. For a given arithmetic circuit, there are two types of constraints, the **gate constraint** and **copy constraint**.

Here is an example of proving the knowledge of $x, y$ such that $x^3 + xy = 14$. Note that $x = 2, y = 3$ satisfies the equation. The arithmetic circuit of the corresponding equation is shown below.

| The arithmetic circuit of the equation $x^3 + xy = 14$. | 

Respectively, $a_i, b_i$ represent the left and right inputs, while $c_i$ represents the output for each $i$-th gate. The color of each variable indicates its assigned value, meaning variables sharing the same color have identical values.

Now the prover has to prove these two contraints:

1. For the gate constraint, for each gate input $a_i, b_i$ and output $c_i$, the gate is valid (i.e., $c_i = a_i + b_i$ for the addition gate and $c_i = a_i \times b_i$ for the multiplication gate).
2. For the copy constraint, if the color is the same, then the value is the same (i.e., $a_1 = b_1 = a_2 = a_3, c_1 = b_3, \dots$).

If both constraints are verified, the verifier convinces the prover’s knowledge of $x, y$ such that $x^3 + xy = 14$.

**Note:** Actual protocols use mathematical building blocks such as vanishing polynomials, FFTs, and polynomial commitments. To simplify understanding, this explanation focuses on PLONK’s core concepts rather than replicating the protocol exactly as described in the paper. For in-depth details, refer to the [original PLONK paper↗](https://eprint.iacr.org/2019/953).


#### Gate Constraint[](https://www.zellic.io/blog/introducing-polocolo#gate-constraint)

For the gate constraint, each gate is represented by the following equation: $(q_{L_i})a_i + (q_{R_i})b_i + (q_{O_i})c_i + (q_{M_i})a_ib_i + q_{C_i} = 0.$

The selectors $(q_{L_i}, q_{R_i}, q_{O_i}, q_{M_i}, q_{C_i})$ are determined by the gate type. In our example, the four gates are configured as follows:

$$
\begin{aligned} 0 \cdot a_1 + 0 \cdot b_1 + 1 \cdot c_1 + (-1) \cdot a_1b_1 + 0 &= 0 \\ 0 \cdot a_2 + 0 \cdot b_2 + 1 \cdot c_2 + (-1) \cdot a_2b_2 + 0 &= 0 \\ 0 \cdot a_3 + 0 \cdot b_3 + 1 \cdot c_3 + (-1) \cdot a_3b_3 + 0 &= 0 \\ (-1) \cdot a_4 + (-1) \cdot b_4 + 0 \cdot c_4 + (0) \cdot a_4b_4 + (-14) &= 0 \\ \end{aligned}
$$
Similar to [Groth16↗](https://www.zellic.io/blog/how-does-tornado-cash-work#groth16), the prover constructs a polynomial $q_L(x)$ such that $q_L(i) = q_{L_i}$ for $i \in \{1,2,3,4\}$. Polynomials $q_R(x), q_O(x), q_M(x), q_C(x), a(x), b(x), c(x)$ are also derived in the similar manner. The combined constraint is then
$q_L(x)a(x) + q_{R}(x)b(x) + q_{O}(x)c(x) + q_{M}(x)a(x)b(x) + q_{C}(x) = 0$ for $x \in \{1,2,3,4\}$.

#### Copy Constraint[](https://www.zellic.io/blog/introducing-polocolo#copy-constraint)

For the copy constraint, the prover must demonstrate the following equalities:

$$
\begin{aligned} & a_1 = a_2 = a_3 = b_1, \\ & b_3 = c_1, \\ & a_4 = c_3, \\ & b_4 = c_2. \\ \end{aligned}
$$
Equalities involving more than two variables can be decomposed into pairwise constraints: $a_1 = a_2 = a_3 = b_1 \Leftrightarrow a_1 = a_2, a_2 = a_3, a_3 = b_1.$

To formalize this, define two vectors $v$ and $v'$ representing the original and permuted variable assignments:

$$
\begin{aligned} v &= [a_1, a_2, a_3, a_4, b_1, b_2, b_3, b_4, c_1, c_2, c_3, c_4] \\ v' &= [a_2, a_3, b_1, c_3, a_1, b_2, c_1, c_2, b_3, b_4, a_4, c_4]. \end{aligned}
$$
If $v = v'$, all required equalities hold. To verify the entire permutation at once, define a permutation function $\sigma : \{1,\dots,12\} \rightarrow \{1,\dots,12\}$, where $\sigma(i)$ denotes the index of element $v[i]$ in $v'$. For example, $v[1] = a_1$ maps to $v'[5]$. Therefore, $\sigma(1) = 5$.

The prover must show $v[i] = v'[\sigma(i)] = v[\sigma(i)]$ for each $i \in \{1, \dots, 12\}$. Instead of direct equality checks, the prover demonstrates $\prod_{i \in \{1,\dots,12\}} \frac{v[i] + i \cdot \beta + \gamma}{v[i] + \sigma(i) \cdot \beta + \gamma} = 1$

for random $\beta, \gamma$. It can be easily seen that valid permutations ensure numerator and denominator terms cancel pairwise. For instance, the terms corresponding to $i \in \{1,2,3,5\}$ (linked to $a_1 = a_2 = a_3 = b_1$) yield:

$$
\frac{(a_1 + \beta + \gamma) \cdot (a_2 + 2\beta + \gamma) \cdot (a_3 + 3\beta + \gamma) \cdot (b_1 + 5\beta + \gamma)}{(a_1 + 5\beta + \gamma) \cdot (a_2 + \beta + \gamma) \cdot (a_3 + 2\beta + \gamma) \cdot (b_1 + 3\beta + \gamma)}.
$$
If $a_1 = a_2 = a_3 = b_1$, the fraction simplifies to $1$.

Let polynomials $f, g$ be defined as $f = v[i] + i \cdot \beta + \gamma$ and $g = v[i] + \sigma(i) \cdot \beta + \gamma$, respectively.

Define a polynomial $p$ as $p(1) = 1$ and $p(i) = \prod_{j < i} \frac{f(j)}{g(j)}$ for $i \in \{2,\dots,12\}$.

Then

$$
\begin{align} & p(1) = 1, \\ & p(x+1) = \frac{g(x)p(x)}{f(x)} \textrm{ for } x \in \{1,\dots,11\}, \\ & p(12) = 1 \\ \end{align}
$$
must hold.

By accumulating gate constraints and copy constraints, the prover need to show

$$
\begin{align} & q_L(x)a(x) + q_{R}(x)b(x) + q_{O}(x)c(x) + q_{M}(x)a(x)b(x) + q_{C}(x) = 0 \textrm{ for } x \in \{1,\dots,4\}, \\ & p(1) = 1, \\ & p(x+1) = \frac{g(x)p(x)}{f(x)} \textrm{ for } x \in \{1,\dots,11\}, \\ & p(12) = 1. \\ \end{align}
$$
The functions $q_L, q_R, q_O, q_M,$ and $q_C$ are determined by the circuit and publicly calculated, while the functions $a, b, c,$ and $p$ are derived from the prover’s private witness. These equations are efficiently verifiable using mathematical building blocks such as vanishing polynomials, FFTs, and polynomial commitments. Detailed explanations are omitted in this post.

An important point to note is that the degree of the polynomials $q_L, q_R, q_O, q_M, q_C, a, b, c,$ and $p$ is determined by the number of gates. Thus, **the prover’s complexity** is proportional to **the number of gates**.

## How Does PlonKup Work?[](https://www.zellic.io/blog/introducing-polocolo#how-does-plonkup-work)

PLONK faced a common challenge: operations with high degrees in the native field $\mathbb{F}_p$ require significant overhead. This led to the invention of an extension of PLONK, named [PlonKup↗](https://eprint.iacr.org/2022/086).

In a vanilla PLONK, the prover can use addition and multiplicative gates. PlonkUp supports one additional type of gate: **lookup gates**. Using lookup gates, a prover can prove a witness $x$ belongs to a public table $T$.

In PlonKup, gate constraints are extended by introducing a new selector $q_K$ for lookup gates. For the $i$-th element $(x_i, y_i, z_i)$ in the public table $T$, the element is compressed as $t_i = x_i + \zeta y_i + \zeta^2 z_i$ using a random value $\zeta$.

The gate constraints for input gates $a_i, b_i$ and output gate $c_i$ are extended as follows:

$$
\begin{align} & (q_{L_i})a_i + (q_{R_i})b_i + (q_{O_i})c_i + (q_{M_i})a_ib_i + q_{C_i} = 0, \\ & q_{K_i}(a_i + \zeta b_i + \zeta^2 c_i - f_i) = 0, \\ & f_i \in \{t_1, \dots, t_n\}. \end{align}
$$
If the $i$-th gate is an arithmetic gate, then $q_{K_i} = 0$. Conversely, if the $i$-th gate is a lookup gate, then $q_{K_i} = 1$.

While the first two equations can be derived similarly through vanilla PLONK, the third equation $f_i \in \{t_1, \dots, t_n\}$ requires the specialized strategy introduced in [plookup↗](https://eprint.iacr.org/2020/315). Due to the complexity of this component, it’s recommended to check [plookup↗](https://eprint.iacr.org/2020/315) and the [PlonKup↗](https://eprint.iacr.org/2022/086) papers for further details.

### Lookup Arguments[](https://www.zellic.io/blog/introducing-polocolo#lookup-arguments)

To appreciate PlonKup’s utility, let’s examine why lookup arguments matter. If the ZK proof system only allows addition and multiplicative gates, operations that cannot be represented algebraically simply require a large number of constraints. For instance, XOR of two 16-bits elements $a, b$ is a lightweight operation in traditional CPUs. However, representing $c = a \oplus b$ in $\mathbb{F}_p$ requires complex computation as follows:

$$
\begin{align} a_i \cdot (1 - a_i) = 0 \textrm{ for } i \in \{1,\dots,16\} : & \textrm{ 16 mul gates} \\ a = \sum_{i \in \{1,\dots,16\}} 2^{i-1} \cdot a_i : & \textrm{ 15 add gates} \\ b_i \cdot (1 - a_i) = 0 \textrm{ for } i \in \{1,\dots,16\} : & \textrm{ 16 mul gates} \\ b = \sum_{i \in \{1,\dots,16\}} 2^{i-1} \cdot b_i : & \textrm{ 15 add gates} \\ c_i = a_i + b_i - 2a_ib_i \textrm{ for } i \in \{1,\dots,16\} : & \textrm{ 32 add gates and 16 mul gates} \\ c = \sum_{i \in \{1,\dots,16\}} 2^{i-1} \cdot c_i : & \textrm{ 15 add gates} \\ \end{align}
$$
This is 48 multiplication gates and 77 addition gates.

If the ZK proof system supports lookup gates, the required number of gates is dramatically reduced. First, define the table $T$ as $T = \{(x,y,z) \vert x < 2^4, y < 2^4, z = x \oplus y\}$, which contains $2^8$ elements. Then the XOR operation can be computed as follows:

$$
\begin{align} a = \sum_{i \in \{1,\dots,4\}} 16^{i-1} \cdot a_i : & \textrm{ 3 add gates}\\ b = \sum_{i \in \{1,\dots,4\}} 16^{i-1} \cdot b_i : & \textrm{ 3 add gates} \\ c = \sum_{i \in \{1,\dots,4\}} 16^{i-1} \cdot c_i : & \textrm{ 3 add gates} \\ (a_i, b_i, c_i) \in T \textrm{ for } i \in \{1,\dots,4\} : & \textrm{ 4 lookup gates} \end{align}
$$
This requires only nine addition gates and four lookup gates.

| Handling XOR using a lookup table. | 

Since the prover’s complexity in PLONK is proportional to the total number of gates, XOR can be handled much more efficiently once the lookup table is enabled.

## The First Lookup-Based ZK-Friendly Hash Function[](https://www.zellic.io/blog/introducing-polocolo#the-first-lookup-based-zk-friendly-hash-function)

It is natural to attempt to design ZK-friendly hash functions using lookup gates. The main advantage of using lookup gates in ZK-friendly hash functions is that they are not expressed in a simple algebraic way, which can provide resistance to algebraic attacks. For instance, representing the condition $x \in T$ algebraically (e.g., $f(x) = 0$) requires a polynomial $f$ of degree $\vert T \vert - 1$.

[Reinforced Concrete↗](https://eprint.iacr.org/2021/1038) is the first lookup-based ZK-friendly hash function, presented at CCS 2022. Reinforced Concrete consists of Bricks, Concrete, and Bars layers. Among them, lookup table is used in the **Bars layer**. In the Bars layer, $t$ elements are processed in parallel through the Bar function. In the Bar function, similar to computing XOR using lookup gates, an element $x \in \mathbb{F}_p$ is first decomposed into $(x_1, \dots, x_n)$ where
$x = \sum_{i \in \{1, \dots, n\}} 1024^{i-1} \cdot x_i.$

Then $x_i$ is fed into to a small-sized lookup table $S$, yielding $y_i = S(x_i)$. The output is then determined by $y = \sum_{i \in \{1, \dots, n\}} 1024^{i-1} \cdot y_i,$ which reconstructs the composed output from $y_i$.

| Bar function $bar : \mathbb{F}_p \rightarrow \mathbb{F}_p$ in Reinforced Concrete. | 

This structure uses a lookup table in a canonical way, maintaining reasonable efficiency with no known vulnerabilities reported. However, a key drawback is the high cost evaluating the Bars layer in a ZK setting. Out of the 15 layers in Reinforced Concrete, only one is the Bars layer — while it still accounts for 75% of the constraints in the PlonKup. In general, it is desirable and natural to iterate a simple layer over multiple rounds. Reducing the cost of the Bars layer and iterating it over multiple rounds may enhance security and allow a trade-off between efficiency and security. This motivates **Polocolo’s design**.

## Introducing Polocolo[](https://www.zellic.io/blog/introducing-polocolo#introducing-polocolo)

Polocolo is another lookup-based ZK-friendly hash function from a different design rationale. The name Polocolo derives from **po**wer residue for **lo**wer **co**st table **lo**okup.

To map an input $x \in \mathbb{F}_p$ to a lookup table, the possible value of $x$ must be constrained via preprocessing. The Bar function in Reinforced Concrete uses a base expansion method to apply a lookup table to an element of $\mathbb{F}_p$: $x \in \mathbb{F}_p$ is decomposed into an $n$-tuple $(x_1, \dots, x_n) \in \mathbb{Z}_{s_1} \times \dots \times \mathbb{Z}_{s_n}$ then each $x_i$ is passing through small S-boxes, as explained in previous section. Each component is then fed into an S-box via table lookup. The outputs from the S-boxes are combined again to define the corresponding output of the Bar function. However, base expansion is significantly expensive in most ZK settings.

To address this, I propose an alternative approach, dubbed the **power residue method**, which efficiently applies lookup tables to $\mathbb{F}_p$ elements for a large prime $p(\approx 2^{256})$. A [power residue↗](https://en.wikipedia.org/wiki/Power_residue_symbol) can be seen as a generalization of the Legendre symbol. When a positive integer $m$ divides $p-1$, the $m$-th power residue of $x$ is defined as
$\left(\frac{x}{p}\right)_m = x^{(p-1)/m}.$
The $m$-th power residue takes $m+1$ distinct values, so each possibility can be an input to a lookup table $T$ of size $m+1$.

Now our new S-box $S : \mathbb{F}_p \rightarrow \mathbb{F}_p$ is defined as

$$
S(x) = x^{-1} \cdot T\left[\left(\frac{x}{p}\right)_m \right].
$$
By appropriately choosing $T$, this S-box can be made bijective. Moreover, this S-box is of a high degree that requires only 14 PLONK gates — for example, when $m = 1024$, which is significantly fewer than 94 gates required for the Bar function from Reinforced Concrete. Using this S-box, I propose Polocolo, a new lookup-based ZK-friendly hash function.

In part 2 of this post, I will introduce the detailed specification and cryptanalysis of Polocolo, along with a performance comparison with other ZK-friendly hash functions.

## About Us[](https://www.zellic.io/blog/introducing-polocolo#about-us)

Zellic specializes in securing emerging technologies. Our security researchers have uncovered vulnerabilities in the most valuable targets, from Fortune 500s to DeFi giants.

Developers, founders, and investors trust our security assessments to ship quickly, confidently, and without critical vulnerabilities. With our background in real-world offensive security research, we find what others miss.

[Contact us↗](https://zellic.io/contact) for an audit that’s better than the rest. Real audits, not rubber stamps.
