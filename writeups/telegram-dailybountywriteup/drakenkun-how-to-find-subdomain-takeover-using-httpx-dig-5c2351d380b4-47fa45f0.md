# how to find subdomain takeover using httpx dig 5c2351d380b4

- **Source URL:** https://medium.com/@DrakenKun/how-to-find-subdomain-takeover-using-httpx-dig-5c2351d380b4?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20260130174617/https://medium.com/@DrakenKun/how-to-find-subdomain-takeover-using-httpx-dig-5c2351d380b4
- **Fetched:** 2026-11-27
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/3864 (id 3864)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# How to find subdomain takeover using httpx + dig

Hello Everyone

Today I found a simple finding vulnerability with high impact that I would like to share it with you , but before we begin we have to know what is subdomain takeover

**subdomain takeover occurs when an attacker gains control over a subdomain of a target domain. Typically, this happens when the subdomain has a canonical name (CNAME) in the Domain Name System (DNS), but no host is providing content for it**


let’s say we have domain called **example.com**

first we have to do subdomain enumeration , I usually use subfinder with editing the API configuration file you can check it on [https://securitytrails.com/blog/subfinder](https://securitytrails.com/blog/subfinder)

`subfinder -d example.com -all -cs > main.txt ; cat main.txt | cut -d "," -f 1 > domains.txt ; rm -rf main.txt`
now we have created a file named **domains.txt** and then we need to check the live subdomains and checking the status code of them

simply we can use httpx tool by typing command

`cat domains.txt | httpx -title -wc -sc -cl -ct -location -web-server -asn -o alive-subdomains.txt` I found interested subdomain with error code 404 that points to “GOOGLE-CLOUD-PLATFORM”

let’s name it **altice.example.com**

after visited that url I found a defualt NOT Found page for “Leadpages services”

Here we start to retrieving information about DNS name servers by dig command

we can type on terminal

`dig altice.example.com`
or visiting [https://www.digwebinterface.com/](https://www.digwebinterface.com/)

in this result we found the CNAME server is **custom-proxy.leadpages.net**

I tried to visit [https://github.com/EdOverflow/can-i-take-over-xyz](https://github.com/EdOverflow/can-i-take-over-xyz) to check if that service is vulnerable or not but unfortunately, I haven’t found it there

But also that doesn’t mean “Leadpages services” isn’t vulnerable

After creating a free trial for 14 days account and you have to put your valid paypal email or valid credit card on [https://www.leadpages.com/](https://www.leadpages.com/)

Start modifying the template and change it to my name as a POC

Here’s the most exciting part

Click on **upadte** > **site publishing options**

put your vulnerable subdomain in our case : **altice.example.com**

click on done

now the ssl will be connected to our custom domain

let’s visit the vulnerable site right now

And I Finally Found My name

while I was writing that writeup I got some ideas of google dorks that may help U

`site:"*.example.com" intext:"PAGE NOT FOUND" | intext:"project not found" | intext:"Repository not found"  | intext:"domain does not exist" | intext:"This page could not be found" | intext:"404 Blog is not found" | intext:"No settings were found for this company" | intext:"domain name is invalid"`
In case you have any questions you can ask me in the comments section and I will asnwer it happily

and don’t forget to follow me in [twitter](https://twitter.com/Amr_MustafaAA) to get useful informations & tips

Thank U ❤
