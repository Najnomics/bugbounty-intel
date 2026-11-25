# DOM XSS using Google Dorks

- **Source URL:** https://jeyabalaji700.medium.com/dom-xss-using-google-dorks-4bd0f69328d8?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20230725080209/https://jeyabalaji700.medium.com/dom-xss-using-google-dorks-4bd0f69328d8?source=rss------bug_bounty-5
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/3402 (id 3402)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# DOM XSS using Google Dorks

--

Using Google dorks we can find XSS

For finding this Our Target want to use WordPress. In this article I going to use [CVE-2021–24891](https://web.archive.org/web/20230725080209/https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-24891). Please go through the articles for this CVE to learn about this DOM XSS. Here I am going to help to find this DOM XSS.

Give the following dork to find the website using elementor plugin

site:*target.com* inurl:”elementor”

After that check the elementor version. For this vulnerability, The version want to less then 3.4.8. You can use Wappalyzer or other tools.

`https://target.com/#elementor-action:action=lightbox&settings=eyJ0eXBlIjoibnVsbCIsImh0bWwiOiI8c2NyaXB0PmFsZXJ0KCd4c3MnKTwvc2NyaXB0PiJ9`
Now paste the given payload and reload the page

We got pop up
