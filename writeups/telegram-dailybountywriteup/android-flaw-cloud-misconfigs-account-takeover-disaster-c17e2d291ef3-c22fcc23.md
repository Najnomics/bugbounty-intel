# Android Flaw + Cloud Misconfigs + Account Takeover = Disaster⚡

- **Source URL:** https://vettrivel007.medium.com/android-flaw-cloud-misconfigs-account-takeover-disaster-c17e2d291ef3?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20251105124733/https://vettrivel007.medium.com/android-flaw-cloud-misconfigs-account-takeover-disaster-c17e2d291ef3?source=rss------bug_bounty-5
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/11567 (id 11567)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Android Flaw + Cloud Misconfigs + Account Takeover = Disaster⚡

I can able to identify 6 vulnerabilities only by the exposure of strings.xml

### The Backstory

During a freelance Vulnerability Assessment and Penetration Testing (VAPT) engagement, I was tasked with testing a mobile and cloud application for a healthcare startup.

*After receiving scope and authorization from the client, I began my usual process:*

- **Reconnaissance**
- **Enumeration**
- **Vulnerability Assessment**
- **Escalating the Severity**

Little did I know that a single, common mistake in the Android app would unravel the entire security of their platform.

### The Initial Discovery — A Treasure Trove in `strings.xml`

My first step was to analyze the Android application (APK). I decompiled it, which is like unpacking a box to see all its contents. One of the first files I always check is `strings.xml`. This file typically holds simple text labels, but developers sometimes accidentally store secrets here.

And there it was, staring right back at me ,

**Hardcoded Firebase API keys and an open Google Cloud Storage (GCS) bucket URL.**


This was the “uh-oh” moment. What looked like a simple Sensitive Information Disclosure was actually the key to the kingdom. I knew I had to push further.

### Vulnerability 01: **Firebase Configuration Exposed Publicly**

The exposed API key led me straight to the associated web application. A quick look at the source code revealed the same Firebase configuration hardcoded in a JavaScript file.

The Endpoint:

`https://[REDACTED]/static/js/main.5aa76257.js`


This configuration is a “master key.” It contained the `apiKey`, `authDomain`, `projectId` and most critically the `storageBucket` address. With this, I knew exactly which Firebase project to target and had the credentials to interact with it.

### Vulnerability 02: Publicly Accessible Firebase Storage

With the `storageBucket` address from the leaked config, I decided to see if the door was locked. I used a simple `curl` command to ask the storage bucket for a list of its contents.

**Step-by-Step Exploitation:**

1. List all files in the bucket:

`curl -s "https://firebasestorage.googleapis.com/v0/b/[REDACTED].firebasestorage.app/o"`
The server responded with a JSON list of every single file. No authentication required.


2\. Download any file directly:

From the JSON response, I constructed a URL to download anything I wanted:

`https://firebasestorage.googleapis.com/v0/b/[REDACTED].firebasestorage.app/o/<FILENAME>?alt=media`
The impact was chilling. I could access:

- PDF patient reports
- ECG and heart signal data (.json files)
- Audio recordings of heartbeats (.wav files)
- Medical measurements (.txt files)
- etc..

This was a catastrophic privacy failure. It was like a hospital leaving all patient records in an unlocked filing cabinet in the lobby.

*Unauthenticated public access to Protected Health Information (PHI) is a nightmare scenario, violating regulations like HIPAA and GDPR.*


### Vulnerability 03: Insecure Authentication & Login Bypass

Knowing the data was exposed, I needed to see what an “authenticated” user could do. I used the leaked API key to create a new account directly through Firebase’s API.

**Step-by-Step Exploitation:**

1. Create a fake user account:

`curl -X POST \ "https://identitytoolkit.googleapis.com/v1/accounts:signUp?key=[REDACTED]" \ -H "Content-Type: application/json" \ -d '{ "email": "attacker@example.com", "password": "FakePassword123!", "returnSecureToken": true }'`
The server instantly created the account and provided a valid login token. No email verification was required.

I went to `https://[REDACTED].web.app/`, entered my fake credentials, and was granted full access to the user dashboard.


The application completely trusted accounts that had not verified their email. An attacker could create thousands of fake accounts to abuse the system.

*This broken authentication mechanism allowed anyone to become a “user,” bypassing a critical security control.*


### Vulnerability 04: The Exposed User Database

Publicly Accessible Firestore Database

Now I went for the crown jewels: the user database. I targeted the Firestore database using its public REST API.

**Step-by-Step Exploitation:**

I sent unauthenticated requests to the Firestore collections:

```
# Get all user data
curl -s "https://firestore.googleapis.com/v1/projects/[REDACTED]/databases/(default)/documents/users"
```
```
# Get all doctor data
curl -s "https://firestore.googleapis.com/v1/projects/[REDACTED]/databases/(default)/documents/doctors"
```
```
# Get all patient data
curl -s "https://firestore.googleapis.com/v1/projects/[REDACTED]/databases/(default)/documents/patients"
```
Again, no password was needed. The database returned everything:

- Full Names
- Email Addresses
- User IDs
- Etc ..

This was the final, devastating blow. An attacker now had a complete directory of every user and doctor on the platform, perfect for targeted phishing or identity theft.

*Mass exposure of PII is a severe breach of trust and privacy regulations.*


### The Devastating Chain Reaction

This wasn’t four separate bugs; it was a cascading failure.

1. **The Spark:** Hardcoded secrets in the mobile app.
2. **The Escalation:** Misconfigured cloud storage rules, exposing medical data.
3. **The Bypass:** Broken authentication, allowing fake account access.
4. **The Breach:** Misconfigured database rules, exposing all user PII.

A single misconfiguration led to a total system compromise. An attacker could have stolen the entire user database, exfiltrated private medical records, and used the platform maliciously.

### The Fix & Lessons

I reported all issues immediately. The client acted swiftly to:

1. Rotate all exposed API keys and secrets.
2. Implement strict Firebase Security Rules requiring authentication for all database and storage access.
3. Enforce email verification before granting any application access.
4. Remove sensitive configuration from client-side code.

**Key Takeaways for Developers:**

- Never hardcode secrets in client-side code (mobile apps, JavaScript). Always use secure backend environments.
- The “public” flag in cloud security rules is DANGEROUS. Always default to “deny” and add “allow” rules for authenticated users.
- Always enforce email verification if you use email-based authentication.
- Assume your client-side code is public. Any secret there *will* be found.

If you need professional VAPT done (limited budget, but with full quality):

→ DM me or mail me at uvettrivel007@gmail.com.

→ I’ll handle the technical part; you’ll get the report, the fixes, and the peace of mind. 😇

I’ll catch up with you later with another interesting topic.

Stay tuned, and feel free to connect with me on LinkedIn: [VETTRIVEL U](https://web.archive.org/web/20251105124733/https://www.linkedin.com/in/vettrivel2006).

Thank you for reading! : )
