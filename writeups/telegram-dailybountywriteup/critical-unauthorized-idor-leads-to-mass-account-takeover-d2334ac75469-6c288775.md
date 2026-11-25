# Critical Unauthorized IDOR Leads to Mass Account Takeover

- **Source URL:** https://larebsec.medium.com/critical-unauthorized-idor-leads-to-mass-account-takeover-d2334ac75469?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20231012150426/https://larebsec.medium.com/critical-unauthorized-idor-leads-to-mass-account-takeover-d2334ac75469?source=rss------bug_bounty-5
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/3454 (id 3454)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
Assalamu alaekum guyzz, After months of duplicates and false positives, Alhamdulillah I have found a valid bug, actually A very high impactful bug, IDOR which can lead to Account Takeover of all the users on the Web Application.

So here we go, We all know what IDOR is, but those who don’t know, IDOR occurs when a web application provides users with an authorized reference or ID that can be used to access or change other unauthorized information. For more info check on [portswigger](https://web.archive.org/web/20231012150426/https://portswigger.net/web-security/access-control/idor)

Lets dive right into it, let the site be redacted.com, as the bug has not been patched yet, so I visited the website and checked for all the functionality, my every time habit, and let my script for info gathering like subdomain, ports enumeration, directories with mixup of tools like sublit3r, ffuf, amass, wayback, katana, gau etc etc….I noticed that I can’t register for new account as it was asking for valid information which i did not have then.

## In Pursuit of suc55e5

I jumped on the subdomains. After all the searching through subdomains i found 6–7 login panels but did not get any luck in finding anything juicy or useful. I was exhausted, so shut down my laptop and went straight to bed.

Next morning with full JOSHH, I started to look for any functionality if any has been missed then I looked that we can book items without registering any account. and after booking an item we got Thank you reciept of order’s confirmation with some URL like [https://www.redacted.com/thankyou/119/64c4d47aefa3c/235936](https://web.archive.org/web/20231012150426/https://www.redacted.com/sadrzaj-thankyou/119/64c4d47aefa3c/235936) ,That Some id like number caught my attention and i was like wohoo wait, why not play with some number.

Sent it to repeater, I changed number to random no. and BOOOOM!!! I can see another user’s personal information and I took a sigh of relief. This way I can see all the user’s personal information.

# **Assail Soldiers**

Then I thought why not increase it’s impact, I remembered that in starting we have login functionality, it asked for email and some loyalty card number. I looked up some user’s information got from IDOR…. I can get the necessary information for logging in,I was soooo much happy and quickly tried to log in any user’s Account and here’s another BOOOOOOOM!!! I was logged in another user’s account with full the functionality. A*n Account Takeover*


I can log into anyone’s account on webapp and can use all the functionality like edit, order etc etc. I immediately reported the vulnerability to the company.

*Takeaways:*

\~Always check all the functionality.

\~Always check burpsuite history see if any url that has been missed from showing.

\~Look for side functionality, do not be depressed if could not find anything on login panels.

\~Always think, ok now what can I do to increase it’s impact.

\~Try to chain vulnerabilities.

\~Do not stop only on what if, just do it, try it and see its result

Keep trying and practice and practice and practice….

Like and share with your friends if you learned something new. You can find me on [linkedin](https://web.archive.org/web/20231012150426/https://www.linkedin.com/in/lareb-malik/)
