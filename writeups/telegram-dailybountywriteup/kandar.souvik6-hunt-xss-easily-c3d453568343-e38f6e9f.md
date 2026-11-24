# Hunt XSS easily

- **Source URL:** https://medium.com/@kandar.souvik6/hunt-xss-easily-c3d453568343?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20230111225204/https://medium.com/@kandar.souvik6/hunt-xss-easily-c3d453568343
- **Fetched:** 2026-11-24
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/1244 (id 1244)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Hunt XSS easily

Hi, everyone .XSS is a common bug that is found accross all the platforms.The easiest way to do that is to use an automation tool .For example xsstrike([https://github.com/s0md3v/XSStrike](https://github.com/s0md3v/XSStrike))

At first we need an url with parameter, after that using XSStrike an XSS vulnaribility can be found easily.

The whole process is as follows-

1. git clone [https://github.com/s0md3v/XSStrike](https://github.com/s0md3v/XSStrike)
2. cd XSStrike
3. pip3 install -r requirements.txt
4. python3 [xsstrike.py](https://github.com/s0md3v/XSStrike/blob/master/xsstrike.py) -u “http://test.com/sadasd?asdasd=aas”
