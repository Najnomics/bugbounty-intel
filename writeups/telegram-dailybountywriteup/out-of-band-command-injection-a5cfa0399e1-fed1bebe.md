# Out Of Band Command Injection

- **Source URL:** https://roadtooscp.medium.com/out-of-band-command-injection-a5cfa0399e1?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20230102192934/https://roadtooscp.medium.com/out-of-band-command-injection-a5cfa0399e1
- **Fetched:** 2026-11-27
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/1203 (id 1203)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Out Of Band Command Injection

Command Injection or OS Command Injection is a kind of injection vulnerabilities, where an attacker is able to exploit an unsanitized user input further to run system level commands in the server, which may lead to complete takeover of Vulnerable application server.

**Before delving deep into the injection technique lets look at the anatomy of command injection**

Think about an application which uses system level command to produce a output for user. something like given as below, where websites helps to resolve different kind network based resolution like mx records ,dns lookup etc.

Since the above website doesn’t authorize you to pentest so I had to create a demo website(Below) to demonstrate the same

it is quite obvious that above website will use some system level commands to produce the output as required. So inherently this website is designed to use any system command for functionality.

**Scenarios where we can find Command injections:**

A command injection attack can happen due to various types of vulnerabilities.

Here are some common ones:

- **Arbitrary command injections**: applications that allow a malicious user to run arbitrary commands rather than desired
- Insecure Deserialization-Serialization: executing deserialization without performing proper input validation can lead to command injections
- XXE injection: if an application uses an XML parser that hasn’t been configured properly to parse user XML input then that can be leveraged to execute command injection
- Insecure file upload: applications that allow users to upload files with arbitrary files extensions can be vulnerable to command injections through malicious commands when inserting into the webroot
- SSTI: applications that use server-side templates to generate dynamic HTML responses may be vulnerable to the insertion of harmful server-side templates if unsafe user-supplied data is included in a template

# How one can detect OS command injection attacks

There are many ways to detect command injection attacks. One way is to look at the request parameters and see whether there are any suspicious strings. Another method is to examine the response body and see whether there are unexpected results.

One may also use plugin like Shelling which is indeed a great tool to locate the Command injection in a web app

**Demo Time**

Exploiting a scenario with an out of band data filtration technique:

Thanks for reading!!!

See you next time !!
