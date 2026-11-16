# http://surge.sh/

- **Source URL:** http://surge.sh/
- **Fetched from:** https://surge.sh/
- **Fetched:** 2026-11-16
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/3740 (id 3740)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Publish to the web in one command.

Surge puts a folder of static files on a global network, with HTTPS, at a surge.sh name or your own domain—straight from your terminal, your CI, or your coding agent.

$ `npm install --global surge`
$ `surge ./dist example.surge.sh`

Using a coding agent? Point it at [surge.sh/docs/agents](https://surge.sh/docs/agents).

- 18,791,349deployments
- 242.30 TBpublished
- 3,832,699projects

Live totals. Each pill is a real publish happening now—anonymized, sizes and speeds only.

## Build, publish, live.

Surge doesn't build your project or ask you to describe it. You build the way you already do, and hand Surge the output.

1. ### Build Any tool that writes static files: Vite, Astro, Eleventy, Hugo, or a folder you wrote by hand. $ `npm run build`
2. ### Publish The directory and the domain, as arguments. No config file, and no prompts once you're logged in. $ `surge ./dist lucid-example.surge.sh`
3. ### Live Uploaded, cut over atomically, and served from every region before the command returns. HTTPS is immediate on surge.sh and follows DNS on your own domain. Every publish is a revision you can roll back to.

$ surge ./dist lucid-example.surge.sh
   Running as you@example.com (Free)
        project: ./dist
         domain: lucid-example.surge.sh
           size: 3 files, 672 bytes
         upload: \[=========================\] 100%
            CDN: \[=========================\] 100%
     encryption: \[=========================\] 100%
  ┌──────────┬────────────────────────────────────────────────────────────────┬───────────────────────┐
  │   CERT   │   \*.surge.sh, surge.sh                                         │   auto-renew          │
  ├──────────┼────────────────────────────────────────────────────────────────┼───────────────────────┤
  │   DNS    │   using Surge Name Servers                                     │   geo-aware           │
  └──────────┴────────────────────────────────────────────────────────────────┴───────────────────────┘
  ┌──────────┬──────────────────┬───────────────────────┬─────────────────────┬─────────────┬─────────┐
  │   HTTP   │   sfo.surge.sh   │   US, San Francisco   │   138.197.235.123   │   D.Ocean   │   ✔ ◍   │
  │   HTTP   │   lhr.surge.sh   │   GB, London          │   46.101.67.123     │   D.Ocean   │   ✔ ◍   │
  │   HTTP   │   yyz.surge.sh   │   CA, Toronto         │   159.203.50.177    │   D.Ocean   │   ✔ ◍   │
  │   HTTP   │   jfk.surge.sh   │   US, New York        │   159.203.159.100   │   D.Ocean   │   ✔ ◍   │
  │   HTTP   │   ams.surge.sh   │   NL, Amsterdam       │   188.166.132.94    │   D.Ocean   │   ✔ ◍   │
  │   HTTP   │   fra.surge.sh   │   DE, Frankfurt       │   138.68.112.220    │   D.Ocean   │   ✔ ◍   │
  │   HTTP   │   sgp.surge.sh   │   SG, Singapore       │   139.59.195.30     │   D.Ocean   │   ✔ ◍   │
  │   HTTP   │   blr.surge.sh   │   IN, Bangalore       │   139.59.50.135     │   D.Ocean   │   ✔ ◍   │
  │   HTTP   │   syd.surge.sh   │   AU, Sydney          │   45.76.126.95      │   Vultr     │   ✔ ◍   │
  │   HTTP   │   nrt.surge.sh   │   JP, Tokyo           │   172.104.96.133    │   Linode    │   ✔ ◍   │
  └──────────┴──────────────────┴───────────────────────┴─────────────────────┴─────────────┴─────────┘
   Live preview ................................................ 1785787164375--lucid-example.surge.sh
   Latest ............................................................. latest--lucid-example.surge.sh
   Production ................................................................. lucid-example.surge.sh
   Success! - Published to lucid-example.surge.sh
   domain written to dist/CNAME

## What you don't have to do.

Surge does one job: it puts static files on the web and keeps them there. Everything it leaves out is something you don't have to learn, configure, or pay for.

- **No config file.**A directory is the project and the domain is an argument. The CLI remembers it in a one-line `CNAME` file.
- **CLI native.**Domains, certificates, tokens, orgs, rollbacks: every operation is a command you can script.
- **No build service.**Build where you already build—your laptop, your CI, your agent's sandbox. Surge publishes the result.
- **No servers to size.**Static files, served from ten regions. Nothing to scale, patch, or keep warm.
- **No lock-in.**It's your files, in your repository. `surge my-app.surge.sh teardown` takes them down; nothing else to export.
- **No surprise charges.**Free includes custom domains and certificates. If you upgrade, the bill is the plan price, always.

## The parts that matter once it's real.

Previews, rollbacks, domains and certificates—each one a command, each one documented down to the output.

### [Preview before production](https://surge.sh/docs/cli/previews)

$ `surge ./dist my-app.surge.sh --preview`

Uploads a revision to its own URL, like `1785787164375--my-app.surge.sh`, without touching production. Cut it over when it's right.

### [Revisions and rollback](https://surge.sh/docs/cli/revisions)

$ `surge my-app.surge.sh rollback`

Every publish is a revision and production switches atomically. The last 100 are kept, so rollback, roll-forward and cutover are instant.

### [Custom domains, free](https://surge.sh/docs/platform/custom-domains)

$ `surge ./dist example.com`

Point a CNAME at `geo.surge.world`, add an A record, or delegate to Surge's name servers. Free on every plan.

### [Certificates, managed](https://surge.sh/docs/platform/ssl)

$ `surge ./dist example.com --force https`

Certificates are issued as soon as your domain points at Surge and renewed automatically. `--force https` redirects plain HTTP.

### [Single-page apps](https://surge.sh/docs/platform/spa-routing)

$ `cp dist/index.html dist/200.html`

A `200.html` serves every unknown path, so client-side routes deep-link. Add `404.html` for your own not-found page. Clean URLs are automatic.

### [Tokens for CI and agents](https://surge.sh/docs/cli/automation)

$ `surge tokens add --domain my-app.surge.sh`

A token scoped to one domain. Set `SURGE_TOKEN` and nothing prompts; without credentials the CLI exits non-zero instead of waiting.

## Publish the output directory.

Surge serves whatever your build writes. These are the directories to hand it.

| Project | Output | Publish | Guide | 
|---|---|---|---|
| Vite (React, Vue, Svelte) | `dist` | `surge ./dist my-app.surge.sh` | [Guide](https://surge.sh/docs/guides/vite) | 
| Astro | `dist` | `surge ./dist my-app.surge.sh` | [Guide](https://surge.sh/docs/guides/astro) | 
| React or Vue single-page app | `dist` | `cp dist/index.html dist/200.html` | [Guide](https://surge.sh/docs/guides/spa) | 
| Eleventy | `_site` | `surge ./_site my-docs.surge.sh` | [Guide](https://surge.sh/docs/guides/eleventy) | 
| Hand-written HTML | `.` | `surge . my-page.surge.sh` | [Guide](https://surge.sh/docs/getting-started) | 
| A single HTML file | `page.html` | `surge page.html my-page.surge.sh` | [Guide](https://surge.sh/docs/cli/publishing) | 
| GitHub Actions | — | A preview for every pull request | [Guide](https://surge.sh/docs/guides/github-actions) | 

Surge hosts static files: HTML, CSS, JavaScript, images, fonts, media. It doesn't run server code, functions or databases—pair it with an API you host elsewhere.

## An agent needs what a script needs.

A token, a command that never stops to ask, and a URL at the end. That's all Surge has ever been, which is why coding agents already reach for it.

- **Scoped tokens.** The human mints a token for one domain; the agent can't touch anything else.
- **Preview first.** `--preview` gives the agent a URL to show you; production moves only when you say so.
- **Fails loudly.** No credentials and no terminal means an error and a non-zero exit, never a hang.
- **Readable docs.** Every docs page is also served as markdown, and [llms.txt](https://surge.sh/llms.txt) indexes them.

\# the human, once
$ surge tokens add --domain my-app.surge.sh -m "coding agent"
# the agent, every time
$ export SURGE\_TOKEN=\<token>
$ npm run build
$ npx surge ./dist my-app.surge.sh --preview
   Success! - Preview available at 1785787164375--my-app.surge.sh
# only after you approve
$ npx surge my-app.surge.sh cutover 1785787164375

## Built to be depended on.

Surge has published the same way for over a decade. The evidence is public, and most of it is live.

- 2014The [surge](https://www.npmjs.com/package/surge) CLI's first release on npm. `surge` still publishes the way it did then.
- 18M+Deployments, counted live at the top of this page, across more than 3.8 million projects.
- 10 regionsServing every project, with each region's status and uptime on the [network page](https://surge.sh/network).
- 100k+Installs of the CLI from npm every month.

In the open: projects that publish to Surge from their public CI. Each name links to the workflow that does it.

**Serving is sacred.**

Limits pause publishing, never serving. A project that's live stays live.


**No surprise charges.**

No metered bandwidth, no overages. The bill is the plan price.


## Publish something now.

Free, including custom domains and certificates. Pro adds password protection and redirects for $30 a month.

$ `npx surge`
