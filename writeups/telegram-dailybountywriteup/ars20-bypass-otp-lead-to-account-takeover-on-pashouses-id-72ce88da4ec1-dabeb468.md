# Bypass OTP Lead to Account Takeover on pashouses.id

- **Source URL:** https://medium.com/@ars20/bypass-otp-lead-to-account-takeover-on-pashouses-id-72ce88da4ec1?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20230507204816/https://medium.com/@ars20/bypass-otp-lead-to-account-takeover-on-pashouses-id-72ce88da4ec1
- **Fetched:** 2026-11-24
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/2495 (id 2495)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
Pada bulan Feb 2023, ini salah satu bug yang saya laporkan & sudah di patch dengan cukup baik (+/- 3 hari).

Pada saat itu saya sedang scrolling instagram dan tidak sengaja lewat iklan dari Pashouses, kebetulan juga saya lagi membuka burpsuite (Tools Pentes). Akhirnya iseng — iseng & kepikiran untuk cari bug di website Pashoses.

Pertama kali sempet mikir kayanya gak mungkin ada karena setelah dibrowsing Pashouses salah satau perusahaan yang lumayan terkenal dalam hal jual beli rumah. Jadi cuma modal nekat doang buat nge-Pentes ni web.

Setelah mencari bug di tiap — tiap fitur, dari A — Z akhirnya saya notice kalo dibagian *daftar* dan *reset password* ada pesan yang dikirim web ke user ketika memasukan OTP. Yaitu pesan *Sukses* atau *Gagal* yang udah pasti pesan tersebut dikirimkan melalui server. Sehingga saya kepikiran untuk menggunakan 2 nomor berbeda. Nantinya nomor pertama akan saya gunakan untuk mendaftar akun dan memasukan OTP yang valid. Sehingga dengan begitu saya bisa melihat pesan yang dikirimkan server ketika user memasukan OTP yang valid.

Gambar di atas merupakan pesan yang dikirim server ketika user memasukan OTP yang valid *“next\_flow”: 1* merupakan kode tahap pendaftaran. Lalu saya mencoba melakukan Bypass OTP saat proses pendaftaran pada nomor kedua dan hasilnya berhasil :)

Akun di atas adalah hasil Bypass OTP yang terbukti berhasil dan gak berhenti sampai di situ. Ternyata di website Pashouses ketika user ingin login juga membutuhkan OTP. Sehingga saya mencoba melakukan Bypass OTP kedua yang bertujuan men-Takeover akun yang udah saya daftarkan tadi.

Ternyata kalo kalian sadar. Pesan yang dikirimkan server sebelumnya yaitu *“next\_flow”: 1* bisa dirubah menjadi angka 2 untuk menandakan bahwa user sedang melakukan proses reset password. Sehingga dengan begitu saya tinggal login menggunakan nomor target yang ingin diambil alih akun nya dan mem-Bypass OTP login tersebut menggunakan pesan server yang udah didapat sebelumnya. Tapi jangan lupa untuk merubah *“next\_flow”: 1* menjadi *“next\_flow”: 2*.

BERESS DAH !! Stay Safe ya.

**Timeline:**

06 Feb 2023 — Reporting Bug

08 Feb 2023 — Verification Bug

13 Feb 2023 — Bug Fixed & Rewarded
