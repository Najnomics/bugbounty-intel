# — without spending a dollar.

- **Source URL:** https://medium.com/@kokyaw-gza/without-spending-a-dollar-873632f8fe21
- **Fetched from:** https://medium.com/@kokyaw-gza/without-spending-a-dollar-873632f8fe21?source=rss-e2bca7bb9da4------2
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14882 (id 14882)
- **Method:** medium-rss-feed (full content:encoded) readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- **Author/Published (RSS):**  GhostZA (ကိုကျော်) / Wed, 26 Aug 2026 16:53:21 GMT

— without spending a dollar.

The first time I found an unauthenticated ComfyUI instance sitting on a public IP, rendering someone’s custom AI videos without a password — I almost closed my laptop and walked away.

It was too easy. No exploit. No CVE. Just… open.

Three years later, I’ve mapped thousands of similar instances across hundreds of platforms. This is the workflow I use, the tools I rely on, and the lessons I’ve learned along the way.

I’m not a company. I don’t sell courses. I don’t run a “consulting firm.” I’m one person in Yangon with a fiber connection and too much free time.

This is what I actually do.

\## Why AI Platforms Are a Goldmine (Right Now)

AI is the fastest-growing attack surface in 2026. Every week, dozens of new AI startups ship a product built on:

The developers are brilliant. They’re building faster than any security team can keep up with. That’s not their fault — that’s the gap I live in.

\## My Default Recon Stack (All Free, All Open Source)

I don’t have a Burp Pro license. I don’t need one.

That’s it. No Splunk. No Tenable. No enterprise nonsense.

\## The 5 Patterns I Find Every Week

After thousands of probes, I’ve narrowed it down to five recurring patterns:

\### 1. The “Anonymous Supabase” Leak

Startup builds with NEXT\_PUBLIC\_SUPABASE\_ANON\_KEY=... in their client bundle. RLS is set on most tables — but not all. One forgotten users table with auth.role() = 'anon' read access = the entire database.

\### 2. The ComfyUI on Port 8188

Someone runs ComfyUI with --listen 0.0.0.0 --enable-cors-header \* for “remote access.” Now anyone on the internet can submit prompts on their GPU.

\### 3. The Stripe Refund Race

Checkout flow charges once. Refund webhook processes async. Submit 5 simultaneous refund requests = 5x your money back before the order even clears.

\### 4. The Unauthenticated Admin Panel

Build an admin dashboard. Forget the auth middleware. Expose it at /admin. The internets finds it in 6 hours.

\### 5. The MCP Server with --no-auth

Model Context Protocol servers are the new hotness. Some ship with default config that lets any client connect — and most of them have shell access.

I have working PoCs for all five. I publish them on GitHub under kokyaw-gza/ when I have time. The goal isn’t the loot — it’s making sure the vendor patches it.

\## My Disclosure Ethic

I’m not in this for “bounties.” I disclose to vendors when:

For big platforms (the FAANG-tier), I keep the methodology public and the specifics private. If I find a €300 credit forge on a major AI platform, I don’t post the exact RPC endpoint — I post the pattern. Vendors fix the class of bug, not just my instance.

This keeps me out of jail and keeps the vendors honest. Win-win.

\## What’s Next

I’m going to start publishing my toolset on GitHub over the coming weeks:

If you find my work useful, follow me here. Or check the GitHub: github.com/kokyaw-gza

I’m one person. I’m not fast. But I find things.

— -
