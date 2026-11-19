# I found RCE on Viber.

- **Source URL:** https://medium.com/@deadoverflow/i-found-rce-on-viber-432cf9e17eb0?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20240817102545/https://medium.com/@deadoverflow/i-found-rce-on-viber-432cf9e17eb0
- **Fetched:** 2026-11-19
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/6869 (id 6869)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# I found RCE on Viber.

Before I even start, please subscribe to my youtube channel, as initially I’m a YouTuber, however my channel got striked because I upload literal hacking content. So please support me as I tend to teach my viewers a lot about security in general. My channel is [https://youtube.com/@deadoverlofw](https://youtu.be/Pda0f9YUI30?si=tETS0UMkxqkikgLG)

# I found RCE on Viber

To be fair, it is debatable if even this is an RCE, however here is what we need to know about this.

I watched John Hammond’s video regarding WhatsApp arbitrary code execution, and just decided to test that for Viber. So I simply loaded Viber and made a “malicious” .pyw file.

Then just dragged and dropped it into viber.

And if you click on this file you will see that it executes.

Now an attacker can send this file to someone who has python installed on their computer and could potentially execute some malicious code on victims machine.

Now this is not really a vulnerability since viber isn’t executing these files itself, viber just tries to open this file which causes windows to run it as a regular python program. Please spread awareness about this as Telegram, WhatsApp and now Viber are all falling in the same pit of being “vulnerable” to this issue.

# What can you do?

Your best option is not to open any files which could be malicious because as of now we only know that py files can be executed. However there could be more to discover. So please make sure to be careful when opening files on any of these platforms, especially .pyw files or .pyz files. Do not open those.
