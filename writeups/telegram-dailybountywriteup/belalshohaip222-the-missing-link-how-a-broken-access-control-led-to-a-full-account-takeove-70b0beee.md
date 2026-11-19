# The Missing Link

- **Source URL:** https://medium.com/@belalshohaip222/the-missing-link-how-a-broken-access-control-led-to-a-full-account-takeover-ato-607436c5b636?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20260509150327/https://medium.com/@belalshohaip222/the-missing-link-how-a-broken-access-control-led-to-a-full-account-takeover-ato-607436c5b636
- **Fetched:** 2026-11-19
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/13355 (id 13355)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# The Missing Link: How a Broken Access Control Led to a Full Account Takeover (ATO)

## Introduction: The Illusion of Security

In modern web applications, the User Interface (UI) often acts as the first line of defense. It guides users, enforces rules, and prevents them from making invalid requests. But as Bug Bounty Hunters, we know one golden rule: **Never trust the client.** Just because the UI enforces a rule doesn’t mean the backend API does.

Recently, while hunting on a private bug bounty program (for a critical fleet management platform), I discovered a severe **Broken Access Control** vulnerability. The application appeared to enforce a strict “Current Password” check before allowing a password change. However, by understanding how the API requests were sequenced and finding a missing logical link, I was able to bypass this check entirely, escalating a temporary session compromise into a **Permanent Account Takeover (ATO)**.

Here is the story of how a seemingly secure password change mechanism was broken.

## The Premise: How the Password Change Was Supposed to Work

I started by observing the intended workflow. I logged into my test account, navigated to the profile settings, and clicked “Change Password.”

As expected, the UI presented a standard form requiring three fields:

1. Current Password
2. New Password
3. Confirm New Password

I filled out the form and intercepted the traffic using Burp Suite to see what was happening under the hood. I noticed that clicking “Save” triggered **two distinct API requests** in sequence:

**Request 1: The Authentication Check**

The client sent an `Authenticate` request to the `/apiv1` endpoint containing the *Current Password*.

If the server responded with a success (Valid Password), the UI proceeded to the next step.

**Request 2: The Update Request**

The client then sent a `Set` request to the same `/apiv1` endpoint, containing a massive JSON payload with the user's profile data, including a new key: `"password": "NewPassword123!"`.

Everything looked logical on the surface. The UI was doing its job perfectly. But my hacker mindset kicked in with a critical question: **How does the server know that Request 1 actually happened before processing Request 2?**

## The Missing Link: Server-Side Amnesia

I stared at the two requests. There was no temporary token, no specific authorization header, and no session flag linking the successful `Authenticate` request to the subsequent `Set` request.

The security of the password change relied entirely on the UI’s promise: *“I swear, Server, I already checked their old password. You can trust me to update it now.”*

To prove this theory, I decided to test if the server suffered from “Amnesia.” Could I just skip the Authentication step entirely?

## The Exploit: Bypassing the Current Password Check

The exploitation phase was incredibly straightforward:

1. I navigated to the target application using an active session (simulating a scenario where an attacker found an unlocked computer or hijacked a valid session cookie).
2. I did **not** use the UI to change the password.
3. Instead, I went directly to Burp Suite, took a generic `Set` profile update request, and manually injected the password change parameter into the JSON payload:
4. `"password": "Hacking@123"`
5. I sent this isolated `Set` request to the server, completely skipping the `Authenticate` request.

**The Malicious Payload:**

```
POST /apiv1 HTTP/2
Host: bugcrowd.target.com
Cookie: sessionId=0x46bkhhqCmDatRopL0Xgg;
Content-Type: text/plain;charset=UTF-8
```
```
{
  "method": "Set",
  "params": {
    "typeName": "User",
    "entity": {
      "id": "b5",
      "firstName": "Bugcrowd",
      "lastName": "Ninja",
      "name": "golden-meadow@bugcrowdninja.com",
      "password": "Hacking@123" 
    },
    "credentials": {
      "sessionId": "0x46bkhhqCmDatRopL0Xgg",
      "userName": "golden-meadow@bugcrowdninja.com"
    }
  }
}
```
I held my breath.

**Response:** `HTTP 200 OK`. The server processed the request.

I immediately opened a new incognito window and tried logging in with the victim’s email and my new password (`Hacking@123`).

**Login Successful.** I had successfully changed the password without ever knowing the current one. The Account Takeover was complete. 🎯

## The Impact: Why This is Critical

In the context of this specific application (a logistics and fleet management platform), an Account Takeover is not just a privacy issue; it’s an operational catastrophe.

By bypassing this check, an attacker can turn a temporary session compromise (like finding an unlocked terminal in a warehouse) into a **permanent lockout**.

If a Fleet Administrator’s account is hijacked:

- **Operational Paralysis:** The company loses real-time visibility over its vehicles and assets.
- **Safety Risks:** Critical alerts (accidents, harsh driving, panic buttons) cannot be monitored or addressed.
- **Financial Loss:** Inability to manage dispatching leads to delayed deliveries and violated SLAs.

The attacker effectively holds the real-world operations of the company hostage.

## The Root Cause & Remediation

The root cause of this vulnerability is a classic case of **Improper Access Control** and failing to enforce state or authorization on critical actions at the API level. The API endpoint (`POST /apiv1` with method: `Set`) updated user objects blindly without verifying if the context of the request (a password change) was authorized.

**How to fix it:**

- **Require Old Password in the Payload:** The most straightforward fix is to redesign the `Set` API request to explicitly require the `oldPassword` alongside the `newPassword` whenever a password change is attempted. The backend must validate the old password hash before committing the update.
- **Cryptographic Linking (Tokens):** Alternatively, if the two-step architecture is required, the `Authenticate` endpoint should return a short-lived, single-use token upon successful validation of the old password. The `Set` request must then require this exact token to authorize the password modification.

## Key Takeaways for Hunters 🕵️♂️

- **Don’t Trust the UI Workflow:** Just because a form asks for an “Old Password” or sends multiple sequential requests, doesn’t mean the backend actually enforces that sequence.
- **Look for the “Missing Link”:** Whenever you see a multi-step process (Step A validates, Step B executes), ask yourself: *How are these steps linked?* If there’s no cryptographic token or session flag linking them, try executing Step B directly.
- **Isolate and Modify:** Take standard profile update requests and try injecting sensitive parameters (like `"password"`, `"role"`, or `"email"`) to see if the server processes them blindly.

This bug was a fantastic reminder that sometimes the most critical vulnerabilities are hidden in plain sight, disguised by a well-designed User Interface.

**Happy Hacking! 🔥**

## Let’s Connect! 🌐

If you enjoyed this writeup, let’s stay connected! I regularly share bug bounty tips, methodologies, and security insights.

- **LinkedIn:** [Connect with me here](http://www.linkedin.com/in/belal-shohaip-5a34b7306) 👔
- **X (Twitter):** [Follow me here](https://x.com/BelScarabX) 🐦

**Don’t forget to drop 50 claps 👏 if you found this helpful!**
