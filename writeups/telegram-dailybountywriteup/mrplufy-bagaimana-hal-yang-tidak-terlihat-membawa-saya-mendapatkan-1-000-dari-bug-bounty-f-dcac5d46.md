# Bagaimana “Hal yang Tidak Terlihat” Membawa Saya Mendapatkan $1.000 dari Bug Bounty

- **Source URL:** https://medium.com/@MrPlufy/bagaimana-hal-yang-tidak-terlihat-membawa-saya-mendapatkan-1-000-dari-bug-bounty-f44baec86368
- **Fetched from:** https://medium.com/@MrPlufy/bagaimana-hal-yang-tidak-terlihat-membawa-saya-mendapatkan-1-000-dari-bug-bounty-f44baec86368?source=rss-2e69ae55a3e8------2
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14899 (id 14899)
- **Method:** medium-rss-feed (full content:encoded) readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- **Author/Published (RSS):** Ahmad Tazkiarni Ramadhan / Sun, 06 Sep 2026 02:29:02 GMT

Banyak hal dari para pemburu yang mereka lewatkan dan tidak menyadari tentang hal yang tidak terlihat namun menghasilkan $1.000 hanya dari hal yang sederhana.

Pada tulisan kali ini, saya ingin membagikan suatu hal yang mungkin banyak terlewatkan oleh pemburu kerentanan lain yang mereka tidak sadari dan sering mereka lewatkan.

Hal ini bisa terjadi karena kebanyakan dari kita (termasuk saya) mungkin terlalu fokus dengan hal yang terlihat seperti fitur, form dan sebagainya. sehingga kita lupa untuk mengecek disisi server apakah itu dapat diterima atau tidak. Hal ini kadang yang luput dari perhatian sehingga banyak yang terlewatkan ketika kita mencari sebuah kerentanan.

Sebelum semua ini terjadi, saya telah melaporkan kerentanan Parameter Injection yang dimana seorang user bisa melakukan manipulasi status file “Pending” menjadi “Approved”. Karena kerentanan ini terjadi akibat server terlalu mempercayai inputan yang dikirim oleh user dalam request.

Pada request tersebut, ketika user mencoba untuk mengedit file miliknya dan mengirim permintaan edit tersebut. Pada request edit tersebut menyertakan parameter “status”:”pending” dan user dapat merubah parameter tersebut menjadi “status”:”approved” sehingga file yang tadinya akan diperiksa oleh team internal bisa menjadi terlewatkan.

Setelah saya melaporkan kerentanan ini dan mendapatkan imbalan $500 dari penyelerangga bug bouty. Akhirnya mereka menutup kerentanan itu dengan menghapus parameter yang bermasalah dari request. Dan ketika mereka menyuruh saya untuk mengecek hasil perbaikannya, saya pikir itu sudah selesai dan masalah sebenarnya sudah teratasi karena parameter yang bermasalah sudah dihapus dari request.

Tapi ….. itu belum menjadi solusi yang tepat !!! Kenapa hal itu bisa terjadi ?. Developer berasumsi bahwa dengan menghapus parameter yang bermasalah sudah mengatasi celah kerentanan tersebut. Sebenenarnya yang terjadi tidaklah demikian. Karena menghapus saja tidaklah cukup tanpa melakukan validasi disisi server untuk memastikan bahwa server juga aman dari inputan yang dimasukan oleh user.

Ketika saya sedang mengamati perilaku dari request yang telah dihapus oleh team developer. Saya mendapatkan pencerahan mengenai hal selanjutnya “Apakah dengan menghapus parameter ini membuatnya menjadi lebih aman?”, “Bagaimana dengan server?” dan “Apakah jika saya memasukannya sekali lagi dengan manual server akan menerima hal tersebut?”.

Ini adalah request awal setelah perbaikan. Nampak sudah aman tetapi sebenarnya masih rentan.

Setelah saya memasukan parameter “status”:”active” secara manual.

Dan BOOMM !!! Server kembali meresponse hal tersebut dan mengubah file menjadi status active kembali.

Meskipun developer telah melakukan perbaikan dengan menghapus parameter tersebut. Cara itu ternyata masih belum sepenuhnya efektif karena server ternyata tidak dilindungi dan divalidasi sehingga membuatnya tetap rentan.

Atas kejadian ini, saya kembali melaporkan kerentanan tersebut dengan semua hal yang dibutuhkan secara terperinci dan lengkap. Tentang bagaimana server tetap meresponse permintaan tersebut tanpa adanya validasi yang diperbaiki.

Akhirnya mereka memvalidasi dan mengakui kesalahan tersebut serta membayar imbalan yang sama dengan yang sebelumnya. Karena root cause dan impactnya masih tetap sama berdasarkan kerenatan sebelumnya.

Pelajaran yang bisa diambil dari kejadian ini :

Bagi Bug Hunter pelajaran yang bisa diambil adalah jangan hanya mengamati apa yang terlihat. Tapi, mulailah dari hal yang tidak terlihat maksudnya adalah dengan mengamati perilaku dari server tersebut. Karena, dengan mengamati perilaku dari server kita bisa menentukan tindakan untuk selanjutnya.

Perhatikan bahwa ketika anda menemukan kerentanan yang telah diperbaiki, lihat bagaimana server tersebut meresponse dan menyelesaikan masalah dari kerentananya. Itu akan memberikan banyak gambaran mengenai cara untuk melewati perbaikan tersebut.

Bagi Developer pelajaran yang bisa diambil adalah jangan terlalu mengandalkan semuanya dari sisi client meskipun parameter dari sisi client sudah dihilangkan. Selalu lakukan perbaikan hingga ke sisi server dan lakukan secara menyeluruh. Dengan begitu, mungkin masalah dapat teratasi dengan lebih baik lagi.

Terimakasih telah menyempatkan waktunya untuk membaca tulisan ini. Semoga ini dapat bermanfaat terutama bagi kita semua yang haus akan ilmu.

Jangan lupa berikan Tanggapan dan Komentar terbaiknya karena itu adalah semangat bagi saya untuk menulis write-up lainnya,
