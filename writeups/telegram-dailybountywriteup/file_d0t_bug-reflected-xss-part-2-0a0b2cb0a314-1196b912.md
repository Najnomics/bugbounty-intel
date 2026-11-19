# Reflected XSS — Part 2

- **Source URL:** https://medium.com/@file_d0t_bug/reflected-xss-part-2-0a0b2cb0a314?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20251127192452/https://medium.com/@file_d0t_bug/reflected-xss-part-2-0a0b2cb0a314
- **Fetched:** 2026-11-19
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/11146 (id 11146)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Reflected XSS — Part 2

## بسم الله الرحمن الرحيم و الصلاة و السلام على أشرف الأنبياء و المرسلين

**Introduction 📝**

Hey I am Ruba Khaled *(file.bug)* ,I found a **reflected XSS** in a public bug bounty program inside a password-reset page. 

This is part 2 of my XSS journey — read part 1 here:

**Recon tip — subdomain enumeration 🕵️♀️**

Before diving in: for subdomain enumeration I often use this website because it returns unique results that some scanners and Google dorks miss:

**How I discover Reflected xss bug? Any tool ? ⚒️**

I prefer manual hunting over blindly running tools. I test each parameter manually, and only when I can’t find anything I run a parameter-fuzzing tool. One tool I use is **Arjun** (I run it with the default wordlist):

`arjun -u http://example.com`
for Installation details 📥:

**The bug 🐞**

I’ll call the target *target.com* because the issue is still open.

While testing *target.com*, I checked the password reset flow. I entered my email and received the usual password-reset email:

I followed the link and inspected the page source.

**Token parameter 🔐**

I changed the token value to see whether it was reflected in the page source. It was reflected inside an HTML attribute, but only alphabetical characters appeared; the double quote " (which would close the attribute value) was blocked.

**Email parameter 📧**

Next I checked the email parameter. My email is also reflected in the page source.

I tested injecting a value with a quote:

jjjjjjjjj"

The double quote " was **reflected successfully** inside a \<script> tag.

Since the injection point was inside a \<script> block, I didn’t need to inject a new \<script> tag — I could close strings and break the existing JavaScript context.

**Payload and How it works 🧩**

I used this simple payload:

`");alert('XSS')//` How it works:

• ") — closes the open string and the open parenthesis in the existing JS.

• ; — ends the current statement.

• alert('XSS') — shows a popup to demonstrate code execution (you can run any JS).

• // — comments out the rest of the original line to avoid syntax errors.

Because the email parameter was inserted directly into a script block without proper encoding, the payload executed successfully.

**The end 🎬**

Thanks for reading! If you enjoyed this, please clap 👏🏼👏🏼👏🏼 and follow for more bug-bounty write-ups — maybe there will be a Part 3 of my XSS journey !

Contact: [file\_d0t\_bug](https://x.com/file_d0t_bug) on X (Twitter) 🐦
