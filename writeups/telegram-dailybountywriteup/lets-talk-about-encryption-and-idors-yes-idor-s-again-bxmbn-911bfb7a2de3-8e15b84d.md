# Let’s Talk About Encryption And IDORs(Yes, IDOR,s Again)— @bxmbn

- **Source URL:** https://bxmbn.medium.com/lets-talk-about-encryption-and-idors-yes-idor-s-again-bxmbn-911bfb7a2de3?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20251014112843/https://bxmbn.medium.com/lets-talk-about-encryption-and-idors-yes-idor-s-again-bxmbn-911bfb7a2de3
- **Fetched:** 2026-11-27
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/8878 (id 8878)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Let’s Talk About Encryption And IDORs (Yes, IDORs Again)— @bxmbn

Imagine a system designed to protect sensitive user data — like insurance policies — only to have a single misstep turn it into an open book. That’s exactly what I stumbled upon while poking around a certain event registration protection service. What started as curiosity about an API endpoint spiraled into a discovery that could grant complete access to any user’s policy. Here’s how it unfolded, step by step, and why it matters.

## The Discovery: An API with a Secret

It all began with a website that stores user policies — think of it as a digital filing cabinet for insurance plans. While exploring, I found that there was an API call to: **/api/claims/encrypt?text=EUSP2386411060** with my Insurance Policy there (**EUSP2386411060**) and the response was the encrypted value of my policy ID, this value gives access to the policy

So in short, if your policy is **EUSP2386411061** I can encrypt it and basically access your insurance policy as the encrypted value is used to access a PDF file containing your policy Information..

## **Cracking the Code: A Step-by-Step Breakdown**

Let’s walk through how this works. say **EUSP2386401065** is your Policy ID

**Step 1: Encrypting the Policy ID**

Using a simple HTTP GET request, the attacker sent the policy ID to the encryption endpoint. Here’s what it looked like:

```
GET /api/claims/encrypt?text=EUSP2386401065 HTTP/2
Host: [redacted-]
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:122.0) Gecko/20100101 Firefox/122.0
Accept: application/json, text/plain, */*
```
The response? A neat little encrypted string: ***BnmnNGD6EFL2Eeo85nTHA***.

**Step 2: Unlocking the Policy**

Next, the attacker takes that encrypted string and plugged it into: /**api/certificates/policies/*{e*ncrypted\_string\_from\_step\_1}** Like so:

/api/certificates/policies/*BnmnNGD6EFL2Eeo85nTHA*

Boom — The PDF popped up, confirming the details of your policy **EUSP2386401065**. Full names, Date of birth, Addresses, but most importantly the Dates and coverage since these will allow the attacker to then authenticate..

**Step 3: Taking Control**

Here’s where it gets downright eerie. Armed with the policy ID and a purchase date from the PDF, I headed to the service’s management portal. I selected “Policy Number” from the login options, entered **EUSP2386401065**, picked “Purchase Date,” and typed in the date from the policy details. Just like that, I was in — full access to manage or even take over the policy.

The kicker as mentioned, This wasn’t a one-off. The policy IDs follow a numeric pattern, meaning you could feasibly encrypt any ID, get its access key, and repeat the process for every user in the system.

**The Flaw: Encryption as a Weak Link**

So, what’s going on here? The system uses the same encryption algorithm for every policy ID, and the encrypted output doubles as an access key. There’s no additional verification — no secret handshake, no second factor. If you can guess or obtain a policy ID (and they’re sequential), you can encrypt it, grab the key, and waltz into the policy vault. It’s like locking a safe with a key that’s printed on the outside.

**The Stakes: Why This Matters**

The impact is staggering. This isn’t just a peek at someone’s insurance plan — it’s complete access. An attacker could view, modify, or even cancel policies, all without the user’s knowledge. For a service handling potentially thousands of users, this is a skeleton key to the entire database. Personal data, financial details, event plans — all up for grabs.

**The Bigger Picture**

This isn’t about pointing fingers at a specific company (hence the redactions). It’s a wake-up call for how we design and secure systems. Encryption is powerful, but when it’s the only gatekeeper — and a predictable one at that — it’s not enough. Sequential IDs, exposed endpoints, and lax access controls are a recipe for trouble.

I reported this responsibly, but it’s a reminder: the smallest oversight can turn a fortress into a house of cards. Next time you trust a service with your data, ask yourself — what’s stopping someone from finding the key?

Thank you for reviewing this Writeup! . I will also be Answering any Questions in [https://x.com/bxmbn](https://x.com/bxmbn)
