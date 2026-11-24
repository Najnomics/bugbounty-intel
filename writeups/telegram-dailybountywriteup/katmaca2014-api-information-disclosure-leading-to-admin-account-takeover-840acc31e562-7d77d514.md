# API Information Disclosure Leading to Admin Account Takeover

- **Source URL:** https://medium.com/@katmaca2014/api-information-disclosure-leading-to-admin-account-takeover-840acc31e562?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20251126142101/https://medium.com/@katmaca2014/api-information-disclosure-leading-to-admin-account-takeover-840acc31e562
- **Fetched:** 2026-11-24
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/3900 (id 3900)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# API Information Disclosure Leading to Admin Account Takeover

Hi everyone! In this project, my primary responsibility was to identify vulnerabilities in the website’s APIs. I’d like to share an incident where an API information disclosure ultimately led to an Admin account takeover. Lets look into it…

To begin, I followed standard procedures by running the website’s APIs and analyzing the requests and responses using Postman and Burp Suite. During this analysis, I stumbled upon an interesting finding. In one of the API endpoints, a key named “ApiUrl” was present, accompanied by a value. However, this value was not the expected IP address but a distinct address not utilized in the website’s main domains. This piqued my curiosity and prompted further investigation.

```
HTTP Response: 
HTTP/2 200 OK
Content-Length: 35988
Content-Type: application/json; charset=utf-8
Server: Microsoft-IIS/10.0
X-Frame-Options: sameorigin
X-Content-Type-Options: nosniff
Content-Security-Policy: default-src 'self'; script-src 'self' 'unsafe-inline' 'unsafe-eval'; font-src *; frame-src *
Permissions-Policy: accelerometer=(),autoplay=(),camera=(),display-capture=(),document-domain=(),encrypted-media=(),fullscreen=(),geolocation=(),gyroscope=(),magnetometer=(),microphone=(),midi=(),payment=(),picture-in-picture=(),publickey-credentials-get=(),screen-wake-lock=(),sync-xhr=(self),usb=(),web-share=(),xr-spatial-tracking=()
Strict-Transport-Security: max-age=31536000; includeSubDomains; preload
X-Xss-Protection: 1; mode=block
Date: Wed, 09 Aug 2023 08:11:43 GMT
{"Result":{"DeviceInfo":{"TerminalNo":"*****","Limit":50000,
"ApiUrl":"https://NEW-IPADDR/api/",
"ApiUserName":"******==",
"ApiPassword":"******=="},"TaxProfileList":
[{"Title":"KDV 1","TaxVatIncluded":1,"Idx":1},
```
Upon attempting to access the provided URL, I encountered a 404 error, indicating that the specified URL was not found. Nevertheless, the correct IP address indicated that there might be an alternative endpoint worth exploring. My investigation continued, and I used GoBuster to search for potential endpoints using the “seclists/discovery/web-content/big.txt” wordlist:

`gobuster dir -u IPADDR -w /usr/share/seclists/Discovery/Web-Content/big.txt`
After GoBuster completed its scan, it revealed the existence of an endpoint named “/trs.” Upon entering “IPADDR/trs” into the browser’s URL bar, I discovered an older webpage associated with the application.

Continuing my assessment, I decided to test common administrator usernames, which led me to discover that the default username was “admin.” To uncover the password, I executed a Burp Suite Intruder attack, using a list of 500 commonly used passwords for admin users. Once the Intruder process was completed, I successfully gained access to the web application with admin privileges.

In conclusion, the critical vulnerability that allowed an Admin account takeover stemmed from the API information disclosure. It’s imperative to note that developers should refrain from including the IP address of hidden websites in response packets, as this can lead to unauthorized access. Furthermore, administrators should employ robust and hard-to-guess passwords to enhance security measures.
