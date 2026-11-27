# SUBDOMAIN TAKEOVER

- **Source URL:** https://medium.com/@ivishnujs/subdomain-takeover-5c4974aa782f?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20220829211243/https://medium.com/@ivishnujs/subdomain-takeover-5c4974aa782f
- **Fetched:** 2026-11-27
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/57 (id 57)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# SUBDOMAIN TAKEOVER

**What are Subdomains?**


A domain name typically has two parts: **The top-level domain (TLD)** is the extension, such as *.com* or *.org*, and the **second-level domain (SLD)** is the unique part of the domain name, often a business or brand name. In the *hubspot.com* example, *com* is the TLD and *hubspot* is the SLD.

The **subdomain** is what goes *before* the SLD. The most common subdomain is *www*, which stands for World Wide Web. This subdomain contains a website’s homepage and its most important pages. The *www* subdomain is so widely used that most [domain registrars](https://blog.hubspot.com/website/best-domain-registrars) include it with domain name purchases.

Subdomains are also commonly used to separate a section of a website from the main site. For example, *blog.hubspot.com* and *shop.hubspot.com* direct to our blog and online store respectively.

**What is Subdomain Takeover?**


A subdomain takeover occurs when an attacker gains control over a subdomain of a target domain. Typically, this happens when the subdomain has a canonical name (**CNAME**) in the Domain Name System (**DNS**) , but no host is providing content for it , or the subdomain is giving a 404 error and no longer available . This can happen because either a virtual host hasn’t been published yet or a virtual host has been removed. An attacker can take over that subdomain by providing their own virtual host and then hosting their own content for it.

E**asy Method to look for Subdomain Takeover**


1. Enumerating all the subdomains using using various tools like [***Amass***](https://github.com/OWASP/Amass)*,* [***SubBrute***](https://github.com/TheRook/subbrute)*,* [***Knock***](https://github.com/guelfoweb/knock)py , **dnsrecon**, [***Sublist3r***](https://github.com/aboul3la/Sublist3r)*,* [***subfinder***](https://github.com/projectdiscovery/subfinder)

2\. Combine all the subdomains found using above and sort them without having duplicates

3\. Lets see from the created list how many of them are live using [***httpx***](https://github.com/projectdiscovery/httpx), *httprobe* and create a new list from the output

4\. To check whether subdomains are vulnerable to subdomain takeover/not, I use tool called [***subzy***](https://github.com/LukaSikic/subzy). ( alternatives [***sub404***](https://github.com/r3curs1v3-pr0xy/sub404), *subjack, tko-subs)*

It shows that particular subdomains are vulnerable to subdomain takeover. Then I check IP address of subdomain to whom it belongs to using whois command.

I tried to open subdomain in browser. Then it give message like below. Message is nothing but fingerprint/pattern that are provided by different cloud providers. To know more about different fingerprint of cloud service providers go to

# **Shopify hosting:**

For subdomain takeover I need to have account on that cloud hosting engine who provide cloud hosting service. In my case it was **shopify**. So I simply created account on shopify.com , which ask your basic info for account creation and it will provide you 14 days trial account, other service providers have different policy.

**Takeover**

Once after creation of account of shopify,

1. Go to **add domain**

2. Click on **Connect existing domain**

3. provide vulnerable **domain name** only (sub.shofify.com)

4. click on **verify connection**.

5. You are able to host any contain (Malicious script/ phishing page and much more) on that subdomain.

# **if the vulnerable subdomain is a Github hosting:**

## Takeover

(Assuming you have GitHub account created.)

1. Go to [new repository](https://github.com/new) page
2. Set *Repository name* to canonical domain name (i.e., {something}.github.io from CNAME record)
3. Click *Create repository*
4. Push content using git to a newly created repo. GitHub itself provides the steps to achieve it
5. Switch to *Settings* tab
6. In *GitHub Pages* section choose *master branch* as source
7. Click *Save*
8. After saving, set *Custom domain* to source domain name (i.e., the domain name which you want to take over)
9. Click *Save*

# If the vulnerable subdomain is a Readme.io hosting:

Readme.io is a popular service for hosting your documentation. As turns out, they also offer custom domain support and more importantly, subdomain takeover is possible using `readme.io` domains.

## Takeover

(Assuming you have Readme.io account created.)

1. Go to [dashboard](https://dash.readme.io/).
2. Set *Project Name* and its *subdomain*. Subdomain does not need to match the domain you are trying to takeover.
3. In left sidebar, go to *General Settings* -> *Custom Domain*.
4. Set *Custom domain* to the domain you want to takeover.
5. Click *Save*.

# If the vulnerable subdomain is a AWS hosting:

Amazon Simple Storage Service (Amazon S3) is a scalable, high-speed, low-cost, web-based cloud storage service designed for online backup and archiving of data and application programs. It is probably the most popular of the AWS services and provides a scalable solution for object storage via WEB APIs. In fact, S3 buckets offer far more versatile solutions than that.Consider the case of a web application that needs a staging area to house content that is to be served to users or maybe hosting of videos, music or other downloadables or maybe you just want to store a backup on the web. AWS S3 has you covered. The image illustrates how a web application makes use of AWS S3 to store media files like pictures uploaded by users or content like JavaScript and CSS that is employed by the application itself.

## Takeover

1. Go to [S3 panel](https://s3.console.aws.amazon.com/s3/)
2. Click *Create Bucket*
3. Set *Bucket name* to source domain name (i.e., the domain you want to take over)
4. Click *Next* multiple times to finish
5. Open the created bucket
6. Click *Upload*
7. Select the file which will be used for PoC (HTML or TXT file). I recommend naming it differently than *index.html*; you can use *poc* (without extension)
8. In *Permissions* tab select *Grant public read access to this object(s)*
9. After upload, select the file and click *More -> Change metadata*
10. Click *Add metadata*, select *Content-Type* and value should reflect the type of document. If HTML, choose *text/html*, etc.
11. (Optional) If the bucket was configured as a website
12. Switch to *Properties* tab
13. Click *Static website hosting*
14. Select *Use this bucket to host a website*
15. As an index, choose the file that you uploaded
16. Click *Save*

REFERENCES:
