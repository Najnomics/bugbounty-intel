# Belajar dari Celah RCE di NASA VDP

- **Source URL:** https://medium.com/@radith614/belajar-dari-celah-rce-di-nasa-vdp-dokumentasi-dan-analisis-teknis-0a61473cab43
- **Fetched from:** https://medium.com/@radith614/belajar-dari-celah-rce-di-nasa-vdp-dokumentasi-dan-analisis-teknis-0a61473cab43?source=rss-018a8bd5d10c------2
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:**  (id 14898)
- **Method:** medium-rss-feed (full content:encoded) readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- **Author/Published (RSS):** Radith / Fri, 04 Sep 2026 22:59:18 GMT

Oleh: Adiel Radithya Putra Irwana

Halo rekan-rekan aku adalah Tech Enthusiast dan juga sebagai pelajar, semoga kita semua senantiasa dalam semangat untuk terus mengeksplorasi dan belajar.

Artikel ini saya tulis murni sebagai sarana berbagi wawasan (*knowledge sharing*) dan dokumentasi portofolio teknis dari salah satu temuan saya di program *Vulnerability Disclosure Program* (VDP) NASA. Sebagai seorang pelajar yang saat ini duduk di bangku **kelas 12 TJKT 1 jurusan Teknik Jaringan Komputer dan Telekomunikasi (TJKT) di SMKN 1 Kota Bengkulu**, saya percaya bahwa usia atau status pendidikan bukanlah batasan untuk terus berkarya. Belakangan ini, mungkin terdapat beberapa diskusi atau simpang siur informasi mengenai validitas temuan ini. Sebagai sesama pembelajar yang menjunjung tinggi transparansi dan integritas, saya merasa cara paling elegan untuk menjawab keraguan tersebut adalah dengan menyajikan data teknis yang objektif dan bukti resmi. Di dunia *cybersecurity*, kita semua berangkat dari titik yang sama — sebagai pelajar — dan selalu ada ruang untuk saling mendukung dan bertumbuh bersama.

Mari kita bedah secara sederhana dan teknis bagaimana celah *Unauthenticated OS Command Injection* (Remote Code Execution / RCE) ini ditemukan, dampaknya, serta bagaimana mitigasi yang tepat. Laporan ini telah berstatus DISCLOSED (*Coordinated Disclosure*) secara resmi oleh tim NASA di Bugcrowd.

**1. Reconnaissance & Discovery (Pengumpulan Informasi)** Dalam setiap pengujian keamanan, fase pengumpulan informasi adalah fondasi utamanya. Saat memetakan aset digital milik Badan Penerbangan dan Antariksa Nasional (NASA), salah satu target cakupan (*scope*) yang menarik perhatian saya adalah layanan publik di bawah ekosistem \[https://nasa.gov\](https://nasa.gov).

Fokus pengamatan saya tertuju pada Layanan Pemuatan Massal Internasional NASA, spesifiknya pada *endpoint* skrip di \[TARGET\_DOMAIN\]/cgi-bin/eop\_series.py. Bayangkan skrip ini seperti jembatan otomatis di belakang layar yang menerima data dari pengguna (lewat tautan *website*) lalu menyuruh komputer server untuk menjalankan perintah tertentu. Dari kacamata seorang pelajar TJKT yang terbiasa mempelajari jaringan dan sistem komputer, area yang langsung berinteraksi dengan sistem operasi tingkat rendah seperti ini sering kali menyimpan celah jika tidak dijaga ketat.

**2. Technical Deep Dive (Analisis Akar Masalah)** Mengapa skrip tersebut bisa rentan terhadap RCE (Eksekusi Perintah Jarak Jauh)? Sederhananya, aplikasi web ini menerima masukan dari pengguna melalui tautan URL (misalnya parameter eop\_group), lalu menggabungkannya ke dalam perintah sistem operasi tanpa penyaringan yang benar.

**3. Proof of Concept (PoC) & Safe Exploitation** Untuk membuktikan kerentanan ini secara aman tanpa merusak sistem, saya menguji pengiriman perintah melalui tautan URL sederhana.

Ketika mencoba menyisipkan perintah menggunakan titik koma (%3B), sistem berhasil menolak dan memblokirnya. Namun, karena karakter ampersand (%26) diizinkan, kita bisa memanfaatkannya untuk menyisipkan perintah dasar sistem seperti id melalui tautan *web*.

Hasil respons dari server menampilkan teks seperti uid=33(apache). Artinya, perintah tambahan yang dikirimkan berhasil dijalankan oleh server. Celah ini sangat berbahaya karena penyerang dapat masuk tanpa perlu memasukkan kata sandi (*unauthenticated*), lalu mengambil kendali penuh atas hak istimewa *user* server untuk membaca, menulis, atau memodifikasi data di dalam sistem hosting tersebut.

**4. Remediation (Solusi dan Perbaikan)** Sebagai bagian dari edukasi untuk membangun aplikasi yang lebih aman, celah ini dapat ditutup melalui beberapa langkah mitigasi:

**5. Timeline & Official Recognition** Proses penanganan celah ini berjalan dengan sangat profesional melalui koordinasi yang baik bersama tim keamanan:

Sebagai bentuk apresiasi atas kontribusi ini, saya menerima Surat Pengakuan Resmi (*Letter of Recognition* / LoR) dari NASA VDP atas nama **Adiel Radithya Putra Irwana**. Pencapaian ini menjadi motivasi besar bagi saya, khususnya sebagai siswa SMK yang ingin terus membuktikan bahwa semangat belajar dapat membawa kita melangkah jauh.

Semoga bedah teknis ini dapat menjawab rasa penasaran teman-teman sekaligus memberikan sudut pandang objektif mengenai keamanan siber. Di atas langit masih ada langit; esok hari selalu ada hal baru untuk dipelajari. Mari kita jadikan komunitas teknologi di Indonesia sebagai ruang yang aman, sehat, dan saling mendukung.

Bagaimana menurut kalian, pendekatan apa yang biasanya paling efektif untuk mendeteksi celah keamanan pada aplikasi web saat pertama kali melakukan pengujian?
