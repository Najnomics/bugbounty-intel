# 1000$ IDOR

- **Source URL:** https://medium.com/@a13h1/1000-idor-unauthorized-project-inclusion-in-expense-b9ce08b28c71?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20240721100351/https://medium.com/@a13h1/1000-idor-unauthorized-project-inclusion-in-expense-b9ce08b28c71
- **Fetched:** 2026-11-23
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/6738 (id 6738)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# 1000$ IDOR : Unauthorized Project Inclusion in Expense

Hi Everyone! Today, I’m excited to talk about a critical vulnerability I discovered in a platform (let’s call it ExamFit), which allowed users to bypass project status restrictions and submit unauthorized expense reports. Join me as we explore how this flaw was identified and its implications.

**Understanding ExamFit:**


ExamFit is a robust expense management system designed to ensure accuracy and compliance with organizational policies. It serves as a centralized hub where organizations manage their financial transactions and monitor project expenses securely.

**The Flaw :**


In examfit if admin restrict/disable a project, no user can be able to submit an expense report through that project. Despite stringent project status controls set by administrators, a vulnerability was found that allows users to manipulate API requests. By using a specific POST request to /hr/expenses/submission/submit, users can include disabled project IDs in the projectId parameter. This oversight enables the creation of expense reports associated with projects that should be inaccessible.

## **Steps to Reproduce:**

- **Access ExamFit Platform:** Log in with a standard user account.
- **Use the POST Request:** Send a POST request to /hr/expenses/submission/submit, including the disabled project ID in the projectId parameter.

```
POST /hr/expenses/submission/submit HTTP/2 
Host: api.examfit.com 
Content-Type: application/json 
Authorization: Bearer [your_token_here]  
{     "fileIds": ["660ecac2e469dd1094a3ed50"],     "name": "test",     "type": "food",     "projectId": "651ac823c634d37bac8aa6b6", // Include disabled project ID here     "price": 50,     "date": "09/04/2024",     "message": "vff",     "isClientMeal": 0,     "externalGuests": [],     "taxes": [] }
```
- **Submit the Request:** Observe how the project status restriction is bypassed.
- **Verification:** Check from an admin account if the disabled project appears in the expense report.

**Impact:**


This vulnerability compromises the integrity of expense management within ExamFit. Attackers could exploit this flaw to submit fraudulent expense reports tied to disabled projects, leading to financial inaccuracies, compliance breaches, and erosion of trust within the organization.

**Response and Resolution:**


Upon reporting, ExamFit promptly acknowledged the severity of the issue and initiated corrective measures. The vulnerability was reassessed as high severity due to its potential impact on financial controls and organizational trust. As a token of appreciation for responsible disclosure, ExamFit awarded a bounty of $1,000 for uncovering this critical security flaw.

**Takeaway:**


Thorough testing, including manipulation of API requests and testing for IDOR vulnerabilities, is crucial in identifying and mitigating risks. By actively searching for and reporting such vulnerabilities, security researchers play a vital role in safeguarding organizational assets and maintaining user trust.

**Support and Follow:**


If you found this write-up insightful, please leave a clap and share your feedback in the comments. Follow me for more exciting findings and cybersecurity tips!

Find me on Twitter: @a13h1\_

**Thank you for your continued support. Keep clapping, commenting, and sharing your thoughts!**
