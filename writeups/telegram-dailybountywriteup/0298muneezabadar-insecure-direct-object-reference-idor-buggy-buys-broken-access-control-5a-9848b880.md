# Insecure Direct Object Reference (IDOR)

- **Source URL:** https://medium.com/@0298muneezabadar/insecure-direct-object-reference-idor-buggy-buys-broken-access-control-5a59bba49610?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250801130919/https://medium.com/@0298muneezabadar/insecure-direct-object-reference-idor-buggy-buys-broken-access-control-5a59bba49610?source=rss------bug_bounty-5
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/10381 (id 10381)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Insecure Direct Object Reference (IDOR): Buggy Buy’s Broken Access Control

Insecure Direct Object Reference (IDOR) vulnerabilities are found in many modern web applications. This vulnerability fails to properly validate whether the person is authorized or not, due to this it can expose many internal objects such as files, database records, or User IDs.

In this post, we will perform two walkthroughs to understand IDOR more clearly by the help of Buggy Buy.

Buggy Buy is a purposely vulnerable e-commerce platform that simulates real-world scenarios for security testing.

*Requirements:*

- Buggy Buy: [https://vulnerable-web-application-jecw.vercel.app/login](https://web.archive.org/web/20250801130919/https://vulnerable-web-application-jecw.vercel.app/login)
- Burp Suite.
- Read: [Forced Browsing](https://web.archive.org/web/20250801130919/https://medium.com/@0298muneezabadar/c926153504d4)

**Walkthrough: Accessing Order Summary**

In this walkthrough, we will access another user’s Order details;

**Steps # 1: Place Order**

- Login as user.
- Navigate to Product page.
- Choose the item and add to the cart.
- Go to the cart and proceed to checkout.
- Fill out the shipping details.
- Then continue and Place Order.
- You’ll get the Order Summary.

**Step # 2: Manipulate the URL.**

- Replace the Order ID (Order IDs you got by [Forced Browsing](https://web.archive.org/web/20250801130919/https://medium.com/@0298muneezabadar/c926153504d4)).
- I’m using User999's Order ID: 688b33044a95d9049590317b

- This URL will return the User999’s Order Details.

The another way to get Order Details is;

By Tracking the Order.

**Step # 1: Navigate to Track Order.**

- Under User drop down menu you can find “Track Order”.

**Step # 2: Track User999’s Order**

- Enter User999’s Order ID found by [forced browsing](https://web.archive.org/web/20250801130919/https://medium.com/@0298muneezabadar/c926153504d4).

- Hit “View Order Details”.

This is how you can view anothers user order details, which is a critical vulnerability because it is disclosing users personal details like email and address.

**Walkthrough: Deleting User Account without Admin Privileges**

In this walkthrough, As a user we will delete another user account;

**Step # 1: Start Burp Suite and Enable Intercept**

- Open Burp Suite and go to the Proxy tab.
- Make sure Intercept is ON.

**Step # 2: Login as User**

- Navigate to Buggy Buy’s user login page.
- Login as a user.

- Hit “Sign In”.
- You’ll see the captured request on Burp Suite.

**Step # 2: Manipulate Endpoint**

- In Burp, right-click the request → Send to repeater.
- You’ll see the endpoint.

- Manipulate this endpoint.

“688b4fb3ae737905ed9d8d80" is the User ID of User: User02 obtained by the [Forced Browsing](https://web.archive.org/web/20250801130919/https://medium.com/@0298muneezabadar/c926153504d4).

**Step # 3: Delete the User**

- Hit “Send”.
- The User will be deleted successfully.

**Step # 4: Verification**

- Check if the user deleted or not.
- Login as User02, use email and password obtain by forced browsing.

**Impact**

- **Unauthorized Access to Sensitive Information**: Attackers can access other users’ order details, including personal data such as names, emails, and shipping addresses.
- **Account Manipulation**: Users can delete other user accounts without any administrative privileges.
- **Privacy Violation**: Unauthorized viewing and tampering of user data violates user confidentiality.
- **Business Risk**: These flaws can lead to customer trust issues, legal implications (e.g., GDPR violations), and financial losses if exploited at scale.

**Prevention**

1. **Implement Object-Level Authorization Checks**
Always verify that the requesting user owns or has permission to access the resource (e.g., order, user profile).
2. **Never Rely on Client-Side Data Alone**
Validate all IDs and references on the server side, regardless of what the front end sends.
3. **Use Secure Session Contexts**
Determine the target resource based on authenticated session info, not from user-supplied parameters.
4. **Monitor for Enumeration Pattern**s
Detect and rate-limit repeated attempts to access different IDs or resources.
5. **Apply Role-Based Access Control (RBAC)**
Ensure only users with appropriate roles (e.g., admin) can perform sensitive operations like account deletion.

**Conclusion:**

This walkthrough highlights how simple IDOR vulnerabilities in seemingly harmless features (like order tracking or user management) can lead to critical security issues. Through forced browsing and lack of proper authorization, attackers can expose sensitive user information or even delete accounts without admin rights.

Buggy Buy serves as a perfect example of why object-level access control is essential, every request must be treated as potentially untrusted and validated accordingly.

**IDOR may look simple, but its impact can be massive.**


Stay secure, test deeply, and never trust user input blindly.

This post is for educational purposes only. All testing was performed in a legal, controlled environment.


**WEB APPLICATION PENETRATION TESTING:**
