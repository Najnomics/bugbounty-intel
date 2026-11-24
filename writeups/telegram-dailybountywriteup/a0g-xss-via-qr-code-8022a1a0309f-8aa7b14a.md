# XSS Via Qr Code

- **Source URL:** https://medium.com/@A0g/xss-via-qr-code-8022a1a0309f?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20230526023654/https://medium.com/@A0g/xss-via-qr-code-8022a1a0309f
- **Fetched:** 2026-11-24
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/2798 (id 2798)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# XSS Via Qr Code

--

Hi Al Salam Alykum, it’s a simple XSS but with a unexpected vulnerable point, i hope the write-up is clear, if not ping me, happy hacking.

While Reconnaissance we found an **http://example.com/index.html** path with a response code 200 which was unexpected as the main URL (**http://example.com**) is a login page, then after visiting it found a QR code scanner.

The button “ Code Scanner “ redirects to a GitHub tool “ [https://github.com/mebjas/html5-qrcode](https://github.com/mebjas/html5-qrcode) “ then we used the QR Generator website “ [https://www.the-qrcode-generator.com/](https://www.the-qrcode-generator.com/) “ to create our QR code.

First we embed a random text in the QR Code to see how the application is handling the scanner output.

Found that the application is printing the embed text.

When inspect the text we found that it printed via HTML span tag.

So we Created a new QR code with the simple following payload

“ \</span>\<img src=a onerror=alert(“XSS”)> “

After Uploading it we Got An Alert !!!
