# How to Configure Subfinder with API Keys for Better Passive Subdomain Enumeration

- **Source URL:** https://medium.com/@MaMad4Ever/how-to-configure-subfinder-with-api-keys-for-better-passive-subdomain-enumeration-1c0e3e12b5fe
- **Fetched from:** https://medium.com/@MaMad4Ever/how-to-configure-subfinder-with-api-keys-for-better-passive-subdomain-enumeration-1c0e3e12b5fe?source=rss-f3c7198db2c9------2
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14899 (id 14899)
- **Method:** medium-rss-feed (full content:encoded) readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- **Author/Published (RSS):** MaMad / Sun, 06 Sep 2026 01:53:14 GMT

[Subfinder](https://github.com/projectdiscovery/subfinder) is a passive subdomain enumeration tool developed by [ProjectDiscovery](https://projectdiscovery.io/).

It collects subdomains from different public sources and APIs such as [Chaos](https://chaos.projectdiscovery.io/), [DNSDumpster](https://dnsdumpster.com/), [FOFA](https://en.fofa.info/), [Netlas.io](https://netlas.io/), [SecurityTrails](https://securitytrails.com/), [Shodan](https://www.shodan.io/), [VirusTotal](https://www.virustotal.com), [WhoisXMLApi](https://www.whoisxmlapi.com/), [ZoomEye](https://www.zoomeye.ai/) and many other sources.

In this guide, we’ll configure Subfinder with API keys to improve passive subdomain enumeration.

Subfinder uses a default configuration file for API keys:

\~/.config/subfinder/provider-config.yaml

You can configure your API keys inside this file.

If you want to use a custom configuration file, you can specify its path with the -config flag:

subfinder -config /path/to/provider-config.yaml

nano \~/.config/subfinder/provider-config.yaml

2\. Then add your API keys under the corresponding providers.

For example:

bevigil: \[\]

binaryedge: \[\]

bufferover: \[\]

builtwith: \[\]

c99: \[\]

censys: \[\]

certspotter: \[\]

chaos: \[\]

chinaz: \[\]

digitalyama: \[\]

dnsdb: \[\]

dnsdumpster: \[\]

dnsrepo: \[\]

facebook: \[\]

fofa: \[\]

fullhunt: \[\]

github: \[\]

hunter: \[\]

intelx: \[\]

leakix: \[\]

netlas: \[\]

quake: \[\]

redhuntlabs: \[\]

robtex: \[\]

securitytrails: \[\]

shodan: \[\]

threatbook: \[\]

virustotal: \[\]

whoisxmlapi: \[\]

zoomeyeapi: \[\]

Replace the empty values with your own API keys where required.

You don’t need to configure every provider. Add the sources you have access to and want to use.

***Important:*** *Never publish your real API keys in a public repository, screenshot, or article.*

Now, **See the difference in the results.** 👌
