# File Path Traversal

- **Source URL:** https://medium.com/@nitishmukhiya/file-path-traversal-complete-hands-on-guide-from-portswigger-labs-to-real-world-testing-bb288a5457a7
- **Fetched from:** https://systemweakness.com/file-path-traversal-complete-hands-on-guide-from-portswigger-labs-to-real-world-testing-bb288a5457a7?source=rss-174be325ed82------2
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:**  (id 14909)
- **Method:** medium-rss-feed (full content:encoded) readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- **Author/Published (RSS):** Nitish Mukhiya / Sun, 13 Sep 2026 02:44:26 GMT

***Note on notation:*** *Throughout this article, traversal sequences are written in “defanged” form — e.g. ../ instead of the literal two-dot-plus-slash sequence — a convention widely used in security write-ups (similar to defanging IPs/URLs in threat-intel reports) so the text isn't mistaken for a live payload by automated content scanners. Replace .. with two literal periods when actually testing in Burp Suite.*

Most web applications need to serve files at some point — a product image, a downloadable invoice, a user avatar, a document preview. To do this, the application usually accepts a filename or path as user input and uses it to build a path on the server’s filesystem.

A normal request looks harmless:

/image?filename=11.jpg

The application expects filename to be one of a small set of legitimate values — 11.jpg, 12.jpg, and so on — and reads that file from a fixed directory on disk. The problem starts when the application trusts this parameter without checking that the resulting path actually stays inside the folder it's supposed to serve files from.

File Path Traversal (also called Directory Traversal) is what happens when an attacker manipulates that filename parameter to make the application read a file *outside* the intended directory. Instead of 11.jpg, the attacker supplies a value built from special path sequences that walk the application back up the directory tree and into files it was never meant to expose.

This class of vulnerability is worth learning well because:

***Note:*** *The difference between a “normal” file request and an “attacker-controlled” one isn’t the HTTP method or the endpoint — it’s whether the server validates that the resolved path stays within an allowed boundary before it opens the file.*

At its core, Path Traversal abuses the operating system’s own path syntax. On Linux and most Unix-like systems, a parent-directory marker (two dots) refers to the parent of the current directory. If a web application blindly concatenates user input onto a base directory, an attacker can chain these markers to escape that directory entirely:

/image?filename=\[dot\]\[dot\]/\[dot\]\[dot\]/\[dot\]\[dot\]/etc/passwd

If the application’s image folder is, say, /var/www/html/images/, then each traversal marker moves one level up:

/var/www/html/images/\[dot\]\[dot\]/\[dot\]\[dot\]/\[dot\]\[dot\]/etc/passwd

→ /var/www/html/\[dot\]\[dot\]/\[dot\]\[dot\]/etc/passwd

→ /var/www/\[dot\]\[dot\]/etc/passwd

→ /etc/passwd

A few concepts worth being precise about:

These three terms get used interchangeably by beginners, but they describe different vulnerability classes with different potential impact.

Vulnerability What Happens Typical Mechanism Potential Impact **Path Traversal** Application reads a file outside the intended directory and returns its contents open() / file\_get\_contents() / send\_file() on an unvalidated path Disclosure of file contents (read-only) **Local File Inclusion (LFI)** Application *includes* (parses/executes) a local file as part of its own code or template include(), require(), template engines that load "local" files Disclosure, and in vulnerable configurations, **code execution Remote File Inclusion (RFI)** Application includes a file hosted on a remote, attacker-controlled server Remote include in permissive PHP configurations Direct remote code execution (in modern PHP this generally requires allow\_url\_include, which is off by default)

Traversal  → read only

Inclusion → read + potential execution (depends on language/runtime)

*Not every path traversal is an LFI, and not every LFI is remotely exploitable as RFI. Confirm impact for each specific application rather than assuming escalation is automatic.*

Before testing traversal, it helps to be completely comfortable with how paths work on the command line, because the exact same logic is what the web application’s filesystem calls are doing under the hood.

/

├── home

│ └── kali

│ └── Desktop

└── var

└── www

└── html

└── images

An **absolute path** always starts from the root (/) and fully specifies the location, regardless of where you currently are:

cd /var/www

A **relative path** is interpreted starting from wherever you currently are, and the parent-directory marker means “go up one directory”:

cd \[dot\]\[dot\]/\[dot\]\[dot\]/\[dot\]\[dot\]/var/www

If your current directory is /home/kali/Desktop, that walks up three levels (to /) and back down into var/www — landing in the same place as the absolute path above, just via a longer route.

This is exactly the mechanic that path traversal payloads exploit: by supplying enough traversal markers, an attacker can walk from a web application’s intended file directory all the way back to the filesystem root, then back down into any file the web server process has permission to read.

Path traversal candidates show up anywhere the application takes a file-related identifier from the user. Common parameter names to look for include:

?file=

?filename=

?path=

?download=

?view=

?template=

?doc=

But don’t limit the search to query strings. The same pattern shows up in:

**Reconnaissance tools** that help surface these parameters at scale: **ParamSpider** and **gau** (GetAllUrls) for pulling historical/known parameters from a domain, alongside Burp Suite’s Proxy/HTTP History for live traffic.

These locations are interesting because they all share the same underlying pattern: **user input directly or indirectly influences a filesystem path that the server will open and return.**

Reconnaissance

↓

Identify file-related functionality

↓

Inspect requests

↓

Test normal behavior

↓

Try basic traversal

↓

Analyze response

↓

Test bypass techniques

↓

Confirm impact

↓

Document evidence

Burp Suite’s **Proxy/HTTP History** is where you’ll spot candidate requests, **Repeater** is where you’ll manually iterate on one request, and **Intruder** is where you automate testing a payload list against one injection point.

**Steps to reproduce:**

**Lesson:** No filtering exists at all here — any correctly-depthed traversal payload works immediately, because the application never validates the resolved path.

**Lesson:** The filter only catches the relative traversal pattern; it has a blind spot for direct absolute paths.

**Lesson:** Single-pass stripping filters are trivially defeated by nesting the pattern inside itself.

**Lesson:** An extra decode step performed *after* the filter check creates a gap that double-encoding walks straight through.

**Lesson:** Validating that a string *starts with* an expected path is meaningless if the check happens *before* canonicalization — it checks the input’s shape, not where it actually resolves to.

***Important caveat:*** *this technique is* ***not universally effective today****. It relied on specific behavior in older PHP versions (pre-5.3.4) and certain C library string-handling functions. Modern PHP and most current runtimes either reject null bytes outright or handle them safely. This lab exists to teach the* historical *mechanism — confirm the stack before assuming it applies to a real target.*

There’s no universal “correct” depth — it depends entirely on how deep the file-serving directory sits relative to the filesystem root. Extra traversal markers beyond the root are harmless once you’ve already reached /, so it's common to try a range of depths, one level at a time, since some servers behave differently depending on exact depth:

\[dot\]\[dot\]/etc/passwd

\[dot\]\[dot\]/\[dot\]\[dot\]/etc/passwd

\[dot\]\[dot\]/\[dot\]\[dot\]/\[dot\]\[dot\]/etc/passwd

\[dot\]\[dot\]/\[dot\]\[dot\]/\[dot\]\[dot\]/\[dot\]\[dot\]/etc/passwd

\[dot\]\[dot\]/\[dot\]\[dot\]/\[dot\]\[dot\]/\[dot\]\[dot\]/\[dot\]\[dot\]/etc/passwd

\[dot\]\[dot\]/\[dot\]\[dot\]/\[dot\]\[dot\]/\[dot\]\[dot\]/\[dot\]\[dot\]/\[dot\]\[dot\]/etc/passwd

... continue up to roughly 10 levels if needed

Alternative separator styles, worth trying since behavior depends on OS/web server/framework/path-parser:

\[dot\]\[dot\]//\[dot\]\[dot\]//\[dot\]\[dot\]//    (doubled-slash variant)

\[dot\]\[dot\]\\\[dot\]\[dot\]\\\[dot\]\[dot\]\ (Windows-native backslash)

\[dot\]\[dot\]\\\\\[dot\]\[dot\]\\\\\[dot\]\[dot\]\\ (escaped-backslash variant)

None of these should be assumed to work universally — they’re candidates to test, not guarantees.

Many applications block direct use of the traversal marker, but decoding behavior in proxies or application layers may allow functionally equivalent payloads through. Effective categories include:

These techniques become even more powerful when path values pass through **multiple decoding layers** — for example, a request that goes through Nginx, then a Node.js layer, then a Python application, where each layer may decode independently.

Browse the target with Burp’s proxy running. Filter history for requests containing keywords like file, filename, path, doc, or download.

Keywords to scan responses for: root:, /bin/bash, DB\_PASSWORD, define('DB\_PASSWORD, root:x:0:0:root:/root:/bin/bash, daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin.

*Only run this kind of testing against systems you are explicitly authorized to test — a lab environment, a bug bounty program’s in-scope assets, or your own infrastructure.*

Not every file below will exist or be readable on every target — it depends entirely on OS, configuration, and process privileges.

**Unix/Linux:**

**Windows:**

**Web-specific and deployment-related:**

These files often contain JWT signing secrets, SMTP credentials, database logins, API keys, hardcoded cloud tokens, and internal service credentials used across CI/CD pipelines or production systems.

**Direct impact:** disclosure of arbitrary file contents readable by the web server process; exposure of application source code; disclosure of internal file-system paths and directory structure.

**Possible chained impact:**

Path Traversal → Read configuration file → Discover credential → Credential reused elsewhere → Potential further compromise

For example, reading a .env file discloses a database password → that password is reused for an internal admin panel → access to that panel exposes more of the environment. The *ceiling* of the impact depends entirely on what a given application stores on disk and how those secrets are used elsewhere — assess case-by-case rather than assuming.

Categories of consequence: sensitive information disclosure, credential exposure (database, SMTP, JWT signing secrets), API key exposure, cloud credential exposure (AWS/GCP/Azure), source-code disclosure, internal path/architecture disclosure, configuration disclosure, and potential privilege escalation or lateral movement depending on what’s exposed.

Defenders should watch for: repeated parent-directory markers, single and double URL-encoded variants, unusually long or repeated traversal sequences, repeated manipulation of file-related parameters, and requests targeting known sensitive file paths (/etc/passwd, win.ini, .env).

Relevant telemetry: **web server logs** (raw request URLs, including encoded sequences), **WAF** (many ship default traversal rules, though bypassable via the encoding techniques above), **SIEM** (correlate traversal-pattern requests across time/source IP), **application logs** (ideally logging the resolved, post-normalization path), and **endpoint telemetry** (unusual file-access patterns by the serving process).

$root = '/var/www/html/docs/';

$user\_input = $\_GET\['file'\];

$path = realpath($root . $user\_input);

```
if ($path === false || strpos($path, realpath($root)) !== 0) {
    http_response_code(403);
    echo "Access denied";
    exit;
}
```
echo file\_get\_contents($path);

realpath() resolves the concatenated path into its canonical, absolute form, fully processing any traversal or single-dot segments. The strpos check rejects the request unless the resolved path still starts inside $root — this is the check that catches traversal, because no matter how the input was crafted, once it's fully resolved, either it's inside $root or it isn't.

from flask import send\_file, abort

import os

ROOT = '/var/www/html/docs/'

def safe\_join(root, \*paths):

root = os.path.realpath(root)

path = os.path.realpath(os.path.join(root, \*paths))

if os.path.commonpath(\[root, path\]) != root:

return None

return path

```
filename = request.args.get('file')
path = safe_join(ROOT, filename)
if not path:
    abort(403)
return send_file(path)
```
os.path.commonpath(\[root, path\]) finds the longest shared prefix between the canonical root and the resolved candidate path — if that shared prefix isn't exactly root, the candidate has escaped the allowed directory and safe\_join returns None instead of a path, so the request is rejected before any file is opened.

Blacklisting characters or sequences is a reactive approach — it only defends against patterns you thought of in advance, and the labs above show how easily naive stripping is bypassed. A stronger design avoids the problem entirely:

/download?file=/some/user/supplied/path     ← avoid this shape

/download?id=123                             ← prefer this

↓

Database lookup

↓

Known filename (fixed, server-controlled)

↓

Controlled file access

The user only ever supplies an opaque identifier; the actual filename is looked up server-side from a fixed, trusted mapping — eliminating traversal as a possibility rather than trying to filter it out.

*Removing traversal markers from user input alone is* ***not*** *a complete defense — Labs 3 and 4 demonstrate exactly why naive stripping and decode-order issues make blacklist-only filtering unreliable.*

Understand → Observe → Identify → Test → Bypass → Confirm → Assess Impact → Report

Technique Concept Purpose Basic traversal Repeated parent-directory markers Test parent-directory traversal Absolute path Direct filesystem-root path Test direct absolute path access URL encoding Percent-encoded marker Test single-decode filter behavior Double encoding Percent-encoded percent-encoding Test multiple/superfluous decoding layers Overlong UTF-8 Non-standard multi-byte encoding Test legacy/non-strict parsers Mixed slashes Forward vs. backslash separators Test parser/OS differences Non-recursive bypass Marker nested inside itself Test single-pass stripping filters Null byte Percent-encoded null + fake extension Test legacy extension validation Prefix validation bypass Expected prefix + trailing traversal Test canonicalization order flaws

Lab Main Concept Key Lesson Lab 1: Simple case Unfiltered traversal Basic traversal works when no validation exists at all Lab 2: Absolute path bypass Relative-only filtering Blocking the relative marker doesn’t block direct absolute paths Lab 3: Non-recursive stripping Single-pass filters Stripping a pattern once, without re-checking output, can leave a valid sequence behind Lab 4: Superfluous URL-decode Multiple decoding layers An extra decode step performed after filtering can be exploited via double encoding Lab 5: Start-of-path validation Prefix checks before canonicalization Validating that input *starts with* an expected path is meaningless if done before path resolution Lab 6: Extension validation / null byte Legacy string-termination behavior Extension checks alone are weak; historical null-byte truncation shows why validating *content* matters more than validating *filename shape*

File Path Traversal is, at its core, a story about unsafe path handling: an application trusts user input to help build a filesystem path, and fails to confirm — after full resolution — that the result stays where it’s supposed to. Every payload category and bypass technique in this article exists because of a specific, identifiable gap in how a particular filter processes input: whether it checks before or after decoding, before or after normalization, on the raw string or the resolved one.

That’s the real skill being tested across these six labs. Memorizing a list of traversal payloads gets you through the first one or two labs. Understanding *why* a filter is blocking what it’s blocking — and reasoning backward to the exact bypass that defeats that specific logic — is what gets you through the rest, and what will make the difference on a real target that doesn’t match any lab exactly.

Burp Suite’s Proxy, Repeater, and Intruder aren’t just tools for firing payloads faster; used well, they’re how you build the evidence needed to understand what an application is actually doing with your input. On the defensive side, the lesson is consistent across every lab: canonicalize before you validate, and prefer allowlisting known-good identifiers over trying to blacklist an open-ended set of bad ones.

For anyone starting out in bug bounty hunting or application security: path traversal is one of the best vulnerability classes to build real methodology on, precisely because the difference between “payload didn’t work” and “target isn’t vulnerable” is so often just a matter of understanding one more layer of how the application processes your input.

**Nitish Mukhiya** is a security researcher and bug bounty hunter focused on web application security, currently sharpening his skills through PortSwigger’s Web Security Academy.

[File Path Traversal: Complete Hands-On Guide from PortSwigger Labs to Real-World Testing](https://systemweakness.com/file-path-traversal-complete-hands-on-guide-from-portswigger-labs-to-real-world-testing-bb288a5457a7) was originally published in [System Weakness](https://systemweakness.com) on Medium, where people are continuing the conversation by highlighting and responding to this story.
