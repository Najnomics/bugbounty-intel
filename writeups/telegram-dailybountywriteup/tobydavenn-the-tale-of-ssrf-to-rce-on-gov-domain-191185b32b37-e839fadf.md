# The Tale Of SSRF To RCE on .GOV Domain

- **Source URL:** https://medium.com/@tobydavenn/the-tale-of-ssrf-to-rce-on-gov-domain-191185b32b37?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20221211033509/https://medium.com/@tobydavenn/the-tale-of-ssrf-to-rce-on-gov-domain-191185b32b37?source=rss------bug_bounty-5
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/224 (id 224)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# The Tale Of SSRF To RCE on .GOV Domain

Welcome back, I hope everyone is well. Without further hesitation let’s dive into it!

What is SSRF? SSRF is Server Side Request Forgery. This is a high/critical vulnerability when demonstrated with impact. SSRF allows an attacker should the server be making the requests, to potentially request and access internal pages.

Often SSRF is not plain sailing and you will need to utilise a range of bypasses, such as IP address blacklists, url encoding on pages and DNS tampering, but for the case of this vulnerable, it was pretty straight forward.

**How did I find this vulnerability?**

Waybackurls

GAU

waybackurls >> GAU >> combined.txt

gospider | tee gospider.txt

gospider.txt >> combined.txt

Manually look through file for interesting endpoints. I came across an endpoint called “/proxy”. This was a blank page when loaded. Inspecting the source revealed a var parameter which i was able to add to the request, this parameter was used for requesting a URL.

adding this parameter to the endpoint and requesting my burpcollab link allowed me to received a HTTP request from the servers IP. Removing the BC link and added “https://127.0.0.1” and sending the request received no response, interesting. I modified the IP and sent https://127.1 and a 200 OK was received with the internal page rendered on the screen, this just showed a redirect URL. Nothing too interesting but it shows limited filtering on any URLs.

From here I tried the AWS internal IP 169.254.169.254/metadata and sure enough the metadata was displayed. We now have full access to AWS for the company and can look around to gather keys and other information.

I took the request and tried a file path — file:///etc/passwd and sure enough again this loaded. From here I could request the host file to get an understanding of the internal IP ranges. Making a note, I sent the request to burp repeater and scanned across the internal address space for any interesting pages on port 8080 or with the url /admin.

I had learnt form a portswigger lab about shellshock, which is an RCE vulnerability that can be exploited via the user agent, googling will show you the payload. I added this payload to my intruder request and re-scanned across the internal range. Sure enough I got a ping back confirming an internal host was vulnerable. We now have full internal access and Remote Code Execution internally from the outside!

**Takeaways:**

Information gathering and recon is key!

Always check source code for hidden parameters

Try to escalate a high finding to critical with further exploitation.
