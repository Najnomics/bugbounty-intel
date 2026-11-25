# How a Re-Authentication Feature Unintentionally Bypassed 2FA Entirely

- **Source URL:** https://medium.com/@omarelza3im44/how-a-re-authentication-feature-unintentionally-bypassed-2fa-entirely-7be9dc750ef3
- **Fetched from:** https://medium.com/@omarelza3im44/how-a-re-authentication-feature-unintentionally-bypassed-2fa-entirely-7be9dc750ef3?source=rss-9f0daf2ee15a------2
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:**  (id 14893)
- **Method:** medium-rss-feed (full content:encoded) readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- **Author/Published (RSS):** Omar Zaky / Tue, 01 Sep 2026 20:42:57 GMT

Finding a logic flaw always comes with a unique kind of excitement — especially when it relies purely on how an application handles user state rather than complex payloads.

A while back, I stumbled upon a classic logic bug in a target application where the built-in Re-Authentication mechanism completely invalidated the protection of Two-Factor Authentication (2FA). Even though this report ultimately turned out to be a Duplicate, the execution path and root cause make for a fascinating case study in session management vulnerabilities.

The Scenario 🎭

The target application had 2FA enforced for sensitive account actions and logins. However, it also possessed a common UX feature: if your session had been inactive or partially expired, navigating directly to a sensitive internal endpoint (like /settings) wouldn't immediately kick you out to the full login page.

Instead, the application presented a Re-Authentication Prompt asking only for the primary password to confirm identity before allowing access to the settings.

The Flaw Step-by-Step 🚶♂️

Long-Term Inactivity:Assume an account has 2FA enabled. The user logs out or leaves the browser session inactive for an extended period (even up to a month).

Direct Navigation:Instead of visiting /login and going through the standard credentials + 2FA flow, you navigate directly to a restricted URL such as \[https://target.com/settings\](https://target.com/settings).

The Re-Auth Trigger: The backend recognizes an expired or partial session token and halts full access, redirecting you to a prompt: “Please enter your password to continue to Settings.”

The Bypass:You enter the primary account password. The server validates the password, grants access to /settings, and simultaneously updates the session state to Fully Authenticated.

Full Unrestricted Access:From that moment on, you can freely browse the entire application — Dashboard, Profile, Billing, and internal actions — without ever being prompted for a 2FA OTP token.

What Went Wrong Under the Hood? 🧠

This issue stems from Inadequate State Verification during Privilege Elevation (Re-Authentication Flaw).

Partial Session Retention: The application failed to completely invalidate and destroy long-lived session cookies on the server side after expiration.

Flawed State Transition: When the user supplied the correct password at the /settings prompt, the backend logic assumed the identity verification was complete. It refreshed the session flag to AUTHENTICATED=TRUE across the entire application context, completely forgetting to check whether the account had 2FA enabled (IS\_2FA\_VERIFIED).

In short, the application treated a quick password check as an absolute substitute for the entire multi-factor authentication pipeline.

Remediations 🛡️

Enforce Unified Auth Checks: Any action or prompt that elevates a session from expired/unverified to fully authenticated must evaluate all required authentication factors (Password + 2FA).

Strict Session Invalidation: Invalidate and clear stale session tokens completely on timeout rather than leaving them in a semi-active state that accepts re-authentication shortcuts.

Contextual Permissions: Re-authentication prompts for sensitive actions should only grant narrow, localized permissions rather than elevating the global session state.

Even when a finding turns out to be a duplicate, exploring how state machines fail behind the scenes is always a great exercise in logic testing. Never underestimate simple endpoint manipulation! 🚀
