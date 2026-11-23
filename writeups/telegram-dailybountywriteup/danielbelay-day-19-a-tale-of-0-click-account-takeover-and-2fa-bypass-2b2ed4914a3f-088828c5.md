# Day 19

- **Source URL:** https://medium.com/@danielbelay/day-19-a-tale-of-0-click-account-takeover-and-2fa-bypass-2b2ed4914a3f?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20261024063317/https://medium.com/@danielbelay/day-19-a-tale-of-0-click-account-takeover-and-2fa-bypass-2b2ed4914a3f
- **Fetched:** 2026-11-23
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/8896 (id 8896)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Day 19: A Tale of 0-Click Account Takeover and 2FA Bypass

This write-up by **Firas Fatnassi** describes two critical vulnerabilities: **a 0-click account takeover via password reset abuse** and a **2FA bypass due to API key leakage**.

## 0-Click Account Takeover

The researcher was testing the **password reset functionality** of a target website ([**https://redacted.com**](https://redacted.com)) when they discovered an **email parameter manipulation vulnerability**.

## Exploiting the Password Reset Mechanism

Initially, they attempted basic attacks like:

✔️ **Host header manipulation**

✔️ **Brute-forcing reset tokens**

However, these **did not work**.

Then, they analyzed the **password reset request**, which looked something like this:

```
{
  "email": "attacker@gmail.com"
}
```
🔍 **Idea:** What if the `"email"` parameter was changed from a **string** to an **array**?

So, they modified the request:

```
{
  "email": ["victim@gmail.com", "attacker@gmail.com"]
}
```
💡 **Result:** The server **sent the password reset link to both email addresses**!

## Attack Scenario

1️⃣ The attacker requests a **password reset**.

2️⃣ They intercept the request and **add the victim’s email** alongside their own.

3️⃣ The password reset email is sent to **both** emails.

4️⃣ The attacker **uses the link to reset the victim’s password** and takes over their account.

🚀 **Bug Impact: Full account takeover** with **zero user interaction!**

## Get dani3l’s stories in your inbox

Join Medium for free to get updates from this writer.

✅ The researcher reported the bug, and it was classified as a **critical vulnerability**.

## 2FA Bypass via API Key Leakage

Next, the researcher analyzed the **2FA mechanism**, which was enabled via **Google Authenticator** (6-digit TOTP codes).

Since brute-forcing the 2FA code was **impractical** due to:

❌ **Rate limits**

❌ **Time-based expiration (every 60 sec)**

They moved to **response manipulation testing** by:

✔️ Changing response values (`"success": "false"` → `"success": "true"`)

✔️ **Forced browsing** (attempting to access the dashboard directly)

✔️ Looking for **2FA-related parameters** (`"2FA_Enabled": "false"`)

## Discovering API Key Leakage

While inspecting the **login request response**, they noticed that the server **returned sensitive information, including an API key!**

```
{
  "user_id": "123456",
  "session_token": "abcdefg",
  "api_key": "API_SECRET_HERE"
}
```
📌 **Exploiting the API Key**

Since the researcher had **already read the API documentation**, they knew that the **API key allowed full access to the account**, effectively bypassing **2FA authentication**.

💡 **Impact: If an attacker had the victim’s credentials, they could access the victim’s account without 2FA, simply by using the leaked API key.**

## Key Takeaways & Lessons Learned

✔️ **Always test how password reset emails are handled** — Manipulating parameters can lead to **account takeover**.

✔️ **Check API responses carefully** — Sometimes, **critical information is leaked directly in the response**.

✔️ **Never assume a tested system is secure** — Other researchers had tested the platform but **missed these vulnerabilities**.

🔹 **Bonus 2FA Bypass Tip**

If an API allows authentication via **email and password**, test whether **2FA is enforced**. If not, 2FA can be **bypassed via API authentication**!

## Final Thoughts

The **development team fixed both vulnerabilities in under 2 hours** and rewarded the researcher with a **bug bounty**.

📢 **Moral of the story:**

🛠️ **Test everything, even if others have already looked at it.**

🔎 **Sometimes, the smallest details can lead to the biggest discoveries!**
