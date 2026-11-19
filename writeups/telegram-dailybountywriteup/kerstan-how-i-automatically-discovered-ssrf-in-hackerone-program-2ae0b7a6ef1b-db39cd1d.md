# How I Automatically Discovered SSRF in Hackerone Program

- **Source URL:** https://medium.com/@kerstan/how-i-automatically-discovered-ssrf-in-hackerone-program-2ae0b7a6ef1b?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20240105161745/https://medium.com/@kerstan/how-i-automatically-discovered-ssrf-in-hackerone-program-2ae0b7a6ef1b
- **Fetched:** 2026-11-19
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/4723 (id 4723)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
**Subscribed to:** [https://medium.com/@kerstan](/@kerstan)

Hi guys, I am Kerstan. Today, I will share you how I automatically discoverd SSRF on hackerone Program.

Finding a blind SSRF is relatively easy, but to earn more bounty, you need to exploit it and gain more access. It requires relentless effort. Try harder, bro!

If this writing has been helpful to you, please consider giving it a clap and following. Thanks bro.

So, let’s get started.

# 1. Download & Install

First, you need to download AutoRepeater from the following address. Once downloaded, go to the Extender interface of Burp and import AutoRepeater.jar.

# 2. Automatically Discovered SSRF

You need to do two preparatory steps:

1. You need a dnslog platform where you can view the logs, such as Burp’s Collaborator or ceye.io. You can also use other platforms.
2. You need to prepare the following two regular expressions.

```
(?i)^(https|http|file)://.*
(?i)^(https|http|file)%3A%2F%2F.*
```
Let’s explain the two regular expressions briefly:

The first regular expression ensures that unencoded URLs can be matched correctly.

The second regular expression ensures that encoded URLs can be matched correctly.

They are used to match URLs and replace them with dnslog addresses, and then automatically send the requests.

So, all we need to do is check if there is any data on the DNS log platform or test all the endpoints that carry URLs to determine if there is an SSRF vulnerability.

In my experience, any place that carries SSRF has the potential for an SSRF. It is recommended to test all of them.

Now, let’s configure the rules for AutoRepeater.

Once you have configured everything as mentioned above, you just need to click here to start waiting for dnslog data…
