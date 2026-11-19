# Uncovering SSRF attack

- **Source URL:** https://medium.com/@cyberkarthi/uncovering-ssrf-attack-cd2eac89db72?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20230627100110/https://medium.com/@cyberkarthi/uncovering-ssrf-attack-cd2eac89db72
- **Fetched:** 2026-11-19
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/3096 (id 3096)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Uncovering SSRF attack🎯

--

Hello fellow bug hunters,

Today we gonna unleash the bug “**SSRF-(Server Side Request Forgery)**”

I usually prefer SSRF while hunting, SSRF commonly occurs in parameters, input field, headers and even in file upload and XXE which leads to SSRF.

**What is SSRF?**

A Server-Side Request Forgery (SSRF) attack involves an attacker abusing server functionality to access or modify resources. The attacker targets an application that supports data imports from URLs or allows them to read data from URLs.

**How SSRF occurs?**

SSRF flaws occur whenever a web application is fetching a remote resource without validating the user-supplied URL. It allows an attacker to coerce the application to send a crafted request to an unexpected destination, even when protected by a firewall, VPN, or another type of network access control list (ACL)

You may already seen many blogs about SSRF, but this one is different.

I just wrote simple python script for better understanding, how the root cause of SSRF occurs

import requests

def fetch\_data(url):

response = requests.get(url)

return response.text

def process\_user\_input(url):

data = fetch\_data(url)


user\_url = input(“Enter a URL: “)

process\_user\_input(user\_url)

The above code is a vulnerable code, it doesn’t validate the user input and it directly loads the data.

By exploiting SSRF, we can able to read local files, Remote file inclusion, Internal port scanning even in some cases it could leads to RCE (Remote Code Execution)

Check the attached image below for PoC.

And yes, as a security researchers and a secure code developer, we must know how to mitigate a flaw,

**There are some ways to resolve the occurence of SSRF:**

**1. Input Validation and Whitelisting**

Validate and sanitize all user-supplied input, especially URLs. Implement strict input validation to ensure that the URL adheres to the expected format and protocol. Whitelist allowed domains or IP addresses to restrict the scope of requests.

**2. Use Safe API**

If your application needs to fetch data from external sources, consider using a safe API that provides limited and controlled access to specific resources. Avoid using APIs that allow arbitrary URLs to be fetched.

**3. Restrict Access to Internal Resources:**

Ensure that the application’s server and back-end systems are properly configured to restrict access to internal resources. Utilize firewalls, network segregation, and access control mechanisms to prevent requests to sensitive internal URLs or IP ranges.

I wrote a below script for better understanding to how to mitigate the SSRF.

from urllib.parse import urlparse, urlunparse

def is\_safe\_url(url):

allowed\_protocols = (‘http’, ‘https’)

allowed\_domains = (‘[example.com](http://example.com/)’, ‘[api.example.com](http://api.example.com/)’)

parsed\_url = urlparse(url)

return parsed\_url.scheme in allowed\_protocols and parsed\_url.hostname in allowed\_domains

def process\_user\_input(url):

if is\_safe\_url(url):

print(“Safe URL: “, url)

else:

print(“Unsafe URL: “, url)

user\_url = input(“Enter a URL: “)

process\_user\_input(user\_url)

Now, we can able to resolve the SSRF attack.

I hope now you will have a better understanding of how SSRF occurs and how to mitigate the occurence✌

Keep an eye out for the upcoming writeups and join me in the quest for a more secure digital world.

Thank you for reading,

# **Connect with me:**

Instagram : [https://www.instagram.com/cyber\_karthi/](https://www.instagram.com/cyber_karthi/)

Linkedin : [https://www.linkedin.com/in/cyber-karthi/](https://www.linkedin.com/in/cyber-karthi/)
