# Weird LFI and escalating the impact from High to Critical

- **Source URL:** https://medium.com/@snoopy101/weird-lfi-and-escalating-the-impact-from-high-to-critical-3e804f5366e9?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20251126142735/https://medium.com/@snoopy101/weird-lfi-and-escalating-the-impact-from-high-to-critical-3e804f5366e9
- **Fetched:** 2026-11-24
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/3906 (id 3906)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Weird LFI and escalating the impact from High to Critical

Hey wonderful hackers. I was hacking on a VDP program and after a light recon I picked one subdomain to hunt.

I clicked around and used the website as intended but when I looked at the requests in burp, this request caught my eyes.

`https://target.tld/api/whitelabel/getFile?file=favico`
So I tested for LFI and tried to get the `/etc/passwd` file, but the response was empty. I tried all bypasses but no luck.

I tried endpoints from [Seclists](https://github.com/danielmiessler/SecLists/tree/master/Fuzzing/LFI) and I got these files:

```
https://target.tld/api/whitelabel/getFile?file=../../../../../../../../../../../../etc/hosts
https://target.tld/api/whitelabel/getFile?file=../../../../../../../../../../../../var/log/dmesg
https://target.tld/api/whitelabel/getFile?file=../../../../../../../../../../../../etc/ssh/ssh_host_dsa_key
https://target.tld/api/whitelabel/getFile?file=../../../../../../../../../../../../var/log/dpkg.log
```
### That's all. Nothing quite impactful.

Anyway this is an LFI and based on the **wrong** belief the impact is High, but I personally believe that the impact of LFI must be **Critical**.

Some examples of High impact LFIs:

### They did it on my report too:

I wanted to escalate this to **Critical**, so I had to find something, and It’s a little difficult by brute-forcing.

I fuzzed internal endpoints with special characters and unicodes and I found something interesting. The `*` character was returning a file in every directory. (I guess it was the first file. I still don’t know)

I sent this request:

`https://target.tld/api/whitelabel/getFile?file=../../../../../../../../../../../../../../../var/www/*`
I got Database credentials:

They were valid and I logged into the Database.

### Source code disclosure:

### ***Is it still “High” baby?***

Story is over here, but I found another thing about that `*` behavior.

It can be used like this too: `/etc/apache2/*SOME-STRING`

If that string matches part of the file name in that directory, it returns the file. Like these examples:

*I don’t know the reason still. Please tell me if you know. :)*

**Takeaway:**

- The impact of LFI vulnerability is definitely Critical.

*Reach me at:*

LinkedIn:

[https://www.linkedin.com/in/ali-imani-2a896a266/](https://www.linkedin.com/in/ali-imani-2a896a266/)

twitter:

[https://twitter.com/snoopy101101](https://twitter.com/snoopy101101)

Thanks for reading. Love y’all.
