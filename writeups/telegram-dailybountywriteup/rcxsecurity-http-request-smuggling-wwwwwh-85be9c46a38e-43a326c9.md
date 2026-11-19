# http request smuggling wwwwwh 85be9c46a38e

- **Source URL:** https://medium.com/@rcxsecurity/http-request-smuggling-wwwwwh-85be9c46a38e?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20240306181818/https://medium.com/@rcxsecurity/http-request-smuggling-wwwwwh-85be9c46a38e
- **Fetched:** 2026-11-19
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/5474 (id 5474)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# HTTP Request Smuggling: WWWWWH?

Next up in the WWWWWH series, we’ll be jumping into the Who, What, When, Where, Why, and How of HTTP Request Smuggling. If you’re new here, the purpose of this series is to move past the *How* to exploit a vulnerability that so much hackers focus on. Instead, we’ll explore the vulnerability from a holistic, end-to-end perspective to understand not only how to approach the attack in a real life-scenario, but also how to weaponize Request Smuggling while performing research.

# HTTP Request Smuggling

HTTP Request Smuggling is a web vulnerability that takes advantage of a request chaining mechanism between servers that so many applications use today. It’s not very common to see a request go straight from a user’s browser to a backend server anymore. Instead, a request will generally be chained between different servers, like load balancers and reverse proxies. Attackers take advantage of this chaining by sending ambiguous requests, attempting to make the front end and back end servers interpret them differently. They do this by leveraging the *Content-Length (CL)* and *Transfer-Encoding (TE)* headers in a request to cause a miscommunication.

- *Content-Length*: Specifies the length of the message body in bytes.
- *Transfer-Encoding*: Specifies the message body uses chunked encoding, meaning it’s sent in one or more chunks.

Since a request can use both a CL and TE header, attackers craft requests with conflicting headers, probing for discrepancies in handling the request between the Front-End and Back-End.

If you’re interested in learning more about other vulnerabilities, here are some quick links to other articles in the WWWWWH series:

Or, if you’re interested in Daily Cybersecurity and Tech content, check me out on [Twitter/X](https://twitter.com/rcxsecurity)!

# WWWWWH Analysis

**Who?**

When performing a Request Smuggling attack, it is extremely difficult to target any single individual, especially if found in a popular production application. Your smuggled request will be appended to the beginning of the following request, meaning the victim will end up being the next user to send a request Due to the nature of this attack, exploitation of this vulnerability will have a broad audience.

**What?**

This attack is targeting a configuration miscommunication between servers, causing the HTTP requests to be interpreted differently. This can come in three different attack vectors:

- *CL.TE* — Front end uses CL, Back end uses TE
- *TE.CL* — Front end uses TE, Back end uses CL
- *TE.TE* — Front end and back end support TE, but one can be induced to not process the header through obfuscation.

As mentioned above, web apps commonly chain requests between servers before hitting the backend, each one parsing the request and determining the start/end of each. If both servers don’t agree about boundaries, an attacker can send ambiguous requests that take advantage of this miscommunication. This results in requests being interpreted differently by the front end and back end.

We’ll be specifically covering this vulnerability when downgrading requests from *HTTP/2* to *HTTP/1.1* — as the vulnerabilities in *HTTP/2* are slightly different and more difficult to exploit.

**When?**

If the goal is to serve this attack to massive amounts of people, this attack is best served when the target application is in peak hours. However, you might have better success detecting the vulnerability in off-hours, since you’ll need to send two requests in quick succession in order to process the smuggled request yourself to verify its viability. But, after verification of the vulnerability, you’ll be able to smuggle a request to another user. As long as you wait a reasonable amount of time for another user to send a request, (this time delay would vary depending on the application and traffic) you can deliver the attack — otherwise you would smuggle the request to yourself.

**Where?**

Since this attack is leveraging a discrepancy in processing requests between servers, you’ll need to first identify this vulnerability is present through reconnaissance testing. You can kick off scans via BurpSuite in order to automate this detection, but it is likely that some manual testing may be required. The primary way of testing for this vulnerability is to send requests of the different attack types and look for an observable time delay. You can deliver these payloads over the internet from the comfort of your own home, like the rest of the vulnerabilities we have covered in this series.

**Why?**

The purpose of performing this attack is often to bypass front-end security controls, bypass client authentication, or to gain unauthorized access to exfiltrate sensitive data. However, this attack is generally going to need to be chained with other vulnerabilities to achieve maximum impact. Some common vulnerability chains are session hijacking, [reflected XSS](https://www.cyberseccafe.com/post/reflected-cross-site-scripting-xss-wwwwwh), internal/open redirect, [web cache poisoning](https://www.cyberseccafe.com/post/web-cache-poisoning-wwwwwh), and remote file inclusion to execute remote commands. You can also use this to simply capture other user’s requests to find other valuable information. While a difficult vulnerability to find and exploit in the wild, it is nonetheless something to be extremely weary of.

**How?**

There are 3 different kinds of attacks, so we’ll walk through the basics of detection and exploitation for each.

*CL.TE*

As mentioned above, this vulnerability occurs when the front end processes the Content-Length header, and the back end processes the Transfer-Encoding header. To test for CL.TE, you can send a request that looks like the following:

```
POST / HTTP/1.1
Host: cyberseccafe.com
Transfer-Encoding: chunked
Content-Length: 4
1
F
X
```
If a vulnerability is present, this request will trigger a noticeable time delay in the response because it sends a chunked request with a hanging byte on the end. The server will process the first chunk and wait for the next, causing the delay.

*Quick Tip:* I’d recommend pasting this request in your BurpSuite and highlighting the body to understand where the Content-Length cuts off. Since the length is 4, it will leave the X hanging.


We can send a basic request like the following to fully confirm the vulnerability.

```
POST /search HTTP/1.1
Host: cyberseccafe.com
Content-Type: application/x-www-form-urlencoded
Content-Length: 50
Transfer-Encoding: chunked
ff
q=smuggler&z=
0
GET /404 HTTP/1.1
Foo: z
```
In this example, the Front End will process the Content-Length. This amount ends up being to the end of of the line Foo: z. However, the backend processes the Transfer-Encoding header, meaning that it thinks the request is chunked. This means, it believes the first request cuts off at 0 and the GET /404 request is completely separate. So, if this vulnerability is present, sending a second request after the first will return a 404 error — confirming a CL.TE request smuggling vulnerability is present.

*TE.CL*

The TE.CL attack will be opposite of the CL.TE, meaning the front end interprets the Transfer-Encoding header, and the back end uses the Content-Length. Lets send a request like the following:

```
POST / HTTP/1.1
Host: cyberseccafe.com
Transfer-Encoding: chunked
Content-Length: 6
0
X
```
Here, the front end processes TE and treats the 0 as if it’s terminating the request, leaving the X as the hanging chunk. The server will be expecting more content, so it will cause an observable time delay.

If you send the same request again, it should attempt an XPOST method, appending the hanging chunk to the beginning of the following request.

Once observed, you can send the following POC to confirm the found vulnerability:

```
POST /feature HTTP/1.1
Host: cyberseccafe.com
Content-Type: application/x-www-form-urlencoded
Content-Length: 4
Transfer-Encoding: chunked
8f
GET /404 HTTP/1.1
Host: cyberseccafe.com
Content-Type: application/x-www-form-urlencoded
Content-Length: 130
z=
0
```
Breaking down this request, the front-end interprets the TE header, meaning it believes the entire request is sent and it is waiting for more. However, the back end is processing the CL header, meaning that it believes the first request ends at 8f, and GET /404 is the beginning of a new request. So, when the next request gets sent, it will append that GET /404 request to the beginning of the next, and return a 404 error to the victim.

*TE.TE*

The last example of a Request Smuggling attack is when both front end and back end support the Transfer-Encoding header. As an attacker, you can use obfuscation of the TE header to attempt to induce either the front end or back end to not process it. You can then smuggle in a second request like shown above.

Some obfuscation examples are:

Transfer-Encoding: xchunkedTransfer-Encoding : chunkedTransfer-Encoding: chunked

Transfer-Encoding: xTransfer-Encoding:\[tab\]chunked\[space\]Transfer-Encoding: chunkedX: X\[\n\]Transfer-Encoding: chunkedTransfer-Encoding

: chunked

# WWWWWH

As you can see, Request Smuggling is quite the complex vulnerability, but this WWWWWH analysis of it should have helped shed some light on how it works while researching! Remember, when testing for these vulnerabilities, it’s possible to mess up production environments. So, it’s important to be careful to not DoS the systems or take down the service. We’re researchers, not malicious actors! To protect against this, it’s important to make sure that your front end and back end systems are on the same page, and the threat will be mitigated!

If you enjoyed this analysis of the HTTP Request Smuggling vulnerability, you can find more vulnerability analysis under the WWWWWH tab on my website! As always, this material is meant to be used for educational purposes and not for malicious practice.
