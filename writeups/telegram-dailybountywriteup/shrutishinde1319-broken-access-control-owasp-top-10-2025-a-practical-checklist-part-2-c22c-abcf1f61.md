# Broken Access Control OWASP Top 10 (2025)

- **Source URL:** https://medium.com/@shrutishinde1319/broken-access-control-owasp-top-10-2025-a-practical-checklist-part-2-c22c078e0cae
- **Fetched from:** https://medium.com/@shrutishinde1319/broken-access-control-owasp-top-10-2025-a-practical-checklist-part-2-c22c078e0cae?source=rss-85fdc83f6cda------2
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:**  (id 14937)
- **Method:** medium-rss-feed (full content:encoded) readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- **Author/Published (RSS):** Shruti Vijay Shinde / Wed, 07 Oct 2026 06:16:33 GMT

Hey everyone! 👋

In [Part 1](https://medium.com/@shrutishinde1319/broken-access-control-owasp-top-10-2025-the-1-web-security-risk-d843bd36ef5e?postPublishedType=repub), we covered the basics of **Broken Access Control (BAC)** — IDOR, horizontal and vertical privilege escalation, and forced browsing.

Now let’s make it practical.

Start with:

https://target.com/robots.txt

https://target.com/sitemap.xml

Sometimes robots.txt reveals interesting paths:

Disallow: /admin-panel/

Disallow: /internal/

Disallow: /staff/

These paths aren’t necessarily protected. If you find something interesting, check whether the application actually enforces authorization.

**Remember:** robots.txt tells search engines what not to crawl. It doesn't protect a page from attackers.

Check the page source, JavaScript files, and Network tab in DevTools.

Look for:

For example:

```
if (user.role === "admin") {
    showAdminPanel();
}
```
The button may be hidden from normal users, but the API endpoint behind it could still be accessible directly.

**Hiding a feature is not the same as protecting it.**

Whenever you see an ID in a request, try changing it.

GET /api/invoice?invoice\_id=1042

Try another value:

GET /api/invoice?invoice\_id=1043

Also look for:

If changing the reference gives you access to another user’s resource, it could indicate an **IDOR/Broken Access Control** vulnerability.

Don’t focus only on the request.

Sometimes the response contains information that isn’t visible in the UI:

```
{
  "status": "success",
  "user": {
    "role_id": 123
  }
}
```
You may find:

While testing an email update functionality, I noticed information in the response that wasn’t visible on the page.

**Always read the complete response not just the status code.**

UUIDs may look random:

550e8400-e29b-41d4-a716-446655440000

But randomness doesn’t replace authorization.

UUIDs can sometimes appear in API responses, team/member lists, URLs, invitation links, JavaScript files, or other places.

If you obtain another user’s UUID, check whether it can be used to access their resources:

GET /api/documents/\<uuid>

If the application returns the resource without checking whether you are authorized to access it, that’s still a Broken Access Control issue.

**Random ID ≠ Authorization.**

If you receive:

401 Unauthorized

403 Forbidden

don’t always assume the test is over.

Depending on the application architecture, different components such as reverse proxies, web servers, and backend applications may process the request differently.

For example, access-control bypass techniques may involve headers such as:

X-Original-URL: /admin/dashboard

X-Rewrite-URL: /admin/dashboard

These techniques don’t work everywhere, but they are worth understanding and practicing in authorized environments.

That’s where many access control issues begin.

Thanks for reading! 🙌

More practical security testing tips coming in the next part.
