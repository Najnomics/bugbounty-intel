# From “Website Not Accessible” to Critical Error-Based SQLi

- **Source URL:** https://medium.com/@chos3n/from-website-not-accessible-to-critical-error-based-sqli-483cda463a10?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20251230190717/https://medium.com/@chos3n/from-website-not-accessible-to-critical-error-based-sqli-483cda463a10
- **Fetched:** 2026-11-19
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/12206 (id 12206)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# From “Website Not Accessible” to Critical Error-Based SQLi

Most bug hunters skip domains that look locked down or inactive. This vulnerability came from doing the opposite.

**First Impression**: “Website Not Accessible”

No UI. No links. No functionality. At face value, the domain looked completely inaccessible and safe to ignore.That restriction, however, applied only to the **frontend**.

## Technology Fingerprinting

Using basic technology analysis, the backend stack was identified as:

IIS 10.0

ASP.NET

ColdFusion (CFML)Windows Server

A legacy Windows + ColdFusion stack is often a strong signal for forgotten endpoints.

**Initial Testing**: Short Name Enumeration

Given the IIS + ColdFusion stack, my first thought was **IIS short name (8.3) enumeration**. I tested for short-name disclosure, but it didn’t reveal anything useful. No valid hits, no interesting behavior.At this point, there was no obvious vulnerability — but I continued probing.

Random Path Testing Reveals Internal Information “target.com/aaa” looks interesting yeah.

That was the first sign that the domain, although restricted at the frontend, **might still be vulnerable underneath**.

**Turning Point**: Web Archive Recon

Using web archive sources, I enumerated historical URLs associated with the domain.This led me to a **JavaScript file**, which became the turning point of the investigation.Inside the JS file, I found references to **three backend endpoints**.

One of them immediately stood out:

## Testing the ColdFusion Endpoint

The `/websnips/getItemImages.cfm` endpoint was still live and responded with JSON data containing image paths.While this endpoint did leak internal image locations, it didn’t expose anything sensitive or exploitable on its own. Still, it confirmed:

- The `/websnips/` directory existed
- ColdFusion endpoints were reachable
- Legacy backend code was active

This made the directory a strong candidate for further testing.

### **Directory Fuzzing Leads to a Hidden Endpoint**

That’s when I discovered another endpoint:

`/websnips/vstats.cfm`
Accessing it returned an **HTTP 500 error** with a ColdFusion error page.

The error message stated:

`key [NAME] doesn't exist`
This immediately revealed that the endpoint expected a parameter named `name`.

## Parameter Injection Triggers Database Errors

I added the missing parameter:

`/websnips/vstats.cfm?name=aaa`
This time, the response changed again — now returning a **database error**:

`Invalid column name 'aaa'`
Even worse, the application disclosed the **full SQL query** being executed.

## Final Confirmation: Error-Based SQL Injection

To fully confirm exploitability, I tested a classic error-based SQL injection payload:

`/websnips/vstats.cfm?name=CAST((SELECT @@version) AS INT)`
The database responded with a conversion error that leaked the **full database version information**, confirming a **fully exploitable error-based SQL injection**.

*That’s it guys . Thanks for taking the time to read — I hope this write-up was useful and insightful.*


feel free to contact me : [https://x.com/Peet28385834](https://x.com/Peet28385834)
