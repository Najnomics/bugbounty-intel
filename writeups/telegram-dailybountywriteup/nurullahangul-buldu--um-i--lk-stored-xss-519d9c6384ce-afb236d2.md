# [TR] Bulduğum İlk Stored XSS

- **Source URL:** https://medium.com/@nurullaHangul/buldu%C4%9Fum-i%CC%87lk-stored-xss-519d9c6384ce?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20230410235159/https://medium.com/@nurullaHangul/buldu%C4%9Fum-i%CC%87lk-stored-xss-519d9c6384ce?source=rss------bug_bounty-5
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/2256 (id 2256)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# \[TR\] Bulduğum İlk Stored XSS

XSS sayesinde web tarayıcılarında istediğimiz zararlı kodları çalıştırabiliriz. Örneğin cookie ve kişisel bilgileri çalabilir, bilgisayarlara programlar indirtebiliriz.

## Etki:

İsim kısmına zararlı BEEF kodu yazıldığında yorumlarımı görüntüleyen kullanıcılar ve profilimi görüntüleyen web sitesi adminlerinin web tarayıcılarında zararlı kodlar çalıştırabilir ve bir trojan indirtebilirim.

## Tespit:

Web sitesinde adres bilgilerim kısmının kaynak kodlarına baktım ve HTML tagları içerisinde value kısmına yazıldığını gördüm.

İsim kısmında filtreleme olup olmadığını öğrenmek için \<>/ karakterlerini yazdım ve herhangi bir filtreleme olmadığını gördüm.

## Saldırı Aşaması:

Yazdığım bilgiler value kısmında “” içerisinde kaldı ve XSS kodum çalışmadı. Bende 1 tane “ koydum ve value kısmından çıktım daha sonra payloadı yazdım. *“\<script>alert(8)\</script>*

## 2. Stored XSS:

Adres kısmına baktım ve \<textarea> içerisinde yazıldığını farkettim.

Scriptin çalışması için \<textarea> tag’ini kapatmam gerekti.

Diğer profil bilgilerinde de benzer işlemleri uygulayarak xss payloadını çalıştırdım.
