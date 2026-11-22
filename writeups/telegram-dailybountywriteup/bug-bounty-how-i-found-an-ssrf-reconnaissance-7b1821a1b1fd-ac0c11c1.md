# Bug Bounty { How I found an SSRF ( Reconnaissance ) }

- **Source URL:** https://srahulceh.medium.com/bug-bounty-how-i-found-an-ssrf-reconnaissance-7b1821a1b1fd?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20220906205543/https://srahulceh.medium.com/bug-bounty-how-i-found-an-ssrf-reconnaissance-7b1821a1b1fd
- **Fetched:** 2026-11-22
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/136 (id 136)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Bug Bounty { How I found an SSRF ( Reconnaissance ) }

Hello everyone, I am [**S Rahul**](https://www.linkedin.com/in/7srambo/), working as a **Information Security Analyst** at NUK 9 Auditors and A Bug bounty hunter at Hackerone, Bugcrowd etc. A well-rounded IT professional with 2+ years of cyber security experience.

Today I am going to discuss my recent finding, which is Server-Side Request Forgery (SSRF) to Internal Port Scanning.

**What is SSRF ?**

**Server-side request forgery (also known as SSRF)** is a web security vulnerability that allows an attacker to induce the server-side application to make HTTP requests to an arbitrary domain of the attacker’s choosing. In typical SSRF examples, the attacker might cause the server to make a connection back to itself, or to other web-based services within the organization’s infrastructure, or to external third-party systems. SSRF attacks often exploit trust relationships to escalate an attack from the vulnerable application and perform unauthorised actions. These trust relationships might exist in relation to the server itself, or in relation to other back-end systems within the same organization. To learn more, you can refer to the [PortSwigger Web Security Academy](https://portswigger.net/web-security/ssrf).

**What exactly is WaybackURLs (Wayback Machine)?**

Web crawling in security testing is an important aspect as this is the process of indexing data on web pages by using automated scripts or crawling programs. These scripts or crawling programmes are known as web crawlers, spiders, spider bots, and crawlers. **Waybackurls** is also a Golang-based script or tool used for crawling domains and fetching known URLs from Wayback Machines, also known as Archives for \*.target.com.To learn more about waybackurls and the installation process, you can refer to [waybackurls](https://github.com/tomnomnom/waybackurls).

**Let’s begin with our main topic i.e. how I found an SSRF using Reconnaissance.**

I have selected a bug bounty program through [*Google Dorks*](https://github.com/sushiwushi/bug-bounty-dorks/blob/master/dorks.txt). Due to their responsible disclosure policy, I can’t disclose the program. Let us call the domain as target.com.

First, I did subdomain enumeration through the [subfinder tool](https://github.com/projectdiscovery/subfinder) and saved the output in domains.txt. After that, I ran the [httpprobe tool](https://github.com/tomnomnom/httprobe) on domains.txt to get the live domains and saved the output in live\_domains.txt.

*subfinder -d target.com > domains.txt*

*cat domains.txt | httprobe > live\_domains.txt*

Now I run the following command to collect web crawling urls through waybackurls.

*cat live\_domains.txt | waybackurls > urls.txt*

Once I collected all the urls in urls.txt , I ran the [httpx tool](https://github.com/projectdiscovery/httpx) to identify the status, title, tech, etc. and saved the output in status.txt.

*cat urls.txt | httpx — status-code-title > status.txt*

Now I have sorted all the URLs that are live and accessable, and I have removed all the non-working URLs. That makes my recon simple.

I opened the status.txt and started looking for sensitive information, parameters, usernames, passwords, tokens, sensitive files, etc.

*Keywords I used : password, username, mail.com, token, access\_token, url=, redirect\_url=, api, id=, accessUrl=, payment, etc.*

After 30 minutes of crawling and sorting, I got one interesting url that is like

[https://subdomain.target.com/webinar/?roomId=1ec1f5d8-0887-4fbb-a3dc-1b9f94bc04dc&displayName=mack&accessToken=sda3-q23aed-aerae&peerId=123123-321as-waaew-ads&api](https://subdomain.target.com/webinar/?roomId=1ec1f5d8-0887-4fbb-a3dc-1b9f94bc04dc&displayName=mack&accessToken=sda3-q23aed-aerae&peerId=123123-321as-waaew-ads&api) Event=https://example.com/api/meet&accessUrl=https://example.com/api/accessCheck/&itisparticipant=true&nameScreenDisabled=true&startWithFS=true&controlsDisabled=true

My attention was drawn to the parameters “**apiEvent**” and “**accessUrl**””

Now i have replaced the parameter urls with my Burp collabartor server

After replacing with burp collab server, Url look like this:

Now I opened the url in the browser and I got DNS and HTTP on my collabartor server with their internal IP

Now i have done whois to confirm whether this IP address is of their organisation or a third-party. 

**whois ip**

I got confirmation that the IP I got is the internal IP of the organization.

Now quickly to increase the impact, I have fired my burpsuite and 1. captured the same request in burpsuite > 2.sended it to the intruder >3. selected a pitchfork attack type > 4.position payload added at ended of 2 urls >5.Set the loop request to 100 > 6.Started the attack > 7. I got http,dns,smtp requests

Now I got DNS and HTTP requests, as well as an SMTP request in my Burp collab server, confirming that I was able to perform internal port scanning using the SSRF vulnerability.

I quickly made the poc and reported it to the bug bounty program.

**Reported :** Aug 5, 2022

**Response :** Aug 12, 2022 *Hello! We would like to ask you, what is the best way to exploit this vulnerability? What consequences do you see in using this vulnerability? is it just information disclosure or it can be exploited somehow else?*

**Reported:** *Given a brief information, what an attacker can do by this vulnerability and what are possible ways to exploit it such as Consequences of the SSRF vulnerability :- SSRF leads to Internal IP disclosure, SSRF leads to Internal Port scanning*

**Response:** Aug 18, 2022 Triage and *Rewarded with $$$ bounty*

Thanks for reading guys.

Don’t forget to follow and connect with me through [***Instagram***](https://www.instagram.com/7srambo/), [**LinkedIn**](https://www.linkedin.com/in/7srambo/), [***Twitter***](https://twitter.com/7srambo) .
