# How I Got Paid for Turning an Image Fetcher into an Arbitrary File Read

- **Source URL:** https://medium.com/@raahil.mw/how-i-got-paid-for-turning-an-image-fetcher-into-an-arbitrary-file-read-0d15679bae00
- **Fetched from:** https://medium.com/@raahil.mw/how-i-got-paid-for-turning-an-image-fetcher-into-an-arbitrary-file-read-0d15679bae00?source=rss-cd682ef574e3------2
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14938 (id 14938)
- **Method:** medium-rss-feed (full content:encoded) readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- **Author/Published (RSS):** Raahil Muhammad Wildan / Wed, 07 Oct 2026 14:16:21 GMT

*Disclosure note: The affected organization and infrastructure have been anonymized. All examples use example.com. The vulnerability was fixed before publication.*

While testing a web application, I found an endpoint that accepted an image URL and returned the result as Base64 data.

The feature looked simple: provide an image URL, let the server fetch it, and receive the encoded image in the response.

While testing how the endpoint handled different URLs, I discovered that it accepted the file:// scheme. This allowed me to replace the image URL with a path to a local file on the server.

The application read the file and returned its contents in the same response field normally used for images.

The affected endpoint was:

POST /api/v1/image-base-64

It accepted an image parameter:

image=https://example.com/image.png

The server fetched the supplied URL and returned the result as Base64 inside data.image.

Base64 is an encoding format. Anyone who receives the encoded value can decode it and recover the original content.

I started by checking whether the server fetched URLs on behalf of the user.

curl -sk \

-u '\<REDACTED\_USERNAME>:\<REDACTED\_PASSWORD>' \

-X POST \

--data-urlencode 'image=http://httpbin.org/ip' \

'https://example.com/api/v1/image-base-64'

After decoding the Base64 response, I received:

```
{
  "origin": "<SERVER_EGRESS_IP>"
}
```
The returned IP confirmed that the request came from the application server.

This behavior is known as server-side request forgery, or SSRF. It happens when an application makes a request to a destination controlled by the user.

URLs begin with a scheme that tells an application how to access a resource. Web applications usually work with http:// and [https://.](https://.)

The file:// scheme is different. It tells the application to open a file from its own filesystem.

I replaced the HTTP URL with a local file path:

curl -sk \

-u '\<REDACTED\_USERNAME>:\<REDACTED\_PASSWORD>' \

-X POST \

--data-raw 'image=file:///etc/hostname' \

'https://example.com/api/v1/image-base-64'

The server returned another Base64 value. After decoding it, I recovered the server’s hostname.

I repeated the test with:

file:///etc/os-release

The decoded response contained operating-system information from the server. This confirmed that the API could read local files and return their contents to the caller.

The application blocked some obvious paths.

A direct request for /etc/passwd returned HTTP 403:

file:///etc/passwd

The filter could be bypassed by changing how the same path was written:

file:///etc/./passwd

file:///etc//passwd

file:///etc/pass%2577d

These variations returned HTTP 200.

The first payload uses a dot segment, the second adds an extra slash, and the third uses URL encoding. The application eventually normalized them to the same file path.

After decoding the response, I confirmed that it contained entries from /etc/passwd.

The filter appeared to inspect the raw input for blocked words. It did not account for the value that the application would produce after decoding and path normalization.

The complete attack required only a few steps:

Testing a sensitive configuration path

The application used CodeIgniter, which commonly stores database settings in:

application/config/database.php

I confirmed that this file existed and produced a non-empty response. I did not decode or extract its contents because it could contain database credentials.

This proved that application configuration files were reachable. It did not prove that the file contained valid credentials or that a database could be accessed.

No attempt was made to connect to a database or use any potentially exposed secrets.

The confirmed impact was an arbitrary local file read on the UAT server.

An attacker could read files available to the application’s operating-system user. Depending on the server configuration, this might expose:

Further compromise would depend on what those files contained. I did not test those possibilities.

The endpoint allowed the user to control the URL scheme. Since file:// was accepted, the server could be instructed to open local files.

The path filter also relied on blocked keywords and exact string patterns. Encoding and normalization created different strings that resolved to the same file.

The endpoint then returned the complete file content through its normal Base64 response.

An image-fetching endpoint should only accept the protocols required by the feature, usually http:// and https://. Schemes such as file://, gopher://, and ftp:// should be rejected.

The application should normalize the URL before validating it. HTTP destinations should be checked against private, loopback, link-local, and cloud metadata addresses. The same checks should run again after every redirect.

The endpoint should also confirm that the response is a valid image and enforce a reasonable size limit.

A WAF can provide another layer of protection, but the application must decide which protocols and destinations the backend is allowed to access.
