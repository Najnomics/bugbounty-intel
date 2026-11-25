# ChatGPT Hacking Prompts, SQLi, XSS, Vuln Analysis, Nuclei Templates, and more

- **Source URL:** https://systemweakness.com/chatgpt-hacking-prompts-sqli-xss-vuln-analysis-nuclei-templates-and-more-dba6fa839a45?source=rss------bug_bounty-5
- **Fetched from:** https://systemweakness.com/chatgpt-hacking-prompts-sqli-xss-vuln-analysis-nuclei-templates-and-more-dba6fa839a45?gi=6f925e296a5a&source=rss------bug_bounty-5
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/1716 (id 1716)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
Member-only story

# ChatGPT Hacking Prompts, SQLi, XSS, Vuln Analysis, Nuclei Templates, and more

## Several prompts for hacking with ChatGPT I’ve consolidated with demos.

The magic with ChatGPT is it can generate the script for you, explain what it does, and improve it.

### Red team / offensive security / bug hunting:

ChatGPT has some great ideas. As always, the prompts are the most important. Here are some great examples by [Aakash Rathee on youtube](https://www.youtube.com/@aakashrathee_yt)

- [10 SQL Injection payload](https://youtu.be/AX5BmwYX9kQ?t=107)s.
- [10 blind SQL Injectrion payloads](https://youtu.be/AX5BmwYX9kQ?t=172)
- [10 XSS payloads](https://youtu.be/AX5BmwYX9kQ?t=232) (cross site scripting)
- [Encoded XSS payload](https://youtu.be/AX5BmwYX9kQ?t=387)
- For webapps, [find login vulnerabilities](https://youtu.be/AX5BmwYX9kQ?t=478) (ideas, not scripts)
- [Exploit file upload functionality](https://youtu.be/AX5BmwYX9kQ?t=680) (tactics)
- [Bash script to find subdomain with help of subfinder, take input from user for target](https://youtu.be/0kjedNSmafs?t=96) (and [save the alive results in a file](https://youtu.be/0kjedNSmafs?t=250))

**Nuclei templates**

Nuclei is an open source vulnerability scanner. Templates are used to specify the target and action of the scanner.

- [Create Nuclei template for .env in a server](https://youtu.be/0kjedNSmafs?t=488)
- [Nuclei template for wordpress users](https://youtu.be/0kjedNSmafs?t=529)
- [Nuclei template to check for default credentials](https://youtu.be/0kjedNSmafs?t=589) (in Apache Servers)

### Blue team / defensive security / analysis:

You can use ChatGPT to analyze code responses or explain the vulnerability present.
