# Hacking CSRF

- **Source URL:** https://infosecwriteups.com/hacking-csrf-bypass-same-site-cookie-restriction-14f01342dd30?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250506014345/https://infosecwriteups.com/hacking-csrf-bypass-same-site-cookie-restriction-14f01342dd30
- **Fetched:** 2026-11-24
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/3084 (id 3084)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Hacking CSRF: Bypass Same Site Cookie Restriction

## Bypass CSRF Protection technique

Hey, Guys welcome to my blog so today we are going to discuss about bypassing CSRF the Same Site cookie Protection. it is a critical topic but I will explain it simply with multiple parts to bypass this you need some basic understanding of TLD, Origin, and major same-site protection attribute

## What is Same-Site Protection?

Same-Site protection is a security mechanism implemented by web browsers to control how cookies are sent in cross-site requests. It allows website owners to specify whether a cookie should be included in requests initiated from a different site or origin

Before the implementation of the Same site restriction, the browser will send the cookie with every request even though the request is generated from a third-party unrelated origin or website

And this may induce a variety of cross-domain attacks like CSRF so to protect from this same site restriction is come into scope but it still bypassable with some technique

Chrome automatically includes the LAX attribute same site protection as the default so don’t test the CSRF in Chrome uses Firefox but I don’t in the future firefox will also update

## TLD ( Top Level Domain )

TLD is nothing but top-level domains like .com, .org

But there are many types

Generic top-level domains (gTLDs): These are general-purpose domains that are not associated with any specific country or geographic location. Examples include “.com,” “.org,” “.net,” “.info,” and many more. There are also more specific gTLDs like “.edu” (education), “.gov” (government), “.mil” (military), and “.int” (international organizations).

Country codes top-level domains (ccTLDs): These are two-letter domains reserved for specific countries or territories. Examples include “.us” (United States), “.uk” (United Kingdom), “.de” (Germany), “.jp” (Japan), and so on. Each country has its own unique ccTLD.

Sponsored top-level domains (sTLDs): These are specialized domain extensions sponsored by specific organizations or interest groups. They have specific eligibility requirements and are often tied to particular industries or communities. Examples include “.gov” (U.S. government), “.edu” (educational institutions), “.aero” (aviation industry), and “.museum” (museums).

New generic top-level domains (new gTLDs): These are additional TLDs introduced in recent years to expand the domain namespace and provide more specific or industry-focused options. Examples include “.photography,” “.travel,” “.app,” “.xyz,” and numerous others. These new gTLDs offer more choices for domain name registration.

But it is not necessary just to know what is TLD

## What is Origin?

Origin refers to the combination of protocol or scheme, domain, and port

You get a clear idea in the below table

Let me explain one from this table the request from [https://evil.com](https://evil.com) → Now the request goes to [http://evil.com](http://evil.com) it is wrong because it is a different port and it has different origins

https → 443 and http → 80

Actually, the request goes to the origin of [https://evil.com](https://evil.com)

Now let’s discuss how the same site restriction works.

## How does the same site restriction work?

The browser currently supports the three attribute

1. Strict
2. Lax
3. None

## Strict

SameSite=Strict

When the SameSite attribute is set to “Strict” in a cookie’s attribute list, it means that the cookie should only be sent in requests initiated from the same origin (i.e., same combination of protocol, domain, and port). The browser will not include the cookie in cross-site requests, even if the request originates from a different page on the same site.

By using the SameSite=Strict attribute, website owners can enforce a strict same-origin policy for cookies, enhancing security and protecting against certain types of attacks, such as CSRF (Cross-Site Request Forgery). This attribute helps prevent the cookie from being accessed by third-party websites and ensures that it is only used in requests made within the same origin.

It is most secure for CSRF but user experience will get affected

## Lax

SameSite=Lax

When the SameSite attribute is set to “Lax” in a cookie’s attribute list, it means that the cookie should not be sent in cross-site requests that are initiated by third-party websites. However, the cookie will still be included in top-level navigations, which are requests that come from the same site or origin.

The Lax value provides a balance between security and functionality. It allows cookies to be used more restrictedly, reducing the risk of certain attacks like CSRF (Cross-Site Request Forgery) while still allowing common user interactions within the same site.

## None

SameSite=None

When the SameSite attribute is set to “None” in a cookie’s attribute list, it means that the cookie can be sent in cross-site requests, including those initiated by third-party websites. However, there are additional requirements for using SameSite=None.

To use SameSite=None, the cookie must include the “Secure” attribute. This indicates that the cookie should only be sent over a secure (HTTPS) connection. The combination of SameSite=None and Secure ensures that the cookie is only sent in cross-site requests when the connection is secure.

Setting SameSite=None is useful when cookies are required for cross-origin functionality or third-party integrations. It allows for the exchange of cookies between different sites while still enforcing the requirement of a secure connection.

So I hope you will understand this article if you like this please give the applause and follow up my blog for more updates

Donate to Me: [https://www.buymeacoffee.com/0xevilox](https://www.buymeacoffee.com/0xevilox)
