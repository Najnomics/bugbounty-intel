# Information Disclosure — Intercom Identity Verification secret (HMAC key) is hard-coded in…

- **Source URL:** https://medium.com/@jokodfir/information-disclosure-intercom-identity-verification-secret-hmac-key-is-hard-coded-in-59a6413bfd0d
- **Fetched from:** https://medium.com/feed/@jokodfir
- **Fetched:** 2026-11-16
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14985 (id 14985)
- **Method:** medium-rss-content readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
### Information Disclosure — **Intercom Identity Verification secret (HMAC key) is hard-coded in client-side JavaScript**

Assalamualaikum wr. wb.

Bismillah

This is my seventeenth article, I hope it proves useful to readers.

A few months ago, I discovered this vulnerability through a VDP program.

\## Summary

The web application target (\*\*\*) integrates Intercom’s Messenger with \*\*Identity Verification\*\* (Intercom’s HMAC-based anti-impersonation feature). The whole point of Identity Verification is that the browser should only ever receive a pre-computed \`user\_hash\`; the \*\*secret key used to compute it must stay on the server\*\*.

The web application target (\*\*\*) does the opposite: it computes the \`user\_hash\` \*\*in the browser\*\*, which means the secret key is shipped to every visitor inside a JavaScript bundle. I found the key sitting in plaintext in \`\*\*\*.js\`, and I confirmed it’s the real, currently-active key by using it to reproduce — byte-for-byte — the exact \`user\_hash\` that my own browser sent to Intercom.

With that key, anyone can compute a valid \`user\_hash\` for \*\*any\*\* member ID. Member IDs are small sequential integers (mine is \`\*\*\*\*\`), so an attacker can walk the ID space, forge a \`user\_hash\` for each one, and boot the Intercom Messenger \*as that user\* — gaining access to the victim’s support conversation history (which routinely contains personal and account information) and the ability to send messages while impersonating them.

This is a web target-side misconfiguration (the web target exposing its own Intercom secret), not a flaw in Intercom. I did \*\*not\*\* send any forged identity to Intercom or access anyone else’s conversations — my proof stops at reproducing my own hash and showing that arbitrary hashes are trivially computable offline.

**## Steps to Reproduce**

- \*\*\*\*\*
- \*\*\*\*\*
- \*\*\*\*\*

\## Impact

Intercom Identity Verification exists precisely to stop one user from impersonating another in the Messenger. By shipping the HMAC secret to the browser, the web target defeats its own protection:

\- Any visitor can extract the key from \`\*\*\*\*.js\` and compute a valid \`user\_hash\` for \*\*any\*\* \`member\_id\`.

- \`member\_id\`s are sequential integers (mine is \`\*\*\*\*\`), so this is enumerable at scale, not a one-off.

- Booting Intercom as a victim lets an attacker read that victim’s \*\*support conversation history\*\* — which on a lending platform frequently contains names, contact details, account/loan specifics, and other PII — and \*\*send messages as the victim\*\*, which can be used for social-engineering follow-ons.

- The key is retrievable \*\*without even logging in\*\* (it’s in a public static asset), lowering the bar further.

Because the secret is now public knowledge (anyone who has loaded the app has it), it should be treated as compromised and rotated, not just relocated.

\## Remediation

1. \*\*Compute \`user\_hash\` on the server.\*\* Add a small backend endpoint (or include it in an existing authenticated bootstrap response) that returns the already-computed \`user\_hash\` for the logged-in user. Never send the HMAC secret to the browser, and remove the client-side \`CryptoJS.HmacSHA256(…)\` call and the crypto-js include that supports it.

2. \*\*Rotate the exposed secret immediately\*\* in the Intercom workspace settings for app \`\*\*\*\`.

3. After rotating, double-check that the secret no longer appears in any shipped bundle (\`grep\` the built assets for the app IDs / the new key).

#cybersecurity #pentest
