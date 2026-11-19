# Bypassing Protocol Concatenation in SSRF

- **Source URL:** https://medium.com/@lopseg/bypassing-protocol-concatenation-in-ssrf-strategies-for-testing-vulnerable-applications-6c8f5f04128?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20230627043307/https://medium.com/@lopseg/bypassing-protocol-concatenation-in-ssrf-strategies-for-testing-vulnerable-applications-6c8f5f04128
- **Fetched:** 2026-11-19
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/2613 (id 2613)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Bypassing Protocol Concatenation in SSRF: Strategies for Testing Vulnerable Applications

--

TL;DR: In this blog post, we will explore different techniques to bypass the automatic concatenation of \`[https://\`](https://`) in a URL when testing for Server-Side Request Forgery (SSRF) vulnerabilities. These methods include using URL-encoded control characters, double or multiple URL schemes, and alternative protocols.

# Introduction

Server-Side Request Forgery (SSRF) is a security vulnerability that allows an attacker to make requests from a vulnerable server to other systems, potentially gaining unauthorized access to internal resources. One common obstacle faced by security researchers when testing for SSRF vulnerabilities is the automatic concatenation of \`[https://\`](https://`) at the beginning of a URL by the target application. In this blog post, we will discuss several techniques that can be used to bypass this behavior and successfully exploit SSRF vulnerabilities.

## 1. Using URL-encoded control characters

One way to bypass automatic protocol concatenation is by using URL-encoded control characters such as \`%00\`, \`%09\`, \`%0a\`, \`%0d\`, and \`%20\`. These characters can potentially break the concatenation and allow for a successful SSRF attack:

\`\`\`

[https://%00file:///etc/passwd](https://%00file:///etc/passwd)

[https://%09file:///etc/passwd](https://%09file:///etc/passwd)

\`\`\`

## 2. Double or multiple URL schemes

Another technique is to use double or multiple URL schemes in the hope that the application only removes the first instance of the \`[https://\`](https://`) protocol:

\`\`\`

[https://http://file:///etc/passwd](https://http://file:///etc/passwd)

[https://https://file:///etc/passwd](https://https://file:///etc/passwd)

\`\`\`

## 3. Alternative protocols and the data scheme

In some cases, using alternative protocols like the data scheme (\`data:\`) can help bypass the automatic concatenation of \`[https://\`](https://`). The data scheme allows you to include the content of a file directly in the URL:

\`\`\`

data:text/plain;base64,L2V0Yy9wYXNzd2Q=

\`\`\`

Other URL schemes that might prove helpful include \`gopher://\`, \`tftp://\`, and \`ftp://\`.

## Conclusion

Bypassing protocol concatenation when testing for SSRF vulnerabilities can be challenging. The techniques outlined in this blog post may not always work, as the success of these methods depends on the specific application and its vulnerabilities. However, by understanding and experimenting with these strategies, security researchers can improve their ability to identify and exploit SSRF vulnerabilities.

Remember, always perform security testing with the explicit consent of the system owner and adhere to responsible disclosure practices.

Happy hunting!
