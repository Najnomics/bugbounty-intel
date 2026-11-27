# Subdomain Takeover

- **Source URL:** https://medium.com/@orkhan_alibayli/subdomain-takeover-95646de1f436?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20230202215327/https://medium.com/@orkhan_alibayli/subdomain-takeover-95646de1f436
- **Fetched:** 2026-11-27
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/942 (id 942)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Subdomain Takeover

# 1. Underlying reason which causes subdomain takeover vulnerabilities

## CNAME record and subdomain takeover

CNAME record is simply an alias of a given domain. For example, let’s say we have a root domain by the name *example.com* and we want to create a subdomain called *sub.example.com*. The content of this subdomain can be stored in different places like Azure virtual machine, GitHub pages and etc. For this situation, I assume the contents of *sub.example.com* is served by GitHub pages called *sub.github.io*. In most situations, a DNS query for domains returns the IP address of the server where the contents are served ( this is called A record ). But since we want our DNS query to return the IP address of *sub.github.com* ( Actually this is not exactly the IP address of our subdomain. This is the IP address of *github.io*. HTTP requests arrive at our subdomain with the help of a concept called virtual hosts which I will explain in the next sections ). For this purpose we create CNAME records that point to *sub.github.io* as described below:

Until our *sub.github.com* page was deleted for some reason everything works fine. We are typing *blog.example.com* in our browser. DNS query returns us the IP of GitHub pages (this process is transparent for browsers. That is why although returned IP belongs to another domain browser does not notice it) and we are getting our web page. But if the page does not exists 404 status code is returned. Real danger begins right there. The Danger is that since our subdomain is unclaimed in GitHub pages anybody can create a GitHub page and link our subdomain (*sub.example.com*) to a fake page. This is the overview of the subdomain takeover.

The general steps for detecting subdomain takeovers are these:

- Find all subdomains of the given domain
- Request DNS queries for CNAME records
- Send HTTP requests for returned URLs by DNS requests and check for HTTP status code 404.
- Detect service type ( AWS, Azure, GitHub, Heroku and etc. ). Detecting is important because subdomain takeover is not possible in some services.
- Alert

# 2. Subdomain enumeration

There are different methods for subdomain enumeration. But I will cover methods which I have used:

## Certificate transparency

Every issued certificate by certificate authorities has to be logged and shared publicly for preventing wrong certificate issuances. CT (Certificate Transparency) also provides a method for the owner of the domain to monitor any issue about the domain. One of the most popular websites for monitoring CT is this site: [https://crt.sh](https://crt.sh/). Here is an example from this site:

As you can see from the image above when I created a subdomain with the name *blog.orkhan-alibayli.com* and when the certificate was issued to this subdomain it was logged. So this is a great way for finding subdomains that use TLS. But we can not use this method for finding all of the subdomains of a given domain because this method works only when the domain does not use wildcard certificates.

As you can see if Google would only use a wildcard certificate for all of its subdomains there will be no way for us to detect these subdomains. But Google uses certificates that are not wildcard for some of its subdomains. These certificates are only for these specific subdomains which is why we can detect these subdomains with the help of CT. But subdomains that don’t have specific certificates can not be detected via CT. These are the cons of subdomain enumeration with CT.

The reason for not using one wildcard certificate for all subdomains is security. For example, if Google uses one wildcard certificate for one of the subdomains which is not important ( this is possible because companies can have a few thousand subdomains, even more ) and if an attacker somehow compromises this server which serves the subdomain then the attacker can decrypt all data which encrypted by this certificate. That is why using wildcard certificates for all domains can be dangerous.

## DNS Brute forcing

DNS brute forcing is used for domains that can not be detected by CT because of wildcard certificates. The process of sending DNS requests for potential subdomains which are from wordlists and then checking DNS query statuses is called **DNS brute forcing**. The basic idea is something like below:

If the query gets NXDOMAIN status this means the subdomain does not exist. NOERROR status means the query resolved successfully. This is the main principle behind DNS brute forcing ( Actually there are also other status codes that means different things. For simplicity I used only 2 status codes ). But there is one problem which is wildcard DNS records. For example, if I have *\*.orkhan-alibyali.com* record every DNS request for subdomains will return valid responses (*thisisdoesntexist.orkhan-alibayli.com*). However, DNS brute-forcing tools can detect it using some techniques.

## Tools for subdomain enumeration

## \* OWASP Amass

I am using Amass for subdomain enumeration since its success rate ( this is my opinion ) is higher than other tools. For enumeration purposes, amass uses CT, and scrapping in different search engines. Also with API keys, it can use VirusTotal, GitHub, SOCRadar, and many other platforms for intelligence purposes.

## \* MassDNS

MassDNS is a high-performance tool for resolving a high amount of DNS queries. We can use MassDNS for detecting subdomains that can not be detected by CT transparency tools because of wildcard certificates.

# 3. Verifying Subdomain takeover vulnerability

## - Different behavior by service providers ( for example virtual host-based service, or only CNAME based )

Let’s assume, we have CNAME record like below (*example.github.io*) for the domain *blog.orkhan-alibayli.com*:

In this situation, for some services, I should enter a canonical name, but for some services, I should enter my subdomain (in this case *blog.orkhan-alibayli.com*). The reason for this difference is that some services use an HTTP host header but some services do not. For services that do not use an HTTP host header, I do not know exactly how the server returns desired App. But for HTTP host-based services process is described below:

# 4. Second-order subdomain takeover

When a website uses third-party domains for some contents ( for example, a javascript file ) and if this domain is vulnerable to subdomain takeover then we can inject malicious javascript files to web pages that use this domain. To detect this vulnerability we should get all domains used by the site and check for subdomain takeover as described in previous steps.

**Thank you very much for reading.**

**You can find me on my LinkedIn page.**
