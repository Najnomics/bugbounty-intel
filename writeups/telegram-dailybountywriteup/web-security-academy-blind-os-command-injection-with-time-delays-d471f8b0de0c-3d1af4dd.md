# Web Security Academy — Blind OS command injection with time delays

- **Source URL:** https://r4bb1t.medium.com/web-security-academy-blind-os-command-injection-with-time-delays-d471f8b0de0c?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20221111002130/https://r4bb1t.medium.com/web-security-academy-blind-os-command-injection-with-time-delays-d471f8b0de0c
- **Fetched:** 2026-11-27
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/735 (id 735)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
## Web Security Academy

# Blind OS command injection with time delays

This lab is part of the Web Security Academy by Portswigger. It is under the category “OS command injection”. This time we have to exploit a blind command injection vulnerability. When opening the web page, we see a web shop with some item.

But this time, the web shop has a “Submit feedback” form. When opening that form, we are redirected to a form, where we can submit a name, email, subject and message.

I thought about, that this form is using a bash command to save the data. Something like `echo "data" > file.txt` . So I injected the following payload into the “Name” input field: `test" && sleep 10 #` .

This payload worked and I was able to complete the challenge.

# Mitigation

Instead of using OS commands to save the data, use programming specific functions. Every programming language has functions to interact with the file system, without using OS commands. Also escape or filter command joining symbols, such as `&&` , `||` etc.
