# 🛡️ Assessing the Security Maturity of Blockchain Code

- **Source URL:** https://blog.trailofbits.com/2023/07/14/evaluating-blockchain-security-maturity
- **Fetched:** 2026-11-17
- **Channel:** @defendor_eng
- **Telegram message:** https://t.me/defendor_eng/305 (id 305)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Evaluating blockchain security maturity

Holistic security reviews should reveal far more than simple bugs. Often, these bugs indicate deeper issues that can be challenging to understand and address. Given the time-boxed nature of reviews, security engineers may not have the opportunity to identify all bugs caused by these problems—and they may continue to cause issues in the future, even after initial bugs are fixed.

That’s why it’s important to think about security more holistically when developing a secure product. This perspective requires consideration of the software development lifecycle and the architecture and design of the software. We’ve developed a set of [codebase maturity criteria](https://secure-contracts.com/development-guidelines/code_maturity.html) for assessing a codebase’s compliance with industry standards and best practices. Our resulting recommendations have facilitated substantial enhancements to our clients’ codebases. For instance, [Balancer](https://balancer.fi/) developed better arithmetic primitives based on our [recommendations on arithmetic rounding (Appendix H)](https://github.com/trailofbits/publications/blob/master/reviews/2021-04-balancer-balancerv2-securityreview.pdf), while other clients, including Optimism, Uniswap, and Primitive, strengthened their codebases through the implementation of [Echidna properties](https://github.com/crytic/echidna#property-testing-suites).

We’re sharing these guidelines to help everyone assess and enhance the maturity of their own smart contract codebases.

## How we evaluate maturity

Drawing from our experience performing hundreds of security audits over more than a decade, we’ve identified several important control families. They are where we commonly identify security flaws, and where improvements are frequently needed to enhance a product’s security posture. Achieving greater maturity in these areas results in fewer bugs over the product’s lifecycle (and happier security engineers).

We rank each of these categories as weak, moderate, satisfactory, or strong:

- Arithmetic
- Auditing
- Authentication/access controls
- Complexity management
- Decentralization
- Documentation
- Low-level manipulation
- Transaction ordering risks
- Testing and verification

(Note that we apply this control family-based approach for all of our clients, blockchain or otherwise, and adjust the controls based on the target of our review. Our cryptography and application security teams have their own recommended controls.)

Most teams will have to exert substantial effort to achieve satisfactory maturity. For example, if a codebase doesn’t include an automated testing method targeting arithmetic, it can be considered moderate at best. This may seem strict, but the reality is that if you haven’t incorporated fuzzing into your development process in 2023, you’ve fallen behind. Likewise, if your system reports events, yet lacks a strategy for monitoring them or responding to reported failures, you should rethink your incident response strategy.

Although we formulated these best practices based on extensive experience, we’re open to feedback. We periodically update this list as we work with more clients and as the controls required to deliver secure blockchain solutions change over time.

## Using the code maturity evaluation

Assessing a project against these specific guidelines facilitates an in-depth and informed conversation about software security risks for blockchain projects. In an environment where new threats come out daily and infosec Twitter can’t stay on one topic for more than an hour, this helps teams focus on fundamental necessities. It also helps demonstrate positive progress toward safety rather than just detection of bugs (a negative indicator).

Our guidelines can be used as a self-evaluation protocol for various roles involved in software development:

- **Developers should follow the guidelines.** Incorporating them throughout development will help identify potential blind spots. A project striving to achieve satisfactory or higher ratings across all categories on day one will position itself for success and reduce the likelihood of security issues.
- **Security engineers should measure their target against the guidelines.** They should use the information gathered from a code review to enrich their evaluation and provide guidance to developers on improving maturity. However, they should remember that these criteria are intended to guide self-reflection and are not a comprehensive checklist that addresses all risks. A key responsibility of security engineers is to contextualize the maturity evaluation.
- **Company leaders should allocate resources to address deficiencies.** They should review the maturity evaluation to understand the status of their project security. This will assist them in prioritizing and determining how to improve the organization’s security posture and allocate resources to weak spots.

## Toward an industry-wide best practice

We encourage security industry professionals to adopt these guidelines as a best practice. We will periodically update them as best practices evolve and new risks emerge. If you want to enhance your entire security posture—and go beyond simply finding bugs—please contact us through [our website](https://www.trailofbits.com/contact/) or [email](https://blog.trailofbits.com/cdn-cgi/l/email-protection#e093818c8593a0949281898c8f8682899493ce838f8d).
