# Blind XSS on Registration System

- **Source URL:** https://medium.com/@aurelioyudistira/blind-xss-on-registration-system-410eb0b98109?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20240105162858/https://medium.com/@aurelioyudistira/blind-xss-on-registration-system-410eb0b98109?source=rss------bug_bounty-5
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/4660 (id 4660)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
Banyak dari kita yang sering menggunakan website-website di internet. Namun, apakah kalian yakin data-data yang kalian masukkan di dalam website tersebut terjaga dengan baik keamanannya?

Dalam kesempatan ini saya menemukan kerentanan di salah satu subdomain milik pemerintah. Kerentanan yang saya temukan berupa “Blind XSS” yang terdapat pada sistem registrasi, berikut PoC nya

1. Masuk ke bagian register dari website korban
2. Ganti data-data seperti username menjadi payload XSS

3\. Klik register, kemudian kemudian cek ke XSS Hunter.

Sebagai tambahan, informasi pribadi user dapat digunakan untuk **Account Stealing**

Semoga bermanfaat!
