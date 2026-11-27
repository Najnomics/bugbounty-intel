# Mendapatkan Akses SMTP Melalui Celah SQL Injection

- **Source URL:** https://rdnzx.medium.com/mendapatkan-akses-smtp-melalui-celah-sql-injection-f6d593fcad5e?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250906052426/https://rdnzx.medium.com/mendapatkan-akses-smtp-melalui-celah-sql-injection-f6d593fcad5e
- **Fetched:** 2026-11-27
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/7368 (id 7368)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Mendapatkan Akses SMTP Melalui Celah *SQL Injection*

### TL;DR

Saya menemukan celah keamanan ini pada website kampus saya, yang menggunakan aplikasi pihak ketiga (vendor) untuk sistem *e-learning*. Setelah menemukan celah tersebut, saya segera melaporkannya kepada vendor terkait. Saat ini, celah keamanan tersebut telah diperbaiki oleh pihak vendor. Namun, karena vendor tidak memberikan izin untuk mempublikasikan temuan ini secara lengkap, beberapa informasi sensitif akan saya sensor.

## Menemukan Celah *SQL Injection*

Beberapa waktu lalu, kampus saya mengumumkan bahwa aplikasi *e-learning* akan diperbarui ke versi terbaru. Sebagai mahasiswa, saya diundang untuk mengikuti sesi pengenalan aplikasi *e-learning* tersebut melalui *Zoom meeting*. Setelah pengumuman ini beredar, rasa penasaran saya muncul untuk mencoba menguji aplikasi berbasis web tersebut, yang disebut **SIAKAD-KAMPUS**. Rasa penasaran saya dipicu oleh informasi di halaman login, yang menyebutkan bahwa login ke aplikasi dilakukan menggunakan NIM dan NIK. Ini langsung menarik perhatian saya.

Saya segera mempersiapkan *tools* yang biasa saya gunakan, yaitu BurpSuite dan Kali Linux. Setelah itu, saya login ke aplikasi menggunakan kredensial yang tercantum pada papan pengumuman. Setelah berhasil login dan dialihkan ke halaman *dashboard*, saya mencoba mengakses berbagai fitur yang ada di aplikasi tersebut sambil menangkap *HTTP request* yang terjadi.

Hingga akhirnya, saya menemukan dua *URL Endpoint* yang menarik perhatian saya.

### #1 SQL Injection pada *URL Endpoint* /v1/pengumuman

*URL Endpoint* ini menarik perhatian saya untuk menguji serangan *SQL Injection*. Saya mulai menguji semua parameter yang ada pada *URL Endpoint* tersebut dengan menggunakan tanda petik (‘) untuk memeriksa apakah parameter tersebut rentan terhadap *SQL Injection*. Akhirnya, saya menemukan bahwa parameter `order[tanggalPublish]` menghasilkan *error MySQL*, yang menunjukkan bahwa parameter tersebut rentan terhadap serangan *SQL Injection* dan mengindikasikan bahwa sistem menggunakan *DBMS MySQL*.

Setelah mendapatkan informasi tersebut, saya coba mengeksploitasi menggunakan *tools* yang disebut *sqlmap.* Kemudian, saya membuka Kali Linux saya dan menjalankan *tools sqlmap* tersebut dengan perintah berikut :

Setelah menjalankan perintah tersebut, berikut adalah hasil dari *tools sqlmap* :

Gambar di atas merupakan hasil dari *tools sqlmap*, dan saya berhasil mendapatkan akses ke 301 *database* yang tersedia pada vendor ini. *Database-database* tersebut merupakan milik kampus-kampus yang juga menggunakan vendor ini. Wow, saya dapat mengakses informasi dari *database* kampus lain akibat celah SQL Injection ini. Menarik!

Dari celah ini saya dapat mengakses seluruh data admin, mahasiswa (nik, nama lengkap, alamat, nama orang tua, asal sekolah, dll)

(berlanjut ke URL Endpoint kedua).

### **#2 SQL Injection pada URL Endpoint /v1/mahasiswa/{id}/mutasi\_ccash/semua**

*URL endpoint* ini juga menarik perhatian saya karena terdapat dua parameter yang memunculkan *error MySQL* setelah saya mengujinya dengan menambahkan tanda petik (‘). Parameter tersebut adalah `tanggal[mulai]` dan `tanggal[hingga]`, yang mengindikasikan bahwa parameter ini rentan terhadap serangan *SQL Injection*.

Kemudian saya coba menggunakan *tools sqlmap* dan menjalankan perintah yang sama seperti pada sebelumnya. Dan berikut adalah hasil dari *tools sqlmap* :

*Database* tersebut merupakan milik kampus saya, kemudian saya mencoba melihat isi tabel dari *database* tersebut, dengan menambahkan perintah `--table`seperti berikut :

Berikut adalah hasil dari perintah yang dijalankan diatas :

Dapat dilihat pada gambar diatas, tabel **konfigsmtp** menarik perhatian saya. Biasanya nama tersebut berisikan konfigurasi kredensial sensitif untuk mengakses *SMTP (Simple Mail Transfer Protocol)* yang digunakan untuk mengirim email. Kemudian saya mencoba melihat kolom dari tabel tersebut dengan menambahkan perintah `--columns`:

Berikut adalah hasil yang didapat setelah menjalankan perintah diatas :

Setelah berhasil mendapatkan nama kolom yang terdapat pada tabel **konfigsmtp**, kemudian saya mencoba untuk melihat isi dari kolom-kolom tersebut dengan menambahkan perintah `-C nama_kolom,kolom1,kolom2 --dump`seperti berikut :

Berikut adalah hasil dari perintah yang dijalankan diatas :

Setelah mendapatkan informasi tersebut, saya mencoba memvalidasi apakah kredensial tersebut valid atau tidak. Saya membuat kode menggunakan PHP untuk memeriksa apakah saya dapat mengirim email dari email internal. Jika email berhasil terkirim, maka kredensial tersebut dianggap valid. Berikut kode yang saya buat :

Kemudian saya mencoba menjalankan kode tersebut dengan php server dan mencoba mengaksesnya pada browser. Setelah diakses pada browser, muncul kalimat “Email berhasil dikirim” menandakan bahwa kredensial tersebut valid.

Kemudian setelah itu, saya memeriksa inbox pada email saya, untuk mengecek apakah email tersebut benar terkirim atau tidak. Berikut hasilnya :

Setelah mengetahui itu, segera saya membuat laporan untuk dua temuan saya ini dan melaporkannya kepada vendor terkait.

Berkat temuan tersebut, saya diberikan penghargaan berupa uang (saya tidak bisa menyebutkan nominalnya) dan ucapan terimakasih dari manajemen vendor karena sudah membantu mengamankan sistem.

Mungkin cukup sekian tulisan dari saya, semoga tulisan ini bermanfaat bagi pembaca sekalian, mohon maaf apabila ada kekurangan dari kalimat atau kata-kata yang saya sampaikan.

./Logout

Buy me a coffee if you want to :
