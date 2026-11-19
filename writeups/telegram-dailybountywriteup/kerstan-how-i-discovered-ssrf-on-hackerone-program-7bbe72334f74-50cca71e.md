# How I Discovered SSRF on Hackerone Program

- **Source URL:** https://medium.com/@kerstan/how-i-discovered-ssrf-on-hackerone-program-7bbe72334f74?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20240107003731/https://medium.com/@kerstan/how-i-discovered-ssrf-on-hackerone-program-7bbe72334f74
- **Fetched:** 2026-11-19
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/4722 (id 4722)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
**Subscribed to:** [https://medium.com/@kerstan](/@kerstan)

Hi guys, I am Kerstan. Today, I will share you how I discoverd SSRF on hackerone Program.

The process of discovering bugs can be lengthy, but the results are often rewarding. Keep trying harder, bro!

If this writing has been helpful to you, please consider giving it a clap and following. Thanks bro.

So, let’s get started.

# 1. Sensitive endpoint discovered

First, I gathered some business information from the Program scope on Hackerone.

I conducted regular tests such as web bug and IDOR, but I found absolutely no opportunity. The filters and authentication mechanisms were very robust, and users were authenticated using uuid as parameters.

I couldn’t exploit the uuid to cause an IDOR bug.

It’s already the next morning and I haven’t found any bug yet. I decided to take a break and grab a cup of coffee.

I decided to go through Burp’s HttpHistory again to see if there were any sensitive requests that I might have missed.

Wow, finally, I came across a sensitive Graphql request.

```
POST /agw/graphql?op=UrlReachableVerifierQuery&client_trace_id=09bee58d-8358-4f00-acc0-
8d26d0018d32,rst:1678201703792 HTTP/1.1
Host: xxxxx
Cookie: xxxx
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101
Firefox/110.0
Accept: */*
Accept-Language: zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2
Accept-Encoding: gzip, deflate
Content-Type: application/json
Authorization: xxxxx
Content-Length: 386
Origin: 
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: same-site
Te: trailers
Connection: close
{"operationName":"UrlReachableVerifierQuery","variables":{
"url":"http://xxxx.com/"},"query":"query UrlReachableVerifierQuery($url: String!) {\n
verifyUrlReachable(url: $url) {\n
... on UrlReachableResult {\n
__typename\n }\n ... on GenericError {\n
__typename\n }\n __typename\n
```
[https://xxxxx](https://xxxxx)
