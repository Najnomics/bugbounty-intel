# The easiest way to get subdomain takeover

- **Source URL:** https://medium.com/@AhmedMhesham/easiest-way-to-get-subdomain-takeover-76f444c8ee6f?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20230130223117/https://medium.com/@AhmedMhesham/easiest-way-to-get-subdomain-takeover-76f444c8ee6f
- **Fetched:** 2026-11-27
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/1542 (id 1542)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# The easiest way to get subdomain takeover

# **بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيم**

In the **name** of **Allah**

## First of all what is subdomain takeover?

A subdomain takeover occurs when an attacker is able to claim ownership of a subdomain that is no longer in use or is not properly configured. This can happen when a subdomain is pointed to a third-party service (such as a content delivery network or a cloud service) that is no longer being used, or when a subdomain is not properly configured to point to a valid DNS record. Once the attacker has taken over the subdomain, they can use it to host malicious content or steal sensitive information.

With the help of CNAME, or Canonical Name (it is a type of DNS record that allows a domain or subdomain to point to another domain. This can be used to redirect traffic from one domain to another, or to point a subdomain to a different server).

In the context of subdomain takeover, an attacker can take over a subdomain by creating a CNAME record that points the subdomain to a domain that they control. Once the attacker has created the CNAME record, they can host malicious content or steal sensitive information from visitors to the subdomain


## How do we know that the subdomain is vulnerable?

using [can-i-take-over-xyz repository](https://github.com/EdOverflow/can-i-take-over-xyz) , you will find there the Fingerprint of being vulnerable and the way to take it over


what is Trickest platform?

**A platform enabling bug bounty hunters, penetration testers, and SecOps teams to build and automate workflows from start to finish**.

**the platform gives a free demo for 10 days with 50$ in your wallet**


Automating this process is very easy using [**Trickest.io**](https://trickest.io/) platform. so let’s see how to

1. sign up in Trickest platform

click on get access

2\. type your First Name, Last Name, choose the purpose “bug bounty hunting” and your social media account link and submit

3\. check your email from 1 \~ 3 days

complete your signing up

4\. From Trickest’s Library search for “34”

click on it then choose copy workflow


then create a new space and type a name for it

then create

and choose it then click copy

you will find it in your workflow open it then open workflow

this workflow is for generating subdomains and check the alive of them

from library on the right search for “takeover”

grab 1, 2, 3 to the end of this workflow

and make them like this

using “Library and Inputs”

this workflow well do 3 things

1. generate a subdomains
2. check the alive of them
3. check for subdomain takeover

all you have to do now is copying your domains in pastpin page and take the raw link of it like this

Click here and add your link

now click the save then start button 

check your workflow after it finishes

click on the last tools to see your results

and here we go

I found one.

Best regards,
