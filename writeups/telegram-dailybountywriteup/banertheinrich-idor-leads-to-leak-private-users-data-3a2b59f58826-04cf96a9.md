# IDOR leads to leak private user’s data

- **Source URL:** https://medium.com/@banertheinrich/idor-leads-to-leak-private-users-data-3a2b59f58826?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20241211144828/https://medium.com/@banertheinrich/idor-leads-to-leak-private-users-data-3a2b59f58826
- **Fetched:** 2026-11-23
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/8147 (id 8147)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# IDOR leads to leak private user’s data

**Introduction**

بسم الله الرحمن الرحيم و الصلاة و السلام على أشرف المرسلين

Hello! My name is Adham Heinrich, and this is my second write-up. Today, I’ll walk you through how I identified an IDOR (Insecure Direct Object Reference) vulnerability on an online shopping website that exposed sensitive user data.

**Background**

The target website is an online shop. After two days of exploring its technologies and concept, I used various reconnaissance techniques, including:

- Enumerating subdomains
- Fuzzing paths
- Testing for logic bugs

Unfortunately, none of these methods revealed any vulnerabilities. As part of my standard process, I turned to **waybackurls** to extract historical URLs related to the target domain. I then filtered the results for the keyword “token,” hoping to uncover potential sensitive information. Here’s the command I used:

`echo "https://www.target.com" | waybackurls | grep "token"`
This approach revealed several URLs associated with a subdomain:

**community.target.com**

I accessed the identified URLs and noticed sensitive user data being displayed. Since this subdomain did not seem to allow interaction between users, it raised questions about why this data was visible in the first place.

To investigate further, I used **Burp Suite** to intercept requests and analyze the responses. In one particular request, I identified a parameter called `id` in the URL. Here’s an example:

`GET https://community.target.com/user?id=12345`
I modified the `id` value in the URL to test for IDOR by changing it to another user’s ID, such as `id=12346`. Upon sending the modified request, I received a response containing private information about another user.

**Findings**

The vulnerability allowed me to access sensitive user data by simply altering the `id` parameter in the URL. This data included:

This demonstrates a lack of proper authorization checks, as the server did not verify whether the requesting user had the right to access the data associated with the given `id`.

**Impact**

The exposure of private user data due to an IDOR vulnerability is a significant security risk. Such vulnerabilities can lead to:

- Breaches of user privacy
- Potential exploitation by malicious actors
- Violation of data protection regulations (e.g., GDPR)

**Lessons Learned**

Here are some key takeaways from this experience:

1. **Waybackurls and grep are powerful tools**: Searching for specific keywords like “token” can uncover useful leads during recon.

**2.Check for IDOR vulnerabilities in all endpoints**: Always test whether parameters like `id` can be modified to access unauthorized data.

**4. Implement proper access controls**: Ensure every request is validated to confirm the user’s permissions for accessing the requested resource.

و السلام عليكم و رحمة الله و بركاته
