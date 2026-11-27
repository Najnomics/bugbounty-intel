# Part 2- Everything You Need to Know About Browser Security Policies — CSP, Cookie Attributes, etc.

- **Source URL:** https://medium.com/@vikramroot/part-2-everything-you-need-to-know-about-browser-security-policies-csp-cookie-attributes-etc-3ea98f737b3a?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250919233955/https://medium.com/@vikramroot/part-2-everything-you-need-to-know-about-browser-security-policies-csp-cookie-attributes-etc-3ea98f737b3a
- **Fetched:** 2026-11-27
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/6474 (id 6474)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Part 2- Everything You Need to Know About Browser Security Policies — CSP, Cookie Attributes, etc.

Hello Everyone, we have covered the Same Origin Policy ( SOP ), and Cross-Origin-Resource-Sharing (CORS) in part 1. Here is the URL for part 1 : [Click here.](/@vikramroot/part-1-everything-you-need-to-know-about-browser-security-policies-sop-cors-3eb025fd3ab8)

In this blog, we will discuss more about Content-Securtiy-Policy, HTTP Strict Transport Security (HSTS), X-Frame-Options, and Cookie Attributes.

*Content-Security-Policy*

*HTTP Strict Transport Security (HSTS)*

*X-Frame-Options*

*Cookie Attributes*


## 1. CSP: Content Security Policy

Content Security Policy (CSP) is a powerful security feature that helps prevent a wide range of attacks, including Cross-Site Scripting (XSS), data injection attacks, and other forms of code injection attacks.

### How CSP Works

CSP works by allowing web developers to create a whitelist of sources from which content can be loaded on their website. This is done by setting the `Content-Security-Policy` HTTP header or by using a `<meta>` tag within the HTML document. When the browser loads the page, it checks the CSP directives and blocks any resources that don't match the allowed sources.

### Key Directives in CSP

1. **default-src:** This directive serves as a fallback for other resource types when they don’t have specific directives. It specifies the default sources from which content can be loaded.

`Content-Security-Policy: default-src 'self'`
2\. **script-src:** This directive controls which sources are allowed to execute scripts. This is crucial for preventing XSS attacks.

`Content-Security-Policy: script-src 'self' https://trusted.cdn.com`
### Example Scenario

Imagine you have a web application `https://example.com` and you want to implement CSP to enhance security. Here’s how you can configure CSP to allow content from trusted sources only:

**Objective:** Securely load scripts, styles, images, and fonts from specified sources while blocking all others.

```
Content-Security-Policy: default-src 'self'; 
                        script-src 'self' https://trusted.cdn.com; 
                        style-src 'self' 'unsafe-inline' https://trusted.cdn.com; 
                        img-src 'self' https://images.example.com; 
                        connect-src 'self' https://api.example.com; 
                        font-src 'self' https://fonts.example.com; 
                        frame-src 'self' https://trusted.example.com
```
This policy ensures that all content is loaded from `self` (the same origin) and specific trusted sources, providing a robust defense against code injection attacks.

## 2. HSTS: HTTP Strict Transport Security

HTTP Strict Transport Security (HSTS) is a crucial security mechanism designed to protect websites and users by ensuring that connections are made only over HTTPS, thereby preventing any attempts to connect over HTTP. It helps protect websites against man-in-the-middle attacks such as protocol downgrade attacks and cookie hijacking. HSTS is implemented by web servers via the `Strict-Transport-Security` HTTP header, which instructs browsers to only interact with the website using HTTPS.

**How HSTS Works**

When a browser first connects to a server over HTTPS, the server can include the `Strict-Transport-Security` header in its response. This header tells the browser to remember to only use HTTPS for a specified duration when accessing the site in the future.

**Example HSTS Header**:

`Strict-Transport-Security: max-age=31536000; includeSubDomains; preload`
**Parameters**:

1. **max-age**
`max-age=31536000` means the browser will enforce HTTPS for one year. Every time the browser receives this, the max-age will become 1 year automatically.
2. **includeSubDomains**
3. **preload**
[HSTS preload list](https://hstspreload.org/)).

**Note: Initial HTTPS Connection Requirement:** For HSTS to be enforced, the browser must first connect to the site via HTTPS at least once. This initial connection allows the browser to confirm that the server supports HTTPS and to receive the HSTS header. Subsequent connections will then be automatically upgraded to HTTPS.

**Security Implication:** If the initial connection is made over HTTP and is not redirected to HTTPS, the HSTS header will be ignored by the browser. This is to prevent Man-In-The-Middle (MITM) attacks where an attacker could intercept the initial HTTP request and strip or modify the HSTS header.

## 3. X-Frame-Options

X-Frame-Options is an HTTP response header used to protect web applications from clickjacking attacks. Clickjacking occurs when an attacker tricks a user into clicking on something different from what the user perceives, potentially compromising sensitive information or actions. By using X-Frame-Options, developers can ensure that their web pages are not embedded into other sites without their permission.

This security feature helps control whether a browser should be allowed to render a page in a `<frame>`, `<iframe>`, `<embed>`, or `<object>`, thus preventing malicious framing of your site.

**The X-Frame-Options header has three main directives:**

1. **DENY:** This directive disallows the site from being loaded in a frame, iframe, embed, or object universally, even if the request comes from the same origin.

`X-Frame-Options: DENY`
**2. SAMEORIGIN:** This directive allows the page to be loaded in a frame, iframe, embed, or object only if the request is from the same origin as the page.

`X-Frame-Options: SAMEORIGIN`
**3. ALLOW-FROM uri:** This directive permits the page to be framed only by a specified origin. Note that this directive is not widely supported by all browsers.

`X-Frame-Options: ALLOW-FROM https://trusted.example.com`
The X-Frame-Options header is a simple yet powerful tool for enhancing web security. By controlling how and where your web pages can be embedded, you can effectively protect your users from clickjacking attacks.

## 4. Cookie Attributes

Cookies are essential for maintaining user sessions and storing data in web applications. However, if not managed properly, cookies can introduce security risks. To enhance the security of cookies, several attributes can be set to control their behavior. In this blog post, we’ll explore the key cookie attributes: Secure, HttpOnly, and SameSite, and how they help in protecting your web applications.

`Set-Cookie: sessionId=abc123; Secure; HttpOnly; SameSite= $Directive`
1. **Secure Attribute**: The Secure attribute ensures that cookies are only sent over secure, encrypted connections (HTTPS). This prevents the cookie from being transmitted over unencrypted HTTP, where it could be intercepted by attackers significantly reducing the risk of man-in-the-middle (MITM) attacks.

2\. **HttpOnly Attribute**: The HttpOnly attribute prevents JavaScript from accessing the cookie, mitigating the risk of Cross-Site Scripting (XSS) attacks. By using the HttpOnly attribute, you prevent client-side scripts from accessing the cookie, thereby protecting sensitive information from being exposed through XSS vulnerabilities.

**3. SameSite Attribute:** The SameSite attribute restricts how cookies are sent with cross-site requests, providing protection against Cross-Site Request Forgery (CSRF) attacks. It has three directives: Strict, Lax, and None.

- **SameSite=Strict**: Cookies are only sent for requests originating from the same site. This means the cookie will not be sent with requests initiated by third-party websites.
- **SameSite=Lax**: Cookies are sent with requests made from third-party sites, but only with safe HTTP methods like GET. This provides a balance between security and usability.
- **SameSite=None**: Cookies are sent with all cross-site requests, without any restrictions. Necessary for cross-site scenarios such as third-party integrations and Single Sign-On (SSO) solutions. To use `SameSite=None`, the `Secure` attribute must also be set to ensure the cookie is only sent over HTTPS.

Note: If the `SameSite` attribute is not specified, modern browsers like Google Chrome default to `SameSite=Lax`. This default setting helps provide a basic level of protection against CSRF attacks.

Part 1: [Click here](/@vikramroot/part-1-everything-you-need-to-know-about-browser-security-policies-sop-cors-3eb025fd3ab8)

Thank you for reading about browser security policies. Reach out to me here if you have any doubts or topic suggestions: [Linkedin](https://www.linkedin.com/in/vikram--naidu/)
