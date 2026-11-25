# File Upload Bypass to Remote Code Execution (RCE) HEXAPHP

- **Source URL:** https://hexaphp.medium.com/file-upload-bypass-to-remote-code-execution-rce-hexaphp-cbb7e5f09175?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20260326232411/https://hexaphp.medium.com/file-upload-bypass-to-remote-code-execution-rce-hexaphp-cbb7e5f09175?source=rss------bug_bounty-5
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/13281 (id 13281)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# **File Upload Bypass to Remote Code Execution (RCE) HEXAPHP**

## Introduction

Hello everyone,

I’m Aland Dlshad, also known as HexaPHP. I’m a cybersecurity specialist focused on web application penetration testing and vulnerability research.

In this write-up, I present the discovery of a critical Remote Code Execution (RCE) vulnerability in a file upload functionality. The issue was caused by insufficient validation of uploaded files, allowing manipulation of filenames and paths. By combining a double extension technique with path traversal, it was possible to bypass restrictions and upload a malicious file to an unintended location, ultimately leading to full system compromise.

## Discovery Process

The assessment began by registering a normal user account. At first glance, the application appeared to function as expected, with no obvious vulnerabilities.

While exploring the features, attention was drawn to the profile section, where users were allowed to upload a profile picture. This functionality became the primary target for testing.

As an initial step, a standard image file was uploaded using:

`filename="11.png"`
The upload succeeded without restrictions. Afterward, the file path was identified, confirming that uploaded files were stored and accessible within the same domain. This indicated that user-controlled files could potentially be accessed directly via the web.

## Initial Testing

To evaluate the robustness of the upload validation, the filename was modified to:

`filename="11.php"`
Although the file upload was accepted, it did not execute as PHP code. This suggested that some level of filtering or handling was in place, but not comprehensive enough.

Multiple bypass attempts were performed, including variations in extensions and encoding techniques however, these attempts did not initially succeed.

## Bypassing File Upload Restrictions

Further testing focused on manipulating both the filename and the request headers.

In the final attempt, the upload request was modified as follows:

Changed the `Content-Type` to:

`application/x-php`
Modified the filename to:

`../11.png.php`
This payload combined two important techniques:

- **Double Extension** (`.png.php`) to bypass extension filtering
- **Directory Traversal** (`../`) to move one level back from the intended upload directory

The upload was successful, confirming that the validation mechanism could be bypassed and that files could be written outside the designated directory.

## Conclusion

This vulnerability demonstrates the risks associated with improper file upload validation. Relying solely on client-controlled attributes such as filename or content type is insufficient and can be easily bypassed.

To mitigate such issues, developers should:

- Enforce strict server-side validation and file type whitelisting
- Sanitize and normalize filenames
- Store uploaded files outside the web root
- Rename files to prevent user-controlled naming
- Disable execution permissions in upload directories

Implementing these controls is essential to prevent exploitation and ensure the security of web applications.

## Contact

If you’d like to connect or learn more about my work:

**https://hexaphp.com**
