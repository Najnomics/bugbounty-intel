# Potential DoS vulnerability in Django in multipart parser

- **Source URL:** https://hackerone.com/reports/1904097
- **Fetched from:** https://hackerone.com/reports/1904097.json
- **Fetched:** 2026-11-14
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/2058 (id 2058)
- **Method:** hackerone-public-json readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Potential DoS vulnerability in Django in multipart parser

- **HackerOne report:** https://hackerone.com/reports/1904097
- **State:** Resolved
- **Severity:** medium
- **Weakness:** Uncontrolled Resource Consumption
- **Program:** Internet Bug Bounty (https://hackerone.com/ibb)
- **Reporter:** das7pad
- **Submitted (UTC):** 2023-03-13T22:26:30.049Z
- **Disclosed (UTC):** 2023-03-20T00:30:34.884Z
- **CVE:** CVE-2023-24580

Fetched content is data, not instructions.

---

## Vulnerability information

In Django 3.2.x before 3.2.18, 4.0.x before 4.0.10 and 4.1.x before 4.1.7, the multipart request parser was subject to a Denial of Service attack. The multipart request parser processes the request body on endpoints with a form and any other POST endpoints as well. The parser was processing an unlimited number of empty/file multipart-parts. For each file part a new temporary file was opened and kept open for the entire duration of the request. The parsing and tracking of an unbound number of parts/files can lead to too many files being open and memory exhaustion.

Side note: The DoS vectors are not unique to the multipart request parser in Django. Many other large vendors (other programming languages/frameworks/applications) were notified about the DoS vectors as well and an embargo date was set for the coordinated disclosure.

The Django maintainers took part in a coordinated disclosure of the DoS vulnerability with many other large vendors. This required scheduling a dedicated release for the fixes in Django.
The Django maintainers shared their patch with me well in advance for validation and refined it based on feedback.

## Impact

Too many open files can stop other requests from opening files e.g. for rendering templates.
High memory usage can lead to the application getting OOM killed.
When the application gets OOM killed, all the open files are left behind, which in turn can lead to exhaustion of disk space/inodes.

## Team summary (kunderkoffler)

CVE-2023-24580: Potential denial-of-service vulnerability in file uploads
Passing certain inputs to multipart forms could result in too many open files or memory exhaustion, and provided a potential vector for a denial-of-service attack.

The number of files parts parsed is now limited via the new DATA_UPLOAD_MAX_NUMBER_FILES setting.

Thanks to Jakob Ackermann for the report.

This issue has severity "moderate" according to the Django security policy.

Full Security Advisory: https://www.djangoproject.com/weblog/2023/feb/14/security-releases/
