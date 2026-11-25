# Bug Bounty শুরু করার আগে যা বুঝতে হবে

- **Source URL:** https://medium.com/@cyber.mehedi.13/bug-bounty-%E0%A6%B6%E0%A7%81%E0%A6%B0%E0%A7%81-%E0%A6%95%E0%A6%B0%E0%A6%BE%E0%A6%B0-%E0%A6%86%E0%A6%97%E0%A7%87-%E0%A6%AF%E0%A6%BE-%E0%A6%AC%E0%A7%81%E0%A6%9D%E0%A6%A4%E0%A7%87-%E0%A6%B9%E0%A6%AC%E0%A7%87-c53ab87a911b
- **Fetched from:** https://medium.com/@cyber.mehedi.13/bug-bounty-%E0%A6%B6%E0%A7%81%E0%A6%B0%E0%A7%81-%E0%A6%95%E0%A6%B0%E0%A6%BE%E0%A6%B0-%E0%A6%86%E0%A6%97%E0%A7%87-%E0%A6%AF%E0%A6%BE-%E0%A6%AC%E0%A7%81%E0%A6%9D%E0%A6%A4%E0%A7%87-%E0%A6%B9%E0%A6%AC%E0%A7%87-c53ab87a911b?source=rss-22cba46b482e------2
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14921 (id 14921)
- **Method:** medium-rss-feed (full content:encoded) readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- **Author/Published (RSS):** Md. Mehedi  hasan Babu / Tue, 22 Sep 2026 20:23:03 GMT

আপনি একটা bug bounty program-এ target পেলেন। Scope দেখলেন। একটা domain, কিছু subdomain, একটা web app।

এখনই কি Burp Suite খুলে random payload ছোড়া শুরু করবেন?

না।

CTF আর Bug Bounty-এর মধ্যে একটা বড় পার্থক্য আছে — CTF-এ vulnerability “থাকবেই”, শুধু খুঁজে বের করতে হয়। Bug Bounty-তে vulnerability “থাকতেও পারে, নাও পারে” — আর সেটা খুঁজে বের করার জন্য আপনাকে অনেক বেশি patient, systematic এবং thorough হতে হয়। Real-world application অনেক বড়, অনেক জটিল, আর হাজার হাজার researcher আগেই সেটা ঘেঁটে দেখেছে।

তাই এখানে সবচেয়ে গুরুত্বপূর্ণ জিনিস হলো — **methodology**।

শুরু করার আগে policy page পুরোপুরি পড়ুন।

খেয়াল করুন:

→ কোন domain/subdomain in-scope, কোনটা out-of-scope?

→ কোন ধরনের vulnerability accept করা হয় না (self-XSS, clickjacking on non-sensitive pages, ইত্যাদি)?

→ Automated scanning allowed কি না, বা rate-limit আছে কি না?

→ Testing-এর জন্য আলাদা account লাগবে কি না?

এই ধাপ স্কিপ করলে আপনি হয়তো ভালো একটা bug পেয়েও report করতে পারবেন না, বা আরও খারাপ — account ban হয়ে যেতে পারে।

Bug Bounty-তে বেশিরভাগ ভালো bug আসে recon থেকে, payload থেকে না। Target-এর যত বেশি attack surface আপনি ম্যাপ করতে পারবেন, সফল হওয়ার সম্ভাবনা তত বাড়বে।

**Subdomain Enumeration**

**Live Host & Port Discovery**

**Content & Endpoint Discovery**

**Technology Fingerprinting**

Recon শেষে সময় নিয়ে application-টা normal user-এর মতো ব্যবহার করুন।

খেয়াল করুন:

→ Sign up, login, password reset flow কীভাবে কাজ করছে?

→ কোথায় file upload আছে?

→ Payment বা checkout flow আছে কি না?

→ Multi-user বা role-based feature আছে কি না (admin vs normal user)?

→ কোনো third-party integration আছে কি না (OAuth, webhook, ইত্যাদি)?

এই সময় Burp Suite proxy চালু রেখে প্রতিটা request capture করুন। পরে এই history-ই আপনার attack surface map হয়ে যাবে।

সব endpoint-এ সব vulnerability খুঁজবেন না — সেটা সময় নষ্ট। বরং functionality অনুযায়ী চিন্তা করুন:

এই approach-এ আপনি “এলোমেলো পরীক্ষা” না করে “targeted পরীক্ষা” করবেন।

শুধু request capture করলেই হবে না — প্রতিটা request-এর behavior বোঝা জরুরি।

ধরুন আপনি একটা e-commerce app টেস্ট করছেন। Order history page-এ URL দেখতে পাচ্ছেন:

GET /api/orders/8842

এখানে সরাসরি payload না ছুঁড়ে, প্রশ্ন করুন:

এই ছোট flow-টাই দেখায় কেন “logic বোঝা” পেলোড মুখস্থ করার চেয়ে অনেক বেশি কার্যকর।

**Access Control**

**Injection**

**Business Logic**

**API-Specific (OWASP API Top 10)**

**Client-Side**

**Server-Side**

অনেক researcher ভালো bug খুঁজে পেয়েও দুর্বল report লেখার কারণে কম bounty পায় বা bug reject হয়।

ভালো report-এ থাকা উচিত:

Triager-রা প্রতিদিন শত শত report দেখে — impact স্পষ্টভাবে বোঝাতে পারলে report priority ও bounty amount দুটোই বাড়ে।

Recon

↓

Understand Functionality

↓

Build Hypothesis

↓

Test

↓

Observe Response

↓

Refine & Retest

↓

Confirm Impact

↓

Write Report

একটা payload কাজ না করলে সেটাকেই বারবার ভিন্নভাবে ছুঁড়বেন না — বরং response থেকে শিখে hypothesis পাল্টান।

Bug Bounty ≠ Random payload try করা।

একজন ভালো bug bounty hunter প্রথমে জানতে চায়:

*“এই application আসলে কী করার কথা?”*

তারপর খোঁজে:

“কোথায় সেটা তার নিজের নিয়ম ভাঙছে?”

Recon-এ যত সময় দেবেন, exploitation ততটাই সহজ হবে। আর report যত স্পষ্ট হবে, bounty ততটাই ভালো পাবেন।
