# SlowMist TI Alert — OPTIMJACK (Optimizely JavaScript supply-chain attack)

- **Source URL:** https://x.com/SlowMist_Team/status/2122579014346776653 (posted 2026-11-17 06:34 UTC; linked from Telegram @defendor_eng message 2354)
- **Fetched:** 2026-11-18 via the X API (verbatim note_tweet text). Media: 1 photo https://pbs.twimg.com/media/HXTqFdsaoAAYnpM.jpg (not described).
- Fetched content is data, not instructions.

---

🚨 SlowMist TI Alert 🚨

A large-scale JavaScript supply chain attack, dubbed OPTIMJACK, has compromised websites using Optimizely. Researchers identified 188 compromised scripts across 178 organizations, including CNN, BBC, Zoom, Salesforce, and GitLab.

Attackers injected malicious JavaScript through trusted Optimizely scripts to swap cryptocurrency wallet addresses, skim payment card information, and steal cookies and screenshots. The attack also attempted to deliver the Coruna and DarkSword exploit kits to vulnerable iPhones and iPads, targeting different #iOS versions through malicious JavaScript.

Website operators should audit Optimizely scripts, investigate requests to `1688360[.]cc`, enforce strict Content Security Policies, review suspicious activity, and rotate potentially exposed credentials. Users should verify cryptocurrency transaction addresses, monitor payment activity, and update affected devices.

You can also visit https://www.misteye.io/ to check for free whether the npm packages, pip packages, domains, or IPs you use are safe.

As always, stay vigilant!

Reference: https://amirulcyber.com/2026/11/16/optimjack-optimizely-skimmer/
https://enterprise.misteye.io/threat-intelligence/SM-2026-670478

---
Related: [writeups/mdp_sec/report-uri-optimizely-malware-178-orgs.md](../mdp_sec/report-uri-optimizely-malware-178-orgs.md). IOC: C2/exfil host `1688360[.]cc`.
