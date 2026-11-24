# 1.4M PII data leakage (IDOR)

- **Source URL:** https://medium.com/@tusharaj98355/1-4m-pii-data-leakage-idor-aee596aef4d9?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20240211161255/https://medium.com/@tusharaj98355/1-4m-pii-data-leakage-idor-aee596aef4d9
- **Fetched:** 2026-11-24
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/5168 (id 5168)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# 1.4M PII data leakage (IDOR)

--

The year 2024 began with a bang. I was hunting on my favourite private bug bounty program on H1, I had tested almost all the functionalities of the web app. Although this is a managed program by H1, the company staff never miss my reports and triage them themselves (Pro tip: build good relationship with the programs and platform).

After extensive searching, I stumbled upon a new functionality:

The API call to update the checklist resembled like this:

Flow to update the document:

Doc uploaded to FileStack->URL generated (https://cdn.redacted.com/(random alphanumeric digits)-> redacted.com assigned a numeric ID to this Doc.


There is no misconfiguration here and probably it is a secure way to upload files but I observed the DocURL was being reflected in the reponse page:

There were many ID’s present here but one starting with 147… seemed interesting because this was being reflected at the response with the “fileSrc” parameter.

Changing the DocID parameter changed the “fileSrc” URL:

From this URL, I was able to find someone else’s Cardiovascular Health report:

I had access to almost all the Documents present(roughly 1.4 million records).

## **Tip:**

Always use Auth Analyzer or any other tool to automate finding these type of vulnerabilties, they are easy to use and very helpful.

*I reported it to the program and it was triaged after 3 days because I submitted it on Friday night.*

Thanks for reading.
