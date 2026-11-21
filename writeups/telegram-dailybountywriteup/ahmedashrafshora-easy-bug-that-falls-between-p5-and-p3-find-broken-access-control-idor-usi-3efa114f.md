# Easy Bug That Falls Between P5 and P3

- **Source URL:** https://medium.com/@ahmedashrafshora/easy-bug-that-falls-between-p5-and-p3-find-broken-access-control-idor-using-autoreisze-in-burp-6f427852a788?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250822013502/https://medium.com/@ahmedashrafshora/easy-bug-that-falls-between-p5-and-p3-find-broken-access-control-idor-using-autoreisze-in-burp-6f427852a788
- **Fetched:** 2026-11-21
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/9666 (id 9666)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Easy Bug That Falls Between P5 and P3: Find Broken Access Control & IDOR Using AutoReisze in Burp Suite

# Introduction

In the bug bounty world, sometimes the simplest methods yield the biggest results. Introducing **AutoReisze** — a Burp Suite extension that helps you easily and reliably find **Broken Access Control** and **IDOR** vulnerabilities.

This tool works by sending three requests per endpoint: one with the legitimate user’s cookies, one with attacker’s cookies, and one without any cookies at all. This approach quickly reveals whether access control mechanisms are properly enforced or if unauthorized access is possible.

No deep hacking skills are needed — just a sharp eye and this handy tool. Also, many organizations tend to downplay the severity of these vulnerabilities, but the risk level can vary case by case, ranging anywhere from P5 up to P2 depending on the impact.

Ready to learn how to use AutoReisze inside Burp Suite and level up your bug hunting? Let’s get started.

# Setting Up the Extension

To get started with the **Autorize** extension inside **Burp Suite**, follow these steps:

1. **Install Autorize** from the Burp Suite BApp Store.

- Open **Burp Suite** → Go to **BApp Store** → Search for **Autorize** → Click **Install**.
- Once installed, go to the **Autorize** tab inside Burp.

**2.** Setting Up Python for Burp Suite Extensions

1. Go to **Settings** in Burp Suite.
2. Navigate to **Extensions > Python Environment**.
3. Click on **“Select file”** and choose your Python interpreter (e.g., `/usr/bin/python3` on Kali Linux).

That’s it! Now Burp Suite can run any Python-based extension smoothly

If you’re unable to find the JSON file, no worries — here’s a direct link to a ready-made one you can customize

[https://repo1.maven.org/maven2/org/python/jython-standalone/2.7.3/jython-standalone-2.7.3.jar](https://repo1.maven.org/maven2/org/python/jython-standalone/2.7.3/jython-standalone-2.7.3.jar)

# How Autorize Works: Detecting Authorization Vulnerabilities with Three Requests

**Autorize** is a Burp Suite extension designed to simplify and speed up the detection of **authorization vulnerabilities**, such as **IDOR (Insecure Direct Object References)** and **Broken Access Control** — tasks which are often very time-consuming during penetration tests.

## What Does Autorize Do?

- You provide Autorize with session cookies from a **low-privileged user** (e.g., a normal user with limited access).
- Then, you browse the website as a **high-privileged user** (e.g., admin).
- Autorize automatically **repeats every intercepted request** three times with different cookies to check for unauthorized access:

1. **Original request with the high-privileged user’s cookies**
2. **Modified request with the low-privileged user’s cookies (the “attacker”)**
3. **Request with no cookies at all**

This process helps to detect if sensitive pages or functions accessible to high-privileged users can be accessed by low-privileged users or unauthenticated users, indicating a possible authorization flaw.

## How Does It Detect Vulnerabilities?

Autorize compares the **response lengths** (the size of the HTTP response) for these three requests:

- If the **original request** and the **modified (attacker) request** have **very similar response lengths**, this suggests the low-privileged user sees almost the same content as the high-privileged user — a strong sign of an authorization bypass.
- If the **request without cookies** returns a very different response (usually an error or login page), it confirms the difference between authenticated and unauthenticated access.
- If **all three responses are nearly identical**, it usually means the page or resource is public or not protected by authorization controls (e.g., a public “forgot password” page).

## How to Use Autorize in Practice

1. **Load the session cookies** of a low-privileged user into the extension.
2. **Activate Autorize** and start browsing the website as a high-privileged user.
3. Visit sensitive areas like **“Forgot Password”** or **admin-only pages**.
4. Autorize automatically sends the 3 requests per action and compares their lengths.
5. Review the results in the Autorize tab, where:

- **Red** means a possible bypass (authorization vulnerability detected).
- **Green** means proper enforcement (access control working correctly).
- **Yellow** means uncertain — may need fine-tuning of detection parameters.

Why Use Autorize?

- **Automates** a very tedious part of penetration testing.
- Quickly **flags possible access control issues** that require manual verification.
- Supports configuration to fine-tune detection sensitivity and select which requests to test

# The Vulnerability I Found in a Public Bug Bounty Program

During testing with the **Autorize** tool, I discovered multiple entry points where the **response lengths were identical** between requests with different session cookies. Investigating manually, I confirmed that it was possible to **access another user’s account by injecting their session cookie into my own session**.

This vulnerability falls under **Broken Authentication and Session Management > Session Fixation** with a **Remote Attack Vector (P3 severity)**

# Details

**Summary:**

An authentication bypass vulnerability was found due to improper session validation. By injecting attacker B’s session cookie into the browser where victim A was logged in, the attacker gained full access to victim A’s account, the **display name for the attacker’s account changed to victim’s name**.

**Exploitation Steps:**

1. **Open two different browsers:**

- Browser 1 logged in as victim (Account A).
- Browser 2 logged in as attacker (Account B).

1. **Extract session cookies of attacker (Account B)** using Burp Suite.
2. **Close Browser 2** (attacker’s session).
3. **Inject attacker’s cookies into Browser 1’s session** (victim’s browser) via the Burp Suite “Authorize” tool or browser tools.
4. **Observe requests in Burp Suite:**
Requests are sent twice — once with victim’s cookies, once with attacker’s cookies. Both return nearly identical responses (same length and content).
5. **Gain full access to victim’s dashboard and perform actions as if logged in as victim.**
6. **Session persistence through cache:**
Even after logout or session close, pressing the browser’s back button restored access to victim’s account using the injected cookies (Broken Cache behavior).

**Additional Discovery: Session Confusion**

- After injecting attacker’s cookies into victim’s session, the **display name for the attacker’s account changed to victim’s name**.
- This is caused by **session confusion in the GraphQL resolver**, which links the victim’s session data to the attacker’s cookies.
- The issue allows attackers to **inject crafted display names**, which can impersonate trusted users or trick others into phishing or taking dangerous actions.

Examples of malicious display names attackers can use:

- `help@yourbank.com`
- `🛡️Security-Team Update Required Immediately`
- `Visit` [http://hacker.com](http://hacker.com)

These names deceive users into believing the message is legitimate while it is crafted by the attacker to exploit user trust within the UI.

# Impact

This vulnerability can lead to **complete account takeover** and **UI deception attacks**, posing serious security and privacy risks to users and the organization

# But unfortunately

As usual, many programs try to downplay vulnerabilities to offer lower bounty rewards. For example, this issue was classified as **Broken Authentication and Session Management > Session Fixation > Local Attack Vector = P5**, even though it fits better as **Broken Authentication and Session Management > Session Fixation > Remote Attack Vector = P3**.

**About Me**

I’m Ahmed Ashraf Shora, a passionate cybersecurity student and bug bounty hunter dedicated to uncovering vulnerabilities and improving digital security. This finding is just one step in my ongoing journey to learn, explore, and contribute to the cybersecurity community.

Feel free to connect with me on LinkedIn to follow my progress and collaborate on future projects:

[LinkedIn: linkedin.com/in/ahmed-ashraf-shora-557ba3328](http://linkedin.com/in/ahmed-ashraf-shora-557ba3328)

This is only the beginning — I won’t stop until I make the internet a safer place.
