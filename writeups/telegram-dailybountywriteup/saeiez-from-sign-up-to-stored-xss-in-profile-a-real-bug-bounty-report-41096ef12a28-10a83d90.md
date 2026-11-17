# From Sign-Up to Stored XSS in Profile

- **Source URL:** https://medium.com/@Saeiez/from-sign-up-to-stored-xss-in-profile-a-real-bug-bounty-report-41096ef12a28?source=rss------bug_bounty-5
- **Fetched from:** https://medium.com/feed/@Saeiez
- **Fetched:** 2026-11-17
- **Channel:** @dailybountywriteup
- **Telegram message:**  (id 10679)
- **Method:** medium-rss-content readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
### 🧾 Introduction

In this post, I’ll walk you through how I discovered a **Stored XSS** vulnerability during a bug bounty program.

At first, the application seemed secure — any attempt to submit raw HTML tags was blocked with a *potentially dangerous Request.Form* error.

But with a small trick using encoded input, I was able to bypass this validation and achieve JavaScript execution in the profile page.

### 🧪 Testing Environment

The target was a web application running on **ASP.NET** (based on the error messages and behavior).

The sign-up and login forms had fields such as FName and LName where user data was collected.

### 🐞 Step 1: Raw Input Test

I first tried submitting a simple HTML tag:

\<saeed>

But the server immediately responded with:

A potentially dangerous Request.Form value was detected from the client (FName="\<saeed>")

So, raw \< and > characters were blocked by ASP.NET’s built-in **Request Validation**.

### 🎯 Step 2: Bypassing with URL Encoding

To bypass this, I encoded the payload:

d%22+onmousemove%3D%22alert(1)%22

**Which translates to:**

d" onmousemove="alert(1)"

This time, the request was **accepted without errors**. ✅

### 👀 Step 3: Rendering in Profile

During sign-up/login, nothing happened.

But later, when the data was displayed in the **profile form**, the input was rendered as part of an \<img> tag:

\<img src="/..../.../.../....?width=20&crop=0,0,20,20" alt="saeed d" onmousemove="alert(1)" />

The moment I hovered my mouse over the image, my PoC payload fired:

alert(1)

➡️ This confirmed a **Stored XSS** vulnerability, triggered every time the profile page is viewed.

### 💥 Impact

- Since this is **stored**, the payload executes for **every user** viewing the page.
- A real attacker could:
- Steal cookies or session tokens
- Inject phishing content
- Deface the page
- Load external malicious scripts

### 🛡️ Root Cause

1. Input validation existed on the **request side**, but could be bypassed via encoding.
2. On the **output side**, the application failed to sanitize or encode user data before rendering it into the DOM.

### 🛠️ Remediation

- Always apply **output encoding** (HtmlEncode) before rendering user data.
- Strip dangerous attributes like onmousemove, onerror, onclick, etc.
- Enforce **whitelisting** for allowed inputs instead of blacklisting.

### 🧾 Conclusion

- Input filtering alone is not enough — output encoding is essential.
- Even frameworks with built-in protections (like ASP.NET) can be bypassed if developers rely only on request validation.
- Stored XSS vulnerabilities can appear in places you least expect — in this case, a seemingly harmless profile field.

This was a great reminder for me that creativity and persistence often lead to impactful findings in bug bounty hunting. 🚀
