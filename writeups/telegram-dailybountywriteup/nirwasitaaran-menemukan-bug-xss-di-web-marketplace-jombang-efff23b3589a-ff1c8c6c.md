# Menemukan Bug XSS di Web Marketplace Jombang

- **Source URL:** https://medium.com/@nirwasitaaran/menemukan-bug-xss-di-web-marketplace-jombang-efff23b3589a
- **Fetched from:** https://medium.com/@nirwasitaaran/menemukan-bug-xss-di-web-marketplace-jombang-efff23b3589a?source=rss-feb6eed950a3------2
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:**  (id 14937)
- **Method:** medium-rss-feed (full content:encoded) readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- **Author/Published (RSS):** Aruna Rasendriya Nirwasita / Wed, 07 Oct 2026 03:37:48 GMT

**Perkenalan**Halo semuanya!

Pada kesempatan ini saya ingin berbagi salah satu temuan saya, yaitu celah **Reflected Cross-Site Scripting (XSS)** pada **Jomart Marketplace** platform e-commerce resmi milik Pemerintah Kabupaten Jombang (marketplace.jombangkab.go.id).

***Disclaimer:*** *Write-up ini dipublikasikan* ***murni setelah celah dilaporkan, diverifikasi, dan ditangani*** *oleh pihak pengelola. Tujuannya semata untuk edukasi dan berbagi pengalaman, bukan untuk merugikan pihak mana pun. Seluruh pengujian dilakukan secara terbatas hanya untuk membuktikan keberadaan celah, tanpa mengakses atau mengubah data apa pun.*

Singkatnya, Reflected XSS terjadi ketika input dari pengguna dipantulkan kembali ke halaman tanpa validasi dan *output encoding* yang benar, sehingga penyerang bisa menyusun sebuah tautan yang mengeksekusi JavaScript di peramban korban saat dibuka.

**Kronologi & Penemuan Kerentanan**Target pertama yang saya perhatikan adalah

Saya mulai dari yang paling sederhana: memasukkan beberapa karakter spesial untuk melihat bagaimana aplikasi memperlakukannya.

test"\<>

Aplikasi memantulkan input apa adanya ke halaman hasil, tanpa sanitasi:

Menampilkan 0 produk untuk "test"\<>"

Karakter ", \<, dan > kembali utuh tanpa di-*encode*. Ini indikasi kuat bahwa karakter markup tidak dinetralkan pada keluaran — artinya parameter pencarian berpotensi bisa disisipi kode.

Dari situ saya lanjutkan dengan *payload* XSS:

`<IMG """><SCRIPT>alert("XSS By ./ARN")</SCRIPT>">`
Setelah *payload* dikirim melalui parameter pencarian dan halaman dimuat ulang, peramban mengeksekusi skrip yang disisipkan dan menampilkan dialog:

XSS By ./ARN

Dialog yang muncul ini mengonfirmasi bahwa parameter pencarian dapat digunakan untuk menjalankan JavaScript sewenang-wenang di peramban pengguna **Reflected XSS yang terverifikasi.**

**Impact (Dampak Risiko)**Secara tingkatan celah ini berada pada tingkat

Tingkat keparahan sesungguhnya bergantung pada konteks aplikasi dan kontrol keamanan lain yang diterapkan.

**Mitigation / Rekomendasi Perbaikan**

**Penutup & Solusi**Temuan ini sudah saya laporkan kepada CSIRT terkait lewat responsible disclosure, dan Alhamdulillah mendapatkan respon dan apresiasi.

Semoga ke depan sistemnya bisa lebih aman, dan ini juga jadi pengalaman berharga buat saya pribadi.

**Timeline:**

Terima kasih kepada tim pengelola Jomart Marketplace / Pemerintah Kabupaten Jombang yang telah menindaklanjuti laporan ini secara serius dan responsif. Temuan sesederhana ini menegaskan bahwa hal mendasar seperti *output encoding* yang terlewat pun masih bisa dijumpai pada layanan publik yang digunakan luas.

“***Stay Ethical,Curious,Learn,and Happy Hacking***”

— Aruna Rasendriya Nirwasita
