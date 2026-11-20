# Cross-site and server-side request forgeries (CSRF and SSRF)

- **Source URL:** https://medium.com/@forensics.000/cross-site-and-server-side-request-forgeries-csrf-and-ssrf-b91911e42e44?source=rss------bug_bounty-5
- **Fetched from:** https://medium.com/feed/@forensics.000
- **Fetched:** 2026-11-20
- **Channel:** @dailybountywriteup
- **Telegram message:**  (id 5280)
- **Method:** medium-rss-content readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
### Request forgeries

A request to a web application can be forged to trick the web application into performing an unintended action. Two types of request forgeries exist: cross-site request forgery (CSRF) and server-side request forgery (SSRF).

### Cross-site request forgery (CSRF)

A ***cross-site request forgery (CSRF)***, also known as ***client-side request forgery*** or ***XSRF***, is an attack in which an attacker sends a forged request to a web application on behalf of an authenticated user. A CSRF attack exploits a web application’s trust in an authenticated user. Ex: A banking web application stores an authentication token on a user’s device when the user authenticates to the banking web application. If the user does not logout from the banking web application, the authentication token remains on the user’s device and can be used by an attacker to perform a banking transaction on behalf of the user and without the user’s knowledge.

1. An attacker sends a forged request to the user to exploit the web application’s trust in the user. The forged request can be an embedded script or a URL.
2. User unknowingly sends the attacker’s forged request to the web application. The authentication token is included with each request sent from the user to the web application.
3. Since the request is from an authenticated user, the web application responds to the forged request, which may include sending the user’s confidential data to the attacker.

### Server-side request forgery (SSRF)

A ***server-side request forgery (SSRF)*** is an attack in which an attacker sends forged requests from a web application’s server to other servers. In an SSRF attack, an attacker tricks a server into making an unauthorized request. An SSRF attack uses a web server to access or modify internal resources that are protected from external networks. SSRF can also be used to access a web server’s other available services through the server’s loopback interface. Ex: An attacker sends a forged request to a web server to retrieve user account information from a back-end database server.
