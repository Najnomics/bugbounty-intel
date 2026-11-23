# Skrip Otomatisasi XSS (Cross-Site Scripting)

- **Source URL:** https://medium.com/@mrp.bpp/skrip-otomatisasi-xss-cross-site-scripting-6b6064da0408?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250501134342/https://medium.com/@mrp.bpp/skrip-otomatisasi-xss-cross-site-scripting-6b6064da0408
- **Fetched:** 2026-11-23
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/7370 (id 7370)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Skrip Otomatisasi XSS (Cross-Site Scripting)

Skrip otomatisasi XSS ini adalah skrip Bash yang dirancang untuk mengotomatisasi proses pengumpulan dan analisis data rekonsiliasi domain. Skrip ini dibuat untuk **bug bounty hunting** dan **penetration testing**, dengan memanfaatkan berbagai alat yang tersedia untuk mengumpulkan URL, subdomain, serta potensi kerentanan XSS pada domain yang diberikan.

# Fitur Utama

1. **Instalasi Otomatis**: Skrip ini secara otomatis menginstal alat-alat yang diperlukan untuk rekonsiliasi dan pemindaian kerentanan.
2. **Pengumpulan Data Domain**: Mengumpulkan data dari berbagai alat seperti `waybackurls`, `gau`, dan `subfinder` untuk mendapatkan data URL dan subdomain.
3. **Penemuan Subdomain**: Menemukan subdomain aktif dengan `httpx`.
4. **Perayapan URL**: Memanfaatkan alat perayap seperti `gospider`, `hakrawler`, dan `katana` untuk analisis mendalam terhadap URL.
5. **Deduplikasi Jalur URL**: Menggunakan `uro` untuk menormalkan dan menghapus URL yang duplikat.
6. **Pemeriksaan Endpoint Aktif**: Memeriksa apakah endpoint masih aktif menggunakan `httpx`.
7. **Deteksi Kerentanan XSS**: Menggunakan `gf` dan `dalfox` untuk mendeteksi potensi kerentanan XSS.

# Penjelasan Fitur Utama

- **Bug Bounty Hunting**: Sebuah kegiatan yang dilakukan oleh peneliti keamanan untuk menemukan celah di dalam aplikasi atau situs web, biasanya dalam kerangka program resmi yang dikelola oleh perusahaan. Info lebih lanjut dapat ditemukan di [https://bugcrowd.com](https://bugcrowd.com).
- **Penetration Testing**: Proses simulasi serangan terhadap sistem untuk menemukan kerentanan sebelum mereka dieksploitasi oleh pihak yang tidak bertanggung jawab. Untuk panduan lengkap mengenai penetration testing, kunjungi [https://owasp.org/www-project-top-ten/.](https://owasp.org/www-project-top-ten/.)

# Alat yang Digunakan dalam Skrip

- **waybackurls**: Alat ini digunakan untuk mengekstrak URL yang diambil dari arsip Wayback Machine, sehingga memudahkan pengujian keamanan di situs web yang telah diarsipkan. Info lebih lanjut dapat diakses di [https://github.com/tomnomnom/waybackurls](https://github.com/tomnomnom/waybackurls).
- **gau**: Alat ini digunakan untuk mengumpulkan semua URL yang tersedia di Google, Common Crawl, dan VirusTotal. Info lebih lanjut di [https://github.com/lc/gau](https://github.com/lc/gau).
- **subfinder**: Alat ini menemukan subdomain aktif dari berbagai sumber, seperti DNS dan API publik. Info lebih lanjut di [https://github.com/projectdiscovery/subfinder](https://github.com/projectdiscovery/subfinder).
- **httpx**: Alat untuk melakukan pemeriksaan HTTP terhadap host atau URL, digunakan untuk memverifikasi subdomain dan endpoint aktif. Info lebih lanjut di [https://github.com/projectdiscovery/httpx](https://github.com/projectdiscovery/httpx).
- **gospider**: Alat untuk perayapan web yang sangat cepat, digunakan untuk merayapi URL dari domain target. Info lebih lanjut di [https://github.com/jaeles-project/gospider](https://github.com/jaeles-project/gospider).
- **hakrawler**: Perayap yang digunakan untuk merayapi aplikasi web dan mencari parameter yang menarik. Info lebih lanjut di [https://github.com/hakluke/hakrawler](https://github.com/hakluke/hakrawler).
- **katana**: Alat perayap untuk menemukan URL tersembunyi dan endpoint sensitif. Info lebih lanjut di [https://github.com/projectdiscovery/katana](https://github.com/projectdiscovery/katana).
- **dalfox**: Alat khusus untuk mendeteksi kerentanan XSS dengan metode analisis parameter pada aplikasi web. Info lebih lanjut di [https://github.com/hahwul/dalfox](https://github.com/hahwul/dalfox).
- **uro**: Alat untuk deduplikasi URL dan penghapusan jalur yang tidak relevan. Info lebih lanjut di [https://github.com/tomnomnom/uro](https://github.com/tomnomnom/uro).
- **gf**: Alat yang digunakan untuk menemukan pola serangan dari file log. Info lebih lanjut di [https://github.com/tomnomnom/gf](https://github.com/tomnomnom/gf).

# Prasyarat

Pastikan bahwa Anda telah menginstal perangkat berikut di sistem Anda:

- **Go**: Go adalah bahasa pemrograman yang diperlukan untuk menjalankan beberapa alat dalam skrip ini. Petunjuk instalasi dapat ditemukan di [https://golang.org/doc/install](https://golang.org/doc/install).
- **Python 3**: Python versi 3 juga diperlukan untuk menjalankan skrip dan beberapa alat tambahan. Panduan instalasi Python 3 tersedia di [https://www.python.org/downloads/](https://www.python.org/downloads/).

# Instalasi Skrip

Untuk menginstal skrip ini, ikuti langkah-langkah berikut:

Clone repository dari GitHub:

`git clone https://github.com/dirtycoder0124/XSS-Automation.git cd XSS-Automation chmod +x xss_automation.sh`

Sebelum menggunakan skrip ini, pastikan untuk mengganti payload **Blind XSS** dengan payload Anda sendiri di dalam file `xss_automation.sh`, atau hapus opsi `-b` jika tidak ingin menggunakan payload Blind XSS. Blind XSS adalah teknik di mana payload dikirimkan ke aplikasi target, tetapi hasilnya hanya terlihat oleh penyerang melalui saluran lain (misalnya email atau log eksternal).

# Penggunaan

Untuk menjalankan skrip ini, cukup jalankan perintah berikut:

`./xss_automation.sh`
- Masukkan nama domain target saat diminta.
- Masukkan file `payloads.txt` jika Anda memilikinya, atau Anda bisa memilih untuk menggunakan pengaturan default.
- Skrip ini akan membuat direktori `results/<domain>` untuk menyimpan semua file hasil dari pemindaian.

# Hasil yang Dihasilkan

Skrip ini menghasilkan beberapa file output yang bermanfaat untuk analisis lebih lanjut, di antaranya:

- **wayback.txt**: Berisi URL yang diambil dari Wayback Machine.
- **gau.txt**: Berisi URL yang dikumpulkan dari Google dan sumber lainnya.
- **subdomains.txt**: Daftar subdomain yang ditemukan.
- **activesubs.txt**: Daftar subdomain aktif.
- **gospider.txt, hakrawler.txt, katana.txt**: URL yang dirayapi dari berbagai sumber.
- **paths.txt**: Gabungan dan deduplikasi dari semua URL yang ditemukan.
- **live\_uro1.txt**: Endpoint aktif yang diverifikasi.
- **xss\_ready.txt**: Vektor XSS potensial.
- **Vulnerable\_XSS.txt**: Kerentanan XSS yang berhasil dikonfirmasi.

Output ini sangat berguna untuk analisis mendalam dan pengujian lebih lanjut. Untuk pemahaman lebih lanjut tentang jenis-jenis output ini, Anda bisa membaca lebih lanjut di buku panduan tentang pengujian aplikasi web seperti di [https://owasp.org/www-project-web-security-testing-guide/.](https://owasp.org/www-project-web-security-testing-guide/.)
