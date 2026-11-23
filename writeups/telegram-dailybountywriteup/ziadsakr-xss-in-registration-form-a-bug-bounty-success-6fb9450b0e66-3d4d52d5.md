# XSS in Registration Form

- **Source URL:** https://medium.com/@ziadsakr/xss-in-registration-form-a-bug-bounty-success-6fb9450b0e66?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20241117121525/https://medium.com/@ziadsakr/xss-in-registration-form-a-bug-bounty-success-6fb9450b0e66
- **Fetched:** 2026-11-23
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/7887 (id 7887)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
Hello everyone , I hope you are well.

بسم الله الرحمن الرحيم

# Introduction

**This is my first Write-Up for my first bug I have found in my bug bounty journey, which started by the way in just two weeks ago.** It has been an exciting and educational experience, and I am proud to share how I collaborated with my friend **Ahmed Hisham** ([CipherHawk](https://medium.com/u/0b1e7473516a?source=post_page---user_mention--6fb9450b0e66--------------------------------)), I discovered a **Cross-Site Scripting (XSS)** vulnerability in the registration form of a web application. This vulnerability allowed malicious scripts to be executed in the context of user’s browser.

In this article, I’ll walk you through the process we followed to discover, exploit, and validate this vulnerability, as well as the key takeaways for improving web application security.

# What is Reflected XSS?

Reflected XSS occurs when an attacker injects malicious scripts into a webpage through user input, and the server immediately reflects this input back to the user without proper sensitization. Unlike stored XSS, where the malicious script is stored on the server, reflected XSS is executed in real-time during the user’s interaction with the page. This vulnerability is commonly exploited via URL parameters or forms that don’t adequately sanitize input.

The attacker can craft a URL containing malicious JavaScript, and when the victim clicks on the link, the script executes in their browser, potentially stealing session cookies, manipulating page content, or performing unauthorized actions on behalf of the user.

# The Discovery

During a bug bounty engagement, I was working with Ahmed Hisham to assess a web application’s registration form. As we examined the form, we noticed that certain input fields didn’t sanitize or validate user input properly. We quickly realized this could be an opportunity to test for HTML/XSS vulnerabilities.

# The Attack Vector

The registration form allowed input fields to accept user data, including names, email addresses, and more. However, it didn’t properly handle special characters or JavaScript event handlers, so i try to inject some JS events like **onerror**, or **onmouseover**.

It reflects our payload in the input tags so we injected the following payload into the `first_name` field:

`"onmouseover=alert(document.cookie)`
when rendering the input tag should be something like that

`<input type="text" class="form-control" name="gc_company" id="gc_company" required="required" value="\" onmouseover="alert(document.cookie)">`
But the firewall detect it !

I needed a way to bypass the validation, so I experimented with various techniques until I fully understood how it processes and validates the entered data. During my tests, I observed that when I inserted dummy characters between parts of a word, the system automatically removed them and reassembled the word. This gave me the idea to insert a JavaScript event, like `onmouseover`, and strategically place dummy characters within it to evade the validation. Here's how I implemented it:

`"onmous%25%37%34eover=alert(document.cookie)>123`
Then make the request and BooM!!

XSS is Fired 🔥

That’s all for today, I hope you enjoyed reading this write-up, and hopefully, there will be more exciting vulnerabilities and stronger findings in the future!

#xss #bugbounty #bugbountytips #js #hunters
