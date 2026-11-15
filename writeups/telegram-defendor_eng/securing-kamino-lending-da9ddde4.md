# 🔬 How Formal Verification Caught a Future Risk in Kamino Lending

- **Source URL:** https://www.certora.com/blog/securing-kamino-lending
- **Fetched:** 2026-11-15
- **Channel:** @defendor_eng
- **Telegram message:** https://t.me/defendor_eng/1783 (id 1783)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
[← Engineers' Hub](https://www.certora.com/blog/engineers-hub)

# Securing Kamino Lending

How Formal Verification Prevented Future Risks

Author:

[Pamina Georgiou](https://www.certora.com/author/pamina)

## **Kamino Lending and Its Commitment to Security**

[Kamino Lending](https://github.com/Kamino-Finance/klend) (KLend) is a cutting-edge lending protocol on Solana, designed to offer efficient, decentralized borrowing and lending solutions. Built for speed and scalability, KLend lets users deposit collateral and borrow liquidity while ensuring fair and transparent exchange rates.

As part of their ongoing commitment to security, [Kamino Finance](https://app.kamino.finance/) partnered with Certora to perform a rigorous code audit, including [formal verification](https://www.certora.com/blog/white-paper) of critical invariants in their protocol with the [Certora Prover](https://www.certora.com/blog/white-paper).

Our [analysis](https://www.certora.com/reports/kamino-lending-security-report) uncovered a precision loss issue in the exchange rate calculation. A subtle yet significant rounding bug allowed someone to redeem more collateral than they originally deposited —an edge case that, while not exploitable today, could become a risk in the future. Thanks to Kamino’s proactive approach, they quickly addressed the issue, reinforcing their position as a leader in DeFi security.

Let's take a closer look:

## The Precision Loss Bug in Kamino Lending

[Kamino’s lending protocol](https://github.com/Kamino-Finance/klend) determined the exchange rate between collateral shares and liquidity in terms of the share value per liquid token in the system:

The exchange rate is represented using a fixed point representation Fraction with 68 bits for the integer and 60 bits for the fractional part, which is a wrapper for Rust’s built-in fixed point library [Fixed](https://docs.rs/fixed/latest/fixed/).

Here’s the key logic:

**Division rounding:** While this approach works in most cases, the division introduces a rounding issue because the **Fraction** type uses 60 bits for the fractional part: any value must be rounded to the nearest multiple of `2^-60`. However, the exact mathematical quotient may have more precision than 60 bits allow. In this case, only the first 60 bits are kept, and the remainder is discarded, resulting in a slightly lower stored value.

**Error amplification in subsequent operations:** Since the exchange rate is rounded down when stored in a **Fraction**, any subsequent calculation with this rate — such as converting collateral to liquidity by performing a division — can amplify small precision losses. Dividing by a number that is slightly too low produces a quotient that is slightly too high.

**Impact on redeeming collateral:** The downward rounding of the exchange rate means the division operation can produce a slightly larger output than expected. This becomes problematic when users redeem collateral. The protocol determines the liquidity to return with another division of the share amount to withdraw by the exchange rate:

Since the exchange rate is rounded down, using it in division operations can result in a liquidity amount that rounds up. This could allow a user to withdraw slightly more liquidity than intended.

## How did we uncover the edge case with the help of formal verification?

Formal verification’s magic lies in its ability to explore all possible values for every parameter, ensuring that even the rarest edge cases are uncovered. Using [symbolic execution](https://en.wikipedia.org/wiki/Symbolic_execution), the Certora Prover systematically evaluated two solvency invariants: the number of issued shares must always be less than or equal to the number of the underlying assets, and no user operation should decrease the value of a single share.

Symbolic execution ensures that every potential combination of inputs, including those far beyond what might be considered "normal," is analyzed. The prover identified that these invariants could be broken under certain extreme conditions.

### **Verifying Inductive Invariants**

To establish that an invariant is inductive, we prove it for every user operation that could modify the relevant amounts. In this case, the necessary values are stored in the protocol’s **reserve** object, so any operation accepting a **reserve** as an argument requires verification.

Using structural induction, we:

1. **Prove the base case:** the invariant holds immediately after initializing a reserve.
2. **Verify the step cases:** assuming the invariant holds at a nondeterministic but fixed state, we perform an operation and confirm that the invariant remains intact. Each operation results in one such step case.

The rules that uncovered the bug focused on the operation to redeem collateral.

**Reserve Solvency:** The following rule assumes the property that the amount of liquidity in the system needs to be greater than or equal to the amount of collateral shares minted before calling the redeem function with a nondeterministic amount of shares `collateral_amount` to redeem. It checks that after the redemption operation, the property is still valid. Here’s the essence of the rule:

The Certora Prover flagged that the solvency invariant could fail under specific conditions involving large numbers due to the rounding error during collateral redemption. By systematically testing operations against the solvency rule, the Prover exposed this subtle issue, demonstrating the precision and thoroughness of formal verification.

**Share Value Evolution:** The second rule that shows the critical path involves the nature of the supposed development of share value over time. No matter which user operation is performed, the value of a share can only increase. Specifically, this means that the following must hold:

We can check this behavior in the following (simplified) way:

The Certora Prover showed another counterexample for redeeming that allowed the user to decrease the share price. Once flagged, the manual audit team analyzed the flagged code paths, confirmed the bug, and contextualized its real-world implications.

## Understanding Error Thresholds and Exploitability Risks on Solana

It is important to note that although the rounding error introduces a slight upward bias in the liquidity calculation, it is not exploitable on Solana today. The exchange rate rounds down during calculation due to the fractional representation, introducing a rounding error that is very small (at most `2^-60` per operation). When dividing a large collateral amount by this rate, the resulting liquidity value can round up. Specifically, extremely large numbers such as collateral amounts above `2^59` might render the absolute error significant in the context of financial calculations.

To put this in perspective, one of the tokens on the Solana ecosystem with the largest supply is BONK. At the time of writing, the BONK Token has:

To trigger the rounding error, we would need to make a deposit of an amount larger than `2^59` and have an exchange rate that has the right characteristics. If we simulate this, we can get:

This shows that it is possible to gain only 1 lamport of BONK by exploiting this rounding error, while the attacker would need `2e12` BONK tokens worth **$216m** to perform the attack. This is about three times as much as the holdings of the largest single BONK holder account. These numbers show that this rounding issue is hardly exploitable at this moment, especially considering the transaction costs of performing such an attack.

However, **identifying this edge case highlights the importance of forward-looking security practices**. While this is far beyond the supply of any current Solana token, the potential for a future issue still exists. In theory, this behavior allows users to exploit the protocol by redeeming more than they supplied in the first place, that is free money 💸

While the current ecosystem makes exploiting this bug infeasible for now, uncovering it reinforces the case for blending formal verification with manual audits. It demonstrates the power of symbolic tools to uncover subtle, edge-case vulnerabilities that manual efforts alone might miss.

## How did the Kamino lending team fix the precision loss issue in exchange rate calculation?

Although this bug was not exploitable at the time of discovery — because no Solana tokens currently have a total supply large enough to trigger it — Kamino took immediate action to strengthen their protocol against future risks.

They implemented the industry-standard **Mul-Div pattern** to ensure precise and secure exchange rate calculations. The updated formula follows this common structure:

By rounding down the result of this computation, this fix [guarantees](https://prover.certora.com/output/696612/3b2a3cf46a84404193fd4d0b11230f74/?anonymousKey=723d59c10c84cd7f12a25b9f93f442d08fc84db1) that users cannot withdraw more liquidity than intended.

## Conclusion

This case exemplifies why **combining formal verification and manual code audits is the gold standard for DeFi security**. Manual audits excel at assessing logic and finding creative exploits, while formal verification dives deep into mathematical guarantees and edge cases. Formal verification ensures protocols are robust against future changes, whether from new tokens with larger supplies or unforeseen shifts in blockchain dynamics.

Projects build trust and resilience by catching these bugs early, signaling their commitment to security and reliability. Kamino Finance’s proactive response to this issue highlights their dedication to DeFi security. Rather than ignoring a non-exploitable bug, they chose to patch it, ensuring their protocol remains robust even as the Solana ecosystem evolves.

At [Certora](https://www.certora.com/), we take pride in helping teams like Kamino identify and mitigate security risks before they become problems. By leveraging formal verification, we can detect even the most subtle vulnerabilities and help DeFi protocols maintain the highest security standards.

Want to secure your protocol with Certora? [Get in touch](https://www.certora.com/signup?plan=audit) today!
