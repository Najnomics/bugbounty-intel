# Cara Efektif Hacker Professional Menangani Sort-lived Token/Session menggunakan Burp Suite

- **Source URL:** https://medium.com/@muhammadyusuf.muhayuf/cara-efektif-hacker-professional-menangani-sort-lived-token-session-menggunakan-burp-suite-e425b557b455
- **Fetched from:** https://medium.com/@muhammadyusuf.muhayuf/cara-efektif-hacker-professional-menangani-sort-lived-token-session-menggunakan-burp-suite-e425b557b455?source=rss-9b237cef8991------2
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14903 (id 14903)
- **Method:** medium-rss-feed (full content:encoded) readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- **Author/Published (RSS):** Muhayuf / Wed, 09 Sep 2026 03:34:58 GMT

Pernah nggak sih kalian ketemu web yang token/session-nya ganti tiap beberapa detik atau menit?! Dan kalian masih mengirimkan request secara manual untuk mendapatkan token/session terbaru?! Pada artikel kali ini, saya akan memberi tahu kalian ekstensi Burp Suite bernama **Collector** yg dibuat oleh salah satu youtuber hacking bernama [Tib3rius](https://medium.com/u/16a5c5e916e4). di artikel ini akan saya beritahu mulai dari proses intalasi sampai cara menggunakannya.

Saat melakukan *penetration testing* atau *bug bounty*, salah satu hal membuat kita frustrasi adalah ketika berhadapan dengan aplikasi web modern yang mengimplementasikan *short-lived tokens*, Anti-CSRF token, atau UUID yang diperbarui setiap beberapa detik.

Menyalin token secara manual ke Burp Repeater atau Intruder setiap kali sesi kedaluwarsa bukan cuma membuang waktu, tapi juga merusak flow analisis kita. Di sinilah sebuah ekstensi keren bernama **Collector** hadir sebagai penyelamat.

Ekstensi ini tidak tersedia di **BApp Store.** Oleh karena itu, kita perlu mengunduh extension tersebut dari repository GitHub [berikut](https://github.com/Tib3rius/Collector/releases), lalu download file Collector dengan ekstensi .jar.

**Catatan:** Gunakan versi terbaru yang tersedia dan pastikan versi extension kompatibel dengan versi Burp Suite serta Java yang digunakan.

Selanjutnya buka Burp Suite, pada tab *extensions* klik button add. setelah itu pilih extension type *java* dan pilih file *Collector.jar* yg sebelumnya didownload lalu klik next.

Jika berhasil, akan muncul message sebagai berikut.

menu yang berfungsi untuk melakukan pengaturan bucket/tempat penyimpanan token

- radio button Enabled: mengaktifkan/non-aktifkan bucket

- Bucket Type: pengauran untuk cara penyimpanan dan pengambilan token dalam bucket

- Max Size: jumlah maximum token yang disimpan dalam bucket (-1 berarti unlimited)

- When Bucket is Full: pengaturan untuk menangani jika token dalam bucket penuh (menyesuaikan pengaturan Max Size)

- radio button Unique Tokens: pengaturan untuk memperbolehkan/tidak menyimpan duplicate token

menu yang berfungsi untuk mengatur token yang akan disimpan

- Collection Sources & Collection Tools: mengaktifkan menu mana saja yang akan digunakan untuk mendapat token

- Collection URLs: endpoint yang digunakan untuk mengambil token

- Collection Patterns: pengaturan pattern header/body pada request/response yang memiliki token untuk diambil/disimpan pada bucket

-Post-Collection JavaScript: untuk menghandle token yang membutuhkan decode/encode agar bisa digunakan

menu yang berfungsi untuk memonitor dan mengatur token yang digunakan/disimpan.

menu yang berfungsi untuk mengatur token yang akan ditempel

- Replacement Sinks & Replacement Tools: mengaktifkan menu mana saja yang akan digunakan untuk menempel token

- Replacement URLs: endpoint yang digunakan untuk menempel token

-Pre-Replacement JavaScript: untuk menghandle token yang membutuhkan decode/encode agar bisa digunakan

- Replacement Rules: pengaturan pattern header/body pada request yang membutuhkan token untuk digunakan

Saya mempunyai sebuah website yang menyimpan session user menggunakan token pada header:

X-Acc-Op: TOKEN

Masalahnya, token tersebut selalu diperbarui setiap **30 detik**. Akibatnya, jika menggunakan token yang sudah expired atau token yang tidak sesuai, server akan memberikan response error:

Hal ini tentunya cukup merepotkan jika kita ingin melakukan testing menggunakan Burp Repeater atau Intruder, karena kita harus terus-menerus mendapatkan token terbaru dan menggantinya secara manual.

Nah, sekarang kita akan menggunakan Collector untuk mengotomatisasi proses tersebut.

Bagian ini membutuhkan sedikit kemampuan teknis dan pemahaman terhadap behavior aplikasi yang sedang kita test. Hal pertama yang perlu kita lakukan adalah mencari tahu **endpoint mana yang digunakan aplikasi untuk mendapatkan atau me-refresh token**.

Biasanya, saya menggunakan fitur **Filter Search** pada HTTP History Burp Suite dengan kata kunci yang umum seperti:

token

authentication

bearer

refresh

session

access

authorize

Keyword tersebut tentunya dapat disesuaikan dengan aplikasi yang sedang kita test.

Setelah melakukan filtering pada HTTP History, kita dapat melihat request yang berhubungan dengan proses authentication atau token refresh. Pada case ini, saya menemukan **dua endpoint** yang digunakan aplikasi untuk melakukan generate token.

Setelah mengetahui endpoint tersebut, kita dapat menggunakannya sebagai sumber token untuk Collector.

Selanjutnya kita pergi ke menu extension dan add bucket baru. Pada **Bucket Configuration**, saya menggunakan konfigurasi seperti pada gambar berikut.

Ada beberapa konfigurasi yang perlu diperhatikan:

Setelah bucket selesai dibuat, langkah berikutnya adalah mengatur bagaimana Collector mengambil token dari aplikasi. Masuk ke menu token collection, Kemudian lakukan konfigurasi sesuai kebutuhan (penjelasannya terlampir dibawah). berikut contoh konfigurasi saya:

Ada beberapa konfigurasi penting yang saya gunakan.

Pada **Collection Pattern**, kita perlu menentukan bagian mana dari HTTP response yang ingin diambil. Kita dapat menentukan parameter pada body atau header yang ingin diambil, kemudian menggunakan regex untuk mengambil value dari parameter tersebut.

Sebagai contoh, jika response memiliki:

```
{
    "token": "eyJhbGciOiJIUzI1NiIs..."
}
```
kita dapat membuat pattern yang mencari parameter token dan menggunakan regex untuk mengambil value-nya. Jika kita ingin mengambil seluruh value dari parameter tersebut, kita dapat menggunakan regex seperti yang ditunjukkan pada gambar.

**Penjelasan regex:**

\[^"\]+

Jadi, \[^"\]+ dapat diartikan sebagai:

***“Ambil satu atau lebih karakter apa pun selama karakter tersebut bukan double quote (******").”***

Kita dapat menguji pattern tersebut pada Regex Tester untuk memastikan bahwa hasil match hanya berisi token yang kita inginkan saat memasukkan pattern.

Setelah Token Collection selesai dikonfigurasi, kita dapat melihat apakah Collector benar-benar berhasil mengambil token.

Di menu ini kita dapat melihat token yang berhasil dikumpulkan oleh Collector.

Sekarang kita sudah berhasil mendapatkan token. Langkah terakhir yang kita perlu lakukan adalah membuat Collector menggunakan token tersebut pada request yang kita kirim.

Konfigurasi yang saya gunakan dapat dilihat pada screenshot berikut.

Untuk memastikan bahwa replacement benar-benar terjadi, kita dapat menggunakan **Logger** pada Burp Suite. Pertama-tama perhatikan request *repeater* berikut

Jika kita buka *Logger*, kita dapat melihat request yang benar-benar diproses dan dikirim. nilai headernya sudah berbeda dengan token yang terlihat pada Repeater.

Ini menunjukkan bahwa Collector telah berhasil mengambil token terbaru dari bucket dan menggantinya pada request sebelum dikirim.

Short-lived token sebenarnya merupakan mekanisme yang cukup umum digunakan oleh aplikasi modern. Dari sisi security, token dengan lifetime pendek dapat membantu mengurangi dampak ketika token berhasil diperoleh oleh pihak yang tidak berwenang.

Namun, dari sisi penetration tester, mekanisme ini terkadang dapat menjadi cukup merepotkan, terutama ketika kita perlu melakukan testing secara berulang.

Menurut saya, salah satu hal paling menarik dari Collector bukan hanya kemampuannya untuk mengganti token secara otomatis, tetapi bagaimana extension ini dapat membantu kita membuat workflow penetration testing menjadi lebih efisien. Secara keseluruhan, workflow yang kita lakukan adalah:

1\. Identify Token Refresh Endpoint

↓

2. Create Bucket

↓

3. Configure Token Collection

↓

4. Extract Token Using Regex

↓

5. Store Token in Bucket

↓

6. Configure Token Replacement

↓

7. Verify Actual Request

Jadi, ketika kalian menemukan aplikasi dengan token yang berubah setiap beberapa detik, jangan sampai workflow testing kalian berubah *copas dan repeat.* Manfaatkan automation sebisa mungkin, sehingga kita bisa menghabiskan lebih banyak waktu untuk mencari vulnerability daripada mengurus token.

**Happy Hunting! 🔐**
