# How I Found an Account Takeover Bug in the Forgot Password Flow

- **Source URL:** https://medusa0xf.medium.com/how-i-found-an-account-takeover-bug-in-the-forgot-password-flow-49dbc82311f5?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250828042028/https://medusa0xf.medium.com/how-i-found-an-account-takeover-bug-in-the-forgot-password-flow-49dbc82311f5
- **Fetched:** 2026-11-23
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/10662 (id 10662)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
Member-only story

# How I Found an Account Takeover Bug in the Forgot Password Flow

## Introduction

While I was hunting on a target, I came across an acquisition related to it, so I decided to look around the new domain. It immediately caught my eye because it was an e-commerce application with registration and login functionality.

My approach was to first browse the application like a normal user while keeping Burp Suite running to observe the requests and responses. I created an account, completed email verification, and explored the various functionalities inside.

That’s when I found a critical vulnerability, the password reset token was exposed directly in the API response, which could easily lead to a full account takeover.

## What’s the flow of password reset functionality?

A **password reset** is the process that lets a user set a new password when they forget their old one (or want to change it for security reasons).

In most applications, the flow looks like this:

1. User clicks *“Forgot Password”*.
2. The app asks for their…
