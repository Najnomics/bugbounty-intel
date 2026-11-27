# Bypassing 4-Digit MFA — A HackSmarter Lab Writeup

- **Source URL:** https://medium.com/@cyberologist-bd/bypassing-4-digit-mfa-a-hacksmarter-lab-writeup-873052edf5de?source=rss------bug_bounty-5
- **Fetched from:** https://medium.com/feed/@cyberologist-bd
- **Fetched:** 2026-11-27
- **Channel:** @dailybountywriteup
- **Telegram message:**  (id 13416)
- **Method:** medium-rss-content readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
**Platform:** [HackSmarter](https://www.hacksmarter.org/catalog)

**Challenge:** Bypass MFA

**Difficulty:** Beginner

**Tools Used:** Burp Suite Community Edition, OpenVPN

### Objective

Bypass a 4-digit MFA code on a login page using only a valid set of credentials.

**Given credentials:**

- Username: Tony
- Password: basketball

### Setup

After downloading the VPN configuration file from the course dashboard, I connected to the lab network:

sudo openvpn foundations\_of\_web\_app\_pentesting.ovpn

Once the terminal showed Initialization Sequence Completed, the lab machine was reachable. The target IP assigned was 10.1.221.228.

### Reconnaissance

Navigating to http://10.1.221.228 loads a login page at /login. Nothing unusual — a standard username and password form.

I logged in with Tony’s credentials.

Access granted immediately, no MFA prompt yet. That tells us MFA is optional and disabled by default on this account.

### Setting Up the Target

Under Tony’s profile, I found a **General Settings** section with a checkbox to enable 2FA.

I checked it and saved. Then I logged out.

Logging back in with the same credentials now triggers a new screen.

A 4-digit verification code, sent to Tony’s device.

But, I am not Tony.

So, I do not have his device as well as I do not have the code.

Umm.. Lets put a random code, e.g: 1234

Incorrect 2FA — sure thing as expected.

### The Attack — Brute Forcing the MFA Code

### Step 1 — Intercept the request

I opened Burp Suite, went to the **Proxy** tab, and turned **Intercept On**.

Back in the browser, I entered a dummy code (1234) and clicked **Verify**.

Burp caught the request.

The **POST** body contained the code parameter. That is our target.

### Step 2 — Send to Intruder

With the request sitting in the Proxy intercept panel, I pressed Ctrl + I to send it to **Intruder**, then clicked **Forward** to let the browser continue.

### Step 3 — Configure the attack

In the **Positions** tab, I clicked **Clear §** to remove all of Burp’s auto-guessed positions.

Then manually highlighted the value of the code parameter and clicked **Add §**. Now only the code field is marked for brute-forcing or fuzzing.

In the **Payloads** tab, I configured the following:

- **Attack type:** Sniper — one payload set, one position. The right choice when you are targeting a single field.
- **Payload type:** Numbers.
- **Range:** 0000 to 9999. Type (sequential or random) doesn’t matter.
- **Min/Max integer digits:** 4 — this ensures Burp sends 0001 rather than 1, which matters because the server expects a zero-padded 4-digit string.

### Step 4 — Start the attack

After double-checking everything, I clicked **Start Attack** and let Burp run through all 10,000 possibilities.

### Analysing the Results

Once the attack finished, I sorted the results by **Status Code**.

Every single request returned 200 OK , except one, which returned 302 Found. A 302 is a redirect, and in the context of a login flow, a redirect means success. The server accepted the code and sent the browser somewhere else.

The winning payload: **8467**

I confirmed this by clicking that request and checking the **Render** tab. The response showed Tony’s authenticated session.

### Getting In

I turned Intercept off, navigated to http://10.1.221.228/mfa, typed 8467, and submitted.

Done. Full access to Tony’s account, **MFA bypassed.**

### What Made This Possible

**Four** things went wrong on the server side, and any one of them alone would have made this attack significantly harder or impossible.

1. **Short code length:** A 4-digit code gives an attacker exactly 10,000 values to try. That is not a large number. Bump it to 6 digits and the search space becomes 1,000,000. Bump it to 8 and it becomes 100,000,000. Length directly controls how long a brute force takes and at 4 digits, it barely takes any time at all.

**2. Numeric-only characters:** Restricting the code to digits further shrinks attacker effort. A 4-character code mixing letters and numbers has over 1.6 million possible values. A 4-digit numeric code has 10,000. The character set choice matters as much as the length.

**3. No rate limiting:** The server accepted all 10,000 requests without ever blocking the source IP, locking the account, or slowing down. A proper implementation locks the account after three to five failed attempts — the same way banks work. Without that, an attacker with enough patience and a wordlist will always get through eventually.

**4. No token expiry:** The MFA code stayed valid for the entire duration of the attack. Real MFA codes expire in 30 to 60 seconds, which makes a 10,000-request brute force mathematically impossible to complete in time. A code that never expires is barely a second factor. It is just a second password, and a short one at that.

Together, these four failures turned a security feature into a checkbox with no real enforcement behind it.

### Takeaway

MFA is only as strong as its implementation. Slapping a verification step onto a login page means nothing if the code is four digits long, numeric only, never expires, and the server will happily accept ten thousand guesses without blinking.

When you are testing applications, do not just check whether MFA exists. Check how it was built. Look at the code length, the character set, whether failed attempts trigger any lockout, and how long the token stays valid. Each of those is a separate control, and each one can fail independently. In this lab all four failed at once which is why a standard Burp Intruder run with a number list was enough to get in.

*Lab completed on HackSmarter — Foundations of Web App Pentesting.*

**Happy hacking!**
