# Reflected Chaos

- **Source URL:** https://medium.com/@bonghaxor_34691/reflected-chaos-how-one-xss-vector-spawned-three-cves-f20e2df3275f?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250905084452/https://medium.com/@bonghaxor_34691/reflected-chaos-how-one-xss-vector-spawned-three-cves-f20e2df3275f
- **Fetched:** 2026-11-21
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/9704 (id 9704)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Reflected Chaos: How One XSS Vector Spawned Three CVEs

A routine bug bounty checks. A familiar endpoint. But one odd behavior caught my eye — a parameter that echoed back a payload with just a little too much trust.

What looked like a textbook XSS turned out to be a tripwire into three separate applications — each vulnerable, each exploitable, and each silently exposing its users to the invisible threat of script injection.

In a world where security filters give a false sense of protection, I followed the trail of `<script>` tags and JavaScript payloads into the heart of three CVE-worthy disclosures. This isn’t just about cross-site scripting. It’s about how overlooked assumptions, legacy frameworks, and chained misconfigurations can lead to exploitable realities in production.

Here’s how I uncovered the flaws, exploited them safely, and worked with vendors to fix them — before someone else could take advantage.

**Dissecting the Vulnerability: A Screenshot Walkthrough**

I have found this type of vulnerabilities in multiple endpoints. After analysing the PSIRT team send me below email confirming 3 CVEs:

Happy Hunting!!
