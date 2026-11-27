# My journey to find CSRF (Cross-Site Request Forgery )

- **Source URL:** https://medium.com/@osamamohamed21212121/my-journey-to-find-csrf-cross-site-request-forgery-ddf1e1bd579d?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250716121857/https://medium.com/@osamamohamed21212121/my-journey-to-find-csrf-cross-site-request-forgery-ddf1e1bd579d
- **Fetched:** 2026-11-27
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/7248 (id 7248)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# My journey to find CSRF (Cross-Site Request Forgery )

Hello, my name is Osama Mohammed, and I am a penetration tester and bug hunter.

Hi, welcome back to another blog. In this blog, we’re going to know how I found my CSRF in the external program. So, before starting, if you haven’t followed our medium account, do follow, guys. So without wasting time let’s get into the story of the CSRF .

until I found the function responsible for ‘Forgot Password.’

Fortunately, this website did not require the current password before changing it to a new one.”

“I realized here that there was a high chance to find a CSRF vulnerability.

I just needed to confirm two important things:

Referrer: I had to ensure that the website allowed password changes from different sources or, in short, that I could change the password with a referrer different from the original website.

For example:

Referrer: [https://www.target.com/reset-password](https://www.target.com/reset-password)

I confirmed that I could change it to anything, like:

Referrer: [https://www.attacker.com/](https://www.attacker.com/)

I succeeded in that! :)

response:

200 ok

**Now we are 50% closer to finding the vulnerability.**

**Token**: This is the most difficult part because most websites verify it very well, but there are many ways to bypass it if the site checks the token.

Now it’s time for exploitation!

I confirmed all the previous steps.

The only thing left was the token.

I changed my password, intercepted the request, manipulated the token value, and even deleted it, and I successfully changed the password.”

and BOOOOOOOOOOOOOM 

CSRF

“I quickly created the HTML page, wrote the code, and confirmed the vulnerability.”

Done

Thank you for watching.

“Don’t hesitate if you have any questions about anything.

I will leave my account for contact.

Follow me.”

***LinkedIn Profile :***
https://www.linkedin.com/in/osama-mohamed-b788b12b1/
