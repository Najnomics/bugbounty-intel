# How I got RCE on an Indian university without admin credentials Tale of directory listing, SQL…

- **Source URL:** https://medium.com/@alimuhammadsecured/how-i-got-rce-on-an-indian-university-without-admin-credentials-tale-of-directory-listing-sql-1f77e2933011?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20240911091453/https://medium.com/@alimuhammadsecured/how-i-got-rce-on-an-indian-university-without-admin-credentials-tale-of-directory-listing-sql-1f77e2933011
- **Fetched:** 2026-11-19
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/7233 (id 7233)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# How I got RCE on an Indian university without admin credentials Tale of directory listing, SQL injection, File uploads, BAC, LFI

Hacking Indian university’s web servers.

I found numerous vulnerabilities in the website, the most notable were:

*SQL Injection (Reflected)*

*Directory listing (allowed me to trigger the shell)*

*BAC (broken access control) gave me access to sensitive meeting documents*

*Arbitrary File upload to get a shell*

*Possible XSS stored (would be triggered in the admin panel)*


# Part 1: Exploiting SQL Injection

At first I looked around for a few minutes and noticed some GET **parameters** that were **Base64 encoded**. **FFUF** for directory fuzzing was not practical due to some sort of **rate limiting** and **firewall** in place. Moreover, this site was being hosted on **CPanel**.

As I was looking around I fired these in the background:

Nmap server

Subdomain FUZZING (bunch of defaults, CPanel, etc)


The SQL injection was promising and I was able to dump the admin username and credentials, this was slow because I had to base64encode my payloads and could not automate due to robust rate-limiting and firewall restrictions.

After a stereotypical **ORDER BY** and **UNION SELECT** I noticed **colum 2** was being reflected. Therefore, we can use this to dump information.

Now we simply dump the table contents:

Unfortunately, I could not crack the hash and it was salted **Bcrypt hash** which Rockyou.txt failed.

Nonetheless, this is still a vulnerability.

# Part 2: Leveraging Directory listing & BAC

What I like to do on sites I do VPA on is to copy the URL to an image, paste it, and see if I can list the /images directory and see if **directory listing** is enabled. In my case, it was.

I went through all the files and nothing interesting came up, but did you notice something interesting in the URL?

**/admin/logged**


This may hint at **BAC (Broken Access control).**

I knew there must be some sort of BAC, but I could not find it in the /logged directory because every time I went there it said “**session expired**” and it would be a redirect. This was not a **EAR (Execute After Return)** because I disabled redirects and no luck. The reason EARs happen is an example below:

This is obviously not real code, but pseudocode. If you’re session is vlid then you’re allowed to view /admin/logged and access **Restricted Admin Panel Routes.** However, if you’re not it redirects you back to login and sends you a message that your session is expired. However, do you see the issue? There is not **return**, only a redirect. Which means your browser is just redirecting, but technically that data is still accessible with an invalid session. When fuzzing this can be obvious if you have a **302 (redirect)** statuscode with a large **content length** number-keep an eye out for this during bug bounty hunting!

To fix **EARs** in PHP is simple, just add **die()** (in pseudocode I just put **return**) to kill the route.

## Google Dorking

I was too stubborn and wanted to find my first ever BAC so I did some google dorking.

Since I have a strong feeling there is a **BAC** in the admin panel I simply did

*site: SITE.com intext: admin (can put quotes for exact matches)*


After looking around I found an interesting result

*/admin/logged/applicant-schools.php?ID=*


# BOOM!

I was able to see sensitive documents, emails, and messages from other Universities, which were declined an admission, which were approved, why, etc. The reason this works is because there is most likely a **root.php** file on the **admin/logged** panel that’s checking for session, but not the individual **admin PHP files**.

I’m sure there were more vulnerabilities in these admin-only pages, but I wanted something more: **RCE**.

# Part 3: Arbitrary File upload to get a shell

I’m sure you noticed the how universities can apply and send documents to this web server. So perhaps there is an area of Arbitrary File Uploads (**AFU**).

Let’s just google dork since I’m too lazy to traverse the site:

## **BOOM!**

Another route to go down, turns out this endpoint was specifically for universities and not for public-use, but was still indexed on Google. As a result there was no file extension checks and I simply uploaded a **PHP web shell**.

## Where is the Shell?

The only issue is I need to trigger this shell in order to get RCE, I have a ready-to-go shell, just don’t know where it is. Remember, **directory listing**?

After looking around for a bit I finally found the directory that stores the uploads: “**admin/logged/images/applications/myshell.php**”

Well, we found some sensitive files. The web-server had really good firewall rules and I was not able to pop a shell whatsoever. Moreover, this is a limited account and I had very little read permissions.

# Part 4: Stored XSS on Admin Page

I’m 90% sure there exists a stored XSS on the admin page because we’re able to send membership requests as a university and the text does not seem to be sanitized. However, I concluded my testing as the admin page should never be facing the internet anyway, moreover, I explained to them a full-recode of the admin panel and configurations was necessary.
