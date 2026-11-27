# Stored XSS via SVG File Upload in a Project Management Application

- **Source URL:** https://medium.com/@am011416854/stored-xss-via-svg-file-upload-in-a-project-management-application-038c0944c3f7?source=rss------bug_bounty-5
- **Fetched from:** https://medium.com/feed/@am011416854
- **Fetched:** 2026-11-27
- **Channel:** @dailybountywriteup
- **Telegram message:**  (id 14402)
- **Method:** medium-rss-content readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
**Bug Bounty Write-up | Stored XSS | File Upload Security**

### Introduction

During one of my bug bounty hunting sessions, I came across a **Stored Cross-Site Scripting (XSS)** vulnerability in a project management web application. The vulnerability was triggered through a file upload feature that allowed SVG files without proper sanitization.

Unlike Reflected XSS, Stored XSS is significantly more dangerous because the malicious payload is **permanently stored on the server** and executes automatically in the browser of every user who visits the affected page — no interaction or social engineering required.

### Target Overview

**Application Type:** Web-based Tasks & Project Management Platform

**Vulnerable Feature:** File Attachment Upload within Project Creation

**Endpoint Structure:**

`/app/organization/{org_id}/group/{group_id}/project/{project_id}/task/{task_id}`
**Severity:** High

### Why Is SVG Dangerous?

Before diving into the technical details, it’s important to understand why SVG files are particularly dangerous in the context of file uploads.

SVG (Scalable Vector Graphics) files are **not just images** — they are XML-based documents that fully support:

- Inline JavaScript via event handlers like onload
- External script inclusion via \<script> tags
- DOM manipulation within the browser context

This means that if an application renders an SVG file directly in the same origin without sanitization, it becomes a perfect XSS vector.

### Reconnaissance

#### Exploring the Application

I started by mapping out the application’s features as a regular authenticated user. I noticed the platform offered a **Create Project** functionality under the following navigation path:

/app/organization/\[ID\]/group/\[ID\]/project/\[ID\]/task/\[ID\]

Upon clicking **Create Project**, the form presented:

- Project Name
- Description
- **File Attachment** — with a Drag & Drop or Browser File option

The moment I saw that file upload field, one question immediately came to mind:

“Does this application accept SVG files?”

### Testing Phase

#### Step 1 — Crafting the SVG Payload

I created a simple SVG file with an embedded JavaScript payload using the onload event handler:

```
<svg xmlns="http://www.w3.org/2000/svg" onload="alert('hacked with Ashraf')">
</svg>
```
**Why this payload?**

- The onload attribute fires immediately when the SVG is rendered in the browser
- No user interaction is needed beyond opening the file
- It executes within the application’s origin context

#### Step 2 — Uploading the File

I saved the payload as test.svg and uploaded it through the attachment field in the Create Project form.

The application accepted the file **without any error or warning** — no file type restriction, no content validation, no sanitization.

#### Step 3 — Triggering the Vulnerability

After the upload completed, I navigated to the uploaded SVG file from within the application.

**The result:**

The JavaScript executed immediately — an alert box appeared with the message:

hacked with Ashraf

The alert was fired within the **application’s origin domain**, confirming this was a true Stored XSS execution context, not a sandboxed file viewer.

### Attack Flow

Attacker Creates Project

│

▼

Uploads Malicious SVG File

│

▼

Application Stores File Without Sanitization

│

▼

Victim Opens the Uploaded SVG

│

▼

JavaScript Executes in Victim's Browser

│

▼

✅ Stored XSS Confirmed

### Impact

This vulnerability has serious real-world implications:

Attack Scenario          Description

Session Hijacking Steal session cookies via document.cookie

Account Takeover Capture credentials or tokens

PhishingInject fake login forms within the trusted domain

Malware Delivery Redirect victims to malicious external pages

Data Exfiltration Access and send sensitive DOM data to an attacker-controlled server

The fact that this is **Stored XSS** means every team member with access to the project is a potential victim — the attack scales automatically.

### Root Cause Analysis

The vulnerability existed due to multiple missing security controls:

1. **No file type validation** — The server accepted SVG without restricting to safe image formats
2. **No content sanitization** — SVG content was stored and served as-is
3. **Same-origin file serving** — The SVG was rendered directly under the application’s domain, giving the JavaScript full access to cookies and the DOM
4. **No Content Security Policy (CSP)** — No policy was in place to block inline script execution

### Remediation Recommendations

#### 1. Sanitize SVG Content

Strip all JavaScript-related attributes and tags from SVG files before storing them. Libraries like **DOMPurify** can sanitize SVG on the client side, and server-side tools like **svg-sanitizer** can handle it on the backend.

#### 2. Serve Uploads from a Separate Domain

Serve all user-uploaded files from an isolated domain (e.g., static.example-cdn.com) so that even if JavaScript executes, it has no access to the main application's cookies or DOM.

#### 3. Implement a Strong Content Security Policy (CSP)

Add a CSP header that blocks inline script execution:

Content-Security-Policy: default-src 'self'; script-src 'self'; object-src 'none';

#### 4. Restrict Allowed File Types

Whitelist only safe image formats (PNG, JPG, GIF, WebP) and explicitly block SVG, HTML, and XML uploads where not necessary.

#### 5. Validate File Content (MIME Sniffing)

Don’t rely solely on the file extension. Validate the actual content type on the server side by inspecting the file’s magic bytes.

### Conclusion

This bug demonstrates how a seemingly simple file upload feature can lead to a critical Stored XSS vulnerability when SVG files are accepted without proper sanitization or isolation. The fix isn’t complicated, but the impact of leaving it unpatched is severe — every user who opens that project becomes a victim.

Always question every file upload field. And always ask: *“What happens if I upload an SVG?”*

*Happy hunting. 🎯*

*— Ashraf (0*[xPinocchioSec](http://twitter.com/OxPinocchioSec)*)*
