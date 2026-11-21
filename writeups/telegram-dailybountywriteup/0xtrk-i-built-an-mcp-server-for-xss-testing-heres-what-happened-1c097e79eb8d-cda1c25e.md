# I Built an MCP Server for XSS Testing — Here’s What Happened

- **Source URL:** https://medium.com/@0xTrk/i-built-an-mcp-server-for-xss-testing-heres-what-happened-1c097e79eb8d?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250905231429/https://medium.com/@0xTrk/i-built-an-mcp-server-for-xss-testing-heres-what-happened-1c097e79eb8d
- **Fetched:** 2026-11-21
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/9818 (id 9818)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# I Built an MCP Server for XSS Testing — Here’s What Happened

Hello everyone, how are you doing? I hope you’re all well. In this brief article, I’m going to talk to you about MCP servers as well as my little MCP server that allows AI to have the necessary environment to test XSS vulnerabilities. It’s mainly for reflected XSS, but there’s also the possibility to test stored XSS when chained with another MCP server: browsermcp.

## Introduction: MCP what is this?

So first, what exactly is an MCP server : a technology that everyone’s talking about but still seems unclear to some?

An MCP server (Model Context Protocol server) is simply a server that allows an AI to interact with external tools or custom components. This protocol is often used to enable AI to access databases, tools, etc. In short, it’s an emerging technology. Actually, quite a few companies are implementing this.

Think about PayPal: [https://mcp.paypal.com/sse](https://mcp.paypal.com/sse)

Personally, I used Python’s fastMCP library to create the MCP server I’m presenting to you. (Well, it’s more the algorithm that I created, then I did what we call… ah, vibe coding!)

The 3 types of functionality of an MCP server via fastMCP that we can use are:

**@mcp.tool()** => To expose a function or tool that the AI can call. Example: a simple function that allows it to make HTTP requests.

**@mcp.resources()** => Used to provide the AI with static or dynamic resources. Example: documents, JSON files, databases, etc.

**@mcp.prompt()** => Allows providing the AI with prompts that it will execute.

Once we’re done with the theoretical part => by the way, I strongly invite you to learn more about this subject if you haven’t already, because these are just the basics so you can understand what follows.

## My MCP Server — XSS TESTER

Like everyone else, I was surprised by this technology because it’s really a huge step forward in technology and especially a big step in IT in general!!!!

So since I’m interested in the world of web pentesting, I decided to create an MCP server that will allow AI to test XSS vulnerabilities. And to do this, I decided to create 6 mcp.tools on my MCP server so the AI can successfully conduct its tests. Here they are:

**test\_xss\_url** — Automatically tests if a URL is vulnerable to XSS attacks by detecting malicious JavaScript execution

**get\_raw\_html\_response** — Retrieves raw HTML code from a web page to manually analyze the presence of XSS payloads in the response

**search\_in\_html\_response** — Searches for specific terms in a page’s HTML with context, useful for checking if XSS payloads are reflected

**get\_javascript\_file** — Downloads and analyzes JavaScript files to detect DOM XSS vulnerabilities in client code

**get\_http\_headers** — Examines security HTTP headers (CSP, X-Frame-Options, etc.) to evaluate XSS protections

**make\_custom\_http\_request** — Performs custom HTTP requests with headers/cookies to test XSS in authenticated contexts

You should know that this MCP server is mainly for reflected XSS, but as I mentioned, it can be used for stored XSS by using the BROWSERMCP server for form submission, and the XSS tester MCP server to analyze and validate the XSS. Anyway, I’ll put the GitHub repository link for my MCP server and the browser MCP server so you can analyze all this properly.

## POC

Now that we have all this, let’s test if this server can actually find XSS or if it’s just bluff??

Let’s start by launching the MCP server (personally I use VSCode X Copilot) with Ctrl + Shift + P => run the server

As mentioned above, you can see there are 6 tools.

So let’s launch a basic test on a basic lab from PortSwigger Academy

Here’s another test, this time with XSS into a template literal with angle brackets, single, double quotes, backslash and backticks Unicode-escaped:

I could do thousands of tests for POC but the article would risk being long. I invite you to test this yourself, and don’t hesitate to improve it and share your impressions with me.

But my advice: never be too general with AI, give the AI a precise goal. Example: instead of asking “test XSS,” you ask: “Test XSS knowing that there’s Cloudflare behind and there are CSP policies. Try to bypass them by analyzing how your payload is reflected each time.” => This is a simple example, but the best way to prompt is to ask the AI how to prompt xdd

It’s not “wow” but it’s the beginning of something. I can’t imagine what experts must be doing with this technology and their experience. In conclusion, we’re at the beginning of something that will shake up our way of doing things, of seeing things. Even if it’s the beginning and it’s still incredible for now. We shouldn’t rely entirely on it, on the contrary (not for now). We need to know how to talk with AI (prompt engineering) because even if you have the best MCP, if you don’t know how to talk with AI, it’s useless. Know how to put it in context. And especially the game changer: use it as an employee, support, mentor. To be among the hottest tomorrow, we’ll have to accept change and not have what we call the ostrich phenomenon (that is, putting your head in the ground like an ostrich to avoid facing reality).

On that note, peace be upon you.
