# Could This Have Been a €1,000 Bug? My First Accepted Bug Bounty Report

- **Source URL:** https://vicricsec.medium.com/could-this-have-been-a-1-000-bug-my-first-accepted-bug-bounty-report-e44b8c75cd2c
- **Fetched from:** https://vicricsec.medium.com/could-this-have-been-a-1-000-bug-my-first-accepted-bug-bounty-report-e44b8c75cd2c?source=rss-30c177ba646d------2
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14952 (id 14952)
- **Method:** medium-rss-feed (full content:encoded) readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- **Author/Published (RSS):** Vicricsec / Mon, 19 Oct 2026 05:06:20 GMT

*From Out of Scope to Accepted: My journey to my first accepted security finding.*

Hi, I’m **Vikas Meena(Vicricsec)**, a cybersecurity researcher, bug bounty hunter, website developer, and digital marketer. I’ve worked on movie promotion campaigns, including *Krishna and Chitthi*, and marketing for an upcoming movie featuring Sapna Choudhary.

This is the story of my first accepted bug bounty report and what I learned along the way.

During manual reconnaissance, I discovered a publicly accessible resource associated with a container repository.

I noticed that it appeared to allow access without authentication, so I investigated further instead of making assumptions.

Using Burp Suite, I inspected HTTP requests and responses, examined the accessible metadata, and assessed the potential security impact.

My methodology involved:

The investigation revealed an access control issue that could expose internal repository information and container-related resources.

After submitting my report, I received an unexpected decision: **Out of Scope**.

It was disappointing, but I remained professional and continued learning.

Later, the company reviewed the report again. On 2 June 2026, it confirmed that the finding was legitimate and needed to be fixed.

My report was finally **Accepted** — my first accepted bug bounty finding!

*Figure 2: My report’s journey from Out of Scope to Accepted.*

The affected asset was classified as Tier 3 under the program’s reward structure. This asset did not offer standard payouts for the applicable severity categories.

Although the finding was accepted, the company awarded me a **€50 company bonus**.

Could a similar vulnerability on a bounty-eligible asset potentially receive €1,000 or more? Possibly, depending on the impact, severity, and program rules. However, €1,000 was not the official valuation of my finding.

This experience was about more than a €50 bonus. It was my first accepted report and a reminder to keep learning, improving, and hunting.

The journey wasn’t straightforward, but it taught me the value of persistence, technical investigation, and professional communication.

**Thanks for reading!**

**— Vikas (Vicricsec)**
