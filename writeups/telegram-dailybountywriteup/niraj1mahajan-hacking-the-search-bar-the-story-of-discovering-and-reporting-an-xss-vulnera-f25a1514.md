# Hacking the Search Bar

- **Source URL:** https://medium.com/@niraj1mahajan/hacking-the-search-bar-the-story-of-discovering-and-reporting-an-xss-vulnerability-on-bing-com-cac2f241835?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250714230052/https://medium.com/@niraj1mahajan/hacking-the-search-bar-the-story-of-discovering-and-reporting-an-xss-vulnerability-on-bing-com-cac2f241835
- **Fetched:** 2026-11-24
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/1757 (id 1757)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Hacking the Search Bar: The Story of Discovering and Reporting an XSS Vulnerability on Bing.com

Hello Researchers,

Welcome back to my [Medium](/@niraj1mahajan/) write-up! I’m thrilled to have you here again, and I’m looking forward to sharing some new and exciting content with you.

After being listed on the Hall of Fame in **Google** and **Apple**, I have decided to start hunting for vulnerabilities on **Microsoft**! 🤩 Soon enough, I discovered an XSS vulnerability on Bing.com, which earned me a place in [Microsoft’s Hall of Fame](https://msrc.microsoft.com/update-guide/acknowledgement). 🏆🎉

**What is XSS (Cross-Site Scripting):**

XSS (Cross-Site Scripting) is a type of security vulnerability commonly found in web applications. It occurs when an attacker can inject and execute malicious scripts or code into a web page viewed by other users. This can result in the attacker being able to steal sensitive user information, such as login credentials or personal data, or perform actions on the user’s behalf, such as making unauthorized transactions or posting unwanted content.

**About my finding:**

While casually browsing the web on Microsoft Edge, I decided to test for an XSS vulnerability on the default search engine, Bing.com. It was unexpected that the Bing search results page exhibited a pop-up in response to the XSS payload I had entered.

Knowing that it wasn’t possible to get a pop-up on the main Bing.com search bar, I realized that this could be a potential vulnerability. To verify my finding, I opened an incognito browser window to test the same scenario. To my relief, the XSS pop-up was not appearing in incognito mode. Then I checked the account I was logged into and found that I was using my work account.

I tested the same scenario with my personal account, but the pop-up was not appearing. This confirmed that the XSS vulnerability was only present for work and school accounts.

Without wasting any time, I wrote a detailed report to the Microsoft Security Response Center (MSRC) team, explaining the steps to reproduce the vulnerability.

The vulnerability was promptly addressed and resolved, making the web a safer place for all users. I was grateful to have been able to contribute to the security of such a widely-used platform.

As a result of finding this vulnerability, I was awarded a spot on Microsoft’s Top Security Researchers [2022 Q2 Leaderboard](https://msrc.microsoft.com/leaderboard) at number 55 🏆😎

**Steps to Reproduce:**

1. Go to Bing.com
2. Login with Microsoft Work/School Account
3. Enter XSS Payload in the Search Field and Click on Search
4. Again Click on Search Bar to Trigger the XSS

**Important Note/Tip:** It’s worth nothing that attempting to exploit the vulnerability with a normal account versus a work/school account may yield different outcomes.😁

If you need any help or want to connect, you can connect with me via [LinkedIn](https://www.linkedin.com/in/niraj1mahajan/).

I hope it will help you in your Bug Hunting !!

Thanks for Reading !!😊

./Keep\_Hacking
