# Broken Access Control via Hardcoded Bearer Token in Public JS File

- **Source URL:** https://medium.com/@nnouh4967/broken-access-control-via-hardcoded-bearer-token-in-public-js-file-b2f6c87b4d44?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250821183616/https://medium.com/@nnouh4967/broken-access-control-via-hardcoded-bearer-token-in-public-js-file-b2f6c87b4d44
- **Fetched:** 2026-11-19
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/10041 (id 10041)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Broken Access Control via Hardcoded Bearer Token in Public JS File 💥

**بِسْمِ اللَّـهِ الرَّحْمَٰنِ الرَّحِيمِ، وَالصَّلَاةُ وَالسَّلَامُ عَلَىٰ الْمَبْعُوثِ رَحْمَةً لِلْعَالَمِينَ ﷺ**

# Hidden Secrets in JavaScript — How I Gained Full Access to Modify Product Metadata (description, blocked…)

**Hello hackers!**

In this write-up, I’ll walk you through a real story where I found a powerful **Bearer token** hidden inside a **public JavaScript file**.

This one token led to **full read/write access** to sensitive product data — yes, full control! 

Let’s call the target `example.com` for privacy reasons.

**Grab your coffee and let’s dive in ☕**

# The Hunt Begins — Browsing JS Files

While casually reviewing public-facing JavaScript files on the target website, I stumbled upon something that made my inner hacker scream:

`Authorization: Bearer 9332e73dbc1e4ccda90db1dc4...`
Yep — a **hardcoded token** in plain sight.

No protection, no obfuscation, just chilling there in the JS file.

I knew I had to move fast.

# Step 1 — Searching for Vulnerable Endpoints

The next step was simple: **Find where this token works.**

After some endpoint discovery and testing, I hit a **goldmine**:

`GET /bc/v2/items`
This endpoint returned **all product metadata**, including:

- Product numbers (`no`)
- Descriptions
- Blocked status
- Categories
- And more…

# Wait… What Is `/bc/v2/items`?

I noticed the structure follows a **RESTful API** pattern. Here’s a quick breakdown:

Part Meaning `/bc` Likely stands for "business control" or a module `/v2` API version 2 `/items` Collection of product items `/123456` Path parameter – specific product ID

So basically, I could interact with individual products like this:

`/bc/v2/items/123456`
# Step 2 — Let’s Try to Modify Something…

Now the real fun begins 

I changed the method to `PATCH` and tried modifying a product:

```
PATCH /bc/v2/items/123456
Authorization: Bearer [leaked token]
Content-Type: application/json
```
```
{
  "description": "Na7na7 was here!",
  "blocked": true
}
```
✅ Boom! The server responded with `200 OK` and reflected the changes:

Then I fetched `/bc/v2/items` again to confirm — and yes, the changes were saved

# Why PATCH and Not POST?

Here’s the difference in simple terms:

`POST` is used when you want to **create a new resource** — like adding a brand-new product to the database. Every time you send a POST request, it usually creates something new.

On the other hand, `PATCH` is used when you want to **modify part of an existing resource**. It doesn't replace the whole thing — it just updates the fields you include in the request.

Also, PATCH is **idempotent**, which means sending the same PATCH request multiple times will have the same result. But POST is **not idempotent**, because repeating it might create multiple new entries.

So in my case, since I wanted to **update an existing product**, `PATCH` was the perfect choice — and a great way to test for broken access controls .

# Why This Matters

This wasn’t just a small bug — the token gave me:

Full **unauthorized access** to internal APIs

- ️ Ability to **read, edit, and corrupt** products
- Potential to **disrupt the business logi**c and supply chain
- If deployed to production — this could have caused **massive data integrity issue**s

# Final Thoughts

*💡 Lesson for developers:*

Never hardcode secrets into frontend JS files.

Use environment variables. Rotate tokens.

*Always enforce proper authentication and authorization on the server side.*


Although the report was accepted as a **P2 (High Severity)** issue, unfortunately, it was submitted under a **VDP** — .

Still, it was a great learning experience and a solid addition to my hacking journey
