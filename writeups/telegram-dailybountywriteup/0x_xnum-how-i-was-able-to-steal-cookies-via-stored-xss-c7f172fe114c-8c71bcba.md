# How I was able to steal cookies via stored XSS

- **Source URL:** https://medium.com/@0x_xnum/how-i-was-able-to-steal-cookies-via-stored-xss-c7f172fe114c?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20240715223505/https://medium.com/@0x_xnum/how-i-was-able-to-steal-cookies-via-stored-xss-c7f172fe114c?source=rss------bug_bounty-5
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/6526 (id 6526)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# How I was able to steal user cookies via stored XSS

well that wasn’t too long !

hello again, it’s ahmed tarek and I recently found a significant stored XSS (Cross-Site Scripting) with vulnerability on a web platform and wanted to share the details with you all. This finding highlights the importance of web security and proper input validation.

well as usaual our target is www.target.com which is an e-commerce platform where users can buy products and also create shops and add products to their shop.

so i created two accounts: an user account and a shop account

from the shop account I created a shop named “ahmed” under a random category called “Ahmeee”.

then i went to Add New Product and added a new product but Instead of giving a normal name to a product, I thought, why not try an XSS payload?

Here’s what I used :

*\<img src=”invalid-image” onerror=”alert(document.cookie)”>*

then i clicked in “Add Product” and navigate to my user account

From the user account, I visited my shop and clicked on the category “Ahmeee”.

then I found the product that I had injected with the XSS payload!

I clicked on the product, then clicked “Add to Cart”, and boom, the XSS payload executed, displaying the user session cookies!

**Impact:** This vulnerability allows attackers to hijack user sessions by capturing their cookies, leading to potential unauthorized access to user accounts.

**Recommendation:** Proper input sanitization and output encoding should be implemented to prevent such attacks. Additionally, deploying a Content Security Policy (CSP) can help mitigate this vulnerability.

# Lesson Learnt !

Inject XSS payloads in every input you see; maybe it will work!

\*\*edit\*\*

Well the program was a scam, and doesn’t even respond to the reports so avoid it if you find it, it’s “dukaan.com”

\*\*edit\*\*

you can follow me on social media to see more Write-Ups
