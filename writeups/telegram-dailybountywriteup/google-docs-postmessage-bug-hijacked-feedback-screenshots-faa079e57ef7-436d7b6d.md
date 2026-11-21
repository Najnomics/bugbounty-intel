# Google Docs postMessage Bug

- **Source URL:** https://masimshahzad.medium.com/google-docs-postmessage-bug-hijacked-feedback-screenshots-faa079e57ef7
- **Fetched from:** https://masimshahzad.medium.com/feed
- **Fetched:** 2026-11-21
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14994 (id 14994)
- **Method:** medium-rss-content readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
### How one wildcard target origin in Google’s shared Send Feedback widget let an outside page capture screenshots of private documents

*AI-assisted: drafted with AI help from public sources, then reviewed and edited. This is an analytical case study of a public disclosure, not my own discovery.*

A single asterisk decided who received a screenshot of your private document. In 2020, Sreeram KL showed a [Google Docs postMessage bug](https://blog.geekycat.in/posts/hijacking-google-docs-screenshots/) where the Send Feedback feature could hand a document screenshot to an attacker’s page instead of Google. It was reported to Google’s Vulnerability Reward Program and, per press coverage, earned $3,133.70.

***Disclaimer:*** *Educational and defensive use only. This was fixed in 2020. Reproduction details are intentionally omitted.*

### Vulnerability Overview

- **Type:** Cross-origin data leak through postMessage with a wildcard target origin, combined with a navigable cross-origin iframe
- **CWE (analytical mapping, not from the source):** CWE-345 (Insufficient Verification of Data Authenticity), CWE-1021 (Improper Restriction of Rendered UI Layers)
- **CVE:** Not reported
- **Severity/CVSS:** Not reported. Bounty: $3,133.70, as reported by The Hacker News, not stated on the researcher’s post

### How the Google Docs postMessage Bug Worked (high level)

Google’s Send Feedback widget lives on [www.google.com](http://www.google.com) and is embedded into products like Docs through iframes. When you open it, Docs passes the page’s pixels across origins with postMessage, a sandboxed Google domain renders them into an image, and on Send the screenshot and description travel back to the feedback frame.

Most of those messages named their exact destination, so redirecting a frame elsewhere got nothing. The final submit message did not: its target origin was the wildcard, meaning “deliver to whoever is in this window now.”

The second ingredient was a browser rule: a page that embeds a document can change the location of frames nested inside it if the embedded page allows framing. Docs did. So a malicious page could embed a document, wait for the victim to open Send Feedback, swap the feedback frame for its own page, and receive the screenshot when the victim clicked Send.

### Impact

Feedback screenshots capture whatever is on screen: contracts, financials, internal plans. The attack needed the victim to visit a hostile page and use Send Feedback, so it was not silent, but the user had no visible sign that the data went anywhere other than Google.

### Fixing Google Docs-Style postMessage Leaks (my own analysis)

**1. Never send sensitive data with a wildcard target.** Name the exact origin, every time.

**2. Verify on receipt.** Receivers must check event.origin and event.source before trusting a message.

**3. Limit who can frame you.** A frame-ancestors policy stops hostile pages from wrapping your app and steering nested frames.

**4. Audit shared widgets centrally.** One component embedded across many products multiplies one mistake.

// Pseudocode: sending and receiving feedback data safely

const FEEDBACK\_ORIGIN = "https://feedback.example.com";

function submitFeedback(frame, payload) {

frame.contentWindow.postMessage(payload, FEEDBACK\_ORIGIN); // never "\*"

}

window.addEventListener("message", (event) => {

if (event.origin !== FEEDBACK\_ORIGIN) return; // drop strangers

if (event.source !== feedbackFrame.contentWindow) return; // right window too

handleFeedbackReply(event.data);

});

// Server header for the host app:

// Content-Security-Policy: frame-ancestors 'self'

### Key Takeaways

- postMessage with “\*” is a broadcast, not a delivery.
- Frames you embed can be swapped by whoever embeds you.
- Defence takes both ends: exact target origins when sending, origin checks when receiving.

### Credit & Sources

Research by **Sreeram KL**: [Hijacking Google Docs Screenshots](https://blog.geekycat.in/posts/hijacking-google-docs-screenshots/) (Geekycat Blog, December 2020); bounty figure from [The Hacker News](https://thehackernews.com/2020/12/a-google-docs-bug-could-have-allowed.html). Facts come from those sources; analysis and code are original.

Next breakdown: another real bug bounty case. Follow @masimshahzad for daily bug bounty breakdowns.
