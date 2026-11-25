# How I Found My First Bug

- **Source URL:** https://medium.com/@atitofffff/how-i-found-my-first-bug-information-disclosure-via-exposed-directory-listing-5589bc190c5c
- **Fetched from:** https://medium.com/@atitofffff/how-i-found-my-first-bug-information-disclosure-via-exposed-directory-listing-5589bc190c5c?source=rss-e8206667325e------2
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14968 (id 14968)
- **Method:** medium-rss-feed (full content:encoded) readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- **Author/Published (RSS):** ATIT0 / Mon, 02 Nov 2026 17:44:01 GMT

While conducting a routine reconnaissance and asset discovery phase on a target bug bounty program back in January 2025, I stumbled upon a common yet misconfiguration that often slips past developers: an exposed static directory listing.

In this write-up, I want to walk you through how I discovered this information disclosure vulnerability, starting from a seemingly dead subdomain all the way to uncovering exposed server files, version control artifacts, and tracking how the issue was eventually remediated.

During the enumeration process, I used subdomain enumeration tools to discover potential targets belonging to the organization. One of the subdomains I found initially returned a **Page not found** or seemed completely inactive when visiting it directly in the browser.

However, instead of ignoring it, I decided to run a directory and path fuzzing session using **ffuf** to check for any hidden paths or directories that might be lurking beneath the surface.

ffuf -u https://sub.domain.com/FUZZ -w wordlist.txt -mc 200

After running the fuzzing process, I noticed that a specific path responded successfully, revealing a hidden directory named static:

https://sub.domain.com/static/

When I navigated to that URL, instead of a standard 403 Forbidden or error page, the web server responded with an open directory index (Index of /static). This meant that directory listing was enabled on the server, exposing the entire file tree structure of that directory to anyone on the internet.

Upon inspecting the directory index, I found several sensitive files, configuration scripts, and version control artifacts exposed:

An exposed static directory and version control artifacts carry multiple security risks if leveraged by a malicious actor:

Every bug hunter knows the bitter-sweet feeling of receiving a **“Duplicate”** status on a report. After submitting this finding to the program, the triage team closed the report as a duplicate because another researcher had reported it slightly earlier.

However, finding a bug is only part of the learning curve, tracking how platforms handle security over time is another. When I decided to look for the exact same static endpoint (/static/) later on, I noticed a significant change.

The organization had cleaned up their assets, sensitive version control folders .svn/ and internal testing paths were removed, showing that the security team eventually hardened the endpoint.

Writing about this journey reminded me of two essential lessons every bug hunter should keep in mind:

Keep hacking, stay curious, and see you in the next write-up.
