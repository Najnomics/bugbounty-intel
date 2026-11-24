# IDOR in a very damn vulnerable goverment site

- **Source URL:** https://medium.com/@bl4cksku11/idor-in-goverment-site-ffd523c47e5b?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20251126142210/https://medium.com/@bl4cksku11/idor-in-goverment-site-ffd523c47e5b
- **Fetched:** 2026-11-24
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/4164 (id 4164)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# IDOR in a very damn vulnerable goverment site

Hey sup guys! In this post I’ll be digging on a very damn vulnerable government site that I found, this is just telling us how deprecated the cybersec is in my country. You’ll get crazy about the lot of things you can find exposed on the internet tho.

Due to privacy purposes let’s call this site ***example.gov.comm,*** I don’t want problems haha.

## IDOR

IDOR (Insecure direct object reference) is a kind of broken access control vulnerability that occurs when an application provides direct access to objects based on user-supplied input. In the context of web applications, this means that an attacker can manipulate input, such as a URL parameter, to access and potentially modify objects (files, database records, user accounts, etc.) they are not authorized to access.

Let’s break down how IDOR vulnerabilities work.

`http://example.gov.comm/Services/index.php?ID=101037`
Normal Use Case:

- A user logs into the application and has access to their own data. For example, if “User A” logs in, they can access their data using the URL:

```
http://example.gov.comm/Services/index.php?ID=101037
          (where 101037 is their unique identifier)
```
IDOR Vulnerability:

- The vulnerability occurs when there is insufficient access control and validation. In this case, the application may not properly check if the user making the request has permission to access the resource associated with the “ID” parameter.
- An attacker, who doesn’t have permission to access certain data, can manipulate this parameter to access other users’ data or sensitive resources.

For example, an attacker could change the URL to: 101038

```
http://example.gov.comm/Services/index.php?ID=101038
          (where 101038 is their unique identifier)
```
If there is no proper access control in place, the application might serve the data associated with the “ID” 101038, which could be another user’s private information, for example private information of “User B”. This is a clear violation of security and privacy.

### Exploiting the IDOR

First of all, guess what? When I access to main domain of the site, there was no site, just directory listing enabled, I refused to believe that, lol.

Those directories were full of PHP applications, one of those apps “**PInicial-1.php**” was like a main page of the site.

Based on the main page explanation message, we can deduce that is a web application that centralizes all the processes of register and procedures of services requests, this means a lot of private information, customers data and org data also.

Let’s go the interesting part, hanging around the files, I found a file named “prueba2.php”, what looks like the list of administrative users and collaborators of the application:

Well, placing my mouse over these hyperlinks I noticed that it is sending a POST request to “**index1.php**” and giving a “**Identificator**” parameter to the “**index1.php**”:

I quickly intercept a request of one of those hyperlinks to see what is going on and see if we can modify that ID field. The response to the request was a 302 (redirection) status code, the server is redirecting me to the main page, so I check out the main page, and guess what?

Yep, now my name is Roger.

So, in here what I tried is to change the value of the User ID to try get another user account, check this out:

And yes, now I’m Damar, this is a positive indicator of an IDOR, so well this is the article of today, I reported this issue to the Goverment instutution, and now the page is down.

### Conclusion

To mitigate IDOR vulnerabilities, web applications should implement proper access controls **and ensure that a user can only access the resources they have the authority to access.** This typically involves checking the user’s permissions and verifying that they have the necessary rights to access a particular resource before providing it.

The risk associated with IDOR vulnerabilities is that unauthorized users can access and potentially manipulate sensitive information, leading to data breaches, unauthorized data changes, or even complete system compromise. It’s crucial for web developers to implement proper security measures to prevent such vulnerabilities and regularly test their applications for these types of issues.

See you next time bug hunters, happy hacking!!
