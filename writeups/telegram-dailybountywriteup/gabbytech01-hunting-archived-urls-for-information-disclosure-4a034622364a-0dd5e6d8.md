# Hunting archived URLs for information disclosure

- **Source URL:** https://medium.com/@gabbytech01/hunting-archived-urls-for-information-disclosure-4a034622364a
- **Fetched from:** https://medium.com/@gabbytech01/hunting-archived-urls-for-information-disclosure-4a034622364a?source=rss-84e5795bdfd8------2
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14940 (id 14940)
- **Method:** medium-rss-feed (full content:encoded) readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- **Author/Published (RSS):** Gabriel Odusanya / Thu, 08 Oct 2026 15:43:40 GMT

The Wayback Machine keeps copies of pages it has already crawled. Its CDX API lets you list those URLs. That list is a lead. It is not a vulnerability, and a filename match is not a report.

Use it only on a programme that allows this kind of research, and only on in-scope hosts. Many programmes reject unvalidated scanner output and low-impact disclosure that contains no secrets.

The request has to be exact

The host is \`web.archive.org\`, not \`webarchive.org\`. Parameters are separated with \`&\`. The field parameter is \`fl\` (the letter L). \`f1\` is ignored. \`output=json\` is the documented format. \`output=text\` is not.

A browser query looks like this:

\`url\` is the pattern. \`\*.example.com/\*\` means subdomains and paths. \`collapse=urlkey\` keeps one row per unique URL instead of every snapshot. \`fl=original\` returns only the original URL. \`limit=100\` stops a wildcard from dumping a huge index. Raise it only after the small query works.

From a terminal, encode the parameters so the wildcard is not mangled:

curl -G “[https://web.archive.org/cdx/search/cdx](https://web.archive.org/cdx/search/cdx)" — data-urlencode “url=\*.example.com/\*” — data-urlencode “collapse=urlkey” — data-urlencode “output=json” — data-urlencode “fl=original” — data-urlencode “limit=100” -o output.txt

That \`curl\` command writes the file. \`du -h output.txt\` does not download anything. It only prints how large the file already is.

What each field means

A default CDX row contains \`urlkey\`, \`timestamp\`, \`original\`, \`mimetype\`, \`statuscode\`, \`digest\`, and \`length\`. Asking for \`original\` alone is enough for a first pass. Add \`timestamp\` and \`statuscode\` if you want to know when it was crawled and whether the archive saw a 200.

Useful extras, still on the same endpoint:

\- \`filter=statuscode:200\` keeps captures that succeeded at the time.

- \`from=2020&to=2024\` limits the years.

- \`output=json\` returns a header row, then one array per URL.

A filename filter is a lead, not a finding

After you have \`output.txt\`, strip duplicates and search for names that often mark backups, configs, and dumps. Images and ordinary markdown are noise.

grep -E ‘\.sql|\.bak|\.backup|\.zip|\.tar|\.tgz|\.gz|\.config|\.ya?ml|\.env|\.key|\.pem|\.log|\.db’ output.txt

A hit means the archive once indexed that path. It does not mean the file is still online, or that it contains a secret.

If the live URL now returns 404, paste the same URL into web.archive.org and open an older snapshot. Read only enough to see whether the snapshot has credentials, customer data, or a private key. If it does, stop and report it through the programme. Do not crawl the rest of the file, and do not attach someone else’s data to a write-up.

What programmes usually pay

Eligible disclosure is a file or response that exposes something sensitive: a database dump, a cloud key, a private key, an internal config with secrets. A public JavaScript file, a logo, a \`.md\` readme, or a stack trace with no secrets is normally closed as informational. Missing security headers are a different issue, and many programmes exclude them outright.

Before you send it, check three things. The host is in scope. You are the first report. The proof is a screenshot of the sensitive part, with tokens redacted, plus the archived URL and the date of the snapshot. One issue per report. Delete the artifact when they close it, if the policy says to.

What not to do

Do not point this workflow at a company that has no programme. Do not treat blog, roadmap, or third-party plugin hosts as in scope just because the wildcard returned them. Do not run the filename list as if every match were a live backup. The archive remembers URLs. The programme pays only when those URLs still prove a real exposure.
