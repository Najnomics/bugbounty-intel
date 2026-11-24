# How I discovered XSS via triple URL encode

- **Source URL:** https://medium.com/@mohammed01550038865/how-i-discovred-xss-via-url-encode-3-times-86ccd5354081?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20230507171255/https://medium.com/@mohammed01550038865/how-i-discovred-xss-via-url-encode-3-times-86ccd5354081
- **Fetched:** 2026-11-24
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/2593 (id 2593)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# How I discovered XSS via triple URL encode

--

Helllloooo Hackers,

This my Report on how I discovered XSS via triple URL encode and bypass WAF

first I started with Recon . Recon is the most important part of bug bounty so take your time on Recon

I collected Subdomains , endpoints and params. I found subdomain looks this [https://maindomain.com/blog](https://maindomain.com/blog) I browsed this I can see search box I am started with test XSS on this search box first I used this payload “>\<svg onload=confirm(‘XSS’)> and I got Nothing as shown in the image payload Reflected on the page put not trigger.

Then I used this website for URL encode [URL Encode and Decode — Online (urlencoder.org)](https://www.urlencoder.org/) . and encode this payload “>\<svg onlod=confirm()> and test again the also the payload not trigger and I can’t see pop up then I encode the previous payload aging and test again also the payload not work then I encoded the previous payload agin and retest Now I can see pop up as shown in the image below .

the finall payload :

%2522%253E%253CsVg%252FOnLuFy%253D%2522X%253Dy%2522oNloaD%253D%253B1%255Econfirm%25281%2529%253E

this the 3 times encode for this payload

“>\<sVg/OnLuFy=”X=y”oNloaD=;1^confirm(1)>/\`\`¹//

I reported this to security team and submission changed to triaged after one day from submitted the report and security team fixed the submission after 2 days because this affect on the main domain and I got the bounty after 10 days.

Tips :

try URL encode

try double URL encode.

try triple URL encode.

try base64 encode.

always see the source code to create the right payload.

I hope this is useful for U.

Best regards,

Smallest Hacker!
