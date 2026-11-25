# SSRF

- **Source URL:** https://medium.com/@shadow_28/ssrf-a-sneaky-way-to-bypass-url-filters-using-http-redirects-046ff54ce667
- **Fetched from:** https://bugbountywizard.app/ssrf-a-sneaky-way-to-bypass-url-filters-using-http-redirects-046ff54ce667?source=rss-02f14d17c4fe------2
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:**  (id 14959)
- **Method:** medium-rss-feed (full content:encoded) readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- **Author/Published (RSS):** Sumit Raj / Sun, 25 Oct 2026 19:11:08 GMT

Recently when i was hunting for a vulnerability disclosure program, I figured out a new methodology for SSRF bypass.

Suppose a web application has an endpoint:

GET /fetch?url=https://example.com HTTP/1.1

Host: vulnerable-app.com

The application fetches the URL provided in the url parameter.

Internally, its logic might look like this:

import requests

@app.route("/fetch")

def fetch():

url = request.args.get("url")

# Application fetches the supplied URL

response = requests.get(url)

return response.text

The application makes an outbound HTTP request to the supplied URL.

If the application also constructs a shell command using that URL, the vulnerability could involve both:

However, SSRF and command injection are separate vulnerabilities. SSRF allows the server to make requests to unintended destinations, while command injection occurs when attacker-controlled input reaches a command interpreter in an unsafe manner.

Assume the application has a firewall or input validation rule that blocks suspicious characters and command patterns.

For example, you submit:

GET /fetch?url=https://example.com/?cmd=$(id)

The firewall detects the suspicious payload:

$(id)

The request is blocked.

HTTP redirects use response status codes such as:

A server can respond with a 302 and a Location header that tells the HTTP client where to make its next request.

For example:

HTTP/1.1 302 Found

Location: https://example.org/next

If the client follows redirects, it makes another request to the URL specified in the Location header.

This introduces an important distinction:

The URL submitted to the application is not necessarily the URL ultimately requested by its HTTP client.

Suppose you control a test redirect server.

The server receives a request to:

GET /redirect HTTP/1.1

Host: redirect.example

It responds:

HTTP/1.1 302 Found

Location: https://destination.example/resource

The application initially sees:

https://redirect.example/redirect

But the HTTP client may subsequently request:

https://destination.example/resource

The complete flow is:

Consider an application that performs validation like this:

```
url = request.args.get("url")
if "localhost" in url:    
    return "Blocked", 403
if "127.0.0.1" in url:    
    return "Blocked", 403
response = requests.get(url)
```
The validation only checks the original input.

If the application accepts a URL pointing to a redirect server, it may validate:

Then the HTTP client follows the redirect to another destination.

The application might never validate the destination URL.

This is a redirect validation gap.

The security issue is not that redirects are inherently malicious. The issue is that the application trusts a URL before redirect processing and does not revalidate the destination afterward.

Let’s reproduce the redirect behavior without command injection or access to internal services.

We’ll use two local HTTP servers:

Create destination.py:

from http.server import HTTPServer, BaseHTTPRequestHandler

class DestinationHandler(BaseHTTPRequestHandler):

def do\_GET(self):

print("Destination received:", self.path)


self.send\_response(200)

self.end\_headers()

self.wfile.write(

b"Hello from destination server"

)

server = HTTPServer(

("127.0.0.1", 9002),

DestinationHandler

)

print("Destination server running on port 9002")

server.serve\_forever()

This server simply receives requests and returns a message.

Create redirect.py:

from http.server import HTTPServer, BaseHTTPRequestHandler

class RedirectHandler(BaseHTTPRequestHandler):

def do\_GET(self):

self.send\_response(302)

self.send\_header(

"Location",

"http://127.0.0.1:9002/demo"

)


self.end\_headers()

server = HTTPServer(

("127.0.0.1", 9001),

RedirectHandler

)

print("Redirect server running on port 9001")

server.serve\_forever()

This server returns a redirect to the local destination.

Open two PowerShell terminals.

Terminal 1:

python destination.py

Terminal 2:

python redirect.py

Both servers should start.

Run:

curl.exe -i http://127.0.0.1:9001/redirect

Expected response:

HTTP/1.0 302 Found

Location: http://127.0.0.1:9002/demo

Now follow the redirect:

curl.exe -i -L http://127.0.0.1:9001/redirect

Expected result:

HTTP/1.0 200 OK

Hello from destination server

The destination server terminal should show:

Destination received: /demo

This confirms that the client followed the redirect.

Your original scenario has an additional component: the destination URL contains a command injection payload.

The conceptual flow is:

Stage

1.User supplies a URL to the vulnerable application

2\. Firewall inspects the original URL

3\. Application requests the supplied URL

4\. Redirect server responds with a new destination

5\. HTTP client follows the redirect

6\. Application or downstream component processes the resulting request

The critical question is where the command injection actually occurs.

For example, if the application uses a shell command to process the final URL, redirect handling could change which input reaches that command.

But if the application only makes HTTP requests and never invokes a shell, a redirect alone cannot create OS command execution.

Similarly, if the application validates the final destination and safely handles URL parameters, the redirect will not bypass those controls.

For a client-approved SSRF assessment, I would test the following separately.

Direct URL fetch :- Whether the application performs server-side requests

Redirect following:- Whether the HTTP client follows redirects

Redirect destination validation:- Whether each destination is validated

Redirect count:- Whether excessive redirects are restricted

Protocol restrictions:- Whether only approved schemes are accepted

DNS resolution:- Whether resolved addresses are checked against internal ranges

Command execution evidence:- Whether input actually reaches a shell or command interpreter

A secure implementation should:

For SSRF prevention, validating only the hostname string is insufficient. DNS resolution and redirect handling must also be considered.

Your technique exploits a trust-boundary mismatch:

Input validation

↓

Accepted URL

↓

HTTP request

↓

Redirect

↓

New destination

The firewall may inspect only the first URL, while the HTTP client processes a second URL that was never subjected to equivalent validation.

This is best described as SSRF redirect validation bypass when the security control fails to validate the redirected destination.

If command injection is also present, that is a separate issue that needs evidence showing attacker-controlled data reaches a command interpreter.

[SSRF: A Sneaky Way to Bypass URL Filters Using HTTP Redirects](https://bugbountywizard.app/ssrf-a-sneaky-way-to-bypass-url-filters-using-http-redirects-046ff54ce667) was originally published in [BugBountywizard](https://bugbountywizard.app) on Medium, where people are continuing the conversation by highlighting and responding to this story.
