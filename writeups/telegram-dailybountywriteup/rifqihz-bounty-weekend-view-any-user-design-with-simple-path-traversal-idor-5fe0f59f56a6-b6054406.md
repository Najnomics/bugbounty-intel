# [Bounty Weekend] View Any User Design With Simple Path Traversal IDOR

- **Source URL:** https://medium.com/@rifqihz/bounty-weekend-view-any-user-design-with-simple-path-traversal-idor-5fe0f59f56a6?source=rss------bug_bounty-5
- **Fetched from:** https://medium.com/feed/@rifqihz
- **Fetched:** 2026-11-19
- **Channel:** @dailybountywriteup
- **Telegram message:**  (id 6414)
- **Method:** medium-rss-content readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
Bismillah, hello there ! I’m Rifqihz, a penetration tester, bug hunter and a college student who’s currently learning and writing about cyber security related topics.

Welcome to the **3rd** article of “**Bounty Weekend**”. I created this mini project to share about my bug bounty reports, technique, ideas and all things related to bug bounty. So please enjoy and give me any advice if you have one !

#### Background

The target application is a platform that allows users to create personalized designs for products and then purchase these customized items. Users can choose from various templates or upload their own designs to be printed on the products, ensuring a unique and personalized shopping experience.

#### Discovery

While accessing my design. I found this request

GET https://www.domain.com/ucd/ucd.php?action=load&xmlpath=/files/cart\_items/193/61304833/UCD.xml&convertYear=0&is\_temp=0

The request will return a response containing XML data about user design

#### Analysis

In the xmlpath parameter I found that it used a specific format

/file/cart\_items/\<category\_id>/\<design\_id>/UCD.xml

I tried to change the design\_id to my test account design id. But it return 403 forbidden.

### Exploitation

We can bypass it by using path traversal. Payload :

/file/cart\_items/\<category\_id>/\<attacker\_design\_id>/../\<victim\_design\_id>/UCD

### Report

The CVSS scoring were using Hackerone 3.0 CVSS

CVSS:3.0/AV:N/AC:L/PR:L/UI:N/S:U/C:L/I:N/A:N/CR:X/IR:X/AR:X

Alhamdulillah, you’ve reach the end. Hopefully you learn something from here and thanks for your support !

I’m sorry if it’s lack of screenshots because it’s a report from 2022 and i don’t really document it well back then :(
