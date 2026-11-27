# Client Side Desync Attack (CL.0 Request Smuggling) — Bounty of $150

- **Source URL:** https://bpandasec.medium.com/client-side-desync-attack-cl-0-request-smuggling-bounty-of-150-327d3aeaeea6?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20260226011539/https://bpandasec.medium.com/client-side-desync-attack-cl-0-request-smuggling-bounty-of-150-327d3aeaeea6
- **Fetched:** 2026-11-27
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/2480 (id 2480)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Client Side Desync Attack (CL.0 Request Smuggling) — Bounty of $150

--

*Hello everyone. I’m Bodhendu Panda, a cyber security geek. Today, let’s look at how I was able to find a* client-side desync attack vulnerability on a public bug bounty platform.

**Description**

HTTP request parsing between a reverse proxy and the web application. An unauthenticated attacker may exploit this issue and poison requests of other users, which may lead to various consequences including account takeover.

**Issue background:-**

Client-side desync (CSD) vulnerabilities occur when a web server fails to correctly process the Content-Length of POST requests. By exploiting this behaviour, an attacker can force a victim’s browser to desynchronize its connection with the website, typically leading to XSS.

**Steps to exploit the Vulnerability:-**

I was hunting for a program, and let’s call the subdomain abc.example.com. I have observed that the website has two ports open (80,443).

So I have tried to exploit port 80, and I have noticed that on port 80, I was able to downgrade HTTP/2 to HTTP/1.1. As show in the below image.

Note: It is an CL.0 request smuggling; hence, turn off the auto-update content length from the burp repeater settings.

Now you can change the connection from closed to keep-alive.

Now it’s time to add another request to the repeater to perform request smuggling.

On sending the request in repeater, you can observe that I was able to fetch the response of the second request as well.

Accessing the \`/admin\` path directly returned a 404 response. However, when I included \`/admin\` as the path within a smuggled request (2nd request) and sent both requests (smuggled request and normal requst with path as /) using the Repeater’s group tab, I was able to successfully access the admin dashboard.

**Issue remediation:-**

You can resolve this vulnerability by patching the server so that it either processes POST requests correctly, or closes the connection after handling them. You could also disable connection reuse entirely, but this may reduce performance. You can also resolve this issue by enabling HTTP/2.

**Thank you for reading. I hope you have found the blog helpful. Have a nice day. Happy Hacking!!!. Subscribe to the blog for more walkthroughs, tricks and bug bounty writeups.**
