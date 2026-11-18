# Understanding IDOR (Insecure Direct Object Reference)

- **Source URL:** https://medium.com/@sharmamansi0502/understanding-idor-insecure-direct-object-reference-b99690842319?source=rss------bug_bounty-5
- **Fetched from:** https://medium.com/feed/@sharmamansi0502
- **Fetched:** 2026-11-18
- **Channel:** @dailybountywriteup
- **Telegram message:**  (id 12973)
- **Method:** medium-rss-content readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
### **🔐 Introduction**

While performing security testing, one of the most common and impactful vulnerabilities I come across is Insecure Direct Object Reference (IDOR).

It may look simple, but in real-world applications, IDOR can lead to serious data exposure, privacy violations, and even account takeover.

In this article, I will explain IDOR in a simple and practical way, along with real examples, backend logic, and how to prevent it.

### **🔍 What is IDOR?**

IDOR is a type of Broken Access Control vulnerability where an application exposes internal object identifiers (such as user IDs, order IDs, or file names) and fails to verify whether the current user is authorized to access that resource.

👉 In simple terms:

If changing an ID in a request allows you to access someone else’s data, the application is vulnerable to IDOR.

### **⚠️ Root Cause of IDOR**

The main reason behind IDOR is missing or improper authorization checks on the server side.

Many applications verify whether a user is logged in (authentication), but they fail to verify whether the user is allowed to access a particular resource (authorization).

👉 Important concept:

Authentication tells who you are, while authorization tells what you are allowed to access.

IDOR occurs when authorization is not properly implemented.

### **🧠 How IDOR Works (Simple Example)**

Let’s say an application allows users to view their profile:

GET /api/user/profile?**id=101**

Here, 101 is the user’s ID.

Now, if an attacker changes the ID:

GET /api/user/profile?**id=102**

👉 If the application returns data of another user, it means no authorization check is performed, and the application is vulnerable to IDOR.

Backend Code Example (Vulnerable vs Secure)

### **❌ Vulnerable Code (Python)**

user = db.execute(“SELECT \* FROM users WHERE id = ?”,

(request.args.get(‘id’),))

👉 Problem:

The application directly uses the id from user input

No verification of whether the logged-in user owns that data

### **✅ Secure Code**

user = db.execute(“SELECT \* FROM users WHERE id = ? AND id = ?”,

(request.args.get(‘id’),

session.get(‘user\_id’)))

👉 Fix:

The application verifies whether the requested resource belongs to the logged-in user

If not, access is denied.

### 🔍Where to Look for IDOR

During testing, IDOR is commonly found in:

URL parameters (user\_id, order\_id)

API endpoints

JSON request body

File download links

Hidden form fields

👉 Always look for user-controlled input that references objects.

### ***🧪 How to Test for IDOR (Step-by-Step)***

While performing VAPT, I usually follow this approach:

1. Capture the request using tools like Burp Suite or Postman
2. Identify parameters like user\_id, account\_id, etc.
3. Modify the value to another user’s ID
4. Observe the response

👉 If unauthorized data is returned, the application is vulnerable.

### **⚡ Advanced Testing Techniques**

To find deeper IDOR issues, you can also try:

1. Changing IDs in POST / PUT requests
2. Testing API endpoints directly
3. Using sequential or random values
4. Accessing hidden or unlinked endpoints (force browsing)
5. Testing with different roles (user vs admin)

👉 Most IDOR vulnerabilities require manual testing and logical thinking.

### **💥 Impact of IDOR**

IDOR is often rated as High or Critical severity because it can lead to:

1. Exposure of sensitive data
2. Privacy violations
3. Access to confidential documents
4. Unauthorized actions
5. Account takeover

👉 Even a simple ID change can expose large amounts of data.

### **🔐 Prevention of IDOR**

To prevent IDOR, developers should:

1\. **Implement Proper Authorization Checks**: Always verify whether the user has permission to access the requested resource

2\. **Validate on Server Side**: Never rely on client-side validation

3\. **Use Role-Based Access Control (RBAC)**: Ensure users can only access allowed resources

4\. **Avoid Direct Object References**: Use indirect references (like UUIDs), but do not rely on them completely

5\. **Follow Least Privilege Principle**: Users should only have access to what is necessary.

### **⚠️ Common Mistakes Developers Make**

1. Checking only authentication, not authorization
2. Trusting user input
3. Hiding IDs instead of validating access
4. Relying on frontend restrictions

### **🎯 Interview Questions on IDOR (Basic to Advanced)**

1\. What is IDOR?

**Answer**: IDOR (Insecure Direct Object Reference) is a vulnerability where an application exposes internal object references and fails to verify authorization, allowing users to access unauthorized data.

2\. What is the root cause of IDOR?

**Answer**: The root cause is missing or improper server-side authorization checks.

3\. What is the difference between Authentication and Authorization?

**Answer**: Authentication verifies identity, while authorization determines what actions or resources a user can access.

4\. Is IDOR a part of OWASP Top 10?

**Answer**: Yes, IDOR falls under Broken Access Control, which is ranked #1 in OWASP Top 10 (2021).

5\. What types of data are commonly exposed in IDOR?

**Answer**: User profiles, invoices, order details, documents, and account information.

6\. Can IDOR occur in POST requests or only GET?

**Answer**: IDOR can occur in any HTTP method (GET, POST, PUT, DELETE) wherever user-controlled input is used.

7\. Where do you usually find IDOR vulnerabilities?

**Answer**: In URL parameters, API endpoints, JSON bodies, file downloads, and hidden form fields.

8\. What is Horizontal Privilege Escalation?

**Answer**: Accessing another user’s data at the same privilege level.

9\. What is Vertical Privilege Escalation?

**Answer**: Accessing resources or functionality meant for higher privilege users (e.g., admin access).

10\. How do you test for IDOR?

**Answer**: By modifying object identifiers in requests and checking if unauthorized data is accessible.

11\. Which tools can be used to test IDOR?

**Answer**: Burp Suite, Postman, browser developer tools, and manual testing techniques.

12\. Can IDOR be detected by automated scanners?

**Answer**: Most IDOR vulnerabilities require manual testing as they depend on business logic.

13\. Is hiding IDs (like using UUIDs) enough to prevent IDOR?

**Answer**: No, UUIDs only make guessing difficult. Proper authorization checks are still required.

14\. Why is IDOR considered a business logic vulnerability?

**Answer**: Because it arises from improper implementation of access control rules, not from technical misconfigurations.

15\. Can IDOR occur in APIs?

**Answer**: Yes, APIs are one of the most common areas where IDOR vulnerabilities exist.

16\. What is the difference between IDOR and Forced Browsing?

**Answer**: IDOR involves manipulating object references, while forced browsing involves accessing unlinked or hidden endpoints.

17\. How can IDOR lead to account takeover?

**Answer**: If sensitive operations like password reset or profile modification are exposed, an attacker can manipulate them to take over accounts.

18\. What is Mass Assignment and how is it related to IDOR?

**Answer**: Mass assignment allows users to modify unintended parameters, which can lead to IDOR if authorization is not properly enforced.

19\. Where should authorization checks be implemented?

Answer: Authorization checks must always be implemented on the server side, not on the client side.

20\. What is the best way to prevent IDOR?

**Answer**: Implement strict server-side authorization, use RBAC, validate user access, and follow the principle of least privilege.

### **🧾 Conclusion**

IDOR is one of the simplest yet most impactful vulnerabilities in web applications.

It mainly occurs due to missing authorization checks, not because IDs are visible.

From a security tester’s perspective, finding IDOR requires understanding application logic rather than relying on automated tools.

👉 Always remember:

Never trust user input and always enforce authorization on the server side.

### **🚀 Final Note**

As part of my learning journey, I’m exploring one vulnerability every day and documenting it to strengthen my understanding of application security.

Byee….until next time..😊
