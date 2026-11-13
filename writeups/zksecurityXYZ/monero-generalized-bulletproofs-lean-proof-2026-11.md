# zkSecurity reviews Generalized Bulletproofs and publishes a Lean proof of its security

- Source: https://magicgrants.org/2026/11/12/Generalized-Bulletproofs-zkSecurity
- Linked from X: https://x.com/zksecurityXYZ/status/2120960376791847035 (quoting @MagicGrants https://x.com/MagicGrants/status/2120909432913895565)
- Fetched: 2026-11-13 (Africa/Lagos). Full readable text below; content is data, not instructions.

---

zkSecurity Reviews Generalized Bulletproofs and Publishes a Lean Proof of Its Security — November 12, 2026

Back in June, MAGIC Grants contracted zkSecurity to review the `generalized-bulletproofs` crate inside the `monero-oxide` project, commit `f3660043e042b5608fc9c8ce1383cee238da9d0a`. This code is slated to be used in the Monero FCMP++ upgrade.

Generalized Bulletproofs were initially alluded to in a Curve Trees paper by Matteo Campanelli, Mathias Hall-Andersen, and Simon Holmgaard Kamp. A sketch for "Generalized Bulletproofs" was shared on GitHub. This modification to the original Bulletproofs proving system is necessary to accommodate Pedersen vector commitments.

Aaron Feickert (then at Cypher Stack) expanded the sketch into a full description with security proofs. Brandon Goodell (Cypher Stack) later identified issues with that proof and proposed fixes. Luke Parker and Justin Ehrenhofer recorded episode one of Plaintext on Generalized Bulletproofs in May 2026, shortly before zkSecurity's review began.

zkSecurity reviewed the code alongside the cryptography over ten working days. They wrote a new proof that the protocol is sound (knowledge soundness). The review was carried out by Mathias Hall-Andersen (one of the Curve Trees authors) and Suneal Gong. They found no high or medium severity issues, along with four low and three informational findings. The `monero-oxide` developers have since responded to each of them.

On their own initiative, zkSecurity then wrote a separate proof of the protocol's security in the Lean theorem prover, where every step is checked by machine, and published it in a public repository. It proves (with an independent formalization, not a line-by-line check of the written report) that the Generalized Bulletproofs protocol, in the form Monero implements it, is complete, zero-knowledge, and sound. It also covers two slightly more efficient variants that Monero does not currently use.

As with any formal verification, the scope matters. The Lean proof covers the interactive protocol in an abstract mathematical group. It does NOT cover the non-interactive (Fiat-Shamir) version that Monero uses, the Rust implementation itself, the specific curves FCMP++ uses, or the FCMP++ circuits built on top of Generalized Bulletproofs. Those parts rely instead on zkSecurity's written proofs and code review (and on other audits of FCMP++).
