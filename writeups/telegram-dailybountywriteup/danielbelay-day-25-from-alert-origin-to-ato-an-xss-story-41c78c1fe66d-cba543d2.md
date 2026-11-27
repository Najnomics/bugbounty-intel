# Day 25

- **Source URL:** https://medium.com/@danielbelay/day-25-from-alert-origin-to-ato-an-xss-story-41c78c1fe66d?source=rss------bug_bounty-5
- **Fetched from:** https://medium.com/feed/@danielbelay
- **Fetched:** 2026-11-27
- **Channel:** @dailybountywriteup
- **Telegram message:**  (id 9031)
- **Method:** medium-rss-content readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
### Day 25: From alert(origin) to ATO — An XSS Story

Today’s **Account Takeover (ATO) vulnerability** was discovered by **Remmy**. This case highlights how a **Stored XSS vulnerability** was exploited to steal **session cookies** and fully compromise user accounts.

### Step 1: Discovering the XSS Vulnerability

🔎 **Initial Recon & Testing**

- Discovered a **React-based web application** but knew that some features might still use **vanilla JavaScript**.
- Tested different inputs **(manual fuzzing)** across functionalities.

💡 **The Breakthrough: Nickname Editing Feature**

- The **nickname editor** allowed users to set a fancy nickname.
- **Expanded view** allowed additional customizations.
- **Nickname reflected in the URL and profile page.**

### Step 2: Bypassing Input Filters & WAF Protections

🛠️ **First Tests:**

- \< was **reflected**, indicating potential for XSS.
- **Blocking on valid tags** (e.g., \<img src=x>).

🛠️ **Fuzzing Inputs:**

- Used **PortSwigger**, tested multiple encodings (Unicode, HEX, etc.).
- **Success:** Injected an XSS payload using **HTML-encoded tab characters** (	).
- **Final Payload:**
- \<	i	m	g	 	s	r	c	x	=	 	o	n	e	r	r	o	r	=	a	l	e	r	t	(	o	r	i	g	i	n	)	>
- **Bypassed regex-based filters!**

### Step 3: Response Manipulation to Bypass Character Limits

🔐 **Problem:**

- Nickname input had a **32-character limit**, but the payload was **161 characters**.

🔄 **Solution:**

- **Modified server response**:
- Changed "status": "failed" → "status": "success".
- Adjusted HTTP response codes to **bypass the restriction**.
- Successfully **injected the XSS payload** and triggered execution.

🚨 **Impact:** The script **executed when victims viewed the attacker’s profile.**

### Step 4: Escalating XSS to Account Takeover (ATO)

🔥 **Goal:** Steal the **victim’s session cookies** and gain unauthorized access.

💻 **Plan:**

1. **Write a payload** to exfiltrate **session cookies**.
2. **Deploy** it in the nickname field.
3. **Trigger execution** when victims **viewed the attacker’s profile.**
4. **Profit 😈** — Hijack their session and take over their account.

💥 **Execution:**

- The **XSS payload successfully stole authentication cookies**.
- The attacker **imported the session**, bypassing login **without credentials**.

🚨 **Impact: Full account takeover (ATO) achieved!**

### Step 5: Report Submission & Outcome

📌 **Reported:** Submitted a detailed **PoC (Proof of Concept)**.

📌 **Tested on own account — 100% working.**

📌 **Status: Closed as a duplicate** (another pentest team had already reported it). 😢

💡 **Lesson Learned:**

- Even if your finding is valid, **timing matters** in bug bounty.
- **Stored XSS → ATO escalation is a real-world risk!**

### Prevention & Fixes

✅ **Filter & Encode User Input Properly**

✅ **Use a Web Application Firewall (WAF) with Advanced Detection**

✅ **Set HTTP Only & Secure Flags on Cookies**

✅ **Implement a Strong Content Security Policy (CSP)**

### Final Thoughts

🚀 **XSS is NOT just “alert(1)” — It can lead to full Account Takeover (ATO)!**

🎯 **Lesson of the day:**

💡 **Think beyond basic exploitation — Always escalate impact!**

🔥 **Another day, another Account Takeover!** 💰
