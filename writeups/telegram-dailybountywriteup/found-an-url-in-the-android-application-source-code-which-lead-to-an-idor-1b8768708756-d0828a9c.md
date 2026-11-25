# Found an URL in the android application source code which lead to an IDOR

- **Source URL:** https://vengeance.medium.com/found-an-url-in-the-android-application-source-code-which-lead-to-an-idor-1b8768708756?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20260710144222/https://vengeance.medium.com/found-an-url-in-the-android-application-source-code-which-lead-to-an-idor-1b8768708756?source=rss------bug_bounty-5
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/1754 (id 1754)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Found an URL in the android application source code which lead to an IDOR

I was testing the target which had its web application and mobile application in scope. Let’s say the target is example.com

Firstly, I tested its web application which had only one domain in its scope. I found some vulnerabilities in the target web application and reported them to the program (Most of them were duplicates 😅).

Then I moved on to mobile application testing. With the little knowledge and experience I had with android application testing, I used apktool to decompile the android apk file. Then I started diving deep into the source code to see if I can find any hardcoded keys, tokens, or anything useful.

After some time I found a URL in the source code which I had not seen while testing the web application. The URL was *“https://example.com/getCustomerInfo?loginToken=”*

To automate the process, [Apkleaks](https://web.archive.org/web/20260710144222/https://github.com/dwisiswant0/apkleaks) can be used to scan APK files for URIs, endpoints & secrets.


Immediately I entered a random value in *loginToken* parameter and checked if I got any information. But the server responded with a 500 status code.

Then I began to check burp history to see if any previous HTTP request or response contains any *loginToken* value. After some time I got an id parameter in the HTTP response with a numerical value. The response of */user/get-finance-user* had an id parameter whose value can be used as a value of *loginToken* parameter.

After using the value from the id parameter as a value of *loginToken* parameter I got my information in the response.

Then I used the burp intruder to brute force the *loginToken* value and got all the available information of the customers.

So checking only the source code of an android application helped me to find a new endpoint through which I was able to find an IDOR vulnerability in the web application.

Even though you don't plan to test the mobile application, reviewing the source code can provide you with useful information.

Thanks for reading.

Twitter: [Vengeance0x0](https://web.archive.org/web/20260710144222/https://twitter.com/Vengeance0x0)
