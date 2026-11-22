# How I Leveraged Open Redirect to Account Takeover

- **Source URL:** https://goziem.medium.com/how-i-leveraged-open-redirect-to-account-takeover-9d877e8b30ef?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20251126141646/https://goziem.medium.com/how-i-leveraged-open-redirect-to-account-takeover-9d877e8b30ef
- **Fetched:** 2026-11-22
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/2433 (id 2433)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# How I Leveraged Open Redirect to Account Takeover

2 min readApr 20, 2023

Hello, hackers!

## **Summary**

An **account takeover** bug is a type of vulnerability that can be exploited by attackers to gain unauthorized access to user accounts on a system or platform. This type of bug can be used to steal sensitive information, such as personal data, financial information, or intellectual property, or to carry out malicious activities, such as spreading malware, launching phishing attacks, or hijacking the account for spam or other purposes.

## **How I found the bug:**

- The target I was testing had its subdomains in scope.
- I simply used subfinder to gather all subdomains.
- I found a subdomain like ***community.target.com***
- I used a tool to then get all urls associated with the subdomain.
- While going through all of them one by one, I came across an error message from a url:

- I noticed that when I clicked on the try again button, it took me to another part of the website so my guess was that there was some sort of open redirect going on since there was also a url parameter in the url.
- I also noticed that the url parameter wasn’t in form of a url so I suspected that it was encoded in base64 and then I went over to [Base64 decoder](https://www.base64decode.org/)
- I decoded the payload and I was correct. There was some sort of encoding involved and the encoded url was ***https://community.target.com***
- I quickly tested it for open redirect by encoding https://anysite.com in base64 and putting it into the url parameter and I got redirected immediately.
- I then tried for Reflected XSS using javascript:alert() and an alert box popped up.
- I wanted to report it but I knew that I could further escalate it to ATO.
- Through the help of ChatGPT, I successfully crafted a payload to steal user’s cookie and send them to my server.

- I was already excited an decided to report the bug as an ATO bug shortly after, the report was marked as OOS for some reason, but I did learn a lot from the bug.

I collaborated on this with [Topenga](https://twitter.com/TopengaNFT) and it was a nice one.

## **Tips**

1. Always test for xss if you find a case of open redirect
2. Encode your payloads
3. Never give up.

Thanks for reading and feel free to ask any questions.
