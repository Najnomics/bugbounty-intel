# This is how i escalated self XSS with CSRF

- **Source URL:** https://medium.com/@pvnk24/this-is-how-i-escalated-self-xss-with-csrf-80113ab3080e?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20240721110315/https://medium.com/@pvnk24/this-is-how-i-escalated-self-xss-with-csrf-80113ab3080e?source=rss------bug_bounty-5
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/6750 (id 6750)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
Hi guys, Hope you are doing great, i am [Pavan](https://web.archive.org/web/20240721110315/https://x.com/pavank_24), Today i am going to share how i escalated a self XSS with CSRF.

While reviewing one of the targets, I discovered a subdomain using a Google dork query: `site:target.com intitle:admin`. This query revealed a login page on the subdomain of the main target.

**Here is how i checked target as i don’t have login credentials**

I am not familiar with this subdomain and don’t have any information about it. I tried basic approaches before resorting to brute-forcing credentials and other pages because I want to avoid flooding the server with excessive requests.

**Default credentials:**

Similar to every one i tried some of default credentials and nothing worked.

**View Page Source for any Extra Information:**

I viewed page source to check if any extra information i get but nothing i got.

**Javascript Files:**

I gone through the javascript files to check any other paths which are available other than login and found nothing.

**Checked Tech stack:**

I tried to find tech stack so that i can search for vulnerabilities by version it was behind proxy nothing got reviled. (Here i couldn’t find a trusted version)

**Urls with wayback machine:**

I checked wayback machine to find other accessible urls which gives me some lead and i found some of urls but all are redirecting to login screen nothing found interesting

As I considered my options beyond logging in, I noticed there was a “Forgot Password” feature. I clicked on it and tried using “admin” as the username. The response was “**User admin not found**,” which made me excited because the username got reflected in the response.

Immediately, I tried a basic XSS payload by entering `admin<h1>hi</h1>`. The response was "Invalid username." To understand why I was getting this error, I examined the JavaScript file and discovered that there was a regex check for the username, allowing only numbers and names.

Additionally, I noticed that the input was encrypted using an algorithm before being sent to the server. However, the server’s response was returned as normal text without any encryption

So i couldn’t send my xss payload directly and even i send it is just a self XSS. now i got idea i created CSRF POC by encrypting my XSS Payaload “**admin\</div>\<script>alert(1)\</script>**” Using their algorithm so here i bypassed their checking of regex as i directly submitted form with my CSRF POC.

when some one clicks on it yes it redirects to their page and xss fires.I submitted issue to them.

Hope you learned something today!! Have a nice day.
