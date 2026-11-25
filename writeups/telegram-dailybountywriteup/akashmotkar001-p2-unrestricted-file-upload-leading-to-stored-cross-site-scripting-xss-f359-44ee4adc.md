# P2 Unrestricted File Upload Leading to Stored Cross-Site Scripting (XSS)

- **Source URL:** https://medium.com/@akashmotkar001/p2-unrestricted-file-upload-leading-to-stored-cross-site-scripting-xss-f3593e691060
- **Fetched from:** https://medium.com/@akashmotkar001/p2-unrestricted-file-upload-leading-to-stored-cross-site-scripting-xss-f3593e691060?source=rss-38c39a01cc6a------2
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:**  (id 14998)
- **Method:** medium-rss-feed (full content:encoded) readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- **Author/Published (RSS):** Akash motkar / Tue, 24 Nov 2026 11:05:14 GMT

**Severity:** P2 — High 

**Vulnerability Type:** Unrestricted File Upload / Stored Cross-Site Scripting

**CWE:**

**OWASP:** A05 — Injection

The application’s file upload functionality may permit users to upload files containing active HTML or JavaScript content without sufficient server-side validation.

If uploaded files are subsequently served from a location where the browser interprets their contents as executable HTML, an attacker may be able to host a malicious payload on the application’s infrastructure.

When another user accesses the uploaded file or a page that renders its contents without proper sanitization, the browser may execute attacker-controlled JavaScript in the context of the application’s origin.

Depending on the application’s origin isolation, cookie protections, and affected functionality, this could expose sensitive information or allow unauthorized actions through the victim’s authenticated session.

The issue becomes particularly serious when uploaded content is automatically rendered or shared with privileged users.

**Component:** File Upload / Attachment Management

**HTTP Method:** POST

**Affected Functionality:** User file uploads and file rendering

**Authentication Required:** Depends on application implementation

**Potential Impact:** Stored XSS and unauthorized actions

Navigate to a feature that accepts user-uploaded files, such as profile attachments, support tickets, document uploads, or chat attachments.

Upload a harmless test file and intercept the request using Burp Suite.

Example:

POST /api/v1/files/upload HTTP/1.1

Host: \<application-host>

Authorization: Bearer \<TEST\_TOKEN>

Content-Type: multipart/form-data; boundary=----TestBoundary

------TestBoundary

Content-Disposition: form-data; name="file"; filename="test.html"

Content-Type: text/html

\<html>

\<body>

\<script>alert(document.domain)\</script>

\</body>

\</html>

------TestBoundary--

Submit the controlled HTML file and inspect whether the application accepts it.

Review the response for the uploaded file identifier or retrieval location.

Acceptance alone does not establish XSS.

Access the uploaded file through the application’s normal download or preview functionality.

Inspect the HTTP response headers, particularly:

Open the uploaded file in a controlled browser session.

Determine whether the browser interprets the uploaded content as executable HTML and whether the harmless JavaScript test executes.

Using a second controlled account, access the uploaded content through the application’s intended sharing or rendering workflow.

Determine whether the payload executes in the second account’s browser and identify the security origin in which it executes.

Do not collect session cookies, access real user data, or perform unauthorized actions.

**Stored Cross-Site Scripting:** Malicious content may execute when users access an uploaded file.

**Authenticated User Interaction:** If execution occurs within the application’s trusted origin, an attacker may be able to perform actions using the victim’s browser session, subject to applicable security controls.

**Sensitive Information Exposure:** Application data accessible to the victim’s browser may be at risk if the payload can access it.

**Privileged User Targeting:** If administrators or support personnel access uploaded content, they may become targets of the stored payload.

**Potential Account Compromise:** Account takeover may become possible only if the demonstrated execution context and available application functionality permit it.

The likely root cause is inadequate validation and isolation of uploaded content.

Potential contributing weaknesses include:

AttributeClassificationVulnerabilityUnrestricted File Upload / Stored XSSSeverityP2 — High (conditional)CWECWE-434, CWE-79OWASPA05 — InjectionAttack VectorNetworkPrivileges RequiredDepends on upload permissionsUser InteractionRequired to access uploaded contentStatusIllustrative — Requires Validation
