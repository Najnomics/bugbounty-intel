# Bypassing SSRF Protections

- **Source URL:** https://medium.com/@tobydavenn/bypassing-ssrf-protections-45e5e3ac31e9?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20221231131129/https://medium.com/@tobydavenn/bypassing-ssrf-protections-45e5e3ac31e9
- **Fetched:** 2026-11-19
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/1170 (id 1170)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Bypassing SSRF Protections

Hello,

It has been a while since I last posted. I wanted to share a neat SSRF bypass I found while hunting on a private program.

SSRF stands for server side request forgery. Server side request forgery allows an attacker to abuse HTTP requests to request information about the server internally or internal network.

Things to look out for? Parameters such as url= next= host= image= img= etc. Anything that looks to be making a web request to a server. This can then be abused to point the request internally.

**How did I find the vulnerable endpoint?**

Whilst hunting on a private program, I was doing extensive recon. I had gathered a huge list of subdomains, mainly pulling from censys. After this, I had brute forced and searched in wayback machine for URLs across all hosts. At the time, ssrf was my focus, so I gathered my directory and endpoint output and grepped for “proxy.php”. Luckily I had a hit.

When studying the request, this was making an outbound HTTP request to a specified URL. If I entered my burp collaborator link, I did not receive a lookup. I tried the usual basics, entering 127.0.0.1 and IP notations of internal hosts, each request was blocked unless the request had the websites hostname in it.

This is where things get technical. when sending a request such with my burp collaborator, alongside browser credentials formatting, e.g. url=https://hostnameofwebsite.com@myburpcollablink I got a hit back.

I tried to then exploit this by changing it around because currently the above was using the browser to send hostnameofwebsite as credentials to myburpcollablink, which was no good.

I had recently just seen an ssrf video on google when it was explained if you used a \ this would stop parsing on the backend after the first host. The front end would interpret the request as hostnameofwebsite as credentials to myburpcollablink but the backend would process just the front end request so hostnameofwebsite. Here i changed it around and used url=http://169.254.1698.254\@hostnameofwebsite.

Lets explain. 169.254 is the internal ip address of the AWS metadata. The front end request is seeing this as 169.254 as credentials to hostnameofwebsite, which passes the front end check as hostnameofwebsite must be in the request. The backend ignores this format and processes as [http://169.254.169.254\](http://169.254.169.254\) which then cuts off and passes just the request.

Closed as resolved
