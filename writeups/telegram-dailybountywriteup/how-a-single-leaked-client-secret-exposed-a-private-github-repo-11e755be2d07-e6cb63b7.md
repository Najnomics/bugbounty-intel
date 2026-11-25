# How a Single Leaked Client Secret Exposed a Private GitHub Repo

- **Source URL:** https://s5treak.medium.com/how-a-single-leaked-client-secret-exposed-a-private-github-repo-11e755be2d07
- **Fetched from:** https://s5treak.medium.com/how-a-single-leaked-client-secret-exposed-a-private-github-repo-11e755be2d07?source=rss-4095a823e1b1------2
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14969 (id 14969)
- **Method:** medium-rss-feed (full content:encoded) readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- **Author/Published (RSS):** Prosper Kalu / Tue, 03 Nov 2026 20:14:13 GMT

During a recent assessment, I turned a single hardcoded secret found in a public JavaScript bundle into **administrative access to the target’s private GitHub repository**. The chain took four unauthenticated steps:

hardcoded OAuth app secret (public JS)

→ mint an app access token

→ enumerate webhook callback URLs (internal hosts leak)

→ hit a leaked webhook → production debug page

→ git remote in the debug page contains an admin-scoped GitHub PAT

No user interaction, no victim, no privileged account. Just the public bundle.

The app’s frontend bundle shipped an **OAuth App Secret** in plaintext. Secrets like this are server-only by definition — the browser can’t use them without exposing them.

curl -s "https://graph.example.com/oauth/access\_token?client\_id=REDACTED&client\_secret=REDACTED&grant\_type=client\_credentials"

# {"access\_token":"REDACTED|…","token\_type":"bearer"}

**Step 1 done.** I now had a valid app token — authenticated as the company’s own application. — -

App tokens are supposed to be low-value. But with this one, the provider’s API happily returned the app’s **webhook subscriptions** — including internal callback URLs:

One of the webhook URLs returned an **HTTP 500 with a full laravel framework debug page** when hit with a plain GET.

Framework debug pages often embed a JSON “report” with app metadata — including the deployed app’s **git remote URL**. In this case, the remote had a **Personal Access Token baked into it**:

I confirmed the token without touching source code:

This was found during authorized testing. I validated the token with **metadata-only API calls** — no source code was read or modified — and the organization revoked the token and rotated their secrets after disclosure.
