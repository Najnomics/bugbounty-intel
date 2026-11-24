# From Error_Log File(P4) To Company Account Takeover(P1) and Unauthorized Actions On API

- **Source URL:** https://medium.com/@mohanad.hussam23/from-error-log-file-p4-to-company-account-takeover-p1-and-unauthorized-actions-on-api-35e45e43273a?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20230324155213/https://medium.com/@mohanad.hussam23/from-error-log-file-p4-to-company-account-takeover-p1-and-unauthorized-actions-on-api-35e45e43273a
- **Fetched:** 2026-11-24
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/1435 (id 1435)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# From Error\_Log File(P4) To Company Account Takeover(P1) and Unauthorized Actions On API

Hi Everyone,My name is **Muhanad Israiwi**.

I’m Bug Bounty Hunter,Software Engineering Student At Amman Arab University.

I was working On Program we can call it (**Aex-Target**),The Target has domain which we will can call it **\*.aex-target.com**

What Basically I do every time I go hunting is Subdomain-Enumeration,Collect and Sort The result in one file

**-Some Subdomain-Enumeration Tools:**

**Findomain,Sublist3r,Amass,Subfinder**

Command For Sorting,Removing Duplicates and Saving Results In **new\_file.txt** or you can use tool called [**anew**](https://github.com/tomnomnom/anew) from **tomnomnom**

`cat file.txt | sort -u > new_file.txt`
Using [**Httpx**](https://github.com/projectdiscovery/httpx) I filtered The Live Subdomains and Save it in **Result.txt**

Then I did Fuzzing On The Live Subdomains which is saved in **Result.txt from before.**

**-Tools You Can Use For Directory Fuzzing** 

1-**FFuf,Dirsearech,**[**wfuzz**](https://github.com/xmendez/wfuzz) Tools With **World\_List or any List You Have.**

After Doing Fuzzing I found **error\_log** File In one of the Subdomains which was like this

**Vulnerable-File**:[https://aex-target.com/**log.txt**](https://aex-target.com/log.txt)

Inside Of The File it was a lot of errors and dummy information,but I noticed Some Request Headers Locking Like This:

```
{
 Authorization: Token 66d3337fefbf4d91xxxxxxxxxxxxx
 Accept: application/json
 singularityheader: appId=64xx
 Content-Type: application/json; charset=utf-8
 Content-Length: 23
}
```
After I found these Information I started searching inside **log.txt** for any **API-Endpoints** so I can use Request Header With It.

To do This I just Press **CTRL+F** and search for **/api/** and I found **API-Endpoint** like This One

or you can use a command to extract Urls From The File.

So,I Found **API-Endpoint** Locking Like This

[https://xxxUpload.com/api/encodingjobs/1xx9788/](https://xxxUpload.com/api/encodingjobs/1xx9788/)

When I navigate To The **API-Endpoint** which is [https://xxxUpload.com/api/encodingjobs/179788/](https://xxxUpload.com/api/encodingjobs/179788/) 

**It Return**

**{“detail”:”Authentication credentials were not provided.”}**

So You know what is that mean 😀 ,Let’s use the Request Headers to try to get **Authenticated.**

**\[+\]Exploits**

**1-I tried sending This Request Using curl**

- **I was able to view all the Encoding jobs Using The Authentication Token**


curl “https://xxxUpload.com/api/encodingjobs/" -H “Authorization: Token 66d3337fefbf4d91xxxxxxxxxxxxx”
But That’s not **Enough to Be High impact**,So I did an API-Endpoints Fuzzing Using Using **Dirsearech** with List Of API-Endpoints You can get it from here [**API-World\_List**](https://github.com/chrislockard/api_wordlist) .

**I Discovered These Endpoints:**

[https://xxxUpload.com/api/groups/](https://xxxUpload.com/api/groups/)

[https://xxxUpload.com/api/devices/](https://xxxUpload.com/api/devices/)

[https://xxxUpload.com/api/networktypes/](https://xxxUpload.com/api/networktypes/)

[https://xxxUpload.com/api/products/](https://xxxUpload.com/api/products/)

I started Using The same curl request ,but changing the **API-Endpoints with the new one I Found**

**Viewing All Devices Inside The Accounts**

[https://xxxUpload.com/api/devices/](https://xxxUpload.com/api/devices/)

**Viewing All Groups Inside The Accounts**

[https://xxxUpload.com/api/groups/](https://xxxUpload.com/api/groups/)

**Viewing All Products Inside The Accounts**

[https://xxxUpload.com/api/products/](https://xxxUpload.com/api/products/)

Hope It was helpful and Good Write Up.😀

You can follow me,ask me on [**Linkedin**](https://www.linkedin.com/in/muhanad-israiwi-766b89207/),**Twitter**

**Thanks For Reading.**
