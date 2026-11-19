# Broken Access Control to Gain Unauthorized Role Management in a Public Program

- **Source URL:** https://medium.com/@bassemwanies2002/broken-access-control-to-gain-unauthorized-role-management-in-a-public-program-6925f83d0dc4?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250905182753/https://medium.com/@bassemwanies2002/broken-access-control-to-gain-unauthorized-role-management-in-a-public-program-6925f83d0dc4
- **Fetched:** 2026-11-19
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/10279 (id 10279)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Broken Access Control to Gain Unauthorized Role Management in a Public Program

قَالَ اللَّهُ تَعَالَى: {يَرْفَعِ اللَّهُ الَّذِينَ آمَنُوا مِنكُمْ وَالَّذِينَ أُوتُوا الْعِلْمَ دَرَجَاتٍ ۚ وَاللَّهُ بِمَا تَعْمَلُونَ خَبِيرٌ} (سورة المجادلة، الآية 11).

## ✍️ About Me

I’m Bassem (AKA. **satan11**), a bug bounty hunter and aspiring penetration tester. I publish real-world writeups to help others learn from the bugs I find in live programs.

## 📌 Summary

In this writeup, I’ll walk you through how I discovered an **improper access control vulnerability** in a public bug bounty program. The vulnerability allowed a low-privileged **Backoffice Editor** to gain access to a restricted roles management endpoint — and not just view it, but also **create, edit, and delete user roles** that should have been off-limits.

The issue was caused by **over-privileged JWT permissions**, granting access beyond the intended scope.

## 🕵️♂️ Target Endpoint (Redacted):

`/development/entitlements/roles`

## 👨💻 Affected Role:

`Backoffice Editor` — meant to be limited to basic admin/backoffice operations.

## 🧪 Technical Breakdown & Reproduction Steps

*The vulnerability stemmed from the JWT token assigned to the Backoffice Editor, which contained elevated permissions:*


```
"dp.entitlements.plans.read",
"dp.entitlements.plans.write"
```
These were enough to bypass UI-level restrictions and interact directly with sensitive backend APIs.

### ✅ Steps to Reproduce:

1. **Login as a Backoffice Editor**
2. **Visit the entitlements section. You’ll see a message like:**

*| “Roles & permissions module is currently disabled.” |*

3\. **Intercept and send a manual POST request** to the role creation endpoint:

Observe the successful creation of the role:

## 🎯 Impact

This vulnerability allowed:

- Unauthorized access to the **entitlements/roles** module
- Creation of arbitrary roles
- Modification or deletion of existing roles

Such access **breaks the principle of least privilege** and could lead to privilege escalation or broader security misconfigurations in a real-world deployment.

## 🧩 Root Cause

- Backend relied **entirely on JWT claims** for access control.
- No **role-based access enforcement** at the endpoint level.
- Frontend “disabled” UI provided a false sense of restriction.

Eventually it was triaged as duplicate:
