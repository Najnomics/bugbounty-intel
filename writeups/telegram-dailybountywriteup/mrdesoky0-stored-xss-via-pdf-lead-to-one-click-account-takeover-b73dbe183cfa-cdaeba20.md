# Stored XSS via PDF lead to One-Click Account Takeover

- **Source URL:** https://medium.com/@mrdesoky0/stored-xss-via-pdf-lead-to-one-click-account-takeover-b73dbe183cfa?source=rss------bug_bounty-5
- **Fetched from:** https://medium.com/feed/@mrdesoky0
- **Fetched:** 2026-11-27
- **Channel:** @dailybountywriteup
- **Telegram message:**  (id 10984)
- **Method:** medium-rss-content readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
Hello — I’m Desoky (mrdesoky0). I’ve been a bug hunter for about a month, and I used to be an Android developer for \~2.5 years.

I’ll explain how I found a **Stored XSS via PDF upload** and turned it into a **one-click account takeover** — meaning I could take the victim’s account with a single click.

The bug was in a team/board app owned by a large company (I can’t name them). They have approximately **25,000 employees** and **130,000,000 users**, and they run a private bug bounty program outside public platforms.

The app is a board where teams share ideas, images and files. Teams have multiple roles and different permissions. I started by looking for access-control issues but didn’t find anything useful, so I focused on file uploads.

I tried uploading images with XSS payloads but the image upload point was protected. Then I found a separate endpoint that accepts **PDF** uploads, so I tried embedding an XSS payload inside a PDF.

The script I used is in my repo here:

[https://github.com/mrdesoky0/vulnerabilities/blob/main/xss/generate\_pdf\_xss.py](https://github.com/mrdesoky0/vulnerabilities/blob/main/xss/generate_pdf_xss.py)

Run it like this and put your payload inside the quotes:

python generate\_pdf\_xss.py "alert(document.cookie)"

That generates a PDF containing XSS. I made a PDF that triggers alert(document.cookie) and uploaded it — the app didn’t filter it and the PDF was accepted. When any team member opened the PDF inside the app viewer they saw the alert with their cookie, so I confirmed the XSS was working.

PDF.js (used by Firefox and many web integrations). It allows arbitrary JavaScript execution, not just alerts, because it exploits a vulnerability in the font rendering path. You can check more details about this specific vector here:

[https://codeanlabs.com/2024/05/cve-2024-4367-arbitrary-js-execution-in-pdf-js/](https://codeanlabs.com/2024/05/cve-2024-4367-arbitrary-js-execution-in-pdf-js/)

Next I made another PDF with a payload that exfiltrates the cookie to my external test server (I used interactsh). I uploaded it and when another user opened the PDF I received their cookie on my server.

**Step to reproduce**

1. Generate a PDF with an XSS payload (example above).
2. Upload the generated PDF to the app’s PDF upload endpoint.
3. Open the uploaded PDF inside the app viewer as another authenticated user.
4. Use an payload to send the cookie to an external server (e.g., interactsh) and confirm receipt.
5. Use the stolen session (cookie) to access authenticated-only endpoints.
6. Find an endpoint that allows changing the user email while a valid session is present and change the email to one you control.
7. Change the password using the session (or account recovery relying on the updated email) and log in with the new credentials — account takeover.

One more thing — I’ll upload a simple PoC image showing the PDF opened inside the app and the alert(document.cookie) as proof.

Since this is session hijacking, I turned it into a one-click ATO simply: I confirmed the session worked, used the stolen cookie to change the victim’s email to mine, then changed the password and logged in.

The vulnerability was accepted as **high** and has been fixed. **Alhamdulillah.**

That’s it — hope someone learns from this and finds similar issues. Good luck to everyone.
