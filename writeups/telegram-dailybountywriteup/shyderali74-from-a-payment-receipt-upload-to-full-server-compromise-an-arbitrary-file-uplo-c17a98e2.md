# From a Payment Receipt Upload to Full Server Compromise

- **Source URL:** https://medium.com/@shyderali74/from-a-payment-receipt-upload-to-full-server-compromise-an-arbitrary-file-upload-case-study-5f97a9b52be5
- **Fetched from:** https://medium.com/@shyderali74/from-a-payment-receipt-upload-to-full-server-compromise-an-arbitrary-file-upload-case-study-5f97a9b52be5?source=rss-f72348f8bf81------2
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14916 (id 14916)
- **Method:** medium-rss-feed (full content:encoded) readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- **Author/Published (RSS):** Shyderali / Thu, 17 Sep 2026 14:33:38 GMT

*How a public “upload your receipt” feature became remote code execution and full server takeover, and the controls that would have stopped it.*

**Category:** Web Application Security · **Class:** Arbitrary / Unrestricted File Upload → Remote Code Execution · **Severity:** Critical · **CVSS 3.1:** 9.9 (AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:L/A:H)

***Disclosure note.*** *This write-up is published with the client’s consent. All identifying information (organisation name, branding, domains, hostnames, IP addresses, account data and credentials) has been redacted or replaced with neutral placeholders: the fictional “gzone” auction platform on demo.gzone.com, RFC 5737 example IP ranges, and demo secrets. The vulnerability was reported through our engagement channel and has since been remediated. The intent here is educational: to show how a single feature that accepts a file, a payment receipt, can escalate all the way to full server takeover.*

During a web application penetration test, an online auction platform allowed any authenticated user to upload a “wire-transfer receipt” when topping up their wallet. The upload endpoint accepted **any file type**, stored the file under the **web-served** assets/uploads/ directory, and preserved its original extension.

A minimal **PHP web shell** was uploaded in place of a receipt, its exact stored path recovered from an ordinary API response, and requested in the browser. The server **executed** it. From there it was possible to run arbitrary operating-system commands, map the host, read the application’s .env file (database credentials, mail credentials, payment-gateway keys), and obtain a fully interactive shell. A single, innocuous-looking receipt-upload field yielded **remote code execution** on production infrastructure.

File uploads are among the oldest and most dependable footholds in web application security. The attacker’s first objective is to place their own code on the target; an upload feature does precisely that. The second objective is to have it executed.

An upload turns into code execution when three conditions hold at once, and in practice they frequently do:

When those align, uploading a .php file and then requesting it grants code execution in the security context of the web server. Consequences range from full system takeover and data theft to internal pivoting, persistence, and defacement, depending entirely on what the application does with the file and where it lands.

The platform provided a wallet feature. To add funds, a user could select **Wire Transfer** and then **Upload Receipt**, a field intended for an image or PDF of a bank-transfer confirmation.

That single input, “upload a receipt,” was the entire attack surface required.

Rather than an image, a minimal PHP web shell was submitted to the receipt endpoint. Intercepting the request in Burp Suite, the payload was sent as receipt\_image with the filename testhyder.php, and the server accepted it, responding “Receipt successfully attached.”

The web shell was intentionally minimal: it executes whatever operating-system command is supplied as a request parameter and returns the output.

A web shell is only useful if it can be reached. The storage path did not need to be guessed; the application disclosed it. Loading the wallet triggers a POST /api/get\_transactions request.

For each transaction, the response returns receipt\_image and receipt\_url: the exact server-side path at which the uploaded shell was written.

Requesting that path directly in the browser did not download or reject the file: it was executed by the PHP interpreter, confirming code execution on the server.

With execution confirmed, commands were passed through the shell’s parameter. Listing the upload directory (ls):

Reading the host’s network configuration (ip a):

From arbitrary command execution, access was escalated to a fully interactive reverse shell and the application was enumerated. Reading the framework’s environment file (cat .env) exposed the most sensitive material in cleartext:

At this point the outcome was unambiguous: **complete compromise of the production web server and its data** (database access, mail-system access, and payment-gateway secrets), reachable by any registered user through a receipt-upload button.

The application trusted the uploaded file on three fronts simultaneously:

Any one of these controls, applied correctly, would have broken the chain. All three were absent.

**1. Validate by content, not by name.** Enforce a strict allow-list of accepted types using server-side MIME and magic-byte inspection, and reject everything else. Do not trust the client-supplied extension or Content-Type.

**2. Store uploads outside the web root.** Keep user files where the web server will neither execute nor serve them directly, and return them through a controlled handler that sets a safe Content-Type and Content-Disposition. If they must live under the web root, host them on a separate domain or bucket with execution disabled.

**3. Disable script execution in upload directories.** Configure the web and application server so that no interpreter runs anything under the upload path; for example, remove handler mappings for that directory.

**4. Rename stored files.** Replace the user-supplied filename with a server-generated identifier (random or hashed, plus a timestamp) and a normalised, safe extension, preventing extension smuggling and overwrites.

**5. Do not leak internal storage paths.** API responses should reference uploads via opaque identifiers or signed URLs, never raw server-side file system paths.

**6. Enforce size limits and malware scanning,** and apply least privilege so that a compromised web process cannot read application-wide secrets or reach sensitive back-end systems.

***Remediation status:*** *During reassessment, the client had implemented server-side MIME-type restrictions on the upload endpoint, which block the upload of executable files and resolve this vulnerability.*

If your application accepts files anywhere (receipts, avatars, KYC documents, support attachments), it is worth confirming today that a renamed .php can neither be stored with its extension, nor served, nor executed.

*This case study is part of our ongoing security research and responsible-disclosure practice. Findings are published only after remediation and with the client’s consent, with all identifying details removed.*
