# Image XSS on Exif.tools | Hacking exif.tools by image injection by CYBER KALKI

- **Source URL:** https://medium.com/@krivadna/image-xss-on-exif-tools-hacking-exif-tools-by-image-injection-by-cyber-kalki-63b7d1261a19?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20251003181023/https://medium.com/@krivadna/image-xss-on-exif-tools-hacking-exif-tools-by-image-injection-by-cyber-kalki-63b7d1261a19
- **Fetched:** 2026-11-19
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/11162 (id 11162)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# 🧠 Image XSS on Exif.tools | Hacking exif.tools by image injection by CYBER KALKI

I uncovered and demonstrated a multi-surface vulnerability on Exif.tools, chaining metadata reflection, open redirect, form upload bypass through successful image-based XSS.

🎯 Target Surface: Exif.tools Upload Endpoint

Exif.tools allows users to upload images and view their metadata. The backend parses EXIF fields and reflects them in a rendered HTML view. That reflection surface became my entry point as html renders unescaped.

🛡️ Mitigation Advice

For developers maintaining Exif.tools or similar platforms:

\- Sanitize reflected metadata before rendering

### Download images

https://github.com/krivadna/imagexss
