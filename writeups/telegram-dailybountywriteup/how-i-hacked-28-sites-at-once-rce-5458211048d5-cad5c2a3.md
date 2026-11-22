# How I hacked 28 sites at once [RCE]

- **Source URL:** https://al1z4deh.medium.com/how-i-hacked-28-sites-at-once-rce-5458211048d5?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20260718060012/https://al1z4deh.medium.com/how-i-hacked-28-sites-at-once-rce-5458211048d5
- **Fetched:** 2026-11-22
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/2207 (id 2207)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# How I hacked 28 sites at once \[RCE\]

**Attention: My purpose in sharing this post is for your learning and attention only. If your company, organization, or site has been exposed to this vulnerability, I suggest you report it.**

Hello,

I will tell you how I found RCE on a site I came across while searching for exploit while preparing for OSCP. When I entered the site, I saw that it was built on a VPS, and I could access 28 websites from here. So there were 28 victims because of a mistake. While testing, I found that I could make changes to other sites. Now let’s move on to how I found it.

A feature in Symfony, a popular open source framework for building PHP applications, could expose websites to remote code execution (RCE) if configured improperly, a security researcher has found.

Attackers could exploit the feature, which allows browsers to download fragments of web pages, to run arbitrary commands on the Symfony server.

Symfony servers support a “/\_fragment” command that allows clients to provide custom PHP commands and return the HTML output. To prevent misuse, Symfony requires requesters to sign their messages with a cryptographic key stored on the server.

Reference link:

- Step 1

I first came across the site while searching the internet for “\_fragment”.

- Step 2

When I looked at the site, I came across “403 forbidden”. I am convinced once again that there is abuse here.

- Step 3

I started using an exploit code I found on Github.

Exploitation took place here. Let’s go to the link shown.

POC

- Step 4

Now let’s use the “system” function and enter the command to use it as rce.

Here is the result.

And looking at the “/etc/hosts” file:

I also checked other sites, and they were successful. More than 50 sites I’ve discovered are currently affected by this vulnerability. I wrote this in everyone’s mail and added it to the link for the POC.

“Thank you for reading. I hope that will be useful.If you have any questions or comments, please do not hesitate to write. Have a good days”
