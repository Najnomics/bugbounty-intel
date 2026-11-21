# This tool helped me to find IDOR

- **Source URL:** https://medium.com/@canonminibeast/this-tool-helped-me-to-find-idor-c87a9c1a04f3?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250502134206/https://medium.com/@canonminibeast/this-tool-helped-me-to-find-idor-c87a9c1a04f3
- **Fetched:** 2026-11-21
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/9004 (id 9004)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# This tool helped me to find IDOR

hey hi guys ,its for bug bounty hunters. This blogs helps beginner bug bounty hunter ,when the noob hunters planned to hunt for a IDOR vulnerability the stuck with the uuid which is so long and they loose hope and feel unmotivated.

This blog helps you to find idor

IDOR-Insecure direct object references.(It is a access control vulnerability)

The beginner stuck with this kind of uuid ,no worries folks ill help with a github tool

`GET /api/uuid=880e5400-31sn-13ns-13122001312002 HTTP/1.1`
uuid-enum

This tool helps you to bruteforce the uuid ,until it finds a valid uuid,I just give the link below for u guys

`https://github.com/it4chis3c/uuid-enum`
Steps to install it

Step 1: git clone [https://github.com/it4chis3c/uuid-enum.git](https://github.com/it4chis3c/uuid-enum.git)

Step 2: cd uuid-enum

Step 3: Run the command — pip install -r requirements.txt

Note that if u kali linux u neeed to create a venv

Step 4:python3 uuid\_enum.py -u “[https://target.com/user/UUID\_HERE](https://api.target.com/user/UUID_HERE)" -m sequential -c 100 -t 10 -o 5
