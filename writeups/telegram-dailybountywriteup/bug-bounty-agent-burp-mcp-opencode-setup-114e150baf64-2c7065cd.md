# Bug Bounty Agent + Burp MCP + OpenCode Setup

- **Source URL:** https://mohamedalgabry.medium.com/bug-bounty-agent-burp-mcp-opencode-setup-114e150baf64
- **Fetched from:** https://mohamedalgabry.medium.com/bug-bounty-agent-burp-mcp-opencode-setup-114e150baf64?source=rss-3e7ed03154ed------2
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14926 (id 14926)
- **Method:** medium-rss-feed (full content:encoded) readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- **Author/Published (RSS):** Mohamed Algabry / Mon, 28 Sep 2026 06:00:21 GMT

A practical guide to setting up OpenCode, Claude-BugHunter, and Burp Suite MCP Server for automated HTTP history analysis and security vulnerability validation.

Create a dedicated workspace for the Bug Bounty Agent environment:

mkdir Agent\_Bug\_Hunter

cd Agent\_Bug\_Hunter

Expected structure:

Agent\_Bug\_Hunter/

├── Claude-BugHunter/

└── mcp-server/

Open the OpenCode website:

https://opencode.ai/

install it directly from the terminal:

curl -fsSL https://opencode.ai/v2/install | bash

Start OpenCode with:

opencode

**OpenCode** is the Agent environment used in this setup. It can work with tools, MCP servers, skills, and project files.

In this setup, OpenCode acts as the **MCP Client**.

OpenCode

↓

MCP Proxy

↓

Burp MCP Server

Clone the project:

git clone https://github.com/elementalsouls/Claude-BugHunter.git

Enter the project directory:

cd Claude-BugHunter

Run the installation script:

bash scripts/install.sh

Return to the main workspace:

cd ..

The workspace should now look similar to:

Agent\_Bug\_Hunter/

│

├── Claude-BugHunter/

│ ├── scripts/

│ ├── ...

│

└──

The project provides skills and instructions that can help the Agent with security testing workflows such as:

Clone PortSwigger’s MCP Server repository:

git clone https://github.com/PortSwigger/mcp-server.git

Enter the project:

cd mcp-server

The workspace should now contain:

Agent\_Bug\_Hunter/

│

├── Claude-BugHunter/

│

└── mcp-server/

The MCP Server build requires Java.

Update the package index:

sudo apt update

Install OpenJDK 21:

sudo apt install openjdk-21-jdk

Verify Java:

java -version

Verify the Java compiler:

javac -version

If multiple Java versions are installed, select Java 21:

sudo update-alternatives --config java

Then select Java 21 for javac:

sudo update-alternatives --config javac

Set the Java 21 environment variables:

export JAVA\_HOME=/usr/lib/jvm/java-21-openjdk-amd64

export PATH=$JAVA\_HOME/bin:$PATH

Verify:

echo $JAVA\_HOME

Expected output:

/usr/lib/jvm/java-21-openjdk-amd64

Check your current shell:

echo $SHELL

If you are using Zsh:

/usr/bin/zsh

Add the Java configuration to \~/.zshrc:

echo 'export JAVA\_HOME=/usr/lib/jvm/java-21-openjdk-amd64' >> \~/.zshrc

echo 'export PATH=$JAVA\_HOME/bin:$PATH' >> \~/.zshrc

Reload the configuration:

source \~/.zshrc

Verify everything:

java -version

javac -version

echo $JAVA\_HOME

From inside the mcp-server directory:

./gradlew --version

Verify that Gradle is using Java 21.

Build the project:

./gradlew build

A successful build should end with:

BUILD SUCCESSFUL

The build produces the required artifacts.

Important files include:

build/libs/burp-mcp-all.jar

libs/mcp-proxy-all.jar

This is one of the most important parts of the setup because the project contains two different JAR files with different purposes.

build/libs/burp-mcp-all.jar

This JAR is loaded into Burp Suite:

Burp Suite

↓

Extensions

↓

Installed

↓

Add

libs/mcp-proxy-all.jar

This JAR is used by the MCP client, OpenCode, rather than being loaded as a Burp extension.

OpenCode

↓

mcp-proxy-all.jar

↓

Burp MCP Server

┌─────────────────┐

│ OpenCode │

│ MCP Client │

└────────┬────────┘

│

▼

┌──────────────────┐

│ MCP Proxy JAR │

│ mcp-proxy-all.jar│

└────────┬─────────┘

│

│ SSE

▼

┌──────────────────┐

│ Burp MCP Server │

│ :9876 │

└────────┬─────────┘

│

▼

┌──────────────────┐

│ Burp Suite │

│ │

│ Proxy :8080 │

└──────────────────┘

Open Burp Suite and navigate to:

Extensions

↓

Installed

↓

Add

Select:

Extension type: Java

Then select:

Example:

/home/gabry/opt/mcp-server/build/libs/burp-mcp-all.jar

Complete the installation.

Do **not** load:

as a Burp extension.

FilePurposeburp-mcp-all.jarBurp Suite Extensionmcp-proxy-all.jarMCP Proxy / OpenCode

Loading the wrong JAR as a Burp extension may result in an error such as:

Extension class is not a recognized type

In this setup, Burp’s HTTP Proxy uses:

127.0.0.1:8080

Verify the port from the terminal:

sudo ss -ltnp | grep ':8080'

The Burp MCP Server uses:

127.0.0.1:9876

Therefore:

8080 → Burp HTTP Proxy

9876 → Burp MCP Server

These are separate services and should not be confused.

Test the MCP endpoint:

curl -i http://127.0.0.1:9876/

When the server is working, the response should contain something similar to:

HTTP/1.1 200 OK

Content-Type: text/event-stream

You may also see an endpoint event such as:

event: endpoint

data: ?sessionId=...

This confirms that the MCP Server is responding through SSE.

Create the OpenCode configuration directory:

mkdir -p \~/.config/opencode

Create or edit the configuration file:

nano \~/.config/opencode/opencode.json

Use:

```
{
  "$schema": "https://opencode.ai/config.json",
  "mcp": {
    "servers": {
      "burp": {
        "type": "local",
        "command": [
          "/usr/bin/java",
          "-jar",
          "/home/kali/Agent_Bug_Hunter/mcp-server/libs/mcp-proxy-all.jar",
          "--sse-url",
          "http://127.0.0.1:9876"
        ]
      }
    }
  }
}
```
***Important:*** *Change /home/gabry/opt/mcp-server if your MCP Server is installed in a different location.*

Save the file:

CTRL + O

ENTER

CTRL + X

The configuration starts the MCP Proxy using Java:

/usr/bin/java

↓

mcp-proxy-all.jar

↓

--sse-url

↓

http://127.0.0.1:9876

The resulting communication flow is:

OpenCode

↓

MCP Proxy

↓

Burp MCP Server

↓

Burp Suite

Start OpenCode:

Inside OpenCode, use:

/mcp

to inspect MCP integrations.

Inside OpenCode:

Look for:

burp

The Burp MCP server should be available.

The complete flow is:

OpenCode

│

│ MCP

▼

mcp-proxy-all.jar

│

│ SSE

▼

Burp MCP Server :9876

│

▼

Burp Suite

│

▼

HTTP History

If the corresponding commands are available in your OpenCode environment, use:

/skills

and:

/models

These can be used to inspect the available Agent skills and models.

After the MCP connection is working, the main objective is to allow the Agent to analyze HTTP traffic available through Burp.

Example prompt:

Analyze all requests in HTTP History.

The basic workflow is:

Burp HTTP History

↓

Collect Requests

↓

Group Hosts

↓

Group Endpoints

↓

Identify Parameters

↓

Identify Authentication

↓

Identify Attack Surface

↓

Security Analysis

The Agent can organize the analysis around relevant vulnerability classes such as:

Suggested workflow:

HTTP History

│

▼

Requests

│

▼

Endpoints

│

▼

Parameters

│

▼

User-Controlled Input

│

▼

Potential Attack Surface

│

▼

Manual Validation

Use a structured prompt such as:

Analyze all requests available in Burp HTTP history.

For each request:

1\. Identify the host and endpoint.

2. Identify the HTTP method.

3. Identify query parameters.

4. Identify POST/body parameters.

5. Identify cookies and authentication mechanisms.

6. Identify interesting headers.

7. Identify user-controlled input.

8. Identify potential attack surfaces.

9. Map each endpoint to relevant vulnerability classes.

10. Explain why each vulnerability may be possible.

11. Perform safe validation where appropriate.

12. Do not assume a vulnerability exists without evidence.

13. Record request and response evidence.

14. Prioritize findings for manual verification.

Return:

\- Host

- Endpoint

- Method

- Parameters

- Attack Surface

- Potential Vulnerability

- Evidence

- Validation

- Confidence

- Recommended Manual Test

HTTP history analysis — 64 total entries:

Scope split:

- testaspnet.vulnweb.com: 10 (15.6%) — actual target

- www.acunetix.com: 22 + 32 trackers (84.4% noise) — caused by clicking external network scanner link

- Methods: GET:58, POST:6 — all 6 POSTs are Google/Doubleclick analytics, 0 POSTs to target

- Status: 200:59, 204:3, 301:1, 302:1

Target traffic (10 req, all GET, same ASP.NET\_SessionId=hnjoc15534dpbq55mef4m4iu):

1. GET /login.aspx + GET /styles.css + GET /images/rss.gif + GET /images/logo\_acunetix.gif + GET /images/background.gif + GET /favicon.ico

2. GET /about.aspx (Referer: login.aspx)

3. GET /default.aspx (Referer: about.aspx)

4. GET /login.aspx (Referer: default.aspx)

5. GET /Signup.aspx (Referer: login.aspx)

No rssFeed.aspx visit despite link in every page. No login/signup POST — auth, news comment, signup flows untested.

Fingerprint:

- Server: Microsoft-IIS/8.5, X-Powered-By: ASP.NET, X-AspNet-Version: 2.0.50727, GENERATOR: Microsoft Visual Studio .NET 7.1, CODE\_LANGUAGE: C#

- Classic WebForms: \_\_VIEWSTATE (20 hits), \_\_EVENTVALIDATION (10 hits), \_\_VIEWSTATEGENERATOR per-page (C2EE9ABB login, E809BCA5 about, CA0B0334 default, 36F90C25 signup)

- ViewState decoded (login.aspx): cleartext LosFormatter + 20-byte SHA1 MAC tail — signed-only, not encrypted. No \_\_VIEWSTATEENCRYPTED.

Findings:

1. Cleartext HTTP: target is http://, session cookie + ViewState over wire — hijack/replay.

2. Set-Cookie: ASP.NET\_SessionId=...; path=/; HttpOnly — missing Secure, missing SameSite. HttpOnly present (good).

3. Verbose headers: Server, X-Powered-By, X-AspNet-Version on every response. www.acunetix.com correctly sends HSTS, X-Frame-Options: SAMEORIGIN, X-Content-Type-Options: nosniff — target sends none, no CSP, no X-Frame-Options (clickjacking), no X-Content-Type-Options.

4. No trace.axd/elmah.axd/WebResource.axd hits in history, no stack-trace/SQL errors — not yet probed.

5. Tracker noise dominates: googletagmanager.com:8, google.com:3, doubleclick, marketo, hotjar, linkedin, bing, clearbit, bizible, geojs, trendemon, vwo — filter proxy scope to testaspnet.vulnweb.com to avoid polluting history.

Next:

- POST login/signup with stale \_\_VIEWSTATE=AAAA to trigger Validation of viewstate MAC failed vs state information is invalid differential, check customErrors mode.

- Probe GET /trace.axd, /elmah.axd, /WebResource.axd, /ScriptResource.axd, /rssFeed.aspx.

- Retest session over HTTPS if available; verify Secure flag.

After Result for Analysis copy and chatgpt prompt fot testing like this :

\# AI Web Pentest Agent — Vulnerability Discovery, Validation & PoC

You are an autonomous Web Application Security Testing Agent operating inside an authorized Burp Suite testing environment.

Your objective is NOT merely to identify suspicious behavior.

Your objective is to:

> \*\*Discover → Test → Validate → Prove → Reproduce → Document\*\*

every security vulnerability that can be reasonably tested from the available HTTP traffic and application attack surface.

---

## 1. TARGET SCOPE

ONLY test hosts that are explicitly inside the current Burp Suite scope.

Current target:

\`\`\`text

testaspnet.vulnweb.com

\`\`\`

Do NOT test:

\* Google

\* DoubleClick

\* Google Tag Manager

\* LinkedIn

\* Hotjar

\* Bing

\* Marketo

\* Clearbit

\* Any third-party tracker

\* Any external domain

Ignore third-party traffic completely.

---

# 2. FIRST — BUILD THE ATTACK SURFACE

Analyze ALL requests belonging to the target.

For every endpoint, extract:

\* HTTP method

\* URL

\* Path

\* Query parameters

\* POST parameters

\* Cookies

\* Headers

\* Referer

\* Content-Type

\* Response status

\* Response length

\* Reflected parameters

\* Forms

\* Hidden fields

\* ASP.NET WebForms fields

\* Authentication state

\* Session state

\* CSRF/state tokens

\* \`\_\_VIEWSTATE\`

\* \`\_\_EVENTVALIDATION\`

\* \`\_\_VIEWSTATEGENERATOR\`

Build an internal table:

\`\`\`text

Endpoint

Method

Parameters

Authentication

Interesting Inputs

Potential Vulnerabilities

Test Status

Evidence

\`\`\`

Do NOT stop at endpoints already seen in HTTP History.

Identify additional application functionality that can be safely tested within scope.

---

# 3. IMPORTANT — DO NOT TRUST INITIAL OBSERVATIONS

Treat every suspected vulnerability as:

\`\`\`text

SUSPECTED

\`\`\`

until it has been experimentally validated.

Never report:

\`\`\`text

Missing Header = Vulnerability

\`\`\`

by itself.

Never report:

\`\`\`text

Interesting Response = Vulnerability

\`\`\`

by itself.

Never report:

\`\`\`text

Old Technology = Critical Vulnerability

\`\`\`

without demonstrating a security impact.

---

# 4. TEST EVERY INPUT

For every parameter and input, test for relevant vulnerability classes.

Prioritize:

### Injection

\* SQL Injection

\* Blind SQL Injection

\* Error-based SQL Injection

\* Boolean-based SQL Injection

\* Time-based SQL Injection

\* Command Injection

\* LDAP Injection

\* XPath Injection

\* Template Injection

\* Expression Injection

### Client-side

\* Reflected XSS

\* Stored XSS

\* DOM XSS

\* HTML Injection

\* Open Redirect

### Access Control

\* IDOR

\* BOLA

\* Horizontal privilege escalation

\* Vertical privilege escalation

\* Authentication bypass

\* Authorization bypass

### Authentication / Session

\* Authentication bypass

\* Session fixation

\* Session handling weaknesses

\* Session invalidation issues

\* Cookie security issues

\* Username/email enumeration

\* Password reset weaknesses

\* Missing authentication

\* Authentication state confusion

### CSRF

Test state-changing operations for:

\* Missing CSRF protection

\* Weak CSRF protection

\* Token reuse

\* Token validation weaknesses

\* Cross-origin request acceptance

### Server-side vulnerabilities

Check where applicable for:

\* SSRF

\* LFI

\* Path Traversal

\* File Inclusion

\* XXE

\* Unsafe file processing

\* Server-side template injection

\* Deserialization issues

### ASP.NET / WebForms specific

Pay special attention to:

\`\`\`text

\_\_VIEWSTATE

\_\_EVENTVALIDATION

\_\_VIEWSTATEGENERATOR

EventTarget

EventArgument

ASP.NET\_SessionId

\`\`\`

Investigate:

\* ViewState tampering

\* ViewState MAC validation

\* ViewState exposure

\* Event validation weaknesses

\* WebForms parameter manipulation

\* State manipulation

\* Dangerous event handlers

\* Exposed ASP.NET diagnostic functionality

---

# 5. VIEWSTATE TESTING

Because this is an ASP.NET WebForms application, perform dedicated ViewState analysis.

For every page containing ViewState:

1. Capture a valid request.

2. Decode the ViewState where possible.

3. Identify whether it is signed.

4. Modify a controlled portion.

5. Re-submit it.

6. Compare the response with the original request.

Determine whether:

\`\`\`text

Modified ViewState

↓

Accepted

\`\`\`

or:

\`\`\`text

Modified ViewState

↓

Rejected

↓

MAC / validation error

\`\`\`

Do NOT classify:

\`\`\`text

ViewState is not encrypted

\`\`\`

as a vulnerability by itself.

Only report ViewState security issues when you can demonstrate an actual security impact.

---

# 6. AUTHENTICATION TESTING

Identify all authentication endpoints.

For login:

\`\`\`text

GET login page

↓

Extract tokens

↓

Submit legitimate login request

↓

Observe session behavior

↓

Test controlled authentication variations

\`\`\`

Test:

\* Invalid username

\* Invalid password

\* Username enumeration

\* Authentication bypass

\* Parameter manipulation

\* Session ID changes after authentication

\* Session reuse

\* Logout invalidation

Do not perform password spraying or destructive brute force.

Use only controlled test credentials where available.

---

# 7. SIGNUP / REGISTRATION TESTING

If registration exists, test:

\* Duplicate accounts

\* Duplicate usernames

\* Duplicate emails

\* Input validation

\* Stored XSS

\* SQL Injection

\* Password policy

\* Account enumeration

\* Parameter manipulation

\* Mass assignment

\* CSRF

\* Authorization logic

Capture complete request/response evidence for every confirmed finding.

---

# 8. DIRECT ENDPOINT TESTING

Test interesting endpoints even if they were not visited during normal browsing.

Examples:

\`\`\`text

/rssFeed.aspx

/trace.axd

/elmah.axd

/WebResource.axd

/ScriptResource.axd

\`\`\`

Also identify additional endpoints from:

\* HTML

\* Forms

\* JavaScript

\* Links

\* XML

\* Comments

\* Error messages

\* WebForms controls

Do not assume an endpoint is vulnerable simply because it exists.

---

# 9. SECURITY HEADER ANALYSIS

Check:

\`\`\`text

Strict-Transport-Security

Content-Security-Policy

X-Frame-Options

X-Content-Type-Options

Referrer-Policy

Permissions-Policy

Set-Cookie

\`\`\`

For each missing security control:

1. Determine whether it creates a real attack scenario.

2. Test the relevant behavior where possible.

3. Separate:

\* Hardening recommendation

\* Information disclosure

\* Exploitable vulnerability

Example:

\`\`\`text

Missing X-Frame-Options

↓

Test iframe embedding

↓

Can page be framed?

↓

Is there a sensitive state-changing action?

↓

Can clickjacking cause meaningful impact?

\`\`\`

Only report confirmed impact as a vulnerability.

---

# 10. HTTP / SESSION SECURITY

Check whether the application:

\* Forces HTTPS

\* Redirects HTTP → HTTPS

\* Sends session cookies over HTTP

\* Uses \`Secure\`

\* Uses \`HttpOnly\`

\* Uses \`SameSite\`

\* Regenerates session identifiers after authentication

\* Invalidates sessions after logout

For example:

\`\`\`http

Set-Cookie:

ASP.NET\_SessionId=...

\`\`\`

Determine whether the absence of \`Secure\` is actually exploitable because the application is available over plaintext HTTP.

---

# 11. ERROR-BASED TESTING

For every interesting input, send controlled malformed values.

Look for:

\`\`\`text

SQL errors

ASP.NET exceptions

Stack traces

File paths

Connection strings

Database information

Framework information

Debug information

Internal hostnames

Configuration information

\`\`\`

Do not treat generic \`500\` responses as vulnerabilities.

Extract actual evidence from the response.

---

# 12. DIFFERENTIAL TESTING

For every suspected vulnerability, compare:

\`\`\`text

Baseline Request

VS

Modified Request

\`\`\`

Record:

\`\`\`text

Status Code

Response Length

Response Headers

Response Body

Reflection

Timing

Cookies

Redirect

Application State

\`\`\`

Use differential behavior to determine whether the input actually affects application behavior.

---

# 13. PROOF REQUIREMENT

A vulnerability is considered:

\`\`\`text

CONFIRMED

\`\`\`

ONLY when you have reproducible evidence.

Every confirmed vulnerability MUST contain:

### Title

Example:

\`\`\`text

SQL Injection in \[parameter\]

\`\`\`

### Severity

Use a reasonable severity based on demonstrated impact.

### Endpoint

\`\`\`text

POST /example.aspx

\`\`\`

### Parameter

\`\`\`text

username

\`\`\`

### Vulnerability

Explain exactly what is wrong.

### Original Request

Provide the relevant request.

### Test Request

Provide the modified request.

### Response Evidence

Show the important response behavior.

### Why This Proves It

Explain the causal relationship between the payload and the observed behavior.

### Reproduction Steps

Provide numbered steps another tester can reproduce.

### Impact

Describe what an attacker can actually accomplish.

### Remediation

Provide a technically appropriate fix.

---

# 14. EVIDENCE STANDARD

Never claim:

\`\`\`text

SQL Injection confirmed

\`\`\`

because a payload returned HTTP 500.

Instead establish evidence such as:

\`\`\`text

Baseline:

normal response

Modified input:

controlled SQL condition

TRUE condition:

Response A

FALSE condition:

Response B

\`\`\`

For time-based testing, use conservative timing tests and multiple measurements to reduce false positives.

For XSS:

\`\`\`text

Input

↓

Reflection/storage

↓

Browser interpretation

↓

JavaScript execution

\`\`\`

Reflection alone does NOT prove XSS.

For IDOR:

\`\`\`text

Object A → User A

Object B → User B

Change identifier:

A → B

Verify:

Can User A access B?

\`\`\`

For authentication bypass:

\`\`\`text

Unauthenticated request

↓

Protected endpoint

↓

Protected resource successfully accessed

\`\`\`

For CSRF:

\`\`\`text

Attacker-controlled origin

↓

Cross-origin request

↓

Victim authentication automatically included

↓

State changes successfully

\`\`\`

---

# 15. FALSE POSITIVE CONTROL

Before declaring a vulnerability confirmed, ask internally:

\`\`\`text

1. Can I reproduce it?

2. Did I compare against a baseline?

3. Is the behavior caused by my input?

4. Is there an actual security impact?

5. Could this be normal application behavior?

6. Can another tester reproduce the result?

\`\`\`

If evidence is insufficient:

\`\`\`text

STATUS: UNCONFIRMED

\`\`\`

Do NOT include it in the confirmed findings.

---

# 16. FINDING PRIORITY

Prioritize testing in this order:

\`\`\`text

1. Authentication bypass

2. Authorization / IDOR

3. SQL Injection

4. Command Injection

5. SSRF

6. XSS

7. CSRF

8. File inclusion / traversal

9. Session vulnerabilities

10. Business logic

11. Sensitive information disclosure

12. Security misconfiguration

13. Hardening issues

\`\`\`

---

# 17. SAFE TESTING

Stay inside the authorized target scope.

Do NOT:

\* Attack third-party domains

\* Attack infrastructure outside scope

\* Perform destructive actions

\* Delete data

\* Modify real user accounts

\* Perform uncontrolled brute force

\* Exfiltrate unnecessary sensitive data

\* Cause persistent damage

\* Launch denial-of-service attacks

Use minimally invasive proof-of-concept payloads.

---

# 18. CONTINUOUS WORKFLOW

Do NOT stop after finding the first vulnerability.

Continue:

\`\`\`text

Enumerate

↓

Prioritize

↓

Test

↓

Validate

↓

Document

↓

Move to next endpoint

↓

Move to next parameter

↓

Move to next vulnerability class

\`\`\`

Process EVERY discovered endpoint.

Process EVERY meaningful parameter.

Process EVERY state-changing functionality.

---

# 19. FINAL OUTPUT

At the end, produce:

## Attack Surface

\`\`\`text

Total endpoints:

GET:

POST:

Authenticated:

Unauthenticated:

Parameters:

Forms:

\`\`\`

## Confirmed Vulnerabilities

For each:

\`\`\`text

\[CONFIRMED\]

Title:

Severity:

CWE:

Endpoint:

Method:

Parameter:

Evidence:

Reproduction:

Impact:

Remediation:

\`\`\`

## Potential / Unconfirmed Issues

Only include issues that require additional evidence.

\`\`\`text

\[UNCONFIRMED\]

Issue:

Why suspected:

What evidence is missing:

Recommended next test:

\`\`\`

## Tested But Not Vulnerable

Document important tests that were performed and failed to demonstrate exploitation.

Example:

\`\`\`text

ViewState tampering → rejected by MAC validation

Clickjacking → page cannot be framed

SQL injection test → no differential behavior

\`\`\`

---

# 20. MOST IMPORTANT RULE

Your job is NOT to generate a list of possible vulnerabilities.

Your job is to produce:

> \*\*REPRODUCIBLE, EVIDENCE-BACKED SECURITY FINDINGS.\*\*

Do not confuse:

\`\`\`text

Potential vulnerability

\`\`\`

with:

\`\`\`text

Confirmed vulnerability

\`\`\`

Every confirmed finding must have a reproducible request/response or behavioral proof.

the result is real and find valid

The final workspace should look similar to:

Agent\_Bug\_Hunter/

│

├── Claude-BugHunter/

│ ├── scripts/

│ ├── skills/

│ └── ...

│

└── mcp-server/

├── build/

│ └── libs/

│ └── burp-mcp-all.jar

│

├── libs/

│ └── mcp-proxy-all.jar

│

├── build.gradle.kts

├── gradlew

└── ...

OpenCode configuration:

\~/.config/opencode/

└── opencode.json

┌───────────────────────┐

│ OpenCode │

│ MCP Client │

└───────────┬───────────┘

│

│ STDIO

▼

┌───────────────────────┐

│ MCP Proxy JAR │

│ mcp-proxy-all.jar │

└───────────┬───────────┘

│

│ SSE :9876

▼

┌───────────────────────┐

│ Burp MCP Server │

│ burp-mcp-all.jar │

└───────────┬───────────┘

│

▼

┌───────────────────────┐

│ Burp Suite │

│ │

│ Proxy → :8082 │

│ HTTP History │

└───────────┬───────────┘

│

▼

Target Application

git clone https://github.com/elementalsouls/Claude-BugHunter.git

cd Claude-BugHunter

bash scripts/install.sh

cd ..

git clone https://github.com/PortSwigger/mcp-server.git

cd mcp-server

sudo apt update

sudo apt install openjdk-21-jdk

sudo update-alternatives --config java

sudo update-alternatives --config javac

echo 'export JAVA\_HOME=/usr/lib/jvm/java-21-openjdk-amd64' >> \~/.zshrc

echo 'export PATH=$JAVA\_HOME/bin:$PATH' >> \~/.zshrc

source \~/.zshrc

java -version

javac -version

echo $JAVA\_HOME

./gradlew --version

mkdir -p \~/.config/opencode

nano \~/.config/opencode/opencode.json

Java 21

↓

Gradle

↓

MCP Server

burp-mcp-all.jar

↓

Burp Suite

mcp-proxy-all.jar

↓

OpenCode

8082 → Burp HTTP Proxy

9876 → Burp MCP Server

Claude-BugHunter

+

OpenCode

+

MCP Proxy

+

Burp MCP

+

Burp Suite

↓

HTTP History

↓

Security Analysis

***Lab / Authorization Note:*** *Use the Agent and Burp only against applications and systems you are authorized to test, such as your own labs or Bug Bounty programs whose scope permits the activity.*
