# The “Out of Scope” Bugs

- **Source URL:** https://ratnadeepdeyroy.medium.com/the-out-of-scope-bugs-how-to-find-escalate-and-fix-31-commonly-rejected-bug-bounty-findings-91748175e47e
- **Fetched from:** https://ratnadeepdeyroy.medium.com/feed
- **Fetched:** 2026-11-17
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14986 (id 14986)
- **Method:** medium-rss-content readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
*Why your report got closed as “Informative”, and how to turn low-impact findings into valid ones without breaking program rules.*

Most bug bounty programs publish a list of **non-qualifying vulnerabilities**. If you’ve hunted for a while, you’ve probably had something on that list closed as *N/A* or *Informative*. Read the list closely, though. Most entries carry a qualifier: *“without proven impact”*, *“with low impact”*, *“that cannot be used against other users”*.

That qualifier is what matters. The bug class isn’t banned. What gets rejected is the finding **when it’s reported on its own**. If you chain it into account takeover, data exposure or stored XSS, it can become a valid, paid report.

This guide covers 31 of these items. Each one gets six parts:

- **Why it’s excluded**: the program’s reasoning
- **How to test**: detection and verification
- **How to escalate**: what proof makes it reportable
- **Fix**: what the developer should do
- **Detect (blue team)**: what defenders should log and alert on
- **MITRE ATT&CK, CWE and a real-world precedent**

***Ground rules.*** *Only test assets that are in scope and that you’re authorized to test. Use your own test accounts. Never touch other users’ data. Respect the program’s rate limits. If a program says an item is out of scope even with impact, believe it.*

Each section below includes testing steps, escalation, fixes, blue-team detection, ATT&CK/CWE mapping and a real-world precedent. The kill-chain section after the list shows how they combine.

### 1. WordPress Username Disclosure

**Why it’s excluded:** WordPress exposes author slugs by design. Usernames aren’t secrets.

**How to test:** Request /wp-json/wp/v2/users, /?author=1 (it redirects to /author/\<slug>/) and /wp-json/oembed/1.0/embed?url=.... You can also run wpscan --url target --enumerate u.

**How to escalate:** A username list by itself pays nothing. It starts to matter when the REST API leaks more than the slug, such as email addresses, roles or private user meta. It also matters when you combine it with a separate weakness, for example no lockout on wp-login.php together with a default admin account. Report the leaked PII or the auth weakness, not the usernames.

**Fix:** Restrict the /users REST endpoint to authenticated users, block ?author= enumeration and use display names that differ from login names.

**Detect (blue team):** Watch for bursts of ?author=N or /wp-json/wp/v2/users requests from one IP, and failed logins across many usernames.

**MITRE ATT&CK:** T1589.003 Gather Victim Identity Info: Employee Names → T1110.003 Password Spraying

**CWE:** CWE-200, CWE-203

**Real-world:** CVE-2017–5487: the WordPress 4.7 REST API exposed user data to unauthenticated visitors.

### 2. Pre-Auth Account Takeover / OAuth Squatting

**Why it’s excluded:** The attack needs the victim to sign up later with a specific email, so programs see it as speculative.

**How to test:** You need two of your own identities. Register with email/password using an email you control, but don’t verify it. Then sign in with OAuth (Google, Microsoft and so on) using the same email. Check whether the accounts merge and whether the password set before OAuth still works. Also check whether the app lets you change your email to an unverified address that later gets linked through SSO.

**How to escalate:** Show the full chain with your own two accounts: the pre-registered password still logs in after the “victim” identity signs up through OAuth, and you can see that identity’s data. Show it working *without* the victim verifying anything. Programs accept this much more readily when the target provider lets anyone create accounts with arbitrary unverified emails.

**Fix:** Require email verification before an account is usable. Never auto-link an OAuth identity to an unverified local account. On first SSO login, invalidate any pre-existing password and sessions.

**Detect (blue team):** Alert when an OAuth identity links to an account whose email was never verified, and on logins from two different credential types close together.

**MITRE ATT&CK:** T1078 Valid Accounts, T1098 Account Manipulation

**CWE:** CWE-287

**Real-world:** Sudhodanan & Paverd, “Pre-hijacked accounts” (USENIX Security 2022), found this class in dozens of major services.

### 3. Self-XSS

**Why it’s excluded:** Only the attacker’s own browser runs the script.

**How to test:** Look for fields that reflect input only to yourself, such as profile drafts or local search history. Confirm execution with a harmless alert(document.domain).

**How to escalate:** You need a way to deliver it to someone else:

- A **login CSRF** or **session fixation** that logs the victim into your account, where the payload runs on their origin.
- A CSRF that writes the payload into the *victim’s* field.
- The same field rendered elsewhere, such as admin panels, shared workspaces, emails or exports.
- A cache that stores your response and serves it to others.

Report the whole chain.

**Fix:** Context-aware output encoding everywhere, a strict CSP, and CSRF protection on login and on every state-changing request.

**Detect (blue team):** CSP violation reports, script-like strings stored in profile fields, and login CSRF patterns (cross-site POST to /login).

**MITRE ATT&CK:** T1059.007 JavaScript, T1185 Browser Session Hijacking

**CWE:** CWE-79

**Real-world:** The Facebook “paste this in your console” self-XSS scams were common enough that browsers and Facebook added console warnings.

### 4. Verbose Messages, Files and Directory Listings

**Why it’s excluded:** A stack trace or an open /assets/ listing with nothing sensitive in it has no impact.

**How to test:** Send malformed input to trigger errors, use content discovery with ffuf or dirsearch against curated wordlists, and look for .git/, .env, backup.zip and phpinfo.php.

**How to escalate:** Look for something sensitive in what’s exposed: credentials, API keys, internal hostnames you can reach, source code (rebuild .git with git-dumper), database dumps or PII. If you find a key, confirm it's live with a read-only, harmless call, then stop.

**Fix:** Turn off debug mode in production, return generic error pages, disable autoindex and keep secrets out of the web root.

**Detect (blue team):** WAF and access logs for requests to /.git/, /.env, \*.bak, and high 404 rates from one source (content discovery).

**MITRE ATT&CK:** T1592.002 Gather Victim Host Info: Software, T1552.001 Credentials In Files

**CWE:** CWE-209, CWE-548

**Real-world:** Exposed .git directories and .env files regularly leak cloud keys and DB credentials.

### 5. CORS Misconfiguration on Non-Sensitive Endpoints

**Why it’s excluded:** Reading public data from another origin doesn’t hurt anyone.

**How to test:** Send Origin: https://evil.example and check whether the response reflects it in Access-Control-Allow-Origin together with Access-Control-Allow-Credentials: true. Try the variants null, target.com.evil.example and eviltarget.com.

**How to escalate:** Find an endpoint with the same misconfiguration that returns **authenticated, sensitive data**, like profiles, tokens, API keys or messages. Build a proof-of-concept page that fetches it with credentials: 'include' and shows *your own test account's* data being read from an attacker origin.

**Fix:** Use an explicit origin allowlist, never reflect arbitrary origins with credentials, and never trust null.

**Detect (blue team):** Log the Origin header on authenticated API calls and alert on unexpected origins that receive credentialed responses.

**MITRE ATT&CK:** T1185 Browser Session Hijacking, T1530 Data from Cloud Storage (when APIs expose stored data)

**CWE:** CWE-942

**Real-world:** James Kettle, “Exploiting CORS misconfigurations for Bitcoins and bounties” (2016).

### 6. Missing Cookie Flags

**Why it’s excluded:** A missing flag is a hardening gap, not an exploit.

**How to test:** Look at Set-Cookie headers for Secure, HttpOnly and SameSite.

**How to escalate:** The missing flag has to make another bug exploitable. For example, a missing HttpOnly plus a real XSS means the session can be stolen. A missing SameSite plus a state-changing endpoint without a CSRF token means CSRF works. Report the chain.

**Fix:** Set session cookies to Secure; HttpOnly; SameSite=Lax (or Strict), and use the \_\_Host- prefix where you can.

**Detect (blue team):** The same session cookie seen from two IPs or user agents at once; session cookies sent over plain HTTP.

**MITRE ATT&CK:** T1539 Steal Web Session Cookie, T1557 Adversary-in-the-Middle

**CWE:** CWE-614, CWE-1004, CWE-1275

**Real-world:** Firesheep (2010) hijacked sessions on open Wi-Fi because cookies were sent without the Secure flag over HTTP.

### 7. Missing Security Headers

**Why it’s excluded:** Scanner output isn’t a vulnerability.

**How to test:** Check for Content-Security-Policy, Strict-Transport-Security, X-Frame-Options/frame-ancestors, X-Content-Type-Options and Referrer-Policy.

**How to escalate:** Same idea as cookie flags: tie it to an attack that works. Missing nosniff plus an upload that's served inline can mean content-sniffing XSS. Missing framing protection plus a sensitive one-click action is clickjacking (item 13). Missing Referrer-Policy plus tokens in URLs is token leakage (item 16).

**Fix:** Set a baseline header policy at the edge or proxy and roll out CSP in report-only mode first.

**Detect (blue team):** Continuous header scanning in CI and at the edge; use CSP report-to to see what would break or be blocked.

**MITRE ATT&CK:** Enables other techniques (T1189 Drive-by Compromise, T1185)

**CWE:** CWE-693

**Real-world:** Header gaps show up as enabling conditions in most clickjacking and XSS chains.

### 8. CSRF with No or Low Impact

**Why it’s excluded:** CSRF on logout, theme changes or newsletter toggles doesn’t matter much.

**How to test:** For state-changing requests, remove or alter the CSRF token, switch POST to GET, change the content type to text/plain or a form encoding, and check whether the SameSite cookie setting lets the request through.

**How to escalate:** Target actions that matter: changing email, password or phone number, adding an OAuth app or API key, transferring funds, changing permissions, disabling 2FA. A CSRF on email change usually leads to full account takeover through password reset. Include an auto-submitting HTML PoC and show it working against your own victim account.

**Fix:** Synchronizer or double-submit tokens, SameSite cookies, and re-authentication for sensitive actions.

**Detect (blue team):** Sensitive actions where the Origin/Referer doesn't match your domain; email changes followed quickly by a password reset.

**MITRE ATT&CK:** T1098 Account Manipulation → T1078 Valid Accounts

**CWE:** CWE-352

**Real-world:** Zeller & Felten (Princeton, 2008) showed CSRF in ING Direct that could open accounts and move money.

### 9. Autocomplete Attribute on Forms

**Why it’s excluded:** Modern browsers ignore autocomplete="off" on password fields, and the risk needs physical access to the device.

**How to test:** Inspect sensitive forms (card number, CVV, OTP) for missing autocomplete="off" or one-time-code.

**How to escalate:** There’s almost never a path to accepted impact. Leave it out or put it in a pentest report’s informational section.

**Fix:** Use the correct autocomplete tokens, such as cc-number and one-time-code, and never store sensitive values in the client.

**Detect (blue team):** Not really detectable server-side. Check it in code review.

**MITRE ATT&CK:** T1555.003 Credentials from Web Browsers (needs device access)

**CWE:** CWE-525

**Real-world:** No meaningful real-world exploitation on its own.

### 10. Reverse Tabnabbing

**Why it’s excluded:** Modern browsers treat target="\_blank" as noopener by default.

**How to test:** Look for window.open() calls without noopener, or links where users control the destination and that explicitly set rel="opener".

**How to escalate:** It’s only meaningful when the attacker controls the opened page (user-submitted links) and the opener reference survives in current browsers. Show that the original tab is navigated to a look-alike URL. Even then, many programs pay little or nothing.

**Fix:** Add rel="noopener noreferrer" and pass noopener to window.open.

**Detect (blue team):** Find window.open calls without noopener in static analysis (ESLint react/jsx-no-target-blank).

**MITRE ATT&CK:** T1566.002 Spearphishing Link, T1656 Impersonation

**CWE:** CWE-1022

**Real-world:** Mathias Bynens popularised the issue in 2016. Chrome 88 (2021) made noopener the default for target=\_blank.

### 11. Bypassing or Missing Rate Limits

**Why it’s excluded:** Unlimited requests to most endpoints aren’t harmful.

**How to test:** Send a small, controlled burst (for example 20 to 50 requests) to auth-related endpoints. Try common bypasses: X-Forwarded-For rotation, changing letter case or adding trailing slashes to the path, adding parameters, and using the API version instead of the web endpoint.

**How to escalate:** Impact depends on **the endpoint**. Missing rate limits on **OTP or 2FA verification**, **password reset codes** or **login** can make brute force feasible. Do the math in your report instead of brute-forcing: “a 6-digit OTP has 1,000,000 possibilities, the code is valid for 10 minutes, and I observed N requests/second with no lockout, so the expected time to success is X.” Show the lack of throttling with a few dozen requests against *your own* account and stop there.

**Fix:** Limit per account and per IP, lock out progressively, expire codes after a few attempts, and add CAPTCHA after repeated failures.

**Detect (blue team):** Failed OTP or login counts per account and per IP, rotating X-Forwarded-For values, and many attempts on one account from many IPs.

**MITRE ATT&CK:** T1110.001 Password Guessing, T1110.004 Credential Stuffing

**CWE:** CWE-307, CWE-799

**Real-world:** Laxman Muthiyah (2019) showed Instagram’s password-reset OTP could be brute-forced by spreading requests across IPs. Meta paid $30,000.

### 12. Best-Practice Violations (Password Policy, Expiry, Re-use)

**Why it’s excluded:** These are policy choices. NIST 800–63B actually advises *against* forced expiry.

**How to test:** Check minimum length, whether breached passwords are rejected, and whether changing a password requires the current one.

**How to escalate:** Weak policy on its own is rarely paid. What’s reportable is a *logic* flaw, such as changing a password without the current password while it’s also vulnerable to CSRF or XSS, or a reset that doesn’t invalidate the old password.

**Fix:** Follow NIST guidance: at least 8 characters (12 or more is better), screen against breached-password lists, no arbitrary composition rules, and support MFA.

**Detect (blue team):** Logins that match known-breached passwords (HIBP k-anonymity API) and spikes of successful logins from new ASNs.

**MITRE ATT&CK:** T1110.004 Credential Stuffing, T1078 Valid Accounts

**CWE:** CWE-521, CWE-620

**Real-world:** Credential stuffing based on password reuse is behind many large account-takeover waves.

### 13. Clickjacking Without Proven Impact

**Why it’s excluded:** Framing a page where clicks do nothing sensitive, or where the attack needs implausible user interaction, has no impact.

**How to test:** Check for missing X-Frame-Options or CSP frame-ancestors, then try to load the page in an iframe on a local HTML file.

**How to escalate:** Find a page where **one or two clicks** do something sensitive, like deleting an account, granting OAuth consent, changing privacy settings, transferring funds or approving a connection. Build a PoC that overlays a believable decoy (“Click to claim reward”) and record a video of it working against your own test account.

**Fix:** Content-Security-Policy: frame-ancestors 'self' plus confirmation steps for destructive actions.

**Detect (blue team):** CSP frame-ancestors violation reports, and Referer values from unknown framing sites on sensitive actions.

**MITRE ATT&CK:** T1189 Drive-by Compromise, T1204 User Execution

**CWE:** CWE-1021

**Real-world:** Hansen & Grossman (2008) used clickjacking against the Adobe Flash settings page to turn on webcams and microphones. Later came Facebook “likejacking”.

### 14. CSV Injection

**Why it’s excluded:** The payload runs in the victim’s spreadsheet application, which warns them, so programs consider it a client-side problem.

**How to test:** Put a value starting with =, +, - or @ (for example =1+1) into a field that ends up in a CSV export. Export the file and check whether the formula is calculated.

**How to escalate:** Show that data you control ends up in exports opened by *other privileged users*, such as admin user exports or financial reports, and that the formula can leak data from other cells (for example through HYPERLINK to a URL you control) without extra warnings in the target spreadsheet app. Many programs still exclude it, so check the policy first.

**Fix:** Prefix cells starting with = + - @, tab or carriage return with a single quote, and quote all fields.

**Detect (blue team):** Stored values starting with = + - @ in fields that get exported.

**MITRE ATT&CK:** T1204.002 User Execution: Malicious File

**CWE:** CWE-1236

**Real-world:** George Mauer, “The Absurdly Underestimated Dangers of CSV Injection” (2014).

### 15. Sessions Not Invalidated (Logout, Password Change, 2FA Enable)

**Why it’s excluded:** It needs an attacker who already has a session.

**How to test:** Log in from two browsers. In browser A, log out, change the password or turn on 2FA. Then check whether browser B’s session, and any captured JWT or refresh token, still works.

**How to escalate:** Combine it with a realistic way to steal a session, such as token leakage (item 16), XSS or a shared device. Show that after the victim “secures” the account, the attacker’s access survives. Long-lived tokens that can’t be revoked, such as API keys or refresh tokens, make a stronger case.

**Fix:** Revoke sessions server-side, offer “log out of all devices”, and rotate tokens on security events.

**Detect (blue team):** Requests using a session that should have been revoked after logout or a password change; tokens used after a 2FA enrolment event.

**MITRE ATT&CK:** T1550.004 Use Alternate Auth Material: Web Session Cookie

**CWE:** CWE-613

**Real-world:** Long-lived sessions and refresh tokens let attackers keep access after a victim “secures” the account. This is common in infostealer-driven ATO.

### 16. Tokens Leaked to Third Parties

**Why it’s excluded:** The third party is usually trusted, like analytics, or the token has no value.

**How to test:** Look for tokens in URLs (password reset links, magic links, OAuth code/access\_token) on pages that load third-party scripts or images, then check the Referer sent to those domains in the browser's DevTools Network tab.

**How to escalate:** Prove the leaked token is **sensitive and still valid**. For example, a password reset token sent to an analytics domain that can still be used afterwards, or an OAuth code leaked to a domain that third parties or users can control. Show the token in the outgoing request and that it gives access to your own test account.

**Fix:** Referrer-Policy: no-referrer on sensitive pages, keep tokens out of URLs (use POST or fragments), and make tokens single-use and short-lived.

**Detect (blue team):** Audit outbound Referers in a headless crawl of token-bearing pages. Alert when the same reset token is used more than once.

**MITRE ATT&CK:** T1528 Steal Application Access Token, T1550.001 Application Access Token

**CWE:** CWE-598, CWE-200

**Real-world:** OAuth “code” and reset-token Referer leaks to analytics and CDN domains come up again and again in public bounty write-ups.

### 17. Email Spoofing, SPF, DMARC, DKIM

**Why it’s excluded:** Almost every program excludes it outright. It’s a domain configuration issue that deliverability filters largely mitigate.

**How to test:** dig TXT target.com and dig TXT \_dmarc.target.com, or use MXToolbox. Check for p=none, a missing DMARC record or \~all instead of -all.

**How to escalate:** In most programs there’s no path. Don’t send spoofed mail to real people. The exception is spoofing *inside the app’s own features* (see item 20) or an unauthenticated mail relay the company runs, which is a different bug class.

**Fix:** SPF with -all, DKIM signing, and DMARC moving toward p=reject.

**Detect (blue team):** DMARC aggregate (rua) reports show who sends mail as your domain.

**MITRE ATT&CK:** T1566 Phishing, T1656 Impersonation

**CWE:** CWE-290

**Real-world:** Business email compromise relies heavily on spoofed or look-alike sender domains. The FBI IC3 ranks it among the costliest cybercrimes.

### 18. Content Injection Without HTML Modification

**Why it’s excluded:** Text reflected into a page, like “Error: \<your text>”, is a minor phishing concern.

**How to test:** Find parameters that are reflected as plain text in error pages or 404 messages.

**How to escalate:** Look for **HTML injection** instead. If tags render, you may get to XSS, dangling-markup data exfiltration or credential-harvesting forms on the trusted origin. If it really is only text, it’ll be closed. Check whether the text is injected into *emails* the platform sends, which is more convincing.

**Fix:** Don’t reflect user input in error messages, and encode output.

**Detect (blue team):** Reflected parameters with URLs or phone numbers in error pages; user-controlled text in outgoing emails.

**MITRE ATT&CK:** T1566.002 Spearphishing Link, T1656 Impersonation

**CWE:** CWE-74

**Real-world:** Text injected into trusted-domain pages or emails is a common way to place scam phone numbers and links.

### 19. Username / Email Enumeration

**Why it’s excluded:** Most sign-up forms have to reveal “email already in use”, so it’s often unavoidable.

**How to test:** Compare responses, status codes and timing for existing and non-existing accounts on login, password reset and registration.

**How to escalate:** It matters on sensitive platforms (health, dating, whistleblowing) where *membership itself* is private, or when the endpoint returns PII beyond true/false, like full name, phone number or profile ID. It also helps when combined with no rate limiting at scale. Make your case around privacy impact.

**Fix:** Use generic messages (“If an account exists, we’ve sent an email”), keep response times consistent and rate-limit.

**Detect (blue team):** High volumes of distinct usernames checked from one client against reset, signup or contact-import endpoints.

**MITRE ATT&CK:** T1589.002 Gather Victim Identity Info: Email Addresses

**CWE:** CWE-203, CWE-204

**Real-world:** Facebook’s data on 533M users (2021) was scraped through abuse of the contact-importer feature (according to Facebook), a phone-number enumeration at scale.

### 20. Email Bombing

**Why it’s excluded:** Sending many emails to one address is a nuisance with no confidentiality or integrity impact.

**How to test:** Use **only your own email address** and a small count, say 5 to 10 triggers, on features like “resend verification”, “invite” or “share”.

**How to escalate:** The better finding is usually a **content injection into emails**: you control the text, links or display name in an email the company sends to *arbitrary recipients* from its trusted domain. That’s a realistic phishing vector. Show one email to your own second inbox. Don’t send to third parties.

**Fix:** Rate-limit email-sending features per user and recipient, strip or validate user-controlled content in templates and require verification before sending invites.

**Detect (blue team):** Per-recipient send volume and repeated triggers of invite or resend endpoints.

**MITRE ATT&CK:** T1667 Email Bombing (added in ATT&CK v17), often followed by T1656 Impersonation

**CWE:** CWE-770

**Real-world:** In 2024 Black Basta affiliates flooded victims’ inboxes, then called them on Microsoft Teams posing as IT help desk (reported by Rapid7 and Microsoft).

### 21. HTTP Request Smuggling Without Proven Impact

**Why it’s excluded:** Timing-based detection alone doesn’t show exploitability, and testing can affect other users.

**How to test:** Use Burp Suite’s *HTTP Request Smuggler* extension or PortSwigger’s methodology to detect CL.TE, TE.CL or H2 desync behavior. Do it carefully, with low request volume, and preferably during low traffic.

**How to escalate:** Programs want a *non-destructive* confirmation that affects only you. For example, smuggle a request prefix that makes **your own next request** return a different response, or show you can bypass a front-end access control on your own requests. Never try to capture other users’ requests or poison shared caches in production. Many programs ask you to stop and contact them once you’ve confirmed a desync.

**Fix:** Normalize ambiguous requests at the front end, reject requests with both Content-Length and Transfer-Encoding, use HTTP/2 end to end, and keep proxies patched.

**Detect (blue team):** Requests with both Content-Length and Transfer-Encoding, malformed chunked bodies, and front-end/back-end response mismatches.

**MITRE ATT&CK:** T1190 Exploit Public-Facing Application

**CWE:** CWE-444

**Real-world:** James Kettle, “HTTP Desync Attacks” (2019), including a desync on PayPal’s login.

### 22. Homograph (IDN) Attacks

**Why it’s excluded:** Browsers display punycode for mixed-script domains, and registering look-alike domains isn’t the target’s vulnerability.

**How to test:** Check whether the app accepts Unicode look-alikes in *usernames, display names or email addresses*, for example a Cyrillic “а” instead of Latin “a”.

**How to escalate:** Show an **in-app** impact: impersonating an admin or verified account because names aren’t normalized, or Unicode case-folding collisions in password reset where the email normalizes to someone else’s address. Test the reset only with two of your own addresses.

**Fix:** Normalize identifiers with NFKC, use confusable detection (Unicode TR39) and compare canonical forms.

**Detect (blue team):** Mixed-script or confusable usernames at registration (Unicode TR39 skeleton matching), and new look-alike domain registrations (certificate transparency monitoring).

**MITRE ATT&CK:** T1583.001 Acquire Infrastructure: Domains, T1036 Masquerading

**CWE:** CWE-1007

**Real-world:** Xudong Zheng (2017) registered a punycode domain that displayed as “apple.com” in Chrome and Firefox.

### 23. XML-RPC Enabled

**Why it’s excluded:** xmlrpc.php is on by default in WordPress.

**How to test:** POST a system.listMethods call to /xmlrpc.php.

**How to escalate:** Show a real weakness: system.multicall getting around login rate limiting (prove it by sending many credential attempts in *one* request against your own account, then stop), or pingback.ping reaching *internal* hosts (that's SSRF; see item 29).

**Fix:** Disable XML-RPC if it isn’t used, or block system.multicall and pingback.ping.

**Detect (blue team):** POSTs to /xmlrpc.php with system.multicall or pingback.ping.

**MITRE ATT&CK:** T1110.001 Password Guessing, T1190

**CWE:** CWE-307, CWE-918

**Real-world:** Sucuri (2015) documented brute-force campaigns that used system.multicall to test hundreds of passwords in one request.

### 24. Banner Grabbing / Version Disclosure

**Why it’s excluded:** A version string isn’t exploitable on its own.

**How to test:** Look at the Server, X-Powered-By and X-AspNet-Version headers, generator meta tags, and readme.html / CHANGELOG files.

**How to escalate:** Map the version to a **known CVE** and confirm the vulnerable code path is present and reachable, ideally with a safe, non-destructive check like a version-specific file or behavior. Report the CVE, not the banner.

**Fix:** Patch first. Suppressing banners only reduces noise.

**Detect (blue team):** An asset inventory plus SBOM-to-CVE matching. Banner suppression doesn’t stop fingerprinting.

**MITRE ATT&CK:** T1592.002 Gather Victim Host Info: Software → T1190

**CWE:** CWE-497, CWE-200

**Real-world:** Equifax (2017) was breached through Apache Struts CVE-2017–5638, which was easy to find by version.

### 25. Metadata Not Stripped from Files

**Why it’s excluded:** EXIF in a user’s own upload is the user’s own data.

**How to test:** Upload a photo containing GPS EXIF data, download it as another user or logged out, and run exiftool on it.

**How to escalate:** Show that **other users’ private data** is exposed. For example, profile photos or marketplace listings keep GPS coordinates that reveal home addresses, on a platform where location privacy matters. Use your own uploaded image as the evidence.

**Fix:** Strip metadata server-side on upload, for instance by re-encoding the image.

**Detect (blue team):** Scan served images for leftover EXIF GPS tags in CI or with a periodic job.

**MITRE ATT&CK:** T1593 Search Open Websites/Domains, T1589 Gather Victim Identity Info

**CWE:** CWE-212

**Real-world:** In 2012 an EXIF GPS tag in a Vice photo revealed John McAfee’s location in Guatemala.

### 26. Same-Site Scripting

**Why it’s excluded:** This is the old localhost.target.com → 127.0.0.1 DNS issue. It needs an attacker on the victim's own machine.

**How to test:** dig localhost.target.com.

**How to escalate:** There’s almost never a path. Leave it out.

**Fix:** Remove localhost records from public DNS zones.

**Detect (blue team):** Lint DNS zones for localhost / 127.0.0.1 records.

**MITRE ATT&CK:** T1185 Browser Session Hijacking (needs a local foothold)

**CWE:** No dedicated CWE

**Real-world:** Tavis Ormandy described the issue on Bugtraq in 2008.

### 27. Subdomain Takeover Without Taking Over the Subdomain

**Why it’s excluded:** A dangling CNAME isn’t proof that someone can claim it.

**How to test:** Enumerate subdomains with subfinder or amass, check for CNAMEs pointing to deprovisioned services, and compare the response fingerprints against the *can-i-take-over-xyz* project.

**How to escalate:** Actually **claim** the resource, such as the S3 bucket, GitHub Pages site or Heroku app, and serve a harmless proof file at an unguessable path (for example /poc-\<random>.html containing your handle). Don't put anything visible at the root. Explain the impact: cookies scoped to the parent domain, CORS or CSP trust of \*.target.com, or OAuth redirect allowlists. Release the resource when the program asks.

**Fix:** Remove DNS records before deprovisioning and monitor for dangling CNAMEs.

**Detect (blue team):** Continuously check CNAMEs against cloud resources you still own. Tools: dnsReaper, subjack, nuclei takeover templates.

**MITRE ATT&CK:** T1584.001 Compromise Infrastructure: Domains, T1539

**CWE:** CWE-284 (no dedicated CWE)

**Real-world:** EdOverflow’s “can-i-take-over-xyz” collects fingerprints for dozens of services, and takeovers on big-tech subdomains are reported regularly.

### 28. Arbitrary File Upload Without Proof the File Exists

**Why it’s excluded:** If you can’t reach or run the file, nothing has happened.

**How to test:** Try bypassing extension and content-type checks (double extensions, .pHp, a changed Content-Type, polyglots) and look for where the file is stored.

**How to escalate:** Find the storage URL, through the response, predictable naming or CDN paths, and show that the file is **served from a trusted origin**. A harmless HTML or SVG file that runs alert(document.domain) proves stored XSS. For server-side execution, a benign file that prints a unique string proves it. Never upload web shells. Delete your files afterwards.

**Fix:** Allowlist extensions and verify magic bytes, rename files, store them outside the web root or on a separate sandbox domain, and serve them with Content-Disposition: attachment and nosniff.

**Detect (blue team):** New executable or HTML files in upload directories, uploads where the MIME type doesn’t match the magic bytes, and requests to recently uploaded paths.

**MITRE ATT&CK:** T1505.003 Server Software Component: Web Shell, T1190

**CWE:** CWE-434

**Real-world:** CVE-2018–9206: blueimp jQuery-File-Upload allowed unauthenticated arbitrary uploads and was exploited in the wild.

### 29. Blind SSRF Without Proven Business Impact

**Why it’s excluded:** A DNS or HTTP pingback to your server shows only that the server makes outbound requests, which is often intended (webhooks, URL previews).

**How to test:** Supply Burp Collaborator or interactsh URLs in URL parameters, webhooks, image fetchers, PDF generators and XML inputs.

**How to escalate:** Show you can reach **internal** resources. Response time or status differences between internal ports can show internal port scanning. Show access to cloud metadata (169.254.169.254; stop at confirming it's reachable, and don't use any credentials you see). Show you can reach internal-only services or bypass allowlists through redirects. A *non-blind* response reflection is much stronger.

**Fix:** Enforce an egress allowlist, block private and link-local ranges after DNS resolution, require IMDSv2 and don’t follow redirects.

**Detect (blue team):** Egress logs showing app servers connecting to private ranges or 169.254.169.254; enable IMDSv2 hop-limit alerts.

**MITRE ATT&CK:** T1552.005 Cloud Instance Metadata API, T1046 Network Service Discovery

**CWE:** CWE-918

**Real-world:** Capital One (2019): SSRF against a misconfigured WAF reached AWS instance metadata and exposed about 100M customer records.

### 30. Disclosed or Misconfigured Google Maps API Keys

**Why it’s excluded:** Maps keys are meant to be public in client-side code.

**How to test:** Find AIza... keys in JavaScript and use the *KeyHacks* methodology to check which APIs they're enabled for.

**How to escalate:** Show that the key is **unrestricted** (no HTTP referrer or app restriction) and enabled for **billable or sensitive APIs** beyond Maps JS. Make one or two calls only, never a cost-generating volume. Most programs still exclude this, so check the policy.

**Fix:** Restrict keys by referrer, app or IP and by API, and set quotas and billing alerts.

**Detect (blue team):** Usage spikes and unexpected APIs in the Google Cloud console; billing alerts.

**MITRE ATT&CK:** T1496 Resource Hijacking (billing abuse)

**CWE:** CWE-284

**Real-world:** The open-source KeyHacks project lists how to check which APIs a leaked key works against.

### 31. Host Header Injection Without Proven Business Impact

**Why it’s excluded:** A reflected Host header in your own response affects only you.

**How to test:** Change Host, or add X-Forwarded-Host / X-Host, and see whether the value appears in links, redirects or emails.

**How to escalate:** The classic escalation is **password reset poisoning**. Request a reset for *your own second account* with a modified Host. If the emailed reset link points to your domain, the token would leak to an attacker when the victim clicks it. Show the email and the token arriving at your server. Other impacts are web cache poisoning (test only with a cache-buster parameter so other users aren't affected) and routing-based SSRF.

**Fix:** Build absolute URLs from a configured canonical hostname, never from request headers, and validate Host against an allowlist.

**Detect (blue team):** Reset requests whose Host or X-Forwarded-Host doesn't match the canonical domain; reset links clicked from unexpected domains.

**MITRE ATT&CK:** T1528 Steal Application Access Token → T1078

**CWE:** CWE-640, CWE-20

**Real-world:** James Kettle, “Practical HTTP Host header attacks” (2013) and “Practical Web Cache Poisoning” (2018).

### Chaining Low-Severity Bugs: Five Kill Chains Mapped to MITRE ATT&CK

Here is how the “boring” findings above combine into real incidents. Each chain lists the ATT&CK tactic, the technique and the bug it relies on.

### Chain A: Enumeration → No Rate Limit → Account Takeover

1. **Reconnaissance**: T1589.002. Email enumeration on the reset endpoint (#19) confirms which accounts exist.
2. **Credential Access**: T1110.001. No rate limit on the 6-digit reset OTP (#11), bypassed through IP rotation.
3. **Initial Access / Persistence**: T1078 Valid Accounts. The attacker sets a new password. Sessions not invalidated (#15) keep the attacker’s foothold even after the victim resets it again.

*Precedent:* the 2019 Instagram reset-OTP brute force.

### Chain B: Missing SameSite + Low-Impact CSRF + Self-XSS → Stored XSS → Session Theft

1. **Initial Access**: T1189. The victim visits an attacker page.
2. **Execution**: T1059.007. CSRF (#8), possible because of missing SameSite (#6), writes the self-XSS payload (#3) into the victim's own profile.
3. **Credential Access**: T1539. The cookie is missing HttpOnly (#6), so the session cookie can be read.
4. **Lateral Movement / Defense Evasion**: T1550.004. The attacker replays the session.

### Chain C: Dangling CNAME → Subdomain Takeover → Cookie/OAuth Theft

1. **Resource Development**: T1584.001. Claim the abandoned cloud resource (#27).
2. **Credential Access**: T1539 / T1528. Parent-domain cookies are sent to the subdomain, or the subdomain is on the OAuth redirect\_uri allowlist, leaking tokens (#16).
3. **Collection**: CORS trusting \*.target.com (#5) lets the attacker read authenticated APIs.

### Chain D: Host Header Injection → Reset Poisoning → ATO

1. **Credential Access**: T1528. The reset link is built from X-Forwarded-Host (#31).
2. **Collection**: the victim clicks the link, and the token goes to the attacker domain, the same issue as #16.
3. **Initial Access**: T1078. The attacker resets the password.

### Chain E: Blind SSRF → Cloud Metadata → Data Theft

1. **Initial Access**: T1190. A webhook or image fetcher with blind SSRF (#29, or XML-RPC pingback #23).
2. **Discovery**: T1046. Internal port and service mapping through timing.
3. **Credential Access**: T1552.005. Instance metadata credentials (IMDSv1).
4. **Exfiltration**: T1530. Data read from cloud storage. This is the Capital One 2019 pattern.

### Bonus: Email Bombing → Help-Desk Vishing (Real Ransomware TTP)

T1667 Email Bombing floods the inbox (#20). Then T1656 Impersonation: a fake “IT support” call on Teams talks the user into installing remote-access tooling. This was seen in 2024 Black Basta intrusions. Missing per-recipient rate limits on *your* app’s email features can make your domain part of someone else’s attack.

### A Reporting Checklist That Gets These Accepted

1. **Read the policy first.** If the program says “out of scope even with impact”, don’t report it.
2. **Lead with impact, not the bug class.** Write “Account takeover via CSRF on email change”, not “Missing CSRF token”.
3. **Give a complete, reproducible chain** using only your own accounts, with request/response pairs and a short video.
4. **Quantify where you can:** brute-force time, number of affected users, data fields exposed.
5. **Stay non-destructive:** minimal requests, no real users’ data, clean up anything you uploaded or claimed.
6. **Suggest a fix.** It speeds up triage and builds trust with the team.

### Final Thoughts

An out-of-scope list tells you what the program won’t pay for *on its own*. Each item on it can be a building block. Whether it gets paid depends on whether you can connect it to an impact the business cares about. Find the weakness, then work out what an attacker could actually do with it.

*Happy (and authorized) hunting.*
