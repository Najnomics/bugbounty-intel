# Deep Recon Leads to Unauthenticated Upload & IDOR — Rewarded with Bounty $$$

- **Source URL:** https://medium.com/@0xAsad_Eldin/deep-recon-leads-to-unauthenticated-upload-idor-rewarded-with-bounty-bfa58a03397f?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250519160112/https://medium.com/@0xAsad_Eldin/deep-recon-leads-to-unauthenticated-upload-idor-rewarded-with-bounty-bfa58a03397f
- **Fetched:** 2026-11-21
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/9679 (id 9679)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Deep Recon Leads to Unauthenticated Upload & IDOR — Rewarded with Bounty $$$

# **بِسْمِ اللَّهِ الرَّحْمَنِ الرَّحِيم**

# **الْحَمْدُ لِلَّهِ وَحْدَهُ، نَصَرَ عَبْدَهُ، وَأَعَزَّ جُنْدَهُ، وَهَزَمَ الْأَحْزَابَ وَحْدَهُ، وَالصَّلَاةُ وَالسَّلَامُ عَلَى مَنْ لَا نَبِيَّ بَعْدَهُ، أَمَّا بَعْدُ**

**السلام عليكم ورحمة الله وبركاته**

**أسألُ الله العظيم رب العرش العظيم أن يُفرّج عن إخواننا في فلسطين كل كرب، وينصرهم على من عادَاهُم، ويحفظ أرضهم وأهلهم، ويرزقهم الصبر والثبات والنجاح في مواجهة الظلم والاحتلال. وأدعو الله أن يثبت المجاهدين في حركة حماس، وأن يمدّهم بالقوة والعزيمة، ويرزقهم النصر المبين، ويحفظهم من كل سوء، ويجعل كفّهم على أعدائهم، ويفتح لهم أبواب الفرج والتمكين، ويعزّ الإسلام والمسلمين على أيديهم.**

# Who Am I?

My name is **Osama Eid**, aka **0xAsad\_Eldin** (أسد الدين) — and yes, **“Asad”** means **lion**, not the name (أسعد). I’m a Level 3 cybersecurity student passionate about bug bounty hunting, with a strong focus on deep recon and manual testing.

# Initial Phase — Choosing a Target

While exploring wildcard programs on Bugcrowd, I stumbled upon a promising target. I decided to dig deep with **intensive recon**, something I absolutely enjoy doing.

# Recon Phase

I used a modified version of a recon bash script by [Az3m](https://medium.com/u/cf75ba8959e8?source=post_page---user_mention--bfa58a03397f---------------------------------------), tailored to my own workflow. Here’s what it looked like:

```
#!/usr/bin/env bash
domain=$1
if ! [ $domain ]; then
  echo "[!] No target provided."
  echo ">> $0 <example.com>"
  exit 1
fi
subfinder -all -silent -d $domain -o subfinder.txt
findomain -t $domain -u findomain.txt
curl -s "https://crt.sh/?q=%25.${domain}&output=json" | jq -r '.[].name_value' | sed 's/\*\.//g' | anew crtsh_subs.txt
github-subdomains -d $domain -t <Your_Git_Hub_Token>-o github_subs.txt
amass enum -passive -norecursive -d $domain -o amass.txt
echo "$domain"|dnsgen - |tee dnsgen.txt
echo "$domain"|alterx |tee alterx.txt
puredns bruteforce resolvers.txt
cat subfinder.txt findomain.txt amass.txt dnsgen.txt crtsh_subs.txt
alterx.txt |uniq -u |tee subdaomins1.txt
```
Then, I filtered live subdomains using:

`cat subdaomins1.txt | httpx  -silent -sc -probe -title -td -ip -p 81,82,443,8080,3000,8443,9000,5432,9001,9002,9003,8888,2079,2083,2086,2082,2096,2095,9999,8888,7443,8443,9443,66,4444,80,443,445,457,1080,1100,1241,1352,1433,1434,1521,1944,2301,3000,3128,3306,4000,4001,4100,5000,5432,5800,5801,5802,6346,6347,7001,7002,4433,9443,8140,6443,8089,4343,10000,4443,31337,3001,10250,5986,3790,9001,7548,2376,2083,5006,8085,4444,9943,55553,5001,3780,8181,9091,16993,8083,9095,7443,10443,8880,995,587,465,110,2083 -t 90 -mc 200,404,403,302,301,303,304,305,306,307,302 -o live1.txt`
After that, I proceeded to gather subdomains of the discovered subdomains

```
echo “extracts the subdomains”
cat live1.txt|awk '{print $1 }' |cut -d / -f3 |awk -F: '{print $1 }'|tee subdomain2.txt
echo "extracts the last 3 segments of each domain"
cat subdomain2.txt|awk -F. '{print $(NF-2)"."$(NF-1)"."$NF}'|uniq -u |tee subdomain2_uniq.txt
subfinder -all -silent -dL subdomain2_uniq.txt -o subfinder2.txt
cat subdomain2_uniq.txt |dnsgen - |tee dnsgen2.txt
cat subdomain2_uniq.txt |alterx |tee alterx2.txt
```
Then, I filtered live subdomains using:

`cat subdomain2_uniq.txt | ~/.pdtm/go/bin/httpx  -silent -sc -probe -title -td -ip -p 81,82,443,8080,3000,8443,9000,5432,9001,9002,9003,8888,2079,2083,2086,2082,2096,2095,9999,8888,7443,8443,9443,66,4444,80,443,445,457,1080,1100,1241,1352,1433,1434,1521,1944,2301,3000,3128,3306,4000,4001,4100,5000,5432,5800,5801,5802,6346,6347,7001,7002,4433,9443,8140,6443,8089,4343,10000,4443,31337,3001,10250,5986,3790,9001,7548,2376,2083,5006,8085,4444,9943,55553,5001,3780,8181,9091,16993,8083,9095,7443,10443,8880,995,587,465,110,2083 -t 90 -mc 200,404,403,302,301,303,304,305,306,307,302 -o live1.txt`
# Testing Phase

After gathering live hosts, I manually visited each one — prioritizing status code **200**, but also checking others like **403** and **404**.

One subdomain stood out.

IDOR + Unauthenticated File Upload Chain

Let’s call the subdomain:

**weird.target.com**

It initially showed a blank white page, but after directory fuzzing, I discovered:

`https://weird.target.com/docs`
I began testing every endpoint and discovered that the `/files/all` and `/files` endpoints listed all internal files related to employees and the company.

I then began testing the `/upload` endpoint, which initially responded with a "wrong method" error.

So, I opened Burp Suite, changed the request method to `POST`, crafted a file upload request — and to my surprise, the file was uploaded successfully **without any authentication**.

I then returned to the `/files/` endpoint and confirmed that the file had been uploaded successfully.

The uploaded file appeared under the official company email, making it seem as though it was uploaded by a legitimate internal user. I then attempted to achieve remote code execution (RCE) by uploading a PHP payload. Although the file was successfully uploaded, the server was configured to block the execution of PHP code. I also tested for path traversal, but found it was not possible. After that, I explored other endpoints such as `/delete/` and `/download/`, and discovered I could read and delete internal files without any authentication — so I reported the issue immediately , and Alhamdulillah, I received a bounty for my findings.

Additionally, I discovered a race condition vulnerability on another domain related to the target. I plan to publish a detailed write-up soon if the company confirms that the issue has been resolved.

# Contact

If you’d like to connect or discuss anything related to this write-up, feel free to reach out via:

LinkedIn: [https://www.linkedin.com/in/osamaeidsaid](https://www.linkedin.com/in/osamaeidsaid)
