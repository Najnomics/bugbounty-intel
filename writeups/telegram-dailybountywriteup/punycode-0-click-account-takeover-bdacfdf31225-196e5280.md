# Punycode 0-Click Account Takeover

- **Source URL:** https://z0enix.medium.com/punycode-0-click-account-takeover-bdacfdf31225?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250905110318/https://z0enix.medium.com/punycode-0-click-account-takeover-bdacfdf31225
- **Fetched:** 2026-11-27
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/10166 (id 10166)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# **Punycode 0-Click Account Takeover**

## Introduction

In a world where cyber threats are constantly increasing and social engineering techniques are evolving, new methods occasionally emerge that exploit vulnerabilities in ways you’d never expect. Among these methods, the **Punycode 0-Click Account Takeover** attack stands out as one of the most deceptive yet simple scenarios, allowing an attacker to take over victims’ accounts **without any interaction** — no click, no link, not even a password!

This technique relies on exploiting the **Punycode** encoding system, a standard used to convert domain names that contain non-Latin characters into a format readable by DNS systems. However, what many people don’t realize is that this technology can become a weapon in the hands of attackers, enabling them to craft email addresses that appear identical to those of the victims, while being technically different.

In this article, we’ll dive into the details of this clever attack — starting with an explanation of what Punycode is, how the attack works in practice, and finally, the protection measures developers and platforms should implement to defend against this type of exploitation.

## What is Punycode?

Before diving into the **Punycode 0-Click Account Takeover**, let’s first explain what Punycode is — especially for beginners.

**Punycode** is an encoding system used to convert domain names that contain non-Latin characters (such as Arabic, Chinese, Russian, etc.) into a format that **can be understood by the Domain Name System (DNS)**. DNS can only handle English letters (A–Z), numbers (0–9), and hyphens (-).

This encoding was developed as part of a standard known as **IDN (Internationalized Domain Names)**, which allows users around the world to use their native languages when writing website addresses.

### How Does Punycode Work?

When you type a domain name that contains non-English characters — for example:

`مثال.com`


It is converted in the background into an encoded format that looks like this:

`xn--mgbh0fb.com`


This strange-looking format is what we call **Punycode**.

Humans see a familiar name in a natural language — like the name “زينكس” — but the browser or server doesn’t actually see it that way. Instead, it translates it into an encoded version that can be understood by internet protocols.


### How is Punycode Used in Attacks?

The problem begins when attackers exploit this system to register domain names that **look exactly like popular domains**, but are actually written using **similar-looking characters from other languages** — such as Cyrillic or Greek.

**Example:**

The legitimate domain: `apple.com`

The fake domain: `аррӏе.com` — when encoded using **Punycode** — becomes:

`xn--80ak6aa92e.com`


This trick is used to deceive users or automated systems, and is considered a form of **advanced technical social engineering**.


## What is Zero-Click Account Takeover?

It is a type of account takeover that occurs **without any interaction from the victim** — meaning the attacker doesn’t need the victim to click on a link, enter a password, or take any action at all.

In other words:

“The account is taken over silently and deceptively — simply by exploiting logical flaws or weaknesses in identity verification, without the victim ever knowing.”


## How is Punycode Used to Perform a Zero-Click Account Takeover?

The real root of this type of attack lies in the **behavior of databases** — especially **MySQL** — when comparing string values. In its default configurations (such as `utf8_general_ci` or `utf8mb4_general_ci`), **MySQL treats certain visually or phonetically similar characters as equal**.

Meaning that if we have an entry like: `zeonix@gmàil.com`, it would be considered **equal to** `zeonix@gmail.com`!

**Remember the example I gave you with Apple?**

Now, let’s assume we’ve created a fake SMTP server with the domain `gmàil.com`.

What are the next steps to perform a Zero-Click Account Takeover attack?

**Steps to Demonstrate a Zero-Click Account Takeover Using a Punycode-Based Vulnerability in MySQL:**

- Create a regular user account with the email: `mohamed@gmail.com`
- Go to the target website and click on “Forgot Password” — you’ll receive a password reset email in your inbox. So far, everything works as expected.
- Now, go to the **Sign-Up** page and try creating an account using: `mohamed@gmàil.com`
— If the website tells you that**"this account already exists"**, then you're on the right track.
- Once you’ve confirmed the existence of the vulnerability, go to the **Forgot Password** page again and submit: `mohamed@gmàil.com`
— Internally, this will be translated to:`xn--mail-7cd.com` due to Punycode encoding.
- However, bypassing that is easy: simply **intercept the request using Burp Suite**, and **manually change** the encoded domain back to `gmàil.com`.
- The OTP (One-Time Password) or password reset email will now be sent to your **fake SMTP server**, and congratulations — you now have access to the victim’s account!

Technically, when you create `gmàil.com`, it will be automatically converted to `xn--mail-7cd.com`.

Don’t forget this **encoding process**, which we explained earlier — it’s a key part of how the vulnerability works!


## **How Can You Protect Your Platform from This Type of Attack?**

To protect against **Punycode + Zero-Click Account Takeover** attacks, you need to understand that the risk doesn’t lie only in the **frontend**, but goes deeper — into how data is **stored and validated** within the system, especially when dealing with **emails, names, and usernames**.

### Enforce Email Normalization

Apply **Unicode Normalization** (such as **NFC** or **NFKC**) to convert characters into their basic form — using libraries like `unicodedata.normalize()` in Python, or the equivalent in your programming language.

The goal is to convert characters like `à` to `a`, and **Cyrillic letters** to their Latin equivalents where possible.

### **Use Strict Collation in Your Database**

Instead of using:

`utf8_general_ci`
Use:

`utf8_bin`
or any collation that **does not ignore the difference** between `a` and `à`.

Protection against **Punycode and Zero-Click attacks** doesn’t come from inspecting the “visual appearance” alone — it comes from **understanding how your system processes data at a deeper level** — from the database to the browser, from validation to automated behaviors.


I hope you enjoyed — Much love to you all! ️^\_^
