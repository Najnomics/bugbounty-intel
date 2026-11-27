# Race Condition on Likes of Product Leads to Products can appear more popular

- **Source URL:** https://medium.com/@omdubey170/race-condition-on-likes-of-product-leads-to-products-can-appear-more-popular-a39038d16203?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20240904041818/https://medium.com/@omdubey170/race-condition-on-likes-of-product-leads-to-products-can-appear-more-popular-a39038d16203
- **Fetched:** 2026-11-27
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/7042 (id 7042)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Race Condition on Likes of Product Leads to Products can appear more popular

In my recent bug bounty activities, I stumbled upon a significant race condition vulnerability in a popular e-commerce platform. This vulnerability, when exploited, can seriously impact the integrity of product favorite counts and user trust. Here’s a detailed breakdown of the issue and its implications.

# Description:

The vulnerability I discovered involves a race condition in the way the platform handles product favorites. A race condition occurs when multiple processes or threads access shared resources concurrently, leading to unpredictable results. In this case, the favorite count of a product can be manipulated through repeated requests, thanks to dynamic caching.

# Steps to Reproduce:

**Account Creation:**

Create an account on the platform and navigate to any product page. For instance, \[this product page\](https://www.example.com/listings/\*\*\*-wear-x-tommy-hilfiger) initially shows 0 favorites.

**Adding to Favorites:**

Click on the heart icon to add the product to your favorites. The count should increase.

**Capturing the Request:**

Use Burp Suite to capture the HTTP request when you add the product to favorites and send it to Repeater.

**Replicating the Request:**

Copy the captured request as a cURL command and create a bash script that repeats this command multiple times.

**Running the Script:**

Execute the bash script to send multiple requests, significantly increasing the favorites count.

**Observations:**

Due to dynamic caching, the favorites count is visible for a specific time. By hosting the script on a VPS and running it continuously, I was able to keep increasing the favorites count, exploiting the race condition.

Receiving a Small Bounty but OKK

# Impact of the Vulnerability

**Artificially Inflated Favorites:**

Products can appear more popular than they are, misleading potential buyers into thinking they are more desirable.

**Loss of User Trust:**

Users may question the accuracy of the favorites count, leading to a loss of confidence in the platform’s reliability.

**Data Integrity Issues:**

Manipulated favorite counts can skew the platform’s analytics and reporting, affecting business decisions.

**Potential Denial-of-Service (DoS):**

Continuous manipulation of favorites can overwhelm the system, potentially causing performance issues or downtime for legitimate users.
