# JWT Privilege Escalation to Container RCE via Jinja2 SSTI “ Intigriti challenge”

- **Source URL:** https://medium.com/@banertheinrich/jwt-privilege-escalation-to-container-rce-via-jinja2-ssti-intigriti-challenge-16186324241c?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20251222134807/https://medium.com/@banertheinrich/jwt-privilege-escalation-to-container-rce-via-jinja2-ssti-intigriti-challenge-16186324241c?source=rss------bug_bounty-5
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/11862 (id 11862)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# JWT Privilege Escalation to Container RCE via Jinja2 SSTI “ Intigriti challenge”

The application is a Flask-based e-commerce platform running inside a Docker container. The attack chain combines a JWT role forgery vulnerability with a high-impact Server-Side Template Injection (SSTI) in the “Change Display Name” feature, ultimately leading to unrestricted remote code execution as the application user.

1. Initial Access & JWT Role Forgery

The registration endpoint creates regular user accounts and immediately returns a signed JWT (HS256).

Decoding the token revealed a predictable payload containing user\_id, username, and role.

Although the server did not support the “none” algorithm, the application trusted the role claim without any secondary verification server-side.

Using Burp Suite’s JWT Editor extension, the payload was modified from:

JSON

{“user\_id”:9,”username”:”adham”,”role”:”user”}

to

JSON

{“user\_id”:1,”username”:”admin”,”role”:”admin”

After re-signing the token with the non algorithm, the application accepted it and granted full administrative privileges.

2\. SSTI Discovery in “Change Display Name”

The admin panel allowed changing the display name, which was directly rendered using Jinja2 templating without proper sanitization.

Basic test ${{7\*7}} rendered as $49, confirming Jinja2 SSTI (the $ prefix is characteristic of this challenge’s rendering behavior).

3\. Bypassing Heavy Blacklists

Classic payload chains like ‘’.class.mro\[1\].subclasses() returned empty or heavily filtered results, indicating aggressive attribute/class blacklisting.

However, the config object and its \_\_init\_\_.\_\_globals\_\_ attribute were not filtered at all.

This gave direct access to Python builtins:

{{ config.\_\_class\_\_.\_\_init\_\_.\_\_globals\_\_\[‘\_\_builtins\_\_’\] }}

4\. Achieving Remote Code Execution

With \_\_builtins\_\_ exposed, arbitrary command execution became trivial:

jinja

{{ config.\_\_class\_\_.\_\_init\_\_.\_\_globals\_\_\[‘\_\_builtins\_\_’\].eval(“\_\_import\_\_(‘os’).popen(‘id’).read()”) }}

Confirmed execution as appuser inside the container.

Further commands allowed full directory traversal, source code inspection, and sensitive file disclosure.

.

Last thing , I searched the word “ intigriti “ to get the flag , I got it !
