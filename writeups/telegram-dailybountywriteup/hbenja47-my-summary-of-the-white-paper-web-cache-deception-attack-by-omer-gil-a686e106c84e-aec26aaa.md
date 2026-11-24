# My summary of the White Paper “Web Cache Deception Attack” by Omer Gil

- **Source URL:** https://medium.com/@hbenja47/my-summary-of-the-white-paper-web-cache-deception-attack-by-omer-gil-a686e106c84e?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20230925222055/https://medium.com/@hbenja47/my-summary-of-the-white-paper-web-cache-deception-attack-by-omer-gil-a686e106c84e
- **Fetched:** 2026-11-24
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/2832 (id 2832)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# My summary of the White Paper “Web Cache Deception Attack” by Omer Gil

--

Static files such as .css, .js, .txt, .png, .bmp, .gif, and others are considered public files and are stored in the public cache to serve them to any web user.

To implement caching between the client and the server (not the browser cache), different services are used, such as:

- CDN
- Load balancer
- Reverse proxy

These services serve the mentioned static files, which are public and do not contain sensitive information. This is a great service that optimizes response time for the client and does not overload the server(s).

If the file has never been used or has exceeded its cache lifetime (if it was cached), it needs to be requested from the server. Once requested, the caching service checks if it’s a static file and then caches it, making it publicly available for other clients that request it, eliminating the need to make another request to the server.

# Server Response to a Request like this:

http://www.example.com/home.php/nonexistent.css

# Server Response

In the case where /home.php contains the user’s data making the request and nonexistent.css is a non-existent static file, the server can respond with a 200 OK status and the same content as http://www.example.com/home.php, as if it didn’t take into account nonexistent.css. This depends on the server’s technology and configuration.

# Web Cache Deception (WCD) Methodology

1. The attacker sends the victim the malicious URL https://www.bank.com/account.do/logo.png.
2. The victim accesses the URL (they must be logged into their account beforehand).
3. The request reaches the proxy, which is unaware of this file and asks the server about it.
4. The server responds with the victim’s account content using a 200 OK status.
5. The caching system receives the file and identifies that the URL ends with a static file extension (.png), treating it as a public static file and creating a cache folder with the file logo.png.
6. The victim receives their account page as usual.
7. The attacker accesses https://www.bank.com/account.do/logo.png, and the request is received by the proxy, which returns the cached victim’s account page.

# What does this imply?

A successful exploitation allows the attacker to obtain the victim’s personal information. The impact can be greater if the response contains the victim’s session information, such as CSRF tokens, security questions, tokens, or session cookies, potentially leading to an account takeover.

# Conditions

Three conditions must be met for a WCD attack to succeed:

1. When adding the /nonexistent.css path to the page to be cached, it must return the original content (sometimes it may return a 404 error but still cache the victim’s information).
2. The web caching functionality must be configured to cache files based on their extension.
3. The victim must be authenticated when accessing the malicious URL.

# Regarding Some Web Frameworks

# PHP

A PHP application without a framework always returns a 200 OK response when a /nonexistent.gif path is added, with the content of the requested URL.

# Django

It also returns a 200 OK response if the /nonexistent.css path is added. However, it also works if the extension is added directly to the URL that is to be compromised, for example: http://www.sampleapp.com/inbox.css, where the real URL is http://www.sampleapp.com/inbox. However, if the urlpatterns are configured correctly with a $ in the regex (e.g., “url(r’^inbox/$’, …”), it will not work.

# ASP.NET

ASP.NET uses a feature called FriendlyURLs, which allows users to use cleaner and more user-friendly URLs. For example, accessing https://www.example.com/home.aspx is possible without the extension: https://www.example.com/home. This feature can be configured in the Route.config file and is enabled by default in any ASP.NET application.

If this feature is active, the WCD attack will not work because requesting http://localhost:39790/Account/Manage.aspx/test.css will return http://localhost:39790/Account/Manage/test.css and result in a 404 Not Found response. However, if this feature is disabled, the attack will work perfectly.

# Caching Mechanisms

# Cloudflare

When Cloudflare receives a file from the server, its servers go through two phases. The first phase is the Eligibility Phase, where it checks if caching is enabled for the website and the directory from which the file originates. If this is affirmative, it then checks the file extension, caching the following file types:

class, css, jar, js, jpg, jpeg, gif, ico, png, bmp, pict, csv, doc, docx, xls, xlsx, ps, pdf, pls, ppt, pptx, tif, tiff, ttf, otf, webp, woff, woff2, svg, svgz, eot, eps, ejs, swf, torrent, midi, mid

If this happens, it proceeds to the second phase, the Desqualification Phase, where Cloudflare checks for HTTP caching headers. If the server returns a header indicating that the cache is dynamic, Cloudflare does not store it. However, there is an option in Cloudflare’s configuration that allows creating an “Edge cache expire TTL” rule that overrides the caching headers returned by the server.

# IIS ARR

ARR (Application Request Routing) is an IIS feature that provides load balancing capabilities. One feature of ARR is its caching system. Rules are configured to store files in the cache directory, specifying which file types and for how long they should be cached. For example, it could be configured to always cache all \*.css files for 60 minutes. This means that all CSS extensions will always be cached for 60 minutes. This “always” rule also includes ignoring caching headers. Therefore, if http://www.sampleapp.com/welcome.php/test.css is requested, a directory named welcome.php is created in the cache directory, and within it, a file named test.css that contains all the data from the user’s welcome.php page.

# NGINX

An NGINX server functioning as a load balancer provides the capability to cache the content returned from web servers. Caching rules can be configured in the configuration files to, for example, specify caching all static files that match a certain pattern: (css|js|gif|png)$ { proxy\_cache my\_cache … }. If an authenticated user accesses http://www.sampleapp.com/app/welcome.php/test.css, NGINX considers it a static file and caches it.

# Mitigation

1. Configure the caching mechanism only if the HTTP caching header allows it.
2. Store all static files in a specific directory and only allow caching the content from that directory.
3. If the caching mechanism allows caching based on file content, configure it.
4. Configure the web server to not return the content of different paths, especially those that contain user information, when adding /nonexistent.css at the end. In that case, it should return a 404 or a 302.

# Summary

WCD is a simple attack that can have serious consequences, such as stealing the user’s personal information or even achieving an account takeover. Limited examples of this attack were presented here, but there are many variations depending on the framework used and the caching mechanism in place. No framework or caching mechanism is vulnerable to this attack by itself; it is the improper configurations that can enable a successful attack. To prevent this attack, it is recommended that technical personnel be aware of the cache exploitation possibilities. Additionally, providers should not have default options that facilitate the attack, and the technician configuring the service should be given warnings about the potential risks.

Here is the original text https://www.blackhat.com/docs/us-17/wednesday/us-17-Gil-Web-Cache-Deception-Attack-wp.pdf
