# Discovering and Reporting SQL Injection

- **Source URL:** https://medium.com/@mjoker22mjoker22/discovering-and-reporting-sql-injection-a-technical-walkthrough-of-can-2026-2040978-f3d52aabcdb1
- **Fetched from:** https://medium.com/@mjoker22mjoker22/discovering-and-reporting-sql-injection-a-technical-walkthrough-of-can-2026-2040978-f3d52aabcdb1?source=rss-b71ce75f56b3------2
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:**  (id 14962)
- **Method:** medium-rss-feed (full content:encoded) readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- **Author/Published (RSS):** Mahdi Karimi / Tue, 27 Oct 2026 21:40:33 GMT

Author: Mahdi Karimi

Date: October 28, 2026

Vulnerability Type: SQL Injection (CWE-89)

Affected Target: Lower Niger River Basin Development Authority Web Portal (lnrbda.gov.ng)

Tracking ID: CAN-2026–2040978 (Pending CVE Publication)

Introduction

Web application security remains one of the most critical challenges for public and private organizations alike. Even a minor oversight in handling user input can lead to severe data breaches. In this write-up, I will walk through the discovery of a SQL Injection (SQLi) vulnerability on a public sector web portal (lnrbda.gov.ng), how it was verified, and the responsible disclosure process — including reserving an official tracking identifier (CAN-2026–2040978) via MITRE CNA-LR.

1\. Reconnaissance and Discovery

While analyzing public web assets, my attention was drawn to the news reading section of the portal, which utilized a dynamic GET parameter to fetch records from the database:

[http://www.lnrbda.gov.ng/readnews.php?id=1](http://www.lnrbda.gov.ng/readnews.php?id=1)

In web applications, parameters directly interacting with database queries without proper sanitization or parameterization are prime candidates for SQL Injection. To test for anomalies, I introduced basic error-inducing characters (such as single quotes ‘) into the id parameter. The application exhibited behavioral shifts, indicating that user input was being concatenated directly into backend SQL queries without adequate filtering.

2\. Technical Analysis & Verification

Because the application did not directly output database error messages or query results onto the web page, standard error-based SQLi was ineffective. Instead, the vulnerability manifested as Blind SQL Injection, requiring inferential testing methods:

1. Boolean-based Blind: Injecting logical conditions to observe whether the page returned true or false states (e.g., verifying if the content altered based on AND 3792=3792).

2. Time-based Blind: Forcing the database engine to pause execution (SLEEP(5)) to measure response delays.

Automated Verification via SQLMap:

python sqlmap -u “[http://www.lnrbda.gov.ng/readnews.php?id=1](http://www.lnrbda.gov.ng/readnews.php?id=1)" — level=5 — risk=3 — tamper=space2comment — random-agent — batch

Results confirmed:

- Parameter: id (GET)

- Vulnerability Types Identified:

\* Boolean-based blind (WHERE or HAVING clause evaluation)

\* Time-based blind (MySQL >= 5.0.12 query delay execution)

3\. Impact Assessment

An unauthenticated remote attacker exploiting this vulnerability could:

- Extract sensitive administrative records and internal database tables.

- Read backend database structures and schema names.

- Potentially compromise the confidentiality and integrity of the web server’s underlying data storage.

4\. Responsible Disclosure & CVE Request Process

Security research is incomplete without responsible disclosure and proper tracking. To ensure transparency:

1. Advisory Formulation: I structured a complete proof-of-concept (PoC) and technical advisory.

2. CNA-LR Engagement: Since the target organization did not have a dedicated CVE Numbering Authority (CNA), I routed the case through the MITRE CNA-LR (CNA of Last Resort) portal.

3. Tracking Assignment: Following official guidelines on cve.org, I successfully reserved tracking ID CAN-2026–2040978 for official review and CVE ID issuance.

5\. Remediation & Fix

The root cause of SQL Injection is the direct concatenation of untrusted user input into database queries. To remediate this issue, developers must adopt Prepared Statements and Parameterized Queries (such as PDO in PHP).

Vulnerable pattern (Conceptual):

$id = $\_GET\[‘id’\];

$query = “SELECT \* FROM news WHERE id = “ . $id;

Secure pattern (Remediation):

$stmt = $pdo->prepare(‘SELECT \* FROM news WHERE id = :id’);

$stmt->execute(\[‘id’ => $\_GET\[‘id’\]\]);

$newsItem = $stmt->fetch();

Conclusion

This discovery highlights the importance of rigorous input validation and secure coding practices in web applications, particularly on public-facing portals. By adhering to responsible disclosure and engaging with the global vulnerability tracking ecosystem (MITRE), researchers can help secure the digital infrastructure while contributing to the community knowledge base.
