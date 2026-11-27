# Web App Hacking Tips & Trick — Celah File Upload — Bagian 3

- **Source URL:** https://medium.com/@mrp.bpp/web-app-hacking-tips-trick-celah-file-upload-bagian-3-8ec192d1633b?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250503115856/https://medium.com/@mrp.bpp/web-app-hacking-tips-trick-celah-file-upload-bagian-3-8ec192d1633b
- **Fetched:** 2026-11-27
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/7391 (id 7391)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Web App Hacking Tips & Trick — Celah File Upload — Bagian 3

## XXE (XML External Entity)

**Penjelasan**: XXE (XML External Entity) adalah serangan di mana penyerang memanipulasi parser XML untuk memproses entitas eksternal yang berbahaya. Ini bisa digunakan untuk membaca file dari server atau menjalankan serangan DoS.

**Contoh**:

- **Upload menggunakan file SVG**: Penyerang bisa menyisipkan entitas eksternal dalam file SVG seperti ini:

**Dampak**: Penyerang bisa menggunakan XXE untuk membaca file sensitif dari server, mengakses informasi yang tidak seharusnya tersedia, atau menyebabkan kerusakan pada sistem dengan serangan DoS.

## XSS (Cross-Site Scripting)

- **Penjelasan**: XSS adalah serangan di mana penyerang menyisipkan skrip berbahaya ke dalam halaman web yang kemudian dijalankan di browser pengguna lain. Ini bisa terjadi ketika file yang diunggah tidak divalidasi dengan benar, seperti SVG atau GIF yang berisi kode JavaScript berbahaya.

**Contoh**:

- **Mengunggah file GIF dengan XSS**:

`GIF89a/*<svg/onload=alert(1)>*/=alert(document.domain)//;`
- **Mengunggah file SVG dengan XSS**:

`<svg xmlns="http://www.w3.org/2000/svg" onload="alert(1)"/>`
**Dampak**: XSS memungkinkan penyerang mencuri data sensitif dari pengguna, seperti cookie sesi, atau memanipulasi halaman web untuk kepentingan jahat.

## Open Redirect

**Penjelasan**: Open Redirect adalah serangan di mana penyerang menggunakan fitur pengalihan di dalam aplikasi web untuk mengarahkan pengguna ke situs berbahaya tanpa mereka sadari. Jika file yang diunggah dapat menjalankan skrip pengalihan, maka pengguna yang mengakses file tersebut bisa diarahkan ke situs yang dikendalikan oleh penyerang.

**Contoh**:

- **Mengunggah file SVG dengan Open Redirect**:

`<?xml version="1.0" encoding="UTF-8" standalone="yes"?> <svg onload="window.location='https://attacker.com'" xmlns="http://www.w3.org/2000/svg">     <rect width="300" height="100" style="fill:rgb(0,0,255);stroke-width:3;stroke:rgb(0,0,0)" /> </svg>`
**Dampak**: Serangan ini bisa digunakan untuk mencuri kredensial atau informasi sensitif dengan mengarahkan korban ke situs phishing.

# Bypass Validasi Konten

**Penjelasan**: Beberapa aplikasi memeriksa **Content-Type** dan **Content-Length** file yang diunggah untuk mencegah file berbahaya diunggah. Namun, penyerang bisa mencoba memanipulasi header ini untuk mem-bypass validasi dan mengunggah file berbahaya.

**Contoh**:

- **Content-Type**: Mengubah Content-Type menjadi tipe gambar yang diizinkan (misalnya `image/png`), padahal file sebenarnya adalah skrip PHP berbahaya.
- **Content-Length**: Jika server membatasi ukuran file yang diunggah, penyerang bisa memanipulasi header Content-Length untuk mengunggah file yang lebih besar dari batas yang diizinkan, atau file dengan shell kecil seperti:

``<?=`$_GET[x]`?>``
**Dampak**: Penyerang bisa memanipulasi pemeriksaan konten dan mengunggah skrip berbahaya yang mengeksekusi perintah atau mencuri informasi dari server.

# Bypass Validasi Konten melalui Manipulasi Header

## Validasi Content-Type

**Penjelasan**: Banyak server memeriksa header `Content-Type` untuk menentukan jenis file yang diunggah, misalnya `image/png` untuk gambar atau `application/pdf` untuk dokumen. Jika tidak ada pemeriksaan yang benar atau mekanisme validasi yang ketat, penyerang bisa memanipulasi header ini untuk mengelabui server agar mempercayai bahwa file berbahaya adalah file aman.

**Contoh**:

- **Upload file.php**: Penyerang bisa mengubah header `Content-Type` dari file PHP berbahaya menjadi tipe yang diizinkan, seperti `image/png` atau `image/jpeg`, meskipun file tersebut sebenarnya adalah skrip PHP yang berbahaya. Server mungkin tidak memeriksa isi file dengan baik dan langsung mengizinkan pengunggahan file tersebut, sehingga penyerang bisa menjalankan kode berbahaya pada server setelah file diakses.

**Dampak**: Jika manipulasi `Content-Type` berhasil, penyerang bisa menyisipkan skrip berbahaya di server. Misalnya, file PHP yang diunggah bisa dijalankan di server, memungkinkan **Remote Code Execution (RCE)** dan memberi penyerang akses penuh ke server.

## Validasi Content-Length

**Penjelasan**: `Content-Length` adalah header yang menunjukkan ukuran file yang diunggah. Banyak server membatasi ukuran file yang bisa diunggah untuk mencegah serangan **Denial of Service (DoS)** dengan cara mengunggah file berukuran besar. Namun, penyerang bisa memanipulasi nilai ini atau memanfaatkan celah di mekanisme validasi untuk mengunggah file yang lebih besar dari yang diizinkan.

**Contoh**:

- **Small PHP Shell**: Penyerang bisa mencoba mengunggah shell kecil dengan konten seperti:

``<?=`$_GET[x]`?>``
- Ukuran file ini mungkin sangat kecil dan bisa melewati batasan `Content-Length`, tetapi tetap memberikan akses ke eksekusi perintah di server. Penyerang bisa memanfaatkan skrip ini untuk menjalankan perintah shell di server dengan cara mengirimkan permintaan HTTP yang memanggil file ini dengan parameter yang sesuai.

**Dampak**: Meskipun ukuran file kecil, shell tersebut memungkinkan penyerang mengeksekusi perintah berbahaya pada server, yang bisa digunakan untuk mengambil alih kendali penuh server atau mencuri data sensitif.

## Bypass Konten melalui Manipulasi Isi File

- **Penjelasan**: Beberapa aplikasi web mungkin memeriksa isi file yang diunggah untuk menentukan apakah file tersebut aman, misalnya dengan memeriksa tanda tangan file atau header file (seperti tanda `GIF89a;` pada gambar GIF). Penyerang bisa mencoba mengelabui pemeriksaan ini dengan menambahkan tanda tangan file yang sah di depan file berbahaya.

**Contoh**:

- **Content Bypass Shell**: Penyerang bisa menambahkan teks seperti `GIF89a;` di depan kode PHP berbahaya untuk menyamar sebagai file gambar GIF. Contoh file:

`GIF89a; <?php system($_GET['cmd']); ?>`
- Server mungkin menganggap file ini sebagai gambar GIF karena memulai dengan tanda `GIF89a;`, padahal sebenarnya file tersebut berisi skrip PHP berbahaya.

**Dampak**: Jika manipulasi berhasil, file ini bisa digunakan untuk mengeksekusi perintah pada server, memberikan penyerang kendali atas server dan memungkinkannya mencuri data atau merusak sistem.

# Teknik Miscellaneous (Lain-lain) dalam Serangan Upload File

## Mengunggah File .js dan file .config (web.config)

**Penjelasan**: File JavaScript (`.js`) atau file konfigurasi web server (`web.config`) dapat diunggah oleh penyerang untuk menyisipkan atau mengubah pengaturan aplikasi web. File `.config` digunakan di server berbasis Microsoft IIS, sedangkan file `.js` digunakan untuk menjalankan kode JavaScript di browser klien.

**Contoh**:

- **file.js**: Penyerang dapat menyisipkan kode JavaScript berbahaya yang akan dieksekusi pada browser pengguna ketika file diakses. Contoh kode XSS yang disisipkan di dalam file `.js`:

`<script>alert(document.cookie)</script>`
- **web.config**: Penyerang bisa mengubah pengaturan server IIS dengan file `web.config` yang dimodifikasi, yang dapat mengarahkan ulang URL, mengubah aturan otentikasi, atau memungkinkan file skrip dieksekusi.

**Dampak**: File JavaScript berbahaya dapat digunakan untuk serangan **XSS**, mencuri data sensitif seperti cookie sesi. Sementara itu, file konfigurasi yang berbahaya dapat mengubah pengaturan server dan mengarahkan pengguna ke halaman jahat, atau bahkan memungkinkan penyerang menjalankan kode pada server.

## Serangan DoS dengan “Pixel Flood” Menggunakan Gambar

**Penjelasan**: **Pixel Flood Attack** adalah bentuk serangan **Denial of Service (DoS)** di mana penyerang mengunggah gambar dengan ukuran resolusi yang sangat besar tetapi ukuran file yang relatif kecil. Saat server mencoba memproses gambar, penggunaan sumber daya (CPU dan RAM) meningkat secara drastis, menyebabkan server menjadi lambat atau tidak responsif.

**Contoh**:

- Penyerang bisa mengunggah gambar dengan nama seperti `1234...99.png` yang memiliki resolusi besar (misalnya, 100.000 x 100.000 piksel) tetapi ukuran file kecil. Ketika server mencoba memproses gambar ini, server bisa kelebihan beban dan crash, sehingga menyebabkan **Denial of Service (DoS)**.

**Dampak**: Serangan ini bisa menyebabkan server menjadi lambat atau tidak responsif, sehingga situs web atau aplikasi menjadi tidak bisa diakses oleh pengguna lain.

## Zip Slip

**Penjelasan**: **Zip Slip** adalah serangan di mana penyerang mengunggah file terkompresi (.zip) yang berisi file berbahaya (misalnya, skrip PHP). Ketika file ZIP diekstrak oleh server, file berbahaya ditempatkan di lokasi yang tidak diinginkan dan dapat dieksekusi, memberikan penyerang akses ke server.

**Contoh**:

- Penyerang mengunggah file ZIP yang berisi file PHP berbahaya (`rce.php`) di dalamnya. Ketika file ZIP diekstrak di server, file PHP bisa ditempatkan di direktori yang diakses publik, misalnya: `site.com/path?page=zip://path/file.zip%23rce.php`. Penyerang kemudian dapat mengakses file ini dan mengeksekusi kode berbahaya pada server.

**Dampak**: Zip Slip memungkinkan penyerang menyisipkan file berbahaya ke dalam server dan mengeksekusi skrip jarak jauh (RCE), yang bisa mengakibatkan pengambilalihan penuh server.
