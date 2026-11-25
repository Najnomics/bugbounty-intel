# From Shodan to an Unpaid Delivery

- **Source URL:** https://medium.com/@gjethva10/from-shodan-to-an-unpaid-delivery-how-a-chain-of-weaknesses-led-to-real-world-impact-266a4ef00b1e
- **Fetched from:** https://medium.com/@gjethva10/from-shodan-to-an-unpaid-delivery-how-a-chain-of-weaknesses-led-to-real-world-impact-266a4ef00b1e?source=rss-31b7314240b4------2
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14965 (id 14965)
- **Method:** medium-rss-feed (full content:encoded) readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- **Author/Published (RSS):** Gaurang Jethva / Fri, 30 Oct 2026 18:38:15 GMT

One discovery can uncover more than you initially expect.

This investigation started with Shodan and ended with a real physical product being delivered without genuine payment being collected.

While enumerating the external attack surface of a target, I discovered an IP address associated with its domain. Opening it directly in a browser revealed a fully functional application that appeared identical to the website accessible through the target’s domain.

The application relied on OTP-based authentication, but a predictable value, 1234, was accepted, allowing access.

Exploring the application hosted on IP address revealed several sections, including an e-commerce section that redirected to a separate retail UAT environment. There, I encountered the same authentication mechanism, and the same predictable OTP worked again.

What initially appeared to be a weakness in one application had now led to another environment.

This was where I handed over the investigation to my teammate, **Vijay Sawant**, who continued exploring the retail application’s functionality beyond the initial discovery and authentication bypass.

He examined the ordering and payment workflow. The store offered several payment options, including one associated with the company’s own payment mechanism.

Selecting that option opened a page branded as a Razorpay Private Limited bank interface. Interestingly, the page explicitly described itself as a demo bank and allowed the transaction to be marked successful or unsuccessful.

The important question was what the store would do with that result.

A payment page displaying a success message does not prove that money has actually been transferred. The merchant’s backend must independently verify the transaction before treating an order as paid.

In this case, after the transaction was marked successful, the store itself displayed the order as paid.

The order could then be tracked through the store and Delhivery.

Eventually, a real physical product was delivered despite no genuine payment being collected.

**The investigation had moved from an authentication weakness to a tangible business impact.**

One thing this investigation reinforced was the value of collaboration during security assessments.

My initial work uncovered the externally accessible application, the authentication weakness, and the route into the retail UAT environment. Handing those findings over to Vijay allowed the investigation to progress further into the e-commerce workflow and establish the wider business impact.

Security assessments rarely depend on a single discovery. One person may identify an entry point, while another brings a different perspective, investigates the downstream functionality, and connects the technical weakness to its business consequences.

Sharing findings, communicating context clearly, and building on each other’s work can reveal risks that might otherwise remain undiscovered.

Shoutout to **Vijay Sawant** for carrying the investigation forward and helping connect the initial findings to their real-world impact.

*Disclosure note:* No proof-of-concept (PoC), screenshots, or sensitive technical evidence have been shared as part of this publication.
