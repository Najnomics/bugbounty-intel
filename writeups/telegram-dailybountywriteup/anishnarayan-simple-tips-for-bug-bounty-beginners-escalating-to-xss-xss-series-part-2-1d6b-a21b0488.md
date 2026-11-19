# Simple Tips for Bug Bounty Beginners

- **Source URL:** https://medium.com/@anishnarayan/simple-tips-for-bug-bounty-beginners-escalating-to-xss-xss-series-part-2-1d6b75ecf942?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250418103337/https://medium.com/@anishnarayan/simple-tips-for-bug-bounty-beginners-escalating-to-xss-xss-series-part-2-1d6b75ecf942
- **Fetched:** 2026-11-19
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/7740 (id 7740)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Simple Tips for Bug Bounty Beginners: Escalating Open-Redirect to XSS (XSS Series Part — 2)

A website had a vulnerability known as an open redirect.

I have already explained about open-redirect in my [previous article](/@anishnarayan/simple-tips-for-bug-bounty-beginners-finding-open-redirect-bugs-cdd11c57af38).

Since the website’s parameter, in this case, the “redirect\_to” parameter in the URL, allows users to redirect to any URL. When someone navigates to “redirect\_to=//[phising.com](http://phising.com/),” the website redirects the user to “ phising.com.”

Now it is time to get to the XSS vulnerability.

Cross-site scripting (XSS) is an attack in which an attacker injects malicious executable scripts into the code of a trusted application or website. Attackers often initiate an XSS attack by sending a malicious link to a user and enticing the user to click it.

Now we want to see how open-redirect can be escalated to XSS. The most common type of XSS that occurs from open-redirect or URL manipulation is reflected in XSS.

Reflected Cross-Site Scripting (Reflected XSS) is a type of XSS vulnerability that occurs when an attacker injects malicious scripts into a website’s URL or input fields, and the website immediately “reflects” that input back to the user without proper validation or encoding. The script is executed in the victim’s browser, typically as a result of the victim clicking on a maliciously crafted link, leading to the execution of unauthorized code in the user’s browser

The impact of XSS is mainly private cookies getting exposed to malicious users leading to cookie theft and other problems such as user impersonation, session hijacking, unauthorized access and other actions, phishing, etc.

Tools such as XSStrike can be used to find URLs that could be vulnerable to XSS using the command:

python3 payloader.py


which is used to load the interface for the list of payloader tools. After selecting from the tools, you need to enter the URL each time you test with a given tool or when you want to enter your own custom payload.

But automated payloads result in false positives often and the testing would be insufficient, so it’s advisable to parallelly do manual payload testing to see if XSS pops up with any of the attempted payloads.

For the sake of minimal impact on the website to be tested, we will begin with the payload javascript:alert(‘XSS’) to test for XSS.

For some context, the entire URL will look something like [https://victim.com/?redirect\_to=javascript:alert('XSS')](https://victim.com/?redirect_to=javascript%3Aalert%28%27XSS%27%29). However, in most cases, XSS will not pop up simply by entering this payload.

So you might have to use a browser extension named “Wappalyzer” to see if any CDN is being used by the website. If a CDN is in the picture, it’s time to prepare for a long game because the firewall will block your attempts to pop an XSS.

This means that you have to obfuscate the payload and see if the obfuscated payload can help with the XSS. Now it’s time which parts of the payload are being blocked by the firewall.

Now it’s a different story if the firewall is blocking only the “alert” part of your payload. In this case, you still have a good shot at popping an XSS. However, if the “javascript” part of your payload is blocked, it’s not going to be simple.

Now, let’s get to the scenario where only “alert” is blocked by the firewall. In our first attempt, we can try to encode the payload starting from the semicolon (:) after the javascript.

We are going to assume that the firewall will block even encoded characters, so we go with a highly obfuscated XSS payload instead of a basic obfuscation payload where we use the ‘top’ object and ‘source’ property to construct the alert function.

1\. If you have been involved in frontend web development you would know that the ‘top’ property returns a reference to the topmost window in the current window hierarchy.

2\. Whereas the source property in JavaScript is used to return the text of the regular expression pattern before the dot.

3\. ‘+’ operator is used to concatenate the regular expression strings /al/ and /ert/

Putting everything together, we are using the technique of confusing the firewall by using a combination of top property, regular expression, source property, and string concatenation to craft the payload:

javascript:top/al/.source+/ert/.source.

It is highly likely that this payload can bypass the firewall and pop an alert on the screen and we have used string manipulation techniques to successfully execute an XSS.

**Solution:**

To mitigate these risks, it’s essential to implement robust input validation, output encoding, and proper cookie security attributes (like \`HttpOnly\` and \`Secure\`) to minimize the impact of reflected XSS vulnerabilities.

*Important Note: Vulnerabilities should never be used without permission on someone else’s website and testing is to be done only when the website permits, following the guidelines for testing.*


\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Also, check out the below Medium article:
