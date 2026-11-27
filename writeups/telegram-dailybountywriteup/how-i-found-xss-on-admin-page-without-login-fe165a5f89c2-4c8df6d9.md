# How I found XSS on Admin Page without login!

- **Source URL:** https://sl4x0.medium.com/how-i-found-xss-on-admin-page-without-login-fe165a5f89c2?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20251012181124/https://sl4x0.medium.com/how-i-found-xss-on-admin-page-without-login-fe165a5f89c2
- **Fetched:** 2026-11-27
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/1478 (id 1478)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# How I found XSS on Admin Page without login!

## Introduction

بسم الله الرحمن الرحيم

Hello Awesome Hackers, this is my first Write-Ups in Real Target; I will explain how Fuzzing helped me get an XSS on Admin Page Just in 1 Minute!

## Approaching

I am doing Bug Bounty Hunting On Open-Source Projects; As I like doing this and giving back support to these projects and its community!

So I chose an Application running PHP as I can understand its code!

I Begin with collecting Subs and Endpoints to map the full Application to have a full picture of how it works and what its capabilities are!

## Interesting Endpoint

When I am checking the collecting results; Actually i check it with *CTRL+F* to find interesting keywords like *admin*, *panel*, *dev*, *internal* ..etc.

While doing this, I found this Link:

[https://redacted.redacted.com/admin/login](https://demo.redacted.com/admin/login)
Trying Some Dumb Default Password and SQLi Payload; with no Successfully Login or Bypassing!

## Fuzzing

So I start Fuzzing Using *Arjun* as I can find any Parameter But when I do this I found a really helpful error 🤓

*Arjun* just pushed a helpful error as I didn’t skip it so let’s try combining the full URL; then injecting XSS Payload!

## Exploitation

The full URL with the Payload becomes:

[https://redacted.redacted.com/admin/login?perspective=asdf1234](https://redacted.redacted.com/admin/login?perspective=asdf1234)
After Submitting and Viewing the Source code:

`https://redacted.redacted.com/admin/login?perspective=asdf"onload%3d"alert('Slax Was Here!')"asdf`
SUBMITTING!!


## Wrapping Up

Remember the one rule

 *“Fuzzing, Fuzzing, Fuzzingggg”*

I hope you guys enjoyed the Write-Up, See you on the Other one!
