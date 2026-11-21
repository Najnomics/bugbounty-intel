# My Simple Method to Test for IDOR Vulnerabilities

- **Source URL:** https://medium.com/@ibtissamhammadi1/my-simple-method-to-test-for-idor-vulnerabilities-5963f6ed8785?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250905105302/https://medium.com/@ibtissamhammadi1/my-simple-method-to-test-for-idor-vulnerabilities-5963f6ed8785
- **Fetched:** 2026-11-21
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/10334 (id 10334)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
Member-only story

# My Simple Method to Test for IDOR Vulnerabilities

## **I found a bug — but it was marked as duplicate. Here’s how I did it.**

That was my first big lesson in **bug bounty hunting**. The vulnerability? **Insecure Direct Object References (IDOR)**, a sneaky flaw that lets attackers access data they shouldn’t.

**Privilege escalation** and **broken access control (BAC)** are two sides of the same dangerous coin. If a system doesn’t properly check **who you are**, you might end up deleting users, editing permissions, or even accessing admin panels, **without any hacking skills**.

Most automated scanners miss these flaws. That’s why I rely on a **manual-only approach** using **Burp Suite** and **Notion**. Here’s my step-by-step method — **no fancy tools required**.

### Step-by-Step Methodology

**Step 1: Permission Mapping (The Notion Trick)**

Before testing, I **documented every role’s permissions** in **Notion**. Example:

“As a Contracts Manager, I could approve contracts — but according to the rules, I shouldn’t be able to delete users. Does the API enforce this?”


This helped me **spot inconsistencies** later.

**Step 2: Token Harvesting (Burp Suite Magic)**
