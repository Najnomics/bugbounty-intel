# [Business Logic Error] Coupon Code Reuse and Stack leads to Buy Product for Free.

- **Source URL:** https://betabyte.medium.com/business-logic-error-coupon-code-reuse-and-stack-leads-to-buy-product-for-free-38420b02c94a
- **Fetched from:** https://betabyte.medium.com/business-logic-error-coupon-code-reuse-and-stack-leads-to-buy-product-for-free-38420b02c94a?source=rss-31f81e7598aa------2
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14960 (id 14960)
- **Method:** medium-rss-feed (full content:encoded) readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- **Author/Published (RSS):** Md. Hachib Kazi / Tue, 27 Oct 2026 01:01:02 GMT

FLAG: INTIGRITI{094638e6-ba2f-4c50–8bb4–41ced0d5debd}

**Challenge:** Halloween Store

**Platform:** intigriti

**Category:** Web Security / Business Logic Error

**Vulnerability:** Payment Bypass via Coupon Reuse

**Difficulty:** Medium

**Intigriti’s Challenge 1026** Created by **Globules**

**Target:** *https://challenge-1026.challenges.intigriti.io/challenge*

This is **Intigriti’s Challenge 1026** Created by **Globules.** The challange contains a Business Logic Error in Coupon code functionality. Any coupon code can be used multiple times and multiple coupon code can be used in a single order.

This is a classical business logic issue which leads to buy any product for free. The root cause of this issue is that the application doesn’t enforce proper validation on **Coupon Code** usages that’s leads anyone to stack multiple coupon code and reuse coupon code in a single order. We got our first coupon code as **October Exclusive: NIGHT20 gives 20% off The Midnight Collection** at the top of the challenge site and we get another coupon code by **subscribe the newsletter**. The second code is **NEWS30 gives 30% off** . Both code is reusable and can be stacked.

3\. Get the first coupon code ***NIGHT20*** from top of the challange page.

4\. Get the second coupon code ***NEWS30*** by ***subscribing the newsletter***.

5\. Now use the coupon code one by one two times each.

6. ***NIGHT20 > NEWS30 > NIGHT20 > NEWS30*** or vice verca.

7\. When the price get down to **$0**, then place the order to get the flag.

This small business logic issue has huge effect on a business. It enables an attacker to:

Business Logic Error is an overlooked vulnerability in web application. Any automated tools or scanner cannot find this type of vulnerability. This challenge shows how a small logic issue on coupon code use can leads the company to huge financial loss.

**Key Takeways:** Always invalidate coupon code after single used or make it limited to one use for every account. Also enforce single coupon code use in a single order.

This write-up is being created for educational and CTF purposes only. All the testing was performed with proper authorization on Intigriti October 2026 CTF challenge environment and by following the program rules.
