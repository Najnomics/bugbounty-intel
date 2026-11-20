# IDOR(Insecure Direct Object Reference) Price Manipulation on Private Bug Bounty Program

- **Source URL:** https://medium.com/@bry4nzheng/idor-insecure-direct-object-reference-price-manipulation-on-private-bug-bounty-program-2527431ffcfd?source=rss------bug_bounty-5
- **Fetched from:** https://medium.com/feed/@bry4nzheng
- **Fetched:** 2026-11-20
- **Channel:** @dailybountywriteup
- **Telegram message:**  (id 5263)
- **Method:** medium-rss-content readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
**Introduction:** During my participation in a private bug bounty program, I uncovered a significant security flaw within the system. This vulnerability, known as a Business Logic Flaw, could potentially lead to unauthorized access and manipulation of sensitive data.

**Discovery:** While conducting routine testing on the platform, I stumbled upon a peculiar behavior during the checkout process. Upon further investigation, I observed that it was possible to manipulate the quantity field for items in the shopping cart. Curiously, by entering a negative value for the quantity, I discovered that it resulted in a deduction from the total checkout amount.

**Exploitation:** I crafted a series of requests aimed at manipulating the checkout process. By intercepting and modifying the quantity parameter in the checkout request, I was able to deduct the total amount to zero dollars.

Firstly, I used a tool called Burp Suite to intercept and analyze the traffic between my browser and the server while going through the checkout process. I wanted to see how the application handles the quantity of items in the shopping cart.

When I added items to the cart and proceeded to checkout, I noticed that the quantity parameter was being passed along with each item. Curiously, I decided to tamper with this parameter by entering a negative value instead of the usual positive ones.

Surprisingly, the server accepted the negative quantity without any issue. This immediately caught my attention because it meant I could potentially manipulate the checkout total by subtracting from it instead of adding to it.

To confirm this suspicion, I experimented with different combinations of items and quantities.

By strategically adjusting the quantities, I was able to bring the total checkout amount down to $0. It was like a mathematical puzzle, trying to balance the quantities of items to achieve that zero total.

**Recommendations for Mitigation:** To address this vulnerability and prevent potential exploitation, I recommend implementing the following measures:

1. Input Validation: Implement strict input validation mechanisms to ensure that only valid and authorized values are accepted for quantity parameters during checkout.
2. Transaction Integrity Checks: Implement integrity checks and validation mechanisms to ensure the consistency and accuracy of transactional data, thereby mitigating the risk of manipulation or tampering.
