# SSRF methodology by Aakash Rathee

- **Source URL:** https://iamaakashrathee.medium.com/ssrf-methodology-by-aakash-rathee-f175665e2ea?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20260915142450/https://iamaakashrathee.medium.com/ssrf-methodology-by-aakash-rathee-f175665e2ea
- **Fetched:** 2026-11-27
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/2444 (id 2444)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# SSRF methodology by [Aakash Rathee](https://medium.com/u/76558046434?source=post_page---user_mention--f175665e2ea-----------------------------------------)

Hi, I’m Aakash Rathee, a **Security Engineer III at Esper**. I work on a variety of security topics, including Application Security, Cloud Security, and DevSecOps. Additionally, I enjoy participating in bug bounty programs as a way to stay sharp and learn about new vulnerabilities.

In the world of web application security, one vulnerability that can often be overlooked is **Server-Side Request Forgery (SSRF)**. This vulnerability occurs when an attacker is able to manipulate a web application into making requests on their behalf, potentially allowing them to access sensitive data or services that should be restricted. In this article, we’ll take a closer look at what SSRF is, how it works, and some common techniques for finding it in web applications.

## Methodology:

If you want to check video tutorial of this, you check that here…

**Youtube** : [https://youtu.be/m43nr2t1wQM](https://youtu.be/m43nr2t1wQM)

### Step 1: Subdomain Enumeration

The first step in finding SSRF vulnerabilities is to perform subdomain enumeration on the target web application. This involves identifying all the subdomains associated with the application, which can help in discovering hidden attack surfaces and potential vulnerabilities.

There are a variety of tools and techniques that can be used for subdomain enumeration, including:

- DNS Dumpster
- Sublist3r
- Amass
- Google Dorking
- Certificate Transparency Logs
- subdomainer

Once you have a list of subdomains associated with the web application, you can start to look for potential SSRF vulnerabilities on each of them.

### Step 2: Find Live Domains

Once you have a list of subdomains associated with the web application, the next step is to identify which ones are actually live and responsive. This can be done using tools like HTTPX, which can quickly test a large number of domains for responsiveness and HTTP status codes.

To use HTTPX, simply pass it a list of domains to test and it will return a list of responsive domains along with their HTTP status codes. You can then filter out any domains that return error codes or are not responsive, leaving you with a list of live domains that you can test for potential SSRF vulnerabilities.

`cat all-domains.txt | httpx > all-live.txt`
### Step 3: Identify All URLs

Once you have a list of live domains associated with the web application, the next step is to identify all the URLs associated with each of them. This can be done using tools like **gauplus**, which can crawl a website and identify all the URLs associated with it.

To find all the urls associated with the domains, perform this command.

`cat all-live.txt | gauplus -subs -b png,jpg,gif,jpeg,swf,woff,gif,svg -o allUrls.txt`
### Step 4: Injection Burp Collaborator URL in Parameters

Once you have a list of all the URLs associated with the live domains, the next step is to identify any parameters in the URLs that may be vulnerable to SSRF attacks. One way to do this is to grep for URLs that contain `=` in them, as this is often an indication of a parameter.

And, after finding all the URLs with parameter we need to replace them with **burp collaborator** url with the help **qsreplace** tool.

So the whole command will look like.

`cat allUrls.txt | grep "=" | qsreplace http://troupga5ke78yjdu4hv12s1v2m8dw3ks.oastify.com > ssrf.txt`
Now in the file `ssrf.txt` we have all the urls with parameter replaced by burp collaborator link.

### Step 5: Test for SSRF Vulnerabilities

Once you have injected a Burp Collaborator URL into the parameters of the URLs, the next step is to test each of them for potential SSRF vulnerabilities. One way to do this is to make a request to each of the URLs with follow redirects enabled, using a tool like `httpx`.

`cat ssrf.txt | httpx -fr`
- -fr is for follow redirect.

If any url vulnerable to SSRF will be show in burp collaborator.

### Step 6: How to check which URL is vulnerable

Once you confirmed that ssrf.txt file contains a URL which is vulnerable to SSRF.

Divide the File in multiple files with the following command

`split -l 10 ssrf.txt output_file_prefix`
The above command going to create 10 different file. 

Clear the Burp Collaborator first.

Check each file with the same command mentioned in step 5.

If any interaction shown check each URL manually. (If this file is big, again split it)

That’s all. You get your SSRF vulnerable URL.

**If you like this Article** :

Please Follow me on Medium, LinkedIn and Subscribe to my Youtube Channel.

LinkedIN : [https://www.linkedin.com/in/aakash-rathee-730834125/](https://www.linkedin.com/in/aakash-rathee-730834125/)

Youtube : [https://www.youtube.com/channel/UCfOwaz-7AgowC6FWkqBKV-Q](https://www.youtube.com/channel/UCfOwaz-7AgowC6FWkqBKV-Q)

## Support My Work

If you found this article helpful and would like to support my work, please consider buying me a coffee through the Buy Me a Coffee platform. Your support can help me to continue creating content and improving the quality of my work. You can visit my Buy Me a Coffee page at
