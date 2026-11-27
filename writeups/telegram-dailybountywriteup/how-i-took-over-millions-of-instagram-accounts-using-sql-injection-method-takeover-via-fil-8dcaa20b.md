# How I Took Over Millions of Instagram Accounts Using SQL Injection Method & Takeover via Filtering…

- **Source URL:** https://pwn0sec.medium.com/how-i-took-over-millions-of-instagram-accounts-using-sql-injection-method-takeover-via-filtering-cd858d486a54?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20251019231541/https://pwn0sec.medium.com/how-i-took-over-millions-of-instagram-accounts-using-sql-injection-method-takeover-via-filtering-cd858d486a54
- **Fetched:** 2026-11-27
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/8337 (id 8337)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# How I Took Over Millions of Instagram Accounts Using SQL Injection Method & Takeover via Filtering Database Users() Function

Bagaimana Saya Mengambil Alih Jutaan Akun Instagram Menggunakan Metode Injeksi SQL & Pengambilalihan melalui Fungsi Memfilter Pengguna Basis Data ()


Dokumen ini menyajikan materi presentasi yang mendalam mengenai teknik SQL Injection dan bagaimana metode ini dapat digunakan untuk mengambil alih jutaan akun Instagram. Dalam presentasi ini, kita akan membahas pengertian SQL Injection, cara kerjanya, serta langkah-langkah teknis yang diambil untuk mengeksploitasi celah keamanan. Selain itu, kita juga akan menganalisis dampak dari teknik ini terhadap pengguna dan perusahaan, serta memberikan solusi dan langkah mitigasi yang dapat diambil untuk melindungi aplikasi dari eksploitasi serupa.

SQL Injection adalah salah satu teknik serangan yang paling umum digunakan dalam dunia keamanan siber. Memahami teknik ini sangat penting bagi pengembang dan pengguna untuk melindungi data mereka. Kebocoran data yang terjadi melalui metode ini dapat menyebabkan kerugian besar, baik bagi individu maupun perusahaan.

## Apa itu SQL Injection?

SQL Injection adalah teknik serangan yang memungkinkan penyerang untuk menyisipkan perintah SQL ke dalam kueri yang dieksekusi oleh aplikasi. Hal ini dapat mengakibatkan akses tidak sah ke database dan pengambilan data sensitif.

## Bagaimana cara kerjanya dalam konteks aplikasi web

Serangan SQL Injection biasanya terjadi ketika aplikasi web tidak memvalidasi input pengguna dengan benar. Penyerang dapat memanfaatkan celah ini untuk menjalankan perintah SQL yang tidak diinginkan.

## Contoh kasus nyata dari SQL Injection di Instagram

Salah satu contoh nyata adalah ketika penyerang berhasil mengakses data pengguna melalui celah SQL Injection, yang memungkinkan mereka untuk mengambil alih akun tanpa izin.

## Apa itu SQL Injection?

SQL Injection adalah teknik serangan yang memungkinkan penyerang untuk menyisipkan perintah SQL ke dalam kueri yang dieksekusi oleh aplikasi. Hal ini dapat mengakibatkan akses tidak sah ke database dan pengambilan data sensitif.

## Bagaimana cara kerjanya dalam konteks aplikasi web

Serangan SQL Injection biasanya terjadi ketika aplikasi web tidak memvalidasi input pengguna dengan benar. Penyerang dapat memanfaatkan celah ini untuk menjalankan perintah SQL yang tidak diinginkan.

## Contoh kasus nyata dari SQL Injection di Instagram

Salah satu contoh nyata adalah ketika penyerang berhasil mengakses data pengguna melalui celah SQL Injection, yang memungkinkan mereka untuk mengambil alih akun tanpa izin.

## Strategi Pengambilalihan Akun Instagram

Langkah-langkah teknis dalam mengidentifikasi dan mengeksploitasi celah SQL Injection pada Instagram

1. **Identifikasi Input Rentan**: Mencari formulir atau parameter URL yang menerima input pengguna.
2. **Uji Kelayakan**: Menggunakan karakter khusus untuk menguji apakah aplikasi rentan terhadap SQL Injection.
3. **Eksploitasi**: Setelah menemukan celah, penyerang dapat menyisipkan perintah SQL untuk mendapatkan akses ke database.

## Teknik filtrasi database menggunakan users() function untuk mendapatkan akses lebih lanjut

Fungsi `users()` dalam SQL dapat digunakan untuk mendapatkan informasi tentang pengguna yang terdaftar. Dengan memanfaatkan celah SQL Injection, penyerang dapat memanggil fungsi ini untuk mendapatkan data sensitif.

## Apa itu SQL Injection?

SQL Injection adalah teknik serangan yang memungkinkan penyerang untuk menyisipkan perintah SQL ke dalam kueri yang dieksekusi oleh aplikasi. Hal ini dapat mengakibatkan akses tidak sah ke database dan pengambilan data sensitif.

## Bagaimana cara kerjanya dalam konteks aplikasi web

Serangan SQL Injection biasanya terjadi ketika aplikasi web tidak memvalidasi input pengguna dengan benar. Penyerang dapat memanfaatkan celah ini untuk menjalankan perintah SQL yang tidak diinginkan.

## Contoh kasus nyata dari SQL Injection di Instagram

Salah satu contoh nyata adalah ketika penyerang berhasil mengakses data pengguna melalui celah SQL Injection, yang memungkinkan mereka untuk mengambil alih akun tanpa izin.

## Strategi Pengambilalihan Akun Instagram

## Langkah-langkah teknis dalam mengidentifikasi dan mengeksploitasi celah SQL Injection pada Instagram

1. **Identifikasi Input Rentan**: Mencari formulir atau parameter URL yang menerima input pengguna.
2. **Uji Kelayakan**: Menggunakan karakter khusus untuk menguji apakah aplikasi rentan terhadap SQL Injection.
3. **Eksploitasi**: Setelah menemukan celah, penyerang dapat menyisipkan perintah SQL untuk mendapatkan akses ke database.

## Teknik filtrasi database menggunakan users() function untuk mendapatkan akses lebih lanjut

Fungsi `users()` dalam SQL dapat digunakan untuk mendapatkan informasi tentang pengguna yang terdaftar. Dengan memanfaatkan celah SQL Injection, penyerang dapat memanggil fungsi ini untuk mendapatkan data sensitif.

## Mengapa Celah Keamanan Ini Sangat Berbahaya dan Dampak yang Dapat Ditimbulkan?

Celah keamanan, seperti yang ditemukan dalam serangan SQL Injection, merupakan ancaman serius bagi banyak sistem, terutama karena dampaknya yang dapat merusak integritas dan kerahasiaan data sensitif. Sebagai contoh, selama bertahun-tahun saya melakukan riset terhadap berbagai serangan SQL Injection yang menargetkan sistem database seperti MySQL, MongoDB, MariaDB, dan lainnya. Saya menemukan bahwa celah-celah ini sering kali dapat dieksploitasi dengan cara memanipulasi query-query yang dikirimkan ke database. Dengan menghafal dan memahami pola query-query yang digunakan oleh sistem tersebut, saya dapat mengakses informasi sensitif seperti nama pengguna, email, dan kata sandi.

Setelah mendapatkan kredensial ini, saya menyimpannya dalam sebuah database terpisah untuk penelitian lebih lanjut. Tujuan utama saya adalah untuk memahami betapa banyak data yang bocor dari celah-celah ini dan bagaimana data tersebut dapat dimanfaatkan oleh pihak yang tidak bertanggung jawab.

## Automation BOT dalam Penelitian Keamanan:

*Pembuatan Alat untuk Memeriksa Kredensial yang Bocor*

Dalam rangka meningkatkan efisiensi riset saya, saya mengembangkan sebuah alat otomatisasi, seperti *Multiple Instagram Account Checker*. Alat ini berfungsi untuk secara otomatis memeriksa kredensial yang telah saya kumpulkan sebelumnya (termasuk username, email, dan password) yang saya pisahkan dalam file *credentials.txt*. Alat ini kemudian memverifikasi apakah kredensial tersebut digunakan pada platform sosial media seperti Instagram dan lainnya, untuk mengekspos potensi kerentanannya lebih lanjut.

Hasil dari riset ini menunjukkan adanya pola yang mengkhawatirkan di Indonesia, di mana banyak pengguna yang menggunakan kredensial yang sama (username dan password) pada berbagai platform. Banyak dari mereka yang mendaftarkan akun mereka pada situs-situs yang rentan terhadap serangan malware dan menggunakan password yang lemah atau mudah ditebak. Ini menciptakan risiko yang sangat besar, karena ketika satu akun diretas, penyerang dapat mengakses banyak akun lainnya, termasuk akun media sosial dan akun bank.

## Dampak Jangka Panjang dan Pentingnya Keamanan yang Kuat

Dampak dari kebocoran data seperti ini tidak hanya terbatas pada individu yang menjadi korban, tetapi juga dapat merusak reputasi perusahaan yang menyimpan data pelanggan mereka. Jika kredensial yang bocor digunakan untuk mengakses akun bank atau informasi sensitif lainnya, itu dapat menyebabkan kerugian finansial yang signifikan. Oleh karena itu, sangat penting bagi individu dan perusahaan untuk menggunakan kata sandi yang kuat dan unik untuk setiap akun serta menjaga sistem mereka agar tetap terlindungi dari celah-celah keamanan seperti SQL Injection. Upaya pencegahan sejak dini sangat penting untuk menghindari serangan yang dapat merusak integritas sistem secara keseluruhan.

### **Kesimpulan**

Berdasarkan penelitian yang telah saya lakukan selama lebih dari 8 tahun, saya menemukan bahwa banyak pengguna di Indonesia yang masih menggunakan password yang sama saat melakukan registrasi di berbagai platform digital maupun website pemerintah. Kondisi ini menunjukkan adanya mindset yang rendah terhadap pentingnya keamanan data pribadi. Hal ini membuka celah bagi para penyerang untuk dengan mudah mengakses dan mengambil alih akun serta informasi yang dimiliki oleh individu, termasuk data pribadi yang sangat sensitif.

Fenomena ini tidak hanya terjadi di kalangan masyarakat umum, tetapi juga di kalangan pemerintahan Indonesia. Dalam riset saya terkait kerentanannya pada website dan sistem digitalisasi pemerintah, saya mencoba mencocokkan berbagai kredensial yang ada di dalam database mereka, dan hasilnya cukup mengejutkan. Saya berhasil memperoleh akses ke akun-akun pribadi dan kredensial masyarakat yang belum sadar akan risiko kebocoran data. Meskipun saya telah berupaya berkoordinasi dengan pihak berwenang, ternyata banyak pejabat yang tidak memiliki pemahaman yang cukup tentang teknologi. Dari beberapa pertemuan dengan pejabat di divisi teknologi, hampir 50% dari mereka tidak mengetahui hal mendasar tentang teknologi yang mereka kelola. Seperti anak kecil yang tidak paham dengan apa yang mereka lakukan.

Yang lebih mengejutkan lagi, beberapa pejabat bahkan meremehkan kebocoran data yang terjadi, dengan mengatakan bahwa ***“data masyarakat yang bocor, bukan data kami.”*** Hal ini menunjukkan kurangnya kepedulian dan keseriusan dalam menangani masalah kebocoran data yang dapat merugikan banyak pihak. Salah satu contoh nyata adalah kebocoran data CPNS yang terjadi pada tahun lalu, yang merupakan bukti nyata bahwa sistem yang mereka bangun rentan terhadap serangan. Keadaan ini semakin diperparah dengan adanya banyak server pemerintah yang juga terpapar kerentanannya.

Secara keseluruhan, temuan ini menjadi pengingat penting bahwa kesadaran dan pemahaman akan teknologi dan keamanan siber sangat dibutuhkan, baik di kalangan masyarakat maupun di pemerintah, agar kebocoran data dan serangan siber dapat dicegah dengan lebih efektif.

## **Sumber & Referensi:**

Untuk lebih lanjut mengenai penelitian saya dan berbagai informasi terkait keamanan siber, Anda dapat mengunjungi:

**Apa itu Pwn0sec Research?**

Pwn0sec Research adalah platform yang didedikasikan untuk penelitian dan pengembangan dalam bidang keamanan siber. Di sini, kami menyediakan berbagai riset, alat, dan informasi terkait ancaman siber, serta solusi untuk meningkatkan keamanan digital di berbagai sektor, termasuk pemerintahan, industri, dan masyarakat umum. Kami berfokus pada pemecahan masalah kerentanannya dan memberikan pemahaman yang lebih baik tentang potensi risiko yang ada di dunia maya.

**Ikuti Kami di Media Sosial:**

[@cscpwn0sec](https://instagram.com/cscpwn0sec) — Untuk diskusi seputar teknologi dan riset komunitas.

[@pwn0sec](https://instagram.com/pwn0sec) — Untuk mengikuti grup dan perkembangan Pwn0sec.
