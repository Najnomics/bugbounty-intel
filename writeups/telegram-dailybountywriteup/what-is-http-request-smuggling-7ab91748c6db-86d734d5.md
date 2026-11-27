# what is http request smuggling 7ab91748c6db

- **Source URL:** https://cyberw1ng.medium.com/what-is-http-request-smuggling-7ab91748c6db?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20240731002521/https://cyberw1ng.medium.com/what-is-http-request-smuggling-7ab91748c6db
- **Fetched:** 2026-11-27
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/5952 (id 5952)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# What is HTTP request smuggling?

## In this section, we’ll explain HTTP request smuggling attacks and describe how common request smuggling vulnerabilities can arise. HTTP request smuggling is a technique for interfering with the way a web site processes sequences of HTTP requests that are received from one or more users. Request smuggling vulnerabilities are often critical in nature | Karthikeyan Nagaraj

# What is HTTP request smuggling?

HTTP request smuggling is a technique for interfering with the way a web site processes sequences of HTTP requests that are received from one or more users. Request smuggling vulnerabilities are often critical in nature, allowing an attacker to bypass security controls, gain unauthorized access to sensitive data, and directly compromise other application users.

Request smuggling is primarily associated with HTTP/1 requests. However, websites that support HTTP/2 may be vulnerable, depending on their back-end architecture.

# What happens in an HTTP request smuggling attack?

Today’s web applications frequently employ chains of HTTP servers between users and the ultimate application logic. Users send requests to a front-end server (sometimes called a load balancer or reverse proxy) and this server forwards requests to one or more back-end servers. This type of architecture is increasingly common, and in some cases unavoidable, in modern cloud-based applications.

When the front-end server forwards HTTP requests to a back-end server, it typically sends several requests over the same back-end network connection, because this is much more efficient and performant. The protocol is very simple; HTTP requests are sent one after another, and the receiving server has to determine where one request ends and the next one begins:

# How do HTTP request smuggling vulnerabilities arise?

Most HTTP request smuggling vulnerabilities arise because the HTTP/1 specification provides two different ways to specify where a request ends: the `Content-Length` header and the `Transfer-Encoding` header.

The `Content-Length` header is straightforward: it specifies the length of the message body in bytes. For example:

```
POST /search HTTP/1.1
Host: normal-website.com
Content-Type: application/x-www-form-urlencoded
Content-Length: 11
q=smuggling
```
The `Transfer-Encoding` header can be used to specify that the message body uses chunked encoding. This means that the message body contains one or more chunks of data. Each chunk consists of the chunk size in bytes (expressed in hexadecimal), followed by a newline, followed by the chunk contents. The message is terminated with a chunk of size zero. For example:

```
POST /search HTTP/1.1
Host: normal-website.com
Content-Type: application/x-www-form-urlencoded
Transfer-Encoding: chunked
b
q=smuggling
0
```
As the HTTP/1 specification provides two different methods for specifying the length of HTTP messages, it is possible for a single message to use both methods at once, such that they conflict with each other. The specification attempts to prevent this problem by stating that if both the `Content-Length` and `Transfer-Encoding` headers are present, then the `Content-Length` header should be ignored. This might be sufficient to avoid ambiguity when only a single server is in play, but not when two or more servers are chained together. In this situation, problems can arise for two reasons:

- Some servers do not support the `Transfer-Encoding` header in requests.
- Some servers that do support the `Transfer-Encoding` header can be induced not to process it if the header is obfuscated in some way.

If the front-end and back-end servers behave differently in relation to the (possibly obfuscated) `Transfer-Encoding` header, then they might disagree about the boundaries between successive requests, leading to request smuggling vulnerabilities.

# How to perform an HTTP request smuggling attack

Classic request smuggling attacks involve placing both the `Content-Length` header and the `Transfer-Encoding` header into a single HTTP/1 request and manipulating these so that the front-end and back-end servers process the request differently. The exact way in which this is done depends on the behavior of the two servers:

- CL.TE: the front-end server uses the `Content-Length` header and the back-end server uses the `Transfer-Encoding` header.
- TE.CL: the front-end server uses the `Transfer-Encoding` header and the back-end server uses the `Content-Length` header.
- TE.TE: the front-end and back-end servers both support the `Transfer-Encoding` header, but one of the servers can be induced not to process it by obfuscating the header in some way.

# CL.TE vulnerabilities

Here, the front-end server uses the `Content-Length` header and the back-end server uses the `Transfer-Encoding` header. We can perform a simple HTTP request smuggling attack as follows:

```
POST / HTTP/1.1
Host: vulnerable-website.com
Content-Length: 13
Transfer-Encoding: chunked
0
SMUGGLED
```
The front-end server processes the `Content-Length` header and determines that the request body is 13 bytes long, up to the end of `SMUGGLED`. This request is forwarded on to the back-end server.

The back-end server processes the `Transfer-Encoding` header, and so treats the message body as using chunked encoding. It processes the first chunk, which is stated to be zero length, and so is treated as terminating the request. The following bytes, `SMUGGLED`, are left unprocessed, and the back-end server will treat these as being the start of the next request in the sequence.

# TE.CL vulnerabilities

Here, the front-end server uses the `Transfer-Encoding` header and the back-end server uses the `Content-Length` header. We can perform a simple HTTP request smuggling attack as follows:

```
POST / HTTP/1.1
Host: vulnerable-website.com
Content-Length: 3
Transfer-Encoding: chunked
8
SMUGGLED
0
```
The front-end server processes the `Transfer-Encoding` header, and so treats the message body as using chunked encoding. It processes the first chunk, which is stated to be 8 bytes long, up to the start of the line following `SMUGGLED`. It processes the second chunk, which is stated to be zero length, and so is treated as terminating the request. This request is forwarded on to the back-end server.

The back-end server processes the `Content-Length` header and determines that the request body is 3 bytes long, up to the start of the line following `8`. The following bytes, starting with `SMUGGLED`, are left unprocessed, and the back-end server will treat these as being the start of the next request in the sequence.

# TE.TE behavior: obfuscating the TE header

Here, the front-end and back-end servers both support the `Transfer-Encoding` header, but one of the servers can be induced not to process it by obfuscating the header in some way.

There are potentially endless ways to obfuscate the `Transfer-Encoding` header. For example:

```
Transfer-Encoding: xchunked
Transfer-Encoding : chunked
Transfer-Encoding: chunked
Transfer-Encoding: x
Transfer-Encoding:[tab]chunked
[space]Transfer-Encoding: chunked
X: X[\n]Transfer-Encoding: chunked
Transfer-Encoding
: chunked
```
Each of these techniques involves a subtle departure from the HTTP specification. Real-world code that implements a protocol specification rarely adheres to it with absolute precision, and it is common for different implementations to tolerate different variations from the specification. To uncover a TE.TE vulnerability, it is necessary to find some variation of the `Transfer-Encoding` header such that only one of the front-end or back-end servers processes it, while the other server ignores it.

Depending on whether it is the front-end or the back-end server that can be induced not to process the obfuscated `Transfer-Encoding` header, the remainder of the attack will take the same form as for the CL.TE or TE.CL vulnerabilities already described.

A YouTube Channel for Cybersecurity Lab’s Poc and Write-ups

Telegram Channel for Free Ethical Hacking Dumps

Thank you for Reading!

Happy Ethical Hacking \~

`Author: Karthikeyan Nagaraj ~ Cyberw1ng`
