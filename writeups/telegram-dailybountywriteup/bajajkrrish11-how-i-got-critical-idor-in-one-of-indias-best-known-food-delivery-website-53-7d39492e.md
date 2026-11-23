# How I got Critical IDOR in one of India’s Best Known Food Delivery Website

- **Source URL:** https://medium.com/@bajajkrrish11/how-i-got-critical-idor-in-one-of-indias-best-known-food-delivery-website-5349c521e44b?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20240530015740/https://medium.com/@bajajkrrish11/how-i-got-critical-idor-in-one-of-indias-best-known-food-delivery-website-5349c521e44b
- **Fetched:** 2026-11-23
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/6138 (id 6138)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# How I got Critical IDOR in one of India’s Best Known Food Delivery Website

Hello everyone,

Today I am going to share how I got Critical IDOR on Swiggy BBP. This is my first bug bounty write-up so, pardon me for my mistakes. A bit of introduction about me, My name is Krrish I’m a Btech CSE Student and a part-time bug bounty hunter.

So, let’s Begin with the findings we will explain in this report.

While Looking for a program to hack on I always look for wide and open scope programs as they give me so much freedom to look for assets that can match my skills. So, after I decided to start hacking on one of the public programs and after doing **Subdomain Enumeration** using Tools like: (Sublist3r, Knockpy, Virustotal and Amass) and save all subdomains after sorting the unique ones to a file ie: swiggy.txt , then i decided to look for some interesting subdomains after using **HTTPX Tool** and collecting all 200 response code subdomains.

Then I use **Dirsearch** for directory listing bugs… got some but not enough to report them as critical or high severity bug to Swiggy, so i used grep command in swiggy.txt file to grasp some interesting subdomains (*command*: cat swiggy.txt | grep “admin,dev, developer, production, etc”)

I got one subdomain, let’s say it as (redacted.\*.swiggy.com) so its basically a subdomain of Swiggy which helps restaurants to be registered on it. So while my initial testing i got a login page where new user can register too so i registered via my Number and the OTP came and I got logged in, after Registereing there’s a place to list our restaurant, i do typed any random restaurant name for registration and then there’s a field to Provide **FSSAI Number,** i send random number and then due to some issues i was not able to crack the wall since it requires correct FSSAI number then i search everywhere its possible but not lucky to get one :(

Then i got Frustrated since i was being hunting from 2 hours on swiggy without positive outcome :) then i just switch to Netflix and rest for half hour then started my Burpsuite again, and check for some cool endpoint at that FSSAI Number Request, So i submit my Number can capture the request in burp then send it to repeater and started playing with it, not holly-fuck i was’nt that lucky :(

Now i just logged out from my account and thought let’s try once more so I Re-Login with my Mobile number and go to Application as shown which is Left Incomplete and here’s is a Joy, I got new Endpoint which was: (/external/swiggy/form/inbounds/1234566)

So I started my Burp and capture this endpoint request in it and send it to intruder so since its just a Numerical digits so it was easy to bruteforce the digits, I started my attack and in response I got all registered **Restaurants details** (Everything :) )

And this was my reaction:

I was like WOW, I have done it :) Now its time to report i reported it to swiggy security team and they fixed it in appx. \~5 days and I was thinking to get a bounty of more than 500$ minimum from them but i forgot that swiggy is indian BBP :) Hence they Fixed the bug and send me just 2000 Rupees :)

Although I was so happy to get a bug in swiggy.

# We are done!

Thanks for reading, hope you learned something new.
