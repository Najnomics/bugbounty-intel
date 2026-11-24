# HackTheBox — Web Attacks

- **Source URL:** https://medium.com/@harry.hphu/hackthebox-web-attacks-error-based-xxe-to-exfiltrate-data-3f577eef18c7?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20240105162343/https://medium.com/@harry.hphu/hackthebox-web-attacks-error-based-xxe-to-exfiltrate-data-3f577eef18c7
- **Fetched:** 2026-11-24
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/4553 (id 4553)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
From my previous blog post, [HackTheBox — Web Attacks: From XXE Injection to Advanced Local File Disclosure](/@harry.hphu/hackthebox-web-attacks-from-xxe-injection-to-advanced-local-file-disclosure-64d1bf5acdca), I went over a technique to disclose sensitive information on the front end of the web applications. However, in a lot of cases, web applications don’t display anything on the front end. Hence, even if we retrieve the file, its content won’t be displayed anywhere on the application.

What we can do is check to see if the application displays any errors if XML form is broken. If yes, we can take advantage of the error messages to disclose information.

Now that we’ve confirmed the application displays errors, we can use similar techniques to exfiltrate contents of files from the target.

First we host a `error-based-xxe.dtd` file on the attacking machine

In the `error-based-xxe.dtd` file, we first define `file` entity which requests the `/etc/passwd` file. This entity is then joined with a non-existing entity, `%nonExistingEntity;` , which will yield errors.

Now, inject the payload to the application. The payload consists of an entity called `%remote`, which references to the `error-based-xxe.dtd` file on the attacking machine. Send the request and we will get error messages, together with the content of the flag.

*HTB{3rr0r5\_c4n\_l34k\_d474}*

**Note:** this attack is not reliable because we use `file://` to retrieve the file, which does not always work, or due to length limitations. On top of that, if the file has special characters, it will break the application.
