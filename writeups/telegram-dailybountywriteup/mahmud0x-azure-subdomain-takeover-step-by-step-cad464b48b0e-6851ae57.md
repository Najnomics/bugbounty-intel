# Azure subdomain takeover step by step!

- **Source URL:** https://medium.com/@mahmud0x/azure-subdomain-takeover-step-by-step-cad464b48b0e?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20251126142848/https://medium.com/@mahmud0x/azure-subdomain-takeover-step-by-step-cad464b48b0e
- **Fetched:** 2026-11-27
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/3632 (id 3632)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Azure subdomain takeover step by step!

Aug 17, 2023

Today I scanned some subdomain list via **nuclei**. I received a info like this:

Sounds Juicyyyyyyy

Let’s start….

First we will run dig on that subdomain

dig subdomain.example.com


We will claim this subdomain in our azure portal.

First of all go to App Services > Create > Web app


Enter the azurewebsites.net subdomain name, enter other required infos and claim it. I will use python 3.8


Now go to github and fork this repo

[https://github.com/Azure-Samples/python-docs-hello-world](https://github.com/Azure-Samples/python-docs-hello-world)

Edit the app.py


Now go to Deployment Center and connect you github account


Select the repo we just forked and click deployment. It will take 5–10 minutes to reflect


Let’s visit the subdomain


Done!
