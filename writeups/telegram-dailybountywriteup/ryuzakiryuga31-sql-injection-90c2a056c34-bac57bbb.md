# Sql injection

- **Source URL:** https://medium.com/@ryuzakiryuga31/sql-injection-90c2a056c34?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20221206143829/https://medium.com/@ryuzakiryuga31/sql-injection-90c2a056c34
- **Fetched:** 2026-11-22
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/978 (id 978)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Sql injection

This is for information only, and this scenario has been encountered more than once, but it must be noted

I will explain everything in detail Well, first of all, we do the usual thing, but here I will be brief. I used a tool in the system and extracted the parameter of the site. This site was the Target

`waybackurls Target.gov| grep "id="`   After extracting the parameters and examining them, I found that the error was repeated in several of them, or rather the injection succeeded. I first resorted to manual injection, but I did not find any benefit. After several attempts, the injection succeeded, and I extracted the following information. Above all, the link was:

`https://Target.gov/cgi-bin/ws.exe/prod/cdbs/pubacc/prod/corrp_list.pl?Facility_id=54570%27`
A little tip When there is data injection, the output when there is a vulnerability should not be as follows

`You have an error in your SQL syntax; check the` But it could be information like

```
ٍServer = Heimdal
your MariaDB server version for the right syntax to use near '\'' at line 1
DB = Order_by a.recived_data_desc
```
I tried several times, but it did not work for me to extract more information, as the data base was empty of any data I sent the report and it was accepted and it turns out that this vulnerability has been reported before -\_-
