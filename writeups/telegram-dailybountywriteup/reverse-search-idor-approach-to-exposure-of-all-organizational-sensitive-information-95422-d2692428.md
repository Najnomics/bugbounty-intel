# Reverse Search IDOR approach to Exposure of all Organizational Sensitive Information.

- **Source URL:** https://infosecwriteups.com/reverse-search-idor-approach-to-exposure-of-all-organizational-sensitive-information-954220b96a59?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20240912211250/https://infosecwriteups.com/reverse-search-idor-approach-to-exposure-of-all-organizational-sensitive-information-954220b96a59
- **Fetched:** 2026-11-19
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/3955 (id 3955)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Reverse Search IDOR approach to Exposure of all Organizational Sensitive Information.

IDORs Everywhere.

Alright people, let’s do this one last time.

I’m Manav Bankatwala, and I’m a security researcher. I’m not sure what kind of radioactive spider bit me, but it gave me the power to see security vulnerabilities everywhere.

# **Summary:**

This writeup focuses on finding of an IDOR vulnerability which I escalated from Low to Critical severity (Read till the end). I already submitted a plenty of bugs to this private program and thought of stop testing until I got this IDOR. Let’s start from the beginning.

This application has a functionality where as soon as you create an account with a company name. You will be assigned a custom domain i.e. something like “newcompany.target.com”. Your login page will be appeared only through this domain and all the further endpoints as well. I never thought that I will find an IDOR like this.

This IDOR allowed me to get the data of any corporate account from all of the target API Calls. The company paid me $$$ for this vulnerability which was their highest bounty amount.

# **Understanding the application:**

At the very first stage, I turned on my Burp Suite proxy and started using the application from the login page. Whenever I check for IDOR, I usually first visit the profile page and capture all the API calls used. Same way I visited the profile page here and observed the API calls. I found that all the API calls made have two parameters, i.e. CorpID and SiteID. These parameters contains a long alphanumeric value which we cannot guess. This is the point where I though I could test for IDORs. There were some API calls which only had CorpID parameter to get the data and some api calls where both the parameters were needed.

I collected all the API endpoints which were having these two parameters and kept it aside for future use.

# **Exploiting IDOR (LOW):**

To know if these parameters are actually vulnerable, I created another corporate account let’s say victim account and copied the CorpID and SiteID. Moved to the previous endpoints and changed the IDs to new account. Well I got the victim company details in the response.

# **Actual Steps:**

1. Login to attacker account and capture all the API calls which have CorpID and SiteID as parameters.
2. Login to the victim account and copy the CorpID and SiteID.
3. Paste this values in previous attacker’s API calls and get the response.

# **But why low?**

To exploit this IDOR, the attacker have to insert a value which is not guessable. But as the application was having user management, it was possible for a low privilege user to get all the corporate information which is only allowed to admin user. Still the user is added by admin itself, it’s a risk of insider threat. I didn’t reported this at that time and thought to escalate this later.

# **Reverse Search values:**

Upon trying many things like viewing the source code of all the profile pages, I didn’t found anywhere the values being leaked. So for the last, I tried one thing. I copied the “SiteID” value and used the Burp Suite Search function with a filter “Response Headers” and “Response Body”. I got one result with the API call **“/reply/GetfirstCorp?CorpID=”** where the SiteID value was in the response but looking at the request, we need to pass the CorpID value.

Again I copied the CorpID value and used the Burp Suite Search function to find the value in responses. With a result, there was an API call i.e. **“/reply/stylebydomain”** where I was able to see the CorpID in response. But there was no parameter in the request which I can change and get the CorpID of other corporate accounts. I though it must be getting through the Bearer token. But even after removing the bearer token from request, The CorpID was present in the response.

Finally, I observed the HOST header value which was “mycompany.target.com”. I changed this value to “victimcompany.target.com” and sent the request. There we go, we got the CorpID of the victim corporate account. We can get this domains by google dorking or through waybackurls. I tried this value on all the API endpoints with only one parameter and was able to get details like API key, Billing Information etc. Then I used the old API call to get SiteID and got the other corporate info too.

# **Final Exploit Flow:**

1. Use the API call “**/reply/stylebydomain**” with the Host header value of victim company. i.e. “victimcompany.target.com” and get the CorpID.
2. Use the CorpID value in API call “**/reply/GetfirstCorp?CorpID=**” to get the SiteID value.
3. Use other API calls like **“/reply/getalladmin?corpid=” , “/reply/getcurrentSubs” , “/reply/getcorpsettings”.** To extract all the data of the victim corporate account.

# **Conclusion:**

Whenever you come across these type of parameters, always surf the whole website and then search for that value with response filter. Specially when you can view other people accounts. You may get API endpoints where the value is reflected and get to the root endpoint from where it is generating the non-guessable value.

My next Writeup will be all about Hacking India’s largest **\*\*\*** network system. (Can’t disclose as permission in process). Bypassing the payment methods applied including their protections.

# Follow me to get latest updates:

[https://www.linkedin.com/in/manavbankatwala/](https://www.linkedin.com/in/manavbankatwala/)
