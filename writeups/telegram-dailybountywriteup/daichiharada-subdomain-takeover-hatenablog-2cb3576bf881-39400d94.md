# Subdomain Takeover on hatenablog.com (はてなブログ)

- **Source URL:** https://medium.com/@daichiharada/subdomain-takeover-hatenablog-2cb3576bf881?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20240720215236/https://medium.com/@daichiharada/subdomain-takeover-hatenablog-2cb3576bf881
- **Fetched:** 2026-11-27
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/6737 (id 6737)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Subdomain Takeover on hatenablog.com (はてなブログ)

# What is Subdomain Takeover?

This blog explains everything: [https://www.hackerone.com/hackerone-community-blog/guide-subdomain-takeovers](https://www.hackerone.com/hackerone-community-blog/guide-subdomain-takeovers)

# Hatebablog custom domain feature

Hatena blog (はてなブログ) is relatively famous blogging platform in Japan and has unique cultures on it.

As a Hatena Blog PRO (Paid) feature, You can set custom domain on your blog site, with referring A record to 13.230.115.161 / 13.115.18.61 or CNAME record to hatenablog.com. Additionally, you need to set custom domain on hatena blog configuration.

After a while, the domain settings will be verified, and you will be able to access your blog with your custom domain.

# How Subdomain Takeover Happens on Hatenablog?

Since there is no domain verification mechanism, custom domain can be taken over by attackers. Below are the potential scenarios that admins need to be careful.

- Set A/CNAME record but forgot to set hatena blog custom domain
- Deleted hatena blog but forgot to remove A/CNAME record
- Expired hatena blog PRO subscription ? ( Not 100% sure. I didn’t really confirmed this )

# How to Find Subdomain Takeover on Hatenablog?

If you find subdomains referring hatenablog.com / 13.230.115.161 / 13.115.18.61 and if you see this page, that’s it.

To place a PoC, you need to take your own hatena ID, set up a blog, and purchase PRO subscription. Domain configuration can be changed from here: [https://blog.hatena.ne.jp/my/config/detail](https://blog.hatena.ne.jp/my/config/detail)
