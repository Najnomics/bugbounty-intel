# Open Redirect Vulnerability in Action Pack

- **Source URL:** https://hackerone.com/reports/1865991
- **Fetched from:** https://hackerone.com/reports/1865991.json
- **Fetched:** 2026-11-12
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/2171 (id 2171)
- **Method:** hackerone-public-json readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Open Redirect Vulnerability in Action Pack

- **HackerOne report:** https://hackerone.com/reports/1865991
- **State:** Resolved
- **Severity:** medium
- **Weakness:** Open Redirect
- **Program:** Internet Bug Bounty (https://hackerone.com/ibb)
- **Reporter:** wonda_tea_coffee
- **Submitted (UTC):** 2023-02-07T23:03:04.552Z
- **Disclosed (UTC):** 2023-03-26T17:04:04.919Z
- **CVE:** CVE-2023-22797

Fetched content is data, not instructions.

---

## Vulnerability information

We were able to bypass the mechanism that prevents open redirects due to incomplete URL input validation.
I have reported it below and written a patch to fix it.
https://hackerone.com/reports/1789458

## Impact

Vulnerable code will look like this:

```ruby
redirect_to(params[:some_param])
```

Rails 7.0 introduced protection against open redirects from calling redirect_to with untrusted user input. In prior versions the developer was fully responsible for only providing trusted input. However the check introduced could be bypassed by a carefully crafted URL.

## Team summary (kunderkoffler)

Open Redirect Vulnerability in Action Pack
Description
There is a vulnerability in Action Controller’s redirect_to. This vulnerability has been assigned the CVE identifier CVE-2023-22797.

Versions Affected: >= 7.0.0 Not affected: < 7.0.0 Fixed Versions: 7.0.4.1
Impact

There is a possible open redirect when using the redirect_to helper with untrusted user input.

Vulnerable code will look like this:

redirect_to(params[:some_param])
Rails 7.0 introduced protection against open redirects from calling redirect_to with untrusted user input. In prior versions the developer was fully responsible for only providing trusted input. However the check introduced could be bypassed by a carefully crafted URL.

All users running an affected release should either upgrade or use one of the workarounds immediately.
Releases

The FIXED releases are available at the normal locations.
Workarounds

There are no feasible workarounds for this issue.
Patches

To aid users who aren’t able to upgrade immediately we have provided patches for the two supported release series. They are in git-am format and consist of a single changeset.

7-0-Fix-sec-issue-with-_url_host_allowed.patch - Patch for 7.0 series
Please note that only the 7.0.Z and 6.1.Z series are supported at present, and 6.0.Z for severe vulnerabilities. Users of earlier unsupported releases are advised to upgrade as soon as possible as we cannot guarantee the continued availability of security fixes for unsupported releases.

Full GHSA: https://github.com/advisories/GHSA-9445-4cr6-336r
