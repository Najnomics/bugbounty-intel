# Unauthenticated Access to Dinas Pendidikan Provinsi Jawa Barat Exposes 7,481 Visitor Records

- **Source URL:** https://medium.com/@augustkevinsanjaya/unauthenticated-access-to-dinas-pendidikan-provinsi-jawa-barat-exposes-7-481-visitor-records-66ebfcca53bb
- **Fetched from:** https://medium.com/@augustkevinsanjaya/unauthenticated-access-to-dinas-pendidikan-provinsi-jawa-barat-exposes-7-481-visitor-records-66ebfcca53bb?source=rss-90b1c3670526------2
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14980 (id 14980)
- **Method:** medium-rss-feed (full content:encoded) readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- **Author/Published (RSS):** Kevin Sanjaya / Thu, 12 Nov 2026 07:04:29 GMT

It started with a simple exploration of a government application in West Java, Indonesia.

While checking the Guest Book application belonging to the West Java Provincial Education Office, I came across an administrative dashboard that immediately caught my attention.

The /admin page was accessible directly from the internet. No login page, no authentication prompt, nothing.

Naturally, I wanted to understand whether this was just a frontend configuration issue or something deeper.

So, I opened Developer Tools and started looking at the requests being sent to the backend.

That’s when things got interesting.

The dashboard was fetching visitor records from a backend API. I noticed that the requests didn’t include an Authorization header or any session cookies.

Despite that, the server happily returned a successful response.

Here’s a simplified example of what I found:

```
{
  "status": 200,
  "message": "Sukses GET Guest",
  "data": {
    "count": 7481,
    "rows": [...]
  }
}
```
The response indicated **7,481 visitor records**.

What concerned me most wasn’t just the number. It was the kind of information contained in those records.

Some of the exposed fields included:

At that point, it was clear that this wasn’t simply an exposed admin dashboard. The backend was also allowing unauthenticated access to sensitive visitor information.

I also noticed an Excel export feature with date filters on the dashboard. Since I didn’t want to access more data than necessary, I deliberately avoided testing bulk exports.

Personal information on this scale should never be accessible without proper authorization.

A combination of NIK, phone numbers, addresses, and other personal details could potentially be used for identity theft, fraud, or targeted social engineering.

The issue was particularly concerning because accessing the application didn’t require any valid credentials.

From a security standpoint, this was a Broken Access Control vulnerability, accompanied by missing authentication controls on administrative resources.

**The estimated CVSS 3.1 score was 7.5 (High).**

I kept the testing as simple and limited as possible.

I only inspected the initial records needed to verify the issue. No data was modified, deleted, or downloaded in bulk. I also made sure that personal information in the screenshots was masked.

On **October 12, 2026**, I submitted my report to CSIRT Jabarprov through its official reporting channel.

After the disclosure process and subsequent follow-up, the vulnerability was eventually fixed.

I’m glad the issue was addressed, especially considering the amount and sensitivity of the information involved.

This finding is a good reminder that an application can look perfectly normal on the frontend while having serious security problems behind the scenes.

Protecting an administrative page isn’t enough. Every backend API handling sensitive information needs to enforce authentication and authorization independently.

Sometimes, all it takes is one missing access control check to expose thousands of records.

That’s why I believe responsible disclosure matters. Finding a vulnerability is only one part of security research. Making sure it gets fixed is just as important.

**Happy hacking!**

*Disclaimer: This article was written after the vulnerability had been fixed. Testing was limited to read-only verification and conducted for responsible disclosure purposes. No personal information or complete visitor records are shared in this publication.*
