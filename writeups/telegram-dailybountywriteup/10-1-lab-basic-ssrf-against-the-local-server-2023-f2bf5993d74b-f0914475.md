# 10.1 Lab

- **Source URL:** https://cyberw1ng.medium.com/10-1-lab-basic-ssrf-against-the-local-server-2023-f2bf5993d74b?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20240731001954/https://cyberw1ng.medium.com/10-1-lab-basic-ssrf-against-the-local-server-2023-f2bf5993d74b
- **Fetched:** 2026-11-27
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/3995 (id 3995)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# 10.1 Lab: Basic SSRF against the local server | 2023

## This lab has a stock check feature which fetches data from an internal system.To solve the lab, change the stock check URL to access the admin interface at [http://localhost/admin](http://localhost/admin) and delete the user Carlos | Karthikeyan Nagaraj

2 min readSep 29, 2023

## Description

This lab has a stock check feature which fetches data from an internal system.

To solve the lab, change the stock check URL to access the admin interface at `http://localhost/admin` and delete the user `carlos`

## Solution

1. Click a Product and Check out the Stock Checking Functionality
2. Capture the request, you can see that there is a parameter called stockAPI which has a encoded string
3. Send the request to the decoder and click smart decode to decode the string and know that it is directing to an internal page
4. So now, change the stockAPI parameter to [http://localhost/admin](http://localhost/admin) as given in Lab description and send the request
5. Now you can able to see that the response is successful and on inspecting the code you can get the URL to delete user `Carlos`
6. If you are using a professional version, you can render the response for a better result
7. Copy the URL that we found on 4th step’s response
8. Now Paste it on the stockAPI Parameter to solve the Lab

If you would like to support me so that I could create more free content — [https://www.buymeacoffee.com/cyberw1ng](https://www.buymeacoffee.com/cyberw1ng)

Thank you for Reading!

Happy Hacking \~

`Author: Karthikeyan Nagaraj ~ Cyberw1ng`
Telegram Channel for Ethical Hacking Dumps — [https://t.me/ethicalhackingessentials](https://t.me/ethicalhackingessentials)
