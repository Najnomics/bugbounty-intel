# Web Cache Poisoning

- **Source URL:** https://medium.com/@bughunt.bochi/web-cache-poisoning-turning-speed-into-a-security-nightmare-b2cde92e1036?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20251126140236/https://medium.com/@bughunt.bochi/web-cache-poisoning-turning-speed-into-a-security-nightmare-b2cde92e1036
- **Fetched:** 2026-11-19
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/8492 (id 8492)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Web Cache Poisoning: Turning Speed into a Security Nightmare

whoami *¯\\\_(ツ)\_/¯*


Hello, fellow bug hunters and cybersecurity geeks! I’m Yash Nimbalkar. Currently pursuing my Master’s degree in Cyber Security, I spend my time sometimes poking around platforms to see if they’ve left any digital doors open.

Today we will be discussing about **Web Cache Posioning**. Let’s dive into it!

## What is Web Cache Poisoning?

Web cache poisoning occurs when an attacker manipulates a server’s caching mechanism to store and serve malicious content. Since the cache serves this content to all users accessing the site, the impact can range from defacement and phishing to malware propagation. It’s a clever yet dangerous technique that leverages an optimization feature against itself.

You can imagine web cache poisoning is like sneaking a fake ingredient into the soup that gets served to everyone. It turns a helpful optimization into a dangerous delivery mechanism for malicious content. What’s more, once the soup is poisoned, everyone’s having a *bad day.*

## Vulnerability Summary

The caching mechanism on `target.com` was susceptible to manipulation, allowing an attacker to inject malicious content into the cache. Once poisoned, the cache served this altered response to unsuspecting users, creating opportunities for:

- **Phishing**: Redirecting users to malicious sites.
- **XSS Attacks**: Executing scripts in the victim’s browser.
- **Defacement**: Displaying altered or offensive content.

## Steps to Exploit

Here’s how I was able to exploit the vulnerability:

**1.Prepare the Setup**

- Navigate to `target.com`.
- Clear all cookies and refresh the page while capturing the HTTP request using Burp Suite.
- If you see *Cache: HIT* or *Cache: MISS (or anything similar),* in the response, then you can try out the next steps.
- Also, do check if there is a Max-Age: xx in the response as this parameter decides how much time the cache will be stored in the server.

**2. Observe Cache Behavior**

- Send the captured request to Burp’s Repeater tool.
- Notice that the cache refreshes approximately every few seconds/minutes, depending on the configuration.
- While testing for Web Cache Poisoning, do remember to use cache buster (targeturl/?cb=123), so that you won’t mess with the actual site.

**3. Inject Malicious Content**

- In Burp Collaborator, copy the payload URL.
- Add the header `X-Forwarded-Host: [Collaborator URL]` to the HTTP request in Repeater.
- Send the modified request to the server.

**4. Cache Poisoning in Action**

- Wait for the cache to refresh.
- Clear cookies in the browser and reload the page.
- The browser now displays the poisoned cache response containing the collaborator URL or malicious payload.

In my case, whatever I injected in the header `X-Forwarded-Host:` was being reflected in the site response.

Similarly, you can see if whatever you inject in the headers does get reflected in the response or not. By analyzing the response, you can then decide what you want to do like: *phishing, XSS or defacement of website*.

## Severity: High

Given the potential for widespread impact and the ease with which the cache could be poisoned, this vulnerability was rated **High** severity.

## Lessons Learned: Cache Wisely

1. **Don’t Let Headers Run Wild**
Make sure headers like`X-Forwarded-Host` are validated, or you might just be giving attackers the keys to your cache pantry.
2. **Limit Cache Lifespan**
Shorter cache durations mean less time for malicious content to brew. You wouldn’t leave milk on the counter for 13 minutes, so why let your cache sit that long?
3. **Segregate User-Specific Content**
Mixing user-specific responses in a cache is like serving peanut butter to someone with allergies — not ideal.

Web cache poisoning is one of the most fascinating bugs I encounter. It highlights how critical it is to thoroughly test optimization features like caching for potential abuse.

I’m always eager to learn and grow in the field of cybersecurity. If you’d like to collaborate or discuss vulnerabilities, let’s connect:

Together, we can make the web a safer place, one vulnerability at a time. 🚀

Good Luck! Happy Hunting!
