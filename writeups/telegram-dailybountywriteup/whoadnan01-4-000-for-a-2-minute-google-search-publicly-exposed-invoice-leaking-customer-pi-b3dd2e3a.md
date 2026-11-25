# ₹4,000 for a 2-Minute Google Search

- **Source URL:** https://medium.com/@whoadnan01/4-000-for-a-2-minute-google-search-publicly-exposed-invoice-leaking-customer-pii-7365bb80c6ab
- **Fetched from:** https://medium.com/@whoadnan01/4-000-for-a-2-minute-google-search-publicly-exposed-invoice-leaking-customer-pii-7365bb80c6ab?source=rss-25d89dee1af0------2
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14888 (id 14888)
- **Method:** medium-rss-feed (full content:encoded) readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- **Author/Published (RSS):** WhoAdnan / Sun, 30 Aug 2026 06:41:32 GMT

Sometimes, finding a security vulnerability doesn’t require sophisticated tools, complex exploitation, or advanced techniques.

In this case, a simple Google search was enough to uncover a publicly accessible invoice belonging to **redacted.com**. The document contained highly sensitive customer information, including personally identifiable information (PII), contact details, address information, order details, and payment-related information.

I responsibly disclosed the issue through the company’s **self-hosted bug bounty program**, and the organization validated the vulnerability and awarded a **₹4,000 bounty**.

The interesting part?

**The entire discovery took less than two minutes.**

**Target:** redacted.com

**Vulnerability Type:** Sensitive Information Disclosure / Publicly Accessible Sensitive Document

**Severity:** High *(depending on the organization’s security assessment and exact data exposed)*

**Bounty:** ₹4,000

**Discovery Method:** Google Search / Google Dorking

**Status:** Resolved / Disclosed Responsibly

I started with a simple Google dork to look for publicly indexed PDF documents belonging to the target:

site:redacted.com ext:pdf

The search returned several PDF files associated with the domain.

While reviewing the results, I noticed an invoice that was accessible directly from the search results without any authentication.

I opened the document expecting to find relatively harmless information.

Instead, the invoice contained a significant amount of sensitive customer information.

The publicly accessible invoice contained information such as:

The combination of these data points significantly increased the potential impact of the exposure.

***No authentication or special access was required to access the document.***

Anyone who discovered the indexed URL could potentially access the information.

The vulnerability could be reproduced using a simple search query:

Review the indexed PDF results.

Identify the publicly accessible invoice.

Open the PDF.

Observe that sensitive customer information is available without authentication.

For responsible disclosure, I did **not** download, distribute, or unnecessarily access additional customer records.

This was more than simply an accidentally exposed PDF.

The document contained multiple categories of sensitive information belonging to a customer. Public exposure of such information could potentially result in:

The severity of the issue is particularly concerning because **no technical exploitation was necessary**.

The information was already publicly accessible through a search engine.

One of the most interesting aspects of this finding was how little effort was required to discover it.

The entire process was essentially:

**Google → Dork → PDF → Sensitive Information**

⏱️ **Time to discovery: \~1–2 minutes**

This is a good reminder that security doesn’t always come down to complicated exploitation techniques.

Sometimes, the biggest vulnerabilities are hiding in plain sight.

After confirming that the document was publicly accessible and contained sensitive information, I reported the issue directly to **redacted.com’s self-hosted bug bounty program**.

I provided:

The vulnerable URL

Steps to reproduce

A description of the exposed information

Security impact

Screenshots/evidence with sensitive information appropriately redacted

I avoided accessing unnecessary additional records and did not publicly disclose the customer’s information.

The security team reviewed the report, confirmed the vulnerability, and subsequently rewarded the report with a **₹4,000 bounty**.

**Bounty Received: ₹4,000**

What started as a simple Google search resulted in the discovery of a genuine information disclosure vulnerability affecting customer privacy.

More importantly, the issue demonstrated that sensitive documents should never be assumed to be safe simply because they aren’t linked from a website’s visible pages.

If a document is publicly accessible, search engines and other indexing mechanisms may make it discoverable.

This finding reinforced a few important lessons:

You don’t always need an expensive toolset to discover security issues.

Basic search-engine reconnaissance can sometimes reveal valuable findings.

Invoices, receipts, customer documents, reports, backups, and internal files should be properly protected with authentication and authorization where required.

Organizations should regularly monitor what sensitive content is being indexed by search engines.

The vulnerability took only a couple of minutes to discover, but the information exposed could have significant consequences for affected customers.

This was probably one of the simplest bugs I’ve discovered — but also a great reminder of an important principle in cybersecurity:

***The complexity of finding a vulnerability doesn’t determine its impact.***

A two-minute Google search was enough to uncover sensitive customer information that should never have been publicly accessible.

The organization responded appropriately through its bug bounty program, validated the issue, and rewarded the report.

**Sometimes, you don’t need to hack the system. You just need to look where nobody else thought to look.** 🔎

If you found this write-up useful or you’re interested in cybersecurity, bug bounty hunting, and vulnerability research, feel free to connect with me:

**X (Twitter):** [@adnankai5ar](https://x.com/adnankai5ar)

**LinkedIn:** [Adnan K](https://www.linkedin.com/in/adnan-k-8b2a7926b/).

**Keep hunting. Keep learning. Keep securing. 🔐**
