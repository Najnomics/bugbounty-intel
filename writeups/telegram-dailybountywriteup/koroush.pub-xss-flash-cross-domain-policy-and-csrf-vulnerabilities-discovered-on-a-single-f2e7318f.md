# XSS, Flash Cross-Domain Policy, and CSRF Vulnerabilities Discovered on a Single Website

- **Source URL:** https://medium.com/@koroush.pub/xss-flash-cross-domain-policy-and-csrf-vulnerabilities-discovered-on-a-single-website-4948dff4ec11?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20230311162200/https://medium.com/@koroush.pub/xss-flash-cross-domain-policy-and-csrf-vulnerabilities-discovered-on-a-single-website-4948dff4ec11?source=rss------bug_bounty-5
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/1537 (id 1537)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# XSS, Flash Cross-Domain Policy, and CSRF Vulnerabilities Discovered on a Single Website

Hello everyone, my name is Koroush, (aka whiteOwl). 

In this write-up, I will be discussing the methods I used to bypass the site’s input sanitization process for cross-site scripting (XSS) vulnerabilities, as well as identifying a misconfiguration flaw in the Flash cross-domain policy and cross-site request forgery (CSRF) protection.

I was thinking to buy a Nintendo Switch console and for that, I was searching on google for different sites and checking prices in this process, one of the sites caught my attention.

when I searched helloxss in the search bar of this particular site the helloxss word was reflected in the title bar, URL, and in the site’s body.

it attracts my attention and I decided to play around with the site search bar. when i tested it with simple xss payloads like

\`\<img src=1 onerror=alert(1)>\`

these attempts did not result in any successful execution of the payload.(what else could I except?)

I checked several XSS and polyglots with no success. then use the xss’or app (if u don’t know what is this utility, check this \[github\]([https://github.com/evilcos/xssor2](https://web.archive.org/web/20230311162200/https://github.com/evilcos/xssor2)) page) xss’or has diffrent modules for encoding XSS payloads and it has useful XSS payloads dictionary and other utilities, I used escape module on:

\`ps5ps4psp\<script>alert(1)\</script>nintedo\`

and entered this payload in the search bar and guess what BOOM! 

it bypasses website sanitize entry process and caused my payload to run successfully.

I searched for other bugs for a little while and with help of good old burp I found another bug called Flash cross-domain policy 

(never heard of it tho!) but with a little search, I understand the concept and impact of it(The Flash cross-domain policy controls whether Flash client components running on other domains can perform two-way interaction with the domain that publishes the policy. If another domain is allowed by the policy, then that domain can potentially attack users of the application. 

If a user is logged in to the application and visits a domain allowed by the policy, then any malicious content running on that domain can potentially gain full access to the application within the security context of the logged-in user.)

During my analysis of the account details changing functionality, I noticed that the website did not have any protection against cross-site request forgery (CSRF) attacks. As proof-of-concept, I created a new account and logged into it in a private browser tab. I then used Burp Suite to intercept the request for changing all fields, and created a CSRF exploit, I utilized a tool like ngrok to host my exploit page and ran it in the main browser. Upon executing the exploit, I was able to successfully change the account details of the main account to match the details of my newly created account.

After successfully exploiting the vulnerability, I received a violation notification from ngrok for using their service to host malicious content. However, discovering and reporting this bug was a valuable learning experience. I hope that sharing my process and the techniques used will be informative and educational for others. Thanks for reading, and I look forward to sharing more findings in the future.
