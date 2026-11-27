# Google Pixel Lock Screen Bypass

- **Source URL:** https://masimshahzad.medium.com/google-pixel-lock-screen-bypass-the-70k-sim-swap-ed6821e4e6b1
- **Fetched from:** https://masimshahzad.medium.com/feed
- **Fetched:** 2026-11-27
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/15000 (id 15000)
- **Method:** medium-rss-content readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
A forgotten SIM PIN led David Schütz to a race condition that unlocked locked Pixel phones, no fingerprint or passcode. Google paid $70K

*AI-assisted: drafted with AI help from public sources, then reviewed and edited. This is an analytical case study of a public disclosure, not my own discovery.*

Hand someone your locked phone, and they hand it back unlocked: no PIN, no fingerprint, no malware. That was the Google Pixel lock screen bypass David Schütz found in 2022, after a dead battery and a forgotten SIM PIN. Anyone with physical access and their own PIN-locked SIM could reach the home screen. Google fixed it as CVE-2022–20465 and paid $70,000.

***Disclaimer:*** *Educational and defensive use only. This was fixed in the November 2022 Android security update. Reproduction steps are intentionally omitted.*

### Vulnerability Overview

- **Type:** Lock screen authentication bypass caused by a race condition in the lock screen’s “security screen” stack
- **CWE (analytical mapping):** CWE-362 (Race Condition), CWE-305 (Authentication Bypass by Primary Weakness)
- **CVE:** CVE-2022–20465. Android’s November 2022 bulletin rates it High (elevation of privilege, Android 10 to 13); NVD scores it CVSS 3.1 4.6 Medium, reflecting the physical access requirement
- **Bounty:** $70,000 from the Android VRP, paid as an exception after the report was first closed as a duplicate

### How the Google Pixel Lock Screen Bypass Worked (high level)

Schütz noticed something odd after resetting his SIM with its PUK code: the phone showed a fingerprint prompt straight after a reboot, when it should have demanded the passcode. Repeating the SIM reset the next day on a phone that was merely locked, he landed on his own home screen. It reproduced on a Pixel 6 and a Pixel 5.

Android stacks “security screens”: the SIM PUK prompt can sit on top of the normal fingerprint or PIN screen. When the PUK step succeeded, it asked the stack to dismiss the current screen, without saying which screen it meant.

Meanwhile, another component watching SIM state had already swapped the active screen back to the normal lock screen. So the PUK component’s dismiss call hit the wrong target. Dismissing the real lock screen meant unlocking the phone.

### Business Impact

A lost or stolen Pixel was effectively open to anyone with a SIM tray tool and a SIM they controlled. That covers personal data, authenticator apps, work profiles and anything else a lock screen is meant to protect.

The disclosure path matters too. Triage took 37 minutes, then a month of silence ended with a duplicate verdict, effectively $0 against a $100,000 table maximum. Only after a live demo, a call and an October deadline did Google confirm his report was what triggered the fix, and pay $70,000.

### Fixing Google Pixel-Style Lock Screen Races (my own analysis)

**1. Name the target.** Android’s fix made dismiss take the type of screen the caller wants removed; the PUK flow can now only dismiss a SIM PUK screen.

**2. Treat stale callers as no-ops.** If the top of the stack changed, the late caller does nothing.

**3. Fail closed on unlock.** Reaching an empty stack should still require proof that the owner authenticated.

\# Pseudocode: a screen may only dismiss itself, never "whatever is on top"

class SecurityStack:

def dismiss(self, caller\_mode, caller\_id):

with self.lock:

top = self.stack\[-1\] if self.stack else None

if top is None or top.mode != caller\_mode or top.id != caller\_id:

audit("stale\_dismiss\_ignored", caller\_mode)

return False # late or wrong caller: no-op

self.stack.pop()

if not self.stack: # last screen gone -> unlock?

if not self.owner\_verified\_since\_lock():

self.push(PrimaryAuthScreen()) # fail closed

return False

unlock\_device()

return True

# Test: SIM event swaps the top screen before the PUK flow finishes -> phone stays locked

### Key Takeaways

- “Dismiss the current thing” is an ambiguous command, and race conditions love ambiguity.
- Secondary prompts (SIM, Wi-Fi, accessibility) must never be able to close the primary authentication screen.
- Duplicate handling is part of security: the report that gets a fix shipped deserves a clear owner and timeline.

### Credit & Sources

Discovered and reported by **David Schütz** (xdavidhu). Primary source: [Accidental $70k Google Pixel Lock Screen Bypass](https://bugs.xdavidhu.me/google/2022/11/10/accidental-70k-google-pixel-lock-screen-bypass/), 10 November 2022. Corroboration: [Android Security Bulletin, November 2022](https://source.android.com/docs/security/bulletin/2022-11-01) and the [NVD entry for CVE-2022–20465](https://nvd.nist.gov/vuln/detail/CVE-2022-20465). Facts come from those sources; analysis and code are original.

Next breakdown: an Apple auth bypass that started with one hidden form field. Follow @masimshahzad for daily bug bounty breakdowns.
