# XSS on out of scope domain? CORS is your secret weapon!

- **Source URL:** https://c4rrilat0r.medium.com/xss-on-out-of-scope-domain-cors-is-your-secret-weapon-93e433278080?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20240526042133/https://c4rrilat0r.medium.com/xss-on-out-of-scope-domain-cors-is-your-secret-weapon-93e433278080
- **Fetched:** 2026-11-19
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/5792 (id 5792)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# XSS on out of scope domain? CORS is your secret weapon!

Hello everyone, and welcome to my second Medium post! I hope you enjoy and find it helpful.

In this post, we’re exploring XSS (Cross-Site Scripting) vulnerabilities, which can sometimes be overlooked, particularly when they occur in out-of-scope (OOS) domains. However, when combined with CORS (Cross-Origin Resource Sharing) misconfigurations, these vulnerabilities can become valid within the scope of a security program, potentially leading to bounty eligibility.

To illustrate this, I’ve got a real-life example from a HackerOne program I stumbled upon. Let’s call it “redacted.com” and its out-of-scope counterpart “community.redacted.com”.

One day, while skimming through the automated results of my workflow, I stumbled upon an XSS vulnerability lurking within the “community.redacted.com” domain.

Upon reviewing the HackerOne program, I found out that while \*.redacted.com fell within the scope for bounty eligibility, “community.redacted.com” did not. Realizing this, I couldn’t help but feel a bit disappointed initially, as I had underestimated the potential severity of the vulnerability.

But, if that vulnerability had been dismissed, I wouldn’t be writing this blog, right?

After some days of pondering over this XSS, I realized that I was missing something. Sometimes, with a broad scope, it is necessary for some applications to utilize Cross-Origin Resource Sharing (CORS) to integrate applications within the same scope.

Now, let’s talk about CORS. CORS is a security feature implemented by web browsers to control access to resources from different origins. It allows web servers to specify which origins have permission to access their resources. When an application sets the `Access-Control-Allow-Origin` header to `*.redacted.com`, it essentially allows any web page hosted on a subdomain of "redacted.com" to access its resources.

The issue arises when the `Access-Control-Allow-Credentials` header is set to `true`. This header indicates whether the request can include credentials such as cookies, authorization headers, or TLS client certificates. When this header is set to `true`, it means that the server is willing to accept credentials from the requesting origin, assuming it's permitted by the `Access-Control-Allow-Origin` header.

So, what’s the issue here? By allowing any subdomain of “redacted.com” to access resources with credentials, such as session cookies, an attacker could exploit an XSS vulnerability in an out-of-scope domain (like “community.redacted.com”) to steal sensitive user data or perform unauthorized actions on behalf of the user within the scope domain (“redacted.com”).

After analyzing that, the next step is to search for a domain within redacted.com that allows `Access-Control-Allow-Origin` from any domain within redacted.com and has `Access-Control-Allow-Credentials` set to true. Another critical condition to consider is that the domain with the CORS misconfiguration should have cookies to access sensitive information.

To automate this process, you can use a modified version of the CORS misconfiguration detection nuclei template from [Project Discovery](https://raw.githubusercontent.com/projectdiscovery/nuclei-templates/main/http/vulnerabilities/generic/cors-misconfig.yaml). This version is adjusted to avoid unnecessary requests and can be found here:

```
id: cors-misconfig
info:
  name: CORS Misconfiguration
  author: c4rrilat0r
  severity: info
  tags: cors,generic,misconfig
http:
  - raw:
      - |
        GET  HTTP/1.1
        Host: {{Hostname}}
        Origin: {{cors_origin}}
    payloads:
      cors_origin:
        - "https://{{tolower(rand_base(5))}}.{{RDN}}" # Find domain in RDN with Misconfiguration
    stop-at-first-match: true
    matchers:
      - type: dsl
        name: arbitrary-origin
        dsl:
          - "contains(tolower(header), 'access-control-allow-origin: {{cors_origin}}')"
          - "contains(tolower(header), 'access-control-allow-credentials: true')"
        condition: and
```
After some manual testing, luck was on my side this time! I stumbled upon a significant misconfiguration right on the main page of [www.redacted.com](http://www.redacted.com). When I tested it using the XSS domain ‘community.redacted.com’ as the origin, I hit the jackpot:

- Got access to sensitive info through cookies.
- Found that ‘community.redacted.com’ was allowed in the ‘Access-Control-Allow-Origin’ header.
- ‘Access-Control-Allow-Credentials’ was set to True.

With all this juicy info, I cooked up an XSS payload on community.redacted.com to fetch sensitive data from [www.redacted.com](http://www.redacted.com). And boom! By cleverly chaining the XSS with the CORS setup, I managed to swipe sensitive info from a different origin.

The payload used to access and consume sensitive information from another domain was as follows:

```
url= 'https://www.redacted.com/profile'; 
fetch(url ,{credentials:`include`}) // To send the cookies in the request
  .then(response=>{return(response.text());}) 
  .then(data=>alert(JSON.stringify(JSON.parse(data)[`user`])));
```
The exploitation led to the successful retrieval and consumption of sensitive information from the target domain ([www.redacted.com](http://www.redacted.com)) by the XSS vulnerability present in the out-of-scope (OOS) domain community.redacted.com.

I promptly prepared the report and submitted it, hoping that the program team would recognize the value of this chain of vulnerabilities. Fortunately, the program team was fantastic; they triaged the report within a day and awarded a bounty of $904!

I hope this technique proves helpful to someone grappling with an XSS vulnerability in an out-of-scope domain. I wouldn’t recommend automatically scanning domains out of scope due to program restrictions. However, if you’ve already identified the XSS, you can certainly test if this technique works for you. Stay safe and responsible in your security research endeavors!

Thank you for joining me.

You can following me on twitter: [https://twitter.com/c4rrilat0r](https://twitter.com/c4rrilat0r).
