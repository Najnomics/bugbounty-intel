# How I found a IDOR at Monitor Mozilla ?

- **Source URL:** https://medium.com/@abnid312/how-i-found-a-idor-at-monitor-mozilla-313fc6c52f25?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20240605103424/https://medium.com/@abnid312/how-i-found-a-idor-at-monitor-mozilla-313fc6c52f25
- **Fetched:** 2026-11-19
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/6117 (id 6117)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
Hi Folks!

This is my first writeup on this platform. On this occassion, i want to share my story find a bug IDOR (Insecure Direct Object References) at [Mozilla Monitor](https://monitor.mozilla.org/).

What is Mozilla Monitor?

Mozilla Monitor is a free service that notifies you when your email has been part of a breach, announced its new paid subscription service offering: automatic data removal and continuous monitoring of your exposed personal information.


At the time, I was trying to find out if my email had been leaked on multiple platforms using Mozilla’s Monitor service. Then, I tried to create an account on the website using my email address.

After I registered on the website, I got several notifications that it was true that my email had a data leak on several platforms. After I got the notification, I immediately recovered my email by changing the email password and activating several password security recommendations.

After I recovered my account that was affected by the data leak, I tried to explore the service. In the dashboard account, in the settings section. There is a feature is **Monitor Settings,** where you can add another email address to scan these emails that whether the email has a data leak or not.

An explanation of the image above, When adding an email address, the email automatically has an identity stored in the *id* parameter, and also for *subscriber\_id* is an identity of the owner’s team.

# Exploitation

In this part of the exploit, I tried to create accounts with different email addresses. After I created an account on the website, I tried to add an email address to the monitoring email address with a random email.

Let’s just assume that my first account as the attacker, and the second account as the victim.

On the first account, I tried deleting the email address in the monitoring email address to see the request endpoints. After that, I saw that the request was directed to the **/user/settings** endpoint with the **POST** method along with the JSON in the body section. In the JSON content there are the following *id*, *subscriber\_id*, *sha1*, *email*, and *verification\_token*, etc.

What concerns me is the *id* parameter which is the identity of each email address.

In the second account, I turned on Intercept in the Burpsuite app when I deleted an email address in the email address monitoring, after that I sent it to the repeater to save the request and then I canceled the deletion by pressing the **Drop** button. In this case, I know the parameter *id* rather than the email address of the second account.

After I have obtained the parameter *id* of the second account. I returned to the first account by doing the same thing, namely trying to delete the email address in the monitoring email address, after which the request was sent to the repeater.

After I sent the first account’s email address deletion request to the repeater, I tried to change the value of the id parameter contained in the second account.

BOOOOMM!!!

After I checked the account which as a victim’s, I saw that the email was deleted.

We apologize if there are any wrong words. I am happy if you have suggestions and criticisms for my future writing

Thank you for taking the time to read my story, **Happy Hunting** !

Reference : [https://hackerone.com/reports/2382484](https://hackerone.com/reports/2382484)
