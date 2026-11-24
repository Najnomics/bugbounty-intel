# Explanation of CSRF ( Cross-Site Request Forgery )

- **Source URL:** https://infosecwriteups.com/explanation-of-csrf-cross-site-request-forgery-bc6a5042bcbf?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250506014345/https://infosecwriteups.com/explanation-of-csrf-cross-site-request-forgery-bc6a5042bcbf
- **Fetched:** 2026-11-24
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/2817 (id 2817)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Explanation of CSRF ( Cross-Site Request Forgery )

## Explain Cross-Site Request Forgery

Hey Guys Welcome to my Blog Today we going to discuss about CSRF vulnerability which is probably medium / Low and sometimes it is out of scope / not applicable to log-in and Logout functionality I will say why this is not acceptable for this function and finale we discuss about hunting of CSRF

## What is CRSF?

CSRF (Cross-Site Request Forgery) allows the attacker to modify the user information, Password, etc.. and it does not happen directly the attacker wants to trick the user to click a link where the user already authenticated on the application through the Browser

Let’s say there is two user Ram is the attacker and Tom is the victim

In this scenario, Tom has created an account on reacted.com and already authenticated through his browser if tom visits that website through his browser it won’t ask for the username and password to log in again due to cookie

A cookie is nothing but a 4KB file stored in your local browser which is used to store user-specific data, such as session identifiers, preferences, or shopping cart items and later it retrieves by the server


On another side, the ram has found the CSRF vulnerblity on password reset and Draft some malicious HTML code

```
<html>
  <body>
    <form action="reacted.com" method="POST">
      <input type="hidden" name="password" value="hacked" />
      <input type="hidden" name="password_confirmation" value="hacked" />
      <input type="submit" value="Submit request" />
    </form>
  <script>
   document.addEventListener('DOMContentLoaded', function(event) {
    document.createElement('form').submit.call(document.getElementById('myForm'));
    });
  </script>
  </body>
</html>
```
After that, Ram embedded his malicious code and hosted it on trust.com.in and he send it to tom

If He clicks that link the password will get reset and we can able to take over his account

Since Tom is authenticated, reacted.com processes the request and changes the password to “hacked”, effectively compromising Tom’s account.

This scenario highlights the importance of implementing proper security measures, such as implementing CSRF protection mechanisms, to prevent such attacks. CSRF protection typically involves adding anti-CSRF tokens or using techniques like same-site cookies or double-submitted cookies to validate requests and ensure they originated from the legitimate user’s browser.

So Now you can clearly get the idea about CSRF

## Why is it out-of-scope and Not-applicable in login/logout?

This is because there is no impact on that bug it is just simple login/logout not going to make any impactful changes let's see you're running a company and you're getting a lot of high-severity vulnerabilities like XSS, SQL, etc. So here you will fix that high severity or nothing impact

Definitely high severity right !!!! So be a Hacker and look for a Big one !!!!

And Make proud to hackers Community with a Big one !! You can do it!!

## Hunting for CSRF !!!

1. **Check for state change action endpoint:** State Change action is nothing but the action that changes or alters the user data

For example, Password Change, delete Account, send message / Email

2\. **Lack of CSRF Protection:** check if there is a CSRF token if it is available we will bypass that using some techniques and no means it is vulnerable to CSRF (Sometimes Same-site Protection is also there)

3\. **Confirm the Vulnerability:** Confirm the vulnerability by drafting the HTML form or using Burpsuite Pro to generate the HTML form of CSRF

Some of the websites do not have any CSRF token but still they can be safe by using refer token we can also able to bypass this

Checkout Part-2 article for CSRF bug: [https://evilox.medium.com/unmasking-basic-csrf-bug-hunter-5003dbe44466](https://evilox.medium.com/unmasking-basic-csrf-bug-hunter-5003dbe44466)

I hope you will understand this article if like give applause and click the follow button to get an Update
