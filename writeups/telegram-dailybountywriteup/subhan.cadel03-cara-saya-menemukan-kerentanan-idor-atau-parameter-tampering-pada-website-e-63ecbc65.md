# CARA SAYA MENEMUKAN KERENTANAN IDOR ATAU PARAMETER TAMPERING PADA WEBSITE ECOMMERCE

- **Source URL:** https://medium.com/@subhan.cadel03/cara-saya-menemukan-kerentanan-idor-atau-parameter-tampering-pada-website-ecommerce-58e83399b2ae?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20230325093658/https://medium.com/@subhan.cadel03/cara-saya-menemukan-kerentanan-idor-atau-parameter-tampering-pada-website-ecommerce-58e83399b2ae
- **Fetched:** 2026-11-24
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/2096 (id 2096)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# CARA SAYA MENEMUKAN KERENTANAN IDOR ATAU PARAMETER TAMPERING PADA WEBSITE ECOMMERCE

Hello perkenalkan saya subhan, ini merupakan tulisan pertama saya dan kali ini saya mau berbagi cerita tentang temuan saya yaitu temuan kerentanan parameter tampering atau IDOR atau apapun itulah namanya.

saya menemukan kerentanan ini disalah satu platform penjualan alat masak yang ada di indonesia. Awal mula saya menukan kerentanan ini adalah ketika saya coba-coba mencari target untuk melakukan penetrasi testing kemudian setelah melakukan pencarian akhirnya saya sampai pada ecommerce ini( “*sebut saja www.nanana.co.id”).* setelah melakukan riview terhadap website, pikiran saya tertuju pada fitur penjualannya, *“kayaknya merubah harga barang seru nih!”.* Akhirnya saya buka Burpsuite dengan maksud untuk menangkap request yang dikirimkan website ke server. kemudian saya mencoba memilih barang yang ingin saya beli

Disini saya mencoba memesan satu barang dengan harga 227k yang dikirim dengan menggunakan JNE. kemudian saya masuk ke Burpsuite untuk menangkap request yang dikirmkan keserver

disini saya mencoba mencari nilai pembayaran yang mana disini bisa kita lihat hasil intercep dari Burpsuite, saya menemukan harga pembayaran seperti yang saya lingkar biru. Kemudian saya coba mengganti value nya dengan harga 500 rupiah kemudian mengirimkannya kembali and boom.!!!!

Harga yang seharunya 227 ribu berubah menjadi 500 rupiah. uwuwuwuwuwuwuwuwuwuuwuw

kemudian dengan bukti yang cukup kuat akhirnya saya memutuskan melaporkan temuan saya ke pemilik website.

TAMAT.!!!!!!!!!

Saksikan tulisan saya selanjutnya, babai.!!!!!
