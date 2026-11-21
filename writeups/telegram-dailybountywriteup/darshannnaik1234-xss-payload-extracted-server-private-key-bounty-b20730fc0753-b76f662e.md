# XSS Payload Extracted Server Private Key | $$$ Bounty

- **Source URL:** https://medium.com/@darshannnaik1234/xss-payload-extracted-server-private-key-bounty-b20730fc0753?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250315140038/https://medium.com/@darshannnaik1234/xss-payload-extracted-server-private-key-bounty-b20730fc0753
- **Fetched:** 2026-11-21
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/9066 (id 9066)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# XSS Payload Extracted Server Private Key | $$$ Bounty

Hey guys this is the Darshan aka dashanhackz from the Instagram. I was found the amazing vulnerability in the European website program by the intigrity and that would take me to the $$$ bounty.

I started my bug hunting journey to get some hall of fame and show them on the twitter but after adhering my 3rd target from the intigrity I decided to hunt for the money and within this program I got my first bounty of my life i.e, $$$ worth.

Here is the thing , I have made a common methodology that every hacker made to find the most of the vulnerabilities on the targets. Here with that same methodology I have found a amazing vulnerability that will leads to get the server data.

First with the help of the some of the tools I tried to find out the subdomain of the target :

Here I Used the Subfinder tools

## $ subfinder -d domain.com | tee sub.txt

Here we will store all the subdomain into the sub.txt file.

Now as per the subdomains I have found that the file having the mutliple subdomain with the most of the targets are having the false non running subdomain means those are not alive on the server. So here I need to fix though things with the httpx tool.

For the live domains or the subdomain list we will use the httpx tool for live data access.

## $ cat sub.txt | httpx | tee alive.txt

Here with the help of the reading of the files of the subdomain you have to find the live targets those are stored in the server.

Now After getting the subdomain every target is the new targets for us. Yess this has been taught by my mentor Mr. Akash Pawar a brilliant hacker. Now after this we have to find the is there any subdomain takeover by chance is missing by the developer or not. Ya network engineer in the server leads to map the CNAME with the subdomain to the main server but my mistakenly sometimes the server pointing CNAME Expired so there we have to use the subzy tool to get the all the list of subdomain and scanned those subdomain and checkout if its vulnerable or not.

## $ ./subzy — target \<file.txt> // Here the file will be our alive.txt and sub.txt

Mostly I will recommend you to add the alive file only cause that will give you the less false positive result

Here after scanning the whole file of the subdomain we can easily find out that here we will have more false positive result. But how did I find out. I will tell you.

After Scanning the data of the alive.txt file we found that there are 5 subdomain those are vulnerable and can be used for the subdomain takeover. Then by checking the CNAME record of the each subdomain with the help of the dig command.

## $ dig \<sub-domain.domain.com>

Here will find out the CNAME record of the domain and where it is pointing.

Here found that all the vulnerable subdomain those are carried out for the subdomain takeover vulnerability that are having the valid pointing to the domain that is having the live and active CNMAE.

After this go for the Katana tools and find out all the endpoints those are present within the website target or the domain with. Mostly for the web crawling this tool is used by many security researcher.

## $ katana -list \<alive.txt>

From the katana we will find out the all the endpoints of the target.

After that I was disappointed and started the manual pentesting.

First after opening the domain. Lets get all the web request and traffic into the burpsuite for the better site map and having the parameterized request.

In the proxy tab we have to click on the http history.

Proxy -> http history

or

Target -> site map

Now from here lets left click and select the parameterized request only within the tab of the http history.

Here we are searching parameterized request due to only one reason. Cause the thing is the all the parameterized request can be used for the attack and payload insertion.

Here there is one input field within the target website and that was having the wildcard in the bug hunting program but still let it be. I was targeted for the low bounty only cause I don’t having the idea of the bug it was a normal or not.

Lets come to point yeah. I found out that there is one input field that is having the search query parameter and that will captured on the burp so here I tried for the basic xss payload.

Now go by points to point.

- I found the input field
- I tried to place a xss payload within the each query request.
- Here we tried all the payloads those are available on the git.
- Still Didn’t found the xss then try for the encoding
- I decided to build base64 payload on “>\<img src = x onerror=alert(document.cookie)>
- Now after sending this payload to from the burp I got 200 OK with some glitch.
- Here I take that response in the browser
- After opening response in the browser we found out that one file is getting downloaded.
- I found some of the sensitive data of the server via those file.

After finding the sensitive data from the file I was very happy to have the sensitive data finding in the file website so I decided to upload PoC of this to the intigrity bug hunting platform. As far as I got the sensitive information I submitted this bug as the medium vulnerability.

After reviewing the report they decided to make it low.

I was very disappointed when they set this vulnerability to low but after adding one more triage analyst from the intigrity they have found that there is a vulnerability which will leads to get the server RSA key id with the same methodology and they directly converted the vulnerability as LOW -> HIGH , after converting from LOW to HIGH vulnerability they give me $$$ bounty as a token of appreciation.

So this was my first bounty journey within the bug hunting journey.

I hope you will like it. If you like please follow me on the twitter @Darshan\_Cyber and Instagram @darshanhackz.

Thenkssssss !!!!!!
