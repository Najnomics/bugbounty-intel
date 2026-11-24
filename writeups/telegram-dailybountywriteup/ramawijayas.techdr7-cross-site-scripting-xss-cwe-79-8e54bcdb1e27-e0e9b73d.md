# Cross-Site Scripting — XSS [CWE-79]

- **Source URL:** https://medium.com/@ramawijayas.techdr7/cross-site-scripting-xss-cwe-79-8e54bcdb1e27?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20230127063430/https://medium.com/@ramawijayas.techdr7/cross-site-scripting-xss-cwe-79-8e54bcdb1e27
- **Fetched:** 2026-11-24
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/1297 (id 1297)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Cross-Site Scripting — XSS \[CWE-79\]

## **Improper Neutralization of Input During Web Page Generation (‘Cross-site Scripting’)**

**Table of Content 1. Deskripsi 2. Potensi dampak 3. Pola serangan 4. Perangkat lunak yang terpengaruh 5. Contoh Eksploitasi 6. Cara mencegah XSS 7. Penilaian Keparahan dan CVSS**


1. Deskripsi

XSS (Cross Site Scripting) adalah eksploitasi keamanan di mana penyerang menempatkan *malicious client-end code* ke laman web. Serangan ini sudah cukup sering terjadi dalam beberapa tahun terakhir dan kebanyakan serangan ini menyerang *website-website* besar.

Tujuan utama dari penggunaan XSS yakni untuk mengambil data penting, mengambil *cookie* dari *user* atau mengirimkan suatu program yang dapat merusak *user*, namun seakan-akan penyebabnya adalah dari web itu sendiri.

**CARA KERJA XSS**

2\. Potensi Dampak XSS:

Dampak sebenarnya dari serangan XSS umumnya bergantung pada sifat aplikasi, fungsionalitas dan datanya, serta status pengguna yang disusupi. Daftar jalan serangan potensial yang tidak lengkap tercantum di bawah ini. Setelah serangan berhasil, pengguna jahat dapat melakukan berbagai tindakan: mencuri cookie pengguna, memodifikasi konten halaman web, dan melakukan operasi dengan situs dalam sesi pengguna (proksi XSS).

❏ Pencurian Cookie;

❏ Perusakan halaman web;

❏ Hamparan iFrame untuk memfasilitasi phishing, pencurian kredensial;

❏ iFrame tersembunyi untuk memuat JavaScript berbahaya, untuk mencoba mengeksploitasi mesin korban;

❏ Pengalihan ke situs web lain, untuk memfasilitasi pengiriman malware;

❏ Injeksi JavaScript berbahaya, mengubah situs yang disusupi menjadi situs unduhan drive-by.


3\. Pola Serangan:

Pola serangan berikut dapat memanfaatkan kerentanan skrip lintas situs, menurut klasifikasi CAPEC (Common Attack Pattern Enumeration and Classification):

CAPEC-18: Menyematkan Skrip di Elemen Non-skrip

CAPEC-19: Menyematkan Script di dalam Script

CAPEC-32: Menyematkan Script dalam HTTP Query Strings

CAPEC-63: Injeksi Skrip Sederhana

CAPEC-85: Jejak Jaringan Klien (menggunakan AJAX/XSS)

CAPEC-86: Skrip Penyematan (XSS ) di Header HTTP

CAPEC-91: XSS dalam Tag IMG

CAPEC-106: Pembuatan Skrip Lintas Situs melalui File Log

CAPEC-198: Pembuatan Skrip Lintas Situs di Halaman Kesalahan

CAPEC-199: Pembuatan Skrip Lintas Situs Menggunakan Sintaks Alternatif

CAPEC-209: Pembuatan Skrip Lintas Situs Menggunakan Ketidakcocokan Jenis MIME

CAPEC-232: Eksploitasi Keistimewaan/Kepercayaan

CAPEC-243: Pembuatan Skrip Lintas Situs dalam Atribut

CAPEC-244: Pembuatan Skrip Lintas Situs melalui Skema URI yang Dikodekan

CAPEC-245: Pembuatan Skrip Lintas Situs Menggunakan Karakter Ganda, mis. %3C%3Cskrip

CAPEC-246: Pembuatan Skrip Lintas Situs Menggunakan Flash

CAPEC-247: Cross-Site Scripting dengan Masking melalui Karakter Tidak Valid dalam Pengidentifikasi


Klasifikasi Ancaman WASC Alternatif menjelaskan Cross-site Scripting sebagai serangan di bawah WASC-8.

4\. Perangkat lunak yang terpengaruh:

Perangkat lunak yang menggunakan HTML untuk menampilkan data berpotensi rentan terhadap kelemahan ini: aplikasi web, browser, kontrol ActiveX, plugin browser, klien email dan RSS, frontend untuk solusi perangkat keras, dll.

5\. Contoh Eksploitasi

Menggunakan kerentanan di ForkCMS — HTB23075 security advisory (CVE-2012–1188) sebagai contoh kelemahan ini dan menunjukkan dua serangan berbeda terhadap aplikasi yang rentan.

**Pencurian Cookie** 

Pengguna jahat dapat mencuri cookie dan menggunakannya untuk mendapatkan akses ke aplikasi. Eksploitasi yang berhasil mengharuskan pengguna, yang masuk ke aplikasi, mengikuti tautan yang dibuat khusus ke situs web yang rentan

halaman yang dihasilkan terlihat sebagai berikut:

Ini berarti skrip fork.js yang terletak di attackersite.com akan dimuat dan dijalankan. Skrip fork.js berisi kode berikut:

Kode di atas mengirimkan permintaan HTTP POST ke file [http://attackersite.com/fork.php](http://attackersite.com/fork.php) yang mencatat semua data dan mengalihkan korban kembali ke situs web asli. Skrip fork.php berisi kode berikut:

Penyerang dapat menggunakan data yang diterima untuk membuat cookie dan mendapatkan akses ke aplikasi. Ini dapat dicapai dengan plugin editor cookie apa pun:

Kami menggunakan plugin Editor Cookie untuk Firefox untuk membuat cookie yang diperlukan. Setelah itu, kita tinggal mengunjungi website yang rentan:

**Phising**

Contoh eksploitasi lain dari kerentanan ini menggunakan beberapa teknik rekayasa sosial untuk mencuri kata sandi administrator.

Ini adalah window login biasa:

PoC berikut mengubah konten halaman ini:

Penyerang juga dapat mengubah beberapa elemen halaman dan mencuri kredensial pengguna setelah mengelabui korban agar mengikuti tautan yang dibuat khusus:

Pengguna jahat dapat membuat laman web yang terlihat identik dengan yang sah dan mencegat informasi yang berpotensi sensitif:

Seperti yang bisa kita lihat, tag “iframe” dimuat dari domain eksternal attacker-site.com. Halaman terlihat sama seperti biasanya kecuali tombol kirim, yang mengirimkan data ke domain jahat, dan URL yang sangat panjang. Bilah status dengan situs web berbahaya sengaja dibiarkan; itu dapat dengan mudah diubah menjadi nilai arbitrer.

XSS berbasis DOM dengan JSON dan Ajax Vektor eksploitasi lain untuk kerentanan skrip lintas situs adalah injeksi JSON/Ajax. Aplikasi web modern banyak menggunakan teknologi Ajax untuk menampilkan dan memperbarui data penting tanpa memuat ulang halaman. Dalam contoh ini, kami akan mendemonstrasikan XSS berbasis DOM melawan aplikasi web palsu dan menunjukkan betapa mudahnya mengeksploitasi kerentanan ini.

Misalkan kita memiliki aplikasi obrolan langsung yang menampilkan status setiap kontak di daftar pengguna. Pengguna dapat menggunakan pesan khusus untuk menampilkan status mereka. Daftar pengguna dan statusnya dibangun oleh skrip sisi server dan diteruskan ke setiap anggota obrolan melalui objek JSON.

Objek JSON:

{“OnlineUsers”: “4”, “UserAndStatus”: \[“User1, Online”, “User2, Online”, “User3, Online”, “User4, Busy”\]}


Kode JavaScript:

var http\_request = new XMLHttpRequest();

var Contacts;

http\_request.open(“GET”, url, true);

http\_request.onreadystatechange = function ()

{

if (http\_request.readyState == 4)

{

if (http\_request.status == 200) {

Contacts = eval(“(“ + http\_request.responseText + “)”);

}

http\_request = null;

}

};

http\_request.send(null);


Fungsi JavaScript eval() sangat penting untuk data JSON. Dalam hal validasi input yang tidak tepat, sangat mudah untuk dieksploitasi. Misalnya, dengan status pengguna khusus, dimungkinkan untuk menyuntikkan string berikut ke dalam objek JSON:

Busy”});alert(“DOM based XSS”);//

dan jalankan fungsi alert() di browser setiap anggota obrolan.

6\. Cara mencegah serangan XSS:

Mencegah pembuatan XSS adalah hal yang sepele dalam beberapa kasus, tetapi bisa jauh lebih sulit bergantung pada kerumitan aplikasi dan caranya menangani data yang dapat dikontrol pengguna. Secara umum, mencegah kerentanan XSS secara efektif kemungkinan melibatkan kombinasi dari langkah-langkah berikut:

- Filter input pada saat kedatangan. Pada titik di mana input pengguna diterima, filter seketat mungkin berdasarkan input yang diharapkan atau valid.
- Mengkodekan data pada output. Pada titik di mana data yang dapat dikontrol pengguna dikeluarkan dalam respons HTTP, enkode keluaran untuk mencegahnya ditafsirkan sebagai konten aktif. Bergantung pada konteks keluaran, ini mungkin memerlukan penerapan kombinasi penyandian HTML, URL, JavaScript, dan CSS.
- Gunakan tajuk respons yang sesuai. Untuk mencegah XSS dalam respons HTTP yang tidak dimaksudkan untuk berisi HTML atau JavaScript apa pun, Anda dapat menggunakan header Content-Type dan X-Content-Type-Options untuk memastikan bahwa browser menginterpretasikan respons sesuai keinginan Anda.
- Kebijakan Keamanan Konten. Sebagai garis pertahanan terakhir, Anda dapat menggunakan Content Security Policy (CSP) untuk mengurangi keparahan kerentanan XSS yang masih terjadi.

7\. Keparahan dan Penilaian CVSS

Pembuatan skrip lintas situs memengaruhi integritas dan kerahasiaan data dan memerlukan beberapa interaksi pengguna (pengguna harus mengunjungi halaman yang dibuat khusus atau mengikuti tautan berbahaya). Itu harus dinilai sebagai berikut:

6.1 \[CVSS:3.0/AV:N/.AC:L/.PR:N/.UI:R/.S:C/.C:L/.I:L/.A:N\] — Keparahan sedang.

Jika interaksi pengguna tidak diperlukan (mis., dalam kasus XSS yang disimpan di halaman yang dapat diakses publik), kami menyarankan untuk menilai kelemahan ini sebagai UI:N:

7.2 \[CVSS:3.0/AV:N/.AC:L/.PR:N/.UI:N/.S:C/.C:L/.I:L/.A:N\] — Keparahan tinggi.

Terimakasih!

Be ethic, be smart and enjoy your hacks!!

Referensi:
