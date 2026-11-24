# IDOR Disclose User Pending Trip Information | Part 01

- **Source URL:** https://medium.com/@anmolvishwakarma7466/idor-disclose-user-pending-trip-information-part-01-5e92202318c9?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20221206143830/https://medium.com/@anmolvishwakarma7466/idor-disclose-user-pending-trip-information-part-01-5e92202318c9
- **Fetched:** 2026-11-24
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/953 (id 953)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# **IDOR Disclose User Pending Trip Information | Part 01**

Hi Amazing Hackers & Security Enthusiasts, today I am going to write about something very important. Identifying IDOR bugs that lead to full account takeovers without user interaction is my first IDOR bug.

Let’s do some background about IDOR before jumping on the bug

IDOR (Insecure direct object references)

Insecure direct object references (IDOR) are a type of access control vulnerability that arises when an application uses user-supplied input to access objects directly. IDOR vulnerabilities are most commonly associated with horizontal privilege escalation, but they can also arise in relation to vertical privilege escalation.

So, let’s call the target as **target.com.** I started with the Recon on the main domain. Now after Recon I Started to understand the application how it work. Just Open the Burp. and start to analyze the application how it work, how it process the request, see which methods are allowed. analyze the Source Code for any secret-API key , or any token, or endpoints.

I look and use some functionality like update profile, upload profile image, and change password without old password, and monitor each and every request and response using burp.

Bug 01: **IDOR Disclose User Pending Trip Information**.

I schedule a trip and after that I make a request to get information about my trip. so the request look like

/target-dev/index.php/UserPortal/Trip/tripListByUser


Request Look Like

POST /targetservice-dev/index.php/UserPortal/Trip/tripListByUser HTTP/1.1

Host: app.target.com

Cookie: \_ga\_4FPFRN1P35=GS1.1.1669338233.4.0.1669338233.0.0.0; \_ga=GA1.1.749545081.1669213744; bfp\_sn\_rf\_b10ce94cf299b167b74a6944e0aec9d4=Direct; bfp\_sn\_rt\_b10ce94cf299b167b74a6944e0aec9d4=1669215441778; ci\_session=4rk74md1hpc0hrac5dfv3li2av

User-Agent: Mozilla/5.0 (X11; Linux x86\_64; rv:91.0) Gecko/20100101 Firefox/91.0

Accept: application/json, text/plain, \*/\*

Accept-Language: en-US,en;q=0.5

Accept-Encoding: gzip, deflate

Content-Type: application/x-www-form-urlencoded

Content-Length: 59

Origin: https://app.target.com

Referer: https://app.target.com/target-user-portal/

Sec-Fetch-Dest: empty

Sec-Fetch-Mode: cors

Sec-Fetch-Site: same-origin

Te: trailers

Connection: close

{“user\_id”:”1654",”status”:”pending”,”[T](https://app.loadmee.com)ARGETAUTHKEY”:8342}


Now Note The two things First is [T](https://app.loadmee.com)ARGETAUTHKEY and second is “user\_id”:”1654".

send this request to repeater and see the response you get the information about the pending trip information.

Now after that send request to intruder and brute force the the “user\_id” and payload is Number Start from 0000 to 9999 and sequence is 1. click on Start Attack. And shortlist the request and response on length Booom you get other user pending trip information with disclose user id and user pick and drop location.

Response Look Like

{“user\_id”:”418",”status”:”pending”,”LOADMEEAUTHKEY”:8012, Trip\_Id:XXXX, Tripe\_location: “user pick data”, Tripe\_destination: “trip drop location”, Essitemate\_total:35000}

And So this response disclose the two things

1. register User Id and Location
2. Trip Data

It’s my first write-up! It is a great feeling to be with the right path with a great mentor. Please also guide me on how to write a good article.

Happy Hacking
