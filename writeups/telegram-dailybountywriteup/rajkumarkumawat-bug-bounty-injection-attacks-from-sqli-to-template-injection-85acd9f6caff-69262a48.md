# Bug Bounty

- **Source URL:** https://medium.com/@rajkumarkumawat/bug-bounty-injection-attacks-from-sqli-to-template-injection-85acd9f6caff?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250905081921/https://medium.com/@rajkumarkumawat/bug-bounty-injection-attacks-from-sqli-to-template-injection-85acd9f6caff?source=rss------bug_bounty-5
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/10536 (id 10536)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Bug Bounty: Injection Attacks — From SQLi to Template Injection

Injection attacks have haunted web applications for decades. From classic SQL Injections (SQLi) to modern-day Server-Side Template Injections (SSTI), these flaws offer attackers direct paths to data breaches, shell access, and full compromise. In this blog, we’ll explore the full spectrum of injection vulnerabilities, how they work, how to exploit them, and most importantly, how to defend against them.

## 📊 Understanding Injection Attacks

Injection vulnerabilities occur when untrusted input is sent to an interpreter as part of a command or query. Attackers exploit this to trick the interpreter into executing unintended commands.

**Common Types of Injections:**

- **SQL Injection (SQLi)**
- **Command Injection**
- **LDAP Injection**
- **XML Injection**
- **Server-Side Template Injection (SSTI)**
- **NoSQL Injection**

Each type targets a different backend component, but the root cause remains: **failure to validate and sanitize user input.**

## 🔹 SQL Injection (SQLi)

## ✈ What Is It?

SQLi targets database queries through unsanitized inputs. If inputs are interpolated directly into SQL queries, attackers can manipulate them.

## 👨🔧 Example Payloads

```
' OR 1=1 --
admin' --
1'; DROP TABLE users; --
```
## 🧪 Tools for SQLi

- **sqlmap** (automated SQLi tool)
- **Burp Suite**
- **SQLite3 CLI**

## 🎓 Labs

## 🔹 Command Injection

## ✈ What Is It?

Occurs when input is injected into OS-level commands.

## 👨🔧 Payload Examples

```
127.0.0.1; whoami
127.0.0.1 && id
127.0.0.1 || cat /etc/passwd
```
## 🧪 Tools

- Burp Suite
- Netcat
- Gobuster for endpoint fuzzing

## 🎓 Labs

## 🔹 Server-Side Template Injection (SSTI)

## ✈ What Is It?

Template engines like Jinja2, Twig, and Handlebars may allow input to be interpreted as code.

## 👨🔧 Payloads

```
{{7*7}}
{{config}}
{{ ''.__class__.__mro__[1].__subclasses__() }}
```
## 🧪 Tools

- tplmap
- SSTImap
- Burp Repeater + Intruder

## 🎓 Labs

## 🔹 NoSQL Injection

## ✈ What Is It?

Targets NoSQL databases like MongoDB using JSON-style injection.

## 👨🔧 Payloads

`{"username": {"$ne": null}, "password": {"$ne": null}}`
## 🧪 Tools

- NoSQLMap
- MongoDB CLI
- Burp Suite

## 🎓 Labs

## 🔧 Defensive Strategies

## ❌ Never Trust User Input

Always validate input on both the client and server sides.

## ✅ Use Prepared Statements (Parametrized Queries)

For SQL:

`cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))`
## 🛡️ Web Application Firewalls

Use WAFs to detect and block basic injection attempts.

## ⚙ Framework-Level Protections

- Django ORM, Laravel Eloquent, and Mongoose help prevent injections
- Use built-in sanitization filters for templates

## 🔍 Real-World Exploits

- **SQLi in TalkTalk (2015)**: Led to the breach of 150,000+ customers.
- **Command Injection in GitLab (CVE-2021–22205)**
- **SSTI in Flask apps (Jinja2)**: Often used for RCE payloads

## 🔖 Final Words

Injection vulnerabilities continue to top the OWASP Top 10 due to their devastating impact and simple exploitation. From SQLi to SSTI, mastering these flaws is a must for ethical hackers and defenders alike.

**Stay curious, stay ethical, and always sanitize!**
