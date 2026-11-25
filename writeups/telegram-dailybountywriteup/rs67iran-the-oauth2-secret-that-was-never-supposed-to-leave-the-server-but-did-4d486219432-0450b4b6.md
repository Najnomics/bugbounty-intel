# The OAuth2 Secret That Was Never Supposed to Leave the Server — But Did

- **Source URL:** https://medium.com/@rs67iran/the-oauth2-secret-that-was-never-supposed-to-leave-the-server-but-did-4d4862194323
- **Fetched from:** https://medium.com/@rs67iran/the-oauth2-secret-that-was-never-supposed-to-leave-the-server-but-did-4d4862194323?source=rss-6a5d4b979781------2
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14886 (id 14886)
- **Method:** medium-rss-feed (full content:encoded) readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- **Author/Published (RSS):** Reza / Fri, 28 Aug 2026 23:42:03 GMT

There’s a specific kind of quiet that happens when you’re scrolling through a minified JavaScript bundle and a string catches your eye that doesn’t look like the rest. Not a variable name, not a class hash — a value, long and opaque, shaped exactly like something that’s supposed to be secret.

This is the story of one of those moments: a hardcoded OAuth2 client\_secret sitting in plain text inside a large organization's public-facing code, wired directly into their AWS Cognito identity infrastructure. No obfuscation, no environment-variable indirection. Just... there.

I’m not naming the organization or publishing the value, the file path, or enough of the discovery technique to make this a how-to guide. What I want to share is *why* this bug class keeps happening, what it means when it does, and how to hunt for it responsibly — because if you do any web recon or frontend review, you’ve probably walked past this exact bug without noticing. It doesn’t look like a vulnerability. It looks like configuration.

OAuth2 client secrets exist to answer one question: *is this request really coming from an application I trust?* That trust model only works if the secret stays where only the trusted party can see it — never shipped to a browser or a mobile binary. The moment it crosses that line, it stops being a secret and becomes a public value with a misleading name.

*Top: the secret never leaves the backend. Bottom: it rode along in a client-accessible bundle — reachable by anyone with a browser’s network tab or a basic app-unpacking tool.*

Nobody sits down and decides to expose a secret. It happens gradually — a quick prototype wires it in “just for now,” a build script bundles a config file that was never meant to leave the repo, a mobile app embeds a credential to skip a round trip. The code works, the tests pass, nothing looks broken. And it ships.

Bug hunting doesn’t feel like discovery in the moment — it feels like elimination. Most leads are false positives; the real work is verification, not the initial spot.

I found the string during routine recon through public client-side bundles — its shape and entropy read like a real credential, and the surrounding context pointed at Cognito’s token endpoint. That made it a *candidate*, nothing more; plenty of credential-shaped strings turn out to be stale test values or documentation placeholders.

The part that actually took time was verification: confirming the value could successfully authenticate against Cognito’s token endpoint, proving it was live, trusted infrastructure — not a rotated or dead credential. The response came back with a valid token — proof the secret wasn’t dead weight from an old deployment, but an active credential the identity provider still trusted. From there I mapped exactly what the secret’s scopes allowed, without exercising anything beyond what was needed to confirm impact, and reported it through the program’s disclosure process.

Anyone can grep a bundle for suspicious strings. Separating a real, exploitable secret from noise — without touching anything beyond what’s needed to prove the point — is what separates a useful report from a false-positive ticket.

This wasn’t a small product. It was infrastructure serving a large user base, built by teams that presumably run security reviews and CI/CD scanning — and the secret still shipped, client-accessible.

A few reasons this pattern persists: secrets don’t announce themselves in a diff the way a logic bug does; automated scanners catch known formats far more reliably than custom ones, and often only run against source repos, not shipped build artifacts; and “temporary” code has a way of becoming permanent because nobody owns removing it before release.

***A secret doesn’t stop being a secret because nobody’s looked yet.***

None of this is a knock on the engineers involved — it’s a systems problem, not a competence problem. Which is exactly why it’s worth writing about instead of quietly reporting and moving on.

The most dangerous vulnerabilities aren’t always the flashiest ones. A hardcoded secret isn’t a clever exploit chain — it’s a value that was never supposed to leave the building, sitting in a place anyone could find with nothing more than developer tools and patience.

The fix isn’t a smarter WAF rule or a better scanner. It’s treating “what does the client actually receive” as a first-class security question, every time something ships.

*This writeup is intentionally anonymized and generalized — no identifying details, exact values, or reproduction steps are included.*
