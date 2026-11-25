# ​Broken Authentication ability to ATO via JWT Algorithm Manipulation

- **Source URL:** https://skysenz.medium.com/broken-authentication-ability-to-ato-via-jwt-algorithm-manipulation-bfc2ba500787?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20260323171116/https://skysenz.medium.com/broken-authentication-ability-to-ato-via-jwt-algorithm-manipulation-bfc2ba500787?source=rss------bug_bounty-5
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/13039 (id 13039)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Broken Authentication ability To Privilege Escalation via JWT Algorithm Manipulation

1 min readJust now

## Summary:

Gua nemuin kerentanan bac atau privilage lebih tepatnya, di implementasi JWT. Backend tidak melakukan validasi algoritma signature dengan benar sehingga penyerang dapat mengubah algoritma menjadi none, memodifikasi payload misal: mengubah role menjadi admin dan mendapatkan akses penuh tanpa secret key.

## Steps to Reproduce:

1.Login sebagai user biasa dan tangkap request menggunakan Burp Suite.

2.Ambil JWT dari header Authorization: Bearer.

Decode JWT (bisa pakai JWT.io atau extension Burp).

3\. ubah header seperti contoh dibawah

```
header: "alg": "HS256" menjadi "alg": "none".
Ubah payload: "role": "user" menjadi "role": "admin".
Hapus bagian signature (karakter setelah titik kedua), tapi sisakan titiknya. Format: header.payload.
```
4.Kirim request kembali dengan token modifikasi tersebut ke endpoint admin (misal: /api/admin/settings).

5.Result: Server menerima token dan memberikan akses admin

Impact / dampak

Penyerang dapat mengambil alih akun administrator Privilege Escalation mengakses data sensitif seluruh user, dan memodifikasi konfigurasi sistem secara ilegal
