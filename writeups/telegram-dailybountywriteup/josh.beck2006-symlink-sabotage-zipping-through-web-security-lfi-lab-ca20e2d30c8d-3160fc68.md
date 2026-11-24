# Symlink Sabotage

- **Source URL:** https://medium.com/@josh.beck2006/symlink-sabotage-zipping-through-web-security-lfi-lab-ca20e2d30c8d?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20240219034421/https://medium.com/@josh.beck2006/symlink-sabotage-zipping-through-web-security-lfi-lab-ca20e2d30c8d
- **Fetched:** 2026-11-24
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/5222 (id 5222)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
Objective: Learn how to exploit web applications that accept file uploads using symlinks within ZIP files.

Time to complete: \~20–30 minutes.

In this lab Participants will:

- Craft a unique ZIP file using Python, embedding a .pdf with a cleverly preserved symlink.
- Utilize this technique to navigate the web server’s filesystem.
- Locate the final flag in the web application source code using this technique.

VM with walkthrough can be found [here](https://humble-raptor-f30.notion.site/Symlink-Sabotage-ZIPping-Through-Web-Security-a1e93524ee374a16934286df0e20765d?pvs=4).
