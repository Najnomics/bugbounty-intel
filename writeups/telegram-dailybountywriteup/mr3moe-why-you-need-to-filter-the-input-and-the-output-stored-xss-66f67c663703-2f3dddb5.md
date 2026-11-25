# why you need to filter the input and the output —  stored xss

- **Source URL:** https://medium.com/@Mr3Moe/why-you-need-to-filter-the-input-and-the-output-stored-xss-66f67c663703?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20240105163424/https://medium.com/@Mr3Moe/why-you-need-to-filter-the-input-and-the-output-stored-xss-66f67c663703?source=rss------bug_bounty-5
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/4748 (id 4748)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
**Introduction**

**XSS** is one of the most common types of vulnerabilities that bug hunters look for. This is because most of the time when you fuzz or inject an XSS payload into forms and/or parameters, you will see the payload firing if the parameters or forms do not validate the input correctly.

On the other hand, it can be very challenging to determine if a parameter or form is not vulnerable to XSS due to the limitations of the results we obtain after injecting our payload. So, let’s dive into the details of my findings in one of the Bugcrowd’s programs.

**Finding Stored XSS**

I was invited to one of Bugcrowd’s programs. The program was quite old, and there were already hunters who had completed testing on it. So, I started looking for endpoints that other hunters had not discovered to avoid duplicates. I stumbled upon page allows you to upload plugins and the page has many form inputs including name , description , image and more .. I tried to inject simple html payload like **”>\<h1>hey\</h1>** to each fields to test the result.

NOTE : Always start with a simple HTML payload and monitor the results because some applications use custom XSS filters that are based on regex to filter only javascript related payloads like **\<script>alert(1)\</script>** and if the HTML injection works you must start looking for pattren to bypass that filter to get javascript payload working because HTML injection consider as low Finding.


So, after I inject my payload into all fields and click on **save** , I get redirected to the plugin’s main page, and my payload gets filtered.

so from this , I assumed that none of these fields were vulnerable to an XSS attack, but I kept digging deeper to see if my payload gets reflected on a different page since my payload was stored in the database. After moving around , I was able to find a page called **User** responsible for managing users and each user you can assign to them plugins to manage .

so I in **User** page I clicked on one of the users and then I clicked on **assign plugins** then the request was made by ajax to request all available plugins by names and here when I found my html payload got reflected when I search for first letter which was **h** , Here ‘s the scenario.

**POC**

1 — go to plugins page and click on add plugin .

2 — in the name field insert your **javascript** payload for example “**>\<script>alert(1)\</script>** and click save.

3 — go to users page and click on any user and then click on assign plugin .

4 — type **“** or click on **spacebar** to display all plugins you will notice the alert function will pop up with alert 1 .
