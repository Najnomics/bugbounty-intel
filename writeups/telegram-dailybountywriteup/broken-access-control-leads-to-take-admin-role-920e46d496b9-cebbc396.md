# Broken Access Control leads to Take Admin Role

- **Source URL:** https://0xebn-taimia.medium.com/broken-access-control-leads-to-take-admin-role-920e46d496b9?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20260304044535/https://0xebn-taimia.medium.com/broken-access-control-leads-to-take-admin-role-920e46d496b9
- **Fetched:** 2026-11-27
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/6111 (id 6111)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
### **Broken Access Control leads to Take Admin Role**

بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيمِ | In the name of God, the most gracious, the most merciful

Hello hackers, My name is Momen samir (0xEbn-Taimia), Today i’ll be discussing a bug that i recently found with my friends by collaboration on bugcrowd

So lets git in to it , First the tools we used :

1- Subfinder (with API keys to collect more subdomains)

2- FFUF ( To fuzz for endpoints)

3-Burp suite ( a proxy tool to intercept the requests )

- \- First we collect the subdomains and we found a subdomain named :

*https://mktgadt.example.com*


The response from that subdomain was 404 not found with content lenght 0 zero

- \- But always fuzz may you find something, here we used ffuf

*ffuf -w /home/kali/Desktop/wordlist/fuzz.txt -recursion -u https://mktgadt.example.com/FUZZ*


After fuzzing we found an interesting endpoint with response 200 ok :

*https://mktgadt.example.com/*audience/login


The endpoint was an admin login page and there was a create account option !!!!

We immediately created the account but its normal user with no privilege with type : viewer

- now we try to show the create account request in burp and we notice that the parameter “type” is existing in the request

what if we change the parameter value to admin ?

- Booom ! we are admin and we can see the admin interface

there was more than one type and we can make account with any type :

- 1- super-admin ( edit or delete or change privilege )
- 2- admin ( delete)
- 3- editor (can edit activity )
- 4- viewer (just view )

now with super admin account try to edit any account privilege to see its work or no and,

its work !

We immediately report it to bugcrowd as P1 and it got triaged in just 5 minutes

but unfortunately the website team tell us that this finding had been fixed prior to this submission being accepted on their end

But how and it got triaged in just 5 minutes and the bug was fixed in less than 1 day

and they tell us that them still wanted to have a gesture of gratitude with us and decided to award us with a P4 bounty as this finding helped establish a communication channel with the owning team

we didn’t get the bounty we expected but in the end we can’t stop saying:

**Thank god | الْحَمْدُ لِلَّهِ**
