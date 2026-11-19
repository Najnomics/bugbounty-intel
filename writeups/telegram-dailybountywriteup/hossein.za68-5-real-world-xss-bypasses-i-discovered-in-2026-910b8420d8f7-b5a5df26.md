# 5 Real World XSS Bypasses I Discovered in 2026

- **Source URL:** https://medium.com/@hossein.za68/5-real-world-xss-bypasses-i-discovered-in-2026-910b8420d8f7
- **Fetched from:** https://web.archive.org/web/20261111155258/https://medium.com/@hossein.za68/5-real-world-xss-bypasses-i-discovered-in-2026-910b8420d8f7
- **Fetched:** 2026-11-19
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14890 (id 14890)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# 5 Real World XSS Bypasses I Discovered in 2026

Hello everyone 👋

Throughout 2026, while working on enterprise penetration testing projects, VDP programs, and Bug Bounty programs, I discovered several XSS vulnerabilities.

I selected five of the cases that I found particularly interesting and different, and decided to share them in this article. I hope you find them useful and can apply similar techniques and approaches in your future testing.

The goal of this article is not simply to provide a collection of ready-made payloads. Instead, I want to explain why common XSS payloads failed in each scenario and how analyzing the application’s behavior and identifying the right attack path eventually led to successful XSS exploitation.

## 1. Bypassing WAF and Server-Side Character Restrictions with URL Encoding

On one of the targets, I started with some basic input reflection testing.

For example, I submitted:

`"<test`
and noticed that the input was reflected in the page source without any significant encoding.

At first, this looked like a promising reflection point for XSS testing. However, when I tried common XSS payloads, I couldn’t get them to execute.

After several attempts and some WAF fingerprinting, I noticed that certain payloads resulted in a `403 Forbidden` response, while some other payloads caused the application itself to return an error instead of the usual WAF blocking response.

One of the payloads that produced this different behavior was:

`['XSS'].map(alert)`
After further investigation, I realized that part of the restriction was related to how the server stack processed the URI.

Apache Tomcat can reject certain special characters in URI components when they are not appropriately encoded. Tomcat provides options such as `relaxedQueryChars` and `relaxedPathChars` for controlling some of these restrictions.

So instead of sending `[` and `]` directly, I URL-encoded them:

`%5B%27XSS%27%5D.map(alert)`
The payload then executed successfully.

What I found particularly interesting about this case was that at first I thought I was dealing purely with a WAF restriction. However, further investigation showed that I also needed to consider the difference between **WAF behavior and server-side URI parsing restrictions**.

This is an important point when testing XSS: if a payload is blocked with a `403`, don't always assume that the WAF is the only thing preventing exploitation. Sometimes you need to determine exactly which layer in the request-processing chain is rejecting your payload.

## 2. Exploiting HTML Metadata Through a Remote HTML Document

The second case was one of the more interesting scenarios I encountered while testing functionality related to URLs and content previews.

On one part of the application, users could provide a URL, such as the address of their personal website. The application would then retrieve content from that URL and extract some of its metadata to generate a preview or description.

This is similar to what we commonly see in messaging platforms and social networks: when you share a URL, the application often retrieves information such as the page title, description, or other metadata and displays it as part of the link preview.

To test this functionality, I hosted a simple HTML file on a server under my control:

```
<head>
    <meta name="viewport" content="test123">
</head>
```
I then provided the URL of this HTML file to the target application instead of a normal website URL.

If the value `test123` appeared in the generated preview or page source, it would indicate that data retrieved from the external HTML document was being incorporated into the application's output.

Of course, simply retrieving metadata from an external URL does not automatically mean that an XSS vulnerability exists.

To demonstrate XSS, we need to determine whether attacker-controlled data is eventually placed into an **executable HTML context**.

For example, if the application takes the metadata retrieved from our server and inserts it into its HTML output without proper sanitization or context-appropriate encoding, that data may become HTML markup instead of remaining plain text. OWASP emphasizes that output encoding must be appropriate for the context in which the data is rendered.

For testing purposes, it is better to host the content as a complete and valid HTML document, but the minimal example above is sufficient to demonstrate the concept.

Once I confirmed that the `test123` value was being retrieved from the external HTML document and reflected in the application's output, I modified the HTML file on my server and placed an XSS payload inside the metadata:

```
<head>
    <meta name="viewport" content="<img src=1 onerror=alert(`xss`)>">
</head>
```
I then submitted the URL of the modified HTML document to the application again.

If the application retrieves the metadata and inserts it into its HTML output without proper sanitization, the payload can be interpreted as HTML markup rather than plain text, resulting in XSS.

What makes this scenario interesting is that the XSS entry point isn’t necessarily a traditional input such as a search box or form field.

Instead, the application first:

1. Fetches an attacker-controlled URL.
2. Extracts part of its HTML metadata.
3. Places that data into the application’s output.
4. Allows the browser to interpret it as HTML.

This is a good reminder that when testing URL-based functionality, the entire data flow should be considered — not just direct user input.

## 3. XSS Through MIME Type Manipulation in a File Viewer

In the third scenario, the application had a file upload feature where users could upload files such as PNG images.

Normally, simply creating a PNG file containing an XSS payload does not cause JavaScript to execute. The fact that arbitrary text is present inside a file with a `.png` extension does not, by itself, make the browser interpret that content as HTML.

However, there was an interesting detail in this application.

After uploading a file, it was displayed through a dedicated viewer, and the file type was specified in the URL.

For example:

I created a file with a `.png` extension, but instead of putting actual image data inside it, I placed HTML content containing an XSS payload:

I uploaded the file and observed that the viewer displayed it using:

I then manually changed the parameter to:

The request became:

Because the viewer trusted the `type` parameter when determining how the uploaded content should be served, the stored content was now interpreted as HTML, and the XSS payload executed.

The vulnerability was therefore not simply “uploading a PNG containing XSS.”

Instead, it was a combination of several insecure behaviors:

```
Upload arbitrary content
        ↓
File stored with .png extension
        ↓
File exposed through a viewer
        ↓
Viewer trusts user-controlled MIME type
        ↓
type=image/png → type=text/html
        ↓
Browser interprets content as HTML
        ↓
XSS
```
This is an important distinction when testing file upload functionality.

## Get Hossein Zarei’s stories in your inbox

Join Medium for free to get updates from this writer.

Don’t focus only on the file extension validation. Also investigate how the uploaded file is ultimately served, how its `Content-Type` is determined, whether a dedicated viewer is involved, and whether any user-controlled parameter can influence how the file is interpreted.

## 4. XSS via an `embed` Element and a `data:` URL

The fourth case involved an application that used the `<embed>` element to display an image.

For example, the request looked similar to:

The page source contained an element similar to:

Since the `src` value was controllable, I started testing whether I could change the MIME type used in the `data:` URL from `image/png` to another type.

The general syntax of a `data:` URL is:

Therefore, one of the payloads worth testing in this context is:

Here, `text/html` indicates that the content of the `data:` URL is HTML.

However, the payload that worked successfully in my test was:

The Base64 portion of this payload represents content equivalent to an SVG element containing an event handler.

The final request therefore looked like this:

The payload successfully resulted in JavaScript execution.

The interesting part of this scenario is that when an application places user-controlled input directly into the `src` attribute of an element such as `<embed>`, you shouldn't limit your testing to conventional `http://` URLs or expected image formats.

Schemes such as `data:` and MIME type manipulation can introduce an entirely different attack surface.

The `<embed>` element uses its `src` attribute as the URL of the resource being embedded, making the handling and validation of attacker-controlled URLs particularly important.

It is also worth noting that the exact behavior of these payloads can depend on the browser and how the embedded content and MIME type are handled. Therefore, when reporting this type of issue, it is a good idea to document the browser and exact testing conditions.

## 5. Bypassing Uppercase Input Transformation with HTML Entities

The final case was one of the simplest but most interesting bypasses I encountered.

On this target, user input was automatically converted entirely to uppercase before being reflected into the page source.

For example, if I submitted:

the application reflected it as:

At first glance, this transformation appeared capable of interfering with common XSS payloads.

For example:

would effectively become:

The key detail here is that HTML treats tag and attribute names without regard to letter casing, while JavaScript treats identifiers differently.

As a result, changing `alert` to `ALERT` can prevent the original JavaScript expression from working. The automatic uppercase transformation was therefore enough to break the straightforward approach.

I also experimented with different encoding techniques, including Unicode representations and HTML character references, but the initial approaches did not produce the result I was looking for.

Instead of continuing with the same approach, I decided to test a different HTML context.

I focused on an image element and its error-handling mechanism. This provided a different execution path that was not affected in the same way by the application’s uppercase transformation.

The test payload was:

After the application converted the input to uppercase, it appeared in the source as:

However, unlike the previous payload, this one executed successfully.

The reason is that HTML character references are decoded while the HTML is being parsed. The resulting value is therefore interpreted by the event handler as:

The uppercase transformation does not cause a problem for the HTML tag or attribute names, and changing the case of the hexadecimal characters inside the character references does not prevent them from being decoded.

This case taught me an important lesson:

**When a simple sanitization or transformation breaks an XSS payload, don’t immediately assume that XSS is no longer exploitable. First identify the output context, then determine whether the transformation actually affects the final syntax interpreted by the browser.**

## Conclusion

All five of these cases had one thing in common for me: finding XSS is often much more than simply finding a reflection point and sending :

Sometimes you need to understand exactly where the data is being placed, which layer of the application stack processes it, what encoding or transformation is applied to it, and how the browser ultimately parses the resulting data.

In these cases, techniques and concepts such as:

- URL encoding
- Server-side URI parsing
- HTML metadata
- MIME types
- `data:` URLs
- `<embed>`
- HTML entities
- Event handlers
- Case transformation

all played a role in reaching successful XSS execution.

I hope these techniques were useful and that you can apply the underlying ideas in your future testing.

If you found the article useful, I’d really appreciate a Clap 👏 to help more people discover these techniques and experiences.
