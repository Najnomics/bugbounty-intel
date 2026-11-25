# How I Hacked an IISc Subdomain Without Knowing the Admin Password ️

- **Source URL:** https://medium.com/@mvsbadm625/how-i-hacked-an-iisc-subdomain-without-knowing-the-admin-password-%EF%B8%8F-ca4aa68c3c93
- **Fetched from:** https://medium.com/@mvsbadm625/how-i-hacked-an-iisc-subdomain-without-knowing-the-admin-password-%EF%B8%8F-ca4aa68c3c93?source=rss-c9c7bd1b7a24------2
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14980 (id 14980)
- **Method:** medium-rss-feed (full content:encoded) readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- **Author/Published (RSS):** M Venkata Sasidhar Kaushik / Thu, 12 Nov 2026 06:13:17 GMT

During one of my security research sessions, I started exploring publicly exposed infrastructure associated with the Indian Institute of Science (IISc). While performing reconnaissance using Shodan, I discovered a host associated with an IISc subdomain that exposed a HTTPS port.

What initially appeared to be an ordinary exposed web service eventually led me to an administrative portal containing sensitive institutional information. I was unable to authenticate using the credentials I had tried. Instead of continuing with password guessing, I decided to investigate how the application handled authentication responses. This led me to discover an authentication-related weakness that allowed me to bypass the portal’s login interface through HTTP response manipulation.

Here’s how I approached the investigation.

I started my investigation by exploring IISc-related domains and subdomains using Shodan. During this process, I identified a publicly accessible host associated with an IISc subdomain.

The host exposed a HTTPS port. I decided to investigate the HTTPS service running. Upon accessing the host through a browser, I discovered an administrative portal belonging to the IISc ecosystem.

The portal appeared to provide administrative functionality for managing institutional resources.

The administrative portal presented a login interface that required valid credentials. Since I did not possess any credentials, I initially tested a few commonly used default combinations, including:

None of these combinations worked.

Rather than continuing with password guessing, I decided to examine the application’s authentication mechanism and understand how the frontend processed responses from the authentication endpoint.

I opened Burp Suite and configured the browser to route application traffic through the proxy. After submitting the login form, I intercepted the authentication request and examined the corresponding server response.

The application returned an HTTP response with:

HTTP/1.1 401 Unauthorized

The response also contained an error message indicating that the supplied credentials were invalid. This was the expected behaviour for an unsuccessful authentication attempt. However, I became interested in how the frontend handled this response.

In particular, I wanted to understand whether the application’s login interface relied entirely on the response status and message returned by the authentication endpoint.

I decided to investigate the application’s response-handling behaviour. Using Burp Suite, I intercepted the authentication response before it reached the browser.

I modified the intercepted response by:

HTTP/1.1 200 Unauthorized

2\. Removing the error message indicating invalid credentials.

I then forwarded the modified response to the browser.

**Unexpectedly, the application allowed me to proceed past the login interface.**

The administrative portal became accessible through the browser, despite the original authentication attempt having returned an unauthorized response.

This was a significant observation because the application’s frontend appeared to trust the modified authentication response.

After accessing the administrative portal, I began examining the available sections to understand the potential security impact. The portal contained several categories of sensitive institutional information and administrative resources.

Some of the information I encountered included:

The discovery raised serious concerns about the confidentiality of institutional information. An administrative portal is expected to enforce strong authentication and authorization controls because it may provide access to resources that should never be publicly accessible.

In this case, manipulating the HTTP response appeared sufficient to bypass the login interface and reach the administrative portal. I avoided reproducing sensitive records or accessing unrelated resources.

This finding highlights an important security principle: authentication must never depend exclusively on client-side application behaviour.

When a frontend relies on HTTP response properties to determine whether a user is authenticated, manipulating the response may cause the application to behave as though authentication succeeded.

However, there is an important distinction between bypassing the login interface and bypassing server-side authentication. Changing a response in an intercepting proxy does not change the authentication decision made by the server. Therefore, the actual security impact depends on whether protected backend APIs independently validate the user’s authentication and authorization.

If backend endpoints also trust client-controlled session state or fail to enforce authorization, the consequences could be significantly more serious.

After identifying the issue and understanding its potential impact, I decided to report the finding to the concerned institution rather than disclose sensitive information publicly.

I submitted my findings to the IT Head of IISc, explaining the authentication-related weakness, the testing methodology, and the potential exposure of sensitive institutional information.

The report was acknowledged, and I received appreciation and thanks for responsibly reporting the issue. Discovering a vulnerability is only one part of the process. Communicating the issue responsibly and helping the affected organization understand the security implications are equally important.

What started as routine reconnaissance using Shodan turned into an interesting security discovery involving an administrative portal associated with IISc. After identifying an exposed host, I investigated its administrative interface and examined the authentication mechanism when my initial login attempts failed. By manipulating the intercepted HTTP response, I managed to bypass the portal’s login interface and encountered sensitive institutional information. I subsequently reported the issue to the IISc IT Head and received acknowledgement and appreciation for my responsible disclosure.

Responsible security research is not just about finding weaknesses. It is about identifying risks, communicating them appropriately, and helping organizations improve their security posture.

Thank you very much for reading this! ✌️
