# 🛡️ Critical n8n Vulnerability with CVSS 9.9

- **Source URL:** https://thehackernews.com/2025/12/critical-n8n-flaw-cvss-99-enables.html
- **Fetched:** 2026-11-16
- **Channel:** @defendor_eng
- **Telegram message:** https://t.me/defendor_eng/1000 (id 1000)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
A critical security vulnerability has been disclosed in the [n8n](https://www.npmjs.com/package/n8n) workflow automation platform that, if successfully exploited, could result in arbitrary code execution under certain circumstances.

The vulnerability, tracked as **[CVE-2025-68613](https://nvd.nist.gov/vuln/detail/CVE-2025-68613)**, carries a CVSS score of 9.9 out of a maximum of 10.0. Security researcher [Fatih Çelik](https://fatihhcelik.github.io) has been credited with discovering and reporting the flaw. The package has about 57,000 weekly downloads, according to statistics on npm.

"Under certain conditions, expressions supplied by authenticated users during workflow configuration may be evaluated in an execution context that is not sufficiently isolated from the underlying runtime," the maintainers of the npm package [said](https://github.com/n8n-io/n8n/security/advisories/GHSA-v98v-ff95-f3cp).

"An authenticated attacker could abuse this behavior to execute arbitrary code with the privileges of the n8n process. Successful exploitation may lead to full compromise of the affected instance, including unauthorized access to sensitive data, modification of workflows, and execution of system-level operations."

The issue, which affects all versions including and higher than 0.211.0 and below 1.120.4, has been patched in 1.120.4, 1.121.1, and 1.122.0. Per the attack surface management platform Censys, there are [103,476 potentially vulnerable instances](https://censys.com/advisory/cve-2025-68613) as of December 22, 2025. A majority of the instances are located in the U.S., Germany, France, Brazil, and Singapore.

In light of the criticality of the flaw, users are advised to apply the updates as soon as possible. If immediate patching is not an option, it's advised to limit workflow creation and editing permissions to trusted users and deploy n8n in a hardened environment with restricted operating system privileges and network access to mitigate the risk.

[Google News](https://news.google.com/publications/CAAqLQgKIidDQklTRndnTWFoTUtFWFJvWldoaFkydGxjbTVsZDNNdVkyOXRLQUFQAQ),
