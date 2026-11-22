# Server Side Template Injection (SSTI) -By CTRL

- **Source URL:** https://medium.com/@CTRL2030/server-side-template-injection-ssti-by-ctrl-6d6a59a9fedb?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20251126172844/https://medium.com/@CTRL2030/server-side-template-injection-ssti-by-ctrl-6d6a59a9fedb
- **Fetched:** 2026-11-22
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/3410 (id 3410)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Server Side Template Injection (SSTI) -By CTRL

السلام عليكم ورحمة الله وبركاته

## **What is SSTI?**

Server-side template injection is a vulnerability where the attacker [injects malicious input](https://cobalt.io/vulnerability-wiki/v10-malicious) into a template to execute commands on the server-side. This vulnerability occurs when invalid user input is embedded into the template engine which can generally lead to remote code execution (RCE).

Template engines are designed to combine templates with a data model to produce result documents which helps populating dynamic data into web pages. Template engines can be used to display information about users, products etc. Some of the most popular template engines can be listed as the followings:

- PHP–Smarty,Twigs
- JAVA–Velocity,Freemaker
- Python–JINJA,Mako,Tornado • JavaScript–Jade,Rage
- Ruby-Liquid

## How Does It Work?

I will explain on a real example of a vulnerability SSTI

**Proof of Concept :**

Step 1: A simple example to prove a vulnerability SSTI use payload : {{20\*20}} and {{9000000000000+1}}

Step 2: Can see results SSTI payloads

## What’s the Impact of SSTI?

The impact of server-side template injection vulnerabilities is generally critical, resulting in remote code execution by taking full control of the back-end server. Even without the code execution, the attacker may be able to read sensitive data on the server. There are also rare cases where an SSTI vulnerability is not critical, depending on the template engine.

## Remediation

Remediations for the [SSTI vulnerability](https://cobalt.io/vulnerability-wiki/v5-validation-sanitization/ssti) depend on the different template engines in use. There are 2 common suggestions to remediate this vulnerability:

- Sanitization: Sanitize user input before passing it into the templates to minimize vulnerabilities from any malicious.
- Sandboxing: In case using risky characters is a business need, it is recommended to use a sandbox within a safe environment.

**Resources** :
