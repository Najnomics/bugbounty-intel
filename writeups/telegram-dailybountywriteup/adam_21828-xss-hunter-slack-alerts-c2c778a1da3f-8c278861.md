# XSS Hunter Slack Alerts

- **Source URL:** https://medium.com/@adam_21828/xss-hunter-slack-alerts-c2c778a1da3f?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20221209210241/https://medium.com/@adam_21828/xss-hunter-slack-alerts-c2c778a1da3f
- **Fetched:** 2026-11-24
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/1044 (id 1044)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# XSS Hunter Slack Alerts

This is a tutorial of how to setup XSS Hunter with Slack Alerts

This is my fork of XSS Hunter [https://github.com/adamjsturge/xsshunter-express](https://github.com/adamjsturge/xsshunter-express)

This is the only fork that I know of that has Slack integration and I made it myself so I give it my own stamp.

I use both [Digital Ocean](https://m.do.co/c/a165a29be76c) and [VPSCheap](https://crm.vpscheap.net/aff.php?aff=27) feel free to click on my affiliate links or not.

My first recommendation to save yourself headache and time is to point your domain to wherever you are hosting before we start this process. Also have open the default README.md to do along with this

`git clone https://github.com/adamjsturge/xsshunter-express.git`
We need to make some changes to the default yml that XSS Hunter uses. You can use your favorite terminal code editor

```
cd xsshunter-express
vi docker-compose.yml
```
Things we need to change

- HOSTNAME to your domain

- SSL\_CONTACT\_EMAIL to your email address

- SMTP\_EMAIL\_NOTIFICATIONS\_ENABLED=false

Email notifcations aren’t necessary when you have slack notification

For the SLACK\_WEBHOOK go to [https://slack.com/help/articles/115005265063-Incoming-webhooks-for-Slack](https://slack.com/help/articles/115005265063-Incoming-webhooks-for-Slack)

`curl -X POST --data-urlencode "payload={\"channel\": \"#xssalerting\", \"username\": \"webhookbot\", \"text\": \"This is posted to #xssalerting and comes from a bot named webhookbot.\", \"icon_emoji\": \":ghost:\"}" https://hooks.slack.com/services/`
This Curl will let you text that your webhook is working

To get a webhook for your channel and make sure your yml one matches

The SLACK\_WEBHOOK in the yml **needs** to start with https://

The next step might not be necessary but can resolve a lot of issues of docker not working

`systemctl enable docker`
This will get the Database started for XSSHunter

`docker-compose up -d postgresdb`
# BE READY TO GRAB THE PASSWORD

After this next command the password will be printed when run for the first time and won’t be printed in the terminal again.

`docker-compose up xsshunterexpress`
# Common Debug Steps

## Slack Notification not sending

First step here is to make sure SLACK\_WEBHOOK starts with https:// and that the curl command is correct. You might want to change the slack Emoji if you don’t have [hackerman](https://slackmojis.com/emojis/7530-hackerman)

Second thing to try is to try this command `npm ci` This should fix most problems but also shouldn’t be necessary. Also remember to run`docker compose build` when you make changes

## Docker Compose Broken

I ran into my own issues when testing this. Doing `apt get` or your linux’s package manager might give an old version. Please check that you are on docker compose version 2.\* Using the link from above will solve this problem

## SSL Cert broken

This can be an issue because your domain wasn’t pointing to your IP when it was created. You might be timed out and have to just wait it allow you to do it again. This happened once to me and I made sure to point the domain before starting work and letting the cache clear when checking with a DNS resolver

## Explicit Affiliate links

Digital Ocean: [https://m.do.co/c/a165a29be76c](https://m.do.co/c/a165a29be76c)

VPSCheap: [https://crm.vpscheap.net/aff.php?aff=27](https://crm.vpscheap.net/aff.php?aff=27)

My Twitter: [https://twitter.com/adamjsturge](https://twitter.com/adamjsturge)
