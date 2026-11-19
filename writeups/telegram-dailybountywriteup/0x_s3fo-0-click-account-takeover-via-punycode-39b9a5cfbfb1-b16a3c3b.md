# 0-click Account Takeover via Punycode

- **Source URL:** https://medium.com/@0x_s3fo/0-click-account-takeover-via-punycode-39b9a5cfbfb1?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20251019194119/https://medium.com/@0x_s3fo/0-click-account-takeover-via-punycode-39b9a5cfbfb1
- **Fetched:** 2026-11-19
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/11220 (id 11220)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# 0-click Account Takeover via Punycode

بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيمِ

اللَّهُمَّ صَلِّ وَسَلِّمْ وَبَارِكْ عَلَى سَيِّدِنَا مُحَمَّدٍ

Hi, I’m **Saif Eldin**. I’m a security researcher and bug bounty hunter who enjoys finding real-world vulnerabilities.

### **On the First: What’s Punycode and How It Can Break Authentication?**

Before explaining the attack, let’s understand how the Internet actually reads domain names and emails.

The Internet’s **DNS system** only understands basic English characters, what’s called **ASCII** (letters`a-z`, numbers, and a few symbols).

But today, people all over the world use **Unicode,** a much bigger set of characters that includes every language and accent (like `à`, `ö`, `é`, or even Arabic and Chinese).

So what happens if you try to register a domain that contains one of these special letters?

That’s where **IDNs** (Internationalized Domain Names) come in. An IDN is simply a domain that includes Unicode characters, such as:

```
tàrget.com
café.com
mỳsite.com
```
However, since **DNS can’t read Unicode directly**, the browser converts it into a special ASCII-compatible format called **Punycode,** a version that starts with `xn--`.

For example:

`tàrget.com` → `xn--trget-rqa.com`

`café.com` → `xn--caf-dma.com`

Now here’s the problem: **many Unicode characters look identical to normal ASCII ones.**

For example, `a` and `à` look almost the same to the human eye, but technically, they’re different characters.

### **Why did This Attack happen?**

The attack happens when the website or its database accidentally treats two different email strings as the same value, for example, when MySQL (or some app logic) performs a cast. In that case, the system sees the regular ASCII email and the Punycode version as identical, and that mix-up is exactly what the attacker takes advantage of.

Example:

- `saif@target.com`
- `saif@tàrget.com`

If you register with `saif@target.com` and later try to register `saif@tàrget.com`, and the site replies **“User with this email already exists.”** That’s a strong indicator that the app or database is casting those addresses to the same value. When that happens, a password-reset or invite request using the attacker-controlled Punycode address can end up affecting the real `saif@target.com` account, which is exactly how a 0-click takeover can occur.

### Now, let’s dive into the attack

**Steps To Reproduce:**

1- Register a normal ASCII email account, for example, [saif@adrixa.com](mailto:saif@adrixa.com)

2- I tried to invite the Punycode email[saif@adrixà.com](mailto:saif@adrix%C3%A0.com)

3- Go to `https://` and submit [target.com/reset-password](http://piwiksandbox.com/reset-password)[saif@adrixà.com](mailto:saif@adrix%C3%A0.com)

4- The system sends a reset link to [saif@adrixà.com](mailto:saif@adrix%C3%A0.com)

6- Log in using the original ASCII email [saif@adrixa.com](mailto:saif@adrixa.com)

I reported the issue responsibly to the security team with PoC steps, screenshots. They confirmed the bug, classified it as **Critical**

**Follow Me**
