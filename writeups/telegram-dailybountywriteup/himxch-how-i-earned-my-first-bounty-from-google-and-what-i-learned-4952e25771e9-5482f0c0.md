# How I Earned My First $$$ Bounty from Google — And What I Learned

- **Source URL:** https://medium.com/@himxch/how-i-earned-my-first-bounty-from-google-and-what-i-learned-4952e25771e9
- **Fetched from:** https://medium.com/@himxch/how-i-earned-my-first-bounty-from-google-and-what-i-learned-4952e25771e9?source=rss-42e10082a76f------2
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14938 (id 14938)
- **Method:** medium-rss-feed (full content:encoded) readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- **Author/Published (RSS):** Himxch / Wed, 07 Oct 2026 18:30:16 GMT

**Bug Bounty | Cloud Security | Responsible Disclosure**

I’ve been doing security research for a while, but landing my first significant bug bounty reward from a major tech company felt different. Not just because of the money — but because it proved that methodical research, persistence, and the right framing can turn an auto-rejected vulnerability into a confirmed fix and a real payout.

This is the story of how I found a security misconfiguration in Google’s infrastructure, overcame an initial rejection, and earned my first Google VRP reward. Along the way, I learned lessons about cloud security, responsible disclosure, and how to present a finding so that it lands.

I was doing routine research on how cloud platforms configure storage access for public-facing features. I identified a Google-hosted service with a public-sharing feature — users can export content, generate a link, and share it with anyone.

Simple feature: you create something, you get a link, anyone with that link can access it.

The question I asked myself: *What permissions are actually needed for that? And what permissions are actually granted?*

I started probing the cloud storage backend that backs this feature — and that’s where I found the gap.

When I tested the storage backend, I discovered the bucket had been configured with overly permissive IAM policies.

**The technical issue:**

The service’s sharing feature only requires a single permission: read specific objects by direct reference. That's it. If you have a share link, you can fetch the file it points to. That's the intended behavior.

But the bucket’s IAM policy granted allUsers a broader role that bundled two permissions:

The second permission shouldn’t be there. The sharing feature never uses it. But it was granted anyway.

**What this means:**

With the list permission, I could query the storage API directly and retrieve a complete index of *every object* ever stored in that bucket — no authentication needed, no link required, no prior knowledge of any object name.

It’s like leaving the front door locked but the complete guest list visible outside. The sharing feature intended only for people with a key, but the entire directory is indexable without one.

**Step 1: List the bucket index**

I queried the storage API’s list endpoint with no authentication:

GET https://storage.googleapis.com/\[bucket-name\]/

Response: a complete index of thousands of objects, with direct download links, creation dates, and file sizes.

**Step 2: Download arbitrary objects**

Each object in the listing came with a direct mediaLink. I could fetch any object by simply requesting it:

GET https://storage.googleapis.com/download/\[object-path\]

No authentication required. No rate limiting observed.

**Step 3: Verify scale**

I paginated through the full listing using the nextPageToken field. The bucket contained thousands of user-generated objects spanning years of data. All enumerable, all downloadable, all unauthenticated.

**1. Bulk Extraction of All User Content**

An attacker could automatically download every object ever created on the platform. Instead of accessing only the content they had a link to, they could grab everything at once — thousands of files spanning years of data.

**2. Unintended Information Disclosure**

Object metadata and user-supplied labels are stored alongside each file. During testing, I found multiple instances where users had included personal information (names, IDs, email addresses, etc.) in their object metadata — information they clearly never intended to be publicly discoverable. They thought they were sharing a private link; the enumeration exposed them at scale anyway.

**3. No Safeguards**

The system had no rate limiting or CAPTCHA to stop automated bulk extraction. It was trivially easy to pull everything at scale.

I filed my report on Google’s Bug Hunters platform, laying out:

**The first response**: Rejected. Auto-classified as “Intended Behavior.”

Their reasoning: public buckets for sharing features are standard, and it’s the customer’s job to configure them correctly.

That stung. But I was confident I had something real — the distinction between *reads* and *listing* is crucial, and they’d missed it.

**My rebuttal**: I pushed back with a more precise framing. I pointed out that this service isn’t a third-party customer’s GCP project — it’s Google’s own product infrastructure. The “shared responsibility model” doesn’t apply when Google owns and operates the bucket themselves. And I emphasized again: the issue isn’t that reads are public (they should be for sharing), it’s that listing the entire bucket index is public (it shouldn’t be).

**The result**: They re-opened it. Formal bug classification. Assigned to their engineering team. Confirmed fixed. And $$$ reward approved.

That first rejection taught me something valuable: if you’re confident in your finding, it’s worth a well-articulated push-back. Not aggressive, not argumentative — just precise.

This was a textbook case of “permission creep” — the bucket’s IAM policy granted more permissions than the feature actually used.

**The root cause:** Predefined IAM roles bundle multiple permissions for convenience. The role granted included both read and list, but only read was needed. This is a common trap — you grant a role for one permission, and get others you didn't plan for.

**The fix:** Replace the overly broad role with one that grants only read — no list. Cloud platforms typically offer both bundled roles (for convenience) and granular roles (for precision). This case needed precision.

**Why it matters:**

The lesson: audit your IAM bindings regularly. One permission you didn’t mean to grant can turn a secure design into an exposure.

**Don’t give up on auto-rejections.** When Google said “Intended Behavior,” I could have accepted it and moved on. But I’d invested time in understanding the distinction between the two permissions, and I was confident in my framing. One more email with the right argument flipped the decision. Auto-rejections are filters, not verdicts.

**Precision beats volume.** I didn’t try to inflate the severity or manufacture urgency. I presented a clear technical argument: get vs. list, intentional vs. unintentional, with proof. Google responded to that precision. They didn't need a flashy report or a YouTube video — they needed clarity.

**First-party infrastructure matters.** Just because Google hosts something doesn’t mean it’s automatically secure. First-party products have the same permission creep and configuration issues as customer workloads. They’re worth researching.

**Responsible disclosure actually works.** This is probably the most important takeaway. Google fixed the issue. They paid the bounty. They’re supportive of the writeup. The whole process is designed to incentivize researchers to report vulnerabilities responsibly instead of exploiting them. It works.

If you’re managing cloud infrastructure, here’s the takeaway: regularly audit what permissions your apps actually need vs. what you’ve granted them. Convenience (bundled permissions, predefined roles) often leads to overpermissioning. Test your public endpoints as an outsider would — sometimes that’s the only way to see what you’re really exposing.

Thanks to Google’s security team for the prompt response and fix, and for rewarding the research. And thanks to everyone working on bug bounty programs — they make the internet a little bit safer.

**Tags**: #BugBounty #CloudSecurity #IAMSecurity #Cybersecurity #ResponsibleDisclosure #InformationSecurity #VulnerabilityResearch #GoogleVRP

**Have a security finding of your own?** Consider responsible disclosure — most major platforms have VRP programs and actively reward researchers who follow the right process.
