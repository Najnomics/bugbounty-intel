# Hacker101 CTF

- **Source URL:** https://medium.com/@YusifMammadzada/hacker101-ctf-osusec-school-of-pwn-write-up-f62bbc309408
- **Fetched from:** https://yusifmammadzada.medium.com/hacker101-ctf-osusec-school-of-pwn-write-up-f62bbc309408?source=rss-5e81e99b760d------2
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14963 (id 14963)
- **Method:** medium-rss-feed (full content:encoded) readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- **Author/Published (RSS):** Yusif Mammadzada / Wed, 28 Oct 2026 18:52:53 GMT

In this write-up, we will explore the step-by-step exploitation of the **OSUSEC (School of Pwn)** challenge on the Hacker101 CTF platform. This challenge simulates a real-world scenario involving multiple web vulnerabilities, specifically **SQL Injection (SQLi)**, **Client-Side Privilege Escalation**, and **Insecure Direct Object Reference (IDOR)** coupled with weak encoding.

Step 1: Bypassing Authentication via SQL Injection

The target application presents a standard login interface at the /login endpoint. To test for authentication bypass vulnerabilities, a classic SQL Injection payload was injected into the username field:

Due to a lack of proper input sanitization and parameterized queries on the backend database execution, the logical condition evaluated to true. The application successfully bypassed the authentication mechanism and granted access to the internal dashboard.

Step 2: Dashboard Analysis and Restrictions

Upon successful authentication, the application redirects to the /dashboard endpoint, logging us in under a staff account (rhonda.daniels). The dashboard displays a "Your Students" table containing student names and their respective academic grades. However, at this stage, the student records are rendered as static text with no interactive components or editing capabilities.

Step 3: Client-Side Privilege Escalation via Browser Console

To inspect the underlying application logic and look for hidden features, the browser’s **Developer Tools (F12) -> Console** was utilized. Examination of the client-side JavaScript source revealed that authorization checks are handled poorly on the client side.

By executing the following commands directly in the console, the user’s privilege state was manipulated to simulate an administrator session, and the interface elements were dynamically updated:

javascript

staff.admin = true;

setupLinks();

Immediately after executing these functions, the static student names within the table were converted into clickable hyperlinks, indicating that administrative capabilities had been unlocked.

Step 4: Parameter Analysis & Base64 Decoding

Clicking on a student record (e.g., *Brett, Nancie*) redirects the browser to a record modification endpoint with the following URL structure:

.../update-student/TmFuY2llX0JyZXR0

The alphanumeric string TmFuY2llX0JyZXR0 at the end of the URL exhibits the structural characteristics of **Base64** encoding. Utilizing **CyberChef** with the **"From Base64"** operation confirmed this hypothesis. The decoded output revealed the raw parameter format: Nancie\_Brett (the student's first and last name separated by an underscore).

Step 5: IDOR Exploitation and Flag Retrieval

The reliance on predictable, client-controlled encoding for object referencing confirms a critical **Insecure Direct Object Reference (IDOR)** vulnerability. An attacker can manipulate this parameter to access or modify records belonging to any user in the database.

To target the required profile (e.g., the target user Natasha\_Drew), the name was encoded using the **"To Base64"** operation in CyberChef, resulting in the following payload:

Replacing the original Base64 string in the URL with this generated payload and reloading the page successfully loaded the grade modification form for the target student. Submitting a modified grade by clicking **“Update Record”** triggered the backend validation and successfully rendered the hidden **Flag**.

The OSUSEC challenge highlights the critical necessity of defense-in-depth. Security controls must never rely exclusively on client-side state manipulation (such as JavaScript flags), and sensitive object parameters must be securely validated on the server side to prevent authentication bypass and unauthorized data modification.

Break the system, catch the flag. Happy Hacking! 🚩
