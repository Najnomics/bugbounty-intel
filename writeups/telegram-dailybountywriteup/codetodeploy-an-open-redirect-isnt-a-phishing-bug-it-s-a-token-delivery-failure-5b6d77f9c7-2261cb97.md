# An Open Redirect Isn’t a Phishing Bug. It’s a Token Delivery Failure.

- **Source URL:** https://medium.com/codetodeploy/an-open-redirect-isnt-a-phishing-bug-it-s-a-token-delivery-failure-5b6d77f9c794
- **Fetched from:** https://web.archive.org/web/20261111075314/https://medium.com/codetodeploy/an-open-redirect-isnt-a-phishing-bug-it-s-a-token-delivery-failure-5b6d77f9c794
- **Fetched:** 2026-11-27
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14959 (id 14959)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
Member-only story

# An Open Redirect Isn’t a Phishing Bug. It’s a Token Delivery Failure.

*When the browser is carrying a credential, a redirect isn’t a redirect. It’s a delivery.*

*⚠️ Verification note: HackerOne’s report pages were not reachable through my tools this session. This article’s evidence rests on \~12 specific report numbers — their severities, bounties, upvotes, and quoted details. I could not re-verify any of them this pass; treat every figure tied to a report number as unconfirmed until checked directly. The two CVEs and the RFC were verified independently — see the notes inline and in Sources.*


In 2019, Uber fixed an OAuth bug where the `state` parameter carried a redirect location instead of a CSRF token. Earlier this month, Apache CXF shipped the same design in a framework component whose only job is sign-in — CVE-2026-79650, published October 14, 2026. **Seven years apart, same bug, different scale.**

*💥 Master AI & Tech Skills in 3 Months!*

💰 One Subscription. Multiple Courses. More Savings.

🔥 Get Up to 50% OFF | ⏰ Limited-Time Offer

*👉 Enroll Now & Start Learning*


The question that opens open-redirect threads on r/bugbounty is always some version of *“found an*…
