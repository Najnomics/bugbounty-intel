# RCE by finding secret hidden files via Encryption and hashing

- **Source URL:** https://medium.com/@karim.engmohamed/%D8%A7%D9%84%D8%B3%D9%84%D8%A7%D9%85-%D8%B9%D9%84%D9%8A%D9%83%D9%85-e37717c23cfd?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20241109230824/https://medium.com/@karim.engmohamed/%D8%A7%D9%84%D8%B3%D9%84%D8%A7%D9%85-%D8%B9%D9%84%D9%8A%D9%83%D9%85-e37717c23cfd
- **Fetched:** 2026-11-19
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/7817 (id 7817)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
السلام عليكم

- Many of you get subdomains and try to find hidden directories by using tools like dirsearch but the fact is, this is not enough as many secret files can be hidden via some hashed string or encryption so try this next time you are hunting

1. Using Hashes and Encodings for File Discovery

Instead of just trying common file names, this technique involves creating hashed and encoded values of typical file names (uploads, cmd, index, const) using algorithms like MD5, SHA-1, SHA-256, or base64.

Example:- https://example.com/(hash).php


By doing this, you increase the chance of finding files that might be hidden under hashed or encoded names.

You can create modified wordlists like this.

Base64 Encoding:-

```
cat list.txt | while read row; do
echo -n "row" | base64 | tee -a
base64list.txt;
```
2.Using ‘ffuf’ for Fuzzing

With the generated wordlists, you can use ffuf to check multiple file types and hash values.

Example:-

```
ffuf -w base64list.txt:/W1 -w
extentions.txt:/W2 -u "https://example.com/W1.W2" -mc 200
```
This allows you to test combinations of hash values or encoded values with different file extensions (like \`.php\`, \`.bak\`, zip….).
