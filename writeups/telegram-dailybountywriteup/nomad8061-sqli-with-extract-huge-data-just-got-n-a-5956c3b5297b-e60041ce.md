# SQLI  with extract Huge Data just Got N/A

- **Source URL:** https://medium.com/@nomad8061/sqli-with-extract-huge-data-just-got-n-a-5956c3b5297b?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250504100630/https://medium.com/@nomad8061/sqli-with-extract-huge-data-just-got-n-a-5956c3b5297b
- **Fetched:** 2026-11-22
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/5740 (id 5740)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# SQLI 💉 with extract Huge Data just Got N/A 🤦🏻

Hello Geeks you are ready to listen my crazy story 📝 let’s go

so our target today is private BBP so let’s name it nomad.com

so first thing i do when start Hunting i go for third party service like Fofa and censys,zoomeye,shodan 

in my case i went first to shodan and used this Dork to see what we have with our target

`Ssl.cert.subject.CN:"nomad.com"`
after 2 minutes of me a search on shodan i found this see the image below

i opened index of / and i found two endpoint cgi-bin and hnet

i opened them i found in hnet/ login panel with name of the company on the panel

when i saw this panel i told myself there is SQLI there i had this feeling because the panel seemed somewhat old

so when i see login panel first thing i try it is authentication bypass and response manipulation etc…. 

I tried authentication bypass and response manipulation i didn’t get any result 

so i added in the first input and second admin’ admin’ and BOOM i got SQLI error

we have Error-based SQLi so let’s exploit it always i prefer the manual approach so i tried but i didn't git any thing so i told myself lets run sqlmap while i do my manual test 

i got the request from burp suite and i added it in nomad.txt 

and i sent it to sqlmap with this command

`sqlmap -r  nomad.txt --dbs --hostname`  i didn’t get any result with normal command lets increase it with this command

`sqlmap -r nomad.txt  --level 5 --risk 3   --ignore-cod 401 --dbs --hostname`  i got this 

sqlmap failed to extract the names of database and hostnames

so i sent the the request to the burp suite scanner to see what she tell us and she caught the SQLI 🤷🏽

so let’s do intruder parte to discover Blind SQLI

as you see in video we have delay between requests so we got Blind SQLI

But now we need good poc so let’s try ghauri with this command

`ghauri -r nomad.txt  --dbs  --hostname`  ghauri is the magic 🤩

but if you were among the elite hacker you should have noticed something our target was nomad.com But we found SQLI on nomad.com.br what do you think Is it out of scope? 

Let me know what you think in the comments

Note: when i extracted the names of the database the company name was present in the data names lol

this was the company teams response

what do we learn today from this ?

1-dont trust the results of the tools like sqlmap or ghauri or burp suite Just trust your mind and try more than one Method

2- Do not go outside the scope even if the effect is within the scope because this will depend on the opinion of the program team

This is the end of our story today i hope it will be useful to you

You can follow me on Twitter and Facebook. I will post useful information soon
