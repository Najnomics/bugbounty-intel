# Password Reset Poisoning with Host Header Injection

- **Source URL:** https://infosecwriteups.com/password-reset-poisoning-with-host-header-injection-345b902a9ca5?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20230209092653/https://infosecwriteups.com/password-reset-poisoning-with-host-header-injection-345b902a9ca5
- **Fetched:** 2026-11-24
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/1607 (id 1607)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Password Reset Poisoning with Host Header Injection

Hey folks, I am [Bharat Singh](https://twitter.com/zingzangoo) a Security researcher and Bug Hunter. I am here with an amazing writeup about Password Reset Poisoning with Host Header Injection Vulnerability which I recently found on a VDP and got rewarded with a HOF.

**What is Host Header Injection?**

Host Header injection is a type of vulnerability that allows an attacker to manipulate the host header sent in an HTTP request. By manipulating the host header, an attacker can direct the web server to serve a different website or application. This can be used to perform various types of attacks, such as phishing, cross-site scripting (XSS), or even redirecting a user to a malicious website with password reset poisoning.


Now lets dive into the main story about how I found that bug and how you guys can find and exploit this vulnerability.

## Story of the Bug

I was hunting on a VDP (Vulnerability Disclosure Program), it was a video streaming platform where you can watch movies and series. I tested that webapp for about 1 hour but got no luck and finally decided to test the password reset functionality, but I was not expecting to find any vulnerability there.

After clicking on forgot password option, I entered my email address and intercepted that request in my Burp Suite and send that request to the repeater.

I decided to play with that request and changed the Host to evil.com but the response throws an error. So I added an additional parameter below the Host parameter that is X-Forwarded-Host with value evil.com, like this:

Host: target.com

X-Forwarded-Host: evil.com


And it gave me a 200 OK response which I usually got, but in most of the cases password reset link remains same, as it does not change on the backend. But in this case I got the modified password reset link on my email address with host evil.com :

**Here are some ways you can find Password Reset Poisoning with Host Header Injection:**

\>> Try directly changing the password reset request’s Host

Host: evil.com


\>> Or try by adding X-Forwarded-Host

Host: target.com

X-Forwarded-Host: evil.com


\>> Try to add another Host header with different value

Host: target.com

Host: evil.com


**Steps to Reproduce:**

1\. Go to reset password page and enter the email for password reset link.

2\. Now intercept the request in Burp Suite and send it to repeater.

3\. Add a parameter X-Forwarded-Host below the Host parameter with any host. **(Also try the above techniques mentioned)**

4\. If you receive a password reset link from the injected host then you got the bug.

**Impact:**

An attacker can redirect users to a malicious site,which will leak the user’s password reset link/token leading to full account takeover or an attacker can send malware to the user’s system via the malicious link.

**End:**

If you find this writeup helpful then do hit that 👏 clap button, also don’t forgot to connect with me on [**TWITTER**](https://twitter.com/zingzangoo) and [**LINKEDIN**](https://www.linkedin.com/in/bharat-s1ngh/) to get regular updates.
