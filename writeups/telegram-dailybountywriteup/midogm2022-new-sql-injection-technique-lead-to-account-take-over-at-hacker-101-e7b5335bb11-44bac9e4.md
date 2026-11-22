# New Sql Injection Technique lead to account take over at hacker 101

- **Source URL:** https://medium.com/@midogm2022/new-sql-injection-technique-lead-to-account-take-over-at-hacker-101-e7b5335bb118?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20230311160221/https://medium.com/@midogm2022/new-sql-injection-technique-lead-to-account-take-over-at-hacker-101-e7b5335bb118
- **Fetched:** 2026-11-22
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/1769 (id 1769)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# New Sql Injection Technique lead to account take over at hacker 101

Hello guys my name is Mohamed yasser (Nitro), this is new writeup that will tell you a new technique to dump admin account of website in 10 minute only

## first our target we will signed him as example.com , first when I try to solve this ctf I found that i can’t edit any page or create one and couldn’t access it and example.com redirected me to login page so l fired my burpsuite to know what’s happend and found this

## so I checked login page if it has any of SQL Injection by trying user (name =mohamed‘) at username

## and Boom :) found error based when get this response

so good news :) I will try to take this post request of login page at text file to access database by sqlmap commends

sqlmap -r /home/nitro/Desktop/123456.txt — dbs

but unfortunately sql map couldn’t access any thing

so I tried to do this manualy by burp intruder :) , so take this request and go to intruder to know length of username and password by this Injection commend and make min & max lingth of intruder =0>>>20 for payload of username and 0>20 for password


and found different length at response of username = 9 and password = 6

and now finally we know number of character of username and password of admin , so we will brute force this account by only one step in username and password …..by this commend only which username =9 characters which any of them referd by $\_$

and this is my fucken fast result

Bingo :) username =francisco

and only replace number of $\_$ to be 6 times and replace username with password like this

and this is the result

password = manual :)

actually I do this manually and password is same manually word :)

so lets fire my browser and show if we can get this fucken flage or not !

and Bingo :) we got flag wow (:

fianlly , this writup has finished. i hope you have a good time reading this writeup and got this fast techneque I found and would to shared it with you (: so good night.
