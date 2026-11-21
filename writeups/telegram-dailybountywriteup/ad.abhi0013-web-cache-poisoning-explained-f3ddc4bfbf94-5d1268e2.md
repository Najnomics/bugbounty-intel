# Web cache poisoning explained

- **Source URL:** https://medium.com/@ad.abhi0013/web-cache-poisoning-explained-f3ddc4bfbf94?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20241101131143/https://medium.com/@ad.abhi0013/web-cache-poisoning-explained-f3ddc4bfbf94
- **Fetched:** 2026-11-21
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/7702 (id 7702)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Web cache poisoning explained

Web cache poisoning involves manipulating the web cache to store harmful content, which is then delivered to other users. The three primary methods used to poison web caches are request smuggling, request splitting, and using unkeyed inputs (also called practical web cache poisoning). This article will focus on cache poisoning through unkeyed inputs, as it is currently the most prevalent method for performing web cache poisoning.

# **How does the caching work ?**

In order to understand what web cache poisoning is and what its consequences are, we need to first take a look at how web caches work. Caching means that you store frequently accessed content in order to speed up subsequent requests to access that content. Some examples of caches include memory caches, DNS caches and web caches.

A web cache operates by temporarily storing HTTP responses according to specific rules. It primarily determines which content to cache by using what are known as cache keys.

Cache keys are elements of an HTTP request that the cache relies on to uniquely identify a response.Typically a cache key consists of the values of one or more response headers as well as the whole or part of the URL path. A typical request can look like this:

`GET` **/totally/real/mysite?do=true** HTTP/1.1

`Host:` **example.com**

`User-Agent: Mozilla/5.0...`

`Accept: */*`

`Cookie: language=en;`

The parts of the request that are bold represent the cache key. If the cache can match the cache key to an existing record in the cache it will respond with that record instead of passing the request along to the origin. This reduces the amount of requests that the origin has to handle, which leads to lower cost for the application owner and often faster response times for users. Web caches can either be implemented locally or through a CDN.

The idea is that cache keys are supposed to reflect any changes to the response. Issues start to happen when parts of the request other than the cache keys can modify the response content.

# **Unkeyed and keyed inputs**

In web caching, **unkeyed inputs** are parts of an HTTP request that a cache server ignores when determining which response to cache, whereas **keyed inputs** are the parts that the cache does consider.

When a cache server only “keys” certain parts of a request, like the URL or headers, while ignoring other parts like query parameters, it can lead to **cache poisoning**. This happens because an attacker can manipulate unkeyed inputs to create a malicious response that the cache saves and subsequently serves to other users.

# Example of Unkeyed vs. Keyed Inputs

Consider a cache server that keys only on the **URL** and **method** of an HTTP request but ignores the **User-Agent** header. Here’s an example to illustrate this:

## Scenario:

1. A cache server receives a request and caches the response based on the URL:

```
GET /example-page HTTP/1.1
Host: www.example.com
User-Agent: Mozilla/5.0
```
2\. An attacker makes a request with an unkeyed input that’s ignored by the cache, such as a `User-Agent` header, but injects malicious content:

```
GET /example-page HTTP/1.1
Host: www.example.com
User-Agent: MaliciousBot/1.0
```
If the `User-Agent` header is not a keyed input, the cache stores this response as if it’s valid for all users accessing `/example-page`, regardless of the `User-Agent` value. This means users requesting `/example-page` will now receive the poisoned content until the cache expires.

By selectively ignoring certain inputs, the cache server becomes vulnerable to **cache poisoning** through unkeyed inputs, as it inadvertently caches and serves the malicious content to unsuspecting users.

# Why does this happen ?

This situation commonly arises when a cache layer is added in front of an application that previously operated without one. If the team implementing the cache is unaware of how specific inputs influence the application’s responses, they might unintentionally leave some utilized inputs unkeyed.

Additionally, many frameworks use request headers to generate responses in ways that developers may not fully realize. Because these frameworks often abstract away low-level handling of request headers, such issues can easily go unnoticed.

# Scenario: Poisoning with Language Header Manipulation

Suppose an e-commerce site allows users to view its content in different languages by detecting the `Accept-Language` HTTP header. However, the site has a caching layer that only keys the cache on the URL and ignores the `Accept-Language` header, making it vulnerable to cache poisoning.

1. **Normal Request from a User**
A legitimate user requests the English version of the home page:

```
GET /home HTTP/1.1
Host: www.example.com
Accept-Language: en
```
- **Response (Cached):** The server returns the English content, and the cache stores it for future requests to `/home`.

1. **Attack Request (Poisoning the Cache)**
An attacker sends a request with the`Accept-Language` header set to a custom value, `fr<script>alert('Hacked')</script>`, to inject malicious code:

```
GET /home HTTP/1.1
Host: www.example.com
Accept-Language: fr<script>alert('Hacked')</script>
```
- **Response (Poisoned):** If the server does not properly handle the `Accept-Language` input, it could respond with the malicious content, which is then cached for the `/home` URL.

```
GET /home HTTP/1.1
Host: www.example.com
Accept-Language: en
```
1. **Subsequent User Requests**
When another user requests the home page without specifying the language or with any language:

```
GET /home HTTP/1.1
Host: www.example.com
Accept-Language: en
```
- **Response (Poisoned Content):** The cache returns the poisoned response containing the malicious code, resulting in a potential XSS attack on the user’s browser.

This scenario highlights how ignoring headers or inputs in cache keys can lead to unintended cache poisoning, potentially exposing users to malicious content.

# Potential impact

Manipulation of web cache contents means that an attacker could potentially target anyone that tries to access the vulnerable application. It can be used to create a [stored XSS](https://blog.detectify.com/2019/03/15/what-are-the-different-types-of-xss/), [open redirects](https://blog.detectify.com/2019/05/16/the-real-impact-of-an-open-redirect/) and Denial-Of-Service depending on what parts of the application are vulnerable.

# How to mitigate it

There are multiple ways to mitigate this type of attack:

- If possible, make sure to only cache static resources. It might not be possible though since this could mean that more traffic is served to the origin which will likely increase cost. Performance might also suffer because of this.
- Find all inputs (headers, cookies and query strings) that are reflected in the response without being part of the cache key. Make sure to either disable them, remove them in the cache layer or add them to the cache key.
