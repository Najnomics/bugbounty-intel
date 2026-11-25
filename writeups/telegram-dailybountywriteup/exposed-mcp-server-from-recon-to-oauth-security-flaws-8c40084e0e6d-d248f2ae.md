# Exposed MCP Server

- **Source URL:** https://scriptjacker.medium.com/exposed-mcp-server-from-recon-to-oauth-security-flaws-8c40084e0e6d
- **Fetched from:** https://scriptjacker.medium.com/exposed-mcp-server-from-recon-to-oauth-security-flaws-8c40084e0e6d?source=rss-d1a41cbb187a------2
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:**  (id 14950)
- **Method:** medium-rss-feed (full content:encoded) readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- **Author/Published (RSS):** Parth Narula / Fri, 16 Oct 2026 16:20:05 GMT

Hey Hackers, I am Parth Narula. A penetration tester, bug hunter, red teamer and overall a security researcher. I live for those moments where a bit of thinking outside the box leads to an interesting security finding.

*I am starting a series of the bugs that I found in the services and functionalities related to AI in the applications.*

This time, I was doing reconnaissance on REDACTED when I came across an MCP service. What started with a simple JSON response eventually led me to exposed API documentation, OAuth client registration, and some unexpected redirect behavior.

During my reconnaissance, I came across an MCP service belonging to REDACTED.

I opened the service in my browser, and it returned a simple JSON response:

```
{
  "status": "ok"
}
```
Nothing interesting, right?

It was just a normal status response indicating that the service was responding. There was no sensitive information in this response, and nothing immediately suggested a vulnerability.

But I wanted to explore the service further.

So I started directory enumeration using dirsearch to see whether there were any interesting files or directories accessible without authentication.

While going through the results, I noticed something interesting.

The scanner identified a few accessible resources inside an /examples/ directory, including:

/examples/sitemap.xml

/examples/sitemap.xml.gz

Both sitemap files returned HTTP 200 responses.

Now, a sitemap itself is not a security vulnerability. But it can be useful during recon because it sometimes reveals pages that are not directly linked from the main application.

So I decided to open it and this is where things started getting interesting.

When I opened /examples/sitemap.xml, it exposed several documentation paths.

One of them immediately caught my attention:

/examples/api-reference.html

The sitemap also referenced other pages, including an architecture page and an overview page.

I started wondering what information was available inside these documentation pages. So I opened the API reference.

A complete documentation interface for the MCP service, accessible without logging in.

The documentation contained several sections, including:

API Reference

HTTP Endpoints

MCP Tools

Skill Resources

Error Handling

Authentication

Rate Limits

Response Metadata

At first, I was just exploring the documented functionality.

But then I noticed an Authentication section.

Obviously, that was something I wanted to examine more closely :)

I opened the Authentication section to understand how the service handled users and API clients.

To my surprise, it explained the OAuth process in considerable detail. It described client registration, authorization requests and token exchange.

The documented flow started with:

POST /mcp/register

Then:

GET /mcp/authorize

And finally:

POST /mcp/token

The documentation even showed the parameters required for authorization, including:

response\_type

client\_id

redirect\_uri

scope

state

code\_challenge

code\_challenge\_method

Further down, I noticed another interesting detail.

The documentation described the JWT token format and listed several accepted subject claims:

sub

email

user\_id

uid

client\_id

azp

This was useful information about how the authentication system was designed.

Of course, documenting JWT claims is not automatically a vulnerability. But during security testing, understanding what an application accepts can help identify areas that deserve closer examination.

I continued exploring the API reference. It also listed several operational endpoints:

POST /mcp/register

POST /mcp/token

GET /mcp/authorize

GET /mcp/auth/callback

GET /mcp/consent

At this point, I had a pretty good understanding of the authentication flow without needing to log into the service.

But reading documentation was only the beginning. I wanted to see how the backend actually behaved.

I went back to the API documentation and looked at this endpoint again:

The documentation described it as dynamic client registration.

Basically, an application could submit its details and receive a client identifier and other registration information.

I wanted to understand which values the server would accept.

One parameter caught my attention:

"redirect\_uris": \[\]

This parameter tells the authorization server where the browser can return after part of the OAuth flow.

So I started wondering. What if I register my own client and supply a domain that I control as the redirect URI?

I opened Burp Suite and prepared the following request:

POST /mcp/register HTTP/2

Host: REDACTED

```
{
  "client_name": "My AI App",
  "redirect_uris": [
    "https://COLLABORATOR.example/"
  ]
}
```
I used a Burp Collaborator domain so that I could observe whether anything tried to connect to it.

Then I sent the request.

The server responded with:

HTTP/2 201 Created

The response included a newly generated client ID, client secret, and the registered redirect URI.

```
{
  "client_id": "REDACTED",
  "client_secret": "REDACTED",
  "redirect_uris": [
    "https://COLLABORATOR.example/"
  ]
}
```
The server accepted the registration request and stored the redirect URI I supplied and this is a vulnerability because redirect\_uri is not getting validated.

There was no authentication required for this registration.

At this point, I had confirmed that I could register a client with my own callback URL.

After sending the registration request, I checked Burp Collaborator.

And guess what? There were interactions.

I observed both DNS and HTTP requests associated with the Collaborator domain I had submitted.

The HTTP interaction was a request to the root path:

GET / HTTP/1.1

Host: COLLABORATOR.example

Now this was interesting.

I had submitted a URL as part of the OAuth client registration process, and shortly afterward, that same domain received network requests.

The application fetches arbitrary URLs from its own infrastructure without proper restrictions, this creates an SSRF vulnerability..

And I was not finished yet.

After successfully registering the client, I moved on to the authorization endpoint.

Remember the endpoint I found earlier?

The authorization request accepts a client\_id and a redirect\_uri, along with the other OAuth parameters.

I already had a newly registered client ID and a callback URL pointing to my Collaborator domain.

So I constructed an authorization request using those values.

The request followed this structure:

/mcp/authorize?response\_type=code&client\_id=REDACTED&redirect\_uri=https://COLLABORATOR.example/&scope=openid&state=TEST&code\_challenge=REDACTED&code\_challenge\_method=S256

Then I opened it in my browser.

The browser eventually reached the callback domain that I had registered.

So the registered callback URL was being used during the authorization flow and redirect\_uri is not getting validated and I could use this to steal authorization code.

That confirmed the redirect behavior I observed.

**Recon can reveal much more than you expect:** A normal status endpoint might not be interesting by itself, but exploring related directories and documentation can uncover functionality that deserves further testing.

**Read the API documentation carefully:** API references can reveal endpoints, authentication flows, parameters and features that are not immediately visible through the main application.

**Do not stop at the frontend:** When you discover an API endpoint, understand how it works and check how the backend handles the parameters you control.

I hope you learn something new. Follow for more amazing articles and give claps if you like this one :)

Need expert pentesting services?

Visit [https://scriptjacker.in](https://scriptjacker.in) or let’s collaborate on your next project! 🤝

Want to learn from my experiences? Check out my articles on [https://blogs.scriptjacker.in](https://blogs.scriptjacker.in)
