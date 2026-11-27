# Your First Android Bug Bounty Report

- **Source URL:** https://medium.com/@akifkhan0120/your-first-android-bug-bounty-report-from-finding-to-payout-in-2025-444cb4888bcd?source=rss------bug_bounty-5
- **Fetched from:** https://medium.com/feed/@akifkhan0120
- **Fetched:** 2026-11-27
- **Channel:** @dailybountywriteup
- **Telegram message:**  (id 13799)
- **Method:** medium-rss-content readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
**Tags:** bug-bounty android-security mobile-pentesting ethical-hacking cybersecurity hackerone bugcrowd infosec career beginner

**Estimated read time:** 22 minutes

“Finding the bug is 40% of the work. The report is the other 60%.” *— Every senior bug bounty researcher, eventually*

### The Moment Nobody Warned You About

You found it.

You changed a username parameter in Burp Suite. Another user’s account data came back. You stared at the screen for a moment, confirmed it twice, opened a third account and tested again. It worked every time.

You have a real IDOR vulnerability in a real application with a live bug bounty program.

And then you open the submission form — and freeze.

*Severity: Critical / High / Medium / Low? Title: how specific? how technical? Steps to reproduce: how much detail? Impact: what exactly do I write here? CVSS score: what is that?*

You spend forty minutes writing something. You submit. Three days later you get a response:

Status: Informational

Triager note: Unable to reproduce. Please provide more detailed

reproduction steps. Closing as informational.

Your finding was real. Your report got it closed as not actionable.

This is the wall between Parts 1–5 of this series and actual income. You now know how to find vulnerabilities. This article teaches you how to communicate them in a way that gets paid.

Welcome to Part 6 — the series finale.

### Why Reports Fail (The Diagram You Need First)

Before writing a single word of a report, understand why good findings get rejected. It is almost never because the vulnerability was invalid.

WHY VALID FINDINGS GET CLOSED WITHOUT PAYMENT:

──────────────────────────────────────────────────────────────────

Finding is real

│

├─► Report cannot be reproduced by triager

│ └─► Closed: "Cannot reproduce"

│

├─► Impact is unclear or understated

│ └─► Downgraded: Medium → Low → Informational

│

├─► Out of scope (wrong app version, excluded endpoint)

│ └─► Closed: "Out of scope"

│

├─► Duplicate (someone filed it first)

│ └─► Closed: "Duplicate" (no payout)

│

├─► Missing proof of concept

│ └─► Triager cannot verify → sits in queue → expires

│

└─► Correct reproduction steps, clear impact, in scope,

with proof of concept

└─► PAID ✓

──────────────────────────────────────────────────────────────────

Every item in that list is a writing problem, not a technical problem. You found the vulnerability. The report is what stands between that finding and payment.

This article fixes each failure mode, one by one.

### Step 1: Choose the Right Program Before You Test Anything

**The moment of confusion:** You find a vulnerability in a popular app. You check HackerOne. The company has a program. You submit. You get back:

This vulnerability is out of scope for our program.

Specifically, our program excludes third-party libraries

and rate limiting issues.

You tested the right thing on the wrong program — or the right program with the wrong scope.

**Read the program policy before you open Burp Suite.** Every bug bounty program has a policy page that specifies:

- **In scope:** which apps, domains, and API versions are testable
- **Out of scope:** what is explicitly excluded (rate limiting, self-XSS, clickjacking, third-party components, and more)
- **Reward ranges:** what severity pays what
- **Safe harbour:** legal protections for good-faith researchers
- **Disclosure policy:** how long before you can publish

**How to find the right program as a beginner:**

Criteria for a good first program:

──────────────────────────────────────────────────────

✓ Response time \< 7 days (check HackerOne stats)

✓ Payout rate > 80% (triagers are fair)

✓ Android app explicitly in scope

✓ Wide scope (more endpoints = more attack surface)

✓ Clear reward table (no vague "bounties at our discretion")

✗ Avoid: "No bounties, hall of fame only" programs (for now)

✗ Avoid: Programs with response time > 30 days

──────────────────────────────────────────────────────

**Platforms to start with:**

**HackerOne** — largest platform, most structured, best for beginners. Filter by: Android → Has bounties → Sort by response efficiency.

**Bugcrowd** — strong mobile program portfolio. Good for researchers outside the US/EU — Bugcrowd has strong programs from APAC companies.

**Intigriti** — European platform, less saturated for many programs, faster response times on average.

**Google Play Security Reward Program** — specifically for Android apps on the Play Store. Pays $1,000–$300,000 depending on severity. Wide scope by definition — any app on the Play Store qualifies.

**The habit to build here:** Keep a spreadsheet of programs you want to test. For each one: scope in, scope out, reward table, average response time (visible on HackerOne program stats), and the date you last checked the policy. Policies change. A scope that excluded your finding last month may include it today.

**Now make it harder:** The app you want to test has no bug bounty program. You can still report responsibly — find the company’s security contact (usually security@company.com or a security.txt file at /.well-known/security.txt), report privately, and negotiate a response. This is called coordinated disclosure. It does not pay bounties, but it builds reputation and CVEs — both valuable early in your career.

### Step 2: Confirm and Document Before You Write Anything

**The moment of confusion:** You found the IDOR. You are excited. You open the report form immediately and start describing what you saw.

Three hours later, the triager asks if you tested on version 4.2.1 or 4.3.0, and whether the finding reproduces on a physical device or only on an emulator.

You do not know. You forgot to check.

**Before writing one word of a report, collect this information:**

\# 1. App version — check in the About screen OR:

adb shell dumpsys package com.target.app | grep versionName

# Output: versionName=4.2.1

\# 2. Android version of your test device

adb shell getprop ro.build.version.release

# Output: 10

\# 3. Device/emulator type

adb shell getprop ro.product.model

# Output: sdk\_gphone\_x86\_64 (emulator) or Pixel 6 (physical)

\# 4. Exact timestamp of your test (for the report)

date

# Output: Sun May 24 14:32:11 IST 2025

\# 5. Burp Suite request — export as raw HTTP

# Right-click request → Copy → Copy as curl command

# Save the exact request that demonstrated the vulnerability

**Screenshot everything:**

- The vulnerable request in Burp Suite (with the modified parameter highlighted)
- The response showing the other user’s data
- Your test account credentials (so the triager can reproduce with the same accounts)
- The normal request (without modification) for comparison

**Video proof of concept (when screenshots are ambiguous):**

\# Record emulator screen

adb shell screenrecord /sdcard/poc\_recording.mp4

# Interact with the app to demonstrate the finding

# Ctrl+C to stop recording

adb pull /sdcard/poc\_recording.mp4 ./

A 60-second screen recording showing the exploit working is worth more than five paragraphs of explanation. Triagers process dozens of reports per day. A video they can watch once is reproduced in their head without any effort.

**The habit to build here:** Before starting any test session, open a notes file with today’s date, the app version, Android version, and device type already filled in. Every finding gets its own section with a screenshot taken the moment you confirm it. Never leave a testing session without documentation — memory is unreliable, and you will test the same endpoint again in a month and not remember what you already found.

### Step 3: Score Your Finding Correctly

**The moment of confusion:** You submit a Critical. The triager downgrades it to Medium. You push back. They explain that because the data accessed is not sensitive (just a username and account ID) and requires authentication, the CVSS score is lower than you thought.

You had the right finding. You had the wrong severity.

**CVSS — the scoring system programs use:**

CVSS (Common Vulnerability Scoring System) is the standard severity calculation. Every professional report maps to a CVSS score. Understanding it prevents severity disputes.

The four most important CVSS metrics for mobile findings:

METRIC              OPTIONS                    SCORE IMPACT

──────────────────────────────────────────────────────────────

Attack Vector Network / Adjacent / Network = highest

Local / Physical

Authentication      None / Single / Multiple     None = highest

Required

Confidentiality     None / Partial / Complete    Complete = highest

Impact

Integrity Impact    None / Partial / Complete    Complete = highest

──────────────────────────────────────────────────────────────

**Severity guide for common Android findings:**

Finding Typical Severity Why IDOR — access other user’s PII High (7.5–8.9) Network, auth required, partial confidentiality IDOR — transfer funds for other user Critical (9.0+) Network, auth, complete integrity impact Broken auth — session not invalidated Medium (5.0–6.9) Requires physical access to token JWT alg:none bypass Critical (9.0+) Network, no auth, complete integrity Mass assignment — privilege escalation Critical (9.0+) Network, auth required, complete impact Hardcoded API key High–Critical Depends on what the key accesses Plaintext password storage Medium (5.0–6.9) Requires local access Sensitive data in logs Medium (4.0–6.9) Requires local access, limited scope Rate limiting bypass on login Low–Medium No direct data impact Exported activity — auth bypass High (7.0–8.9) Local access, complete auth bypass

**Use the official CVSS calculator:** first.org/cvss/calculator/3.1

Fill in each metric honestly. Programs trust researchers who score accurately — it builds a reputation as a reliable reporter. Researchers who always submit Critical get triaged more slowly.

**The habit to build here:** Calculate CVSS before writing the severity in your report. Copy the calculator URL into your report so the triager can verify your reasoning. A self-justified score is harder to dispute than an assertion with no backing.

### Step 4: Write the Report — The Exact Structure That Gets Paid

This is the template that senior researchers use. Every field matters. None are optional.

### Title

**Formula:** \[Vulnerability Type\] in \[Component/Endpoint\] allows \[Impact\]

❌ Bad:  "IDOR vulnerability"

❌ Bad: "I can see other users' data"

✓ Good: "IDOR in GET /api/v1/users/{id}/profile allows

authenticated users to access any account's

personal information without authorisation"

✓ Good: "Unauthenticated access to POST /transfer endpoint

via JWT algorithm confusion allows arbitrary

fund transfers from any user account"

The title should tell the triager: what type of bug, where it is, and what an attacker can do with it — before they read a single other word.

### Severity

State your CVSS score and link the calculator. Do not just write “Critical.” Write:

Severity: High (CVSS 3.1 Score: 8.1)

CVSS Vector: AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:N

Calculator: https://www.first.org/cvss/calculator/3.1#AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:N

### Description

Two to four sentences. What the vulnerability is, why it exists, and why it matters. Technical but readable by a developer, not just a security researcher.

```
The /api/v1/users/{id}/profile endpoint returns full user profile
data — including name, email, phone number, and home address —
based solely on the user ID supplied in the URL path parameter.
The server validates that the requesting user is authenticated
but does not verify that the authenticated user is authorised
to access the requested profile ID.
```
This allows any authenticated user to retrieve the personal

information of any other user in the system by iterating or

guessing user IDs, with no indication to the victim that their

data has been accessed.

### Steps to Reproduce

Numbered. Exact. Reproducible by someone who has never seen your screen. Assume the triager is competent but has zero context about what you did.

Environment:

App version: com.target.app v4.2.1

Android version: 10 (API 29)

Test device: Android emulator (x86\_64)

Test date: 24 May 2025

Prerequisites:

Two accounts are required to demonstrate this finding.

Account A (attacker): username=testuser\_a, password=TestPass@123

Account B (victim): username=testuser\_b, password=TestPass@456

Both accounts can be registered through the app's signup flow.

Steps:

1. Register Account B and note the user ID assigned

(visible in the /dashboard response as "userId": 1235)

2\. Log in as Account A using the app or directly:

POST /api/v1/login

{"username": "testuser\_a", "password": "TestPass@123"}

Save the session token from the response.

3\. Using Account A's session token, send the following request:

GET /api/v1/users/1235/profile HTTP/1.1

Host: api.targetapp.com

Authorization: Bearer \[Account\_A\_token\]

4\. Observe that the response returns Account B's full profile:

{

"userId": 1235,

"username": "testuser\_b",

"email": "testuser\_b@example.com",

"phone": "+91-XXXXXXXXXX",

"address": "123 Example Street, Mumbai"

}

5\. Account A has accessed Account B's personal data

using only Account B's user ID — no other credentials required.

### Proof of Concept

Attach:

- Screenshot of the vulnerable request (Burp Suite)
- Screenshot of the response containing the other user’s data
- Side-by-side screenshot showing Account B’s data in Account A’s session
- (Recommended) Screen recording of the full reproduction

If the vulnerability requires a script to demonstrate:

\# poc\_idor.py

import requests

TARGET   = "https://api.targetapp.com"

TOKEN\_A = "Bearer eyJhbGci..." # Account A's token

VICTIM\_ID = 1235 # Account B's user ID

```
headers = {"Authorization": TOKEN_A}
response = requests.get(
    f"{TARGET}/api/v1/users/{VICTIM_ID}/profile",
    headers=headers
)
```
```
print(f"Status: {response.status_code}")
print(f"Data:   {response.json()}")
# Expected if vulnerable:
# Status: 200
# Data: {"userId": 1235, "email": "testuser_b@...", ...}
```
### Impact

This is the section most beginners write too briefly. Impact is not “the attacker can see user data.” Impact is what that means in the real world.

An attacker who exploits this vulnerability can:

1\. Enumerate all registered user accounts by iterating user IDs

sequentially (user IDs appear to be assigned incrementally

starting from 1000).

2\. Harvest personal information (names, email addresses, phone

numbers, home addresses) for all users without their knowledge

or consent — a GDPR and PDPA compliance violation.

3\. Use harvested phone numbers and email addresses for targeted

phishing, SIM swap attacks, or social engineering.

4\. In combination with the /transfer endpoint (separate finding),

use harvested account IDs to initiate fraudulent transfers.

At the time of testing, the application had approximately

50,000 registered users based on the highest observed user ID.

All 50,000 accounts are affected.

The last paragraph — the affected user count — elevates every IDOR from “one user’s data” to a scale that justifies the severity rating.

### Remediation

Tell the developer exactly how to fix it. Vague remediation wastes their time. Specific remediation gets the report marked as high quality and gets you a reputation as a thorough researcher.

Recommended fix:

```
On every request to /api/v1/users/{id}/profile, verify that the
authenticated user's ID (extracted from the validated session token)
matches the requested {id} parameter before returning profile data.
```
Example pseudocode:

def get\_profile(request, user\_id):

authenticated\_user = get\_user\_from\_token(request.headers\["Authorization"\])

if authenticated\_user.id != user\_id and not authenticated\_user.is\_admin:

return 403 Forbidden

return User.get(user\_id)

Admin users may legitimately access other profiles — implement

role-based access control to allow this without opening the

endpoint to all authenticated users.

### Step 5: Submit, Follow Up, and Handle Responses

**After submitting — what to expect and when:**

Day 1–3:    Automated acknowledgement (most platforms)

Day 3–7: Triager reviews and responds

→ "Triaging" means it is being looked at

→ "Need more info" means your repro steps need detail

Day 7–21: Developer confirms or disputes the finding

Day 21–60: Fix developed and deployed

Day 60–90: Bounty paid (sometimes faster, sometimes slower)

**If you get “Need more information”:**

Read exactly what they asked. Answer exactly that question. Do not rewrite the entire report. Do not add new findings. Do not ask why it was downgraded. Answer the specific question, add any missing evidence, and close your response with:

Please let me know if you need any additional information

to reproduce this finding. Happy to jump on a call if that

would help resolve it faster.

**If you get a severity downgrade:**

You can dispute it — once, politely, with evidence. Provide the CVSS calculation you believe is correct and explain each metric choice. Accept the triager’s final decision gracefully. Getting a reputation as a difficult reporter is more damaging to your career than accepting one downgraded finding.

**If you get “Duplicate”:**

This means someone else found it first. You get nothing — but this is valuable information. It tells you that you found a real vulnerability that was worth reporting. You are testing at the right level. Keep going.

**If you get “Out of scope”:**

Re-read the program policy carefully. If you genuinely believe it should be in scope, ask once: “Could you clarify why this falls outside scope? The policy states \[specific quote\] which I believed covered this endpoint.” If they confirm it is out of scope, move on.

**The habit to build here:** Keep a report tracker — a simple spreadsheet with columns for: program, finding title, submission date, current status, payout received. Review it weekly. Follow up on reports that have been in “Triaging” for more than 14 days with a single polite message: “Happy to provide additional information if needed.”

### Step 6: Build Your Reputation Over Time

The researchers earning significant income from bug bounty are not finding new vulnerabilities every day. They are finding vulnerabilities consistently, reporting them professionally, and building a reputation that gets their reports triaged faster and paid more generously.

**What builds reputation:**

**Report quality.** Every report you submit that is clear, reproducible, and well-scoped makes the next report from your handle get taken more seriously. Triagers remember handles associated with quality.

**Volume of valid findings.** Submitting 10 low-quality reports harms your reputation. Submitting 3 well-documented valid findings builds it. Quality always beats quantity.

**Responsiveness.** When a triager asks for more information, responding within 24 hours — with exactly what they asked for — signals professionalism.

**Writeups.** After a finding is fixed and the disclosure period has passed, write a public technical walkthrough. Post it on Medium (your existing series is already building this habit). Writeups are read by security teams at other companies who run bug bounty programs. Researchers who publish writeups get invited to private programs — where competition is lower and payouts are higher.

**The HackerOne reputation system:** HackerOne specifically uses a reputation score that affects which programs you can access. Every valid report earns reputation points. Duplicate and informational reports lose points. Keep your signal:noise ratio high.

### Real Payout Examples — What This Actually Looks Like

These are real disclosed reports from HackerOne and Bugcrowd (details generalised):

**Finding: IDOR in profile endpoint, financial app** Researcher: India-based, 8 months experience Report quality: Clear steps, video PoC, CVSS calculated Response time: 4 days to triage, 18 days to fix Payout: $3,500 (High severity)

**Finding: JWT alg:none bypass, fintech app** Researcher: Philippines-based, first year of bug bounty Report quality: Python PoC script, full impact statement, CVSS 9.1 Response time: 2 days to triage, 11 days to fix Payout: $8,000 (Critical)

**Finding: Hardcoded API key in APK, e-commerce app** Researcher: Nigeria-based, second-ever submission Report quality: JADX screenshot, curl verification command, remediation Response time: 6 days to triage, 30 days to fix Payout: $2,000 (High)

**Finding: Exported activity — auth bypass, banking app** Researcher: Indonesia-based, 3 months experience Report quality: ADB command to reproduce, before/after screenshots Response time: 3 days to triage, 14 days to fix Payout: $4,500 (High)

None of these researchers had degrees in computer science. None had years of professional experience. They had the skills from a series exactly like the one you just finished — and they could write a report that communicated those findings clearly.

### Your Complete Android Pentesting Series — What You Have Built

Across six articles, starting from an empty emulator, you have built a complete mobile security testing capability:

Part Topic What you can do now 1 ✅ Android Pentesting Intro Set up a lab, read manifests, intercept traffic 2 ✅ Frida Deep Dive Hook any function, bypass auth, dump crypto keys 3 ✅ SSL Pinning Bypass Defeat every pinning implementation, ranked 4 ✅ Banking App Walkthrough Full assessment of a realistic target, 8 vulnerability classes 5 ✅ Android API Security Testing IDOR, broken auth, mass assignment, rate limiting, business logic 6 ✅ (this) Your First Bug Bounty Report Write findings that get paid, build lasting reputation

That is a complete Android security skillset — from zero to employable.

### One Strong Recommendation

Every technique in this series stays current for about 18 months before the tools evolve enough to need updating. One resource stays relevant permanently: **the HackerOne Hacktivity feed** at hackerone.com/hacktivity.

Hacktivity is a public feed of disclosed bug bounty reports from hundreds of programs. Filter by: Android → High and Critical severity → Last 6 months.

Read ten of these reports. Not to copy the findings — to study the writing. Notice how top researchers structure their titles. Notice how they calculate impact. Notice how they write reproduction steps.

This is the equivalent of Keith McNulty’s advice to “write down what you know before computing anything.” Before writing your next report, read three recent disclosed reports on the same platform. Your report will be measurably better for it.

The Hacktivity feed is free, updated daily, and is the single best education in bug bounty report writing that exists.

### What Comes Next

The Android series is complete. But the methodology you have built transfers directly to new targets:

**iOS App Pentesting** — same Frida, same Objection, same API testing methodology. Different platform, higher bounty rates. The next series starts exactly where this one ended.

**Web Application Hacking** — every API testing technique from Part 5 works on web APIs. IDOR, broken auth, mass assignment, rate limiting — identical classes, browser-based tooling.

**The Bug Bounty standalone guide** — a single article covering the full bug bounty ecosystem: platforms, programs, income reality, and career path. The highest-traffic article this series can feed.

The foundation is built. Where you take it next is your decision.

*Submitted your first report after reading this series? Drop the finding type in the comments — no targets, no details, just the vulnerability class. Seeing what the community finds first tells me what Part 7 should cover.*

*Thank you for following this series from Part 1. Building something complete is harder than building something good. You did both.*

*All techniques in this series are for educational purposes only. Always test within authorised scope. Responsible disclosure is not optional — it is what separates security researchers from criminals.*

**SEO Meta Description:** Complete guide to writing your first Android bug bounty report in 2025 — covering program selection on HackerOne and Bugcrowd, CVSS scoring, exact report structure with title description steps to reproduce impact and remediation, handling triager responses, and building long-term reputation. Part 6 closing the Android pentesting series.

**Focus Keywords:** android bug bounty report writing 2025, how to write bug bounty report, HackerOne first report beginner, CVSS scoring bug bounty, android vulnerability report template, bug bounty payout android, mobile security bug bounty guide, responsible disclosure android
