# How I found a SQL Injection bug in using my cellphone

- **Source URL:** https://medium.com/@0xnaeem/how-i-found-a-sql-injection-bug-in-using-my-cellphone-5b5193fdc314?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20230713133032/https://medium.com/@0xnaeem/how-i-found-a-sql-injection-bug-in-using-my-cellphone-5b5193fdc314
- **Fetched:** 2026-11-19
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/3101 (id 3101)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# How I found a SQL Injection bug in using my cellphone.

--

Assalamu Alaikum

I am Naeem Ahmed Sayed (0xNaeem),

Part Time Bug Bounty Hunter from Bangladesh . 

and welcome to my story about a critical bug I found on the phone.

Let’s Start, I choose Hackerone VDP Program And Most Interesting Thing this vdp Program give reward critical and high bug . So I started my recon and searching for login forms , reset password using Google Dorking And also Shodan Help me to find origin IP without WAF I used a simple dork.

Google Dork: site:\*.target.com intext: forgotpassword

and then I found a subdomain that caught my attention. This Subdomain look like sub.target.com/path/forgotPassword.jsp and I started testing time based SQL injection but WAF can't give me future exploit, Then simply use Shodan dork to find origin IP and play without WAF .

Shodan Dork:

Ssl.cert.subject.cn:"sub.target.com" 200

I used the following payload on forgot password:

admin'XOR(if(now()=sysdate(),sleep(10),0))XOR'Z

And open DevTools on kiwi browser to see server response after 10 seconds. I quickly capture the post request in Kiwi Browser for exploit in SQLMap.

When I see the sqlmap result I'm surprised and I couldn’t believe I got my first SQL Injection bug on my phone 🤳 .

Report: April / 03 / 2022

Trigger: April / 04 / 2022

Resolved: Jun / 19 / 2023 :)

If you like this story follow me for more stories like this.

Note: I’m not expert in English.

So forgive me if I am wrong..

Allah Hafiz

Thank you !!!
