# Coinbase Bug Bounty

- **Source URL:** https://masimshahzad.medium.com/coinbase-bug-bounty-selling-crypto-you-never-owned-9ba96a3f97e0
- **Fetched from:** https://masimshahzad.medium.com/feed
- **Fetched:** 2026-11-24
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14997 (id 14997)
- **Method:** medium-rss-content readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
### Coinbase’s largest-ever bounty, $250,000: a trading API checked that you had a balance, never which asset that balance was in

*AI-assisted: drafted with AI help from public sources, then reviewed and edited. This is an analytical case study of a public disclosure, not my own discovery.*

The biggest Coinbase bug bounty ever paid was not for an RCE. It was for one missing comparison. In February 2022, a trader known as Tree of Alpha found Coinbase’s Retail Advanced Trading API let a user sell an asset they did not hold, on a live order book. Coinbase patched it the same afternoon and paid $250,000.

***Disclaimer:*** *Educational and defensive use only. This was fixed on 11 February 2022. Reproduction details are intentionally omitted.*

### Vulnerability Overview

- **Type:** Business logic flaw: an order’s product and source account were never checked against each other
- **CWE (analytical mapping, not from the source):** CWE-20 (Improper Input Validation), CWE-840 (Business Logic Errors)
- **CVE:** None (hosted service)
- **Severity/Bounty:** Severity rating not reported. Bounty: $250,000, confirmed by Coinbase as its largest ever

### How the Coinbase Bug Bounty Flaw Worked (high level)

An order request carried three client choices: the product (an order book such as BTC-USD), the account the funds come from, and the account the proceeds go to. The UI kept them consistent; the backend never checked.

The validation service asked one question: does the source account hold enough for this order? It never asked the second: is the source account in the asset this order book trades? A user holding a cheap token and zero bitcoin could place a bitcoin sell order, name the token wallet as the source, and the balance check would read the wrong number and pass.

### Business Impact

An attacker could push sell orders for assets they did not own into a real market. Coinbase cites limits: a limited-beta platform, price-protection circuit breakers and trade surveillance. It states the flaw was never maliciously exploited.

The researcher’s first move was a public tweet asking for a security contact. Within about 90 minutes Coinbase had reproduced it and set the platform to cancel-only mode; a patch shipped by 4:01 PM PST.

### Fixing Coinbase-Style Business Logic Bugs (my own analysis)

**1. Validate relationships, not just fields.** Each ID can be valid on its own and still be wrong together.

**2. Reserve, don’t read.** An atomic hold on the exact asset being spent beats a balance read followed by a trade.

**3. Keep a kill switch.** Cancel-only mode turned a market risk into hours of downtime.

\# Pseudocode: every account in an order must match the product it trades

def validate\_order(session, order):

product = PRODUCTS.get(order.product\_id) # e.g. base="BTC", quote="USD"

src = accounts.get(order.source\_account\_id)

dst = accounts.get(order.target\_account\_id)

if product is None or src is None or dst is None:

return reject("invalid\_order")

if src.owner != session.user\_id or dst.owner != session.user\_id:

return reject("invalid\_order") # same answer for missing or foreign

if order.side == "sell":

spend, receive = product.base, product.quote

else:

spend, receive = product.quote, product.base

if src.asset != spend or dst.asset != receive:

return reject("account\_product\_mismatch") # the check that was missing

if not ledger.reserve(src.id, spend, order.max\_spend()): # atomic hold

return reject("insufficient\_funds")

return accept(order)

# Test: BTC-USD sell with a SHIB source -> account\_product\_mismatch, no hold created

### Key Takeaways

- A balance check that reads the wrong account is not a balance check.
- UI consistency is not a security control.
- Publish an easy-to-find security contact.

### Credit & Sources

Found by **Tree of Alpha** (pseudonymous; credited by Coinbase as Tree\_of\_alpha). Primary source: Coinbase’s [Retrospective: Recent Coinbase Bug Bounty Award](https://www.coinbase.com/blog/retrospective-recent-coinbase-bug-bounty-award) (18 February 2022): timeline, root cause and bounty. Researcher credit: Coinbase’s [10-year bug bounty post](https://www.coinbase.com/blog/celebrating-10-years-of-our-bug-bounty-program). Facts come from those sources; analysis and code are original.

Next breakdown: another real bug bounty case. Follow @masimshahzad for daily bug bounty breakdowns.
